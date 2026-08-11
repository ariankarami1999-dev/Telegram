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
<img src="https://cdn4.telesco.pe/file/YA7iM2qOnU-2eGdwMyjWK_4nIuiQYwK001xAQm0ZIRHtXdkO6oUv_qt2EhNRkiOMekuPqPJu5jFYNbYwNfuBhTHeOYXpYua263Fshp9bd1AULwLhZVHIuu-mlJF0vfDebVixZ5h0tQdka_TM5Z5HQM-jOKo7oem7p8_a2QtpjfZXhjLaEuBav9DhvmUr6Ovep2prKPxq9xn65J33ZU-w41bN5EZ3VdCKYCt32G9UBUmJ1mKUneRshvBAC6243iIY_KNSapY4wAt5gXg_0_qP69SatqktAvVPaewHUeNm69lJ0FjzxfUT9TJmWQ_0TKkcbK7ur6fXKiecl4Jw5mommQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 13:53:21</div>
<hr>

<div class="tg-post" id="msg-87526">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owBfXjiV70sMQEmKMpnHudOEIH1nOnaFWshSV7ZwVfFBStL-8dSRK_ml_SjtQobNjqBmGtOe1pUxrZVJnrx3zx2-Kpp3maqGCH5AeD265K-FJKUclNdz3F7wlbpxxH59zaKvRkKVThpbNFVKQk4y9OwUK7wbe79Xsqs8fAzetIMPWKFlP9P4oZNRh1rnHaf3yf-Q46muiwTMBWemLFg8YcbZGVKW4LEdxXI4nJmTyn1DDKLuLjgVyROoJ1nCBhIXB0gTYKdr05PfUKt86pN7sErCyTG5G4ydz0-HZOwpygxEVbCMzlGvDUhYKXT8elpDq9agQuuDymuVd376rcLnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMmsCojjfVs6JT7linLxsBi1KNoIT-j113CsDVnJrf1bdggTLxCpCXlyU-DOEs65Vt4MP-05tCKRhr-2Y5o11n6wKq99i1Vbt_Xb_9WiOh9y0NoW7iVX5b968NYRnH3Taadkg3-U3GIYbhD7J_PgF02NxNehYV7ljIc4sf4wvQy4BCCYOwIjcny9j7cufN-nzrnMU2JdbFKJaftThkTn18UbAYaIkNz2_nkg1P60SUPYAjABr9DrLgNN_AWbOFX2HTt5QGjXDULQtgvrOiIkatUMBeWBL5SPnZDhJiFVgq7322oCfxrhS91KNR9hlxjVUZqBNCu1b05qcWUlxZDZIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
أنباء متداولة عن استشهاد 3 منتسبين أثناء أداء الواجب في قاطع عمليات صلاح الدين.</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/naya_foriraq/87526" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87525">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/87525" target="_blank">📅 12:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87524">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/naya_foriraq/87524" target="_blank">📅 12:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87523">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2SYH1oTL0nJSe5uEsCttE_ZaIBOlhcG_UGNkUCrFSl-V-8AeUC5UOr6K9DgPj7l79S2k5vcv9s9ZBqcdt0Hl5CvG4DsvevHHPS5oOV6YvvwyLdq4VKpeq7y-z2kX9OFmDmIWmnXprP4WowM7IdomHfDwZOFbeWSK4fSVf1d5UuUPKDGs2Zi_lxXI4mUOr2iDkUXS5QYnmI4dAhRqhBc_xnvulkjuaNCYkigXYUKTuOFU48dw2Hoq_yO0Sw4u55kAL-W3OAFhYtTl_eat_gq1_kML2M-hr64EullB__PzpHUU2p5cxEgS6IgO2z4Y-ot3FJ2122-jalJYlMGSfF06A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
محكمة الجنايات في دمشق: الحكم غيابيا على بشار الأسد بالإعدام.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/87523" target="_blank">📅 11:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87522">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-AlkHa6xF1mzXPf4WZZ2tIvwjACEtPiDK21rgeKzvY7nsMuHim2hXKKUfAPnZTw_kgJI7tzpcxIlNxHN16Mfwl1OjnGhA20FnCJtsEp2HFde0aMIhXUApUdDrlue1el0JU2f6P8tX1EJvorUoUI6DfpwAW099o5nDDoadVOXbZPpHMGPyUSyBw7pxA0yrXM683rT_roTLf4xSEYD5dSUwa31B3qpPEcCSFUaskKTvG3SgCcnfNM_F3OqLuMnf4b-aa_Jlql8_sZ4t-38uCf9cOkjeHCq48Zss3fDIvXY9zaAs644d4lRfZVD6MnvwZmDrM-9R6q0vpkFLPrYF2vRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
محكمة الجنايات في دمشق: الحكم غيابيا على بشار الأسد بالإعدام.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/87522" target="_blank">📅 11:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87521">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قصف اخر باب المندب</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/87521" target="_blank">📅 11:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87520">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قصف اخر باب المندب</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/87520" target="_blank">📅 11:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87519">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
أنباء متداولة عن استشهاد 3 منتسبين أثناء أداء الواجب في قاطع عمليات صلاح الدين.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/87519" target="_blank">📅 11:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87518">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ffc5a740.mp4?token=J0aI7xrvc0Ur_O3Bj78Pm3-U5qeV_Le5l-4kBlu1DMsB60ATZnvKvCT7F0ncXS9lm5SeyPMu70zLTi-ssvmGzrrZwXJLlFI_E3DMds5QLa1d38gCOL-x-EHS3cwQNWvA0uZaEtaloqSyMCvOC5o_QbGXCxmtZrRI9OdjJJv0qG4NLqHd2EJkzXsWbgnYE39IEbRoTW8UviBuJb8i4Quk6TYXxuMoIvK8VrSmtYL-u3IjbxHWi6d3zntYVX0xWdR1U6bZZ8FeEaGlJgB1NSaZS6QuyLq6gX466tWaAmtmJtss3J1ENq84L1P09ScpLa8qFFHq0Mnq-0xV1cPw5l3ZSky5J8KVZiOJnZB8o1WBaZHPCwGgOZuCVvzED1V0NIufAO4Fh0S-m0V5wZqXvh76hizm9KUcIxcIfdSijCFjDu67E4Gfu2waapxhajwN-zX-fTEK9eG-KZD2bY4080k0HiQ5Znzc9OIF_ARqiSv2L5Ks4cXMOSboUlZOTsed8CnP3chFQumQU3fUW3BOgkkkw2GkCsj_JdaCpf4yLB9sbirjFQmBuWVzPNlIInf3-gmNOagUJkOhK5ISjtTdmTeeq2-4gw4HJ-FaMwfczu5j8YGCyQjtRfg9pWctEyzAew8nwf2263A1oeB2lwd2AlRpof0rdZzYampgQ3orGUDNHto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ffc5a740.mp4?token=J0aI7xrvc0Ur_O3Bj78Pm3-U5qeV_Le5l-4kBlu1DMsB60ATZnvKvCT7F0ncXS9lm5SeyPMu70zLTi-ssvmGzrrZwXJLlFI_E3DMds5QLa1d38gCOL-x-EHS3cwQNWvA0uZaEtaloqSyMCvOC5o_QbGXCxmtZrRI9OdjJJv0qG4NLqHd2EJkzXsWbgnYE39IEbRoTW8UviBuJb8i4Quk6TYXxuMoIvK8VrSmtYL-u3IjbxHWi6d3zntYVX0xWdR1U6bZZ8FeEaGlJgB1NSaZS6QuyLq6gX466tWaAmtmJtss3J1ENq84L1P09ScpLa8qFFHq0Mnq-0xV1cPw5l3ZSky5J8KVZiOJnZB8o1WBaZHPCwGgOZuCVvzED1V0NIufAO4Fh0S-m0V5wZqXvh76hizm9KUcIxcIfdSijCFjDu67E4Gfu2waapxhajwN-zX-fTEK9eG-KZD2bY4080k0HiQ5Znzc9OIF_ARqiSv2L5Ks4cXMOSboUlZOTsed8CnP3chFQumQU3fUW3BOgkkkw2GkCsj_JdaCpf4yLB9sbirjFQmBuWVzPNlIInf3-gmNOagUJkOhK5ISjtTdmTeeq2-4gw4HJ-FaMwfczu5j8YGCyQjtRfg9pWctEyzAew8nwf2263A1oeB2lwd2AlRpof0rdZzYampgQ3orGUDNHto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/87518" target="_blank">📅 11:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87517">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6d2a4fee.mp4?token=oBsCfv6hizzIdYq0dYMiyEQYb-4zE63xV_jGM--KgXXKhiycJ4dcdtT6-KafJkhexDZgA104qFu5ZSpVZRFDYZM9CbhJkXz68ekvmDMNNntqh18pSU9cmGe3l7xAu4eUZ7b4-daNtP0kJ8J_KOvXNOrK3iWGx5axPqrTiv8iAxIH9vpxt8OZlI_mYUAkbRUT63ZHc7MVqz8qh5qFU0-vKK8TiI1bipQ1-E8VOyFYDW2J9l80pHvRdDRtByz26wmuZBznxfEa0OwXHQGreIeds-dI_Ee14YQjQkJ66j1GICnY8z6oLh90I9QZQK61ZhlYfNEV6sqYWhKvmO0Q4eTQsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6d2a4fee.mp4?token=oBsCfv6hizzIdYq0dYMiyEQYb-4zE63xV_jGM--KgXXKhiycJ4dcdtT6-KafJkhexDZgA104qFu5ZSpVZRFDYZM9CbhJkXz68ekvmDMNNntqh18pSU9cmGe3l7xAu4eUZ7b4-daNtP0kJ8J_KOvXNOrK3iWGx5axPqrTiv8iAxIH9vpxt8OZlI_mYUAkbRUT63ZHc7MVqz8qh5qFU0-vKK8TiI1bipQ1-E8VOyFYDW2J9l80pHvRdDRtByz26wmuZBznxfEa0OwXHQGreIeds-dI_Ee14YQjQkJ66j1GICnY8z6oLh90I9QZQK61ZhlYfNEV6sqYWhKvmO0Q4eTQsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  السبب في نقص الذخيرة هو أن بايدن قدم ما قيمته 300 مليار دولار لأوكرانيا.  إنهم لا يذكرون ذلك أبدًا. الآن، أنا أيضًا أقدم المساعدة لأوكرانيا، ولكن يجب عليهم الدفع.  بمعنى آخر، الاتحاد الأوروبي - أنا لا أتعامل مباشرة مع أوكرانيا. أنا أقدم المساعدة…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/87517" target="_blank">📅 11:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87516">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe9815653.mp4?token=shbRMM0LxQdI0n49L41NjVvX7fe6ZqrrmfFEnEtlF2Z1gL-U_ZeP6oceCi2wFi-7AZF22ZBg0v5Yg5akVSyjcchxO3IYh8vBWUc8hvh3riMG_pFNuGpNwUM0x5Dd2SuwY02elaQ8arUxm9HV-0LXogdp1DgbOy9spvdvZnQ4nvdafNyqs5cNjsG8Ja2RcnJarHCkz_EUyinEVQgozv9jlZtgCEWxvT48BznxsXsEiE0JMGUQUM22Wngq4bihJvKTlPj6t7BgelcrOvi2OGw0VsyFsY26RDuwj5u0JPe1FrW4H7DcDLKMM_KppEiNWCuJPSGkZFjxTL_5beAE-n34_YQw7RUi9mfZqowD58iVpcbw2vkdG8SHsqm-_szltHIYl056PPyElWRWFtF3HhpS-m7CilPWiBKNBVd1pzyjyvLoJ4fmjy3YW_BtooohF6LuVQPjL2zcLx0MCcCXw6nu3qrQMzeD_NCUF02OogWonxOEYOPQzaiDVjoHbw_LSb-jQdHEsn16iQxAv3pNuWrknN_vtEft7VagI8BNZVFghs79Srod6clzWl3FN1yUA7nTIqspprIacZa3pXv1-98fVvsBDqPjiYGdoTI18xfWrWQznN70Qnc3U-GzTB8CXANOnuRSQ-6NjzxipXQWN8q7I5Jnr0ISGvt1bW5tgWR5y2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe9815653.mp4?token=shbRMM0LxQdI0n49L41NjVvX7fe6ZqrrmfFEnEtlF2Z1gL-U_ZeP6oceCi2wFi-7AZF22ZBg0v5Yg5akVSyjcchxO3IYh8vBWUc8hvh3riMG_pFNuGpNwUM0x5Dd2SuwY02elaQ8arUxm9HV-0LXogdp1DgbOy9spvdvZnQ4nvdafNyqs5cNjsG8Ja2RcnJarHCkz_EUyinEVQgozv9jlZtgCEWxvT48BznxsXsEiE0JMGUQUM22Wngq4bihJvKTlPj6t7BgelcrOvi2OGw0VsyFsY26RDuwj5u0JPe1FrW4H7DcDLKMM_KppEiNWCuJPSGkZFjxTL_5beAE-n34_YQw7RUi9mfZqowD58iVpcbw2vkdG8SHsqm-_szltHIYl056PPyElWRWFtF3HhpS-m7CilPWiBKNBVd1pzyjyvLoJ4fmjy3YW_BtooohF6LuVQPjL2zcLx0MCcCXw6nu3qrQMzeD_NCUF02OogWonxOEYOPQzaiDVjoHbw_LSb-jQdHEsn16iQxAv3pNuWrknN_vtEft7VagI8BNZVFghs79Srod6clzWl3FN1yUA7nTIqspprIacZa3pXv1-98fVvsBDqPjiYGdoTI18xfWrWQznN70Qnc3U-GzTB8CXANOnuRSQ-6NjzxipXQWN8q7I5Jnr0ISGvt1bW5tgWR5y2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
السبب في نقص الذخيرة هو أن بايدن قدم ما قيمته 300 مليار دولار لأوكرانيا.
إنهم لا يذكرون ذلك أبدًا. الآن، أنا أيضًا أقدم المساعدة لأوكرانيا، ولكن يجب عليهم الدفع.
بمعنى آخر، الاتحاد الأوروبي - أنا لا أتعامل مباشرة مع أوكرانيا. أنا أقدم المساعدة للاتحاد الأوروبي. لديهم أموال، وهم يدفعون المبلغ الكامل.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/87516" target="_blank">📅 11:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87515">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIjZJnjnLBKo_7jTEIXXf6T3JZiRK4CwqmnocK4sxA-PXi7pGvL4iFd_Do3BKBWEsptDX0igxP3ytRvqhKy1fHfeic0iMi4hXSELdXPdWgLdgQPM4cE1xBKu4kKy0_mlBny4MjPFA1VRKalWRn55j0gx4n12ghYKwWll4vDE8KM-NUWNRu_pqNWnXBMxm0eLgHQznPK3aQanBZ243OtUC_VO4N7xVwYgF5_UHBAAtK1lBj5QVQGfcVoeXcVwVZMHTNiHvPL30TBmk7cPGh_FQb3I3IVj5GIPEhbj7IDeqwgVOn7XHdlrr23i0pbzF2nO-aCmQ600VAqBSW-hqSsm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
استمرار ارتفاع أسعار النفط وسط تصاعد التوترات في المنطقة حيث وصل سعر برميل النفط الواحد إلى ما يقارب 90 دولار والارتفاع مستمر.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/87515" target="_blank">📅 10:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87514">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حدث بحري في باب المندب</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/87514" target="_blank">📅 09:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87513">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حدث بحري في باب المندب</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/87513" target="_blank">📅 09:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87512">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ebe3dbff.mp4?token=pQlgrDR54ZyvlmgUGHkrXFoTxqsiwZ0LPXrJaywpVRsubyjvIoHWziT51yz2O8m8E6zvvHEFt2l9nbd0a85A4ozVfaGqtcNHfStdDHorJ1b4IVZ7dDu3lDNcEbqGXa5el4M5oHsakZhHzPeqr-UtqyCV9-RzgZzfnyuvqLeiGr_5XTBl4tCRS8h4DAgv9BNIYM3TvnwEy7lnCtJC-9r7tNKnKCUpnP4H7nhqelpkyxThLZtcRjo6L9616EbQOOWNCAwjHydbs-Op4AXYPWXK9JN7MkjJboO38mQ6oBjKmMvMPRxorYJ9G0rG4cURbz5G6BbrMYwUjNFGWLtl5P1z-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ebe3dbff.mp4?token=pQlgrDR54ZyvlmgUGHkrXFoTxqsiwZ0LPXrJaywpVRsubyjvIoHWziT51yz2O8m8E6zvvHEFt2l9nbd0a85A4ozVfaGqtcNHfStdDHorJ1b4IVZ7dDu3lDNcEbqGXa5el4M5oHsakZhHzPeqr-UtqyCV9-RzgZzfnyuvqLeiGr_5XTBl4tCRS8h4DAgv9BNIYM3TvnwEy7lnCtJC-9r7tNKnKCUpnP4H7nhqelpkyxThLZtcRjo6L9616EbQOOWNCAwjHydbs-Op4AXYPWXK9JN7MkjJboO38mQ6oBjKmMvMPRxorYJ9G0rG4cURbz5G6BbrMYwUjNFGWLtl5P1z-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسرب نفطي واسع النطاق بمساحة كبيرة جداً كشفت عنه صور الأقمار الصناعية قرب مضيق هرمز ؛ تشير التقارير إلى أن مصدر التسرب هو ناقلات نفط كانت تنوي العبور دون الالتزام بالإجراءات التي أعلنت عنها الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/87512" target="_blank">📅 09:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87511">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترمب لريل أمريكا فويس:
نتحكم في قدر كبير من أموال الإيرانيين وأصولهم وهي تحت سيطرتنا التام
لدينا 3 استراتيجيات للتعامل مع إيران أولاها مراقبة مدى سوء وضعها والثانية ضربها بشدة الاستراتيجية الثالثة هي الضغط الاقتصادي ونحن نفعل ذلك على أي حال
أكبر تغيير رأيته خلال ربع قرن ما حدث لإسرائيل فقد كان لديها أقوى لوبي في واشنطن
إذا سمحنا للطرف الآخر بالفوز في الانتخابات النصفية فستصبح البلاد تحت حكم الجهاديين</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/87511" target="_blank">📅 09:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87510">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0JhEH97kVKdldeBFvmndmi5vjZHhEnDVllDeQ5i99kx1NXlEoKNJNtxSOd0V2YUs8UAK9esIvWkzkb8MfO2OUREmd6bQP3uXLeBgDikdVBVEpOYAmVVsrjAq-FTWVMA8cZKGW59pN3Pt_Uk5P7mZy-dgocsd6-1B7divCXVUZb9t-pkFo9PXhWcNmKb5pBXGDo4zRjwoDuJeTalKNd65wMrLIdtqCfa9dbhvCJgmbJ5sEIrLvlfzNNA25LZAMI7hsRfcX7D4hXTBFrriIj5gVevCW-2PN51uzLm2WQdD5u4UdlQFrO6lilUlnzrfseT3Q_FdIHXawknPwWiscPLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
سيرتكب الاتحاد الدولي لكرة القدم (فيفا) خطأً فادحًا إذا فكر، لأي سبب من الأسباب، في استبدال الرئيس جياني إنفانتينو. إنه رائع، فقد ترأس للتو أنجح كأس عالم على الإطلاق، بأربع مرات. إذا رحل، فلن يكون ناجحًا أو مربحًا مرة أخرى! شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87510" target="_blank">📅 05:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87509">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvQwA1n1G8r5Wb5LIm2xmG1r9YSBBptnum-kgC1fCDdVR83iSh7BcjKonAsYnueXC_ZKdQI7T_FyLElMMnL9JTdVPJ7Hzod3jsH48o-_94oxnUIGVSzwxYIB43SUHD464YbeNQg6VK-BmIH6QxDQejayv7cNYD97Zi7i7OQ-vbMnmzRIbMsP1tM77BlT1FNnMxWuLc8yz_b5MPmD8fQwC_cLfzfHlKVRkoHp1jVp0nN3T3sPOAXxWUEY8Yy81ziTKJYUoSoJ9NYy0RDQqclcG3pDALGzJuFzAyUZ6EeRyK1pACri4NGrMxT4GzJWD0vfpCc7prj1Em-PisoEBlrotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تطلق موجة صواريخ نحو معسكرات مرتزقة السعودية في مدينة المخا.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87509" target="_blank">📅 05:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87508">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6c0e1a2e.mp4?token=Pj4ZX8XVHHyeRrkWzy9Gle8kV4i6Hpankj5Vqi9G7n2MJQfOi3qerA7bKE-TLTOvZFT_3jWlFQ8XkMpn82AhSeSBxjHX9Uuw0Lpxt1QwCzEYmIjRjm0C2wFFXbSQs2aN2JHo81npVepbHwRCuaxb7FAVF6bliN7UsrFGAMHmN8HR7kDhYwKo00ZSfNUVG_6Vcz2TCP0diB1eqNdRsAELvYGPJtE9GCTvCegLPnpY-xIGR5Drx_jN8MbcBubOHo0xOLaKkzfk7_4ScfmKq6mf_4B5_ZlypbNGPHYynO4EOZxwjv-rFubg_mW-VasTxuGpM5SJ-3xKqR6yiWj36YSOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6c0e1a2e.mp4?token=Pj4ZX8XVHHyeRrkWzy9Gle8kV4i6Hpankj5Vqi9G7n2MJQfOi3qerA7bKE-TLTOvZFT_3jWlFQ8XkMpn82AhSeSBxjHX9Uuw0Lpxt1QwCzEYmIjRjm0C2wFFXbSQs2aN2JHo81npVepbHwRCuaxb7FAVF6bliN7UsrFGAMHmN8HR7kDhYwKo00ZSfNUVG_6Vcz2TCP0diB1eqNdRsAELvYGPJtE9GCTvCegLPnpY-xIGR5Drx_jN8MbcBubOHo0xOLaKkzfk7_4ScfmKq6mf_4B5_ZlypbNGPHYynO4EOZxwjv-rFubg_mW-VasTxuGpM5SJ-3xKqR6yiWj36YSOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع حريق كبير في مصنع خلط وتعبئة الزيوت بمدينة الزاوية الليبية إثر استهداف بمسيرة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87508" target="_blank">📅 03:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87507">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec3b4b656.mp4?token=SbSWsUREiaHL5SPZUDTGPgnj_qcDTJtMjLNLvXK4MVgPzwXMY7zQLxYwR15k0KJ4pAKjIu9cYjHDZHLf7vQWzDdEkgCgt_sW8v_Bpl1nr1AEUj9CpIBS4gGyMw43Fc3PSVX3HzKDQi9MnBMpQP1pzfCjoz2BAEuX0ZWEqdqPoh2UA4C2B9tRA_vW5pwnMVQvdNs0JKlp5r24hSKeYml-fVmOagF-WVeh-fbamnZIbY8lwZ7tB1nJb-QeXnBq-pgmetTzGbr1PrPTVpYJuGaPy5t3FwelJCjrNO5W4z1mPD17LukpMob9DsOw1jACLo-Nz_tUf7YE9m0M4Qx-e93SSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec3b4b656.mp4?token=SbSWsUREiaHL5SPZUDTGPgnj_qcDTJtMjLNLvXK4MVgPzwXMY7zQLxYwR15k0KJ4pAKjIu9cYjHDZHLf7vQWzDdEkgCgt_sW8v_Bpl1nr1AEUj9CpIBS4gGyMw43Fc3PSVX3HzKDQi9MnBMpQP1pzfCjoz2BAEuX0ZWEqdqPoh2UA4C2B9tRA_vW5pwnMVQvdNs0JKlp5r24hSKeYml-fVmOagF-WVeh-fbamnZIbY8lwZ7tB1nJb-QeXnBq-pgmetTzGbr1PrPTVpYJuGaPy5t3FwelJCjrNO5W4z1mPD17LukpMob9DsOw1jACLo-Nz_tUf7YE9m0M4Qx-e93SSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تطلق أسراب من المسيرات نحو معسكرات ومعاقل مرتزقة السعودية في مدينة المخا اليمنية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87507" target="_blank">📅 02:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87506">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
واشنطن بوست:
تم نقل الرئيس ترامب سرًا من أنقرة، تركيا، على متن طائرة من طراز C-32A تابعة للقوات الجوية الأمريكية الشهر الماضي، بعد قمة الناتو، وذلك بسبب تهديد إيراني باغتياله، بينما أصر البيت الأبيض علنًا على أنه كان مسافرًا على متن الطائرة الرئاسية "Air Force One" التقليدية.
في البداية، صعد ترامب إلى متن طائرة بوينج 747 أمام الكاميرات في مطار إسنبوغا في أنقرة، قبل أن يتم نقله سرًا إلى الطائرة الأصغر C-32A باستخدام شاحنة طعام تابعة للمطار. ثم أقلعت طائرة 747، وعلى متنها صحفيون وموظفو البيت الأبيض، بهدف تضليل المراقبين، بينما سافر ترامب ووزير الحرب هيغسيث بشكل منفصل إلى بريطانيا.
حلقت طائرة C-32A التابعة لترامب تحت رمز الاستدعاء العسكري غير المحدد "RCH18"، مع إيقاف تشغيل الأنظمة التي تسمح بتتبع الطائرة علنًا. وفي الوقت نفسه، استخدمت طائرة 747 المستخدمة كطعم في النهاية رمز الاستدعاء "AF1" على الرغم من عدم وجود ترامب على متنها.
بعد الوصول إلى قاعدة سلاح الجو الملكي في ميلنهال في بريطانيا، عاد ترامب إلى الطائرة الرئاسية "Air Force One" التقليدية قبل أن يظهر أمام الكاميرات، مما حافظ على الانطباع بأنه سافر على متنها من تركيا.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87506" target="_blank">📅 02:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87504">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8603ec3c72.mp4?token=alQUoBWMmL9ki7IZaHvn9-PeDgaGe6f7ShwYIE-1Vc8QPoGP98x3_XXafUJ4nkoNRdbVwNImTK_9qFfY9_TqyFQu-eZQ4R69vPPiN40PhdDwEU5PCK_xNDdacd89lpq6YOSV2uquOLhIsLkaR8NWk5UCyxY3nEVIr3c9iJIkRGScLf3aG8ZQS2rROmUItOd5624jBNR9p8Ar_fp-G5SO4VpdSm3vz3Ds1vxdUlGpLbTxdz7yEWcfqkEsv6ExPbo4aXIulR6XlD8kCQwVZ3CTC7toLhJmhIi2Wv6GNRmiXhlAZgpgDiEOuXDZKvJcW5Yc8iXwu3xd3OJbPtgaPPXdzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8603ec3c72.mp4?token=alQUoBWMmL9ki7IZaHvn9-PeDgaGe6f7ShwYIE-1Vc8QPoGP98x3_XXafUJ4nkoNRdbVwNImTK_9qFfY9_TqyFQu-eZQ4R69vPPiN40PhdDwEU5PCK_xNDdacd89lpq6YOSV2uquOLhIsLkaR8NWk5UCyxY3nEVIr3c9iJIkRGScLf3aG8ZQS2rROmUItOd5624jBNR9p8Ar_fp-G5SO4VpdSm3vz3Ds1vxdUlGpLbTxdz7yEWcfqkEsv6ExPbo4aXIulR6XlD8kCQwVZ3CTC7toLhJmhIi2Wv6GNRmiXhlAZgpgDiEOuXDZKvJcW5Yc8iXwu3xd3OJbPtgaPPXdzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مروحي مكثف يحلق في سماء مدينة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87504" target="_blank">📅 02:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87503">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67e2ac79b.mp4?token=YaXvGyCRyXfteFnhtJ7aXfavrFX8vrhYuZqUmcj_4LMsbbOzAvvlefs68WtQsHVhcnT8YBtO_CwLqhj1cvjJhd40zxI_FsTR6p6v1BUzspAPmmO3vxz87kPuxb6nlKvkQloNa8nj5cCzvzx-dU78Al8iuiUopCV6UKsPwm39tkq9BtHZsauYH95IiH0xmeND7-Cp-TnlIEZfkRRC0Hr9GNb2SlpBiDOFdtjf0VufRN8EMGdOE-F0qN6A7Cc8PlO97OsWXaV6GWjD0jHuKQYbfHpv4dCuoQhI_92gh-2tE_mpxqdR035Gv-j6NKsAN_aRgPy-KI1ztIbfisoOU8RIaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67e2ac79b.mp4?token=YaXvGyCRyXfteFnhtJ7aXfavrFX8vrhYuZqUmcj_4LMsbbOzAvvlefs68WtQsHVhcnT8YBtO_CwLqhj1cvjJhd40zxI_FsTR6p6v1BUzspAPmmO3vxz87kPuxb6nlKvkQloNa8nj5cCzvzx-dU78Al8iuiUopCV6UKsPwm39tkq9BtHZsauYH95IiH0xmeND7-Cp-TnlIEZfkRRC0Hr9GNb2SlpBiDOFdtjf0VufRN8EMGdOE-F0qN6A7Cc8PlO97OsWXaV6GWjD0jHuKQYbfHpv4dCuoQhI_92gh-2tE_mpxqdR035Gv-j6NKsAN_aRgPy-KI1ztIbfisoOU8RIaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
هجوم جديد بطائرات مسيرة يستهدف مصانع مدينة الزاوية في ليبيا.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87503" target="_blank">📅 01:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87502">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87502" target="_blank">📅 01:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87501">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يستهدف العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87501" target="_blank">📅 01:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87500">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey3kYypzikks_YWvCkXTCcajkcPfi4g7imGbkMty3k9JJiOUcvK79NExJkZGL2ExSDkgHoBEwFKHedeS3vM1cU5sMb-DzoDlXaHiUoWCdH10wlaSDlyz3FRftoBzyDIZBGanz3qCtQ-d6Pj9q2VJEywQ4721RdWPy1vgKWqH9u4wKd3dkNU5y7ETldH1VprR3xD5mWvGIPOQbF86eEZ3lb3ITkL6Aq74j4_Y8GcTMNDWJFOf6Q4k0k5wQr7NBXzaqS8D15IxxWkFHCDLPWnXNE4XCnuAH1D8qSoN6S4_d-wXML2RVRsuhUR8_--knqe6hLtWZ4fN49F92Cu-aTvfFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
به نیابت از گروه‌های بسیج مردمی در عراق، انتصاب "شیخ ابوزینب" به سمت فرماندهی بسیج در جمهوری اسلامی ایران را تبریک عرض می‌نماییم، و تعهد می‌دهیم که بر مسیر رهبر شهید انقلاب، آیت‌الله سید علی خامنه‌ای، استوار بمانیم و پشت پرچم سید مجتبی خامنه‌ای باشیم تا زمانی که دشمن آمریکایی را در این منطقه به زانو درآوریم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/87500" target="_blank">📅 00:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87497">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFLomdahIBVn-DFDrzMhPUU6YtoD0nxSeYNDlvNhW94G3EpIX39OlRg6vKTfvqiFBtag_xmF_VHKJKNCELRmKD28YTWgET-Fwm-RsuFwTqAkfkuqGmWJF5MpGgSMMU2qdtvg4hgI5Ba2wvVuzNmCcdxYdBwFB9-EiMvDCkj5fA5PDWb2aNMNW_dUhji3G13EZT-pwSYCBFr2PlUfXzOFxc-n3-7F9bpGXxFWq6f09cqaUZK4CDYDWv7RBaPeml8AuVXn1xQ2MOW2MclzDg7sozNCVzuez4ay-kY0gv0gZZil7GymtVmf5sVcdjbILAcgM0v5FnYV5V1T9suQLsQZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d2884ce92.mp4?token=kQAMGZh2LMbwK1FzROLv6UtsYD4wmUR6rcc-IIX76_C21y2Q7zwgmlm1124FzCOAkwfJFN7q0jJGKT_pAFP83OiHt98G_SzrNd-w9BKfqtjxoGpm-hIJbRlC3EWrcbDRWA9o8JYNzmk9U_xnAKTotaXbijFlwCn5CLERYvs8BKmH8owuk4bT4s5neWbdNYfiLeUuDB5UVUgjK-deovRLJ83Vm1GIaM1dZ1NHx5C7MueTAanYXVjMI_w04gbWbvwNbnv4LiuQca_fu_f4stMdVr-icK9Q-vnjO65EwiChjFLCEbtb_6zOxz_Fc7yAwjEHFPjre7AcoleGiZNI7UHTAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d2884ce92.mp4?token=kQAMGZh2LMbwK1FzROLv6UtsYD4wmUR6rcc-IIX76_C21y2Q7zwgmlm1124FzCOAkwfJFN7q0jJGKT_pAFP83OiHt98G_SzrNd-w9BKfqtjxoGpm-hIJbRlC3EWrcbDRWA9o8JYNzmk9U_xnAKTotaXbijFlwCn5CLERYvs8BKmH8owuk4bT4s5neWbdNYfiLeUuDB5UVUgjK-deovRLJ83Vm1GIaM1dZ1NHx5C7MueTAanYXVjMI_w04gbWbvwNbnv4LiuQca_fu_f4stMdVr-icK9Q-vnjO65EwiChjFLCEbtb_6zOxz_Fc7yAwjEHFPjre7AcoleGiZNI7UHTAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
احتجاجات واسعة وغلق عدة طرق من قبل المتظاهرين في محافظة واسط العراقية بخصوص تردي الكهرباء وخدمات اخرى.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87497" target="_blank">📅 23:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87496">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الاعلام السعودي:
قائد فيلق القدس إسماعيل قاآني يصل بغداد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87496" target="_blank">📅 23:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87495">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/107e5a4702.mp4?token=Ep2IbXW6zFdiEkW_x1U0zTQ5e1BKh6cMnX0LEdx_sPNSRVYck07cG6vuHYp8jajPB9FFdaWmyfdg57Elb-gnYFjA8Ur21Cs2CevCwnM5myPlaBeGemLoLgR1c2ej7WAL5Ch9KlF8mWtZN_ExokfRlfuOS84yO6GtEaQ0xbzVc_RwFrygs2mG3yyIIOwApzvpK_b2yxdhreO7KqM5mnJfeFFnmmJdyCOT_SrY73axN3rIGVflSgsx9dr2Ma9nwMDqVP-CzsOPYU5VaHVDBg6iWZtfrIaytyrtZW-PLk9uLpJNCD-meSdColQC4pvfQA7ST2tulthMgjS34bVjgVjRA3xKPLDVOS81JeSF5q5IdHQjYsbCYwgttkK3r2XU9ozRG38-xn4lArjH8FjQURrwrxq-R2j1ttsfc6Guf-R85jB6kKb4otgiX5J9M3-3mfc8M4tasNzLJEs5y6dmnT1zKVnvIyt0YcTvSYxhQ43JwXetuE-_BasxjE5eQKHfu93ZDJ2Nwg_v6GsRaSE1NCZAEMErpYUr5ps1wmAUABIFZfHJ-JTdSAXCfvO5Nto-S2uHMAp7hqW4hlVTrHeip7BIE7qhjP13N7-zILAWQpA5eRiTYiNGNnsTFee-qhSRbvfQ1mYnmw5lrMAfgFbltfSaz0kSLxsFff9LaPkyRYYAlZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/107e5a4702.mp4?token=Ep2IbXW6zFdiEkW_x1U0zTQ5e1BKh6cMnX0LEdx_sPNSRVYck07cG6vuHYp8jajPB9FFdaWmyfdg57Elb-gnYFjA8Ur21Cs2CevCwnM5myPlaBeGemLoLgR1c2ej7WAL5Ch9KlF8mWtZN_ExokfRlfuOS84yO6GtEaQ0xbzVc_RwFrygs2mG3yyIIOwApzvpK_b2yxdhreO7KqM5mnJfeFFnmmJdyCOT_SrY73axN3rIGVflSgsx9dr2Ma9nwMDqVP-CzsOPYU5VaHVDBg6iWZtfrIaytyrtZW-PLk9uLpJNCD-meSdColQC4pvfQA7ST2tulthMgjS34bVjgVjRA3xKPLDVOS81JeSF5q5IdHQjYsbCYwgttkK3r2XU9ozRG38-xn4lArjH8FjQURrwrxq-R2j1ttsfc6Guf-R85jB6kKb4otgiX5J9M3-3mfc8M4tasNzLJEs5y6dmnT1zKVnvIyt0YcTvSYxhQ43JwXetuE-_BasxjE5eQKHfu93ZDJ2Nwg_v6GsRaSE1NCZAEMErpYUr5ps1wmAUABIFZfHJ-JTdSAXCfvO5Nto-S2uHMAp7hqW4hlVTrHeip7BIE7qhjP13N7-zILAWQpA5eRiTYiNGNnsTFee-qhSRbvfQ1mYnmw5lrMAfgFbltfSaz0kSLxsFff9LaPkyRYYAlZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: ما زلنا نمتلك القدرة على التصعيد، ستطالب الولايات المتحدة بتعويضات مالية عن الأضرار التي ألحقتها إيران.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87495" target="_blank">📅 23:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87494">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
🇸🇾
‏
الاعلام الاميركي
الوكالة الدولية ستزيل قريبا مواد نووية مخزنة في موقع سري بسوريا.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87494" target="_blank">📅 23:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87493">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af84017206.mp4?token=P5mflu4ypQ9u8KUb3LTqZYsqlQQklxY8Qyxq7IOjxJbQIp2zLL-VSBQwMFeeAvHb7SHb5p6KfAzpO4KRPJ4q5pqqHfyR9BMPtQpr3EDiXK7VToc60mPTSCTZY6eH2RRXkedzOCRW5SLELwxTm06i3WP3Nu05OimkR15UcqVxb6Kl6fqCsTLpdNI5uRIf4dY7QlpfycQuglI0HXrc-DqlzBO9piNY6ngNDXurBwmBnbhDZ9A2A9O6t7sfubuXE3L44QJQ02FH6lJy3lIWcGsJN-nBjxV-aD8kmqe2qsmJ0DqAvnBxz5GH8E2LfhNTtNMEe4Q8-yv50PxGFHsO2Og-0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af84017206.mp4?token=P5mflu4ypQ9u8KUb3LTqZYsqlQQklxY8Qyxq7IOjxJbQIp2zLL-VSBQwMFeeAvHb7SHb5p6KfAzpO4KRPJ4q5pqqHfyR9BMPtQpr3EDiXK7VToc60mPTSCTZY6eH2RRXkedzOCRW5SLELwxTm06i3WP3Nu05OimkR15UcqVxb6Kl6fqCsTLpdNI5uRIf4dY7QlpfycQuglI0HXrc-DqlzBO9piNY6ngNDXurBwmBnbhDZ9A2A9O6t7sfubuXE3L44QJQ02FH6lJy3lIWcGsJN-nBjxV-aD8kmqe2qsmJ0DqAvnBxz5GH8E2LfhNTtNMEe4Q8-yv50PxGFHsO2Og-0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب بشأن إيران:
ما زلنا نمتلك القدرة على التصعيد، ستطالب الولايات المتحدة بتعويضات مالية عن الأضرار التي ألحقتها إيران.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87493" target="_blank">📅 22:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87492">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3123d44ff.mp4?token=JVjKOAgpmnrG3qPfohdfyhRH4Sk2q2bCfEN88rglKVLOBwJBswHJNUeSsMn_QlBPC7SK_k4TUoJmH9koS3jBuLn3ZkDDsQ7ew5TkMWzAe0mwvIhaq1lG7PiBxBpFT4vi9EQN0vSOzIPYW1cvjLj_10lhm75i5AJQhRXJwq2Mcnc84QE_HfF9sUETj3rNYbmXtXlKQ6K1XmtPJLufMsRkeRysPaFQixeW14HBbKCD2GfZYUCICBXBYfmNZxig4WwKkfVu_Sh3s64VcBv8ZxTGoMGAOTw9yI1XPqtmQeCVmuCdWUT_ah2w82_I5DglUUyKSFr-6cCKDiYuzQMpfktxHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3123d44ff.mp4?token=JVjKOAgpmnrG3qPfohdfyhRH4Sk2q2bCfEN88rglKVLOBwJBswHJNUeSsMn_QlBPC7SK_k4TUoJmH9koS3jBuLn3ZkDDsQ7ew5TkMWzAe0mwvIhaq1lG7PiBxBpFT4vi9EQN0vSOzIPYW1cvjLj_10lhm75i5AJQhRXJwq2Mcnc84QE_HfF9sUETj3rNYbmXtXlKQ6K1XmtPJLufMsRkeRysPaFQixeW14HBbKCD2GfZYUCICBXBYfmNZxig4WwKkfVu_Sh3s64VcBv8ZxTGoMGAOTw9yI1XPqtmQeCVmuCdWUT_ah2w82_I5DglUUyKSFr-6cCKDiYuzQMpfktxHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الضربات الجوية التي دمرت 8 مضافات لعصابات داعش الارهابية في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87492" target="_blank">📅 22:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87491">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea061f9pNXoSrobayE28Bxe0mNVUQxZAq5UooTWxza2eYp8xODcPiCvbo96yKunLikswYRKnZ8gc4zfbsp2UcF9aUrI1b2jLFB8XhzsoCvne-Fmzl7ChWDJwr_ndB1WCXK4MqI7TEt1MUUkwmuMb9yp6teZ5Wz-ADUU0zGQoE78kwKm3r_4pYp62eFwnEi5zFNo1hc4xT-pyh_8E7ugeCSxFMjv_-Y9xF-xLDxxFs-j8Pj4zZXeFf43XfpR_6FoOh4KvxXR8YM4kBNRunROd-lUt2LBFw14m6hRWEOYQ-GnSY8D0uqjO0NCodzb2wlY2gnYja91Z_wuopEc2WO_lng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحيدي من جديد...</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87491" target="_blank">📅 22:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87490">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75311b4b2d.mp4?token=b2dxpjjySwVP-rZyfR29tPiP7Zm3olgYJBHmHOh5LlEa5ncGXHi8zCZRla9YFDNhOJAGLGhNuiyGsKBbiH_tvhSDDEnEilmqd1BGgxi6SqiRHuTrxboF1z2_NjzKDiH5vdDwprDVqGh4CrFF_woHDycpPJDIZFmhEQyNk_uQjEMJd2x5f2nJquKCPBPZ-LVrp16tX8_UXkJG9Hdo8cgOQrsWBHtUwbkQn4hbv7h5cnFhDXJcHTe5oPbp1LLWUI98yNe3faPMDZO4aXkwXxoXKNkm8uAmP_3p6ZDIjZC6HFs_x_6KivkjGfmf8P4NObRAOR3_lQSEaSgH3ZmoTyF2ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75311b4b2d.mp4?token=b2dxpjjySwVP-rZyfR29tPiP7Zm3olgYJBHmHOh5LlEa5ncGXHi8zCZRla9YFDNhOJAGLGhNuiyGsKBbiH_tvhSDDEnEilmqd1BGgxi6SqiRHuTrxboF1z2_NjzKDiH5vdDwprDVqGh4CrFF_woHDycpPJDIZFmhEQyNk_uQjEMJd2x5f2nJquKCPBPZ-LVrp16tX8_UXkJG9Hdo8cgOQrsWBHtUwbkQn4hbv7h5cnFhDXJcHTe5oPbp1LLWUI98yNe3faPMDZO4aXkwXxoXKNkm8uAmP_3p6ZDIjZC6HFs_x_6KivkjGfmf8P4NObRAOR3_lQSEaSgH3ZmoTyF2ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في ثاني حادثة في مصفاة الزاوية حرائق واسعة تطال المصفى عقب انفجارات مجهولة</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87490" target="_blank">📅 21:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87489">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658af79ef2.mp4?token=B2JVcZp0xSjxK6NUbqSkJJHtE9uLC_QOL48STyN8vhJuvuzJfU_YyeD1OY5z-8mJ6LGCuTu7GYy-m0piEWkP4K7SQ43UeYYDd5C9j5LgzvRT_0JJwPCYdFbvQOQiufkGEv-QKtOZc5GVxJ4m1QMeixeF8lTxxBec7vZF_mVnq2J_XtfmZJLxwnZjGr6QFf_4UjeysC71a4GbT3HC4LpiKkDDOAAxhsOyangAQOfpAH3IPciVSv9pCQthbIMDIM8r32Cz_HDJCYBtNZPxkLy1VXrTkZdzbjI01OBzGVBQHEtcHa2UeaeLQzcp0BhlrU97TlhqLTTOtJ3mIFH6U1NcaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658af79ef2.mp4?token=B2JVcZp0xSjxK6NUbqSkJJHtE9uLC_QOL48STyN8vhJuvuzJfU_YyeD1OY5z-8mJ6LGCuTu7GYy-m0piEWkP4K7SQ43UeYYDd5C9j5LgzvRT_0JJwPCYdFbvQOQiufkGEv-QKtOZc5GVxJ4m1QMeixeF8lTxxBec7vZF_mVnq2J_XtfmZJLxwnZjGr6QFf_4UjeysC71a4GbT3HC4LpiKkDDOAAxhsOyangAQOfpAH3IPciVSv9pCQthbIMDIM8r32Cz_HDJCYBtNZPxkLy1VXrTkZdzbjI01OBzGVBQHEtcHa2UeaeLQzcp0BhlrU97TlhqLTTOtJ3mIFH6U1NcaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87489" target="_blank">📅 21:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87488">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجارات في خزان وقود في مصفاة الزاوية في ليبيا ولم تُعرف طبيعة الانفجارات بعد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87488" target="_blank">📅 21:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87487">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2e77472c.mp4?token=MF4vEcYQ2OaFPye-ZygINgIPx4rAWMhXVWc28ifuCmUOl-9mNfT9jyNyI3k8R5D2J5evvWnUzZ-gwlHPCGHiQmTdyuyH8p-jjdpiaHkUgQNebIymL6evJKZScCqx2Gvhi_HZ2sMAuYPr5PG2r5M6tUK3UaDGlKxTLiUEJX-cr6pzvBvDsGLIC63ZjFPkKLOe7OPQRBCyVocM9LefJ9h4SZjKEMoJSQDbdFPkK2iRoNCsz0AVtJz2kQDeAqDYqXLEH3gymTtkw5J6RygKmjbSoDhyvBIhpGDXdtBAnT0PO2c-_LSIJsvVdI7C0rvHXVV6nAWYfThzMdS8lTvdgbau2oFAzxijjbo9_iSsK-SJRkRcgUeQFOuUjMRCZ62x-_WAt0nyFarFDikvaGqnhjqTr7748gzuod5rRXXdXNFFBeGYpatr8QeMEF-aeQmv-kpJ_uWmFJR5U2Wa3hM_Y2nk0_edt5c39_31G3E-WF3JagsxwefCc_GtyBFsk12FeX5Rcrur3nfLaIwFyQu0_1QEcKzn8OIPXewoAQuH4UvXNEyxxIMnEBVQe_lThw1y-l0TiD_TPgzyqyHFglAYwa2Q6H8IK1YFLOBWLnJfDFxRZ0QSqUh3fywlWdidEekZS9Acm9pmKQxX7je1emVOm438DnpnnGFkZqsEBtxBdmqwS88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2e77472c.mp4?token=MF4vEcYQ2OaFPye-ZygINgIPx4rAWMhXVWc28ifuCmUOl-9mNfT9jyNyI3k8R5D2J5evvWnUzZ-gwlHPCGHiQmTdyuyH8p-jjdpiaHkUgQNebIymL6evJKZScCqx2Gvhi_HZ2sMAuYPr5PG2r5M6tUK3UaDGlKxTLiUEJX-cr6pzvBvDsGLIC63ZjFPkKLOe7OPQRBCyVocM9LefJ9h4SZjKEMoJSQDbdFPkK2iRoNCsz0AVtJz2kQDeAqDYqXLEH3gymTtkw5J6RygKmjbSoDhyvBIhpGDXdtBAnT0PO2c-_LSIJsvVdI7C0rvHXVV6nAWYfThzMdS8lTvdgbau2oFAzxijjbo9_iSsK-SJRkRcgUeQFOuUjMRCZ62x-_WAt0nyFarFDikvaGqnhjqTr7748gzuod5rRXXdXNFFBeGYpatr8QeMEF-aeQmv-kpJ_uWmFJR5U2Wa3hM_Y2nk0_edt5c39_31G3E-WF3JagsxwefCc_GtyBFsk12FeX5Rcrur3nfLaIwFyQu0_1QEcKzn8OIPXewoAQuH4UvXNEyxxIMnEBVQe_lThw1y-l0TiD_TPgzyqyHFglAYwa2Q6H8IK1YFLOBWLnJfDFxRZ0QSqUh3fywlWdidEekZS9Acm9pmKQxX7je1emVOm438DnpnnGFkZqsEBtxBdmqwS88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
إيران جعلت ترامب يشعر بالخوف والقلق الشديدين، لدرجة أنه بات يحتاج إلى نظام دفاع جوي قصير المدى من طراز AN/TWQ-1، مزوّد برادار AN/MPQ-64 Sentinel، لمرافقته أثناء ممارسة رياضة الغولف.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87487" target="_blank">📅 21:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87486">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4213d8a3.mp4?token=fnA53eRPDKTSS4t_27m2usqTiBldLsSJRuJJi5Maxxcij5YVN1jNBlaCV8leccyHiZuUvOQxWipmP-Ru3XV7lfO438EIDDfPBmq-8MS5C-UJWZ1INatCO7uJ4vQqLK-qmUXcpvz65AT-nOfJRmGm5pURAVWerlDlNiI0YhFqKiT8oBH8KrU7KaRAugGtcLuOcD9GaUmQFJ2351Hd8xYgwpfUwBD1dHjxLB5pPm2k2o0_SZo1OZ8Hpjrfxkuye0lbKVOfdOXtujkUbb1QIiOLspn4BS5T1w0Sezb9F6UeEm2HX5vmbV1gEqvOj7JhIZvNDEElvnXiFQtSWJ-Kg5HKVDlqjQG9P1z_3AvS5zY2TC3sNSrzCd5ADLUoQfCgX1nbKyiSTzv3UHlHDd8TEOaVGVKlr1vZprvcl-q0jWiyEjHyEOR2fXcjmrUK_GeRzCZ8CmtC83zDY4mtK8ifHQCFNih3u0ijdP-qeExW_KwbJciHmqrxPlPnvqRdLRPwPG19cJhFQFLjB-3PktBFD93dpM1pEnEYCoIERjFSrctXwCthpgCpcdiOpylabafYIfH9nurldAbIQsSulxrpu95geOf5pM9f_nhIj9yThk4HhwMiHLU4lHFBe5Z2WOIo-dk8b28YkJ9B2tud4lrhbne0J-owKqMl40SH_Tb8RDsknCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4213d8a3.mp4?token=fnA53eRPDKTSS4t_27m2usqTiBldLsSJRuJJi5Maxxcij5YVN1jNBlaCV8leccyHiZuUvOQxWipmP-Ru3XV7lfO438EIDDfPBmq-8MS5C-UJWZ1INatCO7uJ4vQqLK-qmUXcpvz65AT-nOfJRmGm5pURAVWerlDlNiI0YhFqKiT8oBH8KrU7KaRAugGtcLuOcD9GaUmQFJ2351Hd8xYgwpfUwBD1dHjxLB5pPm2k2o0_SZo1OZ8Hpjrfxkuye0lbKVOfdOXtujkUbb1QIiOLspn4BS5T1w0Sezb9F6UeEm2HX5vmbV1gEqvOj7JhIZvNDEElvnXiFQtSWJ-Kg5HKVDlqjQG9P1z_3AvS5zY2TC3sNSrzCd5ADLUoQfCgX1nbKyiSTzv3UHlHDd8TEOaVGVKlr1vZprvcl-q0jWiyEjHyEOR2fXcjmrUK_GeRzCZ8CmtC83zDY4mtK8ifHQCFNih3u0ijdP-qeExW_KwbJciHmqrxPlPnvqRdLRPwPG19cJhFQFLjB-3PktBFD93dpM1pEnEYCoIERjFSrctXwCthpgCpcdiOpylabafYIfH9nurldAbIQsSulxrpu95geOf5pM9f_nhIj9yThk4HhwMiHLU4lHFBe5Z2WOIo-dk8b28YkJ9B2tud4lrhbne0J-owKqMl40SH_Tb8RDsknCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تُعرض للمرة الأولى توثق اللحظات الأولى لانتشال جثامين شهداء العـ ـدوان السعودي–الأمريكي على قطعات الحشد الشعبي، وتحديدًا في قاطع عمليات ديالى.
وقد صُوِّرت هذه اللقطات قبل وصول فرق الإنقاذ، علمًا أن مصوّر المشهد كان جريحًا لحظة توثيقها.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87486" target="_blank">📅 21:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87485">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqhgbQQJw550fAF3ppXjtaGAk1Nof0OXpo5OoUwqiTKaBgW5M-lbHBtkqMylZPAEh2vn8qLb-q6be7A0un15wt4joWooVxfv_g-6obAcv45PFENGJ0TGOoQMGVSBIca2CYW7RvsDoA3jvaMof57sjcA8pKBkh8nTvgfUOjAcYQaHgI2G6uUTyp-jPl-ixQUUT7lIOgqENKA_GQVrDEn3UfOrpsQE5Gi7nISkpUeniqITGKCI13DLUq2HRgojkXTQHNtMaxo0R6rnLWlVk5XgAZn6rQc-uzW_-mRw7MCuqzthGiadMd0f4IlAUe_I2s7eqrWSl-xSYblQ0ALR8WaO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: أرى أن ممثلي الجمهورية الإسلامية الإيرانية يطالبون بتعويضات عن الأضرار التي لحقت بهم خلال النزاع العسكري الذي استمر خمسة أشهر (والذي بدأ لأنهم يرفضون امتلاك سلاح نووي)، على الرغم من أن هذا الأمر لم يُذكر قط في أي من مفاوضاتنا أو اجتماعاتنا! لكنها…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87485" target="_blank">📅 21:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87484">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔻
تجميع لضربات انصار الله في اليمن وهم يدكون تجمعات ال سعود على غرار لحن اغنية Believer.
مشاهدة ممتعة...</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87484" target="_blank">📅 20:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87483">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=qPX9UnUAE9HUtYL_q7m-b2DsWbE2Z7GMLFf79O9Uv-DdciqS0-sh3hR7ZBmw47hgwmwDwmbwX4OiETxJ3TfWC2pi2JJHa-PbR7ESvx3N4pgsPpLKWiW7i2SpYCD_cF8b5Gka-YpKiFEXaT5DTjAoUztSry75t4Ct9qALMTbcs4tf8QLo5TV--fe4Qim9HqHyGsASfdPD85mOaPDAeWOTrI_20qSTWT5E7QYtQxSG7mqi4KFRR9tcZm6QVGfgtaQ2BkCqfab0-ZJIowWbLLe2I2slY3Iho96EhLAb-F8ML70dT-Oxm0Gm1IoUKvpMQNbEOOeW3t9rFnXXyniyk2gadw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=qPX9UnUAE9HUtYL_q7m-b2DsWbE2Z7GMLFf79O9Uv-DdciqS0-sh3hR7ZBmw47hgwmwDwmbwX4OiETxJ3TfWC2pi2JJHa-PbR7ESvx3N4pgsPpLKWiW7i2SpYCD_cF8b5Gka-YpKiFEXaT5DTjAoUztSry75t4Ct9qALMTbcs4tf8QLo5TV--fe4Qim9HqHyGsASfdPD85mOaPDAeWOTrI_20qSTWT5E7QYtQxSG7mqi4KFRR9tcZm6QVGfgtaQ2BkCqfab0-ZJIowWbLLe2I2slY3Iho96EhLAb-F8ML70dT-Oxm0Gm1IoUKvpMQNbEOOeW3t9rFnXXyniyk2gadw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: أرى أن ممثلي الجمهورية الإسلامية الإيرانية يطالبون بتعويضات عن الأضرار التي لحقت بهم خلال النزاع العسكري الذي استمر خمسة أشهر (والذي بدأ لأنهم يرفضون امتلاك سلاح نووي)، على الرغم من أن هذا الأمر لم يُذكر قط في أي من مفاوضاتنا أو اجتماعاتنا! لكنها…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87483" target="_blank">📅 20:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87482">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbmWn2Q2kHxMU_T88kis6rOoAv1IFjKk4upNNeThtIvp1MIX1qQZfQxSN3qnr1zViidpjrKI2mFa9IBHWobVaWVaE2ceWYy8Tt20wwCLgII00-jJbEo5H75TpSjIJfYsEpiOQHZgUX7Dgp9HjmyX_qGztUgXwxp_RqUzq9brBGmSeAHtM71XLhRfDtoEim5NBZpMQ4DYzSIZU17tINW9XKuLfDnS5ARiMD2w7uXwSbpHkNnNkOBq5P6kRDQ-gOgGjvML-kI6ta7ImOkQsjMUl75-iqvlHnjpI5rmgTzaPtQllOusC76poVtsmpWK7nusWKSE06GeM3wd8jGU6R8iwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
أرى أن ممثلي الجمهورية الإسلامية الإيرانية يطالبون بتعويضات عن الأضرار التي لحقت بهم خلال النزاع العسكري الذي استمر خمسة أشهر (والذي بدأ لأنهم يرفضون امتلاك سلاح نووي)، على الرغم من أن هذا الأمر لم يُذكر قط في أي من مفاوضاتنا أو اجتماعاتنا! لكنها فكرة مثيرة للاهتمام، لأنني أطالب الآن بدوري بتعويضات من إيران عن جميع القتلى والجرحى الذين سقطوا جراء قنابلها المزروعة على جوانب الطرق وفي العديد من الصراعات التي اشتهرت بها، والتي قادها في البداية الجنرال سليماني، بما في ذلك عائلات ضحايا المدمرة الأمريكية كول، وآلاف آخرين سقطوا في المعارك. إضافةً إلى ذلك، يجب دفع تعويضات لعائلات مئات الآلاف من المتظاهرين الأبرياء الذين قتلتهم إيران على مدى الخمسين عامًا الماضية، ناهيك عن 52 ألف قتيل سقطوا في الأشهر الخمسة الماضية. لقد وجهت ممثليّ بوضع هذا الأمر بشكل حاسم في جميع المفاوضات المستقبلية. شكرًا لاهتمامكم بهذا الموضوع! الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87482" target="_blank">📅 20:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7cf11d6c.mp4?token=OYTxg8t_0VsvsFzVTUvkzeIOxq9AvyDyMTKiEinAdo7y0fcIyhHnfszXeR_o1duXTQCVMFJaj2gEH8Yi6KX94-uYwho24D0gcoGZ45QosPWFe4Ff8MdWieZWJdCdqLTbWgqANXY54MaNvJGiyaHrCJqL7sYz4ODZTby9XNcR_66f-fu9TzZV-Tht4_0DljRsVwpS4IB0b1TFoZ9QZmgWwGcKKjRonExIuFBpiwOtoofZ1bTk75lj7bzTCEtzW9BZsGxCQgKRJnK7HZwMhTm9Xzp4EnTGOhxyuS70faaAL3Fn1D-wyvyH2SKE85WidtSpFtSAR0QND3BgjDtcnHwXzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7cf11d6c.mp4?token=OYTxg8t_0VsvsFzVTUvkzeIOxq9AvyDyMTKiEinAdo7y0fcIyhHnfszXeR_o1duXTQCVMFJaj2gEH8Yi6KX94-uYwho24D0gcoGZ45QosPWFe4Ff8MdWieZWJdCdqLTbWgqANXY54MaNvJGiyaHrCJqL7sYz4ODZTby9XNcR_66f-fu9TzZV-Tht4_0DljRsVwpS4IB0b1TFoZ9QZmgWwGcKKjRonExIuFBpiwOtoofZ1bTk75lj7bzTCEtzW9BZsGxCQgKRJnK7HZwMhTm9Xzp4EnTGOhxyuS70faaAL3Fn1D-wyvyH2SKE85WidtSpFtSAR0QND3BgjDtcnHwXzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
تحضيرات من سكان الكورد لقطع الطرق احتجاجا على الاجرائات التعسفية التي تتخذها عصابات الجولاني بحق القومية الكوردية في سوريا.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87479" target="_blank">📅 19:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqJ2sNjPZuTNMpntHEmHTGE92oZW9psBM53I9RcV5vBtijw1wyIOWEXR9_rXGy9iDe38XifL5l7gm2kqk1UGCMOJxU4kHlN4Cp5hx14pUtlVxX2mUjXSnpcj3WBa18VVmCFMvchyvrUKHvCtkgR_dFK4NxNGOxFzQRy9gfRIPdGa0SngAkRNQsRM5LGLYRJqyxlu09UxXAmacD7ZGkjYs-K6_x-ElMVHUQkZjjMHtczYOqYI-GYjtWsQEGBBqcchh_41xK-EztwNPqAVO_knFreRE_tZy3XEeE1-mqEFFNFFwb6yerx8kew_0Er9DZ6Lv_FXWi5qmyQr_boR4iHuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
السيد القائد في إيران السيد مجتبي الخامنئي يصدر حكماً بتعيين اللواء علي عبداللهي رئيساً لهيئة الأركان للقوات المسلحة وتعيين اللواء أحمد وحيدي قائداً للحرس الثوري واللواء مصطفى إيزادي نائباً له وتعيين العميد علي عظمائي قائداً لبحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87478" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDbCxh6RDjfRCqk-tCwUyeN7MZVcFb-aP1gRLU3osdX6MkS5gLN4K1xPhQhOJkROtV0PK43gJzgzkT4c410MYOTxdzWTwe96kgO5D4TYN0wEuFqL_YA44GQn8kAghPZvFEfxyLQZZAPqIocRG5jiAS_W9QfqYGtCXSYkGcvyx1SlgCVuYvfG7acteLIUsOGbPMdF9nnAHxjr1jAuCUdi0bTPADr3baa8YNODfKHzOE4pCAEI68XHr8R0-Ix-L-gIR02YTHsQCrhUQb2CpbDKt_kiylmoYOvyrkmXVouC0iHbXYoqRchc4WQQR_g7aPmd3eqe68b_wwTSH8DkJY8o9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مكتب قائد الثورة: أوامر بتعيين عدد من كبار القادة العسكريين في الجمهورية الإسلامية الإيرانية سيتم نشرها خلال ساعة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87477" target="_blank">📅 19:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc415cb3.mp4?token=EEvMOMfLXbfTyidqF7yTnrFtng0C-sdDEt2b9jRv9cYzrCzpZ5vRgM2uX4eiWNvppd8W-qbOHG_wmFhTnKVRADgHRCAOq9dcyZwGbqGuJpHHfPZY2g7y0H7793KZ8wyYSnIqKXVvi-IwbK8tzS7BpLvr6TK5mZ9lZvyWh-DImuQqi2_mxA5sh2E6DEd6TTG00kv9dmnV893kYuyCNNmzRXNn1YGPNxu6cr6IgIfKuAw4HibGb24TScBt7v9lgnhxNYtvSBZG6I4NB6I1_0DvLUABbxLocOGblXLqPnVHIsJiE3jCDAPWpdrK_p_Q4hRf_WpIjyX17CK4aQMHVS0yjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc415cb3.mp4?token=EEvMOMfLXbfTyidqF7yTnrFtng0C-sdDEt2b9jRv9cYzrCzpZ5vRgM2uX4eiWNvppd8W-qbOHG_wmFhTnKVRADgHRCAOq9dcyZwGbqGuJpHHfPZY2g7y0H7793KZ8wyYSnIqKXVvi-IwbK8tzS7BpLvr6TK5mZ9lZvyWh-DImuQqi2_mxA5sh2E6DEd6TTG00kv9dmnV893kYuyCNNmzRXNn1YGPNxu6cr6IgIfKuAw4HibGb24TScBt7v9lgnhxNYtvSBZG6I4NB6I1_0DvLUABbxLocOGblXLqPnVHIsJiE3jCDAPWpdrK_p_Q4hRf_WpIjyX17CK4aQMHVS0yjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني و جماعات الكوردية في القامشلي بسوريا.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87476" target="_blank">📅 18:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني و جماعات الكوردية في القامشلي بسوريا.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87475" target="_blank">📅 18:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87474">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
مكتب قائد الثورة:
أوامر بتعيين عدد من كبار القادة العسكريين في الجمهورية الإسلامية الإيرانية سيتم نشرها خلال ساعة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87474" target="_blank">📅 18:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87473">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
🇮🇱
اعلام العدو:
أميركا تواصل تقليص عدد طائرات التزوّد بالوقود في مطار بن غوريون، عدد طائرات التزوّد بالوقود الأميركية في مطار بن غوريون تقترب من مستويات وقف إطلاق النار.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87473" target="_blank">📅 18:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87472">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87472" target="_blank">📅 18:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87471">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87471" target="_blank">📅 18:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87470">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
🔻
هيئة الحشد الشعبي:  توضح هيئة الحشد الشعبي أن المقرات الوهمية التي أعلنت عنها وزارة الداخلية، والتي ادّعى القائمون عليها انتسابها إلى هيئة الحشد الشعبي، لا تمت إلى الهيئة بأي صلة.  وتؤكد الهيئة أن إجراءات إغلاق هذه المقرات ومتابعتها نُفذت ضمن عملية نفذتها…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87470" target="_blank">📅 18:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87469">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇷🇺
🇸🇪
جهاز المخابرات السويدي يزعم إحباط عملية استخباراتية روسية في السويد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87469" target="_blank">📅 17:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87468">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
🇾🇪
انصار الله يشنون هجوم مسير على مرتزقة السعودية في المخا.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87468" target="_blank">📅 17:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87467">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس البرلمان الايراني محمد باقر قاليباف يزور العاصمة بغداد الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87467" target="_blank">📅 17:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87466">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZACHpJfW9_ZaIKOYToc0CTSmYDjV_qal4Nyy7qOkzRMSB4uPs7bdLbYFee4DXGasxLxwmZKVK4uV9McoYemNKjcA4cPaI86lSHYCayn82jXPLvb-Rh-JqAo5nSxjxhulqRiTrnRjEn1IrQd-a4nin1fLelSK0W8rc0GvaY1tP4pZKWlNR0cYWQ4I9Nd0HgLv9EGSiN5OpYDe11cOd4841lCaUr7M6QBANND3o_W4N9L-yLE3VCO4pxpdq4qe2P0EBYzyna3BnCh8ETaW2QCLWQOIemXsFt1bCKQnQFIgjyx36ziqxH7Jt0OqaXP1N3XuDQfKlOGWAfnk-N2LyDdPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اندلاع حريق قرب مرقد سيد محمد (عليه السلام) في قضاء بلد شمالي العراق</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87466" target="_blank">📅 17:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87464">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d385f60930.mp4?token=aUyZYvrZsf5ifqMKBNY97WRWdrOL9-MB_0fufwFOx0uyzc2XPH6s_E4I5BrhaSYSxr9Yq3sZEFM8bSganD4XB41uAT8Izz4_vD75wXkwXXaBxPYGwH97eRwCxZq16TpNEJvq-8ndVy3vSZymlDQOtrEPtwLZS8-TOu2d-86yOO0tIBVNHfVhBUdn34qC4UpKXBdmlcKku_-886OrHBLyfEmOS2jvAtIFTBZBcfWP94HZCYzXtb8Zn2CT4oIRn7R9KcVKquvKEiAnjJcRRsyP1PkH5bbwsAXtD-O8chAo5ziagmfPgMYLRYBaQkD2qq5G8zmZLhx3j6MYvLS1ReInMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d385f60930.mp4?token=aUyZYvrZsf5ifqMKBNY97WRWdrOL9-MB_0fufwFOx0uyzc2XPH6s_E4I5BrhaSYSxr9Yq3sZEFM8bSganD4XB41uAT8Izz4_vD75wXkwXXaBxPYGwH97eRwCxZq16TpNEJvq-8ndVy3vSZymlDQOtrEPtwLZS8-TOu2d-86yOO0tIBVNHfVhBUdn34qC4UpKXBdmlcKku_-886OrHBLyfEmOS2jvAtIFTBZBcfWP94HZCYzXtb8Zn2CT4oIRn7R9KcVKquvKEiAnjJcRRsyP1PkH5bbwsAXtD-O8chAo5ziagmfPgMYLRYBaQkD2qq5G8zmZLhx3j6MYvLS1ReInMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلزال بقوة 7.1 درجة يضرب كولومبيا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87464" target="_blank">📅 16:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87463">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">زلزال بقوة 7.1 درجة يضرب كولومبيا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87463" target="_blank">📅 16:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87462">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca01a4bc22.mp4?token=v2PZrYexP0NJotF5BCMeEQ3WHdT4cO2x5CEY83cJByErKb1wFutaY86cW--1BQjzR3iU8Z8hzhE0u09hlr3CaKSSSb3A3jtxHBLi8ls_M1tP6cmRmVTjoAwMQvzr5DkYmpoO1NBw6mDMDnYL8Gkk5XQEL3jyq6mcm2a0UsAMNLnm3qeScbYVxTpFfO0I0QR-8Fm5ZmAydnJbc6r9fDFh0TxWRoOa09Np84mecjL_7GwVDyjHJY6xpYvYWzLif4M59Mpb__enK4VCLeBZUD_m18IEEF21spFb1sLLDqOhWSfiLIuhapDbjN8NKV_UauWDJmiHNAAXcM-d67DwZaI02A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca01a4bc22.mp4?token=v2PZrYexP0NJotF5BCMeEQ3WHdT4cO2x5CEY83cJByErKb1wFutaY86cW--1BQjzR3iU8Z8hzhE0u09hlr3CaKSSSb3A3jtxHBLi8ls_M1tP6cmRmVTjoAwMQvzr5DkYmpoO1NBw6mDMDnYL8Gkk5XQEL3jyq6mcm2a0UsAMNLnm3qeScbYVxTpFfO0I0QR-8Fm5ZmAydnJbc6r9fDFh0TxWRoOa09Np84mecjL_7GwVDyjHJY6xpYvYWzLif4M59Mpb__enK4VCLeBZUD_m18IEEF21spFb1sLLDqOhWSfiLIuhapDbjN8NKV_UauWDJmiHNAAXcM-d67DwZaI02A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات الامنية تعتدي بالضرب على المتظاهرين المحتجين على تردي واقع الكهرباء في محافظة ذي قار جنوبي العراق</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87462" target="_blank">📅 16:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87461">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يلتقي قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87461" target="_blank">📅 15:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87460">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
المتحدث باسم حرس الثورة الإسلامية:
صواريخنا لديها القدرة على التوجيه، وحتى بعض الصواريخ يمكنها تغيير مسارها في مواجهة منظومات الدفاع الجوي للعدو. حتى إذا تم تحديد هدف لصاروخ ما، يمكننا تغيير ذلك الهدف في منتصف المسار وتحديد هدف ثانوي له.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87460" target="_blank">📅 15:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87458">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdivRDiHp4rAPLkkobrjGLfljsTWwRV0XTNG7aUNfKO9VByUVPg3np57GLE_DOAp92YnMOJvHyuKBTfqVQjMfJSys2JmNsKYKiiV1gLQKcdkiSIMLfjZTbO97KBY6NF3RAIYIO2In44OfLXsb2fbQIS6ntz48rJPbUGphjr6txHTuQSOhW_OMgIiFEgnxUCdiWFV618sUxfVBr5-k5d-f4kxnHP1uIZfJynruocirMTsQGyQ3Dk7Z-6rrIbzGPIkSWRnrEq11Q1nHqYcNSIW3wShKLkUilGEfIXgMQ_v13sSUXIzrJGx8CjQT-zf7NUMHclN4UFjDlj4Y5QkfYcltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انه زمن الديكة الشرسة اذ ولى زمن الدجاج الابيض … بحر الما يغرك ينعبر كل يوم
؛ والديج ضربته توجع</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87458" target="_blank">📅 15:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87457">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
مواطن من بغداد يتعرض لصدمة بسبب الارتفاع الكبير في أسعار الوقود في إقليم كردستان شمالي العراق وسط اتهامات لعصابات مرتبطة بعائلة البرزاني بتهريب كميات النفط ومشتقاته المخصصة للإقليم إلى تركيا ما أدى إلى شح الوقود وارتفاع أسعاره بشكل كبير على المواطنين.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87457" target="_blank">📅 14:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87456">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd242d2b06.mp4?token=VK5qMjOU83AqDKa2f9zAqdteVx7qzm4gm8nIPSC3vTRBfUFdQw8632gIMDpvmpHtwB8_Y1NlNQW47F0Dii47OQ71OK42w37gj6gF_S8iKnEX1L11TlzYPRLMs61amiVdiPxOdr9KreOSbiyCMJIdnLS_yUip0yiK-nDI2kozk33Zd3AjOa75vjPnhLDcsS3G44VaJQFb5dsHuN-JRYzBRE2g5oNQYrA333cUT5gz2v9ft3K7M5uQqLcKhJzfVpGiPZT679Q6dVPGPv1GAjmYo37shWEIZug_SYJBZjM09yXIBf7FPQSDKMG9FnHnei99JHUwqRbxX3HGozuIqQGVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd242d2b06.mp4?token=VK5qMjOU83AqDKa2f9zAqdteVx7qzm4gm8nIPSC3vTRBfUFdQw8632gIMDpvmpHtwB8_Y1NlNQW47F0Dii47OQ71OK42w37gj6gF_S8iKnEX1L11TlzYPRLMs61amiVdiPxOdr9KreOSbiyCMJIdnLS_yUip0yiK-nDI2kozk33Zd3AjOa75vjPnhLDcsS3G44VaJQFb5dsHuN-JRYzBRE2g5oNQYrA333cUT5gz2v9ft3K7M5uQqLcKhJzfVpGiPZT679Q6dVPGPv1GAjmYo37shWEIZug_SYJBZjM09yXIBf7FPQSDKMG9FnHnei99JHUwqRbxX3HGozuIqQGVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعض الديون لا تنسى .. الحرب السعودية المفروضة على العراق</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87456" target="_blank">📅 14:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87455">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صفارات الإنذار تدوي في العاصمة الأوكرانية كييف وتحذير من هجمات باليستية</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87455" target="_blank">📅 14:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87454">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
الحكومة العراقية:
هناك تنسيق أمني وعسكري منتظم لتسلم المواقع التي تشغلها قوات التحالف الدولي في حلول 30 أيلول المقبل.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87454" target="_blank">📅 14:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87453">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKT9H6P_LTyl3tbfCy-SZnChz63ZWuzt--Ugu-UPqFEDwxNRmB3kbzLlpBN--mkvbTYsYqSPT-qWYjfGg3fYjwGG8zA-ovgx1QbYXg5pxEY7pSVByI3Tn1B-9dWLky-htRptzr-2Fc_au_pWNSGsKGcbOcYbzB9lqHOq1iCxDJwboTxYoPh8TkJipNypu-6zmf2zt1RzyATdK0LkSkqHDwHu2D2rmEuXTovQdp1S7DKGwU1XmGOKR9VOFhNiindW8gjZc3dnIPjWw_JX6hO-ZD-OsqiNcHHQy9BHmHnQNed3ozMkRLCkdm4WPSiGM21zM2AE4lCb02sWiQ4Xy5RWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
"نريد ماي يا انصار الحسين"
مناشدة عبر بوت نايا:
نداء لاهل الغانمة (الحشد الشعبي) نحن مواطنين يسكنون محافظة ميسان الجمعيات منطقة حجي حسن الثانية المكان المؤشر باللون الاحمر مقطوع عنه الماء صار اليوم سادس ناشدنه المحافظة ناشدنه المستثمر لكن ماكو اي حلول ما بقى الها غير الحشد ولد المهندس الشهيد ونگلكم (نريد ماي)  يا انصار الحسين عليه السلام</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87453" target="_blank">📅 13:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87452">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇶
🔻
هيئة الحشد الشعبي
:
توضح هيئة الحشد الشعبي أن المقرات الوهمية التي أعلنت عنها وزارة الداخلية، والتي ادّعى القائمون عليها انتسابها إلى هيئة الحشد الشعبي، لا تمت إلى الهيئة بأي صلة.
وتؤكد الهيئة أن إجراءات إغلاق هذه المقرات ومتابعتها نُفذت ضمن عملية نفذتها المديرية العامة للأمن والانضباط في هيئة الحشد الشعبي، في إطار أعمال اللجنة الدائمة لحصر السلاح، المُشكَّلة من قبل القائد العام للقوات المسلحة.
كما تجدد الهيئة تأكيدها استمرارها في متابعة ومعالجة مثل هذه الحالات، واتخاذ الإجراءات القانونية والإدارية اللازمة بحق كل من يحاول انتحال صفة الهيئة أو استغلال اسمها بأي شكل من الأشكال.
هيئة الحشد الشعبي
10 آب 2026</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87452" target="_blank">📅 13:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87451">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
الحكومة العراقية:
لم نكن نعلم بالعدوان ورئيس الوزراء العراقي كلف وزارة الخارجية لرفع مذكرة الى مجلس الأمن حول القصف على مقرات الحشد الشعبي.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87451" target="_blank">📅 13:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87450">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇶
العراق يقوم بتخفيضات جديدة لنفطه المصدر الى دول قارة اسيا.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87450" target="_blank">📅 13:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87449">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
العراق يقوم بتخفيضات جديدة لنفطه المصدر الى دول قارة اسيا.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87449" target="_blank">📅 13:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اعلام سعودي: مسيرات انصار الله تستهدف مواقع المرتزقة في منطقة بيحان بشبوة</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87448" target="_blank">📅 13:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اعلام سعودي: مسيرات انصار الله تستهدف مواقع المرتزقة في منطقة بيحان بشبوة</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87447" target="_blank">📅 12:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55da867fa.mp4?token=FNANp6MVzq9nBfRC0M_dt64BhUMLfuKo74GdpCcIjq01aC29a8zrkUKbufG-Tln-owX_SiNf23S1Uktp1-k8oyNmYVkX3ja_5uoNnoqPrilhKEvYSVLHALvFq1I4noe8HVZPyJrROcHL6w-gUDZRytF2reiDye2Uka0EV5TEVmuODS84nhvLbVqbg8MvIcddkDCqU9UMe5XvD5raTrsHQ3skCBeAbrvxXgUfdkM921el7d5T6aFnY9QQEXKoJZFrXXvtbdklNNbkqvbprppPwdbEnPvr2lt1jOFph3nuYhk2clXXZXD0FJV5wt1dPWZclM6PF3yNPFSUD9QzMtctbFmDIv-7ODW8P2FZVyONbNuzu6JpYiY4AUaxh0qRKsQ0rO10KTx11kAEU-c2Fj6YiEETzotWXTBQMk9n7in-LprOajBOiDFBWCW6ysbrhzA-fUcugtjyA9Iww6q88vT-gdWahffltgLeWOUzSPMYkCc5E1hQa88b70vMbJO8qALfhO8TFU8cRKTE1z3s9WAVdcY0mmp0bvao0QFvbO-eWS37OhgxsICPYhiTIECUEdJjMzI169tCgR1UxluDeAqC4qyjERhOAvzdG4WFBKpYLq8i_ZFgg1LXFJPVWUIsl2wNl4e6Aqvw0v4u_Yl4g6J8wiFMhJ2ZdC2yAZTDl1S8IoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55da867fa.mp4?token=FNANp6MVzq9nBfRC0M_dt64BhUMLfuKo74GdpCcIjq01aC29a8zrkUKbufG-Tln-owX_SiNf23S1Uktp1-k8oyNmYVkX3ja_5uoNnoqPrilhKEvYSVLHALvFq1I4noe8HVZPyJrROcHL6w-gUDZRytF2reiDye2Uka0EV5TEVmuODS84nhvLbVqbg8MvIcddkDCqU9UMe5XvD5raTrsHQ3skCBeAbrvxXgUfdkM921el7d5T6aFnY9QQEXKoJZFrXXvtbdklNNbkqvbprppPwdbEnPvr2lt1jOFph3nuYhk2clXXZXD0FJV5wt1dPWZclM6PF3yNPFSUD9QzMtctbFmDIv-7ODW8P2FZVyONbNuzu6JpYiY4AUaxh0qRKsQ0rO10KTx11kAEU-c2Fj6YiEETzotWXTBQMk9n7in-LprOajBOiDFBWCW6ysbrhzA-fUcugtjyA9Iww6q88vT-gdWahffltgLeWOUzSPMYkCc5E1hQa88b70vMbJO8qALfhO8TFU8cRKTE1z3s9WAVdcY0mmp0bvao0QFvbO-eWS37OhgxsICPYhiTIECUEdJjMzI169tCgR1UxluDeAqC4qyjERhOAvzdG4WFBKpYLq8i_ZFgg1LXFJPVWUIsl2wNl4e6Aqvw0v4u_Yl4g6J8wiFMhJ2ZdC2yAZTDl1S8IoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الايرانية: لم يتم حتى الآن اتخاذ قرار بشأن مشاركة الرئيس في اجتماع الأمم المتحدة في نيويورك.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/87446" target="_blank">📅 12:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87445">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هجمات سيبرانية تستهدف الامارات</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87445" target="_blank">📅 12:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هجمات سيبرانية تستهدف الامارات</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87444" target="_blank">📅 12:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87443">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الايرانية:
لم يتم حتى الآن اتخاذ قرار بشأن مشاركة الرئيس في اجتماع الأمم المتحدة في نيويورك.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/87443" target="_blank">📅 12:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87442">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
الجيش العراقي ينفذ قصف جوي لمواقع تواجد عصابات داعـSh بواسطة طائرات (سزنا كرفان). قد أسفرت الواجبات عن تدمير ( 8)  مضافات بالكامل ضمن قاطع مسؤولية الفرقة 11 في قيادة عمليات كركوك شمال العراق</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/87442" target="_blank">📅 12:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇾🇪
🔻
هجوم بالمسيرات وانفجارات قرب قصر المعاشيق بعدن جنوبي اليمن.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/87440" target="_blank">📅 08:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇱
🇺🇸
إعلام العدو عن مصادر سياسية: خلافات بين الولايات المتحدة وإسرائيل على خلفية وثيقة الـ15 نقطة بشأن غزة</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/87439" target="_blank">📅 08:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87437">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇾🇪
🇸🇦
مرتزقة السعودية تعلن عن مقتل 7 وإصابة 30 مرتزق، جراء هجوم يمني بالصواريخ والطائرات المسيرة الإنتحارية طال مواقع عسكرية في مدينة المخا اليمنية.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/naya_foriraq/87437" target="_blank">📅 04:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
🇸🇦
إنفجارات عنيفة تهز معسكرات مرتزقة السعودية في مدينة مأرب اليمنية.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/naya_foriraq/87436" target="_blank">📅 03:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBud5MQgyY2XtBP4qYA6cflDydWFVycAXhU8fMjL2-Stp-VW6zCD79-ZznA67qF7G71xBmUSbK9iW17g7MNPljqOedFSRfyvizCNB7oQcQB0gvwqjoVF207jsPY9gFg5M7ocFHXpq556itkSFaNW1ad3sFUVepPuCFew-TMg_vpjLya0iX7XuMsQmmEsfGumZwAKunR897qv6ZN3C_cXLoq2ycXrfFO4_wM7c-n-LLUUfTOF8jCMo7ZNlJWeRdZGL29O1KlpjG31K73Y53jQ-pgN5TEcVlRU_FeXbZnnPDaf5qmvt812xbv-9uhkE-AEqGhTeqEoQeiEIVG_FHahmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
نتيجة الهجمات التي تشنها القوات اليمنية..
السعودية تستمر في إغلاق مطارات جيزان ونجران وأبها حتى إشعار أخر.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/naya_foriraq/87435" target="_blank">📅 02:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87434">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzUKQzEpyWw51QVUcRFuirK3BptQRKSGq6e8yHaGMw0PM5MRiy5Dfrl32t-YhHJFHd4PBorQ0SoNHjjAmc4QJhzdVDJS4_AzciRtIHuMatbXjW20_QsUEiHzTE2Jzpdiz_8QhLTQIDOoYo-6ICbmwjfqzONagL_5dnodm10b-KKHeKumy_E2PFEzmzeEAwK_DWnS6Ph04IjOmIAYBWrtGiK2kH5ZeOtAUQpUtzWtuwXZePPzS8YArRs1qkAzOKYs3_v_sqkC8ZSJt1mkZ9uQf9LS9c32eDQyvRHSmGiHtskdpGn69WQXWIHNbRrkvgclxLdVJjAKyYioaLnq9z-XDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد اخرى من السفينة المشتعلة قبالة سواحل عمان بعد دكها بالصواريخ من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/naya_foriraq/87434" target="_blank">📅 01:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v07Ev9WOSzP2aLJquBC4OnfJ7RGZ9HRzVtaRNK7x6-pGb1PjALIsisecwydJsdAKwBkZCcICJCVchwmDRrHc6D_w7PWMchuJZfWUU5fbhhWd_ss6ll0hxLr2VzypoiNtx96eQvNdQ9YxMjKd3o7n1HXZouy6Dt-tbZY1nPbks5_AQ2hYQHqByiQ4FcImUHZOqMUBpo1KqREFcKKWdDcw9Y5w5Rfwu7q92baFu_TfiJ8mHZ4hAkltiSq0mCEhfJ17SvSw2ctYekqqCS7sBAP9NSC4mO46PM26NeYwCnxk19A6jcBNdI1Pss4DPhrSU6dB5ClLhTjCWlmPvLly9DmTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
تعرف على محسن رضائي ؟!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/naya_foriraq/87433" target="_blank">📅 01:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87432">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الحادثة بالمختصر ، ووقعت قبل أقل من ثلاثة أسابيع في محافظة واسط، حيث تم ضبط سيارتين محمّلتين بطائرات مسيّرة.   وهذا يعني ان الرواية التي أنتجتها قناة العربية السعودية هي رواية كاذبة بالمطلق واستخدمت صور قديمة من واسط وركبتها على بابل لأسباب سياسية كون بابل…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/87432" target="_blank">📅 01:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87431">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مسيرة معادية ثانية تم استهدافها وإسقاطها من قبل الدفاعات الجوية الإيرانية في أجواء جنوب البلاد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/87431" target="_blank">📅 01:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87430">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/87430" target="_blank">📅 01:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87429">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/87429" target="_blank">📅 01:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87428">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0db1cb8610.mp4?token=HEpN__ca_VhnckPkKgpdM5dfdNxYKObZS5iovBi_HTt988rrJ9eEocxYTVw6_Ds9WBb_SuB5ZUJxXhSg9xMJMUAfbbkQzLdDNubxzK8Dl2PM3gbztYz1MlJYjpoPHy0wHrblTD_Z_1880O_L0bD8aQVdf43_xA-GCTXs2hhkml2_0v-zo7OgCa808aLS3ueQiDV9P6KsvNSfHaO8QbmRhpW5tTpfy2ODxRsaShTWO2Dd8tKyyfUs0AGV6w9zhbCMhQ_oGD7jmwRrsAFQx7j6yEZzSi_rvJ57rzDblRPRgvvzPF4CQjH36WS5KNlWWZdHGIVSJpm1K_f1TCFoUwTshw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0db1cb8610.mp4?token=HEpN__ca_VhnckPkKgpdM5dfdNxYKObZS5iovBi_HTt988rrJ9eEocxYTVw6_Ds9WBb_SuB5ZUJxXhSg9xMJMUAfbbkQzLdDNubxzK8Dl2PM3gbztYz1MlJYjpoPHy0wHrblTD_Z_1880O_L0bD8aQVdf43_xA-GCTXs2hhkml2_0v-zo7OgCa808aLS3ueQiDV9P6KsvNSfHaO8QbmRhpW5tTpfy2ODxRsaShTWO2Dd8tKyyfUs0AGV6w9zhbCMhQ_oGD7jmwRrsAFQx7j6yEZzSi_rvJ57rzDblRPRgvvzPF4CQjH36WS5KNlWWZdHGIVSJpm1K_f1TCFoUwTshw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف سفينة واشتعال النيران فيها قبالة سواحل عمان بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/87428" target="_blank">📅 01:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87427">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bprTziD0u6aKrR32f7G6GxejUFElcmJLE9QQZIC-ByncBHFGhVKECOy-m9X71a7jrGGCbvRBoferYt9-OY43hOBRZOj4yDD5A-ZEwdk8qyhVQPn6YCO819FVhf6KS1KEiNKx5hAPsxAPS8VtP09TAzxccczC6uCZCS18xnrGEdvuEA_WYu9Kr-G_4ysKewywLjCbm4krtcVI1TZeoaB7D1NIXkTRirANH-g2u4TuORi9GbwTW8wc7Ab-ji07la3JoVq8gtlBp1UbtuOnQIsrP40di_YZ0oIe_6YyofY7YcMe954DXXJdRM-TGEENPeofEZvS3OK05I7RWNTY-qapYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يستغني عن فريقه تدريجيا
تعيين ويل شارف مساعداً جديداً للرئيس ومستشاراً للبيت الأبيض، ليحل محل ديفيد وارينغتون الذي سينتقل إلى القطاع الخاص.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87427" target="_blank">📅 01:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87426">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مصدر امني لنايا
عملية نوعية في منطقة الكرادة خارج بالعاصمة بغداد ؛ العثور على مبلغ مالي كبير يخص وزير العمل والشؤون الاجتماعية السابق .</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87426" target="_blank">📅 00:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87425">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">أنباء عن أن المسيرة التي تم اسقاطها في أجواء جنوبي إيران تابعة للسعودية.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87425" target="_blank">📅 00:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87423">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edJoZw-9No22JHmTmjvmBCxoApfmF1KNACngB6sGAi2P7uVO3aGiWQ1t2hEJBzDeTwYGnNpkwe2yE8YU9E3OBnz4QZWC0ZBJFo-YUntjlVRw-55ZuycSW7JLsn7BU2sknzgUSzdQcmijBP9H55E07Iqibsv-EDQB5V6hTKz2coUqHd-HQU5LPOK9zUw9Rvot_NwKogCpLLwLsTSYvSxY_MGKqFi1LK9-VeTF7ZnKEUdeGcN6OyGGxlnlRNYnDCO1nG_U44bTSXjOtpPgmumhQraceyBkbjudINL5SZFRiC4roLr29Zf6ecP1zMVMYI1goJC66g1VgosVp3vaVhBVsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=v9Vz55nMxiCY0dRGcoJUptDMg2vFuar6mO3pV3M4b9hMY8LpAlpPROE_iI-sumu4VePhrPXzhVRhtQzcqvjJdoewcsYkxf0NgJ3onNlPDWRF42-14QDeG0hwq2fk9PuQFwaJ8CXMGZIRsoDJ3A7jcz2K02bT5omCUnR1ewAmLNorbG3f5ksxn7AIiciUW6jnI7rUN-jelVb0qXj2Aw9CfePzd0gvGiXF_iGHiWZVGuePdVsYnYZCiTwI3kG_NjI1gqOaGSJ8esmMczhMOpuh-IvEvHQTACAmjWqa2ZmyqA9D7dvu5paSrNGmdR_6SQBcdaZmXd37MiwvLHKyR55_pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=v9Vz55nMxiCY0dRGcoJUptDMg2vFuar6mO3pV3M4b9hMY8LpAlpPROE_iI-sumu4VePhrPXzhVRhtQzcqvjJdoewcsYkxf0NgJ3onNlPDWRF42-14QDeG0hwq2fk9PuQFwaJ8CXMGZIRsoDJ3A7jcz2K02bT5omCUnR1ewAmLNorbG3f5ksxn7AIiciUW6jnI7rUN-jelVb0qXj2Aw9CfePzd0gvGiXF_iGHiWZVGuePdVsYnYZCiTwI3kG_NjI1gqOaGSJ8esmMczhMOpuh-IvEvHQTACAmjWqa2ZmyqA9D7dvu5paSrNGmdR_6SQBcdaZmXd37MiwvLHKyR55_pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف واسقاط مسيرة أمريكية في جنوب إيران</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87423" target="_blank">📅 00:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87422">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87422" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87421">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=b3WdT55fggKuFPUHP3bJ3StUVJ9bXlB8Vvyzd4VxWdN9MIXtj8lEMHONI_kz0wXNZMC5V4_5yvrvJAi2_J4lPWeFW9YYNU8FDyyEI6ys-FYNmfj8pxEDX0ksbYtkkqm0UTxLanr-p49O3YfbzplYnwxhIeS0UPqVbXRf1psoc8bh8J2Ej38Kgbu60BbhL0uEeDTvaPXQ7krrT1LtQuUxnoJClhmhnF9xxeVPwUyBwY6_OfZgVf1MUOVw1Zi9zESW6Zue509-t2EB7NBEnVndm8VzgcwlKsotogMUbi0RW_FkswfXsi62oPl6uM-0TTfKVL47RoiBeGYJMCJp1Mw6Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=b3WdT55fggKuFPUHP3bJ3StUVJ9bXlB8Vvyzd4VxWdN9MIXtj8lEMHONI_kz0wXNZMC5V4_5yvrvJAi2_J4lPWeFW9YYNU8FDyyEI6ys-FYNmfj8pxEDX0ksbYtkkqm0UTxLanr-p49O3YfbzplYnwxhIeS0UPqVbXRf1psoc8bh8J2Ej38Kgbu60BbhL0uEeDTvaPXQ7krrT1LtQuUxnoJClhmhnF9xxeVPwUyBwY6_OfZgVf1MUOVw1Zi9zESW6Zue509-t2EB7NBEnVndm8VzgcwlKsotogMUbi0RW_FkswfXsi62oPl6uM-0TTfKVL47RoiBeGYJMCJp1Mw6Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة تطال سفينة مخالفة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/87421" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87420" target="_blank">📅 00:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87419">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجارات بالقرب من مضيق هرمز</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87419" target="_blank">📅 00:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87418">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات بالقرب من مضيق هرمز</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87418" target="_blank">📅 00:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87417">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مصدر امني لنايا
اعادة انتشار وتموضع قطعات جهاز مكافحة الارهاب والشرطة الاتحادية في مداخل المنطقه الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87417" target="_blank">📅 00:27 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
