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
<img src="https://cdn4.telesco.pe/file/tecJTruiXiy5IwUOpV9OAVtCL2OtqO_FGAyrgw4wuTaP9DfGFit6YvYRFmGh1cTmUhOYUPiGJSMnFob09nbOHGdlY7dt9z44PtDwp-D_3cWRPvzxGeqaQXw6k6shHsFrj28mJU-4aqRevT112nOVufHftKZ5ppBeL5mNqiTMqwudQL_Lt3D-3bNt5n7vvhYpnRdJNTtvfohpmTTtCqmAf4TvQNIFHV7wAQBwCRr4miq96rHDOhtSrJrRzZCwFW_b5lT64rzFUh_d7Pmrhu5zlBWhpdl9YsKHc0VqRdkiNj0Al2wKcM_2LuHq6zPoCZ6FfWQlQlq44wMATpgIjp8AVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 107K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 18:42:55</div>
<hr>

<div class="tg-post" id="msg-71735">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apeV68qyoOPErigKe1NMJMej3K0Yh50RufINYjmJtPhcg0cXBSqZcowkCZE89x3Xc994LzbfxyZMRF54m2QP-X76H9jIa3Wnw2TZFF5N7wUvWM7JrCDxq96b2Wd6bOZW7DXifZ2V1bxzvLcOvYMgICPnWooMyd8iIYyWueIcsrDAauSYbNtiKhb2F-JyxVdTQruK4NxoWN5dZcQ7_sdI49Jm10J7lbka_ZxAfFgVttAkl3rSR-ru8J-qnuvmggJ5zB729mMcHFUXZGE6dbIm69RtCQoYO3S738W0xr8_IcPPhFg4gL7L41wn5wUZXswSvInj6JdEz1c62bfTTek81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bao42zozIJkvHyZ7ixLEXhZkDiNUx900lxwTti4d48fe7uL2TaUdwGfah029mmbGsufxHiyiqkPwQpiHIQhwBNlMwKg-IQfOWx_IXT3YXpCEM5EDh5q-DM6_m_dH8vu2t6-YWMgk4G6C2Y7cagfzg98Y8S80O23tkLTD0ZiZY-zUogYWtVvYyrzngOD87DRDNch2PARuANp0FEzHaS900sqq7w32yfV02fYha-8rQy1OzzhqmW3UEglebZPA9V7bZxEuboS2XwQs2SvEVgK_i43CuMG-jq_q_eWnOSgRlGzQSW41jjTfSuoPrdVuRDqMecwGpf8eteB0dkbSLBGvoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حوثی‌های یمن تصاویری منتشر کردند که مدعی‌اند سرنگونی و لاشه یک جنگنده اف-۱۵ عربستان سعودی در استان مأرب را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 430 · <a href="https://t.me/news_hut/71735" target="_blank">📅 18:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71734">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=AKZfWx21y1b_e_aiGXF9F2JxZCX701qpe94jSgNXqFH3jb4Bt-mLZ2i5WtM_BY2EcoUWbDf3FSuqY73NmixV2Q5pV48Rn8iC6YKDX0pnf4TKCuSkYwz-iSYoc-L3I39D-Lav3C0aaCTtg6PVNN3uiYYqGULR5jqY2zDTDcvJS-ZT2KAWxT8t3TzRkTDcHw6_KHlhqqftDUgDBRFYvDSoZd_sBB_7og3HGQo5yQJMskKDNcpo8D8ws7i-xgGe68-C9rS6TeBeDaXuO1CLcz6PM7Kli8SrTwIrczlVZfOoMilzR-iKAe4lMlJtvroDEN0vVcEh8I6dRPphe4lnZU5tHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f8c75931.mp4?token=AKZfWx21y1b_e_aiGXF9F2JxZCX701qpe94jSgNXqFH3jb4Bt-mLZ2i5WtM_BY2EcoUWbDf3FSuqY73NmixV2Q5pV48Rn8iC6YKDX0pnf4TKCuSkYwz-iSYoc-L3I39D-Lav3C0aaCTtg6PVNN3uiYYqGULR5jqY2zDTDcvJS-ZT2KAWxT8t3TzRkTDcHw6_KHlhqqftDUgDBRFYvDSoZd_sBB_7og3HGQo5yQJMskKDNcpo8D8ws7i-xgGe68-C9rS6TeBeDaXuO1CLcz6PM7Kli8SrTwIrczlVZfOoMilzR-iKAe4lMlJtvroDEN0vVcEh8I6dRPphe4lnZU5tHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تهران یه کافه مذهبی به اسم ام‌البنین افتتاح شده و مخصوص آدمای مذهبیه و ورود افراد غیرمذهبی به اونجا ممنوعه.
شنبه هر هفته هم سفره‌ ام‌البنین دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/news_hut/71734" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71733">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71733" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/news_hut/71733" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71732">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQNJ-__BaFbRmtpxOCXAxwsj6x2wM_2-gjM7DfHO-djrfGDAvltkzmHYTHZvChJ-bZBsD3m6dOrQesm8oQ5CVFbPfFZ_A6FFqyx8swNYYHHcIfVeI7gnJ53eH3ISQyu35gKwZTbjc1dbFUFbJmXAu6WzI0LBty2sGK2j6mhcfv4EstwU7vDt64Rzeq_VzAoiNHlvkv9h_5VkQ4urs8gunSO_T8VLP2uR1w8UZtel_9i2Q34aJUemsGS_iOC1JZG-N0V9BkDWeYOQVrmwc28zjJov85PvEIg-NQbJDDfCMj8gPX9PeGRJKjX2zIZdRAoSQIva3XlgoQy7lythOMNeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/news_hut/71732" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71731">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534f93c783.mp4?token=o_cS7KaDC9YXlOb4-vOTogvNUZKBfOm-cpIGJeQ1GeA1LelSxxy9V9xqxKlimNb7IEeiVJe4tP8ZCtx1JC6WMPLkwwmWV99si4RH1EIP551bDA-9nQIl_bbgkW5m6aN41gLjC5aDCVi2-nWYHfIl6IoKalqtkf7yz-vU3Kmi-U_Euava0jNF5RE9LOtxH4m5c2ST_Y7_aJaejTTSqMwayC6mjPhITAqt0SePaBm69Ppns78ujQCc-ZNmFmdwNDYbfHjNq5OhcwQk6llobctgY_FdzOJM6Eveai8zbWR8Pkfld6YyiHsq7H2G9s6UWjVuK7IlcHqQPescZuvbDjOgMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534f93c783.mp4?token=o_cS7KaDC9YXlOb4-vOTogvNUZKBfOm-cpIGJeQ1GeA1LelSxxy9V9xqxKlimNb7IEeiVJe4tP8ZCtx1JC6WMPLkwwmWV99si4RH1EIP551bDA-9nQIl_bbgkW5m6aN41gLjC5aDCVi2-nWYHfIl6IoKalqtkf7yz-vU3Kmi-U_Euava0jNF5RE9LOtxH4m5c2ST_Y7_aJaejTTSqMwayC6mjPhITAqt0SePaBm69Ppns78ujQCc-ZNmFmdwNDYbfHjNq5OhcwQk6llobctgY_FdzOJM6Eveai8zbWR8Pkfld6YyiHsq7H2G9s6UWjVuK7IlcHqQPescZuvbDjOgMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این کلیپ تاریخی که چند نفر میخواستن با برنو، سوخت رسان و جنگنده بزنن
@News_Hut</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/news_hut/71731" target="_blank">📅 17:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71730">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فاکس‌نیوز:
یک کشتی طرف قرارداد ایالات متحده در نزدیکی تنگه هرمز هدف حمله‌ای از سوی ایران قرار گرفت که در آن از چهار پهپاد و دست‌کم یک موشک استفاده شده بود.
این حمله منجر به جراحات جزئی، از جمله عوارض ناشی از استنشاق دود، شد.
تعدادی از کارکنان آمریکایی در این کشتی حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/news_hut/71730" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71729">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeJwKBecWeh-UZwLT6BEjC324XgvPJgR3qIp8uMjdRgHoDH2XQsEM5OAe7zBAyFrQSzCwS4C6HAVNGw_2fMgAUrLJrW2q28W6pTvlSoKfNIuPDTQPnio79lk1NBmE7MzbDA-_DoWGmyJNOgeia5oiWlN-mNAXARO4vt4CD0F2GsZHnrV0j5dr6tgrblDb2SN84rGPcSxGHypbViDOzUQuCD6pqvyb_Ui6JAuWDNPY3RBk50oi4ScvW4LKMKJgA-GB5ItOM7apdJk9YA8ynMxWkQV658OtR4hglDk9jLNaR4eJif-y08b5o0bo7bbJozSW79bQrciicsukMu17rVyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در تجمعات شبانه:
@News_Hut</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/news_hut/71729" target="_blank">📅 17:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71728">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2421361f81.mp4?token=gFv5jUUJWZIdH8dUnBpJul7WIEB8uIuc3gZtfTrMsUUq-M4TXb8mxbHUlW5yXQb57A6lwoglsJY7UNFX1cCo9L8uTy8Uhukx75azNJvWls2priRcv8Q6ex4pt28z9sLO9gLYTlHrUae9FiQ6nZoFMH9qHa-jhsiAUrJBYKEbQJ9IszAy55FG0TojQqcQZRj1bw-x8sAQCRcg4ZI8-qoadGrfSR49VG9cDQaE5yEntvjzIcpfIqhxbBpXE8MWcJEPy39A9bYhU584QPKd7q4j2wh5ae09IrqBiinH9aHz7CzPLZQ3T7xn9mNMX29gmeYc6NovxB07-KoDdRaqP6HhSo4-8F9aLqeYTCgy_7Z295A14pZW0cMrj75bBQgtEll7U91WW8wDDCyZBB6HkZilzDH-8gsLDqcABgpl_SfgPTYqu8Sddac4Ha-8zVsLDUDDvxFivYLpTFurlehLjceZ1Lv0nX38IjG1CWTOimTChaWpCxn75d_N3-HG8wZ_YekGCjUHpNqA7aE9bdlevRgh3QVU5XTtotQqUoEV0_Dv-5liJRvxuIg25x1wPUutxwklGU3LVnU3bVNNtRkOdKjgcID_66AkQsnx9f2Dqo8VOJy4UT8GXKFb0uxPzGnMA3r7Uiup0LUceGlzQ3mVySLXZH1ZANLLITxnjalNdhCn5SU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2421361f81.mp4?token=gFv5jUUJWZIdH8dUnBpJul7WIEB8uIuc3gZtfTrMsUUq-M4TXb8mxbHUlW5yXQb57A6lwoglsJY7UNFX1cCo9L8uTy8Uhukx75azNJvWls2priRcv8Q6ex4pt28z9sLO9gLYTlHrUae9FiQ6nZoFMH9qHa-jhsiAUrJBYKEbQJ9IszAy55FG0TojQqcQZRj1bw-x8sAQCRcg4ZI8-qoadGrfSR49VG9cDQaE5yEntvjzIcpfIqhxbBpXE8MWcJEPy39A9bYhU584QPKd7q4j2wh5ae09IrqBiinH9aHz7CzPLZQ3T7xn9mNMX29gmeYc6NovxB07-KoDdRaqP6HhSo4-8F9aLqeYTCgy_7Z295A14pZW0cMrj75bBQgtEll7U91WW8wDDCyZBB6HkZilzDH-8gsLDqcABgpl_SfgPTYqu8Sddac4Ha-8zVsLDUDDvxFivYLpTFurlehLjceZ1Lv0nX38IjG1CWTOimTChaWpCxn75d_N3-HG8wZ_YekGCjUHpNqA7aE9bdlevRgh3QVU5XTtotQqUoEV0_Dv-5liJRvxuIg25x1wPUutxwklGU3LVnU3bVNNtRkOdKjgcID_66AkQsnx9f2Dqo8VOJy4UT8GXKFb0uxPzGnMA3r7Uiup0LUceGlzQ3mVySLXZH1ZANLLITxnjalNdhCn5SU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیویس کیس سخنگوی سابق نخست‌وزیر اسرائیل:
دیکتاتورهای ایران ظرف چند هفته سقوط خواهند کرد؛
دو هفته، سه روز، شش ساعت و چهارده دقیقه دقیقاً
@News_Hut</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/news_hut/71728" target="_blank">📅 16:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71727">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=JGO-D1d0QwL0Ygm-mf8L70_3J3zTx-KI4MY8AHlQiCJ-eblWFca0Awad4oQRQN9ibHSa9SAcuD9lHrjQG5FiDfTXiOmJqyK_aigtl4mENPfp11-1cWY5AYSFx-BZkeSde7K_s-tjl4J0YqPN6f--OE3oNAf2KX1khC6uG3hGMSJtY6jdupxsxfTFMDjcUrMncT2NrWiKHTNcXcm48Jyhc3AEJmtbanRTi31le2Cy8WhnLfbSEkQw6B_mOEG1pvtN2XGamLYwSTrHrjLYbBNnycflEEs9ExP7PFnOBShatUzTxj4RqTZiJaAP8tYvnrF3Ud-k2Jiiri_3nSNZG3QX6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de91f58f7a.mp4?token=JGO-D1d0QwL0Ygm-mf8L70_3J3zTx-KI4MY8AHlQiCJ-eblWFca0Awad4oQRQN9ibHSa9SAcuD9lHrjQG5FiDfTXiOmJqyK_aigtl4mENPfp11-1cWY5AYSFx-BZkeSde7K_s-tjl4J0YqPN6f--OE3oNAf2KX1khC6uG3hGMSJtY6jdupxsxfTFMDjcUrMncT2NrWiKHTNcXcm48Jyhc3AEJmtbanRTi31le2Cy8WhnLfbSEkQw6B_mOEG1pvtN2XGamLYwSTrHrjLYbBNnycflEEs9ExP7PFnOBShatUzTxj4RqTZiJaAP8tYvnrF3Ud-k2Jiiri_3nSNZG3QX6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ دعوای این دو تا بچه گربه خیلی وایرال شده، از بس کوچولو ان، دستاشون به همدیگه نمیرسه و رو هوا همدیگرو کتک میزنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/71727" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71726">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=hdecSHLXWph5asYGUquJMQv-QJe_0fDYlGtEEsBoRWX8RjJuhMJxKfFMjAapkWmVbt7BNvSUHe8VkSxLGP3ksaAQipN103kvpeMGDADGIhKyObFLSKTpDy3XXYqfHfEa3TB6BiH-TAQA8Pks0PMKPjjyZgKVmwX7LrQmcEQCzNqInv0RMmYL_-dvzWB7SwOyzxiK-9GJCMOdpRbsp_Wd3MgJogpT74NMZFDfUnTPjrpuZYemyG3scwyvDnVDRZKRScVN42abuK9maBaSbKMyF1VyeUHf9qdjMn9F4tPmWyZIqoBIuAWx-GZ9qIfdp4yjK7k8P7Qqo4T40MJRZtlGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f04518ba.mp4?token=hdecSHLXWph5asYGUquJMQv-QJe_0fDYlGtEEsBoRWX8RjJuhMJxKfFMjAapkWmVbt7BNvSUHe8VkSxLGP3ksaAQipN103kvpeMGDADGIhKyObFLSKTpDy3XXYqfHfEa3TB6BiH-TAQA8Pks0PMKPjjyZgKVmwX7LrQmcEQCzNqInv0RMmYL_-dvzWB7SwOyzxiK-9GJCMOdpRbsp_Wd3MgJogpT74NMZFDfUnTPjrpuZYemyG3scwyvDnVDRZKRScVN42abuK9maBaSbKMyF1VyeUHf9qdjMn9F4tPmWyZIqoBIuAWx-GZ9qIfdp4yjK7k8P7Qqo4T40MJRZtlGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه رستوران تو آمریکا باز شده که تم بیمارستانی داره و تمام‌ کارکنانش کاستوم دکتری و پرستاری پوشیدن و اگه غذاتونو کامل نخورید باید براشون قمبل کنید تا خانوم دکتر بیاد شلاقتون بزنه...
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/71726" target="_blank">📅 15:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71725">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=BrSwmY1tzPnuiEbR4HPZJyXs2VkPR4WgsIjVkZmCXt2d7M-KBt_Sjt2LzE9UGbnkFxwAobWnQPCURgKz71vBdjeSb7TUo1NbmxJLsLFuzTnIyQACdzub9ak3qB4GnTTYvJYMRsIZnSIO3C4YoLTwwhGDNPfz00ubTaQfHV61YD9IgRxa7hHOjgSKn2uQ4Oww6sgu08VN3ZfYTfCVU6ZoyZeGkYMx6CrYH_grvHSHKTaNsKtmHlQwuQI5ilqgJkOsaOcmP8B2oNmOHeUhaFcUMaNRcDw5FcsEGHtXfj1Y0SbRdyJxC8sr-fZY8Hs6ail-dybcUFfM-JMre0BjKbjo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=BrSwmY1tzPnuiEbR4HPZJyXs2VkPR4WgsIjVkZmCXt2d7M-KBt_Sjt2LzE9UGbnkFxwAobWnQPCURgKz71vBdjeSb7TUo1NbmxJLsLFuzTnIyQACdzub9ak3qB4GnTTYvJYMRsIZnSIO3C4YoLTwwhGDNPfz00ubTaQfHV61YD9IgRxa7hHOjgSKn2uQ4Oww6sgu08VN3ZfYTfCVU6ZoyZeGkYMx6CrYH_grvHSHKTaNsKtmHlQwuQI5ilqgJkOsaOcmP8B2oNmOHeUhaFcUMaNRcDw5FcsEGHtXfj1Y0SbRdyJxC8sr-fZY8Hs6ail-dybcUFfM-JMre0BjKbjo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله افراد لباس شخصی و آتش به اختیار به یک رستوران در رشت به نام « سحرخیزان » و تخریب رستوران به بهانه حجاب⁩⁩
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/71725" target="_blank">📅 15:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71724">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBircfuAO4fQzHEkv24keVbIIcFATHGqTWbWSmqiLimpf-nUCUNF1FdALPIMHo7DzlwkBW-SI_RzTFkVT0pZ0wCaQ-jgJDToLG0ZuUn3kw8zLvbMgTdThKbXtZpL7YGu6dgsmKPLTg09N2aLCHuN1oqGgDq4iFx94IJI3k97oCByNF9cf30_vt2d5myiAKSmknUxgnLZ1c-mHZZFdetTsD_2SW1bxtCUv3QCo4cJDD0N7q7Bb3OL6QWKg1UieZhKysyYZApxUiRlmiq24XJkce0w2aaRNVwjPnV7jqwmX3g57ODiLOwnBwOZkocaIZ-CRGkVhjn4xYifna887_UD1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛  سامانه‌پاتریوت شیطان‌بزرگ مانع شد خانه‌خدا توسط حوثی‌ها نابود شود!  @News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/71724" target="_blank">📅 14:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71723">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=oPY3whaWuoxiLL4qg8vdKDKG13Xz8p-FTXQdJ9Y5uTCCsTTmy-axF9Lcg00Xr1nPWFxJww1nNmqOylKYCFSdS14sxcL7bhZXfP92gjYE8EnJZ7KeLt1li3OCkIGT4hty7d8U-koRnC_ByoMwxvt3xBCflI01yOuuBxBFy8L4d8FjlvYRAsk27ALfvb0z2ALa80tNfn3VIZZlktjmn8PCGhosMoTc8aPyAK8qPKbv626pIlfioCovZE7oMqYtT8OYDKSMivljM8QOdPk1iU160MQJE5Uf4Tk2U9V30FnESEov01zy4r6f1WaGN8kTigXa6UsBFYaFPov9JrETMSkHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b212130ba.mp4?token=oPY3whaWuoxiLL4qg8vdKDKG13Xz8p-FTXQdJ9Y5uTCCsTTmy-axF9Lcg00Xr1nPWFxJww1nNmqOylKYCFSdS14sxcL7bhZXfP92gjYE8EnJZ7KeLt1li3OCkIGT4hty7d8U-koRnC_ByoMwxvt3xBCflI01yOuuBxBFy8L4d8FjlvYRAsk27ALfvb0z2ALa80tNfn3VIZZlktjmn8PCGhosMoTc8aPyAK8qPKbv626pIlfioCovZE7oMqYtT8OYDKSMivljM8QOdPk1iU160MQJE5Uf4Tk2U9V30FnESEov01zy4r6f1WaGN8kTigXa6UsBFYaFPov9JrETMSkHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حوثی های یمن به مکه مکرمه حمله کردند؛
سامانه‌پاتریوت شیطان‌بزرگ مانع شد
خانه‌خدا توسط حوثی‌ها نابود شود!
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71723" target="_blank">📅 14:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71719">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7dNxcSUyAkuiFcY9FYd2jAisy2gWE0Q7zbHqy08JDZ9jNr0NrX5oqNr8hivlhLDAEnK5PZ4DLUx_wc1794ttfcE_ElbhpholqwmDs-RlISj8DljEfA8AUWeYBf1MOl80q_93GeqvchdugMsCk_Abc0zCfHtIP8VHmqeeCxF1H_WO6d6a4P1S5oCvqWfmFj7_6G6rf35vZcgv_Sllv60PGEwA-u6knU_rCOdtOqPfNN-xPeMS0H-njZy0R7eXOlRg19pP8MrQyedYhvUdBcCYZQhpEeW0qSgC-MGfyBF_L-xcuCR6iMC4MRuGnOPtDupjHEdLQ7x1GrzflJwVwmBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pW12F1okZyW41x2Th-2ai8PNirE9wBFFzGg-OAtL-sPXxIrneESWx3FFXZ0RDtGXajS13sCCSKmx66pDp2MTcBG5s7y0PBEYC2J3tw9hU0eK0s5lz96-BI9X3iBI3nKwvFDkypNRZNy9ot6nU2Geqg7eIOTxMUeyTH2X6C2DhBzU2xDugEcMx9fKo6mw5Q9rRsqJFerGDXdVs4KvSow2I0-7TH6WOvtz48hUIh9UvHjb8Fu4gDozknrXqOee8p14PhXoKtPdsDs4FpXYu_EHLrcmNpsRClJQabwXo-aZkfsEX3EHptrZLhMDrTGluK9izfRZWfhHTu7I3Ps6HTYE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSqxL8dyUaTmptnwg16rHmEiMOLdUc2vVPewk1MDC3TqFVm_MOuxqTCBNfm2wTUqkkCrChL6Ae1wWXztAb2aGXrKBpy43oCTB5vqG-OkZakmGZ7C-183lOWlRiONpnjMecVGMsKILQLaDxE7irT7rwuq5-0MOqnKg4LEaA00obz3v7nCbgk_V8aVMyxmYnUFtztv1pDQryYyW6mhHQW140mHE5K0JtS0PAp_JFZCRa7G3tlJjFmMtFWq9TSwQgPDWYzg9uAW0bpITSb6kvpMkYvL-uVfOjptRmBwSbMhM3vYvvnSq1R5D6vLda5iT4f8Wo-nOf1Jt32wvg7qMJtwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0c61SOWqDCkBmcaRRtko9loo1qi-BSuTDp10wsgn0cUGceoZAeVLtpoyJFTS8PYw507aXUmArOOHSqCVhHwMg2IdE8HS7KinFmQt1Rt2v4lzMy94ZwIayjvtAGR31p3j1FbfPxv40iPL8OFUgFeQa9fsHvHjAbCzKb69Snpq9sV9shYJUMMyQx5itmZUsU3zrA3t7vajPZ0rnbyBpmLgUrh7nwTRQGTJcXiSIDncD81jiL1Lx4FdcOSLaLmh5dL0hDpfbXliHgJ8EXLiyeV1qjv48ZB9zVr_T1jmVZa128Lprp7SrvKZriUFbuTOY3NzSWQyFuymIjbwYn2pwKe2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌های اختصاصی که توسط سی‌بی‌اس نیوز به دست آمده، خسارات گسترده‌ای را در چندین موضع نظامی ایالات متحده در خاورمیانه پس از حملات موشکی و پهپادی ایران نشان می‌دهد.
این تصاویر که توسط اعضای فعال ارتش که ناشناس هستند، ارائه شده است، ساختمان‌ها، وسایل نقلیه و تجهیزات تخریب‌شده را در پایگاه‌هایی در عربستان سعودی و کویت نشان می‌دهد.
در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای بوئینگ E-3 Sentry مورد اصابت قرار گرفت و قسمت دم آن جدا شد.
در کمپ بورینگ و کمپ عریفجان در کویت، عکس‌ها نشان دهنده پادگان‌ها، تریلرها و وسایل نقلیه آسیب‌دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/71719" target="_blank">📅 14:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71718">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEh69QbmQAAmj8xjUZ2MJMfJ3sO3POPO5BE0lVrOfzWc1p-ZwnoiMXV_-Ib4KL-YwGkSVxZCajgcBpfJjSyImLLxflynnwbtp6THm2XHcH8oNZ8-iliSXgA7leb9CxOm71_6JsB4E0ZRT7JrZze_SJrPWxGYhlBzP4g6JSWby9SxpQX_lM3HsAykJcCnrFJSxSDs2J9au7MdY1YuRSOTBJw-myMs1W05bQ4uidWsEY-vSDaHRq2XjsMh39W7dKUKcjF28UwNmYCrDQUw4EdauzKb9qpU5oqzzUnm_tvJnkeam6L7yBSBOb2ZydzS1EP150Sf7nD_ztMce8PJHjtobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشته است
این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری می‌کرده، که در فایل فروش هم این اطلاعات موجود است
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71718" target="_blank">📅 13:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71714">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a175287c.mp4?token=SUGZVbGQ6JPPfd7F0CrQDeTuI5G9AYzN5mpbS-nHBud4jmgkOeiX_7eJEMQN64zwYMbP2UiZv2XsCcDlWMCx1B2bvrJ6NohNq9aALEGwbv49sXVjJnLb1RVfmuBMclZMJXGB-1mL6_0YVMtJYYZHj7Ufstq8_uiaCd_0mK-UqzZfG3jToPG726Ujwf4Pzh-oUvNUdSfJ9jNN6RtUxPAt3V1dMfMOQOzQfMo5pzMzEd_oha3Rz4PUnSEF4TwtvLMLHtUhT86z8DzMHPMeCaxcfEVekbKtTeF-r-4yajiKPANE_Cdm7BpjbYD6CG4AMDGZgw8Llf54tSOaCkE2NV1sAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a175287c.mp4?token=SUGZVbGQ6JPPfd7F0CrQDeTuI5G9AYzN5mpbS-nHBud4jmgkOeiX_7eJEMQN64zwYMbP2UiZv2XsCcDlWMCx1B2bvrJ6NohNq9aALEGwbv49sXVjJnLb1RVfmuBMclZMJXGB-1mL6_0YVMtJYYZHj7Ufstq8_uiaCd_0mK-UqzZfG3jToPG726Ujwf4Pzh-oUvNUdSfJ9jNN6RtUxPAt3V1dMfMOQOzQfMo5pzMzEd_oha3Rz4PUnSEF4TwtvLMLHtUhT86z8DzMHPMeCaxcfEVekbKtTeF-r-4yajiKPANE_Cdm7BpjbYD6CG4AMDGZgw8Llf54tSOaCkE2NV1sAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
:ویدیو هایی از اعتصاب عمومی در سنندج،سقز،دیواندره و دیگر شهرهای استان کردستان به مناسبت چهارمین سالگرد قتل مهسا(ژینا)امینی به دست حکومت آغاز شده است.
همچنین ویدیو هایی از شهرستان پیرانشهر در استان آذربایجان غربی رسیده که نشان می‌دهد بازاریان دست به اعتصاب زده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71714" target="_blank">📅 12:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71713">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه پسر ۱۴ ساله با یه دختر ۱۳ ساله وارد رابطه شده و ا‌ومده پیش دکتر میگه من پرده اینو زدم و گشاد شده؛
حالا اومد پیش دکتر ازمایش بده ببینه این دختره قبلا رابطه جنسی داشته یا نه.
سن رابطه جنسی تو ایران داره به ۱۲ سال میرسه!
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71713" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71712">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71712" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71711">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF7dBHFCxJAjsa1Fuyb_AwSNAGvtgka92vvYt2iJ7D72kpgMv-xsjq6q_OCMd6G1TH5CXnwnede3-yKEIS0lHSqgm3iBk5ysmRxsFtelDZXDvHYsKPW2RhxtXdvzzOFUeL2mybwy4ry1rEQcPKi32gFmRWSIhjx7_weu5XV703Tu9ZxpN2e-6Vvs9rT9luhCYZB33HM6IE1Q6fPPbXU0N3govsR7Spwh3vhDYWfTG9ayWmhpC_R0n3hx-LPcUbNU2W05jZ9E0pY_4tVEqwtEcD4EH3Pf-cYejWfpY6oNNSh8snFbVbjDXgGfsIQIvoTs_BRYoHe-Uyr0jxMvkS-h6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71711" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71710">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEc_qQDBfY1wYSpfA0lHZSpOtsSyD-uX5IBstxtjbLipgXHArxbdrfXaO_Qb4DpV9Y6208ljnP8qkT2V5_q-0Z7o2atmnnJ21ltkkuR4gNjheYgGI_r9xJrfXqLyWaQXC5EBT3NZ1CN_Sar5adwPZi3RRU4YW4FQVLQdk4NzatZgpI73GWyxAbe-Gh1RZPbfo2gSynMSmWED9zB-TAB2LJPmPJ-2P3hm6-284ds0GjqcAQHEAKQRiy4cOSnHaxeFhP9_wdvhe0yAsjiL4B3KQ6qVzgWTEIPkbFVlz7nLqj_q4CZPhZ6dpyk0c9rpjdBT7n3HarCsFTOkgGTgq7ZkOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده برای اولین بار تأیید کرد که سلاح‌هایی در مدار دارد.
مینک، وزیر نیروی هوایی:
ایالات متحده اکنون سلاح‌های کنترل فضایی در مدار دارد که قادر به دفاع از نیروی مشترک در برابر اقدامات خصمانه دشمن هستند.
از بیان نوع، تعداد یا زمان پرتاب آنها خودداری کرد.
نیروی فضایی می‌گوید که می‌توان از آنها برای "اختلال، تخریب و حتی تخریب" به صورت تهاجمی یا دفاعی استفاده کرد.
کارشناسان فکر می‌کنند که به احتمال زیاد، پارازیت‌اندازهای فضایی یا جنگ الکترونیکی - سلاح‌های جنبشی - مشکلات مربوط به زباله‌های فضایی را ایجاد می‌کنند.
این به دهه‌ها ابهام رسمی پایان می‌دهد.
اولین نقاشی نیروی فضایی به معنای واقعی کلمه یک هواپیمای فضایی را در حال نابودی یک ماهواره متخاصم نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71710" target="_blank">📅 11:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71709">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26353c8137.mp4?token=FyJQaCIsn4Dg7zcG7s_S0d5FuR6-dVA72hRu6zZsLCnbk-tqvK9dsXhkCTYoEiVUtEHvgHjsQy6cE5BpiYoJZwTLv4J04y2R9rL8GkxNeDJah-zxPokHBPMPdqKVYlYjGCdDFzc1Fos2GpFwoB20bk_p14sA3Py6yYzLS4QtQJKAe99Fh1Y-3PoBjo7fb-RB624PxUZhFvZMOShn_BFUUvfB5kloNwSHrBXn1T1L76swI5eEOr7yovfYXuoKMsJAjXkExpkDArb8MyYuKH4v0MiOMX2OAyOPSPlI8B-tCK_Z0Pvg_mGhJ6-z4kzPwsfAlvFPZgrSKD-gKMTEG1lozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26353c8137.mp4?token=FyJQaCIsn4Dg7zcG7s_S0d5FuR6-dVA72hRu6zZsLCnbk-tqvK9dsXhkCTYoEiVUtEHvgHjsQy6cE5BpiYoJZwTLv4J04y2R9rL8GkxNeDJah-zxPokHBPMPdqKVYlYjGCdDFzc1Fos2GpFwoB20bk_p14sA3Py6yYzLS4QtQJKAe99Fh1Y-3PoBjo7fb-RB624PxUZhFvZMOShn_BFUUvfB5kloNwSHrBXn1T1L76swI5eEOr7yovfYXuoKMsJAjXkExpkDArb8MyYuKH4v0MiOMX2OAyOPSPlI8B-tCK_Z0Pvg_mGhJ6-z4kzPwsfAlvFPZgrSKD-gKMTEG1lozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک دانش‌آموز دختر برزیلی بعد از اینکه نمره‌ی خوبی تو امتحانش نگرفت با چاقو به معلمش حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71709" target="_blank">📅 10:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71708">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=W6VZRQ2huGJY5ovGjcj7dWkiH4X0gdmJNQjHzv58BiOsCZjMmBjI5IhAl8dpRWGP3DKtUmo2RPbCd9-MX8y0SY4FseFw6bEGful_zom5MiSwtuQtlV7dKwlm6tnt5LgP0msMhqEs_fgG_wjwBR5ysFB5iCPOGw7UaVmfe6BVuZFTj3nPp_waU3Je1gv_s6OguEyVafhkcqmuabALB1CeZmKZvtXD4_S_nbHOlvxCQhhWykEEAZjJRVH7YCF6noecnINfz3VF8eKx9Q1HKcJdVVQvtqTX8qbd30tSkzHLuzPgKD8ntvv_Z1OKWZeHDFvxhl09rV-mYtqhdVOtiJIuSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=W6VZRQ2huGJY5ovGjcj7dWkiH4X0gdmJNQjHzv58BiOsCZjMmBjI5IhAl8dpRWGP3DKtUmo2RPbCd9-MX8y0SY4FseFw6bEGful_zom5MiSwtuQtlV7dKwlm6tnt5LgP0msMhqEs_fgG_wjwBR5ysFB5iCPOGw7UaVmfe6BVuZFTj3nPp_waU3Je1gv_s6OguEyVafhkcqmuabALB1CeZmKZvtXD4_S_nbHOlvxCQhhWykEEAZjJRVH7YCF6noecnINfz3VF8eKx9Q1HKcJdVVQvtqTX8qbd30tSkzHLuzPgKD8ntvv_Z1OKWZeHDFvxhl09rV-mYtqhdVOtiJIuSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گفته خانم دکتر(روانشناس بالینی)؛
خودارضایی نه تنها ضرری نداره بلکه خودارضایی یه چیز سالم و بی‌ضرره که به عملکرد ذهن و مغز کمک میکنه، باعث کاهش استرس میشه و حتی به رابطه شما کمک میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71708" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71704">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-Dt_l5x6Xm8CyBL6sB1fk6cKhuaQjXD6OXuxBZ0ZFtgAECWQU6NwFm5RyVU05BNR_y_4lv1qAgOFj4vvaMZHt5hh-c90EQLxQ9q_wcwq7yn4if94S-dF6w0cvGUv90OiZJO3gdCZS5ZNfBofGeD5bzv25bnO3f8JQkrn7ZvjFjQrM3tTgd9jj9nUpOwsmdzjWp4_wxDtVkR4lAx71zx9AGWhxWmUcCiP1ERLoBBOoYN5TNTC9-aQZyBf_yaK_9FKy4cLwB33xlm3HNBrKrcLynnqKFe3b8YTEuBp7CvaQnzFr2zCI5cKDjkSbzAGC8eN6mqa6_Fy9lF9L3MUpAZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=vUa5J3I_tZe3R2sBn4ReJXiRqSXlI2opmrySEWPBOpT6MOrmoEzSOn21EK6hWbTeyTczlIgD78__Bmyes8v800aMATQPV43VXAwF8eoFtD23cUXwlxGQ9z3pG3GSSOd-hL67gVOKrUfuQxQgFZhSFedNaAXSGYti0Hrr5V7hn5O9NziXFSGxrxtHT8JOpWzac5cYgouiNz8-CL_HrM3y8NosLyZzhE1ERD_Atve2rRhO_MoPa1YsJSNafvNPIhXh64HeQH46HpE9Id9qygmM-ucS-4ouqtDbHONcCvPLZwIMlyECgti7rsj1gox2n1xQl4FtFjt6xvhnycZUaBxpEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=vUa5J3I_tZe3R2sBn4ReJXiRqSXlI2opmrySEWPBOpT6MOrmoEzSOn21EK6hWbTeyTczlIgD78__Bmyes8v800aMATQPV43VXAwF8eoFtD23cUXwlxGQ9z3pG3GSSOd-hL67gVOKrUfuQxQgFZhSFedNaAXSGYti0Hrr5V7hn5O9NziXFSGxrxtHT8JOpWzac5cYgouiNz8-CL_HrM3y8NosLyZzhE1ERD_Atve2rRhO_MoPa1YsJSNafvNPIhXh64HeQH46HpE9Id9qygmM-ucS-4ouqtDbHONcCvPLZwIMlyECgti7rsj1gox2n1xQl4FtFjt6xvhnycZUaBxpEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر تیک تاکر به اسم فاطمه تاجیک دیشب توسط چندتا دختر که میگفتن عکساشونو گذاشته چنلش خفت شده و خودشو دوست پسرشو کتک زدن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71704" target="_blank">📅 09:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71703">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEzuwC4eSf_d30pndB0QMKwvtoDSqZiFFHOJQjIfiZjRbp_yztnnhLGcnvZk0874V83X2bCiziRsQG-NQQDB8s0xy6VtmOoFtv5qaB9Rg9TrBOCNhVVA3rj4sK9KiwpX6MCIykkVBWLYObpKC9tKIjRh3nPNm6iqqNZwFelFAFLpLT1J8-xpEpcWVolCZogBIVLzgmN96boD4Wyn-JrypO1Hy1XYrc6BXF84Ma0J3klp74j3ieYC1nE3TDzA5u7qLO22fBc-p97n6JW9wPBcEKac5WvyvRF7PIcwNTPDVNsQ9zBQZRH9DY5o-ofE50h0RD2wLJf4lre9mWAOFPKR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس:
فرماندهان ارشد نظامی ایالات متحده، اسرائیل و هشت کشور عربی هفته گذشته در آلمان دیداری محرمانه برای گفتگو درباره جنگ با ایران و امنیت منطقه برگزار کردند.
این نشست که به میزبانی «سنتکام» (فرماندهی مرکزی ایالات متحده) برگزار شد، با حضور فرماندهان نظامی اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر همراه بود.
دریاسالار برد کوپر ضمن تأکید بر تداوم حضور نیروهای آمریکایی در منطقه با وجود حملات ایران، شرکت‌کنندگان را در جریان برنامه‌هایی برای گسترش تردد کشتی‌ها در تنگه هرمز قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71703" target="_blank">📅 09:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71702">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71702" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71701">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ht013ER3f2KVA58T0W089JROWPh8tIEhbfyJ-kRNtGruEWMGVAwQPX6SR999SztWSn9AhpZfCdBLkacGcIv6ofwZ6tJf2WAFPyIaakxTecvpJ-c0rBo-ZJrz9HNMYtzCryrN40GBzVwT--JXU77asSjtEBprrcHjbMijszIdR74q3HyPHPriNF6FANePT25u2K6h3_ZkWjaRmsaHGV2zuNYzTN0qAz3O7nvobI_6N808CzQ3cOUCM_6a2Y6sLee8DPo1m5StpM5CkvEXPUEbF23goPBxpwD7rZAs5zRrH-q-qgjcP6rjLCPUGR-QUb_KrIwHBwne09KvC52VbfHzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71701" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71700">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71700" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71699">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71699" target="_blank">📅 01:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71698">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwzw3jiD_k7uBbSMzSCVrBFnUvmLUJtyZKheyEQFuuNTnHWvvk0roZEMmVcntTXHXgIqCNNpImBaMFuLoI96aRj4z4lwgoNk-TqTnfiPX_3rWPsvYIWzv4aRb-YHeCk9wNZNT51mjo18yWqYLFbk8FM4ia2mKxM1clW5vUFfSVz1TSYHTG9r3h8c2IXTT6V3II0orG0hg_a4Hnb3eohsQeDmcD5xNCXcmBIELybJfJucXyCj378iOgJlqjEfd4EC6tPIlxYNw_XudR2mmxJvuF3fXOo1jTXp9oKBYs011ldnWGkOPEBYrZnwD7bssREUL8qtktHalxd0wCkf2RB_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آلمان (DPA) مدعی است که حوثی‌های یمن اکنون در تنگه باب‌المندب مین‌های دریایی کار گذاشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71698" target="_blank">📅 01:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71697">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=FVd1WAAyb2LyFI0SxKqM9bXiEQMSgbVeMshnVaXmKyHXYr_0MVbA8A3u7Y9PfVGtR8cvNeNwyqpXhpOMDXt5JIdgxcZU8fhLSwc1Btrp3pC7L-TAwHeBhexsjGPUexPoxu9jjESS6pFpi8w_VP_0YTXFLc7eq-TtIui6a-GVJ7jkmwwFxUYq2w8PgIahbBAguCbJhT7cFIp7tS6PwLVlCTMAvKD5nqaIg-FwzI4FUuq5MV_bp__iLKWM68SZy7ZRNYB2icoa-aMbn7a2fXR3ktvJCLutr7HurATWT4UBCiKEQvpuPuyRD-r4h2QPt05eHprod8M-Tj9HPIIXkjKu2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=FVd1WAAyb2LyFI0SxKqM9bXiEQMSgbVeMshnVaXmKyHXYr_0MVbA8A3u7Y9PfVGtR8cvNeNwyqpXhpOMDXt5JIdgxcZU8fhLSwc1Btrp3pC7L-TAwHeBhexsjGPUexPoxu9jjESS6pFpi8w_VP_0YTXFLc7eq-TtIui6a-GVJ7jkmwwFxUYq2w8PgIahbBAguCbJhT7cFIp7tS6PwLVlCTMAvKD5nqaIg-FwzI4FUuq5MV_bp__iLKWM68SZy7ZRNYB2icoa-aMbn7a2fXR3ktvJCLutr7HurATWT4UBCiKEQvpuPuyRD-r4h2QPt05eHprod8M-Tj9HPIIXkjKu2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا به‌تازگی طرح استیضاح دونالد ترامپ را که توسط «اَل گرین» (نماینده دموکرات از تگزاس) ارائه شده بود، با رأی قاطع و سنگین ۲۳۲ به ۱۴۷ رد کرد.
بخش بزرگی از دموکرات‌های مجلس به این طرحِ پوچ و بی‌معنی رأی منفی دادند، چرا که اَل گرین خودسرانه عمل کرده بود و آن‌ها می‌دانستند که این قطعنامه به جایی نخواهد رسید
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71697" target="_blank">📅 01:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71696">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ونس امشب گفت که تو ماه‌های آینده، جنگ وارد مراحل جدیدی می‌شه؛
اما در شرایط فعلی همه‌ی تحلیلگرهای نظامی معتقدند که بخاطر انتخابات میان‌دوره‌ای، جنگی گسترده از آمریکا نمی‌بینم.
اما یه نکته‌ای اینجا وجود داره، انتخابات سنا و مجلس نمایندگان آمریکا  نوامبر ۲۰۲۶ (۱۲ آبان) برگزار می‌شه ولی نمایندگان انتخابی، با ۶۱ روز فاصله به سر کار میان، یعنی از ۱۲ آبان ۱۴۰۵ تا ۱۳ دی ۱۴۰۵، سنا و مجلس نمایندگان با همون اعضای قبلی ادامه می‌دن و می‌تونن قانون تصویب کنند؛ بنابراین از لحاظ تئوری، بهترین زمان برای حملات دوباره‌ی آمریکا همین دو ماهه (در صورتی که دموکرات ها پیروز بشن)
ولی یادمون نره که ترامپ یکی از غیرقابل پیش‌بینی ترین سیاستمدار های دنیاست
#hjAly‌</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71696" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71695">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM9onFjRvK1ID4z9x1dG6EoXtRvqKlDSai6jKDYEOLvI141lZrmSesUWXR4lTjyQ5Gg7Z5Xu6VFiiQXQZIuhXntd-f1cmgeu_8ZEafeXZRFHlvvViCdPWlMH_pm-kYLLZIJqyoE2qv385EB7xMDRFf6GsE5a-MDKNyzda95yL7xhj6fqS3gxir_m0KLd2IsuCD8xKbMyAV6K6D6TGlwOonsvvFBhqzcZV30BAmtUk67f7y1KUvvYoywDfYnRwKdcFAUL6WxN7Ln9IzFAqJIm82oM-PZjhBgQ_jhvXOCzV0fQ4t6fBH2D3EHmKB0oyJyC3zSB66KTvBIssRFKxohPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلیا هاشمی:  امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت. مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71695" target="_blank">📅 00:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71694">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ایلیا هاشمی:
امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت.
مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین لحظه لغو شد؟ یا مسئله‌ای دیگر…
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71694" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71693">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=CL0jHkTTDpLkOBy4xPE3akwGxgcNWDh56b0NlAyqscFan0EG05JUNzfaRI1TY37eRlpngQEWUdKWF0GmSLPPK0VeBRmnytuj7XeQkUDyJ7hWLz10uuFYBSOPPSYOPswmAieDlekbI8A-mjXXiexOHOZI3SASq62rXyGlpccdW7nlLrA9GEbpKyNT2NyDnDzRy9mV9p7EBWceiPNT2rUIcBKBiTaqCte-_E9ysMC6fgCNELnjDivl35VvrzkIPtHG9wERCpiIWuXGsKyp8OSFQyGmBAYxl2ivebzl9TCCfcHTHeXul3dxpibRZ5v2KBTo1NDAJlQOlZ4MJuJel-EWXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=CL0jHkTTDpLkOBy4xPE3akwGxgcNWDh56b0NlAyqscFan0EG05JUNzfaRI1TY37eRlpngQEWUdKWF0GmSLPPK0VeBRmnytuj7XeQkUDyJ7hWLz10uuFYBSOPPSYOPswmAieDlekbI8A-mjXXiexOHOZI3SASq62rXyGlpccdW7nlLrA9GEbpKyNT2NyDnDzRy9mV9p7EBWceiPNT2rUIcBKBiTaqCte-_E9ysMC6fgCNELnjDivl35VvrzkIPtHG9wERCpiIWuXGsKyp8OSFQyGmBAYxl2ivebzl9TCCfcHTHeXul3dxpibRZ5v2KBTo1NDAJlQOlZ4MJuJel-EWXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سریع‌القلم:
آمریکایی‌ها بعد از انتخابات کنگره به سراغ عملیات نظامی علیه ایران می‌آیند چه دموکرات ها پیروز شوند چه جمهوری خواهان!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71693" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71692">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71692" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71691">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71691" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71690">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=kyHWkgB1BqkKfs1IbGL7nSIaU0FqiQzmZwXxdZplGpYx5v3g9yj-H-9KjF3FFeoRAnBDxEIqfLOED46n4jTbqSan9AXN4Gj3fUyobDKRFO1EqiURMinqd1kYqjei4wAGjRNIIxTnQRG8nQCsi-ru-xYcwUyq1xNqHR5lJkA9gqaPeRtBdWPoLnogcYkpOAmDPN-_7fPsQL3PDwpyMVoxVl1Nvy008azY3dujo8bPeBXrhqwyDu_0a81pJ6zQzSiudZ83y7HGxsHvmMvgPSVnE7pf46ZKSN8YfM0PUczAS7ZMF_gHDbp_Y_eBnI196DZ3kehaxb5MBR1P8Hih9P9q8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=kyHWkgB1BqkKfs1IbGL7nSIaU0FqiQzmZwXxdZplGpYx5v3g9yj-H-9KjF3FFeoRAnBDxEIqfLOED46n4jTbqSan9AXN4Gj3fUyobDKRFO1EqiURMinqd1kYqjei4wAGjRNIIxTnQRG8nQCsi-ru-xYcwUyq1xNqHR5lJkA9gqaPeRtBdWPoLnogcYkpOAmDPN-_7fPsQL3PDwpyMVoxVl1Nvy008azY3dujo8bPeBXrhqwyDu_0a81pJ6zQzSiudZ83y7HGxsHvmMvgPSVnE7pf46ZKSN8YfM0PUczAS7ZMF_gHDbp_Y_eBnI196DZ3kehaxb5MBR1P8Hih9P9q8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای جنجالی یه
جنده
: دختری که ادعا می‌کنه باکره‌اس، دقیقا به چی افتخار می‌کنه؟
تو قطعا ایراد داری، مگه میشه یه نفر با کسی رابطه نداشته باشه؟ آقایون حتی توی سوراخ موش هم فرو میکنن، اونوقت تورو نکردن!؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71690" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71689">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=OT0xaMm4tUBPUSVyf0GPgNaGO7VRpNPDubZ4QcLjDRZA151QZl2EilouanWCay8CE6Jv5xukfJFYKWouqLRK44Nn3pcK3Pj6Tb20Et6dcs8Lk9XRvxYHMOctiLzX-s6RrQYpc28DNGpxxPAEKwhOsnSx1dadQOUvIJCCz5KR2jPXEmU8CxXF0PkW8uUfh46_50ZZ75NCYREtlHAN1p5_rUCluTecppssyqROwekPlvaqZLR6sQecQdXc8RbV6aJZRr8HhvPj_YioTUUXOzjdA4yjDnr5PZUrb-rjOiZLa-RKnNHDicZ5KOMj6U2F_ox8dbof07Xhw_qzadtQeaigUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=OT0xaMm4tUBPUSVyf0GPgNaGO7VRpNPDubZ4QcLjDRZA151QZl2EilouanWCay8CE6Jv5xukfJFYKWouqLRK44Nn3pcK3Pj6Tb20Et6dcs8Lk9XRvxYHMOctiLzX-s6RrQYpc28DNGpxxPAEKwhOsnSx1dadQOUvIJCCz5KR2jPXEmU8CxXF0PkW8uUfh46_50ZZ75NCYREtlHAN1p5_rUCluTecppssyqROwekPlvaqZLR6sQecQdXc8RbV6aJZRr8HhvPj_YioTUUXOzjdA4yjDnr5PZUrb-rjOiZLa-RKnNHDicZ5KOMj6U2F_ox8dbof07Xhw_qzadtQeaigUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی ایران یه تور راه اندازی شده به اسم «هیلینگ آب دریا» ، این شکلیه که میرین کنار ساحل و تا جایی که میتونین باید گریه کنین.
برای شرکت در این تور هم میلیونی باید پول بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71689" target="_blank">📅 22:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71688">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان با انتشار بیانیه‌ای مشترک، برای(فردا) روز چهارشنبه ۲۵ شهریور ۱۴۰۵ (۱۶ سپتامبر ۲۰۲۶) فراخوان اعتصاب عمومی صادر کرده است. این فراخوان هم‌زمان با چهارمین سالگرد ژینا (مهسا) امینی و آغاز اعتراضات «زن، زندگی، آزادی» اعلام شده است.
در این بیانیه از بازاریان، اصناف، کارگران و دیگر اقشار جامعه خواسته شده است با تعطیلی مغازه‌ها و بازارها و خودداری از حضور در محل کار، در این اعتصاب مشارکت کنند. صادرکنندگان فراخوان، وضعیت اقتصادی، فقر، گرانی، بیکاری و همچنین آنچه تشدید فشارهای امنیتی و صدور احکام سنگین می‌دانند را از دلایل این اقدام عنوان کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71688" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71687">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265561794f.mp4?token=kGE5ckojkGscB4XWsPw-FpY_u_6lMor6-BmqWF6E9utAoaKvLd6HY2ho4EwZv3Sea8tpcizDtV09-jgcKgabgJv6YLKahiQXYzGBJy8RfJGkVghfSl9IiszlXjcyuAbpXenszkZTGuBb_-wlhzMHuef7m9kI0vqV0kQ8S4okV7Sldym7Q8bqAsMYqos_KvXJdJPymFmGT6hnaHMY5-H4W6XKbUAJXEE7Rs49AmbaS3Nj08ownaIg9zNZ7Jl2V_y9711bVcFkHwHUJXEHDjp0tW2fS676L5f55fyFnzVId1S2scvVJ9KeoaEA3eyYBpx_JRtwF1K9Iysh8DraMZ-Thw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265561794f.mp4?token=kGE5ckojkGscB4XWsPw-FpY_u_6lMor6-BmqWF6E9utAoaKvLd6HY2ho4EwZv3Sea8tpcizDtV09-jgcKgabgJv6YLKahiQXYzGBJy8RfJGkVghfSl9IiszlXjcyuAbpXenszkZTGuBb_-wlhzMHuef7m9kI0vqV0kQ8S4okV7Sldym7Q8bqAsMYqos_KvXJdJPymFmGT6hnaHMY5-H4W6XKbUAJXEE7Rs49AmbaS3Nj08ownaIg9zNZ7Jl2V_y9711bVcFkHwHUJXEHDjp0tW2fS676L5f55fyFnzVId1S2scvVJ9KeoaEA3eyYBpx_JRtwF1K9Iysh8DraMZ-Thw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی سخنگوی دولت :
امیدواریم نیازی به تغییر سهمیه‌های اول و دوم بنزین نداشته باشیم؛ ولی اگه بخواهیم گرون یا کمش کنیم حتما شما مردم را در جریان خواهیم گذاشت و بدون اطلاع‌رسانی کاری نمیکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71687" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71686">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شنیده شدن صدای دو انفجار از سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71686" target="_blank">📅 21:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71685">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/61894edf33.mp4?token=HR-C8zva3jWvVX0ZWKc7TQvlSQIdcIFYl6NAVFqc8ztR4OSybBNVQlaS00AzjHa1wfreCznb54ZBEXZpaNSuHPX5zdvrQkR_OxOIPL9sEamFf1TP-D53zjW_Y4-LcGSZU13zkvAKwIo7XuuDmBYOXcIBgX2mhIWnvyYAHj3-1Rg_Zbr85M4yqNGt9YPEP5SfnQdRWY8IJ88a9d3bdstO6bnlM-fXrlDGnBc67jj_a0GzR9EJsRXzVa7AASF5v_rXdMCLshKqbEh_mLy1LBFcTwz18BPMvoxPP4-DZw-DSdDTnfoU-bQimd5anf2o2tXHKyJ8_vfP-Kqtu7dubDWWaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/61894edf33.mp4?token=HR-C8zva3jWvVX0ZWKc7TQvlSQIdcIFYl6NAVFqc8ztR4OSybBNVQlaS00AzjHa1wfreCznb54ZBEXZpaNSuHPX5zdvrQkR_OxOIPL9sEamFf1TP-D53zjW_Y4-LcGSZU13zkvAKwIo7XuuDmBYOXcIBgX2mhIWnvyYAHj3-1Rg_Zbr85M4yqNGt9YPEP5SfnQdRWY8IJ88a9d3bdstO6bnlM-fXrlDGnBc67jj_a0GzR9EJsRXzVa7AASF5v_rXdMCLshKqbEh_mLy1LBFcTwz18BPMvoxPP4-DZw-DSdDTnfoU-bQimd5anf2o2tXHKyJ8_vfP-Kqtu7dubDWWaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، هواپیمای تهاجمی A-10C Thunderbolt II نیروی هوایی ایالات متحده، مواضع داعش را در نزدیکی «جبل‌العمور» در شرق استان حمص (مرکز سوریه) هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71685" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71684">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1QdwUeNvTTaRd3l3W-AxIG5ONgTFoAAR_xEPvclStGG6YgNdKClYSJ8-xJqNLF8e4hvfPKIB2ZEHrzxYeJnFuhYxH9LX4Mu9o4TPxDe9qbxpW2LpAjkUyAH_8rcWnygumXkttijTPA_D5s-7Xjy-lrXgCYnP3dWownPIYOPuZqPKxLiQ5GVEeCvws40JjfjH7TRry8dIsZMijmBMQJKggPtYrJcB6epoha0YKTLcLCC5nEsiU6UI0gRcbB8nHIyK-OsohJaPhytGDDonrm37beHT59l1vkJd6r6TA-t1tz4VuiwBirr_9dieGknVXNg0lgwm9PYNL2hWomvCw2t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن پست:
دولت ترامپ در حال تدارک فروش ۴۰ هزار بمب سنگین (از انواع MK-84 و BLU-117 با وزن ۲۰۰۰ پوند) به ارزش ۲.۸ میلیارد دلار به اسرائیل است؛ این بزرگترین معامله تسلیحاتی از این دست در سال‌های اخیر محسوب می‌شود که هزینه آن از محل پول مالیات‌دهندگان آمریکایی تأمین می‌گردد.
این‌ها همان بمب‌هایی هستند که بایدن پیش‌تر به دلیل نگرانی‌ از تلفات غیرنظامیان، ارسال آن‌ها را به‌طور موقت متوقف کرده بود.
این قرارداد برای تصویب به کنگره ارجاع می‌شود و می‌تواند آزمونی برای دموکرات‌ها باشد؛ چرا که در ماه ژوئیه، بیش از ۱۰۰ نماینده دموکرات مجلس نمایندگان به کاهش کمک‌ها به اسرائیل رأی داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71684" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71683">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=iU4xhHy6UFpQHPiDDUPr2uTQeD_0HW47S5NF0LhcgnA_s8KMPFdGPZ3zKWlyIJmfeG_zX-Tmx3uub22Uyf4_DeQAzcORWQ7MJXnVWcfiJ17M7SXgrCx5NsWDEHZ48SfFtu0Ru-Vh6cytuWNun-6mKN6eJAgRkamv1p-kDcnpKed5ItCNED3r-NXxZ3xseDsPB4b6SfbGGkICzSFAcQ6lkcB_pgHMKWAC6wWn8iU3Y4akEMtBgNPhKSlSCOwvxYQSvCc8daypZEf9dL5CqpEgqwc5xCOzA4LmbhM9SPeLPaIeXnuOJ3OJn08kt4ZZpGF3pqrhLQNMeOsxnzz24u81KYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=iU4xhHy6UFpQHPiDDUPr2uTQeD_0HW47S5NF0LhcgnA_s8KMPFdGPZ3zKWlyIJmfeG_zX-Tmx3uub22Uyf4_DeQAzcORWQ7MJXnVWcfiJ17M7SXgrCx5NsWDEHZ48SfFtu0Ru-Vh6cytuWNun-6mKN6eJAgRkamv1p-kDcnpKed5ItCNED3r-NXxZ3xseDsPB4b6SfbGGkICzSFAcQ6lkcB_pgHMKWAC6wWn8iU3Y4akEMtBgNPhKSlSCOwvxYQSvCc8daypZEf9dL5CqpEgqwc5xCOzA4LmbhM9SPeLPaIeXnuOJ3OJn08kt4ZZpGF3pqrhLQNMeOsxnzz24u81KYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از نفتکش «ال‌گایا» (EL GAIA) پس از اصابت به آن در بخش جنوبی تنگه هرمز منتشر کرد.
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که ایران ماه گذشته با موشک و در پایان هفته جاری نیز با پهپاد به این نفتکش حمله کرده است؛
در مقابل، ایران مدعی است که این شناور پس از ورود به «منطقه ممنوعه» در بخش جنوبی تنگه، با یک مین دریایی برخورد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71683" target="_blank">📅 20:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71682">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=og-vZtCLLJLdcovhIB6Yjx_9awSHD3677lq8rRhEfN6Z4Fp9pcnk6WZ3T8UyF3DNaFW5lKkf2bCCV_lmVGA4qF-51EyvuLDA3yoYX10gLrKKdsjTM0U8zHgKYmpPlpSD_Z4YYYa5e6HdCfqcZEnOtGqWvuVC_BbnZf_7UQPjlGH7YN3EQtei5gTVcM0PZTo9UbkskQ0GfPWLWw7_CfFyGdi5VgssQwxe-2awkR5lh0AFYnFDNJFFnNK6wuY16hp3P0Be_P15gWyxq6Cw6aJldcJr6Eh2E_c5tvi9jIAB_ROhXSUmSPiLo54dZK5-b3C9C80Ov2a_pCzrFvBus7Rh2x1p6qJ1aw7X6fOJx-yR2V46lFJR6cBwU8MoJTFaXsl0dce7iN1yBHHsu_xmnOp-rOmXSM0ZxNvLg0l8RwwI-lJieDbmHVbGmrRs-FmPIb5MFnAPEFAOEuS41UQ1KH8wbHY-DgtSZauNT7DgqsKI7W-KNUX-yQDc7AotzkHVmUFAaxFh0qAAt0Y5PMlgySmEhghANduFKhUKLn12JI1MytdH6WD8feFsRFcWK2Vq0jkSOWArrGw46dM4IcI_cOBWzcyRFOUDGU6xP3Mefw78kO7FliMJSA0-_zJzWPleGnowFqhcLGjRGBG_UBNkMOfySjHrsyxywfGT6ucA8Et5Cy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=og-vZtCLLJLdcovhIB6Yjx_9awSHD3677lq8rRhEfN6Z4Fp9pcnk6WZ3T8UyF3DNaFW5lKkf2bCCV_lmVGA4qF-51EyvuLDA3yoYX10gLrKKdsjTM0U8zHgKYmpPlpSD_Z4YYYa5e6HdCfqcZEnOtGqWvuVC_BbnZf_7UQPjlGH7YN3EQtei5gTVcM0PZTo9UbkskQ0GfPWLWw7_CfFyGdi5VgssQwxe-2awkR5lh0AFYnFDNJFFnNK6wuY16hp3P0Be_P15gWyxq6Cw6aJldcJr6Eh2E_c5tvi9jIAB_ROhXSUmSPiLo54dZK5-b3C9C80Ov2a_pCzrFvBus7Rh2x1p6qJ1aw7X6fOJx-yR2V46lFJR6cBwU8MoJTFaXsl0dce7iN1yBHHsu_xmnOp-rOmXSM0ZxNvLg0l8RwwI-lJieDbmHVbGmrRs-FmPIb5MFnAPEFAOEuS41UQ1KH8wbHY-DgtSZauNT7DgqsKI7W-KNUX-yQDc7AotzkHVmUFAaxFh0qAAt0Y5PMlgySmEhghANduFKhUKLn12JI1MytdH6WD8feFsRFcWK2Vq0jkSOWArrGw46dM4IcI_cOBWzcyRFOUDGU6xP3Mefw78kO7FliMJSA0-_zJzWPleGnowFqhcLGjRGBG_UBNkMOfySjHrsyxywfGT6ucA8Et5Cy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
تنها کافی است به سخنان رئیس‌جمهور، رئیس مجلس و رئیس بانک مرکزی ایران اشاره کنم که اذعان داشته‌اند اقتصاد کشور در وضعیتی بسیار وخیم و بحرانی قرار دارد؛ هشداری که خطاب به هم‌قطاران تندروی آن‌ها در سپاه پاسداران و همچنین مردم ایران بیان شده است.
ما شاهد سقوط ارزش پول ملی و تورم سرسام‌آور بوده‌ایم؛
و در کمال ناباوری، کشوری که سومین ذخایر بزرگ انرژی جهان را در اختیار دارد، اکنون با قطعی برق سه تا چهار ساعته مواجه است.
این وضعیت اسفبار اقتصادی ناشی از تحریم‌هاست؛ ترکیبی از تحریم‌ها و اقداماتی که ما طی ماه‌های گذشته برای شناسایی و مسدودسازی مسیرهای مالی و سیستم‌های پرداخت آن‌ها انجام داده‌ایم و در حال اعمال فشار شدید بر آن‌ها هستیم.
به باور من، واکنش‌های تند و خشونت‌آمیزی که اکنون از سوی آن‌ها شاهد هستیم، درست مانند رفتار حیوانی زخمی است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71682" target="_blank">📅 19:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71681">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=q5LKu1uLXoUivwOXz5ChpWNB05iNf-aPHXxhmZDYCPbXqA_IgcT0bUJSCH0bLTpKhpkCDGGDfn_hQfBMAfo5cksCdCN9cTjDa5njTpmzPsIhT644T22tSBect9jih6pEWgoZDn7gvcH6jWa1JncpNtGqPt-yU10CG6TsDWFzgXP6Dy1qUXd9K5pxA935pz1lkzcE9reWN7AAVzhEF4hya9VkDXi87SDt26XWasS7qxTj62aT6JUGyflmj3bLEV9ALexl11cfR2-Y4aE7taRAQ61bXSQ8SqDHH8w8m8TVCCDdJaq1sLjERSs5-TWEomtDt66_OM13t4T4JzPr8U-1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=q5LKu1uLXoUivwOXz5ChpWNB05iNf-aPHXxhmZDYCPbXqA_IgcT0bUJSCH0bLTpKhpkCDGGDfn_hQfBMAfo5cksCdCN9cTjDa5njTpmzPsIhT644T22tSBect9jih6pEWgoZDn7gvcH6jWa1JncpNtGqPt-yU10CG6TsDWFzgXP6Dy1qUXd9K5pxA935pz1lkzcE9reWN7AAVzhEF4hya9VkDXi87SDt26XWasS7qxTj62aT6JUGyflmj3bLEV9ALexl11cfR2-Y4aE7taRAQ61bXSQ8SqDHH8w8m8TVCCDdJaq1sLjERSs5-TWEomtDt66_OM13t4T4JzPr8U-1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر، آتش‌سوزی‌های گسترده در تأسیسات ذخیره‌سازی «آرامکو» در «ابها» واقع در جنوب غربی عربستان سعودی را پس از حملات پهپادی و موشکی حوثی‌ها نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71681" target="_blank">📅 18:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71680">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
لحظاتی قبل یک پهپاد دیگر از نوع MQ-1 متعلق به آمریکا بر فراز تنگه هرمز با استفاده از یک سیستم پدافند هوایی متعلق به نیروی قدس سپاه پاسداران انقلاب اسلامی سرنگون شد.
این سومین پهبادی است که سپاه مدعی سرنگونی آن در روز جاری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71680" target="_blank">📅 18:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71679">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8132b94509.mp4?token=oVO3gH2u7MaPgCBrmd1oNVDDeZlsugv2SZiLwBDGF3B1-iSiwPl5dDgzWNtStI_Jo3-NdGfh_c0lCsrEKyJ4GTMqNF5qpG0xJTvmM58m5RJVCZDZkO9wZVWVGA9tFXOwT6RaPCWoD6OV5wOwm0AmvLbvNCmpy-8zrS14yWp38UGfPXYHloC5pfFBS9LDUf3cz_fxvG62G-UcB7icges1iQxovxAEGb0tWMCTpfU4s2SxRG2UyAC3m55clhQkHb52Vcm-nGVm2YFaD2SU_QbY1rjdOzN_gnjtfKiSxhRvzbWkt5U48W6RfULSjcI14mQxzQviUKL32EwvFQZqwLP99g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8132b94509.mp4?token=oVO3gH2u7MaPgCBrmd1oNVDDeZlsugv2SZiLwBDGF3B1-iSiwPl5dDgzWNtStI_Jo3-NdGfh_c0lCsrEKyJ4GTMqNF5qpG0xJTvmM58m5RJVCZDZkO9wZVWVGA9tFXOwT6RaPCWoD6OV5wOwm0AmvLbvNCmpy-8zrS14yWp38UGfPXYHloC5pfFBS9LDUf3cz_fxvG62G-UcB7icges1iQxovxAEGb0tWMCTpfU4s2SxRG2UyAC3m55clhQkHb52Vcm-nGVm2YFaD2SU_QbY1rjdOzN_gnjtfKiSxhRvzbWkt5U48W6RfULSjcI14mQxzQviUKL32EwvFQZqwLP99g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پروازهای داخلی(کرمانشاه به مشهد)دچار سانحه شده و بخشی از کابین دچار شکستگی و اسیب میشه، خوشبختانه مسافران این پرواز سالم به مقصد رسیدند. جزییات دقیق این پرواز و نقص فنی هنوز مشخص نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71679" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71678">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71678" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71678" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71677">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsYK_AnOnCqEtWaizFT55uhtNZ2tJiIC08xQ3NVBFf6kHUt0dBOuQTcjFgPCkHY-DPyxEbHHmAaJsN9kp4tZfBlBU8lrHZS-eiuOI-b8Ad5k7Fr88K7u-4kz41_vYU0LtGEg8Kdj6_bOkodey6QkjZgMbNwckSdkgkM2nylb5zuI83YQGhmzLoVD4O2siM-ar2uC5O41-GWHIVRxlzSmOqmIYj-hsiQIuqLvB4uvjO_HoIPAe343vUQx5dmkPnZnC10wdhfyCaWN_WEs55DYsBh-bLRB1EYTgz-zvq3uu6129Qr9JPjsf9WQ_2nbSzbpT-MHOxbY6gseRp7qxxUgLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
تاتنهام
🆚
لیورپول
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
تاتنهام: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
⚽️
لیورپول: ۲ برد، ۳ تساوی و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71677" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71676">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=E2FZLPStjp5r-oHARq_2Yw4nhG0w2HVP0DUXfx4bxnnP34dw-Kqp8RJM_hxDdKTNht4LVNoUjjjWaqjnk614rnYd-6rscox8CZwkpVCsvDgDbqWPP3Q8izFvfluw0VgTxaBVMG0dyApWWXZ3NjHiRUdQRmQYABbqErCDwdVq_3h-lciCXjstPYpkqY-9dzNrLNF173r0kRXv2sHVKmOKQ8YDequlXeIzaf18tRQLPhV_n5QMXUDO8cbQ4wRTzZ55k2jZzhdo1jBRRS2mslp8s_Xc3tVNUpVEoJFsFzEnniLk-o581dnUA-cHiTCMvjoqMDdskxuoTJyFqbRJ_XzI4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=E2FZLPStjp5r-oHARq_2Yw4nhG0w2HVP0DUXfx4bxnnP34dw-Kqp8RJM_hxDdKTNht4LVNoUjjjWaqjnk614rnYd-6rscox8CZwkpVCsvDgDbqWPP3Q8izFvfluw0VgTxaBVMG0dyApWWXZ3NjHiRUdQRmQYABbqErCDwdVq_3h-lciCXjstPYpkqY-9dzNrLNF173r0kRXv2sHVKmOKQ8YDequlXeIzaf18tRQLPhV_n5QMXUDO8cbQ4wRTzZ55k2jZzhdo1jBRRS2mslp8s_Xc3tVNUpVEoJFsFzEnniLk-o581dnUA-cHiTCMvjoqMDdskxuoTJyFqbRJ_XzI4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
بسنت درباره ایران:
ترامپ در حال اقدام علیه رژیمی است که خود را وقف شعار «مرگ بر آمریکا» کرده و برای تحقق همین هدف به دنبال دستیابی به سلاح‌های هسته‌ای است؛
اقداماتی که رؤسای جمهور پیشین مدت‌ها از انجام آن طفره می‌رفتند.
تحت رهبری او،آمریکا دیگر تهدید ایران را مدیریت نمی‌کند؛ ما در حال پایان دادن به آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71676" target="_blank">📅 18:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71675">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG_NBGoidIHFz4YxqaeOW0pwwdin5Ikt9TLahv72Mx8nUozGmGT3DRUXPeKqe1mA-kyeGhGD1oKHHJarPZ5WLRlcRjhIdZlnn9lcr37CgECi2avJlXJpxILuhBuZEATeyfe8XHlR_WxM5xZz29VDP-gzznIFR41UxhfKokSlF_3tFBb2XgipDeNBI6aie3UqbDAMUvX9eQafWEvx8rBLLO3KgDOYDGgp_x1A2GfRA_tuumiNNlFZmsCqX4jvIwuN4nGiQLNMbNuKofiZjzLuPQJ7d2qvtuq11-nHtsUB1Ii3swqYuwg_W7V0M1H1oweqR4lnRAkXPs7CvSPzex14Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس. تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.   @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71675" target="_blank">📅 17:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71674">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=COtYnsflvn5E5-W8Y45cNyH6m7voR3Pz-futMDykdnYShGSHuoeWpZnTSl6fNsRYGVuHaR_3-3QC5l2khddkCuJckYZLHyVT1yrQTgCsE_9Mp4Ip9dPG4mdGAZxZAVSCWStZpX7mJHddbCAkZ8sb1w__rbNAv405UQutLS35xlACp-6AWL4d9Mksj1gBjiFprkI-FmK3vvNI2djlD3dhba2FRgONPt6SVQswldYobQu1YYc_3zMHx9rXUSUp2cbkRRonXWL4o_w0aFMcebH79WnWJn7SR7FKEcCSi22p_BKnN-rI4MS3rEreVsEItAZb4fjrYhY5mQEFajo7-EzNHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=COtYnsflvn5E5-W8Y45cNyH6m7voR3Pz-futMDykdnYShGSHuoeWpZnTSl6fNsRYGVuHaR_3-3QC5l2khddkCuJckYZLHyVT1yrQTgCsE_9Mp4Ip9dPG4mdGAZxZAVSCWStZpX7mJHddbCAkZ8sb1w__rbNAv405UQutLS35xlACp-6AWL4d9Mksj1gBjiFprkI-FmK3vvNI2djlD3dhba2FRgONPt6SVQswldYobQu1YYc_3zMHx9rXUSUp2cbkRRonXWL4o_w0aFMcebH79WnWJn7SR7FKEcCSi22p_BKnN-rI4MS3rEreVsEItAZb4fjrYhY5mQEFajo7-EzNHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سی‌و‌سه پُل اصفهان، یه پسر نوجوون اومد مثلا یه حرکت نمایشی بزنه و از یه ارتفاع نسبتا بلند بپره پایین که فرود ناموفقی داشت و با سر رفت تو زمین...
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71674" target="_blank">📅 17:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71673">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=Ikt6zieIVTtH5i7aJogq0_0AO11e8CKlS7eaCJ1R_5v2831Su_e149SMEanLr1nA1l9qA4jKjvtO_2xiFGtvcK8LMiJuVAqjZte9sHd2qklKRnJj8XqE59493yDZd76AWxHya9Rf-ayFdjrxN2cEoVpjsLwjYPuYy9PMdRul2w_nI63pWIOvBDu8xYbLk8lYm1usqw2g8PVRDiiC8sV6NhA_H5tyIfCqzcQ-bqHNue9IqyCM8CtgytR81yITSC7f3azn3Nx1djm7aGkhc0K7BrGeyJ3krYL0_IExLignRKahktXTnv9wsgKYlHEtsRRCrXqXweuzXxqGY7kg8UpTaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=Ikt6zieIVTtH5i7aJogq0_0AO11e8CKlS7eaCJ1R_5v2831Su_e149SMEanLr1nA1l9qA4jKjvtO_2xiFGtvcK8LMiJuVAqjZte9sHd2qklKRnJj8XqE59493yDZd76AWxHya9Rf-ayFdjrxN2cEoVpjsLwjYPuYy9PMdRul2w_nI63pWIOvBDu8xYbLk8lYm1usqw2g8PVRDiiC8sV6NhA_H5tyIfCqzcQ-bqHNue9IqyCM8CtgytR81yITSC7f3azn3Nx1djm7aGkhc0K7BrGeyJ3krYL0_IExLignRKahktXTnv9wsgKYlHEtsRRCrXqXweuzXxqGY7kg8UpTaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71673" target="_blank">📅 16:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71672">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نفتالی بنت درباره ایران:
این رژیم فاسد و پوسیده است؛ همچون درختی که از درون دچار پوسیدگی شده و سرانجام فرو خواهد ریخت.
در مورد این درخت پوسیده، می‌توانیم اینجا و آنجا حفاری‌هایی انجام دهیم. منظورم صرفاً اقدامات نظامی (کینتیک) نیست.
صحبت من درباره اقدامات اقتصادی، کارهایی که نمی‌خواهم نامی از آن‌ها ببرم، و همچنین تقویت معترضان داخلی و تقویت دشمنانِ این رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71672" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71671">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=D0ZJywnSm2tRbD2WwJOxSO2Y_CLFf1-VrxYjaMtAL-QVkELUmsx3Jq_uCr8QLwI9gJayP_SSBSyx2LI_tBRJs8y-yT6CKmtCS1kbiBKna9iFsjDS7FBpiQwIiLwBFk1mwLAlhrBzLMj_3Zss6Ta-4IIaOjPKNa6iLKzbAx7-ysfyPoaX19FhDGCFFp7vBruHQCwYyX327o6HpnKZfSOPySE9aa8R4lQvph1WixbhLncRGqtSPF2XOfLQQIV2nZesVYp-XfTMHT_ThpPXh9VXRA2XTarc9qAopVsdWGnvTbA_dXRLiaN00oXzMvZtFpRAYhaToVVdUaN6tmX4VcBaWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=D0ZJywnSm2tRbD2WwJOxSO2Y_CLFf1-VrxYjaMtAL-QVkELUmsx3Jq_uCr8QLwI9gJayP_SSBSyx2LI_tBRJs8y-yT6CKmtCS1kbiBKna9iFsjDS7FBpiQwIiLwBFk1mwLAlhrBzLMj_3Zss6Ta-4IIaOjPKNa6iLKzbAx7-ysfyPoaX19FhDGCFFp7vBruHQCwYyX327o6HpnKZfSOPySE9aa8R4lQvph1WixbhLncRGqtSPF2XOfLQQIV2nZesVYp-XfTMHT_ThpPXh9VXRA2XTarc9qAopVsdWGnvTbA_dXRLiaN00oXzMvZtFpRAYhaToVVdUaN6tmX4VcBaWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌ های این خانم به‌شدت وایرال شده و دخترا هم خیلی بهش انتقاد کردن:
اگه یه مرد، دارایی های خودش رو به نام خانومش بزنه، اون زندگی رو با دستای خودش نابود کرده.
آقایون اگه ۵ تا خونه هم به نامشون باشه، هیچوقت تو دعوا خانوم‌ خودشون رو بیرون نمیکنن
ولی اگه خانوما یه چیزی به نامشون باشه به این موضوع فکر میکنن که میتونن بدون اون آقا ادامه بدن.
من خودم خانواده‌هایی دیدم که به دخترشون میگفتن تو که ماشین و خونه به نامت زده دیگه احتیاجی بهش نداری، خودت برو زندگی کن.
خانوما اصلا جنبه‌‌ی اینکه چیزی به نامشون باشه رو ندارن، اون اگه بخواد زندگی کنه با یدونه سکه هم زندگیش رو میکنه، آقایون بفهمید من دارم چی میگم...
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71671" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71670">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=OIslZ3o4IWimDHUGHphPuBkL3pu-V_xMY2q1ozV8gsqDIBP95cvx8mbidZDJG4yLvIGZFuM5MU7HcvMEJF7Ofa5t9hQzwID55H5dSaer11JIkChSik0wUX64BgRczNwpVYeraYxAeTJAMlKWdkZf_nLv8zwUolqobFipAR0wCsrwT3Zabr_U9zE3gKFPqWDHGfb7gKsWt8PkRIrMefh4XkK4xTnK0UHHNpSdoreOgOgdnm6rTe0DKC9iGRJiqJ-rhO8bw6peslx6qZnp9pIyblncDModcpIeFeDu8AqxNgRGP1JhLhqGGsch3lCgWD1rCi_sIfX-84EnZWq9hOmnvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=OIslZ3o4IWimDHUGHphPuBkL3pu-V_xMY2q1ozV8gsqDIBP95cvx8mbidZDJG4yLvIGZFuM5MU7HcvMEJF7Ofa5t9hQzwID55H5dSaer11JIkChSik0wUX64BgRczNwpVYeraYxAeTJAMlKWdkZf_nLv8zwUolqobFipAR0wCsrwT3Zabr_U9zE3gKFPqWDHGfb7gKsWt8PkRIrMefh4XkK4xTnK0UHHNpSdoreOgOgdnm6rTe0DKC9iGRJiqJ-rhO8bw6peslx6qZnp9pIyblncDModcpIeFeDu8AqxNgRGP1JhLhqGGsch3lCgWD1rCi_sIfX-84EnZWq9hOmnvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیراندازی نیروهای انتظامی به سمت بالگردآمریکایی در جریان عملیات نجات خلبان مفقودی آمریکا در روز روشن
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71670" target="_blank">📅 15:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71669">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=G4a6W4owuaFOZqfFEHiU0XXrUrtpAKFfCepUkasv5ph7tUJBj8qWfEneFuPUOQU3vZOAnhkfUQtCDUnoC6kUk_zKZObBs6xiHYtjipLq36PUTEOj_uqP40hiUAGxM8XirkNu9FlIWcadAkYU_0IWDlcxxuQ4DfcENbu4EclUmiimkJsmm8_79g7qZ60_Yu31ClIkc5h2vpMl4jTqSmiNzKaJ2WpwhrputnaVyPUb-1BuwakMkbF1aTeTjWEo0CqCIuNLx8zuJtDOckm75GZWkA4I4eYnMrwKORKleAKe20y6ry_Ke5DK2wfgf0-A_wEypxAwVmeLmKwYRboNCi4iXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=G4a6W4owuaFOZqfFEHiU0XXrUrtpAKFfCepUkasv5ph7tUJBj8qWfEneFuPUOQU3vZOAnhkfUQtCDUnoC6kUk_zKZObBs6xiHYtjipLq36PUTEOj_uqP40hiUAGxM8XirkNu9FlIWcadAkYU_0IWDlcxxuQ4DfcENbu4EclUmiimkJsmm8_79g7qZ60_Yu31ClIkc5h2vpMl4jTqSmiNzKaJ2WpwhrputnaVyPUb-1BuwakMkbF1aTeTjWEo0CqCIuNLx8zuJtDOckm75GZWkA4I4eYnMrwKORKleAKe20y6ry_Ke5DK2wfgf0-A_wEypxAwVmeLmKwYRboNCi4iXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر زنِ مجتبی خامنه‌ای:
مجتبی خامنه‌ای با همسرش سریال " فرار از زندان " رو مفصل نشستن دیدن و درباره اتفاقاتی که داخل سریال افتاده بود هم صحبت میکردن.
یه بار تو یه جمعی گوشی یکی زنگ خورد، من گفتم این چه آهنگیه دیگه؟ که یهو مجتبی گفتش این آهنگِ یکی از فیلم‌های کریستوفر نولانه دیگه، چطوری نمیشناسیش؟
‌
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71669" target="_blank">📅 14:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71668">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiX9GIInCP5VVuNzZ_fut804hG_ynJtibE_9DS56kF6Ly6WatSVAzk58PKCeQxjOEzD69pc7eHE4JN23ad-F3CAREdzJeLVyaPlGGouOAH_Peo8kVDo-NmVV3rffeYnTRRLHRQssu50zI67uYrOifSYEvouW70nJVIWtiMxXP8eGq0qXoAn-3eRGDcsv6UDcbUwBFHqThUBDUapV5ERM-JQuTII12q5HmJ2BtqL98sVu0VI-E2_i17dcNF_8Jzw5sKbUyHj-Dc_q_FF-UcnlRsO1NbpeGsEQ3I1iFd9jlmjWpjxYvHsyI0IcnL7p8zYSHWXvSExH9HsgCqBWgTb4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی:
«نشست عمان» با حضور کشورهای خلیج فارس برای تثبیتِ مسیر تنگه هرمز، با نقش‌آفرینیِ جدیِ آمریکا و برخی از کشورهای حوزه خلیج فارس فعلا لغو شد
عربستان» به بهانه اصابت خط لوله‌اش و درخواستی که از پاکستانی‌ها داشته تا ایران را راضی کنند که به انصارلله بگوید از فتوحاتِ جدید عقب نشینی کند، «بحرین» بابتِ ناراحتی از جنگ رمضان و پرتابه‌‌های متعددی که بخاطر میزبانی از زیرساخت‌های نظامیِ آمریکا در خاکِ کشورش دریافت کرده و «امارات» هم بابتِ اُفت جایگاش در آینده‌‌ی منطقه در صورتی که مسیر جدید تنگه تثبیت شود، در نشستِ مهمِ عمان شرکت نکرده و کارشکنی کردند!
ولی بازیگرِ اصلیِ لغوِ این نشست، آمریکاست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71668" target="_blank">📅 13:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71667">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حملات موشکی/پهبادی حوثی های یمن به مکه، طائف و جده عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71667" target="_blank">📅 12:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71666">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDYQBKEJtdC2wdNfQO6xnHWvWuvjzOgqONNqkHETkD6WhxQsjyoZqey5LsPcB9NQiUORiVPypOR06D3Qp_PNcdeijjS_4L2vOXIRvag_9fOl-9FeqeTw5mw36O2sOxbDm2SvjeIZqZ52Ib1gJoTLpMQbRIX03BCdZDNa3WG-gqgOhZKfframTs2cKKHUh9B6k8AyScjCcEipJAFZZ6QO2QX4TK5mNMxp9OtRy5KM1nkgBbjLYpmXcMvzzgdyDf0U9FudQvruW4JKgs5BWVnOchysq2xq0UWbbYnSzEwsJVF5eFrvud1KXD2FlRhKEBeoJaqc4mKhhyM_sDC7VcsCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) :
گزارشی با تأخیر زمانی درباره وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک منبع موثق گزارش داده است که شناوری مورد اصابت یک پرتابه ناشناس قرار گرفته است.
هیچ‌گونه خسارت یا پیامد زیست‌محیطی گزارش نشده و مقامات در حال بررسی موضوع هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71666" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71665">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=IKCp0oyNeC9AmTZc0lg_uUd6BGlNr5BYLvlauU0WqqDowMbNj83VS_LJuLlVUlWpUXiqd576kgKogAmSP7XTBmCcWfxih3g70avjna3U3Rm1oVObosidYyZUBzRz3KxS1jYPWBhMw7l8Vq3vm8XuLq9h0KfYXrCN4l3eHRI9r3_YggjXPI7MFX7sv9Q2yN1alwN0eFHFKS90UD8DCZt23BGN2selbDJU-yEOfkw8mzq69e7tnx-zCOWHX2dSd411iE377RREHbOFSBU2BMlYHN4Ur8tQufuuMWAYa-mF_qK9-BU_fmJVFaWQLgpWgZpW6Vy8FZ9kj2uXO4yGuyEVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=IKCp0oyNeC9AmTZc0lg_uUd6BGlNr5BYLvlauU0WqqDowMbNj83VS_LJuLlVUlWpUXiqd576kgKogAmSP7XTBmCcWfxih3g70avjna3U3Rm1oVObosidYyZUBzRz3KxS1jYPWBhMw7l8Vq3vm8XuLq9h0KfYXrCN4l3eHRI9r3_YggjXPI7MFX7sv9Q2yN1alwN0eFHFKS90UD8DCZt23BGN2selbDJU-yEOfkw8mzq69e7tnx-zCOWHX2dSd411iE377RREHbOFSBU2BMlYHN4Ur8tQufuuMWAYa-mF_qK9-BU_fmJVFaWQLgpWgZpW6Vy8FZ9kj2uXO4yGuyEVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبه ناو سپاه با عنوان «رودکی» که در جنگ ۴۰ روزه منهدم شد در حال غرق شدن است. این کشتی تجاری بود اما به نظامی تغییر کاربری داد و گفته شد هلی‌کوپتربر است اما هدف حمله قرار گرفت و نابود شد.
در جریان جنگ ۴۰ روزه تقریبا تمام شبه ناوهای سـ.ـپاه و ارتش از بین رفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71665" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71664">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71664" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71663">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfXN2IbDpLVGy14iQgGPdS6Xs6G1Zw3QUzLh0YxBUXjAfZa7jvap13A76U8evXjzZ_lIkeKohmU_X_Wryq4D2jxbJXvkM3Te0oMJ_RrsNtIKJ_B4MN3uUTockuuHqWwP-tJC5ZkxYUHtMPRyFJAkgzyJhlOggdc8xBELTakaboNtfkpGbqKt0rWJzxGTUAAp8JEsQ-Wga5kXbUIZjpHXUdfgixPhZi7EwuM8L5ML-v63K0UGCKrm8-wqirzOKPIMMp1CZ2LsoMKc27B8MSz0zMm8FOBv1NY_bGOZX30JdKKeKlb9ZlaZYGYn2ukAZGRhJX7nxeuffd3dhxoQ6O9zdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
رئال مادرید
🆚
الچه
⚽️
را در TrexBet پیش‌بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
رئال مادرید: ۴ برد، ۱ شکست و ۱۴ گل زده
⚽️
الچه: ۲ تساوی، ۳ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71663" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71662">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cFIMnWWp724q-rKnH_18wiJzZzBk_wghP84B6EvQSmaRburPYw-D1VLKtFlCJ8lbJTnDOVuqHAwwnG4AnkVVJ6a08NFIkij3ncJ2sSkJ-_RMb1xkRswbQH1ZDOtgaf8sS-lubdwrIxZywCAq3OlfSvRk9flcN2x16uJHWfCEd1Ug0gQO7EUlOZg1uTzpiWhRQBvMyzdEdiiWg9ymhy-VIXiuTKmL-CiiB9V14NQiRxSRjT3Y7LhIvG9AcJsfrFRGODwvezX6umLqRLUItePd6Z26J6bqoaFyq3hQ4t9B9QxfJ_Wcql1G8WNCX667E6vRfXa8JM0mn6LDlfoAGP2uhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71662" target="_blank">📅 11:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71661">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=KyOhKkN4V52Zz7-OR28m13pwHWDov4frqPTGbggkLUC4Moz5N2UgO4nsjk4GS9F-6IEkNI20r53sBYQ6mS6_ikv3c0nh-1gU7nbNDs04-MkrNXRdZ2s5E57nFPOnwu8rq7WCWvcsVIirFa938sBd10Fp8SLqk458UPU-YzuiRoeOpFK0gH3NvA1kQAsTqfUtIrSwBuHeyvV5Qiw3ZJoMcvW-Xj_z2198KHjLkM889Nvoy1g3qjAaJYK9fhkBolhk90DuhVP0rFf0DfuxigMjWFBe76Z4NwoX5wEhdDjFV9V4vRRxNWv327o8UZiXlbrdykuZW167-bhaSTZNheo2yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=KyOhKkN4V52Zz7-OR28m13pwHWDov4frqPTGbggkLUC4Moz5N2UgO4nsjk4GS9F-6IEkNI20r53sBYQ6mS6_ikv3c0nh-1gU7nbNDs04-MkrNXRdZ2s5E57nFPOnwu8rq7WCWvcsVIirFa938sBd10Fp8SLqk458UPU-YzuiRoeOpFK0gH3NvA1kQAsTqfUtIrSwBuHeyvV5Qiw3ZJoMcvW-Xj_z2198KHjLkM889Nvoy1g3qjAaJYK9fhkBolhk90DuhVP0rFf0DfuxigMjWFBe76Z4NwoX5wEhdDjFV9V4vRRxNWv327o8UZiXlbrdykuZW167-bhaSTZNheo2yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: آیا قرار است همه ما تا ۱۰ سال دیگر بمیریم یا نه؟ موضوع بحث همین است.
ایلان ماسک: خب، متأسفم که باید این را بگویم، اما همه ما خواهیم مرد.
مجری: می‌شود یک بازه زمانی مشخص کنید؟
ایلان ماسک: بله، نرخ مرگ‌ومیر همچنان ثابت و ۱۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71661" target="_blank">📅 11:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71659">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎙
صحبت های این خانم درباره سگش:
خرج ماهانه سگم حدود سیصد/چهارصد میلیون تومنه
😳
روتین روزانش صبح حدوداً ساعت ۱۰ بیدار می‌شه، یعنی صبح همه رو بیدار می‌کنه. بعد تا ساعت یازده که می‌شه، یه مربی شخصی داره که میاد می‌بردش یه جا مثل فضای باشگاه.
بعد هم که ساعت سه و چهار غذاشون رو می‌خوره. پوستش حساسه و یه سری شامپوهای خاص داره که ما همیشه می‌زنیم.
شب‌ها من یه دور پیاده‌روی می‌برمش و بعد هم شامشون رو خودم می‌دم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71659" target="_blank">📅 11:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71658">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=sn1lkwpd78EPY93SeqGxt_kgFKSdjTDhhmghJGc2se_GJV2aQYFl_hEjMMIk3BoB99TrZObwPbkbSaPzNOzEhRth79fVzRbLo5xlN-tahREGfedJWqzx_AN0OqlwSj_T8KV32rl1_RVJ_tRPaTWNBivUGNqV06UKJStfChYYH2DbuXT_Kzzdzk2D8ctSStLpK_XEe_HIrO1DxSQ8wBLoxybchLfKJUGODlvEEthxTbCUkA6JWVTW7eI6hCEy3Mq8X1KIOaPK4LwJp7_PdR1ENn0SjNuxkZ92tDUE5oW1dHBLh5n9jFjMy0u1JTIrzdDpbMiS5NnuWbImapScAdRDjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=sn1lkwpd78EPY93SeqGxt_kgFKSdjTDhhmghJGc2se_GJV2aQYFl_hEjMMIk3BoB99TrZObwPbkbSaPzNOzEhRth79fVzRbLo5xlN-tahREGfedJWqzx_AN0OqlwSj_T8KV32rl1_RVJ_tRPaTWNBivUGNqV06UKJStfChYYH2DbuXT_Kzzdzk2D8ctSStLpK_XEe_HIrO1DxSQ8wBLoxybchLfKJUGODlvEEthxTbCUkA6JWVTW7eI6hCEy3Mq8X1KIOaPK4LwJp7_PdR1ENn0SjNuxkZ92tDUE5oW1dHBLh5n9jFjMy0u1JTIrzdDpbMiS5NnuWbImapScAdRDjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب علیه روحانی در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71658" target="_blank">📅 11:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71657">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوباره آمار مبتلایان به کرونا تو کشور داره می‌ره بالا، خیلی مراقبت کنید
من خودمم دو روزه به شکل عجیبی گلو دردم
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71657" target="_blank">📅 10:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71656">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840407be05.mp4?token=UgeH0cYFDVoTAwfEHfsAxZT2zkdwGD7MC4uHaLlofTE8L6Mut_aoe8B6G_EVm2OvKPL01RlewV2CeSr1AYFOy8-u9jakrEGpnpaIv1dcTiHzcZLNclXKo4gfvV6HprvKoGiR4uWZvqyP98Il5H0r5k4kkpKa43xTL27E6WQuTbiKQvRm8RxRhiff6hqa4BILVylG6zhp3VX_tx-Wk59Qjp1wBVj-ZgxYCNaqE-rmndgsSzzHjA06hZRelFs8SEkmN3R7RQ05THPVOzEtINMOpWPJnTHjIl6JVJPeuQefpFWFpntUAV_MpvZGIh2y04Dre1YoLlSnl5fX14HO_rjH6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840407be05.mp4?token=UgeH0cYFDVoTAwfEHfsAxZT2zkdwGD7MC4uHaLlofTE8L6Mut_aoe8B6G_EVm2OvKPL01RlewV2CeSr1AYFOy8-u9jakrEGpnpaIv1dcTiHzcZLNclXKo4gfvV6HprvKoGiR4uWZvqyP98Il5H0r5k4kkpKa43xTL27E6WQuTbiKQvRm8RxRhiff6hqa4BILVylG6zhp3VX_tx-Wk59Qjp1wBVj-ZgxYCNaqE-rmndgsSzzHjA06hZRelFs8SEkmN3R7RQ05THPVOzEtINMOpWPJnTHjIl6JVJPeuQefpFWFpntUAV_MpvZGIh2y04Dre1YoLlSnl5fX14HO_rjH6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار شده 240 تومن؛
همون لحظه صداوسیما:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71656" target="_blank">📅 10:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71653">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=GbPxXHEQ9kZanTLLZt5Wpxx46TE8Ai_af7ijNBUoo2YWFm4hf92d46jqxJUR3rZ-QW3r5iK2o9tEbQvzoYZ2r3_pfx_BqnXIr1vaByrLu8b_YK0e5mZ8ZqBvRl3aJAgGEZXHKZLwHq3-qYEMWeExHeWJ4AyeECCkP7Ng-fp7wBlGOApsUTlAfSU7E7Ba87wrKWyLvbFnDhvKc_nNC5RZzsT-JsZj03MnXWzTo4gTJXaVaFO4tTKKVWH98A0asj_lGJfXIaq6VyDi26BkEYT4Y_WOsLIUpKJC1Pu-DJ-4ljwqjlb6b96qZbowvhhA_hqvwMQvRkj4KHnEhIxRQVKLM5xSOGZHsjr1ywzhPOpO4KJGo99LnNtXSmNGFwGbZSaKcae2p_Xgs4vJwWIpqfzB86BS6gxLQnlE2JdmoV4YDnZBRCYnrw9iGoQwGiKLtafZihVuCL9ld0tusReOfEOKXN7Dhe9Zr4Bp8lQgpyXPlpV9TyHqRmL3LWzUnIY26Jydunm7rCEy9xBCKKMXcbJ7OsC3o2OqmVy6DN5qOeeiHf-A8g_sV-wiIQMzlOYEqjJPzEJBXhxfoY-YWuUm0pqGaPtnZtxgHRh-ECsUjtT1d-bbNnIXtvpRSob1p1Scwj-MLyBbEhR63_vzPaOXeL6q2scNMspuzLm4xfcUPm3svmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=GbPxXHEQ9kZanTLLZt5Wpxx46TE8Ai_af7ijNBUoo2YWFm4hf92d46jqxJUR3rZ-QW3r5iK2o9tEbQvzoYZ2r3_pfx_BqnXIr1vaByrLu8b_YK0e5mZ8ZqBvRl3aJAgGEZXHKZLwHq3-qYEMWeExHeWJ4AyeECCkP7Ng-fp7wBlGOApsUTlAfSU7E7Ba87wrKWyLvbFnDhvKc_nNC5RZzsT-JsZj03MnXWzTo4gTJXaVaFO4tTKKVWH98A0asj_lGJfXIaq6VyDi26BkEYT4Y_WOsLIUpKJC1Pu-DJ-4ljwqjlb6b96qZbowvhhA_hqvwMQvRkj4KHnEhIxRQVKLM5xSOGZHsjr1ywzhPOpO4KJGo99LnNtXSmNGFwGbZSaKcae2p_Xgs4vJwWIpqfzB86BS6gxLQnlE2JdmoV4YDnZBRCYnrw9iGoQwGiKLtafZihVuCL9ld0tusReOfEOKXN7Dhe9Zr4Bp8lQgpyXPlpV9TyHqRmL3LWzUnIY26Jydunm7rCEy9xBCKKMXcbJ7OsC3o2OqmVy6DN5qOeeiHf-A8g_sV-wiIQMzlOYEqjJPzEJBXhxfoY-YWuUm0pqGaPtnZtxgHRh-ECsUjtT1d-bbNnIXtvpRSob1p1Scwj-MLyBbEhR63_vzPaOXeL6q2scNMspuzLm4xfcUPm3svmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوهای این خانم معلم برزیلی مهربان و زحمتکش بخاطر سبک خاص تدریسش حسابی وایرال شده:
تو یکی از ویدیوهاش که حسابی هم وایرال شده به یه دانش آموز فوت فتیشش که درسشو خوب بلد بوده به عنوان جایزه اجازه داده پاهاشو لیس بزنه…
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71653" target="_blank">📅 10:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71652">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=McF9-Hv0Zh3aFjpvj2UMawlehJaoED6YiPdr35B_8fp5q0MSgJTfdVxhB6uHEdCLm-6OehErb5LxMDbKNOfENrp4nJA-fwGvYhiMQRwVmj1UT18XpCGQhZl9WIaOmqDv6NnderLufbnrId3tMg4xBhsWY2Vs_JE2I9AVh11afAkT1tJ3T5SY2Xd7h1yM-SzteJOTGjksN_88U23fNzyP13VFOCkPZj678FNurlRhJ9Fupwjl4Et539DNlJbuGRduzKm_LQdyGZOBEoZ6jC0dICG8eyN3CKrVwGxa6DRv5Y2EcOnqXBxN16xvSuMiHRNT7cWhgeCzSsaoWAK1M-Rdzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=McF9-Hv0Zh3aFjpvj2UMawlehJaoED6YiPdr35B_8fp5q0MSgJTfdVxhB6uHEdCLm-6OehErb5LxMDbKNOfENrp4nJA-fwGvYhiMQRwVmj1UT18XpCGQhZl9WIaOmqDv6NnderLufbnrId3tMg4xBhsWY2Vs_JE2I9AVh11afAkT1tJ3T5SY2Xd7h1yM-SzteJOTGjksN_88U23fNzyP13VFOCkPZj678FNurlRhJ9Fupwjl4Et539DNlJbuGRduzKm_LQdyGZOBEoZ6jC0dICG8eyN3CKrVwGxa6DRv5Y2EcOnqXBxN16xvSuMiHRNT7cWhgeCzSsaoWAK1M-Rdzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش‌چشم، کارشناس صداوسیما:
در عرض ۴ ماه موشکی ساختیم که هنوز اندیشکده‌ها و رسانه‌های غربی موندن که سیستمش چیه. موشکی که بدون نیاز به ماهواره، ناو در حال حرکت رو پیدا میکنه و دنبالش میره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71652" target="_blank">📅 09:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71651">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168229fd60.mp4?token=qHj3hDhfe0XAvK3bwohsoPhD9iQFRfK8hGg88b3vfG33Tq-tbb9zkPMhvnIghlLwcmmwAz_Pg9hogaZradKmJZ2G5d2_ekHeHzyya019lnUcgYyC0HoTp3njv7OXW_nUDqp88OymdxWfOFFmNSmdxqK5E1Yg8M88u9Nng2LLj90ZB7ZwBG5yfpJiJiGQ72-w4JqWpuHZGl5chsgylKxwSQZS_CjCJJYjCpFC-yI0itqEgq-yxiMJihHrjk58HgQmZw0OjOxY2wWRM3dL9BQGMxrSRe9zDvQbY2zBti9jjqmMeBUbftdA8JWAlYqu8MvkhOtUoL7ahG8DusvjwfUBUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168229fd60.mp4?token=qHj3hDhfe0XAvK3bwohsoPhD9iQFRfK8hGg88b3vfG33Tq-tbb9zkPMhvnIghlLwcmmwAz_Pg9hogaZradKmJZ2G5d2_ekHeHzyya019lnUcgYyC0HoTp3njv7OXW_nUDqp88OymdxWfOFFmNSmdxqK5E1Yg8M88u9Nng2LLj90ZB7ZwBG5yfpJiJiGQ72-w4JqWpuHZGl5chsgylKxwSQZS_CjCJJYjCpFC-yI0itqEgq-yxiMJihHrjk58HgQmZw0OjOxY2wWRM3dL9BQGMxrSRe9zDvQbY2zBti9jjqmMeBUbftdA8JWAlYqu8MvkhOtUoL7ahG8DusvjwfUBUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواب رییس کمیسیون امنیت ملی به روحانی:
اون روزایی که تصمیمات غلط میگرفتن اون زمان دنبال رفراندوم نبودن بلکه دنبال حاشیه بودن
اکثریت مجلس خواستار برخورد قانونی با روحانی هستیم و این تقاضا رو ارسال کردیم
قرار نیست یکی تو گذشته مقامی داشته الان از عدل الهی و کشوری مصونیت داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71651" target="_blank">📅 09:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71648">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=ZstwtEBPnV-1Yv1BIkHq4VW-L4UFOlTN_-gwCOdsqeLP06TqNJM7Ksc1EjkbOTDHvu3WUiDxhqhbZHhZqcwnzTaIQXUAkarFzATK1BRI2M08rKvHXoviTdBMyLxXsiTHnp_zRqdE2EvXfWxCQZ3jWWHE1ygOATax9pk2MGe1KP1TDKI37HHbfw5-6LhfXnt89ya1_MjhKPT3NdIVeftss1HdJnr5T1Ulv1pubV5JBgJzQUAcZRggz35syapnK3yTgxwLlxPLCgUQgEqM8i-mOuOuK7dSMtwWcrjZ_5-oE91uLZoVBtiGD8kYjGv-mmdjvUY_suPDN8mTl1LfS5MchQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=ZstwtEBPnV-1Yv1BIkHq4VW-L4UFOlTN_-gwCOdsqeLP06TqNJM7Ksc1EjkbOTDHvu3WUiDxhqhbZHhZqcwnzTaIQXUAkarFzATK1BRI2M08rKvHXoviTdBMyLxXsiTHnp_zRqdE2EvXfWxCQZ3jWWHE1ygOATax9pk2MGe1KP1TDKI37HHbfw5-6LhfXnt89ya1_MjhKPT3NdIVeftss1HdJnr5T1Ulv1pubV5JBgJzQUAcZRggz35syapnK3yTgxwLlxPLCgUQgEqM8i-mOuOuK7dSMtwWcrjZ_5-oE91uLZoVBtiGD8kYjGv-mmdjvUY_suPDN8mTl1LfS5MchQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل یک عملیات ترور علیه یک فرمانده حماس در غزه انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71648" target="_blank">📅 00:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71647">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm9KgPJdD5eMfh-AFy9uBwdHwU3vXapPax63cRdQZ0XKh16rBj6UOUofMGI5DQLNR0-tP2AgnA74rNU8hL9HlXZeHssxBDJ3Nz-YZzncRuy1opUdlrdw3YHQYKQhrgvwtDsjEbDzDgD844OnwdWbS5JPCxScf4uWct-11pzWa8jBAtIyZhZrnQfKvGH7OSN8FWnbu-StbvOL-MF2cef0M409oNgzDIEuPEmCpokGdyA4ihCAjWeoRyThyH23UyZQwDckmFIha0Xe8gP_ymk0J6hWkoLixCVB_oZ0TuK6bNDJUu_UTjfJC54EiO3XWHh_V4xyXXv84yp62-WIIUruSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
با سیگنال‌های متناقض رئیس‌جمهور آمریکا حواستان پرت نشود؛ از «مذاکره نمی‌کنیم» تا «برای گفت‌وگو آماده‌ایم». معادلات مربوط به نفت و تنگه‌ها تغییر کرده است. دست و پا زدن برای کنترل تبعات، جلوی آنچه در‌راه است را نخواهد گرفت.
تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71647" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71646">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس.
تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71646" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71645">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o82NY5mmiH5jJQrGPMjhWu3DC9bcmfVVA5oGusK2gFR6cp5OsEmjGALYrRbanNe8Tovey4188CZvJf033ZgeDvRuchUaO9Cu0PpMzk1wfM1jcPdjwsYSe5ytFHlLldyN1EQ393KutloLJn51SDPFnG37fFyE2VWu915BNi6K7r7VjbE37dtUMxFR-BdfxgUfpPtNhulgWffGhLveYw95ZXiCqXMsYakoGhSZQBp4-gxcJTOcW7G0-OsyVWlqi7tETR_JzvWHb88uJ3bErYkX8JyFa3DQ_fnl4MNnGxCF6CZFnlKmcSGu-wUg_KXHj08dsMlNmE7xNC9xrmm1p_2Iuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
ماه گذشته، نفتکش «ال‌گایا» با پرچم پاناما هدف اصابت موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، در حالی که این کشتی در آب‌های ساحلی عمان لنگر انداخته بود، ایران بار دیگر با استفاده از پهپاد به آن حمله کرد.
این نفتکش هم‌اکنون توسط یکی از شرکای منطقه‌ای در حال یدک‌کشی است. ادعای کذب سپاه پاسداران، نمونه‌ای دیگر از دروغ‌پردازی‌ها و تلاش‌های این نهاد برای ارعاب و ایجاد مانع در مسیر تردد کشتی‌های تجاری در این تنگه(هرمز) است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71645" target="_blank">📅 23:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71644">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیروز در بروجرد گروهی از معتادا در اعتراض به شرایط بد کمپ از اونجا فرار کردن و با این کار انعطاف و آمادگی بدنی بالای خودشونو نشون دادن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71644" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71643">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71643" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71642">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71642" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71641">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hd8m0B821gpEZwGnwAmyqgavCJMMRWhIPUBB37g4H0jkDU2Tm3lJ7p3nlHQbXtRUShTR4Wg1OwsAVRGxxV7pLvmk449_wvK5_T6pA4xqZvmXK0wcL1yzyoOizQBfMORqXvOcp7Z9i3HGLSdBxf3YZIZ7soCWp4ponyJRdNNuAdr20m9K6zsKUGeR8PkqhJt0ZhmLU3XlcUsCebfFXOtxILA5gedvTWNllITll-Skb4YGnqpAiyzjdkDwBzn_d_kdPMQq-fGyBMOnA5Mcga688pM-yI-1u9-xumMxBVh-hE331mMLMcL0ja4VPMUkdpoXC6ZAGAP68vFVy3uqTaqZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
نفت‌کش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در جنوب تنگه هرمز، با یک مین دریایی برخورد کرده است.
تلاش‌ها برای مهار آتش بی‌نتیجه ماند و تمام بدنه نفت‌کش در شعله‌های آتش می‌سوزد.
سپاه پاسداران اعلام کرد که پیش‌تر درباره خطرات این مسیر غیرقانونی هشدار داده بود و تأکید کرد که تنگه هرمز «همچنان بسته و تحت کنترل هوشمند ماست.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71641" target="_blank">📅 22:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71640">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d776b60914.mp4?token=WPSkKQs3QD0Cm4mMqpDonSYWAVTlfH7aBGEgZRnfmOY0Y8znBPSU3g8APoyz5d34VKMZdKANQdCliPA7mScOsCrJZkQgsISiSonvbshCvmiy3jHcr6rIsyQOOAY_hCbucvhs_ghVaY9Zy6nu8Un-S50b-KvXjCXKo1XNkGBdPOpEcsx2WdQiNf6h8dSYbP6LYgh9ZzMO5JdBTydw3ZM0LPIOVKqP9Bqkb5tMfymPKzZ2cjF1bEXPS0cvHFeI_o5VwQfhTVoNvhwhN7P2tFym6N_8SMrd7sdttbQpC-GudyURsjoDrkBJ1Dg1xOfr3nTKv6gprGTJnq2e5rpskXoluA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d776b60914.mp4?token=WPSkKQs3QD0Cm4mMqpDonSYWAVTlfH7aBGEgZRnfmOY0Y8znBPSU3g8APoyz5d34VKMZdKANQdCliPA7mScOsCrJZkQgsISiSonvbshCvmiy3jHcr6rIsyQOOAY_hCbucvhs_ghVaY9Zy6nu8Un-S50b-KvXjCXKo1XNkGBdPOpEcsx2WdQiNf6h8dSYbP6LYgh9ZzMO5JdBTydw3ZM0LPIOVKqP9Bqkb5tMfymPKzZ2cjF1bEXPS0cvHFeI_o5VwQfhTVoNvhwhN7P2tFym6N_8SMrd7sdttbQpC-GudyURsjoDrkBJ1Dg1xOfr3nTKv6gprGTJnq2e5rpskXoluA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره سرگرمی های روزمره :
سودوکو بازی نکنید اعدادی که کنار هم قرار میگیرن یه رمزه یه چیز نهفته رو آزاد میکنه
فضای سیاه سفید تخته و شطرنج هم شدیدا جذب کننده اجنه هستش
🎙
مجری:
اونوقت بگو هیچی بازی نکنیم دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71640" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71636">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DIMjzEtL3v66iFdznEenEf3WL56SxKy-khlFtecyn51Mryt92nPMkfGnMOZdLzhWkWK55UULvNdvhCyyFy_VYcrjXElqlIWvzWy3QHQ-Y0kwVN2dJuwvqSafi8jjLoO8WqepTVePV97tQrAHvE09ZNRwJVBZOrInwaJd1v8QSnzIDyUDXeLUrV1gJEKtlRJtK0g-lCpLfNYunLwWFpbbR9-v8Jf8gJBmIyaD3vz8Kf6UgZlAGUz6Itj55OjDGFeIYw1iU3pLAV8eWryf-lqGPY6yow8xRMaTi7oqWbEGVFhpLqesAKaTyVW6_30B-wUEh17q2ruKIFG4cX2ZVN8_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hTOHx3s-c9UwP4IKeUJAQleXSkhXZf7LAopZjuhkySeeflLut166VvjH2ykHDdxxtjjsDxz2OiKPviOUsIki6DQsBH1UiUDtdB4ulGgbYg8EBrGcG6tm1eKrAd9HkK1E-_SQOZNUskeJQiikZF5qpMb_XrEEj00q11yR-aSA8HOmzDx508Ra1H21b_t2NTBU7EvTS7VpTYG1T64wTvHh0XRwXaEENC69_9obKCdfofF5vo2-yn0nuJXKklCN7omcdxMMRYhNDUKqIHDsIBwI7DLiJ63eXFxubTMqEP8MxkidSjBPTKQ4OIKf_q9EF_RSGhjm_aaGjT8ktC0g5H5-sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیامکی که داره برای مردم ارسال میشه، از فردا رسما جانفداها برای شرکت در دوره‌های نظامی و امدادی، اعزام میشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71636" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71635">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9266483.mp4?token=Dk5vTlHxvPRRWHoh6pAYdrkZkF_PlMW8e3VC6Mo_QQ4898spNfAzdO4Iv8EzK6MYwp3FBk-Q0mt9iO0bWiVoaKI63b6tcEjRSug-QOQhiI4NsQMafvWlmFSiMjt1xl000lmMQQkudsdsC-LmN2xK0LGmLD0WY5AqY1LE2sp0rSS5fH1a5DRzs86Lu-EMoB3Q7w05Ywh1ABsh5p0jfLsVLAMpz6wb7ZvP14MAsztEktQe79OhXTaAk1heCtWgPlSoqeY1lVOKL1XI_ACghZMokZUwLSPneGTYRwz23trdX25mfvtQUSnclQntakqpa8AjFCBXi94Fb7HfIaSe8gaAXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9266483.mp4?token=Dk5vTlHxvPRRWHoh6pAYdrkZkF_PlMW8e3VC6Mo_QQ4898spNfAzdO4Iv8EzK6MYwp3FBk-Q0mt9iO0bWiVoaKI63b6tcEjRSug-QOQhiI4NsQMafvWlmFSiMjt1xl000lmMQQkudsdsC-LmN2xK0LGmLD0WY5AqY1LE2sp0rSS5fH1a5DRzs86Lu-EMoB3Q7w05Ywh1ABsh5p0jfLsVLAMpz6wb7ZvP14MAsztEktQe79OhXTaAk1heCtWgPlSoqeY1lVOKL1XI_ACghZMokZUwLSPneGTYRwz23trdX25mfvtQUSnclQntakqpa8AjFCBXi94Fb7HfIaSe8gaAXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
سیاست ما روشن است: ما به نابودی زیرساخت‌های تروریستی در «منطقه امنیتی» لبنان و رفع هرگونه تهدید علیه دولت اسرائیل ادامه خواهیم داد.
به دشمنانمان می‌گویم: اگر تا به حال درس نگرفته‌اید و تصمیم دارید دوباره به ما حمله کنید، ضربات سنگین‌تری متحمل خواهید شد.
هنوز کارهای ناتمامی باقی مانده است و به یاری خداوند، آن‌ها را به سرانجام خواهیم رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71635" target="_blank">📅 22:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71634">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ogv92PZ65J5oBkCOxBnvKkYAppD0tk4HD9HSXIrInu1FnjTQGm7OL7uihGC2gCpuLU7sUTe93fjc0ZqQ5ww5Mq1Bj2YcWPRP7LEXwsLl6DS6nNqafN4WCZtYuwIFmIu6wEBLKbx5aFG4f-HjdxUY45henu3WehKzvawnhYIAKx4Z4Dk791BwlVk-KTLDXuZo_GigHF4kAiiTYCU62NdNmNTNdFAUtNsvHXT2PKwUDMIO21o-tSiOhqkpPl6tshdlRVreZcmFDS6RZ4caPfr6kGI51_W1gj9yBRh32sMDwpCPLK8dQS5OsyuJrnw2gcf2qx8zsFdJUJTE_-ctxJhDgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری «عملیات طرد اقتصادی» (Operation Economic Outcast) را با هدف قطع تمامی شریان‌های حیاتی مالی رژیم ایران و حامیان آن آغاز کرده است. به همین دلیل، من فراخوان جدیدی صادر کردم تا افشاگران اطلاعات خود را درباره کسانی که اقدامات تروریستی ایران را تسهیل می‌کنند، ارائه دهند.
خطاب به هر کسی در سراسر جهان که اطلاعاتی درباره این شریان‌های مالی دارد: این فرصت شماست. اگر اطلاعاتی قابل‌استفاده برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت پاداش باشید؛ فارغ از اینکه کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند. اگر چیزی دیدید، اطلاع دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71634" target="_blank">📅 21:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71633">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mV01is54P8hAgW7iPxEDstBTMf6Fdd82XAfeuofu53JudON7nqeiXLXgCl5BMe_BTLecWMxabkWytCpK2mHhlJSzrZsvK8qz_LCedbEqIMFtGbQpL222OInX2yho2vxdWZ_xjm900uySsXkvOZeQvRVJxSZ0iJWxsa2WqbyK8m_Ou1w8qv59CcANvYFb60SisjB8jJQxaWUj5OGUICiVLOCEGLdhtNYa5nkBMu3-fDJhH5Siicf9otW9H7J-2tXMciDtdwX4T7jPeTyE_HMKf2FEDjUKdGKJFs2xMPVgiBaWk04J8AyASmGxdPASEnVGT6uWwnGs6_pJCecMDLvCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
نفت در حال عبور از تنگه هرمز است.
کشورهای جهان — که هیچ‌گونه کمکی به ما نکرده‌اند — باید پس از پایان یافتن این غائله و فتنه‌انگیزیِ ساختگی، هزینه‌های ایالات متحده آمریکا را جبران کنند؛ و قطعاً چنین خواهند کرد.
ما این کار را بسیار بیشتر به خاطر دیگران انجام می‌دهیم تا به خاطر خودمان، و نسل‌هاست که چنین رویه‌ای داشته‌ایم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71633" target="_blank">📅 20:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71632">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8ExI7xsGbw8LcRCzWjyEdUi-brXuVjkTZ8xWA6nGL1utMsnGPFJB91S811kC-AkEXU5PLSgaxggafKcEYH7UpS5NmmKVtXeROURIyQLrPhP8QMhTqxo4turH-rd0c-abFb7OmmhGuNdXRTW-beRQHQgxhT1J9xhFpnoqtsoe-LXhUKrgRYiIaJmf-8O3uju5KpZHlSls-_yTyfrZ_SWWIN5o7l_bFHxbEMFLnOY0oRg67F4HQi8qRJ2qn1nO0Q-3cqkbXTi4O-7MxzOtUxknw9MoKf73pXFdNON7Q3ErYQeaO3aTgQT3e2odCSho4yAoU-RmVAd1riSEH8YRHrVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
امیدوارم همه متوجه باشند که افزایش قیمت‌ها در سراسر آمریکا ناشی از عملکرد «جو بایدنِ خواب‌آلود» و دولت او بوده است، نه «ترامپ».
حتی قیمت نفت در دوران بایدن بالاتر از سطح فعلی بود، حال آنکه ما مانع از دستیابی ایران به سلاح هسته‌ای شده بودیم!
به‌جز نفت که فعلاً وضعیتی متفاوت دارد، قیمت‌ها به‌شدت در حال کاهش هستند؛ قیمت نفت نیز به‌محض پایان یافتن درگیری نظامی با ایران — که زمان زیادی هم تا آن نمانده — به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71632" target="_blank">📅 20:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71631">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIhWOBV61OMs2yLiFLBdqmy2lbMhBNAAGoblD_ME78fUuiUPExB7J4HwbLQfS8NX7fTOJ_rXEiGq8M67xfupvcb4CRFadoXTHBwPFzWKQ7-m_Lfl2tKDAJpgT1X243pT7who7mQ_1jhnuNJNpcCkUrlteAPv-DXM9DruLUZ7OUxK1Rhc2vS8aFMf_K82-myzMfV9MPRsIZE6tGeM4bE8r2iKuoX5MZl88FpMfA8s31EPDLhCu6D0CPfkxbikQ_3cy0PWYRyDuS0yyYz0Z1YA-QuICthlEtmc5rmV0W3W2ydb3saRKNZdMCC76Z9yy7GnEFufwVKNPjUqQRWSh-Xg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
من به تازگی گزارشی دریافت کرده‌ام مبنی بر اینکه ایالات متحده بیش از هر زمان دیگری در تاریخ خود، سلاح‌های نفیس و ویژه تولید می‌کند.
این سلاح‌ها روزانه به نیروهای ما در خاورمیانه و فراتر از آن تحویل داده می‌شوند. کارخانه‌های شرکت دفاعی ما به صورت شبانه‌روزی در حال فعالیت هستند و همزمان به طور متوسط هر کدام ۴ تا ۵ کارخانه جدید در مقیاس بزرگ می‌سازند!
تمرکز اصلی این تولید بر روی پاتریوت‌ها، سیستم‌های THAAD، تاماهاوک‌ها و سایر سیستم‌های موشکی استاندارد بوده است که ما در حال حاضر تعداد زیادی از آنها را در انبار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71631" target="_blank">📅 20:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71630">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
تسنیم:
ایران بارها اعلام کرده است که به دنبال مذاکره برای رسیدن به توافقی با دولت ایالات متحده نیست.
ترامپ همچنان ادعاهای نادرستی درباره توافقی با ایران مطرح می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71630" target="_blank">📅 19:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71629">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  «ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد. این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71629" target="_blank">📅 19:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71628">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXk3B9m8S3WMTdchgVBfnJRDdX2doBlqbAoBDHkUzqVr-AcvG76914T5K3CbqLc-jYBE8sBZNEOxmSR-wFnPY1wCeIYDIPgPPETOrQ-lM_J13a4z9B8VAliweaN2GzxpC7h9mFKcWTsl8eVh47oG9SPEUs8hvu1kYnISM91FAQBF_8I-o7qqBlq8aOuwnIH59f7L51uahh77MiNZt_6raxQxMqCkhOAFRGvScA1OR9fGc4rrlqJMM2KHvs2Fc486s7oleFQAlwPRhU2H_e12i22R2vnKHoWy28HKhgMqJLfVrGZybPjFx-AF7ueiQhzC9OubgN3oUdzKGpFrfyDZ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
«ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد.
این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71628" target="_blank">📅 19:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71627">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=Xnpkstl6rcvhfIpoX5tAVCwiM6OdB1ZZZGJ_hOfNVFCWofSdneJ6Tzi3z7Kv37FU_0HLHEIwWjXVY2ZMB7fqJTHe25Jc6Mq4pCqkt2UlxoiSTZYy0g2bW3yvj7n-c9zaTr_Odg6ZjbKQMHDwM9ixAYVm4wx9pUrXWBsLxCwFpoVKtSQF9rRhidReusoMrUvCyRnhPfDjuIjfIEl566Tx0LAGuCtXNXTNqsQxBYXBU6XmSwquoWO-rJNp627nXgtbWMq_kbwt4zIQouKPdN61VrL38v0hMQD4Yn55lebKz84ZXfTPIT5PU3m6h_rxNMVOlLOQAVS4eOIGQSO52sLPsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=Xnpkstl6rcvhfIpoX5tAVCwiM6OdB1ZZZGJ_hOfNVFCWofSdneJ6Tzi3z7Kv37FU_0HLHEIwWjXVY2ZMB7fqJTHe25Jc6Mq4pCqkt2UlxoiSTZYy0g2bW3yvj7n-c9zaTr_Odg6ZjbKQMHDwM9ixAYVm4wx9pUrXWBsLxCwFpoVKtSQF9rRhidReusoMrUvCyRnhPfDjuIjfIEl566Tx0LAGuCtXNXTNqsQxBYXBU6XmSwquoWO-rJNp627nXgtbWMq_kbwt4zIQouKPdN61VrL38v0hMQD4Yn55lebKz84ZXfTPIT5PU3m6h_rxNMVOlLOQAVS4eOIGQSO52sLPsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ رفته ایرلند و چپای ایرلند هم برای اعتراض این حرکتو زدن؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71627" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71626">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71626" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71626" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71625">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNFOetw4DTMe8DY7HFq4fsKBtn0XhtNU6m2axIac_w-_EFgCYmbjMLCs3cMojgZAa8F8B5fmmBO4fKUcAANwLVHPEs8vHIa6Qtc1rwaq00CH_z9YGPUr6MDZ8ympL4gN_jLVzff35O1qTjlHl3grj5t1cEeyOBcik1S9O18Z37lBullyZaT93g_M9OSvcfag03ftmoq5DmcGpvozcGbHp3W1guoqOjosZusHPL1qawMkSVxouCIDfkLpUy87maSP2idbuQmZ13GHAGb5hpQYZT_ISAUqrOntVIMfEm5ypOkOjbkN3l-jniTMiUuSEKyLGwuU2sRADmWGCNBkfuOw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شب بزرگ فوتبال آسیا !
نبرد هیجان انگیز
⚽️
السد
🆚
استقلال
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل دو تیم باهم:
⚽️
السد: ۲ برد، ۳ تساوی و ۱۰ گل زده
⚽️
استقلال: ۳ تساوی، ۲ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71625" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcIo_dngMRmk-l8oKBDjC43QUQoV6hPNmPVfpKG7nLwdIZbHpgOKcknKDJBacD7HmjF79kOk3LQZ9C28CWT0hdXHnPtgcTyvLxz8nrPr-4gGvuOnFkfo_xGuWWAmJ0-rtEnx2bdf6v4iAASZmJ9HsgpJ0V9Nje6Tng2oFfD6G6sc9lmzyADeVHJyK2Ev3-8HuJpOcwiGdCO6kqTdbsmSkz9wxalu__WE9FH--x99G_6tQE5XhlwReOc7GN8mdPd2cbIaMSgwmj72dyIDuhv0YpuMQ7dR53i020WDZF-FyF7ZaYHVSVfppc-JVZPWFcZrzv72Xafeog8jhCVfyhoM7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
اوکراین موافقت کرده است که به تأسیسات انرژی روسیه حمله نکند؛ روسیه نیز متعهد شده است که همین کار را انجام دهد!
افزایش قیمت جهانی گازوئیل عمدتاً ناشی از جنگ روسیه و اوکراین است، نه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71624" target="_blank">📅 18:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
دقایقی پیش چندین انفجار سنگین در چابهار سیستان و بلوچستان رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71623" target="_blank">📅 18:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
ویدیویی از عملیات نجات افسر تسلیحات ملقب به "براوو Bravo"(زیرنویس فارسی)
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71622" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObRucqzE_CXy9GQErTkaEm2A-GQfpJ2HT9wSBbnczKUH92i94ysnP01iMpuXZy29ve06cCWZgPVi2uQxFlz8ZFzFHthfrhTg0qghYulhs94_2d71CDrbun7RtQKB9jxnUWz2VfC2F2DnireSxUp3IAdIgD3pOegBq9CrdHWLZJ7QSybEk4VuhGFFMJD4lbuPa78qunEgq9_OxFM1ZUT_z-kovZmO8QtiuSjEJL_XyUTH4GAVKQ8xoQYYxp4FDNp7a6lBAgm7Vl4a_S9X4kiwzdW8I8pI_Mk4q9Gxlp72xedrFRYcDXKi86XxmNKnSy2POBsLXOzd9Qhvl0t1XNUpiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو هفته آینده برای سخنرانی در مجمع عمومی سازمان ملل در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71621" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71620">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=oGhDpOEy1Om1IqVQR1J5itDp6vHuCjwAj6bvfLr6aJeDPZZXhg82lkPOYyt-XLdaOgsTOBy_ztq-_lgHf7AXZdd8hWsm6vk5uWolBSTRxGEDtZHVWn5k8ws3oGlgJO_qkEizohcsie8gdZlUTdzmEZ1rxBJ_yDLDBvOoa21sPk1eGBXy4IrWAIPDz-dDb0GMhFq9dyoBu3bf4EYkk6ViWTli3NGc-UbfKGQquzVzngcfponE27TTlCy-ZLSvSyfwr3bbeAojdUr_E3AjMnWgWS5ZXP3FTF8LnLlfSN90tRRq7ZCuUVezjb93yoa4_khHFPQAV8BdFVXxpDCJWT_I2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=oGhDpOEy1Om1IqVQR1J5itDp6vHuCjwAj6bvfLr6aJeDPZZXhg82lkPOYyt-XLdaOgsTOBy_ztq-_lgHf7AXZdd8hWsm6vk5uWolBSTRxGEDtZHVWn5k8ws3oGlgJO_qkEizohcsie8gdZlUTdzmEZ1rxBJ_yDLDBvOoa21sPk1eGBXy4IrWAIPDz-dDb0GMhFq9dyoBu3bf4EYkk6ViWTli3NGc-UbfKGQquzVzngcfponE27TTlCy-ZLSvSyfwr3bbeAojdUr_E3AjMnWgWS5ZXP3FTF8LnLlfSN90tRRq7ZCuUVezjb93yoa4_khHFPQAV8BdFVXxpDCJWT_I2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک پهپاد روسی «گران» (Geran) در بخشی از جاده در شهر «پاولوگراد» که مملو از خودروهای غیرنظامیان بود، سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71620" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71619">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=XF1vYrUNFEuFX-URFXbeIYzixPsw-iuIafQiSOSH1omKys3aZlEnzeoHueNNbfcXcNrcwLV4YUgegJtGRl8vzwCpKaZkBJ_xBxKwmulBwap1kUyH5JQevnpj5cM65guj_fhdLb2YOVrt6YKsOPEi56pjllYOus5MsAtL7LzQ85bm1GiXvZMk370aOApM6qPx0VF-GhlmZJiat_UjBXXvESo61ijhmi_fCi02smv-TnCvOt6wgM7ZiouV8gevGi9iDXiC_Dq2-N2KcgY53TwN0v-OwVPwjgAgVFdh2OYZaZu0id7_2c9yUAYd5Zv0he1V5ENe5zYsHcIocUHxOGlg-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=XF1vYrUNFEuFX-URFXbeIYzixPsw-iuIafQiSOSH1omKys3aZlEnzeoHueNNbfcXcNrcwLV4YUgegJtGRl8vzwCpKaZkBJ_xBxKwmulBwap1kUyH5JQevnpj5cM65guj_fhdLb2YOVrt6YKsOPEi56pjllYOus5MsAtL7LzQ85bm1GiXvZMk370aOApM6qPx0VF-GhlmZJiat_UjBXXvESo61ijhmi_fCi02smv-TnCvOt6wgM7ZiouV8gevGi9iDXiC_Dq2-N2KcgY53TwN0v-OwVPwjgAgVFdh2OYZaZu0id7_2c9yUAYd5Zv0he1V5ENe5zYsHcIocUHxOGlg-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگزاری این کنسرت خیابونی مختلط توی کیش باعث شده صدای طرفداران حکومت در بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71619" target="_blank">📅 16:35 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
