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
<img src="https://cdn4.telesco.pe/file/azFqCb5rhu4rajNTvdQWqWIh57YGVJnggormibUFLIVcRr5B11uSjwToZjq_8MPSlrjgy3zWXX855umU_kYlNwJnvKE84xiYsuqSDG5X0lsA1CuiXmpg32j0Yk9m0TpLPWM6tABfu5XvGO4Qp7gJLhh9DO9zKwf1ioEH7nVbrlBhTVLcnKg7dQCpiS6pF7VkXYaOwsIIVOVYjRwnnAKbQKyJoYgRWayqWiaYgVV0GFh-rprYTjLTOn3-mE2M2anDOeS0-nYvva2T_PErlwj5WhKKL14rmJcDkk1-Xn9gFRJdDpdTJJ7-IgvEpS6l7kN_afTr76B3oC3zK-_G6v5YOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 02:23:17</div>
<hr>

<div class="tg-post" id="msg-81753">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBARNR6ZWMgfTjsNH4gWQWmTFLFJ-MwVYE8PF-WaWbcXMJ9HcY_EmiGjSJGG5wgyJEtNJOAtP3mrbo-a9XL77LeZDIdb3EZlRTHjZb69_zRZSsDCXBxJx0rjHloRET6rrVKwx6Ozi6HIhGjkzf0bqGPaitFxrBe25mqU80ul2nrojWSdGMD0Tw_KF3C4OHVHoJu_XNUowSm7wnNCMsjBVlN3qbe3vSpJgEhMsYFIFbK4XSfmA2XLA2VxGRl1-fJrP9eB6G3BMXPGkdjQDgJPqhedwk695O_ddMw3LdPHjhdtU-N-akaVo-g8zY2C6kgtqAFnktwANxW5DEC_ZY1-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرا رسیدن اربعین حسینی رو به همه شیعیان دنیا تسلیت عرض میکنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/81753" target="_blank">📅 01:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81752">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ستار هاشمی کیرم تو ناموست این چه نتیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/funhiphop/81752" target="_blank">📅 00:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b8952566.mp4?token=Abb1RUZIQ-D-sc2UdaOnTqqXvDmo-H6hsr5_r4ykIpjY8A6afgm99ybWQoETlWggjJHc-i-0MLAwphiK2tfVE1fwgTXQc-A94LIq9rqLe1FNFYzqFT01HQRpj6D_g--JHxoKu5LsLMK0NVCIhfj3hPs4G4P_M0gxusR3wJIq_3R-gvCUNV4f7UOc2fhYYT34bgyWM5xEeut0L190ahHtNhrvAP0txVz33oZouQe43PK3Ob2fGV1f6E1kTLp9onfeesvwJRglQIdBimMt4IlWMpvmliDIrgW5n3tTN1OHwBmGg-Xa3Ri9RLr6RPE_wMVBERVTUNzgqtRX-Lp5hX5Pcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b8952566.mp4?token=Abb1RUZIQ-D-sc2UdaOnTqqXvDmo-H6hsr5_r4ykIpjY8A6afgm99ybWQoETlWggjJHc-i-0MLAwphiK2tfVE1fwgTXQc-A94LIq9rqLe1FNFYzqFT01HQRpj6D_g--JHxoKu5LsLMK0NVCIhfj3hPs4G4P_M0gxusR3wJIq_3R-gvCUNV4f7UOc2fhYYT34bgyWM5xEeut0L190ahHtNhrvAP0txVz33oZouQe43PK3Ob2fGV1f6E1kTLp9onfeesvwJRglQIdBimMt4IlWMpvmliDIrgW5n3tTN1OHwBmGg-Xa3Ri9RLr6RPE_wMVBERVTUNzgqtRX-Lp5hX5Pcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آره خلاصه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/funhiphop/81751" target="_blank">📅 00:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81750">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f96365f95a.mp4?token=f9IZLHUmhXkIzai9C_dzJGM8vBObiTpZY4bt49pEK98WYgIdw-ZWV63CSX1Kza3pjg-2JpLSokiC702yg35JxyYTelQDOkVcMkhUXEeKIIhpBYtZMYd22HkHOK7l0FTiJoiA9fwyK29Sv8H0JI8kdQYPQ0rjGwwMAP5md7rTGwHmVhKuuUBplpOuo6gg-RkrlFkX0MM5vcb4fYy0fCJ6AcjUSAQ4VITBRFfReVAklW3Ag134VlyAepk76lEZk236wCCzC78UZEGl8NEECXjAXaHwgYbPQd62CKpIjGOlacLaKKu2v8mfY86ijKK8i6T0Xggs5OSV_CeRkZYT3N9TBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f96365f95a.mp4?token=f9IZLHUmhXkIzai9C_dzJGM8vBObiTpZY4bt49pEK98WYgIdw-ZWV63CSX1Kza3pjg-2JpLSokiC702yg35JxyYTelQDOkVcMkhUXEeKIIhpBYtZMYd22HkHOK7l0FTiJoiA9fwyK29Sv8H0JI8kdQYPQ0rjGwwMAP5md7rTGwHmVhKuuUBplpOuo6gg-RkrlFkX0MM5vcb4fYy0fCJ6AcjUSAQ4VITBRFfReVAklW3Ag134VlyAepk76lEZk236wCCzC78UZEGl8NEECXjAXaHwgYbPQd62CKpIjGOlacLaKKu2v8mfY86ijKK8i6T0Xggs5OSV_CeRkZYT3N9TBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/81750" target="_blank">📅 23:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81749">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
الان میان میبرنم
ترامپ:
چمن مثل انسان‌هاست. آن هم زندگی دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81749" target="_blank">📅 22:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81748">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ امروز (
درحالی که دیروز گفته بود فردا با ایران مذاکره مستقیم داریم و تنگه باز می‌شه
): فردا تنگه کاملا باز می‌شه و بعدش هم در مورد هسته‌ای مذاکره می‌کنیم و همه‌چی به خوبی پیش می‌ره وگرنه خواهیم دید چگونه کیر خواهم شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81748" target="_blank">📅 22:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81747">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ درباره ایران: این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است.
(آخرین فرصت از فرصت یکی مونده به آخر قبل فرصت جدید دادن.)
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81747" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81746">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است.
(آخرین فرصت از فرصت یکی مونده به آخر قبل فرصت جدید دادن.)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81746" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81745">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSWgiRAdPjQFH1_UvntvXn4cXjXhut-gvsSMz5qxd5TkzmKWRyj2Sc4j79LY5WIcnHBC0xVlgTBO0ul78Ki78KFAlXPQT0VfEsqcaw_tcxcevFU1DfLzhT5ufluJWs5XkqQhSXdswv5Vi7Ey9xmbFpogwxZJTrhQ5Ygsk268UHD3RdyCAymbpOeZGJz_zjAGoDRwsu0fCNNalg8PeG1VNePMd_XN_jlqnEJ13S6FbsDIjuU1eOAiNYkFr5N4b1R8iskKBj_vMvpWg-Ikxq-TLUnpT6Kkh8nxeVinbtPYsIyuqFDFkapRXJxbiWyAfPEIyXBwqTwURr4YR0K11CEapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسایی که جانفدا اسم نوشتید نگاه کنید شاید بکارتون بیاد
مستند تفنگداران دریایی که با همکاری نتفلیکس و ارتش امریکا ساخته شده درمورد تمرینات
و
مانورهای
واقعی هستش.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81745" target="_blank">📅 21:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81744">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv2L5DYcD2J5HliTjB-4Q5Tx95ZDJDjl0cuD7oj1PwV59WWbKAUb6rtvsY_fSdYIaaS-g1EBULjq0TCsl7hzoUfV8gdkLlu_ODr_gU-fFFjATn0swBUWl0YqGSAwxcssu3IWDIuxcLrdRSniV__2AYCCZo8MUO-bOD22bT_W5Cp5lMmxo3tdJmKH5MhfjZ_a2TPweJZpVYtfo6Sz9LlKw0-43TmU31RwSiUOgC1qWvPkKRIajaDuLFXW_u0KnnAdXmBN7J3TfLRvmyT22LDWfcoEQB6nsFbqMZGhfga8t6hE6R2-RVmcUEtHMdBMlrZPSArxte6flZZ3KgPbB5PJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاحالا دقت کرده بودید اگه نقشه ایران رو برعکس کنید میشه صورت ترامپ؟
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81744" target="_blank">📅 21:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81743">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMflGn06pxY_4xoh3Uk9yayQhx7ii-sWQM4mw-m0GQFZn_tkp04sJ3mHmN_zHW0hm4DRQT4vFTqsHytvHVb4aZi39ifvFRkls9SVzoOph9tXVb8mBDz2hv9TTHf8cgsCVrZ7HTAy4m69vXDGCJt8mpY6iFoWrXP-0MHoI4GQx3iPLu0xi_uv7ZWJJGHLtSBketURVicFNaOkeX4yO1g8MIX3Wiukb5Voq2DxkfnEYWJxpT8dZsbjxqaDug5fesBB12zTgjSkE8e8RjWWDXSTNDp-LPK2cKrStgNZCXMdObZRKEFS_dnCQJVeiukCwf3FHJzbIwxCimDeW2U0hRSQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی جدی می‌خواید بگید هنوز هیچکدومتون تاکتیکای بسیار هوشمندانه‌ای مثل «انتشار عکس مونث بی‌حجاب کنار صندوق» و «مجهول ضرب در ۳» رو به این میانجیگرای خوش تکنیک یاد ندادید که به این زحمتا نیوفتن؟
این بود رسم رفاقت و برادری؟
💔
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81743" target="_blank">📅 21:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81742">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNBMjEbRr3UN_IivRW6mBS0GCNhUv3t7YpxHK52ram6uUP6rdPecX4rCo2b3_B1aV6OsUdzjjVWXMkAhjUyBxGmVdIoRugh76CuVU12Wxr3txkVbNmRnG9YcXYoxhkBTqW_UPRIct_oKuHtJ1D7uUwWzd40Ko6YIcmnBv1qTMIO-RebdYMEWaoGp8G6NNzBgitPovU53JloPGpmn_jdr4exHtZmhWekIglVoEXAq7d5aLhEI6Nq3PhvQuxzny4T6JImIaRjnpSq8RfT-GKl8CTz8STj2GP78iym7jUCjlZdpAkSvV1W-OWuCw__qS2zGiZw-DIRdRwPRDTPytJhRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یکی دو هفته‌ی دیگه به این شطرنج ۱۶ بعدیش و مذاکرات عمیق با توهمات و تخیلاتش ادامه بده، ارتش آمریکا تسلیم بی‌قید و شرط رو می‌پذیره و بعدش روند ۶۰ روزه مذاکرات سر فعالیت هسته‌ای آمریکا شروع میشه خدا بخواد.
#بماند_به_یادگار
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/81742" target="_blank">📅 20:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81741">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به ابر قهرمان های ترک میگن ترکمن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81741" target="_blank">📅 20:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81740">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVRrG9l6UonsV_OkXTiu1wEtuaQzUdJ72BGTmT2_FZSm9JTy4_nYhLDuxdQ9FFCKBfJur9u9uBdBnYXTIrTnTc1q1n9iNKMZ0-hxFScr1l96trB_lmlwgyJSGfAbCXC5NEo1Z-YCCJ6-Sqd5cmnyptNw1Wqvf25HD0XXvvglgELLVs3zDE7z33qtaEXHk7GFiYbUre77RP_-PKfNhJ5p4OxZVMCkbJ_n3Mw9H-H_Gv7Nzf7Fg1iCXR7zasIiVBzcICIz0WbW910FZQQRE-HRbRgNtWLjZndaP5A_KePOPFuq8V7WSwUTTPJS-1QBdalwMNr2m7qC7BJUy5jEeIOpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.2  پ‌ن: بهم اعتماد کنید و فصل چهار به بعد ادامه ندید و ولش کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81740" target="_blank">📅 18:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81738">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2wHA8OeN-PDueHYVOR47cviHQLw93OQSKXw1HOngfVC4K6PQbZN9hP7iVPdylaE7nnKmv1wCGll_pVigMrSQwCcyph0DuO-UEwRAo4dUN8P-aGvk0ijEpOtWmYyTw1f5J8y1IsW1501uZRjJmuTQgkAhpXrruTjHpGfoHW7ZiqrK40K_zxrZighHlifbNRrTUAh6APTNbGJRK-7c0cUiyb-MkTOzuByaYqmQvftPDK3TfFco6sJbhsoyIvEpV5q7Z79ZueGolyqXgDdxH4GYxQLXLCl_SQunj18q0ufj_4q8tswZsa_L2COGSYfNScwoirMku0bKPwClH_qS9YQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هری؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81738" target="_blank">📅 18:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81737">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlGJotRqsS_SGPiIm2ZD2TjKkISQvUseHK5CjbZF1d2sCJcWpHPYsQ7GJI_P4qgcRxAdpUu4LLCMXKVlRfqeuRyWdNQElvnWfwMcsUcFBj3YO-JV-OmPUwn2CQ6BA8Lrmc_O63ZTVphokC0JUw2sP1qegQyk-FfvPCal0-APrBtl4r6AtMtX_96MCRGvovT1uhsXmzyWkdEgssnXF0sgQBaYl6Jav6DBE5f7bFVZMREbWurGAg5q0kfC3qboeCfHYxBCxzjpkwsTvlpBW_MDvhLC2D0nbS7u44V5hL9FVC4tzCvR7r4t8V0hov4CP6QRGQrVEnnVHk-A9w2VpYNmjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فنای تعصبی رونالدو و مسی و رپفارس شروع کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81737" target="_blank">📅 18:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81736">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحَسَ</strong></div>
<div class="tg-text">نشور سفید نمیشه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81736" target="_blank">📅 17:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81735">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maw_Lkp_9OoooBRfbbSV7Vx3FX0PZJPqRJJJOAYQuOFgtQqATOU1uUQCo8pJU21pN27m0RiSQgGhQ5qCrqHSfQKsKKvBnbNyAqQ6-7brXooTDTgum_b08HrTAPPM5B6gTdEKmoNvJeb0N1IoIrCqjaYLnMJbAYdKXSuD8iAzewR-gqjAz2ank2rgpoA5wJ6O7Ry8D5LXNShJiMA9c80a3UvJnjiWWgRd-4YdJJ-ckaNBTlkXfKGyaNOt44yCH13qXMV86EECO8a6wQTKcqvwV1PONF2gGrGxUCQS2bKE5Z1SHjxnBDw0-3VRDcNkxnDaFYZrA0zPzHQfo4pqIeCLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوس دختر وینی داره پتشو میشوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81735" target="_blank">📅 17:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81734">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ9k-HbjGASIPpG3aGu1qLrXqk3anhmt_kpJToByk3owvs9nanMX5R2xBhCd4m0O87l_1xVKpC_C3nHAU127jztHSzgH9JdyOYsZ2rrpUJOaMHNilxEnDvj5z-hZ0bIhIw45Hwld7F15FQPrlAYxKeMyvnWN1wZZEmAVseUt1IcuJbt_SBYEKdrykqnIUM2xugTzjBYMiDbQ0ky028-i4bgwh_c-lg_4-nGmuVEXrxf9vXaXQxVfFC1Z_7s4_ZMvIMK0_oiY6cJRQomnSBA53_n9F5POegWzSDFhEegvIrigp9B5Ipil54uLNJ_ExGCrYUszfQmhcquRaQIHXZjvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا ۲۰ درصد بونوس افزایشی ماشین اسلات
🎰
در روزهای دوشنبه تا جمعه، با حداقل ۵ میلیون ریال دلار شارژ حساب کاربری در طول روز و ثبت حداقل ۲ میلیون و ۵۰۰ هزار ریال پیش‌بینی ناموفق در بازی‌های ماشین اسلات، بت‌فوروارد در هر روز با توجه به مبلغ شارژ حساب کاربری تا ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را تا سقف ۵۰ میلیون ریال به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SLT20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g12
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81734" target="_blank">📅 17:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81733">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">-خانوم جورجینا ایا وکیلم شمارو به عقد کریستیانو دربیارم؟
+عروس رفته جام جهانی دامادو بیاره.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81733" target="_blank">📅 17:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9qQJbggvJEzLCm0n76OsljePD2AGwUbUA-cMUKGXEBFc_ijxElIhYYUettpc19re5BQfcjWtoFVDVAPigSD6Lm_saq_2AmAqcl90YKV7RirtEZkeNaLSwPP0JmYZfdx-m-fTEaUKEfKDu7fJO5QRleYEx18Ysy0DZDhUP5r3L221Ut1ILic8HIYJedBLfDhf-RzqcyTDiwnlhOpS-6tFNLbycBUT4T_2Xph6np1aC7P6usvF3fScCMwaylDfNtTOnr5U6Rr4N-qSKb7lNMYnE3GLgbsyBO_LFwpWolJ-BwaBhG_Lc9OkKdHRYgpwmbcB2FcegKg7vpN79dOGnwPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش هنوز انقلاب نشده ها
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81732" target="_blank">📅 16:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خفه شید تلخون ترک داده</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81731" target="_blank">📅 16:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جواد ظریف: بسته موندن تنگه هرمز، اجماع جهانی با همراهی چین علیه ما ایجاد میکنه
پ.ن: خدا از دهنت بشنوه اینا باورشون شده قراره تنگه تبدیل به یه سلاح خطرناک تر از بمب اتم بشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81730" target="_blank">📅 15:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqPzgFd9ZZVPoZa9iDKPXhSrMCr0odhMsHr73dYyx0CoJdCwBx77k1Ms6nN1QXwVFfkmI7NwstMron7SGpAZvQCEWwxcgNuUwXPmz_XPBh266AQoHCwQ7RcHnjocHZXi-IYowUn9TKJ_pGbBy9MDJvs7z-QBZnTqvQToO6Mb-LTy-gDez92GZWTjhMRESTIZg8A8B5ILRCwLoLILZSOaAzfx_YesPOLuFjjn0PQ-xpwckWo3aT6dq8gHy8WOc0-3QxxtqxfNVSZyu1zU2iq-Gn2u2SuSEQJp9KKzEqFXSYrdTeFU7idOh2Smr_VWN9l1Vw_K7xsYqb0-HJN6qLehQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر دردناک بود و جانگداز
امیر و رهام از هم جدا شدن و گروه ماکان بند منحل شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81729" target="_blank">📅 15:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFXsyK0nyqw1uJxG85c-vrQlXmhKv9Uf8D6_7ZwP21L_bvRvSm-jaHGC_wtdMzNkpk3ugi8ut_jrL4qEUNyVjlLEk16h0VauCP7VoG9uLwVNhPVIjVC7uCXVC8RHB-9odGyrB0fJuz3oHKKASpMd6GxS9D8BuDb2_LoMRpjI0z6jCv7hcFEkZWLuiVtvVMKfnl1RsAiWbFcC5PAPze-iO5JTynQgG5Nd5Ca4o3Ukf7B4GQsazEZlyuz9a3X85DQLWK7bv6LLgZGkj-baGk6BupB4OsE7LgRF_lSZX4mmV_yJVnL8FQIgVNcrl9faXfpHdaMPktSVmUU2vnuK3Tv2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترک چندوقت اخیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81728" target="_blank">📅 15:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81727">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بستنی قسطی ندیده بودیم که اونم دیدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81727" target="_blank">📅 15:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81725">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SekZmEy9hLUk_Tz2LSo6bnry88hN66eU2qRszMtiOmXsO21K9mXyUl_SJopJdQmvCgPfWTYaBnKrc8-1Pp-G248FipUwZY4obJ83OqsFFPsrPJN8t8sPvQY-DXY8v_W0OBCppBh1sbCTbdv-r14hP3IistPYWilUw8gIONkBEdlX5JoGFfIp7Ql3hTL6uCSzANxAornPgsTSpfSIfyLviuVb0vfaR5wvHqrCtBgpTCzEgoiwoQxohJGJlcCYQL8VpcNa0lGSC-Hgo0z7kF27_BkEvLuSdjsIFPUnAcIxGUxMrfxAUZRBGDpCFYeZ35Sg-y2lXadd0P_qu5C48kcSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بستنی قسطی ندیده بودیم که اونم دیدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81725" target="_blank">📅 14:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81724">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هرچی پیج تو اینستاگرام میبینم به دستور مقام قضایی بسته شده، وقتشه برا پیشگیری علی رو دوباره ادمین کنم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81724" target="_blank">📅 14:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81723">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFy3pacGAADUFRSBpH14JJ7jVa06UCfiYv1Hd2QZEO_s6EU-ozpjvS9fd_wwmgFYMgKuZEWhSIEqBejp-pLbekd4qiB7yz1cUOOBq_YBD602lTXrsy2_YUHsFB7vJYVVmQ1ffce__5mtBdtojAOTvmGpD6zQs66VaslmKXeI955Pe2FLbfjTUWAkN-jJXtbvLaajqBwnpKZd6VLd58f_LFqu39ZPpb5pwHFiUaGIcjG3Go1M6MJ0Wp7mEVe3FUsHQMr43kwaQToY9hXN9Zn8yBKrhmAp1Rjhf4Rb6_YFsfFSS3pUaQx59SIcu1tauZq5_YrMF-DhzbEt7QFpx4z1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا، حافظ ممبر های فان هیپ هاپ باش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81723" target="_blank">📅 14:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81722">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">با این حجم از هواپیماهای باربری نظامی آمریکا که به خاورمیانه میان و می‌رن دوتا احتمال بیشتر وجود نداره:
یا دکتر عراقچی پخت و پز کرده، توافق خیلی وقته پشت پرده بسته شده و آمریکا داره تجهیزاتشو از منطقه خالی می‌کنه؛
یا اینکه دکتر عراقچی به معنای واقعی کلمه پخت و پز کرده و آمریکا داره اونقدر بمب برا مراسم بعد از مذاکرات انبار می‌کنه که قراره ازمون یه سری یاد و خاطره و چند تا کلیپ فرید کنزو تو آپارات باقی بمونه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81722" target="_blank">📅 12:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81721">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTc-Cl2S1QDOFsa-lKm6GaEXuTXxMOCxS2ri-a4E8hoHF1Eh62142M2AvXMBsLx86m36gmeA8SBFs97_EoN6qgn0cHFovcCFGCDAbrIdFviBfnZb9535DcO5zhtRMNwwD2poz1VwgeZcl9st7XzR1oouLHOE1U2pBzuBJi1QTpT8sNHjtDNE3JiUNOfgvBtAK6cxsRp-QQY3umwR_sTj3pKhxevjuCy9aXRMrPopOuHwpCzGy7gYi42wljEPx9WYOR_gir9cOwUvwhR-nQ1SXVgY8uVRWoYbQVNmpdxAPOvcYV7pZrX9UeyyCi6t1qYYIE7S2exiwtr-V6Qc6-gRMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره واقعا به چه حقارتی افتاده بنده خدا؛
اگه بچه خوبی بود و ایران می‌موند خیلی راحت می‌تونست مجوز یه کنسرت خیلی خفن آنلاین تو لایو اینستاگرامش رو با اسپانسری دوغ آلیس بگیره و برا هزار دلار بره هیئت علی ضیا کاتالوگ فیلیمو رو پر کنه نعره بزنه اییینهههه خووونواااادهههه رپفارسییییی.
جدی آینده خودشو رو نابود کرد این پسر.
💔
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81721" target="_blank">📅 12:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81720">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رسایی زورش به مذاکره کننده ها نمیرسه هی میاد فتوا میده که اینترنتو باید قطع کنیم، ولمان کن دیگر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81720" target="_blank">📅 11:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81719">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae84dba5cb.mp4?token=BO9JKumGrDzImfeo_4RPNOlvUkMM7xk-xsQhlB0iLcuRYx_bBLfbj_srTvSsGzWpm-hLf6K55F_4pwHLDd1C3sJ9Zem3MJepxFR_r6vX2LKBP3gcGLJIrfPNJWne_cEp3A2_orHKBfO0MOHKR2L3wCD1NFUQjvBVrtZmqN7CiKvpShzPE-x0Pu2bT8LHD7R_hMJfTpFZuXierpIWggsLxPj1eQT6Ud7xFrFre48Cu4MHSY223IcOABPS0qmtYr-kazJ2MtC8ujLE4it5ak3jFXI2geqpeXReUUIWvjP3Kn_FCVX3TIvXmDN5faxQVbiv8U4Kcrb5_qeMjdevqb7qhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae84dba5cb.mp4?token=BO9JKumGrDzImfeo_4RPNOlvUkMM7xk-xsQhlB0iLcuRYx_bBLfbj_srTvSsGzWpm-hLf6K55F_4pwHLDd1C3sJ9Zem3MJepxFR_r6vX2LKBP3gcGLJIrfPNJWne_cEp3A2_orHKBfO0MOHKR2L3wCD1NFUQjvBVrtZmqN7CiKvpShzPE-x0Pu2bT8LHD7R_hMJfTpFZuXierpIWggsLxPj1eQT6Ud7xFrFre48Cu4MHSY223IcOABPS0qmtYr-kazJ2MtC8ujLE4it5ak3jFXI2geqpeXReUUIWvjP3Kn_FCVX3TIvXmDN5faxQVbiv8U4Kcrb5_qeMjdevqb7qhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهین نجفی فنات دارن اکسپلورمو تسخیر میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81719" target="_blank">📅 11:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81718">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCm_LmPHbIcNjqwcPcsj9--6ENW4ZuqfE9JoS-Fleg6j_C-jyYxTG7Mc5G-YLgRKCvCwtusEAYvHu0gbGNIqchYTCOKIoDeIsYTUQBP5LUperWGt76kHxwPqnHAPIb2NZn_yhf9lQkCaq-qfAtcro75bBdwqSYTHvkPPcKOWnkoQ2op-ZsPgy7HUrCtsmEXdkVrr_O4FO6oSYYSvKHD7yCVttFVL2Y7lBeD74I9170g418PgVQiJQ4geBZOlBfbXxPRMYj_u5uVV2gj0_1wRPBxNLIsGG5VHCgcGBWIn7V7Fj4J2puNwprYjvp3WO44SzRomrqJE4bZpSFYwiIMN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگولیییی
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81718" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81717">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e5e60e28.mp4?token=uirKmYR_OpJyRFqbtcKxoLJZ87ek7Cy9yibcAj-j5tFquarEi4aSpMrriKQzILhE3smpx48jLsPwKua9PKHaGxoB_JMBoNZNGS7t5ZZkHRbjmW3vyBvdpvmVH9ijRwtuwsDCBrMkcfRhWgZhonzII-RzAj1atej4iNffZK96m--JbXefdziTGnzJ-czdZVjJgkqf5xAGPwPk_7thZUsXvGgOGVH4S4Xqt1UrHRZKo-lBY4Ux_qRHN4hGbmY8eIfZenYB-6LQAt6-SPuNfqvnON1mYhG85hJ_FoTZC9NNDru92u1acAygL016-q7EMjGxR7lerPOEFh7XkUWZnyOAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e5e60e28.mp4?token=uirKmYR_OpJyRFqbtcKxoLJZ87ek7Cy9yibcAj-j5tFquarEi4aSpMrriKQzILhE3smpx48jLsPwKua9PKHaGxoB_JMBoNZNGS7t5ZZkHRbjmW3vyBvdpvmVH9ijRwtuwsDCBrMkcfRhWgZhonzII-RzAj1atej4iNffZK96m--JbXefdziTGnzJ-czdZVjJgkqf5xAGPwPk_7thZUsXvGgOGVH4S4Xqt1UrHRZKo-lBY4Ux_qRHN4hGbmY8eIfZenYB-6LQAt6-SPuNfqvnON1mYhG85hJ_FoTZC9NNDru92u1acAygL016-q7EMjGxR7lerPOEFh7XkUWZnyOAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین علی گرامی، پدر تشریفات ایران گفت اول تعارف، لطفا بگو الان کی بهت تعارف کرده رپر شی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81717" target="_blank">📅 10:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81716">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdzDLfI6QrTUtDbwaeSbUzsj8aLGsiZV5JxRI5PgJaomX1H6kF24fg3MILV2_ulcm5YgmnYC_ESZ_Yb6KvPoOvAmtqkdPosQYVblpnwLsC9wppNvMFRmCr2ZvRC1s5IyC9R4XGj6EnuOpa2vOz6IKst3CZQN4sZXACuPcbYV4b_PP9zx566HIGN8dxhmXFwooaw5uDSN54hgKwKBmNfl5z0EP8680DRXM52zZzvuZo4mStErQOiEKKaUliYks-FAeePOSqIVLc3OToRzqAoXkE8mW_1Sl69JZxCMxKavEvvH3KtOOCGRaEVdzqeUEQOJBgLkck2TH2YaOzvrvUeS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا ۲۰ درصد بونوس افزایشی ماشین اسلات
🎰
در روزهای دوشنبه تا جمعه، با حداقل ۵ میلیون ریال دلار شارژ حساب کاربری در طول روز و ثبت حداقل ۲ میلیون و ۵۰۰ هزار ریال پیش‌بینی ناموفق در بازی‌های ماشین اسلات، بت‌فوروارد در هر روز با توجه به مبلغ شارژ حساب کاربری تا ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را تا سقف ۵۰ میلیون ریال به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SLT20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r12
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81716" target="_blank">📅 10:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81715">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امید بهزاد و پویا صفوت، از معترضین دی ماه اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81715" target="_blank">📅 10:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81714">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ببینید ترامپ چه روانی ایه که لابی سیاسی یهودیا تو آمریکا هم نمیتونه کاریش کنه، رو اوردن به لابی کردن با کشورای عربی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81714" target="_blank">📅 10:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81713">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: حمله‌ای که آمریکا برای ایران در نظر گرفته بود، می‌تونست بزرگ‌ترین حمله از زمان جنگ جهانی دوم باشه، اما متوقف شد. محمد بن‌سلمان ترجیح داده به‌جای حمله، توافق با ایران حاصل بشه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81713" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81712">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIJVit3K-agVhLt5e9ySeI3Djs3ntV6bxPfj3Ml2LMvHNAWNkjBlbSs6PCvLCU1q5D17wUZh23hvXy_jHRKW3vXQuIkr2kMBJOlGNB1Qfc0QvZPQ9x3UkBzvDaxhR6o9AP5m66DfanzY-FH-Nt4N78IB_tu-k42s52AjFshev6uiwEulaYdBqJpTZ_YCxfHvNWbcYqYTSOVy7IcL1693AjAUH3TM-cdlzFLz_QHOE3YkSEytS8jHJ4gf77rVx2HN2843UmN6RI8VAwP62uh381GzEd1GnpF7AN6oLOtc8nxZY7scMgy9ZJBYOlguseqsMN9m8R-w8xTXCGH6F5Ye2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میبینم کاخ سفید این پستو زده بیشتر تنو بدنم میلرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81712" target="_blank">📅 09:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81711">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW13vuMbGF4ioTo1OrLc9cPs5xvQhusx-c73TWsRgqyvnowQU51yb4oECCfv2WC3boWw-Xnk82QtbsRXIhZAvB82J4i2f-5pX-UkyO4gqsWaUFyI7GLv2vAvKTyUaEuOZhlzBEIoxJyGiMCoEAJwzq7JewMBGg06gW5-Q_ZjozMFVKVlUKbY7CGm_H3gvZ3KtKcUxOaPRy3XOf9BUrcfxW4c3pBtl0gbdOfmDOeVTh_nU2wIM7O5HeO_ETr0dPgtJLPX_IEpZnr8O5Q3_42l3KNatxd18ft73us1Q1U96FUiXAgNsS3XNiDFHBJJZRVZFuyqI6XqZxnqFjJMLdg-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام نه قطعیم لطفا آهنگ نده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81711" target="_blank">📅 08:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81710">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فوررررررررری
آکسیوس: منابع نزدیک به کاخ سفید تایید کردند که تا دقایقی دیگر ترامپ دو نقطه را خواهد زد؛ پشم‌های زیربغل و خایه‌ش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/81710" target="_blank">📅 02:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سلام انفجار نفتکش شوخوش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81709" target="_blank">📅 02:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81708">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عباس مگه صبح نگفتی تنگه بازه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/81708" target="_blank">📅 01:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81707">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سلام انفجار نفتکش شوخوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/81707" target="_blank">📅 01:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81706">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SroFp3d4-aDgCd8vhGPcNUgA6a0M-W9tkLWUx13ocd4P3aEk9K91mlLOwg8pOqIicX4t77LvlKqcZmtDboSj1Oh4hyY7kmkWQ3JWubjYuF48eQRaU_7S1i_J8vZDys8Cguwbl0hC4AVwDKNi071522QJEP6u16Q2xMFD9v_LjHrAzdKNmPFFF0fNKQcWnnnIl-NnrKGZuBD3i7yQ5-3uDTnY18XzHPEfU9ef1LuMHkJpqqBy5IVxuLBhcGzckLr0jAcUA4ZmDpHOc_mm8zuSb8-csD4Kx9BJ62gyaqrFrpqsoo4qs5qyxyX6p2cWVpBiIoas8LmGgt-7Rp-fKN9wxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی کصکشکششش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/81706" target="_blank">📅 01:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81705">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u93jUQfmluENzpLcWxtn7ZdSncQK2gN0RdV_UJm0jfnPuB0oGF5aB14I5VSqFdIws4orDxvdBqwaRqDnPL2QIyeKe7EuPkaZTX9_P656aHSNpST6bH0I8Rp2cREPkGOD5Kx-rhNLjmW42DeAko5ggDQ1vLqE2GLPc_o2G9D-PnTfwiI780dSpeytNx52ObG-sXi8WR_hfEWzI0P8KxdKLBSkMbDYgwkhxUJr7pVzMzxXkTpwRscwd5hbEnIWKe5qOPyTHNfmPsDLb018vYAbEGVKZnMUrT73ILId5T-Xq4D18HGwBiAJOn29lQIX_TXw77vpvrfm-G1KFsrcoXic5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید راجب اتفاقای دیروز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81705" target="_blank">📅 00:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-eSStsaQSucLvWVPNnGcczlGgNs8qzj1BL6VT71xE0n2L6DhgRd1WI5d4kkLdDWNiXxc3xwEV9hg6cgNlUWIrqOOijn57ObHNESI_XJudOX6Nl6vL8oaU0pkgzgF77-bkYhW2NuCpsO0Sb7mHhXlWz4hIPeTjYGbx3rLSsDL7fDS2y_LaTquk18fKtLL36cDW41Z3xoxcUF9ech4J2edoLTG_OUO2M9qvSE8JFkimdVifX_khiEjRTrSa8jyqnU9BYP70b9oUfQUJInMt_XxY4LFHkeaiNKDWmjFAePbrq9gf8tTbt3GSEyRWZb7DXr_ttvFjfxeRoK4VXyVa3ebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت پزشکیان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81704" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81703">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حماس خودش خلع سلاح رو قبول کرده امضا کرده، ایران بیانیه داده که نه توطئه در کار است ما نمیزاریم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81703" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIDXt5vqKzr2S1N4PMmv5v_YozqI9qYzk-7hmk4sEP0GYYmfWYjZq_0T6B9W253lMbYPbBlqUo6BQlyREbdPA8WrHrgiGGl3kHCeU-qf4TR3AtPJrYTdRtavfpIgdbdGDdvJfkeztN_XX2fLMxSZmz0FdHajzWV1UqilkVeTkcMZpOQpRm7ejmhKa2796Q2e1lindQWgzbJiEEMwdQLqLjdIQmND7JXHrSTPa5GryOeMJYdl7RYA4EbBr-HO4-Z02bW3GgGm2uf4wmt4iTEoDOI8TcuplVnsB8X-EATTx4rxh1oPG5zG1_OZQ4MPEU-UgKj-38P4IIYwerADo0-_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی ناموسا ببین کاراتو
نيروي انتظامي تهران بزرگ امروز یه دختر پسره رو توی پارک با گزارشات همسایه دستگیر کردن! حالا میپرسید به چه علت ، چیکار این بدبختا داشتید؟ به این علت که هر روز این دختر پسر میومدن اینجا دختره به پاهاش کیک میمالیده و پسره پاهاشو می‌خورده و فیلم فوت فیتیش ضبط میکردن
همسایه ها هم دیدن و گزارش دادن به ماموران انتظامی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/81702" target="_blank">📅 21:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81701">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbFoj60JUWeOjz8T-ZPMLp00Ajt7vYy7QDMEIdzYxvg_DIoN-ABIL4JbfzR4ZGyy5KHIUW--N25gmh8hPNEAmV8DVx1vEXvFOIR2CrMvfgRud15dyBM7ulWahyIlzAQr8b1LN6lPsK1-3QWHdpcrn0mrLvpPryvS2Ge5knx44gCfuSE95oHObRge9qov8jSv4KSih3tpHyfIegqG_008KOmvx70vCS5n49ltthB1uJxHf9DXEe3avXNOuKYR9m4MZjHHXCMDFqTgyRDxE7o1ZOfwNqd_bsCjgF8ZUXCcRNk48nGW_fDCaxfonFGnDOXBECI_YFozWToDASjWDrkLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- زنان با قاعدگی بارداری زایمان و یائسگی دست و پنجه نرم میکنند  مردان با چه چیزی؟
+ رونالد ارائوخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81701" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81699">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وول استریت جرنال و I24NEWS اسرائیل: علاوه بر اسرائیل حتی کشورهای عربی و میانجیگرها هم از تصمیمات لحظه‌ای ترامپ کلافه شدن و حتی یه سریشون مستقیم به ترامپ گفتن داداش خودمونیم ها ولی کصماد  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81699" target="_blank">📅 19:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81698">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وول استریت جرنال و I24NEWS اسرائیل:
علاوه بر اسرائیل حتی کشورهای عربی و میانجیگرها هم از تصمیمات لحظه‌ای ترامپ کلافه شدن و حتی یه سریشون مستقیم به ترامپ گفتن داداش خودمونیم ها ولی کصماد
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81698" target="_blank">📅 18:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81697">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI_Fff0gaWFzZZ-HkQpWum2apCQSjKstnQZKbZqySc-MUraoEPyEO8gFzohLd49xejpVNP9QUX8rsXmcGdf3MdIouowAvI1AK5w1_2qNaW7fBT2D2HeE6IXMABRSdpjzCSJARIH-wDaoEEtr1dcRVazTJ-AXB9prjGaioOvAi9B0PGc2KCWDJCJ-ji2fdQnN8oM9CTM3f-cfHc2SFP0Vcra6yNKgkRrrAOFzKGeFCdPGpAVb1OLz9M811YWe431a5sCINov9H-Dfrh8zbs4ChU9NQnHFShFVuP_ywpMmkDQYYp1PjyVFiWNaqSv5-eB9PWh2S4gX1NFa9FmIKjxf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاس زدناشون
😅
😅
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81697" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81696">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فوووووریییی</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81696" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81695">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فوووووریییی</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81695" target="_blank">📅 18:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81691">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قاآنی رئیس ستاد مشترک ارتش اسرائیل و عراقچی رفتن عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81691" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81690">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81690" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81689">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_yqPUWON-kM_A4OmLV5P-Mgfwou900wlofEvAzgMNfRQ5mI_cxsy1z1fdxKx9xddeu9KhUs4_I9TS5ejEQ0D_7eJ46NN_VDodLtCL7eiM9SLNzjc3zFw2fq285HE-GMQ9p7N6CmCKSCFmDmurOzG9o4SatE97Ter9Yadsis9eH9bhRv8ELePMa6XNuYbjsahK2I0605bH7WKi9mEBM_sy72s8Z5ESni4YiaRvWlgz14RPema-BhD1EhCR-q-wNqt2BPW0oSOPOD7xw3mFknSvdCksm9PpDYV5yhHUlTb6k1VZu3djD9ZAZJwqMWFnel6F3nUolLzeoA7hXS3ryrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81689" target="_blank">📅 16:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81688">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHr4E9J2yV1Rj919vnnw9wMj3QrOv-UMCpdKdxQHo_uYzssOaoz18sVud12DWnDktSpMWMCb13CtpMDpgfmjCJczrvf95vEYvsH15iMd5TgVFaHFF0uPYszwvzaE2_aSYIVfsEJr4yhpIG0Yd-fO3D2CVkW2qfvYWjW2iHsDKsEPjJjJiNkvGp7uUJM9GYYUXMtNom3g2F5HnVXoPYWUmcjRQ9mho8dtgZr-H5I1qeK0zsLhkRzAc-hFG9wGFGRpeS26JU73O7urSIdhsozsJjYoHiIIHDmnOEFecCoSI4UVVQAqhk3KJHvUeq6E6LHqiF8dNsppVbb9bkvO9rGDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81688" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81687">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWUcFPXn2VRBV3I2k-s1wWKoZwmi_MXQ2W0DY4krfX3H03eGaKwdXpM3pOQvZp4HJHF4kARlPWC2BK4AaMDyTRV37v0uNXrmXIIZz5f_C9N7tCU9o0o1YitbEFax7j1UXV8JD024g6QeNMdjGfLUMs5cMQN-G0AYMafj_4U3pUC88IzyDad0tS9VA-tGON92yWMc9fl4FoxDBuNmsaSmYgizXy5PArRka3JYS9Ftl7-PV47Ew0o2AQ75j5X0vMFXpoBuqY20uzfQ0U741qGKgUzgVdBzPEhADWkuIOgZs1lGEzL0TYIu_vBkPqAaTrjPvbUtG9nYNgMpe2pBvh6I4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لیورپول
🏴
-
🏴
لیدز یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه سلجر فیلد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لیورپول در ۳ بازی اخیر خود شکست نخورده است.
✅
لیدز در ۳ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر لیورپول ۳.۳ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما باشد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81687" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81686">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
چین میاد بهترشو میسازه
چین به عنوان بزرگترین خریدار نفت آرامکو، قراره سرمایه گذاری های بیشتری در این شرکت انجام بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81686" target="_blank">📅 15:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81685">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4Sbeobv1Sd2XPr9TwaBhEup5FPrtE-MJpbZJJpepF1Kjuq7rNt4rab8q_s-CjvjUydOcR4sngk1GxU2RaEaKUPxjr6gQ86VLuiyPxvHwIxoW5BuMc70YRWR2Aux0qUyV0ZoDclIENr1vNtQdGGM2K0hRitQTEWd6_nu_ZtGWtXZZAgl32JsMTBekiZrSHfY6IwvRb0bSXmwBf3uryaOo3tIWM8J6zCAOL33tJwRV8W9pIbVScQgG1hw5qJqJ980db27SqSFdORccUAuDT0ncrmw15rYG5vkt66vx61svA_X0AwTRlN6QBI2gn5ymlNTrxQ3j1mwdVt3OsKV9B_Q_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگا یکی ترجمه بکنه چی نوشته
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81685" target="_blank">📅 15:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81684">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نبویان، نماینده مجلس: عده‌ای در ایران با انگیزه‌های گوناگون از جمله نجات دشمن مجددا به فکر مذاکره افتاده‌اند!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81684" target="_blank">📅 15:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81683">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
ببین ما داریم چی میکشیم
کان نیوز: نتانیاهو و کابینه اش از تصمیمات لحظه ای ترامپ کلافه شده اند
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81683" target="_blank">📅 14:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81682">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTqeSP6v3SWZKnw2MUJWwkBOeZKExHvPfzE0F2kOYAqEBnodOqHa_sq_Oirn_RoIzJmcd0zJTsIUPkyaHnvvNTLLllU_sh8XWCPoRwzfOJ7mPirSki-9rCt_e5ltB134gz3Q08MGI9N6oGBnzWu8JQBJtm7v-u_RgimXFamWSGj2ON7tTgUjd9z7vSnepB1CaPA2NMcOV19EnVs-Vgjjf3j1lqgXw_GHMXBtnjOa8ziOIf3hNWWigqN223gHxJf4kfjNwi53alMHAhmCh-DcQ3_uBy7wfeg48vhOtq-Uc-i-k7wJImfgRCSSWuxr1asca6x3GV6j68bRdab0NmYrhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاضرم قسم بخورم کسی پیام بده دارم میگه خب تو پولداری ۵۰۰ بزن کارتم رفیق شیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81682" target="_blank">📅 14:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81681">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فارس خبر بازگشایی تنگه هرمز رو تکذیب کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81681" target="_blank">📅 13:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81680">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خاک فرعی مگه داریم</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81680" target="_blank">📅 13:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81678">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bx_pVpyfbClmzZxg3XdWJ_JjSSbwJNpPsm2um36mBz7M9ygb0mjGE5K0RpOVbHn9fhY428D1pRXPJFuHIECQCXgjutIGYDH-orgMnNRv3PefmRSUsr9iQ1DeokDTNUZIvbZgEmwTqc4Frq9JkpIIKUozuBCXV9H5pnF-73D-j2xll_nJWlpCPeBQNJC1xQMA-mrzW_Jb37px963K1Z3Cu0TqIZ_CvaRer07ExEn_wAuFhsz98yCcs_DdYsR2kMr3rzUHIDqeLtLxscbwYv8SEwAGQUZYobn1nOynGPMaWosd_pLDtjVYyM0GcJZBNkiqxnqm9keRYXwTgplnnqvtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMtajKX46B4KI-BHazmiKC1oQtfEyJk7CQWsOpTe9VhUJvdXRaQVNtSIwtKZqJhE5MdVoGeKuvrDVq84TrzgvTVzCh_D_ehTrm6gBfbIVguDg5EdnjgUyBXhMShiyOMRzoSEVazY7z_DDvSyy2LRxVrY2V2JZnFyZVgEeRW6aGlKsvwM80GnSYNQwMgNlmYVr_pRLwbzfZrxTELZfsvU2Xhbhw0q3tWmsIbbMvR6kvFk5HSbUrGb1TJDJubOGkdokOdJ5zA0A1y6FVCPhun_N-uoXZZFHKw3wkESgQV2mW_xnHDU7DWJMIFErkVm5b4GeF3DODTanQsAhHF_-KXIaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یسریا کسخل شدن فک میکنن مراکشیا به خاک اصلی اسپانیا حمله کردن
شهری که بهش حمله کردن:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81678" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81677">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsIq8Rn9h3hpR_PrrqGtVKqr5xOGBY6wuPD9ZeOuh_AqWzJk98bBXoOijo7SQ3hMWPPnlavJ-crCmn87vl2NBpXl6FUo58WGw0f5BSE3aCGtPzqMGx5t8f41EPGY2ewm-T8YAcyTLbgNPOosXfFD6GVOOrys3i3rR3T-_Oy4Blkdh6sm5Tv7VPFZb1ZT-owp_QSYi9LmP1OFX7EsXRCVE0eoYj4IAoa15LmwZDngggl0vmEq51VVyGwURENMW7J07MUC2crOQG9J57ZZDDBwPFfITIXSIbJSw4bTjFDVJwf-DiRKXaPEPq6dzhjD0812XGbhHosNdW-x-YWY3b2lFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لیورپول
🏴
-
🏴
لیدز یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه سلجر فیلد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لیورپول در ۳ بازی اخیر خود شکست نخورده است.
✅
لیدز در ۳ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر لیورپول ۳.۳ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما باشد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81677" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81676">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNwxhaQxcdk4ofcKATMAXkN3euMJJCkK402wv400YGXhkLqRTmu9YK1Dmr5OFhwvxD7cxkLIZHiSSv4j-y89rtUxmjMfWHBHTafom6VNZRos3PiLuLPxEF6SIMHmyyNyIFns3Wvn2FVq-INsus8JVTJKjbM8oBpkdjMU9c38i3tS8XDzZLIGo6RSKNTw6JoTq1Z8w_3v5PgDAQih-XA5Q0lJocyVFzvvE98cbhMIH0f96QnvXuEDiGzo1IcfFr7b8A_lceFGhwErqR72esSgst3xTtrb7Z6I00VNJYYZhetEoMrvnUpyZA0Iye_biDKjDamTrJMHka6YaibEgjKlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های یامال درباره فان هیپ هاپ:
اگه چنلی بامزه تر از اون پیدا کردید، من ابرو هامو میزنم.
#Arash
@FunHipHop</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81676" target="_blank">📅 13:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81675">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYv-zreGFG4-_vkpLkLscnhYFAs7t5ywp2bYjK2CrpTy1Hu5J4aiTgYsdR6ONBzKcq7U8j84rHdbPSxj-tlvacLUm5aKh25W5IHyJv6Jj9XwaL28yIe3hDtInxNMBSonezXDn64tJssgJJgqLTsO1lw2FF_l3684X-9mqkpqVcIyaQjuKBk0-uKytJUkGwcrSGnxzCuETpmhIjFKfm0kQffGGb68O4e3GqB5RjfQ647v7TyStybAzVt6ieyztsao1aOj9U3JwQcH8Q7f7i6UIk40y5PfEwMKk-gTzZKYbo09hXTEYFgMeTxZEjeqlD4SaO3AKG78-d1qtboCPGXC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۳ اسفند، چند روز بعد از شروع جنگ، رسانه‌های حکومتی گفتن پدافند ایران یه جنگنده اسرائیلی رو بالای لواسان زده. حتی یه ویدیو هم پخش شد که چند نفر داشتن با خوشحالی «الله‌اکبر» می‌گفتن.
ولی خبرگزاری‌هلی اسرائیلی گفتن ماجرا برعکسه و یه اف-۳۵ اومده یه یاک-۱۳۰ ایرانی رو بالای تهران زده و بعدش هم رسانه‌های داخلی کلاً ساکت شدن و واکنشی نداشتن.
حالا بعداً معلوم شده خلبان یاک-۱۳۰ ایجکت کرده بوده و زنده مونده، یه طبیعت‌گرد به اسم جواد قارایی پیداش کرده و به خاطر همین کارش هم از فرمانده نیروی هوایی لوح تقدیر گرفته.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81675" target="_blank">📅 12:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81674">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQqdC_ejTtvgfOx6K3-sbPDHaalyiXdDdUnaNQs8vjfOV1cnWvUL6ElICjRURSnDEW3lcUOeW3oc6r7-WFN1lPpy_Zu6cRi72W3jP8BT2P29Lmv8i5RrT3_CFvEkrUCMyLOp5J3_lw5gJntsnlsGZR7qVFXJ4gdgjdJjBAs6rZYJngqjzYzEXQwiDOIznD1sU7cQNeEtxeBdeoMg2kYXd5K7tYS2fnep6l3L_AO9uf3oWWLgunzUl0JdJTfCKq60Bv349YWmjDLth4UsdbjMP6TJUPW6twKJfhjqjuG1LJojKqu9s5lhE56Kw_4thVXtJ6R7ZT9f4zNjItrhlbRYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمون ایران کیر شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81674" target="_blank">📅 12:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81673">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بیشتر از همه دلم برا اونایی که دیشب رفتن بنزین زدن میسوزه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81673" target="_blank">📅 12:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81672">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhxnZGo0mIcaJfTlODgXxC43AEmVuxyc4XvdWANkMb1dqj-oLe9xQflDxs7dfNwRQHGu88eL9jWal21rfB7qqMSzDkTlKPlBARKk0dgf7KfYYOYQ41-3Np94lywrwN_tB_ykiGwSqKyt_n2Mehod05Sw3qFMRicX7Jo414hHRgI35sFizLYUEaU8s8CfPUgdjxujJr8NMGJisek8dvT_B15VDC8YU4dQfB2C8aj1kpOSCV0IP3fNKFsXzNUfe4OK72FNCITnIx3H7YRwZbvyuisdvxtCAK2BAi0uaWvJmZfWx4nngTxeB60WAj1tSTB0amasOGLAUcLJKE3h620ncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقبی اردلان این میما واسه سال ۹۷ بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81672" target="_blank">📅 11:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81671">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f01cb7d9.mp4?token=W7qyp7euEJRn7Q7QuIHlkhCZ4LEPKJwEIw-Uqer4Nl93PMtnZPe3tNL3ZfgK0EhjwfW4BZtxdya2ioOMZF7i9ejrVIEU9w5Suu7pPOxfUxvuU-PUqWJIOlKt1ybsjXkKgI9-4XSh9p8-36ldPyNOcI_9hYTaiqUhgd8o_fl9sO4bhlYy9S0huehaJ-BhZvqkTqyT-Ary1vXC1TgY2iDqB7Z7R4zrr314qKz_iCeJQfeGTlVjMvXgm7wSmWA4ExedOjBCTDJWsA-fys5uLwi4zYu9lz59jjSRVHnjCm1fB9MhihrS7NDtKduPyq1t2Tz8E7AHkphgBYZouCQhbHZBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f01cb7d9.mp4?token=W7qyp7euEJRn7Q7QuIHlkhCZ4LEPKJwEIw-Uqer4Nl93PMtnZPe3tNL3ZfgK0EhjwfW4BZtxdya2ioOMZF7i9ejrVIEU9w5Suu7pPOxfUxvuU-PUqWJIOlKt1ybsjXkKgI9-4XSh9p8-36ldPyNOcI_9hYTaiqUhgd8o_fl9sO4bhlYy9S0huehaJ-BhZvqkTqyT-Ary1vXC1TgY2iDqB7Z7R4zrr314qKz_iCeJQfeGTlVjMvXgm7wSmWA4ExedOjBCTDJWsA-fys5uLwi4zYu9lz59jjSRVHnjCm1fB9MhihrS7NDtKduPyq1t2Tz8E7AHkphgBYZouCQhbHZBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صرفا جهت یادآوری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81671" target="_blank">📅 11:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81670">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">المیادین: تعلیق حمله آمریکا به ایران پس از تلاش‌های جی‌دی ونس، معاون رئیس‌جمهور، و رئیس ستاد ارتش آمریکا برای منصرف کردن ترامپ از این کار صورت گرفت.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81670" target="_blank">📅 10:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81669">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7QG4_EV2mOxO_h8d10p8ZMqRrRegIZnvmW9k_IpWo6plQp9BJEKQqFaJlHH_JUgWL7-DZH8zzKXpkzxCIrsAKfALi6n_QddAcK-ovF1oc1V8-ZSLHPhu4tSV_7XzHvOH3KPMD017kalLCYzFHhkg7Qqk3kEvTC8u-tZPPiwjuFQRKUPxrbkf2s0z9YPFkUMPjHyEw73msOQubXxbIXoOb02pQqktdEuTQdzePvgO7_KJNDZrjmr_2EA8gRaLLaopDqmZw3FGU7XHYZRtLy01r8b6qlfM0GbzD6x34PVfdQECYRbrC-4nybBmPf-jq1WK1h9ItNeiZLelTao-HKtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش یه سینگل میخوای بدی اندازه تریپل آلبوم دریک داری براش مارکتینگ میکنی، بده دیگه گاییدی
پ.ن: کوروش این عکسو با یه تیکه از بیت آهنگ Fiancée پست کرده اینستاش
#اخبار_جنگ_شرمنده_بابت_پست_رپی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81669" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81668">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بخدا اگه این مارکو روبیو رئیس جمهور آمریکا بود الان یه جنگ جهانی رو شاخ دنیا بود</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81668" target="_blank">📅 09:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81667">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چنلای ایرانی یه جوری این توییت رو با دوازده تا ایموجی آژیر و پنج بار فوری گفتن پوشش می‌دن که انگار انتظار داشتن کاخ سفید بیاد این ویدیو از دیدار امروز سربازای آمریکا با ترامپ رو بذاره بهشون ناموسی بده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81667" target="_blank">📅 09:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81666">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLWVor8xOyQaTFYO7TLrpxNN1qX3zF80KSveksiMeXZCdWbb4gd7KMcPkMo2CHSACnidJ_M-HUu1_8pS821wpWCT2Z70eNw4-YqHusL6tVhRuckjWUqHzpM9uehIUV0tZ-rFeL-R7KACJH_KuRz_nlG_fUb7ySzhi2HS5pALYkqZVzI5iOg93Mc_b2F4sZhudokfUmBxru3AG1gfuah8C7mXsUGWALQMwul9QkNWT2tB-e25Tk-chM1YjWPzKyI08F8X5RoU1UkO8cU2aZ1ksxgvrVUhCEZZO2rSnuwsQzjoZeWR6fxmmzNVVxBJuazxvGYvyU1-pcIEJ5fzUkL4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#معذرت_بابت_پست_رپی
رک بگو میخوای باهاش فیت بدی دیگه این کارا چیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81666" target="_blank">📅 09:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81665">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید: این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81665" target="_blank">📅 07:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81664">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftXIpts3im3ogPFfjlAJqAzTu1jBiUG8W-i2fKQ9N_xXl0RHrDoLfa3wv1jmf8a5PktaR1quiAzVRFX4T44AIRGJmVMOEeZAzJkbfHhOIlOcEWnR6GFVa1dUrM6X7aZoEIXr_j4L497D9qRBCKnBYF_vWrTO-jYfVPkUAsk7ukHHRSWhSzJZj4dpsx77bHi53R906RTwFZVaDHAImsjm7VsZHBHjvkL5AiSueeYME62UFqzd5OMfyxYrUivwOFr3ayT7t59-sv80zhqLtoWx2PBrJPb5ma2hfdSOd9kWDisfh_cZH46dBUReX-sDWgXD_1eO2FgAuie594zUL8HC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81664" target="_blank">📅 06:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81663">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چتایی که از ملتفت پخش شده همشون فیکه و تو ویس و ویدیو هاشونم که چیز خاصی نبوده جز ی سری حرفای جمع های خودمونی و شخصی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81663" target="_blank">📅 02:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81662">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امشب بنزین بزنیم یا زوده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81662" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81660">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce55f6098a.mp4?token=bOgmOsg-LAspVyeMzprRdGfVjxXljjzEt1UV7V8Ix_h4nk9usLfEmc5vnb36716Sq2PCTPEVWQMCo104ZL1NzXSFY8Yatka7t9Grj725pFWfe2_S26NA82n5ACcukwdRmfEc2aHULh7xkOcxEEw3Qt3G34P9PKlQtIcZrOYIKVHqNTrIidk7HMkvZzyLprAehPUMBdbhOsNZL1pTBasWilFgaSPcNbdIEtPuFGLJXBsDSZmB8gvfsIeRsD14WBL489wrDwcfY7f0NVxGulbRX76A7EJm7Ihd_y6I2MHuPaL5iUalLG5Q1J-mIxJ57U2uwbxBbqB_bD28xohCf68qdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce55f6098a.mp4?token=bOgmOsg-LAspVyeMzprRdGfVjxXljjzEt1UV7V8Ix_h4nk9usLfEmc5vnb36716Sq2PCTPEVWQMCo104ZL1NzXSFY8Yatka7t9Grj725pFWfe2_S26NA82n5ACcukwdRmfEc2aHULh7xkOcxEEw3Qt3G34P9PKlQtIcZrOYIKVHqNTrIidk7HMkvZzyLprAehPUMBdbhOsNZL1pTBasWilFgaSPcNbdIEtPuFGLJXBsDSZmB8gvfsIeRsD14WBL489wrDwcfY7f0NVxGulbRX76A7EJm7Ihd_y6I2MHuPaL5iUalLG5Q1J-mIxJ57U2uwbxBbqB_bD28xohCf68qdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فدایی حتی به لوله آبم رحم نکرد، وصلش کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/81660" target="_blank">📅 01:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81658">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27da425db.mov?token=azQMB6WKD0Hq-oVmWnxKJNCtwgJ0u8MgiUN9Wb3S0mVhPuzo63DMky645Ze5bQScsukkRyKRRM_gTa6dfHKHDnvXGp_orWOfpC-2nt3JafxfnwVxgTxiGpQ3ofUYt5F-3K8WZrWBSSEKT3Ms6d86kYF93uoKY45FhqN2HEwlpkUyAch7La3ozAOBqbB874A4yjKRTW9FSEzp0SzirRFsgbiJi1_VDGV4XDMgXCfC_Rc0VMafmMDW718oXzjqMvuwTAhcfrw9EnczZgJ5WkFOrINbm_gcGEBuu-EebrWZ6kOUgUKeTLlmrRMtwHvYBWRXlQtOXy3a7-A2_JrwyJYMJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27da425db.mov?token=azQMB6WKD0Hq-oVmWnxKJNCtwgJ0u8MgiUN9Wb3S0mVhPuzo63DMky645Ze5bQScsukkRyKRRM_gTa6dfHKHDnvXGp_orWOfpC-2nt3JafxfnwVxgTxiGpQ3ofUYt5F-3K8WZrWBSSEKT3Ms6d86kYF93uoKY45FhqN2HEwlpkUyAch7La3ozAOBqbB874A4yjKRTW9FSEzp0SzirRFsgbiJi1_VDGV4XDMgXCfC_Rc0VMafmMDW718oXzjqMvuwTAhcfrw9EnczZgJ5WkFOrINbm_gcGEBuu-EebrWZ6kOUgUKeTLlmrRMtwHvYBWRXlQtOXy3a7-A2_JrwyJYMJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویسای منتسب به اعضای ملتفت(تایید و تکذیب نمیشه)
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81658" target="_blank">📅 01:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81657">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شاتای جدید مهدیار و شاپور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81657" target="_blank">📅 00:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81656">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یه بیکاری اومده چند تا شات و ویدیو از چت اعضای ملتفت پخش کرده که نمیدونم واقعیه یا نه چند تاشو میزارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81656" target="_blank">📅 00:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81654">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kG_lAcbD3-lLYT1n2C-pAGBDa8at-PAsOFSWrTKI9Os73xtJMqHFa_N7Z81MRKCO8hqxCcOTJgx7jhWEkF2zp2xZ5xNw3QrcPt--p1t1NEX_agUrrrLQ6tiH5cg90wRv7gg0_DybF4CXvHli03_5V3KFtLb6qkvpkIGYPHPuJv7olU9tavwMer7QD0UgKb-WEwdjHEBWvX-f1XTxd6h_j27zkV8ulDErKfA3O7hXLjGo7DrzFi0trPxKJGgh9D07P4GXg_VMgNGDHRiAieEQztO6KIewGCeqqa3F6wyRufbZmayAcCUIZtpHXdEJ2rszaGSKb3B9yDrs9GPm_CpvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqVqGX8geKeyAqFet4FnHfhqmgysuQQy-DLwPnICsHeM8DIeBAykeiQ-gAeSJ_zFeBmZixVraAH3vXVR7OQifYrslwFqZKKsrTj4p8-MfknqvzWK4uzd5JQYxMHJqZpk8Z0siCOo634oVjvEL23DIlM_cwDKLmY17e6Lz-nsWrpteLNX_8YvD7Lu2tAnaWQoyv9_IgPOuSUZPLkPN-L5oJSw4QnmKUnm41QkkaakhxApcWrL_LWQ-yIrDlOqJPpXESpEOsQh1gqj52BoOIlltE_sHfuAmdjI77hhXpsyEYoUPlq-jFF4r7AQbxkntiYWGsT2ejSO455M09lyx3hwIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید مهدیار و شاپور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81654" target="_blank">📅 00:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81653">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ساعات پیش عراقچی با وزیر خارجه ترکیه، و عاصم منیر تلفنی صحبت کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81653" target="_blank">📅 00:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81652">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ساعات پیش عراقچی با وزیر خارجه ترکیه، و عاصم منیر تلفنی صحبت کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81652" target="_blank">📅 00:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81651">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">زدن زیرساخت های نفتی و برقی برای امریکا و اسرائیل کار خاصی نداره
پس چرا عملیات رو شروع نمیکنن؟
چون منتظرن مقاماتی که هدف هستند در دسترس قرار بگیرند
اون موقع عملیات بزرگ شروع میشه
دقیقا عین ۹ اسفند‌ ۱۴۰۴
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81651" target="_blank">📅 23:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81650">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhsHcwqjmDgDRmbiBziNBmPEpNo_QoZLMmh1SUoBaCvByueYoiVPzzdt_jrcqPhHm03GfELWO_gpO_4LtbC648DlITkj_Tg7e1JwDz6ZeE77cO4XxHohhbd0Z4C4HhhZo-INhsnzVEETLQ8S_ODqLJsaDdNqGyXY6uypazl78KT_GAWU2GIXi7aq8UlOjPlZuvIV5zHkpU6ThxqZVGdtfUEtyiv6LUc34UYjeUe7oKKN0LKr5Z3n_mQ9ZM_bLwzT2vt8qTtEw54aYcUED68-LlTpVkuiJBzQElgqBZN4MPe0mUaTiXtifjoAMpFTQlmr7fO6UFBpMcbmTrfHHBKOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اکانت رسمی مرتبط با وزارت دفاع آمریکا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81650" target="_blank">📅 23:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81649">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چرا کسی از من درخواست نمیکنه خاورمیانه رو ترک کنم.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81649" target="_blank">📅 23:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81643">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWmdAqggdyyN6MtMLUg7xcoFMx_0HglWH56eL2ZuZxIKdrFw934PZUTtUONNvtBuNdx-YdUvjns71GSOj7O5djAnWuQG5vtQG0CGrPpj9idm0v_TylcI3oELNHOW8wIaUjLpLUFN8M32sJcULz5k0fy7ND6w3taaiEkqsVIDd4dk9oQQXW8-955CqupAqeTed5-gbggp8Z3XxBLuJ27k2UsFujU9J0MhDEYgPo_uRLIV8icm7lpe38nrcSFvhNlez9VpA-FmOfQysTiVtu-bxbsQ9QRgVU4A1dU6ooSqjBmtrU_6fsOXinkamHp3THtHlIEDq0quapRIiMSuGVpKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SItCSKKNe4GC6-_xM0fVde9AEm0KPKPxYukSLtAaiNE7sjxYn4URKWUJezdkX1SpLUQbK92JiIUE7NwB8k-bCdSjvY8AiiJQneOkb59m-Ustq1doF_a4sl44qmdtBz0CowlOUoyQTvgCRvYj8HcNgn3yNzTHX2dVvAEt2c4e4vBROPgC4kFoIMf0ZnDRObomb21OS2w5witPLknwyFe04HHv9PeJy4MJ1qWI2JIGH9a0o_NRR5exXo7iM7_B9gATlwajQyZEEGBES3WnekPxCsb9O-9LhbpiS-kKEisu-wtbgIQjALFYvG3igItaR3pZQx-nmCSU2expv74a-X7oWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaXQmnpUFnLUzJrIfHum51FfUaZwF_3LxYQngC4qpcKB4IGYlU8XfbaiB-PtYAOedAAog2s6IQnZZv7umvj1bwZ6xVnXlUSBuZ-Y7M-IQqr3zzinG1vwCyec2LLTu4s9-Tdem_4jnlBcbP8VVT6YH4JLId0a9CFHqBGczAkjeZikrUKPGR6fT0fjtewC2qRwqJFkt9srZdb9lX5SOWHmeXZJDdr2d_VNGIB3qX4T53TWkkNSFv_FVofaqvRbQr23ubQ3Rq7DL4tkRx2MetYNsmRUlwATPWcj01dIJd8p4UZtgx6ntRrwgbEfVdsTRkgjAduGj44Kr0or0EMIiN0FVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWW5hnMLRzSpptRAXTQbSiAEWJnVg4fPr7WELdYJXlTf9b1AZ5Q5dtogvScP5fPaOn2SuzgoK8B5MzKw9mWKfpT1X-XPKdmwyy8u7QdykkI73cHaYl6ALde6zZy4RMz2bijrf1XbQEJruYFTeeKKOPIFVfCa9hD2ajbAjuygIUpR05x6GgHILK2E_2b27PD-_fMyf3wBymkzUp6waYY2eXFows0UwXo4k7pvE07w4A5YbZsPl_ZaivNXVReE69xQr7ZIOSM5rd0YjRNxBfUwZzon_ZtcwM-siOISiqXfW__Hmv_hsNHYtfox0ek__Iwa4c0tPZ8PBLvDuCmLS0__Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROO3rl4wQjncd1TBHPF4_UxhuuhzbTc1yF1wbJzJCH-hqKfW9oKxzggJ_pJL4SEiXaDEp07QGudckhfQws5ixSvMLIaYKTS_tGbJ8jEbqld6zu8uQu1tKtPgJnOQNcXbvEbsBHdwpnijwnG-9NafC7IbGP9z9H8Vna_NYa77Tnl1S0b6rYI5TntmSgQKjhRRGCHR7TZNyVoBrxyOqofvhoAnmg7CuFa7H7WmyVdMj5y84M8tlPvkbmXQCr3MzMQeeP2CP55oWeHXfefU99FgRENjG6kfNyfMIWbgjRKveVDWJ-ZZYhEjBhfOUFMjM2YWePf5SDXKTaIBCtneYKHxrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تنها فرق شوهر عموی من با ترامپ اینه که شوهر عموم، بزرگترین اقتصاد دنیا و جهت حرکت تقریبا کل اتفاقات جهان زیر دستش نیست و بلد هم نیست تو نیم ساعت 37 تا کصشعر ai پست کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81643" target="_blank">📅 22:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81642">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">#پست_دارای_محتوای_رپی
سپهر خلسه:
نیلو یعنی عشق؛ شایعه طلاق و خیانت درست نکنید.
✋🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81642" target="_blank">📅 22:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81641">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خلسه چه خفن شده</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81641" target="_blank">📅 22:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81640">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خلسه چه خفن شده</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81640" target="_blank">📅 22:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81639">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این سری، این سری دیگه قطعا میزنن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81639" target="_blank">📅 21:43 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
