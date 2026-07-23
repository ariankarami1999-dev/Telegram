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
<img src="https://cdn4.telesco.pe/file/YOxq070t0dZpYCmQekig9NwpN2t5iSn8K0puPFdDOuw6kYkM-iX5o93MwX78NngB6NM0MupEDeCkOhrk1WYB4Ep8Rc-yVOaJ6FDhhaT6ueRmlY7orW8ZStiwUUYv7ixUXvhDlc9UMfQE8BtvR-xSGDGBDQjc7jdQoLo9WYeF6AxAaF-z1OMkR4Qqhu2K5Z8nRSM2Dy0L5uelWHHXnhZE5YUo8JYWLqvck9Z8d0rOXCwYU8w6OEMoPChu4YUD9vBRNMVcX9KpEDsQ52S2msuZDz1Px0NMuLaDWn9TJCL8_-QI8rf1wYJhWtQmu2EuEy6RqR3lI3NZkxsXR9gFJ9txaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 553K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 21:23:04</div>
<hr>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdFwBPAmTSiZEgpavRRZzWR2na5_l6A7rkW7OegCTlXpaU8po4ir_Rk4OsBUJZdVJjycquv94I8oUq3aguXZLzvBhi-n94fW4bABu2UOGzeK5hFzE8Y1ajCE68UyJPHWpMuVNS_CZpmYfpkc9Pa0kjFktZHHHeHuqKU7mxosmgUAhI11EAe3_r61K7HoZUuySDW0rcMdOAcsPbWy4HZnQmgMd5grfzxQsec-SR7fMnRZn0MITF94WsV6-wGoR3iEHLNCxK54ieZMLY2UMU1ikzTK0tI9TyyavMELqJwSuni3-dkjAuF_672KYiodpIi1kSXoODJglIjcvr7Q2Nze3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=tyHMOQdAWycA6sTyxlHyo9ExOYKLa7ZW7L_g5yJV6H78ysInXpXmqdwVPR6D8op65f05PnsbUKywglaMwWOGrOOONLVVSW40_NX9lUPOEwjQSK7XdjIr_41M_5Ky5lCFzGWNTmlnnM30Ng1TFX_9z_CTJFmGiIKe0kBQo7tZlf4dTRIg9tydbyvc1FzY1TbOvxXnjt2iEl_BZHWSMcYoFeKfIWXfWOpobnmb_JXxZbJTJtk1TEcQfIb9GoFdJIjONRQo15LjVRICakaCs1FdkozqAYmKUbdu0pRxcaFlF99qKs2LWn7UvQ94F2d-b6Y6qRP5bMvxVz8eltNSz8xzi01I6pIOowKsPEEPARZFj3etff2UlV5FN5IMN8Io09KDibO1MC4eof57KmP2roqcgwQ2AsgE3muEwndaFmGi7H1LxPPC1FXnAMMNb7FK9X4o8p52umCWZnakGg7OeEj_q0zVdR8CoYEJ4oo5_ZpJmkENi8yMMMxeZ-WgdUCGezuAi_6K6V9TcJDoldRw3kg7V4OvbGHjC3SjucAOqfEbbIRvafrMngWJe8OVPuZdBasz7mBrmBC6loFkdVh1j-5ef8GzmT3ZMRySPPGhG_dX_Idej9VtmIRqW2Hd5nC-9tug1BhTCGTlSyw8UjTOfvseaM6ujggT-82ZWgWtXFadvBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=tyHMOQdAWycA6sTyxlHyo9ExOYKLa7ZW7L_g5yJV6H78ysInXpXmqdwVPR6D8op65f05PnsbUKywglaMwWOGrOOONLVVSW40_NX9lUPOEwjQSK7XdjIr_41M_5Ky5lCFzGWNTmlnnM30Ng1TFX_9z_CTJFmGiIKe0kBQo7tZlf4dTRIg9tydbyvc1FzY1TbOvxXnjt2iEl_BZHWSMcYoFeKfIWXfWOpobnmb_JXxZbJTJtk1TEcQfIb9GoFdJIjONRQo15LjVRICakaCs1FdkozqAYmKUbdu0pRxcaFlF99qKs2LWn7UvQ94F2d-b6Y6qRP5bMvxVz8eltNSz8xzi01I6pIOowKsPEEPARZFj3etff2UlV5FN5IMN8Io09KDibO1MC4eof57KmP2roqcgwQ2AsgE3muEwndaFmGi7H1LxPPC1FXnAMMNb7FK9X4o8p52umCWZnakGg7OeEj_q0zVdR8CoYEJ4oo5_ZpJmkENi8yMMMxeZ-WgdUCGezuAi_6K6V9TcJDoldRw3kg7V4OvbGHjC3SjucAOqfEbbIRvafrMngWJe8OVPuZdBasz7mBrmBC6loFkdVh1j-5ef8GzmT3ZMRySPPGhG_dX_Idej9VtmIRqW2Hd5nC-9tug1BhTCGTlSyw8UjTOfvseaM6ujggT-82ZWgWtXFadvBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unGyYLy6hAegd0GC-jM4ifYQqQlkZZzCb9wncQTe8psRzl2BzsSAFMoVvEoJwByGWwHoyBcJdlggTQMdrOTY1lumAG-Js9D7jhAm6qjtO-GB1csbCwnzHMtlJN0ERNFbGCBSHXOsCCYsQHI-H8X3w07DV0okDGKgw1oto6FD8s8NYdrutBDvt6OEY89QnQHjg5OUB5yL_0zfDneSOIY956ixyOK5Er8Sp0u5VciecC_InVnAMMEH0wCJrtgMQFo0cX2t2OdjF60eOd40jHkGuhAHt5W8HTljr7AeuUHZ752nDIPdcDz9w7iJl3z089_RHl4fHf3NNsjLbr_XTk6ehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De9TkAfOOzAWELPk8s1n3Bpn-rH3M6TAmSpM6DvFF_mDnNjTYOXFORvp4SFJ7S22uH6gTaANKFEvGyaNmMf90DoFRdyFD9rYXt2J-A8EWQngkQRvFPmqAvgkU2XZmkRK2qM0fs-0PVnvxVg9pCV0YhJNGJYmxyPBVueROIM1uHvPmZam1CG6BEeosxPSnh3EU1Uk7T1nzDvch8a4HGQf-0WDH2N4RBxbmWlXnlt-crKzrgCGlDBwfDqy9QQxzFF5cUWBQtCZMlU4zLMWiR7NziBsDPCYtQZYnnav8BVb9CiHr0aaIBCsXJ1lqhdzBfIl0WDmTThLBgGgiraJaB0AeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwc-7qyEft1wT-ndxx_hdiVXCU0qBnUEGoxI0WeZ6DX8gpo_OdFnxMb0oH0SPn6vAsZzpyYRxn07UM5ZR_1Kll5C4uXFn1_TOSEiNJytzTz8nvnw3HICAIwgBDPNo0PbOM-LV8qHeN1w2moRgs6YX-WvqmrPSD_iJ1Llo5CHBdt2xvm6VIbE_oaCH81VP1u18fsIFF87e0YnEjg6bgHTI5Zc_x1EyN-5kKj8bBFe8qhqPzNksleGEhzm-MnhfGMJEVGe2y4i3AHcvVhbZCOPn1182OuBEHDhK8WzcVGeM1lF9mADv1iDUkNAShR9HqC3xh-Zx-4oF87zkNY23yBtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5eIEcnWQA65ZIy67PMpWw0HZnTE9hCnE8pQlf6JXJAuSk_YUw-e2_1AFXGSmjIeghB-LsQSdgnAxPL8ZBhgs-u_-accrEXlyVAKdZD8UIfXn--5X-kxSWnudiPIIABSgq9X2OqC-t8F6zsh7IEFbP4FpWoaFgkV0wmwOoNjwMhEUOEsA3V-G7eL11qj4lKo3MP3rjxqYTvy0HQZz_gdGtrNgtuJpJNDQCunwlQBRbPIjzYuAhDcEXdDzV4JPUTpNTKBmQk5CeqPuzfphG4DjFa2fqKzXgiaQWDPc4fPsiEzGLevtlNuwKyb1DakPfyvivAR4Fod7Vcu1JrodEPfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_dIvFnbwakqCFLH7qW6wvDzmdsrvW4ykxVMshkBi14eLfeUQg3h2wUAGYN04ON9Cr5Erx8MHNJSEJUBUNxpl8gkJdHjtMR0OWUhBRPtyfIP6vcAIq9JnApU0iW1WDSzPSAa39Mon1qsg3pdht5bkZCQb_bRLPixBupO8nNe2jWvAVD04e1500O2Uy-4I9sEbMTjJVztChlblPiet_eDrSPvcvlrY-eWk9kI4mMYwN-b7Rqa3erVsSi9Fun2EVv1Xugmk7WlGsNwMTPtGTYVYwY-AugnsKJw52HewUTw7PocsTFYVIf4PoYQVrVeCFZGze818lUXO_XspeJr79olWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26359">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1c92XWqokyFO_vcLOjnIm881no_60acVTJMrVFl162t4wksD-jb3kc1YVOtyLBGkLATeyvqb_ySc3gTwTeZXJ02qdqVGamBYK1-AYhyraKmMrvMQhGs8S9_OmNCoaRU178FAMMT8LEbyXKsfB9w5ibUgmgcxFBX6NH2Qvtq6fvMPWSmzqbOK5J0xC8xTkoOMPnbvLnSaZfGL1rR1wsMGtAPk5KdT4A28amamqq48-PJWVN3i_3mJ77Hx9yL96Cl7skg6TH2-kcQ0KyDgSncmM9YutT18puJABT0Wa1HJJyZHX-YPkGJsJR9uGgwmtslFhT3v-YCyHKoPQWfuqvoyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/26359" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3aD-yQv_td-0dLRb9X9WPIU1t2oNZLJNoCX24ahDb3HpNmX_Oj7Wpn_MSEMAlFDF6BG8_5JFgREiLi9ZTMf2_0X43eXETJK8Q2jD3EBJq97ayIGPGcy43jXH-PfNqOxrDkBgrFc2OY29Zuuq3Gxj8KuHYYJc0l21B8w7fz2cva4xW2PjkRherWaBAFX4mO0q4bcqmd-z2-6WElQRdxIk09FH5ryCly3Flwh_q_tFSk2_7t1BqFbx8h80Q9zxG6-eZcYXqZLOyb0RMDyqA9wlKqpHR1HUhevAzQHMLH4vP4FZYbAAT-TbOwcAmaVyO2Q8Xf-HoyrW8k3LWGFkn_p5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqO2jwoK0cZc3hik18ZHZRy7TlgkbFS_OG1KUxBxZdjc6o2OY14MOWGbGyN-uUU7GpCNeha6OQRyhxtvc56EYvaExFG9CPHT1ZWVFBUETuNN0313Q7nvxfjLeeIxoGOV9nJ0kIfftFKITD7CcO5wyPqwFYAoiSteMomWVez1Ys2Y2cWEMRb3QoJT_cwTJ47_ZZoo3AzSozFObHeW-EPnhgbdhVXrs87JSLHYySMZzHcAgceiRZGWOSOrn-BUdhRBHUdKhvH7DAtlQXYUHG8eNgezi4XTIs9F43A-hpbQg5QcoXAc1WGc_CPR5N9XzoD86xhOMlRjDnuRmAaPvtMe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=kgdKe35U1HTFKrfD_qYsgKgMrDL2uNnldRbgc4XNjAV7c_LEMDaYsqTi2wCuz3nO85Kloxy2lbzg-tq5GoEyUBbj_Io5Ltf5m4vgRfO6LBMjXqMSQ1w4zSKOwl_HYFto2peTJ3O1FEoUcaIcaf-Qiz9mWWab2O9kGBQt4aJIW7RRS01gOCamAUt8ff3N59cIIueZWQq4m-E3q0npHKMg-eStc-vjpYtAjIzy5t9JCP9TeDFYM6n992_KNjM4dwrXVH7O7XIM5Ha9UT-Wg4WFYlW6yn83DpQW_7mYh8qTUEIXHl67_XvFpCg_ORT4KLM-umUEiUkyvd-7FTucIgKzjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=kgdKe35U1HTFKrfD_qYsgKgMrDL2uNnldRbgc4XNjAV7c_LEMDaYsqTi2wCuz3nO85Kloxy2lbzg-tq5GoEyUBbj_Io5Ltf5m4vgRfO6LBMjXqMSQ1w4zSKOwl_HYFto2peTJ3O1FEoUcaIcaf-Qiz9mWWab2O9kGBQt4aJIW7RRS01gOCamAUt8ff3N59cIIueZWQq4m-E3q0npHKMg-eStc-vjpYtAjIzy5t9JCP9TeDFYM6n992_KNjM4dwrXVH7O7XIM5Ha9UT-Wg4WFYlW6yn83DpQW_7mYh8qTUEIXHl67_XvFpCg_ORT4KLM-umUEiUkyvd-7FTucIgKzjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Fo6UXcc_C_Q99PwzYfF6yGXFDytd6aRjcbzG_bho51epeK0vR3kNRa70O22MXvqV1UPsc-qsYoszcLoBDCWsq8YAOZ8QaC6k8Cs-KV-UoOp8W-nYT2NHhF5bHt1VxK0SGy_I-xO41JvM75ToqNHwhgLmqOTtYQPbTmu9SXQw7mSleTtSuP_4P-vu4h6n_0iDU7NdiR7vDtksXgXV55o4XoAW_zwo-ezqGuJqUeXbH8VA9Je69rHSj4eQc7GTFLCn0UtJqovHi1Io-GXF8cW0jm20Tfxzp3im1PBWoC4dPgn2YngkrgCuUaQEI5PQh1H0IksSZxsBoDNnCi1wmwUC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Fo6UXcc_C_Q99PwzYfF6yGXFDytd6aRjcbzG_bho51epeK0vR3kNRa70O22MXvqV1UPsc-qsYoszcLoBDCWsq8YAOZ8QaC6k8Cs-KV-UoOp8W-nYT2NHhF5bHt1VxK0SGy_I-xO41JvM75ToqNHwhgLmqOTtYQPbTmu9SXQw7mSleTtSuP_4P-vu4h6n_0iDU7NdiR7vDtksXgXV55o4XoAW_zwo-ezqGuJqUeXbH8VA9Je69rHSj4eQc7GTFLCn0UtJqovHi1Io-GXF8cW0jm20Tfxzp3im1PBWoC4dPgn2YngkrgCuUaQEI5PQh1H0IksSZxsBoDNnCi1wmwUC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWxmBggWwQznbBepo12YLLjelbnCb8_hPGWlLv4mxlCm8eyxPWE-Fup52Dh7xwlt_2MNU09MgD9f9ag8CuR3DekXx0WQaHDy6x-nxj5E4VAx5PS5DrvFJWSUhCc6QUNWSnyIxPiIyY2i5GkLRdARYzndOUGrO07ZjEKEmCFyDs3_aceDPOqioncQOGSUvOx8KL9eS9qIWlXM5AWiaasqgwzqfjGZ5vviXWBB9hkHv6Zp2S6V200GLKu2bzdiO-POPzOoLZ4klWFd6_jcfBmWqHwo8Vz0p7jo8nV84m6PY1E4TDDQ4o2piifuFtMnXGws8vhEEwijGGkbMwrij_lHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLBqqvUJjGyCsQ7DUEFv-GqaJfJ6I6nw8qeTC90swm369o2W0cKZ1M2WyHQ4ub1B_oiI_xpktW-Ic2FLkgGHBUA5m_vjfTCPgp23CjEhbn0jgbCO2-KTXKk71z-LClUaLu5lKuV6Cojj7-z7JnzKwQByr7BbfPDqF1Xw8qw5B_3G10y8a-qvSV6xFzaB-M69ZbNVwTv_smEkgsIpXZGziTLXtkBK1Hvp46zNB7zmBMzIwzaElKv3VJ01WJpOZ-dn4wauJxu_A3IiSujljQLjwYygQpEqLRUUT_eBZsZmsYMWamrG314q77KLJ5aQiBiTbl6MYTw5ruQICwQYTSAy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgHSp4FQPT5edCGRTVBS4QeTExlLZg2kkiMvoQDm2_uQyxSODprtlQzd-pCi6KasAlo2-Sjn9XQBV7v_9JOuN41texcBtD0mxF_3NPzGZlgJlf9ewYGTkwyUlewLYA0NcSRCiBzKeQZEY3foULEt2hOzOu4rYOQ-3eiA_qQg2YraEXsmBFY9r5VKweY4xzv6Ecgewu8ELjD4PLf9XSMs7cYpjOyjjmGpPWYI4f4khLuzR8pRp5hz3ibNsetVT1slA2rPIPOYMKKiP9x1OhEbkfRdhhybMmvNDTLHmiDaHJd7wHeaMc9ZTVfjJyNzNI5yxza-O6XjFafkSXQNit4u4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voXfS-YhRjK86VpLbhCrWjLv0xUto9kt6PSW4f0w1YFa8cqfnJVC2FWSw9iSCD5K5gX8EDSz1VDmUcpSZYckxN9sTggw66OAo7EKuKUTzoQLw1yCaxGGHjI72SVtnBNyrZ-NtqcjDCG54ocXjsm2MgoM3e8FNMYJp8CsAsETzp4LN6AHB_jgapucI3iFqwigWBJId57BWwPRq8EJv35KbsM6SEgsab6KYdqhEBLraKYksZGVd5noXwQnPOZH_8si0dvIN4rOyrC3gDQgWs7fGrbiT-hxZqs_XN062NlQzuL8p30MthVhFoprZn-FC3-Rs3lC4cAB4KOnkH862ZgM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwT0W9ddS1AN_HfBzYjYAFcGZnwtA2Gg41d4Y0aOW1vICpgsIv-7kiBpJtPxsRit4xuPDMcf4D_WAXYv2eFEaZDSqcSGjFg8nrZX6rSAQ8U9tBlOMit0ZlrTjUOMLTEFD3P8g_QG0u0dgBvlwEKnxLIRWwMTeCovGSYyIW9uW-72nDZ5CIC44JQVaJ_-d6SsptDPPNH96Uc5q_D54tjHdpkQPfdqQnoEgBdOwUGT8yBGKM4h49Fcy61oHaZMFBKn_4wnJIyA-7gRoXEDFIIcurjmTw-wEz6RvcfS33Cn5Glb2IZ8L5-K2zviyFuIDgNlPs-7Y-URnb1q2XMR6bv3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJJbFZb63tFVSKU_S6oS4yPXsafURms0CrcF_5A8rEIQjXhxLhbGAj-ucIk6QW111CmWXlcj5Q-6d1fSJ8Snp76mNC4VkF2QmU-2wbOvtWUMhvl190cKgVFgVewBG-V0qlJuUQjdrv6S8DYiEWIrX3R2aJ9VfO4Z34790s6TYx921XVIrNYyjyPfVPTjFwwS_fEadmNymgpAkVKhjM7Ey8qxg35Pudj20J5zecjfaK9ZwR8X-67pnRBjF0UiUznhsko6lzVIGxW_eEnJ9Kak9qiMxpGcg40hHlr6q_RtmzMt2Gc91g7ntsSxvgXx957GMjkT2aFIUzWPhYcCcATpJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJFb7yQgoTuZtg50X1f2eXsWSiBQM-l4suzT6WYQvpGGmfyQnXal3gyatBAFkg7CgxrAImcA9iRyt5TYOhE_NW0f4RFLtIoN9hH1l-O1pM3L7QvxKCLPAxfXlC2Y2EavJP3dvwKqC0iQiNHoqK_NmoMGurZfNss1k_79mwcM0xOkbLE2aHy1fO16xMEKYAK-xPiJG39_Ee6n7fTitxI_XJTHRDe5rBlgRHB-OX3Uv7bjxy15cBM7CbVdaOPZHL6em9RlcvqqJ3outtzMEweeLWG3ON9a1R7z6wYx0FdGN7hlrWNyAEKDqToiXslBUVAToiaLeVqd_hbaMqaskJtnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26346">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWagqnPWTc2Rgnz37aT8k3zGW4d1jGTmGFZ8aIBdnKLNywpsxBMzm5ruXOWctfQZdfNghkhiIaqThmiqEopC-AbRrqvP2cJMHnkbL2WJmCV03IEmtw8BhdBeQF0WtPlSRVbSGl7Q6cmVjwglgNRbZQzD2s_ayPwElYqFM1SwtQjF08X7AfneA-yb2TiBdRgdQzaM93xjsShm9CtK3imDiwF0PEE2S545TUvwancZBhRhq__XFSq3Y3t5gjBUHV9fwlFEh02jwT6USsRfbyI7_0FIQH_TCwRuc5kqGSCfSfK04aZs6zFPxGm1mLTluq8Daa6IzOl1k7E8X0aPwXh9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26346" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=DkttDk_L8YCwlmjYANErDHhniJKAM0ky1GHmbSc4ron1iZVFCaKgOuc-rpOVRrP4raimdFt21M5DkuQgjn8_7m3WfDlRJyW_XkK664SOGrROakoGFvwHJeZvMNmddcpjtcJ2ccjJT0nzqAnRfLYNb_gZRpHVxd6L4woiJr8jj47hoteIonQ3FlzvT6hoLRG1lqsQSBMcHUmX_QPNHEPCHUDyxgrRxF741jBSlI_gU47B9uYUxXYoSeW2zRG_bB6KbCyLtADqJOqEFsDvD44UeU4s-660guNWZMwzUDLX7lemRuMTA0FBshIMYiFMYfPg8K_JIFNy8tjDMc5gWx_GZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=DkttDk_L8YCwlmjYANErDHhniJKAM0ky1GHmbSc4ron1iZVFCaKgOuc-rpOVRrP4raimdFt21M5DkuQgjn8_7m3WfDlRJyW_XkK664SOGrROakoGFvwHJeZvMNmddcpjtcJ2ccjJT0nzqAnRfLYNb_gZRpHVxd6L4woiJr8jj47hoteIonQ3FlzvT6hoLRG1lqsQSBMcHUmX_QPNHEPCHUDyxgrRxF741jBSlI_gU47B9uYUxXYoSeW2zRG_bB6KbCyLtADqJOqEFsDvD44UeU4s-660guNWZMwzUDLX7lemRuMTA0FBshIMYiFMYfPg8K_JIFNy8tjDMc5gWx_GZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIT1fTrPzu4C_PhQM5ozlU9oNZHkzbbUsD178TQLukRksm9ARnJ6Wngptn2IpJOOs4Rsm8gfwbzI0QCWIF5PG3H3a2dzxXNrKnIHFTsTc_oiXZVL43EwQDFySGul8__TwPgxqBhbo2ksc8XlSkTc6MNbLJAhW4HP6rgSf-o8LYqeK-1CJfmFlufxDsgXpbJxL_91c0LaTpdTBVUqwUldOCSetjP3TFNQSCj2RnbOE2CLpWa_5eW_32h0_-kqzcOF35BYKd3j7tfaM1nHElxeAh4VG17QFVw7Bey9o6HYF43jV95P5-XsQ0vdNKjkAQDp_BoYFV4WfqhUBiUzWq8htg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=QBPmLcMwIhVaY7HRXtnXm_ft2r49Z_aklSO41dLU0kIpUdH4lZ5QFkGwjaRpstlZ5h_awy4jU3d-JtqKqCM4Nj2I03rXc3MSR5wxxI5K3-2Ii-LDPN4DvY_WqLoBFYe3dwI5S4uq7SZGCFx2Bg0Nz28dmuLaKpgvO5bcR1Gii_h7MQEFEy3mAjILFbGf6Nwewt616SZafYcs97BllFJCbEpumaF_EMkbq4F3wl53eHTI3JHW-Bu44zYMWm6WJMiuHpLpyA2wPYvltv_2EHGV47wGq8iZgD9FnuTWtYH2pKkHccYiFeCxH2gOembDHhQ2aLK8E12xFqYsffWw_NpS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=QBPmLcMwIhVaY7HRXtnXm_ft2r49Z_aklSO41dLU0kIpUdH4lZ5QFkGwjaRpstlZ5h_awy4jU3d-JtqKqCM4Nj2I03rXc3MSR5wxxI5K3-2Ii-LDPN4DvY_WqLoBFYe3dwI5S4uq7SZGCFx2Bg0Nz28dmuLaKpgvO5bcR1Gii_h7MQEFEy3mAjILFbGf6Nwewt616SZafYcs97BllFJCbEpumaF_EMkbq4F3wl53eHTI3JHW-Bu44zYMWm6WJMiuHpLpyA2wPYvltv_2EHGV47wGq8iZgD9FnuTWtYH2pKkHccYiFeCxH2gOembDHhQ2aLK8E12xFqYsffWw_NpS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur1OfUBdn70HhtK5vDyYNONIbGvN9v67zx3ogAYV9i3AFjs4_y8O358j5ucieDLgmByhvRPK59j8onOUBztuQnIP11h_QhpYeUlqAZwp4CzCYQ_VUyECUaIxiVE1sDgQOyjNbvtp8hhToYtG_QU6RaYBVq_K0JLBuGVXkR-JVcwuwn2iMI1w5G7mO4dyhaMfjetBZ771dUyOfGnUv7Fn8ULra7UxsGITyJdVmhGtohQBhGGVLzHdBE1jlGenStg6aL7c5AZsHJuioiLNrXpmK_X287m1IwbkvtDKTFfn67sKty2X33__5Y9PeJ1jRHlL6Y-9dbU8ltQbp6jOTl_oNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhL-7w1TUQ_33jcbFyVaTyHSpO43OwVbkXaT16pg-m9LWn6KBKmgE_PVFlXTiawy8RZetw8W5DwysSWNdhuWzGvThaM8oyUm7Cbff4aDwOMm7jWqnNpkByOu6HDOWJBdaYvaMrpbvfCiVuPg2botEwBI_vUM3NX2DVgz_-U2LNXrGsRfyCAx4k1np8ai2ZCBjm1rQjYRVwEAirhEonOJ4xcQJorBqYrVSVm3gNDREFIgw6mRB_cS5N1Cn-qWsLkyyXxgMLgNlk6hXDTGsd99-jEI-Sx6DijnxulP0G-G_96RJXPQfPh03snrd0LY3W7KxZdH9vtrPj2TYOYgzb-euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3uSNg7L8uWofXmLPQTIWhn7Hl5KVvVUv6BjrrP4vdv74YopVYBmE7_OVjp67gpiyn9Feims7H2-oKIcAPLZNxpXoZVC5sPPo68XyKMVIf8vHtRSFnDqg_x2k64ylRVmd-pWiF6lQG9sUBhhdbOhV_imejhnvqmVu9zcHPqxdsRe8-RBvIRuNbw_OlNi3d0S9__Xp-K68bvB6gTdKgFPICZo-HZOJBBP3Gn0UnYCv7xozKizOJcOCx2DzzRtUfy4-j5ArhMxu0rjUxLqZRK4uxUlfSWqEPja7JaOcdQW359vykt-G6OuD8ZhRB4ALcRzcK2GYjc_k34uXVJDli4nYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6BQ2CTzMycdQfKgUqs1yGsHdzUAqXA6-VdS-F2QcJIfzKQL6M8kdjOf_oCJZydW3-zf9Bz5u4H32hAMhcGF1zpixw82gG6NHDfbuTzUbb3zHXLnUKUMHVPNNGk3swBVWtZuBBlsAUTRXyiFAplekbbiEeeH8YhkF-6m8Rrgj6Is1cMu2_FtSfPku78vJKWYLLDM88clSkJqyXjzFz9h4w61NV9gaHQj2WsIoYYG3Ic-P7btHnJpEW2d7YTJlxCV6F4_L7CKQr7001y0ErJ_FOPejCO-vj1UFzG0_tkmXWPJaXh_3CEidJoAPRPIdYGPf7wtm__CxbO15DvFE3IU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIHrhGH1pginezTNwD6O6DitAxlxUpWXaKBuAWsCNxgPPGeno17E4AdUFatZxq1gSEwhbQc79l6DX2PxccafKddqN2j4gW27vwzqJN54gPqthDp4j5A9fVdBMuXrPmZC0tDrFZbrqoQtULt1bf_0juWz7EvsVM_8aTcnijaT05yqO8dBYFLHCBnoua3nM6IKnTWNIA3-tLyPg8rgM_43vvLkeJDmfuPaaXnYuHymfh1FuuONm5lQutLEQCpXl9zyn16Kg_Qlh08b67ulxzvff5h2hWMnNwKVJrgMEhSL98FeJT9HZcPfV1TTZC_-0gIT5Mn81jS1P6WUVWVvKbCyug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUAiyg11op--ytOQghfGqaBnUXCmvMAXbCjlUGQGNKJcdaEyRVRJwf9bsqmDxItU3xiYgCx-J5gCmxpI3L4kJfaTTvyCFuzrTd7YHFTHnhI5i0cxT115r7DzZr7mo0R9YXSai4Z8Fbw9Jq8MTBVBgovmy_4xCbr24hqrBEtAgNPg6AQnK99f8t3Wsyyu6RJMFx3wSxv8UJa6x2-V5JjIPlRB3CkTMO3LJZ8e0ypzavpfy-_c7XaM2JpRzqEZYPYBVOutcFXZaMCKl3wcJiFY4ZQYjb8C7iutXoWm8WFjq70ZMOg_RHPtEPxxH38QsjeiyKr4UysljYXt_WFBbRvH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=YDCiPPh8RcBvFHKiteHA7PjpNUGczdROZxTYh6G9KltovGfyP1THDAEYhlfsgcyyeCAi-dXx6So_AXD9tRjEJo9DT1hOL-dDIAhczFOWqZYXjIwjKwvhQfSPpPymC-IzdSgI7RGdP7ib5BquHnHiDyiURinLtQS32RbJj4tbvUt51LViTuphMHlvapyukvRCNHJNMVZzMluGyl_Xn44XoyqV3EVUXg2hPXUx0Naw2xMyF-fqZlzXURiOr8U98Ow4B-DJCCqN2x6R4VzwZaX5itk3-UzOKCW9dMHxxOr4nf5bJSMP1bU6IaU0L3dyX7ZR6CARKZixyLco2-b57TRSxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=YDCiPPh8RcBvFHKiteHA7PjpNUGczdROZxTYh6G9KltovGfyP1THDAEYhlfsgcyyeCAi-dXx6So_AXD9tRjEJo9DT1hOL-dDIAhczFOWqZYXjIwjKwvhQfSPpPymC-IzdSgI7RGdP7ib5BquHnHiDyiURinLtQS32RbJj4tbvUt51LViTuphMHlvapyukvRCNHJNMVZzMluGyl_Xn44XoyqV3EVUXg2hPXUx0Naw2xMyF-fqZlzXURiOr8U98Ow4B-DJCCqN2x6R4VzwZaX5itk3-UzOKCW9dMHxxOr4nf5bJSMP1bU6IaU0L3dyX7ZR6CARKZixyLco2-b57TRSxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKbK4wD3Fh6Kbk9HtkoT4SJZK1-66q4VMZK3AdYbEPv7ufuqITZb3qISMVmBK6bas3xQ302_V02_0K27KKCtEHzBwhqAcByst1dQFywYsQCPRwa0mdGRzfGuP6WDRZVEzTVPADDENdLOOWq7qtXD2dadXsS0elkz-H5CNi__XFxVQilY-oOf5X-MyP_2Fpcg0KvsBabeB10zvZy1JvX4GIZPzqNKNwg1Kpw_cZ6_iKmzNWF3KBsDXBYZTcZyNFK8-EqkZPEdBnzH8Ej7FjOyMOyaEiF9njTzdmnKkxcV0qTlSDPQ4MDGQc2RM7m2cV5IZmQmdK7vhBfEGjpmZUZCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSuZ_MLKdZldb2qdw5pDQ6OZD0aoTz3aRfbRIUyUIZf5RJaUoAo27EmixI--QBSMWj7BkIHlvSiFyZaGQ_uzZVMVup0WSwqx8_b50a7YF4vFx13EHApTMRMSiD1wDd_PECKICvJD7Z9UX2EfIH2B9GNST2Ycdw270osXYEquwg-GQvnnSPoJXJ3rVOFXJgyYnnWZfKmpSF5qABMpTS0YA1XP3tE8dvZLVf2UgxqN-yZK3-abMT00iQfoEb_m4PV8ELn3B69PBfC0N34JLYd368zhQqe4y95ygzmg3WeeAlm9UbMYLvs1s6jUJ_AdRZpcFP72Su3UbQeltprzKxnZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZkCYgIYV8y3JYVt-Yuj0XQyWszcVRJcyigYZSf7mORjoP7GIgqMWkzAhcIkCdCJGZIvvBXpC5qh554APCVwserbybHv4l2DhQnroKl8m48BVQ9Hy7rLL01Lnm6gMvpgbnmGHQoAl9W_aNiZyrWmdP2ct8Y20C-LuHldYCRREBh9I6PMxmh6M6EU4fpJPk4ie66Yg6IexPQjBtq72rg6HPS_R6Fc5mByWoKv8ZvTHNMMKwH706YM-XoubZCR1zCvaKWETzUCq4Nb5JHlVy2oh_qzO6CO-d5rL2t3can1Ye43a6DKEdf7RWP5imHvbou9M_PEgp_cWaulIqDNR9grGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26331">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TudvMNuO2Ukk6PkXPQBUZno566PU96Cfb-SKAuWGQR2oo2vSsjXtVGYWXSxraDNJNdxwE2zBVm51RUYMETBccjSjJVMjyNRYZmqRzOlUbflg0p5gdADwJeKI7TEF6wQUOWGdxbGKfkNfc4QZgBl4UXLKR-I3vk8ZeL-CYLsu5BKPU5WDRei8vFaA3tmTYAveCGCf1wasr7ETIKKvCTuZtmkXkbqE4ImoIN_y4HOspjih7XF9f5cn5RnNg5vZ12cOQFyXBsOGe7DVvLz9qKhvh3F-0ZWw1NJhMIqSB3AE1HOHStSNSKnJD0FxYtIq6BsNYIKCvxbZ3zkspXjnNaECgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔊
با چرخ بخت وینرو ، برنده ی ایفون 17 پرومکس شو
🔊
💰
هر هفته شانس این رو داری که با چرخ بخت وینرو حتما برنده باشی جوایزی مثل گوشی آیفون 17 پرومکس ، جوایز نقدی و فری اسپین
✅
حداقل مبلغ شارژ برای دریافت شانس 10 میلیون تومان در هفته می باشد
🚨
ورود به چرخ بخت وینرو
🎲
با وینرو فرصت برنده بودن را تجربه کنید
💎
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr1
📩
@winro_io</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26331" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=GTG-m6WSFYF1ZkHvElVHwI1U_BCr_ij8uX6Y55cf7CRVpAow-h_HAAvPxQvl33g9t8444jpMImZ_jo_GTLBO87OTHy9O8Rlp8u1GmimMBFDwQ9X3m9BAHKuXj2W4tBtX3XRJIaNdiOJfSdFIL-6gp94geM5r0APfD_D7XCKdJYvoX9xrKjY-tVQNhR1W906EhvUdZg4Nw4Q5pB5WWHNZN1QiIrDtv7WS8Nk5I0kSW1mSOvb-XSVHM0odJ8_cDIpgsKiaAvtS0C2xONok8cvBlYU_QjV8YCVRh9tSVHirguGho67j0PLj2WVt6MRJ2ks_PL0aoa9zJMT3dyzlrP0SIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=GTG-m6WSFYF1ZkHvElVHwI1U_BCr_ij8uX6Y55cf7CRVpAow-h_HAAvPxQvl33g9t8444jpMImZ_jo_GTLBO87OTHy9O8Rlp8u1GmimMBFDwQ9X3m9BAHKuXj2W4tBtX3XRJIaNdiOJfSdFIL-6gp94geM5r0APfD_D7XCKdJYvoX9xrKjY-tVQNhR1W906EhvUdZg4Nw4Q5pB5WWHNZN1QiIrDtv7WS8Nk5I0kSW1mSOvb-XSVHM0odJ8_cDIpgsKiaAvtS0C2xONok8cvBlYU_QjV8YCVRh9tSVHirguGho67j0PLj2WVt6MRJ2ks_PL0aoa9zJMT3dyzlrP0SIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌مهدی‌قایدی درسال‌های اول حضورش دراستقلال: رحمتی و حسینی بشدت‌باهام بد رفتاری کردند. تو یه بازی درون تیمی به حسینی گل زد گفت دفعه آخرت باشه این کار رومیکنی‌ها! مهدی رحمتیم گفت این کار رو بامن‌بکنی شلوار رو از پات در میارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=hQCysF42MzC40VVV7iq9jHZlq2vzyW3ovgVqxXOXL56pGc7ZkHPiyRGhbx8dgMM4oNGi0QrR0tfhdZjfVmnNgZtK1OJBCupXYcL9Kf5TAkFLeABObwjMzq8esemUj-HJdNjI_x9XqUnCTtcwtSzWB-okkWUtfrt5lXvKtohDlwbKRD5CQkshP-ubIZVqBA0mfTqWOHv1UkUo-zR9CY9pMO3eIg0AXb-WqohpD1-xdKFDe4muM1UvoOpucKOjQRCr8GevZcCzF1lDozR2BIskbovHq7ZgXQTLc_ES-o-Qtu2Evua1dOCMHJZbX63SzEg2Wc_PUR3pXZlshnwlNWkVHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=hQCysF42MzC40VVV7iq9jHZlq2vzyW3ovgVqxXOXL56pGc7ZkHPiyRGhbx8dgMM4oNGi0QrR0tfhdZjfVmnNgZtK1OJBCupXYcL9Kf5TAkFLeABObwjMzq8esemUj-HJdNjI_x9XqUnCTtcwtSzWB-okkWUtfrt5lXvKtohDlwbKRD5CQkshP-ubIZVqBA0mfTqWOHv1UkUo-zR9CY9pMO3eIg0AXb-WqohpD1-xdKFDe4muM1UvoOpucKOjQRCr8GevZcCzF1lDozR2BIskbovHq7ZgXQTLc_ES-o-Qtu2Evua1dOCMHJZbX63SzEg2Wc_PUR3pXZlshnwlNWkVHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
بدل ایرانی مارک کوکوریا ستاره چپ پا تیم ملی اسپانیا و باشگاه رئال مادرید هم پیدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=an4E9pvysm53cr3UcYNkE_3NGZX_2QG8j4q5pRFtRdNQEsMg_AizomxPPK7XoucEM9msA6P1TvjUrfqRV-F1Cp810FLbH6Pq5nQ_8cwufwafiBApwG_FKq7RRrHm8nYRwJrs0-g3Q5oR1idp0UUybXQzWQpg3eK9vcdUIpZWIPwacsGm2uDGud9IPjiTaMWU4xbWX8bcd4xxnBfCqSIxnF1ZrCLm_8k3KRP2S_MGZU-i14Q2gftWZyso7VDWGS51HykVpg3J3Zo2TCZ9GtGdTvg2cacVdMT2b6_aDay_OeX7frt_WB8H8Y_ndqLMm0hZudXMn9DXcPuT-SQzYn3-ym8vZvh6SYiRcNrUEuVy4CQ15HHE9-_nTMFI4uuzH8feCzPUrRhSHnmyoSHv7bnBHOSpzyA1MOJVtzHG4w-JTo45Z3VHjGZ4wEt16Y-TsMluj6TKUiC9jHZxS92cUk4yKnZcWYq4TYf4gnjzmoYW8GfODAmu33R3UlZerJ0Gawesan9sUj8dpAdrKPPQ1rALWm3UFj31sazcOmpK19oL-FTp-fRnKU3xhLoBUcnZ9hAFbHviAD7vLeH4RwjwvYN4OPblWBCw2S2FXdXUUGFuSsSu7j78LPgB2Azl8joL0FJsAF5485duVCvg60U0bBrk6POqJPeZFHaOeO9qPEjqx8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=an4E9pvysm53cr3UcYNkE_3NGZX_2QG8j4q5pRFtRdNQEsMg_AizomxPPK7XoucEM9msA6P1TvjUrfqRV-F1Cp810FLbH6Pq5nQ_8cwufwafiBApwG_FKq7RRrHm8nYRwJrs0-g3Q5oR1idp0UUybXQzWQpg3eK9vcdUIpZWIPwacsGm2uDGud9IPjiTaMWU4xbWX8bcd4xxnBfCqSIxnF1ZrCLm_8k3KRP2S_MGZU-i14Q2gftWZyso7VDWGS51HykVpg3J3Zo2TCZ9GtGdTvg2cacVdMT2b6_aDay_OeX7frt_WB8H8Y_ndqLMm0hZudXMn9DXcPuT-SQzYn3-ym8vZvh6SYiRcNrUEuVy4CQ15HHE9-_nTMFI4uuzH8feCzPUrRhSHnmyoSHv7bnBHOSpzyA1MOJVtzHG4w-JTo45Z3VHjGZ4wEt16Y-TsMluj6TKUiC9jHZxS92cUk4yKnZcWYq4TYf4gnjzmoYW8GfODAmu33R3UlZerJ0Gawesan9sUj8dpAdrKPPQ1rALWm3UFj31sazcOmpK19oL-FTp-fRnKU3xhLoBUcnZ9hAFbHviAD7vLeH4RwjwvYN4OPblWBCw2S2FXdXUUGFuSsSu7j78LPgB2Azl8joL0FJsAF5485duVCvg60U0bBrk6POqJPeZFHaOeO9qPEjqx8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش مهدی قائدی به حرکات عجیب و غریب قلعه‌ نویی کنار زمین؛ خودش از خنده رود بر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=aSa1732_AQvJYhO3-RxfXYLOwpCr8qFGrXs_xaLuieYVf0FJi5EpE2yyi5bm_y87hvY7UXBBf7B1J4ImdyNzAWhIFkF-E7FcKH9r80sW5LgYqS4QtXeSVynVYxMe5O4xuMYBxTwsqslEOdZBJjlRmuNAm0Z3ejS_yOMpI33dazvTYILVDt0Wn3j32xDoACtkB72fTyXrEIS0sJnF4_LnHTrc_Kmr5mQ6X4UvsQKyOYYJ6TKnBbGxsirbso3jLxu2KK6CO484n1WG6gsRpLIlUOEQWVdWt85klSjChkaVy-DHxprcYHAfZEiHV-1N4NwdoI7YomRQgcVWqxLfVubmfIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=aSa1732_AQvJYhO3-RxfXYLOwpCr8qFGrXs_xaLuieYVf0FJi5EpE2yyi5bm_y87hvY7UXBBf7B1J4ImdyNzAWhIFkF-E7FcKH9r80sW5LgYqS4QtXeSVynVYxMe5O4xuMYBxTwsqslEOdZBJjlRmuNAm0Z3ejS_yOMpI33dazvTYILVDt0Wn3j32xDoACtkB72fTyXrEIS0sJnF4_LnHTrc_Kmr5mQ6X4UvsQKyOYYJ6TKnBbGxsirbso3jLxu2KK6CO484n1WG6gsRpLIlUOEQWVdWt85klSjChkaVy-DHxprcYHAfZEiHV-1N4NwdoI7YomRQgcVWqxLfVubmfIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9CZk-_2g9k1HULkdLxkHBEe6EM9yD1-OmnPVNbDg0N8y-N3KnEnjZNLgExkHyhD5ERTIYiTuPiodDd6pPugo6aNFdL8rWQqJ1n-kTxvJxn3Cd6zbi4fvNdUXzeFNJO97OKuOuQQBpqUxKA1eZ7gGaSNAW7C00m5LX14P9rLvl5n13HO64dehpAbKJCJsQf2C3dqqkYjsqIKxTeec3rw-UizKmgKNtX4lDzjZe93MOhGgbHjShlkVc8_t_4FZu1Peyee-Ky77f_9y4-hJ1bCBJ1sBJgxplqB28l5Kgd0u1SIWS56EnriB75v38o0nReVNVPKqpdAcejRooLuLo4TEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=LrPLbyCWSo_WG1g0Wc7oorwCKMzCq7_yfOm06v9tzZV3nXzEktgjuiCbaSTriFx7w2VctDPCHX96VFgknJN4y2C__WUZqzOhC0C_7AX9Vmf_tnIVu9a4lk8aC_VyaFwDgEqHo5cwMWwSQAX06nXBcBgUUiTEnUCBn47B7qXAH9H9-0dIz-KOXy6n8-_gXmRQiKkLfOVq5Y38pooualKRzG63zm4nQeFNuzDF4EVpViSpQdExeS0l_ncvV89mwJcDmt-niE89YXM7viDbkk4yjIwGrjlOmSoqu-4poZwR0kyTx4jTaKnc9oyTfYso0k_Xt8nUmoxHfPFkjDNUq6zjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=LrPLbyCWSo_WG1g0Wc7oorwCKMzCq7_yfOm06v9tzZV3nXzEktgjuiCbaSTriFx7w2VctDPCHX96VFgknJN4y2C__WUZqzOhC0C_7AX9Vmf_tnIVu9a4lk8aC_VyaFwDgEqHo5cwMWwSQAX06nXBcBgUUiTEnUCBn47B7qXAH9H9-0dIz-KOXy6n8-_gXmRQiKkLfOVq5Y38pooualKRzG63zm4nQeFNuzDF4EVpViSpQdExeS0l_ncvV89mwJcDmt-niE89YXM7viDbkk4yjIwGrjlOmSoqu-4poZwR0kyTx4jTaKnc9oyTfYso0k_Xt8nUmoxHfPFkjDNUq6zjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
تیم بارسلونا دربازی چهار آبان‌ماه با رئال مادرید با این کیت جدید به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=Hk6L81g45Ke0PYrfS8IlO9nJ-uqZV0iK8lm9yI8__i_mVRh4oZTEVpQNLhxyiIfW0apObnc3T1DkVCuhVW9pCo6K-tNOAoERQIqGp5DB00QhNuNRs_Jicyl4K50535CPttuWvoZUFS5JtMiM7KPxJ5B6YTbgkO_3qBGhhFQKDm5DPr-sKjHiY94ZhpwRZCpU-GY9E6FI-1JFMOLfwfMAkvSqQd52bBG8YL4NYLxv6ecW7lHG2FSLL6zyg_VVVx242AnQ9PAMh4DkBPpKNI89B-Uv1UuBo0C_pWENK6mVFQbOg6Pf_wgXsmSvA3mSZ3v0fZxaV9JHmQkpIyS_F7SzLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=Hk6L81g45Ke0PYrfS8IlO9nJ-uqZV0iK8lm9yI8__i_mVRh4oZTEVpQNLhxyiIfW0apObnc3T1DkVCuhVW9pCo6K-tNOAoERQIqGp5DB00QhNuNRs_Jicyl4K50535CPttuWvoZUFS5JtMiM7KPxJ5B6YTbgkO_3qBGhhFQKDm5DPr-sKjHiY94ZhpwRZCpU-GY9E6FI-1JFMOLfwfMAkvSqQd52bBG8YL4NYLxv6ecW7lHG2FSLL6zyg_VVVx242AnQ9PAMh4DkBPpKNI89B-Uv1UuBo0C_pWENK6mVFQbOg6Pf_wgXsmSvA3mSZ3v0fZxaV9JHmQkpIyS_F7SzLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vToRAS4xL2-z1E8N73q8AolZTwsn4Rp5Eh4r6fK7tIXxrMOv9vpu-D5vGcyISbEeZGbvZgRfM3ceu3uCohzXMD9EXOa6lMIGcWKqcNqCRhvggStBaSrcGqY6WL_aQfETrttwcakdWsVkzLHMvIpXGbzFJkBMza1w40-wDqBFFPCceYUnSvl8_4spgZ--2yEIXjI2NuvAlh7VBQDU25BQn8J8QBGRkh0y2lEXg6qcYTrRrVVcrE4ufTTJUaLO92xpt5_-rbrcKrqLQLrW0L7xx29g-AQcjT38ddobmpht7W8wa0BKiMKes7ulRl7OzP5p0t1pJQ1zcxI3sw2dXelkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=QVihHFGOs5cfprt4ZFDwaW_nBZUNkSnQyn2sR7Kjwl90K3lg_z6hCYZMCY5Ly_JTRv0CAADrRNCjyaiC4jKrkJYMLWCLFO0xP8U2iasKAaKREoGwJI6LqVuV4hFIOufhR5AaOgGZTMVEnlZmvllFpQINr9Vzq1bPEsnkkueOkIQO3CjWD5xV18fGHB0fX1ju_RHPXIo7vKj0oRCWQCTaVyfXaHD_jNP9_qRob8op98PnhbqFfCJ-Hzl8i7QudQGFoTgi5tyHCc3_mv6N-Mg_Avvs2LDmh_QkgHXCvZk8LEFx38yGXZmab_iEZe-UdKqVHqHBIv5AISJZPBlqX4XzSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=QVihHFGOs5cfprt4ZFDwaW_nBZUNkSnQyn2sR7Kjwl90K3lg_z6hCYZMCY5Ly_JTRv0CAADrRNCjyaiC4jKrkJYMLWCLFO0xP8U2iasKAaKREoGwJI6LqVuV4hFIOufhR5AaOgGZTMVEnlZmvllFpQINr9Vzq1bPEsnkkueOkIQO3CjWD5xV18fGHB0fX1ju_RHPXIo7vKj0oRCWQCTaVyfXaHD_jNP9_qRob8op98PnhbqFfCJ-Hzl8i7QudQGFoTgi5tyHCc3_mv6N-Mg_Avvs2LDmh_QkgHXCvZk8LEFx38yGXZmab_iEZe-UdKqVHqHBIv5AISJZPBlqX4XzSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6LVrJa8oqsRMUaj6SGQhETyXe63e7QE3Eb8aPlNk3XGM15CpBChX4mESjOt1wxRZD58K2h6DuJDORNEVRMYvtow7lsmBIsFx5hwDwOyHvkxsrXdCHMfgG70UIo-qF7bqd2gHISK9RDH1uVPnazuT07DZ-n9uaDR6s_ypn7HrpxjM7mhw1JOF51MOKQryIEC_EzQracKDmiHi0Zm_R1WwpUAO5gCu3sjDaH8V--tU_K4eELrY0aosnF2RatDzSEiIqp_gx7hGoz0xg8r4vnZ56mDYGXb0qX2-nYBr8WW-yOWjM3b9I-VVvD94wYwV-boyxCArJLBSa4gkvZ1K0q_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLHsKfCiEvsr4ZnUAKJeCAT3yPiop0TtXZQnKh6FRcJUAarsO84ag-NK2Cxu9t4rc1L09EhKPdSGjLqNzHHlSFZGN46A3aBAlK-E8jBhR4vaVO2Dkn-Xm-5K5XlNirERk6nyKMN20nMmUaZOUm5KRncVK4As5wennQU6f_rPFqr1yT3wjQmuS-MJon4bpHF9t4pW0LprGcel2CAjNStQc7-zS80KSWMfY_Fq3qy3JMOzDqYas605NnhVvABzrGQGpNDkZuWcPNLIFtstZXMjkqCfU3KsOT_dvxirvbte_L2c9-24QpvEn-MVUQ7rplqaXM_iGADUGXxtpOHWpp8RmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctDaKSaRR1NPvfc8vNLmnZTGAm-0B4skPwxCy9da0hhwhEgKMgo8mJnlga0IVgmInsrq0Aq4MfIr_xYCj1GSl6tgXrBtPKVXjjdWEa_9aWJj5m0abUfTwje05uu5_4CzJm9qfYVGu0PQhc_S6eytESmAc9HrYxnQ_lXr-Y5MPgi8ogFtAPrE0DbXs8SFdQynvOaHlWR17WphB7TOVqIIyxH12Ww5pdz7kviVjO4uLcalEsQpMNSqSz_EpKI60rJGgNT6S-MrHgURblUdKG2AiyeIF0LuhyxvoHsqiSHPFyuFw8gzIfotkOMZnBeTRgPS3xZZLsm23NrxGYRDoi_CRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC0DSFxvu_m52OB51NUlsAswbhr2CVugYffzTaXjfIyhcvWV0NctgdYKN24l7e4TyFQKe1GHZyVYWIKOeWID3IYWajQrkzM_U3kY0x4YLZLTpq8IvJUmh997lLLyQTQy7vdukanQLySIoQ8GI409u7QCGE_qEsyMfzgMk1NPT04BNIxfDo9dPCYG10L46Y_0uXylW_i7VArnQq4U7x-KsD-6tUGCLAaBk4S3DG_v5rUEF1-PTsxN3kDHiydwUyI2eO1-zgIXpBWWWc7bNCwkkHSSq8lesTYzVxY9Y1rinhw6rODYSKbzJCsq4k-L0NvjdEW8ac_QncuqZLA1KGofTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbVOCz234UnVd5CYJ3y-h3GXK9A-0FECTciyhHv6fYrV7TvQnAH3SHYt5eZ3QIxzhaTdAzg4siPMUgqXc1J4yWSrtOe46YMaosEBSmVFpncjbQ4zYMsewGO9tUP4PoB0XI-tvTV-JjaL0pSh9KEjpSRwfe51O0X7AHbgv32CdFUwiOVeYkinGv0PSq1icS3JJ77KtkY2xI_eZZzY4tNDFiaKbErJ2qQgr6AF-VJiEo7WmX5PKd67gsoz76mjfFAPUg-hi6j1XqMDkBshMXCKInppa5wFjZGW5yjQGAkmC9gvRoFGUDa1fk6GyfFVRsPHX4hZtTTXXzw98u2553B_Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttmz8zzu94R7IxgSoc_ZkwW_MzJhagi8GPZR81uWRJm2-iEFy4D-7TPwT0A2p66_2nUjqVaKSrBXfuh1Aolow5MyMO8Gk8Of_AV5XSEG49igHCiiwkdTDy0C2y7W0TOSvV7-cUQzF4aVzjqmmZOhmG4q7JZC8KS8X7YZIlSNUra9WPQVGCsGZs_9s7ERNXfMg8OmZHFwJUbL12L6JvlCWxoxEfsBd5N86104y7ieY3lvi8IIMViKFc9dPE65AWCXFiIWIur2EEEuCCRkVHUhUjxoADHaDEeE9l63Sw7gAfxtBw6IrY502-VHrcu_Gjp01LT9ozBKxHLiRb1K1X1n-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVmLIdQhEheURK-ZOOrMf_qo0qbIsU8hhPK3MCBHaMkWXHpGHzudCxQUdIlKY6HVU6BJU2hk6ZAxxqvDjWSsSGU0H7wnmqdHa8UvWVW0BUgWOn9zePfy-8t61t_0nofJ8awc8T-mJ_9I-04bA4AQStFfY5QMDSUMHGNFh1_UYvhLtmuxvzkuQqii0iFZ27Kn24nw31xoEQivd1i6EQHNyDljlDFagb-SkqEX9nlb3_0zfWTERH06O30Ud5o--1Y9AmyckWkZQUbBY5fnl0aq73tOm_E90512o8VPB6ZOoVyhqOd03jXp9xaxHlWmqh-7LT7Kne7HOOqbVInXNieaow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncqLODV85oxQGFTBbLuGQHtzXA0dzJ0J9vpu0jZyicCxMr3NuybtzXl4cz90gozTZqTMnVpWKR8e4JKgtoHUo3XJ_1DGVDz8kaJsNKsjIzHQSbFTK3u6jSJ5yk9BF29zPOruUgdLMCpxWOVZOUL2BqKBsQ2ZzxyzJhUlqMU88qMAClcrVMpc1BT3etV_FuxAgzpvfaFFdn0on-Mk-P8b_bb2jZ1G3ZicPLZ6c3Olqjksx2lzC4YRC5VHdN83S3f_vK7egak8yKxW2rMXC_8dsQa5SpUi2tSnwhUbFmgwBt8oZgLLI82ViwJYnumvNcA-kVqaB8tlvn9dnZ6oIrjpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L16Td9NyxDySRut8HAJ9Q7ovs4DHp1BLeCYbcasm_lCtau6nKdRbmhHNUkvsQ2rh9kBXXOI3g79kPf0QpXkZqVd0dbmO4Mk76l1KxRZO7UNDnAsHC4T5JHjddnQbeeD9KHYfT50VtrhEx3JJ420S2AJWk_9mBYmbvzCzuBf_sZV0Sra0Q6tFvH-_PIWR5HAlIWA6TTWM50ZPtHuR--_jWaSkfgxiAkRHOVoxuYP56xsbN79h-iRuXSaVURWRFIYuICbyphbRLXQIygRDcnxuR0AO-EkRJQG-EwPqKjyRaU_JZ_oDL-Q87dFzhi1ZVLgAUQXWUoSyGCmiMJgxb0kzSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtB3WhqVsf6keXVXK4VOIVyzHHcWeSIWCBMciihpmkt5aBHrz-syJYfMybmiG5pTEhvtPzvVdmyrL8_Cv0iCHv__9TFKv6gAkb9ZzdXnsGB-RsOqw4uQCK83GBVZn3DNX-L5_kBWaURio8y32ytgnXrobONmTkP57zy362YA6ZW9aad399cZWQNnE1tdOAlGQgfyzz8H0sOEmsNDZfesdf14CI1GgXTGjCKj11WjYpaZjDvs0gloBzVACRHR9Wu6PpjYspv6n_b1tXBGxTjiSHCH84jKNQPYN5D-Kka01zWdIr9KlEDJoFdaat9EGHNiqDjLE4NeY1XSrR9e4d8JSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTfd3ja1aU22udiOPJpeqiHpfHYCFpjFmTGBvcPEGpoFyqq8p9_l8bPCF038p_KlLYCVq2lmYIK_1_WlD7LiR5XQb-V8xyWoY1bN6ZbQ0xXBShD2eXlVxaOlZIZXanqg7IBnudqNOElDpbqr4eVeHlhU0T89i1pprpVBmjWvE0mzPZS17sGnv-DjeRfoQj0ufdUbp17JId20UPZ01rAnzm7qL_xY4MBclzEXURx1axy28iaxKPCKYJmx16CAaUOzeO76cs9NbKFv7p37noZpXedC0VtbrkVsFlAc5SUvktgE0pyB5xMtalMdavspkr58F73Aduf7Zt5WJR2qCMImpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abKBTEMCSzRIEi2fpeXXipDCQwaPsvWcvAYwRgrDu6gUZFF7phS6mtWWT5JrXR4WtbquNSaw2zhTMJzrV66UW_kwkDWl4Pie8jfWr83toIaHjDpHHgXUIx6yU_HbjHFXqTK_yaYtOBwPMi8uZnkjdHLq6Jq04rGmacf11cXVigbBFoFLR9YVMKlo3EG1-ek2U1jFxWvi6P9hHiXJ91mXkSSqKZZ9lFdCUiSbAB6Q59mA0RjDeT-Hc6t1XnvLybrHcLCFX8xlF0aPnepX26LNMMzArvcUucY9xqdHD-fM3RzWDt8dSxSqNdk7nHQElEnTBWOY_4Tqme4zzZBdcwQzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=SB6zPDmb5ih9o5oXutRfJuTdQCEnohneMNeGZe3Ejt8qP-0RKcw-ukUxXUC9VqJyz8tEJOdDIEQuRtcd18zoe4UAAU05w59b8SHcG6xEy5SpQH6GFxKIQxEJbGcR7TZt-8iVZ40QF7pKIvbLeIXpIknA4lQgdb_wHwk4SVwRnogOgHdr2Z1wl5YB4v26ZpRPeMKPSlh7ly7JdZ-WlnMyhXM82RW7UdzZLYlELrTakBFaydBvAFwN2xSFCuCJ58HIGRZM7Sit4x_vJTNRV5TUaPXZpt1xaJijuCCSgZOcJiETOf_05wkm1zXndD6EFTjZ8_aFRAPACEmZIpq9ejt4oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=SB6zPDmb5ih9o5oXutRfJuTdQCEnohneMNeGZe3Ejt8qP-0RKcw-ukUxXUC9VqJyz8tEJOdDIEQuRtcd18zoe4UAAU05w59b8SHcG6xEy5SpQH6GFxKIQxEJbGcR7TZt-8iVZ40QF7pKIvbLeIXpIknA4lQgdb_wHwk4SVwRnogOgHdr2Z1wl5YB4v26ZpRPeMKPSlh7ly7JdZ-WlnMyhXM82RW7UdzZLYlELrTakBFaydBvAFwN2xSFCuCJ58HIGRZM7Sit4x_vJTNRV5TUaPXZpt1xaJijuCCSgZOcJiETOf_05wkm1zXndD6EFTjZ8_aFRAPACEmZIpq9ejt4oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=PSSekFrPhlZwlkuiC_8eLozqCjXBxLbNvnZbJNbcVyLLJMIPwt1PuPUAUYaIjZ3uGaQtjwy_ST1ER7l1SVBoczTjIG0hHUNihE9Oadhb_PMFG4NUCyI7Gx6Jted5NAoLuiX9rQDcswGWSa9Kt444HAltUkqKtFaifzMs4QTc5SVmfWGyBH5BI3CC7gdviAk_Eeyzm-Hcd4aYA38sG3Hc9CihfD3DjrYMt9Y47qs8HMcSVY3C0vgjApnWbkOpJ7cQOjBsfCYwZviJ5E1JAU42358L_48sVjErD7JQcVmxiCBDsG_6FFoxWx6dsNsAZKmkdDglnt5lXPVnMvaqhMW7SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=PSSekFrPhlZwlkuiC_8eLozqCjXBxLbNvnZbJNbcVyLLJMIPwt1PuPUAUYaIjZ3uGaQtjwy_ST1ER7l1SVBoczTjIG0hHUNihE9Oadhb_PMFG4NUCyI7Gx6Jted5NAoLuiX9rQDcswGWSa9Kt444HAltUkqKtFaifzMs4QTc5SVmfWGyBH5BI3CC7gdviAk_Eeyzm-Hcd4aYA38sG3Hc9CihfD3DjrYMt9Y47qs8HMcSVY3C0vgjApnWbkOpJ7cQOjBsfCYwZviJ5E1JAU42358L_48sVjErD7JQcVmxiCBDsG_6FFoxWx6dsNsAZKmkdDglnt5lXPVnMvaqhMW7SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3f49A3vZBiSEq3HEcsKqhSEzPEgkwkXgUumKOJ9bgD1sf0BZ3eieePSdltBLUJQ56dsRuduLuLL8UfuU-AxY2bT1cw_dr4V41DJoET_338dZ5R9ic43UgJ9IVsEwHbPKKHfiK6h-yfuqTQJbSOfuJzzE3lFjfrrXBdsnea1IFfDVFAbtn8Xzi2G370FKo79ADdRablbS94SGuEaoctBpoxif06WDzEIc3dUHLP7S89a_Ze1LnxPXcHIVNnPGwsY1hboA7AtVGrKba0wG-m4bXmbS8rKLy-eHTr2oVudXbwR1IljAy__R-96y_1cfdqZuG7QEoGSlAVcUA-lmo30xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8jJU1NKzSH8FHEKSsjVSh976ojMzad9-tVhBN7zkkvuV7jKwLFQIBruFk3WedRdpSraSB5BoAzrfV4_xBa14uKZq2OQNb3ERiSnL7yBITDD6cNsBe9qPf5w-KawSDaOVnoQ359AgVXagJ0GbuFl1pvtvUa5jv4iY3Q223YGg1OSu6QM4n0UNqnvdyOBIkv5WohdUEL_UDh0j6yLP6RzX6ZuoR9D_mwUvew_XnWv7OkO_PzIsZl7-iNvpiOvR-gkFuQo_0o_T3GwzvvuYJC06FMIAo0N6RfRpfny7sh0VeJhN01eHtjWuJsVqaMnnAHoZxFPfOoAbwk4ufVaQcHw_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGOC__TJzXohw4soXNV749wkzIixgW277dvnHf2zj6IvIHk8rkBjtw357hTBx2PcqqeRqFQHfnjw-VdPa9XVwqKc0cnctGzUJjSev6WRPP4XxUcp5Ct8SdpSLmFZIOfdZaJCNEbCVTQhpn-yul0d_3Bxm7RO85_muqHRcpK3dBYNWsxX7h5E0LbUq7D04nisqJ4cTofAGfYH5alToV0G5ZJs_3rAGliCs_TtEp_lj74nM6XOT66NbSJIINSHkHGyYBCiFDwZ7QAyDgKY7U3t3yfBU4CBl7bDQWbYN93y5sLvvasEMnDBlvIFzlxvrbHke60qNct6XXOIhy4oCXXTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAm87nV_YHzK0CyLdMR4ZpRAEPFsW1J8Tqu0IGCvyNFrRNzzykENPuNBcj92l6XTuGSSrhG_GwUOq9LGaO0Bq2BC_AUFNwhisEDFgZtYLY_eT8Hxw9SCAf3-W4KMVsdG62bZjxrVHM-fsrYEBSx37xrj6jcEag7VufD0K12ve-K0eOANkSpYbnzRgLuwvhf-kDJMp1ycFirTh8uyhsROZRdpdh49JeMtLPl7OWjWsD0m3f7mMYBcwgDLZIUHtOGHLw3tzNHrGz9Yb-8PdFA78mE0XMoofxqwGpNASNM_YgDStz5XnMRv1urgenp0uatPd4nYlPv-8aj6yiLlHqjpCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqvIdJ1_Og5Ad-Sgw7B0u5uAK8R4CgW6PFTWwwLOOiN9jrBd08PwzIxFbXnaJU-UOO4K6IItnfozHyE7Gh2wWrKc0PmSXvZ5cMU6YdzPcyUhalbuaUNkG0PRw8lJMeXC-URASTdAEbhx9bEjFP8DBFKJ23QK0_80GhSFtCK3ZYh0PVu9SR0RaHbPlWwJwzl3pXihpTEaWTIAG6DV6Bst2gLJl4fykmCSg6P-X5yx93T95S5CRAw1c_r4I_Hjn_Uhnw04vZ9lvPb3gUIGKKAfDpev3xKfGnGaREcpdC5JgEmD-l0ngthg4v9g_rWPbmHNEi-hvWbeZmR6DHDKgFHtow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooS-WkieKlNji_PHfvNLOQyHN3-6MY2KeNTpALEDtsRHk7ob6j9ODWqIyA4dRVcBeI6_vGDaQOd2VLUb_ypi7n8Cpg9rDPUlES50GXDdhuf4p-6v4i5NduU4IecT2wBzYPUKER1G87IbgCUky4qBowUlUtJG0cAY_42CkmYw6zQVLGoyZWoSLjybvEQEPTkfPIvkXrVMkMeAHQDsXppjwQLf55xqUJ5sBnHxfwzBUGAvkAgvZt_a_f1ACUIc2hSX6OUAR3gEdcBipOwyl-X5HA3qLA5hxkqVL4pxSksGvQ-7CyH-sY3CZgJHVqKOuRpUeP46hdpN1wqEepmqprsUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWcCIefZQx-FJw-wq5XocFo62-32zSnFxpKWuW8g29ye-dFu21jOmLHed2NXtoP3mq_vDV9Pz-SvSiH9NUqV_dEoMWJ2mYfn7YUs0dYGFF53QNr7_TFWBx--NMTol3JzGWiai4hMiLPQMiQLnqq4ghGXry4-L_BRQdZMtF8pPAlsfhHBfFjUx266jLU8DmD0K9tgzZfxYSxZn5M39jDZZJcVSEOML6PPuQLAXJOiKmMuKWAzmvekyTyhLFYObLxxO80XJppTYOXy360K-cUlpRe0Tr3lquao1PH48WmJwR9fvV0KODFtK11jc6bkoG-o0TVhgqZKSdkZSx3gbE6btw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV1n3AOA7wyuhdhC_V_rK_QpioIPLce906BmEXJb0o6QT0RCRSke3RymtGZ_pXPlEx70hlJcqC-vVIj4bwH96YJcJDcObsCqK3Sr9Hb2ovuxLUXXnmADqwMPlG75m_DBGdDjxDcSXJxP03vRQkwpsijcR5NeUObqVzFgtUrityJvhI-aqS6EL_mDPnUV1nCuYjGN9HNTv6XtCnZ7YvnIL-pEZDS3KiZTO0Ua-dA5AU8PAp4K8UIQqEUKkEPtxm4L_m_CrNg_0HWDV0qFNtsa81hW3JBJcpS6ICCIp3YEcvURKV4OMg82zZ7n3fTbY41rjS55VvCEjoVV-JoOpmsXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSwVr4xM-w6i1pO_Jcl1hyYUenxP6LqKLj8aASLIMJ1nof-AGlJDeSEccUwydGUQouAzvhbzt_yLNoxffPMK2tfqSiCY5aAafMqI-72KagPCKKUEcxXZDe-EkG-IiEXGTvMTU4V_oWK6iW11C32gP-em1meTlf48V08bKzizOah_nhKelng9yONBqFVjMr2juHhS8jtJIqnYl1YAV8Iautm83OCcz5D8jcZHVS0NUgItuZ6UeU5BEBc2Do2A5hauOOs9ZLC8mDSIQua8K0CXsBH4VZZtHjCWpzDvuCWQ6GpydU44t8BGPG8kaUWNGsc9UR0urNAuR9ZZ-GKepG4r0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVy8YvqGcmij4lTnlEqis3St4ajOg35Culc72SyAoPNCe_BIX5AJ1rTHTxWGNglrjC6ELl1ru98YWtPIFYpEjsKDDWRa17t3vI5QbIjP7p7gcryiW6Pymgn4uGfxJr-owEaZVhSZDf9poGOoWdUWuUx_3Z_o0Neg3zbh04E12x9_XKYoxfbBCfrz-BHL6OWxZAblpQIVyPbE7X3A-0N7QXM5WO_gW2KVkUwudTjHBH8iw--kv4qUM7tBuO_1j6ut6cyTzbuG2iokK9IBmbP7FuLPjFyd98bRcPJd369WIPIOfX3TcDkzElZjgO361Y0VQ_4529c1ulwM5ukJ3vWvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDSzJ-n2vu6aI__kRZDDqJ2KFwb5whUN57UC1spXvibT_0mh-8PDXv5cTE-j7c1PXmc4sv5cWMYlLXSMo5Z9Uw8UXNnk0aa-maS9WJyv4K5onpjPQNJuq1pe8KJtnHCLOXLkpddeESpU6aG6lSaY8o1NE6KbJZ-c97lM0BKpcE2bAwZ8PrLpndeiOo3CKTHE7BujAtJh4524hnRptjrhgf98rTfYYym1N0YUAgFWbenBmN4iPBs9Bo537MJN7M8u4aiCAEw1gNMc90U3tC_ZBL8desGtHi7moESxU93vCHCuPUDKzSHGrihO1tKNI1cXtotJ0DqFVZzrqhjFCitfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ2rt_zzBOdLQN8X-IbKLJY8N1nS51ZunW1mfQcRp0qBSTrunBIzgXQ3ywCewHe0gSSxaDJm9OVgHHDsDhqb9qtQcO_qTwIt19C75HCEkb5Bms9oOHh5GK3jCyA4FO7jdajCe7CwabIxHB4s0K3_Vh73pnZ0jgabp1YjfXoRF7Ss6tAVBJYclJq3kMch5KJwsTgvr3SC1_6by1EqR8mozQYPnwffNKax1VbEM74ML7MIXA2pnEMxjQp55IXrIUKAi5gguC1W_Xq62Xge7_wyNOs8Gw4Q-mVG1bAZHmeQYc4IUAx9HvAUvOJZ6y1W0WKb2_bVFVLJ8E7QJebtjIgsXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGZJ37lTte8N_uWSyQG9y0JoK2F0OrU8Ona-eTs7LDccD6PClsDkmqbKwsGu4WjDId6rAvpLbgXW5SsKthALfyOKcMxrMnABKfHxve763kQHl9xAnFufOMZYXoGqR2J_AXUasuGIAMP8leEaGlWbpJnKt6VbdPNc6zb5-r-TXHOUG5rwsMp275mLHyXgT0PN2lxRwxoQ_65MZWp1u8NH4GgJmJlVTrbv7fz56xC0n-H1Mj8NxgDdi3BATfh00-LKUerisV_9ztaJrjQ55gi9HspnikA0zSvB51irbSY4kRrQ-j5WmX1jF08qQeUtWbSCIN3Amu4DYPXJ_X1uJQKeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZbNYrHjDzNqPlTm7B3YHC5Fk_Y9zjax73F2DOq6zJR19sR7noT26VOyUtuOVNWYlDJHWX_HdDDixplFVU2iV7QOw-sUAshPappQ-AegK6VeC7SmVwp1Gkjb-Kx__WHucYM78sc2vAlJO8c_lWTbQeGw12KQz0vYpYFM1qjVlwYNUESpPLAcbfP5bCCokyAf1oYjLNFeMd3hC11sHKk-F0sWXKvaWgWYYO3z5BYC2GqO2PtZmyiC4DI2lWU0vmVLB-rkyOeSqa_On7wwMDA7QIhAkTXv_5xIJaDfLUw2fdpyS-cNz6Gj8plqbs4lp30w9TTHtgcXIRcjTZ_XhXW-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dBnTxXcXwVaM70dMH5iN4jSxKbT-CBrpGTOdv9jmOlRCdKnGVEOjiiUasPVnmVmNP38fI4uOsOjDOUyHOB7QlTsaOupcXuN0xjdS-3ktITQDIkdsaRilaxsmnPlYhfvgo2DzAkNE5uRDY2WLvY38QhV_gob9-9lSbU41AlT9JFGX_otWTU8X9Kcy-Rpy7JTxA1V8LXziXU588JNTk2Y124cuSF5qo3zQuuaMOoReDwENmo_cOGpiggONwLcwsRcYg8W_jKLEZLyfzYE0-ZAT_axkuU8rV5tR3q6A0FVrTNlzHc6lc5flPh6-BLXalvaPjlIgjj10Wqnf61aLi3Vj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0mgPYvRinZA63QGnWyd1VIaKhEsTDygxHCP3ohOhA85ZZQ8DJ2tmwrW5tRU8-6e8ieR5zwjG_AWlc20kcqm5YFQI753lxAHYUGxyXaoiZJa9VX0sFOSv_wKVukGZnU690PlJHWWsfeIciF9mbP8P-xAl_D3FbuZhNZTVyRCA4ZJMARvpi-PNeiKr0QaUDoLDBj3o3gpK88FMmJUJQ-KaLiDk08yUzW0rl67zoNagaBwNShDNViHhlAHwaZSQ5381c4Rx1FApT44BJa0Pa9WAQS41BDLX4MsgOwlYykFh-3-IFtwhFeuTWMsOrAMBkUbpdNbPRC6AsUBn2ChaKoNPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh5g956D2bttDDy52pH8Tvg6wsu8J0CWAOZPnDag8WZOriRS_RplZOaqfVWcaJvbnIHEaVfkXpsLCVaylCdnQ_KLu_rN3ZlpmX0RBNrbr6ff1OSV9zi8onfPOSk2C3UBAQBo1ioYiwBciVXQHWIN2KwqnAeM2AR2TqybSriGwjdKHsR1i5u_KDUwVnZEfGdultDqi3YtSTTxGpPJzaBf7MDEiMaPdkYmfK8Cl_hA9n5-igzyetvwOMbLL-iJYwiAYls3sUKmfxMXnJ1C2oY9XtQy1fH77rXtcw6TAgzzEUTXiZJLWTyyhR6don4I9Ywc0GeT6zLgLYPG2_Vt4ofgXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXB8SypnwLLQcVs_iyPMVpFiXv_8aNihrf-8cuEI3kPZHiuDp9NHh8-aAfcPIuRX21JTo-BeZ3NRjhBLeyG-eWzoqUAoIavNyB05tm5mxm-o2L99FREuxU9GKVKXfQUk5ub2XNFUNeA3nplGnu_F2SOixRCPglh7ioiRHH52JvG6gqti2anr4jy6weq6ov2hGzQKkAgR6_M8sYBq2WNvjTE8jPF96PNYFlDeSIPKBUQZmYRjZsbpB-Gj7khLBFxRBKCV9iVPnwV43tX99Y-cfg8CAdyfZe0iwdzbi0eVvt52PHPY9548IFgYRpLPk6w9Xcx8ewCYu3I7gkBywSRoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGf_GzSuQD4-kucTCttkzdT9cgBqamlUJYp0COFs_lJTtgIGV3nG0qopp0GgvJ1g6cIx9sVlqj9X3D5PgGE37bhOEBoU9pAu0EsWHhIuFusw0oMn74wYzhbvs07MGlq3drRxHIsRX9SkHnMUa2fZeoXWOGe-FPFC-9DeK5ZUd1E2p7MZIlfSCF2p3t_iumwc5pksBorTy801GrWkRLoz9Ifa0dtWHyYMlj0cnVLWKKT1w0vpIyXLVj89hKre5pKFog5bEp_HURt3Qz5IJ1IGn_1_B6Lvhar1iz6WlOsflM2mEFDDtkQ8EaxdXnex7eQfVoUdgQcPgwv98Q-fUF4-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_b7B4x191kvOn7g3vglBDP1ThE6MAr_gkBzO28I9DkqS_6wOU_0bjGX9qEbYGezrmQzBx-PRuB-wDHZJP-QKyRwLEJEu7ApvZotNiT1-LsVemG7uazICCPJfALriRVNAY2H4Wz4PT_Swe5dE-QD3BlbwpOVCX6t59Y8SRK4yKuTk4X99lCRRyl4lxDxlTl2aLnW4Z4ToCOdip89VPbqJtWwL899p3sTHmD74_lL273OnPOW6t3KvE14pvizPWEZX6bUK2SpykpJr3iOikDjMM9OTd2jjAsw2mv1gWM86BlrlpT-p8gTlPWHzSVqWLs6O5LynJJCJkGnCnS6J4KDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilpz2mgUd58zbS_SLRJ8KuuTUzSjAzFL40u1mvjvzt-RzR3SVaxEjqctYrRvj2xoZT8yAY6cfWYI2GaaDetqqBPhNvL-3aSODt8Fp9_2Gg_PsY08G0GyN55w5RDtz_R4KOdVpWUu4mmXm4H3qfn_Ou9Dmyt6dx8zeb67VUpM-TZsocUm8dJV2A4o-_06i84xBs93zYEEUjc4XJnPIF-6LNacieKsGVI9J4_X8kN4PLrnEI2zad0idB3CX8600IE446a4Z5wygQmcECd3-3Xa2Q78foYLe_8zBzjGI_ZLfKY0ch2eg_Ajh041hpJ0dt0XDh4mD35lEPEa9qUsRtR_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_VyTjug0zAs_EMhMUhirIM4Exu_AHXQVWUuf2Y_7CoOTg-TAjTRWjVirPX5Eup2_IBiy_duSX_bxTT1KVixiueDMWbgu0vvR_CF_7Uy-9A0pVO79n6NcrrqI0zcYhJIrkLiNHsLc-SSZ2eUUNIhviX7bZctO9vrJ0aj57kNQGtU6Si758g69-tPyIXJ08OG5ql9PzJY7gaiflC8LPTZXgd6p6TgH2ZuimIdw3Iw_1yUOzPjqFB3VIjzwmhbviiSilTVrS_cbxvqQMxTUc-z2ebnVDegq5dT0vV-rGt3gkxOJFJs0xYhv84UImyWk4JvkHwFn8TVW6q9fR2KN6Wz6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOzRMMjkV7fiD1Qz2LSz9nUvYjkkNtK225Ul6fo0k1cUnCHKmINnJy_RN3cE_NupG9Flgtjy9fJCvoNwqThnG96NZ9V0-7Glp-TqCZrDEwVAoRsPZOu2Ur497_IFxn7cszUiLOFBYS9dbE3D4XSYx8_0vktXzZgRIcds8TWxnOoemi0_AQLlCbD5qSiHd4LEmvcKB2KSzDSiDGN6d_iCdHki__kf4hIWxgy2A-3vu1qo4oV_e-12B35n96jSsm7BS2FuEXP9u3XNL2WXfXLHbuBsVXVZjSkW0W4wc7SKQMtZRoit4Nxwjd2WJ50apzto8-yCGOldCX8izKfAKeYujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI9mkdeaY9KZlhlPHkIkLFkNAdu4BCIAeKNRaIX7mqfq8-OIzOjGrycGoHvOJ08cnSzqMSbELwx7s3RuB9z_67yaVmNjc62DMoGysCp4we7RVVfU1eMNrLYo3VcKgrgILyBGpk8dKNtVH4idbvFjtsNK1CNt25UADpCk-k_DhUZ9eW3CjF2-svOhxZbxds0UW1CIAmUKzjPofir8LGHBCjsjSJHEovMBwGXEDqH3v90EBeLalSgZxHUd033dD9M0m9jkN8zbxY78Fn-TL6ZtfkbFoteBXXIcj4-vP19ragKbbkH_IBwyhRzkg1eNfiqPNKgIvHPPF9k-pwFIIJmDKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUmOl63-Uws_PHw6FqzHByyXMpCqM7OP13HuyT2FAygMp70MD-NqRK145L5F9SjlWpKf982BNDaExkv38dV6g0u8RMcZOSAPfD4r1JNGXqc0jFTz9cIMm7hWjm-l4aNsRN_CifBS_sEQ4r_RuD1hzi_nB6vAEYES6JtmsL3KzTB7qTZqScFRSxigZSkJOp4zS9X2QyIquQ-mCHt773YZ0yPpVyJqN5I6lkTFZPr-Sh3noTADpHdxhV-Z_RGTVFvTI7_C5NI6oi2OcdmfcopCz0rzy0BFUswGq_ggUfmFxDbQaSbKXx71jwbN697q02yuLVVJAD0L9uIFOQ8FXRQ_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owFjldIKL0ehmrbz-auJJXYZysQE5iq-qvvdOaZ8swV8HHE5Biy-cpkNaKIasMFD-mFUMkROCwujlhd6ke81yeZ_Uu_Jm79NZtWOtN1EUk_iP2JYfmUMvU77ovcpUfkit2xBP4aN4UfABktWWHlN1w1MIKSW69V0klpsijFFibHFupsd1jCrTPjW6D5-Pg63YvlknuZ68BXOaUjCQq_yLJAt9jomrljJ0Uv86vBBpkt0Iq_MAzwD5HoJFQw3O9iTNCvk1SsZoJwOKF91vcE6mPcogmx-N0rWXK3wZ3WjU4DnqwzJCMW5kYlSszPET8TaBeWOdoLhlsirYQWKAwp26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG5gg1nvsb3XTifH9HUuNvD6e2nIuRAGXNDHhOuUrhY1zaGz8xI_K7kRXoMZZ_9xZDLnlGbE9wvbakcAqJwAfCDgJM-UAsc5_-5pd14Xrbkn6xCQxraJaHj5i1twEkw5urEcPquJ_9TxtFxQneXg8u5rf42Ewjm4ay6tblEpsPRGEwZ8U6CFbR62yXciACF6Vo83XYlGPUgW5goN4pUM_pFFSTlP1tYaIm0tgRu6JZlYIt6_IlSbtpMFYbYe5q3U1LSGjK8gK5Mc_4Vom_wgTJS7vpoXeGPIwg9cDsfv4tSTCvBHoFhpRm-7PO5w3i-4nsoAaO_kJoTCMMO8M8oIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIqeosIxklf9Md6ki8-r1d6cQRBwEZ4LUdyW4kSpK2dt_z8Bn39FdrD3LU7CrmpykefuCerX-5ryZutEpTypABxjpTRq2q6EfnuVxtljAjhkOPMaHn1jqHmBo8lBrr_F-6vgTfHGjdf5jRn1onEnIIhMwVKw0IbX_e6h01VHuZULzcoeUJCajcIpqMj7NdWoRn97NmwZgVUYQYWOyvjYh_UWZdl0W2LjybssCygvy1Wd6jACLYf2nk6nALtVXfF1-kqQv6MpJiZtM4JSKPrxBImH99MZ5qSqFomZG_15isXEBTwJnjdTV6qnyUrFM7flFNDzDiJvqbTt1dFq8siORQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jn7t7CCLXavX8H11k9Rax1AqsH4RSHMl7tICNSKq5sZHuhtIfRvCzb8vaH8TL03-M4zykA6GhLiMvavbNdkTn-cELQBmO-yIF8SjR1aINcvxUysc6A-eRxyvEyLztQrkX1yKKEnfeIPvPr1wm5F4BIIvWfgCM8EvZ2diU1beHXGRNI6R_S_jHl_HMZ_OeQK3LXYK3otiCn8NpyNgIFzrKQUHRe_XDGoomCeZki1gFiRcVCWUJLUbDy-jL4UvcetRQHQ_n_cn4nDPQpoK4t2AhViMhKpxCvcAweXAJmR7WIPdwrt8GboA5jhQ8TLbHUNvUKseiPwankGPTbJGFFKAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIZ5CL9z0zxv1rC9VpTTFIAR07qchFU7AhNBFB2esF42K3PzDxJg8YxO_kcWeqmx7WXhiIZ8lJgWyWGAYSLHCDE1zwTFypitvmi6RJ0fLVEDUxx5Gyxgq_E-20mkSeMXOwNrwSJfxNfzt8KyjDuWzq7HVXFNEWWp0ZP8kGYMOD2bQ6If9hbX1ERTmLKTjSJf6rAaHS-0ToRU8ZY69yIVwOP2JyUm-vppnWmNGay1ZBkQ6mced3ff--KCiyrwd3XX72Yjpf65CzNTYHpV5H_9qx9fpujIYF6vrzC3tAp-YF0o3Y2ycJnL4R3flxIyRlazpIdNgv_AYOIp3NSCv71pBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DikCk1JBIONtfurMKWGHsXf2eHNCayfeW9DBT9pkW1WSYuoxaRk_T0Z0FFssz7C1q2kk433Dvv6ap4qQB9EnULIYw_4-_AehgzU6KHWnKVM8tdU1kiHNo5TzmHrXEh4NOrQ3nTzUwtgEyjttW9PXeO23E4OgeMA7GuVDlsTl0vMzbllsNUvVC7WdDKeYvXHFwIkCMfCZrSzVmwsS8ktk4eD8Bt674mcDJAzakCHuhOWNCgLDeyP4fMJfMWPn2yazaSnxcXS9pwMDROj1FMgajsp_Bifs8xwgAhyiH-0kATpJZRvmmK_jwBjb8tTeyHvOSBF90tCREz7w5d9MMILFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDnoObQ_EBR6ZNB3nrUAzDUDQlPzmb1rTwaPjTYKceUPQj_oOMynpg-hWd0KD17hh7GowNIrqL_wONhzFreRpue4V6vi_CxmhenkyBu7tvB-UsMeyuDUYPMf98CoSEKJgwg8eQiNTRoUPMh-ehlxq0KVOuX-qj-1I9mULQNSsIwfMC51T0kGbFSSelaiGE3ugk4NQ8gSTenJc_c-2EfkvHm3J3q_Z2gejaUIU2S_JIquGxvI5UUAeBwpT9hQeTICrBKcbEKNo8GPS3GKTVcfgtcFitiAaB9fao0ncF5Y4ECsmBDF-EKrtpuQostjhWlEo5V49swiN8kXcKiOMOLE_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=TQqrX0QUHLfGFd-9Mu8N1WXAuVr8BMzaijDNeN9iQzwWe2moYeTY8Aqy4jt4gnYOBqbWk0IZcSTWswYWH-f1vUmdG8nmXksSdvPl_p1gkYAyDFQlb2W6YhExJCRWSl8Q46hkYwBY1QlIJjDZekpf-h2-8g27ivA5KVbxwe4DMoLev4rnPi9a5LY0cSRKIPNt-mR8ysTerdTWPYqs-92b43y42SzR3D-RpQsuZ4mGntiCXM31hDIoDWZusW5bRbs0up1eqGdHUqkqGQXa7Xol8FWwx02aiWAoIYBE_Vza6dBijMFRHFH1d23c8tzpaMqPWGygfU5Z328r29VmG2syKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=TQqrX0QUHLfGFd-9Mu8N1WXAuVr8BMzaijDNeN9iQzwWe2moYeTY8Aqy4jt4gnYOBqbWk0IZcSTWswYWH-f1vUmdG8nmXksSdvPl_p1gkYAyDFQlb2W6YhExJCRWSl8Q46hkYwBY1QlIJjDZekpf-h2-8g27ivA5KVbxwe4DMoLev4rnPi9a5LY0cSRKIPNt-mR8ysTerdTWPYqs-92b43y42SzR3D-RpQsuZ4mGntiCXM31hDIoDWZusW5bRbs0up1eqGdHUqkqGQXa7Xol8FWwx02aiWAoIYBE_Vza6dBijMFRHFH1d23c8tzpaMqPWGygfU5Z328r29VmG2syKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce5IMt8BtYXeW9HTiRpURnLCDrqlxvGXsJBclY_H9E4MO-WKRR4xaCd2-xKiiGxti8k7Q3_CtM2ZVmJPG-lwNcgDNGJ-335W7R6RfZEFqKDl0CVvhR-VM76HCcIO9GUAZge9clSoUs7vUkxKrPWRohAu_87Bv_xXhOPhsFNb2wFbDhGIuvlirUFF3VIXHmOfqeqOw3wUt3PRGIDqiPTZVUD9vjhm7gADtbqxKhX9X3YQsJzAyjg3VX7b0Ey_DDAC_AWW5idrD96dZujravNIG7CqcbTO1xWA5JhNMgmyUXsXSsT5N-dP8i-RR50G4hZej_-gP4DtwnDrhVzmdyZBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=IC5nM9y7YaJx2rT8bhLVjLUCSr0ORKoNkVFVqCQAL3eTdBvnIA75CK0VUBpicfo3yjt1nDm8I2IaQVx8G5qLYb6fTJDc_SS4-eEhAHom-suE6bWwYhb2MxsaI6ZLedkta_9rzH5Ft4rRdJuZJrmDWs37yJ9qo8H3mRsf9ixBmoMVyzG3LpCHr4WFcwXAPhaDx09V_P4CWGMUJUClF6BodtqnAfgyLWO-xD3iLVqUIbRII8GQkA3EJXMMKUvaMbX2yzXX1oKOhAd3ktDzfA-_wTw9u7dFs86zdJMxiA_SRDmYdb9u6-v03MRmCxnwClpqnlMHkOmOedxOvBPzKJ_T1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=IC5nM9y7YaJx2rT8bhLVjLUCSr0ORKoNkVFVqCQAL3eTdBvnIA75CK0VUBpicfo3yjt1nDm8I2IaQVx8G5qLYb6fTJDc_SS4-eEhAHom-suE6bWwYhb2MxsaI6ZLedkta_9rzH5Ft4rRdJuZJrmDWs37yJ9qo8H3mRsf9ixBmoMVyzG3LpCHr4WFcwXAPhaDx09V_P4CWGMUJUClF6BodtqnAfgyLWO-xD3iLVqUIbRII8GQkA3EJXMMKUvaMbX2yzXX1oKOhAd3ktDzfA-_wTw9u7dFs86zdJMxiA_SRDmYdb9u6-v03MRmCxnwClpqnlMHkOmOedxOvBPzKJ_T1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIR0y9Bt4zN2-xucxRPYgOvIfs_nk2gH0sA6Hbf2mIuLxwlsOpowq1XNXXv6RCCUycZpjOa09GznkA2lX5b4c53r341fQODZ6zJD0_yItOaiVJrl5ssRFsN-Yz7u-FL0mLzaYdHEsJVwQg55cBApQJYl9b-W9nkSVMfBLIwZNEQvJu3pcgmJUH8zfZohI1hMmGwnhudcpXU4jPPxO-VtuKX4Hy0DgQoKNKVpPoKVIFimHE7FE8qx4GoIzLodsaB4zg4tcGPyfV7lpVgfmFr4Q104HUs5J_cVNerMI0GMMoe8paD_zD5MuCIeo6zG-vWnNS1ZLOamxuip-kLboSYPNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgMwS8UZ6Q1BGDKfga6ity2pesLjDsdExgyQTkKGouzGI98aZIF6LR31IrLdqnTFhSggBsVBLU1U0In8N2DAla7VkJi4wIjW5bciZjeSb3u7OLS2zNZtRQlzI2WZpa7ShwfuH-nwiSdSDvCx8E7pJjvwm3_zuV3Qa5rTHRDnCVoTOVvr6Q0VJSUVJha3bJeB55njhbtI8cAVtHVT--GHxll55Y5zuVzFwDQfyZ99GMyYWXJFlGTPnXgqC5iuDzDPm12RxEVKwiayIFZcNbAsvGxso1ZKzWlJDDJOJIYnW_XCLCj06sm-NyXBCoVSRzHuVeWEnuwvl9ygPBYT4C_TDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=sbi0OO6Hj9ou41It6ExOb-DnoFYqY1Ee_jHuenFvAA4mumk_DpuKy0ocewuDrPJR9XQpXzMWvWsITXTB3UFlyrFdCL5w5aVOWm0q0HZlwGNMoDOPX5R1VNvThiY56idagUuJWIpITaJ_8xUSAUlIO3b-tkJ-KSVXGU7aYPZTfCJDjCxJcpQEVcY395_tWT_caimb3VK6BIBnh2fN_O1t6bh_0Wr09O-dBqBmXRmNrLZc3v_PhJUOzyfKYvaa0pORniP-v9tkTO_R6WYGWXu4pNuxBLaDpITCDJDa109yoKQu3BWLMlOLO5FeFTeR8YkB9XXvXONU5_NmNbkzFth-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=sbi0OO6Hj9ou41It6ExOb-DnoFYqY1Ee_jHuenFvAA4mumk_DpuKy0ocewuDrPJR9XQpXzMWvWsITXTB3UFlyrFdCL5w5aVOWm0q0HZlwGNMoDOPX5R1VNvThiY56idagUuJWIpITaJ_8xUSAUlIO3b-tkJ-KSVXGU7aYPZTfCJDjCxJcpQEVcY395_tWT_caimb3VK6BIBnh2fN_O1t6bh_0Wr09O-dBqBmXRmNrLZc3v_PhJUOzyfKYvaa0pORniP-v9tkTO_R6WYGWXu4pNuxBLaDpITCDJDa109yoKQu3BWLMlOLO5FeFTeR8YkB9XXvXONU5_NmNbkzFth-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7IRnM3gVRzHXlgcKDRNmw15w7DPnCZ3ckBfKD1OKJFerMDzc1fiTx7IbPjDBgWpnUv7lPTm98z9gMdczefuwcZjRIIibkWMKa5RzH8L20ycjKpEz7RJtkMBzgs-ESbmnj29vNS5hB9LRDBH6MWMuzK6Vk_dV9zQHrS_pnNf07rHTbibjVsEWYP4r702jO5le0oes8cw_IGTe_JenPSkUPiaeIHaXItve8OHXwDC35vPNspPQmwxZLzrAM2NPFjlyjOrO7NbGeJLMJHc-BRO7qfZ118mhO1FdWfR905c5F-7iP5BDu2GaxdtmAJoC7SxCpx2tQ0o6d0pc5ICo2lcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bh-TT5_WYY7u0f-GEXWNa0VQ0FJmFsuLiBLWJJVnNZY6CoJmpScITxvaKRLxwNVQ_i1Hy3QNTbNYbB59wZSvYbjEfyxXxVAtP5QaR7DWsirozE91H_SsvPOC2F3rHxhtdnyfwCxrEKY_xbYWnHyScahEpanA-cvFVENp0KbYRfN_wVZrDV-N5gsTdzKwJWM3o2zDAsGZyZx9bMMqPUQDarEVy-2L_cdpXjZJL4OAYNBNXoajYMpDYOjJFv9bA4_KwYoOeeqJaT2wbY77OPxu7ZkNccf6Q0V7qjrDyd9YxlfDYe2hJWDGr5trLXkW921N9BRpNsyxOqJC0MpKuicOQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egIVDWHOLT6rIS6AfaBRQtDnO37ENJfmq5amWtFC6cTjEsWLCyR3AEYX3rSN4QF6CpuBAq82_Eom_q-45HwpnJWOe69Duz6ynQP5GNpbXEiMeVhx2E78V9wUEZb-Wu5O9f1I_jB3k4M5iSk0aq2vh3tF24zH1T36ocrBptg8SvJznQ_mDKkbTmHcMDH0XIKaCU4wQGwSJWMzu3O3PGeTajIN0ye0StaT4y_9ruDoj98bys9uJlxVlqN7Eurlb2WksyH87J7Y8qA0UwYNn5Y6BMkbs2DcslD9beGg_tJk2MVrujG86hwObLFVhW420EeAah75uSVCh-Jj3sLsUqAUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=k1D1Xw3dfEaNyTb4L_h5PCXZYVzg8NXyYWhUnAp3NEzBfFb32vAmbjFvyniMNjMcajBKXuCrf2PiWOs4RR6vgu710IKTph7IIDYmLBL4jyw7kB9atj_FaD4-oNC_PaYu_sdiyrZtq2CezRMvvRwIEOsSrTkbKVLtC84QcbKx3msdoGgGkiUeUuIht-kg1dg0pR9zqrmvtdaX_IMp3Lg7_Uqq5ftb82SoM0qCcAKCsCr-tbyDiV-g-13spJ5AZJVBy8ljZd0vb336ozxWgsgfRHyQKuv7hAmmbxvFr7JQx6Mmw21VOKlmR4tx7IhS74U0YiXnVNl_xynJeUqD4e8Arg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=k1D1Xw3dfEaNyTb4L_h5PCXZYVzg8NXyYWhUnAp3NEzBfFb32vAmbjFvyniMNjMcajBKXuCrf2PiWOs4RR6vgu710IKTph7IIDYmLBL4jyw7kB9atj_FaD4-oNC_PaYu_sdiyrZtq2CezRMvvRwIEOsSrTkbKVLtC84QcbKx3msdoGgGkiUeUuIht-kg1dg0pR9zqrmvtdaX_IMp3Lg7_Uqq5ftb82SoM0qCcAKCsCr-tbyDiV-g-13spJ5AZJVBy8ljZd0vb336ozxWgsgfRHyQKuv7hAmmbxvFr7JQx6Mmw21VOKlmR4tx7IhS74U0YiXnVNl_xynJeUqD4e8Arg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
