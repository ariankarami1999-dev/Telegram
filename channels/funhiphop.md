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
<img src="https://cdn4.telesco.pe/file/uuBqIuCxj1taWsOKRqAlOXySBDTZSHa5asfVSOb1MZvYJmFIIF6TMIcQ3VhTCT7K820JdqFDX357GBPj-LFoMJVUzJWADmpelEiQiQsXYqzc_gMDghfD2W5hLrHWJeW7LRLm1mFyASELXafxfL_QazeWxyZTqGUo6FXlFJNd4edd2AVJBS8F9gLzhIYfhyrzLaK1R8v9GtNmaXKK6axZsk21uzr9JSg2yXjijhApTgdJOMpeUscxw_oMI41N9YsYJ8GE1ePQ89x1VUqusD-IiDiv9aOW25AfF4iAyYTnq0oxWMUo1ILyk9XulKzObgXnjerJmYzDSjBf2P60QnrYmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 169K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 08:18:16</div>
<hr>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الان وضعیت جوری شده فنای مسی دارن از پرتغال تعریف میکنن فنای رونالدو از آرژانتین
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/funhiphop/78268" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/78267" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گل دوم برای آمریکا
پوچتینو تیم خوبی ساخته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/78266" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ دوباره مصاحبه کسشر کرده که به خاطر اعصاب ممبر های عزیز ترجیح میدم پوشش ندم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/78265" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کشور جنایتکار آمریکا گل اول رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78264" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بازی استرالیا و رقیبش هم داره شروع میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78263" target="_blank">📅 22:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78262">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw0wUlfXKOk7jMHp3peWLhZP1Qh1JJ4LrUfiPmNymeEEwvh8Oc4nmV3ggGiMrWxCpqINKErWhuFLbocRyePSbwpNMlOea8iWdDONWwp2H4N2xSAkudHNvnRXZAkpc4bycRIgXbYCYcuhw5SLUsaVp-C5aWkEldDDtYTXZSTrtR0mdY9iRcaRAa736q0kUgKZ9LHzRGb_Yug5rAzFnxpvzKiHacj-d7XcN6NsXsVILnC1_0loX0rqV87xpy87FzUwaQIFLls-Cpmp9-49JBE9g-YEQdOTjMBciwDyq1tgZXW7Dklp1oRxwekLJRECf82WSlpM85mVkNwDvYFpJbntnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین رونالدوی موجود در جام جهانی 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78262" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oidmaOkvlye9kLxiXFnPOIPekaEaDj8pOAbiUZdJoPocVJdd40rLzSJ4FaNvSpDwQ5yJfv0Zys2exD_U0LgIzNcx4McfCulnV1auVIkBNaki8XuH8K8eJp9BPMkoOae1_EDz3O7vW8onLyyN0ZykMEwqAxNVJ6YCZeJGO-FHGbZNSx3Ntbs0fodtM4ceUsI71kfMJ6UChoKiabWJ3uFWsfOvFdbuBdSGeS46Ktp3lnmpExqodw_4oyyYJaURA0xIe8qe2vS5Tk1pZNtRQCcfz5ifva5hiHhcC92nC-qVgxKaq0wTeLEsddb9tQaAf5qNUM7_QLfEULTJ5cBgCIOcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید کون میداد تا بهش 10 بدید؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78261" target="_blank">📅 20:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فنای رونالدو به پیج کل بازیکنا تیم ملی پرتغال حمله کردن دارن فحش میدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78260" target="_blank">📅 20:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Offc9nsst3g5qbCEokUWAW0ETT0YgruT3k2eYp8oxpSik3p2k_rpxz4hAEOXD_3ooysol2GEX-m181QxWx0aKGv3Xdd26N8ZrU7tZ5la-iNt-WUj-awZ4tXTJzi056OI3GBlHtDMDLhhBbRtqKw5J0gWlRt7j0JdTBpXkHsh1JWgQTnI52ymFJAWDacf0RU8eshNDH0h__0k_plrQNDKDBSr-5N6_vhY6FowMXEi5y8Z--NrwZf8pikl8T7vPjMYioOQCF751c2NXFPTWHP8I7PqNhsoiPT_hLSxb0lbqM_VqLG-8-Y7qnD6YcYnJIrSFXyWt2N6KvgMoI7cCG9vuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید شایع به نام بلاتکلیفی منتشر شد.
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78259" target="_blank">📅 19:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شایع ترک داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78258" target="_blank">📅 19:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTQARp8KE_y7dbdJkNq01OQqMly6NYsXgyI7WG4OBhJYODqn18n7P3Kn_neLskwJmKz0DcU5X0Xn7Ly3R3sOuVjVpTbwZ5QFc9aSUXMRqgT77EYPnZa8d-_CBYyNpqwNatmvkmsCBer11DnErKPw-yDkifXbSVXOxt-umVauICW-MFH-2ZyyhVae6uEVfWOxcs0QNkS4NK5kaFJgcOUcg9K4Kw2YOKczwaYyOyenHC4YhBCuDKzKXfqL-whF9xaka3Nvoyp4lT-DpWP9i-pw7oolCz_6HVjaAM1meo1n9WKASkChHmm4HsUuKlHqXEViFiTpq7uyYf9xSNzJngYJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنیف عمران‌زاده: یه شب تو باغ با برادر خانمم مست کردیم تصمیم گرفتم از فوتبال خداحافظی کنم، به خانومم گفتم یه پیام تو پیجم منتشر کنه که من خداحافظی کردم از فوتبال، فردا صبح بیدار شدم از تصمیمی که گرفتم پشیمون شدم ولی رفتم تو گوشی یهو دیدم همه واسم پیام گذاشتن داداش تو ادامه مسیر زندگیت موفق باشی، منم دیگه مجبور شدم از فوتبال خداحافظی کنم با اینکه دلم نمیخواست این کار رو کنم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78256" target="_blank">📅 18:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9eBzYif42E4kp34bwXPpcKL_EeeKj0miAi0pYSg2EpaQP-okfzQJBSXqz0c9TNuALjvIRYJue1tqstBvYsjPunfbODKuITNIlePhSlLZ6cdYmiEWeCzfLyb9BoTO_cRpsfhnHzxOUuH7QI2wSKGs5fLydRrSnLux2DZyQJXnf4KEOJE9mOzSSnXrKyZnxE7wltnE88Z8G4gkqZu0opZM69A76hkM0Dc8nVFGk498V3csIbsAx2NIyo5epee5d0aNdl5jV6Hy2C6wOOMGeez6Hnti6sYrbLYe2aPnLwiKZ9q50HvOS4cNETkEzkA3PVPtMNjFiQOWRs0-pultdYU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78255" target="_blank">📅 17:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78254">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9pFfjXai5SMJo61nJBQEu3eXAoW3cthNBWqAiZOAZMfm1qZQI0_xujh0cC0klNb0GWs5wJdGd237z4rcBcJB5HyVgvqJXD3X19DgTDFa2EELz76q0baDYuRjKDitJ0WLcP5bmfcuaU5VOpwHoFBSTynXVu53rnPk3w4jcpe1XitnXRfLyIE9nDv1iTyVNWey7o4yYJa0tToGTAI29irHHUVM5RSpWbt9Zu7OBRqm70iHz6IO_YcwfWkGkZDm0V9S8QeerMKjMuHDeBxJE3ViTeODnJ0Ah1ODESFVEifG6-GHspJa1WgJ6NzLb9yDA4C0DSpLZV-sK3rihW6Wt6nMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78254" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78253">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جام جهانی ۲۰۲۶ با بری بت شیرینه
🔥</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78253" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78252">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎁
🌳
جام جهانی با سوپرایزهای بری بت
🌳
🎁
⭐️
تورنمنت 1،000،000،000 تومانی
⭐️
✨
شارژ اضافه
0️⃣
1️⃣
🔣
برای واریز کریپتویی
💰
🏆
5️⃣
🔣
کش بک روزانه ورزشی
🏆
📱
همین حالا در بری بت ثبت نام کنید تا بهترین‌ها را تجربه کنید
✅
G29
🅰
🔴
ورود به سایت
👇
🔴
https://gfyweuuchsa.shop/fa/affiliates/?btag=914641_l303106
☑️
کانال رسمی ما در تلگرام
👇
☑️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78252" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78251">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZR1PO7G2rta2Jgy6ytfRGkEaoVBXdKO3izzhS1gRZY6QXy123Rg7K6KZTzbnrplPMc3UIswIX6heg1_-pkAx9gfB1LiIc-hjacK8DlFVsuWwNeq0H_gnFZz4MzfJotgbMtKyY-bsiY9mRJO3sjjI_M2Ka5GEUYWIrjEBpBFiIvFjArU8EclHtCoO9XSv97mQBlhEu-zng8bhfzhBoZ8zkA0te5Waf_Ex2mbUQk5r8Xh_A1UpjmNbY3SnIRIvJK0nP44BcpP6WUO9KZDikHeR2hy7OHlhP7LYW3OegOO886QYYq7mDQsZgcoWu6uw82l7pHFq6pGZstU5CqExfeywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژوتا یالا از قبر بیا بیرون پاس بده دیگه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78251" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnO3i1rXeM1pbj9aocaTYwqe47gBYrE79kheNhSW4nUcuBoVa3SgHWBeSIkkrEqdlVORRjeQULWH1JOYXf52VLYEt-3pW7gVAowt3HgwKPtv_dwnIc3XxD_Uwp1k9GiXZbqJXkqmBCEiAJSjEjVBTLMZnVa1D0ypLKoZ0KTHkTAdbQlDvFfveGgWDquWytsfZF72V9f_VyAex4Fx1IiBjW4WE6THTautqMbSaP8XnG9OhPhHHVEszGrRaUs7U24vo0z8qj_bFJ6y89gOAvWabXgRLlMw-eRDNkNBfOBp6qM7Ukt_IYuFDCw1DZIEPK3pIN5h9utlKN0OWeoj0oMh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78250" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfvfNjp3TTV64OB_EjswTRdHy3mNsR2iOOTSn2sYWD5DqKP8SBj2zztAwQDA643DfSBt1WaBVrvG23XEQzdcHnl-rwxqUZ3cQPqVptemweYpKcg_hWf5nBS0KHWKW_5VS5Uv-UAweD9wWUGBKwPTYyVDVvQrGCLFNtK1CK4X4NvwqdeGiobpCqHxXc_BmcMBUbM9h2FZOcFCdk2G7njs6CMwCnzYJ7rTzOf2m6CdMLPomhwYVtlqbDjj0TJAsGVwjJTtAWHIAUDaavloErBF1iMbWMgfsTHceNPHwJuDiscCTh199wK-buoEx-SqmBB3IcjclE-lEcB2K5Hsic25og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در واکنش به لغو دیدار فردا و کنسل شدن مذاکرات:
«ما از روی استیصال به دنبال دیدار نبودیم؛ این ایران بود که چنین درخواستی داشت. آن‌ها تمام شده‌اند!
ما همان مهلت ۶۰ روزه را تا آخر اجرا می‌کنیم.
هیچ پولی هم دریافت نمی‌کنند؛ حتی یک سنت!»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78248" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUREKsdi9BTa20ZGwQ5WNzqX3QETw7QNce9s3u_cNNDS59i5BfZ7Ek4ZUQKLSuubiME9b6lZgU-sbHeIsTG4FR0MSdttEm32XJTVOpZg4mIA40M2jQiFEVEDOKiL4gf83y08zMwI95Q5k9N-QdNGFh7IgmKRjL0VMPOulb6DKt_ETh6dVf-AVkOAYZv3GcyE6akZvjG1wcN7bz48LMsnLzWB0EeN3OXwNfyFV3LFCSRHiLPf6GX8S0Pf0LMK-155Qmxk3QqrHv-0PYZ8p6FmGIIR-BU_TG-MK_l3cN7HHiLCgtE1eOkdYW8YZ1Oe4i5YFo2rjUbZbquRNbBmhdeq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید بهزاد لیتو به نام "Late night drive" منتشر شد
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78247" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78246" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ میاد خایه مالی میکنه و میگه اسرائیل باید حملاتش به لبنان رو متوقف کنه وگرنه باهاشون برخورد میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78245" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سپاه باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78244" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78243">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">معاون راهبردی پزشکیان: تجمعات شبانه باید جمع شود. آنها سلامت روانی جامعه را بر هم می‌زنند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78243" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مادر اشکان لئو رو گاییدن الان تو کماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78242" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kABgFYkt7yQ0mUnUn83awhITkBfu423t9waadZxRK_8GDAorcW6SsK2i7GPcSk-2o_g6EMoXoU0TwDADjf08fFD-8_u5AnxR_fpvWWCY5VaeWz5_wfV18XExTLEMWhIrfSQqgD051Eh16Bphi1I1_nIz6umG9wzNvtrTH_uwh0DKuTxun1iji6K65nkgCYtx6N6NWzNZvFLH1pF_VkgG7-m8nfKPN8L63WTPqmqZLDVW3Ek9BXEXaXg9pZ8Ocdcfbgp3QrtjbJMFUzrPFbQWHsXSR38hLtxDuzonoHJxEGx-0kDcVzdDV8a4VWOBBUx2K_ri05cuPGa1GgHPM_UtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم ترین دغدغه این روزام اینه که بدونم این یارو پایین تنه چی میپوشه میاد جلو دوربین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78241" target="_blank">📅 12:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جنوب لبنان چرا منهدم نمیشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78240" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aafpymu7aH80vK-d5fs_l8FShvT7NcoSJO5fiDdGZv2_0ORygrbCnImOrO1kpAXuABL7UlOmW1GuVD9ybyCO4oJ0h3_GnHDFXyWXitsPFEpA2QuMeYiWm9wxzZySsNh26Bx05oAW4w82QYpZrcgo-kH1zJgoRlkAwgkXUvb-AmO4M8GA844w207TbZUmJLCq9VvGtzXboCKWsGPmQVb_0o6o9ZN3h_EWgm35Qg10ih4Hpecik3mNcRNayuzWMoOr1Gz2mS14uUODBOqfNFihpwGp119mrGTz9kBRB_BX-fxMA_WTXnrhBFVDc_-EUEq4dnt0TqizSJQod1KNjH-H_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبلنا که ترک پوریو میذاشتم آرشیو تو کمتر از ۲۴ ساعت بالای ۲۰۰۰ تا فوروارد میشد، امارش تقریبا یک سوم شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78239" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDqhtsZBF4415tKZM_aWkmeCjFPf8BqicEvbMYbZtveiMYUGEz64W9I5GzEsWAai_hVfI1XGSUqCH1-0E_wq3j5J05fmTVZ7AQMRcPI5-dqt9pn6qh3pAAFOUn_oDrR4R0jJ0YmiqV_h9LDbelgQM9I70KmHPYg_2H5YUMsfBw_615ewA-452s84MRU6QfjF_LKwHu2S8Ccb_3KpAykhr1HTb6TzjxE4s04wO4Ad1gFsnccyloK2YmrnlftJ89SUnQWtb3os8swu7NKVGF6PhIaGFJxExYu6Ip4ebLwKTfYLD_K950bAzr1CRhCxqommimnHrgf80-T29SrtXjM3UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای مادرجنده
💔
آقای مادرجنده چقد فید شدی آقای مادرجنده
💔
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78238" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78237" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78237" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2x87FCRuDjwVnRa7xuoCKynmcV4YPhX0a_AHA10jl5-avjeO8cv2ZfhP6ezCv_KcYt_RXV3kQmN_7CgS3Bwp4e8ontd1VbnwxDaEl969W3986juq8kHe3K-dZ7A4lw4qNCVb_touEZXXwpyEWBvKsseT5cLLw1TiZCSbEdK_rELJBqpqj4PIWDt6UYLbkd4nKHAE-3CGlToW2gyq8AK49TrGopmYzQh9Rid5ULWbPBepbZYH9qqUcj73FJcxmvW-eBF87mQVYoo06DqURyzvfgiATxKIQIj1PKJDRYQX3sv7QI5P6lzXnsx5VSA_tI_5Jm0L3Kr02yWxNo_3hBvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r29
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78236" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سوییس کنسل شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78235" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ولی سکانس به درک واصل شدن حرمله >>>>
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78234" target="_blank">📅 02:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان کسی از ساعت دقیق پخش مختارنامه خبر داره؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78233" target="_blank">📅 02:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78230" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اون سازمان دریانوردی که اسمش یادم نیس: تنگه هرمز گشاد شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78229" target="_blank">📅 23:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تروخدا وضعیتو المیادین: هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78228" target="_blank">📅 23:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تروخدا وضعیتو
المیادین:
هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78227" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78226">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شجاع خلیلزاده به عنوان مادرکسه ترین موجود هفته اول جام جهانی انتخاب شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78226" target="_blank">📅 23:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXqYYemqj2gdsXWxUn1ipnUd7KFugbExoFonduWV6WbcCixN-1c8tPWaby3qBTqD1aaKmpi7eeYE6-DKZeaJxtMctgxVkE2Qtl6CyqW4J5ekJ5ksjT86-TTbCEFPU2-sQYLE0-P32ENySi9YZwX3zGhnfHXc2tfOSfO28mTJjygCfcrNIH0iXsdrqZUW-OQSWVPnYkz3HCHpSol2dOm88fA_KAo8tJX64Cj1JYuwrB2KE1PVRMFmUVxuWknsEq1esEgbZGajftgqFouJw6FU3ObBa5ghECJYtJIHXswLrJQATy6Mic1hF9Zrhscxt9u-jXCf0uFv7axmiWv8Sbx_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام چه داره پیشرفت میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78225" target="_blank">📅 23:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78224" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78223">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWeera news | ویرا نیوز</strong></div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78223" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0LXKSqQYLNjHbbusjdz0LGQvViUd-cWGFNhckjb0k5ENjp38awKb0Ss1kSi_8m8HEoQ2PdvXNN0w4UzWBnCR9GYFiso1tYlcqmSfZ5cusTK5mJCoYmdUmx4wAqiE1ZBBksML1m-pyHAgRhsp-f6nnZY-skVUJN4c-WBSPSXjVlsRBpEQT7lPqr2xUqrBcCxIjjW5k2viTQmhcXVLrUaxBb0grSH3wJSf5Kbf8xGlwG9caht4diFZtOs8PTpEHxm83dszk4_4bxCn1G_5vkzDctCUAY1ucrD-NH-JYXiIpnBPkag5mmzz0CGcdcyZNIRUh_apikM3qxv5Z8ZnLqRMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون ۱۰ نسل قبل یارو نسل کشی کردن یعنی این دختره خوشگل نیست؟ خار منطق
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78222" target="_blank">📅 22:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78221">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خب حل شد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78221" target="_blank">📅 21:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78220">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شما جنبه افغانستان ندارید، بزار یچی دیگه بزارم</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78220" target="_blank">📅 21:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پوری کیرم دهنت کاش خایمال نبودی</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78219" target="_blank">📅 21:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تنها کسی که میتونه برینه وسط مذاکرات تندرو های داخلی ایرانن، تحلیلای مرادویسی من‌باب نتانیاهو همه کاره اس رو جدی نگیرید، نتانیاهو خیلی وقته قدرتش تو لابی کردن در آمریکا از دست داده و توهم اینکه آمریکا سگِ اسرائیله هم از تفکرات رائفی پور طوره
ونس امشب یه حرف حقی زد، نتانیاهو بدون ترامپ و آمریکا(عملا یعنی بدون جمهوری خواه ها) هیچه.
تا فردا صبحم لبنانو بزنن هیچ آتش بسی نقض نمیشه، ولی تندرو ها تنها کسایی هستن که میتونن کیر کنن تو توافق بین ایران و آمریکا
اینکه مجتبی خامنه ای امشب همه چیو ریخت رو پزشکیان اگه نتونن جو رو کنترل کنن میتونه استارت یه درگیری داخلی بین موافقان و مخالفان مذاکره باشه
تنکس فور یور اتنشن تو دیس متر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78218" target="_blank">📅 21:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78217" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862002bab.mp4?token=DRtWhtW9fKROwlCtwaw4ziGxAutfF-Hz7bbfrQmSOIBkl1VaNtCt8esVloim2aFOmkD_OQojy_QMByZau0F-ZUU5vpSR7mJK8nt5PGoaBiSdyGDBXffIBx0m7MaIzS5w4kEjclWevBDcqPN50Dy8x60p3oK3DZaglCRbw1MqrH4NNQ63wvw-o6Mqka9elEQmCmb5HAMN-8v_6Nnzn1ZKvDIW8gpiQVFZPNXb9L7Fg1j1N5_ivRqJCOnQbmIVGqvG1qt0F9RGTJflc4gMLQMA3CnYQggOZQD06xGOto6pUyVT3yATLNqF8p4ARjKBDIE0Zes0-mr4zQvWonGhq7xSJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862002bab.mp4?token=DRtWhtW9fKROwlCtwaw4ziGxAutfF-Hz7bbfrQmSOIBkl1VaNtCt8esVloim2aFOmkD_OQojy_QMByZau0F-ZUU5vpSR7mJK8nt5PGoaBiSdyGDBXffIBx0m7MaIzS5w4kEjclWevBDcqPN50Dy8x60p3oK3DZaglCRbw1MqrH4NNQ63wvw-o6Mqka9elEQmCmb5HAMN-8v_6Nnzn1ZKvDIW8gpiQVFZPNXb9L7Fg1j1N5_ivRqJCOnQbmIVGqvG1qt0F9RGTJflc4gMLQMA3CnYQggOZQD06xGOto6pUyVT3yATLNqF8p4ARjKBDIE0Zes0-mr4zQvWonGhq7xSJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه داروین درمورد تکامل انسان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78216" target="_blank">📅 20:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">محاصره دریایی تموم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78215" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78214" target="_blank">📅 20:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78213">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-psa2R6sZTpK91_6EOjQkVmdvdGjNUv7nUObPmSVByADCcJDqvqmv0j0jZ7m093op_RthkIzNa81JmqqLZfs-FcDrFKq473k7TaRAypsB22DDBkxh-6oBe6hIDAxN1zRlJy_bBrUh9GYZFNoLR2xJfC7wrIz8Y221z5viVLa0U7Af38rgg33g4n-99Y4m-ZTlrSisuw1pAjBmCjsnxDs6piibaagfGY3v-YjDkJcAyuse6uiqSyiHRoeBarH2Y2kGJKO3oNiBARo-3PZwkN4YGWNOiWwocYAHTjc2AGjCGpgrB3fT_7OesmA9-dhJ61dL4wo4gq9gLYwCJ0nHGo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتو جدید ممد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78213" target="_blank">📅 19:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78212">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKx_jfSJOWIPkd6xkCBNWCOUFnIMfkup7L1mCNbkDs87PWwWq4Fjdg4VVfgyOXJ0Ql5VSKPb8IFJXbhE5_XQ6dQ9V95XdNPt0ojEOJ64lmXdvLDBP9QMrRuByo1QQVnCIFIPvx3RU9cTQLD3G-12P8TLsFXWY4m6xFUWXURVLeO_bHM4SoXhKsv6pTUOKZs_l2QaBTlbL-JHry7tG19vX-GSMPY4gbu9yycYceOzVooZKOiunD4LVtjxiF3bd4rozcbv3jGcGK721ZfGqCwEaCXRpuzRz6YhTS7SgTU9ag9qtk-xD8_npOJs42FchgHPFffaVhCIUpDd_i82_Ho8Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری عماد قویدل برای پوری
@FunHipHop
| Behi</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78212" target="_blank">📅 19:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-TcJW24Fk7L39spRsp1MnQh3GsDTqt5WCm3rcxQcq3TI7P9fu9sZTGXw3VaAdM6QYKoDEK_Uc_3DxvkaJH4QnwQKRz-aO1L2wyDiQcv1NoabaH9L1-DsU0F8jQkvzzQOZQpxmyjwWqTWQU5ETlvFJmpByUVMAzZiPuynZFG_5e26LgEtZA56wJFSykBKL11snEgag_B2eb0UpT0hZMwOmfyrUQUw2asUVpnLzwLqss99c06pwroKTuVN6-0DTohqWj60SPHL_yk4MLKZJF73PdLnZxp8fpTfAbaIH_8EjIm26gG6LNJJl1oNZYuiwyO8WesENAcsS5Ogyi2DDfm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 کامیون ایموجی خنده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78211" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78210" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78209">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_D6TdNGUpLOVS8be2e0RkMSUTmKXevkFav2s78nYO6gYg8_rq1PQ143WzzKq-m_V9vh-OJsRxKbuFx3TSctRlFiIMxg35WT2LE7TnSo2D-YSEMGiqShNzMo_veeDvDNfOLxny83o1XKPE9sF6dd6pzuPmmlCJaOm5jq7Xd2VlsLcJ38ymelNcgdwMPB2_o4TeIP3bdBTuRiRebPtl7x1ACzX6WxWkj4VvepMS3K8hqd9KxNsHY6ksI6c45QLAu1LzLNS9T2GIz_1TUvOwNmf5-OUKk42vhNs1EeWfrrJ7QBjF1VP_7l-dcSzRqQWP5AUgqy0g-RbVvA0yvC7szTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78209" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taJxwpBmf6BZIbO5hu3V_zELvvlWZYtysBG4Begv9vPMueLb3TFT1wSh3v7V5b8V8xiHf3hfPdapZ2uFjOdnfOPZKbRFhsFbJXeskOEjGGIJZlNzphn-zq_UVxVlvIN5kFwC1p7xY8w3a4qdWJ9RaM68kJ5u_mNPf3GXugSi7jayoWkvi-HrVTU6uxQH60UF-YI6p-biaNYKpdnxpZ063GakDDrRzd5oMeBX_kqG1EBrB0X5vdeG-vB2DEzc3ab1qyXJA2K7Jo_SqhYdPtnt3l_SaEQEBnzjOnf1dzMihKQsihoV6ihQI50_3R5KAgdQ6gSrL-QG1hbD0aeJaVCvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ساله ترجیح دادم پول سیگار
بشه غذا واسه حیوونای تو خیابون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78208" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78207" target="_blank">📅 18:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTqG_jEByNeERIzObdN8U1isJ2Q9hwk_QlBpZcgtMMSPiHNBpWrC52YqYKCRubeGDpypneFF1r_ZP8KHrbtztVAtDaeF0SzsGw_Aod43Dfva6Dig0sA0YU6cM6Qg8GlHQQFEoU-zYjMFx4WIPmO50Pddu6z-XXuKjPHs-d8oxeG8YElfS6jnP-KzinOiS83ZkWagBnWmitinAc8RTDSYw0qsGxW4i0sPTYeE1uPq3KYm-3FGWE-u3RvcvoO6XrncT52O6-gWeqmNSR1WI5uOntG_Nd1tDfcB-GYAZRtnnUTuc09cbi2vNr9blk4gKn5VS-Z6r7Mn-fNF-pbFTtTwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب جام‌جهانی
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78206" target="_blank">📅 18:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78205">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLk</strong></div>
<div class="tg-text">بچه بودم دوست داشتم مثل رونالدو بازی کنم،
الان رونالدو مثل من بازی می‌کنه</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78205" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78204">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noTKwkeN7XVLY3CY9W3I7yScfeg82F7smjGofZgYe-atMq_pUkP5yzTd1lolbhk6R2qY-HZSabTJaYbmgTsdDO-x1INi-J94ibQJHG6tfG-SvB-VWFFdc3UJ3ec06itw29uGlFEFspB-YVokPO4rhEoCJSweol1vz6j7bjeguuogjXRBXIFmv8vzWgDrsWxNQDrV2NJu7yb0vz2Nd6-1uwn_Oyuxsk_T8vXT86KIUWFDyXtnHeu_RF2sOLW9G79cBZpCGulr-lgD1nl3478aPZSPk1smtKW6I4z1eqza3BpZpKvpM6fFiI0N8WEQkfiHSyQls3uag5DF1wDjAGoqNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای تاپ دنیا توی اولین بازیشون درخشیدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78203" target="_blank">📅 17:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikf5HG_W4mBVKqi9oeTynqgSILQlXJk739dym5LfI6YC0p8tT-uRBhkTyGDJg6nwKNa5aMkSrKjs7RLPvjI0xqKVrITb1eckCXGU54ACTgHCrr5kSacNvjHxyQ70on4jNzP8i3bxFur6g7IXVMQnzq6B-RZJhXPx80KV2KIXiTETOZ10xS6wWCgJtAxCcJK7Ld3L_acZBZp2IB_WgwX2WceBCJECVUlAXTh5Roh7cfhQJgmi4M4zzDtREZ0bN_r5ZtUjeEC5nV_0qK7GoDfvHf3d816BrMZi9x-GkLGhuSVuapznE78AMIkFi2vSAOKimyiDW0bMHp_Q1_RIlx2GVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g28
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78202" target="_blank">📅 17:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78201" target="_blank">📅 17:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB53MfCLdkSwcqQJ_PlygK6YKBmWATRMKA6dxJhyjFdTRTHtcs_mMZHnove2IDimMlTnGFVl4pMIqha4hgc0HMPaqfeWnJ9YcBbXF04kYkRWFhGRCixUnpV_hXHnnzLtw58ldCX7dY-fcKmBxAiLdq22gb9zaVkiBsKCcxJ1VsSyKYkv62AqOeubPeO_hUzCMvUmmBgachGl-m6Vc06g7q9dHq3WLXWWBnfUnJe_3qEcVZ3EfhLjrP4iibDmqIUGrptts1FSodOvSv0IqX72VCmmU5BGNijPx7Ltc7vT6WkoCZVhWEaIzBI4HwpPXJQsOEtCZZ2AV8G9xg8ESF63YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم سرپا ریلیز شد   YouTube  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPhBBqn8h2yCSB4OWHxcZqGFP3UUa8MuSeuuV06FEYcacU7vhNHTNvAqQa-WiwDK5xj5UySuDZdYd2YY_LTqaNuFDzZb-5Ps0d64Q5vgb-vz6v20878IwRYl8BxkA4SHrcGNWaelxRYkCY698r0sHLGbspmLpfw3xi1__GkO3Q0TcCPW6cNLKyJKaZsIOGz61KPzOLloMoa1_R0f8qYd2FRcnuMTOntRhcFy2WksiKgImztbw0e1XquV9ofObWOS6nmGPXyzKHBAAKiE4LMTvl0SREibFAI1NV8ilTRb-gitukwWSMJp6aQdYoBQvopSj8heeiEDKcXc8fgeqcD94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم
سرپا
ریلیز شد
YouTube
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78199" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78198">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وقتی مردم ایران صدای بمب‌ها را نمی‌شنوند، ناراحت می‌شوند؛ آن‌ها می‌خواهند همچنان صدای بمب‌ها را بشنوند. چون آن‌ها می‌خواهند آزاد شوند.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78198" target="_blank">📅 17:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ: فقط مردمان دیوانه میگویند کشورم را بمباران کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78197" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWkxv-i5Lhd7ro8dy1zk1azFCGwxSMGFatrpEdnWaatuAwGwAOANkKJYH-wV4Per5Cmti5QzIErXOsdu6ej9gNCCSNVWnh0mbHwJapTClH5_2Yoz-BkIl453uWiBr_y4A7EtODg4Kq-xWkeuRKclvZZtKpwA9kVExMAWCWtto0D87R73ixgslQ8IW7GTjXWUZgc7o5yURC6rRFF88Pr42nGYBA2DCfIJeOEr7qejoBu745zLK-SIegbgdNyKpUIV3EgjI71XiVY2LpFCEo3-dhD_SgTJKpomB23gt0bcdfNR2Ucfji_G8fTlq2bjO8JsPmWV4Al96IOuY5bvTtIMzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78196" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqBvpu-00NC4y5W1HksbazrGYM2EMBJyCQieRjKNXIgFrP0eenErsh060oX_PzgHxCWmf-UmLPmYLBRTLIrhyyNIxw_5MHVeurhzAdCNOLl1XOFyo8ZM7il--lKyyuxRT7b9ZG6MWNALHV5HEg6pFImgzEWB0vNUI8dPbWX7DP4_DHgLzcNx9EhdmcMljv_38wUAJetKVg0S8fKmfMvplTCthaEgwPRyvBU_rF7neY9VwrxWDKqKjtCtPSoioHu8HZCEmZlbLYl8uey4t5G-SDx51ftB8NxZR6YRf2lawDK3ZGsiBBTeS0aHilexpyBVeW4COgB7Js4g73qmwRcvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سنت خجالت بکش کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78195" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78194">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پوری میخوام برم بیرون، سریع تر ترکو ریلیز کن یکم بخندم برم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78194" target="_blank">📅 15:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromuıǝssoɥ pɐɯɯɐɥoW</strong></div>
<div class="tg-text">مهدی واقعا افغانیه؟ آگه آره که کیرم دهن صاحب کانال که یه سگ افغان و ادمین کرده</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78193" target="_blank">📅 15:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ef661660.mp4?token=e40XjydJrq1a4_BbfobtDsm-R_ssGKW-WuYybHzZlSRlqL31S6m8a_sVOt4LUD6BNbohePdo833BpbSN5sdY7DC6IxhxWE_f8XIdI78MyW3sly20K-jwTh5VU6X4h5QjpfiY41WMx1JHy8ru_7xqXavseQisjQ0K6wSnvip1tFkahuyofSTjqD_T_H6qfAujfINSOjhZluZNazsKfvdPcuG2T2nJ0HPu4DdcxQT_ynjq-vc0u7OgmZM1bgQ0Se2GHKuBkVQ7Ptk23HWCIYz8fTyFcqSpuFyfS3V1TSgkdO3ScR-Elchm1vjRyAnIYH_YvlAOJrrVA3blaCSFaO2PVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ef661660.mp4?token=e40XjydJrq1a4_BbfobtDsm-R_ssGKW-WuYybHzZlSRlqL31S6m8a_sVOt4LUD6BNbohePdo833BpbSN5sdY7DC6IxhxWE_f8XIdI78MyW3sly20K-jwTh5VU6X4h5QjpfiY41WMx1JHy8ru_7xqXavseQisjQ0K6wSnvip1tFkahuyofSTjqD_T_H6qfAujfINSOjhZluZNazsKfvdPcuG2T2nJ0HPu4DdcxQT_ynjq-vc0u7OgmZM1bgQ0Se2GHKuBkVQ7Ptk23HWCIYz8fTyFcqSpuFyfS3V1TSgkdO3ScR-Elchm1vjRyAnIYH_YvlAOJrrVA3blaCSFaO2PVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچ یک کانادا و حومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78192" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">راستی محرمه، پرچم عوض شد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78191" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انقد همه پرچم گذاشتن جلو اسمشون منم تصمیم گرفتم بزارم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78190" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-R5XCQY3dw0gnGKPWNefZAurb6_4F4jYEeGlqHaS9t3uSrw5aTjkuhFYqYW-DLWTKC0MQRHv85Go0mhoVCMbKOhcZxBihmywYJncrtL-A9v-h6L7omQCxh7289miumwMv8WVTkox3xQo22T_N8b8plTQJAW7WQsrDeHtZMp36FYDwpxxxZjRhmZj68UO-urpUXSpurOBzEGyFiNpAE1xf04DWXvG9u631-iiGKEcuNA06hkmgVPcT__14KyUN2MAB0jcd0DusHZskd9bEGHckRKnwpq0jvjFZ_xRO2I6Z8VSnLLGPtD9xZM4MQCSTdA8spcdK7tyHu-wUZI8EQ27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت اوردم براتون که توش میتونید خودتونو درحالت امضای توافق با آمریکا قرار بدید
پرامپتش:
A tight close-up mirror selfie, black and white, grainy backstage aesthetic.
Subject 1 (Foreground): A young man with messy, sweaty wavy hair. He is wearing a tight superhero suit with a web texture. His face has realistic battle-damage makeup (cuts, dirt, bruises) and he looks exhausted but calm.
Subject 2 (Right): A girl leaning her chin heavily on the man's shoulder, snuggling in very close. She is holding a small retro silver camera directly to her eye, covering half her face, smiling.
The lighting is harsh and direct (flash photography style), creating strong shadows. The background is cluttered with a hanging white t-shirt and messy towels. High noise, raw, candid snapshot.
‌
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78189" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78186">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78186" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78185">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78185" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78184">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjTVv3FIsN3tTPufAQvG5rI5CAUpeNkwiVtl1kzUdgcL-YQGfatafqQCw8GBN_vgIFZp6IKKvVBF1A9iVKCGpzlpB7WBYIQx-uEnrqykJ2_YVN4lyYfEsUNMIlUwggBplYZeypVL3dT37azftfblJHQOFz34iP94aNXm8TIA0uwU-XJI0S_SZsQer0HDXE-R4fSxuPGKndqUphNytWXoqP9i9pFICyjf3dRiMd9gq5TGFIaMWGG0T_txxPnKqMyJ3JsS4IziaeYy6EkMiFf9mK8DDXCDGMJE4_-GlM5CmAAfPWHDJaMhqyF-6XzVtQcOrtkGBMyUwYPFbiavX8Heqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78184" target="_blank">📅 13:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خب دیگه توافق هم امضا شد و مانعی برای سخنرانی مقام معظم رهبری در ملا عام وجود ندارد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78182" target="_blank">📅 13:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78181" target="_blank">📅 12:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgvAJtIttXiIuL_Pxv9xEQgGb8pnsKGdhEeu8zN3_3ZSg93accvYbSii21QyPr8hPgDUrSdZDE3Nwbm0YnTKfC4mDC5xthhD2i80uX4nMpL2FO8dvFzhA69IoEjMZzomCxYd7RN1bfLOxAnaI33SRKHIW_VVKrRb0Rw5v21k3CrCC4KTNX6f_fYnB7cMdW99-Rb14qs6m9w4GAWrBOU9NJR5eQ36he1cQgbqFYklT1aB2OcqETvcEhme-gs1E6VG0vrAF0VddoBq043TdfZR4bvHjRfJ9d3YTJSPOb8VsI_DOHK7tywmI29qc_PgZDSiX0p2kCGmrIn6POOCIDRmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78180" target="_blank">📅 12:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">عرفان چطوری میتونی انقد کصشر باشی داداش</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78179" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آرتا:‌ کصه بشینه نمیره عین جمهوری اسلامی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78178" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78177">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78177" target="_blank">📅 12:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78176" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acGGAUZ66oXSo_JD3cLvIuDUC9kmYieetzcjz1NAXClGFnN25XFr5Be3BNMll5vmtwJIxmUg0atOHbv2vsTvTK5CxxcCvqJ9OshdbDgLEd4yUKuuAVjKvLHL4FKRLDLz9ioSShWKd-XlCB0sHaa3Km22DLh_oQFgUfXk-dotbdx-LYi2C7qj-UagOhEystmoaIX3lDXxEQGzkq6Nz2hSJIIkuTTlJ0uzmyU3vnNAEwiwN75ENDrsNNc8kpdZpBWaUljfwqXqEpjfiZRFph8lQ_PjT9qlh2upKynOckfDV2NjxBJ5IS9ID7IkUq9SWROo5pHKTBojEuR1gyfTPqXNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.
Download
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78174" target="_blank">📅 12:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آرتا، ویناک، عرفان پایدار، کوروش و کچی فیت دادن</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78173" target="_blank">📅 12:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78172">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmYBd23FVPu8w28ASg1r8RLgTXabs2IErCd5cjIpg4TGgJu35hOcAkEoBUBdqDSC-J0TFPnw6vNqXq87mb9-peHxqLZ7BttfUjBfcQZGsiEvqXq50y4SFAUYb8kbuhXwv-nV9p-U2EJ_WMWtlhxN7bZ22NeTNI5HeXBtdpKcRZw-v2i5-YkTVvlhn-RTt7yXVzqhplbAJ2zaB58KqMQos0zBkHEuv6lRT1w8pQz4ye6mNEvrlJCZLIzAfVpo1qZf_RLRTC9CVvfqDCkPk-jY9urek8hcdGqMCffy4gM7EUYxqvFZSjuGqIsEHoWcsIJwyLr8OzyerIdE80Jnd366zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی بدون خایه نمیمونه، بالاخره یه جفت خایه پیدا میکنه برا مالیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78172" target="_blank">📅 12:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78171">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آیت الله سید دونالد الدین ترامپ(دالگخیز): عادلانه نیست تمام کشورها موشک داشته باشند اما ایران نداشته باشد
آنها باید بتوانند دفاع کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78171" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78170" target="_blank">📅 11:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78169">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78169" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شاهین نجفی نوستراداموس   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78168" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=QQtAcc1FTsYMeBm9S6yxDkvtVE4K3wCKHC2HLl1mFhBTHf3w2TUbF5Hh6C7fntPc-nqvVDF2JOEySR23FHa1Y-VqzU_FHQ9yKp-j-9lUfKI6tZW6ql1Nwcd6NsYmaDZVmqu-ZjAybm_6L2ca5xUiQyesegw6zaqGP-nh4AF3xciEQJ51nykXSHXEgSTJNHjUVTTR4IvoiK-FAedrg8gyxPuCzMXz_nPS6oFDX-Oj-CxuC0cNGZiLIP2YqmsCPdxWpQy2JBt38BX1zMFZ9lRQu84e-inim9HNEb3dAGu-48_4tsetslV4e3iNOT-fHaXofx8ZFQrW2x7gjb0jbpIYLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=QQtAcc1FTsYMeBm9S6yxDkvtVE4K3wCKHC2HLl1mFhBTHf3w2TUbF5Hh6C7fntPc-nqvVDF2JOEySR23FHa1Y-VqzU_FHQ9yKp-j-9lUfKI6tZW6ql1Nwcd6NsYmaDZVmqu-ZjAybm_6L2ca5xUiQyesegw6zaqGP-nh4AF3xciEQJ51nykXSHXEgSTJNHjUVTTR4IvoiK-FAedrg8gyxPuCzMXz_nPS6oFDX-Oj-CxuC0cNGZiLIP2YqmsCPdxWpQy2JBt38BX1zMFZ9lRQu84e-inim9HNEb3dAGu-48_4tsetslV4e3iNOT-fHaXofx8ZFQrW2x7gjb0jbpIYLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهین نجفی نوستراداموس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78167" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_B0ZhLuDafUXWAjANJnSc6VvZda8UCFyL5MIxBSUdEIruHVQECqUCnM_gHaRN45O2eydHQ01tyQJuae2DlxzMYtMg6-h1kjQPaeC5YcxsLWAcAy5lJt7pqNPqPYjj2JN8e2AVrvyN7oiQM6qAElTpC8TpzUsuzhGie7D9sMiO9Psk3IW0SlM-G7YB_Nc_uLpt0X2FGd1BW0ojC3KyMvdK0-HH-EUVRozsru6-6TjkWqIzI26mlDwrF2oV64i0wm9kQeoGhW2AXgcHYYC2JyHVC5t5W90eT79cOaw6SSWYA1LSY2gOkv9DtqLGcJAxDEoJRP-CVchUJ5lLthFZKnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ها درحال درخشیدن....
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78166" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78165" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERsPM64wpBuD1fUd_AXO_1pMtITEDfJ16_B2h8oeNIXMH7ed_AM8JXwMN2luy3fYuQ6OujEsp9dnSD7wjkPisazv0Q9Dz-9MoLnSywSuIRrI8YdxvCPEY6x-F2AYwUWegNjubid0-fRhFBLwr8czgTmFIwGfCxJ4NU1grJC0rbTQIMI2p8MUA7x9b6fmgwNpIqF_HO0BgWP_6DSWdsaTtnez7KZHTWnJDr6LhvVp0WLm0xFQeVaUE3MHsYQkJa3aCd-3MntFZne89_or89XbsbG7EYuaW6QPdAnT_iX4EiOn-kiH6Kd1D8_6Er2ACju0ewlAMJB_KJh0LmfSQPfQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r28
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78164" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78163">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=nzRyBWdpFEH_iaH9YJqLEygjyZgfeD1YdFso16XHoyj0BJoX9GB8Mru_XuLsuFWlsic9lByfTiQSUO3EVLwaVlsJItB79LTgrXWfGiuwlUl6pzkXw6rgZK1CQ6skf7UGnB2_u_Z3gEZiSXYSi-CL7zTaXd2OaeBT6L0utWii4Kdlsl1K5TeGTuQYIo6OglknQ0mUsJmiobF-F2fyvMLutO78EcHnDRmLAG_KUW5regVfY2DvRkC152jQmLaY_DDIJ_-IGHpkXkZIOh1_mtiCiDtES196a-3A98ccorFXLkZtVbSp3VdoDLuF0EQqRi-jDEAu9MWpXfi37x6ZzcHimQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=nzRyBWdpFEH_iaH9YJqLEygjyZgfeD1YdFso16XHoyj0BJoX9GB8Mru_XuLsuFWlsic9lByfTiQSUO3EVLwaVlsJItB79LTgrXWfGiuwlUl6pzkXw6rgZK1CQ6skf7UGnB2_u_Z3gEZiSXYSi-CL7zTaXd2OaeBT6L0utWii4Kdlsl1K5TeGTuQYIo6OglknQ0mUsJmiobF-F2fyvMLutO78EcHnDRmLAG_KUW5regVfY2DvRkC152jQmLaY_DDIJ_-IGHpkXkZIOh1_mtiCiDtES196a-3A98ccorFXLkZtVbSp3VdoDLuF0EQqRi-jDEAu9MWpXfi37x6ZzcHimQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
یک انسان خردمند در ژانویه ۲۰۲۰ گفت: «ایران هرگز در هیچ جنگی پیروز نشده، اما هرگز در هیچ مذاکره‌ای هم شکست نخورده است».
ترامپ:
این را چه کسی گفته است؟
خبرنگار:
دونالد ترامپ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78163" target="_blank">📅 08:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78162">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIQTeVQufUVACuGUnSU2y_-tizip8Mu2xE1n63EXdE4lBme8LJT168x20LnQieL8xOZWVPBlKCXBRPhpqoLjsFiHZAL0y_xN5gqieaZpyszygcwtXSMA27wGnvF_-U8SJIoX65eAtXMVqgWhYf0qzKR6Q1scl3MHn2aVSKnzpC8jrikYxmaKI9KnqG3qtWCKLkMojW5TUVKioKeP4RiHKWFLxVVZcBIZ4ZXYj7I0KI2X1WW_CqBbBZtdnjjux5y8FVa16BQ7OdnDV9NslEcNVa4HSYQT8IkM9t-8gJJ1CTLfnbnmi8uw6x5BIO-RpFaZJeNi3sTsyMGKlwxLYObrNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78162" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtZnr1tSvJrWFPQGmLmLMLYsJ2u_SGjr_2Ro65D0iYkK8e6v_G-UArMUdsdFs-D04mZJNMz7IjRHSKejgrQZvNpPj_7CEDTrC5qbSEgpO3HWx8lS4qvLLPKHK9_6UNSHLRLdhq9gfrzmFnJzmEVSr6NiA8apPUl1AZrsUTNpiDtFSNrbHKCmq9Bri0mpyxv5fU1UXvfHn06rlUgrqir0g_QwiliyaGGjvu0PZX7uZ-C5xmVWHZHWcE3EWXuvnZH2aUrMqUC0KqJkDjGp7Btq5gmjx2oQWMm0Xyp4kC4K6ad9kxvDzLeA827zLY-J3UehMZ4NbDAsvqVcZ_JA8Cs6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwR3Xyk9hYl3Y5CIeneJCdooHitWM9-asx2js7bsHTJtooQxQyBDkBx7VwoPxqmjcY_jD4gnPCm8xOv63MOibi8_7GQt1mtzf7mQGEWHCmzXU-JBVWGJ1wCJuwcoAhIkug_yWYOO98ayQoz27BJ_dv6WZAwpBntc3WpPwM0u5M_5VOfRvOAf1YK-uq8T7LU2CeEb9CpaoXHJl6X0-dMaLDdCtJ3e371Bqzd7BD1KPfIJovdJTJcZsrDjsJEumlPhFjiQnPOjqGUEBnflJlZvlZCMIyFh5yrd52-_0K0X-yfkpZ0GJ2hEmu3BiTpWPOkPVaORUjRyJlstaLH4ocoPOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78160" target="_blank">📅 06:14 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
