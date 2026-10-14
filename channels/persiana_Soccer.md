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
<img src="https://cdn4.telesco.pe/file/injPJ0msUHQK2sQJ5CHZdNuy4qxVxr3UZPUw_sZXZdx-rRSCltrl4ZSegl0zLgutHRjM3eTn_xm6QlezEUqiujXkZFn3TnzBTKd3xsDTRNjYvDRT5iQqfY41gUKQfqOpvk3SNisFzLHBtGPAfq9dv4bgMERmW3NIOF_kBp0jo7hCZhbO6UFjT_t1KB7QMrax_AEk5e-EO3geUJkkLwWUMf7sBbdYZi8WB0_flLBRUxJmJHz4CjHpuOec1D54oPYKb_nYbFxJoepylMtumPBc6ZFO30EFz-M1krDSkTEtsa6PJ4U3z0uZq0jgz5sSLqJTuRHRm0Azyqd6yvOGff2HBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 469K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتارتباط با ما:@ads_Persianaaهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 11:20:30</div>
<hr>

<div class="tg-post" id="msg-31541">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52b689cf97.mp4?token=BoEYH8o3ZoXWItEBqvrDRRQLnb2MHBtkuNb9Nobt5MMFzWa_mZciNj2I8sS0DFT8gVwH0UBfsEvRgxecKv1WOXq3_gPtKQd53zPPvAszrJ7IZvuXy7AUMHfYXtFwgPpk4rS9m_agBdAj23QLv0YR0pOuSIT4ihkV5y3oMtvyW35iauzlmKhxsH9Sjn2zJdBMnL47adjhlwXzznhq5Y__fPK5P2iALBWklJ3LkZOxhlXZOZdBS_gBAppZKHo-aLuqkex6Lh-ptyTW9bbhc0Qe6u_7XPFZM_6nixb7Muxtxxs9_7n9ObKzjszDJVCX2E9bGFM5ycYJawEfu9JdI9gPPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52b689cf97.mp4?token=BoEYH8o3ZoXWItEBqvrDRRQLnb2MHBtkuNb9Nobt5MMFzWa_mZciNj2I8sS0DFT8gVwH0UBfsEvRgxecKv1WOXq3_gPtKQd53zPPvAszrJ7IZvuXy7AUMHfYXtFwgPpk4rS9m_agBdAj23QLv0YR0pOuSIT4ihkV5y3oMtvyW35iauzlmKhxsH9Sjn2zJdBMnL47adjhlwXzznhq5Y__fPK5P2iALBWklJ3LkZOxhlXZOZdBS_gBAppZKHo-aLuqkex6Lh-ptyTW9bbhc0Qe6u_7XPFZM_6nixb7Muxtxxs9_7n9ObKzjszDJVCX2E9bGFM5ycYJawEfu9JdI9gPPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/31541" target="_blank">📅 11:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31540">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiRWcn9xTqREAQcdxKEEVixOOwYcKXq70me6OcNBTIqH7R672jC82Qiq8uHlipCttigEybXzHvTOYXkmq9NFMzZNhn0vNR5CGUZWhKMzsF296i7MoumFDrFArr5XtartAuOduZpWPfLkoP5wORDP0rqa_VePksUtzPSI1h3PUjg7Jqkq9SAMywWx0UVX6VeYDOWpr-hZvzLBGTZSiSPdaSzeB6byhYhmHnAVEmpZq2qMOLNvFRpDljtoLBOM4V5vnAQShIF9vTsaWSVgMb7bpONyMO2eq6nyfBv7jSOCCuwxXtyIE-GjcoMx7_0ACq_PunA3zn9JbFWtz0GyyEXn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد استثنایی‌بارسلونا درفصل‌جدید رقابت‌ها: 10 مسابقه، 10 پیروزی، 43 گل زده. شاگردان فلیک سوم آبان ماه به مصاف رئال مادرید خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/31540" target="_blank">📅 10:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31539">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETHaa2GVSu89goRugNh9U4yeAQdJdup5Kp53JhN-Onyi2wkIFqWsimaYMe6dax5Um3bv7WTpsKmJlnj05QY5QZ26NHKJghsCwqcbJsbxGb6OZwF6PX8At-k2R5P8iQ9vzT2XE56VfY9g2nHrYcLfIyLD5KCMaCyDhRpSfQhIRDLwoO1HPUb1ifngh9nvjxlSZ7-YKHPPmRSdvd9HF6yqJ5VNmlFM-gY-5pjYDpTNylrWTHEOLurTFKN8MYaRGClBjnsm08_JFqhFgTHVUWiPPu61GIIgw9XqD7zrMEJdYyiVkehQNiggLayc-cvV1aLnR6DfyG2yIYwAWQDxZtYtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین تعداد گل زده دریک سال تقدیمی در تاریخ فوتبال؛ ۹۱ گل در یک سال؛ رکوردی که انگار برای شکسته نشدن درمستطیل سبز ثبت شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/31539" target="_blank">📅 10:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31538">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLjm1irg_AZO3YKD-fyv0WTvI0XbJ-X2QAjX3eTaEUoUIn-sx9YuFjz1J9VSwcBkbGPreLDKVgs_JElHqEJ5_eBs504ymQ7cQcgbtUyH7JPDKjvKEtcUNYse1_zZdMthUPvHQZDWtT8WEFM3ZIkpzsGuAnC7HzMPYC-vbsANcbf3-rtgsi1RQT3x9iN7cLgyrqYSdLss1jAMEZHMz15mGjR5ceXE5coliKLehxFKUrHkmc70Cu2q_0UwrHGSDgoQlYRjN8CfstiqpAlxGkCMzd1835KzuP5xllBrMtzAqRTTQjzff-ak2iuuy4KSkMH9zXuWEagxvkaRpLSUj9ZCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج اسفناک منچستریونایتدِ مایکل کریک در فصل جدید: 9 بازی و تنها 2 پیروزی؛ شیاطین سرخ نیاز به یک شوک از جنس آنتونیو کونته دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/31538" target="_blank">📅 09:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31537">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJXx4VALD2BWrg9NmR2DgZS4_G37rTDA_bDLfxdILtWkwJICiV-LnJ-hOpFKxhYS2LgYWvR0W9XeQjSuBO0FyfXkCPhzUE-m-FtTQnfhObbj4GsClIUQz_Sc14sqAirgeqRBBXjllzQgExyDS9saB2QU6S1_6Npza0n85CQua0fnUzR3bfUIsIn-uHGHyV51uVLClvd4pHG12o2jpXVxv0mcnEJcGHHIeyn0Eb2OpOXM6LBBA7Xq5vzedR23u8I4mLT3shFBIqrFNBOQihfZIHyeIZWtXRk5DeZR5lO2NyfUm7DFpt3wB8-sQexm9BhirAl73vzwu-CU0x7KH-cPPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گالاتاسرایم نتونست نوار پیروزی‌های بارسا فلیک رو پاره کنههه؛ آتش بازی ابی اناری ها در خاک ترکیه با برتری چهار بر یک مقابل یاران رافائل لیائو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/31537" target="_blank">📅 09:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXzo5uDFR8kqU6wy1mKde3KOM-Ok2VxQD3-1GrHWNLwQSLV6lRPp6YavA1MgVqpwIPSVoJ7o6J8NflBi-Nv8r1fzFtWTYR2UNvEoG3nDjCJ8PQmFwm4IWdYTuNZOQuJIVneJ1PfgWkqg4BiNuFCoUYnzMkJ6AYL6tZf_PZU5KeaRil3bCFqUKhiiJ0PfZ2pviSmEn3GPsLcyWUP4LPTHz6E6Y7x7rsapBQfqdpJUX1hGuangM5hsb2I1ESyPR4sQZ5PWTbTfgAiVIDdZM_8zVrTSYdw-ELiFJN3a_388AIEJL5rcb722FF06fiG2LpmdSdls0oKuijjH4K_bLVbGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛جدال‌معوقه‌پرسپولیسی‌ها برای صدرنشینی‌لیگ و بازگشت آقای‌خاص به شهر رم
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/31536" target="_blank">📅 08:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuV5zBh-M8qVKrtXsBh00O3wBm399my8_UE9v-HNHNSKd93edSrblpW_82lFjFK8HlSE_NfVuuJPGYDW8_eiTaWoje2liquc85qmg-b3wVA4PZGEAT9bU3eBxwk_ecpQqFLBfMNnaHxT2LuVbLY3T6g8rGW52q9nK_n0xIYHu1BUkGvTQD01ZrHVavtX2jOo0bdZVsvshxbkkSSH4HaDxRW7z-k39dkgDyLLkLyyIVFnB2awspXkGXN8aexbYLndl6pTeHi0govSPeEbq3C52WOaJfViik279blAA1tYDFZJ6jAGJNRQ-Q1wdto1SHe_Swv_RJrl-pwgzcidFjyXlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از برد قاطعانه کاتالان‌ها در ترکیه تا توقف شاگردان کمپانی مقابل تیم نروژی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/31535" target="_blank">📅 07:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31534">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fshSOYsX8VS5xLJTqCzfHtXmAXPD8nMrHxwVs5DIINZxJ4F9l-YG1qF-9FTULM3K49cAzWrzlBnjTvdpZKTyLK-s5j9b1kya-7UvIoj-hOTxQn50BLSmySNA5tZjAyUS9xju47a9NvB7bS3lsxaCXy_QhdgR9LL_BExc0nLZ9IP33UQkfUJxgUVwCNBoHszNWjjiFpuyZbhix0Ev61b-lsrLhMp63FDcek-iGR3nmn0ukzXgp57j3zjjNrZEyhcYqEUijF9SrL8oAdZnx6BrMEBVGIh_wKOgKrc5XWlBS5DDLzRwzoGBbIilejOe8wXVIk-UbwlnUPCtc9_OFy6H4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پنج مدعی اصلی دریافت جایزه توپ طلا؛ امباپه بالاتر از همه؛ لامین یامال درتعقیب ستاره فرانسوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/31534" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot-2_i2wK4qd075cDtNBXU_aTknR334rItngV91AsJWrtBM7uwPAHviAlLa7XrfRjRsCnfANMxR1CUJ1HomD8VWyQwr9ltN_LFvkxW6MfYBRAbNsjKVGp4Z_eB02eYhtZoHohPeky7oXlzRCHP_Hp1MD1693bao2ypUutFWA4G48-lt_gu32b6vD_L46jgkUuCbBBzMSxqZfO1Q2zdKhtrdC3rpjdttzVNtaqHUnyw_jBnTobaBe79e6VtK-c7LmMniHBySau2kNpwiI11aE_Q0jstbDSR1VVmpM1omVh7x7Zt1aZwuND4xUBsKiwtgHY9Ohw2p9315wItomuNfS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ نخبگان آسیا در پایان هفته دوم رقابت‌ها؛ الهلال دوبرصفر السد رو شکست داد؛ شباب الاهلی در شب درخشش سردار الاتحاد رو در عربستان شکست داد. آبی ها با پنجره بسته در رتبه دوم. شاگردان جوادنکونام دوازدهم‌جدول‌رده‌بندی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/31533" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBussiness Account</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX1_KnwBeFrJS0P281G5ykccQOTGBP9eLOYbXzPXY-sMrviZA1FtP2qLbP-GVmFpJTSm-nzl0bzSIGNHuvWjv-HsGqXnpIOD5JmoBjouOPwklzSybgcwW1lqs7pKCVklO59hs94QByBc58wCcVI4r-bONY7TVcGWwnGto-OKZCQ9nmcEPo6SvWK4-le6fgvy1BtGdtcjLjntvHkPPrP9_ZhJC9iimYurJMpTpb-oZAqZneUjCsw11G9Q2W-Br1ALdLXEcxZuwJzwxRqnPq64RV50Ac51HY2KwLxIdEcsXF2WffANv6huqa00uYzQBcUEkPOPkjJqblOBWECAXu-AKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
‼️
تاحالا شده دلت بخواد وارد بازار ترید بشی ولی علم کافیشو نداشته باشی ؟!
💵
چاره ی کار اینجاست!
یه هوش مصنوعی اومده که خودش بازارو تحلیل میکنه و اتومات برات ترید میکنه، اونم رایگان !
❌
دیگه وقت و پولتو صرف یادگیری علم ترید نکن، ترند دنیا الان هوش مصنوعیه ازش عقب بمونی باختی!
⚠️
بیا تو این کانال نتایج رو ببین خودت:
➡️
https://t.me/+gaXi_cMYHks5MDA0</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/31532" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVqdkZNVFOWe2jBZ66xhhugriOYm4c9M8CuEvdKYlOECydVJPnFL6EtzPqWErPgprj3aCnwApLtJO-3xPqCEypp-TkEL1WyormQPMer999C_lf0BHM4ZfK6umNKGhLXkyJICH0mOymDtJ9N8erVu8jI6WRZspwNIyA7bVMT4158HfA0bJe0PrTZu_M3itnoRxD2Q4TDIK8P7j2D_OE6cq7_chztkJt9EZUVU4Ta9z0dkATsfXL8yxXc6CmQXrZu2yz3EIQ9LDIJniWwlnx_2GbFZq5No62dPtau320hukqGhp7b9U-NRfMMZEYfsEmb2V6Pq3EPuR7HJQKAdkrbnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای امشب هفته دوم لیگ قهرمانان اروپا؛ پیروزی پرگل بارسا مقابل گالاتاسرای در خاک ترکیه و شکست تلخ شیاطین سرخ برابر اتلتیکو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/31531" target="_blank">📅 00:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">📊
نتایج دیدارهای امشب هفته دوم لیگ قهرمانان اروپا؛ پیروزی پرگل بارسا مقابل گالاتاسرای در خاک ترکیه و شکست تلخ شیاطین سرخ برابر اتلتیکو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/31530" target="_blank">📅 00:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoKGoe9wNgsTYCavQUltQUNJJqQG7mvNjzn-WYBWHdx8aBS_wzX9CxjDTOsQKI9_Ki_sDSV514wQ8ELUJUsPXVb2lZ6MfOisCmhKdCr8eoRgRKE5bx0MzJLFn9TVLqYLdLmnffELd6CE9kpWtVTZ5W9-2Yj7UF_4YXo28GouwpBMBKEG-rJZeNrAwyN4qeU31sqEsUQk9vSscZYaTqKYTVjVKhO8nHmqgMzUuKjJL3vE3YEovHefDefBr5k4YAPHqrPBPxJ-KofZLAMeQAp0hg8-Xms0tESman3jKCnhgvIf67H8ursVg7Q_Z8BWKJqWb5g1M5VRGV2ljSyD18XiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌نیمه‌اول‌مسابقات‌امشب‌لیگ قهرمانان اروپا؛ شکست یک نیمه ای یونایتد و بایرن و توقف بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/31529" target="_blank">📅 00:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECpNSFFCdEyyb0Qrc7qnnqSc7McKDDX0j6e3naBJ-YfdR-3SF5SSRrBs13ZofJCN34Z6vwlMS4-fEeBYBv3tTzkIj04tLNGHtJ01NhKzX7pmjLIUEgx0e2KNO0jNYPWOOM4xfHM5mjOAS_9TjU3Aip6oeHG-2XTiJHcX7qz5PDw-rBFo94CQZmnFTUykkDzxf-9v7-fgGXz9diGYHRhVq7GxUKDSbWCluu0zofJPzR2rU3_NWSy3286PGh3Dq8c5K32EOsP-nBo0HbzQMTl8zGeL_nsBnbRDwdFEtSb-kKDjd1MdMU8jaHqNMjKA4QOIvbV-p2gXrk3Ck8hrr4AdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/31528" target="_blank">📅 00:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZChFh1QI_0tiDWJXtYalQ4GXyBe_h8UZMQehZoIvaiZf-amgPFcHTrwimGPCbWSpI8YLI57fbx3tnl24UYYleWGT0DOcDczcg2_hzo8VUbAZIO0B-Iz9PyMNRDgr2wV-TBb-_GlMyEdVpn4egvicCiAX3lCdV_52crLxeyoZ5zj_aVsoeslKvo_XqKiHfEerKezUwq28fXVha7jFQdBJCgUZdB2qYa586HtjyGqYbLkSeQjuXns2xX7l5ImwemE9jJ-M8pGRfhSLVGjF8sTq-NpYD5lq6qu9C4LkToD9v3l6zhbmriUse2W59TJsX2_qf0MX5K1DhZaqqeXQzBZ2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قول حمید مریخ ایجنت یاسر آسانی به مدیریت باشگاه استقلال: در نیم‌فصل یک ستاره خارجی دیگر در حد یاسر آسانی برای خط حمله خواهم آورد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/31527" target="_blank">📅 00:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31526">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caWsmUbdXhqpgJ8OTUAVA-4Ocnv2V2G3c-p7FcJcoShlQm7WEtOirr-CDwv9vMgbq8rdBNJNtecut_HKRR0yqwHpvrHHlh2o5rgbL91_m4hYX2A4mnS2adtb-LZVAwGB-XCX4f6HmKlCqC6cW9l7ohFMzLPfz54TNF8KVCB4i7Mh2xwKyP-zM6nIadz9fII53RA4e_J6-430lxGbqcox57JkeUClyX8emIrd6JJalQmkI_9Zwf4TjgksT_xsnCQt89X-cvbOJa89GpZpThxwrss_7OJztgwd5hIIydJuHeetXDRX9KbAKz-rR8q_ExUeYB31T_VgWS2JqfeFYEwEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دبل‌ تماشایی‌ سردار آزمون مقابل تیم الاتحاد درخاک‌عربستان روی پاس هوشمندانه رضا غندی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/31526" target="_blank">📅 23:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31525">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3UsAJ_mHJ8A94_6Yn3V-e8qP4b4w7lGJj9w6aUIBM1T1wSRhTbb2LSX9eS4PVJX9O7EEqwhhf_tqSt7h9LAdtpbosZD2dsJXu106ULK89t8talorcnr5epjDKr2S4saCBCTCdPyj8ikHTFOTTjOmB5nXbvTYLyKoQOrBWMwlZcKqCAkn30MKSAq4ckeQWdMxq-WcYhE9EQ7VHidfWJcl9CcWW8D_h942_UPixUmTacHTKHSRE4-7nOfGS97c4n9A2561XgbPP53uTafDOE_Ynti6_1kMNGBE82GtwfFbvSWd8BudWgFTJQBsiijlbuk9NeSy0a8Yl7reQnJ0jjHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/31525" target="_blank">📅 23:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO-6WOfWYLtyWlEJ-1lL9lmnIlxu-NPNKq7bPjKg2Awv8wsx7D0Jwtdq-L7SrpWT4XUur6sTBfTKXTCbtsxIlB4v2qP8SmamAismRLlH0v8KP3T891xbbsUpw9dV0M2gI6E-luHFtAunBW6ZKocM0Qd1cs3UfCIvDBX2S6B9NUtcWRDKBKDvmHhijkJAXUFkUHu6oBPX2iAIxwEX8gF7LZa1aIVYHYFwKydS4Q_vTfy6VX51onPH1D7MGe452ccwdkC6LAaoBcj4uHegrhDWcs5Jucxr-GDgLIZzxkAmwvomxw6v6caBoIPl1AxeGILnX4J_ML0Jgi_kvbR48Nnxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس در بازی فردا با خیبر خرم آباد؛ تیوی بیفوما دچارسرماخوردگی شده و اگه به بازی نرسه به‌احتمال‌زیاد اورونوف جایگزین او در ترکیب‌اصلی‌سرخ‌هاخواهدشد. کنعانی زادگان و ایری نیز دیگر غایبان پرسپولیس در این بازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/31524" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e058158de7.mp4?token=QsVYl_Xp_YjKjnyUEp8gAZRRge7Nu1wYySgkOtYWTv30868WTYBSAB9poc25_Q7Wu-eJC6jGjh2UXFgZrAFN7ZXWkkdplo9gOEFo6nRp_p_56zhmcvE2gSoItiNoDa9yX5ajhU--p7AKuyIqMhi1OqyCBNFE1GEdYYUv-1YEjV_shTeLK4Rdadq2R4XFxocjTOYm4-8eOll0oS0KWCJ6lNVQYWLatI7wyj6Dhhw7lB3BUhCCj9b0SJzkpITBbdAkVfXOs3h1wQCw0k48PcSYkfhQn7x0BNVfXbRYTLSAx8bOf6vYBQAyG50UybGFR0wee_kpcZbDfc9r-tQ3IA_oEmCdELcUXHw6a2tPUxX4n1XnlP1i1BxC5Ma0a30SRnyu2ExaFJ8cypMGbahvQwAB7OztG9i-As9rTYgIyeid_uLZOX88w5SQvYApR5x5Sn8CzP2qbhQtx3qtBntbGf8ldWUmCUVmFbl2XMWBM17NG5ayFKYUmV7L8Y4qlqpAprPAqz6stSWGGBYNwG0B3XWKjRahRODHiI0_KDKZ2hRQr2RQpAC8OAR0cq1i3iJXaYvhPgIlN4IQZcZctOsD9nNoTnCTpzWvkFR8fFVWzBhEslLTQKmx8plBQr_ZNYYBa8sdpF84EyvbvtMA3o2lVqxx2izJ5ipI7z5fWBsniIawSVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e058158de7.mp4?token=QsVYl_Xp_YjKjnyUEp8gAZRRge7Nu1wYySgkOtYWTv30868WTYBSAB9poc25_Q7Wu-eJC6jGjh2UXFgZrAFN7ZXWkkdplo9gOEFo6nRp_p_56zhmcvE2gSoItiNoDa9yX5ajhU--p7AKuyIqMhi1OqyCBNFE1GEdYYUv-1YEjV_shTeLK4Rdadq2R4XFxocjTOYm4-8eOll0oS0KWCJ6lNVQYWLatI7wyj6Dhhw7lB3BUhCCj9b0SJzkpITBbdAkVfXOs3h1wQCw0k48PcSYkfhQn7x0BNVfXbRYTLSAx8bOf6vYBQAyG50UybGFR0wee_kpcZbDfc9r-tQ3IA_oEmCdELcUXHw6a2tPUxX4n1XnlP1i1BxC5Ma0a30SRnyu2ExaFJ8cypMGbahvQwAB7OztG9i-As9rTYgIyeid_uLZOX88w5SQvYApR5x5Sn8CzP2qbhQtx3qtBntbGf8ldWUmCUVmFbl2XMWBM17NG5ayFKYUmV7L8Y4qlqpAprPAqz6stSWGGBYNwG0B3XWKjRahRODHiI0_KDKZ2hRQr2RQpAC8OAR0cq1i3iJXaYvhPgIlN4IQZcZctOsD9nNoTnCTpzWvkFR8fFVWzBhEslLTQKmx8plBQr_ZNYYBa8sdpF84EyvbvtMA3o2lVqxx2izJ5ipI7z5fWBsniIawSVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت‌برگ‌ریزون‌گل‌تماشایی یاسر آسانی در بازی امشب استقلال‌به‌الغرافه به‌سوپرگل‌خاطره انگیز آرین روبن در دوران حضورش در باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/31523" target="_blank">📅 22:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUJGgzbtjfYcHYg5e9EtwuOoB_b9VaBMvI2wLPLcD8zmgHGv28hcVl2LBsWkq4GRznzJnkvIu-oPEm6NLuR7nle_mWND2qRhsebrKeTOvmvueQEPg2GkZM_6eVJqKKUgu67rG-C4TOXaAg4ggvR4LtkS37CNo3FmLJjREtXnCzsgp5sTkrp4WgEPtOHy6s186UnyXGZpaKFjx8xH1eKOjG4p_ZLHHQd_FytOp4AzCMLkvTkXo00OnIH09KbcRTFsjJkm9dPfL3H0t814EfBdWb6ASrpQItasdVU0M0CHe9JmDlGUlqlMyc_jTo-UXH8K0bqfW8mp10Izxc_t9b-YnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دانیال ایری مدافع جوان تیم پرسپولیس که چند هفته به دلیل مصدومیت دور از میادین بود در فاصله 24 ساعت تا دیدار باخیبرخرم‌آباد به تمرینات گروهی سرخپوشان بازگشت اما به احتمال بسیارزیاد در بازی فردا در ترکیب فیکس حضور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/31522" target="_blank">📅 22:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31521">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=dTwiSrtqih0oyKdcTZ8GszxnuzPNXzJxsVKZp8FeVBGQJw4WimYNpAt-u9Sz0Xk5xoOYYcBU8RCsjuUZXZn28MZ45CIwxROyiewPdNmyMXp3NMnrUdjKyC6vDTlfUBbJmqBu3inWTFHov23trCFPJFtmHOTvM8_fP3YtF093IfAyjYrAOCX7wT-QnC6QiDnPjTtFUht8T0xQxE--dnq0C7q8t7BaES4dK_Ywxa_Q8LaasSkMuz1t-jeTpssUQ13ye0dAHeQlOhnHF-87mCFjJpA8vDSTa8uBhzgwdgMQ5YOcx3ye060GCkA_VQV0CtRU0VMCBepdoeZFZTSRUnj_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=dTwiSrtqih0oyKdcTZ8GszxnuzPNXzJxsVKZp8FeVBGQJw4WimYNpAt-u9Sz0Xk5xoOYYcBU8RCsjuUZXZn28MZ45CIwxROyiewPdNmyMXp3NMnrUdjKyC6vDTlfUBbJmqBu3inWTFHov23trCFPJFtmHOTvM8_fP3YtF093IfAyjYrAOCX7wT-QnC6QiDnPjTtFUht8T0xQxE--dnq0C7q8t7BaES4dK_Ywxa_Q8LaasSkMuz1t-jeTpssUQ13ye0dAHeQlOhnHF-87mCFjJpA8vDSTa8uBhzgwdgMQ5YOcx3ye060GCkA_VQV0CtRU0VMCBepdoeZFZTSRUnj_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گلزنی‌سردارآزمون ستاره‌ایرانی شباب الاهلی دربازی امشب‌مقابل الاتحادعربستان در لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31521" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31520">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/559d04596c.mp4?token=jMaAF6Pr2ugUpsdCU_0sD4UD91PbD0ywsYkUuQbz-_QHMjT0Kw69EA6qZpfyXaESBNeVIxEoyjLgjnNeWJk8PlT-zfonEHec7xJORoZyXnknK8iPjFHvuOWcwVlmicesH2C3eByp4RKu_vdyBOreyfX0FMfv82FD5-OymeaPTcxXdSvzhCOvB1PF7sFhcLCE5ddT3dwkyC-wongb7NGCf8qFHE1JO5r1DYZ_cvOdYThnkeiR6LiSHc29DXcR5VfVmooIShXy3fmA0gvhK8dn8Si8rOIh8AoVknjbnZGGrgg9usg74z299GVI6ic1wvcJdN4B6B7WIpH0cYDRFTgk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/559d04596c.mp4?token=jMaAF6Pr2ugUpsdCU_0sD4UD91PbD0ywsYkUuQbz-_QHMjT0Kw69EA6qZpfyXaESBNeVIxEoyjLgjnNeWJk8PlT-zfonEHec7xJORoZyXnknK8iPjFHvuOWcwVlmicesH2C3eByp4RKu_vdyBOreyfX0FMfv82FD5-OymeaPTcxXdSvzhCOvB1PF7sFhcLCE5ddT3dwkyC-wongb7NGCf8qFHE1JO5r1DYZ_cvOdYThnkeiR6LiSHc29DXcR5VfVmooIShXy3fmA0gvhK8dn8Si8rOIh8AoVknjbnZGGrgg9usg74z299GVI6ic1wvcJdN4B6B7WIpH0cYDRFTgk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول لیگ نخبگان آسیا در پایان دیدارهای امشب؛ دو بازی مونده که السد فردا به مصاف الهلال میره و الاتحاد نیز از شباب الاهلی و یاران سردار و سعیدعزت‌میزبانی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/31520" target="_blank">📅 22:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDM1uYwjBQVuQIIpCqg_a5o4uzZPhygBAW4wKd7WPnkcs_t2NFerAj8olyykYrkPbrI1s59NAynHUFn-5c6lK744-To2ucWqGg863GF03CILbbCOjt-JcV7B7DptlveqU2NM7YE6jerX3QST0T5jLxGOKnivbEr2QW1kvWMyKhtksfVEyDwCm1gv1Oj1ZLgdyFl0mewaqMSeeTVsCFTGS0F5Nl2IrMLEJ-s4uv2pCMupq9YjFiaqdR2Us9XnAD0F79rG7IHx-O7xAkdzbSJS8pcqqN9qWeRWPqFybuzwFFZ1knuOEKTRGHaOUPeLbaw3mPI6il0V9S-8tLGxFGk49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31519" target="_blank">📅 21:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31516">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6Q_Q9fkpaXF1JALrsKNsRKMSLGmjdbrrhCtK2AeufWEhA0uQdihHwxvCCU_Q8FviO2LpQ9i0rANLgOrONn4VKJh0rlTRrZbLrw8kaPsV743VF1kBvv-TGeKU3hcBKAOqHD75W_-jhOg6cPKjk_0Fq2t1maqky6I0l8djm58eUfx2NO21ljM9ZQRT9COazelNjsMRl6ncWHHUK4hFKYdEGTH3Oho27szLpUx1FXdaQAQ6QwolD9gQp7y9oNjgYn-rFgVxglzl4gsFZzHzLJcn4oyv2TFv5rV1cerPx2ui0GQeHMh9ORCmoVaYpNNVXxy5wWmDsGDcrJZmlxKHTthLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syHdJoVZYba1KgfkA_GhVt_9cGHnYiR2VuAaBxgq4yp2crCUexGiMexaxrcg3fPUslzyvCqOFZ6QQqOLjlZQGC5zU906RcrmXx04RiDBJc6B3FigOlm82bGj3nE3NKJWW2cB7polifben17kji9ABy9L7tRE7XtZhU1eWwt_anxCL_5wd_wE3_2RAk8SZPAnpGFAMymtrQ_cJbqTEYC8Xee-PI4d7uCWspoRISl6Sx0GKHKKzFUXFjDsmPLg3e8ZpxalzB8gRp4Iw0QNLBvRV_xsw5kPSTDj2oxVUcuG2T424jTIVzaAv5jLaTKHjHaSrQJMc0Akl8MLXRB3adDMzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا
؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31516" target="_blank">📅 21:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31514">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6YsgX5r5-A2PJnY43lXRFurMDuTVPA3tb13DfGJYtrOHsCTwt6eJAHRO3sd-IR7YgHK8myRrAm8l4xPwxSTihjuvlnPugWttkYTAtkv7oG-mvcPIiKKOL1z3RUmeQ4taEvmLWMurI-9eQFtMVmPE0-83yETRGWCZHoNbRxT-tktSn2xGA4mwnhQqyWM8psw5txiBkkgedQcBwsbM1BuIGEEq5uGUCVpfV_029Ano1buuYae5pzQF_huPY3SvcaUJ5j3VAFlvmJAAS6XPEFCNWUTmwK5GIGkWjq3TV97G7CG_DYvX6-WFJ-gZY5TtSIcJgylpV4PAUFsx3kE2L3zsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZI0HGFaR9bsiOmE3KIgZtTl5mByM3QKzhgo6b_wDQE6QPxKlyGJQkl432MdO9s5jo6tl7KdlP_siJRhR5LJRfFX-KtrEgFLE8jbYRpHpnFfD5Qk3BZrbk5zZndCbh-yoSbDl6Hwp0iFqLSHlhCHGalOK_EwGK-R10yipvnAmnR6ZhbSAAeB3xXhau9j9R3Lwq7RRjZ9oD2hTR66wct1JVOtc9R7E7g8-Q_BLTJvCEsI-tt45NKeojX8TH1k10QdQnFyynLe5FTMRRbIbUYEpjktkQx6ezlAlZBGpMgulhFp9tgE2A3vLQTAH2XS6dBskxdSmjtI8gXwNaYvg0D0Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
کاکا اسطوره برزیلی باشگاه آث میلان: وقتی همسر سابقم گفت‌که‌میخواد از من جداشه و مجردی زندگی کنه من همه تلاشمو کردم که اون بمونه ولی دیگه لحظه ای فرا رسید که اون گفت: نمیخوام.
‼️
اون روز به درسی از زندگی رسیدم که میخوام به تمامی مردای‌جهان بگم: برای موندن…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/31514" target="_blank">📅 21:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31513">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBKj4gP-LJUxJYO7Rnbr8hxWuJp1SP_ZQnn7X2bx5GPR0GNi2n5jkkDv04s8yn-8VPCsBJJJer5iMX__YZ8NGantjB1UqUxgURAN0EPk0yKIskYxPsyCBIdYROeS0HywTe-ELnISNdoaN2AK_M_uTSGo_EZAk1DgFyurL0H91Z_wJLCJOn7CUdFxDa6rAsp9Givnyp7JGht4xxKpUYZoPC9W5kqQDSd8l4SmrfKgxuvB11oWJEBjbtomNyS9Ml22VLsy_rnIOXynwpGRr_s9-SUS908ZL8Evfypl070pg1zmJSsHctDgnLOT8P__eTT_hsRoAk6wSVDtRM0LALVktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31513" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31512">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00694d1532.mp4?token=Xd0zjmpmgAj4_1La0lr1iW2wu_h7ucd8GmeGmoggYElCHSIiUy0STJPzPL1PEvbXArDxtAvSzJIcQEUd5LiN87q71OGDxhfp4D5bKEVZa5mFMeyBGdJVJFd1yNqE4i0sLtAIfkF8--HFlO9pFGOuk4hy-gw2XqzDj-7ilzqTAY0atpyeC70GeMowSezLn4tNHoZ1uBSDyd3bNuCbcTQPQGKTr7T3O0c6Ae_gYqjeHsoRFBg1YtrbTVU5Q0P1x4JEz6IMJbMnJDE6qpMt3KpgU9ltEyvpnmnsmnAb8pQXVYmI9LtieynFL0Leeow4w7mdFo0xcgtYBJLuFfn1pTQiVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00694d1532.mp4?token=Xd0zjmpmgAj4_1La0lr1iW2wu_h7ucd8GmeGmoggYElCHSIiUy0STJPzPL1PEvbXArDxtAvSzJIcQEUd5LiN87q71OGDxhfp4D5bKEVZa5mFMeyBGdJVJFd1yNqE4i0sLtAIfkF8--HFlO9pFGOuk4hy-gw2XqzDj-7ilzqTAY0atpyeC70GeMowSezLn4tNHoZ1uBSDyd3bNuCbcTQPQGKTr7T3O0c6Ae_gYqjeHsoRFBg1YtrbTVU5Q0P1x4JEz6IMJbMnJDE6qpMt3KpgU9ltEyvpnmnsmnAb8pQXVYmI9LtieynFL0Leeow4w7mdFo0xcgtYBJLuFfn1pTQiVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌امیرقلعه‌نویی‌علیه عادل:
خودشون برنامه‌ دارند و مجوز گرفتن‌ از اسرائیل مجوز گرفتن یا جمهوری اسلامی؟ اسپانسراتونم که مال جمهوری اسلامیه. تا جایی که تونستی تیم ملی رو زدی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/31512" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31511">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icfomzqlyiU_UUCCoX9lNtVZtkGGQ8srbs2oFpPD8yGX0xQVFCol4taJA3WRlHd98Pl1iJkTqI2Frf5lPYRVK72nce52xe7UydnhvkO8l5ulJO4UmhU0sMV6iPajX08sxxT3eQfUxNJ8qQGWXwo0yjo2CZ1Ct0UmBnsM5aESgtvS4dKPFoEvpvS36dzyhFn7G4OxxpoecBz8jOhxWAYsBgGRi9YpD-zcTqdmWx3gxfUb_VhTBStxio3yT6bCo2yOt6kGmSGayKddVj0KPHLr2UnEgomRmZtn_HsNpra4SNzdAV3f1GRTihtCovn3F4JMryrVDKnRhsAcwt-O9XOY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه سازمان نظام وظیفه پاسخ مثبت بدهد؛ علیرضا بیرانوند دروازه‌بان 34 ساله تیم ملی با عقد قراردادی تا پایان خدمت سربازی به تیم لیگ یکی نیرو زمینی تهران خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31511" target="_blank">📅 20:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31510">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=bAMPaiJT0HDQqkdeM6871djO3DIMvBcSVKPtkiaFoa0z8DWFOdPer18yWPEJ0xZhhsFn8dICKoqlVJ-YDUeJriCszp5GlBsoUlikbgIJGu5T85QTzq3z1N4yPaFAmU_HLZ--kEgBEVVKs12E7B7UDXqQZ508RKISCLhqLLd5FRKVETPbuCctAfatXrSmbh5D65wLNivupiKCkquMzyYcJ49aen-k1nHBR3boYfSqy1cTBHCZDBOq1h5haDU9r7KBCnvNlDqZ3vVO7ks2zU9NUvnQ82jr9A2FSff1It-96hiVzazAd6jfVRm7NmECELMI8IISofg96j0HrKNUqrhilw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=bAMPaiJT0HDQqkdeM6871djO3DIMvBcSVKPtkiaFoa0z8DWFOdPer18yWPEJ0xZhhsFn8dICKoqlVJ-YDUeJriCszp5GlBsoUlikbgIJGu5T85QTzq3z1N4yPaFAmU_HLZ--kEgBEVVKs12E7B7UDXqQZ508RKISCLhqLLd5FRKVETPbuCctAfatXrSmbh5D65wLNivupiKCkquMzyYcJ49aen-k1nHBR3boYfSqy1cTBHCZDBOq1h5haDU9r7KBCnvNlDqZ3vVO7ks2zU9NUvnQ82jr9A2FSff1It-96hiVzazAd6jfVRm7NmECELMI8IISofg96j0HrKNUqrhilw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31510" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31509">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5tziIzlaMn-K0PZCM-Hg9Ek_708IpUve4hbJbestD7NbJQI0CsbKng-tSK38Cym-lKR9gCE1ztNl47HqyOCkYXp67fK9gAxG-vAKcVLmXgB5dANna_2O3PaqM4N4jw319XzxmnJ24dFolSHhdCWmvdGVETY176VmQ-cH0L39cRXAbjgYLzkw7X7dpAhP9feKVzw7mjrB21nJsZYIbEYqxQPbsywLoDpfLeEcVALTJcKxjjNMQOliBShWs0gTIsh2UsZrQRX3F9TBxt-qTQvZ9gi31zESrvUA7aSza3HhTfR9IibbmM4qKp43YyAE4ddvOGtvtdgwhcQlOt6iyLPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31509" target="_blank">📅 19:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31508">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31508" target="_blank">📅 19:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31507">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📊
جدول‌ آنلاین‌لیگ‌برتر درپایان دیدار معوقه دوتیم سپاهان
🆚
ذوب؛ فردا در صورت پیروزی پرسپولیس مقابل خیبر خرم‌آباد؛ سرخ‌ها صدرنشین خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31507" target="_blank">📅 19:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31506">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfxJSbDarNz_7XysuF-KHWInE38A-nrj5iXXsai9nA4u8_3dWjvZMvNiZq8LuDFtp6bn5ApDMGqsJmzHm57GzM9kvNgvIBuH-H1Mf1dagt0L2QgQczKcF1mjmwJrUh7d0ZThDhNF-la6mfbn_sfcGywJRWhs57eSykjy0kg5apl8ylMEiA8nWw7hmw7i0E3pv8Rq7sy2QdKlDXp6ArigZ4YiQFb_ZNvfeoGSamqv81cjXP5vMSAPCSM3MPphzc2RfthapWszqavROtQ6OJKjemZLHp67NG0KlMjGBGySMW3jtJK_Hl-ENsoK2korxi3xxT7MSxU5sdTe4H-Gr9uqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی با گلزنی به الغرافه به آمار ۱۱ گل زده در ۱۲ بازی لیگ نخبگان رسید. او حالا بالاتر ازفیرمینو ۱۰ گله و به تنهایی دررده‌سوم بهترین گلزنان‌لیگ‌نخبگان‌قرار داره. ریاض‌محرز با ۱۳ و سالم الدوساری با ۱۲ گل زده بالاتر از آسانی قرار دارند.
⚪️
…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31506" target="_blank">📅 18:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31505">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkHRd8NUicoq1nAs2NGVyWfl-matYHVuHze8V2bWhMSy38IPg7F85lk9ZmdonCwrXJ4Z7GPQTYCoaIuh6guK_jIZbQOUJmL4oaR8TQ78sDw-TNF2k9oWolxSJiBYVuNGRBX10dgQ6qzne9l_faEjKIjxNaXnX5NYsv2IrkV-k-WdjVt3XTeC23-BLJgQpcwKE7Y5LnCwTj6pcVN74B6IAR6NqSQz5C22HjLVnSJA-sWtM9E4OZe21WXY17S3CG_0Gp5OUeu1dAuBXHdTKO6F9KEBCaH_YtYR5dJaIL_YD1RO9rLzQ94cFOWvoDoDKYXlq15J1XIOD3MQsOnUBM0-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در شب برد دو بر یک سپاهان مقابل ذوب آهن در شهرآورد اصفهان؛ سیدحسین‌حسینی بازهم نتوانست برای طلایی‌پوشان‌ موفق به کلین‌شیت شود‌. سپاهانِ محرم نوید کیا شیرین با این پیروزی شانزده امتیازی شد و در رتبه چهارم جدول رده بندی قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31505" target="_blank">📅 18:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31504">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🟢
🟡
گل‌اول‌ودوم سپاهان به ذوب آهن در نیمه اول دیدار امروز دوتیم‌توسط مهدی لطفی و کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31504" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31502">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW0BissLdM47ehMJwo20YLFUD9VYx9I7g9w9s3Q7GPrd2O--qaFdLsPkUJsIkQPQ5nPtJnRbQNUNlyUeF_Axhm6QDOTjj4q-Si_xXWM7TC_vgU7B-4HGTqXPP6xBpn_LQAA_ysKjqlZSuXxwgNOi0fYaDqp5nVK8V2W0E3TmUD0cjlpd95sF79KbS0x2Xcw4nWSmnO-lxmGiAJ37y-i99vGppgnb3Xw2P150zVa0ebYRer8fEHTFxQhgJ2KcfYkOOOwueKhT0l9sbjjlq-30wEcqmI_rFY4Cb72YeYFFseam9aMoK_t5nKnGvLX1axhCYJXBCp851yabaepjFIoCDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31502" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31501">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5NBCQqBwU_txYpWY9y9-yq0zPQPgKfdyhzbCqDxibYpBGrv8jYxnkLkFgxZSMtr7YcxrpnflCsKRXBuV5PJ3BnqKiMap0G8fcmOg9qN9bNzN6qQo6vNRyHEOn_RDCvwV8MfdjWrJdtXLJilxQCZTjlR5hC_2U3NUiY5GZ3P8Dy8o1eMrC5-nppkLpXTF1tO4BSFZG5plpDHNCQnhq7m93hbbXZPRuxR9mfzYvjQVoufRvX4PwO094nTE1m6zVieBP4AKttuqaglyuX3XpnzwbcL3rpTaIWbH2i7oxNXSe4QwGN6Hlgxck2ClcyenMgwo6PUCupWvRbXV3XQu7Ei4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد استقلالِ سهراب بختیاری زاده مقابل سه‌تیم‌مطرح قطری: 3 مسابقه، 3 پیروزی، 7 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31501" target="_blank">📅 17:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31500">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=SKfL0hY7LttwzcujyQ0FxP1nI_WzK8M6mfuSNAUvVkyEvyAeijeUlxYLburCulO4HsAnI0_0Z0DIochfjEPeA4dpHDDvGHnUWiWR60e-QLZDmepxj87TMoQJywOX7nNHMWp_hYmrkmlDScH4F8xMLt81919X5_69oXkihg2PMIWdajuMsuRuQDmroqB5M3OL-3gcc-jCUBPcaaKS-wAuQ7ETuXXvvcA1O7Kf4LfUnFsY1fvYbV_dkLwI1Wb4C_Dh8ba0XNAaXVcZVGdvrRLs5jFFUeIJC52F_MjkppC01saIFOgMNGAbJXDOMydIp1R8MYqFsLlkLxCjKAMTyKBRqUOGUtLjqsLnegIJXz9g0OJQ17aDzbW156jU7kXzdIkQ56puND2xpr6Y3pB2nXYyqCJVUTeFOR06hIpQxoMTx-fRgSVJ4oOYFHB_7IyL16kj7p7_j5QcQhYAkoXcdzrx355QQrXTpcvIzo3Xe5fuGbBOdsIOGg6R4ktmQDdDxPff56bMe3ky7EiSRPwx5ue_M9pcFD8HdMXtuhP0pss9Q-qMR99ilB96lWp34sYiyDJaHIGIa4Wb-dWICD3hO2P4SpGgfkD770PYluWQrq2bJAQICoL3tHrd4qZ6d-7rNy3puglQbzRmznIjyp-5uIwQNJKs23uNLV8JVqIOQ0kJLhU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=SKfL0hY7LttwzcujyQ0FxP1nI_WzK8M6mfuSNAUvVkyEvyAeijeUlxYLburCulO4HsAnI0_0Z0DIochfjEPeA4dpHDDvGHnUWiWR60e-QLZDmepxj87TMoQJywOX7nNHMWp_hYmrkmlDScH4F8xMLt81919X5_69oXkihg2PMIWdajuMsuRuQDmroqB5M3OL-3gcc-jCUBPcaaKS-wAuQ7ETuXXvvcA1O7Kf4LfUnFsY1fvYbV_dkLwI1Wb4C_Dh8ba0XNAaXVcZVGdvrRLs5jFFUeIJC52F_MjkppC01saIFOgMNGAbJXDOMydIp1R8MYqFsLlkLxCjKAMTyKBRqUOGUtLjqsLnegIJXz9g0OJQ17aDzbW156jU7kXzdIkQ56puND2xpr6Y3pB2nXYyqCJVUTeFOR06hIpQxoMTx-fRgSVJ4oOYFHB_7IyL16kj7p7_j5QcQhYAkoXcdzrx355QQrXTpcvIzo3Xe5fuGbBOdsIOGg6R4ktmQDdDxPff56bMe3ky7EiSRPwx5ue_M9pcFD8HdMXtuhP0pss9Q-qMR99ilB96lWp34sYiyDJaHIGIa4Wb-dWICD3hO2P4SpGgfkD770PYluWQrq2bJAQICoL3tHrd4qZ6d-7rNy3puglQbzRmznIjyp-5uIwQNJKs23uNLV8JVqIOQ0kJLhU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد ستاره‌ایرانی جوهور دارالتعظیم؛ شهاب زاهدی از ابتدای فصل تاکنون در پنج بازی سوپر لیگ هفت گل و در دو حضور تعویضی در جام حذفی نیز سه گل زده تا با 10 گل بهترین گلزن این تیم باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31500" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31499">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9RVJISe2bMwbrVd3CGioDYoJYGy54GbrzCwo6JtyG7clUgMmTlDiAR9TjgPbWnbJQ6KlDvgSgen_giuGwD0FdBECJDA_MTGlKCquBrm81CNd9XgnbShgX-8Pn2r9IS7yXFXMbbqwQddrsi-12GUjVtGnox1Ri3-I4HJOIK84z7NB8y7lzicWdaykT1wcNi6G3jAfnShIaIOb30DhjnejKUJnNPTWWr68JMjMT_lzKsCsONf_KrVGND6wCx3B8rr6q5nfmQErkeotw_uDk3Ys_7-KKAaSoQozv0RjYiTMtYTygqG0BIzzqJgac54XJuamVLOj_vObhhgyiBsxpBcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شماتیک‌ترکیب‌بارسلونا دربازی سال 2022 با گالاتاسرای ترکیه در لیگ قهرمانان اروپا که آبی اناری ها موفق شدند اون مسابقه رو دو بر یک ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31499" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31498">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بانک تحصیلات ،بانک  مشاوره اخذ مدارک دانشگاهی. واحدهای معتبر ایران. کارشناسی، کارشناسی ارشد، دکترا.‌ پزشکی عمومی،داروسازی،دندانپزشکی
پیراپزشکی. با استعلام.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@banketahsilat
⬇️
⬇️
⬇️
⬇️
⬇️
جهت ارتباط با ادمین
@tahsilat_azad
@tahsilat_azad</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/31498" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31497">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ht_6AQGXtGbIBUzpbr3YlBA9aDid_8wcxNNELPBs7Aa8tgsJrNk-hCurf5zIcBmzRRkAgHo7T5Sk0QaVeb5Yai1zuIJlaDEBCw3V-Q5GJ4RPfH4wHLV13-Dxz48aIgEaU-_Algy_0e7Coxqh-Gf1eOqRTscTbn2dz-A_-_FWv3Oj_gTXISaH4ePjm8tn5CCOhBlIXaKGEHiTkLIoWSPKhr8l7P02xb-nav6eMJKyM7T5mBXmAuTMn1hzhfR0eZe9NvgDjQrCCHAf_sIeBN00f0AfhrdK8Nqrw4U_-VqWg1DrLxPDH5uVz664Pse5QE5BmxVAjWcqdxNlDf1ZcmVY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیدارفرداپرسپولیس
🆚
خیبر؛
ششمین تقابل دو تیم‌است. در ۵ دیدار قبلی خیبر سه برد و پرسپولیس دو پیروزی کسب‌کرده.تقابل‌های پرسپولیس و خیبر ۱۳ گل داشته که سهم پرسپولیس شش گل و خیبر هفت گل بثمر رسانده. اسماعیل بابایی، ایگور سرگیف، علی علیپور،اورونوف و عیسی‌مرادی گلزنان تقابل‌های این دو تیم بودند که در دیدار فردا هم حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31497" target="_blank">📅 16:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31496">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=r9fLs98A_KgBL1vz8qPbtk-YCt9ac94fhb6-628v9JxcMBGMxfsvtGDqpzjwv2fQ3KDRIe9Ao_I5FdzFXhOcTREPaHuxYrDFJzj3P6YWFGoYye7Qni2jt0p1-t_hTpzLZptNskpDdpHEI5BCUwuA86gikO49Xz6A63yUyphE47320cFkWHysSMh1Mkyu8GhQOBF8gFPYNxggDmBUZUMn6VH9FWz9RH781R_Dh2eAiGAqjsD1CAfi-h1_SzN7fP_pi6my_1_vy-6ZFa9k_UNRS3oKLrFdZh37ctufl4yA_0_sdUMJy82o9ecFqbTXJlaqP25I3jZ4cnfsp7AA_SxGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=r9fLs98A_KgBL1vz8qPbtk-YCt9ac94fhb6-628v9JxcMBGMxfsvtGDqpzjwv2fQ3KDRIe9Ao_I5FdzFXhOcTREPaHuxYrDFJzj3P6YWFGoYye7Qni2jt0p1-t_hTpzLZptNskpDdpHEI5BCUwuA86gikO49Xz6A63yUyphE47320cFkWHysSMh1Mkyu8GhQOBF8gFPYNxggDmBUZUMn6VH9FWz9RH781R_Dh2eAiGAqjsD1CAfi-h1_SzN7fP_pi6my_1_vy-6ZFa9k_UNRS3oKLrFdZh37ctufl4yA_0_sdUMJy82o9ecFqbTXJlaqP25I3jZ4cnfsp7AA_SxGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
معوقه هفته هفتم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل ذوب اهن؛ ساعت 16 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31496" target="_blank">📅 16:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31495">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSeMs_Mawl9Mr5gey_IG4wivpFVvfuRu6MN26PaQsCP6R13gF9SBuD9CuVUH8wvp0ExbXxcEGE_OOK0D_uJgFL5Kfossadc9lcEEfMpcm4UBtqWUpdaFFVwuaCMGPRQRVoWIAns4tV6OOFuEeWJXWROlNKqVuA3Bn4cQeK4hU2KkQDoGqX0RKkhCfK0ALFsp1FXxnwLKKgWVf6CzYT76i5JDUaWkF4eaItUaW0Yede5dv5-3k2jz3LBGPuE5ZPMOkIhudFvPINn5mk1AP3C99kohn2dsLGTPYZufvFTshLmwdFtPHnAJhOVgIZiIk7AMYS-dtkBkpNvD1sTEQTCd1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ یاسین جرجانی مدافع‌جوان فصل قبل آلومینیوم با قرار دادی سه ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31495" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31494">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP-00K8cnB2psuOSFbw_DRfGn6Ka69sCesmRVIKskyoFzVyC2V2Xs63AyJsG8BEc4KFBxxX7Ke-fcI-ox-GDR0ggHl9lHWzxW8GdoKQUCIsnZ2lOL8hIIYcSBgUOV54DA-cK5t2q5X2In6yJtr7lIcCnHL2QHBPhYcaM5kGH7svWwwwtJaMqJciHSa7xeiXVhheaycDDJC_F8zTBQ9bU1cAI-Fh-vj2VIdwgyEk9jFd0__0nMdKFlsPADfcU2QbyuSnCIv87w1iqJHESyG1nabt8rdiM-D8VhjO47b_zyAP9weoRJSszZLAv4q2GoQhB6jumUKnlwwl-e5iq1U2GzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
دانیال ایری و حسین کنعانی‌زادگان دو مدافع میانی پرسپولیس به دلیل مصدومیت دیدار روز چهار شنبه مقابل تیم خیبر خرم آباد رو نیز از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31494" target="_blank">📅 15:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31493">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRTiEJ35JEBcsj8MUqMrB7vQ3SThqZC9R7qPloEbZn3zcWVhXrXaIC1Y8-RLLWf8dYQ8_5QDq7M-X_gQiwbpEQiYl7e7hnPcwwc9ECvuyVeuFvo0LsDI0t9Ns94ICXR8sSKWAfcOr32e6_vqhfph9Qwb_yWlnkzfyTWLwL-SpiojzBLftX31b8sKr8BCDN7gnNbximKQMNTymlLPl9-FK3iAVO2Bh_js6PvCoQ_Tk5ufTV5YRmDSsCN1yBZboNg4Sw0KFCaAiDDfXE9BzapZ7QKoZWDfpc3SV1YxFPTr508U6uy9aec0penKyhvotW8JfgjOUVx41nGRAxl-tFeKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ معوقه‌هفته‌هفتم رقابت‌های لیگ برتر که قراره امروز و فردا برگزار بشه. درصورت برد پرسپولیس در بازی فردا سرخ‌ها صدرنشین میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31493" target="_blank">📅 15:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31492">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxqdmWV-ZgjRI81ELctyqEn2r4VA6QmamgripNCXzg1FVvwMt8OjzGuSikEFy4kD6kIH-1x8m4yS0aBqPvdtwExc075wIg4mRGqw0yiXwNNd3TMQfCVkrbnzLi71VG42rIFJVIIQ5k5Niv6Jcy5IjoRzFJYcLu9rOLP_X5KzXgec_MsCj7_DoZ9sHg3MCPsTINJvc7WiMe5FRoNyXc7BgoPrFsLisdGZ-ghWxCmYZ3WwGrsUqtRCFe_vwT_fuDjAg6b8XZmhWgwzIANKtHeeOt3E0cdWRhbkLB1PShWLUFzK_tf8GBtaXQcNaZdLgNsONSRXVYp2eNFgBdBK8EnWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31492" target="_blank">📅 14:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31491">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmDA6G0DiNYIj7ODdPeeKwmOZs-pU1kPF1S5J-qyKYHmm72QaD3NNtZdYfzvKKroQR7ch4QzdZwo1DKFL4QKCaEYKty-h35m3Noi4IIFEcnZn7pursDG58l7puQADK8QUqGEHsJkwTkjONkGgF_wH4CwvakMEUOZESwMUB84s2N562_uxTZ1iZv2bjpMjsKE3Q1m8t1y5cJulr3VwBvK7TC_cnByeCSzZe72Cb8tMby15GyJGNHjOg1BkyZbAFRBBxR0nB9oTRaDA3MJIoVYbRFjPl3xoegtsij_eAQYtf73W8tSflJo6j_hPMPTp5PyBPeYLWuxWahdbGM0pQJDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد! جواد نکونام سرمربی تراکتور: شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31491" target="_blank">📅 14:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31490">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwHeuPXyDVW9bdEdWMT-p1pQ0ZgEtPZeW6ZhZHg6y8tPnC39nV2fGPaCb30xieG_cNdS0boTq0IyjutrCldHDUDAOeBCTIMPcmJn1sxzLiK9Hqm-W92MbBFCOGlN1D1krXWm_xNn-VRflyMr6ZEusBsYirZP6-WES7Aa0gtUXzyQ5pi0x2bbzg83qHY-5d6mzu7V3fj1VuYqAwYhmSyKXJs479HLmqm877UH-LgN4ZE_tqV8QFIGtZY8Dw8NUbZwaKzSG1x346bkgwsNl-3NhdYm3yJhXVKeFm0y2NLB6EDdaKd_q2GXWGuGjJbcDwZfD_kfKY1x2mQDRAcR18WKDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییر زمان چند دیدار هفته نهم و دهم؛ استقلال و گل گهر بجای یکشنبه روز دوشنبه بازی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31490" target="_blank">📅 13:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31489">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK2uY8boVWdOytQWwDkOrdWm40NPYZ43cnRcn7DGZu9M2doKq_fOu0FJEdRPuyhagr6J2C1XeEPdwkP9ztYgM0rQOmN6pU3HPxKFq2216acHRgXRDufouE1bgGq1llNEu_FeVZCkLpT7WIXPawcDOIAx_8AJt1X8KopBpAnzKPB9UZpnVMhuzDxzibg7RrCsLxmiPbpeFaa89QE20lkAcuRqeK3RzmJjVPlwcw5ROJitKOKOyvrTSGhm2OvXsrddEuTgbJArtmoW9HerxkrpGonWTqnFdWhtkNb5pvVd8BhgZUsvMl_UDqa7G9gcNPW7q56KA1d_jB_XQ9_vWyr2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛سخنگوی‌نظام‌وظیفه: باتوجه به کسری‌ هایی که علیرضابیرانوندبخاطرمتاهلی و داشتن‌فرزند خورده سربازی او تیرماه سال آینده به پایان میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31489" target="_blank">📅 13:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31488">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCLBeqWj-B7jxBursZ_YaUwEHFGW0soVL_B7QIJr3qm60OoBmF0p4W_BAKgm16Z_9vEFme_NGX5VbPH9d4wYdW4-f9C7K20uI9jYIYaebnLyEVAvDA2Fhyy67ypGrL6B1JHMdjTGrVEz6qowgSs6BEEBuCWlsioY6TlPluIj9fsd0IaSVyyWkW7vTBasMPXcdfGnuRZhGSsqnzK0X02SW1LE2g1y-bp9I86wxWvPfyDVweBFLq4kCpUeYVdZtY2zJjqKpXX7rCTWpnUYH_qvH0T2JIDcZqpFA2foKogDLI75MML-P2aEpCIrWqk7fbWMnPyVyQVVgHQZdpE4-GtmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درهفته‌پنجم‌رقابت‌های‌بوندسلیگا؛ شاگردان نیکو کواچ در دورتموند درحالیکه تا دقیقه 85 دو بر صفر از وردربرمن جلو بود در عرض تنها هفت دقیقه دو گل دریافت کرد و 3 امتیاز شیرین پرید. زنبورها در چهار بازی اخیر خود به پیروزی رسیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31488" target="_blank">📅 12:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31487">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMX1pp-42tcCraI22Ar1ppgYsL3RbiXsErIuTRfF-GLUkf1YNvI1_l07DODunYaLyokOWIPaJRodz7-GHSWW0fxoh2hSDtH1u6H44Xb3HAVMtxKmW9DK0BHsI3wf-sRjs_dw66jYkk56aLTaerOggJyj2dMgXOwa-_sSXejNC6GPdCUlL3nR-eyYeCLDy_5NGq6Kt5sx0QS5KlV9T62GE6VzBE3yk3u8OdWDOfrvx8-uXHIVUR0Qvp9LK2Dwk6Qh-1Jl-fPBpU1U2zA3FzbYQKRSaLqkdcsMIH9MnjO10NAoHYDkUFL9fMTwy_H4G6jvJ3FByTdaVt-9ekNlSw8Bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکثر مسابقات لیگ برتر مصر رو ایشون گزارش میکنه و برای هرمسابقه 5 هزار دلار دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31487" target="_blank">📅 12:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31486">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l16qSgV5xxcVwrpgRJNhxplnwBOvr1TuqpnXZNv_45PZX-2-AA7FneoMZ5z3yqKdEEvRc1p7hS4vQ4MRiCbnUau2ANVLnZq0lsBt8mYwQqXrF19KxXW6YZiCkK7nbH1rhpAFSAEt4Bcpzt4h3KT709v8BPHGYQmZymiFtAXa-KaeRnFU2ZTohHpbAtPd4LoOloFwf1K_XzybBXeyhR54M-SZ25IvfvcaqzN659uEXuWkFUdiLKtuGyNoH9ngvU7rzA-Oyht7YoapDdr3H-ljubyyvyHMtPJKO-yTNwNcOeJCA_yIxQ31p8vSW9IpBym-9madzReWF3_7RZvIRpyDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسیرسفر گلگهر از سیرجان تا بحرین را مشاهده میکنید. پرواز از سیرجان به تهران، از تهران به نجف، از نجف به بغداد با اتوبوس، از بغداد به مسقط عمان، از عمان به منامه. به همین دلیل خواستار به تعویق افتادن دیدار با استقلال شدند که مخالفت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31486" target="_blank">📅 12:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31485">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=nop_MHysKAOu8stozIMRpC87Dv8ZPj2EDO7CinPkLMdRAyG7TwzcDdhTFqtd9zhWFJNwigZC-44zjGQQKjhoMfdDzLq52YtkX3RzzmcelukbmVrqJ_57W2ya3_jeiIYlLyHXUoJOTRRUNsm_UIczWnvjKfSgah1BnawdVf16jdRKlKwFJLoaZps0GqGb-H4ylVetMwZyQk99k2ZSc-SyNpsh7RtKGejKpo8R2tTse_GnbsXCp5qHBRYTT7JiNWzp4_jlDT4Qx8SuacU05PAgMsvhJA33PNDas8kB3GQczli3mmkYlDBNuQpAkvRsEZTPfvKQsAVuxpvwynTfMXyXox-U5zpur1uHc0WChTSJhKB70arE6grrD1w356p1Lj5i0Fybv3F2Dj7B4MI96ic5LpnXpYj5wAcHa233x-fNztVubRXnyGxbRlgBdabXeLMjLpG_YI6vxBLHz0cLAPW4osileKFPcdBEkczdIlCSQZ4zDFPApNVpaXtWLu1wKeWOqZzTJ1hkUgxzxUmkEQkO21sGsAG83hsvhVRjCBNaXiaoCR_AHQQ71hj_ZGEIJ7kY5yl257U5NUYObPPKEbaY1LOyzdyANtCWZ4VkEBJAubzz2WTawk1HdX94CjKMYvbYHYzz_0KOfRPb2P3Cq0cdX8oqSk8bxh3reQuTe9m06Ps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=nop_MHysKAOu8stozIMRpC87Dv8ZPj2EDO7CinPkLMdRAyG7TwzcDdhTFqtd9zhWFJNwigZC-44zjGQQKjhoMfdDzLq52YtkX3RzzmcelukbmVrqJ_57W2ya3_jeiIYlLyHXUoJOTRRUNsm_UIczWnvjKfSgah1BnawdVf16jdRKlKwFJLoaZps0GqGb-H4ylVetMwZyQk99k2ZSc-SyNpsh7RtKGejKpo8R2tTse_GnbsXCp5qHBRYTT7JiNWzp4_jlDT4Qx8SuacU05PAgMsvhJA33PNDas8kB3GQczli3mmkYlDBNuQpAkvRsEZTPfvKQsAVuxpvwynTfMXyXox-U5zpur1uHc0WChTSJhKB70arE6grrD1w356p1Lj5i0Fybv3F2Dj7B4MI96ic5LpnXpYj5wAcHa233x-fNztVubRXnyGxbRlgBdabXeLMjLpG_YI6vxBLHz0cLAPW4osileKFPcdBEkczdIlCSQZ4zDFPApNVpaXtWLu1wKeWOqZzTJ1hkUgxzxUmkEQkO21sGsAG83hsvhVRjCBNaXiaoCR_AHQQ71hj_ZGEIJ7kY5yl257U5NUYObPPKEbaY1LOyzdyANtCWZ4VkEBJAubzz2WTawk1HdX94CjKMYvbYHYzz_0KOfRPb2P3Cq0cdX8oqSk8bxh3reQuTe9m06Ps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31485" target="_blank">📅 12:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31484">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUdgA2gSrV9hP79JCyoiPtJq515IE9Og1aVw1iDY626YZXSRh5bbPRTgmZ-hVJTIwyfgcxCX_iX1yFv4zdfiago8Aqyb9alKGDCR9lcClGoZRBNn-hunCPqmZWOQ9duwEhejSG0TQU_KjXdyM4a8KZZ3M0v-70wdMGC7sBbGt5TCNIG5Lh6gxLau4wvoanBdkWkegyQ_BUdv-v6G809RG4g_PGSFFVL-1l9CF6UKgUxX1dHgxOrrPb6D5xwDuqzeNfFSG1M7qjNV9opCEu8WTfOdCp7uM-S52HHXWNUxy46UjMZ6LuSWQlbr-8fH4tuwXqpdArx-b3SW1-0O5Q4zyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
با اعلام رومانو؛ دنی کارواخال مدافع راست رئال مادرید با قراردادی یک ساله به ختافه پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31484" target="_blank">📅 11:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31483">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL9cnIGzI0QUyX7afBzqrcBUOMNF46Sz2Av1cc9bxWGHlyseCOU3bIFjZzngcqdOlTbgm_82j-NHluDbFQ8Ut2jnK6uipHnX_Hg326ptMo0jVESlANpjQiB5NvNsx-W7i-Y1f9FlyVpxmKtBcanrrwdOWOs2-DkjM2ctNwFdOCNM_nYv6dr39TVQtooW0bEMdt8mlG7FwVYCdN1wEJ6cmVnXP7AIOf5dwCmnpUrYpu1TR53fwZa9JOeTjm136q_Eg_xEqCo7Z7FfRar_QSTj2G2Jo8wOZ7EHWlL7cyZXgcqYXSaAyrMaMl07XVh71O3GR02ybw47br9B5BAvVm_NoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمایت‌تمام‌قد کریس‌رونالدو از کشور عربستان در جنگ با حوثی‌های یمن: جنگ هم شود از اینجا نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31483" target="_blank">📅 11:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31482">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWlyUmXjvsszo72SQ-WHTZH-lqL3_cFs_gxr2LPgSbvtc7Lk-ObKmV4siR_d98d89II0w7sAQkcoYl3wnMTUWstwN71BSUxzTn8rX1GifQU7F7OSOhnwnlulxynbcpmrt4UuwV99u9DNo8sh6xEM8_42jjoU2L42RYlv_gki7h0crE7Jwmgpi6rCuMwIFrl_V76yQV--p5KeKSLVuKeWK2ravkrtQHLmYUNPxiRDMdk97SCRyCuy3AETSO3Kwc8qITb8OEVMDjEjpqkA7JWPF4MIpjlI8cfYVxudxD9BswEvD8VKNe8jONMIAociqhum4gC2325NGD8oXcQUcws4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31482" target="_blank">📅 10:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31481">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvAd1Dn_ZvTdScoR6Qp-F2KtE8E_qQszPFSCKv15c3yYQ7wJoHj2aBU9lN3lbAGdEBiZjcYMfGGYwPSHFBXYWVQlxrCv6pDB6lxkYl0BqyXS3hKcCyaGcENLTWIFNxLpa-OdSbnq_FMP42H_VEQKZdWkXQiUdl8VoDyGQGB6hdPzX2hn5m1pml9Z_dILSbnlnu9eyVx1xtb47ECDzuP7XzzCsRSk12ioSjG_RucanM9-Jv3_rZFWUkdB7T9UTwk-qEzHs1xCoAFAMRUPTL4Q-1VLexEAmBHEQftSgHpks8AdIxPPhWXTRpYqt7u5jm7eVE39igqZb5fmFodVNjP3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
برنامه‌مسابقات‌این هفته رقابت‌های لیگ قهرمانان اروپا که قراره فرداشب و پس فرداشب برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31481" target="_blank">📅 10:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31480">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzVRL9LBD0ZikDtHmfQIWSxpFlgan4LbFGPIGHwEvduIjxfTLMN4W-N5VgZvOckyTO9RewtVMkj166acdSjWGIVhU_YkZx6loT7Mb2WxeZJOkgnl4uV2tzAEAEHYCUxJLvu06fdqTcKt4g_Tqj89ytlOx0TeKEyq20xLsFV5lzzzQgNrOLqpP-6cfMYrPirxdlKbg-RugeiEpempEQ3cjngzUhgAIxItBSfFuyQNxRggbxxvmAVYTN0vo6w2Z2Es8mITiWnw9-YwY2lB0Bl55UP9jC8h8JIyIVrQH5gNZy62vYVvoz8wMJgbFdK7KeCCmKkYiOJAaMcBgfQVB7ZzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
👤
سعید الهویی دستیار و همه‌کاره کادر فنی امیرقلعه‌نویی رسما گفت که مهدی قایدی بخاطر اون مصاحبه‌اش باامیرحسین قیاسی خط‌خورده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31480" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31479">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKxSdPc_d9ZoK9g569LhZm8L1534AWkA1lCqucr9B9oXdo_5qMuq1YICurO6x7VIqZqxhxGpC4rRTbOleMdu5YrMtcTQ4tgkqK6ksyzJy251SVY1zVfJch1DfdV2Fv2AJ78f4IrpXfig3_00H2bt7uCfB7gzqRt1h4dgLI3QQY5J9y0GROOXNDvBdyH_TSTtn79SLnH3so5nUmlrYq_QB8iiz5NVzpbLsEK5jRR4WFIKHFEPpulgRByiKyPnmxj6D4kcGSmolDpd3Jwq8ZD9NDknEB6m1uyviPWY_HaCKhijrPWeEsfmHls7OmtHR81Pz8GtaqojnilwFXfBtYzjZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته نهم و دهم رقابت های لیگ برتر که قراره از شنبه 25 مهرماه استارت بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31479" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31477">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=doz0l9NAtR97pRlym5g0FSC46bd-XPXSYg4qT1nYIx9z8L51N3N7XKFCUsVbQF5N-EXJHDfaeuiexTGhhDLnwSxCm40sqkUZ1ByM6U5dHVAwAkYBJ_sjXhFIFDW7jBsAsch8mH7Mel5Qn26tbeBVyhnbv5ApNJsMUeSdTkO4dJxAh3plkQaDsee9r_9mM7sYC6xCFjd47nnR3PgXiSUOXGPRjPkgGgszFIoX31DImfR0RRdagBKgnIZrXIr6HSDW1kknItzNC1SRDNQQQAQcAXFLU1bC9ZjnrqXmRlbBQyF4JL-yjzQP6PTa6TsOLXGL5Vm1sfzrGbho9Fq_aMxjLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=doz0l9NAtR97pRlym5g0FSC46bd-XPXSYg4qT1nYIx9z8L51N3N7XKFCUsVbQF5N-EXJHDfaeuiexTGhhDLnwSxCm40sqkUZ1ByM6U5dHVAwAkYBJ_sjXhFIFDW7jBsAsch8mH7Mel5Qn26tbeBVyhnbv5ApNJsMUeSdTkO4dJxAh3plkQaDsee9r_9mM7sYC6xCFjd47nnR3PgXiSUOXGPRjPkgGgszFIoX31DImfR0RRdagBKgnIZrXIr6HSDW1kknItzNC1SRDNQQQAQcAXFLU1bC9ZjnrqXmRlbBQyF4JL-yjzQP6PTa6TsOLXGL5Vm1sfzrGbho9Fq_aMxjLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دستور محمدرضا زنوزی مالک تراکتور به حجت کریمی: قرارداد علیرضا بیرانوند روفسخ کن. او دیگر به هیچ عنوان جایگاهی در تراکتور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31477" target="_blank">📅 09:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31476">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=NbZkLEf35xm6O5kJxNwNNJqmty2CmOWWnIPcujMoeW3K1Ht8SuOxhVnCpRw88LWreykMN02pWGmlpEfzOkVDZH_LiQwT7X1ljXCPVm28xBmLNfADTKfxwH6InrCNf2LWA6CLUdtAPrOpZJT6LNSf1yZ56VnQdLXfr4G3KMSmiwitGKPlCVihfzfcpYDTN5n7h43EPMEGKoKbOAxhJ6HQt5lP5bApK4jVfYsGz9nuOzUuS8bFqDiz03FYlRKNRfMQWDTpedGC9FL_SvdiDaQfSEtdA8P34EzzhjwgCKb5WuUNwvz3nNtYv68QeYGRgYMTEJE3Eu3g46pIe_hcAH9YQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=NbZkLEf35xm6O5kJxNwNNJqmty2CmOWWnIPcujMoeW3K1Ht8SuOxhVnCpRw88LWreykMN02pWGmlpEfzOkVDZH_LiQwT7X1ljXCPVm28xBmLNfADTKfxwH6InrCNf2LWA6CLUdtAPrOpZJT6LNSf1yZ56VnQdLXfr4G3KMSmiwitGKPlCVihfzfcpYDTN5n7h43EPMEGKoKbOAxhJ6HQt5lP5bApK4jVfYsGz9nuOzUuS8bFqDiz03FYlRKNRfMQWDTpedGC9FL_SvdiDaQfSEtdA8P34EzzhjwgCKb5WuUNwvz3nNtYv68QeYGRgYMTEJE3Eu3g46pIe_hcAH9YQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش حامد لک به صحبت‌های بیرانوند علیه علی دایی: طوری می‌گوید در نوجوانی کارگری کرده که انگارهمه‌فوتبالیست‌های‌ایران در خانواده میلیاردر متولد شده‌اند. ببند دهنت رو بابا. حرف نزن تو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31476" target="_blank">📅 09:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31475">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=D2G6a4-gD3BbdPF3UXDMoAukceFD9tKcQUc64ua1rCltSvs_pGGC6mBoutZ1M1QA-S9QPVfcYWbfnj9JlaU2W-A_8DE3D-pHWuq_sEYpVM7qIxP3wXm4P2vHB_CHQUwzQkHR9aKKsDnI1pGZCJbS6fIJ-qrP747GYt9XpnuNjHLbpbcNGjk3nBkvH1IdQX2H7EzWzAbPakcmO6bRm-yJD_VWhAX5cM1Jj8ht6SPGoL7vuittyM6v4qH16p0FObaup5Sb9LfO6uLnarvMXvtYvGKwRY6QM9x-phAR3sC6WSmB1oMdEhyrXcK5sdj0pO4lbY6EkmIH2uGIE3EngBCT9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=D2G6a4-gD3BbdPF3UXDMoAukceFD9tKcQUc64ua1rCltSvs_pGGC6mBoutZ1M1QA-S9QPVfcYWbfnj9JlaU2W-A_8DE3D-pHWuq_sEYpVM7qIxP3wXm4P2vHB_CHQUwzQkHR9aKKsDnI1pGZCJbS6fIJ-qrP747GYt9XpnuNjHLbpbcNGjk3nBkvH1IdQX2H7EzWzAbPakcmO6bRm-yJD_VWhAX5cM1Jj8ht6SPGoL7vuittyM6v4qH16p0FObaup5Sb9LfO6uLnarvMXvtYvGKwRY6QM9x-phAR3sC6WSmB1oMdEhyrXcK5sdj0pO4lbY6EkmIH2uGIE3EngBCT9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دیدنی‌کریس‌رونالدو در بازی شب گذشته النصر مقابل نفتچی از زاویه‌ای متفاوت؛ CR7 بدون نگاه به دروازه حریف توپ رو وارد دروازه کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31475" target="_blank">📅 09:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31474">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFkkWaLSvMbogEM9ZRk8An3pit8ag8V5QjOIiBsMHv9E9qp_1YeLqN3Iy_L37JqdXmTZsP2S4o14WMUFruAelRJH-MKNR1PlHFvcLw4LFDuI3sIQqY1tS3T1NcAuK-R7-wJypZ77-opnGEW_B3isXAdsWSFUB5IWv-K0DEjb2GCyOw20_LHMRlEEACDoeWPgHECm_HfCSE28luPXyTDtnxOoEmfN-1trA95cvw9zWqOIbDfhjj55dYUQQAOUKcl7mEDSzva8rY0uxBJqIzdaIyDEsXLUi8hlHCN9PluthZB1irEDDVg3Iw0Xbh2dnfDsevfHieJ9F_8i5ojALlco5jBqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFkkWaLSvMbogEM9ZRk8An3pit8ag8V5QjOIiBsMHv9E9qp_1YeLqN3Iy_L37JqdXmTZsP2S4o14WMUFruAelRJH-MKNR1PlHFvcLw4LFDuI3sIQqY1tS3T1NcAuK-R7-wJypZ77-opnGEW_B3isXAdsWSFUB5IWv-K0DEjb2GCyOw20_LHMRlEEACDoeWPgHECm_HfCSE28luPXyTDtnxOoEmfN-1trA95cvw9zWqOIbDfhjj55dYUQQAOUKcl7mEDSzva8rY0uxBJqIzdaIyDEsXLUi8hlHCN9PluthZB1irEDDVg3Iw0Xbh2dnfDsevfHieJ9F_8i5ojALlco5jBqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/31474" target="_blank">📅 02:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31472">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEGrT7ATNs7rK4RgUXiSMZisOHjuAV5ujxznm_E5KNgDW-aJxP_jfKcErPZd2Y_zdaE_dTRPuzTdXv9ptFjLbAM6RZ5c3JvXk_6wKlctqV_wuEW2JZwNbRAPLZh7wqKhAgrXXwvZRno8KrPio47eIgCGblDUEUfhPpdFUixobPLp8yUqRFxCJT9kTcd_r_V01CUiH1B7-uDZ8pyv1h_4Xy-a_SzJESuAAEvl7nPSi9KWp9w2S-1jgFgxp01V3hka6ZgsEh7zLYbC1JHnVEkqmhFR9pJHveScsreL5kwIB3iCcg-cgaH4m9wyvQfCePyPHRqoch-pNRH7yKxStVBZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/31472" target="_blank">📅 01:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31470">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QADNiSHg3fZteQzI-b-LWRZG6Hkokb1ivcYe3v2ysCyyBQb7pNg5i9lemabSc6FqwXDK6YfQ8a7JHRMtCWu1bbwRxZtAFaFXDaxnPPAdueEngKIXRiYq30GNkEQXzEWwrLhf_MCiu4RZJsFmPfKjUPpD3e3nzQRKviNB96URwOiZiny-0VGztg0-LWztYW9EWFjUUXqGTrEnkbuM5jHZBS9pZXN8M3VqLGR0ZbTFtceynURytEUs6GJq-s6X83PhwKDe44zJlP1yxBAThuI8BRwXCmpxAE0zl680bSyl0_QNwTGN0qncGU5vLZt3ViZ-ZG_c-Q2qQR_vp6kND28hMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ از دوئل تماشایی شیاطین سرخ با شاگردان سیمئونه تا نبرد بارسا و گالاتاسرای‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/31470" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31469">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btMJUlZnw1e-lVdmtp7EdGqWQka2qY-Xc7hXLkpqpHTTT8CCYffb-o37X-LVHa7WIjcIVzzPKZN8t1LoGVbhlJ7aQxq-KXOux5izoLk2ItFNvcuY80cuOFlnW2SfUujVyzK-zSob6JT9WOSbT3lJ3Hz3fdx22qFYTTwRIh-NyeMYtB-zx7hoBLYVxIN76EuRWZQzTigVjwdW0E1Q3ae9VkngjP9gDzFzNezNpLOOrb-fhgkav9UzB-D6NdFJkFakgHsyQk174k6CDo8swcTuVr_YD_RQFYGy86XVmC1vavHGB_HC4cQzur3nO5w4GYGXgS08NrB_Twq8qMR-8JxHQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
دومین برد پیاپی استقلالی‌ ها درلیگ‌نخبگان آسیا 2027 با سهراب بختیاری‌زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/31469" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31466">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L63Rfsg8lspO9jFL8ugJHQEUUeJw5P071xITi7cTTjnDntwdLGCLWl7Do1riPtX2X8Zb_Zn4QISExygIUPP6P3SsTwI51ZJdIJmHzLcD2BWeaQnR9YFIoATomUX9bWs8nLdnnto0-xnjSjHHsmmeFLPwzZB3LAOGpyQ2L5ubs0GHFpFdz-N99sJowHBiDuEulpIWANKut5q61IyWanP68qbP1bC2Pfm9GsE0e0Hwi8SqgrXzAe74noe1AxmlK70iqqw_dCi1VdOKop4vrUJ7MtmW_n5C81F3SvqYkf4nIaQMzrEW_XZy6YsHDiSzBYbI3hemgfORYWDdHeTwmg-vUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvLkT8YzIEEL7b4Q1Cavtosw7eamppeWlSeETMwy2ja0XGDycP-eygAc26JZmRFC4dDQmd5ppSyglrsJtP3KppPkURiNI_M3ACnTqNnOisAPt0WGNhGxUIag_-UoLE_VhJ8fP3T9ARFnIofD28p9sBbpVt-SQmhvFi6GU2la4XDw33uYF-dRejDnvwdWcDgNmWPpvTM5wKC_RkJuv_iC9gg9P3MGY_O1ZLAw2xkCDDJQWx5zFPF7q6DAiXgMBJvEDXqq-UPm0gWfijnm3wumb1cnh0LzX9tDy3NLg5QqEO4_mPcj93nuM2CbiwgJSUflB2LiS310KLdCUTWiBZHe_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/31466" target="_blank">📅 00:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31465">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lejdAiShJ4n3u1sinwQmYfmwZEjfgxp3Sg178Xy-HrHFwv4-Gnz2yJP3OYrF7WfpG7Gkr9-LXs4USe0bwC4DHpbGwSMmRmbCmJiLm1IhekfqNNpz811rxbhSUd02RTLCTk-CntzqlEZWRD3EKm92PVJTqBTcTz0WyrTDcft_YJWs348HWKNykVnqgsNrFnTQ2EH1IyKldumBFvVkvvJ0zjhvtC9R_qmtYdStoyBUe8p5V6SRsG-ctfY-drS15wkHSPJRVAJfNzqXrJDH1zk-j4MTBNr7mTH2ImV8y_2CEUzbcuLQ6vvRByqT10VIj1KmEHLsuc5xar1j8PoneUQrkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/31465" target="_blank">📅 00:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31463">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeZvOFjFpVl5tz7OsFEdcDW59w01O-073GEj4iQiazNJATzFYQDhJGANK-8xkum3G7KnXNjZQhEIVpfhQzFkr0xTev20WZmXVbUKfkyOkKJpta_iyQzq1sUnTWS0oLFfJIE9YWFundK755B4VaWYzdD-iMheB9Y-IYV6lfXngDbfhp22zV0JPxTk9vsbiTsCamo9sTGOXD9mIaSJizkGXdUrwBNJsRk8TjK_oprfpLtJhNd7CXpvudWnq0haziOVlTGjz67eLQ7U9wOU79K2XkRDTXz4mTiH1_iJwx3Oiaq3-TgNqKuDCs2PAx4tKv0_qsLNbLIifeu30fD0ZTA7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ یحیی گلمحمدی سرمربی دهوک عراقی توافقی قراردادش رو با این تیم عراقی فسخ کرد و به احتمال فراوان با عقد قراردادی چهار ساله سرمربی تیم امید خواهد شد. فدراسیون با افشین قطبی برای هدایت تیم ملی امید به توافق نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/31463" target="_blank">📅 00:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31462">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyeT2HBJlmL9DEbdScd65f8IOGqX3WRJOn1sWEWmEmynykqjYzupYw8fIt_UYta6Da4OlMHtzfkcW6bUGTAfE1fesP6-RKRj7QzMyuMmvv3tfKxSz5uc0beYqXTCrFC3BDYOINy4tz7j7JWnTK1rHvbrF5LZVbMBbVLSSlSkw92vPh18_vd3PdS2Smk1Wi9PmO6ghXcBvlaxYwUDrSmi1wL636lBxTYJF6ET-h9UzH0TzJ7YNLeSAWxfPyfBXCXSK2NcBhP85kTE8xm-wgjQucWk7WKymIrBsyUT5pNxpnkHnUUFOwFm9EhrbgPiVR0RLXrAtfYTMHWDHhCyRa3c8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگام این چه خبری که منتشر شد؛ آرجی میته، بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، به‌دلیل خودکشی در سن ‌34 سالگی درگذشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/31462" target="_blank">📅 00:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31461">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=luEgfU1PuGtBqRsruV-BxYZ_XSzPVD3gasVL7xguj14pN3-B3XcuzjOVwRWj8yEeJcORxfp0_TRDn45qO0IPedblyBlpU0zKVQjd6Ta61aHDSX_vch1t8FqQetEEwYL8zatldl3Oil1oirCoE3K3KLkjBuqZHdqASptiRUwO-kW2pVXwqAZ5anJeguOHUXXmobnJc7XF7_6zbFqCXI-WO3jn3lLoF2Q46S6HaHl_OpR8gHnPlWoVUgvfLNhOo3PuoTyNR5K2Ndi379dyMF5c0ccTwwJ5wl70FyM3-oRVsvObD8FIwpQUQbq7-WjvOozOCXE4lPiZwvRHRF8XPuAZLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=luEgfU1PuGtBqRsruV-BxYZ_XSzPVD3gasVL7xguj14pN3-B3XcuzjOVwRWj8yEeJcORxfp0_TRDn45qO0IPedblyBlpU0zKVQjd6Ta61aHDSX_vch1t8FqQetEEwYL8zatldl3Oil1oirCoE3K3KLkjBuqZHdqASptiRUwO-kW2pVXwqAZ5anJeguOHUXXmobnJc7XF7_6zbFqCXI-WO3jn3lLoF2Q46S6HaHl_OpR8gHnPlWoVUgvfLNhOo3PuoTyNR5K2Ndi379dyMF5c0ccTwwJ5wl70FyM3-oRVsvObD8FIwpQUQbq7-WjvOozOCXE4lPiZwvRHRF8XPuAZLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش از بازی با گالاسرای در UCL
؛ یکی از خبرنگاران درباره‌وضعیت‌فعلی رئال از هانسی فلیک سوال پرسید که اون‌هم‌عصبی‌شد و گفت امیدوارم بالاخره یه روزی یاد بگیری از این سوالات نپرسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/31461" target="_blank">📅 00:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31460">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN5Xr6vdM7BBKNJNEgvD5qx0PEm6Rc5yqdanNaaNtEy-pcUs7YWzTM0-Ngj_xYZfqVef4kvlaEOZaH7N6S-Xy0ZunAbSJF148cc6Jg3kxaH3-9oUsfkrFPabRSQ1a3VF67b7BZClG7LpO7Wsy5P3gk8jQ4CGVySFuz9AFx1-KNPtm-e03GbetCMJYJIzkJDq6zg01FH3tGcEXYNh5DhTCIZGjFHrFom8ZTXNdQCJ3WNkGFKc-nw03YqKmcQRcuzjKl0cXBktv4uytcXj6JG4Xgai-kGoYtPh34qrqf9RdmBC1Hr8CN19Dz569UNrC4Y2u0iw9XtGRkLdNJS_GcTyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/31460" target="_blank">📅 00:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31459">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApP-qq_rvZCZ1B4F6Q1vjlu_7AE_xylGABeAnXsh3wpjyhwPz0WLCS9gH2405AnIpzwS2U7_Ue8vUrwdOVBv8wsk2C0Z8mryyzcMZEQNRkhVpXei3_bKdAr__i6xD3yAPmT8zw1-nBKS1TdJME8-udPRFDhqFw3j1Z8iNQzPhc0BMaYwVJYybPsaHxXE1RFnwN27Z_OFyCaC7jCpoHtNEz4Y9_ZKTNCKSVpHGDkrZyUAs4sEtqMqNDC92r3nGLVQHAuNs5PiDC3BXfyc4urFvlPm-uJ22sDXNO6muOKAhj2SluZ1zvbpAKoS74ffvUTgM00vRVSJ43lVDyJf7xXeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/31459" target="_blank">📅 23:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31458">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYqntHYZYqIwMizo2jyXQDWdM0f1ovZajnQ_DpoB4e41U2dAoG-oz3FvwbKNglEVDzfnHfLSlBRzkv3r2GwcYFpKKPVS_tjFbn6ZK4yXWqoxz1gZ6Vmrzy4AzcHlhDsXBE4bUgANCdu0t1Ro_ktsFgpnU0cw71k1KkPAmFkc8_xayDNU8TDrwKmJlDUovPbV_P5JwTq4OzR8ylkq4n0GWuWhK7le187Pw22JRgJ4Vxqix63CjccAd0VyJxmbzhVoVvrxxi8ffELf3V8DkLsIsTj3Puf1E-jHwJpmeSv2rIryOOUFXlCvwENHWDN_Np4yxqvc5racnfngB1oxnsjXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/31458" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31457">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57855f950d.mp4?token=qKsk_h2yhEZDh6ClOFh2l-s6stelfw5dLoxN5ki_oA__ju-9xMcnUrZeBc2T9tWko6u6Al6VrGFsf2EQ5HyH2HpbEdbNQmq57sOAzsFY72UDr0-OsjVRG0N73zy2MKCraIXAS6aNF0zxmXanI3YbDcPKXorDhRh83IAhHt4kPIGAuQWJ_sNPm34qkvK6wjFJIOA5To2OIxS3jaSQjCsbcpUwUSiYHWVeCLd10J6-z8XiSEvxdzI_5BmNanb7MCzlyKoP9ozCreeT_WiEn3uGqxYeQWLLXfTiI4fz1x0vYVVMvw9u3_Js3NKt9hplAI72nR3fTvoUucPoL2juaJWf0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57855f950d.mp4?token=qKsk_h2yhEZDh6ClOFh2l-s6stelfw5dLoxN5ki_oA__ju-9xMcnUrZeBc2T9tWko6u6Al6VrGFsf2EQ5HyH2HpbEdbNQmq57sOAzsFY72UDr0-OsjVRG0N73zy2MKCraIXAS6aNF0zxmXanI3YbDcPKXorDhRh83IAhHt4kPIGAuQWJ_sNPm34qkvK6wjFJIOA5To2OIxS3jaSQjCsbcpUwUSiYHWVeCLd10J6-z8XiSEvxdzI_5BmNanb7MCzlyKoP9ozCreeT_WiEn3uGqxYeQWLLXfTiI4fz1x0vYVVMvw9u3_Js3NKt9hplAI72nR3fTvoUucPoL2juaJWf0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/31457" target="_blank">📅 23:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31456">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYssitxwQ0IS5guY-5RqUnsosM3T9wV4xDLSzDLr7Cdv-RWOLP-XK8Rscx6i5jrvviOdi5pcbEZrOQvL4KgiMJxQU_FYx5AIFyERhJDWpKaOIgJwyX4LlByaoN6q-CIPbAHljIXgheen6jxhfAEx7jawqYqRPNqm4ue4kgBPsiRz2pqgP43Fl5paNLvZP2EHpeaOsMH3LOR6UQ4Mxei8o6AZ9YVhpwVh1J-8Kj-yKB27wn1T9KAfA5vgVyk41G59umLEy9Bn0b-UPYF0IOMCCNp6kudznR_Vpg62NySJu_B9HSxZZvk09ZWg27TLA6PQ5h40ww7QnRWNVvqsBsYZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حوثی های یمن: بزودی تمومه ستاره های فوتبال از عربستان خارج میشن. کار میکنیم که عربستان نتونه هیچ‌فوتبالی‌رو درخاکش برگزار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/31456" target="_blank">📅 23:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31455">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=FdGPL1FkBdSSwcQICL23_YppoRGc5dR4ViTpyl6N5AQacJ7vJw1Liaq3WJ24--eLGrR8PJY4rUNnShqgqvu9pp2tp5jrYCojG-qOnY5dFz0UnTR9wIihqTsWhQPVwPRqnrycjvdhr96Jem3s_uYQHVVKZKWZB38ix5gOio-MB_4yX4wLQxRjZwBh--SxzCAPj8sFCO-maCrxNpTIWgVlsHusx3Gj7sgey5qPV2GgSe29Cf2vAuIP1Lj7mNt9CsBxzDrkSn9XzSi31oBcnZFT2BbwRh6l62hPkSDGj-sdxoMMBT35_wz6KoGwazG1eWhrNbY_-MT9sNRUjJjg0gu3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=FdGPL1FkBdSSwcQICL23_YppoRGc5dR4ViTpyl6N5AQacJ7vJw1Liaq3WJ24--eLGrR8PJY4rUNnShqgqvu9pp2tp5jrYCojG-qOnY5dFz0UnTR9wIihqTsWhQPVwPRqnrycjvdhr96Jem3s_uYQHVVKZKWZB38ix5gOio-MB_4yX4wLQxRjZwBh--SxzCAPj8sFCO-maCrxNpTIWgVlsHusx3Gj7sgey5qPV2GgSe29Cf2vAuIP1Lj7mNt9CsBxzDrkSn9XzSi31oBcnZFT2BbwRh6l62hPkSDGj-sdxoMMBT35_wz6KoGwazG1eWhrNbY_-MT9sNRUjJjg0gu3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
قطری‌ها خیلی زود دومیم خوردند؛ گل دوم استقلال به الغرافه توسط گودرزی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/31455" target="_blank">📅 23:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31454">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=T6SbEizysu9I6SwlhDOi34jawK4ixcSESzPF_4VS-vpAO1F4sKsOKQBdip-CccE66DqBCTIrYv6GhYtq7TUqQAXioh82vUhnpQ1JMkb7UEdIsD7QZPbmhNzXHBVXpMgFlb2Q8jgJj8pmsolqzc_k2fYHkIcly5RopVVdz4dPdhwfYiwK6mpnhwSf5R3STDDaPt5WIsOCijMxPwMONxTjrpaFkRQqFZMHGJ7-RAjAbDYRhtfgb3nyF3oJVtrwr3gCFTT7v33HIbXqXBnhpIyotxjVM4tt_GuKvUc9nWNWi7objFbzmb88BtiIz_bjKWBv4eaeSZ1rhHM7plvZ1LStEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=T6SbEizysu9I6SwlhDOi34jawK4ixcSESzPF_4VS-vpAO1F4sKsOKQBdip-CccE66DqBCTIrYv6GhYtq7TUqQAXioh82vUhnpQ1JMkb7UEdIsD7QZPbmhNzXHBVXpMgFlb2Q8jgJj8pmsolqzc_k2fYHkIcly5RopVVdz4dPdhwfYiwK6mpnhwSf5R3STDDaPt5WIsOCijMxPwMONxTjrpaFkRQqFZMHGJ7-RAjAbDYRhtfgb3nyF3oJVtrwr3gCFTT7v33HIbXqXBnhpIyotxjVM4tt_GuKvUc9nWNWi7objFbzmb88BtiIz_bjKWBv4eaeSZ1rhHM7plvZ1LStEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آبی‌ها گل مساوی رو از قطری‌ها دریافت کردند؛ گل اول‌الغرافه به استقلال توسط فرجانی ساسی 48
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/31454" target="_blank">📅 23:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=AlcZWokTdxQiR119d0jX2MJMmvEjT5-XnkPMHTbtNzjlKP1l5Q9BsbLpBa1G2z66YoHAiE8-rAgVJaomB-i9XB5P8dQ4oN9R6sU5REyj0RRt-HndBLkMfgtXY9qPhMDRQlrekEVUOCXHbei-GSyLSC6yL2N8lt4t2uCijvwoXncZNaY7fgbSQXYDTcjRLLLgaz0iw3VFvQAnHFyexPxtfe4DU5hjr0fqdX4A4PZejQ__ZALEldkSkQiurgr4s-p5f67qtgTLBr-zwMLlFzp8BtYx0vgDP72yceHiYWkuddfJtODoN9bjiGxtS-SuSjVYnGSesmhx27ToGx-lrCR--A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=AlcZWokTdxQiR119d0jX2MJMmvEjT5-XnkPMHTbtNzjlKP1l5Q9BsbLpBa1G2z66YoHAiE8-rAgVJaomB-i9XB5P8dQ4oN9R6sU5REyj0RRt-HndBLkMfgtXY9qPhMDRQlrekEVUOCXHbei-GSyLSC6yL2N8lt4t2uCijvwoXncZNaY7fgbSQXYDTcjRLLLgaz0iw3VFvQAnHFyexPxtfe4DU5hjr0fqdX4A4PZejQ__ZALEldkSkQiurgr4s-p5f67qtgTLBr-zwMLlFzp8BtYx0vgDP72yceHiYWkuddfJtODoN9bjiGxtS-SuSjVYnGSesmhx27ToGx-lrCR--A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/31453" target="_blank">📅 23:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31452">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBeSG-4zTg3L0FHCBDFrMaXKYlawt-BVqBN6P0o8Pt-lIN0FN6vTuQGgkvoJ-AU-RuWZXGkJTg-CTfpimlJaFqOREIGI7M-pmwzv46D-P8P_SZ11jDhHKp6gxPWbdQ2wdy3uVKTX_5j6ys1-eGqfWnpvOL3AFWO2gbq8LFjqnazKolghGVL4Dxa4-FtE7ZSfkb8tpfEk37VhqQ8kjzRemDISWWZDjWRD1KPy2WhoCtWJxe5GIXs7ZLqL3z55GXAf8tYiA9mr8Uen9eNGOKfvWftw9hFrxuR0REvAO8eDJH0IzAfQeQbVrqe1WwRoqBII1TLyfn8F5jkDbosAHI5tHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/31452" target="_blank">📅 22:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31451">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM1FOZUZ0MNlLaGyzn-0tDfIjOyRUe2JsDKdlvdZCHfWPBotutwIpq7a0_pvypgMhfIa858zbvfz0Kvt0XarvWP6NuhhOCZLLYTvsiEk3FNgQOR-iN0QbhrLLTLlTqxjpy9IFlGECAITTjzXhRwIfZ7roq6784zu3Ob-stqHyRg9MhVURqM0NkUF1gFv31Y5Nt-aHz4xvihRMYACnmPpk8mz2SDSNUpWlcYuyYmKB6j_NilBqll5BK8qW9Wxf4PJ7o2iNJQfIwxYo4WyV9Uf3W-2BRx3doaHLBt2xBTEAAeaoBzQ8zQDhXqDpF-ceS0vFnEWcU5YQsMlM7JnZ0sQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی‌امشب النصر درلیگ‌نخبگان‌بخاطر هشدار امنیتی و احتمال حمله‌حوثی‌های‌یمن‌تاخیر خورد. عربستان با این‌وضع 3 ماه‌دیگه‌میخواد جام ملتها رومیزبانی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/31451" target="_blank">📅 22:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31450">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔵
👤
سوپرگل پشم ریزون فوق ستاره آلبانیایی تیم استقلال بلافاصله بعد از اومدن به زمین بازی؛ گل اول استقلال به الغرافه توسط یاسر آسانی در دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/31450" target="_blank">📅 22:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31449">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=Mq8nN-O-5baQvY9_K84B-kPBbHFpGiREoOQVThcT2WLS80yTaDC6u5mPeIe0hZ-9u4PBHyEHdtaMl9R04zL1D6RjFbPPF_ldstMeE9WZ5nQ2TIdhv8JIutURO5yKE1mpgq0dJYfvd61POXPT0UEbxiFgEmu_u9vxq2-Pb2nWG4NT5SMhKs5XZKuH3yRkdALnB4JX3b5M875_ANKMncrGWPS0xhYTfCpjiSIMRqjuGwvZtJU1mh1oZVBTm73OjHBrTk5sTk01kCi1rB9BfIhsSvlJNvyfEWWOmYrZl-KtU8mM6n1IfdKrgXo2e4x72FmakXJax0Q33RGK4zilRR-r-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=Mq8nN-O-5baQvY9_K84B-kPBbHFpGiREoOQVThcT2WLS80yTaDC6u5mPeIe0hZ-9u4PBHyEHdtaMl9R04zL1D6RjFbPPF_ldstMeE9WZ5nQ2TIdhv8JIutURO5yKE1mpgq0dJYfvd61POXPT0UEbxiFgEmu_u9vxq2-Pb2nWG4NT5SMhKs5XZKuH3yRkdALnB4JX3b5M875_ANKMncrGWPS0xhYTfCpjiSIMRqjuGwvZtJU1mh1oZVBTm73OjHBrTk5sTk01kCi1rB9BfIhsSvlJNvyfEWWOmYrZl-KtU8mM6n1IfdKrgXo2e4x72FmakXJax0Q33RGK4zilRR-r-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک ترکیب استقلال برای دیدار حساس امشب مقابل الغرافه قطر در هفته دوم لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/31449" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31448">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=IohZNKTOfwGZcVTekDnQ8NyW3Nty4Wq4gC8PYsxJ-IRTnw1y23SJRuz-AalNPtThqvAcA5YhH5K_9PoG4RqPQwGhoeoc52wF_hEtjm7TA16OcltEWiJvwnI-om4uOO3HOwavMIySNK7UwAL5_HrZW1Vwc2A5InmL39CWGtScUtaLqA8YrAo4mIfO7Z068aDCKUsw8DDNHzZ8Xwpc8pgSzxpyGzQ81r043g_6rIfpGnEu7cScFJPICp55_SuDdjvLNZW9hzbIyU22tcS-XPBsLQ2YPyAoJe3RMtGbgvcPvK7YFg87Qz5hbETESmrHFgv76wh50WQ2w2dFG_H9FkjiFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=IohZNKTOfwGZcVTekDnQ8NyW3Nty4Wq4gC8PYsxJ-IRTnw1y23SJRuz-AalNPtThqvAcA5YhH5K_9PoG4RqPQwGhoeoc52wF_hEtjm7TA16OcltEWiJvwnI-om4uOO3HOwavMIySNK7UwAL5_HrZW1Vwc2A5InmL39CWGtScUtaLqA8YrAo4mIfO7Z068aDCKUsw8DDNHzZ8Xwpc8pgSzxpyGzQ81r043g_6rIfpGnEu7cScFJPICp55_SuDdjvLNZW9hzbIyU22tcS-XPBsLQ2YPyAoJe3RMtGbgvcPvK7YFg87Qz5hbETESmrHFgv76wh50WQ2w2dFG_H9FkjiFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به دلیل جنگ اخیر دو کشور عربستان و یمن و شلیک و برخورد چندموشک به‌فرودگاه های عربستان احتمال‌گرفتن‌میزبانی جام ملت های آسیا از عربستان وبرگزاری این مسابقه در یک کشور دیگه وجود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31448" target="_blank">📅 22:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31447">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=Hh5x66i8FR3M7JWziT8pvTa2Amaf-S26Q4nqxz4oqchZ00ltnkhKAW3oVgll1o7ZQE2C9i6pqe_o5KW4cvMKg1XAUypmdS931QBTZeGKo0Bz-bhBF_IFE6jLUssvOQw7NgvoFq-6ioxbtuGo2B2VOwtOKA72vFjdwoK2THQeidOj1rOs1C_jJ2L2SV2wSCbS-QLAoXXpZ6hWX19cw5QlSo2oqHMBoIj5KO8J87s-61VwNthALlwRLvOC5HU6bt-Zoav6_v_YDDTAPK_4bMS2pdH0tIcuowAwy_S_yclOg7Qh2nLRbeo866BEv5r6I-cIC9-BWnKoht3tjDg3OQRHwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=Hh5x66i8FR3M7JWziT8pvTa2Amaf-S26Q4nqxz4oqchZ00ltnkhKAW3oVgll1o7ZQE2C9i6pqe_o5KW4cvMKg1XAUypmdS931QBTZeGKo0Bz-bhBF_IFE6jLUssvOQw7NgvoFq-6ioxbtuGo2B2VOwtOKA72vFjdwoK2THQeidOj1rOs1C_jJ2L2SV2wSCbS-QLAoXXpZ6hWX19cw5QlSo2oqHMBoIj5KO8J87s-61VwNthALlwRLvOC5HU6bt-Zoav6_v_YDDTAPK_4bMS2pdH0tIcuowAwy_S_yclOg7Qh2nLRbeo866BEv5r6I-cIC9-BWnKoht3tjDg3OQRHwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی جالب از فوق ستاره‌های حال حاضر فوتبال اگه خانوم میبودند؛ نیمار خیلی بهش میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31447" target="_blank">📅 21:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31446">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDHYVyjd307r25q0HhiWpXZnsgq9N4tYUYsULDKLH7Hk0kvoALRwTufyxKBVdd0B9bkziPEljvV1hs2vNnKC1QkJhH8O6RJJo-nkRU-2w6sQ1qztNdu2-mW9Hk4h2uHzB-4zQC3qGM4sH7sfEC22dmzEGAvWpdyZ85H4246Zx8kGnRXfyObqMFD4ObdT_15PXTOENODcSq0dsAK93o-Fhp1CR8Mw8_wbkKugyV193LdZcNtXcDpkeKUc351AVrOxBu5Y8AdMgUcGbM02py-ErfJ4sRbPyNUYX5ggs-A538SDRMP9aKX30jPgSAXCIQwMOX73XxfyRnzoNeNfLOIZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باگذشت‌‌بیش‌از 15 دقیقه از مسابقه بازی تراکتور و الشمال؛ شبکه‌ورزش موفق به دزدیدن تصاویر شد و بازی تراکتور الان داره پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31446" target="_blank">📅 21:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31445">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYi_NCZ78pi7g4d7i3tFNJxzwNHEEmO8cyChLVqL0ub3kmLRoPxZKj9cVw1r2e6ax9w0OIQ5WcLp1GCfm36yOUp23st5hbvjGAz0VeFcHs-Z2JJMxXaP_0FurAqTuSpAazrSFbyd7Xuj2Hfk_Isn5TaqbUYWNbam3Gr3ed9k0_-gOGEz0lk9c_HVcKUUkq7OjqfMVnt5PARiobj1CAbxsuHNN7gslgzSOwkMS5y0jiJseYFwrPl4dXSS2ZqVJAkPL-37Skx0Oyn6MK-qXyYHY7-zrH748THvdr7TUxWS9m1dByWyWu6hkWLqlvnpoRXmFDguvvnpE3EUq_BqMCbz8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛آغاز هفته‌دوم لیگ الیت با نبرد حساس شاگردان بختیاری‌زاده مقابل الغرافه   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31445" target="_blank">📅 21:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31444">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvvEitLvXf8COdBkz2rSZcVxZ72IkJoLxoXP-75_geNUyMbss4gyRFct7FLdHbGxOQxuuF0Iya928Lti77ZXp1AkUPxSb3LUV92yHxpUSTNOYnqne3_mzrdH3Ntqu0vzK4V_Ifw3Dre5eXV6_1Bs5OaBdL3TKTFzOgg3TBIwqWAGwdYn7EhNA817qO8S0P2N68eJNFPTX522Ej6fsbcHhhKX7WyzU5XJr5Vr9jVZpjuVcRRm6ra9XKZDzkLq4AmgqMZUdsBgd8UaGV_C9Nez33TS_Tv4BbLq6wkUjY9o6XpEO2bnb40iulJDqjQHcRn8B8MGqxLd8PJdS2jDLAsN8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار باشگاه فنرباغچه و فن کریس رونالدو که در ورزشگاه بازی شب‌گذشته تیم ملی کشورش مقابل فرانسه درهفته‌اول لیگ ملت‌های اروپا حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31444" target="_blank">📅 20:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31443">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5aE4lV6OuGzsWl1ovkf0aCW9WI7QN6V2kgI7qL2rPtOJ9yoqWDM-L_oAVnuKWQucfF3xO9YLWWD0tOgPFS9lw_LFGH-Vlv2Wc7xyUb1S-hbekbMax5MmWRtRzgq5T2Fq69EqSOjVH6TQ1y2rKbo--l9SEnAhPzF0fvmUhJgOR5-XUbVxWiUrExFS82DcVULc21Sg4zRJOFXBSAQslxhL_fIRgrW4R4kRlhXPi2Jyn5HGtHnPgQ7zqGq27nH80KmKl-K4Mc2Saa3HxWnLtVLKmYAfH1Fi1CNxFoMaEiNuIIXs_YfNAMedqm7j_U5YB0-ae22T2qRyYKl5tNV1aWjbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌نخبگان‌آسیا؛ ترکیب استقلال برای دیدار مقابل الغرافه قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31443" target="_blank">📅 20:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31442">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vh15aBEZNbGPIfUAz6TaL5Drk_K2fNkN6kqhOC6uj9icixLCy-Ca0B5iw9rBEvnXQou7418S81IXVZlw3J4JOTXpXVKvNlRo9L-zVSHUKNaio1yuwIS3J-15a53mkSzvuObx41bVp6k_B0_B6_1ylKdVC1OBv24ZLlF2YRnSQlLRTPU776dkN0XzHzalouVgoscTqOfJf5P7uxOZQ5QkMG79DOmG06BL69dqBzMkxUW6lvE0JqoDYKzmouO5fVRnjvkSUUa2W0dnSNmJdndwY1HiRmDRUutdh2eq71c1GZDA9S5AMWnBTrKDgSWYIhpLZyjVKguY28Vsq6Lqu_t8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31442" target="_blank">📅 20:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31441">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=FKtVUZMNEnNk0T8h7diO-QWDUS3-v1NXxicCSmY3HOOBfuyc4-7HnjVuiLSb3FXY2u-t4hMEqVTI4IxGipGsQSwXWWcpsjEjSr1Q4Pd4Unlb1gH3Bn8GUVTqGVDHyK_YP5ZZQmPsnzoAhLjDoKJBIwrxu2qvgx7aUUMyTwogI799MIngV5AlHf0WO1hamDtbCPOG-ZXKQMkfJ2APA0jIWomSXLpb01CQ07Jq0iuL16qkFCfy0PmiOZ7O1PAwR83EMeb1CoXn8ONuxTwzVgS53Y5sIhn8k7ByWjcbcwzW3k9ETwtxSsicqsusqX85rFffPQNIWa3p-VA7b0-tlIb5ZahTjHdd1MTOlZnqs9Rg4xVaecqGbnKunUs8xMYWMHY3u5x4Icu6qk_fSAno7gYbfzci7txPgaGZ00MrI_8I2yDsql3pfQz-4eG5qvUQ0A8WVSthhdrF7_sUQiR-CxF7JivAuUvngXxkFYTbGeEno2QlvE1l1jsuQR0B0kA--m5l8FlYX1lNoLonEBOc64bfKenSNGLlA3TD4-RTx3N3b3pezL66JV-xOOZoSZgr0SidU0F29WsIwgWJDatnm9Q3toSs5pTNJuPhJ2iuXJ_8xEucrN7oNYcx_czMky9owd2QYThy2HXq5TNd6YL0lw8XEtdeb_qITGKChAh1NtLmf2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=FKtVUZMNEnNk0T8h7diO-QWDUS3-v1NXxicCSmY3HOOBfuyc4-7HnjVuiLSb3FXY2u-t4hMEqVTI4IxGipGsQSwXWWcpsjEjSr1Q4Pd4Unlb1gH3Bn8GUVTqGVDHyK_YP5ZZQmPsnzoAhLjDoKJBIwrxu2qvgx7aUUMyTwogI799MIngV5AlHf0WO1hamDtbCPOG-ZXKQMkfJ2APA0jIWomSXLpb01CQ07Jq0iuL16qkFCfy0PmiOZ7O1PAwR83EMeb1CoXn8ONuxTwzVgS53Y5sIhn8k7ByWjcbcwzW3k9ETwtxSsicqsusqX85rFffPQNIWa3p-VA7b0-tlIb5ZahTjHdd1MTOlZnqs9Rg4xVaecqGbnKunUs8xMYWMHY3u5x4Icu6qk_fSAno7gYbfzci7txPgaGZ00MrI_8I2yDsql3pfQz-4eG5qvUQ0A8WVSthhdrF7_sUQiR-CxF7JivAuUvngXxkFYTbGeEno2QlvE1l1jsuQR0B0kA--m5l8FlYX1lNoLonEBOc64bfKenSNGLlA3TD4-RTx3N3b3pezL66JV-xOOZoSZgr0SidU0F29WsIwgWJDatnm9Q3toSs5pTNJuPhJ2iuXJ_8xEucrN7oNYcx_czMky9owd2QYThy2HXq5TNd6YL0lw8XEtdeb_qITGKChAh1NtLmf2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ریا بوز، استعداد ۱۹ ساله انگلیسی، پس از حضور درآکادمی‌ های چلسی و برایتون و تجربه اسپورتینگ، حالا بازیکن وستهمه و بصورت قرضی برای ساندرلند بازی میکنه. به‌ایشون‌لقب آلیشا لمن جدید داده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31441" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31439">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKG_SgXTnLIvWCfTxRmUxtu_01hfJf848QkGgnvv0o7L3GKHPLP4ubwHizbAcjP8cTceYAJlK8bb8Qy9UKY-GNJ12j8r5UHMazHh7KZpXFrJcuToQ03bInp2SuGWFlEOr5NcmqjFaz8Gk2vZ2HmOQc9QctoSJvRgs1x5t1XfUZBLbqO8qVRWxFHd2mweaDR3GuKHro8TCc_ENs-C2wEugZXvU6RhWfzXggd_vYxaLtQc0YXpejGjSnSzfPTVAXNbpQNL5yW1KZGl-kMFYwjlimemhLs_r0So8IWk-waApNhNOxuPAgRFuKKIYMzuUCpxmvXmEnXsd2ojaDPCKBrFWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31439" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31438">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eomlSY8SnIrKgUFky3PVvVi8fL4zmhRGQe7V5dXA7Ps8saX7aaIhxt6ReTBqQr_NRA_MGYsRcvwbqSwoyKmc0f9TEtNbMTceMFmBu5gtCbOMp8UqnJqNeAYL49i4kkvK-Y66DnsC6UUa0bsCwbOHfzDKiOv19g-8MUY87-gtNq9Ihoik31k6xkLK5mUT6cI2n4rtiMbVw5d_4bNW8ioNH1WsarYC0HRz7XhSSgd8Rh-w1NEhT4njP6d_OcYjKbQqEiLzyhg2-SSb5m-4xg5Xx6wKD6hXGAB0jrEyg7jQbGRoJ82X43bq9HR7GXNc6aOsW7mnqRJzKCAThKz8oErjMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مقایسه‌عملکرد مهدی‌تارتار
🆚
وحید هاشمیان دوسرمربی فعلی و سابق‌پرسپولیس بعد از هفت بازی ابتدایی‌سرخپوشان درلیگ برتر: مهدی تارتار: 5 برد، 1 مساوی،1 شکست، 16 امتیاز؛ وحید هاشمیان: 1 برد، پنج مساوی، 1 باخت و کسب تنها 8 امتیاز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31438" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31437">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aR7wIeZnpZ9Y50F-NQYcv1vPoK8ug6DJjAVGfKmoE3xPg11oJm7KpaESXw6a29qEBrGDZRUYE-tIbM5J2Hcz-Slh9jY9iWjUrLn5nPPljoqTZBcX2o6qmZbvUQOMN8Dz18KAzH1MUWr__ylXXWnxsGAiSpyyn1DEv16bYAOp2lLO8VI9f40P5DEjDeXrFKWSukj1Rz0M0QMhLU-uf4W1T7jEB79u9H_o0Q7o1qo1VzyPYdK7RTWsR-_S6EO6V3Q6z1Vmuimmvevr5G25EJyieXAPZhUtSjoZMpoiAUNPN79U4voaamKB7QrLMBPechFjn38dmVmghUX9Bhq4y5N51g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فدراسیون فوتبال اسپانیا؛ وینیسسوس جونیور ستاره برزیلی تیم رئال مادرید مسابقه سوم آبان‌ماه با بارسا رو بدلیل محرومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31437" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31436">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEln1EMM2Gr2V4N7rg9hRSvKr-BzdEjc9-PiHkG08f-CAQrDcSnGzYri5GRZmldCd3Zn6QFMwPSgbidr6z-yUPZcsUEwDbjPF--a_jvXsnO5uESlpv-6KqWV6t3yhEYNFeDT0NVKaCL_ZJDFOClXF5erwyT44uiMenSOpr6jbXo-qHIZxEeoyoVlSjpsZRZeWe2OrLy7kAMZ1Z4s3yH1xbUHpfsHOcW4-ugvXS6d5gizN--iyD6Ww0CbHgJfO52WT5P6ln1iEqShPNZXnBjjhbDxtoJYx5DjDxUQst_vuGc2QuxDgrIti0uabXprfvUb4R-W76l6EqXsDjLm0zsdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه از هزینه‌ای که باشگاه بارسلونا برای جذب پدری کرد بابقیه‌باشگاه‌هاکه برای جذب بازیکن هم پستی پدری هزینه‌کرده. پدری درحال‌حاضر یکی از بهترین و آماده ترین هافبک فوتبال جهانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31436" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31434">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2Jof-v74qW3o6RQsHFqf_CJjDzMIREK5D4J_DxlNVajUY-oK5CGI0g5PT5zUK8fvi2-BzSBJuvUsqDW6tfzy7oNGq7yx-0sQfpXjONT5fd1L6OooWvGAcXABa746rerczxAlgaXHomqyoNyAp60tLTF7LLAra-V7Wsi0HJwi7llL3jkitB6Rks5OBRQEGM7hV5ya0XBrEAJWz97W5xRnX3dmxl5V3dBdf2f6qWYM79udsGj30WT2TgHbyEF41obRzv9QBKybG9By1w-_H36JtSesLwExyqjRFuMlBZD3YIsZ3jv-IsGbRPT_q0D9EGYVhz5isvXqR9wS9eC_VWEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31434" target="_blank">📅 18:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31433">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=dLN8N7zE25aEO4S2-p2K-GJYc6_P_VzL-M9YNEKcHHE1Pfe4VJDwvUTPoMMjzGErDWwcCAjALmFWJ7lezUaIO-gXiRw-Umoqx3VMyDZvYbi66na8zQjvo6TiFQ8JZ9n68qAP9fT3B7LNhX-EZ_-C83BBdmyygSRRi9LCSTJSM0EzANlZB2AnwCk0VeECf2HOct6gRpEuRTTFWE0HqovemCcmODfCAAzf3Q9b5MruCKh61sz2lXZr1Gb3noRXhrJ-fsdmY6REkV_9Yb8rpCqC3A1arVcb2Eu17HWlX1M-PE94udQCHP68LAXRmX9NC2TakydYC1Jnr5INULOxoxlrRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=dLN8N7zE25aEO4S2-p2K-GJYc6_P_VzL-M9YNEKcHHE1Pfe4VJDwvUTPoMMjzGErDWwcCAjALmFWJ7lezUaIO-gXiRw-Umoqx3VMyDZvYbi66na8zQjvo6TiFQ8JZ9n68qAP9fT3B7LNhX-EZ_-C83BBdmyygSRRi9LCSTJSM0EzANlZB2AnwCk0VeECf2HOct6gRpEuRTTFWE0HqovemCcmODfCAAzf3Q9b5MruCKh61sz2lXZr1Gb3noRXhrJ-fsdmY6REkV_9Yb8rpCqC3A1arVcb2Eu17HWlX1M-PE94udQCHP68LAXRmX9NC2TakydYC1Jnr5INULOxoxlrRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد!
جواد نکونام سرمربی تراکتور:
شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31433" target="_blank">📅 18:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31432">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hh1p7MnlDLsof6VmU3xk-9jzI7JQwal-xthJp2YFUVzN9ARHtFrTTuZvlvejMN3waSr31U-06YhxAPJAu-rLtRs0sj1qFHBYBl1NgGDImrUhpdur8xdWSStyQF74LbpNkDw0jNQ82-OKFwAPf-lMibedAVJQnRqm7TOi4jDWt52uKZ47ZQ6xLH3TVZJGrJE6nRrzhMeJ3HpTRja6w0tKBOiQeVQpxOCjI8ECiUKIo1RsH8Zy-kd6wJDqX8iS79x6ciLhC6tsdfRCTVYzmnhizE2ySgwKVKF2aFVFkzOBAOtUhhtvf_l4uknI_mmf57XhGPEqK5Z5d_1pQC4cFrZoHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31432" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31431">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7ELTRYsN7dVqAypbRN-0K5aCA01_G4fXBacN2WOU3oYloFi_2ZzITvpviFeojBhUJK9P8rk4r8InYCoWqlfi6lL2c0JMpezATVRgtBQF_4R3QbvUdDuBHDPqUUlS4OzbnHulTs6mgE09nkq9AuiDUdKy72nX64HQLdXDDRzA3A8se_yY5fXcwxUJzPxcQvX_-K0UlvnrrQddbqz3EsoCu_lQH_M2I57Y_wIj-MkOzTbKQsSzkaqIEsBqx3JIIIENmjjqFZes-inRu5vLVYQoNeiyj08pB_8hqSUym2qLlIXKoCsuHcr7YRuy4kAMriMaO34RV-3L27tsOarROnBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قد عجیب پسر رونالدو!
کریس جونیور درحالی‌که فقط ۱۶ سالشه، قدش به حدود ۱۹۰ سانتی‌ متر رسیده و حالا ازپدرش کریس‌رونالدو باقد حدود ۱۸۷ سانتی‌مترم بلندتره! جالب اینجاست که با توجه به‌سنش، هنوز صفحه رشد قدیش بسته نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31431" target="_blank">📅 18:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31430">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBIkfrtzoRaHQYaC7EWCWac2ZNTijYFnvhaQ_5HA57ezupyZJl8k0AThrt3TgG-8avtebiO0olWewfPSH2qDQSAnL_6EjQzQFFa00Nfsc3jwzRDNjhg5kb2qgTMT9H-JZ-cnmxe0v9Sur-DwUPowZ1bCh_G7yx0uLBs1hyPfW-2a5DzBCj1NP-A_f8SpNDjEOg6eo58EOPI955QgCJrSi1MwQ4PhYF5SSXzpZC6TkuPua4ylpwpHr8W-p2wgUXuV3d62VNNgU_xz2qvTH1-dTJh9KU-GYe9bCyyKjo3D6ov_nfYoN9fqzyMhTpkZLwbbXJIMkscAVjM4AgOsBsNDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31430" target="_blank">📅 17:42 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
