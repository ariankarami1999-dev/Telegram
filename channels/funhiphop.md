<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/V61L43q0nImIsHRYq_7RCc-ncKEqHkzfC0Fm0BL1WmzxTMLE5DRQmYV7J6-kQh-liRw466den72GUPIVqC0P9vrozOi--QFzApqvpwKmTM4XYCU2LAosmaAkRuDXsko0pvQw1qY7ThWoFXQ6rBJSJBI4aTe70ooD0O4mDX5w5nnmExERxPB3VaIwSMWfxI9Z1uEFyiBIE9ZxWjME_9Ohg1mS8atRmhbovkHsUCR_LDIPEVcFfFEwFh1EWlK70vJMdrW3gfljAVn7qIAwX6HV_TuCflvjpCC7QTOP1phNaA7jcZE1bDV7fNg3da9sbAsJfUa4h3KAI2qm7AjMkAhmHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 18:42:20</div>
<hr>

<div class="tg-post" id="msg-82281">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/funhiphop/82281" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82278">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXz6SGaG1sAaCHfEv96El6hf-6VpqccIkMhvYwhBDTdqHsF9IUjH0K0kah_ELv29eIJEKJ4OjMGi-E9DqVAwOwSRFFWGXskI-UIpNczTfr3itTfcZ9p_qB4BHIVa9idMi4Xz0dArqqYmALTdzaGPlBrPA8Nf6s03K5AkRqYOOqzxB_YPxmR8Kzy7GX9LFU7-QkVka501EBXAfpEyJWjMMbD3n51D6X6dkE7Gh5_oN5sI_DfVldKeXz_cK7z4GxP0S4lgHQRdkRvkGzbQWVIPOYF3hvG8QLHx_KOOCzK08W-BM-E7WikAXdxzniEBLGBQr_1Hz_Xx9upB66_WVKE7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RxY5CXgOK4PydZSAg3SHHY1sMdAXitIQTKsG6gpbR5Q-FVa0ZBcZyt9AsLueDweLYzSUWAzmIORg66ig4R_uvZ_-Ucb44VRLsAO9o0omqpXL7PgpSs6_75jTf5EjZ5_A1XRzB2B7A9vBODxSgQFdhfSyIQCsR1FckMVLVQI0AAk7d2IcyBXam6S_ocaKfxvQLLqMadPJTKrS59ThHE8ScPzBW5JlOA8DeE3ymIP7wgIidjkFTQVAVVpmv4ai2fzh9z5RqIboDt2EJxgLsDvonHZuXOY_KOQodtKS5xZsyStjGSTkzu9CeLdE_XfQV3_ejhshwOFtM2JqD8MZRoe-Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید چرسی تو چنلش
تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/funhiphop/82278" target="_blank">📅 18:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82277">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQIptDoKqaEIPbp7TLAw8NkJge_w05aLArzNSbNQYdcL03z9l1wWpea1DNvfn39w81zoUd_N-OaIFCHaMKxahjdANhEdNvO-kg4tNQdbYBO5KGE22p_xcrEp47fbUawl1QV-ppVRyH3meA3jopfImP6Q2n4ntMETzIy4Mp3T3V1VDNfuL5W1s5ZfWiekAXe5jkzKoZ7z3c-f5Xu1q8B-xesnFKLPnGuDsZzAdG4OvuAk1jWzujbGLYMvM8BF_bf9UMNiJOGMHgOZXAFxL_A8_d_QHilL2asRRhUT8nD4ZmPChLEyDGxCyZXRjg3gLI2uatn9tYj_lf3Wa3Das7CeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیار این کارو نکن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/funhiphop/82277" target="_blank">📅 18:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82276">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCsje9QCwQ_nDd2oEJjc1PE_rgneKQ839nnmKzqyVEZvNWB5nFjckUigOxSgvOTjmeVZ5HxEja6WL5vyTry0Plcq_oF_KgPuxKSolscBWE0GTncZBlpOvfT0J2Qv7ic2pIV5gWSLLV_n3Vc0oko6F3ufJlWBTi4u--oyvfipn0NWnkYI1_pFqHiz6dfaA7QN0mQUcX_Q0_-xSN0AJdiDt6G7phZGv-6EpeXCe7kKMCcF-vnuW-r_vKyxO20KqDQ5yKvUgMgtMB-R-p3H9nTgVaVXpdpM_7x_4mue-uTt3CfSHhA1ueGie8ZDopTKhRGoRHDl7J5_TWDs-yD1CYjRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لانس
🇫🇷
-
🇫🇷
پاری سن ژرمن
🏆
فینال سوپر جام فرانسه
🇫🇷
🕔
یکشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه بولارت-دللیس
🎲
با بیش از ۵۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لانس در ۱۰
دیدار اخیر خود، ۶ برد و ۲ تساوی کسب کرده و در ۲ بازی شکست خورده است.
✅
پاری سن ژرمن در ۱۰
دیدار اخیر خود، ۴ برد و ۴ تساوی کسب کرده و در ۲ بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر لانس ۳.۳ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر پاری سن ژرمن ۳.۱ گل در هر بازی بوده است.
🧠
خستگی یعنی توقف، نه تصمیم تازه.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r25
💻
@BetForward</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/funhiphop/82276" target="_blank">📅 18:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82275">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عربستان جملات ضد اسرائیلی رو از توی کتابای درسیش حذف کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/funhiphop/82275" target="_blank">📅 17:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82274">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpC9hJtVwDeJdgD0iQA0qK7pGYyoXpU2VY-giKgpFOh510PCokpbSbSJJDyEu5C0iXYE_bULmrA4BPb2fpY7m9YysF93VrEHETlHHvuc_OnEa-CadDK6wvjNl0ndwEZeDGjinX1CuRe7h3CobaD7khgHBr3UlMyO3QDFP5tIOvZy8rZLg7FCQ5_IFL-ThBaPseV7Tyb8KsC8S3mouU7CEDonH8uo1ldCzusQv5JqmCuaHeReFq3JOOIzMl4TuRRf77bDkeU7t1dQHy9s6H3jWFTXQhu18soWgiB8NdgfinIwYcWKU0t16_CBK0sNkz749bqKOVKRYlGQKGZ2IMSKWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/funhiphop/82274" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82273">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuETjOu2j3hJhIrAevh4POEVULIde0KR9_6PI0uya3vd6ytmKGnsGfGPn5qoj6w0FbRCGvwYnC3gcETCjxcxREEYiGky_zcuDSgMI4U8tVHgx06nXS9OmuPxydlGshOnxY4N5srei_XtrOhRp2CTMMpIDuMRA3l2LPGMnD4F7KXqBGIV8SVlvCRE48Sa7LAXSmocGXE-Nhpt-cZ04HeRMM-nA_0UMDY-AiLRPn0g0jTTd_AdzjiqZhg6D6l0W6igrILm4gkL1EMoya9abTkH8CqFzQk7QQhUVr1zUIg7TFl4DHlj5okwdVVcXSEYxuqe2lim28VccofDAVKE4kVdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید متین فتاحی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/funhiphop/82273" target="_blank">📅 15:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82272">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGsx3Ugt1aaQ2zrA0uRyszJ2pk5ueFfM9ID5P-o_8qjRHyY2KTD4kmwj2FRZh0uolEVF_hjHw3jdFLra1uxZeGLoqPNVoZ_Lh3NVKsBZwJ7eH2whs6-AZ8gctUVnninivFicYhz9L5I_qRWh306sZGuAlAsNPW5voV4rJyOAjArRR9MqN3EAcOBAgA4w9cBmp9kMofjVW7Ge030SMZQm7fGNk62E4QD7LpqRvF5tm6nitUEYqe9Ug6JkK-nlnSZpulIYuxau--IqluJfq47IyiEtwn1g-GyZEVs2mYz_-vKFVVqyAJ1qNUzuWw1SNQGEiBSjJsyssG5xZwnKrhmw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرامو از مراکشیا یاد بگیرید، اسپانیا چون عاشق اسلام بود بهش تزریق کردن که احساس کمبود نکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/funhiphop/82272" target="_blank">📅 15:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82271">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIV82dwevXQyjPHikbzN3EckVSrM00y8kdYpjU5zw1b--ElbhyqCewFpe5WZFr5yMbxrd0vGSQVbfOoOsFEjNIl9DqeUHDblN5uR2605DDvfI0sIEAi20qZkexurfL8AfVGKcb_1sXKXo7VyIhY2falXRb9n7itl_Yv3ZwFaykp8pA737QeO7fGiRcrJx-98hw9KBBYw2a2K16aA9V8EVO74rjrMN9fY7m9QBXa0WeL7XnTRTH0Xq-ge2Uvqwrj2hjEFwCON4-8nStvM3Tu2yJYvJOM4AvyP5u7scB6Ssu5hQKVmikf5K_i_NKPAkGIRbidOISzByRvcBqeroZ0dDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح اطلاعات و نگرش آرتیستی که خودشو یک شخص با سوادِ سیاسی و تاریخی میدونه:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/82271" target="_blank">📅 14:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82270">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فرمانده کل ارتش:
هر ایرانی بتونه یه سرباز آمریکایی رو اسیر کنه یا بکشه 30000 دلار میدیم بهش.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/82270" target="_blank">📅 13:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82269">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=c014wRQ_2uE9O4hNcNGwBN2hAipvoHf_rZ05gkReJIAvsDn5WSrrSI0pf5QMVldf1aPOjuoKRLS2JaouGmCsmq1K-JFcdi3RnVKVBFsd9_gH9aKFhQ1_2Ofi8nWUnkL7Y7kB47TJFTN-njGgfItS0eg1Uun6J2qomWayJ24HvAEdpVAZqdVw_TqLJhl2AM89iqnOVLw3fQKKhH5LFsEeSmXnId4a9yhM9U4tJdLpriN2ymO-Ukj1N7UEznOENtz-kRpZAo05MRge2Mw844dX7Xu2r7vMYWPqJQQquCUUtmVrmWr8oKy2F-wHHz8vmG_RLEQCvwc9EDSFI4gDBAT2XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=c014wRQ_2uE9O4hNcNGwBN2hAipvoHf_rZ05gkReJIAvsDn5WSrrSI0pf5QMVldf1aPOjuoKRLS2JaouGmCsmq1K-JFcdi3RnVKVBFsd9_gH9aKFhQ1_2Ofi8nWUnkL7Y7kB47TJFTN-njGgfItS0eg1Uun6J2qomWayJ24HvAEdpVAZqdVw_TqLJhl2AM89iqnOVLw3fQKKhH5LFsEeSmXnId4a9yhM9U4tJdLpriN2ymO-Ukj1N7UEznOENtz-kRpZAo05MRge2Mw844dX7Xu2r7vMYWPqJQQquCUUtmVrmWr8oKy2F-wHHz8vmG_RLEQCvwc9EDSFI4gDBAT2XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهی دیشب با زنش رفتن کنسرت د ویکند.
یه i love you هم تو استوریش نوشته که من متوجه نشدم با د ویکنده یا با زنشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82269" target="_blank">📅 12:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82268">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOrUquRyIyH0tgwktvXFtuKD8v8GhgckSIiUqJiaUpq0I6ECXwj3OyKa3g_VNUuzhgJI2nCMnmkC9nxXJW5vfxt_U8HGOt6GqkqBvl9KPd8gzMB3igFXXLsbDadaawonUoO3eixQQRhmF-ryQ3dIHDz7AdAFxiVbYTATRQSzf7j0ZvSDpeg0g2xZ2CDbHSG65xLo1Xf5EljDvmGI8ZD2hT0JL5Cn0OkMANjtcxZEzWO6S-ST28IFyKQCEIarqha8yLJz6zbJqOejAHrGd5eJLiPDHVHidu0UIqwtMaDvOeURIDRxssBX_zS-8b6wI2l9Gz9AHLw3c6B8I4XFqJqC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82268" target="_blank">📅 11:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82267">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkiCH7IHGb48LXkSajCiEJdtYANGbhyo7edakcB2aZ2TCfn6vY3vhhZIBcMZyYLg9NSz375Mi5ZiZR-JMq2rxCh--LellJQAHZ3Ii_9ItCcqSmsD5aUXABbzB6GmhNFwee7kOcGRQO6M-AnO6wWAkeME2dcl64UbUOg3iGksSDKPOVyucthKmliO0XbZF_JGvbSK8IChnsdfnBBQnwABlp8iNaH7WyVHrLvuql9DMBKe6sy3CZ_gPXR9Zp65gy81eLsvsK7x3rxISN7pjGq0yuAOl_xz4csouVzZOxH7oc09EqJYhwj39Ic_RpGEEMoaqeBLKJQHlSl1elpj2ZH1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لانس
🇫🇷
-
🇫🇷
پاری سن ژرمن
🏆
فینال سوپر جام فرانسه
🇫🇷
🕔
یکشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه بولارت-دللیس
🎲
با بیش از ۵۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لانس در ۱۰
دیدار اخیر خود، ۶ برد و ۲ تساوی کسب کرده و در ۲ بازی شکست خورده است.
✅
پاری سن ژرمن در ۱۰
دیدار اخیر خود، ۴ برد و ۴ تساوی کسب کرده و در ۲ بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر لانس ۳.۳ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر پاری سن ژرمن ۳.۱ گل در هر بازی بوده است.
🧠
خستگی یعنی توقف، نه تصمیم تازه.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r25
💻
@BetForward</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82267" target="_blank">📅 11:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82266">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu0v2cQbN6u94gwZwjh4R3eC0ebiQj6SGYyDc44KndmMRHAReomhXSGJZpsu53SwS5YgYC1-OcpJhgGmwVs4P4azTIAyqD6btN6evmrcKPhQcaxu69BaW_ziver3RbwDUjb6N0zUjpdsa_5n5bxJW6S_BnbMPvAP-uJXskVkm8MUst-zFEFuXCTMQei1Yae6MoIFSNhn9qPAQthL00ry05kyDJ-lQb3dWcTMF82IaBlBlXwSXsx5tsV5msWwiZ_cpVXTMHhtED0SCscePlXHzdy96vtdGZAq85NjpRtfTvrd4MjHpmwICh-qi79n5mJRxFBIgHLV7SFKV1N7kdgOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرام صادقی یکی از معترضان در اعتراضات 18 و 19 دی در کرج اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82266" target="_blank">📅 10:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82265">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYctcevTSOFYyt1nGuchapWsadPcrBk2YZOzmYuejv4IU8HvVWsndaWNVzjqeiHcEL8c9ewOn06lqxBlUTkqPeYw6sQAyJ88YsDEioGaE36XJktCdVWCDecba2dI3LEPjp-TMPx_at2I7QXsZRgrkU5JNJ-_n30szBIa00I241FDQDGQRs0tr4VJCLTM90JBsJkzTbmTeefkyx44_i0X9c7JXtbqquh4X_XSwDQXkTwlYcr7cKMzD4LisVjAwj3G_--Q1iZ20ta0y8LqLXmVAJkFkAFU9g99X6P84iWJUm9kP3pEAMH6iwcHWbq--jMuUDe_Rmffp63so1xyT8-QeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی پیشرو سیک سینابو زده و سیناب برگشته ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82265" target="_blank">📅 08:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82263">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFscdgy_JMihCpGVWPs8NeANhTS5Kq3lzH9UCOtPhjf15FjQwQUh32sGmiiEj7x-EUw8AuKoI0BVb0ZomKc_9dxzuTj2tA922CINECpuX8NsL3LCRcAr0O4rMYgUiRAxm2EUo-_ksJVuqd66yMjCfbAoP2AprJnZrKxueIK2PgrAR4IyPIS2lfC4VyuMKB2RrygzP34UsaYuGN3nZI8-k5Tlnp-lMEXTYw9Wypxbanfqd1VNrYnRcrLAyKV4bJb9YdVlstKI6mfBQ7-rO_ka1X6yyhpezp8JgjO4LtVoVHrhXB9Fim1Q6IqROr4-ilGmb7PZ_qdCb6yUMwzExC5e2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82263" target="_blank">📅 03:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82262">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82262" target="_blank">📅 02:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82261">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نمیدونم براتون مهمه یا نه ولی دلو فردا ترک میده، اگه دوست خودتونم بود باز بکیرتون بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82261" target="_blank">📅 00:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82260">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-qS9ubnOg_v22XVjcMYsvV08B3OIisQMEg5nw4V4JZN3ALLalb6XmPtWhfvqeaJj3uEXZikNijLG3DXNKXTNvSuvQgSt-jKDQc85z6b6oKkE60sWPmsDl-8XOF0ju7ZYeYUaYXjzbG6nvwrzK2HKeOiV1gHH4n7UgV9vg-ATzSnZvCnsEF9IWlzbXQ-9Zll4BHzHMgIPyp5tdfB3ZRwnRk-x9qN_hqKpdk1FLyiTPoyi39FgSkBISb8a0ydreI7rfmsW7G91LkPE2WydXkRq4ZOHlN4b6p2dUYjQv8YbXIVUnwmbdrNqIuqDtI9OmmUkZNlwhHDTPH60Pps9ps-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم انتخاب خیلی بدی کرده و رو چیز اشتباهی نشسته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82260" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82258">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JcKYxtwQ5vJQTSP7xnS4sNPahlsB77RKZOxtII35u5bkRR228PYrr8s2ZmH1n0JclsuZRrknfqo5R2ouQSl0t0rFZP4iKdfPqix8yzQbl5xh77CoBxpTz5jqZZuURm0t50kN338ZCycRfmLyJEzKxGLa3yI1oFFk-97fMIn2d_B-b7483dohjEXZTUDDbAlHsLfEw-Yju1G61v2O4C50FaR1BbpuXXOSR1U9AjEIrxp51IXyelEycyBF-yL6QIFUaa2R2gjrrfbjQeBpfXM7XWXW-Y7-fgfLhWTJtgsUbeOpctqoXjlk3nasn8MTg3bDDSyBhgM1Yl14k0YS-KiQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5huNJkb-nfflA5c3tTn97Gzgi1bvKxA-iGU57lKnmP9hmHVEbeVAa3v3Y2dvHn5PGuY5CsIwG7piXyLQz2xVoaXv8s69Gc2fjEC5qKgUuaw1H35WzWdKz0kDyShmYl-Gx1Zs2-TXI1zKkPhczr1vNJ5TYTera7Zv8JN-s-lVGLNLzn0WhdxvP4-hvzziLY8aIMaM64MbksP1Ho0am1ZWAFnyo_daUZ99jx7YxGmqEvPNPVKThmzO6ods6DHvdDHdkmHO1Xo649MGpm8WYBe0ATO7G1VMjCBGucKsCcWL2OAmmNw_spbbaMFENFuKkSgZlQ3PBMcQehZR43NHP7mAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اوبی میرفته دایرکت ملت میگفته عکس با کارت ملی بدید عضو گارد جاویدانتون کنم و اسلحه بدم بهتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82258" target="_blank">📅 00:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82257">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛ + حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82257" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82254">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtVP-l67t-c8CzHFT5g4DvW6gQhSuuqdWr0n6TkBLbylCW3FF2vpV8jhOzA7j6Jow-UokpynIpHxGgmWhWzYnfz51Wye6BPHsGhSDxiTDZJRHwJQR-FlzTqbeMvWi6-2FNZ5Oihvy34RQ_a9m7UTQ9dABzwHx6CGnPSy133E3rMkt650uxrYccJR8N0RUg9JXzKqWX14-oNvodGnBXX0fc3jzMMlJzyTcRHnV3_TLnNNo2RSjZQ156IH1C2yPAWwE40DHSWZNMGt2ONPolETX3FuRwrGKvHW9T1j1jO7dr25LB2FPijNvL12XiobdISR_I8Kgn7WIJhW4Nw93MoOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWpN1yw-HkvsjzdSYHKtH3aB3Fm82t9s6bipqxfHKmidTSR8EwPy0cjS-GWKBVIuV8aJre9fpCTh-OwHJ84bmpf8Hzvlp0k5fIZoiylFD_n4qFnzbL0uzIs0YcuwLp6vVVJAeBCofqsFxBFqnQi3NWq8ZwwYxrjkZRL2jOzLp77YGEq_t_RhHn3nPWu70cxAsxco907CKr2tWxp7yhT1kTGDQMaFvkQxi0lrs33UINxWmCO4p5NSMafgTLqcpsTPWbp5ShbMNVAN1euhOOoj1DvoVfdDo4lNFG-KTfTWkPdGNZp8Tbanpdl9WwlibH3Tpv7tfBtIoOCwppcMIDd9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBugwyUF67uJ-kYFSj6e6vVN9JCD3O4Kd84wMLBByys1zRj4zryJupZZjoK5Z5vObtdw1Ad3DaS1Y16aly3PzPRiAAjT5slqVg3YSjliayrb6LBTuX6wBKGmWrYLblGwvhsaplDDGQjcQSmXa1f0VNywsi5KMRfSxtEine23hKDjiZnQkFqWNd28hsTEflXopzc2H2yA0Ihhyf_ejS8Rz0LhTikrurOKOeTqEm3K-S0_XIPBZPms0P68OVXKZWOnTRvyi_T31a-iSXq7Bj6DGzCnfWcU_nXszqdcmtEi0A7PbzxqJL8WHjm21NI3ZQamIiIjpGuQ-pBmmt6O4A3CsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛
+ حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها
@TopTel</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82254" target="_blank">📅 23:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82253">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">روسیه بصورت فوری تا زمستان ۲۰۲۷ صادرات بنزین و دیزل خودش رو ممنوع کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82253" target="_blank">📅 23:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82252">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=mrAblCHYrp_SqWLpBDP_ja-Ktfx7Vx30FctepiU3erWsOxJRsLRa00veWTl1AEuVWWh8KJqWUeGhOBnx0gI0yBOg0uPna0xfZ13L1YSzwI659PdzOBHhxWCViY77lHaJxrkqJFxGAu5YAJ44yyUqSThpPKokFF97iL29GDu8YHnJqT0h-qB5uKugUU73aHjxlbNCH1mlHwgKyptjeHCzKzSx6ng7mRhBQa9MQj2uJPWOG3ukQiVPSr3Xp5sopOgSCfR--qet3EUFgdd12amTthfyYeDncVqEyGdcpc2_pbfcqDophdFaAReMf-dJcfibtRWeHOYrlvq_YFyHk8wR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=mrAblCHYrp_SqWLpBDP_ja-Ktfx7Vx30FctepiU3erWsOxJRsLRa00veWTl1AEuVWWh8KJqWUeGhOBnx0gI0yBOg0uPna0xfZ13L1YSzwI659PdzOBHhxWCViY77lHaJxrkqJFxGAu5YAJ44yyUqSThpPKokFF97iL29GDu8YHnJqT0h-qB5uKugUU73aHjxlbNCH1mlHwgKyptjeHCzKzSx6ng7mRhBQa9MQj2uJPWOG3ukQiVPSr3Xp5sopOgSCfR--qet3EUFgdd12amTthfyYeDncVqEyGdcpc2_pbfcqDophdFaAReMf-dJcfibtRWeHOYrlvq_YFyHk8wR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کصکش فقط یک دقیقه‌ کیر گوزیدی، چطوری تو راند اول ناک اوت شدی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82252" target="_blank">📅 22:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82251">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">راستی این یارو امیر علی اکبری تو راند 1 ناک اوت شد اونم با ضربه جب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82251" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82250">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سلام فریب جان سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82250" target="_blank">📅 22:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82249">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سلام فریب جان سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82249" target="_blank">📅 22:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82248">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyyVlmJG74CKlMntWMX7ZraUR3GD6VmY5hcZh-9S7DYETEuqWQrRjpTxwAMSGomkWbHAmpklnRWrG-G4JTGlmRaF3h-xcVbVChQR-E1keC7r2FFvvzRk9CTYWLTNHel_Flek4jOCRTLWD9GjOdRTVxmyPGzO-fD3F2K3xvtXvL1jRCCpisvShwpfAWYy4sEE6n4E8pkmGF0fnAV7XSECEJczDa2CF0-iiuDP0FxTzNmcYIDZw-otsJ29RFkKOd7dLVDeCDSwgC1U2SYLR-PJPjXz4m9tWQTHzVnwPqpR0gRh-9ivt8-k3EehUbiKhO4Vl5rPtDiAS4Hrhr_LlJpWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82248" target="_blank">📅 21:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82244">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD4-s48PNZfajDaoMQXPn4bzSGOt-7nOlg37PSG33KtczHIn6eWh-UlfH4A3G2tWWRI8iXO4rY62sd24V7wfsKVz_X3DkaPI_GvKhJf8EWeQ8c8YiWhGLB89OkdEeLgBxFW4mDCDIUVsBb_bWXTURcpqww6nPmVs5ms-DSX5_9-QmOqnF3KMSZ8CWr3dvxcPMBNlDrnteHNcGFi6QnrA3U5r87yqyX0R4N4cHa_Wm2pe1n-f5V8_JBxcidAIU1h50jHKvh9sAX9NK3KJYXOSy70AHnjiM0TTy3imhsuLwPH6FEIM9_kJsDwzp2GI6zYOPrIsxOviQp2gaM00oK_qPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل نصف حیوون آزاری های جامعه این بازیه، فک کن وقتی بچه بودی اینو بدن دستت بگن کتکش بزن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82244" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82243">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔥
دنبال یه VPN واقعی می‌گردی؟
⚡
سرعت بالا
⚡
اتصال پایدار
⚡
بدون قطعی‌های آزاردهنده
⚡
پینگ پایین برای گیم
💎
مناسب اینستاگرام، تلگرام و وب‌گردی
📩
برای دریافت کانفیگ ریپلای کن یا پیام بده: @wizard_0061
📲
همین الان عضو چنل شو: @v2ray_configw</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82243" target="_blank">📅 21:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82241">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JTlw6r67hQWRHPY4MG8vjzqx8tiQ0LSWRYtqdMOLRaMNYv28MzASXSVoNEU6kaWlnfQLPtumiA_N0SsryTvSgUKZs_ZT4b804TEOFCnkQJPhY4hgLyPuaWwZ2c_HdPb4RvaiR7ZNAU6GCw-2uX2AxK7gQYGvLvqqqPzejvLqEKAmSpZZgKHXqg4oweWGHiAdQO5xQlP5lkkXVNoltYJN-bD-0isrr5T4TGysKXXJUWmdzurLaEF3Gpyp__diqEwvM3phpZFg0F5dVUf5ik3mdN8zNfwGP7AYDQvuJvZIYejdDRfpmc0Zgkwu_ONnoxEaMhtYtCYD0zI7x6YKFQGTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دنبال یه VPN واقعی می‌گردی؟
⚡
سرعت بالا
⚡
اتصال پایدار
⚡
بدون قطعی‌های آزاردهنده
⚡
پینگ پایین برای گیم
💎
مناسب اینستاگرام، تلگرام و وب‌گردی
📩
برای دریافت کانفیگ ریپلای کن یا پیام بده:
@wizard_0061
📲
همین الان عضو چنل شو:
@v2ray_configw</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82241" target="_blank">📅 21:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82240">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یارو بهترین کص ها ایران اشاره کنه زیرشن بعد بره دایرکت یکی نود بگیره جق بزنه روش؟
میفهمی حالا سطح تفکر من و شما و دلیل اینکه میگم نادون و احمقید؟</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82240" target="_blank">📅 21:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82239">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms5hIJh5BfuEQD2ZkxkRkC3YmRXE3Zm5hMzbJkLhINdpy1ewTUtEnRtjLYvuJoV2XvBHzydHl6mF17Ps6MlnMBfeg8-yVIFBXDrnPKG1SKhDJ8MjD_VedulKLEvIxiq6Ja8j93MCvtIyTOsYk-u70MgoD2EdfLOifMgWMTSQEtOoJRXsRWYQ-BZ4zkLbz4GQULSboYa5vG90vr715k_8ILKP5V42aqgYPre5BP4OdmDrkd4IM33QDmDbtEKh7kDfe-wJDnqWvBoK2ZgCUqQh0A6zeaN86RoP-VxMWTU64R19nrP1B_-EqbtPP7tpc6zOU_IeR-8xSH6l-faxEObsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه همه‌چیز رو میگه و آبروشو میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82239" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82238">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پرسپولیس تارتار بوی سه گانه میده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82238" target="_blank">📅 19:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQ1yYP_R_OCiEDr-viUip_yaonnjQg5G3h-3dnSBV4QBp3B4VypUtiZPjYpm31TB1wrDpz7vTlQ5DKgMHhIMgA60QFeowSbFmsZVWrHnxvBZIxPMzndVdIwng9KgaaFdx_CyxAKM5q9WWPbZB5sjqZj9_0rXrco1oQvuxlQ1zUu_Uf6AtG7yGSuTPUp8ZLMCd0ObHxIXmdWa8zA9QHxKbDmzdYiZITcG4kOAzCddbOK-Q5N-_sgW1pxGSd9vI9dYnn6y3YnVM-HwYNz1jaxrGIvcbEVRR7Z40oUVZDUz_E0QhCnwN59J1JKHjvQTSZGjn6r3rxM28RRywFSQxIt1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RL0KsV2WmhfkyaWtsRyZ8F-jTV52d8HakbMmAVoFX3Gpx-AY2s47kPVnqjC2yCVLRzEKnU-phYaab-eqMvBfxKK7fY6zidXOEFSHy77WOq48EMqwy_JS_htaHQJP8vP8DAvl475qtDnpjqS74QwmyN5BwS-j-u4K_k2S0K06OCm_rVjuoWbYP_MYcGd6b3_EvVBiBKWhtA4FXdmzCrRGBW9dUfwRDVJOjpmfgScOPnryp7YVkP2XRhrDQfAQKxKA6bW5TktDztPka7PNfBlt1Ooxu30h3hvuxRnJTBNHHouhnAel-bZyxa--pvIj6OyuA6dzBZQmnkLURVCrRdMQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O30yCNCFNjSJKJtPSEvzTVNxTgoPFVeKhrULIpXUpFYxTsUlVNn-I53atTWK3T6S3gwvC3aHX_BaKDuBeVrPNeBbPEuG3hHBBYmAZ2d4frZR466MyTXce_mcEso7hselPXF4io1cYHK8SEgdecZxWVynrtFi5X4rMO7VaWvFmQ4XKs4YGPECRp1P9jvX9tG3O3CN1Xd_YqX2_0DZJIfzMNnNikltUlENpTkWxeuRJDRFi9Vo5aDyaTOtiiFqDcqn2KlR5FcWP8AvGol_zVLxK_xTNqQs9-YH3uTs2AnYBRWK8uewIYA29ICAJ9SPwUh6zCcdLlrIa_9C7r_ZyhO5kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افغانستان
🤝
فلسطین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82235" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8lEHcALkIKNeZXNrDGhqwTB4MiLX6rooo38Z75UyYNwjqZw4OJs6Gd6NdW4659-zLidnT_jdbaWhpQQ3UQr6FAHucJ9MPp9FFm4ZMN8JNZZYcT6_SpxeI7t2pN5t8y9O0bAgh9Qc7Hrt3U47HuPOqN5pr0UsECqpmozTyedl1uaV-c6Pq75FWDVzQSCQE3rW9SA8LYpFhmho5D16GNPVD6xBIiZk1hZ4qFsw3yimmcFoP-6HgFHg-_lvFytWLurhXiziaWBxQCVR3WFgYgpwNYwDvccWzrCuzXesY_SNnUZpf1vUHZguygI3yPIo8f2jDPCEC00dGDkyMo03khHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه محمود خستمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82234" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82233">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=mr_itw6brPxxYRS1gwuwORRG7qyIAU8-ewkPLNp_D8SVQZdBfrXqRil9p2jaYvqPw0Tc6MgvDw7zodoQvFvWcJjpVm2nblGVB5KSlmGGhELrblLYZQ-ewrL_BdO7sRcvpSc0z3dTMQf6WhDQ2I4SWtnLD6JVKKRwLyBLG1mLP8GFhn4FmoaI8sBKXe90pYMoRD7ZmhJA0LJXwsTUA4dh9e4c-OJ7yqO9TOuvOeiYc-Bhs8o-_0xwNXiYcD89IK5r5hunn5DU4BXs74vbQz2r4zF-Ar4iN97F_bZm6UpTK_FVA9qTkBznl8cIApPCEbNGqwJraZza4TuXDhmiWwxQEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=mr_itw6brPxxYRS1gwuwORRG7qyIAU8-ewkPLNp_D8SVQZdBfrXqRil9p2jaYvqPw0Tc6MgvDw7zodoQvFvWcJjpVm2nblGVB5KSlmGGhELrblLYZQ-ewrL_BdO7sRcvpSc0z3dTMQf6WhDQ2I4SWtnLD6JVKKRwLyBLG1mLP8GFhn4FmoaI8sBKXe90pYMoRD7ZmhJA0LJXwsTUA4dh9e4c-OJ7yqO9TOuvOeiYc-Bhs8o-_0xwNXiYcD89IK5r5hunn5DU4BXs74vbQz2r4zF-Ar4iN97F_bZm6UpTK_FVA9qTkBznl8cIApPCEbNGqwJraZza4TuXDhmiWwxQEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم دیشب یکی از هوادارای استقلال داشت مصاحبه می‌کرد که یهو رفیقش جلو دوربین انگشتش کرد
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82233" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82232">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B55Y2hvw9Iuz8GDSVlfrsHuAnmSuW08NMy1vsX4Oon2xY0-x3vr9UjQcOSrLM4Lpb0MnxMfJAFOe2gbrElqZ6Enniih_m3ngE0EHDkX51QGnQKUtuxJ_OjsP6n7sJz8YSjnR5X_XjMZDSAgEE8noIYsGOqme1cRLBgPdpac3WbTNOcPXUYLXMqJhZbGILjkEhxOGVyN0Hu4lDb9xfbEPzXFhuh9ECLWNnxx1BGTrKRVHWz4kBQli9AddAZfZkt6zw3Mky01xhdXEg0L3gm7Pph-6rysoXdWP7-4eD55UAvbBghgvW8nNymK6473or0yiu7uQzh_EpBa9AiN6CFhRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
نشویل - اینتر میامی
🏆
لیگ ام‌ال‌اس ایالات متحده آمریکا
🇺🇸
🕔
بامداد یکشنبه ساعت ۰۴:۰۰
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📝
حقایق مسابقه:
‌
1️⃣
اینتر میامی در ۷ بازی اخیر خود در لیگ شکست نخورده است.
2️⃣
اینتر میامی در ۱۴ بازی اخیر خود در لیگ حدأقل ۱ گل زده است.
3️⃣
نشویل ۴ بازی اخیر خانگی خود در لیگ را برده است.
4️⃣
نشویل در ۱۰ بازی اخیر خانگی خود در لیگ شکست نخورده است.
5️⃣
اینتر میامی ۶ بازی اخیر خارج از خانه خود در لیگ را برده است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r24
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82232" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82231">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXwcCKlMsTtFAbUuGZ4oG60m2fpsEIkQ0G-WsiOtOOG-1OHNrT9yvxE5VtyFABupMlaNdz60yhRTPFO6L7Tbm4EVb1SflAYEPHZDbDfVd9bPX3GgtHmIDGsSqlYm4ejtjvDmp3Foqpn6XNAhkFZTIqPAE_hLsRbFyhAxYIOmnNELFSe8t9oefZ_KnxDMz_lgtbxLJVAGa1pr8hfRWvS_Pqji2ayKZfXfhsPC4O5v1Er0gv9g8oBdb8f2Z9m3oxcPR6D7zn9ze3GNqxnMO8y6nfmJ0xKNpWMGa9r2uRZXPJVEga-7taTL0PNDg21w6MhBPNi5w5MGOxNdAdoQVjClQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده بعدی توپ طلا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82231" target="_blank">📅 16:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82230">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حال ندارم عکسای خیانت بیگ شگی رو بزارم برید چنلای دیگه ببینید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82230" target="_blank">📅 15:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82229">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تیجی چرا آلبومشو نمیده، گایید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82229" target="_blank">📅 14:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82228">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82228" target="_blank">📅 12:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82227">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=j22XPvtksDGZfCL01JdHFrRBqjXVTx_z0krfsH_22F_HHieDYUg2aH6J34vM38TiiE9pln5QC8LUEZmMASvwaXb4RfUoHjdW0orqPtxGt6-XCBLCZ0sgARPZfFH0q_X4VAvS-witqvtnpquggIuAmglXIpSRJLdo4qC-CN5gdBs-8shDeQOC5f3aF9hi3oyJ8h7yKkRaaz0zFrmT462cRiMy6Ndt8z_k_RegyjZqVkgFYcxMM1zzsiwsXc7itFixyQan28B8k7XmD9Tx8iuUruQfj0lVyJHcpxFleJUO6soCoDxsMdEVSrxFMRI4lkTAc-w-Z74Lilibz9al4OupJ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=j22XPvtksDGZfCL01JdHFrRBqjXVTx_z0krfsH_22F_HHieDYUg2aH6J34vM38TiiE9pln5QC8LUEZmMASvwaXb4RfUoHjdW0orqPtxGt6-XCBLCZ0sgARPZfFH0q_X4VAvS-witqvtnpquggIuAmglXIpSRJLdo4qC-CN5gdBs-8shDeQOC5f3aF9hi3oyJ8h7yKkRaaz0zFrmT462cRiMy6Ndt8z_k_RegyjZqVkgFYcxMM1zzsiwsXc7itFixyQan28B8k7XmD9Tx8iuUruQfj0lVyJHcpxFleJUO6soCoDxsMdEVSrxFMRI4lkTAc-w-Z74Lilibz9al4OupJ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴
: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82227" target="_blank">📅 12:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82226">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=HTyHIheKoVF5N4VdwPNyL0e2rdZiEsAr_I2r5dzbsILR_7yhgvRNFv1yXxHLl5rh4nZy6uHZSiLPmbOx6B2B_CGCm7OWtNxLNShJL5f4PkhwEJvv3PzcvAVC2r0i7HZ8N__tlyO6fWgjgxv1zx33ZdJREzZQs7aKUKUT0H1BgObKmxbDqAbnPxU7zNFEjKzd059EQawgpA67tyj1TqJ7MqB3ULUO9J3dVWkOK682J6Y8WEBHN3hjUt6ZhOPZ-NXu9PHvYweArZnyRY_UsyQY_MdC2SaGeqEzFpUFRylJsQXSKdFkZmFXn0Xkj6xbBt_MUXJNyKnazZOTQl2TP-aPgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=HTyHIheKoVF5N4VdwPNyL0e2rdZiEsAr_I2r5dzbsILR_7yhgvRNFv1yXxHLl5rh4nZy6uHZSiLPmbOx6B2B_CGCm7OWtNxLNShJL5f4PkhwEJvv3PzcvAVC2r0i7HZ8N__tlyO6fWgjgxv1zx33ZdJREzZQs7aKUKUT0H1BgObKmxbDqAbnPxU7zNFEjKzd059EQawgpA67tyj1TqJ7MqB3ULUO9J3dVWkOK682J6Y8WEBHN3hjUt6ZhOPZ-NXu9PHvYweArZnyRY_UsyQY_MdC2SaGeqEzFpUFRylJsQXSKdFkZmFXn0Xkj6xbBt_MUXJNyKnazZOTQl2TP-aPgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مامان ددان تو اینستا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82226" target="_blank">📅 12:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خلسه میگه دیس خشی آمادس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82225" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82223">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=DpNXHEAyfGbJiVF5rEhCmlOYn3I8br_n5s8O6Cw45kzGhi0ZNW5ps3BgpsgIUb7nmIUOLek0CVxKwxsf6fN-vil4fY8BN7IEQBMBVr_H3kpUJspeT6ZhgPoQif62pecDuL_tefHgWpsIU4SUCyqa6KGU-X-DurvSRX9BzsFHmhzpGUaFJWblAlWIis4p2r35hMtQxEuGl5Y0xihCua6ItIGqWaOFVXUsQzBouMXDFJr_cyY6yxIdgbgcLhYrnQ-R0sKcsILQpzxfurnbDxWi8496AJgRFN3uy9S1jLPzMtUkufofUSdIfFwd--2S2joZCi7wcNGupOC2zmFWY2HaLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=DpNXHEAyfGbJiVF5rEhCmlOYn3I8br_n5s8O6Cw45kzGhi0ZNW5ps3BgpsgIUb7nmIUOLek0CVxKwxsf6fN-vil4fY8BN7IEQBMBVr_H3kpUJspeT6ZhgPoQif62pecDuL_tefHgWpsIU4SUCyqa6KGU-X-DurvSRX9BzsFHmhzpGUaFJWblAlWIis4p2r35hMtQxEuGl5Y0xihCua6ItIGqWaOFVXUsQzBouMXDFJr_cyY6yxIdgbgcLhYrnQ-R0sKcsILQpzxfurnbDxWi8496AJgRFN3uy9S1jLPzMtUkufofUSdIfFwd--2S2joZCi7wcNGupOC2zmFWY2HaLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فیلم Avengers: DoomsDay منتشر شد
۴ ماه مونده تا انتشار خود فیلم، این یعنی تعویق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82223" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82222">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKuyvOKuGBxYeQCnG3zOsuifBcTh822S_EUjqrvBKSTtKPRI1dvxGzGDs42Rpko-bCtx94eYgHyVK5IwtEiCOmX2jQOxWzzB6yDq9dpPkO6a-XFj_fZ5nmTfU9euw7j1GIHgvYAbQWJT2j34qPgS8dSTQJ7islMLUMYBD-bDAQxR9CWL901qyOjSEInZrfvkMnbDeAjY0eU3ge2aADEU_Rkc1gU8B5kBagJsbnLQr18tiFTAVAeo4T8jPamnRkt4IK1RIvGqrJJ9DxFxlVs0bHw1tk0zL5Vwtj3MMPZ5CppL-JNzGUtHqzSW_pKp-5A5KE8-8qL9-64XnUqU9MXdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری شیپ استیلر و کوروشو کجای دلم بزارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82222" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82221">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEFFN67EEOvdMpdfSox0xRU0CEGIc83VR5ieEkYXQ62o34VqBZ2o4U8Gns4SJtPmz6r_J8Lg9yB-qLguLSsQkSAoC6h5-HMaIiw71Pz0Ywn2rfOL49rhdgK1712S0W95ZcbTsDbR6wLeksoGFScFsdMr290FVDDM6GM8jZvDEajQyFZAdxKuh23sukEWk4p-EBLfn-F9u8RSJRcv-oHOv-OsuFJKGpS-bi3cuGBs-l1rTIglkHV7W6k1xi9LxqGgweU4bsaX1oaMB6GczP869AiwGpzINUh5VNP2t05lEO-PZ-t66wUGr5UKmNoA-cxRqGArGNFu0TlCuVsLIbRYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
نشویل - اینتر میامی
🏆
لیگ ام‌ال‌اس ایالات متحده آمریکا
🇺🇸
🕔
بامداد یکشنبه ساعت ۰۴:۰۰
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📝
حقایق مسابقه:
‌
1️⃣
اینتر میامی در ۷ بازی اخیر خود در لیگ شکست نخورده است.
2️⃣
اینتر میامی در ۱۴ بازی اخیر خود در لیگ حدأقل ۱ گل زده است.
3️⃣
نشویل ۴ بازی اخیر خانگی خود در لیگ را برده است.
4️⃣
نشویل در ۱۰ بازی اخیر خانگی خود در لیگ شکست نخورده است.
5️⃣
اینتر میامی ۶ بازی اخیر خارج از خانه خود در لیگ را برده است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r24
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82221" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82220">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">من بعد اینکه فهمیدم منو لک لکا نیاوردن:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82220" target="_blank">📅 03:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82218">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBWgsZyWdbEonRWID7COUUe77LBWHfTzFvVv1XXydOv5raC1KwrqC9bA7QEPQVar7ib3RpDtWpz_me4HiyTUflyg5tfwvFp2wkbO4469j-gBtHW7preBm3q6qchgloQ4OQhVwXYyAlLibQECOQvjfJ4U4xktstr7yYorMPyAam32uXfd4un47hse_BhloGrZmikMUeHFB_74HPzCuaWN333ZX0pZjSbjy5KIYXjmMY3tuZg5lKGhbHpT1NPrMYwx8dCAjlbv1R8_weTyFqX6t96RbnLPUN7V48-rKL-5xfTGubfSCtIVPf1WY5C6G9mSrKy8R36ZIxXInIw2suMIbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYF9_zoPCim8AdUpqJazU3_pBGFLdnJRcvAkZPiSua8sjvPiLYxEILJSMkteZr2c_6Ny04dq-9u0eAUzUY-LxUm4uvusTgAxdcixj3naj3ZHNpT9XADcLuYuZK-ydQgaTw_KfX8tWRaZruMq1P8qKfhPqK698s7aowKkF_rc5muLJ5XM47Zi1LadzZJkvEVEmzti4jtKMZOpx8ki3bvhC5v5kvHrvPR9Sttkdu4wsiP5uQpwA8IxkfFpmTAOAn68Rp0hBDAqv287_mntWqrdz7ZdmjmYFmhla6uoUun1VGKL7ub1p1CQiDbUG1Njit7N-ST9j_n69VP_vRb_s25UWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آخه کی ظهر مست میکنه پوتک جان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82218" target="_blank">📅 03:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82217">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6oARNXKHbT6Ykx_cMJe6bZHyWRdSND7iRw64lh0YVgVh1pZAUGrcT_cON5_l3ebvDfHC2Pkm1d-UwMNeDIeZN-Fb-rFqMow0gqTSI1-DbScrTEdcsgHyx0xh2v_Afrhf_r5pW_HTIRGHh_IiAWZfYlZTyGjaLzOfI-qAfXpoGc6zOpQwc5FwiGjXND2wwp9oMPbadAwgeD7oas5-El91Z_pjGzXplJbiUTeBcRxtKlOtWn6Rr2-Ue4pXrdBr4h2Y7HRr13fODFQleeqOxuSTc5lKToaCNYrVP2pwQFb_MGORIbPcJCrssWlGvbYG2JykUDKhptseSpA1UKrUm8quQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته بود: بچها زن نگیرید، خوراکیاتونو میخورن استیکر گول زننده هم میفرستن هیچی نمیتونید بهشون بگید.
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82217" target="_blank">📅 02:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82216">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ: تنگه هرمز تو کون ملانیا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82216" target="_blank">📅 01:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82215">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFrguqjDYBzcOcH5lFLutFC3p_zYnNfVtUaI5WpV5rdzCRY7jbIhNKNXUfl_297zVQEoNc0EMSFVGgMWUSO5veMnLv3q-qYE8EK2kU7_DxvxLb_KQ-5myET6vSb3QWmYrZ1WB_q6qr72INRuN3PfUZkYzR5ytzl7LPf3V2P8a1W4RcjO88p0rNlY95aKNy80lop8ABxGNR-eIoGR24e25YpD8H3aMgP_9TD1YKofzPs2QsNzN6TydewWeCNxjZbEwglY92g4LjMxka6wzLo8WTcpXSu4icnU8nztFwYoaEht-WZH4sQT_qwcbH43SgD_gP_2SK95K3VJnoGjuuf4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا همینقدر موجودات ساده ای ان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82215" target="_blank">📅 00:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82214">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پاریس یدونه مهاجم از دست داد سه تا گرفت، بارسا دوتا از دست داده یدونه هم نگرفته
رئال یدونه وینگرو ۱۴۰ میل خرید پاریس ۳ تارو انقد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82214" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82213">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLwEQRVpGakLpUy1NN9Iecb4KzosYb85P7Pjg-cHItytzAi7DqAXbF-86NPDFfX57GEbmbHS9D_J4nl9xdJEGsEdGSRX5hxsRjFIjZb8lupCU4JUdEdUAjfIByybtRj5pXnNN4kVvHJhj3iYvpzdZHdD7nNn7SECXiCUCaRCbOLufJ1IaC7v-aImB9d5DaVKCytfRnKgMUwaNaAI55VnUI3v1WhICoNh37oDY63t6f_tJSerdoaNdebAB2Hgsl55MJKvp9VXrpdxSrCsltowtwGfQAdQPbyUGEme-H0u5e2smzN1hinP2jDnjIvVgLXfvA-vzwJaTie0k_VhjbeLYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش و جیدال تو یه حرکت انتحاری مادر ددان رو هدف قرار دادن و دارن یه نسخه دیگه از همکاری هاشون با ددان منتشر میکنن و نسخه اصلی رو از پلتفرما میکشن پایین که کردیتش به اونا نرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82213" target="_blank">📅 23:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82211">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ما یک ضربه اقتصادی قوی به ایران وارد خواهیم کرد و برایم مهم نیست که این قبل از انتخابات میان‌دوره‌ای باشد یا نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82211" target="_blank">📅 23:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82210">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrGpxfvOJgRtCwlyIB3kf00u2LIlXYen9uY3wGVL51f5N4YLZeh08fyRDSRb8ZH6PvZck7T7PXI8_2hxhrZFRyOEHXN13HBFSeS5m9OuX_nbC6u7gercHQHkTUpRJBn3qo130p0WiywsLzDgS2uBqVjdUxL5FPFasqhcpGcU1FKUO3ooAH74jpnrKHhS3ve_LmmycOGXgsFoXrMBS24IN9gwXuqSk0TbCEG75cSaVkcAO2dAOcSetAuykMMpDKgGFn-EYdOubQ0-mXb1wBaD7uLIAGTamLencmzbEqntGcbGt7XIbrFf4lzCSv0Yu3O4UnpArOwMF6XvasQk4fQedQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو تروقران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82210" target="_blank">📅 23:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82209">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=L1p_Kmyk1PuiIQRaOVUJHlbGYSeUN94AtmUeGQp49SIPWIOmL9Zhy5tPBVohDZI9T_lX6qcjO_3iCPNR2qK4N7EJa10nPGZb5MYVLDIZCAgunW6LJponPgXb14vJNVAz_EVXkdayeTGRlWEot_VMPIAnFNhk_mxVSz6OeUVyhxvgcPIe7IQGZC1Ri7MZUyuSqjYk07DoWzysO2Wor8kbrtLUc_PWOpAGiQw6NsffW6jGWSJODp_SpXQG8Jxu57ae-9jhsQaK3vyJu6-ufc0VtxkovN0ZUrWRxKC-rRoHymFDp_YdSdVI2N8CNI82VSWinAypzEQ9af5qCSh3rgdVgDb4nRxTc6038EoOTUlT5RIcQUf259dF1GH-EakTJq56a8TRQk8HnQo_SKJsOJUhAGcE0aF_iBi1qujqVJ9PVfm2JRzoAmykhsDL10HZ0SFTLyZ7GLEEQMpeVVqWNiQCEf1p-f9SVwbaCfDsmEcBmrpw8b9ay9SYF6HKXddbSAGsURBcDAn0OpjGzhmmYDt-fikiU3XU7TKVrDYl_4kIZxHkZKnpABE_7nrk5OvbTt4mHqBTzv5Q0SEUXFPRfzKkXkTsaamns_bBq5nJZqDHAcCK9kirts58E-hgScdD4qffmVYOp7m7TjGKI64ZOnsuDC7HVDyMrE1VsOhr-SMBpOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=L1p_Kmyk1PuiIQRaOVUJHlbGYSeUN94AtmUeGQp49SIPWIOmL9Zhy5tPBVohDZI9T_lX6qcjO_3iCPNR2qK4N7EJa10nPGZb5MYVLDIZCAgunW6LJponPgXb14vJNVAz_EVXkdayeTGRlWEot_VMPIAnFNhk_mxVSz6OeUVyhxvgcPIe7IQGZC1Ri7MZUyuSqjYk07DoWzysO2Wor8kbrtLUc_PWOpAGiQw6NsffW6jGWSJODp_SpXQG8Jxu57ae-9jhsQaK3vyJu6-ufc0VtxkovN0ZUrWRxKC-rRoHymFDp_YdSdVI2N8CNI82VSWinAypzEQ9af5qCSh3rgdVgDb4nRxTc6038EoOTUlT5RIcQUf259dF1GH-EakTJq56a8TRQk8HnQo_SKJsOJUhAGcE0aF_iBi1qujqVJ9PVfm2JRzoAmykhsDL10HZ0SFTLyZ7GLEEQMpeVVqWNiQCEf1p-f9SVwbaCfDsmEcBmrpw8b9ay9SYF6HKXddbSAGsURBcDAn0OpjGzhmmYDt-fikiU3XU7TKVrDYl_4kIZxHkZKnpABE_7nrk5OvbTt4mHqBTzv5Q0SEUXFPRfzKkXkTsaamns_bBq5nJZqDHAcCK9kirts58E-hgScdD4qffmVYOp7m7TjGKI64ZOnsuDC7HVDyMrE1VsOhr-SMBpOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فصل دوم سریال Mobland که ۲۷ شهریور منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82209" target="_blank">📅 22:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82208">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_K8asz2uXHxYUNHQp-HsnYjXodkpP42Hs_TibLZQQiIewFOdrPuwEyqxaB2ck3t3rZL_X-zWIDBPgb60fTPDyoTAk4jE8keiVNdFhDZDXSXk2e-VZ8K5FyPfIlOtLVqfH9TIKxOa__K-HGeKH3-pZa6Be_qGdB21amrSt_3ob6g1GZY2CseBhoo9pTxIlFAgULp6LyZd-qm_ZXsnozGz0SNjl-vzcewGkfFc3RfeuQQfHnaSLPivHqVIjstIbmkhrg-z9c5c9yNxDpvrnv5b2p7I9sMm7YBhMgzfUdTc-rUNcWONFdwxO6D-Z0pG1WC3GEtu85gDY1gvcNIlgCH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم نفت رها شده در اطراف هنگام و قشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82208" target="_blank">📅 22:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82207">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مایکل اولیسه :
با تشکر از رئالِ مادرید، فصل آینده اگه مقابل این تیم گلزنی کنم به احترامِ حضوری که در فتوشاپ‌های این باشگاه داشتم خوشحالی نمیکنم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82207" target="_blank">📅 21:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82206" target="_blank">📅 21:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKEAg3pZjXxn3v5M4Ck7YZDJhXy92vTJfFy9tYKh9Srerp69A_TWklYCvyFtTe1tWqAAm6csmq7L1e6IwtKiHPun7Rr2ZJ5ZgVdCp10tEVyrjibL_M40PSpQ2obJai2GafPGJ-UhhK3oJBGALtIxyWT_ExntrHZwzAOv8X9_Q6mBKC5lHvvIOV_zmtDgi7UONPiGmpgxMskh6FY85yh4QoZ4vnnekmHF35wthEq0HjvdLvCzP4B0EMqpXO_t0JaRNR-7xDg_SvzbiwJe0oRo0-IhHt5jEGxXd2nVMQEYzryKKP2XH4HH7zGkPLsfMvgYiTZgYQAh908izMt8M0QfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82205" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj1I-dojd74vLI0-ZveOfSp_3S6K0EV-DZvW-HWs9kMcQBNLW10v5PGeeErZXcvHfycLGPhwd6tp2HUxzpY56dx1M2y85kizL90yfbCbZKGaGLyuYpAH7tU9nRKeCOcf0PLeaiXJaVyJPMED3fnYcfXw66oKrFLDzVNRsAlQftGCDKYDzfwcw7xK0mDjWMWmTEAHfIerlw9e5uHWO19RuBeuKisXV1fWfQuGTRXBly-i77qbcOgAsZJaPiyg8QWjz5e82CIq2Oif1SiRZNVCdj4KlZvqKVy9QRPfqKXHCRaLrORLDZ2zTcd3FDAo7YNiInkl6U7nT2acN2osyW3hvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از نسخه افغانی دیجیکالا به نام افغان بازار رونمایی شد :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82204" target="_blank">📅 20:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82203">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmCBvsXOGLNAQQz8ab0HN1zEsKDQpH4-4tZECzptxf6BLYAkJi5E9il4yrjfMaZHe4cQiR8nLUFs3MpUJYD5_e30Ty6v3FBM7bZB-OdT3rveHdgpnm4SnovPkyHz3gZE5UfDe3pUqI1sEZFain3nfOGvuaViqXvTx-rRl6SJ3ZIZsAvRjEEl_Nppp9N7jHG73OvaMndG9VqNS8cOuvBXK6HTEOIJuWhx4TGlqHikJpINzOvTm9HofyoS6QH0fiPc9hJ1S40QCi9DewhP1_CqCfw8UeMMW0WKGB6u5XjP-G2Xocpb7Bo9m-2uoGIihroMUVvM5QCTNauxJ06e2OVstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قسمتی از وضعیت جامعه از زبان پرستار بیمارستان :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82203" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82202">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMiRk4zqajUwVpr35fRkypnuxrH2insJUPWUyfOk2toICUGBMOAPFQYl6M1S40ACJ-ukMXlZx9NP_NIEbXERINxFk_l_YAkbZ-0VCDsybIZEVgBMv_DSo1VESR4riXIJy0Mv84GFX33jQkUTQ2ytGDzSOBjpoyZWgkd9A8AqD_RGFzPrpktly_OVJcRSULNUzrmeHY-z7tatkDrRDmhCj-mW2hN89mYA-RQ6DEX4oKnVKxRAlTKIE16M1Bx2ESgMzVtO2dO-tjkOcQ-QjcyHUAsZxT7VbzNZVHUqAi9fJFmuWzAnnFshg05I7fp0Y7ubzCxp2e6aXpNPjwvRKQbziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال  پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌ فوروارد با توجه به مبلغ پیش‌بینی، در هر روز از رقابت‌های لیگ، تا ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
21
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82202" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82201">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ بزن که باز این لیگ کیری ایران شروع شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82201" target="_blank">📅 20:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82198">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atIjfNK8JdQbmYBdU84FNTLotCXuv5nBA9cGep-JicvSmHY9lOlzByNKjceycoILMRqYI_VVM38YywRIfTFM19ossZS8ktaQznQTLspHIxZFZK2MxjBDskyOJv6KBqSWUrVakD1Sl0XlZkZuMYuPikysq_73TQyZTuHMZ8lhubVkbE-o5tYshvjUlcick8GhG35evp5rgM49Ir9fX2tRXcNrs6k_MonpFkqq3_j-nWoKtJ77atLZk2_fOcWyyHM5-cCPVEEBpRNT_uKE6-OoJeHOO468J6W72y64N9_3MawO7_vHUbGH1SEuCqIuXuDSBRgrBFbUfircZxVdFPAlWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82198" target="_blank">📅 19:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82197">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daLvOD3kJtjeJQLImvx8YgdxD0Bf3j2dtEvQMLBo3sICuqf7jF3RyXFjY-kpElkRclAPFZNJT-d9Us-VIrAEm3Fv81cX0gMaD64T7JbeFKP69Ld1qMV3GEk4rKwpiGed4D1XxeU6QBe6C5pqzAlAw0gqNcZquLwEuVGAFGeUSGwD6RKYXinM5mbScyZCxERGwdEMcOmyXkC45_vuPGec1cPMWF05oNrIqL4GFzIzfuOnQ46NjxTh8gtb0O6CDMY2WDxRYt090ZKSU68YquTtDXqce8U1iGu_ds_QxIkFDPZ_b_VHNyjvn-EQstsKXNWNdmSNV9CFhX5X8w979dd9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه قهرمان‌ها شنل نمی‌پوشن
بانی بلو گفته موقع ضبط فیلم سوپرش با 1000 تا مرد تو کمتر از 24 ساعت، وقتی یکی از اون مردها شلوارشو میکشه پایین، بقیه شروع میکنن به مسخره کردن سایز کیرش و بهش میگن دول موشی ولی ایشون که تحمل همچین محیط کاری سمی و تمسخرآمیزی رو نداشته فورا دستور میده تا اونایی که مسخره میکردن رو از اتاق بیرون کنن و بعد به اون مرده دلداری میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82197" target="_blank">📅 17:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82196">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDz5Nm_QGr0ta832TGUWyN6sQoOiFhK96EQxuJFWgHTdo9duDd92gDLPQw4lxRrHvJGWW9KCPWTkUfpUZmVPUfdSkfQ48HiN_ylcI3hi0DfcLImQZFWqm3q3-3AFTxELzR2Cd4vN8K4aQ1q_G_OGPFid_ARyB-Xq3dUIkyxpnpVY0ogMzGPno_QYEeif0buoCzyaRFQ85xiqryu9_CJIS4MIxIDGudBxdy96I69eze5_51H5f0dXLz8y-En4lW_XlhEtmHteCkKS29haaEEkJVY8JrUh1pcgd09XQvDyZfYpY-gISlRzv8rxQeIkhzPFLCBm3f3B30rx07nSlV8aEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اکوادور ۵۴۰ کیلو کوکائین کشف و ضبط کرده که تصویر هالند روشون چاپ شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82196" target="_blank">📅 16:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82195">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=ZKlEmLYNwHEn9Lbm_Vn_HxigtHwZnRau6PwQiFM_pRwM7YjKs2lrWdVvQhUyjngbNsxYvK1M1aIfD8_ds8sosoMri36AVpVPVoy_nrvqe2S-ufE-v4YmrK3ULEKtzvrLofpxBpY6iytvKwU8j4nRulurTH5GQovauipEAcZ1GNUzWgVf3HYvsPZO3GiNXosGC0PfqIaNb4XsxzXlKY_G96xUv-slGHwzCx_Gf7BcdPATt5kGWQGkaH3rD9_L680puRAbfmCEcQbE45n7nQ6ydGbksZoS0aCRB1ryZ4dj3AT0e68mYRughs6ffkvgPITlPji4TMz6jpwYa-r3WOKMNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=ZKlEmLYNwHEn9Lbm_Vn_HxigtHwZnRau6PwQiFM_pRwM7YjKs2lrWdVvQhUyjngbNsxYvK1M1aIfD8_ds8sosoMri36AVpVPVoy_nrvqe2S-ufE-v4YmrK3ULEKtzvrLofpxBpY6iytvKwU8j4nRulurTH5GQovauipEAcZ1GNUzWgVf3HYvsPZO3GiNXosGC0PfqIaNb4XsxzXlKY_G96xUv-slGHwzCx_Gf7BcdPATt5kGWQGkaH3rD9_L680puRAbfmCEcQbE45n7nQ6ydGbksZoS0aCRB1ryZ4dj3AT0e68mYRughs6ffkvgPITlPji4TMz6jpwYa-r3WOKMNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدایا ببین من نمیخوام برم جهنم، ولی یارو اینجوری پوستر درست کرده حق ندارم بخندم؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82195" target="_blank">📅 15:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82194">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بنزین آزاد قراره ۱۰هزارتومن بشه، فدایی حرومزاده رو دیس کنید همش تقصیر اونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82194" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82193">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbcxIJOzF8K1UC82Z2C9j_TsJ6Fw4fZeMJbTuFlf-w3l-QvZNmWtNkMk1JiwTgmKuuxqSvLgChoJushbEUDN61xP8Zt-GEkpLAbXTI9Lll_KREa_h3ex-k-JZTGp5VORSYstG6nWkgYXrcL7vVEzahX8POYg948s3ursHabGuHtKl1w_Ro9_ISqGYvkacbOnJFVZhLQXhjNUisCCFKrATUM2H743S6dmsY88GBeeASfPxJwrNq5SKZ1kJTRV2Ceg_5z-eb4gncYGrz0a54zfpknjmwpMGMsq4NI6X5mRLla0EqP6VVxlPSC_o2NytBgDhSVGdsZfAZqZmPBt_sPf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیش سال از این شاهکار گذشت و اما بارسای قدرتمند اون دوران با حضور مسی که نذاشت بایرن گل نهم رو بزنه
🔥
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82193" target="_blank">📅 14:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82192">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تو اگه منو میخواستی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82192" target="_blank">📅 14:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82191">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">7Khat – Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82191" target="_blank">📅 13:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82190">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
  <div class="tg-doc-extra">7Khat</div>
</div>
<a href="https://t.me/funhiphop/82190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بخدا خود هیچکس یادش نبود همچین ترکی داره، بعد ممد ازش سمپل کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82190" target="_blank">📅 13:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82189">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82189" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82188">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzaIoZfpe_F3pFyB12wO7F27lc4kSQ2hJNK6yh7PFl8jXWSsenlxb5_NtVouRJebeR7Mg84-uhKvNaN6rAuM88P9JYmUFQv8MQRNdHCcq9Bd9Scsygd94o4tB7TF7duvy2VSb7oA-GjrDCRy8sJvJ9YLCD3um8usPm5QTZiSTIzMRJmjgS4eXSFEsEH-fhHNfTrt07Y_AiG3Qp82HHo9SPX2vFAjqrMCEdA49uev0C4Bb8emFdfCUO4vzNZOpDjgmHAvkOKTTVtZ4RoJHUv1KD8wORDQJBpT1np5cHovUi3fTVhKjWHB5TGcGc0fJzZ0Up4kEczMX0gw93wI0O_mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82188" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82187">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2Z265bYt4ocSk2NF18Xz4ulFQHIDrS2Y6kNr3MMxY92aAEalrHcWnds7ee1Fvri2_VTMBcYPTwMCJu6q9Y4QeG_B66VLet9yG4LWMsbCm9Gxy_PnwNNVJDuzmBVvE82Fy_WyibXek2MjJ_NJW8bF5nB47I4dvuWYco7mIyDlEGmXgANrW2pRH4P_pJDNPcWDe8dQUQOZiE4v9ZBJmGJgyc49BrmwjixJJveqwMX24Q_YUjakiYvIi9J7F4h4RRGHCqXudiAkH-euVDbQKYfMA8prZM1OyPN_NdFT0XNJdmJ9oqZmFy_M4Af1C5mhiTZRvWvBKgsK-ViVuIIc950cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد روبیو و ونس  ترامپ مسائل ایران رو سپرده به این یارو که در عین حال گی هم هست و شوهر داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82187" target="_blank">📅 11:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82186">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWrnwKG5MU-GkWNF1wugAOZE3oyY7yHiwgSRyQlnMFw-ayjv6BClmX-BoK8UGZJlHj5sorCF6aC8fybWBw5EuicpKcpbRwsbkaHhEDmpYqKjICoR2pj6DhKWar1Ret5v0ojVHF5LKwdJ-x1qIRUmZecCKf9XfHvjfBOQUJdPWIOjm9-rnwh17_fNIs4K004Ydzp78U1ghzHI8J3Bcd4v7go04-f6ZZWfYAM6dx47f9hniwSBX1hCNAg2hEPqOdButyLVgwDpD-_wRPPpDa3ws6tmNGQjZDjX78kvRyiZxym71j03lgiacalhHu3TtxPZT96Az6FK09l4S9cd_XL-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون یه پلشت بی فرهنگ کون اینو نداره ۱۰۰ متر جلوتر پارک کنه و پیاده برگرده عقب، ماشینو ول میکنه وسط خیابون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82186" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82185">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jaf0fpOk3WJgsIn-slmthOacgU9fIA4uKpyeWQ2x1WxQOleE8BKvw2tgdLhIk9_TBk58yThG6eRkiXo_9p2B1e1pia1X_MGc8w6X2Eulj97FlGFomYeT3TaUjBcId3arv31f5Mqp7vM04kXDYWrad3BEmtE-0yae_Bf68HKhL2ctSeauMN7AYRFS9wwYyOawpjqpCESO09XsXREY1X5_gTHPotfscvAQLZzNqQ7ozZ_Psh7srsW1dQ6aiq8fFTRKEoNxRC7ZV2olWVKEkbTx79x8c18M2FJVUCZUtsIF8HzfuadBwHTn0caVL1vpnGwC1GxtAJpHdIyoz4GyO5n2WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تراکتور
🔴
-
⚪️
پیکان
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
جمعه ساعت ۱۸:۰۰
🏟
ورزشگاه یادگار امام، تبریز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز+
📊
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۵ برد سهم تراکتور و ۱ برد سهم پیکان بوده و ۴ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
قبل از شروع، سقف مبلغ و زمان‌تان را تعیین کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r23
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82185" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82184">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpkk55AeZyq3TyFPmTYIsY9ubG8oouPurVD5tHObCOGJO99QjLOmGEBCs0QrhQbcvdjQoFLAovDfi6fpWuqxR9wioVL_22L8HCu7km5JiA1qan23wV836WpEBEmR7v1j4gdr-gkc_nr3shzjitwiEkWJMx2BAZP4iHTKYcKIjxPbQpQqV0ALMZayk-CwepC7Vjcw_kZKGukz4nQx4be8-efQivWduMXVS8mXIGt8B0va8aCeapUa44neTJ_8Zq5s-G2S_bt_OGrmrrNHFIglXYfG9nSIPINBJ9B_4stO6Uqpgy2vhr8TbrOaPqrwErQyReLj6YOo1GQNgBlJh_mnhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز بیشتر پشمام می‌ریزه از ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82184" target="_blank">📅 10:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82183">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCCvrSg7EHG_N_mrunDlVnzZf8UPY3Crf0c-ZTEcnz0AtJRBKfDlBvy4m7TIhgeGVQT-SttLvB6UyTpTkqLwIpTebLN-bI0kQSZl-hPKvnogA_KMCCuJlxLXoAiDJRjFxsk3uhKSpsYKx_krvLPczy-_hma76bKsUKTXXrKfTubkxCcbEciz7MCIHw7EaXUD4JOnBv3JIZGu6HfJ4nJJ6EaypFIpV8i_bER3gH3e2E7RTt1wvNZuLSjNTSs2iPVIo-WZyDzD6l02dKm9_zpfkRA_Zd2TsabvSdyBIMzxdDxsteCxOfWhySCwFo4uEHRq_YTTVTUtrlGE8JIcpvrmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا که جای مغز تو کلتون ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82183" target="_blank">📅 10:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82182">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82182" target="_blank">📅 04:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82181">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdQNBxS-DgeNDvS6pDsvNVFMbwxsRs0ARFDTjMjNr5kJbWwuqVGlP9fAx2zWw4wHWbB8MgfNVwqMj2F_xA-1cSPFKAE_FtNDnyaw_EULAGrEsG9-s0EmHqpKgn5-BqZYhtLppcbXp0oBYy1V_c1rpUB-6x9MTBZQlB2MGyloh7CydbAyq2WMS71PakExQQy5ARorUy2h_E3C8OqjamNM9T2hN0W7UbzAsUSZIfgz2PJC1BUoQA6NiHbEb0YxXD2xSQEaXGbXTAUuIU9QlPm4nbnaKBCFdWqaQgDhxXDN-bnsFdGyeBsvdSBuRLcAQ78yR50JlXYqwjlfkq141zNT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اگه رستوران بزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82181" target="_blank">📅 02:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82180">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK1frAz38ehcir8UgqIUNtQBj3w30XJT0ClNEMgnOOjYVDHl3q01vyJZgngBNKSuWjtYOToJVPFUYbqG25KozP4c_--8sX8qBgNceBr_T-zU4WGkqFJ6v5ai6Kvt0RYrTOeZSPUlYNHDsqiFQM5Yk9lzzFSVKWhX3YnX8XyGCwnGqGwIpNm7Ts59jeDc2OzlHH5YlPaful-4fxtOPzHTQiMZxkCipRF5_Xj401hLH5uHCuBJ3bhqFgcM25V7SyXegHCJwTIR0qScVkm_5SFnsH0simqK02bcHH6uftT8o9FbL2nSfgdbhR3kWuOStpSKIovnxEm0IpYC1LkCFZG5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه شکار شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82180" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82179">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apr1r8OcgU-a3m_e4X4DVumxeNQcYXCGrftXmG8p1W8LaR6wpkNyGgtWH_CchFgZcnNldRX4gfqvDrce785wIZU4tZwloX4Me5T-wgn2nVjxgaCHVH2ctNoRcbuNFV-l-7YaQy_mrFJOhs5ou_WZw6wRSaROBP7sXxqog6gXxn8tm7_OjhW6G5mO2W77yYTuT6tEOig2oqgRMjBAvrEVgYQ12hjvozySuKs7oLsb47kw2cTfc0-CPbRjCaHTlKrwG7nDIWV3mhFj5HBGdruDrQ8Tn6580P-rBTkfAZ0clyT6gUad50l9QabBWj7QPqMHIFK-dyYZHnZAsd1d7bKf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیری پلشتی کیانوش  @FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82179" target="_blank">📅 23:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82178">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5782494606.mp4?token=e6pmAUhqhCbhQEWAYCYOp8HL904EEn7-0_YYhK2PIwuLbEuXO4zteXmo4OMHD_YLDNFwPOLfl4ibyml61GMCSZNJwStLaMEBlwWLBqbzQOhDoD0O9dpdASKU6ZUKy7FvKx-dCG35GboAs9GusPKREcsY2X6VTceQ7u9cDGBgjxHE1xSldhfJkKzO7cafERaQN1-QNflGJZQc22tUTZ0LtNNlnq9RtIwxqEc8tCJhdsU7aC77xdx7Ya3AEGyr7aP07wLtidOncqXuZ31ss2PsgxWt7oiyMKog5VoYsoqHNuIFvAzXncBTyU1p6BDpYTCOZrFe9J3h6urciSTE-N6602oL8tkE8plL9oTkImgrBLqZFjnxVLi4VDAWkzNFa2SleSZ_DCEN8RphKf75KrOORI_FLztNVHY-idP5dXp53nl2dVGhrU6nVAabYD1Yo_NLGwKfv7omtw_cOXPvdev_0j4BugrPx_-Ir4GrF6tgzyStV_xOHo400fWzeVVmN-04o_j-AastdgS5pJoOanzDh_3Tb2P7roBNe1tha7rOpcZ_rP5nh_nh7YwAoSTVgNnOqF2O1Llm6pGi2BLdwDK0I9Mt9SsnRQiuXH895HVVJakYteZbQB8-LxG7du5IaTIff61xL9CgK7LUpT2brmyIb--O-1VYSzhBM_fcjF9WBL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5782494606.mp4?token=e6pmAUhqhCbhQEWAYCYOp8HL904EEn7-0_YYhK2PIwuLbEuXO4zteXmo4OMHD_YLDNFwPOLfl4ibyml61GMCSZNJwStLaMEBlwWLBqbzQOhDoD0O9dpdASKU6ZUKy7FvKx-dCG35GboAs9GusPKREcsY2X6VTceQ7u9cDGBgjxHE1xSldhfJkKzO7cafERaQN1-QNflGJZQc22tUTZ0LtNNlnq9RtIwxqEc8tCJhdsU7aC77xdx7Ya3AEGyr7aP07wLtidOncqXuZ31ss2PsgxWt7oiyMKog5VoYsoqHNuIFvAzXncBTyU1p6BDpYTCOZrFe9J3h6urciSTE-N6602oL8tkE8plL9oTkImgrBLqZFjnxVLi4VDAWkzNFa2SleSZ_DCEN8RphKf75KrOORI_FLztNVHY-idP5dXp53nl2dVGhrU6nVAabYD1Yo_NLGwKfv7omtw_cOXPvdev_0j4BugrPx_-Ir4GrF6tgzyStV_xOHo400fWzeVVmN-04o_j-AastdgS5pJoOanzDh_3Tb2P7roBNe1tha7rOpcZ_rP5nh_nh7YwAoSTVgNnOqF2O1Llm6pGi2BLdwDK0I9Mt9SsnRQiuXH895HVVJakYteZbQB8-LxG7du5IaTIff61xL9CgK7LUpT2brmyIb--O-1VYSzhBM_fcjF9WBL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه عزيزانى كه از رفتن خانم کارولین لیویت سخنگوى كاخ سفيد ناراحت بودند ، مثل اينكه ايشون مى خواد بشه سخنگوى جديد كاخ سفيد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82178" target="_blank">📅 22:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82177">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3mpnDlGovXm0n6O3a6e-qHz6CZ5wsXGksZYB-PibQSF27Jj7bs6XLCFq_WMLDAlzmwfjd98YvUPvyeWnQfdbxnySj0wn-1Xy15mBQE7RVkEhqkoiPzb4S5CvvRA1UhbBfSTPkxB-9ZiHQxPbEnDHbApEOtZLMm5Bn5byqOBlJtfiJxdAv87bVWT81wbn9-TVhB4Q4CxClz3ticGF2b_9-__H6uuZMzG_eM1DXphUPqR9On2E5uFOP0Jb83ZL0L5T6jhcGVJgOn3m8iqUspMO8BKx8nopkaWDsvM-PKaeKHubIjC9Ref_EFDvtHeLTnk_koi_ctG-f_ocWGdNTRvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "قبلنا" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82177" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82176">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403c217675.mp4?token=JZ6JpIYP69Al9SscME-P3hkMuxkjdGGWpSRsP24w_VjL0E5L_bBHGsysVo16GvZCRmMeugsdntzYVK-N6lZryiIfhBZ-vQ42az5sQ0mAkvnbZkYidgn1efRnWNThW1EvL11cBFOwhCU3sIYybVLySoGw6zNDGJVw6ahDWnWuz0lPmcTfsHLyBmBMUXj0pU11hEi2Qd6PSpQ7Zx63WLO-Ae-JHJXgo1KCA65Rh1k6FsviHjCEYOmc2cj5PDiVa9INBPFyTluEj-b06MliGXWVLqbhqs4rEuoT7P0xfJr3YWIBNBNO9um09SdPTE6Tm3AcEVH8iMp8hbY8Yzfot0gtOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403c217675.mp4?token=JZ6JpIYP69Al9SscME-P3hkMuxkjdGGWpSRsP24w_VjL0E5L_bBHGsysVo16GvZCRmMeugsdntzYVK-N6lZryiIfhBZ-vQ42az5sQ0mAkvnbZkYidgn1efRnWNThW1EvL11cBFOwhCU3sIYybVLySoGw6zNDGJVw6ahDWnWuz0lPmcTfsHLyBmBMUXj0pU11hEi2Qd6PSpQ7Zx63WLO-Ae-JHJXgo1KCA65Rh1k6FsviHjCEYOmc2cj5PDiVa9INBPFyTluEj-b06MliGXWVLqbhqs4rEuoT7P0xfJr3YWIBNBNO9um09SdPTE6Tm3AcEVH8iMp8hbY8Yzfot0gtOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آروم بخندید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82176" target="_blank">📅 19:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82171">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7ITwEC1uuwrIH2jiW2lLPEO31CjyVpAagVX4ivVrDzIpNNdeSWX-3IqFTvgIZ3XZ1NeeHyE4e_VxlO156bUoNtBi6dyA8XsyWcHgmY5pTciLOPRSe41W0M3iSt6wEWz__KgXeMvmxH6Elao0vHX4Bl1KQpXtaztx-U-GIBvs-3G7A8L7wQNOKFBzIN1V3ChHn51cqR_pXj7uFT4EF28t1j9sLickO9ObdM3uZ-zxKxSR5l6LVQrkjQYd2_vhQ9ljge4Tn-QCxGeh8HTX6YMpTi1igi6RN_QNKcuKrir1Pv-dW9TkNnPWqk2dkOp2tV39AnJxV-AooGRgu8gixJUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZDTOKEAjqeZFDTfv1ffPhcOSZ7UcRxRHf5EIE4JBJ2sHWNUdSjZM_UycK6yKXmMMvQdsDcXw0hrPaMN9IFRelqwgwBpGfYRGFOiSV0oXj_QlMmCMdmp4mKN8M-uDMDOgNyQZ7CIX0g7TOHFarlBHmFwT5aSZabbnY83BNtbJkjVvIXiHbaCg7DiWbzDDV_1D32KaZ7nm4gIKyd4h9NiOi6h3pYKzaBaTFm5RSPJAtceX28QDyp2oUz-E-fyjuwLfHT5B7axIrmIrrYVttHSwF7SSJI6C42nKKJXTHjN8UF372pqNFvWBz66rb6ccyOeiiVS6ZVan1Ssgw4mihgevg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBHH1PEd03BzJnD0kB3E4Jjea9qQyDPo8LoEu8OuHIlLpnixzp6WgSPQofYh5dhSB75hzDmv24rWaiGf11QSVDpSHL_sw89SLA7-6-pSIiTHWyJeXbtilmVf-wMVBL096rVDbJQ5pB_iN0KUzvwj9IGihBwFWkvimZbgkmdVGfgu2Lp2-D-iS4eddCblH-B3n-SZ98Fcwf7zXanBV_qRrCUJXWm9V7PpO6nKQbYbOTj0Dg74I3J9tw7RVWcoR6OSx6jHkn4KU3zyesD-h7XFNN8LPSYq7DAzqmjpWH6L3Zzz3AF6F5ed6T2uRx7xtVwLmgWLnmmGp7h7eijrRVOZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZpJNW3iv7id2DqerCsbSpDO-11niq5Ev-xqu7E4E8sTPuTx1S_1LxCjTCHW_9FASfARgy2Ju1UL6T70-frMIRbSs2UDDkO2Z0bE-ZVPYdUElGotsnJVCGC2sv7VLo5K2gTxk-hxy_SYvbxWptknupV2j-zlCQM7K4BSFeIXXwQIjEVka1dnUFLBhGYmP-77FnAWrg0FMG0oNmynn1gIf2oO1DGhXzsGgz2f9ceCkomB3Lowv1m8ko6c18SQvBng4XPhghZZcm2FYi1gqnwnWv5BGBfIoVrxD002iAsVf5ROKLUPSUkdexAOrkvtVaUKZbfayX1YMWkWawXPYAdyGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=D5fgWV7ZBAghcN0t8u4YrFonFLyPXFJyY03F1zL9DLKBddmUxMz_Sf5rWH7AjI4qw91KgDPo9MQu19VfxpSJtdl8nCOFGEFstVWplzfqBk-st-wZBv3hMMWZBP75cUko1bmhlMDibMcowj9jW495tCoANNfSTcZuMiBUgvpE6n3E58mA8sKqCqtV1Csks_mBcIjZbMOlIfk_DDJFy505h4N7o75l3xoEklYqu_innS0yFBnOFIUKfMfj-7MFNHAxzuO1x3YUxLKNAZBJM9CjgcJOe0aQGX-laXaDa-Az0JvbM9frHxxyik0sBR45Ag_iYQJOI8bs9GtBfvnJVyijvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=D5fgWV7ZBAghcN0t8u4YrFonFLyPXFJyY03F1zL9DLKBddmUxMz_Sf5rWH7AjI4qw91KgDPo9MQu19VfxpSJtdl8nCOFGEFstVWplzfqBk-st-wZBv3hMMWZBP75cUko1bmhlMDibMcowj9jW495tCoANNfSTcZuMiBUgvpE6n3E58mA8sKqCqtV1Csks_mBcIjZbMOlIfk_DDJFy505h4N7o75l3xoEklYqu_innS0yFBnOFIUKfMfj-7MFNHAxzuO1x3YUxLKNAZBJM9CjgcJOe0aQGX-laXaDa-Az0JvbM9frHxxyik0sBR45Ag_iYQJOI8bs9GtBfvnJVyijvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامنتای اینستا واقعا جذابه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82171" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82170">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWIeZqq5J0uL5pWx-3iMma_1y5ev25FZIOq-3i1_WIFZyqtZevh6GB1AtiBiKADyHOirwKvO3cfSSyWrbKHB60XeFEw9NoA5_E61uFiYW51ORoCD0aoBoXNC4UMrLXf6qTv8bcEAyjjKdInGS848EQkf6nl0e-UFv7OpgwpL_DTUOu0nyYQzANA1fpcwqpqzF-evd7EXuCeqKx84kESr37ktQm2U1ZkenGugI7OZqv6D1C2NzKMNznlU7mxm6m-aDMXOQdRFIhJ-Gf4a4-Yp_IAragu7av6KIJQiKrQ4jI6ggzdnjkeT4HZ13_FEpKKBjn8z8Rhanin1V-1gzD1Xwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودتو گول نزن ارسام کیر کاگانم نمیشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82170" target="_blank">📅 18:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82169">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پس دابل آلبوم و این کصشرا چی بود
این چه کصشریه</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82169" target="_blank">📅 18:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82168">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بزار جیبت بیبی</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82168" target="_blank">📅 18:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82167">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82167" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82166">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpD6-23ehvS4s6ll8QhkMAP2wlCNBMKhTzsUDXhpYboQuafsB4yrOcRiDZzyKnoitRTOhU2xV8tbgJbKGjHc4_eeLZ-vhDgf4NFhPYrtb-BCjnfCIzSkhuBufu_aKsBkRYmJ9XapyJnit4pL1YxyNq4g-UuFyVs7-QiQI0Dg_e5mlMcJ4zj0pmneu8VjlDEgP2ClXPrAg04UlWt3GCZFkcahV0hMYhtapRsEP9jnLAlgPLF_YsahKPB2hQyJ5W4OPsxnd2SZRVq4nxabhUOd_EkArPOourheReZI1Gk_meK9b8Uw2BfgPXl9D8oNAjCoaZqcbi7874-T5w_gO-ZBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82166" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82164">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82164" target="_blank">📅 17:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82163">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qk5i2mXCTMOhQykG1HGQfKB40FJ_YJojduvF6ILxidIIQEvO6frxssuOpYHiRSEZZ4pt5ajpRyiyK6mla--XlTlydjNRXI6l9j8PKOvO5yvxT93GkmPZ80cnqnVdedKPDctO4jLAOgSov5rRvDW1UsoHdlyvQ1D7_AEUYoO6GwvkEM5HCzmeavbIXEZmphFTz9oCiCHUubQQM0EvBTyhe1oLxKwprHqkKJGCZujEwYJUgCXYLXbyfjJOfrl4BOYBJ9liqJXPlZ72HZdgvNNvkAGr_PdIaHf8ikRO6OBI8W-zgS5ou0HEL-tkCrtYDMQsTyf-w4Fj21uJFiOUPB_SWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82163" target="_blank">📅 17:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82162">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=qtC-wJLEGmHvqxyKInUJ72wasBU1htAAYFaFPRlTymAInIHHNBleHodswgCppFGM2B6jUwdUuJf2v3pBdrZQQigS9iSriyogmJNO7aqeElh8TFhnNfmYef-uLkeVrF-5MzdAKslUMyeF8krdXF8fch0HnR3Lsc6d6GuIPajeKGJKk3f7mK_SRYM10uzS5pgOl6QW2ysOJEKaDyNJNeWt4nEe96LlGOx6akNrBns8Kv-YBpRQazR6OUHgk3r-8LqnaPCuwVWl5DpAhX5bKp5dUjudEej9jcHxmHUZhwyD069AdlRPWUph7abF7T7IPzT-BSyRRkKp7J22xSgdDxMOtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=qtC-wJLEGmHvqxyKInUJ72wasBU1htAAYFaFPRlTymAInIHHNBleHodswgCppFGM2B6jUwdUuJf2v3pBdrZQQigS9iSriyogmJNO7aqeElh8TFhnNfmYef-uLkeVrF-5MzdAKslUMyeF8krdXF8fch0HnR3Lsc6d6GuIPajeKGJKk3f7mK_SRYM10uzS5pgOl6QW2ysOJEKaDyNJNeWt4nEe96LlGOx6akNrBns8Kv-YBpRQazR6OUHgk3r-8LqnaPCuwVWl5DpAhX5bKp5dUjudEej9jcHxmHUZhwyD069AdlRPWUph7abF7T7IPzT-BSyRRkKp7J22xSgdDxMOtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82162" target="_blank">📅 17:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82161">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a59034baf.mp4?token=CAd1RkMJSGsv-msggOkos1u-HhGX_-EGdNP_zkxwVRZR6TNayJmD2g3IiuFBPJJ0NGTL1gE3PqQJs_ldYKD4Xvm6fH-jRqFnsn8qp-ronZr681blGmA7i4q3Erp0dI1NdT3Ltc8wQnb1dx7J_nHuwXEiact2ghuvjsBuAuLc1_gWZn2qd-R_BTUtJTcQ8Bl6qAw4u9ac4KeI8osJoTTAkhZ8jYZwy5_IjSP3DFV5s5JlXuoCj7CfRI7qUcrjgpBU6mdg9CaES4U3538OF9bbgrTn0PZaJ-Fp9j4dcEtwOnOqXLUa6hnUIE4Ls4xNjgHrvguNXywRD5erNqeGIJWQ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a59034baf.mp4?token=CAd1RkMJSGsv-msggOkos1u-HhGX_-EGdNP_zkxwVRZR6TNayJmD2g3IiuFBPJJ0NGTL1gE3PqQJs_ldYKD4Xvm6fH-jRqFnsn8qp-ronZr681blGmA7i4q3Erp0dI1NdT3Ltc8wQnb1dx7J_nHuwXEiact2ghuvjsBuAuLc1_gWZn2qd-R_BTUtJTcQ8Bl6qAw4u9ac4KeI8osJoTTAkhZ8jYZwy5_IjSP3DFV5s5JlXuoCj7CfRI7qUcrjgpBU6mdg9CaES4U3538OF9bbgrTn0PZaJ-Fp9j4dcEtwOnOqXLUa6hnUIE4Ls4xNjgHrvguNXywRD5erNqeGIJWQ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارتوش کورک
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82161" target="_blank">📅 16:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82160">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سیتی خداست، هر سری که تیما اون پولی که برا رودری میخوادو میدن میگه نه ده تا بیشتر، خلاصه قیمتشو از ۴۰ میل بردن رو ۸۰ میل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82160" target="_blank">📅 13:41 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
