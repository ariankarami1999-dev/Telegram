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
<img src="https://cdn4.telesco.pe/file/FHadioX0GrbajPg9EV7dJdGyH5-KIOqcUbiMhmHC9gRh-FTSQVeZpppE9G0ADWLYXehZKjpSzvcPxbKfmc3XtOCnSlFXsXfymYTJ9dE8Vw2B-x133CPALaBhHEZbuWXHUY4QMsAqDXPZ7EZrAgZMnmPotxeutskqHbQGtfORB7JQznGB9ny1NP2raqffJBLquzvqgFjt0WSN95jqPZm02TeGSQFvKv3vxPaPYHRoVxV26OT72x2qVakmigMh5tQHvbH2hLIvH_4-hGT2Cot9xAczd7v6_jJMi6tWyJ1jyvb-0dvXH8BNOo76MtUsNwEf4pj855Vg--OTEpVaqAn0gw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 18:14:17</div>
<hr>

<div class="tg-post" id="msg-675176">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvJPeB3ES3kMueCClvxNXDPCAdEMP3q05zDRwMBeA1kzjMaJXjnlhBTze6p4xksucjgn8rxu439dcLcZGUc9hm4tkPy8otecosaFbUQ4lFCFom0ar9Mk-Y_y7z3n3Dj56hvh2uXdTU49zrVp3kPjru5wGJ7-6QAp0_7GUyMAM6vSYbdcnhfktzodpj1HcM_7CDKdBSI06ivSy6QTvZ7QlgQKqkxPMMGwU02lAjEYwGwklc9Vv4yZLsUR0I6lmOGVXUi1zZFloKwj5saM6puFUxznmAu0KRRo4ygWYa6AkT2qeVO1Czo4VgRy61wAOngGZwSSArdxiOtjvndghcKQWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-XR8G3EIS2JNKOORUPM-bWDUxamLc1Yho1bmkMg7D4iZC7N2MdbHgL4ANiZD-qq6NRRk1N5J0xxV9XR8iZDOvrDQIFrA497P66sdnQceNLjH_r0uqAmLUxtNPlJyq43_uEMzyp6B6X1Qvr-oM9eHPyyjWRZFDA6saEkGcPgPB5NIt3cOW4Q4oRh5R4JEDOw-2lU_TwR1JzzaMEECpaQ-lGBmcd5Bk4dIzYFDnuvcxp2z9Mg9MQuOgIdA1Csh6ihDZ0kj4GNB0MSq7-HeoTU55LggcUSfN5Vk9EKBR8n6nZTKSOSm6lWvunK_bycArfAQ-QXKVG8O9sonQZO1_Zpww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت احساس تنهایی و ارتباط اجتماعی در ایران و جهان
🔹
طبق پیمایش گالوپ، ۳۳٪ ایرانیان احساس تنهایی می‌کنند؛ در حالی که میانگین جهانی ۲۳٪ است.
🔹
با این حال، احساس ارتباط با دیگران در ایران کمی بالاتر از میانگین جهانی گزارش شده است؛ چراکه تنهایی همیشه به تعداد روابط بستگی ندارد و کیفیت آن‌ها اهمیت بیشتری دارد.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/675176" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675175">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
تعلیق پروازهای خطوط هوایی بین‌المللی به اقلیم کردستان عراق در پی تحولات امنیتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/675175" target="_blank">📅 18:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675174">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivEW7IgYkTKXxhEWV-wMxYYCcJxalJ95x1ICm1O0uQEScbF7zsIIhhy-PrgnNTQgQmsiM75FW0MGe06N83R_znjesbANEzWsuUFA_SaTmnqUa1PIPfmErURaKcZnhSJ5ooXj1mpvil7H-6G5GQv-5iLgkg3Rv-Yo-9T3c-1_msjvzyUWWdgh4_qvi3Mk0euDy5iHEJ2-obENvUYgvCJXUe4kNOf-joNJ1NytkAWmFGiDW7Woc9zjcrdciVv6wvh4E3TIyoiPJQ5SVKpvKwuW-Xm2mWTCuUTfiRf0r7qVDUq_dpjsnni7xf22AXLCwg_e-YS33mbDXVF9BhbKVszIPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نصرالله معین، خواننده در واکنش به خبر فوت اکبر عبدی: از شنیدن خبر درگذشت اکبر عبدی، هنرمند دوست‌داشتنی و عزیز کشورم، عمیقا متاثر و اندوهگین شدم. باور این خبر تلخ بسیار سخت است؛ هنرمندی که سال‌ها با هنر، لبخند و خاطرات ماندگارش در قلب مردم جای داشت و نام همیشه در یادها خواهد ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/675174" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675173">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ1AVcR_Um9ynfuUQEEZFZpyOSywuxX9dtD-9NPQxRGMDlioocZYpGVMCFwRhxvvicc3t9DSxAZJtWVZ2BSs9HDL7V7Suu_WCCtY5Ho8G5PKl5Zbi9JtcTPzfRBNs2OTbIzieDhNLDst6Y7-4zlHUtwnphmEF1U1NjGA8w0lsWeN3qej5fIZtIdKxSrANsTcV7-nitgLg1NtjooiG4o99PVFi_06RyXZEZyXGQ8FiM2xd4z2r3pTXjG6BGrxYBrMujnGxAVLMc0V89EzM0dGJDov_vrwkNLFO60V22DKqzvFBu4Q1FwjlVpqmjX-gItIwkmqo4zXpfpnrGZAguJSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاهزاده‌ای که در دو جبهه با روس و عثمانی جنگید
🔹
محمدعلی‌میرزا دولتشاه، فرزند ارشد فتحعلی‌شاه قاجار، از نامدارترین فرماندهان نظامی ایران بود. او با فرماندهی سپاه ایران در جنگ‌های عثمانی و روس، مرزهای غربی کشور را تثبیت نمود و با شکست‌دادن نیروهای روس تا…</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/675173" target="_blank">📅 18:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675163">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KckcIWTkVTt3vYvXqlQyScTjoluyy6AWWu4L5G2cHFs0HMaH2zCp1tHH7cwo_D7wr5ene8PIFa9IvJq2rtJvVWq_Ej__h7yOrNX-aJ39B9NNa1xuIZxtGpZ44RsQB9ywZ83UlllU1avrCWA0AGBEjT7nCe72_t2WhiQs8E6nm08aVyptSR4nnXwgrZ764hG1u8RXjtMF1nQ6MOqflpzw4wKFreEvt8K8JTwstDiwGQQ8DsR1-4cDvOfQoS60Vmb9o6n64C3QiUr64vIbTlE6Q55kxopwRG5wNTrek1yslUzgGXtusHRAvgS-2X_QFis1-30NVzWpPdu2PlDvmc44Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DL87WmaRk7_71uQ9XIUyhkHdTdIq5h3kaHV-gMeWPmfJV3HRiMmn-G5Gv9PDFYZATcrqpCZIBLOCc3MTTuqUGXE2bMR7YY2ep0J0MHskJ28m10UY8E9pWAnbYAC0YO-hY5hV1R5bq4TeYv5wmTzMxLzgbRx7cC8a2a-3QAsHzwT88TRNfadEsHughm5BPP9iZgUPiJHnMWMX43Af_LHXemwH5UcpnRJZxY54TygnpfRk6VFtUJ-_EUuo7hfXBVWU3JMZZtyTd9WF_uURznF8qxNgM-NTfNaDgSYFjM5qhnzg7dSZro9qilCcpyYe8tMdsEXVrAAwmgtX_m_T9eP9pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYy4Gv2fkR7yAD6pcXF5AibYyKthcQuoynOiAG37r__xn3bXE_xE55grIi_pbYxKsPSyk2ya6O7Fs9bo5QoJVCnGys2ScjoAOVkgwITXnzKdEz8NNSWXHZPMZJYwlsgUlXOO0Apl6TpWd9mHvOPOEXN0EziRVttR_WJlPh5blv8oObgLtc_tJ58ZYfAiF75tEmliMOmvvJIl1h_T3b0Hnt6VgvfYJTMjJaXja-zEJnnuy0wVtmRPRJb6SspVAnidkU4Vq085jMIKHI5qdNaNi_LqsoVcgiae27hqd7IQv5khAe6eTPAv9CPW5IHLR4lwrgQSfgZ_e9sKWOe_QHUSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-oOMUouVuQDQEWNm_ddtmxW37HZETOgojZzxu9EtxNEdbGIG7qMq7Sbgm-h6vOwIxBCdP6yt7CWkZvSPVoYbX4oVeYkGnRty1N073uOgpl5K8wT_dmRa6EoJDDhQUCzO5BR-uLAgq4tqIJy6kcXhTGLx8trGzU0yf3T4nathHSJlNCIVCMzSjiALOExWoICMPhSkrwJpoCynA0QUS2M-b166zyODquoDMWRkhycenbYSPO-Rtm8nESu4tN_tjCuO-WxZEnTEufNzhrdEI6cueR18J1QUG6bBYIBaKd0qPaxQxmDfw9dBgJhcWMotJAwOGbPytnAELmdDM0WeG4NrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4jjkhbptF3z8FzU_zVKoYSgAW8fa5-LB6FcQwUxq13gQkbJHoOVMWK-hxKRych2zdpJzeGRVBu-MtSL94ktVfIhoIGRIF7Z-zsJKAX9XDytAfN6T-sqxtHa9fHO3PCrCf809OOgWqYt8o58UK622PSZ9ez2eXV9ZhdI_pohYmW46zHSGgAJDs-KSoihEODWCQ4sCTjDZqbQ5etQPYANjZZ0CJoedqipQBFfqW8JhITL0RFiU9WqMfOyX6vM1nFJou8lDdHl0spCyZlTYHwBgPurbSKFWC3LH6Qsu_jYeEPrLoZsTnOAFcu-OYc7-xpHFVuJOU0VIUDtyMnj0iQ1Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hzgLfAumJb7XrGfejvDWybUY8j3S1Xc56SRwOnykIswpHqWIRokW1TY0weAw12K8C4Un4S9LaB5hWyWYtPMB3TRVRzr0SphdiOSFW3Kakd9M48mwNPpV5t6lWEVZ5-X9Ti36KGBSCthTsF6AkbUOThUVm6L4SkI6RVSHVUDDsqev68W2FwrKzkuVYItxjXWezxsG1dQj_vHQRTNDLnGQuHRe8OhNS13KqtMdeucuDLHcyUZROd3_Kc7M3zlBOkZnqVidHQRWqTbl0kYwq8UpWS_ihoorlue7b7Kni1WVSP671uTLC6fqQlUtwKbh-GJSyWhjtVMuXuwR8IGNB-b6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mg5s2_VZwbpZV8fKNjDxPu3GSRBVugnUz5DWjvK_O4n187_gLNV7Gh5VO7Te_6dwuq9-XcwNHYd9AG1uvM9cNYhGK5av-PbgdxYUiRaWWmHghTdwM-faRUcmFt2RPKPURYfSk0J4gVr3DMDcI_AXCk6koJaHtZZ_5AliJsNPRifg3ZlQVCaU84NTlhJsMD4uMa1BbbzWQ9xbh-4Miln9DEUz5w6DBPQLXpBJQaBmQIkfGm2GqIvd3jFMvHAIfuADg1y71gwuvg0Z6soCFasJmJueuYyJ8XokKqikuHS0vCSWwtCcdZQDeuWdpGd3Un3e11j6vrdamaH0NsnsKb0Tew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hd99xFSb1S6_mas--kZjIuTD4qtY-_5VNXnl5swyhVZTac1TZ1fEX7rtYDP1w0Y8GXcFQlDqX603-o6h8W6Qma6ac8w0NYWq7CAOK4Mj0XED4L6I8LyhmxO6xSBIQcHFyyQLTGSpockthVQHl9Z6u_D9bnYcAsUqYyN3a6d7DIJrZrsRvNqOkgnUCZyZAe99FB88bEfLrY4uGXmrF_1pOyo05UoGUwq0Ruio7T7noQvvdhufPozhaGRqxz951TM52VVAYy9_BQvAyYV-IrzTvP1e-49snxMw4jcwcE0gK5WXZefXn5xGQw_wXa2RxlH2UwQL_TTmphVfFiqp16v8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cinmyiao6GTW_oNuLJzXJLVsaLUep0_K0q0rVQiR4Wxv_viR0Xfr-7ij9ApCzDoJS5bWMNqFdxpELrqQg4ZRgF1_H1WusazqVUA1RdIgaqr5BE-0IUbZVHcWPE0KBCZeB-USYZjBbJ9eNLhVgiD1WA7Xizt0z2rK_z-KnRNo8Qn-WM97pMGm5DXNbc58LWyxM6Q8lm5GzFX4mgz4f8y1_mb7TpZQkB0gDrn6g57SlBJIWZWa6YzpfATJTZ_tOw6TfrLFj-JD9Pe7j3FKJsH28SO0Aq87k2Pt-QavUV5NejS2CPCjZWqYlm7k_mpHBdi2vqXjKohbJvR0CxSDOAAtBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpplI54yOQ-PGidFyhHuRr24v3qe_FAkUzs-ZF5Gzz-sJRoOFGk20X0NGFwP63P8Ok_EB6JXWd9YvB2x1MexdGLzkDkXwukHnrhxZgLbnAJNmsqmHu2OIxnEOmy4XpXoEmWmQ2vqA07jIfT66VqXCQaJtbesPuY5UNT-VJlQ-7aC71CEKKsQziPiIQ__V8P--tFDe0cP-aiYEq9RCcR4Qycmkq2Ap5rCZhwcXYuMXA1UTDtuBjDd7nyxJNH9P3s-GoqXQIEYKj2nXB3DE8t6jCgSfZuhgak2aOd-sK5w0H2AKNLf6r2ZumUJ-FoCTqDb-WLca1lRQGsr9mLAk1xgig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤌
کلی ویلا با قیمت کل توو کانالم هست عضو شو ببین
👇
👇
📱
[کانال تلگرام من]
(
https://t.me/fafamelk_68
)
این ویلا ارزش واقعی و قیمت بازارش حدود ۱۳
میلیارد تومنه
،
اما مالک به خاطر
نیاز به نقدینگی و انجام یک معامله فوری
فقط تا پایان هفته حاضر شده با 8/500
میلیارد تومان
واگذارش کنه
همین امروز برای بازدید تا پایان هفته آینده زنگ بزن
تا ساعت بازدیدت رو هماهنگ کنیم.
⏳
📌
#چمستان
❌
دارای 250متر زمین ،240متر بنا،3خواب مستر،روف گاردن،سند مدارک کامل
💰
قیمت کل:فقط
8/500 میلیارد تا پایان هفته
فروش اقساطی بدون بهره
🚗
معاوضه با خودرو،طلا و دلار
📶
خانم رضوی
09194565022</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/675163" target="_blank">📅 18:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675162">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
استاندار ایلام: تاکنون حدود ۳۰ درصد ظرفیت پارکینگ اربعین مهران تکمیل شده.
🔹
رویترز: پاتریوت‌های یونان به عربستان در رهگیری موشک‌های یمن کمک می‌کنند.
🔹
۱۰۰۰ جایگاه در کشور به صورت رایگان، گاز CNG را عرضه خواهند کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/675162" target="_blank">📅 17:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675161">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای اکسیوس: طرحی جدید از سوی میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین کشتی های عبوری است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/675161" target="_blank">📅 17:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675160">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
روابط عمومی سپاه استان زنجان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در غرب زنجان، در روز یکشنبه ۴ مرداد، قبل از ظهر از ساعت ۹ تا ۱۲ وجود دارد
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/675160" target="_blank">📅 17:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675156">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzhoK-wCO_iXR4G0vpqwjmqAGUx5iOG0DbFK0_x3ohiPsjEdQqZ4Jju3Vj0I_ASoCMrnEjgjuC6krpyp986Wk44em9B33i01bU_JRq8jE47x0PAHKmTwiTy2IDZnTc4WNkRIkocGmLZ0tcos3nfnF1lHUp3kFSeYu5o7qkAJEAQC-Oij1r_TBnA7WAo7jRlSQf3WsxBsTBfWoCyDYJw8Vi5DrYHIg786Y48tFqxKyrKhzz0LWMcbK-DOZe5LcLkXfwflsPlSTEqyLCPevRzNofo6qygY0Wgy4eZN_Lp71CcIqnYkPX_w0xDLSYysCDH2BLO0XY4IcvpFqqXL4E2Skw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTZ1L4aVhAwQ-IFLRorD1nojPY7l77sy-Wk30I7rpKgCemJAmgi37nWhqsrP_-pC_gpbxfxJrewhGrjgs8GnG5P0F2VLn6KbwhFnDg8ecHNGieaqxmkm3RoU7p2D8sUne0O1rAev8-IG4fRVQr92SaOTuG1mPcxtjsVMNrauO8WX7d4Wh_jknWSyG6lBpJag6PRB6j2gqUy1fX9TZ4VW9geaLjIy9Ptfliij89479eWsfVFOYAMVxjksbTYw_JTUHTIe48Qge1sCLGL7m-L5st4HdaNFyGnl8J4bIEqLIPIb8KAD5ovQDfbDGYset_c9j8oMJEOWixg7PMz4zku_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvTa79rkca1FjEKoWx79HGqlT0qyCIongmBXkfUthcY33cwPiLpBsYcTxWNzpnxUFd2T_OisLNwfY-SK8fAxfCGhI30rTtUFEboLYqeEZQSIgyuPiKEhsXjP24akNRjTv0PbQk6yuvK8hzEGg0coKXvwJfOyTH-ggpue1qiBWGGB_5ArdDmkaS4AeXKDYXB6s6uqcbqN4vIcJ4MByxHOrAi_kGE_kg5rHenv0FEARfZvabvJlk7M3USgY_fHQbg0izLwhb1XgSST8kRGp4oLf4JAfoc4cHMims2uPGD551diqdPbXgZG_oBuun4_dGyPtgf8nLxDRjAGuoxpcaBriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CotYOYy3Lgnv0QTyE7OrNxKbxJv1qFoNE9nxSwwqF3EjV_Yb3ZUk6Ilz4utdmUsKnTS6FDFwPX2am7JBBdJCUPAGI_lR-6PpB_aq8eq9g6H7FF6rmps5QN6xxwglmWsrlBp5ct5FiJ7iEYZC8Yrdclahv1vA4EaulhBXq6uEPXdsG4AUj_XEA0JanyAgNskPAiFy8TgUWMWACMfQdZRbwZa-HS31vcGMEs0D5PkIeYg6dK9DrLaOJOmY4NTdm2TbMmHV0Fa_trGRpe2f214Wf2_pQTe43-nsEPnw0Wb8_6FCyvIX0VrsAIW2ZxeGpzOIQ_VFo_11A9FY2zep7PIahg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در مواقع جنگی آب یک کالای استراتژیک است؛ امروز مدیریت ملی مصرف می‌تواند سرنوشت کشور را تغییر دهد
#همه_باهم_برای_ایران
#صرفه_جویی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/675156" target="_blank">📅 17:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675155">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
قوه‌قضاییه
:
ساعدی‌نیا اجازه کافه‌داری ندارد
🔹
بر اساس حکم بدوی، صادق ساعدی‌نیا از فعالیت در حوزه کافه‌داری محروم شده و دستور پلمپ تمامی شعب کافه‌های او همچنان برقرار است. بر اساس اعلام مرجع مربوط، در صورت فعالیت مجدد واحدهای متخلف پلمپ و جریمه خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/675155" target="_blank">📅 17:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675154">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پلیس خوزستان: مراقب کلاهبرداران اربعین باشید
🔹
فرماندهی انتظامی خوزستان:
افراد سودجو با ارسال پیامک، لینک و صفحات جعلی و با وعده‌هایی مانند دریافت ارز اربعین بدون نوبت، ثبت‌نام فوری ارز زیارتی، در تلاش برای سرقت اطلاعات بانکی و هویتی زائران هستند؛ از کلیک روی لینک‌های ناشناس و مشکوک خودداری کنید.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/675154" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675153">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wj6nn0k7SPpm4E9AvHtCtp0By8UWCVJKddDovcrnmn6x6q9j5csauK6FDtFpHM3mMIv4yjNFprHiSLZAtbeh5y_MJ_aIBXRV37oKQ4EeS9VzqxjlxbBZcNFeaY2avjqQTKR8kV8ZKA1ozWkGqrFUFvf5DVJFJIUzZdaubi1c0U99KtzHsEx1a8plRKB9tMRvm8tpBoWooPuu2hO9LGZmI2UpcTcGFsENISfiCdZP1hDfEW8JuQ9qaUqqbckHx437PuUZXqvYRVD7fW44Sve6z2AwJQaaqfAVSuzcQzvTIEkYMgRL4vRGOk-xnb86nWomhZ-fh1eBpMQlPNmTwHzjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ کاهش بزرگ قیمت طلا پس از رشدهای شدید
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/675153" target="_blank">📅 17:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675152">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ اسرائیل: شرکت‌های هواپیمایی خارجی لغو پروازهای خود به مقصد و از مبدأ اسرائیل را آغاز کردند
🔹
آماده‌باش در سطح بالا در اسرائیل برقرار است، زیرا آنها منتظر تصمیم ترامپ در مورد آینده رویارویی با ایران هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/675152" target="_blank">📅 17:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675151">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czl-qApsn3Mt10TQSxxnzzI0wrZpLCiCYREMiz48nstdKMyJC3AHvESIqeFuKg7vFo7pa7Nhs7YMwy_C_wNZkLdqBVyCYkGgvjNkFdbry8kgJMOohGV0w3oURenDSGWzKYwSliEXtg4phlKVBh1EtGfMzaibp0Qw88GQw-0nxth3VOPaMI55nhMhyO00OhhxYW_Pw18HsdAV3PJyFUFFz07WVwF26h0iJhFnbvkMRor5Bwmb0lP07In2SMygUZliQDEePjg61slAONs0pH768-aXCjIonCPsuVomNWu7xwTdZ_hfVFFNX7gulnfjqwB3KGMBhnUM4xHvlBYHitBVYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوچک‌ترین اسب جهان؛ فقط ۵۶ سانتی‌متر قد دارد
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/675151" target="_blank">📅 17:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675150">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای نیویورک پست: آمریکا در حال بررسی طرح ربایش اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران است.
🔹
حج و زیارت: تاکنون ۲۵۰ هزار زائر از مرز شلمچه و ۵۰ هزار زائر از مرز چذابه خارج شده‌اند.
🔹
محمد یاراحمدی از گویندگان و دوبلورهای قدیمی کشورمان شامگاه دوم مردادماه درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/675150" target="_blank">📅 17:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675149">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7f4e5c1a.mp4?token=N2CBjpyE_m0nTfJ6U1QxEnScNMPPuJVpjCIDmPnlOPgwqIvemIZwRDFaerp_KNtF18jn1dl-eUxIgJMfPFMXDycY2f0LlcfJ-zOqXJjOaRPJW4LyOESnaM8l-bHcBj-tERHe3qKhLkL8rjkh_dHUrlAqLRKROokRlktVIcJLx3NskAEXp4Xu9bshxefeiGliCkwP9nPvvpYXOSIT96MmuEFLZt34PkOPO6FJLNiM2LjiApBGuqHB8BV7F7n51JNbzOPsAoSTGeMuAbYv99xnckPCgm4fIkZEt01dCtY5hC9HVi1dVoB8d1kUaAvBH-OuRd1tZSDNQkvW942j3RGipw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7f4e5c1a.mp4?token=N2CBjpyE_m0nTfJ6U1QxEnScNMPPuJVpjCIDmPnlOPgwqIvemIZwRDFaerp_KNtF18jn1dl-eUxIgJMfPFMXDycY2f0LlcfJ-zOqXJjOaRPJW4LyOESnaM8l-bHcBj-tERHe3qKhLkL8rjkh_dHUrlAqLRKROokRlktVIcJLx3NskAEXp4Xu9bshxefeiGliCkwP9nPvvpYXOSIT96MmuEFLZt34PkOPO6FJLNiM2LjiApBGuqHB8BV7F7n51JNbzOPsAoSTGeMuAbYv99xnckPCgm4fIkZEt01dCtY5hC9HVi1dVoB8d1kUaAvBH-OuRd1tZSDNQkvW942j3RGipw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
🧹
خودروی همیشه تمیز، بدون ذره ای گرد و غبار!
جارو شارژی خودرو  با مکش قدرتمند ۴۵۰۰Pa و ۲۰–۲۵ دقیقه کارکرد مداوم
کم‌حجم، سبک و قابل شارژ با USB — همیشه همراهت، همیشه آماده!
⚡️
🧼
از صندلی تا کنسول، از زیر پا تا گوشه‌های دست‌نیافتنی…
همه‌جا رو در چند دقیقه برق بنداز!
🤩
🌟
قیمت اصلی: 1,598,000 تومان
🔥
قیمت ویژه فقط برای امروز: فقط 1,089,000 تومان
🔥
🏠
پرداخت درب منزل
خرید
👇
memarket24.ir/dirmob/180124/g-en26903</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/675149" target="_blank">📅 17:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675148">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
رویترز: کارآموز ناتو به ظن جاسوسی بازداشت شد
دادستانی بلژیک:
🔹
یک شهروند کانادایی با اصالت چینی که در یکی از مراکز ناتو در بلژیک کارآموز بوده، به ظن جاسوسی بازداشت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/675148" target="_blank">📅 16:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeCdVBJ0o0Z8js9f_D-SjM9JV-SVsf94azPVzEwljmiusX5JlmoZT_beL87vseKAKNLefUIm9oS-Mc16RyLdkFZiFa4YHWnuvrU1cX19vDB-cg0csHcHCABy14PAr6EmfzNYJrmDgM3rpB-Dv-PvkOTix3xvV7SK74r1d4zLZTeqrjlku9XwwTVYYdJgOGzouHGnr8-Y4UXVdQRRVQ0hFz02t6Hm7pWEciwReJeEN9eNmqI6jQ7TMGIBldsDJPZklwWhF24SsTf3YoW51CQTBeqqal3pdmXqF6jHljrvuiCIDcJEqHFgu7cWMVGmo44EbuQ3Kv3sJ9XQFe4XUvMFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند روش نگهداری مواد غذایی که عمرشان را ۲ برابر می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/675146" target="_blank">📅 16:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675145">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
آتلانتیک: آمریکا بدون برنامه وارد شد، با مشت ایران بیرون آمد!
آتلانتیک:
🔹
یک ضرب‌المثل نظامی می‌گوید: «تا وقتی مشت به دهانت نخورده، همه برنامه دارند.» آمریکا در جنگ با ایران دقیقاً با همین واقعیت روبه‌رو شد.
🔹
بدون استراتژی و بدون چشم‌انداز روشن وارد میدان شد، اما پس از دریافت ضربه، ناچار شد توافقی را امضا کند که به ادعای این نشریه، جنگ را با شرایطی مطلوب برای ایران پایان خواهد داد.
🔹
اکنون آمریکا بار دیگر به میدان بازگشته، بی‌آنکه توضیح دهد این بار چرا وارد جنگ شده و چه تفاوتی با دور قبل دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/675145" target="_blank">📅 16:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای اکسیوس: طرحی جدید از سوی میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین کشتی های عبوری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/675144" target="_blank">📅 16:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d18d97ca8.mp4?token=rJKhNtqhZ2HPeOtc4XsAbjngF2RobMIQtFfM49Qi-d30M9xZutwRXe--n74DKWkC1sGMs2NIbljWFeM42_ex7NiPnx9aIwwkQw1PFtSKzPJtdYjugv1Y_d9MeZ_ubPu8CLqURMkePsWFFhNY1B0Z8JjEm29YuZViJ60ow4-crLM1FlK1A1issJqLpGHtuXPJ8z_TMmHaeo0UOQ4PN3nQ9O7WDEKI6SNlnqLRvjwacxcMYwz6viQahD2X1C0gGLbzZOGegqoPdcDvpV3SAM-l5sXMFc6jVNWmMfNeEmCgFvCFejG6CaumncXjoeG7IoUeQJQ1jZtd3WLBrs5AkEaJTUfX6wy6mwkUcfxLey4KvGU4ICQ0rYZ4eZ4dz_Xap3i-rvoIssMmnMG3uPk7Ut38XQjmhK9XGNaO-ZS4MwbeA_BtMV_G6HM3TVoupehavWSwkM-G0miv-Y80zEvNeeLoHIR5vCMOmCF3paWhY0ZZPAv67GeF7_ca2kN_VtwtbxNpBjU956T5ut8QDVWXlkRVA8_hL8msOxEKct5odKCPNRyBhzXcuRHLe59HbGrgeyKJdvw6wzyRlOU6bHlqFIllXn8uN_UDnDGnGekV2oQlGtAvR4L-SJcyFZhbkRYzTU2zBdQ2H3UxUOgt_0K1VMM_8kdSOIP_-4Q5-40ds7MaZXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d18d97ca8.mp4?token=rJKhNtqhZ2HPeOtc4XsAbjngF2RobMIQtFfM49Qi-d30M9xZutwRXe--n74DKWkC1sGMs2NIbljWFeM42_ex7NiPnx9aIwwkQw1PFtSKzPJtdYjugv1Y_d9MeZ_ubPu8CLqURMkePsWFFhNY1B0Z8JjEm29YuZViJ60ow4-crLM1FlK1A1issJqLpGHtuXPJ8z_TMmHaeo0UOQ4PN3nQ9O7WDEKI6SNlnqLRvjwacxcMYwz6viQahD2X1C0gGLbzZOGegqoPdcDvpV3SAM-l5sXMFc6jVNWmMfNeEmCgFvCFejG6CaumncXjoeG7IoUeQJQ1jZtd3WLBrs5AkEaJTUfX6wy6mwkUcfxLey4KvGU4ICQ0rYZ4eZ4dz_Xap3i-rvoIssMmnMG3uPk7Ut38XQjmhK9XGNaO-ZS4MwbeA_BtMV_G6HM3TVoupehavWSwkM-G0miv-Y80zEvNeeLoHIR5vCMOmCF3paWhY0ZZPAv67GeF7_ca2kN_VtwtbxNpBjU956T5ut8QDVWXlkRVA8_hL8msOxEKct5odKCPNRyBhzXcuRHLe59HbGrgeyKJdvw6wzyRlOU6bHlqFIllXn8uN_UDnDGnGekV2oQlGtAvR4L-SJcyFZhbkRYzTU2zBdQ2H3UxUOgt_0K1VMM_8kdSOIP_-4Q5-40ds7MaZXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوش برای موکب اسکان شهید ابراهیم هادی
🏴
برای سیاه‌پوش کردن موکب اسکان شهید ابراهیم هادی، به 1000 متر مربع پوش نیاز داریم
📍
باب‌القبله حرم مطهر امام حسین(ع) | حدود هزار متر تا حرم
🔹
هزینه هر متر
: ۱ میلیون و ۸۰۰ هزار تومان
🔹
سهم مشارکت: ۴۵۰ هزار تومان
تا الان هزینه 500 متر از 1000 متر جمع شده
❌
این پوش، سایه‌ای میشه برای زائری که زیر آفتاب سوزان کربلا، کیلومترها قدم زده...
🥺
اربعین امسال، به یاد رهبر شهیدمون
👇
باید با شکوه‌تر از هر سال برگزار بشه
♥️
پرداخت سریع و آسان
👇🏻
https://payping.ir/d/j47J
💳
6063731266068221
💳
5041721113831557
به نام: هیئت علمدار کمیل
📱
09136729200
@Ebrahimhadi_Yazd</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/675143" target="_blank">📅 16:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675142">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2ahdkdCqgWkxajuTXJawZ7kCAkm4-KStUgUxT4ygjODs3d6mvpySroAYbrmIye0NV7qLu88Q4nwjzUpcQMHmffrAYU78u64NNSR1YLxCyYXQ-rVoiqcYEG0YOLzGn6JwN_4sxj-Gby0k77FUX8ld8XKHfIZrd55PEOiKmO6yKANTht8E0Uhq_ax54kBYMme29LQzLuoksaNImqY9aw8vNDVg_i2Zat7Ojz53TeByBFNugUW7PTfYj2vzlLzD1OtWpGUZdBqYNTQVWsMemLZiTBw7N0uS-r0lY6gJX5Y6Ex9p1EUlBYme9lQhQFfL_W6XEj9qD0GgYg8p6hEh66dOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منقار تیغی Razorbill؛ شاهکار هندسه در آفرینش طبیعت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/675142" target="_blank">📅 16:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675140">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_670BarEI7wlMa_LmzIYwzH_66I8oYc1iR7RTohl0hSIPQfIULrB-UhFUL-G_TZGCpNyWTsJp7Lnq3JArTpMwihCARsFSt-55APovLwpLBYDe0mHL0NrxhYg-Ac8hENNSpoboJ2TWDYxvf0DzHApI7mMd2LrJ6r5Lq3ezhtPnMTwvSTqyr15Fr0IDKzBK4T8vPqO0bM7SNjKPL4_O1qzb3iAtZhqnD2AOsISdDR2CSZAgg93Wp4q0DZMRFwDt8AvnS0N1vU33DZ47Q30FlzmlQJCysRi_cHW8rKmgOItPHID576mUktzY43WFHthPnJqCAErPEfeMp_HUmQEec92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص ۸۰ درصدی تمایل به خرید در بازار طلا؛ بازار خود را برای «۱۳ صفر» آماده می‌کند
🔹
هر سال با نزدیک شدن به ایام «۱۳ صفر»، بازار طلا جان تازه‌ای می‌گیرد. اما امسال اوضاع فرق دارد؛ شاخص تمایل به خرید در پلتفرم طلاین امروز به ۸۰ درصد رسیده؛ یعنی تقاضا برای خرید طلا نسبت به هفته‌های قبل رشد چشمگیری داشته و این یعنی بازار زودتر از همیشه به استقبال «۱۳ صفر» رفته است.
🔹
اقبال به افزایش نرخ طلا در حالی رقم می‌خورد که در ماه‌های گذشته این بازار دچار تلاطم‌های بسیاری بوده است ولی همچنان مردم خریدار طلا هستند و طلاین به‌عنوان یکی از مقاصد اصلی خرید طلای آب‌شده، این موج را به وضوح در شاخص خود منعکس کرده است. عدد ۷۴ درصد نشان می‌دهد که تقاضای امسال در آستانه محرم، از سال‌های قبل هم بیشتر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/675140" target="_blank">📅 16:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675139">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
آخرین تصاویر از وضعیت پل‌ها و تونل‌های مورد حمله آمریکا در استان هرمزگان
🔹
روایت خبرنگار خبرفوری از استان‌ هرمزگان
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/675139" target="_blank">📅 16:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675138">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
انفجار در اربیل
🔹
منابع عربی از حمله به پایگاه آمریکایی در مجاورت فرودگاه اربیل خبر می‌‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/675138" target="_blank">📅 16:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675137">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad07b266e.mp4?token=CcsA2etGohfIm1JwhSrTy_jKctBGIH0OA9geL6v1yBXDuwfAifc7Z-lHVwwxeyN6FAlg6H6uvfQVSTu_licmN6arsRosII3sX80Q66_--qZsfvAXk-aolkLA3ARDgSx0qgln-rZwYMW-i88wrAVsp3WC8OWKGBs5tryr3zMXFPkSW2wNWxuprgqOrkh9s819V0dw22M9tUgdv3sEl-NBW7t8RRsLhWSg3U3M50AueCXaiCcJ29w-8MmzWqt9g7kYeiBVKJOeRmUjgAVr2EKzA4p-rfAb4NiWxR6go8UnryFbf8RIZlSGa7UznKPM8kPFylVVSj-zVbnR3WHojIGGLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad07b266e.mp4?token=CcsA2etGohfIm1JwhSrTy_jKctBGIH0OA9geL6v1yBXDuwfAifc7Z-lHVwwxeyN6FAlg6H6uvfQVSTu_licmN6arsRosII3sX80Q66_--qZsfvAXk-aolkLA3ARDgSx0qgln-rZwYMW-i88wrAVsp3WC8OWKGBs5tryr3zMXFPkSW2wNWxuprgqOrkh9s819V0dw22M9tUgdv3sEl-NBW7t8RRsLhWSg3U3M50AueCXaiCcJ29w-8MmzWqt9g7kYeiBVKJOeRmUjgAVr2EKzA4p-rfAb4NiWxR6go8UnryFbf8RIZlSGa7UznKPM8kPFylVVSj-zVbnR3WHojIGGLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با حقوق‌کارمندی مدیریت پول کنیم تا آخر ماه کم نیاریم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/675137" target="_blank">📅 16:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675136">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5194524b9.mp4?token=MGLHiqExa2fjoMATcnIKHdiXrp9OZelb_syAC859mum6gwNI9cOeb_gztT9uJrmHYkmrZBnJXIzAcYnffddhA1PPL75n-lz5Kp9JRkyI6jYIr6-eX8h7j9-QFKs_9PRi1yVbA8-iraPmQWXVZdddcQHgdeFvFNzJtRyOSjDjf6Icqj2WE-ORfOvIzZbAkuCS5IiJ_BksD7jVPL3HKAKt936l41wTLk5E5DFDRKnmHf81JDXhcDeF5R9GHzcODKDLURq3Mzrusris2yfjdGhJpr3XhFmcLC9wBfe-wFnLFm3Dmpl3Mkgo9US-9ORda3Rd4bJbQmYpMHSSir6uVvZy77D5q4YWklpn5Pkl7jldzu8nUUWy9k4rBkxWzmy43CueK-MjIf1UGvfP1Ez4iqOEpC4NDQkov6z5W_rc0AH0yyTcKCYHjv65nupiW3f_9N417Wb7i6Qyc440E_5ohLm_NpDM8Mcyp8BB1wunpF6BZyO8aSzWGDydAZMOjCYWfXQIAtpQoftbxLNSflaaoNiIxvTosc029MrwydPUV37KuqZ_kTlWO8SnbnT6lVswC1DZUXrXgzMsd3YsYxRvB4KrAytHskVPT45vsK2y3JGt9pu8sxzJ_vM1iGAOf84y5fbIVhLcg68AtnidTfxOaUzH_akvoUKatB0RvfnduS6xdIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5194524b9.mp4?token=MGLHiqExa2fjoMATcnIKHdiXrp9OZelb_syAC859mum6gwNI9cOeb_gztT9uJrmHYkmrZBnJXIzAcYnffddhA1PPL75n-lz5Kp9JRkyI6jYIr6-eX8h7j9-QFKs_9PRi1yVbA8-iraPmQWXVZdddcQHgdeFvFNzJtRyOSjDjf6Icqj2WE-ORfOvIzZbAkuCS5IiJ_BksD7jVPL3HKAKt936l41wTLk5E5DFDRKnmHf81JDXhcDeF5R9GHzcODKDLURq3Mzrusris2yfjdGhJpr3XhFmcLC9wBfe-wFnLFm3Dmpl3Mkgo9US-9ORda3Rd4bJbQmYpMHSSir6uVvZy77D5q4YWklpn5Pkl7jldzu8nUUWy9k4rBkxWzmy43CueK-MjIf1UGvfP1Ez4iqOEpC4NDQkov6z5W_rc0AH0yyTcKCYHjv65nupiW3f_9N417Wb7i6Qyc440E_5ohLm_NpDM8Mcyp8BB1wunpF6BZyO8aSzWGDydAZMOjCYWfXQIAtpQoftbxLNSflaaoNiIxvTosc029MrwydPUV37KuqZ_kTlWO8SnbnT6lVswC1DZUXrXgzMsd3YsYxRvB4KrAytHskVPT45vsK2y3JGt9pu8sxzJ_vM1iGAOf84y5fbIVhLcg68AtnidTfxOaUzH_akvoUKatB0RvfnduS6xdIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
قرار همدلی؛ برای ایران
🤝
این روزها مردمان خونگرم جنوب کشور، گرمای طاقت‌فرسایی را تحمل می‌کنند. بیایید با یک تصمیم ساده، سهم خودمان را در کاهش مصرف برق ادا کنیم.
قرار ما: کاهش مصرف برق، به احترام مردمان جنوب کشور.
🤝
💚
#مدیریت_مصرف
#پویش_۲۵درجه_قرار_همدلی
🆔
@tehran_roshan
💡
قرار ما همدلیه
🫶</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/675136" target="_blank">📅 16:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675135">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f91b4907f.mp4?token=uSrgZr47AWZNdaG7Zm5Ljyg_NvwA0v94d1V-rVhEG9uGp3oN9vjMI3reWG2avt0Xh7l6rskr4ceocr8bG8h4IlPEJ9zHSG4bh_ibs1f-F7ZL-uy3jxzfCv_O1dvNOLd8jxOLiQxwMNGPtXg9HFTkl9jdsAe4ptWIEsIX3fyTi371ouCqwMUzIfxBkDcC_kFahwI3TPH3xBTaqIbXePTS1rnmGAy3dCo6WE1efjX1GRefZ-HW3H1SJpoMLgKErbCBpiqCobaH1-e0W5pdOYNp69sWf6jk61KCoSN5akjymnUFCk9WMhxz7hmA6jIG8Yvs5-sp1YLv6fPv8jf2pE3ZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f91b4907f.mp4?token=uSrgZr47AWZNdaG7Zm5Ljyg_NvwA0v94d1V-rVhEG9uGp3oN9vjMI3reWG2avt0Xh7l6rskr4ceocr8bG8h4IlPEJ9zHSG4bh_ibs1f-F7ZL-uy3jxzfCv_O1dvNOLd8jxOLiQxwMNGPtXg9HFTkl9jdsAe4ptWIEsIX3fyTi371ouCqwMUzIfxBkDcC_kFahwI3TPH3xBTaqIbXePTS1rnmGAy3dCo6WE1efjX1GRefZ-HW3H1SJpoMLgKErbCBpiqCobaH1-e0W5pdOYNp69sWf6jk61KCoSN5akjymnUFCk9WMhxz7hmA6jIG8Yvs5-sp1YLv6fPv8jf2pE3ZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیرعلی جداوی، دومین جاویدالاثر مدرسه شجره طیبه میناب
🔹
دلیل عدم انتشار نام او تاکنون، درخواست پدرش برای مخفی ماندن خبر از مادر باردارش بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/675135" target="_blank">📅 16:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675134">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: رهبر جدید ایران تمایل بیشتری به دنبال کردن سلاح هسته‌ای دارد
ادعای نیویورک‌تایمز:
🔹
سازمان‌های اطلاعاتی آمریکا معتقدند که آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، بسیار بیشتر از پدر و سلف خود به دنبال کردن سلاح هسته‌ای علاقه‌مند است. پدر آیت‌الله خامنه‌ای سوگند یاد کرده بود که از توسعه سلاح هسته‌ای منصرف شود!
🔹
جانشین او هرگز علناً خواستار ساخت سلاح هسته‌ای توسط ایران نشده اما سازمان‌های اطلاعاتی امریکا معتقدند که او جاه‌طلبی‌هایی برای توسعه سلاح‌های هسته‌ای پیشرفته دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/675134" target="_blank">📅 15:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
رسانه‌ها پشتوانه‌ای برای نظام هستند  حسن نتاج صلحدار، نماینده مجلس:
🔹
نگاه ما به رسانه‌ها به عنوان پشتوانه‌ای برای نظام انقلاب و جبهه مقاومت همواره مثبت بوده است و رسانه‌ها می‌توانند نقش تأثیرگذاری در تبیین مطالب نظام و انقلاب در شرایط فعلی جامعه ایفا کنند.…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/675133" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای المیادین: کویت و بحرین از جولانی خواستند تا در صورت وقوع درگیری زمینی با ایران، نیروهای جهادی خود را برای کمک به این دو کشور بفرستد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/675132" target="_blank">📅 15:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a55e0a0410.mp4?token=HzKfe4DoPPvO7-lM3c9JQbO3AeXv1LCoIrqJefPSleWArt-JGlYE6ikqSoApEt7MfxigsXr9OjPqbbuEEjRHpD_EZxURXFXzUEhEtrac_zhf1UL6J-YCiQWtIV1GsIhSaqBmRAAW42NLrpuA18i-l_WtQhSqIH1PzszdRkOheiLkhvqK4rEdg-3QETeEF5kvRy5oRllskbKohrSx4OZnhRFVgirpSUcY_1FgIMJRgblzzJ5T9KdVmh3jdQYwAu66OLJGIfu8EUEgdjOR8e2S9-XLZv6afbDllWRkRrpz5vdXxciAnGNXbfnXkNVAJQM-j7PIlaN3y1R4Xd0TkS80rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a55e0a0410.mp4?token=HzKfe4DoPPvO7-lM3c9JQbO3AeXv1LCoIrqJefPSleWArt-JGlYE6ikqSoApEt7MfxigsXr9OjPqbbuEEjRHpD_EZxURXFXzUEhEtrac_zhf1UL6J-YCiQWtIV1GsIhSaqBmRAAW42NLrpuA18i-l_WtQhSqIH1PzszdRkOheiLkhvqK4rEdg-3QETeEF5kvRy5oRllskbKohrSx4OZnhRFVgirpSUcY_1FgIMJRgblzzJ5T9KdVmh3jdQYwAu66OLJGIfu8EUEgdjOR8e2S9-XLZv6afbDllWRkRrpz5vdXxciAnGNXbfnXkNVAJQM-j7PIlaN3y1R4Xd0TkS80rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری شبکه سه: ۱۰۰ روز است که هر بار اسم بچه‌ می‌آید ناخودآگاه به میناب پرتاب می‌شوم/ کسانی که دم از حقوق بشر می‌زنند، کودکان ایران را به خاک و خون کشیدند. ما از خون کودکان میناب نمی‌گذریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/675131" target="_blank">📅 15:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
‌ عملیات اول، اهداف حساسی از تأسیسات متعلق به شرکت آرامکو در جیزان را با ده‌ها موشک بالستیک و پهپاد هدف قرار دادکروز و چند پهپاد هدف قرار داد
🔹
عملیات دوم، اهداف حساس متعلق به شرکت آرامکو در شهر ینبع را با چند موشک بالستیک هدف قرار داده‌شد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/675130" target="_blank">📅 15:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
‌ سخنگوی نیروهای مسلح یمن: پدافند هوایی با یک گروه از هواپیماهای دشمن که وارد حریم هوایی شده بودند، درگیر شد و از انجام جنایات بیشتر علیه این ملت بزرگ جلوگیری کرد  ‌
🔹
دیشب ۲ عملیات نظامی مهم علیه تأسیسات آرامکو در جیزان و ینبع انجام دادیم، این اقدام در پاسخ…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/675129" target="_blank">📅 15:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675128">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
‌
سخنگوی نیروهای مسلح یمن: پدافند هوایی با یک گروه از هواپیماهای دشمن که وارد حریم هوایی شده بودند، درگیر شد و از انجام جنایات بیشتر علیه این ملت بزرگ جلوگیری کرد
‌
🔹
دیشب ۲ عملیات نظامی مهم علیه تأسیسات آرامکو در جیزان و ینبع انجام دادیم، این اقدام در پاسخ به تجاوزات سعودی علیه شهر و بندر حدیده و جزیره کمران و همچنین ادامهٔ محاصره مردم یمن و نقض حاکمیت یمن صورت گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/675128" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت: آمریکا می‌خواهد داعش را فعال کند
محمدرضا محسنی ثانی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
آمریکا پس از آن‌که در مذاکرات، حملات نظامی و هدف قرار دادن زیرساخت‌ها به نتیجه نرسید، اکنون به‌دنبال فعال‌سازی گروه‌های تروریستی و تهدید زمینی است.
🔹
آمریکا روی نیروهای داعش و برخی گروه‌های مستقر در آن سوی مرزهای غربی حساب باز کرده، اما هر کانونی که برای چنین تحرکاتی شکل گرفته، توسط سپاه و ارتش درهم کوبیده شده است. اگر آمریکا دست به تجاوز زمینی بزند، فرصت مناسبی برای وارد کردن شکستی سنگین‌تر به این کشور فراهم می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/675126" target="_blank">📅 15:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عضو کمیسیون مجلس: مذاکرات در هماهنگی با مسئولان ارشد کشوری انجام می‌شود.
🔹
تردد زائران اربعین از مرز سومار در شهرستان گیلانغرب از امروز آغاز شد.
🔹
معاریو: نتانیاهو برای نجات از شکست انتخاباتی به دنبال اقدام علیه ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/675125" target="_blank">📅 15:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675124">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCP3mISzlHHX5UG92ao9aMKbAyOAGqsmqwJEO2Xhx6wp0kpUAX39m7t8r_FC0rOQ_0ijDCXSv02vk3txdSVZ8I_tggTbWTFJdbSB15vhgK4iSvTGVJrjejbFaPa8WOAGR6KnWvBAjQLy-aaQWiVxvMlkQX1kENPv_tQgRSKxfydxMIR1RGbsEM6KxY5udkEiA6ZafHUXfR0eRgXcp9dN8rsCJCSyoKlq5aBrqnfm7AHKwd2cFafFp2oT9uoEhsslHmy8IkGHuqK1uLL06v6ZWerNpi-c283Z5YuEiYQxKYjNi9SfT4Eg9z7iv9uQk2QxFug6Udp5CsSOgJPj3wkTmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد دریافت «عوارض تأمین امنیت» از کشتی‌ها؛ طرح جدید میانجی‌ها برای بازگشایی تنگه هرمز
🔹
به گزارش اکسیوس، در پی تشدید تنش‌ها در خلیج فارس، طرحی جدید از سوی میانجی‌ها پیش‌روی ایالات متحده و ایران قرار گرفته که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و مهم‌تر از همه، پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است.
🔹
طرح این پیشنهاد از سوی رسانه‌های غربی، نشان می‌دهد بازار انرژی برای حفظ ثبات خود، راهکارهای عمل‌گرایانه را به استراتژی‌های محدودکننده ترجیح داده است. روی میز آمدن ایده «پرداخت حق خدمات»، در واقع پذیرش این واقعیت میدانی است که تراز کردن معادلات دریانوردی، بدون تعامل با بازیگر مسلط این پهنه ممکن نیست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/675124" target="_blank">📅 15:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJoYLH8QMSbK0azvDbmVZVR8w_RkjGXAVPvgSfmq6bBeNrzeuMXvUbP4EcOWyJit9yQ32dxCoJbk8P5mHVrWuSqIGp1YxCraDhSSOxjI2BAwh1uOPNrR1OLD8SjZ9e-zU4exqN8bV6KJx_oOGU7UD0TkhV5diOI__-4Sun4ManZtBzRi0mkHTGwJ90AOLjc67R3e83MFi-sQOI4ehxtpFt4yOqZfIngvnr3H4_VyCISBIdfzz9cqFM0zDRcmvY42jrqcKAJDCZzscJacstdxQ3Izn2PlmElQoh2zrNEMCBbRIA77sRQBymv_cuNbpA53jlbiEf86QONJh3OiVqeoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivkG3GiJqDoyWJGkbbnNij3eUoMiVEAvVl5pMiHvWaYyFSG8ckngnefHx1qBc8u-88jvdO_JvBwrsc6mYQNX3rBtLufLXbKT7Z_2J3CTqC3W7XIq_rghsuu8O22eZsjw5FjOqR_h6sEY8zo7uWtfGCXJFHvbJpmVVJ55CAh2sYJmuDOXk545yHnzUH_Ory2nUu6yESpj2yNXtvEhqVDHMA4eoaKxQpK7GJiZy5opd2XqEj3QjsC9ey5A60oQi7Z6DHVMRFwiN0-Htat4azw8KUOp5j-k3cnqfpZx4MQI7ZFzyAhGZQWWTeVfK3HNTZKXcKVMIbNSpo0vAGy0-5i8NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صادرات ۱۵ محصول کشاورزی آزاد شد
🔹
وزارت جهادکشاورزی چهاردهمین فهرست جدید محصولات مستثنی از ممنوعیت صادرات، شامل ۱۵ محصول را برای اجرا ابلاغ کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/675122" target="_blank">📅 15:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
موشکی که پدافند آمریکا را گیج و سردرگم کرده است
وال استریت ژورنال:
🔹
موشک بالستیک «خیبرشکن» به ستون فقرات توان موشکی ایران تبدیل شده و تهران با به‌کارگیری تاکتیک‌های جدید، مسیرهای پروازی متنوع و حملات ترکیبی، تلاش می‌کند سامانه‌های پدافندی آمریکا و متحدانش را سردرگم کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/675121" target="_blank">📅 15:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISuu8txOs9aEvedJNajVoQuNDkJABBLJJr1G26pHRhmBLmqCcHmV0lAY6AtW7xZg9u62fTB_LnwjvsRqAl6_xMAMzsJrge-TbYN_LGMfBILyrjlj0yCA_ECoC3QMm3l5XcjPQNZBJGK_ijm0-6ucCZFzCyyXiBQk_nsWmgLiE3Y80x6xOBKwmycxQx9ESUKUwPZkPlfBk5Wbwv-5TW2I1G9AwqwOg_E7OGwy5Uf7BdpTc9f0SHZ_TB1yilJrAziJNbFq6Vxa9speu5E6HDSdK_JdiDk2c_f-gFvu2E-2GU9v_Z35sVDCOZlon1VV2uMOatiSrTwJ_kS6CHG2A03Msg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیباترین شاهکار خلقت؛ شکوفه‌های گیلاس‌ ژاپن
🍒
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/675120" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLXYNZD0HHEjD9ZhHPvCSH4BsXHQr_d9vVJKsZvP0tgXVc5MY74WC3tVn4ogi5OC9ZSo4-t8FfCxkyja7wXOHmal0lXt1A_mdAj3EVSqVkYKUwPqYEGIdlzmp-cpwYCr2PzitrdvCh1tj39dExkBidO3MSZNc0-p_Cj1VxEHHDSAn5FXtnbM5t8-ciGR42oTtdsdFfS1QWE38eEi5WnAxYMU4ZsggLsmKzNCH7FF5qWs_3B_WNCOf53tfEqQy4p0sf_NWIJQx3Wdu5vq9x34Uk8WmHHC7VCRcJ2SxpF4jG40X-l9Zg-A0J7MkmE7FsuReSD5aHWTZ8Odf_8v75q7GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فحاشی مخفیانه ترامپ علیه مقامات ایران
ادعای وال‌استریت‌ژورنال:
🔹
ترامپ در مورد جنگ با ایران بدون پایان روشن صبرش را از دست می‌دهد. به گفته یک مقام ارشد دولت، رئیس جمهور نسبت به دیپلماسی بدبین شده و در «حالت انتقام» از تهران قرار گرفته است.
🔹
به گفته شخصی که نظرات او را شنیده، در جلسه اخیر در دفتر بیضی شکل، ترامپ به شدت علیه رهبران و مقامات ایران سخنرانی کرد و آنها را آشغال و دیوانه خواند و مجموعه‌ای از فحاشی‌ها را آغاز کرد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/675119" target="_blank">📅 14:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f2466bb3.mp4?token=tYZzYcrBtetrZxCWQUQqW84cCepQziF1PNJT23AoEK-GeiXtT_vvLU62ZLCbwPsT9FwryHkOwbkPFpn1-AvWRlJdzIqZn51RwYJlvfF3MEedhahL8Hw3SIzDZ75LpNEPLdtNF9XwrrZ4CPkRU5aqYIHV9TjpIjamJuLxZ4RmneeC92X80c6nek4Kwbd7Qj1MoF1NcYlq5jmpPJ3llPcawJ_ALKrsXoBvxsgkyuPJOr7UG-sDCeR6BYugr76V9fR-NfsB5AzXnRGbLfviedHRfhA4ZJ8LMPwA6OBTMDuLfAXKsYYWAqegb55E0nNNaNwMjeWq2VTkfs4izZ6vMuPYvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f2466bb3.mp4?token=tYZzYcrBtetrZxCWQUQqW84cCepQziF1PNJT23AoEK-GeiXtT_vvLU62ZLCbwPsT9FwryHkOwbkPFpn1-AvWRlJdzIqZn51RwYJlvfF3MEedhahL8Hw3SIzDZ75LpNEPLdtNF9XwrrZ4CPkRU5aqYIHV9TjpIjamJuLxZ4RmneeC92X80c6nek4Kwbd7Qj1MoF1NcYlq5jmpPJ3llPcawJ_ALKrsXoBvxsgkyuPJOr7UG-sDCeR6BYugr76V9fR-NfsB5AzXnRGbLfviedHRfhA4ZJ8LMPwA6OBTMDuLfAXKsYYWAqegb55E0nNNaNwMjeWq2VTkfs4izZ6vMuPYvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقرار استارلینک نسل ۳ با استارشیپ و انفجار بوستر
🔹
اسپیس‌ایکس با استارشیپ ماهواره‌های استارلینک V3 را مستقر کرد، اما بوستر سوپرهوی حین فرود در خلیج مکزیک منفجر شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/675118" target="_blank">📅 14:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
الجزیره: ایران فهرست اهداف جدیدی در داخل اسرائیل تهیه کرده است
🔹
یک منبع امنیتی ایرانی به الجزیره گفت در صورت آغاز هرگونه جنگ، این اهداف را مورد حمله قرار خواهد داد؛ اهدافی که به گفته این منبع، بازسازی آن‌ها سال‌ها زمان خواهد برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/675117" target="_blank">📅 14:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtDY2LHhVW6c1E9jwwBUsaEHu8QZCJert4HG_vGxHeURKq__nechwL_G78QO0osz6PVB9QtAzmpz-n-orm4o3I1bnZrSHhmKZqgnQYI_oHrcCxDH3PWaRuAwm8GhwlM0O2K_Wqvwce3XKQSftE3JvZUgo1uqtcn9lUp3W1ggkG4kGhjW1he6Qovm64E2IRAbV50EJ3dUxs329_4RDvTYX8eVHZSDmRg45ZVrtwqeSVUYvGD5QsBwg1Wp1BWXNle1zEJUA8uYph_lExl_bPMN0VITOHYdZ7gqg9OzfTpmGRdiAf9jcLDeJtcuYSm19y5tZhn0rgYq3uz1rxvM4dVntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQzrMZNd6zW33Oo8bccNljPlKERjU0K4derBw4yhw833C0k0fQfnX8Y4zS_NkocZuCTAS06Tju0xPvAOm_cywFo_tftY5jkUJmEOVxL7aM5LQzi4qDfTPtm2PP61-6MTnoXacknS-DmoSznfhwdq0wPsRElP4mIc_O1u3A51wQtBhJlR5KuBM-fvD2e-zpmGcQwJ1-87miI-ugJY4xPcXA4NGJpKNYhG6HWYdVFPy_T7pN9ATriuLEno2y_qKHMdhoZwCvjSiVTPWmfmwg9IZaIpTGXLEWFQQmBHB-NQD08Q5FnMpTexoEsf_nuOCGuPHs0H66K9XeSBEuVjvIp-6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91ea1a64eb.mp4?token=ou7qA363SEETMZxtp-TzxvhD0PPUdPz3CGtAfRLxS6MyhDll4QTn3NfQgnJK_csTE76QBOb4UWeXJ8TIUT4CYnbKHhhVWhk7GfWqdhiL70BB3d6nxkzBtsm6AozmcuhFhIQ8v66oS4Nvm-DLtQ-O06XALEFPbHL735M1kWCyCY2yJyLZdes2CHIiHBxlVF1Y7Y1k6wa1o92P_wmH71W300j3er3-2vjYmIWG-FGseUQ6zNBSWO9jLpckoFOn1pApGzC-V_FMholfPiNWpBHFbXnoTt32JH7pX5rYt2hSViQlwBGBFmtuGZmo6Q0qRkkDienwjJPFqJqUAw1Glu0Ygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91ea1a64eb.mp4?token=ou7qA363SEETMZxtp-TzxvhD0PPUdPz3CGtAfRLxS6MyhDll4QTn3NfQgnJK_csTE76QBOb4UWeXJ8TIUT4CYnbKHhhVWhk7GfWqdhiL70BB3d6nxkzBtsm6AozmcuhFhIQ8v66oS4Nvm-DLtQ-O06XALEFPbHL735M1kWCyCY2yJyLZdes2CHIiHBxlVF1Y7Y1k6wa1o92P_wmH71W300j3er3-2vjYmIWG-FGseUQ6zNBSWO9jLpckoFOn1pApGzC-V_FMholfPiNWpBHFbXnoTt32JH7pX5rYt2hSViQlwBGBFmtuGZmo6Q0qRkkDienwjJPFqJqUAw1Glu0Ygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سانحه رانندگی مرگبار در سوریه؛ بر اثر برخورد یک اتوبوس نظامی و یک اتوبوس غیرنظامی تاکنون ۳۵ نفر کشته شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/675114" target="_blank">📅 14:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce403cb1f4.mp4?token=Kjy6-AbjMOgv2Yy0mZeKuYEgNU-NQ1EerqMoTBPELnN3uIpOC4LZQabz_9nI3hS8YuE37ZRN7v_odF4rlfipxupiqW7-S4DBF81qb__EBG05b_ICx4PMTJLlrWBhjLP4NmdPaQGOg4QSgOuwQedeAIpzOFWdc5zRRc0niNLvDMOUqsKJF6SkLztcUOaNfwwdMmSBmGRTdRs-sVrrqS7g6MXPmz9hWNnM1ltZSO5plq_jEt6uq7qlrigES0y7aOn6uFXvXPimu6x3YBsviL4UacSmotdIFp2kKhLIDp2I3usLQmAMx4q69DuoyU_jAKm-PKzJ2o6hvS6ig1HFhSlzZKamZ34TH8YQ9n9zqlnDDRhPPWJWcEjJVb1-7nO-RntxK_I0yVYqUq82uPWTiEHRKPnuH_h6emjQzcLsAPBqhJWuNwSAKTy8lVWJJogwfoMB6G-iwvd8Q5VChV9jeBRHYqDQdCt5ejJTC9V7OvB5Xf0l2tvsHPnvxJ3WRjB3rALmwrSf5DraxQR82vtR6ovNh7aGPSsR1FsDb2IFb6C7U-Dd24bA7WwV9U0TSkjWRSrr2yGqFuRi7CEuxGEZgYHEQaq-Se7jUxcfrMaUJB1a3KxGSdi8kxFRgnb78j_qqUz7Slhl_4CJ8LYjHRKxOncNJ_g4sXrfI8Bn2ehaU1jUQgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce403cb1f4.mp4?token=Kjy6-AbjMOgv2Yy0mZeKuYEgNU-NQ1EerqMoTBPELnN3uIpOC4LZQabz_9nI3hS8YuE37ZRN7v_odF4rlfipxupiqW7-S4DBF81qb__EBG05b_ICx4PMTJLlrWBhjLP4NmdPaQGOg4QSgOuwQedeAIpzOFWdc5zRRc0niNLvDMOUqsKJF6SkLztcUOaNfwwdMmSBmGRTdRs-sVrrqS7g6MXPmz9hWNnM1ltZSO5plq_jEt6uq7qlrigES0y7aOn6uFXvXPimu6x3YBsviL4UacSmotdIFp2kKhLIDp2I3usLQmAMx4q69DuoyU_jAKm-PKzJ2o6hvS6ig1HFhSlzZKamZ34TH8YQ9n9zqlnDDRhPPWJWcEjJVb1-7nO-RntxK_I0yVYqUq82uPWTiEHRKPnuH_h6emjQzcLsAPBqhJWuNwSAKTy8lVWJJogwfoMB6G-iwvd8Q5VChV9jeBRHYqDQdCt5ejJTC9V7OvB5Xf0l2tvsHPnvxJ3WRjB3rALmwrSf5DraxQR82vtR6ovNh7aGPSsR1FsDb2IFb6C7U-Dd24bA7WwV9U0TSkjWRSrr2yGqFuRi7CEuxGEZgYHEQaq-Se7jUxcfrMaUJB1a3KxGSdi8kxFRgnb78j_qqUz7Slhl_4CJ8LYjHRKxOncNJ_g4sXrfI8Bn2ehaU1jUQgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: در ۲۴ ساعت گذشته ۴ کشتی با شلیک اخطار نیروی دریایی سپاه متوقف شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/675113" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کمبود پرستار در کشور به ۱۱۰ هزار نفر رسید
محمد جمالیان، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
کمبود ۱۱۰ هزار پرستار در کشور به علت‌های توسعه تخت‌های بیمارستانی، بازنشستگی و ترک خدمت پرستاران و مهاجرت نیروهای ماهر است که شیب ملایمی یافته اما همچنان ادامه دارد.
🔹
مطمئنا دولت مقصر اصلی مهاجرت پرستاران است، وقتی درآمدها پایین است و کشورهای حاشیه پول خوبی به پرستاران می‌دهند آنها هم به آن کشورها می‌روند.
🔹
دلیل اصلی مهاجرت پایین بودن درآمد پرستاران نسبت به هزینه‌های زندگی به‌ویژه در کلان‌شهرها است، کار در بخش دولتی جذابیت ندارد
@TV_Fori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/675112" target="_blank">📅 14:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe30add31.mp4?token=QZ5KZUt4b_amHqwyCjtKKDNVNQJP0Pzi05FcA9s4Ibx5fA8_pNIUJaiG1afBAicEU7xVXvbN_B_oKfWNbxUhP1ZVrufiMlqh2KhanaquY0T1i_1BOvsptr1AoNUucDqxvJ4QBLc-laE1r_pNmVpsTrBZJOgZepJklPy1c21gDD_-4GK_fkYHZyqMym0KvpWCTm5LXS2pmy-mtIXfguVnewNksludFK7OOa2vkOCkkPkWzIVnwFDkqrvfFGqF4jK3sdqtvSYd0tbRTt4882xzN4ri7KNwTzwEyRAcUH4oY-039lLIsP24sbAFD4rCVXKquQ8Z7a6712_b3CxaxT4iIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe30add31.mp4?token=QZ5KZUt4b_amHqwyCjtKKDNVNQJP0Pzi05FcA9s4Ibx5fA8_pNIUJaiG1afBAicEU7xVXvbN_B_oKfWNbxUhP1ZVrufiMlqh2KhanaquY0T1i_1BOvsptr1AoNUucDqxvJ4QBLc-laE1r_pNmVpsTrBZJOgZepJklPy1c21gDD_-4GK_fkYHZyqMym0KvpWCTm5LXS2pmy-mtIXfguVnewNksludFK7OOa2vkOCkkPkWzIVnwFDkqrvfFGqF4jK3sdqtvSYd0tbRTt4882xzN4ri7KNwTzwEyRAcUH4oY-039lLIsP24sbAFD4rCVXKquQ8Z7a6712_b3CxaxT4iIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنوب؛ قصه‌ای كه موج‌ها هر روز از نو روايتش مى‌كنند... #همه_باهم_برای_ایران
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/675111" target="_blank">📅 14:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKO09jp3VQC674HFEQyLnTy0XCxAKQ_xOub_aYPwAFzwqGW9VjjLfrIhbtKr6_PdsJfFoprjnagEYglzVpPImKEff8ZiA95gI78sktDNR8n53wgSCzPhFVD5TZS0VjlY6L7KKmDvZ_m9xzvg7SBxbN_rLhltQUmd0rHMxQNouo2d0q_QJ0EftVpTMP_q3eoGrs9-4w8zJlJNR2GPWFu2y2OtKHBB8AepWw96Y_u409d_XQi1qfj8mBfU0X6ezYljIadZY8rU__4uvYxNmYWk_wJPbhelDWWGBljd1zCz5mhw0fo7D89_EwEKMe1I9l8G08xQ_UA6RK7j6rdBRg-cJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تداوم نقض آتش‌بس،
ارتش صهیونیستی اطراف شهرک الطیبه در جنوب لبنان را مورد حمله قرار داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/675110" target="_blank">📅 14:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای سفیر کویت در آمریکا: دولت کویت در هیچ گونه عملیات نظامی علیه ایران شرکت نکرده است و نیز اجازه نداده است که از خاک آن برای انجام عملیات تهاجمی علیه هیچ یک از کشورهای همسایه استفاده شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/675109" target="_blank">📅 14:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای زلنسکی: شناورهای مرتبط با ایران را هدف قرار دادیم
🔹
رئیس‌جمهور اوکراین امروز در پیامی ادعا کرد «در حملات دوربرد خود در دریای خزر به نتایج بسیار مهمی دست یافتیم؛ از جمله شناورهایی که برای انتقال محموله‌های نظامی مرتبط با ایران مورد استفاده قرار می‌گرفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/675108" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تیزر قسمت دوازدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم نرجس اربابی که بخاطر بیماری زمینه‌ای، در میان روزمرگی‌های زندگی، به ناگاه روح از جسم جدا شده و در مکانی از دنیای برزخی پاسخ دهنده و نظاره‌گر امور مرتبط با حق‌الناس از جمله حق پدر و مادر و همسر می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: نرجس اربابی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/675107" target="_blank">📅 14:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwfiD-SS3LZhdfaFgv3zNS3oz6Ee20Z1XlGsfEFxhtpPJrn7NSXvzkvz80s9AEsguQZ7YazIwrJ9CUEJ3dgVoB08JhIlEqKbzY4_OQEoSjes3aj6xHWv6drJYy203Y9sr4GZ0eEnOp1GCvug8Rh010hc_0_gp-AgI-fHrpLF2IW8dodF-iiVMyuRaMNXiMdaExva20yMdlW3CT0acw2x-cd0YL7NRLMoSHzA4-P6SrEufAQlbECXHUOhjD9RZOVdbH3ZCHAChBtgVaUqWS-qd-aIdNSW8j7YO0NoG_IZ8lYkvW01hv99t0pSYjZmSomizmbrGtM5H1sX8iRgsET2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ کد کاربردیChatGPT که هر کاربری باید بدونه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/675106" target="_blank">📅 14:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iq_wi4Pp0N8QNH5fvI1pRgBZzYVp9QbQe_ZEgt1doVQ-9ZPwmtz9hZ0WutBfJBs9dkfCavky56O6HdMLOakfqav9nWuGojrIb2Kd7u8bTp9bxqESju60qmoCWQGtLyC4UkJA3zoE9XShpaV_eEPZhURn1sftdpVmPbGeN_zxTqfUEsH4giI6XVSK-MJ6A3FXNDIul7FU7K211ggoSOMJWN3aIVZeoXIZUqw6ll5PYmfnCwF6cYtMSTw3O3YvSiFG0hvSweIGJe4uw2CxA0HnDl-8IeZre4Ve63tnbqYNUe_fnQHP1EYFNDRNCyXLc13a-QVuJMR-EhRSOWiXg3Hnjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر از این کتونی‌ها داری، این راهنمای استایل رو از دست نده
👟
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/675105" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675104">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEMhEuh9RalwHYYQMTVvqADOXLWEDGvBMkhc0nDQbv71_SEVz-2vK9rrQbKetWLaBPbkfDx4lCvKyQIgvx5fqiQOE4QlHQ9hNl4v7pwMHuuCKENEpkWKzP1r70Vs8PuYAgbkl0SeXEr0e55rXoKF9oczSw2Qm6vMMgH8E7YAdLJJfUbfgJhPRZfqq_KRafnTb3zGjjDDW045t_868-k0CDlWzYQQ85-IF_8xnHu40F6Ip0tSbRkFHE7L00naOOsBs7eOVyaIylFHJF6oXhyjwBHPQKIu8i4qD-UIHSevER6Sslui3C1v4yoFqK-_q6gyyh86lAL_3RNv-pxYRqfxNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انقلاب بزرگ دوروف؛ تلگرام ابر برنامه شد
🔹
پاول دوروف، بنیانگذار تلگرام، رسماً اعلام کرد که تا پایان تابستان امسال، یک کیف پول غیرمتمرکز را به‌ صورت کاملاً بومی درون پیام‌رسان تلگرام عرضه خواهد کرد.
🔹
این کیف پول که با نام تاریخی «گرام» احیا شده، به گفته دوروف بزرگ‌ترین عرضه یک کیف پول غیرامانی در تاریخ خواهد بود. اگر این پروژه اجرا شود، تلگرام از یک پیام‌رسان ساده فراتر رفته و به دروازه ورود کریپتو به زندگی روزمره صدها میلیون کاربر تبدیل خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/675104" target="_blank">📅 13:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675103">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رادیو رژیم اسرائیل: ارتش در کرانه باختری دستور توسعه حملات دریافت کرده است.
🔹
۴۹ نفر در کشور مبتلا به تب کریمه کنگو شدند و ۵ نفر جان باخته‌اند.
🔹
راه‌آهن: ۳۰۰ هزار صندلی قطار برای جابجایی زائران تامین شده است، نرخ بلیت‌ها افزایش نمی‌یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/675103" target="_blank">📅 13:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675102">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3aa067437.mp4?token=cRsq1acM2lStKQX2PCE0Baf7ejX1Ahu6OUTxRdfCiDDy3Fx-tChNP2eMiPRSn4VX2Jl4vJRaThDloUty0ZHjUGzBJBI0OnFaAoG6ga5YyGgE-GjYZ-3O6ztgrO7b45kLpGwxSJQc0fDenVctsNb6RcdgfAdAeH_X9TDURF1giVIKwXrTLSgHmxO9ze04j04zQO7LfZwevvCU2ZaRIcykU-F4V6uTFzyaV7Tiub0OVK5GbaRDMuN_lLu-lo21CvOQrJtkyPrzjzktKtYErI-aMAPxihxC_QAf1n1y9cf1-bmKtrURT9LTLPy44ML6MPPIRGUWNbJGGjCYonK8CA4ZqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3aa067437.mp4?token=cRsq1acM2lStKQX2PCE0Baf7ejX1Ahu6OUTxRdfCiDDy3Fx-tChNP2eMiPRSn4VX2Jl4vJRaThDloUty0ZHjUGzBJBI0OnFaAoG6ga5YyGgE-GjYZ-3O6ztgrO7b45kLpGwxSJQc0fDenVctsNb6RcdgfAdAeH_X9TDURF1giVIKwXrTLSgHmxO9ze04j04zQO7LfZwevvCU2ZaRIcykU-F4V6uTFzyaV7Tiub0OVK5GbaRDMuN_lLu-lo21CvOQrJtkyPrzjzktKtYErI-aMAPxihxC_QAf1n1y9cf1-bmKtrURT9LTLPy44ML6MPPIRGUWNbJGGjCYonK8CA4ZqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: آستانۀ تحمل ما در ایران تغییر کرده است
🔹
توانایی حملات پیش‌دستانه به دشمن را داریم و آن را در عمل نشان داده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/675102" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675101">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04ebc19f4.mp4?token=osUMpzTyzrhk0Ew__uFBuCx1zKAumKIPjOOq-miLS05QT5MsPWTwXTBANcA5UVlYliDDXdTK4ZKogNiLKZ1zIUTd0x3p1Gu1AlA4MUo8-EHlLuiNJW9N95UZ1QAUBNjputybZ9WsBp5rO53A5jU5HPdjyAj9jHlHJPkoVvPq7QTU3X65VhZZRgzYyCqFV1RREt5IClyerrp4RBYKadbd4DuwoNUtSD6tHUANEu33B-Xb3l8KvK-9UzFUlOF09Zyz1sSBXlL1l27HLyYZwDXtVq5e-L8tZSlWEIl-DrXsbH3sfOwJP2eQg3MRHuUjiRr-Wk4B4TBSePLZJe7h1K0Vpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04ebc19f4.mp4?token=osUMpzTyzrhk0Ew__uFBuCx1zKAumKIPjOOq-miLS05QT5MsPWTwXTBANcA5UVlYliDDXdTK4ZKogNiLKZ1zIUTd0x3p1Gu1AlA4MUo8-EHlLuiNJW9N95UZ1QAUBNjputybZ9WsBp5rO53A5jU5HPdjyAj9jHlHJPkoVvPq7QTU3X65VhZZRgzYyCqFV1RREt5IClyerrp4RBYKadbd4DuwoNUtSD6tHUANEu33B-Xb3l8KvK-9UzFUlOF09Zyz1sSBXlL1l27HLyYZwDXtVq5e-L8tZSlWEIl-DrXsbH3sfOwJP2eQg3MRHuUjiRr-Wk4B4TBSePLZJe7h1K0Vpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خرسی که به‌جای فرار، بغل دامپزشکش رو انتخاب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/675101" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675100">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlKJHgrtaAxI9Jto_5v6LUhbLJ4J7sQ_aH9DNy3Q3rXWavq2sYqPtQsQ30yLGn8mJ1UtXl4XTcZYTjkvdKCOHJ7el9ltHlw7NWqbIznc21w1iu0NI_NJa_q8AzggAgnQnkfwJ9p6oOHvijqMG4gPxR-lt6wJ0Q3KwmfPXkDlhuk_b316PH1wJOEVfcQB8_FWWFAY97OHekYJNmL2sCI72ZJa3io5CvkfiJzJzZZTckL5YMDEZKAQthEuq_0-L5sGDXMXIyTofa4bd2Tb1VyetzeZFxhVPXyu9vuSFTJwbeA6LQf6WfsiNRwmbGlx0EWp58bZv34E6T48pN25W_Eaww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع خبری از حمله جنگنده‌های عربستان سعودی به مناطق مختلف استان‌های مأرب و جوف در شمال شرقی یمن خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/675100" target="_blank">📅 13:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675099">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd598f420.mp4?token=cn_gN7m9gxc_O6DAb_BUBE9oKiOdNmPitsD05MsHE_fZ9fAFjpMbgvDFsCgqaSR8YmYobXoNIc8J5SaFd6C1rid750xiIOVGA2H7ELMMMwMZ60kY35znKFARDVSLrYvKVx6ySG8LmaLW2AyF8vSZ0MrBgAFht102DZVTsA20tXBlml0huYtEe0szdtrtT2t2R0Tr97VxAxZKza8dGZRZKCXjFS1sHDKoVeyBs_ojuljnDu6K73nVvr2ZNsh48ET314k1L42P748uCNIgG07sjco_6xHiJzAk2_Icn7_Fu6MkfU9shqVMBdOFeZZkdPm6TYIEtoQ2hMnOGZ-kJLG9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd598f420.mp4?token=cn_gN7m9gxc_O6DAb_BUBE9oKiOdNmPitsD05MsHE_fZ9fAFjpMbgvDFsCgqaSR8YmYobXoNIc8J5SaFd6C1rid750xiIOVGA2H7ELMMMwMZ60kY35znKFARDVSLrYvKVx6ySG8LmaLW2AyF8vSZ0MrBgAFht102DZVTsA20tXBlml0huYtEe0szdtrtT2t2R0Tr97VxAxZKza8dGZRZKCXjFS1sHDKoVeyBs_ojuljnDu6K73nVvr2ZNsh48ET314k1L42P748uCNIgG07sjco_6xHiJzAk2_Icn7_Fu6MkfU9shqVMBdOFeZZkdPm6TYIEtoQ2hMnOGZ-kJLG9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: تغییر قیمت یا سهمیه بنزین قطعی است، مبلغ کالابرگ افزایش نمی‌یابد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/675099" target="_blank">📅 13:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675098">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تصمیم جدید برای تامین برق صنایع کشور
زهرا سعیدی مبارکه، سخنگوی کمیسیون صنایع و معادن مجلس در
#گفتگو
با خبرفوری:
🔹
در آخرین جلسه مشترک با وزیر صنعت، معدن و تجارت و معاونان این وزارتخانه، مقرر شد صنایع کشور بر اساس میزان نیاز و تاب‌آوری اولویت‌بندی شوند و فهرست این اولویت‌ها در اختیار وزارت نیرو و وزارت نفت قرار گیرد تا خاموشی‌ها به‌صورت هدفمند مدیریت شود.
🔹
بر اساس این تصمیم، واحدهایی که آسیب‌پذیری بیشتری دارند باید در اولویت تأمین برق قرار بگیرند تا خسارت ناشی از قطعی برق به بخش تولید کاهش یابد.
@TV_Fori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/675098" target="_blank">📅 13:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675097">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L48IwmtT1YQGYgz6eXmKDus9A2NEeWVA5o9PW6-pQWIfmxdTj3Xb1GN-ulauZ2m6eDcYrDSLB-0_JCXXaqDB5Xdnpifc7_sj74qxv4ysjylSxJJaA9St7L62KN4uu-s9kcv5p51_L3Nclwv2GyNKu3ulADvbJs8SWg3VAdawdTQ65KiAz1zUms8pu9DGiq2Fhk-wjiY4x6R9eM5XxQhjdJ-ePzm0yutxY5O8aV57jNjb4rSsc_cJgkllc2Nz5vwIMfsaJEsFpSbfkWqDBFmrIC8CHlLBk7wCY3KhIirF_78M_uTJ1jJel3YRwB_bca5odHn-UmoOZPmCshXrXTriGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذوالقدر: شلیک‌های مداوم و هدفمند رزمندگان ما، تا تسلیم کامل دشمن و گرفتن انتقام خون کودکان مظلوم میناب و لامرد و... ادامه خواهد داشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/675097" target="_blank">📅 13:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675096">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca97763004.mp4?token=hRwLp6SjzcNt0fcSnmjqB7ImLA3IWCUpss-nsVcd9XOro4OaeubN9-Be7iwoOWuCNCrdccIR1oppyB8_AggrEULjp1NuMYKl3xIo8Lvm4kzMW-SbK5nBfOVMOCZL6Q76dpVtTCHmUD_6y8ipP6UQIq1wn4r4lMoturm7ikI9yLaMdP_plU1_2vGiSibqvBussy2DT2_0ZsSJ_0R-8CHTYI9y9n6-cU0oCAa6IJkWpZHfojSJr-6Z8PjtcXbsUkPARqzgxYCQfScCOLH9SUlabSZsBL0eiiMVnFuB60rvIVw7aCcx0jaIy0I4QrsgOmEsE5kkZ6A3FiSxpnFN_QluVE4uxUVRD61655z8Dsbw_8y5EEZz-7K52IyQszC4woXUh1USMIwq4UVHjWOV5JGs_2saRwchMN5rwITFIxT3DbmMrii1R8QsgWEapS_KgZC0H-eHE5DJ-oWOWrfF9Wk6ys4jK-aDlOQNxkgRDXzuqjTg2Cx1bYjqHyJvIvfbyeDEwE3s8XGXxJhkNDvpKBqUQyD79ja2KZ563TrUfiXnkN9FHKjuHY-eTfQFar862k-lMoSvJbOL8ktZ0zDgGw4ym6H-9kU8hx0FYAZ8eTOHaAPvT0cw-VSS8-qXJ0greQOIg9YHcpEX8VRci_ctKYDR9V3icce9pFKReC2WtkqLSwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca97763004.mp4?token=hRwLp6SjzcNt0fcSnmjqB7ImLA3IWCUpss-nsVcd9XOro4OaeubN9-Be7iwoOWuCNCrdccIR1oppyB8_AggrEULjp1NuMYKl3xIo8Lvm4kzMW-SbK5nBfOVMOCZL6Q76dpVtTCHmUD_6y8ipP6UQIq1wn4r4lMoturm7ikI9yLaMdP_plU1_2vGiSibqvBussy2DT2_0ZsSJ_0R-8CHTYI9y9n6-cU0oCAa6IJkWpZHfojSJr-6Z8PjtcXbsUkPARqzgxYCQfScCOLH9SUlabSZsBL0eiiMVnFuB60rvIVw7aCcx0jaIy0I4QrsgOmEsE5kkZ6A3FiSxpnFN_QluVE4uxUVRD61655z8Dsbw_8y5EEZz-7K52IyQszC4woXUh1USMIwq4UVHjWOV5JGs_2saRwchMN5rwITFIxT3DbmMrii1R8QsgWEapS_KgZC0H-eHE5DJ-oWOWrfF9Wk6ys4jK-aDlOQNxkgRDXzuqjTg2Cx1bYjqHyJvIvfbyeDEwE3s8XGXxJhkNDvpKBqUQyD79ja2KZ563TrUfiXnkN9FHKjuHY-eTfQFar862k-lMoSvJbOL8ktZ0zDgGw4ym6H-9kU8hx0FYAZ8eTOHaAPvT0cw-VSS8-qXJ0greQOIg9YHcpEX8VRci_ctKYDR9V3icce9pFKReC2WtkqLSwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران به تکنیک کور کردن چشم آمریکا رسید
🔹
پاسخ‌های نظامی متفاوت و کوبنده هفته قبل ایران به آمریکا سران کاخ سفید را حیرت زده کرد.
🔹
ایران از توانمندی رونمایی کرد که مقامات دولت ترامپ فکرش را هم نمی‌کردند. جزئیات این شگفتانه نظامی ایران را در این ویدئو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/675096" target="_blank">📅 13:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675095">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3aZm8Hkcz6xv4Vj7_aJaAJsxaEfJUgGQm9wrnnJCZslmGWsxGXYFRqB3ppozgDsysmnlZ7GD6eAji8X9tjyyDPkdGLWJXNxbo3IEPmw6ZYsNyELFBwmDgtq9coENEH9DdrMtDvj8gFvfBkAPqAzDWuxfN_eq9gmTMQCWSohgFtahBPwFYE0QUBh1a0j9wt1Tp-1labKQMUaUcRuSLYJeL-EELhCsWp_LIA4XAaCVIzgzout4JDtDdKSyCLLbz085XppFQxw0xJaxG9wbPwbqmznmExk03zqGth6y-94pXNxTTVU7mKJ7swwiWi65vMA6XQpeFQ2bZpkF462FeSD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا ترامپ از نفت بالای ۱۰۰ دلار می‌ترسد؟
🔹
هر بار قیمت نفت برنت از مرز ۱۰۴ دلار عبور کرده، اقتصاد جهانی به رکود سقوط کرده است.
🔹
این شاخص، ۶ رکود از ۶ رکود را با دقت ۱۰۰ درصد پیش‌بینی کرده!
🔹
ترامپ به همین دلیل است که از افزایش قیمت نفت وحشت دارد؛ آمریکا در باتلاق جنگ ایران گیر کرده و نخستین تاثیر ان گرانی نفت است.
ترامپ به خوبی می‌داند که عدد ۱۰۴ دلار، خط قرمز مرگبار اقتصاد آمریکاست./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/675095" target="_blank">📅 13:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675094">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQfeJ3SKx6wGx_UrQ5FpJD-3-tKxsJhzyuwvT20BUWh0nOAvLYWsjHJyjmatO3PkjdRTgctkF5-6eoRzPxWg2MQ26ZbMB1NUZiW4WB6VJoXdMHa1EOyUXUBdWP8ZExr7UNZqmCprFucV8z0Fp3rBDCLXjIU5OJd17Z6l8Y_cbaV1rO6Sj7jLxPwjMamHqNDJZSStDqtF0hNcPvfBe-0GSL_4VKEpG7kT0kIuX6UVBu-s2qobhdu34sH4tsrXvSl-o1aM1M2BKMpBbTep9SoGjvmpvQa2GXGBhQFhsyL5pqxBeguvOLWOlywbcX1yNEjyTZD5ncKC4bPuQ2kkXinfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۳ مرداد ۱۴۰۵؛ ساعت ۱۲:۴۰
🔹
بازار طلا و ارز در شروع معاملات هفته، با افت چشمگیر قیمت‌ها مواجه شد.
🔹
قیمت دلار آزاد با کاهش به کانال ۱۹۱ هزار تومان عقب‌نشینی کرد و هر گرم طلای ۱۸ عیار با افت قیمت روی رقم ۱۸ میلیون و ۳۳۳ هزار تومان ایستاد./ تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/675094" target="_blank">📅 13:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675093">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALlu6eIZyBqHiReOpbeFxoVhugs7Sbh1cGAOEqLEARm8sJLc121dHIBmvbIePMaNX2EfjRV84O4w1YTAhfR5dEbZyOtKso6nuJtzQcDhAHdQRHc3KsD_wHN7cSy-NoREEUSv65bJya99aJluRWgDrQbCs3ErJoa9dn5qs40J5R09S3mbrMzBqK5AvhLuqU7BWIsJlzkYbn5P9vw5oejkzrD2HTWV47-WyFHOsaQOvK9gAIYby9qP1wFwOSkkU8UzPpMRNNPSoSKa3a4nqrmeQNkGpDYcT254eYgOsbek3zZ3my_BFuvTKH_Snq_QReMlUZbtEXjeNl95STubCmPpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام مرکز داده آمازون در بحرین؛ ضربه به شبکه دیجیتال ارتش آمریکا
🔹
تصاویر ماهواره‌ای از انهدام سومین مرکز داده آمازون در بحرین خبر می‌دهند که وظیفه پشتیبانی اطلاعاتی و ارائه خدمات ابری به ارتش آمریکا را بر عهده داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/675093" target="_blank">📅 13:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675092">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/og-2UnuU2-71xq0wuRIOgR6rLT5SzfiHfBvEPUP_MN2jmqVC5Nt0CryjEqRyBAEcleqARYbs3dJv5YqqL-96j_2AfEz3P_wZ4RGqEoDzbuOXIfxesWgd9mE7p0gapdz1qOJOgN6e6i5wvIsye5X2yf3VTrAg7VsYjbOZn5iLNitBBEE6RxV-PIG1GaH5C3LcYJ58_1MUWqNd0Z46Q65WfDkDDDk1s8G63P242MV7PM1spewSqW_pUrABzORDaJfNMCT45gmqaIuXSdTdpP8SFNlxelxTM_tvH4Se3JlXrU5fR_obWHDTYwPaB108jFxadn2jKIrYfFrUAIb8_7Xf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬅️
درکنار ۱۱۰ شعبه‌ منتخب در سراسر کشور
⭐️
بانک شهر ارز اربعین زائران را در مرزهای مهران، شلمچه و ترمینال سلام فرودگاه امام‌خمینی(ره) تأمین می‌کند
🔻
همزمان با آغاز سفرهای اربعین حسینی، بانک شهر با استقرار گیشه‌های خدمات بانکی در مرزهای مهران، شلمچه و ترمینال سلام فرودگاه بین‌المللی امام خمینی (ره)، ارائه خدمات ارزی و بانکی به زائران را آغاز کرده است.
🔺
به گزارش روابط عمومی بانک شهر، بانک شهر در راستای تسهیل فرآیند دریافت ارز اربعین و ارائه خدمات مورد نیاز زائران، گیشه‌های ویژه خود را در مرزهای مهران و شلمچه و همچنین ترمینال سلام فرودگاه بین‌المللی امام خمینی (ره) راه‌اندازی کرده است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/675092" target="_blank">📅 13:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675091">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec75536af.mp4?token=qGC-QJ3-cGOpUGR9jIF09t6ehpi5cUjhdaQlVoJuPtprbEchG6s5_lblT9hjT0ltCS_ezCBZa4CZC5uDSc4ungYfN-RyITb0af9-NPprpJQkgjduh748ZRDueuUNVkcPtyfXZmNXJdiqZMGe7Cp8CnG9pKVm2_OhVoDM7IKGekPYXfsj0b4RDhY36-oteo6PjiydRLra2W5ZsZ_RSZ--Tr0wZImaK-ax6jIfnFICcpud8r5P6dr-AXGqUvTYCyzQVhcXg7wZ4bMKbx4V2QdsgREHi_fgMzgxeTokXG90HGOdcqAPMxJ4CjUtE8OKCryV8Cch2Xxn7WchL6j9oYAidw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec75536af.mp4?token=qGC-QJ3-cGOpUGR9jIF09t6ehpi5cUjhdaQlVoJuPtprbEchG6s5_lblT9hjT0ltCS_ezCBZa4CZC5uDSc4ungYfN-RyITb0af9-NPprpJQkgjduh748ZRDueuUNVkcPtyfXZmNXJdiqZMGe7Cp8CnG9pKVm2_OhVoDM7IKGekPYXfsj0b4RDhY36-oteo6PjiydRLra2W5ZsZ_RSZ--Tr0wZImaK-ax6jIfnFICcpud8r5P6dr-AXGqUvTYCyzQVhcXg7wZ4bMKbx4V2QdsgREHi_fgMzgxeTokXG90HGOdcqAPMxJ4CjUtE8OKCryV8Cch2Xxn7WchL6j9oYAidw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شالیکاران ژاپنی از ربات خورشیدی برای جمع‌آوری علف‌های هرز در شالیزار استفاده می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/675091" target="_blank">📅 13:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675090">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTkNgVBEXWFLZsyMffm31HMZ96Q_13duIdbFxgczqw7yeBA7cfr1jnwcIgk34JEQ14rFJ0gxPK7_gCk3yG-VIuq9Ef2QZis4s4N7QBLG-I9zCnKtx0AhgdbusAm0b-KmT22_REkoj61esoonHXa6FaRHhJzovPj2nApjwz2kQpLF54L-TMqpKXt8WdrymYnIUG0D3N1XsXcCidtknTLh2ZkCmAGqtHdezUy7FJGyd1anmJpvs4VTsjRrUNKoFeet3wpBXSETU-kyVJJjFL8ihDvdyJadQWtdtD9-ipJRaRBez8F_AV87k_3iIQcbkkJNzxgOJGn1ICbaTbzBwJy3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفتر فرماندار کالیفرنیا: ترامپ حرامزاده است
🔹
در پی اتهام‌زنی‌های دونالد ترامپ علیه «گوین نیوسام» در ضیافت خبرنگاران کاخ سفید، دفتر فرماندار کالیفرنیا با انتشار پیامی در شبکه‌ اجتماعی ایکس، رئیس‌جمهور آمریکا را «حرامزاده» و «خوک» خطاب کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/675090" target="_blank">📅 12:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675089">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snZoLh-WVDolkecH_WPRmoh9otYnaxhlKFhnNMOZw1wfwjR8g29MtpEi0GJ7DkXAQ8yo12Bw4m7MnNyenHXiA6xXrL-orqkg9pMbd_-kamptstcncVB8Pszi8pBOBF7nAaJk95WlCDmfavwgNQvHlgcKIq3Eme7Blnn8AqsaqpoyJsE9_My-BMFbuLhHZL4-x53Lhas5MyjwU1RcBKjTLoSsWnbN_n87XI6B55qXsSc5bm5Ch3EVaHb8FOShl89EfpJebY87aDqBbWjb8ijeVBhNpjN77jMzj_7k0ji19hjRbjVpeXMjdyeHiYj_-dFb23Pu8CLkkKYK6MBQFkHpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماندگارترین نقش‌های اکبر عبدی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/675089" target="_blank">📅 12:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675086">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQDiTOwj-URxmCWdIufVLX6QzOkLEuG7SWNSdMl8xZmEAdih9pcAxnwsFAxx1LLnIJcjSkViawK5z_ls7Mkqf21My_OVX7YVqGsy7QsNp4M2wOhElg88I1ur_7vpFH1kWbMVnTGHEcntSM3KnT-ie7Ro_s-k85-vXndkmP2ojMY_vVPXfscT5aCoN7yU1LtzrEDMakK8HWW-BA6SZct6MEIza-Hj3oFVSG_CKu__B1I4MAqtYaIYXYNqzvamFIWVWn6rJ3ZP44KvYZepwXbVF0vj3wEw9jn4Z3CcVKGLktEBGwFAPLIxaoy5X9tLd6ybVaWfRPbz7kob25IBmLaXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgz0w68PJPQ6_OMMTXu772n3TDZrtyfTFhzLiIwBLlV0oS3UtgIyZvp7HDOzXr7lqEl3JFD36_awjdCR0uporkRpn4VGd4iJHMoWUMfBwHmskVHj1syhuKi5P4H3owJ8RXY0cha1cqJFj1gjlsq6g4APMpE_P7NMJ2A_tiqnOP5tOSUiN_d99a6yNFDoCu9koRbHzVlJUhu63x8MjZO2cwqCmE-EktjH5RcuyuyazmgdU_cPZdkQ8Sz7kZ6t4pGCHnAuyFVkKhVvgudAtL8NHKUkxOzbiGYJw9cACoiKbU3N2qWD0y0bfuJjha5HGs98x7hvaDUyLtsF8Uo9R4ZklA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر ماهواره ای انهدام کامل سوله مهمات نیروهای ویژه ارتش امریکا -پایگاه ملک فیصل، اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/675086" target="_blank">📅 12:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
فرصت دو هفته‌ای بانک مرکزی برای رفع سوءاثر چک و اقساط معوق
بانک مرکزی:
🔹
صادرکنندگان چک‌های برگشتی و صاحبان تسهیلات معوق در بانک‌های ملی، صادرات، تجارت و توسعه صادرات که در بازه اختلالات بانکی اخیر دچار مشکل شده‌اند، دو هفته فرصت دارند بدون ثبت نمره منفی در کارنامه اعتبارسنجی خود، نسبت به پرداخت و رفع سوءاثر اقدام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/675085" target="_blank">📅 12:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675084">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای گاردین: ایران با فناوری چین و تجربه جنگ روسیه و اوکراین، پایگاه‌های آمریکا را هدف می‌گیرد
🔹
ایران با کمک تصاویر ماهواره‌ای چینی و تاکتیک‌های آموخته‌شده توسط روسیه در اوکراین، پایگاه‌های آمریکا و زیرساخت‌های حیاتی در خلیج فارس را با دقت فزاینده‌ای بمباران می‌کند.
🔹
ایران توانایی موشکی موثری را حفظ کرده است که رهبری جدید آن مایل به استقرار آن است.
🔹
موشک‌های ایرانی دارای ناوبری پیچیده‌ای هستند و همزمان با پرتاب به سمت اهداف از GPS، BeiDou چین و Glonass روسیه استفاده می‌کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/675084" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
واکنش شفیعیان مشاور رسانه‌ای دفتر رئیس جمهور به مسدود شدن خبرفوری @AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/675080" target="_blank">📅 12:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/795cca7353.mp4?token=jZ_BUs2F3pBWmqZUn000UeN6Rt2VXFBJbXmsIi0yRLoGtXtYtgfeGTB8_0-VB3Ywh5Cl7jFG6PFhprfJsLcjdtEXCYzULIFE7I7nn3dBlwp3CRfz3t4ZS5TZ4jOrZt0dDTQHh0nQJWNj-MAJavi-TSu0sCqH8Yx_KKUoYCSunggz4J1h6GzhUJNhBr4YtexmxLU7upDErhRS3PCNhCW5jtUPNntIghdngHuMeJTXyhVWqRdHVc3yvAQTtZn5NATakZKethNejXIylBtVOumPqeJm1HIkrIsWY5Qma6gv27PfOabh45qGVRB770Qw5ty1BeFrAFEuCmgj_y6t058DWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/795cca7353.mp4?token=jZ_BUs2F3pBWmqZUn000UeN6Rt2VXFBJbXmsIi0yRLoGtXtYtgfeGTB8_0-VB3Ywh5Cl7jFG6PFhprfJsLcjdtEXCYzULIFE7I7nn3dBlwp3CRfz3t4ZS5TZ4jOrZt0dDTQHh0nQJWNj-MAJavi-TSu0sCqH8Yx_KKUoYCSunggz4J1h6GzhUJNhBr4YtexmxLU7upDErhRS3PCNhCW5jtUPNntIghdngHuMeJTXyhVWqRdHVc3yvAQTtZn5NATakZKethNejXIylBtVOumPqeJm1HIkrIsWY5Qma6gv27PfOabh45qGVRB770Qw5ty1BeFrAFEuCmgj_y6t058DWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/675079" target="_blank">📅 12:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
گاردین: در توان موشکی ایران یک تحول واقعی رخ داده است
رسانه انگلیسی به نقل از کارشناسان:
🔹
پاسخ ایران به حملات متجازوانه آمریکا نشان داد که ارتقای توان عملیاتی موشک‌های ایران با تغییراتی در فناوری و سخت‌افزار این موشک‌ها منجر به «تحول واقعی» توان موشکی ایران شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/675078" target="_blank">📅 12:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCITuzzXTXNl5s6h7AzRj-3YTOI705i67GpJhZsd1AEiHWqIrmYBRTe5r5Tui7Rz3LYUQl8pPuE9zIT9uW1OkxSgTp0YvcskgFDusVLTWfHsYFrC06Od7JGhJo5tuBVHFrrpncw-p94FvpeBjPqMTC1M1eOsUnHRHCbKFmKK1Ipg77Gy46PlzBoHOPXtS4Q0e_B_f5dZP6Cs7knfbvydKo-VrH8dHV8-sJaGfNXwGuAc5ic8cgFtlNkaqLHNNzDd11lqmvfKSn5Z5q2ave4I7Md_7wVFQZqnyFzm3WQgOrOSq8UIbsid0VJwNh4_M9pMozeX1mzfSF42I2Pbi0f-Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/675077" target="_blank">📅 12:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e498ed3d63.mp4?token=eBQAbySaJ6vOb53jsrkKEJ7uXrILPlwNYLbYWby75vsJd7E7TCo2q-lWevFtspCokW70RPsBJDkaJTR45Vka_-F-Mer1HSF0qDpcPnxmPTgXTvktLTyOJMNwxdddTaEbTbwV85gqVOaAdfffLhxoQEIBapASUFZ0NciH8T56crA3aJBGRG0a8Zzd9rrE3gFUHCPelKYG68FLh9uj_XXJfBYDvx_H1gQkaWwxhmwb9AoD1trHxrZrkIwfSC_cnxA0KpS6BQGOAwLY93zRO3NCEUqhj3ehodg3O7UZHA_FVf7XpWUaOiqCs7wU7GG9OsyJgOk_GlyKV0hlEwbf_sA7Txw1riCKRTRcA3aM1mW0oSM9UMNp0NQWTE_jMzoZQw2DHbID6AOEQvscjRpHFMjj2vcVHoP4jf7iAep1CpEuEVvVGPkPKw_5HmAi3OTJvOkY0iSiJD2e-lv__OehX5a_rJo4_Pu4f5LYet3JktHoXY5KOxLJf3-VyCXM1yuz7oA3IN7cqyiFlVC3O4uVjN4n2X0G-dvXfJJ54QKDqNAIkOhgD-Eb8HfoBEWBhPZhzs1vC_G_M-GG8xtZz0kwNz6S7iX0uKMv41ONHUFiFRLe-2Xfb25VTPFzT_KBbZgL7fUt6eEmjXHkGF8bMKPjN0vexcKq9jM1IVNC3BwQgBNjdXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e498ed3d63.mp4?token=eBQAbySaJ6vOb53jsrkKEJ7uXrILPlwNYLbYWby75vsJd7E7TCo2q-lWevFtspCokW70RPsBJDkaJTR45Vka_-F-Mer1HSF0qDpcPnxmPTgXTvktLTyOJMNwxdddTaEbTbwV85gqVOaAdfffLhxoQEIBapASUFZ0NciH8T56crA3aJBGRG0a8Zzd9rrE3gFUHCPelKYG68FLh9uj_XXJfBYDvx_H1gQkaWwxhmwb9AoD1trHxrZrkIwfSC_cnxA0KpS6BQGOAwLY93zRO3NCEUqhj3ehodg3O7UZHA_FVf7XpWUaOiqCs7wU7GG9OsyJgOk_GlyKV0hlEwbf_sA7Txw1riCKRTRcA3aM1mW0oSM9UMNp0NQWTE_jMzoZQw2DHbID6AOEQvscjRpHFMjj2vcVHoP4jf7iAep1CpEuEVvVGPkPKw_5HmAi3OTJvOkY0iSiJD2e-lv__OehX5a_rJo4_Pu4f5LYet3JktHoXY5KOxLJf3-VyCXM1yuz7oA3IN7cqyiFlVC3O4uVjN4n2X0G-dvXfJJ54QKDqNAIkOhgD-Eb8HfoBEWBhPZhzs1vC_G_M-GG8xtZz0kwNz6S7iX0uKMv41ONHUFiFRLe-2Xfb25VTPFzT_KBbZgL7fUt6eEmjXHkGF8bMKPjN0vexcKq9jM1IVNC3BwQgBNjdXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بعضی‌ وقت‌ها زیر چشم‌مون نبض میزنه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/675076" target="_blank">📅 12:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_YZnPMFeERjML_eaUvyRkdyvPS8r_fgXus7IF9lbyWzFYiLrWK08pwNEPKu4-ZWBchDRZt5GO_tmSRB8eDQoRjtkN0pT0eK1ZmISSMnBA9HabmxSCVJYc-4oRAQuxMeWKoBvbsp10Srecax8LHrElm2PxUERlc_f8QnBH6iNqIgEg5ZOTNXYwIBxv5eZp5lX3f5otxTDjtOxWcA_nmSSpIqKQkX0qYyxb2M9QMSfAAqT4fE5dzaW6vBgvmQx1IIeiXk0CcUbBcnvIcs3YG79q8VW0lKhCzyqcwlIM-3jGmMEmgr9w8QSMYsIG6yqKeIrZAAMDk-28h9-syCNFCfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو در سامانه جامع
شروع طرح از ساعت ۱۰ صبح روز شنبه ۳ مرداد ماه
هموطنان گرامی می‌توانند اقلام مصرفی وارداتی را به نرخ مصوب با محدودیت کد‌ملی دریافت نمایند.
مراجعه به وب‌سایت رسمی سامانه تخصیص اقلام مصرفی خودرو به‌نشانی:
https://iranko.ir
.</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/675075" target="_blank">📅 12:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675073">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974a8f67a5.mp4?token=bkT5GP5VEkF5b3zPETT_n225RLMczHd-8K-Wj0VexAunnU6IW6rNH0o5CpTE7q4qmLcEq7E33CMr0JJa_iKYTKaZe56GCwD9Dw7hWoaPrbT5a3p8iZG8rJQy59dGNu_V7Ksec504DBplIX7mxLbN374cETf_YNmtngR9T8Ue2Zvnn2oV2umGAEC5MrhHWsc8Mg0mYgBqd8LN-QUwMKG6eBvRCrnOYkEHBkwxPi7vm4L_1wvKzrV6aUseVfH-Nr1aoUPro4l2zUnpHEFCyZgazgPg5XnMO8Z0QuA5eO6vDJNEm8pIDr5T-QYiOuJemq_VUzyHxocQoLrKOFZEsVDxQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974a8f67a5.mp4?token=bkT5GP5VEkF5b3zPETT_n225RLMczHd-8K-Wj0VexAunnU6IW6rNH0o5CpTE7q4qmLcEq7E33CMr0JJa_iKYTKaZe56GCwD9Dw7hWoaPrbT5a3p8iZG8rJQy59dGNu_V7Ksec504DBplIX7mxLbN374cETf_YNmtngR9T8Ue2Zvnn2oV2umGAEC5MrhHWsc8Mg0mYgBqd8LN-QUwMKG6eBvRCrnOYkEHBkwxPi7vm4L_1wvKzrV6aUseVfH-Nr1aoUPro4l2zUnpHEFCyZgazgPg5XnMO8Z0QuA5eO6vDJNEm8pIDr5T-QYiOuJemq_VUzyHxocQoLrKOFZEsVDxQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای جالب برخورد صاعقه با موشک چینی در حین پرتاب!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/675073" target="_blank">📅 11:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675071">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
نمایی از سیل و آب‌گرفتگی در آنکارا
🔹
بر اثر بارش شدید باران در آنکارا، خیابان‌های پایتخت ترکیه شاهد آب گرفتگی و سیل بود که باعث شد رفت و آمد خودروها با مشکل روبرو شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/675071" target="_blank">📅 11:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675070">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5d3f4438.mp4?token=GKDByJVZGes47_w00Csl-vxeZR4INeZtL2kNJYMWqbwmSYfpkObq3nSuFZrgqwHGrI9OfvpXxf09l6dZlE0aXMqF_qdWW4hJfAkH84SvhB38rw5Se-HSAcGwjMM_hu3F1issN6m7VgKeKDVRRDbcEqcaIVvGr_6sKlLzk0-nzTNcRIeVVtYa6UkCnSGQlTKN7A4kRxuPiiOo_FN9rAykPAh3TCksIkYZiMxaPtLMPyIO6jjE8kUBlur7PpN0kuDAWhS12J92n6j9NIQ6-qCIfgIpebP7wCOV8X4BalqVGeTCvee-rsY3JcUHHD8yDP67ExTlKeQtD6R8_5Mi1zIIWbGLC2CUP7y73w-m8lEwtBb4RgUN7LbrwNj0JVPJ7YGFKeoZavAYuHcbBwrUs_X6DmwWwZ32ieAEaO2eI4o3fTaHKcClhKIQRQxDaLXuNO1y7B8X2Gh7j_gS_lOvx2LCpQJUKbsyfFWznp5b3RgycOvzrFf1w1f7OPlLvy0N-dKK6NUG8UEmdGEYYXSsemyNxmhsu7ktIvpFhKNDMWDIoL6pKMeMt2rvvZxSKLTRwDv6mVaNOQuYZAMjINnW5tWPr3dJkiRwhg85188S0klt9CUe4pJLUyMzXK514eHMbRONe1RVczZbqB8v7fraCspcQpzHR4lQsilrtNLr8Hz8E6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5d3f4438.mp4?token=GKDByJVZGes47_w00Csl-vxeZR4INeZtL2kNJYMWqbwmSYfpkObq3nSuFZrgqwHGrI9OfvpXxf09l6dZlE0aXMqF_qdWW4hJfAkH84SvhB38rw5Se-HSAcGwjMM_hu3F1issN6m7VgKeKDVRRDbcEqcaIVvGr_6sKlLzk0-nzTNcRIeVVtYa6UkCnSGQlTKN7A4kRxuPiiOo_FN9rAykPAh3TCksIkYZiMxaPtLMPyIO6jjE8kUBlur7PpN0kuDAWhS12J92n6j9NIQ6-qCIfgIpebP7wCOV8X4BalqVGeTCvee-rsY3JcUHHD8yDP67ExTlKeQtD6R8_5Mi1zIIWbGLC2CUP7y73w-m8lEwtBb4RgUN7LbrwNj0JVPJ7YGFKeoZavAYuHcbBwrUs_X6DmwWwZ32ieAEaO2eI4o3fTaHKcClhKIQRQxDaLXuNO1y7B8X2Gh7j_gS_lOvx2LCpQJUKbsyfFWznp5b3RgycOvzrFf1w1f7OPlLvy0N-dKK6NUG8UEmdGEYYXSsemyNxmhsu7ktIvpFhKNDMWDIoL6pKMeMt2rvvZxSKLTRwDv6mVaNOQuYZAMjINnW5tWPr3dJkiRwhg85188S0klt9CUe4pJLUyMzXK514eHMbRONe1RVczZbqB8v7fraCspcQpzHR4lQsilrtNLr8Hz8E6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنسول‌های بازی از ۱۹۷۹ تا الان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/675070" target="_blank">📅 11:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675069">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d163b2e8.mp4?token=BYfoCWiE2wZpWMCNvLANFY0mZoZT1Pun_wxK28q8VcmcAzrxu7HjFJknDl3DmUPCvNDvig1Wa_4p2F8nnM2yhyYhj2V8yaBm1ENwl6BSIodYusT7LoRgjCNmltuo54NVV_LxCnNTUTnyEoEqA9X9qPTAEBlsP8X081kehZyHb9BcUEJGTv1IDsCrnRZS0b1Nv3fefaSAdtvo4Kx-hjgctPxHlGyLhh3X4k_NnIpA2UpWgdo3SvnJcxVG3ibekfsvQCuzKyVI6NkkO23q8WieBEW-SAlci-881frz61EHFPlR9eBh-eb-0g8QnbZPYUgwJDFHln1HAmc3I7tm7tA3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d163b2e8.mp4?token=BYfoCWiE2wZpWMCNvLANFY0mZoZT1Pun_wxK28q8VcmcAzrxu7HjFJknDl3DmUPCvNDvig1Wa_4p2F8nnM2yhyYhj2V8yaBm1ENwl6BSIodYusT7LoRgjCNmltuo54NVV_LxCnNTUTnyEoEqA9X9qPTAEBlsP8X081kehZyHb9BcUEJGTv1IDsCrnRZS0b1Nv3fefaSAdtvo4Kx-hjgctPxHlGyLhh3X4k_NnIpA2UpWgdo3SvnJcxVG3ibekfsvQCuzKyVI6NkkO23q8WieBEW-SAlci-881frz61EHFPlR9eBh-eb-0g8QnbZPYUgwJDFHln1HAmc3I7tm7tA3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
استوری اینفانتینو برای تولد مهدی مهدوی‌کیا
🔹
«صمیمانه‌ترین تبریک تولد را به یکی از بزرگان فوتبال آسیا و جهان، مهدی مهدوی‌کیا، تقدیم می‌کنم. دوران درخشان بازی تو در سطح باشگاهی و ملی، به‌ویژه نمایش فراموش‌نشدنی‌ات در جام جهانی ۱۹۹۸، هرگز از یادها نخواهد رفت.»…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/675069" target="_blank">📅 11:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675068">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCpgTdCNQsLwSYyYsrQoWPs9BClL-CP792dxJL-YiwoVh-IUaHnrZX4Twr6HLeA4W9gpvuHdnUg2nPbv5e50GUON6MIZl3Z5qJHVzDCietc6UQf_x3SRIoknYf9siTWmPkx5sc-YOoFO99HZMx1MvGtbuO9jl7o_bdWqfipzJUOXvlMynuGOac5fQ9AW46d3psIjwkJvcRlBnO25eyrxNPTuq2ocBRa7yo7wE_MFkkMYis1uJE5r5WsDhMgn1wLTjB-SZeY1w9o-2cBhFbICO3OYy9V2GdNA_XNy3td8FRwh2KhmxkRQFtWguHcPPI6tR_RxfgzRzVxPcwlBJD_8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه چیز درباره توافق احتمالی ۱۰ روزه ایران و آمریکا/ ماجرای سفر مرموز نخست‌وزیر عراق به تهران/ یا جنگ بزرگ می شود یا یک تفاهم غیرمنتظره
🔹
آنطور که از خلال گزارش ها می توان برداشت کرد، مهم ترین مفاد توافق ۱۰ روزه، توقف کامل حملات آمریکا به ایران و برداشتن محاصره دریایی از سوی واشنگتن و باز شدن تنگه هرمز از سوی ایران است. بازه زمانی اجرای توافق نیز ۱۰ روز است و دو طرف تلاش می کنند طی این ۱۰ روز مقدمات را برای گفتگوهای آتی و ایضا، تفاهم گسترده تر فراهم کنند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3232847</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/675068" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675061">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9eb476257.mp4?token=aqB-LGwrKGvHrb9GELALOUt3QQoQ1CV8jQNJ768NY1mc7NF9TLTEnNNBonYmTfWmFZjijY7Bi-bM-E_dO4K5NeEJghKrR_QccY1G8DzR2-B9tpM771BxKVBOI1jAyQ8PnMioWYMYDnspAhlMLNrwOZymDd6PFoIep1l7A8HibKSrpzfzMnVLJ1CkkctDjJbDrtoaq2vlsA5KLbllwqcscx4diDo2uAi4ePRTVK_YkcPi8wdrt6TIyRlNl-I_u9Zo23ufkmMDOL__6-FkRyB1ZkzJ_Dco5B-6P4gbx_y9kNj5OJdH1owyeE5ScHE9_CxWvR3QQoPG2EOJ9CCAHXDnqimcIyd0jtg2fMLsoRFb1eKf_zy765UQQTlDHJFlmEYnHTR0PjGd6UrocG2wiEIwm1EBnp4YEhn58Vjpn_3MotAplJDbRrff0D0hh5rq8u2N_D4TCIQIVah95QKMnM2Ec9sH9Hpo70amIBQLfHoD-OJVjkjxHKYg2XMheB_uX0xKzU5mTzZ00Ti_KgdCBstSbNbeRcZxpJZWxsgwroWwM8GVcpjKlORCfRlMLkXrmZSjQYmiMkD95WCCVDT-OsGhg7J4YUV29OSeWhXirllNHh4gqbUarOHF0_CMAtqPELGU3atwApL2i_x04hUlA7gy9YpnW-AhvRaNxHTOHqhuawM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9eb476257.mp4?token=aqB-LGwrKGvHrb9GELALOUt3QQoQ1CV8jQNJ768NY1mc7NF9TLTEnNNBonYmTfWmFZjijY7Bi-bM-E_dO4K5NeEJghKrR_QccY1G8DzR2-B9tpM771BxKVBOI1jAyQ8PnMioWYMYDnspAhlMLNrwOZymDd6PFoIep1l7A8HibKSrpzfzMnVLJ1CkkctDjJbDrtoaq2vlsA5KLbllwqcscx4diDo2uAi4ePRTVK_YkcPi8wdrt6TIyRlNl-I_u9Zo23ufkmMDOL__6-FkRyB1ZkzJ_Dco5B-6P4gbx_y9kNj5OJdH1owyeE5ScHE9_CxWvR3QQoPG2EOJ9CCAHXDnqimcIyd0jtg2fMLsoRFb1eKf_zy765UQQTlDHJFlmEYnHTR0PjGd6UrocG2wiEIwm1EBnp4YEhn58Vjpn_3MotAplJDbRrff0D0hh5rq8u2N_D4TCIQIVah95QKMnM2Ec9sH9Hpo70amIBQLfHoD-OJVjkjxHKYg2XMheB_uX0xKzU5mTzZ00Ti_KgdCBstSbNbeRcZxpJZWxsgwroWwM8GVcpjKlORCfRlMLkXrmZSjQYmiMkD95WCCVDT-OsGhg7J4YUV29OSeWhXirllNHh4gqbUarOHF0_CMAtqPELGU3atwApL2i_x04hUlA7gy9YpnW-AhvRaNxHTOHqhuawM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت در جیزان عربستان بعد از حملات تلافی‌جویانه موشکی یمن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/675061" target="_blank">📅 11:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675060">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
بغداد: جنگ ایران ۴۵ میلیارد دلار برای عراق هزینه داشته است
الحره:
🔹
مشاور مالی نخست‌وزیر عراق، مظهر محمد صالح، تخمین زد که جنگ ایران بین ۴۰ تا ۴۵ میلیارد دلار برای عراق هزینه داشته است که ناشی از کاهش شدید صادرات نفت است.
🔹
پیش از جنگ،  عراق روزانه حدود ۳.۳ میلیون بشکه نفت خام صادر می‌کرد که حالا به کمتر از ۱۰ درصد سطح عادی خود کاهش یافته است.
🔹
نفت برای عراق سالانه حدود ۸۸ میلیارد دلار درآمد ایجاد می‌کرد./خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/675060" target="_blank">📅 10:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675059">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2mTBCIL2amIc5X02Yecj3N_-cZMte2fct-bUV83oBRt6aDERD8wCGkB-Ehxtb2d3tqlh7V27Z9GMdEvNM0b9j0QsxEK6T8J-KR8ZhLjtNgHDfzekPZtlrUxh9CEOqa9998yun_vYSulUL26M0uqNfI5S-C3dVyC9YjhoQ11lMVlY0We8smKIa70oxW9PNzhVUfxuS3zy2ukxTeQyoqbFjuU4c4jcZeeC2SyljPFGEZa6IUpgZoVSwkc8fkNVy61cpYhO5WLbyOHYeiNJ-gaDslZcK4nLe0ZDPdJ5kymUtJztgGZTPfejxxrqcq7WuXw3jVd5BCIR3kbe7AaKNhkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جامونده‌های اربعین، این فراخوان مخصوص شماست!
🚩
می‌خوای توی حال و هوای پیاده‌روی اربعین شریک باشی؟ با شرکت در پویش «زیارت به نیابت از رهبر شهید»، هم نایب‌الزیاره می‌شی و هم می‌تونی مسافر کربلا بشی!
🔸
۱۰۰۱ جایزه سفر به کربلای معلی
🔸
برای ثبت‌نام در قرعه‌کشی، عدد ۲ را به سامانه ۳۰۰۰۱۱۵۲ ارسال کنید.
این فرصت رو از دست نده
@Heyate_gharar</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/675059" target="_blank">📅 10:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675058">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0ffd72ba.mp4?token=ZfJCeqZ28ai2nk1AdlmodXYanG0B8nHmW8LwBPvJblu1Sn-mhULzHlx1OLvghlDi5TIpsswLZCophGDaZ3R6H2jZa8Ivvo8nov5bbXqCfVkPNA_mMq-ZE43cuob4Q7TIivfDmekH6Kq7ZFMvZZWCbwrwLN1K6c5bBnNL9t6CaLhbj6U1DeMRYAdq1-cWhH8uSyHgXGBxXmxt5fUKpcSng1JuZ5tD6p2f8mhozZW2SK_hvoGQPWGXfFJhVxzLDg_oSgVmOMU8MG1Bfi3IU_4bq1xOXmSprAuIQ4fER6ZPBAy1JZPYhTu6BPM6xh29fnGHyoFkEpS66Aw6Cr_HCO3d8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0ffd72ba.mp4?token=ZfJCeqZ28ai2nk1AdlmodXYanG0B8nHmW8LwBPvJblu1Sn-mhULzHlx1OLvghlDi5TIpsswLZCophGDaZ3R6H2jZa8Ivvo8nov5bbXqCfVkPNA_mMq-ZE43cuob4Q7TIivfDmekH6Kq7ZFMvZZWCbwrwLN1K6c5bBnNL9t6CaLhbj6U1DeMRYAdq1-cWhH8uSyHgXGBxXmxt5fUKpcSng1JuZ5tD6p2f8mhozZW2SK_hvoGQPWGXfFJhVxzLDg_oSgVmOMU8MG1Bfi3IU_4bq1xOXmSprAuIQ4fER6ZPBAy1JZPYhTu6BPM6xh29fnGHyoFkEpS66Aw6Cr_HCO3d8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/675058" target="_blank">📅 10:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675057">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TivZAcFfc5u-gcSULSNUeEVe1dOAzXRLaCQUaVGZmSzRxtolmidFHY7AwB0egKRdpOv9obSiNFjyZvjnVXsc9RkrVSVAGU6XyQoAg0ELdgM068_SNRW7itVQj1VoEuqhztaSrll9l59-Y2MYrtdcJVZzsV-efrlTzV2dLryaP7sYySlPIi259aGHVj_MKI0erEQFy3VpTEtESCM1muP5-CJ7GcEy1xqXOedC5urrUTAZrCvIC-g-6Q3Y10DrFm4_whrKvy1yOuIm0qX8ac7ue1hcNhzU422fa144d95m-pTpGfl2Qq0KT1EMCnvv8kO1gtThVOzoxuWBp_xk4lsohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودمان را خلع سلاح نکنیم!  مهتا قره‌داشی سردبیر خبرفوری:
🔹
دکترین رسمی دفاعی آمریکا می‌گوید «رسانه، بخشی از توان رزمی نیروهای مسلح است.» این را پنتاگون سال‌ها پیش در اسناد راهبردی خود ثبت کرده.
🔹
رسانه برای آنها فقط ویترین اخبار نیست؛ یک سامانه موشکی در «محیط…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/675057" target="_blank">📅 10:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675055">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d6e30712.mp4?token=lFn6e8IiuHEGnfMLUtDHo_Jk77VAkJwWzQ9IweX-IMy8YbyzO586r58eZHVIyqCW-wDtfuncD6-lB7A6LppOR_g_cBJTliKyOgRd1y-1AOXciykH4Q67akPASpnnHeSubzA7HqQA3N-lLmHged6DYHnueCB7Raz4jzi6W76dQ_BL3fBhviHcSSR3va7lUNOZ2PN1vW_RUgVWBHSVWFErUtZgMQjRE_RPDkY6J3yFogaFmTMeHeJ6JB0Mf5A1se_fNbWY_n4RO2CrTOXAtHnR8Zz_u4SCWPAHQ2D63lBT6VvsmHiF_vPJYzWA4xTX2uAnywol7bjc4Tt9Kq_J-OSK9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d6e30712.mp4?token=lFn6e8IiuHEGnfMLUtDHo_Jk77VAkJwWzQ9IweX-IMy8YbyzO586r58eZHVIyqCW-wDtfuncD6-lB7A6LppOR_g_cBJTliKyOgRd1y-1AOXciykH4Q67akPASpnnHeSubzA7HqQA3N-lLmHged6DYHnueCB7Raz4jzi6W76dQ_BL3fBhviHcSSR3va7lUNOZ2PN1vW_RUgVWBHSVWFErUtZgMQjRE_RPDkY6J3yFogaFmTMeHeJ6JB0Mf5A1se_fNbWY_n4RO2CrTOXAtHnR8Zz_u4SCWPAHQ2D63lBT6VvsmHiF_vPJYzWA4xTX2uAnywol7bjc4Tt9Kq_J-OSK9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعال شدن آبفشان چابهار در فصل مونسون
🔹
آبفشان چابهار با وزش بادهای موسمی اقیانوس هند و بالا آمدن سطح آب دریا، حدود سه ماه فعال می‌شود و از نیمه شهریور دیگر این جاذبه طبیعی قابل مشاهده نیست.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/675055" target="_blank">📅 10:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675054">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74dddcfba.mp4?token=G8LK-Ny_aQXkuAaD1MDthGBAc3GfHLsyRsn-YFRdmp29dHww3kwDICukZwZFZqA6xZeIZTXnZeADMq8kpGRADhl3Ws8x0kmxGWMjduGwyBHhZVyTOPZCuk2SJkPrVdF6sKw3CWO_sWTPG9kBU3O8LsiPC3z76lCLekt7qvJa3qX3AhnbR0TLfzrov4dgxInZlnGBzntw5S4EQ9ZShkDHhxqpX1wc5T2_0pFsuWrknRfZud2GyiEJ34cYSLafE3GF5fCR8mPpQUfdLFFmy5nNGbPggDpXbyz5mLHe9hdocMCxXocEQ9ubG2xb_NXFKkHP4YB_6orGHKEZgXwEOcOqGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74dddcfba.mp4?token=G8LK-Ny_aQXkuAaD1MDthGBAc3GfHLsyRsn-YFRdmp29dHww3kwDICukZwZFZqA6xZeIZTXnZeADMq8kpGRADhl3Ws8x0kmxGWMjduGwyBHhZVyTOPZCuk2SJkPrVdF6sKw3CWO_sWTPG9kBU3O8LsiPC3z76lCLekt7qvJa3qX3AhnbR0TLfzrov4dgxInZlnGBzntw5S4EQ9ZShkDHhxqpX1wc5T2_0pFsuWrknRfZud2GyiEJ34cYSLafE3GF5fCR8mPpQUfdLFFmy5nNGbPggDpXbyz5mLHe9hdocMCxXocEQ9ubG2xb_NXFKkHP4YB_6orGHKEZgXwEOcOqGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سالاد سیب زمینی خودش یک شام مقوی و خوشمزست
😋
🥗
مواد لازم:
🔹
کلم قرمز
🔹
کاهو پیچ
🔹
خیارشور
🔹
نخود سبز
🔹
سیب زمینی
🔹
سس مایونز
🔹
ذرت و جعفری
🔹
نمک و فلفل سیاه
🔹
پودر سیر و آویشن #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/675054" target="_blank">📅 10:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675053">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiIjR0c-AabZ8ggrD1tKTbUeoKpPtBwuwchP_BImqEC_iBCyh2Aspe8wFQBBHRQui3uPHlZow-45NL-op4A4S2vroxXov_Qs6xf_PdvBBpaRsYtf_74muqK8rg-sntoxPT_wb0m3HbuOEyUk-Q-K4i8sQqcOsc6124xu2Tg47d6TFmM193eILRMf1p5Gzfeplj4zZv-jN1KeeEqRnBjmthhgDN3USD62mg5yif0AmgFcSKjTMqLYdjhkvx5hHyAYOaPmWJBEl7zXbeMaH9udhW4bnMw4pY62x_bvIiKBopgN7gUAI5DOjyJJweaxPzwKfLcLoBUpxYWaqYbGutwqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پنتاگون تعداد کشته‌شده‌های آمریکایی را کم کرد
ای‌بی‌سی نیوز:
🔹
پنتاگون تعداد کشته‌شدگان و مجروحان جنگی ایران را کاهش داد و این امر پرسش‌ها و خشم زیادی را برانگیخت. این پایگاه داده به عنوان سند عمومی و معتبر دولت از کشته‌شدگان جنگی عمل می‌کند.
🔹
مقامات وزارت دفاع این اختلافات را به یک اشتباه فنی نسبت می‌دهند. قانون‌گذاران می‌گویند دولت در حال مبهم کردن تعداد تلفات است و سعی دارد با تغییر نام جنگ، محدودیت ۶۰ روزه اقدام نظامی بدون مجوز کنگره را دور بزند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/675053" target="_blank">📅 10:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675050">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEgzrOf8QfC2QZ7NzoSIMSHzUHUFhppaA9mPdF4OIVAqwJjahb8NPPCDEJvIAQ3y_pf9NAEzh5Imv1_f-AHRVWt8uoLSaYah-Le5yFX_BvkVMHDqJlNLzrHVTqdfbisRbJd2YQwyvyoBWO0h4rvzpjiw_I8bB552tpx2ohMxqdUOfPuOV-lqtWysDKjzkac0wPEKpzISiDx7Asp8vHviFhmPIpfd6qzfDcPjRl6U5zqkD6JE9eAKqu1D-blEkUPbdg6t5l0IJczD6EwCLfiWDrVLRaRbVe_wShJjjAbwJuO9QmdWLv8_zs55KCSRMfO2Jsp25AZ1L-r8iilbY5_etw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/675050" target="_blank">📅 10:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675049">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBxSUh0LzkBpVkvnyF9VaFiHmOf3J5oqemoDyf_mDehILOIgKbak9rCEsB6zK-sOaMjveBF1Ot4VKqHv59QArfZ2rAk086nh6m9bYxAC9lKOUUX8vcJK1Fp9WoIdlDXiepFIomGviMoM9pVvPWxn0Y0T9GGH_2GASrSJeI3OMhozKNrx9jXWb8GxKp1V9m_lDrEz7trXiGd99_9b2AlJSOSqmSnKcv0P9sw5sYY3t3XD4Qtgh-KLGPqt1y2CpTItN6o9pYHnrL7l6YumdjGYzjKQQk8s23gCauLbKaK_i5o7NT1HMe5krjfLmv19r_ec5NPc1hRmE75b-K4s4Dh91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلمان از جنگ با ایران عقب کشید؛ کشتی‌ها برگشتند
رسانه نظامی Defense News:
🔹
با توجه به اینکه پایانی برای جنگ ایران متصور نیست، آلمان دو فروند از کشتی‌های نیروی دریایی خود را که برای مأموریت هرمز در نظر گرفته شده بودند، از این مأموریت خارج کرد.
🔹
مین‌یاب «فولدا» و کشتی پشتیبانی «موزل» راهی شرق مدیترانه شده‌اند و تا مشخص شدن اینکه آیا اساساً مأموریتی در کار خواهد بود یا نه، در همان منطقه باقی می‌مانند.
🔹
وزارت دفاع آلمان صراحتاً گفت: «با شروع دوباره درگیری‌ها بین ایران و آمریکا، دیگر شرایط برای مأموریت فراهم نیست.» /خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/675049" target="_blank">📅 10:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675048">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3R5LsQR8yPy2eqjtpFpENLOW43HDGqfhOER4jfk_NDEbo8-xAen-R_dbwfENQzXMlUE6jvElkydIPyAxrF-1idTSnFafENYuCbwQOBJfOlzIcZg-yPAgWL6-MhV5wFcBCKa86QQKqUmemm70yV76jcHt-2TDowypoY_LSw8UPUzL4RmENZt0LSgse5R1Team83vKSzdllbnZ6emla2rnDaQKVVFHUyowkwsiMDtiRGYPrRqqGDfgZRI-Y3QscGg6_YtuiuXl2Gi4POIL90KnoCycCVlFNKz58EyKtKLSWA4kz5O8MpkjAiZlQ4i6ny8EkkZMu_uJicu_4NjDZX3fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👠
UPGRADE YOUR STYLE!
‼️
تا ۷۰٪ تخفیف بر روی کیف، صندل، کفش، اکسسوری و البسه زنانه و مردانه چرم
💳
پرداخت اقساطی با اسنپ پی در خرید آنلاین
💳
پرداخت اقساطی با اسنپ پی، دیجی پی و زرین پلاس در خرید حضوری(مشهد، اصفهان، شیراز، اردبیل، بابل، بابلسر، کلارآباد، زاهدان)
🆔
@monofashion_co
🌐
www.mono-fashion.com</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/675048" target="_blank">📅 10:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675046">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm4DDfNd3CuSu2SYtX9T4hYwLppDIrH3nvCzYEheksAKrc921cJJb8Sl_WGnSaxyjqWYeUNa7LO0jZXXsxsVUqDe0K3PZ9YhBrkvjyi9r5WjlT0yGPDHpDQ1kuuYMsC_U33qyEl3Zor1uG9cBHnkxPmRxtzJLRgdHueCM4itZbz25k45n6KAnBvDtecISNYyDP_tQlCmbfbGFChO-8hiwMBW9kqzAu8NSLZDx1fkQtarojHE9qdt_ttIuMEznT2jxwBefT37NIC1rFgHPauE7qRpgXRN_TBgQ3XbK1l5lTGqFcZtipkGxE00lydRGOyZB3KVBTaB5voGNT0GNadVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری اینفانتینو برای تولد مهدی مهدوی‌کیا
🔹
«صمیمانه‌ترین تبریک تولد را به یکی از بزرگان فوتبال آسیا و جهان، مهدی مهدوی‌کیا، تقدیم می‌کنم. دوران درخشان بازی تو در سطح باشگاهی و ملی، به‌ویژه نمایش فراموش‌نشدنی‌ات در جام جهانی ۱۹۹۸، هرگز از یادها نخواهد رفت.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/675046" target="_blank">📅 09:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675044">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
نیویورک‌تایمز: نیروهای وابسته به ایران می‌خواستند در ترکیه هواپیمای ترامپ را بزنند
ادعای نیویورک‌تایمز:
🔹
ترامپ با جت اهدایی قطر، بدون سیستم دفاعی پیشرفته، به آنکارا پرواز کرد و با ایر فورس وان قدیمی به خانه برگشت. سرویس مخفی امریکا پس از دریافت اطلاعاتی مبنی بر طرح شلیک موشک به هواپیمای رئیس‌جمهور، تصمیم به تعویض هواپیما گرفت.
🔹
به گفته منابع ناشناس پس از آنکه مقامات آمریکایی این تهدید را شناسایی کردند، سرویس مخفی به ترامپ توصیه کرد که قبل از ترک کشور هواپیما را عوض کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/675044" target="_blank">📅 09:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675043">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
راز آخرین‌جلسه شمخانی فاش شد
👇
khabarfoori.com/fa/tiny/news-3232741
🔹
امروز کدام شهرهای ایران هدف حمله قرار گرفت؟ + جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3232597
🔹
جنجال بازیگر فیلم‌های مستهجن پس از فینال جام جهانی
👇
khabarfoori.com/fa/tiny/news-3232778
🔹
رایزنی‌های فشرده برای آتش‌بس ۱۰ روزه | ایران چراغ سبز نشان داد؟
👇
khabarfoori.com/fa/tiny/news-3232805
🔹
اختلاف پزشکیان و جبلی بالا گرفت | ماجرای توبیخ رییس صداوسیما چه بود؟
👇
khabarfoori.com/fa/tiny/news-3232771
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/675043" target="_blank">📅 09:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675041">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c3f4524d.mp4?token=igPVUkQAF9F-jYY-XV8NsdSnhvYXjIWH1myyHB4qGbFLYrpUqE7PzbPHW1FKljfWkD7lUJusGN_njBw8tcuI1lqOiWSM6qXT_EWRkZlv4uQ6rFd2qlyex0k7MV5mQVn7Nowl17O8r5LxoII1H_BfQV4skkr8K-zcCb_eTat0qoYI4x082yBF0exKYlazfH_JR86LJDPJ_VnXZbBEtpNg7T60Zxzvy4Q3t7oB_g_LApWhEBvOE0b4SRz5sKnEayaql5jgNTMAMFCetTWLEN1BGNc9pqQF7mcsdM8Ia_wQVmVkdsgeKHMLw3wogBb7CmBPjB_TwXGiqb7MfmTrAX0Wvz2U_UeIqLzExUzn8vivIiVVfsiGJOAxqoVd3sn7wlI2lyk-eNPWowx1mu0XfcawCM1NTlYi0E-GCYE2xmWUftK1AjYW02OGKdLgtAUnOBW8gev9f9jC9oxIzDd5mKlSiXuJo6cwv0Ho0SUWMlA34nhfeKgzE1EpLu7whIyDW0NWIxwVQwpa02t_P7G2-jckVy64YqIwWhZnYjhyZQAtldLqGbuBIVUUP0REbBTfWszyDDSXfjtWMp0Yxq5UA4YNMnkbx1RYZD4E6HPnk8KmKJUzC8V6NIinaGV1KW-8_ikreru2VeOHTXghj0pTLHDxH1zm1IxFQn6ESWMjmfOqOco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c3f4524d.mp4?token=igPVUkQAF9F-jYY-XV8NsdSnhvYXjIWH1myyHB4qGbFLYrpUqE7PzbPHW1FKljfWkD7lUJusGN_njBw8tcuI1lqOiWSM6qXT_EWRkZlv4uQ6rFd2qlyex0k7MV5mQVn7Nowl17O8r5LxoII1H_BfQV4skkr8K-zcCb_eTat0qoYI4x082yBF0exKYlazfH_JR86LJDPJ_VnXZbBEtpNg7T60Zxzvy4Q3t7oB_g_LApWhEBvOE0b4SRz5sKnEayaql5jgNTMAMFCetTWLEN1BGNc9pqQF7mcsdM8Ia_wQVmVkdsgeKHMLw3wogBb7CmBPjB_TwXGiqb7MfmTrAX0Wvz2U_UeIqLzExUzn8vivIiVVfsiGJOAxqoVd3sn7wlI2lyk-eNPWowx1mu0XfcawCM1NTlYi0E-GCYE2xmWUftK1AjYW02OGKdLgtAUnOBW8gev9f9jC9oxIzDd5mKlSiXuJo6cwv0Ho0SUWMlA34nhfeKgzE1EpLu7whIyDW0NWIxwVQwpa02t_P7G2-jckVy64YqIwWhZnYjhyZQAtldLqGbuBIVUUP0REbBTfWszyDDSXfjtWMp0Yxq5UA4YNMnkbx1RYZD4E6HPnk8KmKJUzC8V6NIinaGV1KW-8_ikreru2VeOHTXghj0pTLHDxH1zm1IxFQn6ESWMjmfOqOco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت تصویر پرتاب استارشیپ از خاک مکزیک
🔹
پرتاب دوم استارشیپ، بزرگ‌ترین موشک شرکت اسپیس‌ایکس (۱۲۱ متری) متعلق به ایلان ماسک، از زاویه دید ناظران در خاک مکزیک به ثبت رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/675041" target="_blank">📅 09:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675040">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
سی‌ان‌ان: توقف ۱۳ شب حمله پیاپی سنتکام به ایران
شبکه سی‌ان‌ان:
🔹
پس از ۱۳ شب حملات متوالی آمریکا علیه ایران، فرماندهی مرکزی ایالات متحده (سنتکام) روز جمعه هیچ اطلاعیه‌ای مبنی بر انجام حمله جدید منتشر نکرده است.
🔹
هنوز مشخص نیست این موضوع به معنای توقف عملیات نظامی است یا خیر./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/675040" target="_blank">📅 09:30 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
