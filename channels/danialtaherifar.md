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
<img src="https://cdn4.telesco.pe/file/JKFwG5vqeL3AxImzU1e6WTG5fgdgKXQBt4CdkH7b91AZznew_CC7cia2UzDDSDQQbbZaOXppgz-Oz8wEk2tA9DOoKagXTEzinZTLKCLZVYacPUL1KhxcSrQDdR2s4OdES_ASju9cRFzSq45UMFIJpWjfyeXHrGOnxTvLJwCd7iQRyU1iGrlsiC0wWhaq4A90AtW2kO3MmkeR4MtwGVLt6gBHLI9VtesDtLHDhrjbmEw0XIE9eyOxwyM8Z-3kjcUUEzG9ETvTFs6YgbiTVPZlfcije-GznBVAO83FFMTUWKxy1gTJtLXPAcZE0ktusPTK_huuKS-bbPiCteYtpntXxw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.52K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-952">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJfPu844dvnuRUp5g35ax-XHGWHZ20pRf--f6JjUhg4lTpxgEyDRH8uMeKDzpim7fJoojdL6AbY8S0kfX2n_keUohlK2QXG-KXdkwxKiOcbDWukwfWB92syh-xU5mK87eGyB4shVgKIuR-7ItrGcIAuodungSwLpq1GjzeBCarMilwhdo9RBTkEVb10uNtlSPG3AAMkS3t7Xdrqr5c4fKHxMn8Xyxh5o-kOLmiwSjBoUg1vqY3gTnFtmuS-Hr_t6pEJYAmGFLZO60x1fWnUGhMbJ7Tr8QScquEjqcWk4ZXntnXBQtbLpg1qGy_WybZfN4ztHatvMEn6KiazNOD7xwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
GLM5.3 با رشد خیره کننده ای معرفی شد.   z.ai این مدل رو به zcode اضافه کرده و بنچمارک‌های جالبی هم به دست آورده با اینکه بر مبنای مدل قبلی کار شده و post-training شده    @danialtaherifar</div>
<div class="tg-footer">👁️ 494 · <a href="https://t.me/danialtaherifar/952" target="_blank">📅 17:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-951">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJy4QM5fnWnJarUYnmEdy0zM0w2Xqob8K8cefIyb5SLEJgLTSXOOdqHekeQLSGGcas0XzdZQbhdl45rsWpSANvuCe7-G1PXfd1mlWIep9LqdyOBg2YWkImRUmxyevcmyi3mLxhOeYDsGiBNVVJH3h7mJ1SozeGIABMTtvVZ2ySjQCXWovTuzZcS9BYerMa_q39yarTL5bbhVmwsXQvSi_UOgmYCNR9vyHBlViDUQawgJ2GO38F1BzWYigsu65qe6Gg17O2J11yQDUSKO4C0ZeWi_ReQhPHYINsSKcmRCSEoZ8LD2Q93hXovAxS5B5oJU6UWqUDMy8nVOMGs6atFLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
GLM5.3 با رشد خیره کننده ای معرفی شد.
z.ai
این مدل رو به zcode اضافه کرده و بنچمارک‌های جالبی هم به دست آورده با اینکه بر مبنای مدل قبلی کار شده و post-training شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 484 · <a href="https://t.me/danialtaherifar/951" target="_blank">📅 15:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-950">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8gNpCOvfLbwYqVStwOwyW8H-mp-7Y7zEyHAV5dZenaZT-Q1SnBjFeVjrhpNP-QtrMoknND0JQBBUmqjbL-QBXgWGY14aQsHjswpMfehyBHTHvmRtWTQV7iBOK3Bmcg65xknm3q-a_AaEQGO0raTDd_0SowsOLpT8d054DoHKhg10w3vMmcx19Rr_rE_TJA-cmP9xfm9zg9caJfULFRRNY9_qlj9A9N1zO140Fainy2uBdAt36yGw0wb75KuK-_cIdcxKnRxkbnReyVedBGJxi4aGgug4uRRUpSUKnFBufj-jKfv9uv9OfrCelAX01bSLloG1zjunTlz9jH01uVmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اضافه کردن پراپرتی های سوشال به سرچ کنسول اضافه شد به صورت سراسری
@danialtaherifar</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/danialtaherifar/950" target="_blank">📅 23:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-948">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s65QZ_QxWIjGIkMIKRVCqzAjl9VC8nD_S1UQhSIt2W6WromIRwHJUp2MAS_yeHgokDW8MwsPlOuEYK9InxPhBjcWoelsUVfeO3l-pewpODhvEPN34ZHfbVuTT_LDdkhnlUD6wSQHPZ1wUyKdxGspKemAi0c-XXqWNWj3Uh0qKzYkAJv9MQc_wD_RhwuRA3iQwm5_Euzd0cvlB_zqVya-hDAy7J9RsuV9-cOfnXaWEWg1dM00aND7iN7wrEvkeK0xyE9SnZDNTaACfeb3TqwJMZfUWHDzraLZwPq2SLbr3Gw5bBOF31BvgDvJU9oGD2CRfixshA6o_jZ-2SsbEDEBeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSmWzmFLMI7EHVTil7XcyJk1JcwSc5hz975WmHcIgc_uUpB9fBbDp-OKZcyRuixoyGGipVPMqwdXz-yePl2hs8AHiHxrJPzbiT7Jo6brg1pbv-F06ZDdaAWJE0DSh6MwMwoJKKRDq6jWOmYcQA1-4eM2HW9uZ26UtMGbbWimZD3RbEA4RbqsV8ta_N4Hv7QexmDsuyO5TXuPeoRepsTHfGeAE7ZQHzUgn3nhTOsU1EgMfQc-WCSJiiaA4_uFtkg6ZTgB5p4mnh9s6I6LZxq3BRo-Py6veWQ8udONvcObZ2ttfME_crJV_aZ-jJJ6RRdL4E_i6HmpEBZP9g3zKOv6iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😒
کلاد ایمیل میزنه به اون اکانتی که بن کرده که بیا fable5 استفاده کن.
دلخوش میشی که شاید ....
و بعد با تصویر دوم روبرو میشی :/
@danialtaherifar</div>
<div class="tg-footer">👁️ 743 · <a href="https://t.me/danialtaherifar/948" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-947">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKXo0IbSMn91Qt9Me5OGqgrDy2XGJ6-b1pxeVF72h7D0mBn38c1R-dTkqQOa3JgdWXkN6ebFCz8UH8pyerE6ZMcHUnvRhSToCeb7YWu5N47f75ROy7CJuSY1i6chl_jw1FdL1V-dDt76rsJ5qDXX08udxljNyb_YkMgsRBFGC69uZ7F95WfAq4g62YZ_K2wyx1JchZxVKhD7aCQLvdYW8WI1PKGtFsaESapsSQf9uwlV84PBhhRrJaZ_59WXIy4y_T0YqEDjAG9ShpUOwALUIPefvVquNZS_gBfQ_bqqNOB8lj8DsNhbxXCpBZjM7BIQfQJylFXM3KuDOx8tK8L7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌بابا هم اعلام کرد که مدل Qwen 3.8 با 2.4 تریلیون پارامتر و به صورت open weight به زودی منتشر میشه و در حد و اندازه های مدل های سطح بالا بعد از fable5 هست.
خواهیم دید
😁
#ai
@danialtaherifar</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/danialtaherifar/947" target="_blank">📅 13:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-946">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این وسط با kimi3 هم آشنا بشید!    یک مدل هوش مصنوعی با 2.8 تریلیون پارامتر! و کانتکست ۱ میلیونی که عملکرد فوق العاده ای داشته و در سطحی نزدیک به Fable 5 , gpt5.6 ظاهر شده.   این اتفاق بسیار بزرگی هست برای مدل های چینی و ما تحریم شده‌ها از امکانات دنیای غرب.…</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/danialtaherifar/946" target="_blank">📅 18:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-944">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qx1jXxl98LFl93jvX_LDz-x59g5M5m-JVy9BtGif8Y6SwFg54CyYpmt9ghS0Z0jPoo43VDoYnzfOeoDfEnYpQWrHWa5_G2OR1D_ZjzcS6HoaChGxe4thDt7RMGsQFQKly0JbbDe43767qR61DONF_u9P7hm-e6xHZ4LKnVX_4uLBu1mMaBW-5Z_LQ6KDJcaIhht0_lviISaXatHtE0c2cxShODPP4DUi5Sn7UjNdeZkJi1ZZgdf5O06lzbsL-NI36dyq__tCMbu_sRJYxEZH2AwTxKlhKo1K3sEJmSqY7JCeFopsZZNMQVKsNejCkXRboRZdTyhKDs9Eqdvnd5Cg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93f82da84.mp4?token=iNnz_gMosbfIc75rDSDgWXQ-edMJ8TGF6P-xlFIMQ11AElPCLR91zhkTy5I-JkrNLJNu4S8CC8SUo58MJ88Fn5M5KCGeThKOW5eLqM-2EsqyZIlrA2mSKmB_lVJxliHl2XzXTQnxFjodJssyDYwYzdOMffSxvJnbv39M4s0ebtauFUirgNz0Q571JXIJVmrbMkBO6VtrRqWO27kbfz4SY6JBjQVv5-rC_CC1FS6SphP8ChL9mVt46N3LlunxfRKv6q20ivyIaTw3heTmQ0ICzMwaYfaK8-lNYL-cprilBE-EjVtOjkuo_qmUWtoP3IZIxbPomQXhLAKQtFNx3Dzzrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93f82da84.mp4?token=iNnz_gMosbfIc75rDSDgWXQ-edMJ8TGF6P-xlFIMQ11AElPCLR91zhkTy5I-JkrNLJNu4S8CC8SUo58MJ88Fn5M5KCGeThKOW5eLqM-2EsqyZIlrA2mSKmB_lVJxliHl2XzXTQnxFjodJssyDYwYzdOMffSxvJnbv39M4s0ebtauFUirgNz0Q571JXIJVmrbMkBO6VtrRqWO27kbfz4SY6JBjQVv5-rC_CC1FS6SphP8ChL9mVt46N3LlunxfRKv6q20ivyIaTw3heTmQ0ICzMwaYfaK8-lNYL-cprilBE-EjVtOjkuo_qmUWtoP3IZIxbPomQXhLAKQtFNx3Dzzrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط با kimi3 هم آشنا بشید!
یک مدل هوش مصنوعی با 2.8 تریلیون پارامتر! و کانتکست ۱ میلیونی که عملکرد فوق العاده ای داشته و در سطحی نزدیک به Fable 5 , gpt5.6 ظاهر شده.
این اتفاق بسیار بزرگی هست برای مدل های چینی و ما تحریم شده‌ها از امکانات دنیای غرب.
من تجربه کار با GLM 5.2 رو بعد از بسته شدن اکانت آنتروپیک داشتم که اونم سطح بسیار خوبی داشت، اما قابل اتکا نبود برای تصمیم گیری ها، و الان امیدوارم فرصتش بشه که kimi 3 هم تجربه کنم (اگر خاورمیانه بذاره).
@danialtaherifar</div>
<div class="tg-footer">👁️ 694 · <a href="https://t.me/danialtaherifar/944" target="_blank">📅 01:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-943">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjX-vrKKznrO84jb7F3pZe70OqSwAd7LFJTSfMVFLMmLxGO6vVMX6epquTjfjQpM3VtNUWxTBVUe4T4kmfcm5U4o5nBU_AtgeB0Rq9kxKCQuHkicUX68n8khRAosugwY6rY5G3kNF3vUAMHpVfZYecrxtm3l73oAi268gS2idx0uV3LTI3SJIsJZF0565tVpVyVHGuhh-xFlvoOtH05DCNKqD4m22mfucGX2asqT2ULWtpIcZkdzFPPMLDp7p7fNgoZGzB9X4x6OtEWEhCAJo9MnyYbWYli0mYaXrntSa4ykenVnuxXi_ddTat5LRNmJI-kIaOk29RRBzD4N0qoDrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ظهر امروز اوضاع نت اصلا خوب نیست و رو به بدتر رفتن هم رفته
کارای مهمتون رو انجام بدین، احتمال هر شرایطی هست مجددا
@danialtaherifar</div>
<div class="tg-footer">👁️ 575 · <a href="https://t.me/danialtaherifar/943" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-942">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">باز بریم بک آپ سایت هارو بگیریم :/
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/942" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-941">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📚
۷ ایده از Phil Chen درباره آینده کسب‌وکار در عصر هوش مصنوعی
چند روز پیش رشته‌توییتی از Phil Chen، از اعضای سابق OpenAI، DeepMind و Scale AI، خواندم که به نظرم یکی از ارزشمندترین مطالبی بود که اخیراً درباره آینده کار و کسب‌وکار منتشر شده است.
خلاصه مهم‌ترین ایده‌های آن:
۱.
هر کاری که خروجی آن قابل ارزیابی باشد، دیر یا زود خودکار می‌شود.
بنابراین ارزش انسان به سمت قضاوت، خلاقیت، تصمیم‌گیری در ابهام و اعتمادسازی حرکت می‌کند.
۲.
کمیاب‌ترین منابع آینده پول نیستند.
زمان، اعتبار و روابط واقعی، دارایی‌هایی هستند که به‌سادگی قابل کپی شدن نیستند.
۳.
مهم‌ترین مهارت، انتخاب مسئله درست است.
وقتی هوش مصنوعی می‌تواند بسیاری از مسائل را حل کند، مزیت رقابتی در انتخاب مسئله‌ای است که ارزش حل شدن دارد.
۴.
به‌جای ساخت راه‌حل‌های موقت، سیستم‌های مقیاس‌پذیر بسازید.
هوش مصنوعی سرعت ساخت را بالا برده؛ بنابراین مزیت پایدار از سیستم‌ها به دست می‌آید، نه از ترفندها.
۵.
تمایز واقعی در «آخرین ۱۰ درصد» ساخته می‌شود.
AI پیش‌نویس خوبی تولید می‌کند، اما کیفیت نهایی، سلیقه، جزئیات و استاندارد اجرا همان چیزی است که برند شما را می‌سازد.
۶.
هم فرصت بسازید، هم از فرصت استفاده کنید.
برندسازی، شبکه‌سازی و قرار گرفتن در محیط مناسب، کیفیت فرصت‌ها را افزایش می‌دهد؛ اما اجرای درست است که آن فرصت را به نتیجه تبدیل می‌کند.
۷.
هوش مصنوعی فقط یک ابزار نیست؛ یک طرز فکر است.
هدف صرفاً سریع‌تر کار کردن نیست؛ بلکه ساختن سیستم‌هایی است که بدون وابستگی کامل به شما نیز بتوانند رشد کنند.
جمع‌بندی:
به‌نظر من مهم‌ترین پیام این نوشته این است:
مزیت رقابتی آینده از «کار بیشتر» به دست نمی‌آید؛ از «
اهرم بهتر
» به دست می‌آید.
هوش مصنوعی دیگر یک ابزار جانبی نیست؛ بخشی از معماری هر کسب‌وکار مدرن است.
📖
منبع: رشته‌توییت Phil Chen در X
https://x.com/philhchen/status/2072793818945167475
@danialtaherifar</div>
<div class="tg-footer">👁️ 703 · <a href="https://t.me/danialtaherifar/941" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 844 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJlur-bqKJaNpvJ0lcSTc1FoI6OCGG02sN8JRfzx-bNuuRisZlotX2kkv-tAoht9q6_OBXPW5EAOAP3bf0i4VXMwIpYW-exrWT5V4MrX8WpXEpJB6sEsVrvSwgcmE0J9_wu6L8YfC62pVDQWleOVY12DTiqpOYuW0IE-H1fqadWStRJHbG3iVHSUfm_PgvJuWX8X3xvMtuJy76V0fEyfj_n36fThkkEiiXvyr-GgKiGfn0ya5-gIIsxLXVNxMjsG0RSqRNzf3u4AnpceKrjN6d-JmswXOZbrL63bqK5hrr3EmEObTwMuOEmz8uMgh7TjSAjMmkv-t5t8a8QVX4pv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=Scm7PT_iV3mqVy6d9KQ_XsbsBqRZsgrMpyBbZr6t5q3gGyZCTe4rX9hl5MpeVStbSo3eyL6VGpGPUbapQXqW7B59n4NYnPXhQtl3Jnoszh6aux70b6PB1DNAuRKHgDqDMFq9YmwoGX5UBjehtRHG6pzjuSpA9LTtlxltVS5A2mO6zyJs_a_bDVr4By-cGlflk196m8UO70GXSolEW9IssdLlbPN1T_ll3UXlHBFnrAzv2j9VjiEjWL4s14uIVKCOaECdJOMcoWHocoDtTiNcko0ncb1NvV10WZitG8jb2JDiE-STA3-xPCerMzZdcDLLPFOSheUht2ARVS33qK6yhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=Scm7PT_iV3mqVy6d9KQ_XsbsBqRZsgrMpyBbZr6t5q3gGyZCTe4rX9hl5MpeVStbSo3eyL6VGpGPUbapQXqW7B59n4NYnPXhQtl3Jnoszh6aux70b6PB1DNAuRKHgDqDMFq9YmwoGX5UBjehtRHG6pzjuSpA9LTtlxltVS5A2mO6zyJs_a_bDVr4By-cGlflk196m8UO70GXSolEW9IssdLlbPN1T_ll3UXlHBFnrAzv2j9VjiEjWL4s14uIVKCOaECdJOMcoWHocoDtTiNcko0ncb1NvV10WZitG8jb2JDiE-STA3-xPCerMzZdcDLLPFOSheUht2ARVS33qK6yhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCYIYsoPLR53EOqOEsEZImTM7JQq-x6FHEDa0YnCn0YOotme9fGayOobFO4PfO2-iFTPBbXJrUIjA13kSHb8h2jo0ehmSFiKoY9rPQfH_fKaAyP6sGcJX2UuR7vgAjCFIp--UDOerCJlRIdO6lu2A6Id2FVyp9lNdDhCJHKfKDkElC5k5htSkw84wBPentAWHSKkW0qSWfZo8P6K9rVx3fwqUMwpvasWx0U2vCMhfHKHEHkltsqVdy7GvkXx-fQ0N2Mt6BRDi1WS1TkWlKDpzdrU48JF-OiqQaSfhYRB-DQYvi_epxN4Omuqpi_wD07PzmDRlOlK64MBieCGYSD3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 847 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCHxEC0g4AETwvosDlnttm0q_hTWPbsU9E3mQXabQ8ZOV9mMZe33Rj4MGyeyUlhnrja6dlEb_6m9mK0_LuvtEf1S3RBSJpbPWzu-pJgGHTlpr6YqgaF1dX3s5l7RpswnqFUs4Hqc4iHckAofCwWObNw54z-VkIEOnZdHGlKKC8CJvCvqBRaKiuSBt3paaf_gUHMQaW7moDvvN7Z1BBnOy4WjFsALxmIu6tfgyQh9ZbcsbhIDMqMVA5NlbUFoaZnV-sQxB87h9-mKIvTidBOZI7Bda8ks4NQ_LqVLZLF71aFV9JAM-qt0G8W-cYAeRJc3UXvZwai806GIHlX2QTAvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clpq1zVGLP0K8dsHnM5L3NTdONphenwAAer8STSQjsKHSGfJVL9_Rg2ZSi-z4A5WqioKVtDv4DKBDg2TfmaKjBdWvF7FksCjTFPXZ5RgxIWrc9SoPX7NuFDwMweSgabrZg6V5froEi_2ZVFpOSP0YUxwKhafXh4iONohuPwZ--a0vZXyfLLr7iPZUbu3Ot3WKqX3t2d63TVi2x1QRqsviYEvm0xcxHe-9nRDHohLezwJWKqfRrgsaV534BrU4oLQaIqBHbF7KaZWxR2zcf1Ai93_sr8wL4MTRqL2T6CycqQwc-6UjdPxUq48YvuwfGzPoFYHRfvYuJ2u4Il09ToSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-tbWJYGUhf3KZmOtmJEJ9HZYsyQESFgz2c2wmWyhyhxDRfvgYJzvoQBBi0yGCDvnV9F89sutdfM5bruvOJreUJId-FsZmLLAdzvdjX9FonZ0bCMBsseg7qF7vowSG20oz1ZdenHjnfLmbNprlEZgDItJFSdYRvnNigfjjbfC3E5HE_6jceENBJtBkGLV4SvZtgi4yfXpQ7iWe7UOs42ksIAYN7qb8USb1MDoBPZWHEAUccIE7bPx42ueUboHK4QsVYp7EDQvhz1rPoZt-UrKxzzzKNwE9y2PyYMYbQgUGfCgdohDWrts6YMiHouIRK2xgoH2QnZzsQVMFobOhBrtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCmRSllIT5UXiFpqczLQrvGmexfxSn8lQ9jbW4GOtHNQC_8UmtIUV6VeeN5LBA7ony5EB1Q3JVlvZi3j_f_svWgu0a4DQwp0ksaeIdTvHh_yDseqn5cG1058hxDiGwLMoqDhZku0ngv83ajPq13buQaQqMda6osOJuAG9o--zJEnOCd-PiwzRYSRV1-Ix9WR42xtTOcTixeSM-LL9gmH4LLARJwSUGLzh9HHW4F9Wo-044lKt8EgfDKvDDvW1gh88S3abtifgMRWpeKyH12HFjIgrEBw3P1Qg9dF0enRtjxGK3zptUhoeB__nAYAbnwj-Xpah4iXgx1wQOplgeyHEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZTu11VNqkJ61zlnG7Sn59ASluiCLGULfogftufre3BI7m5ezacpcahosgbCeMXQtLf8M5Ktt0Qh-Cu0h3aqi1W07Tq9vBlP15pQ8osBLTOXB8LlqaZZ13ulTq7B7teUPJb2rgnCYFEc2czrZackfM4eT55UqYJ17nVvHYIm4cCCtuEdcZYuBgSvcYpQg5H5DuUal5wq43_gtsD6mo0gi6DErPKcVVB1A3QwX2BI91vGE7DCDrQBnQW_3p8MpGIf3rphi0Dj1szYzg6jm1tLxScXkJoW1KJde0tvr07g5bkB9fcGS7lMdKLRZ7rUdwumM_0Jds7BHeZl-ZHK3tNXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 999 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 967 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mT9hXZO7N-6owPN0y0oFvmyAiQDY7K3N83bgGCb-NtIUIC0nFPbTIIZp9-pl5sIAtWdZy9alEtWk1PfOTj_ft_LaNycm8d62pRksJAaShT-snRN07DLJUOvEbJOH3l1z1kr5E3wFp8iJQTVA9kZZ2L4yVlBkdZeXyCvvvGTJ0mwkry8-xMbDlQxchcZScXeg7uR_j2X82ey2uuZVPdg9j7MF70_yJAipFCV5SLRF6y-6FNobzM5ktcXN104NMaITVh7fg_A7Wk41HsYjoIfKg9ifI5KnkHxDgX8W2pLEJZUUQvoIh4FFSHMk55kAHeQPAo3epi7X-ploMD8P7BO-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Isko4_RpVerB4rx4tvGT52ds1hVAn29m0xolFjSH4FJR5xknOcgW5AifFGTGYXTmOcU5iKyQfCIG5QstqK9w88JkCeIQfPbcrBA7kw5Mcftr_V4Vg6NamlO1l-RRvuEGP9Z81uBiP-MHLdiE0n8BcZipw-tAzv01lm49lzYSYvTTKlxoAIfZglgBirQAN0-baDQN3VYE9OUlGOyaFBAZ1JzgShy2Z04RRE_fUcvBFFNts1DIpNh6ddb1r3Pnfisw1efVBnWpDguZC0OQE8HGHQ4E5CxlWosc_2TFmv_mAocsGXYs8sUwZ5oAk1bzC59hC_fhO1UIj3EpDgBGrJkbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqWiqwORL1xZisx1euUHR7O_EtmdaPk9Qp5h_0d5PQra-YarPpEtmZNv-Z141AFh3dB1f4uO3JS_7b5LnMLXBzrQWF9JeVBcG9qsujCbpOUtKszhHYIyO74vD1KLjc5fmwSvMOvYWaxahj-7gZLhgcG8TKt_L3KE_L3tg2XjeQJxMTukyEUu1rBBvEljDvdtoZo0CY2PjCcCx3VFAmpd-MK5BcqhILsFcBZdcbHy6PqnyRwz_qPTsNfBb1fzOrCJePQ4BiJU52oWEd_J4SSA007VyFcg-xlF0j6FOphTravdSHTQx3tmQDDQCNTc5JI5nXw4fb8tmKVRs81AlzKdEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga6BNptGi6n1yRe6q80GPXAOtVV49u--5TmtvMzhDGaPqdw0wvN-bFrJRHX2ydSKyQ4UkcmyZOkqSS29Dl_NFZq9wOuUCk5bYs1pzc77prU5b9k7jXepq9GNf8Lkmagz5pWffp8SbAn2wXxrjgNELMynExrPF3yY5wb8P-d9ty_tWMSJqQjX1rFj2xdqdCSUaVIs6wMBW3WAfA8hX1yBorSikvI2I3VJaFJDy1GYMpOWnzTGf91jsgTyFMnn1jxlhyM3W32c6vtb6l7065eo_NpMzkPPDEUPnfI8smCEDs96ZzjPTcTrxOPMwBeeZngkhtsPqNPwYFyYr7tq5IPhkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 923 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 710 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuI4DxcLQVc0iWdZfoe-Me1VexSAcWKd1E25ih-8_-DfbNj1B-DF7q8_1CsvT8L6uZS-ddojkImapwDanJbLbvXmcwbSzsYvWHaMMNgdQwf0APJBRcsK3j-bsqf_AmrijpZfVAzvJb-ypflbNWKmxBxMHxStGMofxx3U0k8vSPEFxYnSIyJN1BiaY9p9Q-GuaRGm2hqtC9eDDyXFmgYKkdSItjOPlgMk9rAkXumr1kiV5ZkUxbuIlo8LQfeEDWb67q84N_xNrBm7smyB0xM9IeTxtWzllY1sHlYmIuDpLBURaWiSG2S2XFzpojw4YTIZHRwRohY6vLMYQCtbgOYO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 795 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfD72r6msWNnnW_4Y1yP0Xpcxo4QYwuA-SXH6TihG7Zljsl9tUfaXFY1jaha-ZB7dJwqbhgYXG9Rry4F2qUBQATfasiIMhFWPUvkQ9pLmFwHI6AleUeqoF1NnrcCOnZKJorZOjAmMyWVO6tkoCewbJfWIaR7p4_gLlcAbbBsDr8ot78C1UVUTMPzwEi_pzFcywe2Fc3vcFoQQ7GVaevUqHn9h5z5vKEpzLy0_NTguwVM3NZ3_4u-vCfK7zckbjiQC7b08nPbjejBJTEeJosVknkW18_7Bb78mSNJTxRZ8uEcHKIeo9gr_mpU92dzpIQdTwaboUw8R2XUU4gJICHbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 712 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9sOtjd-hM4RglrS5rfVGJ3ReCbDh11pD0eWSS59OSZKfXKdNVX9qjyyHYaMojj9e-AR3rSwm2Sgc4dxVyqXtW8t93-IEAOQgKuC-fn0CAMMAYJtmRBXerDU7D06Tvy4T7ShYhVPn92-N7ekwKckjnObsNrd6RQlv4ySekfjziZY87-cXm9_fi6vQVt8nNdnVI4HL1knwLGgStnqKO4y6MeHm573wBqKtr7Ym3WogN9inS5E98zlxRpggqpUoyVkMBmzv_K8plDJ_wsbms0yXymXuk96rC05ukj15sARb5g5jw6TDHewis3VWANWTPRE0MPOFZsd5UwctUjDcQ4xJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLBhCzNcPuwNQpUE5JsAGNECDKBFjzaymo8daBE_AXdoCVgFuomlhvi0MXIcxAIY9YF7ujuTrL3XWPh_FR6xzmOWGoWFp_ERV56IRy4sYTsNoMCXM9mikcix2BobHz6jXIak23DnUndKlTGecjx79p1-ur6VI-69n4qLAM9l7euVe-4AGE3DiOyIY1XzbllNBSgj5NAtvtA6UibvEqgKEtq24tus16uTf_VpOuT-XUNaxkhw36rPg0y8mVht-Cmb2QwEbPjFeZYOlCG8NCLqrukAcj7iqPV_ewlDxDJh3RE10Ix7AhRxo-KY-32L1q_v58ZUQ9WgAsLTp_McNtg9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ma6VCUUxNlVp0EQAoxRZh_F5EJlQP1I2qxQESAPUbVQF2jfr2hnM-8Ul29J2rvc5yzPDGqXqQPgL48hpnoKh4YOR7CfyFVP3xjUnpC5_9gMF_Dd1_6Cyf7OnfayChZmlkl7dRFvsNTcuBtKwmAONxusQdS7RjM9IvA1ui1Ar7YCjQCUzz_XEEu3-yJ4LwTQsjNATOMhA7H_xvyrjlpaqREyPten_3lw5sWtc6AXyuRluD3brt1aEHUIzEl_v8EuiqdzeAn7TxDrTWZqy4eMF0VzF69zRJGC3WIjMvu0tjxzrpkmf1FqlCF88lpgpvcpHmVEjTrBOdYEOGFcpLxKhkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ecn-jgoxWDE3T_aCQjgMgu1H9gfO_jbu1fAlQqAsXgl0DcEuZ_Vui1Mhsuxf4iQeegA72P4d14tgLL9zDJuS9jbAdsZcuVk3IH5vI8h7IaeKgm_CX2XQ2EQu2Q0HooPYvnvQr16WYI8NiCCx55OCiYNN9XVUNB1GM885D9n85UDftgFrsfYXBARu4yTrGT3PQZM8GtsMnjsvLt3-QB4LdAd3G-oN1ukmYOzi4mP8VWfgr93ZU7NniPNF3gmQQJYhzyaHCTDx9uavyKgpMFPlNue5g5WV-kWE3KhSG_X8Q5cHB3HPbr8APanww16JJbpDIy4SzpXXmPY5bDe5vTE6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kISwhfEIEJcY3GjUX7bh2FMRiRj4FTlAuAKeMyF4ighuCNFjCyf7311dLQSWAGpr-OckVHRrrJGeuAI-CqjAmffTQITJUM3vZn1kaXMoUIueIMjNjNyt6MMixi5W9LaUdFYSV7mLI_VTgycPYn8c7EXAiPNAhHFm1Oqzys96z1DXMvkmgxVvvrVJ5x9NxugYt-G5rxDnUTTLA82gTGCCQ0y2DRbaiZwnL2b2zmrC0rEeyqu2ZdNx9kFP_Qbf1hBETON0dNd1lPmdwZgB0je0B4vuSBTK5ciNdf3WPZQeSDklAz_9FONxKBExsYMKRNspDpXXvovTuHA911SDiSSJJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_CRtijyFlrCfaMuffX9cVM53ssUi-CWc4dSHCmScoUNYtz2R1ok5DA7yFbT1Cf2JT68Iqpk_nWKff_lkU88gYkjwrCusiAdk55EADYNgU_b1pfRzYgQVKjNhZRwAnxJRvHx4OG8b0pxyKZ3fhjM_nUynZwDlbHJ0BJg_LtoE_HaGf49vu_KXDtufMRAJNKar_E3l37qsJo9VX1oah6z3x6j-kDXYCzV6Zsj07Lkqet1HDeideFIA2H_vxv3yRvSye6GJtcUyyv-BrZefD63h-SCHXMhjUbaPTg_BZwGoyq-B7i2WVJmG3kW9Lm-nzYLoJNUBJwzMwM8MAAeJ-_u3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=C1CgfC8h0vI5JjGCNo0SwuROaZOvGSIYORQ-3MwWnsoM3s4PrRfyhXB7YoaAfGODQJp5pDrYe75JCKAiTpcMsJGi7IuFK7juz2GkxdCE9Zfq8OtK3BN1JBb8kimmE6ypG_cshQO5AM7x6bBLZdtAQqeXQAHdq6L23qlEdIADFx7CGl_W_YhDUJoVhM8wl8wlBaLeOEBG6-RcIiGeco9ENsDdToBRYgSMnTU9_lQ_tHiLn-NjZSPNUqqURfS3XZLA6OesANRWSPFzBHghFeuGFz-mOEVavOlUHM_0BQ5njm4W1dSi7x0hZz-vpYgAdS0qUgoZmk94a80cy0NONPagcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=C1CgfC8h0vI5JjGCNo0SwuROaZOvGSIYORQ-3MwWnsoM3s4PrRfyhXB7YoaAfGODQJp5pDrYe75JCKAiTpcMsJGi7IuFK7juz2GkxdCE9Zfq8OtK3BN1JBb8kimmE6ypG_cshQO5AM7x6bBLZdtAQqeXQAHdq6L23qlEdIADFx7CGl_W_YhDUJoVhM8wl8wlBaLeOEBG6-RcIiGeco9ENsDdToBRYgSMnTU9_lQ_tHiLn-NjZSPNUqqURfS3XZLA6OesANRWSPFzBHghFeuGFz-mOEVavOlUHM_0BQ5njm4W1dSi7x0hZz-vpYgAdS0qUgoZmk94a80cy0NONPagcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_HGhIp_Jlq2-JisJM6yvzOiPbdeQ-twznp8vHM9-ApbSkD9vyWS9LQAtMqGOudmFLYUi7APSrnuZJUG6DXVJAA_K0Q7cDAx-6ucMx71gFCmbSh36SWdt1JBWCXUPzDwiZxhQKLvfDhGNqkmL0Fdv_2IRxnZpqPdxY5qdTrIjRVvMtqitTbt-1dWz7ow_bkGtPGw0d-1MTkmvwmRapcL984c7vwGFZOiftUrlBAPk6nft5_fRGPWPR7ZXhXtzKVUcpGSCb962tsN-8vqqjYDt-Y6DgCuFdlPx-N_G1XfL4PsAl-dktWHeEnr1Nqhzs2Lx1dg573VJUPW2-d0t262ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKpQAHjJcFkpjmaQsJ-q48WZCJBJTGOx7xlooMRt-uyizSN1VDUCpaSLvuV9Ev4WlCoYOCPD18IaiTegbifbzAYE9VitLWb8R8HEkd0N-J8WeDdSCmumGkq6XsfCVVTtzJfPHvWnKy5fQs0HhNhs6ZquEUUpRcVi43f4MaSdFPy98_-QwWLa_zltUQD4zUwgnNsf_Trz5dHcCcvv77v2LJREeEdWVf2vhKg7ctAHOOImIZQyiBxtqHWFlzo8oFhDKqU4Q7QoZb-GRxQN3xjiuAh4WbGue0tNU-H-U0YOzHeXXFAGdxeB4W9YETSEWEPzwesdCKN7oIuX5xF4YulxOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 796 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cs5N-lHQTPHzMAPI2U5aCCSLXsDGgqXPrsPaeHBRB_Z7lohqb98B4VlkZ1jSP8b_-yXfGEDAIypsDPlBckrsnV9a5bPOdPMpcZgDIksrxCN1YS5mSJ_nZgXJDOfh6WUUqB0D1ZCv_4kDBYmGgMw0N1qHQC3L0prZIis95jgsd3u-Eyg4MYO7XwcZJTty1eawijSylRcH1eJLehMDfZnU-alMSptfuan3Uv9lQdDiePWlzXfg4CS1qfpKa7DTpWDc1mBJd5Gv8dQNIP-G4StNx7NszrhmZVyF-hT78q5A3Wst9pTz852j4tGVOX_kRlIQ0zn6ZdDrx3AF176bRfV6Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTChouOecGkzPmKvucEoW3ELY6hOgecpBVeWdk1xJi-MZKRkK2F02o7c7UKa2Zj6vLDTWD5eOTjeXY7xd5M9L0vGadxmi8PQtTUCxzeGG99R10EAzWob4d1_U9RasWPjceoIxkEEdlzZto98JcV0c_Z3Kumzcx8XU9wP2G3AbUUtGvteSl84SY6ndUY0UhtEI1ZyczvmeCxWi8G6W3CdTHN9zDdZXmEZSgt5VgT61-kGBzkNkhTMjsc-xsHcr1kZhLeBFM7dwmtAN97DdecnbxHpxbdh6z0qZ4FvtgbJK-KyWHkzjro06n30JPI1xQ5V3ocZbt78JatEaLQlHAzC5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b61qqSuoeJdaM9bIJJEsmAxSdHnbDIH8973rWn-e8pmbkiqvv62EIUiobpryb5-5WLnJyYDr7NNo9Q9KpTBL0pT_whe5TaYMNOuLxlAt-FTUSGeRxWlJnTvCmA8u8CDjUxwLGmT9SsDqH77lk77jxPcSH44dzOXtVgPXO-usfTe_CMaaAqgnWa_V3hjxwaGRRRvdY0JrHor8Y4_WJs9lQsUphn87URAx0PzRXZ0RFhcHouMRo9AKDHurK77MCdLoaBOvK8QjYQpfUkbd4PXL0-hycKyr_NLi9_C_oZWHyP4gOPkZ0ToHtuLQH6sugDyt3xWDoIOCuISRjXx7i0mAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9CT2I21WxJ3X6-Gvm4gFTKn1feLDQ96mtVLR3v8BAtloSpBbvp2KepOVPx1E4EoaFFMC5h4tByuvAhPCVMwj1Pyn8tBAkQqkUw1-QOoYn1sJdmRS_U3_hs1BA8l0lT_JAmza5y_DnVR5Wo0UpzUrUXChbVO5S9RUZDHdsv7jE1L7qAubIar5x_m0n4xd9mNfqro02V9QzQ6QSbS8sP2dcFY4_Hi0_odsvmPV8zQN45FJiUOVUmprlOnXxsjyRS42ENGREolQaU69HIVSiqtDBbONG3YHlpTHASG2f-DsNx3w9OviUGQwMG8hdWHL8sGiIZcwwosD2-DaFFxzL2sMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 759 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1mLVAYIVm-WCnswB4sMYFYwx-ID9zXLy3DNSY-XiXLCNS1_-hOUCSz2wgDogu1euSYhIRdxSfyDCU6PIA9uvgGm7XRJ1TMRuYGHx_p3sZFR7S-5p3Ta_JwLq_B6gL5B7cYyXqPHm0whmFys2XhlGB7N1bJsbNclHTZ0mybWs9YF7LlLQA4kA9R1bYgSwnWF4j3YrN2R7oGQ8GataHHB-8eXQMrFCMiTRpnaQX7Ko0v3il5jIG2YEwX2Gst9U6bvS3d9WFRpfk1U4cZNGk7tOnMkr-_bUoIvPHyzcJGPWBFGiIYPC29xFo81GIgBvLrZFlBawE6iNXX9er1ki6cVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJhMP3T_VnycrEYsZzwGqn_JfJ0JFS6OPh9XdT3QeYvS4l-GCO5jmhjYO97f_vdTXhNQedk4ZHe5kxJbuHXOESHfoQ9rnePv6mu-rpLJ8LS_xlNZKqvbEsrFxwnJwjSa5cciCzLVXtWXYvXaxCUgoYN026QP3myqe2Vo6l-i9NS_424vTsQpXLVXeU83aWHZgXb3D-VZvpUhFqREWYbgE8J9Rr093dmrpY3lZ0WV2ZqKan_Yq3CG2lKhBAjVlkZtpPt0UXxK5q6tOMvvnr9YIEPze2D8ynxcQrTHbZIAAQycO1NU2kxQK220Dn7Cn-aMVgaMjNGpDyp6kW4AiRY_iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNrsRos-C_DiDVvegzj6KhbXk8GIdNXTKFdakeanzbFFC2WFFW_6MFedfp7SyTHoXuBBw1aZYqonBNFhGJopx7yTg5n3i45Mpb38P7qtQzFAO6FawICsSmf9df8IY7OGx7WsXGrOOKtPYZzBXQO2WKj_EqLfMkpWBvz2kK5WlYCTenv8AaqXnU8IKbDH4OQXjD0AsVanvlSIPi0NcBwKVxSYdoLwhbrv2sRRsvXqSFzqHxvD_mFa1PYKlKEMRl1yDo4PkFg2JrJZpvOgcLvO14L08B_Zze_9PLhdVDiW8Wl5DP2rCjqSIRvYkWjO-EJW3teGLw7kWq8b4optYv1LUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 826 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 732 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ4AoATrkZ1osyeMDiPwCCOkacJ6OOBBQRfiyt0jqstUM80-BaIuGOZd8ckHObvbDiB7UW70I8jQ7ClRXgd5CJnuOrJvWeBSlVnhXptcKoDP9xV163Zd2pPPBKYUW9Am1eE_pmIyw4HIMukpcpESY97ZPdrxwksheHjAgjdLAP1RQ7SZzyE2tPI8opU9GKOGtLGEcTX88meMoLNTA5z1K_L4aaaaFSc9QzGizcyR4WpmMitqeEtO5wI_DssW5vclxKUBMBn5y9gItt-0k8jpwApYnCENHFnqVHoB2o97uX9y6q-1QFOAOY6vRJCUKs5hZ0JzQGu2vFPAnopgulHTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 831 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkUcVjY2H02C7awwAxPyZF2IcnteDrte5e_Qa3RRVBGzupQmigw4v1aTmVvXpK1d0DbMP8IJNHy5w2oAjj0zT6x83oGuCbMubsOTKJwSLd8NXc1PuR0HO7aPnzg7ddcz9rbVMQ5y-PhwnaNEteaApFC8h9UlwAa16ytPaactf_Sg_lBfEygJNMeFQmakxjohGpmAK3m3ae36bBSF5f1JpQv7MurLJ6XhewEiuQan4V2ZZQwBobSaSLEhHucKgT-IPd-1pEzv4Kp5_EAOoF_Et086Bj5uOZt3t5GXAdFzJdB2KtkxB414_Zizcnh5qL0MU-oDHfQm-cg5MVdnB4kINQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 614 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwGLjFPIq-kXd6y_Gi0W8hsVkKuDFekzYn4JS3I7XYVsXCw5d3fwytkiqeDSmUqFQmQd9rIdwLwhvg-4MiZLUM-NJjc0_4ipmNTF-LZpGN7to7bq2mUxJba-N_nqVYuiJqm2MPPopYR9qb7evWx9TzPjqE37cRO_EwwLdCR6fqOEKpDT4fVxGjI-5vfxQxKT8mAj1aZDD7E1pyNjV3E15lpnQEJleVUEJf8_DgAl3eeqHUgUNMWGBoNNXPkUa1CDRS7zinku3zvNOLG25blxu3dwr1d668AOEWfMzLUq4K-2sTzoPUxBApZUOftoT8ixUi-RP9cgfeP1YEet5N5wdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 651 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shO_mS9FcN7LOfq1NvZR77C7wJJiPRkZ5i_gErc2w-e1tj65WX5ykN0SEXrWtZxxC2ZG2Y4aEZsprsCoF2RmGkEwxDeNIM40ilB4qmiTF264LEj7_H-aKeEj9vu2eststvc9fdYoPLNESU6noJRBDUBrMWfAVAi0P-f4f50ycnEbhABLtKukdpSe4QwACrcOAWPDsiaobNMlPq5r6DHf6uYo3ydrqJXxvOVE0mFaZ4AZOgqxaEsuaXS2NHEu3Mm4HpBBDXVl2D8c3KlzLghfygTVv8SUvkM86GNHWGCsEJc2BEuEZqIifcJCcdYkm1qI0oaKxqDb2OheLv0cp48NhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfLNPswXbiGgH3g1NZALnpeSBIWN2x63vv3c16aO_m3BGSyGQTQhGHJn8zP5QF2XDN7pZtE-Spbgrtp3hhnifsfPSLN7swKBZ8q2mMqL8qc6iEcBlcn2bzy_ULpboIG9h--DmyqFoCkOLQv6afB0nzdjOIdAJy5HLy3mV9CVVqo12D6kkxHJhgV8sV9P5tslo0pAzO3vw95q78b-5WpfpCRNh7eq_fOv_TIQTACIjPmZN_LORZNpEh7-cPlbpFbDik2tUvb27g1i09dNa7hF26VSqeZu9ioKr00G36B_Yz9-MT1aBdgwKtv1y-C6spngnucFuvuU1ZW17ihm3aWwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvVx89JfFKoCdyGEdXSZsWJIvcJfGX1FEDWMNn64HNsoldsXqYkMk9PuSfej0bxXXJo2ncVq5XJKq6c2L7-JhucnXaUClK7aFsSjMsf5L0vm7ExwNWx7SxEAxS22YEfEcBD0b2XwaeD4vtNuBltbF5AHv5jXLWP-khacjUcr6BN9GxlVSJ9kGSTcHg8oe91qRfIwHkYQc7rN9Ef9Jb5QBEFvggyfsey5TRX7qi3xwgOmTuaa_4Mepyyxc9O6eLOY2Evd5a_LAbahP9ypTDstBUId-F9CkHfXNXqUDiw663Oskvb5M_Bta4OcDWcd86sUaP9qIRmaVOwdSujxEbyVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-WYMXqCpA1-lnqikhdZ68UuAqhTw2MpmINHhNn_JyJ_BNiN3gnlTxY2NHmn8Xyh8vzUr-yzBmTMgQL1EgEJUewrex5Dnm8CSW_DwFtvdcCJ1VX8fYHhg-bgn-GUHUcsmHYV7oymWKRkWNXdnyf-AfpK7O2jP69SEpzpSJCo_1EvQ9QpGpoTM_gvE_NSgPJVPFCATZ7mEMRdYNByBQWijsnNUB7DCzTCMrH69CiKQ4Agd88-xnDXQV67UEfKLKw2rdLFJRakLr6FnQLGzrCOF0lMeC9muYtz86lRJJOAE41Sxvg2i1LSOCir9jPuzMr7mUHtUGo2Ft1JYe8xl6Chkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4k5WWXhr6kmlK2RxmTWWg1oeP2DvNvi_eYRsMCucEnrwjQF2f5HHGnG2f3VJgdovHyX5AWV_tZbNTW_nRsthG8WhNuLIst-Pimyp1mcKS6w0W8Jermew_dWeTiRoXlwwe4He1yqHNkrWlYTKB-jLhPNxlWe8tp3R-ULoENPcyuGUxR7vODpanV6gxk6NbvbW_Z9rIqcOZkh6LPajfimjX4jhZLRVdNBJTJ5jHCkotRQ1UkMnA-C88lqu8GWO9FqrikLdKcsTIWefOtjfDMRs_dKH1-k1DSnhG8EFO5M5XiLQO15zcySG45fDRa18eI2XfKCF9dDQK3ysikSnTzd6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvMXlLFOxvkZdB1bkoInqw4YizwbEwx2CLkhQP1NXqDelSSaV798PCPjlOlPElvBZt8hHYvF0yELXDgRk05MJ0hcYbAH7T0iSZ7xrxCIb7joxc3O-SXmyHsfTbO14YF2Qw2QcvadnS0rFilCEgtWSm3rMYY5avHQ6hbO9EsQCWHmQ8lsRsSE-xksSAcIYc3m-NS093mHSPHzd1oPurdEWPktG_iYOk0wvNNh52l90k-__LQKZ5A45MH4Jn88tC1IHzj9RLv3S3qg0MY0__Z6E1_KhZ5tI26d5EOaKFRWWV1Q3ZsL-AJcCM5MMqh1q4d1KOCYiHYeuryFTI0Rfav7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 588 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMTOinbtgVPy7ud0Lsn26CKd4K1nUY34cUf--8_mU4eajg5FRE4UDqIOVJ7sU9wffQi5gB3EE9B0tBWm_SjR9N12Czmf7nNWn8sCTVjPndt6gJugcoFRdvp4qf9LXvtrS0QCLG-dxNEfisHnMsB2YZjMBgJKaPf1Nlqr44tAYOTF6AYOCFL3UfJScFKvwYur3cSJOyki8iRP0ekN8nhQK10u08WLngQUYzxSSTRYWniGpAwz5IOcfghXsHzuIeiUIff6KxvWF0z8Jmc4hfnNJJ8J4vA_bY50DfSp6Npuvq33XdR5EEJKtFkoaqglW84m9KpfKjUqgxe9EEAftVYNFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 602 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMvSzdCVdR5t20ZwoAy1BjwpioLxd_dVzvW-fXN3FM097dxLzebmwafeiJ-W9cUWS_cuRZgheDAfmlDGsu5PEtOMomU3b3Zs0fvWCs7IFniPGKzUxD7oLm1yfduYo6SNSPBrjK0Gzai6EAdCSXrkxzNe3zt_EruSJjvzGNPE8wy-sz1tn9sm2DOc6a5ITmUGpjE_7fzluOoMdRU_Cgt70Z6XZGkRT9qHL0u8IFucS2CKtTuyxhwVfj58LQ-Z5hGNlxA4Jrka9bw_DzLlP_MO6sY9IVDFU82RALGHtpDdEi2HpB_TlEq6MXmuVEUQq9nVYlOyYw_2pPw2scRIifHurw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 712 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiXtND_k7zvEDGJdqE6cX1MpNJGiqynWRZ5m8LsvyBVFuv1atYUMX7zp2mxFaCLkFfzVsAGMzTchMQow7OH16TBNb3xwlfviApGnFp2LaNbuqGHuB5miztS7jxJ2-Ro-7mRCRAxfEXpG0qPaVNwuFpsPEsrJ4PEeOlDA_t4O0fu6AEJf3Crcv4n4cfs27TSRGb2q35AFij_tE_UP2K_3NEjEXPh74giV0Sytv2yQN7tjw-RdwpXg6Ru52Zs2XPqxStF1AdsHSIEp5wHvhdFLWYWQtbG6auZA1IZCWdBJXeR-bswT16ihWXMAk9C1ZBSI8ZCYf0svBB6nqLPINCqPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 654 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-iWJ6aQ4MDhZA-uORrSrD7ILJ_d90Rxbj_v-M99vx2YnwO38sgdqUcvYbWtaWxruv2UztKj3iJNuph-FJTC2aWpbcxRlCPTu1KRNVLKDGEnkqJnMkWjcCEI19qa2uiEbpMEMlRrv7G0o-fI17LzgWtpxkmhj6PuSIkj63lgL0n6Fshef-_ODFasIq7pc3M-DV_TU8DsLny-EUu1dXcf4udqOYLydYofzh71swgG6c5IQhmx0shVjif8nR8Z4d6RXhqgyOKvTGJ1qHVEUW0dUpgUKiNtQXB8y_2htWG3Rkz2Yu7nQ_CG-zNHr6M067LEeSHJ3P5lyGjJFacquFDRVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 723 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvR5XRBAVnp53mwEiMPR7zjtWtKZs3U3UoTOaPmHM_1MDctjmdBZx7HtcRNCfVFWxz6CPjjdCqaWiUYpiV_toT601IFNx8cnQZxmCKSVARmAdIyakIR5USzuwscBJEw1Uc7cGm5IuB3ZvN4cPwPo40uuGBRQfnQavFO0GDZOOusjlQLZFUNpO9a7sKlBSi-mmPPLAjdnTiCTByYFJNePR6wfxhj0FsUoH6IDhXevpH49sceZ1UYPRk3wiuNAaXZVvMsx5KCSKdDEwd49HIwmPuzIlgs8nXgvoHjD8CtswmLfg430XTT0rdrFiBfKYmMPs_FKjneaplTiwsQMXaFwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVJIp-_K_SNUtFciCdYkX7xBLrPjd-H_82H-Tm1udrJ8-5NRCP_EgHGTYQHRqxjB5TDbvByP5nvEV9ShDafR6SnGvzwTXKuZ9edirh28ScIYZWHPUb8PxisoEf_M4yXBRn62g59UKui7rkju3RhK7-Qn2m39C4BrTbMHGmV99AWm2VaXniGqez3bvtKRm4GwkaeTpoKSGm3GUHoTRgzIxrUVKCe5qC4picwwIcEND7x4FnQu6lgjuL14LMhvUdLccfi3HzEKCEdRsWMbpzYuwTa0X_i1ffm-otdhmpdYI1oiZ1bb6IS2SIB9a4KBx3tPAuYigM_SctSHj9dqn4kd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 650 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbJ5TyHbRaXA3PVXzKsxu7m_t-1z1Jz4Xia8RtKgRUvRqFd9aHfIgtGou-AkonQWUX1BGQaNAnVutobAJqSI4VrBvKeFC7GFOwZBXLLIP-somMpv9ux6z7bYC8Ge-4EhI8W6VXtzhmcHHTPpQpGftakpF2TFIwhxnayQ1IEmnF7VWePK-DohHfyUinOR4Pul9fZnxklYbVm_fRf6ss2J1gmqhU5jyEOBZkTGFqj5lJ3r31VfwPs_W9qfrHyTAeIbuagoEuC_Gg1SzdjVJ1XgfGSYMItybVud8qahw0KSIJOggR5Zw5WmQWSHfh8wpnVqX3nNw7SRNYB1v0qLjtCoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igS7lIAvJQWMIixWefumpoR0j7PV44g7o5sxWCYFajhEr6hbjtHXKzjhtTenS05hJBDnRqe1fXQbj2zOwKnHv_YXNY07xjX2i7uuSEQbGCoO8LkWYLvodvjxNjdXmzxBqsLvYhLWGGg97Bnj2YJjjPl6BQpdFtga00WtH8yTYE5DosBYw6ubCRkhr-07Z2p0o7PiihZg1s-FYHL9BqvXs884PA6g4LlGx5hOmYGgn2uPt-xbM-BQN9ho215dNK4HQW5SqfeTZxPc_DQnXiH0PUThfK8DhW-k1yGdgqhSM6ITyHHqKpffAxBDn3FMJnr0OV2WFfhC-HG6DUkC9OFkRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4fPRnb3v9ddpptitIrr8DMYDd4BbdIQ6IjeFc9TqWQOo6AhI71ykz_Q6NRtJu6atv2rxPGmGuJ7pqv3Mk49eFMzVU5ag6YFKDuJ1ZYlfoslcdQRijDD8kPGWEYQeU8I31kIVpx6L9xGLwZV6UbWy_ikY2rsmJH5gdrh3GvTX-MjeceU-uyY6cMZ19cnIBTOB3_MOWGGgCfmhCsRWBz9hvhjK0rWLXXpvkhJ5gU_mv0zf3VnP2VtbscD0QKTg8vfX0xr7UTaLh7HKmQcU7otm61JZRVmE2MnnbwV-sWWRokd6sBI7MOzV158_X5YdO50Yau4G-07NnAc5yKH4uLqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 555 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VR6wvLlntJ5bOHpmZQYAWb5JblDAM6bFKJgaL9e3dF6E9ahT1Z2IQbd8tF1H_qteYSDKZMDlm7Un5013KEHFDlpPVdywjf4tp2rRsoXDuk5ilkAVSmkhaYnZkL_VfaDGf6zksFktp4T3VJDhxlKgPnSzlHYn9203OfqIFSad6bbamwkdEVxJp00Bj576oejaz6ttbCUa1JRYYJ2ue0ry7kWGxBnZpFFl9M-Nxc53KuKPY6pFZMeXipS4v4uF1_JhDrm92z1esU1Xnf85WhPKmIZulO3GKiFvUQDOkwQxh199GzWaESGE7Htfg93ygLwKYsB09qM1jIb58tuC1HaZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 554 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnJ-j34A3l4gSrk3tdnkVBrUVoGlJioIcoq2GEI7-id0ZS3-FjIlS_qPa_UanBaA1jIe88mi6fHGIPlZwpfF6w1CAcy4PFVBgXlVh7hwa_vXkTTN0WFAugi4mUcnMBcQvLFL0pV2QhiHC5BDtqVLA1P0R8LB_LfDYqZ9JDUm71d6t28VObNrJykr1eE9tqK-BhurkqHbmncdVFsM8P8XNLWy2v6zfQSoG6SakmIcxq-nONfQG8FqcITYhip2UYlZoNKbT1Mi5Ln9iKyn7yMHCpBXI3-BXfeTXWnITfp_tvZW-lMIpuW9QlQESjotunHtzhOINHh9Tk1aHxu7Mp8UzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 678 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxs02-mO9LqYCPy-CG3yXNj0RLHQWZZVpLt16Zxc1EKd0PjZh3TC6fke7_vrrDnndAcpbwdXkWneF5V-3tm9OADxiu_bOpY9dHVocFle-GdcbIscFreyj7SnEEGffbGPYBvIR5TgbQFN6pqLw4JBA7GQXeBP8J8Ky9LbHWE3HE7K9sn_rJhirR0x9Z59XwPCdvUKn1tAkYC_1QdrYu_WfSADOwugybOdzcE4MYuVUGBMv5xpLel7KgiwR34z5P3CY-cTli1m81ptj-mM_U4ifTaLIq40juxpAHsDf7Apo13marWya7cTmBqGPMwVRZSOsXI0pfAyT-HESpCGDOTfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 698 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GC_P7OuqbZIDBZKTk9SWz7meVYS3UIaxj_tDHE4C7FOAZtH_Fsgfkyfb4dzpsPWpRmpYVXlFFheCtmJXsw5C3XMhqjePMSa52P9JuF-AeCvCoXsQDHA7cprNdO8lCl_T56vTCNZMtpAKiJ1U--cUQzhr71YD7QIkjSyWB2cKkYjrvfHAejazzGWokSsUs3JXspWiobxYZMKRWYSxecXI0CCQ2jZn_zB2JdqKfT2SLOUUxC-2qSDGMiG6awlWpu_WR4XRDMMWsYVpTZIA_S41lZqj3cmPkIgu6F07_dpcOAuOnz9ED2uSkKn7a-8rPAbgTOsOObSxtWAl_XIsdL64xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITR9w_wCbYCugmfEHboVhzQJnW4cLpkASgkS-E9KWSLPYrMztGZX0gpMNrP-XZzIIQwvmOL_cTj7xCnPbf8h28WgrJWMPe_BPXwa3n9jZRR9M1cv2-ADezUvfyD8QX5mQYVvPu8N_lGSfeYTIj1ihq14R8JtGNWPONm_GBJ74_QrulxFp7mxO2uJY4O0bfnKBekrZTOKphaDPJbWymb-cRuwH-ug8BkLeAHfMu4fXhjaYf2_vPcdA35-9_LATU-XpWofcL2NqUj4OApQ7uQMCJafZVCVhJj-KixhUmL3XrsSoDZFcxL1K60eUOH4yAQP6JSFelFsXTlyq26_t4jxtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mSy1dihaWdBAchYy_CqwWbc4h8adKeEInXv4HLwrYfAWIps-fMbKXNS6UeCL2urnBKJ37mZ16ta5u3tqEljll7c3RUu97ML0Lr8uevPqh7jWZ_dVZUW31qh-29ZR-i_oDgIUcXG4t5N_BCDFI4ezECjKv6PM8EFNcqpyMQulezr3vewmYVX-IppnqFOBdvfUaDd_9hkcKBGxQTWMoNw68uvWBdX8_1WWCyuIGSGKPqXKUli-5fgbWlXk0t_qVW_Iouv4PKn_i16I_bhe246mAhebSbvRoVNO6AJVAPEmwLtU6PdD9QCctAEEKD-_Gqm4C855IGxQ-cMjHVLn0GeIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kX-2vXBD0qG3uy-j_75qtZxRK53ONUbxM6QdLbMrYWXTc5mi52Z9Val0a-1B4xhvWmxJqC1LMtHYA3mAm5lC1POvRHhh1p0JR_HADXwJmrgnX6HOq9eeY2g8efjPmTORDLnDERUfe92H4quforBMSLJ92xEbbrqGYvF6UeBIuS5G5sthJb1JFb5fDfapW_AQQy3IkgGbKYVFY1WlyJjq1v0TLgh9XEc9JM57EYsduaLHq3k7PdC0WN6oZt2HdrSrjh6O-rKHj210uyS8VZQBAjK9JfM34AzFttwxilwg4fJZ8Y3GG_oIDOedYD0vDg7cA3cORqtkSoPtt3C8bCrU3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzXjPj8Q2CxJPpW7KvWZA3Kw1nZvUT5ixsmhpC6FTzBCgq5XsSAz-HzGnYYvY68tKm4-0CX_sCZAHSNNVTbpnkH9kNetARKz7I3WFnU2_Q2tZCF6K3VwODyVW1L0tKjmUP9eAcjBiaL-rA8xzlN2znLnu3iU1mOwSPGyv_8jPVxWVp92qA037qrSrkrG6cd1JPNVWdltpXOQ_fclxUDcPCUzrouCcziegZlG7891ZGSdz2HourHfMKEChNc5zMjK97I-PfRE0AiYFmEfQ8bnAoEJs7hFX_153prId0EXoRXq7JUd7p3GsY5jvSbAqe7eku2bymRBcUX0lIyPpk-eWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 593 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 590 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttpIoDDNztqhGYeYEubEBLk0WQq46kS7iJaHsdxTWW5lgUHYbmLpjzY_4gvMmRUhAlGpGUL9ITqbJCP1q5TBehDiM9eHnmdf3i2sNFio4WTiY-zbTJH1sEgKc62UbRFP4I8vxl16YORrXTRScj6kswCG1ngc8IBYrym9LDQg5h4ZKqbfABhxbGppaL_hurkFSvEBt44pXwJhfBrjP0MjIiqAwzNkTlL2haNNfonRwc64avi2mnR41Tl1ldX3iNmh7UGNH9nRN56Q7N7RyI2T4fHpJ1qClRatyg6Vvr_JKvcMFxZdv11zjEbW0Pjwva5UxJMaid057RK9NfQpV2Dg5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Am-5sga2QUVT9RI_tZKHNL7hvd7bGhEuBfraRGbVIf_Z_7VsQ9pS51HhL4eCiZDDqVxtkW4aMDcKa_mVroVEWVkdn-awL_4wT8mEiMJB_AmPurgUcB4sR6PXVNP6F4zHV_nycXFF5feGg_jaMDQJmTSxFkSkH18Fq02RFrFgTuPYTtcvcSnN7AbEhqvmYfH8WBxDbl07rp1rpDVwW3Z0WeJnj2irGeqqkJ8TeW3r3dvdgwGb1SBaIohZDqY8yuEyvlJwrAnSqqKEjy4Q2DO3_ZhSVG7PRGuaMXc5GubXp4r8xHoF6w0DcM1Q8H2n2NpOLSCPkk2J11Xxw2aeScK6aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bl35RCtRccBQYL1p_5HiXDxbWg4Zdf1TG17pZONOjE2t_7tDiXOhWLqXtk87cFAUK5yeTaQgH3h0UW3Knps69aVO2RuqMmRrTDP9_1TzBIQJ6sJn1F0bTmcyz4_CVF--4NPO00cuiWaMCeas17eSOimPso7rEgIvdSBHAhAKFbDX76dom4rkoIQwXjFx7EEg1Q7rS9PQSQzLMMTJ42i9CaJZ5_yW-69G3rtERQcFijH9G2X22O6EkzMmF6X_XrXEVvASZ8QiwEDKf-HdeF6XLo2i2SLdHsZoMhOQhz8rHCQ853qErj7upcSYF1rN9wTjx9OKFVEyXXCuzo7SA1IQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 722 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiAsG2wYED6cqX3ncMloxfAZ5AnTpaZwSdUWUCDlqhCERkSDKO1Q0oAcxG4aB-IZVzxBNnQgxs7Y6BYnDJ4QKEJ11TbR2xGtIEfiBssUan3Km05SKs65p0ch8M9gzca0ZQRvEs3IWXewc1EiXURRf6LptOFaN5itEISmEtadppEKfxnHr46Xw4swtkEkZrnvNDtqRDsbWwoqZLLneOHfKYh98qmuCw09M2WKtGQ5arhyTP9mo8Dbw59wE2-1Z0T_vMF1dJ0vpihhYkRcSZyIYIGDOI0VFEYfGD-SWEbzRYRvh7kVmtAxbqOysuueVftgl6kvguC6pwEJIvUCKiomdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHkqVpGAEhpbxZEzANycRRmCUyp-zQJnHVobFNh5R90C7uNnVoUMZsO7ItxGWR7bdc2eoZ1NqUO-IhyWU3SE7eWguQgblL3WrqrrUF1gSNlb7-6nnMSuusSfTi1oaDcqt8Ga5B1E_LqOP9TBujEiMgBWon8JuJ1cmmvXb7S-OFD909i0yz6PPNUOM9glKB6GME-9qjHKGM4Dy0eLrY4pKp7RPtO2fLZGm-l22DQCdyiaDf0mJFBudZhO4ifqVFFO58ixZO4Kd4dMmW-ZCyfNSa2YDi2A7zcbWX4uzpkvFMYAFS8gdl0Zy8RfK8QZ0qUpRjw5dhL-MT1q8fLcxjKD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aA__lrN_1yCeBXHFeVlmUImaCVDto2k8zjGHBIYY0y8vFqnEsFjH_b49fCvRIZm-6QdPxvbMzBU9moaIme8pVKPnkPunTEdimMM_sJ1QJIzUszPKoqX3obDNN4IKUNyEWZS1hOJllcHcDiOMvn1T_QJ21ALEDjfuCU-gQY0Lyi5pQuZfMmk4jjhsnRa9KKe9Zxo9VGRzIPhaO5zkYakIRqFXmOmtIu5v2AKfhaznVChON4hjRYNK8MFE7Nyhn0rSmecEF6caOol1NWUSthUFAQEeXcMxlYPJTMZdKuZanIEE3XN0qMYatJRQgOH8fTPMCOTvKo-u5uffjc46OQ7BxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKUBsrjVWPIYuw_WGVJ9JuxT5KM7NrmU2WrkTQJ86BsajkHgRbsHhXbS6UV0oXzkjuhRpPZgIwgliONpzPWX3nm57BnWn-VNpAzroOMJ_Ah5dzLOnv_toTBD7idfMQ6toA4YSeFi0nrr8G3874rEx7UBZU9Hdt1gWykY8BsNDZwvQLkiIxAojri1afIlJJGD8VVXYFh1OIJff1IEAInsBLITebYf-VX37yExohm1Bop4OW1cLnEbLBS3aE4g5fItyBl3--JKctBqcGf9ps76ArFsNvyvo3A94jDMxw_-tbAOOulxF3R7oSI_mFgQESfqls-BgwdDjrtPh-m1HahhTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 615 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abZ8iXlUR21I4cQ7XLA8-ufH2lYtNWeGyX9jw182-AdcipxhDn4PD8ODbXn1AmP_hGMwFJrHeF_3PytwBodujAG4hzqoWf94Cet3lNkkM8ZwN0gNepcvgtgED-bRrxhimZIt4dBN5Al_5e2UGrueR7nDGhLegm92oTY70EFeKT64bSUpfqZQ9pwAYvI830r-e8WNrthaiMUeXRVzd--mM-BHBQq729RW3NjBoMUlML2frWQzQFtUz0WK-uaQY9sCmrB3VnSl83Rwc62x7R3LtnuxhOytoxSR_rVbvINcFwrA00iCINL_1LG3YKguzfkbTG1Oow7kHEFn5H1rww7VTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 626 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uy_MZg6b1ub6AoxfudUpIlSKGNTOClyCksTl97-JYYkBTe9fiimzIBS4ZGpA9KIPOFeOlO713YJ6_PgK4R9G1iR9SJGO3oNkVe1vhgtBV8lOH3XoAZ2NBpA7tTiX023hDhHHeMZG8c8OaO3-8aedKWBZebpVXptsf1LkVLe_sn8NdPecik6TFXdtwDBVI94m9Y_eZPOLGv7ccc9LBAgxIkbTFhsiJtX9OeheXyLeAUoRs06A-5DSTzwc4YFUQgHCttfEoqGJ2svIviGyhTIwjlH6c0H3te-FtAErrvyo0wJ_0SNChTK-sHlrUZxWl3rti9yqX__ucAFd6OiMkeDLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 617 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 680 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 685 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhGX-5x7x2IqrGqcdYIOC-G9MRM07QIDJDXJv4fBkCN_oGidJTBwruWJ4iMT2m7Mq1E_BqSt1aU964_wIZWe1eeEV_HDTM9PR4uhzTDy7QSG9opGpizUIaJDXxBIM2lxtMr98EMMsmGffkS8MlpaZZmR7NWjjDna8dKP8Sm69ISJ8XelR7cZjNov-XA6ty9QLa3K4eQVKxUP_TG0Rft7BjX8LszvkTp8gBtUJB2WfIFQ7inxI0U0gkFRu9d3odQMcpK1MKHnxUPrgth3hs3Tjzj-z1j5wWmC9ESq6D5XGVo8AoIYVFyedlk0GrvPaqW-xexL7wruZRMnzYsk3R9bzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaCMN9mlFDoXP86OyxcHb6njLkcVrf6NDVQfyn1WwXpQImL1zybR-893dZOEjI9tQovqhcdPstj8NxJWmePUX_9ZPvfQvZK3n-L-SWbhSq3kWia6nq4qe7RDrZ6BO3D3GO_-f1P50HOPUVkxQSGfyvaLkzddMk4AqOhmchwNVHM6f9fYem5cPKw-BV9YPEDCEwkx-6Yrc8GtUEFBqZcbmRIbnG6mk09fue_DxstNZdT0oYab2axfiLXcj6VMZik0xTfmWC_JAPlrThDMCn5JL6p3AxpF0Sk9ibFq0WZH-88b1hlAcZEqYPxDfqiMZKulKbYJEc7pvO7HoiUFwcSTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=KBBLqSLp0yv3qVDmoQObMW-ZTQPzQ3Bq5Zf5Vpqvu6bCD8eeghKRf2pk5lODjDpUjErfmOSkFUNDMRJ_LxOMBbS-0NU_wL96ztU6lNoZdytFzJ8db6dhJLurUDSva1scRZGU67LWmszkFbQyWpk3c2mfiWZ3WC__lLLbuMBsS_F8Hwy_9Lh_FD2cnSizlCsjHn1hQ4sSQhByBd39HpDiSGLpeN6tldTZ9-zyOjV8o9-O55ynh8UjujIsuSOfPAFoJUZcLHe2iJDh_NPmhs02uH2ebPcB7qKqZsW3oya2DdYEFtRb51idVI3mcDqtHOYLspit-BcPIQFfaDZLRb5nag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=KBBLqSLp0yv3qVDmoQObMW-ZTQPzQ3Bq5Zf5Vpqvu6bCD8eeghKRf2pk5lODjDpUjErfmOSkFUNDMRJ_LxOMBbS-0NU_wL96ztU6lNoZdytFzJ8db6dhJLurUDSva1scRZGU67LWmszkFbQyWpk3c2mfiWZ3WC__lLLbuMBsS_F8Hwy_9Lh_FD2cnSizlCsjHn1hQ4sSQhByBd39HpDiSGLpeN6tldTZ9-zyOjV8o9-O55ynh8UjujIsuSOfPAFoJUZcLHe2iJDh_NPmhs02uH2ebPcB7qKqZsW3oya2DdYEFtRb51idVI3mcDqtHOYLspit-BcPIQFfaDZLRb5nag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DD1SazqfbVSzPfg1PTQIx6Z9nM8WfB7q6eaDC8gaYjrFyurh21Ru8u54JbVsctQRzy3vv_TIIlUpj2WW0GgafLeA6Di3Ztemv6CiqiTUTznE9fvvA3YtIqrW4BI0kq1xxVKl55SmPBIfh9v5pp4eODDkkZMs2gpnYO-OS2OB2S8DsUqSClJyAv9yZQ8-cawFc8Uf_4OTqxxTFZJ-5dr2Y6d-RAjjQP8bzHRfFd4keuiXCUVq2aHUdXG7d8ssf5bMpVHx_IvY6cV0hmMrcjaVCUKFxZi9K_n0R-2_kSkgqn0SFEKR7vqHeLcZONKwCjX_c28G5XWRr2jU4cmCILklgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
