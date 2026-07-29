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
<img src="https://cdn4.telesco.pe/file/tii12tyDIUX0tYNVbOdNprZNALc3QaI_S2unNAZ9L21VapsfkSipwbXxvhKrncfo_g2jQCGjqRjlS1jtsKijNKHsEBYdpaPdZTttcFwIJ_oRLzDDeZwxMvWrGTaQqpwbUVbA5O-zN9hXSwDgJx-hPmgWongNbmoDpKI-Tw2lfUSsxs7sJvovM_ZvQZQrRKmq429lKt9_mEmcGoGrfZc8BfFsWyTEhixEprGRegjrgyvvWZZRWDdGy_HGDyQOTz4vU2XFhGP58vWonSBrfvPwN9aakEUgBMjsaZg7q6M8ltyX8Qg3iw4AhNKN9zVoPv27jzMKxc_SKkxbcHMS1crInQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 142K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 11:32:26</div>
<hr>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=nDyxe39lrg97YNMLWT-XY4i9OL0qdyr3HQPxFyBLWRxyA_aDZTHgDCyD-xs8FVw9JlNU8DbaWLBuFfnpqlVCwK0DLJFBTXQheGw6KhqokszQgWYtPebsw81arUbh6026juJHHP9aBrSodnfDn7qF39TfIBvTVLte5Zq0TOz0Vw1rxwNww_eFLCMqJjsrT-rFOO-z-JarDrs9RZbjABfS3gsT684JtRgh_42cicc2DteDs-mRYD2muRkc34BOEv30PnPhXJh0ICGcydeTBwXYm26pKz4hOE5h9IfWtlPv-7UQtbyVhDLWlYsOxK7WhWbrGPoNF_k2AdXsTFnk2jnV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=nDyxe39lrg97YNMLWT-XY4i9OL0qdyr3HQPxFyBLWRxyA_aDZTHgDCyD-xs8FVw9JlNU8DbaWLBuFfnpqlVCwK0DLJFBTXQheGw6KhqokszQgWYtPebsw81arUbh6026juJHHP9aBrSodnfDn7qF39TfIBvTVLte5Zq0TOz0Vw1rxwNww_eFLCMqJjsrT-rFOO-z-JarDrs9RZbjABfS3gsT684JtRgh_42cicc2DteDs-mRYD2muRkc34BOEv30PnPhXJh0ICGcydeTBwXYm26pKz4hOE5h9IfWtlPv-7UQtbyVhDLWlYsOxK7WhWbrGPoNF_k2AdXsTFnk2jnV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=dNMPk1r9DhONkAz9W9O30NEI1dsyiaCgaZb4MSXO3DVzljop7c5ANlkcnEXyILDEf2c_PlTU1idyP5VNkx6UBf5cRJHhcKm1hQAzmqsCFkGVUE2wxzFI3C7pnjTNMO-fHVD7Zqt116yu_CcFoygO8p1l9qu5wzCVnWsjkGnw9yM_gHy3VnOUR2RiWoLU5slgc9V63yKQGqbllD7KbmMm9eq4JVSv48pCCNVw3ZgKlXHax3xRxIov9jfGGssn35i7P1anCTDRBOBlsuDKyaG6MoWEaVZEMehjgzOpJvb2Z1BMk1qVi-r1YXyZ95Hlbh6P0dnQheXz2NEHGiYO2T3ONg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=dNMPk1r9DhONkAz9W9O30NEI1dsyiaCgaZb4MSXO3DVzljop7c5ANlkcnEXyILDEf2c_PlTU1idyP5VNkx6UBf5cRJHhcKm1hQAzmqsCFkGVUE2wxzFI3C7pnjTNMO-fHVD7Zqt116yu_CcFoygO8p1l9qu5wzCVnWsjkGnw9yM_gHy3VnOUR2RiWoLU5slgc9V63yKQGqbllD7KbmMm9eq4JVSv48pCCNVw3ZgKlXHax3xRxIov9jfGGssn35i7P1anCTDRBOBlsuDKyaG6MoWEaVZEMehjgzOpJvb2Z1BMk1qVi-r1YXyZ95Hlbh6P0dnQheXz2NEHGiYO2T3ONg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTGZyj8yLFc8tJ52ej5C2aIR8eLS-flrwkPArKO1nSj_64cv4J3N3ErQe_vXPXoCi4qRYRny3BtG1rKgaYy-76M_8tw1f5ltJctqAD93n6f25xJ4uMc2jaaN6kZN_U4qPRlUUVitfqqnKQ6uCAvOzmX1AHEQ10HT5PMCm1SYJ3G-eagNmpy40PUF8HCIzTslbcimV-RyVrpQj8WRdrVMme4ZelcwGu-rGXI1E9DPp-CxpyvSWwQk5tSibS53hWDN2iJjymLwfedb2dAVcKgxpJy3ypwHJY3DKva93lCd6rtxRHPLdKrpoyu80f89m3rLN4oj-ZpUdhWPUM1Uv33MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=LdQwf-7_WLo0HfB4aZ7XDGfxyval--2h5GEhbyHgBO9sZ-gQsD_cMfq2QkdFGl5ShNL0wVwDXW1YHLFa-Nklqkfi20-GN3x6ZB5vVX6ltOZSDlEp1JzlWWNYAHbX6DPXDjau7wwnBgQfcV3xA91H2kqZpFq4dDjV_tFXpLpDSuURiCESbk8I3sOaUEt0xyTWOBARpCqo-Z-bBv2XAic7XnpAinSnStwUoabommEtUzyOKhU2JRcNJwZqQKTgxCkJ4wJSw8AB27znQ1ahSvlwhT5c7AO8laEVDWit9xVVVpf_wXFpjO5MUxBKiqgDnoOKbA_qLfNd83gYUoUjusN1sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=LdQwf-7_WLo0HfB4aZ7XDGfxyval--2h5GEhbyHgBO9sZ-gQsD_cMfq2QkdFGl5ShNL0wVwDXW1YHLFa-Nklqkfi20-GN3x6ZB5vVX6ltOZSDlEp1JzlWWNYAHbX6DPXDjau7wwnBgQfcV3xA91H2kqZpFq4dDjV_tFXpLpDSuURiCESbk8I3sOaUEt0xyTWOBARpCqo-Z-bBv2XAic7XnpAinSnStwUoabommEtUzyOKhU2JRcNJwZqQKTgxCkJ4wJSw8AB27znQ1ahSvlwhT5c7AO8laEVDWit9xVVVpf_wXFpjO5MUxBKiqgDnoOKbA_qLfNd83gYUoUjusN1sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=cutrD9X1GmzNSmEU4egm7NtBEhZbjJs8y3HQowJ6yzAqru2-HWbFIMj1a2A3s_AA1KGSu8s3MP2woU5veP-fxp3zL6eO7Z7djylipZQAtvEmTHkz4HV4pWmaS2e-xdhmpVikoBvbI7uJb8Q3LFpZ7su8s4z2V1tkO8Mh2CaPGI3_zvmXzCXAenNyGqptaXVbdK29ahdU43e8wwEM2QvP4elbFPiR4P9vVBr3VUV8XDGi1F-J86VU-G1Cl18vlQBpMjtPqKESNvwZcbFOny2Y_UNdndxQffPp4rGx-s_DhlB_viD1yjkaiDLT-1ZJGfpdwLB6NcJGxQK4VhzAJb-VNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=cutrD9X1GmzNSmEU4egm7NtBEhZbjJs8y3HQowJ6yzAqru2-HWbFIMj1a2A3s_AA1KGSu8s3MP2woU5veP-fxp3zL6eO7Z7djylipZQAtvEmTHkz4HV4pWmaS2e-xdhmpVikoBvbI7uJb8Q3LFpZ7su8s4z2V1tkO8Mh2CaPGI3_zvmXzCXAenNyGqptaXVbdK29ahdU43e8wwEM2QvP4elbFPiR4P9vVBr3VUV8XDGi1F-J86VU-G1Cl18vlQBpMjtPqKESNvwZcbFOny2Y_UNdndxQffPp4rGx-s_DhlB_viD1yjkaiDLT-1ZJGfpdwLB6NcJGxQK4VhzAJb-VNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=vGImj1bxQvz1NswauDzss8GvC0-XWz6d7Dnwqd9U3F4ZsEYO-2hWV11zup654ipLncBKax2BhRDHV7DBuKjiFY1XM6LbMpxVjMD48W7L9P8ETXN7qUXsGg-1nPXK3ofOnsJhrCWHRPFBX8gUtaZ56V15G3-KfVo_AwAkLkQQzLBsmM4BjdZ1asWTIGaGLriMxABCFyKI7uA9d-lQ04lQXc9ZhRqBQ7SBDxwHJF39a88Z8MyfXCeNp8sPSUFulZjIlh2vHuqny2y1HA4ET6yzAqGh82QqTU7J9JwzvRI86HVMQLoejKWtuYpCnZ9H9J_6UKiLeAwSn1ycBH6DqrLuNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=vGImj1bxQvz1NswauDzss8GvC0-XWz6d7Dnwqd9U3F4ZsEYO-2hWV11zup654ipLncBKax2BhRDHV7DBuKjiFY1XM6LbMpxVjMD48W7L9P8ETXN7qUXsGg-1nPXK3ofOnsJhrCWHRPFBX8gUtaZ56V15G3-KfVo_AwAkLkQQzLBsmM4BjdZ1asWTIGaGLriMxABCFyKI7uA9d-lQ04lQXc9ZhRqBQ7SBDxwHJF39a88Z8MyfXCeNp8sPSUFulZjIlh2vHuqny2y1HA4ET6yzAqGh82QqTU7J9JwzvRI86HVMQLoejKWtuYpCnZ9H9J_6UKiLeAwSn1ycBH6DqrLuNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=MsCAC8akjb_WkApy_1obh2DDhThBI8hZNmbbmj2x3hLeMImgnwiM3v87lgpamc2V7US03KSq8XtsE3SQjEBDlVjiiUAHIqtzGxhHWopU02CBibWsEUCTBiU1cJXElnM9cmBPAEuLKoayOVYsWxL81uX0y6N2tC27ibWuK7Kus_fKgcCVSmQ2waVT60AH2ha0jEoiWE8TfklDVxyBOjSCd6PiLmyYv8BA7Z9BYqxEvkSMzfvfVnYHh8Hv-Cu8G1bSr5BASuMqrR1FKXF8fWJol2OTO_hqGItQuHZu1GlNo9os_lCzA3h0k1_e80NhEuxHMoN55cZvTpiFZ1LlYO74BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=MsCAC8akjb_WkApy_1obh2DDhThBI8hZNmbbmj2x3hLeMImgnwiM3v87lgpamc2V7US03KSq8XtsE3SQjEBDlVjiiUAHIqtzGxhHWopU02CBibWsEUCTBiU1cJXElnM9cmBPAEuLKoayOVYsWxL81uX0y6N2tC27ibWuK7Kus_fKgcCVSmQ2waVT60AH2ha0jEoiWE8TfklDVxyBOjSCd6PiLmyYv8BA7Z9BYqxEvkSMzfvfVnYHh8Hv-Cu8G1bSr5BASuMqrR1FKXF8fWJol2OTO_hqGItQuHZu1GlNo9os_lCzA3h0k1_e80NhEuxHMoN55cZvTpiFZ1LlYO74BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWnjfiksSHODzqsjSoMpCGguSDcm6QH6LoZuHS4DlYqIeB4G2s_yXlAfGZpFXGvmJFTcBmMBr-QvLaFtN9f4SuZVr2EF6iO9rAndrK_2bu_vjF_qFVJlVv13KxWEIe3j_eWKvQLrKXxbIoFcM7H5NHGCt3tmwu_8Usd3vLRTlturEqIRqLBwpdM6lAQOic0X_NLucPYeTnEglw7uTBvgIOTcCTM6AJ0RVxFAmEIGKo2b4mJxCu3Zc9Scu17JRmH_e90fs54nac9HMNn1Jipiu1qHMekKu22qrJ3vGaTHUCITWT_TbYplR-S5ZGyEaArE6AnJR5NFniRvUdjEfOKHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVws3qCMpZh3ZofX1NPDxICk8qY24h-ezbXDH902NCBC9HL1fWDc0DNHrgT7gyvF2JP_eYtFjH7_mpU11YnIpCFC-TdPAvyEPqE5Xe3dtruNkvwAJHJTnaTmnGFEXyOV_XPpuE0EuQsCq_eDbcxQ8eZvdMcfpT9D_eIePZ54mmtzEIEZ2pXbNfLf-ZTI6KtOSXZQFXGdv0gQb2-p-MrqT6hYYW1-0ne5eb5US4rNOwNPRyHrVsWxj9LwWlB-rHGbeVc66dYY14wbG11svc6wCuntukoL7eMvcd-haocadL1AhZbrGSqKnPLBy-CDD7uvthPmX2ru63xlj2oPboD7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=e5Z7cTrGiRopGnM4yA-2XTQO-vtKynYKtuCVbAJTkTipYB2efHuq20og6LqfDlawB7ndBmBDqQ0uiwFPjsZ_QAw2QES7aBMSGeF6dIPfsPOnN8QRdzf7E3PyOcb_ro9WGD2htlCwuXmQSUoLQ3It8dhD8geM7tmIKc512fs6RosO55owexuNbQ-K0dzI_Q8Zsyi5W34-ASbynfBcq5Z_FyF2nTvfI77v7RJb0RagpQ7YRVczrSV5rJCc1dYMjz7khW3bSvN7j82g_5Kk8gi1w0eA_luMnPUdKfNjvHZ4CW9dVqPFkKMR0l5O1KQbQ1lqOHGAQkxgym9pp5iw2UIcgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=e5Z7cTrGiRopGnM4yA-2XTQO-vtKynYKtuCVbAJTkTipYB2efHuq20og6LqfDlawB7ndBmBDqQ0uiwFPjsZ_QAw2QES7aBMSGeF6dIPfsPOnN8QRdzf7E3PyOcb_ro9WGD2htlCwuXmQSUoLQ3It8dhD8geM7tmIKc512fs6RosO55owexuNbQ-K0dzI_Q8Zsyi5W34-ASbynfBcq5Z_FyF2nTvfI77v7RJb0RagpQ7YRVczrSV5rJCc1dYMjz7khW3bSvN7j82g_5Kk8gi1w0eA_luMnPUdKfNjvHZ4CW9dVqPFkKMR0l5O1KQbQ1lqOHGAQkxgym9pp5iw2UIcgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVPNx4Zlp3YrRdTdV4xsRDe0Q-Qy5BtS6q6MeCeqGQocKvL2iDAtp-j0Dwb6l-T43h-0dzXBxuNAQQzT-YfDVeh64hyKzXygctRuJT4hmSMjEZ52AmAqjaCiTOoOG5QOtbXfRGPUkIWWNDNwQxNGGlrBBgl6sa26EbwaikLNVH8UpaXwxmBD5aPxS8bcRyQcVNGzak7Le-oLsuy5VHvobkPNnfVBKObeuXTbQkZXJWskfegwXKl3V2x872GlSeV5Ky4jgOn1-_dqIdC4fuqd2Vx9zCWDPsZYYMYHuh8367iPDuF1tJJ2a2RaoJmafJCENsglL1J32pk-OC8unAuMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl9Lw5bw4Ch0NaP6EC4PbNHSO9wHIvSvQsl0BF22syZ7qFAO8TI4ugUonPz4CCjuder3T4MdQAiDrfsUr3Zz4CzKdEr36wW3iQxLdV86rBLqffBJwT-2n-s5b704NWzLB4OLS_h5wcX8LfJzHb5XNLadO38TuPo82wFRt38PAZtdz8NGybxRROs-gM8L9_BiloxdBiXQwqJOphrQ-19lbp4F16yJpIL3pqckd7bEcXYmo5jmYc6qs_khvhfdzmbVhbecEkJFursVcd81yTa_3GJEK32oEprQ7Ge9-17MdBPqn8OYPqVhnS5lJKJNydDs_lgYMEIL4PwP5RHdT3G66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lnZ3sOx5obt7dheNfL6aWJQ8GqwAOXfrLFpXxOv8sALRVJU0FcjEtwxMOjfJ_FQ3s85u4D-Qo0IOmE5zoZOf6mEoHTRAL7WKgSZUFl0M8kSnpWeVI8w5NtP6Gs00Jk2GV1ZRI9lIrUZ1QnJlCYawdlAoG7G03BKLxlUMO58ZIht-y062D8J-edCWcF-XGCYvt5tC6XA3DmFid8XF9Mx2rahG7I1P7uUk9EDOKt1BpTDrGiXU5mWrBv1Ps77fhs_rBu0qYUaTi1iSK8PDm1vHumIOg_C6M5A-_2HcjCwx_zIaCzKr4bbgZ8CY8iBADCZOfuJjE0PQMfL64uVxZDcR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pAGmPjSdxWBxi3ps3gKf_XhO0xrjwWHBp84ZVyq3oDbHTA2-9vLm5wj-bBFVQOlwD3dQVIYEmqqIxW24ZGj6GGl_HQulaI3oDh2vix33S2FNMC1_OVA1xcltpm8V8-u4KCyEfkrfXcy01p0aI0TvGzPwZSlShYIpSyo9Sr91UVUflLd9WzVNMhL83JiM8RMNm2pO5LcLQRblet6QnDEAQE0CHH8yDO6y6IHFs8oaRyn8bC_vcTIRgZwvLMGsNH-O5ppSDQVQw_k0q7JfnwhnNXVRWSX3WaRwgnFYgGuSXssEqWpGjTr--GNcGLLmVutmMGAyiGwEiq2uG0SnGx2Xcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=rXWhJc1M-9nS3RSejfFDvkTBmZdmVRmWEH_Q5f58LsKE65da8CKr45p0ER9540ZT_8TpVtte5fbZXLeri05cF3P-_C0IDqy9YUiVVB1q92yI2QMxbLXA4_w22IZqvEbx1auMt3FPwC-JHhaqCJZzEQTxZ1vU5J7pCGmmfkIItODLSTQ2frMuzuuNmcxSSfMnXs6dyEMHYeM6pdLCiuufj3z6bFbqpdzzUsy5vk-egFl__305-6HIofQDO5xt156BEAb0df74mPkiOrGMfqvQbZUh5sVRaVkvqbob0J2u3luSP_przCoQ30fiQHiBBwM7fvW5fkNkbPh1mXYYQ2RiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=rXWhJc1M-9nS3RSejfFDvkTBmZdmVRmWEH_Q5f58LsKE65da8CKr45p0ER9540ZT_8TpVtte5fbZXLeri05cF3P-_C0IDqy9YUiVVB1q92yI2QMxbLXA4_w22IZqvEbx1auMt3FPwC-JHhaqCJZzEQTxZ1vU5J7pCGmmfkIItODLSTQ2frMuzuuNmcxSSfMnXs6dyEMHYeM6pdLCiuufj3z6bFbqpdzzUsy5vk-egFl__305-6HIofQDO5xt156BEAb0df74mPkiOrGMfqvQbZUh5sVRaVkvqbob0J2u3luSP_przCoQ30fiQHiBBwM7fvW5fkNkbPh1mXYYQ2RiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Np6jWug_8XF6bS8b50_H43Tqn43_amxN1woYDpAFeoMwygHWGfsGrxqJYha4fyROPt_CgN62_9k-lHq7BRDXUqm5cOZXS6c_ezTBjiPtLIF_eZ7LP4dCso8hJ4-Zn1p71BHL-cbZGVhvTggNC0e_qVLFsvsa2QA3ye0hk0VJHbOonKbK4Q0xOdWrgZKtR75_j9BeVh3GRxcjoiQJGLF9N8N-rp9gm_rdbdmQRUderYLI-H-jy5nhWhH1kE9Myxq1uEt4_9DUB4HgUrbNB6_r5E76Br2HWl_8Uu-kIAq8-KVnBpt0Vbq2_hHGINFeg_46qqpdOnyREzIrdwj5WMX_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=ikgAPoh50KyX-H9CI9yXR2kL12Ngb_gzEUGGrEoIOSMy3vxtuFxSNxKYtggn61HnBaQQl6wRc8FGYxqizKoyGrs6X46D9oL_K_bX0N68WS4zb72D0q1QdJVU0C1zWlnoBiA0dCh--RirRdfhqPnJfiofq0b8E2h46Qjxg52mU5hgXY2FST6eqTIbDsG4KbXuwgtSeltJ2qSKokm-kU_qOfqL6qup5UX6YNDohHwZ4VbvDkNLzmb6Q7F1xJGCmNL5OMetXf4hq8bH1P3HlnnL1IxvfP8R-DzOhl0vt1LBSFz6ZPZm-QEkRXPqy_qnoNbXznA26QCTYUV-BmiN2vk3jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=ikgAPoh50KyX-H9CI9yXR2kL12Ngb_gzEUGGrEoIOSMy3vxtuFxSNxKYtggn61HnBaQQl6wRc8FGYxqizKoyGrs6X46D9oL_K_bX0N68WS4zb72D0q1QdJVU0C1zWlnoBiA0dCh--RirRdfhqPnJfiofq0b8E2h46Qjxg52mU5hgXY2FST6eqTIbDsG4KbXuwgtSeltJ2qSKokm-kU_qOfqL6qup5UX6YNDohHwZ4VbvDkNLzmb6Q7F1xJGCmNL5OMetXf4hq8bH1P3HlnnL1IxvfP8R-DzOhl0vt1LBSFz6ZPZm-QEkRXPqy_qnoNbXznA26QCTYUV-BmiN2vk3jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkS-Y--LMqBwb_dh_RiFQs2vYgFWEOLgoGld3r-ux-L3aWfTcHCuR_AZxI7UYexSvO_vpmUN0st4-wKD3L1J7SQTQHSmZ9FjbnMQR5RgJl2OZFAy-R5VmQ-Q4vqUk6zwQLWtJs1lQg9G6YaHH_7ZJIEcAimEQ7bbr2MJZR9oBvJuN-xgztXz0lK6PBKP2p8hDyG05dLB3pUGgJssTqh2GkfBsgcx-lhO_t2haMuhg_oEHfi02DrL3Z4ljcCzi_WBBqt3Ees1ncv7AmL6xvD1cIzPBHt686D_XTQmaWkL73sVd65s5wZIaTzSLKQ88PqIe81BsnsdbKX2K9OgtcDFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzRI1UxUcIRXPMIGEClm0EjhRtcABYh2HdAzpL8okEhlmS_qanu5tLODnx9pa2BhAkEJ5XiGild7Achl17JPzQPPuWurgMML9nZJK3Tuf9auvkZ0HcWvLyy3_sF2_8tHabvcROgn727ocCOTqZPhNRj4VB4REs5vgaInx1ooLsOz2r_gHllm1fPp-ouRksNskShMPT6JFza-HfcGE3C-whswP8s3GZkg0L3BymypfGbn1QB_cHSNtX-Sy7Tlv5yJ1J_T61cs-7qBm9SInJL-p_cK0NtITd844QOMlQeXPMD2kT2w2EbZT7w7fNl5Jqj1IBPL9Q9A1J9kjSmrwqLWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=Ei-kPnCOc-3qdXUgFMTTkmckeGrZxte__qs5OmtJKcwWBg4-_pisnMJb7q_vB6YbKN3VRALbRoFzvd3fS3cQf56GD5CEodlTMNbcqBDviyLMxqkHVi6_KctfKljjDI6xGoFWvGaoRN3JLE_uK-GXkth99LFndy67ljkzJFr0lbdr9AqH5F_5ZfvG0aDzLeVbQb1bjZuIvp24s-A2XuxrWCLeeB4vvPhBUkEVhU3P70kESpDSqE97JGULeJ5ctVJtAI4CcRuTuJxWQXgW5q37z9w_joCAl2L7CoVahUk3-DE0_DTBnKpqibdxdo_cdsa3AUIdY2wfduSEOYR9rV1SKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=Ei-kPnCOc-3qdXUgFMTTkmckeGrZxte__qs5OmtJKcwWBg4-_pisnMJb7q_vB6YbKN3VRALbRoFzvd3fS3cQf56GD5CEodlTMNbcqBDviyLMxqkHVi6_KctfKljjDI6xGoFWvGaoRN3JLE_uK-GXkth99LFndy67ljkzJFr0lbdr9AqH5F_5ZfvG0aDzLeVbQb1bjZuIvp24s-A2XuxrWCLeeB4vvPhBUkEVhU3P70kESpDSqE97JGULeJ5ctVJtAI4CcRuTuJxWQXgW5q37z9w_joCAl2L7CoVahUk3-DE0_DTBnKpqibdxdo_cdsa3AUIdY2wfduSEOYR9rV1SKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFKV6ENmw5dSpLOS4hhnIQFLxcD88R_aT-Lzkqiptw25hZkm7ujMOhrFR11Pc7vwch78ek-doiPi8RTVjU4Kt9HZbM3MrSbFsp4G7reFDSKUUNP74QAoj2q6_pZuNJ7rfQeUeeZM_KVuRbzS9RU48Trh9i-Dut0lkROxqF1Z68BpgPiHp33K4Dc1PjeQhNSlZRXQ51tlvPJ82v_wgCAxIAxuJlFerUdxmftwprvaP1C_qjJzQndkof6wWY5K9Hj9lQ6Uixaw7Smv1FTVPkmb6hd5rWc5g4CHAqrXVbdHT3VHc0rxUnrDx7PTcvqLxoEWr-LylifBRkSrqhWsGCdpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=a-UXQ9nUnSB8-gr9npqV2P3GQ26uZrnl7p-MXgv_TtcVD1RbbUu2KG6Q6Rdn0zxnBytKGRKxaTHrGsmyM4ExjW01lJ4758Q8PN9cZEFNZvtRthRwjoqAoZbxHYTE5t5SbhEoEo11qyMT2sMdsYU9AAKLwXl4lK3tvPifq4FzIZDReldhRGzqcFknY5_wmhhDNzSyWOqL1vXF67iUSsCL24Zrp6aFVfYK0Dg8kK79UQAzVNN8Fojsj-kU8plRYxjaQ12VmFP-xR8HBnvz77AoJLB6hnW0uA5BeekioQXGQb3-WrfZvN3Di0Klm4OYihDWyIN2FmXxYKO7UJM_OgABsC_kDayBD-rrR4_er2Y4LI-IxpgtXML7ZgK750vVMc21XqlI4abIn0hsKW5zCdOvQQ1mc4asu7lCCwG6wO8ARBi6zjSaDUAFf4FSqgsDrTGfp4TL7WSx5X3hEfoaU76Xe_2nYpbAt9I2Nl3EzbPTRTYi5BpfNyFH83cp3tg-hrPgZzoCNTUTKcn2SFyxKUBnXksCZt0FIa_oeePEZhEaOoDyUlhtnHNU3tiA5M2n_HvicnJZ2FXYIPmt70VFh4An6NQrMCI_x0m0QsmYZx1tqQe1yPDo1SoQ0nEcKiPjh7gyledC7P7nNc2J3cJyEmWYvMnWaqYxt4WE3nrZmag57fo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=a-UXQ9nUnSB8-gr9npqV2P3GQ26uZrnl7p-MXgv_TtcVD1RbbUu2KG6Q6Rdn0zxnBytKGRKxaTHrGsmyM4ExjW01lJ4758Q8PN9cZEFNZvtRthRwjoqAoZbxHYTE5t5SbhEoEo11qyMT2sMdsYU9AAKLwXl4lK3tvPifq4FzIZDReldhRGzqcFknY5_wmhhDNzSyWOqL1vXF67iUSsCL24Zrp6aFVfYK0Dg8kK79UQAzVNN8Fojsj-kU8plRYxjaQ12VmFP-xR8HBnvz77AoJLB6hnW0uA5BeekioQXGQb3-WrfZvN3Di0Klm4OYihDWyIN2FmXxYKO7UJM_OgABsC_kDayBD-rrR4_er2Y4LI-IxpgtXML7ZgK750vVMc21XqlI4abIn0hsKW5zCdOvQQ1mc4asu7lCCwG6wO8ARBi6zjSaDUAFf4FSqgsDrTGfp4TL7WSx5X3hEfoaU76Xe_2nYpbAt9I2Nl3EzbPTRTYi5BpfNyFH83cp3tg-hrPgZzoCNTUTKcn2SFyxKUBnXksCZt0FIa_oeePEZhEaOoDyUlhtnHNU3tiA5M2n_HvicnJZ2FXYIPmt70VFh4An6NQrMCI_x0m0QsmYZx1tqQe1yPDo1SoQ0nEcKiPjh7gyledC7P7nNc2J3cJyEmWYvMnWaqYxt4WE3nrZmag57fo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=Y5oWTn_XRRDfzKd-BfVJSjV3IVFM6-__-qND_fZpBTQvIQo3-3rI73nuYtY04LsU2NxUzHsgknP_47y1NBh1sKz1rZelK6LdsS8Ep-PN1EBe9zUJWVjJ-J0ConDF5kLxhBbXV0v3dV1aRR86SmO8ZNu1Evj0wcnCX7xfMdBn-zcxPXB7aENewr8_j_ZLtQBI-w1lBgP7oWzkveoa9VSrUxI0rsZVsc4ODScgGft2ONLJsDT0qZBV6X1KUGkFnJRAe5kFyMWo_jtXoeinELYNn_hqx-Co5sY5gHibOOmNssfBPo0q97dyd13CwckIDh5zVnh7KXAiHUKh5QkBs9lhyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=Y5oWTn_XRRDfzKd-BfVJSjV3IVFM6-__-qND_fZpBTQvIQo3-3rI73nuYtY04LsU2NxUzHsgknP_47y1NBh1sKz1rZelK6LdsS8Ep-PN1EBe9zUJWVjJ-J0ConDF5kLxhBbXV0v3dV1aRR86SmO8ZNu1Evj0wcnCX7xfMdBn-zcxPXB7aENewr8_j_ZLtQBI-w1lBgP7oWzkveoa9VSrUxI0rsZVsc4ODScgGft2ONLJsDT0qZBV6X1KUGkFnJRAe5kFyMWo_jtXoeinELYNn_hqx-Co5sY5gHibOOmNssfBPo0q97dyd13CwckIDh5zVnh7KXAiHUKh5QkBs9lhyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2El6paZCqIWo_l8GWyHPhO4liUzKK2TrkyBnU_zOWIubPDfyD8wzW7R3Cf0_lxpOH4g6lDjpEumfBTFTLiyzNeXWKJyTa_FjaxpEuE7mYPgTK6_0XuGk2y3_ZR1_I76i9ThPf7ne7vDd71xF1PcVEJ-YAWcqM-1PHkfRViAi_DxcH_2H7KHD8QzkyA0BxKlWvT4h2GrlhsK9rdCtuIvZQgsodFXVQMXtZf42KDgsRidi1UfW0RLbP1W9MeZJYjyj8b-96OglrAth3SsYYHkhX8aLbg1DlX1PRk1IEHaVhVbbWzFMgCTZ-G92C7tKeU0n6m4wTCd5ggo84hymdm-3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=uDNwiIuuzspbN-KI6aRQHDEB2yPbI5dtUe1WQlQM8KbIoYs-8TwBYkzx9xJ4FGc8gXKCxirsKC7v6AM8HYPODxkGibZ8Bi-FXMwCrGPL73fH0iKASUD7j0TeJocdzPVWWASCekzaMGOupza_Ap9Nu2wzKchuts3EZDX10rlz1zl8RFwOwdPYkfWgPOjLqPWZi_A5vD5H2_fbvwqXUxSTSDa_jRbXxZVqnKevqgxjn7wqqwhkgPyl2fJ8948bRlxRzK7HJ8V3XvQXK5tQ6JV18Q15T6cDTLoZsHJIQJ50EgjXZvdzbjW_Ewf0nQ7ZFsyBCeLPgnqVnss6KEkvAhEYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=uDNwiIuuzspbN-KI6aRQHDEB2yPbI5dtUe1WQlQM8KbIoYs-8TwBYkzx9xJ4FGc8gXKCxirsKC7v6AM8HYPODxkGibZ8Bi-FXMwCrGPL73fH0iKASUD7j0TeJocdzPVWWASCekzaMGOupza_Ap9Nu2wzKchuts3EZDX10rlz1zl8RFwOwdPYkfWgPOjLqPWZi_A5vD5H2_fbvwqXUxSTSDa_jRbXxZVqnKevqgxjn7wqqwhkgPyl2fJ8948bRlxRzK7HJ8V3XvQXK5tQ6JV18Q15T6cDTLoZsHJIQJ50EgjXZvdzbjW_Ewf0nQ7ZFsyBCeLPgnqVnss6KEkvAhEYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=ZgrY176nGFLqS3sw-5KRj8C0IlxRFOtM4_i_r-JkoF6leRQZr6dtM-4v2nuMTN2g9TXtB2cvWQ7ai3dNEagJm3jt81BVc_2YYXcJXMMWhn7-pgrzLZwSam-Eq5Djn-Xme0itd8YBodjHF_lcTAJnzOmQZKVbHE9IihxR2DckB84MxbNtx-8pDmDoeaN3yasMEesQ4TeLZklLDCjeS8SW9260_CnnKPk9z3C86wE0Hj7YNfQmaHRnJWyGWtesOwEJmITo7KiFupEsf8uFnwonG1ELeGDsEdAzAneYTk4CNBGzuD4PFb7EkwuIsY22K4y5AGLwxK7ZlTGqcSX-cRqc1w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=ZgrY176nGFLqS3sw-5KRj8C0IlxRFOtM4_i_r-JkoF6leRQZr6dtM-4v2nuMTN2g9TXtB2cvWQ7ai3dNEagJm3jt81BVc_2YYXcJXMMWhn7-pgrzLZwSam-Eq5Djn-Xme0itd8YBodjHF_lcTAJnzOmQZKVbHE9IihxR2DckB84MxbNtx-8pDmDoeaN3yasMEesQ4TeLZklLDCjeS8SW9260_CnnKPk9z3C86wE0Hj7YNfQmaHRnJWyGWtesOwEJmITo7KiFupEsf8uFnwonG1ELeGDsEdAzAneYTk4CNBGzuD4PFb7EkwuIsY22K4y5AGLwxK7ZlTGqcSX-cRqc1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjYWkoKF5AiOyWrwm6ONL03y_9wQvY2SWpqyKkM5smfVsxQ4t1caw77jt4MAxmoSG5GVplAF0tP8fD4SVhEi-nZC3A9UP3MWpeEt19ofmMGXpPOx2on4jcP4MEC6mcDDa45vgqRaYxhp0nex-p97KlX_TbTSiL1TL76RXym9-xzC2IdMq0Xj9cZsPbKRILCfaA015faKwzW1jUV6kjRHHoUTNxnRZWn1_1ooPW5uZGd-IVJh3imcALVuDgUIbWjD9SszZ9HtfdcoF__kLznxTyubSc0IPH4vaSv_bX0LIZr8jee4dLZzXomJfyPSYfI7WPw3uvbmNpZ89hgwuzWqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=StcX6E-7_zKpi-M5-E1wF3hHmZgjlY7A6vu8hddQpQN9u4JRDTv-LadyUa00QMgErsKkvnFbqdphBDsGVOz1WpW1ajEMAv1YYXX22oIDAhz8j2gWpUj1j1DOwJQK7s6AID5Wpv-TcxYq6sdgSTCobQV3b7v4692QrG9OzgE7m1bauutja4TeOX9v0SXM96ED5cjUSePIrvfHIV74LxEiu_MQphdEwfasd0UWJJNMc1oI2DhN8dRFvndziOJNyLo6ohVsLG_lxu-4AFptOSOt4S9trUEzradFhqedIQqFa_nH_1kU7TRm9gXfHQwhcWbOpfuj3Bv9gUq36TPqfWI8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=StcX6E-7_zKpi-M5-E1wF3hHmZgjlY7A6vu8hddQpQN9u4JRDTv-LadyUa00QMgErsKkvnFbqdphBDsGVOz1WpW1ajEMAv1YYXX22oIDAhz8j2gWpUj1j1DOwJQK7s6AID5Wpv-TcxYq6sdgSTCobQV3b7v4692QrG9OzgE7m1bauutja4TeOX9v0SXM96ED5cjUSePIrvfHIV74LxEiu_MQphdEwfasd0UWJJNMc1oI2DhN8dRFvndziOJNyLo6ohVsLG_lxu-4AFptOSOt4S9trUEzradFhqedIQqFa_nH_1kU7TRm9gXfHQwhcWbOpfuj3Bv9gUq36TPqfWI8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRhnq9WgGRRTis0amp3aNkqEgJlE1NUEnlUE-rQb-RIQ5cm0kfbDNgyG1x3JHU2Py9kOJ6XC-Bsuyxr8uQv9bB213lmGE71zolR9RvD1w6R8hpKlYp-aezFPibTskb6qXRpXVDZSsw6zV_fdHzQoWDqWvwp6wtJRvuGy6fCfc3p7YwLP73yWQ6D-kYF7w6q8aqycklu5O8de_OCUxZCaDmnuBQBHGJnEAK3_A2XuHm8aAcCJbJXkYJg_CA0YLniu33hC1cHYq1qG-8JZKG-PvFsPjy6wN6dtZ5Ca1GL_VOcvJ_-ash8z7WVOnuDYdFtDvTdDKJ-uG_o94BpiZeBChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhM8b7ZkZORtPvLDxqxB1Fgmzct_YS2kDdqLkbb0P6-L7LtmNHPlikjdboiXgqSloGjl2CtjKDxkVie5CxVjl1f2zzR6nlo1mk8_8AU9-uS6e5WJrb23i1hat8xXPHUOxMGzEK5f05lx7xYFhxbdDOk3e8f3h7CFlZ7s2hoDP6l7mgd_noo1WM7AzwCGgtYC-2Z9hlEHCTuNUeShqnB74slMRbautCtN4UPQdhC4clF6GjGf99cd5TaZLwk1ZRrzjaczbEAIQwiGC1BD-6h0ftcZoo2A9y2V5kDk1fixgqUWZMSu-e_9WW4OkjR-EmjQzyKWBq-IWdec_5cYUs0XKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrCWcyb9dtFYGjBnS6Lq60Ad7ZYXOVUHFyPPs27P084P9znqL_KXkjhpg2DZl_IloVBqE-0v2cexHegfH2pLLRaSSAT-QCuZ14VEoqqZGIhneSgVr7OlKFb8aJz_8Lr9f20L-w5rzgisTLANiAXn9mab5l9117Rzaqn_We-nF6jbZzB2qfAatT-YNHQs7APBU5-mlMBAO2IiSYGaltewt2cp16ZgCMfaAz7MWQZKcrEFL4OeAk7M6KPlra1QdOI-X-vBdgrZaKNXiV-nD3hPlFlzWJhkJusVMuVL-Z5i29jBLeN-zFhToSwt0_MZijBVEcetZbstM7C7MAvAlEFGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szL4JvpIgvtkOV9g-rqvbn9DWT8DZcgDzhq24uUg1nFVD11fDtFkI8JDP4t_gBe_f0g9V9JGPGltKvsu-esyxicxvHXmZ9nzMyaXIVvazlHo61tdNpfaAi5uy668lIw5Pz8zRu34kvqlDFJa2wqhzdPMbf2UeSt7yyghVBmHpObsTFr2QdBH2h7S8haWLKk-OWXkb8z5dmTFUP3BqkxGvCU39AilD5TnYOB33IJk45LQDQHcX2wCriP5VC9U7Q29kdKWurYwtodqroK7NxruIaUzh1rfgRdPHURbuMfCfEkRRWJ3Y4ZXZOgW86eX2ex-Ht7kPwVwCbWt8rjjwLLghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=QpOWoEityc-pa34QigU-wgp21DaSm-causRLsEg45lIsWgAvvTVH3Q8dTNqYKUxQ3tFW9kCcQL8PMBiEijgsjTZRzsU61fle3-1PrzL3oO56oKXX6Pc3qjgBg9-6KQ9iw3usOWauCVeHcj79yNTfD0Kyy3mIUvL1aWHkI2p3rczw0k3gZxsKXrF5FOb-HOjHtJXcmN8Ry6scozjwDVOVihCIJ6YGZ3j-MJaPJ4_nixxVFlTzd0mPn_9wRp-CSuxEnCsr1izcnt1EkyAnamm5IqsA4ppR4vSc_zEe1C3Y3gdRyLG3DLMVqDlvcGNmbPeEU-VXi6aSuqWY_IGFAZldKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=QpOWoEityc-pa34QigU-wgp21DaSm-causRLsEg45lIsWgAvvTVH3Q8dTNqYKUxQ3tFW9kCcQL8PMBiEijgsjTZRzsU61fle3-1PrzL3oO56oKXX6Pc3qjgBg9-6KQ9iw3usOWauCVeHcj79yNTfD0Kyy3mIUvL1aWHkI2p3rczw0k3gZxsKXrF5FOb-HOjHtJXcmN8Ry6scozjwDVOVihCIJ6YGZ3j-MJaPJ4_nixxVFlTzd0mPn_9wRp-CSuxEnCsr1izcnt1EkyAnamm5IqsA4ppR4vSc_zEe1C3Y3gdRyLG3DLMVqDlvcGNmbPeEU-VXi6aSuqWY_IGFAZldKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8bTZ8DVnWkSbrnfYV_DoEo_GlMySvikpgW7fvbXl77t7dveY771A-nF7xuevTHpie4zyYHghJ1mR4ZPpB7sVgW4u-f6NohPGbPvTczBu_BtXEZoUVwiowmEZWWfuyTltrIgDI9TiVP5iq1rJhZ_A-5SG9bW5tBVs6PJ-CEPYZ1f4YouHDmcW7XvIRvcrt-BZzDF_kEax6fzLGUUN7VO27IJ2S1Bo8iLmEaYKtf5LTnQz9risgG4pUFo0iEcE9lZAJcHoIo2-yoL8NzPi9oSIOiN99d1ykq61T2Q07e-mIqT-Aw2-7z-br4ZHPB9DcFVqrzKbBMshb5kgMdRcg11QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=S9VTpA8wnZep0IMJlCqSB3JcKHieoq-3yvfhfUYfVf9LVrs_jBmC0FK_gs0Z0vLdS5GGvgqtZKXdgVpowgYzfiCJ4T-76veelntAC-xF1-P67_VwPD-WeGGsyyAy8XDyaDBnAafY6ESla4FcdEFJmeSPEjWeNs23Cm0YMxYTulh5dAvcgHYhbv8XiohlgB76uqVwkKXDxDG0WKEtdmjIbVydj7fG3KgP52k_FNUFqFDCH39G8-QkO2sHji30noV7rNcuNw0eIU-4ueUsiE2U4xp2_B-faiPZwwYpbMO1hAUWCUhzylK_1sMEE-6Kr_fMuGTjqz4mCKRRK0gglQJYIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=S9VTpA8wnZep0IMJlCqSB3JcKHieoq-3yvfhfUYfVf9LVrs_jBmC0FK_gs0Z0vLdS5GGvgqtZKXdgVpowgYzfiCJ4T-76veelntAC-xF1-P67_VwPD-WeGGsyyAy8XDyaDBnAafY6ESla4FcdEFJmeSPEjWeNs23Cm0YMxYTulh5dAvcgHYhbv8XiohlgB76uqVwkKXDxDG0WKEtdmjIbVydj7fG3KgP52k_FNUFqFDCH39G8-QkO2sHji30noV7rNcuNw0eIU-4ueUsiE2U4xp2_B-faiPZwwYpbMO1hAUWCUhzylK_1sMEE-6Kr_fMuGTjqz4mCKRRK0gglQJYIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pbwyboe_AZcyK4urxke0dRoA-U5xr2pKMOJDM07fIDSjUtJJpY75qUPoG5BFhx93Y9_4OQwxb2-LVq1Doh9GroXFaVxP6S4FO4KRYizDEFQnA2pCR-1IY3eMa_lQyFySg0ZYXRx6HTL83gwhDebMOueDqduzK_iqcx9hDnNNmscKTA5Zyj0edOwk-u9bbS1JxkaagiPjmAVvIOQTbgbX_9mYgTM8FtkvYZtRkuI69ETwjEEkv9IzluX9uw0sw9qs-ETp1jxkpBZidMPyijd3Do4oGP_5I8LbkWnwj7L--g5TkQHwlQOqGHNRUfkafgLopiWwXoEpxwyAtG3Zt-HYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T29eF3wiU0TtuHdVK9DSqiyQY8EF1AZnxRmyuFC7aUEisbubmbJnFiPCP17GQEOIhMVEY_e4UGRfl1sMzmiFQzT12D5DWJ5RuJhPP0XkXsTLKFbEj0EXSD4rgKpbJ1ac-rjp2qgtv1Y3ZP3xkZD7OKjHm2Z-hG8zy2uPFHdOHstGxVgNhhLRkfNSYuo4VhCPzsmvQzB9Pl-B3vkhM8E1Y83o3jrujjZ8qLrhlujeVbfD0MG1CgmRuyqo928oeb83PCdmJaqA_j8LgetctsAfp_cEex5Gdqar3HtYYqfQ90IJX87pp4gbk4zhjBmLua8QSQLCQAVH2cqOP2YjjIX_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYFXdWzWpfcRSyHMNNSOuTDYkdHxZzSiNxjInuozz0-WaUPRuRs4-ow7w1uXLvQxrus0vji3TR4ga1OsaxBTyqKdSdAFcx3OBnKMxtDFOTit7YEGFkxyhfisvZ8tp1EF0t52ciAjvIuqVeDsuyomuRXI7Th-7shZyWuwX3ANQGBakUPwWrTFl9w16o6zZ9ZWJ3VkM3_DEAHpApXWSKIULYprlsjS8v7_OTT9aqnkAYSQGIqVJnY6nGMgsYGJz0tyfILOglo5tUXTmopfQQvTJ9NNp6NemRqKNI9gUsODE11rKjOaRHPdd_Nz3R-qFqI0PDk-X0KPvDft4PJcGSxU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vJjJQUVitHMKriGqD1I-GF-D5DAqzMtT03rXkjq-vrfHyky8babgq7t9Yudwh_8eoh1dEiwb9gkR25pwVQH0OUCNpy7VXFt1bP5iWu-eLHO9eh0rS8LI9Hw0fMeHAoJLH4hNhiL39wb52NUxr7Up9kJJB9EF6qhbe8vsu8eMjZy5PXWwtuxGzZIaficJJIY5LpP7CapKSusGdLfM9b0h7UNvJxKwO1-1BXxd9UVHbqoCEAljDX2Q1syUBq8K4o0MQSQAodE9eKPblNT5Xurn1WdwRFhqNBqZucFnu61IMY4SWs8Lj76tq_kfTgMd7jKLE2AXlpsvM2M6ujZaUaE_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIGr5bumye3aRjeKeH5SvHYqig4UOdYVOAwWEiIQMnyeemcjaGmN2BYxCUw9MkI9kyaj9l7g3w2345JAOuDCsPMAXZanMiCI8NGuHVaD02ZMC62lI7EHDuk906u_MLdODe_laXVFB_emurYmaIG3DsEpIJqGhPORaKERdDClozUdFdkz5nN5D27rw04YL0uBH-f4XLwGk7u0Xa-MvKuL4CuxrvheXWR0QDUw0Um-CL4I_-QAE9cp-dZZ0Y7uTPd4BPiqnySeRRJJvDubQmn20_V7OQVCvnvFkQXi4_yttJXHNNdy_xfIGL_LDAAjJhMWYNbvw6BUe6HCHBcsNEcIFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxB2MqQw8ceuxT5bFSgzd3TYPudR2zZpwWt_g3veA0s0N5C4D2-IrdPv7LW-uVLWwlUpwoESqWhxmWjSfDFQ4X4uAxjBjAEBlDmprxLTCif2aXqqLSqZG_ofD_qW_BsNtF6z9QJHaQKnDfCHVmq2_lvVCgwf3Z7nrjg_r9eLvkvx-oMZ45rCw4b0EVvEeldyaYosLxpfvhIg50Wgg6Z_mQyHcIV0NMxrnWMloMFH-9YC5tq2AenvzauC14zSsX9Mxktn_5hVR2vWECaIfNiTmFSYlhzFXlVx9eeVteNmtCTrJMjqEyYlzfa3JTbXqEoYAFwohtcq6woV_IU0lG_TBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEY9oCXfwWPTEhn58oVesfb-G2ZbYErx_JZDWXNsvw_DTwL0pmb7vqFDLkjucqjoPGYFEvWU63yXkxqXP4VgecdZRnD6gMPmPb8NZLMq3NPtdo1iq1GzWw62YQmM1iF9VozH2jjYDitvJo9NIiEhW8GAD_pBqXD0UGU6VFW44AEr5_gcqwO5HJseJVk8sa5brQf1rxT9aXPeH69DBahws-zq8UZYBxWZuRRxtSmaRzx9apBYmxON5a0RqC7SlsREnpKau2ENwcAm5mZ507LyaINR8nFm6DmrkpDI_SDsi666VyPJBdf9hqZT_VptC7Oe7lthH4ZT0oc1IPn8IORZow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=AuGGfWClr5yV58rMVA_Bj8oeEi9gLaxUboj3qVBVbPVSmm2kpdEwezNtZjH8bxlMdPPXPPyZt8KuL5ldzyye-17URfGCu0NpL6VaKZf7ZnqNn7GMgKepIKxuctGCNodt2e4cdaQYhrZH5ThzpN1MjQhzOt6Cdaa_zChjbVGvUjtbkH7S-Tp8dt5HM7GysaQwE2KGwi1dw5JWymqTpBK65goYCy51ZVCRnbJUwtms4mMWOPY0Qj5ivVjEyeuojxCC7PRLjZ_sjWK7LwRL3mhNsk_cSrI4IVf8y-UCPEU9OSomryjfyLS0gkvU_IoKVvXwOgHHoswNjLS5FJUm_Njp_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=AuGGfWClr5yV58rMVA_Bj8oeEi9gLaxUboj3qVBVbPVSmm2kpdEwezNtZjH8bxlMdPPXPPyZt8KuL5ldzyye-17URfGCu0NpL6VaKZf7ZnqNn7GMgKepIKxuctGCNodt2e4cdaQYhrZH5ThzpN1MjQhzOt6Cdaa_zChjbVGvUjtbkH7S-Tp8dt5HM7GysaQwE2KGwi1dw5JWymqTpBK65goYCy51ZVCRnbJUwtms4mMWOPY0Qj5ivVjEyeuojxCC7PRLjZ_sjWK7LwRL3mhNsk_cSrI4IVf8y-UCPEU9OSomryjfyLS0gkvU_IoKVvXwOgHHoswNjLS5FJUm_Njp_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhgId4Y1s0y5aTCAoG_TNLwaHIeLVo6V3roJU4ZVSFDAwJvaUr0RORJHVjO6fcFuhlUJDZMHhWPehZiw920X5ExSsbzt39qudrGmUcANPme0g-MBNwor4t8nUiEsd3l-Iw9vdxc1r-gC2Roq_P_fkGqv8-mTyF73rAWkoa8wY9Ne10I64MJavt7RwUkcUjF3ETJbEgatfWx6HrE6ib2EeCaSa0QHnz30mndqMSPPTJBB7IzLT2NwCtVbYCvD6SOmROWQyMx4QykWclH1jQgeGiLHbOqkMLwJ8iYL3eKXD7vxvdDvWd7KxjFIGx-CjVtlnY3fVY-Yc3mqATN-FS7g6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=NvHGMhBvnUtR0kbwrpl_GWKr4skIl7K8rblHfMFQJvMrPnA0CqQ1nVT1ZVp6aXTfh6TuLC9iuh7LWOjr5Mw1QFpNnSCZgIXULCt8N-NPiZp8CBQa71ZArbP_0d-kzCWJYQ9pFsd6hV96rm8Z3jrKOafPfQ7dgxBhZ6Gk0gMfKpw9bAM1U5Om9y7BKVpVxP9bAfIfUh0aXZo61-1jXFfpsblfKq82EFcf0xceE8-V5kxj1Q2qD3G2rYb6fRI70e8wBS__CqFlKJ-cC65Xf-pp2Ef75-VsjfR1zBw8-iCK0TyuT1UaeuKGEvZ3ZC4e9Z5HWG3I9SX_6gdlnPig7SR8Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=NvHGMhBvnUtR0kbwrpl_GWKr4skIl7K8rblHfMFQJvMrPnA0CqQ1nVT1ZVp6aXTfh6TuLC9iuh7LWOjr5Mw1QFpNnSCZgIXULCt8N-NPiZp8CBQa71ZArbP_0d-kzCWJYQ9pFsd6hV96rm8Z3jrKOafPfQ7dgxBhZ6Gk0gMfKpw9bAM1U5Om9y7BKVpVxP9bAfIfUh0aXZo61-1jXFfpsblfKq82EFcf0xceE8-V5kxj1Q2qD3G2rYb6fRI70e8wBS__CqFlKJ-cC65Xf-pp2Ef75-VsjfR1zBw8-iCK0TyuT1UaeuKGEvZ3ZC4e9Z5HWG3I9SX_6gdlnPig7SR8Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=aWdTwb7NtulH2wrfKCKJWqYt0sTRlx-flmC3uD6bSsc2W8fRszhHKHtUdj2TSgwYvQL-Xu688klf1Fm9b_9VdH7So3N46i3tTm7ZiMi8crvy3xXWDBJCIANtJ5uBZTswz-A3CEirp8V2hUitC_eQbmohGgA7ZkfTU-gCwZeTXOEpQCpKwMvfvRWhTOYGrolvsGl4PsZwBRP0W0AQbqTpXud4vDDbx-G7pQ0Zl5IMqtuqbNS34FX80FwiUsFZ0XxV_ErAZwDEu2ONnaYxwyE2lV5nHWTdJ6gnY2yUPxU9b3pVAUCO5Z4wLcZ_WlAVMOhd3T_PNR0t7QLwjjImZo0MeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=aWdTwb7NtulH2wrfKCKJWqYt0sTRlx-flmC3uD6bSsc2W8fRszhHKHtUdj2TSgwYvQL-Xu688klf1Fm9b_9VdH7So3N46i3tTm7ZiMi8crvy3xXWDBJCIANtJ5uBZTswz-A3CEirp8V2hUitC_eQbmohGgA7ZkfTU-gCwZeTXOEpQCpKwMvfvRWhTOYGrolvsGl4PsZwBRP0W0AQbqTpXud4vDDbx-G7pQ0Zl5IMqtuqbNS34FX80FwiUsFZ0XxV_ErAZwDEu2ONnaYxwyE2lV5nHWTdJ6gnY2yUPxU9b3pVAUCO5Z4wLcZ_WlAVMOhd3T_PNR0t7QLwjjImZo0MeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=gttsBW7qEc66_EoDhJUlmzokbrWpOXCOCesVn-kRC-LC-a9eD_qVgsUhCkTf9Us8-AMae7HfisK2JVoVZVqGP025CCkY5vnFmGquyxcoNhyYA9-4nj6oaCZsrwSguIeqTxJhNidTqjRCupHToVGd3bOTwYWF61OzhjZO2_guIng1f304cmNqe6HI7D40QUXL1r3jXjjNaTnLOYScMJOWeHt7PkpjMr4AyXRuqf3FvzhKkt2hiEoM4iWX4WBiX1gmI0OhSt3W4-XLjXM6Fi_zJ_hhzBeI5MShEbL7ijHyJmu3SYdPyN7iMtPgEC28b9Mi9op26fe4qICv0avzaHvKCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=gttsBW7qEc66_EoDhJUlmzokbrWpOXCOCesVn-kRC-LC-a9eD_qVgsUhCkTf9Us8-AMae7HfisK2JVoVZVqGP025CCkY5vnFmGquyxcoNhyYA9-4nj6oaCZsrwSguIeqTxJhNidTqjRCupHToVGd3bOTwYWF61OzhjZO2_guIng1f304cmNqe6HI7D40QUXL1r3jXjjNaTnLOYScMJOWeHt7PkpjMr4AyXRuqf3FvzhKkt2hiEoM4iWX4WBiX1gmI0OhSt3W4-XLjXM6Fi_zJ_hhzBeI5MShEbL7ijHyJmu3SYdPyN7iMtPgEC28b9Mi9op26fe4qICv0avzaHvKCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما محاصره رو برداشتیم، اما چون اونا توافق رو زیر پا گذاشتن، دوباره محاصره رو برقرار کردیم.
اونا مدام توافق رو نقض می‌کنن. دیگه نمی‌تونیم اجازه بدیم به شکستن توافق‌ها ادامه بدن.»
«ایران تنگه رو کنترل نمی‌کنه؛ ما کنترلش می‌کنیم.
اونا شاید بتونن چند تا مین دریایی بندازن و اوضاع رو به‌هم بریزن، اما کنترل تنگه دست ماست.
حتی یه کشتی هم بدون اینکه ایران جلوش رو بگیره از اونجا رد نشده.»
«وقتی قاسم سلیمانی رو از بین بردم، ضربه بزرگی بهشون وارد شد. به نظرم اگه اون هنوز زنده بود، ایران جور دیگه‌ای عمل می‌کرد. حتی ممکن بود به سلاح هسته‌ای هم رسیده باشن.»
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=dGCGzom_NHB1ZwuB3s2p-tCHbhgUkUTHCyS9dQCubGgksP-tzJhOLysg00JqppdHjkR7tG4m6V5KDp0rD9FZsGWGOWsbHGxUm5LfjvbLlA_fKLes4prDFK1BQ5DWUw2MRPipjGByI6BBAGgIOWl6TLgPLX5rRoA_1z0QwHFiSQmc-3YPf-KxOnsmMGH_1SfKt76mX4KdzkhmsU-1rE_tBLpNFiYhp7yM_WKhKElhTTFKfIwnJgFmhKqLSYSVJtBxRL2jriGTAoGuu1yxowU4-2jC4581-yliWvXR4BDWoWpN6PdXCrqr8Yxa0DewsxUu7bf-5UE5m_qEXvdrqUQ1Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=dGCGzom_NHB1ZwuB3s2p-tCHbhgUkUTHCyS9dQCubGgksP-tzJhOLysg00JqppdHjkR7tG4m6V5KDp0rD9FZsGWGOWsbHGxUm5LfjvbLlA_fKLes4prDFK1BQ5DWUw2MRPipjGByI6BBAGgIOWl6TLgPLX5rRoA_1z0QwHFiSQmc-3YPf-KxOnsmMGH_1SfKt76mX4KdzkhmsU-1rE_tBLpNFiYhp7yM_WKhKElhTTFKfIwnJgFmhKqLSYSVJtBxRL2jriGTAoGuu1yxowU4-2jC4581-yliWvXR4BDWoWpN6PdXCrqr8Yxa0DewsxUu7bf-5UE5m_qEXvdrqUQ1Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه دوباره برگردم و بخوام کار رو تموم کنم، همون‌طور که بعضیا دوست دارن، خیلی راحت می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهم ایران رو نابود کنم.
ساختن یه پل حدود 10 سال طول می‌کشه. پل‌ها سخت‌ترین زیرساخت برای بازسازین و بعد از اون هم نیروگاه‌ها قرار دارن.
من می‌تونم ظرف یک روز همه نیروگاه‌های برق ایران رو از بین ببرم. اون وقت حدود 91 میلیون نفر بدون برق و بدون پل می‌مونن. برای همین این یه تصمیم خیلی حساسه.
اونا می‌دونن اگه به توافق نرسن، من این کار رو انجام میدم .
پل‌های اصلی واقعاً از بین میرن؛ فکر می‌کنم تو کمتر از دو ساعت بیشتر پل‌های مهم نابود میشن و نیروگاه‌ها هم ظرف یک روز.
ولی اگه بشه از انجام این کار جلوگیری کرد، ترجیح میدم این اتفاق نیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9Hjpm_dQAuIGIKv3U84alHm8pizRrw9LoTHYz1K8ilUUfhxdyIz4C55ncswTxeK33uxMQ_PF6FCwfbujX7rkCGQkYocfMmORHUt64pHrrt8qUN8NUaL4ImjtpFVwLvhw5TM8mpcGTJci9YjTrRPd4s-dXYO5Ll-jZ9yfTM_HMYI8wUfQM7AtzVNmQFwQJNB0BwPYnYYnrNVhTX4w00OGRPNV5EsheG4d-YxUx5HQ9ZBikExUfsODpYlRv7GLyAvEvYANYByMhIk-OrE6hz6vSMuccNWVwY4lTqCfv1Q3c-w0qcKJexKebYH76zUANWkoxGWdfIfNrAy4fewNyEXrZ1x-34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9Hjpm_dQAuIGIKv3U84alHm8pizRrw9LoTHYz1K8ilUUfhxdyIz4C55ncswTxeK33uxMQ_PF6FCwfbujX7rkCGQkYocfMmORHUt64pHrrt8qUN8NUaL4ImjtpFVwLvhw5TM8mpcGTJci9YjTrRPd4s-dXYO5Ll-jZ9yfTM_HMYI8wUfQM7AtzVNmQFwQJNB0BwPYnYYnrNVhTX4w00OGRPNV5EsheG4d-YxUx5HQ9ZBikExUfsODpYlRv7GLyAvEvYANYByMhIk-OrE6hz6vSMuccNWVwY4lTqCfv1Q3c-w0qcKJexKebYH76zUANWkoxGWdfIfNrAy4fewNyEXrZ1x-34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=oua1RrN1byDFTVKjdmPp4GXYKBKVhgIVxsuombfg7_SjBIiF2FMwpqUvRNKnQG_MlYle-MVc1FWBmpvhtsOz8mxIy_N-Fai_KMYK0nqjRjA5lXL1zPmpQIvxLIDMfHdd6VDgzbjuxLgxrWghvy4NpW0Aq8IAGZtd1WHWg_UJJTysI2-lEEShTuA2yFhe_Pm5OUV6ZVQ9tqY2jJWafB5FMhlANgr0HYeEhhOvNI-A_sjsRz2xQLzMFZ3E0holM38cv6xcdoyA5714hHSS8-5iAynWF-00LFjq5Qa6bnnho-bzwV3vJfHQM5sM0RJNkPQDirfj7MeIR2_a0s_hwsBpE5gFaVBFt9X3jijDkLn_fKgTwLgXFbSKE4t62Dpbi-pZtoj39rMvAObO_ntbKgn-gN_FNYRNc1DS-cuLp0sTW_ivKs0mL8GXnygLLX1uTH5C7zBwpOBuxUGmqq1j5uquXvHGo93dTJLMqGi8-U1_eP7H-rARNu25qckOy0Dm8VsfojlTN0ND_r-NCWv5eiwA4-gj7iB1W5MmKHuy6V7e5vxoLb9VshrVnPqksuuSfDQe3Haftl1Y-PKNYu3e3p8cbFUxuOJtWc9Y52Bh1G8614ZnWDRF8k7RoE5IeHBejU7x3mWQeEXMJMSB_fEE-JMCGsfxCGp3FAKQy2B7sJQw0uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=oua1RrN1byDFTVKjdmPp4GXYKBKVhgIVxsuombfg7_SjBIiF2FMwpqUvRNKnQG_MlYle-MVc1FWBmpvhtsOz8mxIy_N-Fai_KMYK0nqjRjA5lXL1zPmpQIvxLIDMfHdd6VDgzbjuxLgxrWghvy4NpW0Aq8IAGZtd1WHWg_UJJTysI2-lEEShTuA2yFhe_Pm5OUV6ZVQ9tqY2jJWafB5FMhlANgr0HYeEhhOvNI-A_sjsRz2xQLzMFZ3E0holM38cv6xcdoyA5714hHSS8-5iAynWF-00LFjq5Qa6bnnho-bzwV3vJfHQM5sM0RJNkPQDirfj7MeIR2_a0s_hwsBpE5gFaVBFt9X3jijDkLn_fKgTwLgXFbSKE4t62Dpbi-pZtoj39rMvAObO_ntbKgn-gN_FNYRNc1DS-cuLp0sTW_ivKs0mL8GXnygLLX1uTH5C7zBwpOBuxUGmqq1j5uquXvHGo93dTJLMqGi8-U1_eP7H-rARNu25qckOy0Dm8VsfojlTN0ND_r-NCWv5eiwA4-gj7iB1W5MmKHuy6V7e5vxoLb9VshrVnPqksuuSfDQe3Haftl1Y-PKNYu3e3p8cbFUxuOJtWc9Y52Bh1G8614ZnWDRF8k7RoE5IeHBejU7x3mWQeEXMJMSB_fEE-JMCGsfxCGp3FAKQy2B7sJQw0uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=YMX6KfPiU5mv5E9PlHVkanqDZKwFF2SiRw6bLbwbUI3fqHS03fFIdZk8vQO5lbV7Y9qx66HFv3_Dgh8qz1byguOQd71bzuPQx8JPt3D5BaI16-TRmXYDxwNk-_r8aygoGpiiq7koZVNtD6NKOEJT6WuBBn1DQEdLJVhA_Old09X-eApo4HJczP9uQ2fmXUKFvijRtn_j7K-DIzo1oOhleWk6o5I0dZHYQbuSuNS3Emy9FCwkbJBelz410cxwdfGBdEPtKriA8OelfwSvEwx6UiRBJcgvWmiZtWRnSYueaNdL6h4bIQ5aWti1OCFVQ9w3CYQAaSksFAA6wQ_AFTzUtpxI1qd_EdaL8oIgUL2BOv5Dbxo2h6doJ7L40uVNF9sn4rpWjaiRzn2oHNhlkqigHqPvXYlMAC3N5u2fKTR6gDBMEk9-3jbYM2LCy7tkiR5Z2QKA1DQrleofZignX491HrpOupELAJ27JydMgNZszTNaclYHVSLr3tP2BHU7OjK5u5gzT_eikCbVCxmhOHYG5YAcTEooy9INsw7HaaNH0SNFbc6tEg8utg0NQHUwpw3RgCFC9Bpi6UE76jN75ZA1_tfUaGk4oXPmZNqCIb4BTxSajYhAn__0A6XIzHKzkfaJgj6fpo7d1Jc6aMcytvZmClbndAVozlXuBHSDsst5BMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=YMX6KfPiU5mv5E9PlHVkanqDZKwFF2SiRw6bLbwbUI3fqHS03fFIdZk8vQO5lbV7Y9qx66HFv3_Dgh8qz1byguOQd71bzuPQx8JPt3D5BaI16-TRmXYDxwNk-_r8aygoGpiiq7koZVNtD6NKOEJT6WuBBn1DQEdLJVhA_Old09X-eApo4HJczP9uQ2fmXUKFvijRtn_j7K-DIzo1oOhleWk6o5I0dZHYQbuSuNS3Emy9FCwkbJBelz410cxwdfGBdEPtKriA8OelfwSvEwx6UiRBJcgvWmiZtWRnSYueaNdL6h4bIQ5aWti1OCFVQ9w3CYQAaSksFAA6wQ_AFTzUtpxI1qd_EdaL8oIgUL2BOv5Dbxo2h6doJ7L40uVNF9sn4rpWjaiRzn2oHNhlkqigHqPvXYlMAC3N5u2fKTR6gDBMEk9-3jbYM2LCy7tkiR5Z2QKA1DQrleofZignX491HrpOupELAJ27JydMgNZszTNaclYHVSLr3tP2BHU7OjK5u5gzT_eikCbVCxmhOHYG5YAcTEooy9INsw7HaaNH0SNFbc6tEg8utg0NQHUwpw3RgCFC9Bpi6UE76jN75ZA1_tfUaGk4oXPmZNqCIb4BTxSajYhAn__0A6XIzHKzkfaJgj6fpo7d1Jc6aMcytvZmClbndAVozlXuBHSDsst5BMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Od23-sDblC4A7zwvR60kevOC9UnQLbSKaxmj2ypKijvLwTxajjyke8IVQDn8Z4tIE84qRCiNVeMPUbT6WLtczpP1KyAuf0yKqsQbAXymrJCHbN6R0FFOZKL4qaFwOJq1T-Nm01fAZdkQVX9cICCgfNWS7-91R-OfMRsFUY4VU1nXO2Fajqo_fvw_Lht8YcfXk6qQV4u0CVNfUBIulS5VDGOAgN-Mq97jBehj60ze0oRFw53WGrSJcimJss_6whh6rfHGbT__2KVwmI0PYOGXnFbLEoS0LQPyPjtS5U3nFDdaI9mt7pUxhlN0tBEcqCiYZw18JDkpc0aX4Yp-FyjxZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sl3UNVBl87QcY_6RYd7JP1BQDL9rdtwqoWlMvdO-vV_K4bshUEX0R4U-CIRa9742cSV5330kRQuD1bCDK6bRi-WOmqUONmDTaBGNFCDOgFTZF3rFQt105B0F3doUAtyhQg_79cERgZpEdRNYgUECYuziXhS0YCzy2puE4t9CBQL11s9Lst-3we-SNSvdG_swHRVtSysc2fDkd_vzzeWKZ05GM1lriTyC41H7heyEqY0wjip2eYOt9DsdUoTYqMUzbKinQv84mns4T6n1LyFdLsD1QJB0hqXs1YgpVBCk9F-R5dYbB9pacTecrmYe6qqqNEssqFQbaL0LsoJdTfJMog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=S7CxM_9Kptpp63mob7RbNfDOSHeqSuJI0Z7hwgW5Bzs83OQeCi4Bjbgmj5VxjKLzstvT9c1pJtdm9Js4QILj0l75bpFJdfg7Wzl56IQIaCDhwero7466WO9CxHWkwAVBjOxg2h3TM9IGmDnl6g_tlzSGtc9qqXaEoTmHjF1FURYLOB3BpmT0wrIphm41L5W_ErRu_-oF1FfAQDXm4lPkC4-BLP25RLJN-MKvk3XvwewHr3o-6G4IFnXXh2is0cCuCXRzJmMHyao89BWwxhaq2v1FqMDV07AHu_Y7rhov_BEfT2qo-qB654p_6IfgdLlB_FZKW_4jsEnx-s9wNIH_kzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=S7CxM_9Kptpp63mob7RbNfDOSHeqSuJI0Z7hwgW5Bzs83OQeCi4Bjbgmj5VxjKLzstvT9c1pJtdm9Js4QILj0l75bpFJdfg7Wzl56IQIaCDhwero7466WO9CxHWkwAVBjOxg2h3TM9IGmDnl6g_tlzSGtc9qqXaEoTmHjF1FURYLOB3BpmT0wrIphm41L5W_ErRu_-oF1FfAQDXm4lPkC4-BLP25RLJN-MKvk3XvwewHr3o-6G4IFnXXh2is0cCuCXRzJmMHyao89BWwxhaq2v1FqMDV07AHu_Y7rhov_BEfT2qo-qB654p_6IfgdLlB_FZKW_4jsEnx-s9wNIH_kzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=VFEvV-ejboDLPEY7btgygANr3p0rDdMwtFK8SvZ4KLHhOZSgWMNqkXDtyRkqYeddZqoB0NriUOXbxe4eJvpWH3aWVhAZr-fIviY7XZibA0ffNW_BZw4wTTrcyl1geIU9VjlvrDS1SCN6b-p15g0o76a2-XWo3QxBxftUNTbeAqICDrN3V7r0XpCT5LuQvjPT8rEqi5A8XbX15E70d2hd8UdcSlDitpGufqVzzGMZCqamV698au7-2pVaHXHv7bLdGAb-KDGkEVdrsQxxBbYfIbwv3MY2hSRJFZJYpIS6iGT8nMlVPDBVZCbJ57ua-23yaqbgVs27aKV7UF0aWxyxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=VFEvV-ejboDLPEY7btgygANr3p0rDdMwtFK8SvZ4KLHhOZSgWMNqkXDtyRkqYeddZqoB0NriUOXbxe4eJvpWH3aWVhAZr-fIviY7XZibA0ffNW_BZw4wTTrcyl1geIU9VjlvrDS1SCN6b-p15g0o76a2-XWo3QxBxftUNTbeAqICDrN3V7r0XpCT5LuQvjPT8rEqi5A8XbX15E70d2hd8UdcSlDitpGufqVzzGMZCqamV698au7-2pVaHXHv7bLdGAb-KDGkEVdrsQxxBbYfIbwv3MY2hSRJFZJYpIS6iGT8nMlVPDBVZCbJ57ua-23yaqbgVs27aKV7UF0aWxyxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=MaVYOaNu-GuzOAsJKvrNaui3b4TxnHWRbj27GW3WQGYVqIRTt5fR5DZavZ4P2apcN29r9nR-kmX6KUTOBYBY636JvHUMJfCp6vN-K2dK5ZyBR_itGW4QAbH9XqPDJauus_awgI4BQjym6p5lB-n4tQQng20WjmDOGI_LyAiY8hR7qHVBbMZy5E41PwgHqsGdhdR1Ij3hi3IeSYw_bd6OTnAQMYfcwrrasaURMaXVT8Y64WH-BY5VPXwDVrQpKWIqucNKMj7cjYKTO_6cBA0gf-SZtoSj3vIdKTpczyc18cO3z-bXw12_PmZFNhvORLeKHmh5tRVMGGp2mDLdXDM9cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=MaVYOaNu-GuzOAsJKvrNaui3b4TxnHWRbj27GW3WQGYVqIRTt5fR5DZavZ4P2apcN29r9nR-kmX6KUTOBYBY636JvHUMJfCp6vN-K2dK5ZyBR_itGW4QAbH9XqPDJauus_awgI4BQjym6p5lB-n4tQQng20WjmDOGI_LyAiY8hR7qHVBbMZy5E41PwgHqsGdhdR1Ij3hi3IeSYw_bd6OTnAQMYfcwrrasaURMaXVT8Y64WH-BY5VPXwDVrQpKWIqucNKMj7cjYKTO_6cBA0gf-SZtoSj3vIdKTpczyc18cO3z-bXw12_PmZFNhvORLeKHmh5tRVMGGp2mDLdXDM9cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=gCDroZqcGSB810MRRSFXRp7rgGYHIzt6xMdNCU6RfwN6qZTiBPfJJJAJ142HemLe1rtr7nDKey6Zpa6w3Ck9w9b34kTiWtQh2ie4s7fNXtOdZcPbAr9aCAuvstlCGyn2-Adc9KWO_635M9j58dnvST-3LBdBm-gjJo7ugXm_3zruN6N--hsnitZ0Zvr4ywNoSDyEQ_JFDaskGKXvL7U5U2fhbnXMartCI9-LHvnT_skeDLNn1S0K_z_QSC9qhrGIoAmM65LAN9Ge293KTX8vQ5ClokWGmNgGA0FXclh2IsL7Kl4SLl-XxsSrXM18sdgiE54Ypycb6-PDXhFoSvIroA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=gCDroZqcGSB810MRRSFXRp7rgGYHIzt6xMdNCU6RfwN6qZTiBPfJJJAJ142HemLe1rtr7nDKey6Zpa6w3Ck9w9b34kTiWtQh2ie4s7fNXtOdZcPbAr9aCAuvstlCGyn2-Adc9KWO_635M9j58dnvST-3LBdBm-gjJo7ugXm_3zruN6N--hsnitZ0Zvr4ywNoSDyEQ_JFDaskGKXvL7U5U2fhbnXMartCI9-LHvnT_skeDLNn1S0K_z_QSC9qhrGIoAmM65LAN9Ge293KTX8vQ5ClokWGmNgGA0FXclh2IsL7Kl4SLl-XxsSrXM18sdgiE54Ypycb6-PDXhFoSvIroA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=upBuZ6YHL_Eyl-5SuOlaWax0Cz_v2sIg1_Ax0JF-NcGRzb4rfHcVTGRLU5ZneeKKDiGdNfvVRkAUT0ubJC7kAJL20FXBG-g5gLzsMpaTrV6ggwFoL_kq-q22dJjMqeYnWOoRTAu2-6aO8_DWelksBmfTQMMisGptEXAXJuQHCbtOp8WIbZzcQQH4t4Olbt077UfEMLbyJ37BWydnp-9zJRDv3DYaU-qr4LRaLBcjTP9z2U1Ri9_Q9aZqi95Qg19K4kVoUeW7ThbYgxeGe9MFLTFl6OPimEn_Mf-YN4kjmvVMMRs0R-pxIGu6wMyvBQ25jQZVgyKvDkvNmJm5HsFgQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=upBuZ6YHL_Eyl-5SuOlaWax0Cz_v2sIg1_Ax0JF-NcGRzb4rfHcVTGRLU5ZneeKKDiGdNfvVRkAUT0ubJC7kAJL20FXBG-g5gLzsMpaTrV6ggwFoL_kq-q22dJjMqeYnWOoRTAu2-6aO8_DWelksBmfTQMMisGptEXAXJuQHCbtOp8WIbZzcQQH4t4Olbt077UfEMLbyJ37BWydnp-9zJRDv3DYaU-qr4LRaLBcjTP9z2U1Ri9_Q9aZqi95Qg19K4kVoUeW7ThbYgxeGe9MFLTFl6OPimEn_Mf-YN4kjmvVMMRs0R-pxIGu6wMyvBQ25jQZVgyKvDkvNmJm5HsFgQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=tdVilTNuEn0KFKCtIsJ8ZIuxavfSOxYvrFdn_XJr-4eJgMkCA2bn2jb8QhYNL51mL-f8Te_34dKGavsm04VK9aayFiGN5WXGV26L4zoX-I1w1v6pLVozLjLN6oISopBb3CceEXl3QUW87sd2cGV1ZsnfABxL9dumrLWNONxBZHARSfmiE5v5aehR-aNTwAOkAX1XtJwh7c7XAH266pvWl4TEdqYOo0lA1PPHHS9mcSWp6I_PG9NwL-aCgqcraPo2k8dvdl4PEU1p0UUN63dYgancxibBNtYKbSPjxbjzwnbalxo9r6QsHjUUt-leWPVXBhJ_-p0iZxnCA-fZ_30OEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=tdVilTNuEn0KFKCtIsJ8ZIuxavfSOxYvrFdn_XJr-4eJgMkCA2bn2jb8QhYNL51mL-f8Te_34dKGavsm04VK9aayFiGN5WXGV26L4zoX-I1w1v6pLVozLjLN6oISopBb3CceEXl3QUW87sd2cGV1ZsnfABxL9dumrLWNONxBZHARSfmiE5v5aehR-aNTwAOkAX1XtJwh7c7XAH266pvWl4TEdqYOo0lA1PPHHS9mcSWp6I_PG9NwL-aCgqcraPo2k8dvdl4PEU1p0UUN63dYgancxibBNtYKbSPjxbjzwnbalxo9r6QsHjUUt-leWPVXBhJ_-p0iZxnCA-fZ_30OEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FyzPOCtneVleB8FjYH2WYpMAz1JUXegVgo543z4DYQpf6ynE-4TGjelWkdw-rMBhUJquNxfZ-706UqVDNXJBFR2Ki_elC1BKnf7iV4Er7hI6WQb8zZowl1UZEPGmFjnbLomg0hfoLRNd4scUCOXl77fiQVfiy6fqB61eEyZ1Kh5vL0jsGS9Sg0gzbEgxJKJwV80YLWPumUGMwriADOWWEwwy1rVh3FGjKqcpO3hXnMXQQNrI-StVOQhIFpuXjaMLpGvCRI8Hz5rfUGAhU9i5LsjLjdx7_esUsGJrU81aIcRyh9H7cRmKhXeHDEaZ67POsXoP-gIW0APc0X7LLx5bCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtlbaNOGGsL6N_mt6zMIQ-zVhNdLX8uYucY7_MTjolyzy1c-ybgkkqUzK7S7x-Mr6lCW-gy2LKQvn2WpZinxO16iTXFH2UhzgijoQEXNPyE4c1rcT0PtHofnJyUaft426Q_NtCcjOXAxqbCJ8OmleZLqA8WSVFnXmKBl9QtgrCprhUrP4BhabZJ0bROP2FsmOlN41cpDmLtrttUul7cgaUV0b0Jk1WCU7pzlQw5wccRz_AbJxAd_7mXwyCel3o4YyzncNvVP1xlArdvrw0lXcm_1R7fbhMLzbUhhWb58-S3haCYMSPILJDdNCFukt-7Kh50IrMaaatkbdpRcpCsZbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=jYHSY1Si6rQB-L4vcJIc_M9dVJCkDwA8kMDnudkIQtRgMfmLEuOf0pHFk393tSl2p6yXH7Rn0DmAJI1siUYluy1fV5FjDX7WuGA98zn9gz3TCSgWZDm9dliAvy5UHyfoa2-FbnpscEh0S9HgH4vVVAqVTUnZkXwn0pv2jv5OKhXzQkZadaT0c_yCiEqFjj9nbgldQmBAAdevvv6UNju7AZlnVr3jnpKHDGFUbPlsahP-o8uA5kg-Y2J6pUrgLaDaxprWb_llDorOYXcKqT1rGoFQLMdkbAWdso9i3YvgMNZTqFLBI3285gK2Yph7iYYnjSSy1MoMEDDeNq11goJFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=jYHSY1Si6rQB-L4vcJIc_M9dVJCkDwA8kMDnudkIQtRgMfmLEuOf0pHFk393tSl2p6yXH7Rn0DmAJI1siUYluy1fV5FjDX7WuGA98zn9gz3TCSgWZDm9dliAvy5UHyfoa2-FbnpscEh0S9HgH4vVVAqVTUnZkXwn0pv2jv5OKhXzQkZadaT0c_yCiEqFjj9nbgldQmBAAdevvv6UNju7AZlnVr3jnpKHDGFUbPlsahP-o8uA5kg-Y2J6pUrgLaDaxprWb_llDorOYXcKqT1rGoFQLMdkbAWdso9i3YvgMNZTqFLBI3285gK2Yph7iYYnjSSy1MoMEDDeNq11goJFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=RjK1VIkM_vl7Oyk7-0-RM7FqFLgLhnBYz-IVJcpXA5yOVgtAd13Dues_Yg7r9O_N6od-bGjG0wmJhRn6cz839OyueNce9o9EiTh6S_LDZWAz9uV1jLoY6gk98aANHoBmf0RtP45w0HDpPAaJtR9n3pdqS4ZiTr-vQ-e0Mqf6yp3IStmV72H_fneNfLEsh2chKRs8IqoHiPSXFDJ8Vz0C-fhAxFIvwcW7K5got9jxGWet_A0ubmT58EK-270nk_OX-AT6MVdu6i19CQeDvKf5yfW_KsN7Fyiah0-x1IJfr1B4TKy8XuU8JduQ5SOjBTHTs1N_3fgqrNAxqFEFNUuicpKVEG90UpMJnuCv8cPJ3W7wbQTQdvBxyOBW71O2plteZVsDpG9sAYP5WBp9I1lrPcvIPpIRn73oMJ74wJ9YDZt3RyKREqGPeM6lwReID9xgKDShmnN5_W3mvM-KmF567HIqrop2eB4tMIWGyFcZW4z2X0zA0ng7HgM6NjqZ2jJKCMqOEsyoqUjCRD_nqrchXfkcGZs6Bt0ajHQYFiKBa5RN5Qd7EYxXdLIWjNhdDrCAouOrCgf5hScO3gv6Ht9Yi4ReBntXAFdyHXb1ovCD-5vKvBN_lmyvG-bzemEBLRcas7TXcd0Iq2MW56bS7kMuXeoNuUS6SneMSZCG1ew-P-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=RjK1VIkM_vl7Oyk7-0-RM7FqFLgLhnBYz-IVJcpXA5yOVgtAd13Dues_Yg7r9O_N6od-bGjG0wmJhRn6cz839OyueNce9o9EiTh6S_LDZWAz9uV1jLoY6gk98aANHoBmf0RtP45w0HDpPAaJtR9n3pdqS4ZiTr-vQ-e0Mqf6yp3IStmV72H_fneNfLEsh2chKRs8IqoHiPSXFDJ8Vz0C-fhAxFIvwcW7K5got9jxGWet_A0ubmT58EK-270nk_OX-AT6MVdu6i19CQeDvKf5yfW_KsN7Fyiah0-x1IJfr1B4TKy8XuU8JduQ5SOjBTHTs1N_3fgqrNAxqFEFNUuicpKVEG90UpMJnuCv8cPJ3W7wbQTQdvBxyOBW71O2plteZVsDpG9sAYP5WBp9I1lrPcvIPpIRn73oMJ74wJ9YDZt3RyKREqGPeM6lwReID9xgKDShmnN5_W3mvM-KmF567HIqrop2eB4tMIWGyFcZW4z2X0zA0ng7HgM6NjqZ2jJKCMqOEsyoqUjCRD_nqrchXfkcGZs6Bt0ajHQYFiKBa5RN5Qd7EYxXdLIWjNhdDrCAouOrCgf5hScO3gv6Ht9Yi4ReBntXAFdyHXb1ovCD-5vKvBN_lmyvG-bzemEBLRcas7TXcd0Iq2MW56bS7kMuXeoNuUS6SneMSZCG1ew-P-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=VmKpxfS-T5govsCc0RlZTpWAg7deFFH6X2vQqn1Z-YURCgxg33G0kZePssmbqDY3m7a049i8gfmvErqxgZWbFIt_35P9hZ8H6wgTuXwf6Jc-WFOsN0LciUHSAVq6vN-Ah6G3C6Q9c3rQm_hWd-JE0v-E0uN3hxb6bOFrQqwZ7sM7f39XbTX8BxAqAQKtteS-rUim7ZAGnAA1OzSZDzcPkLLzzLqq50ax4R4JSXuH0_caAhQAunKSJD8x8nSsZoVt-foY3j5oMHAwkHvAvZKAka9jZlaELWh7YILTNPvRqOvyRZWZdNaCWMDkklDscxuwSmGlU_YsdrfM8iKqdpFs4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=VmKpxfS-T5govsCc0RlZTpWAg7deFFH6X2vQqn1Z-YURCgxg33G0kZePssmbqDY3m7a049i8gfmvErqxgZWbFIt_35P9hZ8H6wgTuXwf6Jc-WFOsN0LciUHSAVq6vN-Ah6G3C6Q9c3rQm_hWd-JE0v-E0uN3hxb6bOFrQqwZ7sM7f39XbTX8BxAqAQKtteS-rUim7ZAGnAA1OzSZDzcPkLLzzLqq50ax4R4JSXuH0_caAhQAunKSJD8x8nSsZoVt-foY3j5oMHAwkHvAvZKAka9jZlaELWh7YILTNPvRqOvyRZWZdNaCWMDkklDscxuwSmGlU_YsdrfM8iKqdpFs4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sirDgZPs0QsWmoySjlZhCcLYhcFHWKl7V0fuZw_FqVCj9EY1Il5fAZywxw0q3yt4Cp9v564QVLNddN_GkJ5IAKGV5m498cQW5rHMqp2PWd3xG2XCC7pEaMQBiaGNjcXAIuYuPDBtB9cdX-9iqDavuY37IA8s6fBfl1lB9isx8yj9yHl_n2IlxchNfGVZj5hIFP2KIdcKNBsIbvnK0dMyubS2_MkcX9NeOQ0qyH0QXA4i7bz-Vu5YSuhrgjq1OGWx-HubPRKaf9cX1mkuUGDfnXgDX6hX35q0Tir-AWnB9m_hXGOKjYo9wQgpIjLzBYN-NnGfUO6JPyD_PsSChZfAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=YjmCGlz4tAmZVK6-kAzmXCAYJqFcj6p0cATT9H-lbWdvCkO9GKqg90J6OE2NfwSG8wC4cHSgG2Tv6mjuzC8_LwEBdN2UZF-Dc2abnvLpCuZmqoeC4mWWsrfZjB8oEao4x5Y0nGrGGHTeV7nzFm8p7ysHIcK4xCrOgAoF1-Zy8sK2-LGmLvtTc984HgxVzsz93B_1GIncKWFKZbHXu3XOX0HJj74Z9sarbKf8WLO-iDFJvJRVgljmPANhj-y1jGegoEuGT5bFl0ZJ6CqkofZdAqgnMzPSP8MFmuVY8KQAHQcSp9-4jH1p0smrdejPrPUU_S0NJXHGSYN3OWbwoQ3vWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=YjmCGlz4tAmZVK6-kAzmXCAYJqFcj6p0cATT9H-lbWdvCkO9GKqg90J6OE2NfwSG8wC4cHSgG2Tv6mjuzC8_LwEBdN2UZF-Dc2abnvLpCuZmqoeC4mWWsrfZjB8oEao4x5Y0nGrGGHTeV7nzFm8p7ysHIcK4xCrOgAoF1-Zy8sK2-LGmLvtTc984HgxVzsz93B_1GIncKWFKZbHXu3XOX0HJj74Z9sarbKf8WLO-iDFJvJRVgljmPANhj-y1jGegoEuGT5bFl0ZJ6CqkofZdAqgnMzPSP8MFmuVY8KQAHQcSp9-4jH1p0smrdejPrPUU_S0NJXHGSYN3OWbwoQ3vWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCvgy-JMqcqQGgYBeJ_TPCt5WodNB5aMmHl-4TeBQhPTP_x1cr4mFC9bszXJ63b8uqajJD7WDhRcV7sELGuRquz5xd53kikn_QzukSAarUpK7gJY0HJ3PBB09JpR0RdgdSJT6Kt8dPYiRW4dyLrhkXwiIUouc2NmJLgleiTg37KJCfYBcFC-g3asi0XKg2T1NmFXHMVeZDWSD2StBlMqtM6C0dDEXdzqbGHy3KEPEDhxkxtRbG5Nml14j8LG3Pi9TJKNqSaGJ3-nz5A9PeAycXIlVTm5RgAym9pW_NPj7pfT8da952JYIqZaK9LtKWd5LPjtUfStDz9HSrmuDBHKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/deMi0lNgzPYdFZT_ygn_cADgF0SYJg9bWhDWVRZuaiM2Fv2uqSbSepHCnfdlpAtgSIePr5E5H7ucqgOTfAl5bLX4UcKHIvYKGUOGaNIncjkazM96u6CT_NId1czVCxOYZPPLFx9TeEAhFopZ61RSzAsBwFsZDDDR3qF2XKi6yi6EN2f4RTclToQzm2kSmf46fUy5G8yj3VtZKGUckMEblzcLroOPvt035W_xaYFPFNszVkWajNQ0cX2xlxggyhrjtnPHwFx1S-2t9-yR8rODEt9DHryLkjuLzIYUgg5j9Ci9koVzCzSuzxZ7knBKvHjXTDScMDgnfcygO0KLOztgKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=iIYprNaXkXo5asPRCR1v7C_DusDhxBtUGVqV1TIDv50AIX5VZ2kfoS7KjDS5nf_RZvYEZy5z9U4mZxvgZl1kOswjUqPTsH1ybSbhWKqYR67NfMklCq0ZC70HmrBw8D6dkWC28gV63hNaj4s2GsuiVTOJByzAIMwCy8z1ym6EpVncRrQqTdevzgs77OGSaOlPB7rNf9Ml7OjKIcw03kzWNNi0tn2MByc5_7_f_4tmbBy9dyCFafghiE-cxK3FKG-M-oJLiHt8f7oIgV0_8c578u8_wdFfLkNw25tYmPO4f90RFgnw97JhOzEtg483gtEq2gWcAFMWldbaAvGA6oEkjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=iIYprNaXkXo5asPRCR1v7C_DusDhxBtUGVqV1TIDv50AIX5VZ2kfoS7KjDS5nf_RZvYEZy5z9U4mZxvgZl1kOswjUqPTsH1ybSbhWKqYR67NfMklCq0ZC70HmrBw8D6dkWC28gV63hNaj4s2GsuiVTOJByzAIMwCy8z1ym6EpVncRrQqTdevzgs77OGSaOlPB7rNf9Ml7OjKIcw03kzWNNi0tn2MByc5_7_f_4tmbBy9dyCFafghiE-cxK3FKG-M-oJLiHt8f7oIgV0_8c578u8_wdFfLkNw25tYmPO4f90RFgnw97JhOzEtg483gtEq2gWcAFMWldbaAvGA6oEkjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=mJwooPfj04p6ap0ZIL3B8WGhsZj58aSTo9GWCVH23vVSVPsV2_ezmaDsgycG5YD8WPPg88ogNObDcL88g4NmBPSNpvBRcVAyqatvf0-PQqApBl0kJMaDC8fXDW-4i39rXYjY3EkpUGISoJesgHga-a644z8Pqia5AJHWFdy8OYcBTj1mktWSPDcpg0m1FpIjL3HK9OUHZNE_cruddLgPv8sAmD0r7ZGbFaIZmywi3UmwKDZvw9La6O8-VY9CgtqzzuyVXwaZ2dLW4Gs_naSvZkMdyA66VS_4IIuY-SuiXbRj9bXOqfWSK0ctDjYsm-JxoAwsbiZ0xmzbX37EmsL-tA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=mJwooPfj04p6ap0ZIL3B8WGhsZj58aSTo9GWCVH23vVSVPsV2_ezmaDsgycG5YD8WPPg88ogNObDcL88g4NmBPSNpvBRcVAyqatvf0-PQqApBl0kJMaDC8fXDW-4i39rXYjY3EkpUGISoJesgHga-a644z8Pqia5AJHWFdy8OYcBTj1mktWSPDcpg0m1FpIjL3HK9OUHZNE_cruddLgPv8sAmD0r7ZGbFaIZmywi3UmwKDZvw9La6O8-VY9CgtqzzuyVXwaZ2dLW4Gs_naSvZkMdyA66VS_4IIuY-SuiXbRj9bXOqfWSK0ctDjYsm-JxoAwsbiZ0xmzbX37EmsL-tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2wNTc9-3jNcI9KodSjb_G_dD84H7Dkb2hSK5Ebi_V0fSosR181gHxMhtYxiTCO4G8_UTR6InuLRDx1Sc0aX2SUVNL3axozAMgrR4H-DU25uD4oRIWgQcvCNheH1kGf71tIpj3t9wbyUp50XqSx-vxdKA50LQd4aDGDh883J9SBH9zr-FQiFIEFgiOnh8waIYfCKAF63xuVTsL5qhSfrZNhL_nDwv6DSWM5vNxfznSSpOLEw_52EcS2bBjQlXyZ5IWVzK6gOWHdYqcLovnPqGC1xQ0Zk1JWkEjcK2Mvv3iD1NaiAfgaIi9Vj3Q6cp2uCgeHT_Q5Bi3gXqh6H-w1Frw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WfX43kq2sZyd8I9vu99yunm09GjZMpXb0RpxTWY0ZdnF426Clur9xgt5rSKsd9fVFjB3Wa8FkbCaApFGfzIB9eLB_eguh13uJ1ZBRFn4EOBRWE_qjbKQZ08Z4mdbViPWI0d7gAST4nX0MgdPaMrje0xuD-jmPD0FUhEAFugYDd-pzygnZkK0klx3aX3qb4fxKl43XaRG8d9vMc0NCx0dSjudHlmlfSiEfovtNGd0fMLaqjOSkrI13TUPv8S748mjQuEI946Fu2cEfGvnME_zZ2IHGZycFuFuWs_DTnhLYH6AgSIDZhxYCBe1r8l3A_JFulIppZbMObxSF7y70Pnd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCU5qexRCbk3I4KlNJLFhjMT5lxWLMALthW3r752FlQMLF6V672efzW88sQaC_f4D7fKSYEmuNnf7eMGROcMsXyUdLjWRk1BI1DT-vmUv8xMinekrF5U8SAKxtdvDlMxWoc3UI4Tw1QL0sDBOGtDA_7aFnk-eZ2aJu_UM6PS1gLMy9MkIW1QmZIxfGa17cx89NKJwSc7LB1_35UoujdxvHv17v9GGtaypgEgndFEka83VPlFeo90XgFElZTu5dS8bq4bBdjOxI_OneRWnTFJwA8KrFm4sNv-skSPjv9Iuzzo6gXXY-ddW7w9LLiVBn41JdY4d4xmQHOm2BqabHdeGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=Xm2GB_o5SoPrDDJemjE02vTrprXBPPE8eOnylLqCu9zMeMixTkoF0eC22gW-ujUIJ2kN620ZwpECSrdW_R7oFBt5nSLPFHkqV_Q1AZQZ2Z8gYP-g73ltQ0DtyFsPIdRY4U96PWLku2wtiBZXdRJjQRl_ZQUKFvdqZN4gBEqxSMDWTkcSsdjBqnVEsugboP3e8MEYpXrSkH7pQn83d6U6MieVw5w0CXrSm7Nx5G2W46t1_fA7qYYYBci1gQVTMhdth3wMjqP7zJDXbtQmzj8PGaL2DyngryEcs5wv82KGWlq8OCcWfkKMbeFA0NZUjmUZzhoKDIVqVf-nyJtIEw6lcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=Xm2GB_o5SoPrDDJemjE02vTrprXBPPE8eOnylLqCu9zMeMixTkoF0eC22gW-ujUIJ2kN620ZwpECSrdW_R7oFBt5nSLPFHkqV_Q1AZQZ2Z8gYP-g73ltQ0DtyFsPIdRY4U96PWLku2wtiBZXdRJjQRl_ZQUKFvdqZN4gBEqxSMDWTkcSsdjBqnVEsugboP3e8MEYpXrSkH7pQn83d6U6MieVw5w0CXrSm7Nx5G2W46t1_fA7qYYYBci1gQVTMhdth3wMjqP7zJDXbtQmzj8PGaL2DyngryEcs5wv82KGWlq8OCcWfkKMbeFA0NZUjmUZzhoKDIVqVf-nyJtIEw6lcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=LEM7y7lddezamI0nEVA0i9P8Lbzbxgo_g4ohJL8wgHZoWWDTjyN7bfOrDWIBA2GD9uWhz8QTHMp2wchO9trAbHB0G2ior3BJw5mV-NoA96U3knrWe99uF-kjeyqNAPDziuo5BbfnRk7v51k98YlKJ79Z8KC_NaLer07BYI1-vd9e074Kp26vsT6SpFidqkldjDMl5NfYJeN_yjoYRItxDa0wcpzSdwShb_DRX-LDBsSYT5RHc7RK-RTvhZW_j8vHQk12JtBgGerpIpsotfZ3HrsB-YZRfv6mSW1ZPJ4FLs_rGt1RY0tw27lr7yvI02q6m12dVG446ZYfqtoz3CIrlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=LEM7y7lddezamI0nEVA0i9P8Lbzbxgo_g4ohJL8wgHZoWWDTjyN7bfOrDWIBA2GD9uWhz8QTHMp2wchO9trAbHB0G2ior3BJw5mV-NoA96U3knrWe99uF-kjeyqNAPDziuo5BbfnRk7v51k98YlKJ79Z8KC_NaLer07BYI1-vd9e074Kp26vsT6SpFidqkldjDMl5NfYJeN_yjoYRItxDa0wcpzSdwShb_DRX-LDBsSYT5RHc7RK-RTvhZW_j8vHQk12JtBgGerpIpsotfZ3HrsB-YZRfv6mSW1ZPJ4FLs_rGt1RY0tw27lr7yvI02q6m12dVG446ZYfqtoz3CIrlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=kam-3WPqImoR7SylOzfD5FOg-4untj2HkQTJPagl2_u2-cMzFq774UdArxxQe9KYUR8jDLevVwwbMnZ8cxy2fw_yAUGttL80HNpPZTJCOCkj-8EUdClDY74D0bfgV90FShqw1MLnnU8wwsSB8S3J8nTcgpKGG0oy2I4BGgbLKCKbVO0gOjW76nr50YLHCvR5V07RxmWbEcoFKMJXB3RufpMQeK1AQKRSMWPNPrrfFJCNq8b72cgO9Dx1AFz00USKJiA6i-MeypcC-8ys7PPeERH6Q5dWA8ZoF-I-ykJUUKRK5pqAuRMIpsD55RUoKWE4tr8znxnRJm1eb8feshR9Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=kam-3WPqImoR7SylOzfD5FOg-4untj2HkQTJPagl2_u2-cMzFq774UdArxxQe9KYUR8jDLevVwwbMnZ8cxy2fw_yAUGttL80HNpPZTJCOCkj-8EUdClDY74D0bfgV90FShqw1MLnnU8wwsSB8S3J8nTcgpKGG0oy2I4BGgbLKCKbVO0gOjW76nr50YLHCvR5V07RxmWbEcoFKMJXB3RufpMQeK1AQKRSMWPNPrrfFJCNq8b72cgO9Dx1AFz00USKJiA6i-MeypcC-8ys7PPeERH6Q5dWA8ZoF-I-ykJUUKRK5pqAuRMIpsD55RUoKWE4tr8znxnRJm1eb8feshR9Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_w4mwb4j6Mk_ydEglHMWn9Ietn5_eT-cLDnsGAdAqpF4M2Tg-joSlWY8eoAjW5qdxIMm8iynbjFX3dkIvjVf5YtnYIwNdcMOx4KU21kfFjRUG4VgodLPZkmu_jvjFuIpOGtNZ3tCW7GvORwOYqPueDbmCc4wJz0raTI6JQnRfG3BCi2hUPWZVMA6FA85YYmrz558KWdbhpsxoRrHR3LwBrrskDke550Ud3HVWmlkCW9FdA__AASamlHlosKxYrv-1wSrk-Hh8G13vm6cBKa5JVYi6diXUV37tip6VSWltWZ4H8qNQvqCaW3EqwopEpVsv3328spffB6OmVilS3qYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApSuuxqjMl0FEQIgvxjGdEz5gNBc2fzH4cvELoutFqScsvOiRwODBv9WmAq0bgr90fLVnnpH2I7DaNB9FWUsNlCvxmOWU1VWthFuzrzrb60b8B9S3MR_mKP3HoQ0NiyqKyGy_vUxPkmGi2o2Cfy3ua-ft0MnTEdJnXrt_Teh3o8RLTT2DoxgABL3ZxXw5qWGA1CjIUsB8zo3lFjBDH29wVnrniqc_Ov3DI1NIYH1VpOJTdQ3qagXELmaY588pNh-tjA9zUpUl439nqF-oWvwxVMPO6VB9xutzsp5qPg-6gZ525S2fT7aWhnwPcPbpXur3lfRDrzqPwH-OetOGUGtvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSHJYH5KGAUtFdbb1ZON_WK0qvxQ_EDMcBifpocOWWyl7bhlUj8Njk6DBqlzGONeFTttCNJ8-TLqEoo3OpwVHagfUiY1zjInGdDbg_DYBYsUFdZzCCtqEelHEbwUzpXlOMhC5oxmaV4ozvnoslfGn494w2WYH-xW6s3qODPv-owMevn7Wah_QN6U5GOtPRSxLWOfE7lRmf5Qfay94r5oah1Ro2FSMKxlpBJk6BgRYhHUw1VDHYOmok2RwR2kNKqFiKIEy2rnFvbYnU2OBURZ877rQLdz5i8smDSM_FS7kHo7yErJlUSNSBt6eB6W2RL7DPVi45nk0O3Cj6zU3MEN-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=RTVsTatb2Z4vN3p8Li3gr-vzWMJ-VFqN90rXapP0q9KMtGMFXcG4l91UAapAwpBBJvoc-ABh9m6C_H5HWpceG6qp_04SUI_ZxoMvNI__AIAqdBnxrLn3lSK27Ope6l3VSr8Hkw6I3IVEuGlJErQPL2FfBoOOF0ZQopADz893muiXYiYrcuLW4X2rdG3e5vqO8PItasXPns1B1q6TXNg6uCXOlq3FdBvQ0YJUtH12X6dDId2VnQnlr_iPggrUBqLIpzyRbslId6M5m4vJvuuzTAfk8Y8zjd2fU3OGy6tEZM9aZm5t5GqFSIz-mvK0v0SDgZJ-cGrFn8SsQWDX8Rq9cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=RTVsTatb2Z4vN3p8Li3gr-vzWMJ-VFqN90rXapP0q9KMtGMFXcG4l91UAapAwpBBJvoc-ABh9m6C_H5HWpceG6qp_04SUI_ZxoMvNI__AIAqdBnxrLn3lSK27Ope6l3VSr8Hkw6I3IVEuGlJErQPL2FfBoOOF0ZQopADz893muiXYiYrcuLW4X2rdG3e5vqO8PItasXPns1B1q6TXNg6uCXOlq3FdBvQ0YJUtH12X6dDId2VnQnlr_iPggrUBqLIpzyRbslId6M5m4vJvuuzTAfk8Y8zjd2fU3OGy6tEZM9aZm5t5GqFSIz-mvK0v0SDgZJ-cGrFn8SsQWDX8Rq9cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همان اتفاقی که در ونزوئلا رخ داد، در ایران هم در حال وقوع است.
مردم فقط آن را نمی‌بینند.
نمی‌توانی به آن‌ها رشوه بدهی؛ باید شکستشان بدهی. و ما داریم حسابی آن‌ها را درهم می‌کوبیم.
مذاکرات دوستانه‌ای در جریان است. ایران می‌گوید: «خواهش می‌کنم، خواهش می‌کنم، محاصره‌ای در کار نباشد.»
سوخت برای مدتی پایین آمد. بعد، آن‌ها درست رفتار نکردند و من مجبور شدم برگردم. حالا دوباره دارند درست رفتار می‌کنند.
هرگاه کسی جلو آمد و پرسید: «چرا داریم این کار را می‌کنیم؟» فقط بگویید: «چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست یابد.» خیلی ساده است. همین و بس؛ دیگر نیازی نیست چیزی بگویید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69078" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0LKJzOM91sF19Kn8qOqITGfKK3kzDU8WVB4CiLls7UsX3WuELN01_VVqQVXvnOLfLPtfhnJM4pI7G8HgC9hR7M4lTKc-3K-0rdnhdSNrXW2Gf63DPlBSNJLDxphTM4thZdQxSWUMxEakyCGM3U6pnNUK8Fl_cHAlIjDEDk_b1VifbbHScJSftSxCIltW6EZPkU60XIMSspX_LuYLt9l3fitjLRRDUWtOXr8KOhlkgFDruV2xNCpHK03KRiBQNQ_sbGdHvJLDj2-VyOBQL3m3ph-8B8cglqaSHFHDJvGNzbyDmfoZaCA6SrC_WuQqXfE4yZlr2NR2IaFBNcjeN6wWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=H6FRQ85lwGDU7zX3Xq0bZJt6OuNfYptH-s2B-2rFYoSCnem0raLc2P_PV3Z3N3m9czrrx2yBO3h3wRpFhtAJOTtYEmmBlGguk_zG6-sGzieRKm2-_-D3CbYSxnYa5aupYCvjZHn4jsq_-L-x14B3WudUofjomm92DnMlwDcOe1iwpHppb9veWGNhEHCm2TTkMyS_7pWDzi6BiNPD5Lp_pvpFTJNNWsxqjXrlEws7uK4D31XJT3Cycy0waFKiyq1vdyL18yweum0JCAtnrrGEtk297ekkabOJwC70OfWlY-VQ4OE7R7QfVbmjmL6awdV4J_JGZlda-Qsa_OeyfzypGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=H6FRQ85lwGDU7zX3Xq0bZJt6OuNfYptH-s2B-2rFYoSCnem0raLc2P_PV3Z3N3m9czrrx2yBO3h3wRpFhtAJOTtYEmmBlGguk_zG6-sGzieRKm2-_-D3CbYSxnYa5aupYCvjZHn4jsq_-L-x14B3WudUofjomm92DnMlwDcOe1iwpHppb9veWGNhEHCm2TTkMyS_7pWDzi6BiNPD5Lp_pvpFTJNNWsxqjXrlEws7uK4D31XJT3Cycy0waFKiyq1vdyL18yweum0JCAtnrrGEtk297ekkabOJwC70OfWlY-VQ4OE7R7QfVbmjmL6awdV4J_JGZlda-Qsa_OeyfzypGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9dOxF6J6yGny45mbj5YUJu_tn0e1COhJTAtjGOZUZExJQ11EgPWGMI_J3NaxoDLFp2RFlOFd4rAXzL_hmHAN4K5xk5YElsqAw7JpbtQuR-ggF_5RHZUV4y_wfXrRloHUVyZY4n7NuH2s1lehAtiAjEiUrpSp2g94_lJf3pf5XG5HVaBKivRWINWfoAU1hiRlKWn3Ock32Tmv_mkCMbh8dBBWxy1VoYc5Q2K32LQ3fdZOP5WNEpKXkcMpa6Dl-t_pmKAyHd7qevu1hiTSi1usHjrwtdFbbck8JjsN3RZRqjks_A0TE1yBHvTW2ddWDRFbUdwqHeQ2IAyZ-x7PKgqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=irB4MNRicRsY1cqZ9FD5vvgWuU77gwUHrmKjLYSeP1oQVwbe6S5ouzNuqHizJ3utdxowHZUCQu7PEg4RFHu7FRObcxbR0rCpwz7vjZR3GGUwmhKht1xe9so60mQ9_LS-8BG9jdqkugsjAhBDjP1w_oel07XcIBaqZODRFDxJPK1LmAwvCGughXheg-GyDndKdysLQrQENhdjZbFyUxlS22-sRLwzyv5JmakHkVlKRQDXn1ATJBIV-0bb9ozI2k7Ru9VZ1nLP_uPVy3Qpgbdk6IActFiij1Y0R7nVby7QqcuW8rwoVko_7OcKIOhTetTmEVN1nru7HAcY6G6I-4cP3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=irB4MNRicRsY1cqZ9FD5vvgWuU77gwUHrmKjLYSeP1oQVwbe6S5ouzNuqHizJ3utdxowHZUCQu7PEg4RFHu7FRObcxbR0rCpwz7vjZR3GGUwmhKht1xe9so60mQ9_LS-8BG9jdqkugsjAhBDjP1w_oel07XcIBaqZODRFDxJPK1LmAwvCGughXheg-GyDndKdysLQrQENhdjZbFyUxlS22-sRLwzyv5JmakHkVlKRQDXn1ATJBIV-0bb9ozI2k7Ru9VZ1nLP_uPVy3Qpgbdk6IActFiij1Y0R7nVby7QqcuW8rwoVko_7OcKIOhTetTmEVN1nru7HAcY6G6I-4cP3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7QMAKVlfNrdgg90SS6OR3dLRThE3fvV_7ycyLXETG08bYseKZowRs9ZMKN_5BZJ9L2kcV4t3RESeCiPxiNbCm61Zxl23lmuMR0SPreIGTL_OVCTjZJWyv2mXkAdm9s0QqB_zLeWXsT8I0ygRYu22ya7Cy64uP6x4kVBt8uOAd7W0k-UlVirOi_51HGaz_hP-CaXt4oJeC7jYzU7qS9amxBQO0rssrwRVEpFgXWM9SV3Z7eEe6GOSy2yv-1aJb_70G8Jr4pVg03BRm8281PpbK_R24EeDmtmfY8B6OitwN-zVV14h_ieW2rIzxAtNxnoGUAoy3dmDVbAZqtdgEPycqfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7QMAKVlfNrdgg90SS6OR3dLRThE3fvV_7ycyLXETG08bYseKZowRs9ZMKN_5BZJ9L2kcV4t3RESeCiPxiNbCm61Zxl23lmuMR0SPreIGTL_OVCTjZJWyv2mXkAdm9s0QqB_zLeWXsT8I0ygRYu22ya7Cy64uP6x4kVBt8uOAd7W0k-UlVirOi_51HGaz_hP-CaXt4oJeC7jYzU7qS9amxBQO0rssrwRVEpFgXWM9SV3Z7eEe6GOSy2yv-1aJb_70G8Jr4pVg03BRm8281PpbK_R24EeDmtmfY8B6OitwN-zVV14h_ieW2rIzxAtNxnoGUAoy3dmDVbAZqtdgEPycqfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=YldOvusve51Os2CPkQ4uV4Qr3VRqtBk6zXWJCvIAarvnoPOxMs6Zvct2TACZ6ycS1jpzysWk_UoRYkaPIqWeWCpN2_BYeRkIR0-uh0sLIKExAbGiEppb_TZe7LLBvvu2zhheos6i0vfZNnBofhtdOa9AzNwMmX-9CW6WGa0Iquw0k0WmmTGDHuDcthOq-OZ72x-uowOZR76GJ8nvSyecnQCwfmt9QiKzbfOZVo7dVrsMZcFhJI6deAJjz1MxksoEWyuLpm_xn3ZOFHrog_2v2lrl9JJA3A4ImzE0QZJIeSgB_-oGY_8rERw1Zhpyqyx2ym_oCkXQ0inzv46l6gmvtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=YldOvusve51Os2CPkQ4uV4Qr3VRqtBk6zXWJCvIAarvnoPOxMs6Zvct2TACZ6ycS1jpzysWk_UoRYkaPIqWeWCpN2_BYeRkIR0-uh0sLIKExAbGiEppb_TZe7LLBvvu2zhheos6i0vfZNnBofhtdOa9AzNwMmX-9CW6WGa0Iquw0k0WmmTGDHuDcthOq-OZ72x-uowOZR76GJ8nvSyecnQCwfmt9QiKzbfOZVo7dVrsMZcFhJI6deAJjz1MxksoEWyuLpm_xn3ZOFHrog_2v2lrl9JJA3A4ImzE0QZJIeSgB_-oGY_8rERw1Zhpyqyx2ym_oCkXQ0inzv46l6gmvtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=IFNndpTmCwzmI-N7LU5X5sNPful27cVleXJNcgbWZyoQlRs-FXPDmL7jS2PvQ9Xo_pl_zr7BYQU8h6qRRepWWSQq2ErzW95xUXs6IdaVl4SXqkY-qGK0LlU81CJPlaR1FbullPNeDG00NqzG3imiMeSVPlULB1ggvQQ6QNNIRyik5e449YyvvR9rzauLXts6WoS1lWwK415MLb-v4DJhgoT_bj6bAKUk6SwfVIR79dkjNTIySGO12ZmiPSlvnrUbpihNctBGWESn21fnUzMqoEFNqAIlo24QSPeuShFtL5x6sEqpXstWz4zdG_TRxpqrcpB-09hrO7ryPj77x1s56A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=IFNndpTmCwzmI-N7LU5X5sNPful27cVleXJNcgbWZyoQlRs-FXPDmL7jS2PvQ9Xo_pl_zr7BYQU8h6qRRepWWSQq2ErzW95xUXs6IdaVl4SXqkY-qGK0LlU81CJPlaR1FbullPNeDG00NqzG3imiMeSVPlULB1ggvQQ6QNNIRyik5e449YyvvR9rzauLXts6WoS1lWwK415MLb-v4DJhgoT_bj6bAKUk6SwfVIR79dkjNTIySGO12ZmiPSlvnrUbpihNctBGWESn21fnUzMqoEFNqAIlo24QSPeuShFtL5x6sEqpXstWz4zdG_TRxpqrcpB-09hrO7ryPj77x1s56A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFxeq8r1hKLs6AwOw4EaRdkGSxqS2I7uNtEqxy_3pxt6X6a8qhj84_hVNkRW9XMJCwl2Y1ThsoEex7erH8KwgJvebi2dv3FBI7lXVl1MSBHYHzZ8Kgp0jq9BBX8g1EksnNBlbHBAi0wBtSCZ_huMq0WQdfOxPeTk8Jy4IM7j8LZOAyOZPudiR5OOL6eIinvfkgqgtTV5P3cJiYY6DiEX3ZjLi96C5eU3RK403EFxKD7XZUQ_flr8vhLaW-ZBDeb7zCazXLuCnaMWPBV8rpKfhAZzgR5OoL_oSshUE6wafu1zZ-QM6Udp2Qeqoq5V-j-jTHyuM6584j4oRwZ8bQXS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=PSprn2oAIEWkXEcCCrOXHPKfVpvP5P15amRG00iUbwVIMSVxn6HZZlSLpVgD_sovnXkiXvDwBz8AduA7qQSx-9jKpyGsnwiJ4wytrvuDnQ4vojU9G3t-AT0l9bK06vy9rIqus9CnQqcDj-8tkdY1wlg3N31_BkMCUmuom8Wa9xPtOs0VeF1GaNYidZ67rp_0NeGPqmJzE44UDP_vneNvXxNnfU6Px1oz3t5FfPCT8HD3Z8XhVrDpJgrIQ0kCocSZT0yXQcuLPEn4hCAOzUl8FDJxq8zwjGt_qqydgsbmk7kpbA_68MH1ou4zW9FVoWwXHVkY0PaQcUPBm9iGSJh_1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=PSprn2oAIEWkXEcCCrOXHPKfVpvP5P15amRG00iUbwVIMSVxn6HZZlSLpVgD_sovnXkiXvDwBz8AduA7qQSx-9jKpyGsnwiJ4wytrvuDnQ4vojU9G3t-AT0l9bK06vy9rIqus9CnQqcDj-8tkdY1wlg3N31_BkMCUmuom8Wa9xPtOs0VeF1GaNYidZ67rp_0NeGPqmJzE44UDP_vneNvXxNnfU6Px1oz3t5FfPCT8HD3Z8XhVrDpJgrIQ0kCocSZT0yXQcuLPEn4hCAOzUl8FDJxq8zwjGt_qqydgsbmk7kpbA_68MH1ou4zW9FVoWwXHVkY0PaQcUPBm9iGSJh_1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=kyrxqTu40TAafzRkJb8N7iFK-l-3bpQBPHsEk3RgGjyTW2A5hYe4RfZAqiLaf-00xhaJXKgLpyiqH7fuN_aDxcmg09iiK0EtWuyLZLp0c4W56ELm0bYmVUt6JLCYuBrukPmtMqlrCHPgTXucGOvZwWrTsb_9Os9VsARHFcKl8V_WPe0GyzI9fdX4XxpYtLAKKkMA8rz1Mgrzvdyy3XmE9OaLcpeQIxZuoGtkVOk2taMj4KWPl1hfKS_sId7_GDlVBOXwO9PembUYqG3aeBp3ISYk6pTiY5ho6W9-QJ3S5brE-zs-24qSrsTmGNEf-ommbiFe6y3rxXBake2vBVXg_zTY6PRyLVRXsLoxUomB20-Q10nqtCWul_37LPV1sGH_FjTADf_FqlDfqjgWNQVVmfLEh7IaDKQ77OxVq5nOz8lipauEL7_USfxqUSiTY_qIlrYiV5hLZtsQCaBVSZITb55qOHi0-sqBaU3JPRdzc3WP7Flur6r38np_pmkGhBVKVWVg_uPzAc5yimqXns6i9PsfW01CTiyoV5ggE0Ogwd9hMIfTcrqil8UhOSAfgTlDcR7gHvbt4NZpgzDMY-q2KQ1-SfyKBP0xYOk5lDp58GkC967WnqEYJ7BLPO9elwj_LhmrOB9nAjU8xgtomry94vDGNrUnguvvysWqhW6AX8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=kyrxqTu40TAafzRkJb8N7iFK-l-3bpQBPHsEk3RgGjyTW2A5hYe4RfZAqiLaf-00xhaJXKgLpyiqH7fuN_aDxcmg09iiK0EtWuyLZLp0c4W56ELm0bYmVUt6JLCYuBrukPmtMqlrCHPgTXucGOvZwWrTsb_9Os9VsARHFcKl8V_WPe0GyzI9fdX4XxpYtLAKKkMA8rz1Mgrzvdyy3XmE9OaLcpeQIxZuoGtkVOk2taMj4KWPl1hfKS_sId7_GDlVBOXwO9PembUYqG3aeBp3ISYk6pTiY5ho6W9-QJ3S5brE-zs-24qSrsTmGNEf-ommbiFe6y3rxXBake2vBVXg_zTY6PRyLVRXsLoxUomB20-Q10nqtCWul_37LPV1sGH_FjTADf_FqlDfqjgWNQVVmfLEh7IaDKQ77OxVq5nOz8lipauEL7_USfxqUSiTY_qIlrYiV5hLZtsQCaBVSZITb55qOHi0-sqBaU3JPRdzc3WP7Flur6r38np_pmkGhBVKVWVg_uPzAc5yimqXns6i9PsfW01CTiyoV5ggE0Ogwd9hMIfTcrqil8UhOSAfgTlDcR7gHvbt4NZpgzDMY-q2KQ1-SfyKBP0xYOk5lDp58GkC967WnqEYJ7BLPO9elwj_LhmrOB9nAjU8xgtomry94vDGNrUnguvvysWqhW6AX8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=uOyqNZSw17vRZxlQH7uExSSj8EvuD7POwJnndqAHCi0WsuieLxBZGN0B0oyoCimmkRdSdwOLZzXYABF1SYfBCgQRZGe80gAp1MIca2CA8BnQ0LGYfFXB5AxoCUyel7SYPy49K6KQY2b9ietCgfEiyRef9H2jS1rIqKBx8Hbn6kA_gTlzlD5nz2Kv-c-xx3-M9NjaPGTOQOPQoOULM8dLd-qGEC5B2nEJ_CfL-1E0s1Wmos8rc6NwEQ2AbfvT7uNp8Z0NqpoVM4BE9MLAnFKWJtk4JXv3qJiouquEm9W4rHJOjwJdTsskpbbTw0_qFZb1y6OiePeSyyE0r1KktfZLxkK5uu5g_5gBLe_j8loGA98hV6CFIjiSPovH8N05oE4aOmEFMhiJvJKl-e8e5cJos5gCUYzsRTLy8HCklD-0dp1GK4cEFWQ8j6eZqHnn32elcyCWSkzYiFD8KuzUT231fvOVWjm9XZiTJomoJOLHwUnPV5BgrvJDJ4zZltXZMgs2uVOK6KrcQiFgNu39RzxT8sxON8zjPoXL4gLaCbqzrwgjO80bqiKA0Bu0mFk-8lT_RjvIiUsPs8kraMv3t6ZpvNHbqiYdAQD6HBAyRprDftl697o5IQmwkhitC-Ls9bifevMlTzImBbfIahOSadOaexWW9JXotyvYLrVhA1ICWA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=uOyqNZSw17vRZxlQH7uExSSj8EvuD7POwJnndqAHCi0WsuieLxBZGN0B0oyoCimmkRdSdwOLZzXYABF1SYfBCgQRZGe80gAp1MIca2CA8BnQ0LGYfFXB5AxoCUyel7SYPy49K6KQY2b9ietCgfEiyRef9H2jS1rIqKBx8Hbn6kA_gTlzlD5nz2Kv-c-xx3-M9NjaPGTOQOPQoOULM8dLd-qGEC5B2nEJ_CfL-1E0s1Wmos8rc6NwEQ2AbfvT7uNp8Z0NqpoVM4BE9MLAnFKWJtk4JXv3qJiouquEm9W4rHJOjwJdTsskpbbTw0_qFZb1y6OiePeSyyE0r1KktfZLxkK5uu5g_5gBLe_j8loGA98hV6CFIjiSPovH8N05oE4aOmEFMhiJvJKl-e8e5cJos5gCUYzsRTLy8HCklD-0dp1GK4cEFWQ8j6eZqHnn32elcyCWSkzYiFD8KuzUT231fvOVWjm9XZiTJomoJOLHwUnPV5BgrvJDJ4zZltXZMgs2uVOK6KrcQiFgNu39RzxT8sxON8zjPoXL4gLaCbqzrwgjO80bqiKA0Bu0mFk-8lT_RjvIiUsPs8kraMv3t6ZpvNHbqiYdAQD6HBAyRprDftl697o5IQmwkhitC-Ls9bifevMlTzImBbfIahOSadOaexWW9JXotyvYLrVhA1ICWA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
