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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 16:43:36</div>
<hr>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCdyUQ1YBOFLA4N6dfEO7SW_fZuWFcConm1oTJ46BUMO__yHA_Sf1oqLUDQtcW8EiAWnwIGdcZqy70R4-GbWMQLCbi8Yp03Ykwu0hMCqRLr1HfpbsVWdOwrpb4aqF488FpAnDnzJx9FHxgbVjlF8p4h9t9aBKVYW1kBowW0HCwFp1RVHhiCPKb2-mMC9uNHhy7EHEU9M3Wnboijaua3_bBj-ZMMzbmDerxt0fMOP3LZLcyR6mqsohIBexhtODx7X_lKbicoAnUvOaHzcAsa-4hj1S9Y-emSkcuc9yCgSnVMs9F10t-F1cGldykqfvZ5rMt2OACsWE0_weIzSc1OzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj-veqmFkxbU7tgEThin7mBozcSogSB3LQXkTJ5icqIiQaMQINDwSOdm-tyEkAmGSPBct-bgcDS_41aWy4Z1gFyjMAe9w3JtIZfEpiaOafYeA79Goibog1MYKJUOoZrVLGgo2ivjzoFaFN08q8-l0c508p4HRfqovj9KX1BlG8HfzJo2t84zQt01qatm6H203C-5RXPcmKLHYNT5Ileo6bKnqbrNqwPw8OSuzxOURv3FPYKMu6dQ-M3D7tsv8i__t9roAhIEVQ-zNdQgnxA-xEWiMpX2f-o6IgKXPIWb-g0hPsE1xUjHXIdfC3S39KgVZu_HsDy69Oq-vURNY4uHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThjbyQeNHqMu79xJR43-BnU0P8nGmZ2EVQOmWeUROYnDnc9anhIqmwYY07A4Xv-YHrbnwOnQIc195FTdNAerCJ0PDDvpU5TcVekW8UP7Ph_LczDCsWk6IUqll1dTMAmLglcr7L2YGu0hiOqZ6ZbMmP4qQ89WAKXvN85qh6-6CeBM6C9JrE1nAOStakbH3VMUXqiowHcQ925FeiqVp_ZMlouj2ioHi60UsJoOy1EGsqD4ZN8neXorK-YtuwjHaA1hP4h56xTnqq6QLskj37KQ4Xp2QKEb2iHhyqmpMF72I6Vc4XltHoS6-2NfLUyx_HX65JyIzHeAuRD-TorGmcP-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFSjT3XneP1bPb5dmETDnWqc63IixHhFLC9juaNCU-LmovqXwr5DtuZqav6dW0v0jIYDNcCKRwehe2n2Wp6_-h4qS5ttYquc9_JGI1h1VmMtdDbFH84vvqPsfgvpw1xrai0WVwH_h843-cemfbyEZDrIOgIajPikDBul_YYel7pS5DRqWiTZyxDXgyTSHmKq723LixhHbpzPKeD2IqtqOfbVGads1kqXsEE7BLcFW0VcVhstdSRqReOVZ3FTFRRIN9KkNZddqWjS2PjXgGdmMsG6TRDfbJtKnEt_KHN8eZI-UFs5T8zj21tG8VlhXxAFPq5_1j4eTJUdcAwadyL-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr0PnkYnw6ozYfDw-hax7ZMyYTpCWAmjudQoCTZZ234poz_rZfIU0cetvhm0ayxbtRWAcqYlokn9id-5jBRkYz4Kvbs5duEWSAw2l2gxlacP0Zk2VA2RU6x85-ZxoveAl3QNsZDLR_YKTFaRKvMqkM51i65opFxOMbe9GN2qF2qpPhJntB-RALhybappT94P4EjcIForNvaX8L_2k_hkbmdYozgZZeRceruC3-ONhTvfiwTQRAjzApE7Ycz6DFllZL82Dbs_L49JLPcRbtSzXPVJo9DHmZVQlk8H-zrpHqp1EjT6t0MPvBQk6ORb6LZ_aZZjbyCsPyYEsANxrmtFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGUYJYCeg01_GrUdQ2c5nCK9HvC-pDiORrpwvhatRkzu4zwz3u6JZxXkQtHYwKOSlKcKPKXuXDWbZVBa8TLdu7AYOj_L0rxCapOY7aOHQjcVw8HlI1ro44Os2fVJ86ony9-6KFeUn_QNOXxI_a2SFjxZeS2MEvcFdbpj26M9UYz2yxREerAR-82HLhVN5QcGt1vPDe95HWS5Xe0v8SYk_kHH1oufabHXP0wqR60v3yjC124X8SIZkVlxsQlvtii3APihfJWP2mKPVu1Q6IyGa9y_O1NdCRWph4oUOfnrBqzqtj8Yzwo1j-84xt196Wr85QLzP4wWQ6_mg93UwwoTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKlcARNib46iBTfCqticAV5QV_CBxZjumzVuQ2t1KjZAn8bgcAx98Tf_oFBU7-88rVoabYBeKqShj-mjlSnwdFajGq6ud0G5MXOa-ds9X6LibCrTYJyvI9rToIoWbi0Wt4Y6fugB2ckk1m6pFCYP7JQUCDHmZE80iXRditjW6s0n3-wvCqG3U5wzy_z_kl4vgNZJLquOoHOEXs2y33hGz-VILTuSP104a9ZfUNuSRz3xo8HjZEAgYlhvYE0rtu9cSVejESjGi9-ayRVP6pwGscLqPj3Tj9BIVemrxUYbOvgdhZWaDapA0yGxfS99NEuzQShu6437n0c6iwdpq8rzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv4MxdOj2Zj2CCoIwW0UayljEpy1l_FIzkgvF1m8NMP9o2vWdoUfNMzqy3LW1LmK4CuvVBRh7vhJIQLM2tCfrXi4adUSEp_Mxcu6XmHkB5iojTn84tL--oxZHvrKUQ_8bo6ktiSAFYCDQsioPVGkqzUG-BfTqCaBmyUB0XFsW9xPSQw7oxLx3OJ3jHUzoWtovT8WC1BFlvfAItZOBblW20gGuY2j6nc0M8hU3BCtKTLrmEFSppntYUAYwrSpnkHTum8v7Jg3ufn1UZdn8GJi5UGhmHJkh5t9jcEFw53wa20JBs_G-bJYs2yylSW6RmZjXlNuZR55pCMJuO0g_DZPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npPOJgp7U5iCQFk8H-KIe7EhRjpoXTwL_c_V97zfpjGLRXrHO1tXpIvi9ht3HvX-00s-2fUCIaEnHV9VgTj3rqxuOSEGY1NsE13Wxg0FIspBtjGiZwOCVnKbWEKE0vR0Bd4mumXne8DK_avv6SHupq1oP2wi_X_eKBwlYQid3yU5bSF2tukBeObMAFw7OJLJAij07yht51330nX-wjwsH6NTsshIed5I3BpeiT8s2jnBSIY6opsX3sKwpfmVBU7SmYjwhjQ1YzcRG44pB09IKqT3T4rDjqJyPSDaaTot3SZOTUAigNBxl3Vqtf2CtLDr-v2_lWqnoCNYyBNYoF8YnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OggEIESIGZcrbGqiEhFdCecYspuFIfg2DLzN3xOeHEyaRz-LtmXNNzxHBFZquIFGvQuq7u1yf7s1Q6h4fWITm1iXDTT5mA-vZam8RS8U1Ui4v8rE8kJq-AQB0KW7YklvRUPdUVLOzVUL_UmyEuu7X6-n0IvRiFcpzccBf_rvVcyumEW1viGfXuTlO4Wy2tNdPznlaUJHwT_xSC0K7gKqiDQiLo3Ff78ezTuGnn6URSf5EE44VQLUj24ktLacKRwcFyeTqZokRZ2Nj8BuIOPRO5Pw14aBDjPJFkgZWTogq2ZholoOnMkB6GtE5l69w19VTWxbZaPhaVF4fTKJ8W7oHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQhr-0sJjaTSxCmfVRgH1vIFcN3IPE45MC_a0W0cdt9Bd-SUmB_H-5UgraGhlMXLGsselm-xWZ3-kbUlG6Yb03CxrUM-8bzzUQs3yH0otcIriCBfEtokdUZE17zvOERiPw58EvSLxkM8w4Ejhi9AP4EnHXSLomy-8dCIFwgthKT_2aeGAus2H6aoTOLnndS0kiSgrQCRturFd0S-npIXUO9jdearsiJYQmZD_aKtmf2PApaAjJlT_h5U1hlp5JIaNAiQQSOx8E3Sm-lbPYyYg5PuxTwKU5xTvCT09Ae_4lqbBVnmbu1kPwMEm2OoOEWis-8QEBX62Fg_yU1ijv7cAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1r1QXNWfwJBDQygPHRkaQKBpoXgbgRt_yLlQ1TOvNzj7Jcw8AND7Ni_-ZUCA3UDUkQC6a6XNEyi4qcQMx5R5XpjY0F0dyipOABfp4WHoaKe47weQdGY6JzbIR9XrGZWP_FBCHyna7m6s_Z_cuM5T_qjR4y2h271sRO_nWOhSjKysxFWNTyT2JGAPRcUfgDWYA0mRnHwmaR3e361yufRPDKJJ7t7zMRpmM7s_UxfjCrm-wp1-ZIZMKnsaeCcTqJN-midhCm6gn3N8G4VKa61WK8ssd-wSKsLG37YADfBuPiJF0T2Nl1iY6MF5zt152lmjFELValnhvBG-UVw6QvV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXAWllHg8Aw9QizZY_SYEWfX-YNr9WwFbgri1TyMIVoO6_dcUdjeobofzeFMSc3LNnF8WcMQjp-on01r3aVZNbr1uJN8KwS96d9SjC_Wrgeoe8DGqlxfwTXJIqyF799aPzjTuCLu2xOBHvF9f_ieBONlAsicjujmJRn9JQXwV_KmpieeLTkXvyi_iFHAVx-ran_0BogfCNgxOZ_dwwmZLBWATejxjJxKCRJ3stkeoQVXd1UaTJH1-GyS8vJnZNpu8OrScWqe76LAwmzNSIMq2O5Vze0EFDcAJLRv5bob3VxImL_tsZUSnQtiyWa1n4eZczw_clyzFOfTlZEgwlBirg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcybI1UjZOxT9fi4hAMImFbnd94GKUW4kl-kjsXTHhv5xFV7D0VlxqtRbTF2Le3mBOK_-seNLfGh8AOCAqFtx3XRqwxVhIVtdtjQozYPw5ugVx8eMa0vjq3YAx2KuM9mMVl6_gmHAzBCHn-IeIXHO_4NoBaj3moVF1DE0ugPdRRoNLzPBUTcUOR0XafxCKuLsYmKeam4ki1IThfKiWc_R9cZQdxkpvMuSsyzZOO8YXfgppx0bnNJri-TEwB-9M68AKpF3fAgDSyfTAo1vOI99C0aHs5Mlpfik98RNzy2iDM29edwpLArVXnBPw7pBOUmAyi69vsSlfb0NGmjstk-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaTy24xa8fBDvDA53jyhcaLkqD7VdLbLlP9uEybVVXwNLYyeCf6M1HUnyQVxQJp12pWBcWIqlEvjT5PIgQV-HfAIgwUqHeBu1LghGESl34TZV4S-CNg827e_Ra5ENgBxOCPaRBTSLysSJOleWxo7l_tb4hH-EcVMXX8QWN_4MIXkkZNF7nu7cJXlnJsCjuNKfcb8P6ROhI3J9XBixnzENAMXAf4jR2xY6Cis8hGQyYQEhj6vbSQuHaA1XV5RDk0WGe-0G-Ji_R07bGgUK9W8Fhl5li0EpQGPb_77JwxsoyoPDdjUP5vhPfsM0tjqbicdP5mxC80WwI4fGJzU84M88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKHuhQmoCSl9gO0cGIoFTiWB4UYy3-P1BH1gRNkC5MPsUqmNuKJ4lyBHJPUJcpM8_WsYv8tGONmbDbQe5OfApfs-v71Va3YbnRl_MvCIjY9ztXeHqdfG4y66NL2qPWO6IfvCV2SSPJeEi7e9Jp9H-__Ao6Qm-05eEnnCaV1uTGlJg0Xs-oySEtfb6VkBmETdhsbe_gP7QjiyAx_4Vi9RIJKGeFbpnW_CC2yhfVNXNiBcoUBwrVK1tWZFHiOurxk9ZU3sMaFEsb4O8gb-kpGr4QyPkuXmF8mKglepgx118WqilRoNF4s_539X5HKZWpOMskrfYJoGiqbKeY2DIU5pdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp-WA6dTuqnYehg_T8ey9BMXGtErtTtFA0HOtwEZhkPsxEzTA4_ICafye-MZAKciqkrb4Fbot4HnweHUp1dh0vgaSaTARe3CWHFChGexHmTe6cmaxb4t4bAwWkCsnAJuSsdDWdLlVKLB-0reJ41fZGtT3kDKML-JIZxGrO05b90AjzYdvVVKKRX_uMyaZbi96t8h47YLfqwZVL_j09A94fbBv-Q-uFf0MQWocyvuQ95b4JV0KijXx1fX63ZEhWfKz8oYdYCGn_QTvVCnoz8YsTMgKcK5DKPhAkRCB4vso9DCJrJdtv5eiAXY6SZ-oWNZzKahOgixMiWNzqh-owS8Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFPW3HMkXy_r4loyMFwXiCAP7IvFt_eXUj8BSoAoitORr9TOy0SFVv5r7uh0JKsuodXaaB7jwGnzVkZ8LK5EUzT2nwfsjiV1HZAunv4sTgxFsMl7qKeEOyKpLJT2jzvKflP3klW7rG59eccISfIUa-FjuEYuhjepllNETpg_Va9T24ZSi_MM5tjm3638i-BE1Ad0RtgjHajcjLEkz-dIXkQ1gyNzrGYbw66CRGxHoqorNLARrdxj_sxsxrjgngmyXK0cqBZqYz4o0adNL0GduvmaBUO8rIPMwzTohI1StyvxJAeIqFcbF4vZ5wnR2_3_oZ9jjpaDyt9tQVcRU_LLOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVUkv458pj2oQzML8rJGXtmshEYqMNz3J4ehO4BD6YsUlhufBttPZ0gZB8qnSzane8YdVuhCFmzOwbjhRYxJHzqTygis_9Kle28uHRmkbkDa9Vc_blo14tqpA3BSsQxQEQVJzvRPdDxY3zr-y1Sf5J3Vbx6iGSih2DzXWpNxHbY_WvBPjQ-zsx4udL0YeoUFvDm8nheaQu7yS8My3aaYHKSnVuGlX_iK5HjJAJeqegdgbtzSlPgYHTJ88QGey05bLPpa4OyNWS8kCeU5GNnBNOOvs2hlpnBHQkigMqHza12mMEbOqCzacWs_xFpb0dKRgFmzppgq5kXxSJMuEJBKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsImseeQrVTA2SatpkVvlJr-_NOo2X-KxvtR2JIfOYVpsH1atGUhz941zvyexMEClfFqm7W4DZGhQJe_sv2MJdZcnwkZXMXADcqKX5ouXBI-5lF_b0ZeOsZyhJP2CP7FjKMzrlYP32TA0S2drUvBvlIBIv2yP7_EZAG3zYq5aDaZYd9_6u0fmO6sIQBdq6qLvjz4T72IjMt-k0naf06Mqz26hYaDMSGJzRkFuZdv4ZFFQw32HT25n-3PBW9HdNF8VbjoYn1r7-zxRcABlUQOXIaaxPybE-Uws0bnJLsEXHIoRlTSk7iXXnFI8M8vkwcvgVWkdXtDat-cEX_XtiEP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=CrPhhA8YFJa47mGD80_u6J_fZ26GxHY0Y5fJVoEQryRcUvVf2Vuu6c46dFvoJZ4PUR3jfkkxZ7hpNa0_PJGTWl4NKTrpqB-zOSuPe3zfwL-7wIyzozOOqePZ58cYeNKkdSBV_BlzU7AGEEnKxgGeD8C47QcTvs7nb79ZmZTpNupTbAsaqZGmVOlxpiCZEcAdh4KwHD6AZwmjXfeOOhyahpGM-f82-iiATx31Kd2-YRgLC89J0rwPZhHU6RoFfZ5vbAfFbEtD75turPHJ8XWo92ko2RJaJW8pMN3aPW1PBEuJdSR9KPNtnsw3I2TVA9H-7oVWEqY1QHnuzjKEa-KuLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=CrPhhA8YFJa47mGD80_u6J_fZ26GxHY0Y5fJVoEQryRcUvVf2Vuu6c46dFvoJZ4PUR3jfkkxZ7hpNa0_PJGTWl4NKTrpqB-zOSuPe3zfwL-7wIyzozOOqePZ58cYeNKkdSBV_BlzU7AGEEnKxgGeD8C47QcTvs7nb79ZmZTpNupTbAsaqZGmVOlxpiCZEcAdh4KwHD6AZwmjXfeOOhyahpGM-f82-iiATx31Kd2-YRgLC89J0rwPZhHU6RoFfZ5vbAfFbEtD75turPHJ8XWo92ko2RJaJW8pMN3aPW1PBEuJdSR9KPNtnsw3I2TVA9H-7oVWEqY1QHnuzjKEa-KuLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGbkpwsGeihYa5abN4zNS2QS8aNs9YhoRK2tXJVNZ3mfKxtD5R9MzGoFKFvqtpHLnykJeOGnxqRYvG9ZiEcphhntKRBj6NrNDXYADJgEbqmi4zmakJeCVJ3x3ZEDNAHBlMQwYm6vZ3F9e7w7mi6rcQ2x4lBSA9tQoIm7g8l1XAE38p-rUSe_olB13nh9IsqeIeLZwEF4NYh2HrmowuGwsKvsrtqYCiHUWANhdt4JV4OVUVk4C9A8QWahmBgW8LUAaeGlogORBduGtmAC8FDj08htLm7Vxpn3YRc3HonJ3dvQ7wsjjgD1YvqHSE-xi8xVbcg7tn5Vv7WVJlDqixs52Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMgcYOZoFCQIqDN5GYpImdf-v3HGYPWKyO1BAVo3Oh-DMO-7zHP1EHk7AICRXuwGvXPtxAw12CFNVDb8wUUFPC4N6YHv6tou5qIgHeBZtHqB7eqXEGSIgfKWdmvNRJb88Ljc-2zZK00NjPOu0GicDf9hd6RxMyTo7M_SBmwkHpi0-kn5TZeVJRpl6Q6eqMUzrXrD6GWOZqcZ7dI3629fSWOqTYuRT3ZJ4a7fxMTGnGFSa7R9Bp9T0mbVzMea3dCwHyA4Ty8EwUfuYXk_OB50WzTJlwzJaPj6O0jKLQ38isksnLoDGqF2ncr0DgZymJwMb5xr0AmbQdLmp9jdKgmOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuIEue7_O9HgnmgBoSx2G0VnAxesZx8-lSUU_1lTL0aIABkgGt-VbzUShFFuYJDWY9qLRKURzGxVnaQ7Bx20KpybbzJ98gdkvPjoPplTWiU5e1f1fz3FICx3_kfrt6rr51nbzYoj7tCsNm58ChbSndMFiNmRa2aj4NxEIR4x6Awnq7TvH0Sml-Tmcb3_waPoWmgu2muLXYOPHcSleh_cHk6Z6I89qCi6-DpI4e40GOrkhUZPT81MaAantPle19uHXpSVvM3lqzw48zcqULzDhJ-31VCLff7gMpZnby_MAdRyhalsEYnZdg5GFNqqLpDW6KJrH8_PGa6qWGHYTD0h8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abERRcUCyZtjLKY9edl8cci-MLmhzVef0mN8ZLaXIjfWxprpRyODq4EjL_ABaMTslR6tSpNMeX3cP3yUjpNLrrmxHtHdXnrEdDuoZ7o2TARtO4F-6tH68jBlf9K1eUSzR47qQfibhIybq3ZLRFeRFSJbBK7SriSLb5RLxHZsSrrZzaxtsXmQxPk-dwktbciCIvubN_JYwv9tCUEkPNww9nLjo6kM0yfXOEhlYWrY4PP9lyvEXbMB0ljhj2iNKzuxwjJzd4r2cC6JqCP57pZMiqoRK2fhOjktgeFfiRDiVrwnSzLeR6K1u_kGn1g_nCNC5ItN2HYhzvUmzZ5_gdra6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYYC_ttINKqjkRgrvIrOl4DcrIArFs69dhCc0AsReC2TNGd1nQb7y4daYMveCzBc6eGD1D3Ntg1VLHv3054UkDFJGFDpvOtGsWb6OeWE-RO9hydO9VNEsMN19TCF33Ywwtiaj8oqWhuzNhVZAt6mhsbPtWDSgW02N8pFurksJ3ameT2X-tS5cgfxKSEOq5jUhl_zNe1SfWQiDHr65EK6WRlzHhAt6F5KC8QbQ4KEXgVE52zMxcdKGYXIK2r-eK5cWkRL9ryKARvPMggF-OYjHf2GQYRc8rb-Am4OtOC612cNF0db3L6iRFxUwMDkPX1YVCcJsztjkz1bu72QUVQ02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Paxmw0O8J5L_h9o3Q7-KL5OWqaArhGgRz6PMXv_WL-nNSiy6MWN2omYRTsTriaHTQDyUsTDbYwjY2krqfUzdB_f02Ry8t-Wgorj66EDF3g3o2ZsSrL4nk8-5nuS4SMXAx0KnRB-YZ1Wwi3fGw2pz5IATTXfcRuDTmuxhwn4MhOzlH3xri1stDs2sKOdBfjjECK4Doqep6QC9QN_1ybBFhJoTJqzcAaDcB-oDdbJyjWIuQkde_4-NqNIrhnrznrK0nfjiEDyBTA438kvku32c7qq7DC-7wvvKHrxC1I2BcytpuWaUu3nQqd-fBD0Xfdc_u68ntpkBAFSz7ZYSxwExZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc51CfIkkJzwC3HtSSTNUeVRGOjahemTnG9Uux_MERf4s9CcOakXBqQBX6BzBYAuyY8YrwCSVo_y99nEr6Lbse72I9bHSbE5orkpEgv-8yMlI-7gNeNZjZQLHQPQ0ai50X1l8biJXMvL-33Tu68c_plbC2xt6y1G5WSRuYcsZSK-CSCEbK5iW4CTGo6LibyJWb3qSYdoNUjRuIiait14E8V2aHvr_nttqqYULeOJRE-8m6YK014eXPZTETsA3kI6zE9cPgvy5ijz93Fjhjx3-b1sDbg019HluftFtT_1tnaoLYKPrgtMFyqfb6k1FkLA0kYh88RKJN9gF81riINt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYho82mk7Bmeg4pWnpNIby7ssfg0hdSxvceXI-yUlz7mtmZueMNUXqXijRjmzUX1Of8qket6Lf1_nwNxw5NQIFb7PPviY0i3tNan8k6rm6qTwHeRK5_g4a_xsPLxkTr7B7xu3UIafsTW33PvslHEFSRVdcK32gz_CEQqOL4fXtPzzhTf6gKkrS6yQPNhPSiGrJxE2uMikhSCs8kYLXB-BCU9U2qEx_llfag0dkispKXXgOdRb9SvI3dkHn0oonBdSeHb-ofJGRfAKMybyu4zkNra405Aki0mRdFhotGP7i_avu9ccwJrtJovjHoyS8qSYNJJAZjPZVA3V0CpnAaOfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHAY5uF-6R7wANBu5oUmZsWwL0sX3sRVP89n8dM-wUq-ab6R3yxzSxBLNdecUngnml9qtXA70HffJiY85PfPeSsx4OEjxJOW8OQMP2qHalnj7pZjw11Wgn6HENVByP1TgGSzB4rAWjk_b8pwGUS28pc2NCjKr142ZkqpS5wRndtNFz_uuWpZWg_DPXi0bdXptuNUQMY-xZfeERh9-hIs2TlYTnCGcmq4GZTMhrIZioWgg1JBlUChX0LshFErEdU8gvciF2maUcR0lSfx5hoPqCjMC_t6DIZnKUyzCZFoM-neTeq0BEVaFCIzJqZ9C4VJqnSWdW7PrGhUaFuUFxemjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjXPNgeON7uzE93SSydL9Diwj-1YaW2Ab--xSt9U3s3oQC19Zsl4YXLK0wZOjW1b6O64T6ziPn3WyH_80iH2HI8L3PQrfW7V-87TW0y3888XkhcEi_InFDL6ToQGhw982hfPO1synAWUAneD9xsO0cLN82vDoN_WWyfpIJ6CPyhOryW3L-YaZ4JkCQxDnjIffz4mHQo087aEf3qziUbYhFEgvNmtNjhhWDTBOC8-reiifHwBEC3UpXS2VYSkUSIhs9WTcNpk6z_T4VsO5KOOmQBkVrNWGmWky7mNxjqm_U3L2Co_FgtfEst7NdlbRn5snl-GVj_KGvGefrgtvUj7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSQb6DBTL320HkSs3E-GbZKLE2J28cFSavFkpwVo9gbUTblRvPwdvqCvg50X262jsj_MyAp3E1aM5-Qsx9Iy9ceXq5QqRw-i_fWGrqQZVtYlY2B32UozpNqPuvl6gJt5cr2QxncvyIOvSRRmfA6JE7BfkoyWojJWzJD9KmZ1ZBNc_TZQ6hgb2NLw33lL_vMp_BgmADdwLfJs0H3ThVivTuMmUluWbk_uzJ9Rx0DSXKmeX2qclmApfKho1CqsoS1Ix-rtrZv3T3Ce_a5x494Tkb8ThW10g_jfBjNaCIRIpT7H2mwOxYVMyS3ncOyciWsSgH6Su0LkRrTuURd_HaHfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W13MF7lV6IoxLgxQG_0lqO-hSR_TUwna8uXOTqpxeedxTDxiNPHlzj3J9jiYiaGXaN_y43j4uy8hNKtn62mB10aukwY78l8sh9AIq5aJ0K6r_S1glDuDELHjBcbVCJ7-Ab4vesMi-fzXIud6swfMJaZt2RFXWmfMxj5VWNQx2sbJVQxiVU9c-SsIi1Y_BwZDczuA-bDJhAxLsMFJ2wHRrXg6lD2G-WdSv3DLnOEyO7nHStgjd22fbMdvu4atQ8t85PKN-QwLyJdfWo7DR5ad7ncekLRpYnENMxQDzkQWCVc0hsZTASmY8K2_kl47Ta4OXsQGvln7j_fDIOQqGPwX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noFg6x_SEoBrqp31FnJmagKO87fUR2NIdTCapH0vcq9sfk1TI9M0JikNN5uiGyhhrv4BgwbVSEJ8j5RVTBxbhgnAgwnAVsPs6heHbJdB5sAZaZ9QuOCyvJboZqBxJ89xXFEFtOg_N3ODWpeVHYA1k8eMFdBw3xnwTPCi_gmMvs3m5sCrzoOtgL8mDJDq6CgG60VzA4FSixSYRN2nyyHZQbr49_dGyrpKnw35K8LkUYgt9RGAgUBET2kwXlx9hYEIMj_DSMe5rB2yul3UhasI8Iq65UcUOpw8PXz5wbCE1YPcTuq4U_eWZ7U8OtyVwpJKRuB5bp-zSUMnE_pVVukM9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXC4s2NSqtK6sfXm27dqf59f3xQZ3R9TKOwabE4IYPK1_4gW-Gzh1w5wCekFEXcv0Q6xnqsXO83zMOM4E5umcS7GAVhPywoZY_tSLTTtygPalQStdwzzQRKR9hvRmSq2JoHWjKHpX_DAH0d40Z1dEmg8Dje1FqahH78QH17VPjFtLQfhUL4XQiXU9y9xqWbGBHiwVgavbmrruS3MWXaYgqc2KWcqKN8F2r_pplorHqCckeof9koN2JPxYj8mqz1WHwd0wj-K-XthTTfZM79upoQpyUxZrf9rvLMY-D2Y73PZSbmA-6DAIumwx-eV7X4S_-u7KUiFLe3NlyTiJWZZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcWrHWuptyMQsGOJTUZn-unXTkZ8RYu1Eb_l7EFekEG6U65LWhOMUq7DU-jUWr6adIfp1BGTbiqkXiaWYukWPteoYQq_qThs5Mc4_8ze5gBgLf4L1bs8FeQbJlOJ7w8uyCyHYNaqYlcScYuGBjp3pz7pjt-ZkvYmC2bkokQ3MsiGW1CeVXIYtioGGsFsuGTEin4UDu95JbYao8C7nHZeydVjps29Hed_zUjNRwGGiZyaKVcXyAQFEBqJWQp5QLFgvCg7XOVeO_ipoR-MgWXmh4siLQqKVsrlhXW9P64acVBAykFyAQzmtHufaO26ahKy1P0vux04Ywqxbakbf53EAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amW1Auw8grtJLF57weADFtd_twYRLlzNMJY_nmKK2mZO_nCH_USr8Q7y8ZN5G_2BqS51VjkCug-eq3tOAhAqxbrTsZX9a5FfaQOftQyJlUAtzy62GpERYm0LZ4n4VGffGCve2hfROIag35vxbmstmKATiFXurBfge3JBOSYKd2zsVV3Slh5i4GnPv8reTSoeKwyScn2Q2OkgXVDtnBB6Vxnhf1j0atbA34r2FqHCzn_-CIPL28Bj6RNlZAaLqAk-SBEADe2d56ZukAC9vUdjun4eJZXQPyfoKsBjNQCXJqCSNIwcVUTxx2cuHRmIxsa-H9yd0aG_Nn03fHk-C_3Q4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYlIqxSuJo8kIFNBdPdrOTX5vDRzdSFJ00wYOF4P5G21jmFNVGgEufmkHonG733YTqDrv8KesZogMJYTY3K-hMOje6TWFA73rRfQ_MQgqwvhmmoVlH1r4pL6J-FBR2PN8FRZ_iJP_oZoSGQBndgpIFL6GZybJ_QbpYz2OnpI4w_akdoaOxzs1i-x_zDs1GNUw8_55oJTBWHvhYdQpywwLSLSs5JYYHg8P3Gx6IseDv8ynxL5O-h5sUrn-K_aWS6M9_Yk-MRozM5ddGhulVQ4wjCvbD_b12wG8sR_Hkrf3aQwm58HnZyH5gq4hE0xlc8EYC_EPireQ64L6bc8FTIyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFTgokhEPJHV87aNLtr1zmG5811ACDMyYtBpU0zXCw7pgV_gLIBUnES3Bshexu3iBTJZLxruEtvUri0ERgPFfSKbjPz2SJxtY1TEWuhuFMI-h2EbJhoKZ0_EUreVlWmuHanC6-aJ83uke7OF1mXxwOfaual20sPMA31LplHJTWjD8b96aza8v8c2wtgvfWZiFmY5K7K6Te7euGU_FYFTG7meRQj035kHmOjt16eLg1KcPw9Ve2ycyIbt5WuTCzB36Hje368BV1tYf_XKv3vpkq0rMgTVWpcaoBbRsDwblGtWu1HOoyJ2yO8u9pSGlsX1aW1sbTwPxj9WFYBdx4-gxHis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFTgokhEPJHV87aNLtr1zmG5811ACDMyYtBpU0zXCw7pgV_gLIBUnES3Bshexu3iBTJZLxruEtvUri0ERgPFfSKbjPz2SJxtY1TEWuhuFMI-h2EbJhoKZ0_EUreVlWmuHanC6-aJ83uke7OF1mXxwOfaual20sPMA31LplHJTWjD8b96aza8v8c2wtgvfWZiFmY5K7K6Te7euGU_FYFTG7meRQj035kHmOjt16eLg1KcPw9Ve2ycyIbt5WuTCzB36Hje368BV1tYf_XKv3vpkq0rMgTVWpcaoBbRsDwblGtWu1HOoyJ2yO8u9pSGlsX1aW1sbTwPxj9WFYBdx4-gxHis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVYl75A9iHTytq7yRFEy6LtuEcvPzA37baWbuxyupTJ-6nVP5hTr8kgJCRdNh68K3eqlBtN0-Jq1c8xgTisqHw4uTVvg3YYGNRV7poWxn_toHoOhZic0AoBvNAJ4OAs5tWYNqlN28dFjAhT4WNrw55XF4oJ-dO9IOjrsczxRDw-gW3qWWWlOfZzRIxUgkyPTfG5kj3Y82sW8JBwSjzFLGNlHcq7YL58ZYpZaVZhpTOv9MO8XX7jtKNeyYnZ0f16RhwiBde7jgP86lBdru2sA83mWZ_OR9lTuQDhdIz1m5DoiB6Asnq5luYrvzyOb80AQjUsep1NtgPfxSTZriE5lcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYzdqkMUMQ6oyOvWmcCwl788PKO_yAwOLkSmWorzzQkI7tCQnaAAWVXLoAOHEoVc9uAxxnI3wZLn5AOkN3dn64AdlhQWLAGsatywAcfB-sukOBlE0uDYcfdEqh3rULcmJTLnKZEIdFq-U9EfO0OBWk6oKd8Fx-2orSF-EW-k0LOuGwZuCR6Y7bJenMUbIH-YdPGby88MIbYoFwHHgvYJ3NNNWvvIlYax5grJty6vgYf9L2SaHYplbbL5OkEmW1a4AjMqhIy6PkjQOo-7mG9QT-tYhIieN0_zkZ_ztIayyFVkmHEnTGd8X8o95GfigeQkbyohUUN8gCFFA_bi5yxm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rirhiXP6E2Oiew0cvxMFTMUmvM4ZvZ1WKqvgVqGrooSj-4gjzL6XBjHXIxmYx6Ppx0byAbuySWHW3oRzLdm05TITXwCr0WaoCl0fYWijXf8COV6JuY6yuhDg6rf1N9IFQ3bMi_RcikWbMBABiqWlw1G2yjqOBisJu1wosH-b9eQDADVKCZrrO9SnUiwWHAYmj4X2I3eF8jLt2M8nYwdq4b_5zYHS32Gsj6aIIQEbfha1NIsDEMkuLHSm_HrGafcnstcJstiUGxaYnhI0PXr-p1nH2IPK9dGNP7ARQGVA9kegl3Abb3GrgCfKxOQIn7gv27568jeF6fQoppEhrkH3Pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpVKeu9yG6i5vYkkoWNGMtO_vCY4OAMbFd2DDtEHetSU8MIlIDVt4VtDNYI4GMkJ1nbceZ8S1pYqE_vYSYTDsukh5Xq_G3uO1GhpEGa4rryOnZwkZzUF3_Ff4t6yppgSKGt66jNEvPT5Gxyme-VdAF-FqEleePwHMbLlikWGHPD-JoxS0Ugte8u4sC6GQbk2jPg6qy3zPbBTxOMsN5FyelNFJ2XpNLSXutP7JXqrg6Vn_t_wqIzDGRI9oKFr1M80yb6FRzQ2J30iWT3O36GplXO4TFVdXuLaQF8Xq1nykjH3023WuE1nhqhArLrbpcTuzhf_9ncWXkroi-b6r6cMIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEB7Bo69zSPoQNafQQ87GvkzNHpFHo8EcPkssHV0y4OcHzDy0ZN_l_RV5Tk-HU_Gt11DakB96hjOZcAX6UucPAMhlCDxFZXbtdfMh-FQST_777iqtp3ilGRYp0fMTdDW8PNgX73Hbpw6G7sNlZAL2mMZ_Gg2EPmj7bj6tdERqVfioIuztC2Z7nGerJO7-kF5QoP1b8HP_Ay0CoQApSfrBYsbStTCCMoB7Vtc665S2MJ5vVVYcxNuDVDKgS70kTv7gc4ariS-wpz0nmeDNrUtJgQ8OStxyo9qA8H851Ka-pD4HKs2nDCiqblwXqzTRCctz3Q1uLbXrNT0DdCZhLQneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1IIfMYcdwDvuCwgw4Y5P0GNqy4WXmfRYS6jx0KQdgDiLPiLrxyEfU9-eezFwoFLfx-A_N6nyxBdzAdRuzEE9q1UAn3N0UNR9qpH5J-fEklT2owIev6eJP2rX3Q841Ae6aRJWraSpXxkoWBaCcEzxA45CA7u7qDgRVt4FuzLAOl3eOJtkB-GWfQzZwsUZWh46lm2et6RtBiyg3qEbxw6l3JXzHXq54sLOe0QJ4H1iO4UuBowRa4g7aBJ0CT2k0O_QqaRJw_mZ_vahP4aCwX0ckTfNKo5MPfN3UEYuyezACBNTK0nwGmlq1CGfao9BsTGuulLvzLQS4H5IdpjNhSOLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvN9ptPx1Wkujn6zXYLir-tsNhDYSqgbB3ycjZO4QU-6cgN2-QzSoL6q5YJUXWl6QzZ-QR0DFX1ZJruRgsr12Fu9C2ZsCnmEyLuGMxatmvKjcgf3Hevfm1Ev-0711EZKBbM3ZgbmWtEwxnQZskzcwmIYldgHvLfOJlCF0jxbWhplGWG8fk52O2CFOWjReIGaUsVt7HW5kPo2eSxzrx7HkI5GzY_79hcJY8bK08qqFTgxj8P70bbFU_g0DAN0GhdHEzEZgGoN-E7EkBYJR7_7_sZW0fiDeP1k0BP05zyMdnaLsOF4WDFMaU-Fdfg0SyHxi5KNNq0V9rIGXK-B2m_QdA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=QTT8w8tlJkpbpp5N9vuE21QdvGH9cYMoKmbY2l_YlHQHmkFm_-WDEKmh_Kvo1uzDcfEKzgjPVZRaGBfPoyOjc3ZxEFCbexBdoIWx16eYbqvIEmmQqNsGsQJMaBmED1IBbdk5ZyY77mvnQQEb4js-sSxPBRMwrZbqGwkTGgm92m68aQ5f5ylNMCyGMXj6eL-enI8HpwafE-tHzQiXzSn3VVvq_lDsa8yc0EhMtvJDsoZBpmgDK0FXt4bENvTYrE5PenW718EENW--UeiTnBUBjXJ7OWEp_xUgZbVb0A3OAQv_pMnvUIM2izZ7LT5K3QH3Iij3IAcdlEJW9JhW0eatVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=QTT8w8tlJkpbpp5N9vuE21QdvGH9cYMoKmbY2l_YlHQHmkFm_-WDEKmh_Kvo1uzDcfEKzgjPVZRaGBfPoyOjc3ZxEFCbexBdoIWx16eYbqvIEmmQqNsGsQJMaBmED1IBbdk5ZyY77mvnQQEb4js-sSxPBRMwrZbqGwkTGgm92m68aQ5f5ylNMCyGMXj6eL-enI8HpwafE-tHzQiXzSn3VVvq_lDsa8yc0EhMtvJDsoZBpmgDK0FXt4bENvTYrE5PenW718EENW--UeiTnBUBjXJ7OWEp_xUgZbVb0A3OAQv_pMnvUIM2izZ7LT5K3QH3Iij3IAcdlEJW9JhW0eatVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3ZyYOnBaF8zBSzF-2irR4CfVZWMhyimXrOk_ZS8VHd_bXj66NSPqw8srZn-yIezIuBwSoBE9ImuE4fesUYzi8zKQwK16KKt8HoA9tlAwXP7ARXCGF8G58P0ctYvGrT8BXnRTxN46MwjZueh4PhUinCboX49mx1adfgbkG0BExkY0v1AN8oMuRpJr5Q2SepVUZL9GZuBKZMK5g9_I5_4Ms83b32-aQdbTRDph3wUsWmvnelIKhW7OGxmYSPzxks-aji02ZG9tTZbpknDdYA-Pe93wTp0KVm578RVNWbKykaLvcom094VtO3VCSZGu3s2yrmLKX4ktrFy9b19IIdZpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTO-Kpvugdgbiod5uu6MuB3z3dPCZPxEzWQ1qZvldaeajNm545vkMQXZW9VLmX3yeNiVU-L6KPNAPOo0scS9vJYLnK_0mtvSe-pR04jK4HfZhA2DmRN-vHPPf0O3YqVDuvBSFFO2cljxGys7wlkQhIileFKfgnlKCtsZzqTTUkWKhSAL_DBtsc5noiFXhlrW3fSUzyFfJtIrAsGpWkvEKozbcm--gbsojTzs3q2IL9WkfSyRC1rhMes_Aj14ABz-Irj4VWIJk8LL9iyHTiNL9RpA-bt1dsh3bugyXd_hCdkbB90kKoN40m8MXhOwXIWw0vjfjcJ1FWtTfM8npjIjvQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=B-4ujPhdJMJrJLvtmDTBK33C14RI7umEt6WXFUzFflepxHFDDjzGCuTFla6W_pyrdxX6qebkdH1m3E0BTWZjKDk7gkOvijBVDZ9wW9YywGvyogHryDpQFBH7tU5Sq1y_8tF_OAJK7utnVR1ik985qaA6f75s-jHTweC7iHIxZyb5MA-g_6kfIVbhWpn3kbRMNgw0nSlyaUY6eNa6vbl83D3ZEnVffMEasApPyhWVlTO7XISCtDw63hOCGbPRxyy_SbBYl051RtkyMsbyW756xvHt1S0iERsn7pRfp9hE0JOJq8uGyI8a5j1_qyfXKI_tQNgB0rqTK3c43AAFzQ_vKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=B-4ujPhdJMJrJLvtmDTBK33C14RI7umEt6WXFUzFflepxHFDDjzGCuTFla6W_pyrdxX6qebkdH1m3E0BTWZjKDk7gkOvijBVDZ9wW9YywGvyogHryDpQFBH7tU5Sq1y_8tF_OAJK7utnVR1ik985qaA6f75s-jHTweC7iHIxZyb5MA-g_6kfIVbhWpn3kbRMNgw0nSlyaUY6eNa6vbl83D3ZEnVffMEasApPyhWVlTO7XISCtDw63hOCGbPRxyy_SbBYl051RtkyMsbyW756xvHt1S0iERsn7pRfp9hE0JOJq8uGyI8a5j1_qyfXKI_tQNgB0rqTK3c43AAFzQ_vKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOaz9PUf86LOUqbNtZ_CVXo7j8UIs89YRB0T-YI8Z_HaLJR8cTCz2DJyBZbjSc4UxguCcxa3SPImcFiXOc1ICT892hqbZwejAQhpQqcI7OEI4r1ovahwix3jSoJjkM6F1rR2j846ncDoz2TTyrKZKuwALe-nDQ5i_UBeiQcZeEi_R61oxky_7txHFVadgTwe-BtFDBbWOSOP9aKghqKvci1aSR6polWf5vRwqHurq1DKJSDhGVyfh_74Zzvgi1UU8XpMiWkzlPD9lK_s5EHAM0BirIL0DazKN1DZ04pUGg3LflarPNaZvKh3j6UlZjz7422Lx3Q7NQNXL4y8NMhfcw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=cDzSSxvqSWEGtC5nUk8SO-7ujtjBIkD66li6vhJUFFJc2g8Z5xlnb6oxhJrsPVBWODKxzeOsS52TcYZ67e1V8asYALdX1iu-nY-dHV94akSalIdxJvFSSlCc730SXPDjfQdDolzdnB6QFagk58t7AHCgU6ch67DmqGZI5LyUdyeq5mkLl_74krlnrGkeFLG4716QuoSZioc8ZCFlU6TvYoQfWsDbhIXquqcc6e9lWkKtMBUr1sjlJvxMDfEJcSWKQghwZQHdfNZoMpleauRH841m_4uJHWF9bMejZBzfcJSgDOil4a19KwHvD8eJEVA9IJRdvXZzYdjC47qrHjU-5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=cDzSSxvqSWEGtC5nUk8SO-7ujtjBIkD66li6vhJUFFJc2g8Z5xlnb6oxhJrsPVBWODKxzeOsS52TcYZ67e1V8asYALdX1iu-nY-dHV94akSalIdxJvFSSlCc730SXPDjfQdDolzdnB6QFagk58t7AHCgU6ch67DmqGZI5LyUdyeq5mkLl_74krlnrGkeFLG4716QuoSZioc8ZCFlU6TvYoQfWsDbhIXquqcc6e9lWkKtMBUr1sjlJvxMDfEJcSWKQghwZQHdfNZoMpleauRH841m_4uJHWF9bMejZBzfcJSgDOil4a19KwHvD8eJEVA9IJRdvXZzYdjC47qrHjU-5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOcHeD4XEAIB_aqO3UMoH4XvbJRlc1JVp9zHFbuBOfX59ZWQgavANrdmDS3oaHsFdSn2DNspf9-YkjrWUcmHTrz55L3zd4d-zIoDhDM8iQBCw9n4wHBZ0WgT6mId-zveRuwEPpfLy-9PaqNwF5fRmjTBSNctCeyPVy-dA8-sj5-eZlvipAYYYIL-Jyz_iO8AKflbsUJ62wR1ZsIbmycxxnKBCsyJdWwyzMFat-lpe1Y0_tcEKLrCf15PmhegZtpSdozkk8eVww-TThgWcYkuQVu6yR2AFaSsn7Rw3I2hInA94JVypUFlN6WdxTlTY16EuuLDVKQ5YGRNgHN8HChGYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgREpz8xCmgsrNzUvBIvk5awyyLM3bIa28vzs-dKq8gT5wd3qiaSakfdLvsapPWiXOKZ-rwcGWiBE4bjG-JaJPchyrXqPlCoTML2hTfhtaNVSa4m1PmSaR4PnadmALH0OjrRDaSW-bEDTHbvhtc5-Bdy-2NJYidiNxPeq9esdzOFfE6KR6tnN4OtNdPkwITtOJXTrwdh3PRZm5GGniCIOi0NmR-gBkqEukheaxSwrqmwOm7NTXf5lR9khvyilpHnh-Ye8AX8lQqkrblGoeUiqa3MOj2ebiZzYBrr-T9j4UED3XzCZaFviQ6eUKOnQCYCXHex7Xq-hR2Yi857QHKx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izh1M1UXGSjl2TrDkmyIsM5I4kz_c6Gma0JfoOs9KQJ-YuxOipZqun9zTAgbqjqQ7wbWcLarvzlXli3sh51vYHgin5G0bGn-NrwifOI2UqLdzgvh4bCc6eaq4mRrTjL50pMyqaMAyBDqcZpwIrFalrk2W8OK_Gr2O5iZ1Oc7x6BzwpF-sGOO7Owlj7-HgsYxFxC3EtHhPRDyFpHUrfo9OisF5EfE-p8GoO6usXbCPukrvSB3a0lsXgRfsxLaqV6Zt6jsSQ2L8Xn7EXDObwU6mLSMKPzXCiOAXR_3dZ5fhnUrloOgfU7uHiWigtRPfYnkxCLx44zIyNnlHBFRYhbhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IueM2nNTsO5iqlXcijCP88U3V_egXbu36Nlw49wbtqrHXTxNYLubGou6bxm1J1001lvhgKK08p5E_79cQk46N31jS9zeU9sCvGoPOVJfVYcFhKOcYx5T9vMQgtPkTkbhmYEysbZVy_GcN-5dOqYi3yFD-Kbor8jVJjz9HLOpLmgv-WR-tYvc07AbzktV8yTRp4H12ihni8lpumHk_iFIvdKYOrVLWzq9nLpAYYXYYjIT7BVX-oQyBHgOKNxVqS9BzefF4x6zdPRvDmlrMEeCkTj-SVE0eSq2O3PgB_fqdoWlGq6Vb1F1kEa4Fm5_JibSg4dUhu7Yt-s7qofQM4JdfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYQhJnUIt2S70ybBB1Aycds_0_lBYV9FMlH4jw7PLZajni4wMGttbd2dVAaytYVeqbCMbwoaAqvV0diKuHqIXVfIytDH5HFLtV240R0BkTTGg8meCP7LZjpVWtAw1OQHSP_FlFgUmvkfpg0T-_ycSn75YQeDVVeHUZdldKE52IJsK7pSQtOhHiflnkkDvZQ1E9AKdm0a99EpFqkdOiUedYafXETypdP8BSX8ndpD81bQcPPvaNhr9pUJAwIATbxdriBPYRx-WzYTb-nbhFJzLXjqSOSezF1KWss9uOGwUT2NZ78HmYd1UERicYRor_DfMlik1o79iQwdFG5l5zs2BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geUbEwBA5YXF5UHYqF0Y1FJaJ7Z9NclHQpdFn5hdCmI9wYNvPVNW24HODwOjXmO9RTrMitwK5kyeeGs79QBvZsPF6aaFMZirHDCAdJ4kgp18y5VCaR7Oe4Ysl032DwwobIu1EBKtJY6udmeZvqRamJMSj77r07JbIaKryRBvXs4-3fw7YXUH0tShW2ZARz5MLshyc8fewt_gIPf8ICvvcp4zJuHWILTtuQK2QT9x3cwDWofNZUcvik1TIjUE0Ckb4N1o3eXh9AWuA8OLkO7FACHIuKWDfmMkOuA6kM3-Up150EPr0VKCe9pdRsqFKwvIva8Vlghb-EUTWMJB4iiwEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnT-Wcpb1gXxnqatjhPhn2S9qKURCow4LLF2pcV8hNBpZjVKiHlg8GhADGOgFxI5bQ7qEuW3tWvyGRxVHtqpg1fiQWwhLbKQE50l3wj5noXJp-eWw_vIYwfg1cxbuQFnGkeKB0M4yI8lbcY4ANf2mACUuwEG-6hC6wgMzcMCL0HclraADA1HCxoGw5N9U1aYMtE-yvQ5qDZKdBwuo5CxZ1UqD62rjDZrSqHrCHh7t0wxdQsESPmJDMrRXEI5K13VDTloaMShWj4JHXN7wRGbOTfi_e9p5lMtv6noTbYgwpl4p8dRJ_5nimpiUkZeb6FpbQfmppu6ye8al15UAiloZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOYPu6K0RHCUmZ5zQNqbgyMjZe9ddhD4wrTEenxJOok8p-VK__BaPr9EgWLo2OpJrFN9w6X78gH0SHjgi_lXw9wU3rcr7ccyTFRHSmk-H4ZMp9XH4McuoF12xqKBMKbIsNvAYBRGapiDGDat5FX47i_epRjJrbYlVJPSp1YfYgfowxnzouSkOrKA2mJQ5TgpWG7mdunngEWmLbEfZdedJN97V6jUVMuzOHgNKVFtD9mzbKE5Dx8xlniXtCOUysb94wktglCFZqRq1-lkvrDwReeppfJ5-9I0MOKRsUYn5Seg6elvdE9RpcfTFiJfL8-2HB5_JyEYYwwMa5doYQGWIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_1xNh_yQXVDxZobiijKTxSZHlrCP5lEmJ49KcHf0w4AcoqfhIJySLduYG_XaimILN7K_2XrHvuKhL4fLMYQ8WUslgdQkaXhhEww-dDI8kWFqxfhqBiv4NtymUw1XVS9EB5AoQoC00JGJ4o056SAhieYPTThOqnksmnijeArA4Cap9cIFeeCY39PoUFuTLO3cZsJrfBE4rUPKOwkCbO2ScbQpt83zwN6Oqg3P0Werkhk8ffJeLQwn3j53KRIAey-7MoUdmOTwRBhNANsxViQKMEsV-F5egRxDKwtn8RQAgviHBT3FaADEQcGfTXQXHtePDUCIAXg8C_J8BqLAxIiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL512qy2yZUQI1TXscpxz_10tm9BhJz34Ho59eUW-wOZkuIydABT4HlH0sMXFU9Z47IOSDDWBkywLu0j_q58O12cO7DHjVoiMo3tlUNqe5_nV147CBV3UgHZL8epYNvyvNWNCD-UVwnp5UI7YAnxap10rpnR5C4TZq40d2TM7tqV2eK0XQZftpRp7Oq2u-zdbuh2oDYA-LtVLryKUQzQ5LeXWV1U3233N7We5bITmGja7w3RLQZTXNL3agjOa_I3liAoF9syIcmDkOvOR-a4uGR-6P7nf-zI-yPf2R6TpFptN3kEt7GpmMxD-_vJTTP60ZFz9igIo2KilmSo-GBNdg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=Wq_PJd-uZqdCyJwoV3IZu0_OQc-uevNpQZth2H-zrDjEFX31P9V4IG8Nrft4iz9xz4EVs1CPMVC5PQAd2_rJse2XqogSQT8EB95apHOc8C1cLxks8PwdAdGRoBhpkzuG55jYgo3EzOoEam3J6gz9fOTR6GhwU15qcVLYKh68lYpEiENv_FZmZY8ZoCu6r_O92a-FgAuV8RskGkYgM4HT967pQX6H0IN4cAGkwCYbQK95STt5i5jc26dmT9gndK1Gcdo2CEKn1UhXls5iiVbjCg49dywLuHsuSFZxrlMwlSHns8HhQqbrvk83Jk-IysdekFTmaXQcmmx7FoSD18AG7FIGwR1TyTdwkTPiG1BXfFuL4962eUi-y1zAxchqAa1Y-Gm0JmcuTPx4BwQoGDc3QnTjqvMB-8SoWfMu802f6FRXaGxoHgzJVAl_pCUygYqyiU2LfrE3ssjmk1-k1FUdTf3-G3zWfgq_-sAmt-MGe-HV3o3ZxEPpFOqGVmm6FIDivOX699XpGQGALIJZv0N27VQUgOq1f1Ewt9SiuZp02KPVS9RaQystMjW5QeuR_nDON78-MvJQdgfWMN0sq6pETdBNAD-C-LLfgR5IhAM0s7WC_ZRc_UNgxCHDn1IeTCkgNK6MiaiEyRF6_Cl9vRLt9RIlCJzFR_IV3SHx2rn7ZiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=Wq_PJd-uZqdCyJwoV3IZu0_OQc-uevNpQZth2H-zrDjEFX31P9V4IG8Nrft4iz9xz4EVs1CPMVC5PQAd2_rJse2XqogSQT8EB95apHOc8C1cLxks8PwdAdGRoBhpkzuG55jYgo3EzOoEam3J6gz9fOTR6GhwU15qcVLYKh68lYpEiENv_FZmZY8ZoCu6r_O92a-FgAuV8RskGkYgM4HT967pQX6H0IN4cAGkwCYbQK95STt5i5jc26dmT9gndK1Gcdo2CEKn1UhXls5iiVbjCg49dywLuHsuSFZxrlMwlSHns8HhQqbrvk83Jk-IysdekFTmaXQcmmx7FoSD18AG7FIGwR1TyTdwkTPiG1BXfFuL4962eUi-y1zAxchqAa1Y-Gm0JmcuTPx4BwQoGDc3QnTjqvMB-8SoWfMu802f6FRXaGxoHgzJVAl_pCUygYqyiU2LfrE3ssjmk1-k1FUdTf3-G3zWfgq_-sAmt-MGe-HV3o3ZxEPpFOqGVmm6FIDivOX699XpGQGALIJZv0N27VQUgOq1f1Ewt9SiuZp02KPVS9RaQystMjW5QeuR_nDON78-MvJQdgfWMN0sq6pETdBNAD-C-LLfgR5IhAM0s7WC_ZRc_UNgxCHDn1IeTCkgNK6MiaiEyRF6_Cl9vRLt9RIlCJzFR_IV3SHx2rn7ZiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3yhGlUZtAzSsZJOQOUvcl6Tbo4gEQQK8STjVRXvYCHMk0LNnztRy9Jprli6oPvqW7NX7WTi41UFQmvFao_mDS5JMg2ut1-xGReIJKc8k5wDlODG17Cy_LX61ibtoFlx1pc2lomAb3F3RgwAkTPXbT6SpCtfXrknH65mHzaltEhp_hecSPEfmd-yz92ZpsCxSpxaJFBHbTKmjbkKJy965nRwn0XR9K2ZwKYzMeRDQ2N9neNDC_0yUAsWkzM5iVfZm_QpKx9qx5TVNfPnCS-Y6j0TlFFh4SvNfgLq0KBY38TTJpjJV34HaduicnIP2bZXeZlrDSJ2QbD0RQN0J78Lug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw8WxdH-iBTsF-PRcdYOldRxkSrgxiJWriYxACyI4gzAnhXzyUBbWv8_VkEkksg_rgSFyvSoHF6tT8fJRoKYpgclLOs40p_Mkex01c-th30m80Zi4GlK4Siq7bGUelQgm43rN8uUFEa8eL1-O6YUwUcG0r9kcSgtCdgFU0qxT6ZRDLqDY7JuH42wKbZrzrEC6QmW9vFbdKWL4wcthM4D_1m0x310zOaLNp1m1-O9yeY3PLH-MPHLNIo107yjGIfIfJbw7LxS4mn35vCY5cl64jSEh79y8A6dAJqSccdUhb0wjsys5n8ry_GdLzm-jQqaNyNNRb0TM57u5tZUPiujDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjQFLnos2LiI7gT0qhBSZP8NdIPCL6zFj72z1l3bAVwoM7l3Lcc6-yXWnBz0pf1SzELIMJRThJrQItMr-1gm2ex00xp0DaPzxCNYhj2eqMR3yyXdHQlBVQoZcO2CcuPvh2LUhRgYtGasI0Hl32vpqm0cT95brp7UgdvEe5yclhXoaxnrabLdO3eFSJwgeInuliX9eEw62jdiJsjAG1MYteEpgL_clbe_iAU-P69VUWq9YjyBjKkRNV5Y6a4upwYsNY_2D6SxB35-_fgd1Kai58KiDkg6dSrCB5BsCsuqWNnJ2nOPq0ZxxB5UKodEUbi6UOtmNVHCjax1DoWGY2Srvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVZz8gZCk030ECarizSJwn2ZKkvmJ9z8bh8xTMvsP1adEexrc-j21O39v97bdG-Emdlbk-N_qy0aKlRG2F1s_4vlOJHAOXMh9ZZkuxQ6EZFYPoxrD1WXd-eOdhV34LKYnn5jPCzC4D4kmldZaB-ejV3z0ellUGjAG9FeqoqCVtzsYWgV-Tm9j362vIQkk1K1j8-1ZSLY8YTbwewKaI9VcDwk11gKSx6wcLbzdhwZ7nJXVgfb_CifKXItdnwBpJhZrOtW7dDXgA_LeLBZSAQuDX4bzGVxW5NLIVJr6gshdhXjxIRr0_hO5Isha4pr6fJUHcd_6lKnF_r2NBCzVqA7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/22002" target="_blank">📅 23:57 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTtnbim6HhwnA7sIp--CnWFI5bpsEHwjS2A3y7WBpRDHK5Ni2yRQVdYNzpw7s1rKEQLJXmHOW8HY_19a9zS31K0d4YnwYJC6oT74rPc2gCSm8BBA2uKrvj2XIr4qhNkuZI-Y4KE9kb7a7pTKDtM9COB9-mFRM-o5vWJ1Mj9z30YTTYLuozgHEmn8p_BlodjqbcTGPMmGJ3ZdQW0q9JpXA-N9bCZAOPByM3mMT3IKG_AjloRbdRo1VsoooomAB1rtuVzX__4OpTRaNviQTvby559ZB5j7uPGmYUABf8lYpAUl-abgTrreTMGqsNsK4OqXHJRHYuCYXyMvdvAdxsFyNw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=cMDkLeAAZz1E4DnhTqsnm_h7aYqmTbD0QqRTWkggSdGXPVbkLs4sR1_qLLpOXTtk0r2grhBnfdtXVxx-4eLH_y0AcLee69WqYaFzBBLX1yK9bGdyp9pKSsTGZKlAqBzsZAUwJ8k3D7ABS0FJnA-_HYV3TfVuO2KBa_iLYfS313QVYRMRuw1H6kOpplu5XV-tXCnf6m9dgpX86xUYDFEEASA6P9zvJK9YdKFdKAceZ_81Mt8ds5L_x_n21wlfznGaSd2-0iMA9DHT9Eee9SOk4GJpqpRsoTc-uB824OCh22vV17IuSJHWsmERYjBgXyux9t24I7ucw0pmhInl7unE9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=cMDkLeAAZz1E4DnhTqsnm_h7aYqmTbD0QqRTWkggSdGXPVbkLs4sR1_qLLpOXTtk0r2grhBnfdtXVxx-4eLH_y0AcLee69WqYaFzBBLX1yK9bGdyp9pKSsTGZKlAqBzsZAUwJ8k3D7ABS0FJnA-_HYV3TfVuO2KBa_iLYfS313QVYRMRuw1H6kOpplu5XV-tXCnf6m9dgpX86xUYDFEEASA6P9zvJK9YdKFdKAceZ_81Mt8ds5L_x_n21wlfznGaSd2-0iMA9DHT9Eee9SOk4GJpqpRsoTc-uB824OCh22vV17IuSJHWsmERYjBgXyux9t24I7ucw0pmhInl7unE9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/21999" target="_blank">📅 23:05 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21998">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=uAPj6dVIuk6a3ykD_LfhdbZTmIzXewNLzWXK7JNXKHuypStb8Glge5ak06dYWwWMEN8sbbzNWGhbKngwvgbxGI4ujJ2_8mgby8Ua_8my0xjOZqbZpyvVmVXMe1NJew53Q7r9yYRQw762dvtVQp0HOFYFFfg3A2Lnp6F_d0AsfPVyFtHEWbIsipVPzbQfkJZ7iI4TOuvBGubXhtg0E7yR7i9p1TJGMkYlMzE_Qs1kwEGDCsMV8kUROJ-GqzBKjjq4BUknpzDSungGjDU6Qf4lNKsU60YzUUt0LehU89J9jot3jA0aCMyJMFSTymHdr9Hq1u8xZGJ3D2Ne1uDhaQBd-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=uAPj6dVIuk6a3ykD_LfhdbZTmIzXewNLzWXK7JNXKHuypStb8Glge5ak06dYWwWMEN8sbbzNWGhbKngwvgbxGI4ujJ2_8mgby8Ua_8my0xjOZqbZpyvVmVXMe1NJew53Q7r9yYRQw762dvtVQp0HOFYFFfg3A2Lnp6F_d0AsfPVyFtHEWbIsipVPzbQfkJZ7iI4TOuvBGubXhtg0E7yR7i9p1TJGMkYlMzE_Qs1kwEGDCsMV8kUROJ-GqzBKjjq4BUknpzDSungGjDU6Qf4lNKsU60YzUUt0LehU89J9jot3jA0aCMyJMFSTymHdr9Hq1u8xZGJ3D2Ne1uDhaQBd-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
