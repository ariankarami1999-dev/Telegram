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
<img src="https://cdn4.telesco.pe/file/T65xj10RbAQWdGrKZtScce2_0HoEKzNJfFbY22UMBvYAKNUb1IQaoH5zbAeUcof8Vbm1qG39ybgZxjM3dgxsMNhLwCayynaz88KrL8TUTFox-QhPyLGG1Z_FhpCa1LjZPeSoSvyIApm2k2vtOjprXeWlvdlv8xSdXl7EM_Es1OLGlU_IwKIBAyaKnriPJsvbx4T3P0uMBAvUX4_nlAS-o5BVx4h6z7PlS5z13kP97g2xRGnrUqIYF0X_EAKqEWxO3zmjgb9HXpi6y5vqB8lGtSIrFZiooMRgh0_m9l38yliZgVZYIsRAkRoVcYdHVNuNM09CcibSXEmlCrmAwxgQFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 21:09:14</div>
<hr>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYARrQngjfhwa9owHREzIhBJlle1fvYd93T-eRtLMXNZl_9QmyZARBMRmKkewF2BWz9ofITjKVeOpv_2od7TzX54wIoXPXV9YC4PEwnuCo7gdxnwYCCUnNzplYtarxqmFMV7SnOknrpVCWsM35VRqI5vUowF14HXsvsKQf3Q3JDpjztGhY-ASK6MBdghw8Jt8aLENNzSmfsgXLAcvpgLhneenHI9KGaVKBQ4tWeg4uoEUVHKsNsN2o-Yzki0pZqcA3qHP1l8ds_mPwZeAV9Br8q-ayC62vRGBopP-sf0lv72nciNuHwTqSFQ70-qnSgGgbzDagrXJeTpAThG1Uw5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2eq_AYHEmyGM-t_GYmfSql95uMhnBXd6eA8lfjmuRJ0S9IpYaJrKnsDF8Qb_P_DlU24goPy54oLm0mYmRRs2WhHRlc1r2-jzbpNLdeDRER1DPFgeKLrrqq9NhLt8V14Cxyjh5ZQ3Xf_rt1Qjy329fgY04VTxPaG397JLoKxc6uY0NK0dogN_CRyckU-m2p-3xHbF9WxAN5FgFnxMLsoDxTtijscmPEYhieyhtogDpdvbZv5pYH1R_n-ka7oaC2mXVSv6BdxH8F2np1_AO14syTt53AjZ5QxjxIVRscqJ-DZxcVYZW1yw4t7Ro2I9Nmz8rfmyZiXJzFEwMPpuX2lbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0qrPiYNKc01fZhSOtfSMkRAL1mDOFMCQ2oVoBujjzyAoaP7jkEnptWTHfga2NSFlUC5Sb5_gkkOEt_Syur11gZm05895M0VsSzzKAuV8UGa_VWQeAGUbx9pW8VJy1r0mmi0PiF3BDlnnEFHJB5iDpVIRXJyhoeHtuDOOVk0sUe7bVaP8dbOZkE9T_dK7_HSOtR_5xZReUUvKW9glgqIJ0lNUhg4zDmwOKM3-Ad8PGpG3k7sK6SnGDZUKyFxXTCDQ3mpjSuJcsRHEj38TjpsnO6H4q3131S0-BbzIqkfWkyDbr_cgZAENSyF61tTqa6Vg09xMDVc7S5z0ANYI4peNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDV4NmIBTU8-gdY0RKnCAzvjiXx28oJBnnip31C4OiSDTTEwOUNGVexRZD9_QG5jkK45saUvQEi4rOHQPQtVQpNJUQkx59kMKMpcZicz2pB4m623MpjDFgcWjdVId443VWo4UH8eL8Cf1VerINlh52dajLa1kR1ebc-4sCifnv4iEWiIR1ubjmIEi2a8UGqhL68chcldMMCahxPjqoC5K0CRmuJ57gHCAtedacevPwVZcp8CP_qu79tkxeDj9gjh3GSHkelKkgvjPH2Qhs496S61ikIh5yMCfCspk-6AfP9rw59F_YqTu4tdJanyY2BDMbONHNHo-hGpKMvUrfVJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBDF1oewFHdmY2bFPLROZ5Pft52CwEgHQo2KELE6Vwtqrhcg3BTSMR2_ALLPsS-wVmiNWyC_CkhSOmiz-aRtiPaGc3CcrkS1XTxBUYm_3OJ10dUESlgqHH0lNwzrA-OlaEDXwI0Vo9aYnl8b1l8-QuzGDkcLl5LKo92486sWubBx0EiFFe999esXmWyBOssB6YwabMV5TqhXgYbeBazMVeCGbs34V9JtyI8i_U0wjdNnsoKomQY2X41p5rP7TPNFnwlXQeXDs85eIeb7scpDn0a3Ms4jF5BYEJyt7VY1zb7qedcvxMkP00LqTJUV-gw2BXamUgwiyIM4Oqp2BdvXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cla1X7EnM2vgYNXhxoVWftOTnxDfTYErL_0E1bMH8h9L8UFktuPk0NqRhpeLhil5WJs9X65s5MhqGNxSdI8AkBaqLSzO0bS5v1ZlONehPl4Tm-qypaag7lKEciOMC2xKybRkbk8jTMyJpgnfJEtyu2AoyY-9nto8cz5Hx5Rrtv6rjnhN7_pafDkNcKS2GDpoJoE66QxBBld8l2B3VP900rabW69D1TvR1ynnTTpE_QhtLEQW09ZSWWna1JeQcngiFr8RPhVr9t4WWBMRP0gNtknRQrbilat9DzaQ1tu2QlpLL1UM9JTyKXlCO3uV-xb8vadK91_EYzPG0nkXeZ_MOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPKvEK4cjB6ur_6M9aekCBckrcJ22cHU0PmxM2_oifuYkZvOO7ZaIS98rswfm32qunX-rJonYvMgzsqR2IYxjY4nlWkV6_9aCf7lgl4HjwYhrW18T1VKqD8gQkCY7HhBFoQY7RxTN3PCnjOv0HsnRm-RRQ0wWnXwmsv3cMqbx40TicEgPU6O4FGgWXd8E9nmurKd52rZuTRBQWwm1AehZx6DG1pWuzNYKSGZOD9Hj1wihTVXJU7tUkd_l_eMoTcvUxuimTr9CxP1iHnjjgqpFXqto15vOayksNBX7uUcYY_azMtDmhTj8H_Z4blf8Lcxq5B_rZXthAJ96vmUH3ndog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw8hCPlWTLHpgVMfZiKHgPIugUEQ7gyIQZP9xgqu3GSnT_ZgmoxCsR1lMDwVlNC0lAKNvZKCw5AxurK9GkjWsuDJaFrrO_CwSBBBp98NLX2uLOmLGBjCNdkaqLQzpTOzoYIWRtrdCNHSKR1miGBK1tE8GHRxj3aT_jxxeWPwpBD8chi4L3lXmeifV2QyLiKnv7PB-PZbKg91dZEZ0kro0irSzQ0YSYVIEV75S2iSOICee3XcU4FDR7weDIusxFJiYOCdFbFu3bSpKjoPI1Bk1CiNSauc_iWSXnGfaVYipdKWbJ4GscM8fBGD-MxBjmXEf4N_hNT9CVHYTCv3k0Fqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=vqQkQbRKBzyKIrOptxlg8x5bfZIPaO2dePmNO33l2KtkgJ_0wEl0aFCxTZmS8nkWBiqkVjKhLCM0hrsUzX07w1z80IbO8HJOFeKUtqomywRHbK4d0qYACNl6RRCFsfL1fJhIW_qz81YEz5SYLjYG4Kh8v6zUpCktmTJwnhyB7l3E-29gvvEajTwyACc-AtbZOMyO3iXTcfEziEPxxaB_rnfw1ThwdGKbWSH8ZiNOcrDzFQMOx05KhakHb4j64_lS4lfkWVxA-PSvjF4wrICWZBTbDpuuckA4YcIUnnwwyCyZVKWC8LcxkwW2cwr_-6lI0KVRtY0qTGvSMiqaftmi1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=vqQkQbRKBzyKIrOptxlg8x5bfZIPaO2dePmNO33l2KtkgJ_0wEl0aFCxTZmS8nkWBiqkVjKhLCM0hrsUzX07w1z80IbO8HJOFeKUtqomywRHbK4d0qYACNl6RRCFsfL1fJhIW_qz81YEz5SYLjYG4Kh8v6zUpCktmTJwnhyB7l3E-29gvvEajTwyACc-AtbZOMyO3iXTcfEziEPxxaB_rnfw1ThwdGKbWSH8ZiNOcrDzFQMOx05KhakHb4j64_lS4lfkWVxA-PSvjF4wrICWZBTbDpuuckA4YcIUnnwwyCyZVKWC8LcxkwW2cwr_-6lI0KVRtY0qTGvSMiqaftmi1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfOhJJ3L64WqMYmjhcQ9Lg0jQaK5euGx3R2zeEOQPM2d5HCip8AAvEoHntjMy8C5EhNUWrjdCM-H4RZIsdRYjNdGAH4AKNuxxEm5qvOQcrFx00hexwYDjREajjfZByuvGMZD7lmWwx3n3hmjR3OdVqwv3blKDTZ_H5VD0mCmy_hLv4hdR2ZeGx_gE1l-iyXZxcFrsXTjzIvoHY8xXfM8xyqaGFOKGnZGjpBcMuAqXrU8M_PtEJnTHKC04tUrHsOxYoozvmh2NFuyVnQDcz8TMBk1TAyNmy47BMhHuVplKJ-bQ-keLWP57J1Mj99Y1DVh1EeF28Oz8w8xe2lZAHLpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StdbKNy2NYED09oUAj1exNe3bpmDbOQN8a2r_G_HYG14Q67H9sCdm2biYTTo_9AmCa5BRw-u__I0xuSYEB9pY1JZtQ0mx-8KXQcOBEjNFZzambSVsKCNsjZwhcyqh8U7K79OxOpppgMBLYJGXAjs6h-qqVr23USPmWpJmiRK8fsrRx5WkndKhiSnPwjj0PM3Ojusq2iXwoHwcED9ulmEj5S9XfwxhDL-QqMAFqDz6Z86OEw7wx0bcjpC6D8GUc_8rbMYZ4eISZC8p3u0ex6tYtXmecJHWT4vzxAFMhQA3lMbvhTMezgccWAnThOOemmp1A0B_69IawIPEH3spN0i-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0YdZm_XlwtWGvjqLSxs7OoJSB3FiMlFyB4cL33Sy9hkqCa_5UDWq6b3KG8doeaVdlX3vJl6LKyW1n7oi4TYsPA4-7KzeKgAMYDcoMaU0pWP-vjrUxgUTH4oobMYAuwIo4jreQ_NqjOF9XgpGqKn6NJBHQYQCNA00Z3iI8fIduKta1rilw_pWyWvhyG0kMG9LfHWTT1ma8cIUEui_gajpbKwTrKjjCe7X6z8_zMobOlIH5lwqYOitCKrnnmMl2UNCzA3EJwuFqDsenFeakJi80yBa-I3CYLLTdrhTEEbOAut3uy4ziR7sUbkvnKPHiwPHeDYTcxxO7OrfnsrMBENog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4qRUQi3mWBvfwhUjfiNuIyuM1lq7OP4M76SWu5bFry03AbqCC_vRhrNREJ2x0p-jLFf8sctfDt5NG3-UD4xBnV1VCTpIBsKIUp07-B8fX0AKvCjjL72hOlpiW81ePDe2N6I4_6uGX3dZDqby_oTVtI_stDHaevncShUHLm6dv2i58Ol4Ltun7dJSY2F48kLLEEc5ib3RKXkFuT6xnReeLf6YtIyimz7jnYoxgOWgJRPqegUly5RqKCZsQhAT_PxluCCHgN_uh2Ga3gAJddT1pC_kV7UqRCf-lDs_oqm1UAMWEzvk3Mc4NWtU2Yf4CuDoGqQPbihvSEwT4ZdXbN89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F972b6kBBj53eXauYVRPdxzlZ9gdbhHJrVqtCufF2KqpS0hnBLOkB6tlhY3in-2E2tokB1pv1EElp4tD6zR_CkJXnqrl1HMfyRfucPVsuxzIhevWXbDtflVbCX49VMlg1tKnIHYxjNHvCXxWtM7SEJebAe4Ljw38VUFRb4HBaONUUPkkF09bIQggiSgpKpG_v0IUNVIMeF2RCdqYwF0GLFx-cFtB55p0kz2d6QPpzn2Wf4Dt4iwvuePdOlMBgzbFzMOzuMu_YwLZ0eJ15JRtLEBjVTmMUyrCKYIihsyc_PzLXjm5nWqULOVZePX0-ms22OMZhb7mFJeHEd9gVXTj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=R-AFW1GUZ7EYbgMz3C1MuDnu3jEK9MurdU-sinX2EIHIx46yJRMt8q55Nwo6HOqdqYiDYDy0VzlqgsejnHDfyHJL3uRiP7SKhNiyWrIspyc2pSntsX3GmOlVyUMwiqkXHcvTLqa8C1qh3rOrYNL5vyNhb0A8JnnNEu1ECVZ09mf-BVNVI68Ejg8hqjbn0tFA6m6yNMOtQOI-yNeB1m53z9Sksswagn7a7V-6bDXDMEd79eedD6kTA_4JHb6ofnhKKzy3V6_TXBQPXz4qkswGRoeIwNxrUtDRry6CkZW9EhICzXyEukNl_-AAB3k12ZBk32DT9EKXFxT960Ndzj_s2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=R-AFW1GUZ7EYbgMz3C1MuDnu3jEK9MurdU-sinX2EIHIx46yJRMt8q55Nwo6HOqdqYiDYDy0VzlqgsejnHDfyHJL3uRiP7SKhNiyWrIspyc2pSntsX3GmOlVyUMwiqkXHcvTLqa8C1qh3rOrYNL5vyNhb0A8JnnNEu1ECVZ09mf-BVNVI68Ejg8hqjbn0tFA6m6yNMOtQOI-yNeB1m53z9Sksswagn7a7V-6bDXDMEd79eedD6kTA_4JHb6ofnhKKzy3V6_TXBQPXz4qkswGRoeIwNxrUtDRry6CkZW9EhICzXyEukNl_-AAB3k12ZBk32DT9EKXFxT960Ndzj_s2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hs0TLLAhjyx34i8pR2yQg4DPCUBhy-GRROFU1QywX1pcPgYHG6ofhGVIWYobx-qlK_tJH63Mn0VFD2aaekJj8TlIVxxlv4i_9OYMSLHWpEby6VFNMNQBjAGaf0zeMSpyTf1Oyk40xeGuxCC9TEjpS3iHaS8Cb1EUSJDHx-Y9JXOEvaj1vwUp9fCRS9HDVkaSfJCTXwc9-77SmiODMX3s5MZb-gEilT-h_N54i3gG9L6CazF8WC5TBUvHe1U2vzLimGm4Z14qMxXU4PjYNGd_2KT_zi19ZIHcYflfIYp9b-uAkjJ1DChP3w8pfRfkxnmXlNRu3OA4H7ZQcLjOkpZBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=KWCi8jyPtpfr4HPf9J6xCsmk5B1qhv4RipDuK07cs6TTvVTfhZSMzPwuDmLt4ZWttfE3y5UHA5C8iQhgLMSglF9fZBsS6YZXKzxaTjRaOW0MOeG6Hru4olcblLSOhFMIDpFJ8r1KqAoDohp356wxFIfLYjNKrHG0AgeyMb5sG4b6y2K6MhWFjAQ8tgmLzHzJx88xJXNN_FmlbsLeyVr4Mi1K8ThCl_L19ABnsuPW1Dr9sAExjDpq7733c1fx8TFMdC8PTSFfSzV68NYXCJmSYG3muz05hQHgkXqp7k3EIwHKUO6ehA_Ywl7JrfjW7yRj1-8qUn2skjS1lci_TZk-XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=KWCi8jyPtpfr4HPf9J6xCsmk5B1qhv4RipDuK07cs6TTvVTfhZSMzPwuDmLt4ZWttfE3y5UHA5C8iQhgLMSglF9fZBsS6YZXKzxaTjRaOW0MOeG6Hru4olcblLSOhFMIDpFJ8r1KqAoDohp356wxFIfLYjNKrHG0AgeyMb5sG4b6y2K6MhWFjAQ8tgmLzHzJx88xJXNN_FmlbsLeyVr4Mi1K8ThCl_L19ABnsuPW1Dr9sAExjDpq7733c1fx8TFMdC8PTSFfSzV68NYXCJmSYG3muz05hQHgkXqp7k3EIwHKUO6ehA_Ywl7JrfjW7yRj1-8qUn2skjS1lci_TZk-XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=oAzblp-2DJcPa684wJHQKafrZ1a9mDlXWAdAvZbKT70GykfK0U0yODi0LfB6Z7_maUVqchVQOR4z26DW1C8CjvzV-nQe5ORbvK1XtVC7u1e6id8lfJUR2iVFO2R2xZzsM94TjHW07GZguKVtvsGxRe2_gL7eMYYmWeyqgd4EIdXeglbbdPabtfqp82zEdHwmdyFxjL-ICGwZLwyAcMKx2whKAX3ZDU_oZzYdcB2SSsoQsvY9wB0n4YeZ1dAZLelLi5p2mwAnXh1Ee8ODjg2d7n8CWTvi6HkogzUWz2mJk7di767lzwTv4UT9spY2g6Zu9bQ_IUx3v1ugcC6gIiIJ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=oAzblp-2DJcPa684wJHQKafrZ1a9mDlXWAdAvZbKT70GykfK0U0yODi0LfB6Z7_maUVqchVQOR4z26DW1C8CjvzV-nQe5ORbvK1XtVC7u1e6id8lfJUR2iVFO2R2xZzsM94TjHW07GZguKVtvsGxRe2_gL7eMYYmWeyqgd4EIdXeglbbdPabtfqp82zEdHwmdyFxjL-ICGwZLwyAcMKx2whKAX3ZDU_oZzYdcB2SSsoQsvY9wB0n4YeZ1dAZLelLi5p2mwAnXh1Ee8ODjg2d7n8CWTvi6HkogzUWz2mJk7di767lzwTv4UT9spY2g6Zu9bQ_IUx3v1ugcC6gIiIJ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzIibcALdLlzMM6cawTfdlKysgak74dVFH4qFHday1jlMJJVRosOeCCXGIGqn3jo2LEXNRxInqFknqOFqdO5P6hHGGyq6bQOqgxOztlWwE4nPKHqkRINWgFoawBEeJX3F9W2WSJRwUXjDlPeIt20kHXOgUjQKaZVWTMY_Y2-0X7KTRiwsJodMjJHYEGRHCpupwSBuI-wOkDrMm0ANz6vdQunNC1fINuSuddCe4WRZHqwBbDd63y3ZzQOcH_NuOnn9D6VFT2NiGDBFZlXYYWyDMj7jWEJFsDP4X89YtTG_Ww9bWfevH-tYwOMCpRROaVoIRZ5cDLPbaVFmhHlNL0l-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scdtB-vkfjIdhSUO8nqMirHc5R-2EzvzVbnySA1y4H_myKZzIuKYRWE1g-0w3n3afjA97wGPxX2fp7lqF0OA3ofbZAx28YfONxEhTrZpaFkiZ7C3E9AsvWnVGRiuEG7MkXROQfZYXj0WtEsKsMMqM00Y1oEkpu7CvZ0bgeERVCX0kfXi8WJBreUl286YA4knEPtN6MfjHG0DgNg8I-aD4LH0yR7OK6zXLjQ9WzT2qoqh8Kg0UIwjV1HJXGD83hb5264tHdZ68fzSBA8Qfzt60_wvNU2TaQ0wyduFiTbRTGXqR2uRiTkjtHuPpo_ucbWOzxXntPmXHMrhksbLH0I9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=nksjFIMKBDXImnBfaDVN1i2iQWN5Nx2aXI7JZdCT25HSbj2xn3Jyl31btISsSwzE3gYNDWj-tVp4hsWaGni_An9e3qVEGdXv1jlrm2c3IGgSv4-dXtmOH6d8nlRMuXy06RiX8xrViojGMODecgkIsOo8mvX5-704uPu5yVPYAunGTnllYnDYdipBrRoXARZKOtLDpiVQP3L7NQtFlz7jDqDCdeTsSJSdEMRphyy02aBY0_KvU0S1llDCl4gdT36ovpTlsvWxPM8Yfe1stG_UX975BQHm0R8buSXnEc70VKYSf5aHYOWRT7NQWLZhktBxIOpRP0BD5L6ZBmfQBu-u3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=nksjFIMKBDXImnBfaDVN1i2iQWN5Nx2aXI7JZdCT25HSbj2xn3Jyl31btISsSwzE3gYNDWj-tVp4hsWaGni_An9e3qVEGdXv1jlrm2c3IGgSv4-dXtmOH6d8nlRMuXy06RiX8xrViojGMODecgkIsOo8mvX5-704uPu5yVPYAunGTnllYnDYdipBrRoXARZKOtLDpiVQP3L7NQtFlz7jDqDCdeTsSJSdEMRphyy02aBY0_KvU0S1llDCl4gdT36ovpTlsvWxPM8Yfe1stG_UX975BQHm0R8buSXnEc70VKYSf5aHYOWRT7NQWLZhktBxIOpRP0BD5L6ZBmfQBu-u3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaL5XG0pqn5qt0REpsH1UPkbk3HUoyhiX5p7zVcFOwuXVsWynQlb4LoWogPv80zjz9sgVpE21Ti1_A1t-G8eH-vtGAViyFWqZ8-Y4YR-D5YS0hlQx97yUymqm2ZCsx4TMHMJ0Lt3PJvsQnHLiSTBnsXBbMQU1sIuWfkNU21kLE98iOBTWgLMg756_-3gFCRK0YdeDJdagPG66rtj8zN4Ij_vfDzK9iHMvMzV76M0M3VyW36nDqUOX0Z8FYotTIgXJvmNFCRk-ZYGF5_CDmD6H04hnprWeYrHp7aWlx9BeXoJQ_2ydaeRoSx4vuaQlsVtYHXCQmHxiuUtTJY3lFb5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXUmipSsTVelmiexVXoe4-Pu5PUNNSpuumVGrRWUkndPJ_JFx_1fUXLOOW_909Km-QV9ehsXW4ekHaGITjAZQh4v0tytnk1DNqUnPXEU1hCZEQCJnWioSx_8QbitXg_qz1_qqGqx1myXX1zQaJhfPkL_tVOQr33jYv6DQKg-TLCTtsDAf14DSgCFwroBiNNEcONfwnIlROODBGs6NWk4Yb8jT7X6TCUgua7QrAgKTnkfa3p5tG7-7Ksg5RBioFvoMDOu3L90bof6a0peQvB3MSfYZI1Qf8Z_i4JoJLHwJA9t4dTvibpBsSxdRxt5uT8xm7dSvUBrpWH8013hXyWbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4WsQtVn3KG4EbVprntVEzGzGByBdHNZmcfDFh7YC3iCxDtIlvGBSvEtkrkRpwHcWsv23DmXYUODQOUQ4jifsrGF7lS90hVzAb0YiG45h7Gf4kbTpuJ7YAnvDruTUy7H7b5cwLievrfLUF7Y19MTEgxN1PNWbpIwTQhMVLuAUcvdbzBXs58IsKHnH-M7CGuP9f7vGTOh1kXKwVpW0r5vWzj_dtAtEf-7N1Xss8l4HkV7UCcS6Qqax832FQgyUZvXLCrDGC0xBP8lJdBjKNnVehjADheujeKoVq-t9UzZTNUce_gQ7q7xH5cx_BTrqN3cvLdk66IrDEidF-cVAQQrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyA5v96rsc0uJ1WDntbWHI0RYdilU6CVSfHwJdGDogPEZd9CZHpjVIqOcQgxD7oYs20bP-Bft8d3ao89FICfhzNNCku0dkXDe3r7XInTFVl0zsan_NrqDLtABXmR6lKrkL61EquUVJ6hz1LIqftieLsVW43K8f4g_V4OFIEgd0rEBAoJPMwTECT7U3TVfyDs8GFtk3zXINTlAE0Oa086uwABCy-2L1fXz46T02CtJb7EH_9LPM6DuGyU5k31fePO--f1-uzxm8ZvWO_PnygVyWrpBJLBLlFJO9FEJvOb0b6q069CF43UqEuatCqzpjsAtxtNvHGsjJ_09sCEfW3Xng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNE-irWj1PAQlMOjxEGh6ARB8aUMuqjioEQeBX76HdbloDc0G2FB1jc_Uor-l7EhsR-3xwtCex7r-cAuUuf5qIvaKRQsKPqyfWUKErCE2j_OtUDLF0epIzgeQVh5WLa_1jlbS4Srh2D7fNqAE364NbCk9WEDiJM185fCTVnRQOm9F3-wsvaCDU97BoTh-7ikMPVUMCRMfK6xlStHI8nmX2W6lvnXPLO1e7yPuVtgD9IBQ-c96IF-rfAnSQkhzz76tDiLJEg7ePUFBAkGUFKbkacR6bs-ln95cMadCsN0KEpZaLzNFblxUiGBoPRAoi9yf4zAWTtiHicaN-slQgPbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMp-4P8OuW_4KD32xzKLn3jp7fRwTOKUrmznoVHBik9swmJTU2dYjckUSpIssBslMw7m5S9wZPKE8lqwGPVGlmeHuOJDF198z_ZrliGoKRsVaDbMobwmafTWTmiS97ggfE__SNx5UY_THGgvmjk_prnCSPuvpJX6GhBJFzVs_lC3D25Y8fbqkkiKc9pH3gx9dd4htkVniJCo4UNpQ3t5d3A3WtQW7Z1bqAGuES4GIRuLlgsIiCqf9Z2wSalSEkEBDkA7qX1tE5YOJqYc3MEaCo2tM7gLKdIRK7n69ShXOnB-eMzMIA2T4AFTBDdXLjUK4r0MEMoIrHqiPiGjY4bq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEJNLhMMdSWZNd5psvwvqDE7s_4XzHSkRTMp0D9jU3J_KAeG68v0953W3cxGXmFcALmm-imkUndjHznVnII9xRAawNT-sUQBOFPjzVq_cU9pSP4Les_2UcugoP2j9ZG_vAldI7vlhhVAFSwWtN5GyGoSQeuPN9bB3vHQR3hKFcbN0Ht2Q-_m4Cu1ZtMDGdQgWgHNRx5bJa-JqI0-P7iOqB-IHTqPeoMgbTfpnyna1s5FKWWH3YqvH6KBhDP0YOf5SNpShqqlJav6RckudJ1x8woDI3OYXRVYLqkdeAQiyXEv0qAN8NGE3OnU6kpcWQ4LS-02vf3IeDTvCHPkr8Yrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM2wovcM7lIpjW9ubN7vN3iR1MG4FPYxOx-ELOuZ85ZTG88K2C7QCsYzkEavzDdI3ldcWle84HqnNUkoa2XqVe28CXna4EHtvhZ6x06ssjOeFv4fjleCaD8Es8MwpZOVD4LZuiuMur7R-NBYqugLKYhpwTpk2QrsQoJGoZMmfyCAe5csWajZJZPFeKHlyaTeSRZsRJW-AEGPgEuVk2YzeW3Nl63eVBpZKN-OOIZMMPc4oIBMj0_v7jrzK9nnfCrFZVmia4zatKswTFByylyNfsUSk1bCHNpqXInILlCe1X9kwIysfJKkiaZgFeZL1RqtnTdjbts9npR8lhuUw0pThw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epMeQjaxnK3qmvF2-A5ePDhvcttclZVYIOGo-9sJbvVvUQTL01G7dQdcd4LvBgTsgUH3FhWnnB8SU1obl5OryOablqjOcbPvAwKUdKoms0LikaF7VqghU9dt7H_sY8MqLo-_1ZlCI5WF2H_sKK-oEal5sHix51fofHtaWVxo6u67PpTH8CCWBLfj2WyqZttuknFD00kZc8h7bXZdliRSaxCoTAGCeWJKv65gArs6utPchRADCwqpgglUqgojgJGwm7SXri0UAl9vRJ2PxkfASRZQlPSEzJbwGftJ009Y0xybWIrZqeCgExEe44RZx23myUQj447KZrtiuM58GbFfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2P-IPeXxhSdb9Eyvd244o19404VJFUy8K_onMw3CJ8cyaQlnNYIZTbtWPkG5AEgSaiWqQkQWw51u6rDAo3pMyYJAK2KFZWIRsrCpu9YQojklPXpUKBhT-a83aSJ8dWdV5wt6QtpNloDUkG05MoaOFPEXxlbFMJMTuVVJMYKv6fzfJzXGKhdYVR40lavB2YPDy6I1yzOyfjAPaLX6t2ePz89gs9Phgej88lR6s2ekaPTGCfCYTsefyj0rvvCEBxpf2NJBQy_E5gY66mzmLPItgae7EGSycpcFvI1nSR5giuFFV67Eu70BWzI2MBjyx9g1dIHfheUoILfxMDazlVM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tu8F4nbDMA22ghh38SzdlctVG3u2enlyvkOemDPYQv8RGqX4YosR5JiX8DJaYuGad798lTWiTx8ngVEtpC3PJU8UlWDYU3SYHkSsvHBqkjgQFYGpQvQc9HmHbJyPnX6REvYS_8i1dXmPi-urM9pntqCcMVMgO64ALLrz1n-PpiC8jKcJhI1hy2HDv8rh1-BBqhPtXWpl4vdjUBgv91FBcwB4IqtxUOmGpu0gLm6-gusL6dZtkPH1UkfTdD-ZuPsLgpz-E4s5xiW3um_nhBcoqIONbjFBRLqxORKh1IgMiFOPyxW41KUuxrwIH9ZnejR2k6qLM8v8UZx3vu9BwbN6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=jR4j99fTk9nV8993LZbjxZKF0L1Itkm_HFLBttHX4CARQ-Oru3zinq6BJk2av_fzhTn33qRS2RSca0FUYZWlMO7OcDDgRGJoSh2mDQFIriLiFAMW0J4Mz2yC8_tbNEnq4Bd4Qx578lxqQa9cySC_TCAC3TbkmOftQc2-01g22M2TQ2NUttAYWN9FlpXsji8_Wj57JQi9HDfwm9GYxQ9MTyQRgwrQ3Hax98Z_Zu6NxMOWT5EunXRL0O7O1UIQS_fiwrPacUPwZt9fQHB_DljW1t6vyAEVCZo3WYVPkyLoNr65OsEyIfGcI_4H_GeiEmb_jTTJndKgZou6IS0Be8foUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=jR4j99fTk9nV8993LZbjxZKF0L1Itkm_HFLBttHX4CARQ-Oru3zinq6BJk2av_fzhTn33qRS2RSca0FUYZWlMO7OcDDgRGJoSh2mDQFIriLiFAMW0J4Mz2yC8_tbNEnq4Bd4Qx578lxqQa9cySC_TCAC3TbkmOftQc2-01g22M2TQ2NUttAYWN9FlpXsji8_Wj57JQi9HDfwm9GYxQ9MTyQRgwrQ3Hax98Z_Zu6NxMOWT5EunXRL0O7O1UIQS_fiwrPacUPwZt9fQHB_DljW1t6vyAEVCZo3WYVPkyLoNr65OsEyIfGcI_4H_GeiEmb_jTTJndKgZou6IS0Be8foUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=pM-CHw-nKfw5gQDnvs0HppHJ4JQg1kQlUqcPX8n_Dv4uhA8CiZoDF98cQvQ2Hw6MZ6TWRfVSgzH_wGzZBNj7p34n73LbbdnvLPAuk4SW8bC9MrlnaPUMQA6ozbIJn6p1PpMOW6nKHzipaNfdcXrDpf4gMoqmSHiOfwlHYLHqOYDK3PzPxmZC4-hl6wFuqtI0eInY_wdyrUGNXB8uIwzdnhzApMvVe7qfuRsGUlTEIkj0Y2iH82qaqfcSYorSCpMiw20p7XB-QWsM47yBc8oGKxHGqGw07Kp0EXu0nHOp1MoWQhq8KeKM7qbILxdgmAThDrhlOtXJ5F1oA4GIR3nT3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=pM-CHw-nKfw5gQDnvs0HppHJ4JQg1kQlUqcPX8n_Dv4uhA8CiZoDF98cQvQ2Hw6MZ6TWRfVSgzH_wGzZBNj7p34n73LbbdnvLPAuk4SW8bC9MrlnaPUMQA6ozbIJn6p1PpMOW6nKHzipaNfdcXrDpf4gMoqmSHiOfwlHYLHqOYDK3PzPxmZC4-hl6wFuqtI0eInY_wdyrUGNXB8uIwzdnhzApMvVe7qfuRsGUlTEIkj0Y2iH82qaqfcSYorSCpMiw20p7XB-QWsM47yBc8oGKxHGqGw07Kp0EXu0nHOp1MoWQhq8KeKM7qbILxdgmAThDrhlOtXJ5F1oA4GIR3nT3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1eivcjxt5zsrUvkBHNZOtQ545B7ago4L99qb9PqJG5PqIV2DHGYa3ohiphYxDThgnsR0apElxuqnPEy7mgFBrEugWx9yQ4E9C3NG8Zg2daA7lwYJR2WU2K0XvyVAdXlXqZm58yGQgt6gPLjhvy9i5KDCkctsXdUFu_MKmIzHPtc7FK3BVP_SmdtpE4x617xxXI3CMADJ44syo8-Qi_10ImgGxp8PD1LizTtuF_bqZOGDvmKNZTATqqjA6M7EtvrFNXix2OpGdplWuDlyCbatOx0IoZsf4bhHYe9WAAfJWhKIQpcsSQTHzunOnZs8glWjgh33fnQQd2MkHqg8SbPAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOMyMOJHA5BDznb-7IbpubD2mar0t9IKUAHcHpBtjj7_SHN8e2NUUtTCxd0NcJDT6PeM-Xa1-wfO45WFc4xOzcv22bwgPbrk1-kOlQL_4wkHvvn6XD0Fhx8BC53TB6oROHxelDLrHfZ64RqvgxqSpp4q9_j_FeBWrkRSLhvtw0tIvEjhVpPowjTC0UhV1XA7NC40ScicedmC5ateQsZAzJjbVff2ZOVXbEo29A6I4S5n1z_OAd9cE9gpFHZNkcF7CVkwYsOtLQDf667W_qy1h2WK275VLdvTt2TVGWuC8GYKRnWRaWnoA25zMka9sv0a5VxrTfYDY-gGb00i9X6C2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY8GCO2CKkjtw9fT5GgbZTzA1-_IxzPKDyqowdjb0EN0SJ5f7dSeqR0GeAORedd63AMaGvYSfPknZtK1zLa30b2gV3ivs8BanX8YnnThcRzQSvvhH_5Bff2J9dd94lqkgi6sCamz_qcOekYfs8eEqqCU5RwnFmhqzewixqukKFu9_nWklVY-4kalweFDVNZHN1iLotLSSRkUnyje4HWJ4jPCCzh2eZVaHdgK-koRRi7gCzcTD9G38ZOXEf4qzcbqRVtnKLtJx4dps7HmfyLt3PW32Y4qD_FvPti-qIa_DQ0Alh0pa1X2Sn-Yf8atMvPf8_W_-EPN0KAKuyGXfcU6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=ol27VaP33IF7WyD3spyCQOjXqIDQJiWpLMpOk0NsSRRKD2UWckhE9VTfp4aEgOlsDTV_joimqST_5VNomGKuiwsizFuoVUGuqG4Gq_zJBi5HF4hrUaIFNZ0_kunmVg9ww3bxZoE2uPXG-jG5XuYGyTIhkZkItSg8OCQUyjZiu1xe9vSu9Vh0oOj0Uvo3KanepxqLtTy5-5QChGJnvc3F9Y2qyZra9M4-M-jcLFbTs4sGY-2D7HgXtXPfF730SBKUz8ADUe8QjpdnWmaYuvTs1M5g7jg1-JQHbcKmPF91UzH6KChvNn9JVgZ1Hx0W4MkBm_Yj9p-f8_3La39GnF36yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=ol27VaP33IF7WyD3spyCQOjXqIDQJiWpLMpOk0NsSRRKD2UWckhE9VTfp4aEgOlsDTV_joimqST_5VNomGKuiwsizFuoVUGuqG4Gq_zJBi5HF4hrUaIFNZ0_kunmVg9ww3bxZoE2uPXG-jG5XuYGyTIhkZkItSg8OCQUyjZiu1xe9vSu9Vh0oOj0Uvo3KanepxqLtTy5-5QChGJnvc3F9Y2qyZra9M4-M-jcLFbTs4sGY-2D7HgXtXPfF730SBKUz8ADUe8QjpdnWmaYuvTs1M5g7jg1-JQHbcKmPF91UzH6KChvNn9JVgZ1Hx0W4MkBm_Yj9p-f8_3La39GnF36yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انترهای جمهوری اسلامی
یادتونه برای حمله گروه تروریستی حماس،
شیرینی میدادن؟ یک‌ شب شیرینی دادن و ۲ سال
به سازمان ملل و به دنیا فحش میدادن که چرا مداخله نمی‌کنید و متوقف نمیکنید؟
(شما چرا نرفتید متوقف کنید؟ و البته میگن
پیروز شدن و نمیگن اگه پیروز شدن
چرا خواستار توقف مسیر پیروزی‌ها بودن)
حالا هر شب میگن «بزن و ‌دوباره بزن»!
فردا که «زدن‌ها» شروع شد، بخش «خوردن» که رسید، مقصر میشه دنیا و این «لاشخورها» میشن «کبوتران صلح»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca0dBV0O7ofyME90N4lxMwbv6cN12IhipKIRptSVKQu04sllU09qq18KpVEaNbLniPaAwz4ofeqecQc6-cg8IusW6RNVg46M8nMmfLCjG3pDlpJjJuIVVT0dysLHNBdTtLtoELDq4oajVnxUAuHqsigJvGBEB91TkCJ-kP3TZu_vMzVbybB1GmBZ7fRp28jBRY6SM_9RU7ZLrGLVV5HOotpYG_kYY2nI89r-3dbG4i9BsPzDL7PVvEVaBpqn4kMDEbjd1ST0KEaYm_Jg2ZdVhEEfrO7jcGXZUIBoFwu8JVexShIjDvAjmctudg4rvHXnZb3EftZYn7dZj0-w5NtFaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veekGg4LEgh9x_rv5U1lz9_ljjDaU9XgC6nzX63KZ8L1bncBliHBpT_zUkW84LOEB5rO8-kRzKMf6puMdQ2zIMqy9zwkureGoGt0Z0KtKSYFFx_sBJf71qHBUoQBYeToMhxAgWlhpE2CiHoNkkVLHt6n8Dz3Ku4DcF6L_tzFcI0YfsDi-ZoN0NPLWEvX8-a_Uo6I4IiVyo5gGVvhsvPvEShucgsCd7byu19fPsqOcVs6DoSOGkRLXONrVkQyFGOTX8fxrSlC67zLsOFlCMVpf8-p6iXCdp9j-uZvsOp_Pkp74Fhn5E2CRcV6idIyWzPvOP5qMQ__NUMxN9QPP0f_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txyZfz6e5DSeAMFVkSbZZdwT6qfP1QaWLYGAuZ8BfB3eCyKeiUPxAZEnYEhtIv4qom3gxoPQR6eljDo7nSYj1viJ2W2xGkTB16TM56uPb_eczsKyaZeWEbLrVPNYiTEtegSdyGO_0fVBywRLWcr4aKO-1m_sFKz0RW5_MaRvxgY_bqE2ASwhhffgs5GEzElJZ2T_iV2C7u6y0jIP-3vlGzCaAq4vxnYlmWRMNdx95E_KKm6PR2OJSYscUyzhXmO9xcsQgjIa-oiZedKL_-Lt8uD71NvkmdZ43ikFDdZkrY-ST5ryWHNHjEsdTy3MxV3sw2PkHHrAZHwgAfSWA0_5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aq83DeVf3Qg31ht4qAnAaNA7GnqPdGPVJTbdGZso2NSUJcN-uMa1PU1uhRetPxGfsY4RsMtE00d5IhvfSbRMYeL0yjkZ2--ydrdXgP9c7b8_nlVnn6dPdSWeUPXcyKL2sReyjLnM6Ed_QHVlyLL446FI8nKXKITT_XAn100nf95WZCEFtUKVr1vS9ixGYvOf-8vJ6C6b0oQWCd5r1zdC1rb2d5r2nmcQkK2ZXbuhepqLRDZHeJz4SpuqcdBqyhKM7-VqBKtUTfi7bqxSx5lmsCFXTH4pzOk4DD6q6H86h2KCpZRRaR4Wa4JLw_UeX9o_VwYC8tDhtC5aR5Xfp0htsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXHOCJn3m1BIyfCN1HZkLPaznr4qmMHJwrmCCI3gvinvqG5X5chHPfjwtI1OM-FEmol0_FvfMQOCZMs6ZtWX9CCCsCbiwKEJxTo25RlCaKwvgiKYjgZYjiY9VZGx5bcosrv2wkYqBJB2VqJom_2nLDLQpRAwRfE4EnzjD4JWTB4ttk0MKBVwlY9PNys080n5upLPDrbHbM2W6Lo1pxDsjWD1ILM2UNOlLl1mu6Fy_cmgaMmek3Ti7bE4yzd48NeMT5Qv8bSGsuNBr7JTWCrjKudUgLUkas4N_Dm9S23h_0b3dtM9OzHUldWwP-thBLA9Q3nfOSDS-SXdI16UWj-BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfQHB_Cnj9V909mgYqNVzmpot2CiJiXcTeNFdqASU7827t--cRKOdFJ4dYvX-B2CtiQ2O3dmylkPacUzx2oIToqVNkMvF41I4QGAv17LFtJVpO_jc_TUsAfmk5esDE2ECWSzt7n6fzEPNr5iFYDYT87XfYxKFXdIa0Q12bedU7UhOlN1CcjtR6wqLNoOQRvW3nZ3Bj8go34fjMyWDOTm6HQ3Qwv57qwWDzLtTSu872BQaOY9LiYr_8-nitMv6JmOk5YVMYpqgIPJqZj7T6JkOeQadFwUww_3FcWk8Y5vyScGuRbpktAU0UtJwaQ0b4KaeMfKUEKPjOVLTsN3yMUO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxMvonmVk4h0SZswqDFN00N82uSKzsuOggjTjkTb2615fKoreDzT-R0rnIOA9vcifByrGjC0kwNj7LDEMp33zOugqQ9MJC8QwQJOJn9gu2U6O0_mQyB3XTxGvDo339UHeqr2AnblHF1guy-gyu9mDbaCgjkl5oUvlwAd4UH54nL2PbDbVc5Dadi5RywjNjhiao-cwRZ6WB3redm2FWGD3gKmSu6z7ie0OtbwZYEgdbhemt3KuTwu2kqVttdPbNOlclTiX2J3L1slpvx8gyDp9sQPKpXoGxcFXDqgY4qOrVmqbSBasuL92slbHGeHKtX-7hGEC2--OSgWJo6vS9fyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BtYNHm_0LaKiu474h2kQIMYhhAGdbV-u2zckmvouRQ2eKHa2mDP7OCI4VKNUUHpPsW-7ALMz8sXXtXZEnxktxvWDuqMdUw7qEbu-YFdbzz6f-toosiindslwS76b0STr7-_nHYArr9SWqcTXKnhDAM7R7SZZI73kfwgtTXFdpWTSrnK7EyzIwEtnrOXy76WMLDzsGLPa6aKbRmt8hrbnYGtPGhcgUXqbGGQDx0QYoJSNUbAGuJFiujO8_DcBog_bntkSE-I-40Bby8mr36eOenpvBwYMi0TxqsFAgSSITyAo7w5v8kmpW3dXLZpgjCc80h1cxWRHqJ_4aHNviBb5Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAcCr-NRtSfXT_DGmD2WI2cWEd40ydmAVwUKB-aTpo2xHwGrE6o9ANa9fWkwIqDiJwplbDM8k-gYrZP0100q7VRi8fo0xaoW40cFAFvK3GaNF_o_KCYJaOUz9n7ENK7clyjCs8jSzXZtf-6i1uY0G7Y6hfTcUtWKPKjfxRqTkTsYyCcNZIXtEaBAvDsNz8l5EmF5mRHhDXMrTuKVKk7bQq0e0cP0MaSBnDZ1xV1OoDSsPCgVKOJVnX_nJfbRecP4Q4p3Xx1-QMh8PhdaPch2RMugY7C74UdfCBE3m_IHL0q5OT1Co_egQNj-CAvnhtUpde8vO9k2DKX4beK5HTdTlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvTkENSWRAxOP_TueiBvNegmDY0mLi9rb9El7sLANXKrgaUvSmXtJe9kpoUJH_qrcG59cw59cVxtLxuPptD8iPuMQZG_E_LVbwXDkjlWYEC1G70Yyh8Mz0vjHOmyP_oC5O_Ag8Vos3ugJeQUR1UPMJJHZNdWwSiMSTZVHPF5JHv9rqbqGAYuFfg6OaDKeDxUSUogykKvbVmJDFMlZW26I6-JeI2EqNCPPynMH2WUfY5tk3jX4eBdiIRg_USJtZ8rLVwz9YAo3-N0PK4s1grvDF4AWni_Y5j7Q2rOmasFszEBtiXv6hGF6Uy1-pkRASW4u3k2iqy0cQvAIWulS3PHcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJIo6zcThqddPeL0DvnN32KHOYo9KE5-Y5yuQAD5qYe7caTLHQoQNB3pTx_up4roBeE1yvkxdO8IlODket5NRXM4P_zCIHay8LvUyZX1VTSukri4k4Amx3oXiIhnWn3gmFWpYNUS7L8Q4d-TlBr9mDzOTShzqG1Rtq3y9MAhY2UXw92RF1EHbgALMarkVYAoK35NGpPW5MQdYUryKN6KqMbbG7QMFuybxavHagBcfE3zQIvdb-DiUvCzAx_M_8RPH3g6NGh7-zNUcfu8QyTAU4m2CwvCI0_eJc1qwTsM-phhPzfwb9poWCPhx3J2V-nZvUISJ9S27DM_le7u7fEnNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=G0hOjOwQE66R77OXPOoe9fWirSd79OhLuLWeI6V70kSO9w5Lx20NagVS3kNHK4xHIyvTl-D3rlV_xGmRqP8iESmc7cscaL1XwSylci5BvmCTWouY-lghqLMaYg35zBypAVjhYB5bbHJIimM9akUZgh5sT2P-iC_B20iipg-84Vlg3FHBI1dRsBXA8jcGSkN5cQPuLlFdfh2IMA9eXYHeJbUoDr2sd_bVl4qW7ZbFfpgWJaIDL5HXt9lmJdIC2eJYa2VvcpV2_aHQjEsglcS1leQWdihOYRJa-nHz8Su6C_dRaXuo9bAp8e6pXRzsv8EHeoq3OodmqUtEuF0JVLC7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=G0hOjOwQE66R77OXPOoe9fWirSd79OhLuLWeI6V70kSO9w5Lx20NagVS3kNHK4xHIyvTl-D3rlV_xGmRqP8iESmc7cscaL1XwSylci5BvmCTWouY-lghqLMaYg35zBypAVjhYB5bbHJIimM9akUZgh5sT2P-iC_B20iipg-84Vlg3FHBI1dRsBXA8jcGSkN5cQPuLlFdfh2IMA9eXYHeJbUoDr2sd_bVl4qW7ZbFfpgWJaIDL5HXt9lmJdIC2eJYa2VvcpV2_aHQjEsglcS1leQWdihOYRJa-nHz8Su6C_dRaXuo9bAp8e6pXRzsv8EHeoq3OodmqUtEuF0JVLC7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=fce_IorFkueHvrtD8DB_fKMOVimIBg60Dxk73XQjgURfBHf1e3L9qOg1G7it0KvdbaLRPOXRQD9qK7eTWjKuML0E1eH_dnKIjvRK37FjEvnMveTiAykXYMfYGlVfBhHD5Viuwr4Rm22ngzXEgJBiLaxVY0T_p2vZ6d0_dejIqNLqi1ViHh584i-BCe3bSuI1VTaA_ZWqdPFEiWVycp3EzJJ9uejk-6i3vQd9BnxDLQN2fSgEk4HM1IEMb54I0oPhcdW7RU2vgLMOvT_waUE5EgikKMRDZ_4SgvzQrAnwiK1gmt2b_nlVMP--v15UsQSnYc_WdRxL4sMJlcYFIIbiDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=fce_IorFkueHvrtD8DB_fKMOVimIBg60Dxk73XQjgURfBHf1e3L9qOg1G7it0KvdbaLRPOXRQD9qK7eTWjKuML0E1eH_dnKIjvRK37FjEvnMveTiAykXYMfYGlVfBhHD5Viuwr4Rm22ngzXEgJBiLaxVY0T_p2vZ6d0_dejIqNLqi1ViHh584i-BCe3bSuI1VTaA_ZWqdPFEiWVycp3EzJJ9uejk-6i3vQd9BnxDLQN2fSgEk4HM1IEMb54I0oPhcdW7RU2vgLMOvT_waUE5EgikKMRDZ_4SgvzQrAnwiK1gmt2b_nlVMP--v15UsQSnYc_WdRxL4sMJlcYFIIbiDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=R11dIA9rzMjOcCdAgw5XvrdVA_5Hu4BI06M_nr3qe_ZgcMWaIo1YrIAwYHp2ctipexX3PL1HnTNuyC-7jjKPpHsWtBK6Bb_dukUhagUYmXEQhmmyN9cKNWhfAGpIDE5yAwfoqQvYXv8XJU5DPko8jJYtbdhLmTHDmnXyWoZpw7IEzF-bGBvOSDjAd_cZlZ9Eu1bQBFzbqGcQQv-g5lhiTrAPEylf5j_NBSn6Z42HWmau2cFkknSZunVuJctQkbCaPLI68Uf0EUQq0Bx6a_90cQ_OgweCfPeHoGIfIvFYi9smyN6Z2NkoXfnZaC1iAAN0498yJnbTZyCpVPy3bPkGqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=R11dIA9rzMjOcCdAgw5XvrdVA_5Hu4BI06M_nr3qe_ZgcMWaIo1YrIAwYHp2ctipexX3PL1HnTNuyC-7jjKPpHsWtBK6Bb_dukUhagUYmXEQhmmyN9cKNWhfAGpIDE5yAwfoqQvYXv8XJU5DPko8jJYtbdhLmTHDmnXyWoZpw7IEzF-bGBvOSDjAd_cZlZ9Eu1bQBFzbqGcQQv-g5lhiTrAPEylf5j_NBSn6Z42HWmau2cFkknSZunVuJctQkbCaPLI68Uf0EUQq0Bx6a_90cQ_OgweCfPeHoGIfIvFYi9smyN6Z2NkoXfnZaC1iAAN0498yJnbTZyCpVPy3bPkGqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtvPyXc6Zfd38eeGLXPbQcKBjm52mvtZqlxVAvNYOIE-Wvl3ODLFQykIzMef7UQdNQKojysXfzV1KVcOUxFxYue61Y-tRkJS2wNjpkGvxlbDCwNGxgNVhu56rvZSv0CqYbgIUs7w72VKTqCK6I5bh5EIPip9boTxi2PvCYu7Ud5xbNRx5oEjrZJmuNWvTFlNEaKvsu0R4rLdcAH81T5QIhoU2wXLAUCYQcDrKNrtnCCGmN6iuzVh33q5fVMfC9zIJ_64S71iW_8iBlcxmSkblez2nL0YjU5SmK3D2TgvQNCZTk1JNDiR8K2LTSe61EUlZUbDOhnuBUqKKfsopfbZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=fD8g4M8jKy7DW74R_bQL4WLZAQLtmwiKtALgkzWOwRoUoJhBsrfTzXvH0suQYqtReBuiQluPR2LPvc8kdsubN4L1EkYbYtkIxGoO4QppuZ9vGtAaHPduLCH_a_YBXMMF7rDaDRvh7p3epBmKJJCwJsfzpFp37Tor7qkEVmE-bM9fNUG9y6H-ASQI7NARNj3FDuPjTQjunOQuLGLRghby7VYkWLvW48wUiy40IiFNpRN78tt8c6-pZ-QC-ODHeNX3bQDYhSlub0CQeTX9t3BQRkNdjLtu9b64yOdZOv0tnUXh4gfHfHQj_PlD1RusIl0GM3g1yTcV69adQHlHPo6dIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=fD8g4M8jKy7DW74R_bQL4WLZAQLtmwiKtALgkzWOwRoUoJhBsrfTzXvH0suQYqtReBuiQluPR2LPvc8kdsubN4L1EkYbYtkIxGoO4QppuZ9vGtAaHPduLCH_a_YBXMMF7rDaDRvh7p3epBmKJJCwJsfzpFp37Tor7qkEVmE-bM9fNUG9y6H-ASQI7NARNj3FDuPjTQjunOQuLGLRghby7VYkWLvW48wUiy40IiFNpRN78tt8c6-pZ-QC-ODHeNX3bQDYhSlub0CQeTX9t3BQRkNdjLtu9b64yOdZOv0tnUXh4gfHfHQj_PlD1RusIl0GM3g1yTcV69adQHlHPo6dIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=cdCNYMSUrMARkfirgPeH3rd5YfQc-xcNRd0A2gtF45JcCWtO2Zdxbly7HyL1tddMmB-8Cz53V1pqFZb_Uyot1Us-rwOfDKFVnB70ekHylKmQwUUMygNM2cxMyKy0r372vGrMJyMhKmP5Xay988nsccVBaG_cUJOHYE4sm7YkVgBK1yYw4qnOuNj7ibKL-cqIY14c2uB4RBuaDPYBJXgft0EqymsSteYRx_1TGAF1GICV-mE0zp5IqNswVHyVWMMkkn3VPS-TRAlmOwQ4KQhv8XgSJKRRNl0Gxxr3AQangOiwYc3AdDw5ifTi6tG9iVGnP1fZUi8r40zS_kFLWc3cDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=cdCNYMSUrMARkfirgPeH3rd5YfQc-xcNRd0A2gtF45JcCWtO2Zdxbly7HyL1tddMmB-8Cz53V1pqFZb_Uyot1Us-rwOfDKFVnB70ekHylKmQwUUMygNM2cxMyKy0r372vGrMJyMhKmP5Xay988nsccVBaG_cUJOHYE4sm7YkVgBK1yYw4qnOuNj7ibKL-cqIY14c2uB4RBuaDPYBJXgft0EqymsSteYRx_1TGAF1GICV-mE0zp5IqNswVHyVWMMkkn3VPS-TRAlmOwQ4KQhv8XgSJKRRNl0Gxxr3AQangOiwYc3AdDw5ifTi6tG9iVGnP1fZUi8r40zS_kFLWc3cDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYE7LvVkLdvA5YYskUnzvlkiiE7W8btNJQf1_IXPdIwXFC5vKWDJLOrXAjmn9cUPP-SmzRM58v9KyWFJi-hVrU873fNUD3W4y2HRZnYHyi6m3u_p-CDn6NX7nubfdpxCQuyooiFRhCIlpCu8f1PAorKr0z4QRKRTm26E9i-0q4T95LKUun1GRhKXrPH43pyB64l1BFfMPK-UKTlVNWrlwgDldb0Hk_UM1z_7TFASmAaIoSqc_1_PKdNCga-Vw2h_5_wKgsOa8SIovnZ7mhHq9st0Mg0xpZOlF-fARtSSOsfZ8pvy1ZMO5-AzzSQ4lIMHShKz2USwBrl2IzTStIbYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqNz9RZaG7P-VVNJxmZQ7b1hkYcu-wb63g-lOVh_GdPlavj3VeDmBI_OAW_5P-00yBY7yjDPl2hwJg1n95ACjyf5ajg-Aq3QzMWshvSNhyzZAQCIBldMDH0WujgRmecLSQDsYSqMsfNlSfffYPia7yU-sx6XZETtt9YoH_Tj03-f7cYJhpOVN1TziK93jJQisT4jUWBzuJ9vOlolGn6mkK2nFNeNUoiwDM_BUF1Ow_T5Cxd-StOQ_NKjCjpXYCP4PORDiOIut0lnBiPsshzPeY0GN34ZimXEcBnjN9OjLpAjQYD3EeGkinICq6XWMaLzwknRZvLnbB9xvYe0_Q-uxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjVbc04CQIjKDp_UU44_Lt2AtSpFV9xTKPcOxjNsei7-oYt2RuDl2k1ez73WNImXgtdjP3-dCSovxmrHTwFK6-ycfnTBEh-4dOXGCt8dNULBJMtPBQ8KE-dHbdgMMFikw2-SpTW4r1NIxKpFZnaG9Zon9-exS4hzmF7TJ0a5RucslOEYhTX0sGODXWxai4At6i_jZURNGL5d4SWBO32zaPJEc5rMPWfKZ9t_hXYSBJj95wikIk58VRGoJAIfwcAFXwwhKmM3SMlXPrTz1HKxSd62sGR1baJErWVhUMQUkuV6c1txVlO_WD1YKkrYfvaJnVEkAe-bt5khJBkjMWJBOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWY-_Fostip_cz7Bd_Z7UaD-9O4WfTaN8Hv8vZrUhlTN0YbQh8A4_-0HfQa8bcj8zhUQqdQeUDjOP4CFefjH9-L85OZQpxn_2coZUenuw3NpIwBOQMsViu-NKvGczwnuq67K9uJLqnVMFfccygHwpnrKMw7cwfR83_xmL40zA5CWju3wp9XOC3fd8lzspNAQ1Y4yppKMN_VU1AgeR6Q6VevhO4TlbZ13-qeHmYRFaXxmAtaJgnLapwV3Jfith8vrIW8Fn4fvOTCP2NOxducWB1gF5kGcFNu9d4PxJxURDyAPqv8PeUFEYoJSxdv_LOeTsD5Iy1ykP0ISRmZjnjfjVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJYhwMFeOw9bPwA8HeXv3cuJQikcJDSrPMqZF0EoSxs0ZYG4s2tGLD-Akkn11W69DgATKk7gF4Nt2tlOOJoht5CPKz8ruoRgp4Ibd-gc-Hc1L0S3ExXjQkX07AhKbTgIkPfgTGKUWgfJnpQBBtDJJCLaQyIDKi68m_5Cjuz9YUtel048GL6NWveA9V3QR18k0WLPu83eAb7xs45nMxS9N7ZqdKR_0iEclrcpcm60A_OgB_mSpwTiDNAg1glGGUi7F-qL_oLGZ8pye4sMRiuKzfyhkEeoVq02R7nKYjzsI_B9wXvLxt-51923S-7Avl5hAziEzwcHZQgIPus1J09SMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6oETH2rKO05s_WapvFXOR207gJIjOTzjqUhuszQuOjolb7NXiXMG-ud2DvbjkAoEmolnoWQiogZWfaZz2CSmMd7ovudxqJT9-TJtaTmtH0bBzCEedr1qykJshLgaxao-1DxJnr2Zb_LmOTTxlmaxbtes8ywZzbmISLcmWDPXNjmz0Ef35XP37GKSiptkA2bhriQa3yihh7lwCc1vsPOIbrZlWeth-AI1zWxIG8wU1WD6PbYwLuiXaoTzn1a_p5I37PM47OqND_gEGgwhLxGHZIxsQqjefAqGV9shwC0uEzYHyOEMMgMPdV7K1R8cBxeR86mVRbRJ3GCbGb0-FhHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISlwotuec2naprpkuGLpCjnD0hxgX8qL3-kb9MuNY5ImW4uNv_7uzU9EoZ5bF8YEihBldmcAwmVhOayNPQuN8LKDdS-FzWKW1KBG4d1j4otAUUJvgWb1mt43sMNWcK5wN6bN8Jo8Rty6igHyWhK0ca0s4fseNIQPBY4UU_lpmwvR8mk1BAhGRIByuoOZROXkz8IbDHaaUNGdu_P4eKSUGOEaBouo76l8qQucp6-IjnziIoHymm-froiizunstv_sLHTaekc6YAlHs1nwCxru2JTyoZq7imgfEBOScN01FKIYlUGuqbtTGFTJIZE_snSsNM2z8AKX-TQ2gF69W1ny8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=bZY7aEjHSL8m-UEWbwyQWPWY-3LfYmMkKq8rlBH1oNRna9nq-BZA8OvDknTGhJjOQAkCWGpiEWbJ6p_HSGSj32GGUTAmuhg_Ia-oJBvf9V5MnhPPFN60cV6dXf56FjPQJ0HRGOoDlqsHiemfDJOm6vGNhcFmqLBVKCSqnGRGjN8gRwV7ycFbgOpD6i4ym7wbtii3DTdIdNsUrEKbJ1ANajzRY6XxqU6nHp62gqdj-vIAD0SOS32n38MAxCnHfLYsIlo94dLIDYAI8sqF_7FyO8rKykw5GQ9_F80tzrrwvoCMXpaPJ4vYqZ-bnTmEghFDrIOl70hJNrH9ouc9Ccvc1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=bZY7aEjHSL8m-UEWbwyQWPWY-3LfYmMkKq8rlBH1oNRna9nq-BZA8OvDknTGhJjOQAkCWGpiEWbJ6p_HSGSj32GGUTAmuhg_Ia-oJBvf9V5MnhPPFN60cV6dXf56FjPQJ0HRGOoDlqsHiemfDJOm6vGNhcFmqLBVKCSqnGRGjN8gRwV7ycFbgOpD6i4ym7wbtii3DTdIdNsUrEKbJ1ANajzRY6XxqU6nHp62gqdj-vIAD0SOS32n38MAxCnHfLYsIlo94dLIDYAI8sqF_7FyO8rKykw5GQ9_F80tzrrwvoCMXpaPJ4vYqZ-bnTmEghFDrIOl70hJNrH9ouc9Ccvc1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq3ZolGW_3zgGqyxQi_ihn2Hzh1aMZ4YrndoSGZhr278AN2LpoF9wPYysfgkfw5q_1Y3_gSawm4v05xi6KqFzH8sSBP0UHahSRt4i0EhiXK8ClELiyjtPwxLsZoG_z2gFp3fMot63scZvdDjJ6cxsUSUV8iB_JTChY52mVfCwX9hCHA8hxFHOWRB_EWghd_Zb76Smf2T540ryRd0CxwTF4jVbX79qmQSkQOP0Opqed4RHz_rVyfcztrWkvLxxeG8ZQVBfUhe6Bsjw6CzLCSDgoGAvvJquhb3PV-gJXh4fty9w6abxblQbWyoZXtCGQqap3n_1gLSt7-hCreNAhWmRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGg4ORm9V6oLbzbT8wxSPWjo_Ss_tTx5Exexshx375e0Zrh-euWOID1ukBXDn6Ke_-KooPA13-SMXy29NGHcgNdws_YR2z_zew_gFhbvVoXQIio9P9SpVXtcSpwpksLTcRLVj6v7WTh1iP3fWpafDrXUZqpq4lKzK6i9_fbW1ZiHXYDAcFX1Z9RNU9MS4mHBs0DOwi4ge2xmJE-KeYsRPC8gMxRcdS8FWdesDPyf6ITSBTovhJZBHrwkwt3sBt1LrI1MAHMyz0ct-W56JKvNcil0mq2ctOYdIthNkoPQ8U9pZogxKSu4Wy3dS2GJEa219Qkd2SR5uUX9wMhNJeLoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Drg_ChrVUAwCkK2VDGNh0-eE9jUt5mW0FFX2G42EqT3oVmRdnvxMrGlHHXKNGLVuYgSQWhdr-inAJ7YOM4lOkhp_CqVilibyV-lPPQ2bFUzYUQpMRkxNnEWwvkTLD2rurmEO0b3ATf1Ys78EG2luY4X5q9o_im0tsKJ0oNpgM4gFYWLjm-MnRkPs9tQDAd6ieC4ZJVIAGD9CeMZn_A3byg7249zKFMxEyR-d5OgB7_Q8Dj-08xAyXzZi_e_o_tv3mLoEVmiyL3cdDqk-77KuYk2W8_1Aiw1d7aR79FQoRFE1teM4DJ7CoToH--qC7UiWHSnxOFlMMn3tHo5OF0dPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oarNKKMWLIeh1Aw-HBYgTb62PMjRV3aD3bEijBB1nkihc9K44yxFd39ElRzb3oOfrN7YhCvEOT2s5m5hI6HdmD-EqLskrJJjqNHQJPp40Xb_RdHgebDn5MGFRIuHcu9gPh4NXIEgl12JhuetORtQaXyrkZkx3K_-zhaywdcRqoq_1Sa0Owr3XOoL9LzNC9bBgVLZNYkoJNTsTcbgsh31nYZIAz8h62DYSOpTj50wf983-M2z0rmWobKZPYpEXzRSIX9WX5pH9Vsc-v8RLULPm7kAs3r582G5mEy7hAGzyHzhVB64H7OCnVsFAwMyU9BVkvVhDhdxuTbblaJNHmPbpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
