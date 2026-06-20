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
<img src="https://cdn4.telesco.pe/file/d-cUiAdVG8gbiGWccE0bJSFFvpHVbyMpaGQLu2YGkiCz4oPU6PRAivaeSLrEiuw7xWdvD9ook01zAo01luIMZSXF47XuhY-tzbBaNqseoNTH9w57mPqlGI7O4zqhs_O-3jkoXRTOW42ayCei8J_UEEv7Jdpkm_DfmJjfChYmA2LZC0Juok1cXNWcWuV9vMa4HpJjetQmFXHmLwntY_A0S-HbhIB9MNg9iVUNVT7Afbm-E-qpuTDFBP066RP5RdK7EGSAeuZHd7pdNgqzAM5HxLgOFePVtGamZf3y-ulOcw9tb3Ntngm0yj6l4F3514RbK4Sked9uyV87kO1eZdsbwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 01:30:28</div>
<hr>

<div class="tg-post" id="msg-15466">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
کانالی که ترور هنیه و نصرالله رو دقیق پیشبینی کرده بود، دلار ۱۶۰ تومنی رو هم دو ماه پیش اعلام کرده بود از تاریخ و نحوه حمله ایران به اسرائیل پرده برداشت!!!
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
🔴
LINK - CHANNEL
🔴</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/15466" target="_blank">📅 01:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15465">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حسین پاک، خبرنگار مستقر در لبنان: از ساعاتی قبل عملیات نظامی از سوی اسرائیل متوقف شده است.
@withyashar</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/withyashar/15465" target="_blank">📅 01:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15464">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بر اساس آخرین اخبار، ساعت قلعه نویی در مکزیک دزیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/withyashar/15464" target="_blank">📅 00:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15463">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a879665e8e.mp4?token=gjsKnJggl1hM-2QBNQybmS29eF51FtnrZHYIRh9ZWgnj_YlLtbkb9RLozdaR2OjpNX1SSq_CpxVnH8aylUiRNLv-HHen8f2Lta_OQzbjxpK2XUWvGreqPrdb9WFOOt5eeyEUXna18A0Gq9lsHlhrHKM5K7pW0Y-iJOGkuYz9Afu3pUPgWbE_D9D5XvvYYqLK_18e0Ctq_Jj-K-ICpHqxnKdjRlGUocwsaNOvNFCz7gg2SYJT36Y6LiYnog2TzQ7bSKoVw7WHOe11TvXCRGKEgCTFN0-6enZdfVW3PA3GQtIn0TphJEdm0aBfUCbCn-MTtTaNiOawyZjnWH4nNOqEpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a879665e8e.mp4?token=gjsKnJggl1hM-2QBNQybmS29eF51FtnrZHYIRh9ZWgnj_YlLtbkb9RLozdaR2OjpNX1SSq_CpxVnH8aylUiRNLv-HHen8f2Lta_OQzbjxpK2XUWvGreqPrdb9WFOOt5eeyEUXna18A0Gq9lsHlhrHKM5K7pW0Y-iJOGkuYz9Afu3pUPgWbE_D9D5XvvYYqLK_18e0Ctq_Jj-K-ICpHqxnKdjRlGUocwsaNOvNFCz7gg2SYJT36Y6LiYnog2TzQ7bSKoVw7WHOe11TvXCRGKEgCTFN0-6enZdfVW3PA3GQtIn0TphJEdm0aBfUCbCn-MTtTaNiOawyZjnWH4nNOqEpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️جی‌دی ونس :
«من مشتاقانه منتظر شروع مذاکرات فنی با ایرانی‌ها، پاکستانی‌ها و قطری‌ها هستم...»
@withyashar</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/withyashar/15463" target="_blank">📅 00:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15462">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سی‌ان‌ان: «ونس» از پایگاه هوایی مشترک اندروز، برای شرکت در مذاکرات با ایران راهی سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/15462" target="_blank">📅 00:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15461">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f0d58b03.mp4?token=eRRHjbGyRUpVbnEOZZlwwomgmDAp7xwmTAz90V_Zgf0sH11R0OglEH8US0ClFs0yBeH4v7ct0nrJkBLBW_Tml74t8rmB-le4c6-nbTUgd1FqOpnp-rSGEc1xQYVhyEoFZYsl62uNWHedtGjWvgeC3_p9r-tR1-gYD79xb3_r9ufFh_ctwUS7bW2cKDqQ0wBH1qMiml6AlZMQIFhHBRmxJrI0LyRVOBSJCb53b1Ipm6pD3MNNwIAC1kShSlcIDMERc9pMrsFdrUJNtLH9s28GUy51JlvqXQYxOIFJCfLu42kaeRCqTyC2kMXL_YtY8_h9NmXqC2DM3S7dMplXPAX7AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f0d58b03.mp4?token=eRRHjbGyRUpVbnEOZZlwwomgmDAp7xwmTAz90V_Zgf0sH11R0OglEH8US0ClFs0yBeH4v7ct0nrJkBLBW_Tml74t8rmB-le4c6-nbTUgd1FqOpnp-rSGEc1xQYVhyEoFZYsl62uNWHedtGjWvgeC3_p9r-tR1-gYD79xb3_r9ufFh_ctwUS7bW2cKDqQ0wBH1qMiml6AlZMQIFhHBRmxJrI0LyRVOBSJCb53b1Ipm6pD3MNNwIAC1kShSlcIDMERc9pMrsFdrUJNtLH9s28GUy51JlvqXQYxOIFJCfLu42kaeRCqTyC2kMXL_YtY8_h9NmXqC2DM3S7dMplXPAX7AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت مذاکره کننده ایران، با اسم میناب ۱۶۸، وارد زوریخ سوئیس شد.
ونس معاون ترامپ برای شرکت تو مذاکرات با ایران،راهی سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/15461" target="_blank">📅 00:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15460">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTiti</strong></div>
<div class="tg-text">سلام یاشار جان
باور کن محرم شده میرن بیرون الواطی برای همین  ری اکشنا اومده پایین
😐</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/15460" target="_blank">📅 00:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15459">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from۞۩ ¥𝕒z∂𝓐Ｎ۩ ⓪⓪:①②</strong></div>
<div class="tg-text">شیفت شبی آ فوتبال میبینن</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/15459" target="_blank">📅 00:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15458">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895fd89b8b.mp4?token=KQYAREHpOrj3Ny8LvsS7Pu3f46jd6-IU4RdikatZJvBlxBbB_IYTkkdBvaA_Ic1-QDQRLbQb53XaI3ebfNN8ltp5oJpIJoYonhdA-wbdFmLJdRcrsrk5hWEfIWznlwaANoVFKWlsbVDdVfKqwWvp1k9JwPXF4ik4-zkqcL-ObWZCYhjk-A97P_UPLiWtm6KDfeeQioVmgfP_ElF3rFFWj8PUP3vpdcEL96ugPtKjbJl5_4e_u3HgRgqYGLOWckCwZ_eDtNLViaZlJEmSOgoIpheJuZqw7YFTd-hf6TnrVC6waTVawOLwO2lWbpC-HoTJLuOYnwO-VX1KX1GT7j54ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895fd89b8b.mp4?token=KQYAREHpOrj3Ny8LvsS7Pu3f46jd6-IU4RdikatZJvBlxBbB_IYTkkdBvaA_Ic1-QDQRLbQb53XaI3ebfNN8ltp5oJpIJoYonhdA-wbdFmLJdRcrsrk5hWEfIWznlwaANoVFKWlsbVDdVfKqwWvp1k9JwPXF4ik4-zkqcL-ObWZCYhjk-A97P_UPLiWtm6KDfeeQioVmgfP_ElF3rFFWj8PUP3vpdcEL96ugPtKjbJl5_4e_u3HgRgqYGLOWckCwZ_eDtNLViaZlJEmSOgoIpheJuZqw7YFTd-hf6TnrVC6waTVawOLwO2lWbpC-HoTJLuOYnwO-VX1KX1GT7j54ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن همای سعادت در ارتفاع پنج هزار متری دماوند
@withyashar</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/15458" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15457">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/15457" target="_blank">📅 00:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15456">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بی‌بی‌سی‌: کیر استارمز نخست وزیر بریتانیا دوشنبه استعفا میده
@withyashar</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/15456" target="_blank">📅 23:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15455">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbHesoCu-tTxPsIk2LmkVgknVeLuOp8ap0GhZGR9646tNOxd2nzIb80UfrB_N9Z9-OM4YUNqUC8XFtgKbnLOPNGuOiXJV1I68n79FJClQlTLMc_ZqUpV8gHIUQgVtcq46lTPf4wcDjujt2PK0iVTNUP5W5xqgsmKWYgfizNdG4xx4PG09AkYdmGAdBQaMQGGOSllKnxeM9vMqvT8cnCD0sYfXzleIoQh-NzcabBuTHSZqnsh0r0Jb9Rd6vWbMltqvwRrGidl_36-v9e0-P-Jl2HLIpgjLjDuoCEQDWQ9lrYRU6SAXgbxBMw3rSd6xVhk9la4Nqn32Sdlkgu96ITdvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ..  ..
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/15455" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15454">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVGjCYki4lAyIPBKzdRwf4Ae8ds4vu3cjaWqRwO36Xrva8lyTh-zH4yFsYLGz5cBQvaDvWFOl28OJwDNVJ9UWZGDnm_NvI46ArzMCj4rGeBqafnO6DT1LAo5Fy8xqN3LAe1XKBz1yp2XBJvWFUQC3tFauYSP0J3ildu0qg0XLDy_d1u5-qJ9GQRWtpJ598yWBqcphwvPTwwLHwfNoQkCCit2ZUQw1LFPERivyIvoUYGLP5bVlpSvKon-o9pdHf5gdn4Bh0uibw4DLN29AK_sjOd1vttQLOMPerSuG3THf25kQ61kFkppMi5j-gycPFZNjew1-ew0EgYhWI22REECEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هیئت ایرانیش 15 دقیقه دیگر در زوریخ به زمین خواهد نشست. @withyashar</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/15454" target="_blank">📅 23:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15453">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آی‌۲۴ نیوز نوشت که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به وزرای کابینه این کشور دستور داده از حملات به دونالد ترامپ، رییس‌جمهوری آمریکا خودداری کنند، اما مقام‌های ارشد در محافل خصوصی می‌گویند واشینگتن درک درستی از ایدئولوژی جمهوری اسلامی و حزب‌الله ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/15453" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15452">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اتاق جنگ با یاشار : مشروعیت حتما تا انتها ببینید  ، کلیک کنید کارای اداری یادتون نره  https://www.instagram.com/reel/DZ0c0MCxXpl/?igsh=cTR0Nm90ajdrbWRh</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/15452" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15451">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">️خبرگزاری مشرق:
نبویان، نماینده مجلس، به ۲ـ۱۰ سال حبس محکوم می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/15451" target="_blank">📅 23:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15450">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ در‌تروث:  در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/15450" target="_blank">📅 23:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15449">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نایب‌رئیس شورای سیاسی حزب‌الله لبنان: تلاش‌های آمریکا و اسرائیل برای خلع سلاح حزب‌الله با شکست مواجه شده و تسلیم سلاح غیرممکن است
@withyashat</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/15449" target="_blank">📅 23:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15448">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هواپیمای هیئت ایرانیش 15 دقیقه دیگر در زوریخ به زمین خواهد نشست.
@withyashar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/15448" target="_blank">📅 23:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15447">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اتاق جنگ با یاشار : مشروعیت حتما تا انتها ببینید  ، کلیک کنید کارای اداری یادتون نره  https://www.instagram.com/reel/DZ0c0MCxXpl/?igsh=cTR0Nm90ajdrbWRh</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/15447" target="_blank">📅 23:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15446">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کاور
🔥
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/15446" target="_blank">📅 23:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxGC0iCAS7RV9pbcmZ6vz5AJUsVmsJLnG1PRF3I85GWbUz2F0h0bPu-BaIecf8rjxI5lXzckxJIobykVtH1-YK6W7fE7PQCA5BsHuGkkVYzdzuh07G0I0DVFVDXzrbGiTbFQEQNqisaanXb2uA45QUqKxNDHvhKjNoKC38coUYubcCJbT3UOdydhPk0TJVQ5Bmy-l4ssclU2rbl7tDyC35PC80ry5Y0ZBg7F6PvdekzhSh7QHsUOTAOIpnbSf_mh2QOGBoxCwT_n78MLPcDsWAi98OoqR1DuDEN6tQWVvvtwMwmb_WGjObPKSMUKGZMqqmyRT7RDwN1SAcvZ7iLugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌ها در گذشته، حال و آینده، اعمال شود.
از توجه شما به این موضوع متشکرم!!!
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/15445" target="_blank">📅 22:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xc723-qfekYp99KhoZrF60Mx6H4jiVw0534ur3sKXaGmNqoWWQi1cntawvBfQQClB3pFbyIfNpZ7FSbLILr1S9_KdDio3ZDyc2dGhPfkb2XvY5zF94sMwBuD-Q-_BQ6DdCeJjOPaimlMl3GqNpAPdaYmQlfWtnaUMkHSrxX3os9-AhBGeVqgxUOvxcyWp8_0Cs7zutFaCq_Ou4ll8gGerRBDPwRMpPGO_QJCD6-yafFLVGAIWiFK4q4Ifh7SUM8cndoGcvFLoT4FOF244cm41xDTpJOhkp9PVwfDIi_uL3LdE3bhY1_Dgc_kF8L3Hgvc23S-CtcxSl-BGQnLq1cXeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
🔥
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/15444" target="_blank">📅 22:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/15443" target="_blank">📅 22:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/15442" target="_blank">📅 22:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15441">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/15441" target="_blank">📅 22:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15440">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/15440" target="_blank">📅 21:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره گفت که ارتش اسرائیل به سنتکام اطلاع داده است که به واحدهای خود دستور داده است که به آتش‌بس در لبنان پایبند باشند
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/15439" target="_blank">📅 21:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15438">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhSa5x02TKU_eTReRvidJA-0YiPQ1AH4kIc7P8a7Bh2-hxOkN94-XDY_bi7a0q5zoAIyHU2jSrDnH_s1ykafFvt2iczPvbzb0TovFugcFN-V8gWaBIseC77nRlt6CzrKnwhYV_7MxYteM2Gr0Fw-KzOI-EFNWYDybhJx6zKM4gUjTOUW9F9GhINVp9BofYxFg6kjucVzCpcIqAqrHoref58nRWiY1iZMcQwK5l4Wnt00OBLaEMa30tdOw5slHXHzjPbJg0jJPKEapT1Ima9KkjY_1w5Uqj1S7vETJEdm3nxMhTXR9ibTsCcqze5JMDZMC9Wi8GMjI1Ncnn4ljcxsIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار وزیر کشور پاکستان با پزشکیان
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15438" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15437">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3cb82d210.mp4?token=C6WkE-yhBqz3nzWLaVYa8EA2EaR4kKdfbonr31AHnlWtKT-YOWyInOIiBOCAnA_zMhEwtas8OEZo-ZhNdQnc0SxXtfkOMxld-E3g1ngXg72uplBbPl_3ZgPk2dweDE6VMGDTsrYBax-UwOfQlVxTTJE3ub9qtRdW542KVqbc4brR_YQfrgALih5jJH1quqzyVeYYC0qiRbM8DiVlzySNk1x-uqitAbufa5CPEVKD9ktmhbJdipoAGoSM5m6EydrRI2CS2K0S8fdLJrvzHKuhM4zncGedbqFBSIIBfMFS6GUqG7JOMOBYT5VtWeXP-E0dzqt43uzHkXQqyqCBMkmq-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3cb82d210.mp4?token=C6WkE-yhBqz3nzWLaVYa8EA2EaR4kKdfbonr31AHnlWtKT-YOWyInOIiBOCAnA_zMhEwtas8OEZo-ZhNdQnc0SxXtfkOMxld-E3g1ngXg72uplBbPl_3ZgPk2dweDE6VMGDTsrYBax-UwOfQlVxTTJE3ub9qtRdW542KVqbc4brR_YQfrgALih5jJH1quqzyVeYYC0qiRbM8DiVlzySNk1x-uqitAbufa5CPEVKD9ktmhbJdipoAGoSM5m6EydrRI2CS2K0S8fdLJrvzHKuhM4zncGedbqFBSIIBfMFS6GUqG7JOMOBYT5VtWeXP-E0dzqt43uzHkXQqyqCBMkmq-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قمیشی : به عمویم سیاوش قمیشی گفتم ترامپ برادرت را کشت
سیروس قمیشی
برادر سیاوش قمیشی (خواننده و آهنگساز مشهور ایرانی) بود و پدر «امیر قمیشی» (از تهیه‌کنندگان و برنامه‌سازان تلویزیون رژیم) به شمار می‌رفت. وی در جریان بمباران بیمارستان گاندی تهران کشته شد و طبق گزارش‌های خبری، تنها یک روز تا زمان ترخیص و پایان درمان وی باقی مانده بود
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/15437" target="_blank">📅 21:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نبویان، نماینده مجلس: آمریکا بعد از شهادت آقا از طریق یکی از کشورهای اروپایی، پیام داد که بیایید مثل ونزوئلا تسلیم شوید!  وی‌در ادامه با دلایل بسیار گفت  ماجرای مذاکرات رسما کودتای آقایان علیه رهبری بود! و صدا و سیما هم حرفاشو قطع کرد ! @withyashar
🚨</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15436" target="_blank">📅 20:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">@withyashar
ماجرای ببر از زبان امیر تتلو حالا شد جریان عاصم منیره پاکستان</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/15435" target="_blank">📅 20:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الحدث به نقل از یک منبع آگاه: نخست‌وزیر پاکستان و مارشال عاصم منیر فردا در مذاکرات سوئیس شرکت خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/15434" target="_blank">📅 20:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">لیست هیئت اعزامی ایران به سوئیس به ریاست قالیباف
محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیئت مذاکره کننده ایران
سید عباس عراقچی، وزیر خارجه
علی باقری کنی، معاون بین‌الملل دبیرخانه شورای‌عالی امنیت ملی
عبدالناصر همتی، رئیس کل بانک مرکزی
حمید بورد، معاون وزیر نفت و رئیس شرکت ملی نفت ایران
کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزیر خارجه
اسماعیل بقائی، سخنگوی وزارت خارجه
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15433" target="_blank">📅 20:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15432">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نبویان، نماینده مجلس: آمریکا بعد از شهادت آقا از طریق یکی از کشورهای اروپایی، پیام داد که بیایید مثل ونزوئلا تسلیم شوید!
وی‌در ادامه با دلایل بسیار گفت  ماجرای مذاکرات رسما کودتای آقایان علیه رهبری بود! و صدا و سیما هم حرفاشو قطع کرد !
@withyashar
🚨</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15432" target="_blank">📅 20:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مقام اسرائیلی: ارتش اسرائیل طی دو روز گذشته به 300 هدف حزب‌الله حمله کرد و 100 نفر از نیروهای این گروه رو کشت.
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15431" target="_blank">📅 20:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15430">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بلومبرگ: عراق به میادین نفتی بزرگ دستور داده است که تولید خود را به بیش از ۳ میلیون بشکه در روز افزایش دهند، زیرا صادرات از طریق تنگه هرمز به تدریج پس از توافق آمریکا و ایران بهبود می‌یابد.
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15430" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15429">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مقامات ارشد ارتش اسرائیل به کانال 12 اسرائیل اعلام کردند:
عملیات نظامی در سراسر جنوب لبنان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/15429" target="_blank">📅 19:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15428">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سنتکام بعد از ادعای بسته شدن تنگه : نیروهای آمریکایی همچنان در منطقه حضور دارند و هوشیار هستند تا اطمینان حاصل شود که همه جنبه‌های توافق با ایران رعایت، اجرا و به طور کامل اجرا می‌شوند و همچنین مرکز مشترک اطلاعات دریایی با صدور اطلاعیه‌ای، عبور ایمن برای همه کشتی‌ها در امتداد مسیر تعیین‌شده را که عاری از هرگونه ادعا یا مانع خودسرانه است، تأیید کرد.
تردد کشتی‌های تجاری در تنگه هرمز در ۲۰ ژوئن افزایش یافت، زیرا نیروهای آمریکایی به عملیات خود در منطقه عمومی برای حمایت از آزادی ناوبری ادامه دادند.
امروز عبور ایمن از این آبراه بین‌المللی همچنان برقرار بود و ۵۵ کشتی تجاری در حال عبور بودند و مقادیر زیادی بار و بیش از ۱۷ میلیون بشکه نفت را به بازارهای جهانی منتقل می‌کردند.
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/15428" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15427">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو با دستور توقف جنگ گفت که این دستورالعمل‌ها شامل عقب‌نشینی از مناطق تحت کنترل نیروهای اسرائیلی در جنوب لبنان نمیشه و مناطق تصرف شده، تحت تصرف باقی میمونه.
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/15427" target="_blank">📅 19:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15426">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">محمد جواد ظریف: از مذاکرات استقبال میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/15426" target="_blank">📅 19:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15425">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj_xM5RMhb3wT0x1Pym-HMuIeAwS5-BVoh_nWPLOrjScr1GyU_kxtpA3admyFw74IrVNDorE-QpWQXnYgrFBZScBYD_gtcsM-xsdAbzRAdocjTBMKOczm3ZBgYYaiBkgX6S1amh1B30IG79H0jFjtE8CSC8WFabkxX_wL6KVky_JAGtqAnin_AL7t9zAa1HtCQR1i1veE_fWtGqv7G6NZNAR2BJUVA71qsLtvmpgQRw55hytEghz_gI25efmnklH_5ve5gfiKh2ijbtoC98tUJh-AWWNc-88fWofvfmPdZmS9jfet647LLET3naF0XVJgU4WWIi5x4iPsqXU6ucNZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه اولین تیمی شد که از جام جهانی حذف شد.
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/15425" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15424">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هم اکنون جی دی ونس به فاکس نیوز :
ما هیچ مدرکی مبنی بر اینکه ایرانی‌ها هنوز تنگه هرمز را می‌بندند، نمی‌بینیم.
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15424" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15423">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سخنگوی تیم مذاکره‌کننده: طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/15423" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15422">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بقایی: سفر به ژنو فاز دوم مذاکرات نیست و صرفا برای امضای یادداشت تفاهم به صورت حضوری است
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/15422" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15421">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فاکس نیوز به نقل از ونس، معاون ترامپ: اوضاع در مذاکرات با ایران خوب پیش میره و انتظار دارم به سوئیس سفر کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/15421" target="_blank">📅 17:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15420">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ایسنا: هیات مذاکره کننده ایران تا دقایقی دیگر عازم سوئیس می‌شوند
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15420" target="_blank">📅 17:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15419">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الحدث: عراقچی امشب همراه وزیر کشور پاکستان به سوئیس سفر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15419" target="_blank">📅 17:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15418">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تندروها معتقدن کودتای قالیباف تکمیل شده و الان قدرت اصلی کشور دست قالیبافه. چون با اینکه رهبر‌ گفته توافق خوب نیست ولی مجری های صداوسیما میگن توافق خوبه
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15418" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15417">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فایننشال‌تایمز: پایان عملیات نظامی اسرائیل در لبنان بعید است
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15417" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15416">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سخنگوی وزارت خارجه:
هیئت ایرانی برای پیگیری و مطالبۀ اجرای تعهدات طرف مقابل به سوئیس سفر خواهد کرد.
در سوئیس قرار است دربارۀ اجرای تعهدات طرف مقابل مطالبه‌گری داشته باشیم و مشخص شود آن‌ها چطور می‌خواهند به تعهداتشان عمل کنند.
ما به تعهداتمان پایبند بودیم و طرف مقابل موظف است اسرائیل را به توقف حمله به لبنان وادار کند.
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15416" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15415">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d9156929.mp4?token=rJM4vF4j8fJNLsI--tQbEYPr_edBMb7k3dWz_3yHfREe898BfSmtaO0k0xJC9D9qsJu8DzLzt8L8YWuwv-T0pi48aKwGlg0nHOeNmwhZWYB9j0DSMpdOKN4NKVd0_nzOH4Vu1VyS3-RIOij-XqAeB95a90m9Ex9tsVD1AaYS8d-UjvBXWNo5FOxedMZ0sxa59C1HjtdN77nYkTEPb9H2dQCTYGm6zs2kOMulTW4gB8fQYbIAAdODQBQ8eHbZHnXDvCm6l2uplpGaGyNyRZaq6jkLNRFZJ2_DoVE2At4xpRG5lY8Y9PyNRZlbXsZXTxGlNc5ybng1r91khNwhPurdWw_FxMs6bHCyMMieadMeALR0Utm8wPHanv0w1hW7_dypzqpYmipRfUHBxNx8Pds01IOiPMN_K6F5aYDMdszRvuzxxhrHdBGUvY6eZuabuJ5zeONV2SgyzM3qkx0DJdL0DHYPMYoTN60xap8TPfVQERi1N7gPJWcWWIyZwfwFTQgckNtvlEwa2bIpE9rRATbv0C5p1jFTuLtfGSwR18fLrHPu0rs4JV4EUrh7NLDF5Wn9tOwyuagmIk6wW2I1BQF39XgrsShvhNVkC_AVUSi7hA-RthAyf12_DlKusmWjOqDUb59EkozWUTyQfZBK0j8VJmnp9rrwTFC-IOzor9foJx8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d9156929.mp4?token=rJM4vF4j8fJNLsI--tQbEYPr_edBMb7k3dWz_3yHfREe898BfSmtaO0k0xJC9D9qsJu8DzLzt8L8YWuwv-T0pi48aKwGlg0nHOeNmwhZWYB9j0DSMpdOKN4NKVd0_nzOH4Vu1VyS3-RIOij-XqAeB95a90m9Ex9tsVD1AaYS8d-UjvBXWNo5FOxedMZ0sxa59C1HjtdN77nYkTEPb9H2dQCTYGm6zs2kOMulTW4gB8fQYbIAAdODQBQ8eHbZHnXDvCm6l2uplpGaGyNyRZaq6jkLNRFZJ2_DoVE2At4xpRG5lY8Y9PyNRZlbXsZXTxGlNc5ybng1r91khNwhPurdWw_FxMs6bHCyMMieadMeALR0Utm8wPHanv0w1hW7_dypzqpYmipRfUHBxNx8Pds01IOiPMN_K6F5aYDMdszRvuzxxhrHdBGUvY6eZuabuJ5zeONV2SgyzM3qkx0DJdL0DHYPMYoTN60xap8TPfVQERi1N7gPJWcWWIyZwfwFTQgckNtvlEwa2bIpE9rRATbv0C5p1jFTuLtfGSwR18fLrHPu0rs4JV4EUrh7NLDF5Wn9tOwyuagmIk6wW2I1BQF39XgrsShvhNVkC_AVUSi7hA-RthAyf12_DlKusmWjOqDUb59EkozWUTyQfZBK0j8VJmnp9rrwTFC-IOzor9foJx8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگه بابا جنگه !!!
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/15415" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15414">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تسنیم: نیازی به دیدار ویتکوف و عراقچی نیست.
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/15414" target="_blank">📅 16:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15413">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تنگه هرمز مجددا بسته شد
قرارگاه مرکزی حضرت خاتم‌الانبیا:
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامهپایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم مظلوم این سرزمین و همچنین با توجه به عدم عقب‌نشینی نیروهای اشغالگر صهیونی از اراضی جنوب لبنان، اعلام می‌دارد تنگه هرمز به روی تردد شناورها بسته خواهد شد.
متذکر می‌گردد این گام اول پاسخ به عهدشکنی دشمن است و در صورت ادامه تجاوز گام‌های بعدی برای پایبند کردن دشمن به اجرای تعهدات برنامه ریزی و اقدام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15413" target="_blank">📅 16:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15412">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_K2j0x2dULsp52UiwFZ492a-fKRvaumk5FIY_SG-J1PA9yoYZ-IVcgZcx5MwhPODMP1eqZ9o41iSTVgmBZ9LH4cblQYosqqhkp_NPQo6iWcb7tVCPNlyHtit8KV2vptta3sG8xoVmXW1Soc9ZWmr9xLOdaQFGoRTXTx5LAAkvisb3rw5qQDsbJMogyZkjPfHTi6iqsu_KMGkZHt0TZdIE1k6lf_kza6y5K_3V8LHJ2T15fn98wZ0J1oi6cKkDQB56vrLSOLN8h6L96I4HZ4mQbkv8FTzhaQ6f9qCy9ZOzLIod1fihBeEjJuqCNxvLn3fR_nzNMJUo9vO_Mku4T1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ
خبری
درباره تاثیر خود بر آینده سیاسی نتانیاهو را بازنشر کرد
دونالد ترامپ:
«ترامپ برگ‌های برنده را در سرنوشت انتخاباتی متزلزل نتانیاهو در اختیار دارد.»
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/15412" target="_blank">📅 16:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15411">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37917b1e44.mp4?token=M-9gVp2AqUfof36BDHse9YiwUOY6iNswVGK_Shm72TLCJids5_arMNiQ-_iJpP3Dlte5TCzIx4wQRK5NTAks-pnCmC80lQdAgtXTxJ79869OoQ5uWzpyIwmn_yh7g6TniXnN9_9Se_xRGyrdFkkDUxt75bUn3s5fkWkBCU-B1t4tNxFjZ22sk8zsfXV4aGXl353iH5BVXgUXfbXCylvRphg70WpSAodMUODB8g3kEb2WxQScZWLoSjoyQCT4vx_q8vdoOyZYcPxlU-rFTMFxBOAEEn9-89Q6EOkwmtyxWJFtEdpCXbZnVrA4MFAmDJ1ON6fuBbvv7jcy7dsF2S038w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37917b1e44.mp4?token=M-9gVp2AqUfof36BDHse9YiwUOY6iNswVGK_Shm72TLCJids5_arMNiQ-_iJpP3Dlte5TCzIx4wQRK5NTAks-pnCmC80lQdAgtXTxJ79869OoQ5uWzpyIwmn_yh7g6TniXnN9_9Se_xRGyrdFkkDUxt75bUn3s5fkWkBCU-B1t4tNxFjZ22sk8zsfXV4aGXl353iH5BVXgUXfbXCylvRphg70WpSAodMUODB8g3kEb2WxQScZWLoSjoyQCT4vx_q8vdoOyZYcPxlU-rFTMFxBOAEEn9-89Q6EOkwmtyxWJFtEdpCXbZnVrA4MFAmDJ1ON6fuBbvv7jcy7dsF2S038w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در طول ۲۴ ساعت گذشته، نزدیک به ۲۰ شناور از تنگه هرمز عبور کرده‌اند.
از این تعداد، ۵ شناور از مسیر امن تعیین‌شده توسط ایالات متحده که از آب‌های عمان عبور می‌کند، استفاده کرده‌اند.
بقیه شناورها از طرح جداسازی ترافیک ایران استفاده می‌کنند.
در حال حاضر دو مسیر اصلی برای عبور کشتی‌ها از تنگه هرمز وجود دارد
اول ، طرح ترافیکی ایران (TSS) که همان مسیر اصلی و همیشگی تنگه هرمز است که عمدتاً نزدیک سواحل و جزایر ایران قرار دارد.
مسیر دوم کریدور موقت ایجادشده توسط آمریکا در آب‌های عمان و دورتر از سواحل ایران و طراحی‌شده در زمان جنگ و موقت.
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/15411" target="_blank">📅 16:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15410">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYHCo6TtgUf5m3t10QzdfH_gIKwBN-ASZnOFDlBKJWqRxoI3-IRje2CetKPUmV8ke9mYFVXc5gwVdWr-Tz86UJK_OzsVX-E0n_mIUcrigFh5ql1PrWJlvPy2l9E3d8T06mMdjydy6df3kRQuy2JCWpmKpfIcoXbPDs-LQcrYrqGGWpgmJ2Ww--yyguVjDArYHatArBynhzFLrE3PLmTAsOBo8_13aDR6M1-_pPCTV0fRpzYjezibsXF3aV_yGu4Zb5LKRCwpYyQd3ZFVnVsI1DxhpCS_kATK0Xs74FRywO4N7WD_JD6RFApebw_Cq2Tw6-j-CR8TkFul0GmYdXNW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه سوئیس: مذاکره آمریکا و ایران در فضایی محرمانه در بورگن‌اشتوک ادامه خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/15410" target="_blank">📅 16:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15409">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXlq5IepwGlIx5naFSACttOqYP2o11rFaczHJt_Q3m3MnhjWU-36Ls8ZrsPCHOsctBlG5-szvvsyREwxTEjEeBQKFY445qHB-EhuU141p43LwkLcb-dV6kbxrNCJGOyK5rTUHPzfXyN-l0TnLrSCkFsPkwkVMqBoXp1TjVBiIV_n8gbbwsZVfN92lI-dgKQPmMe5YbotnNLFsGVLtJIHVm-9iHPYJYRJ1kcAnnXEGadScyG7i1hzL1dfljLxp2GbB4D4b6Lb3Z_4wcXiaSE3KKp6JjDwYWWmvLfKHcP-O3zpY2SCYV9W6oRkpLBODRu3tBcpRhZUbLpgT4v_r0IG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در ‌تروث :
جورجیا ملونی، نخست‌وزیر ایتالیا، در طول نشست گروه ۷ در فرانسه، بارها و بارها از من خواست که باهم عکس بگیریم. اون در ایتالیا از نظر میزان محبوبیت وضعیت ضعیفی داره؛ احتمالا به این دلیل که وقتی نوبت به جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران رسید، به ایالات متحده آمریکا—کشوری که واقعا ایتالیا رو دوست داره و از آن محافظت می‌کند—پشت کرد (البته ناتو هم در این مورد همین کار رو کرد!).
اون حتی اجازه نداد از باندهای فرود یا باندهای پرواز ایتالیا استفاده کنیم، که یک دشواری لوجستیکی بزرگ بود؛ آن هم با وجود این واقعیت که ایالات متحده سالانه صدها میلیارد دلار برای محافظت از ایتالیا و دیگر متحدان «به اصطلاح» ناتو هزینه می‌کنه. حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، اون می‌خواد دوباره با ما دوست بشه تا «آمار محبوبیتش» رو بالا ببره.
نه، خیلی ممنون!!!
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15409" target="_blank">📅 15:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15408">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fc382a14.mp4?token=cu_lOMUMINtT8BE5tbN42adCxQ3h2iOB65iR9NH-Y9gAKD9Bode2wroXoVO4gBci-Hc0XvWwKOsRAOkVau3Xz0UiyMCeT-PSjk4dQ9IwXyMH5Q7woMKsbtbbzC_d9Tr1k0Yj-voE8cLAyAJj6r6CNQRrM_v8ZGFIbuJ4N9QgypTEY8HyKJzXU_aUl-E8erzsZtdw89kDXIKQpv2pc-aIkmhq82OyJYbzFJ8FSJpj5W004yMIqTqq0Q8JnbdkH6S4888VyTaspejjmEw1AykH3Z3cTnm7vUUVd7MEzavoQc1BDhaB8GnWBgvYzI1J7GyM-H1Qan19s8klGpo7_sz3iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fc382a14.mp4?token=cu_lOMUMINtT8BE5tbN42adCxQ3h2iOB65iR9NH-Y9gAKD9Bode2wroXoVO4gBci-Hc0XvWwKOsRAOkVau3Xz0UiyMCeT-PSjk4dQ9IwXyMH5Q7woMKsbtbbzC_d9Tr1k0Yj-voE8cLAyAJj6r6CNQRrM_v8ZGFIbuJ4N9QgypTEY8HyKJzXU_aUl-E8erzsZtdw89kDXIKQpv2pc-aIkmhq82OyJYbzFJ8FSJpj5W004yMIqTqq0Q8JnbdkH6S4888VyTaspejjmEw1AykH3Z3cTnm7vUUVd7MEzavoQc1BDhaB8GnWBgvYzI1J7GyM-H1Qan19s8klGpo7_sz3iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون خمین
🚨
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/15408" target="_blank">📅 15:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15406">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JticsIfY_GwCZHzZaSZSrNW4Sw6oDJ0eYTfiwuCi6yvn1PRstiN0SG5tR99qcgPOAnA2My9bQGQH8Mms9ojQ3y__ig2Dv5mnYpKzsiIFg7XKaZfRXom5LYD3MFilAQTFPgwc4C3mFyLNs_NymmcIeJmaTNxnnSDtyWXANzVkx6cy-kbzqhR3GgUk2Csas2AWHseQ9AiFEAAFK2_oUEAzAoa2XirlujkWh7SEoykjwJ0BUfTngF9SIsdTDEksMJfUNHIjQ9e1w2eCqCAn41ui0TAjdRGgUt22I8RnJHp2w_rEmqE36T0BmUozOS6t5_Af0uRjpuPxx0_JJQzxZxZ5rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث برای بار هزارم : خنده‌داره که چطور دموکرات‌ها دوست دارن بگن ایران امروز در موقعیت قوی‌تری نسبت به سه ماه پیش قرار داره، با وجود اینکه از نظر نظامی شکست خوردن، نه نیروی دریایی دارن و نه نیروی هوایی. به همین دلیله که من بهشون میگم دموکرات!!! رئیس جمهور دی‌جی‌تی
@withyashar</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/15406" target="_blank">📅 15:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15405">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فاکس‌نیوز: ویتکاف و کوشنر در سوئیس هستند
شبکه خبری فاکس‌نیوز اعلام کرد، بنا به گزارش‌ها، استیو ویتکاف، فرستاده کاخ سفید، و جرد کوشنر، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس هستند، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/15405" target="_blank">📅 15:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15404">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرنگار صداسیما: شاهد یکی از شدیدترین حملات به منطقۀ نبطیه هستیم؛ نبطیه تقریبا خالی از جمعیت شده
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/15404" target="_blank">📅 15:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15403">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/15403" target="_blank">📅 14:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15402">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">@withyashar
خاطرات شمال</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/15402" target="_blank">📅 14:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15401">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/15401" target="_blank">📅 14:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15400">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/15400" target="_blank">📅 14:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15399">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ در تروث : چپ‌های افراطی و دموکرات‌های احمق دارند می‌بینند که ما در جنگ علیه ایران چقدر خوب عمل کرده‌ایم، به‌طوری که کشورشان از نظر نظامی به‌طور کامل شکست خورده است. اوباما فقط میلیاردها دلار پول نقد به آن‌ها می‌داد و هرگز از ارتشِ آن‌زمانِ تضعیف‌شده‌مان برای کاری که باید انجام می‌شد استفاده نکرد تا بزرگ‌ترین حامی تروریسم در جهان، یعنی ایران، مهار شود. آن‌ها کوچک‌ترین احترامی برای او قائل نبودند. آن‌ها فکر می‌کردند او، مثل جو خواب‌آلود بایدن، رهبری ضعیف و بی‌اثر است، و در این مورد ۱۰۰٪ درست می‌گفتند. ایران ۴۷ سال از مجازات برای “جنایت” گریخت، تا وقتی که من آمدم. بعد همه‌چیز تغییر کرد. آمریکا بازگشته است!!!
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/15399" target="_blank">📅 14:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15398">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/872d942820.mp4?token=d6Wb9zmC00tUzJjUAdEeqS3WPCFN2TUDuXLfKluNDGOiWBchFfP9bmWoIMp_uNJtiVEUyDRkkm98aUFG1_PGlENhuWHMMs1joG15-3ddmcjSDsyekihdwxTDCA1miZCC-wVoMuH47E3d3Z4NyKn3LvVSqWj-XdxWitNjitZBqL-3pkW-f7V_HXTRjd6IwmsTAotu_qk5BK1nc7quZmEx3PwJv8EBlSHGgtqI-P9hJkTj-cVgf5CiBEO0fjL9Oi16nrS0rv8ALmjT-wb7afaBFd4K7lwcOkdVTAApoME3RT7u7lqi1qIbZL7nYOyve-SPvDo7fR-4JdZ5zrrkLsGWkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/872d942820.mp4?token=d6Wb9zmC00tUzJjUAdEeqS3WPCFN2TUDuXLfKluNDGOiWBchFfP9bmWoIMp_uNJtiVEUyDRkkm98aUFG1_PGlENhuWHMMs1joG15-3ddmcjSDsyekihdwxTDCA1miZCC-wVoMuH47E3d3Z4NyKn3LvVSqWj-XdxWitNjitZBqL-3pkW-f7V_HXTRjd6IwmsTAotu_qk5BK1nc7quZmEx3PwJv8EBlSHGgtqI-P9hJkTj-cVgf5CiBEO0fjL9Oi16nrS0rv8ALmjT-wb7afaBFd4K7lwcOkdVTAApoME3RT7u7lqi1qIbZL7nYOyve-SPvDo7fR-4JdZ5zrrkLsGWkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون خمین
🚨
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15398" target="_blank">📅 14:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15397">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">العربیه :  مذاکرات تا اطلاع ثانوی لغو شد. هیات آمریکایی و هیات ایرانی سفر خود به سوئیس را لغو کردند
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/15397" target="_blank">📅 14:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15396">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دولت هلند اعلام کرد مسیر حرکت یک ناوچه پدافند هوایی خود را به سوی تنگه هرمز تغییر داده است تا در صورت تشکیل یک مأموریت بین‌المللی احتمالی در این آبراه راهبردی، امکان مشارکت در آن را داشته باشد به گفته وزیر دفاع هلند،
رسیدن آن به محدوده تنگه هرمز چند هفته زمان خواهد برد.
این تصمیم در حالی اعلام شده است که فرانسه و بریتانیا برای ایجاد یک مأموریت چندملیتی دریایی در تنگه هرمز تلاش می‌کنند.
آلمان نیز روز پنجشنبه اعلام کرد دو کشتی خود را برای آمادگی جهت مشارکت احتمالی در مأموریت نظامی در تنگه هرمز به دریای سرخ اعزام می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/15396" target="_blank">📅 14:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرگزاری NBC به نقل از یک مقام آمریکایی اعلام کرد «نیروهای ایالات متحده به عملیات خود در منطقه برای حمایت از آزادی کشتیرانی ادامه خواهند داد و اجازه حمله به هیچ کشتی‌ای را نخواهند داد.»
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15395" target="_blank">📅 13:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سوئیس تصمیم گرفته تدابیر امنیتی در کشور را تا ۲۲ ژوئن تمدید کند، در حالی که منتظر موافقت طرف ایرانی برای ازسرگیری مذاکرات است.
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15394" target="_blank">📅 13:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15393">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نیویورک تایمز:  مقامات غربی از نتانیاهو خواسته‌اند حملات به لبنان را متوقف کند تا ایران نتواند خروج از مذاکرات را توجیه کند.
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/15393" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش شنیده شدن صدای انفجار در‌بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15392" target="_blank">📅 13:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15391">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تسنیم : دیدار با ویتکاف هیچ توجیهی ندارد. خوشبختانه مقامات ایرانی تا این لحظه حاضر  به دیدار با تیم آمریکایی نشده اند
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/15391" target="_blank">📅 13:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15390">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش شنیده شدن صدای انفجار در‌بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/15390" target="_blank">📅 13:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15389">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هم اکنون حملات فوق سنگین اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/15389" target="_blank">📅 13:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15388">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">instagram.com/yashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/15388" target="_blank">📅 12:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15387">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزاری رویترز به نقل از یک مقام اسرائیلی اعلام کرد که حزب الله از شب گذشته تا کنون بیش از ۵۰ راکت به سمت نیروهای اسرائیلی شلیک کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/15387" target="_blank">📅 12:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15386">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرنگار العربیه از لوسرن: یک هیئت بلندپایه آمریکایی وارد سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/15386" target="_blank">📅 11:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15385">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ایلان ماسک: «در آینده، برای تولید پادماده (Antimatter) جهت سفر به منظومه‌های ستاره‌ای دیگر، یک تریلیون ضربدر یک تریلیون دلار هزینه خواهد شد.آن زمان دیگر چیزی با دلار اندازه‌گیری نخواهد شد؛ فقط با جرم و انرژی.»
پادماده (Antimatter) یکی از قدرتمندترین گزینه‌های پیشنهادی برای سوخت فضاپیماهای آینده است، اما فعلاً استفاده از آن به‌عنوان سوخت در حد یک ایده و فناوری نظری باقی مانده. هنگام برخورد پادماده با ماده‌ی معمولی، تقریباً تمام جرم آن‌ها به انرژی تبدیل می‌شود و انرژی عظیمی آزاد می‌کند. امروز تولید حتی مقدار بسیار ناچیزی از پادماده فوق‌العاده گران است و هزینه‌ی آن تا ۶۰ تریلیون دلار برای هر گرم تخمین زده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/15385" target="_blank">📅 11:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15384">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">"وال‌استریت ژورنال" گزارش داد که ایالات متحده و قطر در حال تدوین طرحی برای آزادسازی میلیاردها دلار از دارایی‌های مسدودشده ایران هستند.
در مرحله نخست ایران می‌تواند به دستکم ۶ میلیارد دلار از منابع مالی خود که در قطر نگهداری می‌شود، دسترسی پیدا کند.
بانک مرکزی ایران در صورت اجرای این طرح خواهد توانست از این منابع برای خرید مواد غذایی، دارو و سایر کالاهای بشردوستانه ضروری استفاده کند.
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/15384" target="_blank">📅 11:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15383">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو: ما در حال محکم‌تر کردن و در دست گرفتن حماس در غزه هستیم، جایی که بیش از ۶۰ درصد از قلمرو نوار را در اختیار داریم و در لبنان، ما تهدید یک تهاجم زمینی علیه جوامع ما را پس زدیم و توان موشکی حزب‌الله را شکستیم.
هنوز کار بیشتری برای انجام دادن در هر دو مکان وجود دارد.
ما باید منافع امنیتی خود را به قاطعیت حفظ کنیم در حالی که ارتباط مهم با دوستان آمریکایی خود را نیز حفظ می‌کنیم.
ما ادامه خواهیم داد تا مسیر خود را با خرد و قضاوت سالم طی کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/15383" target="_blank">📅 11:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15382">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرگزاری دولت: وزیر کشور پاکستان برای دیدار با مسئولان بلند پایه ایرانی، عازم‌ تهران شد
او در این سفر «پیش‌برد مذاکرات» را پیگیری خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/15382" target="_blank">📅 10:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15381">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">توضیح بانک مرکزی درباره اختلال در فرایند ۴ بانک کشور:
این اختلال در اثر حمله سایبری به زیرساخت‌ ارتباطی این بانک‌ها ایجاد شده
هیچ‌گونه آسیبی به اطلاعات مشتریان این بانک‌ها وارد نشده
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/15381" target="_blank">📅 10:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15380">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به گزارش رویترز، در نتیجه لغو تحریم‌های ایران، سپاه پاسداران ایران آماده است تا از نظر دسترسی به صندوق بازسازی بالقوه ۳۰۰ میلیارد دلاری، «برد بزرگی» کسب کند، ضمن اینکه از محل معافیت از تحریم‌های فروش نفت نیز درآمد کسب خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/15380" target="_blank">📅 10:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15379">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">منابع خبری صبح امروز از حمله هوایی اسرائیل به یک ساختمان مسکونی در مرکز شهر غزه خبر دادند که در این حمله ۳نفر کشته شدند
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/15379" target="_blank">📅 09:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15378">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">میخوای بفهمی قیمت طلا بالا میره یا نه؟  میخوای ارزش دلارهایی که خریدیو هر لحظه چک کنی؟  سودتو هی بفهمی فقط کافیه به تحلیل‌های این کانال گوش بدی
✨
@link_Nostradamus @link_Nostradamus</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/15378" target="_blank">📅 04:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15377">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">میخوای بفهمی قیمت طلا بالا میره یا نه؟
میخوای ارزش دلارهایی که خریدیو هر لحظه چک کنی؟
سودتو هی بفهمی
فقط کافیه به تحلیل‌های این کانال گوش بدی
✨
@link_Nostradamus
@link_Nostradamus</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/15377" target="_blank">📅 04:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15376">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ برای یک سفر
نادر به کمپ دیوید
در آخر هفته برنامه‌ریزی کرده و هم‌اکنون در حال اقامت/حرکت به آنجاست. این سفر هم‌زمان با
افزایش تنش‌ها در خاورمیانه و پرونده ایران
انجام شده و شامل جلسات سیاسی در همان محل است.
گزارش شده که او از پایگاه «جُینت بیس اندروز» بعد از رو  نمایی از ایر فرس وان جدید به کمپ دیوید حرکت کرده است.
@withyashar
آخرین باری که رئیس‌جمهور ترامپ برای یک دوره طولانی به «کمپ دیوید» رفت، همان زمانی بود که عملیات «چکش نیمه‌شب» را دریافت کردیم؛ یعنی بمباران سایت‌های هسته‌ای ایران، حدود یک سال پیش در همین آخر هفته.
و حالا بخشی دیگر از نخستین گفت‌وگوی تصویری ترامپ پس از امضای آن «یادداشت تفاهم» در پاریس و در کاخ ورسای، با آکسیوس. در این مصاحبه از رئیس‌جمهور ترامپ پرسیده شد: آیا برای قدرت ایالات متحده محدودیتی وجود دارد؟ و چه درس‌هایی از این جنگ ۴ ماهه گرفته شده است (یادتان باشد کاخ سفید گفته بود این جنگ فقط ۴ تا ۶ هفته طول می‌کشد؟)
@withyashar
ترامپ گفت: «من هنوز این درس را نگرفته‌ام. می‌دانم محدودیت‌هایی وجود دارد، اما در عمل می‌گویم محدودیتی نیست. ما آن‌ها را کاملاً از نظر نظامی شکست دادیم.» او همچنین گفت این «یادداشت تفاهم» شبیه تسلیم بی‌قید و شرط نیست، هرچند احتمالاً در واقع همان تسلیم بی‌قید و شرط است.
مصاحبه کامل بعداً در برنامه آکسیوس منتشر خواهد شد.
حالا دیشب، حزب‌الله حمله‌ای به شمال اسرائیل انجام داد که در نتیجه آن چهار سرباز اسرائیلی کشته شدند و این اقدام نقض آتش‌بس محسوب شد. سپس اسرائیل نیز حملات تلافی‌جویانه‌ای در لبنان انجام داد.
@withyashar
یادآوری می‌شود که آتش‌بس در لبنان بخشی از همان یادداشت تفاهمی بود که ترامپ امضا کرده بود. معاون رئیس‌جمهور، جی‌دی ونس، دیروز در کاخ سفید به خبرنگاران گفت که حفظ این آتش‌بس چالش‌برانگیز خواهد بود:
«ما انتظار داریم حزب‌الله به سمت اسرائیل موشک و پهپاد شلیک نکند، و همچنین انتظار داریم اسرائیل هم در لبنان کنترل‌شده عمل کند. هر دو طرف باید به تعهدات خود پایبند باشند.»
او اضافه کرد که چنین آتش‌بس‌هایی گاهی کمی آشفته هستند.
همچنین قرار بود معاون رئیس‌جمهور، جی‌دی ونس، با پروازی به سوئیس برود تا یک دوره ۶۰ روزه مذاکرات با ایران درباره برنامه هسته‌ای را آغاز کند، اما این سفر لغو شد چون ایران اعلام کرد به دلیل درگیری میان حزب‌الله و اسرائیل در این نشست شرکت نخواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/15376" target="_blank">📅 03:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15375">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آکسیوس: ویتکاف برای اولین دور مذاکرات داره میره سوئیس.
البته
فعلا تاریخ جدیدی برای مذاکرات تایید نشده؛ نخست وزیر قطر هم به عنوان میانجی اصلی الان تو سوئیسه.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/15375" target="_blank">📅 03:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15374">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بابک زنجانی : ‏به نظر می‌رسد یک موضوع نفوذ و خرابکاری امنیتی در کشور در حال وقوع است.
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/15374" target="_blank">📅 02:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15373">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عفو بین‌الملل هشدار داد مقام‌های جمهوری اسلامی از پوشش شرایط جنگی برای تشدید سرکوب استفاده کرده‌اند. همزمان برخی خانواده کشته‌شدگان‌ دی هم از حذف نام آنها در سامانه «بهشت زهرا»ا خبر دادند.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/15373" target="_blank">📅 02:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15372">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ارتش اسرائیل (IDF) در حال پیشروی به سمت تپه علی الطاهر است.
بعد از بمباران سنگین تپه الطاهر در هفت روز گذشته، حال نیروهای اسرائیلی در حال فتح این تپه هستند.
تپه الطاهر از لحاظ استراتژیک آخرین سد دفاعی شهر نبطیه است‌.
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/15372" target="_blank">📅 02:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15371">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElbJ3WjvNI7ZQrbnO5ifEb9xiROlNv8_n3WlyuXK0d5Slh03xHm2WdGFbTapavIxSA-XNt_tb_2VT6oqn_OoNOIyy6YaPFvA7KF1rR8qkw_-gliQWrJGCne4qV2Dcay7GrR0jNhF315eAi1MKHSRLkR4yksyJtU_rVVU7rtyvCqgS5XjjQsIiGXQhClUCiguckCfB8N8-y_grUYiiWP3sTqe-IQ9vzjNesN8cLJPN1MKxHCS5htsax8nEmhKnE4cR4W-myRaBWKbPBJ-TKJ5GapVq6jAGrShsg2o04Yb3E752AKhMmBQ6sPODAcJaTePaEb1E9cNnjmpWxT6cXja3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت ۱۰ نفتکش ایرانی به نام های؛ دیونا، قهرمان، سونیا، دورنا، آمبر، خندان، برف، هدی، استارلا و دریا عمیق به طرف چین
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/15371" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15370">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تیم ملی آمریکا با برد ۲ هیچ برابر استرالیا به عنوان دومین تیم پر قدرت به مرحله حذفی جام جهانی ۲۰۲۶ صعود کرد!
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/15370" target="_blank">📅 01:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15369">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746536a751.mp4?token=vZ7VxwHss2ojgr8pLSD5TDfCgq2vmVRpWtAywFhCHM21x2yy6cp9VBbCqZqlWUKeJWya6I2XsAIE264ypB0UuB2QxkEElFOEIWvHSbMjhfK4fXK9wrw5ckWm1ZknJ3Hl0AB2520KFEPtrmIbFjwzDN1Z8jNwusFHJ7kBFcK230VsyVQWA1QxcxANiqUbSEAE_CcYU5KS0ZSZ_pjcRiJVGI8FWH4Ev6BId_Yj0GcWzhneE5taTltNoKsSPbFB7YTL3A8IBJsJJFVMXkSdHGRAP8FcqQ7oytwFHZ0THiQpD1KOJPO9Q0AiccqXtWkKpBCzSSP7v_ZVSBSoUMwXcNTjew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746536a751.mp4?token=vZ7VxwHss2ojgr8pLSD5TDfCgq2vmVRpWtAywFhCHM21x2yy6cp9VBbCqZqlWUKeJWya6I2XsAIE264ypB0UuB2QxkEElFOEIWvHSbMjhfK4fXK9wrw5ckWm1ZknJ3Hl0AB2520KFEPtrmIbFjwzDN1Z8jNwusFHJ7kBFcK230VsyVQWA1QxcxANiqUbSEAE_CcYU5KS0ZSZ_pjcRiJVGI8FWH4Ev6BId_Yj0GcWzhneE5taTltNoKsSPbFB7YTL3A8IBJsJJFVMXkSdHGRAP8FcqQ7oytwFHZ0THiQpD1KOJPO9Q0AiccqXtWkKpBCzSSP7v_ZVSBSoUMwXcNTjew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان درگیری‌های سنگین بین نیروهای اسرائیل و حزب‌الله تو لُبنان
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/15369" target="_blank">📅 01:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15368">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of6ppRA9zUHN61cM0_6Orvf5Icd89u9D2s82jbpRDHyWRCmmK7asa4e7XnXegWExijA_eTuADO7YmKt3leN-ZAKRgHd-pBX0nmfhGgKmOhgIb37IT8knaJW5ObgrO2kLgZhpEnRcVzLPALx4y1f8qpMbKCQ5B6n9wuLPCzttr2I4Ftqm5WSbs8OphQt3-mXoZP7m5u0zhtbo9hWBjG3uGbwdpNx_WclIIRUaI4QS3ScPYNwHPVLvgvh45TWDU7bxL8Ya3HiKPYAb2Jd6KjUDzHmc7GsZvr48nrxCufFqx4T2VoSLubPE_tg2I-2t8MU1K2-Kkl2VUsQrNN6uIH4Zug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور لایو
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/15368" target="_blank">📅 01:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15367">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">https://www.instagram.com/reel/DZyFKZXCHfl/?igsh=anMxYmI2ZnUzdHpy
لایو سیو شد</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/15367" target="_blank">📅 00:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15366">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">میرم لایو اینستاگرام
💥
🚨
۵ دقیقه دیگه نتیف های اینستاگرام رو روشن کنید و اگه ندارید فالو کنید instagram.com/yashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/15366" target="_blank">📅 00:14 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
