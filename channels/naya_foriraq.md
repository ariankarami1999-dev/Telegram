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
<img src="https://cdn4.telesco.pe/file/Y98uSoqxP30A0ywLcP68XBnujkBaBka1teym36NVnok3WMCZclmGRW5UnjMwXHSx1lwGnhzdmCCvAVdYUEsl3zK19o0I4FJfeUkklgnfDlvENgoGP6x2L3CpSUFgO5z0PXKvAWIyDQlnFoCO_oNOtR9kIuXqiOs9r-a_ceetlhwTicwzb2dEcMdNsAhNlbHPPNu2n-Ggza2JoNVNWl6FUJknUfsYqxh0GqWyh4PnmbRS7QHLa93rLG8YFPr_5CTrbT5u11NgbLiOMiogPzfAlo872nSEprahgWIGI7bphiP4V_CjkLfq0U9E_PYTIAu5-TpP_1aAuSBM7EVup4ZqHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 01:51:16</div>
<hr>

<div class="tg-post" id="msg-89344">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
الاطلاقات نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/naya_foriraq/89344" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89343">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
اصوات طائرات مسيرة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/naya_foriraq/89343" target="_blank">📅 01:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144436e58e.mp4?token=DjmdHODhEodM0Pjr6Ik6PcdY_s8UkwfGPzZqi7DvW5jJYBHv-5ZVmk8qaSQ5tJLpVCD9UGGRUDa9m9Fjm35doV-KmzjzYyekRG58XLoboxZ4tMAC72O3Stu1Ibz3Y6JXl6wZj-b3D62Og3fo97aS0DFvS_ocTurcO87GLVgpdI7-7o9W9x9_4mIwFDbNYhFK1NYL5hfLf9D3TAkIk57U-RT2krF45kKt8-mKjBxoCoho1nMUFULsfuU4szHWN3l3rtC5-Jt5shTrkc9H6K8nwX6q4OiS5Wed8SgTsD62RjKF7fSuVvOlUJN4RmXklKV9OkPyI07cg2znyVXWJFZxtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144436e58e.mp4?token=DjmdHODhEodM0Pjr6Ik6PcdY_s8UkwfGPzZqi7DvW5jJYBHv-5ZVmk8qaSQ5tJLpVCD9UGGRUDa9m9Fjm35doV-KmzjzYyekRG58XLoboxZ4tMAC72O3Stu1Ibz3Y6JXl6wZj-b3D62Og3fo97aS0DFvS_ocTurcO87GLVgpdI7-7o9W9x9_4mIwFDbNYhFK1NYL5hfLf9D3TAkIk57U-RT2krF45kKt8-mKjBxoCoho1nMUFULsfuU4szHWN3l3rtC5-Jt5shTrkc9H6K8nwX6q4OiS5Wed8SgTsD62RjKF7fSuVvOlUJN4RmXklKV9OkPyI07cg2znyVXWJFZxtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
اشتباكات عنيفة بين القوات اليمنية والمليشيات الموالية للسعودية في اليمن عندة جبهات محافظة الحديدة.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/naya_foriraq/89342" target="_blank">📅 01:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ ايرانية.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/89341" target="_blank">📅 00:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ ايرانية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/89340" target="_blank">📅 00:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/89339" target="_blank">📅 00:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c097e8b2.mp4?token=p1KuHQg0ec17ct2IXRmz9rdveDvnCfMeg3VNsn51NChyLMR8qKfoP2jM_BSkmWNdUenSu7CP7uKDHWvWdFDqu4rbsR8H8VCexskxZ-pn0mLdq6uuMSeHG_9e79rp_qWIXoQArPRbQLJSdVT2ezJRz5Jj5uU0nGiFFgy11QVHkqcWXiW07Tvn1G338icp250KEsOnHYEUY0VfQhZ5jDr3g5QgqRHgvj7a4ac_4wOlMxwYG35cFEn73PqwBD_5VjVOMXFa689L5T-GC1EFmeF26HL_50wzXPJT86xKBNYv019I_C-oF_ybdnH_xOGiidk97obh4THcmzhwqRGuaQ0iLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c097e8b2.mp4?token=p1KuHQg0ec17ct2IXRmz9rdveDvnCfMeg3VNsn51NChyLMR8qKfoP2jM_BSkmWNdUenSu7CP7uKDHWvWdFDqu4rbsR8H8VCexskxZ-pn0mLdq6uuMSeHG_9e79rp_qWIXoQArPRbQLJSdVT2ezJRz5Jj5uU0nGiFFgy11QVHkqcWXiW07Tvn1G338icp250KEsOnHYEUY0VfQhZ5jDr3g5QgqRHgvj7a4ac_4wOlMxwYG35cFEn73PqwBD_5VjVOMXFa689L5T-GC1EFmeF26HL_50wzXPJT86xKBNYv019I_C-oF_ybdnH_xOGiidk97obh4THcmzhwqRGuaQ0iLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
اشتباكات مسلحة مع عنصر من تنظيم داعش الارهابي في مدينة اسطنبول التركية واصابة شخص واحد كحصيلة اولية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/89338" target="_blank">📅 00:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
الخارجية الايراني:
‏
أكدت الحكومة القطرية، في وثيقة رسمية قدمت إلى الاتحاد الدولي للاتصالات، أن الضربات الدفاعية الإيرانية ضد القوات الأمريكية المتمركزة على الأراضي القطرية "كانت موجهة نحو المنشآت العسكرية الأمريكية. [...] ولم يتم استهداف أي مناطق مدنية".
‏الاستثناء الوحيد الذي ادّعته قطر هو الهجوم على منشأة غاز في 18 مارس/آذار. لكن تجدر الإشارة إلى أن المنشآت التي استُهدفت في ذلك اليوم كانت تخدم العدوان العسكري الأمريكي على إيران.
‏يتناقض هذا بشكل صارخ مع سجل الولايات المتحدة الطويل في شن هجمات متعمدة على أهداف مدنية - المدارس والمستشفيات والأحياء السكنية وحفلات الزفاف والجسور وغيرها.
‏هناك فرق شاسع بين أمة متحضرة تعلمت أهمية الالتزام بالمبادئ الأخلاقية والإنسانية حتى في ظل الظروف الأكثر إيلاماً، وبين الحكام المتعطشين للحرب الذين لا يلتزمون بسيادة القانون أو الأخلاق في ممارسة سلطتهم.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89337" target="_blank">📅 23:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
ترامب:
كان لديهم ثلاثة مواقع، والآن ربما يكون لديهم جبل الفأس. لقد تم تدمير المواقع الثلاثة... لدينا كاميرات في كل منطقة رئيسية من المواقع الثلاثة الأولى، ولدينا أيضًا كاميرات على جبل الفأس. نحن نعرف كل من يدخل ويخرج.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89336" target="_blank">📅 23:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89334">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
ترامب
: لقد فعلت الصواب بشأن إيران، أريد فقط إنهاء الحرب في أوكرانيا، لم تكن المملكة المتحدة موجودة لمساعدتي.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89334" target="_blank">📅 21:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89333">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجار عبوة ناسفة في صحراء محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89333" target="_blank">📅 21:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89332">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857088ab20.mp4?token=STG9DNcLhr1YZYLeR36xfRowyigXGBiN1lZsjapbkondG7q6dZEPeeQ3fhmRjZws9nrzlGGKKA99MV6SzhsJg5-kyvuaTP4OiD_7OITqzthgJPd7TU9sAzErvnILivJJEvWaeSTBTldxFy8Kp6cHuCx1nTdHd_PyHUTpBG1vbZGDmxQY4ALQi3fmYH3B20Y1CJl4Bal49ZzYoBgEre8vGfK7A1KcEWjAxiVA6yTyJsbnE3MCorQlG0nSui85mYv_EPSZX_lMAbt2JHgC8Dnvtxq_aaALqsYI668cXjk5vpA6EBELIQEx505KZRuVIbwXSfIyRm5wTEAwg7GNDNuTVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857088ab20.mp4?token=STG9DNcLhr1YZYLeR36xfRowyigXGBiN1lZsjapbkondG7q6dZEPeeQ3fhmRjZws9nrzlGGKKA99MV6SzhsJg5-kyvuaTP4OiD_7OITqzthgJPd7TU9sAzErvnILivJJEvWaeSTBTldxFy8Kp6cHuCx1nTdHd_PyHUTpBG1vbZGDmxQY4ALQi3fmYH3B20Y1CJl4Bal49ZzYoBgEre8vGfK7A1KcEWjAxiVA6yTyJsbnE3MCorQlG0nSui85mYv_EPSZX_lMAbt2JHgC8Dnvtxq_aaALqsYI668cXjk5vpA6EBELIQEx505KZRuVIbwXSfIyRm5wTEAwg7GNDNuTVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏فانس: لا أعتقد أن لدينا أي معلومات بخصوص هجوم الزفاف، الولايات المتحدة لا تستهدف المدنيين أبدًا في القتال، ولن نفعل ذلك أبدًا.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89332" target="_blank">📅 21:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89331">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
وكالة فارس: ارتفاع عدد الشهداء في الهجوم الأمريكي على حفل زفاف في سيريك إلى 5 أشخاص.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89331" target="_blank">📅 21:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89330">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNGj4YwbuDcG1oa_D3Raj49DwHk-ShhJAPdOvztiYsXvzt2EscP88pNrpP57jhVMfbAp-yD1HjtS_ezlxqMmvTEw1NEVdHtb9q-evHJ0PCTQaz_h5Vxg_GAs0EgJ9iH_gCafTqv6Qpz7SkOP3v2nt4lS9TL1UuRBoa9ad5VkiKNYVpN8-vp2GLjf_NL-DbGcvJATFpWUDHQCsKCGfFYMBXuIc4DGuKrDhsQJqEPqRoc35eb3bYOf5cIXMZ0V2HA-bO4Db7sF5dEezuBBPXre3leqhc-gL-tTYnZdXJJxk8TmKULX7yhJcdbB61UE0OveDLiMneHdHSckxLvGTj00bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
طائرة مسيرة مجهولة المصدر تحلق قبالة سواحل الجمهورية الإسلامية في إيران وبسبب التشويش تظهر كانّها داخل اجواء ايران .</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89330" target="_blank">📅 21:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
انباء متداولة عن إطلاقات من ايران نحو المصالح الاميركية في المنطقة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89329" target="_blank">📅 20:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
قال ترامب إنه سيطلب من الدول الأوروبية تعويض الولايات المتحدة عن المساعدات العسكرية والذخائر التي سبق إرسالها إلى أوكرانيا، في حين بدا أنه يشير إلى وقف المزيد من المبيعات للدول الحليفة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89328" target="_blank">📅 20:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇦
زيلينسكي
: روسيا أحرقت مصنعًا لشركة "كوكا كولا" - وهي إشارة واضحة إلى أمريكا
😫</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/89327" target="_blank">📅 20:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki6xr_0KOfEZ2Qx9WdavOVDK9_8cIe9OM6Pe8m6sHE734Aev5Dg5AK2szLg9vjep3ix-sClLS87tkFOpKC981K3JVmg2TSHe1Vy3TXrSYWCRPhKX3bCA0OL7dOGmkVLOF3HyNXmSXXIAwTr9OnebFOePy8DVS7AdyGO9Ge21hKn08RDKOYwpYaZLeDhUdwJAAYSNzyPj2R2P7boyvLPnIs84VLW2lBjXni6LsjjOgxYm3zUj1-YpKFcpSwsGPUvr3ZGmcaBvcfrkPhPAqj_ouljo-yTXlw-ibvCDtGZrfHsjRSGwR5bbb_Pt_15XQheAvmdZ8FphtpIKK0fCIps0EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
قاليباف
: ابذل جهدًا أكبر يا بطل. كأن مستقبلك المهني يعتمد على ذلك (لأنه كذلك بالفعل). أو استنزف مواردك إلى ما دون مستوى الخطر وشاهد كهوفك تنهار (مع مستقبلك المهني). أو صلِّ لآلهة الملح في برايان ماوند.
‏العالم لديه بالفعل ما يكفيه من الفشار</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89325" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
وزارة الاتصالات العراقية:
وجهنا بتخفيض أسعار الإنترنت المزود لدوائر الدولة كافة بنسبة تخفيض 40% (السعات ثابتة والسعر منخفض -40%).
كما وجهنا بزيادة سرعات إنترنت الأبراج المزود للمواطنين في المناطق التي لم تُغطَّ بخدمة الكيبل الضوئي وبنسبة زيادة قدرها 40% (السعر ثابت والسعات مرتفعة +40%)، وتلتزم الشركات المزودة للإنترنت بسياسة الوزارة المتضمنة باقتين فقط (باقتين لاشتراكات الأبراج واربع باقات لاشتراكات الكيبل).</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89324" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADOrXP_CBzOxWCNEsuTK7jkyhZyAgovpcvbPZh3Y80yc5AU4xdDqkZ2bgiBRxeKgwZq-G38Ig9YCPkKDsvOuAx-YzkYA51Bctp9uamuVZpAHofElYe1Zdm3Uj0wIJIFwjqmBW_S66Vg30ZRmEmmWX_Glm_uAeIk54lmqnM8tELsrg9mn5Iij97FepgIkPmeEUX73Xg5wk4Xo68_yN6Xj1ENHw6WKXCVWP5pU_V1IUFSGbogt9LE139rXXbEp_LSNN_HWJ4TZ1LCScDLWi9BiLbsKuuH_eWC109PI2uZFF21bXNzPQikMUKr4CNg_xwAbWCM0yO4utzC8US3n-mPLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
الولايلت المتحدة تضع مكافأة لمن يدلي بالمعلومات عن قائد قيادة العمليات السيبرانية التابعة للحرس الثوري الإسلامي، لاستهدافه البنية التحتية الحيوية للولايات المتحدة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89323" target="_blank">📅 20:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7aabb08e2.mp4?token=rKgfavcr6NRKlxbn83Kgjg89Xxx_fHYWEFPGDUmb5zPaww9HVG-RKWrrTJ5YfgsiTOLWZGcS8ziJZ_ENHJn7EafCgq7acjiBk7wZlStWXuYC_Eax6m7SCYSHIYE7-uFAW5koab2Z6K8bGyXlm-DTC9fDhsDa9whYQPoQKZVC4dxrEOfrKzOUJfqWjCraAoi3i0_uaLCdvilmb4Bf_AB7CotGugiZLxqdB2o5HYGNGxopP9vWzGHQV7kgQ1cJlSzlLiU6RQhxYGEAqurnCV551n92XchdOqetub7-DKfe4oeVWwZYBlHazAKzlqOLx7_h0vE4Rs64nLy03lAo0xKodw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7aabb08e2.mp4?token=rKgfavcr6NRKlxbn83Kgjg89Xxx_fHYWEFPGDUmb5zPaww9HVG-RKWrrTJ5YfgsiTOLWZGcS8ziJZ_ENHJn7EafCgq7acjiBk7wZlStWXuYC_Eax6m7SCYSHIYE7-uFAW5koab2Z6K8bGyXlm-DTC9fDhsDa9whYQPoQKZVC4dxrEOfrKzOUJfqWjCraAoi3i0_uaLCdvilmb4Bf_AB7CotGugiZLxqdB2o5HYGNGxopP9vWzGHQV7kgQ1cJlSzlLiU6RQhxYGEAqurnCV551n92XchdOqetub7-DKfe4oeVWwZYBlHazAKzlqOLx7_h0vE4Rs64nLy03lAo0xKodw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
في خبر معتاد...
الاحتلال الصهيوني يشن غارة جوية على العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89322" target="_blank">📅 19:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇱
‏
نتن ياهو للمرة المليار:
نحن على ثقة بقدرتنا على إسقاط النظام الإيراني. هذه هي المهمة الأساسية، وهي وشيكة التنفيذ.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89321" target="_blank">📅 19:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انباء عن اطلاق صواريخ باتجاه مضيق هرمز</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89320" target="_blank">📅 19:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq7_CMZJQO3uxdAP5Z0wgpTVb4S9mM6v4MuOljxWWRI83X4ccvTc_mnaRbYE4qlrMCdBhwvNFu2ZG8d3m5HLzxrC5aRVotSW3uBmIXMVybeov_T2fyzkD6phReS105HKSDi1nGCYkz5CLQFspJ8tUR-SE1XYjozD9Cn8vCHo2ANTlkq6NFjqU9CVaiZ6sGmbVcNlWPtqWbACIeyHCSHm3hh-XhRo1mb3PJRBI2Zbpfdy2K6YgjkdHS7HB1HQv9y22TktV0BIdR1btcIUD-o0e7WykpTWHuBDo5Mp9MqMmonPvrhNSIW781fLBtit7gcGzB0kRvHm6J-hYn9hLEL2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يهدد كندا:
من الجيد جدًا للسياسيين الكنديين مثل رئيس الوزراء كارني أن يجعلوا الرئيس دونالد ج. ترامب "عدوًا"، إلى أن ينهار اقتصادهم، وعندها سيثبت أنه سيء ​​للغاية للسياسة، أسوأ من أي شيء حدث لسياسي كندي على الإطلاق. ترقبوا فقط!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89319" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">توقف ادوات الذكاء الاصطناعي Claude وGrok ايضا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89318" target="_blank">📅 18:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQjhoj8ilathf-6uT3RzWqh3JZ8P1uVvSxdZtTqabTiTBLZPjdi96ghgnnDbeS5j8tHUBJt698jEVx0ycTYgfrJHbIjxI8PZTS70GTWKDVCJJFXPeQLMH_ZRTClwJIg68U3u6MfdYkgWBL_fMZJUyHNW7jd0NUv8TKtaDoMZCiyDO_dnfN9nphonres30y5ryrTmJEHUYM4Dq-D6u9bw1svHDXttEN2ymqFjafaCvDpXE3gzrXK6dE27WlURvXBxRxfGELHuJ6OTeS6SLLfWg1SzD7oZmQwdwHi4qKcENhlLh6fOd17h8Xl728JAuPV_WqizOAVLu_4JtxZqZA4oGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
ترامب:
بالنسبة للخونة الأوغاد الذين يرفضون الإبلاغ بدقة عن عمليتنا العسكرية في إيران، لدينا كميات غير محدودة تقريبًا من الذخيرة متوسطة إلى عالية الجودة، أكثر بكثير مما يمكننا استخدامه في هذه الحرب، أو في أي حرب أخرى (وهو أمر مستبعد للغاية!)، والتي قد تندلع بشكل غير محتمل. بالإضافة إلى ذلك، فإننا ننتج الذخائر بمستويات لم نشهدها من قبل. نحن نخزنها ونستعد لأي طارئ قد يحدث. نحن نأخذها لأنفسنا، الولايات المتحدة الأمريكية، بدلاً من بيعها للآخرين، لكن المبيعات للحلفاء ستبدأ قريبًا مرة أخرى. أيضًا، يرجى العلم أن إدارة بايدن قدمت ذخائر لأوكرانيا أكثر بكثير، دون أي تكلفة عليها على الإطلاق، مما استخدمناه في إيران. تم منح مئات المليارات من الدولارات لأوكرانيا وحلف شمال الأطلسي مجانًا، والتي كانت أوروبا ستدفع ثمنها لو طُلب منها ذلك، لكننا سنطلب تلك الأموال، وإن كان ذلك متأخرًا بعض الشيء!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89317" target="_blank">📅 18:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1wRH7r5no22iXPh9oCe1AvCOwYvKylijCgK9yeE9M1x4VOBnzotf2Ue_R3AW3ValZui24TeeZ6lyKn_KRtbxmwPa1oPD0boUiibJkvWkd6FjqPB1vqyGYSrs3SKWj5cT75kDcCU4huXTJLka90cw2TH3qHSH-rO5PNSx-XvHYoR_ZB26i9rgTEW4XyGwyVK17GantnN_38VDwCH7BK8b1hLtMfWlsTBVYTZ7CGOLZoeIH8ipH8KuRboHte2_mq9scITDYi1UlZgJtsUigEAqkAMJi64OM7NGmZk1wcVlNPO-cto-PhBRCVsm2qiMCYwAfbGexb7XF7ZMvS4yJjvow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تقني
▫️
توقف تطبيق الذكاء الاصطناعي ChatGPT عن العمل لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/89316" target="_blank">📅 18:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1BACuxeYfFmpUmjC7T0lqh-QFhWplIjIaNG0vVs2bbFbg8_q1ZhQBLP83WkdHxoPNqd0gJ8RgJCCSyqg_zAjCBXRRczq86rhYZPPQoT8LC7vDvueIvu5zHsCrvlWJ6_cFeVMb2p-nbOd2jCj3hE4gt_kuxIxYCs0gCJ1UxIBXhMs1QQeZMBrzPokDqyZmBKPJoe80iPE1phYi393m2IX7iQMnso1la_TQdv-YW2uupj1Vh57g9hWcmT-TuV_S1Ed6AN-uXAjs5J3OfQUD-wNGrq168SmstZ82HTEt0gd2Ril9wpt7j8n1dJ8jRNUI5UoxnhhiSkoQSIyISJh5nJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
‏
ترامب:
إنّ الأشخاص ووسائل الإعلام الذين يصرّون على حقيقة أننا لا نملك ذخيرة (وهم مخطئون تمامًا!)، هم في الواقع خونة. يفعلون ذلك لأنهم يفضّلون أن تخسر الولايات المتحدة حربًا ننتصر فيها بسهولة، على أن يروني أنتصر!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89315" target="_blank">📅 18:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89314">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">#تقني
▫️
توقف تطبيق الذكاء الاصطناعي ChatGPT عن العمل لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89314" target="_blank">📅 18:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
وكالة فارس:
ارتفاع عدد الشهداء في الهجوم الأمريكي على حفل زفاف في سيريك إلى 5 أشخاص.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/89313" target="_blank">📅 18:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89312">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
ارتفاع صادرات العراق من النفط الخام إلى 2.340 مليون برميل يوميا وهو ما يعادل 71% من الصادرات النفطية قبل اغلاق المضيق.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89312" target="_blank">📅 18:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89311">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwOgLRwBPB6JvwsEHItkGVHVXPGvFXR3dxqYqQARoD8i4WRlV-bVu8_5CPrvyyAp54r3iGzyYMKNiSZN2Vd4NLEOD13M7xNJHCrJrFomoC1H2PC8u844l5xox9fczjTY40eSGfRf4Y3MnZ8IpYvzqo56vJUoIiN-1vGCMCLx7jzhvyFzMREND3LyojQxcRWdoedHwGGeSuhZ2spKKPiX0Jqk2_PF_fvWtEEv2utNytfLuPKJOYAPS7ptL_b0Yqst3ypvVNz2Qo0or4wwmPc9MKaqaGbplivmrSC3i91LESQvNipXOoddZYAq3LX1_SIEi0XpVMlEE3mchMNRSRQBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارحلوا أيها الجبناء
تسقط الوصاية الأمريكية على العراق</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89311" target="_blank">📅 17:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اعلام العدو يقول ان السلطة اللبنانية سلمت الكيان خرائط وصورا لمقابر ومواقع أخرى يحتمل أن تكون فيها أدلة أو رفات لجنود صهاينة</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89310" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89309">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇨🇳
🇷🇺
بعد طلب وزير الخزانة الامريكي من العالم يوم امس بالابتعاد عن روسيا..
وكالة شينخوا الصينية الرسمية:
الصين تعمق التعاون الاستثماري مع روسيا.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89309" target="_blank">📅 17:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏نظام ال سعود يعلن تقديم دعم مالي لمرتزقته في اليمن ويؤكد ارساله لما يسمى بـ"البنك المركزي اليمني".</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89308" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89307">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPtDVlComuxjRxsWUwLULmmciJ8gneX0S--msO3TdfLMbmBeq3qc037dL7W_YYdWt6t1lMVguxfWl9m16DC_ibO0zTwAyluwAlwIRn9WkQK8jE3RE16_2FvVJGk3qhNjIP5-Iugmenls1CjnBT-a9oh6DzMSl3YhoCweXpCrWsiXvXSkfyGfKcdqLjA8aNjiLFzo7iP9qK-tI7eBcMeSvC3-U89XjHRHRBxjVoqMPExfW0zvUbcWyAGvAcVqGcMB1bcyqlM994b1d30jo8-UT6V6MzDehNnDQsSUxAWfwegaws6YLIWjyh_vgXuHfDQcvvUnN0aI4jKYlufVRjox9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
القائد العام لحرس الثورة:
لن يضيع دم شهداء كوهستاك المظلومين، وسيُحاسب مرتكبو هذه الجريمة وقادتها. سيحمي الحرس الثوري والقوات المسلحة الأخرى حرمة دماء شهداء كوهستاك وشهداء سيادة إيران الإسلامية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89307" target="_blank">📅 16:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد نوعية جديدة لاستهداف القوات المسلحة اليمنية تجمعات وآليات العدو السعودي في عدة جبهات بطائرة رجوم المسيرة</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/89306" target="_blank">📅 16:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89296">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TA8cPGFQ376LT4mVagSJAL_38eaAUdofbWIpBlwmM4DAX1VaSf61PIRlQ9Sw7N8xrCUsgsk2lGJPEKhVHTAVKW8pX_Rwaq8dBp5FhrivFOde8ey2r7hmYC63Dq5eyB-gIlFytXmL2V-i_Z2BzkymZt80sRuV9qgRr27U5XL--PN4JvYTBaXbQ9mr63F-EShTbipUn0tqNpC20pvJEAtuelLR5XmenOZ-V-_odBLEy_sRX_xvm-BXNB_96Mox05Sf9D8tU-1Baf96ZItl08WV5P9civD1W7cqS4wtAXHYW60ys1oZOJsxD4YGUxwqYTWnsnnH2HsSXLavPD_57sC_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emc0ztKCC0r54v77tyyMYKXTxpAkY2nkWxqxukhTOuChcOhj2gFfFO9Y0_qm8u2PnwWx7h-0x5p9Cc-otTaj3Y5G8QQ0L9BGee8nFEvTtVn99KcRHHMBsdiMN_6T9V-GTxbOV-zz8w8Zuhl8Cuy9NLLhMndMcp2w9Tx6zufZrMJoOSMC3BFIsAbSpLM8wWiV4aeWbuxm1jUpmTU6z-Kc8h6ONfV4pUCkrAsnntobNjQBVa5U1x6TQlMlL1jW7r6sUJgknN_nWjr3QOJsXBSJacokyKtyKfcK_Eg7wA9aJSxgsYLx_NtC_W0DN2FuRcK5AWYiZEdCJYOea8yDwSLonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zx37QrEA37JHehsU2gqUMJdywXUSDkGhM_NifKF2zSQambSReDH6Q8yVk-NdFwR-eQBXGky372c8h0JCodpuN6TrEPQc46hNfZFM6HhPfLX7F06AjYJ4MC8z-6ll6DcGyhm0b69A48mTh1DlLnxVndEFKunf6Dr0eCvWn5_Frr3lOdEEuQyNl6SP4JMHzyOkdwVNqk8T6poIsGxYcfeHG7nv4mCuzkYA5KjjTj_MzR3J-0_-hkin-C7kEYv-VZEWi9v391Py3N_GEvFPtbiQf500CoeFgNNjdAkQo9wGdERLJJ7tVI9lM4D9JIccOsAAUg2w2Xhc1WM0Fln7a-tkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7sNBpPlJ6HAqSTIuvvsFMJkUwFKzExLBPv9Y6RxDYjvKFw7ZxgznP4IDsVw7t4KvL09TTdYEHnQCe-1OXlvyFoCxD8eMdkRmuJPwCah6I2S6yymsH8TciwPX6ylc2r-pvc9NP-2wf-8U0_2NJKsHnbZ90mMy3yVqDZQ0_fwlCzIL_UM9yX2DBhcoQFRiKsQ_F1ExfsCRBzplkojHz7zh0g9a3ZXbD0BKY-h5sY3Rt1vsmrKftyAB9nOGLqYL-HShIu_9FbHLfDYbk11eJSx26X1rWAGcjCcK-koX2gLLLwWIlsk2bYYTjkPRdo1rwFnZEHzDii33kiJTP0knmNPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPPyA_cpc6Iil1zgnizg21ry1H6tndJw9X7w7PfSUWsf3Z3AjAcFkSLZUnBk16pmrRmQjmKI-im5eNS4X8opQvOCzt1NGbq9UVR2rS8KA0y9dH8ZdFq03tAYzpl8hmpex09Xvq5gDsT5UbZYsPAkWUUFZGGDTrM1tRCPbMBm_FL9Y2diEESU1pb0fNUmaR0Raoe1kKHYJDjyg3H3Jmk5QKUosEqxLwO3q7Q2ePXNVsG83B0akW9uSGx0MCr0bFr7Al4VCqPIBOFBWbNIWThDKAx4ladt36a0RkxNjqri47IXUuOaHnKCm-tLlzd25v8SIKOjSQ9ECsPHpmkK8z8XvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4PYV3nQs6ennicG9FmgWsEyUvxEZnxKy72tmhD9NSKHTQ8aCssqSXOdf938uWEwllvUArMp4Qm1oShfuDbutkgxaQ2I07aE1MQDTh6jJGdjCnGB5C170SE5TenAWF_bkuQIRxJMCK6mPkX73QNaqPPvX8bjTktG7n6Gjc1SdoaZe0LB3vT0Ds1eRwRsE4MYRtScGso5X991aY_RFkFpFq0Q_LdKa3uDBLcn5hQtM47FI2Ru_3OlblbI-f0uCE-416zPu-xrSBVV-15FAd3zpYCW3Lwom38_eLX2U6BluQPYWFyH__FoKctGrtdnLk9EtJATA8km5ZL-gVW7gKsxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixj6ToFug16AQb0fIQan_nTNS1aqvzWMLSQ4YRSWt7_49nE76zA8QMbJezOlwvLEabaSYPdz3-qlq2T4gzBncVC8OlHwEYZNMy-_vQ3Qsg7jJkkW2vmCCiBfHipVRPcQ2twIlRYBvn9Z8c3VusaM-xwZzYZXilRLbEi4Y4z0DMHiEwkENcUaDvhNo5eFrK_GrIdx3hXJyW1d_x087wFF1r_heLIYnIqZCnFy6b0h5TPOZuw-Gb6_otl24LdTWjhsUCGVsR4b2hYndRFnQZelhtfCmbIIH9xwIeZx6jHOyiBMFp1D0gCBLVnARx91lck07P0FLOfWxNOaBAwYL-MJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bubtvV40lppzUk1PyHeuVLRnfCHPq0bTcnxyoUSPuo3cOiiRbqJ2j7bLpRcoZV6dX5hNus8QEMAU1gCpQ_mNm4lFtQEv9ldXvyk5W8z-3md3Rm1mlsPniMC21bp2Ti1eD7mlDvq7ij48QptNlvUgBb2UGzrKAO9hunsb2PKTdhAiQSpSKUYWWYVQUJSzN1wNM80erhXY0ppHPvMrHcQUcHL4FaCODi7MOXcu-8csVmltaHFjCR12teYiMM2iOKCxG4uLoRsYj_m7vdR8ULhpqg5uTkDvcIXCpUeb_Yw5daE8M4s0Csb9P9anjMKheZdkV7rNl6rKM_idiuoFV623FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IR7psAF6lw6wxhWhzh56upvxEYH919vXbQF8P7FZna98DitQzl3QqhPA7DugC54CRmZV0a4_LFpdruNM0gny4QgQy660p4IastoajeYvaYHwbaVUtq-1WwKxRDsinAPK8io35N8hQERKbq8SgkLHtS2o9b2lnrQ0k5KWUBQ3AnY2K9bxucBSJvjIXBD8H-SpiN7OzxuLJ0oXZF9bggXUAqOzwKdcehAt_mtkmYSwjIwkCMqne65Ay7BlCSTQZbwOJZIoq1iuOKNL8GAwd5KdpoIv2AxWFH3_Ka9_N3ajeUyDdesGSOo6xKWTOe-1je3UgO-WRS_QH3eV4XwgJaVBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tc2nTIDnOPeUvs590OCX7Ue8tAP6q9GKNULKGBJAlo-LET1lKOZB0i9Ay9IkfYS049O6QtfKTmWM9NwjGmRr3AEREqeMEfnlWp_yJNUjzoWMTOrG3BUOKYoWm5gEbAtXmULnq8ay0dUmwv8rLjAqUov44nrQj96xuHDe1hr8PgTXM54rH9R7dOUrxzRwmj6oPHelhB2oVOD8FcxWT1Tl5FzMsbBN-iee5chIfklJa5NTLt2I4rRSkYLx2WHFdABm9nd0xCP_Kt07zqJmiZKYbkQI62NCxMVTT3OOFEPECHm82Wj26Jo-HqJwomI3vRbdp-mAC7Z5kE22vNEk7a7zuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
صور من مشاهد نوعية جديدة لاستهداف القوات المسلحة اليمنية تجمعات وآليات العدو السعودي في عدة جبهات بطائرة رجوم المسيرة</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89296" target="_blank">📅 16:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89295">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c54e19f0f.mp4?token=kEusLmhqidfnaw1oV0IkZ8SnP514Hn_NKUDkJ8Lx3CrL3i8r6GWg9OeG4zrP7JMi32aEO58KrYuNT3FNh_9xZ4WeljOt8Evur2Iw2mBFe15xo3XASHJaHCGckZGBtW6XPerCArgPbfoblM2q5CY7GHLER4KeE7ldqFFB5nWTctfqvIDfu690ps2tiXMrFkadtwik1gAUALtAvbtxlZ0ecR9-e-NKID7EgOXHK5Lqx3rvMNSvXSA0pRfpuayzt-_hPNtKg54R6kTgPbssrhHEcO5zWa5gLda93zYdaGE76WCWZg6AephllnIOLMjmV0hJs8hAbW65q3R7GOfG1xIK5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c54e19f0f.mp4?token=kEusLmhqidfnaw1oV0IkZ8SnP514Hn_NKUDkJ8Lx3CrL3i8r6GWg9OeG4zrP7JMi32aEO58KrYuNT3FNh_9xZ4WeljOt8Evur2Iw2mBFe15xo3XASHJaHCGckZGBtW6XPerCArgPbfoblM2q5CY7GHLER4KeE7ldqFFB5nWTctfqvIDfu690ps2tiXMrFkadtwik1gAUALtAvbtxlZ0ecR9-e-NKID7EgOXHK5Lqx3rvMNSvXSA0pRfpuayzt-_hPNtKg54R6kTgPbssrhHEcO5zWa5gLda93zYdaGE76WCWZg6AephllnIOLMjmV0hJs8hAbW65q3R7GOfG1xIK5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
قوات انصار الله تسيطر على مواقع تابعة لمرتزقة السعودية في جبهات الكدحة بمديرية المعافر والطوير والأحطوب والكويحة بمديرية جبل حبشي وصولا إلى جبل غباري بمديرية الوازعية والعقمة بمديرية موزع مع استمرار المواجهات الضارية وسقوط عدد كبير من القتلى والجرحى في…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/89295" target="_blank">📅 16:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89294">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
🇾🇪
قوات انصار الله تسيطر على مواقع تابعة لمرتزقة السعودية في جبهات الكدحة بمديرية المعافر والطوير والأحطوب والكويحة بمديرية جبل حبشي وصولا إلى جبل غباري بمديرية الوازعية والعقمة بمديرية موزع مع استمرار المواجهات الضارية وسقوط عدد كبير من القتلى والجرحى في صفوف المرتزقة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89294" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89293">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnaXSZJhOh56jdHyK1T6990my8jvs4bsKFf-VMd1wD_8yuBHgcEbtBmpJt64Ja_AkdB_YNzY_luC3V2SO6SmBEswZvQHAjd2fOqp0Rab3eem9PPI5HhS1LFccHIEd_MsNZo7Zr9kPJ8vz8meWNwObssiXEgzxTR-XWEzbzwpfJMhOmTtz4H01UOICvb1kDFwGMcXJYCSQLMWRJ38huOJ5fIA0Wqf2eudNEsJcRE3gW3-Tfp7_Nyyg81Yj-4BW22ou30a4QfjsQ7O0ME6Q9jvIqYC0Mx5j0qE_QcvEia6v6hR0QzziNbhqMZuux3YPCAm820xHrkJxi2Hgp2rCwvE4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
استشهاد 6 من عناصر القوات البحرية الايرانية التابعة للجيش في هجوم إرهابي امريكي على جنوب البلاد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89293" target="_blank">📅 15:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89290">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZMrQ3Ewy5pTMcB60VpJQm9W3chw384ULpScF49Ym9GykrSSnoY4hKyDJCmISpQRyJe_PJGuF_iARgNXOohlgDuRI-hJBP1GHj8xtE7PPSiGyHyIrv31xTivUcp_k7VDX08eosEqtCsVwS3rKpifqVXP_M1gDaRUTkL2Tp80efPQgZIoHEuHsJ20EVSn7ZPi-eKJpksGArbn8JWxZBsTDX_A9joJ_poTMCFu_noqdYICOPvQB30Ws-yOPlP0EiMmAg5OZrCcYpDNX1noof4S2MmEF3fDyib1AEi7CxEa_vA84WSbbH_2G3j-i6gpGzX1V89R_RlKmnprlX8OUPZQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPBtrqdt49ESAnjwC249HGcU7_TbMxyk7HuPBe32DHgnICXPy6mxuR7B-HvGKXVvrYSa2QK_qy0baexNz_SgoDbERjU7envTv9y3POKzY5XgGiP473FF1IDX-ejcj2wG1y605ulfnidUu160UxqD-zivmBjqLqya2Ucgn7dsdcMh1jrXLNGCcJHBCs79xkxJQiItbERiB4nu2Dx2Wus4i8iawJat7s5oJWjvbWEejI78hE53MdHEb-9wQArT7cHOX8EN933SHFBHc7Gv1LyOHqQ6KK4oca7xWSq9MObALR5c9nEhEKW3Tq7T_kmFfZx3bwJdfOOtn3lD65zyw8QKYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcjEoxtets7k4CvSd81mCUQgW8S8t2j1Tl_twjLqpJvUAB-6R1WV8TnGgOfwYF33L3aIMXgBDOsiLduIjJ0tVaQYfBtxCS8AH8z-6dazs7hvoqtsa9cnrFYjNY4vuKRmcwJg4uwjPi9BaghtKNcCRdBXiPTw4r71wp4FXX7inK19pERzP3OCf9oAl53kBY6J3TsHN-FfZ_kmISsqqxeMqfyXayWHtoDYtWz5pWnh6rfIMf-IdU6LWn5jmzDAVXuqGT2bSDr9hwiFng3lEgjeE1e1ERhENiGWAwOAp1TJrvRDBPVuVeEgJELowmn0HiEfdhN6BFJVptJnkoXq0xmtQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#ترفيهي
🇰🇼
‏دويلة الكويت تدرج الهجمات الإيرانية على القواعد الامريكية ضمن المناهج الدراسية الجديدة وتبدا بتعليم الاطفال انها اعتداءات ايرانية على الكويت.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89290" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89287">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCEO6FEcKZyClKhY0Yzbj3zpb760zJv_TLQhjDvNA-7Tf507BsIJMJ38pdUXSM2vLVPbi005gtaFQBM884Ng45ozb8vH9OkyOIsLOK-GkqIjB7yRSEU6wEvpmQD6g9hiieEWJq4b1jY9sVaFop1ZfXWBMIHoLIqyHdhOn3i3a8PWR76seWVv7CIzy3VTbVKCbACdpI42Kiqa-u8fAhrM-Xlpo6lKx3asSPS_fsZnWwYu1xcGBB5uBsMqJAMDGS86yh3jCAM8FQo7XkfgYw0ZrdU6iZijyt-tMJUwg1SxWnZWu-tLYFV_8lRTLukV8ii0jzAxjcT1n9HYiDZWZDqBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BL0xZ7zOOf1GXQRZIOGc432_uQcto0MuZkQhC2044lKMB8WQHx43bVzY5zjW5pA7MjTp6hYgqcWqp1oH6aj9OEwm24Z8bjy-0Bf2_Pj26edro4UeYqAAxjLjMwab4xy4Y3NtqJI12N1SGw2SinQmAy5FNeNfbtiaz610LpwfiFBaeOQ19JqQSqjTwW9vQSK6yDEA7eHbuPDyq_66s_GWw-ge33X2UgyhHmlHP8mRNWjhI9LgRg2-8I61D07jinT6043-SAT5O83PrMvRP7hPb7mdNVzTLbvOm5LqvXjy8_4E_O5JiMZD78m7_LO1FBj8ZtC8ectvH0QxwPBxvW5pVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsvyK47Z-XqFaEY2Gu-5gLirwmE3tfr8ovbTyOYxVfpLiv9z3Swu7XK_Wb8GMOS6D3G9ikoCwnFceDc_oAnRYfl2sStLKkFMTrtMb2GK2yzrwQ3R653d13MYBRbPOIzC4K9AK2-SseeYSjxYTWt3thWXkCI1_kbbExuhZUKtTuO0f9K36zAKrN3w5284mmKzLcPqv3ajsMD5saBDuGJkyydX3e67wCcOAMDWWPfgGoclCriTaRW1cxBvC2w2VCR_DIwcVMnRRbvZ1CYz2apPCV54-ufmvheuU9bOhMjihK8eDZZVpXyl2ZqDwI0evWYWqeaXu8xpN9aAXTNXGjPSrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
استشهاد 3 طيارين من الجيش في هجوم أمريكي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89287" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89286">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
🇺🇸
🇮🇶
الحكم على ثلاثة مجاهدين بالسجن لمدة ١٥ عام بعد هجومهم على القاعدة الفرنسية في محافظة كركوك بصواريخ الكاتيوشا اثناء حرب الجمهورية الإسلامية في ايران ضد الولايات المتحدة الأمريكية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89286" target="_blank">📅 13:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHjKGO7_ktVIgrfiT3uzibxD95MvmwaAbhU1aVHPsJSbtT2pkPPKG-RY1sTHiez5sTM6tYy7naL50YZfJfGakfBrjixIF5KNfwAoeVKRKwbbhXekCw5wOvwRnGSMKah_f4p2jkRLclEwNrZZZMtJ9MHNPMHZpGRPJQRKM3QGGPdzcZkB15AJOT4MeXSIXYsYwyVw4gzVXJObkRF8QjPNFWzG20KBui7l2VL1DBb9Xdc42yvc67iD97PWbvVi5eW_7JO0XqY4LC69G_gVruQ1cQOzemtxtzM6XAjmMFNUuIxw958mkTns84ee9g-7pvq3nTxSj3qrpq0Q699W6-Qc5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇸
وفد قيادي من حركة المقاومة الإسلامية حماس يجري زيارة إلى الجمهورية الإسلامية التقى خلالها بكبار المسؤولين الإيرانيين وقدم الوفد شرحا مفصلا لما توصلت إليه الحركة مع الوسطاء وممثلي مجلس السلام من اتفاق على خارطة الطريق لتنفيذ المرحلة الثانية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/89285" target="_blank">📅 13:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89284">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة الرابعة عصرا مشاهد نوعية جديدة لاستهداف تجمعات وآليات العدو السعودي في عدة جبهات بطائرة رجوم المسيرة</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89284" target="_blank">📅 13:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89283">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن تستهدف تعز بالصواريخ الباليستية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/89283" target="_blank">📅 13:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89282">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔵
🇷🇺
بولندا تستدعي سفير روسيا في وارشو.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/89282" target="_blank">📅 12:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89281">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇷🇺
🔵
هل انتقلت الحرب إلى ألمانيا ؟!  ألمانيا تستحق "ضربة مباشرة تستهدف جميع مصانع الأسلحة الألمانية التي تزود العصابات البنديرية "، هذا ما صرح به نائب رئيس مجلس الأمن الروسي، دميتري ميدفيديف، في تعليقه على اتهامات برلين لموسكو بـ هجوم على مطار لايبزيغ.
🇷🇺
…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/89281" target="_blank">📅 12:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89280">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن تستهدف تعز بالصواريخ الباليستية</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89280" target="_blank">📅 12:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89279">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇷🇺
🔵
هل انتقلت الحرب إلى ألمانيا ؟!  ألمانيا تستحق "ضربة مباشرة تستهدف جميع مصانع الأسلحة الألمانية التي تزود العصابات البنديرية "، هذا ما صرح به نائب رئيس مجلس الأمن الروسي، دميتري ميدفيديف، في تعليقه على اتهامات برلين لموسكو بـ هجوم على مطار لايبزيغ.
🇷🇺
…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/89279" target="_blank">📅 11:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89278">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇱
الاعلام العبري: تم إطلاق صافرات الإنذار في مستوطنة نيلى الواقعة في منطقة بنيامين. وذلك بناءً على معلومات استخباراتية حول وجود مقاوم في المنطقة، تم استدعاء العديد من القوات، بما في ذلك وحدة "دوبدبان" ووحدات الاستعداد المحلية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/89278" target="_blank">📅 11:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoAAV3HhcZ5CWNcRmcYpul3I6wOfILPpJyHJleNqCAJs04EFvy4w8Qnt8tAMLpvk0g915dZvq9BSePqVhQu6V-WBBliXo-Qeq6cyNKSz0uOp4tvX1-IX1xxXar2lscPpjvPZ7YH3Z4p5qiBssU_DBeF4-h0KMutgO4Ryx2HUhA6xAHlNqDOqOvxrhtCRo3_DmU3ddxklM87RalsU-exjPo1686Wi3SB6K1mS69GsJND8vzKTNB8nabK4OngP0u3cK7J-Nr-eyI_hJCoKGrcNDyKip3WPmlU9jUL1xMSmkLSA4j4S330zfl9cPpwE793rGKfKwEZuCovZNDoEeJH_OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في الكويت</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89277" target="_blank">📅 05:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89276">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
وول ستريت جورنال:
وزير الحرب الأمريكي يمدد انتشار القوات الأمريكية في الشرق الأوسط إلى عام 2027.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/89276" target="_blank">📅 05:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89275">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صواريخ ومسيرات تدك القواعد الأمريكية في الكويت</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/89275" target="_blank">📅 05:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89274">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
مسؤولون أمريكيون:
ترامب يجري، في جلسات خاصة، مباحثات مع كبار مساعديه حول إمكانية إعلان إنهاء الحرب على إيران، مشيرين إلى أن ترامب أبدى تأييده للفكرة.
كما يعتقد ترامب أن الضغوط الاقتصادية ستجبر النظام على تفكيك برنامجه النووي أو الانهيار.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/89274" target="_blank">📅 05:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89273">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgOLV7A5-J8kuwCWTGLcsnxHkZ81F7kQMQGfd5QdvXlkvvihIIjsnWmx-AGwc2J77hlIiyi1PhMSL2_dFMmmeLhuxuCMF3xTwa6HvS_fjtbx3z38JoBuGif5KqH_9vkwpbQJEWwBbHdQkFlWk-9eTGwBn6sab4zqmZ93jeFc-UBcwr1dMxcaQqg2UH_gSd9m1xAvBYGm0Y16OiLTs2yycYb6DXum1-TRhl4ueNhBwk-MkD6TxKhhGWsKHeJ_8eSgtNG3WkkVDSS-C9LzWbhSAhjIAu5KSgbVYnH10sKga-WzwT8FqTbz20VJaieLPPT3d4TyVcIK3eV37q8YdM_18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ ومسيرات تدك القواعد الأمريكية في الكويت</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/89273" target="_blank">📅 05:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89272">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات في الكويت</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/89272" target="_blank">📅 05:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89270">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارات في الكويت</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/89270" target="_blank">📅 05:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d9a8e6a5.mp4?token=Rik0RhKGCHqzYjm6RXTfLyqnmECCd26uEe6TtF83NGsH-3M5hnkJbG2LhYqBCEadXRrpYlY42NEfVQwHYJ9OU611NC8P2Wqsybsr0aYgiMGTt3BtYjIiYkhcSPvH1PhdIG-8R6qra9jgazvMSkjBoSwuc8xYktNZY7aQ2jlw1Jp9Rnljwi2rkwWHz8cjsDL74azKv3L42emEPYLkgZBf__FRFv8kIlF48NyvI2_cOJfgDl5caQkc8uEVQuw0mohO30l983EyoW-PZD1Q6aXEJmVbEyfTarEFMufSF_bz-iZHPtRgSoAdQNlSy_uco56wagSswIgsy3SGpeueaVxSyhPVI9xIruuoc9xQHfy2rtlAXtkUvr-snw8Oui65Un3MM0M662TCxc1UKztLp9ClHLxfhtvF00VY3t0uwuyyox3igfel4AWibp7FWOv5id0HfLkGYzAjpvNtidc144shD4XSBVxbSfFvztkUR_g63dZxicYer0DUYv7QL3Y0v6l4MgTBdE8je3zQSVBjQgtRKzmRoYI1XI01Rehz1Muh_EKpSPuJdfQRTEFyEQY66lD_549AUq6RcURZeZXHnofeV0twS6ijE3SFbAUGEV6oUWdaoyNiy-4tvGTzNxvx4DLK1CS3nNrgz3HeUyP00AUpLGlWE9u2iNT0xdUhQCzl9QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d9a8e6a5.mp4?token=Rik0RhKGCHqzYjm6RXTfLyqnmECCd26uEe6TtF83NGsH-3M5hnkJbG2LhYqBCEadXRrpYlY42NEfVQwHYJ9OU611NC8P2Wqsybsr0aYgiMGTt3BtYjIiYkhcSPvH1PhdIG-8R6qra9jgazvMSkjBoSwuc8xYktNZY7aQ2jlw1Jp9Rnljwi2rkwWHz8cjsDL74azKv3L42emEPYLkgZBf__FRFv8kIlF48NyvI2_cOJfgDl5caQkc8uEVQuw0mohO30l983EyoW-PZD1Q6aXEJmVbEyfTarEFMufSF_bz-iZHPtRgSoAdQNlSy_uco56wagSswIgsy3SGpeueaVxSyhPVI9xIruuoc9xQHfy2rtlAXtkUvr-snw8Oui65Un3MM0M662TCxc1UKztLp9ClHLxfhtvF00VY3t0uwuyyox3igfel4AWibp7FWOv5id0HfLkGYzAjpvNtidc144shD4XSBVxbSfFvztkUR_g63dZxicYer0DUYv7QL3Y0v6l4MgTBdE8je3zQSVBjQgtRKzmRoYI1XI01Rehz1Muh_EKpSPuJdfQRTEFyEQY66lD_549AUq6RcURZeZXHnofeV0twS6ijE3SFbAUGEV6oUWdaoyNiy-4tvGTzNxvx4DLK1CS3nNrgz3HeUyP00AUpLGlWE9u2iNT0xdUhQCzl9QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عقب التعرض الإرهابي على نقطة تابعة للحشد الشعبي.. طيران حربي يحلق في سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/89269" target="_blank">📅 04:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
عجلات الإسعاف تستمر في نقل جرحى الحشد الشعبي إلى مستشفى التون كوبري في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89268" target="_blank">📅 03:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead99d67d3.mp4?token=SN6JzGcum7XjqPflKOzPQvHtYLA6jdTh9CNxegKUku1HFHsjjdxdUinrXsQ8R9aa1OtQFoe8q07a5RiRj6mOYvFdnn2aOWo_d9HyMzYKq-ucdg3RlzaCH3WJTb0EInPMn9_CGRFh3g08dVKjbCX49JzNXOo0y5DhwpF9kv_7UrPmmVLkRgpniKNWwMm5X3y7KL__I5FGKQX08ohjHVByYQIFUFReXn6MD5W_oDRHadGXqUrgtsPvRQIp-jwsimc-br_LAu34F_xbXkOPhaqzbhtjMczQzM8LsRVY-d7HWtyhy7KxXizVd0tLPl5CMkMHPCNn5No1yZwqS5qGxFgNjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead99d67d3.mp4?token=SN6JzGcum7XjqPflKOzPQvHtYLA6jdTh9CNxegKUku1HFHsjjdxdUinrXsQ8R9aa1OtQFoe8q07a5RiRj6mOYvFdnn2aOWo_d9HyMzYKq-ucdg3RlzaCH3WJTb0EInPMn9_CGRFh3g08dVKjbCX49JzNXOo0y5DhwpF9kv_7UrPmmVLkRgpniKNWwMm5X3y7KL__I5FGKQX08ohjHVByYQIFUFReXn6MD5W_oDRHadGXqUrgtsPvRQIp-jwsimc-br_LAu34F_xbXkOPhaqzbhtjMczQzM8LsRVY-d7HWtyhy7KxXizVd0tLPl5CMkMHPCNn5No1yZwqS5qGxFgNjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عجلات الإسعاف تستمر في نقل جرحى الحشد الشعبي إلى مستشفى التون كوبري في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/89267" target="_blank">📅 03:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89265">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKvDtknWOzTZMLhAYyvdwMrFdFGa3iFAD17DbmPxzoS555eCtjPymJ_4r_dOwW71O0BpEmAEfXH-CflwFBUNO3ZjJGIPO_FtpPp0AU0tImVPw6IQ0NRRQ6c4Abdp0zGMEBlFrFaTdOhj94FqEN0JcmwUpzCI-BeWLHUwZXQ4-9zULvmUCAF5FLxf5BEUaWAGciHIfzRj0rypJWhaeJaCyu4qa9FpuRNxhQ0yiotX8FLVe853bBNCglET5Hj59d7IOZ29KesW8AAzeEobTOt7J_7oLNedD0JeGuTFgos7dgZhDKjCWi5Z2Zjk5fv5NHMb3dmqI-BqPwouB8vHFqiZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17c09a0ae.mp4?token=JoJJhrKPaknIIDORl3KfXR8CHtFIz2NgoBbCLAnK04a_EEefCkDxTbtI8onhMbY8gNyYQqwZxU8LUVmcC6d7B9bkEBgOXYZ282l7_9MOrVP9hThEWk4jZkc6WT2okWiDdSyFTclmiOY9XR7QYuYTQYMRGJ7oguDVGzVpg6myxWzUmMz78I8CmufZer2oWgsN9r6jl5HrNu81NlK98N3J3FGkEDp7u3LoTdFdJx9kxKlHJgigxaB4gRm12cTxr5oIZy98TIOhqDpW9EL4Zd6neidrX49tx1CAoqI1aSLB5IkvtlNholq9axNj6Xb_nIdgXMZmiCVV41EsS73I35Snag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17c09a0ae.mp4?token=JoJJhrKPaknIIDORl3KfXR8CHtFIz2NgoBbCLAnK04a_EEefCkDxTbtI8onhMbY8gNyYQqwZxU8LUVmcC6d7B9bkEBgOXYZ282l7_9MOrVP9hThEWk4jZkc6WT2okWiDdSyFTclmiOY9XR7QYuYTQYMRGJ7oguDVGzVpg6myxWzUmMz78I8CmufZer2oWgsN9r6jl5HrNu81NlK98N3J3FGkEDp7u3LoTdFdJx9kxKlHJgigxaB4gRm12cTxr5oIZy98TIOhqDpW9EL4Zd6neidrX49tx1CAoqI1aSLB5IkvtlNholq9axNj6Xb_nIdgXMZmiCVV41EsS73I35Snag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
نتيجة الهجوم الصاروخي الإيراني..
تظهر علامة احتراق محتملة على مدرج قاعدة الأمير الحسن الجوية في الأردن. ‏تستضيف القاعدة طائرات أمريكية بدون طيار من طراز MQ-4C تقوم بمهام استطلاع ومراقبة يومية قبالة سواحل إيران.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89265" target="_blank">📅 03:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89261">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pq9vHQa8cQQ4ZoN-BHTWjq7wUDiZdZOCViOs3C-pfxb7bw4DJ9bogVOFQQVTFcN3Y3PIUTQfAn-jUMKCEMtUnKfneADenYz_pTLBtpVCEYvL95wN5MiXmiGvYciTh5Vf9C-lKjK5YJur56tosSLOod69zTo24ZLaEfXpu-7SDkgOKrOivzo7DKqlz35nDgWRXnh1QxwZVE417lqFmqD0wpDZ8b2ameSQhjVAHOmW1DvYlQkA84kBAEm6gjChze0MovcbW_QsufqddEGomGuPht2AdK12h3ICM3EBzx_UukVRswQMab31SxLjV0kKoqscyOU3_PrnLSM5H6f-FyUk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jm2HssxvjOaDEKiqUeB73ftbbykH-x_W4DALh4xRRBQpEm3LYEu9tCKJ2kdc9rKFSoQjAwGw3Fy0Jo9zRfSkTh69vk-wYrz3r40p2olhAC7hDlF5piFaETk2XznHWWUQxD_Imu5xO_bC0ESxaT8yQAsWI-109Hf6YrceXyiwfUkpjKyu6jU36_WpZOtCt_OGjN1PfnuZK3efSbRZNNR-PO2ehQyAaqsTP7QFbKIMwJkBv31RrYaPAz2gKdC2PPAYR7-6R-OhE0dNYcur3qgXuJ2trcZjyQtdtIQz44A7zfW7FAbU-kxwFT4H1JeRlQN3LQil4NgJMa8fObNlzvNWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDQulRPx4SPppZfioijeo1z4oDD3y60JSO9zzHw7tQL1RCscHBNwMYH5l0T-JMRtYsrogLUtQR3kNU3EaaAy9npYgdlH_5CuOj94IN6LhkfOuuBUgfOxwsnP43k2kpnOmlYq-K3DbazFbibGIgURKgPDp531Hex5aPYBIB1h7RIGAx5YN9w5HjFQsjHErL3eiBwncN3D_cclXRwg1PqsBPRjZf1fBms8gdq-mAvFpp4dbVQ0rGUyko5YlqejhNMHcV6gg_C2P44n9q0fiv4BvCgLuS3r2RgG_opRQ4E6a4LRyuH19YZ4McxkglhvOAWTtXOZ4Qp8EPuL1WDjmiDNRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRvT4OioX22xcOC_2VdqOmbItXo90fqGiZ2B37qWnRSKoptNzR2ZTFboIUbHDnSx0Evn192_a27K2EwL-U7lgyuS6vPdHcduOr-RGrwwRjqfbtGk1ICKEOMxBB-0ZiQFzmpZ9if7C641_-E9QRq2ZiEdi8_M8Z1nH8FjjSTr7Ev51tcYJjyjU7D-8Yk_FgrY0GxD19FPheuDSQVAyKOVtXF9GGYXZaPwvu50IS6EtdxhQMJQhGKGifKCOyQ8EVq74Ri1h4GvcITPyMiy0gXSAtAaFTuk05t-mW7Z7gSSHY1UNO21JGyNIxyzFRBSw8mW3S-2yEeTSWwN9TY3DOBHIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
من مستشفى التون كوبري في محافظة كركوك.. شهيد وجريح كحصيلة أولية نتيجة تعرض على نقطة تابعة للحشد الشعبي.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89261" target="_blank">📅 03:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89260">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6a8d47d96.mp4?token=VS3UrfnLapFSQ_7vC8Fo2ACix0WvaCiCG6Vg_1lPiX12gO-4s60SjA-WdR_C3dfSVWYkP7fzosXwv2Tl1Nhq0LSw1_oe1PbUYZQKTNJ8Dimv7nkT4PIg7rx6w3npcw6W0YLljWCdD455xKiuGWWW8HOSeAhYbGPCLaa_nUC4cr7upniio7YZLbq5MN8HSaMM8KU91geQRGKEVLqo2gGg1D_CzrkXqEEfIy1oQbUulOJogCZrMbItCw6REBreHPd3rC_mJ3Lwey5iiXo_b8cVL_zzM9mhskLfIHp92Ty6a0JRpXjt6xDKNgzgdI1B7qiPGfj8TR6La0gSy8B4C7pUFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6a8d47d96.mp4?token=VS3UrfnLapFSQ_7vC8Fo2ACix0WvaCiCG6Vg_1lPiX12gO-4s60SjA-WdR_C3dfSVWYkP7fzosXwv2Tl1Nhq0LSw1_oe1PbUYZQKTNJ8Dimv7nkT4PIg7rx6w3npcw6W0YLljWCdD455xKiuGWWW8HOSeAhYbGPCLaa_nUC4cr7upniio7YZLbq5MN8HSaMM8KU91geQRGKEVLqo2gGg1D_CzrkXqEEfIy1oQbUulOJogCZrMbItCw6REBreHPd3rC_mJ3Lwey5iiXo_b8cVL_zzM9mhskLfIHp92Ty6a0JRpXjt6xDKNgzgdI1B7qiPGfj8TR6La0gSy8B4C7pUFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إصابة 2 من منتسبي الحشد الشعبي جراء إطلاق نار من قبل مجهولين تجاه نقطة في منطقة التون كوبري بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/89260" target="_blank">📅 03:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89259">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763cf4b10f.mp4?token=CDJG2k-2h-g1g4tGuKmjJdhf_qOSSUFyR6iA1ARhX3Bl3ATiXWJ8unMr6nDDP4jujKNYl9aG3E0hk1aW8GZ16I2gga9JT3UzPq8jpRToiHicPTy9Q9sglUnSjVRMJmmnCR3Zzwd-UYKlaxGs2Q71syjM_2QSHTeatkMYwVukMfbOa36KvOrLtLVeuaM0guv3l9psoex_Tck68NRYrHkqdLOcAq6ejgacXIQF1_5RbKqe7NUpOWzT1YOIwAZ_DYTEPh1qS4kSHCScPPLkejaTR7O16Eq9ouv9Up1EKl-xRBscNlcBwhsvdFBBDsxeOaBF_f9Y11RCLZY2MKU6iEv3IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763cf4b10f.mp4?token=CDJG2k-2h-g1g4tGuKmjJdhf_qOSSUFyR6iA1ARhX3Bl3ATiXWJ8unMr6nDDP4jujKNYl9aG3E0hk1aW8GZ16I2gga9JT3UzPq8jpRToiHicPTy9Q9sglUnSjVRMJmmnCR3Zzwd-UYKlaxGs2Q71syjM_2QSHTeatkMYwVukMfbOa36KvOrLtLVeuaM0guv3l9psoex_Tck68NRYrHkqdLOcAq6ejgacXIQF1_5RbKqe7NUpOWzT1YOIwAZ_DYTEPh1qS4kSHCScPPLkejaTR7O16Eq9ouv9Up1EKl-xRBscNlcBwhsvdFBBDsxeOaBF_f9Y11RCLZY2MKU6iEv3IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إصابة 2 من منتسبي الحشد الشعبي جراء إطلاق نار من قبل مجهولين تجاه نقطة في منطقة التون كوبري بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/89259" target="_blank">📅 03:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89258">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5e743d4eb.mp4?token=OKiZ44ANxXbOU8rQwNXRuZ5_69PrN4yObPAbEY-IiMeU2y36aw5L9444lfvzj1I9sK4te9MLb5Rrn4W16T32Blyw-FMqBtZpxz2My7f4sViQs1OeNW2LlCki2xMECDK6VrXwgCoFHeR-3x9twP7bnF5z4TFrfbaWHrBn-qpYlNh6pNHgvYQ_T3xMp66Bp6euy12TPn5x__hvNMUD3ITBRPrbn9Evpvs-fetoAU4jggUdU0L97w8HNLIz4-sIDu_XShLRsZ2m4eJ_ob7gVMoNldDWm9B3PogihdhyMviCpbW_2erUjySEyYUP1_zjxoApEHHbRBMeB9EkxkGZarOd2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5e743d4eb.mp4?token=OKiZ44ANxXbOU8rQwNXRuZ5_69PrN4yObPAbEY-IiMeU2y36aw5L9444lfvzj1I9sK4te9MLb5Rrn4W16T32Blyw-FMqBtZpxz2My7f4sViQs1OeNW2LlCki2xMECDK6VrXwgCoFHeR-3x9twP7bnF5z4TFrfbaWHrBn-qpYlNh6pNHgvYQ_T3xMp66Bp6euy12TPn5x__hvNMUD3ITBRPrbn9Evpvs-fetoAU4jggUdU0L97w8HNLIz4-sIDu_XShLRsZ2m4eJ_ob7gVMoNldDWm9B3PogihdhyMviCpbW_2erUjySEyYUP1_zjxoApEHHbRBMeB9EkxkGZarOd2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
توثيق لإطلاق صواريخ من قبل القوات اليمنية نحو مواقع مرتزقة السعودية في مدينة المخا.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/89258" target="_blank">📅 02:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89256">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da43261ac5.mp4?token=lwOBBzY3C2qQ5fmXGcWJyKz9A0P_tGpzlvMFkPtdgSixdC7BTBqTHDDP6pYzQXLIlenc6PBDVt0nJU9-cDJ1HHrjxcbbI8KCsxLWIKQETqeeM-4Akk7MbuV605ftOrDPWqMs4z_SZcLkPpZF8YcqaDpF_N57EODz7FhJEXHjfRbvCZimUv6SQzEPKP46KqPkk3OYN_qn52aj8TSs4pSCl5ERFmcrF4AMhGUrtw-RRB_1KW9B5E06WPLXHaO8gXCZPOufC62uTrNE5Oyl5VKg0sGS_J15v-xmrJBELmuFSVfPSze45uwOViVoeTNw2uLtWqIU9MbEgeKxEEp2gkiNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da43261ac5.mp4?token=lwOBBzY3C2qQ5fmXGcWJyKz9A0P_tGpzlvMFkPtdgSixdC7BTBqTHDDP6pYzQXLIlenc6PBDVt0nJU9-cDJ1HHrjxcbbI8KCsxLWIKQETqeeM-4Akk7MbuV605ftOrDPWqMs4z_SZcLkPpZF8YcqaDpF_N57EODz7FhJEXHjfRbvCZimUv6SQzEPKP46KqPkk3OYN_qn52aj8TSs4pSCl5ERFmcrF4AMhGUrtw-RRB_1KW9B5E06WPLXHaO8gXCZPOufC62uTrNE5Oyl5VKg0sGS_J15v-xmrJBELmuFSVfPSze45uwOViVoeTNw2uLtWqIU9MbEgeKxEEp2gkiNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
حادث إطلاق نار في ولاية مينيسوتا الأمريكية؛ مقتل وإصابة عدد من الأشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/89256" target="_blank">📅 02:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89255">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
🇮🇱
ترامب:
إسرائيل لا ينبغي أن تقلق. هل تعرفون السبب؟ لأنني الرئيس وسأعتني بإسرائيل.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89255" target="_blank">📅 01:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89254">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
سماع دوي إنفجارات مجهولة بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/89254" target="_blank">📅 01:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89253">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daWS3vBqpZtFXNxk8d8bayRgRvp799of4EYixd0mFr1mquJR3WcKq-NknPvxnR-e702chJIJfQvWRU0FRk8QrsQtVSW7kZnqb3pcZ639LuNYJpFHVgdL-ejNIn02PxqliDUwrpGjUxNwgztPbDfE6zEgu4cVcSMmzdA6-kjWdE8YU-gfw9gCJhsUvMe9KW71ONGPOiV3osDqvFcTMQ68EzLLUGVFNJ3f9dZMAgQxVpBII0HN1oMckmjlFWJq2kt3cnr_uqZcciAfJSDYhFD7kBHfTlre6DK27vsPdsIp9oKZDJAp6tX5ey1RCQw9utiBwms1F6_1mfABYHH4kkZ9mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: أعلنت خرائط أبل للتو أنها غيرت اسم بحيرة أونتاريو إلى بحيرة أمريكا، وبذلك أصبح هذا التغيير المهم للغاية في الأسماء، بين خرائط جوجل وخرائط أبل، كاملاً ومصدقاً عليه وملزماً. شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/89253" target="_blank">📅 23:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89252">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
تم إطلاق صافرات الإنذار في مستوطنة نيلى الواقعة في منطقة بنيامين. وذلك بناءً على معلومات استخباراتية حول وجود مقاوم في المنطقة، تم استدعاء العديد من القوات، بما في ذلك وحدة "دوبدبان" ووحدات الاستعداد المحلية.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/89252" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89251">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">المراسل: إذا كنت تريد أن يثور الشعب الإيراني، فهل سترسل وكالة المخابرات المركزية (CIA) لتزويد الإيرانيين بالأسلحة؟  ترامب: لا أريد أن أقول ذلك. لن يكون من المناسب أن أقول ذلك. أنا لست ضد ذلك.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/89251" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89250">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
🇸🇦
🇾🇪
بعد الحصار الايراني واليمني:
‏تراجعت صادرات النفط السعودية إلى أدنى مستوى لها في تسع سنوات، حيث تهدد هجمات على ناقلات النفط عملية التعافي.
‏بلغت صادرات النفط في البلاد حوالي 3 ملايين برميل يومياً في شهر أغسطس.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/89250" target="_blank">📅 21:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89249">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376c3a971.mp4?token=C0O-DmVa0IciLRKbegyNB4tk_Raw9n0Nx6Ca_xkw_QNt_8BfbeG7O_rBbaC7-M_2jpdOy5SHRwl7JOO1Zu6CEkSXnDmrhBISkR_SqDT7RxUsgQvtp_dmRaXYpA0649h8CiCXbZSBGWkrzD9ATr_SxohKOSrXb3c19fkNMxeCNVeC5gOqxudS6L-ustuyaRsA5sabGOOQjI2qHyeWzQnzNaR1ZmkJPLTCbpvieOBNu1Cb5eP9GnLlZHfzwOcae6rGjMG8Vay7cpM4oP-fIBFLADQIlaC9w5GFSfZZIq_BEqjy2GKM7LwJdc_AvXrtX6DqJWBGxSynjlkLKkbplwG6Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376c3a971.mp4?token=C0O-DmVa0IciLRKbegyNB4tk_Raw9n0Nx6Ca_xkw_QNt_8BfbeG7O_rBbaC7-M_2jpdOy5SHRwl7JOO1Zu6CEkSXnDmrhBISkR_SqDT7RxUsgQvtp_dmRaXYpA0649h8CiCXbZSBGWkrzD9ATr_SxohKOSrXb3c19fkNMxeCNVeC5gOqxudS6L-ustuyaRsA5sabGOOQjI2qHyeWzQnzNaR1ZmkJPLTCbpvieOBNu1Cb5eP9GnLlZHfzwOcae6rGjMG8Vay7cpM4oP-fIBFLADQIlaC9w5GFSfZZIq_BEqjy2GKM7LwJdc_AvXrtX6DqJWBGxSynjlkLKkbplwG6Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
‏ترامب يعيد ما قاله قبل ٨٠ يوما : السلطات الإيرانية تطلق النار بالرشاشات والقناصات على رؤوس المتظاهرين.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/89249" target="_blank">📅 21:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89248">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
🇺🇸
‏
ترامب يعيد ما قاله قبل ٨٠ يوما :
السلطات الإيرانية تطلق النار بالرشاشات والقناصات على رؤوس المتظاهرين.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/89248" target="_blank">📅 21:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89247">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">▫️
مسودة تقرير لوكالة الطاقة الذرية: لم نجر منذ فبراير  أي عملية تحقق بالمنشآت  الإيرانية المعلنة باستثناء بوشهر،فقدنا منذ يونيو 2025 القدرة على تتبع المخزون النووي المعلن بمنشآت شملها القصف.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/89247" target="_blank">📅 21:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89246">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">▫️
مسودة تقرير لوكالة الطاقة الذرية:
لم نجر منذ فبراير  أي عملية تحقق بالمنشآت  الإيرانية المعلنة باستثناء بوشهر،فقدنا منذ يونيو 2025 القدرة على تتبع المخزون النووي المعلن بمنشآت شملها القصف.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/89246" target="_blank">📅 21:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89245">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3Q6M9z0QcGu7s-YMfTVGppjtzYFW-HMlm9l6dqdlgLdYa2cuffB_wJXfcoEwGu4KDX0nktxLNvKWrPtF7hxr-5iEKwm7Vi7RWYdtJpXYDCJSkLfadT32JZQV-Cv7ci-Z84LOMdR5sK6cFO8ty6ItC8A73MgPF_DnmHUg-kyfW3e_rzjyaITewwYaQNzEcpdcZWWecHVBxlVMFMN1ppvDC77cRar59Ded2jGV6Y8yiwR6RPjwuESs_xJthSHAk43RF4l7dGVTwdCaNzRe8nzafPC6Ga0lfsFw-1ngCWjkl_jiiy_Xel-zQBp7MrjCmLd_RQM3PRvTEM8LAPzQYdH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
عثور على ثلاث عبوات ناسفة في وارشو عاصمة بولندا بالقرب من محطة سكة الحديد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/89245" target="_blank">📅 21:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89244">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇱
🇺🇸
الاعلام العبري: ‏
بعد الهجوم، وجهت الولايات المتحدة رسالة إلى طهران عبر قطر: إذا استمرت إيران في التصعيد، فإن واشنطن مستعدة للانتقال من ضرب الأهداف العسكرية إلى ضرب البنية التحتية للطاقة والنفط.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89244" target="_blank">📅 20:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89243">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
🇮🇷
المتحدث باسم الأمين العام للأمم المتحدة:
أعرب الأمين العام عن قلقه إزاء التقارير التي تفيد بوقوع ضحايا جراء الهجمات الأمريكية على إيران.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/89243" target="_blank">📅 20:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89242">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇱
‏
نتنياهو
:سنطيح بالنظام في إيران - سيسقط. جميع أنظمتنا تعمل على إسقاط النظام، إذا هاجمونا، فسيكون هذا الهجوم الأخير لهم.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89242" target="_blank">📅 20:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89241">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqW1egbhjQaIaxcxGkWsYazLsnouztJSvAglgyqvh1pwD3WG7Cq92op5-A_AFGpz9PreqhFPlSKBDlbEDr1wKueiQAmHP5OIn6vhkrzNEFziEdZdEEQkK8LATE0CVO3MmDFqExycMhEnW62Cz0N2WdmUWVyEFugHT_6sfNTdlOvBOblLcjluGzrxxbdtTGHS9RZnqaD3baxl-bnZZ7O7_q71R3OnYMrJbCjZVCkUUCv1ELhM00eqLqTjsQw4F3GT66fl9kBfhwGXXqqKNeFo-2ah2W7ti9jehzWlcykCz4jUcpASPvRHzgNhMciSUcmxgCwclyz3sSvHRsyyWAMWOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇸🇾
بعد 18 عامًا، تتبنى إسرائيل مسؤولية اغتيال الجنرال محمد سليمان عام 2008، وهو المستشار الأمني المقرب والأعلى رتبة لرئيس سوريا.
وصلت فرقة من القوات البحرية الخاصة عن طريق البحر وأطلقت عليه النار من مسافة قريبة، ثم اختفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/89241" target="_blank">📅 20:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89240">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq9ZJThxJ2gu-yfgcSBCB4whDOc-w8DLXXXnlIYsYquqntce3gH8m4aPUVanQOWx1vR6Iqwu66PHo_nthmbQn1iTN4QSY3NlfQwHnj2IEbOWq-O576LYTPMd3o8Yl5wBSsDfZr8W6Yuhl-NYP5LemYQBLsyuewHxVm-Tjf_a34aApah2zwWFlXv5-HUde0ZIexfhUalMB0sfYMdviIUTMWIBvuhOFFfrg-1LZtGa00nPG7wbZzPGMwQJ9Q1EQWIrH-hhzDzgAYpWt_2Y-45vmtuiXZO8HNjC9tkFnVemK8i_SAG1T05Ujm472mR1s6yQ43GhZjy_wXu1GKxuCR6OKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الشيخ اكرم الكعبي:
إن بقي جندي واحد بعد تاريخ ٩/٣٠ فلن نتركه يعود سالماً وسترسله إليهم جثة هامدة.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/89240" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89239">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇹🇷
🇮🇱
اعلام العدو عن مسؤول إسرائيلي رفيع:
لا نعتبر تركيا عدوًا إنما خصم بعد خطواتها في السنوات الأخيرة</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/89239" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89238">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي ماركو روبيو:
لا ينبغي لأي دولة أن تساعد إيران في التحايل على العقوبات. ولا ينبغي لأي دولة أن تساهم في إيجاد آليات تمكنها من تحقيق إيرادات تستخدمها لتمويل الإرهاب ومحاولة بناء سلاح نووي. وإذا قررت الدول القيام بذلك، فسيتعين علينا فرض عقوبات عليها أيضًا.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89238" target="_blank">📅 19:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89237">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGAsrdGJFvaC7hEqT5s2u6JmSSCViT7jlr-QbGdbV_MGFWSVvjW6E0Lg7E3Tbbn_Tbn1sYNSseULS5Jl6ryHNbaUZvIPpIiOH42X_Et0Hoz8rp0IV0wk0_aiYblyEBCbv01JZubBbOVuB9BXQgUZsLnaYUy9-fJjfxUGrwFrcg0Pq_q6HCQdtub5cbqWZu4p6d0nF9gHgr3ZIohKIBaU5QL70CKQzDc-P5iZgJSFlOoyyRNUcHkQ3s7EJ8hDLsC13Vd7tVHNUIhCKu61YhxTgDq_5A-GJ-a96waXNAXF062PAfd1_LFw3s1KZrRQMq_jshCmzcmX4q7Q5gYwsOj-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🇺🇸
‏
ترامب:
الآن وقد أصبح مضيق هرمز تحت سيطرة الولايات المتحدة، هل نغير اسمه إلى مضيق ترامب؟ مثل أمريكا نفسها، سيصبح الوضع أكثر سخونة من أي وقت مضى!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89237" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89236">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/89236" target="_blank">📅 18:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89235">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89235" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89234">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
إذا امتلكت إيران سلاحا نوويا حينها سيُدمر نصف العالم.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/89234" target="_blank">📅 18:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89233">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
ارتفاع صادرات العراق من النفط الخام إلى 2.340 مليون برميل يوميا وهو ما يعادل 71% من الصادرات النفطية قبل اغلاق المضيق.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/89233" target="_blank">📅 18:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89232">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e648c65e.mp4?token=X3QM17eskcrmf97tbIP5Ir-D75NY5wWj3N7akMl1a5_B1X-5W_2l0PePIYeXAOu2mKD9y9LiZMuBLmzrLMDs7fD0cO0Zex2NMV6NiCCNnc_KuvN8hZuSdkymF1__rvZcmjgRSdUuftrdyi2MOwU6jkzQApH3GmD8GUUSvYVTnqmSsqh4DhbEYtaU6ebv2r3uOrONrS1rvINcaH4FxThQ1iid5oCKNDKGZkraLAdmEWmM1QdatMXJ695W-M2MwQWZhrH2yVuynJCO-htmOZHGzS28bglITrHfHTOFkqYMsGDJvHg2_gn-67TQoGZRb63gvfeahYxXcZcVYpCz9fXfXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e648c65e.mp4?token=X3QM17eskcrmf97tbIP5Ir-D75NY5wWj3N7akMl1a5_B1X-5W_2l0PePIYeXAOu2mKD9y9LiZMuBLmzrLMDs7fD0cO0Zex2NMV6NiCCNnc_KuvN8hZuSdkymF1__rvZcmjgRSdUuftrdyi2MOwU6jkzQApH3GmD8GUUSvYVTnqmSsqh4DhbEYtaU6ebv2r3uOrONrS1rvINcaH4FxThQ1iid5oCKNDKGZkraLAdmEWmM1QdatMXJ695W-M2MwQWZhrH2yVuynJCO-htmOZHGzS28bglITrHfHTOFkqYMsGDJvHg2_gn-67TQoGZRb63gvfeahYxXcZcVYpCz9fXfXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاقمار الصناعية تظهر منطقة متفحمة واسعة في مجمع عسكري أمريكي بجوار مطار أربيل الدولي في اقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89232" target="_blank">📅 18:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89230">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOU-XfJjLwjLa3XZWobI-RmQ2Vo-zg5PJOjGxPAObvtOazhrHcHKO6Wq957a29rnkYWZ-nBgva2gEh2KMBd_Ec6PFvVU0dFXsmNEjySv1Qp-oMxx-ETSFsnrz-LISDjCZD0oMBghykUPf-HT6f0HJ3WGtiBeSvT4g7iJ60Gx799BpkThpm8CNCXd1XmevRQ2c5MgFvi2v-RPiWfkDGquvaLwJI5j0CJIT-ybKvUCiM7Hlpmi5al5JQpgbb75t5A_XY4RS_9VHw99q_r-fWJEPgzkDbOtAZD6I3FO8R515EfKk6CY06j9qFK3ga5Z4OjIJ38eHj2nW4p075U3hKnp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNzpBSVMd8VWBg2OjxxsYEGidW_kwxze4z15sH8v0pcIPNfH98lhWcUlHSp0IlYmUyBJirkXUQTG7F-mqWnWPkkx20TSd7AqX-KFSBqrnH2DHq-hEVuZWczUuyWsNNl4R9csqhEMHX1gQaH2o7YmK8yLpsujZpY4zFUrr_1uFmxrve415e4tYxiLsYss4QYtB2lkADzc6407JjEinA3Dbt2iE8yzgEd33K9r3Kgp5vbJwESlauUeoXa3K10vYiPpos43Q3xdPASCpkpdV1riS1os5SJCw4lWYb5_s7DHo6VKOCOh2K0r5FRlF4fZl4SrhTt-5R-6dv8Rpsnb00VTVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اشتباكات مسلحة داخل العاصمة الاوكرانية كييف بين منتسبي الاجهزة الامنية في البلاد
مكتب المدعي العام الاوكراني وجهاز امن أوكرانيا اتهم جهاز الاستخبارات العامة بالعمل السري لصالح روسيا وجهاز الامن الفدرالي الروسي
وشنوا الهجوم على جهاز الاستخبارات العامة وحسب المصادر عدد القتلى حاليا عند جهاز الاستخبارات وصل ٣ اشخاص للخطة الجارية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/89230" target="_blank">📅 17:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89229">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حدث امني في مضيق هرمز: استهداف ناقلة نفط وإصابة شخصين كحصيلة اولية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89229" target="_blank">📅 17:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89228">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
حرس الحدود الإيراني يصادر سفينة تحمل 382 ألف لتر من الوقود المهرب في شمال الخليج، ويحتجز 11 مشتبهاً أجنبياً.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89228" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89227">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الوكالة الذرية:
لا نعرف الوضع الدقيق لمحطة أصفهان للتخصيب ولم نجر أي تحقق ميداني في أي منشأة نووية بإيران منذ فبراير</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89227" target="_blank">📅 17:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89226">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EztROBZcippasCcZZxX8jUIr6cJWBx1LQdZ30zJlEBNJBVDhxpQAmPHgPe7mOLGkmKnk1yrIAqGsL_wMYyynwp8_95TtPqlR_i6gTMtPCv3OTpiO8lYxSevkDNBx2N6V12HGb6Gne9g01A_DyyrIXVcMAEVJnkwyhTbCxcDHXwJoPwmqnWu29m6A1iZ5Mjr-Vb6oRJxUpA6HsWiKXp5IdN2k50J3dNFipmwI-imY3vRoHZDwDxSLrYJ8THnl9_-mgfvuHIGWTSnxy448FRwBJOJCpsCLzYrrWeDuzRudO7eM85ceV2j56UUlaKrDH5CCb68roqJeFv2CGlXnCFP8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الايرانية:
يزعم تيم هوكينز، المتحدث باسم القيادة المركزية الأمريكية، - بينما ينكر جريمة الحرب الوحشية في ‌سيريك - أن الولايات المتحدة لا تستهدف المدنيين!
‏يبدو أنه نسي سجله العسكري: كاكاراك في عام 2002، وموكاراديب في عام 2004، وديه بالا وويتش باغتو في عام 2008 - وهي هجمات أمريكية موثقة في أفغانستان والعراق أسفرت عن مقتل مدنيين، بمن فيهم نساء وأطفال.
‏لقد نسي شيئًا آخر أيضًا: حتى مسلسل Homeland، وهو مسلسل تلفزيوني أمريكي الإنتاج، صور في موسمه الرابع غارة أمريكية بطائرة مسيرة على حفل زفاف في باكستان - وهو هجوم أسفر عن مقتل حوالي 40 مدنيًا.
‏إن الحقيقة مروعة لدرجة أن الدعاية الأمريكية نفسها لم تجرؤ قط على طرح الادعاء الذي يطرحه هوكينز اليوم.
‏سيريك ليس مجرد قصة. المدنيون حقيقيون. الضحايا حقيقيون.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/89226" target="_blank">📅 17:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89225">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j298V817tQioRjH_2TEfnFot5ryRMyaylGlbCISxL3wLHMKuWFQ5xZp1B1ds6LBfXi2qq81UISxcYdRQU5k3qZtr94IpGfRKWDRy6RSzqQF2JtdlyExAT9Oz7vtEbnO6-TqVXCavbJnTxgJ20mA50rN8KJ8fD1GgEODS8K_H5Ka4XKb_G4DRBMDdV-nW8WPcO3WrxhqIgaNL_cTUwYzmQxjty6OLTtC7Ar7v8xFPtEUghkh0-kphucov98-cfjqkcIkzRNGdXFRpLW10wtHNQ2jjjAEtRrDMGFsdWzGDoAd9a9ptjQbJAOEF4MpRzqKqsQy2JTKPWDoeRgVxWCDcFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
الجمهورية الاسلامية الايرانية تكلف مصطفى طرفي قنصلا للجمهورية في محافظة البصرة العراقية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89225" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89224">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6900ea796b.mp4?token=V5WQUftawhkNJbmbseylVbiX9mfOtpGquGSJK5P5XYqC9HknjUSywb6vcCkQHyBYSrCZlbJ-aRY_5WqyqIcaHI9OyxQ63NJvzYv7crJPqMRXGQ6uYTulfhBnXn3lhe_rjs6r-CRpPhwQoLzzENGc_ykbkqivOSjuhn_N3OuYWEEGmNuT3rQA3JSCriui3hGzTsKXeHVcCdbFVZ7r6r11qlnB-aIwcpoaxYyxJ4saNGWFbQmSHL4uRyRPcysHODGZqDS4P2JA_fWi-t8k3ooB0_5F6R-sJN-XdmbVSVjnuAYRQZgDCg508Vg_L_NFIxHnwLnGqNpp4bT-1G7UXnVgSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6900ea796b.mp4?token=V5WQUftawhkNJbmbseylVbiX9mfOtpGquGSJK5P5XYqC9HknjUSywb6vcCkQHyBYSrCZlbJ-aRY_5WqyqIcaHI9OyxQ63NJvzYv7crJPqMRXGQ6uYTulfhBnXn3lhe_rjs6r-CRpPhwQoLzzENGc_ykbkqivOSjuhn_N3OuYWEEGmNuT3rQA3JSCriui3hGzTsKXeHVcCdbFVZ7r6r11qlnB-aIwcpoaxYyxJ4saNGWFbQmSHL4uRyRPcysHODGZqDS4P2JA_fWi-t8k3ooB0_5F6R-sJN-XdmbVSVjnuAYRQZgDCg508Vg_L_NFIxHnwLnGqNpp4bT-1G7UXnVgSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89224" target="_blank">📅 16:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89223">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89223" target="_blank">📅 16:41 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
