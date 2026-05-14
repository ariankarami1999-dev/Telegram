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
<img src="https://cdn4.telesco.pe/file/kDu9ufzvlI3rt3dje5IZJax-ydP6l6mp0esL0ePGkDNzkoFK4zmFaR31mEXu9qKFRbj4_3Sr9_QJgPumWmqv4VSfZRnwGz3ITnyieun4fo0ftnl7AtBs2OcjmhbuBIngYwzD4wAIOS13sG84XWQtp6ADwqY3N1PTPXEoytnjxJHRnXUWHButlkg1kM62vibdP6rg58B1mKc_83soObx8TttZYzW18PY1y62NcC4WHVKON3YA13fJKWcLQlwbxU0mtbbLOkoXABco-vB3EWj1NtWD67kxnUjm9lIq2usaxDulcMCY127On5AxWmnDkqYa46JVu0febvG6yauABw4ohQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 211K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 14:56:46</div>
<hr>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCdyUQ1YBOFLA4N6dfEO7SW_fZuWFcConm1oTJ46BUMO__yHA_Sf1oqLUDQtcW8EiAWnwIGdcZqy70R4-GbWMQLCbi8Yp03Ykwu0hMCqRLr1HfpbsVWdOwrpb4aqF488FpAnDnzJx9FHxgbVjlF8p4h9t9aBKVYW1kBowW0HCwFp1RVHhiCPKb2-mMC9uNHhy7EHEU9M3Wnboijaua3_bBj-ZMMzbmDerxt0fMOP3LZLcyR6mqsohIBexhtODx7X_lKbicoAnUvOaHzcAsa-4hj1S9Y-emSkcuc9yCgSnVMs9F10t-F1cGldykqfvZ5rMt2OACsWE0_weIzSc1OzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj-veqmFkxbU7tgEThin7mBozcSogSB3LQXkTJ5icqIiQaMQINDwSOdm-tyEkAmGSPBct-bgcDS_41aWy4Z1gFyjMAe9w3JtIZfEpiaOafYeA79Goibog1MYKJUOoZrVLGgo2ivjzoFaFN08q8-l0c508p4HRfqovj9KX1BlG8HfzJo2t84zQt01qatm6H203C-5RXPcmKLHYNT5Ileo6bKnqbrNqwPw8OSuzxOURv3FPYKMu6dQ-M3D7tsv8i__t9roAhIEVQ-zNdQgnxA-xEWiMpX2f-o6IgKXPIWb-g0hPsE1xUjHXIdfC3S39KgVZu_HsDy69Oq-vURNY4uHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFIapQtA5GAP-KNKA4Evm1J4iZD8mtpog9zGNtdQ1NPNnsT-800yHk3S9Ez4cx5u_jaflbRXz5OS9nYbbaW1A3DZAtkZwvWaiM8cPV0ncrfx235rg9P872fWzZsXqaYiqYzb30lrO_6r9U1WtGzVqKG3NBLAG1aeS-TspTYH9TqZmQZ-x2I0D0nuZTQZYNQ-k6uUGfnpGuoxmq2WbeGyGU6s7PMhBn8KqQGpn6jZSAQQ30ENyc6v0W3l9YhIjOdDIiFuhobFjjTa5RANvXBjQRifRoU08v035XNek5GVJweuGRQqO4oAUj0k1g5MoF5BiulfDIeDmPiMWIZyJghoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThjbyQeNHqMu79xJR43-BnU0P8nGmZ2EVQOmWeUROYnDnc9anhIqmwYY07A4Xv-YHrbnwOnQIc195FTdNAerCJ0PDDvpU5TcVekW8UP7Ph_LczDCsWk6IUqll1dTMAmLglcr7L2YGu0hiOqZ6ZbMmP4qQ89WAKXvN85qh6-6CeBM6C9JrE1nAOStakbH3VMUXqiowHcQ925FeiqVp_ZMlouj2ioHi60UsJoOy1EGsqD4ZN8neXorK-YtuwjHaA1hP4h56xTnqq6QLskj37KQ4Xp2QKEb2iHhyqmpMF72I6Vc4XltHoS6-2NfLUyx_HX65JyIzHeAuRD-TorGmcP-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFSjT3XneP1bPb5dmETDnWqc63IixHhFLC9juaNCU-LmovqXwr5DtuZqav6dW0v0jIYDNcCKRwehe2n2Wp6_-h4qS5ttYquc9_JGI1h1VmMtdDbFH84vvqPsfgvpw1xrai0WVwH_h843-cemfbyEZDrIOgIajPikDBul_YYel7pS5DRqWiTZyxDXgyTSHmKq723LixhHbpzPKeD2IqtqOfbVGads1kqXsEE7BLcFW0VcVhstdSRqReOVZ3FTFRRIN9KkNZddqWjS2PjXgGdmMsG6TRDfbJtKnEt_KHN8eZI-UFs5T8zj21tG8VlhXxAFPq5_1j4eTJUdcAwadyL-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr0PnkYnw6ozYfDw-hax7ZMyYTpCWAmjudQoCTZZ234poz_rZfIU0cetvhm0ayxbtRWAcqYlokn9id-5jBRkYz4Kvbs5duEWSAw2l2gxlacP0Zk2VA2RU6x85-ZxoveAl3QNsZDLR_YKTFaRKvMqkM51i65opFxOMbe9GN2qF2qpPhJntB-RALhybappT94P4EjcIForNvaX8L_2k_hkbmdYozgZZeRceruC3-ONhTvfiwTQRAjzApE7Ycz6DFllZL82Dbs_L49JLPcRbtSzXPVJo9DHmZVQlk8H-zrpHqp1EjT6t0MPvBQk6ORb6LZ_aZZjbyCsPyYEsANxrmtFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGUYJYCeg01_GrUdQ2c5nCK9HvC-pDiORrpwvhatRkzu4zwz3u6JZxXkQtHYwKOSlKcKPKXuXDWbZVBa8TLdu7AYOj_L0rxCapOY7aOHQjcVw8HlI1ro44Os2fVJ86ony9-6KFeUn_QNOXxI_a2SFjxZeS2MEvcFdbpj26M9UYz2yxREerAR-82HLhVN5QcGt1vPDe95HWS5Xe0v8SYk_kHH1oufabHXP0wqR60v3yjC124X8SIZkVlxsQlvtii3APihfJWP2mKPVu1Q6IyGa9y_O1NdCRWph4oUOfnrBqzqtj8Yzwo1j-84xt196Wr85QLzP4wWQ6_mg93UwwoTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKlcARNib46iBTfCqticAV5QV_CBxZjumzVuQ2t1KjZAn8bgcAx98Tf_oFBU7-88rVoabYBeKqShj-mjlSnwdFajGq6ud0G5MXOa-ds9X6LibCrTYJyvI9rToIoWbi0Wt4Y6fugB2ckk1m6pFCYP7JQUCDHmZE80iXRditjW6s0n3-wvCqG3U5wzy_z_kl4vgNZJLquOoHOEXs2y33hGz-VILTuSP104a9ZfUNuSRz3xo8HjZEAgYlhvYE0rtu9cSVejESjGi9-ayRVP6pwGscLqPj3Tj9BIVemrxUYbOvgdhZWaDapA0yGxfS99NEuzQShu6437n0c6iwdpq8rzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=YbZciyXD_KI3AnlF1D9ZCd9P0G4nYi6YzUV8n6dx1cNqTQmCcyKF9BNQVd26M5eIUtTjS9w3fwbJ8TrcztgdYMck0zH1Jx0zqfSohUybTZn_XadSRgUj7tUCAHnm8kRUT7hw4zHOaWSQawnKe5FbYrVgkG0vyooa9V2y91pYSczsXFMaX0_3a-Jyy0jiqATZ-5hgq4SUCtLq1Q3llgv2RPo3kEWbO9JOW6IaS32u7iGJDQGkZipXGIRati_96HdMwyxyh8vo3EWPyl24RUN36hpAEOS9D36BA0Xk4F1GlP5cobTegNcBZgySPk2dVDP_Sp4Ypx0XrKYCxlfnzUbNPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=YbZciyXD_KI3AnlF1D9ZCd9P0G4nYi6YzUV8n6dx1cNqTQmCcyKF9BNQVd26M5eIUtTjS9w3fwbJ8TrcztgdYMck0zH1Jx0zqfSohUybTZn_XadSRgUj7tUCAHnm8kRUT7hw4zHOaWSQawnKe5FbYrVgkG0vyooa9V2y91pYSczsXFMaX0_3a-Jyy0jiqATZ-5hgq4SUCtLq1Q3llgv2RPo3kEWbO9JOW6IaS32u7iGJDQGkZipXGIRati_96HdMwyxyh8vo3EWPyl24RUN36hpAEOS9D36BA0Xk4F1GlP5cobTegNcBZgySPk2dVDP_Sp4Ypx0XrKYCxlfnzUbNPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvP8q5LYLh3yqr6UqXHauWPrQ5dWvoX2yL7VGc17TecPjC3yQBq5ue6uDAGbZgG8N2phG2OnKJb3RfHevkNlWokeELtoozFo_1dLe9NTts5RpwUEwDF8y326-j9okYI8Q1B-4Qnmyp7kF77tP2HK8EjmIy5gw2vsK_KwYmWQtgDCbAQ4JBR2whyAd3PZHxsWse3rPUsEVsDSwyFINu463uPdPT3zNRVDDD1OoWfxFwMblOLbAlX0dhh7T6GLSE2dyahk3jBdUlI0m5OfftpJub-Bly2MNNHOoV3NlwM1S_RHA1JDlpMlovEorLXh4epxHzRYIv4nWhV5-_hKcGvXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv4MxdOj2Zj2CCoIwW0UayljEpy1l_FIzkgvF1m8NMP9o2vWdoUfNMzqy3LW1LmK4CuvVBRh7vhJIQLM2tCfrXi4adUSEp_Mxcu6XmHkB5iojTn84tL--oxZHvrKUQ_8bo6ktiSAFYCDQsioPVGkqzUG-BfTqCaBmyUB0XFsW9xPSQw7oxLx3OJ3jHUzoWtovT8WC1BFlvfAItZOBblW20gGuY2j6nc0M8hU3BCtKTLrmEFSppntYUAYwrSpnkHTum8v7Jg3ufn1UZdn8GJi5UGhmHJkh5t9jcEFw53wa20JBs_G-bJYs2yylSW6RmZjXlNuZR55pCMJuO0g_DZPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=vrRSd5peITwrJyZCZhy02E7AwYNz0h1zwoQFLapDroSXz4rO-lrLJPz4Agrmo7hQTOUWhO1jsYIej1yG_K5oOITin_UlrCh2z0sMy57s3WTGkmINZmHf_ZXKcvj3h3eCkwgwiEFMNoXtfgv8-NFbW6ENF9Hng6gP88D6hAb70nTqC07dit9SiLBOnbgvtbMffdONkx4uBzaKCI2snTSkHZVggubD4mIWwVEJXSXvijSIjxlm9lRsdtaMOPfVKtfggQyhX4IHaVrzKSvV2VIxKJbSy3A0RJXiR1ZfrAgrrlMSKk2DEHCmRyg-jlV5VRt7Xq4xF24XWz69bt_fUYRkLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=vrRSd5peITwrJyZCZhy02E7AwYNz0h1zwoQFLapDroSXz4rO-lrLJPz4Agrmo7hQTOUWhO1jsYIej1yG_K5oOITin_UlrCh2z0sMy57s3WTGkmINZmHf_ZXKcvj3h3eCkwgwiEFMNoXtfgv8-NFbW6ENF9Hng6gP88D6hAb70nTqC07dit9SiLBOnbgvtbMffdONkx4uBzaKCI2snTSkHZVggubD4mIWwVEJXSXvijSIjxlm9lRsdtaMOPfVKtfggQyhX4IHaVrzKSvV2VIxKJbSy3A0RJXiR1ZfrAgrrlMSKk2DEHCmRyg-jlV5VRt7Xq4xF24XWz69bt_fUYRkLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npPOJgp7U5iCQFk8H-KIe7EhRjpoXTwL_c_V97zfpjGLRXrHO1tXpIvi9ht3HvX-00s-2fUCIaEnHV9VgTj3rqxuOSEGY1NsE13Wxg0FIspBtjGiZwOCVnKbWEKE0vR0Bd4mumXne8DK_avv6SHupq1oP2wi_X_eKBwlYQid3yU5bSF2tukBeObMAFw7OJLJAij07yht51330nX-wjwsH6NTsshIed5I3BpeiT8s2jnBSIY6opsX3sKwpfmVBU7SmYjwhjQ1YzcRG44pB09IKqT3T4rDjqJyPSDaaTot3SZOTUAigNBxl3Vqtf2CtLDr-v2_lWqnoCNYyBNYoF8YnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ggu2WqGtdXFGUlzxjOnEmGrpIuPYmINqMOcLnIQ6uKC2Usn0kzGqyrGY6ttnDS5-ssNCo53HHlxiThRWK66eSDZaLoq5ViNH2SP47qdNTAL9h06e0MQ9cTTrpCMuIQ1sSoRZT81EoED0Xk76Qu_xDZsiqXuXefQqvNVh1Z80RHbhzXddnQObASrjGMId64Ejp8u8f7etqzwSiwQcvghdfAXOjdP0G2PJFhj_aOoGJUX1mFOZnNlcvhHTWlG4CYf_2njZfsrwL9ArwXoYe-igo1OOhPhPxcg5z-PeItUP01EKJqO5Epg3dkIeIioax8_ilGoT50bUyyzlAqURH9TSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niqCgpKWx_Iz6PXuKXCHlilV9JKYvT4yJPLxiigsdMANZPbxjWhfx8i4SYWWWFBQvBVSMkil22pT0a6Q099XeBNmk31_lTlBq2gD7MaGcYKuOaPsTtZWPxs3hvLzIOpQY6S0A9p7cSiVecN-EvLMHmfk4EoN9Iv3c3ZEdnYYPofejn49qOb0hQoq_j7CbCR-3-VHawGb2VvDFzPUCDPq9l6KJ7sQBV_sBTxPE1i2jxBLePUuzjEq-GpYkQhaZZQlYh-gBURMRN5exlMatzZmq6dxjl_W05h3WlM4pw1sZjha7ZAHuT8hLgu-Ey05ysnebQnRuLysKNbz2VX8lccYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0wlq72lcwngfc4uyNmQ85WgSqOEX6-qqhYcUuR3HjZTIAjNX-RNXRJMOPlP8Zt3KPx0SrPwhaZjP_BXvzzJzCP8EQM1LkwfhLAJSa4_hjd98G30aJObMPrfWfVknSH0Z1kqFkK4iLuygpA5_NEizO506Esw2u_UXd4iqOZ-WH6fE7JqgiThNYE9AZLhInjRexssNdZfeyQJZODgGgYX3nFBNd7IrX0dM_9v0vzHIqlmvggDT1gKELs-a7stQ9MCtrOrtGOsdFoeuad5345H6SAn00m8logvKtvMsqzox6lqriGncNy9EfEWZubOKY8pVNTqrdzEXn8B-Xj_gukobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTMa7aY9rz_JRcdTs724gTdYzJv9J-f0hxExZtS6JAflWRjRx5QgEr2jECru2FprjW3vpqSoghhRMexLkk8PHwy2XitWpcALLTGJfaj2TdxpBwBqKfmjaH42RW2zjtsPFeJgG7FJj2wogeySySpFJaHDtfumLN3zUBxFFDo8SpVj9cNOWd0WFJSBK-f9tUEVat2otvzlwmlxRfvBS8raOFuD8uyst05mQ2mnC1K8_6ChTC19VXHjzUIvam2l_YGXLg37QhhT_lCA1JBeSuCj2XWzwqpZjJT2tPxs4fJ1rAdNFoXtOK_Ki9IVyXpSo9M-PBYEpQ51vW8tdp0duOavfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jpx9X4yYicz_rX7fcEtyCcq84rjAPlJbpZMsNKQmPBSXUGtU0o1dmj85EJZuEpebtKsdxiNuuEW86VpAOneA3tonlayh3cDBMwuEHSTvrGNU4i76Tabx9XhQeujs353IgKqx5FgJVnj09UjMPXk2jEorlkxQMGbcMHpyPrOBXFbNneBjO8OYDf49wND_eYIBeoQVrSxvnWeGbdyumnMeVwFX9adfVVkCuf82TLlfTyRuUVE3m2Mh5_NmzZTr2wscjF_8bJjp2k5uP5cRzggUg1QPVvLMgEiYmx2sNh8b4stkFUF191XpNzJ0l8YW7M8K3pYqUT245IuEyPV8hAtI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaTy24xa8fBDvDA53jyhcaLkqD7VdLbLlP9uEybVVXwNLYyeCf6M1HUnyQVxQJp12pWBcWIqlEvjT5PIgQV-HfAIgwUqHeBu1LghGESl34TZV4S-CNg827e_Ra5ENgBxOCPaRBTSLysSJOleWxo7l_tb4hH-EcVMXX8QWN_4MIXkkZNF7nu7cJXlnJsCjuNKfcb8P6ROhI3J9XBixnzENAMXAf4jR2xY6Cis8hGQyYQEhj6vbSQuHaA1XV5RDk0WGe-0G-Ji_R07bGgUK9W8Fhl5li0EpQGPb_77JwxsoyoPDdjUP5vhPfsM0tjqbicdP5mxC80WwI4fGJzU84M88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM4hV8dTpywf8jD9QG5CEpJHJF0-lzPvRW_6KvrAsdlTjONCGxri-yLzFZa9ZUh6vNX7BgSEtZVi1K7PYhjn8cgPR8VGXKO3mguPas3XRexOcepV6qy1sExav9C62eXA6sYhc0orphYTLKbgyYAsPvchbTeUWOJya5VekQw-KMSYK90UJTM68tOz-s68I5vO5xU9-7N6F2JxlKqzxz91lLwE0qT0zjK3_bbMc0hFmwQgfPyh3LWm2jFlk07vuEdZQ4u1-thoEtWIjPjtp6u6MmovZiLMMdOL2iqaWVVGWtF6ks4jlYSmFoHa9a3eLIh0gWLfLXPV43bhN0tDLBcr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE2XK0SL0yfvpo9VukpHTR9-UPjMtuUpJgCfzVNMTcAuKkP3dOsT0Zj6KFIl-gDWlxoayN1YZKKzDWh9hPs-al2M9h0V9s0Q1gwmtZm5d9mKUHFMKvPNiEpcYnzuqW_fP_Dbih63Q11LzRYVUdOnTQAs8_40th6u0g9kEraSZimuEV0E8c-FCKu3e0sX8egsDK4DFPE01bVQyTmmN9gF7bq5wPe5PM7rylh4XjcCGlc7BV7N2Bk3j6VZJLQ5JHWQZg3rrkw7tQk1-4-XHPHDaK1bxC9GDzZ0wozMK466c8NuWtW5sdjT7CIqztEWWNgo6fOO_o3_nasMB2c99Yzqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZnWRHsN9kh-ByDEJCIFZQYfgadckBjPR4cIIboyYiF4AwPaanC_xBgt4GQUt6WXih0TX3vWdPXgvjtWe8P34PpLKb2c9fzhBjEdXpzSWL_igmXyFc8I9kZyic658RlZDsEVTnpJFu9P3L5V57FJxKBqGH78KRvWxZMlr1eXDerHLfh6Xhj2urIEyvoj1prXAgxZWF4aA9yvVWlxiGCwS_Jq5Y0dwgdm_ZUjOWnEuO1scwhIfTiRYphZyYvaqWYZyKz5tO4ydDuavccG7THjodXyosWSqD2rj34yYflolCJ87F6SHbltltacTrBlIS2ICntTxEHHCXupfA2gVMWjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEQVclzbbGVTy7_bdjOOHS1ULPNckF2Ex-4T2jsonBhqbhwig9ZtqxzSKYDKpaPLzK18O5CdIygruD225AdwrUq_W4HcIG2wr4T8_ZtpytIYTOnDgQAPc_41fyEJNDcucNphssZZhp_KCLnZVqFGHRlaJiLDHeVt7sBvJdKC5NMJ4uaIeR_3wvuJZei8US5mxi_b9F5vDDYfHlgOS6OA02nGbtJ-lyle_YNLLJkBt60Vgg4zwoNwMrpU5ru7GwlSHQq3nq-8GIVIeRMEJ2UtJ0RPaJHkGvvHhVFlFVyw9ch5_p9cmvVhskws2QcSlV96LWsK72E_GxPmI9dRtk2vYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSLU154mzqdP1wQ8waMivVGwcVL8QYwAIwHmsXnLdS6G6l2mbTY7hv9gah30cgb2EJPun7Goqo9w_0wE2HSvuEMhCGZ76ZsTA6WlDpCMctG1B4YUeQxHwAMt0rd6dbufuzj3qGtXrhVCkWNlK2vsHkRROMW_ZsPf_mywEWjbs_cyl8mf8-Tc4awqwd2oqJ7HQ_A8hk27iTapV_8-p9pNGQYmbaRNz3XgEj_Gk5gaizzl_RQyAldNI-bqAUCQ2OB05TXKz5hCRTpummHRfTGSpCbO3G_1jlFl765eCcMv8o_q8kcnvlnq8RE4Y0P8NjmBB-fAb-v2PrsH6BLUe67B3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhkLuSSYn9d3UbhADPFXQW36nG6vBh0DkKGSwhySgrPVWxCt1hmaZFYxMrJq1bVrfTC-F0jG-xKDluVwrMpcWCa-eXzLM44QC-jdCczQ_SqoVG1VZuUyatE-PpnRyTUhSkrunP8Qafzs0H_X3zG7nPi2xIJk8FC8LnuQjygQyGdNDltNEHDndU4q32hoPRQxo3f3lAiHmAS2QrGFWEa6pwqnuELvn2mbM85-Whnbdo8-ZtywyU1KPVmHAS_MYByAO7NQq6v5ulAtJBIO__hp4yW4431KvVE8Qvuya0CimkGlXSftt_ZIj_2YAbqpcDcjE9rEhK0PSn3rf7I7mnEmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giVteRlGCScEh4cHVl8QPveqvcTw9OO7e0Bku75HsZdlQA3tS7h2W_FppQGZerib6R1YIkaaARe_x2_42cDzp3_M6FTN5Vnju6EJb9lsK75cW_T2zISUj2laU9o4I6SfiWBliJwt_amLqSZcEkRkgOkDmOOBgC_4d01yhNQdZizD8YRyoVSlFVikx6NYmmSf8a2tZPnyneaA5ao9joTHCFKHO42jBAUXuzo7c2_wx2dqJXW-XrRWRdSf_j0ZyyXc2d2zFlSfxr7l9Rqedv81R1xKPBfiNNwv8JYwJFuCoCOn6XGXe-91qcLfkj4Am-eQXybnAlKu7JSu5EoT4wjESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=Y_PT8POF0NPJcFJBflbA2DE7FfhaZkCe_fwVRdfy89l3B2rBfROZhfKKfcC2K810ciaPH-YEmEXYUXe9GF-k_d6Wb6Yw9_FolYNP769mCtSc34YCv4aTHP2JDohwTuETLbv-P9v_lK7pNx1Cio2DqW5Ice6Ih26-GASiAXWB94vY9FZjQHauTE7tzNS8DCeOuQiK-MbPH8FiHWZEFDd3375oKjturdZSZNIFDebXq0wd2mbyKlzE1WJaWbR2j6OhcDPezMMsk8iCeKPOr5W1UxW8OIVB5kPZXH_beRRks6xOrJNkag_S_DTyyscL0tvfsPrnVnVkrxs2c0Vjro1Qug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=Y_PT8POF0NPJcFJBflbA2DE7FfhaZkCe_fwVRdfy89l3B2rBfROZhfKKfcC2K810ciaPH-YEmEXYUXe9GF-k_d6Wb6Yw9_FolYNP769mCtSc34YCv4aTHP2JDohwTuETLbv-P9v_lK7pNx1Cio2DqW5Ice6Ih26-GASiAXWB94vY9FZjQHauTE7tzNS8DCeOuQiK-MbPH8FiHWZEFDd3375oKjturdZSZNIFDebXq0wd2mbyKlzE1WJaWbR2j6OhcDPezMMsk8iCeKPOr5W1UxW8OIVB5kPZXH_beRRks6xOrJNkag_S_DTyyscL0tvfsPrnVnVkrxs2c0Vjro1Qug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K442PAqCMIcCgJ24bUHu3AojwiWLBSUAnriSH70xzQdVeWzTUJrZQOjxXEV2voXfSap3W6Ycg_3EQTV6SebLfWb27P4odsMxb3zXP2CzWLYAQ_ZLVRqUpwuCQdTpy-EyGU7zyaz9jIwCWGsPIpU-wtT6DSVFwO4SmvjpYOzfVTak7NGEdd1CHUwdxUjNQPiO-Ng_htCzqFbhLPIsCdw0Fg3DSMashSWuM4Q7pC23MffRovN8kIam8I0xR8GM4cZZbpDDl75bMABFI0E-b_DPbr3tNBbAs28gfaUt_0CXD8o7evrARvXSfVZa-NQewsKyxsDvpqMCKwMY8UBLIEX_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMgcYOZoFCQIqDN5GYpImdf-v3HGYPWKyO1BAVo3Oh-DMO-7zHP1EHk7AICRXuwGvXPtxAw12CFNVDb8wUUFPC4N6YHv6tou5qIgHeBZtHqB7eqXEGSIgfKWdmvNRJb88Ljc-2zZK00NjPOu0GicDf9hd6RxMyTo7M_SBmwkHpi0-kn5TZeVJRpl6Q6eqMUzrXrD6GWOZqcZ7dI3629fSWOqTYuRT3ZJ4a7fxMTGnGFSa7R9Bp9T0mbVzMea3dCwHyA4Ty8EwUfuYXk_OB50WzTJlwzJaPj6O0jKLQ38isksnLoDGqF2ncr0DgZymJwMb5xr0AmbQdLmp9jdKgmOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuIEue7_O9HgnmgBoSx2G0VnAxesZx8-lSUU_1lTL0aIABkgGt-VbzUShFFuYJDWY9qLRKURzGxVnaQ7Bx20KpybbzJ98gdkvPjoPplTWiU5e1f1fz3FICx3_kfrt6rr51nbzYoj7tCsNm58ChbSndMFiNmRa2aj4NxEIR4x6Awnq7TvH0Sml-Tmcb3_waPoWmgu2muLXYOPHcSleh_cHk6Z6I89qCi6-DpI4e40GOrkhUZPT81MaAantPle19uHXpSVvM3lqzw48zcqULzDhJ-31VCLff7gMpZnby_MAdRyhalsEYnZdg5GFNqqLpDW6KJrH8_PGa6qWGHYTD0h8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaNfS2e_8rqfbylRwku_oxTkAn_CYLHnyge2gIjdUq3DkwbLNrc0jlxC3x6flZDGBK6-wQtlu2Dyr9I5gd1MNJSHkL-CMquJ88_hw_PzTpO4m2Z5qqX45jhOgW2BE_cLjzf9vx1Jh4gmWUPJ-attIi7502FfdAXKcdYSvkHcz5eOcC36WlM8oppjnAjzY4GeJ_6bGoyxbIgEFPJPEQUDwJDFqPJPAteGdiHQWyTb9gLQrRpnt1oHAnhRrI-MlrfdI3xvtfl6Tj2ww7Xyv05WRN1AHX3G-LNiJEGnhdvCeTOCuqd0fDtFKblqztiM4WrfNxYeCzuEtd_fb2nnMx9_cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abERRcUCyZtjLKY9edl8cci-MLmhzVef0mN8ZLaXIjfWxprpRyODq4EjL_ABaMTslR6tSpNMeX3cP3yUjpNLrrmxHtHdXnrEdDuoZ7o2TARtO4F-6tH68jBlf9K1eUSzR47qQfibhIybq3ZLRFeRFSJbBK7SriSLb5RLxHZsSrrZzaxtsXmQxPk-dwktbciCIvubN_JYwv9tCUEkPNww9nLjo6kM0yfXOEhlYWrY4PP9lyvEXbMB0ljhj2iNKzuxwjJzd4r2cC6JqCP57pZMiqoRK2fhOjktgeFfiRDiVrwnSzLeR6K1u_kGn1g_nCNC5ItN2HYhzvUmzZ5_gdra6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYYC_ttINKqjkRgrvIrOl4DcrIArFs69dhCc0AsReC2TNGd1nQb7y4daYMveCzBc6eGD1D3Ntg1VLHv3054UkDFJGFDpvOtGsWb6OeWE-RO9hydO9VNEsMN19TCF33Ywwtiaj8oqWhuzNhVZAt6mhsbPtWDSgW02N8pFurksJ3ameT2X-tS5cgfxKSEOq5jUhl_zNe1SfWQiDHr65EK6WRlzHhAt6F5KC8QbQ4KEXgVE52zMxcdKGYXIK2r-eK5cWkRL9ryKARvPMggF-OYjHf2GQYRc8rb-Am4OtOC612cNF0db3L6iRFxUwMDkPX1YVCcJsztjkz1bu72QUVQ02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilx8uP5ef39PgeLBkZhRpOHMlIebSFnjyGrXAZtRuZ23CTezGuIXIDkAQoxCnTh-3dW-dwFtKd2b8jXUZb8VHcrhzxENvzcldH3qMpYdpZlqNMIZjUQavRzYkvVCM-C7k7QO8SpY4VsJ8uKlZhYQ-0mBT9DS9787BNdDySH5SYwCiIrraE6ceiBk3rqVGaQR-Pf_2QxariT_ek68bDNmqLVqeVN9myhJQWdrZjfy653YU5OqzEuFaFZV3f7lXU_rVIcWduZXVrW0613hWLmFlV1D1G63-xTjChks9yQELTQVK2Nl31AeW-zq1uH72XEIjlOo3ouQhtbukI0jWO-TRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szJEUMBhbLr0agzWbbkKVkrGsGlCR8lMvhU8rwUBphhjzH6hOVNWvXHVU277eVKs6K_Nkv2hgwmAkqoAPHtU5GqMFuN1n-9LjYo8sYRU5AkWoGlMQe1BfNNjd8I0JvmpTcsa8-5_DrxLEhQl88emUOCLEOCyTlWcCy9-9gn7pKfzCgVIc7FHrwoclWLkyfeyBiMamfRMFOHnJQhRaZz3gjeRPJ9LdRU_fKOBtdQ2Q8yXOxYUAwfGxMcMyREAv6GUL27Bh4yjnGBvWqNF9C-_dW35DmMQ6x-HgjZLJmkCOUcq0uNy9bNoHa7t4GBvhHJWmzS1PkfUxA7MQjp4HuSOyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueAic4XzgljEB3OrJakrmAvwXf06BrkaJm1pBuyzvora2sQ6o1_HGj-afSmf4qRhnkoHYFm13nDmhIbbWiFajV1z3ygIZXAr9WzfU-upw_hJrwOL1s2aaCwxFyQgjKSyCtgAx0ZB-phANEvGr8hLIrc2nDw4jjIHeimXgcFYOaSJlz4oPplOzsLlY4QEJesGPm09ERPrPyBJTWjLGTiBSqq_0qZsb8F4XRoVqEM9GVIp3BkpxA4Q-vlX0Bv9OoOQs-nqwxIPSlG8ZB4UFiGwv7UXznJhhJgavZ8gSzLo6Zmqavlz7K-tl_kXhoRHJibH65r8VBv9PuW4_K9Imw25fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcoj5l5x6VrUgjVlvdNbxIEftZ2lcd5PJZYY8LeBSqECZhDIxyv7ONqscSuPnkXfr9mO1UYVqKeEtGs__ERzCvAf-GZPv0_G5v9MVXOs2sl8YENOmii50NBcPRP2B5ixychOo-ziKaS8Q9nk_dhv3pPXgbxrB2sYWmxATY_02Um9Kqtf5mGSvP11kO6P0BP1uJY9eg5x6386PpZtbCQ3Yrq8klTNcC3yQDgRHrOTVsGqdRJR75aoCL5InBb8-HHI7MXRfH4z94emaj1EqxsIgwQTo4nYEXDR7T5DNmWyCI5N5iaZ8W72oMl1i3ZOjwxmcRzXcQbLb3x-OuerfVqCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COdqtLisCqDCcKR-zabEAXaQfAE2cZ2On0Ji0wulBQEgOpLsfyFfxRwIdb81Cgf7dVYWKoezjQLoDpAyQHWRwMrRQ9FihwYVVnJTGaINMnCeWSGBNck5tgT-IF4vmShKcs62ySIxeyL4QMwQ1EbeuboT9xq0I6TS7txeNplpELrQlOo4-cXsz0RVpoxcU-9KkDtS_0k7N5Bgm_KzCfvJvgsBHz_wePVNq9AlioR1yu9WbYGHf6TEHZZ9cvGViLZ_G5RV50FNyj8ybqbwNcRroc6kyyPXTTyAZrJHvSzQT6KOzgLP1E8o_mIyCCVOwmOx0fMYoBEGG7s1IP-uPGbvkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbMXxkCXrMMIL6kUOqdLCtnRkj0Lkhi9bFlU2iELHAxqimtEGyX9cm8hVQkKoBODwGy6TTAej90-pjlLQgUbBSXCe0i5Y9H15NjQyesbGC3-a0cQcFaci53kj9BhVFfjJ2FKTTcFbgVaGD5ZLPPa_vfvZitWUQfkITlqF5Bxt99QXsTLfRyQKAwcKQ93Al-vEhbz1ds6S9iSjz1et8wFqnXFxSjazZy0n5lg2YzvaipluaDDPX2rQs3kPqFA6hG4_9ck1yWYDrbiDbkXe_xrNCzF8NmR4VUh9xnOrk8DJkETW9ra78AbeCYievDUuLYpS6_4jUpWyQo5HfHG18o0RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttzGsgruI06D-kz11lDxzYO4TD7lKv-MRdsax7D3mHnD4v3c2C1D7uVeT79mCphG3iPQ5md-RqfiM70ZnwoykfJkPRttB9RMNFzyF-f8z6pFwRouYM-V6YYB86LRxTCBHxX7B2vulJtX0uH6IELER8bQHLHKiQ3nRBvSUlY8xricYFWY3-4HSqpMs8JbqcSMnEwjlLRs0Djid7opvC3y5RvlqPh6mG03WjwN82h7Ye_lrQU7FGJBVcnNvIRqmVqx4ybwzJoKaqhNnMr62jyCCx_AyPimHcASExL-E6Mnh2b9Lv4-qVtd3_GozJgEA7ZBbvszLGZ92v6kpz0yRfF2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFjJL-q79cYlUoyZ1VPEW_II-tMQcbszd4AGtaeb3yFvj1ocizZPrGnvykqfnzCaCr-w-FcNRcmgk-CC1Mdx-heOmGz-GHIAkyPpCNGM2w3sxMX9zN3bufp4gGRDgQ-xSg-4xmghYDJSRXofsF-z7ZMt9TPWrXPS_p4h3gNIQfEG1ih9FX6XSb3TLzillibXjEBb0EXC1-2NffjZ56tGIMNtyqcTAJ8eM5-ZF-ZcEs1YAQ0oSk0TfKq4zx83RND2tZPgMzkjmxcGiY7kzY1cexEn0HB03ZPfDi0pvZON_Z-qrcjwOmOXiYR1FBwLLcTrtKEOqyy6259Mwx9VNhPQkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un6IzSnD47UQ-_6pdRkRLBOi2zyvEQGiJFkRbwHL8t10In86w7-pOMm9AmjmdqcLFE612ls-CXXMO_eg9P2Cdouv4Xs1q9sZA4_O-gmpExkcQSGPER9vUSQCD2oIgY9HfoqLI9wze6fZJg87V5Wj247F9wy50Kkm006lyDgiiC9qvFPyFNJseIHy8jwyLSaukxEv9fCIfFsyWU6YxexgM9e9lGBZ0JMGe-L7QldF--iPfWx8wYzOV1jAXJGXUJAw5njUpfY21PNj1LlLXijMk3t3TcMvAxgf6qTqNLfSgeWhVd_2AMA3QSShZ6eV5pdwbkIOA3APIiTF9gsV5eAkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fn1RVbwLbskGySmmzok7hRqQrHGWk1V38Z3J79-vb2b5QLvJxamALYo77I5XRhM-5yElHQY_JH9J8cumSE-ZlOJ-M8mlhVhd6GJIJvxUk4nw4I1MkGdvUQypHW641cUBoRwyltKfHzZcnqN2euJaHWjmB9ecRtPq8IAXs_Yso0DdzQctwY1HSEL6Hi-MdTfyDVP-bHKdFKiXE7soNeEavvfFMQO6-pJNpGHSjwSJpx7jws6NV3KgL203GVq_mZGHn0Keo1VCHZzOUpQaHuoBmp2kUYC_9vSBERsy0vi6gLP-ePTBUr6fy-l5hHcYUc4bKq19tMTSJNatDwkrJPWP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O33kIqi44-L8UG9KjCMN1Gmlzcgi5gr0m3JGSJbmUX0Yy7c_j-7FCmJeBQ9i3kn-ZNdFxTD3Ww0h_N4rjV_8aRUXB3w6reIQkM1h78DNAGFVIbp2ISx6zG1mH5O6HimifaBDZStPSqbglfsAqLajnIK1Oyx7w8k5Ax063bqBruZVt9ZKTNVzfoex52bkMNaGbFRQ0mA06QUtQpvf89ceoEscXsbDjqu7zejCr8QaGNg8jvI4G63SkeTUkeuhez4AKzXmrl5LjbUIGM8vNk-bOCP62NWL5rO0tCdeCwt90-NLABsxFAb4bkovPAaHXXDEX0HZ2ZsxTvF_hHUf9rArsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W13MF7lV6IoxLgxQG_0lqO-hSR_TUwna8uXOTqpxeedxTDxiNPHlzj3J9jiYiaGXaN_y43j4uy8hNKtn62mB10aukwY78l8sh9AIq5aJ0K6r_S1glDuDELHjBcbVCJ7-Ab4vesMi-fzXIud6swfMJaZt2RFXWmfMxj5VWNQx2sbJVQxiVU9c-SsIi1Y_BwZDczuA-bDJhAxLsMFJ2wHRrXg6lD2G-WdSv3DLnOEyO7nHStgjd22fbMdvu4atQ8t85PKN-QwLyJdfWo7DR5ad7ncekLRpYnENMxQDzkQWCVc0hsZTASmY8K2_kl47Ta4OXsQGvln7j_fDIOQqGPwX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUdWbpoz0NxP2Z1Eg53KJidscQo2UUmWBwXD3XurqREFtkZqpK3sZ-rYeyrrIsKJc3c-Xrzcwcd_Pv7Fc66x40NFpE-QX2fZrCH0XhhMxMqwUWdf9CZUR9XFFxVUFWZfD9-wLEqkug-3V3X87tV5uYVN8XXHbw0ghDz0r7_55eRX3Nq1IlERyNWt6ilMuaavy1dHs1zlji8l9O5REIW_RT3kOYQz4tVGTouNM6IDZxkmtMktpT9AQNN60ffira4fJ5T6waowb59OML-SLUIqUYPPmG86qz60L8TjmT2H5m58U_uUe7gMoUv_adq2jCOuIZePJD_bv-heyEYwgUcU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtBq9R3GHsB0fixrlKflV3_EYeUdA8dXjx9BrQJN4kzsEaw92IFUVFkzDU9qrsYT2uDtAkmqc3iklLdBaTflzAMoj-qY2uXaZaGV8OEpciDsBoxckBTn457TxzwywA8UaFFOLWTDVgbaD3yCeIVdO34S-yeVoozUEeOzsWGABRtx7YsY0LjXvhD3x8pIE_d367e8LA6RcRtZi_XC2bIlIPdliKCP5XWnqIlw8oFgu9WOnsjV3Gm_Wo5HxdiqZoLLETzz24LrxUaZ-w3dNeTPQJ0-u5FPONyp2nmAu1Vwb0MDUIwy5LuSMX9_eU3yGjx5-c2zP6p0UWzgM1sEC5163Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ7CMCxvi0Hohf6yacx8ioae_h39Vx32KN2sWK5iBxs7byGE9p8wzvjchHvh4t4GOpKb4JrP2l5KlY8YOmjcc1e1QMwEWE4lwqD2P1k1WsI_TNJydM91flvu4u62NaRN9BmpTsOa5Ib8i_bSjds7MWtIwmZyBp31_6bDUSYYdg931Fyp6tCB1JK1bWIGRlS71JkZUYQwE6C7KD2vLW_FfILSy1PEew_V2CPS4pFB1THm66HxMDGZ_hPHR7dQtSWqezdO1q-fnZ0J4sBS8zQEWkkDBGwpsX2ZaoSo8lCwqSK_9X4kRkIipxLVZN8WkYbVrr61aIui-Rf1MMSMapcSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOqp6HhdHfSCLgeNdBQ7eUzgN8M5OLlqFJ1lBpf97PEbjQAxu3t5CFGnMFujpnmKwybQBCbnPfG47O5p7rtTJ6qhe_2grIXUE_Bchb5ZbU0LvVcGtD48ivPicqBulu2JhA1O_uiUuJtHyB0RfwQgNZsqUgyMOgNYybwc2jn8lHowJJLIxMhInKzW9ndBEH4yXfiqdpuobm1rSuZaGM0pM3VPFUgoyV0ZN-O3uFdSEJ7yB0CBPpiNGMAPQI1LtHoxBEg5eDfGFn8BmnDMz0rT6uBX3qSWuUmuYS5rSKE8XXBrLvwmsYa2imDGlvxr-VU86cseFs-6ncmLO1eR8vS4gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyAM1CSKDh-M9-6OsjEsCqcZPWb0t_0Ie5R3Z4mcndteBVyJ7skMA1phe9kkbHtglHArIyXg1qqrjy8enBoHIzzSKKN9RjPpdUyrZCHZCZFV9eshytcB4leEnvLeEXSqauc48BtmXbJf7h1FJe5Osy4E2AUgy01XBwZ9_Vl3jqeH4T1IurdVVByV-WOn5-wTtNonDKQasfJI7E-mLYu7I8PaSI_gQ0G31euAMaeQ9L2Gg9nArE0quUh1nOs2lxJ1V4iewy7D5DzwByfs4Josonttt74ouUAvMBz5sm-6erpAmaGTDBOo9uJ7Mthf2bJ0LUBs7erkSJFS7djukbjurA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=v-vgpPZnJ1SQ38yGy1-UtVaDHO1tUb2ng7KU5qhArJO2-59Tz_KuivuV2bNC84fQSnCl4NBOC7pKfKxYKWnavfW22feK1SjaJnQNkASOI4gcmkPWN3LLJyNU3lqTMthyjWKdfXB00xg18yWwMxRNwrQ1gUEURsi9ywCwyvPqkXG1F1CoYHQ8rwG0q8YULn5EyawycERltEBMnhmaQGkAbCAVN9-jbhOheHTYEBFOhRRu-jcn8S_N8g00NZC31lxpg2a5ixTTzpf2XfYkRtzh01S5qPZTx5-37LpXQ_iWMj26gkK-VOJGo3myEryDgzRE1HCaWoDpYUYJBkkXFbq0EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=v-vgpPZnJ1SQ38yGy1-UtVaDHO1tUb2ng7KU5qhArJO2-59Tz_KuivuV2bNC84fQSnCl4NBOC7pKfKxYKWnavfW22feK1SjaJnQNkASOI4gcmkPWN3LLJyNU3lqTMthyjWKdfXB00xg18yWwMxRNwrQ1gUEURsi9ywCwyvPqkXG1F1CoYHQ8rwG0q8YULn5EyawycERltEBMnhmaQGkAbCAVN9-jbhOheHTYEBFOhRRu-jcn8S_N8g00NZC31lxpg2a5ixTTzpf2XfYkRtzh01S5qPZTx5-37LpXQ_iWMj26gkK-VOJGo3myEryDgzRE1HCaWoDpYUYJBkkXFbq0EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVfa7dBl1sfapmX3bu67IhWoBpw2hYvID9ggaRZcouV96xZfJ1HZoREwwLaLU4n5qJgl7XNnk59S_O9QMuNRUQYW0dv70yXjhDL_f57xPmWAtAEUZDFAsHKj_l1gXbqQ1x9TXrInkR2yTix2CIlpE8yk5nctg6qqZ9XDPaJAS8X4AaUbKLyPG9T1_6Jk1xAbVzGugd9pol3UESbL2fNiCb7Tq8lgZQ2VFwmp0poseAc_h28L_FR3Z_Hiae0AW0wkUiLZVSBQJ-snrTqN14WMA_W5G7xJdHQwcADdM7vOzx5tmxZiGiA6xWEHgDT06m_XyDgekTL-glkX8cF5DpEEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFX6sBAK5rUnaQPa_WkUgy6EShiVGOcioim08uhbsZ0cbm_XMrfzZfHJtJZPY3edKP4RJe-DcAp45Pearqair0Mc0JZsm9rhK-3y9ql20BjnUXSgmQwDpwChprONsSd5qggk0BHJC9YnAdc-oBcZDmfzVIn92l0CDbkYwr_FajFOH3opkQOreTLJ-VWkLXidRNu34EnU618DrkGDkXOBcqJwLkv_dWIxQ0_5TUQJEMuZiuYq69wnhdqADNYFTp-T_8KEbDG2LaA87muC3OiZky-SLDKGmA9XfTkYA2tXOp7FoJHEMNKwTP6cvgp2EkFTGTJIQWzIhbI-cPQcGbebpgoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFX6sBAK5rUnaQPa_WkUgy6EShiVGOcioim08uhbsZ0cbm_XMrfzZfHJtJZPY3edKP4RJe-DcAp45Pearqair0Mc0JZsm9rhK-3y9ql20BjnUXSgmQwDpwChprONsSd5qggk0BHJC9YnAdc-oBcZDmfzVIn92l0CDbkYwr_FajFOH3opkQOreTLJ-VWkLXidRNu34EnU618DrkGDkXOBcqJwLkv_dWIxQ0_5TUQJEMuZiuYq69wnhdqADNYFTp-T_8KEbDG2LaA87muC3OiZky-SLDKGmA9XfTkYA2tXOp7FoJHEMNKwTP6cvgp2EkFTGTJIQWzIhbI-cPQcGbebpgoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6CXvr8V1pobHLyqI5g42zFHyNy7adeNjCqG5rKUmmNQCqPdwQ6h1Nm6GAx07TKRkINUEJE9eKQPUSDl7fy_MD4E4Yo3l_ilguVftS8VO6crOsr2YIWgYH1lncUYHo_63vExzzl0g36VPwXPqeLOi6-Ymks2RPLEktuAzSpUAqn33v5iXfwCjSr_JjcHz4CumSaMf9vdIlFvbgAeRvsUtO1vxaJNIQJjk3HXl_U0vk8AvLLJTITiTe2F1EA50gotDkFMe0NBq-rCZzOTC1j4D3sBmjixIcnDN9bgmz08OGEDeb7GLOGaIGc25Zqf20zoFcF8Qy-pJko-DorIKdaLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R41sV0qUASjiKzyqtSAZ16ErRG--RUDr8AnLpfRXceMhLD81GFZVnKy3aSDWqnohAw-9CLj4nEGInElbXbqBGpemxE37FjTssCKuhOOPHQWG__Gam_U2myCnLx2WUMFUnj2nELsqfmwKuGbGUbD10jHcYTpxGSDTQaKppOAXyY9lzoBdB90IYrXkP-xLxDYwvNl9xmLVSQTCuMgA3XtwB-0Owx9u1pFSXZyd1MkhMqBNdHj1hOzzhpEcgGfevgDAINx3wwbpJz1NNhhLeeYKs9pqK5m2v6LHUfFsDRDxbbh4F-GRgC-FuboOlkKFjCyJPWE_dOrWjFnToGGndr8lhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzBZhRkFB8gviTo6RVWDDCzsYHtZZJeb9nCStjcVjZaavbPbt8mNNRYfplT9v0Ozm0QQuETlnjOPUK7Ilmiptn7YsOZbs1Hs7s5xWqGqrm-iw5rL3WD4LlzMf2uFrv_8qwfze68Jg-8gjMsiD96Mqfk6a-AX32UZ6CPOmqCT-Unbs_tNW9xxNxu7XJUeHfUIH9tGUTE-yCiAyUybwo_ddaCh2fs62lB4ufF9UG5i5fpaU9CzwqhlTtUIZULlMx4Ks5_XjUVISOB8G5U0TFNwz9qHzFk51YPy30WwjNymCTy4mLU_VVPCIIuozkwHrMNmSAI1MRg9vrmyBIWup2CQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRthDEbd3VezOWyszaysNMoOMOb9grgZo3WJY8Q_u_-w_p7tVBIA5yRd_uQKk1bvyoli21ske-l-tSr-bR0dtQNSTLIiTJm00nBvKJVZ95vVYM-ghlbsyeX0kufp8OXNW6uNi97UU3mKItnj4MoZVkITfN_ccE2TwFWHCmRvRXmdPbdPl9b2skNADan1RcT5D0uJ9lNgKKNJqoaV4csaNd_WNJd52Z6BidT6dFnxkFcbzLFWtODzesm5xCK_YCXfJoRHq1qsisVGQxXb9Nr7wSKUfaxkL6qF63J2U6BEQD_gTd6qPiCCTZ-RJRfRtxbZBhmit9BjHyUnew6bR4on6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f23EdEfKvM_7mUloqf4kZQQpCS45bEBnDmK6iKsuTB9WcG5ImDi-Bzmw5EGRa0uCWmwQoJk1K_1KPeXps6AofiJCyw9hEKlzBY84wtIU8Q8IpJcozHrVw3PB-Sev2KweiZ3lIcqhbLIUxtD3q9rJfsCWdMRbKqngiTkZdqa2pErVAdqhxa8cNpRzr769l3c-a-yJTNAqUugDu2-OPvOHm68XeUqOMLz73IZ2d1qvVV3Ynm5Jlp46TplKwaIyfkmeOpWQDhXbhqDQMEIAKeHRIscl0PvpqlIIEV_aTpUeyFs8nAlsj9Zm3fl2Jsdpxn3e3AUgbjTROhsRShqDFKeBww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeRSDsGU_R0upP66vKShwn-IE9KwdHTuzUeIibRlIVmK3yzv92yHIVKOC-JMqx5uEFFYdD8Fb0ztrPj0hsyLVmEp05cf-VQOzkuYiLlkbyTfrPzugyCgxe_FsLC0MM_PaI2I7xjMtP3HcmNBK7sg5Lmvgd_J6LhZPJnjbWUl9yz9_rrAQ__-XU99ZWvwECTVf68ZvE05tflYGSlibyLDcl_2ZK2m3_nOQFl7XUIlq-G2Ec3wr_XeDZuSH29RY1juA7u1hJBl06xmdshMSehaY3amcQ3Q4FIvTf0EPtuUzXQh4MXPO7KmT4qSTBy3gJm0nX9gnaDy9KmjgPaQMo8aDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I501sRaevVLKcgn7Khu9KvuqTfw_5-2ewNPaDP33KhYfi_klqSByFzaBjF8suQwaUgHKwSgQBHa_rvHieYITucYYRH3NwB2rQWFSqttYx-Gr0OH0oagcHq6G7AjJo80KysEevLPse2vRdx5B00ixo3YJbMFvyqEPNgaDXu7T0T1yyTRzxw0rumHl02WGkCXGQwNBwC2ZKQakJzAeD5G0BmJEOOWXTl2jlfYSpDNQu5LuultMFF20BQ0UNuDeB9_9KmGoVW7LS2VOBsy9l4EL6yt-KKwXlANCGR19OxCflYmtfejbcnoBR5xZYuQOy1XLxus-HMMrKVC-Ph5AtnfDqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0rvHkjj10QSkYJODJAZl-80z7tE0qRU-1bOIK8Uty9MVJQ_FG-s5Z4kLmhpCgSmoWjxmsY8AKASZVmLbtDkkSs8uYZzrlpzOIdUBiFnOQTt9YVnc2hRps_VPCUIMBqyh2pBuTgj_ZPB-S6t_3jBe6iZDWoQiYGtt2jbqkR0a3vGXuvHuDucVzQUNfJpIpD-e3fseo-uPgH26psCYxgDcnwXP3Fdx26eWjLZIQMeoN31_2Vl5LpJw1ZUH2RM5OXPMsquIV1iKhCgaKTpTiWelhV0NudvRWCA58EAesepK-RNBdMC1_YO_yUi6G0xvtoNAhPLVYMwek8_cOBAOhrFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWnBgy_0Ph556nDCvxtipR0EZ3hX6FhvF98q24wm90t-3Sg4AOp5WgL4eRcB02a1pbdkNvxYyIMdn_EGd1Yj18pQTBV8d65qdOTSP_2rrbtZfnY5sJqaMbXDI1H9UtZfjxMveZhXAMGoeh39Dt3AUztBH3DZH1ySG0_EUB7b5UJDx5bMwOa-x3B099AdppvLSB0RxMh_txcZgcCGaJFs56-nkYIhkycA1FXg1BP7sCxu1NWdEoexDXuYTN9sk5Y3UIKmH4CFRE7vfSoBfvEwJ1ZHzePnxqocH1y92LTa-1qKzfBOjKaz_w739LfFtzvTwDyaVQpjtnGTqvhhUhyVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICdk1HNLAJ4_cgO7wkbh1IYZ7XemDqnlVHEn24n5ARg4t6JMu1VUi9prZSKritXzWv-4jx5FU7KXusMCdaUd58G_CpCanNuLis978T8xF4_RLJw8hb-y3AlSxMa68hwB4zWQmX5c2D4ZRtheR78qcOb0KGy4ELaH7fzmed4eusqV2B8VUDnRFc27Wy_FOHn-pPKgNJuhRh7HX1puQtP41Tz92kscBbNGWJ06uRl6eLSkp0X9PUld_8ysNarZaeLBdMrXeASCAlJdE07o1w5ho1PaIOKkfbuHWYT2vys2Yl9ISIDDMhg7YjESLIvJWQhbIE4snMsd3RVS6kpFAr0fIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnZV6KyzPvSFTrEDTtrL_it7npVtUu_BzDNPArWAqg9xYPltBxOOKfr4ee1_7qe3TwZesS7KeY59pamKBx9zpEkSYA1GHZFuTGXRl3r_MwKyH9C-L3zOz_ic0zoanRRQlUOwhqesNEax5JI6m5wBxfJKXAnb3FqyOPoO0xoZEFwWgqh2h_ObAj1NYEsIJKjt-YpO-ng7hI1I5QYnIsFpBq-kRzWobR4qfgFbNay4zlZefQlIgAMfT6wwyqdkB3HDOw8GGIlfcBqxluCt4Ozy-r5EXdFtP4GbQwDa9KB1NduScA7NKrArDjXpK4PGbYE-Zo2wjqkiBTmeftOB5WEpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=aSNMKRLwmYUZL90LpeCubbbHLyz16iHDIUZDd9R4G03NvIKhs4irJtTv5pZrZLyC3o5W9Yyw3IG2N6I1sCz_aLlv1EoRHUWL8ADEk9_1GsDVvlZmfnikTshlPeK0uWe4oD7-8JnVWEOuNhdGi-5KGU9Cl5V5NabzgG2cxOCAwDePWN8ereoNAdnyUqHxdlbW2cY4NUAOgsRFn6YuUFY6uQ14QTZTCNKgk6SFZFwW7sHOvdA-5hhQOUPv1lOxMVgYGUrDLNjb6YMb_S5nUDyMzyCd88O9ULO0iaUQOE61eeVfEIrohbZHT_oBe2zeEtlCvtazKq8hOunl8b-o-5oemg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=aSNMKRLwmYUZL90LpeCubbbHLyz16iHDIUZDd9R4G03NvIKhs4irJtTv5pZrZLyC3o5W9Yyw3IG2N6I1sCz_aLlv1EoRHUWL8ADEk9_1GsDVvlZmfnikTshlPeK0uWe4oD7-8JnVWEOuNhdGi-5KGU9Cl5V5NabzgG2cxOCAwDePWN8ereoNAdnyUqHxdlbW2cY4NUAOgsRFn6YuUFY6uQ14QTZTCNKgk6SFZFwW7sHOvdA-5hhQOUPv1lOxMVgYGUrDLNjb6YMb_S5nUDyMzyCd88O9ULO0iaUQOE61eeVfEIrohbZHT_oBe2zeEtlCvtazKq8hOunl8b-o-5oemg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtycAU3hB1ppU17Eiphu0erkVycTSwTn8_-fj9q9QsnLVwe-AAQxuH9mfzkJmYye6YPhTRC3xaqi8ugHZ0WWyYNMcOnlkszlwotxpu5T104Sb5UOnyfRhC9ivdKwWMYmHA8bCTUWjgLgIWKZtGbqC0suTL7lXucRXvGlbeusng2_WHgSYXgZEbgl7W4aYowDmufSjPrEdAeOfegKWFluhy2fWKymLnO6QbZdTimditfS5cXgIo_qiR6dqKOvkxl5Dqu2Bo-e37ROCRMC9iZUwd2I8EEJFJyxxYHJARZ63cV0BOxNgu7GqSgrKZ3M36trR72c74B3rU0BrcgFcTMNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR6vK7hjcLbbczA1dFaRgui7BEccimQiBugbMWN9M1y5JP960K21XoOUHr_OnLnDOprnrbqrouFe-JbsdY8jmp4HMC7k3T0LS03fumyp2olhw5gLz--OQw2ExC6VyLyg0CnqOJxjTn8DkzJrW_h-ASyEgtqkjvkGHWKOTzdmMxSWzi40RTTVzc_mF1x7AFEoEyr20qAIl8XprXNIwMvV_1PmR3vSuS1tTiBl4wOWkBTwv2cOlW0ktp_9WQYj_V0apDd2V-re9SwtnwNiFyDY-f84oN03XLmR5xhsP8b5BWSsb_p2rE6i5aarqRz3tgE6bryDec7qthMU56Gmhms49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi--8JAEIsJRh1ndFrPA_RUcWLoANXcKMjER-HjkBUNtcG_pxC60jWtXzYkFyat8Cn5LhP3uV0_DyJPaPsxmmrE_kcJBwXvQ1o7s3QYG18zpfOzqWUgmfTIuTWKrtnDBPjWBuVJ0Fll2C7ZVI-ePRM6gZqgJSIlRvIQFOxG9tmLxqA2fp9AZEg6bTeVmh2OFsagZkqviMeEwhVlAHW1W0CrBz8PtINL4i-_2d1JcAKMgXtxCXq5vCVRLNojD4ElxucKhFHRNgyyTq_bQcqnA97EX3RZ8lqGT5gkDPSI64QtVWKEcggVUku7yn7bCj9TqRdssk9gcUbbhfQM1uUwcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaZ8x3VYvqEc5kShzCOg18LJLeoaAJcPp6lQAVZaex05-jlKoNzNC-hYAHtnlNgJciEnphBxLkqmkSeuweJZuSuyzm0oTNmtvbKMmC8vRLkEs_nqD-pcrh1v3xyKTVCMI56veVsnCmefBSn0Imitj-UmRSVwC4EowVXXq7RcGvpwnioVOcHjNZJ-MelAkXRvqEIr7Sh-y7WyI0v35skJOO774FVZvVcdp6X9ao21Q3Cr3SEj6WFbXoz8SZGxUyqjO3stpSKgXDJ3M93CjAHf1KGmrcytBKk2nEvjC1PKcaDKDpld23CdpcsE9HpE5BnFTuLARD8jK2sON8FFg3hB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siAz9P_zTxcy2OKzafC5Otu5Lpu009HD5FI5tNEe8zaRMoJTtkXIALitf--KTumyzdyay-fg7NcDCNY9u2oXdlTR1t3cuuPfgrEb0JBlS1Xoy4tAJH6ZamS3JjADoZQOFpZmJH-Srsyk960NZjkdSQVSvD0RbhWHY8AgFucsR-LolK8otPXnTfzGsyWg__SjJM0KRGjt4pskjzgD97LitbheIrGm_syjCB785SzgSxVFLvR2jGmhMk26hoNmIubTnh3hkBGmOlzQPoOgJSPndQoehWsqw2Vh1wKb-H8YPG1cJ9g7b4TPGiiejzZQmqG_fA7I5d_u_dHzOBnaNGTTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FirMaxdJ4wwGJ3PtUx21pIPPHFMftxpNVOt1hwf-L2hPlUE1XTFVmdninDJfaIVz-Nb9Awd0lHCLsMa617B0d-Vko_y9aVDApof35yD7WLz7TKWbNUom2EPO3qicpOvzc4S046JWJ6I1bgRFR9QivhqPsRKjpgKZd54_T_2B5WMqcjh0cVo8_VmMQypNFjbNiaERZ6MZwRiJTPzzTGlGgPeM5NzxOJLHderg3qaVQNa6QU2CpkWK7uuFrIssCRZBpApgH1XD5-pt8QhQM-VL2QlqeU3JTfoPmd8cgoPec1U48DZvnUm1DoTgtJpf7UjF8-NaeS0Xw43Cz2zQrPZVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dT-XdoGqRCW8RI7xRkI1it9W7h_6AU1XKAFe3VAatxO18yM9yrrA0OrYvuk3HNIgXEzy2QtNxBkHIKiVNyWQV6XKYW4tViUbuT_P_Moqf4ka6cxG_APyynDa9aoxK0pvgJpulNhoCSAXKr4IMGLhvO4Uf5zKdR4igIQMJtAcUiHA_kms1a1nWMLeTUDOwT7jZyNeIK1A1m_aZut5CxVYkqH5_gIs9ymd1Wqj5coKytil86ZWQ3Plf0ET9p9s-T7B_FJSXnZmDF-uhWkSYclu7V2zWNyGFUN00k5BCRibHoeRrWMR4YoY1tgXEdnwV7NILnYrrpoe7uDqvF18MFLHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=CEkY7Wf4K5ebApwuHH6P7q12ELw2t0dqa8OZG3aoX0SXLhG-EZ-V9_D5oy4GAN9YuuOp_EHwAPkDo453qKhVCntctGOc29Ty2o9gSwMlANPO2FvJK2h_kK4GtQFvQKvizu3_xaSAodbms6sbU8I30o7TP_WXsNSelZ1BkEzqvjCki6A_RBqT0fELlBZDndQClIQB4Z_802PkA2VQVuD03K5QY4_090DTU1MBipbLuJhFZbqQ2VSMNcj90p0ODqzhONgb4jHx5anSk3Qhjzx6EM565mKFqez63EDvk_jmPYKIaTiv70WfvNDzTd4AADD3B4D_WMpmarZOB40rAdDOcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=CEkY7Wf4K5ebApwuHH6P7q12ELw2t0dqa8OZG3aoX0SXLhG-EZ-V9_D5oy4GAN9YuuOp_EHwAPkDo453qKhVCntctGOc29Ty2o9gSwMlANPO2FvJK2h_kK4GtQFvQKvizu3_xaSAodbms6sbU8I30o7TP_WXsNSelZ1BkEzqvjCki6A_RBqT0fELlBZDndQClIQB4Z_802PkA2VQVuD03K5QY4_090DTU1MBipbLuJhFZbqQ2VSMNcj90p0ODqzhONgb4jHx5anSk3Qhjzx6EM565mKFqez63EDvk_jmPYKIaTiv70WfvNDzTd4AADD3B4D_WMpmarZOB40rAdDOcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=B8w5vMcvsR7Qz-sdS9PoauVgMq6BFOKK1V2OwzlwJ9z1dCo6B_aP0_S9f17fI_pTu3kdLs6C4Yrl6CrPG6MMlciWwbQzPwBonvlGy5P-1NUCRtXO5RgSnF-waAp95IR-iWLqFJCLCZmOxCA869re9b3vf_O7X69goHa3AYNBXY1-7g1evvLUmaKgW5flxJgEsdntOSB8kEPNJcUkq_p3P14rFYgHx3LM6L1iWzWO2OvnspOszATrGxDa5pfs7fHEkrjcDpOE4m0Y4-w5dlpC2FgzGRXQeoIUI_OZ1hFEZflH8goDCySeHFQVM-rz9m5m7wBeBF2KV8GZMQ4ljq7CHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=B8w5vMcvsR7Qz-sdS9PoauVgMq6BFOKK1V2OwzlwJ9z1dCo6B_aP0_S9f17fI_pTu3kdLs6C4Yrl6CrPG6MMlciWwbQzPwBonvlGy5P-1NUCRtXO5RgSnF-waAp95IR-iWLqFJCLCZmOxCA869re9b3vf_O7X69goHa3AYNBXY1-7g1evvLUmaKgW5flxJgEsdntOSB8kEPNJcUkq_p3P14rFYgHx3LM6L1iWzWO2OvnspOszATrGxDa5pfs7fHEkrjcDpOE4m0Y4-w5dlpC2FgzGRXQeoIUI_OZ1hFEZflH8goDCySeHFQVM-rz9m5m7wBeBF2KV8GZMQ4ljq7CHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpzjpV70M5PkG9tM1PhB3IeYSK-rBlQPtST2_0h932WA3jrUqwZNFK26EcKD2zyhuxHT_-9CVM9PKF8BJVfYw3b90hWu7BzFtD_rBV0EJNh5kEVkKRiCrcKRXCUqds_o9NSMwqvHD9ZPRZUVoY8-QNrpTulgtCwf3Ld9Egkq3WFYUMVK72jmsEhNOiV6XfOtl9TgXhdO5a8MqFKaJu9TE3A9KAaIDMqzx38H9ARiHs7GjRXMil_hdRkCpnsp9BziMSWrLQtKumW4Bhk7B5dABpRTC8E3msbMGwKz3qs9eBFlOYIkiTiiWxXII3zV3ijZsSBu3PgqRD8fURO4hUmlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOpoloTjuuNa7wwBuscF0wgherQTMjoUDDtsu4yLYIVlH6_H7r9DjggjjJxfsmQ03YFKI9ymIY7mRveINDe7zKtFreZ3mT_fezkUVP_A-uSyNQ_vufwgqQknCk04bMo27SoqPl28KEMA6ZhuUebly7qIPw1WOy2QL1KflwjnlZwwW9I2V_y5ezXe1BLAiZeDBG6FIq_8iXvb8Fm5APDXNYQB301fxUWimk8WAEeYygWCHbRlMnhuk6KWEdfxNryrl4nsThiGm18tpIUP3MKKr305XHwJFQScFeYo_cvRyOifAvqyGvtiUPhV9YklZVpHWbd02NWZJBdP6VCjuiVgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuJDL_WWdYJhH-GerN1_E9cSEq0g1zU01iaivb_uuBDW8jz2s6vsnx6uCAUqJ37rW7kmIflAvYMs5c_8Pi1IiGPmqxLifssuC6cwMpnK-H7oRBpT8spV6OMKtDaY117XPlY87gUYopRxSrMbOWKx-Lwk7NKfxzYFqWqsQZJqXu8ufYazG_3keAlNLe6K3oCRpK-ocESsM1ezk1hlIq6nWZqaMQhHkLtkEKLD6b6ul8Pq8nVAZBxWnJoPArmpxV3zAUNUFfSbtQN88PjHjV211R3TGtqJVKe8ZteMOy7LupNL145snIinQGRiZocmPHYtCK3fM19lQkLDF8Y7UIZVEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnIw0ecigWBx3Uogfw7cupGrAVEtHhbruH_Em4NO2v4Wcdms4zoZWADkUFFZnIIA9UtOI7vo5LP50JEHXKD5AI9DI7T5uP7gzW4BkbAHbPs_EFpFak4TfOyOyZrHKrUSTXNrszTo8ub6OAEV3_dVONZ3vHMIn-mWydSptVBnEZPe3ADZYAepMTWFIZHT6kUCId84EACcOWLm8PhK3lO_MjAUFNXy_NQJ34SqGmFjvIwyv4qhz1fflfgxD8U5vNbweF8X3YQfFEG2zHZwDxq_frXIVM3BPIHUS6h1Oo34UbkKZ3qXXAJnUFcjCmrauT4mz4yuh2YWVUOvigK2x-XDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dxt9H2KlXGyvvXAC0TnCn3VQ3B-Wt7BZzdgZYS7NEF4N93oaTnqThjeWUYPaqhkJeDhsYFafoHWM6Pcz_h4KUTlzWAQE5uzEujFdapugkIVLw6o2goe0-sXCORfJhvyAIfixYDXdKOUI7-aa4JjJNtRyfGO5zAIY021TgZf4dtL0g9y1i2eHn1JdY7WzyNFBTTvpna-FZKKI7DxV93aCHCM_syWjyPmxSfm5f_-WIxZKYJghcGJP5b6wlKe4jLGsW-dd0feHK1LETAkomi3GleFPtRTHf4zk2tavVfsXofox4fcW3X8z5PvkR5UX8DYlXVpPaBTpZTz1DJr75vw63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4qex3EHXGoiQcE8tHOfSciGGzfTylqWnrKRES5XGEzVLgd_H5ap6DwBj9I81DR4xTXVZPr6ukodljZ4puWFHDJ0NVp2s5SYOiPrFMB4v2KiYw-LH-26ZsENF_daukt1wDekwR-uCqjXiNF7jRM1CuQUI1rRuJ5QsYtCvzhMrE2kF3fFoQRNxsiPAy-w_CF37u69ShYv7xH7SxGQQ5OJ9PITQ_yAy-LKpD0W70tosfq_M2dvQhVWi04kTJVzz_saU30JE_U2JfooMIna0BS3vGNZibTZ1c88oMVpogW-CWw58efJdtiXj2C7p4a7FMJCnSqLUmn1KgNqo6zhtK4fKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=DCKGs3cypv2SEOCf_9hbHF_TM0m4lvaUYqpSRrdThuKscRXmaJmnvwQ_4v6-x34qyhluLEjGolliuWUl6lBE9q3l65vfBdf-yIkD3hNuEdXi5x1ADSapj016OFeajn2na1PriNd0uBxzphQPxFEdiDBcYoz0A2DIU4N0-Xt6NGuVOSbkQUE8jqu6qFFlksqcQiEaxo3Wz34EjFgc8ks_GLN6PeynyutydbHVNUBjuSKYeBqWw1Zam8u6yKhqmmouP_ut9KhMzPnihVewifP7fl1lSB64ji8o2Q8sKe9_O-pKk1aoP86OzXj1R6D1AbC0AxuRV17pgLDw-hve8baVmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=DCKGs3cypv2SEOCf_9hbHF_TM0m4lvaUYqpSRrdThuKscRXmaJmnvwQ_4v6-x34qyhluLEjGolliuWUl6lBE9q3l65vfBdf-yIkD3hNuEdXi5x1ADSapj016OFeajn2na1PriNd0uBxzphQPxFEdiDBcYoz0A2DIU4N0-Xt6NGuVOSbkQUE8jqu6qFFlksqcQiEaxo3Wz34EjFgc8ks_GLN6PeynyutydbHVNUBjuSKYeBqWw1Zam8u6yKhqmmouP_ut9KhMzPnihVewifP7fl1lSB64ji8o2Q8sKe9_O-pKk1aoP86OzXj1R6D1AbC0AxuRV17pgLDw-hve8baVmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niQjlVN64VdahD-o2cebySVQJot9M97IyQXpBtY-mQpIrpeGs5yE_bDxxta6G_omhgbRXrBWbhYvkM7uHjR2I42acK8DEVL-MS95iOG0gcJYE4J3-F0kIe93kxmICT_aqDBdyHLPseXKW6Px4b16n1VQKNphasTyb04AVysi2JH3kMKk0TI3zIpjwqXHCAkBT1waaYgFYhcUxgPqPyssMjXrcj-nsJtrRAeKIzm8WSu5dhI-M7IspKxgaIwAoDeb7n94a2p-7fhN7_cZ-RTv8DiB98o1dnn7dGPGtbKvE_mo4k2s81X8iWT-VVgWazjfjr8AmVIwtT5Q57elkTMJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتیجه‌دو مسابقه امشب ¼نهایی لیگ‌قهرمانان
🇩🇪
بایرن‌مونیخ
2️⃣
-
1️⃣
رئال‌مادرید
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
اسپورتینگ لیسبون
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbdP_7XADKPD90uXDzGlJWtQHmbydrej_llWuqHOaKTl5lIoJpNmJb1RVyqZzzd3x9RkTAA2BnEYMi_iw3GVgM4HVF-v9DI0okFoLpmhouNh0QFLq-p19DIwzEvaCO1m7mNsTg7f3BqRCUq5K4UlYD-MDuDgafuNPP3W-KRq-fLtGGRtFUMJb4QkGdhjKeCVZYEM_hbvuMa-EO-Ce0Scex4TTNg4eo-tJb2mysv4StvDyYLlagOLyT0e9FkaK53ybGpyNdFoNA0LG4qLpajHVX_EFwff9pHIRIR2kqxBsSVb4otfAqaHI5h0myMNEBlM2DbBcrx2N3QzgQHflCI3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcz5aq-IVEi8TLpBPwJTnLIweEdaXYb56lX_YRrgPd6pdSl9PFDMkuQmqp2bXctufMP796S1wTrwJnFfh8BNeKjmZJg0TWuSU1buxmtB3wGiKNAMohao_EuTXaYC5UsNuG1r1C3tECVMpdj1jOmj4USWdjntzprTqDW9qGgCwJahVPoVIBAcGbYJ4MaRs5KY3m4SWZ1c3S4Z_lm0jmdUbovn06kY16KrRlCtiaZ-vdAiOYolrE8GeVOzzKHuUSDPNwm5pCMUzQ7AtLwDxja4rjqsU25LvMfW4QNllo6wXRR-1exuxOvAlMBgP7pLj65u9n7ZmW6uLjW9u6u5Cw0Iug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns-cNNcz7AUiVkYmQKbX1LJrWuVdZVykGlqOgDO88VmbDDFyE91283Y0_m9DuNUIXsmTbYDaUbB7YpGpHUcdG5H2DVrCGQQGXXLRcrh-rmKSwFHXIcRblwfzmD33HXqon_FzX7obGB0f97NdABa6PENntZSgo7o19y11Etu7zhKFQ9QppeMapYyhzUCXijCIqkYodO3R9vft9nyvVJL8VNnIb7sf6V4a2Ynkfp98jup_ONGIqBoFisIDPZFhsHVupJsiLH0vfq5glEosqyDWSWhm4_ZF9YNoAbb1SneMuk98jafZ2BXOPjCgI0hP6jZr6sQWdkzpzLD7PV6UTwJBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMeKJXjhqUm1NHTUgqAKWFGATeAjMaIf3aX_Vep1SDpS-EsLlPXhdZbpvzGZR9UYlVYJJVe1Cz3IkvnkWXxJ-Lxno1QkZm1SN9VXKUFICVt-C7q-SkO9UAWusiq-wrTMuw25eNo3Lu48Th4wKUtUWlH3sM-tsjgXAMQu1CpvMpXUx4433CCD_ip_dr1i1gOOxmJ2QzgBQE4_8IzVyNhNnPPZ21pcYtDxAzwpVwB27yh8pSG95X-CpMly42y5rP5x5TLZNpoLyH6FgZMWfwgmR-jrY1iPy1rKa-A7KWBAOXqzn6uOXw9JFHJBWmjMMOSrz4xojp5VCUDxL5z1oLusoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZf0ekRief_iI2cKsQrnvENmJ1AAyGVuFfLFDCkmOAsDw-CyGqd0g5mLD4oveyzMbtGTbpRVT3qD_AzjrJV879mcGoofW5TwCR2TBHT8R1ureQlHsJBVDtdnXzZAriPd9aWxla5PfNaRzDX53vhFvy-wIO6cOm2cJMXso7YXbF1u97q1P8o_A6xKt0CQfeuIFPLR6tIIAI1ZYNCD6NGUu8EnoTAIEUwdU021oDpfOIaIF8YRO1z5fOPvE88cxBtAkjsbK_RzNmPAyzruXrvnY1vWT76ph5lD9a1ao53wsqETr7MvByJ18t6_vy_T11lymezn45Z1T_nzE1_etGOWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awLcoc4aQOpKaIvXyA8I6eqCC4Yow8fK3ibOCsN_Th-Q518PIjVMFT5Es4azu_IuPQfBtBrcDK5b2_Vx_nmw-hh3h0B8KPcTUwx2bNmnCKi5eoKrFmpNSd-cONOXto4Nsy5kfumV__nc4hPHOk9HGbkwbQZ_wgwCQEjWtDWlf-VL5FTdJVgpo6WEDrIPYdOckbqGxwIs_n34wre0FoaCUf1zBGg5YCGy0nt0g2WKnEIw-sUmbzA3fAKuxQAX5sHIKHyRbG9Lhav0_eghTFdrPCwbIZdM_lrIjhoGhB1g9Ah4RC8Gqo4ZaMoAR5v_349Fm7z-925BABlu9RXoNzHJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1OnulOqYfGrwTxfM9rRAglr2o-DY0QiTIrpcYOuYLePFWgGa5-HCtkSeWUYP4zo3z53GGd4Pijr_-S7mjQ4aNOrdEi0BqOaoz9qHWkQt9njyUhjGgQ1t5tpWD3Ol7b2U9eqJMTPwi-9HlQx_qaajerbqX02V72iP7kEv62sYnB-9NOqwXcNAGwXpQobE3jAlpZkdt1WBxvLgealIFfmn0ZuEZW0ckXHbw6gEcCE9yXQXImfmKTgCjfEBBmVEOuWXVJG2Y1Ix4OlxRNOl4x3UPvAxVt8VvwJul7W8Nk45zrPYSAA_rl2ea7BJ5jbsKTmT6rUImBhs0xzzTmgle7-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
​​سال ۲۰۱۶
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۰
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۲
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۳
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۴
: رئال مادرید من سیتی رو حذف کرد.
🇪🇸
​سال ۲۰۲۵
: رئال مادرید من سیتی رو حذف کرد.
⁉️
​سال ۲۰۲۶
: نوبت سیتیزن‌ها یا هتریک رئالی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22009" target="_blank">📅 09:55 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22008">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rimrux9twhLXyHwoYma5HJiB4QbXqarEzpIo37see5lVAXjj6FcGGbqyydcl9kz8Zugt5A0fvl8m4C1AzCsGqfRJuye04vTMb6OYadOEA3d-2wbSN0aeq_fntCI-lAaG6Tl2NKk_58Du0CTwyuxDpum-T5aOPzaVIb2Xl0cO5kT_RAdIygq0EAvLywKRbtwCFBxjtq-cIHz4rIOXnlvEtyei3elFh_k5GdJK5ZlL5haQKjnOo7h5lW3wtsKXhAIQKmUiwEtndDYMD33DcJl6eNcpkjBwwkQ1p_f4f827868adJ3uwFpAwqPvk28rlRY93PUpQ1q-_hL0F9ikRC45tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQfTZLH0UGhMzql2HkwEDRbHg3bDPd03UYK4ZjsTfmoUeNZjqBzZ72ltJVxQYzNjm7z7IAbjomfq_qnr7nWHlC7i0B64VHRnCeO94qa80MlZ3IgxcDeWaHgfEmiD89al_d82lswx5aRC8XyovkEIluzpsb0OewDbKotAN3H0YU-FWNWDyWUAnBwPtqzMw-WJU3JhokLVDhhF2EVQlQJddv0-ZAtTw0LFfvs8ujWMjX5J6ELemhlBQTCs0FktwxFtbpG1EJLIKptQbo1MKKgP5AL2QOX3-qIorwM1HwWGLasDt4jrtA_vQByDGTWvZGOTqrBt3dbDOOjIcV9NY9s2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرانکی دی‌یونگ کاپیتان هلندی بارسلونا به دلیل مصدومیت از ناحیه همسترینگ یک‌ماه دور از میادین خواهد بود. کیلیان‌امباپه ستاره فرانسوی رئال مادرید نیز به دلیل مصدومیت حدود 3 الی 4 هفته قادر به همراهی کهکشانی‌ها نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22007" target="_blank">📅 09:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=TFKSBy--W-ACbZQ1HpXxqvLp5vun-SER2BteY3zfPE5VrepSM5XG6OfIm2zNXe_6kN4Gpa13gLFuFe3gRBkv0Ah9TsqSd-ASg2REAiNlm7nvxQ_dWNJhmihA9TFosrOhDeNPMi7kpM8s90lfGaQAHLBwi_B3NTEZO3ZCF8HwTGmmDXD71EUOYU5e5aTP7Q7Whr_QPuOOsbOQN1GPb5St-ctQ5ybJVIvJNfi80gE5ewuJiWhVG5K-cOFP37Jr6FXxOgn8yG_EZRvR7ieGTn511TOSJYc4mdrkju1pIkyf7FUIYG3PQOZl6DEjnYuAZg0i_S0e0xBre6oykBddsWls-Z3UTj5vN9xMSbWu0is0MFIeShaknHEoOsIBZvUOr44GD6wuvoUnUNCzst8lcJVIlh_7BIJS9WEYr3NPBS0ugV4Y5HH_MioQQymEOVuy_jiKZL4CZQCFsx6NH3G5dQpXvCaTkk6Onzq0wEkavsVKCi5cGIVxL8oi5E7jKqeu6XKojN8k4DjqdRvm11HdqlTcTxK_TeRhkHAuRF63G0oeR7HJ_3ewyl1q4erg6TpDBHMH7C2pBJ5MOAmOJ6tT9O_AaApggEVn19z-JMlD6Dj8m9Y7QiPKX-yC8n8oDDmTeDHf3bksahbCpQrRkP0UboqPBlgcucXPgjTRY7r6VGIEMjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=TFKSBy--W-ACbZQ1HpXxqvLp5vun-SER2BteY3zfPE5VrepSM5XG6OfIm2zNXe_6kN4Gpa13gLFuFe3gRBkv0Ah9TsqSd-ASg2REAiNlm7nvxQ_dWNJhmihA9TFosrOhDeNPMi7kpM8s90lfGaQAHLBwi_B3NTEZO3ZCF8HwTGmmDXD71EUOYU5e5aTP7Q7Whr_QPuOOsbOQN1GPb5St-ctQ5ybJVIvJNfi80gE5ewuJiWhVG5K-cOFP37Jr6FXxOgn8yG_EZRvR7ieGTn511TOSJYc4mdrkju1pIkyf7FUIYG3PQOZl6DEjnYuAZg0i_S0e0xBre6oykBddsWls-Z3UTj5vN9xMSbWu0is0MFIeShaknHEoOsIBZvUOr44GD6wuvoUnUNCzst8lcJVIlh_7BIJS9WEYr3NPBS0ugV4Y5HH_MioQQymEOVuy_jiKZL4CZQCFsx6NH3G5dQpXvCaTkk6Onzq0wEkavsVKCi5cGIVxL8oi5E7jKqeu6XKojN8k4DjqdRvm11HdqlTcTxK_TeRhkHAuRF63G0oeR7HJ_3ewyl1q4erg6TpDBHMH7C2pBJ5MOAmOJ6tT9O_AaApggEVn19z-JMlD6Dj8m9Y7QiPKX-yC8n8oDDmTeDHf3bksahbCpQrRkP0UboqPBlgcucXPgjTRY7r6VGIEMjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
​​
مجموعه‌ای‌از بهترین‌کنترل‌توپ‌‌های سرمربیان در کنار زمین؛ دود از کنده بلند میشه و از این داستانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22006" target="_blank">📅 09:02 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22005">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNPJycQBSEHlJ48SSnsDMczEUdS0VQYCxihWMHeN9xGoGGW3IrV9pdVrv9gPiROB7kgE8HMyAp6Bn7R_3CDyXCKh4grzOzZ-AmnG8jfeslqdcRXH2B9-Us3hDEY3taL3741KsmqOMHYVUVmn9MwTqaGrtf7o9LxinBUQkbSZ-0MucBo-zEuqxn5GwrfLNq83vQvo7NzpRpGkjBX3AJQesTT4w2irUUEiu2Skb9eJJ31G2DKOcnkFlN4kee6XQWcXNqQ-INxiZfQ7kOfk5Sc2II7fgaMcucUYmZ-S1-2f4s6VzFQPf9QpnMCz3P3cbemw3JJ6L67P9VnmJEWkcdyqwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBfTO-urO7cELblYcQraTVZ64iWLHEwZsff_H7ttb4asC5IxYUlAZjWaQDKssdSj1yNvo1CM-2okF6QMD_z46zJTQkhLc_9PhYZOr6TXV17JFwCZSh8ufuauUrSH7VgEEiy_IugpoRa5a6csCKeyG4vGvxdABejXTCYQYTRUz1tCCKjgzd-qpMyHkI0bEQXZbZ88G0YXAaelu25mhMuGUjq4Wjc4nZPXLM22LGiIVdEy7lrHxYllSr8vlnW3P0PdBf4Ns04S_auE-yzwZY2NXh8HKqSImwCYK05tid0jlohX9dhpC6kLkotDFpte200QmDyul0ekdf7W3XxreSjg2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-1Hrfo1wc8srNcKp2TU5naADnF3NgKFu_ebZol1IofyIlQgV82Lo4BU0LwgpcR3YU_jjwPUnjAn4UUcRbZiu0pkvbquZMsEmLdQxfofiJOovrqgiSkP8ZHzXKqkxKaao7lnXrXnc6xpiusYaGO4RyWVWjOoqhLgilDytuiXcklz8qIyEEJSxM6NpChV1yJe6VwsIWVUS2su39OMl3qx8Hi3oz4UeOpcw95UdK-aYk3kHySl6rrvxN8q1MwP5HMVSgRnrFHZPyzNnKQHjhZwu__n4zU_cf_jr61-92cLKKoILsWqQX2DCYcauqdWIrsMFRTH1JWYWZirdAMxYOaIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLELxjVDWgg3OXeZvZLp5Whbg59zET_YLkueKFMtL4h-22NW5mjwSbmdjxhEZjocjggTLyHNqZ7elxdBQfLI6SaTIekJgA0Rou1E_zWvC7seKsUqVxdoC-e0PneTfkaLbZ_Xc_Idl5tgEJR-5aDwMxMknS8P07k5gQra7rwQNAROW3iTolk7mVSvrYc4E3l5Qw1XmZ6qzkPPM8KgI1OMtrh1JDoMCdQJ2EdTLq-5-q8Xr2iXm6syoZ9h7TefGZLyqn5hbEcATgrisTDMOAKPdq8u3FxjLQ63NIAVriyDqLRWVCEApj06WQ6n3R48rK7XJegwC8ufD8PtAtGIbudcfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/22002" target="_blank">📅 23:57 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsrKiWYlWfan3BzEn46ZVZM5vMqC8oGMY8EJhz5stljBG9flDu95qTWIh0B_VD2lQi-3q1bAqsvql4lhpI5xQXSsmVewg1zRyf25LBYNI6PNj_EuvvIMnnzAw1cga2yNmNYkxT7C8YIIQwxlziMozvdRTpyCZQq1D-cyi6yPR4X1hO9nXa6N6dAQA4cZ3eAmn4ys427OIAD2KI6dsC4S8y-wt4Hd8UhWPMPJG1mZazHcfjc4C1IVHz65L4g940X47Ow2Wr7uVguvx95dr2d3gIlSt1gPpVeE7X9GqQoKh6sN63yjl8Bmb0HVB0-1yUNdAntPZEqbluQs5__lmorNXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌اوسمار ویرا سرمربی‌پرسپولیس؛ سروش رفیعی و امین‌کاظمیان علی‌رغم‌حواشی‌اخیر به‌لیست این تیم در بازی فردا با ذوب آهن اضافه شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/22001" target="_blank">📅 23:44 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22000">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=BDXBYwUIXZZRa0hRkszLMW-DZeE_vXKbUV09OOE3Ebj8MDlslYJNZi6lsoxzwuJDOvNMQjlyYPSGTX8lBrA6c3eFkHT5RRZDHLKYoyKaMwA0MMWwk41BEVofh2dUf9B54X_ie08FHGZBEcW9ibBcE4NzAi6N2TdwNtxMpcZ2z1gSNxTFi4vdgTxnTa-a0ptkQoFlmuny-OpmswddNQVyf-M_lEekU6zL4OOODalg3TRLwKnnv6s73sBXPH-fDCVwQwUoHUmytUorpUJmAKN_onSNtubtfq4PbVntWgNq6DKU6KPuGO11yc7xf0DY7pw83RBdu7R5Ndg6YuXFNza2Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=BDXBYwUIXZZRa0hRkszLMW-DZeE_vXKbUV09OOE3Ebj8MDlslYJNZi6lsoxzwuJDOvNMQjlyYPSGTX8lBrA6c3eFkHT5RRZDHLKYoyKaMwA0MMWwk41BEVofh2dUf9B54X_ie08FHGZBEcW9ibBcE4NzAi6N2TdwNtxMpcZ2z1gSNxTFi4vdgTxnTa-a0ptkQoFlmuny-OpmswddNQVyf-M_lEekU6zL4OOODalg3TRLwKnnv6s73sBXPH-fDCVwQwUoHUmytUorpUJmAKN_onSNtubtfq4PbVntWgNq6DKU6KPuGO11yc7xf0DY7pw83RBdu7R5Ndg6YuXFNza2Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لیونل‌مسی بازیکن‌سابق و اسطوره تیم بارسلونا یه‌تایمی کاشته‌هاش حکم پنالتی رو داشتن و تیم‌ها به هر شکلی که شده میخواستن جلوشو بگیرن اما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/22000" target="_blank">📅 23:38 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avqhsOd_sk9JQPovRKpyJXqvQJ-QoVSMJ_ckf1g37qdPUe4DfiZhfI2I5v5ZkIz_RHN2ZMNNFXRYD3YPe3QECA2IC69B2YYFnsF4Ft1xdM9aGTyPP0EPDT13aFw2upLxj5-r8uhTen2GMJIRUrUj_kivvOW2s-dQzsttFZ0vB3ySFh6Q2I0Lkz_UgwOvHsKwgmXzvXgTpucAXwHCF1jxIufsArt0POj2pw8kS5Wx4KdCz1vW4ewwIg7Ag2iKrCZJSSgDNUEApkdLqUFpeiREIkdtEVd8wwN1sQxG9uXQZFfn2UYRUz2JQxPXYs-_wM6izaL-52itN6OMHTiXVHbAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
سعید مظفری زاده مدیرعامل تراکتور:
🔴
از سازمان‌نظام‌وظیفه استعلام گرفتیم که اعلام کردند علی رضا بیرانوند سرباز نیست اما باید تکلیف پایان‌نامه‌ دانشگاه‌اش راکامل مشخص‌کند و معافیت تحصیلی اش تمدید کند. او طبق قانون مشکلی برای همراهی تراکتور نخواهد داشت. تراکتور…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/21999" target="_blank">📅 23:05 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21998">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=JQIXrTqRzyaJZoEW6ydJ_DPZeIWQyV_ILouvbnp4ZdVTOLo7sEZ24F_AwoIPXoXcIXN7iIdL90OQtyHP52FISNfrzvis3X3thEh198MXFokhHvM3YWwyrIjYV7LuoemauaC48WlH1WvJzYMIyYJ50pV5s8WaD6RF9oT-_TLk20Rg183nOU_kJiqMxa1r0zA-BlVHhm-IhkqyWOUlplOakAYNnoZswWYSgxeCXQznS7EaY-77y5TAT1OWUKR6I2UmXEdWy012qnx2Fpr040YE-SR7PqYywDQCtxzo2uENvE5syu5kOScCEeBrmQ1hHxDiqUEg7MCQ3iQQjl1drUsM_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=JQIXrTqRzyaJZoEW6ydJ_DPZeIWQyV_ILouvbnp4ZdVTOLo7sEZ24F_AwoIPXoXcIXN7iIdL90OQtyHP52FISNfrzvis3X3thEh198MXFokhHvM3YWwyrIjYV7LuoemauaC48WlH1WvJzYMIyYJ50pV5s8WaD6RF9oT-_TLk20Rg183nOU_kJiqMxa1r0zA-BlVHhm-IhkqyWOUlplOakAYNnoZswWYSgxeCXQznS7EaY-77y5TAT1OWUKR6I2UmXEdWy012qnx2Fpr040YE-SR7PqYywDQCtxzo2uENvE5syu5kOScCEeBrmQ1hHxDiqUEg7MCQ3iQQjl1drUsM_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
مهدی شریفی مهاجم چارچوب شناس این فصل فجر سپاسی؛ استاد گلزنی به تیم‌های بزرگ ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/21998" target="_blank">📅 22:45 · 08 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
