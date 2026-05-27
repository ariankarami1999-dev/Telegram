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
<img src="https://cdn4.telesco.pe/file/Zyer4a-2Cuf_h8g8IjaffaC5ParuhVPWy37Mb2vsDloB0129KTHzWkp6W229B_QZ-xABRzNiGM_tqbLrtPGDKDxmmvP-oEOpHcwnvL3eA-GSNDrSlHINME1clv1baV0adEXSeCganbWG4zgIaO6W1yLb9_2snQTgFjLnFZR7trgEBb36lwf3Vo-OOl8F26tujml5x0gVr6uBweXIhyLSpu5o8tqEUI63i91V092qK6MZ6CuMY_vqDM4Gc7qnXfdHZr9D1PwNcjrr3MD9yILU7Lf8x4lPnU65qPeZMWuIaM3NH9Z40KQ4C1Ncv_gOU0Bsg1ZKL_HZruLbtzjm1pMhWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYARrQngjfhwa9owHREzIhBJlle1fvYd93T-eRtLMXNZl_9QmyZARBMRmKkewF2BWz9ofITjKVeOpv_2od7TzX54wIoXPXV9YC4PEwnuCo7gdxnwYCCUnNzplYtarxqmFMV7SnOknrpVCWsM35VRqI5vUowF14HXsvsKQf3Q3JDpjztGhY-ASK6MBdghw8Jt8aLENNzSmfsgXLAcvpgLhneenHI9KGaVKBQ4tWeg4uoEUVHKsNsN2o-Yzki0pZqcA3qHP1l8ds_mPwZeAV9Br8q-ayC62vRGBopP-sf0lv72nciNuHwTqSFQ70-qnSgGgbzDagrXJeTpAThG1Uw5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2eq_AYHEmyGM-t_GYmfSql95uMhnBXd6eA8lfjmuRJ0S9IpYaJrKnsDF8Qb_P_DlU24goPy54oLm0mYmRRs2WhHRlc1r2-jzbpNLdeDRER1DPFgeKLrrqq9NhLt8V14Cxyjh5ZQ3Xf_rt1Qjy329fgY04VTxPaG397JLoKxc6uY0NK0dogN_CRyckU-m2p-3xHbF9WxAN5FgFnxMLsoDxTtijscmPEYhieyhtogDpdvbZv5pYH1R_n-ka7oaC2mXVSv6BdxH8F2np1_AO14syTt53AjZ5QxjxIVRscqJ-DZxcVYZW1yw4t7Ro2I9Nmz8rfmyZiXJzFEwMPpuX2lbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0qrPiYNKc01fZhSOtfSMkRAL1mDOFMCQ2oVoBujjzyAoaP7jkEnptWTHfga2NSFlUC5Sb5_gkkOEt_Syur11gZm05895M0VsSzzKAuV8UGa_VWQeAGUbx9pW8VJy1r0mmi0PiF3BDlnnEFHJB5iDpVIRXJyhoeHtuDOOVk0sUe7bVaP8dbOZkE9T_dK7_HSOtR_5xZReUUvKW9glgqIJ0lNUhg4zDmwOKM3-Ad8PGpG3k7sK6SnGDZUKyFxXTCDQ3mpjSuJcsRHEj38TjpsnO6H4q3131S0-BbzIqkfWkyDbr_cgZAENSyF61tTqa6Vg09xMDVc7S5z0ANYI4peNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDV4NmIBTU8-gdY0RKnCAzvjiXx28oJBnnip31C4OiSDTTEwOUNGVexRZD9_QG5jkK45saUvQEi4rOHQPQtVQpNJUQkx59kMKMpcZicz2pB4m623MpjDFgcWjdVId443VWo4UH8eL8Cf1VerINlh52dajLa1kR1ebc-4sCifnv4iEWiIR1ubjmIEi2a8UGqhL68chcldMMCahxPjqoC5K0CRmuJ57gHCAtedacevPwVZcp8CP_qu79tkxeDj9gjh3GSHkelKkgvjPH2Qhs496S61ikIh5yMCfCspk-6AfP9rw59F_YqTu4tdJanyY2BDMbONHNHo-hGpKMvUrfVJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBDF1oewFHdmY2bFPLROZ5Pft52CwEgHQo2KELE6Vwtqrhcg3BTSMR2_ALLPsS-wVmiNWyC_CkhSOmiz-aRtiPaGc3CcrkS1XTxBUYm_3OJ10dUESlgqHH0lNwzrA-OlaEDXwI0Vo9aYnl8b1l8-QuzGDkcLl5LKo92486sWubBx0EiFFe999esXmWyBOssB6YwabMV5TqhXgYbeBazMVeCGbs34V9JtyI8i_U0wjdNnsoKomQY2X41p5rP7TPNFnwlXQeXDs85eIeb7scpDn0a3Ms4jF5BYEJyt7VY1zb7qedcvxMkP00LqTJUV-gw2BXamUgwiyIM4Oqp2BdvXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cla1X7EnM2vgYNXhxoVWftOTnxDfTYErL_0E1bMH8h9L8UFktuPk0NqRhpeLhil5WJs9X65s5MhqGNxSdI8AkBaqLSzO0bS5v1ZlONehPl4Tm-qypaag7lKEciOMC2xKybRkbk8jTMyJpgnfJEtyu2AoyY-9nto8cz5Hx5Rrtv6rjnhN7_pafDkNcKS2GDpoJoE66QxBBld8l2B3VP900rabW69D1TvR1ynnTTpE_QhtLEQW09ZSWWna1JeQcngiFr8RPhVr9t4WWBMRP0gNtknRQrbilat9DzaQ1tu2QlpLL1UM9JTyKXlCO3uV-xb8vadK91_EYzPG0nkXeZ_MOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPKvEK4cjB6ur_6M9aekCBckrcJ22cHU0PmxM2_oifuYkZvOO7ZaIS98rswfm32qunX-rJonYvMgzsqR2IYxjY4nlWkV6_9aCf7lgl4HjwYhrW18T1VKqD8gQkCY7HhBFoQY7RxTN3PCnjOv0HsnRm-RRQ0wWnXwmsv3cMqbx40TicEgPU6O4FGgWXd8E9nmurKd52rZuTRBQWwm1AehZx6DG1pWuzNYKSGZOD9Hj1wihTVXJU7tUkd_l_eMoTcvUxuimTr9CxP1iHnjjgqpFXqto15vOayksNBX7uUcYY_azMtDmhTj8H_Z4blf8Lcxq5B_rZXthAJ96vmUH3ndog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw8hCPlWTLHpgVMfZiKHgPIugUEQ7gyIQZP9xgqu3GSnT_ZgmoxCsR1lMDwVlNC0lAKNvZKCw5AxurK9GkjWsuDJaFrrO_CwSBBBp98NLX2uLOmLGBjCNdkaqLQzpTOzoYIWRtrdCNHSKR1miGBK1tE8GHRxj3aT_jxxeWPwpBD8chi4L3lXmeifV2QyLiKnv7PB-PZbKg91dZEZ0kro0irSzQ0YSYVIEV75S2iSOICee3XcU4FDR7weDIusxFJiYOCdFbFu3bSpKjoPI1Bk1CiNSauc_iWSXnGfaVYipdKWbJ4GscM8fBGD-MxBjmXEf4N_hNT9CVHYTCv3k0Fqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4sHPwwOvyMv33b3BylQkZ-NSbFsrWcpag9qOp2Ya3a4t9h_56mQjNZbE9WPTDLA0xixYR440pSRLwE_W8ShNn4eBMWI-8xaYa1SpgGVLMmhtZ9zW-nuoVcp_o8JvuMe6elpBiFIjE4QlrzyO5oN736iC8p_s1PvOE4DzObYrmjjx8JXAHoT24_aQ5U-pC50BcjFprKsKFRUytTu5RqPadEnaX_yrYXzXEsKGUhMFsDfN1y4Npvg40_JSfRF3PIcsgq6TxVZlPS9fTjf0JwrApGzgUfaY_YKQSk_PXvtvpL_hfMR42N5X92p4D06xxmJmE1NInpKOsxpJAsnJ6E8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StdbKNy2NYED09oUAj1exNe3bpmDbOQN8a2r_G_HYG14Q67H9sCdm2biYTTo_9AmCa5BRw-u__I0xuSYEB9pY1JZtQ0mx-8KXQcOBEjNFZzambSVsKCNsjZwhcyqh8U7K79OxOpppgMBLYJGXAjs6h-qqVr23USPmWpJmiRK8fsrRx5WkndKhiSnPwjj0PM3Ojusq2iXwoHwcED9ulmEj5S9XfwxhDL-QqMAFqDz6Z86OEw7wx0bcjpC6D8GUc_8rbMYZ4eISZC8p3u0ex6tYtXmecJHWT4vzxAFMhQA3lMbvhTMezgccWAnThOOemmp1A0B_69IawIPEH3spN0i-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0YdZm_XlwtWGvjqLSxs7OoJSB3FiMlFyB4cL33Sy9hkqCa_5UDWq6b3KG8doeaVdlX3vJl6LKyW1n7oi4TYsPA4-7KzeKgAMYDcoMaU0pWP-vjrUxgUTH4oobMYAuwIo4jreQ_NqjOF9XgpGqKn6NJBHQYQCNA00Z3iI8fIduKta1rilw_pWyWvhyG0kMG9LfHWTT1ma8cIUEui_gajpbKwTrKjjCe7X6z8_zMobOlIH5lwqYOitCKrnnmMl2UNCzA3EJwuFqDsenFeakJi80yBa-I3CYLLTdrhTEEbOAut3uy4ziR7sUbkvnKPHiwPHeDYTcxxO7OrfnsrMBENog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4qRUQi3mWBvfwhUjfiNuIyuM1lq7OP4M76SWu5bFry03AbqCC_vRhrNREJ2x0p-jLFf8sctfDt5NG3-UD4xBnV1VCTpIBsKIUp07-B8fX0AKvCjjL72hOlpiW81ePDe2N6I4_6uGX3dZDqby_oTVtI_stDHaevncShUHLm6dv2i58Ol4Ltun7dJSY2F48kLLEEc5ib3RKXkFuT6xnReeLf6YtIyimz7jnYoxgOWgJRPqegUly5RqKCZsQhAT_PxluCCHgN_uh2Ga3gAJddT1pC_kV7UqRCf-lDs_oqm1UAMWEzvk3Mc4NWtU2Yf4CuDoGqQPbihvSEwT4ZdXbN89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F972b6kBBj53eXauYVRPdxzlZ9gdbhHJrVqtCufF2KqpS0hnBLOkB6tlhY3in-2E2tokB1pv1EElp4tD6zR_CkJXnqrl1HMfyRfucPVsuxzIhevWXbDtflVbCX49VMlg1tKnIHYxjNHvCXxWtM7SEJebAe4Ljw38VUFRb4HBaONUUPkkF09bIQggiSgpKpG_v0IUNVIMeF2RCdqYwF0GLFx-cFtB55p0kz2d6QPpzn2Wf4Dt4iwvuePdOlMBgzbFzMOzuMu_YwLZ0eJ15JRtLEBjVTmMUyrCKYIihsyc_PzLXjm5nWqULOVZePX0-ms22OMZhb7mFJeHEd9gVXTj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=R-AFW1GUZ7EYbgMz3C1MuDnu3jEK9MurdU-sinX2EIHIx46yJRMt8q55Nwo6HOqdqYiDYDy0VzlqgsejnHDfyHJL3uRiP7SKhNiyWrIspyc2pSntsX3GmOlVyUMwiqkXHcvTLqa8C1qh3rOrYNL5vyNhb0A8JnnNEu1ECVZ09mf-BVNVI68Ejg8hqjbn0tFA6m6yNMOtQOI-yNeB1m53z9Sksswagn7a7V-6bDXDMEd79eedD6kTA_4JHb6ofnhKKzy3V6_TXBQPXz4qkswGRoeIwNxrUtDRry6CkZW9EhICzXyEukNl_-AAB3k12ZBk32DT9EKXFxT960Ndzj_s2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=R-AFW1GUZ7EYbgMz3C1MuDnu3jEK9MurdU-sinX2EIHIx46yJRMt8q55Nwo6HOqdqYiDYDy0VzlqgsejnHDfyHJL3uRiP7SKhNiyWrIspyc2pSntsX3GmOlVyUMwiqkXHcvTLqa8C1qh3rOrYNL5vyNhb0A8JnnNEu1ECVZ09mf-BVNVI68Ejg8hqjbn0tFA6m6yNMOtQOI-yNeB1m53z9Sksswagn7a7V-6bDXDMEd79eedD6kTA_4JHb6ofnhKKzy3V6_TXBQPXz4qkswGRoeIwNxrUtDRry6CkZW9EhICzXyEukNl_-AAB3k12ZBk32DT9EKXFxT960Ndzj_s2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrI_XpXJjzx1OLgwTcVpFvYUkYIdFjukGqotV1vCOLO4_6ElnE6rOjlyZX3aiYEBWniuAOXObf8n0SYrcdbagRO7MARThbBeAgeMVvKjL09HQoyrOH7GHNyVBMS70jWNJt5mFS5Qz4mNH-tcYZ-WcApGzYLgwl_NGlKfUnTmmiSWX6wL7VeILxkg8IkywqVJ-l3aN6QroK0vl1vuFs8U__vgtbBPec43wR6z4sg97KeJFcrt4bWO4Jo8nJzj1tbxRS3haEvVQmZGcY0be3XzrokEqslT8rt9cSahpqBOx_1pqlXfJYOfwQ1ZEVYM3qJQvHgPZbU5RDunQeXbZgGLPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzIibcALdLlzMM6cawTfdlKysgak74dVFH4qFHday1jlMJJVRosOeCCXGIGqn3jo2LEXNRxInqFknqOFqdO5P6hHGGyq6bQOqgxOztlWwE4nPKHqkRINWgFoawBEeJX3F9W2WSJRwUXjDlPeIt20kHXOgUjQKaZVWTMY_Y2-0X7KTRiwsJodMjJHYEGRHCpupwSBuI-wOkDrMm0ANz6vdQunNC1fINuSuddCe4WRZHqwBbDd63y3ZzQOcH_NuOnn9D6VFT2NiGDBFZlXYYWyDMj7jWEJFsDP4X89YtTG_Ww9bWfevH-tYwOMCpRROaVoIRZ5cDLPbaVFmhHlNL0l-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cduv4wjysqmIgGr9eqFM-CZmNMES3itsIX6fyx0vefsOlMC9nR078CQhAtWwOOaMhHBcfiyIRiqYCgeZLB3728BHzvOdw9rRwj-XeG7MEcHic9tHiRCDTi15VqB_EtpCnEpu8Paj5vede-Gr-bygSDeUZeF43u_bBcyg2b_8PW1RhLbkVaV0UZB1vVzIvNLc2J38V2XJhpIipc81pseaR73zSnPAqa1nyLX9iAaHg2zQd5-HnnB-TbEm5ewH9C-harbZeLlt7OQ562uJ4Vbd5PN-rfmzNR0PLfzhCpD5V7qtI-TDrTDOq01llibjFOaCSUqk0rzgbHxg1Lb973gp1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=M6DZ2VnCEaDgw69jaRaZmp-86e3r5CMWJm8efMA92CakrTlv-sZFG6Ks6ku2fDd1dXgFzgkOGjFoNaFSFRBtCRabfPnkGXt58F74t_w5WDnfxch3mhhf_k5zOr2x0kRVTznc2rQSr9C80UIgrb_MM1_HTteuts5415nxuHT3nA4ky499XUy8FpsTZpb4Lfrz4igwFsn_sQqv2BNLFc1zwoUjvhzgQv1C8AIQJ17bZOeW5dvU9FomV-js7lUJqrOlvff1qY5tLoswmtIUsH47Je1YApN6B6f24cFlT9jFJ8chy90xS_zrVr7cBFoJDCkWohtNPjaEA5hy9nWxZwHNwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=M6DZ2VnCEaDgw69jaRaZmp-86e3r5CMWJm8efMA92CakrTlv-sZFG6Ks6ku2fDd1dXgFzgkOGjFoNaFSFRBtCRabfPnkGXt58F74t_w5WDnfxch3mhhf_k5zOr2x0kRVTznc2rQSr9C80UIgrb_MM1_HTteuts5415nxuHT3nA4ky499XUy8FpsTZpb4Lfrz4igwFsn_sQqv2BNLFc1zwoUjvhzgQv1C8AIQJ17bZOeW5dvU9FomV-js7lUJqrOlvff1qY5tLoswmtIUsH47Je1YApN6B6f24cFlT9jFJ8chy90xS_zrVr7cBFoJDCkWohtNPjaEA5hy9nWxZwHNwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf-jco0Vjw-ePXlfHFXUouI2p5EMIhhHXWd-Fn7PnRrNrdYe_dQugVGUroPD-QL04uIgybW2RQXazvaHncXpwPUb9mhrMHbQJrsRssjVWb5Ltl7XQQIFEneUdyBW4cJvOoSNDlSPWw4RIHBZXFWX-7oDYuerqAioebWX57NjJHYhZ3dlIxfyyiR46_Pb7oOg-hHa0lXPDy3O6CsijiIiF6rQF4nz2cLjHI9nl5lEpB7N6oQUq4azP2vAfoHGPNnFJDVcEwvtNkxJkBcn5JfhR0QLjAKwC_9JCBsvB3FQBiVEnXsx2Uu6688TWvgIv6Hp13_SJCS4H_ApVy9W3Zkipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgATPeLDXyZHKGbf8cm_uN92SZPCbMrTNzyveDVOrYQhoNUoVKxHiVx9-b37vVErIghkbOcSal7LtnVVpRZsMZwc_j6jEfyaG4D6zvLrMcgH6Shj-_xiZRURX5AhjmN3VpERlFvBBRY2KHOSvB6PNO14UnvzHwrDAVyGQgeOm1oaGwGzmUys4ZXO1RgZ4KDUv6htB7KNcG7cQz11clXs2SnxjIxEEibeghw2BLwVWMzoYwlspvUD_TQUOIK4tue0oJXDbLqaEAPlJ22PIrqrvXd2xPhHpsxizgpkkD5koiK-MmpYy_8ZKxe0xc6wefrDKuZtvrzcPSiq0DY_CgtjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igoeGPcqXdDCmCAWH8yC78UJeE82Ycm3SRrPPWsgchXU44IVENZWW2KQByLHZkrGFrlck8mpHawNoszo1FDm0UfL1KSuuLpdodY7eU7VytA51qHpgFerlZe_zfhDEPKtEEJgzSfGfHk0MngSpmp3Fmm64IuGAbdyNE7ZnXvvKnYXVFr1WQ2PyCeqWA_DpadFr_XiwVvqtTCZ8MxeRQXg5-g7EtNq39bQiOlDem7jyCfOsR0jfe7n1r5eGCM-DFhr_rmoD53BKidy0Z2NUt4luhZxV6qnNO3WCXM_38dwsxTIhsnpwi_Iux7BKgT5m16VUr8HLMaV6yV503GGadsbBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-628UkCy-aDIfcZdZDk7pXekJQGSIHmxPNMyshoGOnjUUUcUztbvx74WyRSzBJgFlUnsh8cuCHjUKcWn0CvUP4ogZgaCf-ce78dkfOw-xqpCzBWGO2WkKsg3Am02OaaT1uiQmTZatEmh8cla21tQNpmpHmfB3FLqfNMZMN23pSWsnJS3FL1FYMKjrYOLLJT_X0RmccSd8zZoKAvXXxP9BREAlIXQiFVK2GsSUTL4jDyEHoc4pIVNKztXl0YV146fjLR7kQhwDW1ODbYIRGSBKvdCMhbi4UteLitVB_pmY8YFeo7MCk5stchaSmz3BajLiDGiA31svOyEdgWI6K3gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqq2g-1dvwbynohz-unzT4toTfpcIJSLeN3-fwPQYz_G2jVAlJqn2siw38PA9wH1v9cZIDraV3QQljCagcGLUiQblxQ028hSEjiCkYy6WJO1z8thzNZU5Uk_x39o2qK5-KfSQ__uBHLgkR0Nt3g23gjLhiX8zRPfXzKessy4vofJIMfsENMTse0QPZxyl7yWCPSNVMumkNF46zUiNbMxrowXl5HMELEp84UNbhVE9SohwoNMGPUJqPVxyjY29_G6UWiBF33OA5vSSz_SQSP-nOC1RV-phcakMDvVxkNp3LUIUTgfemzj7sSOmvPMyk9HrPVNr7h-iFoSe5gFTWpaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEJNLhMMdSWZNd5psvwvqDE7s_4XzHSkRTMp0D9jU3J_KAeG68v0953W3cxGXmFcALmm-imkUndjHznVnII9xRAawNT-sUQBOFPjzVq_cU9pSP4Les_2UcugoP2j9ZG_vAldI7vlhhVAFSwWtN5GyGoSQeuPN9bB3vHQR3hKFcbN0Ht2Q-_m4Cu1ZtMDGdQgWgHNRx5bJa-JqI0-P7iOqB-IHTqPeoMgbTfpnyna1s5FKWWH3YqvH6KBhDP0YOf5SNpShqqlJav6RckudJ1x8woDI3OYXRVYLqkdeAQiyXEv0qAN8NGE3OnU6kpcWQ4LS-02vf3IeDTvCHPkr8Yrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb6pG49yjPp3dvVKMlEcdv4hHsNWjjE1k0TpcQwG1Nbs7nxHaWBEifKgomIIG6T8pGFasosJ3V1ckDtZ8TwnwEUXjB3Iv2KfVRZWwXW1HF5kBT0J8wPbUCBL4fLdFehmnmepaiJs5yCXNGyFNv17eHe3IMXug6cPIGtk0d_42BrNth5vDm3wH0Jlepg11qCpyuvTRdgGtQ1kLSm5dq8SbxHs1F_LJKxvP41l9JXot5b1-_45t7haRn23-8PalSn36vkeI8ruKlx4_Q3L4Q6v69Ir48oBPPz64H-1iTViWFSGnJbHYHV-nRYyxiJlq_oGg2yn2tOeC6KQORAErwnwpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFXAsnbR2UzTMFOW9PcmScGrEXZwnQ6FSQUR5fN9fACt1tYP1OxXpSIqpoLVqxqPAhun9baedxFsLxnjkOMDcVlYEIpwHjrhJ1z-W8dxOnnZzBiwbIzLiGzhyRA1l-ln7arDaLQlI2u5y5DGXp-NpPweU1RbrEwTexsrrVIB8846qyOBgcZQXhMZQEywwzomrNpFDlVOQkGYXjpzBvdY-HgWWdoFd67hJevJaXvn2YaPdmO2Nm6ZGvOkNvX1P9DW_-MC8AOgLxFfYk_ZXOOhYv3uU0BKxKMzLNgTpZBTBiZHwRjIb--ar2bJg_UAr3uvstcnrSfghiGiiu6eDugv0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW1wuqCufKETddfcPuGRqY7_VWt7PuC---lKXktRC57rZ7ihX7Lo7189PoC_jZivVzI73BWAghWne1Dxp1Xgmn8kLKckH_Kj9rEhTJut_vtdXuTcF11sKRxyDSMbtZHVcCFYV3zE9Us1Z9oWfyqEQRveam5j5t-GYNGrBni3YISgCEI8_2caI01Q8oYnVBwQztflSp7zag7C3MWrnRMRf40lzDNJNZRIdPr0K0OuLiWhM7Ii_q-Wl5B5u9OJZhlq9QZCzNZ66EyPQ9totniyQb4VE8H7Ms4xvgjaCn0UAJmKRYiYlXpwlAjyJ0zdNWnZ26-mC8w4FEsdsWuT5LKERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhKT6e23YRvgtjd8f_SiI_L54rV6zfkGRtrUSuOL2gsFYXw4zyJDlBd_OASbEUxNAOUxK0aFBa3VoxMjpvAWRzawWT83AzncmID6bXDFZUIR7LPTVD0cTlutAbLb1EHkR0H1f-4mp-N3WDdZDelzKI3o-HqCfM9fgRz_OHPva1-RsHjQCPZYjvVkl1hV7yXR6qIoXFi7edIfxwiqmGAaMJe8ItJIJncaz5v2T6lgSqkpNvFbtXbNJz7-1X7Qs1L0uvSNGOnKApy8GBYAdz7WhbTu0w0dAD3C9MjG1TgF_OAt2R1g8D9Qgzy8MbkZVezmxaGcSqECOCek4VMPhQbaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=S6R543qCEgNAnuxpexuMZdHF008vB3Fi2DF_blkvT2v_iNKhq2F443xNPuQBtzgvuySyrc4obsf0JQN2-xwdqYtGlqvhh9YLmkVzamgfE69flESu4CALQtG1UD866DN3rTAI2iKGaFjBcymQa2iGmkXK_Z1hveL6ortNbkoQOukUJaHOJOc3XvjCaqBWuSmC16fYoADqG7Kwl2uyWfC7txVDRxyO80DX3BYB2gp7XjqQf8OLHPWGpMBWPCTdS9QogMCK-dqi1Zapule9KFRw1SZ8eUrASBwFdqs8U019kkkCCPAvH2Dm2PZm0Z80VicAcjtG1GWaubG-Mrruk7sXSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=S6R543qCEgNAnuxpexuMZdHF008vB3Fi2DF_blkvT2v_iNKhq2F443xNPuQBtzgvuySyrc4obsf0JQN2-xwdqYtGlqvhh9YLmkVzamgfE69flESu4CALQtG1UD866DN3rTAI2iKGaFjBcymQa2iGmkXK_Z1hveL6ortNbkoQOukUJaHOJOc3XvjCaqBWuSmC16fYoADqG7Kwl2uyWfC7txVDRxyO80DX3BYB2gp7XjqQf8OLHPWGpMBWPCTdS9QogMCK-dqi1Zapule9KFRw1SZ8eUrASBwFdqs8U019kkkCCPAvH2Dm2PZm0Z80VicAcjtG1GWaubG-Mrruk7sXSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=aN88VSiekKwCch1iNVXbN-runD079fBbU_nm4uuz0aaj8Cb8dmiD1lW5Ae11MxUjb0Ag0R2KUYWFpmRqIkcVFF3AInWNaa31-EmGHEE4NH274eQLrzFZGEke1dHw4dES2Ejog2lnDJ8EHCtzTKY53RrsAqs2L3ra0t379xJPfBgVqm7bBrkM2K0syPATJrd_4floVp7nxyU2BipvQE2sDxVR9oq8_mYnadBrAO8ARvAz60pA0myAzGZCf18z9PmyhoMFLQRwJLrMrD59XFei2oIIdrSXwaBCNb7uxDQCdCwXFRn3adBta7ON1zzMIeslGaCIZg9D6xAmpHmq3zo10g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=aN88VSiekKwCch1iNVXbN-runD079fBbU_nm4uuz0aaj8Cb8dmiD1lW5Ae11MxUjb0Ag0R2KUYWFpmRqIkcVFF3AInWNaa31-EmGHEE4NH274eQLrzFZGEke1dHw4dES2Ejog2lnDJ8EHCtzTKY53RrsAqs2L3ra0t379xJPfBgVqm7bBrkM2K0syPATJrd_4floVp7nxyU2BipvQE2sDxVR9oq8_mYnadBrAO8ARvAz60pA0myAzGZCf18z9PmyhoMFLQRwJLrMrD59XFei2oIIdrSXwaBCNb7uxDQCdCwXFRn3adBta7ON1zzMIeslGaCIZg9D6xAmpHmq3zo10g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSYfoNRPVr2DSbnA0QSVKCQ8ASlwU0HiyVX_WxgOq8YJa7V298Cqp4waBaHCxiWCFvis94d1XHiIzXoi6HkTWPi7Suaa1gjSQkZSmKfV4G3MoNATLM5B2vpP95l05mmg5oEjFhX_vOfR9l3CE5LtxabAszJGNy_hlTcRphfZn_TKV8JZg36ID22pu4arh2RgSEUghJZSC3zW7dG3jNxLSTmnEegbiZL1XaMlZnxDzaz3CvDVsqNxUSwcWijZEUzljr4pcD_qAhadpk-u3iAv-HcEKz0LexWf1nE6vtJDF-ZnHrFXB4n4m8tb7nBmqnYqIVw8MulR0hljLs5ebnGb7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6zZpr5VymKZpT-Elchymr1cwtzhW4aRNgyx25YjeOx580lCNth6ovKZVkPS1K7YO3aXIjj5niIACXIJEzPfeUxcE9EPmujn4ncyz7WBJxAkBH1i7mpjzSSQozfTri0af3KJyJy-2Gkl6Cq4NZlJ_pWwveaKYUJ603uOf4z9w-g1wG3bgc0Mn-7hrN3TXRxR297VP0ygCk9DnArxQaWuS6v5ci1WOOL1n_rt9CZnB1O9mUt3ktnHAHBieHIEvgCD_WTUh1noL3D-ROel2k5I9ag1iOq9Jj7DMZEBbqbyRcXizdC69PzujzBHfOdz3_6LA0fKrK236efAFVuVvuCS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkLh5gstd4tjiG-TTTEwxr4-DprRqYWMPExtnLrG0wJliIVO03hPyy5PFbV0_uwMCvRUZKEwhkcgu1ihrbbv55es23dzTqVWE2xNT7wteu83kECGg4pmQuuiML9qHXGZiYWVPzYQUitzTB9Ef3NLoAkhO7e1RjuGiq4D1EwuwtsOL7vXAdm3MmUqra_xXAeHTLJsJT6RSRBzIQOldntvJfcJKO-mttk9wsLexuCUH7Im_Gu1gv9Z7AvemlFRIxDJBXeTfjFdwLgtYQks2QJeAEqOAHzn-xxYrc4CJIioltzaPkM-wtpiZCQwdVwQgtUyXHFG7fvCHtkUHuIeNm_8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=mdDEU3LllF97NobKeuMgfDx6liSj1Qz_OTTh_o7eJmQ9RGq4dfX21tPiCg3DNqlpXCD3lqy54v14G6mXqYJYWtrBa8NOMVdy0PWT9irDpM0qCNqpjxso_5tlvUK9y4dHpJCqEylhkV5eWVInbA9kJtwRVH0sD4zvXYVdzJoyksFX1LG0Sk3KrnyiLRkllq5WSzjdC_NAQ3jS7s5diBiq_-5aZRT_LPQTXoxS7_XiaGASGxA1H5k9ApcayOTVRtvU7ydUyKQPht0I5qjCk36R10PzRK-vviA8BruW-x6r6QPFGGzHbhcgbO4UyheSXCurYbNYyJ4u_Xr9_-hVWU9kEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=mdDEU3LllF97NobKeuMgfDx6liSj1Qz_OTTh_o7eJmQ9RGq4dfX21tPiCg3DNqlpXCD3lqy54v14G6mXqYJYWtrBa8NOMVdy0PWT9irDpM0qCNqpjxso_5tlvUK9y4dHpJCqEylhkV5eWVInbA9kJtwRVH0sD4zvXYVdzJoyksFX1LG0Sk3KrnyiLRkllq5WSzjdC_NAQ3jS7s5diBiq_-5aZRT_LPQTXoxS7_XiaGASGxA1H5k9ApcayOTVRtvU7ydUyKQPht0I5qjCk36R10PzRK-vviA8BruW-x6r6QPFGGzHbhcgbO4UyheSXCurYbNYyJ4u_Xr9_-hVWU9kEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W82hv1niAFp5WyrHdE9QYbMjq-kgxUN_HQEkfPj5ybJwZW-Ssosoa4LZW39etNAiZoNnHs5u9A7Z28Dnx0i4vtxuJuKWr4_BEfrfu0HGqm5rIV4rG1pY01eZ3aAb3_LNQtD4RMe7cvsRxu6qN51BaI3XWPOF6vBiJPRTMfctQN7QOelgH3qfq5QFh7sP2eFG4x0V_wlJutJcxy_hTANQzVtswcc16igoOmJhU6KY-WHz7UCJbVVJ-G5ZuI81kGX6WzAi6LFCtGsTkztH2La3o3opQjneUofM_Il_zNCVX58cWlaz6usYcaA8cVsDDimuFQJzgs5_WpVSuskTLplaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkcznMB8Ou_K_N5p7BaJtBp9WYUyfRbqOXQ5B4DcCFZKEQHvwNEAiXoi4YUUMbCPFNhRTLgW9ioUMZB_wGrsSh7wWuuAe6B-rzi9bCQZSN6-gXy8-KIibPYn2J92oDYUgwOjq2ezO92sHreiyLrXdsKtfNmA9nmPpwIdgacLmvrBbbCi7yDUNf2bYWjx2j3WvlRHgZIlXPL_yiPhhzEIfiHrKCh9CC3xW9NcUM9qMApN-JOHJ35nCzumP7r-RemFY7WqpT_2xnKG4AMnBIdXcdTi_6fk8uTtJZS_EvhFhWn0GbikfN5eT6pXHSGSN-z0715U09q0e4Q3IaLOMPlvWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH50PNTDEa7V0kPgwMglfFvLcpEmkyF2ImMUvdh9Ykykdl5_MfJHajxZrgH5-NYfEQqo2XKT9UdXuMTYqusJxDZ80rmZ1g4xhceCQeOLZ5SxSrGge4ygSJS0ZbCGhoOqMT38bbX-M_MlZb6m9400k-KMDdjXfrc7bWBHJJapV_SDWsZA7pmjuJechxkvvP2ohPaXk2QZL3kMnKTjdpgrKH8IkEWNJ1f4uzzQQZCvVqf_pWuKWZYqFrHT7wYmIB6Swe8iyeX6XMFUPu5WZt-13IAOXknagfAyExonFVRl9ra7wr256CaB_YKwOwgyAwAVO4nGzibpjIfj8S-seAqTnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVV3xAMhL6L6wd0Dc_WXzFHFFvfckEJLdJiCOhLDmYBfMST7zG5YtUIG1FYWx0jsY-ZZarP-hEIWbggZNxbA8RIngzI0exNZpdpc_4-po8RHCFE8YIbYGt3wPFtrD-BI5ETk_EE_uQUn_VW2Be3p6iwuFrWKdyKFMW4LfZTHJR3uc1NXOmkRKay5g6AbJK3ZVEO9Cqbo11N27A-5vP5y8C1F4dZfMmlxifQi-vNWo1AmmROHlaMTV3KsQlcC6bhjQOPro7hnKwIFtlpKjH6JU0vVC1Fn62PGRMpm2FMo42tydG8OhbudZKtpurEpOoQp-4j_zC0BSZTvbe9hROroNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH9AyCwORiKxFVwsVIZw4HjhT6xxaC8FGC6zAa_Q73wfyLv0vdQbf5cYdKgb3oqrhs8w0qyUpSo426gLQXxarGRMdaF2Iljwb7OsabELtF9F2rQJTyBWILSlENQykyCh2WF2Q6l5aRHclpeJ5mtf1qEVV2O8Y_PYfyFfCQ3EtR9sRklatzGNio4ISc6cKzKect56vAX49_25iD4smISfx4PN89ke51EOkIxdchh8IRZDWHK9JGMJK5QkxV5Y-1AQJPvovMywUJlcesqs_KvX0SyqbBwiseipSD9ZidcqmTS85Y_Md7KYolR0UI-kM0mj_AU4CIEWPWXwcpDwuCgsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRvNkw8FeT39KCgyrgQp50QiO_zURQ3TAlg3v_zLEZp2mnHgScjQTxdPscS0JAB8WRL7HKa9n_03ta3CrRQsepyeYNZNsK3qNiZX_KlJw_x4v49a3H0VyLVjf0wcMd-fOtA1pb_hsdb15SQLm7OYg69_tGW2v8PzCAue8cOQpOFzpewqDUdNAhbOp91-cknUOCBXlxq5P4HrmbDRdoE3M7FTzwAN1hRdK5EZJmjDGAt2fNG8Fuf1Z71d-UN9FH-dPQk8X5vCLxUZDNex46MH3c13tQhz17jPH1eUFLItVfJvRb3QhtmS02etinH_K_gl2Bg0RNUqZnfiJWOAxAhY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXVyDjI6sNFF5IiE36B9ApjssRy5ZOXD3QTqDmgjVH8Suaf97aLkH6zHsB7ipEEAjIbIH7NFSBzJOhWOmaZ1Q4HMRyXsLhJ0fuLVvhSer6hqKWIywFKLsgvHsS72lZULO3eZTpNAwzZ7gtUlJgOODHk0Ci8rJGJc0ZwHpJqN-v3bITKC4YyyLm0q-3o8Zm3oNkFxkiP9DHOKV_DKG7nPgvKPwRnIUfo4Y0tWZe2kl9yj0QxXR1hdjEyD5acpeNyhosTdbGn6HhOvWpgYwl7nS7eoYOSWRyQWBDWl18UdJm3AatWhyCU381dQbFFW4QagbIeFvfXTjI_Ac9MPN61ZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4XRE-utYoUj5l827Lh9nVa_Fz1h3pnIN581MGNTlzO6M40RPw-atVkB0Vx-ZiOwYtCcNWfV7WGce3DC4OQsVCWZh9RGvLggMpWRgzgSsF2m7_Vi85XDP5dzYiOksKquoZIzoBumItPwzNpogP0EEYi4rUp13_uEQ8nswCc7YVltFKsRdoikbNptfoz1wxUWReQNdxwiOsMoXXe9Jx30jGE2vWmi0q1fBCNTy_wgholl8OjsvByDpUAgCAwN0oJ5cZW7Bq-TP0OYXiU7waFQrp3GFDj_HXTR140X0TbjT0urb5myj6cSQ7zJbXs-APiIpLutQIZidsi_W3qTIiKMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDPSviWPscNU8rlaigyhAMg9iXfixvzBY_900faNZ2mSA5wb42yV2B7dwM4AU6-68RtC-ToEm81pTS9BX95jlYl4TVAeHMkKHjua3u0LnP3oVocz70Z2GRtybY6yiKq5_kKeYMpi_55gFGKeropE05A1gNiuYtGjRr1TdRR1_oKu9_7qaekhamYyhbzzqqPbOYgBFvK77EHOIOcnhfKmRtBfWuO9Mk-zM3CIwEU8nswmkoN9YqdKgbHoIwffzUtsZu3D9pPA8d33Cl3e7psW9ZYK4bnFkpN4IdNkYA7pxgRLkKYCzdUBAlhHri5t7e3RpgtBTxRdDi5vgxGCJ9VIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZISSFFBRVuW-AK2EITWc9USnYFot7JW8Bk4j716vIp3RJ0QdlsLZJ07U96gIqMnGz3FREQ4G99kkhpXpK5JUvGHf3WhPy8gZW3We8B28CfqVHEBlV4gz-PG1hPUyiKau6c-vEiyZY1DqaqiPnitsZIxNuERCuLOqIkmQSMMTk7L-uzHxtDm8QUv4JFkdXHrN02IeUU2ruQhKZGhu0_3LBWEIDaD5tQ-HsXTBiurYN0be0g100t0V_bF82WCK7EgOPHbInuSDx48vIlMHoF7ix7GlwcXU-cBzA65fNQT4LZXMTPVksV0xYGjkVSaHNcyQV8_9x--THeh2Fn5eaQCMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5hW9qN-9ti9Hxr_9KG5i9rB2Hrt7qjsekoG6BHsWKlYiP9wS4AziaTHNtdXHhpBhT-Gheq15Kfw97O8qD7zeIq0YNlk4cm065Vl6NjhTW4vw0hOI05XCpictkERqAgvsxDH1tw3vRQ-HtMFrAT33RTbivSVFleRATHMlM8RtxU_XzslnfEaDjtbcy-UmIt6ZR6La5FISYtBMKrwyUcfS5B4On0jPbF6jnUG2DMQfDOBL3ubYXs3bGTp_AaELID1Zx-St3ZPhmMm9k1clnU9G7WaO_EXlstAxZQOYGdgUhGzK1ZujPAq_BHcfxcQ1PU41zIWnHD18_Sw3xv4HgZ7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=NOdSdh0ClLgsJUS9vpUhRDg3qEgymuiPt1QmY9_tLFfptAy4DjvOhKf1URzf3CbgP3cOOmncyt91p-8G8TzoAZrq5RBC4s3Rn8_nh6N8-IMFzDuYlvD262UexUw5eeN8LDZLnVYhWj69DlesNntVvAlFZIbjCfxlRBxW7T4Hq9w79E7dtCHfmTzYrjEUPwU01wyLJ-rYXVPch2O0mZ5rI2qqXvmRV7XXV1AQbYwjrFawPZzLEsa7arht7MeRgh4JrkiKKMQwdGtetb3_2AmvfmZS4dC3I2SkJnbnxG2827SCca1uteiQgqZy5Ao2tOkLe_EAc0Dt2qsMY9wMlYS_WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=NOdSdh0ClLgsJUS9vpUhRDg3qEgymuiPt1QmY9_tLFfptAy4DjvOhKf1URzf3CbgP3cOOmncyt91p-8G8TzoAZrq5RBC4s3Rn8_nh6N8-IMFzDuYlvD262UexUw5eeN8LDZLnVYhWj69DlesNntVvAlFZIbjCfxlRBxW7T4Hq9w79E7dtCHfmTzYrjEUPwU01wyLJ-rYXVPch2O0mZ5rI2qqXvmRV7XXV1AQbYwjrFawPZzLEsa7arht7MeRgh4JrkiKKMQwdGtetb3_2AmvfmZS4dC3I2SkJnbnxG2827SCca1uteiQgqZy5Ao2tOkLe_EAc0Dt2qsMY9wMlYS_WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=hvTTG7nQJ9hSg7Yik5uyP6re81xb7DQASAWXadJv7g434vz9MW2wRNeZ-jpsgwoKwCp46V6es6MZLX9VKcA3oUF-bR-WeokqBsPC6cIJDQGPHtSb6-LBw9vJ5tHMtZWAP99fjkB2JdI7XOzNq_1Q_6yImC2_hdqfzaRew1b2XIYC-_BsyrYJ9eSdR8SmwfeTgTReeptUw2AdaY66Jd_D9E6xLCKYHWnPiCfGGJbLPPV8FAG16z6CT63QoWv9FEO5YnWiEw9xBBWPv7OduRiZ6FOthzJRqsq8RJMIkKLlH43MteCxGWJBQdTOxA-188ycbPpYi3JomYs7TcD0cRzIaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=hvTTG7nQJ9hSg7Yik5uyP6re81xb7DQASAWXadJv7g434vz9MW2wRNeZ-jpsgwoKwCp46V6es6MZLX9VKcA3oUF-bR-WeokqBsPC6cIJDQGPHtSb6-LBw9vJ5tHMtZWAP99fjkB2JdI7XOzNq_1Q_6yImC2_hdqfzaRew1b2XIYC-_BsyrYJ9eSdR8SmwfeTgTReeptUw2AdaY66Jd_D9E6xLCKYHWnPiCfGGJbLPPV8FAG16z6CT63QoWv9FEO5YnWiEw9xBBWPv7OduRiZ6FOthzJRqsq8RJMIkKLlH43MteCxGWJBQdTOxA-188ycbPpYi3JomYs7TcD0cRzIaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=AGmT7J4oUfCA9rGjPUVBlejjaIa47FbWP2pcdx_ZFLEH9Mj6GkT36KhdnWU_BdpjN1VSCCko3SmgYEArRiTI5telgSvKjJ3-z3YO5BWZ4Jdi87waWOvbA1ZNO7JPotIiXr4MPhPEJNnP6FlXrw8hK96q0QkoWY5YDArO9nT5pcmN9YoYRA-I1m85dFFpQFfzvZ3AGyCAFCfxQJM2I-ksxiSmWGjt_YJKUrNaGc7AQ-IrVCWcOVZ_zFk39OAmrJqhunL4jp8nLxL9nxyHs4fAdPDAjEQ19NsUSHhQGSHFrUCn8eq4iUrOnHfx9y5BKYHUjGsSKeSZdlarJPBAk5My4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=AGmT7J4oUfCA9rGjPUVBlejjaIa47FbWP2pcdx_ZFLEH9Mj6GkT36KhdnWU_BdpjN1VSCCko3SmgYEArRiTI5telgSvKjJ3-z3YO5BWZ4Jdi87waWOvbA1ZNO7JPotIiXr4MPhPEJNnP6FlXrw8hK96q0QkoWY5YDArO9nT5pcmN9YoYRA-I1m85dFFpQFfzvZ3AGyCAFCfxQJM2I-ksxiSmWGjt_YJKUrNaGc7AQ-IrVCWcOVZ_zFk39OAmrJqhunL4jp8nLxL9nxyHs4fAdPDAjEQ19NsUSHhQGSHFrUCn8eq4iUrOnHfx9y5BKYHUjGsSKeSZdlarJPBAk5My4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2Pqe3OYkhkK_MAywDHP3tPIvWgfmZI9mQSzrZ2_sI57IJ_djMuQJU12kDz3AtJYQUWXFMFmWM4NNIK-gFXuOtRdtF4O7NBpuc_RhYmHwiMzgoZN1KAbLGYD5gG3LaaFq8MDyacdQyDY0sCv2Rwpg129422KxOhOE5C9_b3W1Ojbeq7JSW2Prlp1CTIrnZjP6FnUAISqNOjQYuhWpgErh2mcGdBJh6UDO8Lcv6c9C6QW6SoiCN96-m29vcVfrFh6PjkJk7O6Flib8NcicF2WgVbN6wzk_UGH4_0X7PqA3pmBp4o20Y-rOFEsdt72qOjeg1YPaHz4aaJDPnLPLpscng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=FW73b4zKqnioXYpEdpBObOErOI_B66pEhSSoPVtGE5q_8P9Xf1XU4_lcbBeglE-IokT14NNkbBMHR80uSUzvcXNPEZTOMT2cTbSND8d5qtPu5DXgrhyP-Vit21XOdkwVuJLtKxgEpmq_x1NnfIm6-LlUsvaBNy780QTkIFvYtINJjBIB_VCgnooE1hLwo23bmJTsRktz0uE-wLz_GoFek5lYokKdSJr0mCUTsFIhjhf0fxMX00MZ06mqG_k114EjHfSnTgYWSeUky9z-UOr50T2Fu6q7dP5JPyOTwODCZN70MfsXLFzoVQWUB3DplvQz78JHCU1vO1NvdRMvLNvXgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=FW73b4zKqnioXYpEdpBObOErOI_B66pEhSSoPVtGE5q_8P9Xf1XU4_lcbBeglE-IokT14NNkbBMHR80uSUzvcXNPEZTOMT2cTbSND8d5qtPu5DXgrhyP-Vit21XOdkwVuJLtKxgEpmq_x1NnfIm6-LlUsvaBNy780QTkIFvYtINJjBIB_VCgnooE1hLwo23bmJTsRktz0uE-wLz_GoFek5lYokKdSJr0mCUTsFIhjhf0fxMX00MZ06mqG_k114EjHfSnTgYWSeUky9z-UOr50T2Fu6q7dP5JPyOTwODCZN70MfsXLFzoVQWUB3DplvQz78JHCU1vO1NvdRMvLNvXgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=lW_miMqi6PB7ueJnzGuBRZstuLRlrMlveJwyo29U7wmXSRpEHOA6yVupNLobiGlEAX4mApUmz1OF2UBqilrM3ORWL9B1FW9lN4mvARSCmliQj3knph3_7KQZ3biITmoOSe8QV-HerQ3OBxFEoWT8ZMGIYLHXmU8rgxPu_7ssDrVM1korhDILxiRF8eBKK9cAFcBl65CAKjosaatuyQd9m-KlI3wURAn1DUvUoe7bQv1GJBVNjATQ8qpLIza6iGhcRJSXC4z6STSECPKZwpCWYtlWrM1INLNQ4zERaG7tRuvlMF9JDn0dj321viGSozJFz2vrJlF57NNXiVYVcdtcKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=lW_miMqi6PB7ueJnzGuBRZstuLRlrMlveJwyo29U7wmXSRpEHOA6yVupNLobiGlEAX4mApUmz1OF2UBqilrM3ORWL9B1FW9lN4mvARSCmliQj3knph3_7KQZ3biITmoOSe8QV-HerQ3OBxFEoWT8ZMGIYLHXmU8rgxPu_7ssDrVM1korhDILxiRF8eBKK9cAFcBl65CAKjosaatuyQd9m-KlI3wURAn1DUvUoe7bQv1GJBVNjATQ8qpLIza6iGhcRJSXC4z6STSECPKZwpCWYtlWrM1INLNQ4zERaG7tRuvlMF9JDn0dj321viGSozJFz2vrJlF57NNXiVYVcdtcKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIRYFDZd-ebtoqzRE9WTcY50HTq4Ngp7HszvFMkuPJWV87hut_S0hF_akRgQUV8V24Z9ndiK_VifqPUrDbzCzTv1Td9RHICGNUd59S53oak0qf30X46jyHQ0xH_MR_MxgOrM2Ia6TvH7XyxbMUqCPw_wA9jTC0ID5-T3HjHZWmBGi1Li7I-IpBx7aebesboCtl1_umD0ekj9RmGedsjY-VZHaEMebsYA-jrMPBUqhpCVCitun32m4IUDul5EQ4mFCmQp8rg-N3ylQV3lqgarzg2ac2x1TH0dGuTIMsTtgUvhWjvMttTn0candi3JEs3GuxzOfzBcdAJXyU-3zkNIhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcwfQoSSGnOETthMBErjx0FXl1_zcRYhUohdSiIoVkcXMOn9YzHO9WofTgbRCIpUK1T4l8ASr8r_zL_6oALkHk-13Sx_XblDWO_QB89o6qWh0DoWqPnpmMaOk6oLQgSadhEqoDupZlDIax7Ivn9Qp_4ceDaznlKAqJZSO1ti9o3HIBvq376KfDFQGYV-xGvGsBGMQqsbaS2_RWVHsrvx-o_mAR2qLJzudDnfpDW1q_UhvTCwGyJRK66tXZOhgRf6bMIqZ7agDzJjLIhlkRO3tI3kUQE91KFmI-_F6hjMWC43LOGF_eYBShuirdJXH0lUB-436K1l82TAuTmvHWnzlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j80D_3bEIFyawSwUsYZARBhuOynfIz0e-Y8H6nuoGOBHO-wsZq85iwHQhxJs0kIHZjlRDsFo58A-DjhknkxF664ZHFu1W6MzSFmKpwmbP9UrBHpmkRahF9oFvC8KZLFrdaBtlS0DTYFQrZNc_p-_DYgo2A5jLihAfh99b4GYR7FTvW8r0knH3eDSpbc2_98ALHT9xKcJ5NoZpFMCJOrXbN7Cc12lJkOFR_u06Qr_JmSqNQZ0GNXrF_5CS81A0MceKgnBcg6sMt9myBr3kQSrk0rRqmidaDB0dBQ2IsHO_c6MLu_wdbBu8XxR6SIgz81zf-M4nacPV79p3whREPZm5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPCu2dIb-k-HJLId3vuqmsQxhb0J-tm7USdezuEsL9JyPp5T_IJsEUrgC3kRJ3e_srzi5hL2eGB44TKxnBTuKDFHSW2PHur9csaCqrVwd5BC8j3-Zz_Avel6an34fVes0xNXPaX6v1MfOefVoNJHOs6JgNLB6gidyoxviHaRBVYoUskIxoJMaAin2ZpXcrIRrhly2Li7iYwaOaVZAu_UfiBiRjAZQlF8_Xpz-pt1gWzN6oTwk-oR4rphAKyADY9quS8NI8MZLPD-T_IRfri2RGQjQwTl7OwgoM4NKcK0BriN5YDSRpX4NTIBjrY2hbTlrw8cXCyOvuXLd3wjRkYwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqAUJJRNClbawVHhqkDx6Xoq7WnHCS79KklWKgqxv4vtf4d8APp2gXtHQ2ecgc-uv44K4Rm2C_SS8Es0Fzec4E-KN4CjmGyqj71gRyVcUnOPf0ybcZY1KEK_8Brtr-aB2yVNjSxqMG25EO8QdrSQgBRH5vCr3eP98wvyGszX8UnMASAuXXlyVVjcBtAbYfPbm6kOL4arIeMvzhG0PSLaYSCqVdRaqeKD55GcktQFqFTi170HKMJ5gBdAXzn6vpJp7RqXx3LZANvWw9_6tk88CieCyt45JPxiX9YTgxqjxYiPY6SNoBIvYeyYCqr1C9HB2Wa7UEfY4motr015f1muzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQ9PV0addHkTThzoT5h6tv57_z4ApvIiuM4_ZsKHlNIy-_LeLOk5LAyG7b7eMcb0Hm9-2J9qUoA-iz6IgkyNH-AV0S583yrDuivqnnnXDJ2vJdtz4237yC6b8pR-8I8xTGkdGK-YU3bKN3NYLZ5xDe_3pHG8vHGDJs145wlzLJDDwrYaYTMr4Jin4tzAROP8z49fp2g001rjya7HyUWSEF4PyyZxLhi--6BdmiyEYf8fi7n9WtG4pbSB5JTTgxJ-1WctoR8e4V0MQMZsCPk8RHellSI1XmZf4sYACT9EAMP-_4LulMCuCKCY1zXGQ-0M8--JuhvZtjisGYTSLaRVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QByeKoCaaZ4ORathhqLO2n9Ujl-AxV_ii795Haq7JnXzg5orvl9kc8k3wEQlCBHcJp5NMsdwJOOSrgWPhvgDSbNCWpa3Qpg9ebolJ8YM6DVTo6S6NT1IEBnHiT7j2AZLUANUDAbLiEWOb56Dwh1NswSF-IgBN66its525V7T6S4Pq0gPc1oZQiGS4DICF8TQD_aPZMCyO5qxiI1C-HzX6Y7Q3zSfGw9qBm4SUvJ8vCQ-QGDJRoHX6KwbEC4cOrzFCUG5ZeXchHvNu-AxQfaN348l1pwH9xICUnWzc7hZPmxxofpZneTOLT8NN4KqxzdCRE9uTjzxBPIXOzbMhteEPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=rsQN6L9_ka2vHYENNveeskjytbpAPmeJ0_cx5od6xj_8KYrwkoIiDpgSCGuUonprglgRDwOPBGq4Z4F_qh6MoIHLrqyhed_0aen-CTBbgpvG7hxRM84drmT-5Ef2M4B9hJ8f8sVH4eahq4Np48DlCUGkhWVP_3LiU2nME0Sz3ZoHPwdNcbgyLsLlPFXgHVsRJRICGS0CU6jE6A7_7e-cysFoizHQF4g3nAWoW-2AygL8U1tjL-aYFZQ-yp2-MPhm4p7HYLyN6-MontR2xt7w297OxxM_2rO4gh4Ol7iBn4GcVmQ0fVAEiweYloKxN6V0uFxparK1Sj02VXkdPHc4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=rsQN6L9_ka2vHYENNveeskjytbpAPmeJ0_cx5od6xj_8KYrwkoIiDpgSCGuUonprglgRDwOPBGq4Z4F_qh6MoIHLrqyhed_0aen-CTBbgpvG7hxRM84drmT-5Ef2M4B9hJ8f8sVH4eahq4Np48DlCUGkhWVP_3LiU2nME0Sz3ZoHPwdNcbgyLsLlPFXgHVsRJRICGS0CU6jE6A7_7e-cysFoizHQF4g3nAWoW-2AygL8U1tjL-aYFZQ-yp2-MPhm4p7HYLyN6-MontR2xt7w297OxxM_2rO4gh4Ol7iBn4GcVmQ0fVAEiweYloKxN6V0uFxparK1Sj02VXkdPHc4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlB4GSCBQV6cxfHZHqN3CwcYNRhXkCBbvk8LHQQ3CEVYL7BFqylGdjgBGDJ5nxJmY7K4jS3iBiK-uXb7ce-6MgyeQAX64-bhjT5NoJ2RgDaUXUj8ct67HoXMG-Mcgy0SBHvCTIlm3oi71lLgtSA-UKH5GgzIG8B3SyJqjv3gFNw67LZmBBAgaQDNaRk0ZSf-wC0ZVuu-AY3u11kiAzLpFb4TvVTuUjENHL3xwl9g1Vxpav0jmyWf_cCGjzg8IdAoWKqBmGd8jtBPBXXK3KVVTOT3ZCU-0bgMEbI0Rysc_uD3LeAQ2EoTuGRQ8IVe2U0hlq8qui1_pHecGGvv2TccWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3vhXkFTHU5Ac3JgTMSNj_y30_FjIRz-nNcv8wp4VluLTA810OI0i3ORBLbFNXTx68j8aRDAn3aC5qgVGxtpkaQx2uTDuL8jOCXYsuwTLiVD8OXGGughR8nd4u8iyiWzwEpNFCINz4w3Fdbxu6TQ_9inE83BIRRAm9OElECPcd--9CP45a-TxIIEXhsAh_8tD3MXLj0SktP399hCjX0c1nQaGtlLm7SM8SpjjOP_KTKCzGked32KTy6v8wUYGjZrjAyv2iRk8gFxj1tI0l1RLuREbIaJlpO5DVA6J1cFDtNv13NopaFo90_uZzis_e2BLgaI7X5kMcSgyDCb0Zb1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGB8FFmyjNt2uTSItmK1OekrL086R9XEhoFYiA6oEsx23YD_Pzubnh_439DpuQDvxU50jFOGQ8AgNxIyd9gBG-8E9lvrFh6_NwLHvucnI9iVMAR90nk8h2P1PaPAyapxyCkhfd__6mpNgLTFsIrE9b0f5KFvSYtn4TNycJD9xxPRGb1v9osrnbrahbcO_ju1jKvHPnldig9IqfhAx1s1gnSEmgfJf77tv1RvZTfmTQSNerv5W_PVehrCFthdLzohnD3Y1RMMT-JOML-fVhtDVag-0ELY9Oau3NUlKw6Z0IcgEBncEWtnQq1XvKMdB9B2KrB9HW84MLmCkEOcUujbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEQEE9nuwHIp2DXQHZAfSh1C_Vrjm_f_idHLLbrCV7HOaCUO9sIDKVKla1LrAL-I7b28o3fF2h0aLMXb9Rdg1nI5StPcmVg8kFuBcLhGyMsibO0ulu7dQRQzLUNacLD8uy77rGY15d2MTu6vsF8oQH3IoTKxlJGsUER3GKCOqxO2NraYiuUAxFXFo6uhs0Io-SvIaDmVcUsBdjPDbeM0s-c7DhuTed-ZKrRpdXTOkW8kuVo9ghjwgdjQD31ilcEj70o-JRFlAgiawTbG20HQCccql7bPlc42vfYp3XoB5SOy-CqF6lndi4irESn2bzQs0aXNJBSX5hdnD-B8YjVhDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=Aie8o-N5LSfryGhzZ19hFCj4lPzvkGkXOEZJSuPIuNnwSrpZE5_-gRt0Rt_n1Smx1iN3AyCntZfTTZ8z2Oote8u6cy-QjKDecRVpnvXCYVN0uKYIgNKGGTbuUfGNqPXQLnreFbof2tWCP_Z4D9aaDqmP7Y4wCrq_bNQ19UY0JPe9lR18-GydFXORk59ijtxk3Y3P3FDKik6QjJsOmZ-qgKf2rWg4Aa9cCnGTVMu9DH_yiIBPqj-OBotYn-GVChLOAPPUZSrxUnoDHF1Lc9VSummrvKPXpGe-2nDCL1EsMpTKLW8dXaAynxIitP8pbe6TrO78eSc1pO84Pl6JwAL7Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=Aie8o-N5LSfryGhzZ19hFCj4lPzvkGkXOEZJSuPIuNnwSrpZE5_-gRt0Rt_n1Smx1iN3AyCntZfTTZ8z2Oote8u6cy-QjKDecRVpnvXCYVN0uKYIgNKGGTbuUfGNqPXQLnreFbof2tWCP_Z4D9aaDqmP7Y4wCrq_bNQ19UY0JPe9lR18-GydFXORk59ijtxk3Y3P3FDKik6QjJsOmZ-qgKf2rWg4Aa9cCnGTVMu9DH_yiIBPqj-OBotYn-GVChLOAPPUZSrxUnoDHF1Lc9VSummrvKPXpGe-2nDCL1EsMpTKLW8dXaAynxIitP8pbe6TrO78eSc1pO84Pl6JwAL7Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
