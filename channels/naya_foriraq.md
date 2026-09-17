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
<img src="https://cdn4.telesco.pe/file/g20pT_YVNV4WUu4jZEcPrShFIrBvPBUCAatYEtI3CoVW7DusHQXChgg3yFuaD5AfLnZGJO6a6FkhycYfLW6z39lOJU7Wx6bnfuwzGfNCH12WrlhpuxqEIL6ApcNC9XbW6o7Jlck_UsC99v-4i_sANwG7SFvnl6Dc_eEtEghjdjTQATTL-2Ql24hddbb-1W22ZGIg1kTiXSon8YjVtY5M7y0o6trRW7Ls3XxEGkIebgsG5iYyPXgB5Gr_zd5UeOi-hyqwg4h6kkUGt_WX5s7AYIbS3Dq_EemKruKxDFkYtXwYoRoN7MuHrgWmg_Ocq8rKuDFB1RjwVHVmaKbG13fg8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 07:40:32</div>
<hr>

<div class="tg-post" id="msg-90758">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇸🇾
إندلاع إشتباكات مسلحة عنيفة بين عصابات الجولاني ومسلحين في مدينة الصنمين بريف محافظة درعا السورية؛ سقوط قتلى وجرحى من الطرفين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/naya_foriraq/90758" target="_blank">📅 07:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90757">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5f30186f.mp4?token=eX_elRKiZrUF-B6BoNXUCztoUFuG71b7Sa31V77ArJYI4fttsn3aXamkP6BrFRoFuHjo0IBYINBsvNrnPfGV9sRPbLZSgEnu8jHUY8bBdj_udEYMmB3PRXvvj5Lb_JLtxz65WCGtaVj90YD1gWJXG7GvPb8Og5Rzdp9Rzp5DZhSjo2vkiiWQFEH0AW9Zgf8karemm3Bu2mQYtKdxwR_JQ2U5fIuHopJoYnioLPTKRFIbd4OCtbpQZJHR8VaKXFZp5-lj7tSjty7dnPMOag2yKXbGL88n7coUCInegKz5pSY1VuQ_p54n7LHEZbu8QQ0WOuCk7_ytQEtdsQGIH7s5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5f30186f.mp4?token=eX_elRKiZrUF-B6BoNXUCztoUFuG71b7Sa31V77ArJYI4fttsn3aXamkP6BrFRoFuHjo0IBYINBsvNrnPfGV9sRPbLZSgEnu8jHUY8bBdj_udEYMmB3PRXvvj5Lb_JLtxz65WCGtaVj90YD1gWJXG7GvPb8Og5Rzdp9Rzp5DZhSjo2vkiiWQFEH0AW9Zgf8karemm3Bu2mQYtKdxwR_JQ2U5fIuHopJoYnioLPTKRFIbd4OCtbpQZJHR8VaKXFZp5-lj7tSjty7dnPMOag2yKXbGL88n7coUCInegKz5pSY1VuQ_p54n7LHEZbu8QQ0WOuCk7_ytQEtdsQGIH7s5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب عن إيران: بصراحة، الأمر سينتهي قريبًا لأنهم لا يستطيعون الاستمرار. أمتهم مدمرة.  قد يكون هناك ارتفاع طفيف في أسعار الوقود. لكن هذا سعر زهيد للغاية مقارنة بما فعلناه.  قد يكون الأمر أكثر من ذلك. وبصراحة، حتى لو كان الأمر أكثر بكثير، إلا أن هذا كله…</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/naya_foriraq/90757" target="_blank">📅 04:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90756">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b525552494.mp4?token=HAsul6Zh2TnOSLM60bhbg3hRPs26zZ82H_EmgjNdmw-Z3XBFFijOHileVaoLar02gde1kKHBNfxSPo13MwbcI9ZX0qYh6LgyUZ00CIkPryZP0bChy1SU0_5QPBGUuzFhhSuxsI-Hw7RtO_VCLCxzKXtni-5DBBZDYKuqsOFLwxzdLwo6UOCnzI_RygBXTOS4fj_7xa-OYhdmZYk2-xXDxXuskHBCtNm5t9-nAAc5GQKpR8gdEaFujbXHw7-kStrTXfKYOCOZBZNW0u3K1KDdFI6wxDjDjUFmnpKzy_7MK6oz8kI-xn66KYMNkVyZKNzwzPCz4-ui3oMvhQTze-bzYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b525552494.mp4?token=HAsul6Zh2TnOSLM60bhbg3hRPs26zZ82H_EmgjNdmw-Z3XBFFijOHileVaoLar02gde1kKHBNfxSPo13MwbcI9ZX0qYh6LgyUZ00CIkPryZP0bChy1SU0_5QPBGUuzFhhSuxsI-Hw7RtO_VCLCxzKXtni-5DBBZDYKuqsOFLwxzdLwo6UOCnzI_RygBXTOS4fj_7xa-OYhdmZYk2-xXDxXuskHBCtNm5t9-nAAc5GQKpR8gdEaFujbXHw7-kStrTXfKYOCOZBZNW0u3K1KDdFI6wxDjDjUFmnpKzy_7MK6oz8kI-xn66KYMNkVyZKNzwzPCz4-ui3oMvhQTze-bzYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
بعد أيام من إستحواذ إيران على قواصة وإستهداف سفن حربية أمريكية.. ترامب: كل شيء دمر في إيران وسلاحها البحري يقبع في قاع الخليج.</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/90756" target="_blank">📅 03:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90755">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب:  الإيرانيون يتعرضون لخسائر فادحة ويريدون التوصل إلى اتفاق بشدة.  الحرب مع إيران ستنتهي قريبا جدا.  يمكننا التوصل إلى اتفاق بشأن إيران في أي وقت نريده.</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/naya_foriraq/90755" target="_blank">📅 03:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90754">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76ac567e2.mp4?token=iF1oYSY_pvlCzN8MapNEkLHakG_pLIni3IElpvqbfDPdL3iajhCfzoS0wMQWc2qfR538Vry_yBSPN5K0QytcWwISl3PQ_dyU0-S4s3Kzf8O3OdLxrr63PUSQTxp9xQjGw99jUcGdvK8iImdK5PFq45X-K2ksuoonV8AcRpTTp68JRlwKzWItpZyDeHTY76-NpvetennkE7mxq73xUjpLsvXqwoVryQ75a48x1PKf1Q-d8h7Ri42k4HNi1q2QQOV2vf7puqC02quGrdSH0ezZ1fMIi3Euxa7V41hLhL-tfwVynf7u-4TnVnIp_LLJeotcSuGQaG_A7q7hkHAsSjM5FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76ac567e2.mp4?token=iF1oYSY_pvlCzN8MapNEkLHakG_pLIni3IElpvqbfDPdL3iajhCfzoS0wMQWc2qfR538Vry_yBSPN5K0QytcWwISl3PQ_dyU0-S4s3Kzf8O3OdLxrr63PUSQTxp9xQjGw99jUcGdvK8iImdK5PFq45X-K2ksuoonV8AcRpTTp68JRlwKzWItpZyDeHTY76-NpvetennkE7mxq73xUjpLsvXqwoVryQ75a48x1PKf1Q-d8h7Ri42k4HNi1q2QQOV2vf7puqC02quGrdSH0ezZ1fMIi3Euxa7V41hLhL-tfwVynf7u-4TnVnIp_LLJeotcSuGQaG_A7q7hkHAsSjM5FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🔻
ترامب: لماذا يجب علينا أن نتحمل عبء الكثير من الدول في أوروبا؟ نحن نتحمل أعباء الدول الأوروبية. كل ما علينا فعله هو أن نقول: "هل تعلمون ماذا؟ لن نتعامل معكم بعد الآن." نحن لا نحتاج إلى أي شيء لديهم.</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/naya_foriraq/90754" target="_blank">📅 03:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90753">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455b367be5.mp4?token=jRbgQgZtQia88r9cSe_mRGNa4PWzlygyZ4AM82X5LvmLU9w_dfXl_00qRd2cHnAa01XaWDggyZB3VWqdT-IvnbfvziyzwyQ-S0k71OpA5NGf0NXvCOVpK3zxqZ09wjLP0LmNDSia-wnX0Q2qwYCRflhwvvxM_UEwc_FZTulKhgee2Jp0h_uH70F5Rl-CJIftsJSKbxkeOhUOyjr1fCZ-6eJ6WnG9jJIZw-0dTivJIxDtBPZXbkMJ5_Rn9ZyDSE-fkukYg84VU0rJVOHXU0PkUi3tDHKnNQTd6eMxZ4-Gs--bsjyQxzFrRzK31mDjq8vktLiPrYSWNf0lp-WBvPcImg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455b367be5.mp4?token=jRbgQgZtQia88r9cSe_mRGNa4PWzlygyZ4AM82X5LvmLU9w_dfXl_00qRd2cHnAa01XaWDggyZB3VWqdT-IvnbfvziyzwyQ-S0k71OpA5NGf0NXvCOVpK3zxqZ09wjLP0LmNDSia-wnX0Q2qwYCRflhwvvxM_UEwc_FZTulKhgee2Jp0h_uH70F5Rl-CJIftsJSKbxkeOhUOyjr1fCZ-6eJ6WnG9jJIZw-0dTivJIxDtBPZXbkMJ5_Rn9ZyDSE-fkukYg84VU0rJVOHXU0PkUi3tDHKnNQTd6eMxZ4-Gs--bsjyQxzFrRzK31mDjq8vktLiPrYSWNf0lp-WBvPcImg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب:  الإيرانيون يتعرضون لخسائر فادحة ويريدون التوصل إلى اتفاق بشدة.  الحرب مع إيران ستنتهي قريبا جدا.  يمكننا التوصل إلى اتفاق بشأن إيران في أي وقت نريده.</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/naya_foriraq/90753" target="_blank">📅 03:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90752">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a82a8098.mp4?token=gDP8B9Fvqeh3pimO8AXLVka8EL-XdNcP4UyW5rNvZEiARHyRi02bKsNjjZA6nK8EbFJeLldJ6OyDWdUIufYheDeKe2sjWWotxUbD1o3iKwsd6XNN9GnT1XO5o79txjd11y7-yZjh2CGKptvF0UDltOTDfS_eNGK2SZI4NJwpE3_NYKyG0GUZ3IsuWRf724dnZOFgxB122Mhe8M9WPuDSQE8S5QYAX4THiU-g-Mi0VI8HKc8eBH3Fti4xuzKdJrJOGAafU7NKMW16zbw2AsRDBv-5T9jvY5cbMo87FF1GcYV-r0qaCX5_fAoNnJoajFpDZ4sdnREU4ljHzGhQ8RbSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a82a8098.mp4?token=gDP8B9Fvqeh3pimO8AXLVka8EL-XdNcP4UyW5rNvZEiARHyRi02bKsNjjZA6nK8EbFJeLldJ6OyDWdUIufYheDeKe2sjWWotxUbD1o3iKwsd6XNN9GnT1XO5o79txjd11y7-yZjh2CGKptvF0UDltOTDfS_eNGK2SZI4NJwpE3_NYKyG0GUZ3IsuWRf724dnZOFgxB122Mhe8M9WPuDSQE8S5QYAX4THiU-g-Mi0VI8HKc8eBH3Fti4xuzKdJrJOGAafU7NKMW16zbw2AsRDBv-5T9jvY5cbMo87FF1GcYV-r0qaCX5_fAoNnJoajFpDZ4sdnREU4ljHzGhQ8RbSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المراسل: هل تعترف بأنهم يرفعون الأسعار بهدف خفض التكاليف بسبب الحرب في إيران؟
🇺🇸
ترامب: لا، إنهم يرفعون الأسعار لجعلني أسوأ ما يمكن. المشكلة التي يواجهونها هي أن لدينا أقوى اقتصاد في التاريخ.</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/naya_foriraq/90752" target="_blank">📅 03:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90750">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8zZTbqxWUmB-5DaLGmqL_smfKILwUm1rDcQ1BbHKm90CPJW54-zv_IqtCEDGCeVuaYVO2jaYFncWQLHR0SogQ8dJFFafqUs9DXwW1nI0XT8-K9Eoi3g5_qOHPXNBQjE_XE-t27OM3UcpRB9NUwvtO0zIBf1AC6V5RrMQXWAoiOdvzLBir59181Q_Db76D-Y-CUPXgk0cCMqCvQv15qRiRUYz-eijJlB_OKsHFtfomGhzzBxbm5-oWuBoiWcLx-tBRBkWsaF8fnOF3Bx_LVolK2RCdYezVMEbkU9agyN95rD1rGUbc74JApVne679IFIHRVzRca0q6YdqKfZsuXWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e0c180b1.mp4?token=ru7YPlhf59Lt4TdNZiVtgokJRgzxtPN4RDBHzhwx4pTSCL15ec9lR3ZE1YN3s7TtnZVgsuA6ZLZu0j4yeLjx_hInFvG1ap7ui21AR4gOVTjY9nswh4qezLwIwlE9dzVqLFLA0iiH3ZF3Z_mm1b2pFONgHEE5Ny9FJOTEkDlFGYauSktOmflVMO_8XNyR3nv5CWKv7Ogim8F78Ple-dTap2xAjT-JZBD6nj7okeZxvpxrOyAWOYQgG3GJktR53NNNnL6VDdXI9-5D1EFydI2vilXP2yxwc5dx5qOWv87ITcV9HThLgqfF18zzzUi6Bp7LROCrXUFCk5KQWdP1G-Sbig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e0c180b1.mp4?token=ru7YPlhf59Lt4TdNZiVtgokJRgzxtPN4RDBHzhwx4pTSCL15ec9lR3ZE1YN3s7TtnZVgsuA6ZLZu0j4yeLjx_hInFvG1ap7ui21AR4gOVTjY9nswh4qezLwIwlE9dzVqLFLA0iiH3ZF3Z_mm1b2pFONgHEE5Ny9FJOTEkDlFGYauSktOmflVMO_8XNyR3nv5CWKv7Ogim8F78Ple-dTap2xAjT-JZBD6nj7okeZxvpxrOyAWOYQgG3GJktR53NNNnL6VDdXI9-5D1EFydI2vilXP2yxwc5dx5qOWv87ITcV9HThLgqfF18zzzUi6Bp7LROCrXUFCk5KQWdP1G-Sbig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يستهدف العاصمة كييف ومدن أوكرانية أخرى.</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/90750" target="_blank">📅 03:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90749">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
‏
أكسيوس:
ترامب سيعقد مباحثات بشأن إيران مع قادة وفود دول الخليج بنيويورك الأسبوع المقبل.
‏ترامب سيطلع دول الخليج على أفكار لاستراتيجية ما بعد الحرب مع إيران.</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/90749" target="_blank">📅 03:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90748">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يستهدف العاصمة كييف ومدن أوكرانية أخرى.</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/naya_foriraq/90748" target="_blank">📅 02:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90747">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec03755b2.mp4?token=cYR0hVqvJ1yFRxLt36289asHhpwhG0nt1I8lEDQldoZmagJGbxX76xX7VIXKfQUpO3ppoThLYza6Gpn992q_rkpwWTPYrwCxa1xsTv8ImmiVZ0flhrzvqibAaqf347Af02nmaSbwzFnzlvC7Ip3wzwF3M5VAj609Na3mralYHl4Ad8zIO8li1DiWwFAuiNCRSrunRwU4HrUmPluOdNWAMEo31YvmpbzTqnVEKlSKdWBTMVhb0tlj6oUW4rSqgyTqSaykRDMSYp5rkrOWi6koTjCFKcBmj9yCSbxUGWDXNYHflywvgGuiC_8zZWLst9slIjm4ubw-aiH2CMUZQxEkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec03755b2.mp4?token=cYR0hVqvJ1yFRxLt36289asHhpwhG0nt1I8lEDQldoZmagJGbxX76xX7VIXKfQUpO3ppoThLYza6Gpn992q_rkpwWTPYrwCxa1xsTv8ImmiVZ0flhrzvqibAaqf347Af02nmaSbwzFnzlvC7Ip3wzwF3M5VAj609Na3mralYHl4Ad8zIO8li1DiWwFAuiNCRSrunRwU4HrUmPluOdNWAMEo31YvmpbzTqnVEKlSKdWBTMVhb0tlj6oUW4rSqgyTqSaykRDMSYp5rkrOWi6koTjCFKcBmj9yCSbxUGWDXNYHflywvgGuiC_8zZWLst9slIjm4ubw-aiH2CMUZQxEkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:  سعر الفائدة مرتفع للغاية ولا يعكس حقيقة الوضع الاقتصادي.  نحن في آخر مراحل الحرب مع إيران.  ‏قد نفرض تعريفات جمركية باهظة على أوروبا إذا اعتبرنا منح كندا صفة دولة مراقبة عملاً عدائياً.   إيران تريد بشدة التوصل إلى اتفاق.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/90747" target="_blank">📅 02:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90746">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔻
دوي إنفجار في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/90746" target="_blank">📅 02:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90745">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9188e09e6.mp4?token=EzUg4jkoEefMubrTL4cSLcfae4UEUr-NMLWxuBuewR46s9_AtwE5SrEjq24ymWmIoPAoiTeegLIfVc-0p4Xtho2AwF9c_bBMkPkXpkFsiOOs6rAXG99hbsbXXjeeHtXZ1_zk1kgFKZYKCZVplr-Snd6Ka4twphFFGRf_VM7kvRep_rOmoUna7TDK6j9qEQ6HXw70AfKzeE8IXprGAYa1Z1I1OQXFmf_B24k_joJkP59wnWMcf9bcNIPyABx0jxJILMMJOKYphy6NUGNXCdj_Ink1w0a_8HVQdvXnECn9noSvgvQvsZf6TpnQw0PkXdCmUq8Oaw44jSB7P7R4X6wC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9188e09e6.mp4?token=EzUg4jkoEefMubrTL4cSLcfae4UEUr-NMLWxuBuewR46s9_AtwE5SrEjq24ymWmIoPAoiTeegLIfVc-0p4Xtho2AwF9c_bBMkPkXpkFsiOOs6rAXG99hbsbXXjeeHtXZ1_zk1kgFKZYKCZVplr-Snd6Ka4twphFFGRf_VM7kvRep_rOmoUna7TDK6j9qEQ6HXw70AfKzeE8IXprGAYa1Z1I1OQXFmf_B24k_joJkP59wnWMcf9bcNIPyABx0jxJILMMJOKYphy6NUGNXCdj_Ink1w0a_8HVQdvXnECn9noSvgvQvsZf6TpnQw0PkXdCmUq8Oaw44jSB7P7R4X6wC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مجلس النواب الأميركي يصوت لصالح تشديد العقوبات وفرض رسوم على روسيا وإيران.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/90745" target="_blank">📅 01:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90744">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
مجلس النواب الأميركي يصوت لصالح تشديد العقوبات وفرض رسوم على روسيا وإيران.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/90744" target="_blank">📅 01:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90743">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f566eb691.mp4?token=dUdoirDbWVkxRUnX0miemt65Ji0jxuKbNMF9vj4NpPAu-X_0JBHaFX52TEOffzr6dhX1fTEGsqJAiNix2LxkvYVW8r-SZeVjTxaOdMYEfTIphazqaoyzYWarkJb9Dih0O7a4Rr6qg6OC_n1hAdAR9ik3qf_9W7wF11CzKMd3IidCqQxs5jIo4AGxfF2aLkJAvbnP-qo1qF7chyjlCqoN51illNWjhWNJKypGnkxYpgCAcP_n7vLdUOCipfzlSpk725tJ7zgg8Fvua7bZZ4iCmuQOMjO6pPHIPKzmb0GF0B8744voLcm6ogxQH8MqlMaelIRvn7fb32ba67603YjheA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f566eb691.mp4?token=dUdoirDbWVkxRUnX0miemt65Ji0jxuKbNMF9vj4NpPAu-X_0JBHaFX52TEOffzr6dhX1fTEGsqJAiNix2LxkvYVW8r-SZeVjTxaOdMYEfTIphazqaoyzYWarkJb9Dih0O7a4Rr6qg6OC_n1hAdAR9ik3qf_9W7wF11CzKMd3IidCqQxs5jIo4AGxfF2aLkJAvbnP-qo1qF7chyjlCqoN51illNWjhWNJKypGnkxYpgCAcP_n7vLdUOCipfzlSpk725tJ7zgg8Fvua7bZZ4iCmuQOMjO6pPHIPKzmb0GF0B8744voLcm6ogxQH8MqlMaelIRvn7fb32ba67603YjheA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:
سعر الفائدة مرتفع للغاية ولا يعكس حقيقة الوضع الاقتصادي.
نحن في آخر مراحل الحرب مع إيران.
‏قد نفرض تعريفات جمركية باهظة على أوروبا إذا اعتبرنا منح كندا صفة دولة مراقبة عملاً عدائياً.
إيران تريد بشدة التوصل إلى اتفاق.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/90743" target="_blank">📅 01:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90742">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6309a31e7c.mp4?token=iB9WhMtWiL5J07Ts15aionHe7bOA487NHg0x6p3HF1ds4I1qWEEG7NYI0msiOVcoYW8hjpk3F8Goy8-H-x81J_qyo8-Bl7p8fdpi-NbYsBEGEYlQyUetsz_Zhx6nEMsmtz6n7gmuSVvqcdmQrlhaW00qmzR1YG3libp-z3mA1zPHjZ3ZmFOvE8eo-NkL_3-P0k1j7DHs0pSG1-03gickDkx9xKXknwJdmXF9QtvHGRmcHb7Lmyk8s5Cyn9HW9IZbKYQnOiHBIq8xr1bhd6WTlyA4SrWj9m5Kjh22bU_tAbPYH3tCE9odhRhQ1k1qndcYejfjlvfCS3NkVBLPYws6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6309a31e7c.mp4?token=iB9WhMtWiL5J07Ts15aionHe7bOA487NHg0x6p3HF1ds4I1qWEEG7NYI0msiOVcoYW8hjpk3F8Goy8-H-x81J_qyo8-Bl7p8fdpi-NbYsBEGEYlQyUetsz_Zhx6nEMsmtz6n7gmuSVvqcdmQrlhaW00qmzR1YG3libp-z3mA1zPHjZ3ZmFOvE8eo-NkL_3-P0k1j7DHs0pSG1-03gickDkx9xKXknwJdmXF9QtvHGRmcHb7Lmyk8s5Cyn9HW9IZbKYQnOiHBIq8xr1bhd6WTlyA4SrWj9m5Kjh22bU_tAbPYH3tCE9odhRhQ1k1qndcYejfjlvfCS3NkVBLPYws6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إرتفاع أعمدة الدخان في شارع فلسطين بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/90742" target="_blank">📅 01:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90741">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3d57b4a1.mp4?token=jqE-1nXDTISJhQ_5IKR1N-tUSVmOWpAkOwAcyJJdbx9BIee5jFxgBXkO3yabmU7p0KYHceeL23-bDnwn1N-2Zh7unrFkNa3r5Pa2B8vl4HXvz3Y1Ye7C9GFTs35dFFJ1i_Ma3j7m_OAfOPZ1ZcFbUaDHEh4EPLSytKJNYRiefA0r9Q-H9jHF_S1OgfgCGbLeJtl7tCAbSo19fFtlDXISre3PVIkpasqv5sMzhXA-nOpKfPVJtU0cyR_VMDSDdNH8qg_O69luZj57-boExwv4lxo34jCmtjnHyfhlCikr2Jx1oIOYPzGY6Tdg2tZM-aBTmWpB5vAwj4KeKtdrpIPKPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3d57b4a1.mp4?token=jqE-1nXDTISJhQ_5IKR1N-tUSVmOWpAkOwAcyJJdbx9BIee5jFxgBXkO3yabmU7p0KYHceeL23-bDnwn1N-2Zh7unrFkNa3r5Pa2B8vl4HXvz3Y1Ye7C9GFTs35dFFJ1i_Ma3j7m_OAfOPZ1ZcFbUaDHEh4EPLSytKJNYRiefA0r9Q-H9jHF_S1OgfgCGbLeJtl7tCAbSo19fFtlDXISre3PVIkpasqv5sMzhXA-nOpKfPVJtU0cyR_VMDSDdNH8qg_O69luZj57-boExwv4lxo34jCmtjnHyfhlCikr2Jx1oIOYPzGY6Tdg2tZM-aBTmWpB5vAwj4KeKtdrpIPKPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إرتفاع أعمدة الدخان في شارع فلسطين بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/90741" target="_blank">📅 01:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90740">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4875422f.mp4?token=AZnA9b8i5ROQYq92lMZcciDSKH09oqm8etotgryJFHlJx7XFXH888xtHROPuY5aL_Y8KMxm24kwIaBLdCEQV8J09yfNT7VLolBxBVYAld05w3yi2sae-ZHyidlWTJW3eykdonsiBk2w5sFixjl0lnC0TPBBawvzr2I5kKrf2e5CeNam00ka-GqTQ058zLB3UtBCitsmd6jBEAUHNPPOndQOMB_vjMMDOPsYV0bKI6kB6awC2xh41eYlddpE6Yz9rA1Gs4ujWVF1Qkjlh6gGP9CVc1IrnGcYgwlxOOEPj7bgK8LLgrfTeA6lBIAbB-axhDTlpfzr6Pn9aOywbMqXifA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4875422f.mp4?token=AZnA9b8i5ROQYq92lMZcciDSKH09oqm8etotgryJFHlJx7XFXH888xtHROPuY5aL_Y8KMxm24kwIaBLdCEQV8J09yfNT7VLolBxBVYAld05w3yi2sae-ZHyidlWTJW3eykdonsiBk2w5sFixjl0lnC0TPBBawvzr2I5kKrf2e5CeNam00ka-GqTQ058zLB3UtBCitsmd6jBEAUHNPPOndQOMB_vjMMDOPsYV0bKI6kB6awC2xh41eYlddpE6Yz9rA1Gs4ujWVF1Qkjlh6gGP9CVc1IrnGcYgwlxOOEPj7bgK8LLgrfTeA6lBIAbB-axhDTlpfzr6Pn9aOywbMqXifA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تسريبات من زيارة بن سلمان لمصر ..</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/90740" target="_blank">📅 01:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90739">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇾🇪
🇸🇦
غارات من طيران العدو السعودي يستهدف مدينة المخا.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/90739" target="_blank">📅 01:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90738">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/711935c900.mp4?token=stAhjm_buvhfVrAr2ze-GSUvE-EhoImVuIckD1U401xkQ-5tFgBEk6FKNkHUU-aYyCN-lLZoEOL0k_QNsjT0_YRKyumZ3pjF_z7gCfKb9NOHlWgewXJLi4TlyLlrfSvz56b0hjP66qAI19If2IqxcKB2Qj48FCGMsMA7_5NGlomw1eUiAqIVQSP3JRJTGPSzRa-5fAilLNBrIktPW8_PPMNcISjBv0PjCQtQd3ox9mr_sgjvWTHb6yR2CMNJouq3PX9a5CfaqUr35ofAlzE-aPBVNg8XYByCd4ve0bIWVbrkpPO2btCIBkodrLnqISMC1JvUhQ4p4tydGG9oyiI5hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/711935c900.mp4?token=stAhjm_buvhfVrAr2ze-GSUvE-EhoImVuIckD1U401xkQ-5tFgBEk6FKNkHUU-aYyCN-lLZoEOL0k_QNsjT0_YRKyumZ3pjF_z7gCfKb9NOHlWgewXJLi4TlyLlrfSvz56b0hjP66qAI19If2IqxcKB2Qj48FCGMsMA7_5NGlomw1eUiAqIVQSP3JRJTGPSzRa-5fAilLNBrIktPW8_PPMNcISjBv0PjCQtQd3ox9mr_sgjvWTHb6yR2CMNJouq3PX9a5CfaqUr35ofAlzE-aPBVNg8XYByCd4ve0bIWVbrkpPO2btCIBkodrLnqISMC1JvUhQ4p4tydGG9oyiI5hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحليق طيران مسير مجهول العائدية في سماء محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/90738" target="_blank">📅 01:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90737">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
الشيخ د. الصادق الغرياني مفتي عام لليبيا: الحرب الجارية في اليمن حقيقتها هي حرب السعودية بالوكالة عن الأمريكان لا لدعم الشرعية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/90737" target="_blank">📅 01:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90736">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">▫️
‏قررت الجزائر إغلاق مجالها الجوي أمام جميع طائرات الإمارات طائرة مدنية وعسكرية مسجلة اعتبارًا من 11 سبتمبر.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/90736" target="_blank">📅 01:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90733">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ex2PJNZ4ZVR3OUndMpkRFBUuMJbcOfm57vJNTxQcv1jcIIiZ8Hi_smclE-URkCNdoilwbp7ELivjQVjUi913kaf8VaGH0M_DUPQR3kEdMTsMaJ8Gw9hfosFCYxghU4lF8w983uD-5g-xqNWDT1oS9ap2nzeCYffYUuWNGCUjZm5ZjWEejpedcEAr4i4-8aAZECrumwtFFdySMPPKr_0_Q9pNbauu6A9UMTYD6IkRw8i6bZAbbjzN1dD0m1kMYfLZ1RSKgvBOHLxE7Twkwaql4vnmkanXnt9r3MMQ4kfHFGqLFnNHPa6q1kWVHIwMj_hBizf9HRBb0jPrgBbZNoJvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tY84ctiojtVANtdgyoiJBQ-J-TF0jEodBKSx75dAfYdVdkb7-FyewB9q6yiuayPpnLcfCoi9meJ4tkGdJRw_jV-0_Eelpenvdkcw7J6zWKytpjfZlVOaXSd3k8ycG-S-nx_YabmAdf2QVUSnTyPKwzcXlJDiCda-1LsUWEapgrtCugPjVHLzkAqnrxjKJEC5mX1DdSAZJR8KZUyu7SPAumlVp44uls7oVzIoXKCZvKrCtQ1i9Z8CvNf_HNYNfX-2-Q9jWhRd8qH4nSqiRCFlO3KpQqIPe8aT_N_w4CaD73jYMHoagqx-n1MUEGLS4XdekSPEsiz6unq8tFx3Xh8jog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dX2XZUaQqmdMQETz8IBsvhq2-dyrCQ6sDfStDr-_Crb3gr0SrJrbr3BDKiv5LL4rt1MAHK0rKTZohvHOZi032eMl3mhc-ydddwtBZXRVLLNDOERot6NQHdL8XnIol2UvashPVRXiJPbmZ_aUKnzphYZekrDE1skjwXutqoPIMYpR1ATDTXYD0MSaXS5rAm_SHkHg35rBILDW1rx9vW0VB6pomyhyqY6aO0OfG4CFSABJxYt0_vaHWrD6ubyPAJqbhvajxSefZFD9Vp8PG_4gX_f8rED2CWbuJDJTRngG4-uWl9Rf-8AH8iDP62-wkvCyVDQBjd8m5eqt440A87vQDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏يُحرق ما يقارب 50 ميغاواط من الغاز في محطة ينبع حاليًا. وهذا أعلى مستوى له خلال الأيام العشرة الماضية، حتى أنه أعلى مما كان عليه الحال عند تعرض خط أنابيب الغاز للضرب.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90733" target="_blank">📅 00:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90732">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الديمقراطية
تدين اجتماع الوكالة الدولية للطاقة الذرية بشأن نزع السلاح النووي.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90732" target="_blank">📅 00:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90731">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
في الاجتماع، الذي قال أحد المصادر إنه عُقد يوم الأحد، أبلغ الحوثيون المسؤولين الأمريكيين أنهم لا ينوون مهاجمة السفن الأمريكية وأنهم ملتزمون بوقف إطلاق النار مع الولايات المتحدة لعام 2025، وفقًا لمصدرين.
قال أحد المصادر، وهو يمني، إن الجماعة المسلحة قالت أيضًا إنها لن تهاجم السفن التجارية، باستثناء تلك التابعة للمملكة العربية السعودية.
وبحسب مصدرين، كان الجانب الأمريكي ممثلاً بموظفين من السفارة</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90731" target="_blank">📅 00:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90730">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLSNM9aNgXYjskiYgNqiZLdH619ZUwTMFjEJDRkJUZWfON8j-q4blwfx6Bx-xHnWmPSaeZ2prcHV8a0F_8iznJnyOfNbnSijzGOS0tDL5vW043RhnJxeAyBtamekVlRdSERjbUIhB8k4WkrlcI5jghAeuRRnisbL_mApLjc475vOFD4EMTfWnoyjBbQRFcPH7eEnzs7H6Y0QXNW4DQrqYg3Izb2I9fAXotXHmalL6UdoV1x3dd9vZlQhwFPgzAEKnp7tZR3QOhIufeumuo8lkKMtXhJA6pGXeeeV7HTBRxQq6qUdzW_EoRpFjHX0Ql9k7fYzzSeVexbxs2jNBHfE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
أسعار صرف الدولار في إقليم كوردستان تصل إلى 158 ألف دينار مقابل كل 100 دولار.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90730" target="_blank">📅 23:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90729">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3882df1f.mp4?token=NtNhVfF5_mpGENx7GVkNPV_HwKDOlKSUfqPbeYNf88GgpVDbR1DEaN5io6vHAx9XHjg-W1CwKbhHCg-ypopnlwmNCxvlaMiIJU2H8y17_mMIMJUCwwgC7XYm2vO_83rUmWEnt9JW1Iklpcz5YxxrxnwbludfQC3RufJcblIs6by3MFlKHbG03rCHxT4XW8E3DrfUVNi3hqZOZeEkA1jRVttTz87H7BPLPvHD1jumFmt8LuXne69gKkzJ1pggPIogP4FM4GwNk5t4Pgc9z2SnqUMRuKDlXy-JTSoHEsRAxQQ9y9atsukT04kw2mTJgTg5QjIv5GETj59Fd-e3OML0pD4HBjVK2c_28MKiWQONxczqUQsU8Mwt2G-GZw7zUEXfGLAvgl5Wz4NXUGsxmv5kL7BpSid-3ycAfpjWBIi_n6PVKdoL9ingij1ZTR1Yhzm2gopl-IN49JJ3zUAZfNO5xT2ZQ2pkhXrWBiK_eN1G58G_Pn48TPW5P2QQ7UxvEJmW1V-XJtDy1HzYCKMTUHlO-J1QGLiNGnO2xOMwMszR7eBfEnQIRRBCdEOynFmxSJEnBsyb3STJYA9GRPtIGxhzw6DgBKqUwr1FtTIX8frpwdSNhnuAV7VsKkQ5i6x1A4oxZaCYlUCbH1qugfRPz7SqNYUPwEj133UH7fpiQ2hS9W0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3882df1f.mp4?token=NtNhVfF5_mpGENx7GVkNPV_HwKDOlKSUfqPbeYNf88GgpVDbR1DEaN5io6vHAx9XHjg-W1CwKbhHCg-ypopnlwmNCxvlaMiIJU2H8y17_mMIMJUCwwgC7XYm2vO_83rUmWEnt9JW1Iklpcz5YxxrxnwbludfQC3RufJcblIs6by3MFlKHbG03rCHxT4XW8E3DrfUVNi3hqZOZeEkA1jRVttTz87H7BPLPvHD1jumFmt8LuXne69gKkzJ1pggPIogP4FM4GwNk5t4Pgc9z2SnqUMRuKDlXy-JTSoHEsRAxQQ9y9atsukT04kw2mTJgTg5QjIv5GETj59Fd-e3OML0pD4HBjVK2c_28MKiWQONxczqUQsU8Mwt2G-GZw7zUEXfGLAvgl5Wz4NXUGsxmv5kL7BpSid-3ycAfpjWBIi_n6PVKdoL9ingij1ZTR1Yhzm2gopl-IN49JJ3zUAZfNO5xT2ZQ2pkhXrWBiK_eN1G58G_Pn48TPW5P2QQ7UxvEJmW1V-XJtDy1HzYCKMTUHlO-J1QGLiNGnO2xOMwMszR7eBfEnQIRRBCdEOynFmxSJEnBsyb3STJYA9GRPtIGxhzw6DgBKqUwr1FtTIX8frpwdSNhnuAV7VsKkQ5i6x1A4oxZaCYlUCbH1qugfRPz7SqNYUPwEj133UH7fpiQ2hS9W0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الشيخ د. الصادق الغرياني مفتي عام لليبيا
: الحرب الجارية في اليمن حقيقتها هي حرب السعودية بالوكالة عن الأمريكان لا لدعم الشرعية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90729" target="_blank">📅 23:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90728">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇱
اعلام الاجنبي:
إسرائيل تعلن الاتفاق مع المغرب على تبادل فتح السفارات</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90728" target="_blank">📅 23:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90727">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9396a1dffc.mp4?token=IjFUx8j9lzHMDUQM7wWIdZrH1FbF6bNo-D7sAERoSBq6xmwLfGizinG3lrkZBF0WU8SKvPwHcuwyiEmkdE3gEadtXdmPSoeQqeXT34CguilSEWzrjiFodKZkXilhn7DsTOUmjy9v6dqP_N_jTxSCavCgS7IKGXMJX20Cyeq-feRkEt3YKzaUDR8Sk5bE4sWponU5Q3jnqsmFE4-u4uutx_9lsFeJklpChK6MpfFnIf033TtjSqQLkx4vqVdCuRzBinUyhb-IVC88JORmW9xESTqombTassi66cqBTbhtTocV2JUGPCWZ3b3IV0-gKswx8Fe3Bb4Wid7f7kcrycDB5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9396a1dffc.mp4?token=IjFUx8j9lzHMDUQM7wWIdZrH1FbF6bNo-D7sAERoSBq6xmwLfGizinG3lrkZBF0WU8SKvPwHcuwyiEmkdE3gEadtXdmPSoeQqeXT34CguilSEWzrjiFodKZkXilhn7DsTOUmjy9v6dqP_N_jTxSCavCgS7IKGXMJX20Cyeq-feRkEt3YKzaUDR8Sk5bE4sWponU5Q3jnqsmFE4-u4uutx_9lsFeJklpChK6MpfFnIf033TtjSqQLkx4vqVdCuRzBinUyhb-IVC88JORmW9xESTqombTassi66cqBTbhtTocV2JUGPCWZ3b3IV0-gKswx8Fe3Bb4Wid7f7kcrycDB5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اندلاع حريق كبير في مستودع نفطي بمنطقة التون كوبري بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90727" target="_blank">📅 22:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90726">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb41645f5.mp4?token=GNbTt9kwWmRV3gPtOU6bvYVw--qLG3gQEdxuLJYD2h2Cko64bfRfJzuhZtb63xWtpdY_bvun_53H74h_4n2bWgkcqoIfZ2_gEPVUJYjcR1qr_eKCCtdXanEs_ggjGhPWmjgyj3g0uo_E3If9Rlydu-dBM7h2u42iX0qbF25W0pVnxVhHLSwvhQiJt7R2FVTaXGAvQmSqgHpWFd0Q4c3HI7SmJhcvEFPoVwlyhlw2Z2z0P0Riyf8I8Qz-tRbp4vN07FHsJvuJqXnlMww04LuJa83B3jgm9Uvvr-sK9u1hYyE22SmmxANQPHmek8TLkd2jeX9XnBzbfQa3vCEi9JiHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb41645f5.mp4?token=GNbTt9kwWmRV3gPtOU6bvYVw--qLG3gQEdxuLJYD2h2Cko64bfRfJzuhZtb63xWtpdY_bvun_53H74h_4n2bWgkcqoIfZ2_gEPVUJYjcR1qr_eKCCtdXanEs_ggjGhPWmjgyj3g0uo_E3If9Rlydu-dBM7h2u42iX0qbF25W0pVnxVhHLSwvhQiJt7R2FVTaXGAvQmSqgHpWFd0Q4c3HI7SmJhcvEFPoVwlyhlw2Z2z0P0Riyf8I8Qz-tRbp4vN07FHsJvuJqXnlMww04LuJa83B3jgm9Uvvr-sK9u1hYyE22SmmxANQPHmek8TLkd2jeX9XnBzbfQa3vCEi9JiHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اندلاع حريق كبير في مستودع نفطي بمنطقة التون كوبري بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90726" target="_blank">📅 22:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90724">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
الاحتلال الاسرائيلي يقصف ريف دمشق بعدة قذائف.
جيش الثورة الالوف الالوف
😆</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90724" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90723">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
🇮🇷
الولايات المتحدة تحقق في علاقة بين إيران وهجمات إلكترونية استهدفت ناقلات متجهة إلى ولاية تكساس.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90723" target="_blank">📅 21:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90722">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية
: ‏شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 40 غارة جوية بطائرات "F15" أقلعت من قاعدة خميس مشيط مستهدفاً محافظات تعز ومأرب وحجة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90722" target="_blank">📅 21:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90721">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
بعون الله وتوفيقه تمكنت القوات المسلحة اليمنية وعند الساعة 18:40  من اعتراض تشكيلين حربيين سعوديين نوع "F15" أقلعت من قاعدة خميس مشيط فوق أجواء المخا بمحافظة تعز بعدد من صواريخ أرض جو محلية الصنع وتم إجبارها على المغادرة فوراً قبل تنفيذ أى عمل عدائي بفضل الله.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90721" target="_blank">📅 20:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90720">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
🔻
وزارة الدفاع العراقية تنفي صدور برقية استخباراتية بشأن نية السعودية استهداف مقرات الحشد الشعبي.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90720" target="_blank">📅 20:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90719">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇵🇰
وزارة الخارجية الباكستانية:
في الوقت الذي كانت فيه البحرية الباكستانية تجري تمرينًا دوريًا، قامت سفينة هندية بتنفيذ مناورات عدوانية في منطقة قريبة.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90719" target="_blank">📅 20:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90717">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇾🇪
العضو في المكتب السياسي لانصار الله في اليمن:
ستواصل قواتنا المسلحة، بعون الله تعالی و تأییده استهداف القواعد العسكرية والمنشآت النفطية والحيوية داخل مملكة آل سعود، حتى لو وضعت في كل منشأة منها مجسمات للكعبة المشرفة.
فنحن اليمانيين، أهل الإيمان والحكمة، وأحفاد الأنصار، وحماة المقدسات، أحرص على الحرمين الشريفين من عبيد جيفري إبستين و ترامب ونتنياهو.
و تهدف عمليات قواتنا المسلحة إلى رفع الحصار عن شعبنا اليمني المسلم، وإنهاء العدوان على بلدنا، ولن تثنينا محاولات التضليل أو التذرع زورا بحماية المقدسات عن مواصلة موقفنا المعلن.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90717" target="_blank">📅 20:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90716">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزارة الخارجية النرويجية تصرح بخصوص قرار داخلي عراقي:
ندعم قرار دمج وحدات حماية سنجار ضمن القوات الحكومية العراقية.
بعد النرويج الحزب التركي حزب العدالة والتنمية:
اندماج قوات "مقاومة" سنجار الإيزيدية تحت سلطة الحكومة العراقية أمر بالغ الأهمية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90716" target="_blank">📅 19:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90715">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
🇸🇦
الاعلام الاميركي:
السعودية تسعى لإعادة نحو نصف سعة خط "شرق غرب" خلال أيام.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90715" target="_blank">📅 19:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90714">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPtj3WOKlmXzc2wT-MjqjZqTecVzH3Ow6Quq4t2j_63hsU1IOxU2oYxzH6b0GVne3z8WQShKFA84ytYb2YlNBkdq8hCVanH50zTurFd16QRxEywJ58UYksy2ianmr4vzngOa6Z4MWdBsDea8Oi3gV_Gk3xKSSgrIwFqRhyr9-RHKctWkdNjwZtdezkEwHxreFp7sznDKXG-V7uJbjdjwNyhNHErTw-o4hJI8Lj19K5ZqLi50spy0ARfQubSlZDXakRmzlwAIMa5TQhqlLY7KNgjNWgaIBRwVXr-I6QWjAre9vffTYJgdJZCTmMy6z63F8R50wO9n8dJHLA36P6rUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد نوعية لإسقاط طائرة مقاتلة سعودية من نوع F-15 وحطامها في أجواء محافظة مأرب بصاروخ أرض-جو محلي الصنع</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90714" target="_blank">📅 18:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📰
رويترز:
تضرر محطتي ضخ على "خط أنابيب النفط شرق-غرب" في السعودية من جراء هجوم الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90713" target="_blank">📅 18:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WD_j85_j9ty9ORQJ39tD2jXdH5NhEt6kf2warHeaooJProIehlNsxl9CB1VrRzhVmjoXU_gRLHZtI0DSJQN_WsLsYIjJLO_3iKDCaZNJ_Ubb-Ja1y92pb6tTa6bMB0GdbcuRvbwQSG9Z0hH34rxTCy9puJeP3Q6ehqX7xQEkiQProK4uHv33bRveGjJ2soZDfebvOvot9sf4fVPn_SYz7XgmvsDWjt-51Sf6DVA4jMU_1q8E7zDA1BQchCkI8-hyxSgNULmbLxUe8PElkkcjC-SJl_UxVLAWGYFn-9SNbJvekP8lfFMY-lyIgHZ4G5ZUnjV8REhci3GrIhhHBhbh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد باقر قاليباف:
لا يمكن لرفع أسعار الفائدة فتح مضيق هرمز، ومخاطر المضيق تنعكس على علاوة المخاطر وأسعار النفط.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90712" target="_blank">📅 18:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUjiONE5mCb5NjTdK_wsbRthM1z5qAs7PzZ_ViLaGzUHeRz1hqngDIY1zWBArau0FeZPeGd5u60R1jSLuyR1-uybPdiP0OtdGuFolksoHF5HsKqhMbuxBRtAnoaSL8YRiaKA2KXyMzGm63F93-ZI1IbKFJeMbjAzpX1C-TrX7cKbHpS0yZfl6NuUMrT9y-tk9dbS3qUziwHauk6wFSOK8LPbBMoi7mMqNCiEyqoPouT__3rgGaKRZb6qnsR5xwdjF0fJhLF8I2eoixphW-oR4GWm-AWuKNJHEJq2J4LP7hTLhZ7k_JvanZGT_CyWI3DAqZsDUit3cx75pF6etGrlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس اركان عصابات الجولاني يلتقي قادة بالجيش الروسي في مطار حميميم باللاذقية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90711" target="_blank">📅 18:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90710">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏
🇷🇺
🇮🇷
🇺🇸
🇸🇦
تقرير اعلام أمريكي : تم التحليق فوق قاعدة عسكرية أمريكية في السعودية من قبل 14 قمرًا صناعيًا روسيًا تجسسية قبل يومين من الهجوم المدمر الإيراني عليها. التوقيت وتسلسل المركبات الفضائية فتح الوصول إلى طيف واسع من البيانات. هذه البيانات، وفقًا للمصادر، ساعدت إيران في تنفيذ بعض هجماتها الأكثر دقة ضد الأصول الأمريكية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90710" target="_blank">📅 18:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90709">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
🇮🇷
هيئة المنافذ الحدودية العراقية:
سيتم إعادة فتح منفذ الشيب الحدودي مع الجمهورية الاسلامية يوم غداً الخميس.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90709" target="_blank">📅 18:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90708">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1543a6daad.mp4?token=V7eJSwyk9358wUqBgMGjqWfd-OChEvuoL7bO25qXkErjIOC6s_tyR-xZH6nmZmk9PSjL5CCJvGAAS7CbNZhZzBWlbJv_yCaB-BhHNbMf9zkbdNagqOjuugQgvik35OJNCE9VEMO2l90ij_IjBILXJtvbRsNyxE7j6u9oQsLPgO0SGPc9dtmj5u1CewKMlz7ofNcY7mXLs6BZmS3IMJfiWJt7nw_Qk9amZR443QYqCibcvervrH3CIUcU9wgSErCmT6ZPpxlwUtg2fmpFQq_GDBbRyUq929PZBwO00DM3BnlzkqlFc2nQ2ZU3q_EuYbR8Bc5ceVQJrUlhLzW1YdHf9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1543a6daad.mp4?token=V7eJSwyk9358wUqBgMGjqWfd-OChEvuoL7bO25qXkErjIOC6s_tyR-xZH6nmZmk9PSjL5CCJvGAAS7CbNZhZzBWlbJv_yCaB-BhHNbMf9zkbdNagqOjuugQgvik35OJNCE9VEMO2l90ij_IjBILXJtvbRsNyxE7j6u9oQsLPgO0SGPc9dtmj5u1CewKMlz7ofNcY7mXLs6BZmS3IMJfiWJt7nw_Qk9amZR443QYqCibcvervrH3CIUcU9wgSErCmT6ZPpxlwUtg2fmpFQq_GDBbRyUq929PZBwO00DM3BnlzkqlFc2nQ2ZU3q_EuYbR8Bc5ceVQJrUlhLzW1YdHf9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇮🇶
‏اقليم كردستان العراق يطلق سراح صهيوني محكوم بالاعدام لارتكابه جريمة قتل على الاراضي العراقية بعد تخفيف الحكم ثم العفو عنه وهو الان يتجه الى الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90708" target="_blank">📅 18:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90707">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇶
هيئة النزاهة العراقية تسترد من الإمارات مداناً هارباً بأربعة أحكام لاختلاسه أكثر من مليار دينار.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90707" target="_blank">📅 18:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90706">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇱
🇮🇶
‏اقليم كردستان العراق يطلق سراح صهيوني محكوم بالاعدام لارتكابه جريمة قتل على الاراضي العراقية بعد تخفيف الحكم ثم العفو عنه وهو الان يتجه الى الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90706" target="_blank">📅 18:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90705">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
بعون الله وتوفيقه تمكنت القوات المسلحة اليمنية قبل قليل من إسقاط طائرة استطلاع مسلح نوع "وينق لونق2" تابعة للعدو السعودي المجرم أثناء قيامها بأعمال عدائية في أجواء محافظة مأرب وذلك بسلاح مناسب.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90705" target="_blank">📅 17:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90698">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcllF_hkBO2qeKz3tz5c_WpWE_jGNUgJ6ehEkcq1XGd2aow4uWogte-tL5E7FzYYYxGO0IXqjKWLDO1yk_5IE0Qs1sDXd5czJ9pU9rAS46hps-Y2bFKIIk-ZygFFhdmfzWsv8VuIGpxK4kvOM8zZ9PY3fhaypbYmGEepBxqelV7YTX1cjSh89QFiHMlXgKsoxNop7PkDQMYLJVUGs6Oum4pogavuIUNoKe9dIG0kko78ktEwyFDQTfMDcwZJ9q3Roz1_v1ce4QjH4Uk2s5lGRAKLTMNesV00GbbMfDcph-xXAYEZG9ggIv7MlDjM5BLDknRfw3HKgLMd4XzzJhkgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBOalZICIxSyfB9F5nVgc68KxF3YV35Cgl57CvoK8Kf87fh7Ib2l_THtYZtAW_iGqO5Qlc85s8XewK7-BUNjlJLPpPaBsd5x8KyzWCP1oHfvxcRqct1tgc4wT5Hbbm1vo2KDBsT9M2EqXkl1gt2zM-ROCCi4-kZVI1NIm0c1vcXZFNu1gEfBY39vAXl16x2mK1_TzVMYzJ_j_XgQKPSPHwjhNuY_dxA6jenwCVBogef8Zfc3DCGwmUPEFaEwzrYpXOfQ8AHnYVoSX2ziPls-6wi4ZxkEzhWzOIBTNBfoFbtyMZ_-oNvh0cFBQiKmNmtgKvBTXVy1W7ftxy__C1yggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8QFtq7SLKTwu8MoVZXUQLueqk0wgfXxbqk5wkcnFh2zE9edPMeHQrHRaV8eE4pOmiG7tM1z4ZO1zrx46LWEsZz64bCe1HaxIT0zkuo-3ij_vj_VOLUqeiezUBekUkJITv8UYI_vQ-VtIqSmL7Pd1q7cIrdSajrEhyqS6I-ZyfZZONmmSfLo8S6BcFSktAVYN6fnZfskWa6kd9XMavDdLHAXx1bg93kjbNIPR7cZiOdJraBBW5CE643PwAu0Xz9X8f1sa8bCQtw4-58E-XeYqDyfPYG233XB9y_ToEZ7nokE-uECL6SWhx50uiSKnIz-ZvCxOeE9o-jms2wwOcZ6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4QVc3t7bnRlcZHJWzWghjcn7ios3pS9RCkQrZX3lEPNVylhqtOv30TDW7V9FhUlwr1-VeYLihiB1DjOO7bC9nmYE2aCnT-FSI3TramIbnfyQk0WZYbJrnrOsMGm8NOmzJGyJQE6SrKnKxEtnbDO_rrQiUZJagjHQM6zZxXqQbxVCOi9cFIzjtfowqx2vrFRi9vjAAxcUZNVQRoZCuju7Vzo1eUuxwPhqtgJIG6wbClFVmLTSWSnsnBxB9yVaY6-O1ghjwjbxeBsT1GAdXuksXwI1-zzxmRPrzbT7fIrIJyGhuGUFKS_twLERPO-LG8_T4wIau8kf_l-70OBrxZW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSLhEitiAwVTFopa4ov3g8rFNzsY2iSIVcEkobnnhbztGLxoPlkZww17K6eGssnRVZaHsDQmRF7EqQnyqq-xZA2wZXYgF5q-94QPlE69g7Ddy6yAf6PCKf3GVe23HKNJTF15L3BV7sDkL06tgAPrKqo7ml7_zj1Trl7Rfy0OmbaQjU8czkonhjiN0HGihPcIt_cMj_DWNTNz80q9xgt1ux9ykYMiXldx-PAaE2eRGWP9x8HA2OdiXR6IRioKCI2soZJuMQKa3eTeKHGTUv7_x5Dhx1553lFHKL-o7YdT8ok_9VCWdxytL1pvrUI0eHH32OYLMrw6B2mEdEabMJCLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmIL0Kfp-6OZp7Hqa2fH1LxtJi8VzuehZ4ajubjs6KRiF25nTAT05V5Byj-i_NP5haFPwINuzP0j7LMiZi2nJ1gzqLJT3xWfIR0hLwyBAv2HxzKGmdvddWV-qKdGN5mNd75OTxurXSA7zyTnUTcvEJjmVnY3VBBEDSW24Qocand9PLG3y6n30G5ieY0smb06LtOJy309ytbEfsTdElg81WsG9NmfQlrDf5QjZGpSAqqX3SnF5XRNi82JChaXvdwYV5LvoO8Ta8QXsZG3Ay8dwvXsA0Pt8LG5P5o_Ogknc73ubW7jDTjq2y5J10-r_aOAnXp-R0qLJjhAF11z_g5cjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9yQ5lVSjX5Rc3QSavRgZ1aVZizXfTcG462oWfDbEfnH6Ba9zsw28qg9JQvrTkwBC9OhWaynOx5nDvWIoqdfqZv48yn4YjiQNuDCKzTyF4JEB99CEzplkX3nttHvz18cU9_qs20ZgsTTW_xurF4v_rVtceidzthva0FDCN3r603lKTRX81jdFr-jpatATBMX_-dAXNB9AuoLwzAB0Wxa165n9p6ndNrdXX1F8OGIY_-0TGLEpP8cKzVXrTFVctGLJE_-FF5Ym3hoLL9fA3gFFcu30628i5r2MjJp85QMo4RL2TJsQl1OZm-BLjKtmc6ahiDTAXcJQrwI_E-ymJh5Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد نوعية لإسقاط طائرة مقاتلة سعودية من نوع F15 وحطامها في محافظة مأرب</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90698" target="_blank">📅 17:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90697">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90697" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/90697" target="_blank">📅 17:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90696">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مشاهد نوعية لإسقاط طائرة مقاتلة سعودية من نوع F-15 وحطامها في أجواء محافظة مأرب بصاروخ أرض-جو محلي الصنع</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90696" target="_blank">📅 17:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90695">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ef2a83f8.mp4?token=MSXReAIAWqXqctkzViRKpA-uKhee3tR0ULUChlScpkDauK32-vP-b9-_kXj6-lMGYiG1nksYkxcwzvUXw47k-QBqLGBJILlhlX36m0FIPQI60roEAljZWmFUtkBTZFTnme-7kr6ai9P_A8A2I7qY_K03cSYhb8rHrdvmMWPUJWJAO8Z2Q8oyq9CB4VZhYnsG7FZBZgvHiFXQN2SzBLdnGE2wsxaWV7AMrQ5Vg4bxE7bGeJY5wX5qLIQ9mjVpjPoqdKQc4Aq_LT2pjhjxQaTYt9HCWRClJ5btN8jlDYn0d0rKcB4f3OjOVpp30RtvG2ZUnonxKthbvahy10Pf-UrMcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ef2a83f8.mp4?token=MSXReAIAWqXqctkzViRKpA-uKhee3tR0ULUChlScpkDauK32-vP-b9-_kXj6-lMGYiG1nksYkxcwzvUXw47k-QBqLGBJILlhlX36m0FIPQI60roEAljZWmFUtkBTZFTnme-7kr6ai9P_A8A2I7qY_K03cSYhb8rHrdvmMWPUJWJAO8Z2Q8oyq9CB4VZhYnsG7FZBZgvHiFXQN2SzBLdnGE2wsxaWV7AMrQ5Vg4bxE7bGeJY5wX5qLIQ9mjVpjPoqdKQc4Aq_LT2pjhjxQaTYt9HCWRClJ5btN8jlDYn0d0rKcB4f3OjOVpp30RtvG2ZUnonxKthbvahy10Pf-UrMcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏التلفزيون السعودي يبث مشاهد للملك سلمان وهو يتقلد سيفه ورمحه لرفع المعنويات واعلان الجهوزية وارسال رسالة ردع للحوثيين</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90695" target="_blank">📅 17:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90694">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رشقة صاروخية باتجاه سفن مخالفة في مضيق هرمز</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90694" target="_blank">📅 17:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90693">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇩🇯
وزير خارجية جيبوتي:
لم نسجل حتى الآن أي اضطراب في باب المندب والملاحة مستمرة بشكل طبيعي.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90693" target="_blank">📅 17:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90692">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ebbea9b7.mp4?token=t7uQUSL2HEyCmOke8VsdNpBgSY0gaRVbyJMHGG5UO542tGUHBjVJQsdwBbmQjQGulA_pdvIk-TaN8btilvMAzlSltsSUDULF3jta41HamZRmh3LPT91nQ7EvrgwD_ct2li_NFyZgQk-nNeuerzBCWPfVdiyrlzd3epXi86Zy-rSfKBzAgXRlyda04K3qRKKmVogLAgzSu4fI7XEIMEMSD_ThjMUY0QugHTuXgA4Qfw5Q__kiY9kvVUkYIK8_tLCC9owODYCrbjiRbMTiBP0hUPDDhxIc8UzIPTbretT75eMNd7ND_BjmJDVlb1Ht-Jo_ChsuS-d3l4d4KHo7lJv_1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ebbea9b7.mp4?token=t7uQUSL2HEyCmOke8VsdNpBgSY0gaRVbyJMHGG5UO542tGUHBjVJQsdwBbmQjQGulA_pdvIk-TaN8btilvMAzlSltsSUDULF3jta41HamZRmh3LPT91nQ7EvrgwD_ct2li_NFyZgQk-nNeuerzBCWPfVdiyrlzd3epXi86Zy-rSfKBzAgXRlyda04K3qRKKmVogLAgzSu4fI7XEIMEMSD_ThjMUY0QugHTuXgA4Qfw5Q__kiY9kvVUkYIK8_tLCC9owODYCrbjiRbMTiBP0hUPDDhxIc8UzIPTbretT75eMNd7ND_BjmJDVlb1Ht-Jo_ChsuS-d3l4d4KHo7lJv_1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحيفة يديعوت أحرونوت العبرية - رون بن يشاي: أظهر الحوثيون في الأسابيع الأخيرة قدرةً مذهلةً على نقل قواتهم مسافة 2500 كيلومتر جنوبًا على طول ساحل البحر الأحمر، والسيطرة على مدينة المخا، والسيطرة على مضيق باب المندب وجزره. وقد مُني الطرف الأخر، الذي حاول الدفاع…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/90692" target="_blank">📅 17:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90691">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWYn4mSKbE7HD_bCqbf2iSTYseaeqKc6HxZmkdurMpstF1rOy9hGNkLPRa57Ix5KKbIgOy2gLyWAEnd0lAm2nAbe_um5eQzmvoKzYKtb_TG1mXCwDytic6krsjqI7ZwE-VZH78kBTRHczgUMvK21X9_rDtVm_pslLdQyAzowEVqCbfKLi_g-Y7GDWahRtvYyaIW1s_0ZHalcOhdKzeBxG1p3n2YhmZX52F-Co9N8CDjVdP2hKAQjW_J7NrXSTnSYrfHRW52lOtfG7OJ5spBU5JWQy1OrVSblWDCN3MU4C_0S4KKDVrM0ucKByXRmhGzfYMfgqQewVbKPsAzVyKTpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏يُحرق ما يقارب 50 ميغاواط من الغاز في محطة ينبع حاليًا. وهذا أعلى مستوى له خلال الأيام العشرة الماضية، حتى أنه أعلى مما كان عليه الحال عند تعرض خط أنابيب الغاز للضرب.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90691" target="_blank">📅 17:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90690">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مواطن مصري يسخر من كذبة ال سعود باستهداف مكة: إن كنت كذوبا فلا تكن جهولا.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90690" target="_blank">📅 17:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90689">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صحيفة يديعوت أحرونوت العبرية - رون بن يشاي:
أظهر الحوثيون في الأسابيع الأخيرة قدرةً مذهلةً على نقل قواتهم مسافة 2500 كيلومتر جنوبًا على طول ساحل البحر الأحمر، والسيطرة على مدينة المخا، والسيطرة على مضيق باب المندب وجزره. وقد مُني الطرف الأخر، الذي حاول الدفاع عن المناطق الخاضعة لسيطرته على طول ساحل البحر الأحمر وداخل اليمن، بهزيمة ساحقة، على الرغم من امتلاكه سلاح جو وقوات مجهزة بأحدث الأسلحة والمركبات المدرعة التي زودتها بها المملكة العربية السعودية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90689" target="_blank">📅 17:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90688">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Homayoun Shajarian - Iran e Man (همایون شجریان و سهراب پورناظری…</div>
  <div class="tg-doc-extra">Melodifa</div>
</div>
<a href="https://t.me/naya_foriraq/90688" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">السلام على ايران وشعب ايران المقاوم
#شاركها</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90688" target="_blank">📅 16:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90687">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فوكس نيوز : سفينة امريكية أُصيبت خلال هجوم إيراني في وقت سابق من هذا الأسبوع.
الحادث وقع قرب مضيق هرمز، وشارك فيه أربع طائرات مسيّرة إيرانية وصاروخ واحد على الأقل. وأصاب أحد المقذوفات السفينة، ما أدى إلى إصابات ويتلقى المصابون العلاج في إحدى دول الخليج، وكان على متن السفينة عدد من الأفراد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90687" target="_blank">📅 16:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90686">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90686" target="_blank">📅 16:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90685">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQb5cWsqFX75hYNZUrQ8PdcGkiHakpMd2TdE_NBfNDK5uH09Zv-8Xn5e9nzfWkc-mztv86ys8q8WO1_zI_qS2vQMhNIOQcQYCLpkLE7JfdBsCq3-oqzMhJGPHmnunBgglrK1DCGQD9QzKLgi0fXRe13nPni8dyKofrd7ZJ4Fs0Kt9KmsfKoJeXXVJwd7zSGZORuSmkP8cac9_d1WTyOvWfxh7OuU8C9vBJ6yNgy9t3Ff8utgSyLfXJlHerhv7MD0Y3-0ft1SQYRPK22MNvcoevDAABJkk_JR4r61XwSXab0lBiEMEY_wRo6coxEJUjhWVcMmyddvZqx1s9jkHaLUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صورة مؤلمة لجيفري ابستين وهو يقف فوق كسوة الكعبة بعد ان وصلته كهدية ليمارس رذيلته فوقها.
هذه الكسوة كانت تغطي الكعبة المشرفة وحلم لكل مسلم في الارض، الا انها وبفضل ال سعود وصلت لجزيرة ابستين.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90685" target="_blank">📅 16:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90684">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قوة خاصة تابعة لليكتي تداهم قصر برهم صالح رئيس جمهورية العراق السابق في محافظة اربيل على طريق كويه وتسيطر عليه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90684" target="_blank">📅 16:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90683">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb74a6e1d0.mp4?token=hiqkF96Bkcn_jDV0Lns9_ZbqWT3oEIkLdkRDREE2VfNrLQtHGkdZNlJ3-cNYVWeOFvkz2qLYoHky1BdaTq1SsduhH02sHf7lzaVM9naOs-5QWofuOD8sP23aDGB93jWLzipMaIwDpaWc7mD0Zc3HT9l-57UWmCjmMYWUxw9F10fAvHIwTx6oLl4m7rSk_s2Ap5ADVwYXWSu2vA5NsFAq4NMGZLBWwK5s3-wfs7-wVGyBiUAZMNthRciNy-sRG7xrxtq1B2x-LlD4spCxw5X1uq9RJquMJfoEeROerJb3i2XRFZJhZ59V_8mfUFyuyG2WLjsc53gvafkFfAuCZv9ZCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb74a6e1d0.mp4?token=hiqkF96Bkcn_jDV0Lns9_ZbqWT3oEIkLdkRDREE2VfNrLQtHGkdZNlJ3-cNYVWeOFvkz2qLYoHky1BdaTq1SsduhH02sHf7lzaVM9naOs-5QWofuOD8sP23aDGB93jWLzipMaIwDpaWc7mD0Zc3HT9l-57UWmCjmMYWUxw9F10fAvHIwTx6oLl4m7rSk_s2Ap5ADVwYXWSu2vA5NsFAq4NMGZLBWwK5s3-wfs7-wVGyBiUAZMNthRciNy-sRG7xrxtq1B2x-LlD4spCxw5X1uq9RJquMJfoEeROerJb3i2XRFZJhZ59V_8mfUFyuyG2WLjsc53gvafkFfAuCZv9ZCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الاقمار الصناعية تظهر موقع اصطدام محتمل في منشأة عسكرية بالقرب من قاعدة الملك خالد الجوية التابعة للقوات الجوية الملكية السعودية. وتظهر آثار احتراق خفيفة، يُحتمل أن تكون ناجمة عن حطام صواريخ أطلقها انصار الله.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90683" target="_blank">📅 16:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90682">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">القوات المسلحة اليمنية:
ترقبوا مشاهد نوعية لإسقاط طائرة مقاتلة سعودية من نوع F15 وحطامها في محافظة مأرب</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90682" target="_blank">📅 16:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90681">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇾🇪
🇾🇪
بيان للقوات المسلحة اليمنية:  بسمِ اللهِ الرحمنِ الرحيمِ قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ} صدقَ اللهُ العظيمُ  يواصلُ العدوُّ السعوديُّ المجرمُ عدوانَـهُ الظالمَ وحصارَـهُ الغاشمَ على بلدِنا…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90681" target="_blank">📅 16:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90680">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlPSwZAK3hpZbIcs9jaVlu4jXFwSJiR_3WP9IBVWsGTnWk4AaY8MCrqTEyRcTg8RiQSaxFXVmT1qx6Ksa8pQZvrT4nGY7xkiYjvwWuVJLZKPcreTAqRP9Il9EKAGiVPj1_8xUea6os8fIofAwEwR744h4skU0_LJAi8rZlLdUEde5unsu9NaZHLK7lYylJ9ucd1IftcTJ1p_sRnONOtT-875KyDN6_OzaCZTH8bRjS507922Rwnw323spnJ7oGoMJ5UJ6q2r-K22vYn7yqAp-fbrrWnUdRI0PXygFuZBYDEi56psbILwjBdzKibz9Y3zwrw3e0Fa5YTqvyLvy-wuKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
في اول تعليق سعودي عن سقوط ال F15
‏وزارة الدفاع السعودية: طائرة الـF-15 التي اسقطها الحوثيين كانت تنقل حجاج لبيت الله الحرام ..</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90680" target="_blank">📅 16:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90679">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
🇮🇶
على الرغم من عدم اصدار العراق بيان..
اقليم كردستان يخالف الدستور العراقي ويصدر بيان يدين فيه المحاولة المزعومة لاستهداف مكة المكرمة ويدعو المجتمع الدولي إلى "موقف حازم وإدانة صريحة"</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90679" target="_blank">📅 15:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90678">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇶
كتلة بدر النيابية العراقية تفتح النار على الحلبوسي
بدر النيابية نحن مع لفتح كل الملفات بما فيها ملف وزارة النقل ونطالب القضاء المحترم بفتح ملف نور زهير بشكل كامل وبيان المتهمين ومن يقف وراء مدير عام الضرائب الذي حصلت على يده الصفقة وحسب علمنا أن كل المدراء العامين آنذاك كانوا ينتمون إلى تقدم.
ونطالب دولة رئيس الوزراء المحترم بفتح كل ملفات الفساد في وزارة الصناعة ووزارة التخطيط بالإضافة إلى مبالغ المكوّن التي قيمتها أكثر من قيمة المشروع بكثير، وكذلك صندوق الإعمار في المناطق المحررة والمشاريع الوهمية فيه.
وكذلك فتح ملف مصافي النفط وتورط حزب تقدم فيها، من أجل إعادة المبالغ المهدورة والتي تُقدّر بعشرات الترليونات من الدنانير.
السيدة النائبة مجرد للتذكير أن موضوع علاء سمير الذي حُكم عليه بقضايا فساد في مشاريع وهمية في وزارة الكهرباء قد تتجاوز مبالغها عدة ترليونات وهو من تنظيمات تقدم ليس خافيًا عنكم.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90678" target="_blank">📅 15:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90677">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
الخارجية السعودية:
ندعو المجتمع الدولي لإدانة اعتداءات الحوثي واتخاذ موقف حازم ضدها.
كفى توسلا.. اخرجوا من اليمن وانهوا حصاركم. لا امان لكم واليمن محاصر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90677" target="_blank">📅 15:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90676">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
مناشدات عبر بوت نايا
المملكة العربية السعودية في هذه الايام غير امنة
لذا نطالب الحكومة العراقية بأن تعييد تقييم مخاطر مشاركة بعثة المنتخب الوطني في بطولة كأس الخليج .
وقت البطولة غير مناسب اصلا ويجب تأجيلها من اجل سلامة المنتخبات الخليجية العزيزة ..</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90676" target="_blank">📅 15:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90675">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇾🇪
🇾🇪
بيان للقوات المسلحة اليمنية:
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ} صدقَ اللهُ العظيمُ
يواصلُ العدوُّ السعوديُّ المجرمُ عدوانَـهُ الظالمَ وحصارَـهُ الغاشمَ على بلدِنا وشعبِنا منذُ اثْنَيْ عشرَ عامًا، وصعَّدَ مِنْ عدوانِـهِ خلالَ هذا الأسبوعِ بشنِّـهِ لأكثرَ مِنْ 450 غارةً جويةً مستهدفًا بها معظمَ المحافظاتِ اليمنيةِ.
ورَدًّا على هذا العدوانِ الغاشمِ على بلدِنا وشعبِنا نفَّذَتِ القواتُ المسلحةُ اليمنيةُ بعونِ اللهِ تعالى عمليتَيْنِ عسكريتَيْنِ نوعيتَيْنِ:
الأولى: استهدَفَتْ شركةَ أرامكو في ينبُعَ بعشراتِ الصواريخِ الباليستيةِ والطائراتِ المسَيَّرةِ وكانتِ الإصاباتُ دقيقةً ومباشرةً بفضلِ اللهِ وتسبَّبَتْ في حرائقَ كبيرةٍ ودمارٍ واسعٍ.
الأخرى: استهدَفَتْ قاعدةَ خميسِ مشيطٍ الجويةَ بعددٍ مِنَ الصواريخِ الباليستيةِ وكانتِ الإصابةُ دقيقةً بفضلِ اللهِ.
إنَّ القواتِ المسلحةَ اليمنيةَ ستواصلُ الدفاعَ عنْ بلدِنا وشعبِنا وستُلَقِّنُ العدوَّ السعوديَّ المجرمَ دروسًا لَنْ ينْسَاها، مستعينةً في ذلكَ باللهِ عزَّ وجلَّ ومتوكلةً عليهِ، نِعْمَ المولى ونِعْمَ النصيرُ.
مستمرونَ في عملياتِنا العسكريةِ باتجاهِ العمقِ السعوديِّ، وفي استهدافِ التحشيداتِ السعوديةِ، وتثبيتِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ حتى وقْفِ العدوانِ وإنهَاءِ الحصارِ عنْ بلدِنا العزيزِ.
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 5 ربيع الثاني 1448هـ
الموافقُ 16 سبتمبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90675" target="_blank">📅 15:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90674">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
تعرض ارهابي على نقطة تابعة للجيش العراقي في محافظة كركوك شمالي العراق</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90674" target="_blank">📅 15:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90673">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هيئة النزاهة العراقية: السجن سبع سنوات بحقّ النائب (بهاء النوري) عن جريمة الكسب غير المشروع ، بلغ حجم التضخم في أموال المدان (5.8) مليارات دينار و(10.9) ملايين دولار وتم إلزام المُدان بردّ أكثر من (40) مليار دينار قيمة الكسب غير المشروع والغرامة التي تعادلها</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90673" target="_blank">📅 14:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90672">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📰
‏رويترز تزعم: مسؤولون أميركيون عقدوا اجتماعًا مع الحوثيين في سلطنة عمان مطلع الأسبوع.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90672" target="_blank">📅 14:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90671">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txN_Ckg9spujWr1foTQAi50roIC3yUPUKOFfTvh86whi_S5-D9JdiHfcbbsj3iRjjMHa4dqga9QOq7vkxzQAgIiD_AY-4zljniB201P6dt84-HReRNkmie3ItQIvoSrpwU-MmesK1KjHrAMi5mT4FfGo1wu8xs0fesZclk4WM3wPNufNGUEp2IMLUiwQPAB-oangplfGJMXawHtAbPE2alYiKmanyy-bB3OKWIUfJQrnWJyRw81NTP2sEIQg68c_V6MOgmznm1ej_mZQK1skgbjO1zg89xRCMRvq9Ff7Tx8J9S6XX5MtM6M2n-jdbe5WqtpPCirqSnStV-u5riCiRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك عبدالعزيز في جدة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90671" target="_blank">📅 14:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90670">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📰
‏
رويترز تزعم:
مسؤولون أميركيون عقدوا اجتماعًا مع الحوثيين في سلطنة عمان مطلع الأسبوع.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90670" target="_blank">📅 14:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90669">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8102a11d2a.mp4?token=fT4TJaS8UhOCeh_ADSyQ76jxk4zWHRWmF8PCn2Py0hCV4jicwLTuPJyE0dD3czyzZWa-RDxEBLhHjq8dXF8-Rcgi4JDR8S5RdR-1uZjOXqImm7FKYEyXhwgxwY2rI39YI3IiO2YInaJ_biAFL8XQaOnkaRkZjB_e5aW90PP0K6UlhQFXaVyJkrQ0VIM1FUt0nWLp4wIvLfz_YXxYT4vv05_8uX4PYkDgQ8rcDUbshUf46Rl-3CBIIETqX5XZuMSIihX8RPifSv5s65jbcxU2AVZ8MaQxHwfh-vvFXSmrGoNL9J5buy10sxtHyoVEHfCPhL-tV1vvwZvYuMEUWubQeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8102a11d2a.mp4?token=fT4TJaS8UhOCeh_ADSyQ76jxk4zWHRWmF8PCn2Py0hCV4jicwLTuPJyE0dD3czyzZWa-RDxEBLhHjq8dXF8-Rcgi4JDR8S5RdR-1uZjOXqImm7FKYEyXhwgxwY2rI39YI3IiO2YInaJ_biAFL8XQaOnkaRkZjB_e5aW90PP0K6UlhQFXaVyJkrQ0VIM1FUt0nWLp4wIvLfz_YXxYT4vv05_8uX4PYkDgQ8rcDUbshUf46Rl-3CBIIETqX5XZuMSIihX8RPifSv5s65jbcxU2AVZ8MaQxHwfh-vvFXSmrGoNL9J5buy10sxtHyoVEHfCPhL-tV1vvwZvYuMEUWubQeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لماذا لم يعد يصدق العالم بالروايات الإعلامية السعودية ؟!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90669" target="_blank">📅 14:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90668">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇷🇺
‏
روسيا:
أميركا لم تبلغنا بنشر أسلحة في الفضاء</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90668" target="_blank">📅 13:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90667">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بيان مهم للقوات المسلحة اليمنية للإعلان عن عدد من العمليات العسكرية في العمق السعودي في تمام الساعة 2:40 عصراً.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90667" target="_blank">📅 13:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90666">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇵🇰
رئيس الوزراء الباكستاني يدعو انصار الله والسعودية لضبط النفس والتفاهم والحوار وسماع دوي كفران من قصر اليمامة في الرياض.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90666" target="_blank">📅 12:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90665">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">عشرات الرحلات الجوية تغيّر مسارها من الأجواء السعودية إلى العراقية مع تواصل هجمات القوات المسلحة اليمنية على النظام السعودي</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90665" target="_blank">📅 12:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90664">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIy5Tc3T7fsOl0j8iZweSCkOOPfcr6CkVRxGB3Z_3qCewrsdpy4325LhOLfhoWmCQvVmb9IBTCHLESsvBNPf8MTmt2SoOFFnIOb2R_rNLLIo1i-yOdVB0vMqljRAG9G_4LV2hD0X1T2KVYdAet707NUOQ6M0IjMlpXF6GtC2BkfphZCAoyje5KLGuEp8xRtGVdpayCWlGt6a1ZRavPWECi7-YwaDZQnLOxK-sqgUzk5WMz5u84NORcV667W6FAic4ahvHK4QOq4bRUIOXOan1jFk3vK6PF27MYYcJkDJgSAKwwcXNrBp97z2bS040xwlsHGBNVcYzCMd3XtRi_iLzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الماكنة الإعلامية السعودية تعيد سردية صدام مع أنصار الله في اليمن ؛ الاستجداء والبكاء عن استهداف مكة المكرمة التي حولها مقترباتها ابن سلمان لأكبر ماخور للدعارة وبارات للمشروبات الكحولية ..</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/90664" target="_blank">📅 11:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90663">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
اقليم كردستان العراق يعاني من أزمة الطاقة
شركة دانة للغاز الاماراتية  تخفض صادراتها وتعلم شركاء قطاع الكهرباء بأن شركة دانة للغاز قد خفضت كمية صادراتها من الغاز إلى محطات توليد الطاقة، مما أدى إلى انخفاض إنتاج الكهرباء بمقدار 1000 ميغاواط.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90663" target="_blank">📅 10:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90662">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
إنفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/90662" target="_blank">📅 09:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90661">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
إنفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/90661" target="_blank">📅 09:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90660">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الله أكبر
🇾🇪
عضو المكتب السياسي لأنصار الله في اليمن "حزام الأسد" يعلن عن استهداف طائرة F15 تابعة للسعودية.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/90660" target="_blank">📅 09:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90659">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الله أكبر
🔻
🇺🇸
الدفاعات الجوية التابعة للحرس الثوري تتمكن من إسقط مسيرة أمريكية من طراز MQ9 في سماء جزيرة قشم جنوبي إيران.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90659" target="_blank">📅 08:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90658">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇦
🇷🇺
‏
زيلينسكي:
روسيا حاولت استهداف طائرتنا الرئاسية مرتين خلال الأسابيع الأخيرة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90658" target="_blank">📅 08:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90657">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
‏بلومبرغ: قوات أميركية صعدت على متن ناقلة نفط متجهة لتكساس للتحقيق في هجوم إلكتروني.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/90657" target="_blank">📅 08:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90656">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
مجلس النواب الأمريكي يصوت للمرة الثالثة على قرار يقيد تحركات ترامب العسكرية بشأن حرب إيران.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/90656" target="_blank">📅 07:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90655">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90d766f6c5.mp4?token=Xc-urGn6X6-yUTMZ1nplP1vfF7aVLgMYLFaj2VcSTZtWlEV_LMGpKGuk2CnpoQ8InRnhPIJw83yzAd0fDOVceCtDQ0BFgNX7kHN_6paa8wQl8_OIX2oQtWrQ2B2yWmaHfPCY8d7xKe-bZYet5z3KEX7ptoHZBAodbUGBZa255U0RynL0fuG_NKofKFGJIDV0neZQHlidDhMIlz0fMHSek2oVR1u-t__pgJ8VkFVPzsR9ZjiBADZ0YOhIFDTbFJsanjwKomenletrt_0S9SaPHY2Tah9bi-eP5Ecae2ZsarPMqQhUQrh0U-UGyVU3RRBg5m7Hxvn0-GuiTQFLeI45-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90d766f6c5.mp4?token=Xc-urGn6X6-yUTMZ1nplP1vfF7aVLgMYLFaj2VcSTZtWlEV_LMGpKGuk2CnpoQ8InRnhPIJw83yzAd0fDOVceCtDQ0BFgNX7kHN_6paa8wQl8_OIX2oQtWrQ2B2yWmaHfPCY8d7xKe-bZYet5z3KEX7ptoHZBAodbUGBZa255U0RynL0fuG_NKofKFGJIDV0neZQHlidDhMIlz0fMHSek2oVR1u-t__pgJ8VkFVPzsR9ZjiBADZ0YOhIFDTbFJsanjwKomenletrt_0S9SaPHY2Tah9bi-eP5Ecae2ZsarPMqQhUQrh0U-UGyVU3RRBg5m7Hxvn0-GuiTQFLeI45-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
إنفجارات عنيفة في العاصمة الأوكرانية كييف نتيجة هجوم روسي بالطائرات المسيرة الإنتحارية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/90655" target="_blank">📅 06:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90654">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59c694da9.mp4?token=udm9Y5ctkP7fH1nDKVLbT91w9kbaUuNDwwOSAElOqgU_zyaUji10UfmciESSZFoT3V-Q9wriDlivr8B9N_e6CLJzzr8E4DZoj2MQO6LcHS9pUaOP3QVCqS7PI8UwNYzc0muXYJgJVVkj63P-18PG2KybDnQmmvj2u6LpMuM9PjnJ7woOp6kog9GsPizHXa0VRHYa1X8ZzRrKc-vEY-sI4VQ1tHvE97lF6oNG2XNvaaZo9Q5SEQb0M4LtLP9RYP5S7j5xrDhfn7kyitbk1zUNOWVyBocv2vaH_GonMxy9-GzUR2_cZ-LrYhtoB-p51qMfpAIJbAJu-u4Ri7jIM2ic1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59c694da9.mp4?token=udm9Y5ctkP7fH1nDKVLbT91w9kbaUuNDwwOSAElOqgU_zyaUji10UfmciESSZFoT3V-Q9wriDlivr8B9N_e6CLJzzr8E4DZoj2MQO6LcHS9pUaOP3QVCqS7PI8UwNYzc0muXYJgJVVkj63P-18PG2KybDnQmmvj2u6LpMuM9PjnJ7woOp6kog9GsPizHXa0VRHYa1X8ZzRrKc-vEY-sI4VQ1tHvE97lF6oNG2XNvaaZo9Q5SEQb0M4LtLP9RYP5S7j5xrDhfn7kyitbk1zUNOWVyBocv2vaH_GonMxy9-GzUR2_cZ-LrYhtoB-p51qMfpAIJbAJu-u4Ri7jIM2ic1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تحطم مروحية تابعة لقناة "إن بي سي نيوز"، بينما كانت تغطي حادث اصطدام حافلة في مدينة لوس أنجلس بولاية كاليفورنيا الأمريكية؛ مقتل 3 وإصابة أخر كحصيلة أولية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/90654" target="_blank">📅 06:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90653">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
🇮🇷
مسؤولين أمريكيين وإقليميين مطلعين:
القوات الأمريكية أطلقت ما بين 60 و70 صاروخًا اعتراضية من طراز MIM-104 Patriot، وأكثر من 12 صاروخًا اعتراضية من طراز THAAD، لمواجهة الهجوم الصاروخي الباليستي الإيراني الذي وقع الأسبوع الماضي ضد القواعد الأمريكية في الأردن، والذي تضمن حوالي 20 صاروخًا باليستيًا.
أن الاستخدام المكثف لأنظمة الدفاع الجوي الاعتراضية لمواجهة هجوم واحد يعادل الكمية التي كان سيتم استخدامها خلال أسبوع كامل في وقت سابق من الحرب.
استخدامت إيران ذخائر عنقودية، وأن بعض الصواريخ الباليستية تمكنت من تجاوز الدفاعات الجوية، مما أدى إلى إصابة طائرات، بما في ذلك طائرات مقاتلة، في قاعدة "موفق السلطي" الجوية.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/90653" target="_blank">📅 05:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90652">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تطلق صواريخ دفاع جوي نحو الطيران الحربي السعودي أثناء دخوله إلى سماء محافظة مأرب.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/90652" target="_blank">📅 04:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90651">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9BDw3mQnVZTvdrGY9a2If6u0zs-AoK0D9CHNXUnVCYS371mlElD8djVu0GXz_-LFRLl2vj8PeDDtUrAKrb75t9RU4P9asbnZGUyrQrMYU6beC5sdmTiz2hIuSsQTu0vTPWu-yMvd-vC4Uui7MTXXsqzH2QOzLPHWt8iiBKSrJVH7xKn_DreuL80cFZiSuzB2AYC2U1mE2qWRAyPZqn_ExoWMwVxeCrQToRLVPmiYyCULHVl2Za0U1mXRVjoFSzk1ZipyP2tF4t1-v-U9igyJujJzIemuDEEi9d5jmIUy4zF6cvB4nlCnHX2MdFZlHVib1cKXtZZEgOvZISI-UwNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
السفارة الأمريكية في الرياض تعلن عن رفعت مستوى التحذير الخاص بالسفر إلى السعودية للمستوى الثالث:
"إعادة النظر في السفر"، وذلك بسبب المخاطر الناجمة عن هجمات الطائرات المسيرة والصواريخ الإيرانية التي تستهدف المصالح الأمريكية، والصراعات المسلحة والإرهاب.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/90651" target="_blank">📅 03:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90650">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تطلق صواريخ دفاع جوي نحو الطيران الحربي السعودي أثناء دخوله إلى سماء محافظة مأرب.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90650" target="_blank">📅 03:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90649">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇸🇦
ضمن سياسة تحريك مشاعر التكفيريين..
السعودية تزعم:
الدفاع الجوى السعودي اعترض طائرة مسيرة حاولت دخول المجال الجوي لمكة المكرمة.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/90649" target="_blank">📅 02:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90648">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
‏
بلومبرغ:
قوات أميركية صعدت على متن ناقلة نفط متجهة لتكساس للتحقيق في هجوم إلكتروني.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/90648" target="_blank">📅 02:48 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
