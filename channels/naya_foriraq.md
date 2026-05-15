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
<img src="https://cdn4.telesco.pe/file/ajqzmAZyv0eAVO8zOoL9F9vYE-v_k3-ToqIeHmNpSgYkK5cOGMTFYb9zkGJYdbLOSgySvo_NTpOHDJHLM2ct6CTxeltkpxwbuctqfVosjk762n1VR-URHauKY2cCsTDWnpc61gF_MIwHGBR_TZj-Is_pZ-mQwPekyiyripHvLzn7wstOCR-EB7oVqCmoDZuv91Z8LcmwLRnitxxrAbQS4QbGr7Y3G3MI4uUSDjbL6Jm94WfGkB3m3J0j8Wz0dcuNYHDtLqj25NK_Qyvqzhx4lmy_DGq8NOJc5Jnq5_Ia2GRMvsBpBLZYuhUsahgj4WliYVNhEicUxcS8wmYk3YpoYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 254K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 20:37:23</div>
<hr>

<div class="tg-post" id="msg-75458">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سوالف الگهوة
الأساس وتصميم سيلتحقون بالمالكي و الفياض والأسدي والغراوي ويلحقهم المجلس الأعلى وأبو الاء الولائي ..</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/75458" target="_blank">📅 20:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DThSDFDgN3U1dGNH7hWZKaYD0SVVtHOqLWJKz4SqrkMXr8gGrTtdznF9Ir8RtZmgo-uwJy2YF74x8j1xYR3cOaMq7YGKXYbZLMrEP_MNgwa2QTbt7eino2eUhZqZKHrp1emeSoYhhQyBI-NNadaWSkzlbcnrqFWZF7kjAqfPY-JS3n_CuspkmMIHnk9Je4ChSE6QDMPQ1UUFZDD_U9VZifoBFdh6g0aCo2TVkSBOSi4pcBOHJ1kMIZyZ5XGXQnnQQ8F4nGJ8bJ8v0Moanr3_ZtTseydRxh87CoO7IXwMoTkTUHoEByGXmm2_9BTj900khb3Wrqu5I2XaenQD_mxgAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السياسي العراقي حامد السيد يؤشر بخلل بموقع رئاسة الجمهورية !</div>
<div class="tg-footer">👁️ 547 · <a href="https://t.me/naya_foriraq/75457" target="_blank">📅 20:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb51233478.mp4?token=YuQhY0zbEcuPbfUOAAem1BH6LUNbAZcep7fNC8uY7VKXpwrXHagddLpLXs9XsW19WbnJ5L_rPDk4rIz2Fls3xMb2Z5ivGi-bRpVfVi5MPf4ofFSBOkUPH_0Xh0WCmH07-VWAU45q8DE93ejuKD8xk_veB7VvYWTME3p3W_BjLjZWjZeFZcaQx1M9kNl1uQbPJ5vTevGonpmWnUYHI8zW90Kiq53kFT95TUaPIP6TQLT-b2--T5tfUgkvpzRsHGl2vwSuEUtXpmYvqFKyezqa3ZGzfjBSDEmqDIKgejuPhqT9DXhqMT81-NmqxHGXkn6NJUTKjXi6-v9VIcThVAh5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb51233478.mp4?token=YuQhY0zbEcuPbfUOAAem1BH6LUNbAZcep7fNC8uY7VKXpwrXHagddLpLXs9XsW19WbnJ5L_rPDk4rIz2Fls3xMb2Z5ivGi-bRpVfVi5MPf4ofFSBOkUPH_0Xh0WCmH07-VWAU45q8DE93ejuKD8xk_veB7VvYWTME3p3W_BjLjZWjZeFZcaQx1M9kNl1uQbPJ5vTevGonpmWnUYHI8zW90Kiq53kFT95TUaPIP6TQLT-b2--T5tfUgkvpzRsHGl2vwSuEUtXpmYvqFKyezqa3ZGzfjBSDEmqDIKgejuPhqT9DXhqMT81-NmqxHGXkn6NJUTKjXi6-v9VIcThVAh5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجار كبير في محطة للغاز بمدينة زوليا الفنزويلية.</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/naya_foriraq/75455" target="_blank">📅 20:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
حدث أمني غير عادي جنوب لبنان ويصنّف على أنه خطير جدًا.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/naya_foriraq/75454" target="_blank">📅 20:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defed828a2.mp4?token=W5uOjUbFlhvTOn1V4oAunYzCljOJbasgtMlDGRf0oi6Wdn1gsVJFw1NkJqmdt4RzBxVnYEEaXCIDt-L_UUFiYvDV8X5LckLwniGIvhdO6emShtMG-Y4LEsWVSsm5kmng2cAh59ytYZAeS0I7isBjfaRNun-3xvQn-YRtJ66kouLN-oyDtkMtuzBXhFkD47Whj1PwFh13Ps9vkGDfb8b7l4zec9hqlOIZa6KXgWj5c9y0GUcKBK9rhjrUj3jgnOogK_LNG-M3vKpuhrh7RUaB0wA-50rgIq0KPRweMDo412y_9Y6VQwp6ttPpCxQ9Lj3tLm8St1aIJYHpGvvK_rZfkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defed828a2.mp4?token=W5uOjUbFlhvTOn1V4oAunYzCljOJbasgtMlDGRf0oi6Wdn1gsVJFw1NkJqmdt4RzBxVnYEEaXCIDt-L_UUFiYvDV8X5LckLwniGIvhdO6emShtMG-Y4LEsWVSsm5kmng2cAh59ytYZAeS0I7isBjfaRNun-3xvQn-YRtJ66kouLN-oyDtkMtuzBXhFkD47Whj1PwFh13Ps9vkGDfb8b7l4zec9hqlOIZa6KXgWj5c9y0GUcKBK9rhjrUj3jgnOogK_LNG-M3vKpuhrh7RUaB0wA-50rgIq0KPRweMDo412y_9Y6VQwp6ttPpCxQ9Lj3tLm8St1aIJYHpGvvK_rZfkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
على الرغم من محاولات الإعتراض.. مسيرة أطلقت من لبنان تصيب هدفها في كريات شمونة واعمدة الدخان ترتفع.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/naya_foriraq/75453" target="_blank">📅 19:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eee05b77d.mp4?token=O6caa6aoRz7Tns73ElRESXL6S4CdgECuqwIL_mikrhRBX8Exi9ooE6XGR5iI70poaWexTNXhtVZmijb0CrCs-tfGDEqfRRVgnFBDthxmJWKMG1vlmcilU5oItjk1IKFci4kljfSvAu1amWwkJA4Bx8-QzKImndF005YBxyjqPWbrHa97smtHquAC98k6vDTbspw1nOuTneP1f9acktmf8BUDgSrQBMwPvaGGzBcUBIgHgDM1gyDr-06nxQIaZ2yN7XFkzmiD6dxmuoA8JZe0h4ni11ipg_P9VwNlno013f0hM8CGcawUfESzF9kO2zF--_cuTLTujH7kRP2-_mUr6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eee05b77d.mp4?token=O6caa6aoRz7Tns73ElRESXL6S4CdgECuqwIL_mikrhRBX8Exi9ooE6XGR5iI70poaWexTNXhtVZmijb0CrCs-tfGDEqfRRVgnFBDthxmJWKMG1vlmcilU5oItjk1IKFci4kljfSvAu1amWwkJA4Bx8-QzKImndF005YBxyjqPWbrHa97smtHquAC98k6vDTbspw1nOuTneP1f9acktmf8BUDgSrQBMwPvaGGzBcUBIgHgDM1gyDr-06nxQIaZ2yN7XFkzmiD6dxmuoA8JZe0h4ni11ipg_P9VwNlno013f0hM8CGcawUfESzF9kO2zF--_cuTLTujH7kRP2-_mUr6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
هجوم مركب جديد.. إطلاق طيران مسير ورشقات صاروخية من لبنان نحو مستوطنة المطلة بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/naya_foriraq/75452" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
ترامب:
لم أقلل من تقدير قدرة إيران على التحمل.
أبقينا على جسور إيران ومحطات توليد الكهرباء وبإمكاننا تدمير كل ذلك بالكامل خلال يومين فقط.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/naya_foriraq/75451" target="_blank">📅 19:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75450">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50710e6d35.mp4?token=nuDhARdT5eZ5g_BwC7c6AZQE-uPStVWsmgJqpnakCghCRiBldmbuhBECgXhS7PtgeJRNZsWq9_NpCMZilz6oELHk-hBc3TABeR4SJApjX9e6JuD3OCo568E6alfD4eGwWyx2v_4FeNttw-dF9mpMn9_VvSbROJ5XIF26cKx5XPwRHu_HsqWSfvxF3PCERvZ73u2gkM8UzHjy28Db9FWKtBO0qdDevvF-CcAbtwDSvVKksnzeIWTOTyjAHHBSBTqQBgIJQX6l5zgZ08CKdV2hTBtbKijBPk3a90hI92LLfUJM4djJNSjRIP2Tdt4DkNTIjX3X5Z8GZcT6cVicgYkhXSXgzQ4r5pz3d0C_7eSIjtMh7Q5kUpzk-3aLNytoLSTDJq44Cnoxos7sgMWJvy1oBaUq44MtvtoqeZMrnvoa80wlD-bND6IZ6GiCKZnzqK_Vx62y9B7qSElznRzkR-xaDHWg_oQF4Ih9cyr4d6TFsZELzEGrGbKWVJ4k9ebGO2Vslcpn4owVmOWtcxAR_f-xMO8AMJuKHWEPeuOrSlAvz9mTSRYs--BxcZir74RtWE1ebtXNWKpPvwRJxAKl6Sda_h9-CKTr-ACtGA6AznJNs7nQY3ivMfr1eIcjKSBASypQFfJYQ5_SO_bdQKEjZ0LSPNVcWK6K0g2rfiX7eHtMMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50710e6d35.mp4?token=nuDhARdT5eZ5g_BwC7c6AZQE-uPStVWsmgJqpnakCghCRiBldmbuhBECgXhS7PtgeJRNZsWq9_NpCMZilz6oELHk-hBc3TABeR4SJApjX9e6JuD3OCo568E6alfD4eGwWyx2v_4FeNttw-dF9mpMn9_VvSbROJ5XIF26cKx5XPwRHu_HsqWSfvxF3PCERvZ73u2gkM8UzHjy28Db9FWKtBO0qdDevvF-CcAbtwDSvVKksnzeIWTOTyjAHHBSBTqQBgIJQX6l5zgZ08CKdV2hTBtbKijBPk3a90hI92LLfUJM4djJNSjRIP2Tdt4DkNTIjX3X5Z8GZcT6cVicgYkhXSXgzQ4r5pz3d0C_7eSIjtMh7Q5kUpzk-3aLNytoLSTDJq44Cnoxos7sgMWJvy1oBaUq44MtvtoqeZMrnvoa80wlD-bND6IZ6GiCKZnzqK_Vx62y9B7qSElznRzkR-xaDHWg_oQF4Ih9cyr4d6TFsZELzEGrGbKWVJ4k9ebGO2Vslcpn4owVmOWtcxAR_f-xMO8AMJuKHWEPeuOrSlAvz9mTSRYs--BxcZir74RtWE1ebtXNWKpPvwRJxAKl6Sda_h9-CKTr-ACtGA6AznJNs7nQY3ivMfr1eIcjKSBASypQFfJYQ5_SO_bdQKEjZ0LSPNVcWK6K0g2rfiX7eHtMMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
06-05-2026
نقطة تموضع تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/naya_foriraq/75450" target="_blank">📅 19:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌟
🏴‍☠️
هجوم مركب جديد..
إطلاق طيران مسير ورشقات صاروخية من لبنان نحو مستوطنة المطلة بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/naya_foriraq/75449" target="_blank">📅 19:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/274d153e34.mp4?token=Mbf0URayl2pi4nEwByopOFjbiZqNw-O6LSzVZaGxXA5moTdHRLvINTwlNe63l571lj-xKUU5ADB2H3iZpQj8re-L_Bl5wKWSAfMQyRMeWq-xc9ZyOPx-w3Bzscx5f0W4OpVj35As2sTHvmY61zC50bhHVmoQVOi7b6X6O_NAxk6_dNa_34F0ipl7HFSugbj5y9c2MYXGIq1_XJhd0LvSYHb9nabIrv-og5CDcD9ukDZWOMEvEUP-4CvtqfgOq-W_Z1hSJ9MZJd1-WrYxTqrmmXBsH0eDmOMEUTdvs4cH5su4ApOWisdrxi97ZIxyguRX8hppjYU-lDOaqDXkIDWbBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/274d153e34.mp4?token=Mbf0URayl2pi4nEwByopOFjbiZqNw-O6LSzVZaGxXA5moTdHRLvINTwlNe63l571lj-xKUU5ADB2H3iZpQj8re-L_Bl5wKWSAfMQyRMeWq-xc9ZyOPx-w3Bzscx5f0W4OpVj35As2sTHvmY61zC50bhHVmoQVOi7b6X6O_NAxk6_dNa_34F0ipl7HFSugbj5y9c2MYXGIq1_XJhd0LvSYHb9nabIrv-og5CDcD9ukDZWOMEvEUP-4CvtqfgOq-W_Z1hSJ9MZJd1-WrYxTqrmmXBsH0eDmOMEUTdvs4cH5su4ApOWisdrxi97ZIxyguRX8hppjYU-lDOaqDXkIDWbBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اندلاع حريق كبير في منطقة بتاح تكفا شرقي تل أبيب المحتلة.</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/naya_foriraq/75448" target="_blank">📅 19:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzAYJq8iSwuUgppeOeM2RQeVabqyPwuqmCmIwh8KswmI1Bw-M9rnAHIjnzKOhJuBme6wkgcPdaV4nC6E9Dv0fPpLuHK5sXQidscTAzT6fslz5m3doPNZvBw5CjNmHbQq_mgpH7RPiaeCWd8wreaUfeFhMp3eWgHmsUiLWwY1S1Q5GRQybDgUD-yWpsRsSIJAnDUEqA51RL5V6pQIqYVRdOnSu7gkXgRUSdahMQTiydHDx__waHXv06JHm2iuhFKsFNNWgvSFSCXugcVa4_FAE2sHdQ1Ha3vIttuSaXIoGFFk4fDmgDXkSUwzlTqt51EDSvW-Dgk7V8cpSDg3-iDjEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط العالمي تلامس 109 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/naya_foriraq/75447" target="_blank">📅 19:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏴‍☠️
هجوم مركب..
إطلاق أسراب من المسيرات ورشقات صاروخية نحو الشمال الفلسطيني المحتل وصافرات الرعب تدوي من رأس الناقورة إلى نهاريا.</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/naya_foriraq/75446" target="_blank">📅 18:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkHGwHlGcawFtQ8zJeVLkvVEMqtvTD06AbxIP_BxHnq8_3PQqbFXc4YeA45CvlIdQ8BX38FUnZh7uTQ_zgzmQoH3QIjfcHJY3LAvOeJE8RbP_jR9KyQaZUYPo8MWdCIGJ0EK9cIxe1L0GEjuizxLJR4OrSRd_NRWaK1JgNC-ASRA0r38OcNEqu4SrWlOIpEHmS4u2Qz3hVHfjyWLLqxbnRaKurNA9vDj_LDiSx6qoGzdJh2F8VLB3FljcNSlNXm2ewUNVKOxUcPAKsxM0trI0GX-HssqIdUMqnDR8GvTxdQWGIoNIJDxf6TUaZ3q_WtqfGkoU3OYYgkYHnaiAt3-FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود بزشكيان:
إذا ذهبَتْ إيرانُ فليذهبْ معها رُوحي وبدني،
ولا تبقَ في هذي الربوع نَسَمةُ حيٍّ أو نَفَسٌ لأحدِ.
‏خلّد الفردوسي، من خلال الشاهنامة، الهوية التاريخية والثقافية لإيران، ومنح البطولة معنىً مرتبطاً بالعدالة. واليوم، يُعدّ أبناء إيران حماة أمن هذا الوطن وعزته في وجه الظالمين.</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/75445" target="_blank">📅 18:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22069c906f.mp4?token=czpDn4lY-HuaXDIriNdLUpTU4TqJpup0jLFgNqJIQS3ZZYXswF9uQFxMlXBku16yh0c5nyTUPinf-JGy4UzGZNQuZJa788VmLtoAd7bqEBz_mbGxNeTzp0n2-qMVtHtegI70U8E1BGaIqrHrMk-_Kued8EYH9tGpS1jDQf1HkvAFFdBaAdEw2a9gL4NvHn_wc_UlP-mlc-qvmg3xFpsu-anTLiibsqaLbdL2qE8dVZyiTNzAga0Zi7gwsggP9j8fn4HWpRAxJJM9em9icHcGHauGXqL8z2uTihdBQqdMZzkAeeB9iRV5qebOps6RdmCx0G5jcQ6g38Ls3lRr7IloNZiwtGiyJ4IOTl7nhj78uFOYd-zpNlc7sELUNlGvYsONsB92qEA6Evvj8e2lfUb_ICDG48XCqKpbOTEKtAxzVMrPw5lSbzM-sGcEBK8OGepgFDzo4FOVY2ccze55l_0tOfgS9CLFWMczfMoQcZVzt59v_iox3INUC4sR43vghqdYf1srBESaqkMGDduFRmBjm7JgJVI7kguYHBV8QL2zp2egQJpLwFfAP9seW4J78CQYR7jvHM03yOIcvUfZNmJ2eOA5gBUaOx5HD26252Qjy4nam12M6yuBAgij0bxlCW3aVsT_sVXVGZINFiv706kyhmzHp_mKNHfYr394pyHB5Ok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22069c906f.mp4?token=czpDn4lY-HuaXDIriNdLUpTU4TqJpup0jLFgNqJIQS3ZZYXswF9uQFxMlXBku16yh0c5nyTUPinf-JGy4UzGZNQuZJa788VmLtoAd7bqEBz_mbGxNeTzp0n2-qMVtHtegI70U8E1BGaIqrHrMk-_Kued8EYH9tGpS1jDQf1HkvAFFdBaAdEw2a9gL4NvHn_wc_UlP-mlc-qvmg3xFpsu-anTLiibsqaLbdL2qE8dVZyiTNzAga0Zi7gwsggP9j8fn4HWpRAxJJM9em9icHcGHauGXqL8z2uTihdBQqdMZzkAeeB9iRV5qebOps6RdmCx0G5jcQ6g38Ls3lRr7IloNZiwtGiyJ4IOTl7nhj78uFOYd-zpNlc7sELUNlGvYsONsB92qEA6Evvj8e2lfUb_ICDG48XCqKpbOTEKtAxzVMrPw5lSbzM-sGcEBK8OGepgFDzo4FOVY2ccze55l_0tOfgS9CLFWMczfMoQcZVzt59v_iox3INUC4sR43vghqdYf1srBESaqkMGDduFRmBjm7JgJVI7kguYHBV8QL2zp2egQJpLwFfAP9seW4J78CQYR7jvHM03yOIcvUfZNmJ2eOA5gBUaOx5HD26252Qjy4nam12M6yuBAgij0bxlCW3aVsT_sVXVGZINFiv706kyhmzHp_mKNHfYr394pyHB5Ok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالفيديو | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-05-2026
آلية هندسية (D9) تابعة لجيش العدو الإسرائيلي عند خلّة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/75444" target="_blank">📅 18:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزير الخارجية الباكستاني:
إعادة 11 باكستانيا و20 إيرانيا اختطفوا على متن سفن سيطرت عليها قوات ألامريكية.</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/75443" target="_blank">📅 17:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75442">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM4ZQ71gdm5QTUWTMFmx_Z4WRKuNArPrBCRUDv2bg38NWvKCXa05RDgBumZvBO9eBWUABFXEcuNHL16wOd7x2YgaDHbZE1P92CkRO7pqtbFj3TbfuKPsTwyVXJE2venbRhcuD-eVNb1dkZS8UDo2GDJd04uVcgVzCnEL_a44hCreDXFwvxo7co5RugNhJX9R-kRFmLtAo3Bebkx8YMHV8wP8BKPd-6N1WCinIx9s6-uMadMYBlUvlNNOqv3Dva6u8-C9Uq5d1EaTl8an-WdBsH7qslLToeIZMoLl57d1fyh6S9ldmQYZBs5dCQFP9u9tfEhwRUDkhy9NLZ99x9LKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل الدفاعات الصهيونية بالقرب من طبريا</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/75442" target="_blank">📅 17:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75441">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 12-05-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/75441" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75440">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزير الطاقة الأمريكي رايت: أعتقد أن الصين ستكون أكبر مشتر للنفط الخام الأمريكي</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/75440" target="_blank">📅 16:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏ترامب: لم أرغب في وقف النار مع إيران وفعلت ذلك كخدمة لباكستان
اشرب جايك لا يبرد
😄</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/75439" target="_blank">📅 16:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">📰
مراسل صحيفة نيويورك بوست:
‏قبل صعودهم على متن طائرة الرئاسة الأمريكية "إير فورس وان" لمغادرة بكين، قام الوفد الأمريكي بأكمله بإلقاء كل ما قدمه لهم المضيفون الصينيون - من هدايا وشارات ودبابيس وأشياء تذكارية - في سلة المهملات الموجودة في الموقع. ‏لم يصعد على متن الطائرة أي شيء من أصل صيني. ‏كان الوفد قد ترك أجهزته الشخصية في المنزل واستخدم هواتف محمولة نظيفة طوال الرحلة.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/75438" target="_blank">📅 15:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سوالف الگهوة
وزير ادّعوا " انه لم يصوت عليه البارحة سوف يعود بقوة القضاء العراقي المستقل ، العامري الزيدي ورجل معهم حكيم اجتمعوا البارحة عند المالكي ليلاً …</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/75437" target="_blank">📅 15:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5ac0cea1.mp4?token=s7D13QZDotFZ0b6cNolg1yQri5ViEg6HL0qZQE0sWk53aANV7wB6t6x5esFOzd0YfQYovPHIeKFRvmr2_YEyW6G1AsniLPW0nlvmJKEO03_m4u3Be0_N9jO5-VD3Fs5uSlb8aPWrY-JDglUm06TBOnO7n5iBq6ipaoST4MT_fLyRwpuXBNyBbk464QkuKSIL0m_IBx1bHa5cZg85887FBxt3BUuahGZKYruh_DuRjHzvRccHF9AGnx9fC5fvEnJ1eUvX3V1LTAvk3pLtboPX3ia9rb231AJyjnq_h3v6O9fDhCYQ18pn_ljey2oYjs1DVCdSHvCH2zyldHIt_C94Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5ac0cea1.mp4?token=s7D13QZDotFZ0b6cNolg1yQri5ViEg6HL0qZQE0sWk53aANV7wB6t6x5esFOzd0YfQYovPHIeKFRvmr2_YEyW6G1AsniLPW0nlvmJKEO03_m4u3Be0_N9jO5-VD3Fs5uSlb8aPWrY-JDglUm06TBOnO7n5iBq6ipaoST4MT_fLyRwpuXBNyBbk464QkuKSIL0m_IBx1bHa5cZg85887FBxt3BUuahGZKYruh_DuRjHzvRccHF9AGnx9fC5fvEnJ1eUvX3V1LTAvk3pLtboPX3ia9rb231AJyjnq_h3v6O9fDhCYQ18pn_ljey2oYjs1DVCdSHvCH2zyldHIt_C94Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يهاجم ‏مراسل بي بي سي بعد ان سأله عن القصف الامريكي الذي استهدف مدرسة ميناب الايرانية
‏
س: سُئل الأدميرال كوبر أمس عن الإضراب الذي استهدف مدرسة البنات--
‏ترامب: حسناً، الأمر قيد التحقيق
‏س: هل يمكنك تأكيد أنه صاروخ أمريكي؟
‏ترامب: مع من أنت؟
‏س: بي بي سي
‏ترامب: بي بي سي مزيفة. هل تقصد أولئك الذين وضعوا الذكاء الاصطناعي في فمي؟</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/75436" target="_blank">📅 15:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انسحاب الاسدي والغراوي رسميا من السوداني</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/75435" target="_blank">📅 15:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75434">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8eBLPkhCGJ_KG02S9O6HPOUVI4ijdZkUEalkhh5duwXXUqMsaudifOvT9dl4g5gutStCRxgIbs9jy4TyLqdEqpXzPrUjKBTYS-lsXs_Q9h1MmsN7bY1f4uXZBSISx8M78oTWL_UBJEB57F3BtAGIlz9uAtDqVurAusensA1yW1MLnT3-7U5kbqVVhZ2KjC4rr_vmm7HGTzkc5AI_iUA_indgdnI38r1crRj42dFDces-PErKHzSnATfnR0Xtc28DsvAw46ykS8WnMqDSbAwTyJ_4ew7tfeoxPDTO7zCRYR_2PhfPAJmkE4qkZLLtaWm-qbh6O6OulRegqYvOSzvkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالف الگهوة   رسالة من ابو علي بوتين للعراق …</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/75434" target="_blank">📅 15:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAmUIuVP_mYZH0yHNcCiXoHvhgL04zJxzguK-klawmZh-lAHXxUjB0Mqp8B9hHFKbzwHEu_iLOJgjIJgerNL-yn1iBf-RHuVcdaKdyIpwranSVktD8fvZ8P3hPo0C_W3__Yy7Rpdo2bqs2xZyLjIGr3cW_AXgY37dfReUP3m8EadFmV_Jq1KkibFq2lf2ggxLd6q13VwA4rZke14kCaQ4-B2Wm_f1pd_4n8g-J92ZnUyVYfBvwmhrGarTOXzSI3tUMsyKKXTRNV_ZE-ZE9dJUvIP3Bsk3OvZFKdXvl18u1NMyqDrM_sh_6QMvki6oPw5pBSjMLvzyK5exuHLKssGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني:
إن مقاومة إيران للتنمر الأمريكي ليست معركة غريبة. فكثير منا يواجه أشكالاً مختلفة من نفس الإكراه البغيض. لقد آن الأوان لنا أن نتكاتف ونعمل معاً على توضيح أن هذه الممارسات يجب أن تُطوى صفحتها إلى الأبد.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/75433" target="_blank">📅 15:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سوالف الگهوة
رسالة من ابو علي بوتين للعراق …</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/75432" target="_blank">📅 15:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏ترامب: لقد أجريت اتصالات مع كيم جونغ أون، زعيم كوريا الشمالية</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/75431" target="_blank">📅 14:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏ترامب: سأتخذ قراراً خلال الأيام القليلة المقبلة بشأن رفع العقوبات المفروضة على شركات النفط الصينية التي تشتري النفط الإيراني.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75430" target="_blank">📅 14:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏ترامب: "الغبار النووي" الإيراني قد يُسلّم إلى الصين أو الولايات المتحدة</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75429" target="_blank">📅 14:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامب: آخر ما نحتاجه الآن هو الحرب.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75428" target="_blank">📅 14:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75427">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏ترامب: لا امانع في تعليق إيران لبرنامجها النووي لمدة 20 عاماً، لكن يجب أن يكون ذلك التزاماً حقيقياً</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/75427" target="_blank">📅 14:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/75426" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0nW9BlNazG6KIjgOTRr2xXlFSoOvySL1cjYxgSmtIpZvFxlFTF8q14Br_qAVVrz2fGvOeMuw81r1e9ef5Ii2nO_ZpPrvXTonvarvEw4ZO-VD1YLQwKgJ_dqmKLjLen8d595cZR8gXN2Ng2F_jLfoqUGu72rtED57Phh43aYr7K3D6Db7mEms9DNImeXZKcymfnnyYmJh6pTqxhSui80iVykScCKJCtmBZ0sPHlkLG5bIDIGCQsTiWnlMrMekFLmcewl3B0SifTozIwhcoFrcmFJO6waDh9Uqf-NzlgOEYgwSajk4fk3xgAaIgcSQLfCOusxPvAoFGf_Bt09oLU1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/75425" target="_blank">📅 14:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامب: لم أقدم أي تعهد بشأن تايوان.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/75424" target="_blank">📅 14:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75423">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامب للصحفيين: لا أعتقد أن هناك خلافًا مع الصين بشأن تايوان</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/75423" target="_blank">📅 14:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75422">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامب بعد اختتام زيارته للصين يقول لفوكس نيوز حول تايوان: لا نتطلع إلى خوض حروب</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/75422" target="_blank">📅 14:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75421">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامب بعد اختتام زيارته للصين يقول لفوكس نيوز حول تايوان: لا نتطلع إلى خوض حروب</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/75421" target="_blank">📅 14:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏بيان لقائد الثورة الاسلامية آية الله السيد مجتبى خامنئي بعد قليل</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75420" target="_blank">📅 14:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75419">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdWlwitBtJG-IdsKZSs0WB9ETNZjpGvVEyW2-Oz56moHJiAS5_RVPbtcefcFCN2Z1brxkGN0JdDQk6Z87YGKKheq95zv94HQ7cKLZM7pUaj1NQ8oTXqVLWRL_axMoApjSHy8FlO3b-5B7lp29q27g3jofWbJD8_y3SrXeYeFhDR8PH2Y02pHWMH-7cRgwPfmbnkakvEFTzHwV1AtRSY3cZQIaADaSU4o4N5KPHupzndVBuU_Mp5Up8Ysa8ZVj_EYLtUymrXxu_le6bdQq421nSpMZH0FXawqAW6s5YKP7CGUZY7lN2mTMe3xWeyd3RXtblAQJBHbdYnTRT_b_HzWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب: ‏الصين لديها قاعة رقص، ويجب أن يكون لدى الولايات المتحدة الأمريكية قاعة مماثلة! إنها قيد الإنشاء، وتسير بوتيرة أسرع من المخطط لها، ‏من المقرر افتتاحها في سبتمبر من عام 2028 تقريباً. الرجل الذي أسير معه هو الرئيس شي جين بينغ، رئيس الصين، أحد أعظم قادة العالم!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/75419" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75418">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏بيان لقائد الثورة الاسلامية آية الله السيد مجتبى خامنئي بعد قليل</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/75418" target="_blank">📅 13:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75417">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlZdEhmheSIb1FgYwMKQCVSmarWfUu4U9t0z7zzVE6yA0L31fYNp7MB9fZiRksESQ3nhkptWUV4Qjdgq8HpgUkgQg4xQhDWvuPX3oHhXjZPG109iNbcG7WuBn_Bsl5GT30zlkzDEU9L2bS1FC3mDVHdU7AurTlKBr5yzI7K_P-p1BuaBwIV93iD7RJMDIdKTbGQy3v0db1tjVWLQknhLfA7n6OF3d1MtKOYqVLkBSarPmNGowtnElcl4zPF8ldQtW-4W4lMwtEXu5-OAIy1FuLy0gMJzDYv0qtvEf2c1aSAkFE7w3hTnTIsqfBzlJgxJaswG5Al2TG1ANASPxPvsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
الرئيس الايراني مسعود بزشكيان يهنئ رئيس الوزراء العراقي بمناسبة نيل الحكومة ثقة البرلمان</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/75417" target="_blank">📅 13:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75416">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني:
- وقف إطلاق النار هش للغاية
- لا يوجد حل عسكري فيما يتعلق بأي شيء له علاقة بإيران
‏- نحن مهتمون بالتفاوض فقط إذا كان الطرف الآخر جاداً
- لا‏ نثق بالأمريكيين
- نحن لا نريد أسلحة نووية، وهذه ليست سياستنا، لدينا برنامج نووي سلمي
‏- يُسمح لجميع السفن بالمرور عبر مضيق هرمز باستثناء السفن التي تخوض حربًا مع الولايات المتحدة
‏- إيران مهتمة بمواصلة أعمال الطاقة والنفط مع الهند
‏- اتفق مع الولايات المتحدة على تأجيل المفاوضات بشأن المواد المخصبة
- الرسائل المتناقضة جعلتنا مترددين بشأن النوايا الحقيقية للأمريكيين في المفاوضات</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75416" target="_blank">📅 13:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75415">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">استهداف دبابة صهيونية في بلدة رشاف جنوب لبنان بمسيرات حزب الله</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75415" target="_blank">📅 13:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75414">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بلومبرغ:
الإمارات حاولت عبثاً حثّ السعوديين على تنسيق الرد على إيران لكنها شعرت بالإحباط عندما قوبل طلبها بالرفض
في حين سارع محمد بن زايد إلى التعاون مع إدارة ترامب والإسرائيليين أبلغه نظراؤه الخليجيون أن هذه ليست حربهم
الإمارات نفذت هجمات محدودة ضد إيران من دون دعم من دول الخليج بدءاً من أوائل مارس ومرة أخرى في أبريل</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75414" target="_blank">📅 12:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75413">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 12-05-2026 تجمّعات لجنود جيش العدو الإسرائيلي في جنوب لبنان بالصواريخ والمسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75413" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b1df4d5.mp4?token=GDAZXT7ZOe0shwLSImQzqDwdDqwqcyMdWmJ1FQ9RAaBFO1b7hZM8o5W8hrxd4mDYd8TBMmIs1u4ajNLNHq27_HU6BSHip6PVm2G8uWnUt-Kp4dFELmjt2qMOvNrIo0YjoDbPCvjI3coBexieT3ultxT5nXqzZj_dEQRVhwhaouT6ATsSOGr1vcBcWbEF92BCf9czmG7CqbD0XMRwE_tZfpBfHPBqJLU2KL2RjFFIt06hoas1rutWqj1R17L7SexpXfPJJSbRRz1FSpYW_QYxVpdL02SEWTe5fpIajGHR8am9JoKf-E3OTV_vdemjB838yqnvxtKnp3i8ASP7kbu6QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b1df4d5.mp4?token=GDAZXT7ZOe0shwLSImQzqDwdDqwqcyMdWmJ1FQ9RAaBFO1b7hZM8o5W8hrxd4mDYd8TBMmIs1u4ajNLNHq27_HU6BSHip6PVm2G8uWnUt-Kp4dFELmjt2qMOvNrIo0YjoDbPCvjI3coBexieT3ultxT5nXqzZj_dEQRVhwhaouT6ATsSOGr1vcBcWbEF92BCf9czmG7CqbD0XMRwE_tZfpBfHPBqJLU2KL2RjFFIt06hoas1rutWqj1R17L7SexpXfPJJSbRRz1FSpYW_QYxVpdL02SEWTe5fpIajGHR8am9JoKf-E3OTV_vdemjB838yqnvxtKnp3i8ASP7kbu6QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالمسيرات يستهدف مقرات حزب الحرية الإرهابي في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75411" target="_blank">📅 11:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7e67fea4.mp4?token=LscT4Y7T-tw7tg3dX4YyIqJ7HsPMHqkbYPBrBajZ2bMTxLW4VnoAh5fHDCCwvOzHC34ilx488lCjgiXyF-8XX8pfy4RaZF4OxTi4GMbn_4o4UUR9nCqEB-kIfa14ou4jd0f5LZZPgLwFbQx_V6pXfC96cAplouut9YJMNx_f2jL20j8rw-8mpeB3osB6yYfF3lVzKstZF09fSLWDhLRcMHBGPnbOs4h7Vtqc9IavhuS1j23jQ0WhvDkB6IubMGvoZFUiJzWIYvDDf8qm_CQq3y0LdWoEHtEOKbScrwf79mQkRUxfzb4Dk-KiedAjjZXcGL228uEpQGMClp_-AmEsmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7e67fea4.mp4?token=LscT4Y7T-tw7tg3dX4YyIqJ7HsPMHqkbYPBrBajZ2bMTxLW4VnoAh5fHDCCwvOzHC34ilx488lCjgiXyF-8XX8pfy4RaZF4OxTi4GMbn_4o4UUR9nCqEB-kIfa14ou4jd0f5LZZPgLwFbQx_V6pXfC96cAplouut9YJMNx_f2jL20j8rw-8mpeB3osB6yYfF3lVzKstZF09fSLWDhLRcMHBGPnbOs4h7Vtqc9IavhuS1j23jQ0WhvDkB6IubMGvoZFUiJzWIYvDDf8qm_CQq3y0LdWoEHtEOKbScrwf79mQkRUxfzb4Dk-KiedAjjZXcGL228uEpQGMClp_-AmEsmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالمسيرات يستهدف مقرات حزب الحرية الإرهابي في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75410" target="_blank">📅 11:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75409">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: هذا هو الوقت الذي يجب فيه على إيران أن تثبت موقعها وتبرز دورها الإقليمي أكثر من أي وقت مضى</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75409" target="_blank">📅 10:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8ecb192c7.mp4?token=ojhIhLfzGXP7G6iqg3oClIyCxh4y9dgozOFzTWzIa_01x1EA4R9fitUVDPZ-Zzp8tmFBvXQVMmeQyv5Zq4wo6X3PQJ-i3ORZ84_2NT8tS-1S8uwq1qE3yMjUGnqdLlXAGQAJ2ve1oz9iiUbdjijbNhgT8B3HwwR8ZAV4ZULg2QD1YZW0M1NjGCFFqC9aoIDFJbv4ROFAIPBEUutIvDIq74HlFpUuzBT2L9r1ZHwVdgoKYP5fRv0m1zzInVTpG_AoOPRgmLltsfUladrqxmw-TcEb2cDwvKWdss5Wzim_YvBPuDXV-g3l6tCX5aThGLo2nXSUr_BAZ6dutsh9oJdxOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8ecb192c7.mp4?token=ojhIhLfzGXP7G6iqg3oClIyCxh4y9dgozOFzTWzIa_01x1EA4R9fitUVDPZ-Zzp8tmFBvXQVMmeQyv5Zq4wo6X3PQJ-i3ORZ84_2NT8tS-1S8uwq1qE3yMjUGnqdLlXAGQAJ2ve1oz9iiUbdjijbNhgT8B3HwwR8ZAV4ZULg2QD1YZW0M1NjGCFFqC9aoIDFJbv4ROFAIPBEUutIvDIq74HlFpUuzBT2L9r1ZHwVdgoKYP5fRv0m1zzInVTpG_AoOPRgmLltsfUladrqxmw-TcEb2cDwvKWdss5Wzim_YvBPuDXV-g3l6tCX5aThGLo2nXSUr_BAZ6dutsh9oJdxOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
🇮🇷
قائد القيادة المركزية الأمريكية
قال امس في مجلس الشيوخ " رئيس الوزراء العراقي الجديد تعهد لنا بإبعاد نفسه عنّ ايران "</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75408" target="_blank">📅 10:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75406">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av34mI9wSoWnf5qRORFOumbDo4LR1PysNsArZyGvfFOP0TCUQrY0jJs0GLFdMN-teVu7xaE9OyeOtIsaJlZi836r1jgbLQTDdhnrvmw600GzAXjS94GB2AcJZTN9nYq7GTBNBZzLuQ3CGt35kp2nZHymFemmZiScMyn1nLi350mi_V1JGhemDjAyLsAscH_tBMdFcsh6LqZiYj5xGYk5JoaQy0XIdPUp_ll7g1X9L1gtg5CKYDoKDfQ8cESYPBR-c_ubJ4SFvAS2UrGF4eoMtMhlEU4tGz8gFi7T1PyycQSEZr9EjbRErJEN9u-mm7qku_C5ynjAW-815--pJnNdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب
عندما أشار الرئيس شي بأناقة شديدة إلى الولايات المتحدة على أنها ربما تكون دولة متراجعة، كان يشير إلى الضرر الهائل الذي عانى منه بلدنا خلال السنوات الأربع لجو بايدن النائم وإدارة بايدن، وعلى هذا الصعيد، كان على حق 100٪. عانى بلدنا بشكل لا يُقاس من حدود مفتوحة، وضرائب مرتفعة، والجنسانية للجميع، والرجال في الرياضات النسائية، وDEI، وصفقات تجارية فظيعة، وجريمة متفشية، وأكثر من ذلك بكثير!
لم يكن يشير الرئيس شي إلى الارتفاع المذهل الذي أظهرته الولايات المتحدة للعالم خلال 16 شهرًا مذهلة من إدارة ترامب، والتي تشمل أسواق الأسهم والـ 401K في أعلى مستوياتها على الإطلاق، والانتصار العسكري في فنزويلا، والتدمير العسكري لإيران (سيستمر!) - أقوى جيش على الأرض إلى حد بعيد، وقوة اقتصادية كبيرة مرة أخرى، مع استثمار 18 تريليون دولارًا أمريكيًا في الولايات المتحدة من قبل الآخرين، وأفضل سوق عمل في التاريخ الأمريكي، مع عدد أكبر من الأشخاص الذين يعملون في الولايات المتحدة الآن من أي وقت مضى، وإنهاء DEI المدمر للبلاد، وأشياء أخرى كثيرة سيكون من المستحيل سردها بسهولة. في الواقع، هنأني الرئيس شي على العديد من النجاحات الهائلة في مثل هذه الفترة القصيرة.
قبل عامين، كنا في الواقع دولةً متراجعة. وعلى هذا، أنا أتفق تمامًا مع الرئيس شي! لكن الآن، الولايات المتحدة هي الدولة الأكثر سخونة في أي مكان في العالم، ونأمل أن تكون علاقتنا مع الصين أقوى وأفضل من أي وقت مضى!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/75406" target="_blank">📅 01:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c66844eb9.mp4?token=hGP7Ny632TXm3Ud6ly5keUXxLaRMEKbUKjbp6E97NFPObNXNNcceDIG_3rylVD3zXLj2q1eU2SPaLf6SrEdNC3fYOUTbF56I6bqOA8EczUo7hf0t0h9J32XRnp2Zj9M10Ad7cem6Dk3sljxBz_iFkkObfiT0Ex5aLvY_f0J3TIoOeox2t1LtNc9JyffnUMmyYHgBM9n2ttmtjh2aOBYlF4PXe5R3GixSBeCZjjxYZJT_YPS_tHFCijhDJhmATHDCjNPoSloxayWi9nh4vkV-UONaEoIYn5iYVl9Tqqo8RQFtQmgoFbNP8tO53vF_EAowg6fkpWtxgWk0Yapobyalvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c66844eb9.mp4?token=hGP7Ny632TXm3Ud6ly5keUXxLaRMEKbUKjbp6E97NFPObNXNNcceDIG_3rylVD3zXLj2q1eU2SPaLf6SrEdNC3fYOUTbF56I6bqOA8EczUo7hf0t0h9J32XRnp2Zj9M10Ad7cem6Dk3sljxBz_iFkkObfiT0Ex5aLvY_f0J3TIoOeox2t1LtNc9JyffnUMmyYHgBM9n2ttmtjh2aOBYlF4PXe5R3GixSBeCZjjxYZJT_YPS_tHFCijhDJhmATHDCjNPoSloxayWi9nh4vkV-UONaEoIYn5iYVl9Tqqo8RQFtQmgoFbNP8tO53vF_EAowg6fkpWtxgWk0Yapobyalvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع أعمدة الدخان من داخل مقر رئاسة الوزراء في ليبيا، عقب اشتباكات عنيفة بين مشجعي أحد الأندية الرياضية امتدت إلى محيط المقر الحكومي.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/75405" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75404" target="_blank">📅 00:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75403">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
🇮🇶
عراقجي يهنئ بتشكيل الحكومة العراقية الجديدة.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/75403" target="_blank">📅 00:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75402">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75402" target="_blank">📅 23:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75401">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY_1KfQFVnVPeLuKIBMepibmfyxwRL7Me81jwvwk7mYRLV-hBR9FD6VxVDTp-W_VI_8CXj3ta8H90U1RjKkpzyke74s7yuyIj3LVLpRzapz2jRHp0aBYY5mtpSuu2dZK8Iq3jYqAeQ4p42V0A7pfXxSvZOM9CKr1oCcA0AAapNW0ElM7xdKwGzHRQSj47OiGpiSLurCbE0PE5SJJ8xV0GVnM8bQ1dPAiKw6ijyz_E4gbSOBCIMWzDeGOt_5uGWQIrPyshxzZANOK-d4_JptjhyQm-dYIhDwFdwYJaLlAxVIs89cdfLHxpI0Txq0GyQ4rCZQUqa_DlbzrhF4wu08Wew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75401" target="_blank">📅 23:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مصدر لنايا  يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75400" target="_blank">📅 23:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROZfHazcKFWN90ZUdZBd47KyoKddor-REkiPdxbxviNS0W9w6HvsBXWcBsiO-GkPDd93kge6jf3g6LexglMiYTzvFV5bcCXxwrI3lIetq-78cS89kpyJ9XRWp1-tMw8a4pCRL51Yp3vCtR5rm8ygQGg0wGf-pSTZiEZhqqOwy5leUDZtcgVlkhgnNFwZ4j-UV4AYCImZt3732M0pYBBYscTarwqG0IarcIN7ED7hVWf1JXWQw26rbTmGhImn_40cAzipoDIW0WGXDbVcsKuZFHmzkpP74k2zbMzMpdKoalwYiY9gY_nURJyPoMRhccEtkmZ2UpB9xYmnuDSI6mczcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
إذن أنت تمول هيغسيث مقدم البرامج التلفزيونية الفاشل، بمعدلات لم يسمع بها أحد منذ عام 2007، حتى يتمكن من تقمص دور وزير الحرب في فناء منزلنا الخلفي في هرمز؟
هل تعلم ما هو أكثر جنوناً من 39 تريليون دولار من الديون ؟ دفع علاوة ما قبل الأزمة المالية العالمية لتمويل لعبة تقمص أدوار حية، وكل ما ستحصل عليه هو أزمة مالية عالمية جديدة تماماً</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75399" target="_blank">📅 23:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75398">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">#سمح_بالنشر
.. مشاهد من إستهداف أبطال المقاومة الإسلامية في العراق
#رجال_البأس_الشديد
أهداف حساسة في عمق
الكيان الصهيوني
الغاصب
بعدد من الطائرات المسيرة حيث حققت إصابات دقيقة ومباشرة .</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75398" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc00397ad.mp4?token=XohqRHHwm_jwyFcOeHDXaho3yL3pCXUGprBUtOARJX7hRJkFzrftKkBJIS9Eb-F0c2FKo2hO6DSl5RY4OwXC3DKyhktl42g5K2kMmpC0JOvsTyLGXuzTiAUXfThhsi51GjkNcnOGYNZTjsGMvpG1MxcD-dyXolzO4xjT0hA1eqKHU0my20QH95Y_zbxESdJgR5sVdJ81dlZW-rJjqAXKGWnT8-7sWIkDlv7Vo7ZM4VAY5RyM4LGdBzQ5DWhxYrlXW_10Zvz3uMRfGRJFwFXaDOkDZoG1eoxLWxVtiwEdX_sTN1-XC2TGkWrj-Ieh0FCCfYAnHbuZsnReRtEtVzmbLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc00397ad.mp4?token=XohqRHHwm_jwyFcOeHDXaho3yL3pCXUGprBUtOARJX7hRJkFzrftKkBJIS9Eb-F0c2FKo2hO6DSl5RY4OwXC3DKyhktl42g5K2kMmpC0JOvsTyLGXuzTiAUXfThhsi51GjkNcnOGYNZTjsGMvpG1MxcD-dyXolzO4xjT0hA1eqKHU0my20QH95Y_zbxESdJgR5sVdJ81dlZW-rJjqAXKGWnT8-7sWIkDlv7Vo7ZM4VAY5RyM4LGdBzQ5DWhxYrlXW_10Zvz3uMRfGRJFwFXaDOkDZoG1eoxLWxVtiwEdX_sTN1-XC2TGkWrj-Ieh0FCCfYAnHbuZsnReRtEtVzmbLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق رشقات صاروخية من لبنان نحو كريات شمونة ومحيطها في الشمال الفلسطيني المحتل والدفاعات الصهيونية تحاول الإعتراض.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75396" target="_blank">📅 22:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87449a5631.mp4?token=rnXubakQhk5XFI4ZFJxHFMLHnDHbHoUHiQ9Gbsp8Nw5uEsTXVk3Ow1csTsyD-vyt0BqU2LNnq1HvMnxe77kScxphbb_0MfbLmTJ0xD6H1-_eOJ7WNCRS7k_uA667VJZlBBXFdCjAw61L93zYZK4Zi8umjoeaZ9a9bvn45ZZ3RP4ZdG5INQOMSuK2mVw1Bg4gazZ3i5rL3A2Oz9ZIXU4a2vXWsk-L88Nlg6XEACyhJQVnSh9-rf50Bla19dQ48QkT6hgBSm12ZtjQMQsSV1aS8IyCSHd8EHJpZmmzucAgXptKHtUsVzHxDJqZwM9sKFqXfwQtt6dieoa8GBUW3xkZYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87449a5631.mp4?token=rnXubakQhk5XFI4ZFJxHFMLHnDHbHoUHiQ9Gbsp8Nw5uEsTXVk3Ow1csTsyD-vyt0BqU2LNnq1HvMnxe77kScxphbb_0MfbLmTJ0xD6H1-_eOJ7WNCRS7k_uA667VJZlBBXFdCjAw61L93zYZK4Zi8umjoeaZ9a9bvn45ZZ3RP4ZdG5INQOMSuK2mVw1Bg4gazZ3i5rL3A2Oz9ZIXU4a2vXWsk-L88Nlg6XEACyhJQVnSh9-rf50Bla19dQ48QkT6hgBSm12ZtjQMQsSV1aS8IyCSHd8EHJpZmmzucAgXptKHtUsVzHxDJqZwM9sKFqXfwQtt6dieoa8GBUW3xkZYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
قصف صهيوني بالقنابل الفسفورية على بلدة على الطاهر في جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75395" target="_blank">📅 22:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مصدر لنايا
يتحدث عن خروج كتلة العقد الوطني من ائتلاف الاعمار والتنمية بسبب ما حصل من ممارسات سيئة في جلسة منح الثقة للحكومة الجديدة  اليوم</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75394" target="_blank">📅 22:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
عضو لجنة الأمن القومي في البرلمان الإيراني "خضريان":
لا ينبغي للكويت أن تنسى أنها سقطت في يد صدام حسين في غضون 90 دقيقة فقط، وعليها أن تدرك حدودها اليوم، وأن الجمهورية الإسلامية قوية للغاية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75393" target="_blank">📅 22:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75392">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceda60f73b.mp4?token=pN__PkPTqYNSOESzWBdz9EPQqIN3gCn6xLg4ljmZYio7IT-W9ZKNaTRPCdDoS8pNwHIj_C4H6Gfn0yUrxuhUX2NaG1NPaVma18xY-hjJk4prK4abIq3P1GypTFc-oBQ5HvgGCpz3PExEbAD7eb_oc6wALfXp0-lkvV7QbCAnM1oUM3ACRTtTelMuEeDzA9lbGVsQbysPCOvo7x_P1TELk2iKfu8Hw_ry_MnkS74dLI9v-rtx7xm53Vxtn3ORXZNFCckXk1wZtwRxlqLwpewEhcbVzPxrMHOUKxvyuZwY-xtzDw51eeKK6yjw74aE5fRFDqPPlNeeTY5siGUTtGrdiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceda60f73b.mp4?token=pN__PkPTqYNSOESzWBdz9EPQqIN3gCn6xLg4ljmZYio7IT-W9ZKNaTRPCdDoS8pNwHIj_C4H6Gfn0yUrxuhUX2NaG1NPaVma18xY-hjJk4prK4abIq3P1GypTFc-oBQ5HvgGCpz3PExEbAD7eb_oc6wALfXp0-lkvV7QbCAnM1oUM3ACRTtTelMuEeDzA9lbGVsQbysPCOvo7x_P1TELk2iKfu8Hw_ry_MnkS74dLI9v-rtx7xm53Vxtn3ORXZNFCckXk1wZtwRxlqLwpewEhcbVzPxrMHOUKxvyuZwY-xtzDw51eeKK6yjw74aE5fRFDqPPlNeeTY5siGUTtGrdiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قيادة العمليات المشتركة:
تم رصد تحركات لعنصر إرهابي خطر ضمن قاطع المسؤولية. و​بعد تحديد الهدف بدقة متناهية، نفذت قيادة طيران الجيش ضربة جوية ناجحة بواسطة الطائرة المسيرة المسلحة (CH5)، مستهدفةً الموقع المرصود في وادي الشاي ضمن قاطع قيادة عمليات كركوك ، إذ تم ​تدمير الوكر الإرهابي بالكامل وقتل العنصر الإرهابي المستهدف.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75392" target="_blank">📅 22:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">يسقط حمد
دعوة لنصرة الشعب البحريني المجاهد .</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75391" target="_blank">📅 22:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سوالف الگهوة   العامري منزعج جدا ؛ ويفكر جديا بسحب وزرائه من الحكومة بسبب مهزلة اليوم في البرلمان …</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75390" target="_blank">📅 21:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سوالف الگهوة
العامري منزعج جدا ؛ ويفكر جديا بسحب وزرائه من الحكومة بسبب مهزلة اليوم في البرلمان …</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75389" target="_blank">📅 21:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287f8d0310.mp4?token=ULs77ergXU3uAt2WoGf7SzAOYFy6fAgthEpO6psJBGyd45PshFDZeI0yezmleldYcS_JObHAyyXeXm1UgFBmCwHeQE2ONllnBYoI2_z-FWLGX5Nc8H8qGE-UF24hwdxPptyFKiXXsPseYME95uA0IvJuVGBSVjsnbhGS0Xa7rWrgbgu8J2RYLwcPEAO5q1URColGZvHpKfAmSu_P_ItL4fcVv07YPlmRrdooTW4hOiJ-yYUKq2dxrfbyzXqx95Sc8Bhc-HQfVibs9dQDL2B17_ur7sQY-WVSytae9-V3Mgo7IRdFdLrgqMxCnGSfdZMsKgWKbc3DfRgJaBWu0wJlQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287f8d0310.mp4?token=ULs77ergXU3uAt2WoGf7SzAOYFy6fAgthEpO6psJBGyd45PshFDZeI0yezmleldYcS_JObHAyyXeXm1UgFBmCwHeQE2ONllnBYoI2_z-FWLGX5Nc8H8qGE-UF24hwdxPptyFKiXXsPseYME95uA0IvJuVGBSVjsnbhGS0Xa7rWrgbgu8J2RYLwcPEAO5q1URColGZvHpKfAmSu_P_ItL4fcVv07YPlmRrdooTW4hOiJ-yYUKq2dxrfbyzXqx95Sc8Bhc-HQfVibs9dQDL2B17_ur7sQY-WVSytae9-V3Mgo7IRdFdLrgqMxCnGSfdZMsKgWKbc3DfRgJaBWu0wJlQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
القناة 12 العبرية عن مصدر: إسرائيل ترفع حالة التأهب إلى الذروة استعدادا لاحتمال تجدد حرب إيران بعد عودة ترمب من الصين.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75388" target="_blank">📅 21:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بولندا تعلن عن تسجيل أول زواج مثلي لها يوم الخميس، بعد أحكام المحاكم الأوروبية والبولندية التي تتطلب الاعتراف بالزواجات المثلية التي تتم في الخارج.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75387" target="_blank">📅 21:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75386">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
النتن ياهو: نقول للعالم أجمع إن القدس ستظل عاصمتنا الأبدية والتاريخية.
‏أبعدنا خطرا وجوديا يتمثل في القنابل النووية والصواريخ الباليستية الإيرانية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75386" target="_blank">📅 21:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf0bEVNf6IFY1Zv6OUM0TUQvR96Hxz0l_y7p0Jxr8q8Sv-UHjzQyTuV-q-9j2GeaVFE_OquuudGCWv11bdiAdHzd3XhgrMDa9bpjV-p-9UH7qHY3Nujjruv2lSyEnFhhcJ1xlliIyEJpolQINW9r45CBIfJQrJi5Z9Idr8I705QPCNSwTJih1Ipt_m_L6x9J42joUG9n4g1fTthVhphJpyrLX5ULWwOTgsDcrMNyBmytN_nmgoIpvOX8JPm_vURtdRipE_mWIuektwMmPPlh3EqJGbuE3dUyd3Ct6UmWMF12doAKKFEIp6x0emtb8KX_bxZsb2DJJX76UJjN9-g3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
عراقجي يهنئ بتشكيل الحكومة العراقية الجديدة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75385" target="_blank">📅 21:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75384">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏴‍☠️
القناة 12 العبرية عن مصدر:
إسرائيل ترفع حالة التأهب إلى الذروة استعدادا لاحتمال تجدد حرب إيران بعد عودة ترمب من الصين.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75384" target="_blank">📅 20:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75383">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال:
إصابة 4 جنود في رأس الناقورة جراء استهدافهم بطائرة مسيرة إطلقت من لبنان.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75383" target="_blank">📅 20:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75382">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭐️
بعد عدم نيلهم ثقة مجلس النواب.. توثيق يظهر لحظة إندلاع توتر واشتباك بين عدد من نواب الكتل السياسية في البرلمان العراقي.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75382" target="_blank">📅 19:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75381">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b2948510.mp4?token=WSt4PS2Y_nAhIMXJYaeQA612wftvTVuQyKmvrALfs-9uAEy3TzIoLS-QG5EuYpWLmlckA27iMP_xA77JAtygF6Fj2n6Y_qKL3-elyvCMjO6ls0Mgau5brCw_j7lLn4s0k8J_pSfwbIVHHELhs64Jmu77VdHm1j3HXElLQudaJ6s0GTqK9Ec5j0tgUpTxUQt_4V19sJ75p2ekiKYtJ53lpK2hHg0Dt13pcstTKj9LLxZn-3t0HBilhpGwvXUeIEEnBWEgd-lKJY53k_XpahbX9qc9XgMLhPMvhiWbr98zfZ34dXs0U6dSdU3SrZRWK3i84kbMS3oBt0hh3hOFirt8mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b2948510.mp4?token=WSt4PS2Y_nAhIMXJYaeQA612wftvTVuQyKmvrALfs-9uAEy3TzIoLS-QG5EuYpWLmlckA27iMP_xA77JAtygF6Fj2n6Y_qKL3-elyvCMjO6ls0Mgau5brCw_j7lLn4s0k8J_pSfwbIVHHELhs64Jmu77VdHm1j3HXElLQudaJ6s0GTqK9Ec5j0tgUpTxUQt_4V19sJ75p2ekiKYtJ53lpK2hHg0Dt13pcstTKj9LLxZn-3t0HBilhpGwvXUeIEEnBWEgd-lKJY53k_XpahbX9qc9XgMLhPMvhiWbr98zfZ34dXs0U6dSdU3SrZRWK3i84kbMS3oBt0hh3hOFirt8mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توترات بين الأحزاب السنية بشأن الثقة بأحد الأسم المطروحة لإحدى الوزارات.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75381" target="_blank">📅 19:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75380">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رئيس مجلس النواب يدعو رئيس مجلس الوزراء علي فالح الزيدي والوزراء المصوت عليهم لأداء اليمين الدستورية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75380" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75379">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5223d3a624.mp4?token=K6yCQgxAJiUXzbQ5P-w916f7SHpvebWIV4-ZaBxDvxCu2BZ_lavDGn80kvO7pHLDtgdWmq-276e5UTd-uGRZEeSx1z2hPQzwyOoz4jDkVFm7lzXc56DQzMP6jqaW7yCegK7mFVkLNtgwrAnr_1mLXcGvy9xcxEFJL-75chVDbKp91OQrkvAlcH1ByFofHwweb99C-lQF-2Cat_br72a2ThgAYJfuDulpYtwCT2LAyA8RQRNNO3_-TUYgTUSGeFCtJUXScX61yGIl5wMnRy4ZIgzhbRG9S_dmPOapBLtgmgDu19dnV-VGoBEW-k6RdW3ebPthHNG4S8Zt9TEokGhUug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5223d3a624.mp4?token=K6yCQgxAJiUXzbQ5P-w916f7SHpvebWIV4-ZaBxDvxCu2BZ_lavDGn80kvO7pHLDtgdWmq-276e5UTd-uGRZEeSx1z2hPQzwyOoz4jDkVFm7lzXc56DQzMP6jqaW7yCegK7mFVkLNtgwrAnr_1mLXcGvy9xcxEFJL-75chVDbKp91OQrkvAlcH1ByFofHwweb99C-lQF-2Cat_br72a2ThgAYJfuDulpYtwCT2LAyA8RQRNNO3_-TUYgTUSGeFCtJUXScX61yGIl5wMnRy4ZIgzhbRG9S_dmPOapBLtgmgDu19dnV-VGoBEW-k6RdW3ebPthHNG4S8Zt9TEokGhUug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مسير في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75379" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75378">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">توترات بين الأحزاب السنية بشأن الثقة بأحد الأسم المطروحة لإحدى الوزارات.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75378" target="_blank">📅 19:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0642dd7275.mp4?token=SYMicSIfTJYMLgEOu94uLmoUiaVRTEDuEGDbOvLbCu6ArN3AszoX1rvRIpaDrMcza9a7i9FTyHBzG3z_C-YMuitTefUCEAdK-fR6st4xVfrDl9KIwPuwZVCc23mkvLI97ZNNfPrMVboCQOi9cFJ7UdLfr1oeG6Sg-TzK3QWogrThaP7yFw1PYXwjCdEYOHC8sSZBvZ1V5cZAVZf_Ep4KaXotFjPL9b1qf1o1POqTT0KYaHGrRbQupVQGCGw0-9jpgzSN6fclKyVtSNzz-nOagvQLQFJP5Faqdc37Cw9DDK4onVzOP031f1Krqy9pz5lF_YNPKHkbMaRdlHkQIaju5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0642dd7275.mp4?token=SYMicSIfTJYMLgEOu94uLmoUiaVRTEDuEGDbOvLbCu6ArN3AszoX1rvRIpaDrMcza9a7i9FTyHBzG3z_C-YMuitTefUCEAdK-fR6st4xVfrDl9KIwPuwZVCc23mkvLI97ZNNfPrMVboCQOi9cFJ7UdLfr1oeG6Sg-TzK3QWogrThaP7yFw1PYXwjCdEYOHC8sSZBvZ1V5cZAVZf_Ep4KaXotFjPL9b1qf1o1POqTT0KYaHGrRbQupVQGCGw0-9jpgzSN6fclKyVtSNzz-nOagvQLQFJP5Faqdc37Cw9DDK4onVzOP031f1Krqy9pz5lF_YNPKHkbMaRdlHkQIaju5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
خلافات داخل مجلس النواب العراقي خلال طرح اسم لأحدى الوزارت.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75377" target="_blank">📅 18:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75376" target="_blank">📅 18:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=p5AmpfsHMkqkvYnbg0tTnvp9SzTujaER8AnhhPRon8pH2oV1jTbl4X_r5cUkhwpCkSiiaW6fhtxvYMnUtq1E7z_Mu8YBWKWuJ_VSvLvzO_CRykwvMjMlTCOTz4VGu722-EiKO2kjbMz1kAeRRPQWAwXncgDGj6R-Sb2U9iLFCsZoKl7LYdjU7XZRyiMQByhX1sHqywVeqn32Q48whqZVUzeq2_RQm2aqTH-tPhzLd4hJT_b3TNEELlZAB75uHcX9gnK1AobjJqJJuGezqGVOlV34onp63zHaW5E3e74wLwzkSGxOZ43985fpSgvTy_uUabdtes4eHbxBc4xeT6oiCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=p5AmpfsHMkqkvYnbg0tTnvp9SzTujaER8AnhhPRon8pH2oV1jTbl4X_r5cUkhwpCkSiiaW6fhtxvYMnUtq1E7z_Mu8YBWKWuJ_VSvLvzO_CRykwvMjMlTCOTz4VGu722-EiKO2kjbMz1kAeRRPQWAwXncgDGj6R-Sb2U9iLFCsZoKl7LYdjU7XZRyiMQByhX1sHqywVeqn32Q48whqZVUzeq2_RQm2aqTH-tPhzLd4hJT_b3TNEELlZAB75uHcX9gnK1AobjJqJJuGezqGVOlV34onp63zHaW5E3e74wLwzkSGxOZ43985fpSgvTy_uUabdtes4eHbxBc4xeT6oiCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75375" target="_blank">📅 18:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa365d566.mp4?token=GIu3ZiETVT8qWv6_9GmpLP82M9Wgmv9WNr41xuYYYPtExU4Mm_NtJK2z4QJdyh_bLTueT5C-hTiG0M2w5H1P9YQduxYCXTRsemQog20s_rl3wSFZFaWYXrJC9BSPhD8tiUZEv-Ruql4x4njZ61JtaUfVHB73-d7MweBDUhmriR2McEAXAGWMw0eODlss8IJa_ZG_BVTHIxFCZlq9CqYEhWq-KpJcKNmXN--6uiXfVoKxt2TdAezFEayWXhJh4cXq03kGhM67N4X5gFV_LjqyCPVfj9KfnTarxfXL0TjQQn51WtnYZgFrUfCTe2UB20E5M5TutjDM9Owk7hiwU01gfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa365d566.mp4?token=GIu3ZiETVT8qWv6_9GmpLP82M9Wgmv9WNr41xuYYYPtExU4Mm_NtJK2z4QJdyh_bLTueT5C-hTiG0M2w5H1P9YQduxYCXTRsemQog20s_rl3wSFZFaWYXrJC9BSPhD8tiUZEv-Ruql4x4njZ61JtaUfVHB73-d7MweBDUhmriR2McEAXAGWMw0eODlss8IJa_ZG_BVTHIxFCZlq9CqYEhWq-KpJcKNmXN--6uiXfVoKxt2TdAezFEayWXhJh4cXq03kGhM67N4X5gFV_LjqyCPVfj9KfnTarxfXL0TjQQn51WtnYZgFrUfCTe2UB20E5M5TutjDM9Owk7hiwU01gfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الوزارات التي تم التصويت عليها من قبل البرلمان العراقي: مجلس النواب يُصوّت بالأغلبية المطلقة على باسم محمد خضير وزيراً للنفط.  مجلس النواب يُصوّت بالأغلبية المطلقة على محمد نوري احمد وزيراً للصناعة.  مجلس النواب يُصوّت بالأغلبية المطلقة على علي سعد وهيب…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75374" target="_blank">📅 18:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">استهداف دبابة ميركافا من قبل حزب الله في بلدة الطيبة جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75373" target="_blank">📅 18:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75372">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مجلس النواب يُصوّت على المنهاج الوزاري لرئيس مجلس الوزراء المكلّف علي فالح الزيدي</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75372" target="_blank">📅 18:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4850c33fc2.mp4?token=BOsi-jSjzZdFGjbJjwVh3Slr2cntJ8-V0ABnVmjabi4xMrcZS7yy9nNNEFTF2YEVWMQoWTlom7j9AmStROMH3IoKbStfmoH4Uq36CWPGkNueJXWuxyynY7SAF9gmaGSVZYB7vCUybdD3U9uuZghn6LitiFKblny-m8SNszSoWrP71gMGA4ZiaHhNBRu5_d8z9AXECT594FEk5GSXXqhmiz6PjaDKPjfc4D3XJ23tM4ESV3iP6RDCRbPWot6Tko8VLdUDTdjYX45n1kUVJwPqAXUq6na2JdKPcX0dnC7wqOPML1sPZWpAPQKpbFGXOQgfhkLm_20IlxOuCuQdj1lZ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4850c33fc2.mp4?token=BOsi-jSjzZdFGjbJjwVh3Slr2cntJ8-V0ABnVmjabi4xMrcZS7yy9nNNEFTF2YEVWMQoWTlom7j9AmStROMH3IoKbStfmoH4Uq36CWPGkNueJXWuxyynY7SAF9gmaGSVZYB7vCUybdD3U9uuZghn6LitiFKblny-m8SNszSoWrP71gMGA4ZiaHhNBRu5_d8z9AXECT594FEk5GSXXqhmiz6PjaDKPjfc4D3XJ23tM4ESV3iP6RDCRbPWot6Tko8VLdUDTdjYX45n1kUVJwPqAXUq6na2JdKPcX0dnC7wqOPML1sPZWpAPQKpbFGXOQgfhkLm_20IlxOuCuQdj1lZ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس مجلس الوزراء المكلّف "علي الزيدي" يبدأ قراءة المنهاج الوزاري للتصويت عليه.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75371" target="_blank">📅 18:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75370">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da1de53a6.mp4?token=RwexOSwUvCmfm_OmG6IKvreSuIIYK9u0xpq6LRhPgJjxR0iPQ1O86CWc14GHBLsTiRQxhkzrrcsYpT7plpjuqDD650-4PtzlM_BmOsHkSe1BF9bMdU8wiuJDSXNMQdepb_-CMWSk_4AL_u8VV0OU00r6gNaLGCOTtdBSDwLtoJ_HrpTk4RpmtYuZ7aPnSjlJWJGqeBUsgh0Vaor2FPDfsaOiddfrMAJN6pQIujw4nVVMy32F-tekNDToyJvpHLpaAr0qWYffSdWh7cjF6kJhO_Q7JbbCTxnTeISWOALzr5ko4ghKFgBJBuT4ZI2yw6BPiv5_3Ulx1kJ_x0aaa9FT1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da1de53a6.mp4?token=RwexOSwUvCmfm_OmG6IKvreSuIIYK9u0xpq6LRhPgJjxR0iPQ1O86CWc14GHBLsTiRQxhkzrrcsYpT7plpjuqDD650-4PtzlM_BmOsHkSe1BF9bMdU8wiuJDSXNMQdepb_-CMWSk_4AL_u8VV0OU00r6gNaLGCOTtdBSDwLtoJ_HrpTk4RpmtYuZ7aPnSjlJWJGqeBUsgh0Vaor2FPDfsaOiddfrMAJN6pQIujw4nVVMy32F-tekNDToyJvpHLpaAr0qWYffSdWh7cjF6kJhO_Q7JbbCTxnTeISWOALzr5ko4ghKFgBJBuT4ZI2yw6BPiv5_3Ulx1kJ_x0aaa9FT1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس النواب يعقد جلسته للتصويت على المنهاج الوزاري وحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75370" target="_blank">📅 18:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72718a0f45.mp4?token=YBXR3hsUcyPN-iycnr9udScw2jKyzWHAmYV7KMeHWu9YMAtRZcn0LMOeG6I8606zJdhSuE5IpHMrMtTfI_wt5AZviwYySQgGiCr64jMzkXnT0E86UrJG1CXcpEkiYpnLuxu9UBiX4xoqalceTb4sX6o25HrshqFlzpgWbzLudU57Lmh5nGGujmPoOrfwLrNeaDK_YtAtx1gaGcmFjuDa0DfFshWAYxNksY-TNJFViwxbBBhm8-kG-sTBFEEdWZhFwB4BGj8ZZZ_Chq9awaRrC3gnWVrxp_GBm_0gIBfSs1MRJNnZJKgF3swgXHtjY4VnxAdB1dCXhNo2Y_GbI_Gr5TnMprxcRtBWtNavw9QK-FknGapXzOPw_JtEOLkKXs9_YP3O5zP6UPxkXMKBH-91uHNrb5gFgwF8HFpPKTRusr2NtEgBfUu6mGF3FdmO_yJb-MsKh0hKbyEf9NI_HqgohK097UYK2O2W5pnSFEQyi0CMXv9ACt38RYb1CyiDn_NX774g8RKBCQhtwj1wjKZGERORCrEtBCNINr0e5d7WprKFF8QuIYhAnX6IS2P2lJgxa7ITAV64rJ2JsN4QjF8_rlkEUSUl04YahhbCnq00p7DHy87ue-ehZ7PpA4Nk2TftAb-HYmx-kX-yQX1UHC3JP5cJOb8tOJoixevJPDzNpuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72718a0f45.mp4?token=YBXR3hsUcyPN-iycnr9udScw2jKyzWHAmYV7KMeHWu9YMAtRZcn0LMOeG6I8606zJdhSuE5IpHMrMtTfI_wt5AZviwYySQgGiCr64jMzkXnT0E86UrJG1CXcpEkiYpnLuxu9UBiX4xoqalceTb4sX6o25HrshqFlzpgWbzLudU57Lmh5nGGujmPoOrfwLrNeaDK_YtAtx1gaGcmFjuDa0DfFshWAYxNksY-TNJFViwxbBBhm8-kG-sTBFEEdWZhFwB4BGj8ZZZ_Chq9awaRrC3gnWVrxp_GBm_0gIBfSs1MRJNnZJKgF3swgXHtjY4VnxAdB1dCXhNo2Y_GbI_Gr5TnMprxcRtBWtNavw9QK-FknGapXzOPw_JtEOLkKXs9_YP3O5zP6UPxkXMKBH-91uHNrb5gFgwF8HFpPKTRusr2NtEgBfUu6mGF3FdmO_yJb-MsKh0hKbyEf9NI_HqgohK097UYK2O2W5pnSFEQyi0CMXv9ACt38RYb1CyiDn_NX774g8RKBCQhtwj1wjKZGERORCrEtBCNINr0e5d7WprKFF8QuIYhAnX6IS2P2lJgxa7ITAV64rJ2JsN4QjF8_rlkEUSUl04YahhbCnq00p7DHy87ue-ehZ7PpA4Nk2TftAb-HYmx-kX-yQX1UHC3JP5cJOb8tOJoixevJPDzNpuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هل ناقشت دعم الصين لإيران مع الرئيس الصيني؟
‏ترامب: لقد ناقشنا الأمر. هممم. أعني، عندما تقول "دعم"، فهم لا يخوضون حربًا معنا أو أي شيء من هذا القبيل. قال إنه لن يقدم معدات عسكرية. هذا تصريحٌ كبير. لكن في الوقت نفسه قال إنهم يشترون الكثير من نفطهم من هناك، ويرغبون في الاستمرار في ذلك.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75369" target="_blank">📅 18:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامب: عرض الرئيس الصيني تقديم المساعدة بشأن إيران</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75368" target="_blank">📅 18:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قيادات سياسية ورئاسات في مبنى البرلمان قبل انطلاق جلسة منح الثقة لحكومة الزيدي</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75367" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLGCNNCudkE1pET1fjTPKvG0nq5E9ELxykin3NWPhGQ_7kSo8JrOuZOpvmbAF3IjDymtvr5yHxBFf4HZbpE8g-S_yzsMsVfi-lMBNV8ved2kV1F1pM7yPZHXJGQAFGgcmKMqs3IZ_dyIVEITBuqgCqI8JqoShqMtY04KUfUFwx_NpFZk3GJ-OSCF_fXHcdEuiCHFHrqz3SIhVF2bSRS9s2QUfADelkS6-4BXf7B71ORpxMUjNok8CE5vY9eGKk2vbkXBxDTGASQU1DOwjwEGFx6kB2bI0KWk3CjsRychN_RCXoIVQ_SUUg8YVPAnguZWX-m2j7RUvx-wyfB_iQezUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرع جرس البرلمان إيذاناً ببدء جلسة منح الثقة لحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75366" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75365">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5hFuEKKzvZCrPH2cbrtGBwVG_SXbOlXMHWsqZ6HJt3SmxpTkhSiUbQAv9QGirHUX6rNC1OV9EXuO4CD_qxDj-vT2N0hyFHK2a4oeXnFh-iu3Uoq5CdwTqUjHPkbCeYLEnqCEuurLMNuN_c0izcQDz8dvPFE4JQQjCt32FjCa_v0FKXW7Gv36euoRDqKQ4PM-GlHk3qRn2G6EZEWjqQ9aqz2u4-naHkoI-YLuyFOV7D5sk9lRJLZkvoFErx6ZwIkUdykyxSl9JIABaG_sXZbt20StWnXoD7PA0NDGN3K0eO5r5fxb0eRK6VXYOMH_PzqsftfVqJzGZ2cSLnhS6Je1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قائد القيادة المركزية الأمريكية:
في الأشهر الثلاثين الماضية فقط قبل بدء عملية الغضب الملحمي، هاجمت جماعات إرهابية مدعومة من إيران القوات والدبلوماسيين الأمريكيين أكثر من 350 مرة - أي ما يعادل هجومًا كل ثلاثة أيام أو أكثر، مما أسفر عن مقتل أربعة من أفراد الخدمة الأمريكية وإصابة ما يقرب من 200 آخرين.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75365" target="_blank">📅 17:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75364">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">القيادات السياسية والرئاسات تتوافد لمجلس النواب العراقي للمشاركة في جلسة منح الثقة لحكومة علي الزيدي</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75364" target="_blank">📅 17:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75363">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فايننشال تايمز:
‏السعودية تطرح معاهدة عدم اعتداء في الشرق الأوسط مع إيران.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75363" target="_blank">📅 17:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75362">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة عيناثا جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75362" target="_blank">📅 17:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75361">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9AgBfOUXV5N0QKg4TFUwvpIu_HczvYYxia3ZX5B6PKQ3mct8COYg3rtfjkN1j5RcT6NlZS8UV2WxZFQ3RoNaLURPBIfusiHToTfE-JYE7JAPzvD2c-kPCU3NexNoMYDIdK_tws7aT3psictsTdbyKG0d7gBqp6yrn7c2JKTLU7c1n1Ts3PqEHJLsl0ZC1VuvrJ9kdeKkU1u2hB8S7d4wsTJrwkzKR4s4OyI74KGrtmyx1kaS8I1M2CgCqwg-8OXOBzrRnmrx51e-AoWxa3yTetJK2vpcLsaM3MptFCceR7JLxwYN7vFNqBpDp20CYuq6cZpgGZAFr6cW0qdMieRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة الاعلام والاتصالات العراقية: ايقاف برنامج (الحق يقال) الذي يقدمه عدنان الطائي لمدة 45 يوم بسبب مخالفة الضوابط والمعايير الاعلامية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75361" target="_blank">📅 17:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75360">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 09-05-2026 جنود من جيش العدو الإسرائيلي في محيط بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75360" target="_blank">📅 17:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75359">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تأجيل الجلسة نصف ساعة</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75359" target="_blank">📅 16:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75358">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الان - العراق   المرشحين للوزارات ورئيس الوزراء يغادرون القصر الرئاسي باتجاه قاعة مجلس النواب</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75358" target="_blank">📅 16:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75357">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الان - العراق
المرشحين للوزارات ورئيس الوزراء يغادرون القصر الرئاسي باتجاه قاعة مجلس النواب</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75357" target="_blank">📅 16:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75356">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صندوق النقد الدولي:
العراق سعى للحصول على مساعدات مالية، محادثات جارية مع العراق حول حجم التمويل وهيكلة قرض محتمل.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75356" target="_blank">📅 16:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75355">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDR2w02_mdLoRwaEPVIfjWFKLxSwukMpnhWPhngCtWBxBzxpEiOX3CHLFYCYrKS7snQFYBtgJW2jbz2yTD4S38XsZQFu0gNZ4pfrrxop8LG4ASMM8BmWjrPGwfYdGAOtX1dFl9XjufrutTJ_mkj2gS75xNgL3YSHMWSYxTihA1jF2ZN4w-27ExfQXHX5flWox2gkzc-JGpubm4813NKW00iQBASp0lwkhfYNg-ljK5a0Mnblwt2a1n7W-PjeiQLOduy4xf1yDiJ9K3vuaDXGXuiizduJgyaT_Yz0cwwLXbgHGETCY4WPooXkFcvDVSO7PG08rXeJ__jUJX4AK2oaPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غضب جماهيري في مواقع التواصل الاجتماعي بعدما بثت قناة العربية السعودية تقرير خاطئ يتحدث عن العراقيات نقلا عن تقرير أمريكي وبعد البحث تبين انه غير صحيح وغير موجود</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75355" target="_blank">📅 16:20 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
