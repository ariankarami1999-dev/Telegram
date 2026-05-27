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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 23:32:33</div>
<hr>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2eq_AYHEmyGM-t_GYmfSql95uMhnBXd6eA8lfjmuRJ0S9IpYaJrKnsDF8Qb_P_DlU24goPy54oLm0mYmRRs2WhHRlc1r2-jzbpNLdeDRER1DPFgeKLrrqq9NhLt8V14Cxyjh5ZQ3Xf_rt1Qjy329fgY04VTxPaG397JLoKxc6uY0NK0dogN_CRyckU-m2p-3xHbF9WxAN5FgFnxMLsoDxTtijscmPEYhieyhtogDpdvbZv5pYH1R_n-ka7oaC2mXVSv6BdxH8F2np1_AO14syTt53AjZ5QxjxIVRscqJ-DZxcVYZW1yw4t7Ro2I9Nmz8rfmyZiXJzFEwMPpuX2lbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0qrPiYNKc01fZhSOtfSMkRAL1mDOFMCQ2oVoBujjzyAoaP7jkEnptWTHfga2NSFlUC5Sb5_gkkOEt_Syur11gZm05895M0VsSzzKAuV8UGa_VWQeAGUbx9pW8VJy1r0mmi0PiF3BDlnnEFHJB5iDpVIRXJyhoeHtuDOOVk0sUe7bVaP8dbOZkE9T_dK7_HSOtR_5xZReUUvKW9glgqIJ0lNUhg4zDmwOKM3-Ad8PGpG3k7sK6SnGDZUKyFxXTCDQ3mpjSuJcsRHEj38TjpsnO6H4q3131S0-BbzIqkfWkyDbr_cgZAENSyF61tTqa6Vg09xMDVc7S5z0ANYI4peNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDV4NmIBTU8-gdY0RKnCAzvjiXx28oJBnnip31C4OiSDTTEwOUNGVexRZD9_QG5jkK45saUvQEi4rOHQPQtVQpNJUQkx59kMKMpcZicz2pB4m623MpjDFgcWjdVId443VWo4UH8eL8Cf1VerINlh52dajLa1kR1ebc-4sCifnv4iEWiIR1ubjmIEi2a8UGqhL68chcldMMCahxPjqoC5K0CRmuJ57gHCAtedacevPwVZcp8CP_qu79tkxeDj9gjh3GSHkelKkgvjPH2Qhs496S61ikIh5yMCfCspk-6AfP9rw59F_YqTu4tdJanyY2BDMbONHNHo-hGpKMvUrfVJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBDF1oewFHdmY2bFPLROZ5Pft52CwEgHQo2KELE6Vwtqrhcg3BTSMR2_ALLPsS-wVmiNWyC_CkhSOmiz-aRtiPaGc3CcrkS1XTxBUYm_3OJ10dUESlgqHH0lNwzrA-OlaEDXwI0Vo9aYnl8b1l8-QuzGDkcLl5LKo92486sWubBx0EiFFe999esXmWyBOssB6YwabMV5TqhXgYbeBazMVeCGbs34V9JtyI8i_U0wjdNnsoKomQY2X41p5rP7TPNFnwlXQeXDs85eIeb7scpDn0a3Ms4jF5BYEJyt7VY1zb7qedcvxMkP00LqTJUV-gw2BXamUgwiyIM4Oqp2BdvXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cla1X7EnM2vgYNXhxoVWftOTnxDfTYErL_0E1bMH8h9L8UFktuPk0NqRhpeLhil5WJs9X65s5MhqGNxSdI8AkBaqLSzO0bS5v1ZlONehPl4Tm-qypaag7lKEciOMC2xKybRkbk8jTMyJpgnfJEtyu2AoyY-9nto8cz5Hx5Rrtv6rjnhN7_pafDkNcKS2GDpoJoE66QxBBld8l2B3VP900rabW69D1TvR1ynnTTpE_QhtLEQW09ZSWWna1JeQcngiFr8RPhVr9t4WWBMRP0gNtknRQrbilat9DzaQ1tu2QlpLL1UM9JTyKXlCO3uV-xb8vadK91_EYzPG0nkXeZ_MOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPKvEK4cjB6ur_6M9aekCBckrcJ22cHU0PmxM2_oifuYkZvOO7ZaIS98rswfm32qunX-rJonYvMgzsqR2IYxjY4nlWkV6_9aCf7lgl4HjwYhrW18T1VKqD8gQkCY7HhBFoQY7RxTN3PCnjOv0HsnRm-RRQ0wWnXwmsv3cMqbx40TicEgPU6O4FGgWXd8E9nmurKd52rZuTRBQWwm1AehZx6DG1pWuzNYKSGZOD9Hj1wihTVXJU7tUkd_l_eMoTcvUxuimTr9CxP1iHnjjgqpFXqto15vOayksNBX7uUcYY_azMtDmhTj8H_Z4blf8Lcxq5B_rZXthAJ96vmUH3ndog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7HI9uK1YjtkrwjXjriEZ9Mf78i3aug9DRxVxLzsw-GFEL8uVNypFJB_g2SAbbxkXEqA3ltCh5ztafiTIdX4ErvFUOGshSYDwwxgQ6jDk-iVK9qjq0xg0f-eeP9lC6WR_Sh_VgtP-9COjyi0vBh6bp7rur4eZSmvMJY1g7fiW0D51UDHAtWBC2E8yv-zdkOY55DPlv0vsV1VFHTfxnwMmJpTt1eF1mzEzt0A7Fs5S2ijC2eY5ZL1YHwkTEiXpEJqwU6mFwiOFVtLjOzjT9iwi-CFKi2mVRTAP5hr--TGIrXkaCsfPvJEk61Scut339kWtnmWcQ6qB9XQA6wmOTksSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=aaGoHH6Rq2v3CWph9pim5DplYvOSyEjVwU9rLxpwMl2oIMU6omO1cE5iGTyvEXyUP34hxSFjRQAHNdChW-Lunhcb-URw6d2-BeohWvJS9dQNtd8KCB7CqTaDhmtFa3_4z1TPKCZubdp-LOVQfgb_7ySMif0VQiWPWt3oY6FNZNgl2XmPAppVKY6stRVGHZ6C9B4ORgqA6u8pDw1V8Dr45chsSluIv8Fpezw-qTxNoF2hme36PpPjKyKnRu2YKH6vkG6LyFHiiJpaWHY1Hb0q64aqO_G75rFfcBNGfZyzo9El5KD17BbPFxaip9m3puP6zNRIDEM8MmqCSGDPQM4RwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=aaGoHH6Rq2v3CWph9pim5DplYvOSyEjVwU9rLxpwMl2oIMU6omO1cE5iGTyvEXyUP34hxSFjRQAHNdChW-Lunhcb-URw6d2-BeohWvJS9dQNtd8KCB7CqTaDhmtFa3_4z1TPKCZubdp-LOVQfgb_7ySMif0VQiWPWt3oY6FNZNgl2XmPAppVKY6stRVGHZ6C9B4ORgqA6u8pDw1V8Dr45chsSluIv8Fpezw-qTxNoF2hme36PpPjKyKnRu2YKH6vkG6LyFHiiJpaWHY1Hb0q64aqO_G75rFfcBNGfZyzo9El5KD17BbPFxaip9m3puP6zNRIDEM8MmqCSGDPQM4RwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StdbKNy2NYED09oUAj1exNe3bpmDbOQN8a2r_G_HYG14Q67H9sCdm2biYTTo_9AmCa5BRw-u__I0xuSYEB9pY1JZtQ0mx-8KXQcOBEjNFZzambSVsKCNsjZwhcyqh8U7K79OxOpppgMBLYJGXAjs6h-qqVr23USPmWpJmiRK8fsrRx5WkndKhiSnPwjj0PM3Ojusq2iXwoHwcED9ulmEj5S9XfwxhDL-QqMAFqDz6Z86OEw7wx0bcjpC6D8GUc_8rbMYZ4eISZC8p3u0ex6tYtXmecJHWT4vzxAFMhQA3lMbvhTMezgccWAnThOOemmp1A0B_69IawIPEH3spN0i-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0YdZm_XlwtWGvjqLSxs7OoJSB3FiMlFyB4cL33Sy9hkqCa_5UDWq6b3KG8doeaVdlX3vJl6LKyW1n7oi4TYsPA4-7KzeKgAMYDcoMaU0pWP-vjrUxgUTH4oobMYAuwIo4jreQ_NqjOF9XgpGqKn6NJBHQYQCNA00Z3iI8fIduKta1rilw_pWyWvhyG0kMG9LfHWTT1ma8cIUEui_gajpbKwTrKjjCe7X6z8_zMobOlIH5lwqYOitCKrnnmMl2UNCzA3EJwuFqDsenFeakJi80yBa-I3CYLLTdrhTEEbOAut3uy4ziR7sUbkvnKPHiwPHeDYTcxxO7OrfnsrMBENog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F972b6kBBj53eXauYVRPdxzlZ9gdbhHJrVqtCufF2KqpS0hnBLOkB6tlhY3in-2E2tokB1pv1EElp4tD6zR_CkJXnqrl1HMfyRfucPVsuxzIhevWXbDtflVbCX49VMlg1tKnIHYxjNHvCXxWtM7SEJebAe4Ljw38VUFRb4HBaONUUPkkF09bIQggiSgpKpG_v0IUNVIMeF2RCdqYwF0GLFx-cFtB55p0kz2d6QPpzn2Wf4Dt4iwvuePdOlMBgzbFzMOzuMu_YwLZ0eJ15JRtLEBjVTmMUyrCKYIihsyc_PzLXjm5nWqULOVZePX0-ms22OMZhb7mFJeHEd9gVXTj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2kYEXzZZNOwZaODTxogNKjyceoXim_e8RhGRgymoXHyxca2VkELLSDBEU9LmEA5k-EykrQVKKw2qsY46qInbnh1PqMF_n8zCS8BxscdOFLsQe8V42VUq5xD_82gbc_w5ZACYeJf6W6pxO574PHtLvxJnBKmX95mLKxY0GyPinX4ps5ZiN55ZdIDiByG-hKTT4-16MpoJAQpgPljHbLypwOsbY8SVId1vo0QihcSBwGS89KNhR7jDfe5VwUiw7ZIXPGInmCchXCn3jEl_-9UlZF0wciKrBWJmNtjgY7vkWfiPE5zPPkeFNi8slsHARL-WCQf5pms7AgTqjMAiwNarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQKpEMV-3vo2PXQFPjLkIPXYk9ui_Q5voUi5tDVcJ3Zw3W4lzGuyIjyqIJF7wSBQMfmDXfWkmw1J_oZwhPT92QGIhQ52s5l1BGsSAuthECF84Rhs1IIBuz1EFMTkp3VJK4nQJne0_OJRp8Eq46RjjAIwK2nFePfp_DU11vtwAcWwdKfMtvo23CdXmj1fYQfQCsODuK4iB80klfPRGG3USIy-HJaiI4XuM-QWGFlsIRcnxa19FKOSXqpJ2-MddstwpyIeztgj4yF4FkpkueIrRe5mAur75Dlfbxx4TxX8E_fo4s_sokpkWy-GteMQ2cxzFfQ-Qe6PawFMSHD_F7sq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=Mk9GUMo3FF6jyrR7FBKaDutJ39ZaLDgRllvkeiTvjN8emsMtCaeiK9MDa3bC9-T_RiwSrEkfH4cU01bqpiiWmBeCMasc1z-IbKIQNEGnjcw8jkHI9QOj5JlUKctJYeZX563GaZn3F8iidAcUSS6gGCO-pnak1K_eYNfPu9cxHgwF2SIorNX_X2hR1zYUBwQ2ejxxsAAyKmPwM5jPj0NSyfCXJUdj-zF9zqZ1o7VFJmPioK5whGm0mDGc4pFRyPR-RwBnZHXzCCi3nZAqFcGZ1fXneu8nw99jTDflE088lds7VbFGEwucei7b5FYYp34xMLgwvDpOx5Fmg6ceLOKkPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=Mk9GUMo3FF6jyrR7FBKaDutJ39ZaLDgRllvkeiTvjN8emsMtCaeiK9MDa3bC9-T_RiwSrEkfH4cU01bqpiiWmBeCMasc1z-IbKIQNEGnjcw8jkHI9QOj5JlUKctJYeZX563GaZn3F8iidAcUSS6gGCO-pnak1K_eYNfPu9cxHgwF2SIorNX_X2hR1zYUBwQ2ejxxsAAyKmPwM5jPj0NSyfCXJUdj-zF9zqZ1o7VFJmPioK5whGm0mDGc4pFRyPR-RwBnZHXzCCi3nZAqFcGZ1fXneu8nw99jTDflE088lds7VbFGEwucei7b5FYYp34xMLgwvDpOx5Fmg6ceLOKkPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnmFPp7ZsrZZsOx7p0xHKh1wVqJtXHHBnMniCxk1a2V3ojyTtSrFPCcFnkMl4N46_vaZE6fpcOEEikf4J33OwPUmE_skt84ZKh5TIzlnOmrAvPe3FtNNsA6vd059xmkgXnX_tix6ybdNgSVP5djaDYPa9pPZao5lsqRteXLyXL5k8QpYyF7BddLAMHWGyWt9GgHt-ppir2Nh3qfCGjfQ-0nnkLat3uXkHkJvffYsAQsR1db5uvqaOfJ1yJ5wcHcVrTRccVt0-b2Ted65BXH6stHHZPZVNIBvQNcId7GbilZdxfHl8I77FS8PTOUdQjbp2KEQRdab6JWd4vC9bqlrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMk3-ChgSz_L43-QRXLDkCVSAuAF3ZGvELuX5Uk89HbW9Ry1qMDugpgg-CbbwbtUXvKDkc1IVamoze7d8hiRNZzkEH6NBBYX4WjFnNWJu1OgJ0iFVUZ0yGVcfbRFPstMKSUzJLIpj3HEJQe5YKfgjPUPGLgPtdcda6RGWBsk-Yshysp2W4SHDexas3zKhP9p3QGA9WjuIs3HUZ0kDXq1SkVa853f8cU2UuuGpuk48R3fjAe4rQ3KqzrykliKHA5keNJZiMQoUJOxxVJq4qnkkaru4AbB-lgoGnJBNV_Cc9ZcxJfipnnMLb74Pw2jtY1o7JnG28-3BNCXXjn8QAfMwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBkzbifT-qbKiW8BGPXkCrVEYZINvpjMhN7y2d0wKYtDtqZZFny6RRAHbp8hkjQ1PqoJPXRy9emxHzAecjBrv-qyLJb_vnUJeMyXJvP1PTG3BPKZuL3teO8LBUMtvQrui9ytlemdandxAcRx4E5HCyM5hvKpvDgC9s2kXfp1EFSz5g3BzNgzLUYNwzd1kd7SzGGDBtV3IQeoZtGC_fK5PufkvQtVyPBnIc1XYljsDf9Dm4O66wvJp1Zk_IFxxeHteZDir1gWz0R0JvDiSdY__rZKkOZcSwlrlIVulSR_iy5_nlJI3f_rdyAor2oD2XbKTMHbv5EyYL957ZJ2C4URUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8Q9x-X1ocaAGrfucGryw9Z9iKCWhjgoczF29K7FIP_iw81rxMSsdpiVIGYwL_cK13k_T-VP-nfCg4CxOuk_mtpjYThNc3E_irzjhTDtAOnGJ5m_V2rRizq0SCRXl_DEXXwksAzy16oqBJ7l3UfddlrNFZSZfoj66dE5WEi1uvK9OKKceaT3OwdF7zSGmxpdQLyOtOps7-9zFXBcnRUIIDKnaosD_eU4l-fsx77TbdbyquvnSecY-GxihViwCjOk5kXBFgKU01wvFjtQwwWJmP_mVO8-X8XuRMovFT_NUJ5UVKV769H-JhFu7ZGkIHU8i-yfJkcysEsStfc3nKm1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVtyjdpXy8ah93ARU9wkNkeKtNEJERLW1OnL_L7y5NhuwXNmrEfyNY9MYxKLrJ77FzBST0fO8_NMD3j7qsWllnTtbSClHl8yNEzdEbO_augjHVXYUBnqq69OHK7zG2N0rV2dyb7o8Vfl5MY9m5A1Y9Ffa-FMuzE_icnmZUuqgQc8odIgNB38L3f9fP4aQxYMvJ-U5PGgMQs9WjZaedZ8IBuPO0-V4_FvxVxot2S0s0VF89RHZQdUq3aXXlVQoGqcpZqwZu8f-MTuG8f1SmPU5hwfSGQNmeBnJ-v4FUu_2kl4RHpOztUC3Ju2uiz09UT_YJ2biACZcY7tvUYNeUrc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEJNLhMMdSWZNd5psvwvqDE7s_4XzHSkRTMp0D9jU3J_KAeG68v0953W3cxGXmFcALmm-imkUndjHznVnII9xRAawNT-sUQBOFPjzVq_cU9pSP4Les_2UcugoP2j9ZG_vAldI7vlhhVAFSwWtN5GyGoSQeuPN9bB3vHQR3hKFcbN0Ht2Q-_m4Cu1ZtMDGdQgWgHNRx5bJa-JqI0-P7iOqB-IHTqPeoMgbTfpnyna1s5FKWWH3YqvH6KBhDP0YOf5SNpShqqlJav6RckudJ1x8woDI3OYXRVYLqkdeAQiyXEv0qAN8NGE3OnU6kpcWQ4LS-02vf3IeDTvCHPkr8Yrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0_7vqsrMIchF_r_UKknPcI8RsjA3v6xbZu0zd0as1Z9aeYPmYtBKnsSUX9Md2gOJ0Yd7h_IFiPGWVl4jys2iKfsRFplKe2li_hjff9sn07SId-d4JJSEiD0IXAigaSigNrCxxq_WdqpcQ6Yrw_B_31m53plR9qIqid95WF3mLUx7UuMyIdx_xsLa1iG1qNlHdIGDVdBSqYBZ9FdmocHq_Tf7h6uJRHMuVeKmB0L0_ETIcOWSU1xx4_R37S5xT8WBkJzEG_FBjRoWMiWevhP-5FyLjl8cnj3zOYFoNNKHW2G4DLYGGSH2Oy2knwFtCzO2GYPtDictqXNYjQH_MeLkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS_owXC-9eNvMx-ZaDejx6bBG06AvMjqFMGAZn0BWN2L2_VVmvsNyF7T8DuG_w7L7UKwIbcRUO6CYOWhwiQlX1phvttQ0k7Stp4H1FMdckcf42bjiinQJfyuC0kVALzpu50Zmj_a8qyNuVpfskr0GILKBz-3Wd4LsrWsk2_sxAZxZVvEjjS4XFOZCY54I8ZnIsLkm__QZZ4-lpHJVmtT3UZLsXELrTV4u0-hAo6JZndogONhMaVkRGe5FhE2TKItI3LvDk5XgUIlrt9_4XA5jccp70gRoENxWLK68xy429Guo59pziS8xAoFcXWwuK1EaM3CguTWcExzSkwtnPb8LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4yZRYNriV38mIwqA4WYkEjDGBQcQm8wAvLk6rwrSZjEMqs9_wFqCpbm5B4TF620M-6YDez6YmydkAvnv1PUtuwz9Ij5TmL-6JykUweQFZmeaJyhdqvDNqH-_9agtb6xONxLxSUA3GjtR5Mqumqsr63ZKflsfWn31KCo4-jgLXUV_o2TNVh5G4BD3Oez39H4VND2t8At7S5V-QbG8orchqhGSWQr17QVJhO4Ky6t5rKBgEDb8Ed-7G2Bl5j3FLeysgLTL_cNednskhph_8EAfEEdWUL1XJqatRDvB8Gzt7HybTEGP6FeDriuxd6TwD5V98FT6sukbeNmyKJqNdkBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=vBhndaB0dMVZ_9wp9jmhgAdihWzSukzB7MBI4JTHW0CafOkC5NwMeMhERxXrdGz6jUQBqvD5bjPHJv0UW-H9N04__opqMGOhtRVyIuAzx8OcSqduoSHCRkoNpoVGzi83OQaUYKKU4axZKhIXLVXxn5y4ffVxjzOcisLgu9uDMakpQ4YR2nbOvlFQqj2AvFuOQym1Tzq8_X3GtfnB1ptPJ-MvH2Wl2oMsOu_SoL7wwoEq6piy3ggfO9llm8Cprq0noX-EDC2AR0PrRovVH30rNJM-zsAKd1K09aRTLjIdk-iOr8EGYgibdWTEtI0zkuNrjrfWPmG5qBcBiw2uqzN_cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=vBhndaB0dMVZ_9wp9jmhgAdihWzSukzB7MBI4JTHW0CafOkC5NwMeMhERxXrdGz6jUQBqvD5bjPHJv0UW-H9N04__opqMGOhtRVyIuAzx8OcSqduoSHCRkoNpoVGzi83OQaUYKKU4axZKhIXLVXxn5y4ffVxjzOcisLgu9uDMakpQ4YR2nbOvlFQqj2AvFuOQym1Tzq8_X3GtfnB1ptPJ-MvH2Wl2oMsOu_SoL7wwoEq6piy3ggfO9llm8Cprq0noX-EDC2AR0PrRovVH30rNJM-zsAKd1K09aRTLjIdk-iOr8EGYgibdWTEtI0zkuNrjrfWPmG5qBcBiw2uqzN_cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=v80oyfsDa01NaXFFT635Fd9Q-mXBKGShza2LyJnsJ4Oxutpn4Eiu9Y4uuFy9mioRpvWWnuJsH4egBcY8ZV8ZydmRHX-rKX1aphUFLacxqnAkihGshpM66gyD6xQ49-0rouTxExoQdFkfJ-SH__vwgR6_ard648ZDBExQDu8d0zFP07Y1_XW5CcIqqAHvjNo1ednJqNvLLwG3UxNaYehnOwnfV74nqaPha65QCfe26MKoj_CyeRgW2Q5no0HVs9P-AK-5PFzgp8vbuAhvkSxxaLkzrksI3brrtomt1Wm-GuBeFjhGBoFkPS5l1sutMb3RwXT09Q7fVZs0tx6SLm_qOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=v80oyfsDa01NaXFFT635Fd9Q-mXBKGShza2LyJnsJ4Oxutpn4Eiu9Y4uuFy9mioRpvWWnuJsH4egBcY8ZV8ZydmRHX-rKX1aphUFLacxqnAkihGshpM66gyD6xQ49-0rouTxExoQdFkfJ-SH__vwgR6_ard648ZDBExQDu8d0zFP07Y1_XW5CcIqqAHvjNo1ednJqNvLLwG3UxNaYehnOwnfV74nqaPha65QCfe26MKoj_CyeRgW2Q5no0HVs9P-AK-5PFzgp8vbuAhvkSxxaLkzrksI3brrtomt1Wm-GuBeFjhGBoFkPS5l1sutMb3RwXT09Q7fVZs0tx6SLm_qOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_cRfh1rgpPmWvyHxpn3-qSY1DLYKy66GKBnBaeQHbM2nATafb78L18wEbDvP2UaUxuY0uTOd_w2mDfA0c51HK_AJChooVGccmN2cSTrGLYPd7PEqt3jGoBwN6-2QioYF9r_8iSxg-wJWaFUhyfUfmdjh5A61CmW9C2xNSHUHkwMS086qaQm0F2Fp87bdDRx4UuVnZ1n7KLgq47Q8c92HKxqqlDMsXIj8TyxMme0n5VxvBl2kQ3ka23xWzZcndBfutbdJ90x9FINiXDWFfERzdPNfoOxx4V6Ol6HY2LurxSHZId4WldiSXyjj_gfL_GjbnzYyCuOJhZp2gA7Wb7ECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5ajPCRiMzp4Mqxc-CP6ZpfrPJdczh73ymmd9GRqbxx_eNBnE7y0vzWZR9gVUmeGrl1dk4zREQjfjchxYBez-y9Yu-6zSktwwWfb_W7XSAw6ER3ec0dL9nvmPtyxa0wa8zFjnKTXLtMOGcvbNGuF4PAGrztRvIy5jbhwoiYZ2iebdP0R-MY8XTwhwqBN069KmLdh07SXlmMVMinnKBcmJWVf67IvaDs6IOSuMRiT4EAi4JQFlIEU1souKPPB2NzwX9xau2XZGguw8BuLguRQNS1AwmitBzfXTe24f581VMpWZYJ4K3nv0SzDchksHYoGuh2zWInyCd60lYgJNXnzvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOiPRfldY026SPbpazKSYgMnt1_0gtVfLiLHHSGwLmhwEMFM2KEybt9z7OJ2UGr2GKLLzNz7ELy2QdjJpK6SjpcM2dIg4n_nc9hZXaeeZOeqMCpADtWKOvNwBawZ_oz5vtKS477hJ-W0FAO6GpR5tHcMHhVLxJdy5JKBd1vok3QDPJET9lSsnqCNq2O9XeaHSAUuRHxMYFq3I4LTNecNifzp8Nur4iglqnbj3lUfcuMMG1stPQAChOP36JMohAQX2d0xEr1drUWDS1Upe6ydcS0ot_lXp8viU2RsTcTOG8FA1rgZZ7Kq5LXnwvP4IG7jzN_EQIKbyayBWiqx31eR3g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=e1NXPtd-U7Bhjit6X0JqzL9AoqU2u51lHZZbl4CpWQoCDPQCcdCg6_uvYSaKa879g65X8B8yu8BTB-vMCCxNbxCZ4tdSZE_IdWe_Wie1Kh_WMhjo7THaI5hKWz2w5jMMEaG_PYPgWAnTY6RRJdIv7RJal6OOfjCjw-m3zMS7Q6jWMFWdgxha8PuXBVg_531EjpNt5Djw_rCUNWmZqx4vEavQpHtd5q_4AiJ09YSgO_UvjgGWBnTBINft4hMGJQ2i3HAXu2dn4omdAGRiENqWCYe4rqEa8t-UUAg6IgILZ5cfaUeMkS5aresBqC0GZtK7HO4EJ7BRmHbXnYpl1vd-gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=e1NXPtd-U7Bhjit6X0JqzL9AoqU2u51lHZZbl4CpWQoCDPQCcdCg6_uvYSaKa879g65X8B8yu8BTB-vMCCxNbxCZ4tdSZE_IdWe_Wie1Kh_WMhjo7THaI5hKWz2w5jMMEaG_PYPgWAnTY6RRJdIv7RJal6OOfjCjw-m3zMS7Q6jWMFWdgxha8PuXBVg_531EjpNt5Djw_rCUNWmZqx4vEavQpHtd5q_4AiJ09YSgO_UvjgGWBnTBINft4hMGJQ2i3HAXu2dn4omdAGRiENqWCYe4rqEa8t-UUAg6IgILZ5cfaUeMkS5aresBqC0GZtK7HO4EJ7BRmHbXnYpl1vd-gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsBUtszWcwG9KxfbL4wnnVoP35_hfKbEBecHgpnvUfUWA2XL5K-8wxGWaunydXzQfUJy1x6hjn_1dq3URRckT0pH7rqpKSe6k5gCqkWk_vDGf1V7sOzpjttDzmMBw6VevLJM0qDauvdgymLhy6mCdEWC_gTs_J6pOU1reqaFM270xZyjtSp4pyVxu-B6qJPwsshKxvuRXdILOhfQdyAH6H7lOaWmhVeIUn4kema75aaYvTJOwjZ3skoSZiEgJbPqzcXwTP9luU67FBm0XQrcrtIHQjdqCV6IeN4ccKMBdz0bEO-rY5aAi6ynz45SmkDsNsT7-EUdjJDnegvKE1lOLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW5_eJcWHS6wXixZiEz0huYUvVkCYQNk7jZ76jFVJ8CwcBF-NxRlLVpdTUmcDQK8D8Qp1piLQ1N_wAQSiQ-PFsz1AIsbNKTKHUc6VnRJ5mt96Hp_xGjbHbyUyu6iIKwJbc1TOQXUXk9Artz2GaQRpeZSKum5zVQuInACrosBuiNE01REwR5OhCrxCBLWTnWT76DfgSTvhZirvjdC0MpbhF7rIH60vI5Ghr16e8CR-4Ln4X4s9TMvSUf1W7Ri9mTHb6bScIxQduVJ74AdWCgQ7sxpuJl4vvrExw_3qeHZvq2_oXGasNrBS-bJTDkAguzQyHIzTjgVRHarTNR8YWgivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZNAgffBo1FrAUVP37T-pYaF0K2ACqii3p-J8gR572nO1aaKEwD1-vxUng7yncKTBeyRyb2drf2REjwBFTsCzqVI0iBspRjo3pipbqamxmD2O3xSHS3WGgFloG2uMOxiXE97bUlV52AkqyKcX01Mv2TYrDPpLJt_UH33ykofrnXZb2meFNOyjpmTAteDZWnCreWWXK6o3ZpGKxYxOxQjcWHyRp_-kW71QV-iJNBwbERJjzXQID91xOJiCA57RyhzEOOqW1phpb3RqGVpNES2iy5gCCeL4M8G-DxNGE3qFR126rc7k1vWsA75BWyymYQE2FpfxCLHvrsl92Fl4WUwCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udof-U9x8ZeRECmkiVM6QzfwPLpDeekJlDkJwZBgaORM5VhHticq8wmOnhX_tYToYFF1M9urpTJRV8UYMEsGnpogIMWVTNrbxzF2F4yU0PFcQ74myPWHrOcmGmDB1iX3GX3A-svZwXeA86sJHqoD0BHTI-SA3No5Yt55F0ZI8J3hiBdi155rpghZpy3QLgw5UKlqIYmLKbtA368c4YgnIYnYK1_tYHASWEce03T9fJ5wcRwpQXH8yyF2rlaqVAnTjiro7RfedDdxVvI4QlTCNp7GY1c7YOxhEMRAs9W2FvL5mD1T_q7uOlHfNPck52gsaPIYcYqrxilo347ZpFqj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0m0sKYYKeZzfqyMAoLG4cKJKMquuCJ91gMrVa7X484uwGQzZalsmBSgx8ouvx1ofGfLFEsdNIK97gjDbOOHVFiJ0LJv0qYSEhMQ5BXj_-woEdwax37aFRZWszVw4WlTxkp945E6pEaU3ATrKEb_xadYvvCGp8nsBFT_8RpF9hZpZpMRdrAKrXlj_szXYufPXFXNQ0FiJkR1hRWFCVMCpDYAztSHceBFpHxv2JW-njFi2zrKf7JQCxL3AWWXfA3zyO7sY5Xvnce69L1NoZQW9jz2pB2C3CRSRbr3kctBlCY2LZuXuW9RGi0RrCSTNcPH4nGDTLAcOgX18fVQPVbZCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUifIVYnLcmhgrJ1aRi0z9SlLjzFOsM0gQcRYAtg_VdgzjEMH0ZSkTNfnQ7l8SjD-wIaME-JHSvXFpT7Bxtdli5umPQ5xZBXoRu18EEdvyn-6SZsoWLppUjKilZrOcVhWrrNFgVoiNBHWKKsyXnsmbnvMEVT7L_f_JjjBICOO178LKt92p0ijdQS7Qt0G35tA6oAoyZ6tQvNKLsQeokkANWmbNi4baSktIokIRNgTIkFlnOYLxmOF4m4YWrwog_Vopv1h8APjsZSNWxFSUymfB1vLcgY5mdDj6cxeUphIr53SrkZbKgAREX4xemtzhn28i0qBOTVp979wYONVoHiag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAcCr-NRtSfXT_DGmD2WI2cWEd40ydmAVwUKB-aTpo2xHwGrE6o9ANa9fWkwIqDiJwplbDM8k-gYrZP0100q7VRi8fo0xaoW40cFAFvK3GaNF_o_KCYJaOUz9n7ENK7clyjCs8jSzXZtf-6i1uY0G7Y6hfTcUtWKPKjfxRqTkTsYyCcNZIXtEaBAvDsNz8l5EmF5mRHhDXMrTuKVKk7bQq0e0cP0MaSBnDZ1xV1OoDSsPCgVKOJVnX_nJfbRecP4Q4p3Xx1-QMh8PhdaPch2RMugY7C74UdfCBE3m_IHL0q5OT1Co_egQNj-CAvnhtUpde8vO9k2DKX4beK5HTdTlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dRGBzTFh2yi2ifHNwCPHNbbAe7U_ru2gpJ9czEkpMO9-nxyFiikeFoPMV8-vXTEDp2noFzd6_GjesUhNnFvoVlyXkpz3medVlaV5bocD94FxBOu_D3Sxt5VUgYb3InSN8ielLF25ISXrqKQmNtj7t-gXcIVoEubmycjCRhZP_wBLf_M-MVFllN_xCLwudP3PRIiXkWX_anrF5r0ptFT0BtOibkIkdEHSkbNit40tFOTE-bKTsMjetAoqwngcP_jyHA4hwAiaCUQQnic3c3QojFi7M4miZ24dMi8OMMDkdxwnmFjKB1HcLXD80OwceM_1mVAo9abxXH6zWcILOr7lUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvIZi7t7cX9EpjrtolIF-2X28R5HwgnxL5aSuTkAo6h5gi16Wex0N1Q9frbWyKuLX925-8ms-KEyzFOUYQfwuhucLEv1-Rsyqu-epXi9l0P6aWk2eDVDcH1TCHDaqmhgxWoWYVoe401rU9Wy15_QtBfxsqKrqutakwC8FCSJRs2aycGrnMhx8y1CP6q4TULwbUT-O37r6JfYlh0Flkg6RtOe8hbn6hwOc7V6pp6qgOd0J00gXGsproh2qWP9sfYECv_ODQGNZTQk0_Gz5Q0mHq4qrenY3FnaU3foZRGzNRzNhppc67VNWpTra3b5gLHq7L5IHVMVwUtsjez0dqjcWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=IgOt2PnDn0osyXNy48Ue70r0ss8Uoy-Z60KWvYxzk-uQyffSBirgHnQTVYu2D9vkV_XR9ZfptIBiGPhUthU7o9FMHfkvqKLoT06pCm8RexDvZBOXrM48m936v-pbZG8iPxyAPQIV63644S9ezGu9kG7GYukHhUkyGA63HEtm3QMxLED083ER5O7-rqL3z_6A_FhLWlUWjoQu_tpS59E3OvD6kCaPfTcIpbDCuZgpIOq-mpB3TG1EJzodgL0u7Z3I3nqBflniXruJ4akTU3LxT0JGK5lJmfaXzn1Z7hAqs957-UyRgTb6YwH1QMc9q44Ukra6hDtaJfoVLpYJPKhZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=IgOt2PnDn0osyXNy48Ue70r0ss8Uoy-Z60KWvYxzk-uQyffSBirgHnQTVYu2D9vkV_XR9ZfptIBiGPhUthU7o9FMHfkvqKLoT06pCm8RexDvZBOXrM48m936v-pbZG8iPxyAPQIV63644S9ezGu9kG7GYukHhUkyGA63HEtm3QMxLED083ER5O7-rqL3z_6A_FhLWlUWjoQu_tpS59E3OvD6kCaPfTcIpbDCuZgpIOq-mpB3TG1EJzodgL0u7Z3I3nqBflniXruJ4akTU3LxT0JGK5lJmfaXzn1Z7hAqs957-UyRgTb6YwH1QMc9q44Ukra6hDtaJfoVLpYJPKhZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=CLeJD3I4l7kOMsXa2gL0SwyiMQZJ56uqY49si_pvGcJOoxPjuda98aDzlM4uEOD0CV63YE8069Vlq3OlSRYAldS_5yBVa40hDG5Goi1kwOw-PBOmpLAmq_YWJlDaYijpJ2lYSESYSj8vwGnWYY8UtXeBJP6O9sNtIUc1gxmTCJBQ1_l3aluIjLy0qYaHW4hvY2WspOyYOSPR4uqoxPfRIpK3AANKbJvBUFHu3PliBtVYVK_8q0EYX1wohEuzzGo4r4KPd4P0z5VdfbcJtdyHWt2cL4VL52R9OdXJO4Pxb6x0Aji-KyOFQPBE7kTcXOeJFPZWDDMVhvJgelqGgoNXsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=CLeJD3I4l7kOMsXa2gL0SwyiMQZJ56uqY49si_pvGcJOoxPjuda98aDzlM4uEOD0CV63YE8069Vlq3OlSRYAldS_5yBVa40hDG5Goi1kwOw-PBOmpLAmq_YWJlDaYijpJ2lYSESYSj8vwGnWYY8UtXeBJP6O9sNtIUc1gxmTCJBQ1_l3aluIjLy0qYaHW4hvY2WspOyYOSPR4uqoxPfRIpK3AANKbJvBUFHu3PliBtVYVK_8q0EYX1wohEuzzGo4r4KPd4P0z5VdfbcJtdyHWt2cL4VL52R9OdXJO4Pxb6x0Aji-KyOFQPBE7kTcXOeJFPZWDDMVhvJgelqGgoNXsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=Mhr4C3A41_M42vQyYMyqo8pzBlgPZb73ME9S7SbLT5maK_InIvMNvm2khTVm_LnP-hRE8ethfdNUvo807aS3JMHmQTEQ92aGDfVXmxzbuJKdiDjp_TffZIvEci-Zfe5PJpqWJfR_Uk2LCxKn_pXxeBDQkYM1G74ls6Y0BCpncdQ7Kj1ZwAolQTE-xSbUIbrPnh7D_u884Y8e_eYmnd4UCGGlWFzHEK-YiZ_P8v_KB5HLs1BsIXnf0L-CLdbuaE1QEtj2bBQAjWUb5_G5jFNl-DJjOBU4B5ACyV4PBBFCBQqXgHByMRr2sVWbHQh9d2pyQhJ_4grUL0-e868jIhym-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=Mhr4C3A41_M42vQyYMyqo8pzBlgPZb73ME9S7SbLT5maK_InIvMNvm2khTVm_LnP-hRE8ethfdNUvo807aS3JMHmQTEQ92aGDfVXmxzbuJKdiDjp_TffZIvEci-Zfe5PJpqWJfR_Uk2LCxKn_pXxeBDQkYM1G74ls6Y0BCpncdQ7Kj1ZwAolQTE-xSbUIbrPnh7D_u884Y8e_eYmnd4UCGGlWFzHEK-YiZ_P8v_KB5HLs1BsIXnf0L-CLdbuaE1QEtj2bBQAjWUb5_G5jFNl-DJjOBU4B5ACyV4PBBFCBQqXgHByMRr2sVWbHQh9d2pyQhJ_4grUL0-e868jIhym-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXd0RrX3Pf5iPFk82u9cKNQ0s2exOG0NjS_BT4YrF6KHwM1YZztSMsUDkdO4ogeUIyG6t9t-hw5MICejGjK2P-7fWDecDY8RAogHS88xt1lGg9S08sbGBjZVpz1YWQwv7Ytv-YUex9SPeC21aSfn8USoXhU2HXWPSlnJEPPbTvBvxVxHtD7rfJLq3-RGeEV9XO62I7zk0fS0fw7Ds62hQk_gNW08E0CzdKoOTIDTsYH2vT_gdF-GHO29sMyqg5cB8e0qYQOqi91Xp_EaPlyLZBn5ZvToh4k0NCOfmc3V33eg6cib6jVeDMNam71qsRH8wZX64flwtcSCnz8QpM_45w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=b6Moe89_HlL6OVokX9dKO62DXpucrGukaKf42hLdaH9IP3FauK3s7pgS4wWTHMJlznzYVd1ikRf-gldq60dP1L3cZ3L8qXlVIx0T7UQwLNTkSp_9-Ap4hAXXwLVfbvbcTjo0WRLoXhrFzvcnarmCrSbpgQ3dOSRZYQj7GpGzIQlLJElcsEe8tDL15AtGxYSkIhXIJRj6Dt1DdsR-apR9BGMG6f-PqBB-1Rd2Bj-hy2WRyIUWXZVxwoHEmSYUdXDkCnDw8dRLJT-nsNvERkxrpwQhjLzVD7RQiwZ0hgsMqphtGyXyEcr2HMxFf68ddMi_gS05i-xhlYSAaPQhSJCodw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=b6Moe89_HlL6OVokX9dKO62DXpucrGukaKf42hLdaH9IP3FauK3s7pgS4wWTHMJlznzYVd1ikRf-gldq60dP1L3cZ3L8qXlVIx0T7UQwLNTkSp_9-Ap4hAXXwLVfbvbcTjo0WRLoXhrFzvcnarmCrSbpgQ3dOSRZYQj7GpGzIQlLJElcsEe8tDL15AtGxYSkIhXIJRj6Dt1DdsR-apR9BGMG6f-PqBB-1Rd2Bj-hy2WRyIUWXZVxwoHEmSYUdXDkCnDw8dRLJT-nsNvERkxrpwQhjLzVD7RQiwZ0hgsMqphtGyXyEcr2HMxFf68ddMi_gS05i-xhlYSAaPQhSJCodw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=vPZbRJHQwTt-EzON5Y4n8CyIOCRvyOP_mnq1y3eMYtefwn5kKpuHRyUTC7ICHnZpQ3MVR3dVEyLScSe6I2AtRdR_QiFnD2HsI7iWVW1rMJ9gpWzwTud7nhdWV5AdrNttSrYphy3L_hF1luKMH8zRV-87Zh4LIR1tUDSFD3hx1mDPEp4gXsTJeojVqUbacKIaoIgsbiEXxLaCMqObtwr1Y9mC7fXW_oYQusdPaT8zlxhvmQxiS0UtFkTYEeAUCdbAjUWBoTgKQPxniZry462lJZs_-xntrosLltl5pFgnh0F33c9CejGvzacySG8_rPvC8_G3sm4XnciF91C62m0biA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=vPZbRJHQwTt-EzON5Y4n8CyIOCRvyOP_mnq1y3eMYtefwn5kKpuHRyUTC7ICHnZpQ3MVR3dVEyLScSe6I2AtRdR_QiFnD2HsI7iWVW1rMJ9gpWzwTud7nhdWV5AdrNttSrYphy3L_hF1luKMH8zRV-87Zh4LIR1tUDSFD3hx1mDPEp4gXsTJeojVqUbacKIaoIgsbiEXxLaCMqObtwr1Y9mC7fXW_oYQusdPaT8zlxhvmQxiS0UtFkTYEeAUCdbAjUWBoTgKQPxniZry462lJZs_-xntrosLltl5pFgnh0F33c9CejGvzacySG8_rPvC8_G3sm4XnciF91C62m0biA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h18b2F3nUOF__oGqXO0Zmr_9lV5YhT9BGBT7xtt11fEvinrbpWRe4gEWB01FjLEase_Mty3zgOcOT_GSQp0BqiY30sd01LWg_RF17iWq_PEXPefxP4VYvY5sANyZR1Le6uxqo_J2oVZ4X7IS0z6XWHZyzDP7e0S2zHVnmaGZzZM_oMNLJOGG-N3fPIf_8wH_JqIqnC-K7HSLRUM6uvalQ3_fyJ56R9NC3T-g32gjjD2NU1VOnuqWyKwxZ8h3CSmjcmTUylOvLJx9Ynr7DRu7yfvCRVwDEORT9cnp_BDu0gr1tVI7m68-ziDoIyo-SK1oKjYpkI607T9SXstTi6Cckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLlacvLRgBMl4uGuEPSwcGDXaWLh_4CIwCagPOkVbpSYDF0z2SHo8fwZPVmlX1J8swa7Wuy2j57Ij6yiZ0cxbvrP2i1vumkfdGcPYoFqy8lqdtxGJyspCwiGvhGYr_jb8s7LFky6Rr9ZN77bIZ-QZFOoSA5bX_7KuRIZabWQ98_Z5QeMjjqPD-0iLCZ42TDTFmjoXoEXgv0ZS2RG-dExAGQMXSWo8PY3OWVPSqM67qGAdMAcFJg-XcmI0-ZKvQPM5GhZuo03nimamFGGP9k4vj73q7qFs_6KYCI9vk_xU8W5kmFYx2CWl74R_cCcW7JM5xDslVaYdlCuF8DcgijLkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNiW1f3Z3cLzVXv9anoD0ANAUVz7spMBcXrF3tMhyllCk-btQ0khyJOWWuNICFjKCblMEeagjDxvQTB1Qgj2-Cfx6nf0wgvlEkmksJP91zJpv49hZDMmoYwgMO8jfVFJ2P-rmRE5MET1dNKEVug8uVX7xdS1-ibNYuEj4R5DIy3CMC89Hn6PAG5m5Sggjqs-HjpYdViF4B59tuzK-MkdAHTt5LP8ve2uVw0aJqLStRTxCKPLeSoFIyQdL1PYFV1SU9Suq7YOxDUVScAdZlTxit7Vjmeoi0o7x9amX7X38hgtCmWUgTNJff4k502V-Qy7up8wjf3I2UEc_35la9kjIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bsZ2AgnZ9plILdAiaoaxgyr5FvwCUHoUmae4hRkGI9XCNXWtaiXmA9p_LrrnTVmYvwpDlL0UrJl-5FWBqjQxjRXf7Qwq4imJyr6Iw-HsfmlxBuJy5yU04ZvWUO2yU7lw39yXS1wgPxwXy0wa-MjJ5AMyk8oDXMyID7bTblE6g1nGnuenXqMDaTGQYe9AkH81cMWFI3JIQWmNt2c8bIM__zJwBGrZYoXpVNa88PwEyDX4dmHLtqvimQHeh0BzueusY6XND95XQ6m7zGaJN-jkaYs4ppbZxyni85I0G9_U9Y9nRCSliSvhNRJzl5d1-zAFepWmqulgy0t2IdJkgueXOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GtuRHGiq1an9o_pzEWUIluS19So9kyfQRVQOgrYJNpACVhuZ1DPFopRSCFu-Fz-VQDtI6Yo5CIp_eDFDDanXwD_K4W-If5nF9cwUbzqPuppBHmJYu5TDuIj63sZKJNRyxCC-qU-3LsA-fOdchP8NvbkBXn8MLzIF22bs8eGKnTo3DeDlqglld0nmCu7bEXEg18WCMnKacMuM7sznnV0S8EvwOlH1QKIogE0ezhl6KJMLcWMI210IomwCF7esZPArPLsLnFQO0aUGRHT-gtnKQqMRTsG985ErBUsE2djh9NAUG53ezcVKOP59Xp3ZNbfHXmIC5puHedq2yf1bLF3GrA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=jzhRbLgbhIjB5rOpCADj2j4nHgbD46kX71Jc2VrIKnAmG-A2g4VsBFre6l2qgsBBIPjjVPjWtC8lAwlZmqx0OTnCNKInqgBHZjlnTwrBhHsAwYChpobu3xZcj9Rj6c6m5cqAA1pClDL7vx-_Pxm9AcH8fsBGyDDbT4XnorYOhw67xhrutgcQedwutM6PwMllTpqIJLuoM2cjLHE4Ssyq6tNz7KWJtTQuGoWgg6SilACI_vvQyHBNuEu10FcS5psUlHB44JSUBbqgEbR9Q0GccKXZEnx8CwumOlzVFMfkRCieDhRgWdT1hpMDj_XkQZbf5pyuz60sSiDpebG_ejMClQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=jzhRbLgbhIjB5rOpCADj2j4nHgbD46kX71Jc2VrIKnAmG-A2g4VsBFre6l2qgsBBIPjjVPjWtC8lAwlZmqx0OTnCNKInqgBHZjlnTwrBhHsAwYChpobu3xZcj9Rj6c6m5cqAA1pClDL7vx-_Pxm9AcH8fsBGyDDbT4XnorYOhw67xhrutgcQedwutM6PwMllTpqIJLuoM2cjLHE4Ssyq6tNz7KWJtTQuGoWgg6SilACI_vvQyHBNuEu10FcS5psUlHB44JSUBbqgEbR9Q0GccKXZEnx8CwumOlzVFMfkRCieDhRgWdT1hpMDj_XkQZbf5pyuz60sSiDpebG_ejMClQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7smfdKEqHtuU6aZ_Tk3c-jtpI2wIPT-l5Sg_gqT8R17dXeJwwLqqQCCLGNsSA_VUD1EC2ugzdcZc3inKDox693Jlc_84uDpTw80Z29JtcfkcvHMO-wPolbpbXvc54nlcVD5rJG5uKpooKnY33lcAnd71FEL8T83AImvv_zEMoEHfjy-tK5aEIdBcPwfkdmSYeGPf7EXv14q7WD1_KqJ2PvWxmjJmblKXc01pL4AAEYye0NjnSjQu8vGe3tNM935qhd4q66ZJdJJDs9o2ft1CxzMTBJ6iyvBzNnm4S4AANF2IWmLbPXryiOg2gFbB6wYTTPvUdlanaj0axXJEqpjQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoRT_tEMPuiQ30q4TeNXXNVnxZJ8JqnPn3KL3eISVOTtgXqcnIQUYD-OSIg-L5eKXsAJ4WVBNvf_BzSHjiHtg7HJTFGUFUzjdyRxeEM9pwjOMWkk4qDEu30pwLPWSoBVl0-CWXLeWBZqMNhz0bDFSMOTGKRqSCzl8zWdtRlD1hd9o2aq7QUfOGGwhDVsMWolLaCWZmtfwC2N30ivCw37HnAkaIkgWFx2V2vCBRtFiihy3-5-sC8kf_v_eyF3X89BZk_sElIoLd9HMDWlhAAxdy4Op2bh-RVRiPkZ5_11NG26UCCniJcH1_xBt_Wkx5gBYLmdnEGWfmRHVdivCqABNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLv0uRb1evcNv8-XKGaBH26bGcoof6NWExOZ0CxD-Z1Vr5qX19NbX4WGONEuwn551peS3a-1Tmgoy1hl6JExEF79QIgDgvsoJVjcfFYgUX3YTQ-Mrzb1bTrMOTFVycq3Heyz_waFPkD9BP2fK8j8NiqiSDP4_FJm-z937ek_UnX5DcWRrA9FWyCeyOH0As4E-EjL27MPG5bJWrcIbmEVpvF316dQw3pJcy5df7cMmA5PBDZKseib9lA5H7Ze2fJ8sTB_DQQbsyqB6HyHqUpBpUypaqUvoqgJQxdlTRhibRSORMHEstYVgiUFvpz3KZ-FHe7X-80HH9w-QBQL4k_bFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMYlHIo8mL-ClAvkb54LTfrhervvcwcp_DqgW0vYgsmHXPKc0fj8OIH3l0gbQ9skF6MW88DQaSh4PPyE2j3sKpYKp_D30IO6cxd6OrAuRXn4iQ8Dj5yo4YnxqKHzeWlNbF-BBqbtbwW8s3khrXwtOK5DEiYBv6S7_t-neytotjzTsHub-8qysj7hhDlNkzQf_2ugUj_cUTwrzSle3myhs9LzEVb6oFyXcfiSZMBO4H3PoebmDXkgZLWUTiiBBhbGIIROKFvNWsGCCyXuBKLstmRU4ucn2yfn6TV_xzbtyGkQU4UAHYZVPP6ZeMUlfMo2-C1hybH7LypHxZgttMaeww.jpg" alt="photo" loading="lazy"/></div>
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
