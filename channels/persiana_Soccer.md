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
<img src="https://cdn4.telesco.pe/file/UmLc1GfMjcWwOnQSCLQa3ob9e2yTwFetjC_h4JjTe0SiNpQjsMgDtXe0r7X8QsnrvqO5u2Mn2QFzt4ZIPxwBmB6wLu9YkrUDk1NuDdYOo_lx3pL2sSECjKTcCYdS2bz8fLrhFzlg2wb6DXc4_Rv4Zokkur8yYSab1KwvkPq7oz348quyy5bl-bQMPXdJlkqbfKpSC8rrhB7P-qcPBN7E3pnTk0VDNSMiLNebmjd9Ga4aQ7GMc8MOS8U1BFfihdkm5UcRM4dbgmEl7PCkPfY_GShkI9VmdKpRyQvRVhu6uNMXPpnTbBbVdzwNuMTGNzF5dvK8pNwxVwsPtvmC9hHp4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 629K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 15:06:30</div>
<hr>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3q5es5ZJXPzY9caEIVD3wd1NdShJci-46wmrakSzImGF2hLeVYNM7CuohQdGg8ZRr013ukL6yDFJvkFgrQOVoLRz6wp-ba5lGo5xpbIjJ6FeukO7GOCLw5sQcCYwiyxby2SY-y8biayJMUypirmSbzWUdFGoFhPvxbCvz80fsKa2icAh9wgQSDz5yARiefEXL_p2OEq2o6dHP6x3Ebrx5CxMCLO4nev4HIxI4q_ypw5OpGPpkPJJdqT9S3TAO0mnzC79yWxn7N--17Y_rZYc12V2wQSjhXMat_Fzn5iPYxQM7OlJw_OkJXfEVYFk5ecEuoeeHXwzl2U9-nwetPBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/retUssdp_gfhy1ihfY55xqHPDRHRLzKuragYTz6un0tFHl38XQYOQq30ZqpDPzrqw19b79sv67Q9VgUn92AopM_3qfoRAzJDgMgGzeRUxtfk7bqhUPwVLHWmPMOqyZxmQFnGBNVHV27DdjbOCZwVyJ9F4FJUTyvL9rth2xNl2tk_cZ_mXxyP85fCPHPPlcvds4zX796obyFqZPaeosf8U5DPJGw-62eKV5thTGHRLb-XRmdD8RSGluQE3inAbi4BJ_oNHqIM-l2rEslYLyQfU5xHJ3a76GfaoAGLjKApcX4CuB8mOzqjujyJoU05wovyWRaFqkz_3MJ5h1ZKkbzIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d39tCvmdr27z7WLjfXiQOkJGi8rrSlvAu-JmpU_in267MKkDSvnH9stfeOJN3g0ekJJrA5FSBzoOnZuP88U8Z5VG70IkUIvA-MCVxa0R7PTW630ta57ldh1g1mJRS7NkCyamAQP5VddPerTDPq375TVhZA94-cbYso1DqGQMRm2NVV8V8XPoLM5K-oJWWE8YpM4uT4eu_DGSgzNQdt72QIDVDIXr32nmTSGx-YudUDAWvhTakMko9tRnCx5enbmwcsBOXwpxJc8kIMME_AGckdsgKq5OVJJcs3scUiMjQyuZte4Nkecr69vWV68WrYvzMTlTwjYjB0hH3shCqzEnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYTRdXCs3BXfRJb1LPdWxP0KEliF41D-w_dOG95CjOIIymS-NgEpoOesPNa7PgN5PZaZgQ92pPv_VVRb5X_BXI7BK-KjPVQQsoFkkBFCHh-MJmS1GxUcdcQ6vPmr0-i5BvwAbCg1Aivn9sFVOJ83sf_nj2nLrQ6vrFI0v1IxD_oRqzKeSOC9Qr9c84PB4V5HF99wiPlJxYcG7QI3ewYJcUM7rRpHztU1CJN4HjAVyk46-xflrmxDVDFUxuHiFHEGY7bKYjsBiWZC5tnQ-LnIZ39jcEg4-0azeBZw3rMreWWA0uk1iVu3qpiMsfXXOJddrZwsBdgm_fK6yaXuLRVvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJvdcyCSPugtiPgFv6dr4N-G3hcs7QcHiyeoYlY5edVAcfvCI41c-G5jDLnaemM7fMJVHZ5iBBYl3iZV643wZ0i2O-4Epa3Vmb1d6HB69S5_l99O0810ZuyvSU2MXuI3DSC97dDFLL8oKxZp8mGgu9BED8iO-y3ZznuDau8sSypIdTdq-fRAclbzf1WNV55uueEwiJZmLnllJwPAXtGdO2enwwo0CYfm1ER6p3iF-pnrI26UGN_8JfeaTM0E94KrSPSjVQLR92eLPiVr2tnNKQ0YW2jYv1TnCbTEN-m8b9FgjXcHKV0wcDA-nwsH7SLrAPNc-oi6XAL3VAAwZYvA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgc-Z9q_aOBXjeeBHJzmOKKhsLkP0WEB1VeDH7C_pWmOXZQwfjm-r9BPAcq6so5MrW7Aycbu_9pGvcNs82CfNFacUEIm2f9pQkopzTYydY_h7vFev9gyRdhyPtk070JCgdhX1z57vwvuMVluTE3tRno_mpKlkQX8ctn6PUYH2tja1zxgDj3ahbQy3EUsQ2ZYkoIR5nxCY3V85DyggXzJXAGIPofxTEzIgskfSUAsJwYjvyAMIolR4-GwmSV8LuYsM2WQwNePsPgxu_4LZPaDTtpwXOyvswB1GUthSKVmjbCMtchUDh7lkSh8Y05VaWmPBwoEdm5sOHZM98DuVFRBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=XrplykliL1HXjaLDUnCNlpIH_D2Eg5VZRMX-hiPakKmu9NEjLcTkGLR0EVfK7RCICswB-lPRP8iKYjhUj6Hk6CRDiTVqwvb0gdIFBb972eJFwTXhIBnlglXfke-krCpnmoqkqJ44J1zKMKj3_36i3CdbyRwVlD_iyMocOogtVMr4st2mgDclCNuWlg7cuCDeSLF35pG-557bc2atZE3rBbvh7iosZZEdYNVSAfp_oQD7V3S52mscKD_rOU75HikAobTcs6_vKHq-3hw4cCyE07kz4JphklFWrhcA69Zvh0RRtmjwzMK0AnGWTLwdA_Ji8mjzuG9t4HtlFTWQPInBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=XrplykliL1HXjaLDUnCNlpIH_D2Eg5VZRMX-hiPakKmu9NEjLcTkGLR0EVfK7RCICswB-lPRP8iKYjhUj6Hk6CRDiTVqwvb0gdIFBb972eJFwTXhIBnlglXfke-krCpnmoqkqJ44J1zKMKj3_36i3CdbyRwVlD_iyMocOogtVMr4st2mgDclCNuWlg7cuCDeSLF35pG-557bc2atZE3rBbvh7iosZZEdYNVSAfp_oQD7V3S52mscKD_rOU75HikAobTcs6_vKHq-3hw4cCyE07kz4JphklFWrhcA69Zvh0RRtmjwzMK0AnGWTLwdA_Ji8mjzuG9t4HtlFTWQPInBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=cbIq-mxaHRHcedyn8yCBQHo5uwW5YnQdgnOyuqEvDMQ2J5p366t0ExVi-Sx2Gi7qrcmOULpiR83eMVwBAvDPJJ9Fm9vJJWX7YE_ZJEEJkwRR6qAK13iVi_-v4k1cFSivHX63WpEXdyqSZUrOprUpU3o2NkLRRiq-E4L9KmNKbVmohXxz-kttWufLhtVrbGQmmrC5vcJ0Y8Qwk0F7n4wfl74HFE4SXl-5YOvjeH2izDA1Az1b5xho8KaWBreefM0GKOGA6-wekPfYSftRf_fUeKaetlHxUoJmb-8sekl7_Vq1rE1mbBZnkm37i3aWl1bhHqDyS3r9TMKrAMmzGK9zFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=cbIq-mxaHRHcedyn8yCBQHo5uwW5YnQdgnOyuqEvDMQ2J5p366t0ExVi-Sx2Gi7qrcmOULpiR83eMVwBAvDPJJ9Fm9vJJWX7YE_ZJEEJkwRR6qAK13iVi_-v4k1cFSivHX63WpEXdyqSZUrOprUpU3o2NkLRRiq-E4L9KmNKbVmohXxz-kttWufLhtVrbGQmmrC5vcJ0Y8Qwk0F7n4wfl74HFE4SXl-5YOvjeH2izDA1Az1b5xho8KaWBreefM0GKOGA6-wekPfYSftRf_fUeKaetlHxUoJmb-8sekl7_Vq1rE1mbBZnkm37i3aWl1bhHqDyS3r9TMKrAMmzGK9zFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27088">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKA5Nx577lVIQpa1BqEE68BCWiSYC6cbIs6lUA0Y4jM05x2hDAr3VIHpvFFY5W-AXc2CBi3l-bsCYrPKA04F8uc_8zkxwRtwfjszX4p3fYnQl67aslEmyUet1_R0zl0C_GMbB6CfugYkEcK0-UXP3WDLaTn64QVA74OtusYwp5ez0OrJ0mDIY325GCzQXl6aYnsRUt9NNCaawVo0_3h59Kb9i7iZ2s7-c68TGPwFjNym7eRHmhonMk5dUPx6gPHKwhVYUT5WyWo2fsaEfxAARY4OEUq5dfPkx2zqhrLRxyziuIXM2qZeqqAIg7wbu8gOcTpkoAJZZJnnTHCwgGisUg.jpg" alt="photo" loading="lazy"/></div>
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
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/27088" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFGPBChoz1tQC4CJ5fGzY0Ax0FnCLMU9zr2OAZA1rM6vjNzc3H1YZvhlrw_ncEFANfnoEYL5R_yuvFak66ekPrU30GkAZqh5XtL8z58-8s63k50-R6JSNZzZeZF5WJp1CDWve55BV6pln5daMO3-C5VtvdJX32jo5fhCaQkB2NAKXBUwYIenhHCfydsNOXJjAFcztZnL1mGzEB-nknqLrrGf-VIOW8ViSySSQJ2SESmfrDGfrT2A8PSaAAWhDNrDZXDhinRp65dFbD7ZJ3gOscIMp8FfMsJeymOa0300cyXUOQvZsCpmuqOdO8Oe-ab1xPYSlY1Hc9rXk8K6xdR70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7kInltQnZitUpPE3rBlOE0CHQQ2mL-DguptyD7ePWVRXIj2TN6fUc8wZZpIDHJaHcuTggICeAcCq5WswGHXghokJpfr4yEBm-mb43osMRTeGpMDicj1G55W_zJpr_vm4xS2Jemx---8ENobTJhh2saxCOd8yPGYUey0f3qd_ByYKD0AVypujkjmUhVdXcPbUteqTLtEoEla3rQy3iZWd403XzB6zFWDw1hWkPDo5G_EcodHyEfhlVvHfc-IcrDid8TnAR1zKLPKhybno0X3M5H21vzjBaaTO6k5Gx6m7hz8iAOLANtfRW7cb4SwApyh7H7l6WvkPTD_YtDtAZqQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz_h5oWkQoJei4d8EFySMhfiRRYiNhFfbtwVoKCLOFu1cETFLQlWynW1MX5SFL1RuoPqNHx4nN5UTrV3tsR2Yd-Lt0VHNjRhu-59LFdQmty8FizZPsVT3ruGDCyAFFxLTmk_dRMGUP1sSLr90fpHxgWB5jRZy5yL8v1AvA2lHd0YSlEuxJbYGi_JbMSvjj_UdU1YuJHLp3cbWVZW7xS9t3J2MH0yH8i3fYu6s-Ga3TKMCcHM9FQp9zOWmhnqHv_TDdaOGo4VXQ09ot_NeUWBBQi8BBi9zgvcwBxDIVWtKaW_Jb0VWGVneip5r5mxlB9RSabgT2L4fhBncnLEhCtxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27084">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMDeZ38zAfyLTVv431OG9uad6kU_Jn3hkgazI8qKd-WwJJM6P4BjXR4IaD8CzWLFmR0nyVzzLs-yhopsjVz1p0UqzVOa_T2ztKEOmrhRI38Yy21b7KJs4DMSx5WOvM0NEmgCfrHn8QHqvYI2CgMsGRKyUzan9TSo07z-tcBTUh7rPVTPx1ZuaKXZFbDKtxSJk6MOuQTeyfmxQrw2rstmzAOCYPYehXpQvJhD6iCM5aIxngxm_s_jB1bzkomxYo5RyFlcEnAVVsT3t9k3OaP90VaqJBGWUwkQq4stfwH_3PLPA8sbY4NqG5TVuEHHAD4haMen0Wbr4S62dcPCbvwaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/27084" target="_blank">📅 10:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27083">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fnuhmhj_aiPpibHors_6D4Aj7oIZIHaLuzVA4HvqqvXDYG2SbA4ib_Oeptwspu68NYT2sK73-GOzMkkNlzawajvgE6-dpMENRB0W8Dq5cnGfQjYUZBDDM-q0QoHxhEO8BknXE0DNBWvrHfqiUU4DXO84BpJ1vkTBT7KQh43V23j2uONiPCFD6irKqTQ1SLWVOZprTEbK6bRyL6vdbwbgju_nQ2mPd9Ke1euWjruLNVFD4XdTffHrwxdav1BsgNAc0bcu5mro-gvwsY6X602g8W9fuXkbhwO6nrQem1_lHEZrjl1bF5jY87tBSAODsnTXBG1VdZQRZ8aOxxh2CMPf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fnuhmhj_aiPpibHors_6D4Aj7oIZIHaLuzVA4HvqqvXDYG2SbA4ib_Oeptwspu68NYT2sK73-GOzMkkNlzawajvgE6-dpMENRB0W8Dq5cnGfQjYUZBDDM-q0QoHxhEO8BknXE0DNBWvrHfqiUU4DXO84BpJ1vkTBT7KQh43V23j2uONiPCFD6irKqTQ1SLWVOZprTEbK6bRyL6vdbwbgju_nQ2mPd9Ke1euWjruLNVFD4XdTffHrwxdav1BsgNAc0bcu5mro-gvwsY6X602g8W9fuXkbhwO6nrQem1_lHEZrjl1bF5jY87tBSAODsnTXBG1VdZQRZ8aOxxh2CMPf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت. هونگ در ابتدای جلسه هم از تمام مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/27083" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27082">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa9f2DOZ-cSTeowMn8XFydmodTllQyxIoJph36QsdRmv8Gu1iRMtloao7dwEg3q8F1viH4AYphOGBMeJlCqqugckG1MIaDsRMcAr8Hy8zYQBAcnaj3V1HQ7xscYV9fcHK5TuLaNjZtVFpyEA3-UwDdqEcpQmb1zu1Or5KgMwYV6JptblknPFUOei2I_MwccfXs7k4UZgEeZSQq34aZzk_HNkExANw9X2HNGBAVZKHs84O4LJL2MHE4-mqebt5QfR970ijTAPU3JHBT74qbhmL2lfg9NkQqWsPq-m2K41hin6bz4RoCgRkMHQp_MNZuZYIp3kkTJlin5cTKGLEY496A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/27082" target="_blank">📅 10:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27080">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0hub9yQ0YJ1yJvtR6-Z9KiAza10A6iNcbxDW0XcADwNbgwe3YAb5eZncnI1ZPiSDWP8w-hUtjY6AZ_I4uyNAYqcGg5QwHjVxeBVCdYNbqkqO9npGnl_O3OlVW3ZpoL8iuYkEwWFk2VzGO7XmaqQ9cyZYnALSsR9cxo-GM5HCXwY2MCyJtdzH30ilNhnA9yWtHGATT-rUddcdrvf5P6FkxDTmhgFYNArePav7PUaRSRpWY1S9i4KhI5TAL3V5E1rxYX2NGw4-GqSENnAk-U0G2TZWZW250sP9t8C0wJlTJsZgv1WvbmHmbsSCEiTy1uiKpx2Wa3tCBT-iH3EQJmXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/27080" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27079">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ5T--nQO2DTR-6UeFS48C41uPWGu56djFlpnfyDcHu1WpZg0YrKEG9xEWwRSN8f2cIDAkWPbCXq4yFs7ciDO05S9uSyU2b6uaVF3nzhcItvzOWVXqbZ7vN-fjGzoYmMrb8oZ0ZlzgXONBxIW2ZavadQVaN034NDaoRU_QGBlWaKAsrqzR1qxWKDrC7i0Vz-DzFe5y0HQYJ_oFGU8hBM3usBmX365WrXROHgTL7Ay0-ncskxHRuvxa9yrNW2yZsrBr7SUVUEAtTZRVjnCl4UU6h5SVGrOeWplEHjmN4gv5gVa0BEokBHE0eMD4eAE4rX9si-awSyB-Kcf8thfgtXuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛
سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27079" target="_blank">📅 01:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27077">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsqwBc1QWM_j6DJbHuzEpPne8qAW-TfXuzf0GsXwlUiVbhKAgT9LAYaKGwHwrIEjVLmoQjzfEkCaTICooK8NfkIjuwtMNhhBhhYbZFKcntg-xxNYcdu-Pig9_yDmnXuvIKchzoiACW3sbsV8fX8n4qbpuw4qKSCHVxANWKPEg-IOh-a8i7LNiUsu7GAVi_K2qoVdAe44PfgORlwr6tnjQ6rWYUskVE72rKSKFvZV6MAJ0EiJMtMHvXvCGtPTb2n8uS4p3-TkfdOTLwadUEdBvQRJiESwpNOu43-2SZcBOTignbDsGyJl6okrGg-ZK9BYndfEW8vI0B8P5Wnnyjb99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی و راحت باواریایی‌ها با تیم میانه‌جدولی کی‌لیگ کره‌جنوبی
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27077" target="_blank">📅 00:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27076">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hI6Na56tW-jOn7jl1Z_heFEhwrRJU4-bC_GcLje5pYVEgv4cEqNXFxLw5QAFhba2h0ur7cC9MtbPFp5_z35hWn1R1ZujglHqowUfwHW9CMeW5hJzCs0n-iG8DrhT8hrZw8UrG94Hd007JZUnnrgR8zy84SEYTItTm7G-xZRaghzPKqkddcG1f8N8G9t7B7Nzy3cdokQaCxwz0DO4fUjvj1y3ZQr1D9yNNu1OMeTrZd5vLPKSED25mtiDuV2ruHwBHENbtt7IvloavUD53_OxkduoHUiANueIPPCVlh_j5FNmJZZh1M3pdqnbKiwWOCdYxiBoltLzyy_xgRUw6koY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
روایتی‌جالب‌از آیمن حسین ستاره تیم ملی عراق و زننده دومین گل تاریخ عراق درجام جهانی: در سن 12 سالگی یتیم شد و پدرش رو از دست داد. بعدش داعشی‌ها داداش دو دزدیدن و هنوز هم پیدا نشده. بعد بخاطر جنگ آواره شد و یه‌مدت هم بخاطر اینکه مخارج خانوادشو قید فوتبال…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27076" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27075">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuijQeHuo-C9qr72MsX-ql7ph0259pMFYrVnyTROvUNeujvZPj7js6xtxxX5bMP4OXlBCcrSTDbSBTaixL8FHu2mMAWSd8oWzJryzjOCAEWq4m0zriJiYmmFA5QTugmCIAWDBFDzfAB-31iy-1XrBQhk-9RYtZx0oCaulKbhj_nCUFk6SaCBf_KokVyYUjFT54lgV8eHmfDZ6dNUQIWxLTacBje2TvXB2v4POJMoFtkzKDdB8eXZKhXRTmzoJ7YmcodQiu6FyZ5iu52R75__KpET739GPVMTtaVfcKczjBOSHtRlscKzCOX7iZ6GsklLx3B7QIU1meVZ_Mr1U4OTgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27075" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27074">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPqpoTI_5z63JolSUxtZwW_BCuvOIGKRo-p8jSJu0TfQyjoNc6BXV-DS24qWqf-DvZeXrmVh8jJUJseVp9_Il0VqSoov2M71kp7DzxMPZyoVha7s3_bXPz6-tz-nPWhqZUH2OqKvfH_Fk3q9SJHwS73m8vsxnOSIWUjBbmhXcwxt7tYv7JynAtM95wnjisFp4CY15SCENkBWklnylJZkv18bkGeNb1XR7v8U481dWWCBf_3WXVcEl3rvK6WPeXba3pKxHWeLo19jRvmDld7-JLQJgeGOuA0EMDZGHL2rphWjSG8DFA0F6r6uLxPHaWpcWh-mHcyC3eBmbH4Y5SGBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27074" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27073">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erNI72XVTHua2H7V1QXse6RjWMwv-EkSG7Hpxf1dPT1lbNKPURu902JhKOFwhvll4njT3uMyo_cJOK9gDMh2enDg2vf0g8VweZt_AzAPsswqaAolssu3CBAlPJq75wup8vqp7TnpkDRW1dHCoZiJ3hlNsLhediRCxfsU-wHSLmSgybrpmn37eqjC5Ymk-54l5eQrBTH5HluVc3DI98ehkQ3bJ98H1sgISv2S_rEDd3WJomei7JJFQgdQ_7zVq-ux6LQ18-coi2vCMAXxYabjEG2yt_1WL-0Q7_Oz7jE4DNHyyj8ZFpJVXUMdnvBHWh9FRNQZMET7bwgI2035vPAksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27073" target="_blank">📅 23:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27072">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzON-oau3bTMOZWbrU_dK-fjiQnx8yuz7quhNOASTS5_Gu-g5a6G0lLaYBVZaz9iHEoF4tN4CueP1tf-ElsbDZy0gvi-29V4IGADggasQwJPx1dzieGh4GRLE7suil4qe5gwztpeT_lmZ9ekFWpofOXyirOqdnDXm1xSGsghssy349_9B1g7QKbJRytR_v1FF61-UyxUeBUgyK2706CAu5z18cv9eB0KLEk7ipFvOzOFlhzvqWLBMDh8ahGx4e0HHYR0xr8wFAoHrk9ma3uevYvUY4yNpQrtq6j1tNUF0_fca4NVHBlatQYLnxAivGnU58OunAyqaYVvkkcCPuPK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
اسکای‌اسپورت:الساندرو باستونی مدافع 27 ساله تیم ملی ایتالیا درخواست جدایی از اینترمیلان داده و به مدیریت افعی‌ها اعلام کرده با جدایی او و پیوستنش به رئال مادرید دراین‌پنجره موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27072" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27071">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoTAKx3t7eBtnAjm3w9tnES8cZn8YJX4bjp4xDTJ4LdyjEax_8F4-RtypufwS-WZd8jOIgk7PQ1ohx71f7iaC-MA-xhFSzO3bRDlmOA15CJHYKEpxr80Ccgk1cmEdlpi9dO0ErzGPlaX3szQA1bZlep6ytYy6RHkwo9mGgoCOsnJtqLQ1DhchGIlyYc1PTsr-UT9_pZnUAVJVYWBKxWvrOESbgsNTJCmWsC8Km8lAIbytRFTly9Nq49VJ0V5f-rgdgUjosKGk5dCQTS0dZSfKQ62LmWx-2cFKZPiDHBMCvulHrSfrkAtj33kB0w2_3wJSgjW0UIK_o6r130BW8rJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27071" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULOflGez0cLn6l479rYSdmkvxbILjq5hepalA7e2oyu-GZRN0fVsjAPOw6GTAVk-Zvz2qGK1Nm-zYooNuz8YtYPRHGRBbTcGI5-3NwMEU10C2eSmd3HQyZcpjUMZQ9MpQ0qJqRjQz7vDLbg5Gwf9SmIyw51gyi-MaCNvKoH3ZAHQUEohgdDl-pkyQkq2S4CEko6wLnKqgxAshwGyS-ughU_d5AgqtVBjknJUmxNKknoHha0YIHA3_M7bR7aXFEIXBAm-gQAXeWcfjPo0bnCFHdqxfBHPrSWoZMFjqvQSKs0A8VMpljysY9ddijadc66m3MyJ6h6UHgHeXCLDavVKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a42Mh6ZuFzjqXC5NWhlHILUbQBzGLB0jdKkQIvTwPhIKuyiYbYzmxfbm9RncSjJbpW54bSgTL7UvwtL0UXFDBFWrcKvCAryuoJdR50ZtzWEaONLwMD2Sjr1YPeUS0d7THBVWGao6I2ir8T5-s8agnvztJRldViFDcnl1WB4k4jZw7WkKVnGF7PRsDR3UBF1XNGt1-85d7zNFr7Y3gBsX2jMuDHGwcBt2AoFOuXLqQdrnGOB1ab2XjyTYWDFtFQlVAdgaUcBkHI4ugnXadnB1TY3qw5GnHZF9RCHmh_Ha-K3D3zCpwpqFdqh9xf4MyPoXXBwp5Z2shinZtTKjtnwi2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=gYU_Aw1TXmcUcgFQmxCV1f-3mmeFTSt7KrMETbptNWpHGa7uzyKhYHOdKdf4GCZPIZU6M2bSgvN5e5PRsYoN2RVjLWqKBNiWgrrb1NUipbQ3hrK0Zro5Px0dvGBCfPV_-3_nQNVpEv7g-ZY83Mv1vPPxtLK6GjoPWJIhKTI-N7cTyM9UQELMsiDIME6WMZu42JjzFRRjAGbM7DgYWE3nEw-u5DoGDBc6ywGiz0_1ulz-LRxU1VL9A86TpPhhElp2rtdqV7uxKwoHXcPkwU7sgV1yUHZdhve1Xrx1oLd5TZtJOmVow8eDPQUQKmTZJ9fsJax3IsCDygvF8Lp1L6kAyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=gYU_Aw1TXmcUcgFQmxCV1f-3mmeFTSt7KrMETbptNWpHGa7uzyKhYHOdKdf4GCZPIZU6M2bSgvN5e5PRsYoN2RVjLWqKBNiWgrrb1NUipbQ3hrK0Zro5Px0dvGBCfPV_-3_nQNVpEv7g-ZY83Mv1vPPxtLK6GjoPWJIhKTI-N7cTyM9UQELMsiDIME6WMZu42JjzFRRjAGbM7DgYWE3nEw-u5DoGDBc6ywGiz0_1ulz-LRxU1VL9A86TpPhhElp2rtdqV7uxKwoHXcPkwU7sgV1yUHZdhve1Xrx1oLd5TZtJOmVow8eDPQUQKmTZJ9fsJax3IsCDygvF8Lp1L6kAyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فصل آینده تو بارسلونا میمونی؟ فران تورِس:
‏من‌قراردادی با بارسلونا دارم، اما در فوتبال نمیتوان پیش‌بینی‌کرد چه‌اتفاقی دقیقا خواهد افتاد. من هم فقط منتظر هستم تا تصمیم درستی بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=AzZefiMMcl5y-dT6H7rB5DybOdUeguHLEyrr69hydlwAUzKxC6UmS7_bmQulh__6HR24GO3KlR_Pubvm6WpmQ-m2HONZEHMK_3XazabgkuWYw3c4Vhh3MXO8gowTWzXVkXkK4fCkfkGe_3VVmrYbfRSVOsL2sppQrhUWAkCIn3L0eBPBP9U-ZQKW-rbV7NymLwJCNYvgdN3nRr6p8JjA_kKzl5ULpvNN8gmMtma_vmD441lTiArC3w_vKOvdhpbsF79KNQcd8u8YlNjFkKeNcqdx9ZC9GzPmTfgOKYB0sChRYcMnAYSxD7T5951GJRgHDB8qGOAjfBhCMmUAoek1sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=AzZefiMMcl5y-dT6H7rB5DybOdUeguHLEyrr69hydlwAUzKxC6UmS7_bmQulh__6HR24GO3KlR_Pubvm6WpmQ-m2HONZEHMK_3XazabgkuWYw3c4Vhh3MXO8gowTWzXVkXkK4fCkfkGe_3VVmrYbfRSVOsL2sppQrhUWAkCIn3L0eBPBP9U-ZQKW-rbV7NymLwJCNYvgdN3nRr6p8JjA_kKzl5ULpvNN8gmMtma_vmD441lTiArC3w_vKOvdhpbsF79KNQcd8u8YlNjFkKeNcqdx9ZC9GzPmTfgOKYB0sChRYcMnAYSxD7T5951GJRgHDB8qGOAjfBhCMmUAoek1sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
دلیل ازدواج کریستیانو مشخص‌شد! حتی قیچی‌ برگردون تماشایی به یووه هم‌به‌پای جورجینا نرسید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdjTfBxWekLRFgS_j_GgPnm5jEE4HkAW9smSQv5lQ38GhXgksMSk-PuGQQCvw443aUu8N7_-o67FO8t4ove3RHeK75_4SMW5nO5OBwNdvBl7s3jZ73crzTFzzKhvCu3NENOqrgE8iLyhJKNFRAzzgwP9IFpskN3w7KkErBwAlbpxbTy2OQDSxAXb1fOh8-ev_FKGv1kzpjgwtE5P6mw26iYRkGVGeP8bypNf2zKKyZCUBflxpdHATJqIgSQ1D7cCsnmAJHDiwuDy_l7vju9dJkMhwjldbDUDEaoirdP5o2cVi2Cdsb0hO5atIaFyDpGtSy4KY1uDLR-ezcWB5dYHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzqoBdFhR1nvTkz6FGlVy-XW06oQjACZCbomLqV-pLr6mRG5Qbfuqt6rYpbroH7JUMBssg1Oc3Gok9KIWi4gwEI-EjPG4nOGzEmjyEvf1BWmt2kfIUg25fvDrMEHt5rL13Iv3YPgFE2xg4AHDkY1jEFSqu72zAXHN5jDUiEw-Bz1mq6S7JoakwRtUTmHVO3liJZe_-EoYf7AJrP6zDI0dFE7TeCUdIskxdQQbnl7SziKLLlHj0hkvhUYKu6hOwbomWnXOWYxrNsxFeBn_YSUKaESFHdRXlQLnANFl5M6FT6OanSxriOjK0RYMBnJV3VXcn8JzaOLzK_W-PCqp07vyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق‌اخباردریافتی‌پرشیانا؛بعداز عدم توافق با مدیران سپاهان و فولاد؛ امید عالیشاه عصر امروز با مدیران باشگاه ذوب اهن جلسه داشت و برای عقد قراردادی دو ساله با گاندوها به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNwxbOY-UlT7oGjEruNbJyXMdkSPc2OkT0_sDsWxzyqTYpfK0bTTWf-tJh5SNwa7FfR_iMTWlz7W76ROuiKlJLXm0eOkPTTvm-p4SZNS5tN5gEjgja_gg_m0uZqR4OWXQ-K7GpBX4s0oGdmArzXdp1yUGFG5Gp2mjW7PvCPLMvThvArwdlzjOs8kYwg9Uq9SwlRmeJmPL2oqBb2XtCvyWorW9sssLv0Fu6uT64Yx7N9Odwm_K8eaPEnsNoTDN-eFYvhh6qgPJeCdJyKLLMVn9YFA5d_pU3KN9kBAwf9dugt9McIKcuamkf6sTk_e9jezDjLqgItt9aLT-Oooh66RDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEXlnbi2ahf17WGy8Y237MXlVjPLZM0UcqGQwY54_oBy3ZHbaj6deyoz7pQk6Jww180yBy1xt5iBFWKxSCN4nAMtpZQkOaR4r4exb7GgkmSyECO_CgwzJUOLEUbUzkIRMjhpTOmkUrop1zFXI7xREzKgmbw2IZ3Cw_KVHD7BudBR6dzfV3Y5zxRyCOKn_7NBKDjyAKMBmabG3YcfSHXcKQnTMR4MHbYDzkDMAq0SEPIp8Y0C5fUxeer_WFs-i-Yszz35Oo-0RZQOSl1BZvnhhqF1lEcvEUcXkCd1f3sBvBPl5OtK9vhMYEjO8QtPo6Mgw0Di5WVS1Tv72gRqqZMR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27062">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=XwcROUPlinLrMhQqfWMQ0s-XQ9tbedO9BYvfKJcTKo1YOjNCMYO-jxHr5wbA_SYLsCIL7A93Q7uJWTaRPhopxAAQ21ZLffoQPEAJGM0DP_L4e9FFwbUJY5Um6flljrAp64MYJhp5_CihogVv-tS17Tf3PgS9vMWXlfcAII8WOf-CPV3zGqwZ9wI61EpbTpWwDHcUWnbekl3Ogcz71dZ8LXn0NHEa6696JA_EO5-JafiywEftEk1q0UCUmmshhmdhSRSNFjHzhWjrLWTqEZRb4hiOOjyUw6ywMGfEjaRZqiTsPVKlxIPr_W1eXAWNAX6oOgnaoVsa-XgmwW2398zTsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=XwcROUPlinLrMhQqfWMQ0s-XQ9tbedO9BYvfKJcTKo1YOjNCMYO-jxHr5wbA_SYLsCIL7A93Q7uJWTaRPhopxAAQ21ZLffoQPEAJGM0DP_L4e9FFwbUJY5Um6flljrAp64MYJhp5_CihogVv-tS17Tf3PgS9vMWXlfcAII8WOf-CPV3zGqwZ9wI61EpbTpWwDHcUWnbekl3Ogcz71dZ8LXn0NHEa6696JA_EO5-JafiywEftEk1q0UCUmmshhmdhSRSNFjHzhWjrLWTqEZRb4hiOOjyUw6ywMGfEjaRZqiTsPVKlxIPr_W1eXAWNAX6oOgnaoVsa-XgmwW2398zTsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو بازی‌بیلیارد تو اینستاگرام 224 میلیون ویو واقعی خورده بود که یه رکورد محسوب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27062" target="_blank">📅 19:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27061">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llYPRa680KfGxKTOGeUyUHSw7Mj2HQUCrsHzQNTSzfS9UEhx08iNoWbRzxHG6uuC1PUvNIYFO-T8r2c_8vxWR1x_pAdy-b9aQJ1YZbz7q1ahw2TL305DntkrJj8X7p_tzKm-GOIxzpTS-gICXqj6Onq87ALcGVj7uFOjBi7smgEb9SQGEqaI9QC0nZhETvvnkVucRzfDtK4BH4P4im7RuqJiiT8bJS3bsvLlWrYaD9vncb7wqP8V6uYwZhRaAAepxSyi8q5OJ5g_YMPLhYuC3QOi1eTCerToDyBLTRG1GCfGzF2NdLAeZ4jpjqgqTf_5Qjltfv4oUvhvjH1GQ11AYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27061" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27060">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8SZOmAKJ8reiHHB1Fnj_oFG94lK69nQ5-XHdIp3BnKquIVMkk_89LhFrKal-kIVBsgTyouBDwxMDRY_0STa53z9tlGvW9I8Wv5Icd9fCVraLHcYJibegT3UfG2KYbvNouDQkQNU5lk_Y8NrkJi6zU4ajvPOn6dy-KhfCjGxckwKtpt_QEP2SRR7SHWxDGWoRooXQyv3_-Kd-b_R8l0OGko8TtKlLUu_D0an-u1eGv7el14s31JyPr6oT_10cTT2fix3Xlr6PWhhjPKkcEvZwuo47VxUDrb4vGqyq_WuU9LXTjIhWlnMOj2APnPjCenMyV4wI1PASxCVXSyCWr3N-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ نگاهی به کارنامه لیونل مسی در دوران حضورش در پاری سن ژرمن در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27060" target="_blank">📅 18:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27059">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpRzg9UuHqgChj74rFw0Wr-BO8nXO1tf9L-CCJjJfaDmv1mezDWerBmglSK7Pc5kDt3Utl0FkjOM_GX4EWCIPNmqUM0i-DSWdQ2O2wPeI1QSRrv-9tdfNcLcE0ERkZQb-W4Y4I72Mc_WMcUdfkUTJim_UojmvfLxOvAQtZBUUVANqIYqqojw4DQ807ccN8mLe5RfEURkoRyXaiIh5aDqi9cFLDaIsSBj2Tz2grMOqOmAO_nrZKszFANtzR-uYqGi-eKaDNBZELxpb6G2btesTyVCpC12TB4X7u6e6kQctdspuB0Jrs43qPGr06a4N-t6VvN8pYAMdi5dkN2vsozrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27059" target="_blank">📅 17:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVZ4KXjDj5Ta9lYTFMqxU2Z2i3Zoiehz8UTAU84p7g9MX0V-bfXFo1RC0iXyuVLDhqOUjHjDK8PEt0bzQbvU_Axe4SfLWCWjtu8PiXK25sQ3Bqjg8i8xYLBWR-B5cr2bfFCHlYIrt_p_1AA52thswSUUg9qsvFZp2yaFqsK8743i_iNrkBJOrz1D6d8DfX89ZWwKthoNK2O0E8alvx3_nt5wLoamKbzHVwJ2jTj54HMAQD_OuPDCLnUbTATye9u1R5L4xhtbLZ-3DTziaGBWQntyFQkU1OEPBD4EuccqebyM3b9IktMm3Dn01mjUmuiTPHU5WOpyUENATB3h5Ec2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL-EspvObJ7TgWr_5fZqz_3U30FLFzBSpMvsG1XMl8J8c8ndW5jMYZEUOzYeyastXSi3h8s_P_yKe1z06D539PZ2DspW-ySxP4_ldakLEQTpGkj473J3JRUxxlVujwfe1dto4NdtOkA1wuPTEEpsRM3KmuVgFY2cPBASCHu9wolDLahYRkqIJesP548NUvfxUx8r9tbxV0iS-I4hH3h5YnZ4EZtJ5htUTP41yASUDCaR0sLFFahfS2yOeeOXbV4apSMEgUI3nLw6WTTOmZm6auTK2RsTxx-fOa345WpdTetZZofOFEh5Ej_YhGzFmeYOakg5lEb1hiUx5HQoICXKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObFrx_lOWwrnZxHqc4eRRBTV0_2QJYGO20Z6ZBXnKOJOe6Efy8nJoIeePlI2SJjlIcDs1XKxuMGwIn16KzgTLukB3hdRv2q28qMzLwg8jNXBSBUr-f_lxNpcprN3gPIWFRRfh0Ctj7zi4lrOuvG2IKT5Lml2JzxIGTQKX2D3bsh7_N4Dab1QcOm07_aWoqQOkbgvut5Z5bvYmJ5xR6i4tp37GKSNTpMJpJ4mBmt0jQlHr7GpOZZlHEf7HHuY7CjUOjRtm4Wd-1YbspyoMHJPywPZgFmYYMEeNRUzzEvjJKiI2ai-vZh5OIXK7v2PRfljaqohkWFRlbS7pREE2cvwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKg2UDVdGVF5vQRMhutRBGCFPdMBK0mhKIY6PXVp9rk-dD0sSQfx_MdUbzX8QYZ2s87omyDIDdkdXlbeQFTc2qMMEXEsdR741jg8YGqZDT2dVyKZJQWepi6fbW3VZLZk0eXsKwM7Ldw5F4bfyZglkqU4-cDQ7gguiN0IAtb7Hd4q3_xz-XtZ69tPvkLNqhjIz38xBGxFSBV7QFSWbasEuruMyrvpGHo1slqjcvSBy2JDoUuzLyJAidLxaNe_mAdqy8AzRMGWPICAXhcDJtXRWtsC4rlQLdngljzF8fIDRiJjChyyvkuGDJcNzhFnBCWjFhagox2CwUfWMN3csMQe5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27054">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2279080601.mp4?token=t5PUSeCDmF0iYF9CT760_4YACJp8f6JTMfmdoCBBytOieVYnvpdPJzeBs-9RUPo9Zg2HO96t5jY3kdCTWrR41jDG3jVfAJ7XQ1pAiZ_LXxXVdmXM7DnhcvwysX08qApE0_LjfywSqp2IYnsMiTy4v2CMAcl2PdHoA_hhiD7twNtom4AXZR9x45lNNjmwTjLjHhn6nJiJxgdquAJtaS6g6MUjJH91mhgMvOXuMIYZk0FBjW1Ef2R9WBZSGHdavmMPTEPtVB1sNDXLQjPN-LYbmas1gmaDT94Zs5d989p7mXggQW-rbDMsSJDdYfR1qoQyBpI79JhUSwSEA2dW5oziKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2279080601.mp4?token=t5PUSeCDmF0iYF9CT760_4YACJp8f6JTMfmdoCBBytOieVYnvpdPJzeBs-9RUPo9Zg2HO96t5jY3kdCTWrR41jDG3jVfAJ7XQ1pAiZ_LXxXVdmXM7DnhcvwysX08qApE0_LjfywSqp2IYnsMiTy4v2CMAcl2PdHoA_hhiD7twNtom4AXZR9x45lNNjmwTjLjHhn6nJiJxgdquAJtaS6g6MUjJH91mhgMvOXuMIYZk0FBjW1Ef2R9WBZSGHdavmMPTEPtVB1sNDXLQjPN-LYbmas1gmaDT94Zs5d989p7mXggQW-rbDMsSJDdYfR1qoQyBpI79JhUSwSEA2dW5oziKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقادحديث‌میرامینی‌ازشرایط‌سخت‌اقتصادی:
یه‌جوون‌چقدر باید کار کنه تا بتونه یه ماشین بخره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27054" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJJhWO6sbD--rzAjVxhgpTOD2T-N-CH28y-IQoyg3l0z03CaXgtAin9re432HROUba6C-ZVuegIqfDrsBIUt_nunG0Pz7cwQS0yvC1MD__FE2xUYjNuJNPQnqPv0t7ykv2_w6tGT1sWnn51qk_rO2oS_qyVu1CiarbMXhQU5d8JIs_iNUNnUPDHlmFz2NReGdYA-XYsFX267Py7OYIrL18YdmqZVyYSNTJa7ncC6yGYK0Mp9bP_0Ebj_qVc5zyE_0JOuWCiDcBFlzleUKLDkfppAcRKHXOnISKJDvcLzMf63UcotSlnBFRvSfQrjt3r3OJQ_kQpkHi-ZyMP3Ef983g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxOyoCUkFdi5XqO2dk1Ftr7HrnCbK0FNRU8vh-TfdYoTUggxbH8wfOL772VQBRe2ZrB_7yh-t87shY7iSmjuYst7usIPrznGTxF1jWXxKtP8ccqatxSMPRtcKseUbsHIWPgD3-klf7gKPiZswzfVXBC1Ic83LmTDBGvaefyiFzX17KckDO1o8n1ANN77Cb-QBRhV7hIzs3mzMUUtrdnVaOs2rS-RD_PiZ-remaS4D0P0Yrvwkn-d-_vlm2AFL9Rz7Jc2HeY7EfsD-PEirg5aMw9CoHh_grwxKLW8dUl1reHrYSGPVHJILHzA40VCeKeGuQfHlnXGw3UUsLA9zmc5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZpmensesyjeqf4Znx0TbdvkZ1C-1HY07EviDzVOPX4NQ6jen3B3410JRmJimCzUyb33h5RgR_gYjBH-IsqZP_n5MrAwwyrkcQ1sUoUcKIO7gRybb0e7ExxEE2nvHcGbUFvfzQ5KWQzl1UrZ8pQiL5ZwRnCV0OGgqx9wxQOuBsY6_M6iQVTteIQuMEiZQ_OcrwS4yo6AC0iEh7g26nX1_XGQOge01T4uWn0lrVma8SHwh_fXUJuVuxUe8k7YYJ2dP-LV9kmscwnX4gEr-LnNSTed9WZwmM60WVUggh0VDFPK-7laCPmr8kPXwRjM7cbfCGlmrwZhk43BgR56Zm4-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk_jVWoWZYG6bvFSZDq1RKpTiLNhX1HuV0zzmTH7ApYvA_8TUwZ_vnemWDU-nEY04axJQnyb-TzXkpl4CXx-VLssUdH8fL1AkO5Vm9W4aTAC9CJPMr1mXFPjkxPApiGDnOGlyurKzelrQ22_1AAZN2rfp2SrJtw9SOOeP5lnxCVph-fugAOebyPhHTRLFZMPcdGgNtXuiwzd4-ksz4xbvas_KBFQ1yg1KyOeQ9FoG7iwwj0vJXA517Mw4ownNSfb--Zwf5I3LnCD1GeAKBHLr9uUCNc7QW48U1T_LXQLiFb0bviYnWKxVsz45BDpEq8ZBKrJHtd-gih3DG-o3rlAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3LHHRMjJf46MfPYWGHMJ9KKSuOw1TblrmAWVih2BJzu9jVdcCkWf70T3q2ZSDiVZXDPmFVbRecjivFVF-Wr-uCYZ4373CKB8gMwg6yCC4MOFOs95bddzdlb1GuKG1KK6GxsuuCGnt7nPWJaHtOcS4sNB2Ko2x4Pjbn1eo_4DgnlN-ZV84WDoorpOR7WPLG3Q84_tN75mPCPZQ6q1p0OE5jKHgi7-LKmZ5krFech9r-UQxzVHmEbMgjX_8GINRCdnN4hx_2XEXfQRkflcjbZLja1O_4S-nkLUB33WFETHK3kK4gsMbc6u2Aiey7xvluRYFwxSDhYPnmm7VNtaXKPhD9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3LHHRMjJf46MfPYWGHMJ9KKSuOw1TblrmAWVih2BJzu9jVdcCkWf70T3q2ZSDiVZXDPmFVbRecjivFVF-Wr-uCYZ4373CKB8gMwg6yCC4MOFOs95bddzdlb1GuKG1KK6GxsuuCGnt7nPWJaHtOcS4sNB2Ko2x4Pjbn1eo_4DgnlN-ZV84WDoorpOR7WPLG3Q84_tN75mPCPZQ6q1p0OE5jKHgi7-LKmZ5krFech9r-UQxzVHmEbMgjX_8GINRCdnN4hx_2XEXfQRkflcjbZLja1O_4S-nkLUB33WFETHK3kK4gsMbc6u2Aiey7xvluRYFwxSDhYPnmm7VNtaXKPhD9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇷
#تقویم؛ 9 سال پیش در چنین روزی؛ PSG نیمار را با مبلغ 222 میلیون یورو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCBBui21jp1nxhCcCkcnXdiB00tRw2nwzfMzDxdi5qn1j1XriR8Ws6O9PdzWzCYrkPvGHknMY-lwhpkDOLynaPK-Dn-3uRmvgKHdnjFdFIrNVPw_X-ymlb4tv2o_dwWNANoefhVCbJ9t6phmG1XLd6JFjz67pB-QQqQfZ9NRBAzkI-AS3rumHrtnUpDyutDAgN27-a-1QMxdWrZxc_dz_02eUjPut6cvsQDS20AKQdcOw7ZkJH8Tz3KHm3u-t_uBfhbczRPq2xTSR5LJ5gWOt6xGtoifO92KRYGr0Qk7NvdAmEUmElO0Od_uoorX-whALBFykqXYcKoSO-3mSQyOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUkScpofzAA43DW5HoHF_4bQtsAP_Zxpgc8dxrmoBeKTxOgI_72lMnXHiK9rvzl_8mT2soY9T-ZJRGIa4TQl5hLTQEcC5nfbyBqbWEXk6RKda06U_WOrs6llrDZ12KXxRiV_DbsdCsV-VNILsEzl4SPMqAjAt-d5K3NXVJPHTN2bXM6NDlw2FQzNuFBfrOk4OMA5UVvh7dl7HE00VHuvqptFqhTzu5l1hDRIgruSNibI4iHnOxqt6cWQPHPzsaE8hySK-ddaGVQi2C_sKtDuVzFylD9B_bUBE1rLGeJNwhR8BW26FT5SoheCiC_HMApyy_9gCwtv2cqdIRz1OZmeFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ha6IOczGsoGF9LELq3tvcfPEXMiLb6LU_65Vz0zIn5xoC2CrguJUTn77c_eZXZTNZN-o2M4WZLXyTZzYvWbYaaetdGEudzWN8k7J97qeo7DrUccy8IElZRLJXVQH-2fS56P9FO2gv8GGjZ5FM4jk1usnTB_ewLDhs9zq5Fkx9HAAODwfi4SeYWLN1wQFGGOuP4n0a0bXVgWru_m-aQicwAvmlD6wqcG8aNS4sNIjlj0yoDmPXnLA-goGVmzQGPjEK0fbvsA876icc47WT-CGD6XdVvXeWtPHhH9MA8vbzfWyjK-nWDSUw3a1wVo5ReqWSOSu37CkdTNQqgOvy-idBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7821302722.mp4?token=X00tv6W6XF2XtPaadCPUybRCitd6l7CfC29sV2eRw-6iRHdSeBrTHFzORCPAnLEr01MCzWzKmYV4-G4aHNg6jjEo4QTE5FpVCTyHFps3hGV1gRjzKSjr4pF72JHztESQJwk8q8HqxD4wtcZXeQEFA0CI4vB1R0HBQRfiqfwQOYMnf2mAPYWHmmWdoeAfodqJEObGg7XOAYCafGUZxiXiViWhL3lnLkjGLJJpLJtR1hzjCYM9OFxml_9o0qXBm5wmz0faBaSTzrycaD60G5BIkaYw-hi-hTPGLjcFA9cYKqWOXS_bZWQHYEKYrgx25wJfLII5t6o0CQTnBu6tsoP41Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7821302722.mp4?token=X00tv6W6XF2XtPaadCPUybRCitd6l7CfC29sV2eRw-6iRHdSeBrTHFzORCPAnLEr01MCzWzKmYV4-G4aHNg6jjEo4QTE5FpVCTyHFps3hGV1gRjzKSjr4pF72JHztESQJwk8q8HqxD4wtcZXeQEFA0CI4vB1R0HBQRfiqfwQOYMnf2mAPYWHmmWdoeAfodqJEObGg7XOAYCafGUZxiXiViWhL3lnLkjGLJJpLJtR1hzjCYM9OFxml_9o0qXBm5wmz0faBaSTzrycaD60G5BIkaYw-hi-hTPGLjcFA9cYKqWOXS_bZWQHYEKYrgx25wJfLII5t6o0CQTnBu6tsoP41Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی‌خاطره‌انگیز از شوتای‌ فوق‌سنگین و برگ ریزون کریس‌رونالدو در دوران‌حضور در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8KLeZETDj-aqAdCR-Rp6dtGaNusTnBO9lH3JoMnMV54LEbbhWRUA10ZTGgB6kkBqMo_s_emOe9pMBhqNFmNqjtr_lgWx6cvVdkuh8oZ2C0xFG5vA4bUuluVeplXNjdOp7pYdVAbHZ6sOPbTzz3ucqcXk5lYey531AYaAx_TEumpMvgMOBpF3uYckOxlbkhas0I4twsHQqhBXp3lOTLMQW4YD6GGsC7GBEdKKZN1-c7r6cn8oJ28R0QiwakC0l4hdZYr_uxNym2HeH1M2V0iHqOWB5MxC9I7VB8whHFQmFqRWVsC0DOlfdIUZNDfIj66HBzfGYY1jBybYJQmJn6Bxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ62Mu215Je0cxsdDESfmKtpNyvONMxVs5sGfdfGT3nRlaK43qdKaJJebQbylDrx417l4EeCw6CnZ8cR9LHfq930KsZLoYopRLCbhBESwGlXK62e44CEt05Ih-FB5-TaDzgZnTOfq0Ukx74D4BttLz-ohoflrT0wFmsKVm7gv_vvjWIP5cUQem76iuLNxBR2DEsARI5EerGO5VqF_7oJwv3AgJPiYDSvPCnyaVgkIbECY-neZH5UfbFkUiGDqx5oPRCSAf1G6pCa6w3aXjmMhjUhYZDCniWjheqcrRCFrxQcrNA0FjuaOEb87tOLf7dXH68-WdLwjDDqc87sK9-Ukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoIx3lVwybR7hZoHHIZ6tPlDgS2WrZHGrDRR5eMkHT6yJatPyuLaqQZX4RWEiPtm_woMLgZRsD8rbFlF3wgxKv8OV26-RRU6uqSz4Tb7Dv3YUagsNMXG8CijEiqQkVcBwDyhPpiIv-xMSJo-WJiFsg5jKcx_hKuc7YLzOka4kzfynZpJSdc7hRkihEEe6qdKiUJF3z98ehrAQinB-DMWEOOAGhSfeJ2kDyrkh6rsrUTYIPzeKuAQ5UVmvNPKT2joFBS5iljit_BkxKvmUIrQ4C3SLVfVVoJVntWNpR6bP6VPpnUfL1qyPnP6sC71I-Foi3vVOz80LZOGxZoJL3UcAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoyQV9LAY9TeQ5T0aowT98YtO31tt8SA5OosrRTJCbTx9dh4Bb0wOhjOLC_XZA4_mRWDcCcmCP1AoT0CArtxz0m3ckLsJToltm_ipGQcw4ynlyeJ7CVTbZ4L0lKQuYobvuM4T5_71S9Z-0XAgSCl1cxOUwwO7t_kI1tLFiT0bihEHIiwTHBC9V1WVAlcTv9L_9S7jbXRqDc0CZJrQPsc1DS5hxmhvAFQ0PDYsrF1XeU95Enbx-JSNA27mB1N6ZRmHkJnR5Ri5bnXHJA0ecjJ-klGPO9LvkY4r9Igaqqrvh5ILmxsIXMfKY9svgze6uUak9z4RkakcOfOXZEwLCWOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTBOSvkVqLQRBNqfU7-3zwfo3Vshoepc9-7zuSzHVZYuAk8CMulS2OnmXTxiDc2KumNY-zM1ztKJwTorFQcTaEcOikcnkE4qv2ao8GOFwqz78fyhLzUkhscxbYdKD2tkN_OlOj8r48wX1COMfQcS0GNcYPxhR8Co3sUPDR37EIIvxKiUM_n2JBtfCr_UoWWHSEfYCWU3149LV_Wb3vAM__uHu40024icbzxI20Z4gXdzRzm6abfgXuyyWyUf4j1LxEt90zyZmVKUCAahxjPVuEJLLXoh4qmIRVjVkd_FBFBkJLaBj6Tw9LU3Nlfa698NKtpXhzsWC_qU5VP_DMFgcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWTbzckt2fej3inhqA-6R-nQIiMobPrdU5LusH2UAyRn8pITn56ZSkbAyOuPhxbVIpLjKlqUnPmudhhIMdRLdVHZ8JxVjB7qG9zywa5gldZaSb0cFR6LtOhrhLTqS0KFlEqRJDQcF4onx2Yy0RBsZDlBHhT3BnhlP1FJAFBqWEZvwzl1OhX8_k4A-VjtDjshw_w7SABY3rDDXCFlK5tWnXgkQgnUJbb_ZPMDdQ1ze8ob4kcxGPpmI-5LNBskX4j7vlGQmbTE9vyvlmFOHyPjkfQ4Miho2zJSNLdBvtQjxz8EiLqgiVGZzlPr7McJxYzJJsCaeJ0QAYSRNAK1dNsEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8H5iAwFyCucB6k6pJovo5G5QV2hU33xEwgrVsW8LZSwFFXkttww7j_VhuxzMzRMF8AliGyyFaOICB7AwfzsngQahV3jRnOw2LFBBe9YthQ5UMEOy0PMxk_s3G5cKUwmTJC8yEWATiokmkujsPoFDJFWKvsjrtqOQyPd7-NS4QtvnEAA52F4hbzBcm-g5oDw_h9SrlCWVj3_e2jYbtj5tfwbi-P2KDFnxnPfiQCIHLMwHGHrhBp4Y0KsiZReR5K6q_zITmXuxE31jHOCLxnuH6SoifXdyfWaY99tpKT7ehQTgj4G0o2oocEu7-odP98BqinwgR1KjA_uR6by5Lt3nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anaZV3MegFD1WyyDX7h9ZlotzXc5bnafmapsfjVswptUefPlS1rvSN7h09m6Fyy0bnZqj2A3Xg7-McXAlv7DOHAKWiBlAtkgSj0mYJpE6wdwrufKOw7y9nIdZEGGITnkDD9OBMZ_V-OjfJNXeh5-53G1Sb0PaveerNT06CRYQvlGmx_eY4rExaM57IMg6xAJ_2qVIQZzslY-AZq_TT2endyFLEHqRYqMUOfzMVkSbgLyJPYFCfv1WLpFcqtRidtPjS3eTsa_D9LCd6Q_8K_phqQCWhWLg0KR1Uf0arn0oUOofXOWWw82jkAiIUmGniDQ1k8EHiaXd80mOIAMwGdYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27034">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=bpnGYyT2rvXtL8_UkbKEREbB__hEIke1sJpczbhjM3cYChTN9IFzUZ6RKXyLkwhcn2yDq16up966TVG5IWy06CFuzeCSRgstBW-rns0VAxCWpNQxOd8CNkhcUpAx1PYCDGPNx318QiiB7umaP6lxpV91pZEQFwp07BPNPx65LtlcZHtMmqeG9Idlk3jENuA8pN7NMdwaJHUBrKFra6-D67QIWnTfIreuoufPg86E9AE70zWU3C4tnb-Sc_Vw7SOP1ogwzeRw_-INEdRX-0XoK-QE4bg9q8wROvfkINBDpaNMowUejNkFy736E56fLu92yLjgxHsdg3mDfv2a2yCTyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=bpnGYyT2rvXtL8_UkbKEREbB__hEIke1sJpczbhjM3cYChTN9IFzUZ6RKXyLkwhcn2yDq16up966TVG5IWy06CFuzeCSRgstBW-rns0VAxCWpNQxOd8CNkhcUpAx1PYCDGPNx318QiiB7umaP6lxpV91pZEQFwp07BPNPx65LtlcZHtMmqeG9Idlk3jENuA8pN7NMdwaJHUBrKFra6-D67QIWnTfIreuoufPg86E9AE70zWU3C4tnb-Sc_Vw7SOP1ogwzeRw_-INEdRX-0XoK-QE4bg9q8wROvfkINBDpaNMowUejNkFy736E56fLu92yLjgxHsdg3mDfv2a2yCTyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27034" target="_blank">📅 09:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27033">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371eeda394.mp4?token=WjVz1Nj4ylJGVr9I9V9ZWd1CC6_Z-5MrElS2ju58rk7kQaBBLjjdUrztfhUnR9QzL6Agn_qgRWHgDP4IotKTRwZFtLnez9uLXT9c7LFY1vbFlOTTOSu_8MdsE6a79cICsCUHn4uCbXK3tJ52hxrOG1_iKpHZg10jvUnKsxObjmr6HZF933if_xjQTr2tcAfRzwWgeuTnGUy9qUPtV2LfPSVrLxKNZb6VtLsFepjk4RD8hNIJPJaLn0iUK4r13pL3VrRLebWkBeB4GK45bVqa22eU9gMQZZQQsSDWJm4_IvbZ_ofxt_VDWf2CD_Oia8CnNB41otlFT4q33Nmzu9cc2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371eeda394.mp4?token=WjVz1Nj4ylJGVr9I9V9ZWd1CC6_Z-5MrElS2ju58rk7kQaBBLjjdUrztfhUnR9QzL6Agn_qgRWHgDP4IotKTRwZFtLnez9uLXT9c7LFY1vbFlOTTOSu_8MdsE6a79cICsCUHn4uCbXK3tJ52hxrOG1_iKpHZg10jvUnKsxObjmr6HZF933if_xjQTr2tcAfRzwWgeuTnGUy9qUPtV2LfPSVrLxKNZb6VtLsFepjk4RD8hNIJPJaLn0iUK4r13pL3VrRLebWkBeB4GK45bVqa22eU9gMQZZQQsSDWJm4_IvbZ_ofxt_VDWf2CD_Oia8CnNB41otlFT4q33Nmzu9cc2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
آرتور ویدال ستاره شیلیایی سابق یوونتوس یکی ازبهترین‌ پنالتی‌ زن‌های تاریخ. ببینید چجوری میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27033" target="_blank">📅 09:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugiSKSIEpe5dEivzca-eOLcgIgrbn6QV3pE4_mXh7LOSQ9KueFps3hEo4BfBLb3bYmjvhnJlfcMRBLXOPHIg3X9gS4NK0UaU9RJ9Z9y58iG-yjIvcic0g-iiAohWTkNy1FLXg1sGH5VEUzP826y4WWe0xNxYc1JOFs-IaXCi-p8tBes_U72uhYX_2IugmrmtDv6Ns81T0nZ4Zahq5eZMu5tlj62ZpiDRhM-eWgXPCr-Q_DdpLj7F_HcqxEO2UceBTeksHFTIf-W3AGy29AXfNMePGYyLmtNOy5YxEUls51E3D_LZb3dkxGSfV4bHS5kly1rl-Zw81Foxr1vigGOLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=t9Qp8EgsqHjcZ4VRL-wFZzOAk6gMnsIJJB0Ka8pnTcJlQGxrcZrB7BtPwN5bAsTVdbwPI12To05M-219k-2oqW7V2-_k9ELiaPNYkahM7SIMRu-K_qMG9UMh-GS9dWnhqAly8cW7HHXOvi7KAZlTxTmwB2XwjhJakmn7IcXLdAqxY-u2qTUIM3ijHY-yCj_e-va62or383jYm9q9OVcMv3VQ3bcOO2NoQrbViNuJW013zkN-nhLUbBnLYN8sKSE_w3S5NTA9DrlWVUykfNrPd6Ykzyrxv7ENd8WGGcgE6cynOZLN7Ejq8iYglNvRJv0Vw7xbBkgvCpKlVEhJVEDb2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=t9Qp8EgsqHjcZ4VRL-wFZzOAk6gMnsIJJB0Ka8pnTcJlQGxrcZrB7BtPwN5bAsTVdbwPI12To05M-219k-2oqW7V2-_k9ELiaPNYkahM7SIMRu-K_qMG9UMh-GS9dWnhqAly8cW7HHXOvi7KAZlTxTmwB2XwjhJakmn7IcXLdAqxY-u2qTUIM3ijHY-yCj_e-va62or383jYm9q9OVcMv3VQ3bcOO2NoQrbViNuJW013zkN-nhLUbBnLYN8sKSE_w3S5NTA9DrlWVUykfNrPd6Ykzyrxv7ENd8WGGcgE6cynOZLN7Ejq8iYglNvRJv0Vw7xbBkgvCpKlVEhJVEDb2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyv9RnXD91cszJY0SBQ6JW6_47ANPqXTfaW_uZxBaXLC4daPHlQFmCfTr85a9wL_OtShAF1hEVauN8iLd15Hlf9uguT6dMePvzj-pjhox0wxv0oRIBEfNU2A5vITfi7cq6hytCKBCr_x5ED1m-4-cXVrR68iMF-lXfWGPpdU_R37ZANaVShvgGM8YNMmmebS_AClOl9aUAslJndrZg3tFgQBSgwqlGc-Xb9FIfBrvIFc1feGoppLP7dqGprc8T_2XdLrkVQjM26YDxdExw6enx4ilbL6D5crXoTr2_3Btzmk2GFO6EnvxIRdg986JvH4KkiuOo7B8PJvevvqbQAHmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWyqrY4PmwJWnPVohYIDpPRV6DplonjkXprBs_SRJIxqJhKnD8tqEKAbmUfNnNhTHPF9hxdK6GWYA01MA7ZHy2NCwBxxrqIKQrL_alWu-6mWLeCAN6ESGDtUQQqNlyLsGG9D2VyB2ovkdM-Vypsoythabsld6A-Dhm4pncsjdfD5E_h3-vr8jA36bMmXfPVkjJlQ_lBeejRjMdqnsB0dJWbysC2Y02B-3NTCeN7Ncb7WkR0f01Ukmc3HL87ps86-46L4nXpBSDjxXiQddWB5JMe_b7tn6c032570NdD_HyZcsj4sNDqT_Vq3X7G95j9gz_82mtZ2ccXcAfrNyzTa2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quhPYp44cv6KzqHKLZrbUM2-paTV7J8tyZc6VUAiKLqwUtvf3OT0gT2IINKCc5vKpmgHrHMTkT3Z_Omf-CP5ak_naKcLQayYUUzTHaaTs2W7bm19nkifuZSd4P47A-Dl3xWVXw9SuaAgeZqwHz0yshA1o1M3WqbR2OG78vcfRZ_KcBtmq-TrKAJhJWs5Go8BRrtDsLIJ-QwK_hCD5rp5NuYgCL7zh2tMQ6s2IPkeuPj25-91p9_H_uwRRNKIY2s6-PMRzMQocz-1xT_LmCpXcQ8fHqrSF8QuiREDCWEV0kdTotQwjOgtpY044nJtAFk62lNvKZ6AIwz3JhGfnsG6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27026">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4oSDRE5Z7SUqfI1nztZ3ULoJpQhV_eAl72sOAJHJag_-CovgxPdsVO9UzCZnX4Lj6Nh3XECyzfnBgJIvpmFqyo80vBvmkCmgfmH6uk_FCXdztfiH2GlBJFAUfsH23Ne9GSB9PgNX8ZGSmEb6m8cswXUFnFFXFbtyMASEeO_w9bI70_xvlRKo6jpR3al533bEBMqlncjzpBbihYKgkPI_ZJk9wqVJzHk0eSs-nGVlvvVrIoZTjuDpVlYCsDu7-l_fJcvb8aZ558PMn-LyvVp6V6TX91GFbmqAgBTEhHqVGqWYsGTHZkknDc9UeyIPyO3TlMP1FS1GRWVDUtmpzMPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شروع‌رویایی‌پرسپولیس‌ِ تارتار در پیش فصل؛ پنج مسابقه، پنج‌پیروزی، پنج کلین‌شیت؛ امروز هم باشش گل تیم ترکیه‌ای ارزروم رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27026" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27025">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMEystyDQF4uLLBu_kgkRkQyNpLCcFQ1Ip5QeWQXOPFjH5LqqVGmOuOYQ6-RQ0BM6S1z3p8bUGXIcTaAvaNDynBIKODXD_lF7ZVX5BRnc5jahadVaQDoxssIBcePt0qaOT7Qjf7JOgzK6Xfc9JoCNiRX1M7xr8nF5UiBwErn3hHqzAj8IVKw5x8Nk0JeQjBqfolDhON2Lm94KUmTVACz-aEEN-OZ4haN6OCo_hwPVNozr8ZIbEh839zuB46eZfr9zihqAEIQ_uMEQtveIb3KJqQGuNm4TzjRwfbZyWBZBE_UBgfUHrNaGpqIrH2g4W7ovyOWUbcti0KpNgSG1cHzag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
الهلال برای جذب رایان، استعداد ۱۹ ساله برزیلی باشگاه بورنموث و تیم‌ملی‌برزیل آماده آغاز مذاکرات شده و این انتقال را بعنوان جانشین احتمالی مالکوم دنبال‌میکند. رایان جوان یکی‌از استعدادهای آینده‌دار فوتبال برزیل به شمار میرود و درسال ۲۰۲۶ باانتقالی به ارزش ۳۵ میلیون یورو راهی تیم بورنموث شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27025" target="_blank">📅 23:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27024">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-M9VqzwhmKtF30A9WsJzUTBV3HJccaGRqKCaE6ppyPFfR7ZAPm5sVOgPC89y6PZ_3Y3YxJAgkI8dVU7yTpDkLhiuhZ7CIZRch6MEERCsZEGbg5trVomNSmDVd8CzGAtP3PBnnMddafk90HeA23aBoLRFcBrVpUaudjjfmF04_B_m7EyG31K_smyGX4HdDJXN8G45Lw9PSFw2PuD22OlSAdn42AtvKTrRTw8crGMG8Lxq79a_iyWmpC2OYWx11N3uBMHfQFWcB_vYUTPqzW5Eap0UPHh9GZlsbu1rdmpeiCQDi4eUerkeT5u_MJyk5dimNtBRnJll-tqKn0Ak9xCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ پیمان‌حدادی‌مدیرعامل‌پرسپولیس فردا بامدیریت باشگاه فولاد خوزستان جلسه خواهد داشت تا آخرین تلاش‌های خود را برای متقاعد کردن فولادی‌ها برای‌فروش ابوالفضل رزاق پور ستاره چپ پای این تیم به کار ببرد. گزینه دوم امیر جعفریه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27024" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27023">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYtLVM3v9a3nS0k6ST-8CWvIDfP75lJ4Ps29MT-7DQWLD7Gh5VVJqoUDdt092dw7MAuXv4ce16oTKKuj2GbCpFYYBml1cbeML4iGAs9Zuk9utbBZ887ds6agoRkXXuFNQkgAUhXqK6DkLCcTxLR5kpYFInHk1s_8Nqw-mOa4Awnwz-w3nfACYM9HlId6wbrQSjANydvk9jiPNuH5AAcOf0-TwJOe4nr8guxGV3RgBvAnT8APcp5wZ97BQWRu1-eDToDHH-jCxOEaXnJlZMJLc2SHkZ7pgmmzjAthZ-sy9Dt-Y6Z46Rnzdix_bCGEZzZ3V3gnFsehIwsQMmFYYVB3Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27023" target="_blank">📅 22:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27022">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdoOQX64JYltms-Pvcz22orR2rzMVmBWXdc3U4mt0e1alqLMoTYG4sZdzP1RvKHAJ3Q4DQNffGzWNiFdXbSse8hW00mNNRoXLAjsgRgMSxOk3ifVqPT1CIh7hdlWjUKi1Pn5kkzHan4oySBfSC5A9G-pxkvyLNpdXhqZI4lEGidjYyREO0ZlmSzHwKQLAiFhJT-SMMcCIiDlU61Nq-bwkEpxhrIsU9IXoXkV7bgJu5BBY-F25pGbU_oY9GjHwcnF0MmYGd8VDGef4BQytesP629CyiKJW3NUqmuxyoMjk8nBRP1ntPZKQdFlVg5-X9hwZ4xt-iLmDM2SSPqC62dMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27022" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27021">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqZDw918GbEokAxfpPJNAcz2smvXC5aY4qNuvJrSFm0P13F1ZiswVEUlDlsgvW-3dm2v97m7j0LinsCvMauRpazWqpYcAqiCAFZ5tSX3yj8SpgwKA0CVvGrzCAtBCPVAa1DCcthLUkIDWtHCwIK8LSCcWZPzAM16nOzHtMDamwNUXS7_hc6pduWvT0JDSov71T9Y5ihDkmLjI3ma3wl_FSv7dpA6A7vGufR79DHK6CdOpcYUAiO_IR4rWP0F1GiQjCgPjRyA-4_MTMepkQQSd4RBZT-1sGMKNpOZf1A8rr-zKZj_FkaiXWMepKzw4WbNAVWCiyVbl3wvXDh3KivLLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27021" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27020">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4mFCgAWA213JdT5lqHwS9VHC5Wly6AXh9pBARramyXfBKAPJCUvH6TYKBfSZcApZXCrY_YCcUDoy40869-WWkZRd1YVcFzVyTnTu8SANbTwguJbAm0cQvP3EePUaIZ3ilxnEm8oj81UhUu6DvXPHBPbg8qKHLC3AUPJpOSeuCgqUUKEzbWVbFP3lovGJBzCHZQXuBO80TJp62uFhMw1d_ZgYc_ZYrZnnr6TaCo2adM3Jm-1urnpRJz1HhigPIzwv43NxnT-cJjDUyFU2zMw4e0SelC6htMlEukxFjvY8EVwNktlh7rByG0u5VIvc2vtrXtwA6B86_bTWE_OgO_cIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/27020" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27019">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=Dlp9oEC1A6Wdwgkqlk3afI0Mkk4jLAeGjF4-CJ3PxW8yepFLz7AuHejjboxtX9bLLMycrQlRA-eqPQkUkxtljGCN5KQ-zZSOIeSf2P8iGcFcW_HzjrkUdmfClvUnXiT8vKei1K7wwmUco4ep21ejj71IrcPYKdiey2xMbELQ6XNpgjl8c3CcJVcz9224lH6LKKwOI2CAUM0prlVY5acougcaCg783QcGF27sUjvl_ox6dD408-MggOUMhNfhNbnAa8cNJJsCEF1dwiAxhY5g_vI6JOAk_blkVCfrvEkDPnyg2rEmG_7jbYKaAlVP5Kx9P95pxgf1-1awFImB3wsBHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=Dlp9oEC1A6Wdwgkqlk3afI0Mkk4jLAeGjF4-CJ3PxW8yepFLz7AuHejjboxtX9bLLMycrQlRA-eqPQkUkxtljGCN5KQ-zZSOIeSf2P8iGcFcW_HzjrkUdmfClvUnXiT8vKei1K7wwmUco4ep21ejj71IrcPYKdiey2xMbELQ6XNpgjl8c3CcJVcz9224lH6LKKwOI2CAUM0prlVY5acougcaCg783QcGF27sUjvl_ox6dD408-MggOUMhNfhNbnAa8cNJJsCEF1dwiAxhY5g_vI6JOAk_blkVCfrvEkDPnyg2rEmG_7jbYKaAlVP5Kx9P95pxgf1-1awFImB3wsBHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/27019" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27018">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4zXTmzjLiyRsKERqClaMYC2tTvJv1cqREN53Qfrm8o8gqPPVGiCn5WH4ocs52DFBah0J3WCfoiCfFvh7sFlwPmSJGSG2lBesETAgkjcP1O2s7acxGpgkTh7dguTEk2_Hf__Zacf0rdxDp74VKSwa8Ur72XpkCdTT8Dfm9etyLgG0BhPi29LCFKLo-EsWTpqPLiTs7Vk4-bDdKCVxhUlEF0_GCrzXIqDir4Qbdg68iY5BYJTvP5_aPj-CHrfc9mro_eMVErkYhCAWIX8ENCQKd8N97nkeIBtYbxm3Wj3_mBsyakhuj7dpJKSWTaKkw1lIaf2NuniDEnDqeNcnnsyAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه گل گهرسیرجان‌رقم‌رضایت‌نامه امیرجعفری مدافع چپ 24ساله‌این‌باشگاه رو 70 میلیارد تومان اعلام کرده است. مهدی تارتار بشدت دنبال جذب این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/27018" target="_blank">📅 20:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27016">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHLvI3yuXqoZjBuBQt0y0PLPU-4BMrcQ0CHVcZpBdpEowWpAdJAx7IbQQB0MIECQj_H4l_ETqY7i8oa2cCB_ua_EZLeYZ054gG31Kxt3YoOUFNaPkX1cj-SPHUl9CsFE2SQczPfiK-FGJZocLW9wmstdz6xb4kTCpn9nryD7iKyOHDLG8XyDLblr_RAvoMPLEJPROAMqaKXBaBKmqe7QRnv86p715vnB-Mck1yCdQGo1Ta-GfcpNbXikubZQHFQ_IHN2vJjb1EiPeCtavfhsEsrbdfEM8yR48bqtyZfFBBx2gPKlwU7_hSD7XHAYD8Cmj3WsSLjEnDNIbTYYOSjCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق صحبتی که با یکی از نزدیکان محمد جواد حسین‌نژاد داشتیم این‌بازیکن‌هم‌آمادگی خود را برای بازگشت به لیگ برتر اعلام کرده و به احتمال فراوان راهی یکی از دوتیم پرسپولیس یا استقلال میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/27016" target="_blank">📅 20:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27015">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1VQPS1SEopoBECCu5wzKB6HRozVSGKmAHk2z9uyu-xfbyXHcfUmE-oj_sV-iwa748oU_kZxQdiQsWiGwWJdanUpXrzQMtQfP-JMPRnhl4Pt4IW03UbXGGDJbv9AET3iI_ojWNLuPpcyfxzMTzqT0_sFNNZjCBUGQisqc3fPOmA0fJU9RPWQLbCjJrlGtVzAFH83RW2OjAcCoKqWNPmRSeDOWlNiP3Shh-t28r5YU9RJ2PIROVqiVaeMKbceEYV4j9N_lxexesxSWq_kARdhujSA_UAEz6hbcSMCtMDFHMS4Yz0_Xlxc0Hcpp4Of3XjeORa19L9d8vC-6lQP3P70mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو درحال‌آماده‌سازی مراسم ازدواج با جورجینا رودریگز برای هفته آینده در مادیرا است. این‌دونفر در کلیسای جامع فونچال رسما ازدواج خواهند کرد و سپس جشن‌ها برای مراسم پذیرایی بسیار خفن به هتل پنج‌ ستاره و لوکس ساوی پالاس منتقل می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/27015" target="_blank">📅 20:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27014">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4pL2UYAn_Q7BEjnfmgaJExKMighSfzZDjGnes5PKqPR5h_38uN0ZH2Ak5_-Hv8DQTms6y9uf1PxU6PlS9QLAmMYoPlniL79HbJWjhN3Ris68hFqcEkUnLytR0bnVigOF0moJ3NRrE_Fale4qEqmtSWkdiHNC2TNq2dVVhUEX_utjW0SjnsyUAVydNONpXnuOme5MlNptogKqPFifpeg6nfHg7-wUHwTKpBvfbhc7xPCEX2R9P2hbAasCzNlHNWadu2Adcs9GFk3qFo7r05I6sk3GfDvrl7DRKRm5_BkXo0bA2xDHje74ww8b8UPuYBiXzr0jBljDK3LoaA9tZtAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27014" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27012">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=M45OBv4_SFtBaA5VGFaGigqflMNe6aN5RjYMiStqAs7tnSuSOwUhNM3CabJEkuW31g7rM0ua3s7kbChMwrT2etZ0fcnIkgwXDrDauDxYm-svfuMyiY4QbU4ElciYScU95wKjYn2ryXE1t6hBvo_gTuta_nkDiJTFL_ZJii_MIaR1UU_PDUJlOrY1IeJ1s5cj1TPJL_xSnTceHyI2ZdZV3yG0Tb-PNFw42lYH8SgX6au8xG93bbEi8hKDS8k_4H9vZ6K9cb2CRV2jgj9pUerJWT6sjXPMJdY5Jc52WHrmwsPJ75UhL6sFtR0EaPcy9t747_ksy4LojekPbelL0k14vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=M45OBv4_SFtBaA5VGFaGigqflMNe6aN5RjYMiStqAs7tnSuSOwUhNM3CabJEkuW31g7rM0ua3s7kbChMwrT2etZ0fcnIkgwXDrDauDxYm-svfuMyiY4QbU4ElciYScU95wKjYn2ryXE1t6hBvo_gTuta_nkDiJTFL_ZJii_MIaR1UU_PDUJlOrY1IeJ1s5cj1TPJL_xSnTceHyI2ZdZV3yG0Tb-PNFw42lYH8SgX6au8xG93bbEi8hKDS8k_4H9vZ6K9cb2CRV2jgj9pUerJWT6sjXPMJdY5Jc52WHrmwsPJ75UhL6sFtR0EaPcy9t747_ksy4LojekPbelL0k14vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27012" target="_blank">📅 19:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27011">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKVDhhx11dBZXp4a1AprPM8-mPUmbImmW9W3Id3YQDqJXT49mtxvDh5e-FKR60vicb25y9MrRdR7-tHVvE2Jl7EOLabRopujt3ri7E2_WbvSRGMjHTi3uKjie2c9v6Up-8C9YKslzW1e_TRQZMuVDR6DdnrBY8vXJ3mx5CxqToLy6zrSgRTeHEIr2HRu1tP-8aI42btiSX7lu6_qZBllQb61oCuWqsLp8yD__LHa7dYiHNCwafjwAeM2jMN6shcNAP0gMhVt4J5nUXJFSRdTGWjph5sPYmQze9p3YbEdtD_8PFNJjSVTbTgY-hoMGaoaRaKsTNRXw6NG5CEge2StbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27011" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27010">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/png3T-phUE-Bhb2AmMF-B7383lWPSr0Xh1dXgVzsSHDmMKLjKa5pFY9MoLThF-kTEkX1ysMrQLyo7G1V8zSmAlL5aRZxt9Zh3x6DafhMNU9ppLB-Yjm8isobqzOYAeueSwmfw8fXRKAk8i_2zWz-lKbj4d7aJr0lbnH-SidMfBzQksbFI0cOQbK7Nks0Wud7OYzahob5D8t9NWQ9roWeaoUuOxGQ7yz4COiMYZaaZFDeAAXFwdy-mLs63pLvxjMjJerYLqdZh_rsQw1QoZR1Ltz_HySqe8bWRBX1FBD7YLn3t5SkpeJoQHr7MGxoiaVShEj_FKjmy09FA2n7L0QTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مریم ایراندوست سرمربی‌ سابق‌تیم‌بانوان ملوان عصر امروز با قرار دادی دو ساله سرمربی تیم بانوان استقلال‌شد حالا زهرا قنبری کاپیتان تیم پرسپولیس به مریم ایران دوست بابت سرمربی شدن تیم بانوان استقلال تبریک گفته و گفته خوش برگشتید انشالله فصل خوبی در باشگاه استقلال…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27010" target="_blank">📅 18:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27009">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX-YvU0_tWOinOq_XIJlFFBfxPou7HZPd5T5lixc4noHUCDjIsMxWnWC8kbS7XALY4_BNZZLBnhSmX8N3UpDpEIZ1aipZWW2I12dqM2Dd2CYWui3AUIKDFVZIkHEan8-gOybQAkikvKphfRFAzxyPzjbcEBxmgEKcehwXQec1-4_3Gr6uPZj3FWjyCo8xkB8IEq6EqO8Xc59wVXq9hs2EF9BNH09KhGxRRvLB0ZoI0NSGXs5XlHF59DJeCSeHd0qK1HgyEAvcjhiAvzpAP5B5MgZG__uQsrg4cUUxxCWEGYcQgAvwqObdCmNHzs107VGZr9PqLQf4eJ61ABOShlwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27009" target="_blank">📅 18:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27008">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
در فینال مسابقات لیگ ملت‌های والیبال لهستان تویه‌بازی‌سخت و نفسگیر موفق شد آمریکا رو 3_2 شکست بده و مجددا قهرمان این رقابت‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27008" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27007">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyCiCHecOijSEjYGKeHbei06zDv2OEFpRLRTXKJEiHq0zv1ed4hbajxqCj4A24fLsZyRd8KAGjwvFgBkfOigndynJDlhrIwLerhbsa_IxbFHrqoBYgCt6D11iYbz1MCwbcB1DwY-BayUoMK5QlvSfAvccfTXkJLTJB8HIAdxRVoVUlTgIVbPkwBYK4GytQREyUmbtjdS_pWDVof_PFtWHHq1JC9gsmXRTS6cECnL4UNx1o_GsuqfXpqZckc1vH6urvACe-vF4bNATz2UQPjaGEyLH0Ol7qANvEOe-9z7MoEo2dXgI25zmK7uUzm2XEgqTgcS3LMxu_FLZlktl6u48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رده‌بندی‌لیگ‌ملتهای والیبال؛ اسلوونی با شکست ژاپن به مقام‌سوم رسید. تیم ملی والیبال اسلوونی با پیروزی برابرژاپن دردیدار رده‌بندی‌لیگ ملت‌ها 2026 به مقام‌سومی و مدال برنز این مسابقات دست یافت تابرای نخستین بار روی سکوی این رقابت‌ها برود.
🏐
ژاپن
1️⃣
-
3️⃣
اسلوونی…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27007" target="_blank">📅 17:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27006">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=OULPJLREDEds7sFpBOEmNhTBPPC0ZozOt1XrilsMplNKYvB49pHqJl3wmQwVxyKFrkTVA2qaVatjp5pROAyOZGtGyowe11smi0w-dXff3iu0mcAe1Zk5stTQrnR6fH0_6J8lbMkDHdNJZKmKDu-SuJ5Dc7CoPk873aGdFySO9REpwkG8nF8iMWkGvWNf8TKPUv3yAqG8nfWpMigmXSjAXFSmk-cGnX7oke7aQ4NplnqSWnHhhTNxmk4BKkXeKVwlnvVqqNKTF5rmPawcp0l2-0Ve-JSNZfM0rpfdAtS9ce2gxic7xXFVl6XmF8q5ibnb7374BHdGJhBykXW8i_gP3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=OULPJLREDEds7sFpBOEmNhTBPPC0ZozOt1XrilsMplNKYvB49pHqJl3wmQwVxyKFrkTVA2qaVatjp5pROAyOZGtGyowe11smi0w-dXff3iu0mcAe1Zk5stTQrnR6fH0_6J8lbMkDHdNJZKmKDu-SuJ5Dc7CoPk873aGdFySO9REpwkG8nF8iMWkGvWNf8TKPUv3yAqG8nfWpMigmXSjAXFSmk-cGnX7oke7aQ4NplnqSWnHhhTNxmk4BKkXeKVwlnvVqqNKTF5rmPawcp0l2-0Ve-JSNZfM0rpfdAtS9ce2gxic7xXFVl6XmF8q5ibnb7374BHdGJhBykXW8i_gP3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27006" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27005">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpy5iAwOf7iQ9l59i21nQyCrdjRzV_yvWfRH8q09AGCLc7pC0bu4lyUzwdvKp6J0wU57WiqWuuWjMpSIPFqp37FRjpYHjunzTeZuYQNBpo-Ubjf2JWBxLVh5ARFKs3mU7WfmE64mRSXCqh9D2ytTaSHlC3wWVRt3PBMR78Pn5eK3eP3Hw_E2inenespGbJrGzH3lpOu4TZnzFubOVfr649o8fsXR5BqYxPsE6obqfJw3m-i1mL1Bmxymy0HqWvZ1PfVFMLvKF9oSxwE34lqhkXchFhJrnKmm-GvZvQgEUb3PkZUwlKeAQ9rDsvwKNiGr6ucUkYPw-STvkTPj_u2I_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27005" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27004">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSl7KEfHsa8uX1OP_oqTwQpD6Fvuzt55c7ccKDtnM9Jc-M4tKH5ZLitEo4SJsTzW5PLqKbcns0oU9Z7vOLy0hzdpt7FPKMXHJ7VM09-XkZYCXMhAy0JA4RARw_7o89dEzUVyYl230FrKruwhs8GH3jBXMfm6hZwxzXWnkH1P7H1tcIrePuK8cDqR1I0zGgizitG6uWFluHLYH2C18Wzkme5Jkqw_qxkbsbiMnmgXi4CfaFyvfWuepN8ZcMCNqbyET0W2GrwcnBx6ksKsxuigQPi94xMzmQ4q7Se_6SiXvowj94IxzSH48zoK6JoLEuaRDCV4u0CcX-HrJalrOTorQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27004" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27003">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLfmsd3Sqfta8joQiQN63S2kNoBGKjN2a5g9odxxLwyIjmOlviidIVeL0OeJZTkMbKodWn6ll1cf3zj8QyU6RWQJdMLrzX2QBj_bKtYdML8GTDS1H9_mFP7p02mq-oVZm3_0_EgzGE99diwua2elw2oqD0MafZNPYog83P4qbZfgeX92zV56PccGEZ_MwTrVipdBv06j4qBl6am73IHdrY3PxVj-JHGdyWJXtwid7WDtAKP4VNdiUkafo9uabSMFitm8KoVdmGOv-9rYO6RaTutz-LBc3Rcmn8vjRsh_y0GBD_hE-mqiRwDG3-yIxL8njff_TGTFfroCYASPbNyziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27003" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27002">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRIofRT1jVVw3IosRPw-sai64KARWmvTHINN3sm65bX4NUC_xqCjqDx1zcO_ynVRW-OYIkyWLIyBIKHAQTR-7W5pF1N3DkJhjTNgDSxa1waNMUjHVXuqPLQ9paiECF07cNliDpzqmIuOG1bhq0Sl9LVvY1XCzflRyICHC15RrgwCcrzbjFjn4QPQ8KRWlJmcYZEfxacPBiqG19ybBNl8WE7kN3UjOzyiOYvr8mnVqEEMxURxvjktIk8cwayGVYiEevo8p_NMjRjvESwsYmoHQu_uYxjVno7TewaANLRjKKWiRYColc7rNYkOQLlI3LEs2I6VZrbAaJh_lvEw2NSWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💰
گران‌قیمت‌ترین بازیکنان در فوتبال زنان
🥇
آلیسیا روسو - آرسنال ۱,۸۰۰,۰۰۰ یورو
🥈
خدیجه شاو - سیتی ۱,۳۰۰,۰۰۰ یورو
🥉
الکسیا پوتیاس - لندن سیتی ۱,۱۵۰,۰۰۰ یورو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27002" target="_blank">📅 15:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27001">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdfeCBod3q1UNz6lymrsnUiV932eh9svOQWC4YBiKQlv8SdWeVVsLSx-6Xs9DKKHMJJteRifFrc98GvdRKH4qNedneQ_eC0RbRWhxfSip53cKgjNVge1n8gDmBpN_jaKQ-PSsnj1Zl-KerUf70TzcnZDfgcxOUnjbgSjMRYCER1yQyP9zgq0GNsMhR-GL761cNdj3JFx1ik0KGBvgLLil-J-F8v1oUq8Ah8NpUxCpdQTvaJ-Ew8DKL_VBjU7Px7bxZ06eZZv8iNmCK-kpV83Q8rz3CFFlU3iN0_YmINU8y8MPZki7PsBBuJ0vzQgt-_S_TQx_l42voLCnx6FqFdppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27001" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27000">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qc_As31WNvr9jOSJaxbMxFA6T76HlGKn6wWCL7JED7Dj5PW0rfh0OGoma8WUtu1miiaaab7ETSgeCHVkLuM1bxxQz6dM4cQeA9WM3kkyQ2NBHId6T8Qk42vSQcYUzkJPSBAbFKBkHy1q2T6o9C5R0LT4UQ1r0a84HL6ps5Nyo3VvrYRJyJ886nVkYUXPh7IwPgAP-8lApePg1sijdHW5Wa7mTCzxff6mkHD8DZ8plcoeBVdBE8RaCMlKAOZ9J1RWdmiJlfjllekqx2rmZALpG3_AzVVyA2owcJxha5KGUZFEI49ZvOEq53OWTdiiNx5ev_84LSvvE8ra_JSL1eKIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27000" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26998">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqytHdfUEqSx3jtqk023-DFCcQfRP4cg984UIVp8MbDs1-OT_LtzwJk8u3VCNnU4H6KYibp-lVinuFENk2TEyUL2NUnHO-mdrCzl1kGJ0anBCgZQgCGG1vQcLLmPc492Re4KHpjoDrl7-FljkLVk9kVHWabgbdjsV9ySGv2fPlsrld0fFpClkWDUFyPJ2vyoAybVKPCP7cYHVRgvBSGpioVNYTju1qKElus6cazmLpZwZoU2r2t2U5LCfMA4VqPuK0U3dkOtzR1icvOPriZJQFMj5hQWveBaPyTloX6Ov0BBg5JvVUfty_0YGBIse5rNVDlj9Jud2er9pnIpZNTPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSIYbMXbEZBLlgkz-TuoS3zuMpQqTW2L85_UwiL9UgDclVBuyW7-T1uh8yTPvWYCzON3paHKK5KLf95kqGPyBf1_lR8B252GEhDSujPn9TiTdfxGNB6KmsvrFZy6h9-HVaFRdRsbHNDxmJOdbFeK59qYyPxQ7YLCqhBimcVKSYafLlOAf2dDpHxPJIk_WlzPbDkg91lD3dqAeHGOT-EdhJIRz-6ftumjPSh9a4otKYOWjm2IMlgPBFbPexM3TIMvGTeUbNiVilmCGeJxcTmV6wxgR4aVA-mRUNTOhS1rIzMNqyIDc2SzEzxPabGsY05_9xr27pCbBICKYVLPj4T-hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
کریس رونالدو و جورجینا میخوان‌؛ مراسم عروسی خود را بعد از مسابقات جام جهانی در جزایر مادیرا در شمال اقیانوس اطلس بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26998" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26997">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIPBw5_-1ELyqIRcyd9euKNnx7R0tJ5k7fDR6GD5c_CeHSo-mio-tvGkPXYnVRz5U2kJHQks_1bAaHWEcqpuZFCtUBAcXstxIb-TcbpSqfHznDpynfDzTyUtzgDIBYT4wOmfuQyMKOtwQb-gX-oBACUBwrJ7wgJjQKRtsWPprRFt_TVKa-LbpGXemodvYS_MFtaxTR7Lxl3hFZkgVhdQU9ecYvrstSBFag53q_c3_RhFPBlmHyJAgFTMUhDYKhlYWEqvz28H4HLwdh9970JeH6FzRD1wC_0E1wglKcU3IheKc4FoN0hdlwWrZlgAzSYKJfoy8MBFOZuQaVmt-JnpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اینم از توضیحات کوکوریا: خیلیا بخاطر مدل موهام منو مسخره میکنن اما دلیل بلند بودن موهام پسرمه که اوتیسم داره، این تنها راهیه که میتونه باباشو از بین بازیکنای دیگه تشخیص بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26997" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26996">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbQSqX9Fc_v3AkfMr5iPjuH3q4_T-IjcP_rZtfmt9jMqojbGiEnXKdJeA9wzc9dJ_nkRX3A38_ZKEAboHqhQWUUyDjs0lHzJ9MZcPppb-BNKYCC0-TV-bggEu3pKWh0nrJ-wzQlicaifajCVu4mxZkK8kUDg1D2GN235E8cTixnlqGOFF3xnsUeU-0NRLXeQay3iJYQAEUNSj-05blHl6D-5KABFOitbjEdu3fiVqlCccCnO45_pLe45n3mAH8mXrf7GgfVLsciCFJHz8qba90AklSgW7sP5CCrm5t_AOMOquZVMZ3zBVnQxkyWllPfYrtP8T_eIEnq4_96OqqHkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس‌نیشیموتو بازیکن تیم‌ملی‌والیبال ژاپن که باعث خنده خود او شد؛ یه لحظه تعادلش رو از دست داد. بازی فینال هم ساعت 15:00 شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26996" target="_blank">📅 13:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26995">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=LdPmuSlKursLdGy4jjGDCdmhcGaJV6Yg2RhkfNRhEPBD_3e2FppOIjdEacCUM-YBYcl4-SNirmdiQHxFl2Tar-NqrRTqiy2BPYtDSN1JOuCfrS7EOtFCtpfe66LifPrhh7TNMeXRX_g7IGcpZ1O55edrLZYHXoj1ezUB0iwcNrmPJfrNyYNs7EWWcJXCI1Vbml9fUNOCTVfW94cW4_ebaNzWle1k0cn6I8LdTCWFuk_TNzXcBqgfZNSIditEJwLz70QY9o-xRGCbR1LHkViFpVCSWDuYx_bN1kfEx_46qaP1oLoYgnh8ADuim2ioCJKfEerCIgGIrjWVwvQgxT-E8ATF4Ku_ZxF2VbZOQnWdQ6cs4c__KDZbC0PfWs2WRBEm2LVWE1myVUP9fJpXxrTUtU3ZBtcYiKiDVDuaupnRkAIdbNRASVIp_B83ZTNBhhHjMRZUzSdzSy54TZOX8uTyNeweS2cbjtr0YFNjuvttCB3BgBS-xg9YIZQg_o60E-Gr85OcUzzJO5Jws7cZap4Z7CLlqxOsNP45Ybkst_CRzvzQmYbV33yVQV9pv1G5Bg3R5SAtOIGznmUA5yD3AvmMVdK95CzqcKtYpiRs8U_p08rD9HMT7Akve1FYZjyfyjKina6xoPUVNCdRhjVQWPuSfzXrb-WModKlo3WMxtzQoZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=LdPmuSlKursLdGy4jjGDCdmhcGaJV6Yg2RhkfNRhEPBD_3e2FppOIjdEacCUM-YBYcl4-SNirmdiQHxFl2Tar-NqrRTqiy2BPYtDSN1JOuCfrS7EOtFCtpfe66LifPrhh7TNMeXRX_g7IGcpZ1O55edrLZYHXoj1ezUB0iwcNrmPJfrNyYNs7EWWcJXCI1Vbml9fUNOCTVfW94cW4_ebaNzWle1k0cn6I8LdTCWFuk_TNzXcBqgfZNSIditEJwLz70QY9o-xRGCbR1LHkViFpVCSWDuYx_bN1kfEx_46qaP1oLoYgnh8ADuim2ioCJKfEerCIgGIrjWVwvQgxT-E8ATF4Ku_ZxF2VbZOQnWdQ6cs4c__KDZbC0PfWs2WRBEm2LVWE1myVUP9fJpXxrTUtU3ZBtcYiKiDVDuaupnRkAIdbNRASVIp_B83ZTNBhhHjMRZUzSdzSy54TZOX8uTyNeweS2cbjtr0YFNjuvttCB3BgBS-xg9YIZQg_o60E-Gr85OcUzzJO5Jws7cZap4Z7CLlqxOsNP45Ybkst_CRzvzQmYbV33yVQV9pv1G5Bg3R5SAtOIGznmUA5yD3AvmMVdK95CzqcKtYpiRs8U_p08rD9HMT7Akve1FYZjyfyjKina6xoPUVNCdRhjVQWPuSfzXrb-WModKlo3WMxtzQoZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
۱۲ سال پیش در چنین روزی
؛ منچستر یونایتد و رئال‌مادرید درمیشیگان به مصاف‌هم رفتند که ۱۰۹,۳۱۸ تماشاگرشاهد این بازی بودند. این‌بازی هم چنان رکورددار بیشترین تماشاگر در طول تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26995" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26994">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=sQWEre6HC0XEBeVbHY7YGG1qFMJTYzbiZ5GQCkx1Iv5mBQDJ4T2t6BRP4-C_ZdI6owmUMiv1B4Kb_qih3Qt2eIk_5mg4fSC59KfiYV6MfMJC70OggAGYCE1hZ4bwDugZETRswBgcgBN9FYVfDXtDhzQx-BmRcRAV8yNhQg0CZ25PELBbx3nwzfLQpDA_5rf8pe8dQ-vrHcOxvFkVnIBXKYYH-ocNGNznAaoJXM3g6fcThMWZCpR14pc1n0-B_pXcHbMZFLn7F4OUQ6fn4ujy7dL-hNpo3-bKbo-aAj2dlzVeM7eUvHIIngdpnOF0SboqzzaSc6BA3IoYfVXgfHTG9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=sQWEre6HC0XEBeVbHY7YGG1qFMJTYzbiZ5GQCkx1Iv5mBQDJ4T2t6BRP4-C_ZdI6owmUMiv1B4Kb_qih3Qt2eIk_5mg4fSC59KfiYV6MfMJC70OggAGYCE1hZ4bwDugZETRswBgcgBN9FYVfDXtDhzQx-BmRcRAV8yNhQg0CZ25PELBbx3nwzfLQpDA_5rf8pe8dQ-vrHcOxvFkVnIBXKYYH-ocNGNznAaoJXM3g6fcThMWZCpR14pc1n0-B_pXcHbMZFLn7F4OUQ6fn4ujy7dL-hNpo3-bKbo-aAj2dlzVeM7eUvHIIngdpnOF0SboqzzaSc6BA3IoYfVXgfHTG9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
رسانه‌های‌ مراکشی: منیر الحدادی تاکنون دو آفر باشگاه‌های مراکشی، دو آفر باشگاه‌ های برزیلی و یک آفر باشگاه‌ های قطری رو به‌ دلیل پایین بودن رقم قرار دادش رد کرده است. بالاترین دستمزد رو باشگاه استقلال ایران به او میداد که فعلا راضی به بازگشت به ایران به…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26994" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26993">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1_MUq8EtezyAl8hVyLYcmEJPL0NrQIr-zhiaVCUA2cXRWlLFGqzcyEztzJqiB3O8lEMuizDDtJukBlaliqE2HWwwIZjrAAkp_CvrExDOHEf7p3q8ZCvxYUbGtMpOiNCEJqhW1qqqCikgSZWnAuwe7s1mPLZFMGQATrHT2v7yOtbS1XUjK-HheaAirhbfwjTYly09u-3t45I6zqqPKIeL4_2Ac50jkvhqoAcwbxtQDGmhegs7j4RdF8WD93JHJogaIAId8FC56czeSMHNo_S0kJ2obdErpuYIc_DQOoZ14CKWHWuNAALip7MDG8SP_ap7X2qsmRNzpxX99tvRSo00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دوران اسپانسرهای شرط‌بندی روی سینه پیراهن‌ های لیگ برتر انگلیس به پایان رسید. از فصل جدید، تیم‌های لیگ‌برتردیگر اجازه ندارند لوگوی شرکت‌های شرط‌ بندی را روی جلوی پیراهن مسابقه درج کنند. این‌قانون‌فقط شامل اسپانسرهای روی سینه است و سایر همکاری‌های تجاری همچنان مجاز خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26993" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26992">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOoM3MeDozRNfg_Z1uROZj-xiR8cC5mtQx2bdjl8N8c06pLMztXhGVLLJQET7lXCCxNbW5F21D3t31hFQ6L-xhXXP-L1Xfa4Jyt1fS0vT-A2sD6ZsX_KVy8K6XN_RBQxHw6FkMqlLj2GXRas-bseH721wvcWfKM8evJmfPLMr8GxvtgtKb969FjYanik3Lq690P6L_4dZfcFygQDfmL-84lNWEPURViCjAh3je5_x6yJv0uLiYmU_JUfIuYmmbDBJdS8xpzkEpbO2TX4an1VrsWdmbBGLuRhFdzP0Fq_iaB3u3lF4RTJzen0OBcqiLkxlTkIRPKlfmze-lrU--M7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
#تکمیلی؛بااعلام‌رسانه‌های اسپانیایی؛ فران تورس بزودی قراردادش رو با بارسا فسخ خواهد کرد و با عقد قراردادی چهار ساله راهی PSG میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26992" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26991">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LetbikPQybiUJmqhwqqGHIX8oHi-vzJ-jOfgXzEGjZmIDZWbHFGDYmLWj9tzmgbi7TPlkSheK9Y6X_oKVl3g0_E1NGmZNA3nG_9NZrLwPollOLojOy5xc9AUcC-Xflk94Fac9ZG1sGajsKEB5Z8GxcFGuzKdMC54nEbQMGAlg1Oo-sNyVoJ_t14_5RqKEhnbF1ZJA1k0W-i167uNrtbgiMVQXnEDzf2HohKccLCPddCf0G3XzAX2IIYhB52H_sBSEFylqjqpDmPxIq3t4Nd-_Eagfuv5gmjT2961l3N6sgM3MEX0XFL6sI2uHSwLfkECNCd8Kb2w4VeTizWoryUQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26991" target="_blank">📅 12:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26990">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHCKU6XVJUCHBSU1o8Hg-C9gd-_6fJCtO_Z5o4HpoEqqXLDdy2k4W_NouSA3cvXOCAgwmgwpUc5_XaERjSiWhS42kmmMbJfYjKUC8lW1REiS2QBvcRmsL-mUftV5aV3EQgOdHTuCkZNHrLl5qC5Vxl-yVb0fi83QY5TpLnMvW50ix850jbIEqTEA5qrdi_3MKM_0yB4o1_kVQxP2u46_cpPq_f4aA9_H4YcxUkRiOdbe9YpjjV2kzV0kPNhbAL_YeRI6fETIoG-EP44SfF8Yctc81kZ1ZT86Jqt2CcTk0b8OZkAgVF6lXBRNFvZl7nD3RNppozPgl4UgwFRvmhhvZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیج بارسا اومده صحنه سجده حمزه عبدالکریم بعد گلش‌رو استوری کرده و دقیقا تو همون استوری تبلیغات یه‌برند مشروبات الکلی رو هم انجام داده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26990" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
