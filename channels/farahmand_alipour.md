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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 03:12:00</div>
<hr>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2eq_AYHEmyGM-t_GYmfSql95uMhnBXd6eA8lfjmuRJ0S9IpYaJrKnsDF8Qb_P_DlU24goPy54oLm0mYmRRs2WhHRlc1r2-jzbpNLdeDRER1DPFgeKLrrqq9NhLt8V14Cxyjh5ZQ3Xf_rt1Qjy329fgY04VTxPaG397JLoKxc6uY0NK0dogN_CRyckU-m2p-3xHbF9WxAN5FgFnxMLsoDxTtijscmPEYhieyhtogDpdvbZv5pYH1R_n-ka7oaC2mXVSv6BdxH8F2np1_AO14syTt53AjZ5QxjxIVRscqJ-DZxcVYZW1yw4t7Ro2I9Nmz8rfmyZiXJzFEwMPpuX2lbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0qrPiYNKc01fZhSOtfSMkRAL1mDOFMCQ2oVoBujjzyAoaP7jkEnptWTHfga2NSFlUC5Sb5_gkkOEt_Syur11gZm05895M0VsSzzKAuV8UGa_VWQeAGUbx9pW8VJy1r0mmi0PiF3BDlnnEFHJB5iDpVIRXJyhoeHtuDOOVk0sUe7bVaP8dbOZkE9T_dK7_HSOtR_5xZReUUvKW9glgqIJ0lNUhg4zDmwOKM3-Ad8PGpG3k7sK6SnGDZUKyFxXTCDQ3mpjSuJcsRHEj38TjpsnO6H4q3131S0-BbzIqkfWkyDbr_cgZAENSyF61tTqa6Vg09xMDVc7S5z0ANYI4peNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDV4NmIBTU8-gdY0RKnCAzvjiXx28oJBnnip31C4OiSDTTEwOUNGVexRZD9_QG5jkK45saUvQEi4rOHQPQtVQpNJUQkx59kMKMpcZicz2pB4m623MpjDFgcWjdVId443VWo4UH8eL8Cf1VerINlh52dajLa1kR1ebc-4sCifnv4iEWiIR1ubjmIEi2a8UGqhL68chcldMMCahxPjqoC5K0CRmuJ57gHCAtedacevPwVZcp8CP_qu79tkxeDj9gjh3GSHkelKkgvjPH2Qhs496S61ikIh5yMCfCspk-6AfP9rw59F_YqTu4tdJanyY2BDMbONHNHo-hGpKMvUrfVJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBDF1oewFHdmY2bFPLROZ5Pft52CwEgHQo2KELE6Vwtqrhcg3BTSMR2_ALLPsS-wVmiNWyC_CkhSOmiz-aRtiPaGc3CcrkS1XTxBUYm_3OJ10dUESlgqHH0lNwzrA-OlaEDXwI0Vo9aYnl8b1l8-QuzGDkcLl5LKo92486sWubBx0EiFFe999esXmWyBOssB6YwabMV5TqhXgYbeBazMVeCGbs34V9JtyI8i_U0wjdNnsoKomQY2X41p5rP7TPNFnwlXQeXDs85eIeb7scpDn0a3Ms4jF5BYEJyt7VY1zb7qedcvxMkP00LqTJUV-gw2BXamUgwiyIM4Oqp2BdvXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cla1X7EnM2vgYNXhxoVWftOTnxDfTYErL_0E1bMH8h9L8UFktuPk0NqRhpeLhil5WJs9X65s5MhqGNxSdI8AkBaqLSzO0bS5v1ZlONehPl4Tm-qypaag7lKEciOMC2xKybRkbk8jTMyJpgnfJEtyu2AoyY-9nto8cz5Hx5Rrtv6rjnhN7_pafDkNcKS2GDpoJoE66QxBBld8l2B3VP900rabW69D1TvR1ynnTTpE_QhtLEQW09ZSWWna1JeQcngiFr8RPhVr9t4WWBMRP0gNtknRQrbilat9DzaQ1tu2QlpLL1UM9JTyKXlCO3uV-xb8vadK91_EYzPG0nkXeZ_MOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPKvEK4cjB6ur_6M9aekCBckrcJ22cHU0PmxM2_oifuYkZvOO7ZaIS98rswfm32qunX-rJonYvMgzsqR2IYxjY4nlWkV6_9aCf7lgl4HjwYhrW18T1VKqD8gQkCY7HhBFoQY7RxTN3PCnjOv0HsnRm-RRQ0wWnXwmsv3cMqbx40TicEgPU6O4FGgWXd8E9nmurKd52rZuTRBQWwm1AehZx6DG1pWuzNYKSGZOD9Hj1wihTVXJU7tUkd_l_eMoTcvUxuimTr9CxP1iHnjjgqpFXqto15vOayksNBX7uUcYY_azMtDmhTj8H_Z4blf8Lcxq5B_rZXthAJ96vmUH3ndog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7HI9uK1YjtkrwjXjriEZ9Mf78i3aug9DRxVxLzsw-GFEL8uVNypFJB_g2SAbbxkXEqA3ltCh5ztafiTIdX4ErvFUOGshSYDwwxgQ6jDk-iVK9qjq0xg0f-eeP9lC6WR_Sh_VgtP-9COjyi0vBh6bp7rur4eZSmvMJY1g7fiW0D51UDHAtWBC2E8yv-zdkOY55DPlv0vsV1VFHTfxnwMmJpTt1eF1mzEzt0A7Fs5S2ijC2eY5ZL1YHwkTEiXpEJqwU6mFwiOFVtLjOzjT9iwi-CFKi2mVRTAP5hr--TGIrXkaCsfPvJEk61Scut339kWtnmWcQ6qB9XQA6wmOTksSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StdbKNy2NYED09oUAj1exNe3bpmDbOQN8a2r_G_HYG14Q67H9sCdm2biYTTo_9AmCa5BRw-u__I0xuSYEB9pY1JZtQ0mx-8KXQcOBEjNFZzambSVsKCNsjZwhcyqh8U7K79OxOpppgMBLYJGXAjs6h-qqVr23USPmWpJmiRK8fsrRx5WkndKhiSnPwjj0PM3Ojusq2iXwoHwcED9ulmEj5S9XfwxhDL-QqMAFqDz6Z86OEw7wx0bcjpC6D8GUc_8rbMYZ4eISZC8p3u0ex6tYtXmecJHWT4vzxAFMhQA3lMbvhTMezgccWAnThOOemmp1A0B_69IawIPEH3spN0i-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0YdZm_XlwtWGvjqLSxs7OoJSB3FiMlFyB4cL33Sy9hkqCa_5UDWq6b3KG8doeaVdlX3vJl6LKyW1n7oi4TYsPA4-7KzeKgAMYDcoMaU0pWP-vjrUxgUTH4oobMYAuwIo4jreQ_NqjOF9XgpGqKn6NJBHQYQCNA00Z3iI8fIduKta1rilw_pWyWvhyG0kMG9LfHWTT1ma8cIUEui_gajpbKwTrKjjCe7X6z8_zMobOlIH5lwqYOitCKrnnmMl2UNCzA3EJwuFqDsenFeakJi80yBa-I3CYLLTdrhTEEbOAut3uy4ziR7sUbkvnKPHiwPHeDYTcxxO7OrfnsrMBENog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F972b6kBBj53eXauYVRPdxzlZ9gdbhHJrVqtCufF2KqpS0hnBLOkB6tlhY3in-2E2tokB1pv1EElp4tD6zR_CkJXnqrl1HMfyRfucPVsuxzIhevWXbDtflVbCX49VMlg1tKnIHYxjNHvCXxWtM7SEJebAe4Ljw38VUFRb4HBaONUUPkkF09bIQggiSgpKpG_v0IUNVIMeF2RCdqYwF0GLFx-cFtB55p0kz2d6QPpzn2Wf4Dt4iwvuePdOlMBgzbFzMOzuMu_YwLZ0eJ15JRtLEBjVTmMUyrCKYIihsyc_PzLXjm5nWqULOVZePX0-ms22OMZhb7mFJeHEd9gVXTj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKsmgb4ODl2tmkzv28gydcdrx3Fw6eHXwre0gXTDruGnAjpkO_lyWDVZTjb74N6a5VqUUeVu5L8-8rlpPZi9OchPtnbpu_NCZNrMnfvGrnQeFhMuTUwOKdchpf8E0Mcp45u-LQGY7RvqJRs299G1w4lnAXTXfLMhGbKWuWQuTUxOXbsMTLf3145PRlq5feJRv8mzkOR-iGnq2J7ldH9w5750F44oNCYRCSHgr_bBqB7L5YMARnCgXzpTAb7k8TnmaTUH1KzVSYvwDw5eEqhDBYs8GiXYESSTHjdbvfYypiSIN7CKj9IQr1jnWrD8BjvhNWpISP_OiEvrX_D8zNpwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=fDbvFlubkkbWWlpG6aYCC6yZdyl6V9STdGxcaeGD5TGQgJo1YcMtHxtDYCS35IjzKXSKPJthDhfyKGxgCcq9Zts0eUUYpwcPSTa_oqdawzQT8gAvXBRz9WpoahpVyK2jVkK2IAp-lMGgBFvhKP00l5XP3AR3mhlO4dW2f_uLh3zsLR-Tiox4l-bYzapniwtvhSkVe31KwfTpN8_kdXs7VMw9ujO_1t1_BwZeVDXjIJ8rYaJPjR8SVQorbk0CQgeblqgxqmI_0bWBraR6fbXjBfQZ0VGnWuXcZsHBLmxHyIQoAD2FWFbToioXAPCy8UwAMBMDfqFaKcyFgZG3MboqjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=fDbvFlubkkbWWlpG6aYCC6yZdyl6V9STdGxcaeGD5TGQgJo1YcMtHxtDYCS35IjzKXSKPJthDhfyKGxgCcq9Zts0eUUYpwcPSTa_oqdawzQT8gAvXBRz9WpoahpVyK2jVkK2IAp-lMGgBFvhKP00l5XP3AR3mhlO4dW2f_uLh3zsLR-Tiox4l-bYzapniwtvhSkVe31KwfTpN8_kdXs7VMw9ujO_1t1_BwZeVDXjIJ8rYaJPjR8SVQorbk0CQgeblqgxqmI_0bWBraR6fbXjBfQZ0VGnWuXcZsHBLmxHyIQoAD2FWFbToioXAPCy8UwAMBMDfqFaKcyFgZG3MboqjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=XG_6c_KnXZnP5XNruHnIp_b9FxitEHD3aqBhmWqZkD91eD-3iwCzgi_W71RBhrEpsAwOZ3uDhKcrFBCtsC3--hyWPqVEBeijo0SrKdTr4AsTOsLntVVt10Pmw_x6mdjf_1qdxMCdGYcZZZL0MHHYgbMRwuq435pYiigE20ll5tZMdh9Lok6-_DxlchZ_xbDwn2U6nUYRXsf6F6Tytedm15BC-PVWiBghb0X8vrrhW2GNNTHd0B21FTfCWQemD2MufskqsPKAHSUxJUnll97tD2B2NpqzEfhk4J--2mvo9mTfK6fX6Ey0qSdsZO6CGT4DCHGfFtSXV1gj74B2-NXNRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=XG_6c_KnXZnP5XNruHnIp_b9FxitEHD3aqBhmWqZkD91eD-3iwCzgi_W71RBhrEpsAwOZ3uDhKcrFBCtsC3--hyWPqVEBeijo0SrKdTr4AsTOsLntVVt10Pmw_x6mdjf_1qdxMCdGYcZZZL0MHHYgbMRwuq435pYiigE20ll5tZMdh9Lok6-_DxlchZ_xbDwn2U6nUYRXsf6F6Tytedm15BC-PVWiBghb0X8vrrhW2GNNTHd0B21FTfCWQemD2MufskqsPKAHSUxJUnll97tD2B2NpqzEfhk4J--2mvo9mTfK6fX6Ey0qSdsZO6CGT4DCHGfFtSXV1gj74B2-NXNRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amTjUENDHBkxdgXa6LFsvt9hAk-KWY2NKBrzIjii3ap1e094Fmitj-uSsiz8RbwabBXL6hb37BHtuDsB9AGmX01R7yRrFzS8lI_eM6krfFKDyT3lp5zBNEmkz43I4gF6-4lzTjUYTDBCt_v5Ul2p4YbBX32fEspmiee8alVuyLB-idhUPeIJ073VzohbLqhcn8mrhVJrUlU9Z_fa3KUsjYqp-HsXcA6lo2B6jbDmNyCwmKp0UE96GN3wmZ4cvp3iVF5sJ2CtHVOacJUmsFY2Vr32-BxMPL92zf8KRvfFxX8T-eskQ20YlwaM_UP2kBUi29dcx1mzqWCrOrZAJvru7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH3-GwBrIOFS_lmOCQ5Onb8l_5GvF0N_wpERcntnFgwjrUS10mFJp4wPNuCFP5h55Ods5GDIK4D_TVKwMGGcqJrynsfK47o7YwB7qkfyPIlxyrpqOA9uRI48FwwOF5SVvl8xusXID0eic7IVe6pAnbL-nomFlvy3vLUwEtXaN2VjpkSuKTMe68cxLC3HhklDatMszt7C2WZNORY0DB2bdvBcMzjGVFcUHgLt1KvK-Fw-SZOMYwTzptvJnCQJZnvRJJz--rPIkOj5eijULQp5vCLn7txLI8-HWgSfb0f5z6CqvQAD27k1lwy9965aqEk3fBW_cbDG25mvQ9VYX35iBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=D8y--KYA3W4uVZgTUOtgjSlsUf3V3TE6PL5s8p45IoSarllO9Dqc6wtGvAeEnZMXHK4ZpDZ5Ud_6sYhwWIoGo_kSa4g68SHFhmfeuXqMp9LC6comr_RPWydNePslqE_CJ1I7a9PnJiqeT-OZY2ZqvnOXqWfH7AFU41azf4HdY5VYF1cdDCFPrUrhNHdwdbWzz0JsGY9qV3qMV_qcwwDHMkj3WyjUtopywAFITFRZYOgEd7XNxC7fJ7NfjNM9e4JCdpRuJ3Gjp6K8SmgPODChYz7uZzlaK5vfnxuX3glPOn1eokQDK58RiQSlYThffx4afo_5EueMi34_T1PLG2y_Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=D8y--KYA3W4uVZgTUOtgjSlsUf3V3TE6PL5s8p45IoSarllO9Dqc6wtGvAeEnZMXHK4ZpDZ5Ud_6sYhwWIoGo_kSa4g68SHFhmfeuXqMp9LC6comr_RPWydNePslqE_CJ1I7a9PnJiqeT-OZY2ZqvnOXqWfH7AFU41azf4HdY5VYF1cdDCFPrUrhNHdwdbWzz0JsGY9qV3qMV_qcwwDHMkj3WyjUtopywAFITFRZYOgEd7XNxC7fJ7NfjNM9e4JCdpRuJ3Gjp6K8SmgPODChYz7uZzlaK5vfnxuX3glPOn1eokQDK58RiQSlYThffx4afo_5EueMi34_T1PLG2y_Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWOst4VceqfwUvXjY-W42oZlurrKofpAFVfCTaiNG5LEyRsAInS595ub3AEyU_MY32RI7nFPLP1M-8hTykgG-1J911DFql2nQHbrTgYfoEt5jLXYG3PaacFIUYHtScjAOoqNdH6B897_Ynaog7CvBV_tvSZ98ylUCtzK6R6llfm-HoflxQGEBF0OomMzuqcGDeJYP-sadjoeGVVizlnbr7KoG2OPa9aAfJTCpx0O_FP3Ijtf63tKrNEDTnk94hUaCulBfOGJLSJm4Mbd-QeaPPnVPA1bvE43WoHBt74cRLZkm6FTRjPZ71aqlUe3162XIXLYzBc-vt1oRXcOjaLHJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpPb2rKYdjdZ161ayv7HCFqi5RFY1T_0xz_4970fPhLXUeZsiqGozQgeGsEtWtO9ofjHWLkMBkLjI46a-SHcr1Uoq58IFUu0x0oxmBoogIR_ayKhKORNqKljQR2I3opJvdgBsieTUYo3ln6dr-r8jqG7zowoMuq5FIz1cXBF5WQbds32ruaA823WaKhrQ2n4yAJ08Czv-g2Nu27l2jpokL-UDDBRedkI0xUv-nvqGhllRcKyabWZBEbVM8T2eeevyiLLvCpJQ2KZJiKjugZFDRMIABVYxDCNTheC7xbdHLXnhztg_1z9PNKCz_8jswpP67t-O5BQAJktmT8o1UrBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWEQtuFspz2B6VNzE2Bx3Ym9ihuh4K6A_weCkcH00oAhwvusahRPKKITWzaprEzwcADxLbQgE7HI6KDFpgRzkpBeVilYbvL8bqoBGJVN2LI_ui9cDIioPBIR-vpWntJlvCI0AHQNeGhliDHPwH231QzjCeQqPsRnsoTZQp5mWn0ijvOGUXUDyfAjqRy53K6GwT9WeZrReal_ftTF_NYGNyCBMnid5aPdouw-RrRjGXfocLWbheJNQ0IuCi5K4w1kvU76cLikpn1BjcecubiTYmxn-G9OWsHMFAYc9uMe6O_8Cwpj5MDXAKb9Mdy5xFY-DjflaVkLwdH9DTu0V9Dxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8_aRQzcQTMTK-5P4N5lvQMusNUdYS1LXpX5-jpHZPKI1Qtpa-ux-jcSHwPVJ17FLWCqpmvrz-dQ4L4B37ub07DrtUIOmRYNOWUUoBHTEzEDjpcQwZ-OWpFcpTC59OJNk4k24rdsuS7FzGuthuxB2mo6m4ftpp8Hc-rXGy3VHyGmL1aFR_ZmDdwtbc_ngzKwtnqzdZvUVX6mAlHiIYYHZOnCIVEa6ljl7Ekh3_5XsCuX5BJ3SVZUfMohp2FzpMYH8fiEaaxWldyXaoM6pzN5tCcbeePz8n21Yf2gv1ZRJIHRbMnO3wDHWiT2DLEYfvu10VHScO_yAa5HR1uQDn2w2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnOTL7l4Jo4TNrCY9BNd5ktBnN-cEWTUNh0Zwzo89HMsXmnXAlmfoS76-XQvI9qpR1zW4umq291uBiYDogEVmbBfDfJtAPipLfi2f8Jv30uLz4KeMQ3OTUU8TqV-LbnvLr1UmvXFeRPE3Ilric5FHlODn8uE5bEIKmfAkrkDmadlr3aGVPw7QIgAT-GozTq5FsrWfUFOqOoKloB8DO7237unirvI9RP8bK7X5vthowJMX_s7jQiUFbyrnRkmlDGDk8zV75HfdRh91E-fg_IjuBv8QduPnTioqNGZUEpGjV-zoUJguD7XEL413PrnUW-idll1LMHLUc-rrSfAI_Dc1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAU5FrWd5cBvWaRvmAS9Z68lAr9hc_AUaiP6ra9T7NXEHzC6V3p-nsZN2vpA5l-EUFH1GddRopnw7-Zg7C4MiOhcweUt4jxan1otM_1MqIFU_C24NDxVGOCx_wGv_D-5S098HUVwUVpZJDs1PRsOCa2LFxNTpW2LXZDht8xf_2nffDH7QpRbRNuhPYAcOuTXtFOEVTppnY8op7GC3lFqFcI3nXrCnNQWNXKLit-aD9neS6MxDvbLjKJNxKaucl44jj4uTnfahuigczo7kX_XHtRSFgMRI42d18hmvyAKnSVRD_htRWcrDTEmw1KzU7MfFZwRMGPRbK_D0hJm-LIjIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUyCsPPmplPN_qWos4dWU2jglCLQeZu3t-mR_bz4dQcDVzYYqtd376hMKIOsGLW4xfylwLWG7P9UTxMVwFMUzDoRUOYhUiYQHoErI3ov-gExzUi2UFeyr-wWc6FLVCcIWazZApQW1FxNrKUdBGYQTYcdf45iZMVhFwAqbi8qLVsfwcvNthcFmyRu2baXvrUZ7miFK4tbs5uYnNpxWFWasgCrX_PZi9g1-L-1UvadhMXiYPHS-cm1cGWJa0YlQt2WiEYWTY5AZP9k3qgPiLoEhQJi8NV4jPSNCZhvhczmuld0c_GpDjFtBcqoK5Ygdlpnn8ZOZuJ_ypLIJJXbxDghQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/essAGp8PySSPNjo7I808a12HQFJ7_x-lKPU_GrEnGdXv6QRKWJED0Rw7NMFKsfh5IE1VI-moeUvEs_oaXS4RR1h81XbQJX0abKScw9Iy3wezNdLWWuZDMcTKwiLQ3aOFQ5RWjdiIH88Jy90NNGDi_w6YrkJKSei0XIEIG6TA1HZKnx9C2m8Fhl4-dTBweuDx-jRbTZJ7QN8CsH4q9cQCKkPzEzBiAOi3tfug-D3eIrrCOK3_5wySi6u8iR_rGERW_9TwhZWQoRJA-HFQEJf06i3dfjTQsJy2a-ngVKrzyhMMdcH33DHVTm3rhmN-KLlqETswNtrBFyLhKa2Y1CJytg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE-uKQVsYQBUdDSp-4gv9aSVEunV9cVzJRjZ8YcFajq9Geze6OsnIChIDhbrNEwdKl1ZmwXnshsOhddj2spxhpiSbASqpJgzqZPXUcHnNAmR2mGcPYsC-cAC7rL-uu0dpawP7tH9RCh5eLnsWXrtg5rxhXQB-CK_yHq_SkwUvI_xt1wOvSbbl00J9l69Q8ZQkueq0d1hfM4szkxPfo8j4nWH8jLerZ79uc0LXYm7xtAsQ1rBHXsif1E2CTnJ6J56dygyGiJccdrFnJeBH-EHkUS3hUWcm5dVHHGFqmAY4-XoArfhKepsRC5Fq82v8Iatxwq2apt5dt0DjBdcs67x5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRO8TddUxoUGEOSRhdyl30rSvtdyTj0rTXPIIH0yDM6OS-hD5VheHHvqL22HaOCbuP5rT5xu68_275m2z41e9ScfuVsD6uGTN5F93xmMLr0MMIEExI0YVLIGP0zuUA9Rvm6VYqgvvSivxkjj6H0rYbqV3zTGY1fTyvCjUWaG-yV2lxLAWN8oaLaZCbpOBM4Rt_eQS8Gs4WlTeT0eeOjAZhyJYQqyNudpsmcjYnEhsrvi51f-Ik0a7vcRC32aRtbFpImPdbHAWLRQJT4GFg3GMEt7kMhjl1MaxewsoSW_7P1q1AJxs9Q4z3pE542OlhSKqB5xlWEpJSpKNzMSOBJpyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=PY75lF0bVUMT4lyo7qZQnq7pRHrEDGEupmXg8VkUVqdLdrCiqGJp1IIbxqZMg4WfdRmlrxBBZG5E6fYJkwgAMMsMpj5WLvZLzRPOGEdEm4fDeRgFOK8CkrNQrKu1AJjbzh3zmJj23V_lVmpXemBQC-bSe9d3o7HGukLMziOk9gZqIgpMJem5GUFPAGpnolu0UaRlqns8R58utwDuhEIH1ytvyiRndGEHKNe-KRHHmD05Oz12uG4y3NWlcyGDOlrtJPAG0vfm3wEu9AnraPkjt4f20Xeebw-StGCIIXCz2wBupZjgZYHxiqEI_o9RU8FFnmZQaxYqtpKTY3PmA9JEoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=PY75lF0bVUMT4lyo7qZQnq7pRHrEDGEupmXg8VkUVqdLdrCiqGJp1IIbxqZMg4WfdRmlrxBBZG5E6fYJkwgAMMsMpj5WLvZLzRPOGEdEm4fDeRgFOK8CkrNQrKu1AJjbzh3zmJj23V_lVmpXemBQC-bSe9d3o7HGukLMziOk9gZqIgpMJem5GUFPAGpnolu0UaRlqns8R58utwDuhEIH1ytvyiRndGEHKNe-KRHHmD05Oz12uG4y3NWlcyGDOlrtJPAG0vfm3wEu9AnraPkjt4f20Xeebw-StGCIIXCz2wBupZjgZYHxiqEI_o9RU8FFnmZQaxYqtpKTY3PmA9JEoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=r9O5zJcRbhc3QPz2I3pkXlmH7tVvWQ6fx2excRLHasaaswK-cgLo8a6m8yQPiH0gh8qH9fHnQh8T52Sx7d_W8a5bt4_phzfUUfCwzZZsIAlvC5JMAWP_eOvgy7PZ6VwjR3n_SgsXnf4sDT1rWsxL_1qcxA1nAqRxTH4la6u4W0Nu5i9j8iKoSm6A3ozIwCY8h8LMbnM6lkts9UFYhxhFulAyzdt3a2jl41vmCHkPjyZTDuzadVuwC20JJa-ZCabO2VRhWyCSfH8rejyt3gOaQQs753F7SLUPe_INtw2PuOAjVAcWolFMn-9VWQJB1O7g1vuNVYhdSVJSQNmXFZC_uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=r9O5zJcRbhc3QPz2I3pkXlmH7tVvWQ6fx2excRLHasaaswK-cgLo8a6m8yQPiH0gh8qH9fHnQh8T52Sx7d_W8a5bt4_phzfUUfCwzZZsIAlvC5JMAWP_eOvgy7PZ6VwjR3n_SgsXnf4sDT1rWsxL_1qcxA1nAqRxTH4la6u4W0Nu5i9j8iKoSm6A3ozIwCY8h8LMbnM6lkts9UFYhxhFulAyzdt3a2jl41vmCHkPjyZTDuzadVuwC20JJa-ZCabO2VRhWyCSfH8rejyt3gOaQQs753F7SLUPe_INtw2PuOAjVAcWolFMn-9VWQJB1O7g1vuNVYhdSVJSQNmXFZC_uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_1UPxttbsHDEYeM1oJgNM84Fzb6g_1VG7ybDhA_UgEHaKFVODFfVQrf97aZtQcg4bTUnCL1zJrqIUs1Dg9EqY4YxL8vYRsTqHfXyB3RgiWEbWRwCJBYtZeqo9IsVLhYLj8li-T0Wrr8IjXKNU782Jxq7xJ-SERO7UxWZTnQDlOTxy4JXX5iW4fPN7ceD-w8EvSZwICOTfuYf1GBcCRQf_vf98jJ4hq05fOex5VLEF9ZJk7rq3ZxhsOF2ynEXoKB0iJx6kGXcNFdh51OBGoWgPLGuQrFvkS94TlIr7rhIoJ6C01FgWZAHIyy90JbUpJ6Qjr8kcca1_Fwc8G_Dgh9aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVQLOo1WEylL1qiY5PhMJKlYJkqKyZX1mZTd_vh--TkXE-qItctq8M-NBMELgElOz11jSvSG9rBBrai4RllhKaOJmqqobibuvMR555dDL0FQ5f9CBaEayOOeIlf8TfcVGCs0M3wl9Vnd-lv0b7AUTuYJkIbqLJFBLZze0k0XPhRxIoai1ECCXoiThvOkDjK9jOFXUTXQXqvdt6v5q7f8ng3uU_V9uMoAYpu8wlLdDja1Cqd-X0C9Y2wOQZqM4il3UXXKa488g8bcImJ5SGIjswx4FEEbazRrSEnkGOyqZTjAtJ2LWUV7HqfO0Vi5Ovoua1QpCbijsTZs6wFqrGXk7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKLJXjQCjkR-2v7aGP_uAP_tGvJaIXa0vsMtUqxIK_wD1pol75WcPLYsLH3hiBGDO68GrfrF4iYxEnNgpGxSAXkJh6GKrkVymnxLJFGA5OQDDRoNrgUvrw0SjDjDrso4MwRbXsiQx1YzSV1uUB2i88D8Gt0zdBTQ9CUDuZO3sjNycQcwDtS-z0gX4Plpc73g4PLEY4hArlcR-Y8zOpLiIffBIY80SR0vB3MKs6Git2ElaaNnezjljsvjPQ_xHDxPyllQYQPKYv-KWZYsFh92UxAZe1-XoQURWmwP2F4eoIAW9tHtBsMIuxFFUPlsHdQxs_8HDK4paTGQGetta229hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=ALGNNVPHIizoPI7n52IxCLAKF9jkW6F6GH3uh6VLVeWzXKy8LXc62XwYLC0d58qnTdY0d3GyOTZI-T1rsVmhqfCwP9k05Rguf5mJxLRdCBE7kzj0AsVLxDzVV9nLQ-bJ_ZSvhNfNdCv2p4DK_ikfF8xKUEDAyPaspGGkYrmihfCxMfObCVtBj47YyWP9ZLJqdQ3ywjCTobceUxe0zjq0u4Llz81--CjUzlSU4BLdsp0sS5m9Ozoq9yE-e0MtKjzHdLaOFvh9-NOcq4poyYJXkPUp-Exof4_DHxlGOn2_VoGnJFbH4HSao2zfVHrY0D5jEbr30glmuGhtVtfXlje4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=ALGNNVPHIizoPI7n52IxCLAKF9jkW6F6GH3uh6VLVeWzXKy8LXc62XwYLC0d58qnTdY0d3GyOTZI-T1rsVmhqfCwP9k05Rguf5mJxLRdCBE7kzj0AsVLxDzVV9nLQ-bJ_ZSvhNfNdCv2p4DK_ikfF8xKUEDAyPaspGGkYrmihfCxMfObCVtBj47YyWP9ZLJqdQ3ywjCTobceUxe0zjq0u4Llz81--CjUzlSU4BLdsp0sS5m9Ozoq9yE-e0MtKjzHdLaOFvh9-NOcq4poyYJXkPUp-Exof4_DHxlGOn2_VoGnJFbH4HSao2zfVHrY0D5jEbr30glmuGhtVtfXlje4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFsn32oeIlLomLr1avPG1qaCilyi5PotgEjIcnz0cF7OwHZyI0uowrOlkb0TKFsU8sMTyCSrQYBQq6TO5VMx0fSLrml7-CH4xQ3-EfFgml7sQ07voCxMMI6T89dJVLBqEc4u1hKR249DFa6-QX5CStv5Q95T16OnG9G04p4dimIEQdmKheHHX0LNMUpVU-9ySgojKAC6gjvdU97i6ejvyVzfT50TkmoptrYPRwvO5QQlHJQp1czX4mo8TGyW2lMqWh9_n5pnHmfRP3BJaqxoeXLMLPlax2WjjNVGFZMW8g2NZ0QXEinLRQcUxOx78snHcjxHpN05yN-8GB3Vc4wyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpjOCNqECLI1uZUogeWu5reCYtC5jjkVsdSRq1F3wmyuhximL200isdTvdpExvKLsfN4WUTVHfpVJBcZ3rK86em7Nort70f0iSjAN0DyrxGZC7-57TrJn2APA6aprQZVJjHw7w32d_YaM8JWRYr_gbZCFWZFnTe9pDohbSXfspzuOE5q7KHHcyHDh_VzgCVFCddSDCrmedRF572A-nJW4A_z4TLVR91SoYFOg2hQP0H7SD9AhXJdwHE9DUEkvJxQcGq7rhePCANBAC0xhNCWhb11uONZPnTz6lKtbdL0b0Ysq9UWSuqIQulahjgeSJfkEeLcQS7ZIWw1iHyLo4E4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oG6aLqEcUu2SfoGFXqIOdTC0zPvy83ct_AJDfchdyVgztXAnXkTgdMo9r4kEAStmaRbriUev-UeX6E0sG6ex854xBLwf2sd2m0vJ1fr9XK09cbGzmiVNoTslhdg1gbN_nslJCTOK-_LWYJ64i-cfr2fF8WE7lEHCTZQtt3YpRML-CdcjkTjPEhJc6H6Cg5SGzKfFszvdfblw9KosotB_x2M4IpuZOWJMkXyaMZmfKDA_yXhNhVIEYXiVD9pMM7qb3zpGUtDZLgs3VVQjFXrsLSUcSqtmL5R1ZS1ZntLWx5esgzmRhZoeSwhbb56FNQY2AFnPTLGlTJpvaPLWt3VQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCWwhyJdAv0-ZX18oHICtY-Iqqiat9zVTN0MKPRA993s7uaCV9oRpVnsSIknNKzqf-W60bv-y6hNOCTRPA8lLtLris9OfLx9jFbN8eRpv3MYss2sDX5ebnDVE_CrraEPwsUiq_EokI39xTcOmkp1X1Vkf-Pmy9hg1_CbM4WV1exNwIJo6WSL6GfBXsWQXGEnNWGrosnQWdNP8daVdEsc1c5sGa0ixGK3s0WEwUXUNzEQs_eFNz41sXyyPXPu-BRGigySv_u4hgp8QkGPsnNyL_q7Xezjh07Uibs7aJ8LxVvNLHdoMY5QPFOvweT75_zpHa6K1c-vgV38bffywiQhkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMuO1_mS3yLde9y4rhiYezE4VyUWIsuEL2XI_4TLLM4Ggn-wm-M3cT_AWZxIiNS8_DvXlFfZ_ieHrv-pIGGE9cDuKh3UORYrJHr6K_qXHntUx9AGsWJ3Sujyb3TnKz68s2k4fKJRYXACfO4KVqkcMKjd9UukJO5auboW2cUPv3bl6tSXahLwwuwKO-rWLLNYQq5WhNEfRlD2RueDCF9Q5yUlZyY7EW3L-dMKWfQzxou3X4EvC6KGu14djcQV9wZrIUASlFYAQx3ozcZCYZ_gZd2ESN0ik5Lby20YBvUmxmMSVXAt-j0EDOoyfJVtJz9scO9Avg49EWYTspCYPTDlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUehP83DCvRi77sdBdikUhImWsoRJ-FOk1zdB_-Jy20KeTwcze-JbuLSQ0QhoKYCXCvl91bGAzY_UOtCaXZsdtKrIcz3QQuTzMXboA8cQRMfv945VXk4NXWLcMvxy68Ww5fLALi78j1iOZqduk9h6nUlHC0CUSsIfgO469VZJg4t7jwbB8TorDe1Frepn2kEbHmbxBFidxC4F-0VyFAUPQxRxOcfz48pCvzAWytovmgrXqhSbLJbZ0YZhaNhyhfZWp1_CFfLqdSKqOSfjW0a1u9n9oG3a3fzr_X1H_AfJFZ1a0m_zuAQu2ea06hIE0lva2AeQOp6LAgrflDkB3FNwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBglCMxdgOAvxmXaBC0we2TuEtq7afu-WpI1tGR0qdkONMwMBGv34BP-dO4wFZKpv15warJrF158t1LHTAzwdN2i1U46FKxd43ZyXttin0VZy9qheB_6zdDU6B0A5r5Yo5fWvZadrLEnjFP3K0CDmrRUKZuCVk_M0WHC1oN7WFCb1lANE1aadtwQjVBupIY-YrSxmebEfv-NpFyV6HKo_UT6QTlCPOAPPR2vuCnrP5VYvlTzJ6jjZ3DFldU-xSWp-3o-XcHHPGGKggQJTrZ4TdYAupo0BXqENyYmzvIs3lvtWcKPXJiA-sj67qZ9C-Ir9z5KCwtNrHMOFP0Y2TvEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxKNvaFRlXLBEdXJKRApTFni8892iAySGkUtQdTrkmO5Ev55olNaOUrH-cYfpj8pv5Ljpg5wJAnpYyz0Tqfy_t3p6A1uKSB-4NDOzWQ0EBRCuv_Qf1d72z7Q8ExHfVmyZcShmPhbyQUglTpVH5x7jpEkk3pBiqVeFylqzaJinrvq4tVYfggKg1L-gVrEANLiIpHvXg5FBrB773u4TIh_OlkFSgoJmsP9lLlJRsmDgnXJ-DtlZ_2uLJ1fMb9MNBe28B-_QWJ1GE3rUFwyKzjIh6L1m3QwMJW8Z4qb3S5YLYYweLF03hNtGwUusybk-6u4eS8ziZHb1BQyX1EeClLQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMGTIjO2MbCuWO12vbwosu90pFe27GLLoAyye7bVywFLJEfAFWUrFJwVSK9BHTaO9XBIUjn9A66Ds4mfZ02EcOCVF7kTagUVjo-ApSwTz2ZaqVtRb2GDmnxS2c1QWwc5Cg-yWHHelu19D080pVYQrz7EWj1FI7piFTbaOaf5z3qZ-qWUaF83Q69ex-5iEzSWNO5dtrRX3-vD9HOULqq1i6fdXCHznfd0lS4n9rwidqgFcC_32pom511yW6TDInA_rlteY_7srArLxZaRvGtWCFUOOUuhu-68BCtU-3wO6tDRF3keI8S8GM3eYSUdhhxlMHM-IcCRWpKhR8QWRxjy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptV83TaZXuXeSxCyIdef21bb3J01-nTXthXem4qb8IyXzkAAftFgCAu_zHvJJp0STFIb4nRrNy5xa334_9oAKN90vKF1DNTKU2YkaA3007I2O_9i7xju3sq1PnTRR605LIMTDzvz4o1Em_MkH-uM7uYmSTNxrOJX7punYhDn_BsF47BNzvSWWgRBksKkyD-9SAN9_PC3BgYClIkbewMlB5df8bDFilBVLBN3BvLyexQ3U95tiyhwM-PW8393DDDyRx1iM7lgJDnIsCP4hsL26-ARgaZAocSaIahW7vK4HCz7xVQZXyt9BURoISsSjTejT3TESjvteniLrEODCcjpxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW5IO3fQL_MQNQIU4CHpREyARaSYZH9uPfyznLJA2A2kxvf9uOC6eEYOes_aD-Gux-36MV05rMxqcxvJnBRe2AKaor_2Sw4BYAiFnSW-ThzgoLkkzOJ0Nym8XoPrDFWeSeMcLgfBfBbJo2AHAm19MN1Nm755JHPDnYwguiLtqUU6UxK04J6GWJwnJ8F46aGSM4iYLDO9Xb0s8EgDRYoAB5eenBNvrzgHqrJJ7mnDx_aKVBDq4mmhghozu8o_qg_CC9PrvVzh8qEL6loxhT4XhOQ5YHI8iKPXQRlGrEZKDe0HwlA3G18tt0HE8bNovm1U7WnLr9Zt08xP1yi0qAslow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=c7NKsqsVxg619dvQfpSVyG1bl54puxdrtGumK_MNi9zSkNachpKLM0Ff1H3bGSMOilbX5Thrl9wjhENNEaClQFbDy7rNDVsUQbnMgbslw2-0ONW9cNHXnaMfSvdyvaVR0jqBrNsDDxU7LWW3wz5RY5EDpps5kRQta95XNDt2r4-znM4eHAiYEfNLoRy938zdGEPrwBJhSV8pACIIgI9i2nag_6adZ9inq7D1VaK3-dJUtb82B-tUK1K7DVJOSDATkNEznJzM54iqxa8xdjU61lYqSfiSKmULTcrue2OzkFmzZWnWhk3qQxqaVfq8CH7tmP1594lUqFCIWMaw_JqIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=c7NKsqsVxg619dvQfpSVyG1bl54puxdrtGumK_MNi9zSkNachpKLM0Ff1H3bGSMOilbX5Thrl9wjhENNEaClQFbDy7rNDVsUQbnMgbslw2-0ONW9cNHXnaMfSvdyvaVR0jqBrNsDDxU7LWW3wz5RY5EDpps5kRQta95XNDt2r4-znM4eHAiYEfNLoRy938zdGEPrwBJhSV8pACIIgI9i2nag_6adZ9inq7D1VaK3-dJUtb82B-tUK1K7DVJOSDATkNEznJzM54iqxa8xdjU61lYqSfiSKmULTcrue2OzkFmzZWnWhk3qQxqaVfq8CH7tmP1594lUqFCIWMaw_JqIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=XMV4oFqRBMuX3aL3obo7iV20D78HMtGfez2i_II-VptpgRt4CmE5VDtUdVeucXmSe25zD-ZDPe5ouu6l3KX_pN_fGZKLf27EVTCB3FJN9rD8xMy_wPJKWiafwPtQuajywN0D40UmvtvvNm5iZYbJcfPayTlHYLQQNHDG7lfLIbXPLHySFoQX3zMa6sxbi3Nbzzbss-O8ujBsBpzFwHC5Y-AVLT6SwtpV7qIj4LPit3EKRHzNFKCjhSsdMGRyRLifUSpsPY3EvNE3hLq8OxNAGDp2g--FgAky0nhQL8P2Xib74sVe009kIa8QqWy0SD2pybnJYQIJ0ap1dOo2UR3E2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=XMV4oFqRBMuX3aL3obo7iV20D78HMtGfez2i_II-VptpgRt4CmE5VDtUdVeucXmSe25zD-ZDPe5ouu6l3KX_pN_fGZKLf27EVTCB3FJN9rD8xMy_wPJKWiafwPtQuajywN0D40UmvtvvNm5iZYbJcfPayTlHYLQQNHDG7lfLIbXPLHySFoQX3zMa6sxbi3Nbzzbss-O8ujBsBpzFwHC5Y-AVLT6SwtpV7qIj4LPit3EKRHzNFKCjhSsdMGRyRLifUSpsPY3EvNE3hLq8OxNAGDp2g--FgAky0nhQL8P2Xib74sVe009kIa8QqWy0SD2pybnJYQIJ0ap1dOo2UR3E2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=Ur4F_JO1bGDFnAYHj436TGj3hgsZyw7TEzc3qoAt0fNUXFAq79WuEhCM5Y5Y1lyJ5KCef4glwfwAtsKGZSKV9WPGSH3MEvE3Yf06mBQ9AGtmdlLzIIesvPaeTULIpARvd3_qAb9vE-NEXY6s13AqMPGiUD4jFWwSDKQACSBUjwSRAGKx_QNlP1_SNQXW3Uc6tB5TZ-teBcgIOaqHFGPvsJrrEr97EupVpNbnvJZdWe0YUB5OGfxgEk5rqFjiMloGxIaJ8XcKcAkgfoGXttZ75Oxsbs42uz4r6pSxWPGb4b8a6PLNStyc8BuQCyk82406vxqAQ6hEa_Lmpa39X64aMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=Ur4F_JO1bGDFnAYHj436TGj3hgsZyw7TEzc3qoAt0fNUXFAq79WuEhCM5Y5Y1lyJ5KCef4glwfwAtsKGZSKV9WPGSH3MEvE3Yf06mBQ9AGtmdlLzIIesvPaeTULIpARvd3_qAb9vE-NEXY6s13AqMPGiUD4jFWwSDKQACSBUjwSRAGKx_QNlP1_SNQXW3Uc6tB5TZ-teBcgIOaqHFGPvsJrrEr97EupVpNbnvJZdWe0YUB5OGfxgEk5rqFjiMloGxIaJ8XcKcAkgfoGXttZ75Oxsbs42uz4r6pSxWPGb4b8a6PLNStyc8BuQCyk82406vxqAQ6hEa_Lmpa39X64aMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_MnNcGGiH1K3XpzMNVuJUzBt0-s7ZeveUewegfv2mzALLXAzJdFD5OzdljurUdjKb0yxoNMl39DL7nkC7Q4bEU0KuKh3vZ-szzy2VJ8h5JlHfGhwzK141y0T0KX9cnPFUo-guliwAlO6okZAqWetaIFbhMd616tZ8Iw-kHul9RDsaeBqI61EOnBAK25kGQBDbNih6MzfEzEUxpp3ZSC9w-bnHKtNOxhqRSRgHF9qksaZk0_4g6uUNcjbvZMxe39OuFhzR0RFMmbpup7axqOCMelczwg6Q7yiij7T8bn_Q9rtFiacVWPUO8uuV7Awaxk5l0-oFQB6Lz-yG-cjdKYlA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=a7sL_jzMqm_kNdgMA6Fb8YYvpYYcvG4w9Tvq8Y4x67xbDC8VG-bHpkOqpWGo8UsN7fJA1pTVw-DId13QHz5T5S0C53L8TIy2SMiDxRJzumPoFL0k3rHrT9IrG6nTwzSAn-Cbb__6wik1iNF8GGX93UsnBA1amgDmHBRWMkGSTmy8PD99vwrryhLpuY4uaDbOSpOymkBSdwk8g2uLKnP1BJZjWBFjjwunbG7mKYcrJYco1HY-2VWPKLvN4bQqAIjU1bhpDEXx5FF0XSOvthujFarxUsK7axmMaiWNJBKdiMlBoDCxPh-VKzErNvejfVmo5uN3bQhBF8nfgkWgTWkCuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=a7sL_jzMqm_kNdgMA6Fb8YYvpYYcvG4w9Tvq8Y4x67xbDC8VG-bHpkOqpWGo8UsN7fJA1pTVw-DId13QHz5T5S0C53L8TIy2SMiDxRJzumPoFL0k3rHrT9IrG6nTwzSAn-Cbb__6wik1iNF8GGX93UsnBA1amgDmHBRWMkGSTmy8PD99vwrryhLpuY4uaDbOSpOymkBSdwk8g2uLKnP1BJZjWBFjjwunbG7mKYcrJYco1HY-2VWPKLvN4bQqAIjU1bhpDEXx5FF0XSOvthujFarxUsK7axmMaiWNJBKdiMlBoDCxPh-VKzErNvejfVmo5uN3bQhBF8nfgkWgTWkCuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=cGDpxh3BBeLXIZQTmIt-WMJULxwOG_E79vUt4lPK5f8JkfROhitm7n3bgJ6HPNVkBEDhCpM5_wCDdCK-kqjOECYwtYK9YLyXJU-sq6yqlnQaaC0chT7BYx6SHaeO2Tj4frbvFgHbdm1qAdP4-7aXN0KAAqMos4p5FyDJpD6dhit8RTJenjKojsO-x9MxtCFGqli3rmkHrZrMsF4MTrKy7eb5I_GUqqjoo_xN9remM0W57dL6GJWwmm8Y2XqfLY6FbhKQfXGK7XqvMzX5EpZ7JxxkJmutl20r-Rjk8IyIMUaB5LRTihJjRcDXX3b86KvlfXR7hZMLEYX_fCfiz9Yumg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=cGDpxh3BBeLXIZQTmIt-WMJULxwOG_E79vUt4lPK5f8JkfROhitm7n3bgJ6HPNVkBEDhCpM5_wCDdCK-kqjOECYwtYK9YLyXJU-sq6yqlnQaaC0chT7BYx6SHaeO2Tj4frbvFgHbdm1qAdP4-7aXN0KAAqMos4p5FyDJpD6dhit8RTJenjKojsO-x9MxtCFGqli3rmkHrZrMsF4MTrKy7eb5I_GUqqjoo_xN9remM0W57dL6GJWwmm8Y2XqfLY6FbhKQfXGK7XqvMzX5EpZ7JxxkJmutl20r-Rjk8IyIMUaB5LRTihJjRcDXX3b86KvlfXR7hZMLEYX_fCfiz9Yumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi2_ShdfoBlzgJeb8asgUCry2FLo5VxgF6j01Hc1CFD0Qknw8vdTyoYYlbZbupwLBekgxiLtIJX8PzvfG6dRUsN9stBJWCaqlO4w4-wTA95TKP0gwyeC9rZ6nNFozDYWxZ0pVz7gLahYGOUJUsqA9WNOeVYXtUjlSuFf7w3UhIo5CWauYgidaPeZCMoC1hhPhjeDiwZ4XTbhNrzlijStSLQSrouLePsWWCgWgT0efdCUBKOIugLLlyLXtEtIc6UJsTdnyaM3SIPo22UOk7qzI_t85PXKYrvuFHp_6Ogyg1kRUO_LSCbyCwOPkbXjDJY1A61qYRIQP6NXvHUGmla40g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsKkqu_F955r_aXW7oAvE2UMMDlp7QPo37entwM1V8FxvY9yJunI0aGVhbhQJ667z_rzBwyPGb_DpB2cgvesbTQss5FdkiQx0eZp0SB7XZjruhKjRwamsplvQ91yEK5bnglSRUaNQ51DJJ-OBoCP7mG1DA1CbrZ0QbXWPJOvXd_57H1ddEDhgDmtEwHqa1PuXu2HulbmYR4rmj3syxJzCfVkdLidSezv9JC0IzM1S_j7E2xSwD-vK17VodrtklvZKqjc6kG_JiOJl_Bi0vjeT_G1AcQ5w1rFqJj3D8bt9iqU2tzQ0Ejo-xo0eizPc252X0n4fgqQPzqAFX85pkkkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pITFtpZLO1ZPX9YAhoVEdjAbiHNdtZhVmIHe_r9AGQhbg-ySiknDeucrU9dFQuKC4EUGtKx8WZcaapYWbjeliPOYTv-Iah5PnEXz1f7xe7nQziQlzv0vG0VVMEZ0rd6RrtWurFIvYABGsC4HU_QCxqC3bjCY6G_m85BhWsyjUC_ProoGMVovnoIIM0bjuboFhxZNbgm9Tv4awuupYS6zsMjsUjNDamvCd-JoWj9rAOviH0hLolaMrgs8zg7Y88lWjJoCEjQeOoftxHwY6VKptXuq14EFHlR9ZpF6os4fQlMvr1ZKqJYWDwnyepkpo-fv-r6yfE_zGBZFZC75FFpI5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjyaQ2ptwcVl_T9ukhuhANvz17MJQ2ogfc4aDQfLkM5Czm4-fVXR2hpw0jVWdU23ctJhIUzWeoUKKRQwIMUmZpo_QcCZO97K_-7dSApF9odQF0RzDbpCGM07AI6sGTGQe560xbmKRZ5fx-KqZWiMld_JOwofvRmpRnqrn1J3fe5S_gP7zu_cEmeQi9T6BoSWjMbkSuHdEAL1DlHwBKofc1CqrgXZhhxe1BfoVtF1MmPsGpoqGdIf6Djk6W9pZG4Bj0Zx81gr48eVjdrB0U3rRbXtvYrhDK8itPLA9X-nLwQYU1AIZVM7YguAeBrFXc8cITKsO2FcZFrYDgxqPvsnTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjM77vJR8KB7fgiizOKp36phQJze3g4oUqNo_0zpftlD2BbMLJWWkaLrLOiCvS2GEhojI57KuTd0a-dBWhtam4Ku_MEJR78LFa8z9lnd7cUVWgYzpgXcFH7pxgn_zSYVJgDN2sYXtpsxWxe_65UQKwuxOdlN2VO4wvrskbe58llQ4DLXHwN2enI63A_FbcRbM2YDcfyZGe-OCxjwOL9aggQKQoOuWWJUSVf0vpnSPrZ7WSFcsGonlDpjZ5ACEvsy5gwDX2xZubcHuWNkIpWg92jDWNkCsXDNUbhF2mHkzrFCCwsPNzrHJVwiIakp9Nz0kswiBkN73EyjnH478USopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4pGWjUlDsr5vOPRnTrK7SVs42vZKsu4lFs7S4kgnwYxDMJnG5aPjo_GeNosQTp6cSzSktuh-5FzycX2QyyYNqMP0X5uaVipIVJYuxIxT0eOyHTrg6mhCAqcbfF48CztB-8pXk8aWrg0B712jweiPkkmR4ZTObnb2USTT8vE7-HJe2FgyhY_Z32LyLzggC8uu_8xr-sSUs45gvipHL0L54Ev0u0zqTxYJsnhSgOUfcjiSSEmKbmSRpzSzzSjml7OhBsGg7f-v86QwLpXAOPygS6Fr0RBMlFyx0ZIcK_4ocRmFhf1AjY93nQdqqSjLsWeQ4zmCd7ZtWLqmrd-6kN2Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOnvK0S-Rf0lmxko7WPNnYlhKUpMTip3lUJKz-exrF6KVvOh-dRt1fGJfy4SYnvQOJMd4Idw9MAXRFs1wc1h-dtqow8hnV_GXEx0OkHlwCVV4tzS6ZPWZDdX15yAr6iPIGswijmOKNk9fKba6iFphRYnWZ7rxKrZtxuqhVV9RKy8a8o-VMLox9dGejlMEHW_4RqkL_ZBxZ6hHHX5HQSlrChZcZm34yCmL3c-Ce1VJ8wshqLCJHZ3JgjTfcqRiCfSWTdepJfoIuumlb0TIH_xTkC0ud4glOOWl_85vlkVEG9SEvdb3zDVW4ubNStnT_XNLeq98GY7i0-O3PqI7Me3Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=i7FBdPgaF46Vw6d_-eRg0hoxefWYvVYJYoNhaS7-We4Jl8LiEjQ6RvwUcyf19JgwHZcesR3xI2FqLLVCmA10h9oiNj6KIGCftciMpuQrwjZIMPjIiQg2VCgM2IZP5SpDDG6XwEljTGJKtbEs6X-A4iH87lVH8knMRuBimt0kVqrtBP85GMENjEbd15f1wIU_yvxZ3g8ZatSFuy3Mu2DPUCzsSYiC8n2vzHn1MOqYogqRydC3qmvEG_hrTp4e6tDARLZ2ToMDwAfFWy3xZjDZgklWC2Vtiq6jciV1NdUUfdkLt-Ue4XbDTgH2Ze7Y1iGgUiZvYSNNbrC41_1_zCfFbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=i7FBdPgaF46Vw6d_-eRg0hoxefWYvVYJYoNhaS7-We4Jl8LiEjQ6RvwUcyf19JgwHZcesR3xI2FqLLVCmA10h9oiNj6KIGCftciMpuQrwjZIMPjIiQg2VCgM2IZP5SpDDG6XwEljTGJKtbEs6X-A4iH87lVH8knMRuBimt0kVqrtBP85GMENjEbd15f1wIU_yvxZ3g8ZatSFuy3Mu2DPUCzsSYiC8n2vzHn1MOqYogqRydC3qmvEG_hrTp4e6tDARLZ2ToMDwAfFWy3xZjDZgklWC2Vtiq6jciV1NdUUfdkLt-Ue4XbDTgH2Ze7Y1iGgUiZvYSNNbrC41_1_zCfFbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXjcNhkgzept_EcZsxMeP7l0WPmuIPwLA9VLOI7AEfI4egsAygPb1CFtgjWilRmK-wnCzjH-QHexge_0xsXIGCYtub1sZZauG9UrLdDepqB1tHaRjufcOTzNrNG_XW-RIWaxEvyt5FeYWbX4ROQpw6tL3_HjLQvj2if-VJYqXc46Z5o7Qdn3pPylaib-Mezs_JxSemgJUH8ZIZuCnImJMi3y5VqGeyZbR44V02c3Jjn9hngvz6B5mU03-KxspGwCBSvTUSWhtCEICTVPdD0HgIjSWahnk8TvROCk_7JTm3jHqB5l9yqMgAEaDx3uYj2wywwCUlXXmpt4pT7H1w7DBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJtVASbNFnp3--GI8sfmv16HRFSDJ8QBu1bIhpe-Wbq3XtDf8ZAjC6sNjROfUIhi2wAWVWxtoyMOc0pyG3c4WU73hXF_r35dLFMHB6yLJD3rnzhFZ8rc9nMYMy_cT8um9UJranGyVwTgKGbNaY01vrt3Mbm8tf9yE473trGvIW8iynP9KsT0Rlr8xmXCX_ZCqDIb3-SPT-D1V_INcaGqZLE_iCrw0h4eMaUfZhSbpcbgaszhx2sRMfJb_RRG_RcRJRUE8YWioAxIJvSZ3Hp_apjjKuIz6IBIDOMZCNMm18oW1nsZ5s7gY7tMxBG9nHhCjiYgMO7JGj5X8TrObgzKig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGQu3mANaDTYGnjfS7nUaGqsfM96EK5xs0kacI8gYNCjEZhC_HZ_7oD3gWpakrg12LcBgb0IyfdRtSpS0Xpk9JXwcxrFjMJ1rb_cG3IsILwpUKdb841PYfBQ4PyqCE1WYhDt_jkRQgbLi2MY9mOYEd-gcB3nknN6s8Nemrk-C1q4Y2JUlAqycDtxarZKr5mSMdiPba_-RN4Gu4yOVGBqL1kQAHV9jur8YfsdPT14-aIY-gqw9QMV3V8AMARk64Us2HWZAApy1ziExNoDwwGYwfyDoa5sqlNabcSQ-Nkkpup9NRvvAVoITI64ApvtplNznj8dIDe7npEI93kRST8Buw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8qeVQN66MdwX-tU5HuAopS0WJU9n-_JhYew2g3386aQy88fWFbQ6IlnXks_Kim-txqKt9t7LzgyCJMp_jNH9V7HSGic6QMuRml9dCkVoH5zruT8eYy90CTe-fX_OQ5-qOCzRjJyqd8xBJK5KfLNqUZ8vAb3Cyvb4UFI6eMaywXETt3ydjcm5heHhxM5Zty-dybAgBtuL6TeZel5pRoM7kZIp5BNeZnu_MXbRBE30EOcRpEqVLMkiODSycefYhPKBFyJ2PsoejoFlEKEloEQPeMPj9NQXZ2TIFdLgtr6Th1X51Ld644KuzBH4UZ_y3KipfC628c2HRaFvUeQZ5dQiw.jpg" alt="photo" loading="lazy"/></div>
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
