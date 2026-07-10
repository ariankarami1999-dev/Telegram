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
<img src="https://cdn4.telesco.pe/file/CiZGMBNWMltb52ip6FFVQ_MdPlrw446EJCS2fInK8He-cmh35qVVrv5qRFzT8dRUXgf4nxKz5EcQJ942ev-oQpn3Qd67Z9o__p7n5FUUHZ0J50uXGBiufluMo-bYUE1v1Y2DSghfpZIVXEiEU7reW0ukZzq09n34joeapxxJthATJPyvJ235-Wtia9gtDbFLgJhhnRBqsSygkCCFfExnmUtko5yh6YUtffsTQKQeB_UD34qlP_3qG-365qp924abFFBfp0xKrzcweyHx1Od-TEyVY8jDvdbVaVzKME6G4aFrjOkGj23KYzm_hfvWCbNXfSs154KaG3t7d7MC9PGnpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 22:25:00</div>
<hr>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzTfmTIhSPNQ0sAQ9yGrDQeuGWTsd_6X1AjF-2xNLYr2MZvTviMUmsvL9CwQfWHj4_0Y-7YLHz6kNvy4PXM6ovQPIUpM5YkF0Ck5LX0bCXFKxj9bMT-smEgIxo-eX3MIqvI-ubg-LIAqbgj2jU3fTQU3kdzXQErQQRzg8_RFBoFffn-oaAXaBBFh_OczACg5hjwnZqqOLk51nbXKb-_z5pW6jGff96szsEI8-4jAkJ0FDBIIatWdoCmTlFOV0ZZYaHhp1LOZpuybs6PvZPNQQYJTjeHrkpXrQQtx1X2yXu19OJZeEY3uLAneR-HMqh3owNx4Nhr3nBg4SXRecEm8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSBuxVQfUESnZCcy-WgBVwSbtrhUAJtL8vjwWkGV5KGKCGNdgvlgYJ-YZMcl3f8yVoGZklPXpG_ATQzKXFTlLfwmqLoMKb7qsZANOh11KTXhVz969B0ZzdbEkirb7Ia0zJRK7z0UVf5Qfk_jJGH9k8oZ9bxjZjRTtfhaWI1b3U5n3lkvVJbICv_FbW3yy2JkRiHVQDf3YORUFzVMz8w7zUKMc58JcxbVXBoh2iBeF6xijCuqPQ3WJ2CxzeYQWXDv-BekEs_Da6sDbTorSDsiJaMGI9p5vkINoFW-eV1GMbz4MT2FxMiDPei3Nq4i5vpR5PLxAFH4gGShlJN-O3PSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufft5Q8ZM8-GqqCcqtsclwukPbgzEesMhMAwD0YXLgsomgHN2qVtr5W_5L_EHsYQtGKKw-kTi8dHS-ofY5aPerbI0QAKh6g7FIRGAk_gGEtfjiy28Je40OtE9tedx7zT69mOPfsJWpYcdqqeJNFPOPrvSksv9jydNxrhk9Y54ybFjbhMZp3FsbCRStEm8Ln9tudwzUpYFe6ytRIMlu1DllperYuv9nB25ozf6HkR4Yqu9t8h8zRlSCPzEMIzAtt0Ewe8EQJzZ8UgHWLgjeUtQMweNO848NpXl0EX2E-1ZTIz3JBgzSoAPPN-lir88mTdDGc8ReyqeJrlMOqvGFxXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wdc2ezdGqWi7n7oEkAEdSAZBV6AQTDA9TgedvmSm15HEfNcsn3gI1GGLQSegBxaQJDzrhgLj-hr9Hlz3heEPfSevQx6A5fF-6Sh1PKc04TyiCIA48d5aoDsgHKmRK-FpzGg_eveHk1zEfr9Ii6mmirQfXUNLkdP-yX1vdZ87RJ3rL1RZD5wOP_YPFxsMf7qbu0OkRqVnw7KikG92WTlsNAzcSvLzl5PWRLXfIi7tmtjlV15lZz9YCHBN66d6smuverSgd5BXp0HjLfCJGB92DarY3fiHv3oJwdn0eGNv-NRa0v13jCKUcKTJ0ItaIR_mg8Siql8D8FTLTLAhtUhJHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXs5wpbelqvY1XLYbT9s4qv2eXF5GLrcAKx7ez4mco9qSKApLX8WwG3oaXLE7xYOfE7E_ABin-O62wYgb1setgDXsS5oUGT2_Zg2LpcgqAiOQGzw3VBM_jug_JI0dzaT9JEuUBi9iOD6BC9zplr2ZGfd8VuuokA1ndwW5kNiXZXAXKPNlH_W3M72Rng-Vdc6NIMS_3xd_m5dDBdCYE0yJPmPp7qwqAIdj83BEKTNVwVvFzyLaoWwN2bPKOoUjB5dwq7w1MAuxcE-4SdTMLetg30GVm2dGOo_OrzNT2tRvIDVRhy_xX7hnnh_SbPEFR-y2GSOdsQOqmRNP2X9GlPvnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSwMMCIuimTg1ol21sHNlt3A0QyHDj7Fg1gbhNbLg1SWWMsZXu8OnZ7KF_Cy7PZUW_uvAo6CyDjpQRO_KKq1NgW1wGJE90KoIOzDDbA_TUCXTp_IzG6FUkzXnxQBix9Fl7q_Cs1aKRRfAWhFYgW-uEkow6ikX-G6TZYwwR6GhM29yg5KWkNIyMkwtBtHKG5ilM_Ivp9eUnpLK9o0JrwJU7AbFjK3rQ6gtvpOxM6Xj0K3iEJWu2QjbDR1cL9NgdC29pkgceCmwJbF5hynEmXU0vfgZwEmzUMYV0l-1xRSCEFljkJvFGMOEGiP3O_mR4wpOLKS8q7j5cyNvRZN5hOZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq87cDYCKd9X6GuLMOj8RjKRTeQsnkJOq65mGFmE0cQZVl81OvXbNLHgaJGTycQFglDhYr09nS-rfGgK-k_2w-zxk9XP0Df-ndnSAErjoANCevc5jz8pilZWaBCx9BYx62M2esz1KKeNixVdYS75F7sS9r_pUWrj7ldC4ERhcoUgfiN0WmiC4Qbbe3uf9l2f3GYMX3UJyeKTzKhm87WurSqKdPFQsGKGogibFUSE1AKFPu5Wj08fh7g20KMi-_kFK2v6fNtglZGiyy31qFqT2nuh6fsdWbokIAC50Hd6ptdsXYBByLj5e2R1zzkfryZNjAt3YOyTWryV3XfP8V5LmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4JzR3x1OuS2UNjxfLJ9q_yerNAyK3BwaH7fzUbNf_lM2XUPcRVjJdH_kiLqfAG_hC0G9IBQPadiUDmt_MRWtSoR_Vkc82VJgD_penHThRJTGiCPLnhdZFcxqXmUjcaspn6yappATPzLqH70xNEOPgWXpQbdgcqYW2MnZGIvRs_ORaU5qOrEKPgdHvcWIV3wrGHeN5dT_c-G6CdWtNcxpsBxycnJtvvPLl8lnHxo0mm0vun0ohavmZa2vxUxkYahwRpPR6-RIu7J2JlqFarPBWjiNSxxAdF_h84rVco_5h_p7dbsjO7TMaCqXfn59zh6liqKKRj7BS6EL7yRhpxFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYVXS4fMFz1AFX5QM1qn7LNjVoZDQdqj_kiatFo-fGQWM285A4oCUJNdI2xBurXQ5QmA8nNxb86CQp6ljWJdy-BTPvrT7pVgLFAipfmKoIUs9-6dYJsNBzYxIlLcZJNyxF09N6ZYjLLeHCrK4T58wAy2NzDeEsOpMs2kX7PqvxiiPxMJUcJS_Apa3ZNSUcRnHHldR8kKtiLiCNYn8pGK1AKj2CT9jWxWIfpFphIGeNZUDy3fMnWcdK5H6zBKRIJq2BzlRHok9r9ageGaQnrn0beV2djEaSdcdxPj4P8dgKr1iLYsejzA2jDVqGxp6M7o-8cj9O75pV3Jpyd7ggQYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tU7USQhs9DgwAR1gvU5AmJovxxNaXORFlP-mLPs9xRkqz1gY8OycTTcwMC2ZdBOFgbTMlWxEsBt_-Oexp9FQChndH7syRrKEJGQ9YAS5jv2Oupg-_sy3DlRg51OovME2G0rPsbgYYYwTA2wCJX9Yp97rqEM68L4k1DSQ5KAaVWw3NFEE7T3Pmw_PQXXlIrCQNloH3DHkFt_hgKlb2nnFrKMPy-uA56wH_Ahz3bNSCpsKiF461zCnwEIeETXRZz9_nWzRIaM8RA5qbAtz5MQ1IZdy9u2nqLjSqXtkKpxR-ZrL4qcRzSNTyLXgWT1t5z3hOP2lyl95A-fifRCIdRWMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/25377" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5bqdA_Js9YTEeCN38IaVkLLh0ajfhD6dCgdtTbEazchLckXfnkFxgiiO7eKbJxA6zUuJju8HQ3vSBImjZrAtXjW1Gp1bih2-nYKGz8j3dmPprfxHg6_YlbH_weZqnpW2PnPxM-gJwgjKYEo_Trr5vcaBDODgJiTGFdTYLI2a0R5kMETmPW_ET7I4iaHvSyjZNT8VD50hFP1203FgqoCnFgbL-5Cj59XzVqzmqLSRlavu11vVcYIyM9-lQQly3SFH-KrrUvakpfXqG2p4wMidp0xVp-j142Oi2Ua9_P1lpeWibkCMfSPLq--v__8iJdQ_BVZnfWJqf82phhNQ5Xa5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnfxXkoLGZ_1viGHlgDt7hrRPqm6a_o2lwWWMxw8b_WiwTMWWMNdfxifM_jWF2MJs5DnCFLZUyZt7br4_0aJ8zBaDK6jFI4dzicI0M__yctoisb8uW5MqCL32Uec9oE0JGUDJMs4ltjzvFcWADo45AhmZCwVRlwnyGjUmpVCDXIOvUbSatojkdZzeo-tzQhTbqAYkwKqq64J6DF7wqVWcYd7esrY-hEkfcsVXtwIXn-FkDpxHO2eXH_B4Z4b7oqyIKrguXGjy8vPGk-hxZm2p2BVpSMjV3YDCPZDDD60IYha2eb_s0udIzyW3FWNBe3juoNMSBlY0I50xu48fp_mQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5DXgNDqSkA_utCkV2wHaeg4GTzYlnyynSAmYh2gevMQhxgHwXPHIOv0R-IArE1Yl9MMiMehM_6An95jE2OYvySpx3478HyEZqDHrDAoNwQFRIJOfADC9F_XjJR6XXNTcBs2EiR2P0c2jkPuFXT7gRZF1JIYECdwQ3ruHyoBrjNxmL5Zs2EP3ff-g-V_DPvPg3Ec5My2FrOCbrraLsE3ZAyvDp3By2BYzEMq9zLaCFL4qxfvfiXAmM6ePcgd42XzqtwsNQERu4tdcPZOXr_-3pCljKtg4maCv_dI2Qgz-kK_c8Sq3SuDAORXjdT5AnRNQUohJevLvP3pTt28aEvAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI6CI1n5HzvC6VMzUvkWoK7v9GtM3m9XZ1oZNlYu39v387CMOYYGJsIUjWz69T3E3b7ErlyLhrBveqHimYmV6qEQ0mosBRkF3-tnxo6WY61nBU1vWswRdACKAIzcI9RUz3v18o73R-Oi3xq-da3D-5QPmcfYzHJwpu4et8RDysrjDvXWmqVRH3eC833MMjQTh2ZND7jamAReu10bCdGbnoZSSLRMsTq2OX1yL704EaOpkVV1XndYAcJMHC0VpQ7otu4MFyowA7zK-1DbdizzS-sXyRSNpsYmQUElBhtyi_ZBPMtCpOf905PeMbPF7jsF29VKw4mJqYzZ64POMf97qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXwN6hgWZFhSTWPN20AzxPkvNGG3kzxZRyQQIdbnz8Dd2RtkRTstFw4gKFAOuWOwQf3JGCERoV02wvCx7ImH6nCL-rB9b6CfyhHAPqT4NNMOkWWOHGX3t1dYRqaoQ2MLzBEUqdBBwwocY4M_sxUk3BufZ-f0QV-Y9VXQT-pgqJgfs2EEIk5yk0YEZlP2cehapjEVM7iToYr1o2V_dG-vhHPT5_R01BX4h0ssT7oFO9x3IoctzUPc2PD5vF4y9PN8GKm8KBgdg4AGx6t4ghShA4FPAMo0fPIibwwxkpk9t5Up5xZ4au6XEQBHblJYsV0EJx1whnCz1tz1enP9e_GiRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9gj53_q5yyry9-fN3nN0ico5zvDajE4eIKxfAMX9l-B02YZm1-2Lzz_d-fbysdAEAtT1ZoKWidqCAR71t-wVtcYXeXtQfbdqIg-UY5aAi0eiud8TfWZ738v3-rbNmup95J-1Fe6JgPA8l9CrKBtG1RGlVk2Lx-yUf9cZRMjzIyDX4iAOmW84CHx8ZIXSH_7BDj6PWGAUa7X_WcStPLOG92QZRGh1qri_Z1hAmDFYRVWi8t4FgXBKsxv2FgOlf6VWG2MFXUm0C6C_qJMCczbbZZdwZX0lsLs4x6xuiUZRsx31AEw1Kv6ZONmHpLx7F_U7LNiW19UM6mPULFVePbluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHHRdTIFgR71E9FumqwYrqK55ctAUq3QZxqYYKB_0AX7hwL6BaPY_dNiLigMaTx9SmTngIC_-rpEO1GY9as9KbU2HGKna93vSRiyq70TrXN1vYmQ0kjgrXeJc3qnH-i8P2pgJ8I4btnDmwD5Ta3xkyuk7ItzxT08XrSaABaMEGIQv9cvqQHrS9LL5kibMHg83A8GEZg7vgcgVcKvAkLywH__4OuJonqZqTGdDZiHEcdKbh15u6Y3euC0X_BGFIeYG-VU7DlwFAOIanaHMH3PyDb_5xEI4x8nBMrVr3QnYHhpI_xVrlX8BxnWBK9n_y1FUhr4ktzbaAhsUp7TsPBJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqpBT0rwS8c8zYrJfRD0RetmB1LQBjIA3_7ZosRw5ZB-kHqoWFnbVhp2FMo7VYWC9gQIWb1xWXeIl46a1Kc-5NbD9_ne_RGVso2y6ImLNXxNLpirP0QPjrm12LC9gbv97Pwik66GMpUnNaHMPvmB_TV0bJ_jQO2O_gl2MmDibpieoq_0opyBW4-MFCCqF4HoFpfXD9S2TL3Bz5jt2Ih_iVaZyA_4Xw1Vu8GfQxJ7g1momgK4oti4563ElAl-bwQ4VqWHl8cxzXbK_CBb0cgQvnussE6einqkQj0ewr6dkRpvbfXUWqML-eHlwa7aw0oDX2hX_xcFYe5W3FdDnF-yVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVYl2LQl9KmD63vP5ikxA2_cauwvK-o-L1zyUBJ4409QJ9E32_2LexFOdjsY6SnTGXo24Ssm6mUdRF9oQ56ikePyVFIRziY0HpPb5DJvGY10bEXCFTC0E9udRzG6-dr_zntyy9RQGtzRgmtOklY3h3CWdkltpXj1iYe02Re8_Cj_H7A_EYBY7eqgDxkYyFh3j-Pb39vcrFLvMnwm7RxnliF7nfRGvKGhYTFTU56X_WCzhvIHjz2LBlJCBv0AzNVz64zBVoIn2indbqrXhpNJu_1-A1lpYXJSE61RfFgNWxmuoYHdBW9cBoOVqow7jPhQ6eayeWnIQH5LFPlk8b4qXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdCvWLbE1sf7jeIynz_YbPUCd7dj0UwAlCk09pHPw1KlzApYWsQRPuHHwVUEuBuIVg0BVByKwVIezhXPMYpA7vOVRmq00MDST-1FO7dUp9nqKkJwzFV_ctLUnVVugBk5GFJGWh1oX85dboZplUZt90TCCWMeeGQ9StgBl8TAGr2j9kMnv2rf8tsiTJsUAxUMUkEGF73tvplia3CwKDkEQFaEkaQfy1v9ZyV3AU6zFBf0FIEbvYc0IIXe5ATrxTq_r3DmV7kgiLXLTHwC5UnVKvZYwX2W4-RTJ6ixwHPc3XsrVX_3WYvASuZxbjUiuLtls-EqYXL7iZ-S0RS9MaS4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnRXMh42vrZyUHVzHslSQvW-gTrbf6eg41Sq1CHUVa-ydnSSwnvlDU2qxkkroNLI5NUE2nWnDMrLoq6G9Ar4YlHLZBbkFAOtWP27Fv09_RdzNOPgoTG2LsC-mg2QAhb53SIPqyaFv2zklxr4-hgZvAX_ku-75KULH8fietMDur9F26lM9DB9HyFHQXNckqnfYeCmKwA8YrqdOt9HWdhwreNckwOr_LkKfMTypAL_RBLmYVwooRh4zR9-OA3Z-vKNSUXWUnk4BJmXha1i7kE-4cHKM_rPWFK75uC99SsEZcaV5zfeTfBETagMzMAwpABiXJb9qWHB9-9KTk3LX3TPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25364">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/25364" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyac7wdtxgSqdIJfKg-LKNc7ujL18hyotwA09FsXxSpPOBZgHBMubF2zfyXtujlQqY8VnEhrSPDXZqIkQJ9LODf4qLdqERGUszSqgEXoLCREkBs9oOE_gG5thbEEabxPlSoOhxEklwlfJnJX0IDVPNuKwGYyIuHrtcBcWvKJBL0rJbsgv-bYLW0am8MtoNwIoWioeKgFcy7soaNZZXectdO2XDm5keglenJ9J12-88KNpItrcuFjE4tDHUyhFlYTTZJgfCqOvnW-Nug2nIGOrl_RLYSYxEN5ZBTwpwuO_xDaCKi_xgjFwxlt8QELx6SiMml6BKK78FFZOc6dwq-zcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOYlYQe3Fi-nnanAJ_ILW1Ppzuck6EsSijKiWdtrihWtD-cLMZhw3CTomn1UHQQdrXruDYLM3-qI8MEq61rDhQu4pXvtOyu6Ohf-YyEukamvEEzjKybQsTu18KJ3DZVUz5dTyZEx5l657OZRYMYStesCsqIER0jzjkxZwACAk80HyNWt_ikRD-6GY9hx3IWtCggiUkTG9n7Tq3A04d4gNnuNPOQmcpZITc3VW2ci9qL1RbW4gpsaELnsvxoY0oCE9xMzMyNZ0HK73nzooDLVZyy_qw1-PlqTx-7RwMuhL3z4nJQTOKsNgwdEPY_KUbP6IoNbYZTyVVqBzigy69U2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoJdVkL4N_pQZiD5-0iEzfN5PbXcPgpHwL9heEZ1jTWKZSzbwcpek2iJaxikk9PMvY8GLvo9Z47jufuzajo6YgRxMv2aFRMZM9VDz1Vny-l-6bUPWPzIwolPihvogggGDirwK54X8XLi3tJbV009AIbHMjABBPcw9Xq80f3OmMtn56JyMC0pe1bNT8zn1r0rHNcw-okl8ASkDu0YiRl4lJyelcF9jLl9fteojx_O7VY6CFSOR11j6jgUi80KoPjsAyjVpYlTYop5M7jt4ZnVzfHoMNicCVFz6iq_k-cVj4FuOeZXC7thunNEX4wp5jFToIonF4N7L8uH-UK1xZnAUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvHZMwfch__FsbEgWkwyBp6qQhjrTfM19qXjyi7WP5vWSRNGIwg8CzzAKnAD21uXvYWNZ7bxM4MgsGk5korERWLra_y4fq27wZ-rXWJ3T628igTTiYa0Nwj0qrHjPmdsEGGC704olNgKhTi0lZmKtpv_y0KwdsJW217TP8u1RtdVr6P3R8EFcv_HVyRGzCD4j27PET3ecuat9t8EsD1B7AJFMbyoFSlWVIXCgwarmK7ptOpy7c6tGgeRQekBAbj7m4BycctAuAD64YDhRReKwqnzVHi1iXXrIp_zrp86kzpb3uXVy8ehLtEzGkxv9iOWNiKcD6yJ8mExOz0QNj2UIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmXc3fSJ5HzibhyMdfO8AcExRHhTcCnaT4xcpCX8r87jKyKEjvHouYfpM-ZHtFX3ZRb8vmI42LapsmxdvTmVDBjBl0_VnmW_xoSja9zVSH4sm62PP8vNisXEqCcUVmWuymTt9lLkHc0yj5O2oKJnj3ghwolBPmLOJtaU_WL8PN_t_XeqtLN8QhVTmtGGXIioaLZO4JC6YeC-X3Wi9fBebOEbttWnokYo0R00FbCRp1jySUl1H2x8LhKuGJbdXl71yrDQ9e1KUw29FCnzXrvVAd-QTwkIRc2MlhShRFUXNYnLdSGlZqmwO1xP3eNDw14bLjVOcucLVEOYhgO3U-nPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kytG5rts5hbg0b6v_4LBbdMNOSlQUfirVHHMFmV4nNZgbNXM4J5qEOqukEAdIwmr0LOTxOuNax5TfISdqg4VojSgQ7t3DB_d_1tfq9aHv1xImhAhXqeaGxz4XjwJW6O-oG2UkMCtSyFpJvkTRl7pxAKORYRWrb2ShRV_ixIu7K8PypXgoxoDdduqFzDjcXwOcKAmMcrdZc4cyHrvB8137c3aWT1XsroKSuAWvLZfbpjOfj6vMBZyXYnSYMM_CHyoIvSuDvg-sjKuXLJ2DAL9LAUe4uQTvtq1X7TiCYW1racXgbH20BIpIGM0eSA1PK_KsXGiB3zF82ou0NLSv44UvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_fx38XxveDImqpGJc6tm4BA-It9NTKGHmph5hobtztTMbvkLMpF9Vt5gVbHyvPoQDRseYC9seNb0khjB0nvZtv4ImYOFh1d0ZMbAGMP6tD5gBbrhw3R67jCsHHWKDTThAWzWzFrP8VDEAn3-w5VFpn8zCw26-fe8ld2x59DDvOAzE0M7juANU4rX3N-j-HcQjzrhPS9weu8f3MPhRT8iU0L9L1DDc2tggatfs-JclntKIwurWTnArvKpfWqIISeZlV5cCJp18LyKe2UkRQFOZ9_Fep9VpPnbl3eln2Sui8D0gXbbtAtdtAR1XSdVLXApL1E1SxpfedWtqTjkdwBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beQvD16DCERY19m7rVqIfaZKBD_LJEnhdMz6p_TP_5zoEOLtrE_EJ03hADWfZX-OHGSVsMyoyegjqoewb0tAPBLhJ2L812s8giMFSw9GhomZqd-b5tX1_gyob523Dl9JfEI5YW4knKF90ujHZ6AT7xeGHPmhp6JXjDEoaUS9Zcdq8E-g6q5GqsDBnHYz4pVOGQ-CYyqpM7YRmUMhOWw3hTKEOAzcL0PVQzyJOChXlzk4KaQIWhWFj6B1DNtey_lWX7o_AS9OwWMLtwkHKLK68KrmMmkoPoplYVONL00YLyGh-uIKuuyfk6nkpmadamg9KiYBdHU9JNifruTG8iKT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKFKpbsA_IN0LFjaaEVCPB7vQOSR9bUeGGWcGok6BD_u7ENKcCeSngB76VbkyumFOygG40Ej_jIzvh164JgKYU7GeBf-HJDHkfCxdNT0tQn0pmpq4e_WVMS8u59f0nTZ_eHX8YN8QoW7zOB3CddYk8iNrMWRe8eOSWzmP2wgRO2ADdiVospuh9C-Uh87eKCmvqeMxrINo8hFa6K7Ung8ypA_r0SBxr8rsoe841I69-epp0TrMdcj_jKMJqYoc5XimCr0uVVXlh9y-Kk2EzAzsVpTEU5nu-Z6o6Gcf6SSfFzDUjC7WtiStnORdqu3Asg_J4V1gE2MkKBuoE5lSJdkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn_M0e9tLzQL4uUjpJ73QuLQIfY0Lr6exZqUVSdZ5Sm5LJUT7kjHB8HQcTnW3BwJoTFyYGo9ZzspcBnsK4RtxZSQQJYXN_8sW1kVHSgp3QBsIqcq73H_ywQbT0knz0tUfZcMYu4vvzVZepaR1VgNlG9D3ynIgBl3S9Frhszsxlwmsh8aMuddi2ryI6trHRV-riW4oppvFmvKf-K1wK43eX4dPFD4ByaI1DcJruXGtYpvEW3CM1tV1lSxJyJYec3TpysBCcp5g2Gpch7OJDcmDEWRXTs5aswidFUwJrDmHZ5mJlu_vLcjTL4NeveDeszFWWtngcXZ8lmUlqCbMSYdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFgu5ySNrzV7xgbDw-5GU_WTdbcX9Kjkq_3z2lcXOsnuk7o1MqqiSc19Tf4P1uX1Xflu8IbGGTDBeXjY1-cOiyT8lyd9nHoNLN_exGBl9Hq8FwSMR1LjIRJz8d_sJNfbvW-llMPX61SDxkxdYKH7TobrqbdEwhLTIVEJjT9BaWIKU_pDdFu8U_nJG1nTyPvhWwa-BoTWljYzG-tQ_QhSHdor4-LJMepxfDcwZOfK7VYJUE6gyzvVS-BYH6dI2oU8xYClkzwDJ1TD46y1E1_5tOwuIVLoa4qurezMPR-bCdscF8En0VIiT5mW1XD2wyga5CQetDRRqmHoJqbUJI_9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfIgal7SZBRYhFVBMcZHijbVMgIVKmYCNn0a8OuLKR12uiQA7GeppEyTAbMYpVCnOa4WVOfUAMKnEqUrLLjt3TnKA23Kwspbl4OjNdIRVBvGnuzVnghKmIx6vhIUF8PC41e975BVe6o0NPRdaqeuBuTRllIOYKlS6Pwx-wENafJ3k9BuiX3-Buq0p6Mcc-FVihPAZJmlgOW06TvGmKD9mFMfS115h08dbDfq2wBFcLjR3yocAqnaithRHAZ2toP7-KfOOYkMS7QNPLiktXWo6BF12rZzsQXjFT3xoQm5GQ-9LE02KNHeCLTwNPmUj_qx_Drd7uz1W6kHMRBOVxH7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PytKNZa9oUQkq3Tl5tnCAVtFhstylql8LZbUgkG5vREaHK75kOCIMMmtVLJBEd5aT8ATFYPqeEQ0oGN0u_GStXeTHpi1izFmRrKwQS9UHV7q4yBfMrqqcVQyB6WKe-RnUCRXrhAyw865NfNl_xbmSlcHWgQUEKi2rptfCB01uXLosgwIwqgIdX4GuCWi_zuJxAi1WVEWoxVFuvSR7_cDbyMe6m6o6xuoTftVkbas--IH3-UJU8Q0phXTTotZ7apJlaDaCxYRkJP4qJUfOw4dKBPzKdoqezfIwAbPHoKW6g8ZfEsBwy_S6IxdRfAbh9CGyV_inVJa7Zgcmau03BzCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2z39nOqoMH6LXWjQejrpXqplNjVKyrMcPw771JepXS40CNwaUHVdrqpYRg8aIsumRdZ8zprhJXCkEl9pTVkJHuqyN5urVfufjULp2fB3VhIQuA18TMbgPc8erZ9Ew0G-MR-RVi9ANvHZoitnYzchhM-d7G6d7TXKBzaqhFZauIZInw01vGd6gcSBNYV08UKJqfjykk24f2B7B94CMTAsyWTsZG9lOF169Q5wimJzNul9s2avebBQC_joHNTYc694BWzv88RKWoD6lh_jqOvVo1Av8_3edLu0cHy7uh86qk3A_EixrO6BxCOEJ49nLFYzlWigwzr1wO-02tNozHR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvdz3yYdVJ5mtxw3K_ZLQYoHrl3JomvS8UN3_jJdSUVxeGtEmqAMatOlRSAqzlGvvSj2yl6lsIVgY7RbHktoEfeUab47zsXj_8NeBY_YNoDw_xqQKjoYFNSqadaMy2lANL_hbNg-6uZgdNdm9N3C2AWldCvKgEQlckieM79feEyBBiyqjfwvC4dLSyPGFTusLEN6RyNd52WvSDZ5pkHs_t2qfpBg9jvOBF8ATZWikjhJd6paftYHUE07aFeIJnO0AjdlLdd0D7wYp8HiRTR6TsOIy2X5BO-xAPZfX1FDJhvkhAcVar0RIuSEVTjP9Dt9MwNxMUFQSpngHGdrszU7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn7AyxTbQRKEAzPsRACuhGE1Xs_aAgRGWeaCMD_frJ0Fac6DcXCyLK9Qf_qrMm1q_mbtlByziF7Pwn6d8XFXpz9d1JCO8ayhUQSozdgXva_R1Qy7zrDuZku_xx9fUXKrDRa3XhfmOaF--J61aJU7e3JShPqrktrXWwK-M9f7V1lQu9dHDOoxHFWQ-xN5dq6Wtq7YccY-uEB93omb0BZz-y5xJxPePaUPPZ9wBOvBC1BOfaCf9qOHB_X6KYVzB-P87IyB0dgfSR9PO7pwBuLSeg9Kz-5sIKNdznGGyVSndJlpMtqJFTc-zJ2wBiFE64hq1L9WLrxrABx540Eonv6_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHvW0wIn1mNlQRYomf5IYUCc7vts-6Rzxlgf4DtfLFOl5G_Izmecm4FtppcwmLZqL2Y2rVQUD2SfqezSLpVu7Wvr8J1D2D5q75og45Wlpd2FCZjBOl35vd5sBeKZ97HE3Rs3O8He5BVZXQHxwfN78GK5Ipgk1sgngaqxvykK__RADfja390BF_PUBhO3yL9DG_UPL9Up6Gz9Dwj-oYnr8Yg8XSs_hvZ6cWGH3M1K3fV5kFdf25IKZed0dzdkzBykelfT3tYPHxax6rwse8OZWWukDh84QXuBgu6Q5GH0IxQLIikLUjMV6wN2_Tx4NJiBDcLODkxDZJHwI1d_euMwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25337">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25337" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwwJc9b_6zb3m3M8fuDr36f1phli7VTt5WVJMSsZP4UDFtLCs7MznYA2UdHcmvqu0-AmBLla2jpmUbQva87NrXndZr6qhmQ_Shq8WBN4Y7BfIVYIzzEZpf-HA7ieTFJ2hYsfstcwoWXU6ewFuxFn3lzVk26OruHYtZNW6DlOn0o475bJGs6-dq3JPWyezF-3PajUYH-4cisg3Koq3guYX9je3TlNI5LAn4G9h70orZccja0drR28Fpiqrjgc40ymMwz6khDKUQIPkp9Z1YXT6XfhNRUyoTRzbWFYbBloypoUO3a52U2ekp5QkpzoAtBtC-qw9uNACNDDoZ41vv7n5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ2h4RK-mKmxSIOR4OD85ISDs8uh0NC1T47tfFOfSVDWYj4dsN3Szje08tbvlram2P7jTCsaratDNLvufYX2t07OsQpmv4LpozlsoFaDbiWEkBS-m5dM94ZyA4q1S-XGEYVA27-MOfa9zBVK7FgBcuZXhEVNc_dGRmfJ_C5g6JqlmlCBMOJV1pAHaj0T4pITnk2MkSiNgPFr8IpCG3PahfwqCcppGHGRfM_Hi0I-Tw93HIPKyQmEswrEr9Z_l9yqD9ObsdYDQeAgjhxMgqByZa5PhAuTvfjlke2HfRtKXXT_p26WCFl8YcTkwAt8AzZQDwyRsaxs9KSOZ08-CAqR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOtlBNokXMmEvwziUdmkADdVU_GPaNxC_a_n2y1X6ZpqqtZM2aY3T8aw3Ng0v3mAOMBxAGE9tHmquOo4JxSZgebYZRXqlQRmiLaU2zcHORtNM8KFebZLlcQUVm8JYMesf41GGm2xS3UQnB2Exn0DYQsdc8uDQ_tT-kKlvw_V9vv45vJ8D-8-BP3O5Hjqulttcb1hs8sX3DYqjxYOjrC0Np2tQ770SbW4D4Hk82GVBx5vMCoRQeF3yqkOEa_hmuhPsFzTO6B8FOvTGxEm9V89FtM-2eBXAgzvv0Vxak7lqtadR5eJ59c0FkJaM9qbXk6ZjkwfgWwK7mewbt0dm7oxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX6Pm3yEDzqGXHKTh6OWNs7eXVwW3_yFFqa88XShG6aZrFngvqdrSZmnA6m2e3OA1SzMKcPAQRq3UyZ521ejMEu8ExZVGOMwDnrHPxnrK7IbXBS83oHbz5nAKK1rdd_kgs7oY58ef7iajrOzmlj0-iNVroHzY9L1GQAHHxaamNcfM2Gz8CRMAR7ZfW4R0DylxRGgRtVfUXYC6t8_AN-_DZXfP-O5-9lDLz_3CRbq45RHmDHtbhDDgCc2sjSVfD6kKyRpkNu-F5BVvsnqVP4FTs9yz2B7U06M2nZaJy_1SKhIBy-YK3KJuY1uZEixVmSczSpLH8rWyOTQPEGlOeY5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2Eu5kgIMqMVCXgSj1P_zouau25o70ocOSI0DzEwqwhZuh7B3Law0ryPiybnzYq18q8QzyRpT2vg-h_tEx-VyEAp3vXNx0RGCtcL2o5UunXNGVpzhzRCuXnNWZtVI3KF6etYiPkgZGm0gZ3qa5zil8Tg5iiilFFCoAHLy9QzZ89KM-CixCiZkiAXAk7mf1s1EXy6kgbKCEu5wSknbbRq_fkbg0hW3yMMHkUBWo5NdLuLzuHRn9ZXMnF8crjEaoX5J4E-K3VFVXpWlun0QKG6_eJCjW2ZtmN1ZY1F7ZO-a8HVTXMl1eZnrutGhaQLygYSKcVUGZPmnLQPiMpUJOgXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcfQ_o_Jh3SoMsYswFeFvpXvRdOlGtXhBe0LVYa7N3UV7Bdf7M9UoNcvmWF34imfr0GJpq3hKYdLGa2JbdL45XqCfZPxjXX2MRnMCvrzDqv8EnH5IA-RrJhcs37PQ0BbBVK0867Rb8zwwjj70xGzf8cApjDsklxPBeDVij1Szmlbys47LcpWJg6U98KaJ_FM95kTk7HLYWGj6ZmNMNKheGrNxWhb7pYlgy23PBKzxiBVNR8Gti2FBHDicsYLTHY3ZEzpvAfs7xFEqizFmaYpt7bgvAjNG7b7WuLQ0IN-ogQKrwxun3-e4a85OhlbdJUQhVz43GEL6cg-_LPKR8Vigg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oC9zA3-OaVqPiy_38LkYku9kHH4Di38NvqP93gFg1ICqUbdSzOpwUOGxJ9fM1tb1XeNTCvlZACst6MSec1pac99lqtYW8j5vYjzWtb2DmR66bFKJ5hxD0dOrfaGE5mB3D-EJtvAmfP1s83vUte1yZxKv92YFN3XYxIQeJHV7WJ8pENkSs0SxGEFWtChnAeV_Zobt-512o_sFSTnqJOBIVgqveqXIWNtoMqxReNjz-ZVdh7BbPNz81q72TPSJfemJC4itknzKbRA6F61kwxJFuiqNukZXLdaz3l4NSMt355LsOls7yrgNLntgjtGdHmFwbl-aLL2DBktwv_YVqMsLvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YmTBbb_X4MZRWj0naTK8CCE6RLXadu-8TfxFlPTWMSFq5i2KhcSTyCLolyyWVLCMQWccJIAp3R6GOSDVH1GOcBppJtN3G_Pe3un9fh-_hzJcMCKaIqkG39fiIYRGh6n8lXytlKV4m64VXfoN60SXl8XjRe85t15FT9Jbe5NwJzwVJWun4TNYo_vzLXnhrOGbwVMcdV9ZFdXx8CeAhsBqFJzLXUtE17TR8TUK-Zbqj3kq2xO5vIsqjMQfoi6vclGC-bA2yODS3LvidmK2VhZNsCcj8erTwcgZ613gLT4DOhGUQeGNzsMPMuFFvLiIfpJoXKIIVLQsIrgTlyw9x9KsZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnzhhtiiXdMkq8slrwpHyzvLO0c9RN1FUwM1_5MbfZG1RQkQdJD6dEFy6C_TD-XhMBky6OPTUP6_YUOeLCUXeR9EYnxFMrDRaDZP6f7jp4E4RUlufr-F4cA90eolqcTE81mj_Tq40Q4X1Txc-s6dFyX5btbhWmdD5I7OpXMWzptt18ETuretda8tpczYiIAR7VlV5EYxe4zQcoWkYSy54w_gKXp_JyuXTYxz9gSKJlN_oMnRiPrxzXAqmNzm_zLDvGaW2f3J59EinERhP1Gsc33pQRRji4XjBjersUFL1TO3sRe3KE9DudWOygKbZxyp0qTzkawEZ3tRnBXemZkGqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqZe2nBI2pbyP29RcUWa-Ktxy4txMci8q3NL82yOABrWDEM7945pR2wgaIgXqORU37kVD_C4vdTgc2wQvKyZvneBLLlp9Qm3PECSzxPvE-uWvRnSeBVZJSEtv-fYL2OIAFW9B2euf_v1MnMQWCdd5m8drj0_vNp1USgKoFU40oUx8cHwkL2H8XeARq0tXPfdPOsmhE6mohERzmHmre3WlVmGHIjTsM5M4E2OwYxZLguf4R78cbpa2rH64PjgJRk8v6G7dTIUCft9rJE-1gl8KJv2W9QQpJb04vrpFPY7WYd99bqeA93gHU6-7u9hUNpnVYuaRZx5mok_u7MtJesLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcmuEd5PCjtF95RfjuuSBkksLx4NguiBWnwRrbb-mrGMz-42aq_AJTQbi6a6PNj0X6Y6yAn_Hox2cmSkT5kTgXNIGk64ehkokqbjM5iheufI1RIKlsLpt7lyFbO3P1s-fPxcPxIhEcH7Rl60jApF2xDPE8NL4azGkcNZqcYYxYwAw2iThrn05tx5NLIb1B1f506uZP0QffAz6dhbyjFYbUkLRjMzmK9OaAhV3NMGlLkv_THRAL_LPFCYnFrWtPEJwxQYxrzJm23Rs84YIknmolItKaJ3_rhlzYMXuT3ixCQEMNyHFPUnT48peWHSlAkytgJnjv0BW_xC_X-i5byWqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-p2czopnhJD_AFeG7ugbKaFQ2BT0MftfaSFPr49PbyS6sAssIZHI8bWL8gM5cRXk6dPkzBKSn8ThFOSihdeCdJkzH1FcE-prjOKWdNEGX9WnHBQ3gFsA8e6pELgaL-s-wSqDfIg-Y27kuKS9S2C_xDsdrMS1b54wwSaGiR86dkHoE7CO5XGN2Rfb_g7h2ICpnvzChtucHLCEOVP-GOPE5gzNRHvPb5H3suH22O1fB6j0Nyk3i77MjA80J07WfkMznzUHZ-R9dZl6n1cpA2CEq1mnQ5NuYlBdmDzIRt7t6eHYd8UI3CrQPDvFK6YT-hRbhhbGh9No3NEYA2OCC_BPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/psqzXmSDT2VdN5zdr_o6Lk9_KT0_-F5NeJQchF1I-dSTwn8By1JUJnWmYfcyTUNExRC46VTWf3qfdvYfUYGu1SmKaHSOEp-cw0Y_3q0LtOXbWhM7s_hIWhJuHwZ01t95am3SS8En_E7JRly0HAcmUMyM34knBWczrPwdBOdEl60_0bbzDXYOX0F8AwSkk-WLtOiQot_rkCdwXYJqagFhGcroMTTD-j_I53j2Ov5UCs8zWH72oA8LjPMSuV8ZPiUSiOUBPrtgFVgZVBzwSvvUHhiHe9CNbbeWkjDPfrbUY59qLPtk8V08H9KqyPI5PDODHWbw-j6GyVoL8SlOuOEKEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ_Z5J4QztzV7uFbwKEi7p7jpC_mBM8wYqcHbFiA9QcW_xeEUYLzqAoIk8FlKu9WxpXpCUMh8uTMn8ozYmr3iDeYMSEGC_rtuAFvTYBBynaPR1uNGlWuXWlQtkGz6UV_WD0qqBETYFqEbcs2j0SY3nWTgmvWo-Z3LpdHBF88UhDqPVKkDgpP8chnaYP3FsQ0gkJEovotd_kcuLygUvCB2N9jMKweRRfq3LB-oXSE_RIr1dP19gMiHwu9ClWj9Xvd-nlabgDoZgzlNtQpY1NhnAzAnlz4xCfaLc0odR8pRMzAAtC5gDT52yoSwMz2tb1-xuTlPnaYA9bBNnu7ZG_-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbhCmuToz53C3x4j8yik66LCP2-WamdVdG42f6kPdHpohBnsmzXMqj06IFCBG0_C8qgaOvP8R1QPdFExkcErVeIL9XbTF3rBuErBON_f4Qj3dzB5EtDNq9oZr0gwC3e0N7kUmXKu4zEtZad-allNw0AkQ_U64gdzrfaa25T_RLwBQRfh-eWJFy_KKP9UacghfBTl0J0CUBGPZ0v6-G2xF5GFLOvXVt-NdrV9RUSiY_tP0GQf_zQ5_au-0mH1oF_UUj7GW-_6S3EGyHy6LPVwBnfk6qTmHj7n_wVQSv2Itfq6KP1XSEu6ZT7EP80Gq40CLXxymwTdDCLy4Io8eW5aEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSH5EmDBprAtE8Th1EmnBBreaMH0ZvY-yTVRk4jw0xCoMKOFx8-aS6O-LKwNluV9GpQ0lG7oNu6LuHDnyq0Brj5eZl6dODP23RuObToTOoyUTCMdoM9dpAheYShdz6tzZUfUVZPRTTZgInC6SlSEMxtW5Ec19Ijq_zFq5CdBAbm9XINtfLEl9d9PMaFrAV61Na7uEXLMCSKb9Em4Jvj_KtoqRHrp6nxKz7onHV6T1sd6egP3-0QKvWhreSp8elkjLSID8S3uGEU1SZzXwiOYbCQXAv7mOkCfF2K-RjSXgn3Mh21g_9QVLPELHl5B-EpWBF_bkwcoFzNlkkS3Bg4DGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAVggjrLGaVhzYQ5wi-E4GVOx32L-92KzmX8cVBTcUQsIvlcNrBOGGawkMhZlqbxpYdVsL7lWiLuR4ygyBvRe-oNN0fpddudrUQPoaV3AVPtf1PtaOInBy-j8sE5qTwLUC8nnOB-_sO2YQ_dD9sDjr8S_h9H1oniB2v71Cf92XcQfjkmw7WI1_qww2961pMuRRPqgmxbb8u4nZ6FXneK3lEweUtQAFoLEVe0TaLvBYQqGAdpF9l5EBrc3VTA3g1_9UdO95w5o3lJrE0PC_iaMbybDa_xPD3gvlzC91FilNMFgTiXq32i0m9d3GyVrTIo9lnyhHgnBaYAdFwQ5ZS9eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVcV6QhPiYX-ugwajivJqyMB-yDldhzW7iK43K6uraAqJMw5Q39kKEI-fy9sbHuSLKyIZqnQtHBX8RmkXVJIRcU9PIPKWbv-VKd_NUVmEG8wYb1Q3c76DyU2xvBzoxKRKhzy81TbU65RNTKI2jNwoqETJsCSM64SfbOXYfe04grRzYNP0LLXwTtpaBMwyKdmJSmCG3rtx45aAfaM5kt79fJOgS8SJXsD0O-2fJxsjrgJGHf_Rycj0igAVfc8_Ro6Nane79qglOMBUkC1irjrKgI0z47VFe-n4lAtjadfAQCoKZB6kou9uuCZmulnahoBh0S-4CrcsAR_bpUog8wMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2548666d77.mp4?token=gK3ll9JuXVAR2zo9XkK2TlhyUG5KimcYYMHEgqzE9XwvMhuIVBF0Eua8ioeC9PvoNb5sP4j_-Zjzt4vvRvGZS6Zp1edFM7y4XogP1Azde0D_gmJihPco9GVcuEe5_yhP7zOyQIGEAtubjldvj39Z_FpapSDIMk6mKmRXaGYSfa7nQgVVb-kewi0fq45F-sYUpQq6ASwBLwzhXY7zEJETaEBhOSIiX83mkW5wWjbZ7g0j49hhijZ_08gkXxcdWI8tWdOAEC2Suzwwid-Yy8q5Vs5irqHqd6L0uTuhNMGKfAX1S71iumV8p6H6NAI5G_Er3z1ghDvCGh-GL6Sz5e0YoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2548666d77.mp4?token=gK3ll9JuXVAR2zo9XkK2TlhyUG5KimcYYMHEgqzE9XwvMhuIVBF0Eua8ioeC9PvoNb5sP4j_-Zjzt4vvRvGZS6Zp1edFM7y4XogP1Azde0D_gmJihPco9GVcuEe5_yhP7zOyQIGEAtubjldvj39Z_FpapSDIMk6mKmRXaGYSfa7nQgVVb-kewi0fq45F-sYUpQq6ASwBLwzhXY7zEJETaEBhOSIiX83mkW5wWjbZ7g0j49hhijZ_08gkXxcdWI8tWdOAEC2Suzwwid-Yy8q5Vs5irqHqd6L0uTuhNMGKfAX1S71iumV8p6H6NAI5G_Er3z1ghDvCGh-GL6Sz5e0YoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
شما حتی خارج از زمین‌بازی‌هم لایق احترام هستی آقای کریس رونالدو؛ شخصیت بینظیر و قلب بزرگی که داری رو هرگز فراموش نخواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=szvgZqajG5oYUSpnqoFTz0vS67E7xFOhSKbrk2XupZquf2ftF_5k0YRZ1sjtmqnQXkmCKoEPh0A2PYVrWqa0mzaBsHQDnu8qf7mXKe5jbGH-MsxyylVmAkwONyt_k6YWPV05HQc37YxnFomJfocC4FhTcXwJvEfHu9O6Gw-fP_rCwDs2u8ecK3KAelk31FJBQNM7q1IOj8CuG4LA_8v3SYzV8YTLF_Ai7kqid_oC6LGpcNRk7GnOpp8YNX15KGpeJDkwC8bDzX4jQJ7Xk8NCEqFVS4NGHwzF5B_-gHODVNJKn_blerRFKD8avd0FaP-jIIqqvvJI8xF8_1B70KzF9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=szvgZqajG5oYUSpnqoFTz0vS67E7xFOhSKbrk2XupZquf2ftF_5k0YRZ1sjtmqnQXkmCKoEPh0A2PYVrWqa0mzaBsHQDnu8qf7mXKe5jbGH-MsxyylVmAkwONyt_k6YWPV05HQc37YxnFomJfocC4FhTcXwJvEfHu9O6Gw-fP_rCwDs2u8ecK3KAelk31FJBQNM7q1IOj8CuG4LA_8v3SYzV8YTLF_Ai7kqid_oC6LGpcNRk7GnOpp8YNX15KGpeJDkwC8bDzX4jQJ7Xk8NCEqFVS4NGHwzF5B_-gHODVNJKn_blerRFKD8avd0FaP-jIIqqvvJI8xF8_1B70KzF9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=tuYkYC7zeKMvVAKg9aSa6Ydwt95Bjnv9BM5S8bdZ9taWNrpTjkYbsi5MEx_j_L1dusVoZ4217vyR7-Zrn4XIIqy6U5yiQlADgO1UJTYttFmgaCx4n9JDGgOMXBpCeTGWGQ53urPwLWnOCr46HUrGg6p3K6ehKC2e0Zh68820rYKs2qdUP_pF7GoSjzbl58MfNsISBBNNzMd8i1aru_bD1T8o7Cfv1mmEjx2mLhYo_xHz4VtsqVTG28WbgqYf3wxP8WdH6pCSQG5Q8uPSBtn7c3I120SFKUPRzKKmNobb1C_0MVPdzYYZOj_DKWScj2kqWUEsJRycADXgbPDZgd2F3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=tuYkYC7zeKMvVAKg9aSa6Ydwt95Bjnv9BM5S8bdZ9taWNrpTjkYbsi5MEx_j_L1dusVoZ4217vyR7-Zrn4XIIqy6U5yiQlADgO1UJTYttFmgaCx4n9JDGgOMXBpCeTGWGQ53urPwLWnOCr46HUrGg6p3K6ehKC2e0Zh68820rYKs2qdUP_pF7GoSjzbl58MfNsISBBNNzMd8i1aru_bD1T8o7Cfv1mmEjx2mLhYo_xHz4VtsqVTG28WbgqYf3wxP8WdH6pCSQG5Q8uPSBtn7c3I120SFKUPRzKKmNobb1C_0MVPdzYYZOj_DKWScj2kqWUEsJRycADXgbPDZgd2F3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phdgX-hJAvOfYEL9qgwjczkycLR0F-TYkESwrWEkDIa1cjM0qahTkoyvXVokrYdmFNA1kVVpm4hDCmMI4LJc168SYftCQffDMt6vdMTIZOg0pkardUYRUuxsKJv5x_tLBB3tlpUP1lqEXAkutc2yxJTAIJFed01HFBNkWvSKz9LgumJPNL9AVBnr78k_hadqmV-Ao-1mwA_-gkAJsF7PBIRAWqS5lq8DmpWXVQvS2Zz6tvMeKypE69l38n8IhfhQn1C5Af9F3n_EDOYIZMd9gP_Rf3ijVye8l4chVQUfHmqLoyq17zyid8OhkSTlj3CAh8bNH6ihbnKLi8vuQrk_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyQWphxRf5PcPp3MfeLEktEq4zrRL4PAuhtskGYCbz0DpY3lM3cByUEzo7uarNfHcJr89_8xjYl5x_MkK8uQZbWyPRdfowkq4fLrAPKXgrfSneOb7FbP8vEg-e92K6k6Pg1T6fKRBJqrItMStMwpfTrUSH_t5FDtv_eM3qfsEgH6J4DQ2PAZ4zonBgHResN7EpX0hJS2IxK58qpY6g6iWIrbaXygxD8slCf2MPF5hUhLunjRMVBm-EGlqWTOupUwPZCUX7G962ExoRdLPUywIaIAR9pnKn8R7_7ebYZHhecwlkoWDqo3aOPQ1ETFi44stbvkzuzqU55WDt6khJHxcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=h8I2cIJmcFzozSI2K_NDJnI9iqa6yi7S_NX0C4jQ_570cVyBzuc17TBF94VG51rsLGwM9HSHVB4gtsaz-vn59rRpeIQWr7IAbA9fOg_FjWNWOVxK5vdTyLrQNaYt3TWsy3zASskUpcsebGqNfGgAU7L_38mZtfZ6ae8OOHoxhoCan-lXrEC7OZD83N0zphiYffCLAK3bFo-qKODT6c1-HwpXQGq70GAqU8TCEY8QBGq0_rsKpY8F8dSBpl3Zh85Xf4DVirlg5wmCCjGSqz1v7X7aWOAgBOqIaAjK0EeUqKsk-vel4K13sZxHNep4E6_y0Nux-ir-7xR46G-MvAi84g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=h8I2cIJmcFzozSI2K_NDJnI9iqa6yi7S_NX0C4jQ_570cVyBzuc17TBF94VG51rsLGwM9HSHVB4gtsaz-vn59rRpeIQWr7IAbA9fOg_FjWNWOVxK5vdTyLrQNaYt3TWsy3zASskUpcsebGqNfGgAU7L_38mZtfZ6ae8OOHoxhoCan-lXrEC7OZD83N0zphiYffCLAK3bFo-qKODT6c1-HwpXQGq70GAqU8TCEY8QBGq0_rsKpY8F8dSBpl3Zh85Xf4DVirlg5wmCCjGSqz1v7X7aWOAgBOqIaAjK0EeUqKsk-vel4K13sZxHNep4E6_y0Nux-ir-7xR46G-MvAi84g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5KNyIJakBaww_U88SgvFcS6RePKvNEH7qxxVgfd5a1DMcmWY-q0kXHaiuOf6wN3WyB7g0f5SBEqZY4NJiZpbecmeNnpRJCzlwImry6aob7yVEqYe3gzRdHF05yMrBU0hHEUu1t3brOkoIa37PKZ7zXk9yub6Y4jKwRn_Tv8ndjwbAVuF-EbonPtE8GJTg6PiSWodHbvi_4eXkHX-w5oqUIwKBWby5jNJ0e2aLyWRbVBOFfgwxNBTY_mFnKaH-jPKaaUhYzWmRm91ODiBEKgQCshoPspHKbmT1Fm0RMHeJydWLA3Sqq3BAO3BEHi96mx9PXuHa40Z9KnDdr-UIxLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMRORARimPvY4Z0EglIHl-aZcO5xbAmbemQIvtLcc_oVtDadvlEECiJ6_qK-cQ5yBDMpY-FL9yydKJOKQE5n7e5DwOKeS3yP5bDTkwKrS4RT52WDhT_4mKhkCyJVmX_YBygrIZr8ChIL0Kn3cztsGEBopa1YgnZFX1-jHew1OFUfQWoFlGi224DivUHisbJg-ibwLV6uIPQoRfcFvgCBIO6mpT5Dj7uQmkTBcWqOCVvvgOq4NiLv5yfAikPc2ltQdDJXMxXXvvd16ZSvQzM4hE3pYbS7CX64XBfOwwRF2d6-Jf9-l6VeemCyn1uTPTdA9B0mKRjIkHzt0NXRlYLbww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd2a9hP9t5WKJwHUsp2NOJ8nrsQBDI-0t6ylWBPdgrQqEryYHiJ4wnanNVOl0zt3LOFlF4sSXKT1CEtTc2ecfR1azlkcbspSj5_IcXQAn0XHXcPxKKyD_PSvBQMbyn4fbeuJnPZoD-QmvFsRiXAvRgM_UkpLrbg38a9jQ7lrXmwkYJ9KOLTgtc8bUUnXWvCO5PmYFtLYXPty6P4vxLjXrPt4xh7f2A2PIVSwyd-eKflAz0kCB4kF7m0vouaNjCR5iPE2cA80nwwG81Y5bhKeEeDV4qm5KQf91XpzAakpcRXWlj8Ii2r3-ojbdHsNugfrYGjrnmFYxhomWzC04zArVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFQaEhsrDPK-j6IJC_tEJ84O8vyGqyRCHEDKRgpPn9dV_FP82vNDYIoPS2g98Erq8Pr0u0RuFoHrGROVJmU5c2ApvcAv8hSj5nSyPWVTXQ9MpoF9AFkMOIjRgq-37ywl5PGsM0Slpfj2ENpY_RzgTV6u49AYV9shrA1B9hI_o5vokJ1jMQE0sgYsZy8D9USDndKVpgXu9rkD13npNu_jAxz4zEavaKKSjeLqRj5hM_gIkMTEpVRSf4wqBJCns8s_-Q5hL1GMCdpfp6C2hztM6SuZyD-PFfSS5Ja7VZ7_mNiLfuWnAMCtVJx3yfOyujTlSA3PpNINKuUN8DCFiisfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUX2ofEVyBIPtz6EBzf-42qcGtouigjpGX9yUhqQHCK7rCkZj19Wc1XqyvLbW2QUADlVDdoig-6vyeKFyrxh3YmtzAN0Nfe9LqM1Z3sOO-GHmg2RXYovpMEzhcejckbJ9MUZZgbWHmqZsrApb0GWRwCEFSEfZB1_SS5-xhwNrF9Wu37cpotwEAR0C2nhhVglPqvcNBNbC4L_uFhlaFQPkJAqo0MJ3pRj76pAkAFZBwp8WKhQzjdrSCCmj_N_s9o8AEi48-fQqHF0u7JUX6x_EGR8XfD_dDVZFIo63Z6EEOxK9ysSwl8dN_lSID4NcPShDKk1ozOsWyUbwaXQv735uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sn22d7SFKv2BZssnagXvwxf2f2mJo3j3M9ekNvOCzE6KClKBR2bM1X2HrWITpxqSiOi73_kVMQkwVLErgqXGJloBV-MRPkMG8nr1mWxyNimBdDyGeVWkh4EG3-o-qvUH78m44DekRGbmyPlI9R9k5QqvAfipMPdMV85o2ng7RmM5UkbhG6Le_nl9qJRT-z-1XT5Mmq4g15Frr4S1FAqydKP94Yuyp5V0mJPBjn0vApomdfarIkJgA-2US5AxQibrOZBVePJBBW2pUGx6Q6RjgXoX8JqAuWJVcOjOxJ6vSbE4lWGjxWX1j0DDFDXt3IUMpglJy_MGIln867ymePoujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_kj2CyOB9QXGx551GFppH8dZvCN6fvD5jcjoP7YnI7xri5rFgG4Zn7qkSTA9tImmCbp-dm9Z5whpRA6rvj4Twi0f0pL6OUrChiR9lP_Mw4JdWa_MchfsZqPh8wbPEU-Xu-nFjd7GFolX5jrrZhVZ7VDT2ow9KuyCNFClXPN-vtJuVm3WsS2hQoa_i-V34lt3mI9mEDW7jTij6tH7U9OISDoFIxgD3i4Efnx97uGle3yHwMiJUshj2G6m1s-hYtkptDwC2j0UcQ8Hi_NQvKWphhuezbik2e6zqlA-tnle3v2JRkRHim9u4tWs42VNBMaf_-Uq8XUAMLvfePyt98oMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ازترکیب دوتیم‌فرانسه-مراکش در جام جهانی 2022 فقط 9 بازیکن همچنان در این دو تیم باقی‌موندن. بقیه‌خداحافظی‌کرده‌اند از بازیهای ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xr_g5xhXUCzoQIIK80zEynoLqkqKeQQlaWXv8N66c3muQTgCIcKf5npFF0acgSF1uLUKnnXZju_KkrQBbJvMSiyQBaAHw-21_c61djIDkXE_ZggY_VNnctnVsazrR4WJbylZiCpOhogZYVdZ00xueor20AbHWtrsNveIdbbjUS-JHmY_B7GuTlHdroitFzIzYm8SwVvbWQCBr3GFT_dfy24LFIvnkrHF-OR_DSYP_0KRC-94M22M74c23yeXyX-h_cJTbkliahN9LPKyFpAf3Nac1z9RU6_RSV5ZNpxQ4mmRnb9WU5jNGAVXRNY2xoEC-JhT5fQeuIxQM_sHmeEikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOguDSkS1-Nx-sPsSQZSWg3jGuJ5g1J90L91og4JKqfu8EPtTpZDhCWXGzzXkElGPlDNahtZT3NQLNQ4tw95DyVxgmqRr4L_jBAWRjSWvsiVZT1XNa4oCVGJsH_oIblVfY8bQ9fbHUj3Kr1hsGw-v_zXYgWMmj6mredKRiLgKhvY7jdweENfMCk3SmJSdRXuT6CTatIFxoXUhdCsX_ngKsPXfI5hTYZa4kDCFmdhOfopB-JChlM1NqtECaMW8NsySUrwrLOFO2fdwDBzAnAZg3xcNyvDGH_rnAiX95RiEZ15-HEzuPxWFqRNZNJ592y-CDW31Pr56H5oPmy5Rzhhcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNGZ2OJ1XEx3AROL6lGezUMhUwHEqUecF2uS4PESL40_Zz07bcEyN7CjmdK92-0MAUKnNu91QUwDqR_Xwn4osw6XQOWxaT5BUTxacZwOrP0oQia7_ydcDVTks_GqUWRqe_lErui2A1QzLikO645yrGQRlKQ33fOPed92K8es7F6DM-VfmAU6i3BDKrgVohYkXSFIxOX9CU9kDC9RMm14J4qp-hbhX13ipM3dukBsEV2RvvpKDU_-A8Z92SpsCvr2Ulyg3VQvx-lO1DXCEfzccGVTbrS_0pr2tr5_DnsmqCtymfPo5PhayTupsyBzfB49PveTB-4Xa73M2GVjAE8mUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVBMVnQoacHcQurhrlxexX4vJlrN3dFh3I3vH1wUlIYNnOaM-ZCZjcLNeiDzCzzT6hw2xe0Qa9iyHUoIgHRJwn5unRyPCbNH77Ms3a-ZKBZXzDqIkoP2JoJfCjRIqrD2Xg27eFjLgk2kDPoRzJO4oq_tR92RCNKEx5K79OCKWsMyDG-k0rCZyor2vZ6rQOzGyKqT7yA8KdVRa23qCp82Bek9-3Xu2U9iDya9SGjmOwDXkqU2LxyFSe9jsCenxOsXGg3NuT2Nsr2p9tgfRQD7XRWyG5TdlRcwDgNbzU2PIoTsmkxb-N0TP17IWuoiU4TInoKKvttPdcc1kqC-EJUOcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMNrOD_7A1CGOZxUxyshYRvraSr-PYfSJgjpYf7Q2GZpVHrwcoU6-EApgvzICXa9tZDL-DGrCr4ldeBIFZ92M-KSgz0CymV0W5ofrUycZYeiomm2oiWCuVpg91nNkoMU8ypAQsNmO7WSCq6xaTyhEmM7Sg9cD2GQAVE5pRyyp2XGgFqKWA0StTsaZZIWi_G4WBaO7-RVA4pZJ-JFT6arxh1HcS7CuuKTcZyg1Py4peqyl1ZeqD9Fo19jRKEuJL24NSn4YaqqMWHU6mgvaYZBROztewRj_lhKJnhTFPepZ7LXSVNC3W5h3lDASdhwL8cnQWGrSwzl444lm2ELmGhpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FM5jo59EfCG8ibbWMYhKPH0A6sLhPza4Tl1m9y6TmXthej7NpD3b3L7OgPP7raE1uwV9m7q0Ic8jK3yzcueGGM5waiF8olHQkKeEf7mn4UzwH4589VTh_bszeJy56ksfiOmx5PGcVgwNWBvFZQmDh4HorozE1wvvN0G1J_713ULL1SYtPUFL6Jt205HDWf-8JPr3pygYizpSh2_3g8JM8eFtHdLoFa6_fBRR0NYTVRW5WCjgtPcUKgS-D3-PMbmGQpMNd0WiH5jdShtCx5Qcd0glxSPi4UWVUodn_efBBOFOMjCcIZKTSvtZ7UMp114gaQ9b6LMU-HOYIHKVbuTJNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHJGsd2oZjKfE_GPjjWt-zGlKXCiQd2w2fNgSOg43N7Fh6swiWfBMi6sO5-H_-NMFofvSs5-z7dnSZeoL1UF6vY0X0taLj-Yjk4smEWIml-yIgmUt82dRm6SVBKMADKfcL5jsm7wSnBxxHhh__TJAJfFo2m_u6PQa1ag2J4WpF9jb-XLh7fdhn7reIuZR8wPRuNu8vyw7J4B9_QnOsWxSGuwafoWYhdR7TXTFnV5jZNDZHVf1W3EeoLhJbUCXdnVNwQjMtE_dcUQ-kJ0A2fjvRoYg0dL-onoaysFLV0MqkVEQX17basxHI3QdEVh99-j_0GpQopxLq8zbIsd-E99zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25297" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPL6k6-BqTdSm2z6rFT72F7TACdDfahR4__hLIWNsvOKKF6D0yDg2D0HMl2a0NXZUuR9XMZqs9YYTmoovDSmkEFZjrnBUWmOPnWYIdpmLlFZd1y75w8jiAAJWd3lmr2b-zkwO52geqcmli2ZxfzRrdiDEt-440e97O3Vs2zgfGx13G9gaonGyF96ejGYKsX_N_XRF6ZuI0tV3Kc6Sn0AovbLV3EohYWsIK7cVng5Xdq5i25ZvoFl7vT_6RUzi7QNZgBdsrpygJKti4PSJY6r65AHMV-7Y_jXqeuWL-W226ZEoJfetGF0TwlY-8scnxUMrX20sN-n4amlW_hOqX0BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بنیامین تانیاهو
: راستش‌روکه بخواین لیونل مسی 39 سالشه و اون قبلاً هر چیزی که میخواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی‌خودش‌رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم؛ حالا از فردا بازی های آرژانتین از صداوسیما پخش نشد تعجب نکنید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwM48lJO170NFH1sbTOa5ccF6D3-C3Q-tSRYt5rbgjN1JoOKXbXR3W9QSDOKSuCFJXX_-at9KTTuzdnOLqm-4Zyy6j8pUzfSz6MQciC7MfCl6Q2RoRAoUPRRC_6rWNSq6mAOjPY5yxNBc4vMM0PL8u4rahvfnSyR0vR35Z-Zi8bHUIgl7p853MW8bh_wCP9SgOpIGr633kZhNdwFd0z_YvvwsAcgRd-YFFtivKT7aZQV8t5-8o1JFeOg5fJHsWBArBV7T88EyOCTBibbx8SdphDay2nZ_LaxzimL9G6zwkHC7UagoGZ22kneQKzDzwFmX5Ut7hGJoUB_XZVp_L90Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhHiaoLYHeJY0ExJhOqAP-Pf9FW3QjlC5cKPxbGJYNmouMbCijkDo9cOWHPe2X-EOV4szyt99WwJh7oxqkgbGgCB_T2sqLY48hrYdhh69kURmVFvr9e-uO8FM6KKf215suFzXmHZ25RXUhnN7XIMdqOZ5Ck5BN_Bc8c2r2KF4S6lvbvZmkwY_g1oUafmDdM0kJmPWgLK1w5m7gPZRkF2_pe69tkSwxfJ4VySGx6BuOOD3FDpOqln16wr1-iOWdVJHzDJlzrpdo90P7CyJTcOxMALNREGh2AeIh6vBevVx1_q7eO3IDyDl9uQfBoDvMLtkIutMCMEw46JnhckwYVe4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwsRfkI9g52QFVXQhsTtwAHZ9h7Ib4dqd-Rgm9bdLfvjgAP_0TCzy3-riMm-Jm-gMLm3rsdLU-IZAXLrDh1CqTawHmctoMtmmi48PttjLE4t4lU6u7lSD5qpAMGL6AZyVwLHoIbMriMPI1l0o7TWsyZn8RMS2cm5IQJ8EnZ-ovw3rVWHDp5kH6P_S31sF5teH8Ar_dZepIFg66P8zBSUOSe21pdG2N9fMOS89dBKEnmL1LpY7hWP6kA6B4vhjt04UCK9JIh5xrezPY0kqzovWW7hGDHTPNlEVQXer4UxvTyYn5u-y-KJxyzhWhj4y3zVguERAxY0qJNDnYyJnsYJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK_4N6oeRVqpv-_TeDq3en4aBwrAO8a-IJmCk6P95qs_RwTKK6uTal3UNIyk88VoRUwmscx2vuyRB_LN1MXK6kvCgWL6Gxz7otUsPc7oyigXtGmkG7RDxObeaFLjknj3LnYzjNqlOtStzHIpDQto9J79yIVE2_SLl3WKzcewBswbwkPrKCTIYg5E3ui9S7YVfe9sSDoLh8Oslg_DcPP0QOlVHcPIUlIrdn7LjXgsDs3UuaaNcHPuov7iD-TVwtFkuYzXNOmX96gGOx3t6k6KMwgbFQIzflmDHxnAXdt7ObjUTKGFHlgC6-yOVjfqR7URMx3RUYxVSN_jJHxRcj7Exg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzG-HegEcRJjpfuO_-yGmi7QXTymWVBRtfZDs_KJLqjqNbrtL29pbZU71yDhC4wG5Kw3txwAw_QJPvY3og0Bsk7S4MTNLYjzgLSXcMjeJsszSIjjv_q1dtYUI49XhWpQ83IiWlOzc3HB0dWiKeqOWZZs5SeR73dpysOLry1Nn25mHlY2dLF8iX1T1gMhpFD6RQind9Lgs6JBeXt_ml991Dlk-SSLCVsuZgyma6MmdNSMhAmd6vm5ReKe-hhNawyz4RDOGA9xtc4GJGfVDIBjp7xuhEJL0tJmDjQQUlbQPsyMAw5Vz4uHIKVAfO4vf8VtaZmr9hVi_FpIe1aTs4SyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmvzAiXm6qRyNasSaeHux8m3yDx4PgQzoLJ4LS6vSDWQFiZ1oerMG7en5ZossMLjIhzpldWzu0DqUl0K8kFXvo_o7je0ajn-7N3Ffu7hsbsROxFftzJoFLdB9JQb0rlO60rs-iHc5kBKchPSAr3TA-VnHhGzfvU7lWAiu7UZ0F0UfQNI55BDSRgXz2W7_EBSO7kQrOfqNr6AwA-aOmIh6q_leJcxSBKg5cIzRkI868DrizMnHRdlfP8ph3ux0afyOg-ydDTc6BNQZUFT3xWwqRrCYfma-Jhs5DR23jp457ThyGIWM7N8saRixDEetJD6GGlmxyivnwvRWDtbdiYocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qk0JNPypumavAqVnm_Wx8I16M0y7V5LF0KXfpsilvziCeiSfpLokdAZS5mt7d0jv9xMqdTKCGpr7mLoBGccfNOtOdDk8kUo4xPa5eaoy_MkePXbRLxh4aOACKCkYHUwKdTygQuZsq4trtldYdjqvMy0T7jLFsQwEOvsZSHnyyvreEU0y_Xhe4rGcGb79__DCtVdybWCCgzKIt55rjtM6lVSro2vLGVbd7qG6My7osuEbJrZwtV3Tfoj0xUTR0GNhHrIAkzwpTlS_yLwr-aIdOp5S1ux8yTq7OcH9RvphZC9koetcVabek9P7wEUhulOSLFUkVvIMmnHtW0Dmq1UC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQTqfGo3SiSZtiQ1XnlO0GrFBE90HOML22VVZIuZYun_gBMNUBRbvkPPkY8bzR1aCvv-zQ8b_cqkwH1cbFICakMlJ8Z-rdUpVJaVjV9eGfB9NJigPRKrVaVr522CgCkM-HmwD9PMCkoO3LQamtC3xdQz9knYUvZxe8JFtxKHHo6X-3C9jGnn29yxhY5NrGVBcktPpMCWb9QORz9qpNyU5ZTLl4Ot12Ea78t-zreJq-Q7o3FcKduLtLIc3fpVgfewQvuI2zHjqQXtGPvh-pjsuC42AXvpnYJno4QraBi2kVBW3763RogKopn3FauS8Rku85a832AVEU_D_arEj1qqZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHrSZA7j2pxqJXYAO-CS2kwSXOQ8o1gEgqe3YdVRKxOnltsDSmsa_6nNj69PbdaZ4GFpleZ2r6rPJ7gAVN5C3sQVUF2BdFU2OlOJFdcgbHSr54onvy_SwEJKjLxH075GW65Z3_8qWtbdD0lZUyomD_m3tVsDbedHvm0IZ-lS-ClRBH60ieom54FlL5sY1agJteatvUHtfYLJvMlo3KzYuF7JuO2qeXsE7ybBblloYPp09iatAD-oVqXxHBc1BAg9p0cOf0yokOcaN66XGKsrHzl1_e0HI30SsEqEGSljEZu03Wi9f6Thw_5DUy-Rdo0tCmBVjjEGdQPZsYS8PyhrRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eecBYEYt0j2qjkIEoBY2BUR82eBQL_yh8swsUYWMa0J3-eg7pSrsRjzd-4rabqzlxNYvE3dw3KLWAYRswz10KtPaXDvzS0QAU4R1ZT5EwiQkKVYeEAFoz5UtfRL6wHRjsPPRYvb0FtJVXAykIbMpEZeQcn7vJjYsWulgffo5V6L7-9TI90VpypJEPU-CBJaXa0erS8ZG2f7ruUFXlRyaDxiSx2FXQdb5QXvXq7o4DDg0u1zPIGg4CB3hp1UQXptVlQS6EZBBBGX8n3lVDyPVJBx6I3h6C9xYIm8cFp1wgBWZtsTQY6KHeDGSE89CKiceVqvTH60fKyNz3fIp8SCs_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEmOabhP3f7K67-IDzfrAlPgpTZ0yNWU5ajAPF8hrzUkYtsUCDHZ24s3YUpAo6d0Rf4GiSM9DQFF0f9Zvss3mYe8FoGjpk1lA4WNyI2ELOiXEGlHuuJfwbjM8IAby3fyleP9D2jjS3UuAEKCSbuaLNFxmsIcl54f7NE0EfgKSTqfqwvoU0MkSfyczs3_zo1IR30INh-pkBqBxiw1h1_S1g-acT6kGrKtlwRuKbdFUL-YEcWuf5udHWhNUC1HIDgNQLroG4XDFD0jM0JEhDb7Y2P4khybjek1GHhVgud-Dm7cgKKxaFjUhgXxwZ9IB7lkuBDN0Hya57HxhpYko6CZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTJiyaWnu7litIctVoDXtEREbaq7ajEv5wqNvejVKh4fTS3ZGcz7mrgevkjAMA9J3mHyfUzuiDntkd_PexD-WJXerHtkxuPJkA170bxVNsU9GO3qnRhOp3tPwqo6qPjKzRq2w4NF8YOYL2UPXUTmLBU5Bwg2-5G0bXR1t1LEs6bGAg_Jf4-pNwuoOG2XQjvtO8XqZVPzQE2c_gb9kv4A_bgjB6xj8sO-Fs7CfUwU_Yei3VX08S4_kHbvdPuX10ZHLqqb4l9_am4liQN4YtJMNiz6hgeR1XQoOGzHKzV07PlQ1HeC03a5cNDSUGCI-xsZFEDWSuQLUuI2aCqhALL1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIhnp1_9DKXBAY_0PuStuLWi7_Ea4O6Aep3mxKVTD9oYm-Kx8ckXk-xm97QUuJp5o6A_i3lk8FPGVE6nq1Tj365tc7FTu34OXRB1eqxXwCQuPJfauu0iJ3p6Kke9xoaQwZQ8KALo98TnSQhi6SIKbGcuuZHvcYW1tnZ3YNa69wRPb4GNJ_VOnaPHNvk4MY9aXx-5iGiq2cwXRNoNsMHh0c5voGmlXMxS1HGKagJGqauO-lh3atas8WJ0NtJ7mxkvY5JU7BJ3L3wTm4ab7rmad5ews3_wT2pBryIEKZ5lZZB5TPRHomL7UDLaeDOuKsrKjXio8DwSTubfFLe89bPzBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW069IVFLkiflq_LAQJ6gbakpXZG-6gjnl1I_pPFV9bHOBdTxYiy5M6-WcH76J7mqknjuMUght_rYumobwubkRLGW7qdgMCMCR7C3xIFbR1jt8-X8BBNoU3huTGy1j0xAWuiMS7xrVc-yZwp1HR9f3E7BwV23W0o9K85fcwsAgQHktTGz-1qSWzTFx_1j851oCugmtK0fEx61uOiurRRIyo9F6uE0tD3mUBlU6x_yUgtUEPNF3mUtJRySV0q1mLyVO0PkxIQRXKJDbCcNk-I7bFWWuvaC3v3e1cuQ4m2VflqRno9FIswG97LUExJyTkBenad2f54YpTAHiOomUS4Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUFnCQW9-4POgsNHXMOgeLboa0EStpaNZnRZUL2pf1FY7mdFs89VOuviIf9kT5WAqcKDKO25erUbN3kjJ4lF5HgAYrVILJI-nAfNYv7iycUiHbDy169vwdkhjb7eSb1fQ3A2eXQ4KxVTg4bgeIxgLydoWlT2my0yr3GKtcdLtNVwkHPnc7CrZLZ3NYVjFzVBOMD0Vtp5K1Gz5_ZfQIUPJRhoRRRoopdypJHHJM9lzseMCJYHcn9djKa5vEz9vkCOXhBgpCo6GsqQpGl3B19yY-HymHfOxupefOtWdaP2iTIPHf1q7-g7JEkiVN4OH9gNRt8S1QNbNVfDmnt2SH6kkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
