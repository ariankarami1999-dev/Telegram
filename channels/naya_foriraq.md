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
<img src="https://cdn4.telesco.pe/file/KTx0vRtDfJYJQ8lWqQgGnbxTV8hiRSFMfJrmFo4cCw4vIGiUz8apGxcnKZgPlOVDkg1wzGr_ko8yBInuLOczDdiwgM3nmz5G9dqkutoapGaYGl5qSXBcWjCPZJM07UX8b826KKm4mB56xN2zpNkcv3oEo-qnOkc0xQLBDtOvCA4v7mDoqksNRzkI39_JoM1Ot0laT_iYONi1Z8cuW9eSmUU_00jQBcDN8p1sZ1KSccTNOFaNKz0RCle8IV5rvXTacxUzZuWv3alQknT_NjVgY-q5QeGo5aE3meSj3fQBdFDV1SZdh8unAtPHAZqrvr_3cv5hwixVqCSe6gy9AMPOaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 23:36:34</div>
<hr>

<div class="tg-post" id="msg-86934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجار سمع بوضوح من الجانب الإيراني في الشلامجة قرب الحدود مع عبادان</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/naya_foriraq/86934" target="_blank">📅 23:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔻
مصدر خاص لنايا... سبب الاستنفار الذي تشهده عصابات الجولاني يعود إلى انشقاقات داخلية مرتبطة بمحاولة لإعادة ترتيب القيادات وأفادت مصادرنا ان خلاف نشب بين العميد جميل الصالح و أبو عمشة قائد فرقة السلطان التابعة لما يُعرف بالجيش السوري أدت لاعتقال ابو عمشة المقرب…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/86933" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouBixjp_uqk3_xovtlgwnl4lRKPE7v9L9s_7ddz_jyNa4eNcg6uRWNo8PC4dxz1KJzgHeZC8d1mu2n9wjfvLQ0ucvmhpPDdrYNoJv1_UbZ5_yskZ5VzXqsQpUyLp06EW1yzqxkqrP4_hf35UvRp2Gq-nnAaQP6V7WINNNKlhF3qn4HxduMB4TnxKUu1sDaJxQFYDm2a5c9_-M1gtW4I0VODDtGGFoTlZ2hVpX7q0MiY6nRxynbay5HodmPOnyg4-eS-_JauROxt8RDJQISdR8IS0jhYw9jcPYsChV7wDzzix0NNLWIqw9EXM4SW8gvhftdqeHy_y1BJbgcrCV52vnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مصدر خاص لنايا... سبب الاستنفار الذي تشهده عصابات الجولاني يعود إلى انشقاقات داخلية مرتبطة بمحاولة لإعادة ترتيب القيادات وأفادت مصادرنا ان خلاف نشب بين العميد جميل الصالح و أبو عمشة قائد فرقة السلطان التابعة لما يُعرف بالجيش السوري أدت لاعتقال ابو عمشة المقرب…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/86932" target="_blank">📅 22:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الاعلام الغربي:
‏أوروبا تتحمل تكاليف إعادة فتح مضيق هرمز في خطة جديدة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/86931" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8713a50d.mp4?token=E4SbBoUKxUpARM3ZAzUMS5SYupNzb4zuMsNknBbcmf93d2zvEgvY4goa8Gh-CBjCgIfs7f-uB4YsnON-gcFvFymz4OFHhgzD0DqduML4Ug4AftrqE4Y9JXtkfXorSsjCbExhT7wDUNuCmySRDJbjXcqf84p5knR_PaNGKdaE6SEml4OSdLDR_U94GHyMQPP1Nlk1gRr8Md5APaF6tickSmyVNWUP_lkRNoFMUIhPGGMZ-APXSCR10tjpZMBmgnUcONs_QLwDcRxtvRHXxm-1B7E-W3xsJlaL8CgB1f30OfwG5t53eh1Mulco8mKTkl958WOh25HmIaiiGhjHunjg2VPLhlnV0t5-_Z0g0s4kq4ONTGcmdJ5DBuItOlez1lx7TVMoQgicsKy8GuDekot_j12-BmjwoCYQv3DHox0mLgotm5ronhKyKn-uEZDSpi1GkB7GDLdIxlAzgSo8l-ZP2V0hRDICzWKsUh3pi9M_OvouNw-ci_Jnsl5V5KVLUc_VmjeAYMdRozsQxcIe965fP_7dJRk_334D3Gxgsia27BfbI-Zu10KI6jmVuhsCaQPuDCPyRh_qRDJgXX19c8abmTBvUQYuXZsEAYdTrfrE8sjPziMfeMjb4Y1huM5TgCrkZ7Wq5D1DpYN4qXWl5safw5EFAqqRjHNX9OoITxu6SrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8713a50d.mp4?token=E4SbBoUKxUpARM3ZAzUMS5SYupNzb4zuMsNknBbcmf93d2zvEgvY4goa8Gh-CBjCgIfs7f-uB4YsnON-gcFvFymz4OFHhgzD0DqduML4Ug4AftrqE4Y9JXtkfXorSsjCbExhT7wDUNuCmySRDJbjXcqf84p5knR_PaNGKdaE6SEml4OSdLDR_U94GHyMQPP1Nlk1gRr8Md5APaF6tickSmyVNWUP_lkRNoFMUIhPGGMZ-APXSCR10tjpZMBmgnUcONs_QLwDcRxtvRHXxm-1B7E-W3xsJlaL8CgB1f30OfwG5t53eh1Mulco8mKTkl958WOh25HmIaiiGhjHunjg2VPLhlnV0t5-_Z0g0s4kq4ONTGcmdJ5DBuItOlez1lx7TVMoQgicsKy8GuDekot_j12-BmjwoCYQv3DHox0mLgotm5ronhKyKn-uEZDSpi1GkB7GDLdIxlAzgSo8l-ZP2V0hRDICzWKsUh3pi9M_OvouNw-ci_Jnsl5V5KVLUc_VmjeAYMdRozsQxcIe965fP_7dJRk_334D3Gxgsia27BfbI-Zu10KI6jmVuhsCaQPuDCPyRh_qRDJgXX19c8abmTBvUQYuXZsEAYdTrfrE8sjPziMfeMjb4Y1huM5TgCrkZ7Wq5D1DpYN4qXWl5safw5EFAqqRjHNX9OoITxu6SrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعرض سفينة مخالفة لقوانين عبور الحرس الثوري لصاروخ مما ادى الى استهدافها بشكل مباشر عند سواحل عمان.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/86930" target="_blank">📅 22:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تأمر برفع الجاهزية فوراً على كامل الحدود السورية العراقية لجميع الفرق والوحدات العسكرية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/86929" target="_blank">📅 22:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86928">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jojGHxRXqfmhUs82_QcgOqBxRUNs2uuJAwTPiYoNkz3OmBk70RxcEEqL3Hp4SbW1_ZIDm3wVpLPQYApf6DCNFnGB8dul3-CGHTwDNnDgafmTu7GwMnJFx7ChTfP5CmR5G8oc_sl1c6CYe1UeVW9H0N8_lr7SjFFO3_RGDM3JXROx8hG-YaUl9evMiy55bn3KsTuTxEIEOgZuFtHjWfvNTrbVlXHudxyeEfVsH8JVZVCSJGgHUAz-4JfAZsOvDnH5n2GsUqVcWFjSNTthw7sFD0fl7tLISFrSt3L7TpZXqEDo2wKpAP1X2diRm4Jzz7rrt2qGKweC5FP_0s8DCa_pSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
الصورة حينما السعودية تحدت النجباء في حلب
بدنا كبة لبنية خال بخناصر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/86928" target="_blank">📅 22:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86927">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4ppSDKGZ8cQMPX2jAAoY6JW2CRR4vSN538d8DGM7L4sr4wHpWtpKjGcWnr-YMY8FrjknjgUmnbYuhr9PUzT_w6ibU3NOQcrkS6MuE_Gqe83oyUlNmc2vRDojxdah5YW-raIV0CUkrwqRjtvYvNLnz_eS8XM_1PWlC9nvPcGccQp-11kwq82gaGT7lp_sPDbTUWcnPgXAz0nrSWxQSrDxmcbixVrHbDcjm-2KLAcqlFx-u8P9o7_07ks2azxr-ItcJyxgj641Mfztc5g1TsL8H7ZOdKNUIXGpbAHWFAsJM9No6wiEjrGu9uNnTaebBY6hriH6LCahOkTr-Hd1ZLy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
حكومة الجولاني تأمر برفع الجاهزية فوراً على كامل الحدود السورية العراقية لجميع الفرق والوحدات العسكرية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/86927" target="_blank">📅 21:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇶
🇸🇾
وزارة خارجية السورية ستفتتح أول قنصلية سورية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/86926" target="_blank">📅 21:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha-23KkFVscnmbfi7rUkWBKHmjy_DrqS29sVxkXhZOZS4STF8WI1BcHzyzPXJ--JsJu2r55jydOIXaZ5ta7YhioP3BGSuqThagjiSXNI7NZx8_5dmi6w2-Rj_Zhjo6_aDMMpANm44fOkj9xkwOTsYlFDeghwYZ2wW_E_C0gy_40l7BzOLcRWqUUMztMv9IWbqEXWmSgMgydX-QWyr0qREG_aj5B6Jxy5n7CFgLpDm-KfFQWYHgNBlx6Johm27qbApO8x6zj-dIiZe1tzbj2hc3bHV6aGMfyrd6fCbzHAzfcSjwjNEYgakHOzagkmvn6k8sPEgqtFBT7j9gZ5pATxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استخبارات الحرس الثوري تنفذ عملية أمنية في محافظة أربيل أسفرت عن اصابة خطرة  للقيادي موكري حسين يزدان بنا نجل زعيم حزب حرية كوردستان المعارض لإيران.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/86925" target="_blank">📅 21:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86924">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw8SljGgc5jCkpVOgZWXCQur442F4U6R3u5B6COi9CqnoZu5lezeH8C60l7NkllRRw1TIHTWFWATd2xT8qD0IKYas9eH1bHE_6OPROak5aTLKHhP5IPavQHpr6buhaEnR1iqQefH5Sd2E2HoOBzidHQQC0Gjc8VehDobIOpE_geActL9xSfV3ng6zcsQ6x3i85G0SU4If7eF7GnYuGmNtJWPFByp_fq27_dFSXU6Oyi24lfKGbJ5LN0eU8BjVjK5zrY9rfTD7FSNmO-lUwvGC_ADRwvxwQF10ZIIzKE72hien_-pLlA5eEQy4CqxKk-Uos84yen7THrFXoLZCLm-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
ارتفاع جنوني في أسعار البنزين في إقليم كوردستان العراق وسط شكاوى متزايدة من المواطنين بشأن رداءة جودة الوقود المتداول وما يسببه من أضرار للمركبات رغم ارتفاع أسعاره.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/86924" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86921">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVRetEM1j_gwTKgixDySZeD0l8YbmwXg5BAHu-475WjBqVQliAp5sU3LD1ETJIptzJ94KgSXvRQHNWtVgqL2Bv8AlS_LUBOzY7OgBdtqLCQgQZEvd85ASnxeYCmwZX-p6A0XXs0apDZwAqlG5Kr_yCzIDaxtM6Eavs2qvkK14bB_qG4y0fAJbHmUZaZtrcl44vNG8C2e3d62HFXtaIy6PS5I3Hk882JloH9c2d4xYY0cv4BUZ0UhDSYXMlThyLxrksb6hxKiahZ8Q2AjBWQNmT2fm6-t9eRl9Hr72-ogMV9Z4FdXL4Ms4Ds3FrkXMkg1fU8uFr2wvHK19j2HnqlD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSbVTheuBjZyjDbt5qPvjCAelFPLNeSWROunfH4Z9WMGIVu_DKkOCEE00psvzCF9x_jhP623SxXIajW-aqvQFss_sxPFovqQD4rfu0ZT1GiMZcmgwEloR6HkaaIfM-WbXUkk_r7J6LHM7HxsX-Mf8Qqm0HiZF6l0cQ9F-qf_8R-pjuJV2ZiH35SH-dEn-ojV8-ZQmc7HdWChsbXFZosUjfnLhUeCEtzExePlFEj_Ytaa5VegIVw0Dcoo5IxST3pGKQ_IcxNoeinhIsSKF_TlXE6Xbr8tGI59_3pFUgYTmJmyxtLFOxBHgWihDtIk4BY2ormdV_pJ93impPjx4tZNtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQrzpbrGpUd6H0eEtUrezqna1F9G_uwzRmvdHnOrhveo4dcvj_1CUE0nKPvg0n5gy9Bp-szYqo2lxMH0X77jfdiaM0WGTGpO3nTX5hPUGmZ9Dr1AWA2imc3TuJP5uSK0jcDR6k47cYCM2uzVTi1AtWR5P2acfbtnf2mRlpcmLqi0dgNXhAh2iJvaZLnsLjcEBg0JIrfDtDzkkJsMgS3kQZADsJpYRM7p6RMZSr-bFubnC1Zr6w7mqZJ_YBJnfqtNM0hKyW86RDbkjA3CSkKIS9RqA4PSREbR7eTWeZLHiDlnJmo7mbnyeGHgyri-2zVsuJyB_QdIA0_3w8zJJbv9pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
قائمة بالأهداف غير العسكرية التي ضربتها الجمهورية الاسلامية الإيرانية خلال الأشهر الخمسة الماضية:
السفارة الإسرائيلية في البحرين
الأحياء الدبلوماسية الأمريكية في الرياض
السفارة الأمريكية في الكويت
القنصلية الأمريكية في دبي
4 مراكز بيانات مختلفة</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/86921" target="_blank">📅 21:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHHaqrUbcHu-exZq8hYZTDKnrSOrhCF9t0dJG8KYvkpmM6lnpMD0NJrWRMpt2vzSLNQUKdSe2qgZPc2uJ1IKJPVffw1g4GJg0eXK5ubhDBAoI6Im8aOZTezztsouqkNkZE_0J4tbjDzZYiPcEHuFxDL_rxUkYa6ThADK-243lCQPyzdQUdL298Kh73CO0fDFHG9fjV2y14W2INqh89mnlFldgBOqRxXmVRBf1Im8Z4UCHeQrVH7mez3tKZ-fdWeTHsg8mYh1R_V_e1Kv35OSTrUPgbHGiCT5Jk-3iJpEFjxJ0bXOTHr3Z66JEpHNPikXx9qHGPd1WBBiJAXB9tp1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#رصد   حملات إعلامية ممنهجة من جهات مدفوعة الثمن بدأت حرب على مواقع التواصل الاجتماعي على الشخصيات العراقية المقاومة ؛ حتى اللحظة تم رصد ٥٠٠ صفحة على الفيس بوك تقوم بنشر منشورات كاذبة ومزورة ..</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/86920" target="_blank">📅 20:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kabu7B6G5FXUPBv7NpLb1XPxdfHD-SBSF1O57OKEIa9ztvoyKchoqmghk4L7S28q-ZdxxWNMG--WP4y_fblTgbm8_L5pefjo8fQvo7EL-w6zFSccH8HJBNln5MP9H5pOkMWLpoF9l51Fps5UxPFtmMqC99_4y9ilmpD0kFcF4dzlJkwjXwhs4QJCPeDkV5kUtZPCehWVb-AKff29zlQPqXFO7m2YB1AFsm9286lneP9Pv3C1GDT35MD6gKvTRg4vU0ZExq9OyrkNUjqhbhVPvIzvEL5wQRJs0N6WsMr8G7zMjlbEibxRLmdX8jsGnvGc0wBS60_Fp82fP8LlKpp-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#رصد
حملات إعلامية ممنهجة من جهات مدفوعة الثمن بدأت حرب على مواقع التواصل الاجتماعي على الشخصيات العراقية المقاومة ؛ حتى اللحظة تم رصد ٥٠٠ صفحة على الفيس بوك تقوم بنشر منشورات كاذبة ومزورة ..</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/86919" target="_blank">📅 20:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تأمر برفع الجاهزية فوراً على كامل الحدود السورية العراقية لجميع الفرق والوحدات العسكرية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/86918" target="_blank">📅 20:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">غرق سفينة هندية على بعد 13 ميل قبالة سواحل الحديدة بعد إستهدافها بزورق إنتحاري مسير.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/86917" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exD5qDvnfIGB-uNj2O_0-pLujoFcKWhRLl5ZKENMWgB-r4USKrBP918ekUfV4X2OHs3ndhfKJCHco5EYlXUeQYFA9MiSvd3PhoFoHy2IJHJ9LwZ9TynO-3alc_31mhFIkVvqabzyvtlzc-ssOyQtSOMIMPIM5qGBxZhLG1NsSCItJtRz5rE6tlLiOZuP_eLeYIxUjDRcYU7z2onxAhFeRqz4RyC8gF9rab9p9lglR4Q9c2bOMPE09r2V7ZhX3_x6NH0BEZI9p2Kobz5cyFc3NkmkvnvqOZ8etBxFKT1aufIhkZ99QrGFq2cGr7g_oTN8hBm8ORM-GYduONIpv5hq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أبلغنا العراق أننا سنضرب الميليشيات الموالية لإيران إذا هاجمت الأردن.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/86915" target="_blank">📅 20:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تأمر برفع الجاهزية فوراً على كامل الحدود السورية العراقية لجميع الفرق والوحدات العسكرية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86914" target="_blank">📅 18:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مصدر امني لنايا : نشر دفاعات جوية عراقية بين الشريط الحدودي العراقي الايراني امتداداً من ديالى إلى واسط .</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86913" target="_blank">📅 18:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-text">"
⭐️
If you have a
verified
Telegram
account with a blue checkmark, we kindly ask you, our esteemed subscriber, to support our channel by promoting the link and sharing updates on the channel."
في حالة تمتلك
حساب تلغرام موثق بالعلامة الزرقاء
نطلب منكم عزيزنا المشترك دعم رابط قناتنا بعمل تعزيز لغرض نشر حالات على القناة
⭐️
https://t.me/boost/naya_foriraq</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86912" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نايا - NAYA
pinned «
يقرأ القران سيدّ من بني هاشم فوق القبر الشريف بالفديو والصوت والصورة …  أنا نايا عندي كل الخفايا
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/86911" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">يقرأ القران سيدّ من بني هاشم فوق القبر الشريف بالفديو والصوت والصورة …
أنا نايا عندي كل الخفايا</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86910" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86909">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
محافظ كربلاء المقدسة:
22 مليون زائر أحيوا زيارة أربعينية الإمام الحسين (ع) من بينهم أكثر من 5 ملايين زائر أجنبي.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86909" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تقرير: تسعى السعودية إلى استخدام الدبلوماسية لوقف تصاعد هجمات الحوثيين</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86908" target="_blank">📅 17:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86907">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/86907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86907" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">غرق سفينة هندية على بعد 13 ميل قبالة سواحل الحديدة بعد إستهدافها بزورق إنتحاري مسير.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86906" target="_blank">📅 17:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86905">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86905" target="_blank">📅 17:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86904">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
عدد من المحافظات العراقية تعطل الدوام الرسمي يوم غد بسبب ارتفاع درجات الحرارة |
تعرف عليها</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86904" target="_blank">📅 17:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
‏
وزير الخارجية الأمريكي روبيو:
تم إحراز تقدم في المحادثات مع إيران لإعادة فتح معبر هرمز</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86903" target="_blank">📅 17:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تقرير:
تسعى السعودية إلى استخدام الدبلوماسية لوقف تصاعد هجمات الحوثيين</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86902" target="_blank">📅 17:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
شركة دانا للغاز وشركة كريسنت للنفط:
سنقوم بتوريد 100 مليون قدم مكعب من الغاز يوميًا من حقل كورمور الى السلطات العراقية لمدة عام..</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86901" target="_blank">📅 17:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اعلام خليجي يزعم: اعلان مرتقب عن اعادة فتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86900" target="_blank">📅 17:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fh22eXKJTCf3ongacDG_Ze8dLimmxAXLHZ6NDnQctZtT49sfcs5VMwWI1jPZ3XqkxAP1qbvau9uVKY6Rz97Ahhzm8wu16CZhL7KeBhh4ViMT4Q8bB_HKQ92F9FCTMbXE4l2UKtRzoS5FI0IDbZy1Dhq2WQMCz1MRpWXJdpbiF-7MDjiBcBDR2Nqlxix8ShhBftp6PuvOkMwkw6FCA5qT_5ziVHPMaUxEFSh550UyA-BiAJQkypLmHw8B3COZKtxIt1Nsz_Jv5UAUw7gJpDmb3hwYfmgfj9i_Iu6C_1vrz_UbJ0GbsvKVtmOPR41_lgBfZWLGITN1CH2qs1Nv8Fs_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇺🇸
فَكِد كَيدَكَ وَاسعَ سَعيَكَ وناصِب جَهدَكَ، فَوَاللَّهِ لا تَمحُوَنَّ ذِكرَنا، ولا تُميتُ وَحيَنا، ولا تُدرِكَ أمَدَنا، ولا تَرحَضُ‌ عَنكَ عارَها، وهَل رَأيُكَ إلّا فَنَدٌ، وأيّامُكَ إلّا عَدَدٌ ، وجَمعُكَ إلّا بَدَدٌ، يَومَ يُنادِي المُنادِ: ألا لَعنَةُ اللَّهِ عَلَى الظّالِمينَ.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86899" target="_blank">📅 17:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مصدر لنايا في المفاوضات بعمان   ايران تريد نسبة 7% من اصل كل سفينة تجارية تمر في هرمز فيما تتوسل امريكا لجعل النسبة 5 % ؛ المصدر لنايا اكد ان سفن روسيا الصين سوف تكون معفى من الضريبة .</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86898" target="_blank">📅 16:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اعلام خليجي يزعم:
اعلان مرتقب عن اعادة فتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86897" target="_blank">📅 16:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86896">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مصدر لنايا في المفاوضات بعمان
ايران تريد نسبة 7% من اصل كل سفينة تجارية تمر في هرمز فيما تتوسل امريكا لجعل النسبة 5 % ؛ المصدر لنايا اكد ان سفن روسيا الصين سوف تكون معفى من الضريبة .</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86896" target="_blank">📅 16:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0550b2f93f.mp4?token=p1vuOqAFBU7Srwo12SKtIcMmsXn_FIXwO2EtoGXKEjSzhskPtoeMpiZhzt0_pw5ZJsiSa_10nmY-atSsn9YgOP_9m8yx0X_Vj9RYiCrQMEKCM5qZ-U7999hNoU259vB6zABDMm3zMIEnkT5PpcR73GVzpvfJRhQlZ4N-vxWo1RwUl9hm4J_Klb_m7RkKEFjY8wvedMSZDIa53Y0vNR5x-XBLvvNy1fMc17SpU619p13U18FHh9QHYhzm7IH_LVnCTLwZ-odcK7uyAwCv8cT-C8WNmbwI3txNloTleOPOU6HeCtEVb1bWyQDC_V_8cCpnBc-YxpOCe4s4tRh3QsqAcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0550b2f93f.mp4?token=p1vuOqAFBU7Srwo12SKtIcMmsXn_FIXwO2EtoGXKEjSzhskPtoeMpiZhzt0_pw5ZJsiSa_10nmY-atSsn9YgOP_9m8yx0X_Vj9RYiCrQMEKCM5qZ-U7999hNoU259vB6zABDMm3zMIEnkT5PpcR73GVzpvfJRhQlZ4N-vxWo1RwUl9hm4J_Klb_m7RkKEFjY8wvedMSZDIa53Y0vNR5x-XBLvvNy1fMc17SpU619p13U18FHh9QHYhzm7IH_LVnCTLwZ-odcK7uyAwCv8cT-C8WNmbwI3txNloTleOPOU6HeCtEVb1bWyQDC_V_8cCpnBc-YxpOCe4s4tRh3QsqAcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ناقلات النفط العملاقة السعودية تغير مسارها حول أفريقيا. ‏ست ناقلات نفط عملاقة ترفع العلم السعودي، تبحر وهي فارغة، انحرفت عن مسار باب المندب وتتجه الآن جنوبًا عبر المحيط الهندي</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86895" target="_blank">📅 16:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزير الخزانة الأميركي سكوت بيسنت يزعم: قد نتوصل إلى اتفاق مع إيران بشأن مضيق هرمز اليوم أو غداً</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86894" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86893">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk5lrK7rjKxdzve6Oc3KKyQ4BaDyt3qn7E_Wz_fkk-D4UnCKSvKa8_fnAOe29p7oJAV3olabOlmo0i3g8BS3YeaSmri8ES5hfk6sGI1cah3g3oz4IiKSFw7Uf4fO3LzI4lnK-ir20gMDjRVLAN-vf3MyamuCb5G1nf_nx5e48epL6l9IDK7QrSEi2tAc_UtuyQj8ZRmrX41jpLnURcXbPV7pdVLJJjbQxeKMi2iiVtyBT_8OYBomy1EG0Guv0VI-8uUS2e9bF4fFmTjGYjxKm_tx30BiEFJZMuQgfoyKZmfpdF9RWqMGx9xL_zVpHk-v8eGmVstYHSzPFVqkScGAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صگار البعث الصدامي وشيخ المجاهدين ابو الحسن العامري يلتقي وزير الخارجية الايراني عباس عراقجي
العامري يوم الاثنين الماضي تجدوني اول بندقية بوجه من يقترب من سلاح المقاومة العراقية</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86893" target="_blank">📅 15:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86892">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇶🇦
قطر تقول ان هناك مشروع اتفاق محتمل يجري تداوله بين الأطراف وان التركيز حاليًا ينصب على إيجاد حلول قصيرة الأجل.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86892" target="_blank">📅 14:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86891">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e077c0ea7c.mp4?token=SUtdZjHPoZCx3cV5zaJinECFkAmQmEzRXECVqRU4wjRsMht1r_hUfp9ViXgTCoCIez4TPjhB25YboWiBV70E1DlEqZgQ6j9f4UFRuOcU8LIimIxd1uZQiHst_7b1B3f2os2pbfHTWCjLfmCPSu16O2Nag4JqXJVhZsmB0mJAlvZZJiB11Z5hHpnu1h0ot2lGf7pZneb_ZXTTSA8ZIq5i9TSxKzyO0DSnu8jBMyN78rAxrpe79mW2x1KDk2IYaeHwvMCXXs9NGUH8DRVNXAAXgx4V9CvH3m6TtF7AmP8p1fvXBD1ddZGEos3HqPjI4cpC2RS0nhdoQphJ1xYiHVi5cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e077c0ea7c.mp4?token=SUtdZjHPoZCx3cV5zaJinECFkAmQmEzRXECVqRU4wjRsMht1r_hUfp9ViXgTCoCIez4TPjhB25YboWiBV70E1DlEqZgQ6j9f4UFRuOcU8LIimIxd1uZQiHst_7b1B3f2os2pbfHTWCjLfmCPSu16O2Nag4JqXJVhZsmB0mJAlvZZJiB11Z5hHpnu1h0ot2lGf7pZneb_ZXTTSA8ZIq5i9TSxKzyO0DSnu8jBMyN78rAxrpe79mW2x1KDk2IYaeHwvMCXXs9NGUH8DRVNXAAXgx4V9CvH3m6TtF7AmP8p1fvXBD1ddZGEos3HqPjI4cpC2RS0nhdoQphJ1xYiHVi5cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجمهورية الاسلامية الايرانية تواصل نقل قوات ومعدات عسكرية على الحدود الايرانية العراقية الكويتية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86891" target="_blank">📅 14:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86890">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇸🇾
سوريا الجولاني توافق على خفض واردات النفط الروسية خلال مفاوضات رفع العقوبات الأمريكية عنها.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86890" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86889">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الدخان يتصاعد من معمل الالمنیوم في مدينة شمس آباد الصناعية والاسباب غير معروفة</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86889" target="_blank">📅 13:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86888">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thn_c6yCN8xHdrw_OPi_ZQ5Fmj3BX91xlFbR8NN2aCE6VWjISXzkn5xCCmBUSahtTvho5A3jCZlm9mU7qPkgojS2ast9mZsm1ncZYswjLiQ5aJAXu3VOQS9PxsQKobW3iKWbd_WjbkuzuZ2eko1IG9elnjF5z014LqOkwSAymLiV754qIGv9AmLy4Ydfgpgn9G-hygZUVd8fJY60vkXUx_X7IgK3W7uDiplRvQwdDevJPlkaPRdFRBPhEFuJa99qVzs127Y8Qe3p-MdbCHl4ty6W3BNP78HRenWUweAGVoeTijuOQs__n77-5t7DEkdfupgv-UZnyBEEO0wJ_pac0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86888" target="_blank">📅 13:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86887">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86887" target="_blank">📅 13:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86886">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي: أكثر من 70 فوجاً انتشرت على حدود المحافظات خلال الزيارة الأربعينية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86886" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي:
أكثر من 70 فوجاً انتشرت على حدود المحافظات خلال الزيارة الأربعينية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86885" target="_blank">📅 13:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6l-2gtBspR_5uv0quNBiSZc3yU-cSOIWZNI7iaeGxqO6DcqXal90UdvNySZoJpKgd1kMnBAlaXE_cIslqlALd78CfM2EJpNfuE-iD-bRrqBnAA_PMjT2Ekh6EZzkrmClaiRDGcmv6GxpRuDDlD4CRP5yBghduNK01Qw4MxD73yeDN-s0O6lTF-k_hI3SGYJnhsoIl9Psu80xMyXHa6O1lOsXoYxkSZYb5dwBKr3Q0iQ2i67v1M5fppTChtQ4VmapvcSpBoY36lAjuVMqD1TiH7t_rclHt30wnXUsIyXdUEReWmuVdi_O-dIdMCJQhML5YHTcTHVS21_mKQ92Zjoww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد لاعمدة الدخان من جنوب طهران لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86884" target="_blank">📅 13:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_tlfjCTl5a9Ra2mmOXDnmpv60UQitWNKHYREDPZWGbhh2QOEz8rPxADc_epdMjGl6nQk_mlQcnTYEpghGe0hISQQ8EsiGH4Vt1SGEYKrIXYyzQfIIIRGJmvdz8C2aHcwoRdLlQ3GWBvaJcmKC5PFpRCHlPzJX6Vg9dC2H2SbDFszNOBTFEoZUn_z7YRitp6JlFc5rcOGQhJak5qXnpTia22if2WfOroMFP-veGgi0oSK43k8nNzXzYiWyC1CC-2jXmTIfM4v77JcS3sZ4FkCn3i_rh95YNpX1_EUbsjgOO3mA94SEfJDqNdMn53cATrU-2fnn4LFSTrbJB-WRdtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد لاعمدة الدخان من جنوب طهران لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/86883" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86882">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مصدر ايراني رفيع المستوى: بالنسبة لمسار الملاحة الخارجة عبر مضيق هرمز، ستسمح سلطنة عُمان للسفن بالمغادرة بعد إبلاغ إيران بذلك</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/86882" target="_blank">📅 13:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86881">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مصدر ايراني رفيع المستوى: ستتبع مساحة الملاحة البحرية الخارجة من هرمز مسارًا يربط بين إيران وعُمان.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/86881" target="_blank">📅 13:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📰
مصدر ايراني رفيع المستوى لرويترز: خطة مؤقتة بشأن مضيق هرمز قيد المناقشة مع سلطنة عمان تمنح طهران السيطرة الكاملة على حركة السفن القادمة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/86880" target="_blank">📅 13:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📰
مصدر ايراني رفيع المستوى لرويترز:
خطة مؤقتة بشأن مضيق هرمز قيد المناقشة مع سلطنة عمان تمنح طهران السيطرة الكاملة على حركة السفن القادمة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/86879" target="_blank">📅 13:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86878">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e85d3110.mp4?token=tkMkWRh5bEKF96vzC5XRSK5f_CEvsEk0aAbaIZeyXcvdbUUB51tdoTaX4BGdXwYs4Dcm-r3-5a3iwjuA1MSRHL9KulqXWQqEGSViYpF_R1o3sWLKJ8yWROAb6mZMHakmG568HTqh9prlxcNveGGYT58NF-RIr09G9JIEeWaHswWGBJkwZeelqwvziVUWOTYgsPc5T2Kaz0EsU-hnahfEXokcQ7RRdYW0l5nv9EIe5bOdsnY26F7Qs6v0xRXUEl1ufswMV20et5BOCCT1jdvGFMgR58ycaqo5Vs33QJPWgWPwp9YLuE14SnfvFGVsXn1XjqiSvCB5TxwKriNO7Pp7SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e85d3110.mp4?token=tkMkWRh5bEKF96vzC5XRSK5f_CEvsEk0aAbaIZeyXcvdbUUB51tdoTaX4BGdXwYs4Dcm-r3-5a3iwjuA1MSRHL9KulqXWQqEGSViYpF_R1o3sWLKJ8yWROAb6mZMHakmG568HTqh9prlxcNveGGYT58NF-RIr09G9JIEeWaHswWGBJkwZeelqwvziVUWOTYgsPc5T2Kaz0EsU-hnahfEXokcQ7RRdYW0l5nv9EIe5bOdsnY26F7Qs6v0xRXUEl1ufswMV20et5BOCCT1jdvGFMgR58ycaqo5Vs33QJPWgWPwp9YLuE14SnfvFGVsXn1XjqiSvCB5TxwKriNO7Pp7SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطن سعودي يوثق نفسه وهو يحرض على الطائفية ويسيء إلى زائري الإمام الحسين (ع) من قلب العاصمة العراقية بغداد  إلى وزارة الداخلية ومديرية الإقامة والجوازات: كيف منح هذا الشخص تأشيرة دخول إلى العراق دون تدقيق في نشاطه ومحتواه رغم ما ينشره من خطاب تحريضي يثير…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86878" target="_blank">📅 13:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86877">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية: عبور ناقلات محملة بالخام العراقي عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/86877" target="_blank">📅 12:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86876">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">السفينة خالفت توجيهات حرس الثورة الاسلامية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86876" target="_blank">📅 12:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86875">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏استهداف سفينة بضائع بمقذوف حربي</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86875" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86874">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حدث امني قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/86874" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86873">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حدث امني قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/86873" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XW38rQN1H5ufrCQqdokh0uV9mITZ5r-KF61zqYfh9836BiwhSfnbYccDh6hh4Is2gGP_gig5oCRtcIULdXNNTJRiYdBQGmjMoaBtKgoptu6FkEK6Lc1TqIhZWOy86s1JtLkaWUPa7dQdGO01qs0RV2AeMOQVSISHd5kiZkFZoxkhg6ysH9T1B7koeryrXeGbHlyP7dKddTrHc4DzFPmGMnfnV_pJgxWy5rPMDwo0QiuBnWW9z97J9G2aaArZ2IRVNaMB16ds2PDtnOBZF-Dtr05LBcBeRr7mwWKAmp1u-MTgLi5TPwtxSj65THHCa8UnP3WyVS9hDtkw-6A3M2hnyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3NXc_GR6pqiiURN-M-ZbkQCHtl-rxi6wYM23XVWm0pZZxnnkdetpYuqe89PeGvO-GdnUVG5SevHYKgiQBU6SFj6dxd5TasG13EpVKlea_AxRno2vlmmCXRDxL25WPNkczAXu8gJSC8ro2i3_M0rzEbbTh0r_ir8Dnxunlw2ooyMzBMGbguAVHPbMHTc-w1y0R2NufMZU_BJlSaddZRyypFcLp9L2Ije9jHsQhChVQx8AaCGOhVDrzuYVikJWhG1Xb90Ol2d7o0CRWI7uP_8apJZJuYgMItgqyh50ACiwRaMFMN-thL4qq9r5ifvlSmVub8ZrGHGJjt44O7DKHP7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EO8-HRTmGfphlnMqGmGjFmZRUY_nNgw-uIasiuD28cEwCj2za1_yWnC2OWskwjqCxQz4QAvtIBn81o5rBaIVGfod7g3wBKiVcvcZ7uH-3D1PXxmwgUZuc6G6z7cZzOtqGAZ3Tw5PEzhJLscAFwWU_USFpsd56WagE22jHDRjKuhhWNTmrAt-2n7J4HCliT78xojGL076vGGIsFl75VZCpr32LeCdyvVOsdmN6ZvLSY5YWO-ihkM5hoGEhy9WhirIx8jbRf-5T1_iFsdPogAlFLUgdHsSXnQrv-7I5nhNUCn6_pme4BS6HFpfLhLMMQuthuHJKa2dRCaOgI1N7XDexA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇱🇧
الجيش اللبناني يدعي إحباط محاولة تهريب صواريخ غراد بقطر 122 ملم من الأراضي السورية إلى الأراضي اللبنانية كانت بطريقها إلى حزب الله.
تنويه للجيش اللبناني: الجنوب اللبناني بحاجة كمان لإحباط التوغل الإسرائيلي
🤷‍♀️</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/86870" target="_blank">📅 12:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afb1b6f848.mp4?token=j9xkO4M91OQgG7rb1MTP3duzgd6UgiMW71DrLCrptsza50-NvEUvaMLDz7A5qqesXGSbjae0xmiczOnLkSb-vLn7lncT6QVoou6A0mV__Ar6Ojpe8rT7NrvSftPYi9IkeCy9fWqjOyUx-jEd9KLVKwYnDU-ZPbLTQdXWU_uNC9Dh3BiUJYa4G1G4SSgJm85_gIKU2JSMHTNwyNrZNZKJlCV_ZrBuN0HLDB9zMxLwN8ZQLiyWi_z9mMNLpyYTAMGrABTgp4MI24l28Yg6-Flv3VWjxWIGUcbVwzP7F0hxNqtXdwEEKNK9ZhLTjgN5jgX2z3g0Jj6FqxiJ7ztaiYdbrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afb1b6f848.mp4?token=j9xkO4M91OQgG7rb1MTP3duzgd6UgiMW71DrLCrptsza50-NvEUvaMLDz7A5qqesXGSbjae0xmiczOnLkSb-vLn7lncT6QVoou6A0mV__Ar6Ojpe8rT7NrvSftPYi9IkeCy9fWqjOyUx-jEd9KLVKwYnDU-ZPbLTQdXWU_uNC9Dh3BiUJYa4G1G4SSgJm85_gIKU2JSMHTNwyNrZNZKJlCV_ZrBuN0HLDB9zMxLwN8ZQLiyWi_z9mMNLpyYTAMGrABTgp4MI24l28Yg6-Flv3VWjxWIGUcbVwzP7F0hxNqtXdwEEKNK9ZhLTjgN5jgX2z3g0Jj6FqxiJ7ztaiYdbrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
اندلاع حريق مفاجئ مجهول على متن سفينة أثناء إبحارها قبالة سواحل منطقة "الفاتح" في مدينة إسطنبول التركية وسط حالة استنفار كبيرة للسلطات البحرية وفرق الإنقاذ.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/86869" target="_blank">📅 12:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8d4da1cb4.mp4?token=uI3PqNkug24nbLbIhpK9Jn0O1BiHUmfQLp2Fjlcz_caG34CZd5ABzRdA6GYh25jfrqw4D3j8DPeVDsvk3HGq3PL_tOjcRpa0-YNN9NYUomeuTTPB80DKVbw8WxdrLiGTysnIHOxmj8UwbYRpuyw5DQCZ6PWAOu7Ho-mFV-XBll0UfSHkMA1yV2B81iHdB1lfhh_H2XHhTh8ovwhYq9lsNPUbQMaG380vSMc6cf2H7h_aNWbrZ0806DiQks2bVZqkoOeIumrhB-lJIdLdyszephXOJl0Rf3muI7eCzvyj2ilYWAWhR4HmYXHi7oG3lZcVMebfsele1BxrnSVCQq5RujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8d4da1cb4.mp4?token=uI3PqNkug24nbLbIhpK9Jn0O1BiHUmfQLp2Fjlcz_caG34CZd5ABzRdA6GYh25jfrqw4D3j8DPeVDsvk3HGq3PL_tOjcRpa0-YNN9NYUomeuTTPB80DKVbw8WxdrLiGTysnIHOxmj8UwbYRpuyw5DQCZ6PWAOu7Ho-mFV-XBll0UfSHkMA1yV2B81iHdB1lfhh_H2XHhTh8ovwhYq9lsNPUbQMaG380vSMc6cf2H7h_aNWbrZ0806DiQks2bVZqkoOeIumrhB-lJIdLdyszephXOJl0Rf3muI7eCzvyj2ilYWAWhR4HmYXHi7oG3lZcVMebfsele1BxrnSVCQq5RujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطن سعودي يوثق نفسه وهو يحرض على الطائفية ويسيء إلى زائري الإمام الحسين (ع) من قلب العاصمة العراقية بغداد
إلى وزارة الداخلية ومديرية الإقامة والجوازات: كيف منح هذا الشخص تأشيرة دخول إلى العراق دون تدقيق في نشاطه ومحتواه رغم ما ينشره من خطاب تحريضي يثير الفتنة ويسيء إلى شريحة واسعة من العراقيين؟!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86867" target="_blank">📅 12:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86864">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ec2bebd6.mp4?token=l8t5UIRV9Im9nvNOV2PMhnESubnAq6PB34HXLBt0VPb0mnJb8HDdFSYW2rfo7TKQr876pMee7QFGt9LN4NDwj3cGcco6wWk4vmQW7XUKQZL01sMtPav1X5uJPWtzdBMniB1YEGvYJHefLQFwfKcOix6XUrw8vMhq4k6a6Za0Qi-6MpEHihJe6g1K2L_Ot8rI-7wcmOZEFoqxgjRwfZFwb-khG0SVUD2Aau9wmIQVYulVFr6YiTca3cNgZxwym8kGWjF9JYeIC-Tz-Nds5tIqAfAt0sEE8iBrbJUsUxJ370szPV9zqsfO3kmOrKWJz-_EnXwcjnZZc44s5KoUhLG_fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ec2bebd6.mp4?token=l8t5UIRV9Im9nvNOV2PMhnESubnAq6PB34HXLBt0VPb0mnJb8HDdFSYW2rfo7TKQr876pMee7QFGt9LN4NDwj3cGcco6wWk4vmQW7XUKQZL01sMtPav1X5uJPWtzdBMniB1YEGvYJHefLQFwfKcOix6XUrw8vMhq4k6a6Za0Qi-6MpEHihJe6g1K2L_Ot8rI-7wcmOZEFoqxgjRwfZFwb-khG0SVUD2Aau9wmIQVYulVFr6YiTca3cNgZxwym8kGWjF9JYeIC-Tz-Nds5tIqAfAt0sEE8iBrbJUsUxJ370szPV9zqsfO3kmOrKWJz-_EnXwcjnZZc44s5KoUhLG_fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇺🇸
تأهب عسكري غير مسبوق في مطار رامون العسكري بالكيان الصهيوني.. حيث أظهرت مشاهد انتشار أسطول طائرات وقود أمريكية في قاعدة رامون لجوية وسط تصاعد التوترات الإقليمية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86864" target="_blank">📅 11:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86863">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
الشيخ نعيم قاسم:
الجمهورية الإسلامية الإيرانية انتصرت ولم يعد هناك مجال للحديث عن من انتصر في المواجهة
إيران عملت على أن يكون لبنان في البند الأول من المذكرة واشترطت إيقاف العدوان والانسحاب الإسرائيلي
المفاوضات المباشرة لم تجلب للبنان إلا العار والذل والخيبة والتنازلات المتتالية
﻿
تحية إلى العراق واليمن على نصرة قضايانا في مواجهة العدو الواحد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86863" target="_blank">📅 10:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجارات قوية في الكويت تسمع دويها في محافظة البصرة.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/86862" target="_blank">📅 08:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86861">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇬🇧
صحيفة تايمز: تسرب أسماء ومعلومات الاتصال بأكثر من 114 ألف موظف في الأجهزة الأمنية البريطانية إلى شبكة الظلام "دارك نت" نتيجة هجوم إلكتروني</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/86861" target="_blank">📅 06:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86860">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCcfjwpj-hXP3DUYXRI7q3wckgn7k7cF_Qe15JMmPmED6a9T9pmDAOtW9fYJO5uYS3Bqj-m-cwwyOA4kBTV1ex2ryiBEKTIXEDr5A1_X1GEnUCnKTmYCVw-8CXy3Z9I0HUWPo-5IPpcm-Svtug9t0QSLXQKKNQEVaN36TAHOO7JZ_hH3eYM-QJEIbI9gemaU-cjJd63RHg4lUqSIxM7KMHjLpmJVWc3WqaMhiaUWURu3mTRKiwrw_cV1g75bM-At4XqaV9T89KlKyyoG7dJDJXMiV7CcX8uNRHTH8MzZnH9OLNeZm8wHuauYx8KjTW7fYLbRItIgoTWQBQyMQfaJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرض سفينة مخالفة لقوانين عبور الحرس الثوري لصاروخ مما ادى الى استهدافها بشكل مباشر عند سواحل عمان.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/naya_foriraq/86860" target="_blank">📅 03:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwrlW2Z9-Y59U8XK4142VFGH3D2zuTUeCJo0ZWULjYqQQBl0dYoxHAFEQJ-MFPZwlNNwGFlsAGQNzVTsYEPKPFE9GKlzQgMXBd_Og4tHU-yip6jbqKYWgEjQBNX4LxcQo1X1mXnbM68DGgJ1WadgZ6WpuL_LN-_YIp_lXGHEJYCN8_rhh6jTvO0uCQ2XgZXr-LQSFGBDTtMsTs-Hvrrv_DaDCahzgGN-wc1rIgvcsm4BhsOqUt5glt8tYJ3hVizBBeKsXC3xTneOfs4FWnl8UKhqsNciJFhdzH1Ilm8usjKJ8xg-np3JYxpWQjEfwiMRkQf5c9Mrceei3p_646v-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز شمال الكويت مجددا ؛ اصابة مباشرة لقاعدة أمريكية</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/naya_foriraq/86859" target="_blank">📅 02:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86858">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات قوية في الكويت تسمع دويها في محافظة البصرة.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/86858" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات قوية في الكويت تسمع دويها في محافظة البصرة.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/86857" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86856">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الله اكبر... ارتفاع النيران من وسط الكويت لاسباب مجهولة.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/86856" target="_blank">📅 02:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86855">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=iswIkxGtX5OkEbSW1FHdbr0cSRfBxKZ2PRpu51knRK0xEeXEIa0ZOT4p7D7iiALEdw3jFG_PD_yxHlbpE9r9l9XHAiopJj9ObKD9zsC5YMUGBFI_TnSYx9BPj2mUZdKc3KCRtnBMp-UKSoajgSupCOWobPMuukMVG4SkmbvK6ybIDTOCJWkbx7ISj9XcvCvd78Ms6sjMt8BTPcx8YCcbFFWgIKOS93Ex28tu2f6azO2A-YiMi_ZSK9Etrzd7neeZIKRvPG6m4M8ypz2Dl9KKhO4rsGaqJESm0o6LAD9SfQKwNPClyJZKVJtNRLXeLbFN06I59f4ogcswhbZC1rhzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=iswIkxGtX5OkEbSW1FHdbr0cSRfBxKZ2PRpu51knRK0xEeXEIa0ZOT4p7D7iiALEdw3jFG_PD_yxHlbpE9r9l9XHAiopJj9ObKD9zsC5YMUGBFI_TnSYx9BPj2mUZdKc3KCRtnBMp-UKSoajgSupCOWobPMuukMVG4SkmbvK6ybIDTOCJWkbx7ISj9XcvCvd78Ms6sjMt8BTPcx8YCcbFFWgIKOS93Ex28tu2f6azO2A-YiMi_ZSK9Etrzd7neeZIKRvPG6m4M8ypz2Dl9KKhO4rsGaqJESm0o6LAD9SfQKwNPClyJZKVJtNRLXeLbFN06I59f4ogcswhbZC1rhzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات قوية في الكويت تسمع دويها في محافظة البصرة.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/naya_foriraq/86855" target="_blank">📅 02:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86854">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارات قوية في الكويت تسمع دويها في محافظة البصرة.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/86854" target="_blank">📅 02:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86853">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e0824f22.mp4?token=hTJFfwHGk4biEQ5wRbWOKyX_i2HfmwjPsrn0yIhlrdIfO-7UVfLUe5F0JMr2Tu5xuByE-NLrABAHd6U-30GGz8rnTFQevUFOFDBgnC8Stw7pHa5y-70MSnOXW0jalyfXe15OVJgjWlfxfjpSvddzmYDFLQds03aCxxaxUbw7lkfbFVAx3rb_paJ0ujFe2c9EoFZesD4KfhCBC5uzWYOwpUxYnrpkJTnFM5qLvdU-dxUxV8a4SJchnrrULPlnIXq1XrAX5k3HHVc0TPXf6DIvpQXFSG_bUC73Wd0HwA8qp5RlFNLoawfmH2PVzyXKU6yYD9oh7n5WqC45eGdfPZ9GHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e0824f22.mp4?token=hTJFfwHGk4biEQ5wRbWOKyX_i2HfmwjPsrn0yIhlrdIfO-7UVfLUe5F0JMr2Tu5xuByE-NLrABAHd6U-30GGz8rnTFQevUFOFDBgnC8Stw7pHa5y-70MSnOXW0jalyfXe15OVJgjWlfxfjpSvddzmYDFLQds03aCxxaxUbw7lkfbFVAx3rb_paJ0ujFe2c9EoFZesD4KfhCBC5uzWYOwpUxYnrpkJTnFM5qLvdU-dxUxV8a4SJchnrrULPlnIXq1XrAX5k3HHVc0TPXf6DIvpQXFSG_bUC73Wd0HwA8qp5RlFNLoawfmH2PVzyXKU6yYD9oh7n5WqC45eGdfPZ9GHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحاج أبو آلاء الولائي الأمين العام لكتائب سيد الشهداء، بين العتبتين المقدستين في محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/86853" target="_blank">📅 01:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86852">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e07b48363.mp4?token=Tv7t8ZX0m6lpn6DpXBI1NFaM-7-oq5kLijFdkwbRzutwcURJciaQUOpPiPi3F3XsxpnlX-_XS3jRK2PDXcgBy2zevS9iZQexMh8TXGgrkIkaFgl7V-GXiqo1deqm5eMDWzDFQuLjDf6XcbCkR89AyrgxrsQe1DGohoKHD2PmEgwsuhiycqowu_UH0L1xlzy_SeFEK4ryoJrOftqEp6fDt6qr8GjGNy3KNjMKy8Sj0PGOc3nMpbJGwldV7dLk9x_bpL48aXCfIegoRvhlO--pQgVnJIfCrCAWNB6YfAUkHSrzkJMS8fDIZf8zxOwVDuXS1hkCuAsnCRTbkC1CeCRt453_OqLYN-uBWk08VD2W_Qv4h3LlxswfQzJJkMVvXHaUa4vF9dlON4klFCy6kEwnP4ubcf6u7qR4A3Lze16lqTIzs2A3N5AFyARTxID-bgQd0ypv9N19nh19gKC7gcuC8LMhI4EpiDf_A6bMwollY3QP8IIaHiOVejyNHYXj_natSGcjgMGhx8VeJgYomoRLpBFraCTgw7nQtPfXF_nOVz7rOc8I1lOsat_SZmIfUBPN6RvauhN8jZ7JM3ivEByVQFWNj2rv0zeE7pen82zThBjpbWXwoDYzOKNQ6uYPamci0MJqOAusfVcYnKjkwA0fUEvXBSQASUhGZzUME-GT620" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e07b48363.mp4?token=Tv7t8ZX0m6lpn6DpXBI1NFaM-7-oq5kLijFdkwbRzutwcURJciaQUOpPiPi3F3XsxpnlX-_XS3jRK2PDXcgBy2zevS9iZQexMh8TXGgrkIkaFgl7V-GXiqo1deqm5eMDWzDFQuLjDf6XcbCkR89AyrgxrsQe1DGohoKHD2PmEgwsuhiycqowu_UH0L1xlzy_SeFEK4ryoJrOftqEp6fDt6qr8GjGNy3KNjMKy8Sj0PGOc3nMpbJGwldV7dLk9x_bpL48aXCfIegoRvhlO--pQgVnJIfCrCAWNB6YfAUkHSrzkJMS8fDIZf8zxOwVDuXS1hkCuAsnCRTbkC1CeCRt453_OqLYN-uBWk08VD2W_Qv4h3LlxswfQzJJkMVvXHaUa4vF9dlON4klFCy6kEwnP4ubcf6u7qR4A3Lze16lqTIzs2A3N5AFyARTxID-bgQd0ypv9N19nh19gKC7gcuC8LMhI4EpiDf_A6bMwollY3QP8IIaHiOVejyNHYXj_natSGcjgMGhx8VeJgYomoRLpBFraCTgw7nQtPfXF_nOVz7rOc8I1lOsat_SZmIfUBPN6RvauhN8jZ7JM3ivEByVQFWNj2rv0zeE7pen82zThBjpbWXwoDYzOKNQ6uYPamci0MJqOAusfVcYnKjkwA0fUEvXBSQASUhGZzUME-GT620" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
متابعات نايا...
آراء زوار الأربعين بشأن قضية تسليم سلاح المقاومة العراقية.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/86852" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86851">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇶
🇺🇸
طيران مسير مجهول يستطلع المنطقة الخضراء وسط العاصمة بغداد والقوات الامنية تحاول المعالجة بمنظومات EW .</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/86851" target="_blank">📅 23:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86849">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a31c1f52.mp4?token=rAcA8opgOnamn3JnMTFfu2Qzb3ZMykfoRHRx3XcMvkLjz0KjJj5YQ3Cff2CXKem-gts91uQUMY1iEqGBFEdBXZ-pQphbghMDkZvBDC_lsOpPYNK98OiLgKaMavyZMeOPk1sIQ0-3LVy3jg8eq_uIOtypeM25us68LyF47UhT25CJ0WQbwR4DcqxXTelWyNZcYnlrylagFrL0QtNNPHu2FOahtxwV3DfXJo2vqwKGMhO1dVhgVJqh8JvMBQqrCk1Hq_EYz6IAyWyXHwdrN6Z2ccnloGbOiOgNZtAMLbKCmYWH1upsXyw4zAvCPPNbuA52oKlgBv4V1bMgpWdurkEamQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a31c1f52.mp4?token=rAcA8opgOnamn3JnMTFfu2Qzb3ZMykfoRHRx3XcMvkLjz0KjJj5YQ3Cff2CXKem-gts91uQUMY1iEqGBFEdBXZ-pQphbghMDkZvBDC_lsOpPYNK98OiLgKaMavyZMeOPk1sIQ0-3LVy3jg8eq_uIOtypeM25us68LyF47UhT25CJ0WQbwR4DcqxXTelWyNZcYnlrylagFrL0QtNNPHu2FOahtxwV3DfXJo2vqwKGMhO1dVhgVJqh8JvMBQqrCk1Hq_EYz6IAyWyXHwdrN6Z2ccnloGbOiOgNZtAMLbKCmYWH1upsXyw4zAvCPPNbuA52oKlgBv4V1bMgpWdurkEamQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
سفينة شحن تركية كانت متجهة إلى روسيا تتعرض لهجوم بطائرات مسيّرة في البحر الأسود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/86849" target="_blank">📅 23:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86848">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇧🇭
البحرين
:  ‏خفر السواحل تعلن عن تغيير منطقة العمل الخاصة بمشروع المسح البحري ثلاثي الأبعاد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86848" target="_blank">📅 22:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86847">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMx14vZhWj1V3fi1WuJNGHr_B1uSs-t5JMDKU69T9FbHzn5uaHmYsW9_jjBPx4jOqby-QYxd0VNWLIny_D54tOR7rykkExykJEqad5nPTIsnmVVugmUUsbPcOGt4iDF8DydFvCzuNEtEJXdrLR2QCNX9BgZi_FsUxCyMY-KbTpP49PpDybDMCSSCerAdUfMSS_M5aIzBc7pTYQ_GS6OstO-5ZWTFrxsa4wZ25IsuErME_AIWmU_gPYPXMKPIqC0UjhGcecTIY7pkqEjryf7eO1t-0psrFsHypRTKkbFnFUUiUk0yAbfiG6cNeCRQxES5_eqdiabvJhhhkbDh0vDJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇨🇳
تعزيزًا للعلاقات بين الشعبين العراقي والصيني، أطلقت شركة باورشينا (PowerChina) الصينية العاملة في العراق مواكب خدمية لتقديم الطعام والمياه والفواكه لزوّار الإمام الحسين (عليه السلام) خلال زيارة الأربعين.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86847" target="_blank">📅 22:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86846">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992b3aa52c.mp4?token=RE_ZxdZJW12lxhMvjc1vLH2s0Qv_HM8gljvKSAVgArkBWWXBnELZz0IOVrz5REngXoPVwqnJoNXJn-RMLV3LEiRMSMYDesOkoPWBbRCpRsXPq6ijAlI0XNrQh-d8xgYNKNxBRjMVDy6HQxJzZ0EGP-Bm-UvrqM2E0lW6oiSHXmCyo-mEiyMNlcHusXMwNjrOpXBtCYbx0Mb10pMhXVZuwsWmuoGB6WZbEfkLU1GP5ZpaI45WcAt-1RZK1FywS-kIUmmcOCWk3QEeBZPUWDVpWjYIliBI6sv6PuXT4FQx0SLUAsIBKQUGCZ7YToiX1dnCkEDqkey8jUpOShi_faijEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992b3aa52c.mp4?token=RE_ZxdZJW12lxhMvjc1vLH2s0Qv_HM8gljvKSAVgArkBWWXBnELZz0IOVrz5REngXoPVwqnJoNXJn-RMLV3LEiRMSMYDesOkoPWBbRCpRsXPq6ijAlI0XNrQh-d8xgYNKNxBRjMVDy6HQxJzZ0EGP-Bm-UvrqM2E0lW6oiSHXmCyo-mEiyMNlcHusXMwNjrOpXBtCYbx0Mb10pMhXVZuwsWmuoGB6WZbEfkLU1GP5ZpaI45WcAt-1RZK1FywS-kIUmmcOCWk3QEeBZPUWDVpWjYIliBI6sv6PuXT4FQx0SLUAsIBKQUGCZ7YToiX1dnCkEDqkey8jUpOShi_faijEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحاج أبو آلاء الولائي الأمين العام لكتائب سيد الشهداء، بين العتبتين المقدستين في محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86846" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86845">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98195db8f9.mp4?token=fzdu8Wn87lJglvE4c0-EonPwPA0ySzhOTALAiyJa4hw6UuQAkNqXcQ-tf7J35hkB7b2SXDRSwQD3ONtosZNkBwdpCy8vbTGY7zNiwkYNtQp-Y_XK1Pvn5MM1B5DIe_rGvwTphBEBfFK_kWzPL44w8MW_095i0Nf_-FculB_MdVKpasdBSbeS-4js1OOQ_xproySxbye0BpwUySfGblWUEf5T6E3JTPWej6qCOYmJ7YpGPo_JbDT09fmsSk07wVe668GMBPmP1t6hbrR2_y_II1CHm2LVhHrwaej7E-CqJfrKC3FQ0bbF5fp1CVmd0eyHiuzdFJs8ODcnXNm2eoTR4l-dAUckqo41ewh3wxySqYex8CQH1wIe8nkqTP0oBknLY6CduAs1pFmqdOC6lsR-K3zXhAhKaJNaRtP6RqaTFf3DsVrQpvnsR_bIogi2LnsaZ0WhiBFizsGkdQpmdpnLEYXS342KK09mYkvQQxH1lUR_xmj0w4ONiMX9ZeSxvFw_BETqb-_cy5Txm-1-HUHjd3GiH1ZVYECnXttqzKSObtxf7GP-KxGg0DphoKga0jmywkpr-lcKfrE_ym7PVMHkE9B7sgdkw6PLH6YKzz336Vdf_0-jv-R0oJR-zB8oHn8fQ3G4MtgwKgCLpF3zPeAIvFI4d1GkrHQF-IdzPOjvX8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98195db8f9.mp4?token=fzdu8Wn87lJglvE4c0-EonPwPA0ySzhOTALAiyJa4hw6UuQAkNqXcQ-tf7J35hkB7b2SXDRSwQD3ONtosZNkBwdpCy8vbTGY7zNiwkYNtQp-Y_XK1Pvn5MM1B5DIe_rGvwTphBEBfFK_kWzPL44w8MW_095i0Nf_-FculB_MdVKpasdBSbeS-4js1OOQ_xproySxbye0BpwUySfGblWUEf5T6E3JTPWej6qCOYmJ7YpGPo_JbDT09fmsSk07wVe668GMBPmP1t6hbrR2_y_II1CHm2LVhHrwaej7E-CqJfrKC3FQ0bbF5fp1CVmd0eyHiuzdFJs8ODcnXNm2eoTR4l-dAUckqo41ewh3wxySqYex8CQH1wIe8nkqTP0oBknLY6CduAs1pFmqdOC6lsR-K3zXhAhKaJNaRtP6RqaTFf3DsVrQpvnsR_bIogi2LnsaZ0WhiBFizsGkdQpmdpnLEYXS342KK09mYkvQQxH1lUR_xmj0w4ONiMX9ZeSxvFw_BETqb-_cy5Txm-1-HUHjd3GiH1ZVYECnXttqzKSObtxf7GP-KxGg0DphoKga0jmywkpr-lcKfrE_ym7PVMHkE9B7sgdkw6PLH6YKzz336Vdf_0-jv-R0oJR-zB8oHn8fQ3G4MtgwKgCLpF3zPeAIvFI4d1GkrHQF-IdzPOjvX8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أَعِرِ اللهَ جُمْجُمَتَكَ، وَاضْرِبِ القَوْمَ بِسَيْفِكَ، وَانْظُرْ إِلَى أَقْصَى القَوْمِ.
جمجمه‌ات را به خدا عاریه بده، با شمشیرت بر دشمن ضربه بزن و تا دورترین نقطهٔ لشكر دشمن را بنگر.
We ready to make one of the most biggest fire party in the world</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86845" target="_blank">📅 22:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86844">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
‏س: هذه هي المرة الخامسة على الأقل التي توقفون فيها الغارات الجوية على إيران منذ أبريل. ما هي رسالتكم للشعب الأمريكي بشأن ما تغير هذه المرة؟  ‏ترامب: حسناً، لا أعرف. أريد أن أمنحهم كل فرصة أخيرة قبل قطع رؤوسهم.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86844" target="_blank">📅 22:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86843">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTVD2U0_wvieAjrCgJacS6xNG22TEAJacwJw3OZjBgcD1qm51_n0VejnzUToqH22sbf0LYX2qcEwLEBexhrs5i9DILpeucu-YlYwprCmU8KKMcxHWoe_2ohh47mw1V2ohUqjVPR_Mvefv7wgbMCjjiKgKDKGIwSKhvrZN8JMQtyk4z68qUiy1EHcQFsLEnCHRr-0AiSr0frKtX52Fc0NxZsEFqIBd-a3kAmRS2-GcdvxkFoSALbHR8XaoEr8DBk08uZ2H_iu5Hbepat5q5ug9uMgz0hw0IFXLoCMzP6TqKPUGhAazXcYXQCC1njnmNM21rpI-xzE45eFNdHTWweK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏س: هذه هي المرة الخامسة على الأقل التي توقفون فيها الغارات الجوية على إيران منذ أبريل. ما هي رسالتكم للشعب الأمريكي بشأن ما تغير هذه المرة؟  ‏ترامب: حسناً، لا أعرف. أريد أن أمنحهم كل فرصة أخيرة قبل قطع رؤوسهم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86843" target="_blank">📅 21:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86842">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
ترامب حول الرسوم المفروضة في مضيق هرمز: لن أسمح لإيران بتحصيل أي رسوم، إذا كان هناك من سيفرض رسومًا، فسوف نكون نحن، لدينا سيطرة كاملة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86842" target="_blank">📅 21:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86841">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇹🇷
سفينة شحن تركية كانت متجهة إلى روسيا تتعرض لهجوم بطائرات مسيّرة في البحر الأسود.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86841" target="_blank">📅 21:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86840">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b23deb7a.mp4?token=pCh_2oljyY57zWQzZr5DgzgTvwgH60Vom5pYzWI3jZOszfbqdIpsyMwCau2SqAHoMZqxQdKTz2YlheK3bY2ZVMxei5bLFITH9znC1lKRNA7zR5IQB68-2LqCUXCPUy1Ov362spg1IJBi4tiTFT7mYDo6_zHyf2_NQ3cXmz_kRH5VYDX6ALabMlyp_cBQFsrzADNfvNnortZhUkwFvmMzQQYmAY-__LXTBDjdcH0YXpfBZ3sP8u0_1M8EQEVAAcq1zB6uql57o7p3i31iOcYG082rU1UcfouDCOIu6qtoFF8qGStD2n17Azq10GLUdYnaAg5pbA8iDecQg0m1JZ5Ejw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b23deb7a.mp4?token=pCh_2oljyY57zWQzZr5DgzgTvwgH60Vom5pYzWI3jZOszfbqdIpsyMwCau2SqAHoMZqxQdKTz2YlheK3bY2ZVMxei5bLFITH9znC1lKRNA7zR5IQB68-2LqCUXCPUy1Ov362spg1IJBi4tiTFT7mYDo6_zHyf2_NQ3cXmz_kRH5VYDX6ALabMlyp_cBQFsrzADNfvNnortZhUkwFvmMzQQYmAY-__LXTBDjdcH0YXpfBZ3sP8u0_1M8EQEVAAcq1zB6uql57o7p3i31iOcYG082rU1UcfouDCOIu6qtoFF8qGStD2n17Azq10GLUdYnaAg5pbA8iDecQg0m1JZ5Ejw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
تضهر صور في الاقمار الصناعية تضرر محطات ومصفات في ينبع اثر الهجمات الاخيرة التي شنها انصار الله في اليمن.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86840" target="_blank">📅 21:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86839">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ab223602.mp4?token=CeBkTIvPNjuqPjJD5msjH69feFZOmOv-98V-20HShG-ksXCafGQ4tbUq-grZ8qjaMJa-9GnAqYgfEFnlOPYUi28Z3AKMTwAE4GAmvGyaHTCB6nQJnTGs0dHDdC-JemRIoPC_edb2VAyPHDKC7k0vJHXKNFMxtG1SpVThVQc6q_6xebjml353Ed1cVmBzToofOe3k4y-uYdOEpPI-mMvPll498GWs7zUKaMZ6THa4O7TFEb4d-PBZ5XDum03QKquzuccTPiG08YnCsCkMcKnVH1wzTfWL-VRAhLHF-XmAl5kC_Jd_yqn3QNdX6j1nqUScEPMcC_r6ZXOsBGQbDCmjZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ab223602.mp4?token=CeBkTIvPNjuqPjJD5msjH69feFZOmOv-98V-20HShG-ksXCafGQ4tbUq-grZ8qjaMJa-9GnAqYgfEFnlOPYUi28Z3AKMTwAE4GAmvGyaHTCB6nQJnTGs0dHDdC-JemRIoPC_edb2VAyPHDKC7k0vJHXKNFMxtG1SpVThVQc6q_6xebjml353Ed1cVmBzToofOe3k4y-uYdOEpPI-mMvPll498GWs7zUKaMZ6THa4O7TFEb4d-PBZ5XDum03QKquzuccTPiG08YnCsCkMcKnVH1wzTfWL-VRAhLHF-XmAl5kC_Jd_yqn3QNdX6j1nqUScEPMcC_r6ZXOsBGQbDCmjZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: نتحدث مع ايران لفتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86839" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86838">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
ترامب: "كنا سنهاجمهم بقوة بالامس. بقوة كبيرة جدًا. بقوة أكبر من أي هجوم منذ الحرب العالمية الثانية."</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86838" target="_blank">📅 21:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86837">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
ترامب: نتحدث مع ايران لفتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86837" target="_blank">📅 21:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86836">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad669497cf.mp4?token=gyShAsy6hMN1Ykss2szQFnIERselWEXVVWjwVecOrtlNK5WF3u1Dhx7Im8YLwGuctCv5X4Ip-D_zKO71Bu4I8vrkYPZ0e4gFHtEPVwU42nBI_hB50c26MrrVr3Y5GlApUm9b_jSo6v2yygHr10HhytbftrGu756E729UpiGt5GuqA9m6sN2RL4DYDW-Fv2xv4kL-OiWylFkyZgKSKR3Y-ppr1rpx4agWMnolE7lRQlR3GRgHoYsGG8359g3EAkFtSn9U57T5pFtA9u7BLsKqxEIvHU0NB6MWw1ydnkgQq4_grP0iXixg0Kt6Ph9QrShcauy_tkNNiS_f6Ygeo2DKGn3ohSUhIv0I8xCNbmCfOLVQjybvPYuBVs9qOczD2_KUZSq0z6DdU2EZqiCaGc8AipHB-lAD92SNtpA8-6h_BSocO7aCfem2aqOxVH0rZ1gxaDFIH1uDCiOkl5w9AyDEPteEinqtaCQWvF2v0I97OJ3xVCna_hhoaEbP7uwcENsDKEyGC9BA1wF0FWoQpTbxq74ti3lx3eQl_FW7sMpLu01l8Q_gRKGarVdnYJPuW2lZpRNTfd7cyNp8Zg2lL7mzcS3vq4bY2TVm1cGtjO1v9gUNWMYMs_njIYG494ba45IT7hltAKm4VrPAc19PEMeVQDn9FdWLNlI3eMREEv2NyOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad669497cf.mp4?token=gyShAsy6hMN1Ykss2szQFnIERselWEXVVWjwVecOrtlNK5WF3u1Dhx7Im8YLwGuctCv5X4Ip-D_zKO71Bu4I8vrkYPZ0e4gFHtEPVwU42nBI_hB50c26MrrVr3Y5GlApUm9b_jSo6v2yygHr10HhytbftrGu756E729UpiGt5GuqA9m6sN2RL4DYDW-Fv2xv4kL-OiWylFkyZgKSKR3Y-ppr1rpx4agWMnolE7lRQlR3GRgHoYsGG8359g3EAkFtSn9U57T5pFtA9u7BLsKqxEIvHU0NB6MWw1ydnkgQq4_grP0iXixg0Kt6Ph9QrShcauy_tkNNiS_f6Ygeo2DKGn3ohSUhIv0I8xCNbmCfOLVQjybvPYuBVs9qOczD2_KUZSq0z6DdU2EZqiCaGc8AipHB-lAD92SNtpA8-6h_BSocO7aCfem2aqOxVH0rZ1gxaDFIH1uDCiOkl5w9AyDEPteEinqtaCQWvF2v0I97OJ3xVCna_hhoaEbP7uwcENsDKEyGC9BA1wF0FWoQpTbxq74ti3lx3eQl_FW7sMpLu01l8Q_gRKGarVdnYJPuW2lZpRNTfd7cyNp8Zg2lL7mzcS3vq4bY2TVm1cGtjO1v9gUNWMYMs_njIYG494ba45IT7hltAKm4VrPAc19PEMeVQDn9FdWLNlI3eMREEv2NyOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حيث نتحدث حاليا عن فتح مضيق هرمز بالكامل.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86836" target="_blank">📅 21:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86835">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085519ec4b.mp4?token=elK-0IAqLCezzrDI8gZNP2nZaqfuB5uO6zcKPrpTa9zw2vzt13HsMcuLMbLUGXpgSY8gg6iMeeN7IFUVm6vM6vdqSfWyO30y_s-6-0Iz0VhCr8SRWvF4p57lDwabqBUJjjfyrtONO0r2HaBBfN3T11PnC2YnaVwKQmTBf6AZE62_hm-EPYl6LjjYtF3MxTMbKkDgA-8MvC7CEZ11XKxG6NW7gj7e50_lbbXUMucXCEhAeJj4-5Bg2H4k51rMAc47X5ZEm_o4ocpdEM-34kFA7chl2DUpJpIMXIVLLCoknjXDmrVCjITiQPP4wIv4cQDjY2aTvxWNs3-audsoBec7VnRhLPJEKcqeMW8cjQbhb__BCjR5Yp5PhKd3WBHzTafitiwbyKtsCVA8_U1mbMaoVemkDqLVMUQK-NqooldkQmMagoi4EgKabhsEQXE2UgKC5eZUfPn1tqcV28Vs-yLasAGHjh4xU1Tsz2kAzseFa8ltjze78fcQ63qVM7YtAWmYoSPwcR9AiW4Zq8S6a7U3xUXArGiUTWlFQW1KFGCG4EcKlzLy44zQ9KkKjLIBiVKbDO74AkP17Dai87rWozsmh8H0nEA0zrZOzuL3SoQUT43AsmVSqgOADPz02LmszxBU9rzwzVqLgFy7CY9j5Vf9ZxM7083fEc8gRfsx1GUAQX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085519ec4b.mp4?token=elK-0IAqLCezzrDI8gZNP2nZaqfuB5uO6zcKPrpTa9zw2vzt13HsMcuLMbLUGXpgSY8gg6iMeeN7IFUVm6vM6vdqSfWyO30y_s-6-0Iz0VhCr8SRWvF4p57lDwabqBUJjjfyrtONO0r2HaBBfN3T11PnC2YnaVwKQmTBf6AZE62_hm-EPYl6LjjYtF3MxTMbKkDgA-8MvC7CEZ11XKxG6NW7gj7e50_lbbXUMucXCEhAeJj4-5Bg2H4k51rMAc47X5ZEm_o4ocpdEM-34kFA7chl2DUpJpIMXIVLLCoknjXDmrVCjITiQPP4wIv4cQDjY2aTvxWNs3-audsoBec7VnRhLPJEKcqeMW8cjQbhb__BCjR5Yp5PhKd3WBHzTafitiwbyKtsCVA8_U1mbMaoVemkDqLVMUQK-NqooldkQmMagoi4EgKabhsEQXE2UgKC5eZUfPn1tqcV28Vs-yLasAGHjh4xU1Tsz2kAzseFa8ltjze78fcQ63qVM7YtAWmYoSPwcR9AiW4Zq8S6a7U3xUXArGiUTWlFQW1KFGCG4EcKlzLy44zQ9KkKjLIBiVKbDO74AkP17Dai87rWozsmh8H0nEA0zrZOzuL3SoQUT43AsmVSqgOADPz02LmszxBU9rzwzVqLgFy7CY9j5Vf9ZxM7083fEc8gRfsx1GUAQX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: الفرصة الأخيرة لإيران لتوقيع وثيقة جيدة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86835" target="_blank">📅 21:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86834">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323354d999.mp4?token=l8gAvDZbQwmOl0TcfLa7U-3vLdBIGTwkgzEpEOchN-a9BZD92dxYsNtAWE4lB7zAfoFdwyFZOlOIjKna2OqaGX8mtMz4V5BucJ92TJjDFt0soT_v0uCcV4smsAbGhZYr0nGoSykPdcqVT7V9iS7jQPOXs9zdkcf8ZhthI_6wC-VkkT-2bIdktUmYcKwkoh9WZoLeUOOvYWvZUcUSxU7ZDBnrDSv501OL6wtqKI4-C3TfkOikZNs9qCmF1-AMQ0w6iTlTxeQKP_TpLL-JkuC9enRJ59RyED0ru7LwPCwzChi6MwF_NF7XLUnC2NvbljJj3PKZ-RdIkDcO_rtVl_qfe73bI732HJgvhBayDlzXkPdS62tEbhiN8c7Ue4WspzhB8cxcCefae7ZTOeiIPYyz1GfJyf68aGtfbAUB1FG-dzk0hdSLgTbkWhg9anu3_ci-JalrFyIv58LYEQtPC7rXy4NEtidifQTAGPg4Sm5rgf_4CZQzZvW9WauqG5b8yQwgj_ShXmTWQzwPXsUKYY3Fs-SP7AMTzQU3EnNMw_3VYWSftdb7a7-dH7usetjmX24ckY8-DHoFsAnyJnbPG9MBFmzQxHCJYkkhwXLXpUOEbOvXrZsnnXvi6RMAqiGyB9BpYlHJkC6SKF7TR7BnIiT1IItg8o8tCVhkjEresTcNFBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323354d999.mp4?token=l8gAvDZbQwmOl0TcfLa7U-3vLdBIGTwkgzEpEOchN-a9BZD92dxYsNtAWE4lB7zAfoFdwyFZOlOIjKna2OqaGX8mtMz4V5BucJ92TJjDFt0soT_v0uCcV4smsAbGhZYr0nGoSykPdcqVT7V9iS7jQPOXs9zdkcf8ZhthI_6wC-VkkT-2bIdktUmYcKwkoh9WZoLeUOOvYWvZUcUSxU7ZDBnrDSv501OL6wtqKI4-C3TfkOikZNs9qCmF1-AMQ0w6iTlTxeQKP_TpLL-JkuC9enRJ59RyED0ru7LwPCwzChi6MwF_NF7XLUnC2NvbljJj3PKZ-RdIkDcO_rtVl_qfe73bI732HJgvhBayDlzXkPdS62tEbhiN8c7Ue4WspzhB8cxcCefae7ZTOeiIPYyz1GfJyf68aGtfbAUB1FG-dzk0hdSLgTbkWhg9anu3_ci-JalrFyIv58LYEQtPC7rXy4NEtidifQTAGPg4Sm5rgf_4CZQzZvW9WauqG5b8yQwgj_ShXmTWQzwPXsUKYY3Fs-SP7AMTzQU3EnNMw_3VYWSftdb7a7-dH7usetjmX24ckY8-DHoFsAnyJnbPG9MBFmzQxHCJYkkhwXLXpUOEbOvXrZsnnXvi6RMAqiGyB9BpYlHJkC6SKF7TR7BnIiT1IItg8o8tCVhkjEresTcNFBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏المراسل: المحادثات مع إيران توقفت الآن.
🇺🇸
‏ترامب: إنهم مستمرون الآن. إنه أمر مذهل.  ‏إنهم لا ينكرون ذلك هذه المرة.  ‏لكن لسبب ما، عندما يتحدثون، لا يحبون أن يقولوا إنهم يتحدثون.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/86834" target="_blank">📅 21:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86833">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167ef831e7.mp4?token=j3JFJgAaf-oMzZ8TOVERQFj-pY5qnttM5NHY1TmZTRs1RZoIvI8vQxE3o3fKARzt7d520RlFXRc6pOXTKmIdm0wjLE3QB6W9P8v18XWBFllf368c5p8u0nmM6j7bIVhRjrXj3srIjQ2zKRfWGjaSHPDI9csGUuSphBlY_KJlL6gokMzlAn0YDufKFt7xaTKzz6mGJaKf5HQGExlZccb0tImqgegGwYumWvChrbSQX6GIINCnE1KlsPxXChxeZI2voSVpYuf9f7LITAX5ogbEOzVGGQ7XXIPm-crpZOihSb5pFOmVstwowcVbpZxPHVNA9IFGG0efewVWoDBVIkU42IuAsYRM4DNtU4F6nOOfr5al-6ZndIqmRPxBq5dMGHojgwEamZXjIXesRg7qcrlPCgm4HRL0homU1N1vZk2v5inwM-NJPsVltKlrJmVm2C9xEoXjnLndH9vOMKU698p4vFFdCTU-HQKI-taTKqc5AG_kX3PJblhmYNam0lr7wRrCn-kNfjWPJP2Xw3BEhaeiOZ-1snd8YORcZ13FWk9hCny4LiIAJKBmTu58ubVw4Zeq2NE2cjZwFgOl2MiL7fQxX2lEfVX8fBsmUlSBaGVFsxPDNESOvi9ctWiotSicBAsR4epnzbbvZnT6D8GON2OfKQtoVLAtb5skjnlM-_CH9g4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167ef831e7.mp4?token=j3JFJgAaf-oMzZ8TOVERQFj-pY5qnttM5NHY1TmZTRs1RZoIvI8vQxE3o3fKARzt7d520RlFXRc6pOXTKmIdm0wjLE3QB6W9P8v18XWBFllf368c5p8u0nmM6j7bIVhRjrXj3srIjQ2zKRfWGjaSHPDI9csGUuSphBlY_KJlL6gokMzlAn0YDufKFt7xaTKzz6mGJaKf5HQGExlZccb0tImqgegGwYumWvChrbSQX6GIINCnE1KlsPxXChxeZI2voSVpYuf9f7LITAX5ogbEOzVGGQ7XXIPm-crpZOihSb5pFOmVstwowcVbpZxPHVNA9IFGG0efewVWoDBVIkU42IuAsYRM4DNtU4F6nOOfr5al-6ZndIqmRPxBq5dMGHojgwEamZXjIXesRg7qcrlPCgm4HRL0homU1N1vZk2v5inwM-NJPsVltKlrJmVm2C9xEoXjnLndH9vOMKU698p4vFFdCTU-HQKI-taTKqc5AG_kX3PJblhmYNam0lr7wRrCn-kNfjWPJP2Xw3BEhaeiOZ-1snd8YORcZ13FWk9hCny4LiIAJKBmTu58ubVw4Zeq2NE2cjZwFgOl2MiL7fQxX2lEfVX8fBsmUlSBaGVFsxPDNESOvi9ctWiotSicBAsR4epnzbbvZnT6D8GON2OfKQtoVLAtb5skjnlM-_CH9g4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: ‏عندما تتحدث إيران، فإنها لا تحب أن تقول ذلك، والمحادثات مع إيران جارية الآن، حيث نتحدث حاليا عن فتح مضيق هرمز بالكامل.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86833" target="_blank">📅 21:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86832">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
‏ترمب: الصراع مع إيران يسير على "نحو جيد للغاية"</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86832" target="_blank">📅 21:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86831">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
‏
ترمب
: الصراع مع إيران يسير على "نحو جيد للغاية"</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86831" target="_blank">📅 21:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86830">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇶
رئيس شركة "سومو" العراقية:
تبلغ ضريبة الجمارك على نقل النفط الخام عبر تركيا 1.62 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86830" target="_blank">📅 21:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86827">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_8w2jWLDfdvKiUuOH2flUqJN-fLgSjQJjtvltsoXM08ykYEdlShG0v8nR_n2f1ESBHpogomfabNDnSVPivi0AmuvMA7kEhy9NOWGkGFdQ3mGlUtLVY8pOjbJeUGK2pKuWAxaJ2imZhJcycGXtYak0TNiQAv9AK13H-0PONPDjcuNHBOmYfxQfSj6QKGA0V7ES3C7PD-e_9nxUdsrCxVZfIBhgs4wtr9nB0uVhY1LEMWChqxaQ3iqhGnVjuxhp9fj6KdzvUqjVjNFHZFzME4gEsRNLIfR4Py5Hzkp55lXEQNlB9fH-k4fH2rS-xSq4TBbtIfhGXCAwHAJi_0dkyCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1c8nXVCtwifCBC_JdvRJYVKYtTEkfRIQI8IVkLeEGVfSPzF_4q34vaDKlcYc0i4o3UOqaUX8-e0wGzgLQ2ARjdb1eMyXCgyI1_ambONKb8qVhsegua3JfOebas7vj1wn500mGaAbwjuG-isUjXEb0Anqk2eTqUyfDuBBc3yFZuDeImXz_JXq-HOsm2AkD5psBarUszcI34qjIn1cf2-nKkEvTAJm0TFlFYE3ni0gErTcBrKwGWWtRDAYpd2gPrVWPQjiHEYfNnADfXYi9pecyzeLzx_dumrzfg2yZZwvUpW_YEgHS4IAQxq751jkBq6d2oYT9Qg7Gw4VuaVVcqM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oz68lekJZzYvoJ5n5VDe5aPTrIoHW2hzU1mj-D2n6Njg-NsWi3Efuw0a1Il2fpXM3qK06C2Hqw8GJux-3gyX48Y7H6jRH6M8SrFrJD92-jVdJ_N69SVCo6vN1RMp3Ego3VUBeQo2Vy7LYZRfmMgjyNhyWjiPP6-OAPN3pGRdzA7-f0v5FVhuFAcyraY_6mJJhLybEZw7SKtMDyZk1f1iqfB3k6UCEa2pXy5hWXfF1XRe8Qqw6QFwSksXAWX8vIaABtC2vV8kB8HvJPq7ra9szscnpjg14nXalIh6nSORO_OpPthCiYp70hxNO8TwnFTjoHcW4kETnTs9PHG1syaQDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">المواكب الحسينية التابعة للحشد الشعبي تستعرض بجرائم ال سعود اتجاه الشعب العراقي في محافظة كربلاء المقدسة
ال سعود ظلمة</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86827" target="_blank">📅 21:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GD-yBX6N9GX3q5VGV7bnyz-WDlNLZ6A-b4w-2UrBSIwmFyOCw2lAFJ4YKiAqKpUOp1n0OTVrTByd-IIhw0J06aBhdb50JQPJIkD2BJXWq-MvxLcEz-h5wmdmXo3U588ctTk37GK0BnK8wf_ZeiWzmjDE_Aset0j-GZHQ-wehl1HQbDbAYPcQOFdqYkqqc8iM_xR6MrWn44_nunRaspylwSoi632AbEgVeG969ij89ALE6BNbwxbltSPAeozvOxX-fp7e0UhN7NAjSLDd427N9jh1WA9iM_LUL3aOb8NGoX1SMcisTP38kVyq6z0ovOtB1TBSYuCVV16Kn4Yr5r9PmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مروحي عراقي تحت إشراف أمريكي في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86826" target="_blank">📅 20:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86825">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
إعلام أمريكي : تم الإبلاغ عن أول حالتي وفاة في الولايات المتحدة لأشخاص أصيبوا بمرض داء السيكلوسبورا في ولاية ميشيغان.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86825" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhePHP75do4qkHS15_o_a1uLnxsCC45Tre7YNJhQBp244f5uQ3T8GwTmSrVJ6qcVL_WTixuLNWyPpSzzvt9SysYDlmwFy8xfBKlu0O1opbCzqy92-7UbFJOLpTIqVbBOqIBgBB3Fgk_O3eRVj9ogk8KbXG6iQjflCRL4QCl9LpSoios3pXXHZP8HhZgX0g9wsDt9-09lvb3VVKkXlqbDkZF-M_3MWdi20HePGSXQt_R2AYL4DCdtCyxzghrfnQGBfVJ-fqVwnsiGXcdQTSBWCG8GSN-0_psuGTlIXk-iBFJ7dtDodxE5O1_RQL6ElY6B7nQxBc9XTxLZuNsuDPYR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فيلق بدر متمسكون بالسلاح ..</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86824" target="_blank">📅 20:27 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
