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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 14:04:32</div>
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
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2eq_AYHEmyGM-t_GYmfSql95uMhnBXd6eA8lfjmuRJ0S9IpYaJrKnsDF8Qb_P_DlU24goPy54oLm0mYmRRs2WhHRlc1r2-jzbpNLdeDRER1DPFgeKLrrqq9NhLt8V14Cxyjh5ZQ3Xf_rt1Qjy329fgY04VTxPaG397JLoKxc6uY0NK0dogN_CRyckU-m2p-3xHbF9WxAN5FgFnxMLsoDxTtijscmPEYhieyhtogDpdvbZv5pYH1R_n-ka7oaC2mXVSv6BdxH8F2np1_AO14syTt53AjZ5QxjxIVRscqJ-DZxcVYZW1yw4t7Ro2I9Nmz8rfmyZiXJzFEwMPpuX2lbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0qrPiYNKc01fZhSOtfSMkRAL1mDOFMCQ2oVoBujjzyAoaP7jkEnptWTHfga2NSFlUC5Sb5_gkkOEt_Syur11gZm05895M0VsSzzKAuV8UGa_VWQeAGUbx9pW8VJy1r0mmi0PiF3BDlnnEFHJB5iDpVIRXJyhoeHtuDOOVk0sUe7bVaP8dbOZkE9T_dK7_HSOtR_5xZReUUvKW9glgqIJ0lNUhg4zDmwOKM3-Ad8PGpG3k7sK6SnGDZUKyFxXTCDQ3mpjSuJcsRHEj38TjpsnO6H4q3131S0-BbzIqkfWkyDbr_cgZAENSyF61tTqa6Vg09xMDVc7S5z0ANYI4peNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDV4NmIBTU8-gdY0RKnCAzvjiXx28oJBnnip31C4OiSDTTEwOUNGVexRZD9_QG5jkK45saUvQEi4rOHQPQtVQpNJUQkx59kMKMpcZicz2pB4m623MpjDFgcWjdVId443VWo4UH8eL8Cf1VerINlh52dajLa1kR1ebc-4sCifnv4iEWiIR1ubjmIEi2a8UGqhL68chcldMMCahxPjqoC5K0CRmuJ57gHCAtedacevPwVZcp8CP_qu79tkxeDj9gjh3GSHkelKkgvjPH2Qhs496S61ikIh5yMCfCspk-6AfP9rw59F_YqTu4tdJanyY2BDMbONHNHo-hGpKMvUrfVJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBDF1oewFHdmY2bFPLROZ5Pft52CwEgHQo2KELE6Vwtqrhcg3BTSMR2_ALLPsS-wVmiNWyC_CkhSOmiz-aRtiPaGc3CcrkS1XTxBUYm_3OJ10dUESlgqHH0lNwzrA-OlaEDXwI0Vo9aYnl8b1l8-QuzGDkcLl5LKo92486sWubBx0EiFFe999esXmWyBOssB6YwabMV5TqhXgYbeBazMVeCGbs34V9JtyI8i_U0wjdNnsoKomQY2X41p5rP7TPNFnwlXQeXDs85eIeb7scpDn0a3Ms4jF5BYEJyt7VY1zb7qedcvxMkP00LqTJUV-gw2BXamUgwiyIM4Oqp2BdvXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cla1X7EnM2vgYNXhxoVWftOTnxDfTYErL_0E1bMH8h9L8UFktuPk0NqRhpeLhil5WJs9X65s5MhqGNxSdI8AkBaqLSzO0bS5v1ZlONehPl4Tm-qypaag7lKEciOMC2xKybRkbk8jTMyJpgnfJEtyu2AoyY-9nto8cz5Hx5Rrtv6rjnhN7_pafDkNcKS2GDpoJoE66QxBBld8l2B3VP900rabW69D1TvR1ynnTTpE_QhtLEQW09ZSWWna1JeQcngiFr8RPhVr9t4WWBMRP0gNtknRQrbilat9DzaQ1tu2QlpLL1UM9JTyKXlCO3uV-xb8vadK91_EYzPG0nkXeZ_MOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPKvEK4cjB6ur_6M9aekCBckrcJ22cHU0PmxM2_oifuYkZvOO7ZaIS98rswfm32qunX-rJonYvMgzsqR2IYxjY4nlWkV6_9aCf7lgl4HjwYhrW18T1VKqD8gQkCY7HhBFoQY7RxTN3PCnjOv0HsnRm-RRQ0wWnXwmsv3cMqbx40TicEgPU6O4FGgWXd8E9nmurKd52rZuTRBQWwm1AehZx6DG1pWuzNYKSGZOD9Hj1wihTVXJU7tUkd_l_eMoTcvUxuimTr9CxP1iHnjjgqpFXqto15vOayksNBX7uUcYY_azMtDmhTj8H_Z4blf8Lcxq5B_rZXthAJ96vmUH3ndog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw8hCPlWTLHpgVMfZiKHgPIugUEQ7gyIQZP9xgqu3GSnT_ZgmoxCsR1lMDwVlNC0lAKNvZKCw5AxurK9GkjWsuDJaFrrO_CwSBBBp98NLX2uLOmLGBjCNdkaqLQzpTOzoYIWRtrdCNHSKR1miGBK1tE8GHRxj3aT_jxxeWPwpBD8chi4L3lXmeifV2QyLiKnv7PB-PZbKg91dZEZ0kro0irSzQ0YSYVIEV75S2iSOICee3XcU4FDR7weDIusxFJiYOCdFbFu3bSpKjoPI1Bk1CiNSauc_iWSXnGfaVYipdKWbJ4GscM8fBGD-MxBjmXEf4N_hNT9CVHYTCv3k0Fqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StdbKNy2NYED09oUAj1exNe3bpmDbOQN8a2r_G_HYG14Q67H9sCdm2biYTTo_9AmCa5BRw-u__I0xuSYEB9pY1JZtQ0mx-8KXQcOBEjNFZzambSVsKCNsjZwhcyqh8U7K79OxOpppgMBLYJGXAjs6h-qqVr23USPmWpJmiRK8fsrRx5WkndKhiSnPwjj0PM3Ojusq2iXwoHwcED9ulmEj5S9XfwxhDL-QqMAFqDz6Z86OEw7wx0bcjpC6D8GUc_8rbMYZ4eISZC8p3u0ex6tYtXmecJHWT4vzxAFMhQA3lMbvhTMezgccWAnThOOemmp1A0B_69IawIPEH3spN0i-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0YdZm_XlwtWGvjqLSxs7OoJSB3FiMlFyB4cL33Sy9hkqCa_5UDWq6b3KG8doeaVdlX3vJl6LKyW1n7oi4TYsPA4-7KzeKgAMYDcoMaU0pWP-vjrUxgUTH4oobMYAuwIo4jreQ_NqjOF9XgpGqKn6NJBHQYQCNA00Z3iI8fIduKta1rilw_pWyWvhyG0kMG9LfHWTT1ma8cIUEui_gajpbKwTrKjjCe7X6z8_zMobOlIH5lwqYOitCKrnnmMl2UNCzA3EJwuFqDsenFeakJi80yBa-I3CYLLTdrhTEEbOAut3uy4ziR7sUbkvnKPHiwPHeDYTcxxO7OrfnsrMBENog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F972b6kBBj53eXauYVRPdxzlZ9gdbhHJrVqtCufF2KqpS0hnBLOkB6tlhY3in-2E2tokB1pv1EElp4tD6zR_CkJXnqrl1HMfyRfucPVsuxzIhevWXbDtflVbCX49VMlg1tKnIHYxjNHvCXxWtM7SEJebAe4Ljw38VUFRb4HBaONUUPkkF09bIQggiSgpKpG_v0IUNVIMeF2RCdqYwF0GLFx-cFtB55p0kz2d6QPpzn2Wf4Dt4iwvuePdOlMBgzbFzMOzuMu_YwLZ0eJ15JRtLEBjVTmMUyrCKYIihsyc_PzLXjm5nWqULOVZePX0-ms22OMZhb7mFJeHEd9gVXTj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfPLNmeBO1Zk-llTc0d8SHIqQ00nwDbeuFYQ9kT4cRRjs40Ya4pgNr8Jc718YGubdtJlTkE95lH0K7jdOzpo4Xb2yjwFmRPHCsuZ08_ov0pzt6jVfy8cjHiwUIsP7QVYzf8cod5oiytL80vwtcNVsIZh-jnAHTHOrCJTAQFrGP972ufH-z-QQQKb-LfLEijd6UqPq7bb5J_Wi6NZvjtwekyXgmIVfy1kMLM29PPrNkGMctP1_ThPTlA5RuBv7iJfnPEGQA9dX4cEuJmJK9i9y4loAryJ9Zldtz7LoXUxe_yRWobxiWXTrfB7g4gTHSsNcIC18CM4pW6-r2PU8_tSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=SEXCMWBmi4vR3tTHLNHsh8CX3-K3zN9oeAwH1ldh1L4jKxtgBbukExqiDUdMfuQ7V59gOxQP6Oui6bnG2jFKyXxZNmTLDZSZOvKxEuRh8u90a8Gb_T80R-7wYexVVzMKFAwOA2Wn7SSAjz7j_usWOHpjdvgEIoKPeFCMvxdsd0rR9WRkeT6aXCSxDKg8FmRBoUXtQkIXL4eiJP7ZYITGiANXmvRrGilUM9LcDZNBMLqIPyHPE3IkMIW45eXKWP5afzI20RNsXEdLNgtS8luljKyVIeUklUq6W-OyuYOvz0jvwBDIoU4BbnPxRiGzAUy5PpX1-Ymha7vb9UdbClHqtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=SEXCMWBmi4vR3tTHLNHsh8CX3-K3zN9oeAwH1ldh1L4jKxtgBbukExqiDUdMfuQ7V59gOxQP6Oui6bnG2jFKyXxZNmTLDZSZOvKxEuRh8u90a8Gb_T80R-7wYexVVzMKFAwOA2Wn7SSAjz7j_usWOHpjdvgEIoKPeFCMvxdsd0rR9WRkeT6aXCSxDKg8FmRBoUXtQkIXL4eiJP7ZYITGiANXmvRrGilUM9LcDZNBMLqIPyHPE3IkMIW45eXKWP5afzI20RNsXEdLNgtS8luljKyVIeUklUq6W-OyuYOvz0jvwBDIoU4BbnPxRiGzAUy5PpX1-Ymha7vb9UdbClHqtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=km684lZDQggV3QtiCSgCKl27QOCgkIJWOFTjD-e3f8WH3rapV_AIFSfBp94j4WKegAdAQA3Fry2vyTlOF6k_R-M44sHa4x0LXJRHehA_BSdbxlhSuK9AfDYxrfI-5uYG03a-myOwRXpJG9A9OQdNDm6wQaLKXvt2yYd_abyzuMG4LIcmc-AJvK-Fco__gP8302QvrPmwEJ3NQYiWSYLl8_9FDYUmRbSHYeML_BkgIIMmdWSe3IuNOjjByen6-cSHT7V7cBpRx852Nk0VOHnwxljvW39syvnD5-G7XRr-7lxDWe7ApPV7RWYQNTa9bbsjUH54Uda031VIOm2XXg5zSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=km684lZDQggV3QtiCSgCKl27QOCgkIJWOFTjD-e3f8WH3rapV_AIFSfBp94j4WKegAdAQA3Fry2vyTlOF6k_R-M44sHa4x0LXJRHehA_BSdbxlhSuK9AfDYxrfI-5uYG03a-myOwRXpJG9A9OQdNDm6wQaLKXvt2yYd_abyzuMG4LIcmc-AJvK-Fco__gP8302QvrPmwEJ3NQYiWSYLl8_9FDYUmRbSHYeML_BkgIIMmdWSe3IuNOjjByen6-cSHT7V7cBpRx852Nk0VOHnwxljvW39syvnD5-G7XRr-7lxDWe7ApPV7RWYQNTa9bbsjUH54Uda031VIOm2XXg5zSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrqW_AAYmu-Y1CBS4P-AIgMLP_Zs2Qs7v5F17mtZzOIylAoB9g4uPR-lsQyDgvFR40McghxZqOUV6-2xKgMwvcfD8panXSXmZS7abrED9JyYonX5UAPda2E2XKXFNM1R5JhVNFqI8nfulEGzqN1mflyt1DgZ5Ra8dfClf1KWUdxrEPaPKVs7MFThomTCpnBzNWDw1rhzQu93XRmgEF5JDiT3K7Jq2OnGKCx5EHCsCbti0Yo0N86tfhDS-aFSr0IwVhY3WN1xoi8gBFLcqLtByQ_mgSLuGS3_hlYXqF32NBmILVQjvPJYbu4DS2JtSIhYUl8bpbDq7eQ1f8ggkkE5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkSuGQLYbFMIP8nzmFPFGgA5N26mdW5xsHmM6Voz4l4hRuyg3-weEIiwPfq3ztmIZlusaPgpS8pZ2WQhQ63ULEIxZY7isYKKFh1wLhMz7qmKv_ZjBF0uGFvcobt8pIGHzZwsKzQbFFCnZlwakAB0_zfBXwiuO7EzBY7O6gcRJAq-7aDdKcLkGzfoCe6bysm8Tczje0vNLfMyuAFieElKq4ZAmN_p6goOOXnVZjY0fcSgLRqkfjsKZzFNnqvHjkZMzN4PiQwJNHM2dhT6ZVR4FllNg7jdCwIln9SiFdaRGTtmYaf6Zffq6xFifB1jSqt8-b1B-PNmA1LozcEVd8jnWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=ch0KcWTXlVt-61CPDXghz4Ui2qqauOknwhOOnnK3AT1sM0WeA4lCgiJEy-ZdK_TbxnHUX2p6ZrDVgY6Zx2UwY8ebzKg8WvKTpEAgxrBhtfiSmXxptQF1zHOjJ4joaGwZqQNG_Nr_p_Jqb8-RS2Eajdbkwp6aShR806kdfeJ_1vIXENtGHgeJIke0u1Rrwic0NO4CB7fGfGNg34JkbpxrFITPYoaGDvWkCFjKPvbAn_WqUa8OXh6e-O8zNVZPvdkg_EOo8pJ2oCu6b3LJ1Bu-FvPlWGkPY1XsRGA1kMHxM59k9PjhzubY91Zx90VTOPg_amtnRWsofrMZONaQUkqmFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=ch0KcWTXlVt-61CPDXghz4Ui2qqauOknwhOOnnK3AT1sM0WeA4lCgiJEy-ZdK_TbxnHUX2p6ZrDVgY6Zx2UwY8ebzKg8WvKTpEAgxrBhtfiSmXxptQF1zHOjJ4joaGwZqQNG_Nr_p_Jqb8-RS2Eajdbkwp6aShR806kdfeJ_1vIXENtGHgeJIke0u1Rrwic0NO4CB7fGfGNg34JkbpxrFITPYoaGDvWkCFjKPvbAn_WqUa8OXh6e-O8zNVZPvdkg_EOo8pJ2oCu6b3LJ1Bu-FvPlWGkPY1XsRGA1kMHxM59k9PjhzubY91Zx90VTOPg_amtnRWsofrMZONaQUkqmFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTyLenxO4J9VRaNH-oxb2u0pJb_EyRsFD0m_yLFLeOSghU7GeZhdG6U4bcUKS_pMO-_VR-Wdsb4NEMBw75shGIYV98798I_y3gAuYUluNdiAaTdIGfzzoiDGwcimjCIFh6HC93FOzK72kj1zUrE2GBgsmQ2QzJ_xDIHhL_oyR0_anwlkBtWsPuj8ge6BbrCiIQzkBK4X5bNoN7yFqMfGeijP7K1Jr887GgfnQZJGPjlvufFr4wy0643BfmVx7qnAI6N6yrIE-wZ2G_utqq16iFCFD4FWfmzmFRK6A3vjHZlBCeF2GDUiD71zl8LgAoZFhLzvXDpQwk-XBJj_40V70Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwGDXgcl3LfS4wWT2BDMCfou3mzY6m5tc7UiFWQVvjbBjSyrLOmygqLd4uski1MZRbbC40ht1GlvkfLWxgFbBzXbc-SVg04o43xCBBSY1pTZYmL3OBCJYy1RTLTd6j6Xm9MF-eyX6IwtJguRJnk1DdUy5xQkyk__XqHNdStA-k-TCuvcfFkwLcCwIkD80qgVAPaAziIR-HvT05qXRtqJnu0o-jsAV3QIPlozTbvDv55irHVIFAkbccoeWLfHQtcgy-_VfINGerISMjJxU7XfIj0arCNUscghcIsgDYR67PqdCxLA3oRQsT2oAvW9eDe7E3GrJAx43s9sQzEFb9cGSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvhS7xAkCV9f83fjPdLhtkt6cfCAC_mIwkjHWdbE9QKW48e-Kbmt0vl3t49kWEsASV1t6D-KhoKkgY3yzaZHBCvIWSKt9XMiFjBy-JdAp8WEr-vnUD9Fhpqm1djwTrmgEtLF2E_kFm47mAEBW-rHfu5KOIrLXVQxJ_mRTpTtbvhU57R1_zVu8kE_Fh1_kQ-DN0Q1hVvd9f3iQ658CrDBpkOq0fjO2_j0gduTzbd7Q3tFZqKj1TXpCuBE6JoRifgFbG0Wsettjl9k3Fb5VT1ZixQNgiq4Dkgm5_uB_t2z0Sl_piMNACSTfnsAPw87WINFxnFNqkGB-Z7AdscbbbCYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_WgeOrNrlrYHr7e3U3wrAv5ydC1G0VoGn-9KMsYhGHx2Fo9IQuXLtSZDSEpwD3_oUaQpMdrXIB9jR_3DhGPtwZQ14bDRc34cpPcz9YGXKwa6OsCC4KCcshyqqcEFb3qFrNeut8WdzLAAXgCG0symHRqjoifC4gFf7aSGao5cpiOeFZTulz7iYMVH2JOYrrShs3_fcc_YsCBvzfLXT_5jo_KLfO9ifxLLm-KY7QSM_1_5gXwJbsCtFkmVlsxFY6Vf4l2w_EzLYgys-eOYO_M33zwVv-k8iRKqJx45K2TE76s3NlV08ffR-_VoqdlL83DokG4jaKKKwx2yVPfGzzzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQUTS5AxeBf2mdrCaTYKDKCnM7XG2nn2euxKzH2vuHWBapqGN6-oRVboBYWr-pIsLE10acCUYExclOek56TZPVT1a2RdHbFT0g49stkgTk2eS0Cz8PkeYDtRKTnQoz_BZ2cGmCn8_1UezJcQZxvezsjY1I1MFiTwrW32qfMoLpvP_58A58Gg46n-z7Rc42brNeWnEK8BsSkz1oUSBuCRCuFG5VcA3dYoGBilqw8eMe2X4WTmtED1Ksdd_Y2YPLZlESaUANHDtL_aBOdvGF7Zwg5UfKq9KfI9aoIZhxAZzyjUITalACdKfbYNoR00zvamxSV_lzLDShGhnaJo5BWFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQXxCIU8yiIdO8Sx-VGIRUtj0W68RoLSVdqv0x9mo7o-kPBmRQNcdJ0uR3Vr0oF8I97ytDFADNBhVpmaXDQbPDeZzXwvdgNuMlE_rVJPPHpdy73pJMcz_pMP0ygszBpKyduQLa3wTPno001ddxweDsP9TuttWC3jBDPZzq4m_5F3r_4FDxlcC9NjKGxW70dFAhS6bFXYsMrbyJ9P0IcnYN3kjYcYTFWR3DJsE7R0oqn7ewMj0U1YluGKzCYOuqy3HXTfIj3LDRITZJn6vivGuuHbja31VD1lrQYbLSFhTbd-clbfLb3RcTd4QevY9XXr3i2auXbCX8kNgOOUo8xidw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgHXHx5q1b6L3Gho0Jx2jBmitkPditLJwho9hIb1rNWDVzdZPZRZOMlJTVJILKygYR1P_tZ5jyRo9-ygOOPasWZDvnju7GirLQdZwLmtZtnmXVNiyLjWiSjmiBBDpicKaB4W9Yptkm9Fpifu28rnV4hsaqb-d2cfsGToQ7R1iyRBsFKj169XohmBBzktUuRENB_0KCHHJox93VJaVMg08Mv-pa8MOlnwA3nSt6F4JUBmFOORJy4h3X6WB_y6lArbQi7F-gicgedHzDfKVlzj9Q36rIOowyKc_wbdFp6CvjQc52OHWmwnWEfz7y417W3ENc0XijvFGpdUTPXs7ZgH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxzPDYX6LBTwVfedAcSrL5kaC7PU7QIoWJKhy_C3HQ7gqu4-JO8vwT5got6ujYpzcDjdHpUl25oBy227tv2bIQuFp0LTmtJ8zeoO-jYtf9o7uwdbuTRfmh1rNniWTupP_5AmAFiWMbsd-QVIlh_pxQFPBaI3w-mRAVbRuZ14lP35H7th3pKLfxKVXUhTYMTsVNlGFXFqfqFOBxvpCjtQgFoL6SkJpNi1l3y0u_HszkPf4Uup8B3vGgaL9cLM_ARszpawrU1vjmhLyG0ZbCLVnsyDtwic3uqdLDIcO8vm7EcIDDDYmvD--TXnQUvz4dNgEXUB8D403DzQ5xfGXcwHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlpaDX7l7K9gXS2AJLY2JonKeLb3PbHMREm-A__19O9xnQZUU73skh4e9-xhx-_0fsQldqqF9wC4A7HBrTYBuVUB3GmJB5s3pA8FKZqeNI3MaAilX00_JujWGZZVVtOYK-a8mL4yesTpmQ6tQPuHgNtxQZ4J2mO2Hn8O2UswHL2ZkYSYnDg2XWNv5DhIMP6sbF_kp_jMKvXWqUmLJFAvCLvGHxdcFcIph8X6hdHDuOFpMr8nXh-4UIiaba0HnW0FTez3DTwhhhah4z31ca-VrA39SinT7pTHkPnJvi_dkZoRhNRtoxQx5ASy_I0iHZzVnhrd38XpNUCh8RuFjGu1pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA33a51UVfNmKppO-KlNJwDhlFmdOJMEApc1qff-Y6K8aP2I9QaW08VieAfZbcIyJwqc1fYYPzh6bpNDlMvu-lA_g3AHCs3iXvywrVGJIlNj2Q-FBCC7pzXK38ObolIZM1CSy57-UXdzmU3G_7FW2qaNf90F4Wi7Vpt4M8OsihMfsMEIlR3ICwBUGkR0HRMLcetG5HombfTc8U3xkWm9UrafuPG8b258s03NZhDSvYQ3dmfSjLuTHC_WoSbMEp2bpRIVPK71y9Hb2PjFiUYbsPS2TBGogX7KaA1n-CWC9twmq5Oeiges7ewwEiw_s9JqB7Z-V6rNXwXD-z2yDtPgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnOtUCEQBPmbQD7Unmp_49RjAQbKTyWmz7QljUDIUyy-aJZB5qajLWrSPRJSqRvbBZ39b1QFdewuvTWydZvgOGh8f_TbsLnXYjOYPFKT_htdXNuFqUH6CbK0wUR1dB--c_wW5SZy-hh4_dIW3vaGstnJxtpzGIqRKdRDKPkDhYp3rC1yloNK4xGeFCPLjhAG0prox9-Sgzaz_BfT4iOyewdG6rGj1629inuhqz8NfEX2edQ154_3b6X6L_Yx3KPsjFro2HqhRCjl0ftTmnt4HETQH_e6Kkowtg0x2Z9pNdLBixYo1sNtPBhiNs_dV_XToTxWz-wNTEg1nWjwLz799w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=RZ7v3qu6cxQPoG6f8s5rB7jgfVo57wtTg66DpPGbFb3R3MLycKDLRbu1N9QU4fW-pCfXx7RTeqnHGrn3BPG5inLgQ_RByw7W4X1dfoGggrCCo1dtlJLaNqaWSStN_Inkxgkk7xxs_V0VTdMQoiJnRh0170N6dpxFkJVnacCMVKXmnEq6JVTZGQuNCt9z1qKnhIeo55jRMxZr9ZHp5cdthne1kiISlx0UTWr6qrM-wq4MKt1SGGFzLjiCh0ZGsFWAyBT_s_IfKaxYVD29OZZRgTKWcBr-SdteLGOkTHW5fmvORV9KddoJu-sKX92O2_I8iyhMOsD1JrUQDxvV78cGYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=RZ7v3qu6cxQPoG6f8s5rB7jgfVo57wtTg66DpPGbFb3R3MLycKDLRbu1N9QU4fW-pCfXx7RTeqnHGrn3BPG5inLgQ_RByw7W4X1dfoGggrCCo1dtlJLaNqaWSStN_Inkxgkk7xxs_V0VTdMQoiJnRh0170N6dpxFkJVnacCMVKXmnEq6JVTZGQuNCt9z1qKnhIeo55jRMxZr9ZHp5cdthne1kiISlx0UTWr6qrM-wq4MKt1SGGFzLjiCh0ZGsFWAyBT_s_IfKaxYVD29OZZRgTKWcBr-SdteLGOkTHW5fmvORV9KddoJu-sKX92O2_I8iyhMOsD1JrUQDxvV78cGYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=NGsc3PNd-r3RRkAd3T3DeJp6mWIBLhvZ7VreuM2AKhBJXd_Tff5tCDdkk7krhm2a02sFdhkSO58opxvACYvYtIptLa27u-laKqIFEQZ21t5ztu-vadLV1EH1H7os5OP9Ti0ZEI9NtiU9M82pAtHiXkPKXAb29NazRGWKiupvd1mNsnalkZIaN4Npr0lHB4CPs6mFL6WZSDr0JkppB8nB00ptxaX49ObE2qtYpwoFmtSLplvIMT7PGgiacHKl0LVav-52UkFqJ5_gKjaDjqpD9FDeJAOWwHWrfLFdicRj_sGD7huMU1eqe-jZfe1d2vgS9T0l41G5BHyTMnXHS2NwVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=NGsc3PNd-r3RRkAd3T3DeJp6mWIBLhvZ7VreuM2AKhBJXd_Tff5tCDdkk7krhm2a02sFdhkSO58opxvACYvYtIptLa27u-laKqIFEQZ21t5ztu-vadLV1EH1H7os5OP9Ti0ZEI9NtiU9M82pAtHiXkPKXAb29NazRGWKiupvd1mNsnalkZIaN4Npr0lHB4CPs6mFL6WZSDr0JkppB8nB00ptxaX49ObE2qtYpwoFmtSLplvIMT7PGgiacHKl0LVav-52UkFqJ5_gKjaDjqpD9FDeJAOWwHWrfLFdicRj_sGD7huMU1eqe-jZfe1d2vgS9T0l41G5BHyTMnXHS2NwVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oimD44EqbHBZhiZVsVcn650PRJrB_vxTJArNNoNBvTOD-k1-ZcryzIzVJqepzJN9RlGad1MmPqV4e-zaWEwOFUs-CRSp16mRO5SJxsi69OzDUqY9j6mqzr17CcCNOHOGpqmG2ctVb_isY_zwzwJahFPkjzLOh38gRdPzJPzfYSOC-XTvzQfWwPlc7Dfx1OkhhgkRIHF5DnFg8exbmywVgvWs0zylfuyUXRTSgYtpyQejkMySjKdWc0Jk2KulRtBEJcWABzlksITpKvIlHslrXtN1n_Md1y3fh6TLDHA2zeEYogMss5NjLOYigpkAwLp9hxtqu2nELcSHk6d1Z_49OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjpoB_7NW0mmhS8G5v-jdwQ_2mdS9EbZJQZUeVdY6i3Q4o7yRCUBBJGXOTu62bNSh9S7bRBUIg7QXqXKJ-XA5qE5W3UZQKtDqIcEAnAjEbYqTGLaLlRw7-r2Qf9jCIT8YRiEdP8An5_I6lIN-pmf6pSPGSmET67eKTIHrMJfe78SeuPU11onSbH4fGJBd3ATD1QTmnaj0DnHeuede5_aROb4kYI3Zews6zu8T_Nb_jbVP_Wc_g8_SoFK80BrAil9lgkQl-GQ88eOkGPinwJZ8JE2-CLXcEJRCw4TZBQWXaBjZnIkVcQEmYdyirvBGVjjozaPcXhDyAFOSOYAmnc-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqhqs6jNsgM8M77pL9Mcl5JBDKRpnsBj8Titp07iGq2rv7n2ciHJoPZeHg2HyL16Z4v03csxd6T_-n6G_AlMmAu8_50IusbHm5w_sScD3aue1h2ptwGCoQYUmkTjPc0s7ik_CcD2Z7EZuceIg0StIbBvgs4qmnxydOVg90PgvKgWThU9twNsd-wBCXfeLv0-cqSdFFiGTIoPciO4koTUbW8Nd3eGFn-xm0_EG5ujGbtQzvtZ8tMg49OZyVQ5sDop2lu1ctmX-VUDNKtKTY3DnjxoDqOGqXZaqhw3wlIM1RPTQHYddyMDx1ILC2VkTI_u4O5ZVvWPBf6H7LTRsWLfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=DDKsOLnBf93xJPwJUzO5cCAW6tpV74fn98oU-_qbI4-4rZAGLQSRZqVc3IOD3Nj63M_cjnBToERFYAP73FwR1TjTurA0599mzIYufpwkqH7FbU3LA8m7DJv3dkhUhihy1a1ooowvasgDULgxz68vMT0l1IgXoYyelnbVQm2BDUGKCBjIEdWeoGIWHBT0cd7MbFWgv9KnUYQTnF-lMJKWVNLicg6HjTQq0t38aEu3EButA0RWOpxBgfGJNjrV7cTlUJw4BMr91PsYV_I7cwXyVl5pMdGVq4AdRb6heOMTjVfI-zxbNYVSx98ka48eFOyYplByXUMyLBKWXaILurtFZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=DDKsOLnBf93xJPwJUzO5cCAW6tpV74fn98oU-_qbI4-4rZAGLQSRZqVc3IOD3Nj63M_cjnBToERFYAP73FwR1TjTurA0599mzIYufpwkqH7FbU3LA8m7DJv3dkhUhihy1a1ooowvasgDULgxz68vMT0l1IgXoYyelnbVQm2BDUGKCBjIEdWeoGIWHBT0cd7MbFWgv9KnUYQTnF-lMJKWVNLicg6HjTQq0t38aEu3EButA0RWOpxBgfGJNjrV7cTlUJw4BMr91PsYV_I7cwXyVl5pMdGVq4AdRb6heOMTjVfI-zxbNYVSx98ka48eFOyYplByXUMyLBKWXaILurtFZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f76X7LgBfTHMxyBckt-4uQcVc2dAwlDpmyyZFOFH3pc3pQlgNZ39S55HMxoq5iwX5-n1F2nP2yUyQ60sVZkc3YzHyJutx-W1JetKYl0FbdrZyv-g0XJkkNgU2R6jeYSirCIxjZ5JuGJNay10Ytp1_yyBNx9IepFLoWtSRVGFrYcxU0n02b4EyhXClveTeO8pSd8Ih8Ytu6UJ7pB0ThqIo-N3YYa3IKvFP1qBXQn7LtP4ukbmY8RrL2xk-W0sJJI8BHRL9qS2dZug6zfU5en_AAvtTJxcUszPyaJ3HdcD0Iqm6y4_fIcrJtodyqwxbFyGdJfOQqX0KU31K2vXHYp7HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtWxCa4UFrzyArAwrKs_3PjJLxUsTCCydLOdFPlO_zNGIrUK5Urr_KkazZLLEWGyekFed6GF_HIYUDyfT3gy5U6cz-U__HUSUuuvNYk9tr_ChS5iQjqGubWf7Ss9IuZoknc4KChfCnu0y5JyyzoLScBhpVEkFuAGf_AAdXe0YyvWT81n8yuNediqAdXfucIOtweqg41lr7bhepeGnYtlQSbTLN2x2Wemop4TYmJ8lEjLZ5eTd3H6-u2JiPsSnzm4Ee4dVo5YOkjVlt3nGJnsfNEdCHLuHIoxY5VcTaatocXsjw-apVfNHmsIC1ARUD7Qs2Oaz2eID35aO4oX9ySIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6x3n227CqDAl8I30SFqPWpNfOgSpYCur90gF4rfdFcyzEujVK3k07NXeXaiEUyyov5lW97ZKZc1Fy4bMVJbSeu3CeOufsdpGhc3RhUTEzu6swQPuiPYcgdmd1rKvm743AboT9bbGQ9r47snl-mT7CMFlF8hDi4VNIANrlE5tmmeeaTVaQujuMLXEP9RztiyOvwNwVG4abQBpanVZdwTjaIwTtFpR9LxPCLIQysvdtTeIvNvjzp4-DDQRyo7feaLCZhDQTL64eS892D18sDbpHFkdFU48Z0jRVFw0JORmaLkv9DQ3aWH3Y2OhB41R7NC1r49eWUbZagpntOCws1mGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuOIzu8yWsyr6EpLKLyStUcIEUeMPkTqo7A95F55R0mU0OJNQisERxp3n2ZpievMmkNh93gbW9wMd3c1sG3FXQ3COACMBYvXJI_-A9UMMqOUmF96HHTARreXkov4VYtB3yyxcrfcYqxuf5GwE0CO_y34T_ot7vejvYzwbQ_9treFS7AyuJBHjvpGPeKMD6k-LbGKNRhDzOtF_MjwQCdD0RGn7IzVmfDJwNUtkMRdcsuTrPpYFKxje6y1xS4SAGZ95QXw4Xgb4R2UVBKooTo7eUxtVghWGVZIn58ayxx4VsSpNkTasx83AOGoYSnkVKhZJTKBZ2wSPGPSzCCSCvBntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHpdVk8fTihi3QeorWgmSXheHZrul4uB_HdLJUgaSfmc4o_DgBLLSSQft_qhv5SIBsof7pPE9-ssLhdKC9NdJDPGv0iOlo649Oc08RXR2SYrtmruZJZrdlqG5CzYlRzp_8Syjp7B1QLbLNehaHdHaxYD1CdMOuGPg_YcKaS8nad6NWQk3W2A0WH89evrobvTDiDArockepy-NyuYVyzBqiUJNJnEXWPQwhu-HJVX66w18kY8-OaFAau-6cPSvahb_yaOP7EFRtjGeXxkhKYkymFTW688Iiz67E5eQWiGTdQHcXrKTdtbs_n0utgIPgV4ezgW8uN1ZV9YI2w3IoTiYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlPe2rWBeO_a-6EEyN95K4dVuMReQVsjo6l7tNuQqnUyxzPWOI9GQ0UziJJMY_qvHQQhQG0BHq1Z4YeJchg1DqBYEZOHcq8pmto_AoIR47U2hVRyX97bkSvLLjw2XYIHrWizTexKi43AkBn54Q4xdG8Xlfc16orlsrJAuhBmr3ZlujlLhx0110dX_HrHERmxnIgx5jL4hVid9qX-VN2hBbKpoEv5JKpyGJSqI9MMKScotXBAm8S8I09y0vkm9gJ_hQUVQ988v8trPE5QeTuB2CGcYzAHiqkXrhmEGdVbb-9T_sgGnbUl7CzxI4uhDoxDgopNiFT0_wuTQ9adljlV2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_ovIwv3SGO9tSFd-hiExCAK6IDwvk3OVdxAWqMwn7VQvlrApbQCZeg_BdHA0XynKZuDJ8Rft-otiYHkpJbJ4DfDxKQVBNk7RzSOOci01FE-9ZzIdC4pDU3HxQvpzIfOPXkcHrbS4b_1RCC9w-joNX7jh0t5516k4u1C-R1PjyaA1lqlponcPT3-HODOAGjNP_FRg8EDNclq3JPqCx3xy4msdG8zciHnNqxLm88CF20G4JaJn1PFXt6w30e7mTy6PS17wgjCZmZmNV-yEkN1RxlTq2A3FEt1ud4M_uE1q_p3H3I2SIDsJs05LvpjvYZ7_ZKp7B8oVdyL9zPRPzsaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8WaFSxVPHRUoiKHEV4SDkbYxp3YpUjOz_L9Bf8OvqothIPBvI0mAk6ssrvBhw6Nmic-Fhnc-HU-IPKq47vF15AIBeLQiqRHnnCQ3TkV9M3el9dAGTRL2IFG1N0suxJSclqhehhhCh-xedAPBk_5nWu6GUEY-0zoIvdTKoS_dca2gUhQl6htqZ_-AHFLFdlnev8c6VZQPhGIFRjjQgUBtf5CHz_YNAPZkjUAC9jQR7OA4RoBHkEk0YIgwACZCse0F81nqdSyuwMYlMbyucL3yM9VJWkbgc4ffWJQbyXW7cQjiTWTsX5AnPfMY6STERZHrARvJaHprkFzexr7sP8fKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKhbJGk7xYRdUNhbUvWJ6FAnmhDtXaild1W56W84PrVe5eKEVnMpvw3ZMQ87wyX0BWPZOJloWWGAzYtz_7KF2AllmYvlYOJ2khO-L_nwY3ziqpK3W3umKsxIyHZo7n7C-TNK8qTMvjmaNGLZeIJwVm_itbBDOZ6bwMBb5lz_pRhmF-XbqdbkMnuYlq9kWRQPU8C5hmAQAJ8b_pxfq6EP94nNbIDG1PbiEPjmh6iKxLgfbmEypNri3N50yhGTnm0fE4QPxD_tr0wol6kyW2mxAWxG2BFgG-xm63S7XrHvNR68fZHFhjZqCQsXqlU1CNzoENAEDJTEgCxdBRjoxaWBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eL-t7HCodbz1F4plCZbRq8__ifqlLNEhpTIMCXfEVmIunlrhLx_swCE2KkKpMQykxP1Cu8AB9pkACkqf3OKLcfpWPijanZlnBQBXi47MlmhfUY_RUZ7azni7h1JgdNO7GOlyxYqq9YODKaPMKFpSVrySLZuCzVdDKMiseMS51oHnB_s3Jf0gIPnDHkk_hzg6YvAC23X-FWcJ2OBsv2ujUJgMDp-8PrHEKFarqlcJywdUqLt8sBdeI9U2fDUGKR42YcHoVBRr3LOaQHaCu54uBcXGjnvspnEfr9NK0aRMW_jcU-6jIyZD8W6oq691p_opSpJpDW9QN9G1KA21Z3LzWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUZtI5wGTsmDX3tfnNgGqMEanZ18YD0L5G6JDohCo4hpGLLbuBvlVk2BatHO6r0fS_sv_wwlezheJr1wB81Ldo5ep3Yvz1OjDisfXAhyDZudbG_RFje3VvKNn393ITB896geiVcdGIW4dF-Y1EYpw0rEVOLKWq5T-NkhcZquqlL5JBZ2QNTqZ5sz50BCNw8jV4J40gmoBTQHrqB-REs8on_2r2ViN_yjpX4V6mUlB6sXX07k8Ql9itFlVcS5t6-iJzAs5KNnCNoIvK7SPnAupJ2E1MdYWA2hVBlM4pBZuedjsbVSNUPDeyYPbf1Zmj4K93clO9kQkK9cnJMYFZeQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=suzMnLgnVFjcJs8vIIdIECGHgLRHluEtttD2FUB1yDEpa0YBTNHOT4crbQ2QI6m-UXC6v6IOeqXiAOi_yZMV_XHACK-2Nqyw8QlMRe6DsgYp3DQpnLimGaAY-CXK-h8XwnnIbpfrLtxP5fmy8iej_sqLOttgOpsq6_0YREjY82DtAvr7ONHszPC_PH327tLpviXchhdpp3_XvReDj-iHC28g9_IVmFDFjoSjPp1pSKcRpzbKDd_kYD8xucBXFPfMvyunAfTPvQawWS5chCi5xMW2mhatDuonTwfZORqshm0brLWTRJ8PuJhDaInDnST74I8Ff4wiGYGYy-M637ejVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=suzMnLgnVFjcJs8vIIdIECGHgLRHluEtttD2FUB1yDEpa0YBTNHOT4crbQ2QI6m-UXC6v6IOeqXiAOi_yZMV_XHACK-2Nqyw8QlMRe6DsgYp3DQpnLimGaAY-CXK-h8XwnnIbpfrLtxP5fmy8iej_sqLOttgOpsq6_0YREjY82DtAvr7ONHszPC_PH327tLpviXchhdpp3_XvReDj-iHC28g9_IVmFDFjoSjPp1pSKcRpzbKDd_kYD8xucBXFPfMvyunAfTPvQawWS5chCi5xMW2mhatDuonTwfZORqshm0brLWTRJ8PuJhDaInDnST74I8Ff4wiGYGYy-M637ejVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=Z4-GprbjWNW8xah71am84rreFcg5ihGEh366k_FUNj_zlJNZtacltgvak0N1SFc3YgxY7aaEgo6PXe95vFYu-vBt-ko8wB8tO0Z8UHZ00RZt3dwvPZKWHjXyJGWzDK1VMZnN4ilUEbR5w9y1El5l2SvKWyXl5nVcyK5lTe5gop0jnvyKMms8UyV3r1_KOQZB4NXyFcvQRyvNDg3umOSZs1NnaCEhdxU6_sbdy0AvTjvA9BWiedXOxMPjvLjMRk8fdPaQVIjEmuk3eCf050W8yfreqgI0DMM3ag2iEx8F4NtKHCoF1jrWVuEzG_PoeKfppOu9f46Tazs7Qms0p-vwEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=Z4-GprbjWNW8xah71am84rreFcg5ihGEh366k_FUNj_zlJNZtacltgvak0N1SFc3YgxY7aaEgo6PXe95vFYu-vBt-ko8wB8tO0Z8UHZ00RZt3dwvPZKWHjXyJGWzDK1VMZnN4ilUEbR5w9y1El5l2SvKWyXl5nVcyK5lTe5gop0jnvyKMms8UyV3r1_KOQZB4NXyFcvQRyvNDg3umOSZs1NnaCEhdxU6_sbdy0AvTjvA9BWiedXOxMPjvLjMRk8fdPaQVIjEmuk3eCf050W8yfreqgI0DMM3ag2iEx8F4NtKHCoF1jrWVuEzG_PoeKfppOu9f46Tazs7Qms0p-vwEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=alOQqeNDclbnk9_SjStT07_BU2YVY4hhR1jySGvDrBRkwhCAHIB9UCGzr3v5bIgFVgvjwEFIuM4CR4bdShiAZzz_MmUJdrPMSNp364vs4yGg_LyFnZbZZOa1E42s0aQDRxP0icXsi2DhGZcVjLHE2ie8qGsdT7yM-NhelP5CLVZcWk68_3JdESJUco4SgUocPSFS7KY8hAuWzhnw-WmhBfA7hFp_YzhmSKFQHjMvAVGccl92PwN_uhdjqh43Ffcw2CbPh_PZok9ZukAPgqSIp8IuCUabNAD7wNxgU2IkQ6_U94SQa5bFuLe4BUQEiVhhZ-keAqYE_286eNzcPb2c1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=alOQqeNDclbnk9_SjStT07_BU2YVY4hhR1jySGvDrBRkwhCAHIB9UCGzr3v5bIgFVgvjwEFIuM4CR4bdShiAZzz_MmUJdrPMSNp364vs4yGg_LyFnZbZZOa1E42s0aQDRxP0icXsi2DhGZcVjLHE2ie8qGsdT7yM-NhelP5CLVZcWk68_3JdESJUco4SgUocPSFS7KY8hAuWzhnw-WmhBfA7hFp_YzhmSKFQHjMvAVGccl92PwN_uhdjqh43Ffcw2CbPh_PZok9ZukAPgqSIp8IuCUabNAD7wNxgU2IkQ6_U94SQa5bFuLe4BUQEiVhhZ-keAqYE_286eNzcPb2c1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNI8SgG5gs7gr2dLilu_77_tfLbaJAju1K8SImcW3z0gRF5cNRNZMvg9r0REoORYtatpaTEBlBlVf6ryS1X8XwPPiEXZbZ-_pSrtUbaepYt8lns9gv12aiDbuJwQvFno-QQoBUqoCFmBQEjEVpYu6nXRb8OkWPwl42Eh5H8YNTTmrA8aMnqR1R5o3QCHqmpzTNso-PTq0aYJQjFgtVIoLiGqrkKcN6Hu4YQTqqDxwOuf45xRd21-n_uichw-Oh-onVVv792WU-ursbbF5xDtQTMtVNgTo8eV46R0FrmwwXSnkaBk-lmFf-aSKVTUVyuG2F0PgsWQj0qXL329rTgS5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=qq5h_0Qs2H4jJ_RyUBYnKEvjRIOaf2wqxdLsamJB7d46r0-7mXQgqHdkMFjqBL5uHq0Toh66FLuThZn0IH_kC-FDVI6chjkacuqon0IMnMm5IBbR0UmZPO7oSI4i4tCI0YSwwXm-NZ7Fzf-16Ioi__qx4bcJH1CyQfHnOt1ECa95Mz6nEbpleqhQ187zbToMtKdijIuCcEmn16WhjQJ6pqLGNxkMI8pzY0uM_72nLT20RWXQIgGDG6xXfoUt-EKfsmxmyR0-pAy5qf0peV2tR1UqX0p4luvLMr37UvIflfdtYIdxc1C25lf5HFPFIsQainCwUWtkFUCCW0f8gzIscg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=qq5h_0Qs2H4jJ_RyUBYnKEvjRIOaf2wqxdLsamJB7d46r0-7mXQgqHdkMFjqBL5uHq0Toh66FLuThZn0IH_kC-FDVI6chjkacuqon0IMnMm5IBbR0UmZPO7oSI4i4tCI0YSwwXm-NZ7Fzf-16Ioi__qx4bcJH1CyQfHnOt1ECa95Mz6nEbpleqhQ187zbToMtKdijIuCcEmn16WhjQJ6pqLGNxkMI8pzY0uM_72nLT20RWXQIgGDG6xXfoUt-EKfsmxmyR0-pAy5qf0peV2tR1UqX0p4luvLMr37UvIflfdtYIdxc1C25lf5HFPFIsQainCwUWtkFUCCW0f8gzIscg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=qM6W6QguRwKiVmUyF4A3mZF7GfKxBmjBIHtlPWoJfKXU3ofLIreBIKU94V3Bjw1uK7NpM329Pe0KVZ1D8xa8t-h_6lgSLJ5qKZ8AJQpL-KnhzQpwN-p1SN3Lx15uMqIw92bBAAts2SBTSl23-N7ri8uj8TEV-SqrRyit1U92ZYZUgLnZlrCiETi_MXLGk1SwgM8SiNKps4pH6sXhuxkrCrR-ZTD87-6opnRbEU7f8NQbWAE8ZzYMATWOnLbIjtelxTMfjOCMeJ-i0LLV3oEVgFLz4pmNZ1CpJlp0VWLV_XET4oPxUtz7Hb8wDunQdpn3KGI51SwqSwDcjkYI8H7FiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=qM6W6QguRwKiVmUyF4A3mZF7GfKxBmjBIHtlPWoJfKXU3ofLIreBIKU94V3Bjw1uK7NpM329Pe0KVZ1D8xa8t-h_6lgSLJ5qKZ8AJQpL-KnhzQpwN-p1SN3Lx15uMqIw92bBAAts2SBTSl23-N7ri8uj8TEV-SqrRyit1U92ZYZUgLnZlrCiETi_MXLGk1SwgM8SiNKps4pH6sXhuxkrCrR-ZTD87-6opnRbEU7f8NQbWAE8ZzYMATWOnLbIjtelxTMfjOCMeJ-i0LLV3oEVgFLz4pmNZ1CpJlp0VWLV_XET4oPxUtz7Hb8wDunQdpn3KGI51SwqSwDcjkYI8H7FiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qx7SARBGXj7FI8VUpQbFTBfh-xQxD5gDWx8vHB4wwd8lvpI3Webm2wPJWTmfO6fIAj_HdLZj1_Ru1cPUIRyyDFevz8R3nihHpeYhPjcISzRyrFihFKhL9h0_O-X8Hnf3pJubvVx-6Xs4VOXv0X4c7TsBcB8tQTWfHlwoJccKAuWoXvWdcu14GGYShcHm_WNCeWLBTlLQ_WggYUtzIVsLo48xzLi1QPztVYjKpau7r12ZR_Cwn2GGeOXawiIhECevOGg4LHkH_vyecMWCAvQGAoR2cYu5KVFURSSIPCpcDnU9iJmT9PdnDH5pdaHqMj71W-vISR01pGeYQS9sQCRLaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEXlATmjFG2C2bFPLGd7_esT7jAja7UEBq5YTRBytvhb_5I9bAuWA7zXwPO29YrfC73gY8XQJSPoQQ6CsHqA0XXyE354a4htwXexfKkfTbKBA1E-kr9cEnrxlUzJkwHFpklwtScXUlFS9MNSfEYfO-qvowTCMfy8tOXRJbaEv0kZs9b52IJPtcFgHwEJO992R-ETG03Y0HzsYvqRMSaYSe1Ir57PMlYl1es4VCRoIhzho7ESxL9T98WT7n8VR8MqZ9YOuyHzRtVmVU4E5QTOqiOsjH2ZP85rbCLi2VuhjYKh_rsI_Xq5BdeurUXtHUdXVBlCV5aXmaV03MLHENkQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFHamuqmi1ixq1C3BVxtmC2V_qoQ0YUXBcNabcKxFOFoRf9cmJjTdNMyzMLZuWOQtQa_XeHLneQRRhu3BbRpoJpj_VqL5Fle2ADwq0eVXPaccjN9EyMqYrszAkgoFZvJiiuBQkflQWp5bADUqDpu_7gjLjij1WHUq8MsDUYvRceLa43O0wgg_kOcNCzFjjKMfxmTj6C8gWXAY12Qw7_Nx7DdPyH3jJEqzqUdVcDy-7zdJpsycCXIHL563hjS4A3Naz1umiphiAEFGVQBQoZTJEU7FvNBf1XNCaKM0nr8HCgYZyon3UpGo3AkncQP3scn81dq8aCcx3xjU60K3MthfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtiN5SnCe2bqfUYwixKNNIvP_JUfJtt_4ViP6q7j_bevgx1mf2BsLPzsbJLy-dS52Odym-CRe2xk6XOmqFVk8ISFWntM4KlWTPJf0ImmiBHYhXAUOMPVjtwPaVogCB2J9JMYq0jaOQ3QiK-fpNScHZaN0kgVnPk-ygPJBx8sM9IYFlSBadllZZJ9L8xTqeRePMFjWwnP_eubpWMKqTcnK9TACO6amdwKd1Oxlqgy8xsceOtVyOX2zLmy4wnY1ATqvFfMdOs_rGfuqLrlYSpPwhkNK8SlxDztQGP9Iidxotgj8owECrNK_C7I4xtTj0H_ID8f4At9mR9MnFubIM1QfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXitN7eWMWoc5cSF2nc0PA7GpCxaaLVtYbmo29EVUecQy_4UB-pLxcZu20L_pDpfWPyoGqMzAV5LpWPR2ltXml7qs3xo3u_SsZFLoIAgaEh1eWj5m1KjhdQmM4uutAE5_YerT2AMhHHRgFU-5FTMvarrypEBlqJ_HvEC-Dvy-yWcEWequrhG4f7NWH35-W7Ta_eShAvxwdP9o8kDEWZ-X9_Zylnm0jPZLWPvl7APZi-1lNVxFx-j9n2Q93GTkVVTpb-b676cyG4Z9M_t_FB6Z0niIzWbUCU57wTXuOF0yc4AG73g2sn_ZD4-crY6UJ2mc8wbZGgg2GRcwmF1-YyUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bi_uEEwpsX4FYovNyNSv5CCw57BNdb1EdG0KzAFCW1glVLgPZz4mmO-Xgr2Q-5GnrPcuecxSeaqJ6JRAVJxamVdDfmxhwRHLAuO5KiKWEG5KHS14jRM7-OlF7oUkVLdgMhy-BO6nLXyWX2GwvCGunUHOxJQldagMvQLGIQje03ovRXvlU2G3WmvYsOelFzuQiPUx58LxuhrIkF4Dyg8etADQIvmJQ-XhwCx11uB-WYM5XZ7YHxxpCmzlw7YzxnUnk1azpxu4N9GKjpFyUjyeAFMHqZ18v2KkBqdZBwTRgalRyatT_xrRWfYEWBTggh_orAPNWVmQpdV9q3CgkCJy8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkN9OkGjiyTSJAd33ADRUKc0_gb7cz64ER5PD6D466Lc7b-ghgrSXBB35a8PfR6VZ28LnEgwhyyU3OOXnSspSF0JqptidqeYmfdxaWCm5W2lMoz1BvGTLK0gnQUPps_6PRbiRz0js0G_H41KCYzyEG3HfFd-HjlvJ0pLmukz6dM2IqXJkK8P8QYymBl8br9b6aXNV6_HkiiDYjLLMpfb-Yh0TJMiLRvwnmCn0DcXUteoP6XqVxMnelpYDY__n6XdhzN9bXxYu39smLodQNAYEEsnUW8xXtFU-XlJa3fHo_7WdBZs5dYezr9ySKz-R2WWB9wQfWDqsAqCcOvgw-mcTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=iFKqirbLAFnv0DZyVOIuMPQDIS17px-xnplsVD6Zub6OAKjyrd4njGbXcZw7D2JgKOKPqkLKHlTctchEac_TaFIQNcwSE34uO4P9fNhavNoRvzUtxifPT7gG-dgfMygVl4TxvroU8M4ZI3t_iV1boScVhO9LgfV6CXZmaJSmOJJ-pV1vj4U-SAbtLdBnmOFEONVEkzx0RQoPqlMiJexF8VmV2HxsajqwHS7Ir0P9vcvSa21zvcqr6tbTTtBPq7uwxToagC4mBgNZwxp_Kz-B5_7yIhvcbUUD0Cq7xmpLVvrsOq-NulO7fFLv1ah8dXP4pOi7ze4g9zGKd7Nw-wusAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=iFKqirbLAFnv0DZyVOIuMPQDIS17px-xnplsVD6Zub6OAKjyrd4njGbXcZw7D2JgKOKPqkLKHlTctchEac_TaFIQNcwSE34uO4P9fNhavNoRvzUtxifPT7gG-dgfMygVl4TxvroU8M4ZI3t_iV1boScVhO9LgfV6CXZmaJSmOJJ-pV1vj4U-SAbtLdBnmOFEONVEkzx0RQoPqlMiJexF8VmV2HxsajqwHS7Ir0P9vcvSa21zvcqr6tbTTtBPq7uwxToagC4mBgNZwxp_Kz-B5_7yIhvcbUUD0Cq7xmpLVvrsOq-NulO7fFLv1ah8dXP4pOi7ze4g9zGKd7Nw-wusAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7VsI4CAEMZ4uu6GUrtYaUH_0Ap4RP66hXI4PCCdvyMQlEl0XfgXLL3SjL4q9ZESJwa63mhntU2H0EuK7JUWbxBNJPlqSVTsHWa_KDq0_AE6xiJ_rFZB18iB8yA5TemsghQD-fkEY02luCnngKeH8orb2W5HL3nhZZKOHUYxcuW6L9GGAda8SLPubwoNgsGrykWDteu9Duj5oH4NrHX3JSlQwKN_KpBy5XijhJpGwrttkN0yAQL55rSOUeD6Dx_5o41EhNB1lRmV03QComk88SyHT5FVVR5aoBag1aMEedKn4S9-cHoVUjO78SWXfrXXF2OCMeUgdSYqGmKARymEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq3L-v9P-rd-E8jkz8zktaL5E-BEgjY5APW2SfL6j2yLMBS-5vOS6lon1DZ7H6fwab3QgTHDIzkPXa-zgNEsDQ-d9Cq8EjI2TZ8Q4i47QPMfZSseAdFFCUmM08UGwLnsOYstLgvinBPGNMDKWyo_sJp9m2qbH6sqKWWTzCPocLcYrwrDJkwfj_xSeZuagxAkA2-u7zgjBk-ZWCD1_WDXQLzG5D35zCvjtvbbIMZ6BD7kcVPHss3KzEBwptQH5NflppiC3jjgzE6HCS_5xxMcDLQrvkbrOhtFQujjKDN5wqtjpDueT9AxQT-1IE5J0_08PRGDSU9TUfrXbFLDd-gu9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWGVJ46EdSAsb6Cy83G-KsL61Jtm3uteIx-elSkQi5OxRk0Xin8N3wua5eCo0LZwW59YyMje2FduSSjiuFwF0Rc1kuSdUgJ5__oNJslaNzl7zW0_ytn7rJ3ufEd3Mell0pDXyuZgtXxC42m2lrxVi6omlVCnbezoqsrq5ut_M7B0_R9lc_S12IyukZmoQfed7kgYDAwZVt2vQoZQ5BP9vJpITinfoA7vkiVg44Y5MbVt2Lov6h6CFQjLAG0Tg2-8cOkk_Vawr1hdkHeo171YTX_Hq0hINKRU7GwOqjlBqWk73SvgG-IsIqK_Mm0aFedJ5tfg-RY2FDewkb2EDQxu6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfwUzR_p7p9IjGcL7H6K9LFVkKuLBgNXvQt-4W_cq1HxM2GqhKbyeNlh5NcsAzRHmK3HDWDncmGO-WpOb6Q0vTjXsHt_XqctuwhWpLjX1QUCbOA8GFgeeV3E7I1sCgjYZdEEV7dk9PrFN25035mLGofohMQd3fBNuHk2huHB4-pYEjh-nZc-6b7JuwuSnOUng0wHZ58P1AeMkQz7MhLgYpINVWN4kteevfDok0EgLgA31vj-c-U10mzvNHnUgDTvNRJv_T5dvzFQYCOipyLDMlOCAb28fA-sZuDXT-BcQvNyKLsXG2ysNxSBTKNZQQxA3PXwVCaJ41QtE7eV5hoMxg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=FY7suZ921GDk3gO-1Jo5f5HUUhMFIDXY8UNINMnXCCqA0y1IKj7b7j3SAPpLgQ5-DcdWk_8iFJSe3itPMarv0zLdAqRJWzX7XLFBqlJmhwwohOI4FzRa77aJEGpKQnzlpjWSHx6kXUBaw77r1aJTim6prToikIGUMnjpJGFaYKRkzzEEU1NJ9vYzReNU7Wi9V-2gB1SQk6WHpKD9tTsOcaZU9oj6sr3hZM0ymQBM0RL7MOMB3kamTN8jw0gLhJX6AOTuGr09p2tl8a9kYxwgQ2UjtAiDc3iMU4U-HTz7en7X8zp9F3jxgtJImvZoRezboNfjLjesW14-04Fe0XfLyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=FY7suZ921GDk3gO-1Jo5f5HUUhMFIDXY8UNINMnXCCqA0y1IKj7b7j3SAPpLgQ5-DcdWk_8iFJSe3itPMarv0zLdAqRJWzX7XLFBqlJmhwwohOI4FzRa77aJEGpKQnzlpjWSHx6kXUBaw77r1aJTim6prToikIGUMnjpJGFaYKRkzzEEU1NJ9vYzReNU7Wi9V-2gB1SQk6WHpKD9tTsOcaZU9oj6sr3hZM0ymQBM0RL7MOMB3kamTN8jw0gLhJX6AOTuGr09p2tl8a9kYxwgQ2UjtAiDc3iMU4U-HTz7en7X8zp9F3jxgtJImvZoRezboNfjLjesW14-04Fe0XfLyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
