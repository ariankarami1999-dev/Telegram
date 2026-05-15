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
<img src="https://cdn4.telesco.pe/file/VMgGQxL6bhKehABhUIU8wDVruIKyQWqiGnqdqqRGGVG3kzH_lpok2_axE78H8lGXxf9elbnY3bdzSBWVIGi7tdmxJ4VXyT8HB-JdERodLGxpZBhS2hClsec_hTrX8vr_q75VACr8K27kWXKRMVHbt3JN7wokYvxL8MvXyn-eiYuMTZLhBp4yyYFXRuIgxwKBJx1ghayHbcUUCayKBEJP3Ie0PscF9iOB3geGmDOs6Hn-t1x2KGNcP2_XSkDM2tEdZUff2b3a2ggcPPOZp5QRcGDCuaBhBzNQepyXeZLEu5f-eHkD6CLRuNKqqEXjrqd5xGejLsimrSZWV0cHp_LKLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 135K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 14:12:51</div>
<hr>

<div class="tg-post" id="msg-89969">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs0SJhAhsMnvqz9L8LuvvBgC5ArdEubgLHVIeiNLFRgT3_OD9lAl2VMnEgI3Imz-gT8t9N1zDEVuIi0n9A555TdMqLc56ELGJLfdEKqvPencPKfNEl_QfC6ljnIThhD6hST4mnYjrWSHY8yX5nDnFlR2S3E6V-cpGxYyEUg9jiXzpRNqOUdP2SbDaWxIQOoQ8i-iMB2E7WpNWEEujjOyWsu8BV6_IfEgZxo3DmEWPjJOtc-F0-3zZ5CRu5PLyL2ay_nrDtUU7xRwA-sHnVbrgMKFKClaeS0iFuWZc7RV2M8r6JkfTFK_FD4S1dY3UiejO14o61MSe8n176-6Z2tJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای بهترین سرمربی فصل پرمیر لیگ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/89969" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89968">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 72 · <a href="https://t.me/Futball180TV/89968" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89967">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFrwBF1ii2Enn8BlRrWWLu9KYqGdwg4PwDl8U0wyumk82cd_QlAFOL6OR0UkM8lEcBPVgcOEhk0kiU9xSnz3vYjFpjPE5oS5o4z90fJb0BC2fTwv0olkgoZu9UHeN1XCejy--aWPeqavrOv1k_vMokIg8GyyHneI1QiXKf8vpICU9EiKih5Ozk3i6df7_uq2KWoGYScqN_OP5tx0p8Jn1HN8h_cIFBOMgJ4D8iZnjQZ-ix6-RdR5T2ueLbAbH9hgEra-pi44OGfUE33wxbSgg52QPPbudeH4pgS08wR0_sx3fOymFOFF5VzgAhjTAn2dBTlNabw3JDCZXK9mTfJXEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 70 · <a href="https://t.me/Futball180TV/89967" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89966">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T49RNihVRvobmbh2ig94Exdg6Mewvq462xaF1II528lPNWRWcuhbApCuZUrv4BTiCdYsmb_5fpquThn4Bohgz74Sex0NaJMElk8KNUllNU9GWcVRxQ1kb8mq0I97SewwHaBYlXky_CnVpm2LB3TIGvaWPwuk6y57cPHAU2hXvTT7rCqPkN286nAPMqzrTyla32WoKoNuf2eWb6mFfYZEkjYAYppM6fIARRm3NNBOPNGbRi38mXXsm5G184NQN6ZKtop8Wv-LwmemMYRE40A9ox24l-E5MP9mGraMYoYJeW3KaU9kas5RcCr-ZoczmGgPiBVL8RoOQPUkhyu3zTPJ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇺
کوبا اعلام کرد رئیس سازمان سیا به این کشور سفر کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/Futball180TV/89966" target="_blank">📅 12:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89965">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOsllhtn3EZRrUNy4Qe9lAoUSt_To1mBW0vQGhQug3_zhjO3yp2GvJDuVcLgQTzzwLa3z_2m-f2qnUW3WY7WQ-cXn379sCckd9kLu1NajRt818NCvHWAKCSo_sxyTwa33MKTuGZ0HQLQEyaccmprzOVTzswEnz-SdnxG82pYRmN7TL_ufJYl9baw3JXt9wULZEjxxoTohNAHqistj_lkNAZr-WmBCS8zYVQNTk-Tr80LTPxbQR7GKDPYFCT4sKSlcTSOOKJD8j80bPjPcRnQ8lO976pRSWmQbyHBf6Tt-agxO6qXJEaZ-ed2lmvtIub86P04OJScvcOEKBttNCX8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
فهرست تیم‌ملی ژاپن برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/Futball180TV/89965" target="_blank">📅 11:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89964">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF6PxcdVkJpkMBtwey-Na1qPOfoUud_VIHDZjTRgUl05L7oVHzzG-eHtfxzf_V2ksW59vkfzTKYcAGjg72pscizaY6uGBr0Qmz5Sl1yhw2kbeUCET_piiCBSnTNFBsFUwsv-tDSwqGRLA7hT9rbO1Rb17p6gWjOU7q40IcVQhDx1m3Mqa7tYYQ6a_ZA1NtDPModLHaAXb4v1Vr44oNbcgBuQOEIC1MxW7yizokAhHasnLuj1XAop0Ygnbwkv8YFbTQB9eLtU74MN61BYdZdXQi25wJ4qnhern4os9jc6ybhORJB1rVoY99OZwXTtCCxzSxi5mo_UYl47HvnRmc5p0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
امباپه: سوت‌های اعتراضی علیه بازیکن مشهوری مثل‌من عادیه. آربلوآ بهم گفته که مهاجم چهارم تیمم هستی درحالی که همیشه آماده بازی کردن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/Futball180TV/89964" target="_blank">📅 09:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89963">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
وزارت آموزش‌وپرورش: امتحانات پایه‌های هفتم تا دهم با نظر استانداران با توجه به شرایط هر استان به صورت حضوری یا مجازی برگزار خواهد شد
امتحانات پایه‌یازدهم و دوازدهم تا تیرماه برگزار نخواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/Futball180TV/89963" target="_blank">📅 09:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89962">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovMDxfeTQSgYSrG1XuRcQXG3R1RmR79Ipjm0yMGa31qCOm9e6EierjLmhN5T2S1IPipZV3fZB2-sUNH9AEpih7T4YqP_FGcWzz0ISl4JK8GkAwhtkjs-XAKNrLB-jCrlR5ErOIsFP4EfWajwpd2KeKDAT66PIRuQwEpI-Pw22yAFynSvWJJSggX7pThdxla_RNo4RkNHfBpXvJirTblao___5g_Frm01aVaga7JC6eSubBQ-4WcVHZs4Maw7vZn0UVVY1LqECzsD7l2kd94iUdFO6Bcat-8iDe1MW2oq1yBpjTGL7TYiHT33UaGg8UIIKknfL4VV3_crG7-ybgLLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که بیشترین قهرمانی در رقابت‌های لیگ در ۵ لیگ برتر اروپایی را بدست آورده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/Futball180TV/89962" target="_blank">📅 09:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89961">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CGFwp5-OHHr_BVe9xdvENccIedjoaYGHHpjohB_ii5ioFoGCFuSdVJVmqSMBJlRfdets3lvTAqnn_Bodv2-igjZnzyFwYUD2dXDTW_2FNl81H5T3dWGpmzwAoqzmgrQWk9nEMwCBjjvPTUC-LpEyN4DBlnmBYmc7VX2tBPQx_FQKulHKGlbMG9NU5Gp0_oR4hLFW2eoeY5bOvLrYUfPsGwmn8Cbr5Wa5YQKZzYXAuIEjlUr6_OXyrzxD_bGWslpJWvSkFLvT-g2dy2pZc6Vb47JzDCelJ-HKBeGuJDl599exEozqrTqSPyu6mTjUmXWNFp1nIf-j1PqWjCM63ZbSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/Futball180TV/89961" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89960">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/Futball180TV/89960" target="_blank">📅 01:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89959">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OUcI7dYsVnN1p_kO4OCAnvYDDHPTfph3OM8JRUpO1TdKLYJJ3h5kCxMvdl0T2XY4RXCOGRL_k_sKwQd3tu994k9FgdYqHoJ9sTxk_u_16fDXGFO9jf6K_1PHoFvvJDq-RQ4RB59v-DqV4G49HAUAdS8p04cO7-k1QLZyaBPg7wPbPqyijiTOv3UJ34Yk6h6SW7rRreYbcv_QpMRds-KU0S_OT2jRWGWTSPJbo7OCfb1QVw3gChVfK3rTrVDQKoyOGXr__NroC4J6jxncAv-4Vh26mDFMAlW2YAIeQHnOVxtc-jOE0phxtCXFyJ_QWDqqOEWN63ue0n027QqVWXWa3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/Futball180TV/89959" target="_blank">📅 01:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89958">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇨🇺
دولت‌کوبا با هشدار تمام شدن مخازن سوختی خود اعلام کرد که برق در سراسر این کشور تا مدتی نامشخص قطع خواهد بود و مردم این کشور در آستانه شورش قرار دارند
+کوبا کشوری‌ست که اخیرا ترامپ اعلام کرده بود سقوط سیستم حاکمیت‌ش بزودی رخ خواهد داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/89958" target="_blank">📅 23:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89957">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=T72W5XcSaqFORrJtj1sh1uMQzDLjJiT80xVmP8EIb0e-_9aCuHfM2soh6Krx5eA16drLYL0CUvfF9v60kI0D0kBYAwps6NC40J9z7nk8LrImWhiinDldydp_bNToPiuTIwzizujNI07JMpfzMZGq-Q02BFd_pCsQoipvfj86v5y3W_eFFeYWgxhz83bWSGZn1MqrWYM3Ed8sFXlTIXziFjqKwNg79pdlw0QkiOoSV_SXgrmjavLhnoaKUCI7Sqcf_fIYcWuiB3js3d83ceXZAt1HNfi-1B3RlPK9kY5dESJmDqjKYTNCjmFxcGDznQllXu4Tlc0FLPy86D-HiE0i4pyd0PddFQM50DiDCfVAhAtjG7ymHx0cFBbz3fxfNwmO-u5yB66sJ9LoeXmnilBv4ZZ48IWHtLzyoGA_avpTERBCCLXCOSR1CR2ED4MXSq0FpVw1A90nBHgHEHEsSyYbBSMXROL16JJXWxUSwBDIrweCC9MJw9a4Lc_UWIU1XfS0i5J-aCFCTnsT19sbKA8NrY8AFnj4vVg8yZQ376pvelFM7BsSE3PhJ2o3yb6fCMGEL6Cw2CsM9SuCdTcY0YZMg2RLJ_6gwTbcz4RrTKnSz0oRG9Gs0rpvNCOxAvIZHvW8O7EBBdihmm8wPUodN3xkss6ekNPTVHpWJAG6jXT-9mo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=T72W5XcSaqFORrJtj1sh1uMQzDLjJiT80xVmP8EIb0e-_9aCuHfM2soh6Krx5eA16drLYL0CUvfF9v60kI0D0kBYAwps6NC40J9z7nk8LrImWhiinDldydp_bNToPiuTIwzizujNI07JMpfzMZGq-Q02BFd_pCsQoipvfj86v5y3W_eFFeYWgxhz83bWSGZn1MqrWYM3Ed8sFXlTIXziFjqKwNg79pdlw0QkiOoSV_SXgrmjavLhnoaKUCI7Sqcf_fIYcWuiB3js3d83ceXZAt1HNfi-1B3RlPK9kY5dESJmDqjKYTNCjmFxcGDznQllXu4Tlc0FLPy86D-HiE0i4pyd0PddFQM50DiDCfVAhAtjG7ymHx0cFBbz3fxfNwmO-u5yB66sJ9LoeXmnilBv4ZZ48IWHtLzyoGA_avpTERBCCLXCOSR1CR2ED4MXSq0FpVw1A90nBHgHEHEsSyYbBSMXROL16JJXWxUSwBDIrweCC9MJw9a4Lc_UWIU1XfS0i5J-aCFCTnsT19sbKA8NrY8AFnj4vVg8yZQ376pvelFM7BsSE3PhJ2o3yb6fCMGEL6Cw2CsM9SuCdTcY0YZMg2RLJ_6gwTbcz4RrTKnSz0oRG9Gs0rpvNCOxAvIZHvW8O7EBBdihmm8wPUodN3xkss6ekNPTVHpWJAG6jXT-9mo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت تلخ یک تولیدکننده در نشست ستاد تسهیل منطقه کاشان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/89957" target="_blank">📅 23:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89956">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRkED5l39QGv1D2viVo5_GFdfY16x-6vEPKD7I6oGGZ6eC2wvNfyKb9GjP4So-KAZTRvsCbpJikrCLPXGM7Sak_7Ew4YGvcCxLQIpPWT7DUDrP3TmP3uQbTZAYTYXW1D4UNxgKAoqscTMBXRghYmd6i6bliLu2fuGS8DD8BZGA3pvxASdaimI6k6zcSGg2WgB_li2o7-j6WlbwbUv2Gxd0oc8QTWJ4C5HmMYZ38pcBh_UQcgs8F7In--YYo9oo8CiJ2G0oQyAJVVvQFb9yttjXcWOxz_rgMfOiRxtet9wGLipMGwG4G7tp0KgeXzeTL60r_SGfHHAnGAJOEMFqSN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇪
فهرست تیم‌ملی سوئد برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/Futball180TV/89956" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89955">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKGwNxRcFg8flq7TDfeyu5JqCUIR3Bg8fHNMoADJkE4u19hfrRyo4KOYPEoM-urTP6Qya97J3liEpSvVZEybvgUx12qWUQPiEngh1udqX95AHluZZBq0DRc6fCs6yI79GApWLKsb2dPL9cr-A1u-vWlNKStdkip4vckPgp3aRxqyU29dIGCQ7oiYantENOGFj1IUZVuzMOHSq7mF1WkBSHCBcF_KYGh-PlOQlTF6XxohLykXNcrSV9sA14eUcgm7h2m4RbO7a4JUHEb5rF4jD0M_bYFG5xygtzI-pwrOGzPtWsaFVeI4nmf_nPThBieTpx_G-dsDM5Z5qf_0E8QiYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست فرانسه برای جام جهانی بدون حضور کاماوینگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/Futball180TV/89955" target="_blank">📅 23:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89954">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=YwjwGmN4344XqPONy0enM32InlYEaD9aHnpcF5qlX-jHKVGxfSnON7Hbahwy7fCoOd7xXmO1ZTel7KybMy1cGXELAXGEKuj6HGqn05gNYfnJ1N_2qd9eNpAC7cd_wlR7E4Yd3Enm6efoYGeXFK463nhW1RKh590pGk8gEtPOQRvc6JESJOowIsOKpVwH5G2Ko5suQtr1wnwummdHdy_YzCPFr9pfEtjGyeLGvnn9679g_0StHNP-uKcFfcBvuiqBAJeCRGJ-5OhEV2yTKBTLxe-3_2ikRou2z9kdZ-7ZJudnIk0PMBlSAnp1rBD7XuFF2HoeeuEDxffyxNnS44CDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=YwjwGmN4344XqPONy0enM32InlYEaD9aHnpcF5qlX-jHKVGxfSnON7Hbahwy7fCoOd7xXmO1ZTel7KybMy1cGXELAXGEKuj6HGqn05gNYfnJ1N_2qd9eNpAC7cd_wlR7E4Yd3Enm6efoYGeXFK463nhW1RKh590pGk8gEtPOQRvc6JESJOowIsOKpVwH5G2Ko5suQtr1wnwummdHdy_YzCPFr9pfEtjGyeLGvnn9679g_0StHNP-uKcFfcBvuiqBAJeCRGJ-5OhEV2yTKBTLxe-3_2ikRou2z9kdZ-7ZJudnIk0PMBlSAnp1rBD7XuFF2HoeeuEDxffyxNnS44CDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاتس وزیر دفاع اسرائیل  :
ماموریت ما کامل نشده است.
ما برای احتمال اینکه ممکن است مجبور به اقدام دوباره شویم - شاید حتی به زودی - آماده‌ایم.
اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/Futball180TV/89954" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89953">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89953" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/Futball180TV/89953" target="_blank">📅 22:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89952">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koksjDYrRF7qd6yhqelZ7NohPffa7MG2enF7qJbxMB1S8XPY9p7YoOzIsMJ-M4s_6RTLB1AcStUJ9ia6ZA63CjDW03H2-ZaXp8kNo_-jZCar0kewJtCzMDppdzO7QJlEz53ZpdcQjybCqjkV_hYZ3k9-l8GQpQhTpyTj7V39KJcuHtJLKSbAMRplDLyJJnOXAazyhxnA0MLmHJpLBpcnVcvEodagiq5irsNo0IegI7on8ye_zCWI4AJk1aaZtXgryU7tjxn1objT7R6yntLiVIcaHOunpffMOwlMWQoIHqlAExYSkx5WwofU0b2hoAp8CTyBD4Fjf4Pxe8sHmg80Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی بدون ریسک بر مبارزه
Verhoeven
🥊
Usyk
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/89952" target="_blank">📅 22:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7iNDEZHl02Bxdjas8JwI7nLWdvF2D6g4YQLrEsocGNTspU8gFmbqyKxxIf-OnFZMFDDPW6B-HOnvNvzxOCJCzbMLyms9RLQRUPR3tM6SRMlx0Q8YOlurVzh2pyZqXYTmhBA8G1m-2U37n0l-OHUEAon4EZJh7kPtoDTKYq3rb76puJxnYvESDpNUs3TRhQmgrAtiAFtVByguuG8iqCKZNMzYhf4DYXfud4Q90CRVnVs2Tuw_Vkh5j0S6hoowrS8VCTEM9YmyyV5jtcJlSWS0fcsArsYnjZ6kkmxiSuC6YqvZj_JAgtlvUBXdQ_3BFECi_WkhSNZBi0fqhAffMt2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
قرارداد آنجلوتی با برزیل تا 2030 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/89951" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5OsKhxtyWYIoH-AYFnP1saohpso6WvrJHzb5fEZnCWzNNX3fZEIIgpm_UBjg9MyZ-T6EPg5nfdKOKHbnxWKdz1z6epgUJnggJZIlF6mlbAvGup8-zyQsuLJwIQdr7NEF73id0wY33N7qSql0ptlCMYnr9ltxS2ZIWusz_QVg-XQSAYGMtbYxiY92aOSWXrGMKLN9K4SfgdFWY0HfT0NgbQ7Xgf6nN-X-i6de2kEenwOTBNIxfdto1_E6n9PHcDfaMFzNbOVXJZ0F4yOYiZ5lUvr-Hfpq_k03XgL1kxfTYsCL5TYTsDPt3m7HMXkILUBHAq7RwgZ1I5U73Cw5hEPuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
فهرست‌ابتدایی کلمبیا برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/Futball180TV/89950" target="_blank">📅 19:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89949">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🔵
یاسر‌آسانی در گفتگو با مدیران استقلال اعلام کرده که بلافاصله پس از پایان جنگ به ایران برمی‌گردد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/89949" target="_blank">📅 19:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89948">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMbBAjw1LQjAAQoz2o8WjOSoctmleMwLtRamQHZ9IKYeqdCxUi-aVaxnN45SHdyqMBQCf7538LELWstg1JDPjDYibmCzTPI13z23JC4QjeZYQq0fVQt3NYI3EMEUvq-fSbLDxPOI30gxbk2tqKetuWQXbmCJABf1FSeZWXmOS7MpJCElFRb8pjXvEk1oIV_8qe0UJSW8iqnPM-jJ5mFZW7J1Ow28kAaXh01J2V01st-I5DBH24kZYKrELIrfGatOVqtQB6X17hTBhyImKKV6JRlXzkbbIc7CPMq6gdROduI4ohHSvSMyOveRJCZp3QN3uGhDZOH0qUlda0SqqR-5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژائو پدرو ستاره تیم فوتبال چلسی هدف‌بعدی نقل‌وانتقالات بارسلونا در صورت عدم جذب آلوارز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/89948" target="_blank">📅 19:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89947">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=hXJW-Zpx-K_K_eZo2x8YfQU4iIRKRhFzzB7l-nXVQ7ppvW53e-fWBHeNKaorfG9qUsm69Sf_-5YXsq6OfbZ--aRqCgkvYV4CVW_i_RTRJ-NltQywrdCL2olUiSZlbL_93DTBlbHexShf3h6I6U_5ycP5DqxJvU_bIofIyZxs1siujvMF5_o723mj3FzFFRyfkAd7Bft9q0HHWxKB1jRsaE_sHy7EmFOleNRnmRkfTkleuXlPRVyyagIu_3VxaDOJn0j4a_aRJPI-bVMCKN8h_e6QPwEfsjchFVZNHGc17NOyiYitIHGwFUwPSIBGeTDoBynHk2TccxvM0UvSFyd1ooO9fLp0x4C_JKOcCYiBEC8alCx2zGPF2dCaFeYVgh3IxdC4WIc-iS50dEY0edAYnAkLfK6uEbrupOjkRQs_16qyBH4kgGGsAd3uYT55vRPmRy4GB3sSGPDqusvjQZNGVj_IzhzQGAH3maYmdYoq5up__NPqHpQM5vslZ1mXOjw-dnsVShEhrXgc0BBkEjA65rcdtdpkVgzbpXbJyjKvPyYqT7TcWzop3peq2kayh-GydmPuiliKubdf2Jl-IVLq8RTyEhvhKzzxWEyorL9BapZCuQICPFgRa8DE0PaDqILcjeLbD1XcrjwmiTZf4IpFSfzzgvWPGpThRRoZMVbP-GY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=hXJW-Zpx-K_K_eZo2x8YfQU4iIRKRhFzzB7l-nXVQ7ppvW53e-fWBHeNKaorfG9qUsm69Sf_-5YXsq6OfbZ--aRqCgkvYV4CVW_i_RTRJ-NltQywrdCL2olUiSZlbL_93DTBlbHexShf3h6I6U_5ycP5DqxJvU_bIofIyZxs1siujvMF5_o723mj3FzFFRyfkAd7Bft9q0HHWxKB1jRsaE_sHy7EmFOleNRnmRkfTkleuXlPRVyyagIu_3VxaDOJn0j4a_aRJPI-bVMCKN8h_e6QPwEfsjchFVZNHGc17NOyiYitIHGwFUwPSIBGeTDoBynHk2TccxvM0UvSFyd1ooO9fLp0x4C_JKOcCYiBEC8alCx2zGPF2dCaFeYVgh3IxdC4WIc-iS50dEY0edAYnAkLfK6uEbrupOjkRQs_16qyBH4kgGGsAd3uYT55vRPmRy4GB3sSGPDqusvjQZNGVj_IzhzQGAH3maYmdYoq5up__NPqHpQM5vslZ1mXOjw-dnsVShEhrXgc0BBkEjA65rcdtdpkVgzbpXbJyjKvPyYqT7TcWzop3peq2kayh-GydmPuiliKubdf2Jl-IVLq8RTyEhvhKzzxWEyorL9BapZCuQICPFgRa8DE0PaDqILcjeLbD1XcrjwmiTZf4IpFSfzzgvWPGpThRRoZMVbP-GY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ستاره روی لوگو فقط برای قهرمانی آسیاست؛
تاجرنیا: لیگ برگزار نشود، قهرمانی حق استقلال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/89947" target="_blank">📅 17:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89946">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tinmbfPdc_YkFZjnNwhVV8cRYCChAtPIrTSYB-rZxjzqYzIsgkKCYGGVHMFO31X-iqK54sthzEbA9W1e5PU4p_uLeGZUmf6g8IeIC1Y-0KiFjYfkNDSnhN08Iz1znotNh11ircB3_HFPfJHIAqPeTNPAIupkA36F91eYO538BpEXBAyg6bilNraBoot0_53S4JYMNV65_BidqKWJbAE9Pp-lGYmSYx1JDzShkO59CJ8HLqKr15oin6lhZebKmW4a5hcyEDWrQwNfHkecp4XyXC9SoSADGwaPwe3ygPea4Qsqb6XRbPL6QwONp7DxHfCmf91M1GTD7ZcxzkpE4e1GCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای کسب‌عنوان بهترین بازیکن فصل لیگ‌برتر انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/89946" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89945">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89945" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/89945" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89944">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9X5chyIT7kn6nMXzqVGDbMQUdAY_i3Rh1FKio0HYQDnkCpR7vxgpEGN4fLX9JnVQyqqZ93byNJm8-gNmalZSoqHI81H0iCbu9thD9IkCYiNTlRyOnNNyGEgxokpHWLtNUGz46HwzElhuuMk85jVW9jCo6pkVIEyLE1wEU3jm1Vvg_YOiQws00wB-zsmd-r5IGQwkZF_lsnbAx7mH6Mj0wRzK9l6AiXMJXkwrpHnUWgkDlsLlijjfRbw3pS0XhcnGJjHIjOVdQfS069y3kSooF7c6TYTrCAYxz5CYI0X1OErCPlX34DLoC7SfY-lRPNFL-W-ouBS7minnuJvmwSnMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتیجه بازی جذاب
🔵
منچستر سیتی  - برنتفورد
🔴
را در 1XBET پیش‌بینی کنید.
🌐
بالاترین ضریب ها را در 1XBET پیش‌بینی کنید.
💎
گستره ی وسیع از گزینه های قابل پیش بینی (قبل از شروع بازی و هم زمان با پخش زنده مسابقات)
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/Futball180TV/89944" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89943">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=d29lgliuOFt5wIkKoAT1QjNUjGCn7OOUzc8g66hRMl2GG6YWscmqCfYL5lfCulW5zwxb4Ex-yTx1SbiqwTwESrUckvjtbbUKcQAYll0CXT8ayxOP28jg5Fh-ESlchovfebQBS_kIocypjjc6cDjxZQ5EecSrRpjEO_QVMHgDcLH_1jrO9KcvUy4pQ1FwOpqQz4KtdUbOh4io4SvRi0fwxze9xA1uNcaK_7ncqAPBUz8KqdNe_VSik3lqr8E8EfdW4FEEWOWo3A6iUfyeWYvK_XP7cXgTNNgMKYIgolCJL2a-yu7W8k3h5OBkvgy6jFahdK1WX1tSDt8DajWVVZpS_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=d29lgliuOFt5wIkKoAT1QjNUjGCn7OOUzc8g66hRMl2GG6YWscmqCfYL5lfCulW5zwxb4Ex-yTx1SbiqwTwESrUckvjtbbUKcQAYll0CXT8ayxOP28jg5Fh-ESlchovfebQBS_kIocypjjc6cDjxZQ5EecSrRpjEO_QVMHgDcLH_1jrO9KcvUy4pQ1FwOpqQz4KtdUbOh4io4SvRi0fwxze9xA1uNcaK_7ncqAPBUz8KqdNe_VSik3lqr8E8EfdW4FEEWOWo3A6iUfyeWYvK_XP7cXgTNNgMKYIgolCJL2a-yu7W8k3h5OBkvgy6jFahdK1WX1tSDt8DajWVVZpS_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/89943" target="_blank">📅 12:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89942">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm2cUN_4-209XTMuPTkcsBNUcGQOINDqyihen-LKGxQEvPxSXHMgre_OwrtP7vkNo5maQL0MEmAXa9N1JGy4Vaa9FsQQ71_q7truMDeDL0W_cv6QuUfZZU99DXdlp75IFE1lEtBfVCHlnlyBz5eRC4uavn-jTrTVFSH2zsCmRdyfSzV5z7rTCrtg3sSkaCr_Hyta9rFjBHJndcriEyPa1TNtL695jYwxEZPK55E0a6TqaIt6_e_Pk28UYU9B5F27-VZPiucGxPyprIB0VDQhpNBdVMIEX4xZLR7oRbnHZ7kmpHQNQuFSMV5RMqcyj5Y4YAmyCjyqk259ji7WXyXvWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژابی‌آلونسو به چلسی
🔜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/Futball180TV/89942" target="_blank">📅 12:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89941">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmFfqD5VbnGY4rlJ0Ms-L-XGn74yK6QTx2YrmGK_OtxlUvpU-q5l_ydQM1SmG6tz1453885liFyyacaCHKL0OUYuCCyRBGvnQEZPC8xK4iTcM-rthzuCXew5Zmi0LG3j4B7LmJdkzWv5J_6FETjpEQiAH-DaepPrAomqL7E2ApwhopGsLT6El1tsmfye-_2rTkWFB0r0IBvFsBeWqRGV8oucx0N2QzaNEBMkw_X9ud5ZatWEqH2Fx9kN89K-xK9KT5Ozi_6uGyplP_x0ABMvlrL3iuqr2zmfW1V5R6Iv39G3fD0VNxQviIIIadiBltdrgP3umbb-BTAgdod3ELTMNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی از کیت اول فصل‌آینده منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89941" target="_blank">📅 12:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89940">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmSlC2QwEOSzH4T1ejqwYgsBDm081CHNiV57RUFyVw257DaRJdEtODRw23zM2R1-t7-ijteQWFq6U6LPxUyxyjW_ctGUJCt4Pr7qN58ljrZxtWRxhOaGyR7fMGeo9gnEWQfMxAnSKtTMcmehgXTN_31JNp3KpCOf_GkPlpaKconSgBFsKDPmymvW8ZBzcaTGk5Nhvfh9sbYkEnkfPj38qVleKOisJb8Ce8O3H-znuNBBgqzmAnnBQd8nv0AbvqiAN7TJa0csbG8Fut1oXWro0znYB7PMIxtcnaSrAxgcip62rK2KKQuVDS7_wuuX5vCC-wLJQIEhkMfsMgfHnYEdyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام فیفا، در بین نیمه بازی فینال جام‌جهانی، شکیرا، مادونا و گروه BTS اجرا خواهند کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89940" target="_blank">📅 11:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89939">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbVla-UMcu9KrU0ZuspvHofsJIXY5t_eY6OmEefYqVhqPFzCNOgykmbrWbmmzn0jyDuqg4xsS2IOrypieJwBhP3O-QwxjIhRxkl36QNphBZ903wC3tpvbYIDNZ2Xety9FenT0PhCb-fnvCdMx6OTqNAhX-a83il3ITXIZkn57MB4sGuDmSqXAqCCQCLnTNOpiaNJ1SKI3Z5AUhy3MeuajhIYnYb24cUxdCP1VUaQGlw5_1W02kJiGXfS1kI6ZTkHhlRLwwKU1mf4EJumucobvsfzzt0omMqZy2e0CoikV9Ne-UNGBQY9dNlJ061WzTWKt3_Psgx9EzSvaOqm7-3isA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام لیست نهایی بازیکنان تیم ملی نیوزیلند، یکی از رقبای ایران برای جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/89939" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89938">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_46HFjjKQWB-X7MoyTDT7GhN4yYolZZoyTiOXbOQgL3w-GzJqf3ixRlcVpRniprOV0DsYM1bpAbCjNQ1n0uViEuReap7-fNQjjO32rbZFAfSoHJ0-RrBzDM91ClBGdaRbEql4GpBI4-01YneOij0fLAPfIpoNDDkgZnxbWix3QZIuQ2mBysrFVy-CidsHdmgG199WFRwP8n6SQGyhxk0WHgvlVzlJ85LNSM0EFlK-OLVII-WUBMkeqpX5pUSO9MgMmv3y1hEnNfb7mtp5pDSxlY5HtiAewqiiqlctpAIx1s8ZJxh8jFoKhSRfaJIdnPG40TRRuzt1RK6ua7gf7rHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نصرالله معین خبر خواندن سرود برای تیم جمهوری اسلامی را تکذیب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/89938" target="_blank">📅 08:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89937">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/89937" target="_blank">📅 00:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89936">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHoI0ENRYsc-zh20r0h7FuWIeRcGJUjAZDW0UBXNFoEgQC0kUhr497BKMpv5MDijTEGADbMcgJul9Oa6xU8a7r5CuC-C3kyigx5IH4BRa_sMPG_RGCcbNgV3gZ3qXrA7YI94koeAxK886OZQd47X0cEGjVaRGN8oRnnfomG5p9nYz04FtuZRpJLYqLIzqYDi2vmagJAl4k5ZS_IpbKGFamgtn0IudqiyihjwqUW24HDRk5N6Zzg1PbxucX_TlhkDRYr0SrGxOcYXyL7qXhw3iB_IumdVbVsmK8Ed-WIzGyROvNxVte_YwOOkDrzslJsHkQXnMpZdPFKhPQp7ylenIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/89936" target="_blank">📅 00:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89935">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYnV_v19oz8VD32QP6Rn1nZ9uZ_HlU9XK-gJmxlSw7eMZWfDrLLjkFscqRuK3gVH-cgbfx2zDO1b-w-RU1l4XatupcNqDnGDJhyVMXDIzaIVVDD9q5eRQnsOd9EXv-TOmR-WCZpNo6DmpRPLFkA8xlmT9ytXkL9qUmLP8Id2JNleXLJUvjxDnwvAoMBiwddc37pa70amzCCCjNIYOkAwES_3PJ1sIoa9NaH_CWGHCEtF0bTddr4-lm6zIoG3XyuxYDktPHdufb9bMf974S9F8wEbghx3lcQp4Tixvf3_szfflxUffQOz96UiLDSi2ckUVsJRHWTN5Ai8qbpoPMCcQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇫🇷
پاری‌سن‌ژرمن قهرمان لیگ‌فرانسه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/89935" target="_blank">📅 00:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89934">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A94Z5grfOg1TTDo7KLvoqqsB0xCTptOaKi-6MRV1G144K3ulJK2TtlP9mnNRS62wpp7BVJrbge8SeFc8jlCCxyBlx2f0utenxIr7McJcf81DNVyv7-Az_TCHhwpnddpPtaal-ShrGwHfT-LFEbIka0xcjJXNO9cgdTBJaGyMDZQ1WyqGhRNizMVblMJm_nVHcGgiNx6VO_lt34ZHUO_rziXWCRTWA05OVvkhzekp002RC_gNKoa1Y8OBYs3IH57PBvCC22Kx1e2B4w_T6y8c4z4UxhI0I6Sx8nNU33PI0PIuYjBNNx0WeH-k-d8XeeiNiGA1SyaKb37c4yZbW63LEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
اینتر با برتری دو بر صفر مقابل لاتزیو قهرمان کوپا ایتالیا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/89934" target="_blank">📅 00:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89933">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgavsypA8hjXDwIw3we2j8W3EDI-R2tfLL8JHp0kS_-pDjmGbtRQcFqfR73vi6lJvIU6ky2hTwgqORxAM2rpTBFHuUAcwkHNdRtCB3FO874ZVbqFGO_WNIV9Hua4YgubsA0CoV5HaLN4qz51jcw_jKwHX1ZJDOBs6rvd17znle8Wau9kZB7G_ib2HZUbuh-bTJvoyL_xbD03J7Y5wx40udE2qb7KfExNzNYH8BXrB1MM1IjiT3WMdGl3Px0Tf9GufXz0F9y1lKW_izFoWeZ5K0_nkUBIku-sCHKH8JiRZpykZmjy0sT_Mbzknk6dEMIz0ldb-DBdBeIBq5SRM-yt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مایکل اولیسه به نخستین بازیکن بوندسلیگا از زمان جیدون سانچو تبدیل شد که در یک فصل بیش از ۱۵ گل و پاس گل به ثبت رسانده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/89933" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89932">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoh6rsJIEZ3zOI8H9H56dKDIKU13y1eQmX2lV3hTghRevvwInqcLmhS8jylokl8fzgq18q0qs-uw6rg7gU2F0YpKkbNtbyI9aHEgIItef_T8R3PwU3meJW0F594g22mc2FkMGcRzePXcAhLjTjzfFLKekB9uWnLVUNlILekHIEBj6D9iM10jDyyG2a-W2-pUj4bi4dRSihtSQIx6QRVLEEepZqSXwJDs1cANxOpL22YOcTsx2cb72RGIPwInz3ZUDkwJ-Ka8FYHQ3ekY563DCzEU3sU6J_CLicC6_AMVoRg-1EOf2xCF1qoy8ViN6jh44R4xdtSk9sWAjifg5hjM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار و عملکرد مارکوس رشفورد در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/89932" target="_blank">📅 20:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89931">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89931" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/Futball180TV/89931" target="_blank">📅 20:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89930">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY-_PaQu7pyq6oKLsrjyxkE1CvrqNZjzMGiDlC_RCQ1r7RWLYbGjBSeqE753lngq3E9YLdd1gSY7RA6xMaomakB50S_fgaZHA7loWuInpZWGdwi92m4vssl19NWG0NTarX2phy4o5eQRaYQE9b9MOBoz1-p7INWu615yBcLNKRDNrVkQNs3aUVQx5FDd583ObutwCX-5dOxsLpBHoTPmJgYvYNSjtbEXiY1fFuJ7A5ChpjHHXUHAVenwzPV-f-WtpsS4L4m_SzeV7HSRj5Kg8DAwD5kgpZXZ1dcnLHaKGZ5TqKN-Xzz5ZT1Z845K2vZRiVhV_w6OQVSMLUewvkQ8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی بدون ریسک بر مبارزه
Verhoeven
🥊
Usyk
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/89930" target="_blank">📅 20:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89929">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
باشگاه سلانگور قهرمان فوتبال مالزی با ارائه پیشنهادی خواستار جذب یاسر‌آسانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/89929" target="_blank">📅 17:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxZE5nlAX0kZq-ngOGczpMvZBQFagaUqfuGSvMEVBHk3pKUcrGJWX8fz2f3ElwimnUhh7OTqji0HiaVq_U_uO_Q7QRcXVaR8mGRls_61W8YGtQLiK3jqKP8jQMhQuecI35NLiUGuiq3koWKC6cRI68urX7B5QtFkrZKC3fSU_MokEahEmqrGcfnsvgAmYCGyKUjP9xFC-vCFbH5ovUrNOkeDxiGfbACwZzkGPfvv4BLMXethtI9EAxRRDrAOvhLePKeLbFqW-3tM62SZd4Lb6ARtsX0-dVN3_vR3k1xGgS9LK134_v41jKoQ9NlobeajZ1GTCXGFntHeAACU5cSzlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
اتلتیکومادرید پیشنهاد تمدید قرارداد با افزایش دستمزد به آلوارز ارائه داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/89928" target="_blank">📅 15:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_ZSuKI9Gs0E6CGlc56d7ab5unSJzhgYpjBgkZYAOwmjewLkHkdRqyWjLhbs9TQsxKW4exhh0buxVC83kll5qQyl3bfq021Ou9SezcbvGf9GjWMpPbqiF15IPV89bFd65YnC3F-6RgZbfsPBJXjkTgE-F3hYkxevr8EYWG8Vcf5hwTqbK22MR3zey9PuMY8_dkoc41egn7iyp-fv00zuRULdi96Cq3TuhdqzWarP3VGaxzrP7zC3En8Zrysa1bqv4_2_cCn_UEa36n3uy3NrlSEVI2J-OPKlfNb9bIEZFJTTYxWz4HsAoIXtHnF0WZ0kFxqmj2y3BCOn7qDjPwPIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
باشگاه بایرن‌مونیخ درحال تکمیل قرارداد با آنتونی گوردون ستاره نیوکاسل برای فصل بعد است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/89927" target="_blank">📅 13:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=GakcnWkMRdkhIFMjhXdez_eSQjUjH2Qew4btwnnK5YaVtuAtgayMSka4EZKj8yx5S7NyhQl0F53ZnGQMtx3VBlc8Gv9w4Uz2Rk10x_LpnfiaQcc8fV6utvYYNW7NJub7AZs_G54DhRrSrFc9lMcCpswwi6b6eMva76ovBKNuH3CuC6sKzJ4piBb269brPh-TRkuM5Jk7CkbgOTaG2AYgQmmoy4-MOS-5hvdnJs_6539q4c_RKqQ1HVbnzOJ3hvGK-BtHu9qsvx7K6bYV4fUMkT97oDqZwiGXK7tr_UZTkHPDA6yMK2cX5puMLjjB2O_IzhK8Nzt9d9nzsjuVtME8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=GakcnWkMRdkhIFMjhXdez_eSQjUjH2Qew4btwnnK5YaVtuAtgayMSka4EZKj8yx5S7NyhQl0F53ZnGQMtx3VBlc8Gv9w4Uz2Rk10x_LpnfiaQcc8fV6utvYYNW7NJub7AZs_G54DhRrSrFc9lMcCpswwi6b6eMva76ovBKNuH3CuC6sKzJ4piBb269brPh-TRkuM5Jk7CkbgOTaG2AYgQmmoy4-MOS-5hvdnJs_6539q4c_RKqQ1HVbnzOJ3hvGK-BtHu9qsvx7K6bYV4fUMkT97oDqZwiGXK7tr_UZTkHPDA6yMK2cX5puMLjjB2O_IzhK8Nzt9d9nzsjuVtME8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در ایام‌آتش‌بس درحال بازی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/89926" target="_blank">📅 13:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89925">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VncCjyEK7QBFWZ9m2oKF9pD6JeSl3X-TZ1k8YEEfdiPcSCI9Z0JvNOU0UQvfNPXdJQNHDYgAiO9bw10bOoHinlxp1avdyKFi-_zdzbnzNtyY65oYBzpghMYwrz9KU_nb56KsfjtXTdQoOnaAUhXQ1Qt9zhTo93PHv7QIWXq8r0GGOKceFQwmP7NytXiTRAtrAKvoDSsFvFRksHT4BxHllQlyWaZEZnZagIDCtpaS4LfFJd0CS7WtgrW1pAAO4RunMw0ZOH2l0IWpd97KY5lcORQoTHcs3kkioE16ZsqCd62hsvLfu3GVQgKiaIlnJEhTR8oHOY4yuh-HeTRc-QJY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
برخلاف اخبار منتشر شده، رئال تا این لحظه اقدامی برای جذب رودری نداشته و این بازیکن بزودی قراردادش با منچسترسیتی تمدید می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/89925" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89924">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d13c-D0MzN62DhSEEFX8-lwqV_kz05M7nBzaqd0Yd_XVyoBuVc5JvlkdoKrlplMTEZy68tAIvcVCGbBbw6fI8OoU9clKwiUoxkqGlfdqeBjr8KEpbWvyMvNuJ9NkKgpBylLsrsXDjM6PCIA0vdkCvPIP2zwjIt9USw7cFy-rH9Mnmfe4tv5wG67HmW0PjPB_em4kL09nkcmHaMBTkgCFDQQNqgrAW-AGGCo3pWTvJYbRynAPYYQ8YMncBlXFNVsRbJ5-0o00AidmPHZ5oE7TcjnRejueJMeei8NuD3AUgpeRpOlbTfJjYZEZehOhMEJkQsOWipQYvn4Q6QtZ4cAhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
یک خبرنگار مطرح لهستانی در خبری فوری اعلام کرد رابرت لواندوفسکی پایان فصل از بارسا رفتنی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/89924" target="_blank">📅 12:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89923">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CailOLHLJEkSKATByio7M_mxccltXKKjPxAuklOQj1KEcyOUDF6NRxJJqIlcTE5mjmzgl4jld8-GXACGcjOOrW-bfHuBzAL8BXAC-QdvgIPAGu_nKeRYZnCqwEbJJ357VTUZonrDSd3quFbrTkpkjr-tS8KnjhlYbZEHKi5Ac_KEttG_7BVhAzZy6J4rOK7AG7hr5DoiOPyFMU_dlYJAzBm3xHGY9ixsbqqDSflv5m06StfM117adxx2s_8eWSJ6aPljoVpBhDh_Gyxz7VxFo59Dg7fc1ICUNzBiC9z3IWPUI1y5fa0hGGT92NNeaVCPCp5Vq_AgwLTQ1C4rCgZVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: قرارداد مانوئل نویر با بایرن‌مونیخ تا ژوئن سال 2027 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89923" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89922">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uka5SnHBckDFdMze-FBvinqhehc1xfvZSe_Vqt17I7QoNLn3QaSW6OrWitHHEwKfjY2Pi1lw27jq0GxcJ3HmRezwc8U-72cm3ifKVNxeeJfQ8kjaYgPEPVGYkxjQg1G69_-0zzR8tTtiGrv1WSzlwLCoGlcShTfzGTta_IZU2U2gfhDO6j81_4P07MdM0zsh_iTN2jAnerN7Bct4AbbFD2QhP76n6imTP-hiXTc0Cx1s9z2y7YYNg9F68WMjCKsouuZejHiT2yBznXdmoAvRqN5qUMxQESEpGaUW9ccUpJ_fUiOWNcJvSyZNfht87BRGkigmQcUujQHPqkQr0H_oHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قصد دارد برای جذب فده والورده از رئال‌مادرید اقدام کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/89922" target="_blank">📅 12:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89921">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhsfItmIGCaf7Dglhac3GP8h7V8nmHv3BzzUfzqWrrhKAAjk1EUJgNci2SSf7glMGNsK4NVGI03SQd9KhovIE5wXQRmOaJIHt4vTKQ7abX7juQGMmNC0aoc5RD3D74hK-XzalIwCsP2_xOBlmFwBuxaPymFw_P4Med7aXs28WZnkn17mA5IR-0IOnANEgJ9OyCSShG34kmqOSkXUytYgQXXaPTQJ6UWa6Q5IDJhtRWfqpIk6aU1_ExRBezYhcFw1mGBfx9ZDbD-bXGYvjKDvPdPD_r3i0rP0XlBCNVTm8Mdin1nq3wbe9y1VROkjB5htOJ1Prb0L5LKgFRoQIn2Czg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
فهرست اولیه تیم ملی بلژیک برای جام جهانی ٢٠٢۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/89921" target="_blank">📅 12:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89920">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph_yfIj1InFDeVwOkHWNtkmDd7dcrD3pmHZ2Ec7uzAVHg4T6EAqxdboLdYX5UKC1dCpsWig7Mi4JKvHgApuyVjpEiq7ckxO3fukm7WUgyU_FLb6jmkiu4bayXjrk2_zv4JzoSDpsPgMCC9MuQiYux3mbYxUC3J3kFyJGz_AosRr9QsEJWr6QJ9VxQml7i73244uw1U6EYR5xADHOoChEYOIMenLT8xSHm95uB1TnuswYDIcYXrE3bAWLsXu6elo_HztzGrzvP5sthYzzkQL8a_nFmRSQBTnP0ifaHDlspoRKFky5vbACzWBJPibMrflrumho-UlLLEGwjP1UmmI8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پی اس جی مذاکره با اتلتیکو برای جذب آلوارز رو شروع کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/Futball180TV/89920" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89919">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89919" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/89919" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89918">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSl5tFr9fwSHqT8pqXa2TAqH8Sn87mBrFYK8gmPwksNXJrLhfNtvNKrIjGh1Ut8b-mSY7YqRPm5YuizjCtBdk9V7xqBWMooGyot2uVBUhkwmretxcrTaLwzkPFAYy0dD_lBRFXUHi_NsSAPQqvQHXpewdhKtb10JNyup8ey15XB5GOE1jraC1fsVe4GNzBiqtUPE2TXm99tyHZn0Ra3_qYYmqo7lEkgx1T7DI-zIyJAAY8M4s0e2X1NxEn3BuIoBP0e6PENdLlUwXZwI5ig-4cB1n2zIM81ymeqpDUm5l24TauvOCnFSImQKizP_XJHixIYQdNSgjJt3W9vlBaSHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/89918" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89917">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
آمریکا برای جام جهانی به پنج بازیکن تیم ملی عراق ویزا نداده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/89917" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89916">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=MHA70ebN0tgQLztWQeCuSR6xoTSAgVjxA8kbqiKbeQviQuL9tnnbJy4Ibht78y5Eto5PWFQwJbSmxPZPJdATX64LI9h66oIm-5-Fa7Mqy9QpYKHMucB57uaTsm_mTrnr8xbWJGfQTqG8215XL44FWYPo08SVtm1KgFNwXwrLvEzCK6d262XQCB_eoLo3xCpNxshkYXZSoD4u06BjCkjUObEOa01IZDk1roQ3wy8Fu9j2pXS3jZ5msRvCPwsU3iZYPdvmcHN7ltLt22HnS-FDs2IzAZDp5AEzT7cEerJ4-pdi3X-EMeBuBlxX4hB1nrKutHw1-EffNkjFgPGSI--7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=MHA70ebN0tgQLztWQeCuSR6xoTSAgVjxA8kbqiKbeQviQuL9tnnbJy4Ibht78y5Eto5PWFQwJbSmxPZPJdATX64LI9h66oIm-5-Fa7Mqy9QpYKHMucB57uaTsm_mTrnr8xbWJGfQTqG8215XL44FWYPo08SVtm1KgFNwXwrLvEzCK6d262XQCB_eoLo3xCpNxshkYXZSoD4u06BjCkjUObEOa01IZDk1roQ3wy8Fu9j2pXS3jZ5msRvCPwsU3iZYPdvmcHN7ltLt22HnS-FDs2IzAZDp5AEzT7cEerJ4-pdi3X-EMeBuBlxX4hB1nrKutHw1-EffNkjFgPGSI--7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درگیری هواداران الهلال روی سکوها در دیدار شب گذشته الهلال مقابل النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/89916" target="_blank">📅 11:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89915">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHGPjjUtH73RfjSGTlIxIZCnm8X0LeGP2EIzLmVefuLF5CJ35jSlLWi5KACRxhUc42Oer29SgAvJD5GSI8MqV5_SfdtYDI8n-lgQaeD2hbr4XTbQ5vQiyeR2WU3nMdYYbABvYuA1kzP1I1KbUR331YxPJZIze0qrz277HJomNC1PinajnY3qIbdmwRrwI2eg76YSlIJ5UyB_jPYBH0kU4YptaQ6yWKzsV3e-9JWSUKtTz-4TgtC3rYgJwJQ175vOO3LZaK_u4Dxoe3Evcz7lpMpGDx1xQxzyCGbOAvE0QZnAOEL1DspnfRwXCZtyftdaUwSyhv24tbJkgdNdt8COAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با برد ۲-۱ مقابل الچه، رئال بتیس موفق شد بعد از حدود ۲۰ سال غیبت، جواز حضور در لیگ قهرمانان اروپا فصل بعد را بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/89915" target="_blank">📅 09:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89912">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حمله پرز به بارسا:
پرونده نیگررا بدترین رسوایی در تاریخ فوتبال است. باورم نمی‌شود که هنوز حل نشده است. داوران همان دوره نیگررا هنوز قضاوت می‌کنند. آنها هنوز بازی‌ها را مدیریت می‌کنند. این غیرقابل باور است. بارسلونا برای خدمات نیگررا به مدت دو دهه پول پرداخت کرده است و این داوران هنوز در دهه سوم قضاوت می‌کنند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/Futball180TV/89912" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89911">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
پرز: رئال‌مادرید مشهورترین باشگاه دنیا است و سایر مسائل خنده داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/89911" target="_blank">📅 19:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89910">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
پرز: با هیئت‌مدیره فعلی در انتخابات شرکت میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/Futball180TV/89910" target="_blank">📅 19:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89909">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
پرز: دوران ریاست من بجز امسال با کسب ۷۶ جام همراه بوده. هرگز فراموش نکنید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/89909" target="_blank">📅 19:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89908">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
پرز: مثل سگ صبح تا شب کار میکنم(جدی)
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/89908" target="_blank">📅 19:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89907">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
پرز درخواست برگزاری انتخابات رئال مادريد رو سه سال زودتر اعلام کرد
دوره فعلی حضور پرز تا ۲۰۲۹ هست ولی او برای نشون دادن اقتدار خودش امسال انتخابات برگزار میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/89907" target="_blank">📅 19:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89906">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
پرز: متاسفانه استعفا نخواهم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/89906" target="_blank">📅 19:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89905">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/89905" target="_blank">📅 19:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89904">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNKRX6gG8l_tQjDqT753yXYve1yW4O-s6vHRzxCiX1qhREh2cKv9T_HN-d5TaTOZsW_g2GLuhfaX5D6Uur3GkXo67aY4VgPmJfteT-_F7OPnfz8A5QjxwfJ4aPeAiMRwmg7X-1CXpF1Hy8HG0dgn_rUhgT71u24IN3qdQiRhPyOq7USj0VDGA9lmJaLt0o8hDd88FlANmKxAzYdXR3PxSZtAtHodh7BibAODjalrYelDud91R74ze7MhHZPxjQi-I5O83cMNlTMEtBg4-L_SXvde3EWjSZt_3FzKCBPG1w24NrcJLST3ile_rxm-mViBxB26_u7q0rv9bVq1uX52CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/89904" target="_blank">📅 19:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89903">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPwrBV_bP_JHfxASCtqFLlfXJZOm5R7HQ6Axw4Rhrxt4iyXdxBXxElXoHFKpi5hvontbo_qBkFrUo4C4cPTmV93_X73mbh_aINr6euX8O1wjO34VdfErSPHgwjJkfPwGu9rlr1o4UNrBjlNWOPh8IfUQ_ufC_zoVydQuZcdqLcDsqo2ZKJcomF6RkJlbTS1v9Bx_n5CtVRR4qLz5eDzFsxnxZ1pwKZHavk_R_eJzomce31UOwQeTkXzsgJ5lZtTLPK8e_2SLtFOcHKV_Y1ZnJAB_1B1UMFSpU72obeVjhu60YKJZHHn3sPVOzKsz7cl4lvkJFCbSiQgl-LN8ryklMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو راموس باشگاه سویا را خرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/89903" target="_blank">📅 14:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89902">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB2cGkX3S2WhVa7fW6YxIbhjOhr5JTfWLH78hujSmeRTJklI39vt3m5xP0p3zxYlnsxEzfa1xoCRztSLc5k3mKInv38kuaZtP9qa9xUfmI5EtTCUBFdceTnV_oK8LpdUGLNeFiIfukG6EI_PVFSlFbciBNhcJvMAXc61xy0dxlnjwKasgrbtjPqaAudoQ9ossfPVbmqyUz8fACd9q9NXtfw29pQTTjDAmjhCDzRPY89b5_8Az1tG-r6B2MgAHy4sV2YdA6TYbpUkWtWIKVzrIUK8a5WmjW8IS4RGYF_tkQ3f6tWNAUNX39Vw823mojhuyu1V9OqiMj9WdRc2BV2tew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
لیست اولیه قطر برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89902" target="_blank">📅 13:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89901">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfWii5-XUJVdespfV5_wND4HyF9FVTOVaul0NQ3dgHdDtDuxtIWaTqQe7X7OeTbIhSVMmB7Zqaw9w0kRq9HRD5n2nrGHkDFNYQ_MQOYPt5CCfJJSyoNGtRL-sJqomnY9PJZ10ddSOLOcoC4p_htMxYa9W5D44PIbGisItNWnVHKPfTm3GdpIb-F2kQIz3SgX6wGuDbCJKXUxi9pcgQeJfSawpYSV7IMXH-SUnWTn6s3tcXRF3fby7nnOAet0ghD184mFpoFFG0eqLGblbh3fMkIAS-Su2VWmITuSsKbWsY1YbtAi0iSU2P0Y1Jd5a0t5QglK3rwR4C-k35PCgjsQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
پیراهن اول یوونتوس در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/89901" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89900">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddYeAXegQAbKcW5AGm59gqAIpqPBKF-IM_Xqsva0xU580aWy-CHIbK8mTyK_TMX2PlRWa2TTMKoR_QefaeVSwWigpUe2T5UYbqHNjllaHj6CbYUgMlvrMfSSh5551fjwCtkqfIVEptPml-qgYM58nw4xftI7U1sBN1xFoSYWWyYNVN6g1RdKlOw7g9Xny4QwnV_p4fIA6D5WqLS3DIeaJSUIc54ysi5RauVdtSc2vk61MI-GilQp9y1BQ5r-9HwOrRd8ZgVaWlAIGVBcM1RbTcjV4dgUEF_Q4OBpPlBYG-njaM1KsPVi9eE4wVdDOtzP-pat8sHQFVq_F110JmnkzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89900" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89897">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4Zbx72PCJydcM9h7GIcPHr39mTT7ysKl7E4Lw0WMc59TC2An88ae0CgUCUdEB1HExcILEbW8clSH0HWAcd6Fz_37f3fsSqj-rl3uICowkz-mGUI4nk78lBFY3IgOrLXgMK79iz3qdwzTrCTbYnqKuXjZHbLIZtuyzHxHYzn23xzjqxlpaW25_lovBQDRSo5vAFbSxGmU5JohFzziEMXlgN7t88Bc0wsJVlgqGhEpxX8csBbVbIiT-oJAKnWMPh9cJ4szi1GcIFgmEf5ngl8RJkpeJdYtqAX_9Up_m7dXofewHocakX0QlEWqXkA8KgDPUn4bfsHNhrXxDWme_DZDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/89897" target="_blank">📅 11:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89896">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbtK2-7N_xeSY5JtY0xNQ6NVGetKn531XqkmIT1-qfwmIyK1V7pCXbg1OooIdyDwf5Hk6jmQK26e1Zzw9NL8F-QKqroThUwgWRDimgn_bGZEMBNUBwNpZH9vunR2dXzWnUXgtvuSAx4SQ6afAsXDv4Ie5DgOFDYjCQZoyOs_KemZLNFCJXKYetx1rjmwMEShf57gN0swEM06rNrCOwvZXYP-CnBxSEf_uYY1aUCO2r4USNSRLdA4Hn2tb2ybpB1uAayYRzbs_72qzZAvX-XwcGhsdzCTaTkmOthhMMvvMhYJTHeij5P0Fj1JFs5taJx3dULBPUhFJUFTWgOc01Egrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسانه‌های اسپانیا: امباپه خواستار فروش والورده توسط رئال‌مادرید شده است هرچند وینیسیوس و بلینگهام شدیدا مخالفت کرده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/89896" target="_blank">📅 11:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89895">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZp6uFKqy9MviIcxRGxYkNZc5uLf627eXY-JIbkPnaYDAJhXObyXuDYa5A4HODCVWhAJcdd2TTPTBL_M53D48_oVIPWRM4Re7Pk9ItHkbmB20OS_8iTCzqwp-JILbjY-rvJbWOtU5WGisvTEAaVsTDccbrixQ71oImxvLJsjoFIxrQ4qei-fRPwJzudJwO3DV7zNCrUPoDEkLD5R8p_SqdTKfrwIpZuhsdmuaYfIZrDtKXfkhEtRSjRz3YnaPbzYIAEFPzVF3qanwkZA8-56u1PWVeEjERl4w9WGld2hcmBsi2eiiR0C7EPEHqJiOXI_LKbKAwMxZSEaz8eLcdhZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نبرد حساس قهرمانی لیگ‌عربستان
🔵
الهلال - النصر
🟡
🔥
امشب ساعت ۲۱:۳۰
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/Futball180TV/89895" target="_blank">📅 09:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89894">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=VcpvWsCwna34qQRJ2g3P97V9krQomJ4w8bRfi6nz3l-5nHRwhsz66r7mYweCeoqoNHUOzf3xs7o4cFo1l3SZEuWTsAjB1mMZCLZblaCCu-kOUqXHQcMeWKSEKpHIfO9pIUkczNdecKjbIDtIDI2HRM7U8FQdGYh6ytzXWn2YTHYVmV910lZproQb2TI4HOM2h92CD8iq_TQ13-BPjf2Fo7hnDnSNmGz_a0Cnqv-STTez7FUhahqdi8yiiIN8tbb8tnJKTXq1ELUGSvE87PR1fJkqBqbLA-O10u6cf7YIOG5zGozCkBeRbAuJTw9K2J8v3-Aksj_-fiMMdmhPf5QBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=VcpvWsCwna34qQRJ2g3P97V9krQomJ4w8bRfi6nz3l-5nHRwhsz66r7mYweCeoqoNHUOzf3xs7o4cFo1l3SZEuWTsAjB1mMZCLZblaCCu-kOUqXHQcMeWKSEKpHIfO9pIUkczNdecKjbIDtIDI2HRM7U8FQdGYh6ytzXWn2YTHYVmV910lZproQb2TI4HOM2h92CD8iq_TQ13-BPjf2Fo7hnDnSNmGz_a0Cnqv-STTez7FUhahqdi8yiiIN8tbb8tnJKTXq1ELUGSvE87PR1fJkqBqbLA-O10u6cf7YIOG5zGozCkBeRbAuJTw9K2J8v3-Aksj_-fiMMdmhPf5QBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی محمد قربانی برای الوحده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/89894" target="_blank">📅 09:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89890">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=v4_z7RYxB8hQJ4_VONri2rOVF1TlLp5RV8HKFWjys71i0AfPNcl6mHr0PYW7ZZGnii04aJ97Rd0jEHtRRk_Rhg1nYdOdIIpHn0nwe_jEe8-2ph19I3nPAiLjS2PIheBWVh6TcrkwCZrx_k2xywaYznT3UuRqYT0wmvShNep52g_xR5GUFIAcZpDiE8F6rjvS-MRItKrYsPExRa6OmvwWxBM4K5Z6G8U6SNbo5R2knOz9MwbY2zzSmJgdgq3P1VgHa9m2xrI89QiGLW3cg6w1a9vbdF6mIw2B7Mf6dU8JCotqmVSOfQmbSDlDcIivHLxiOqPxamcunjEXnOOqcXHP3X7GEfS30Tj3WlUQ-ZOp-qgsADx7Uwg5lzLvVDX8eIiwhWy1fnF8mbTnpyOrn2A3bX9NXp3rXQf00CrcK4euTRgdw-Fv-xG_gfQP9K2lFK8MXkDC-t-ghGVGeHnDaPfNjKr2tItINdBUzgDHJsZPt0WXtcAe7rtiYTbKLoj_ROqfgb3Pa5bY375QirT05alTAdRfRiGFsaohduZQb3BEDPIjU3MI2bIqD3fbV9jH31plJlBl5XhcMvjFPniG_y1atxoL2LxwWsgzIzQr20Y1hMRP1dXPXhVg8saKHWRqEZ9ydgWJibmHwCQa7EHmR9DxMQ5bOD_hIuC1md12GXp4aMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=v4_z7RYxB8hQJ4_VONri2rOVF1TlLp5RV8HKFWjys71i0AfPNcl6mHr0PYW7ZZGnii04aJ97Rd0jEHtRRk_Rhg1nYdOdIIpHn0nwe_jEe8-2ph19I3nPAiLjS2PIheBWVh6TcrkwCZrx_k2xywaYznT3UuRqYT0wmvShNep52g_xR5GUFIAcZpDiE8F6rjvS-MRItKrYsPExRa6OmvwWxBM4K5Z6G8U6SNbo5R2knOz9MwbY2zzSmJgdgq3P1VgHa9m2xrI89QiGLW3cg6w1a9vbdF6mIw2B7Mf6dU8JCotqmVSOfQmbSDlDcIivHLxiOqPxamcunjEXnOOqcXHP3X7GEfS30Tj3WlUQ-ZOp-qgsADx7Uwg5lzLvVDX8eIiwhWy1fnF8mbTnpyOrn2A3bX9NXp3rXQf00CrcK4euTRgdw-Fv-xG_gfQP9K2lFK8MXkDC-t-ghGVGeHnDaPfNjKr2tItINdBUzgDHJsZPt0WXtcAe7rtiYTbKLoj_ROqfgb3Pa5bY375QirT05alTAdRfRiGFsaohduZQb3BEDPIjU3MI2bIqD3fbV9jH31plJlBl5XhcMvjFPniG_y1atxoL2LxwWsgzIzQr20Y1hMRP1dXPXhVg8saKHWRqEZ9ydgWJibmHwCQa7EHmR9DxMQ5bOD_hIuC1md12GXp4aMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درخواست صالح حردانی از مسئولان برای معافیت خدمت سربازی ملی پوشان فوتبال ایران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/89890" target="_blank">📅 00:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89889">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=tUX-9r_BC1Q5YpYequtyIgHSk88he6VK7Wf54atsZPXfq_wzMerkzNQLEcAxz7VlkC5pgCW1rBaVyvoVtgy5fJsptnenIn_RQrzgdMUMTL7q5q6tbLBkGMJ-xMrzEPWNgGghWAKf_M5dNWHlTNeFZ3bOnEMopmwCzaOu3EA0iMgVNTXN5Pg5fwbOljtx2an6aVjzon1I9JnIoEILaK-7wRv4G1sl6aEKhus4YdXKRhEQbUT1bl4cDo4YQ8ikNVre1d4nyTwTpRJkoA1pvPlykvR1ogHW5ZfUFXlUcTWYiNJRfPQeu2Qtl7ZOEGbolhAn7E5n-jL2DRbsKtjMVvbsbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=tUX-9r_BC1Q5YpYequtyIgHSk88he6VK7Wf54atsZPXfq_wzMerkzNQLEcAxz7VlkC5pgCW1rBaVyvoVtgy5fJsptnenIn_RQrzgdMUMTL7q5q6tbLBkGMJ-xMrzEPWNgGghWAKf_M5dNWHlTNeFZ3bOnEMopmwCzaOu3EA0iMgVNTXN5Pg5fwbOljtx2an6aVjzon1I9JnIoEILaK-7wRv4G1sl6aEKhus4YdXKRhEQbUT1bl4cDo4YQ8ikNVre1d4nyTwTpRJkoA1pvPlykvR1ogHW5ZfUFXlUcTWYiNJRfPQeu2Qtl7ZOEGbolhAn7E5n-jL2DRbsKtjMVvbsbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین یامال در جریان جشن قهرمانی بارسا در لالیگای اسپانیا، با در دست داشتن پرچم فلسطین حضور یافت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/89889" target="_blank">📅 22:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89887">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksL68BMTcRTN78MAeoWY7Tah1razQ3dxz5poq-Od4041c2EpPU-voE3-cWSOHZr9ijtlqYO8_XOuWQ_Xyqqouf92tYiu95i-JULDtTR_P7Dgb31CQkitgdoUwKcql3WiyFz0Ad0iwYK0Rpw3qJgtktNCv6oRpmBssCn0ep6GypHVTtLwPN3bV8BIyRSTOGpJ0-8odnEJ4zjO5jg4IRoI3F_GZrOZsHh6F3Ii_cfyVb3A_5EfnDVN6QjvIdgd4k2ficbQRxBukfwg3d55jTDbQFf4uu5QbA8XfoEan5zUKMK81RwQEY0uq9jB19q0jdtt_ceDJSyn4Uugrw2-hIqDMRmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksL68BMTcRTN78MAeoWY7Tah1razQ3dxz5poq-Od4041c2EpPU-voE3-cWSOHZr9ijtlqYO8_XOuWQ_Xyqqouf92tYiu95i-JULDtTR_P7Dgb31CQkitgdoUwKcql3WiyFz0Ad0iwYK0Rpw3qJgtktNCv6oRpmBssCn0ep6GypHVTtLwPN3bV8BIyRSTOGpJ0-8odnEJ4zjO5jg4IRoI3F_GZrOZsHh6F3Ii_cfyVb3A_5EfnDVN6QjvIdgd4k2ficbQRxBukfwg3d55jTDbQFf4uu5QbA8XfoEan5zUKMK81RwQEY0uq9jB19q0jdtt_ceDJSyn4Uugrw2-hIqDMRmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: من از کردهایی که به آنها سلاح دادیم تا آن را در داخل ایران تحویل دهند اما آن را نگه داشتند، بسیار ناامید شده‌ام.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89887" target="_blank">📅 19:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89886">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=izATqa9uyEaDu48wNIWvtZsjHIqFpLou_TQRgp4B93Ac4q5RRBMRXjqxlgYWe98aSJJsQCWpJTa3DpWHDWCsNa6lITTqGSaU3bLoIIvMvWHk4o5oedsVX2sGl1_zJby6biqfT7L40IjMusQoSEcL7ZIbOB8WzvzD3W2zB7Oz-_Q2eQt9Koel08PuwYjSpYnW-KGhqvy1eVFtImY_fRXfj89ukN97rLn3zBbO-ESSd_YkBwvBezOh3B1Z0X_5HJEztYBlsfvXqSPxMB8B5Gwhj0doxqiQKW_tdqZS2_HP_2QoKlO0vTTpZV0ysGGQeSD-T5jFjQ_9LdyooqoCFjSnMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=izATqa9uyEaDu48wNIWvtZsjHIqFpLou_TQRgp4B93Ac4q5RRBMRXjqxlgYWe98aSJJsQCWpJTa3DpWHDWCsNa6lITTqGSaU3bLoIIvMvWHk4o5oedsVX2sGl1_zJby6biqfT7L40IjMusQoSEcL7ZIbOB8WzvzD3W2zB7Oz-_Q2eQt9Koel08PuwYjSpYnW-KGhqvy1eVFtImY_fRXfj89ukN97rLn3zBbO-ESSd_YkBwvBezOh3B1Z0X_5HJEztYBlsfvXqSPxMB8B5Gwhj0doxqiQKW_tdqZS2_HP_2QoKlO0vTTpZV0ysGGQeSD-T5jFjQ_9LdyooqoCFjSnMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😄
🚬
شزنی‌همین الان وسط جشن قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/89886" target="_blank">📅 19:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89885">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYOadZ9qVOGMTjIHW0BxV7D3HtGd9-VzuhBy1YmFbCPlXFawQhrEOWr6de2kw0QGntJ74Z3U48IQ6lGTODS-baLznEsa35xywDup80UurT8cFNQCR3sgPGHtaGEvmWALz2TB71k-SCqUIFxy2N1kUVh_Q9qsIqQdbo48xgRS3yqLnLjzhbTauudY_jCFgUewwiRbmjgOmdQfiL0ZH0TuAFLNpo753XHTARtlCdg26qkkpYkcpO3VhHzjYKN5MqsS0CzfPICjtMiijEVeeM3Z9qu8jXvvJIOMpF8qQH_tXrTE4Sl62s2eVsnhVd5KzBUvDhL9n7deCRmIsFgb4pQrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ایدول‌خبرنگار مطرح آرژانتینی: لوئیز انریکه سرمربی پاری‌سن‌ژرمن خواستار جذب آلوارز ستاره اتلتیکومادرید شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/Futball180TV/89885" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89884">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeTfZvLoQaKKiZB4Y2gcT0ALS9Qc-z3g7Rj74Lw2uX7jw0E7UZxRrR82iSmap9Zbip3wnKY_dVLIPBsRbiQQfXKfos2ozPi04XrOEOKJYSo-1WGniYEYoM3tlfLN2odtbMfj02Wq6uwcKinfGSUJLKXMwG5W4Y9FINLVuJwRQwb4Nwbcb_nE5p7f3WeRNDd_FNS-nO6Fddrg0jSinti36JZ_WvpTYbnrzq8CQEtzFXCFcStOtBga2izECKoNgUanseHaYHaifiWXlhqJAbN7iudF2VWLn379dodhv9ewBjxuIdE70EmEurDPUmwQKLKHvQ9wnkyKNFjNwYG0BSrA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇧🇷
لیست‌ابتدایی تیم‌ملی برزیل برای جام‌جهانی با حضور نیمار ستاره این‌کشور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/89884" target="_blank">📅 17:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89883">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS7sLKjz9hS0sRifo5y5_R_q35iNRsLO_XwVoVlNxwSHsKKNjYH-WZWBT4G3GYlBCCri4U9G09fHOhc2Io_d78uaxih6WU2WoXMWr77rq9Gh87Q8JXze5gjc61xLAA3oy0YgMCV3SOAMv9TmG89CI_uLHeNWHwJTRDG3-KXFHHBSiaZAM97i1ltRx5YaDDJRapcPsotJYngbXsvOy3RFr8Tm25wrH17TM6dGQo6fdKlxyWzcoXg-RnwgXMMbtBU83EqdniSGZip1KQiXj6i5HVUMJcoR3TUYy4vsIq6o1Mz0w8D7T-9bZWWXId4vGqBj61sgolrbuK2M1xVRyVmwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
👀
انریکه سرمربی پاریس: باید بگویم که به احتمال 99,99%  قهرمان اروپا خواهیم شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89883" target="_blank">📅 17:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89882">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAVdK4lrCdkSVdV9tTS28pMUnEKjIlLd81phpQHjA74Hn5pMqh2Z2hasV6f0pshhDJV53HvI59KW6U76ztWv1DFHuqSfrJxfDuFzP3L_cO3EvfYnsThmmari5BRCQSHay-cHz3b1NrxOZ4QjGp3hiMC4tFrMe4c5hGHgfXaB7vFvPGli-bwfONRfHQeDNlzZw5wJGDd_h3utDeTVry4SlC9JfNQiaxJtUCu5VhceZbmHmR6nrhWtZ8HEe2X42Rc_dFLp5GpOXPgvWNFqESrMkhNcHIMaic83xl2YNKjnHJfsNZVlWo8EEvWgOdQRqInSE9i7q1qLqHcXDj1FoqJVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
خامس‌رودریگز اعلام کرد که پس از جام‌جهانی از میادین فوتبال خداحافظی خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/89882" target="_blank">📅 16:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89881">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaN0BgCZK6PmvGmSSzODp6LbKeVB_0xSFxfnRJTPd2DynW--h5PP1sNqqtDFobSN9wyRE18QOkJok3MkcsIM2qtVoo_GsmOsv_foSUtFajoNlRRM9F0zYpVXSJQkwTrevMs7uf730FzHc5TmZAxNiKRvZ8LOMEs--2vK6NU-TD_ctT5sEbF1HJI3a0hloeyQM_xNfAh2sNa5jE8gpvskyFoe1KlyVZeDYdLesizo5KZNzpSWvT6gJ7F-514JkfNK2rezBF1qM90tmd2rImAe3-8-vco-vbZ-RNFBoB-VaQ0y7xe7Ytw78ZC0GDB1tcXMBhQHP18-XCmqT0D-Q36bQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
دنیل‌زیبرت آلمانی داور فینال UCL شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/Futball180TV/89881" target="_blank">📅 16:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89880">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAb8nze9SHV3UJn4S7oFKU7_vHIxDpvgnGjaQlxyNl7t1_h7h9bZUmozTrSpsj3Ej6_pgB0hR9I9eGR-H4IhJf47jLhwKMCmsj5hp0I0BAK397f190mPlndTgPGcy2w1pVmohFTbKBZuO_V7KNVk-9lepoIhD3bhzpjcM6T6ZTrY0bQ65razFcevgkDVZBagaVpzZJKCFSvAMOQLfrq30c9T_jTalKlNFiG_QPvUDOEKunJ0Kw5Bmh-GU_otBwgAT0EOJVpv2gV3d4fblb7cIdvAZ8KC7fpwn4XK6GHzVWokF_ZYITQ_zTOkqqixahgc4VGGUBYkeVfOT81ZRqMEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فهرست ابتدایی آرژانتین برای جام‌جهانی، دیبالا رسما از لیست خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89880" target="_blank">📅 16:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89879">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6bFw9iW_GlZj7YWYBrLkyrRRrM0UE6XxQtWgVR4o5AuRZtlCHXKkIV6duiXtZ0BvrADvnh9jnkjIAqE62nqAP8j6QsY7vpSXXmUaXFXosAKX6O0rU4xzQ5Y-oWiVhCVu1NV9KM0ICw76T8mHz8O6RijnXYKAX0SsmsaaGrgiUkfkifyzzgVfrb-IZj25fOs82sv4etYSPTV_ojG2zAyYoITorfmgZeOxybTtojWH7Mm8elizuApzx9HM5zbQfeAz5VBgw9d2kfXstqeeA3BRUxaBOARMnvV5Y0YZ4XftwCNJCOIP82LVWF189hMxv26yzEPWQG4oeUJO-JKJ58XtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💼
یک ماه تا شروع جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/Futball180TV/89879" target="_blank">📅 13:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89878">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
⚽️
در آستانه جام‌جهانی، یک شهروند آمریکایی به ویروس هانتا مبتلا شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/89878" target="_blank">📅 13:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89877">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
کنفدراسیون فوتبال آسیا درخواست ایران برای تعویق در اعلام نمایندگان آسیایی را رد کرد و بدین‌ترتیب احتمال بسیار زیاد سه تیم استقلال، تراکتور و سپاهان نمایندگان ایران در فصل بعدی رقابت‌های آسیایی خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/89877" target="_blank">📅 13:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89876">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWVS4v04SFcxFnjiVB36TU_ZtAHIG636oYInki86BU8sY10nUQvyY8vtoHIimuptqpCu2dfWadOkTHtHwjYn_k-b1Dan2TCU4Mvh0UbyXXunIpTTD_vLPWAE7_ybfNKMyLJgkygoghwtd56gVHP5A-BSacPB8jFIj2lQwibfYdPmMsrPKemmdJ_uFJ_S0m6pF_jMqFgDDah22mZWmUEiKsaXUR9KyHmcz9FEh-peUAGI4E32nCV7_n1drxrL3Hzvvsp40y_UrzRQgZwH_DPw-_lUIlJTu0qU9u-ZB5KBdfmZMKX_XoPu7KrmpnxMvWFEeAKMHaxw4IC80S0DoxG4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/89876" target="_blank">📅 12:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89875">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2SA0Ez5zjmbTBciRcEqH3bFdItDaYxOTqyx3yDbWbQOPK74IetdyIOZlU3wRmpNBQZrBc2u1ZHhqq2xO4ycDGNZnNhmx_sfiOZcbWDxzYNFS106c6nmrv5INcmdyRh4vZwqI2VNO_h1VPQ2awWJ5CBUFvAvBsp0s1zBaYACjK9AihdBsz2iYqA4QH9okiKlw5_qgQmXuqFkrfZP2tpQJ63Kfj2IieQhtl4x3uARdVAzw8v4MZPhXAaXO_eGtCQsi-R4K0BMzOzmeC1Xh7GdXB6Ao17pzQwn90ZslZFyur_zLb923iDzFV2rp0P2idKEJ-zTXBTRLzsgjzut9nuPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
نیمه‌نهایی سوپرکاپ اسپانیا ۲۰۲۶/۲۷
🇪🇸
بارسلونا X اتلتیکومادرید
🇪🇸
🇪🇸
رئال‌مادرید X رئال‌ سوسیه‌داد
🇪🇸
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/89875" target="_blank">📅 09:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89874">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7Z3chBVCvN8vGLDowl9KYMUfokSMs9h1q1dPOEZG7_y16kgP4eCdNXQccr_-gb3i8LsCfK-ny4zjQ_tZJti3iIVX71kDD4A2f0uerujF3i_thzijB9HjZpz3Aw8-3lIDdvpWL-Ew2rKWxCFpwj0_v43DTqeTY6H4zFZHsjIKGjjF4UQ4gzSoh63mDPJB_wFv5UTUAY5vmmVNJ2M2nUB5Y1xxJFfejkkJj3GgT8DX-GaJX0suLGN1LKq8GOy0_HTsKgFXw3H2TP5gS6F-dQefLs1tpPFKR6BadhZnSiREyLYTjdxga6xfPSfMN_0myr3V6JCSZnUP9F9lMYIvJWAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمار در ۱۷ بازی اخیر سانتوس: ۱۱ گل و ۴ پاس‌گل‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/89874" target="_blank">📅 09:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89872">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=aBJxjZCO5zlelG606uf5a0YXzlqBHITu83tgJ1ruvZu5mmg9kcAjGhK-k3ofbpbAglEDFbIJwYCFqHv4Hsobsf4CA2zU--_gTCmOof-31VyYYEiFp0q6HZX4knJOMXQlGjiMrlwoUW8AV1liasrHbr54skfFCD0cWBueCoFtaLRB3JPIdggZE7_gTb5rVj230EqbrkA0JDKsayQXqM7BBQ2gPr_AW53lrhcooSVtLgbh0EbdeLH8iQCAv3cpl4U04BKuAYIwdnDMneHxx66emoM-yjWJcljBjFwbvZtB5M78kXK6-CwyokZgsgT7-4luasaBDd-Ahzhs7Nc4s3L2jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=aBJxjZCO5zlelG606uf5a0YXzlqBHITu83tgJ1ruvZu5mmg9kcAjGhK-k3ofbpbAglEDFbIJwYCFqHv4Hsobsf4CA2zU--_gTCmOof-31VyYYEiFp0q6HZX4knJOMXQlGjiMrlwoUW8AV1liasrHbr54skfFCD0cWBueCoFtaLRB3JPIdggZE7_gTb5rVj230EqbrkA0JDKsayQXqM7BBQ2gPr_AW53lrhcooSVtLgbh0EbdeLH8iQCAv3cpl4U04BKuAYIwdnDMneHxx66emoM-yjWJcljBjFwbvZtB5M78kXK6-CwyokZgsgT7-4luasaBDd-Ahzhs7Nc4s3L2jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
جام‌قهرمانی لالیگا رسما و شرعا تقدیم بارسا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/89872" target="_blank">📅 00:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89871">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHI0SXig7iyf8RaI7pCwN2F-_CKkRNoH8tU4MEV5MZUlJ8ZErnAulNAMQAonnhX0i2wrLltJOX-RA84g96OfDhUjmiPc8rpdKMVtSEWHuA9xgh50ymhCNBWrV15zsZcXcJrbxuAmrgJeDijNP-vZ1hLPOPL17HpTNfIWRgay_v_vvRyK4BvN819jZ1rcwwLKb8wLXWllzBA5NmUCloLh4Sg3ESjQAVNxg2QKwtGYI0o1aq8CiV457bCSV2QYaWrCHRMMO6550rdSnwSFt8a3P-mb2K3PJCY925MxZdw0bRExp-hw807L9auhNIGnmY80Luf_8QW7sSgGgB98fngQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
لواندوفسکی برای سیزدهمین بار قهرمان لیگ داخلی از میان پنج‌لیگ معتبر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/89871" target="_blank">📅 00:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89870">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVv1sQ9Gb6Rof5YQHEtEawtefARD6CKIhImNHrs_074yIjeLCfnqQhEOypeX-DgOVWvPLMcdfJLXjkCRTLEzPlWmP7mgMup4KRtZ_bgy5n3JbvHG0M64M2nLeqsCvXnr9jwERyoETOc2dQgmwpWHm-sUKrsP66F-NGzdgqGxvr0pfssfQbSObz96wsWl61zn24rnAGyHdMTJ4m-gOk06MGq_M9x27SMwejYbAV33ecTQv5NhavmlcuOyq5cBhOW1sKPgLVjPJlQ0q-_dIEagxWVhyKIc5kxIlgT77IR6j31HCJe_aDt6uJPZO4B9FfXc0W46gMuiWZkPBd7twRb8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرافتخارترین باشگاه‌های اسپانیا در عناوین داخلی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/Futball180TV/89870" target="_blank">📅 00:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89869">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2Mkt_iAFKCZTodMJDQeCCl3B8qkuPrYdrltanEfZDi_7QxVi5ya5dvBTFXGMgiqY1lI5oAmWAShPrtH_Xr8B7y40MOwhnUXZH5P1V-vKJeG93Cimhg2OOofZkaJZBFI8sMWJV6a-HbKss4oGMdjIL4wXx7P4NYQVRhsHriz_nQrRfSrgGUqh5vvZgMS0maxVlkxT5UU8uAPl6i5jNNbPzmRi1ttiHvZRefmtLSdGl6Yk4lBC4yIRWBimMYPV-tW8ESotmboIX8UYOOR3QK61BxHA6Pwkg0b-xHOs1uUWR_O49IcT9ROABzvxlIxAMbtH40MtIuZx1L7XSXtG2Pz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️‍🩹
استوری لیونل‌مسی و تبریک‌قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/89869" target="_blank">📅 00:40 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89868">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
😂
آربلوا: پنالتی واضح ما گرفته نشددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/89868" target="_blank">📅 00:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89867">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqGODy4dyOYCreT0xdWgePLfWKzSzrl0lS4DImVDB47YODgH-ssy2kmX-AhjTrRDgoKu-xpE5Lz7ZoJFXWzBZ0EjemSAVqwC1Y0KqrKcQpQwKPTEFQU_cINiuyOrTpcfWe6beUnE0qRNYpCDYsutKU_5KFO1ThynkRA2mAgTOmBikyBdU1fAzndEYrXOkVjNWaiRC6SzBF-3GuJMlGXi2FLlbf4mQOJaxZ4QSTccosUjfHQp55kRsxQCd_h-WglsMVDzbFGJax-P1z0jTVk7Ap-DJVwpOSJqdMo_VxTBJNaP5TLeLsCqMnivkPu0TII9GWXmSchJqPrj1XirOB0_OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
باشگاه بارسلونا با قهرمانی امشب، به رکورد ۹۹ قهرمانی در تاریخ خود رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/89867" target="_blank">📅 00:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89866">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmvVUo9ty7otYRfu9fymA6SUiigm-tLLxLllKPSkVz0dYe9GZXwkNKVbBwpl9YBKprwuWlV0MarrGL0bWS5UCnxadsf6ScontgWB-OJzxkD_6ciHyKQntxqVOwesO2DQ9Ay_HQvlpImHPf2E8nMkxneW28YdFCoFdLNcFqAO0go_T4mx512bGLkpvv-Jcn3hdRfFRz7h6lmhYW1AHYhMLR24Z4Ew3YN-yC3mB84ie1CQaIW7ktH3OTxBADy3DyMcUa_X5c7PgJUTwMQ91lKdgAokW_nRvrmAj8weARsKt2WiJUBNCW0wY-uHXTpYN-eBqPw791R5KcNjjbXKsMpTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک رئال‌مادرید به بارسلونا
🇪🇸
🇪🇸
🤝
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/Futball180TV/89866" target="_blank">📅 00:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89865">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sur7KzAFD-JetDdrwDHp_ti1T9ZjPiNyLV0RpWQf9ZF7A8MutyTo0SRPvByUHFb1c9eijjJU5xHRT5zFi0kbla31Yqc9wm2FqifOkP1_VCig2gVbSopHjnz5iuA9qh7UkkR4c1aEZlUGgZUhOS6Dl7qo20qaWKL21TOdkOoy5CwAp0drBkyWGzKmzcYi2kmaXY0Y9QecichyoIMypqrrXQ8pEA_WVMDqQ0Rkjr_sD8Qsldd1vadt1DjbwfnwEs-qg-MS6o1ER_mkXWBjKBZhUEUJGwZ_tctKJ9gQuhxoYQfZuW2EwIebeZtVXoleRP97TBva6HbL5-PW41VSY0Cc-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
یه آمار جالب و بی‌اهمیت
📊
لامین‌یامال ۳ قهرمانی لالیگا
⚠️
کریس‌رونالدو ۲ قهرمانی لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/89865" target="_blank">📅 00:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89864">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDj8TvQ0uH8_VdGZe2gOIXX-UgcLUAtZyxpmPusac0mLl9rhj4gQvGvxYRv8nNoJ1tQiOMPMPS5nalqTTo-D1d91sg4gmmXhkPSgLaBqa1_HlpcFz0r_6xJ5tvSDFcykAabsbIjBUEs3z3d48iUYvD7hDvEhNY9YU2mW355Wl4tcJdN0o9bhOG-zhbUKZPSO07WpieAIyO_3vNUzpr0Zqan-cRSgNWGgMeUNKBtRllFFDrrEQAgpnVso_1Hf2M7Qc8GyPHO4IMuWw3mIR9mJ5cjkCOI3RY8vL1xkBt9W0LjQYxZDpdFFOmNDnn3bhJSyHaRVP5p2czCdzJtcNiW-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوان‌گارسیا بهترین دروازه‌بان فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/89864" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89863">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0DmGjM42iTtApqD6SD2CjFlr3hJOlZwSC_-6KJ8-14Dqy7zjMVglFNtgKXnykGt67o38Ot5EKU8uOL4QmLj73s5m8OEJ6Hm-oh4QzVNjblgA6Gn4iTm_tghYiTmJCTa03hItsrJdZZ_pFFEU4XMI6lZR39ghFRaQxSAStnXzGhFTi6_0tf45LgGpUYoRHWR395MtQqYb91s40z-TTdz2vTJ3BRgHri4Rw_Z9BfGBN4p2C0uCaKYBR_ioHSlBXJrncn02U4M5pmEdOUSJLN_5gVaylqk8luoFKP-bUF8WX7auUZ1my5oSS5HG0Pt4H6k2nNqxij5JSLlJKn5VS0SQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
دومین‌فصل و کسب‌پنجمین جام فلیک در بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/Futball180TV/89863" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89862">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtgFJBD5viLQzVAICILmTH8caqHGJjoMCuNZUy1FnP2QKWmTDesOr1POs0xs9FvMzhV0TGZGD-TSSboPle9YjVhbseYUyJ0_GhUDUyo3w2AwZDouWVX5pCFPJh1LxgocHif8wpxklhxtghU6EmItCMx6IpUgbTD_TasSvECqjE6jvl3bBYDtoS4qf1QQl3C2AyyyPPrtxMEHR8MtS_BcPfurAucxGE_YXUF3OlUaWkllUHPq7ltzGF9pm8B2HEEbOdma0JI3ZiCYnBJ5bTF47nFux3zHfDXZDh2R9GONhAmbGjEUA0eiaHDnOz4fo7uHbwWWrhSdTh_LHdIA4ntf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
بارسلونا قهرمان لالیگا شددددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/Futball180TV/89862" target="_blank">📅 00:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89861">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رئال یکی زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/Futball180TV/89861" target="_blank">📅 23:58 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
