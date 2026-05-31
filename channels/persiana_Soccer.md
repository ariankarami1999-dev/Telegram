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
<img src="https://cdn4.telesco.pe/file/Y-xPyG9rqL-hC0ltMCK3SbjmOcov35wdwwLIGE56FNxTCMFRxit_kNmZQ9-u5Ht2NEIys3Sk1mSUf-vDwkJJjxky031IVgP-h2lI2kcgvdbuYRAmWrCa1JohOOlyhaRBRo6iZtoMkwCuKhzItLGA0qVho-mbSgbUNnfJrlw9_rCIx70YVBAl-JJGIrOIdvDEVdLi-COfKHMxYCaFsRAtCzKscN3RG5LL8p_0OgsCIkU5LUQOrMQ0JcX5ECnbu5bLzrjV7tuieXqg5vY84JkXGGpGcfKLWq5aGKYIsu6ZwftNiXjEmU9NpzjsKS2MBuq3nMJJHPpIRhKGeYqXmtSNrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 178K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 22:11:35</div>
<hr>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkzRfdNYcxB58oqGamzCH-1IQ5tVzP2l9gClvGyoRYNp4yVeGABUseYCrDRPG5-Ptwb9xttWVnlhdM8j-YpoA6qmtJI53aQ30YBhf-QlbydJ6Vd4Ie-Uo3wYriXT76q4NzTZ_xfvI_9bqNuPtqESZM_IfKFXmZY1EQYHsoxJV_kOIQ7VMYkeXP2Ymtt9-YvZJTvIcMcRWnyyl766zx4Vfgqa_MtsF98YmJtia7dvD7Xji0JcpQ5gTOfCQL26f9nwKibkGkTMcEZMRNi8ZHx7-dNg0JBMrhaLRHhaZKnhhokxgxKHxC2itkFyLiS2s-09bO13Tc5tJp7Fbiyo5nSxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxpjTHT3O_tL26xv0s5UMhH11s6WshrW7xYoDgtQm9yndkTkZjkxc_p3UeFsALjQaCCV7rJtXDy9PGfvl0iKdLzsXj2Iexuh8AIIg5AveltGkd-FHfDpppUTspp7zgm2U2Do5DUnO3E213JcWkHg6csYBEp1-hH5jv8bww1pVZAbiGHluvzCTCqexZdmTgP3gFMTlU1w2D_u9C6FR0wKG7UqNRNZci-vT8ktMAJP6wcap_ei6xMYfxzGZsmqhXeNN5iAszvRq-g7L8sCi6NryegyOFGrGLfhbKkY4picLPa_WD8fkwKt3eId7P0lmN07Ea7Nzbu7MK3nnUClfqqxfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خبرنگار معروف ترکیه‌ای:
رویایم قهرمانی پرتعال با کریس رونالدو در جام جهانی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/persiana_Soccer/22564" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=HNi029BPcVND0Cx9H5bC0iyICut0Ut32JOB9A_GTccGXhwaZfCs9nkdytvfM8kM9ZJSilKH5J8I_8FoWDmasfXL7nEUlfDU7JA9t2NmjX4GlFtfu-O-7M8CPMgbLyQU7I0umS0_pfu_uxCygRsCV4xm0CJXr3l0CJcHeCdDDhtBsYUa4vICeEtRJB4Rq5vA7OfpfWN-X88cugor8LplbBpp6u6jdsu3Gz25TOGFUjcqXbMm-_dD-qldqd1fkI1-5drCZV5ra0YrAQwD4qpc9SuFjSS2V5AXgBMZ2QkHFudN2M_2WY3bGyzueP4AVWHsucWsI31AWab6soHEHp6asZGuO_-iK2lysfyvnLZZUsG8wkhATAfml_sZDdHoeEJAimUWitZyEaBTOFPL6jhu4ZSZSaNb_Q5d3nWE4AxrcLSXhag-xzZwEzJaLorS54wMLt1FkMg2ESXZT74RXO4H8YXY7k0FbjlzDEGPX-qOHoCnc63IIdt7UU2IzA21rh54gPd-hFPYVhtVBvqJ8-jNQfo7DL_BQdeAgTV1gk7ywX_BVvmZNiQGwcWvMcgiTgYPM6Olf7UilpgyRHQrmApLhHQ8Ka39tOYvaCRqzqSbPZADb7fgUfZg_S3nkjSXPQuVI3qVYgWO5QNSIPcGURziW6SzJChWJr967AMygMRVulnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=HNi029BPcVND0Cx9H5bC0iyICut0Ut32JOB9A_GTccGXhwaZfCs9nkdytvfM8kM9ZJSilKH5J8I_8FoWDmasfXL7nEUlfDU7JA9t2NmjX4GlFtfu-O-7M8CPMgbLyQU7I0umS0_pfu_uxCygRsCV4xm0CJXr3l0CJcHeCdDDhtBsYUa4vICeEtRJB4Rq5vA7OfpfWN-X88cugor8LplbBpp6u6jdsu3Gz25TOGFUjcqXbMm-_dD-qldqd1fkI1-5drCZV5ra0YrAQwD4qpc9SuFjSS2V5AXgBMZ2QkHFudN2M_2WY3bGyzueP4AVWHsucWsI31AWab6soHEHp6asZGuO_-iK2lysfyvnLZZUsG8wkhATAfml_sZDdHoeEJAimUWitZyEaBTOFPL6jhu4ZSZSaNb_Q5d3nWE4AxrcLSXhag-xzZwEzJaLorS54wMLt1FkMg2ESXZT74RXO4H8YXY7k0FbjlzDEGPX-qOHoCnc63IIdt7UU2IzA21rh54gPd-hFPYVhtVBvqJ8-jNQfo7DL_BQdeAgTV1gk7ywX_BVvmZNiQGwcWvMcgiTgYPM6Olf7UilpgyRHQrmApLhHQ8Ka39tOYvaCRqzqSbPZADb7fgUfZg_S3nkjSXPQuVI3qVYgWO5QNSIPcGURziW6SzJChWJr967AMygMRVulnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفت قیچی‌ برگردون‌های برتر تاریخ رقابت های لیگ برتر انگلیس؛ عالی بودند از دست ندید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/persiana_Soccer/22563" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDp7NZiOicn283rqB4OFmtiTyr6yTlk3_Goa185JTXuNknZmBlxYDopxNL2sf3iNKB7sQewAzisddGLZyJv9FroCU-c6OUkiXx38285sJHmWTpHaAVjeaIaw0TID4EgSH609ql3aEAuimJMD_4Sefnwfs5OGXXg4fD89HYZctvODxsuWnBEbkW7-6IRuOzwpOyXzBXFdsUGtdv4pPe3bmObbwBleYYOl0xeJOGXd5qY6tsvDC7NXXer2rSnQZ5UsJGLZ6aqAdyjrATWpvREIEEXpi1OHf58oO49eseTJkgEu8klRjwS0hJ9EFhhkaf_W_bu2Z5PN3FLTDw4cIeQvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/persiana_Soccer/22562" target="_blank">📅 21:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktdc_AN2Qs5Ihu1CsZAmoEajPU4K7TQzwuEypLX9acMXTbF5_C9n9_3LJI6r6hRAH9gW-3lQ66aJIKQCDbKkEQXAWQp1vOquQjMtTvfw5xcvr-fCjKbGE4CBg0znAr92aEugQwkAOZUnHlXBplR8XlCB9RhYH7kKM_Toy4YSAdc0v-7Mft3MwvO-2AjfO-djDUlftqhZiharBKJ5-NjQ7y7y21GyLPE_Q10CRGP0QaU3nik4QpxuT_JfeKs7kTILBa8K_mg03cjUeNKlolwGkJH5ueyaU36qryRXgB8duToC_7GZw4WcEkndqFRYsddpvrNyjzbASg0tzvSvYIBy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ مدیران باشگاه پرسپولیس بامدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22561" target="_blank">📅 21:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tToZxiDvGwGEMtFGM3hrthWl6mD9piXWfQmeDZxHoDl23YS1V0nQY1smXINr5KwaHkcQLleAFi8Uqj94eag6zczRvRHJJBm3cLTmaVpf8-F3KsT-jWHvECLeL8EStz7bcpmPorMeG9TKwqc-CF15UtlU3vBg_6ItLxZn8tzOrzIEpgwRTfFxWcdVa9gYg9DkiWroEeDHEi6z_4tdLCyT6aL8WdtwrVAVVSgUxXrR0_q9tdOlztm4ws4THlMLZU2_vOxjIlreC0beU47IzYBVBiJ1FikunaPRln2ziIioUYzxkDnqWmB2uGX3JVt476xpTjQJjg_ktDsZtQSfpGoFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22560" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSlvyvnRd-DN_rhyV9Zs0EWUu-o59EUDEFxPwZFv-4__SOJki3ZQsGupitOIlDSLfvi32Qgv9xP81ukXFWQFrMbhEZKsgo_ww5rKPqsMPa5URAfjX0TYrxJOjLAhO8CT-iqrKLlpiSbeMsUSdC-mzxO7dr4WgsgV27U4YXyk5YlclArRnxttHg32qXzAiOaA4RXpALm6e1Vnn-tAk9tldHKNGFlQjQMYjH5EVzH1SIa7NACxbkWlxAH-K81TEQgnk4v18YwQ7x628WKckAWrzlkl_oNLTd9Vi6XXuRotMW5yJA8DH-mdcpP2-mC_wyFW5UM3VTEfLjH7s3URQ2h5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/22559" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=d34cmd1hk-O-BOEjOTjXxYPhI6mLN29sCVT5vqbC6d750isSVHbtkfNUB_x2lmvvERgcUl7i3D0kXGR4y670Y0UC6aDFtsyl1V8Ietz6wwBwSD3WrtRBZuZYFy72_8mrpzXzdeVhYuFDHAqVMU0-SN6odCMIN-O0gWf9woAQ0SJ9TKI_piVMayYDCehDaVbMod0GPKjgEwsaaEcyu2d_uF5mELUQbAIdmFxmc1fYPIAAYUPKL6M7Zb4kVO3syU3FAQlvEAjem7VuVNrA0bhRNmqqusuGUBVcX2EGObWA-6Zg05RLpEdsoAmW_1EsyFVXf5jnaBCyXk5_HB5b51EQ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=d34cmd1hk-O-BOEjOTjXxYPhI6mLN29sCVT5vqbC6d750isSVHbtkfNUB_x2lmvvERgcUl7i3D0kXGR4y670Y0UC6aDFtsyl1V8Ietz6wwBwSD3WrtRBZuZYFy72_8mrpzXzdeVhYuFDHAqVMU0-SN6odCMIN-O0gWf9woAQ0SJ9TKI_piVMayYDCehDaVbMod0GPKjgEwsaaEcyu2d_uF5mELUQbAIdmFxmc1fYPIAAYUPKL6M7Zb4kVO3syU3FAQlvEAjem7VuVNrA0bhRNmqqusuGUBVcX2EGObWA-6Zg05RLpEdsoAmW_1EsyFVXf5jnaBCyXk5_HB5b51EQ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازهواداران‌بانو تیم‌های حاضر در رقابت های جام جهانی 2026؛ شما طرفدار کدوم تیمید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22558" target="_blank">📅 20:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvwsuaLh08N7N6TR8SS4-ziCpQyS1LYS3ggjHH1kA0lVtbZjoJlphFDLH26yeOR-j-o7Pqr3Pkj9TXFRM5uyrdXr2G3L7QD4QpKvfuiS80ugtYRH4utjOqQP3VjUVTomT2_WErhhewQEoN0_yPNdcQvsJmUezIzAQfWdOMWGzmxK8XeJ8wasS8vISmNIQZlBcLtdX85LfOAU3MoVV3OxXnz2_W5j-RF90JZaJrARVXpvi_dfwo_2UN9B9xWzsCUaTOETRQd9XrtsccSocuCVo8eVIZ8plkUqOHlkGyiHu1LVw7IVfN21a7xz_GYrREhtuYAfZYV3gZzWD6o1oH8Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ مسعودپزشکیان دقایقی‌قبل به دلیل تسلط کامل‌فرماندهان‌سپاه ازسمت‌خود استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/22557" target="_blank">📅 20:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF6DP41XbeLiNYMtzQ6PacKfsYZ5PFiwUwpIddW136Dwz5jiOYmhpyBnFeyGV_aTPzatL8bCw9Zg5gx_ENs_Sj_Nt0PG3bnrffzPpphahF_g5yUcTDq8dkRozUstSxaOhENk0QKuG6amYKLyi29xldXsyCdBQatuqpuK9VEQNM26XKypEwncvYVFqWJkLnserbkoam1Pp8syBEZ2lUezY1dVhgtu6WpiK_yfXaXhBlHxTx60MZbTM08-xCFMxi6vgHnRAkh_1Z4F_T1BK52ajae2FPZq9RRm6qKRNswmnhx2LP_bybZpz51K2YSQY2P5FwKqUGzB-qwntcxjt5H4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام‌کنفدراسیون فوتبال آسیا؛ مجوز حرفه ای باشگاه سپاهان برای حضور در سطح دوم رقابت های لیگ‌ قهرمانان‌ آسیا صادر نشد و فدراسیون موظفه که یک باشگاه لیگ برتری دیگر رو به AFC معرفی کند.
🔴
درصورتیکه که فدراسیون باشگاه پرسپولیس رو به AFC معرفی کند. اونوقت سرخ…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22556" target="_blank">📅 19:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjHuHFy82UmObqOkyjKT_dcRfJRZJYdq8dMqJ_DsyYWC64hkgwK-tVt_4wvBTlIEmmKT4V_jRZsNjuSCRpnMzP5_Lpc8L56317gDPYnkZugYKysUFTtrMsmIUXHY7oVQFhfCYukwN2WpmqbDsqBbdXPCPJn1vu1L3PQNsfNN8tRAW4wPWJVzkT8kKd-9R7dIc0pdEUodd9FDPYKxqcfgKbidgiTksI61AiNrU-YpdUkeeT-oNUs-wIHVyTJy6SlMdqfQkjS56-zpStfRSf_9Ezs3VvoTdJwzKDJe5CesR0D6OXmVgZJr8rRK3ISramNiR0DC3qommzYgFTgV7ReGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/22555" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_5VZ6qkaMgd1s2E7kv8kFbLG_KUUp23sN59dmDwwPSWQCVNmBq_XhR562VWCmV12GxNCMwSsCJf8S4ktkflIC6jp65t5-oL4E9X2MlPdhNfJ3e5P3ylyQngasJqDsM12fWp01UpjJp69IgUgyzIbwAUR40dnaLfHIC7VdCSJJLnqvNWSFAY2vjlojDKJgadM1rbtv0EL9cpbUm11zWEB58rDQ8Day79r34m1ciEytC_koBO36f0uHcgC8odti-rhqOJAcTw3CjEOPioBy48A9cboAGtZr_mjJDIVKUy_eUMEw9Zgz2X3E4a6cKS-7VmoZXAX2B6Tr1DCF5JdkR1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|موندو:برناردو سیلوا پرتغالی تصمیم نهایی‌اش را برای‌پیوستن به بارسا گرفته و به هانسی فلیک برای‌عقدقرارداد دو ساله با آبی اناری‌ها قول داده. انتظار میره بزودی رونمایی انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/22553" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCtwGVF6iZk_e0FI1LxFTJvKIgkmssBnuDSI6GQnNiVWXS-DayzQAepsG1kC50LEPl3yhUpBkIvc00yMURyyl8rELHsUGNMI94WCe5nE-8Riqq6FLbQ3xh9OPVv_2bErEu0fIt8JreGbySkThNZojZq59um0n096-T5GWMgHGbIANDJ6SEf1oQiokB3fWmc1t7foahiavgdEiRJeN_QJmTiB_O8eoT-1QW1EIRw4iOEiLEMrV4P3nuXZno9C1wcPO3VmhUNH9pOlKtJPLn5n7E1_lixCJQa6U7LfsgvdrEu2eYI3GrfI_kZlzvCuMwDcAbZN5n-m3110e-I7Tzj_yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛مدیران‌پرسپولیس به فدراسیون فوتبال اعلام کرده اند درصورتیکه این باشگاه فصل اینده در سطح دوم‌رقابت‌های‌لیگ قهرمانان‌آسیا حضور داشته باشد موافقت خود را با قهرمانی این فصل استقلال اعلام خواهند کرد. پیش‌تر تنها باشگاهی که مخالف قهرمانی استقلال در این…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/22552" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/av17zHrAdgxtnYsUQhTuIp_6V1zhmwoIxqQJXUHSep5S20BNo11fNcUNevGWHmFCAaFLK8YBU-f4rc6ZnpsWIOJColw6Ur3JNloMj7ml_uXYu-XMqfsolGjgyE3Ijo64w6NTp17xH3JH4D9Mv0hqLhptOcqI_R3u-2142CC90ljH7pYZuEu7sORWkRCJ7bOhe0PAzAfk_6KJ1ECXoPbkoSDpw5yLBveVsYkyGOuzQrOIvyiAKpV1e-hrrzUCE21cB_lyzOfhLcSUJqHv1YIHxJo9XlaSHqqRmfNB0S8kP-Sz14-MFGao29U7SIM_lusk0f2hZ5NHTqWNhYuCYVYklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aASV4Er8gMiudfXMGhfNvCHb5fibyB2lnCia5RK3lrxUL_JgJeFTon4-0m-qMOfYYc6EYGBwx9Q3r-fuI0MgVjR85cix-4DVj-OF2LjojqP1nVsbGUVsA2FS5h_74GQQi_Qp58VGlNxqMqw8bzcqGtAOd98ja0Xf--4fjQ5dMkIQc12jz8qSOoiFohraVUVWeI386tgBiD5rXMCdydvBFQ52tpM7ODOfLjIt6W4bIFA_dl-CvXz9hKeNI9MCEfXYSW0rSJpAqH32HFzcYPIqXfZuTNjAt9Tp_7_ge0XOkDJEKh8b-zrHAbN7_IlwFCzUQE5QeU0vz7i_KHRNm1adag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👤
رقص‌تماشایی خوزه مورایس بعداز قهرمانی الشارجه درسوپرکاپ امارات؛ برگای بازیکنان ریخته. انصافا دانش‌سرمربیگری‌رو داره فقط تو ایران خیلی زود قضاوت‌ها شروع شد. حتی یه جام هم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22550" target="_blank">📅 18:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdSsmIeSqMVM9-5L217aEULWxs3MgOPz8Swsvrf-VbydfJnHCx-oHA5vRyu82AqhWOG7T9Zi9ljLb9yrFYHFlSZQwqCrtRaBhKkqNTWZCi-v1t4XPGKbAyaf5KMCCoQvvtOjWzWNkzd_iJddqKgWhT-j1Uip47C1xqDRpFMFFdKNEIQBb-WPiShO3Ub4r5SnOwkAVUBwZIo2dpB4AuUr88Sf1yWsWtWwMkqZ5MIHK06hOoRL3n9SmgureJe7_wrW8oK-rEQqYaUq-a--_f3yfa2JVHgJvsqDw96m1UW3WXxwwjkSvDnGw8I2bfkJj9EYCRDxIDg4zKoNUoAIYZ2_3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛
مالکان باشگاه پرسپولیس از عملکرد مدیریت سرخپوشان در فصل گذشته‌رضایت‌کافی ندارند و ممکن است بزودی اولویت‌نهایی و آخرین فرصت‌رو به حدادی مدیرعامل فعلی‌این‌تیم بدهند و درصورت‌ادامه عملکرد ضعیفش او رو از مدیرعاملی باشگاه پرسپولیس کنار بگذارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/22547" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=df9ar1NOkmtz_Bxxpd5cleNS336Wy-xHlnDPREr_cNkTbFhcFtoltj078ZSBMBZOS1ckjP8eX6yfbi4ymRNf03DSF_zKs5tcy3719GwzLwODt3-Vlg_0P4dQbAjHxpv3brdPeITkD3VWbjjI5JuhKI4ybYd3os1kmrw4iw9vibpl82pA9MtrAwFJ5Lg-h3PF7oAnqF08Ii8DG4Ild-dvv78Lx9V_NjDvwA_xSEROv83d_5FN8fDfaOwLweNjLkAXCHHfI6Edvm0ONrbHlJAbzccjDYFtWPK8h2OZ50z4Gr_NMvp6w7umjrR4IQ8I-g-fboXe5iHPJ8PaUGZR95OtRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=df9ar1NOkmtz_Bxxpd5cleNS336Wy-xHlnDPREr_cNkTbFhcFtoltj078ZSBMBZOS1ckjP8eX6yfbi4ymRNf03DSF_zKs5tcy3719GwzLwODt3-Vlg_0P4dQbAjHxpv3brdPeITkD3VWbjjI5JuhKI4ybYd3os1kmrw4iw9vibpl82pA9MtrAwFJ5Lg-h3PF7oAnqF08Ii8DG4Ild-dvv78Lx9V_NjDvwA_xSEROv83d_5FN8fDfaOwLweNjLkAXCHHfI6Edvm0ONrbHlJAbzccjDYFtWPK8h2OZ50z4Gr_NMvp6w7umjrR4IQ8I-g-fboXe5iHPJ8PaUGZR95OtRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آماده‌ترین و بهترین‌خط هافبک حال حاضر در جام جهانی؛ بنظرتون پرتغال میتونی امسال قهرمان بشه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22546" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt8RxDaWbZM85ruxIzXeO-0n2CNT4EdFJdTwLsL2T4FWxVKGYikixGoQiXOVLKuLeUVenhTVmcOoayEVw5J_59Qqd-useBIti6t1Kk8VRkpPmo1qXoMpFuVH9qXfQ8bA3Ika9btqG7bDrtWrw4HueLix7mTCuvrYdjxNsT019POzcTQRiXM6uy3vCakhis97656xFjdtu9yRwPSEWBv5Q0J8BJLfWUe6LViL8izYWOhgVmr4VCuex8FFpzfLchcPyG0aGIxiXhNH1P2sqCbv4-71iAkrjQ4Ww-qpb8hS6R9xX59jmmSwiWtXC-XG26ZOdMKKpKt5iQ22lNgGZyqeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/22545" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYSs65hm-hwRxImADxJMdjfddOnsAn70FK9YNDyHJrJTBpzczsxGgVrOgGsoKWFRfp3snWRXtvr1E-hBR4zthtzNLoKAwlfJ5aMbVz2FQnk5dF_XVbHjqfjkg3FZr7IriAvKBcwTUtNPKV7MixiG_J9sJhLCKLD3pyHButsevD9723UpXrYb9-zMhoR2AasGCjHo-GgzHlp4nsMaaMmrSL83mlv1PmVe0DZ_CFNPTNfEvyonH5N9Y8zDd80ZY4LNdTT4KEevpwbBQlUn4FW1Wfg9Iew9iWRMyWCXxV1y8lv6C58ULj2SKkU_-ijD1PF6PS2Bzfp0KgviOVJa2CaxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/22544" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfLYbIhvXJce8vMT7Acs4jT83uiDCN0CzCc94O2gksd2usKL_VEeL62Df0jjp0ROYvO9hp66uC2Y_kJwd1Zs5XTBdJSlEHZNxRn82XKGhIdt5AC7QgNNReT2mr2t66neD90gZNEnawn6DQgAdodq77AHvpxSkIvJ4PShi0SPfDAD5_UXhL-6H_HgctDlNWFVXNxIyLeRfTQSOTXWqhV0CCSmsGtZG3XswDm0salxvvQ009R_vLmeGazfgqIrnQ6gxYz_64c8FWN_p9Xfl-mBwRh6BYwR22Y41FTKbziEuyUqIZlT5pjSK3IFWgSNhn6t96vvLX8DNj2_CQd5mYtj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💩
⚠️
دیگه
#فریب
بونوس‌های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی
#وینرو
و با عضویت 500 هزار تومان‌اعتباربی‌قیدو شرط بگیر
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g10
📱
@winro_io</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22543" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy6yb2X9ce5yWzmgMFYM0QWUJayv_LqYMBGJpdU_pO6o3TBXvikdb9uZlxczGuXY74bNAkk9VUVBT38MW6eDfnMuFdllPxgFEzUIvIfZe0sQWiemrAgiz-SV_v_Q4OY14Ak1th2H3CyXKlN22l9_MGMmpi5CToOQr7mYR5hltxIHQGM-of1ePkAPabcFjH7JduNjEV0uu77zpISuXM37J8jKhElwNM8aKA_yaXHHts98eO-mQt7mGOfF2iAA0-vG2jXHG-p26R-LnIW2sr7-p5iEEdkHQrLembmxORu13QUtM95iHlUuhs7ViJb5awsqgCZIvXwuWn3FsI95RMWrGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/22542" target="_blank">📅 17:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XazcIfe1qQRWTdGfPTA15FMyHZox3NKLDh2rlZd5GdaueZ-RwwvzODQJrQVgpm75si3A1hPVk-ZJ5bQY03hQb8ZCkg6mqlp-rNwFMkHiejXuAUe6AvAyZp1JCtXbhjB5pqRzxGzbtvzB7NznyKeSwB0Rs63NwOxCg5yZuk6pK11yz_xUoFfteY8kQYsIB8pGawynPNUiKoEEPRUFJKpLMvpDTbpP6fO5Y0BJpeSDrak3bOTiFimDlRU7-KnFUndTNf2ubGonlzl3V7_5eloIqdCFrdtgUfMsgHTnnrjmnb7LY0wSlz-BJWlp6ZxD9Z8EAF3KPl-9nMWPFgJjq2AXX_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XazcIfe1qQRWTdGfPTA15FMyHZox3NKLDh2rlZd5GdaueZ-RwwvzODQJrQVgpm75si3A1hPVk-ZJ5bQY03hQb8ZCkg6mqlp-rNwFMkHiejXuAUe6AvAyZp1JCtXbhjB5pqRzxGzbtvzB7NznyKeSwB0Rs63NwOxCg5yZuk6pK11yz_xUoFfteY8kQYsIB8pGawynPNUiKoEEPRUFJKpLMvpDTbpP6fO5Y0BJpeSDrak3bOTiFimDlRU7-KnFUndTNf2ubGonlzl3V7_5eloIqdCFrdtgUfMsgHTnnrjmnb7LY0wSlz-BJWlp6ZxD9Z8EAF3KPl-9nMWPFgJjq2AXX_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/22541" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=hRX8qmB-R8bvBnocsjvW2usOhVdS0tCIYK7O5u-5rDvwKEEM3CmGoiqnuqhvucILO1ZDwWPFLWtYc710-NPbhUGHXw2LCSWcnagxf-zamRscfj9mfLxZg7R6tBvBHGlsTy4xtmGfcaHZKjyoZYh8ouI0DZF_pa340bprW26rOQmnknNip5ZigWuZ96Bwe2tLxk8HvubJTj5nqP_fuMdN9u-PXe943aeC3FcrJSMB5_VdNn-oXyCmUzBHYxfoGACcEVfcIjp6DI8fHsyhkMmCGtd-NuxmIrEuLu49Pzu0YWaQsUNx0k3z7cp7mI9NUjwIEiDXPm1AUjiqBFjSeexAqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=hRX8qmB-R8bvBnocsjvW2usOhVdS0tCIYK7O5u-5rDvwKEEM3CmGoiqnuqhvucILO1ZDwWPFLWtYc710-NPbhUGHXw2LCSWcnagxf-zamRscfj9mfLxZg7R6tBvBHGlsTy4xtmGfcaHZKjyoZYh8ouI0DZF_pa340bprW26rOQmnknNip5ZigWuZ96Bwe2tLxk8HvubJTj5nqP_fuMdN9u-PXe943aeC3FcrJSMB5_VdNn-oXyCmUzBHYxfoGACcEVfcIjp6DI8fHsyhkMmCGtd-NuxmIrEuLu49Pzu0YWaQsUNx0k3z7cp7mI9NUjwIEiDXPm1AUjiqBFjSeexAqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در نظر گرفتن درآمدهای روز مسابقه و فروش بلیت محاسبه شده و صرفاً مربوط به جوایز و سهم‌های مالی یوفا است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22540" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=LECsO_Grg1fi7fpwJPuoTCiynjTCUDVYPm5Trx_zkrtOG9RwxjiqPwI0QOGOAvaBxDabHlw0fsdNzZmtzdbXD_emiW8HMKDNyAf-18wyBdo5a1nOzc86BO7Ew8hVLYHFS6_BZIZHLTckn6oRamK5A0mKF4Z3Zg9M-j0boxngm5IevpZ512D3vTrsE78XWJpHCUpXag79MAE1IsiB0CEjC3xJ16U6wu8lt-jVsnVrCLyy_NKVvAnqzUVUiPgyMZBPHSfltjshlMj_PQ3vIJZ0n7gmsReS-XkstfgrgfBsKkiuaD3HgRCJ43jjcTZgdfQVvzfLGLr706Ief3SIWBngaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=LECsO_Grg1fi7fpwJPuoTCiynjTCUDVYPm5Trx_zkrtOG9RwxjiqPwI0QOGOAvaBxDabHlw0fsdNzZmtzdbXD_emiW8HMKDNyAf-18wyBdo5a1nOzc86BO7Ew8hVLYHFS6_BZIZHLTckn6oRamK5A0mKF4Z3Zg9M-j0boxngm5IevpZ512D3vTrsE78XWJpHCUpXag79MAE1IsiB0CEjC3xJ16U6wu8lt-jVsnVrCLyy_NKVvAnqzUVUiPgyMZBPHSfltjshlMj_PQ3vIJZ0n7gmsReS-XkstfgrgfBsKkiuaD3HgRCJ43jjcTZgdfQVvzfLGLr706Ief3SIWBngaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ایشون هم یه مدل اسپانیایی هستن که دیشب روقهرمانیPSGمبلغ 3 میلیون‌دلار شرط بسته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOuOzLee1NBfy67A1oMawMQRh3iW8Dx7uuUU8LqkB_IA8QOHx9woJuhkKp6wz8-bROaYgPzt9pNEtLlRxSCD3tEzv5sFEJ_t66MMAHDEobMI_x9OspQNOLd29TIkkVzDhudH6GfYmuMx-zZAmDt-oskDlAkiH4_ctBk-zb7tF2K0NUpjDHm_8hu-CPOPsbwX45q-dKuq1_Jrm30RZqYhRlVeFXtjDt9oFwB4tRFYYH46xNOIN9XP1391RHbZrCMPf0inu5wyCQoi_7mRCxHesvIYKf_FAh1IkUDWh8y_UqZ1dO91MxwvcY91RVApK3aTS6ogCgN0se8nk-_XMVquKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یه احتمال فوق‌العاده جذاب؛ اگه پرتغال و آرژانتین در گروه‌ های خود بعنوان صدرنشین صعود کنند و درمراحل حذف بالا بیان در یک چهارم نهایی بهم میخورند و یک جنگ تمام عیار بین یاران کریس رونالدو - لیونل مسی خواهیم‌دید. تقابلی تاریخی که شاید اخرین تقابل این دو…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22537" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObWD0I5mcTanFCJ-jaYDX6gD5ig7mv9GKZFzpZa8IIBeDhPV9_VYG9zTLXTzXG4SqP9BCACrk_6ZOCFdkFqYW9pey4TULioW92Zt52_4IgnJAMGACLiZamNE_BeORgJARHmtC6VlJTAxqvAxSvWCz2gT_ORnaMn_GcK46YDaZhOMifIqSykJ_mW-sSgybFl9U6_yR1iBBfJ3HtWiZqKLhAVqbi_Ok9T3JpM9LuXY703DfMXCgalWH2NuXugy6N8oZVRUUqx5t6Jh2jY3k3yewj2FrbMof10ddqONIjMFufRyeohRN8hJzcSvKBrpFaM8hz4QyXTDKncWn2Whr6o2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22536" target="_blank">📅 15:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYcdx_kxaEKeDpaH7q_Zcp1csFxWNq48Rqq1cZfOUSjeUyp_7blrD0GP387ORH5KUTRYicbvN4rnJEDX27MXxBLxdv2337b5x__U06vEYqpHAZeJdzpm_avycgkIDaj5gAqwP8MiBk7RmtHLOHwB0K30k1I6aB10qodnn-fNKEdpIJYZAgzMH__JxPeMr4NRnV085U7nJqQ-IgnMvFjZnPYuXZ3BTLF_YvdEVlUM5FvgqxrNst3HFxjI4drlsneNtClvFcmq5MX7ZSk44zxoA7n4dJ5OPmvRMDXx6GYpLOysuUOeCDIoIeHc2UAjFeotqxh_kIxlLS-Td_64JjdHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکیپ فرانسه: باشگاه رئال مادرید مذاکرات اولیه‌خود را بانماینده مایکل اولیسه وینگر راست فرانسوی بایرن مونیخ آغاز کرده. سران رئال میخوان اولیسه رو در این تابستون جذب کنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22535" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDi2flK1XL1MM7KsI9U3xss0RLuqgv-eJU5ARfUCmQcKE6nfA-hpjjxXy0B17lZXBIedkUSVtvt2nQDX1m9WBhir9CFaizKfadcm9CrlVZE4FPCDirbowMEDs9vm3AzBRzdho8kLYMAwgdFUHbOsIza8ZrNxIDxoiw4tn-ou3Czir4g7zmIDRsIfQnmVrFkloGrekrbLrQSgov8Q-7-3w89A1GWnd_msBFnZTOyf7NmjCz0bbi9D6IfRGjPusjP-gAqHklrw33x904-F2Nl_9qxUL-_fszZsuJeuxkqHbR-ZHa2yNM1eGVGkYa5Y9StjF71e9Yx3iDctl1bixjTQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22534" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇫🇷
عاشقانه‌های‌بازیکنان‌باشگاه پاری‌سن‌ژرمن با زن و بچه هاشون بعد فینال شب گذشته و قهرمانی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22533" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpaAFIjeWZ9C4_sepgoHdkChTBrCrvpY1sqtv42eIRRKlrPQQwEfZYzEn6TkHpOI_xfjzBq-Ewbyv9fXdBNEWeqR1ZV-uqPRBp6DQzbwMDer3JWW8HUrop5GJoXamsnQXGW0UWEBJL9MvtArH8AkCHr0gu4ZksiUxyERZQjPVNv4Sauw1yocWBstkXNf7wyx-OHFSUrvvs6E1CsmgJfnZ8A4JfvB4MjqxfTV0zyRNUGn-5gDOemQegc3sdCnkRXbT-La3Gxwte7AwPwQIc9AQRJAMttP9JZGh2ne6vjPTo21qxcgHrHAycSm0bqqoOvqGpHCpiY4k9yFtAtia4-l-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22532" target="_blank">📅 13:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">▶️
تعدادی از آیکونیک‌ترین و فوق‌العاده‌ترین گل‌های والی که قبلش هم توپ رد با سینه کنترل کردن.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22531" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE0zrF6QdwtrRbTinAhWqWcnrCua-4Oda1Ub1d9880pYUDgoQ8ijR9JG71K1bDKGC1DsxkP09Ocx-piZMzCZYBBF8XxAlQA4QIBNelOh4vF9SGciFNxi8L42tSLxGWYpDQo-FvJwJpWhEsx9hhaZMyvLy2brkJbWW_eSExXfk9Gi0tq_VJFu2js7It3zC-1ymaMZKNimGdCBOH7QmkYpjKjnaTTO8SeII6bd3srmRSFf7SgbMw2k1OyyFGaDzEHlMSIKfJjRaflMja81c0BGbs94GQ0Kuc2RDmN8_2A1j1OpZ22aqeXiHDvDV8rpehB3cDKw8JnLwkBfLHbju70ouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt4fS0aNTu4n9t1FaBcZnhHDzUi9t6wt1mXIxQzbjZIqukN0jN7tGyXE8ZzFfVNdc3DMkRekdQaZz4RQ44Du2K6Vqm2xeY6QcI5xh9-oUNY6EBLgJ699IZY44QS5Okk6sZnVd3qUL44TNE43r2aIkqlzugXYtd9ZysI3Rc-DCvKxjK7JN9kezxoxOKFg3AaKqtn-e5tQwbKUbiu936nnBLKQ9zG_V9A0nW_CNuiX0HAk_QdftA31JA4px_L-hSLB96gP3xAeqL_exC6lCbjBm0Zcg3Fv-tBZdtd6RegPR6S8xIlQDOaQ8x_kmwXnni-OlQFyH3xWCTlvaDfuG3TeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaXKoPz53ZbF4WlmVF9O9Fnt23b6JBA-q5BUAm9Rdw0B2DY0MUrapH2UWbBqFJaCZmODwXWNbt8pLHagnBbXr8F9iQzshIEbyxX3bFlq2xt51URNyKETeFbjLOVqbp4arys1WLOrHzBvijVEOgwH1fRky-SFAkVVe7p9QzcxRUgVYG5QIwrZz_e3ifmWVR5HQ7MTj4fQKBy_vBXzuOEFNaWwidQ74fsjeXZ_bmYns8HH0SfCvRQPvPDhK6Ei511FchIE81QHZ2uq9lY8tYeWNOHX17Pcc9-1o8Z4XgQwP0JcR40SCfUpw4UKz57bpTPKfNlKY-H9lKnxbxWzU_J1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بااعتماد به نفس کامل به کراشت گفتی بیاد ورزشگاه بازیتو ببینه که تحت تاثیر قرارش بدی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twXSBUkLwHEerxnqFilwM3ItsZEEu1PE5GgrOl-4FAU8SeAaxbfL2so2RdHHUYGsGy5zMeSlra9vQOGOoVx-g8UpqoRcaSQ1LQMIY2MVb-b3SmHs0Ysbxrsrh9-MMc6aJf-iYf2Y7wa_ihlq05osTi9c5ry3iurjf_a1jLqFBF6l08lB72J_GBXIGmSq-WoBh3TQBWaF-wzyZng7bXmNjmxmmkcRxIwZXwLXtr9TyWK0r-iszb9P2Dhd6w9o5OGazpGup-EhKsrnU16pbXSAeud7O-mD8XTL13hwKEdVv--rzUoNADcliRSO0MVlgyJ0OzG5niq63M44ddalU76a7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22526" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=eAnf6VgxqYKer5nnoAuPulp97gRj5j9HFnj0fMruWxLcNRFVWinr5i5B4qx9wKk-vVIltvld_eGqXYw-H8lbjk8I_5Xr-PfML5IBFDc9rKxuK1cG9LklEZuNlqJlPvea71UXRNogbvE2YE__BH9Zhz2qnCZAxN7eU-xBs8kcqGYPER1ZC2QojKB-dXbF5TXVt9swDlH3xF4D-DQfHCxoer3V2V7lBZPqjh9JPfjgXaYYLdGLATxDD5o4aUqLAu70GHtEOr865ITTAWQZQJG-kg7W1ojRkb7wnmDAJTLLE1LHjhSc1Ga1VKLm7HcoSPmTxJPSUVYMWGhsQIb2iwRM8whRYRBdnQ1KzhgztgfM0uGHYA13EuTNVG7ze7uzlheq7kD-tb62kEStb5yTh_NDEhyRcL60GEko_n-kn0k9XOpQ6d3fBczgkcxH-8I6EeoWoIteIAE3D26P-VUmOVqF8lmEgmckyy3ysmgOpb6-0zJQTc7rw2PEU1-Bk1-vrNPzPut3jR8SaBpCc-SUXv6tLV7D3hkRz36l2RKRLtUF7eYiwKvfFWTuRIpdmF9e10Z91JxaUwTcCoj9gCrd7NIcS8Ho1XCGBzUraWl1E6UodSr5Kzc90F_ov5xXVlt3OqhH7cMaPoHD_p5zPcUET_VPboxusY8P2E_BORfcgMhYydI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=eAnf6VgxqYKer5nnoAuPulp97gRj5j9HFnj0fMruWxLcNRFVWinr5i5B4qx9wKk-vVIltvld_eGqXYw-H8lbjk8I_5Xr-PfML5IBFDc9rKxuK1cG9LklEZuNlqJlPvea71UXRNogbvE2YE__BH9Zhz2qnCZAxN7eU-xBs8kcqGYPER1ZC2QojKB-dXbF5TXVt9swDlH3xF4D-DQfHCxoer3V2V7lBZPqjh9JPfjgXaYYLdGLATxDD5o4aUqLAu70GHtEOr865ITTAWQZQJG-kg7W1ojRkb7wnmDAJTLLE1LHjhSc1Ga1VKLm7HcoSPmTxJPSUVYMWGhsQIb2iwRM8whRYRBdnQ1KzhgztgfM0uGHYA13EuTNVG7ze7uzlheq7kD-tb62kEStb5yTh_NDEhyRcL60GEko_n-kn0k9XOpQ6d3fBczgkcxH-8I6EeoWoIteIAE3D26P-VUmOVqF8lmEgmckyy3ysmgOpb6-0zJQTc7rw2PEU1-Bk1-vrNPzPut3jR8SaBpCc-SUXv6tLV7D3hkRz36l2RKRLtUF7eYiwKvfFWTuRIpdmF9e10Z91JxaUwTcCoj9gCrd7NIcS8Ho1XCGBzUraWl1E6UodSr5Kzc90F_ov5xXVlt3OqhH7cMaPoHD_p5zPcUET_VPboxusY8P2E_BORfcgMhYydI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لحظه پنالتی آخر آرسنال و قهرمانی پاری سن ژرمن در فینال لیگ قهرمانان با گزارش جذاب فرشاد محمدی مرام که یکی‌از آرسنالی‌های دو آتیشه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22525" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنش عجیب ایوان تونی بازیکن تیم الاهلی به قیچی برگردون کریس رونالدو ستاره النصر
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22524" target="_blank">📅 11:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlR-izVaYPfLOz03BZFNOMdGXgQMVYM2MlcIpkM2wjSWT6NHtqBqd6ioLZaAjy7B7h5TEPC18QUKTMiRBP2MHuNbLmt_QxDXQoDIn9elChQ-npEpkLCLWIts_bD7-A03x5vVmKQmX3Dj13UzwMMcJ8ABTEJAfUjb7MTdXsfHVZH2rzbwAfl3oyNj08AHce0vXlZ0opkxrEaks2QWskAb_eZvzNnj0zXzhp5LoIi5MbwQkFGNs0MTXz49Mp6OnwIjnkN7zH-oAZJonBO5-GrVpY9yCcbp6qhUHAqABIU6XbxJTCB_F-RDwDAY91izJ19_HgtU59bd4e6c_1ZgVydeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ مدیر برنامه های الهیار صیادمنش مهاجم24ساله سابق تیم فنرباغچه و هال‌سیتی درگفتگویی‌کوتاه بارسانه پرشیانا اعلام کرد اولویت این بازیکن برای فصل آینده حضور در فوتبال اروپاست اما اگر تصمیم‌به‌بازگشت به لیگ برتر داشته باشد اولویت او باشگاه…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22523" target="_blank">📅 10:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fMhGrIc12t8cGl9I76IbF822rhnpeSwjR4iS1yAs3Gu2WYVGX5zD55_KMmdeIhFK0T8CCNF9JfuWvgk2kaA5G7aGtkv5CHiayqKhFNN7CaMG-Jyq3sOerNxR71LuVwhkLzJCDsgc6F0Lpo2BghlsCE_OjIvc-h5F5CbbPHvBzMXw9yfJPrGPSiioezMoiqvXiicAtsAQoVLmDxwDs4jVz5y7mvz0E1XZR4iGcmrMaX1Mal1-JkrviHAwpIzRw8M_nuGuwyUZbNN3u5SJRp9Rol5vYs_Kqxe-GwEIhxqpZx7xh3MtJBDzeIWJu74YehuTdOnM93SWSWVtEFPUy_FCNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fMhGrIc12t8cGl9I76IbF822rhnpeSwjR4iS1yAs3Gu2WYVGX5zD55_KMmdeIhFK0T8CCNF9JfuWvgk2kaA5G7aGtkv5CHiayqKhFNN7CaMG-Jyq3sOerNxR71LuVwhkLzJCDsgc6F0Lpo2BghlsCE_OjIvc-h5F5CbbPHvBzMXw9yfJPrGPSiioezMoiqvXiicAtsAQoVLmDxwDs4jVz5y7mvz0E1XZR4iGcmrMaX1Mal1-JkrviHAwpIzRw8M_nuGuwyUZbNN3u5SJRp9Rol5vYs_Kqxe-GwEIhxqpZx7xh3MtJBDzeIWJu74YehuTdOnM93SWSWVtEFPUy_FCNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژوزه مورینیو سرمربی‌ سابق چلسی:
ابراموویچ مالک چلسی به من‌گفت‌که برای مهاجم کی رو در نظر داری؟ منم بهش گفتم دیدیه دروگبا؛ گفت اون کیه؟ کجاست؟ گفتم شما فقط پول بده و حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22522" target="_blank">📅 10:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یجوری هم متعجب شد از اخراج شدنش که فکر کردم یه خطای ساده انجام داده!!! دِ اخه مرد حسابی زمین فوتبال رو با رینگ بوکس اشتباه گرفتی
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22521" target="_blank">📅 10:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22520" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=KyRlNC9MlB7n1P1g3gVOu713wsYXAKdFg4fEUCV8JK4gWy_rPE8LfOKR_5VqIRpCamNqcmnfrCaQpcDNf-CiAuJVBrJNi7COimhkiJw8cDLpxLQfZ3lidecwg_S7JkxSRh52sHw0lgROeW3Z7pzsXdbykEXnnoQFeA2WGRoDGgHMWEXz8z8CcNw4o489zXQ_QO5FlygBoyFGtOuoI-gPj7DJBsy4tujSYdVshJp7XM4WOWBZAw7zuQQQq-JmqTREvRZYKfVVyZRZ-VG7I-fKvLWDkpeGYyrYfXMpEFKQBlpK4IdyFcwAMK0JjGgfqvUbvc0omGs9OOdqaT1b3GgCyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=KyRlNC9MlB7n1P1g3gVOu713wsYXAKdFg4fEUCV8JK4gWy_rPE8LfOKR_5VqIRpCamNqcmnfrCaQpcDNf-CiAuJVBrJNi7COimhkiJw8cDLpxLQfZ3lidecwg_S7JkxSRh52sHw0lgROeW3Z7pzsXdbykEXnnoQFeA2WGRoDGgHMWEXz8z8CcNw4o489zXQ_QO5FlygBoyFGtOuoI-gPj7DJBsy4tujSYdVshJp7XM4WOWBZAw7zuQQQq-JmqTREvRZYKfVVyZRZ-VG7I-fKvLWDkpeGYyrYfXMpEFKQBlpK4IdyFcwAMK0JjGgfqvUbvc0omGs9OOdqaT1b3GgCyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویتینیا: اونا تا میتونستن وقت تلفی کردن، اما در همچین بازی‌هایی بایدصبورباشی؛
ویتینیا علاوه برکسب‌جایزه بهترین بازیکن فینال یه‌آمار فوق‌العاده هم ثبت کرد؛ هافبک پرتغالی، در فینال لیگ قهرمانان اروپا مقابل آرسنال باثبت ۱۴۱ پاس صحیح، با رکورد تاریخی ژاوی درسال ۲۰۱۱ مقابل‌منچستریونایتد برای بیشترین تعداد پاس‌صحیح دریک‌بازی فینال از زمان شروع ثبت‌دقیق‌داده‌ها درفصل ۲۰۰۳/۰۴ برابری کرد؛ او همچنین باثبت مجموع ۱,۵۸۹ پاس صحیح در این فصل‌از رقابت‌ها و تعداد پاس‌های‌بالای ۱۰۰ در ۹ بازی مختلف، به‌تنها بازیکنی در کنار ژاوی تبدیل شد که به چنین دستاورد بی‌نظیری دست یافته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22519" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22518">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOJv9pBZD9sn5KPGjoB8XxocNU6fhGHDePicUkeWhCy5-BAmTpc2l3vmVeP9gl3gDVOCK1nNgZfrbX43bp5pDzjswMfcdZAEf6U3HONdVQSQHhNNvRoPMqNjKQyhIQGsGUg4TWw8kDbfuTKopLY3axyAcE6Q6PMD5cSMrkxOqiluhZYPNXG2PBnKMr9aa3OndnvOXxPF3wOgh6M6U5JF5GFVeaZHU3wT7qu_0sQ_M4nXv19aUGN5MA8TJfp_j3V9orRTXbNJHcvlA2xXwYmND0bj_iJF5uMRJyRPnWejq5urwPxoCsXPkHvBsMHBmsmSbGLLSPA66DpsTyqR5TuO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
🎉
کافی‌فقط‌عضوبشی‌تا
#وینروبهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r10
📱
@winro_io</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22518" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSr3i4a88R3odeglq7J6gaDvHX64MeK8nmNhbmXZY-nUI-OaVCNM84sHK4rnPgnex8uC10kNI30i89T3ehQbOTvA1jYEgq0C1DPjLoPE92ZUn1kmwqc1v-9Za8asDSlQk9GUactM-PosXd2aIKQVpTD4a93KnWmFiI-b4K4JBGjjyUo8yUH5ZJ9lZtycUiBkyrxNz20bZPacgfFXpXucpnqPsA7Zj-txRxx01ip9fD-PrHDtK2zlVdDwtDX-l_7aeQSjZ7IgMOTjfVtncZbAbMoGa36tYxbzMrfLZbxPcQnY_6wnExVAI28E9KQq3EfkKshvHvDcYylCqW8czr9wRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22517" target="_blank">📅 09:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRGtYcYX-xgxwUSkQzt0fUhQYexxA14oAYzBzPX4rZ2q665QVLeqfJxAADY0xkvlnHboXagmqMAfan7YjPefXQ9IQhptxq69PC6oyTX2ZFIOQJAlzNW0gkSqWggjy2aiO20KSmK1ehJzru2nT25MsSWkHGoa2WReu_nh51Zvp2sG-QBKvBVYvPfheH5AJx__7S9i25qGGFe9bOGgm5ZG9gXVH27iq-UTUrohH4IVH_RfGmghItZTqy53RIbW5KPI9EHHwpJPnwMhHpII21yDjSZaCVW6uUOkhqwl9XClNuCwjjTZeJVskaEQWLlOJ0JiMA70D4PqMS7_KhrWp55e9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22516" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNMgVMRIBOuuv2oonpJR_rI7ibJgXSvto7ZWH_TO15xYV-KPkC_iSkCOCOOobo1av0tG0Tvl_btwp1_5ok4mrpj_XnUqfYCVLiWYQI3P5twTxTdHxbAtS5YEmL6PbgZ_bL0Vd1b3HZYXGcB2PEKy39KI-VLiGoQnqAJsVyH9OsHXju8no0K3CEdAFzOTJWamhu8K63I6cUhl2WZ0iqQvdV9jq1TBDM-VtiCv5yv4dhLRd_dtj5TTvgJr11G99BUadBDItcH1KYwbi-mZrrGyF3tLo77HJL5xHeHzJCD-glamtCop8nJHeaJxwsRQLv5p-UFCZhR7tII6djM1EQ5Qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا ستاره سابق باشگاه منچسترسیتی؛علاوه‌بر بارسا از اتلتیکومادرید نیز آفر دریافت کرده که اعلام کرده اولویتش عقد قرارداد و پیوستن به‌باشگاه بارسلونا است. این انتقال بزودی و به شکل رسمی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22515" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aulmGRz6tDQ-5vyd2wUfdbsGu2GzdAmH2GrleuMJFABplvHyZmdnuDdLEdl8oFGjHBURyZyi_NsyYEOzQu69bfhiQU9TnHGo9zaoTZrwXUyWJ1iOlbT_1OH2V-Nc-nmJmf4JOmJbTKoX08eKfO034ucf6VS3kN0I43wv4wCa6odyfvpUzsj23K0jx7rXzfPRz5YwTvGA_ph1lGmEMAVzEoEMGMx3Lv11I3QUDl3chCECzNc07V05qsw_dKIaX6yCwGvXDmqeeLdgCc3Qn9ESxrF0-x2nVoPitSVFyQnqXac_af3oTnhU-p6YgSjHmwlAKLUT1lwrHHZW5oOOJKdjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
مدیربرنامه‌‌های دراگان اسکوچیچ سرمربی سابق‌تراکتور: به‌باشگاه‌تراکتور قول دادیم که امسال اسکوچیچ راهی تیمی از ایران نشود اما اسکوچیچ از ابتدای فصل آینده با یکی از سه باشگاه سپاهان، پرسپولیس یا استقلال قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22514" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoNTgkR4dcHMXioKaQcLD6M5seqsVa9NTv-i79SVQxLA6ti25liLshU1uk4ccfT13msuf_f7ZXNYwGFT10yJG9IjHzlgAMXM-N75eU7DTZ08Iz_jx294HiFfNHXNFjMpVijf2bBDe5682i99AmWmjRjHaNl5LBPuNj5l2OQWByMRFE4CU084QMCTOvOsq0XOpKLkehm1ibqHjCzDnZQ-Fat4C_JQMhGv9A3x3k9PDsnnaBVl82QoCZWocnDX2rnzGkJPgPZomT6rdozuXS7zgHydJ7uLlCU2RmaEGOekqmdQNEcOLmdbbvvh9HjvXORLVsy5fCvnFne_x1-JtEA_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌بازی‌های‌مهم‌‌امروز؛
آغاز مسابقات دوستانه ملی پیش از آغاز رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22512" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXjcD6bZRTo0KatSJrLD6F3t6oZ9Hv065CH0JtU6O_660pmcJUhLBMCCEGUye-aldBESsz20RtlHYLDQ4m99MZlcclhzbshgAXFBsNWsKNZEWGvcBoWyOSXfGjrohi6KfKeQvtdFPbhR8hzGMKQqADYDlWkSFiLgR5nSB88mO66-t0DQWF8vtGoQezeC8WCgYb02b90_m1b2mbESj1AQTtyunxh_8inGZ2kdAOWRqC3-YCpIc_anHO1B5ZJXx89mpsRY1DYJUCMAv3CUHizXJ9vJcjn7bGI4W_bL5ahD_4CsCnm85ssoXa8yo47-xcvdKv5zk2W4M47mCHQZa3OcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهادیدارمهم‌دیروز؛
دومین قهرمانی پیاپی شاگردان انریکه در UCL با شکست توپچی‌های لندن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22511" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt1bSjJ8RUaie_NuoeqVKUEQmll713ITtsljaSMaLBpu7QgpDv5DZgnNVLT8SFC3DcxQpD9kGuwd7pjoWNDFLIaZP4ISUQfr5jKAmOHyKlStud7RkFSjy7PpQG8RYz5mnUwED8a9ifB-PTC2uxtwpQS0BRizjjT19TkOnrHlno7HbGy6-_TSwYFZZes_rbTxdM6RBMEt8ak5Aue2yrwIUNNubtvN5nrNg2IsKOuwaIQwy58ev1Bv37gFerHumK5tmrOjG8MmNb14sH5zrj4WzvNjMhXxewE9XzLSvekvH274PwY60GhG0uAtPeFow6vtp9D87pFyvSDD8Eo9Yi7mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های دوران سرمربیگری هانسی فلیک‌ و ژوزه مورینیو سرمربیان فصل‌آینده بارسلونا
🆚
رئال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22509" target="_blank">📅 00:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXCd4xbvjB2xJGzXjwnBLaBn__r1B2fL1ZMYJ-lsB-kN7dZNcJxMGEvF2KeYEDA7i90zPpM9g4Vrg4Tmu4RFa6JPgQztNknBb6SaopPqSKJ1kgJ7sAJ81LKmEomimcpvF1UEwaqD5DNOy1l84_R1TPcCvrNwBI__pM2fs2B20N1mI_4Rn0PaIe1nJsG-YevLy-thNwrMulTQNXig7f11SLepIfKxjZCOeMOUr6b5VBtc9fdtz7QEFP96yXDqHsWZH3L9DWRzKD7c9wOmvlbOqCgJPkqZ_dOX3zvDBhqGORBGKKS41WoYgDU6XjszmBwHJ2n6gn2bdkJ36TI3Ny1pMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22508" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2be4rvZaaoqjW8deEFnvmBwGCHQ2PdVvXScCsFcqN4IRA7UaRilEyjRZPOI7lWdCbXNfeUgwyg3z5dqGXTWExL2-305raPyknUocVUShzFMpeceNadgyQDCI7Yqdx404NqqUiqBLf4DjsyMWBxOvF5mKvfkpTsrWWuS2c2fCjKvbdK2T2MDlR5MWNKpXIARPkbKu1p1ewf4JtaXf5ck1wIn86Fm0EKVS5BIxGD-1r7hNdv0Siai2U11gC4-zGXIQj__YvdQ4wQD06WEi2Caw9BqQ-K7cCmaY3XFaVEQkqXNFMbIEhaxn5TO9rqNKc3aJBMIc5JZdZn2vQSBVkuc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تمامی قهرمانان ادوار مختلف رقابت های لیگ قهرمانان اروپا؛ رئالی‌ها همچنان‌بااختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22507" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-bqJoQZkO9IoaMq-t-gmiaxpbyuG_y-wYQv5ipDAC6kqPoHKpH1Xak692hzSm_54TtHSBAxObBGJ5IzBBK-1ZNMxGwheLaTOIb61dY3p9CuPrW9pcJeNjrjfi10hb-n31znnNk5l354RSHUqhFDRN1W5mfo0j6TzMgt8eLEWr4U0zrFGK3RuD3hf7ylfOeegq2pYYsgqzPxxWTp6MreQEpabmGwZ8_xW_yXtF9-UV-7BDnNRuq_v1GvWe7HQ1aEJI14-o_xsMuzV_556fJZ-yWdxZYZ22bMZ-BkWc-ovE7Mfu40-e3szxDKYERZ_MUrnAlgX9Yu55usNsREW46BnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22506" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=o_hR16aP4uWzQQ09y8HZ1TN5XraGHn_1y9VvshBLIh7qIFhyKQ46fB6AMbB7jZ3xfqcFTEDdFaqMkCjsdmVCybLt_0Y7qq1oydBpJNfAKWe9PQa3tXZmz90JeYnS5PaX6OrvOsI-umL9DPDDgzOsOAMXIYmwh_7NhQNfjSPAflXw0hcAyc3AOp0Q1yGPWomtzTkNFq2eIc_G4dkiS_9IfBsHMcL0JfzxxwuhD6_0oq8X7slgyUualjcKMNJH0wsT8BP42tf9Mwc4x55gjp2o4Vd3qrY1Ue2nq9JE4ymdlLC3A33jxazpYPVhPrqiILQUP47FBS-C2xFppAteWvzL6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=o_hR16aP4uWzQQ09y8HZ1TN5XraGHn_1y9VvshBLIh7qIFhyKQ46fB6AMbB7jZ3xfqcFTEDdFaqMkCjsdmVCybLt_0Y7qq1oydBpJNfAKWe9PQa3tXZmz90JeYnS5PaX6OrvOsI-umL9DPDDgzOsOAMXIYmwh_7NhQNfjSPAflXw0hcAyc3AOp0Q1yGPWomtzTkNFq2eIc_G4dkiS_9IfBsHMcL0JfzxxwuhD6_0oq8X7slgyUualjcKMNJH0wsT8BP42tf9Mwc4x55gjp2o4Vd3qrY1Ue2nq9JE4ymdlLC3A33jxazpYPVhPrqiILQUP47FBS-C2xFppAteWvzL6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اینم‌نسخه‌اصلی صحبت‌های امشب عادل فردوسی پور برای دوستانی که قصد استوری کردنش رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22505" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=lfw_ECTWvsrWiFYrsmLJc0pxXaXtDesEwxsHUTWPOXtnpbmLZ0EX9wKZEkPBWwW4-9zMRkeWEJx2v_BAYHIIDb3cpBkvWPbbWg833DxzvhA1sj8V_PX-YXsLb2AZUNab8Dgj6o5_yjQgW2IGdBfK1CcFF8D_gVLPaTohEh8EzpMazr7nZn-EqmA3ILAy3ecawf_Kf2p6g7PB3xdB9K27A0sCP2bmYvCI1QohleMt9pL_KarOsNajJ6uX_Hj0cqoaRmrteNKY-lkYRvcpeuOON7fmNmIgoVBQ4HbpFw7pjzstwU0GEWaLub-VVViH7NxRrFP3AW_ipvwXyvDs5Z2P6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=lfw_ECTWvsrWiFYrsmLJc0pxXaXtDesEwxsHUTWPOXtnpbmLZ0EX9wKZEkPBWwW4-9zMRkeWEJx2v_BAYHIIDb3cpBkvWPbbWg833DxzvhA1sj8V_PX-YXsLb2AZUNab8Dgj6o5_yjQgW2IGdBfK1CcFF8D_gVLPaTohEh8EzpMazr7nZn-EqmA3ILAy3ecawf_Kf2p6g7PB3xdB9K27A0sCP2bmYvCI1QohleMt9pL_KarOsNajJ6uX_Hj0cqoaRmrteNKY-lkYRvcpeuOON7fmNmIgoVBQ4HbpFw7pjzstwU0GEWaLub-VVViH7NxRrFP3AW_ipvwXyvDs5Z2P6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
صحبت‌‌های فوق العاده ارزشمند و گران‌ بهای عادل خان فردوسی‌پور درشروع‌مسابقه امشب فینال چمپیونزلیگ و تسلیت به خانواده‌های داغدار دی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22504" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVqUl8-pm1K0ZmfQEVRFM9HTiAwRj-K1kiUMIZWF7Prw7ketzkEJXWdXvXN-k-rnEwFnPZxdSqVSNpmoNZ9xGxm6GhTEtcaCsdR-2H670xMoX5QzLn7C9Xt50zBMGpKQ9CToCF-2ugmvNsSLN9k1XcEMKpSw-j753ue8456GBpKkJWplT2O1hE7gr14xHst8WjYR_IZnA9O56WsSRuu_OXfVP34pVer3SPnhvNPp1Q0PkL6wPk48FKZ7IyOxasXH_5OA0DMNRulT3yFsOEgdq4YmlyVZZc610BfFOhMtPoYY-illU_AkF8OiqDLKhR9QpENuRdP7Mw4f_KzPWQ0Xsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22503" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22502" target="_blank">📅 22:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50097d1448.mp4?token=AmK-YuSJExVzs_pengBcrBiKe4cPYemvkHeRFnDAvgGe_p836Ifuyr4GOSh_ev-iHVTFdIwrxQALOOwJEDeKd8jlYU-23BJZ-QOLk2Rl1sk66kWVgNEaf_66v-mZ9WCakGakZah3C7dxHOGDrNXMP15xdfLQLYJQ3vwYBFPYN00jEIcweqsaDt82lHL2fxbD9ThV6gKOSV7_2JniHIms5ZXTFnnStokcxijYR-mJ7bS4XVT89mAGzkbyZN-zyQFOD1KVKlngbQU98z2BKcayCrMYGd8s-lnsNvsRm_N5_KawvGc6CjMwpzjfH6moPgh0XZgvd-d3ApsLU63RtQgP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50097d1448.mp4?token=AmK-YuSJExVzs_pengBcrBiKe4cPYemvkHeRFnDAvgGe_p836Ifuyr4GOSh_ev-iHVTFdIwrxQALOOwJEDeKd8jlYU-23BJZ-QOLk2Rl1sk66kWVgNEaf_66v-mZ9WCakGakZah3C7dxHOGDrNXMP15xdfLQLYJQ3vwYBFPYN00jEIcweqsaDt82lHL2fxbD9ThV6gKOSV7_2JniHIms5ZXTFnnStokcxijYR-mJ7bS4XVT89mAGzkbyZN-zyQFOD1KVKlngbQU98z2BKcayCrMYGd8s-lnsNvsRm_N5_KawvGc6CjMwpzjfH6moPgh0XZgvd-d3ApsLU63RtQgP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22501" target="_blank">📅 22:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw0Xn0Dnl8T4C-4Hajg7BRrYPJ7FhJdG-EHgBBtgxyeFUhzua79tnlCCSLEMKcxY_8z---QsdF8zAtbx_ZxydaxKwBrtnr0gqn6pl3onTjGDAJiWz7TanUrVQ4DFex_T7O54UZqebejz3q6RCz7SGQCTHETIz-oVx5u1d3Zsm3cVRqr7xPDPgQwYRVbKf3zlgFUDG7dP6WcwmSrTO0lqdPjpIJRCwe8dOpNdcjume1gRlghmiU2BW-1JaVxt8tLliWoq_ot-dbNyMitrEx_9BonVRf9ta70eSlOEP-8BQPIKUx20YXLVQswXBhy6Og5q7p-6PFVU6QS8CQdGTpnLEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار فینال‌لیگ‌قهرمانان‌اروپا مابین تیم‌های پاری‌ سن‌ ژرمن و آرسنال پس از تساوی یک-یک در اوقات قانونی و اضافه، به ضربات پنالتی کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22500" target="_blank">📅 22:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToiAddkCBUo5GsIZMQwfc-FSRTE2CHn_qF6_5d9AVWZZOp9OD8lPnPt32fmjKhZBmDWjGSrtKAERS0U8dqVZgEF28X1Q3K3iQ-E9epqJPH52t6Pj76N4s9tZ8it-eATj212O9kbvGPQtZ-7Z3S4nI6stjE-80yUMFIKvNhd-OItgpgfTs1nQKt1kO8R_5dQ2BYd5s8moImKmn4WDOFrEl9j-N92dfd00d-zym66NNcJFik6qyFNTkP_XWXa6aDC9_capP7b7hE9eegF1KRea7ogeGYqAPRyZdtAdxVP46-O7tYVWMVh9736eqD50jiD7pfWGYe6vJ3tTGvv96-gmtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازی مهیج و دیدنی امشب دوتیم ارسنال
🆚
پاری سن ژرمن بوقت‌های اضافی کشیده شد. آمارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22498" target="_blank">📅 22:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdH8Iyv9r_U6TKc9KqqsMo3j9q2zrGfbJUKeT9vlCF8mWS51EAN3MgZZgjECd87piFFfOfpF2BNSXcpnpiBqajEoOBZ1ZqDDA3sN0N9H4EROSrT6Rquh4QczC62uhNodfhifVdxqf-meazYcJp41LuQETYNDJYO0CIzi73sFWtUltQO91IaGmMNUbX4jEyp2x0UWX5NGKZoa60_nTU61kNXs3eBoZc-mlQ8dLOMPKnSXCqbWDACz7Rv0lMR1QXB3IIW0vQgX9cJ_txHgt9vIQxGfrhyHDZx9z60ruLdd-a6r76u6CM8LQ-W8RPIJjdLCS9wTs_3D17GCxDaCwt-SrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22497" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa9tiZo92EPRil9zMTyUrfpJIuf5BsTWMFnm2Z78rfXDjECmovtBLZe6Vllz2WVALWqoo730GseFEfjrFK-36P7ZRcBtL4pEytBGVmKKOnovaW1sJgQl8iIVfYSvCOYRTBKo_hGxvsKiMiJ0n9L03cZMhyLmbW3eBB5YK9hfGW80XvZUg7dE1ld2mDCgZGIm8ezBCT9wvfoq8B_Y8YDhKMX7d16_nd3awaIccvAlKGk0LpaWrL0J1_3oxWpqDcNphOtLPIyJSQM_qZDRQTVisvPXtZOOtTSytzGE7cefWwAAml8HMRlqMcOc4lo8toQ3hNFo1RmKer4f_Gk-E1elUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22496" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KivYlUPl4UtTKaczq3BT8mCOiAZuq2pqTQkUBhXg7dykWWaBoi_vUM-jpJoiVbNh0AynCJ1TcJnAG8G_3wQVjq_gzRP9p1LbpsK3UJh6WuPiFE9hcjPviOJ5STBNiistJ4kwRhE84EaPV_JP08tELDrv7OtSAdGy1syrBauFDU6__QM3H4p1heRaPd-Uv4qWZvRq0GdeJUJ0SQGhdMrfL5xPL33YSr3sC_FB-OQu4M8kXMJch5YKiWKO6z-zfBYWiYRBCahzNS-m6VZhwBZy7cxChb1suCZQJVQ547eo9gzxr6xizHrwQuLsvDiyDnqroSSRKUdWPZLXbLc30fF2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تنها 45 دقیقه تا قهرمانی تاریخی آرسنال میکل آرتتا درلیگ‌قهرمانان‌اروپا و کسب دومین جام ارزش مند و شیرین فصل؛ جای عارف خیلی خالیه.
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22495" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZXRUnJoBOHGEFYhSPqa0a9IX4x4zDkGecVcqtFyFs3tdPG8_wVPIrk8jyOx_pTCdTWH_mqduoOEa5QjdqhWopon81itLPvptJGIsvQeqRzmiMzOSh0-RSqEzBcaINHo5gtoBfMKqjbwZnpYYnOSC3d1s7CvbEWqwJZ06hm3xkwxSInPnGU4VhW-0ZIR-ALSL0wYflOYP8TuOwtXioUx_7PjIqloyO52VblTH0Gh7FOCA330K-u_6JUYOj20d1hi-5DnQiKYN2D616oU7ru5_kr_OCgYD9toW32XBIZlMo4Xrx3s55qhYrffGN80rO99YXNITEPyGUXwrXRKP8OKSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22494" target="_blank">📅 20:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTfOYimsHbY_J7yhknwsEviTsby6JIMKhQKjN93plIHImlKDVkWFfHXAvNaTxbqMfsKizQA-rz02pL2DetCapDP56mfDVP_04Fhg16xxEuxgvT0hLHpbzCkZY3q31Fsie-TPJ9WDv1k4xY_96cVdw7SmVo0zaKJcZ7cmbxVvmWlY-9x75WIgLb1iJZilAQgG8frYZiMMHOIhean6oBLpeYPyW8lqPDS4pL0a91BmvYSlS0dxo67Tc5YckgKAgtH1hQYynFzIYE9kOQa_m-dinAgJwMorkdDHjJnIymImAtvUn945xkcjElFEn3rXnFVULoGX_5xsuYDGCjEssTJ3_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
علاوه بر دریک؛ این‌مدل‌انگلیسی طرفدار آرسنال اعلام کرد روی قهرمانی‌این‌تیم درلیگ قهرمانان اروپا دربازی امشب با PSG پنج میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22493" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=hei_kiNZaDQhu9egtZFE3LP2MwCfs-k0VBZzUd5jRpicDERmUkn5Gd6l7zn_91mAaq3LqwviCgjbWEHBVU5lcGhErZ62WHhjFUMNorYDOfvfoeYLCIlb7Qs6l4drUeAXhRziC0EG45rebt9N4oHe2U1HNKr3iMwWLBJIaG09ysLQHbEpVQJqYFflUdIw_SpDrW-YeC74OYh0YCji7Tf_l_re5OraodGtz5DeJTDDhQZKyKvoph85c7jGPil7m6EkVHyE_fJ6h9JmW2iZqTl_-tiumnO-q1HvngQd2j--9Ha4ttQDROZbQu9asRS6uMMBT-0Lxnj7nOmAALZCdLs1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=hei_kiNZaDQhu9egtZFE3LP2MwCfs-k0VBZzUd5jRpicDERmUkn5Gd6l7zn_91mAaq3LqwviCgjbWEHBVU5lcGhErZ62WHhjFUMNorYDOfvfoeYLCIlb7Qs6l4drUeAXhRziC0EG45rebt9N4oHe2U1HNKr3iMwWLBJIaG09ysLQHbEpVQJqYFflUdIw_SpDrW-YeC74OYh0YCji7Tf_l_re5OraodGtz5DeJTDDhQZKyKvoph85c7jGPil7m6EkVHyE_fJ6h9JmW2iZqTl_-tiumnO-q1HvngQd2j--9Ha4ttQDROZbQu9asRS6uMMBT-0Lxnj7nOmAALZCdLs1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22492" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpDr5qKTDji_vsdGIUN_78hAmzYpc5G-xOCuaCDo4DQvii_Q2kWY0dZu9YNrPA66Rti1DyM65M7P1LqCDpAtfz9y-Ob50QG_O9JEYQYs8v2WrBmwudCFooce_v5MKFvnWzEo5tscMbVTGcwtFcTvklRnVFiBPokAtbtPVnAgFInLZud7auzDuGfV_uF1xIrUQ3WCzyNfboodzNvs3VGs_jaal2wnaaqLo1WWA8DUfAJjKMvzpyTroyZ_hYZoMkD2lR7sSadkFlZJ131LJFWW_Z_o7J2w4yD3EMgfi5mUIvae-vw-99hf30fFA_TBgbgax5_PXbVDXKDuf1RpPC5rfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22491" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9qLKrXXhlvOmdC_2JEcZzoxW04INmbnjWMT9-_avnOqFPem9OdwkiGGZWWs_OK9p0BGpqm5jhb6_Si2Ir3q85wnycdP64Wx3wdP5GnZALxBaJL46Po66dRuIHuAc1r0jpn8UqBWfD95TOTSrPpVtu-9XtTnkeSRAwDu2C57-UXzCL-Wj1WfUL7o-LrLQS63xS9JZtZ8gRxAspraVlILDWizcNGcn_w2ZaETAxF_FlcYGckG04Dhr2TOraFt-Cuo01yYNr0ENf3HPWoCZjQE9nC_5yT8K0PuXNr3p-9MY4Izw_kJwAGkunjcElVgL_zflAcQ86prdNborNVPQnr-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22490" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9ZR4DM4VYRQyBqInzYPsy5Pos9Zm8ez9ddzSCqEBxR1WLjuNu2TGAQ3duUolw73be2Uk7z_75xX4M-PJWl962H7W2OsVWcJ4PA66vbwrw0T5nfIZ4oaNocXO7HTAdHhHo8ZjvXXHNwtkrqn8L5TcL5BCc1Av3O6DPEHc5QOHzS3U0QtP8Df10KKA7BH0MPKYq-tuJCdDzb2SnqbctUXx09PE_mla_nXoiKsaP2MAuUPEw0Wb0fr3sa0AjpQE_-LwYsw_Bqi_-7hcUWupeSGIO-fPfjYzSARYy9Zrl0FhvbCTvmPEzg1sGa8UEhWMjjCiDLEK_8NnCKbNqkYXqSfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22488" target="_blank">📅 18:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5gfZ_F3MJtYE62rftSZmyuDGHZOofyQzwg9JCjCq5ajEak77YdrUHcuLtTfsdx1zpX2rtXXl9kRfYuEVOlzCLAlwgdNyGC2b5MPjNC3x4uG9r7Sb7rjt_x7YbIyFvhTPRxgAaIedfo47iOrN7zeAtE4SDwntlK4gMYtYpzNOLDV9ADvQUXeH_Jci3aZcqOOsG1FQoQqGKqWl8cf10I5CCN6cvljcsCoFcV3lmr8eln4saC9GwFVUYOQHOm75dKf919GXN-Qgo2_hvsg8dRtFd9CS9uz7tnHL-DDPS5PpFd11_oDXcxM9v0ApS3y_PqZ5pO_disCYByb_eud2wFclw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVHhuCLbZYJMPLtQfJBdp2y0b3cawfarSJIZJur33QG5laEJ9mySRBv9cEFAIdCJEaxm7E98GJTs088Cd6Gg1IAAvgxKJX4ETgVsJGrGFbvq6gCf0QM1kkAy63yNp1--7flhLH83ec-Ie7yblgI_iLCqI3lEgrYloLiMYsngVmFLHyzT-yDUxlx4ySb0mA0uLviHewdyl6f0DcTBwm1kpc0EjxwPVCq28h5s80VLIAhSr7axUrCveFXR3Zbun77qeaBvMpGWN4oXFdcuX_RE8tgqdYyucdciYrUe0gn2QdYUEiMcXJ0B1wDmk3m3Ii-fk1K-z2orQrNpnVdAlYhL_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
شماتیک‌‌ترکیب‌دوتیم‌پاریسن‌ژرمن و آرسنال؛ ساعت ۱۹:۳۰ با گزارش عادل‌فردوسی‌پور ببینید‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22486" target="_blank">📅 18:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-502O43zvCuQ5MRKz2v9-5mp9y6_7bYodnDl5vmOh4WXj5WYw3FMGBnxtc5Xu-bVkgMWPenrE5ptDLOAvafoEXPRQcB3G0IjhIeE7cZihPJbb8JrsBjn0Cz48RlGkI9fm4wDaKe8Jskk9cjWKDZKsqT21B4oTBIwaMev1R0jD8Ceqi0-pfE7ZFfrAX52G5mOAviYP4xNb9NoU2ByasLIRhmn_ipM5wi-HlpTK3zKSpK5auq9C1z5VYQnL3JmZ685v1RQmUeN9r75V62A-mCGs53vZ9_HcvMP_0ku2-PI2JpCK7s6HF62dAZRsYHBWSuIBZ4BAZLJD9AqY7C6E46_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTeFL3LlYgCTv99rEo3NX70Hq98PUktO_2toLZxMY6qRjc5TABtVvcTcMe_OA-5X_v7WMlNJSK4i25eJSjT9mcd1edZcuiArZuXWb7JUUllki94i8IlJqhLCrbqEP9Fzj7L6gq_jjz7D2FaEBb6nT77XVitw0oprZjq5MsbHMGzln4uJJcGdWeq0GLljqnhrsD8KAt54diwZ-YL4l4z1Ax8STIXGoaoUh8QpHfR79NX3u0wDJBa6Wc8zfIISCdyjpcY4Dk_nTYKpKD4W5kUpZ5oFTh-x87LeTbCGc3gg4cF5RcYh_k1HhSkjISRhr2dAL__rJSVollrUqPoGDflalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEp5nxdH2m3fCHxj3rtAFp6leGfP17j-_OqMYvhpnYTqxqTt7J_TDOPKDxpSFaiJcnAe9207Ru01BxnrnwlfX__nXPVVPfDuE8REhOhyqTndCe4mVvc9NpfYB9OFiqgwblph3F74nr1kPYIgaUWrO-Ri_vkhusxkX1zxjmKbCN1dm48s5-Np6nsm34X9VA6mkyzkggQd-_YuSX1KC_pkhKDkT2W3sj4xT2dDU0PIeGFQDV6SiTyncsRjBzgiqNP-2-XjsyqGeQWTa7qf43ImzC4fIR7MN-GGE4iKbvuXnifUpLIhJrt3kWGnSkpRfdmFGR674w8WRgB1e1dx67cMuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22482" target="_blank">📅 17:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aparat Sport [3.6.2].apk</div>
  <div class="tg-doc-extra">8.2 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/22481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
#مهم
؛ رفقای گل این اپ آپارات اسپرته که تموم بازی های مهم روجلوتراز صداوسیما و با کیفیت فوق العاده و با گزارش فارسی پخش میکنههه. یه قسمتی هم داره میزنی رو صفحه میتونی هم زمان هم بازی رو ببینی هم تو تلگرام و اینستا آنلاین باشی. خودمم ساعت 8 نوبت دندون پزشکی دارم از طریق همین برنامه نگاه میکنم. عادل خان‌هم گزارشگر بازیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22481" target="_blank">📅 17:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22480">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyKJEd7JuBLEHcLPhq_j4eJfq-nW7v39g4r_CrTo43b31nbtDapc5F2kJ4ipfEpeUN-OLkqWHKRTgD5XtUZbPcOs3Iyz14bsYyJ33gYnv9qMYMED5y3ToCeV_vFApM_KO2Znjj7rkCdN5iVB19Ll7qRsncnN-2BGyPegHjJtQlw4uaXZ2BdLBjo7xxbxkKeSQdxBamJhSS0R_XBxqnCYe8DQQqyLhBaX4GYNhRjgwz5n8XufWIbvVBOdkGj0bI5NllMGvwVjjDXzChrqZ7-JP_UYElQn-hNH7n5wviiEsCgWf5SNF67iyKbX5xngmO-7uNgPJT0BvlkkjmbMoW-NqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22480" target="_blank">📅 17:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22479">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=JfTswLWcHS55TOr_QGLo7-h_fKejxDr4l_HMkcBhoU039SfnUD599tzlR6iOTILeExmInTWp_oO0BKNuz2wdKQ06gQgVC--B7HqLwsv64M45WCoVrDXQPdCxKHx6vcDXXLUG2Ja0GH8BUSqZGP6EstjsPiZb1x_poj0BE5dpjailsPg0EKorDza_k8g3Bio0DJZfPpXy2BKm7dnMYlrjlgiOGBjKlJnKeAxN5PnFXrZouoVdTI7npwbGyP7181D3dxHzTL2X8DjGlqW3tD9tGgvSk_JPYdnTR9uzXljauNlocLWViSUXofCIJuWXvdwlit4Vo_29ODC2ipUCmomIX7JB3IHez3gHoNssl5ho_FQxkEXuEW-KLOr6lFthutnIgeDJ5PTFh5c1Vj95ZMPpR09BlUq7O1B3gM_txUUW-sf2ccllchm0VaEXngj1LxWZI5_1N0Ym9SbDmDlYQZnOp-o7sCJ7zK1U1OcyM9SZfzfxUQNujg0UvkktG2Ly5bZvF4pLyUP4Ikva_sfxddktORvmjYSCtpx7yl9jUm84EMi_PSSR9bkibg2O2j3S9tNtE3gOFzPXNphVJQS0gcrG9JigrTeYN0ILR-GSaMqLTTT5ClNI8kbgprIFbXNcigihfIrRraDTiskSYuVxl0VEQkvYhettK0gUkz4Ihhe6Ljc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=JfTswLWcHS55TOr_QGLo7-h_fKejxDr4l_HMkcBhoU039SfnUD599tzlR6iOTILeExmInTWp_oO0BKNuz2wdKQ06gQgVC--B7HqLwsv64M45WCoVrDXQPdCxKHx6vcDXXLUG2Ja0GH8BUSqZGP6EstjsPiZb1x_poj0BE5dpjailsPg0EKorDza_k8g3Bio0DJZfPpXy2BKm7dnMYlrjlgiOGBjKlJnKeAxN5PnFXrZouoVdTI7npwbGyP7181D3dxHzTL2X8DjGlqW3tD9tGgvSk_JPYdnTR9uzXljauNlocLWViSUXofCIJuWXvdwlit4Vo_29ODC2ipUCmomIX7JB3IHez3gHoNssl5ho_FQxkEXuEW-KLOr6lFthutnIgeDJ5PTFh5c1Vj95ZMPpR09BlUq7O1B3gM_txUUW-sf2ccllchm0VaEXngj1LxWZI5_1N0Ym9SbDmDlYQZnOp-o7sCJ7zK1U1OcyM9SZfzfxUQNujg0UvkktG2Ly5bZvF4pLyUP4Ikva_sfxddktORvmjYSCtpx7yl9jUm84EMi_PSSR9bkibg2O2j3S9tNtE3gOFzPXNphVJQS0gcrG9JigrTeYN0ILR-GSaMqLTTT5ClNI8kbgprIFbXNcigihfIrRraDTiskSYuVxl0VEQkvYhettK0gUkz4Ihhe6Ljc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این میم دیکتاتور داره هر روز سمی تر و سمی تر میشه؛ تاثیر کیلیان امباپه روی هم تیمی‌هاش
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22479" target="_blank">📅 16:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DC_1T_5fxabYDEtx8GnnTmyak4ShRNLtazXrX8w87hokv3brKCXeErI8509ZjzV-DL9CTik_rDo_ZeWQ1fMfcZxUKMVP__vxhcdxDarAnd0ukTw19cb9Q_pIIdjxy448Ll3lDNtxzhFi53J8Np78GnS4hldkU0LmF5k7lrRpTXdbQKS-YzS1sg0WGfYAyFGLI9Ch9diHqnIt3ZWT3ZQWumX2GklrFENP4Ta9wMmTKClQaNrGU57wYrCPl9f25VBM0z5kYqBMZ8Z2P0GvOc-JZewlqf0ncVwsgG_2k3aQUuz0IjbK0nZD8GGr2dCTFtKA0irb9ic_DsUBUp0iC9dFzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWvxe9eQY6NycmZ-PInWjtjyqH-hEQL-t7bkSP8l48pNK3LqI71GBRk5XBq86H6EdDyHZkTSNHUJVuB-rW1yA7sD2kqSaSoLr1qXH15fV_Q-GL8XWKlnYqMrKHCycNCQz9ZYQdj7POvWc_QNZXpnYEPjaLQYzNXQt-XWEBtDv1LJfDMKcFLc6XKqCY0aDb3odwMWMGZPKrLRaRjayZUWJJeBDj3HPBoACz0ItyiJtfxmavixpv2c10ffg2peUgU23fK31VwE2JHJ1hslYdV7cc9BExTaxSvoZeRuBJFzJJbS3qtIm9FMih0T2NERlZF2lg4HX0FqWK3oh_SkIFddsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری‌ و خبرنگار بازی حساس امشب دوتیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22477" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALAZZqylM45-74Vp6XtR5VNnKwuhW0mPKZt-7kkIPYW5jYz8UiM4T20fYwgNAA0zP97zO0rUWQZUGbeT_Me5G2TCY92pAZRBeBscM_TTLtbelZvTNEfvhyibclI3nvcUBpFoQWrl4_WhOMFfI5anMWjodEe677ObEBndonR0fzBYDbJkp68TUTXFKzMm7aGSGpVOl-X6Jr-hNhy1Dd09MzZDqvSoWj6ZuylVAUTEns370wtVEq1E4dqsns1Ikl4aADSw5spGoOPB7ARcA4zMOZsEH5Qg_9WEoCrtorRm3inWN6LgkLIUcHMoVpmwBcdJ_AX8s6AxlT2ydx-uPnaf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=tCNtn_FCKUUwy705EZAS4t8GwnyiDjaIRmP2UoW9u5wS4ujlxBnM8JKBAkZqmKb78CRUbGIzHppujn3xbQUVI1IEOUuXuUgmChQm7tBKwS8llhKFMvtLdooiEoLj7iR2Drkb02IoxBOwiIxAaOIS3Ycmc58VfbFqestbKWpm3q_MbfX-Vq4dmwkVbeI7oYtPOipPOmg95xoxeGcpUZQiP5aPDvFxpTkiaIt3oMqJvoN1cjPQyEP08QfDwCAXvfdzTXlw_rXt0e4xMTwqddp8_auOwZ9ZEqZZFtncoNz0gcGiIb3x8Nna1Rbp66auE0wTa_ogH4K-8kgVK4mBR0zADQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=tCNtn_FCKUUwy705EZAS4t8GwnyiDjaIRmP2UoW9u5wS4ujlxBnM8JKBAkZqmKb78CRUbGIzHppujn3xbQUVI1IEOUuXuUgmChQm7tBKwS8llhKFMvtLdooiEoLj7iR2Drkb02IoxBOwiIxAaOIS3Ycmc58VfbFqestbKWpm3q_MbfX-Vq4dmwkVbeI7oYtPOipPOmg95xoxeGcpUZQiP5aPDvFxpTkiaIt3oMqJvoN1cjPQyEP08QfDwCAXvfdzTXlw_rXt0e4xMTwqddp8_auOwZ9ZEqZZFtncoNz0gcGiIb3x8Nna1Rbp66auE0wTa_ogH4K-8kgVK4mBR0zADQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fyn02ucFY4kfe_rM2lrTq0Q1Us6R1DKy1XQTTvCtIZ16l96uhApOFQycTwzEJr54CuxB4bA30x9-jJ5TkcsALjxBV6VWwe1timHJtds_NlY2Y62zmBhpjjhtGldBuD2cjhVNZLWbBRqhOTpi8SXp3-SUouQ-MQ8FR0swZQy9N3itNbozWpJLORgWEZJrksnP3J7maC35ivazXAAeOEiEdIZQs650l_IHeKyQAx6fbfSD9eX1REslXP1JPbEkIQDYHB5moreVimgb3IDUCtvpe9CxWZsN3DFiMIyfMkiFTgtqKkQ1e3OQk79lTYsrCKasUEXRLGocEckVnrvYnNUXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb_qgz-fvalnHqvLHyaP5BgvoUAzwfQm6cP79KAEaGIX85m9tyuLITjs9DAcCV_SZfRpYNHfGuwCsDgyU7q20gIDZ8FcE45YDUhH4tumGZ8K4arjSa1BXFUCoPDgfm95Wq-AyPHXl3_7sZ2f6v1EFWZ5EnEVuZydeXhxoX46F4maao_mStESUNj5moXF1SUJGx2XnIgCvkdFPzulF3h5O1MD2VfqNFzrvGwuG1bQ09-UO123q2vQ1PWKiUo4Q_2DkTHaiUQ1laKPaOPrZyx0BTXuQwvIivRPIyn2JC7OjYWWDPlHB6iefqqdw8H55L95LKxaQ46ML09CwbgRGO-Fyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmzfRYR4HOOH74s1ihAoOcxjaRIMBK0bUT6O3aYz_OQ6NYfWuv9rtkYKDoXSusxWkjcRS6Ho7-2LNjCtsPBUi84jtIENW4Txl3L8t9pSfEplrMnOkliCPTpbVcv6uR4D0JgG1uLM7hp2cKvqzJQv8LcXoZBAKQVd3Ypr-16M7EGuqMRehfdoKm5p0IUc3epSPnBUSPATKgwiilqpzdLaULZSIrtGBqJaslTMvj8SiAmKuJuHfL2DRAM4XBAmaeauZxa9fTWqvk95b_7xo8tdhW8RqUE0MFHMNDIP0rZlkGhkLd7Io-s5UE57veVN1XPNK2qw11X0oVnyzghyOGc0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF0kZqWHG6_uSVX3Gghl5Wg8JKglzP90YbsogNGp0h1UrtUuwAHBN782Ho-aB7FfEgtSCPJ0-kuzBVSDV9odxhE1gwLVqUVnZEdE3kmgWB7ebeI3mCRul26YXNz9rgifCn-R1UwvaE_ncplqFJdooqBD-STi6PMGZQDBmD45XYBHB3z28dgpgt_flRLtxxGqJOFnUS0u27gMLUJSG79U8qG1p6BIXJCUOplQTcKPrJ28fvA3tzy2fvgMdR0LFyIG-FttKIVL_3IMK5wE2AU43eQr9KANH1iYGsNkszBuCYSmsy8vfj1MEAW6lep-pHhio59sb6xV8qXQYO-koBDaTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFqnFOyy4KxZuRii7OmnMV-eYHY8bpmKDMpbrCtQZuIZhYazyo1I9BRUUpwsqu9dK6wyJfNQVwyfPNMsyeWk1mD9IfMsaeOiF62le6MwlMkuvVQU3CXZc9MIA3U1vwwbxU0Qg_-vXwIpeLTlPZaNuQphkgINzdVZMMxhT1O85iiGiagGcCEWofuMzD3PVuqnCnv2QN1kufTyygwYXJc9543zqKYU-HfEgDseM7QIXQuPjDkXwBOMytXYzlr4PrdYHlxL05FWjMJLvB3OBDyjWPLtkHrli5rrelM1exkUVGZ_hTcZV1sEQzglcZzoFKdTjvrXu4xMgm2LAAS7wmv3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-1FevKzOSose1u9b0tY27SIPSVZRilbiXZy5dUrNS_Zw_1Cqfjvb3Z5wRTD5ETpU-ghmQ2YCvj6RLcBukF1-sMHnqYuBcMAZ0kWrs4kuyF_I1DkNwxZ3VPYynvH-PDKfIJG_3_wU1fCy6YSUZjW-tX-9eBTWXHiX9Yv7gB_oC-kbAcoHO5qbtU9dfkfyk_6ACxCY4y-SAR2dbdf68vjHyxzHqPKQLXICXLmpiPDZA2jGjba0ytTuCJnPa488lrLtIEL-TWtCPwm3DmBGMs5ztXgrIADVdHjSHBFoAFyLJa78hcqu1KgfVHeBLkpeXwWcEnB_UMemDXiWEOnZqPOLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIwXlXQ8zNomP0pvWnVdqNU26l3-43FR4kVQ20p37WdPFVgFAnpT7axtJ4GThR4V7WzzfO2wx-YV-4os61qFU3npViJ0nXgr-gDCkD1iJrcDQs2TbfMWYFkqBuXk5ZJLjX4u9_iP9i63iu8JNv9GEsF4uXu6n_ffLcHC_WfO9jEfd9qLlNOs6AXcPxlnOdblRL2FbL3ZclipL4PTl7W5M10t9MVA7ACgWnh3BSC0SpxYSaovJpEJmACmK7tfkYW_wVSvU3wLkjnG3VHknOSWb_5b5EV0oUCc27jLx250IntLI-UpRg3mJOrKAf6AS0NlXvBIQnb6KbZuT8TLqCex5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUYj7fPFb8YcfFt5yWeK0oDaoU6yylgL-39c0EfJ_00SGfBDiPwNJQgTVutAApXGczjhHKvseT_eO8TSG_6Cn1X1b0NefMGPYGS7VWeJXhazBreylxM0VK3BvHYNQ6KJNvZ-YnAa_IXXUa5_UBgl7gpAoxlJ3qvW0-T6KWDPVspwaUmwArRaHSiRJ2bcEAlVukdtIkcyucKKnd5xMdVscy3bWetzEh9htTS21WODCKv3Ltpkn9vz6tRgzQAgw9FAypsUybngh6KYifg84s4lhq9gOO1cOdWt2oGfetEAbXkOznZzGb3_LODsu2Gz8WQLVxKOt39INX6XMvzpPFGKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZRsIJUiHizMHxICAe0RrscliFaBTMNknRmK5FG5QwuO30Cgb4BeOLdunvMyX50K5SXQRf_UsWW35r0rQJlWiUy0MsUTjzjcXuuRDg3YhIzA064qmzjOfQ5UxedQuqioDTKGWr7E3t6nD1gkdaY4U2W8VONdrZItC-mYBfG-m4CHLApiXQg3vQ01-ct4PsnvIz7KCwMvGQIabpfmLuUrz0_gs_HzmFAUMz8f0QKNTjvD3fBJ64uY7Ies5bpubhD2haFrA--LqrgIrLay2nRgJGyOf5XYlLTkxzyX2YG5eLblsNMW7KSXvnwD7PAyYpiPR3KfoUXynvqnOsqpkYKH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ژول‌کونده مدافع میانی تیم بارسا با پلی استیشن یکش رفته اردوی تیم ملی فرانسه برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22466" target="_blank">📅 14:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuA1MOptYgDTJqYEM_YG3WCrikb0qwaYteHLXe_5fofGFMfuYFoATXK3vkwBeCB0ndqOykhT_CdIJLhWyM31o6deTZDk-OBIRjTOHeu4N8hLCS5zwb01lXt_Q4wtqNc7yO0oMLCMvIe6Yt8l8sqQBbqZGBMJsL4EG6IouO2V3bqOh3ZQ2dGfVexCbp7uMAl4AcnEyR7GZFPqStjeZ22DFJm2itthYyqgy-NgwadamIxrGtbJie8U30jOxXzgmHL4QWh8SzGlrGUq-G_fCyx4X32jSvnip_ttu30rND5aaOfdjLBMCwL5HNXHcCeRp_LHsWtH3H1NOflQhhNVO9EpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22465" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTFUl5lC4PR2lQzLpN6PF1hiUi29rdcWuTLDCUfeUzayNgScGMWkjezp13GEtktRmxrCwg7rB9MdHISDX4AmB-wSuImiiRximoZtZnFmxHkJeILakjDGJmRIqW9mL_qbM04jU9Wv7PZpVTQ2cEj0_nlgSuwjyOcOf2lAjwopueCicUDq2SlaQ5aoR6uJvqculssCj2M5zwjiCr0PtEcAQTza0fF3uN8dWe5hY7P46a14dxIEGwBUB2P92XC-hqHnhBzkMiJjQwbeQfalOh6nOs4xYZo5rkLt4DuZe8eaWrfVIAwNsESHyr2Trk1ToUpCIFGJgZS3iDtzxUl67J6uVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ استن کرونکه مالک آرسنال در صورت قهرمانی این تیم تو چمپیونز لیگ قول داده به هر بازیکن آرسنال یه رولز-رویس فانتوم هدیه بده.
💰
این‌جایزه بین 530 تا 580 هزار دلار ارزش داره.
💵
ناصر خلافم قول داده درصورت قهرمانی پاریس به هر بازیکن این تیم یک میلیون پوند…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22464" target="_blank">📅 13:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWkfNmqxE3u03W0okQI8FFf3of7sAoE975Wu4pTm8Dkx2pxg8IOK-FpAAtSABUpASeU8JztEji7i6gwHcq2srjo5aPm9Sx1JXAMO923ea2W1X0jpAkP_qUC_1pD68NTQ7nOAn7ngLNC2kDqCZknMqubdOTjtWhVK9LNwQYMZ5CxPo_CWiAB78xZXV_fzsVFkTX8d_0nETA2zNZBU4s4ECqrqzJ88k9H7z6xwmHu029sP774JbG-Fe3mAains8GxktquXkVVEHORGM0ebx4C3rAgS4G8L-lpgQjcIqwCfO3-3P9nefWNgamUIEirhzU0C3GGoY8mrLpwZo76yUL8i0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ علی علیپور مهاجم 30 ساله پرسپولیس بزودی با حضور در ساختمان این باشگاه قرار داد خود را به مدت دو فصل تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22463" target="_blank">📅 13:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMT3m3E8vnpV49fVR8GPDHqxUeXWK9zykdbAJIIZY6KVzLSWMDOdX8vySvnJysDoU44OPPKmZWf0ov6SBJAsPp280HcVBr-2d6kuTeGw6Sp-wKRXISm8SxfCIt2ZAWtSbChE5rCRjVLPjKiQ3lXoCD5q1GYxtrmMU1CoszLwyXUH5nTcFfYajz5ooYrEsLZgosDk4iDxMju4a5-3Wke37AKQrr1lGkwpzgaJgnHg06TTb7IeQmYSQL7YUYL7rMKp6G61ZwN-j4g31bj41T1jfGYhSl8dGu-DI2qlsHBkUe8O7bVL3fDFxwZHmzSLR_4dlFlF4w55fJrhojQBtsUP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22462" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXa4UDeMM3Fv_2gSh0s2HImGjP9N7uDcMuUMhPsKeVNN_s8Ke2krqWDlx6lX7bjZs9ME0Gtrcad0TSIq4hhQ7perS-zHyu6OOgcSwLiXKxb6Wbx1KsVv7yLa1KTEgxVZzHF5B64M8NdSqJmv85EOrrLE5jSkJn-qjcUPevMxWS2B7oRb8V_arvIUEj7f2aNPJyirmZrk88BN4EvreApv5ngt2bp0RVIUqGtHqNQxo5tGUIbKyiN29SEn4IPR-Gs8XrzSArotyuFtG2FXt5SfZhYGG-Ms0aO-m-zD5KJlPBscjPGNhbbxJ9zaOWUGdNCh4ag7gwlBNtFvWNFLRo1rSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رسانه‌‌های‌اماراتی: علی‌رغم علاقه شدید فرهادمجیدی‌به‌استقلال و هواداران این باشگاه اما اسطوره آبی‌ها به دلیل حکومت جمهوری اسلامی قید بازگشت‌به‌تیم‌رو زد. مجیدی زمانی به این تیم باز خواهدگشت که دیگراین‌حکومت وجود نداشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22461" target="_blank">📅 12:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9Rk3FbnBuRyKEauFW6cAGoQQ8AaGovdxr5uqPVZcWogd3pdWmPkb0zwbTGOWYfo97sRiFFfkq7uwexUPfLXeZehis8H4yEmMikFpUrcSuaFJkE9qxMqLKMm8eZhR_LH2e8V54yga8_IG73jo-NREiIdHFuhkntOr4xV8gfucKQ0hh_-CtiEQryIUBSfQ2scFDMHAghRHRM_tQptphR5GPZIOf9OldYFrqZO7qI9UwAUot18oIcGkZn0xG-rsyyRoS9cLMqqgD4Wz7a6mU5br25LM_VobStU361YDLCAc0AW7hRW00K8zzHQ-DlRWG6Q57DUPBXzVlHPEGZWG6r26w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب کهکشانی و پرستاره بارسلونا هانسی فلیک در فصل‌اینده رقابت‌ها برای‌فتح UCL؛ به این ترکیب به احتمال فراوان برناردو سیلوا و کوکوریا مدافع چپ اسپانیایی باشگاه چلسی رو نیز اضافه کنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22460" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=ntu6FP_iVtqgDYCP9u_I3ilgEzF3kGvAoauVuzW-VagVmZLjKvAbVo1ASBhWcEgCDvVDJHFFVKO5Unv7zwzMn3HrPHBRIBbXibxcnDmU6NibfMRCWZNWzY4onr1JEnPpDM9duEMqns0Yvj5QbxEiFWAyIMToDFOE6bxmHlkavEP6lEmh1kfPbaDXV--4nqjWojwcQKbe3j5gLdEsQIP-2HCTFLT-vYaqILRuBVfEaWhV9y5qeCWk2Te6i9k776Q42RummNUQPkOGZlUNzoCtYDN1-xTuukIKMX2fL4_DqlqrhonBdPGTIQANDg-P_oq_domGpSlgBi8x_EkIworiE79pE58aMwHEggRVyFhJrsjaX5dmcZA3rBuFHdrwHsBpMWPeURZTWVVLXI-0L2NleDgfpfy4v8DlJAWQ6BeiK2bE-W9dwSRJcjQmXU1eRuM29i2OaGxUIqE52xf3acaZOHrCaGsSbPaqnmxSz6kBnZkCyi5LA-zpbtAJyFHPCMcl7jKYMejvs9OGxiqBIwycjk0EWCJYdaastqqkhC0W8dicgfwCgAKz7rvbd-toPZM4_iOW202eVa1j2JIrwUS4GeEDmtSajIdfUHd8QJLu_gFB5UJll0njTrqf13jCwFQd3E5nGIdlo8BXHnHVL8YWa8NdSDEaynShFXisdV_LnuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=ntu6FP_iVtqgDYCP9u_I3ilgEzF3kGvAoauVuzW-VagVmZLjKvAbVo1ASBhWcEgCDvVDJHFFVKO5Unv7zwzMn3HrPHBRIBbXibxcnDmU6NibfMRCWZNWzY4onr1JEnPpDM9duEMqns0Yvj5QbxEiFWAyIMToDFOE6bxmHlkavEP6lEmh1kfPbaDXV--4nqjWojwcQKbe3j5gLdEsQIP-2HCTFLT-vYaqILRuBVfEaWhV9y5qeCWk2Te6i9k776Q42RummNUQPkOGZlUNzoCtYDN1-xTuukIKMX2fL4_DqlqrhonBdPGTIQANDg-P_oq_domGpSlgBi8x_EkIworiE79pE58aMwHEggRVyFhJrsjaX5dmcZA3rBuFHdrwHsBpMWPeURZTWVVLXI-0L2NleDgfpfy4v8DlJAWQ6BeiK2bE-W9dwSRJcjQmXU1eRuM29i2OaGxUIqE52xf3acaZOHrCaGsSbPaqnmxSz6kBnZkCyi5LA-zpbtAJyFHPCMcl7jKYMejvs9OGxiqBIwycjk0EWCJYdaastqqkhC0W8dicgfwCgAKz7rvbd-toPZM4_iOW202eVa1j2JIrwUS4GeEDmtSajIdfUHd8QJLu_gFB5UJll0njTrqf13jCwFQd3E5nGIdlo8BXHnHVL8YWa8NdSDEaynShFXisdV_LnuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu4WvJUIL1ayz4xKLRhAqmN4mD8DkAJopf88jmEptK-Yq55mopf6gBaGnN9X0gd54yydxGElzau2WanSsjXau5sUpb8092Axdzg91St7Y-8OOgcMkIsRf0uMx-qt2vRzDBBNSku02zzEuO_N-9IncgUmGYV3NWVe0j7ipTGUVThv1wrlhp5RJ7qaIcF0L5V-bQhW1l2jXySEPsvXCluWwgThXJOEBM3FwPplvuyU-8XCqVNyyA4uEow71uu-bVWbdgS8SNUzOKC3sdH3tuzJci-3BVHgeEUw3xbN4noouT_Cf-RAaK1W7mB8se4WLPpfKw_U8P8MzRmBog9nyqgsjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsCMrJTnHyR6-WYv97wHhO3o4_49ZWU6jV-L6lvyjvmZSuQjMGFW9VA808N2plc32e5auSjK5YkckacyCMLgrnxkxZls19rjSqxFmvq3Wq3joY9caHanoim9oWI_mnHyTKHwcvWon3utt2oIukDurFZlflO_h3V5_UY10C9qblv9WmGFzesAu0o9PVgOCKYycbWHDlD-g8_NOOh2Zjyt02GJzMxCX-QypQgBk6d9IMwpMAiOGrVo-H4UT0YM3KYS0cDHPfIcMVMMS-Zf7wrAzQ9JGVQIoSUsOm9CogKEKNhpZ7jrcyY-ppr5JE5Kz0Q4GMbpwEQbluuV5xJa_7shIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMcScYPc5negDguiX4pkZrk1UZZ3bX6XU_wW3-OGytnhadcBoWB3xOyf_gv02Tn4Jnmo1-FCQHqFrxnZ7Jm7X4y8IglwS1PaGOLpvAjrvfZ_IBZXrJPjSrx9-O0TbQqpldfY2NQz-2QQB6wY0D-4WqQZBGz3WJGgRkl8r1nXXR809fTe5yufvwFRgSRer9A_H5s2UhbN37ymKxqB-m9aOu-_dIRYcPcZOclmiHn5P69YsZsV76nJ1u00kugJsxHhDN4R5FSOVYepf7-NeHY44_Sq1qrog-F-sk68rhPEbZjNvljmr6u03OzOR8BirJq7TdsZwxrKL94mLEF-xW4uGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=J2jwdiVDpoW5hcvkuyWSEmOxZXlSCtxIK9bwgIXc3rYUQ0izCtGzF7dYsCdt3SWUX3HSxgglTodmK-3O-GNthtmAr24DzooHnYQ2Dgo4qyuIdz8gcp9oVOzs8IS7bNq0YPwasRdCIzjudTGTlkX6qUwqV78eNIxXIXxAiocfUb1HLRzqOvz1C4j8CoX8ARCwOONTRSCIXehQXXMDIDHrXY0o6stiYPNtjBH1IRagdxJJBVmki2PU8eaVRmouurikVrl9uyh-4OAvk7necHG1hvBIL7yQ3ku996x938l9RX7QJJLoi2OjGiuxYh5aBJwz9z_LQB5VMje25buDG6qFcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=J2jwdiVDpoW5hcvkuyWSEmOxZXlSCtxIK9bwgIXc3rYUQ0izCtGzF7dYsCdt3SWUX3HSxgglTodmK-3O-GNthtmAr24DzooHnYQ2Dgo4qyuIdz8gcp9oVOzs8IS7bNq0YPwasRdCIzjudTGTlkX6qUwqV78eNIxXIXxAiocfUb1HLRzqOvz1C4j8CoX8ARCwOONTRSCIXehQXXMDIDHrXY0o6stiYPNtjBH1IRagdxJJBVmki2PU8eaVRmouurikVrl9uyh-4OAvk7necHG1hvBIL7yQ3ku996x938l9RX7QJJLoi2OjGiuxYh5aBJwz9z_LQB5VMje25buDG6qFcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeZTJHmM7f3hpVdpiccEIbozLVnV_ab8UaRQxRvfFYXp8scYJSga6_OtyqtDPo7ySMK3bvEADLZ4WrkzSVx7_pDWv9FUhgnZ0LDAMQNyttJNhwGTusqUSi54Rus_FNuHOUBaf7SZvzMlf5b3Gzmpb66XRkEWVBgyFtdI5YNIq6jCzzTNgyFtw4-Pq5CW4wK0WyvkNTiyS5_8n_WE2hypblxYAM3M_HYxXOfjBLTNO9Ocr8XgfATS72FO-Y_XIplWcH46-LZU4xfb0w8tYs2fyam4-L0y05VdnFzX2AdP5gUylWxdW2T0v7tYhwwvhCYuVJoaCDEqbZdSg9phdWma6ihg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeZTJHmM7f3hpVdpiccEIbozLVnV_ab8UaRQxRvfFYXp8scYJSga6_OtyqtDPo7ySMK3bvEADLZ4WrkzSVx7_pDWv9FUhgnZ0LDAMQNyttJNhwGTusqUSi54Rus_FNuHOUBaf7SZvzMlf5b3Gzmpb66XRkEWVBgyFtdI5YNIq6jCzzTNgyFtw4-Pq5CW4wK0WyvkNTiyS5_8n_WE2hypblxYAM3M_HYxXOfjBLTNO9Ocr8XgfATS72FO-Y_XIplWcH46-LZU4xfb0w8tYs2fyam4-L0y05VdnFzX2AdP5gUylWxdW2T0v7tYhwwvhCYuVJoaCDEqbZdSg9phdWma6ihg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
