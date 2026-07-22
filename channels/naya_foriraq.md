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
<img src="https://cdn4.telesco.pe/file/BZMsyquTd5zaDHo2M1UcXS99CWhVfHLrdjTO8-g5tr8zft14YXCnDUUI-8-nM6emkDmTds9DKNIXmZI7FdBwKNOoefe-c77kh-qMbHh_8RSF4UCJH_ab0G_h6fBFOsWCqLKkQ6AcQmJ4kPdCO-ZoI3dv5hGgmqC-0lxxYfT1UhHjBBfE6BmrXhcrjecMjBhTsvJxiJ65S4F7qz_3HC0Uqx9lnQT0CrYajkhvG-sYepAuBrB-c2bN-fcrTl1eNcoCiYNoz15RcZZWWV1xpiFBo-5cdXIQuVNXhqASN62o4aCh6QNGnceY-emly-OkTxcQbMsd-v1ubvxY0ZzfRXk2yQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 08:41:34</div>
<hr>

<div class="tg-post" id="msg-84786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clv_biTBT9tWATdbn5bJmW7aacigRS485dqwR3LTFTyNtecxb0vJDROZQPebC88xEZsXQjA2EwapFUwh7lgYe2xY9nmqqp_g_on6cUlgIbyDHlZ845CD96saanL_GiGRgL6aHQ66fDkGKSFqjuHkqlio8ADyLBKqKQnA0_xzbHoPZeVIDr_T5z8KPAIwo-ptLCLuLVUHn_AdWgUY8ColtfPLFreH1avlKBImZfkIbXrEy53paKk0oav9CTfnz3S8wwjfvEDjYtwp-_eGJtJWDVFBfSL206QI-VhrRa47X9FDkye66RPiO2WfRraYUxWbxWsR3x5m5uBLXT7F57hAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
نشرت مواقع أمريكية آثار الضربات الإيرانية على قاعدة برج ٢٢ الأمريكية الملاصقة للشريط الحدودي بين العراق وسوريا والأردن والتي تعرف بالتنف ؛ مرة اخرى غياب تام لمشهد منظومات الدفاع الجوي الأمريكية التي فشلت بالدفاع عن سماء الأردن</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/naya_foriraq/84786" target="_blank">📅 08:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgn_TvKL-3RiANu6puaFgaV9ptu1XykqiBnUmcYPIzbBAIm88o8izeMmSJD1Ulk-uvalC6CZvId3JlYkCO6R55sGUXjZN9-AcJKEO1XBeCqT2gGoQa5-cuf8tt7lhxsJl8Oq5svu87ZSdQWksLAD94D42IwECQCl0_ynQxUDcSWs04IMymq-A460pQMle6igKicOlC3Nc9WuMYfH-zjQDgQMyEOfiASmOXzFcQRzgnttqo3Qc0kInPHsXKfj4mEFV4DU7wX6pMPW0T7FpxJnCXM27IOlCSZ-2VGED_q43IJCMK1IzMeUn9k0UDG_TTf2pWeGeiwp79aAd1uRp8DfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
وصلت طائرة الاتصالات المحمولة جواً من طراز E-11A التابعة لسلاح الجو الأمريكي إلى قاعدة رامشتاين الجوية قادمة من قاعدة روبينز قبل لحظات، ومن المرجح أنها تستعد للانتشار في قاعدة الأمير سلطان الجوية في السعودية، حيث تتمركز 4-5 طائرات من طراز BACN في القاعدة.</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/naya_foriraq/84785" target="_blank">📅 08:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84784">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
‏بيانات كبلر: 3 سفن شحن فقط عبرت مضيق هرمز يوم أمس</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/naya_foriraq/84784" target="_blank">📅 08:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84783">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c08e38319.mp4?token=a_oy4qbSRDzmsVB7zynVnIwYt4fFHl2oAfamfv_Cd1AJuxxL2ALq3B4Mkm_pJ0lwymauuJjDiUpo7I3ZG_FHAWwLgRl96BEJuDbVfOQVAM8ZCOOP1CkkAjOm0pEsttQb4ZW9m68Wj-qzEIwpJY9O0em6PdQFwZnFWzM-H0Hb0diLMu3EbnLxIUFBuLWVQqs8UE4vbA1y8YkhvhiiJkBnmN4_BaFGc-2NEGtSa1hs78iaUcrn_4BuMGK6KmW6QOuFCJq9_q4VSEe936u9JEf6yhqrFRdXVDCMQyiQTSY1SkWA73oUB46h55XAkTidXiJASnDq5a-NZwA2nW7hNf_NrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c08e38319.mp4?token=a_oy4qbSRDzmsVB7zynVnIwYt4fFHl2oAfamfv_Cd1AJuxxL2ALq3B4Mkm_pJ0lwymauuJjDiUpo7I3ZG_FHAWwLgRl96BEJuDbVfOQVAM8ZCOOP1CkkAjOm0pEsttQb4ZW9m68Wj-qzEIwpJY9O0em6PdQFwZnFWzM-H0Hb0diLMu3EbnLxIUFBuLWVQqs8UE4vbA1y8YkhvhiiJkBnmN4_BaFGc-2NEGtSa1hs78iaUcrn_4BuMGK6KmW6QOuFCJq9_q4VSEe936u9JEf6yhqrFRdXVDCMQyiQTSY1SkWA73oUB46h55XAkTidXiJASnDq5a-NZwA2nW7hNf_NrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تُسجل الأجواء الجوية في جنوب العراق تحليقاً مستمراً لطائرات مسيرة مجهولة يُعتقد أنها تقوم بتنفيذ مهام استطلاعية وعمليات مراقبة للمنطقة.</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/naya_foriraq/84783" target="_blank">📅 07:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84782">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇱
🇺🇸
عمدة نيويورك زهران ممداني: نتنياهو مجرم حرب ندعو الحكومة الفيدرالية إلى تنفيذ مذكرة الاعتقال في حال زيارة نتنياهو لنيويورك، حيث من الضروري التأكيد على اعتقال الزعيم الإسرائيلي ومحاكمته على جرائمه.</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/84782" target="_blank">📅 07:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84781">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الله أكبر
موجة صواريخ تنطلق من الجمهورية الإسلامية الإيرانية نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/naya_foriraq/84781" target="_blank">📅 07:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84779">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVAvzIiDiLLpbapemRlKYsGL07oo470uGhebnsOZdkGYxc77t3QoE89NxPg7dd59_oNdH5pGmhyr87eMJMA46v2DWc2KgHk4t22Yiw9Cc0aaLYIk5CMfMETdNz7jn5hJhQEcceTAHXclxqfQcAEK3_2Xop-jkS9VJ4aCMrV5NXbbt8LZ2IqWgtb_6lodqqHj2omkEU9kOwr-6MOJL6VCZEl4E93Zp0Y9tyoKyI_UkufZQVh4FRj7J5OPUs3o98KF-JlcTVQS_JjbVXf6e9z3Mcg48uO33iHbZpGo5iaL2fAeS2eexwQU4-sxsPrsT9tN8U9UPi4FvCAQW7I5blI89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqOKfiafrNuiXS84nnLCgDiaGtiEEWjCwyB484ChWgAerAvACUMlWhHgjyZNH6HKn_S_HAr2rxvwegsyOz_xNQlgKtSKmKE3_cqpZuCHab80NBXyrfhpnHbreB-Puj9o0zpBUhSnKGhIkhEBj2ZKJUuE5C-teYok2AEOMotd62gTYRqP7aRVaBBX1BcDq4cLn7fZGhi4CvAirX-wVYFlleWrhrsHz7yzjVRadX_yGigFG8X393PbRX8YILRK-lqhgGsbfxz87EEeZl1t96bsOYDo8diCpyiT7mWVdyiU-4n1glPu9Q5maWSZMW1b4SOWWdvNKUrVQotvQEiKBva0qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
صورة فضائية لمضيق هرمز تحديداً في جنوب جزيرة لارك تُظهر تعرض ناقلة نفط للاحتراق والتسرب النفطي جراء قصفها من قبل الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/naya_foriraq/84779" target="_blank">📅 07:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84778">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21a80068cf.mp4?token=HvKFSJRBZ0l5kBOgv1biejmkn_ADWlbvWmwSpHGZH27UqpTKZy30PoJanDz8TYKkMYC8omF_2UEA1Rn71zSml2MPvpKvzkWtthFXNZ1FMo-WFDXKWJEppWV3UEje71LF4TjtZkgRlN7s_KBtac53ZPlxleo9FqkpnzI6A5UmqBuCsB25e4qIYuFixQVf9EdMrvy9n5tCugw8GQ9hF2Ve2qJIBybFW6OQcg4ucOtEH7KWPbL7fsdfzMw14QyZ8m_RgLrUhMDuW9i8AIq0VJXIq6aRZj4ZFqiMg1bTSCS78R4PQvbgUA1V27neKObOCYiQgA1_9cXEzbc675RvkJzBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21a80068cf.mp4?token=HvKFSJRBZ0l5kBOgv1biejmkn_ADWlbvWmwSpHGZH27UqpTKZy30PoJanDz8TYKkMYC8omF_2UEA1Rn71zSml2MPvpKvzkWtthFXNZ1FMo-WFDXKWJEppWV3UEje71LF4TjtZkgRlN7s_KBtac53ZPlxleo9FqkpnzI6A5UmqBuCsB25e4qIYuFixQVf9EdMrvy9n5tCugw8GQ9hF2Ve2qJIBybFW6OQcg4ucOtEH7KWPbL7fsdfzMw14QyZ8m_RgLrUhMDuW9i8AIq0VJXIq6aRZj4ZFqiMg1bTSCS78R4PQvbgUA1V27neKObOCYiQgA1_9cXEzbc675RvkJzBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
مشاهد من الأقمار الصناعية توضح أضراراً لحقت بمحطة الدعم الأرضي ومنشأة الصيانة التابعة للطائرات الاستطلاعية الأمريكية في مطار أربيل الدولي شمال العراق جراء القصف الإيراني.</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/naya_foriraq/84778" target="_blank">📅 06:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84777">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57068982f0.mp4?token=uihVVNCTLc0jsDXk8La85WBHQfRC0kIJmAOt8RDGJVkHul4OjG-cLaldnpnfefurTuh6-Ptu6btwFSJaafjoh40g8Q8T6I-tMSRWIP3MItJKbEmcp5Dh9m-vZN5kiJNk3dHSPNF9lbCzPZXWmEaoiTKC-iTnaEATv90FfbAXS-Y2wwOSojne1ppktrQcB8hpHIZ2QSxA1dHtcDtuE2w_cMzL-hYScVUF-DNbI6JjVwDhwiFWDjXiRQzPfwfEbxGQvgHmNTwZrwPTuN9JhkZnHEqj7eXcTmYz8-Tm1FwWW_rGCmhXEd8o1pa59tQyyB44LZ_6ErzHShxIP3zox7cIzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57068982f0.mp4?token=uihVVNCTLc0jsDXk8La85WBHQfRC0kIJmAOt8RDGJVkHul4OjG-cLaldnpnfefurTuh6-Ptu6btwFSJaafjoh40g8Q8T6I-tMSRWIP3MItJKbEmcp5Dh9m-vZN5kiJNk3dHSPNF9lbCzPZXWmEaoiTKC-iTnaEATv90FfbAXS-Y2wwOSojne1ppktrQcB8hpHIZ2QSxA1dHtcDtuE2w_cMzL-hYScVUF-DNbI6JjVwDhwiFWDjXiRQzPfwfEbxGQvgHmNTwZrwPTuN9JhkZnHEqj7eXcTmYz8-Tm1FwWW_rGCmhXEd8o1pa59tQyyB44LZ_6ErzHShxIP3zox7cIzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
ردًا على تكرار العدوان من قبل العدو اللئيم على مناطق في بلادنا، استهدف الجيش الإيراني، في المرحلة الحادية والعشرين من عملية "صاعقة"، قبل ساعات، "مخازن الذخيرة" و"المعدات اللوجستية لمركز قيادة القوات البرية" للجيش الأمريكي الإجرامي في معسكر الدوحة غرب الكويت، وذلك بهجمات مكثفة بطائرات مسيرة.
🔹
يعتبر معسكر الدوحة من أهم وأبرز القواعد العسكرية الأمريكية في غرب الكويت، وهو مركز دعم للقوات الأمريكية المتواجدة في غرب آسيا، حيث يتم فيه استقرار كميات كبيرة من المعدات والجنود التابعين للقوات البرية الأمريكية، بالإضافة إلى القوات البحرية والجوية.
🔹
القوات المسلحة الإيرانية، بتوحيدها المقدس، مستعدة لمواجهة أي مؤامرة أو مغامرة جديدة يقوم بها العدو.</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/naya_foriraq/84777" target="_blank">📅 06:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84776">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏دوربين: هل لديك تقدير جديد حول ما كلفتنا إياه الحرب حتى الآن في هذا الشهر الخامس من السنة الأولى لهذه الحرب في إيران؟
🇺🇸
‏وزير حرب: يا سيادة السيناتور، التقدير الذي لدينا حتى اليوم هو 37.5 مليار.</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/naya_foriraq/84776" target="_blank">📅 06:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84775">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a233b6a886.mp4?token=r11jIHTtX6vjiNNnq7RYqxbrNePh8rM1qre9Vs3hDNFlexXnScaz8WEkY5FWAnRYM07QGhYYltvIDC3FvMPlM8GGd_-D_hwYf-cLyQtnGUrMntGGSCe9g_i0IxxalKzkdDTpAW6QgIjdGyyV1b51iG7doZYUDKvkmGTtdmNSeDC-cygMnTHQQ-NtqBHacWmrUM2bsFK-G92QHSA61DhTPpyQ4dNXdsChb71GBsBid9YNfUM5S4_TvPTQ09giblQzgtGSirvN_tdJiPf1FI5llKqcrtGttjwRaLD3mctfieJ-qgbFwjMJdS3RnJETGl6QGmw6hC3Sk1Z5VB_pLcsiUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a233b6a886.mp4?token=r11jIHTtX6vjiNNnq7RYqxbrNePh8rM1qre9Vs3hDNFlexXnScaz8WEkY5FWAnRYM07QGhYYltvIDC3FvMPlM8GGd_-D_hwYf-cLyQtnGUrMntGGSCe9g_i0IxxalKzkdDTpAW6QgIjdGyyV1b51iG7doZYUDKvkmGTtdmNSeDC-cygMnTHQQ-NtqBHacWmrUM2bsFK-G92QHSA61DhTPpyQ4dNXdsChb71GBsBid9YNfUM5S4_TvPTQ09giblQzgtGSirvN_tdJiPf1FI5llKqcrtGttjwRaLD3mctfieJ-qgbFwjMJdS3RnJETGl6QGmw6hC3Sk1Z5VB_pLcsiUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
وزير الخارجية الأمريكي:
واشنطن منفتحة ومستعدة للتفاوض لتسوية الخلافات في الشرق الأوسط.
المشكلة التي نواجهها هي عدم جدية إيران بشأن المحادثات.
الاقتصاد العالمي مهدد وحصار الممرات المائية الدولية سابقة خطيرة للغاية يمكن أن تتكرر في أجزاء أخرى من العالم.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/84775" target="_blank">📅 05:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84774">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مجدداً تفعيل الدفاعات الجوية في العاصمة الإيرانية طهران</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/84774" target="_blank">📅 04:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84773">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
🇸🇦
وول ستريت جورنال:
وافق الرئيس ترامب على اتفاق تعاون نووي مدني لمدة 30 عامًا مع المملكة العربية السعودية، بقيمة عشرات المليارات من الدولارات.
من المتوقع أن يتم توقيع الاتفاق، الذي سيوقع عليه وزير الطاقة الأمريكي كريس رايت ووزير الطاقة السعودي الأمير عبد العزيز بن سلمان يوم الأربعاء، وسيمنح الشركات الأمريكية دورًا رائدًا في تطوير البنية التحتية النووية المدنية في المملكة، مع استبعاد المنافسين الأجانب إلى حد كبير.
بموجب الاتفاق، يمكن للشركات الأمريكية بناء منشأة لتخصيب اليورانيوم في المملكة العربية السعودية إذا خلصت دراسة مشتركة بين الولايات المتحدة والسعودية إلى أن مثل هذا المشروع مبرر.
من المتوقع أن يتم تقديم الاتفاق إلى الكونجرس للمراجعة في الأيام القادمة، ومن المرجح أن يواجه معارضة من بعض أعضاء الكونجرس.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/84773" target="_blank">📅 04:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84772">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
🇮🇷
مصدر إيراني:
العدوان الامريكي الأخير استهدف مدينة كبودرآهنگ بمحافظة همدان الإيرانية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/84772" target="_blank">📅 04:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84768">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866b442a2d.mp4?token=MwYepwIsAj2vTg5eLqT-YwG6ZUdWKCwuRfuFfBYJJwBCKBZRYeAqUw45dem6J0VtkNE9oMot-TGoLZFeFbcFevnlBiaBBJR5gdB54CgyDdKfa9DO182LcdyOTkxAoFpwMV2VIzXkrfuXXJwdSWYNDzoQ2vUXtUt_VxLx3ku6gbyTo23l9gXeUyYBn9OLI8X52mu8AtyI0-aFitTsNs-wIR_qnasPni8XBhvbiheZ6sjN_LuAAG2B88LO_8YhLX4K32ZwNcpnl4vBZpM8os086Peq1crG2RLolIQcFyq5yw8UfN09FWcvpldTD-5jxUCO_2Eam_Oc2rOgwmk1tlRTAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866b442a2d.mp4?token=MwYepwIsAj2vTg5eLqT-YwG6ZUdWKCwuRfuFfBYJJwBCKBZRYeAqUw45dem6J0VtkNE9oMot-TGoLZFeFbcFevnlBiaBBJR5gdB54CgyDdKfa9DO182LcdyOTkxAoFpwMV2VIzXkrfuXXJwdSWYNDzoQ2vUXtUt_VxLx3ku6gbyTo23l9gXeUyYBn9OLI8X52mu8AtyI0-aFitTsNs-wIR_qnasPni8XBhvbiheZ6sjN_LuAAG2B88LO_8YhLX4K32ZwNcpnl4vBZpM8os086Peq1crG2RLolIQcFyq5yw8UfN09FWcvpldTD-5jxUCO_2Eam_Oc2rOgwmk1tlRTAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي الغاشم على مدينة بهبهان بمحافظة خوزستان جنوبي إيران</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/84768" target="_blank">📅 04:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84767">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7dc06fc7.mp4?token=OCEyQeshAq9Hm4ZRx_fU5IINCjDQm8cbdPfzvmclC3n-Rl-lBJzpY29BSa_3l-n9h0rQ7iQt_Ra0z-IVmVkIVH__OVE-j3Kj42KmVm7mLFvMgXDzL_qajVXS6T6EYMMccjq8RCSHek3A7WSJhVZz-fpXzd_hP2rGt_-8u_mWMP0bDY8wgEc89KbG5S1M5uMf84GO6BAhKaqVI1Lz3n9ElPdAD5kYB89ArytydbY0fouUufNoHW-p-VNW4N7FicX0fpeir63A9fl_Qct_MaGnCt9oipCt0sgJB_t5BKn7g-z4Nl0I52huH5PJgYKlC4hsljvS-iW_eVKhAbavIXY0Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7dc06fc7.mp4?token=OCEyQeshAq9Hm4ZRx_fU5IINCjDQm8cbdPfzvmclC3n-Rl-lBJzpY29BSa_3l-n9h0rQ7iQt_Ra0z-IVmVkIVH__OVE-j3Kj42KmVm7mLFvMgXDzL_qajVXS6T6EYMMccjq8RCSHek3A7WSJhVZz-fpXzd_hP2rGt_-8u_mWMP0bDY8wgEc89KbG5S1M5uMf84GO6BAhKaqVI1Lz3n9ElPdAD5kYB89ArytydbY0fouUufNoHW-p-VNW4N7FicX0fpeir63A9fl_Qct_MaGnCt9oipCt0sgJB_t5BKn7g-z4Nl0I52huH5PJgYKlC4hsljvS-iW_eVKhAbavIXY0Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الامريكي:
تامبا، فلوريدا - في تمام الساعة الثامنة مساءً بتوقيت شرق الولايات المتحدة يوم 21 يوليو، أكملت القيادة المركزية الأمريكية (سنتكوم) بنجاح الليلة الحادية عشرة على التوالي من الضربات الجوية ضد إيران.
استهدفت أصول سنتكوم مراكز العمليات العسكرية الإيرانية، والقدرات البحرية، وحظائر الطائرات، ومرافق تخزين الطائرات المسيّرة، والبنية التحتية اللوجستية العسكرية، وذلك بهدف تقويض قدرة إيران على تهديد الملاحة التجارية في مضيق هرمز.
على مدى الأشهر الثلاثة الماضية، هاجمت إيران أكثر من 30 سفينة تجارية عابرة للممر المائي الدولي الحيوي للتجارة الإقليمية والعالمية. وقد عرّضت هذه الهجمات غير المبررة حياة مئات البحارة الأبرياء للخطر، وقوّضت حرية الملاحة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/84767" target="_blank">📅 04:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84766">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5bf7c4bb2.mp4?token=AnZUdzbq9dG3HB7Sp28XOuJaNXkPu7bnLNrT2ittTfPa25fS0UtNBcD7TrNR3ecMfAIlgYSd3Rh8e2_WLIZwHd4z6y_sDoUJ6OW7b_4ZwyH8tbMIr1hZr_Sm4PM1eHpCuisgIBVb2olasIwcGIbjcv_WKkemFHJ8prn59cwNBZxDBajS5nRUiY9dTLT910tpra-1ceqvgbir54BPZl8mLyiQ3Yqvh1E8GK1kx8KXEPwsEH0snkeH1BipieEGkfDbrkGo6R6EHoSiM27eO1MOyBWbCBkW3UyKtmw7OThjDMJBjAkpeUzLkgm351s8kg7D5PYlkNVaZFXNBEGVhv90JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5bf7c4bb2.mp4?token=AnZUdzbq9dG3HB7Sp28XOuJaNXkPu7bnLNrT2ittTfPa25fS0UtNBcD7TrNR3ecMfAIlgYSd3Rh8e2_WLIZwHd4z6y_sDoUJ6OW7b_4ZwyH8tbMIr1hZr_Sm4PM1eHpCuisgIBVb2olasIwcGIbjcv_WKkemFHJ8prn59cwNBZxDBajS5nRUiY9dTLT910tpra-1ceqvgbir54BPZl8mLyiQ3Yqvh1E8GK1kx8KXEPwsEH0snkeH1BipieEGkfDbrkGo6R6EHoSiM27eO1MOyBWbCBkW3UyKtmw7OThjDMJBjAkpeUzLkgm351s8kg7D5PYlkNVaZFXNBEGVhv90JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادامه فعالیت و شلیک پدافند در آسمان تهران</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84766" target="_blank">📅 04:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84765">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4fae7dfb.mp4?token=e1UXwIKMRfjTAGa6pW5U9Jik2gRolcOrVHvKghFBGs-q2xJ6VRUqH-PddvMLf1As45imBUQBTuEbAjFH2v2qP9j2nwhy7uLfzLX2qFIHO5xWePFnqtaSE7fNNPincUmBBNC575r_c26ryKJ3igvrMYQQ6AjH97lZ2KsJQKAf2COR6rK4tCDknnSdL8iR_snp7Z0LZktCQASNs2089r_84ysC6ufmVgNly21HwLfs_6WNJWF2HiWiYwMXHAc2GvItyRyEFKiBOabXgonRpVqUo46W4Pv_xoYi2-Svtlna8MUokRpLQl1ihf1O8ahbty2boYhpzcfOw2DYRuQO2Fxczw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4fae7dfb.mp4?token=e1UXwIKMRfjTAGa6pW5U9Jik2gRolcOrVHvKghFBGs-q2xJ6VRUqH-PddvMLf1As45imBUQBTuEbAjFH2v2qP9j2nwhy7uLfzLX2qFIHO5xWePFnqtaSE7fNNPincUmBBNC575r_c26ryKJ3igvrMYQQ6AjH97lZ2KsJQKAf2COR6rK4tCDknnSdL8iR_snp7Z0LZktCQASNs2089r_84ysC6ufmVgNly21HwLfs_6WNJWF2HiWiYwMXHAc2GvItyRyEFKiBOabXgonRpVqUo46W4Pv_xoYi2-Svtlna8MUokRpLQl1ihf1O8ahbty2boYhpzcfOw2DYRuQO2Fxczw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء العاصمة طهران تشهد نشاط واسع ومكثف للدفاعات الجوية لصد الاجسام المعادية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/84765" target="_blank">📅 03:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84764">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6295b13288.mp4?token=qFtg0ln0hntuo9eJiu0OLLShCOYpvHm1wgTe-ZDHuxXZ5LkzKdN28zqQGzNUG1XQuvbq5MPJ6jnpMpbdss6B9Ce8Yx-6ZDyuNOKZY6cb0h5JJidGHgZ-I9hz24QORCd-T1Z2nvURfS7pOMEUHTXrTq1JOzz9fm9jchg73cKH3tyVlSwiqfu0m9cGF73Zo6pJg4dqpu2HkXnNaQ0tkdbGpc67KKAlP4kXI3xIjp8R6IFHeEbhyUaf1CdY1Qi9NZzQpIBcUYG6V9HsPGVMfQ-ZUA5Ev5IGu6c97ZJBqieYSI5uyKBY0tlePRpZk4moNJY4hr4IMDGKJWjnYCZpZuNTwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6295b13288.mp4?token=qFtg0ln0hntuo9eJiu0OLLShCOYpvHm1wgTe-ZDHuxXZ5LkzKdN28zqQGzNUG1XQuvbq5MPJ6jnpMpbdss6B9Ce8Yx-6ZDyuNOKZY6cb0h5JJidGHgZ-I9hz24QORCd-T1Z2nvURfS7pOMEUHTXrTq1JOzz9fm9jchg73cKH3tyVlSwiqfu0m9cGF73Zo6pJg4dqpu2HkXnNaQ0tkdbGpc67KKAlP4kXI3xIjp8R6IFHeEbhyUaf1CdY1Qi9NZzQpIBcUYG6V9HsPGVMfQ-ZUA5Ev5IGu6c97ZJBqieYSI5uyKBY0tlePRpZk4moNJY4hr4IMDGKJWjnYCZpZuNTwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء العاصمة طهران تشهد نشاط واسع ومكثف للدفاعات الجوية لصد الاجسام المعادية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/84764" target="_blank">📅 03:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84762">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f18aca379.mp4?token=OxDUwkSKygwR2uEQsuH3PheHW-PDfdN_3kJay91WtiE712_ttG29rQ-4l4BIq5DlTn6hwpaeT7l_0s7I2IWqN93r31WJqkVFXfhjB1Ck755onVRu9duROu828fLQKExckbpWzjKXqXcHMxFbBB1KkVTCLOG91gx_lq34FdezuJ8I4kOkId8_tX-j6kZpX9LZ6Lwm2fdjL7dPuDO7nzgWWcZ7jjNfhN2IzB8hZZySdK7ReuLBJvpkzPWzvuR2QPSkz3D1Aber4nwAOJbLHUay820avtdAH48-5N6c3lR6DilKdyxO9QHHFxyB_K_x_4gTt2m_yKung33x98ps8yOD4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f18aca379.mp4?token=OxDUwkSKygwR2uEQsuH3PheHW-PDfdN_3kJay91WtiE712_ttG29rQ-4l4BIq5DlTn6hwpaeT7l_0s7I2IWqN93r31WJqkVFXfhjB1Ck755onVRu9duROu828fLQKExckbpWzjKXqXcHMxFbBB1KkVTCLOG91gx_lq34FdezuJ8I4kOkId8_tX-j6kZpX9LZ6Lwm2fdjL7dPuDO7nzgWWcZ7jjNfhN2IzB8hZZySdK7ReuLBJvpkzPWzvuR2QPSkz3D1Aber4nwAOJbLHUay820avtdAH48-5N6c3lR6DilKdyxO9QHHFxyB_K_x_4gTt2m_yKung33x98ps8yOD4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرق العاصمة طهران يشهد نشاط كثيف ومستمر للدفاعات الجوية التي تصد وتعترض الاجسام المعادية</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/84762" target="_blank">📅 03:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84761">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51138cc7cc.mp4?token=StxQ0BmQjqf7LrMGMzIyAXCvYtsjBXFvomjgKbrhtIxikPwa0OM0cKQTbWIK0N2oNM8-T1MctrVq7txW-7fh6I1_PFo2JKUYF2u35a9NX9rUalcssPvawXhZguh_BSKikTnb0rXX_maVuptYRlRwKuDi1sLt0wX3lCNr1yLF89dzAGqMCbsegDdrunkbTwTRIl-nEi2QljHyDP7YNC8VZoMwQBtHnr5WbfqjzSGDL-loYBnGAbJlHJT2dBrS44WMgOPbN9rrgJS0E3ZHIWhAovneV-bdWavLNrSvdVvAcO0NO5qBMySlllkyWElOToEt_obsU-9nY7m7rHPM0v8cQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51138cc7cc.mp4?token=StxQ0BmQjqf7LrMGMzIyAXCvYtsjBXFvomjgKbrhtIxikPwa0OM0cKQTbWIK0N2oNM8-T1MctrVq7txW-7fh6I1_PFo2JKUYF2u35a9NX9rUalcssPvawXhZguh_BSKikTnb0rXX_maVuptYRlRwKuDi1sLt0wX3lCNr1yLF89dzAGqMCbsegDdrunkbTwTRIl-nEi2QljHyDP7YNC8VZoMwQBtHnr5WbfqjzSGDL-loYBnGAbJlHJT2dBrS44WMgOPbN9rrgJS0E3ZHIWhAovneV-bdWavLNrSvdVvAcO0NO5qBMySlllkyWElOToEt_obsU-9nY7m7rHPM0v8cQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تفعيل الدفاعات الجوية الإيرانية في شرق العاصمة طهران</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/84761" target="_blank">📅 03:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84760">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/720a617de4.mp4?token=u1e4xNcYaGnjxnQuMzD1Qe3A6D0QzU3Xw4VIRTnHp6keoSwvDufbei0U7mnFIqCBOU6M9Sn4u0BYbx9aGl_BkERs5eFVDEspMVusEtOt2i3wp3vT51Y_mIEN796BpeZHFB-NHXVzjForfMumXuhJco1gMlXcE8C_mEFbmYSC8aWWlxDw_QL4RGQPmwk02aE5RifUKwpMikkYY0OGOJAb5nSmHgX6QMqvbEwlYY_ef7F16QD2X4CyVstsSgKj8v859iFkGjY7lf5ASRJdpfjSFFFCJwmX82rhby3glLcia9e0qzfqHUfw2uhbDkvyJMeHY7VVASYCNdf3x6vYdx6UBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/720a617de4.mp4?token=u1e4xNcYaGnjxnQuMzD1Qe3A6D0QzU3Xw4VIRTnHp6keoSwvDufbei0U7mnFIqCBOU6M9Sn4u0BYbx9aGl_BkERs5eFVDEspMVusEtOt2i3wp3vT51Y_mIEN796BpeZHFB-NHXVzjForfMumXuhJco1gMlXcE8C_mEFbmYSC8aWWlxDw_QL4RGQPmwk02aE5RifUKwpMikkYY0OGOJAb5nSmHgX6QMqvbEwlYY_ef7F16QD2X4CyVstsSgKj8v859iFkGjY7lf5ASRJdpfjSFFFCJwmX82rhby3glLcia9e0qzfqHUfw2uhbDkvyJMeHY7VVASYCNdf3x6vYdx6UBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادامه فعالیت شدید پدافند در آسمان تهران</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/84760" target="_blank">📅 03:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84759">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b910369c.mp4?token=eJ-ZYYqG0AYbXBDp8lJunYguH5Ju755sq3uUY3IOx9KDu203VKDyggR-qgM2PvZ4wTJGUgocUhjuuU8nhx53oKefGF36wSdt62Hpkpzk4TCUsVzX5JVAGY3tfY2Bz3nBNRUAUakbgg_PKhhTxQAHHMqo4BW-vKRmSjRsKVAvK9N_9zOHC06VK4BeWJx_dxNSHOf7s_Ajv8CQbspXBth1up13MmCUOCgMxvBxvGYCIcm-vgKGVJml87EUUWOlMCsxgiOPfkHVMaZPZog8nZtfIWXLliABknqEc30_KLKL10-wjMagzvS0vycMMkCYANIOGWTvqKqU6BlCSTjbFBywhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b910369c.mp4?token=eJ-ZYYqG0AYbXBDp8lJunYguH5Ju755sq3uUY3IOx9KDu203VKDyggR-qgM2PvZ4wTJGUgocUhjuuU8nhx53oKefGF36wSdt62Hpkpzk4TCUsVzX5JVAGY3tfY2Bz3nBNRUAUakbgg_PKhhTxQAHHMqo4BW-vKRmSjRsKVAvK9N_9zOHC06VK4BeWJx_dxNSHOf7s_Ajv8CQbspXBth1up13MmCUOCgMxvBxvGYCIcm-vgKGVJml87EUUWOlMCsxgiOPfkHVMaZPZog8nZtfIWXLliABknqEc30_KLKL10-wjMagzvS0vycMMkCYANIOGWTvqKqU6BlCSTjbFBywhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مسير انتحاري يحلق نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/84759" target="_blank">📅 03:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84758">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bd1820d4.mp4?token=ea7OOZHeitvdkar-tgy8RN06W91gi4aV0QcoDGMrU1PtljrJhKe_0V188ZXrhiszu4a9G4QTpXKcGPCvs4Sn5NvmNTKcP7wo3K4v-2A6ZGNYtqxvfkPvZI5h2tJ96VD8hc8Fitq0g32etwCJPWlniZGzzfSLKUTiTSnNVHGHEdcMdyOOlJp08VDmDQYdp1pU0byW_fjRQf2jVJPL4hhzhMrM4dj8O0qX6_VQvpxE4iovHuo6yRIKr_9jqT1bws3LUW03LQ4c8BcRec1tb1hDFqxB8z5qKR6c7_ORCNjEVhSBxEu15vgEVxxSh_btGEXABV1uOwxYaY1ZE0Gk4gHqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bd1820d4.mp4?token=ea7OOZHeitvdkar-tgy8RN06W91gi4aV0QcoDGMrU1PtljrJhKe_0V188ZXrhiszu4a9G4QTpXKcGPCvs4Sn5NvmNTKcP7wo3K4v-2A6ZGNYtqxvfkPvZI5h2tJ96VD8hc8Fitq0g32etwCJPWlniZGzzfSLKUTiTSnNVHGHEdcMdyOOlJp08VDmDQYdp1pU0byW_fjRQf2jVJPL4hhzhMrM4dj8O0qX6_VQvpxE4iovHuo6yRIKr_9jqT1bws3LUW03LQ4c8BcRec1tb1hDFqxB8z5qKR6c7_ORCNjEVhSBxEu15vgEVxxSh_btGEXABV1uOwxYaY1ZE0Gk4gHqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تستمر في التصدي للعدوان الأمريكي</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/84758" target="_blank">📅 03:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84757">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1162dff92.mp4?token=TKlLXS8uqSYfoCO7aZrE3nnZq-KSxtM_2wqzuQJAIbuyhfQqbXZ9vg2F0x01yWH5yxnjGLfVs9yZuz3RnBjMNejzNu3-r5oOYrbn7vRguufie-HVtZ54gURpQOYp5AwcuOxyU_BJWhwqd3IzoKg6TbF4ITJrkmTsma6t1T-Hchlj7Yyr56zhh9Vi1pXfWUYdEkapKpULaE5IrLYMeju4KV9YEmvrRGNxz9K_HFxqufFoShJ4igu09Lo7LD1kCn_L0062e_BMUNeUTi-Mufej6c163pU1csv2hMXtDjs8nEaFw03QdgP-dkgvhucR02XzmsDnFmzlCZ8ehzj5q1aZmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1162dff92.mp4?token=TKlLXS8uqSYfoCO7aZrE3nnZq-KSxtM_2wqzuQJAIbuyhfQqbXZ9vg2F0x01yWH5yxnjGLfVs9yZuz3RnBjMNejzNu3-r5oOYrbn7vRguufie-HVtZ54gURpQOYp5AwcuOxyU_BJWhwqd3IzoKg6TbF4ITJrkmTsma6t1T-Hchlj7Yyr56zhh9Vi1pXfWUYdEkapKpULaE5IrLYMeju4KV9YEmvrRGNxz9K_HFxqufFoShJ4igu09Lo7LD1kCn_L0062e_BMUNeUTi-Mufej6c163pU1csv2hMXtDjs8nEaFw03QdgP-dkgvhucR02XzmsDnFmzlCZ8ehzj5q1aZmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية في العاصمة طهران</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/84757" target="_blank">📅 03:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84756">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2e324717.mp4?token=gBGmdQpyiwXZWM6UJ5fTAfHh5ssZ2EzwKU8gP3qskcio285Jkv7oSz1Zm2P4C2uscyHlTrcF7DYD8tmbRY3cP7kRm9Ludxz_BU12QrMvnC-DBic5zzvSMxgnCgAgwGFv-acYAjjDpIeMwYR001AEX_ukW0C8fJIJolWjMA1S6ZoR62dE3p2fLJDrxnm4rqAdKHQBtDmMYCl-Q-VKiPBtYN-qDzmQolS_3o7_Msut93MLmCdITHVggj3SSflIbXVdWcoRCL5QwE_voBwbCzWbaHgSwVYf6N_HyfYi0--VMBaWdi8he9M09D71NkRpGBya-3kFn75W919WSV1O2c2kww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2e324717.mp4?token=gBGmdQpyiwXZWM6UJ5fTAfHh5ssZ2EzwKU8gP3qskcio285Jkv7oSz1Zm2P4C2uscyHlTrcF7DYD8tmbRY3cP7kRm9Ludxz_BU12QrMvnC-DBic5zzvSMxgnCgAgwGFv-acYAjjDpIeMwYR001AEX_ukW0C8fJIJolWjMA1S6ZoR62dE3p2fLJDrxnm4rqAdKHQBtDmMYCl-Q-VKiPBtYN-qDzmQolS_3o7_Msut93MLmCdITHVggj3SSflIbXVdWcoRCL5QwE_voBwbCzWbaHgSwVYf6N_HyfYi0--VMBaWdi8he9M09D71NkRpGBya-3kFn75W919WSV1O2c2kww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية في العاصمة طهران تتصدى للاجسام المعادية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/84756" target="_blank">📅 03:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84755">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مصدر إيراني: لاوجود لعدوان على ميناء سيريك جنوبي البلاد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/84755" target="_blank">📅 03:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84754">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مجددا تفعيل الدفاعات الجوية في طهران</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84754" target="_blank">📅 03:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84753">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b702c516d3.mp4?token=cNKaxROoN7WEuYOarEaQTtqGfdq_Uj1sE9NBpFteqWRZXPdNtj9hDr5hv0OqKeRgLIyS90gR0VwQhDRagdfvwAHnBGtH7spR0eyBkTWvWCaVX0AT5ObPSNHDBuAR036O0Sd0hYOS1OSgUJetk0Euc5v5w89oY2GN8g6RytQTJt4xYG1jml4Ypawkof6WdnAhqE1zbBXuXJDoSPbhXnovlMHG51DH5DFDFWeGr-VvuJyph-2H77H44BmtIGZCaTKxwv9d7BPNCR6oG6bTspsyRHNovKQaDsH-AAddG9ehb-tZbHw8lmgHcyvz4NFV-zo6J70vcKoNOdCxrywYbS1Plg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b702c516d3.mp4?token=cNKaxROoN7WEuYOarEaQTtqGfdq_Uj1sE9NBpFteqWRZXPdNtj9hDr5hv0OqKeRgLIyS90gR0VwQhDRagdfvwAHnBGtH7spR0eyBkTWvWCaVX0AT5ObPSNHDBuAR036O0Sd0hYOS1OSgUJetk0Euc5v5w89oY2GN8g6RytQTJt4xYG1jml4Ypawkof6WdnAhqE1zbBXuXJDoSPbhXnovlMHG51DH5DFDFWeGr-VvuJyph-2H77H44BmtIGZCaTKxwv9d7BPNCR6oG6bTspsyRHNovKQaDsH-AAddG9ehb-tZbHw8lmgHcyvz4NFV-zo6J70vcKoNOdCxrywYbS1Plg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الامريكي على محافظة خوزستان جنوبي إيران</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84753" target="_blank">📅 03:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84752">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4135d4c5e6.mp4?token=ctgm7rfdZKC01axZq7PFP3zwG0xrATO0w2LjTnSvtzZ6xRNZzw_KcxA99JlRoDDt9hgZzZHpwLpHbF-srdzEsqhfm_reuWHVFR-yJfQgy7JfNkHPr2Nk3_l4nGyPGFoZT3sEvBiiPRT0B2aBC9updEITzYP2aIbVNdeSR215bceW1elsx50IoAVii1Y3_n9Mh3pXPIGQwhWCN4HM-H7ZSxKrreYwLHKhtSmjZAYXsBDF73MWe8AXJMcI2m9znhIHlUMtNfiDla7CJc25qD0oONFQAM91U72Z0Dg5Ww9dUHScAkZgHEDioanOzN4sXqivXdkebCNlI3PGnWi9wkSLRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4135d4c5e6.mp4?token=ctgm7rfdZKC01axZq7PFP3zwG0xrATO0w2LjTnSvtzZ6xRNZzw_KcxA99JlRoDDt9hgZzZHpwLpHbF-srdzEsqhfm_reuWHVFR-yJfQgy7JfNkHPr2Nk3_l4nGyPGFoZT3sEvBiiPRT0B2aBC9updEITzYP2aIbVNdeSR215bceW1elsx50IoAVii1Y3_n9Mh3pXPIGQwhWCN4HM-H7ZSxKrreYwLHKhtSmjZAYXsBDF73MWe8AXJMcI2m9znhIHlUMtNfiDla7CJc25qD0oONFQAM91U72Z0Dg5Ww9dUHScAkZgHEDioanOzN4sXqivXdkebCNlI3PGnWi9wkSLRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية في سماء العاصمة الإيرانية طهران</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/84752" target="_blank">📅 03:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84751">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تفعيل الدفاعات الجوية في سماء العاصمة الإيرانية طهران</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/84751" target="_blank">📅 03:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84750">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79adcc2835.mp4?token=fBHaK3_c62wleAZhySCJffTeX66_8Ky7yaFnZRV5Dn-IcGqrsrsK6t4AibXLjVdLDIp-Pt6OIXMaTWBd7i9S3d8JU2UlixVHgulM6LshxV7eh_9ENluJKNE5IChrtUExd3eBFSX2cMTUX9PpQYq5OmTJLn5rLwMR_UGowtyDuPqZG9_YAP0WfXwW2EqVRzLW-Ep4AFnZbd4cb80VUjJNnY2nnzjPzNL6kxbCyXWuS6iRMIO-2jWIfafgMSRrCX3528esO_0wXUB1BskJZdszpIEdbTx0va-YGBrG3TEy-YcIlPefD3SNASKGdzLeJGu-iGhCI1bBblXaARR5oSJArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79adcc2835.mp4?token=fBHaK3_c62wleAZhySCJffTeX66_8Ky7yaFnZRV5Dn-IcGqrsrsK6t4AibXLjVdLDIp-Pt6OIXMaTWBd7i9S3d8JU2UlixVHgulM6LshxV7eh_9ENluJKNE5IChrtUExd3eBFSX2cMTUX9PpQYq5OmTJLn5rLwMR_UGowtyDuPqZG9_YAP0WfXwW2EqVRzLW-Ep4AFnZbd4cb80VUjJNnY2nnzjPzNL6kxbCyXWuS6iRMIO-2jWIfafgMSRrCX3528esO_0wXUB1BskJZdszpIEdbTx0va-YGBrG3TEy-YcIlPefD3SNASKGdzLeJGu-iGhCI1bBblXaARR5oSJArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات في تبريز</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/84750" target="_blank">📅 03:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84749">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ec35fbe5.mp4?token=EFqFn_PVJDuSTAvX6oR2Sa8L1URDh16200bZ59kF32nJk2ACb0eLuH7i47O82rAhwxzOXnE2NiwVfjvl0e6lfN2IrwIc6mvfwUOi1dDBokZ3RfXqx1MyJh5GM1aSDphtf9_cl31omCXn8Aan2ZkkASAnvMZBSQll51U8gg8o6siGHyJhnqRcsGIX8HJi_-6tvqmAEFzMSeYDVQVpYPgJ_--QwM1Dz7hXdSUsmmXNpNK2ixT6snDT-3oGKp6Rsf-jOH2nuhaA2pV3xQ2A8ws9J98B_30rauogZLyJgfHekURbjs8aU8TUtOhFsh_MJvSxDE-OJPegdgqLtUSHvJEWpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ec35fbe5.mp4?token=EFqFn_PVJDuSTAvX6oR2Sa8L1URDh16200bZ59kF32nJk2ACb0eLuH7i47O82rAhwxzOXnE2NiwVfjvl0e6lfN2IrwIc6mvfwUOi1dDBokZ3RfXqx1MyJh5GM1aSDphtf9_cl31omCXn8Aan2ZkkASAnvMZBSQll51U8gg8o6siGHyJhnqRcsGIX8HJi_-6tvqmAEFzMSeYDVQVpYPgJ_--QwM1Dz7hXdSUsmmXNpNK2ixT6snDT-3oGKp6Rsf-jOH2nuhaA2pV3xQ2A8ws9J98B_30rauogZLyJgfHekURbjs8aU8TUtOhFsh_MJvSxDE-OJPegdgqLtUSHvJEWpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية في طهران</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/84749" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84748">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تفعيل الدفاعات الجوية في مدينة تبريز</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/84748" target="_blank">📅 03:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84747">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الجيش الامريكي: ‏
بدأت قوات القيادة المركزية الأمريكية (سنتكوم) اليوم، في تمام الساعة السابعة مساءً بتوقيت شرق الولايات المتحدة، شنّ غارات جوية على أهداف عسكرية في إيران لليلة الحادية عشرة على التوالي. وتهدف هذه الغارات إلى مواصلة تقويض قدرة إيران على تهديد الملاحة التجارية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/84747" target="_blank">📅 03:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84746">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تفعيل الدفاعات الجوية في بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/84746" target="_blank">📅 03:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84745">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa639c99e4.mp4?token=Ac3WPJselOEpwdKRaszfDTGYd_x20ylpdo5FhFqqetsfH8n5Gw3mvFoOVeDISZ1rakYzaAHj0hgkU-g9TyLPZPD14m_ZIpcbmT4xr0J-WSLC67E3-BNkS60hgmync2ImW_GhqiQyMVH-Ejd9zIVnxDLdYkpRKSA3N-zVKWe4it7V232h-TogBFAe9JxKOWHc1plgYluuJh1Wnx-64YL9kWrtxOBS1J1YBqKZ5U_IMWEUzwT2bhJI6pfDRKLAQhFfVnjLzsct69md2XEiPPqbi5QTNlXao8D5BgNSxPHFppeeydGP7FouRxNLP4iA5DssrrgceKKFMykZ8NHZkLWkKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa639c99e4.mp4?token=Ac3WPJselOEpwdKRaszfDTGYd_x20ylpdo5FhFqqetsfH8n5Gw3mvFoOVeDISZ1rakYzaAHj0hgkU-g9TyLPZPD14m_ZIpcbmT4xr0J-WSLC67E3-BNkS60hgmync2ImW_GhqiQyMVH-Ejd9zIVnxDLdYkpRKSA3N-zVKWe4it7V232h-TogBFAe9JxKOWHc1plgYluuJh1Wnx-64YL9kWrtxOBS1J1YBqKZ5U_IMWEUzwT2bhJI6pfDRKLAQhFfVnjLzsct69md2XEiPPqbi5QTNlXao8D5BgNSxPHFppeeydGP7FouRxNLP4iA5DssrrgceKKFMykZ8NHZkLWkKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية في طهران</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/84745" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84744">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات عنيفة عند الحدود العراقية الإيرانية سمع دويها في محافظة السليمانية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/84744" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84743">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
البنتاغون: تحديد هوية جندي يعتقد أنه قتل في هجوم للعدو على قاعدة موفق السلطي الجوية في الأردن يوم 17 يوليو.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/84743" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84742">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجارات في مدينتي ماهشهر وبهبهان وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84742" target="_blank">📅 02:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84741">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2358442cb9.mp4?token=RWsvN3tPc52qPEdEG09NKN3h0kdUT0vB9-u0MO7XznrGv2iZA8qURaGQy2Vtnh-Cf5R1VBlIRifzokEo5rfcqWZXVMtDVgd1rk5jp2p1xoTgW3P7-rtmsER115bTux-YVz8dKi4jexUV3ycri7tLi4V1glIFZQoBErjvb0nrRn1-o54a1zq9IKtkNNNFi4yEExE-aIlAs68tSp5uBcc2EWJYglS2O6Mrw_7aQ_Ahttz8sXGCBPWZa-tVrbhGzjzrrKcEgtFLOV04zKwzju8v3qUgDe-0ynvgkUI7DtCZxXxb3VxYLnaMwezLQwqfu9yT4V3tDOpvFy6uRTZpVaIpyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2358442cb9.mp4?token=RWsvN3tPc52qPEdEG09NKN3h0kdUT0vB9-u0MO7XznrGv2iZA8qURaGQy2Vtnh-Cf5R1VBlIRifzokEo5rfcqWZXVMtDVgd1rk5jp2p1xoTgW3P7-rtmsER115bTux-YVz8dKi4jexUV3ycri7tLi4V1glIFZQoBErjvb0nrRn1-o54a1zq9IKtkNNNFi4yEExE-aIlAs68tSp5uBcc2EWJYglS2O6Mrw_7aQ_Ahttz8sXGCBPWZa-tVrbhGzjzrrKcEgtFLOV04zKwzju8v3qUgDe-0ynvgkUI7DtCZxXxb3VxYLnaMwezLQwqfu9yT4V3tDOpvFy6uRTZpVaIpyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في تشابهار وتبريز جنوب شرق وشمال غرب إيران</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84741" target="_blank">📅 02:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84740">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تفعيل الدفاعات الجوية في بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/84740" target="_blank">📅 02:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84739">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجارات في تشابهار وتبريز جنوب شرق وشمال غرب إيران</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/84739" target="_blank">📅 02:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84738">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجارات في قشم</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/84738" target="_blank">📅 02:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84737">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات في تشابهار وتبريز جنوب شرق وشمال غرب إيران</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/84737" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84736">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات في تشابهار وتبريز جنوب شرق وشمال غرب إيران</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84736" target="_blank">📅 02:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84735">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
مصدر إيراني: لاوجود لحدث أمني في العاصمة طهران حتى اللحظة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84735" target="_blank">📅 02:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84734">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله أكبر
موجة صاروخية تنطلق من إيران نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84734" target="_blank">📅 02:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84733">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات في مدينتي ماهشهر وبهبهان وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/84733" target="_blank">📅 02:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84732">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9eBauFW3n1Tg4o6lz5DnQcYjFnOB-z4enA-ngxEFqZI7eePiuN4vOLowLkYfdnM2dCOymvMzL6SreJ-CDHtXB5xFnrgK6FnzEEwm8FCV0fA_Q0mBcha6aQrKJ4L3Vcd2C6fgB8OOWqLvmAPIYCgGO4ofROzJeEY-drWTazq0urKrZovoI7KjHGbvQVsQsuvpFtiS08SCvbeqCm7Ni0oPzMAH94u_rPO2B2SWFyjCLDRssH3bCY2_OO1NG4nhdCdoFPJZd81m3B5Q5IcLFwSXgZLom0GCeu0954Hbuj4K3sjh7R1sGOHHjbxqNgO4CtfLlGTMHCvNG183dmTODLd_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84732" target="_blank">📅 02:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84731">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/84731" target="_blank">📅 02:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84730">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK98yO1bFohA4uueT3DH3iGW0vKCKqa7mwWQsyEsUxJwSSMysNblW06S-aVd7fOuah894hdQki-c3Ygi3dL_EAvCjR7SJsNRBRvRMtCV3txyb-c6EPbXCfaVVuDrb4s3tYh2622DoIssw50BqUbPergYDrjedRDyFLPEoA7NPXuYulzhmicSshZEsh24kIYe8PTvH04d4pNnmWm0Pp0OAbK9_qrFWkaNlEMUtWB407siv4XGCNVhkbZ1D6C2XqyRWaDZ6Sz5K4LoRkJzzJ4RJG5vCANC3_U4xHm6WAUGiy6e3MqWNvpu896fsAX2eq8z0cTzsCXMcdvUzvUQfIbJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب:
اعتبارًا من 1 أغسطس 2026، ستظل جميع الأدوية الجنيسة المستوردة إلى الولايات المتحدة معفاة من الرسوم الجمركية بنسبة صفر بالمئة لمدة عامين، وبعد ذلك سترتفع الرسوم إلى 100% لمدة عام واحد، ثم إلى 200% بعد ذلك. يأتي هذا الإجراء بهدف إعادة توطين إنتاج الأدوية الجنيسة في أمريكا، مع فرض غرامة على الشركات التي تقرر عدم بناء المصانع والمعدات خلال الفترة الزمنية المحددة لها. يهدف هذا الإجراء إلى حماية شعب الولايات المتحدة. أما السياسة المتعلقة بالأدوية الحاصلة على براءات اختراع أو علامات تجارية أو مبتكرة، والتي حققت نجاحًا كبيرًا، فستبقى كما هي. ويجري حاليًا بناء منشآت صيدلانية على مستوى غير مسبوق في جميع أنحاء الولايات المتحدة الأمريكية. شكرًا لاهتمامكم بهذا الأمر! الرئيس دونالد جيه. ترامب»</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84730" target="_blank">📅 02:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84729">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-gEgmOtAsBm2dXfqoq3SUMs45Z-IBxyXScuCiNuhqvqTjwVEAkCZt3sS49Gts8H3TeEK5Ij1JpiDFgowRFH0M-cOKu57issY0Rwl14LR-1EU4MCZCJ8yrvQLfATIf2-TXfRYYLLYAIVLWDfL_OkcyAY-G3hV_JEOH3woI0FbKpt2d8AasL9T5ckW3TkJWHCyI84Z5Ka5Ti24AW2E4-DHf6s4csYA0FUdgRC3ebv2-SKnAJk4HjiowjBHImlTSDryJWzlbcT6zXq_5psfh0nODhvWIwHWrMIr-milXABPDPy94rjfE7Itp9EGbLFFOD35-CzKxKZsZ8vQy_wABYJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد إقلاعها بدقائق..
طائرة مدنية تعود إلى مطار النجف في العراق قبل دخولها الأجواء الإيرانية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/84729" target="_blank">📅 02:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84728">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭐️
ذا أتلانتيك:
‏قال شخصان مقربان من ترامب إنه قد يفكر في مرحلة ما في التخلي عن الحرب في محاولة أخيرة لمساعدة الحزب الجمهوري في صناديق الاقتراع.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84728" target="_blank">📅 02:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84727">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سماع دوي انفجار مجهول في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84727" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84726">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سماع دوي انفجار مجهول في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84726" target="_blank">📅 02:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84725">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e3e74b219.mp4?token=hpek9livGyKinmBOy-P4eQPtbb_eH1_wXXO4P_N0OgTIFXYb8_k6mpQGvVW6EVUnVkQM9HflUp9I11MIJDgkO7mh0y5zYV7aQKVat3fosbGoaGr9MnShb2XklDEhI7dU43lr3CmlVisZs7JA-t0EJVN8CsCjm997pJY3ljvB-m6mVrkUWEg4p5kQ9bzexe9X2RxFggbCe-V2WifWyB9-Y_7hZo8bQJqBh0SzQPQukatzSoZm5fluo9_B-vwxC6wI0BhUwkgEbjdTvTByK5gVDWPVEIPSsPMOThnQ8zRjMSlyO5RRraMJz2uJwceoxV5QxMz-xMR-1ccVZnwoVIKGDjx8O2ZGEV4S4n8kqFTYM9QpTOBmCyQKRrJawpHW7OTYzoVragcZC6KLzdU30iDKqP7Ox6YptVaoUyXXE7ZWjBCpwhxAG7GrZcYitIexKqD1J1IUlWOGONEVx1m3nFu7jW_6_8G9cG86xWViEfo1xkAjo7VIj1Ct99j6uDKpnC5JPbUP4j3bmPsN6FqV_LfaJMWjvRCQwGt4a7xv35xjUv6PKcnWssbsjPHc6X30CM4EKG6-zPdqM2Jjz_WapgnBXR-jx0UeSA89-xr_bgchJDgS6w_H3rHAAvZ9fyJzAqJS0gzuwlc03mtECvk1LphQmbImxZ0tliyU6V0ehbBJcGs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e3e74b219.mp4?token=hpek9livGyKinmBOy-P4eQPtbb_eH1_wXXO4P_N0OgTIFXYb8_k6mpQGvVW6EVUnVkQM9HflUp9I11MIJDgkO7mh0y5zYV7aQKVat3fosbGoaGr9MnShb2XklDEhI7dU43lr3CmlVisZs7JA-t0EJVN8CsCjm997pJY3ljvB-m6mVrkUWEg4p5kQ9bzexe9X2RxFggbCe-V2WifWyB9-Y_7hZo8bQJqBh0SzQPQukatzSoZm5fluo9_B-vwxC6wI0BhUwkgEbjdTvTByK5gVDWPVEIPSsPMOThnQ8zRjMSlyO5RRraMJz2uJwceoxV5QxMz-xMR-1ccVZnwoVIKGDjx8O2ZGEV4S4n8kqFTYM9QpTOBmCyQKRrJawpHW7OTYzoVragcZC6KLzdU30iDKqP7Ox6YptVaoUyXXE7ZWjBCpwhxAG7GrZcYitIexKqD1J1IUlWOGONEVx1m3nFu7jW_6_8G9cG86xWViEfo1xkAjo7VIj1Ct99j6uDKpnC5JPbUP4j3bmPsN6FqV_LfaJMWjvRCQwGt4a7xv35xjUv6PKcnWssbsjPHc6X30CM4EKG6-zPdqM2Jjz_WapgnBXR-jx0UeSA89-xr_bgchJDgS6w_H3rHAAvZ9fyJzAqJS0gzuwlc03mtECvk1LphQmbImxZ0tliyU6V0ehbBJcGs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مساعي فاشلة لإرهابيي المعارضة الكردية الإيرانية بإطفاء النيران داخل مقراتهم والإرتفاعات المحيطة بها في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84725" target="_blank">📅 01:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84724">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
🔻
🔻
راه مكة از كويت مى گذرد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84724" target="_blank">📅 01:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84723">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭐️
نيويورك بوست:
يرغب الرئيس الأمريكي دونالد ترامب في أن يصبح جانى إنفانتينو، رئيس الاتحاد الدولي لكرة القدم (فيفا)، الأمين العام للأمم المتحدة القادم.
يعتقد ترامب أن السمعة العالمية التي يتمتع بها إنفانتينو وخبرته في قيادة فيفا تجعله مرشحًا قويًا لخلاف أنطونيو غوتيريس.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/84723" target="_blank">📅 01:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84722">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/84722" target="_blank">📅 01:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84721">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/84721" target="_blank">📅 01:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84720">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc444ce4b9.mp4?token=NdNBc8OvTGeecfEhVe57dfU74riwLI5ZdPrFnsouYsbIQijwxIo2oWTIUo_TidI-YmJy952MEURmOvoDsKor54fJHjS5PB07O2rnAntIpZfICqL-FZqJIvIJ-tMJBDyntVmQha0KRU6Y0iZ5SYC0LDW5iwKryFI-C2jdhUbX2CD7qSTKlAYRpe_1aNOrXbfV067aL3DTn7eayR3od5uF6s6W89NUYzYNBK8mxJWJ4B1i7RBRAUofQq3e4diteonRqvoqQavaufuANt5KTdzRQGNELk4KhHIVL7XWgSF_zg3r2wW1c05Ae3pswhKjCA8Wq7qABGMLBc8Ux2foUmkmzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc444ce4b9.mp4?token=NdNBc8OvTGeecfEhVe57dfU74riwLI5ZdPrFnsouYsbIQijwxIo2oWTIUo_TidI-YmJy952MEURmOvoDsKor54fJHjS5PB07O2rnAntIpZfICqL-FZqJIvIJ-tMJBDyntVmQha0KRU6Y0iZ5SYC0LDW5iwKryFI-C2jdhUbX2CD7qSTKlAYRpe_1aNOrXbfV067aL3DTn7eayR3od5uF6s6W89NUYzYNBK8mxJWJ4B1i7RBRAUofQq3e4diteonRqvoqQavaufuANt5KTdzRQGNELk4KhHIVL7XWgSF_zg3r2wW1c05Ae3pswhKjCA8Wq7qABGMLBc8Ux2foUmkmzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد قريبة جدا من مكان الذي استهدف بطائرة مسيرة في جبل ازمر بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/84720" target="_blank">📅 01:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84719">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
وول ستريت جورنال:
واشنطن طلبت من إسرائيل البقاء خارج الصراع مع إيران في الوقت الحالي.
دول في المنطقة تمارس ضغوطاً على الولايات المتحدة لضمان عدم شن إسرائيل هجمات على إيران.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/84719" target="_blank">📅 00:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84717">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e3a9751d.mp4?token=QZ0e2RzteKl0ayjRZuzvFYAVNZnkOTHOp-7VcEXhHS22q9afonOx0bnIXTm6Ud6j3hvHOcgXICzjSXuzoDdyOuW-Q8LM2FkzgpbPExbj9IB7qPgpQkEY2kX3RZ4keod1BQDDUOmXa0JrCzb9dLA0NF2xQdn7QH8evLuXgcSRQn7J3a8heKv7WqetI5IUS9UNTp4SkfFGc9v4vY2l59bynrNKjqZE6ykQ5Z3YNGzxKiqmpnJ9wPoqQHh2jI7SO8LsOYvB8nGhss0_TH3lgaKaqUvD-GXtrGpzSCaW0-hQn437YjNU1NuAjZ4PcJfbilZVTpgGMinOVMOeykTmuIhPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e3a9751d.mp4?token=QZ0e2RzteKl0ayjRZuzvFYAVNZnkOTHOp-7VcEXhHS22q9afonOx0bnIXTm6Ud6j3hvHOcgXICzjSXuzoDdyOuW-Q8LM2FkzgpbPExbj9IB7qPgpQkEY2kX3RZ4keod1BQDDUOmXa0JrCzb9dLA0NF2xQdn7QH8evLuXgcSRQn7J3a8heKv7WqetI5IUS9UNTp4SkfFGc9v4vY2l59bynrNKjqZE6ykQ5Z3YNGzxKiqmpnJ9wPoqQHh2jI7SO8LsOYvB8nGhss0_TH3lgaKaqUvD-GXtrGpzSCaW0-hQn437YjNU1NuAjZ4PcJfbilZVTpgGMinOVMOeykTmuIhPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد قريبة جدا من مكان الذي استهدف بطائرة مسيرة في جبل ازمر بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84717" target="_blank">📅 00:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84715">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCYfhQlZfk3qGjZyRPyr2cAnxPtk44Clafx1LwCRvB_HIjY0FDM5Kxo7AUWYWIKxnQu5LimG6pzKFjQRvaW4LhEsKwZsqTAmt-jNzpGAAr7r3_Avfsf-5ZhZ0v1V37QUxeUDti9qsb0JfE_IG30BgCpgsHr73eToSR-tfemcSzV30fnYAgCefkz6f3uxuekCzbdATSyTxxmL4uG_KJ-1tBLXhuZJ4I7VaNBwvJwHd6YVk1b3yKIpw5HM0u4nhLKGlsG7NWNrEDdDONvvfxPfQqwy7KLZjr8AsDBQ2Nvy1m4k1b_xJY5vMuoMq2B3ihh2dQxNcTO-AQ3N285inOhG3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7434eecc7.mp4?token=aVRCALKsIW3NWbqPA0XURYd1-oUH3lFR5zZJnkzDNcZBny_acO8AKb0rFAu2wXxAdkQu_1Ggrio83N1YzzrJsA9LMPvn3Zm9pC0eSF5Rl9VIsKNz0sDMRakBlpOoveKec5o0PY_CqTAf2do_QH8qlrvW-DFs70h5f-YSkpcbgaWUqQLobguoVSNGyBylW2dkAUQvuMuKl8AMG9v_MqclB6BGrZxm8zev1qYo1CscF9-3QRmDZQ7BNTjGQ1bfGK_BifomuAOl9hlrRkAv7J-ON3CqNkiA9qQRI1xh9dXKK3Qs2rDdAlFkIfRL7hvrzUFY2jEXH9B6oluiVcXm3sF3Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7434eecc7.mp4?token=aVRCALKsIW3NWbqPA0XURYd1-oUH3lFR5zZJnkzDNcZBny_acO8AKb0rFAu2wXxAdkQu_1Ggrio83N1YzzrJsA9LMPvn3Zm9pC0eSF5Rl9VIsKNz0sDMRakBlpOoveKec5o0PY_CqTAf2do_QH8qlrvW-DFs70h5f-YSkpcbgaWUqQLobguoVSNGyBylW2dkAUQvuMuKl8AMG9v_MqclB6BGrZxm8zev1qYo1CscF9-3QRmDZQ7BNTjGQ1bfGK_BifomuAOl9hlrRkAv7J-ON3CqNkiA9qQRI1xh9dXKK3Qs2rDdAlFkIfRL7hvrzUFY2jEXH9B6oluiVcXm3sF3Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجلات الاسعاف والاطفاء تتجه الى مكان السقوط في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84715" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84714">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8ce3ff08.mp4?token=PgSdRHgICV9uQ9uIH83c55UH8kDUWf6bnK70NvxerLuAScWAHZqNlqmX6BX-R2nbmXrYLSR1OHuzyr0c4qQWoOYDZitsVjbxiMMIzahA_adMdkXOab9t_5Wy7gXSVzY2VsrVr-c2Vn2mWdcDU1RCvkmYoInIrQEKDu2G4PSDgwsCsccjU5oEez-OKn_5NiQXQL1ePHTMs_3IxgU3jhlVIUtNBqXRu7Dghh6-2jsauU_Tulvm72DI4pw9qjvtlxzkyHufIAs1_HWTgFGNIFWbG7nifuRuNLxCSTRXA1x2NEh-TK6s8hlVj-sU1ezZ65jZYlDhuooegBxPQuNvhYUV0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8ce3ff08.mp4?token=PgSdRHgICV9uQ9uIH83c55UH8kDUWf6bnK70NvxerLuAScWAHZqNlqmX6BX-R2nbmXrYLSR1OHuzyr0c4qQWoOYDZitsVjbxiMMIzahA_adMdkXOab9t_5Wy7gXSVzY2VsrVr-c2Vn2mWdcDU1RCvkmYoInIrQEKDu2G4PSDgwsCsccjU5oEez-OKn_5NiQXQL1ePHTMs_3IxgU3jhlVIUtNBqXRu7Dghh6-2jsauU_Tulvm72DI4pw9qjvtlxzkyHufIAs1_HWTgFGNIFWbG7nifuRuNLxCSTRXA1x2NEh-TK6s8hlVj-sU1ezZ65jZYlDhuooegBxPQuNvhYUV0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جبل ازمر الذي يضم عدة مقرات للاحزاب المعارضة تلتهمه النيران</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84714" target="_blank">📅 00:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84713">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اكسيوس : ترامب يتعهد بأن الولايات المتحدة ستقصف قريباً جبل الفأس الإيراني</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84713" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84711">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632a9e91b.mp4?token=qUdP2UKHVmuVuTa6EZdiV5YN4flmjF3GQLdGv6gjeHyJUFkGV4pqV7a1ZdaYRpjFQU8vxTa9D-wB4lw7CmSj9U1ofKlgNjoNIfDbmt-6PuFhGo2wj942T1Efi_PAQu9JCFKC3mZoaHoW-55dd9rvBtIML9_U6VfyvVcSh0_Rq_c2dFOJK4zlSZxVKtX2-nofSCMBXqWPG_ZX7hfucwrX9TLm9Ht3NhBTef2omuXQjIf00v-sdUdmvTMV5jXK1HuYoWmU-vjB9tK8mlfOY9yS5mZbR08OPHqiY0z8VN7H3-wdWoTxErS-72W5XIaPYLAiQKPhPbETADmdXkodITUIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632a9e91b.mp4?token=qUdP2UKHVmuVuTa6EZdiV5YN4flmjF3GQLdGv6gjeHyJUFkGV4pqV7a1ZdaYRpjFQU8vxTa9D-wB4lw7CmSj9U1ofKlgNjoNIfDbmt-6PuFhGo2wj942T1Efi_PAQu9JCFKC3mZoaHoW-55dd9rvBtIML9_U6VfyvVcSh0_Rq_c2dFOJK4zlSZxVKtX2-nofSCMBXqWPG_ZX7hfucwrX9TLm9Ht3NhBTef2omuXQjIf00v-sdUdmvTMV5jXK1HuYoWmU-vjB9tK8mlfOY9yS5mZbR08OPHqiY0z8VN7H3-wdWoTxErS-72W5XIaPYLAiQKPhPbETADmdXkodITUIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
حرائق لا تتوقف في التهام مقرات الاحزاب المعارضة في محافظة السليمانية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84711" target="_blank">📅 00:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84710">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYUwshu2YRhKYEdCuqfTcjxpvRUhATWnJ4Ou3NRFm7KVibIQBIe8avv32VgDUgqWDrzTD5953DGn3weSWBAtvnNhGUXd9wkcTBVdPXhDhMicw4jRZ-MJdUXBcx8OZ_n7ePe-mMQtNtPd_pmzfzmQAeZJkVsC3QkNCXcYms4jaYR0pEOhfPlEUhX3uJHJXh4cB9KL_vYG--72WnOQwOICC9Gl4z-7xQr4DOX0jquH9VRmZUooxgsAEjRQecD-EnaCDzMMUz0gSVkKCzpXSw0ZyUR-wMZD57PC9R3zbY3vqJQzad2fynWWQslry-moTSVCE_1i0DvSPn_a0q_RzhTZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مشاهد من احتراق مقرات المعارضة في محافظة السليمانية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/84710" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84709">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f411b0734.mp4?token=VJLh2Q5peMYBWb3qVMcQHnS_K0XzjeV18QMtJ_2R0cTE7JYEKdDfIldirLG2cmJSX2770kXcSZ_J0haZXEqgckLKaVPo11x9yIrbEbXmQHOxFsRuoxZvXSuEW5AbkDhypC-TNKv3dpLAv8nS0NUywyC9iZLTZdU2shURDvG17YXt2K7BVc_Wu6kR88DQU8lmYgaLmG9rspsn2uS5GxYLL_m_b4nlQBcf5Gy7_6MGJA1t7s9w4poJM_hjlZGphCTmijQolkEjoaegUlXE_wwtRU8jpESpsez8Abx7FejEc6N2NDazKv3q_GZ4qGV0WhAT0VkeA8t4qLafKR2N7YAfpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f411b0734.mp4?token=VJLh2Q5peMYBWb3qVMcQHnS_K0XzjeV18QMtJ_2R0cTE7JYEKdDfIldirLG2cmJSX2770kXcSZ_J0haZXEqgckLKaVPo11x9yIrbEbXmQHOxFsRuoxZvXSuEW5AbkDhypC-TNKv3dpLAv8nS0NUywyC9iZLTZdU2shURDvG17YXt2K7BVc_Wu6kR88DQU8lmYgaLmG9rspsn2uS5GxYLL_m_b4nlQBcf5Gy7_6MGJA1t7s9w4poJM_hjlZGphCTmijQolkEjoaegUlXE_wwtRU8jpESpsez8Abx7FejEc6N2NDazKv3q_GZ4qGV0WhAT0VkeA8t4qLafKR2N7YAfpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتعال النيران في مقرات الاحزاب المعارضة بمحافظة السليمانية</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84709" target="_blank">📅 00:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84708">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiNomfTm09Gw-joh3Y8sGwFjWmT6OcMAw64pImC8mNWUMYxKdtRvZMWB7F3LEX9oRWQoOgZBWiCgMOVmfp1SC-zXG8KmcQ2loKotI4To4zg4GC83725QD4Zi7Z0OUUxN3yxGgeWLOwvcGTsH_Ex7WUQ_hYRmIrIOMIMhKt57l6ZlvB6ZblMZzI3_MLUgxiEdO7rG71_6FBspEW_ZjOUMA1Z5czDbxEvix47F6i37QUEQFJa_DAiXTvogoKL_E1lmKG2t8wC5wYj1EwxE0gcj6DATtYIucNP3jSwOe6E-IYseijsa3zvUNKYb7mm2NF8XB2r8dlTBTUBrBDfpyGRRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
انفجارات في مقرات الاحزاب المعارضة بمحافظة السليمانية</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84708" target="_blank">📅 00:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84707">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
انفجارات في مقرات الاحزاب المعارضة بمحافظة السليمانية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84707" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84706">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e6b4d02d.mp4?token=E9Z3mV9h_0lrh7dhT_tV9bY2B_04sXmkyhp2X8Bcu6aeohsDOGtEklOcrUfLcZCfpq16-ZUz9yN8ul_D-pAdiMB2121Bjsm_VjJ4CBpmQ2J85Oi7ujaObfxFS3YRo39cknnRc1nVtqoyanFmjZ3sTQOJz0yENANT95CzeJIfYBFSVSSWLKy7dq4hsYR-oeln5GAI70M-DvVQiUmtGhRg08J4cuA67zJ3cElyrJEw8EDUZ_VmplrWm74eshIHCHgMD7gBE9cAQKfId1kIVuVyP32GerblisDw7f7I-NjY_PPSqdW_uo8cfaILYW3k0NbTfQCrgV4-pYsgRytFpYQ9EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e6b4d02d.mp4?token=E9Z3mV9h_0lrh7dhT_tV9bY2B_04sXmkyhp2X8Bcu6aeohsDOGtEklOcrUfLcZCfpq16-ZUz9yN8ul_D-pAdiMB2121Bjsm_VjJ4CBpmQ2J85Oi7ujaObfxFS3YRo39cknnRc1nVtqoyanFmjZ3sTQOJz0yENANT95CzeJIfYBFSVSSWLKy7dq4hsYR-oeln5GAI70M-DvVQiUmtGhRg08J4cuA67zJ3cElyrJEw8EDUZ_VmplrWm74eshIHCHgMD7gBE9cAQKfId1kIVuVyP32GerblisDw7f7I-NjY_PPSqdW_uo8cfaILYW3k0NbTfQCrgV4-pYsgRytFpYQ9EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇮🇱
بالتزامن مع زيارة جوزيف عون إلى الولايات المتحدة، شن الاحتلال الإسرائيلي غارة استهدفت احد بلدات قضاء الصور في جنوب لبنان.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84706" target="_blank">📅 23:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84705">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏دوربين: هل لديك تقدير جديد حول ما كلفتنا إياه الحرب حتى الآن في هذا الشهر الخامس من السنة الأولى لهذه الحرب في إيران؟
🇺🇸
‏وزير حرب: يا سيادة السيناتور، التقدير الذي لدينا حتى اليوم هو 37.5 مليار.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84705" target="_blank">📅 23:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84704">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cefall1jJsjadJL9udiIJEedL3X935PnCMw17b9MjleR4-FS_2pQ19Hz6LdAVwRkYmRcreW_mLGZI4LXI6Dwl17IDouVTSoWinzJGUOLOdlPgLABaAZDuQ1mSg3CEBGVP7JdrO6OdwNjQkc8ehJlPep5ZrPEVbB2nbnYMrjA4CilsQpedl5vIaJIOXVckGig5qMwKO_mvpOC6WoyMiTei4hMiNOqfnKzbi-lYGUp7kkdnmHYtd5PdRgI3hoAb1T_n4BStWlP_3HwuxEql-ruhvFTtETCGBsDjwUtN2-ARe0fdu-F5BnVbqTD2tIZMgveX_5TQqYGTEYuyMubeRddoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يقارن القتلى الاميركان في حرب ايران مع القتلى في الحروب الاخرى
.
حرب أفغانستان: 20 عاما، 2000 قتيل.
حرب العراق: 9 سنوات، 4600 قتيل.
حرب فيتنام: 19 عاما و5 أشهر، 58,220 قتيلا.
الحرب الكورية: 3 سنوات وشهر واحد، 36,574 قتيلا.
حرب فنزويلا: يوم واحد، يا ميت.
الصراع العسكري الإيراني: 4 أشهر، 18 قتيلا.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/84704" target="_blank">📅 23:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84703">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5c8eb918.mp4?token=O4xMm1RbtYvxPQbXQ5CoBpvPOPW5n27pVLThZCZtEQ6WRLgN4hO0ilvHVQ8DM9fnQl5AWIzSepW-Zxig9sWv6GFlkvu0wVhT1zN5bUUWU7WSvPv3JxpmBMyNR5EejyCzVjqnRODzR9FmVH2n65TelfLPCzFnI2lfc4in1E4VJAa-wMiCaPKNJMoPHotTwvUmn2AadRQJuztEVrQFRlOVv9RjlPuk0j8H-pjodTA8Ecg8RVe8UVvyg8TRTdWFOHsYC5srUUbjs71DNl4PIvgtJiWsGh8nSKInrt4xa2_sZfG7rfNQUyhNVudoGjR9E15lvSekqAAkQ_x19EeCvhV6iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5c8eb918.mp4?token=O4xMm1RbtYvxPQbXQ5CoBpvPOPW5n27pVLThZCZtEQ6WRLgN4hO0ilvHVQ8DM9fnQl5AWIzSepW-Zxig9sWv6GFlkvu0wVhT1zN5bUUWU7WSvPv3JxpmBMyNR5EejyCzVjqnRODzR9FmVH2n65TelfLPCzFnI2lfc4in1E4VJAa-wMiCaPKNJMoPHotTwvUmn2AadRQJuztEVrQFRlOVv9RjlPuk0j8H-pjodTA8Ecg8RVe8UVvyg8TRTdWFOHsYC5srUUbjs71DNl4PIvgtJiWsGh8nSKInrt4xa2_sZfG7rfNQUyhNVudoGjR9E15lvSekqAAkQ_x19EeCvhV6iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
دوربين
: هل لديك تقدير جديد حول ما كلفتنا إياه الحرب حتى الآن في هذا الشهر الخامس من السنة الأولى لهذه الحرب في إيران؟
🇺🇸
‏
وزير حرب:
يا سيادة السيناتور، التقدير الذي لدينا حتى اليوم هو 37.5 مليار.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84703" target="_blank">📅 23:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84702">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
رئيس هيئة الأركان المشتركة الأميركية: نحن بحاجة لـ 1.5 تريليون دولار لمواجهة التحديات العسكرية المستقبلية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/84702" target="_blank">📅 23:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84701">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
رئيس هيئة الأركان المشتركة الأميركية:
نحن بحاجة لـ 1.5 تريليون دولار لمواجهة التحديات العسكرية المستقبلية</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84701" target="_blank">📅 23:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84700">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
مجلس الوزراء العراقي يصوت على إنهاء تكليف رئيس مجلس الخدمة العامة الاتحادي ونائبه من مهمات منصبيهما.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/84700" target="_blank">📅 23:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84699">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE32awyXQ53DqP8UoE4pLwu1XxJofs7q8r3VT19i2EEX0Xvh-x44CvQzGmVxAY4khEGPM-z35GmiSdKwKxfprEvCqaGG_VZZeGduCI6fKh7zEqKG0XXQuTCvmTfr4O3MdvuiFxAzZU5I9GurWM6PDIgcDDr_6EFzPaG7g0JGTpvsaDuknXBk6jfJb-kDBMMFLpkKLmakUGruLTp9vuX-kbw8FQ5Nckk0dbGJgqYH9Nt5Kc9JR4OuECSYh73frmINtlJgL2mc7WL1bLJHiOpFWhBQ80pbYtDpXC-MC_eZxCr9NG9IE9uIvQ0YkP583XwSC9mUhcqkigoKhRBiLGd5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يعلن عن افتتاح خط جوي مباشر بين لبنان وأمريكا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/84699" target="_blank">📅 22:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84698">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
العلاقات العامة للحرس الثوري الإسلامي:
في إطار استمرار الموجة الرابعة والعشرين من عملية نصر 2 واستمرار تطهير المنطقة من الرادارات، قام جنود الحرس الثوري البواسل بتدمير وتعطيل رادار إنذار مبكر، ومجمع رادار تكتيكي حول قاعدة علي السالم، ونظام رادار آخر في جزيرة بوبيان بالكويت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/84698" target="_blank">📅 22:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84697">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
وزير النفط العراقي:
القيمة الإجمالية للصفقات الموقعة مع الشركات الأميركية خلال زيارة رئيس الوزراء لواشنطن تقدر بنحو 200 مليار دولار.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/84697" target="_blank">📅 22:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84696">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/557ac7f23a.mp4?token=HFZ_pwDAfPLg3xA_5f2kF_Dj_N8C6Wed_j7QEL_gXqJgD6aCvRGMTBYMq28-yQbq-8369FVl2AvSbeSbbe0MDHOgxMo7tqX8j0kBVMUesQcAgZyJBvdKsY8aFrgbys9PGRdFwnUiqjST0AWltSvMATTP-ZBzEk7BXZFT6a9mIWMZFKnl7gDK9FQgUvdrhUY-CAev6bFVDOpWj9ITASNQ2fjaZZvt-JpuFLNcPt7hMwyMQSwDyET9agguW4LrR78-rT0P6WQZ-q6SZJC0syVG7YqZI1rrf5VEVb27DeUe5Pu3ZOc25i8KHJh-mhrtoODoPPNoJ_ZN774B5TLeXFof5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/557ac7f23a.mp4?token=HFZ_pwDAfPLg3xA_5f2kF_Dj_N8C6Wed_j7QEL_gXqJgD6aCvRGMTBYMq28-yQbq-8369FVl2AvSbeSbbe0MDHOgxMo7tqX8j0kBVMUesQcAgZyJBvdKsY8aFrgbys9PGRdFwnUiqjST0AWltSvMATTP-ZBzEk7BXZFT6a9mIWMZFKnl7gDK9FQgUvdrhUY-CAev6bFVDOpWj9ITASNQ2fjaZZvt-JpuFLNcPt7hMwyMQSwDyET9agguW4LrR78-rT0P6WQZ-q6SZJC0syVG7YqZI1rrf5VEVb27DeUe5Pu3ZOc25i8KHJh-mhrtoODoPPNoJ_ZN774B5TLeXFof5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇺🇸
مشاهد من الأقمار الصناعية ترصد تدمير محطة الدعم الأرضي وصيانة المنطاد في قاعدة الاحتلال الأمريكي بمحافظة أربيل شمالي العراق، إثر استهدافها بالصواريخ الإيرانية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/84696" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84695">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تعليق العمل بمطار أربيل</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/84695" target="_blank">📅 22:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84694">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a1201641.mp4?token=vTm-uV38_Zk3S2nznDeLWRaBzarudMFRIKx_sWXgB4M8RPkdOg56HzdA1YNn-G7x9diKHWy6rL7ggpmKtoaaOuQBR5Y02k81shBjbaJhZQnpx8AdoST2HN4vRnApJ04YEE-7kNKYAXY6R7MPKnyphlW9s6QWtFI44NDoLmUAEHlGbh-c31DTE_ZgF3KShJA2j5JFEG8A5DD2VdY1XfCYKho0UXBsC8Wop7VJppZy68YXMyfnHVbySGD9yF1zhwckXQN7TJOopHMMRdFd65xgXYX0aWuwg-ZjCTD7z_7UMLStHqFN39D_q0vMqjiheDnqSYnBebJHHFVirdctMlUBGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a1201641.mp4?token=vTm-uV38_Zk3S2nznDeLWRaBzarudMFRIKx_sWXgB4M8RPkdOg56HzdA1YNn-G7x9diKHWy6rL7ggpmKtoaaOuQBR5Y02k81shBjbaJhZQnpx8AdoST2HN4vRnApJ04YEE-7kNKYAXY6R7MPKnyphlW9s6QWtFI44NDoLmUAEHlGbh-c31DTE_ZgF3KShJA2j5JFEG8A5DD2VdY1XfCYKho0UXBsC8Wop7VJppZy68YXMyfnHVbySGD9yF1zhwckXQN7TJOopHMMRdFd65xgXYX0aWuwg-ZjCTD7z_7UMLStHqFN39D_q0vMqjiheDnqSYnBebJHHFVirdctMlUBGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر... اصابات مؤكدة في صفوف جيش الاحتلال الاميركي بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/84694" target="_blank">📅 22:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84693">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تعليق العمل بمطار أربيل</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/84693" target="_blank">📅 21:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84692">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اصابة بناية السفارة الصهيونية في البحرين بمسيرة</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/84692" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84691">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/84691" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84690">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/84690" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84689">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765c241b7a.mp4?token=rsebvF48QEVX28gpBNU8bXrZMBuAsunxY_4KzETUrK4IF_JgTrYbGr7wMVCX858BaaMHbNjpTuKehhlH4hEMyiUHkhjstL_4f5vhSUlV40jy7tLiNu5_eB8lGFcifRElGsjIHJm2wc557WvGzShk73Mi-CbuBYtP0Mo4ji1-Ct6K3d7cx1z0XWjLdIyeUQU-dQ_uOVO7ym6nJrKYoRUzwWd99D7L79pKtXUixwI0t5oC8jQer0sXpsifm6YQEWXhT8nw_R3YCr2GI-1zK4lC5yfWa96t8p4FLwewRw1yZdh3JGV3-br-9E9UhoLqHL4Bki5HOewDz2WxW0OUi6WVyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765c241b7a.mp4?token=rsebvF48QEVX28gpBNU8bXrZMBuAsunxY_4KzETUrK4IF_JgTrYbGr7wMVCX858BaaMHbNjpTuKehhlH4hEMyiUHkhjstL_4f5vhSUlV40jy7tLiNu5_eB8lGFcifRElGsjIHJm2wc557WvGzShk73Mi-CbuBYtP0Mo4ji1-Ct6K3d7cx1z0XWjLdIyeUQU-dQ_uOVO7ym6nJrKYoRUzwWd99D7L79pKtXUixwI0t5oC8jQer0sXpsifm6YQEWXhT8nw_R3YCr2GI-1zK4lC5yfWa96t8p4FLwewRw1yZdh3JGV3-br-9E9UhoLqHL4Bki5HOewDz2WxW0OUi6WVyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استمرار ارتفاع اللسنة اللهب من مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/84689" target="_blank">📅 21:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d4c16950.mp4?token=L2__-alkM92FQ54upUbpa6drMFZCSClZ8ctG0xyeKLs6FKLIItri_3nwLNdcngTQSVauhgzcJBy0fEl3CpiYVGMDL6VHi8RRk2JK_ZztN6SSrt0RvwzNx87enLT4mMgTzw5L_VRAiHWJr8nBav_yvHmLpwgMZf2rE398SdCVvnGWj8wEOi_FtZ4KSoesIkt5_57wZn2y7oycrDggCIPX7Chc5bD7lUD5FoWLrfoSPaCtkndmI9I1RWSU1ritzJBvxSUFCL-tiJZV2JBWWTyvOj6Pzo393v5g1V6HnKxHIqIOVmwub10DKvQyIw7B44P-o9gTJYHA3jX_JbAsP8EfYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d4c16950.mp4?token=L2__-alkM92FQ54upUbpa6drMFZCSClZ8ctG0xyeKLs6FKLIItri_3nwLNdcngTQSVauhgzcJBy0fEl3CpiYVGMDL6VHi8RRk2JK_ZztN6SSrt0RvwzNx87enLT4mMgTzw5L_VRAiHWJr8nBav_yvHmLpwgMZf2rE398SdCVvnGWj8wEOi_FtZ4KSoesIkt5_57wZn2y7oycrDggCIPX7Chc5bD7lUD5FoWLrfoSPaCtkndmI9I1RWSU1ritzJBvxSUFCL-tiJZV2JBWWTyvOj6Pzo393v5g1V6HnKxHIqIOVmwub10DKvQyIw7B44P-o9gTJYHA3jX_JbAsP8EfYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
النيران على مرمى البصر اثر سقوط المسيرات الايرانية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84688" target="_blank">📅 21:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
🇮🇷
اصابة مباشرة في موقع القاعدة الاميركية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84687" target="_blank">📅 21:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇶
النيران على مرمى البصر اثر سقوط المسيرات الايرانية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84685" target="_blank">📅 21:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dad9abeee3.mp4?token=F_1hjMMFg2dLcxLvWw_lSsSAy1AaXapkQg2DxvSHoi844p2qsETW4FkKuE7rjduE9GKsRK_BU2ZWlNDKj7qbgT6PRYuS-YNzDsivNRKW_BWr5fZ6iye-AeYL1Opp0uv0nLRfITlCY_WSGdPfbj2NO-hd4l_Axg_FyRqNIm1POqIWOTcaA8muJYCijMviG1g6-Fl-dmcIUUlKbmQ8j5Au5bnTy5tJAAWFrLTh7msfJmgklavcyh5fUcOnjAEm80cu6AkpruJYKcX4cQLY8eMa7IKYKMGQLrm9cdQV_lhoedDRZViZgt2Uu_m1TUWmYXqWYLRs6vXqJIEipifhVuSz3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dad9abeee3.mp4?token=F_1hjMMFg2dLcxLvWw_lSsSAy1AaXapkQg2DxvSHoi844p2qsETW4FkKuE7rjduE9GKsRK_BU2ZWlNDKj7qbgT6PRYuS-YNzDsivNRKW_BWr5fZ6iye-AeYL1Opp0uv0nLRfITlCY_WSGdPfbj2NO-hd4l_Axg_FyRqNIm1POqIWOTcaA8muJYCijMviG1g6-Fl-dmcIUUlKbmQ8j5Au5bnTy5tJAAWFrLTh7msfJmgklavcyh5fUcOnjAEm80cu6AkpruJYKcX4cQLY8eMa7IKYKMGQLrm9cdQV_lhoedDRZViZgt2Uu_m1TUWmYXqWYLRs6vXqJIEipifhVuSz3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
اصابة مباشرة في موقع القاعدة الاميركية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84684" target="_blank">📅 21:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee3de71745.mp4?token=owFzbvYBaYJRa3VGDHy9IH-Ceb3BotKiTwKhwUFwDzkE-IjBncO8G7nT4Z6nIiEZFfeu2L2Yg0vALDRE6lD6_TLh0i-C_vGScDTZS69u6PCjsYAFVAYQLRHM35F9fGL4QRe1Vv9SzlivpzH4DwMHUJfY9-kY0TapA76j2ZTvTq5hEh47mn6YYnVBSraR_hgG8lYF3Cjag1ZiXUazBmh7wAdunFvxqNmsckufb0vijwSb-0gR4XqFDImRMN-MaVYhFDqkAQrGhCSnHAEy_pjProWAlhQ1SI_uBLqt4Gm7T-DBT4lKH0GkXl1EZkPdla8L8qMsamuH4dIIU2-sJ-wZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee3de71745.mp4?token=owFzbvYBaYJRa3VGDHy9IH-Ceb3BotKiTwKhwUFwDzkE-IjBncO8G7nT4Z6nIiEZFfeu2L2Yg0vALDRE6lD6_TLh0i-C_vGScDTZS69u6PCjsYAFVAYQLRHM35F9fGL4QRe1Vv9SzlivpzH4DwMHUJfY9-kY0TapA76j2ZTvTq5hEh47mn6YYnVBSraR_hgG8lYF3Cjag1ZiXUazBmh7wAdunFvxqNmsckufb0vijwSb-0gR4XqFDImRMN-MaVYhFDqkAQrGhCSnHAEy_pjProWAlhQ1SI_uBLqt4Gm7T-DBT4lKH0GkXl1EZkPdla8L8qMsamuH4dIIU2-sJ-wZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84683" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84682">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/84682" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84bcd374c4.mp4?token=pCTV98pZT1_5rsXkaaf0x_18n8aR0aF2ohlB2nSx0441UrBS25JvY0hyARSqfQosahAYlltYI5WBSzYr9_qT1HO1DjTixE5GJfOkE6uFj1YHoWvaLI8E5sJXhJw63fwwtV4O7jx3833JE6PE_VJjGipWTCsiofg31TT2iyPPZ91dYYagVtThlHeurmBJmjiQ5s14zriUWS56C6Zxxw4RFHtaAlzyXd7xBIi24dxoQGp8U9s8L6WMz3R3HwhBgZk92BmoOuehx44eDsn3u1Di36_PBVKB-2zV5rKIz_UpQfg7UO0oykBubxzur5NGarNptjzUJopQ9dbJDoEvOVJKvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84bcd374c4.mp4?token=pCTV98pZT1_5rsXkaaf0x_18n8aR0aF2ohlB2nSx0441UrBS25JvY0hyARSqfQosahAYlltYI5WBSzYr9_qT1HO1DjTixE5GJfOkE6uFj1YHoWvaLI8E5sJXhJw63fwwtV4O7jx3833JE6PE_VJjGipWTCsiofg31TT2iyPPZ91dYYagVtThlHeurmBJmjiQ5s14zriUWS56C6Zxxw4RFHtaAlzyXd7xBIi24dxoQGp8U9s8L6WMz3R3HwhBgZk92BmoOuehx44eDsn3u1Di36_PBVKB-2zV5rKIz_UpQfg7UO0oykBubxzur5NGarNptjzUJopQ9dbJDoEvOVJKvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
الدفاعات الجوية الاميركية في محافظة اربيل لا تتوقف بالانطلاق في محاولة منها للتصدي للمسيرات الايرانية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84681" target="_blank">📅 21:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84680">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6435203c20.mp4?token=Z4rrwvRVQKhcHOWkrLcS9ak4Atub09A7nN8Z2boJPPd42TY0SxRgfhpxGhdD8st8f4RFHhHIqyrhHfn-YW02eULXLajdhBKlWrcY5h2_AEIKxUZc_OUHHNLDsRxIjrNBddBLujZdT-p82LM5JunzryfvoyEK-CFiau3dwUgiWcTBNmk9IAYK602AjjSHlYZbg-xNV00pPa5xcD-jcH1wWhH2GsMa_UWog-auOtIt2YOSWg5lQpUbg6s99wWVGzjoCZXvQkFoVznTOojpik-4bHuZAsQ73KjPsCm2waJBedUYn9frqo0wmlTXSOwcWNe9WztupB2XJfCxN6t-HCIgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6435203c20.mp4?token=Z4rrwvRVQKhcHOWkrLcS9ak4Atub09A7nN8Z2boJPPd42TY0SxRgfhpxGhdD8st8f4RFHhHIqyrhHfn-YW02eULXLajdhBKlWrcY5h2_AEIKxUZc_OUHHNLDsRxIjrNBddBLujZdT-p82LM5JunzryfvoyEK-CFiau3dwUgiWcTBNmk9IAYK602AjjSHlYZbg-xNV00pPa5xcD-jcH1wWhH2GsMa_UWog-auOtIt2YOSWg5lQpUbg6s99wWVGzjoCZXvQkFoVznTOojpik-4bHuZAsQ73KjPsCm2waJBedUYn9frqo0wmlTXSOwcWNe9WztupB2XJfCxN6t-HCIgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار محاولات التصدي للمسيرات الايرانية من قاعدة الاحتلال الاميركي في محافظة اربيل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84680" target="_blank">📅 21:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84679">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff0cf3d8b.mp4?token=Yyy_uWSG6Q-LQw5sZ2fsg376xzPuxmnqn7N6fVpt48odcnT6zO3LDxg28jpFBcnpqda8JErCNxqNpK6aFGAooADKaZYbthJyGFEJN-mnqOd-2L-_dGyPRNJrOiNfI2bCd0Lw4duxMmId_2sCyeFIaoom6U_ep08_MqZXRqA9TjnNGI53YhJOHaU6pXzJpHVL236v-fEXCA9gqvHtIBA6bTj-PlhB7FUTAD0uL4wIJq5uft_De8UlzRc7hOjG_lT99TZTa9tnNDFA6R2KGMkupgs0JCP8cvEPLu1kxd1BDK9XKn7L6hSSLVMrz_25Zcg-6gug-8w00I11RKf1vuVCUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff0cf3d8b.mp4?token=Yyy_uWSG6Q-LQw5sZ2fsg376xzPuxmnqn7N6fVpt48odcnT6zO3LDxg28jpFBcnpqda8JErCNxqNpK6aFGAooADKaZYbthJyGFEJN-mnqOd-2L-_dGyPRNJrOiNfI2bCd0Lw4duxMmId_2sCyeFIaoom6U_ep08_MqZXRqA9TjnNGI53YhJOHaU6pXzJpHVL236v-fEXCA9gqvHtIBA6bTj-PlhB7FUTAD0uL4wIJq5uft_De8UlzRc7hOjG_lT99TZTa9tnNDFA6R2KGMkupgs0JCP8cvEPLu1kxd1BDK9XKn7L6hSSLVMrz_25Zcg-6gug-8w00I11RKf1vuVCUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات مسيرة في سماء محافظة اربيل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84679" target="_blank">📅 21:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84678">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
اطلاق العشرات من الصواريخ الباتريوت من قاعدة مطار اربيل شمال العراق في محاولة لاعتراض الصواريخ الايرانية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84678" target="_blank">📅 21:16 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
