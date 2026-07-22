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
<img src="https://cdn4.telesco.pe/file/L_VAiYb43UDuISIPCzrI39F4AVys2QzoZm7apbs3tVBm7C1w3qk4KlDmbgWgIsJpJof5Aljf1UaxjvloHUg_ew5xB44OFqkVYohS65317mPuyu1phmVb_510ke6iCVLBfdtQmuTKPIexfW4uERORtp7lXUPi1M29njeiqt7YWt_DR4DhLPui4hhAFRpCUlihEImOCZrr8leDR4udRBdkSZGGMOBxwRNRR7I1eKr_3_WvrMyvzt5mVRQDxJmE3meG9_RkLC-Y6KlVi2f_CW15Jm3tlVsKnA720RntwIi9CYB5JH5CYh8w38rj98NwXredkKBmaL_TPC6IdeTbr6BZ-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 153K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 01:04:23</div>
<hr>

<div class="tg-post" id="msg-68829">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=MKgS6NHw9XNzkjRph3DsCZeUUJ4W77X9HWcgvt6Hkr6aCUDDoaU--3w9F6KGX5Ps4rfVjsDMdAXs9z3hdm7hbx4iyV-0QaZ_A8zxJcFVkFdoFgWEUzF8kUecIv68IIRTcoln9jLDiYQS6DzAQB_LgrxQ2kpBjmB7fp_aL7fl3UCfjihust1rOZkQk1HcyXF2V-ZK12UjjPAiHyB_zFwTNSVvgw3HdQ0NODex9Gfn1rskaHljVW3abjlCwFeSQysU9U_b9FZNG0eceS0WNI6ppdoEFZPkWYrkQZdA4rh1W-G9rj-lJv1ZjzmuNaE7cdevmCx0lRsM7T9qGjOTILDFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=MKgS6NHw9XNzkjRph3DsCZeUUJ4W77X9HWcgvt6Hkr6aCUDDoaU--3w9F6KGX5Ps4rfVjsDMdAXs9z3hdm7hbx4iyV-0QaZ_A8zxJcFVkFdoFgWEUzF8kUecIv68IIRTcoln9jLDiYQS6DzAQB_LgrxQ2kpBjmB7fp_aL7fl3UCfjihust1rOZkQk1HcyXF2V-ZK12UjjPAiHyB_zFwTNSVvgw3HdQ0NODex9Gfn1rskaHljVW3abjlCwFeSQysU9U_b9FZNG0eceS0WNI6ppdoEFZPkWYrkQZdA4rh1W-G9rj-lJv1ZjzmuNaE7cdevmCx0lRsM7T9qGjOTILDFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/news_hut/68829" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68828">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
صدای دو انفجار در بوشهر شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/news_hut/68828" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68827">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
فارس:
حملۀ موشکی دشمن آمریکایی به یک سولۀ انبار آسفالت در اطراف رامشیر استان خوزستان.
@News_Hut</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/news_hut/68827" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68826">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJRHLqeX_EfNnRxoNWMr0_qakiUjzsN_zj3HuxiO2jeUsJUG9rU0PQSdYHBAfEGB1J0a8jh1euW4VNOwWfjvG3wvDV_76EeSCek25dmXhsRvpO5fgzi5JjrpF0FPBruDllEJxWeOEQHvDClWo4uXRO2l7xOuHgVxLBQJu8xNHCO1W1_isIMycMlrXBu_t1w0kpaogFbvfijduy0MdpGnYzJikbfi9M_OL9fvo99tVkX1Hf4V-c6RUcsaQNUDK5kyS5QhsBo3fVMeAM_97lA_iMpMGNGDM-pTlGGpzbwHg5LFVjx7_3RDpiGdz4PQy17bGljgmd9yBBxOkJVQmAd3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یک جریان مداوم از تجهیزات هوایی آمریکایی به سمت خاورمیانه در حال انجام است، که احتمالاً شامل هواپیماهای تانکر سوخت‌رسان نیز می‌شود، در چارچوب آمادگی‌ها برای تشدید عملیات نظامی علیه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/news_hut/68826" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68825">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
پاسگاه دریایی زیارت در سیریک هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/news_hut/68825" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68824">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
دقایقی قبل صدای چندین انفجار در اهواز و ماهشهر نیز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/news_hut/68824" target="_blank">📅 00:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68823">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
صداوسیما:
چند دقیقه پیش، صدای انفجاری در منطقه بمانی، واقع در شهرستان سیریک، شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/68823" target="_blank">📅 00:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68822">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030860acf9.mp4?token=Dh2T3xkHl_ooUQug5siZ7Wq2EPNt6n61mIZWeegeNlE5lYnuvRnIucCmKtoXQksuHs3ylPH9drizPQr_Q9cI3V9AHuwwnjUsj4ucLfaWtQC0Jp1R_Po_lJvLgZhExTOAYudHxlvOKV3PXmeSZhFAwH8xZwlANSAJOwsH8TeHaJcC5LxJ9pzKlZM06AQKXNH6M8jUpGE_dnNcHDbptr-DMar-p5sEw1C_lyfakuiUU5dA9hJsqihLXsmmvbD9V_j5KDQmRxq0BQlQ4Rs5aPpo8QB3_qvRc_r-bejppu9g6urW3af8ww342-Y_R5IFkPRhDDZjn2UYzJo8XbTR7rnbcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030860acf9.mp4?token=Dh2T3xkHl_ooUQug5siZ7Wq2EPNt6n61mIZWeegeNlE5lYnuvRnIucCmKtoXQksuHs3ylPH9drizPQr_Q9cI3V9AHuwwnjUsj4ucLfaWtQC0Jp1R_Po_lJvLgZhExTOAYudHxlvOKV3PXmeSZhFAwH8xZwlANSAJOwsH8TeHaJcC5LxJ9pzKlZM06AQKXNH6M8jUpGE_dnNcHDbptr-DMar-p5sEw1C_lyfakuiUU5dA9hJsqihLXsmmvbD9V_j5KDQmRxq0BQlQ4Rs5aPpo8QB3_qvRc_r-bejppu9g6urW3af8ww342-Y_R5IFkPRhDDZjn2UYzJo8XbTR7rnbcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه روز پیش که پل کهورستان رو زدن ، سریع اومدن یه جاده آسفالت از رودخونه خشک شده اونجا کشیدن که رفت‌وآمد متوقف نشه.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/68822" target="_blank">📅 23:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68821">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=FhLvAg4ccKseLrE-w7z-SyyWsSEBzBis7eM7_t1AJodK2EB6m_87CV_V2eMw0vhR5DQ3uzCzKcpw0DUtTxfwoz4_Js5wWG1wDHAvDiiOe1kJ4AmWVuzcM6d11wOGjClnCsKob7a854Py3B-0RYKRA4WWmQ2eqxnGHki6EZlf7oojRWdMnUiQCcREwptFwdRUtPgc-b7BRAZyixBnXs3K_r10tuzqxiD9m4rp1BRFaInMQi-_NTQve0otVFgjnLM9VIJg8Bfm92GN86XONx1pXrb0WuYE5WdArGb1SrfKIKz5cJdmdrpkCeoxUg5QD5VC-r2dZ54KT_d1C_gEX1kOoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=FhLvAg4ccKseLrE-w7z-SyyWsSEBzBis7eM7_t1AJodK2EB6m_87CV_V2eMw0vhR5DQ3uzCzKcpw0DUtTxfwoz4_Js5wWG1wDHAvDiiOe1kJ4AmWVuzcM6d11wOGjClnCsKob7a854Py3B-0RYKRA4WWmQ2eqxnGHki6EZlf7oojRWdMnUiQCcREwptFwdRUtPgc-b7BRAZyixBnXs3K_r10tuzqxiD9m4rp1BRFaInMQi-_NTQve0otVFgjnLM9VIJg8Bfm92GN86XONx1pXrb0WuYE5WdArGb1SrfKIKz5cJdmdrpkCeoxUg5QD5VC-r2dZ54KT_d1C_gEX1kOoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به تنگه‌ها احتیاجی نداریم؛ اصلاً به هیچ‌کدومشون نیاز نداریم.
ما نیازی به تنگه هرمز نداریم، اما مجبوریم این کار رو انجام بدیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.
من اسمش رو جنگ نمی‌ذارم؛ یه درگیری محدود بین ما و جمهوری اسلامی ایران.
اون‌ها اون‌قدر تحت فشار و ضربه هستن که می‌خوان توافق کنن، ولی به نظر من هنوز آماده توافق نیستن.
الان هنوز آماده توافق نیستن.
ولی خیلی زود آماده می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68821" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68820">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇮🇷
ستاد مرکزی خاتم‌الأنبیا:
رئیس‌جمهور ایالات متحده، که رفتاری بی‌منطق و جنایتکارانه دارد و به قتل کودکان متهم است، بار دیگر تهدید کرده است که به زیرساخت‌های این کشور حمله خواهد کرد.
اگر این تهدیدات آمریکا عملی شوند، نیروهای مسلح جمهوری اسلامی ایران اجازه نخواهند داد حتی یک قطره نفت از کشورهای منطقه صادر شود، و زیرساخت‌های نفت، گاز، برق و اقتصادی منطقه هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68820" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68819">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=hE0LtSXga977A_TitBBupGCzKNiUm-Yyl0Z2aYBDreDzAf_dzt71Km4RAfns0F9M8_5F5yywkiRZ_nlYO1u_4Sz89wWNb8-pNJEMaZB-9ESKQJ8NiViKVNIIg1ieF0FNPdTcoBhZJeODFuE-oyG-S8tiKjZq0-TH8D01ZiRiVRpdn1Jhi2mfInKmnUb8O3JbahKtR2o1Noa0xwbosrnU-MzEO9b1F219QvpSvJdGKmz3xa4FQ7Zmdt2TpgwFJGmrKPr6Z7iWB3D9v8Tu9EiVPPaTgM2Ha_uQLYDuqmb-5cB28Qh2X400ULD_cC2AElZqQDH8OeQBy0BPq-nP_dOL4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=hE0LtSXga977A_TitBBupGCzKNiUm-Yyl0Z2aYBDreDzAf_dzt71Km4RAfns0F9M8_5F5yywkiRZ_nlYO1u_4Sz89wWNb8-pNJEMaZB-9ESKQJ8NiViKVNIIg1ieF0FNPdTcoBhZJeODFuE-oyG-S8tiKjZq0-TH8D01ZiRiVRpdn1Jhi2mfInKmnUb8O3JbahKtR2o1Noa0xwbosrnU-MzEO9b1F219QvpSvJdGKmz3xa4FQ7Zmdt2TpgwFJGmrKPr6Z7iWB3D9v8Tu9EiVPPaTgM2Ha_uQLYDuqmb-5cB28Qh2X400ULD_cC2AElZqQDH8OeQBy0BPq-nP_dOL4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو این اوضاع ویدیو های سمی هم وایرال میشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68819" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68818">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4En4EPSGK8G67LtxQRuTXETtxndrFLs0MIRQSi9zaq_qyF1-Hq0M6Tw0iGiTaHbvAUlzv0Oxx3qy1qIyXkSn6k5ivo7BkxcIaQXkJ_keiKJ-aTjI6VH5Rxnc5D6b94UQD1DTyKEAoS1rOfGe9kfAGFRcz38XuKAq6wo03WUq4TeeTQQxpZylvPuc4EQqq9MzfVUMWIA4cN5-fVKJgZ4yE2PTrXgPDoot3nWBhGHgjrrDVikkqYEqS7GQDEJZffhKqJMqqfOp_CDxYhrWbmHSB_Np-_DcWW7KWH39ZffS0p1g43dppe1OZm5YpmVUlTJjJSXt4gTsGAb3F9MXEzsBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مجید موسوی فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما حمله بشه
خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعیه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68818" target="_blank">📅 22:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68817">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=mbZprnl3NE43ceJNMgQJzNEz86w2XxMXNpWQ-ij6_wmQQxQIJtsweZ9OkI1Fe1HKblTSm6Y7YtsIxGH8HYq_Z4ckeh5bDgG85ECeAtvsHupK0pm_2ktDR-1wrMBbycOZvLn0Qwvj9HkvNWPt2Dp_8E75q4RLK_0LZwBN-N1-6OHajq3t3xr-gq8NX2Pigr90QTKJgoWDMajjYP6Db1zbpee0C0Nt-A92YZxlfMYqepPU1mTUoMFEc44P5v8TDY5cJxAOQfB3UGWqowAWZZhkYBZj68zc5KHlWk5pXjMSDF1SAIuri0BzhHGkP8MM6_r3L9Er6q92sZdo89DdHY43qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=mbZprnl3NE43ceJNMgQJzNEz86w2XxMXNpWQ-ij6_wmQQxQIJtsweZ9OkI1Fe1HKblTSm6Y7YtsIxGH8HYq_Z4ckeh5bDgG85ECeAtvsHupK0pm_2ktDR-1wrMBbycOZvLn0Qwvj9HkvNWPt2Dp_8E75q4RLK_0LZwBN-N1-6OHajq3t3xr-gq8NX2Pigr90QTKJgoWDMajjYP6Db1zbpee0C0Nt-A92YZxlfMYqepPU1mTUoMFEc44P5v8TDY5cJxAOQfB3UGWqowAWZZhkYBZj68zc5KHlWk5pXjMSDF1SAIuri0BzhHGkP8MM6_r3L9Er6q92sZdo89DdHY43qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهر چهارشنبه؛ لانچر مستقر در تپه‌های پشت اسکله طاهرویی (سیریک) که روز گذشته مسئولیت شلیک به سمت کشتی‌ها در تنگه هرمز را برعهده داشت، خود هدف اصابت موشک قرار گرفت و یک ستون دود از محل برخورد دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68817" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68816">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhh2P1g2To555iChL4dtdwa72oF9Vvq1NuhAJ5hu7ZjkcWc-mnLXR6szuRJhTHHk0HNgiroxvsrJZ7DslUW6GiqP6Acc7zAY8-NYmg8V1qM9vBPh5Vobfm_Ap4_SCK-bWnSymxvEPUytFwKLwnjp6u5h2nOBouGABJ8IHZNRP-VsRNHo1VEFQyYZdoMsL9Hz0rQ41DCfhEeWUN0SPgqUrRp5xJazhIKVMJPOg1RbiwkWvl7sKZvEGpq-cHwanAZeNjyN74dDkrwfynQLTkbAWsKlelj1mRy9o1uB5De-JaHTQJbfZVty4dpQDPcofoEOQYYow--bLXaAJzkwxWn-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت.
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است.
بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68816" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68815">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA01D8uzQ1YgbxtZ5cTj5gDULEM555B0oi4gxYYPtMzL4xVXDeyyxbl8Z5J8BvQecElmuFY-m9iNm8Kfv0r9MzHj4BnqEwsdpbW2WieS6N8xFI_tEbVmpy0wrTZuEguCMED2gtoeKPjPsIhZCrH8eY1PCmMIqQj4-0MGgFvV3EL06JnH_3YPvLbKUTMW94AYWRK1qmEG7cq5ZWhy1kjZt6azvBMjEwHalShPtMnfKLBZxgpkSdAW1SPcM9dnBbSNVMinRORsbP5c1igZv-hzotUfuH7iUrmI_04Xr4op6oJReZZCudMWnbOiWcvEUQcrFBVP6kjEc6ezw_rF5mNFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال:
رئیس‌جمهور ترامپ به‌تازگی اعلام کرد که پس از کشته شدن نیروهای آمریکایی، به «سنتکام» (فرماندهی مرکزی ایالات متحده) دستور داده است تا «درهای جهنم» را به روی ایران بگشاید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68815" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68814">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68814" target="_blank">📅 20:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68813">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7YwCvMmYmxmt_NDTvOkfT3KeiazKoeZs2xlolK45G6-c5-iE-LqUgxXcAlkpUDJibtI-qR8pUh0nPrBWsG3Tn2oJocveCm6cLt5DsufgAm-6tb4AjbVLj5Xd6wImob-8BL8TE0Gdi9VZvBzVbnAJF-k4tiKs0K-pCAgca4Z6Mvsg1pY1ZMYSUzBoSZ2uVM62YkKdSnD-7kPS6YWoJ8bWVDOph9FGaA30Wd2MN5KGl8OAuWrU7pJQXqjtOV-iI0AnbvX0KY8pYhkSV0mlsVHH0NFoMk3JiWmxYPmAhdnjUc5v8ZgumCinnVyZIvNZfZPfC565g9jFY_93Uj7ceO6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68813" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68812">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJJuU-s11crr5TX7rTUMtihwPFy5sB0d6UOaTn9cn4SAZDKgXTeP6byiWSTHBk-sW6Ex7iakTBh_g1he4-lKr9y7bMkrAP5op96T6Czk_yTLVPOscuZIhZ_N-L3h6XLoqZ048wTQM6Cg6u3DWNR-QmwDCgSpkcwhDIUwj1jUcY3BM1W9HZqHgHRSFWmbpYA7UfYp-oH6eeMtKnOxN4X_V_kAYCP0LKx7PfFbYUA2ScND1d3EynIa0dlQcR2PJUwpTWEvHymL5qlm3X4mEJnWZvxa2gPjXIOzStbDbBx3JEb9AVQ3luiC-ma3gfa0X4AejJ-YnLeOlpLCEq8ZW4yD5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یکی از حملاتی که شب گذشته توسط سنتکام در جریان یازدهمین شب متوالی عملیات علیه ایران اعلام شد، بخش نظامی فرودگاه بوشهر را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68812" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68811">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGNczzS8NpQb1ezGozI1BCdJlbvvkAVYdIhr_v7jBNU-3NZJm2nIpeLDPUq4OjlXkGCcvQ97v0cs6SvkVFyOhs-HFoMSWCjrbprk4wLaqZvNTzUIFauqx1uHtFLFscicOKl3hmftYoi_fj2H4iMHexmlPBg0k-6k89o-wB2bm9iP7p6axl3M7xGZJ56woEYaNk13MzjbSPHRXSl5KcAyI4sHnyZz7UobSmMr1sMB0O0LYNAvalCL_Acm6yFQR4lgHAyGbp_XMW0YBfjALOmQdLJDYfiOiJwL-_i18j7lfB4gVxZU8ffPWDw5yklebD6ybrh-ekH7qZ6knFVi9pFM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
قیمت نفت خام برنت به 93.14 دلار به ازای هر بشکه افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68811" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68810">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuhNN_BoqmZBqOVQ1BxPPGVXlIBEATFcJtDxNJNYJvV2zjpYFv_EWxU3W7S3UI34BYJnEUD8TlpVDmbgGIesmSiKqDMiONBQCUbi3HHMqUL4SLRN_SH_wz3dKbQ90vPpFwLaskQemnlFmrT5L4sesT5T7ldrWmRMdBuZSew8comSY8mfLEyQRFV0e-Fsg0_DXrZo0FXs701apynJtly0DWzLgflo0MG5rrqpgER4GAs4tiUmSVJlrZ7qcaIlzz3PF2qN0NW3kjk4OSaDZnW9b4zP9aRpAOxfJ9DJWU3Vuf08wSqTiNBw9hWRyYiNN0IZOcaEp3MxB7BQfe20z0Ui4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68810" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68809">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=fW0FmXWiycKFTyVJCE_LA8IgXwECJ_BuHNGLtDO0uMFz1EWdqOm-7R5w4sa8TQe2tpYHnbEcqGe6HE6T2JzDCzPDMjmihVNXDpifsBKp0fnIRDihkRN8zn9V67VcpnhZINpNQ91EYrH8vx9wsZ_kjtGQYTLIjSNdZlkDA01Ml6MOubwq_36-4DRUQSyvaBydmTnhDvhK6dgPPKTQ0cEyDNc2rtvAbqpDCWTuVcEVLWbxOpqgby2obTeKZ4r5kCtHNxxXe4ND_7I03v5lPdg0gj9kF1EqW4PTPVfJeI2Z9GQ26jVth1D50Q7eB4uEJT0cJ76es7N1eJUWYhGoC3gTaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=fW0FmXWiycKFTyVJCE_LA8IgXwECJ_BuHNGLtDO0uMFz1EWdqOm-7R5w4sa8TQe2tpYHnbEcqGe6HE6T2JzDCzPDMjmihVNXDpifsBKp0fnIRDihkRN8zn9V67VcpnhZINpNQ91EYrH8vx9wsZ_kjtGQYTLIjSNdZlkDA01Ml6MOubwq_36-4DRUQSyvaBydmTnhDvhK6dgPPKTQ0cEyDNc2rtvAbqpDCWTuVcEVLWbxOpqgby2obTeKZ4r5kCtHNxxXe4ND_7I03v5lPdg0gj9kF1EqW4PTPVfJeI2Z9GQ26jVth1D50Q7eB4uEJT0cJ76es7N1eJUWYhGoC3gTaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس انقد کد کد کرد که
کص
از دهنش پرید بیرون
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68809" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68808">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=qNDcztIAI0CSCQViRZCVu_wpWTQYPq2ij78Pw5IISCs9eU7rhPxgjQ8zD46rZeYZfeFq8nTx9ebTnXXeMOX7aqUtpemtQ-NHgOvy-rPfO4g3SnTJmZc2QCpGRhHt_Q3wzNUpYfh1oJvi_gwPsRT7lDVj8sjMBtqOMxHtKKBYbNi3WuctYPp3Z1uzAd4AU5wzppfvyXRImDaZPDvyzTZ_KGpsAtdsXpB_BV8X122Ausz1QCSdTS4M66YLoM5ho7dndoOIesvFW6TJCEhfsGSsToJcTIBCDYo0wt-XH8GSWPlt-uDia0Jt5xoo_bU4tGXMxo72I87GNEKqLwi6ZM5Jbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=qNDcztIAI0CSCQViRZCVu_wpWTQYPq2ij78Pw5IISCs9eU7rhPxgjQ8zD46rZeYZfeFq8nTx9ebTnXXeMOX7aqUtpemtQ-NHgOvy-rPfO4g3SnTJmZc2QCpGRhHt_Q3wzNUpYfh1oJvi_gwPsRT7lDVj8sjMBtqOMxHtKKBYbNi3WuctYPp3Z1uzAd4AU5wzppfvyXRImDaZPDvyzTZ_KGpsAtdsXpB_BV8X122Ausz1QCSdTS4M66YLoM5ho7dndoOIesvFW6TJCEhfsGSsToJcTIBCDYo0wt-XH8GSWPlt-uDia0Jt5xoo_bU4tGXMxo72I87GNEKqLwi6ZM5Jbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
عراقچی: ما به هیچ عنوان غافلگیر نشدیم!
واسه همه سناریوها برنامه داشتیم و کد بندی شده بودن.
سناریو آخر این بود که رهبری (علی خامنه‌ای) رو بزنن که کدش 110 بود.
تو جلسات کسی دلش نمیومد درباره این کد صحبت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68808" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68807">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
یک منبع نظامی به تسنیم:
هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68807" target="_blank">📅 18:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68806">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:  بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.  @News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68806" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68805">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=IdlMMBKdVgbyOG8BbHlQibnJ7BnsdJIHaVJYhNsBQLbDLNf1Cq3ED70U9r_u-TQhaZLv09WWCZRtWsDqqOiZukbqkGSLPwbY6gsc9-_iYQ9PP3pf3HtWTXT6V6nHgQnGMKW4SmVfFVx_hv2K6IJ98vsLL9OYnq0PuZsBxtgpgKnAvlXUi67r35BiY0NxlvKgGzUIeLa2CH8Bl5QOZ_qxjxoxiNEgpdH27mtSVPWM3nnNdo4mq2ZhFdQrCH186d0Fhnqq6fOrwUrk3kIGpTlnWCaiuMSIpoHweGnFKnihEksGyaKSOcRv2w91fI2of3m0b146KQYju_euPuOW8Ct1lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=IdlMMBKdVgbyOG8BbHlQibnJ7BnsdJIHaVJYhNsBQLbDLNf1Cq3ED70U9r_u-TQhaZLv09WWCZRtWsDqqOiZukbqkGSLPwbY6gsc9-_iYQ9PP3pf3HtWTXT6V6nHgQnGMKW4SmVfFVx_hv2K6IJ98vsLL9OYnq0PuZsBxtgpgKnAvlXUi67r35BiY0NxlvKgGzUIeLa2CH8Bl5QOZ_qxjxoxiNEgpdH27mtSVPWM3nnNdo4mq2ZhFdQrCH186d0Fhnqq6fOrwUrk3kIGpTlnWCaiuMSIpoHweGnFKnihEksGyaKSOcRv2w91fI2of3m0b146KQYju_euPuOW8Ct1lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
دونالد ترامپ درباره ایران:
«آن‌ها بهای سنگینی خواهند پرداخت. آن‌ها در حال نابود شدن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68805" target="_blank">📅 17:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68804">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRKDgQG7yrNvq8T61GwBwB1PXd8qJOO3WF0LFMvDLDIp9rfEHt2JL16p_h-nagSWYbyVNnkhDLUt2oSRfQRKFI-8hG3UaUQCmnR4X1A0S3BVzoP9MsYxrZhtjwXFLk8WP8QfHob-sbRxAafKtjRmHBg4VPMrSxp5_l5Zy3MUDZsdt_-07NbJhEimXZ5VTnQoD_jMEI9DkTD3_9owLDf5wxg0cgmS0-28vCxzZ9PtKy9CjjWE8-isBOV5vtLJFzrOop0EsydEkxdnWfzuoPvhBF_nk7MyVGC6uzB8A9YSYdAQ3rJroIra0gsNHd6kUUk44uVp9pu5_LNoat0ZIlAQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68804" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68803">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSyYem9zgZQJE0NwiXY__CFPfgyn17MvcolECKZJQrwXxl-bV6BEBARPhMJUJ-_Ie_lR11U9B0nn4UdqrdnlV3kUwJDGUwe7NDIewDEgX7lEqwWO5FIaqz9YeHiSfS2wHBB-AvIpsH0D1I9mlTdwf_yYNxaEWTjjYiCTlvghdmZfVlFL4OHUaYPH3rxR0la6RmGf5xni2DN_em0PNkgVD0zCVa7fupkN53n3MAiquTrGvJmqZYffC08wfMsgBjouCD_1i-enE3ODY-xyvjKCt8qtoMSTBANHAlFo2B_lsEbla_Z45LSISK7BsQorQIXecdBSnSqT7ADqAauynpoTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه
حتی اگه نزدیک تهران یا داخل خود تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68803" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68802">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=Oi2MmDkd8UUVSHzmMZWvq8eeWqRM_k9NODGkva6eZHRjUwKeB2KiDwMwGNcyE6WeJStHc-JEMQpsKtPC_iH58BKE6HL8GPqPvdwsgpaIR2eROktGURFzlLe8QA2ICypscT2kdFmZSSNvF8Mqw0IAzFN7bhCAKOdKjrmuHV8TYqmAilQGLA7R1_9k_jYle2ZqjWuCQSmem2O93fGnVWLQsEVYVhY96thkgkZcEhukbJ1qu2JnL87Zz-KVHgkx1_l-oQSyZzK6zvSXbAI2FRg3SJ7WaxtZibst2xPcIOJIQ97cdd3WsgZY78xFaUcjO55-dJQmraqvNBxi-sn3Lwwnyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=Oi2MmDkd8UUVSHzmMZWvq8eeWqRM_k9NODGkva6eZHRjUwKeB2KiDwMwGNcyE6WeJStHc-JEMQpsKtPC_iH58BKE6HL8GPqPvdwsgpaIR2eROktGURFzlLe8QA2ICypscT2kdFmZSSNvF8Mqw0IAzFN7bhCAKOdKjrmuHV8TYqmAilQGLA7R1_9k_jYle2ZqjWuCQSmem2O93fGnVWLQsEVYVhY96thkgkZcEhukbJ1qu2JnL87Zz-KVHgkx1_l-oQSyZzK6zvSXbAI2FRg3SJ7WaxtZibst2xPcIOJIQ97cdd3WsgZY78xFaUcjO55-dJQmraqvNBxi-sn3Lwwnyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مقایسه جمعیت ۷۲ هزار نفری در کنسرت فردی مرکوری در ومبلی لندن (تیر 1364)
و جمعیت مراسم نماز و تشییع علی خامنه‌ای در مصلی تهران (تیر 1405)
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68802" target="_blank">📅 16:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68801">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⏸
ویدیو وایرال شده از گریه های یک دختره بخاطر مردن سگش
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68801" target="_blank">📅 16:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68800">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏
🇮🇷
سپاه پاسداران:
«اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68800" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68799">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5c_bm15xORD_M6oiNwm1rbLaFfbLy8a4uZeKIzPctdud269mpt9oznNwfXAdflpsGFTc5rFZf5htsnFPFUfRqeR3TpCFYplzUG_51ofJN3jlXvTSqPcuSVykQfyXrQVDQsG5apk5Ectawk9ZXRqJDM0dEVq_EhRvuV8JKvja7bkYjX96kutjkKEdr9o1OCgEIyD8CfyVpuQm-C5br8eeeGdMIypLPiAxjPfRgYY9BZTM-hB1d5UL0d9ssaXSlple3bCbMHPDfOjMqxnURDHec1lB5R8hBKalUSmWhlbQM_UAi37_xkzjpCm2xxfIhVHagje-03slwxgm2X6CuEgUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آژیر خطر در عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68799" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68798">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران به بحرین و عربستان سعودی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68798" target="_blank">📅 15:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68797">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=vSl37WMm-aknJLgVgazqxveOTg6GPWiFEBh6LIHghV-0S24zL8NhaxDE69ZZeWw3OaHpeUQHoJzVVDjkTVYsVwMksFU0drVOVIlolrAwEByBXQBfzUM0pMAS9TntgDHyGyA9SuJW4vLWClup91qkLowwUeNvMT6QSAuQz4q2WqlDTuBjsZWNxLjpqfN6jsjhcfVqtNTrF8blL6_jvuzJ2DZla0jFhsAxOUMqBIHLV83i09Wu_YuhaZRH1bFlNEOv5g4Wf6W3wPzIGxU_v_RMsFv7rhSflGvdn3otDS1vC2z4dxMHfFbAY6qy0pone3dFH0h4sSV7zWW4n2SGgtMhTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=vSl37WMm-aknJLgVgazqxveOTg6GPWiFEBh6LIHghV-0S24zL8NhaxDE69ZZeWw3OaHpeUQHoJzVVDjkTVYsVwMksFU0drVOVIlolrAwEByBXQBfzUM0pMAS9TntgDHyGyA9SuJW4vLWClup91qkLowwUeNvMT6QSAuQz4q2WqlDTuBjsZWNxLjpqfN6jsjhcfVqtNTrF8blL6_jvuzJ2DZla0jFhsAxOUMqBIHLV83i09Wu_YuhaZRH1bFlNEOv5g4Wf6W3wPzIGxU_v_RMsFv7rhSflGvdn3otDS1vC2z4dxMHfFbAY6qy0pone3dFH0h4sSV7zWW4n2SGgtMhTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی:
هم‌وطنای عزیزم، مردم بزرگ و شجاع ایران،
با توجه به اینکه تنش‌ها داره بیشتر می‌شه و احتمال داره حمله‌ها، مخصوصاً تو جنوب کشور، گسترده‌تر بشه، می‌خوام چند دقیقه باهاتون حرف بزنم؛ به‌خصوص با مردم عزیز سیستان‌ و بلوچستان، هرمزگان، بوشهر، خوزستان و همه کسایی که کنار خلیج فارس و دریای مکران زندگی می‌کنن.
🇮🇷
جنگ و بحرانی که الان کشورمون گرفتارش شده، از نگاه من یه مقصر بیشتر نداره؛ جمهوری اسلامی.
ولی جنگ واقعی، یعنی جنگ جمهوری اسلامی علیه مردم ایران، از 47 سال پیش شروع شده و هنوز هم ادامه داره.
همه مردم ایران یه جورایی از این حکومت آسیب دیدن. نذاریم کسی طوری حرف بزنه که انگار جنوب ایران تازه وارد جنگ شده.
جنوب ایران از همون روزی وارد جنگ شد که بچه‌های بلوچ به خاطر نبود آب آشامیدنی و امکانات اولیه، قربانی گاندوها شدن؛ از همون روزی که جوون‌های سیستان و بلوچستان، سرزمین رستم، مجبور شدن برای یه لقمه نون سوخت‌بری کنن؛ از همون روزی که هرمزگان و بندرعباس، با اینکه بزرگ‌ترین بندر ایرانن، تو فقر و محرومیت رها شدن؛ از همون روزی که بوشهر با اون همه منابع گاز، و خوزستان که قلب صنعت نفت ایرانه، خودشون از ثروتی که تولید می‌کنن سهمی نبردن.
👑
اما ایران آزاد یه کشور کاملاً متفاوت خواهد بود.
با روی کار اومدن یه دولت ملی، کاربلد و توسعه‌محور، سیستان و بلوچستان می‌تونه با تکیه به موقعیت راهبردیش، جوون‌های توانمندش و دسترسی به آب‌های آزاد، به یکی از مهم‌ترین موتورهای رشد و پیشرفت ایران تبدیل بشه.
چابهار هم می‌تونه دوباره به قلب تجارت ایران و دروازه اتصال به اقیانوس هند، آسیای مرکزی و بازارهای جهانی تبدیل بشه؛ با احیای همون برنامه‌ای که قبل از انقلاب 57 قرار بود اجرا بشه.
هرمزگان، بوشهر، خوزستان و جزایر خلیج فارس هم با توسعه تجارت، گردشگری، صنعت و جذب سرمایه‌گذاری، می‌تونن به ثروتمندترین و پیشرفته‌ترین مناطق ایران تبدیل بشن.
✊
هم‌وطنای عزیز،
🇮🇷
این حکومت نه برای مردم پناهگاه درست کرده و نه حتی توان دفاع درست از آسمون کشور رو داره. در حالی که خودشون تو پناهگاه‌های زیرزمینی قایم شدن، از مدرسه‌ها، بیمارستان‌ها و مراکز غیرنظامی استفاده نظامی می‌کنن و مردم ایران، حتی سربازای وظیفه، رو به سپر انسانی تبدیل کردن.
توی جنگی که جمهوری اسلامی به کشور تحمیل کرده، اولین و مهم‌ترین وظیفه شما اینه که مراقب جون، امنیت و سلامت خودتون و خانواده‌هاتون باشید. چون شما سرمایه واقعی ایران و نیروهای اصلی برای پس گرفتن کشور هستید.
دفتر ارتباطات و رسانه من هم به‌زودی توصیه‌ها و راهنمایی‌های لازم رو منتشر می‌کنه تا مردم بتونن امنیت خودشون رو بیشتر حفظ کنن.
آماده بودن و ادامه دادن این مسیر، یه مسئولیت همیشگیه. هرچقدر مردم قوی‌تر باشن و جمهوری اسلامی ضعیف‌تر، رسیدن به پیروزی نهایی سریع‌تر و با هزینه کمتری انجام می‌شه.
👑
پاینده ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68797" target="_blank">📅 14:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68796">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=VL78-5s_p4krZVXVnek63gjMjsi7p109LrMBYv9IPvRzTM5-NCE-dT5o_38r1uhWNuXXtu_9dwZ-O32_JvspdDvbzGSpQFDwPvCYmsgUQMTQqVNjFtkrWjbhW3p3l6f2tokAiRmGw_oDKRlbO1RvGY4_npYnJE4ON9j1hF-WR70ojkYAzpzK-i4R2SvpTNjmhDtIG9hQiXoQSrQ_mMg2CGQAoftVZsGuHQWMBTmstF1vmD0FuYVjcgnOJCGLocrUFogzUo8OZLiZkEGHpQJmEbGhMgjNBpkDymzU1Z7SuzQPTt_UyjjetnbtiSYHeDczsKeIos5YBkEjWONPalffYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=VL78-5s_p4krZVXVnek63gjMjsi7p109LrMBYv9IPvRzTM5-NCE-dT5o_38r1uhWNuXXtu_9dwZ-O32_JvspdDvbzGSpQFDwPvCYmsgUQMTQqVNjFtkrWjbhW3p3l6f2tokAiRmGw_oDKRlbO1RvGY4_npYnJE4ON9j1hF-WR70ojkYAzpzK-i4R2SvpTNjmhDtIG9hQiXoQSrQ_mMg2CGQAoftVZsGuHQWMBTmstF1vmD0FuYVjcgnOJCGLocrUFogzUo8OZLiZkEGHpQJmEbGhMgjNBpkDymzU1Z7SuzQPTt_UyjjetnbtiSYHeDczsKeIos5YBkEjWONPalffYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تفاهم‌نامه هیچ حقی برای حمله ایران به کشتی‌های تجاری قائل نشده است
.
🎙
خبرنگار:
آیا این تفاهم‌نامه (MoU) ذاتاً دچار اشکال نیست؟ چون در بند ۵، به نوعی به ایران نقش و اختیار در تنگه هرمز را به رسمیت می‌شناسد.
🇺🇸
مارکو روبیو:
فکر نمی‌کنم متن تفاهم‌نامه چنین چیزی را بیان کند. این تفاهم‌نامه به ایران حق نمی‌دهد که پهپاد و موشک به سمت کشتی‌های تجاری شلیک کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68796" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68795">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=mfgYbvWZKxuLt-zUdBevOD9ypNmKe9gfVw1-xJxaj2ni20Q18bFhKBPsJeiQh3OueWL9vH9ZCGW371zSlbWjYP0Xrz7NSZ_FD3m7Nnyja2B9Zz96w_aSXINVnfidbqn6CuOgc3C1YW2oT73ZcP86Opuark2-X48QUyG9KRWUVwPdo0il-R4FQuYsykYK6BMa6rKR_CTfrFZbnekXt9wW9QPtwq3_9jXxiGCdgXrhvG9UV1v-DBXDWSdKSET5ypj0yD6lb0xxTToWCK9fbev5EUeDWJe0Rx_gRMtOPTjVJiG0p0kg19E5gxyL2aCdcnalQpxpEwWDRzO-WwkYv5mMrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=mfgYbvWZKxuLt-zUdBevOD9ypNmKe9gfVw1-xJxaj2ni20Q18bFhKBPsJeiQh3OueWL9vH9ZCGW371zSlbWjYP0Xrz7NSZ_FD3m7Nnyja2B9Zz96w_aSXINVnfidbqn6CuOgc3C1YW2oT73ZcP86Opuark2-X48QUyG9KRWUVwPdo0il-R4FQuYsykYK6BMa6rKR_CTfrFZbnekXt9wW9QPtwq3_9jXxiGCdgXrhvG9UV1v-DBXDWSdKSET5ypj0yD6lb0xxTToWCK9fbev5EUeDWJe0Rx_gRMtOPTjVJiG0p0kg19E5gxyL2aCdcnalQpxpEwWDRzO-WwkYv5mMrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مراد ویسی:
دیدم مردم به من گفتن عراقچی رو فالو کردی رفتم توییتر نگاه کنم ، دیدم نه تو توییتر ندارمش و رفتم تو اینستا دیدم اره عراقچی رو فالو دارم که احتمالا دستم خورده بود و انفالو کردم.
مرسی که بهم تذکر دادید.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68795" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68794">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
فارس:
دقایقی قبل صدای سه انفجار حوالی سیریک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68794" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68789">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=frktzFlOvTo1F9Z203kAPQc-4zwwwvgeTFwi4Nn5HRq7RJFWNybZJ_GFNK4hksjWfF0eU-t76h6OwW3ReNsWHuW-abzVrr7rTsSbO_cRWl_hers7h7ckPFGNzOZosDibqy3OM-a6OyFPPJisZsIJCfJVnkLDf80VF-cXqEn9gTTEw7g58GKpo8_q8tPodlDsXQS3l4MinM6sJEnKmXtiKZa7tLj6GVJR1aKWgFmCvDv1Wx3jbfcgyuQGDp4arMqcIybYSzsy2_jHl2rxwtK0rGOQU22h1a-cRbK5wgnap3H6JyQtLSKEXyoce_cnJzWQIUiizC6xk7sUzHG_b7DZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=frktzFlOvTo1F9Z203kAPQc-4zwwwvgeTFwi4Nn5HRq7RJFWNybZJ_GFNK4hksjWfF0eU-t76h6OwW3ReNsWHuW-abzVrr7rTsSbO_cRWl_hers7h7ckPFGNzOZosDibqy3OM-a6OyFPPJisZsIJCfJVnkLDf80VF-cXqEn9gTTEw7g58GKpo8_q8tPodlDsXQS3l4MinM6sJEnKmXtiKZa7tLj6GVJR1aKWgFmCvDv1Wx3jbfcgyuQGDp4arMqcIybYSzsy2_jHl2rxwtK0rGOQU22h1a-cRbK5wgnap3H6JyQtLSKEXyoce_cnJzWQIUiizC6xk7sUzHG_b7DZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🚀
حملات شدید پهبادی اوکراین به روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68789" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68788">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=uEej_cJhgDJauIWbss5a-x49YxZR_5B4ve5up24MKIhzDWHdcibVA37ohk9nHky5LJWFiRuZDJdAsgmkG3iMggxqUbXAf_rIIR-wT4avwpDIDRSEn17792iknpWfEqxhAXN02je0DsavK2RC74pDJl_3-3K16Vk-bvRzzbL_i5Rrn17uymyib3ZFwEzJFQWWRnYxOq6FMkuTHTWK8HQPCFxej2e2suBhJU3mcLLsf6BJh_lyU0veV6UNC6TZD12pWbq8lG0o1Ik0ujuHywoOhmW33i6D0cPPx-KvBzVZmMS0nX_O1Vqs30pOA-A9hA2NkakF8qn9e6DL-hfvN_wdaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=uEej_cJhgDJauIWbss5a-x49YxZR_5B4ve5up24MKIhzDWHdcibVA37ohk9nHky5LJWFiRuZDJdAsgmkG3iMggxqUbXAf_rIIR-wT4avwpDIDRSEn17792iknpWfEqxhAXN02je0DsavK2RC74pDJl_3-3K16Vk-bvRzzbL_i5Rrn17uymyib3ZFwEzJFQWWRnYxOq6FMkuTHTWK8HQPCFxej2e2suBhJU3mcLLsf6BJh_lyU0veV6UNC6TZD12pWbq8lG0o1Ik0ujuHywoOhmW33i6D0cPPx-KvBzVZmMS0nX_O1Vqs30pOA-A9hA2NkakF8qn9e6DL-hfvN_wdaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی وزارت کشور :
عباس چرت میگه مشهد سقوط کرده بود، تو دی ماه من خودم مشهد بودم خبری نبود اون شب.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68788" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68787">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68787" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68786">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRCfsObK1c1pcnN18bNa_Q_Ol16UizDitDvNEcljbdVT2zHqW9MQhIo7RbH8sbeAVW4qEM4aR9c_WJORzf-rVRBTd9qamxX07QjImG84d6YZKAZuaXQvu_TpUIWOLTzE6JpizC_i94A-WJ3nQA7MllmDs6m93rw2OQENLDo5IAX_CcpWZoiJ8hWkJNM2ZVcZcFn78cqYRxPxb6TYsl2n6xTfTQrjBs8-6x46F0co2gTZeGZxfbaDkVN1yd3CvMRBYtV0Hp7cqOp-8eOS4B50hJTLjq2PTb6y8PtqXI20TfHgGSlnNxC2E--OwIOcWPxdEdqGm8X-yTwJOfbaNPl-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68786" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68785">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=iD86L0PcjidQyKaY8rEpM7077zkfD0AzPjoA4D3rab867feGrp27DPeestMtfmHg5OTkVAParq5BfmNw-W5SeAQ_3hhwOd4ndDe0iGc0yw9jlgDsXaMO37z1IjahlAxJvdzi6e1nlt__x4l4g8XnGSJ9FzXokXUP3ccgi-fYV6opzeI0jlEzmlyWG-Y6paR4XjZbhC462BVfBhI6iDjNIb4DMrbH4qZ0faj9S1EVIZRU3iWKzmVWn0wCr38sjP2A72AnhPpYpvGH8aeWzmTGY8l3Y5OFmyap46-QUkDJC_fvDj22-5FCiGYx-G-yHc3rGlGmQFEIlfNOD6_gGf1Iyg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=iD86L0PcjidQyKaY8rEpM7077zkfD0AzPjoA4D3rab867feGrp27DPeestMtfmHg5OTkVAParq5BfmNw-W5SeAQ_3hhwOd4ndDe0iGc0yw9jlgDsXaMO37z1IjahlAxJvdzi6e1nlt__x4l4g8XnGSJ9FzXokXUP3ccgi-fYV6opzeI0jlEzmlyWG-Y6paR4XjZbhC462BVfBhI6iDjNIb4DMrbH4qZ0faj9S1EVIZRU3iWKzmVWn0wCr38sjP2A72AnhPpYpvGH8aeWzmTGY8l3Y5OFmyap46-QUkDJC_fvDj22-5FCiGYx-G-yHc3rGlGmQFEIlfNOD6_gGf1Iyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این ویدیو از اینکه نشونه آدم پولدار چیه، اخیرا خیلی وایرال شده!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68785" target="_blank">📅 12:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68784">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdvwqNiUl47iWURiyM4rPK-Uxwy98XIs_LyI-SUAg9eS6avjiNcUDRkbV1uuHbTLNHU4VG08fDdkQdo21zRbzrMApH2ovKKgZ0u71LnpWkN3fovl68UcnTRXtDITEOhACb6IHWRZsyKoGRZZpwWUvcAI8MraIZITHiElbH1EBgTSf3RbgK9vUXx5x-w5X2MK8peDQDp3zcM8jycuVTZTPC_GCniXOzIouKXXruRi7RmWIYZBm4SoxwiWiPOhchRCe4LKQt_O6ch74r6TMhSV9HKkKd6gN-w-NWgLFrbpE8LeTGkgKqCjI1wAyYPLpL4XU56VwZz2vErK7KYfJzQY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
شلیک موشک از کرمانشاه به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68784" target="_blank">📅 11:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68783">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=NpYdoMn--Lhzv2v_udaqvGhT1PBdSyfWxrVT6THFCu5iUX6QKCJc6op6r-P0bOJApGLi7H1NnEvLUwLcFW_BVUqUBQ5EQBEbap3FBK5ZBlYPeNx2vcf0HUik12nv5KyI0-uj4t2TO-yYdN9HnGBYJsuFtaTc4Ea1-_RL-LJDWiB6vRg9F3LXgdgca-2iM9Eke0ll_N0RiD_RZZ5aIfsIvxR2ZvDMdwqicHrXq7FM4ooP_H1-NRpMY_sOjRXEPn3jUy7Y--okR_XJA72u2h_FG_eNNQllBOUwZTMZYK0UmFH3NZq63HjnL_Y-DQawq6b7zscyv8-IOMRB92eJbxexjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=NpYdoMn--Lhzv2v_udaqvGhT1PBdSyfWxrVT6THFCu5iUX6QKCJc6op6r-P0bOJApGLi7H1NnEvLUwLcFW_BVUqUBQ5EQBEbap3FBK5ZBlYPeNx2vcf0HUik12nv5KyI0-uj4t2TO-yYdN9HnGBYJsuFtaTc4Ea1-_RL-LJDWiB6vRg9F3LXgdgca-2iM9Eke0ll_N0RiD_RZZ5aIfsIvxR2ZvDMdwqicHrXq7FM4ooP_H1-NRpMY_sOjRXEPn3jUy7Y--okR_XJA72u2h_FG_eNNQllBOUwZTMZYK0UmFH3NZq63HjnL_Y-DQawq6b7zscyv8-IOMRB92eJbxexjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
‌علی‌اکبر رائفی‌پور، ازحامیان جمهوری اسلامی:
با شناختی که از سپاه دارم اگر نظام سقوط کند، سپاه پاسداران موشک‌های خود را بر سر شهرهایی خالی خواهد کرد که به کنترل طرف مقابل درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68783" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68782">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=FEWdadVJpp4JiXtSSzTeEijJzxJYkvSg7EGkYjUJeDFdoErumBOMJsp7okT4olzvaUL6yd3QQ6ivjHH4PM8cd9-d9HC9SY1nPueYIt3QkKsp_ctYuxXNCYNOA37FlJ-00B_ynCOh2euDa06rnfklVL5PLwDWqYg97KYGMT_GVsJfCAoncBerG1Hb22t9qjb8EdxNiCp4W4YgOVi3Eh3M7pIkiqzyAdduF6LIQrhkLo8DmTKCfAmYMe_LlE3faYzMrVQMuE9Nuvbj4s6f-Yl5UXiWVu--c_FkRoQnMwvHM0NSQorboSgRkMI-PBrzeIU2uXqtRI21b0v2X2MomZbk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=FEWdadVJpp4JiXtSSzTeEijJzxJYkvSg7EGkYjUJeDFdoErumBOMJsp7okT4olzvaUL6yd3QQ6ivjHH4PM8cd9-d9HC9SY1nPueYIt3QkKsp_ctYuxXNCYNOA37FlJ-00B_ynCOh2euDa06rnfklVL5PLwDWqYg97KYGMT_GVsJfCAoncBerG1Hb22t9qjb8EdxNiCp4W4YgOVi3Eh3M7pIkiqzyAdduF6LIQrhkLo8DmTKCfAmYMe_LlE3faYzMrVQMuE9Nuvbj4s6f-Yl5UXiWVu--c_FkRoQnMwvHM0NSQorboSgRkMI-PBrzeIU2uXqtRI21b0v2X2MomZbk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⭕️
گفته میشه دیشب با وجود اینکه پدافندا توی تهران خیلی فعال بودن اما انفجاری گزارش نشده.
احتمالا دیشب بیشتر پهپادهای شناسایی آمریکا، مثل MQ-1C Gray Eagle و... تو آسمون تهران بودن و پدافندا هم سعی می‌کردن اونا رو بزنن.
احتمالاً مأموریت اصلی این پهپادا دیشب شناسایی بعضی مکان‌ها، مراکز نظامی، محل استقرار پدافندا، و... بوده و ممکنه که آمریکا درحال آماده کردن خودش برای دور جدیدی از جنگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68782" target="_blank">📅 10:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68781">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=j8VQml4pKBCcdBxAQHMq5jJU-ElFvSQdhLGwx1yYXMw1HltXY-UGy9QN5MincMbXo44AwJ5XWn5IDCtMoN646Y2yAMj9BDZUGbNlA17TVLRxEzKkqRg8m2o2V7mPFr3-GhAOYWUc9AVOZBkTvhsLRF0Gru37OUwwByHNoxTZeVdKuJL-6xW92qSQLUUsMDLO7zyMONeFlGp7YlZ1eXc4I-dk-0Q-u1O7n6yjNjRDnR3bMeJfAInt3xFlWieTNJFi9QnJ-p11En229CbdYVk6g5aJfclHZ9tD5IcxWwo5p6_Ed-7dx-gzjfd6A0Nq2HN8ncKoFzVVRGiPTQktAz5k0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=j8VQml4pKBCcdBxAQHMq5jJU-ElFvSQdhLGwx1yYXMw1HltXY-UGy9QN5MincMbXo44AwJ5XWn5IDCtMoN646Y2yAMj9BDZUGbNlA17TVLRxEzKkqRg8m2o2V7mPFr3-GhAOYWUc9AVOZBkTvhsLRF0Gru37OUwwByHNoxTZeVdKuJL-6xW92qSQLUUsMDLO7zyMONeFlGp7YlZ1eXc4I-dk-0Q-u1O7n6yjNjRDnR3bMeJfAInt3xFlWieTNJFi9QnJ-p11En229CbdYVk6g5aJfclHZ9tD5IcxWwo5p6_Ed-7dx-gzjfd6A0Nq2HN8ncKoFzVVRGiPTQktAz5k0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو روز قبل یه گونی آدم از مجری‌های صداوسیما ، اعضای پایداری و بعضی ورزشکارها در واکنش به کارزاری که راه افتاده بود، پا شدن رفتن جنوب که بگن ما از جنگ ترسی نداریم و این حرف‌ها؛
حالا کجا رفته باشن خوبه؟
بهمنشیر که تو نزدیکی کویته و 14 ساعت [1125 کیلومتر] با بندرعباس فاصله داره
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68781" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68780">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=UpTbEcpvUq7utO4EJGeecU0rD3NablZJcyuJ1uE4_94EPFLlYfUPQqLHkH0Ao9YIF-tow7B2LJ3A09KmQpz8U0wpenw_e8hKjhn9w96cK8NSOlXJiZbZzVictmmYUSv_yjohOSmbzsbM9vh5sYJ1Yl61piwxjXbrh-gNX9UzmdwkOuXi6X3JVLEG5hYI9rlCZPae7pxHjUGMTjKTcFc00yodq1o7EXfZCrKBi1yE7BC2BEV2eq8UC6xYqgqdiGQRnmSiRPFvLKKZd1TUkjfUm0D2LI3TM5uBLrVFghwd9yLU7OA1Na7_xTA9hsACg3b53KubdEBYEzV2z_f_9RGVuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=UpTbEcpvUq7utO4EJGeecU0rD3NablZJcyuJ1uE4_94EPFLlYfUPQqLHkH0Ao9YIF-tow7B2LJ3A09KmQpz8U0wpenw_e8hKjhn9w96cK8NSOlXJiZbZzVictmmYUSv_yjohOSmbzsbM9vh5sYJ1Yl61piwxjXbrh-gNX9UzmdwkOuXi6X3JVLEG5hYI9rlCZPae7pxHjUGMTjKTcFc00yodq1o7EXfZCrKBi1yE7BC2BEV2eq8UC6xYqgqdiGQRnmSiRPFvLKKZd1TUkjfUm0D2LI3TM5uBLrVFghwd9yLU7OA1Na7_xTA9hsACg3b53KubdEBYEzV2z_f_9RGVuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظه‌ای که عادل فردوسی‌پور تو لایو فوتبال 360 بغض و گریه کرد...
اپلیکیشن‌ و سایت فوتبال 360 به علت اینکه عادل و مهمون‌هاش از تیم ملی انتقاد کرده بودن، به درخواست قلعه نویی و باندش فیلتر و از دسترس خارج شده و مجبور شدن برنامه رو تو لایو اینستاگرام و یوتیوب اجرا کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68780" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68779">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=pjp2Ff-7lVXiUXPYFniepHLQtcZbNxBOu3eO1jdeaBhaZjDQIZrd9fZCSd7O1Jp6fZi-z8ncj-ruafe7C_nGwT50EDW4c3IAMQiKdXBvEajPWmhunCg27j7DcIELfE5SJcvH24wMqnWi0uD-XNohESaU-6FVlvsiQYNndjVN9ykatrkpRrm2jtuXXcp15anOPv7Jw8sc-uJXk6LFAPh5wLtylIRGHOvQ_UYs_GyH0K-XxEJij67I1IyxNAyHpomIC9c-D2jx7nKgJJk3NR0tdp5VfqegwyVPlqH12yypuwz992tNnUYUZUIhL-2k_3t9nFGJTpizQiCpX26l2sQUvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=pjp2Ff-7lVXiUXPYFniepHLQtcZbNxBOu3eO1jdeaBhaZjDQIZrd9fZCSd7O1Jp6fZi-z8ncj-ruafe7C_nGwT50EDW4c3IAMQiKdXBvEajPWmhunCg27j7DcIELfE5SJcvH24wMqnWi0uD-XNohESaU-6FVlvsiQYNndjVN9ykatrkpRrm2jtuXXcp15anOPv7Jw8sc-uJXk6LFAPh5wLtylIRGHOvQ_UYs_GyH0K-XxEJij67I1IyxNAyHpomIC9c-D2jx7nKgJJk3NR0tdp5VfqegwyVPlqH12yypuwz992tNnUYUZUIhL-2k_3t9nFGJTpizQiCpX26l2sQUvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
نظر مارکو روبیو درباره برجام (سپتامبر 2015)
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68779" target="_blank">📅 09:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=Uoq1Za_8xb5kv4swh4wdgp6N3uG4YsWtiyqm3i5Zppg41GFxnd5FG7z6M6pu2nn3-e-Jk-5KoDlcEeNOOCaY3hWaoIMMAVfgvwZt8a6g7sYyw8Mf0vWStVEicYNzeOWKgnejnbK0twf70WJbbQQCjqJdsdmp-9byKBqUJVwE2OkrOQ_uM8nhrIOIDXv1Rg36VeexPeGKPCz089x6Dz0gxxAJshXZu7AyXByRFRRNvG7GVOrDjex5qFWKY4T0Fy4NHcosy-jNjcyQRFjCSBS82Klvn52U-BruXtdAfxlN-D7qYJL2pMpL6Djg8BCAsgdETMh34V2YAl4JMBGq6OAbuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=Uoq1Za_8xb5kv4swh4wdgp6N3uG4YsWtiyqm3i5Zppg41GFxnd5FG7z6M6pu2nn3-e-Jk-5KoDlcEeNOOCaY3hWaoIMMAVfgvwZt8a6g7sYyw8Mf0vWStVEicYNzeOWKgnejnbK0twf70WJbbQQCjqJdsdmp-9byKBqUJVwE2OkrOQ_uM8nhrIOIDXv1Rg36VeexPeGKPCz089x6Dz0gxxAJshXZu7AyXByRFRRNvG7GVOrDjex5qFWKY4T0Fy4NHcosy-jNjcyQRFjCSBS82Klvn52U-BruXtdAfxlN-D7qYJL2pMpL6Djg8BCAsgdETMh34V2YAl4JMBGq6OAbuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKOY4omaN0K3U9uPu6RyclegX2u04NXEPs-R6VZFXsBaL4ze1wBATzRFC4rf3ilPj0wIpQ6Z_VQsVVCKq-t7h1D3WolxacR8y2MyWVE9_hfnNdRBFzOK4UvjwqQq2O93AzN5ffkR_3KpD3ovIxrjM7DlUsqDiOn7Tp7ZibeW0jEfZXIfcVN1zv5l8l37RlzyusebbRI7UXmS8Ph1w0AsQyj9jY6kwJHbEwtLqdCLr8OH290SUP14UDaUh3rCp5P4vpSkPKRCJRlEyrtFoVoG6pNiReeTxyPPD00Do_YDLpvjHTCt_ipdFUOHY8Q4PCzygUb_qL2eAlZUngzqrK6tQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت پدافند شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68771" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون حملات شدید آمریکا به</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68770" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68769" target="_blank">📅 02:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تا این لحظه سنتکام هیچ خبری مبنی بر آغاز حملات رو اعلام نکرده! #hjAly‌</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68768" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بابت گزارش های لحظه‌ایتون عمیقاً سپاسگزارم، ولی حتما سعی کنید بعدش چنین گزارش هایی رو پاک کنید خدای‌نکرده جایی تو بازرسی گوشی توسط مزدوران ج.ا، مشکلی پیش نیاد
❤️
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68767" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
هشت انفجار در تبریز  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68766" target="_blank">📅 02:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68765">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68765" target="_blank">📅 02:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه #hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68764" target="_blank">📅 02:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68763">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68763" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68762" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68761">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68761" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68760">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان  @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68760" target="_blank">📅 02:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68759">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68759" target="_blank">📅 02:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68758">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در نارمک!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68758" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68757">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68757" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68756">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxYPnAYmGEygi27l3_19Bqj_MNi0oRlbWGaSVFFKnzJTvUuVCPvk1Z1mxJZNXoJAgT2NHcNTqUnw1LdUN3SSDQBCIS1RYrTBBPGjoxDe8VxtShMc0qGHOoxu4aH_Jb5hgzhiuSkp36A9YJ8A-lhgsrqm00pDAge1Dw25JmUeLd6qUrNF7umXlW71DwPZ-SlWdG56qLxJpsxmnE_ri739H10RFYIjPqYruaGW5iB3Yy9oDnP1sYc36Y3pTrqyzhwsd4oLVH-GGFGmsw6gTaH8zwMYkGJr-6eIwdTZgR7PnQ0QVyyanV0_xjNSEWFPLSXCt0C-NxlzahwDpnfcl-82xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68756" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68755">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=b15hOor01GtsYAwYJzsYftMHJ1Tbhm8afu6X-G9D6goB7jj9Q4MvPh7RIf-KaiWatreWeckNX5z5O3dNvf8grNRvf9V7hecr_dejLtw83jA2clNTv9DhKCPwooiBPKPHOSJbotHIwU0cd_y6rCTLRsGr8T6HNjp709pBZIgnVUw1Zln8_vG82OMieSclSb_KxramuGl9ytLjBM1_deamrFh-tN-LKDZtYuenDHblcuenzuFph1tmsjwJgka4li9nRxDxsf3_Xex5Wk3zLohHk-Wvuj4LhTcaBGhsTNyQCHX8aHJUH4R4J1G_UzEkGcwPJomwSoKCbW33rOoyAYxsKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=b15hOor01GtsYAwYJzsYftMHJ1Tbhm8afu6X-G9D6goB7jj9Q4MvPh7RIf-KaiWatreWeckNX5z5O3dNvf8grNRvf9V7hecr_dejLtw83jA2clNTv9DhKCPwooiBPKPHOSJbotHIwU0cd_y6rCTLRsGr8T6HNjp709pBZIgnVUw1Zln8_vG82OMieSclSb_KxramuGl9ytLjBM1_deamrFh-tN-LKDZtYuenDHblcuenzuFph1tmsjwJgka4li9nRxDxsf3_Xex5Wk3zLohHk-Wvuj4LhTcaBGhsTNyQCHX8aHJUH4R4J1G_UzEkGcwPJomwSoKCbW33rOoyAYxsKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
پهباد‌های انتحاری در آسمان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68755" target="_blank">📅 01:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68754">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
جمهوری اسلامی به کویت حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68754" target="_blank">📅 01:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68753">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=pcT1_Q20nEPUYOvruonerpL88vfmA7upW67YDIxQL-z-FhPIrwqipj41mxLk1IBZSicFwr6PV0H3B-vy-8msm7crdVaqB3TKA37ds_MZOA6h_9tKyjmu4kIZqkQhC3Lhgs2HKfR5OJv9Hf0_yvnOXvmOK0yd-esfQjdgZ7YZIvw9h4wDejA5w88gi_G5tTyYS61P3pkeiOk4KfZ5GwtKZrejncZBIuJ8z5odeYK-EwC1SyECUP6IUL8itYeqS6832HpOUy2ilr-OjyfwhX5-Z0fmsSY2vb3qYrz7u40PZHgWXcxVyOUmvtWuLMhWJg68uWus3mciWAF_YG0ii8qyzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=pcT1_Q20nEPUYOvruonerpL88vfmA7upW67YDIxQL-z-FhPIrwqipj41mxLk1IBZSicFwr6PV0H3B-vy-8msm7crdVaqB3TKA37ds_MZOA6h_9tKyjmu4kIZqkQhC3Lhgs2HKfR5OJv9Hf0_yvnOXvmOK0yd-esfQjdgZ7YZIvw9h4wDejA5w88gi_G5tTyYS61P3pkeiOk4KfZ5GwtKZrejncZBIuJ8z5odeYK-EwC1SyECUP6IUL8itYeqS6832HpOUy2ilr-OjyfwhX5-Z0fmsSY2vb3qYrz7u40PZHgWXcxVyOUmvtWuLMhWJg68uWus3mciWAF_YG0ii8qyzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست وزیر جنگ آمریکا:
«رئیس‌جمهور ترامپ گفت که ما دوباره درگیر جنگ‌های احمقانه‌ای مانند [عراق و افغانستان] نمی‌شویم، و او این کار را نکرده است.
به همین دلیل است که ما سعی نکرده‌ایم جامعه ایران را از نو بسازیم، بلکه صرفاً، به شیوه‌ای واقع‌گرایانه و با شعار «اول آمریکا»، اطمینان حاصل کنیم که آنها هرگز به بمب هسته‌ای راه پیدا نمی‌کنند - کاملاً متوقف می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68753" target="_blank">📅 01:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68752">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=S6D1PgOnzZM5QV_cA_WYM7uPvmE7NrRQcf2FAfgjysBgBB3z1PRNvRUmRetjA2vLCTJaHPPcEzM_qKwmhC13qQ7-05Azhk9bEz_IDyei5qeSqgaYNvTKN5st_pFKYatRFGsGlenK1SqJdtg9LqLyDVD8E01kf_TbfcJqO8FmXtsLspofIqZIPOmoI8L9e3aU1XjT6Y2RFlt4clMTpDIV0WyQ_8SGCf0xvzkcSfLPuTWgSG4yrfWyBANmt4DjFKXd4gV67P9QaPmlpXCDHJQNrVfoniFSM4ecO_0RgVjpXV3m6iKvidK2NzdF10fV86GJb2ASie6t-dxXmc6ksPZP_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=S6D1PgOnzZM5QV_cA_WYM7uPvmE7NrRQcf2FAfgjysBgBB3z1PRNvRUmRetjA2vLCTJaHPPcEzM_qKwmhC13qQ7-05Azhk9bEz_IDyei5qeSqgaYNvTKN5st_pFKYatRFGsGlenK1SqJdtg9LqLyDVD8E01kf_TbfcJqO8FmXtsLspofIqZIPOmoI8L9e3aU1XjT6Y2RFlt4clMTpDIV0WyQ_8SGCf0xvzkcSfLPuTWgSG4yrfWyBANmt4DjFKXd4gV67P9QaPmlpXCDHJQNrVfoniFSM4ecO_0RgVjpXV3m6iKvidK2NzdF10fV86GJb2ASie6t-dxXmc6ksPZP_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاورمیانه هرشب
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68752" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68751">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_6TjUqfE8R3QDgL5KlMYAafM7_IuHBi1mvivFopXlCbbWZNFHxe5gunlqBEz4cfsw_X2hEDTx19q9cdtL1fj6PiogpPaJx6n8ShH9p6sodt61QBmovbX74wTxO_gPPC3pnBCljLGXh3oDkPmZB-r7-DZKdRLmixdrt4rYMGkfzMj1Ry8Yl08uAnQ10C7uUgUM77RRK66BuTXuj6tmio9yUHnkskhIXtscNQradX3j0TR5ggI0Z6UhSrPxaTU8YgdZ-l2ld-j5WHzawztOb3oI_kX-_wJhySQMkrlanyG1FC73ZdztyOuUYyVmMJWhahI3WmvaYMEinMsL9JVmGjMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قرارگاه مرکزی خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته‌ای و تأسیسات حساس ایران رو تهدید کرده که ممکنه بهشون حمله کنه.
اعلام می‌کنیم اگه ارتش متجاوز و تروریست آمریکا چنین اقدامی انجام بده، این کار رو به‌عنوان گسترش جنگ در منطقه تلقی می‌کنیم و همه منافع آمریکا، همچنین منافع متحدها و حامیان این کشور یاغی و شرور، هدف حملات قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68751" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68750">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=TNaz7Ub86wiXlwpMq76BA7eyVM4jiAhA-3L2_e5WH0MeXgfnaHcYS9euoUjWxLlSVEeSYCm500UFBSTBx9cvv6jUKcUhdR9rKxcid-I_KV5Xk3ha_oX7JiZcA3iRJ9UbLeizxG0TWtufXqMuOleVKvWxCvpMutcrM7ge-WRzmHZTezAYxN2Z1AMRJ-eOZAjI3Z_hf_Flx_xsHsLyWVGxcj_kaSdfhiYIyJWCnuhmX5BdFc_tGZ9g2ZTmmhXpYReKbMAL-ZFAa3SbJUsQyeyDM_HS9EusQ1d2BhUshq0yySaXE4vWB9V_EsnPLHoudUJmGY41esSuI0YJyjtCb_gvhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=TNaz7Ub86wiXlwpMq76BA7eyVM4jiAhA-3L2_e5WH0MeXgfnaHcYS9euoUjWxLlSVEeSYCm500UFBSTBx9cvv6jUKcUhdR9rKxcid-I_KV5Xk3ha_oX7JiZcA3iRJ9UbLeizxG0TWtufXqMuOleVKvWxCvpMutcrM7ge-WRzmHZTezAYxN2Z1AMRJ-eOZAjI3Z_hf_Flx_xsHsLyWVGxcj_kaSdfhiYIyJWCnuhmX5BdFc_tGZ9g2ZTmmhXpYReKbMAL-ZFAa3SbJUsQyeyDM_HS9EusQ1d2BhUshq0yySaXE4vWB9V_EsnPLHoudUJmGY41esSuI0YJyjtCb_gvhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
سناتور:
آیا ما توانایی نابود کردن هر آنچه را که در زیر «کوه پیک‌اکس» (Pickaxe Mountain) ایران قرار دارد، داریم؟
⏺
🇺🇸
هگست:
بسیاری از توانمندی‌های ما طبقه‌بندی‌شده (محرمانه) هستند، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای از این کره خاکی دسترسی پیدا کند، آن ارتش ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68750" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68749">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=dbc6-ywja-tlNqyjuOm7UkU4lK6k6EXy5KoHI_85XROXZzK8no1J_1lN28nDYO0jxno_-Dx0HyugdqMahdRxS22lxQBrN7AUj82wvWOiABTCY8Af-3iTLbsTjQwt-2T19SwFoCI54JfgEgm60BU_W7UoYNtz5wbFFy5VLTsPzyQts6IEbTEKbY90e0qOOQbJh3WmbOuRUeOyMDLatJn8zqYFHikMdXYVXXRN7SfoDupvGSZt91GhtLGP-M_c-9ZH1Tm-5WJ3qZCRqrud5mxXCYMtCTrgkEy4W64zukDqOWuVfwrdd2E8KRXyKQjNsw8Auae0F8aONDY_jFrpqRNdhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=dbc6-ywja-tlNqyjuOm7UkU4lK6k6EXy5KoHI_85XROXZzK8no1J_1lN28nDYO0jxno_-Dx0HyugdqMahdRxS22lxQBrN7AUj82wvWOiABTCY8Af-3iTLbsTjQwt-2T19SwFoCI54JfgEgm60BU_W7UoYNtz5wbFFy5VLTsPzyQts6IEbTEKbY90e0qOOQbJh3WmbOuRUeOyMDLatJn8zqYFHikMdXYVXXRN7SfoDupvGSZt91GhtLGP-M_c-9ZH1Tm-5WJ3qZCRqrud5mxXCYMtCTrgkEy4W64zukDqOWuVfwrdd2E8KRXyKQjNsw8Auae0F8aONDY_jFrpqRNdhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست:
محاصره ما دوباره اعمال شده و عملاً غیرقابل‌نفوذ است...
بسیاری از حملاتی که دریاسالار کوپر و سنتکام (CENTCOM) انجام می‌دهند، توانایی ایران برای رصد و پایش در تنگه هرمز را از بین می‌برد.
سناتور جان هوون: « هدف از این بودجه‌گذاری همین است... اطمینان از اینکه ما و متحدانمان می‌توانیم در تنگه هرمز عملیات انجام دهیم... و اینکه ایران را وادار کنیم تا در راستای اهداف ما عمل کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68749" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68748">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=DzJKNAF56bYEUth6ToLn79p_xreO0gxsnWf7yTelFLuGnZizCNBd2JUc-Q_6DiyvxjDL-K-yffQkS_9E6g5GFigU8FBr9IDSAMTDxRxRXDEMTQtwwHVOwBOEB6zaLTSMXSineGKHdOk-kaYLfkZOetZYpeKCsfxkaKXfzh0pQNIsZZdv1fi_MfwcopNocYDeezG3DkU-QbMkgU-ctNZp1WdnFaCHdrJYtYI9UmJ3S6FBNuWWzVpnEWksU1KTwVkCevkkveKULU7xuOdKuNSOVde_KlHlHv20qBBz2twqTLaFRAES1YWK4WHLvcGWi2QwbYwYKXey_3U9dlkkaEHjuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=DzJKNAF56bYEUth6ToLn79p_xreO0gxsnWf7yTelFLuGnZizCNBd2JUc-Q_6DiyvxjDL-K-yffQkS_9E6g5GFigU8FBr9IDSAMTDxRxRXDEMTQtwwHVOwBOEB6zaLTSMXSineGKHdOk-kaYLfkZOetZYpeKCsfxkaKXfzh0pQNIsZZdv1fi_MfwcopNocYDeezG3DkU-QbMkgU-ctNZp1WdnFaCHdrJYtYI9UmJ3S6FBNuWWzVpnEWksU1KTwVkCevkkveKULU7xuOdKuNSOVde_KlHlHv20qBBz2twqTLaFRAES1YWK4WHLvcGWi2QwbYwYKXey_3U9dlkkaEHjuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
من در مقابل یک کمیته نشسته‌ام که می‌خواهد درباره پیروزی در جنگی صحبت کند که چهار سال است ادامه دارد، و درباره شکست استراتژیک درگیری‌ای صحبت می‌کند که چهار ماه است ادامه دارد، تا از دستیابی ایران به بمب هسته‌ای جلوگیری شود.
امیدوارم که در این شهر، دیدگاهی وجود داشته باشد نسبت به اهمیت تاریخی اقداماتی که رئیس‌جمهور ترامپ در حال انجام آن‌ها است.
آیا شما می‌خواهید که گروه‌های افراطی اسلامی به بمب هسته‌ای دست پیدا کنند...؟"
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68748" target="_blank">📅 00:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68747">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=dNDoMUyRDLjtMohP7iFXglHP2A1VywbCWf2nx2kY3B2IOd8CPnyG3_-9mRjKHwdakLAfyJyB2FoM_SXVC7nhPokVMPxsnTD9JGKlh_Dy0hCWaifO9ThR_bMe9_lBY08hE9kSzyhPVP8ZKXCc5FoknbMuIjTU2hkPOWTIbKHImzS8azaueHWNF-vFLc3Y6P6N1UKd5cNsgjmyuBOLeF4FRG6tV0FsOGPBb8CTp3oGpq5qTk6tfBoZAZA50E7m1IfaHNU-s7IbNzJr4jUnpCY4KgzeSL3r5eCXKqwINPmBbrvj-g7n92hesJ1Wta8GKJ4jGubitlZufWCr-CEjtmI1Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=dNDoMUyRDLjtMohP7iFXglHP2A1VywbCWf2nx2kY3B2IOd8CPnyG3_-9mRjKHwdakLAfyJyB2FoM_SXVC7nhPokVMPxsnTD9JGKlh_Dy0hCWaifO9ThR_bMe9_lBY08hE9kSzyhPVP8ZKXCc5FoknbMuIjTU2hkPOWTIbKHImzS8azaueHWNF-vFLc3Y6P6N1UKd5cNsgjmyuBOLeF4FRG6tV0FsOGPBb8CTp3oGpq5qTk6tfBoZAZA50E7m1IfaHNU-s7IbNzJr4jUnpCY4KgzeSL3r5eCXKqwINPmBbrvj-g7n92hesJ1Wta8GKJ4jGubitlZufWCr-CEjtmI1Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست درباره ایران:
ایران از نظر نظامی در ضعیف‌ترین وضعیت تاریخ خود قرار دارد...
بی‌شک اذعان می‌کنم که آن‌ها همچنان از توانمندی‌هایی برخوردارند، اما حجم خساراتی که ما طی این رشته عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین موقعیت تاریخشان قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68747" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68746">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=hXU5BoP-ItOJ_KTg5qII4xk3Tc_jzFpX0x1cqatoqYvI-F6TUSxbClJJxDswgSro2JV1q4_KSQyCELpThq74vAS77XeOynR35NOjnjJngQA2DBgdU7zp1T3lIi9OjFb9kQGE2gpKAKolPJtvzeV4yuTFWc0x8hsYvomzcypXKlkTX-6CNp1UWpITLEWVdMgbkBmlo_yh3dVOJkK9RHlMyi4Edshp4tV2L7Q-_yXKh-XGTQR41Bk4D2fo8an5flEpBLERXZQ8-lgPlLYt5-vFHoUrxDoRUGrg3vTxj2KLjpHTLnCQAVGu3lTb4uPstLM2MJ9lJfHRd6WH11xJt2UdIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=hXU5BoP-ItOJ_KTg5qII4xk3Tc_jzFpX0x1cqatoqYvI-F6TUSxbClJJxDswgSro2JV1q4_KSQyCELpThq74vAS77XeOynR35NOjnjJngQA2DBgdU7zp1T3lIi9OjFb9kQGE2gpKAKolPJtvzeV4yuTFWc0x8hsYvomzcypXKlkTX-6CNp1UWpITLEWVdMgbkBmlo_yh3dVOJkK9RHlMyi4Edshp4tV2L7Q-_yXKh-XGTQR41Bk4D2fo8an5flEpBLERXZQ8-lgPlLYt5-vFHoUrxDoRUGrg3vTxj2KLjpHTLnCQAVGu3lTb4uPstLM2MJ9lJfHRd6WH11xJt2UdIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت
هگست:
این درخواست تکمیلی دو هدف را دنبال می‌کند: حفظ آمادگی نظامی ما برای پاسخگویی به نیازهای جدید امسال؛ و تسریع قابلیت‌های حیاتی برای جایگزینی و تقویت قابلیت‌هایی که در شرایط اضطراری استفاده کرده‌ایم...
در حوزه آمادگی، ما ۲۱ میلیارد دلار درخواست کردیم. این مبلغ برای تأمین حقوق نظامیان، جایگزینی تجهیزات مورد استفاده در عملیات‌های اخیر، حفظ نیروهای مستقر در خط مقدم و افزایش قدرت نهایی پرسنل در عین تثبیت کمبود سوخت حیاتی ماموریت و پشتیبانی از گارد ملی هزینه خواهد شد.
در حوزه قابلیت‌ها، ما ۴۶ میلیارد دلار درخواست کردیم. این بودجه خطوط تولید را گسترش داده و تحویل مهمات مورد نیاز را تسریع می‌کند. ما در مورد موتورهای موشک سوخت جامد، JADM، موشک‌های مافوق صوت و قابلیت‌های ضد پهپاد صحبت می‌کنیم. علاوه بر این، ما از این سرمایه‌گذاری برای تضمین تسلط دیجیتال و فضایی، از جمله شبکه‌های ماهواره‌ای انعطاف‌پذیر، استفاده خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68746" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68745">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=hyPM4FLoGkJVrfLAcPhRyxUPw2nIcs7wjlek2j3u8zcVsSSGjl2nxsUJIJiUQzNfspS8xFz70yh3Pfh6EMyIegvdop29hBW8snoJM0Q9LHMgrdihXu2Og2Q2n30SqwSfOZz_aMcgb_lv8lwjaYFsLAtfOTQEDOPeeGx4XGDtbVVWnsxVJQXlt35hvnSxDSVNbbFWwN1SGf4cVfNcOBFXxnbRCK15IwriXFhMy1oIE9_YcdAEAqTfxQu89ZESHCKFTSOGiNawGuUIOSb93Zo79KR177dTzJHa6sajSLHkaV_xypo1CbkgnGDmHzw7qwu4Jg5I0vj5hRVLoNzCXxUJwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=hyPM4FLoGkJVrfLAcPhRyxUPw2nIcs7wjlek2j3u8zcVsSSGjl2nxsUJIJiUQzNfspS8xFz70yh3Pfh6EMyIegvdop29hBW8snoJM0Q9LHMgrdihXu2Og2Q2n30SqwSfOZz_aMcgb_lv8lwjaYFsLAtfOTQEDOPeeGx4XGDtbVVWnsxVJQXlt35hvnSxDSVNbbFWwN1SGf4cVfNcOBFXxnbRCK15IwriXFhMy1oIE9_YcdAEAqTfxQu89ZESHCKFTSOGiNawGuUIOSb93Zo79KR177dTzJHa6sajSLHkaV_xypo1CbkgnGDmHzw7qwu4Jg5I0vj5hRVLoNzCXxUJwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست وزیر جنگ آمریکا:
«رئیس جمهور ترامپ از یک منطق ساده پیروی می‌کند - ارتش برای تحقق صلح از طریق قدرت به یک سرمایه‌گذاری نسلی نیاز دارد.
ما می‌دانیم که بهترین راه برای ایجاد صلح، آماده شدن برای جنگ است - برای جلوگیری از آن و این دقیقاً همان کاری است که وزارت جنگ انجام می‌دهد - ایجاد نیرویی چنان توانمند که به چالش کشیدن آن برای هر کسی پوچ و بی‌معنی باشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68745" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68744">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0QkGo1rCv2wdtk4NOHoK63YrO4goaCrxCh5CqzqzKjhm2t9CGavUAzMnBhXA5Qk1gfV6cYsNdgJYzD5bkUwPgw55SscAL5P38gwmjnewvrtWXkJv12KvWA6WZZ912Xoc3_4k-XuQbrwl7KzmNvGCtKE-A-2ZibU6jk2DgS5F5c6Ps8Bw6K2vIJ-fhfMmx34zDaETKqOE-nFn6tO4ooTKVGYXQeOFsTIzxKxqVWJ0IZvKN6CFnEK7tV4JOl2dpKR4DeilTAlhmwS8ajRBBEJn2F0enwZBog8LQr2K87IoND04r55sEto5kaqXRanq1BGvWeBWGqQ5aHHZkmJ5rOdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
چند سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل بلند شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68744" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68743">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تاسیسات جدید هسته‌ای ج.ا: ۲۰۰ متر زیر کوه کلنگ
پرنفوذ ترین بمب غیرهسته‌ای آمریکا: GBU-57 با ۶۰ متر نفوذ
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68743" target="_blank">📅 23:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68742">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1f8Cr9qPMvbppv_LZTNE1a_jsXGUZqSlVUSFwUlAydJCE2NIghyhDIA7QEehs-ZmT_zU_KK5yJLHeHRGsBVpQ9tO8rmTU-q7aUshpXJbHccWPjCgwqVALX8dHSvxijNz5iCXLNK30KhItcn9bquqD9j-p-iH4PQcu0BO2nQEGpD_XR3CLuqdZ8ahsnJ6HuYVKCAGf39gcVhQiFQozW9tBvw2qBnqOnBecMdyQFft-qPSK3tf7WKI5MJiKazCo8AetQpY2zLCpVkl3Sa2H6TMtB2ALDcl6c5fbjc_j2jdAZYODbZyZVrwYWQlsUIW5FaG3SKHO7cEP2rJZCBkB0UrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
جنگ افغانستان: ۲۰ سال، ۲ هزار کشته.
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
درگیری‌ها در ونزوئلا: ۱ روز، ۰ کشته.
درگیری‌های نظامی با ایران: ۴ ماه، ۱۸ کشته.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68742" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68741">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=b_9XMjsZxiRSvm0qw0RvWwkdYpGaAcoB5SVgYi-8MRwukvQsnvjl0MBhcq_uwIMWwiPNO-EDEmtImRqYY41pxD4fhVUAHEwCXT-MJHDo4n0YK-mczsGBsAN42_keBP_eVqfqgAa1S159QJIiCOaPcWpnOXSClJZd3be2fFvTg5YtvfoChdCXHaJv8o3gLrfxUegSWtF3iJHrSyWPXe8fnTAGYY9IhhzW74oPLoH-PiK1ilUd087wH8GKyAJdwax86ZgkbOdbqJvFPSxyxkhXUKl1pO63xcR7yLfCfiVbJPC521dZl-72I1CCn_EmyrM1GiF0M3K6LMR1FnmWzTf8jpWxLFSni2szANbbR9QGJ5Zj5gGSBJeiZ2wWF8r1QSxr9ZW9YFyAQOOHWEP5FvtlXqiJlKLQZIOL4iLzwZXRtYMMotyspbgGz9qLIqyqgFg6F1eCaOsHmsh0kl_VxpLekngxy3RVEJm4qFz-MqS5Tj1-LIqL_KfcLtzz_7Q8O-A4Wu7QeWahGV9do0aCGusW3IrHwV1iJi5JwKjzye7c9YOV7VYzY2G0LRHLPo0F1UCABbnQ6ljzxD0jotzjmroifcE2gNBk11x1vjW7_7LqqQz4kB8NLAbvH0-QrMm0Xd0F7pZAB6CrQ9RqSdjL6l6Uk7M2snVev5eoAjwaasf1wRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=b_9XMjsZxiRSvm0qw0RvWwkdYpGaAcoB5SVgYi-8MRwukvQsnvjl0MBhcq_uwIMWwiPNO-EDEmtImRqYY41pxD4fhVUAHEwCXT-MJHDo4n0YK-mczsGBsAN42_keBP_eVqfqgAa1S159QJIiCOaPcWpnOXSClJZd3be2fFvTg5YtvfoChdCXHaJv8o3gLrfxUegSWtF3iJHrSyWPXe8fnTAGYY9IhhzW74oPLoH-PiK1ilUd087wH8GKyAJdwax86ZgkbOdbqJvFPSxyxkhXUKl1pO63xcR7yLfCfiVbJPC521dZl-72I1CCn_EmyrM1GiF0M3K6LMR1FnmWzTf8jpWxLFSni2szANbbR9QGJ5Zj5gGSBJeiZ2wWF8r1QSxr9ZW9YFyAQOOHWEP5FvtlXqiJlKLQZIOL4iLzwZXRtYMMotyspbgGz9qLIqyqgFg6F1eCaOsHmsh0kl_VxpLekngxy3RVEJm4qFz-MqS5Tj1-LIqL_KfcLtzz_7Q8O-A4Wu7QeWahGV9do0aCGusW3IrHwV1iJi5JwKjzye7c9YOV7VYzY2G0LRHLPo0F1UCABbnQ6ljzxD0jotzjmroifcE2gNBk11x1vjW7_7LqqQz4kB8NLAbvH0-QrMm0Xd0F7pZAB6CrQ9RqSdjL6l6Uk7M2snVev5eoAjwaasf1wRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
هرگونه موفقیت عملیاتی در خاورمیانه، از جمله در زمینه محاصره ایران توسط ایالات متحده، با عملکرد نیروهای نظامی متمرکز بر مأموریت‌هایشان آغاز و تکمیل می‌شود. تا تاریخ ۲۱ ژوئیه، نیروهای آمریکایی برای اجرای کامل این محاصره، مسیر ۸ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68741" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68740">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=GYL_bN7TKJ_79JDaB0mZzEhNwzsQAcR2_dJb0vgV-IJ-Z_c7lAVq0ke7_X4P7RN_bBKlaKSYZyMNWoSWMDOR8axRuy5tB1nfsrbeWCYEXmvAIAUp8S-j56Oivj7gvzBIgsPLqzaAduw6_W81oQXWYoUevxqegELqpxKHDEap7U0cschveJKhi122JUxnBZQnJ9RsxXXpWaqSZ8EM2PSex6NrLTrhTNRW-9krS9OtRbdoPipR8N0LyDwqrbH4MNES34xnnNeNrShszyqahm5nrAyhw6PStKrqn5EgkL3mOSrvjvbB_yuXOoFNTIuBh9x7hqh7lNnSm7Dv-KjC_2N6Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=GYL_bN7TKJ_79JDaB0mZzEhNwzsQAcR2_dJb0vgV-IJ-Z_c7lAVq0ke7_X4P7RN_bBKlaKSYZyMNWoSWMDOR8axRuy5tB1nfsrbeWCYEXmvAIAUp8S-j56Oivj7gvzBIgsPLqzaAduw6_W81oQXWYoUevxqegELqpxKHDEap7U0cschveJKhi122JUxnBZQnJ9RsxXXpWaqSZ8EM2PSex6NrLTrhTNRW-9krS9OtRbdoPipR8N0LyDwqrbH4MNES34xnnNeNrShszyqahm5nrAyhw6PStKrqn5EgkL3mOSrvjvbB_yuXOoFNTIuBh9x7hqh7lNnSm7Dv-KjC_2N6Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
جوزف، رئیس جمهور لبنان:
شما رئیس جمهور بزرگی هستید.
🇺🇸
ترامپ:
ببینید این خیلی خوب بلده خایمالی کنه، الان منم هر چی بخواد بهش میدم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68740" target="_blank">📅 23:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68739">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇱
کانال 14 اسرائیل:
سپاه سفارت اسرائیل رو تو بحرین زده.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68739" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68738">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=Ou0KRJ4JlBf-VcZ10vTdNwUsK8V6-ahu9He9UEM_2HPwgLylfjo8b4u5e6Eu9mrvBESNt50qZoF16VpwR0V3aH6HFszvBMMzN63XqRRkMe4IQy3U6RqcMjZZq548NNs-z7T5s9nJg9LkLJrBnelG8YJ3-nV3Ye_1xw1Eg2Xj6khOPqHiBcTK_x4UiEn3ZGOOSEC4iRjgDMoTrUVirnzV6qTcaygrn6XFBfAgbcbJjyNEewhQbHrPgraERJ5TrId3jJJh_z0aUmNSXgUP_1Zm27UlcekkPGkiY9ow36Zk5SpvFLrMcbhNzs7LGnspUENjnohnA3LYR23n3el2_7anSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=Ou0KRJ4JlBf-VcZ10vTdNwUsK8V6-ahu9He9UEM_2HPwgLylfjo8b4u5e6Eu9mrvBESNt50qZoF16VpwR0V3aH6HFszvBMMzN63XqRRkMe4IQy3U6RqcMjZZq548NNs-z7T5s9nJg9LkLJrBnelG8YJ3-nV3Ye_1xw1Eg2Xj6khOPqHiBcTK_x4UiEn3ZGOOSEC4iRjgDMoTrUVirnzV6qTcaygrn6XFBfAgbcbJjyNEewhQbHrPgraERJ5TrId3jJJh_z0aUmNSXgUP_1Zm27UlcekkPGkiY9ow36Zk5SpvFLrMcbhNzs7LGnspUENjnohnA3LYR23n3el2_7anSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
انهدام پهپاد جمهوری اسلامی توسط سامانه آمریکایی برفراز اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68738" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68737">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=BTk8DjdoqGosSfpZfrkhOqpr9c47Gk4sgvsxkQ2BGgK2NZnFqmjhWC19RxkN-SxstZ2Q76U3OmdnAFjh9mJuOmXvY6e80isgry7HQXZApWBqSWHoHI5Xw4JO6sw9xb4FjGInW6pfXECZAzqe8iAmGcOgXPK42AGZz9ENwaHR3H23jHWC0d6pAGoC5WXvB1lWzNZOYR7_sc22OySKQobMBYGQ0hcoE3TgX9ZonZhW_0RcGFxIOpUav9u5LRxjsLXj1O0XCJ8wWA9BSlVPKgLMEn8CFD2tUsO5WpVTDlDedvgb_curqtQWu-4_dtO-b5iVQbWuZPXbENABPPbHyYDHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=BTk8DjdoqGosSfpZfrkhOqpr9c47Gk4sgvsxkQ2BGgK2NZnFqmjhWC19RxkN-SxstZ2Q76U3OmdnAFjh9mJuOmXvY6e80isgry7HQXZApWBqSWHoHI5Xw4JO6sw9xb4FjGInW6pfXECZAzqe8iAmGcOgXPK42AGZz9ENwaHR3H23jHWC0d6pAGoC5WXvB1lWzNZOYR7_sc22OySKQobMBYGQ0hcoE3TgX9ZonZhW_0RcGFxIOpUav9u5LRxjsLXj1O0XCJ8wWA9BSlVPKgLMEn8CFD2tUsO5WpVTDlDedvgb_curqtQWu-4_dtO-b5iVQbWuZPXbENABPPbHyYDHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته دانش آموزی که ۰/۷۵ گرفته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68737" target="_blank">📅 22:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68736">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQC2Iw6kCoOukGQOOLpLL-dM64QEWZj7c_V9I7QtmnPOR1FM9Q4uNcnY4TJc64IyrcCyjCkI1WvTsrM9ILsarqAg7RMVT4yhjXGe0WCNc-ozd-vWAqk8Bv0ohdqfKgU8CHwRlKbfu2vtcGGc7DJrbh5rU_EUX7lnKtPlkxGVrqebpSinaVAU0C0phKnEiS-NcZa-2tOgZoyuJzbb6S9XqEqk7sVNYk7dbvTWieh7ZXLShb2b0k4FpdmO0wgcW2EQTmlGDcooZymWKKm7kuavszLBs0GVio8W6pwK9265p7W2Wz-8ECco2nN6CMEwxb5Rt4ZXP6T4MWCq5fpwrynB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به گفته بعضی از کاربران شیرازی، این اولین بار نیست که چنین اتفاقی می‌افته. ظاهراً چند بار هم دیده شده یه نفر میاد اینجا آتیش روشن می‌کنه و بعد میره؛ اما هنوز معلوم نیست هدفش از این کار چیه...
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68736" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQflCkavRPRyCGUOjTRCbxLDqiC2r5rvyjv4o6ToMdMuIaXvVTZa5-yL3LkEio0t6wikW4wf_4m2c1a-z0DYfuO_ealidzUQeCSP3rJ3SLlEz7g7xybl3tt0U7zuSGVOhEC-w2HnGQwPn_bH91piKsL6zeh12gw9qAndXTCzOo1iLiygd4282q8prssILXxf-Om_0MP_XNxpVA3VCi33WkwkwGPh_W1LeDZXROQLfavv0ORIeQRGFj1LwoLrqK-3-Y-YnKQPRC8FhVdA6XZnRtVlnqf9Vyrm0lTKzSjUJzwk19EQEqpr9i-84uv_nJAeMaWVE3-WUV8rXvAZDrx-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ru_Q_zK2CrU76VNSHujnbFUaBe--4Qdj1JKiyml6IjwOvKiPNNPFaeO056SIAjNcNmz6VloFmmE4xE9oTdsVDBc35dY5cO92Vdzp_49f2uzMmeSs4k7JQnP-T0nx0JYZg10qcJ8VTXGtf8Xw-u289fEfaafj8Bv-lAywGL_qfPlsnGwylmJfZma6WMVLgHZLlBnm_J38g2LcHGOpsn26C3lVMFnko2hL1A0z1ugXrNSKOYQkwwJXQZ8_eGZen1GNaDAwwH4Za-DP248u_KSk3fPZ9tDXAKZuEk30qSPtaXVN5rLwNAi9c0hF6gb-xsjlWMYk8En2iZrN1T8aOWHXpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A4NLa3Ybl2ciBsCdUVgLsF2iKN_WyjkqAokOFz0KDA7PlmE1jZzBu0xYnrQVqCBAIFD-An6HUTpNmx49QR1fajAo89TqBWjaF--L7yXuJpRS1T4weMZZel85COZ3TLlbagHq6aHOVmhu-0rUKiXExNTyBvcc65B25l7Ko0AshBgvcztbMsXVdEVjrE4yMqQjO63F8YZXVgmaMvkH0Vt4jTIjzm4mu110MiiJo-jUONWpI1HO25ML0yNIxbSzi-tuzJqaGtoPOSEiTPHg_SIX2VYZq8B8wqrWNFl1vQiPVUeOnduumXZDmrJ7j5opQnsSlx9iNm9kEZ2HVB6PMdJFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=Xrm28besZmpy3poUSfgg4ZnXZU7G1FI2x_oLdSn6EHXVpJYiGc8zS2-YDIi_utZqdnczn-hdRQbw4SkYgbHnZY8SwI_YhvL2TnWNB7SFWato90qVzYoeXeuQxMJgFR7MYfmm-poYuVkg3hUxNxx6kJkObC4ROX0GtrJzeR2g9GRB2ZNCrGXSF4AyMcW9_KGbfsjNTBk0QG7edQ5ktZZqYxK2RMlzNqL-gaa34c5C_WPBEXqb1y9E7mZhAQv7Y38xFfHnPKBmrMnJjtu34iBXTC4-61U4O4FxhGtlZnbfPp5G76f--B2LPUxrA72tvEcy4thL9TXPcvdiYtd0y3Pqkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=Xrm28besZmpy3poUSfgg4ZnXZU7G1FI2x_oLdSn6EHXVpJYiGc8zS2-YDIi_utZqdnczn-hdRQbw4SkYgbHnZY8SwI_YhvL2TnWNB7SFWato90qVzYoeXeuQxMJgFR7MYfmm-poYuVkg3hUxNxx6kJkObC4ROX0GtrJzeR2g9GRB2ZNCrGXSF4AyMcW9_KGbfsjNTBk0QG7edQ5ktZZqYxK2RMlzNqL-gaa34c5C_WPBEXqb1y9E7mZhAQv7Y38xFfHnPKBmrMnJjtu34iBXTC4-61U4O4FxhGtlZnbfPp5G76f--B2LPUxrA72tvEcy4thL9TXPcvdiYtd0y3Pqkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چندی پیش، همزمان با تهدید رئیس جمهور ترامپ به حمله به «کوه کلنگ» مستحکم ایران، چندین بمب‌افکن سنگین B-1 Lancer نیروی هوایی ایالات متحده، خاک بریتانیا را ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=fhjrq5nh96duGTTllapDwB0PI72yKj6Qqvm9FIRjRhDGexLvuV7GvV76Toy-Qeirm5wmCNpvbEFOMUgD9yD4EqSbzbIvxdN7erxyOxsb8SdbU9bBO8izHw3DgwR4SR0RqV5ivsVEtw5k_tvUVMAp08bA21crBOBUyOvSPRMQXuS6SQhyCGz6yirlFEKmnbZumnknRMWifOZeH5aESc9huWtSPYxOtQNBWLKmIkP9JcaZ2jq_EwVLqoIeeiubsHLNh9SRLtfyqBbJyV0sfq8DJCmS7E0wJjYgMNx7XZPA73XxOMyioKnRghIyVarfFuhMkPg9naYTINtLE-cbZvd5XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=fhjrq5nh96duGTTllapDwB0PI72yKj6Qqvm9FIRjRhDGexLvuV7GvV76Toy-Qeirm5wmCNpvbEFOMUgD9yD4EqSbzbIvxdN7erxyOxsb8SdbU9bBO8izHw3DgwR4SR0RqV5ivsVEtw5k_tvUVMAp08bA21crBOBUyOvSPRMQXuS6SQhyCGz6yirlFEKmnbZumnknRMWifOZeH5aESc9huWtSPYxOtQNBWLKmIkP9JcaZ2jq_EwVLqoIeeiubsHLNh9SRLtfyqBbJyV0sfq8DJCmS7E0wJjYgMNx7XZPA73XxOMyioKnRghIyVarfFuhMkPg9naYTINtLE-cbZvd5XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ:
به ایران فرصت‌های فراوانی داده شده است تا مذاکره کند و نشان دهد که در قبال تنگه هرمز رفتاری معقول دارد. اما اگر آن‌ها بخواهند به کشتی‌های تجاری شلیک کنند، آن‌گاه ما — همان‌طور که رئیس‌جمهور گفته است — ضربه‌ای ده برابر سنگین‌تر به آن‌ها وارد خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=IVbYwNszJBpRQpXqFuEqDN_qHYn2VUoFfHmFlGgeU75xoBHZsJ-CGsIdjN1aiTOip3sXn1yjDagmlv83AoBTRHcqdFGVNC-x_0oIi9MGg85KeA_9x18-Id7BT9vDnL5wgCA92ZEhEJeNFIQR1Ytt1tOr7EjGLv8xOugwc_m3ufjgrYA_Y3v7Hlc8BKrzwZ5GHEqjy124nLOMZCDafPrNrbfag9ATeGblIDG6JwHMp16ZTfXFx1h6owanXHraORgR9xHNInDhvk1SdFGMFl137XGO5yrzJ_hoCm6UP5mRaxyWqwpP4kteFgYKYUp-Dd9wg5NUjW4hGAsA4sQfEGtjDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=IVbYwNszJBpRQpXqFuEqDN_qHYn2VUoFfHmFlGgeU75xoBHZsJ-CGsIdjN1aiTOip3sXn1yjDagmlv83AoBTRHcqdFGVNC-x_0oIi9MGg85KeA_9x18-Id7BT9vDnL5wgCA92ZEhEJeNFIQR1Ytt1tOr7EjGLv8xOugwc_m3ufjgrYA_Y3v7Hlc8BKrzwZ5GHEqjy124nLOMZCDafPrNrbfag9ATeGblIDG6JwHMp16ZTfXFx1h6owanXHraORgR9xHNInDhvk1SdFGMFl137XGO5yrzJ_hoCm6UP5mRaxyWqwpP4kteFgYKYUp-Dd9wg5NUjW4hGAsA4sQfEGtjDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله سپاه که باعث کشته شدن دوتا امریکایی شد:
«داریم توانشون رو در حدی از بین می‌بریم که هیچ‌کس فکرش رو هم نمی‌کرد ممکن باشه. واقعاً ضربات سنگینی خوردن.
البته تونستن یک مورد رو از اردن رد کنن و اگر افراد دیگه‌ای مسئول عملیات بودن، چنین اتفاقی نمی‌افتاد؛ چون ما بهترین تجهیزات دنیا رو داریم.
ما تقریباً جلوی همه‌چیز رو گرفتیم. اما وقتی کار آمریکا رو می‌سپری به آدم‌های دیگه، بعضی وقت‌ها اون‌طور که باید پیش نمیره.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-K9cu2vK8FFHFqHsK-k-wg1RVtu1wPVIXFtP_wVFr434TBPmlF71L5sPBRke5sYhMytZrDATfMjx5PYuiKin1JD7cn9G4SwoYehmwdkTcaHtinyoj05y6a9AiSwHeWyE3zgiMSZm16PEPzuhSslbJu3L_231ijTr1HZMqqG6ilBGkj-FkVMjQtqqVHtpQjA2ySuxFAPnHx_l9ePgJhE95B83uMMoGhZ4ws6-IXUjSj2BoTiizb4UYWNKWfXltkWkuNelkxpQSezBXwjpzuh9gAlbj65J6zNyHWkcrmwMSwfvBrMYZLactFcj57XnoeO32wRwcUIlVN0vilVgspiCkFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-K9cu2vK8FFHFqHsK-k-wg1RVtu1wPVIXFtP_wVFr434TBPmlF71L5sPBRke5sYhMytZrDATfMjx5PYuiKin1JD7cn9G4SwoYehmwdkTcaHtinyoj05y6a9AiSwHeWyE3zgiMSZm16PEPzuhSslbJu3L_231ijTr1HZMqqG6ilBGkj-FkVMjQtqqVHtpQjA2ySuxFAPnHx_l9ePgJhE95B83uMMoGhZ4ws6-IXUjSj2BoTiizb4UYWNKWfXltkWkuNelkxpQSezBXwjpzuh9gAlbj65J6zNyHWkcrmwMSwfvBrMYZLactFcj57XnoeO32wRwcUIlVN0vilVgspiCkFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ:
«قطعاً به سایت جدیدی که درباره‌اش حرف می‌زنن حمله می‌کنیم. کل این ماجرا به خاطر سلاح هسته‌ایه و اون‌ها دارن تلاش می‌کنن دوباره یک سایت هسته‌ای راه بندازن.
ما اون سایت رو هدف قرار می‌دیم. هر جایی که حتی فکر ساخت سلاح هسته‌ای توش باشه، با قدرت خیلی خیلی زیادی بهش حمله می‌کنیم.
هیچ‌کس، جز خود ایرانی‌ها، نمی‌دونه چه میزان خسارت بهشون وارد کردیم.
اگر همین فردا هم از اونجا خارج بشیم، باز هم یک موفقیت بزرگ به دست آوردیم. ولی ما فردا نمیریم.
راستش رو بخواید، هنوز هیچی ندیدن. ما تا الان باهاشون مدارا کردیم.
من اصلاً باور ندارم که بتونن دوباره خودشون رو بازسازی کنن.»
🎙
خبرنگار: «فکر می‌کنید ایران سانتریفیوژهای هسته‌ای رو جابه‌جا کرده؟»
🇺🇸
ترامپ: «ما مواد هسته‌ای رو ردیابی می‌کنیم. اصل ماجرا هم همونجاست و به احتمال خیلی زیاد، خیلی زود اون منطقه رو هدف قرار میدیم.
کار زیادی هم از دستشون برنمیاد. معمولاً همچین چیزی رو علنی نمیگم.
اگر فکر می‌کردم می‌تونن کاری انجام بدن، هیچ‌وقت این حرف رو نمی‌زدم. ولی خیلی زود اون منطقه رو هدف قرار میدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=f864t4BQGl5acBF1LuPTZr6td2hrfbJqIBJy2bsNX8s5W8JnN1sywfJ-LRAXlXRBGAohyLmt90dNGr1GM1gm4T7aDpaHSXcxasxl9TsW4GQRRSpCZV8kY4QZC6XE5y8Dp1yv34LX9TKErPg7AcnSZvf6gkzEhnhNBUbpom_3gDZdEQhCcLf5xfGmvYxgyR47cy15PUSqxGJguyrSx8bSIuOzls4e17fENyrB5_ckBAedYdTL3vGzpGlgiDWrRcNqqILu1E-WGasqsVYSNIJLwI1j7jflOUpe2p030J8kh-oq0aa_Q7ylwFj-JBDESV7ZxM-5QRkFBDOz093CdAQEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=f864t4BQGl5acBF1LuPTZr6td2hrfbJqIBJy2bsNX8s5W8JnN1sywfJ-LRAXlXRBGAohyLmt90dNGr1GM1gm4T7aDpaHSXcxasxl9TsW4GQRRSpCZV8kY4QZC6XE5y8Dp1yv34LX9TKErPg7AcnSZvf6gkzEhnhNBUbpom_3gDZdEQhCcLf5xfGmvYxgyR47cy15PUSqxGJguyrSx8bSIuOzls4e17fENyrB5_ckBAedYdTL3vGzpGlgiDWrRcNqqILu1E-WGasqsVYSNIJLwI1j7jflOUpe2p030J8kh-oq0aa_Q7ylwFj-JBDESV7ZxM-5QRkFBDOz093CdAQEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ :
«جوون‌ها رو می‌کشن؛ انگار هیچ ارزشی ندارن، انگار آب‌نباتن. واقعاً آدم از کاراشون شوکه می‌شه.
همین‌جوری الکی مردم رو می‌کشن؛ بیش از
52 هزار نفر
کشته شدن و هیچ‌کس هم درباره‌ش حرفی نمی‌زنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=Z24UEVCKUvyaT75bfAG8zsAaV4WsG8jDvKKd2z_74QjqZhiGGb92-lgL8NTZDtMVgBH5FJO09IftRMXoH_IQd148d-4EbcZMKnH7PZnd-i-GHCCq9rijzLoqwwCLsHPyF3L0WNvdsHyhrIDmdDsBh1QqtyoYuxmg-WFMQYo63UF76HDAgDjCldifWP_PnJY8BNP3yglo3ggq_eh_HyNGwSDjpRIFSDp7u_Y_d6qegunskODdYM1nOErIt8o6YLvlLSLxLi1NcFOkudoNMjqcaQGzd6KpBAeUGqd6YP9Bx15D7FUOWh2hIgJKB5-vlmBFzDlNcHfWumRswdXUhMaeA1QAH6PoKzGJy_73lhCXqfPRpGWYhY-Y4MS3SJruBo9kKvQigrdil34ZXh70E0APFnrM5UcYczwS0R7ZPwybkUMaXiKbYc_aeH1pJUnGD0AOrfarh-6cHYIyG81HiQrIhbLrbqK1hcVgMwCji4JyEy1ogKIcwWFJCGkHWU5oAnVhAbtMHR-Y5wzJ6U_7e21Yo446At9RBWon3viAoqTxJt60-EgH9o0zIA_QG7n81yn21QwK-FTa4zinYimEsAm7UAMFlms0LC-g8Etawn-0LztUKHgihQVwrlDlKxlI9CBpWa950AMGCDJvYJgBdAXI5Amdnko5gvNsemqQhyXu5SE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=Z24UEVCKUvyaT75bfAG8zsAaV4WsG8jDvKKd2z_74QjqZhiGGb92-lgL8NTZDtMVgBH5FJO09IftRMXoH_IQd148d-4EbcZMKnH7PZnd-i-GHCCq9rijzLoqwwCLsHPyF3L0WNvdsHyhrIDmdDsBh1QqtyoYuxmg-WFMQYo63UF76HDAgDjCldifWP_PnJY8BNP3yglo3ggq_eh_HyNGwSDjpRIFSDp7u_Y_d6qegunskODdYM1nOErIt8o6YLvlLSLxLi1NcFOkudoNMjqcaQGzd6KpBAeUGqd6YP9Bx15D7FUOWh2hIgJKB5-vlmBFzDlNcHfWumRswdXUhMaeA1QAH6PoKzGJy_73lhCXqfPRpGWYhY-Y4MS3SJruBo9kKvQigrdil34ZXh70E0APFnrM5UcYczwS0R7ZPwybkUMaXiKbYc_aeH1pJUnGD0AOrfarh-6cHYIyG81HiQrIhbLrbqK1hcVgMwCji4JyEy1ogKIcwWFJCGkHWU5oAnVhAbtMHR-Y5wzJ6U_7e21Yo446At9RBWon3viAoqTxJt60-EgH9o0zIA_QG7n81yn21QwK-FTa4zinYimEsAm7UAMFlms0LC-g8Etawn-0LztUKHgihQVwrlDlKxlI9CBpWa950AMGCDJvYJgBdAXI5Amdnko5gvNsemqQhyXu5SE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: هیچ نشونه‌ای نیست که ایران بخواد جنگ رو تموم کنه. پس برنامه‌تون چیه؟
🇺🇸
ترامپ: تو از کجا می‌دونی؟ چطوری می‌دونی که نشونه‌ای وجود نداره؟
چرا تو چیزی رو می‌دونی که من نمی‌دونم؟
تو نمی‌دونی چه گفت‌وگوهایی پشت صحنه در حال انجامه. اون‌ها به شدت می‌خوان ملاقات کنن تا بتونن این قضیه رو تموم کنن.
اون‌ها به شدت می‌خوان ملاقات کنن.
تا وقتی که آماده نباشن به شکل معناداری ملاقات کنن، ما هیچ علاقه‌ای به ملاقات نداریم.
ما دارم اون‌ها رو به سطحی پایین میاریم که هیچ‌کس فکرش رو هم نمی‌کرد. واقعاً دارن به شدت ضعیف می‌شن.
البته یه چیزی رو تو اردن رد کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXHO948RX3a1P6Djp78SJ2frbCpMR_WKVOWDkXcy7SvZGGgprW3FIxSx6KrlyBYkt25Xb8CbpBDHFswvnwFcjzUAHRdg9nQEVjkjGMdZZV7v3KfL7dGrm8W82is7pmqZP2Lk1rmBpCbdSPghyc4ZofO9czlBLmyysCTsAy1OsdS3dtE1mr9vjYhkIz0vZqsMWQLFuIuDFaiTH6VaUFxllIjMyjIQM3ZU41CDglJ4Lau8BfeBLnPq6QCHjLbJ-JfFCfAyYHqnoIAg3Yqj55rBZ1-ZH52n6I6dSlnsbAe0Qp6mF_dPlQkU8EZebk4z7QtEvB6FPHdnSWLWjIxkp1TdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=No9D8tPOyxEDhygXj-GlIt1QxTAE4vr8xue1OkqE5gYS-MmJdaEPHjQXui3-0g_WhFTCFQKTJks_5C25NDWIb0lPAFeqMZWoBMjJ3tw-luLw2jMS-v9f5xUvLKCWK8tu6ZnkHn6gVPuUx7ruInJac20E-zFayyS1fze0nE8XjJszCxtO2DVT6h_1AUHJJ_fXPLgxHLy1nE8x6-W7mhCW7X6E6-dkNlxreJq8KY1NOnNtgZL7aEP-gfz4jnWHpn8yr-F40956_xheW1e_ul_jl1HO16Oj4hfsW_xXINbmrMh8Lg_GcZFfm1Wyy1UWgyHo7P9hKBdeNZBm2Ns6U06DFx-eI9IRxxcFpHraiPFCKrW6gpEDXy6re3lhTyYB_qj8kY8_KvJLLtXsOyLgNNOhyKrtSSpZ6Lby3tLHBW8KD-n-xlw9zEJya5kyEefRXKK9inr_s3SrzqBqTaodnozsMxEx7gZ42Dqx_2ILaLyqLmL4rsW40KX8eTt_VU7Vg2GRLmv2hPVRJGi64pTlEFhkBTtwGxuWCtrCUcK1NTX-kXTYH1L6W8jMNP-uHv2aMLkxq-TefeY5KAwwqAJTt1xRPrY2C8IHe4TORMvmYg9aB4Lxb1dCqeaeJhF1k1KA_z3AmN5o6sZn8492LsnEe1VXiJ1RX5uBAVx9k4VlJ95V0U4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=No9D8tPOyxEDhygXj-GlIt1QxTAE4vr8xue1OkqE5gYS-MmJdaEPHjQXui3-0g_WhFTCFQKTJks_5C25NDWIb0lPAFeqMZWoBMjJ3tw-luLw2jMS-v9f5xUvLKCWK8tu6ZnkHn6gVPuUx7ruInJac20E-zFayyS1fze0nE8XjJszCxtO2DVT6h_1AUHJJ_fXPLgxHLy1nE8x6-W7mhCW7X6E6-dkNlxreJq8KY1NOnNtgZL7aEP-gfz4jnWHpn8yr-F40956_xheW1e_ul_jl1HO16Oj4hfsW_xXINbmrMh8Lg_GcZFfm1Wyy1UWgyHo7P9hKBdeNZBm2Ns6U06DFx-eI9IRxxcFpHraiPFCKrW6gpEDXy6re3lhTyYB_qj8kY8_KvJLLtXsOyLgNNOhyKrtSSpZ6Lby3tLHBW8KD-n-xlw9zEJya5kyEefRXKK9inr_s3SrzqBqTaodnozsMxEx7gZ42Dqx_2ILaLyqLmL4rsW40KX8eTt_VU7Vg2GRLmv2hPVRJGi64pTlEFhkBTtwGxuWCtrCUcK1NTX-kXTYH1L6W8jMNP-uHv2aMLkxq-TefeY5KAwwqAJTt1xRPrY2C8IHe4TORMvmYg9aB4Lxb1dCqeaeJhF1k1KA_z3AmN5o6sZn8492LsnEe1VXiJ1RX5uBAVx9k4VlJ95V0U4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای، (خرداد1384):
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
