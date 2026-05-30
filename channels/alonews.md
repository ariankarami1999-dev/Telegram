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
<img src="https://cdn4.telesco.pe/file/AvrEjUeEN7UKx-Z8EXsbu19WRRQNzjKnDdbOFgqU2wW8lZr0xK40GN5WpoNyivhGzCf2mOEKD3wS-6aryX9L1x12rvLUT27xTsv2U_xxeaUSpzD5u0ZFEMxcAvpeRgcdP4uo76HwVd8NaO4LmlIeIbq9QP6rS_O_oUE2pQyWwTOpVcgwtm2qn_WFdLNBJbq0GzDk9iNK-MwORn2NxYuT0QvgQZ9k2eg5UQxaB8cD_7nxdkoGiPMRNKdGyzy9GMIQG0xUNlX1sxDjmW6MoOqMy6IXuyJyT0NrYzpE2ITHok2a9apZAzUePf6tOIuFvV43IbAbpzIbg1ZYa4TcWIZk1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 911K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 15:20:10</div>
<hr>

<div class="tg-post" id="msg-123678">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcs16yEQdjGUQG7s1PeInVeZh-tqERIjYEcSwdvsvniqsGqVwjxvIHcYZ8ZPqxMJaKvvjIhGq-yY5iZA5HN71dVhlIwyE-HuXq1gu3wwmphyjIOnmam6ANlV35ybuYi7HGSps0ritVY7ICiQtbev8QBVdnYTB5oP1FuCfbA2hP3Zof2Bu4LAM6buKRjwzwVuIc2EguTPIbyJ8ueYvzhx8BuV8m_Sk3gTJGAr24YDEORuI7ewR2QKovTQfFSGm23L4SBssn1BUY5bjxjHH4V854d89DeZjiOnOe9HwY2dPxVx5aSRm3LbwpYM_A-mwavd0I5lSyQ-sWScfQh9dGBNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی خطاب به وزیر خزانه‌داری آمریکا: به جای هارت و پورت اضافی به فکر تعظیم باش!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/alonews/123678" target="_blank">📅 15:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ارتش لبنان اعلام کرد که دو سرباز پس از هدف قرار گرفتن داخل یک وسیله نقلیه توسط پهپاد اسرائیلی در جاده آبا (نبطیه) به شدت زخمی شدند.
🔴
آنها برای درمان به بیمارستان منتقل شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/123677" target="_blank">📅 15:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123673">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uM_0XM47puM8NFig5JDFHf45-Bkm537WPN_3kjOrFe9ZoVPgLiWUfQWDC6G-xYN44HZS42p2WAf1z0HOJug_ybIsPPcPMWKGfWVPi-2glzIDl6z3-vBEypoEP9AHHLubWKDIj_wacopERFg18BmqhR8VPH91bx-7dLDixk_IqXJF_JJXK6KOR-uCS1l7IyQIaxQ7WCZmqufr6E42uBoJ0ZRhmVwlA1PK0Dix6KOawOUllXWGDthr7r05K4WrmDW5Sw2fzukWeXjcEVyw4335XNliBO938ujcwIZ5HW3pdnEru3pmq-Yu3Kn7vmHdeAt3z3xxT3uDFE78jnWsf-UeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UjtqcGJhiwjJAz1PmqX_5p_q2lHQxCjH3aBGYEXt_07_ICv22P-naicoI9UWu7lUO85lOD08WKEJLJ89AfSKkpxYhle-g8pOZcKEK7W1wr3-Q2o3BddGAKD58u8G3uGIIjspSzu4Kh2S3Wr23-6myKmLd69aq0JDbZbKcrrLzBpMxIjB3Xq2w29LO4Ul2199678J-NEibv6QSDCjsueFN8nZm7SHtnwgOCXXyng0lBNpRAp2pKxFksqKTP06kJR3i9puUhseOQGA7fmslNuZCLDDbS9lo1dRG01FdN9k4SPvVcfQ9I-cay0-wnxlGR9vClfXb-qsoBeJ0h4avVG6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MA6_XI0fiB55zkKqm7w3USQmcEURYjmPyMXW2PfrjjtyI9d-ud2atIZbyHT0GwTsdaIw0hduWdT1mB1WVU-NlmOkbrju_pYtkKKetwFf2FonRwWyMAJV1f9-vEzIj8Ux6OO6r1eckJcoGk2-N0AITPRVO2BwImRGSNuPuLhSyjwawPIcQmorEJ6pT1wsDpOwhZC0HqyWeL2GwNRC13UDKoEYZHDx8-_aSkv8cY0eWBZwTCrClvgbukFxbj_RCtnBTEpu0OZ3WLjtrRM919et6jptrWLhgmUfIeaZuN0UdpMP_KYWSmK-oGd7IsLYTYMeAGUcDymN6Q_cqZhVAAuvzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E96o34KAgujcYtmdSMvyeoSEBM4vPNvbTmbtTt4QhiAYGxr3arMrM23ieyVPZcBld-ByMHzlai0PUMJRsa7Z03PtbHhOJSNFCvvUEvfjb1caqcE9qJqeaxLZysG0em85yNtg3aJ0N6l0bpdCopMyzEQH9pJhAaA9r98CeBQ_i22-dToV-kbD1UaNo5uTfmDbYDg6chH35Gwc1_hapAuYfSpw8SCc1Nh3vJUA0bkr2mTRyrENFUDwUwTG0wBNgzkJqS4awD-OZ3dkiE7WMIoYBfkhqTOiLWyuhlEjTFOwyvl3EKLflCcG-qFWnK13RVSWoJLo1MMim0GS2Kn42pmfJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش سودان یک پهپاد رزمی CH-95 ساخت چین که توسط نیروهای پشتیبانی سریع تحت حمایت امارات در نزدیکی ربک پرواز می‌کرد را سرنگون کرد، تصاویر لاشه آن موشک ضد تانک Blue Arrow 11 آن را ظاهراً سالم نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/123673" target="_blank">📅 15:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123672">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا:
هرجا که توانسته‌ایم به اوکراین کمک کنیم، کمک کرده‌ایم.
🔴
هرجا که توانسته‌ایم اروپا را قادر سازیم تا بیشتر عمل کند، این کار را کرده‌ایم.
🔴
اگر به میزان پولی که هزینه شده نگاه کنید، اروپا وارد میدان شده و اوکراین در این فرآیند دست‌کم به همان اندازه (اگر نه بیشتر) مؤثر بوده است.
🔴
بنابراین، ما می‌خواهیم آنها بتوانند از خود دفاع کنند و راهی پیدا خواهیم کرد تا مطمئن شویم می‌توانیم به آنها کمک کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/123672" target="_blank">📅 15:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123671">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">💔
خانواده امیرمحمد شاه‌کرمی ۶۰ روز تمام دنبال پسر ۱۴ ساله‌شان گشتند؛ تا اینکه پیکرش را در سردخانه کهریزک پیدا کردند.
🔴
در این مدت حتی با گوشی امیرمحمد با خانواده‌اش تماس گرفتند و وانمود کردند که او بازداشت شده و زنده است.
🔴
خواهرش از لحظه دیدن پیکر امیرمحمد…</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/123671" target="_blank">📅 15:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123670">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce3370eb3.mp4?token=KyvofjRa3_9z4Acf5OaCyYGFbAt5w6CarK5RFpyWsguQpvsmiiKciDlBBkJbKnePIJ83cQTmfyYuIppG-1vHtwqIRhU1T8wbSAaI_69DqemgCu6EJ6ZEJa6LCxci8GtElGWv22lYKqzdy2VW4nJqgoQ-sQp05Q8KgOo5UYwvuV2kuJhM9QhUQF90xiR3wpXXPkunEQj9BCCRYeXJrzznNdLMCKFT0m7cLpLXPmFxiNwYxJiZSIw01CrIrpVcVidHNl-kq2To6tGHTNPxkqeC-58tMiIF_AJ0fec_3e_0gXqXcZRcgV6gwIASodIotdYpC2akwp7_f5ebJQBGf1QReoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce3370eb3.mp4?token=KyvofjRa3_9z4Acf5OaCyYGFbAt5w6CarK5RFpyWsguQpvsmiiKciDlBBkJbKnePIJ83cQTmfyYuIppG-1vHtwqIRhU1T8wbSAaI_69DqemgCu6EJ6ZEJa6LCxci8GtElGWv22lYKqzdy2VW4nJqgoQ-sQp05Q8KgOo5UYwvuV2kuJhM9QhUQF90xiR3wpXXPkunEQj9BCCRYeXJrzznNdLMCKFT0m7cLpLXPmFxiNwYxJiZSIw01CrIrpVcVidHNl-kq2To6tGHTNPxkqeC-58tMiIF_AJ0fec_3e_0gXqXcZRcgV6gwIASodIotdYpC2akwp7_f5ebJQBGf1QReoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث: آنچه در بودجه سال ۲۰۲۷ رئیس‌جمهور ترامپ خواهید دید، سرمایه‌گذاری ۵۶ میلیارد دلاری در تسلط بر پهپادها است.
🔴
ما همچنان از آنچه اوکراین در میدان نبرد انجام داده است، می‌آموزیم.
🔴
ما چیزهای زیادی از اوکراین و نحوه عملکرد آن‌ها یاد گرفته‌ایم.
🔴
قصد داریم نه تنها هم‌سطح باشیم، بلکه بهترین در جهان در این زمینه باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/alonews/123670" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123669">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
مدیرکل آژانس بین‌المللی انرژی اتمی: ما گفتگو و تبادل نظر حداقلی (با ایران) داریم، اما در حال حاضر بسیار محدود است.
🔴
دیدگاه آنها (ایران) این است در حالی که درگیری ادامه دارد، زمان برای از سرگیری همکاری کامل فرا نرسیده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/123669" target="_blank">📅 15:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123668">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWie38ey8b4W4ojcC02Y2h4BAVuALasu9bY9wccF47Xx1ODtKU2DeybGFLcEpemZAAHDb7r6fHcMB4TynYhpC83qNitXsC1vkdGITshrH8tBhh_JnwTtyUQZZAXZZVeokHKb5b7Mal81BC-Yj34wANmnT20M0lvOZmuafu4Xk3yUABIP4e4VrCWJG4TQu-yPGei3vdNaZxukaeizNTULmwoBaHNBDRQ26okRQg_EJL0BzxCHXhYDLIjsaAZ2jxJHYn7iB5qNntEGdAnEusMsd7B-TJJL_Te1zlEidZ6kvYqtrlwlkS8B-9aPdgl6TszqOmScPz3Ww9DsuFNjaSP9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت برنج در ماه می ۲۰ درصد رشد داشته که بیشترین میزان در دو دهه اخیر بوده است
🔴
به غیر از افزایش شدید قیمت کود تحت تأثیر جنگ در خاورمیانه، شرایط آب و هوای سخت در کشورهای آسیای شرقی هم چشم انداز تولید برنج را تیره کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/123668" target="_blank">📅 15:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123667">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری / وزیر جنگ آمریکا: به محاصره دریایی ایران ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123667" target="_blank">📅 15:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123666">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مدیرکل آژانس بین‌المللی انرژی اتمی:
ما گفتگو و تبادل نظر حداقلی (با ایران) داریم، اما در حال حاضر بسیار محدود است.
🔴
دیدگاه آنها (ایران) این است در حالی که درگیری ادامه دارد، زمان برای از سرگیری همکاری کامل فرا نرسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123666" target="_blank">📅 15:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123665">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
الجزیره: وضعیت امنیتی در تنگه هرمز هنوز «بحرانی» است
🔴
هیئت عملیات تجارت بریتانیا اعلام کرد که سطح تهدید امنیت دریایی در تنگه هرمز به دلیل اقدامات محاصره‌آمیز، همچنان بسیار بحرانی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123665" target="_blank">📅 15:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123664">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d88485ba.mp4?token=qPQyek4Ps0VzXQUfcTP-COHpN3fScAJecUGgk6FNth3z3Q2kQFrbKXlueZL7dvfneiugRy_N0VJINoN-CNPPPS9XSRqeqSpXWZB2ktNg-dbF1wu-4NIKFG4qTZLMZtkSruHuto343HeO_SGwkSOQz2tUGjyxGPJJnboVzM_6HGp6uJT3eh-ugKI3QiGwRqG8i6PfnbT1gp8dXAzC7NsF5Poa0ySBlYDhbgN1BtvhXmTodb_1rBxsE2oqEcSrBLNmQgYbSnmOHxPeRo0RVoV7rC0Nr4OAyJouLkD6mUCV6bPF_4-OKemlqm48Cz6zVdY8IIP1k88iROVPKdWP8goeYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d88485ba.mp4?token=qPQyek4Ps0VzXQUfcTP-COHpN3fScAJecUGgk6FNth3z3Q2kQFrbKXlueZL7dvfneiugRy_N0VJINoN-CNPPPS9XSRqeqSpXWZB2ktNg-dbF1wu-4NIKFG4qTZLMZtkSruHuto343HeO_SGwkSOQz2tUGjyxGPJJnboVzM_6HGp6uJT3eh-ugKI3QiGwRqG8i6PfnbT1gp8dXAzC7NsF5Poa0ySBlYDhbgN1BtvhXmTodb_1rBxsE2oqEcSrBLNmQgYbSnmOHxPeRo0RVoV7rC0Nr4OAyJouLkD6mUCV6bPF_4-OKemlqm48Cz6zVdY8IIP1k88iROVPKdWP8goeYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
خانواده امیرمحمد شاه‌کرمی ۶۰ روز تمام دنبال پسر ۱۴ ساله‌شان گشتند؛ تا اینکه پیکرش را در سردخانه کهریزک پیدا کردند.
🔴
در این مدت حتی با گوشی امیرمحمد با خانواده‌اش تماس گرفتند و وانمود کردند که او بازداشت شده و زنده است.
🔴
خواهرش از لحظه دیدن پیکر امیرمحمد در سردخانه و شیون مادر و پدر ویدیویی منتشر کرده و نوشته: «برادرم خوابیده بود؛ سرد، بی‌صدا…»
🔴
امیرمحمد ۱۸ دی از خانه بیرون رفت و دیگر هرگز به خانه برنگشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/123664" target="_blank">📅 15:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123663">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری /  منابع ارشد نظامی لبنان به آناتولی می‌گویند نیروهای اسرائیلی از رودخانه لیتانی در جنوب لبنان عبور کرده و به حومه شهر نبطیه رسیده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/123663" target="_blank">📅 14:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123662">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
بلومبرگ: تداوم چالش‌های اقتصادی روسیه به‌رغم جهش قیمت نفت خام و لغو موقت تحریم‌ها
🔴
بر اساس گزارش بلومبرگ، جهش و افزایش شدید قیمت نفت خام که در پی جنگ ایران رخ داده است، نتوانسته اقتصاد روسیه را از بحران نجات دهد.
🔴
این گزارش اشاره می‌کند که حتی لغو موقت تحریم‌های ایالات متحده علیه نفت روسیه نیز برای دور نگه داشتن اقتصاد این کشور از مشکلات و چالش‌های جدی کافی نبوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/123662" target="_blank">📅 14:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123661">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
صداوسیما: سامانه آرش‌های کمانگیر که چند شب قبل یک پهپاد اوربیتال را ساقط کرده بودند، دیشب نیز پهپاد اسرائیلی را بر فراز جزیره قشم سرنگون کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123661" target="_blank">📅 14:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123660">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
العربی الجديد به نقل از منابع رسمی لبنانی: جلسه پنتاگون دیروز هیچ پیشرفتی به ویژه در تثبیت کامل آتش‌بس نداشت
🔴
اسرائیل تا کنون بر ادامه عملیات خود و ایجاد منطقه حائل در جنوب اصرار دارد
🔴
درخواست‌های از سمت اسرائیل وجود دارد که در شرایط فعلی قابل اجرا نیست
🔴
ارتش لبنان بر اولویت آتش‌بس و عقب‌نشینی اسرائیل برای گسترش نفوذ در جنوب و اعمال کنترل خود تأکید دارد
🔴
ارتش لبنان در جلسه واشنگتن وجود موانعی را که مانع اجرای طرح محدودسازی سلاح می‌شود، تأیید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/123660" target="_blank">📅 14:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123659">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
اسکورت هوایی پوتین در آسمان آستانه از نمای کابین جنگنده قزاقستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/123659" target="_blank">📅 14:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123658">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc124551.mp4?token=eYSft-OTIlM4ID6oSIn707U7WlOlad0WK4rLA5sTdaD3MY6vUP6v9QwQAeT-biR6eEuvKjfw7Pc8abexrbVT59-9XBMcjQfeun_JeiWKD-1JMh2QPvrIAoPLUpIGl8fh_jnc82xcgwJpmtreHxdE_1OHBwjWsvas55ze3o2M9xUb16al2-zhmzrahlg4RWaWRR9XFkDlPQAb9VgLN6WeC_tWHGskss83ihYpi-0DDCWYWVxZNVs1_PyD_9hJYQK3-9nDxNVS3WL6zap4HRKX854w5rwnSsEAhrEHAT42t25fVGQxcVxqIbx0CMsta7W8M8gJ_2WBxa1n15TstCyMng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc124551.mp4?token=eYSft-OTIlM4ID6oSIn707U7WlOlad0WK4rLA5sTdaD3MY6vUP6v9QwQAeT-biR6eEuvKjfw7Pc8abexrbVT59-9XBMcjQfeun_JeiWKD-1JMh2QPvrIAoPLUpIGl8fh_jnc82xcgwJpmtreHxdE_1OHBwjWsvas55ze3o2M9xUb16al2-zhmzrahlg4RWaWRR9XFkDlPQAb9VgLN6WeC_tWHGskss83ihYpi-0DDCWYWVxZNVs1_PyD_9hJYQK3-9nDxNVS3WL6zap4HRKX854w5rwnSsEAhrEHAT42t25fVGQxcVxqIbx0CMsta7W8M8gJ_2WBxa1n15TstCyMng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در شبانه‌روز گذشته ۲۰ کشتی با هماهنگی نیروی دریایی سپاه از تنگۀ هرمز  عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/123658" target="_blank">📅 14:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123657">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_qjeMvfJx0-BNt8CrbabKBn3B-ljsr9v0et_sU5lRuEvZE_yD6-0rBl3prFj3dPJi8srcSC0IR2_mLaT_O8oGubLtzQOUXIfyU0vpxZ4uTRJhxAfW8VySm2mBuXNVJsw5tMYBrMVMiXH1ISdNjIOqM_9UE7j9yQbralG7a95e8G1AD1FbMwobA59_ArPDjaVjBbiv01NxoWLoGzAT8xRjqXJBxxsddiMlpRQDT6If88jsBSg1SPJhxX_0tODbMfw9K_0bfpVqKPxG49MQZRdSCQ62r_Ti2lD7fPoJUzrL3q07nGQ9uSzjjDpTRQUF38kmsdNvT9drNp9I4yhK4Prw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای اسرائیل چهارمین هشدار روزانه را به ساکنان جنوب لبنان به ویژه این شهرهارا صادر کردند: المرونیة، اللوبیه، مایدون، انصاریه، زفاتا، تفاحیتا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123657" target="_blank">📅 14:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123656">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EruCxHiXcEJO1oZmu8DQgLrMFPBQEhKGzEBu32CAyTM-dzzx5CyjSbDtcT_9xybgNaLbE6VjGzcWadW3WdQmEHNU7-CRUeiIGDYc2HssSdohZpk8zGlpFFcQ3OoI2Wb5tZZH9gA5BEm9IQlVw4joHBQ3UCJbMkp27uWaWBJP-y5OWYIvfOZZYA8JPjcJo3L8zIlVcHIgRAdidWN1rebrCNk4xR7Jz2hD4dsBKJpAwyWiFkauPc2ZKRWaqT1H4kQf8r1ECCtlggDG0YAgLXfJPqvUJryi3aj88yWm-uJMCY681bxIKBJH1oT0_cMAD-hNqjpVyoAL8AxU6bKWHKacSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123656" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123655">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وال استریت ژورنال: عربستان سعودی در اوایل آوریل به طور خصوصی به واشنگتن شکایت کرد که ده‌ها حمله تلافی‌جویانه امارات متحده عربی به اهداف ایرانی — از جمله تأسیسات نفتی در بندرعباس و عسلویه — در حال به خطر انداختن زیرساخت‌های انرژی خلیج فارس توسط حملات متقابل ایرانی و افزایش قیمت نفت است.
🔴
ریاض از آمریکا خواست تا ابوظبی را تحت فشار قرار دهد که این حملات را متوقف کند و به تلاش‌های دیپلماتیک بپیوندد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123655" target="_blank">📅 14:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123652">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/MLS-YP_DzMnTVDKTScW6LD3ItZmvKOveBzJ3-uhP8zLD9MN92sBWAVw29-3VNPcsJx0vfk3gqKBrpOquPmqzrsFwgaNADVUfkIOklk9oe_29-EfSJV0Ob1v6wmbuJ899lDuj7dK1VEGUXagfT5hfdkW2YjrPMZyx993ype2LNoegNeSGVI6l7ucg6YL1VgBoEp3Qp1fx8BebFWn2Da6-buR6p8bl-mWtqEGpl37GzPZxMLIX88z-pWQqJ1byUEcBnebSC3fkDc3MiF29jlqD5EMaNXw_Ai7IQwZHAqI_HXAwMnM6wSXY9Vl1lojiH4aJmSbvBgD_Z5G-ojYTaqq64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/A5U3p5mkJIrD6V1r7rDADtOl6XIVnU_QG_9KsbpRT0M385rp9Y9Vj3qCPtZMGIPNJbZNTOZas75JN4MEh9E_Y9otYt86sjicRNxdRSr8XMTmkNodzDt0LUNkrMg2ucL16PSIQ7ozfSlWbawaImPJMVJEr5fyJ6oNE_ANJtIpKYvJ0DgnVZjBb9cKEKPm-cIII8LhSQsAgPDTgwTFWZE0VU42dmmutAe7CgPjTZn1_ku_nCp-8f_DV3eS3Iwzl8r03WVtOLCHb1CnUFmat2bzNNVUcMwVOJ37cvSOtJC1s5owMSraeZiMm0_qAv51yLd9-6OZ1m_y-Cjs3vWE6TSv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Boeu14ZiThqYRLu9md6OL6MU0B8Tp80P7QaKFgAENJx9WutDMmemlyetMF6SeXS_fBwSJZ6KUNngiGw8T9_VSeny2BAhZfXVyshnwPFpBm4DidPENH5gpjQFAE4zKbBvFJf-PDDp5yY5kDzhuholB8yWMG9JsMAlgECkenH-I3-n6SB9kqwJPnMPt99hyAg8ir6IUH1pcvb1iS4b8GvQwcJGdy8yqNhYFesZ3qR_clQTU1VqpzXdU6Gv-37JGov71RzMYkAWbbpTlkKdBmDbWb8jLCQoWV1otG3yeAp2udfWf07XzTeiwM3lymrq_Hj58aWqhppo9Ov5D_YaCTtJJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک سامانه پدافندی میان‌برد سوم خرداد که توسط نیروهای سپاه در کرمانشاه در حال بازیابی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123652" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123651">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
قطر: عوارض موقت عبور از تنگه هرمز قابل مذاکره است
🔴
شیخ سعود بن عبدالرحمن آل ثانی، معاون نخست‌وزیر قطر، امروز در یک کنفرانس دفاعی آسیایی در سنگاپور گفت که قطر با هزینه‌های قانونی دائمی برای عبور و مرور از تنگه هرمز مخالف است، اما عوارض موقت قابل مذاکره است و می‌تواند به احیای عبور و مرور عادی از این آبراه‌های کلیدی کمک کند.
🔴
معاون نخست‌وزیر قطر همچنین گفت که دوحه در تلاش است تا روابطش را با آمریکا و ایران متعادل کند و به دنبال اجماع در شورای همکاری خلیج فارس بر سر یک راهبرد جامع در قبال ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123651" target="_blank">📅 14:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123650">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نیویورک تایمز: پیش‌نویس توافق آتش‌بس بین آمریکا و ایران شامل یک «برنامه بازسازی» و «صندوق سرمایه‌گذاری» است که بخشی از آن توسط ایالات متحده اداره می‌شود و در صورت توافق نهایی به ایران وعده داده خواهد شد. برخی از منابع آن‌ها اعلام کردند که این صندوق ۳۰۰ میلیارد دلار خواهد بود و جزئیات بیشتری در مذاکرات بعدی مورد بحث قرار خواهد گرفت.
🔴
گزارش شده است که مقامات ایرانی پیشنهاد داده‌اند که شرکت‌های آمریکایی، مانند شرکت‌های نفت و انرژی، اجازه سرمایه‌گذاری در ایران را داشته باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/123650" target="_blank">📅 13:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123649">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
اداره عملیات تجارت دریایی بریتانیا (UKMTO) گزارش می‌دهد که سطح تهدید امنیتی دریایی در تنگه هرمز به دلیل محاصره همچنان بسیار بحرانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123649" target="_blank">📅 13:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123648">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کریدور جدید ایران–پاکستان به شبکه ترانزیتی چین متصل میشود
🔴
گزارش‌ها حاکی است کریدور تازه‌فعال‌شده میان تهران و اسلام‌آباد که بر پایه توافق حمل‌ونقل جاده‌ای سال ۲۰۰۸ دو کشور شکل گرفته، اکنون شش مسیر زمینی را از بنادر اصلی پاکستان شامل گوادر، کراچی و بندر قاسم به گذرگاه‌های مرزی تفتان و گبد در ایران متصل میکند.
🔴
اهمیت این پروژه در اتصال آن به کریدور اقتصادی چین–پاکستان (CPEC) عنوان شده است. از طریق این مسیر، ایران میتواند به شبکه ترانزیتی حدود ۳ هزار کیلومتری متصل شود که غرب چین را به اقیانوس هند پیوند میدهد.
🔴
همزمان، ایران نیز پروژه راه‌آهن چابهار–زاهدان را با پیشرفت بیش از ۹۰ درصد دنبال میکند. این خط ریلی که قرار است در سال ۲۰۲۶ به بهره‌برداری برسد، بخشی از کریدور شمال–جنوب محسوب میشود و بنادر جنوبی ایران را به روسیه و آسیای مرکزی متصل خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123648" target="_blank">📅 13:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123647">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
عملیات انهدام مهمات عمل‌نکرده در سنندج از فردا یکشنبه ۱۰ خرداد به مدت یک هفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123647" target="_blank">📅 13:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123646">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس: کشتی‌های روسی و چینی از «شرایط ویژه و رفتار مطلوب» برای عبور از تنگه هرمز برخوردار خواهند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123646" target="_blank">📅 13:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123645">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
یک منبع نظامی به الحدث: وضعیت در جنوب لبنان نگران‌کننده است و وضعیت "در حال از کنترل خارج شدن" است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123645" target="_blank">📅 13:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123644">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
مسافرت قسطی هم از راه رسید...
🔴
وزارت گردشگری: تا هفتهٔ آینده کارت‌های سفر در اختیار مردم قرار می‌گیرد.
🔴
مردم از طریق این کارت می‌توانند هزینه‌های سفر خود را در درازمدت به‌صورت اقساطی پرداخت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123644" target="_blank">📅 13:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123643">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
معاون امنیتی فرمانداری بندرلنگه: به‌دلیل خنثی‌سازی مهمات عمل‌نکردهٔ دشمن تا ساعت ۱۷ امروز، احتمال شنیدن صدای انفجار وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123643" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123642">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM08AJ4I0_5xqVFPDSFdrTFdvu9ndkoyKeEq3pXaFiDvHrw4829tWIh6oRuLlENkt0Gd5TTTNwaEjw4ijPkMhTg0P5zfaihrjCgaLQ01NBizZ_f-X1LqvXbaz_jtw_JlTDwFcW64hlo605Ym19CjKYIuhdSnV4DH_RhpHTMQV1UBte6xrFPHrREFor-vFTTx_8sM6H_Ur4wcAcORpr3Ca0JHGBYrnUpBz9hDytduuflP2iT5k7O04F-gr_1Nwg2O7vymDT76mkeA9fW51ZWn5znf7YC_7p8v3qwIRoomSVbE9OArwNFVLtSgzY45E8TH5ATSAlGDfU-LC7RYzFhMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای نیویورک‌تایمز به نقل از مقامات آمریکایی: تندروها در ایران مانع توافق هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123642" target="_blank">📅 12:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123641">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
هاآرتص: تهدید به استفاده از زور نظامی علیه تهران اکنون تأثیر و قدرت کمتری نسبت به گذشته دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123641" target="_blank">📅 12:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123640">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCknAN2PrJU5eWLYynGsl6wRyZ0ye5-7fXdsy2HWvlgNRrSAE4sZk7K-TNzK04ZNBcu0u7yxkwx46LuQ2ao3BJOahbuOJRbkpnTa7p3tunbO2hecqCp3hB-v77T2wKkYds3DRdnz8KCFeePPNkOIt50vsDqe4QHCn8Y5ZEpxPwK2SS9Sf00hQpCiRhnkp6tVUbZ2P_o3bhAR0-WuQtwt5NfKarvaMGrGRCVOtWbUJNBmsGoZg-_mVOa_Akzdodb_tXhpjAxJa_L_5py5ZiiuzSYdBq0O4JA0IZpQ-9E_AKLJ8EiouHJkGTYEeh07Qh6Kmz4moBe_bWIg28rltODUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های ماهواره‌ای نشان ‌می‌دهد یک کشتی فله‌بر ایرانی به‌نام کیوان با عبور از محاصرهٔ دریایی آمریکا به سواحل ایران در نزدیکی بندر امام خمینی رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123640" target="_blank">📅 12:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123639">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ULgEqqjGaZfJCdB3ddG4VJY3T_u-KXYeWT_R1-u_dswQsqkIexxjlnVFEz32bVjrcJeMOT18Robki9p2KQ6GSI9IR8rWx_9NEAdpzXYc9WeSAFhHnM75IUGE1nEI8N8ZkyDoN92Y2-XRgm8VmkBlt-9OFY3-8o_Y-uTc7PKJUXAw5kBYIS5nygwVZGldQ32sXLyFutzpLbG-bOfb4LhsPSPQpQyBdMQrTNe9m1GGsq9sbv22GMLNlJ-gfHVUPcWlOlyxF8cbalyfKv68jlTAN5l9gZq6s4SBSm-dRRkLTty_n2ao1K_DoKJGu3ji4IEGT3weQGCTsooP11fMucYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار در تاریخ بورس ایران، هیچ سهمی منفی نیست!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123639" target="_blank">📅 12:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123638">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ: محاصره دریایی ایران از همین حالا برداشته خواهد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123638" target="_blank">📅 12:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123637">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یه مقام آمریکایی به الجریزه : ترامپ هیچ توافقی با ایران رو امضا نمی‌کنه مگر اینکه به نفع آمریکا باشه و خط قرمزهاش رعایت بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123637" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123636">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فیلد مارشال  محسن رضایی: رئیس‌جمهور آمریکا برای بار سوم درحال خیانت به دیپلماسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123636" target="_blank">📅 12:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123635">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
مقام ایرانی به الجزیره: هنوز هیچ چیز نهایی نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123635" target="_blank">📅 12:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123634">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
از امروز محدودیت‌های چک برگشتی و لحاظ شدن بدهی‌های غیرجاری وام‌های زیر ۷۰۰ میلیون تومانی در امتیاز اعتباری، پس از پایان مهلت سه‌ماهه بازگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123634" target="_blank">📅 12:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123633">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ارتش : انهدام یک فروند پهپاد «اوربیتر» در منطقه قشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123633" target="_blank">📅 11:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123632">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERULZZbaRpiekOyZr_hrXI7Xs9WW53UhJiJQbRhaaVHtCIHUEvtI-KHJNixadKaDfrqKEHLitydHubVsdj5TSdUu4YK7Uf66OOjhts-kdBleqhOZRdrX71K8LGmM9zxkHQs2rCOMuxV961XNlT4C3NYWQSf1rLMK8J3gX6wJY-qhU8tKdVUULrbcrmJjEhkre0FpG2uINmB1nEBlhB8Rya1oUDUCnj0CFXh6JK47XGJp-Jt4bf4SxnqdfOsKkKN7R6PGDD4BZogWko3si0xquRXFBpBunONQPWln-BpVJgSj87BUMPIlZ2nU5f0YBVUbjwJ9rymMNhOjbGXzQuQidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین شریعتمداری: ایران باید فورا از طریق یمن تنگه باب‌المندب را ببندد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123632" target="_blank">📅 11:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123631">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
کلش ریپورت: روسیه سفیر خود را از ارمنستان فراخواند و خواستار مشورت شد و همسویی روزافزون ایروان با اتحادیه اروپا را دلیل آن اعلام کرد.
🔴
روسیه تهدید کرد که در صورت ادامه حرکت ارمنستان به سمت غرب، عرضه گاز و نفت بدون تعرفه را قطع خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123631" target="_blank">📅 11:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123630">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uvur-BL2z1Ome_-JA2huRcS9ZQzS_RGOctZLnJGaXq6F_eQ7K66iGuE9qfFtichht9XAf7oMvR_2KYFNBebHryx_sEeWCwQk7HHUHcpKdVmQTJjcAn7XSLP677UlX0doCsYSxB-x0rVpw8ArHlmTHChck_97kDBSs96S69SqR200VoTBTVsGjvDRv9IK8y8bwwsS_y5bH6yjICaGgAkInZ6FF0mQRpS5PV-9nkZ1N2KQlfCi2UXF2ssLm57bDCeFCc0e4BsbUmDsWy-2u5V7rA1AGwUrKBumKvuTmHHH9tSA7Cv7dpS6VxNIXrBnpyPqFy-Wz2-JOSReAz5pYC0DCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۱.۱۲ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123630" target="_blank">📅 11:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123628">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ut1ZuRahZTmw6UpveiuJgdUKV1__cJeY90RngHjouyLKxevZt6Dx19xNCLuvYfnrPIpDYDwAYvBanepqz_C9sjDOzh2fq7V_9JS6K4tXh7Hz8DqQLO8IEQREAuqF887a0LfP3_bK3bi5HhQA8XFW8plD6i3y2ea3SjjrIzlUXGrzdK5jmCJGV6ShcO2qlY6OI6FOxjc9t1oNsYbouHK7Ia7N3qQdEDKcnEY7uAJGjHrit0FguNKfOVYqVZg3JWJkjtxyEuxZssm-iz4sxscEK1jubijtkd-7z_A8XwvSIyGAF5_gy1CvWUW4g4H6a4_iKoNUXCBqvIXhwRqddxBY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egE3-_S8I3grCnN6nm_aMvokeXCVgKNl7z_6zwb8HuJZMR5MX_5_oMTJpFXpkAnV4BpSpGDbtjCBbgk3OZJ4S6EWe848I3RA5a-NSGC_k_HAmphweAB1nqPZG9XHYCcBU50ncJ7ft24_eCdGDFw9SgHoy-CDRw9UeUUCCXsob8GD9_Xd11kxQ__wa7HY2FTYIVjxl-6y4Pv_CVj0UhNomhhPt1LIqIgdbdEmM7TzwCJ4Kir5uZKFBx_rK_ia2cnaWs_UQGCRJogaQ4PBXbheH4sGYnOn1XpjCeLkwF4cMjgzZ1AE4Sjm2tq5CJH9ub8QWlhLwdwa1zT8nKi4N74tJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به مواضع حزب‌الله در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/123628" target="_blank">📅 11:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123627">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB5eYdLoCIPc2ZiVgpZn-Kdhvoh2W8HoH4unSy2nj5V9nzaW1OMsZjwY_RA15hKzlZ2eE1Xs0N5OWFI8j3DG47eYjkoG5LFeKXcNBA4gZqiYEgrLP5LMAA885QxbMZ4RRZSt1GJYQ04hdqiZj8klFuQDjU_C4MxM13jSt4ZQpxuXFGfZfX5PnFLvmmXY4I0PrmEmSOAaQ5_wprl1bJtVop3easOTnr6pwrIfIrCJ6iGg2Le6hq1rchrJRw12ky8KYlwti1ngSKdZL7cPdJVOkjB-ao81B1APiLB4PTMlyi1LH1AOieE2RM4oqLR6fnjKw8cb5NIyXkkZCaEXAERopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: جنگنده اف-۱۵ای آمریکا، ماه گذشته با یک موشک دوش‌پرتاب چینی در ایران سرنگون شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/123627" target="_blank">📅 11:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123626">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kRq9HKBnQYZuLgmaC-s_4I8OUIgV2J--2middLtjBanYubyUXY7Hm89EknJsJGLx4HdZiCXYFKeUETugX-QE2eyJQHoEUR-TFv9ViCcGgTMUE7iLXoHeB_FkROHP-GroI0rlpZOtq5pFXwriiui5SOmqrzsI5nDoUsmZNFGADneT0fErGAXTjF8z7M-miM0zL8xP8d1qDXUGKIpJ68zbYkcQfX8D-Kj85IZPpSfiZZuk7b1m_p4vuKN94Aa7NDoMKFyh0S7-NP4kGFWN8lvgeat4E8HG2EVxFw0Feg7tokhW9QYi-hg3l-5NGrOyWnoCJ2TMsEQwi1S54PQyevZeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید آخرین معاینه پزشکی ترامپ را منتشر کرد و اعلام کرد که رئیس‌جمهور ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار دارد، هم‌چنین قلب او ۱۴ سال از سن او جوان تر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123626" target="_blank">📅 11:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123625">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
کنکور سراسری به همراه آزمون پذیرش دانشجومعلم پنجشنبه و جمعه ۲۹ و ۳۰ مرداد ماه برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123625" target="_blank">📅 11:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123624">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مقام ایرانی به الجزیره: هنوز هیچ چیز نهایی نشده است
🔴
او مدعی شد تیم مذاکره‌کننده آمریکا چارچوب حرفه‌ای و اخلاقی مشخصی ندارد و مواضع و خواسته‌های خود را به‌طور مداوم تغییر می‌دهد.
🔴
این اظهارات در حالی مطرح می‌شود که گزارش‌های مختلفی از ادامه مذاکرات، تبادل پیام‌ها و تلاش میانجی‌ها برای کاهش اختلاف‌های باقی‌مانده منتشر شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123624" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123623">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نیویورک پست : آزادسازی منابع ایران مشروط به بازگشایی تنگه هرمز و پاکسازی مین ها است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123623" target="_blank">📅 10:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123621">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نفت برنت بیش از ۹ درصد ریخت و طلا با رشد ۰.۸ درصدی به ۴۵۹۳ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123621" target="_blank">📅 10:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123620">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز در جنوب اصفهان، احتمال شنیدن صدای انفجار در این منطقه وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123620" target="_blank">📅 10:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123618">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f402cf90.mp4?token=mdPjLfFxs4MHhL2kS0P8lNmyQwRpRew_7l8pjRjTxe7Ew8g9BG8LZ0jDa4shUaU_JHIlauFJdIBWyOtWZCz5iXLe9RRUomjOjKcWPFmb3X0EfNKn94h5sGFJuqGppR10UUkX75tZ4dEMAg0NqqfkZjhqYPrDQw0xvrEwA1KlUH_uOwyISPNk3fwiNEq7Au3j9qoJo6tHYBIWgCQReOrn0QbqBqcmN8AUqYFARO7qngiKMTf9U0zGVvJkvUGBWNvaBjyfG4BGYJv8r5Nc8HpCbjK7e0ij7_5MtTzYglfwunH_wt-i0GMGGnO_dIWxzEjKYwsmglit8re5zpo6cHS0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f402cf90.mp4?token=mdPjLfFxs4MHhL2kS0P8lNmyQwRpRew_7l8pjRjTxe7Ew8g9BG8LZ0jDa4shUaU_JHIlauFJdIBWyOtWZCz5iXLe9RRUomjOjKcWPFmb3X0EfNKn94h5sGFJuqGppR10UUkX75tZ4dEMAg0NqqfkZjhqYPrDQw0xvrEwA1KlUH_uOwyISPNk3fwiNEq7Au3j9qoJo6tHYBIWgCQReOrn0QbqBqcmN8AUqYFARO7qngiKMTf9U0zGVvJkvUGBWNvaBjyfG4BGYJv8r5Nc8HpCbjK7e0ij7_5MtTzYglfwunH_wt-i0GMGGnO_dIWxzEjKYwsmglit8re5zpo6cHS0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک راکت حزب‌الله به مرکز کیریات شمونا در منطقه گالیل پان هندل، شمال اسرائیل، لحظاتی پیش اصابت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/123618" target="_blank">📅 10:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123617">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سی‌بی‌اس: انتظار نمی‌رود که ترامپ پیش از تصمیم‌گیری درباره فروش تسلیحات آمریکا به تایوان، با رئیس‌جمهور تایوان، لای چینگ-ته، تماس بگیرد.
🔴
تماس برنامه‌ریزی شده توجه‌ها را جلب کرده بود زیرا هیچ رئیس‌جمهور فعلی آمریکا از سال ۱۹۷۹ به طور مستقیم با رهبر تایوان صحبت نکرده است.
🔴
ترامپ قبلاً گفته بود که قصد دارد پیش از اتخاذ تصمیم درباره بسته تسلیحاتی با لای صحبت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123617" target="_blank">📅 10:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123616">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD8SkFqQkaaPI81iElY4Trn5IuS_WVuOQYFN6v4GPmx2mkUhgaIgS3oe6bGypP0EMvbKjnsj28E-6gMdpplyfhJKfeU1cOdvkk73z9DxZaeO2XHDSsWLS73GkUppL7TcRve7W5O6bx0Viwfp7B2D5RIXxIuQ2hbO6x-gwg92esNcnWdYTncsq3VxLOBJU7rYhJHJ9Iv3xixerF0SN1oC8NrOJ1S8zcwzZte3fA0Wn-i-JyKMWO9GNGJ8fg9cw1bYQlN5XZX9nisUKt4V1hsJBG5xYCzGBw4nIjiESb9O3MEDz4a7O9FtcdFq_pADbr7fPSux9mzo1TlJU7ZUyIAbmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل یک وانت را در بزرگراه حبوش - دیر الزهرانی، جنوب لبنان هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/123616" target="_blank">📅 10:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123615">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK39WVVjf3A9Wcn04iDHiokdJUk5uHLocNQpwkACS9inDwHom_cn7c6iWtNJtWp3rGlwA58EAuetS_hs9tcv5Szy1-yY7eZ92-KxPsaJlyU5V2FCulNEPW3PlMlg9VVwc7_4lO1DKLIVcK6LK2xERYh089s4JfkwLQeMd4C0_m26Hi5nizAzCkAZo_hABSOMioTC6zqNO-3Sm_ujUHkhlUJ5vRwgHKq5rHW1XmlTDxgkD5lPgzd9UjHYgjK3Y0t8LKFNu-FBwpApQp4lzmZ-0iB-OZNMf7rSmWC-gMf-wtrtZ4-UT9xFywpWEXHnvQhjgiPGE224g-tMDxnZCKIQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: پنج پرسنل نظامی آمریکایی و پیمانکار پس از آنکه آوار ناشی از موشک بالستیک فاتح-۱۱۰ ایران که رهگیری شده بود، پایگاه هوایی علی الصالح کویت را هدف قرار داد، مجروح شدند. یک پهپاد MQ-9A ریپر نابود شد و دیگری آسیب دید. جراحات تهدیدکننده جان نیستند؛ این حادثه پیش‌تر فاش نشده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123615" target="_blank">📅 10:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123614">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در کانال
#الونیوز
به کانال زیر مراجعه کنید
👇
📃
https://t.me/ads_alonews
📃
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123614" target="_blank">📅 10:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123613">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbkAwx6y61UBYlSsWN9oksp-UrHLyBe7aqXNQ8GZgmTAmyqF_mn4veQqISqW4k8_72DOTZ9ljjqCpTslW0ChHibzHz5RidBsUXicnoUeFSGI0cxdjWaevu2bf0lJgKKL0R1mLnVWn9zL_NMzOVRfqf6uWUBpsLkQN3UVZgCpLtGFWs763wzyHwm_LFDtUiedhHpFGf1ELTJbv5tPOUPo1GfH2Oi7iXKpggxEFYFjRIB8YkaIb1S4w6T27udJhSvBbJtTZ3qF0DsSA5ZifIRlRaj-r9qzjKCOy_ggV0LmK1SZKadFxljPKNZjrALhiMf6ByCfVgb4SkUtNO0f99nJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای وال استریت ژورنال: موج کوچکی از کشتی‌ها در تاریکی مطلق در حال عبور از تنگه هرمز هستند و بدون چراغ یا سیستم‌های ناوبری خودکار و با کمک ارتش ایالات متحده، از این آبراه خطرناک عبور می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123613" target="_blank">📅 10:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123612">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس ایران در گفتگو با ریانووستی: ایران همواره برای شرکای خود احترام ویژه‌ای قائل بوده‎ و خواهد بود.
🔴
روسیه و چین به عنوان شرکای راهبردی ایران در موضوع تردد شناورهایشان در تنگه هرمز مورد اقدام مثبت بوده و خواهند بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123612" target="_blank">📅 10:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123611">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
پزشک ترامپ: «دست دادن مکرر»، علت کبودی دست‌های رئیس‌جمهور آمریکا است
🔴
این یک اثر شایع و خوش‌خیم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123611" target="_blank">📅 09:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123610">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYqBnTrbowObkldddFrzFrBkqGlwARlD91RtCD9Bus-2RCY38Uzrhe5oE5le3Li0PlcBxf7HF9kAKyI4qbyQAHZQmjONsaFajZt-4R0IhDhGFJ901DzusatiVf8Q38J-pg8d9UAYulss1FT-48GH4paXBMJTuQX1yVCzCjd4bSjLp5oOZsIU1Bij1awZRFdVJ7NkJjRypdi7H9DJxBT2fUgjJHVVYbnKqdEOKF6uOEMO8NjT3wKUvTynK5CZvvyqIPir3lGzKJIX-85tQQyhxenNoC_DldDm38j7Q9xsAzbiUmJJxRYi6Kgn8Qb0tkBfh1EmG9VGEjrM_Cw5SjNVtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توجه‌ها به شبه‌جزیره مسندم؛ نزدیک محل عملیات نیروی دریایی آمریکا
🔴
گزارش‌ها و تصاویر منتشرشده توجه‌ها را به منطقه شبه‌جزیره مسندم در عمان جلب کرده‌اند؛ منطقه‌ای که در نزدیکی محل برخی عملیات‌های اخیر نیروی دریایی آمریکا قرار دارد.
شبه‌جزیره مسندم به دلیل موقعیت راهبردی خود در نزدیکی تنگه هرمز، یکی از مهم‌ترین نقاط ژئوپلیتیکی منطقه محسوب میشود و تحرکات نظامی در اطراف آن همواره مورد توجه رسانه‌ها و تحلیلگران قرار میگیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123610" target="_blank">📅 09:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123608">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t71FlFG5CK7W9zcZbHc-dK4i0cBh4opiCpuDwvtxcPck9UbXRimZv-pyNrENX_4mEBzd6A1Fhdki-K5c5CTRgTcxgdQBJoReheZE9rpAO0bNm-8eGbRl5_wkQnhLc9fCL3lK6YIrfMm2gM_B2SqN96RlwRA3bpmZiepBqhpR22A0HC-RQkibKjHKY5bfVTOSY5dx6zfaA1XFBu17T1PiPrXoEKlFr81iZDwekA4AQkpp5g3k9yNg3M4PuWkvlJ3fHR2Kqpcp34j6tpOdukFOB79ouwAXCp50c5aBrCjnDBiqXBgsyryx6iZb6lYfAbxUg1nPRGMOrfV4_JAuEmRw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRMJp48Osaho0LijCQMiSTZZJ40oQAJDo0YlgoHh__RxClNXw_g4Id5VaQZJ6zg5lE-qy-7QgUDLrMfhbkHEWwMV0RL30iT4yfkRlh81VpuUdk4bIYtoO_3k1-5K0fG7HdEdxzDg2l7rCWKgsHfoj4p9QNpPOW90tp-lzjT9t10JgJZv7HB1qdS_n00fGOBQDPWPbiEh_1fx9Bww1KLv6LgBTCDEX0a1ziU5KnxtwcKLj6h2jEPtrZukxZRnPLUjUYKsbIkDONIf2GPpU5XaNoR6O7ekz7qgSoXHXyrdRE08Y3VI1Cs3G9Dgpxlj5fycBzu-j1og6Msxpnlo_wnBEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیروی دریایی آمریکا: کشتی‌های تجاری از تنگه هرمز دوری کنند
🔴
فرماندهی مرکزی نیروی دریایی ایالات متحده (USNAVCENT) روز گذشته با انتشار یک بیانیه فوری دریایی، به مالکان کشتی، بهره‌برداران و دریانوردان نسبت به آنچه «عملیات نظامی خطرناک در جریان» در تنگه هرمز خوانده شده، هشدار داد.
🔴
در این بیانیه ادعا شده که ایران در تلاش برای «کنترل غیرقانونی» این آبراه استراتژیک از طریق آنچه «مین‌ریزی خطرناک و غیرقانونی» خوانده شده، است؛ اقدامی که به گفته سنتکام، کشتی‌ها و خدمه آن‌ها را در معرض خطر قرار داده است.
🔴
بر اساس این بیانیه، به تمامی دریانوردان توصیه شده است که از «طرح تفکیک تردد» در تنگه هرمز اجتناب کرده و در عوض، عبور خود را با «مرکز همکاری و راهنمایی نیروی دریایی ایالات متحده برای کشتیرانی» هماهنگ کنند.
🔴
در بخش پایانی این بیانیه، هشداری قاطع مطرح شده است مبنی بر اینکه هر شناوری که در حال انجام فعالیت‌های مین‌ریزی یا پشتیبانی از آن مشاهده شود، در چارچوب آنچه «دفاع مشروع» خوانده شده، از سوی نیروهای آمریکایی هدف قرار خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123608" target="_blank">📅 09:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123607">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: نگرانی به حقی در مورد تقویت تاریخی ارتش چین و گسترش فعالیت‌های نظامی آن در منطقه وجود دارد
🔴
یک شبکه قوی‌تر و خوداتکاءتر از متحدان آسیایی برای حفظ تعادل قدرت، ضروری است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123607" target="_blank">📅 09:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123606">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بلومبرگ
:
چین خبرنگار نیویورک تایمز را به دلیل مصاحبه با رئیس جمهور تایوان اخراج کرد
🔴
چین در حالی که پکن کمپین خود را برای منزوی کردن تایوان در عرصه جهانی تشدید می‌کند، یک روزنامه‌نگار نیویورک تایمز را به دلیل مصاحبه‌ای که این روزنامه آمریکایی با رئیس جمهور تایوان انجام داده بود، از این کشور اخراج کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123606" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123605">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: نگرانی به حقی در مورد تقویت تاریخی ارتش چین و گسترش فعالیت‌های نظامی آن در منطقه وجود دارد
🔴
یک شبکه قوی‌تر و خوداتکاءتر از متحدان آسیایی برای حفظ تعادل قدرت، ضروری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123605" target="_blank">📅 09:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123604">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سی‌ان‌ان: اسرائیلی‌ها می‌گویند ترامپ در جنگ با ایران، ما را زیر اتوبوس انداخته
🔴
نتانیاهو، کوشنر و ویتکاف را به خاطر هدایت رئیس‌جمهور آمریکا به سمت پایان دادن به درگیری‌ها، سرزنش می‌کند
🔴
اسرائیلی‌ها درک نمی‌کردند که جنگ می‌تواند به تغییر رژیم در واشنگتن منجر شود
🔴
شاید نتیجه این درگیری، روایت سیاسی نتانیاهو را پیش از انتخابات پیش رو، پیچیده کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123604" target="_blank">📅 09:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123603">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رکوردشکنی گرما در مازندران؛ دمای دشت ناز به ۴۷ درجه رسید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123603" target="_blank">📅 08:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123602">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
آسوشیتدپرس: جمهوری خواهان دولت ترامپ از توافق در حال شکل‌گیری به شدت شاکی هستن و هشدار دادن این توافق ممکنه که توان هسته ای جمهوری اسلامی رو به طور کامل نابود نکنه و دستاورد های نظامی جنگ چهل روزه رو از بین ببره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123602" target="_blank">📅 08:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123601">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
آغاز امتحانات دانش‌آموزان از امروز؛ اکثر امتحانات مجازی است
🔴
رئیس مرکز ارزشیابی آموزش‌وپرورش: سال تحصیلی امسال به‌جای ۲۹ اردیبهشت، تا ۷ خرداد ادامه یافت و از امروز ۹ خرداد، امتحانات پایه‌های اول تا دهم آغاز می‌شود.
🔴
امتحانات دوره ابتدایی غیرحضوری است و بر اساس ارزشیابی تکوینی و تشخیص معلم انجام می‌شود.
🔴
امتحانات پایه‌های هفتم تا دهم به استان‌ها تفویض اختیار شده و اکثر امتحانات مجازی برگزار می‌شود
🔴
امتحانات نهایی پایه‌های یازدهم و دوازدهم از ۲۱ تیر، به‌شرط عادی‌شدن وضعیت با اعلام مراجع ذی‌صلاح، به صورت حضوری آغاز می‌شود و احتمالاً تا چند روز آینده برنامه امتحانی این پایه‌ها نیز اعلام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123601" target="_blank">📅 08:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123600">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فارس : متن توافق که تحت قالب «تعهد در برابر تعهد» تدوین شده، در مراحل نهایی تصویب در ایران قرار دارد و هنوز تصمیم قطعی اتخاذ نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123600" target="_blank">📅 08:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123599">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
یک مقام کاخ سفید به الجزیره: ترامپ هیچ توافقی با ایران امضا نخواهد کرد، مگر اینکه برای آمریکا سودمند باشد و با خطوط قرمز او مطابقت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/123599" target="_blank">📅 08:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123598">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از مقامات آمریکایی:
ارتش آمریکا، با وجود انجام عملیات‌های جست‌وجو، تأیید نکرده است که ایران در تنگه هرمز مین کار گذاشته باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/123598" target="_blank">📅 08:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123597">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پیشنهاد کیهان برای دریافت عوارض از فیبرهای نوری در تنگه هرمز
🔴
روزنامه کیهان پیشنهاد داد از فیبرهای نوری مستقر در کف تنگه هرمز که سرمایه‌ای معادل ۱۰ تریلیون دلار را شامل می‌شود، عوارض دریافت شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/123597" target="_blank">📅 08:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123595">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIj4N3XHZA_c7NymL67lf_bQWzHM9qEt2EpmCXudfRYniWOX3emIHinm0rBb9s32Atoay0ctAGncNdl9gI7BL7_bKM53aP0s9cw3vy7ked6H2Tk-fgdpEdr84Z_j7LCIkQUaVduL05zOzUk6rBVEvIv_GYss7_lnxwwrw_5ngzrlknwiL2TyMwN4mOj9_cRtj2u-hdpqxlqhs3uxD8jh9uhBEdJc86bTbx7tVIewtht8GhhSVJfQHOqrSzOuX1fWqR5nNo7vdBuj-6X9xQrB3E5diZQ_IFWcPLrN-M9uPJ4zZq5erfSABSWflvZ66OFLWLXfqtUzkqcbhicBn4pSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6996539c8.mp4?token=uQKwlOt2G8jFaYHp9V2ImxEpwWKlayGCe-FzFeR2ls_dCdHFdp8DUDmIVBoDQibLd8lByuGi5ctxBx3sKI77aMjDJHrsf3rdbjkl3Oi-IiLV-v5q8Yota7K5Gz8ukECv_fop4TG9zKApCH2Tku-0oC78HtRxcL-RqmOKfIlumIB-2hYGK0UtrXf5lQnrTaY4E1WZ1hGETF4WPwOoyPXI0-8n2pcmsdDEep062qV3SYzpimDUVCxmKBwZooNSgVi5eBdZ-z4Z4Wssef8UrqMWsYrA83ffXNi8Is7x2vxhpdzUDjx-pbga7b4stUfxbWD6hwRc46kRtx1EEx1QL4Ox3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6996539c8.mp4?token=uQKwlOt2G8jFaYHp9V2ImxEpwWKlayGCe-FzFeR2ls_dCdHFdp8DUDmIVBoDQibLd8lByuGi5ctxBx3sKI77aMjDJHrsf3rdbjkl3Oi-IiLV-v5q8Yota7K5Gz8ukECv_fop4TG9zKApCH2Tku-0oC78HtRxcL-RqmOKfIlumIB-2hYGK0UtrXf5lQnrTaY4E1WZ1hGETF4WPwOoyPXI0-8n2pcmsdDEep062qV3SYzpimDUVCxmKBwZooNSgVi5eBdZ-z4Z4Wssef8UrqMWsYrA83ffXNi8Is7x2vxhpdzUDjx-pbga7b4stUfxbWD6hwRc46kRtx1EEx1QL4Ox3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیل حملات هوایی به ارتفاعات جبل علی الطاهر در جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/123595" target="_blank">📅 08:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123594">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QumMHWpgjJDXvKz6WkfqOgQxp_8-DOAo1KwxsyeaGChnu_ytpz50BdofO-ocDdkt1BzXIniBTt7fPlWzyrCEy5Ntp26YqiUpgrfA8VE6JWMVVYFNwD5fYVsi71UpJXYImSu0sJSz_dAw_HLViwGqfcrWene1FCx_eVW9KLg0juMfj-S7kCmD3Zd3Fh9kClUm34jwKHwmRFvO4Utx4Df2F1e01wo6lCMSOFoyD-PcGzrl_kFb9gQQ_M9i2xZa89y4TVhYbtx1rLyeeS19XVUYJ3MJvHOazqHQ_OzvqvpqCMizNYIjmbEmZa61GGGQQRMRg38IesHwJDQe-lPfYHKbLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه پاکستان: ابداً قرار نیست اسرائیل را به رسمیت بشناسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/123594" target="_blank">📅 07:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123592">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SXQV8qPgHDcBcHZA03uVtmVvF_2jjaN9K9Ctv5IF_PgH7qPYBRCAZixvc5h9Iq0SQUDOBYldWHiIgHMPed-3SN6OhfeQLVvABEDBwFXUt6Irg6S2W0gzEm59umJj75NlPaLkU18CelGaU1HM-ah2X033Dz08Dtvw8UaAjQrPWWRrdO1x0GjplwfVj3WEC93SHUbkf6omgfAdWvixTIXBp6ECjzZBG1QZ17HyeakWbjHKIxdr7A6Nw6hSUUxD4jfy86W7jE3ZUP2Xd8mh1bsGh7_p-hbID-3S8nUcau__sDH8VvMLAoHRXsA_4Ec_aHvB35nVIcajd10sCcgrrXFlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q95Yd8yPx4xyeJ3l8Hq7gZ_TYYGzgqQFAfnLH23dkmb1idGf5jq3PaIBGCEYj_Xj9uLbN443hcvDVBxW8zC0NDztSW4Udx4E-W5h9FD0qUlvn0WNJgeo4KTTVJ2nGmMD6JeM7MZb7gsdunfOi-pMMBqmzrgMVGSDirFMYb9M1dCT850Ji9FLZvXLzF4QfATXOqEIlz9y6EFV75Q3RlIL0bC_imAytEmqyVB-UhSCH_D55siItE4IOOHrtDA6LxWATfD8_DLJSbl_wl8W4eeyotR3LCyvWISo6KvEIlMkNSOofU5dGnPEq7K7t1lLBuJgiJtxw8KAAiI7kj9GJeCenQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فرماندهی مرکزی نیروی دریایی ایالات متحده به دریانوردان و پرسنل نیروی هوایی هشدار داده است که سنتکام در تنگه هرمز، در شمال "شبه جزیره مسندم" عمان که در وسط تنگه واقع شده است، عملیات نظامی انجام خواهد داد.
🔴
فرماندهی مرکزی نیروی دریایی ایالات متحده به دریانوردان توصیه کرده است که هنگام عبور از تنگه هرمز با ایالات متحده همکاری کنند.
فرماندهی مرکزی نیروی دریایی ایالات متحده
همچنین اعلام کرده است که هر شناوری که در حال انجام یا حمایت از فعالیت‌های مین‌گذاری دیده شود، توسط ایالات متحده هدف قرار خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/123592" target="_blank">📅 07:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NncaJ1LvEoaYpEgHE7hdDy9tKBDWsC79EL6THsQx7aCn0V9JYFJeJGWqmZ8SQMeqVn94jopGnN8DRT_lKu0AwXwF5CLWmmELlcKLdo0oz_A7habaTLiQRKr6YgV0QLhgOr09Aqrfg93KIwVlK6Qe41G4PLI18l1m2XmesdjWDLTUekZA42ayNfpdh3nC6DGXSy_W780BSWxRXforuK_BFx0oLIpYAshJMBlXGFdbjaqBejs1Y7VBAppygkgQ6XkW2ZB_cORxkxTwoVlL22do0itY1aTe8P47CxdbkOYxAysZOuEFd8U4wxmUvWvllQV_UD1ZtJNasmqATSMVWdU1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
همراه با ساب + حجم مصرفی
برای استفاده طولانی‌تر و بهینه‌تر
😍
@NetAazaadBot
@NetAazaadBot
⚡️
سرعت واقعی بدون افت
🛡
اتصال پایدار و بدون قطعی
🚀
مناسب گیم، دانلود و استفاده روزانه
@NetAazaadBot
@NetAazaadBot
💎
گیگی فقط 19T
📩
برای خرید استارت بزن و سریع وصل شو
🚀</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/123591" target="_blank">📅 01:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N84jVPdvkwmHXaLcY-vGetTLcYC18vmKpulUtsuCTSl50FEHBKMh0SPRtsJOF7tGD5IUYlWCZEFp2Y8Ho-Zimr_zF1Qg72fJoPPZpEWwKCJrzJ9appyzXmOTWOLBtFLr34X8ROGEQ2y2d4Fz8Qn_q-bi73fEmDSjHRdfg_1KXdr8IMM5z39XUxJ1fyFeEu390OGQU1ctj1UqHiqdmQw9ngEu2ZjyT-2oWNkWzfEhuk1JpxgyWb8y1JL6Lp2EqHv5292a1cfxfzNf_x6hAF6UyOEzxQTIzPMq2bT_-1NC-uL5erh7GImxPrvFDzi0v-7eTWz81UwCBhhOVBYWYusDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شورای امنیت سازمان ملل متحد در گزارشی تازه از افزایش خشونت‌های جنسی، تجاوز گروهی، شکنجه و رفتارهای تحقیر‌آمیز علیه زنان و دختران در افغانستان پرده برداشت و مقام‌ها و نیروهای وابسته به طالبان را مسئول بخش عمده این موارد دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/123590" target="_blank">📅 01:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN9fngDrhm8MPw-omzRrOH3xe-gl88gPlkRNr3JliMafGonXN1SROjEAdLfB050GUam4L8VtgDU5XudLX9nED_PVJYgEfPP2ZR0DkT6oEXaisDFQ1zzZQsI4s39r70_1uB2fE14BAlSYE7fi4ZHeeaAzsFwxWoKp4I5mPgex4qTOPfZrSMhomqWAd__sKZZ-bTPF8zvpkQf8_kYIzH9hZfbD0AzqdkrFV8OEl91dbhHrVKUP8grmHdn0LqnHUo9PbTcT-3ZCM5iuksYLdqrxVflQK8qrEfwI1q0825jaB3PMNkhtaXn_UpqFY8Q8dvG3-ILBWjBtcMvbd3l1alTIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت مردم ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/123589" target="_blank">📅 01:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYXZ_0lktkx_0nSWCoZyWliX2kp0S2Vvnsh4Mw4-yhug91AiryinGG4sjBvf_4vA3KKbc4iLDf9vcN5xvRjNH1WAtZIyQjC5AD32x8tiEG5CQ9kAs1dVd2_LoovlAEJG6KhlgKWKuYtv4IUojnRa7pJWxql-tMomsd9icTgTfgsfXvZx_RdCPy9e6cubpnPZWFL-GAyBJC32UuSJlyYB82hawRbpLtFktkUUfnTP1evu8XMdViuPL4YCptLBtN-MW5-EhkTaIRoGltKePN1XamzuAYKwxSRCss8Unvylb1rlXwuyc_wqSi80RsriIlxx4MkZ2Ej_JSlvVjsaieX19w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فردی که در تصویر می‌بینید به گزارش روزنامه فایننشیال تایمز مالک شبکه ایران اینترنشنال است!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/123588" target="_blank">📅 01:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123587">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezRjtopcbI10z4mmKxvaiIzmmfxXUEOV_HJ8ueRC72CU0GIEyvcNf_nPeloTF70hqWPkdEFaogFUjeMn_8Pm0ZTUI1UwZnOIcDta7KlCvET2pA1ttynhJbQJlEWA_x5LdVRHQLMw7QgJ5GNiQO6n9oHlTlyVc2j8Iw49YHpw_flxTs2GiSGGWGQ0BSx745ufA1BDHk91FHnantiztUED9soR0VshB7fYOpekHp2Q9m9114wserxD0y2n6-BD-FkJuk0WkivR4NMzU25la3ukxogM_XmDJFnIBmJYZTUIoD3-P0N3v0CeweK06COzMXSeG57XMkamBcuJltFSSiI41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره:
یک منبع رسمی ایرانی همین الان به من گفت: با تیمی که هیچ چارچوب حرفه‌ای یا اخلاقی ثابتی ندارد، دمدمی مزاج است و مدام خواسته‌هایش را تغییر می‌دهد، نمی‌توان گفت که هیچ چیز «نهایی» شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/123587" target="_blank">📅 00:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123586">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مدیرعامل جی‌پی‌مورگان:
داشتن سلاح هسته‌ای توسط ایران، میتواند بزرگ‌ترین تهدیدی باشد که بشریت در طول تاریخ با آن مواجه شده باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/123586" target="_blank">📅 00:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نیویورک پست: ۶ میلیارد دلار از وجوه نگهداری شده در قطر از جمله آخرین نکات مبهم در توافق صلح با ایران است
🔴
این وجوه مستقیماً به ایران منتقل نخواهد شد، بلکه برای خرید مواد غذایی و لوازم پزشکی استفاده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/123585" target="_blank">📅 00:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9Xk2FpO4rdWp-ebRZi44dFQd3i2lkmFlpqwi5iz4wPr2jQHDQ0cPwm3QX9f8FSSvkCAx8esU7HvnecOxFSCP-nBDVUsNjE_H2uAhBTSKozwqIs8OoPH2-_ugmLS7-Fd6zMfiSM6NuJJlqxpp0tC4uZPUZHaVdXvAQt-WZ1W6-B8haBi5xevXDTYc7ryifLNYhOr4bMAZJNe_cAeQoxn1uxTnejJ_G15Zg4ZExjtNn5SM7ptq9V7LRssmfGsONOPea_B0tI9F6DQ_4xkv82EPYBKPQe9DPVduxmOJP4zJGwjt3RwSiz215yGIlHlT79MIahS7hRMt_rmSJcLlu9Yxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از داماد ۱۷ ساله و عروس ۱۶ ساله در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/123584" target="_blank">📅 00:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123583">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0NhTSxTOpXRd8G2Kh_duGsxMBUdLueL6vhaMExmUsp-G2tk9kEyp1y8rchhVIyL2cPxkp-jMghnjGhbIzLSNpWlyRrb8hV7cayc0NkPKbm6q3I1VMSGndQlPjPdCXv6b6uTvXg0sVz20r--AsJ4nsyxDRimSOTpXVB3f0RVDbCftFFD_vsY37gZ5-04Ps1QW21kk8CQFE9tAxIK6YCFWwDvnmi36sF2KkmwAXz5JI_-PfO7TCrvSIyr1g4OAKTrduML9-yPlMFooz02-ODD7-B_inIgsZgpQIgbTtlzbb_tlR1uFMZb5ZXpz_cal33mOt6v1v3_Pq0VtqpjuoNA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: آمریکا تاب‌ مقاومت جلوی قدرت ما رو نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/123583" target="_blank">📅 00:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123582">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2jLDpotnFwuUZoogU1c_fwxcGdm0IW46IDGzUWt2vVflNG93PjcQsc-ZgmJbQpNnJlz0_GiOOBS6FK4odBS32U9KuPFOJ79tbJbN3FIQcXnmps2mqOnpv76ZG4ny9cq2kibtS3L4rKcHHHqFQ9fFHtiAL1miARsz4aEnxu6kSQFtRBJ4ziCCucvnY3yEch6HEw_r1nZkXeTGwC5E7HHceEHc_64eDasInP9POYlJRGmuDQ77EAU9OTxrUlFTkC3orHM4pRVppjFwgM47qzQF_4VS-Tnr60OUgwv52wlL5o5H8KDRttzWiCCNZ6BWPen5Tl9oUFIlnMy3Iu_vi4BSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فردی که در تصویر می‌بینید به گزارش روزنامه فایننشیال تایمز مالک شبکه ایران اینترنشنال است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/123582" target="_blank">📅 00:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123581">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری/وزیر خزانه داری آمریکا درباره رفع تحریم‌های ایران
🔴
به گزارش الجزیره،  وزیر خزانه‌داری آمریکا مدعی شد که تحریم‌های ایران به تدریج لغو خواهد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/123581" target="_blank">📅 23:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123580">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: محاصره اعمال‌شده بر بنادر ایران به‌تدریج برداشته خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/123580" target="_blank">📅 23:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123579">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8beb1cabba.mp4?token=qBB3aRu_BJej3zi5Vtpk9ovKx63TBAYOsQ1ipnyVHzRE_c7Tuf2EY3WOOXW91BhrYhtXYgxkkUePcOnnY0t_24h3mMxKKjZTILVnmILQSDzIefx-g2WJWbwtJYj_V-QwighaWT_U0Pv-5OfPzIf2SgIxLoz9kbceluMdNY7lp4K5_V4jmU_tlPbQd3N2bYlac5vSZpAhB1yxb2GhHmmxR2CjAedVrWnX2wQvlyMg2Z94oF1VPfL50-5sqho2Qk2GRnNxGQAS1OFN0hdiwITo5Pb4lD5l3C-rcHEW8GpWUzFqhK3Fi1QuHERIP1GY5o84h4kl33NIFeXaU4E1IfSkWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8beb1cabba.mp4?token=qBB3aRu_BJej3zi5Vtpk9ovKx63TBAYOsQ1ipnyVHzRE_c7Tuf2EY3WOOXW91BhrYhtXYgxkkUePcOnnY0t_24h3mMxKKjZTILVnmILQSDzIefx-g2WJWbwtJYj_V-QwighaWT_U0Pv-5OfPzIf2SgIxLoz9kbceluMdNY7lp4K5_V4jmU_tlPbQd3N2bYlac5vSZpAhB1yxb2GhHmmxR2CjAedVrWnX2wQvlyMg2Z94oF1VPfL50-5sqho2Qk2GRnNxGQAS1OFN0hdiwITo5Pb4lD5l3C-rcHEW8GpWUzFqhK3Fi1QuHERIP1GY5o84h4kl33NIFeXaU4E1IfSkWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین علایی:
سه روز قبل از جنگ ۴۰ روزه به شمخانی گفتم: آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می کنند؛ او گفت: نمی‌توانند! گفتم چرا نمی توانند. گفت نمی توانند پیداش کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/123579" target="_blank">📅 23:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123578">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz7brSAkMMurV62sSX6HCS5Hr_GPrKfno9BPcl4Gsv-_Y100bm4nWYQLf01nH3Xq7FHjQ8HMMGwKijEh4bvvYrLUsXAUeZAw5z7-Au0dNFKMyKZfD0Lf7qZn2-GS7L-pQwrwInKR2oFtxWUV2LWuwUog6l0Xrv7tVOkrauiX0y7rZVAHeOJ3ZT6Pr-0AG0UqViTvimSa0kceH8MhGH9t9FASOu0PVZz2vIeeI5vUvOQhIMhexquSbhbpmURPCcdarRjh-3CxGkJeK72q1zhFWM4xQPJaV2ZH3gw3yE71g_sL0EKUCQ02sHuNwPEF6eznXtGZWS-q7h7utrlPpSQ1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/123578" target="_blank">📅 23:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123577">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1defb8b924.mp4?token=ejNp-cEY-_Dl4JYe_gyaRDmWExkevnNd9JyGPZxpO6TfIEzyTt0azKbCIChKEBA7h2xXwK90-dgjzE93-J_BJVEufWmjOo6aotx4zssVCeytoYaMhN-7ozg0Vo7Wcz-ZHtjffJIRZU1bxQzhxtEPOnDHWUlmuN9NOi_JQf14jZ4x5OHDscGhGskVBnQz8bwUVL8mgU7AVFlbwbk25PU3SDF2qXHznoZrwACrJk6kSQuvG5gwEfHoFvBSTXkGQiEyreo-2Ec6qJcBEwi58ZKGsTY5kCbWmwq9c--OBddfnD0JeqBmyH6_XMtFWOlzKQMne9D3QF0gkFIC7sBIgiW4l1BoIKmWc1YDJmrdD-AMPBoWMvN08LbGNso8T3WtJdVrwc5fMu7M3gkRgAk7aoES_QsFGtrIuLDF8Y4wcv6iUL_rtY7hDQxWrvR7ZB-ussPbFD2gvAojO4ptDUT8gEbWrHSd9295ogALns_0CRH0zn0iEev9cRhXv395Ob2sHOfiIUNpJk-mMlA8ckjndKIDhsAE9754pZ6ME_LjjQjvzo7jNAbRx8V4BtD_XUn8N4HJoErFj_AoKmqEXb_fq7kqOhgx8OwvVW7Hr4oo6fzcfGo_dznCgzsD-tdHK5ArNzJhGR0myBtGSiESlEPrdst7gWqsTxOxvHmZeQui_yYIQbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1defb8b924.mp4?token=ejNp-cEY-_Dl4JYe_gyaRDmWExkevnNd9JyGPZxpO6TfIEzyTt0azKbCIChKEBA7h2xXwK90-dgjzE93-J_BJVEufWmjOo6aotx4zssVCeytoYaMhN-7ozg0Vo7Wcz-ZHtjffJIRZU1bxQzhxtEPOnDHWUlmuN9NOi_JQf14jZ4x5OHDscGhGskVBnQz8bwUVL8mgU7AVFlbwbk25PU3SDF2qXHznoZrwACrJk6kSQuvG5gwEfHoFvBSTXkGQiEyreo-2Ec6qJcBEwi58ZKGsTY5kCbWmwq9c--OBddfnD0JeqBmyH6_XMtFWOlzKQMne9D3QF0gkFIC7sBIgiW4l1BoIKmWc1YDJmrdD-AMPBoWMvN08LbGNso8T3WtJdVrwc5fMu7M3gkRgAk7aoES_QsFGtrIuLDF8Y4wcv6iUL_rtY7hDQxWrvR7ZB-ussPbFD2gvAojO4ptDUT8gEbWrHSd9295ogALns_0CRH0zn0iEev9cRhXv395Ob2sHOfiIUNpJk-mMlA8ckjndKIDhsAE9754pZ6ME_LjjQjvzo7jNAbRx8V4BtD_XUn8N4HJoErFj_AoKmqEXb_fq7kqOhgx8OwvVW7Hr4oo6fzcfGo_dznCgzsD-tdHK5ArNzJhGR0myBtGSiESlEPrdst7gWqsTxOxvHmZeQui_yYIQbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین ماشین حاشیه ساز لکسوس Lx700H با قیمت ۱۱۰ میلیارد تومانی پلاک ملی شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/123577" target="_blank">📅 23:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123576">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0acce2b1.mp4?token=fjDnArTVrUcZ1BbU0eR4UTp5sNzL7a4jtbbjRteBbOgY4ooelx_1u7kqrRqNofCpYK1ygXfHv8K9Wnj1iEDtcSGYUjSttdSxD2P7Nm5id6Ett0Sjp8xjzftms18L9wKtZYOWp_HoLblNCWaobfjzhm5XuJdCfSHtxVHFDkNq9284pdtUHCxyQW58v4VyQdRnvu6cDh8eBcLz3FdMaa7QU4JX2oJkXessw7OqezRceAkFnhDEePIXGMz9_BqwAcAxcmr5kei36WSakVqPn5Q5P9iFWDU18F2jL8fDUE8_LSp9fTp1ovfxcVuFcC5YcAPR4iNlq6JtXS8riVdugbatyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0acce2b1.mp4?token=fjDnArTVrUcZ1BbU0eR4UTp5sNzL7a4jtbbjRteBbOgY4ooelx_1u7kqrRqNofCpYK1ygXfHv8K9Wnj1iEDtcSGYUjSttdSxD2P7Nm5id6Ett0Sjp8xjzftms18L9wKtZYOWp_HoLblNCWaobfjzhm5XuJdCfSHtxVHFDkNq9284pdtUHCxyQW58v4VyQdRnvu6cDh8eBcLz3FdMaa7QU4JX2oJkXessw7OqezRceAkFnhDEePIXGMz9_BqwAcAxcmr5kei36WSakVqPn5Q5P9iFWDU18F2jL8fDUE8_LSp9fTp1ovfxcVuFcC5YcAPR4iNlq6JtXS8riVdugbatyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رضا پهلوی: کشور های جهانی به خاطر چشم‌های زیبای من یا شما این کار را نمی‌کنند، آنها این کار را انجام می‌دهند چون به نفع منافع شان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/123576" target="_blank">📅 23:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123575">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: هرگونه گمانه‌زنی درباره پیوستن پاکستان به طرح سازش [پیمان ابراهیم] با اسرائیل را قویا رد می‌کنیم
🔴
تا زمانی که سرزمین فلسطین مطابق مرزهای قبل از ۱۹۶۷ به پایتختی قدس شریف به رسمیت شناخته نشود، هیچ انعطاف‌پذیری در موضع ما وجود نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/123575" target="_blank">📅 23:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123574">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: یک میلیارد دلار از دارایی‌های رمزارز ایران را مصادره کردیم!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/123574" target="_blank">📅 23:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123573">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری/وزیر خزانه داری آمریکا درباره رفع تحریم‌های ایران
🔴
به گزارش الجزیره،  وزیر خزانه‌داری آمریکا مدعی شد که تحریم‌های ایران به تدریج لغو خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/123573" target="_blank">📅 23:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123572">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfAonbBqiu0b7h1DcL3PNKmAEcB88qfCf6ZNstPk7BQx7d25uKiyJYGohLIs-YvpaceVBIctnlQsuAJVzsNkaX1uzc1zi51_CYFL5chvpQHDIGq5L5IyBxuCVVeN-5MkEItm8RUJ2eyFVK4WXsyjVq7UzcFoO2xyaef6yO-3FUI7bUGG7wJWguoKYwyLim60iJfmRPGNFjp7Ab9xao5u4Irt8k08sszAos-DfQOhbSRW05E3JBae2f1TsPMcjgrvM0kqGAliy1IQuhhAbjfTGe2tyHGju9G7EXt-Zjkygc2KpHfhjSKkpHdQJFKifIgk0LJ1oL7DKg-cIF0HuZrMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز اعلام کرد: صادرات نفت و فرآورده‌های نفتی ایران تداوم دارد و امروز یک ابرنفتکش دو میلیون بشکه نفت خام ایران را بارگیری کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/123572" target="_blank">📅 23:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123571">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: یک میلیارد دلار از دارایی‌های رمزارز ایران را مصادره کردیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/123571" target="_blank">📅 23:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123570">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کان اسرائیل: نتانیاهو خواستار از سرگیری حملات به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/123570" target="_blank">📅 23:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123569">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
بسنت وزیر خزانه داری آمریکا:  احتمالاً تورم ایران بیش از ۲۰۰٪ است.
🔴
ما فکر می‌کنیم ایران ماهانه ۴۰۰ تا ۵۰۰ میلیون دلار سرقت می‌کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/123569" target="_blank">📅 22:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123568">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uT9xwaaoDCC0agxBrCdQtGzLHY4YfEpOP00IqhUKw5ODgK-xv8-wKv-X34wpnvNztYDFp_f74MmlZ4-zGTXIOOT2HsrVX8NLFEUxUnYGm1RFxtXxWiqlIpOIWK3fZVi2vzL49ONv7QIawZinCdj14-vm75Q1bL2bP0Dnjm5DSVBvxS_DdNVFHzQRvFQhXECrPzHz5aDFvwZ6Xh0NFQsfYfOaw_lvYGPERq9A_wby0-d6vN8P1OCeXpq3q05uwq0S_BBigei8Sqf0QIDlx8KQteMjU1MhKgsHKugtwfNmyCx1ASN566ay0mWuOyWvJ-b_lJGuqlMIC7ROOBghpyKftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنتاگون در حال جذب صدها عضو نیروهای مسلح برای حضور در رویداد UFC برنامه‌ریزی‌شده توسط رئیس‌جمهور ترامپ در کاخ سفید در ۱۴ ژوئن است، گزارش واشنگتن پست.
🔴
بر اساس یادداشت‌های داخلی که واشنگتن پست بررسی کرده است، نیروهای انتخاب‌شده برای حضور به عنوان تماشاگر با یونیفرم باید هزینه‌های سفر و اقامت خود را بپردازند، استانداردهای فعلی آمادگی جسمانی نظامی — از جمله الزامات قد به کمر — را رعایت کنند و یونیفرم رسمی بپوشند.
🔴
مقامات به دنبال جذب پرسنل درجه‌دار جوان و افسران جوان برای حضور هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/123568" target="_blank">📅 22:44 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
