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
<img src="https://cdn4.telesco.pe/file/nqdKgc2rCh0ws-279eWQ1AF94nGMA_w9UeBmMEw2ebjEGkJz8IztrMidtGIT1S9mXrVEfv77d4kd5NYhN3Cb8dopU6UxyCw6qV-0O2-0ix4uHN8p9YHNPRzpcqSmLj8yYLQHCo72P9MrOz1182MAlAZ1DTXpQRMnRVO_f4TWDkSlIzFgymcVRVSlebBCNPCtjBInS1mLA_2UjSqMGzuiYsTDgvDzaMrtiZELysDJrT9fOn7GfcMcSRu4HdKqvtygd95g45T57xZmuChUw9Mbj5a2fkTh6mZpWEZhxwXZ2244aqZx-yxs87bTm0xGlNUhnLQhRy7dM2_68ZV4h7Z_qQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-93263">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK2wpqHD8VrgW-HLaimSaShpliFcg9pGbZ8zBWcvM5tJK29DqnhfXwAiAuTlFUkgbKJfRNW3CbIN-FqfmK1FjCqJhVi8SFBCddN1M-8E9-at116W_6_dFWTpU5dAfAQ8kXZ_vNFTz84VPRl8htWyhFKsZSXMcRNUvDWcz-t8mi_QX8dK-KoV5OU89SHJwiu6EnxTyK0FVY4vKInQq5iJHLh5nSJeodNxOQ6PoOmySByzE2NeTPNbXnab9xU2kxLZtRsMIPlJnOofwKXbwh4NBp3mTcgcF3lKjHcxkmkn4L05RJqv-HgpF9GkLkmfbWaEczUoK4wN-WWM17gMJTS0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ بموجة جديدة من الهجمات على السعودية</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/naya_foriraq/93263" target="_blank">📅 16:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93262">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ بموجة جديدة من الهجمات على السعودية</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/naya_foriraq/93262" target="_blank">📅 16:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93261">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adee9d62dc.mp4?token=SHjD3150OGYu0hRMKU4uD3o1xQEJzPHhtNb7EEf_akgVdwgoFU5-qQR3FAXO9uoAAM6TKdmMAvw33hBOvHcNSKkL08rs067XU_GZhXWzgXk_Oh6nxp7vGb_Dh_uOsa040PekokYMK-x3_pZdZzzZKiUCtioldM-8KISmHUowqKaglECmzjZhKZhN0Aii6b99xPW1ezgU-zbPYlxMnIEWSEWpsWi6WT5IYP8XAJgMRa-dQs3-nOTgSS-baELQDK-ydGekaHQGSlBJnI3KXkMAwtDBU2kVqfvYuz2o-hVlz5X_4Pg-aqZdftkPd6db7Jw3Ku4paMj79UVZLNmeNNWP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adee9d62dc.mp4?token=SHjD3150OGYu0hRMKU4uD3o1xQEJzPHhtNb7EEf_akgVdwgoFU5-qQR3FAXO9uoAAM6TKdmMAvw33hBOvHcNSKkL08rs067XU_GZhXWzgXk_Oh6nxp7vGb_Dh_uOsa040PekokYMK-x3_pZdZzzZKiUCtioldM-8KISmHUowqKaglECmzjZhKZhN0Aii6b99xPW1ezgU-zbPYlxMnIEWSEWpsWi6WT5IYP8XAJgMRa-dQs3-nOTgSS-baELQDK-ydGekaHQGSlBJnI3KXkMAwtDBU2kVqfvYuz2o-hVlz5X_4Pg-aqZdftkPd6db7Jw3Ku4paMj79UVZLNmeNNWP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الهجوم الذي استهدف مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/naya_foriraq/93261" target="_blank">📅 15:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93260">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11c03a534.mp4?token=ayiwHBW21CQkWROc8E7LWMMVEsRtqy0Izvm8Uj3YMETbQN2E3Xnm7lSJ7NAeBvHF6Dqm3cJ1LpFTM1ic_j75m0_uMK75ufVHkJW63QCujo3x3pGp8NommZ0mTpvA7l7WZcjPJQI7Qct02MLwLGuoP5I31vSlueO1auoaQEEUQf8VcDMGI34U1m5PD316b3V77uQ3FJV_DfM6shIv0U4mijTGOzmByFtwIsTdaOTYZaZhzE5aqRZ6ZWAadSnweX3OiGtd8iCI5DApjuIco7h4Vi6byWDkJTFVUqPkwkdvTsea8DRwibXc056HcDLMPIRahCBirQVPVO9C-VE-wpYyzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11c03a534.mp4?token=ayiwHBW21CQkWROc8E7LWMMVEsRtqy0Izvm8Uj3YMETbQN2E3Xnm7lSJ7NAeBvHF6Dqm3cJ1LpFTM1ic_j75m0_uMK75ufVHkJW63QCujo3x3pGp8NommZ0mTpvA7l7WZcjPJQI7Qct02MLwLGuoP5I31vSlueO1auoaQEEUQf8VcDMGI34U1m5PD316b3V77uQ3FJV_DfM6shIv0U4mijTGOzmByFtwIsTdaOTYZaZhzE5aqRZ6ZWAadSnweX3OiGtd8iCI5DApjuIco7h4Vi6byWDkJTFVUqPkwkdvTsea8DRwibXc056HcDLMPIRahCBirQVPVO9C-VE-wpYyzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تواصل التصاعد من مطار الدمام الدولي في السعودية بعد ضربات القوات المسلحة اليمنية ووفق معادلة المطار بالمطار.</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/93260" target="_blank">📅 14:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93258">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7bd81ef52.mp4?token=uGuCSKhglEHHgQo8Yz7F_6A65U36PufKRovrpQL-USiqyFRQjMDArpqP6DzP5Vp1bfdZmR8IvSHZF8-bC4-H00_iYMM8Kvg5EjmtJQujy4z2EhuIxc0-WPGPPm5WP1HVkC2jGjDFxryM2ilTOTawbgyvUzR9PtNeyOEYVcsv4ojs4Prc91wjk7icFO1gdVxO-y7ed0XmWze2pRxUOa3V7jauuxO2TuuCNRielnr71GfQqsuZnh_hSki2n479S--EUTqmwvyNKkLqZpsa7GloTXs49CG9r-9pOAPNrYj0s4h9sMcD-U84vYmnxNlCqT5K0T8JVIUKXGpVXB_MTSUt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7bd81ef52.mp4?token=uGuCSKhglEHHgQo8Yz7F_6A65U36PufKRovrpQL-USiqyFRQjMDArpqP6DzP5Vp1bfdZmR8IvSHZF8-bC4-H00_iYMM8Kvg5EjmtJQujy4z2EhuIxc0-WPGPPm5WP1HVkC2jGjDFxryM2ilTOTawbgyvUzR9PtNeyOEYVcsv4ojs4Prc91wjk7icFO1gdVxO-y7ed0XmWze2pRxUOa3V7jauuxO2TuuCNRielnr71GfQqsuZnh_hSki2n479S--EUTqmwvyNKkLqZpsa7GloTXs49CG9r-9pOAPNrYj0s4h9sMcD-U84vYmnxNlCqT5K0T8JVIUKXGpVXB_MTSUt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور القمر الصناعي التي التقطت اليوم تُظهر وجود ثقب في مبنى الركاب رقم 3 في مطار الرياض الدولي وذلك في أعقاب الهجوم الصاروخي الذي شنته القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/naya_foriraq/93258" target="_blank">📅 14:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93256">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">السفارة السعودية بالكويت: توفير حافلات لنقل المواطنين الراغبين في العودة إلى الرياض ممن أُلغيت رحلاتهم، شريطة وجود حجز سفر ملغي.
سيكون التجمع في مبنى السفارة بمنطقة الدعية الساعة 11:30 صباحًا والمغادرة الساعة 1:00 ظهرًا يوم غد الاثنين 12 أكتوبر.
بدري على الحوثي يلمس أراضيك</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/naya_foriraq/93256" target="_blank">📅 14:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93254">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d1519bbc8.mp4?token=hiWIbmC__ne144M6UDJFPBtmrYJrZgpnHNykdroVU6XzlHDCphsOW0mN8kbzEq97qbKKchHRK5PD-WFeBmNnPWQ92ENRYxY-lfpM0F-4TrQomSIfWGv51hc3NW2AmkIU-9R2D5bTm1GyroOeULXdwb2bq6cDHVw5F69UBkqLhtBpWLYszWx1Qn3cTNSy1gQZLN1OTj0VIRqb-93YwKxFJg6pyJAu-GM3k6IIkBkUz2tWoqBqWe2LRPycjFBLwJLb3Vr1WOkTjaiLO4oERNOeFqCOgc5m8H8SNLrKHIPnwnzR6FH2Bo6MORkw2EBKm3LyIl7LvK-P6AXxefEhridnGxgAPfdNOxUMoStyi3sOl9VojVinhHAJrEqTulgM0bUZYX14DY_iDLBmcOKFAH4gsalJ9EPRT1ty4LYTHsa3pAPFYSeCY5YoUp_TEk9TTwB-WyfyvyXV_9JqLyfFUpXA3oxThZ0ZDrfsKwtU9kN22zMKJZALT0renzX7kDNz0IaVoV3u5_QlSw84GQleKde4GZPHor6zzR7mz0imQ5kaU37qQ3_n_RDoMmTcIo2BqHe52K0FN5Wobj2x1xZMwNEyns1PU9DeyOue6FVWgp4k47em1UIhw7uRjrKOmz3d5PCKual5DT1o27edS91m8ChP22A-HgDLATaFeiaH7UAE_Wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d1519bbc8.mp4?token=hiWIbmC__ne144M6UDJFPBtmrYJrZgpnHNykdroVU6XzlHDCphsOW0mN8kbzEq97qbKKchHRK5PD-WFeBmNnPWQ92ENRYxY-lfpM0F-4TrQomSIfWGv51hc3NW2AmkIU-9R2D5bTm1GyroOeULXdwb2bq6cDHVw5F69UBkqLhtBpWLYszWx1Qn3cTNSy1gQZLN1OTj0VIRqb-93YwKxFJg6pyJAu-GM3k6IIkBkUz2tWoqBqWe2LRPycjFBLwJLb3Vr1WOkTjaiLO4oERNOeFqCOgc5m8H8SNLrKHIPnwnzR6FH2Bo6MORkw2EBKm3LyIl7LvK-P6AXxefEhridnGxgAPfdNOxUMoStyi3sOl9VojVinhHAJrEqTulgM0bUZYX14DY_iDLBmcOKFAH4gsalJ9EPRT1ty4LYTHsa3pAPFYSeCY5YoUp_TEk9TTwB-WyfyvyXV_9JqLyfFUpXA3oxThZ0ZDrfsKwtU9kN22zMKJZALT0renzX7kDNz0IaVoV3u5_QlSw84GQleKde4GZPHor6zzR7mz0imQ5kaU37qQ3_n_RDoMmTcIo2BqHe52K0FN5Wobj2x1xZMwNEyns1PU9DeyOue6FVWgp4k47em1UIhw7uRjrKOmz3d5PCKual5DT1o27edS91m8ChP22A-HgDLATaFeiaH7UAE_Wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رحلات جوية هندية كانت متجهة الى الرياض تعود ادراجها الى الهند بسبب اغلاق مطار الرياض من قبل القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/93254" target="_blank">📅 14:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93253">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuCaYjbLsG2iiRDdqjYQuFpdk1WKYA4ldI4RuY8FGsRDTzVodK0k6YyKIwHWRfV4B4ZzpckC1m-WnsPfZmepJR_sFO4meEW1cYxGGx8g7OG9shByLE8Qj4AVb8rCDSybQjypFKzdoZlIT0Jx7CBiRHr4FMJJTRVby-YKXVhDtwmxabCg_sYDC3zT91L_Fns3O2I_A0pDoO3v4J5dqqLg3Hq7UYVHSYXZwPOxK3P0R0JvQDrzy88MTypbfyfeubVoRXrPsV8S_kuqoZPFbW6xP70MCRrrPAoEU2a4hi8BIPP0lUCVJ6wbNPcarTPVOYpSFqTfOWZnZdwqUU7jQFqtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية تسيطر على مناطق الصياحي وسوق المقاهي وأجزاء من وادي الضباب وتنشر قواتها على طريق الدخول إلى مدينة تعز. تم قطع طريق تعز-الميسرة أيضًا، ولم يعد لدى المرتزقة أي وسيلة لتوصيل الإمدادات والمساعدات إلى جبهتي الميسرة والنجد القاسم الا عن طريق جبل صابر وهذا مستحيل</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/93253" target="_blank">📅 14:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93252">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6251092052.mp4?token=PkSLAGfh7FUsPS6oXr6FwboyVpJvVcarBOFN7c2YdiWDzkdNQ3HBggyk5dCfLjjwJexJymXnlYKepWjEy3jK99T9JbzB4M8TLGINpbBsFjTQUe2V71ACvV8c21Q3J_7QlT6WdNxEC_QnKl4y7KTWyBnQsVIrtPexjvoMGnI6w5OY0EaiuCkT5ko3QLHfuh_oesdgUrea06s-b4ze-ABzki7PkEwsEkkd_RD_rTqqHwZibTPTeeaZwqnQjD4k30Wf3DdSRdBd5vvFELDxt38v_7k_AbrgjU9Dw0YEQBE4H5YRBzLFhlUz2AABhVkeWoQ7jFIiDtcOfRa3wiJ4FTD88g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6251092052.mp4?token=PkSLAGfh7FUsPS6oXr6FwboyVpJvVcarBOFN7c2YdiWDzkdNQ3HBggyk5dCfLjjwJexJymXnlYKepWjEy3jK99T9JbzB4M8TLGINpbBsFjTQUe2V71ACvV8c21Q3J_7QlT6WdNxEC_QnKl4y7KTWyBnQsVIrtPexjvoMGnI6w5OY0EaiuCkT5ko3QLHfuh_oesdgUrea06s-b4ze-ABzki7PkEwsEkkd_RD_rTqqHwZibTPTeeaZwqnQjD4k30Wf3DdSRdBd5vvFELDxt38v_7k_AbrgjU9Dw0YEQBE4H5YRBzLFhlUz2AABhVkeWoQ7jFIiDtcOfRa3wiJ4FTD88g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المناورات الصاروخية لحرس الثورة متواصلة في الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93252" target="_blank">📅 14:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93251">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d1b89e70.mp4?token=ClisKgVlHSzEeP8YohzXG1YoEttImITerI3PNbemCttlNcvbFp4W9Cg7_UKOADaL4j_6se6JGNZ0mhuDue282UR3hYbCRHVoC8pOsMHDNvHpzpOW0V-n5e1WqDqIi791ypQ2rQcIaiLzwsff2C5hsftuAECWdyOAtl9emax4KgLIUT2GqoN0G6HgdGn_0bXpfxU3wyLROu4wQBkU7e5J9dY2HCsUwouHWOjW-I4qh9ixZ4leoZK_lKnLt0TAui42lUvjzRcaANMsW1n60EWFwvum1HHzHNqJjC_EjJOHZr9fyuOCd5g7tNmUxleRWKCEh2hRksbuwr52pzt324a0bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d1b89e70.mp4?token=ClisKgVlHSzEeP8YohzXG1YoEttImITerI3PNbemCttlNcvbFp4W9Cg7_UKOADaL4j_6se6JGNZ0mhuDue282UR3hYbCRHVoC8pOsMHDNvHpzpOW0V-n5e1WqDqIi791ypQ2rQcIaiLzwsff2C5hsftuAECWdyOAtl9emax4KgLIUT2GqoN0G6HgdGn_0bXpfxU3wyLROu4wQBkU7e5J9dY2HCsUwouHWOjW-I4qh9ixZ4leoZK_lKnLt0TAui42lUvjzRcaANMsW1n60EWFwvum1HHzHNqJjC_EjJOHZr9fyuOCd5g7tNmUxleRWKCEh2hRksbuwr52pzt324a0bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إطلاق سرب مكوّن من خمس طائرات مسيّرة من طراز شاهد-136 خلال مناورات الحرس الثوري
🚀
شلیک یک اسکادران از پهپاد شاهد ۱۳۶ در رزمایش‌های سپاه پاسداران انقلاب اسلامی
@Naya_Press</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/93251" target="_blank">📅 14:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93250">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
على أصحاب البيانات والإدانات مدفوعة الثمن دفع النظام السعودي للكف عن عدوانه</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/93250" target="_blank">📅 14:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93249">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇷🇺
🇸🇦
🇾🇪
🔻
مصدر امني لنايا
استشهد عدد وجرح عدد اخرون من المواطنين الروس نتيجة الهجوم على المراكز الحساسة ومطار الرياض في السعودية البارحة ؛ أنصار الله في اليمن أوصت الدول مرارا وتكرارا بضرورة مغادرة أبنائها وجاليتها الرياض و باقي المدن السعودية عدا مكة والمدينة المنورة كونها تتعامل مع العدو السعودي بالمثل باستهداف المدن والمطارات اليمنية .</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/93249" target="_blank">📅 14:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93248">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇸🇦
الاعلام السعودي:
تعذّر وصول بعثة النادي الفيصلي إلى أبها يوم السبت قبل مواجهة أبها المقررة الأحد بسبب هجمات القوات المسلحة اليمنية والامور تتجه الى تأجيل المباراة مدة 24 ساعة.
من المتوقع ان يتقدم النادي بطلب ترخيص للطيران والهبوط من مركز تنسيق العمليات الانسانية في العاصمة صنعاء والامر متروك للمختصين في صنعاء</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/93248" target="_blank">📅 14:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93247">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4f94d651.mp4?token=RvVCoATx02EpHlNASY4O0IXHal0BIDUObeeyUNt34S5gNarYVzQBDrVzg7ygKdlUENUDnWmcA5r-QC0hkKgyEmDj3MzikTNQXj3dRhXRpf_s2oxpwKJ5m8-s2SGOW3-sjLT2MZLuxvkcRcddeaZIzrte0G-geh2YK2LGfb8b59770eT0TC873efS2Dq-MhIMaxmAUJiUcge4yD7L0V7SVUIY-lQ4mUVRAbGr0s7ewEzasIzJ-gNi0hesPsdtKH25VV-Q1V-fBinoY8pmZAlbxPo8gNEcq3tB-s1Kv-tSizg18PDEZWDZzYvjLxD8O3xOTl3oa7NI2Zp3WLT-rTh6mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4f94d651.mp4?token=RvVCoATx02EpHlNASY4O0IXHal0BIDUObeeyUNt34S5gNarYVzQBDrVzg7ygKdlUENUDnWmcA5r-QC0hkKgyEmDj3MzikTNQXj3dRhXRpf_s2oxpwKJ5m8-s2SGOW3-sjLT2MZLuxvkcRcddeaZIzrte0G-geh2YK2LGfb8b59770eT0TC873efS2Dq-MhIMaxmAUJiUcge4yD7L0V7SVUIY-lQ4mUVRAbGr0s7ewEzasIzJ-gNi0hesPsdtKH25VV-Q1V-fBinoY8pmZAlbxPo8gNEcq3tB-s1Kv-tSizg18PDEZWDZzYvjLxD8O3xOTl3oa7NI2Zp3WLT-rTh6mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من المناورات الصاروخية لحرس الثورة في الجمهورية الاسلامية الايرانية  الاردن فعلت الدفاعات الجوية ظنا منها ان الصواريخ قد تتجه للكيان مؤكدة "لو يموتون جهالي اربعتهم ما اخليهن يعبرن لاسرائيل".</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/93247" target="_blank">📅 13:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93246">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇾🇪
🇾🇪
دبلوماسي بريطاني في الرياض:
‏خرجت للتو من الرياض. تلك الانفجارات السبعة التي ذكرتها في المطار أسفرت عن ثلاثة قتلى و12 جريحاً. لذا قررنا التوجه بالسيارة عبر الصحراء، فالمطار كان مكشوفاً للغاية. تعرض المطار للضرب مرة أخرى أمس. تمتلك السعودية دفاعات جوية أكثر بكثير من بريطانيا، ومع ذلك لم يكن ذلك كافياً.</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/93246" target="_blank">📅 13:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93245">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43172e017.mp4?token=VTo7Yl-ArOw_jMuBvKGgx-DbzCg9vDAdIEHlBCIZBlbv8pCeV8AlNSGJNnkuEVf1chW4UfhX1YKpYoMHRq92VBEC6eOJcavXBZT04AH3ARRYpiNdWzeJowCT9lxq6PsmX3BUyLs_ZxCrJfOoH6AzTM_QIXJhyvpfmCCRflJI7WnDoaYDFaoxztLwwM1TAQCZlWWLOw-rb9j5Z-HpKA42a23iuvR_P_hQvyQ4ScWrC7kG89LPOWiHztBOHEw51L_fHHNc8M8z5ee4zXi237M-G-_WCiuSBGHe4ZUxT4K16YUJwBQ1KRa7QZw6t0WYXf1dumv7duKWSj7lELb1jU2MTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43172e017.mp4?token=VTo7Yl-ArOw_jMuBvKGgx-DbzCg9vDAdIEHlBCIZBlbv8pCeV8AlNSGJNnkuEVf1chW4UfhX1YKpYoMHRq92VBEC6eOJcavXBZT04AH3ARRYpiNdWzeJowCT9lxq6PsmX3BUyLs_ZxCrJfOoH6AzTM_QIXJhyvpfmCCRflJI7WnDoaYDFaoxztLwwM1TAQCZlWWLOw-rb9j5Z-HpKA42a23iuvR_P_hQvyQ4ScWrC7kG89LPOWiHztBOHEw51L_fHHNc8M8z5ee4zXi237M-G-_WCiuSBGHe4ZUxT4K16YUJwBQ1KRa7QZw6t0WYXf1dumv7duKWSj7lELb1jU2MTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المناورات مستمرة و بقوة ...
رزمایش سپاه پاسداران با قدرت ادامه دارد ...
@Naya_Press</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/93245" target="_blank">📅 13:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93241">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8noLoauGa0MwNQEvxPH1MJKQuOLMatnXFELL3Ed2yw2pEY2_jIJFS1xudNI3sXIim8BmpicHnRygBpgpONj3E7gmHXau0dZl-MGGjyRkw94rnVO55ZPlIM9mZMP27aRe8tKBDCqQitcFExs3dE8aQhl1F6mNbp42ckpEWWAuvoUKEwBxqY1aiCYWC-xGWe0TFRLmsVH_mcU0j4rFp8qkecsQVJjSR2tn-H-c0uTUu3R911sw4FBLoY463TF4wAT4ecApAJ1xFfeom6HtmexHtKldXof4FNgagc6EXm53dv-l9cFd1CmYoeQ8iEgTTy3uWW3VkKFMnHTenV5uf8eEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mFCr98VAu0ww3_n4nTtmajDPJquMd_rvWwDJIYIfMi0El36xccrXrMOFm6YiXGds_nLKZ7tWCLEv30Qs8W9oXnMubGmegn99Am00xMDxNDtatSDeQqvmg1o_FQAFhciFot1PYWK4Efxd4-o-w4qKxT3csFxFcNlZMF2tYhyAGpYE3aYNfj2ub-RS5Uqv-kSjJYxfT9JCsqR4TEGDoKb_16-zYoYg0vzIOYNtSS0Se1LdMQd3Lreue2txllXS01RidtIIDyqcJss2hrehIQ6zBHGG70SZuL8EWQ07Pr-8ayh23YcPEH4VajBTGn2uhNKNSIk9Gp4tHAjCbyhwGnq32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eB4JfioNcpp8V4RxkZq8ri64C2yAUgm39NDmqKzWcw1nAugtLIrsWIR95qB5mTaOA9UbKgx-tKJNE2R6mUqhhc2BwPxDqK91ymaRNElMzZbgKH166Jw_rzMsz5QCMUQ4mjsMdoDhYvpu4x0oHRCkqJkpWqP8tEkVCd5mdCzcJ_LlQ74lKLDH5b4LcWwsx8tzGP_HsrSGGCkv7Px7txsEMSs34y7KaP0B0KHn2o61m_qEIz1TdNHBDAgAao4epa2davLy4O2yBMXLsqZDS-DUeRqfe2GZ9EG_ZkI410SrnK0zePBHZzdBCo-hW35Tvn7QP9HuOYiEKqOR-LHBoO7JIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqI3X06qoUpeLheWxsZRVfBiI3AQuGXye88RpeiVVIH3d9e-ywFjTyaSTCjnRtgZT9t8W5fMrPn6DzcHeSQFrxkukfLJR7qCL9bS4ubj0uK49kJrv4wdmhqaAeZLhn6Jd1q4Tji4VW83Rs547L4O2eYVA_iCGieVvMCQjcy9XohB4ELbekvJ1UulJhF4iaskGjh1kN_T0q0SleSJlI8ElHgSMD90cAnNfvqT-aGClDlK2ovzTA-tOfthdbYaDFgLHqJGtnnv18fdd-UaH4vGJZ_UeGA2TsUaWDTDdVQmlGAc4uqgOl5fRnO5pg0OmoP52mzl_QY06CatBJoyYBL2EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
من التجارب الصاروخية الذي ينفذها حرس الثورة في الجمهورية الاسلامية الايرانية.  الكويت تشعر بالقلق</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/naya_foriraq/93241" target="_blank">📅 13:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93240">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇾🇪
وزارة الصحة اليمنية:
إصابة 6 مواطنين بينهم امرأة وطفل جراء استهداف العدو السعودي منزلا في حي سكني بمنطقة باب شعوب بالعاصمة صنعاء.
لن يستنكر احد ويقول مدنيين
ولن تنشر الدول بيانات ادانة</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/93240" target="_blank">📅 13:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93239">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYvqGGR1dSsBDjz7NLRupwg7Xkki-upu01CwNgDqAArtYyXUSJypY3zl7IUigUzjfALKT7Tic173eTEa5krDkDGTGNnB7lgYuKVWoIxul3ssYSZxNOP-Y-0pbUxKGocsiC92jdF2IGN6PJF2fkYwsOVF0LysBuHXDBBpRvVNt_IB_Gy1MdzpDhNFzJL81e3BUcVLvbc-1I_Fgd1eBz84aG43oCylbka_36ZTa0Wy_PDB1hPJ6SHsvbqAdW7fvmL4GQjjpKZHQ5cTZi3rgEzXPn72Oz9fgFBuwtcBcQ44AfhyVrgzDSGYFRdp2k4mxVhs1MVzKCgv6VaSGFoThb7Awg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
مصدر إيراني لنايا   الحرس الثوري أطلق قبل قليل ثلاثين إطلاقة تجريبية من الصواريخ البالستية خيبر شكن وعماد على سبيل التجربة .</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/93239" target="_blank">📅 13:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93238">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وفاة 109 أشخاص منهم 15 طفلا  وفقدان أكثر من 116 بغرق سفينة قرب جيبوتي</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/93238" target="_blank">📅 13:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93237">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
ما لم يكف العدو السعودي عدوانه وتدخله في اليمن فالقادم أعظم بإذن الله.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/93237" target="_blank">📅 13:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93236">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
🔻
مصدر إيراني لنايا   الحرس الثوري أطلق قبل قليل ثلاثين إطلاقة تجريبية من الصواريخ البالستية خيبر شكن وعماد على سبيل التجربة .</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93236" target="_blank">📅 12:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93235">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الله اكبر
🔻
حرس الثورة يجري مناورة واسعة بالصواريخ الفرط صوتية الان داخل ايران .</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93235" target="_blank">📅 12:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93234">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Homayoun Shajarian - Iran e Man (همایون شجریان و سهراب پورناظری…</div>
  <div class="tg-doc-extra">Melodifa</div>
</div>
<a href="https://t.me/naya_foriraq/93234" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#شاركها</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93234" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93233">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الله اكبر
🔻
حرس الثورة يجري مناورة واسعة بالصواريخ الفرط صوتية الان داخل ايران .</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93233" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93232">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات المسلحة اليمنية تتمكن من تحرير قرية الصياحي وسوق المقهاية واجزاء من وادي الضباب، وبذلك تم قطع خط الضباب ومحاصرة مرتزقة السعودية في نجد قسيم والمسراخ بمحافظة تعز.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93232" target="_blank">📅 12:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93231">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔻
وزارة الداخلية البولندية:
الشرطة تلقت معلومات عن هجوم محتمل على رئيس الوزراء ووزير الدفاع.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93231" target="_blank">📅 12:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93230">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇾🇪
دوي إنفجارات في العاصمة اليمنية صنعاء ،وسط أنباء متضاربة بين عمليات إطلاق صواريخ نحو الأهداف والمواقع المعادية من قبل القوات المسلحة اليمنية وعدوان سعودي.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93230" target="_blank">📅 12:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93229">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
🇸🇦
الحكومة العراقية:
نستنكر الاعتداء الذي طال مطار الملك خالد الدولي في الرياض والذي أدى إلى سقوط ضحايا أبرياء ووقوع خسائر مادية وبشرية، بما يسيء إلى الأمن والاستقرار الإقليميين.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93229" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93228">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
البنتاغون : سيتم بث إعدام مطلق النار في فورت هود رمياً بالرصاص في الولايات المتحدة على الهواء مباشرة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93228" target="_blank">📅 11:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93227">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
دوي إنفجارات في العاصمة اليمنية صنعاء ،وسط أنباء متضاربة بين عمليات إطلاق صواريخ نحو الأهداف والمواقع المعادية من قبل القوات المسلحة اليمنية وعدوان سعودي.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93227" target="_blank">📅 11:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93225">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇾🇪
العميد يحيى سريع:
القوات المسلحة اليمنية تجدد تحذيرها لكل الشركات الملاحية الجوية والخبراء والموظفين والعاملين والمسافرين من استخدام المطارات والأجواء السعودية لأنها معرضة للاستهداف ومسرحا للعمليات من قبل قواتنا باستثناء مطاري مكة المكرمة والمدينة المنورة.
وتهيب بالجميع لأخذ تحذيراتنا على محمل الجد وتتحمل السعودية مسؤولية أي اعتراضات فاشلة. وتؤكد القوات المسلحة أنها ماضية في تثبيت المعادلات المعلنة معادلة المطار بالمطار والحصار بالحصار والتصعيد بالتصعيد حتى تحقيق أهدافها.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93225" target="_blank">📅 10:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93224">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3s3UqnlmElU3lMDyRtJuaCVtF1vh7mN2VUEkFnjRUObJresWCbY_9gCKcBkGADpNuO8KghusOtlO7bgri3oJAX9Eb2_5uKO0sJw9J9OKOkQ8hCYzNnPkYgz4yybgldDbUK1cZcqq5bnhIB-2Csaxxi74XV484Rcu6gmIo45IfirBlanmfc89CfGqiCKl77ojOLyYtx1i7Pu1z7eram9JrP4qoO1Nmmr5gg5G7aCOZjfTelA-0zGYp0TX2i8BmYto4V0PDR2ndwsB9GZOtsLLR-H0-o09AGqXBx_TNuQFR4OD_3OW1nPvI7hNOED1ddJG_ynDxClEhkqLmme1PQASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المعارض السعودي البارز حيدر القحطاني يتحدث عن الأوضاع المأساوية داخل السعودية في ظل أجواء الحرب وكيف ورط آل سعود البلاد وشعبها في صراع بات المواطن السعودي يدفع ثمنه من أمنه واستقراره وحياته اليومية وسط مخاوف متزايدة من القصف وتداعيات الحرب  رابط التغريدة</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93224" target="_blank">📅 10:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93222">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OM6TtPIl19whJyCaIKKTXLMMR-kW8tm9JDDiQH0reKAYoRbta8DD3Wu36OrOMk4NeUa165T2tJUN1hXiYuNJs9Mh9IfK_jmYE4q_3aiw-K2pN41gk7LjoI1PiFQdTTuVWJi7Vxz-1OhTXlJlvhUSV8_Btbr_Z74YjZYK4pWhYDpBEECJNeYozNvsfeIbi8rKmLrYXo0ksu8ivZlOPCgtOkuTT6Prg9y5PDSQJnGZgLuQu0EKXTa4-ve2AvADfVmb0J6_5pj3HdxHwVdy7XmlcncCP6Z5j_JP5T8wfN2qFQWl-nC1LS0BCuTgB5S9XnoYwmY40xqpp67vSWnswGDZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsGzrjHSzPFvSIRJLWmJVJoPhQ1tbkf3eWeoZbU0un4n6BGk_R0S4FK52WnKJBvch0KXQdbAIryu__sR2TWzVMb55ZnAYSg8rCmPPdtSNaqo8x51kb1TWQCjuWfP_UGhQeXgNqhxzRJOkrE6im1dwZ-BrK9mEI1SkHOPsE9Splmp9piN9Y4XXxqEdBEHVqHFC7ZVVt6s89mFcPPlaGEZ-RRFIVSqxzcl9aeiISVueHqRYdcV9ihQ0qfMlST_yqMmFuFpva-8QDNUwg1LHxwXVA2SmgpgYjn1yiNam1lbwPXmZ6F7AZCTNCmZ_D6WIGmI6o_dtbBIYZWIFf6eyKB-FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">المعارض السعودي البارز حيدر القحطاني يتحدث عن الأوضاع المأساوية داخل السعودية في ظل أجواء الحرب وكيف ورط آل سعود البلاد وشعبها في صراع بات المواطن السعودي يدفع ثمنه من أمنه واستقراره وحياته اليومية وسط مخاوف متزايدة من القصف وتداعيات الحرب
رابط التغريدة</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93222" target="_blank">📅 10:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93221">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c0e97186.mp4?token=E4Y-TBWtrm3UxzodJKUUxgtW6m5zMdqvx7LBhLGQjMskbASb_jLDCekbvrrVn-tgKJGYcmHHnV-SaFOnSCzK879T3J3LRSwqLr52rAZK-mCZlNBXtvKDK9pEFcvOss3sR65qXgjnBaqV1xT5ShT26jQmLTLvGjpdPFuZg3xVmwK1LwB84CHSDDGowGWVOobVMJv7JbUTEZ4TAS6mt6MoambMcH1e1tpmKBaX1rVavNRBU7FuStthDw1GsULYpb7mt7dCuRYgxT26jUkEyyClCGhTuwZigQ7pCzIg02y_xNFwLSGUNFjPE8DCFmGdhRxJTFvg4Hd8tziHay0mQuig3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c0e97186.mp4?token=E4Y-TBWtrm3UxzodJKUUxgtW6m5zMdqvx7LBhLGQjMskbASb_jLDCekbvrrVn-tgKJGYcmHHnV-SaFOnSCzK879T3J3LRSwqLr52rAZK-mCZlNBXtvKDK9pEFcvOss3sR65qXgjnBaqV1xT5ShT26jQmLTLvGjpdPFuZg3xVmwK1LwB84CHSDDGowGWVOobVMJv7JbUTEZ4TAS6mt6MoambMcH1e1tpmKBaX1rVavNRBU7FuStthDw1GsULYpb7mt7dCuRYgxT26jUkEyyClCGhTuwZigQ7pCzIg02y_xNFwLSGUNFjPE8DCFmGdhRxJTFvg4Hd8tziHay0mQuig3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
تسلل طائرة مسيرة من جهة الحدود اللبنانية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93221" target="_blank">📅 09:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93220">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
ترامب:
الهجمات ضد السعودية كانت فظيعة والسعوديون قادرون على الدفاع عن بلادهم.
لدينا اتصالات مع الحوثيين وسنرى ما سيحدث ولكن ما فعلوه كان سيئا للغاية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/93220" target="_blank">📅 03:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93219">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610dacafee.mp4?token=i90BeQ22TA1BDzWMTkTddk6GWgfUhtH4Ga1YTEVjOzDfZPxlOBJYUcVrWjFBZHi8P0ax4lsbfcSkbWDCJw53qX2wa8XRXSrbbMj0hPh9v2fcqx_Jr3uU4qYHOEVvgxjdguckCcn2yQraK4AGwHSbfaaf6JGqLPjc8S-bGn-WGBH6u-NLxa_34N5C4yb-CBpcUBrFNMONHAu1OtJwxeIC1mEimpitp3fLLVPE5bAPHnDAgQofR-NA56olFiJ5Q6vNwXDYkPieFAF3GIbwepHgH0cNnjx1evZ3Bn0uZUmu-Mgfh8pg80V8lGRuaWF22gpM4Yx8cug5RLyb_oIIUdbRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610dacafee.mp4?token=i90BeQ22TA1BDzWMTkTddk6GWgfUhtH4Ga1YTEVjOzDfZPxlOBJYUcVrWjFBZHi8P0ax4lsbfcSkbWDCJw53qX2wa8XRXSrbbMj0hPh9v2fcqx_Jr3uU4qYHOEVvgxjdguckCcn2yQraK4AGwHSbfaaf6JGqLPjc8S-bGn-WGBH6u-NLxa_34N5C4yb-CBpcUBrFNMONHAu1OtJwxeIC1mEimpitp3fLLVPE5bAPHnDAgQofR-NA56olFiJ5Q6vNwXDYkPieFAF3GIbwepHgH0cNnjx1evZ3Bn0uZUmu-Mgfh8pg80V8lGRuaWF22gpM4Yx8cug5RLyb_oIIUdbRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي:
قامت قوات القيادة المركزية الأمريكية بتعطيل سفينة شحن تجارية في خليج عمان، في 10 أكتوبر، بعد أن تجاهل طاقم السفينة التحذيرات المتكررة وحاول اختراق الحصار البحري المستمر ضد إيران.
‏أصابت طائرة مقاتلة عسكرية أمريكية مؤخرة سفينة الشحن "أوشن موليكا"التي ترفع علم بنما، بذخيرة دقيقة، مما أدى إلى تعطيل نظام الدفع بالكامل وكانت سفينة الشحن الكبيرة تحاول عبور المياه الإقليمية بعد أن غادرت ميناءً إيرانياً.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/93219" target="_blank">📅 03:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93218">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوي انفجارات في المنطقة الشرقية  في السعودية إثر استهدافها بعدد من الطائرات المسيرة</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/93218" target="_blank">📅 03:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93217">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكية:
‏
تدين الولايات المتحدة بشدة الهجمات الأخيرة التي شنها الحوثيون الإرهابيون على المملكة العربية السعودية، بما في ذلك الهجوم الذي وقع اليوم على مطار الملك خالد الدولي في الرياض والذي أودى بحياة العديد من الأبرياء، بمن فيهم مواطن أمريكي.‏تُظهر هذه الهجمات الشنيعة استهتاراً صارخاً بأرواح المدنيين الأبرياء. يجب أن تتوقف فوراً.‏نقف إلى جانب المملكة العربية السعودية وشعبها، ونعرب عن خالص تعازينا للضحايا وعائلاتهم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/93217" target="_blank">📅 03:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93216">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
🇸🇦
هجوم صاروخي يمني يدك محافظة الخرج السعودية.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/93216" target="_blank">📅 01:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93215">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeINRjHi0mYrQuISdtxnCZpyEqW-d_-QAf8lo9G-3hTBEjICKriil8MIUde5NM8IlNnt9d5nhQvoNxFa_rNDcjbPWz_64wtWi9cZTQV_eUdzCO6B4Tholk12nZwqaWL7Wcaq4vmuz-1eKa07Y9q_WV9fQCHOycgJB14P6gG4vr84hhqL77-C8fGZpKpGsQglWARZKpgE0gYKdlg6EPlBIafiuMqYPULn1gXWpcjuoTn12nD1NOfaeTrHkuw_B5oJX4rpluAX132XO74fCLnWHPJ8BrqVRyKFPIhmDOEx6jAIPTXz2I6Hry9eq-1dRgW3-sjhh7ttI5XLVwnh-bSvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إستهداف ناقلة نفط بمقذوف حربي في مضيق هرمز قبالة سواحل عُمان أدى إلى إشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/93215" target="_blank">📅 01:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93214">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705fd22f65.mp4?token=Zn2-cHK-Z6E1LouTW14T-Jx_5fzyKlikyqOfEcH3Q0253VCZofB1E7T9D4qAw07TM3il1hJVBp3OZLVIrLyRwF4yPxLZSCX20Xlc77D7ck_fIbYHyubJQJIFx5YNLZhE2fbJxH644U0etWulo6Ot0vPPWuz0fOUeLQyKm-qPB3ylTn0zuWo5cqMym8qIyjBzqZJ3jH4UeXFHqYkHroMtc_CtNKqaMLcLWpYOff1q9TfUPrvmjZsHvawa58Rgy33GSaLHwfdRdmkz_AsAwQKvp5N5yOoP_W7dkwJ003zVYTga6nRN8bllTqot9sQV1jpn8VGxdgaX6d3FVbKUON3iZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705fd22f65.mp4?token=Zn2-cHK-Z6E1LouTW14T-Jx_5fzyKlikyqOfEcH3Q0253VCZofB1E7T9D4qAw07TM3il1hJVBp3OZLVIrLyRwF4yPxLZSCX20Xlc77D7ck_fIbYHyubJQJIFx5YNLZhE2fbJxH644U0etWulo6Ot0vPPWuz0fOUeLQyKm-qPB3ylTn0zuWo5cqMym8qIyjBzqZJ3jH4UeXFHqYkHroMtc_CtNKqaMLcLWpYOff1q9TfUPrvmjZsHvawa58Rgy33GSaLHwfdRdmkz_AsAwQKvp5N5yOoP_W7dkwJ003zVYTga6nRN8bllTqot9sQV1jpn8VGxdgaX6d3FVbKUON3iZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب عن إيران:
أولئك الشباب الذين فقدناهم في الحرب ضد إيران لم يموتوا سدى.
لا يمكن أن نسمح لشخص مجنون تمامًا بحيازة أسلحة نووية.
إيران دولة شريرة للغاية. إنها الدولة الأولى في مجال الإرهاب.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/93214" target="_blank">📅 01:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93213">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇸🇦
السعودية تعلن عن مقتل 12 شخص بينهم أمريكي ،وإصابة 309 أخرين نتيجة الإستهداف الصاروخي اليمني الذي طال مطار الملك خالد الدولي في العاصمة الرياض.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/93213" target="_blank">📅 01:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93212">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔻
بلومبيرغ:
تشير تقييمات الاستخبارات الغربية إلى أن إيران احتفظت بقدرة إنتاجية كبيرة للصواريخ والطائرات المسيّرة رغم الضربات الأمريكية الإسرائيلية. ويقول مسؤول إن روسيا تعيد تزويد إيران بأنواع إضافية من الصواريخ لم يُكشف عنها.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/93212" target="_blank">📅 00:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93211">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر لنايا:
هجوم صاروخي يمني يدك مواقع حساسة في مدينة جدة السعودية وأعمدة الدخان تتصاعد منها.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/93211" target="_blank">📅 00:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93210">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">توقف الرحلات الجوية في الدمام-بقيق شرق السعودية</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/93210" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93209">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c921dc7e9d.mp4?token=CG_VQrnp-fWXrFa6zLTV6kZdtwJBNSyn6St6LXdsero420CyXo62bplUldIK6uYtOj8J0rwlnmBvcUbua3Y9SnBPNUc1CFFj_KmKVMxQfeHbkeUVbNYvW_G05xGOl3kIZO-lqYF8QVWR1QwdFdqypOgNzbe3Lxk7kn2UEh8YI2_n0OcCHNrJ-udqjaHSWkvO0_X0mkdNey7w-b5LmSR2eIQR1RcXGrR9vv3euuaSCS2bqJhhC-rjGLC_3vkSQYFguiKyTMDq_YdWmqVNIFIt4QCttP96NHlZ019pnQnVR6-fz-X-d-kdl4n2yhJGe-6BSuRY7uvLCEiTWQ_IGGvSNkCSBjvyJImKSOE9zG3Rp8rxJY7mczqnTYCAG4VOFqovPwsjmhVyqtTzQ2nHt9YeADZ5AgVxHdcXtr8Q9ioNDCkN2xFpEVWBir5LIshpsye8NY4A8vxyCnCPfkP-K09qakCZ8v0bpi7j2Vqnp6f8SNwckjcEsR1XCHAbpJ9Z0w14iQ6yYqaajmM09rd3la8bVhzA5ioPoi4Asbr4RlEV2fWocT62Co4unSQY55KwsuXjT3Fghd11jkgHuXZc402Hx1nn0k_KVfblz2XCSEqYFtMofMSxQreRmW-O0shQP2tBLksRN5myrrmP45anz6o0896plw42E9ncGOn9wtQtRLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c921dc7e9d.mp4?token=CG_VQrnp-fWXrFa6zLTV6kZdtwJBNSyn6St6LXdsero420CyXo62bplUldIK6uYtOj8J0rwlnmBvcUbua3Y9SnBPNUc1CFFj_KmKVMxQfeHbkeUVbNYvW_G05xGOl3kIZO-lqYF8QVWR1QwdFdqypOgNzbe3Lxk7kn2UEh8YI2_n0OcCHNrJ-udqjaHSWkvO0_X0mkdNey7w-b5LmSR2eIQR1RcXGrR9vv3euuaSCS2bqJhhC-rjGLC_3vkSQYFguiKyTMDq_YdWmqVNIFIt4QCttP96NHlZ019pnQnVR6-fz-X-d-kdl4n2yhJGe-6BSuRY7uvLCEiTWQ_IGGvSNkCSBjvyJImKSOE9zG3Rp8rxJY7mczqnTYCAG4VOFqovPwsjmhVyqtTzQ2nHt9YeADZ5AgVxHdcXtr8Q9ioNDCkN2xFpEVWBir5LIshpsye8NY4A8vxyCnCPfkP-K09qakCZ8v0bpi7j2Vqnp6f8SNwckjcEsR1XCHAbpJ9Z0w14iQ6yYqaajmM09rd3la8bVhzA5ioPoi4Asbr4RlEV2fWocT62Co4unSQY55KwsuXjT3Fghd11jkgHuXZc402Hx1nn0k_KVfblz2XCSEqYFtMofMSxQreRmW-O0shQP2tBLksRN5myrrmP45anz6o0896plw42E9ncGOn9wtQtRLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف سفينة مخالفة مقابل السواحل الاماراتية</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/93209" target="_blank">📅 00:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93208">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aefc2bfca.mp4?token=Gsgnd7p-VS4MKx_-Fsw2Cgy1ev0uQ8Ducj_WJ-mb_UIZdAFEEELqglZjBX9FRNuC9fx1a3MC3XXJbXmvj9WBUdw0J3g6fWW3iygOxmhufx-nWgS99C6cZJF8TgfaS09KMVsybuO9AvrCWnHW97kPFALBDklIualFqwyu9bBm3fbpHhgm3alZX-HZVoh_yjYWbgWeqJYa7ljLnzTD5f-g_ynx4CT8ZG_T5nyNWfkrq_U8cnt32gme-0R-8QRTDILkPmrZUj60yg1_DU_cY4c4Yq3lagBPswbXEV4wYMNDa6Juu-d1WrAT6YHzRJG72VZieowRBTfM3GOtgYAeIYSZZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aefc2bfca.mp4?token=Gsgnd7p-VS4MKx_-Fsw2Cgy1ev0uQ8Ducj_WJ-mb_UIZdAFEEELqglZjBX9FRNuC9fx1a3MC3XXJbXmvj9WBUdw0J3g6fWW3iygOxmhufx-nWgS99C6cZJF8TgfaS09KMVsybuO9AvrCWnHW97kPFALBDklIualFqwyu9bBm3fbpHhgm3alZX-HZVoh_yjYWbgWeqJYa7ljLnzTD5f-g_ynx4CT8ZG_T5nyNWfkrq_U8cnt32gme-0R-8QRTDILkPmrZUj60yg1_DU_cY4c4Yq3lagBPswbXEV4wYMNDa6Juu-d1WrAT6YHzRJG72VZieowRBTfM3GOtgYAeIYSZZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب يتحدث عن ايران:يمكننا إنهاء الأمر بسرعة كبيرة. إنهم لا يعلمون كم كنت لطيفاً معهم.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/93208" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93207">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
رويترز : ‏أذنت وزارة الطاقة الأمريكية بتبادل طارئ لما يصل إلى 4 ملايين برميل من النفط الخام من الاحتياطي البترولي الاستراتيجي في أعقاب إعصار إيساياس. ولا يزال نحو 69% من إنتاج النفط في خليج المكسيك و57% من إنتاج الغاز الطبيعي متوقفاً</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/93207" target="_blank">📅 23:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93206">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkuS-jd-o9MpkQIln8WxqDuGX5uT_8BzEMnZ8o6JhBv0Bwo-MkzX_rY3j44hO58jhahHnvKlkYJQ-BEEq-zjbep_x_2ghH-6hMrLR3xwzpcEEKcMImCms0DSu75ZAqsiUmMOQBk-wmNZ5DREyZ9wQF3nHIs2PyrgAuLvYrtFlx5oGSl8a8HelVW-tUSq8TSZyGyEpL9XZGzcRbQy_IbMO_lkA8RoNCgaOr95kjtuyopubwymrzjrHYNaUvB8Nxhl5PSSFad-tcTB612hx5EixzLI74OlXAe6vD0LN5cb6_WmXv5S2nq4fDHy806hc4TRdGwT5gRbgEEHPFpNbC-Ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف الرحلات الجوية في الدمام-بقيق شرق السعودية</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/93206" target="_blank">📅 23:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93205">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
رجل من بني كعب يتدخل لمزج الألوان بين الأصفر والأبيض ويطفئ اللون الأحمر الذي قد ينتج من الهوسة التي بلا معنى  .. ابو الاء الولائي يخرج منتصرا سياسيا وميدانيا وعسكريا و النتيجة هذه المرة ٢ لكتائب سيد الشهداء صفر لاعدائه  …</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/93205" target="_blank">📅 23:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93204">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhAalg61wFYVyFf95dfQ4N4u8WW61nvy-u1SLN6q3XwJzHML0aQozfiLTUPc85jhPsK6qVgF4iwaLOcB46WR7S-Hc38YsijduPGhaRXmJfecNVhGyRPifcVwFfFNT1xq-Nlc4QNlSOiHP1uES9I6Vn4nm6Kb3fckP0GDkEW3lOquyfJnEeYQbw8xP7iY_oTrMsZGgtxPI_EQFzLkZx2nxz6hWruEUp2lAFmcKVFXOWx97qpIbP3j2fWMU5SN_IRk7wWd7qhxHbQoMNWvYSK2jF_FkhrXZQPYOtbYfJ6va_YcOtVoMyVy4IfSuShZF4kKYo2U_4SMf6swyq1gNlllGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بقائي:
لإخافة شعبهم، يستحضرون عدواً وهمياً في السماء للتغطية على التهديد الحقيقي على الأرض.
‏لا يكمن الخطر الحقيقي خارج حدودهم ولا في سماء لوس أنجلوس وسان دييغو، بل يكمن في نظام حاكم فرض حرباً غير شرعية على العالم، ذات عواقب عالمية.
‏بل إن الرئيس الأمريكي وصف تدمير لوس أنجلوس وسان دييغو بأنه "ثمن زهيد للغاية يجب دفعه".
‏هذا مثال نموذجي لسياسة الخوف: تخويف الناس بتهديد وهمي، وتصوير تدمير مدنهم على أنه ثمن مقبول يجب دفعه، وتحويل انتباههم عن الخطر الحقيقي.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/93204" target="_blank">📅 23:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93203">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8RwchJkyNCrGYWMlqoMP5W3EeboK0SCvjPTYBiFM0vwq0x0n7ZDemjomGldocVD3vwwAKV-kCFU1M8P7HmR3odtAlbrtuUR29fH1j25dEP654glS9EikB6znAZkgk_DJgFsyo-IvuNC7IKVW1G2IiofvLNcd3ZMqgsq-ES8cnQ195LYHrDEYM6L1OG8B5M3hN2OM4Ba50-TwUKJTKFPudSLzAMlEP9rx3vYZL9EtoA2yHgnrfsi89pcY7CDLEXozlAnCMPC_ZvLdCo6qX8a-y--2VTMoHWXzPZtHMAQvk-_qlKs9GRfSVNWEQvQsneORUxr2FL2Y9y5vRquIDIMcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
استهداف سفينة مخالفة قرب السواحل اماراتية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/93203" target="_blank">📅 22:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93202">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
مصدر يمني مسؤول للميادين:
تفاجأت السعودية من زخم الصواريخ اليمنية ودقتها، هناك خشية من طول أمد الحرب وبدأ بعض الشركات والمستثمرين بالتفكير في مغادرة السعودية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/93202" target="_blank">📅 22:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93201">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
انباء عن تفعيل الدفاعات الجوية في مدينة ارومية شمال غرب الجمهورية الاسلامية.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/93201" target="_blank">📅 22:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
البنتاغون رفع عدد قتلى الجيش منذ بدء حرب إيران إلى 21 بينهم اثنان خارج العمليات القتالية.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/93200" target="_blank">📅 22:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
🇾🇪
‏تحذر القيادة الأمريكية في أفريقيا (أفريكوم) من أن التعاون المتزايد بين الحوثيين في اليمن وحركة الشباب الصومالية قد يهدد القوات الأمريكية والسفن في خليج عدن. ويشعر المسؤولون بالقلق إزاء عمليات نقل الأسلحة المحتملة، وانتشار الطائرات المسيرة، وتوسع العمليات المسلحة.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/93199" target="_blank">📅 22:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇸🇦
فايننشال تايمز :
أحد المستشفيات القريبة من مطار الملك خالد الدولي بالرياض استقبل نحو 50 مصاباً، بعضهم في حالة حرجة، عقب الهجوم. كما تستقبل مستشفيات أخرى مصابين، في حين فعّلت المستشفيات الرئيسية في الرياض بروتوكولات الطوارئ.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/93198" target="_blank">📅 22:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
🇸🇦
‏الخارجية الاميركية للمرة العاشرة تصدر تنبيه امني بحذر السفر للسعودية وبالاخص المناطق المعرضة للاستهداف اليمني.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/93197" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9B3BaYtM57Ia9Bq8zngyDtPPzVis6hrYaK_DzPasnvnzMhRWc77aQsTP85psZs-Bqyh2BSkWvqxJIBv9v5nMOacmzjWQw-r7CIVX0JYJNzj8S-SRv2NE_xf29fpp2AXvcEOWxWaHQFbtL3Q_qeMahLwUJK9ZBzgnefbFfj-7FbuF2KjEsIUotGJiNvQPKYRKF2QnM4JENA7sdn4nZxR-0nnLd9oQLyU0Zos4Fq4SOIPoy8GWBgQHt4vMZyQhIdrmY_Z8-yoUC_WWnoU4bAtgxC6nlJWounQxBdelIguB15_Dd_94eoIn7Z4TC0LhUtUcb2WBt-dCslYvYriTlp5cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مشاهد للناقلة النفط التي تعرضت للاستهداف بلغم بحري.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/93196" target="_blank">📅 21:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">لحظات تسليم مجاميع من تحشيدات العدو السعودي للقوات المسلحة استجابة لقرار العفو العام
من مشاهد تأمين ما تبقى من مديريات سامع والصلو والمواسط - 10 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/93195" target="_blank">📅 20:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
مشاهد للناقلة النفط التي تعرضت للاستهداف بلغم بحري.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/93194" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93193">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇸🇦
‏وزارة الخارجية السعودية تدعو المواطنين الذين تأثرت رحلاتهم أو تعذّر وصولهم إلى وجهاتهم نتيجة إيقاف أو تأخر بعض الرحلات المتجهة إلى مطار الملك خالد الدولي إلى التواصل مع بعثات المملكة في الدول المتواجدين فيها، وذلك لطلب المساعدة وتقديم الإرشادات اللازمة.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/93193" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93192">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
الحرس الثوري
: استهداف سفينة في مضيق هرمز بلغم بحري.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/93192" target="_blank">📅 20:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93191">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7241acac33.mp4?token=qUKOyF2w4lr1PmOp_ucGD9xyY6sUn57hCuzEBiFpPK9CEzXqF3HQ1b5JWONCFm5EIp5TvomVk1_HpDArwyzjcfAczBqonEH9ZxrhXdoxsY7yHv4wzsxk2bDAA0WzVU96K03e5jG-v_VUSPi0S43swPXhwuKgZS6bOtG6i3W8IoCq7wFjPEtP4EsScbmFHdoj4NgCfh7u0wJpWcvtwKAcydjmL87AOZiCGlKd0D5FWJMPlACwx3dplPxp3rc9_8yleOORhz2WXEayahI8jJqJXSkGeK8Bz59bugRm6aNPEyCE6H_iJOgxcf3Ja2WVQC-jJUINi8bNLJgpJ43DZdWdYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7241acac33.mp4?token=qUKOyF2w4lr1PmOp_ucGD9xyY6sUn57hCuzEBiFpPK9CEzXqF3HQ1b5JWONCFm5EIp5TvomVk1_HpDArwyzjcfAczBqonEH9ZxrhXdoxsY7yHv4wzsxk2bDAA0WzVU96K03e5jG-v_VUSPi0S43swPXhwuKgZS6bOtG6i3W8IoCq7wFjPEtP4EsScbmFHdoj4NgCfh7u0wJpWcvtwKAcydjmL87AOZiCGlKd0D5FWJMPlACwx3dplPxp3rc9_8yleOORhz2WXEayahI8jJqJXSkGeK8Bz59bugRm6aNPEyCE6H_iJOgxcf3Ja2WVQC-jJUINi8bNLJgpJ43DZdWdYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب
: لقد مُنحت جائزة نوبل للسلام لشخص لم يسمع به أحد من قبل. كل ما نعرفه هو أنني أعتقد أنها معادية جدًا لإسرائيل، هناك شيء خاطئ في النرويج، اسمحوا لي أن أخبركم.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/93191" target="_blank">📅 20:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93190">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇱
تسلل طائرة مسيرة من جهة الحدود اللبنانية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/93190" target="_blank">📅 20:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93189">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba43f57de.mp4?token=lwdGG-k6E99p51FkqO0ZyseAEbyFCiyFJYA5342kTX6a5vYpmUNmgVy-g_PurQunUWxmaa_0P96__JS1j8bscQMcJwOhL8uSz0mKQTfzQ463BcwdQumyzDFojw7wru4jkcWsQQECjH5lAjpKCd-YtzOpvPJkH9K8HpoR0TnCYE__BuoHqCnxYraWOxOADbRm2xGaU2ImVzQlzX6tJGStCPCYPRt_NL3gQhVhupS-5Pn0K5cNXnm5zKL_lddBADXqbKdvRN6uUaq1KtMws79ZoVe6tDAtsorpZR_DghIchldqwC9dQWfLAlAXxunl3KwqYE-F_1etTgyWDSs8oW7VH33gpFzuw5pFqFkQKJJOYH5c_F31cLpIr6pbHNy-YkxJVxLxjo-Mr8MGdauRtuwgKuKOaMCFknHUtrkowI0nSSfkYOtSO8Ft2ObmqgTvwyO1Ac3sb3qeq5jLZpoJbJnwcWniG-kJJsPu78T_9NmaHgoxRZtRUcdzl4HaXaorlPokuqJVjI0iSeZCv4gsqM_-lS_WeW0YdhaKEa7dKfh-pwR3r69So5908SoY2IgTuXVI1vbwaZD82pLzo-rUeDe4fxZYvBXhWu_cFwLbzpyYOCHX3-7pFHbVj_G8NaSOnX34cTGQoJV1nLg1KVX8kJtqcJ9xTUrlAcw8qhL7ENsLeg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba43f57de.mp4?token=lwdGG-k6E99p51FkqO0ZyseAEbyFCiyFJYA5342kTX6a5vYpmUNmgVy-g_PurQunUWxmaa_0P96__JS1j8bscQMcJwOhL8uSz0mKQTfzQ463BcwdQumyzDFojw7wru4jkcWsQQECjH5lAjpKCd-YtzOpvPJkH9K8HpoR0TnCYE__BuoHqCnxYraWOxOADbRm2xGaU2ImVzQlzX6tJGStCPCYPRt_NL3gQhVhupS-5Pn0K5cNXnm5zKL_lddBADXqbKdvRN6uUaq1KtMws79ZoVe6tDAtsorpZR_DghIchldqwC9dQWfLAlAXxunl3KwqYE-F_1etTgyWDSs8oW7VH33gpFzuw5pFqFkQKJJOYH5c_F31cLpIr6pbHNy-YkxJVxLxjo-Mr8MGdauRtuwgKuKOaMCFknHUtrkowI0nSSfkYOtSO8Ft2ObmqgTvwyO1Ac3sb3qeq5jLZpoJbJnwcWniG-kJJsPu78T_9NmaHgoxRZtRUcdzl4HaXaorlPokuqJVjI0iSeZCv4gsqM_-lS_WeW0YdhaKEa7dKfh-pwR3r69So5908SoY2IgTuXVI1vbwaZD82pLzo-rUeDe4fxZYvBXhWu_cFwLbzpyYOCHX3-7pFHbVj_G8NaSOnX34cTGQoJV1nLg1KVX8kJtqcJ9xTUrlAcw8qhL7ENsLeg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد من داخل مطار الملك خالد الدولي في الرياض تُظهر حجم الدمار والأضرار التي لحقت به جراء استهدافه من قبل قوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/93189" target="_blank">📅 20:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93188">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
حزام الأسد:
في حال انخرط الأميركي أو الإسرائيلي أو أي بلد في العدوان علينا فلدينا الكثير من الخيارات للرد.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93188" target="_blank">📅 20:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93187">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81359a42c.mp4?token=MVGszKJGnMtk4B6VxNDXTvOYwinhJanlRssf0g7Tng1vFQI_c0xHloWy7rC9cQ_6C30DAqnLi2KzVkteI7VdMpODgwtl3hlAvZuigEhoCsbAS95OmCc6xQqh7di5tgvlrloXcLib7Nv3pa55LBXtEenOhUqtJ0XC0ULlZ158MpbMGrsSA6wVyaNI0bHeC8naXIyPD6tWmrX44Ym-XFPkRbc2i8xfSC_HImgjAWqZyKiFBJM60UUeCxxUaIJ9huaaA9ejPB55UbLKSqYilxeRctOs0IFX-7xYeVJ8rrU2w3lCFUh_sBeDw9Ihg_Iz_hXH9MVK4o2uj2kJ3yTmW_WeBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81359a42c.mp4?token=MVGszKJGnMtk4B6VxNDXTvOYwinhJanlRssf0g7Tng1vFQI_c0xHloWy7rC9cQ_6C30DAqnLi2KzVkteI7VdMpODgwtl3hlAvZuigEhoCsbAS95OmCc6xQqh7di5tgvlrloXcLib7Nv3pa55LBXtEenOhUqtJ0XC0ULlZ158MpbMGrsSA6wVyaNI0bHeC8naXIyPD6tWmrX44Ym-XFPkRbc2i8xfSC_HImgjAWqZyKiFBJM60UUeCxxUaIJ9huaaA9ejPB55UbLKSqYilxeRctOs0IFX-7xYeVJ8rrU2w3lCFUh_sBeDw9Ihg_Iz_hXH9MVK4o2uj2kJ3yTmW_WeBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترمب: علمت للتو بوقوع هجوم على مطار الرياض وسأتخذ قرارا.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93187" target="_blank">📅 20:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93186">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fa8a96af.mp4?token=guB9qtwn2BdGStGYzcqGxjSANM3EID0qqjpZMAIIUcrqMGsedTT0fyXvYvGleH0Lltpe5Rn9ZB_oez6VqMEI_t-Qy-qt80Wg8AtsgcLrSm-bzhsDS2mal_OPhaXOj5lNvekRV0jYQGfNa6opwnJQ_OF5ZzHiVylAoJx5cRgIkK4T1qHoeMSN1D3H3AXwDWmNfbeRe5IoTKim56r9xw8Wz_HxTYN2vD6mxQc4nEzipA_bGNyDL-9Y2fWdcq30GRppqkhzoLc5wiTs-SktdCw0Gmb3lDwb1mkEP5iBfevyzjFPCkDcXGmuxPw3noKYMdxKktkpGbHJoxPG65M8kzPCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fa8a96af.mp4?token=guB9qtwn2BdGStGYzcqGxjSANM3EID0qqjpZMAIIUcrqMGsedTT0fyXvYvGleH0Lltpe5Rn9ZB_oez6VqMEI_t-Qy-qt80Wg8AtsgcLrSm-bzhsDS2mal_OPhaXOj5lNvekRV0jYQGfNa6opwnJQ_OF5ZzHiVylAoJx5cRgIkK4T1qHoeMSN1D3H3AXwDWmNfbeRe5IoTKim56r9xw8Wz_HxTYN2vD6mxQc4nEzipA_bGNyDL-9Y2fWdcq30GRppqkhzoLc5wiTs-SktdCw0Gmb3lDwb1mkEP5iBfevyzjFPCkDcXGmuxPw3noKYMdxKktkpGbHJoxPG65M8kzPCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اترامب
: يُريد زيلينسكي إحداث مشاكل للعالم. إنه يريد إحداث مشاكل لمزارعينا من خلال استهداف مصافي النفط الروسية."</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/93186" target="_blank">📅 20:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93185">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
🇸🇦
ترمب
: علمت للتو بوقوع هجوم على مطار الرياض وسأتخذ قرارا.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93185" target="_blank">📅 20:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93184">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92ec687fad.mp4?token=CoNn-7G8XarJbjGJVFQsucwf5sILcnMyLZErR5ZXatpBhVNATzxIUpcBhiWF0X9bl6lPGh20EHSCBZ-vjDpF3uDBr5PQCL8KCtx8BkWWz1J4O6ObvUcO0x3n9VSYeD08iF4QdPsAzX8IzJjaVwFm3cVyNYS7ILIbkKSJ6rne406880gkc0BaFGvnxqanG8U7i4Bh3ADim5Yz_MO_Qbo9Go3TAiHu0V8zCeeXrKh8ynL53E_jKo6p2bUdm1wHE_kGVtY59HL1-LJDm2LhDom1iyAb6YuUh3Y6goNKyiPkI5Q_BP6l3E62T1Y_wO4FZvppWP6dFohSvNPNt3O2uAHL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92ec687fad.mp4?token=CoNn-7G8XarJbjGJVFQsucwf5sILcnMyLZErR5ZXatpBhVNATzxIUpcBhiWF0X9bl6lPGh20EHSCBZ-vjDpF3uDBr5PQCL8KCtx8BkWWz1J4O6ObvUcO0x3n9VSYeD08iF4QdPsAzX8IzJjaVwFm3cVyNYS7ILIbkKSJ6rne406880gkc0BaFGvnxqanG8U7i4Bh3ADim5Yz_MO_Qbo9Go3TAiHu0V8zCeeXrKh8ynL53E_jKo6p2bUdm1wHE_kGVtY59HL1-LJDm2LhDom1iyAb6YuUh3Y6goNKyiPkI5Q_BP6l3E62T1Y_wO4FZvppWP6dFohSvNPNt3O2uAHL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
طيران المدني السعودي: تعليق العمليات التشغيلية مؤقتا في مطار الملك خالد الدولي، ووقوع عدد من الإصابات جراء الاعتداء الذي استهدف مطار الملك خالد الدولي بالرياض، والعمل جارٍ على حصرها.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/93184" target="_blank">📅 20:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93183">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇸🇦
طيران المدني السعودي:
تعليق العمليات التشغيلية مؤقتا في مطار الملك خالد الدولي، ووقوع عدد من الإصابات جراء الاعتداء الذي استهدف مطار الملك خالد الدولي بالرياض، والعمل جارٍ على حصرها.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/93183" target="_blank">📅 20:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93181">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af19485143.mp4?token=Tlg0Kuj-W3eP5OS4_HMA_gQ_257tKauf57VRZfOsf5MivPKrzpGFtWj41YZ0XxoT_tOKz1hu3Ncmcigrd4axynPuj7obQBL7FwYIjjcdbnq444Vo7ZW8w8SjqDhUUDwJDdotJP_QCH09tAXTkRY79DtzbDvqLnWkt6KqJztVtQ6bgWcfW8nNHG6sLIFVOK3-oqYHqGR1KMiCW5gfMBQs-GEHvfxBZv0N0EifF_CFUTtZX2-P-58GWehpIU6NNPorV9XhVsq6Y3yycRlprlAyYV9rYKAUDy5JvQQ8Yh1g20YO3e85NarGKz4Fkm5tuRwCKPsPiBSB34kKLy7ciIeI_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af19485143.mp4?token=Tlg0Kuj-W3eP5OS4_HMA_gQ_257tKauf57VRZfOsf5MivPKrzpGFtWj41YZ0XxoT_tOKz1hu3Ncmcigrd4axynPuj7obQBL7FwYIjjcdbnq444Vo7ZW8w8SjqDhUUDwJDdotJP_QCH09tAXTkRY79DtzbDvqLnWkt6KqJztVtQ6bgWcfW8nNHG6sLIFVOK3-oqYHqGR1KMiCW5gfMBQs-GEHvfxBZv0N0EifF_CFUTtZX2-P-58GWehpIU6NNPorV9XhVsq6Y3yycRlprlAyYV9rYKAUDy5JvQQ8Yh1g20YO3e85NarGKz4Fkm5tuRwCKPsPiBSB34kKLy7ciIeI_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد لمعتمرين أُلغيت رحلاتهم بسبب توقف الرحلات في مطار الرياض بالسعودية إذ يناشدون القوات المسلحة اليمنية السماح لهم بمغادرة السعودية بسبب الوضع الامني المتدني فيها.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/93181" target="_blank">📅 19:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93180">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇾🇪
🇸🇦
طيران العدو السعودي يستهدف المجمع الحكومي في سامع بغارتين وغارة على نقيل حوره بتعز.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/93180" target="_blank">📅 19:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93179">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
انتشار قوات الجيش اليمني في محيط مضيق باب المندب.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93179" target="_blank">📅 19:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93178">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇸🇦
الخارجية الاميركية: ننصح بالتحقق من حالة مغادرة رحلتكم مباشرةً مع شركة الطيران والمطار. كما يُنصح المواطنون الأمريكيون بعدم السفر بالقرب من الحدود اليمنية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/93178" target="_blank">📅 19:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93175">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APH4gmClvo6Hdy7Sb20KA0z8hjOG8n7qx1ZN4jQIEhHkBgGoQlFC212HDLifi2AROtkFXWqUlrgcU7KaHOHl215AhoFE-J8fRF4ElD92thYRb1RY42TE8XahxOErrEvP5CtoaLwaGi4j2ocpU3x8avtjJyG-oqCEb4pWLQvYoCPmmCO6_q38YXMJdUbj0Hk4PPYnXqaNnlkmijeEGOFlF6dDg-X_JupfEltRfPVuaNTD30MCst7v94imr2KmsdVqHdvbbandQTqZ0kVdNtIT2lZMU-KTdQaqFBIEAm3yr8XmxVfm9KjU_tYyCFJYwQo636SbcN-M5In0myATKS7mPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESEozKIoF6k5EOW63Wh7NESWs_QUlzKXYXAD8u_9FGa8mazpsx_dAJDuty8ed0J50WUQTgRQG6OQ_GNziW-Alsph_QKIpDTTKWLLDX4_fwdj9L5gBNz9wwH4Q8cv-XXFJPATjvrmsGA-EbntCeIVVVSSVOV-aqY4O2y7nEcxP7MyJf5Bwn_A_Q9dkf0nq0SByUhz0dF9W2DnX4JHELqPm06bAQGtmcVv8s5-lFQ0i7TH-wQ0_l2aUes522Gf0zGCwLfPcHViAHag-ZBsm8w75RJBdiNmSzwgoEjz-4LsgIjOmnNIUE2IysoxuXSxrn6JMY11PrBXGlvSSloovO8olg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fkvNULyXpfGCd1AL8mijC5ovzdRHyw14NUtP1su8hPy1U34i4YeK9KSrlBcRqtazDkNRRu89bCzile0nwHCfC8-7J8xmbkSlAgXAFMwdVVsEL39Cxu6RM3cVz9V9zmgs7OhCKMkFK2XTvw3wJ420w10acMcU4TzavnYCFSTQR3FuT4XrdZ-qWRHKVfXdDb2HREx26nOl7nSTeABoi28U8ZkD6kyjqgKfRAGUUm1ftX07P5e_F-9jWDU85U_tgAv-JLWQk6fXNi1AsyMJumttw2XuRU3VRPW8k6P8mpT9qniysiBETf9Zp5YBFJ6EWvDF4viA8M7ZsWfekR8I-Kq1fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسبب التصعيد السعودي...
🇾🇪
🇸🇦
يعاني المعتمرون إلى بيت الله الحرام من صعوبات في العودة إلى بلدانهم بسبب توقف الكلي لمطار الملك خالد.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/93175" target="_blank">📅 19:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇾🇪
مشاهد تأمين ما تبقى من مديريات سامع والصلو والمواسط ولحظات تسليم مجاميع من تحشيدات العدو السعودي للقوات المسلحة استجابة لقرار العفو العام - 10 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/93174" target="_blank">📅 19:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93172">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1545c2b0d.mp4?token=gp3_N3XC5rpe-87_DqVzbUxGDJHtmPStrRUVEge-ZIdWpTzpjbiZxUo9Hz4grB8T3J6F0pn5gvwDNhgkQgmRB-FG42gnjJ6VoSi2Xi53h4o4mqPK8Nu17PcaU_z0mu1BZYdqsM9U3IW_X1iZKtvWdkhZf4v8z0wcPqp9w0LvcmC9Wtw-GQK-9Rt_LFlWf5jmJuKy3f8X71tBKaVHY618JxWBzUo59e1xjOuIq1gLyNIhTZ64i0HaskcntvRyUq22wluwPddaRmM0gs-ZPNkhuiSVwKw1t75WwAr6cktuFKzHeMpaT3l_au-udeM4ZENXv_2xZqsJsayPPOUBlUmQkbXM1Ic05wAqlRaVG-aNB2K30WvQNRavNE2wd9lnDNXB-Y5kgUXcSYyX2CkHaCEvemySzalQEFgLKtugEy_37XaOihmkdAlW01-5oOdcJnHszyiPGPqr9ISmPV2oxRgm4sshxHj6qCtnAxujvdPvlu9bjpz-Y2eWxCkP_zPOhwcHfq2Mj4CWFH3aNo_LVj8fG0LWPnEPQMiDgW4OibMunzJ3qGc7mbtWlvzEM_V-SvuMB6JH2QULh1t-e6vHfCQLyBsfXJPI0T16s-Khs4HkvPkjb8vO_LpSrH9ZnDSfmUM-bPuHzPK_xb30u2-Zg0Z5FSlXN9rDQg4zR6AJ2nQI6vM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1545c2b0d.mp4?token=gp3_N3XC5rpe-87_DqVzbUxGDJHtmPStrRUVEge-ZIdWpTzpjbiZxUo9Hz4grB8T3J6F0pn5gvwDNhgkQgmRB-FG42gnjJ6VoSi2Xi53h4o4mqPK8Nu17PcaU_z0mu1BZYdqsM9U3IW_X1iZKtvWdkhZf4v8z0wcPqp9w0LvcmC9Wtw-GQK-9Rt_LFlWf5jmJuKy3f8X71tBKaVHY618JxWBzUo59e1xjOuIq1gLyNIhTZ64i0HaskcntvRyUq22wluwPddaRmM0gs-ZPNkhuiSVwKw1t75WwAr6cktuFKzHeMpaT3l_au-udeM4ZENXv_2xZqsJsayPPOUBlUmQkbXM1Ic05wAqlRaVG-aNB2K30WvQNRavNE2wd9lnDNXB-Y5kgUXcSYyX2CkHaCEvemySzalQEFgLKtugEy_37XaOihmkdAlW01-5oOdcJnHszyiPGPqr9ISmPV2oxRgm4sshxHj6qCtnAxujvdPvlu9bjpz-Y2eWxCkP_zPOhwcHfq2Mj4CWFH3aNo_LVj8fG0LWPnEPQMiDgW4OibMunzJ3qGc7mbtWlvzEM_V-SvuMB6JH2QULh1t-e6vHfCQLyBsfXJPI0T16s-Khs4HkvPkjb8vO_LpSrH9ZnDSfmUM-bPuHzPK_xb30u2-Zg0Z5FSlXN9rDQg4zR6AJ2nQI6vM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مبنى رقم 3 في مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93172" target="_blank">📅 19:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93171">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇾🇪
انتشار قوات الجيش اليمني في محيط مضيق باب المندب.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/93171" target="_blank">📅 19:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93170">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896cc7541e.mp4?token=tAcu2SA5KHsSC50XN7N9j0hJQum10ywoazDPz7v55NDJrbJA2LmEkh1c8GqmkMy1g8OSpSGvkaSXtRBKJxc-hikqjAthLiWgl1KTBwFzGsEYCOrQO82Hl579FMZKPlOZZUp_2mBLJxjpVKxcWI9joUmfN0DDtKfE_yBcuc6UxlihNUJdYac5QH_LTf9Atw6LCpwHxX6oDiapvFuMgoBylAPg8jasqVoncTTP2vACuGsLrXLLuC4k-rxK5q2BDIgWolRhihK7gXjdwV5cjFRjINfKEX_E-QuNqvxclkKxR0kFqCH1psikt_VzNueNUSjxHWeNDb3rmmFGWb7JdN2vzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896cc7541e.mp4?token=tAcu2SA5KHsSC50XN7N9j0hJQum10ywoazDPz7v55NDJrbJA2LmEkh1c8GqmkMy1g8OSpSGvkaSXtRBKJxc-hikqjAthLiWgl1KTBwFzGsEYCOrQO82Hl579FMZKPlOZZUp_2mBLJxjpVKxcWI9joUmfN0DDtKfE_yBcuc6UxlihNUJdYac5QH_LTf9Atw6LCpwHxX6oDiapvFuMgoBylAPg8jasqVoncTTP2vACuGsLrXLLuC4k-rxK5q2BDIgWolRhihK7gXjdwV5cjFRjINfKEX_E-QuNqvxclkKxR0kFqCH1psikt_VzNueNUSjxHWeNDb3rmmFGWb7JdN2vzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
انتشار قوات الجيش اليمني في محيط مضيق باب المندب.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/93170" target="_blank">📅 19:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93169">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الله اكبر
انفجارات الان مجددا في ضواحي العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/93169" target="_blank">📅 18:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93168">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEQIHYvbegc2NB23M0pSDk2oIibqV8UVMR-SlRiLWCf7OeAfPlw86yuEoU9wRxgLYRBqXmCoaOUeH_8w8zzosrZbmRgeesTmgwAU-18OLgL5ghdGl_htW2Qaw8Z5U5dyjFpYd5r3GBqo-RddQk8rfazP0ak1WSu7zIePqsBdMkYSf0yKWNa6gXFCIWd18a9FZd96UAfV4Qa20nUzHZFs3MVWOW1uL8HaSI5G0hUwUuK1EXB2EETqoFb9_9GbwgXikMZOPB8231bkFhW7MxdejNTkqjN-EfHhYqHiVmAeU8ByoBgi1vsFW0_oxW3Dvqa3yhz7KKjGAzJ4RTbzkTYiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ألمانيا وكندا وإسبانيا توصي رعاياها بعدم السفر عبر مطار الرياض.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/93168" target="_blank">📅 18:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93167">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مبنى رقم 3 في مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93167" target="_blank">📅 18:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93166">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01f09c652.mp4?token=qVPL3tW0g8V1hzr17VGUjzEilXDB6jWwycbXfk0GXTgBMzktSGypShZ9JfbhMoK4GTuBf4DNFp0ZqPliAbSGFrDwdSfWzWQuvHmnvvNuPqR0ctk9lmV0bAYCFInqI6bCXPx5tG7HNM2Xq_gkIgfOiJK9t8Faa14qvpSHarYTiUkdYYCkuNhBpxBmp833NonlyNk5tUxTNRSmaqCppPU8NfDwr1-t80MBFPGpSUwR5jsZUuKsI-C0K99fDaMDfKyauhUR8mm1Rwio6ywUsqKXiPkmW9Jn0LVW8F4n8lpUzaxoGkzBRwKnJacB0e_87c4TdCFnC5Wg3NDysY30An774Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01f09c652.mp4?token=qVPL3tW0g8V1hzr17VGUjzEilXDB6jWwycbXfk0GXTgBMzktSGypShZ9JfbhMoK4GTuBf4DNFp0ZqPliAbSGFrDwdSfWzWQuvHmnvvNuPqR0ctk9lmV0bAYCFInqI6bCXPx5tG7HNM2Xq_gkIgfOiJK9t8Faa14qvpSHarYTiUkdYYCkuNhBpxBmp833NonlyNk5tUxTNRSmaqCppPU8NfDwr1-t80MBFPGpSUwR5jsZUuKsI-C0K99fDaMDfKyauhUR8mm1Rwio6ywUsqKXiPkmW9Jn0LVW8F4n8lpUzaxoGkzBRwKnJacB0e_87c4TdCFnC5Wg3NDysY30An774Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاعلام الامريكي: تشير مقاطع الفيديو المتوفرة من مطار الملك خالد الدولي بالرياض إلى وقوع وفيات ولا يزال العدد الدقيق والوضع الحالي داخل المطار مجهولين، لكن لقطات تحققت منها الوكالة تُظهر وفيات مؤكدة</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/93166" target="_blank">📅 18:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93165">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الاعلام الامريكي: تشير مقاطع الفيديو المتوفرة من مطار الملك خالد الدولي بالرياض إلى وقوع وفيات ولا يزال العدد الدقيق والوضع الحالي داخل المطار مجهولين، لكن لقطات تحققت منها الوكالة تُظهر وفيات مؤكدة</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/93165" target="_blank">📅 18:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93164">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">النظام السعودي يقرر اغلاق مطار الرياض</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/93164" target="_blank">📅 18:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93163">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">النظام السعودي يقرر اغلاق مطار الرياض</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/93163" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93162">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">القوات المسلحة اليمنية:
ترقبوا الساعة السابعة مساءً مشاهد تأمين ما تبقى من مديريات سامع والصلو والمواسط ولحظات تسليم مجاميع من تحشيدات العدو السعودي للقوات المسلحة استجابة لقرار العفو العام</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/93162" target="_blank">📅 18:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93161">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43ab69053.mp4?token=Io9dJ4fi-BvmWmWqxGbUpdWneU7_0yEknmLk4ZTrd2HArMjmyY6HZzTkwKeLxcLlvm4lpjX6jb8Qk0FwdsL3s265iSKT8ahQFkolBfZEDwYd8tmbMK7OzUNwnjibBmh4uPEr5KStphQg8G6SITgZ-jr7heloJXjR1nTUw3t34VugMTk7-_vk4Ei2ovaoM9lxJCvz8xl1BSbhaEhmOKw1qLa7lRQhaMpApnMiSOjTQajKxVIUJvU0oQ2XbjAJtkhxBpZgNVlKWfzsLWepK0wfcBi8azs7He5yOxM2Iy_jZ_xNpHwUlM3TCvABuYP3b50rabad-MzROTqIZN9Twa1Wcg25OzPbmgtlfmu2VDXfnliqIxkvaE0hlJe9hk8KR-zEAM1fZ6iJLBqG7RPoln8evGJG51SvmJi3rBzhsF4OPerH1q3vTtw8N8l8vmC20NVQf_v7sBFBmiH-2-8PnogxlkHzcK5HFinGDtLh23ewXrt7Cpc81oW5HP1fXkFHJiOs_-K9FuzP3ypCUTZo3DjV4uEcC8hWe6G_pkGSmvxs7ycvqJt7f64nCDOPkq7-QIt5XLO5ETHzvNbWeBiogYWVqYbUyCHUbFDuv3mpG7rtfPJZHDsN-dN1Tt1QoL8yDLuZ-nlH3bLmRsPjUilX88egdZ0k3Gtg_pgPEsOeIG3pZ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43ab69053.mp4?token=Io9dJ4fi-BvmWmWqxGbUpdWneU7_0yEknmLk4ZTrd2HArMjmyY6HZzTkwKeLxcLlvm4lpjX6jb8Qk0FwdsL3s265iSKT8ahQFkolBfZEDwYd8tmbMK7OzUNwnjibBmh4uPEr5KStphQg8G6SITgZ-jr7heloJXjR1nTUw3t34VugMTk7-_vk4Ei2ovaoM9lxJCvz8xl1BSbhaEhmOKw1qLa7lRQhaMpApnMiSOjTQajKxVIUJvU0oQ2XbjAJtkhxBpZgNVlKWfzsLWepK0wfcBi8azs7He5yOxM2Iy_jZ_xNpHwUlM3TCvABuYP3b50rabad-MzROTqIZN9Twa1Wcg25OzPbmgtlfmu2VDXfnliqIxkvaE0hlJe9hk8KR-zEAM1fZ6iJLBqG7RPoln8evGJG51SvmJi3rBzhsF4OPerH1q3vTtw8N8l8vmC20NVQf_v7sBFBmiH-2-8PnogxlkHzcK5HFinGDtLh23ewXrt7Cpc81oW5HP1fXkFHJiOs_-K9FuzP3ypCUTZo3DjV4uEcC8hWe6G_pkGSmvxs7ycvqJt7f64nCDOPkq7-QIt5XLO5ETHzvNbWeBiogYWVqYbUyCHUbFDuv3mpG7rtfPJZHDsN-dN1Tt1QoL8yDLuZ-nlH3bLmRsPjUilX88egdZ0k3Gtg_pgPEsOeIG3pZ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سيارات الاسعاف تهرع الى مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93161" target="_blank">📅 18:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93160">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597af4f32f.mp4?token=JFDkQtXX0qD5jsJhKTzc3KDlFuo1Iy2rSpPT6rTXFizwHeoGDAboqkWB1CtlpmeODwSFsSeCHCC3-8T7CgD8KgGqYcukkaoYhssVgzAEXrNOJeEPuCsXoRREyZcmMeq5LVtO8UbDdGQNh5Vwo_GkjSrQWnBIjTnM_1YkUh44zfTLe9UEgxBbzcHsJjwdLtK76Mc_3cE7FiqavrKBlrZG0Fer8wp2ohouDqTZKt-fWmnPnauFJYkND9BEbAxEEel1cgmq9eI7kPBHz26Paqb9cMGdBtJVrcDCZjwaiLaSF-BlFgInkx3qpFkvrJKBwOSGjr77QSyntPKBPpCluhYvkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597af4f32f.mp4?token=JFDkQtXX0qD5jsJhKTzc3KDlFuo1Iy2rSpPT6rTXFizwHeoGDAboqkWB1CtlpmeODwSFsSeCHCC3-8T7CgD8KgGqYcukkaoYhssVgzAEXrNOJeEPuCsXoRREyZcmMeq5LVtO8UbDdGQNh5Vwo_GkjSrQWnBIjTnM_1YkUh44zfTLe9UEgxBbzcHsJjwdLtK76Mc_3cE7FiqavrKBlrZG0Fer8wp2ohouDqTZKt-fWmnPnauFJYkND9BEbAxEEel1cgmq9eI7kPBHz26Paqb9cMGdBtJVrcDCZjwaiLaSF-BlFgInkx3qpFkvrJKBwOSGjr77QSyntPKBPpCluhYvkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدماء تملئ مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93160" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93159">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a34b53cb9.mp4?token=AJGhj0h7Cmb85-MQ83bFza7hgBROdQLa0OzOXXjcXJhwXmZm1_VqTIsOzayl2iCPlxpIcLZg5xWuI4J63k5OH7rjeNcrGuD0jBYd6dXM1Cl63uTp5VT3VNaOX6Rl8QK6sejVhlO5murnPIOSvT00gJjGmU2rPh9CNiX0fwZhMbIR15xC1jucSONtBuaJ8v6z-W09FyFuHwv8TKIMMDtxRrwKcj2iVbpgkktjm67CJg3Iq1CL9aQmmBFPDCaIXesWjiIxz_PyKB3DiChE0drXUnj4R6db-Bhu4J4-6psLIqWtOBGqzybzHPqQprjBNIOO4xEFbdg_Lt8llgRao8HerQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a34b53cb9.mp4?token=AJGhj0h7Cmb85-MQ83bFza7hgBROdQLa0OzOXXjcXJhwXmZm1_VqTIsOzayl2iCPlxpIcLZg5xWuI4J63k5OH7rjeNcrGuD0jBYd6dXM1Cl63uTp5VT3VNaOX6Rl8QK6sejVhlO5murnPIOSvT00gJjGmU2rPh9CNiX0fwZhMbIR15xC1jucSONtBuaJ8v6z-W09FyFuHwv8TKIMMDtxRrwKcj2iVbpgkktjm67CJg3Iq1CL9aQmmBFPDCaIXesWjiIxz_PyKB3DiChE0drXUnj4R6db-Bhu4J4-6psLIqWtOBGqzybzHPqQprjBNIOO4xEFbdg_Lt8llgRao8HerQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدماء تملئ مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93159" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93156">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nmx4-JLlIKVacy_-1UMcP5n8PHYussuI64XFdCNkeutWE2i4JO2HxS_-J5P65ufwlINLTnZzxQb3rTjuSCSnwX_Grgj4wNq5-UdmPFCXgAK8K4L7BSHA4AJ_Bm7lruG_QDWaZzwqZdx_qOnfgZTKmaa2jvbPmfBGHyANhUHAMFyaN-RaBS8GFxAF3EgH5_69NKkxWZ5QfF9T6ufQX_z-ExHqi13rQNDcoLcId9L3c5jSKugx6LgIA5q_gc_5LoLyjd6Q7BJLDle90k4As4v-fU4Q2-wFymMnM2Ya1LQQf9IyzgYRsKuHSvmBn4b4h0k2NtDux8Nhp3mq3Z6afCazTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMkZ2dE5o-8DhK7A4GFCaV_xZA4I3nsboC7lIkYRcKahhiOemLEx-4guiMoucKGZLB3gNVB5yOBVqWjPHzA7gEROIKipL162XvAcTz8A-Ou4UvbD1M9ps77xqVfaOOGNgkK-irYzeMaV3K8lz-bANfucDNzqCficZV4Ektfg3xt69FN6ceD453a3P5Mck8OeVBkJOQLMRBpRxrWZ1p89PWn4zzeXUn0llO1clG-6erV4ilJOYaKosvGFrSHak_u9Ifq-FjwSGiu4aBmmtPhubv7i3VovKna_hNBgQqVdw51xx9Uj_kBIQuptwFfpwoh0emIn0f62wjS3UqjC8UmW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8HuNpr6wGUz_fZgxMkvhnf4Rqn8eq6XzSFB3gI1xUmHOf2pxODKzW1vpHgS8I4dgxzeQM23voI2m2i2PoP7erDY7C7-4xpQTXSD60a58FMu0L9Wf1iQZQkjSZ2JMRkKwvLeCysm9756zF7mcHhtn2wgtj5Y0_tGmL4gh7kcyZXjAd0rQ9orvFNt1as05LBD9EyHasbX5dbgwdFx8IiB-EDznK3_n1W44KnTPkBqbr6ibi9bphichfUiWTJMYRro49Kb5GQnsjAojoI_g_G5LlxUwHGFLDWPs4Eom0FDawCGvOeFTupFsZGXKm7G2h6CTVoHVYLBpvM3qw_Pd0TlIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اضطرابات في حركة الطيران فوق كل المحافظات الشرقية والرياض ومكة المكرمة في السعودية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93156" target="_blank">📅 18:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93155">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هبوط مروحية طوارئ تابعة لمستشفى الملك فهد مباشرة في مبنى الركاب رقم 3 بمطار الرياض</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/93155" target="_blank">📅 17:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93154">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ova0BAAwMpgMCklzOvYUqsRq_OVrwybphPCw5nV6mpK4C2Hu1x9kw_enMouCnJUv80ZozDIYzOH03btHkGi5TMjY5XtDZrlAjis8bktZCLkGsG3hPAVASC3bbpy8QTSGMrQWKmizHNxgpqSXGQ_Cyi5JO6uFWm-38pGzQYHxVRZRLVdPu4SZJuDAaFyC7AacLJnNnMqMZ2cWZYLIQ1_SOVSeq5LokKQHh_h_Ws4GZfNRkAZhSZkI2gxVN22wyhnUtgRDT9EYLv8DN8yno7KmcksE78mPz7VRpfv5mEovDYlf8B_a2C5xCxBPmjWt3yih4cR8KKNi0shB1dc19u549A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وسائل اعلام: وقع حادث سقوط ضحايا جماعية في مطار الملك خالد الدولي في الرياض</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93154" target="_blank">📅 17:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93153">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اخلاء مطار الرياض بالكامل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93153" target="_blank">📅 17:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93152">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnXFT9-2aOvM4GxF9vtLhH8p2dIz6aX8XgUeZyrsiVPg0crwx2BDjT4nO2V6sARDs7Ryoi-odwwEVDLam6Z7636EvO0BO3lVuHVCziQTTIkvqPF7Bian0_LxpjIi8tpHXL_TQgVP8GhHHfKXg_Lx_BXYJPDojKh0cOce8MXJng1hxZcGDeLryw8xyd0Pzr5JCgZt5lE0Gfas5ScSdxgnCQfuwfiCF7zzLz48NiwktYi2glhJK3zpYpFf318tp2FQrKYxf0gxpxfeFaayHgteZRaCblD2WMbUjhdgE7di-jry_guP4NJcab9awsSbQa8BA-qiam6lpkZY3upeAfmaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخلاء مطار الرياض بالكامل</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/93152" target="_blank">📅 17:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93150">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhbqgZDa6EH1upwWlBmuuYKO263MvX3GaJTn5ApPvoivlNBXGGISl1V-RjSbVIWup2VaU6cJjvRNWpcSnZri-Y4SegdiTj7xltBG_nH36YPbMGwiaNOU-9dueNi4yXR_mKV2n4nRtIltxTd8KbIqBo0ylr4pP85iGjE3ofttsej28Awi2HYaIdskFYH96sqFMPM56B2GawtGvLdv0sS6MNXusVzyHHYndwyMbEPAgbiHBLLIrdARiTkR8GF7iTEnCJz5WcKfJtAEkGc5R__kYjrYSU5id25W-9YO6QfmKg_yAxgceTqBeH6ajE-Zd6xBQH3Qj6xZzQWRoFZMLtrgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sd2C80t7nd-3GG5vWHEsLew9HXrUGZ-w3THa2aLmJEAe7n7epfSZhUqVn73BgIih-Nf0VUbfZMMK5kOoALnCgv9In1VemdYCqJ8qVZTZGAqpWO-Iu432B3ai5m6Shn00E5b0dg6j5F44L1zCPJeZY_NBAcahoa4duhawDKCi7dD0GL9F3X2hZxVTcRNhN4t2AVtACRUIH8dLn0yNOgM0B75B-Y2Yt1eKywR1PLt-0xOMCJBoBeNH-zsBETO8T2puTJ_tx0tIEJFk63CAtmcdCkzL3Um5bEfA-zPaWTkeiGtBjN9q6cW5MwCK8EoBRASz72ZPkwaKb4fdjuC5UG_blw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الاعلام الامريكي: نشاط مكثف لسيارات الإسعاف بالقرب من مطار الرياض. يقول الشاهد: "الدماء في كل مكان"</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93150" target="_blank">📅 17:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93149">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اصابة صاروخ يمني في مبنى رقم 3 في مطار الملك خالد الدولي في الرياض</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93149" target="_blank">📅 17:28 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
