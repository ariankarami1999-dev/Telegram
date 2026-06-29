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
<img src="https://cdn4.telesco.pe/file/KQYllhrq5fquFtHCl-q3zQgK6mHyFRITxhPfTjZAVFfEZxjL5smCcAsz8EuTtYbMnZoqBTW9beNEJdLakE6fiB2sox75YXmlda737VXHmtfPUH1khrPvscjX6W5fIxMnXHtaszLHO_QSeMSxyPpnaA7ThK6IdDznx9KKY3E87D3kIbWk2dhgeDXuo1Dd6qWtUjqfXa_Fj9O2vHHdraHj7EKGhZRLgCKNQLvMAJNJDK1g8YOIrVCjTXVph6WRw0BVEoA4CHwCvtKlT6F-UQwbJe2BG1Bg18qrPDNY3gGYWeWmiNT9Sje-6VnaYHNd2t7tZBzDg6iTNDj8aEN2Lh3-Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 345K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 18:01:45</div>
<hr>

<div class="tg-post" id="msg-24613">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-MM9uJdACCPEhZhXLv7hGzNYA5yMWxINz59EDOvw7s7yWVnGRk7om2D4YdyNmVr8RZOgncFIjrUvKdT7rFsg1RwyoeTeGxDdAtdjx5lF1jVDxepxtQIDop3yLK2RXMBOZsJRgE4hFKkAWUvd7zw6joyfzFln1TeSigx_NA-Bq9OxZ5xzPRkLqR1rmgIctkmlqsvKRDhQtuZACAx-dMpCkuFqO1-I1ku2Ok6BOcIWxAyPUzJDyzPeJi0x7YBbFnasQYyMkDn7zEgObF-_biA4BWWT6qbVrtnujXSy7_t0GukYDv4GYlvjSTlanE87scSMjLRTWYe7Z11RufDM4uqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/persiana_Soccer/24613" target="_blank">📅 17:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6nj-C6R4jjJZGce3j5955l7ZJeeMBKpy9QQFVPJpUd4CKRVZFswQL07tz8qKXkN-rFF3ebfeGNmZjTLCONVBuIHV8Q_mXX2MP5UHREFg30SI3eWdykhKcPlulMdphR8sp3KPeEUHasVKCHlFKpQ3EOkfJLdn9ONbO7HDDrSuTGcBD4vmpeGFCxwQEt2bPaW3fwJx40Nfs7ja0RGY4zXlNOvDeZOl1V5K2RWw4UAUliLyA-t2WcC2AIBxYQZZftdxvMgrMml3bPs1yAQp1P4fAoxzye25mLGWmq5NlA5XtHtnrkC5uV2k5r95wx56cjWDSqdfPTMeBaUI2EfzvooRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9BcLJDYjDEieQCSTxXMquzIDqkYtckUrxar7W173a42EykiWxHARE_qrATRyE0abowfh7Z4XINWJRi-V8KoLDBp5RH8ynjrOLmZ9BNbeHqMweMXZNV3ge02rXlG4NoO3MrRtzeailSAgyF_9OnFsYFYp-kSvJ6k8I4SwuaAIqk4QSlJq81EhKSCDDnKqSDdIYAibtiW8Z6-zWaMVvQvtlFB4-WtTKsqMo0pAr4Y1GMiBQO9S3UOb1OluoOUKmJOVTJ3OVn7ixcdywynBOPGooQAJa9CuGI6zXQvQWdqqPSwzRCjMwFF6QHct0GVW0suAAFbjazh8Wq6MW07ESZEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUX0tRd4MCovODNxLfXHE_8Ktea0SKPvS8PFQPMQj_Q0OOEx1yFVG74OVaQs0r9gO-PjeI1itlgfISsiIHDZw6Gvse4ilSvkLyQkiH1-9tXb6EVf7emrby2iAW3T8YN4CHcTOuQI6up6AZNjRdxIncKfn9tHA5d5HUXLm97Ygzydgu1Uea50g7bXQzwaAyhK6jepTT7KiEWas6-tXYHkOI9xJRv_VGq-kd1xnc2D3ntPItAI1XCl35o-LsvfDXW2blTZ0c7b8EN2O1zXJl34Cup3Soz0UaSp8AiXHMitF4B-7Re-ZwfcbvhG_QnmT0gwXW_f9WnqxKYt7qCyYEC6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
باشگاه رئال مادرید رقم فروش ادر کاماوینگا هافبک فرانسوی خود را اعلام کرد: 60 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/24610" target="_blank">📅 16:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=bW6r6TG5Bn2aj1ky498wzlmM6p354JAnOTx1UfYPFyjgnLbkuZydwjaPLo7KoAKpBP3HDmZ0QUKYjEXp4KskpDLlgX_hm8Vi_vlUh74PVu6Wj9gbRgTZ84TNr7Xrmu0S0GlAdJHCRLSwJ1tGQEmPgdRPPj-6N9UDsK6D0mB4PrJqqQsoY9sKRPUrTRdnGR7a_KDCcZs2eRw_RvruZt7oyIgFQg7zm0cxHaJ3rjV0BCs3iHVhsO8mXCQwvKDfhcnQlRJUZfXHljkXodug04ligfOEMhJ9aCkzKpTZrQlUeb-V6V1ozuvjDOUdZ2zSrN6dR0vwLn8e69CrEcVxutC4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=bW6r6TG5Bn2aj1ky498wzlmM6p354JAnOTx1UfYPFyjgnLbkuZydwjaPLo7KoAKpBP3HDmZ0QUKYjEXp4KskpDLlgX_hm8Vi_vlUh74PVu6Wj9gbRgTZ84TNr7Xrmu0S0GlAdJHCRLSwJ1tGQEmPgdRPPj-6N9UDsK6D0mB4PrJqqQsoY9sKRPUrTRdnGR7a_KDCcZs2eRw_RvruZt7oyIgFQg7zm0cxHaJ3rjV0BCs3iHVhsO8mXCQwvKDfhcnQlRJUZfXHljkXodug04ligfOEMhJ9aCkzKpTZrQlUeb-V6V1ozuvjDOUdZ2zSrN6dR0vwLn8e69CrEcVxutC4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگی‌که وقتی شاگردان قلعه نویی بعد حذف از جام‌جهانی به ایران برگشتن باید براشون بخونند:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/24609" target="_blank">📅 15:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQzgWv_TEX2nqwbU8no8sadVq6oPMf_sDKC2tBH1FTypVpAsaqBQkAZ_XX9sA6neUkcPTbciAlk_18-Th8_NWn4FSVXdOinx3AfNK2ft1lqgYn85lnTXDNXkimbckU6_emv9PcSnoahoG5gpQkuc6XchCrwU1klwQQdG4BIoQbS-Jd5FXaeKA-yV3AqXdCGRXmjnzL5bPf-34P0eOhQVfgJSSEgkZJXYHccyTLbOArUWA8JiZWWhbVz8KMF0TXnnjJ0iuwnNZToLSTrbD3zoiNSVxhEV-_JJ_CnCp1LWNQfVCrlgxXFr6O8ycIfJThuUKeRHNiZL21wHDEiBT99Kzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/24608" target="_blank">📅 15:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rd0gdzoX7N9CRdmfhq8E9Ee_W6UlDIjNcZrnv4yA3BwuVWFBGEgKFnylQkXWLateR30cnDkm-tCM7L3E_55rducv6XCZ86l_uf2y_AG3nvb2cGtiJxMuQx3h-FQQYEDeqUazAgdzRKMC7onuHCeTp9sHTLPn9EuLnx0TYea5ebA2Eokk4RBb-TjT9gImEOrB8SHEAtfZKOq8oxvwaF_VeesKBpYyyTZa3tF0eIAHq1LFQzAYRHYkGj__22lDjyJZ1yLM-6O1bNVgPxO6Xs1UsEeArccSdctlmqgtLguzVsUwmri9f2vefrYM7iL1kn9wpTe4fKZS72hkz4dszMrFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_3AnMh198Igvs-6lPiBLhQHfSzsaojKLg9sk09iMqwCVZF1_KK6pSsPR-UEQt7viXfFwcWRtCnksRhGP3BS6SCyyF4-KF1EyEtx9N7pvQjfvYUpnq18cKcJyIntnQydJvueNfiJaQyWzoqXQj_YGJibNRY9izNWFm-xSaIj0tTE41qr9rkUx88AbJ6nTI1JjvZ-w6wlAan7OsMBRy95GpnowyBLpgHuz5aBueipW5XjcmKukh60CjKn9Exx7a6Wlw2umi6UNSRvQkfahER1vnuMRQYUktGTgPmonn1Nx6w6TbwhU5NjHzQx1jKIA8YbSKbmnep6-XmWNd7EH7sVSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور کاپیتان دوم تیم ملی برزیل: وینیسیوس فوق‌ستاره جام جهانیه و مطمئن هستم که میتونه ما رو به قهرمانی این رقابت‌ها برسونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24606" target="_blank">📅 14:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4MqMlB1bXMj_o7J1d2OFBGuvQRgD8RooGCoQWwwQVrf1Z4vD89OWUwAUjGZ6691WC9X8H5xcuefXBSWFu6M3jDj9bmbM5zab_PibYg5GVhpPT3lfbXhUd-J9f2Vv3xK2dGRK8hDGzrmJAR0iQAMjTX950qk-8wtd7cmIufEzF_rj5X2Dj4jxdGehFn6hO3cmRcYX0JY1T5ixmTvJvSgEk55_rbBap2cKEsP2vm9f0MQdknBa4o1nSWfNHoXF9zyDtoxyxpUNmnEwg84IpbNAICJiazdTdPN_N3FC-BtXTLJxTRlUvgxaqInSyKAZ29_iqby1ul-thYOJ6bpIJkbhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بلاگر و هوادار تیم ملی اردن در پیجش افشا کرده یکی از بازیکنان متاهل تیم ملی آرژانتین بهش پیشنهاد دوستی و رابطه داده که او رو بلاک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/24605" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNOUWE_kmX4u8Zjy0W9aosIqansoCQG8a3g7tNFCSFsG1LoouYuy2akJ-0GDig8yE_-nOp4ZHma5tebhS9cJoNqa0JPQyGPMBnh_0dAdPwf0HO5EL8TJgoL2fnRyCZkyBNd1Rf45HBed69xC5kVDBeiM3MiKCVSYipYQZRCPMM5holjiIvURmZVS3yZltlrKjn3Gml1Gu3Pcwv5mZ8q4kS3AMb2X9fcgSnCVCix91kNyNu7o6LoYAoeZVt20Ny3KXEtEnwQpqQKEP0JUFp5sOXh-ZEMoF5KjkETNl4XN9vwO7AQ53-W5hHQmCLmIPoAxcKlfnBq2_i6y9IHtX8vWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
مسی باگلش‌‌به اردن حالا ۷۲ گل با کاشته به ثبت رسونده، همون‌تعدادی‌که جونینیو افسانه‌ای داره. لئو به۷ کاشته دیگه نیاز داره تا این رکورد رو هم بشکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/24604" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxSzHR9jYPEL9Po-vuy5YPmIVMjxqKkTbz7CQBouXnyhSc-FxS0RNCReX57AR9HM_VZTr9964V0iMFbo6-MXU1xMY3iYUWclg4-EMZ6uVnhW9bdYVZKE2jGM4o2NnsaFm-ZCgldJTzmaVJeLC6qP7fxGfqJmFA4BDZV1H6xMdb9TuKAKF0l2bmokxBGE3GQjWJKFor9maftwGkzHKXxsRT5FI-TElciGEXGQHgtS3txvHgtg1qPeZ8nYdeIYzEOoSwRattZTp75sWAXonAFHS88IH9rOT6MvaCne7Z9Jem1T0sBgTnnaGZ4MLCgoXsPVyX7T8Rb7rg8VOknZ5DPkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24603" target="_blank">📅 13:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=ajffm4VdZssihP7gUVfxYmISQyX--02MrPAWemTGS3eO4KzcZDCNop5oBNLzZ0OQmKzOFRlxdLDbM_yUihF5zH0OpK5L5wDXHzo7zDkZP6iX4tmRE8wUhYUAEng9_K6aNaLuD9mpyffNIWTlMi-P9jvc7JytTjlHO0JqaObyADDwuVV0jGH6OvfPFZ8gWH9lI3YN7Ns4KiT80bEqZrXTtwKVXgnrfoRatFz_F3OT2HHMmAzxtG_d7FlSb4gAtHjb39Ginxso0pkcQNDIekSiTD0bY8LdEl3HYhxkXyP3Fy0A6AKGe00xNaepqCJj3FzEmAvq9dQrHP3UzkRcXoAHbB2xX39BxN8Kw6ruFed-Sn0RfRbzUEo__aXXKl2ETK4UAjP9XLr5zwN2e9JYoHjn3mwTtz_ywtnRHtW8Oa3w_R3XBLQ9m564LQiKRVhMIs9pfRpD94lRki-zBt3ytzBU_q2PI5b8pdS4F78YPg4492WDPCiVKrpNJWSf7xg1pwe5-AeU9P6mcj3ewWZryuedKUW8ImdLRSC6_WH2S5bGY4VeyJq1zbeahDPtKf2vbYEBEAFbJLjzvU3Rj5sU7dPNNajIfjRkOD-6F1tU_B1VfQ3bS2zwG6ZfrcAX4377h7BbmFz8EDDpJCMUJZXEiKLWUQKAAygHEBb5FBEKJqCmKc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=ajffm4VdZssihP7gUVfxYmISQyX--02MrPAWemTGS3eO4KzcZDCNop5oBNLzZ0OQmKzOFRlxdLDbM_yUihF5zH0OpK5L5wDXHzo7zDkZP6iX4tmRE8wUhYUAEng9_K6aNaLuD9mpyffNIWTlMi-P9jvc7JytTjlHO0JqaObyADDwuVV0jGH6OvfPFZ8gWH9lI3YN7Ns4KiT80bEqZrXTtwKVXgnrfoRatFz_F3OT2HHMmAzxtG_d7FlSb4gAtHjb39Ginxso0pkcQNDIekSiTD0bY8LdEl3HYhxkXyP3Fy0A6AKGe00xNaepqCJj3FzEmAvq9dQrHP3UzkRcXoAHbB2xX39BxN8Kw6ruFed-Sn0RfRbzUEo__aXXKl2ETK4UAjP9XLr5zwN2e9JYoHjn3mwTtz_ywtnRHtW8Oa3w_R3XBLQ9m564LQiKRVhMIs9pfRpD94lRki-zBt3ytzBU_q2PI5b8pdS4F78YPg4492WDPCiVKrpNJWSf7xg1pwe5-AeU9P6mcj3ewWZryuedKUW8ImdLRSC6_WH2S5bGY4VeyJq1zbeahDPtKf2vbYEBEAFbJLjzvU3Rj5sU7dPNNajIfjRkOD-6F1tU_B1VfQ3bS2zwG6ZfrcAX4377h7BbmFz8EDDpJCMUJZXEiKLWUQKAAygHEBb5FBEKJqCmKc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB20u6QVJbVe94RuDRVGbosyI03CIttM6flA36ejQlFiRw8kdY9TEOsMuPB-OX263c2-civ7U25TkpeFLp81xwbCr7P6jvzvGkkyPGsXlmM54_t-z83B4O1_efQA3gppfHOs-vgmk13IKg8JA0r-5d5FUq2mzRW4QYod99oo1UlSeJrnDYcIfQbwsNt2cRGajL_xyGVxOrJ8OhxE8QhCw9ZrW9XzJok7lvpbfsy46KfCXYQofu-fG9ctjWBrZ4yf-77M8vkJfrOCS_0tJ8PLBlEQv0-IAegJ_Vl4lSCqXLqt-H8D4cHYIhXzbAyPhA1kWP8CgVWZ6rDZE-VlXzMDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24601" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=INcHkPvSgXrybGzl2xs0ufg9XPJ7s0jmITlvwIeEZ6xzkTzisyjq3_jd0j6hh9C-Wb73vv_HYrC7AHKvLtc8oECUNSKIqU6qTTiRt6K0Ro6-UEwTsDc1kiSGmaUXkXe6_eKjxlIEoShWEWo1c7JXKkvPANoTtU_EEweZehwYuYpah6V1GUodkFDVZTvfZmtoq7IAI2m0kRXIX6wFA7vxIIezlrvUJ_Jqy9OAC3vYcL2CPc06DW68q8psDky8PPlEiDW2MkPue13j4rY6JA8mJJdZwS1a0IyUu_Dk4UKgrBDWLPAw0pcmCqT0wWm7whXrwnumNvJPzaAup02xctXuRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=INcHkPvSgXrybGzl2xs0ufg9XPJ7s0jmITlvwIeEZ6xzkTzisyjq3_jd0j6hh9C-Wb73vv_HYrC7AHKvLtc8oECUNSKIqU6qTTiRt6K0Ro6-UEwTsDc1kiSGmaUXkXe6_eKjxlIEoShWEWo1c7JXKkvPANoTtU_EEweZehwYuYpah6V1GUodkFDVZTvfZmtoq7IAI2m0kRXIX6wFA7vxIIezlrvUJ_Jqy9OAC3vYcL2CPc06DW68q8psDky8PPlEiDW2MkPue13j4rY6JA8mJJdZwS1a0IyUu_Dk4UKgrBDWLPAw0pcmCqT0wWm7whXrwnumNvJPzaAup02xctXuRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌مناسبت‌دیدارحساس امشب؛
24 سال پیش، فوتبالیست‌ها رؤیایی را به‌تصویرکشید که میلیون‌ها نفر باآن‌بزرگ‌شدند؛ نبرد دو تیم ژاپن و برزیل، جایی که هیچ چیزی غیرممکن نبود. «رویای ژاپنی» فقط یک مسابقه نبود؛ یادآوری این بود که با باور، حتی بزرگ‌ترین غول‌های فوتبال هم شکست‌دادنی‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24600" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24599">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATdGWwg_yMwVuKwSWuoiGvmNvJcLjjpEkMvPF7PfXt8huXxyfW5bqKsMhyEZ1MapHShOx-XUlcfM5W73HtE8wJr_O0uTfqQQ8vFasLY1Gb3fyyXhJlLquNZCYBs9nn-xkyg2zDY-N0cLHKuEcZvSf5LkqR2bAvkniJPOyoEYf-I_OrsGJp1XVpv6otACyBUvWgDvglcKST-SHOaR2GfdoXQW7RJ7OCwMc4AoXS6sjNu58-k9o3b2YVp5K3xgMWIFO8YNCvZHNBuBA8tMlvzQeUVRw_vvyPaR_1ee3oi2Xo_otL-0gdqg9czGL1HGCeDoqNN8Al-Th9YuGMBq0Tct1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24599" target="_blank">📅 12:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMTYZZdQgaurSEknHtllWBjMizYTJD9rEReN3Db95CGfiVWrWgfMm-74da8ChKu2E4qAps7GWL_Od4UPKwMUyzJ0oz5HLovRsraljYs9DkyujMNMTrERkEuZic44gtdsoD_FNLLYd8Zh3pre2-kQwbGuDzV1-4KyLoIOqnHea3HjQpNI8l0M4kItbIVa1V5Iv-J6cLVOBDH2tvzKLMt9ItF0_vyYKZTG7xnig_kXPgz_AiPEZe14bYzGo0u6nB0alOUj5dES1-HspzR-HMZ07uKm76jKlra1PffA4n-1-dhpWQZjBfERGX_fulGkpPYUP9r2SvBe8SmpJcWvVnh0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛
پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/24598" target="_blank">📅 12:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDKHmGShm8GGzCk0aBco3NUKTMPQQ3S5GVLMQ7xCyiCzgSOI3UDd7KuNKRqFfPV_42SFzL_eOry0QV990bmjv9N_G614dJtSXz1LXFBdesWSWdMr2bEmc7DGfIReOTQeIrnzLyJkq7aCDsc9xDtXIc4aaEGRfcieYG4YzVKhiIY8AUi_Sj0wKJ10Lh1RD0Ln7lptehAsp48yuYS-yjupTtlhX2aR7MFwZaisCQ6_iD6TJbZVdPQxFh6lzNP4F3YdXsZsviqCl0Y7HV45nkH3tEPLL7jTVyW3rAleYYk54ei3QAH1Cs4VKWm2_PtzQJT64J2Mw_P23t7RDcXb3wejHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا
#فوری
؛
طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24597" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBpf5t5Zlgm1YMNNNiZCKuK3oNgA7cwZlE23T0U1NE6v3MBCtEsc1SXPhvRHJ6JuLBL-S6QazgUJ0Q95CzgYnpDIsNd0geXeiA7zJAkmq-W86yrP1fkE86KF3cSsxk6e8ikmDneuCV-rm1lu-4Fb9PT2UtKP6vSTKlzHI72wP4QVq2o2plNEAbfd4uU2LgynD7j6w_QTH_gRWvnDYRnSqztG194OxhzjzJepdYmTOLyZha4WiC3gUMHqPg2rOKynfO4pJV91B8kD4KrStOBpJbztUZL0Rl9Oq1x0f7NtQylSsEVAD-scESAPG2QQwD8hCVRkBaKsRqp809HYJF1-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛ تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24595" target="_blank">📅 11:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1mtemeEhpUiNxUXsIXMC_22TE6oj-G22zGVKa5zRUd_yGrgyj84CG5L-7hyaL5r82uMpGMPwp1DcMFdsi1vqj2YpGhmqQxpk79BiVNfoi4dPbtOmYo48AZP2NDgK89u_mEL8-w6zlz0hyDnfPeWLaBeEg__cvWLt1CmK8qs4_mWP4XdEFSYj7tR_AeERTY9dGh19HjxcNmDyTaphXq_rMc0rRPhnKWkr0RmXwHphdG2BPwpbik-NJzkj0__9qd4AtbCAbYBMQkQqKDLa_gxIhokqVUl6xzVzhHO0fKhIom6Y3KL6Ejg4Ui_E69HwzrX7hJ3Lq6pLwDHfkCeV9fRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24594" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5AKVURPYaXFuwYqaWgKSGKt3yTzj-JjTvCyYE6Sc4u-kSeSVyfW4N4xe4pIUi2DksG81LwzuoVAsFJDqAd0jkE1Gh8k3LamrdPojordU94QeVzCKO-SuS1zXIf9iUO8qkCSVOO-b8QidFdgfhnBW2G7WtXMo5flxhni0dfHbj57GYln1XxuAuwCMEfFIoHy8t9MIMGJXpGGzr95LRvq6F_BO5-6uhq5BlV1_YYkpOku1nl0Ndk7z8Ss1mRa7b4SNfUIjtLwlLs2oPRYfBFY5GisQAfqltT37mcsqqaS3K-ZZRnsV4712p04G923_1kKh_g_2oi4-DucvIG1hAtpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24593" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=BLI_Rlb0sD6-GVjVvAnN4WcQA08KEYho31bV7Jd5xm3UPg_F0WVylAVC123PbKpYn7PNi-djts-HnghPFm9dY6EhMK1tMr3Uq6uHB0ZeTiYg0SFOUDQgPKuxXoFVDhEKZ7JN9pjMOhQQT-wmeO9fHhZcLZPImLlnYzlfLHDI9jE2rhBDjSvymwgjFhK8NoscuB4E8eSzsYZ4Sah4NtuP4zIxY3WfE5xYw7FxlON4vvIZf_vd6TOSsNsrGxIQZqND1e3COMjgiZonIBbUg-vaHVKcAWYj5GK1gpvIaS2Wkq1IQwKaOJXd2Pkx9UBSFd-r_ERjFLN0vjDcKouHI3l1VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=BLI_Rlb0sD6-GVjVvAnN4WcQA08KEYho31bV7Jd5xm3UPg_F0WVylAVC123PbKpYn7PNi-djts-HnghPFm9dY6EhMK1tMr3Uq6uHB0ZeTiYg0SFOUDQgPKuxXoFVDhEKZ7JN9pjMOhQQT-wmeO9fHhZcLZPImLlnYzlfLHDI9jE2rhBDjSvymwgjFhK8NoscuB4E8eSzsYZ4Sah4NtuP4zIxY3WfE5xYw7FxlON4vvIZf_vd6TOSsNsrGxIQZqND1e3COMjgiZonIBbUg-vaHVKcAWYj5GK1gpvIaS2Wkq1IQwKaOJXd2Pkx9UBSFd-r_ERjFLN0vjDcKouHI3l1VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24592" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24591">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGbhfXgNwxmHB2mE_sDj_80L6XsrVS8nrvAOsZKNj27yfWIzUtXTAmG1S34Ev64OsbSFNXeE-rYF2Xq15tNNoltItum-biYmPkBtv0wAvK3SNigSfOqz-LxzY4vvszffJhHwgMWqRsCHRL6BmJBLVeqVyADLmtwgygtB2qeoA6fI1Wyo9VtI7CtdkJfCIi2nxVpEv0yB-Mx3uKcjvs2xTzBJbtNrCNkpic9-ROIH0n-j88OL9mUsld4L1qeqCD6UTmWlh436Sy7O97S9yG2dd-cj8iZ43jwpp9-pI6z2VPbZg_gn8PvfN2rSTTKAJLo8zU7tjF09k30FBmgxq8d1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r8
@betinjabet</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24591" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAvFbO_dypMVFaAfgQvNsibtQEmqWyPm89F4lxk0-ABkXCXYS9HWC_04qsHEr64C_C09EXVOx0btEuCHt4wEpB_guuZLjq3itLd2cO4xVO5TnExYdcUiGPl9geEYcXwe8AzMuLEBE_ZQrNsD_lNFTeWkJnNu2EXLSLLOI-i1c7j2mRGJdpN3GuJr2ROVNeuCENiHniDLG8fq0I9ueC8l2ajSLtN0NZ3kNenATr7uF3-YB_xaXl1NO6SZsk517LSRC3PVtqG3RYkPGE9XQsl0m5zhv5koIPIbXH1eZHQepP663-VuA-6dUKpaSa0MvUNOIxSOVQjdTR7dhdnj6ajEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24590" target="_blank">📅 10:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e366pt1XDYwPv_CXcLnvzEqPlzYeLs9WRaSvl7GMfYCoVc2GeRKQE6kg1H-DD3VcweUTmgwAApJd5g62dOy7a5iYfWKm04b6G9mrtMgiGe9Y8-qBPw_O39OTTCod2xzHNELB9-VvjzdIduDPFfTs137Uqb6fvXnTjdUA4es5AgjIZBLODj4YN_lzzyFC682609ZjewQmwLiizlDrnW6Y0huXj-vodVHbxn20hdkWHPrapuxN1Pm8FuGzPUMxz8KunZf5ppcWzBgGzN2p7kMdoR5_R2tsjZMRU0nA07XgmZety7fBtekJ_EUTNSOU1IzU8DbXkS3kWQBZPsUkqVOj0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24589" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24588">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=f0yDQ54C__hrf173uoQssVJrGC4nxNBlkFfTdUjl3jpyPEEP5sQ92AEBGiRQLc-8lsZ3XvLP7L7izk3ZrSzKNV4zJdBPGRz4dBJ-emzmd46mnvbVxJTz5VhtoCbyrnons0JvJ_iU4kT4feDzR9dmfQU40qODL74369U4zrrfQZR-Paihji7e9tAFf7dp9jUujaZQrGzFVL7Vv1DCHP1Xg407zctxzcDbQQT7R2bA8eu6laey3vqxNReIKMos0PhzG2tncMzWTgQoCFFVVeD5a7jR4KiUefbYZGyd45fPDaGQvXT3uzXaJ6EESPpoPiFcNuedxN1gOLtwjZsBetBaOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=f0yDQ54C__hrf173uoQssVJrGC4nxNBlkFfTdUjl3jpyPEEP5sQ92AEBGiRQLc-8lsZ3XvLP7L7izk3ZrSzKNV4zJdBPGRz4dBJ-emzmd46mnvbVxJTz5VhtoCbyrnons0JvJ_iU4kT4feDzR9dmfQU40qODL74369U4zrrfQZR-Paihji7e9tAFf7dp9jUujaZQrGzFVL7Vv1DCHP1Xg407zctxzcDbQQT7R2bA8eu6laey3vqxNReIKMos0PhzG2tncMzWTgQoCFFVVeD5a7jR4KiUefbYZGyd45fPDaGQvXT3uzXaJ6EESPpoPiFcNuedxN1gOLtwjZsBetBaOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
صحبت‌های‌رامین‌رضاییان ستاره استقلال در دوره از رقابت‌های جام ملت‌های آسیا و جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24588" target="_blank">📅 10:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24587">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=YlicGQz05uwDcfotfqgCr7EMrIp_5aPN2YK7MMfgynMV-a-s4wlG9k4Y02gp4g-amCGpdwdJ80N54eo0UXfSvj0bAYujJuhCYaDhhEZoXUY_Nw6IDlghY_WH5XnFADkaSLxG2Wi2i1CIpBNCjgn3VySC6Q8vpJ0SztEHV7iFiav7EvqXx8QxU7ytO1vQOirLLRCKcR54de6ARiS9VeouaGvPn79baNd42nnDn5ymRUZIHuUBWUwJ63-3f91JesIL55oCXa_MuoGY-HWLtQ1CTCAp6GFE9hBa0FYmcln3oZAicjQAy9wpQgRYYLBoFFYMsdjYJrDeiioLupCsnpXV6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=YlicGQz05uwDcfotfqgCr7EMrIp_5aPN2YK7MMfgynMV-a-s4wlG9k4Y02gp4g-amCGpdwdJ80N54eo0UXfSvj0bAYujJuhCYaDhhEZoXUY_Nw6IDlghY_WH5XnFADkaSLxG2Wi2i1CIpBNCjgn3VySC6Q8vpJ0SztEHV7iFiav7EvqXx8QxU7ytO1vQOirLLRCKcR54de6ARiS9VeouaGvPn79baNd42nnDn5ymRUZIHuUBWUwJ63-3f91JesIL55oCXa_MuoGY-HWLtQ1CTCAp6GFE9hBa0FYmcln3oZAicjQAy9wpQgRYYLBoFFYMsdjYJrDeiioLupCsnpXV6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ابوطالب‌حسینی درباره بیانیه اخیر جواد خیابانی با زبان عربی برای الجرایری  ها؛ که گفته‌بود تلاس کنید که اتریش رو شکست بدید‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24587" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=j6lwouodyD3Ela_MVLgv0RUPuAQIfJmzoYrxnYmAJ8JTgLD_HMdhjawPwQ7KH6hpF1u-qF8i7FZYSI4fAg1BwlT37b1wndvHW-6NBFW0WPeNQWFCzhUwPEQHWCr-J1V1gZZx3qUU6sz1NI2usncDiPaH1YZF-6FLhbZxIFVihY2fyjTyf4RQAWbd4MtRzrNSxDx6JE6N0oV3B5-yh_E2t6N_3P92sqOATWRFfUnW-ERJba40M4CyQ7MpHTb6fe_AVj6cUWw-OLAnLFZi6YynXCnBjVng6LVlO78Eh4Iv6RcVZ9du9TDDMshLKhPANWHLouL_83a6fxo67J25niwSmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=j6lwouodyD3Ela_MVLgv0RUPuAQIfJmzoYrxnYmAJ8JTgLD_HMdhjawPwQ7KH6hpF1u-qF8i7FZYSI4fAg1BwlT37b1wndvHW-6NBFW0WPeNQWFCzhUwPEQHWCr-J1V1gZZx3qUU6sz1NI2usncDiPaH1YZF-6FLhbZxIFVihY2fyjTyf4RQAWbd4MtRzrNSxDx6JE6N0oV3B5-yh_E2t6N_3P92sqOATWRFfUnW-ERJba40M4CyQ7MpHTb6fe_AVj6cUWw-OLAnLFZi6YynXCnBjVng6LVlO78Eh4Iv6RcVZ9du9TDDMshLKhPANWHLouL_83a6fxo67J25niwSmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
فوت پسرتازه متولدشده کودی گاگپو ستاره تیم هلند و باشگاه‌لیورپول درکوران‌مسابقات جام جهانی میتونه بدترین‌خبرممکن‌برای این ستاره هلندی باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24586" target="_blank">📅 09:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👤
واکنش عادل در ویژه برنامه امشب جام جهانی به حذف شاگردان امیر قلعه نویی از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24585" target="_blank">📅 09:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuRv5Ins90NIgZNoy4K0HNVwXDNReYAHzJdmw5heXLkYa0LUTEyw4qqvA9QfbUO3KVi5QYTMEWJx6EwI2NNdfY0gva_ge2XomgUpP_Dj562FxpCz4n9TDxvZU7rtKD5UepDWMkTSICq4hA_tVkC9L5GQpLfI7cwJUJKiaJEDeFAyhjjCKNa3NCVOU4JHf1OlQiUY88Psz9qwl5wiZUNgui6fHBYZR9GjgJQ5zURyQzn9vZhLhrkz6hoR9kAUfoV5m1Wg7JbiV0tqsefF_yzbRpoK5WTOPdyoZd5V_4MZJhV52S3j-iKfc6z0KERWzxDTDuw5MZr8VHc65q8R7BGBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24584" target="_blank">📅 02:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4T2rS0nCT1Vjvz9aFjRu_-B3vZ9I1itg7-9LySyijTcD_0fuNhjoq5JEz1MZyLQM021cwmj8HLQ3dNfr7o14NDzSXh4wsYzkSPxcMEdiC3vJ7KL6s8ZLoNHDkdT8kFz4uWATzs1c2D5OQAkgjj8Ul_Ny8sQElsW-zSONnkT8jJvG3ZWgI-R9Z1_InBvWeg4sSZyAgKpbLvj6ROdsdCybAIBke15J98U3Y7BNsSFLGwpG9oLcIa7psnRTZPmJmJIoTNlJa34fGrZAMxtWhb2QgxEKi45PJoC_HZT0ioQ7bpdK0KGqx1yD84dvWteV2B4p_SfAbJpztGYfgrlxMhEGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان با گلزنی در دیدار امروز با مصر، شمار گل‌های خود درجام‌جهانی را به عدد ۳ رساند و درکنار اسطوره‌فوتبال‌برزیل کافو، به صورت مشترک درصدر گلزن‌ترین مدافعان راست تاریخ جام جهانی قرار گرفت. رامین رضاییان: ۳ گل؛ کافو: ۳ گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24583" target="_blank">📅 02:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9CLEqJaYNcI5iQywXd7TyMPvm6ceQ15lv9DUoj5EC8FC9-e6SvkEAlwwFveNS60R4gxaHDUivItvfcNKx0wRiXGl10vlUOsfVSqsw21_WzyyEHzkEfQ9bty4BxRB1EMs5rI5IGs2c0DMT85uij2TJ_-R4aX7zXHzN405DkLRJuiY7DIoVlmfCdBIS2dM-WvfCCJWkqV0N8m-Yk7BW1_wjy3O2jXH7w9diyhWdde24NS9Xbt2ytjmzs0XoQDGywSQ7sMvB6TInqba4hy19suVkiOetoJVbovocoV4-oz-wxW9HQ-sLUPpalVwZy7_vLq4t4gInl4fxHaeiF7_2dF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24579">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMvSxci231zIxnzu2F6THH3wOV-cfQtad5uez_0Ywwm9M287qdJ8bzd8ijo3Px9Jowd23Z6pgxajLTe2vfAURRWVpJAHrZlaeYMBkCgQ5WlxW5XMrWhikRlQSXqwbG-BlgEbKStqxgbLsCrMHKAYqPSW9Snd2MKUABQ-y_jHuTihhpc9Zj3nYttmzbrvJjpaXhMOhC6kuPsldtxItiZOG9xXOdBo3gzh_Nkjhwe8rqWeXcUqMW2LjnoVpbg2KEIhoa1P8fYZGB-WpfGvA56yrCZLRIzv4duxZk5UAGsm-YGllu6CLKdAWj_mJR39qfygeDl7F7UuyhcBqYFlmE-g8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24579" target="_blank">📅 01:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fww-KJHWp_PP9mFBM75xuZi6TaJ9qHq2W2s8WTheZb2lbG2ka8ap0TiGao15sNd0T5lKNifufhQypqMA6xipUs99-wfkxk4_5SWc4wvTvepN5ToA8FXgV20ua-_pGBQuuSsy87HO9YUgkLzCFS6HVj76TQHaGjVzN6V3PlukTnr8KoqhRwRWrOmsAHO53AlfAuxNT08EaEWwXKaCF-oBUDWY86DW5la3GCHxLrJZHtvcOHIEyoGpvPQ0GSHPiY_srQEh4Q-cGQeeCniGUxlrXgEse5w6ILfuvpLqgv1Tt6-PBzKjVQLUczLbzWlmVKwdi95Bq_Xy_036NnHzcVMYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛
تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24578" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USflOvMZ62vfKKbKi3OVoto2zMDX2Qkxm2Pml75ysxmOu6GMcLgENcFsyfJFmfSNLz8_8SOY_uaTUsU0Ze36tdSFLyOi3hMR9h8E7ByENwq8OPXE0JGIUOowc8DAOjS0V85U_QjVO_iUN6_LUdXsXMtBaxxkXn5lzEhLWWe7ketEm3hkOZ3E0EIw0IA5DCmvJQ7bbCcAumW3Au6VabOuekh7Jt0P-leqJZq8dLbR4uU3s1dGMUL5za6r8L-8p4w6iGTlypPbE3zTK2qNxZzxr_1WWI4kBPy9mqEsAYut-G1Xo-jHNZ3FrUui2xIIvnNRfxci2vDfVSBGMOb8ADqdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف بدون گل در جدال کلمبیا - پرتغال تابردآرژانتینی‌ها درشب گلزنی مسی و راهیابی کانادای میزبان بجمع 16 تیم برتر جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24577" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNY8TrPmofG4s2t1vGX5J8egTce-0QF6oCq4sAE8aGzXc9WjVt7khaGPMQCMAQSa2wpLotnM5E6MccCjFwyyAO_eL8fYaq1JriVCkkPlPysfV8ztLR4AHD1-fFmGjDvZO3LHnvoFMHunkAYE5rU3jLha6sqQ9Rhn3rA8hK8_HYQuBxmletJVRWsjqP6gB1x2nITqaNDz2VaGME9X7OQnuUkVpt1XvoYpfqKI9ylbwogcpAIN9YAr6BE8wSnpCRqkTCQRCF7MkzkLam7iIyjAcZc9xaA0li2swHd_VSCFcqgTSY3JK3cuCHxKEWXHqJEFNjfFCJQVueDam6qHI0yIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24575" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=cX-if9AXycuwZNIuxCtfojWjYg2_WuuwoJKJi1lurSWS-yVBhd1W70gq9zzWDrec2yone_TwMEylu-fucS_KU6JTjeIvSfO1uFGv9qVDTJLfbCSRjTkPmAB2s6Uxav4mgl7tkTvEjym2MeKy_KtFU2aXvxRUO9wOaHEOAOG2feSwf1vPsQaqIGF5IOvm-EeyeNeuJ1Vnp7Ih0iVTlQThUBVZ6B8loPT1e-gEIpVyZX1YMDipwM_KOwz3G8ZuiFN0E1n-rJB7e57nFIfXcd6UVzIZsgdL_EKkP9ws8sKoqXEOHdvl5Kok-G-_gm3pOkUfCFLWBbFaK86cp-eQ2xeodA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=cX-if9AXycuwZNIuxCtfojWjYg2_WuuwoJKJi1lurSWS-yVBhd1W70gq9zzWDrec2yone_TwMEylu-fucS_KU6JTjeIvSfO1uFGv9qVDTJLfbCSRjTkPmAB2s6Uxav4mgl7tkTvEjym2MeKy_KtFU2aXvxRUO9wOaHEOAOG2feSwf1vPsQaqIGF5IOvm-EeyeNeuJ1Vnp7Ih0iVTlQThUBVZ6B8loPT1e-gEIpVyZX1YMDipwM_KOwz3G8ZuiFN0E1n-rJB7e57nFIfXcd6UVzIZsgdL_EKkP9ws8sKoqXEOHdvl5Kok-G-_gm3pOkUfCFLWBbFaK86cp-eQ2xeodA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیابانی‌این‌بارگیرداد به تتو روی‌دست امید نورافکن میگه حالا که‌اسم بابات‌علی اسم مامانت چیه
🗿
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24574" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqpJDMOX8h4kGrMYV7RvDLcjjI9Sam5FYiYQ4A_m3Gr5w_k81XFL_exMU4LcDS0hGN56eYwTrHKzFa-OPLlCzX-DLZyXr8eAsT8rzTzZqunG6zvmqUzYTNagmuCdGJb2pcJ9EQ-zvZAFekuH14JalOVpl_dkIDYTPyzlWh_eO_Bkw_zdjmcn62uGhdlOZAM5CspzOSzN1YIyzonhSVM59DNtoYoZrvCuQO7BXf4thQQ6L8z_en1k2UU9g9NNPP4x8d-VUpyNopFymbBP_RjH6-4gt29ER9vyNmUgoB54hILgL1CoP_FCTuOfOQp4669niVx-qNg38uziDnxSSv_wlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
👤
#اختصاصی_پرشیانا #فوری؛ مشاور محمدرضا زنوزی مالک باشگاه تراکتور که در نقل و انتقالات اختیار تام گرفته با باشگاه اتحاد کلبا وارد مذاکره شده تابرای‌گرفتن رضایت نامه محمد مهدی محبی ستاره ملی‌پوش‌کلبایی‌هابه‌توافق برسد و این وینگر 26 ساله‌باقراردادی 3 ساله…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24573" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24572">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oo2iRMmmtf9ZXn8Hf_AiKUv2Qi1N3wWS6myz5on7DjdgOQyPBdO-VJOhMEOGfYzJeDPaHLG66v-bQs5kOGQRDHtgJkI5EYBEO4Y3CNgwTDd9oRfcpu3YXkHW8azNJGHTweqXKht2JuhgJ-qbNWiLo5SFpEvx_4ePF-MZAzx_2ZCZ52oJQusOuAN95ex_5V2FHuVP08route1Wd_ZD30biUwcPAmr6U43KKa6XmbDdS87mb6Cmw7NrtWpP4LwfyG0Gg-I4lGM8zmKmtVOnyz5s8FjYnFjm5EwfwypXxAdDHZOK5HqX75_hh7G6mCaFVzSVJRKRAGmrb3_FTaa7PQtuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جواد نکونام در کنایه به امیر قلعه نویی: شرایط جنگی نباید بهانه شود، عراق سال 2007 در شرایط جنگی قهرمان آسیا شد. پ.ن: این رو کسی میگه که خودش بعدِمساوی‌تیمش باد و هوا رو بهونه میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24572" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24571">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=SQZ68o27p1KPnuNK5av9ISzNHG5u8xwYM1Zj0bBDv1bet3TYggsA_g_QF3tQZ8JarPjxT_w0HYkOC446flPRNRspxAnLtAXabtkE4FvJ_dAZ9PG4uvEtY82W_6KmE3fukIYWwG9xKOWOH1tqLE_cFnrO6yirnDlrIBouoATKwUCn-pJiY02x7MS9daN22Abn4pJia9aQclZVri9c0TqCrqM1nlOOgxcs2o8gORPQ0e8aY5pg-qprsxr9ZshmyW1-GBBdaSstahG6HeXhdILDZ_lOsVjgb6oqTPslVTvpBHsjTl9FZoDBGKVJ0eu2eGGkOdiO1pczpTr4ki0lAguVww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=SQZ68o27p1KPnuNK5av9ISzNHG5u8xwYM1Zj0bBDv1bet3TYggsA_g_QF3tQZ8JarPjxT_w0HYkOC446flPRNRspxAnLtAXabtkE4FvJ_dAZ9PG4uvEtY82W_6KmE3fukIYWwG9xKOWOH1tqLE_cFnrO6yirnDlrIBouoATKwUCn-pJiY02x7MS9daN22Abn4pJia9aQclZVri9c0TqCrqM1nlOOgxcs2o8gORPQ0e8aY5pg-qprsxr9ZshmyW1-GBBdaSstahG6HeXhdILDZ_lOsVjgb6oqTPslVTvpBHsjTl9FZoDBGKVJ0eu2eGGkOdiO1pczpTr4ki0lAguVww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب ابوطالب حسینی درباره حذف شاگردان امیر قلعه نویی از جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24571" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxA_NJXjtW6NsAo-AXzkALMgmS4FQEBAkKYjjdx0QX4YxXrrSmuiOXUsK8i3y7IRK_IcmnKXjDEk5iEgZNMbuvSFPMRfMvjYX71yBTw2jXoSbwy6Xlkr1YGQqRjUnet47PafcbUTlz6mrFcfy7WQWcAhNHsb66rWf2-f-7jcA2qObL3GfK_D2WjmYp7yg4r2ymPYlHiFNSd9cg1ST0kallf4Il3cJ2pqeWGLu63wQLOtcDQ9Uh0beAMZr0pgi1wQkoJdkMe4Ga-DXIu4meDYXc5vk48S4GwQoZLxoqwGM-NsBr1YRTDgvOVeHTFuXjbTM60dmfwr0MOPfxR-JrKRZODk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxA_NJXjtW6NsAo-AXzkALMgmS4FQEBAkKYjjdx0QX4YxXrrSmuiOXUsK8i3y7IRK_IcmnKXjDEk5iEgZNMbuvSFPMRfMvjYX71yBTw2jXoSbwy6Xlkr1YGQqRjUnet47PafcbUTlz6mrFcfy7WQWcAhNHsb66rWf2-f-7jcA2qObL3GfK_D2WjmYp7yg4r2ymPYlHiFNSd9cg1ST0kallf4Il3cJ2pqeWGLu63wQLOtcDQ9Uh0beAMZr0pgi1wQkoJdkMe4Ga-DXIu4meDYXc5vk48S4GwQoZLxoqwGM-NsBr1YRTDgvOVeHTFuXjbTM60dmfwr0MOPfxR-JrKRZODk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24569" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuflv2FdMXZohqrKaMH7QGp2Q9fQGzpexpJSBFrd64TNAYkzx1XQ0CCNaZBOQJAfsLEkeEls0ZoGEv8zomziqbRp2u83k9huIfAjgqkF6nSyJ7WSCA7vjitVfNCbPGOZNLLBfVHi6-DKPpSnMXIbtz4wMzsVOhiWvAeWJ288uWTzrD9vtzgRl9-cg7SEqEv_Wl5XW4CcRVKn_ybVNaL9gpU9J9triCeXgturJROowl6T6luPXzkjb-dl9pAD_Bb28D40ahXCXCt9A5UUPlcgvKxrcrZAza9x7EQZqnuq62D79XIy6k3wW6K-dwK0R1GAgqwc0hDdxCUdNI7KYFhnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24568" target="_blank">📅 23:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=dPTIAWTrecEBRMGPWobmSVQiTk8Kt5cELVCU54-LhdyLpX9RgJG0RunddyGbKFwG_KjZliwms7kvAVJpYR9KSwaBXgEu6bLjTFS_EfGFFnEGY0_-KiB9P3VW-QzHa0pnaJOe8ELRAav6QdKeukqS7fsIsXOeQ2FTGsHAF-fpd1m3yYOCL2fJW1wHUH2vmkkvgWD6FLQGQHccsEdHhLR1DYYCt-dgDhrsIZqjUnUigY9qUsKiY1P5mOMf61uSBU5z-GijfNmCb7peVlWcgcXGeSXfdp6-Qvc3kZKxzGum6cAaNs9x7EBrlrzZNbU4xZG374siwN7Ng_UP1Ph7kSpGQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=dPTIAWTrecEBRMGPWobmSVQiTk8Kt5cELVCU54-LhdyLpX9RgJG0RunddyGbKFwG_KjZliwms7kvAVJpYR9KSwaBXgEu6bLjTFS_EfGFFnEGY0_-KiB9P3VW-QzHa0pnaJOe8ELRAav6QdKeukqS7fsIsXOeQ2FTGsHAF-fpd1m3yYOCL2fJW1wHUH2vmkkvgWD6FLQGQHccsEdHhLR1DYYCt-dgDhrsIZqjUnUigY9qUsKiY1P5mOMf61uSBU5z-GijfNmCb7peVlWcgcXGeSXfdp6-Qvc3kZKxzGum6cAaNs9x7EBrlrzZNbU4xZG374siwN7Ng_UP1Ph7kSpGQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24567" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏐
دربازی‌امشب‌آرژانتین - لهستان در لیگ ملت‌های والیبال ست اول این بازی به شکل برگ ریزونی 50 بر 48 به سود هموطنان لیونل مسی به پایان رسید. قشنگ به اندازه دو ست تو یه ست بازی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24566" target="_blank">📅 22:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDV-UYGzCVEAUuUxXdFX6noobObJxaJr1cy9ct0dohwaWIFRX4v0u7qJjq1S7rE0iPtZoHAml3YbOjPVf5AXvF8n2ytnNw2gnOaeHroZ1zdTTjOFOOzeYafOV6zeidIuq-x3L5H0C_dRaUvXUFrfIv1DeSRg2rm-DjRSkyXL6q5jx3nv2RfFSY7QKKKhmVA962k_3CzGxfhUWBazEkmcWCso_UC3gXsP76j1pQcfxgziAvcBgxdCg6tpib9VcTmIKsDEp7i-9f2wsGJsZbE0zjqbG6DgWEWXoyq86sQDcJ9SB9WDeVr5FXcDxstW011TMOsg8Z8oXBEwBSpC3GS9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24565" target="_blank">📅 22:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=Lqgbvde7ZPk17-18NqqEwU-c_SyWHFYxwKJkgKEQmjGo_AtCegyqL4e4dUPOnP_kvNDcGJ3O4Uj2_P2muzOFY58lKII0YsV4zw5OAEMD7OMWQTX3oloqHkXCgymaABz2nqOwv1uQ8VyocGTaNbHgjwbyByNb6BKlgD_yw9HsuXLoMLndRFB2d1P9fxPc6mUdTAelkKw_ujriCCxCgwwa_Sr4g4XMp0JalFHlI8Md8QkS3p_xwTJO_9NJhCJuCXlTrzwHQKmSAQxyX_4LIal8ZBTqqDq0YO6YYDV0A6f6M1MAZ85TOUhSjGN5N4QSzjXzl0bxC8Yjw7vWesPuO0pJkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=Lqgbvde7ZPk17-18NqqEwU-c_SyWHFYxwKJkgKEQmjGo_AtCegyqL4e4dUPOnP_kvNDcGJ3O4Uj2_P2muzOFY58lKII0YsV4zw5OAEMD7OMWQTX3oloqHkXCgymaABz2nqOwv1uQ8VyocGTaNbHgjwbyByNb6BKlgD_yw9HsuXLoMLndRFB2d1P9fxPc6mUdTAelkKw_ujriCCxCgwwa_Sr4g4XMp0JalFHlI8Md8QkS3p_xwTJO_9NJhCJuCXlTrzwHQKmSAQxyX_4LIal8ZBTqqDq0YO6YYDV0A6f6M1MAZ85TOUhSjGN5N4QSzjXzl0bxC8Yjw7vWesPuO0pJkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
دلداری‌دادن‌کریس رونالدو به رودریگو ستاره جوان رئال مادرید که به‌دلیل مصدومیت جام جهانی رو از دست داد: باید صبور باشی تا موفق شوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24564" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=ACvNodPPjQzHuPMtt8HcBuNTrDCKEUHG02p-tP_lvusrzuEIZaldAIXXOHIXiLQGtvT7DynnGgUHsdACp2TghXSTjP5jd7e6pBrcc_35xUE6UtcTX-uq2a2nT7jrzFxUuP7qT1h0AHbNajSbFWLdOsIxhUGeddAVYyB9N297iLbYAj4mMwi_dJvxTfIZ9IcBnNaAptJ7i2YS0yTP92BSCxudkHMFqnWgXfO5TwweI5a9cx0-kObM8dfraaU9PYVouuBDhNImTTKwayEeauzggaC1Ij80VfSAYCWZKDF3TOSAvuJLwrkNWuC9P20g0bBqL_tgnNfjJB0leDFZteGRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=ACvNodPPjQzHuPMtt8HcBuNTrDCKEUHG02p-tP_lvusrzuEIZaldAIXXOHIXiLQGtvT7DynnGgUHsdACp2TghXSTjP5jd7e6pBrcc_35xUE6UtcTX-uq2a2nT7jrzFxUuP7qT1h0AHbNajSbFWLdOsIxhUGeddAVYyB9N297iLbYAj4mMwi_dJvxTfIZ9IcBnNaAptJ7i2YS0yTP92BSCxudkHMFqnWgXfO5TwweI5a9cx0-kObM8dfraaU9PYVouuBDhNImTTKwayEeauzggaC1Ij80VfSAYCWZKDF3TOSAvuJLwrkNWuC9P20g0bBqL_tgnNfjJB0leDFZteGRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24563" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24562">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chrUe-1e9sAQRL-KebZq64T8JSTMHkkQpQNpbpIdi_WF3c3_CnsO4dtkfe8JoshWL0zK_AIv4HpbiWKce_ZZ5I6Rr9IyiK0i7VDNyu3YQvnfMi3pmRt0t3-1vN89kCkhjR1VFtVky0Sw4r6U10QzRX5K06Cxl1K_YUyvEd1Wy0zG78xqMplyKv3kwPgAoO3CD9-Rj5D1ldSC4d_x0TQ5yHy1b8a-abGrVp7eViOlveI7WE7uAlGdMDBsEhm6uHSPckfpy6aJIK5EOF7Z1QgW-kUh-HDq7dKk0RCsF7NnWS7wTEAEKLDdjQHbt67Ivrq4fImZYjrmD6pghjrRJlg6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار کامل مرحله حذفی
🏆
⚽️
در بتگرام پیش بینی کن کدوم تیم قهرمان این رقابتها میشه
⚽️
🔝
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24562" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=r5BBsxpepmKhIWlloBYZ-yFOlNdnUks8KwLk3auIxDa2BKQdnItgDooUKxYOFkZphfJjsrXcjJIMVvMEZTBws3EHhCxs4mpUWEACZDtU2_Np8z6cjTYE1qHv3aIV-ceIApXjmtN4Bv-EDgM98w68ine4vzBgzsOHg3EY_qJdz9JQqp30Iy4dWJpxm3_4uEYMUaa7jIyN9dVz7BwRPVSwrEjIPG4zWIlVoEBdkNGfbJbUukeoAuvqXamnXg9w5itGHQcZPJjxprVfODeEIIm_m2YY_npra_KA_XBITUL__N41q-asdhSXSMzTRQUynBhr2zFay1rz80alxxGS3zp6Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=r5BBsxpepmKhIWlloBYZ-yFOlNdnUks8KwLk3auIxDa2BKQdnItgDooUKxYOFkZphfJjsrXcjJIMVvMEZTBws3EHhCxs4mpUWEACZDtU2_Np8z6cjTYE1qHv3aIV-ceIApXjmtN4Bv-EDgM98w68ine4vzBgzsOHg3EY_qJdz9JQqp30Iy4dWJpxm3_4uEYMUaa7jIyN9dVz7BwRPVSwrEjIPG4zWIlVoEBdkNGfbJbUukeoAuvqXamnXg9w5itGHQcZPJjxprVfODeEIIm_m2YY_npra_KA_XBITUL__N41q-asdhSXSMzTRQUynBhr2zFay1rz80alxxGS3zp6Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌ های تامل برانگیز آیسان اسلامی درباره باخت شاگردان امیرقلعه‌نویی از جام جهانی 2026
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24561" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=FSR6tgoRVUqMYRTYsTBwU5khigqocF6CatH41oiDelDL1wNvs8akFT8OVO6ERLPrlRuXLr4d74jm7nt2nGdRIt0syVHkx8X0GsJPku8IHhpQITQN6gqFElwxtK-8JJFQMU6_fujtPpsPaKFqp29RMYWJjfhJZpnT7Ib4TpRDU5-SY8HTB6LZF5V0adGiHMBZGtnnu_efyOXtomyxDB0s6hzGjspHHfXXrKIXBa_OgCYiCT-kcncIk-KkJmghw9HN5Q_FZLt3iPGYxA8sAdHLlSH4x2jwYKMQzA1YA8HvzqEBckrhzvvK1W4CoQoc1mMQhHJcJZ29qxilF8gh4ZDOyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=FSR6tgoRVUqMYRTYsTBwU5khigqocF6CatH41oiDelDL1wNvs8akFT8OVO6ERLPrlRuXLr4d74jm7nt2nGdRIt0syVHkx8X0GsJPku8IHhpQITQN6gqFElwxtK-8JJFQMU6_fujtPpsPaKFqp29RMYWJjfhJZpnT7Ib4TpRDU5-SY8HTB6LZF5V0adGiHMBZGtnnu_efyOXtomyxDB0s6hzGjspHHfXXrKIXBa_OgCYiCT-kcncIk-KkJmghw9HN5Q_FZLt3iPGYxA8sAdHLlSH4x2jwYKMQzA1YA8HvzqEBckrhzvvK1W4CoQoc1mMQhHJcJZ29qxilF8gh4ZDOyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یادی کنیم از این ناگفته های عادل فردوسی پور بعد از تعطیلی برنامه دوست داشتنی و محبوب نود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24560" target="_blank">📅 21:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb_THcj1NuxD3403a8IDC5jb3M7xri3iDv6qrGF6kCeAXIhbWJBA5XxQK94NYX6N6otVXEx8_M2ZDUQmlaJbXiLlkx7414EckEvyGi6LsWuNLnhZubXRHu0r5BUP2iGK_cqSb0l_gtRO4xynjYgiqq_a4NoO1qDuEH4cCtYHso2rD9wlkvmh09eUWsWBtoEKDsCZtcsw2VP6ESm_euNGhxaSt973FwpiKOfUPgtzqLoYZljqHBI41Ir7rGybm9yMIV1zIgNvgPjA6OTyDa6aTTNLzLJ94o_H3oh40K6AdkKw9Gw0xJsC6QF9zTeOyWQuL3X4bTn11A0QEfnW0PlPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ باشگاه اتحاد کلبا به ایجنت محمد مهدی محبی اعلام کرده که‌حاضراست با دریافت یک میلیون دلار رضایت‌نامه‌این‌بازیکن رو صادر کنه. مبلغ قبلی که باشگاه اعلام کرده بود 1.2 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24559" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLbu4nTEg3KS2awQt1YNTF4w4slZypy0G5tVwTQNPQ5R8mX-chNhU-bp-XDPVsSg90LadOHmgY0H8tM9kz6DiqP-T3y03rKqZaDNTHNSchsIsbP7aQ9su2N80oc6QVzntkcWZRMJvZ2xauNN4UbpYXFzzEFeFKoCUmNOZvpFMJWWWLof3x2_tjY3Y6lq4meQT2bhNoipJ83sZimGb4qJHA3pj1cByx2L0mpHdBAs9-HKNBDtdAPy4eX7l6idnYTzjoKDpxoKQBYDBkoiVd3gQc9Ih5sjtNrVb4hTzDrZSjKrFfiX04c7ttLORoYF54nfdMrh9K-5cBKaKjqpyueggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه سپاهان 72 ساعت به سید حسین حسینی دروازه‌بان 33 ساله‌فصل‌گذشته خود فرصت داده تاتصمیم نهایی‌اش‌رو برای موندن یا رفتن از این تیم بگیره. مدیریت سپاهان همچون بقیه بازیکنان از حسینی خواسته رقم قرارداش رو کاهش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24558" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkSZv6yWr0IrhSrZ8N0lVTPimIp2H9fbQT_JdwMwLCgNgoA1nstMoXvV6fQKvxH9bOC9eL38__Xq_VXT0q28uIcmFgXUg02eXRnOLbx923zyZVI9HX30FTMn31g9MS36NRCfoy9PLp8csX3xKDMT_ptGfmYxGKoi_WJYNjVBGowUMcYQ2dpgrZvQxxgvxM5KWA5fHs2QZHbFg51IrYIFs3OL-b2-2OM57MyaxQDP23XpHqoNN-IE2b8nEuFosb7HLcpygGQA1bXDG35T78BRcPsKV54CkIQmB0D7E1RGJo2DNtZC4RcE1DSwJW68S6SaCl8srSkgb9VXdOYf8TuE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|رابرت لواندوفسکی با ایجنتش راهی‌آمریکا شده تا با باشگاه شیکاگو فایر مذاکراتی انجام بده و درصورت توافق نهایی با این باشگاه قراردادی دو ساله به ارزش 6M€ امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24557" target="_blank">📅 21:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7Py_KuDFKvreSSEug9nhiXXeqEfbbvrUw6BG1CFrEwsI4gtO4gWzC_p_ft62VGDgOZbd6NSJqSWuA9w4gM3nXqusve0fLtttTvvrmB9r_BTgQ_TI96flA93ivRhO2NEfPZU3S2Hh4G1NaSnnlv6DAUzvLRQPm09GbFZX13d7T2ux1UO4aYWIIqI0g02DN_t1Vug0WKahLI6T8bFUyZ5j0WCUtnwP46LdhHmGMG5D6erMpLHsMU5pKxoZKOIy68N2dGDWfGqyPN8MzZJqGXhpTGn8HZq6QL7yF7QmUluCF-C5jeTDgF_bvYHfe2wLy2oPPq5rPkPTwb9M0kPImRV9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🏆
#تکمیلی؛ سرمربی تیم‌ملی‌کره‌جنوبی بعد از حذف در مرحله‌گروهی‌جام‌جهانی ضمن عذرخواهی از مردم کشورش از سمت خود کناره‌گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24556" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=lFz7EWityqSOnoEttK_8HM2Q0zqqJyIcB1cl_BzILHhCxeoOu-osz2CG6JL9iFxwOzH7usxSONjXu1jP3n1Pi-kXBy6LHQAEK75UCZGAfrBV4qMBHXE79BJmSQ76n5q0Dk-Koh8hABKN86NnQnTaWDU2lGVf6R7Sq9FOc45M6v7y5Amf46kgjc2sfn7UcBROsaKu1ewbWlG-fy40pfltaA4zwgPixkRXJENPNzWVOL0LosVg2RleiebQ6jIwU6cJKRqSahNRLSjcPidmQ_PEN6GRlw8ZLhtANf01-lE3ZfVW5p99yWI48qyNLPWxgq5SG2jXdPLxKxNhEkJ412F6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=lFz7EWityqSOnoEttK_8HM2Q0zqqJyIcB1cl_BzILHhCxeoOu-osz2CG6JL9iFxwOzH7usxSONjXu1jP3n1Pi-kXBy6LHQAEK75UCZGAfrBV4qMBHXE79BJmSQ76n5q0Dk-Koh8hABKN86NnQnTaWDU2lGVf6R7Sq9FOc45M6v7y5Amf46kgjc2sfn7UcBROsaKu1ewbWlG-fy40pfltaA4zwgPixkRXJENPNzWVOL0LosVg2RleiebQ6jIwU6cJKRqSahNRLSjcPidmQ_PEN6GRlw8ZLhtANf01-lE3ZfVW5p99yWI48qyNLPWxgq5SG2jXdPLxKxNhEkJ412F6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌ازتاریخی‌ترین گزارشای صداوسیما از رقابت های جام جهانی که تا ابد ماندگار شد. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24555" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24554">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=OH2DOpWUq_82rSc8HUYBHTsScfU7hDQpUEgT2IhLKC2r2P8zRkwGE6JQF8-AW-h989oxMGva2j2rTtNpM8M751fwUNZ4Mu0xINqPdHmgWFq-jen7AVm5OhzGKTATNw6Zeg3y02x27LZaMleNmkY6xLggovlT4IdQ8AGgEB44yUlJY9l40Ayydaja4nlkkYI8aooj10YXgE-EgCJtFFBuG0KE-TMdEkGdU6kX_0TxtTPpT_GQWON4ZGhuo6W68vaM2_9YJspIiLPvOhgltiexDzpujrCKkCiNQ5YvGnUGfGIDMLt6UCZNsCla0IyG3nsnbnlNPtgDYCW7VdXVmab_Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=OH2DOpWUq_82rSc8HUYBHTsScfU7hDQpUEgT2IhLKC2r2P8zRkwGE6JQF8-AW-h989oxMGva2j2rTtNpM8M751fwUNZ4Mu0xINqPdHmgWFq-jen7AVm5OhzGKTATNw6Zeg3y02x27LZaMleNmkY6xLggovlT4IdQ8AGgEB44yUlJY9l40Ayydaja4nlkkYI8aooj10YXgE-EgCJtFFBuG0KE-TMdEkGdU6kX_0TxtTPpT_GQWON4ZGhuo6W68vaM2_9YJspIiLPvOhgltiexDzpujrCKkCiNQ5YvGnUGfGIDMLt6UCZNsCla0IyG3nsnbnlNPtgDYCW7VdXVmab_Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24554" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuUWvIh-TqyaVmkXtVWmGRQ59k32XjTaj785XppzmWchbh_CHmkZexAHXrOwduRwrv-BUbAZgbjXjQZHYEk2ojmZ6T8s1h14LddEurwPm8IZJHxsmtdX8PmZhDmj3WWLDmPH6xw0jhQm9kSmIYxqbwM_kfHjNQWPq1AhapOX1CHG0hRzzQjoeNSSO2IF5RFhQbjjvNXSiSXtkXg_tzokvFPPKJu_4BTr3VFBSdSUAB-WBCmRhxAwEvvSRo5ZbLwljVke7AuyXufoGxXeghdFCHkHfqVO14Hm5xluqqZtWyWRMsR6TWV5ix3K20xE_26EVXOQplZvZ00BNvhjzktHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ دراگان اسکوچیچ سرمربی فصل گذشته‌تراکتور؛ بادوماگوی دروژدک ستاره گلزن فصل قبل تراکتور صحبت های مفصلی داشته است و درصورتیکه فردا بعنوان سرمربی پرسپولیس انتخاب شود به مدیریت باشگاه خواهد گفت اقدامات لازم رو برای جذب این ستاره کروات 30 ساله انجام…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24553" target="_blank">📅 19:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030de140d.mp4?token=cI0ZwIK8Vo2ok-m7FkqOolcnpY2U931OXimLT_mf_EG8FPx1itumPp4QKbYbTKPe2ARByQtGdBT1_CAxOvFPtFd8prUWw-V2vDdqVKeh7x29l1lGdAQc7-uLm7UjmnO6abUDtTb9LzV0gDyFkCvrFlwuGLBe7tMifogAK-R5lat7JRuckLqE52vJXhPSCQ3ziaK0NV5y4rOCjm35EGASmGgO_qDtkQ_cZpdTVzkwRq-WR_DFPrJkuLotc6r1D-pzpOWCFAFWShZZHdbIp5Br5XwJGu4B-NSj9Fw3W9xSCXH-onyr2O-AsmRwMruOv-hS_p0YHFvdi5xkhikFPbimYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030de140d.mp4?token=cI0ZwIK8Vo2ok-m7FkqOolcnpY2U931OXimLT_mf_EG8FPx1itumPp4QKbYbTKPe2ARByQtGdBT1_CAxOvFPtFd8prUWw-V2vDdqVKeh7x29l1lGdAQc7-uLm7UjmnO6abUDtTb9LzV0gDyFkCvrFlwuGLBe7tMifogAK-R5lat7JRuckLqE52vJXhPSCQ3ziaK0NV5y4rOCjm35EGASmGgO_qDtkQ_cZpdTVzkwRq-WR_DFPrJkuLotc6r1D-pzpOWCFAFWShZZHdbIp5Br5XwJGu4B-NSj9Fw3W9xSCXH-onyr2O-AsmRwMruOv-hS_p0YHFvdi5xkhikFPbimYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=tJ_xoiPNzmJY1XzUaS2GZl7US12SeAIWhC6ey3d-aT4D5JjCZUi8fH8cSLVKMvI9iHqeNgg3RbrI8XMyyksw_Vi2mJUMafS9KnKDwitFKi1eqvEvr0oP3HzMnC-knaVCIYPx08knxLkhQVh14PseioSbq03t94XOSNC6afHRE3tPbgMI8eBWeYiBhtQgekwAgDb8skrGLP5EOMARC28cfqXdn1TT8-nA4D54oix3XZZ3nidnsScLx4FjSvxFkqJwjNy0usLpcFFXpbnI2YYHNuIOEzfu6xtGp0KWz3OdEAcQjIzZfh1y6s-ixH_Jgha0rOrgjXh-1mNzT0s2q2Ypdoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=tJ_xoiPNzmJY1XzUaS2GZl7US12SeAIWhC6ey3d-aT4D5JjCZUi8fH8cSLVKMvI9iHqeNgg3RbrI8XMyyksw_Vi2mJUMafS9KnKDwitFKi1eqvEvr0oP3HzMnC-knaVCIYPx08knxLkhQVh14PseioSbq03t94XOSNC6afHRE3tPbgMI8eBWeYiBhtQgekwAgDb8skrGLP5EOMARC28cfqXdn1TT8-nA4D54oix3XZZ3nidnsScLx4FjSvxFkqJwjNy0usLpcFFXpbnI2YYHNuIOEzfu6xtGp0KWz3OdEAcQjIzZfh1y6s-ixH_Jgha0rOrgjXh-1mNzT0s2q2Ypdoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCxzDJGozQySvF1cM232vz081YiH6oMFEEPG2guw-ntEqlX6vHnWV95GBFsrMmv-AZxFrJHjZB2n6xEsb44YPgWMZIiQmhzw8Uapdq1TGa4gOA0CJ3LVB8n_cXrDy8CtoguxAuNYCWcRIPpWjPgwrE-2rtW6Ohy1EVbzpfeapjKKLN7tTKOcz1YuPCbhxCnePiQlXdNqdS-K8tVUQZimlgPSu_ufA-miUjms31hAgrkESYdwhb_4t9Lif7vWlUkD5E3IpGkwl32m9YQkGaWf9OG7NyuL3qtnX0vRcifpstHDJrINe36Coq0AF3hjXqnfaYMhfXZOpklgc3o6fwCcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFBfeSw-QUxz9ynxlI_x7pXrvzxt3ISzrOwuHn2b3pUO2CCtTK_YD5p_9y-clFjTAl1oTxhQarCqtXDc3pj_5siNbJTNVvbQNLiJUhnStFzSDYCZW1TCde9FglcNd3NkrgKyqLIOUlvY8wig4zhRWDQpkqeLV1dKsx5Ij6AaByikeVdZ8lPq42cKXuOeh1KqiN-DwpEFhf4HnrOj4H__EG97o6iQaq78gl-VQ1AwhVzD1c7-iwx-8JhLgUo5CC45vt7aiZRYOF9TcXe17WmMdcykcAOK2qITFHFpcBgP3PMKK6VAArduUSw50_F73-GvyXQzc5YOZHmHeoM7zUsuWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfu-AtO2vrnILr7uiLmTaxWgSfXA0PBJrRUnK4TNaXUL5hXRnUklXETGsbzErQs-a_F7BMGl7pWSqy-F6cCXdwohh22qIMY2xX0EkcjSObvcj_ZoO4k6_uLvC8UqgVNQKhR2y26k0J323WM6_J1oleguRHtc3zQ2TBFLmI25ohfcGauRHIk9pxBHb94YlgH9YGkWMMsx6aXRBnz0Y_Rf45sE_lkyhRjq5GN9wUUnAVoSWDgXLiuWJUHHYmYaJmDDO5t9wyx3yUcWxvJhaI_CmAlBUSXeOZe0BECtQzrO1ziNQyVWeqgCFRZj0aYmrD6nIyP8sTps-Jq-kZdAwQrZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24546">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=UDaWDj09dmB_zGrX6iSZu3zQFr58yZ0d4UmDzK7HfOhLSnmwPt-k3TgjwXZkI3LQVlpxPTWY0Z38TMlTrDKZyb2GtJ8Na2Lh5Xy4yJ458JbWklzYztXiD8S5rSB_UZxpc-xUxAKeYyPC8xmD1LpdijfMnk-p55dqSzDCWoc1uRKFLjofJtcSGOAkKi57__Aa7KFLUQvxI9CE1KmOuhNyJxOsZooS5Cr0f1EcfHdoPnu5k10-4UNZt4LO18kNbcTBxPj_RDiWG4CqTk9J4I61jqkqbj5jq65ryI0aVxbP6wMTAunXXmkFES33MXjoB11CTZJBX3nry54Sy7x8rpydqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=UDaWDj09dmB_zGrX6iSZu3zQFr58yZ0d4UmDzK7HfOhLSnmwPt-k3TgjwXZkI3LQVlpxPTWY0Z38TMlTrDKZyb2GtJ8Na2Lh5Xy4yJ458JbWklzYztXiD8S5rSB_UZxpc-xUxAKeYyPC8xmD1LpdijfMnk-p55dqSzDCWoc1uRKFLjofJtcSGOAkKi57__Aa7KFLUQvxI9CE1KmOuhNyJxOsZooS5Cr0f1EcfHdoPnu5k10-4UNZt4LO18kNbcTBxPj_RDiWG4CqTk9J4I61jqkqbj5jq65ryI0aVxbP6wMTAunXXmkFES33MXjoB11CTZJBX3nry54Sy7x8rpydqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24546" target="_blank">📅 18:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24545">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_cG9UWq2LB8YFxiNkBpxThd1eUmzzg7NVLS6LP_vaPv6wSwhjkAEuQphrkCxDTYbPkt3440_xQIQbySUAqHM5h6AOZj5-EZw6Y5pRkjYrx10eQLmeAvk32gNRDn3y1cDipAGLEsJZ_AozIObomeKkE37Gi5XFFBd-NirwGaLdK15e4P5aiZ_7xDYOL6LLU6r7hG52tSaeoiTePUkUfkf0ee3k8yZ_eyWo3z0RAIY8FOvY-or2sn-cS-HhNFJ-6UF1VWNre3LroZ_qNRpMWheL0hCyTIjF8isACwSadtszd9G2dA6_KMvE287N57aDk9gMj1o8iOvINHN0hlZIvr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
جادوگرغنایی: کریس‌رونالدو میتونه راجب من هر حرفی بزنه اما بازهم تاکید میکنم این تیم به دراماتیک‌ترین‌شکل‌ممکنه قهرمان جام جهانی میشه. کیپ ورو مقابل آرژانتین همه رو شوکه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24545" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrM8kl8yDzTi1CLbBTbSqdZoDzPFxzjiJA3JOMgEA5JZcceDfnNIvyIvb7r-OZu9bhqGghXwUEm3fYjgtqKn_dP6cPkVEGHphR9yBpLfS_hlc70OrArQpvuehtovsg-CcLtMRMftrv-a2ghlE5OhqAQem2d-0L4CylBfE10RhLACQcd-lspNSxAop3N6pn6WkxyHktVVQfPNYV4QuFFixfKygCeyJwpsBC71PX6rw1RIffJRMsW05OltWcp8IOpiM7Xfum2_VCMpNTrGeXNJOcHDJMOHuISdXPeLlpTCjRB0SQ7G8BCSahyIK0v9Dr--AyGc6GrgPyE7KrqgLojyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAZet6fH8ZR1YkRh1I0Voi1VU6ov02VAa5J6aL55BKLB3i8-aAg41Q-TJSeNzE43UI3yhF4_Fyx9qznCCARMBk2jt6Ss4GjW7Cbz2t4c6bTqRDQbBvJM2NM8gGXMEzW24-_ni5ylj-dby2qbpSEx-ejTOVgmTqq0YY3xryJODnzX0K-mF91uyF7iSB69C0ETjXZsQBNFLOHtp1dofRj90nD6eP5GdUxQ4FMwHD-jLwXttlOpPUPkUIpkcd-s5aMOEGjMQx4BPnYsEF33gAayJd1jz-xbEnct3H2IypnXM7qJ9Iv5OONcnJ-tMZ0oOk_ci9MYBbOxmI2go9AqxSkdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNoo0AsxdoGLGUso1ur7vshiCaE8DztvrXkVFp4g3qV_T5HoRNBcSfSAT47au4woxHPLzgPTjmLEqiddAxa-F3djv0jPi6cKCKKAdwobQ_BWfOUNz6Ygi4T0m6Z6IDC_SJvKFWHieQqYcKL6Jrztb3WKGdYAEPZWpnMhSMxZcKqhJ7ZtZv1YyYbfA3U4NVOtFb1naqVCqZr9XQ7TUC5ulNy6DFUDVMNR-eO3mlIGsQykjtAAlYenN5uxmTwnvJvigw5PH5PWAWH8pJ7qyJIMhKQ9eUlqs1-3omwQA8zhAiYtxC1uKId0fj8QwbG-mjDiduiUA7fdu1vdBXaAFjDw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCpydK5XxPkVbk2chlqzyO567N8FPlRJVl3IQ6ktLE_VaRVApqR9nZyTPTMfz4yy76iYNqTamXnyhJGoh14fUOXN8zyoLk32B1dMq9zT-LgEkgi7zk_YuTv5E0PGbTZGNpX8F18MbDa66dohBcCjl4Di8Uvt43HevwVFC5j7OPaZ-XogLyH9y6V1JtSv_7eM7mF5fpM1MOApH5q9_FSUVuXeoVnwVKgxMxMC8cRV4YdYcIsymx5LjwlkwF62QWhF58sBr0-EuoX6qPA__gv1ZXvULhXVQu2aDyc_KSGjzqoa3JOvbjsZdhn90citvYDc4ToBiR4baANS5hxhLebdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv_uUVmHrR5JjPo5_VXIJMfGcjO0v1JIl53Gg0TxCeRGSJ9llPUKzuMPf5VmEwUjbPAGET7Jc1JRDdbIfyvs2vJQ7JjyU9GYGn7tkFNO219ayU5d85w96mykaJPN4yfehVFFQtMm_JGs1sA_VmkYsdbuiyD6LbsXngoAZDlHhpJrPyJ9mu_iDFPQjHzqyt5ySh7kd1RdOc0JeP9Cl9xgnOPjxZmfuUu2Bk2J7Fr0UUg5deZ93a17KDllV77HD0yDvt8YcW69LYHXW50KzHYRt_9BzAAvjR8iAPZ4Yz0CoaGAbxWNcAsMmsZbSLiiPqDlWYQXbvgGIt50u_2AN8WZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOjVRDUpmA5XxVpzK4XTKhC3ECK3QMZhia1OQOb2MUUVlvYloZ_v6yoypEb7OvoIIhvJ94bbd7xi7OeEy6ZE3ZQhGjWmR09t-1QcK9m-2HuUzNa6tuLEk_vpJiQULdDITV1RcZIzzhgYhL9ouzA3ewurDVhoAOG4FRV8VXFHHlov7oMElezdFu6SsOD8IbGpwf_8-LQTMN3rdTtO5aErwPAvgRASmKsS1Er__jI-UgowISO4YeSYMqNvoaPISERG8yYeM_JFcsk06zBYIqns7K9lHYOdA2TOrj8s-xvxcjnSwTNgYEFkCJyp2TJ12Wtptn3vBD1y8mr3Ha4dWj0MSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuKDw__ODd1Z_ikAvhSngD1RpbW8D_-HUz4yrEpOVL-NI2rGJ81EUTZLY1fq7FQGQVfP6poN32LE5lYbmwDK81KdigQsBJ36k3dVP8yL1sw4CfQUdh0XKqtruiutxMtMoa1O9ANqOd0IylzHE7TaAyoxqz5oKu9Qc7foIDM3XvrqExAa01UqRgw4Efs7bd2Z4Ke4ueQk1t8BcLpPHm3b4jo1ljHN9SIGqerUauIkQ-zQJoLj7PaOZLjkhcN3fx4pCED3ZaU-cpeEOiJyoryuGB-MBYzTjozoWdZ6gBgvdrM4XK2NqJgnWbxacj66WOGQFeAlQNuiQSLX0B4ZhUZv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=XbcMPu5iCUleyt4ED5A-YVBRKz8qWF2mi3rHCOdsI5TuNs18tV-4Dvk5GWbr4uq1EDHFiYivV53EGXhQwy-aNNIB5Eo5zv6IydFc8uKeR3GFDiRIGbfKaPPKgk1lWOjRo35zvJFgdOwFlgMQE4qCxCy-M_azYyT-7oApwAETiwGl6nD7bDh50LV2Rrs_dT5wuoZOAtYf6ORpNJGfw8iBGFVeGVplfic1AzxZcFQC-pk3wzkx6E9MN71p4Rga1xGzGfq56v8B8wwZK2jHU5LMZq1ivU83MCE9hy-wEmWNOC6TkfvyzxrHNcQtR9kYHhk8JmtANVk9h6FvnqdF8Eu0Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=XbcMPu5iCUleyt4ED5A-YVBRKz8qWF2mi3rHCOdsI5TuNs18tV-4Dvk5GWbr4uq1EDHFiYivV53EGXhQwy-aNNIB5Eo5zv6IydFc8uKeR3GFDiRIGbfKaPPKgk1lWOjRo35zvJFgdOwFlgMQE4qCxCy-M_azYyT-7oApwAETiwGl6nD7bDh50LV2Rrs_dT5wuoZOAtYf6ORpNJGfw8iBGFVeGVplfic1AzxZcFQC-pk3wzkx6E9MN71p4Rga1xGzGfq56v8B8wwZK2jHU5LMZq1ivU83MCE9hy-wEmWNOC6TkfvyzxrHNcQtR9kYHhk8JmtANVk9h6FvnqdF8Eu0Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌ لیگ‌ملت‌های‌ والیبال؛ باز هم ثبت یک شکست نزدیک و میلیمتری برابر شاگردان پیاتزا این بارمقابل سامورائی‌ها در پایان پنج ست مسابقه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDDcip6GWe4ti_HW0livkCEHk-jY19KN1-NRimLRmvMla6Lx_mHRUDvEjn5J5f1hRbx2sau7wxNppCnMbgltYLxmLwtBBcePoI_ddWmnTBcTuRA78lMZStEl-4wB0JmD1BAPp2gAc602ClCivkO0X78t1jHXppGUO_7E7GBaNkbAuYoxDNwxBVhAvYj5QhJOE0U_0K6SCM47f4otjShfhxdcZiJhLSaewtq7ju5IlL6DcCtXYEqU0DvEHSHw5c2FtklkRpuqp_GB77c7PO_3vGkk3pJ66CRKslva3bviHFyY60EgnZo7zC6t1XM7TSUE9X5-_e7TesE84fWKc_b-Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI7lC4Ylw1_QQKnBJEEy8mA8cOYWebH1qfE97HNByM5Zbn2ox4oGvbpcpNWiitUSa3P_WPRX77DdGeVdjF9pBTyQ3TkIFZGpT03rJP8QchrpmewNotMF-tJrZXekaCA1-yf07bx1_upvwg6_EMPTOVhq5Q6HM3WheDd_ISftEnmGvBWtchnpizAhduhuKrDgLyvzLR8TmM2fXl9CscyujPXqG5xQ9OXL8iVXFeynYtzn8nBRw6VUnJDiDbIl0Z7hWHMJjsqm0MUG8HL6B8W9b_G8YsLuzjCxOztcqCbp380L9fP6dcbOi7NEkiZC16rFvA5DWJbLgGpGRuyJdMIp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfDvt_UmfQzvShXWZHKG3tAxIzEbfv7Ckp8kY0rvCnHbuJcYKXQNu0bjrK08DQERPLlf5cSKd97bIcHVvNfbmE5hpyACaC2hugqoDg-XZ0BeIUU0KWJs1eA05B3Gl1q_horUWXcsPDWPssCfH9yaQKUn0dIXdTa_W4XVu38CbrztWcgUX02nzatkRmZHsTswqmYVleTjzKzbqGNWoJ6D0_il4T5lK8qy5Fbl2jPKwcf4tupShJMc18a-xis1-qYITO0dZus8auTBP_iI9xwnSw0hLJJWUaATshZKcmFLrUR6u17Hp-eKctx8EOhzC5ADdDAKkLuOIIUo6iI3PWI2Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv5bEwbSUnlUsouUbJyp-0Kr1hvB4ZXjUvvYxjbx0e5Ql-fpGNSWKqlt1FhgcqGN41GFv8OfE-sAgFXKzTM97Bglx7omynv1TzkbBKoRwZAoUN49vKPuVA1lyx2w0s1gFXR8-JPYGS763M82CI6NO_aKDnqYWF1Cq5GQRrWtwLcIj0nyizJadNB7VrhoaNv0Nxcb4xBqFcmYx1fOwxbf9AumEEiWX9yE2q5EPhSg2xu7LdtzhE48nWBTJVnewfup1WtD3kwXw1iyXzqj9fL6oighCU2xDXDayZV8YxWAsI0w_yn0z98I6QvwateZUE7B8kC0cpY7f2xh8R-5yEWBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=ii4pKAesx8H87NZaCQeO6EeXZWBF1tK7Yui1pZ_3q-DG3KDBfE7z41WocoCQKbfiM427fEIklc-7BlSawnsllvcWUuyAhCMNswKPv114LcJolegy8kGmrHHhB-LCa1JDfoYiPg1d_J_gEy7fuG82ugGXNCxrEsyFMltJFn9pyXWCQEAnSjrlm1rMd8yjKgujMAnq0F0LEQCpwA152EfnycWvKgq2eTxsiCmmeNL6yU01JwmudSpmxww8W1TjyVy125pTBlQrA8vzJFTDwLJHabtI8WFm7iYdC391p0HDFB3rkqqfwfGsN8ancdPpSBzD8EzsKeBzK7SgWj34eswHZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=ii4pKAesx8H87NZaCQeO6EeXZWBF1tK7Yui1pZ_3q-DG3KDBfE7z41WocoCQKbfiM427fEIklc-7BlSawnsllvcWUuyAhCMNswKPv114LcJolegy8kGmrHHhB-LCa1JDfoYiPg1d_J_gEy7fuG82ugGXNCxrEsyFMltJFn9pyXWCQEAnSjrlm1rMd8yjKgujMAnq0F0LEQCpwA152EfnycWvKgq2eTxsiCmmeNL6yU01JwmudSpmxww8W1TjyVy125pTBlQrA8vzJFTDwLJHabtI8WFm7iYdC391p0HDFB3rkqqfwfGsN8ancdPpSBzD8EzsKeBzK7SgWj34eswHZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzDjt_Lvsw5FedybGLzmP-Iwdaf-4FEqGuTV-ZC8Peob6FkFp3LLf1Hr5tyRtc5lc1KYEaucSJLY61Qf4R5HQcOxLa3ZMkAYdQ0tHgqZSnp0dezbag3iMMTQCNNJirL7TMPDxU0D6EguGaE2WKmDZVWImV9OqLkcBMdh8rxkK4Ld3CDlU2UOw38aXzwtkCCH2Y81rVoM1Z5iRzPMbIIlJHraMkFMhsbISA5eI4FfvhBARV87aooDONszPhTn9bK1cLeooYnxIh-BSOoiz4D3rZlb0_opzGrThaNdDO6wT7_mOZUjQt_XZH8IrWrwgOH72w6O8_6ECNkcJYaj7qHJWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZRwmD6whZa2bIfqjA2xXnMNYwBdK714b7KdhuOSa4My4De0Na4PolQwCyZK_C1cpkabAfYqDHsfQsIXagVW9DQ6y9PWIrLoxKNcThOWYOGUaZbMxR5UvHPzcRyFzj7o0XMxcppls_wcPKVws0e6WTxL2u6n2xpE0lO_9mlQe-8wwGFl4EU11yse337Q8_oFkxDie4BkXOT113BQbZf0tf93P0sF9c1XsRm-izNNq43UVx-Ux4FnRJFFnylbpmgm0abeaP0axQ1qLzZcKfN8sHG7DLYaK__ZxRfM_NzXxa-LasfQ9KXwGg5uhFptaiWOzoJDn9vntBXZPS_woH_E_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=UNO5F-iwQK2yzaeiFBkJOZX6bz-5sLtPDFfN9UZ5_MrQjv8ShlVIB86se9kQpdzbEaMiGizDN324v9x3ijFe8aBujm4LFqpjEdG-m5LTzBrS1InC4JhgMRNIfFVjau9K6w-_ysrRLXEu2HrQuRSPH2i2SdwP7jSLfXmdfQC6GjNinBV3l64F3xBpqviXGtcGnXxQIFxgKKj8chSjJmM1U9bZCGs2VgU3nUmYhY9gb8czZ27E1zPiotFRc6UB8fepCZegSJhnaikZ9hNwl-ks-oz1kHq7ROyudYQefk532vDRTpWtm2ioxNaS_TX6gbPoQGjQlZUo3lZe_GZW92sIwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=UNO5F-iwQK2yzaeiFBkJOZX6bz-5sLtPDFfN9UZ5_MrQjv8ShlVIB86se9kQpdzbEaMiGizDN324v9x3ijFe8aBujm4LFqpjEdG-m5LTzBrS1InC4JhgMRNIfFVjau9K6w-_ysrRLXEu2HrQuRSPH2i2SdwP7jSLfXmdfQC6GjNinBV3l64F3xBpqviXGtcGnXxQIFxgKKj8chSjJmM1U9bZCGs2VgU3nUmYhY9gb8czZ27E1zPiotFRc6UB8fepCZegSJhnaikZ9hNwl-ks-oz1kHq7ROyudYQefk532vDRTpWtm2ioxNaS_TX6gbPoQGjQlZUo3lZe_GZW92sIwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=Dva4JxobAG9X4D-en9-i2saiJYKHRIzV1ty7leukTKV-Zf2z6mVZNBdPDOjacWxtVL5LMnyHIaoS4xbkH8c9946A6T3QprtaIaoI0gLGnBBWmWc9G83lTVMrh-oy1owwUKN4ZNWVD16kPfV1E9ztSCugb3lTLqQzScqeeHhLxL3IvKXvIY6Wh5tKE9PPxYIPSzHi4sex8Sko28X_AjHQUjpdWkt2EFaM-cKSJjS4KzRswWkBFWUaCYbb-B_JB9r-Z4Zr1fcy_v8MBwaaTp4abzKb3pW8Akfc2J6SoOjg-eLFmwmCn4t_9osVNFFzK0YDGCRpajIGMuZCT-q417nYrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=Dva4JxobAG9X4D-en9-i2saiJYKHRIzV1ty7leukTKV-Zf2z6mVZNBdPDOjacWxtVL5LMnyHIaoS4xbkH8c9946A6T3QprtaIaoI0gLGnBBWmWc9G83lTVMrh-oy1owwUKN4ZNWVD16kPfV1E9ztSCugb3lTLqQzScqeeHhLxL3IvKXvIY6Wh5tKE9PPxYIPSzHi4sex8Sko28X_AjHQUjpdWkt2EFaM-cKSJjS4KzRswWkBFWUaCYbb-B_JB9r-Z4Zr1fcy_v8MBwaaTp4abzKb3pW8Akfc2J6SoOjg-eLFmwmCn4t_9osVNFFzK0YDGCRpajIGMuZCT-q417nYrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMZpUUdwH-FldUShUoeJpuWxpRB_Fb3TUbN1vYLphOmH5tuBWYGYZTm3xvis53tYnSLuDm6TbJSL91SnZF50TC3jQfeOW7TvbwNew2xU68mizPibzXaPIXTMZqr-v1GRrj0k6L31somZWWHJzueRrlu_h2DQcUfwtEiGjUWhXYdjjCrDjzAhzPnwoYLA4Rj4S9Mt2q9jk3YEDOUgI85zpvyx4twJEjHMQ6hD0_D6UvsZoZt_kAhfbb0O4LCT9DCHOVDi2YshGSdXL_r-sI9CXacHh_hm5grSG5UAxKuNeAANqzmc8vCTc715s8DnJKaNJ_Aeknm3I64sbbkrVcnRog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=iMoJ7V7AR0flWmlsrOLuiAGyLXtZmZqTsVsySDNEv5UNGNJ62I0CK_b2HHCMeRwwEouhSn-TmxB_JVlVnxs8bDdS5mxCtp8HUr4sD8egRzwoQpo2N-rQCoenk7CT9Qisv433BYIvQFb_Vk5Sz1GB82ev59ZoH3wtTOdZyvY7TpZmi6C-vOrLadYmtgLFoSKl-3h3NpRb6T58XIEdQTfbYy3czHTgCop_mFLMnXW6iBJorEJuANn0-6VJjIru9LjiRU4xczAre0i76HdxBHH-UwgGG4wiXnaRwD3jngHNKVBCaTN5D50J5a33rh8Qu_dRAnW6iKYdCsHUC822PpBKmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=iMoJ7V7AR0flWmlsrOLuiAGyLXtZmZqTsVsySDNEv5UNGNJ62I0CK_b2HHCMeRwwEouhSn-TmxB_JVlVnxs8bDdS5mxCtp8HUr4sD8egRzwoQpo2N-rQCoenk7CT9Qisv433BYIvQFb_Vk5Sz1GB82ev59ZoH3wtTOdZyvY7TpZmi6C-vOrLadYmtgLFoSKl-3h3NpRb6T58XIEdQTfbYy3czHTgCop_mFLMnXW6iBJorEJuANn0-6VJjIru9LjiRU4xczAre0i76HdxBHH-UwgGG4wiXnaRwD3jngHNKVBCaTN5D50J5a33rh8Qu_dRAnW6iKYdCsHUC822PpBKmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
وضعیت نهایی گروه های دوازده گانه جام جهانی بعد از اتمام دور گروهی+ جدول تیم‌های برتر سوم جام جهانی 2026 در پایان بازی های مرحله گروهی این‌مسابقات‌فوق‌العاده جذاب
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-zoiSb_yQx8PuLIUfVMlb_3jjeMfQWGKMYEyOVuU_KBgZlrzxOcYyaPGxZWuwJbkmacrgizeYDYFk5diSpF3peI2EoDqpV12lfytqMjvK9ZPfvJVLC83VDvHtLWtvSXgIbnOJOv5z7nGj6quPBChqvYE1ZOhE0GZ9w12O9AT0MmIgFH_7a5ttr_iKBuatWzp_4D9o_qQbfhEZHOQSxqRDbfuiy5XXJ-oND8DbY8jMxcofv6xfJwyPTShjSYylEaCW9AjE21sxAWyenPlVHGNhB29t463ad39WnZjYJE9lMruTvu7o9HCV_HaFVWLZK-O9myb5omWZQtFJKuyYbkTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKWep51C7715dybCkeQlZGgI2K4KuYEjml84yvo-CbLU6YqqFNcj9ehqD-I2NpV2luaEflD2yupfHDRzu12CkWbRpycBULG5S9wHcyacvLlDXPTzuJTv3zIxnS_zpeepsdzMXMQWuVex8NLnMsPCYsEyyq2-B7kQj4IQCYNAWt0Ujq7v_So-DR7yLLhr8JowMA_y4e12rbmvU1sNR-Wf1grqEfDvNyBH2r6_ArJT7mjq08yoXD9wQi5oAyxnaoo7irbdjAOn36Prgx30-fpUNiD-scaVKd5xcyQbdevRjlGEXjtvzT9n-SASuIbWiQIccn5sqmjO9O9cs4KlzZwORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خود درگیری‌مدافع‌مسن تیم‌ملی بعدِ بازی با کیپ ورد؛ خلیل‌زاده بعد از اون صحبت‌های گوهربارش در تمرین تیم ملی خطاب به پزشکیان حالا بعد از برد دیشب انواع اقسام توهین‌هارو به مردم کرده.
‼️
حالا این‌کیپ‌وردبود که بزور بردین. فکر کنم اگه تو جام جهانی یه برد بیارن…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24522" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXWA9iP_pqLvyi_jjS2TqQBLi-G0r8qr0gpXy2UWGrzvDtMkeeSPV7-bPvo4xkL7TshUo_7OwI4rEV_67xyEMpR8teOde-23F0UBoeeeiH5_c2Ai5eaLOnajFS2fMvBZAkFy6eXhpZLlEntsrbFMAlBibR7hrnNlBS7srdeQhFCXtQqCEhzyxIM9_xZev_ORrluK538_5eqp5GE9kqymhpUkXG0B8DiHoUk1YV2ouH70yBZ-JRt6eXjFkj_xW53XaP0x931cjrIiu2AWY-Knj0FHuZeGJt9vrIy1e3IM9LmeB9-6-KpgSeNOY2vs-02cGpcDUpkSxU2beE0aSmu2mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1d_OWQUWvOhQ7Ge1KjjgEbMh2cZedY-sJFlJ4kx8mnzlfgOuj5d5ttLYqv01TK1VRAR2qZ6u2pQTO79wRNMfORb-X-At3k4JYxC09RQ4f2POcqAUc5lLqP9Za-ygz9HVAGeHM5iAs2XHeQs0GK8uHKvR9NoP_JY_ht9_H7YS8Lz_WmX9ddjugs0PvlvFtk5PjRZUEMUlBqhstVY6EizXG5snBKEiYrRJ9MQ5nz-WTv1L1mVeRuIMSuRrOP4hKZghkMFLCnUSNJ5Gu0i_9s9vhDYj2LZdQc2jdCbM8LqgA-DHEXyUejFwU_kIcXnFMGluM3gLGGCTxLdHmB73SiuZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=QSqFu0OswEgjG5Aa_P9IYMxVFcxtwIBSaKhBw6vxfu20H4GHoGRoUlMcscQyhR5aDAENOufqrE8HM3PU0Qr9CfT0aikqF-JLOXksU-LdjGZvXj1A0n41z0QBf837wgA-SS-9Vbv4wO561yVRTYYDDuoMyURDAKHDwaD8ilj-rwDQBEalxBkIxd_LHwxYA6ewdSUT7aXpiL8oSn2BO2Cwp4u27YSXCUKEJbin4a1jhGwxrT5qqLMzCNqLpojPPl18FafOJJC57hSrU7KLiO8SMCP4ic0kDwQ7EYtUCBOmr33MwTc5VbYRqmx9Cj3BIa5LzjQNMext0-T9ir0e3-FcLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=QSqFu0OswEgjG5Aa_P9IYMxVFcxtwIBSaKhBw6vxfu20H4GHoGRoUlMcscQyhR5aDAENOufqrE8HM3PU0Qr9CfT0aikqF-JLOXksU-LdjGZvXj1A0n41z0QBf837wgA-SS-9Vbv4wO561yVRTYYDDuoMyURDAKHDwaD8ilj-rwDQBEalxBkIxd_LHwxYA6ewdSUT7aXpiL8oSn2BO2Cwp4u27YSXCUKEJbin4a1jhGwxrT5qqLMzCNqLpojPPl18FafOJJC57hSrU7KLiO8SMCP4ic0kDwQ7EYtUCBOmr33MwTc5VbYRqmx9Cj3BIa5LzjQNMext0-T9ir0e3-FcLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=gABm053B6cNKhlmYSNtRlOEBVrdqxmwWqIZYk56Wt5NtqlfrnjDt5PBsLtXp1J9MX4NuKfWrCiOgZskwmjWeJ4TOOlGtC80TnEhsi4qfriUt0IDhx803ntveHeKQhINvLYU1xWQknkcEPpSA68gncjaw4BCYdtAT-q7obPxJXCZDS5Iry-28KLyklJnTlAo9b9_Q52FEL6Cg2MBotzmiPfvgSFUA9wjTE9ozGUD4n8PmhiP2xX4ofnAISuZ7rcexsEzyTTLg6pZng4zhyaYKyusQJPYynT7B7wg2sjTUrDpDgNU_cf58OvMrGCdiNSXCPwa3dkBqDJZt65tDSwK_8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=gABm053B6cNKhlmYSNtRlOEBVrdqxmwWqIZYk56Wt5NtqlfrnjDt5PBsLtXp1J9MX4NuKfWrCiOgZskwmjWeJ4TOOlGtC80TnEhsi4qfriUt0IDhx803ntveHeKQhINvLYU1xWQknkcEPpSA68gncjaw4BCYdtAT-q7obPxJXCZDS5Iry-28KLyklJnTlAo9b9_Q52FEL6Cg2MBotzmiPfvgSFUA9wjTE9ozGUD4n8PmhiP2xX4ofnAISuZ7rcexsEzyTTLg6pZng4zhyaYKyusQJPYynT7B7wg2sjTUrDpDgNU_cf58OvMrGCdiNSXCPwa3dkBqDJZt65tDSwK_8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=F9NJ2oTU6Zx_Wkufnu1SZFkhExl4F6rh2Neh75Hgl-u2GSCLDtlnVkqh1QDDGCu7TcRASNOGQJwVqTXvYgqOkxJ6RKNFP7HfFHe5z_44BiYbslC28L-0F57R_SnFnizZYPu21Toskcq1llQBfnjhUfABiu-fANIHT5m2j08Q-D07aN_sg4MkPsXEfPq7l-60n6Hfg-zT1FFTxiX9RBwAk6j-ZEJiQQxvaNO8JSAFKuuoqUAdYP2f9T9PXyQMaxM6S3Vd3EfVA3W3Kj_U1AF3uRorGY2FQx1v7jfCRrOo4r8gsOzaMWARSixMB2uIEtK7HraMWVQNtWvMponw9Sy1oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=F9NJ2oTU6Zx_Wkufnu1SZFkhExl4F6rh2Neh75Hgl-u2GSCLDtlnVkqh1QDDGCu7TcRASNOGQJwVqTXvYgqOkxJ6RKNFP7HfFHe5z_44BiYbslC28L-0F57R_SnFnizZYPu21Toskcq1llQBfnjhUfABiu-fANIHT5m2j08Q-D07aN_sg4MkPsXEfPq7l-60n6Hfg-zT1FFTxiX9RBwAk6j-ZEJiQQxvaNO8JSAFKuuoqUAdYP2f9T9PXyQMaxM6S3Vd3EfVA3W3Kj_U1AF3uRorGY2FQx1v7jfCRrOo4r8gsOzaMWARSixMB2uIEtK7HraMWVQNtWvMponw9Sy1oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGKzv-X8iM_XbFRGoYY1jcYKzGF_D9QUuLcd7McYEZ-Wt7PXTXG6Uz1zxg2hrxW_8NlUBOjRfN9f4nrtHPFOMMQVtHE56Z19rwXNjbNCMRFZ3lS3PbM2xPlMy5CwUTDuO2HrefCYThvvSfQPfXbhyXaYekhtaUwjrgKJt9urXsS336xw6rFpUA40Pi46ssyhpazTPhpR3TVEkk_xuh9yAM92Jmvld2XOQZDIz3E41DDbMVMisBTbI9MV5lWrZ3Do4nA7OxEz7JD3kv8kK6RIgkbbnDckdUVuTN1y-WhairII7Pn5fyUR9cDNnlag8y-iFonw4qwXJtRS2ql0KPYBSbj0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGKzv-X8iM_XbFRGoYY1jcYKzGF_D9QUuLcd7McYEZ-Wt7PXTXG6Uz1zxg2hrxW_8NlUBOjRfN9f4nrtHPFOMMQVtHE56Z19rwXNjbNCMRFZ3lS3PbM2xPlMy5CwUTDuO2HrefCYThvvSfQPfXbhyXaYekhtaUwjrgKJt9urXsS336xw6rFpUA40Pi46ssyhpazTPhpR3TVEkk_xuh9yAM92Jmvld2XOQZDIz3E41DDbMVMisBTbI9MV5lWrZ3Do4nA7OxEz7JD3kv8kK6RIgkbbnDckdUVuTN1y-WhairII7Pn5fyUR9cDNnlag8y-iFonw4qwXJtRS2ql0KPYBSbj0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u66GmaI8yX_C9lR8JUfRTWXsYzXYHFJb9RqAMJon3SZVDJkmjrfctVVclcdNzb5bE_MhjvW0RHFj9Z26Vu_XpNg6ufkt2uvZEz1pK8xE2kfZ9xqKx3obNyPvjIROnbWl4z_pNTz7EqY8xijmexZO9eg09btbAkGLe9h2rcEzQdZqRs77nX9mHD6s47b6MAtZ_7P-Gf0GIO8I5A_4vajhDFcXifAqiyhI3G_v50--Rs1UK9-1rCGQM9xOJRiiAmg3o-LXGBp4yeRtI_rGPzES1dwKqoA95XXFqfuxm0CzSZw30_kzFUAs4VV1BvMYs7TUf8qlExurtpK9siCNfmsBgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq16a64JaZsa0LKvhDf1plhL87YR7QrlhFekzLN4KALU_ZWZvGrWE7R20MkCY535XlXXzoPkc79blI8jZb8oY_EtmOaI3gOn2Kd2BLVASkjc-x1eII5w4_bBIO3TkMqWM9OKKKlO8ZdqkjCqvRuJCcq5dOXgaxChVyPJNNjhYBYab3XFK-pfC96_QU68z0UbTrK4mZs6VBw_9XNOhZ5T32yWzbZ3PJ5r6UThnzOW7r1yJD1xyzyg_C1lABEc0VCIt6_rU1esXpHk0m76Z47aF-Zlj2Vm6wWSgwgl967IiflhqKJpy8T0w7lyPxFNjyy8uUnjnF9QUKnIRg_UcXm3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛
این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24511" target="_blank">📅 09:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpChTSdg99E4mECkH2hUU94pm1whcZCp_8uH7KahJdUc6Lg1lQEqsCUpfu7kqNlmU7E19RR9xq5lgvuIENuhQpaUBwNglBuBktr7JjUed550SB_ABWG-3ytXwZfwW9ivSaEpR9h57VYNsrSv5lG_hvfGYaU8O5OuMPvfG88I8Val_yVJ_u-s1SOUjfP20wtWzvDHmlqcpnR1A1RENvkkPBOtSD7RLzwmUKvPCobVRIi7Q18ed8Wqal9GY98GSHy7X8stHSQOW_9oZmOltL52YII3h11eJjp3uiOFwNv3IOafOZy0ILhsH1rye1Q-Lx6XewhMG8Eh3fOHz8h9HkGVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YIy2NUJg-FbPSNVjyLbuvmdmi1DZc1EUPsz3ZaC9Y6nUGGDKYYSpAwduP27iqiK7NmJln3hF5mL3gztPzYdB1Du5OYjl1KDMRIOPb2a2fUbsLbEH7uxqlTAizLxU9_2g4J3-DeYxlLsbQS3Z3tgIhK0jUi5RG6wkY8Z45KtCO03Orb-MzbE0MW2LiPbpmg6UErWiVk0Dh_Z7Grwl9a6hhpTChWHscscO7sQnF7FO3Yu-q3m9K2O_mHmRZ_Hkzcl26VyScKhRslJrh5LQfNV_7ye4Whykxhu6orKkxNZcNbzfQwS2d4it7k6ino8Vqywhzsn0nB2Dap9XwjFtPf1b2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24509" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛
گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24508" target="_blank">📅 09:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24507" target="_blank">📅 09:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=Ksf7x-9VTCcloEhxgaTJDfhYDCujTl-E_WfngnBAjB81MwcCLkR5Tje-v7fLrFH1cLTeTp2yxqVo8S71c1kE5YsUEgUCxYYW5CKLVnOr52CoKPTDUCObAm7-CmCa5imnDe1Iog0PJbpZzWEj40cizelUjtpiLVFBaLifAHR98kHRlQXgLEU19TsbcQ8ZMlimH7AuR81s2VMUeH6R2pnsn30EUQtTxopNlU2pf9yG6AhHrK4ammxUgtvJ8KCwMxfz-VYzlWWvoeWC54ZmSwE8YXDsj6bEoWfpT-bONAaQIcwoOIIEZRIjl2_vFEYcRncLHg9nuCqF-gVdB1qAdAPLaKlqwUheR-3BMzfJlSRthz9KFpmfEEzyXuw1WkOEiWzqKmFPTznxVJkdOWFvLcKPV6m5PqGIZvQF-AqNwfZp-5izU2RlLidYf-QLcJsWZw3uSkxcY-eHy9ebbtE3AHcNEDa71xHoyp8PIzi4hLFivdV9eZJJHg8in9qUwbjkdtgmA1YqEscIJApV7z4l4qePFykV07vLLz67SC4nSIs-UToCaZ0-RNMOXHroF3nLUt-HBRIM_UMav2RVkAWgS0afATYL1jDTbeo406b_HmZsVJs-1enk6fdyeK37tEow-edMAFmLsH__E9jnv2Wg7G90A4VlhdxbB_8FLdZm6IAB41Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=Ksf7x-9VTCcloEhxgaTJDfhYDCujTl-E_WfngnBAjB81MwcCLkR5Tje-v7fLrFH1cLTeTp2yxqVo8S71c1kE5YsUEgUCxYYW5CKLVnOr52CoKPTDUCObAm7-CmCa5imnDe1Iog0PJbpZzWEj40cizelUjtpiLVFBaLifAHR98kHRlQXgLEU19TsbcQ8ZMlimH7AuR81s2VMUeH6R2pnsn30EUQtTxopNlU2pf9yG6AhHrK4ammxUgtvJ8KCwMxfz-VYzlWWvoeWC54ZmSwE8YXDsj6bEoWfpT-bONAaQIcwoOIIEZRIjl2_vFEYcRncLHg9nuCqF-gVdB1qAdAPLaKlqwUheR-3BMzfJlSRthz9KFpmfEEzyXuw1WkOEiWzqKmFPTznxVJkdOWFvLcKPV6m5PqGIZvQF-AqNwfZp-5izU2RlLidYf-QLcJsWZw3uSkxcY-eHy9ebbtE3AHcNEDa71xHoyp8PIzi4hLFivdV9eZJJHg8in9qUwbjkdtgmA1YqEscIJApV7z4l4qePFykV07vLLz67SC4nSIs-UToCaZ0-RNMOXHroF3nLUt-HBRIM_UMav2RVkAWgS0afATYL1jDTbeo406b_HmZsVJs-1enk6fdyeK37tEow-edMAFmLsH__E9jnv2Wg7G90A4VlhdxbB_8FLdZm6IAB41Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24506" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIAvBpXodRhwuWQmj5nhAyeQZ1DhjUHDAhlgtMLW-lglxspgFlXnUykyKHyvIbAtWe1ns5sOCQZpqF4zwM0M4YB8QCRqstlHvtW8kBuunre3YaN75DrXgIsxf49_OpZYpoBDhEtbTWzaKSVb9y_aQAfO20RrZZxtAFJcf8DEOGBvfL-PGUGJfgFt9YVZk7l3qTedv60VCYYJbxRNBWExv_C6mjmGAAsF6oP7VB7Rkb4R0AQCDVumCT06izixkKKvErEoQ7aQEOomjjOM8oqfaL4sn9Mzmj517vk4wlb2dxWUsj22cZANNiLFRM1ZBpUqR1HSEOdKSj4pquwJ3DVrpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24505" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=I5CMiu9ILZfIiHIYcEudT5fCaJSk-DmaYB0T4rWWT7ZVsnV9V_VA9OXE2-uIdNmUkUlp78EkA9gu-hIqZqmlWtwLUwFxIxdUykwFKlKXXL0GaCPMAhMCifig592pruAqLHRCF-2TZZeO1ANcFNvi5XOp0vJud2tt-bCrXLDhG_dEV2OWlHWyYfLwhgTLncxIjN6Q3djIxvsxkT8-UGmtTMeY2FJ6XutB3EZcMV04YMBGmUn2nzzvORq5vvmy8EPwH4Gt6Vm-qEbjzVzv_1btcRdFeAZ3TK7n3BLD89jSgtF1u8CiMHqL0aY3gJluA4wPVepPpD1f2ecwTtFK8CEmmTbKdWiHfa3dM9Et2S-r6doRdxpHkYDOPVEsxW2NUASVEj_gM2oT266x6Jkdmr8zmAeXjA2PnLdLiKVKjSmTNZeJVYaF5aujAerpxNgCXz_6E_ZpGD1Iw-JXwW4jTCnv3Ur-yy3JOVaSX0tPW1NBD5N8XpgVZVBRZUXEc8SRhaDCOHo7QhzZn2RCH0MpCa0G38qE9TCRglRZW8C4AYcni4uCF_P5itdtpgbQj2pyDUU2uSSz_17Z3vZLhXsmyuIjuuNMUo--RNrB_aBtOkhT2zlVqJkuIksMmFlAl1CaSpBHzXnfA6DGN1BYoXPub9OJYukSQJ4Frbx2YodLSElQfN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=I5CMiu9ILZfIiHIYcEudT5fCaJSk-DmaYB0T4rWWT7ZVsnV9V_VA9OXE2-uIdNmUkUlp78EkA9gu-hIqZqmlWtwLUwFxIxdUykwFKlKXXL0GaCPMAhMCifig592pruAqLHRCF-2TZZeO1ANcFNvi5XOp0vJud2tt-bCrXLDhG_dEV2OWlHWyYfLwhgTLncxIjN6Q3djIxvsxkT8-UGmtTMeY2FJ6XutB3EZcMV04YMBGmUn2nzzvORq5vvmy8EPwH4Gt6Vm-qEbjzVzv_1btcRdFeAZ3TK7n3BLD89jSgtF1u8CiMHqL0aY3gJluA4wPVepPpD1f2ecwTtFK8CEmmTbKdWiHfa3dM9Et2S-r6doRdxpHkYDOPVEsxW2NUASVEj_gM2oT266x6Jkdmr8zmAeXjA2PnLdLiKVKjSmTNZeJVYaF5aujAerpxNgCXz_6E_ZpGD1Iw-JXwW4jTCnv3Ur-yy3JOVaSX0tPW1NBD5N8XpgVZVBRZUXEc8SRhaDCOHo7QhzZn2RCH0MpCa0G38qE9TCRglRZW8C4AYcni4uCF_P5itdtpgbQj2pyDUU2uSSz_17Z3vZLhXsmyuIjuuNMUo--RNrB_aBtOkhT2zlVqJkuIksMmFlAl1CaSpBHzXnfA6DGN1BYoXPub9OJYukSQJ4Frbx2YodLSElQfN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFzaELad4_hkOAy6G3lMKc57M3B53fcuEnHeb2UCUg58Jkzpxu2nmysMbQwVM1uY_IojBhiVpXqLRWjEhasrJC33iBfGO8uH3eVJSmEk5-kmyM6VsM0NK1Uhl5_B2haY_W3EAPgG7b8Xgp5UAccgt5BPfd1X4rOnXhJ_MiblICPo5IPjcuuvji8N4DleijqJMEqNTmM-3SzvBmMF_cNKN_RpnpJYtxNaB726eidvWDD244yjfMzXYXeGz46XbHkCfabNrs-LUyzLSPcvymlWTewNKfUxvbffwVwEjQLvXuRKK7SIpMSvEmJEAUDxnTPJ-GKFKz9fvsmnnGzomT3PNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KI0dJC3r0HT2rJTq3YnpDLD8NhjMsZ3X4ovebGehcoPEjcbWjRU0XTh8dxSAnm0NBELI881oEiSMRJkBlkS339ItQbGifUIaQybx5E3pRxkB9NNhhoSVW-BmbOaSNLGxZBkIovM05WlhjsX0IT3sNq_dLiYvaHQzTvHTxykGLQ9Ajl1decaVeeVtzMEpFZNcl2qnkPSj-qcxyU-32DsTSTM8XtVMmx6tylgPWIW1d50RV0GjxklvyN4E3OozanzIrq79PnFznrR-BHT8KsBlL407SkY6m1jqOsad6BlIYYcKbtYNMUm7DXeXQANZCbhVUkmZI88tv9mEHGxUyXyv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iDleP_ZYDxAPH0AE51tbI1fTlFTZVLzUoXTkGNNeSdHlm5_XfLySBvVEIZruiJjEVsNet54Cx6YjsU8XOdsQqMR5D3zaukMQGvL1HsiZ2qFZm8BGdkYV-6HASfztgHKJ1zpyVul9i0AhaFMGlZXKXwP_gSJKSHT8sOkMuQ1eAvKKyiHXTV1ZffZo9kRcmZiXTfxYIDjnDSfsLPRUHMX8H0MtcA-3SSVXPt647FOIEVMoa8vrXdKN8ekfypE_JMHq3TB0Tqq1hDPb1LJP-niNlvX1CeJyQ1xAKjWouxSFM4C-VPLYGde8KaRSRWyGC4lN0jQPqT9Of__W8al9MkMVOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
