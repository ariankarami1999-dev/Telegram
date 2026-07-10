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
<img src="https://cdn4.telesco.pe/file/hOTE7QUM6m_9PsZfirNGW4AHVt4kHsZ40Hu_7J9ERg3khoOu4G8cMub_OiuTMtgQoCcCJJ6hXhwuVm__dDRQz3smlnFMjOF9zXqDSdTvORhGXNdlZWKmRlqJEqY9TDLYP5peIhGkTCzqENcLGGJUxHLnTCe8j-GuzpiFxLlhX8pfdGh3F0CbfGjyEN6bC79Wo472GyW_BRY7-ktDrVt08X23S5nVI4l7QMNVLauFZZGgaZqqNyKQZPEd_u4QCpIwTTz9uHtCxta3t08jnibATlEYJkvCUymtV1t2lOHb0fVkILMNqPVkC09Et1oT-YL8dRr3xIo8AHQBBMesnSop6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 424K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 23:45:05</div>
<hr>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdkfdgH8VDVZKikJAGS-tHqza0NX_LbEIQr7ShnkVqf8Jc4i3W9aKpEFkDKUQ-Xzs4DIvcF5C4LGOiiH5NpyZxSDVeL5oKLbnZ1czBeQMrIUiz2j49YF8mgktRMslaCBS8psWqWkSnU-GIJhvYtxs6fZvWxrzcOZzoEsOGIamMIltM83aEhtF1mm5crlci68Okj8usmlHYpSsN1CrHSJyHV3zx706qfIgxxnBEd-BnrlmXqaQW95TosMiKv9sz7Jq_JBISCyx7G-GsXiol7waX1GSFJ8KaHnq_e-2xaXqLIb8h9ViCtimUVduuk4tzZzXEqXCY0FwPbsD3dKmIXQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKafCsAWx3Jk4qCe3vjb6UoCDXsNx_rGIaxBsYmwHFIG5N25a0FH-zmQ80GDgZ6qnq7Y_d7bIrvsXtkbOwNczPByhTm1ye0K01upuLDQOpznIE68SKMRWGbvkQLRdx28La9Vn54JtHGI6z-gwjJcMz2rzbxFkDsBvAK_fx1ynYCd_QwcA54cdKpK-vaW31XBbkKWraPBTiZjjSA_P3jIblM974NySBZ7e0s-P0i8KlJyfRhEsuljz6XD74SkXXNRcVgCeUUtzDSIMd05xnIX9GDCCuY6gXbrdkiVgzJlIzLHHb813i__ZUSYiVObLYsuBxA2HOxTs8wwDKvysPLL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bL4m_RTOwkpu_diztFnW9lf4yvcOIqSbcRzoH1qx4lur01djzBuD0TO2jJ6t0P9U7t7UNjR0pHpZrFP1wsOBxh8yAsHZxjq4si7A9XWQ3MHy9IO-viM_aDsFuAAAcXN0YKIPAnTrbQRG4py0L6btaP3q4c7songFaq0n_9u-GnR-d_7poI6oivQ6tLE5GfzO-3rGEf8h_JnyU5Elplfhi6GEor-hezxpcGo_15oTzz5BRexm_znCX2QwfTmGXjBLeVziuIkw6qc_9WJaQISzxG55prRc8CigvsSvTj6iCgPNwKas0Bec-Oqt0j1Pbecc5_8IuWsnwcKLpxGyXtm3fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLWXykUQGfzj9sACsoCI0DIjk7Ayu9RB4M83ktoAWZ_wkU9H-DCOVGLSX0_PNaJXDfvfDKav3fSV6fPbS3efBnM_uKY088JHvojlA0YfNzXlQkTnyS7VcJJoPVh__PW-sqA6ss63z-XSXjMU3O8yyx_DKxiUAiKG2kkOq-dViRUeLjhuN-JqgIbhc_1nlQM9XqQk60mKFg_W-K4Mat0zzGPYxeYU-AuK3hVAu1to43H-IH9x0M8w1Ix1ylI7igvWiZ4cAqlo1awZXASdyIRC6EVOjGnbJmVCvP-6v5akr465L09MoKoB_cc7a4flIcSfHAEuWvipNxtU8qLRDjkHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTemXLV_bWU54sQCvmTXJk9ozAiBjZ9mkbeeolUfzsMLjklG3lYNWVUF0-PPDS_bLZ_P7MwRYyD8LbRfiGUalxiLQBuocWkWSjW8aZiruGT1GJXwT7-liHpJwYixy3ZuWQOENFpEcP3_UjDtO7X6HjKQA7KfQNLjNp1IkT2U2htIXnOvow8XL_6BnOYM4WDBnhh_cUYiQVMhuC1cKP7ElNCsXgtj498dJENqsDIwMncjQ-FZy-xdTssqkrDNDjnkWWJ1l3tPXY-jkyfglo0f8bUuoJu2XNTXEUh84LQ9KWgvPvk0EzTDbo19em1r2hRUyE7TdEJi95QHhSVCtGiYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzTfmTIhSPNQ0sAQ9yGrDQeuGWTsd_6X1AjF-2xNLYr2MZvTviMUmsvL9CwQfWHj4_0Y-7YLHz6kNvy4PXM6ovQPIUpM5YkF0Ck5LX0bCXFKxj9bMT-smEgIxo-eX3MIqvI-ubg-LIAqbgj2jU3fTQU3kdzXQErQQRzg8_RFBoFffn-oaAXaBBFh_OczACg5hjwnZqqOLk51nbXKb-_z5pW6jGff96szsEI8-4jAkJ0FDBIIatWdoCmTlFOV0ZZYaHhp1LOZpuybs6PvZPNQQYJTjeHrkpXrQQtx1X2yXu19OJZeEY3uLAneR-HMqh3owNx4Nhr3nBg4SXRecEm8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSBuxVQfUESnZCcy-WgBVwSbtrhUAJtL8vjwWkGV5KGKCGNdgvlgYJ-YZMcl3f8yVoGZklPXpG_ATQzKXFTlLfwmqLoMKb7qsZANOh11KTXhVz969B0ZzdbEkirb7Ia0zJRK7z0UVf5Qfk_jJGH9k8oZ9bxjZjRTtfhaWI1b3U5n3lkvVJbICv_FbW3yy2JkRiHVQDf3YORUFzVMz8w7zUKMc58JcxbVXBoh2iBeF6xijCuqPQ3WJ2CxzeYQWXDv-BekEs_Da6sDbTorSDsiJaMGI9p5vkINoFW-eV1GMbz4MT2FxMiDPei3Nq4i5vpR5PLxAFH4gGShlJN-O3PSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufft5Q8ZM8-GqqCcqtsclwukPbgzEesMhMAwD0YXLgsomgHN2qVtr5W_5L_EHsYQtGKKw-kTi8dHS-ofY5aPerbI0QAKh6g7FIRGAk_gGEtfjiy28Je40OtE9tedx7zT69mOPfsJWpYcdqqeJNFPOPrvSksv9jydNxrhk9Y54ybFjbhMZp3FsbCRStEm8Ln9tudwzUpYFe6ytRIMlu1DllperYuv9nB25ozf6HkR4Yqu9t8h8zRlSCPzEMIzAtt0Ewe8EQJzZ8UgHWLgjeUtQMweNO848NpXl0EX2E-1ZTIz3JBgzSoAPPN-lir88mTdDGc8ReyqeJrlMOqvGFxXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wdc2ezdGqWi7n7oEkAEdSAZBV6AQTDA9TgedvmSm15HEfNcsn3gI1GGLQSegBxaQJDzrhgLj-hr9Hlz3heEPfSevQx6A5fF-6Sh1PKc04TyiCIA48d5aoDsgHKmRK-FpzGg_eveHk1zEfr9Ii6mmirQfXUNLkdP-yX1vdZ87RJ3rL1RZD5wOP_YPFxsMf7qbu0OkRqVnw7KikG92WTlsNAzcSvLzl5PWRLXfIi7tmtjlV15lZz9YCHBN66d6smuverSgd5BXp0HjLfCJGB92DarY3fiHv3oJwdn0eGNv-NRa0v13jCKUcKTJ0ItaIR_mg8Siql8D8FTLTLAhtUhJHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXs5wpbelqvY1XLYbT9s4qv2eXF5GLrcAKx7ez4mco9qSKApLX8WwG3oaXLE7xYOfE7E_ABin-O62wYgb1setgDXsS5oUGT2_Zg2LpcgqAiOQGzw3VBM_jug_JI0dzaT9JEuUBi9iOD6BC9zplr2ZGfd8VuuokA1ndwW5kNiXZXAXKPNlH_W3M72Rng-Vdc6NIMS_3xd_m5dDBdCYE0yJPmPp7qwqAIdj83BEKTNVwVvFzyLaoWwN2bPKOoUjB5dwq7w1MAuxcE-4SdTMLetg30GVm2dGOo_OrzNT2tRvIDVRhy_xX7hnnh_SbPEFR-y2GSOdsQOqmRNP2X9GlPvnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSwMMCIuimTg1ol21sHNlt3A0QyHDj7Fg1gbhNbLg1SWWMsZXu8OnZ7KF_Cy7PZUW_uvAo6CyDjpQRO_KKq1NgW1wGJE90KoIOzDDbA_TUCXTp_IzG6FUkzXnxQBix9Fl7q_Cs1aKRRfAWhFYgW-uEkow6ikX-G6TZYwwR6GhM29yg5KWkNIyMkwtBtHKG5ilM_Ivp9eUnpLK9o0JrwJU7AbFjK3rQ6gtvpOxM6Xj0K3iEJWu2QjbDR1cL9NgdC29pkgceCmwJbF5hynEmXU0vfgZwEmzUMYV0l-1xRSCEFljkJvFGMOEGiP3O_mR4wpOLKS8q7j5cyNvRZN5hOZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq87cDYCKd9X6GuLMOj8RjKRTeQsnkJOq65mGFmE0cQZVl81OvXbNLHgaJGTycQFglDhYr09nS-rfGgK-k_2w-zxk9XP0Df-ndnSAErjoANCevc5jz8pilZWaBCx9BYx62M2esz1KKeNixVdYS75F7sS9r_pUWrj7ldC4ERhcoUgfiN0WmiC4Qbbe3uf9l2f3GYMX3UJyeKTzKhm87WurSqKdPFQsGKGogibFUSE1AKFPu5Wj08fh7g20KMi-_kFK2v6fNtglZGiyy31qFqT2nuh6fsdWbokIAC50Hd6ptdsXYBByLj5e2R1zzkfryZNjAt3YOyTWryV3XfP8V5LmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4JzR3x1OuS2UNjxfLJ9q_yerNAyK3BwaH7fzUbNf_lM2XUPcRVjJdH_kiLqfAG_hC0G9IBQPadiUDmt_MRWtSoR_Vkc82VJgD_penHThRJTGiCPLnhdZFcxqXmUjcaspn6yappATPzLqH70xNEOPgWXpQbdgcqYW2MnZGIvRs_ORaU5qOrEKPgdHvcWIV3wrGHeN5dT_c-G6CdWtNcxpsBxycnJtvvPLl8lnHxo0mm0vun0ohavmZa2vxUxkYahwRpPR6-RIu7J2JlqFarPBWjiNSxxAdF_h84rVco_5h_p7dbsjO7TMaCqXfn59zh6liqKKRj7BS6EL7yRhpxFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU54DQz_niEeBTbRcC7ww-ZijsTQWysx4bIc4vg6wNnCHp595xJvFuvqm_jfbvUI8kvZCoALt9gfEiAysJ87vSgU7q0Yc_fx2WFErPKDEmIbWBwXOFD3FKjKgT1xOGRVFrkRFuGuIuFgZF27pz9zs2tu7KSFHVOCT0Vnq4Ir9Ffcw9i4QI5rXj3_6MOW9ndTwEvfbK-nJcB8Jcu52Yo1FXYdVf6ATWAQX2gQhvTBZS5l0ERpm75g_NIerrnj-wSjLpXPeXPijKfkrqP30Aik3YThUvDhi7qFyyPOEDXyxZO2c31V9XjKGOAC4f8XN7uDU4Zrfop6eZKwXSFiTyE4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری
#اختصاصی_پرشیانا
؛
انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت کنه و درصورت صلاح دید کادرفنی با او قراردادی دو ساله امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYVXS4fMFz1AFX5QM1qn7LNjVoZDQdqj_kiatFo-fGQWM285A4oCUJNdI2xBurXQ5QmA8nNxb86CQp6ljWJdy-BTPvrT7pVgLFAipfmKoIUs9-6dYJsNBzYxIlLcZJNyxF09N6ZYjLLeHCrK4T58wAy2NzDeEsOpMs2kX7PqvxiiPxMJUcJS_Apa3ZNSUcRnHHldR8kKtiLiCNYn8pGK1AKj2CT9jWxWIfpFphIGeNZUDy3fMnWcdK5H6zBKRIJq2BzlRHok9r9ageGaQnrn0beV2djEaSdcdxPj4P8dgKr1iLYsejzA2jDVqGxp6M7o-8cj9O75pV3Jpyd7ggQYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tU7USQhs9DgwAR1gvU5AmJovxxNaXORFlP-mLPs9xRkqz1gY8OycTTcwMC2ZdBOFgbTMlWxEsBt_-Oexp9FQChndH7syRrKEJGQ9YAS5jv2Oupg-_sy3DlRg51OovME2G0rPsbgYYYwTA2wCJX9Yp97rqEM68L4k1DSQ5KAaVWw3NFEE7T3Pmw_PQXXlIrCQNloH3DHkFt_hgKlb2nnFrKMPy-uA56wH_Ahz3bNSCpsKiF461zCnwEIeETXRZz9_nWzRIaM8RA5qbAtz5MQ1IZdy9u2nqLjSqXtkKpxR-ZrL4qcRzSNTyLXgWT1t5z3hOP2lyl95A-fifRCIdRWMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYMA4ds9Q7SjJTuO7IgiF5b1gJwNG-OpM995NZ3BHIYY4RatspaayET2BJ-b65QsYuw_Fga7ATNuJG0iGKpp95rWwwtVP2b_68enurr_Llwyg3SeAygn_y_KVAfuy8xkgEdWM6dxE6E3zxJ7Ozqop4Qs5ugnXU-tVPNnXdThwYgoio9yzErdtGXlvnLg5jK0BNQqTjS-2BzHfVMa5UMHbagpubTCSfAk4VG6Rf2p4cwZNlHMSH0xSEwIWYBboqv9K5x5J4MHOX5symyi3ng5nkLPpZ83NzRz9A9fPkRIWPK4u7jZtSDSO0DxDBauxNKT_u0gVZ74YxBI6S480U1vFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت را ثبت کن!
🇧🇪
بلژیک
🆚
🇪🇸
اسپانیا
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇧🇪
بلژیک یا
🇪🇸
اسپانیا؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p5_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/25377" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5bqdA_Js9YTEeCN38IaVkLLh0ajfhD6dCgdtTbEazchLckXfnkFxgiiO7eKbJxA6zUuJju8HQ3vSBImjZrAtXjW1Gp1bih2-nYKGz8j3dmPprfxHg6_YlbH_weZqnpW2PnPxM-gJwgjKYEo_Trr5vcaBDODgJiTGFdTYLI2a0R5kMETmPW_ET7I4iaHvSyjZNT8VD50hFP1203FgqoCnFgbL-5Cj59XzVqzmqLSRlavu11vVcYIyM9-lQQly3SFH-KrrUvakpfXqG2p4wMidp0xVp-j142Oi2Ua9_P1lpeWibkCMfSPLq--v__8iJdQ_BVZnfWJqf82phhNQ5Xa5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnfxXkoLGZ_1viGHlgDt7hrRPqm6a_o2lwWWMxw8b_WiwTMWWMNdfxifM_jWF2MJs5DnCFLZUyZt7br4_0aJ8zBaDK6jFI4dzicI0M__yctoisb8uW5MqCL32Uec9oE0JGUDJMs4ltjzvFcWADo45AhmZCwVRlwnyGjUmpVCDXIOvUbSatojkdZzeo-tzQhTbqAYkwKqq64J6DF7wqVWcYd7esrY-hEkfcsVXtwIXn-FkDpxHO2eXH_B4Z4b7oqyIKrguXGjy8vPGk-hxZm2p2BVpSMjV3YDCPZDDD60IYha2eb_s0udIzyW3FWNBe3juoNMSBlY0I50xu48fp_mQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5DXgNDqSkA_utCkV2wHaeg4GTzYlnyynSAmYh2gevMQhxgHwXPHIOv0R-IArE1Yl9MMiMehM_6An95jE2OYvySpx3478HyEZqDHrDAoNwQFRIJOfADC9F_XjJR6XXNTcBs2EiR2P0c2jkPuFXT7gRZF1JIYECdwQ3ruHyoBrjNxmL5Zs2EP3ff-g-V_DPvPg3Ec5My2FrOCbrraLsE3ZAyvDp3By2BYzEMq9zLaCFL4qxfvfiXAmM6ePcgd42XzqtwsNQERu4tdcPZOXr_-3pCljKtg4maCv_dI2Qgz-kK_c8Sq3SuDAORXjdT5AnRNQUohJevLvP3pTt28aEvAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=YlU0xiQj8_TlpjTK7QZ3mcJNgIgkWPXspQ0UiSljj15NiP5aP8SSjJU7L9Gm4_5Lr_slGPfEKRtOTbPmYc9gPxKz430M0COE3FkUL0SxyNLQkb-qOCzYoSCIPN4C5xX3w22cCMj0DADxp68y9wGN1gDz_h5It90GG1GPdKNrJNR15poGpLUjGsg7H62jd0C0w4hBm4QIGB1oeuYPckl6VAVRwRKlVJRKHUqEOxS82QIOcckBz1oMOUkG_TV3Ckou_s_wQhfpsNjQGEnR3QH__QQzNC4Pxe3g98jQnE7cSXhyGqk7gO1eZz2icfu0A--9jA1qqvpiBJ0zhR1q7JZ65Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=YlU0xiQj8_TlpjTK7QZ3mcJNgIgkWPXspQ0UiSljj15NiP5aP8SSjJU7L9Gm4_5Lr_slGPfEKRtOTbPmYc9gPxKz430M0COE3FkUL0SxyNLQkb-qOCzYoSCIPN4C5xX3w22cCMj0DADxp68y9wGN1gDz_h5It90GG1GPdKNrJNR15poGpLUjGsg7H62jd0C0w4hBm4QIGB1oeuYPckl6VAVRwRKlVJRKHUqEOxS82QIOcckBz1oMOUkG_TV3Ckou_s_wQhfpsNjQGEnR3QH__QQzNC4Pxe3g98jQnE7cSXhyGqk7gO1eZz2icfu0A--9jA1qqvpiBJ0zhR1q7JZ65Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI6CI1n5HzvC6VMzUvkWoK7v9GtM3m9XZ1oZNlYu39v387CMOYYGJsIUjWz69T3E3b7ErlyLhrBveqHimYmV6qEQ0mosBRkF3-tnxo6WY61nBU1vWswRdACKAIzcI9RUz3v18o73R-Oi3xq-da3D-5QPmcfYzHJwpu4et8RDysrjDvXWmqVRH3eC833MMjQTh2ZND7jamAReu10bCdGbnoZSSLRMsTq2OX1yL704EaOpkVV1XndYAcJMHC0VpQ7otu4MFyowA7zK-1DbdizzS-sXyRSNpsYmQUElBhtyi_ZBPMtCpOf905PeMbPF7jsF29VKw4mJqYzZ64POMf97qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXwN6hgWZFhSTWPN20AzxPkvNGG3kzxZRyQQIdbnz8Dd2RtkRTstFw4gKFAOuWOwQf3JGCERoV02wvCx7ImH6nCL-rB9b6CfyhHAPqT4NNMOkWWOHGX3t1dYRqaoQ2MLzBEUqdBBwwocY4M_sxUk3BufZ-f0QV-Y9VXQT-pgqJgfs2EEIk5yk0YEZlP2cehapjEVM7iToYr1o2V_dG-vhHPT5_R01BX4h0ssT7oFO9x3IoctzUPc2PD5vF4y9PN8GKm8KBgdg4AGx6t4ghShA4FPAMo0fPIibwwxkpk9t5Up5xZ4au6XEQBHblJYsV0EJx1whnCz1tz1enP9e_GiRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9gj53_q5yyry9-fN3nN0ico5zvDajE4eIKxfAMX9l-B02YZm1-2Lzz_d-fbysdAEAtT1ZoKWidqCAR71t-wVtcYXeXtQfbdqIg-UY5aAi0eiud8TfWZ738v3-rbNmup95J-1Fe6JgPA8l9CrKBtG1RGlVk2Lx-yUf9cZRMjzIyDX4iAOmW84CHx8ZIXSH_7BDj6PWGAUa7X_WcStPLOG92QZRGh1qri_Z1hAmDFYRVWi8t4FgXBKsxv2FgOlf6VWG2MFXUm0C6C_qJMCczbbZZdwZX0lsLs4x6xuiUZRsx31AEw1Kv6ZONmHpLx7F_U7LNiW19UM6mPULFVePbluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHHRdTIFgR71E9FumqwYrqK55ctAUq3QZxqYYKB_0AX7hwL6BaPY_dNiLigMaTx9SmTngIC_-rpEO1GY9as9KbU2HGKna93vSRiyq70TrXN1vYmQ0kjgrXeJc3qnH-i8P2pgJ8I4btnDmwD5Ta3xkyuk7ItzxT08XrSaABaMEGIQv9cvqQHrS9LL5kibMHg83A8GEZg7vgcgVcKvAkLywH__4OuJonqZqTGdDZiHEcdKbh15u6Y3euC0X_BGFIeYG-VU7DlwFAOIanaHMH3PyDb_5xEI4x8nBMrVr3QnYHhpI_xVrlX8BxnWBK9n_y1FUhr4ktzbaAhsUp7TsPBJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqpBT0rwS8c8zYrJfRD0RetmB1LQBjIA3_7ZosRw5ZB-kHqoWFnbVhp2FMo7VYWC9gQIWb1xWXeIl46a1Kc-5NbD9_ne_RGVso2y6ImLNXxNLpirP0QPjrm12LC9gbv97Pwik66GMpUnNaHMPvmB_TV0bJ_jQO2O_gl2MmDibpieoq_0opyBW4-MFCCqF4HoFpfXD9S2TL3Bz5jt2Ih_iVaZyA_4Xw1Vu8GfQxJ7g1momgK4oti4563ElAl-bwQ4VqWHl8cxzXbK_CBb0cgQvnussE6einqkQj0ewr6dkRpvbfXUWqML-eHlwa7aw0oDX2hX_xcFYe5W3FdDnF-yVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVYl2LQl9KmD63vP5ikxA2_cauwvK-o-L1zyUBJ4409QJ9E32_2LexFOdjsY6SnTGXo24Ssm6mUdRF9oQ56ikePyVFIRziY0HpPb5DJvGY10bEXCFTC0E9udRzG6-dr_zntyy9RQGtzRgmtOklY3h3CWdkltpXj1iYe02Re8_Cj_H7A_EYBY7eqgDxkYyFh3j-Pb39vcrFLvMnwm7RxnliF7nfRGvKGhYTFTU56X_WCzhvIHjz2LBlJCBv0AzNVz64zBVoIn2indbqrXhpNJu_1-A1lpYXJSE61RfFgNWxmuoYHdBW9cBoOVqow7jPhQ6eayeWnIQH5LFPlk8b4qXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdCvWLbE1sf7jeIynz_YbPUCd7dj0UwAlCk09pHPw1KlzApYWsQRPuHHwVUEuBuIVg0BVByKwVIezhXPMYpA7vOVRmq00MDST-1FO7dUp9nqKkJwzFV_ctLUnVVugBk5GFJGWh1oX85dboZplUZt90TCCWMeeGQ9StgBl8TAGr2j9kMnv2rf8tsiTJsUAxUMUkEGF73tvplia3CwKDkEQFaEkaQfy1v9ZyV3AU6zFBf0FIEbvYc0IIXe5ATrxTq_r3DmV7kgiLXLTHwC5UnVKvZYwX2W4-RTJ6ixwHPc3XsrVX_3WYvASuZxbjUiuLtls-EqYXL7iZ-S0RS9MaS4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnRXMh42vrZyUHVzHslSQvW-gTrbf6eg41Sq1CHUVa-ydnSSwnvlDU2qxkkroNLI5NUE2nWnDMrLoq6G9Ar4YlHLZBbkFAOtWP27Fv09_RdzNOPgoTG2LsC-mg2QAhb53SIPqyaFv2zklxr4-hgZvAX_ku-75KULH8fietMDur9F26lM9DB9HyFHQXNckqnfYeCmKwA8YrqdOt9HWdhwreNckwOr_LkKfMTypAL_RBLmYVwooRh4zR9-OA3Z-vKNSUXWUnk4BJmXha1i7kE-4cHKM_rPWFK75uC99SsEZcaV5zfeTfBETagMzMAwpABiXJb9qWHB9-9KTk3LX3TPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25364">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ohnPCYgumw_Euy8KoA8Yj0tsfmD0vbhQEB-PClghLSg4lqPCyDsjGeDcOTARTs7G-d-Hq-5lek9ZScM274aeHCX2LAGeuqR5BMVyARCvqZjITVI0WYpWlNBQ4sy3jNOI8ShRzlDW7PpqxvRs24T-tXtwxmsJwPpm78t6qGEgPFlRJnExICddY9LN0R_h0exSVZhS7dHfWuycxFa8HM27s3N-hwF2VYszMy4twr-RHWMqu58i7MiFoE70sdcdLLzAHHLRh18CWot3FGwnD7qnqAG_xvRZp1t4-3q3DeeIlqqP2aMMu7knIx1QrZBAuxwLnUxLkq2D1Egg7KTOdglDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
دیدار فوق‌حساااس
اسپانیا
و
بلژیک
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
▶️
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود به‌سایت‌فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25364" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyac7wdtxgSqdIJfKg-LKNc7ujL18hyotwA09FsXxSpPOBZgHBMubF2zfyXtujlQqY8VnEhrSPDXZqIkQJ9LODf4qLdqERGUszSqgEXoLCREkBs9oOE_gG5thbEEabxPlSoOhxEklwlfJnJX0IDVPNuKwGYyIuHrtcBcWvKJBL0rJbsgv-bYLW0am8MtoNwIoWioeKgFcy7soaNZZXectdO2XDm5keglenJ9J12-88KNpItrcuFjE4tDHUyhFlYTTZJgfCqOvnW-Nug2nIGOrl_RLYSYxEN5ZBTwpwuO_xDaCKi_xgjFwxlt8QELx6SiMml6BKK78FFZOc6dwq-zcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOYlYQe3Fi-nnanAJ_ILW1Ppzuck6EsSijKiWdtrihWtD-cLMZhw3CTomn1UHQQdrXruDYLM3-qI8MEq61rDhQu4pXvtOyu6Ohf-YyEukamvEEzjKybQsTu18KJ3DZVUz5dTyZEx5l657OZRYMYStesCsqIER0jzjkxZwACAk80HyNWt_ikRD-6GY9hx3IWtCggiUkTG9n7Tq3A04d4gNnuNPOQmcpZITc3VW2ci9qL1RbW4gpsaELnsvxoY0oCE9xMzMyNZ0HK73nzooDLVZyy_qw1-PlqTx-7RwMuhL3z4nJQTOKsNgwdEPY_KUbP6IoNbYZTyVVqBzigy69U2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoJdVkL4N_pQZiD5-0iEzfN5PbXcPgpHwL9heEZ1jTWKZSzbwcpek2iJaxikk9PMvY8GLvo9Z47jufuzajo6YgRxMv2aFRMZM9VDz1Vny-l-6bUPWPzIwolPihvogggGDirwK54X8XLi3tJbV009AIbHMjABBPcw9Xq80f3OmMtn56JyMC0pe1bNT8zn1r0rHNcw-okl8ASkDu0YiRl4lJyelcF9jLl9fteojx_O7VY6CFSOR11j6jgUi80KoPjsAyjVpYlTYop5M7jt4ZnVzfHoMNicCVFz6iq_k-cVj4FuOeZXC7thunNEX4wp5jFToIonF4N7L8uH-UK1xZnAUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvHZMwfch__FsbEgWkwyBp6qQhjrTfM19qXjyi7WP5vWSRNGIwg8CzzAKnAD21uXvYWNZ7bxM4MgsGk5korERWLra_y4fq27wZ-rXWJ3T628igTTiYa0Nwj0qrHjPmdsEGGC704olNgKhTi0lZmKtpv_y0KwdsJW217TP8u1RtdVr6P3R8EFcv_HVyRGzCD4j27PET3ecuat9t8EsD1B7AJFMbyoFSlWVIXCgwarmK7ptOpy7c6tGgeRQekBAbj7m4BycctAuAD64YDhRReKwqnzVHi1iXXrIp_zrp86kzpb3uXVy8ehLtEzGkxv9iOWNiKcD6yJ8mExOz0QNj2UIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmXc3fSJ5HzibhyMdfO8AcExRHhTcCnaT4xcpCX8r87jKyKEjvHouYfpM-ZHtFX3ZRb8vmI42LapsmxdvTmVDBjBl0_VnmW_xoSja9zVSH4sm62PP8vNisXEqCcUVmWuymTt9lLkHc0yj5O2oKJnj3ghwolBPmLOJtaU_WL8PN_t_XeqtLN8QhVTmtGGXIioaLZO4JC6YeC-X3Wi9fBebOEbttWnokYo0R00FbCRp1jySUl1H2x8LhKuGJbdXl71yrDQ9e1KUw29FCnzXrvVAd-QTwkIRc2MlhShRFUXNYnLdSGlZqmwO1xP3eNDw14bLjVOcucLVEOYhgO3U-nPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=gjnfd748NxHZ2HD5Q5SVRwv43emd6f7FX5YzQtXSO5rFDBfuhZW5fvEz978F5b8wsLZogdpU5PD5mC-BGN_8qIZBon3rWxeP6baKru5hX3YQj00qIHrvvqr3EDddgw-fvrbnK6VQ74un7JpMectvQoaR4TCCX0t7i_Y6QbBg4fQmNIgCfJwga7kF6_O7WxWLGvXMa6Jcv1D2Xdksuws92q0AlNSCcUOL7SG8s3gd7UNjCM9dIYOOPYQ3EqqNPEEjwaJ2FUqgOINaHYocDDUzXbgDHQmbiR6n9xwOw9e3yrUUiPJRZB5asKuaJSZMmcEwkfHtU_tXMEqblHWGqVQvBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=gjnfd748NxHZ2HD5Q5SVRwv43emd6f7FX5YzQtXSO5rFDBfuhZW5fvEz978F5b8wsLZogdpU5PD5mC-BGN_8qIZBon3rWxeP6baKru5hX3YQj00qIHrvvqr3EDddgw-fvrbnK6VQ74un7JpMectvQoaR4TCCX0t7i_Y6QbBg4fQmNIgCfJwga7kF6_O7WxWLGvXMa6Jcv1D2Xdksuws92q0AlNSCcUOL7SG8s3gd7UNjCM9dIYOOPYQ3EqqNPEEjwaJ2FUqgOINaHYocDDUzXbgDHQmbiR6n9xwOw9e3yrUUiPJRZB5asKuaJSZMmcEwkfHtU_tXMEqblHWGqVQvBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=tatWFKJA6K_frZu34L3iIZNRNI3Sg_0r1jH8vvqA5yIm4ZfepgIAu4VtgohdEG2gQyLQ8orlehWWx2BiEPMAYy3rAcm0Bw4RVRQOl2tAoC1Rp6foTE3K0p3WfP7mSMzdTbehWVQP9Mto-04idsg0jAJbivk__r9LdYyuQfHsyOVCv2o4ch71KFJer6wfn4MlM_PI0cDAM7_9NaKZpT_-8r7P4n0KSZpKwxrZhHi0yPwkV4JFMKMhVEbujch4cEVBttz4t3TmuqcKb6GMaPEnhwsmRxeiZ8tsBERaCljKgtvvqLbpnCan5cLw682a9SXhUTXL1z2Qav3EiFnpKTwy-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=tatWFKJA6K_frZu34L3iIZNRNI3Sg_0r1jH8vvqA5yIm4ZfepgIAu4VtgohdEG2gQyLQ8orlehWWx2BiEPMAYy3rAcm0Bw4RVRQOl2tAoC1Rp6foTE3K0p3WfP7mSMzdTbehWVQP9Mto-04idsg0jAJbivk__r9LdYyuQfHsyOVCv2o4ch71KFJer6wfn4MlM_PI0cDAM7_9NaKZpT_-8r7P4n0KSZpKwxrZhHi0yPwkV4JFMKMhVEbujch4cEVBttz4t3TmuqcKb6GMaPEnhwsmRxeiZ8tsBERaCljKgtvvqLbpnCan5cLw682a9SXhUTXL1z2Qav3EiFnpKTwy-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kytG5rts5hbg0b6v_4LBbdMNOSlQUfirVHHMFmV4nNZgbNXM4J5qEOqukEAdIwmr0LOTxOuNax5TfISdqg4VojSgQ7t3DB_d_1tfq9aHv1xImhAhXqeaGxz4XjwJW6O-oG2UkMCtSyFpJvkTRl7pxAKORYRWrb2ShRV_ixIu7K8PypXgoxoDdduqFzDjcXwOcKAmMcrdZc4cyHrvB8137c3aWT1XsroKSuAWvLZfbpjOfj6vMBZyXYnSYMM_CHyoIvSuDvg-sjKuXLJ2DAL9LAUe4uQTvtq1X7TiCYW1racXgbH20BIpIGM0eSA1PK_KsXGiB3zF82ou0NLSv44UvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_fx38XxveDImqpGJc6tm4BA-It9NTKGHmph5hobtztTMbvkLMpF9Vt5gVbHyvPoQDRseYC9seNb0khjB0nvZtv4ImYOFh1d0ZMbAGMP6tD5gBbrhw3R67jCsHHWKDTThAWzWzFrP8VDEAn3-w5VFpn8zCw26-fe8ld2x59DDvOAzE0M7juANU4rX3N-j-HcQjzrhPS9weu8f3MPhRT8iU0L9L1DDc2tggatfs-JclntKIwurWTnArvKpfWqIISeZlV5cCJp18LyKe2UkRQFOZ9_Fep9VpPnbl3eln2Sui8D0gXbbtAtdtAR1XSdVLXApL1E1SxpfedWtqTjkdwBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beQvD16DCERY19m7rVqIfaZKBD_LJEnhdMz6p_TP_5zoEOLtrE_EJ03hADWfZX-OHGSVsMyoyegjqoewb0tAPBLhJ2L812s8giMFSw9GhomZqd-b5tX1_gyob523Dl9JfEI5YW4knKF90ujHZ6AT7xeGHPmhp6JXjDEoaUS9Zcdq8E-g6q5GqsDBnHYz4pVOGQ-CYyqpM7YRmUMhOWw3hTKEOAzcL0PVQzyJOChXlzk4KaQIWhWFj6B1DNtey_lWX7o_AS9OwWMLtwkHKLK68KrmMmkoPoplYVONL00YLyGh-uIKuuyfk6nkpmadamg9KiYBdHU9JNifruTG8iKT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ft63EUDhuTFS4thGLK1-p3fuhU5KrTZWFymj6GhUeXRaSrj0xzwZvo8IbCxYcwV12dKhjIVBO8Ff4-_g4Ze1btXTb0edfNkX6dhqEbN8Va3E1hDjO5tmq_E3Wr51QQvt7aXkmV3BtmreOGB-Gk-TIr7OrIAIm8ahN6G8KKLp5BGEUSf2cFpClTwFj4QMzwGy08cEXr7tkL_Nwisl0We5raAMwZqMX8P-VNQcoI2Y6jMuA-BESpIS3pSs1NMAmIQ4ytA-w0Gc-AeXaTJGFp3o3JSNEqBtw1_gU9KvdYM54b_RrHx9DvrQBmbEaO82fCpwfnQ6FL4g2zK-pqU5gSivlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKFKpbsA_IN0LFjaaEVCPB7vQOSR9bUeGGWcGok6BD_u7ENKcCeSngB76VbkyumFOygG40Ej_jIzvh164JgKYU7GeBf-HJDHkfCxdNT0tQn0pmpq4e_WVMS8u59f0nTZ_eHX8YN8QoW7zOB3CddYk8iNrMWRe8eOSWzmP2wgRO2ADdiVospuh9C-Uh87eKCmvqeMxrINo8hFa6K7Ung8ypA_r0SBxr8rsoe841I69-epp0TrMdcj_jKMJqYoc5XimCr0uVVXlh9y-Kk2EzAzsVpTEU5nu-Z6o6Gcf6SSfFzDUjC7WtiStnORdqu3Asg_J4V1gE2MkKBuoE5lSJdkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn_M0e9tLzQL4uUjpJ73QuLQIfY0Lr6exZqUVSdZ5Sm5LJUT7kjHB8HQcTnW3BwJoTFyYGo9ZzspcBnsK4RtxZSQQJYXN_8sW1kVHSgp3QBsIqcq73H_ywQbT0knz0tUfZcMYu4vvzVZepaR1VgNlG9D3ynIgBl3S9Frhszsxlwmsh8aMuddi2ryI6trHRV-riW4oppvFmvKf-K1wK43eX4dPFD4ByaI1DcJruXGtYpvEW3CM1tV1lSxJyJYec3TpysBCcp5g2Gpch7OJDcmDEWRXTs5aswidFUwJrDmHZ5mJlu_vLcjTL4NeveDeszFWWtngcXZ8lmUlqCbMSYdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFgu5ySNrzV7xgbDw-5GU_WTdbcX9Kjkq_3z2lcXOsnuk7o1MqqiSc19Tf4P1uX1Xflu8IbGGTDBeXjY1-cOiyT8lyd9nHoNLN_exGBl9Hq8FwSMR1LjIRJz8d_sJNfbvW-llMPX61SDxkxdYKH7TobrqbdEwhLTIVEJjT9BaWIKU_pDdFu8U_nJG1nTyPvhWwa-BoTWljYzG-tQ_QhSHdor4-LJMepxfDcwZOfK7VYJUE6gyzvVS-BYH6dI2oU8xYClkzwDJ1TD46y1E1_5tOwuIVLoa4qurezMPR-bCdscF8En0VIiT5mW1XD2wyga5CQetDRRqmHoJqbUJI_9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfIgal7SZBRYhFVBMcZHijbVMgIVKmYCNn0a8OuLKR12uiQA7GeppEyTAbMYpVCnOa4WVOfUAMKnEqUrLLjt3TnKA23Kwspbl4OjNdIRVBvGnuzVnghKmIx6vhIUF8PC41e975BVe6o0NPRdaqeuBuTRllIOYKlS6Pwx-wENafJ3k9BuiX3-Buq0p6Mcc-FVihPAZJmlgOW06TvGmKD9mFMfS115h08dbDfq2wBFcLjR3yocAqnaithRHAZ2toP7-KfOOYkMS7QNPLiktXWo6BF12rZzsQXjFT3xoQm5GQ-9LE02KNHeCLTwNPmUj_qx_Drd7uz1W6kHMRBOVxH7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PytKNZa9oUQkq3Tl5tnCAVtFhstylql8LZbUgkG5vREaHK75kOCIMMmtVLJBEd5aT8ATFYPqeEQ0oGN0u_GStXeTHpi1izFmRrKwQS9UHV7q4yBfMrqqcVQyB6WKe-RnUCRXrhAyw865NfNl_xbmSlcHWgQUEKi2rptfCB01uXLosgwIwqgIdX4GuCWi_zuJxAi1WVEWoxVFuvSR7_cDbyMe6m6o6xuoTftVkbas--IH3-UJU8Q0phXTTotZ7apJlaDaCxYRkJP4qJUfOw4dKBPzKdoqezfIwAbPHoKW6g8ZfEsBwy_S6IxdRfAbh9CGyV_inVJa7Zgcmau03BzCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2z39nOqoMH6LXWjQejrpXqplNjVKyrMcPw771JepXS40CNwaUHVdrqpYRg8aIsumRdZ8zprhJXCkEl9pTVkJHuqyN5urVfufjULp2fB3VhIQuA18TMbgPc8erZ9Ew0G-MR-RVi9ANvHZoitnYzchhM-d7G6d7TXKBzaqhFZauIZInw01vGd6gcSBNYV08UKJqfjykk24f2B7B94CMTAsyWTsZG9lOF169Q5wimJzNul9s2avebBQC_joHNTYc694BWzv88RKWoD6lh_jqOvVo1Av8_3edLu0cHy7uh86qk3A_EixrO6BxCOEJ49nLFYzlWigwzr1wO-02tNozHR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=v2-oWVJTEXcNHzS4hlSC9qfLG5lS-fzUgADRgOfZ9_kPByD_hBCEpmNvgO-PRFVJPetLaTTp79G74bwbSI69cAmDDuARxfLsRUqmUoqhNff_4z9YGqqMOK1xAKSlFuJVIrerMnoxgJwP6Z5Ek_dtTRKmPVemXprvXYymq4dvAii9GBB9n1hzexiFzzZD7QfxgiqVntKclorXPlBeZCKpbxB00LdjdKoN30iyo54DJ4PvZtPBr-zEOteFx2sZuAD3_nXIOcIKzmBOvQ7adcp_DmgG_kNmjidE-Fu7wApA95FLQOUHtj9YJSfU0ev2WZrjtrIHcuioUdC0Zu2mUPYPBX-diny7ETJXJawz3oyE3HBZ_eG6CSnx9wJA9mUvXLZmpESBJf8JepK6r5RqqeyquqAi7o8dVBnYPsJcs-5-WGMkNSUrFq-gZqPPItnmOkgvvN2gd7cxv7NOYYKzcPhMyvaF_4vBVUe6aR6r19HDFOOsrL7AM4zEC-jd370CqG2GRXkCemK9jkWdUYPq-zzM2m-HUTJIR1sKeYn0uVzVI3o29tqyTOTmRaR3b_-kRsRoQrk3wY29hwq9qpT9Pno9PlV5pDjvFAZR1ILMEbaWgxVEuMd-PmBJMdEC9tNudQg-iFkaRcVFdHbDtBytzPFrhSFewP5kL1CLwmJ4-SUVvio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=v2-oWVJTEXcNHzS4hlSC9qfLG5lS-fzUgADRgOfZ9_kPByD_hBCEpmNvgO-PRFVJPetLaTTp79G74bwbSI69cAmDDuARxfLsRUqmUoqhNff_4z9YGqqMOK1xAKSlFuJVIrerMnoxgJwP6Z5Ek_dtTRKmPVemXprvXYymq4dvAii9GBB9n1hzexiFzzZD7QfxgiqVntKclorXPlBeZCKpbxB00LdjdKoN30iyo54DJ4PvZtPBr-zEOteFx2sZuAD3_nXIOcIKzmBOvQ7adcp_DmgG_kNmjidE-Fu7wApA95FLQOUHtj9YJSfU0ev2WZrjtrIHcuioUdC0Zu2mUPYPBX-diny7ETJXJawz3oyE3HBZ_eG6CSnx9wJA9mUvXLZmpESBJf8JepK6r5RqqeyquqAi7o8dVBnYPsJcs-5-WGMkNSUrFq-gZqPPItnmOkgvvN2gd7cxv7NOYYKzcPhMyvaF_4vBVUe6aR6r19HDFOOsrL7AM4zEC-jd370CqG2GRXkCemK9jkWdUYPq-zzM2m-HUTJIR1sKeYn0uVzVI3o29tqyTOTmRaR3b_-kRsRoQrk3wY29hwq9qpT9Pno9PlV5pDjvFAZR1ILMEbaWgxVEuMd-PmBJMdEC9tNudQg-iFkaRcVFdHbDtBytzPFrhSFewP5kL1CLwmJ4-SUVvio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvdz3yYdVJ5mtxw3K_ZLQYoHrl3JomvS8UN3_jJdSUVxeGtEmqAMatOlRSAqzlGvvSj2yl6lsIVgY7RbHktoEfeUab47zsXj_8NeBY_YNoDw_xqQKjoYFNSqadaMy2lANL_hbNg-6uZgdNdm9N3C2AWldCvKgEQlckieM79feEyBBiyqjfwvC4dLSyPGFTusLEN6RyNd52WvSDZ5pkHs_t2qfpBg9jvOBF8ATZWikjhJd6paftYHUE07aFeIJnO0AjdlLdd0D7wYp8HiRTR6TsOIy2X5BO-xAPZfX1FDJhvkhAcVar0RIuSEVTjP9Dt9MwNxMUFQSpngHGdrszU7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn7AyxTbQRKEAzPsRACuhGE1Xs_aAgRGWeaCMD_frJ0Fac6DcXCyLK9Qf_qrMm1q_mbtlByziF7Pwn6d8XFXpz9d1JCO8ayhUQSozdgXva_R1Qy7zrDuZku_xx9fUXKrDRa3XhfmOaF--J61aJU7e3JShPqrktrXWwK-M9f7V1lQu9dHDOoxHFWQ-xN5dq6Wtq7YccY-uEB93omb0BZz-y5xJxPePaUPPZ9wBOvBC1BOfaCf9qOHB_X6KYVzB-P87IyB0dgfSR9PO7pwBuLSeg9Kz-5sIKNdznGGyVSndJlpMtqJFTc-zJ2wBiFE64hq1L9WLrxrABx540Eonv6_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHvW0wIn1mNlQRYomf5IYUCc7vts-6Rzxlgf4DtfLFOl5G_Izmecm4FtppcwmLZqL2Y2rVQUD2SfqezSLpVu7Wvr8J1D2D5q75og45Wlpd2FCZjBOl35vd5sBeKZ97HE3Rs3O8He5BVZXQHxwfN78GK5Ipgk1sgngaqxvykK__RADfja390BF_PUBhO3yL9DG_UPL9Up6Gz9Dwj-oYnr8Yg8XSs_hvZ6cWGH3M1K3fV5kFdf25IKZed0dzdkzBykelfT3tYPHxax6rwse8OZWWukDh84QXuBgu6Q5GH0IxQLIikLUjMV6wN2_Tx4NJiBDcLODkxDZJHwI1d_euMwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45277758ee.mp4?token=jCotd2p7Y_FZqL3uooLMpNfJ3YUqN7AqXjrx3kYcl-D8868sgLfylzSqk0Ma_Lo9oqQEgygIskDLE1gO_VdcI-r7ghpZMIP01k_rIgn0SLljKGiDJDT8xRKitJkq4LGbJoGYgnzuKm_FwFmM0Fs5CT-B45UKF51Is2Mc0MLdh_h4Jd9XhFBscv_395Q3kqZwbF6vC7rMqRZE7CImnA_H9RDKyCARbqYx86DuDFa7US6aHNMmm_LMu03pcFMyz8f0nZf9rZpI_ieA47enN66_HDOVP2Xy5sCHBdLcmetv5lLTSbirS4v9qe66dak3tZMw3CBBeN0UGKHgRwSAUVHKhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45277758ee.mp4?token=jCotd2p7Y_FZqL3uooLMpNfJ3YUqN7AqXjrx3kYcl-D8868sgLfylzSqk0Ma_Lo9oqQEgygIskDLE1gO_VdcI-r7ghpZMIP01k_rIgn0SLljKGiDJDT8xRKitJkq4LGbJoGYgnzuKm_FwFmM0Fs5CT-B45UKF51Is2Mc0MLdh_h4Jd9XhFBscv_395Q3kqZwbF6vC7rMqRZE7CImnA_H9RDKyCARbqYx86DuDFa7US6aHNMmm_LMu03pcFMyz8f0nZf9rZpI_ieA47enN66_HDOVP2Xy5sCHBdLcmetv5lLTSbirS4v9qe66dak3tZMw3CBBeN0UGKHgRwSAUVHKhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی بعد از دیدار برابر مصر: خدا سر ناسازگاری با ما داره. شایدم خدا داره من رو می‌کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25337">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNZyfLshKqm_PM9kvrsN-K2_7lXsXBp1YubD1SVTTbXfY-JcYZ8hs5LDyOmushX0Lqb9HxFTcUyye8mLWh0mGmwaMXbQC0B8vvgCI4AQcbH5IRwHrT2FhjOlL9HUlpZ775_dDwckiUOUAsAiKXXj2vjzu7pQfWdxvTda_ZWK9cx83aSb8AVSIORSZUsjAAg6QdtVgm8QGL-towb5Ta5FQgChDJTs4Tjez5qbRELLWsXZUQT5JfHOYbFX74KaPGLn4UxwyGCXZx-30n2BJJy5iMrY7rmNjVBqNLlQ0uKVCa6J3CAxBr_1NFcO9Ce6h7rlxdWOx3Jd6qLDdNUbOdnA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی
⚽️
⚽️
اسپانیا
🇪🇸
✖️
🇧🇪
بلژیک
⏰
امشب ساعت 22:30
🚨
ورزشگاه سو فای
💰
در صورت پیش بینی اشتباه مسابقات جام جهانی ،
5️⃣
میلیون ریال فری بت دریافت کنید
🔥
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
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
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr19
📩
@winro_io</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25337" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwwJc9b_6zb3m3M8fuDr36f1phli7VTt5WVJMSsZP4UDFtLCs7MznYA2UdHcmvqu0-AmBLla2jpmUbQva87NrXndZr6qhmQ_Shq8WBN4Y7BfIVYIzzEZpf-HA7ieTFJ2hYsfstcwoWXU6ewFuxFn3lzVk26OruHYtZNW6DlOn0o475bJGs6-dq3JPWyezF-3PajUYH-4cisg3Koq3guYX9je3TlNI5LAn4G9h70orZccja0drR28Fpiqrjgc40ymMwz6khDKUQIPkp9Z1YXT6XfhNRUyoTRzbWFYbBloypoUO3a52U2ekp5QkpzoAtBtC-qw9uNACNDDoZ41vv7n5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ2h4RK-mKmxSIOR4OD85ISDs8uh0NC1T47tfFOfSVDWYj4dsN3Szje08tbvlram2P7jTCsaratDNLvufYX2t07OsQpmv4LpozlsoFaDbiWEkBS-m5dM94ZyA4q1S-XGEYVA27-MOfa9zBVK7FgBcuZXhEVNc_dGRmfJ_C5g6JqlmlCBMOJV1pAHaj0T4pITnk2MkSiNgPFr8IpCG3PahfwqCcppGHGRfM_Hi0I-Tw93HIPKyQmEswrEr9Z_l9yqD9ObsdYDQeAgjhxMgqByZa5PhAuTvfjlke2HfRtKXXT_p26WCFl8YcTkwAt8AzZQDwyRsaxs9KSOZ08-CAqR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOtlBNokXMmEvwziUdmkADdVU_GPaNxC_a_n2y1X6ZpqqtZM2aY3T8aw3Ng0v3mAOMBxAGE9tHmquOo4JxSZgebYZRXqlQRmiLaU2zcHORtNM8KFebZLlcQUVm8JYMesf41GGm2xS3UQnB2Exn0DYQsdc8uDQ_tT-kKlvw_V9vv45vJ8D-8-BP3O5Hjqulttcb1hs8sX3DYqjxYOjrC0Np2tQ770SbW4D4Hk82GVBx5vMCoRQeF3yqkOEa_hmuhPsFzTO6B8FOvTGxEm9V89FtM-2eBXAgzvv0Vxak7lqtadR5eJ59c0FkJaM9qbXk6ZjkwfgWwK7mewbt0dm7oxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX6Pm3yEDzqGXHKTh6OWNs7eXVwW3_yFFqa88XShG6aZrFngvqdrSZmnA6m2e3OA1SzMKcPAQRq3UyZ521ejMEu8ExZVGOMwDnrHPxnrK7IbXBS83oHbz5nAKK1rdd_kgs7oY58ef7iajrOzmlj0-iNVroHzY9L1GQAHHxaamNcfM2Gz8CRMAR7ZfW4R0DylxRGgRtVfUXYC6t8_AN-_DZXfP-O5-9lDLz_3CRbq45RHmDHtbhDDgCc2sjSVfD6kKyRpkNu-F5BVvsnqVP4FTs9yz2B7U06M2nZaJy_1SKhIBy-YK3KJuY1uZEixVmSczSpLH8rWyOTQPEGlOeY5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2Eu5kgIMqMVCXgSj1P_zouau25o70ocOSI0DzEwqwhZuh7B3Law0ryPiybnzYq18q8QzyRpT2vg-h_tEx-VyEAp3vXNx0RGCtcL2o5UunXNGVpzhzRCuXnNWZtVI3KF6etYiPkgZGm0gZ3qa5zil8Tg5iiilFFCoAHLy9QzZ89KM-CixCiZkiAXAk7mf1s1EXy6kgbKCEu5wSknbbRq_fkbg0hW3yMMHkUBWo5NdLuLzuHRn9ZXMnF8crjEaoX5J4E-K3VFVXpWlun0QKG6_eJCjW2ZtmN1ZY1F7ZO-a8HVTXMl1eZnrutGhaQLygYSKcVUGZPmnLQPiMpUJOgXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcfQ_o_Jh3SoMsYswFeFvpXvRdOlGtXhBe0LVYa7N3UV7Bdf7M9UoNcvmWF34imfr0GJpq3hKYdLGa2JbdL45XqCfZPxjXX2MRnMCvrzDqv8EnH5IA-RrJhcs37PQ0BbBVK0867Rb8zwwjj70xGzf8cApjDsklxPBeDVij1Szmlbys47LcpWJg6U98KaJ_FM95kTk7HLYWGj6ZmNMNKheGrNxWhb7pYlgy23PBKzxiBVNR8Gti2FBHDicsYLTHY3ZEzpvAfs7xFEqizFmaYpt7bgvAjNG7b7WuLQ0IN-ogQKrwxun3-e4a85OhlbdJUQhVz43GEL6cg-_LPKR8Vigg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oC9zA3-OaVqPiy_38LkYku9kHH4Di38NvqP93gFg1ICqUbdSzOpwUOGxJ9fM1tb1XeNTCvlZACst6MSec1pac99lqtYW8j5vYjzWtb2DmR66bFKJ5hxD0dOrfaGE5mB3D-EJtvAmfP1s83vUte1yZxKv92YFN3XYxIQeJHV7WJ8pENkSs0SxGEFWtChnAeV_Zobt-512o_sFSTnqJOBIVgqveqXIWNtoMqxReNjz-ZVdh7BbPNz81q72TPSJfemJC4itknzKbRA6F61kwxJFuiqNukZXLdaz3l4NSMt355LsOls7yrgNLntgjtGdHmFwbl-aLL2DBktwv_YVqMsLvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YmTBbb_X4MZRWj0naTK8CCE6RLXadu-8TfxFlPTWMSFq5i2KhcSTyCLolyyWVLCMQWccJIAp3R6GOSDVH1GOcBppJtN3G_Pe3un9fh-_hzJcMCKaIqkG39fiIYRGh6n8lXytlKV4m64VXfoN60SXl8XjRe85t15FT9Jbe5NwJzwVJWun4TNYo_vzLXnhrOGbwVMcdV9ZFdXx8CeAhsBqFJzLXUtE17TR8TUK-Zbqj3kq2xO5vIsqjMQfoi6vclGC-bA2yODS3LvidmK2VhZNsCcj8erTwcgZ613gLT4DOhGUQeGNzsMPMuFFvLiIfpJoXKIIVLQsIrgTlyw9x9KsZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgccI0h7QHDcF1U01DhEzre_fac3K6kyIkfP3RDUVnGUoqHOg8M6y2mQyFhsi7aRE6xNOeyG7FItHugLGJKA8T_fH_RBlDzkfjzBY54h5ywQSixpa0-1ffQEXleGg4LsOh_U7YAsvwFjkQF8ejX4qJbQ3nWLQOipa1w8a3wKYRBZn_i3hiwzvO4QBDNuWhE4i2ju-UbpXhMDHLc9SgSi_DzlXQ4tGIPAabWgTi-LJ11dRCEMZAs4jNYcnI--I6VF7dOmLVhoh3VN_jOzAImjtfHGx4RSKcsrnF3Op2MHP79u49dksFMWBaci_KU3jqvo4rNYrNO-RL8jq1wVvmMhDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lnxf-PPkV25g2MZvl5xx39LBVW7n57PckgrMfaVQrpmDRMzrHjK2gelPy3xjoqKgvqigp1TDE03fQkXXTgBtVftChr10ctQfZGSrzhQcgQBMZKZBvoxGBT1CK199JyNPtwDKLyKa5WA-hSsy1SEDzXPIWrTP2NYCWdWmOwqRMtUkqZhB4_OSJss_UgwmReUpge89KcWFs6Mk8pFdo-Zr21pFr_0xRRbDOp4TBqbOzvBnVxeiSTzLFD_PLr3MUWifx3bEn9q1r8UYCsvNre_o7yttfhWrg5LSHngiTtPFj_NHaX13hVj7siqObeIOk8hMvSJbVGlsmlOFQQWVyGgxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4-aGP-oMkiVWtYPY3KHcWJzW6kH5FR1G3cLmveKnz6eVLaRS8Myfhkisp8rC5apL0MVt22m19UgHODcP9wv_a0_N1Uxm1Yh6VB2RHCHfC7rWJgzF0cvxN-91fHrlAJJnI6K1_ojvhS3vKQgQIt_yKvr3xXnk2nO8dT0WPe2tFziKvdJ1z5lvsbhtjvGtSRAjt8piYIFgrG07wZsqzXO9aPArunyfEKmYGU88YbIMiXDhWnNTHE4P5pf4Jcd1LN3sLd2NyQVc0qKMFD0AsJRi1lmYV3xiGE4f5DbvefSbW7__NiYmTPqdmJzYEqsm1tws--iRe8yPNAivBoH563vTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGGhJIFJiGLibyzo01WqDNaPrToyXbecwrE7rOajzNNHc9MlMorFqn0EU-JU3MJ9ZWZhYEtL0WxG12Kg4m7V5gCMEKFgd4JWXqsBATTh8nl76gscIyfwA2UU_dR0eQTpXc3hOV7I_tv8sDC_LK74TDL4SNIxMaj0ainhXJLVnPMy0BGmvYf8ro5WFNRsFl_VK7R1jX5aKgbMPLvOslAwuYHU8_cbGY5NpB4IxwRPL_cwTtiL1eczxJqukhRIdDhrd6_RUfHDur4YjMgXPvyg8JyTXSxu44spmWt02uTpkR0STaVYshTWDFhSCaAOlhgssO1OGZTfOWnVPqpGJaS1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxQxRseHmtFE8k9N8Vy01KqtCaZ5NYliR2so0X5gSPLWTU-FghKNtMIGFDgtoP-NhUwdoWxkLb8JT9_z1s3sf4EtdgB3O6uRIW-O1YdxpffnxRQQzH0WWFEzZD8_eoZQ0taAl98YhcxjcxtWzTEgVUeOR166vBNCy8_oWI-uhgbuwxnbD2TvvcTCn89l4OkpBnFxpvoEA5GdpLSs6HQ52c8e-yi22wU1nkNjXropi-4n4-J8KsTR2duJxiMK30by1jbUxh3Ue8ALp83ES3vAG-uECm08ANdx6v3Hjlt7jhvpcfZROa8WJotGe2bq1XJqZKs8X6niSQnQDU4hPdbXGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYQpzognCkB7etcr3g2catVGat0X_1thFlGPriaqGo-7BssgYe0NNEDzLt8_ln7F-YQOgwCPQRR3pnsujz_PG7p8tAsoAIm1pD6prB2W3u7WIR82xvy5Ua-PwGzaLQ6gGYWouEy0Yk4AVdHAfP_hoikhPxp4CI8Pi7s_2l_OaBd12Wd6GZi0fGhZB9D6CTx4MK_TkvxXuw0zA_kghHkRjCP3MBXcONBrsYil93dXo7HnTZv-8A8nn_ZyyH9_wcJFbtTNm7VpGUXrEBf72WLAV2vPn2fAtNzidXb-hidfZQruXIz5Xa2f7ODKkzkopKJ7UF_i2BnQYijmbMYyE522og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrIIy9tS-IU-mOSPoYY0BQIylTozs8zLteT_9EziJsQP5J3jE3bLzOfinC2JQttdrxpcik91Ot8wnZIKxKzGn7yKL4yblRlvlJq0wCTwq32YB-f-FZ8P3H2TEQ_lnZTLVWwGNmER5PheAUMLSsRpTMpxbEbfb0GjsAR_uokJ6mVSqgbTiwyPbZgX8vc7uUmWAz7Taf6FBDlq22SKwukOqQOpPP08X-NhRxZmRHsSCSJxHqIXPNrAMmH9IxZ8mKI3s_JZFbiJkl5UlwDAJlhtBFZax5AgmCgWtTFCUI8j8YMTKWeLDsrd7eJfEvEXuG3A8Lob5sxn-lV6z4kuQdzNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDnMDyWDSg5d9TUBW9smyvm2KffYh2qayqRlfHY2u3207KkbULeI1Cpj_NIBoSKvXO-xdU8H27ZESggpcmdW1z1Nn-dGBcmGqOg5EqhAlAyHVN-ysleSYd5XIIiL71I5e26lQxyUmNds6vHMZ6QAs8LtszKJVS93cvG9mNH2guz0c0HNCHy8FJjAegKYRD0Ws7BoIr8KqB-oNL6mH4jbru0O-ZIrEqlBibBsqFVosHdxONYvB5iNdGZk7uypLLIPArNdsLDwfuMnBp1r5Ou5R-UJbOYPKT1FUqmfu-x3YjK12i3JwlwMPK8I4G4Vo149UkrPalH50aylOUxjk9B58g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ-tfreinC4e-4SKOvCZlvqGYBEP0JYnj2pn3RPKbivDD1XZ4T4yqPcGuTS076ta-uhCPRNOO6locW66WTHhOfiMSi2N7wegb0dvwzuiH5XSxUkdmopz7OUHYOXNvpqkAw39mooV6_8qBoRNREb-Ya1e2xbH3duugUYX7Xr680WZ4uXdvwIq9oa1RCrG3ijVUt7d45bWUgUY4k1ywNdpTBRSr3mBR8wuKoR6_R01ORY8C1An_mj6Gz8lxXBmFDi_zA4mJdoxvKxApXn6SkMIJaUKYbg6uPu23k7GoeXCQ3flki0v7zQld0cppykpQRUzaBsmkYSLEKsyaA2TsG5pJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQixIskXmet07f-yD2lHpeEptIaqM2925cbDbqSuN2hR3jJqz_cN7AfzpX4rhEKC_4FPNvlqBFtmt-Gd3WWqv1Ql9zY6SqcnHjBz7JTEU-sxKtIMmTF_58ESdGpWp87-GZz3bZvnFXzRDKm0wAxdB307xwY89BkeIXZj-U6z6lbW14-Wd_BUuUhvfOaphtvgQPRyUn5wBUgrptTIwgx4OEVt250J9zLGz7gX5EYChj8uWYFGIDwHwzDmPNXJMrWP8mImNZbTNf53ZSo9J8azm53n3xmZojAo7pM3e6OYqEsZKq24OwI8robeziD_rAuKc5d_9rplrQCmvD8xgat8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2548666d77.mp4?token=EvGhUNS3UMmm_rmMYNbMgZiJOjL20Blo-iW03rv_c8-HL_ikGicuaR9v7jJgZvnl9HELD42K6gmanDQhfJlUflJjiLILEYrvbupudWBc0OXQG8yxWLte8EuKz5wzSZMLp0Wiib6fr_CzRTh0fsp7tvAWYPa0zh0e9wfYTjp5SkTD5gED5FEoJkZ_Tnk4g0wqgMDBJJDNbFVH6ha7H8i1NPc1HmjwYiWe6PWzkFisTb0MY27i1RMsigQhQoC_p0FhNVf9xGN2C_VvBLFufFidldPR56wOs1UX8t43HikR7pgHBTJb1syhTvq1goX3ePbeQauu5IuWA2jd9spnt86a5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2548666d77.mp4?token=EvGhUNS3UMmm_rmMYNbMgZiJOjL20Blo-iW03rv_c8-HL_ikGicuaR9v7jJgZvnl9HELD42K6gmanDQhfJlUflJjiLILEYrvbupudWBc0OXQG8yxWLte8EuKz5wzSZMLp0Wiib6fr_CzRTh0fsp7tvAWYPa0zh0e9wfYTjp5SkTD5gED5FEoJkZ_Tnk4g0wqgMDBJJDNbFVH6ha7H8i1NPc1HmjwYiWe6PWzkFisTb0MY27i1RMsigQhQoC_p0FhNVf9xGN2C_VvBLFufFidldPR56wOs1UX8t43HikR7pgHBTJb1syhTvq1goX3ePbeQauu5IuWA2jd9spnt86a5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
شما حتی خارج از زمین‌بازی‌هم لایق احترام هستی آقای کریس رونالدو؛ شخصیت بینظیر و قلب بزرگی که داری رو هرگز فراموش نخواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=f1vv-jRaqJbY5kKn20roTWMQAXVY4tJ7EE_8gSkpExlD8k6rqB2r0p44z5eHypqgIvZptQxF2VT_U9UpLcPdxQj1dG3cxPCANfP4XUzVQsQRHKE6G9uxhL1Sbf32cYwZrMcHzNE3ZmfMBuftslw9mh9vZ-bsfJ027YtiKmGOu0CrRn1jmLuq9Rj-FI9exKx9oeOaI8OybtOgx2kw-pRM86PnwFRgn7hJImydEIoF7J4D7mrtYxvQgEmvYhaiGqOMNm0wJMXY97ytfGUMaBOimWuIT0mBL7klqWkKFmvN3K-IN7CBcvzFP59u_s0BnOhY6178Zxqn3ckxmljdhCfPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=f1vv-jRaqJbY5kKn20roTWMQAXVY4tJ7EE_8gSkpExlD8k6rqB2r0p44z5eHypqgIvZptQxF2VT_U9UpLcPdxQj1dG3cxPCANfP4XUzVQsQRHKE6G9uxhL1Sbf32cYwZrMcHzNE3ZmfMBuftslw9mh9vZ-bsfJ027YtiKmGOu0CrRn1jmLuq9Rj-FI9exKx9oeOaI8OybtOgx2kw-pRM86PnwFRgn7hJImydEIoF7J4D7mrtYxvQgEmvYhaiGqOMNm0wJMXY97ytfGUMaBOimWuIT0mBL7klqWkKFmvN3K-IN7CBcvzFP59u_s0BnOhY6178Zxqn3ckxmljdhCfPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=Swcz8c4Z-xj1Ti64dv8wc0VeFIGvyqoDLQ90vWprVVpZC7Bh7-NXy_DDbnwL9XfrwNjTwyblPv4w_6h4_3tailRE9cRvUtRDqTVtBb7zPc-JXoLrxqXk_n5xFg0w2ud8hZCMET0P0dJBYXD9ZjJub4-AWE4tQSF_cXoct-1_048lz3Xef0EB5pkB9LEKgs74ZrCRZ5kLmI53MPjG5oy5AfMCrXGZKA0sdknUfLmdiGGXs1Ywm-sQZ-rpqLno5UVXAieRPjlGmWAT4IYuUTe7U0KqfJ3LMeNd0TTDGttzsitj_P8QlWwDGHzvza7epD6XCa_UG2p1MHSv20Ttf3EOZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=Swcz8c4Z-xj1Ti64dv8wc0VeFIGvyqoDLQ90vWprVVpZC7Bh7-NXy_DDbnwL9XfrwNjTwyblPv4w_6h4_3tailRE9cRvUtRDqTVtBb7zPc-JXoLrxqXk_n5xFg0w2ud8hZCMET0P0dJBYXD9ZjJub4-AWE4tQSF_cXoct-1_048lz3Xef0EB5pkB9LEKgs74ZrCRZ5kLmI53MPjG5oy5AfMCrXGZKA0sdknUfLmdiGGXs1Ywm-sQZ-rpqLno5UVXAieRPjlGmWAT4IYuUTe7U0KqfJ3LMeNd0TTDGttzsitj_P8QlWwDGHzvza7epD6XCa_UG2p1MHSv20Ttf3EOZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SazHrmmrtJNEGL34fiOojEu6lbFRs2vTeBS3n65cJcS9LJ7L6Q8bd4o0IUrU5dqcBl3UjfEkgFXbn4kk3mXNt8mhsktlQwsm9RWTI3rRev0RYtKrNK8QXYjWrmwgTqpo5V9vcgyMJc0NP_V_0JyBfiC8uj2zJiWp1JrmIwHR9KZlALYhAI6DH4giwQiVh-_foa-5V7TkVJThxTM-mBK_kVy2UroNl7hIdycEJfWb4Z-EqC67LSuMq2NpOQc9mHV-TrwUORipDoqyCHxrWa25s6hixHhaKZeE2TZVknRPC3ZUVGcBUpY8oo4IC-47GMyz8IUtW0z_7oGBlBf7ttjIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmFEyZ9FQhPqq3ym4C8WImX_iXReuTTuuXjqcWIQPFO8iAEsjkxajKD7T4oa0I3asg8disGwdyxKZzLWcVZWeffR6KlH-phZRbxkRMVnne0tNVK6OEBiu2rnZO9mMl0fB2wt1AO1d70-yA6HLCmc3_yb2N1ONkph2knPpf5oqqWRI3NYZQIG-O7VxmEiJaa73YnU3iwWCqbzjOilmn2khsV486Cu2Zx-o7laFgZH2Ees11kAnNc9RVNmItO-K1-_l7K4imwDnqdWL5NI9jXPYH0fkIJhm66ooOIW-MGT6tUhSiT8bwWRghhqGDrEtDlHQiBX6n6V5P6xumkRetZd1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=UEkKeZ-kJ0BNK2M0itcbbg5P7-182CdfrsoXd_CdruH-cxFgM7-esWlt3iENyJkXz3hggFTS6Hbj8Q9TyLEJ8bEEWVAAArq-YzPtkF9a4gAGgXh0AuMPVgTsGwMpi_LzO9JLQEjGZieVLJ64N7P7o1bIC1TC2TrWanhDDfwRmFpgTpw0rFjHw5THaN0q9iuTEEU7ZxO4dGvF0EIxczdNNbJRHosJ8T9vpZtm_9i2HrUFWHmLzUhT_fFf_VoTNhREnjD2O2Vi_HwCf_Gqwx7ea9nJ_ScN6ul6_ZIfUaKG0nCW54KQTjKsoN4RgbLmn4rmUJIPvo-K4eq3euJTnaIOqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=UEkKeZ-kJ0BNK2M0itcbbg5P7-182CdfrsoXd_CdruH-cxFgM7-esWlt3iENyJkXz3hggFTS6Hbj8Q9TyLEJ8bEEWVAAArq-YzPtkF9a4gAGgXh0AuMPVgTsGwMpi_LzO9JLQEjGZieVLJ64N7P7o1bIC1TC2TrWanhDDfwRmFpgTpw0rFjHw5THaN0q9iuTEEU7ZxO4dGvF0EIxczdNNbJRHosJ8T9vpZtm_9i2HrUFWHmLzUhT_fFf_VoTNhREnjD2O2Vi_HwCf_Gqwx7ea9nJ_ScN6ul6_ZIfUaKG0nCW54KQTjKsoN4RgbLmn4rmUJIPvo-K4eq3euJTnaIOqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOhK8DLk42car_j0Z_DTPq5A9IQphzc76VcEYFXfwLbYu3P38VXZ_txKaRyBNaQFBKiJj1-7AGv0N1crIWU1WA_UnQRWLQt7zIO73S1MSqsZ-3eJGqn5E4ztQ9Y_G1AJOJcJmq6ffb5O4myap6xRd9be8ld1tWbESpziNXLTeR3iFEOsJ5JHRJRbRbSRGFNPmGmDG9Bhzn8kQx1KMioXOdL3_9_LPfQjutKrxcRY0YZrHgspIv7GXxwCUKbKvLuI4PYSxSgoeqadfPwRtefrXcizOozp_wrU1iYID0kapoYALrqBqJ8b2uUL-RBXNNaj5T1iXg82cKpwOIoqsCUlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTfoOKLisTb9iSdf5H21Nqnci7YuE_fKrnYsd1rJkOZFEiZLvehv3ZhTpetHzQG6PyFJaAr8iGpBzHLrXluaCPEsqJncYbbyIxlJsJEX3Guj9p4RZ7JK3oEovb0ajyZ3dIDIz8e2vdu6lmLoPw-KuK82idzdPgBhDHJJXIqniEf2-qzP_wYyH42lZ79FKE0kMO_BbnTNQl0Jy2mimHblgJcQEJy5OotQtpvNmnW-ojeXj9qjPhr1YU1XyfVsU7WLvp-ciKe_4shysofwDoLYjytDAZN3lCJy3ZLGdlFutxE69z0RbcQkrRxSu7Ky03_JnzCDVNScL31o32WKRTukFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLxfBkSCynOL5TkWfXG9_Wc9mkQgxPW0NPwL8RtScPGJcHiXrjcpjbQqPXPg7qx9xEEFMVeqHnaJpvcuHoTUlFgGEM1KJPdIj2fehrVmKPQMoa8Aeqz2kuMoDKhrdWmYnHvZfzYwaPWN2z0935slAyqd3J6MJ8TI4bFa3sw3nV49pgelR28vxv-ua5cG7MEar9SPQmo8td7fYF8x9Q4y2yldH0Pry2qD_woq3SJk1WcOf3u2AWyN7nfYepEGIglMDGELE-nzdtW3Ozz7yjj8dZOUxdpJ6QDgi7gVj_rfEafyiuJGwbg2Vr8oy3vZ_7EwD4jMskDqvr3nTMJwRMghSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEPKOXaGZwsysvJJdBtSzYnaGi2UlwOHEfmGHXb6AVdiyq8c4wCP8cpcKrs2wsDFO3Y4OWSQwQyecC36TzR5R19Vgp-E9xbAXLF-vN2aTJQFlHIuCtQQ8xM9cr2bXqNY9yxPkzkls87t3r3CwP1IJPVfIv1MEXZGj2rMIcAQ50KcgJcSfrtgs-12jNh1V2VmEJq9tGNaCtDU63dZOHsRK9RRda5sfgHdLNm5EPRpUqlVVDprqMx1hAm_rVsVf78b6QprX_kZd-e1TS4kwAO2O54kDCOjJpBj4kr1mxoocSs3L5U2yAPSxJIzDRQgdV5wy4Z34Fx4twmoyaoVFXl3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3BkE0PsIcgcX_qoub77I5qOh6IqalHCN-pzKi1LwnqfBTVZA0Z7Ubp09Qom4JsAUu4SQjPXwELzEhaDW6o5uO5fLH1PNasFoyXhEHRn_CQOurR13fVYquoPp8Yt3y6o6bYoxBpHZDkWEo4DRfrG1topG_jn6b5AZd3RdoVCFGttMyNBE6fXTkTqii1Oqu9OyA3BX06m9J2F9wsT0v3KOTVmUhP5ehNBHjFG33JfCvrTP4ZsVQuFI6OM4ZHfxsCQQvLqYlWjzBxGMYzEYUH4ZvUcomFCjOS0H3ZukBKZu29PNEwabQoK371VYpQ1zMmPRz5_bYABaIwyFNyK3oAegg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GdargN4H7iF7aOu5QKQL3uEgNa6RKuHLNMP_6-9_NmdiNrs_UjyXRGSIrt78jKN_gPewP3lFBMydeph_5oclvCSX4oO0z8s00-zi_KOzAgJhST19eN2NkBDaW3SJXUgNsMKRsLlJ4rqt3IpNTH_QKdW9GvgkCCurDEk-zabW6XV9fUgAjpK7VKNQMbTJzSz-uVc9JZUMt4m-hDI4DAjMHmMaHxz7f4Rxo6daJCTNz7iks7PsS8n23mXNVuSup1suOOHYc-D5do0GCQe3wfwS_WNIeTfeO7sQiY-fsqN7qpA-mExPetx9b5Cr61CsBCzErI_WJrgOof8rD4NDFKVfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PafhxANIdhOihSD8957E0MQXcfWTJjxBu-gvgUEdPfGHRWVexVCxJ6TsyovEZtCPn5Ckeigw78VA07vKug3FWYy-q6nrDp5AFEX-UUimrR_MhitqPEenHqdVbues5ReDu0RJ7IoI5TEJwaKYT1k9-IwEqyEk5I8mkpNZYSL2PVtJc-kfcYyezR4ugrzxZfiqWqD3GKuzZSSVu-PZ8utwkgOFHrVDnHBAq7clb3v78z0w6pDJR5mYmK8lf1AAbaYx20ftnKVH2Oa9ynLOKLt7RA6pqUcBgmpy58MqTy2MEFnrDY9jp-yl0IK9A92dzSIgt-AHnrLoa_576t_YuBqfCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ازترکیب دوتیم‌فرانسه-مراکش در جام جهانی 2022 فقط 9 بازیکن همچنان در این دو تیم باقی‌موندن. بقیه‌خداحافظی‌کرده‌اند از بازیهای ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id7Kru3aX0tP5eYnUwv02j9WHEj4EvZvFuyLy1bg6jC4aNG2l6GedDA2mwrK-XgQ9H2AI3-8cnHm5Ps6cg8va3pUckaZIdp89fHvXZbYXS4VcAg3cFmytAKFAdlvO7GGag5TW1w2pREJwKL3R6tTbeX8abgHkrkaxulTsBq1kq-02JJ24-GP3QpXwJ0Ovep_57GPl36qNDT3N6C-6KfzbE5GDAMddwhU2Sx-G6m50C9jUPJCRzbDnn3D-ndACIgVYeauL2WyEIYiSSF9m3dSjDqw2WOVU4cUxkNRJta9uxerZuNHgJA2jX-xtlk8fofwvZHKO3zf3fjEhG2esqQvyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmdtqHokS5_IgdUDaEUhe2yE_m4aG2vgZ66fCL3YXBA3HzzzES_GRJSF954ULOPGSA5hYn8DlzqPG44EOnDpPqmMp5qx4WqePurvUMoNjcMTM7ggyFU1lxWLVz0KaqmUWag4V4_KchHIOmUOMFnOofricn_Mcozw5xR8rb07BhexmcoNpuYgqamal8jF0hsCIeVqdxfGLdq6hrdnESyVNceI3JqmR7L8yCazrH2e105OhBGtxA384eNuxOHoctjyO64aRXd6_O5-MyjbjwueY4oRoUK_-hgJxifW5YlRYc_eUc9ZUed6XNWKb1JopRGuAzhpcwIPSXjiSd94cpR8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ec9GPbyT35GQ6UDiWVFgH1foPVKcj-8FArpapbtIPFlhVgi74ejYzzxSii92xSGW3eKVQB6LStUwAd26t1Tdr7TYKjatY5M8FzhGWidv9-VLWCORdMxpxmZBM5z-mwlMSBGncsSknh-M7Jfe_E63cFdoVMNF-WFUdqrBPyhBKAfsYuNiRe3NxnTH66qCK7ll7x9blGNyFpLu272jljf-AO_zwGloQzIhpaVQY42yqGatP1459nWrnG0FYQv-BP5rypS5kaq8nXrqz1ihuys-JVsJFVOUCRgQfuRzqovNLB1XT32UlAz3yVMx9nxQf3vBlez-i2DKe0c6Gr_33-HL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UC3J5jpzPcgxd3XFJNrdJkV2YLdLYNCgbPMs3jWM41chLcGerEMMgx4v6gvlXCMUtRCc04LXtweLp2ge9sYOeiJj0NM4MQiZqdDo1cCOZ7ToD_akgkOG7AJQ7IJWoNVuHhPS3-am52dUnG-Xm3hUTnCJzbWHr57Y8JWV8_z_x7eaqF8AcCR8JRg4KE2mTUJ_G7xxKGDdmv8nWHs5o3RlHBw7Cb_NmKdzBOqU2CEOH0_RcDx6LF7MTv3y3wrHNEUqCotiGHRPgTQgqz6zsATouIqcrYagVVc4cf3MPlnDQ-7y31US9m_0A8DnwDZ1ZbE3x8DKW2e8ZKORoJtcMBjsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOSNlGtvG9LYLR-KpP0VGMBLQtr8sq7IjQObo9_JYVdq_WULf0vamP_LYotek9IWqo5RNN-hNg7P0nGwzWf9t92sD5tgAeUnjmqrD2qdDJxpIq74TyaafFODaY_QVLpQFSdheMOIC6hPMvI2tX-XF63JJ1Sc050f4DLDMuKKUI8iuEjPouphf3K9YXJckqtTl9ESF4m_91gb869I4cdUWdgxtBQMDhFbgcsz_Pmnwd4IDgmPBY15YDkjRMYXjiHlAS-GeJpfNdSjR-1hI94nq77k4InsFDF83RgiRl9WU2aTPR8V52Z5ZzdQqqGY6VB8CoFSUTb7CA6jqrxDStqNiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiMfJfotB9vyJn7VEnkz00ujH-ezVV_mq1SEWTN9BQKC6gJMgZ_6kZ1g7ACL-LeDb1qj5gdmdmxoWOKTHSSZLa1FcImsFD_ImdXzQGIKRLNkwgd67qsn1I_1PJ6UqIE-VMlz_0u7-3_W6jjG3DyxVzDa9OOYSP5Go9EaQWzlymdsYx82x8V6tnkUtNDhvGwTL4KF-9VzXFgimm7kD5d8Mb3Ibb8KebfKV_DEp6rjiqRV7q81-RZGuzXEm5rAebk7BL7EQbqj4CvGiayoaujB1CMSYNAeny7s1pm8puuNjL7eKxF1eaA_fD4B2xAYQWPYmxp4qwQZTtnKoZDp-YSjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3P263YCntEakMwWiXmfGYXLXrV-zGYxta9dIkm37MqP1FHdlEznjibXx-cFAgQ53JHOBW3w4rA7x6KXBLv4zDJfVT_ZRu92r1KXZuw1Zb6nm_Vg73qPrCDM0vzT6Gb8xVh6ZErSYrHVSoXet8QqOdd0S8EV2V5EVwDpmcTasOhYqdKWvLYIP-dEQJe0_buz_3Fb6qYIWL3_Bqduo0mbFOGPCQVG0tJfb_0EKMl9JhR-iVN9maY5NjWPSUkB_oKyF7jOhqIUHdEXgMFJHmlNz6dntXsrenEq8_zADRH8wYvl2cO6J088M15sSuHgCi4Z1SfkvebZ02lroe6T2p0WVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25297" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmGT2Zu5xJqVtmrtA-H3ntHkKesjWAIuXNkjtJAZnfp6510w5sDSParF4dxkp_J1g0tQ_RyYO4sI3QyBKbY9IpoaOK9OXru8581P7W8JKWqfqJ_WpVLi8volM9C56UdXTdd4ZXAUTfkp8_5SN97KYpAAAnVBd9m60yelf0p8ADhKUdHJuyfd_hwDnKiK2en9CmUesN3kVMcYArDXBJfA6p2L3QI8HMvMvtlozOTjyQoW3jWZKXq96y5cTZVCu2EXSRZRQ3Vlko4IaSmkhHHXZLf86UPxI6qh_Ge-etSRpPq94VncIR6pA8-jPjxgvtS71poCpwT_0zwEHw7PSIAJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بنیامین تانیاهو
: راستش‌روکه بخواین لیونل مسی 39 سالشه و اون قبلاً هر چیزی که میخواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی‌خودش‌رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم؛ حالا از فردا بازی های آرژانتین از صداوسیما پخش نشد تعجب نکنید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Saoj2uLiqIaOJSNeVYjrRNlj6JwrKIzzBpJR1-m0eFTG_eJb0i78ZhC-Z3g3XPPhz6biAzoUH1VboQDlrWhtB-RbIrRMuzeIF2W1xO2mlpTIETOYreUx6SqtdhupeOK2BWrcoUidEag0rVI-gYye4SQ7qGeFU-IiKA6MT5S7SBlA_CxKd_1dl2ZHZyls8ftaCW7IwV8Qd6WpaC6ak2JdsDzl2Kn_VvKfZhie4gjZz-WW_GXKMFbo84-gibQD6Opqp-NopO6pXhWEcR9Hco3OAmaAXuDGpJnc78lgKPt4XQfoaS73WNRrWa6_VQblpRBUufDfmkEeZb3JDUzTIWGXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k67lvMYGF2qCBY5qYaRW1gabxXrv5dztg7HAyFDS-6Mp14sC7kIlZMsorRyb6v8qUDqrSlkHSLsxjTWG62Y2XWHn0l8ZH6ecI-5WkKfbY-PnK-IdDqWbzwv-oSKQ5my2Keo6bQKoaWo2npZekUFaaTXcLxs46EN_vFLoNMf4joa8C5nDY_B-2DJ6-OrEP0nsyk2rufzZsmJVFZfyk_L1t36uv4VDu5_byAUYKMf03qM9tNPoiY59r0MPjFBYgmzbRELn9lZC7XSTVVmcZY7vq_jzv5I6RUpaGsYfdjjEP7UEbG7FXdwOJezY4dB6NeUnUJGYhVvfqXASIMea3eNHPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP23Aj3ciKDWlOqEpEmDDNKw0xFWby-Z-HKgiHSoG-ytsfnhAveSwS01pVPhY-8V8vUs0LqZRnPIMlnlUBXF6Lee-nh_G4l-1xsbk7yDvMBgsqiI0c3K7VHMKwahcDm3uP2DQBjHhKo0YT2p2CuVlT4tVHBVTo5oGoVpWD_4ahnfVAVNnSydSqorUq2MBkuB2wNKqETwwDi0_sfzNdxzmClbzxVUiKjKTJep7ruV433FPUroK-RnFZV4_YZytaFkVn6c2gAIXY6FttB2j_64LbbhHyQpjaeQkLkU9Bb0G1Y_LzvpXuMeB3r2w44_Jbs2KuQIqii9AxP9K9AZ8bKvcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSFlnL4IW1-b7l_64EVLuGpAcgcBI5-YaY8SoVI8GN2XSrcnpesm0T0KxESytFfGceQvEQmhlcZQm0EuN0Qdd9BW7PGYJkpSoILRmWMhAnmIgeWAC3haCq9sBlWgmAD6a_FiqHIBXHEHm-n_n1OT8YRzgLAXF3KiF5516m344ehut4w4ywxUX016LuJoqcG4Mw4hY4i0-8qUNJZLH2qQ334WvTA2xSSX16-I9qU5J97jVkTnqsxSfpb4d1JB7Li5FnUi5yp0N_aVSMLKkCf0_h8GnA-FaJAOgCElcvlVwYEuApPpKIR-doSAmPCjisF2FP0vxkd43TyAcGP_MIpxlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0P2SDPYLWR97tu5Ru6UcWdfyOeGUq34cVUqc7bnmA67jqXyi_E57jn7KiooFC3nNvy0dZ_4mBWspjsn9_Aag4-xHN8RTg__KMHL3xOzwr_EHtw35E2szEEiIKLg7gEcfNhwGvcJzmxZUPHu89MSFZrVgDU1dbaWGTjvblFRpx-C5vbisvSrEDny3FBx28K2nArs1sXZ1o9tHnA7o9xfotzo8I52HNBBw_Mn0znaPNL8tP9HHR0jcnZFKcV34rr4DWXzGO_kCsXq5F6YmqmMXQfwn-oFq-rwes9CMLHGXTQtfH7AbGcpf5Sorny88kHWOy8-AgoJoG1XUKQGyGNaEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0_4j3POrJrN1W4HGYhoILwjz6U3nLiJ6O1LOc_ilYzLTk5Pf1GafZR6u1k2ZJdcgfx0uDOy894sbTj-MJk5kvrpRmZtTa_2C5kht1de9JsgEun4rwppZQpsj2ntFOD05kfL7wvtBpm3jMG8Y2SvL_Sh-W3dMipmDcOmYc2C2RoCUp--PVvFP2-oj2n99BL9Yyj_gN-BnA80r57R3PIk2dmg272ysMB8LDVmMLfRxOflMo9sfSQuW96FD4v4KnhGic2nfaR23twK3mX6C-QxrD6Km7-W8lqARjFll7P1LuC0jubYAsKpr3AwC8JtYLW55u_bVJhqvFqwn0dY2dZe8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGDafyQVolHxj95hGBkk2zRDqka0mw_zDbcVucIriQ4HfAStO6iwlvCxhyIPCOl-qnFvfADq1lrchsy5Z2cknCJ0RW6QAizNAXPtq_CNuuaM0FFZOFObknIaP0QuXt8ghmAG9DrAJxuI2550A0ZTUQ8zXF1A3S1zcNCFI9G_iEWRvkeKwGOumVkEZv5eLlrnQwbibSK45dx_BM0_cmkUTo2OBNOQLj8caTvu4QXk4hrhjwuQgW1xxTf398z1JWluyDv2TpMqjvVTgM1IVY31k5Q4Z9gtjhv2prH5xqWGNrRgYV1PQOxjPU1obTzSiji2vltB4S92l4DhXwMQQePDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_-gWsGRIJYpTYK6d7yo9CboQLSsD85w8xpZ6t3gQZJQwP0qsmFaMmXMplUrhwmbZTmnTbaKRHjSHPxyeXQ2W_m3lvuH-HPD9PElnWUDXQflbj2yoDqp9irCQQuK3UGibqmyfjwVyQX33rWYk3UgIxpGYN6wp-j-oW6lkOuaSPdFQlC4amXlf028VxtZz17hcsJu0gh9oufJqQuwNBRYb_TVLB_sCn__uKFB16vakuKvjX4E3SnmAKV9KN4UXfT-6NCbJK02cycFFeApp8lBOti-myW2t7-LWT2G94q83QssB1Yz3OMAm8V5rlcxu7t2pApHo8scrkgNoJlXWfp9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم
؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ توجیهی برای اون کار ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25288" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7aYmwxyi3th_notqFj5jwoxPIUJeZCBml7JPPwPRBq8hB5hocegcfKnQU9wW1G24euu0XRp0DCgOIiZ9SqyanYcVkTtLK7fd8IoBg-98m4qgPAhLasqC1855JDURkOaY8amycOgYzbsipaP-sIDd2foeaDlwXcLVbFgDJFu538ZCGcz0gXDgTxDkJDRu3hioXQsu116MznlP_JOqWRnixtDrEduA4BKrbV5VdD2VRGXnSuH_XMAeuFYiNxntwAAMRgIMqoQmsM4lR4ScT8quJBr7-i6xuBNi0tvHHigjZ_sfJp0d6653rAIdzZArS7dCoDVqOlio8P_YLH9JFa7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmOAUDv7nGVaYK-wXbPlqk8ob2VLLzz7AKzRavE1tM_EMfoilnefPGTvkKFsXoqqaA_S9sEHSa9M5ih_5MHEmAxruRaoeXzx1nnysTDVjyKaKjpphNv7IlugrCu0N2Ll5sgijqSc0GH9qSRbf3rTGphtkWUbpsUkXS_Jk9__xWwvndEoibHssfk7efxyUDvhuy5HN6RBE7QETfNqk5OY2iHTqtt-7cnB4eRIywKbo_0vDnmKCe2TP7NNx21_AAo-PDTOAh87a_E0_taBUpSh5_aAIiNYZ_GPQ-X7w0BmcNCdZxqDDLQcPN-gKT2AmOOOoddS5V1eMfxG7WWnLhF0yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXGhWJrF4vjM6n0spvxlUJhtTUGmnw24RBbsCb7NWqUQGgvslGvu7oTqoxhBE7qm75XKWrRzkcjJGO082mMau_7loYZF76tNfuq1Wz68mIWKBWmvHDmI6uBDgZrHtScICiQPIBCk6-ccexKjnl1NrGK-JC3SVewxYtojAlaNQuA5sDE-5qzG2ipMsCF24tFRDWVzMrFEBTJ5L6l8fBmC5y5ythQJAC_IxymR9GKZkngoM45bQq8LRPMtgLPd4Sb-2e5aBkrYqZR8uAG8oS5oLZmkHSOr3IZdr4Eoa80ecfTFMKUKhvCf1Yuu_oBLhSjtC7Xl7fBFpSCXF3GtERJlng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9htQ7z8SfWWXuvheCjdR0t8zvDxSwRmtysQhlEMSt6Anj_6ioEwRMxDyyg9O7sjXARxhucS0jooIZyWhUfygPN6dnqa0pzks1of9ROOcUxcAnYvDPLCAbbk9Hh25xxCde2Ub__PAJc14rXg4dFBJhO-uESa_0HPR9WGEQQCiVy4ViAv0hYdPlLuVayrdL40i8jKgNwl51Z21fPqUTU-832IpCK-4svnDQypG6TxxN8Fa3MBd9PFznTHx0S4YPEBqwZa-P8KBBSTkqFHq41ZmBJjXjSjUc65u693SYxYwuFVDWs9Z5SLSpf_a0npLS2IOBqG9bTIrnBoIJfNEu7RRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
