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
<img src="https://cdn4.telesco.pe/file/EPGMXoQXrC5-5zhiPjRnRPVhKyYXdgUulr1Kg31fkBaIE_ko5ovv-ODSrSomEqmS7THtdKPpyVPFlnR_VdcBguP7wo80E4HU1aIFu7kfMHwDhLJg6Yg3Sy3B-OGj_r9Kg6e_RITf5xalzLvvgojXaf9o9Q33rfiqxT2Yn6VFfcDRZayd4d1YjTPv0Irsn-ZjxgOKcCfgIvAYRaTmcdBJ8gmgb6EOqfXFsNalBYIIRN9IGB3Y8eb6qiLZ4iJrc6mq7Ge_cOSlEnKWwUWghcA7SakPR92ZJfY2Po7Gc5vm_71ug_f4jHYMfip22aNOAkpShy5pa-Nmn5LXSAD51nhnMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 11:14:42</div>
<hr>

<div class="tg-post" id="msg-136283">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
خوش چشم ، کارشناس صداوسیما:
توئیت قالیباف مذاکره‌طلبی است؛ مثل فیلم Inception به او تلقین شده است
🔴
ببینید این جمله را چه کسی به شما پیشنهاد داده؛ پیگیری کنید! به شما تلقین شده است!
🔴
فیلم Inception لئوناردو دیکاپریو را ببین؛  قالیباف الان خودش یک پا وزارت خارجه است؛ مجلس است؛ چین است؛ همه چیز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/136283" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136282">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کیهان: جنگ آمریکا با ایران و اختلافات دو کشور هرگز با مذاکره حل نمی‌شود.
🔴
یکی از دو طرف باید از اصول خود بگذرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/136282" target="_blank">📅 11:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136281">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری / یک کشتی در نزدیکی سواحل امارات هدف قرار گرفت
🔴
این کشتی مورد اصابت یک پرتابه نامشخص قرار گرفته و سیستم ناوبری آن دچار آسیب شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/136281" target="_blank">📅 11:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136280">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpK1xapOcaXLXYjrTfk72P9qTdagHKiRiXx7ogzc3E5Oml5L1yDw9XhZDGLzLli907CgWMRZPJoeqHwbkPlxNAI04luK1QEwJfmtyZtF9RlJ5_EnzJofX8QOk4sGBN0c6IenFe9P7JdTS66Fro66JZ_UpmjbCe9t1tO7TFavOR9x5Dk-ClQdqfmkFVfBiJYvNpZRhrRoah50MOTHBv80ob69_qOqOyeihCerkIKfpNLDwGpfT_GlbjhdnGprv-72LsQHHgVIbFL1BsCnTG_q76EPXbD4Wg_gkGxIrGYLdHdr5e0TG3WpxWfZmmsoV2joRV6c0Sq4S5vlEGvf9pVTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
بیرانوند بزودی استاد دانشگاه تهران میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/136280" target="_blank">📅 11:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136279">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saF2H5RSkRAmPKdh8ldnXNRuPy2aTgijIdWwtJzmcVoYK1KsGLXU4TIz9AnVU8rh4Ho3Qqdh6LmPC8Hh0VBcVxyEeokbsOQYkdVVM9CTKiXt3oizRhhvY7aTM61d-XeOc1L3TrAIOCxG6bi1JktHDc6z5P2iVCCfQ6b8PLuMWW2iPTmerff2KJAGHbshiEN5Ug_9e6fjowQ86IbmOBSb3XRNp-FzZqxSa-2e71qsiI8gOTAJSeWaT5Msl6uO_h6FKoZXQMb_cFLRNoSzyphzzyAyQ6oQ2OIzq2qdmspEfz_QPiAiwc_a45TO2m_87XDGjSCThzaRq7kMPzihES0yYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مغزهای کوچک زنگ زده
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/136279" target="_blank">📅 10:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136278">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
قالیباف در نامه‌ای به پزشکیان برگزاری جلسات علنی در شرایط اضطرار را ابلاغ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/136278" target="_blank">📅 10:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136277">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZCKxnhQ6IONYCCeOrdmxLgd1NsVWtt4hjLLC2dHKYdc3X7A2OsqpoZKHXj2EM7zwstbdAmzNNkWg0GMPYepdEydfEw2qIokRp2ysrBAlWcAIw1qs8EwX_IxqdwsvbNbFLX-L-A2JegpPV-VSXpyTjgPm8Gr_NbbibRt_kmjlaBL4Iya_3KFcw0MoY7iIccmHCZArMhQxsL5be-O-SZP7oIrU2VF4u715h3poUWewz2xZ84B7d5KqW9z_gaejyNXQEvBmG2qSn6eefMeWasLFTTrk0C_DXDibV3PvUsx7SUN266lahRzH_rU0aR0wv1QvRJXYCuWwurpnQ4CjKhFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: سوریه از صادرات صفر سوخت به صادرکننده بیش از یک چهارم کل سوخت خاورمیانه تبدیل شده!!
🔴
بلومبرگ گزارش داد، در بحبوحه بحران تنگه هرمز، عراق برای انتقال فرآورده‌های نفتی از طریق سوریه به سایر کشورها، از ناوگان بزرگی متشکل از کامیون‌های تانکردار استفاده می‌کند؛ زمان تحویل محموله‎ها به بنادر مدیترانه‌ای سوریه می‌تواند تا چهار روز طول بکشد.
🔴
به گزارش این رسانه آمریکایی، تنها در عرض چند ماه، سوریه از صادرات صفر سوخت به صادرکننده بیش از یک چهارم کل سوخت خاورمیانه تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/136277" target="_blank">📅 10:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136276">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCwVxa0DE3MU0KQgqFNDBkI5Vf77gcS75bcsfNPdgDvWUzw4xbtTcDPmnDdRm4wmK-i50_xyNaVlQNwQjFqC_mBDXbp3RRgU17b_z_YCHJn8yrXs6t7tQLdoz9TFytfYGX4OozsHMm-niFmo2gtKRUbecSiShku7NlZ5Iof6SD-uc9HCO6EfAJn_o48MRd-nwB1smklZUohk9EZ_oLvApLSZOe0Y9sZWJ0N5WBhZyG1EkTZlqC9W3RMuPhCcSsuJSDLQhd622fyAXcWk2uWBnNJDnGhxiNzMKlMKZmG6QX-AeztYQT3G8nyl6rWz9ZB0PJne_ans8H4b2SeH3dxLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل و شاباک، عدام ابراهیم شعبان نسمان، رئیس بخش عملیات تیپ غزه در سازمان حماس، که در حملات ۷ اکتبر نقش داشت را کشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/136276" target="_blank">📅 10:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136275">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سوخت‌رسان آمریکایی سیگنال اضطراری ارسال کرد
🔴
هواپیمای سوخت‌رسان آمریکایی متعلق به پایگاه هوایی الظفره در امارات، هنگام پرواز بر فراز خلیج فارس، سیگنال اضطراری ۷۷۰۰ ارسال کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/136275" target="_blank">📅 10:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136274">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McgoGh_JqnnRuy3sGeAl7qQN7GRMbbPq6nOZVkF6ltybAjqk_q7vnfOHR7mcWws7ONEBdTCUNZEOsxfHtU3WP5zCrHzyVCgv9ULRbLStF5yRs-lxR4aZsPuE5JB4Samvs4BJ2WWXa1eiBK1qxr9PLe6AiFLL64JAmrYLAs7tZjMVUVI4qtEZR7OvP91P0FHhBsSpzXEoD1wyn9FXGFzoK-cixp53eD-Mp5PAZAkX-hy2pmk6nBDewanGDlfVEZrq2n5tNCEtE_vptnfRNkUMJ3eOfnw3GLAdPvPJCWczDCgaJxyQM3vqtdiEz2g7lP9ETam_zjrLaGNnId8WM5NQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مِی‌ساقی:
هرچقدر پاداش به تیم ملی بدن، کمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/136274" target="_blank">📅 10:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136273">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نیروگاه برق الزور کویت هدف حمله پهپادی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/136273" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136272">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfEnMtLGt6ajsXFB4bvFPvGojvTm1A1vvO_QoS1NVYWvjgeg8WcBbYLLsKVk14_ys8_8MJkzu5EAg9diU1msrSb8eUsGONJajUGA1N16ON4NMdpZkx_ztZ2HrCVr5wtfraZOUKjh-F7eocAd458Sat1FchW4d2vFRAb40LRxOTXEhm8s22shTvlz8hoF-2gYTi5tSWybg_MAEcwzWakouW5L64b_R_HlKK-dg3zvttfu23w-lFdwqRGvTF6TEE2_C1WLknIR7LwOmDBmucyG-mt7WhcDj4fElT2G0c8vbmd-YAlPK1HatyM7mIClqlGmGoHgHBrcmdbEzCadN-AX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شایعه حمله زمینی پیش دستانه ایران به کویت و این ویدیو از انتقال تجهیزات زرهی که وایرال شده، قدیمی و مربوط به یک مانور نظامی در ایران حدود ۲ سال قبل است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/136272" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136271">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a015ba28.mp4?token=m5rkpBlgj6vg7kGNHGfC2RuCnKxHBHIU_dMN1Rk4et0gB_JWD8mJl1qF0lhnYjmJm4vEWiwR6T4LuW8GPMBQt94BdYNOjQEimUecHIWPmTkSE8sxeeiOoOIZGnvLqarJ-IohXmIuMCVx5dm5wNkcjOawB2dZhyLSxTci8pFkVrLJXS-jP3NJFNMGABJrg6RHuhIff5h-zG500Fy2Hse-O1IXN0zUTcRepOb1P7ZjOrIVVuVxvZoXNXROeS3eCqCv1A4MbWgt4qcIWTGzUBs0lY1syBlTFbR5S--L6Af7k1gDlBlThB3338g4i-rNAYhTTtV6pv36GrkkbB8BCeD9wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a015ba28.mp4?token=m5rkpBlgj6vg7kGNHGfC2RuCnKxHBHIU_dMN1Rk4et0gB_JWD8mJl1qF0lhnYjmJm4vEWiwR6T4LuW8GPMBQt94BdYNOjQEimUecHIWPmTkSE8sxeeiOoOIZGnvLqarJ-IohXmIuMCVx5dm5wNkcjOawB2dZhyLSxTci8pFkVrLJXS-jP3NJFNMGABJrg6RHuhIff5h-zG500Fy2Hse-O1IXN0zUTcRepOb1P7ZjOrIVVuVxvZoXNXROeS3eCqCv1A4MbWgt4qcIWTGzUBs0lY1syBlTFbR5S--L6Af7k1gDlBlThB3338g4i-rNAYhTTtV6pv36GrkkbB8BCeD9wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی منتشر شده از طرف سنتکام از حملات شب گذشته آمریکا بر علیه ایران ، در این حملات از اف۳۵ و اف۱۸ سوپرهورنت استفاده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/136271" target="_blank">📅 10:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136267">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCmdkTdodss2F0gFff55d4xzn8VYEcu_8R7PvWMNIvSls2DvZy9H38Ck2jczSGOJrbhZZwRolTw7REeqMy80z6-ex-MGEwbEGbzuhWcJ20CyePIRy3I7qYh1EkmZZQ6ANU-KTn6mCbRET5odcFREd2edIQpkBM8eCjZ16rwCIJoLnVhID7wezCtGdn_ffzHd5DGWTjUcpB3yaP2xsTWu6fcaFTRozrJtU3ptjj3kGw37j-BKHLjhZtWGvYlCWxRkXR4tJSofnoTtXd7B0C21CReEzUmMIjLPV8O-W6WKy5YplhPCDoy1IryWpqJiwolDpl81C4F5k_eAJj1JbsG1pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnxBpNrdANTm6-j9pNOjg6LWeE1VykNm9E_upHXSo6IKRTNAnSnhIqmyYp5iv52jz8qYjd8OyuF1eR96h3YM8mBn9oK6SprP-2WoCmeu3sG-JtK2GGs3kylAXAhmAO0roeWedFHy7KBjMK_NhyWha58lP_wd_ziwn00XqsTATuh9SMSrP_g7UZG94UYIKFRjAoIvWvS9Hpq5meLW0sv-YPFj1k53MIAOvQD1ZydY6nLqR2PLTA4TViQOXVqsaC2CCuQjDyH_9X4WDdKmZmM-slCHOKX30giLQ-ExX7GoAsmJjxuAANX1RojOfhu5uKBz_DZh2Sh_mDLUJZv6o3vnQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMPemEbx3vC0BhahTX9ZeC_8YQEtzF6vKsr2VhzMjzGe0u2S16aCAwrQtA-z1rM5I0tfr70IglyOlbfErpsKUajuPhU3VBzTV-4hwPkGMemo0knMNBLNFJSlFfXbSAsgU2PO7EigE4i18zOJuX2FkEc3VLuFhmL0yfa1HaKV1vNlNbajU657oWWfqD7wb7vrsM1SMQf-MAF_Qj6c9lzLIcThinPWWOSeI1GeZUUTyifHvLCcntRrYglXkkC7PNvCdAZi4qSd2-SSY-oloD5xQvp9fMyiGlz9gjMCNKNghTZFUdGmXcwsS3uBn1tEyzb-u16tTta_tlA5bA2U9UEKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JECgLxtxg7mO4Vs5IZQp4KZV17GkGdfyNdQCGfWTMyj9QQzznRX_psuleIMOakwgRcE7e-IC3ZPr5oBa1wH2LYpDaylek_iYgaKZg5DLEdl4x29lJAPmhr5Ll9ba0nN898_YVqe8XaRevwZYaJYO1fDVN8urR553c4nI1ACfp-uHHafQHgK8mm_6SaW5nK0Ipu_xYKhuE--KaLR8_24RhmWMNyQJA9wyeiyTdG0HcWP4QvY6ldw-U0gr77gTPJqQ97jKN4X8KnAYeOPugf_-GaupYkvyrEcRIrh8Eb2YiusXQ5ub8pCj1LMUrrjpB6i7BJh5o520Vh1kTH2ngR1Ftg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هدفمند اسرائیل به غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/136267" target="_blank">📅 10:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136266">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GkB_I3yDVHnyofVxQUyMKFizzzMjl5gbo_OVXReS7Xw1qU4kpukwkauyv4fZphbhYdDsUdRYmxF7HcrfHYfu1FlnyD0YY6Pm0lBDabxwEkQ66AKZJz0kfHFVfLHY_OVEGRb-bVvX1aF1g9oaaT3No9wCl6E8ZO3fCVwTUt6-BUfHUFyO_3-J-fQNw1oztAnm5bl6dQiQS97zeWg4dQOvSt9NPYPZMQ2BGBpbnqN1lj1xgh5iPl5hZ7TC187NVvF34TDFTcJW68k0MEUhJ3rnXwSAGgx-IfP5F4R6Jq3yAHQIMk3h1VRKgeUSWm4WE3Mls4ZTSys_HL4YNDfXZmUcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله موشکی اوکراین به یک کارخانه در لیپتسک روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136266" target="_blank">📅 10:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136265">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c7cb1f67.mp4?token=exkpn7VKRIegoQAyKRt2ovz9lni-GwKP1GEOlhpEz3QyeSAnswaVag-0C8RqUItz7lAmF-OX6pnOsSvTgw8xEWOP5HW-86GC97zZqFfIZilcwcGEI5Rzmi3uLtczJcUKY8eEjxKtNFFw1AbtZ7Rh9F7BLOVPY9spBUdj8I_jgywJ2mtmK6MzEsbZOLJLt7Q24E5A2v3OZZg15c3xuMufRHkWerQsmmvirQGg1W0nmp3yuVpb0PTaHF7y7w2zoRrrwS0_S5ygrTFNOK2dofXl5-4PdZqbrUD50BWg2L4xcYWri8EfxcfMAS4Tl8BRWRpf7L177O7cdvdmFznmfG1M8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c7cb1f67.mp4?token=exkpn7VKRIegoQAyKRt2ovz9lni-GwKP1GEOlhpEz3QyeSAnswaVag-0C8RqUItz7lAmF-OX6pnOsSvTgw8xEWOP5HW-86GC97zZqFfIZilcwcGEI5Rzmi3uLtczJcUKY8eEjxKtNFFw1AbtZ7Rh9F7BLOVPY9spBUdj8I_jgywJ2mtmK6MzEsbZOLJLt7Q24E5A2v3OZZg15c3xuMufRHkWerQsmmvirQGg1W0nmp3yuVpb0PTaHF7y7w2zoRrrwS0_S5ygrTFNOK2dofXl5-4PdZqbrUD50BWg2L4xcYWri8EfxcfMAS4Tl8BRWRpf7L177O7cdvdmFznmfG1M8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل در پی اجرای بخشی از توافق با دولت لبنان، از روستای زوطر غربی عقب‌نشینی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/136265" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136264">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
فارس به نقل از یک منبع نظامی: تنگهٔ هرمز همچنان مسدود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/136264" target="_blank">📅 09:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136263">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سپاه: یک رادار هشدار اولیه، یک سامانه رادار دفاع موشکی، یک رادار FPS۱۱۷، یک سامانه پدافندی پاتریوت و سامانه ارتباط ماهواره‌ای مربوط به پدافند هوایی متعلق به ارتش آمریکا را در پایگاه احمد الجابر کویت هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136263" target="_blank">📅 09:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سپاه: تعدادی سرباز در هدف قرار گرفتن مجتمع محل استقرار نیروهای ارتش آمریکا در منطقه‌ی الرُکبان اردن کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136262" target="_blank">📅 09:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136261">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
آکسیوس: تلاش میانجی‌گران برای آتش‌بس ادامه دارد؛ اما ترامپ و اسرائیل به دنبال یک جنگ تمام عیار علیه ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/136261" target="_blank">📅 09:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136260">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1n2iGcJ9Mmt_-5NUlVM9dE2sSsgpZfDf0gmyQFQx0YkFsOySZ3eZO2HjNN6rlJecF1x-SmWucUiiS7yApHNUscmdkiJptiwKOjboajYTuY-GBUIFw2mHV5xkquWV4Ya2yTYMFhjPW4RSwfB5dOJWaVdC7nmdkBT3aMbnS-mPOk9mTMbi_9ybLDQ35Y6qKx589_oE_D9yof1OUhd1ElAGUO5EmQjMCueL8TtwzqQcMFhgiVJ45XodyubvWa22Eq6XQlARlETg0kAR22fKB2hVOBqvfxrvLcy_9fvJ52-K3zSJDKllyYtCqa1-PNoruDEGqVOgvtsp7mr-8zwIj8WEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایجپت اینتل آبزرور: یک نفتکش صبح امروز هنگام عبور از تنگه هرمز، در حدود ۸ مایل دریایی شمال‌شرق لیمه در عمان، هدف حمله سپاه پاسداران قرار گرفت
🔴
این شناور نفتکش M/T KAIFAN متعلق به شرکت نفتکش کویت (KOTC) معرفی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136260" target="_blank">📅 09:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136259">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مسئول آمریکایی: اگر ترامپ تصمیم به گسترش جنگ بگیرد، این حملات شامل تهران و تاسیسات هسته‌ای خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136259" target="_blank">📅 09:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136258">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سپاه : زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین با چند فروند موشک کروز مورد هجوم قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136258" target="_blank">📅 09:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136257">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb993d4abd.mp4?token=jCt-t8euglX2OycMDVxfvPoMSPfWEHy8dcRxhyg3Y6UoWe88dBMe6mBsla2btwUjrtGys9EPmkZUxFBaRABdfiXN5K_IudRDKWaZruJk7BYY9Hq55rww3HrkCVmM5LUnksDcalqTSD6iuh0N2ebNqVhC4irb3LWAy3jfrAz8M4Lr6kyzV2ozwVoQftHxLq6AQLQZPmEdff1UDRvlRNQi5l3iKyRfemXq-lq6apAFdtwY2reCDPfDeKk0d5Lb9tXXYxcMZzJ4H-zxc-YX1iYn0PUuH1Y7fDwt1CctuXb0lqnp48XmZ_T2eBCEkXt0NyDu3bK0atozIumM2m00cDC6CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb993d4abd.mp4?token=jCt-t8euglX2OycMDVxfvPoMSPfWEHy8dcRxhyg3Y6UoWe88dBMe6mBsla2btwUjrtGys9EPmkZUxFBaRABdfiXN5K_IudRDKWaZruJk7BYY9Hq55rww3HrkCVmM5LUnksDcalqTSD6iuh0N2ebNqVhC4irb3LWAy3jfrAz8M4Lr6kyzV2ozwVoQftHxLq6AQLQZPmEdff1UDRvlRNQi5l3iKyRfemXq-lq6apAFdtwY2reCDPfDeKk0d5Lb9tXXYxcMZzJ4H-zxc-YX1iYn0PUuH1Y7fDwt1CctuXb0lqnp48XmZ_T2eBCEkXt0NyDu3bK0atozIumM2m00cDC6CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: به حملات علیه ایران ادامه می‌دهیم
🔴
کریس رایت، در مصاحبه با شبکه «اِی‌بی‌سی» : واشنگتن می‌خواهد با یک توافق صلح‌آمیز به درگیری با ایران پایان دهد، این امر مستلزم همکاری دو طرف است.
🔴
«کاری که ما اکنون انجام می‌دهیم، تضمین جریان نفت، گاز و سایر محصولات از طریق تنگه هرمز، با یا بدون همکاری ایران است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136257" target="_blank">📅 09:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136256">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb851bd1b.mp4?token=Es8yq3e-4qqyIHT9Fd39xPucmSwxCMwVoJPlt5M3n9R-snr-ye_P8ulVS8-9_Zdl2bdNl51z2qnZVd8sI-YM0z_87r4S4Bu9GDcKYSUAED7DCBwZz6VtGdJRHIce25_60EkcaLzO5l7t0Y_XyP5HSatSax5qhpU8v9WWVR0YPX5N85yBOttG4CWoSYnFqRSFRKX0kDdq9Rdz_SLp5srKlTpayAoqsxf9fzHz9eTGPhZzTW5HRouIs-YjW9eSUthgYYGE62dTAp3iRnoQHXyjUpAh8YO_zY-_t23fdWKpiKdSBtGNTMmvIeibfty34RHVFSm0CWlTcu4HOVrEA7jpoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb851bd1b.mp4?token=Es8yq3e-4qqyIHT9Fd39xPucmSwxCMwVoJPlt5M3n9R-snr-ye_P8ulVS8-9_Zdl2bdNl51z2qnZVd8sI-YM0z_87r4S4Bu9GDcKYSUAED7DCBwZz6VtGdJRHIce25_60EkcaLzO5l7t0Y_XyP5HSatSax5qhpU8v9WWVR0YPX5N85yBOttG4CWoSYnFqRSFRKX0kDdq9Rdz_SLp5srKlTpayAoqsxf9fzHz9eTGPhZzTW5HRouIs-YjW9eSUthgYYGE62dTAp3iRnoQHXyjUpAh8YO_zY-_t23fdWKpiKdSBtGNTMmvIeibfty34RHVFSm0CWlTcu4HOVrEA7jpoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر جدید انگلیس: می‌خواهم به کارتن‌خوابی در کشور پایان دهم
🔴
ما به اندازۀ کافی خوب نبوده‌ایم و باید تغییرات اساسی در رویکردهای سیاسی و اقتصادی ایجاد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136256" target="_blank">📅 09:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136255">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در جنوب و غرب اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136255" target="_blank">📅 09:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136254">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccsirRUUrIDMycMFvPzOPHTQ1JG93DkVrj_guYda4zt2rRuhyxkkfpfnio0d_jPmkbk3OjYNMocJ6FXQmiioL-SL-7W_JtOD3hC3buCoT660Al76W_VkIAoylbug4xUl6if8bUGwbEfnxeAXFKD3l8OtIRFh5VHomGdMLcG1cZHM3AT5pbMDGvWsQMgEOE9U281tuVYVxrAepIkgHyuIGFjv2jzHV6yQgXb1iTYSr0_bnJDb1YNxs_m5Dv9T2ceDSrpKYgqmWyfllSBbzNmGO1JkruyWy5tXBB76OO3ALLS1numWo15M6qH_109NQrHB783mhpmHi2M6SJe5_x-Dfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر نفت استراتژیک آمریکا به کمترین میزان در ۴۵ سال اخیر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/136254" target="_blank">📅 08:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136253">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کلید اولیه سوالات آزمون کارشناسی ارشد ۱۴۰۵ دانشگاه‌ها و موسسات آموزش عالی فردا بر روی سایت سازمان سنجش آموزش کشور قرار می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/136253" target="_blank">📅 08:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136252">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d40636c56c.mp4?token=GPVi2cm-mV34YilAgQ2ztWZKWj6W_uv9FQKIifxvSIdZhnosPyBc7EnEdgNwzcYBRSiosceemJ-GaMj47YwG3AFaILFVyzauYsj5H_BHp-UV2UFUMeOcCGAN-Ec_6F-X8Dqm6C-XEdQtLVapZYeZwOLGhPIRi7-kTrAoFzyvMNVxTAAu2oKWefdmR-EP8bM8PIhDN0NKnPMIDMlQXUPifSHzbcpcSyCx7u0-MFJsUiBNyKWeRmvtaK1avAUKAtyCcg9FMj6N8NZqrgyT0IHQj5tY01AYmgulPIxeWGK17jJj-LivX03KVbjmIhBfpQCy-ESHxPqjQKTECtn7A4uJn5GgzUdpPaPYy5ZDtujFDmyiySunkVHUgjE_MLRkiWpG2NpgZnsSHq6QzmSoeHFPo4IEPxUZ-SrO3Fwji9ysHgFXqonJApDgDQOycsfjT62ysDwzSwFxdJGVXYuB33aY6B5koOCW5FuB6i24bQCw0Jup6tj-HGFfZsdW6ceGMk910OKOdU9sNSh8NB57rQEtAOBX9OH5FjFJYSOHD30OROZmdsHuP6NGYXLP908orgpGPPkDIJiBvGyzI14Z6IOPcrO85aIe-aGMKolUUHRqkxERnofGv6MY62npcIoviJaLPiRTOF5umcSPwJlO8ATZxQjwNRYQ-jJyJxakH7CX-s8" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d40636c56c.mp4?token=GPVi2cm-mV34YilAgQ2ztWZKWj6W_uv9FQKIifxvSIdZhnosPyBc7EnEdgNwzcYBRSiosceemJ-GaMj47YwG3AFaILFVyzauYsj5H_BHp-UV2UFUMeOcCGAN-Ec_6F-X8Dqm6C-XEdQtLVapZYeZwOLGhPIRi7-kTrAoFzyvMNVxTAAu2oKWefdmR-EP8bM8PIhDN0NKnPMIDMlQXUPifSHzbcpcSyCx7u0-MFJsUiBNyKWeRmvtaK1avAUKAtyCcg9FMj6N8NZqrgyT0IHQj5tY01AYmgulPIxeWGK17jJj-LivX03KVbjmIhBfpQCy-ESHxPqjQKTECtn7A4uJn5GgzUdpPaPYy5ZDtujFDmyiySunkVHUgjE_MLRkiWpG2NpgZnsSHq6QzmSoeHFPo4IEPxUZ-SrO3Fwji9ysHgFXqonJApDgDQOycsfjT62ysDwzSwFxdJGVXYuB33aY6B5koOCW5FuB6i24bQCw0Jup6tj-HGFfZsdW6ceGMk910OKOdU9sNSh8NB57rQEtAOBX9OH5FjFJYSOHD30OROZmdsHuP6NGYXLP908orgpGPPkDIJiBvGyzI14Z6IOPcrO85aIe-aGMKolUUHRqkxERnofGv6MY62npcIoviJaLPiRTOF5umcSPwJlO8ATZxQjwNRYQ-jJyJxakH7CX-s8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله لفظی خوش چشم به عراقچی:
عراقچی تحلیل‌ راننده تاکسی‌های خط ولنجک - بهشت‌زهرا ارائه می دهد!
🔴
می‌ترسم این تحلیل‌ها از طریق حفره‌های امنیتی به عراقچی القا شده باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136252" target="_blank">📅 08:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136251">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22cdf53d0.mp4?token=APtT5GgSZFLIuLB-05o2tfdYYmRRgbZ2qG1qR2X_zweD3vP3-LHM45PngfvxGl0ghwZNHb_xQzAoHDIWoHJ8TQ0EHsep2pvL3VL5DYz_FBHxHSNAnIQALFLAnohmspkf81eUwHTSs1p1lrHdLn3QBGj2j-EmcBIeX061C514Rzz9Zpnq2mWs3TsT76p087sb58HzsQ-f6tcgqdrkOSYHlmUq54R2tp20pqmHV6orkWbOjqL1QaTQx2C8WZA7BkC49aK3_8x5_atGb7W8iht5L_T5LY7j3yAX29gs7SE9V6YsjW1IYw334AhSjQyXtQ6ubhmm6d90EzAI_556C96oDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22cdf53d0.mp4?token=APtT5GgSZFLIuLB-05o2tfdYYmRRgbZ2qG1qR2X_zweD3vP3-LHM45PngfvxGl0ghwZNHb_xQzAoHDIWoHJ8TQ0EHsep2pvL3VL5DYz_FBHxHSNAnIQALFLAnohmspkf81eUwHTSs1p1lrHdLn3QBGj2j-EmcBIeX061C514Rzz9Zpnq2mWs3TsT76p087sb58HzsQ-f6tcgqdrkOSYHlmUq54R2tp20pqmHV6orkWbOjqL1QaTQx2C8WZA7BkC49aK3_8x5_atGb7W8iht5L_T5LY7j3yAX29gs7SE9V6YsjW1IYw334AhSjQyXtQ6ubhmm6d90EzAI_556C96oDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارلوس خیمنز، نماینده کنگره آمریکا:
شاید چیزی که ایرانی‌ها را پای میز مذاکره بیاورد این باشد که بالاخره بخشی از خاک آنها را بگیریم و بگوییم اینجا دیگر خاک ایران نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136251" target="_blank">📅 08:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136250">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
روزنامه انگلسی گاردین: جنگ آمریکا و ایران نگرانی از کمبود گاز در زمستان را افزایش می‌دهد.
🔴
اروپا برای تأمین ذخایر گاز پیش از فرا رسیدن زمستان با فشارهای فزاینده‌ای روبه‌رو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/136250" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136249">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlpZLD1sTm5zpy5KFPinz4CKYtuR8gG3xx723PTx-CzSjcCsOvw-5twqJnrCQMoW7VfMrVzX3SPIL1Asn3vsRmWFoP8j6jP3hM564Ynn_2thHkNGqQlly2cAuNdc0gKN0VmLxQXo2QevtYLnx8G6If6eneA2onVvWx9iTBoH-9xraRbExHuZ1Q2Dt9mcmUSzRlUij7H_WC9i43pfU9IzVZl12BwON18vadvUqwYX_M4bT5riVJyXG7-0_df3lJLMCbTVVzSfD_XMigAkhl6Feel9kH15QrixExiv46irteUxGQ8JNk-2vlFSPOC-MbzCEYBvG2sSPGEkfus6EBss6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت شونه تخم‌مرغ یه‌شبه ۸۰ هزار تومن رفت بالا
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/136249" target="_blank">📅 08:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136248">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نقاطی که امشب مورد حمله ارتش آمریکا قرار گرفته‌اند:
بندرعباس
جزیره قشم
سیریک
بندر لنگه
بوشهر
چابهار
کنارک
شیراز
کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/136248" target="_blank">📅 03:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136247">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb2c07bcf4.mp4?token=WYQvRrr8XWlI3TBfWM7cBEZOyZSVTvAmyhGwPFugTSDXzyp13L9h-uSfQZFjZUlsDVnsylroL58Yu3DKCFXYx0uZJcNzZCzGEDq7pUjj-vq2zMqLbaW5zejKsCTP59JBe4J9nR15O3AbxZB6yeKh7olbckJwTqKGmNWtISvvqDdK2N0M_SMINyZU8REPbTp1Samv6GsNJPkM8CK0hbDy6xGsCpbVNVMheGSLbn9kDkFyujCnBTzuA2cneU-drrkchgk6jVjyjzzaP45gPRRRKKGZ5nq8qdbjDtvQ_T6hszzA3-HtF_4U9UIV-Ri4Ljdpt0IZGF4wQLHr1WKSeiefLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb2c07bcf4.mp4?token=WYQvRrr8XWlI3TBfWM7cBEZOyZSVTvAmyhGwPFugTSDXzyp13L9h-uSfQZFjZUlsDVnsylroL58Yu3DKCFXYx0uZJcNzZCzGEDq7pUjj-vq2zMqLbaW5zejKsCTP59JBe4J9nR15O3AbxZB6yeKh7olbckJwTqKGmNWtISvvqDdK2N0M_SMINyZU8REPbTp1Samv6GsNJPkM8CK0hbDy6xGsCpbVNVMheGSLbn9kDkFyujCnBTzuA2cneU-drrkchgk6jVjyjzzaP45gPRRRKKGZ5nq8qdbjDtvQ_T6hszzA3-HtF_4U9UIV-Ri4Ljdpt0IZGF4wQLHr1WKSeiefLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فردوسی‌پور:
ما اینجا نوید و محمد رو داریم که خیلی مسلط دارن اجرا میکنن.
🔴
جاودانی:
خداروشکر بهشون صندلی دادی و قدرشناس هستن (تیکه به میثاقی)
🔴
فردوسی‌پور:
نه بابا اینا قطعا آدم حسابی هستن (تیکه به میثاقی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/136247" target="_blank">📅 03:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136246">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
فاکس‌نیوز به نقل از مقام‌های آمریکایی:
اگر ترامپ تصمیم بگیرد دامنه جنگ علیه ایران را به‌طور قابل توجهی گسترش دهد، احتمالاً اسرائیل نیز در این عملیات مشارکت خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/136246" target="_blank">📅 02:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136245">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
چهار انفجار تو نزدیکی پایگاه شهید باهنر تو (کرمان) شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/136245" target="_blank">📅 02:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136244">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/alonews/136244" target="_blank">📅 02:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136243">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gkf4BbBiXzRIJi0wEqcTNJD7RjwNiR_LgYKDTeCG-vOA16ZPOQ63-5mbyXSHHhK8jSE-L0lNacZn9M2IsH_CaxkEmk6RI_WBD_MFfxtOvpT5OEyqohHrDMYbxgKmn6EcS6NtHipdHm3JIZ0b5Y3Qm-nmqOnSolM7MtqXrl3HJjXwFN4yyWMj44w6YYDE4vxGqlMSfh-B39dW26H_GnzTQ1IS7NH7TUCc6kdQ_ZJujs6Hw4vR4FamGYsDWccQqc8zEs9h0BIC51o2p8KUWD_gSM3N-KMER1VvN5pYJgpMCoDUjyguejA11ABOm5UWipaOeNMe0el0PffCaM8vVJX0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماد شرافت در فوتبال ایران
به افتخار عادل
❤️
بزارید
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/136243" target="_blank">📅 02:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136242">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4766344fdb.mp4?token=YsGfFePMy41r_nykWemW_iCH2oqQadG7vxMb1RHvA-KgWKMAJ8QYE5jAPGdH6OJShV2hdH-IlT9b-cmagYk4KgOA3e0oSj4uRXJheKlzNcRImwpC3nW-yO8c8PBwaPys4U2Pz7TlghxfqriHHaqjHFLyd23rAr_6nHlJ8nx2CTBeelqcpBpy9W3Hnbh6E4IFDkbWbKcW-Kspmj1JqOAx53NFK1SczclAQMxlV3pfRR0Zb9exuT3Yb10WUQgDRVG-bMpUwLxL6j8Ke_DRDJmWeH-smI7lbCYmLzJxGHFnAUKzKvgvC9--uges1xUEyBjhhQ8GAMIfVPhv1JBNEAzUwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4766344fdb.mp4?token=YsGfFePMy41r_nykWemW_iCH2oqQadG7vxMb1RHvA-KgWKMAJ8QYE5jAPGdH6OJShV2hdH-IlT9b-cmagYk4KgOA3e0oSj4uRXJheKlzNcRImwpC3nW-yO8c8PBwaPys4U2Pz7TlghxfqriHHaqjHFLyd23rAr_6nHlJ8nx2CTBeelqcpBpy9W3Hnbh6E4IFDkbWbKcW-Kspmj1JqOAx53NFK1SczclAQMxlV3pfRR0Zb9exuT3Yb10WUQgDRVG-bMpUwLxL6j8Ke_DRDJmWeH-smI7lbCYmLzJxGHFnAUKzKvgvC9--uges1xUEyBjhhQ8GAMIfVPhv1JBNEAzUwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قلعه‌نویی:
پاداش یعنی پرداخت به موقع؛ پاداش من رو هنوز کامل ندادن که، فعلا 70 میلیارد تومنش رو دادن.
🔴
این پاداش بابت صعود به جام جهانیه که خودمون به دست آوردیم، پس چرا ایتالیا و امارات صعود نکردن؟
🔴
قرارداد من با تیم ملی 30 میلیارد تومنه اگه تو لیگ بودم زیر 90 تا نمیگرفتم.
🔴
تازه پاداش من ریالی بوده و بَده الان از خودگذشتگی کردم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/136242" target="_blank">📅 02:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136241">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
موج دوم حملات شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/136241" target="_blank">📅 02:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136240">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0s9BpuxqsnL6oOQ7boW1okeqAtiPv7rhaAELR5JQ6NggRGV51lqMCxzKeewMi7o3scYSCOLaSk934aImh553O0nV4_bm3y0B9NAx3JoJ7eumJOuunC0rQW6PoFjsQIPsqjUkbL_47vJwcAzR1cOQPFGGc_RhY9N-vm_kKxgSvKZmsw9j2vmQIhLC-zD4QDvXmkNFTVaMVpLMTyNPlILHtiK-ws9065OuyXRt7HiQz5zUl-2FEZXepusvM1dPj7qV8n-dE2kTKLSkz8UYhxbJd2ic1kpbcGJOp1KR6zt5o2pQIW5zCvc8IEGPd1U1sk1ttg32gbRinMpAsp8S5sueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پایگاه هوایی بندرعباس توسط آمریکا هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/136240" target="_blank">📅 01:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136239">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
گزارش انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/136239" target="_blank">📅 01:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136238">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQViYOL_613sI_NAnCoPUIzRro2ZMNSke5OgREgv05M8qb1nDn9TOOqMucZuS1ZqtEvXsiCFPQIGQ6bwwCY8h029hF-dIqJ-O9SbRW0hleRYq0RgUJ9GoD7E_RzpkFgL6H-WaC-LM87FJy_8UUXoVHv7pX27CzmZHcma6aW_eXb3lIgioYAXg_zP6DGKpo3gl7LRLBbVJWLLGSqhX5I2ffs5VOG0Z16H6fUgOADaTWdVgsz-Trm3AeHnCT1hCdL-6A01szT2Fjmo9_8jQSPy_0ThSjMAR8_Iqd-miNId871i8JkccpSE32YojqR1mVsvqKoG3gRYhKpspLst1iB0gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش‌ها از حمله به یک کشتی در تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/136238" target="_blank">📅 01:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136237">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzZ8z7O1nqd21M10atrFQD6yP0nT4Hk3BXtAddMCCenFYCThdhRcIinotaOplY4piNVoTyCnpZjbRr-VpgPblaK19HPm1f1k1xnDuNUHdnkeoVMiiCD2_o95uzeJsrBW8v3xwN-oprVdmWDrB4n-sQUH5lN26QBe-eYMUP4XT_v5XzOJPcwo_I2uWBmep8Gr4gNz5ct0l5u72QNMQpruSu9uj2pY3ssyLQS2VTL3hHYwoeMZ0UtUltIyUSnbGJAa7p2NKK5qPtnif6e4iKukof5Fh6IQqwBztePaUdjLwLHPhih3YMYPsvGGl3Lm76D8xNSYf1qN82rph3jT9XitLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقتی تو کشتی میزنی و اون زیر ساختت میزنه
🤝
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/136237" target="_blank">📅 01:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136236">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
بغض عادل از صحبت‌های حاج‌رضایی
جایگاه اجتماعی با پول خریدنی نیست / در آخر، تن شریف باقی می‌ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/136236" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136235">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHhJwoYFvIte4udln17jf9m6DTW8IpM9Sgtvh2ntSh715CGe6GavV7yIjxA2mDvflQ7D4r83imsh6mBH3AkBrgygpZnisOwSb6nnA4Zj2MVVRqZwQLXMwMHlKpJ0xVCCDbnQI4GKjNPlrPeSJlMM6l5adSIER1AwTqOXzlK9ANv45QEDeRmPtHnWEr3mFPQlOBauNxUK7uwD6LZXgkgEv75WO7DG608YYP5tc6dcki1uYRObYv-ptjRpOo78cjVrxrwvDHFQUkIzFLP0BpDoEgx_q20sVDZBp3OdjRq8jC3obuyxEIVA3HRS6SIomug-ftIAjeOMRlREFNYN_ZzfzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عادل امشب از این ظلم اشک ریخت
💔
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/136235" target="_blank">📅 01:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136234">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e13a6e02e.mp4?token=O-fyKzVaQpAtqRa0kNrce97pUbDbpi91WE6uuWBCZi3AyhNYOFofd-L6f2xlUUJmylqXxwb2mb1t44e9n_13HmdKB7rlE9A1MrPMc0FXVSmBR0WjQnehJvm8hWWFuoEXPPWT-5zGIEOOfGbvPx8yAllUu8WSUxC0YVZAm4hIQoXsQTQ7eNp2Ro3N_vdD2DUSgCnANW7HjmQk-0rVbR76rVJ7WgL_BtLBv6iGl5zOqE-39mACBIE4whbEXVVT2v3EVSsZWmwWDTxQPH7l1E7mjHT1HSMpuOnz9w0j8ctN8mgA6toQG4M7VuMsp_9LFklBgZJEHlpQRWiOlfaKh47i3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e13a6e02e.mp4?token=O-fyKzVaQpAtqRa0kNrce97pUbDbpi91WE6uuWBCZi3AyhNYOFofd-L6f2xlUUJmylqXxwb2mb1t44e9n_13HmdKB7rlE9A1MrPMc0FXVSmBR0WjQnehJvm8hWWFuoEXPPWT-5zGIEOOfGbvPx8yAllUu8WSUxC0YVZAm4hIQoXsQTQ7eNp2Ro3N_vdD2DUSgCnANW7HjmQk-0rVbR76rVJ7WgL_BtLBv6iGl5zOqE-39mACBIE4whbEXVVT2v3EVSsZWmwWDTxQPH7l1E7mjHT1HSMpuOnz9w0j8ctN8mgA6toQG4M7VuMsp_9LFklBgZJEHlpQRWiOlfaKh47i3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عادل فردوسی‌پور:
من بله قربان‌گو نبودم ، نمیشم و نخواهم شد؛ اصلا بیاید من رو بگیرید ببرید ولی من جلوی شماها سر خم نمیکنم.
🔴
همه پلتفرم‌ها و برنامه‌ها n میلیون تومن پول میدن مهمون میارن، به همه مقدسات قسم مهمون‌های من همگی با یه تلفنِ من میان، علی دایی و کریم باقری با یه زنگ میان این افتخارِ منه.
🔴
خودتون میگید کارآفرینی کنید بعد من کلی آدم از دانشگاه شریف و اینور اونور آوردم اینجا داریم کار می‌کنیم بعد اینجوری رفتار میکنید؟ دیگه نمیدونم چی بگم...
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/136234" target="_blank">📅 01:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136233">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">استوری دنیا جهانبخت از حضور در مراسم عزاداری.  وقتش شد یادی کنیم از ..... زدن دنیا خانوم جهانبخت برای تتلو
😂
😂
😂
◀️
◀️
مشاهده فیلم</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/136233" target="_blank">📅 01:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136232">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxsNkxeTLqMfymLvwPGtmxm0xVpoWhHRb-N-Nhuko3av27w_YpLv4gXGKWBBKuvXGD1bG575g39sajnAfBDGcpLEmEaKJqzxa5xefQT1jUAp9ozH2fUmi64bJa3M0RXrHHHXHhAaM13M2iei5h_OPPVX-rlJYjI7VRj0onjgz35W5s-6QuEQiuflvRAupTw7COUMBVKqQVUjNaXrzIc1t2DVK9cK2-FAVXSa-q8KX5rKA2H8c98z1NSBfv0I_bT2soeL-3uBOf2UQtQSLGbkDJI9xRKw4es39TWFdyxLJ88gRs0jciRB1xQ7dWwOeLXOs6dQ2L_x05W1vuakp3b6Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه‌نویی در شبکه ۳:
140میلیارد تومن پاداش گرفتم، مبلغی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/alonews/136232" target="_blank">📅 01:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136231">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سایت و برنامه فوتبال ۳۶۰ متعلق به عادل فردوسی پور بعد از انتقاد به شهرنویی فیلتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/136231" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136230">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUS9_CGUvB8hybJDgTCS6TcvGuYlSal5QA6dpjxmxshp_gT8l7JjGxUEbnt937HQMb-Al3wrXJ3PtYDhM08ya8AEBAs1k4D4Tz1Ka7CaibDzILFflu61gAgyIoWdf5mlHUX2oBPbi8OAy_Rqort1p8_QqEuFhNzoMxi0bpwHTtcVKnjpmChSxRIxWpKyunwmuO0TRe2iQQAxoP7Vzwi4e2fVqQKK97-FWLGji_MyzpimYezzGcNjRawFyRi8grNQ1-rOe_sedgP-cL4goDeSzj2isgCgJxQs_AK9Ocm_UKSCk717ddILm8mThyDCU--s5JLgHEPESsZEXLrJEB6l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایت و برنامه فوتبال ۳۶۰ متعلق به عادل فردوسی پور بعد از انتقاد به شهرنویی فیلتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/136230" target="_blank">📅 01:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136229">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REjuYxE4-oquvkpA6N-dM-zGOSQoSD6RBB1-lrrNuitY4x408rm9TIs-glRYnaT8fvrBA1vEN1NnpL6SD3aSDFDRou4PedJmJS8YLNcragpPh9umLviGANYTlMEmJVfMFtHdm4lm-y04aSXtx7klSNjxPmM_OuOm5i5NyxvZEVlF8-NzYgLH0DraKZMMnbUA5s1Qt-dgI8WA5R2YYKTmnyDaz4krwThJJqVUJ9VDTK_gCmY1RUQJGuYjhExm4oTNdGzcmGRfbRtq6plurfaRabiWFRnqPQIhT872YrNxl52CyZRSHmOiA_gszoiz0mrQaYrgHbugVH0_7mtHbh0lcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری جدید ترامپ و عکس اینفانتینو
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/136229" target="_blank">📅 01:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136228">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5ZryoWHg3fxcwcTJXpjyIudIRqBx8Q0HfIFfYdZkXZjTCkzEA2o93iJbzP6v7ypLVS4fAKFtEIUpMBNKAgFxcUYq-wHfDByxfJt6-rNU5D2M3N5sse4RL8ln-ofxWpzbwG5PqRP9aA5u6g0lwS6Kvs18lQStTVcXwI0p1CmjzGe4ne0R6RY-n-3ltHytc10ZvWimAc-F_2wceunkXfvSCZv8XR97cqZVrEpBi-rbCceBzJXPuC9pYpLlDz_vscDgTclMjJfzI8hgMubREiEzeXRS8Wys4_9B4zXNq6ZKRdJAFlwNukGJiamMPNliEeGIKvNrqvvqZ95I0GCBtq0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شیراز کوه دراک
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/136228" target="_blank">📅 00:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136227">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e0618ffa.mp4?token=RCl9LhfKlY-BtpDw2Z0Ii1zeewfwk5HhSgntmlrOkWdNrsPmtpxhinnKABmm7Mo5vMBmZX8-26EQe6cKdIae_535QEEWU_FzOzNswcmKf3uyuiI3yKyAwqm13TWwcPDkYte3asKqxUFQeP5NNcqweJ_xOM2NLqWFEeTxL2OU2PXRdvul9B793OAOnSG-ohR3Ns_fCqMikZx2xgIaWBnLr6lGOLfLq8Ys3uzXjIyAKilCGPTuiSFMjQrtI4DSCabUR45kajAnduoywOhHtneF4Gau-QEB7yGIaJF-DvyBrixt9mPdlIaEgNWpIxyukDQAopcwd-1yf8VR-KyL24wte43MxBlQOjmvk8sSOWS8nTK28ov8WLdykjscUgbzNkdKxluL2DL_AEO0i578QQ0xWKaNIeTCbHRkxbIBAC2K_GbUHrW1pGHTUmcDCasFaq92x9jMaXt8C5iFLUf696WOL0XTWs2jSiUcYTB7lnk0TH61KcmCFdUer76rsiNdOIYuiiCMKrtOwSxNdKvi4ZlIHAfyrGpil2J-_SyzDf4pYW_Fz1SN99YLNgSd7sAYc9Qfj_-EsiUFACCT-n-w1srCxXPoRFhSKMa1MC7C9FgqoGhK4wSEKs-9U2KdcE2YSxKun6F1Y3-ooYcAoS0Bs6rIKZybp5H3fTi-b6Zfx-DvZbE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e0618ffa.mp4?token=RCl9LhfKlY-BtpDw2Z0Ii1zeewfwk5HhSgntmlrOkWdNrsPmtpxhinnKABmm7Mo5vMBmZX8-26EQe6cKdIae_535QEEWU_FzOzNswcmKf3uyuiI3yKyAwqm13TWwcPDkYte3asKqxUFQeP5NNcqweJ_xOM2NLqWFEeTxL2OU2PXRdvul9B793OAOnSG-ohR3Ns_fCqMikZx2xgIaWBnLr6lGOLfLq8Ys3uzXjIyAKilCGPTuiSFMjQrtI4DSCabUR45kajAnduoywOhHtneF4Gau-QEB7yGIaJF-DvyBrixt9mPdlIaEgNWpIxyukDQAopcwd-1yf8VR-KyL24wte43MxBlQOjmvk8sSOWS8nTK28ov8WLdykjscUgbzNkdKxluL2DL_AEO0i578QQ0xWKaNIeTCbHRkxbIBAC2K_GbUHrW1pGHTUmcDCasFaq92x9jMaXt8C5iFLUf696WOL0XTWs2jSiUcYTB7lnk0TH61KcmCFdUer76rsiNdOIYuiiCMKrtOwSxNdKvi4ZlIHAfyrGpil2J-_SyzDf4pYW_Fz1SN99YLNgSd7sAYc9Qfj_-EsiUFACCT-n-w1srCxXPoRFhSKMa1MC7C9FgqoGhK4wSEKs-9U2KdcE2YSxKun6F1Y3-ooYcAoS0Bs6rIKZybp5H3fTi-b6Zfx-DvZbE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رضا پهلوی : من خودم رو مقصد نهایی نمی‌دونم
🔴
فقط پلی هستم تا مردم به انتخاب نهایی برسند
🔴
نه طرفدار سلطنت هستم، نه جمهوری
🔴
وظیفه‌م اینه که شرایط یه گفت‌وگوی سالم فراهم بشه و آخرش مردم خودشون تصمیم بگیرن چه نظامی می‌خوان
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/136227" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136226">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
آژیرها در کویت به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/alonews/136226" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136225">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/136225" target="_blank">📅 00:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136224">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
انفجار در بندر لنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/136224" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136223">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
انفجار در شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/136223" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136222">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
انفجار در اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/alonews/136222" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136221">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yi9tnjQfre94MfvaNemUJyamj3dndBEIQ4Z7Ewtv09iQ13NzI1wJ19J3PICJ8weUU25eHmqVy9ezcWEAxgMTCr-SR90d2mopAgN1l27aOAQJNPiwAHgQUTtqvzRHyHYc5Y6pDjUcdwUxrzY7eZx1dZJr1jQKBZj7yxujTrlJ9P3TOvBLlQaZDQVdPKaUDJcb91p7HuJyiBJHwR_gq0VmKQED0iqzFIK8rpo2Fnw9D7iOPRc-J-MKOtvDD2rH_VSL6vhJq0L3kTrGMaLOdjI7J510K_SXU7LXzRrQiWwBf0FIRY_1P3YVo_iYEZfFZcYgISRehqW4k7A8HmsQBBREEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی:
هرکی با تیم‌ملی حال نمیکنه، بی وطنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/136221" target="_blank">📅 00:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136220">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR0tCF2Ublpi7oY22bQQsrXuEsAvnLqwECGr8reGMWW_MQn_SWmtRL_Ls_btWogCUeJluPjON1Cg_gPpuWD73tt8mbkduiW-Wl3v9TSF9DH3KXd07Rv_cAAMEupfcF3uev9hgtY2nYQWLnebdVzdmzU1-caCBkRkg6BTLadjIuBSNmvJUFsvgDXbLnoVHFN9OGWuYeT56La4unNkK4TtwI5t1SjOWbAEfoeewtPFWUg3YdhQYgFSpxO_TJGeTiT0txaXhF2zFWnAZsZ9KEjDOJoh-gcJNdicE47DLkoBDyRJECqNY7IRX-5F02Fjo4a1jjIAMmTIbr4Nz7oUSLEyCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خورشید در چابهار طلوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/136220" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136219">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7843e2638.mp4?token=PeD2lWcXnlogE5cyY9WCP_qNYAfCOHt2hM67eIZ9iI9pUfcA1blzq4HT_DcGUAO8vqlQBSpXjw4B2MK7tTSvSRanNcbDOP5njLX7Stu7CIocMic3RIyGjB6uUn9u_aCWi8l2ICQUmZsP4JRksiVzvbGfwduhaiSGH_e2Z_5dQp8jV0dFjIHtbiDY3x0o_staLXJgX2nH6qaXWeGtnokUmSATA8WKv9Yabm-7o5N9Ase1W9vQ46d0EFqwFwiAkoswd03RTU576DGyp2_GOQDnnpJdSqNSIJQKX_taBMYxqsa_Onahg0W_V8o2EUfS_pbsnQm52QkS2B7uGNuNDGLPxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7843e2638.mp4?token=PeD2lWcXnlogE5cyY9WCP_qNYAfCOHt2hM67eIZ9iI9pUfcA1blzq4HT_DcGUAO8vqlQBSpXjw4B2MK7tTSvSRanNcbDOP5njLX7Stu7CIocMic3RIyGjB6uUn9u_aCWi8l2ICQUmZsP4JRksiVzvbGfwduhaiSGH_e2Z_5dQp8jV0dFjIHtbiDY3x0o_staLXJgX2nH6qaXWeGtnokUmSATA8WKv9Yabm-7o5N9Ase1W9vQ46d0EFqwFwiAkoswd03RTU576DGyp2_GOQDnnpJdSqNSIJQKX_taBMYxqsa_Onahg0W_V8o2EUfS_pbsnQm52QkS2B7uGNuNDGLPxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قلعه نویی قبل و بعد واریز صدها میلیارد پول نقد به حسابش به عنوان پاداش
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/136219" target="_blank">📅 00:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136218">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=szXH3AuQZpXCMeAMkndKqy5doQqfYezXX9EDRliMX93ZDa9736QVss5xfmdpbFcnI757qij991hmrgU0dRUNkH_2KRhXd88bMgj_gqLawvsku_4Odp-7YZkQbvPm1TMjwNdgTEQcoBfrGsWhDtJouVnFnTYhnK-55OF43a9MKVsfh_hH6OkBX1EPgDTqkitdK92MphF0W50rFcw_JXny6VVBBfY49m95fxHLhQWiLWhHsuBcyOrbPOrT7xSObdcTAaB04XnGq63Hg9rzfsg4X4cwMPYlBVrEFy9Lw1zB1V71IN21PBoVwRoZPyR3n8pGx6F2-QgnPNW07CGDpfcEMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=szXH3AuQZpXCMeAMkndKqy5doQqfYezXX9EDRliMX93ZDa9736QVss5xfmdpbFcnI757qij991hmrgU0dRUNkH_2KRhXd88bMgj_gqLawvsku_4Odp-7YZkQbvPm1TMjwNdgTEQcoBfrGsWhDtJouVnFnTYhnK-55OF43a9MKVsfh_hH6OkBX1EPgDTqkitdK92MphF0W50rFcw_JXny6VVBBfY49m95fxHLhQWiLWhHsuBcyOrbPOrT7xSObdcTAaB04XnGq63Hg9rzfsg4X4cwMPYlBVrEFy9Lw1zB1V71IN21PBoVwRoZPyR3n8pGx6F2-QgnPNW07CGDpfcEMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مثل اینکه به دستور قلعه‌نوییِ پرونده‌ساز و خایه مال، واسه عادل فردوسی‌پور مشکل پیش آوردن و اپلیکیشن و سایت 360 اومده پایین!
🔴
عادل رفته تو لایو اینستاگرام داره اجرا می‌کنه...
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/136218" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136217">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
حملات مکرر آمریکا به منطقه چابهار-کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/136217" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136216">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4sNo27B710m4pJ0Lvm3Q3y-WNOze5s1ykYhS6jnCa0-g3OPjYhknxh_bDdfZV-ySmy5q8O841pGsdzWUBTxb-CuGyTsAmTPQTFrmZsXRJwuAfXiKn_goezSQxzY_ZknLUw487DYQiQNeGkGFQmkLi9dgCoTvbGSI2UDecugronpVLx_aZS3iclz0jOAGiiIB24vkM4gD-CvtyXSt4NaJ1HMJPNN74Qpecb1FUKD_H2Ui60fNEPNympUF1DAqtAEkb9ovsJMOgyC7QuIsNXkTWyICvHICLPmCFNPiz5LaOehmpzuGaVEbe4fMQG2nQmqTe7nRVbH5yznYujyjjrdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار فاکس :
احتمال اینکه آمریکا دوباره وارد یه جنگ تمام‌عیار تو خاورمیانه بشه هم داره بیشتر می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/136216" target="_blank">📅 00:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136215">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
انفجار مجدد در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/136215" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136214">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پایگاه امام علی چابهار رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/136214" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136213">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
قلعه‌نویی:
مایه آبروی فوتبال ایران بودیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/136213" target="_blank">📅 00:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136212">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b1cf00f2.mp4?token=H8rbdWFQbiyHsyMj0YhqbenCQiLKq155NdXEwrIH9JtetsTR3funyurN_lBr9MwNsC1_UpEjp2e3mdwk6OAahONuKLVR063dtyxn-C_qq-j2NO-gAicWuuPd0KmSB-5kVcfylw6et6eKI_Y5ANUEt4TFgVZZyBcZnnvoHRfv0apm_XvIFhkTXK5tBspWR6nzSY5pOLAwjjO2cBu25GwcWUH3yqVFHgweMWgssgNVkO3tyPROsFPa81rWf1jU4kaYutkbiDb8eUi75tjfjV49H-HCIAfjC4ZbljtgarCU5lGA_80iMmTfhJfZI7xAhTtWUbg63ackYqEhDL4bogDOYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b1cf00f2.mp4?token=H8rbdWFQbiyHsyMj0YhqbenCQiLKq155NdXEwrIH9JtetsTR3funyurN_lBr9MwNsC1_UpEjp2e3mdwk6OAahONuKLVR063dtyxn-C_qq-j2NO-gAicWuuPd0KmSB-5kVcfylw6et6eKI_Y5ANUEt4TFgVZZyBcZnnvoHRfv0apm_XvIFhkTXK5tBspWR6nzSY5pOLAwjjO2cBu25GwcWUH3yqVFHgweMWgssgNVkO3tyPROsFPa81rWf1jU4kaYutkbiDb8eUi75tjfjV49H-HCIAfjC4ZbljtgarCU5lGA_80iMmTfhJfZI7xAhTtWUbg63ackYqEhDL4bogDOYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
در جواب به حرفای عراقچی باید بگم که تمامیت ارضی مهمترین شرط رضاپهلوی برای قرار گرفتن کنار ایشونه.
🤔
جمهوری اسلامی هنوز نمیخواد بفهمه که دروغ دیگه جواب نمیده و ما تو سال 57 ننگین نیستیم که رسانه ای نباشه تا دروغ هاتون رو نشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/136212" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136211">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
چابهار زیر بمباران سنگین
🔴
۲ تا دیگه سنگین زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/136211" target="_blank">📅 00:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136210">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b2b31776.mp4?token=IJ717KN1eoetXy4C0Cj2hSdVQUC8hGVGhfrvJ3YuZXVDfqiX_S3nbjeYAKEhQw8jQWSCSfpyRAlY61wsavAtHB4K5KUjuksxj3kOAJ7NYPqpqYDjQIRli5Ph0048wibWQEP3-qYZr_axXOFG5EGB4gYwmlPEQfHI5mUyzo_mqymtiYPamjQy9AshZDvbGtLUEsBsr_hfrATbtlDRuMSGth9QEGFd8RVY2KrZG11KZjPVuj5Kn_TC_4p1IIhtOLRAozphJuAYubeil4thxFc0i4hxKHelcyWFrCRf7FggCFcxkb-MbEOepdKZ5qpxDrkGPkBJY286ZTvekJnP-zMNnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b2b31776.mp4?token=IJ717KN1eoetXy4C0Cj2hSdVQUC8hGVGhfrvJ3YuZXVDfqiX_S3nbjeYAKEhQw8jQWSCSfpyRAlY61wsavAtHB4K5KUjuksxj3kOAJ7NYPqpqYDjQIRli5Ph0048wibWQEP3-qYZr_axXOFG5EGB4gYwmlPEQfHI5mUyzo_mqymtiYPamjQy9AshZDvbGtLUEsBsr_hfrATbtlDRuMSGth9QEGFd8RVY2KrZG11KZjPVuj5Kn_TC_4p1IIhtOLRAozphJuAYubeil4thxFc0i4hxKHelcyWFrCRf7FggCFcxkb-MbEOepdKZ5qpxDrkGPkBJY286ZTvekJnP-zMNnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش: اگه آمریکا بخشی‌از خاک ما رو تصرف کنه، ما خاک خودمونو موشک باران میکنیم!
😐
😐
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/136210" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136209">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری/انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/136209" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136208">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/136208" target="_blank">📅 00:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136207">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/انفجار در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/136207" target="_blank">📅 00:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136206">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💢
فوووووووری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/136206" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136205">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJM5As4sa_s1mC5dOQBRh_glT2xCQSqLw-OjH_kL1fEEgBLKppG_FGVAO3PdANdTEUc5XKYRUMRhgeWv9tJkEk3tAqYsi3myuEP9cqtl-sNEYyrOcXIJZBavGjCAJjrOScv8ZHqUwPiXUEqjyu0kC-15qVYK7EgHXLmqDf7FyhHo4OH-qlgtSk93pUDYqniw2WrmhIYmzFUfz6FfMfsoDxGMc-gS1N0rFGHInbWQU4ILzXV0q7DtjlSSybmgMx5Pvb_FzxDKRAhHD6RLMELH4_28EH9KdZwOyhXjH_2N6OClHITJHTVfveXUsGaAzHV1JtL4KgBBIJs3TzUG07joAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا از طرف صدا و سیما به محمدحسین میثاقی به پاس مجاهدت رسانه‌ای یک واحد آپارتمان پاداش داده شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/136205" target="_blank">📅 00:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136204">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
گزارش انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/136204" target="_blank">📅 00:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136203">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
عربستان: ما از کشتی‌های تجاری‌مان در تنگه باب‌المندب محافظت خواهیم کرد و با قاطعیت و قدرت به منابع تهدیدها پاسخ خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/136203" target="_blank">📅 23:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136202">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
لغو امتحانات نهایی هرمزگان در روز سه‌شنبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/136202" target="_blank">📅 23:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136201">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
صدای پدافند در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/136201" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136200">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
صدای پدافند در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/136200" target="_blank">📅 23:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136199">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سفارت ایران در فرانسه: امنیت تنگه هرمز با نادیده گرفتن حقوق و منافع مشروع ایران تأمین نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/136199" target="_blank">📅 23:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136198">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
صداوسیما: صدای انفجار در بخش بمانی شهرستان سیریک شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/136198" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136197">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
مهر: قشم هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/136197" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136196">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/136196" target="_blank">📅 23:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136195">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
روسیه: آلمان یک سال تا ساخت بمب اتم فاصله دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/136195" target="_blank">📅 23:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136194">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ce5b8423f.mp4?token=C27WARLadtwyb4yE34xxM7QSAAf2pk2dDhbOb6AbTEvnh_Xxu4hswYapmBvrt10mZ0C2NqLqMf2rM8WW_aCUUDC-weC55NKB-OxAEW48tJoe0C9KZVMr0UXR_5f939FaV7ZaQ7_mC2U5kROLzG4d6PFIc4McIsN5SjEgrtNadwmTBd-53aAQRmDNELWegpUxHKGB8oifZHdN-3yNFz-dzbCEbSI8hH8anxSLNQSTisnVhd3sl6z6cq-31vYyKv7pl5ad1NQ1OoFPKxFuOM6MskNTic3lIg26ThbI6BC-KkUjzDoBIIAZE6kJxqSsrEpNaEXAP33OjNc9RbttfjW-tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ce5b8423f.mp4?token=C27WARLadtwyb4yE34xxM7QSAAf2pk2dDhbOb6AbTEvnh_Xxu4hswYapmBvrt10mZ0C2NqLqMf2rM8WW_aCUUDC-weC55NKB-OxAEW48tJoe0C9KZVMr0UXR_5f939FaV7ZaQ7_mC2U5kROLzG4d6PFIc4McIsN5SjEgrtNadwmTBd-53aAQRmDNELWegpUxHKGB8oifZHdN-3yNFz-dzbCEbSI8hH8anxSLNQSTisnVhd3sl6z6cq-31vYyKv7pl5ad1NQ1OoFPKxFuOM6MskNTic3lIg26ThbI6BC-KkUjzDoBIIAZE6kJxqSsrEpNaEXAP33OjNc9RbttfjW-tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تهاجم واقعی دشمن به بندرعباس در 18 دی 1404 اتفاق افتاد.
🔴
زمانی که حرام زاده های حکومتی به مردم بی‌دفاع ایران که تنها سلاحشون برای دفاع سنگ بود، شلیک مستقیم میکردن.
🤔
الان که رو لبه سقوط واستادن صحبت از وطن میکنن و حمایت مردم رو میخوان که گوشت قربانی جلوی حمله خارجی باشن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/136194" target="_blank">📅 23:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136193">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSb-1U9_cIH6QnMwbrZQrFktIODNPoO7b2g8gp3ZjUT25egZdtLh6TIqcTRM2C2jhNsw16xi1LRM-ZvL2Cq4_UGtHrNht9riBbsLah73POVO8yNKj_DiRMEzsNArvxU0Jsro-_h1yKZMRm1g1upCOcaYFq7WtUbztHj_1Jkq__NL6sSleqIixZ5y0k4R6MPL6hJbqBGQ4etszttEFEFn3E5u-J8yG9cAHn4EmE11dpkLUKZ4u-n7k8M31-eA1xBNUEMraT3YmKJFORBbb9rMA8l4MNaR1h7gwDEahNAtjuaE6YRQJ_n8QAZ1NQnlaMiYnQfMyx2ayeTmMW6FvRYJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / سنتکام دهمین دور حملات به ایران رو شروع کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/136193" target="_blank">📅 23:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136192">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
هم اکنون فعالیت جنگنده های آمریکا در آسمان بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/136192" target="_blank">📅 23:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136191">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
طبق گزارش ها بیش از ۸ انفجار در بندر عباس شنیده شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/136191" target="_blank">📅 23:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136190">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/136190" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136189">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
احتمال حملات آمریکا به بندرعباس. گزارش‌ها حاکی از آن است که انفجارها بسیار بزرگ بوده‌اند و نمی‌توان آن‌ها را به پرتاب موشک‌های کروز ضدکش مرتبط دانست.
🔴
احتمالاً انفجارهای سیریک نیز نتیجه حملات آمریکا بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/136189" target="_blank">📅 23:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136188">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری / انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/136188" target="_blank">📅 23:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136187">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / بندر عباس صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/136187" target="_blank">📅 23:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136186">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری / بندر عباس صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/136186" target="_blank">📅 23:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136185">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری / بندر عباس صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/136185" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136184">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
عوستاد رائفی پور: ترامپ و امارات، خارک‌ و‌ سه جزیره را نخواهند دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/136184" target="_blank">📅 23:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136183">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت خارجه آمریکا در  یک هشدار امنیتی از شهروندان آمریکایی خواست درپی افزایش تنش‌ها در خاورمیانه، سریعا ایران را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/136183" target="_blank">📅 23:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136182">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpGS2cwj4h4QMyva39TEXvEu47j1VJZAbqfqFrQaCwbYpPUpUbydH4naYKEDnIjWWYnvoUUqwJYmCv7UGiakZVVRqEl0FtIeIfUb2CtoNrHodkTsD9qfNPXbysQZPEGngc1xlR1_E37vVIhiw29pBZ9Cr6_mQDvbEnzM_uMRY_I3SQrAYPGCTg0XcJuQOAKo6A3_fVgPGFzG7mE607lDnjGIrE7sY9aM9FVEbtN7nChE6EdSlt-bpPveB2jOWaSjYXYxKLZI98OjUqaRa0n0m-OCCgr93MBgoOpm5h5g6ES2TOdDz4VCqEG43tIwlorBKLdQ0XgzkeO5PRlia8ou-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روایت متفاوت یک سایت روسی از سرنوشت سومین نظامی مفقود آمریکایی
🔴
یک سایت روسی مدعی شده برخلاف اعلام سنتکام، جسد سومین نظامی مفقود آمریکایی پیدا نشده و احتمال فرار و درخواست پناهندگی او قوت یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/136182" target="_blank">📅 23:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136181">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
صدای چند انفجار از حوالی شهرستان سیریک در شرق هرمزگان شنیده شد و تاکنون جزئیاتی درباره محل دقیق یا علت این انفجارها اعلام نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/136181" target="_blank">📅 23:30 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
