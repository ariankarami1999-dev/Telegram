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
<img src="https://cdn4.telesco.pe/file/aXLDrCXDXLMt8kjygfAojd2LN9q9lfAMvhxzhYmsGKhTXzrPbOcLFEo5eyxUqzVhzCHDHHZTbU_A1JSyZl5D58jgZ2HPnmWJh1UhXgGk_rICgk5eiO_3w3U1pfwhU_SsWIczn4FvvIqWyKGnyNM1eDnsqmtmwDWTKrZ7crv2az3wkH1RFBRpDj8UAOSbEdQPx3Z3fx8LytkqfHvmPPQhixd4hWXRaJNnobn6Uubmm8KJrS-wsoSzNZXB3hiA1IE7DlutvBBLwWX3aeplBY6aDtQUPfhshEVUGI4qLw8DJV8hrvgIwDwfK8JsTlKLNFkuR5zshNVw2_3jIRu5SP1CKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-89702">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
رويترز
: غواصة مسيرة عسكرية أمريكية تعطلت في الشرق الأوسط قبل أكثر من يوم.</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/naya_foriraq/89702" target="_blank">📅 21:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89701">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a28XyA7t7w5Bpj9e_HvHDww_LsjxErcLLSPhL_tJOkK1Q13ZK4ldjp4RIwkyqnzAaUq71BVD8c_Xu5paoLObDcdEcMKlXFHyUr8mtoXVW6_SBs7S2Pdj4u5INu1XMheYHxnaD3A6j8DaRht48HQUMvSFmBDyEGuz7gRAxyNYhEwsmpHfFMjis8bNlzyJ3oPFAhxhuQ4mv3Qjd6s8eMhkWXQfoukLMzVrnn_UDwMTNGZ4tFjcnMNtrILscMZ8ISJnseXmhvTsX0BIB3eTZYxqE1v0upRZ38AEXr1AnitQeRymfCxkIaVcQ85qV7aerV1emyazUJC5m-7wfPULgZAaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
مساجد مدينتي جيزان وأبها تبدأ بالتكبير، عقب مشاهدة الصواريخ اليمنية في سمائهما وهي تتجه نحو أهداف غير مدنية.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/naya_foriraq/89701" target="_blank">📅 21:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89700">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9e91d4ed0.mp4?token=i445VCRYc8TNUQXqjPOCM8zmmzDns9J2yQQP0VwzUgA5QzGOIkHj4g1RQH7kEmFwpPPnlqap8vvYDFqW7Qh1Q5bRZSrSE0287_90So1TPYsR8L9gI9DicDtvJ-hjN_cPSN7vGjZI2L-zXc8T8TujKvCG6uwxfnRsfyjLBIXQoK_-EuhIkXSKfDKNEzzCHdjBz8Yu4bNMG1PNtPj90ncSNknbIiKCVmLf2emKJe8LlEoQK93_dwrE_quNV6sD5zK5q9cwb-O-LO06l5J4wfot2qA98cmzJnFOJYh30wodCjl9XVFgN6U3CpdXuMu56lc6sPPSsE6hr-71I_AYzsj55w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9e91d4ed0.mp4?token=i445VCRYc8TNUQXqjPOCM8zmmzDns9J2yQQP0VwzUgA5QzGOIkHj4g1RQH7kEmFwpPPnlqap8vvYDFqW7Qh1Q5bRZSrSE0287_90So1TPYsR8L9gI9DicDtvJ-hjN_cPSN7vGjZI2L-zXc8T8TujKvCG6uwxfnRsfyjLBIXQoK_-EuhIkXSKfDKNEzzCHdjBz8Yu4bNMG1PNtPj90ncSNknbIiKCVmLf2emKJe8LlEoQK93_dwrE_quNV6sD5zK5q9cwb-O-LO06l5J4wfot2qA98cmzJnFOJYh30wodCjl9XVFgN6U3CpdXuMu56lc6sPPSsE6hr-71I_AYzsj55w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/naya_foriraq/89700" target="_blank">📅 21:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8003399351.mp4?token=PvVux4GWia8B1b5SkdLh2GUIz4DYFAY_giszu4pwTKiHReSNFW-QWAXDg8KyQN1HjBqkF73a26PF0o-Qkggz8cpcRjCepOeviUFL7Xmhwx7XtDml_0DHZ4hyvTiIr4fJury-F_JEV2NWxs_Ln4qIYS03MVaYWS370ddYG0OCfN37UihoCO0W2eTL-2niXr1IFWcuAbOmY8K4AfvPMvjHQYHpimnzuYVE2JZifV6-00SVjhvWt5n91f4fVqYSHi0q-yOFk_KqQujskPwHh_UwSF74qf7RIotdHKq88Bre75PfqmDRdIvud4V2eYJcQPhXgTCJOYmMTjrNZEmPbFVWIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8003399351.mp4?token=PvVux4GWia8B1b5SkdLh2GUIz4DYFAY_giszu4pwTKiHReSNFW-QWAXDg8KyQN1HjBqkF73a26PF0o-Qkggz8cpcRjCepOeviUFL7Xmhwx7XtDml_0DHZ4hyvTiIr4fJury-F_JEV2NWxs_Ln4qIYS03MVaYWS370ddYG0OCfN37UihoCO0W2eTL-2niXr1IFWcuAbOmY8K4AfvPMvjHQYHpimnzuYVE2JZifV6-00SVjhvWt5n91f4fVqYSHi0q-yOFk_KqQujskPwHh_UwSF74qf7RIotdHKq88Bre75PfqmDRdIvud4V2eYJcQPhXgTCJOYmMTjrNZEmPbFVWIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرس الثورة: تم اعتراض وتدمير طائرة مسيرة متطورة من طراز MQ1 بواسطة نظام دفاع جوي متطور تابع لحرس الثورة الإسلامية، وذلك تحت سيطرة الشبكة الموحدة للدفاع الجوي في البلاد، فوق سماء مضيق هرمز.</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/89698" target="_blank">📅 20:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89697">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5X1dOdexDi_Z1m_h7DIhnevhiNidIiMRD3VsGRAmAO7U8z_f3vs68mVXcjvDUV2qcwGpQgAbas7kqrEq5i_-wRlDE_JqvkFiByowut3fbpUESiZWE_xsKMQXA9h4JMGwEBxEBkYcYS9iqdXWdkjpSgpzTpBgbYycgHsEH9d1cmokSCKfC1gv-424zRJzW3NFs0EQovLzyUOb-AXxGO9DcnIdIB6XKOznqs1T6i6Vealu0bgQbBtvzXGcU24N626SzNLukxtgzLd8i4Gq9n4EKWcVBubnzWD-3BstkKUtb6L0h-b8Q-vLKhKK_HZD_RkSMBzURJBN1qPkS8ELop_8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصابات مباشرة في منشاة نفطية بنجران جنوبي السعودية</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/89697" target="_blank">📅 20:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هجوم صاروخي واسع لرجال أبوجبريل على أهداف في العمق السعودي.</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/naya_foriraq/89696" target="_blank">📅 20:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89695">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اصابات مباشرة في منشاة نفطية بنجران جنوبي السعودية</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/89695" target="_blank">📅 20:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/89694" target="_blank">📅 20:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89693">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجارات ضخمة تهز نجران</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/89693" target="_blank">📅 20:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/89692" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/naya_foriraq/89692" target="_blank">📅 20:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منشات نفطية في مدن جنوب السعودية تتعرض لقصف صاروخي يمني واعمدة النيران والدخان تتصاعد منها.</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/89691" target="_blank">📅 20:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات متتالية تطال ابها</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/naya_foriraq/89690" target="_blank">📅 20:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89689">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/naya_foriraq/89689" target="_blank">📅 20:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89688">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/naya_foriraq/89688" target="_blank">📅 20:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89687">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/naya_foriraq/89687" target="_blank">📅 20:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89686">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZ4oO00_6bplS-LX0qCG3FWqaXN1d5W6qoMq6s5-6D3xG3tdjks-wvogc6DdLGR0eWUzFwhsTkphY9SzxLuVXCn50hg1--C2iZB_3yNaKa-d7d7H6iKOarRjKrvLTG-eFob0Su_oe87rz1mT9qIcM9-zoUX8S1LB2aqsS-HduHm1fi9QAHLl53kqmxz3plgiOHjKUUZaZqKjNZqrV4wAfBNBbFOWXZcAx2ePd-qnb1rUSw6T_KRkcWify4ksIVMo73HtDwa95zRUuEF-ZZiOT6kWL-EahefoQ3WVuSOyAsN6qZs3SRS59IMYxR6jirH1ffaGvd4KqsrfYhDkfF-AFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏توقف العمليات الجوية في مطار أبها الدولي جنوب السعودية لاسباب غير معروفة  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/89686" target="_blank">📅 20:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89685">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇱
🇮🇷
‏
نتنياهو
: علينا إكمال المهمة وإسقاط النظام الإيراني</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/89685" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89684">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🇮🇷
🇺🇸
بازداشت یک تبعه ایرانی در نزدیکی سفارت آمریکا در بغداد
یک شهروند ایرانی که قصد داشت با عبور از ایست بازرسی «بابِلون» خود را به مقابل سفارت آمریکا در بغداد رسانده و تجمع اعتراضی برگزار کند، توسط نیروهای امنیتی سفارت بازداشت شد.
این فرد پس از حدود دو ساعت، با حضور فرمانده لشکر به شعبه اطلاعات تحویل داده شد.
@Naya_Press</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/89684" target="_blank">📅 19:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89683">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
انفجارات جديدة تهز مضيق هرمز.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/89683" target="_blank">📅 19:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89682">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
الدفاعات الجوية التابعة للجيش الإيراني تتمكن من إستهداف وإسقاط مسيرة أمريكية من طراز MQ1 في أجواء مضيق هرمز جنوبي إيران.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/89682" target="_blank">📅 19:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89681">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي ‏روبيو:
إيران تقف وراء الأحداث في اليمن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/89681" target="_blank">📅 19:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89680">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇾🇪
🇾🇪
عضو المكتب السياسي لحركة أنصار الله محمد البخيتي: سنرد على كل حماقة سعودية في اليمن بقصف العصب الاقتصادي والأصول العسكرية للمملكة واستمرار الحرب بالداخل سيؤدي لخسارة سعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/89680" target="_blank">📅 19:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89679">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇾🇪
🇾🇪
عضو المكتب السياسي لحركة أنصار الله محمد البخيتي:
سنرد على كل حماقة سعودية في اليمن بقصف العصب الاقتصادي والأصول العسكرية للمملكة واستمرار الحرب بالداخل سيؤدي لخسارة سعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/89679" target="_blank">📅 18:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89678">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
القيادي في انصار الله عبدالملك العجري:
- قابلت السعودية كل جهود السلام لانهاء آثار الحصار الشامل  والغاشم على الأوضاع  المعيشية والإنسانية بالتعنت والمماطلة الأمر الذي اضطر  السلطات الوطنية في صنعاء لاتخاذ بعض الخطوات التصعيدية لإقناع السعودية بتغيير سلوكها العدواني تجاه شعبنا اليمني وحقوقه المشروعة
- إن محاولة ترهيب الأطراف الدولية من خطورة ما تقوم به القوات المسلحة على باب المندب مغالطة مكشوفة فالأهداف معلنة أنها حصرا ضد من يفرض الحصار الغاشم على بلدنا والمجتمع الدولي على دراية أن يقوم به اليمن هو في إطار حقه المشروع للدفاع عن نفسه ولا يستهدف احدا الا من اعتدي عليه
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/89678" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89677">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇸🇦
شركة سوار أطلس المتخصصة في صور الأقمار الصناعية: حرائق هائلة في محطة ‌أبها⁩ لتخزين الوقود ومصفاة جيزان⁩ التابعتين لشركة ارامكو.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89677" target="_blank">📅 18:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89676">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
🌟
بدأ كلمة لترامب سيقول فيها تم تدمير البحرية الايرانية بالتزامن مع الاستيلاء على احدث غواصاته في مضيق هرمز.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/89676" target="_blank">📅 18:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89675">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حرس الثورة يسيطر على غواصة امريكية حديثة في مضيق هرمز</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/89675" target="_blank">📅 18:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89674">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/89674" target="_blank">📅 18:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89673">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بحرية حرس الثورة الاسلامية:  بفضل الله تعالى، تمكن مقاتلو البحرية التابعة للحرس الثوري الإسلامي من نصب كمين لإحدى أحدث الغواصات الذكية التابعة للجيش الإرهابي الأمريكي عند مدخل مضيق هرمز، وذلك في عملية استخباراتية وعملياتية معقدة فجر اليوم. كانت هذه الغواصة…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/89673" target="_blank">📅 18:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89672">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني: في غضون دقائق، سيتم نشر خبر هام حول عملية استهداف مقاتلي القوة البحرية التابعة لحرس الثورة الإسلامية في مضيق هرمز.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/89672" target="_blank">📅 18:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89671">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
‏
وزير خارجية الكيان:
طرد الممثلين البريطانيين من قاعدة كريات غات ومنع 12 نائبا ومواطنا بريطانيا من دخول الكيان وإغلاق القنصلية البريطانية في القدس.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89671" target="_blank">📅 18:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
في غضون دقائق، سيتم نشر خبر هام حول عملية استهداف مقاتلي القوة البحرية التابعة لحرس الثورة الإسلامية في مضيق هرمز.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/89670" target="_blank">📅 17:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89669">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇸🇦
‏توقف العمليات الجوية في مطار أبها الدولي جنوب السعودية لاسباب غير معروفة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89669" target="_blank">📅 17:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇷🇺
الكرملين:
نهاية الحرب ستفتح على الفور آفاقًا هائلة لإعادة العلاقات بين الولايات المتحدة وروسيا، ترامب يرغب في إعادة العلاقات بين الولايات المتحدة وروسيا خلال فترة رئاسته وبوتين يدعم فكرة إعادة العلاقات بين الولايات المتحدة وروسيا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/89668" target="_blank">📅 17:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89667">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
‏الولايات المتحدة تفرض عقوبات جديدة متعلقة بإيران.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/89667" target="_blank">📅 17:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
🇾🇪
القيادي في انصار الله عبدالملك العجري:
‏الاعزاء الجولانيين في سوريا الشقيقة الذين تزيوا بالزي اليمني واعتمروا العمامة اليمنية واحتزموا الخنجر الحميري, ان هذا الزي ماركة للعزة والبأس اليمنيين وبما انكم فعلتم ما فعلتم فعليكم ان تتوجهوا فورا لتحرير اراضيكم المحتلة والا فإنكم تسيئون للعمامة اليمانية والخنجر الحميري.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/89666" target="_blank">📅 17:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89665">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
‏الولايات المتحدة تفرض عقوبات جديدة متعلقة بإيران.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/89665" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89664">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
انفجارات تهز مضيق هرمز.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/89664" target="_blank">📅 17:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89663">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
‏
وزير الدفاع الألماني:
برلين سترسل صواريخ للدفاع الجوي بصورة عاجلة إلى أوكرانيا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/89663" target="_blank">📅 17:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89662">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uohuhSMp6ckRD3cW7G5XgWUaYdv5aqGUdfZvdS7HUsFM8jyofQtALFMQMrSdz_JoUeF4ZLjg07Qn1WCKAlTcNgUP3tKAe1zWpu8QRemyJOU9q2RKElC86ovWVVwGk8h_YU-DOYcX-6A9IvFFYiWhwRwQV5JkbTfrQwVnUQy05fSJpzUdSfTwGVXnU7ICEJUsanHIZZm8GwBx69_SZdoD598WwsygGIlGv2RK2trVGyleAe6QyY5xpnE_LGPE5SL6rMi3OEx2Yo-fDURhh9jUPPfav5pWLQcKG9clhQ8E6SkPd6yUIhKa5RgoBqQCKaWiHWDeL1ZUrvNfs7jJqBsD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية تقرر إيقاف برنامج صوت الشعب لمدة 90 يوم ومنع ظهور مقدمة البرنامج مروة هاشم لنفس المدة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/89662" target="_blank">📅 16:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89661">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/89661" target="_blank">📅 16:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89660">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89660" target="_blank">📅 16:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89659">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇾🇪
🇾🇪
بعد تطهير اليتمة مقاتلي انصار الله يجددون بيعتهم للقائد الحوثي: نحن بجانبك صفا الى صف ونحن جنودك بر وبحر وجو.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/89659" target="_blank">📅 15:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89658">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44712ad80c.mp4?token=l_gjwtYHvLAKwpb2UBqQp9zqvP4jWbsUZj6MFeIjeptWMwFwx1cF6bjNCgSxwiDEPfDHqB3H9qyIGkoDIeS5XGL1Ii6WXJ41f6jZqKX2C-dzAa1roX9g1HEPP8bf0QqOWRJKFFHTIDCpQXLp2hCDvbeFiBW8nsi7pz3FLq1POBY3uVFBQkxYlp4alEeli5PHccTcdF27-auvvpzkQrrTWyKmjXijmHK4H7t1ML3M-_3RQvQ2WqD9qRJQDKifdEcg5pWMef2SuAFDNkrcGemG8eHESYoyDxW5whtoTBn4A9nJ2YOPGor6BKBsj-HSJhIYhgTIg3f5gB8ISx6vgpDExw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44712ad80c.mp4?token=l_gjwtYHvLAKwpb2UBqQp9zqvP4jWbsUZj6MFeIjeptWMwFwx1cF6bjNCgSxwiDEPfDHqB3H9qyIGkoDIeS5XGL1Ii6WXJ41f6jZqKX2C-dzAa1roX9g1HEPP8bf0QqOWRJKFFHTIDCpQXLp2hCDvbeFiBW8nsi7pz3FLq1POBY3uVFBQkxYlp4alEeli5PHccTcdF27-auvvpzkQrrTWyKmjXijmHK4H7t1ML3M-_3RQvQ2WqD9qRJQDKifdEcg5pWMef2SuAFDNkrcGemG8eHESYoyDxW5whtoTBn4A9nJ2YOPGor6BKBsj-HSJhIYhgTIg3f5gB8ISx6vgpDExw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تطهر سوق اليتمة من سحالي بن سلمان وتأسر العشرات منهم  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89658" target="_blank">📅 15:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89656">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">القوات المسلحة اليمنية تطهر سوق اليتمة من سحالي بن سلمان وتأسر العشرات منهم  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/89656" target="_blank">📅 14:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89655">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a0a7665.mp4?token=j_xGWvfVoEy5xZmeVVgCpYXQU9kHs0n4i_2LvY728iCfSvni172wATY09jYoMmRsQguarBniii-0m6lTDkfGoMALNVmWrE42uV_-LWQ2fiKPAlTLvpKLm4gCAc63_VOTR93dUbvAEYCOnTj6C2TcpPmvlKGYjJzUIfyfPhinrijCc0sPrhfKF1Qbr6zGEjYOIpKpPmE5rALYo-ksIWz-74wjKvlytG-oznYVq0yLd_w6nMdIqJ3vG7hqj9ALzM9wmOdPiV2yFWNrzwEqTtuwZkXw3iim0jYl06EQpG58Lop4P2MTegabJtUe4P6ncLzPLjVTc78jG2fSSXHUkuD5lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a0a7665.mp4?token=j_xGWvfVoEy5xZmeVVgCpYXQU9kHs0n4i_2LvY728iCfSvni172wATY09jYoMmRsQguarBniii-0m6lTDkfGoMALNVmWrE42uV_-LWQ2fiKPAlTLvpKLm4gCAc63_VOTR93dUbvAEYCOnTj6C2TcpPmvlKGYjJzUIfyfPhinrijCc0sPrhfKF1Qbr6zGEjYOIpKpPmE5rALYo-ksIWz-74wjKvlytG-oznYVq0yLd_w6nMdIqJ3vG7hqj9ALzM9wmOdPiV2yFWNrzwEqTtuwZkXw3iim0jYl06EQpG58Lop4P2MTegabJtUe4P6ncLzPLjVTc78jG2fSSXHUkuD5lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
عضو المكتب السياسي لأنصار الله حزام الأسد: ‏ونِعم وسبعُ نِعام بقبائل دهم، قبائل الجود والجهاد، دهم الحمراء، وهم في الطليعة إلى جانب قواتنا المسلحة، يطاردون مرتزقةَ التحالف الأبستيني وينكّلون بهم في صحاري وقفار خب والشعف، ويطهرون سوق اليتمة من سحالي بن…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/89655" target="_blank">📅 14:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89654">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇾🇪
🇾🇪
عضو المكتب السياسي لأنصار الله حزام الأسد: ‏
ونِعم وسبعُ نِعام بقبائل دهم، قبائل الجود والجهاد، دهم الحمراء، وهم في الطليعة إلى جانب قواتنا المسلحة، يطاردون مرتزقةَ التحالف الأبستيني وينكّلون بهم في صحاري وقفار خب والشعف، ويطهرون سوق اليتمة من سحالي بن سلمان.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/89654" target="_blank">📅 14:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89653">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الحكومة البريطانية:
تقييد وصول إيران إلى النظام المالي البريطاني وتوسيع حظر التجارة ومنع الطائرات الإيرانية من الهبوط في بريطانيا إلا في الحالات الاستثنائية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/89653" target="_blank">📅 14:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89652">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENFB0NreYj9Ndl6atTVVmPKMNGxLb1BJosKFlA28kcnrJFHBcSZcPVpzFbLhBjlX0omcv8mK2HFEp8Jvs6Mg7enuemsCieqfyhtAvB-QEy_HoFwsVT5N_lM0L8vyPH86QKld7vquRRE1TGjfNwdoR0V0qWfueV6CsdMspB2JoiHk1QmjPKi3F_sFeDKfnc-RxuuXrgoxCpFf-Gjh4ZnOZqY2h4CuMgbaBKOuLEl_FrCr6aG57ZE4wA1CCrNOa2XZ1v2zJVK-zAH_EUg-o4EfHXuD0Tpk87Kj_9IBeuY1-x0ai5PYpSYbA8DtAdZhyTA5qG84yVFogwehb7d6bmULiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مكالمة هاتفية بين الإعلامي قصي شفيق وأحد رجال الأعمال يساومه خلالها على مبلغ مالي ويحدد معه موعد اللقاء لتسليمه المبلغ تمهيدًا لإلقاء القبض عليه بالجرم المشهود. https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89652" target="_blank">📅 13:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89651">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2A7Nxin2x_BI_NBOVgM7zQzDka2z4IFVo20ws6z1fxzDbw5IVVYuOo4QNuMXjO4d0nfr2hhbgjs5TxtgmAQRUBOUqvfk6iowykDOtS5BBzAo1vsl0DHQVDRCjuPtWFKfynT_iLn-mjqqvR43ktaanXmSO85AjEPCSNO9_n-GzAxeJ-_aGNQD75OZZK_6AcWGHFGSwIxI1SgndC2Pid20lt7pG2YXl1ceqri7v6Bmxg2Ol_akRPujiCoeujdvURmY8KvWeXp6EI0Y0eM6eYtjGNoxHcmsCrB5e45CM4tAIEhoj80wUIpgTQYnqhNDXNCdbWpQHulbXz9OudoLb3ZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سفير الاحتلال الامريكي في لبنان: نحن نريد مصلحة البيئة الشيعية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89651" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89650">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عدوان سعودي على مأرب اليمنية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89650" target="_blank">📅 13:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89649">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عدوان سعودي على مأرب اليمنية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89649" target="_blank">📅 13:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89648">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4qsZ___VZ3Ely-DttKqYVIBH0tWljeLfqj2pA6I0qM0xvtxXdlnBTk7iX-1sXUw-QcjCyoqH0EzgHpwqFAzcW5CM8JgPfAkrFogLxagyW0-Ekiolkq8nspwl9pv5_nzuVKDVH5tABTHXaLt8R-83_bKYHR2Aq6TujC2Z44D5yf-yWN9CdCJ-qQf8HZop_QmfV1iJ_dtZIKYOYrABtrl0kDQ3fZ-Vwjgs_eWBGDY4rmlO-T4RW8rb8oOPtKSUZGDuILbHRD5dQEjhZTfpX1pYTgeUQRmzz93x_Gdk9H0vSGzAvooC0cOFV0r2SlDWzDlnrFv0ZCNIt95JRIjfNse4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحرائق متواصلة في جازان السعودية بعد هجوم القوات المسلحة اليمنية.
توني جاي من جازان ومافي شي
الوضع كويس</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89648" target="_blank">📅 13:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89647">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
🇺🇸
قائد الباسيج في الجمهورية الاسلامية لترامب:
إذا كنت قد قضيت على القوة البحرية الإيرانية، فلماذا ما زلت تقاتل في مضيق هرمز؟ يجب على الحكومة الأمريكية أن تقدم حسابًا لشعبها بسبب إشعال الحرب مع إيران. وفقًا لاستطلاعات الرأي التي أجريت في الولايات المتحدة، يعتقد 60٪ من الناس أن إشعال هذه الحرب لم يكن له قيمة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89647" target="_blank">📅 13:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89646">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇷🇺
🔻
الخلافات الاوروبية الروسية تتصاعد وهنغاريا تطرد 10 دبلوماسيين روس.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/89646" target="_blank">📅 12:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28761bb29e.mp4?token=GzHHZaI3wzqojwQqyNlOkqQIWyllj2ZIgZkKsZTGsY_2LVMWBCHlmUuYBG_d_snpHcPz0bocamUsYmTNJCQJUg5qMNADCzWFx8J21vKFYWOoA0U1XqV_j_zEoxBC9GLOhJnbnl08K3vb_pA-Cm3gW3XdFD3XkTBbUWx6G8Fy54bJAbWB6tto7MWLzdo1FyIisLSkxHISsmDO93JYGA6lt0vMJtftIcV-jMF94pqtRxgG2X98Mm1SlLk1AnBtD1t6cHswUzCTGB8H4WjN5yAUEwQWR9AguanIirE2GnLpsu7OZxhljQHNtTgOz9fsZaeCgJn21bRzeM6jNrhCZTSmPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28761bb29e.mp4?token=GzHHZaI3wzqojwQqyNlOkqQIWyllj2ZIgZkKsZTGsY_2LVMWBCHlmUuYBG_d_snpHcPz0bocamUsYmTNJCQJUg5qMNADCzWFx8J21vKFYWOoA0U1XqV_j_zEoxBC9GLOhJnbnl08K3vb_pA-Cm3gW3XdFD3XkTBbUWx6G8Fy54bJAbWB6tto7MWLzdo1FyIisLSkxHISsmDO93JYGA6lt0vMJtftIcV-jMF94pqtRxgG2X98Mm1SlLk1AnBtD1t6cHswUzCTGB8H4WjN5yAUEwQWR9AguanIirE2GnLpsu7OZxhljQHNtTgOz9fsZaeCgJn21bRzeM6jNrhCZTSmPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
في العاصمة بغداد... مشاهد لاحد رجال الامن وهو ينهل بالضرب المباشر على احد المتظاهرين الذي يحمل شهادة الدكتوراه.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89645" target="_blank">📅 12:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36af9ff10.mp4?token=TOONiM1-GTciu-MegtfmExDTFmY2CJ9z8zS4LdMJs2FGNgyYJk47cqc9HwXcuMvJwZmyy42BkriycWIB7TCN-ZcraMaOsBTMNPJj_qRbT7PGlTDT36pvZfbRKqm_rlLwvqWYKFzUf18PzV53kqNaV7ZP4FknNoaIqNfk06t1prSIYB_6WPvH4ZxcwCslZ-Z667Us2q5FR-p0T9oQcI6NR3Iqkv48mQlQN0KNOm5qPW_fan-sp4wzXGGecKF4eBuh7pD46Lmo3SLk4CHH3S0ZpbYz0rsGXaIfO-1i4FZmYbHcMH81fCt4LrON96ariBSpJ2ktBFzp--Ux0Y4UDw1tpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36af9ff10.mp4?token=TOONiM1-GTciu-MegtfmExDTFmY2CJ9z8zS4LdMJs2FGNgyYJk47cqc9HwXcuMvJwZmyy42BkriycWIB7TCN-ZcraMaOsBTMNPJj_qRbT7PGlTDT36pvZfbRKqm_rlLwvqWYKFzUf18PzV53kqNaV7ZP4FknNoaIqNfk06t1prSIYB_6WPvH4ZxcwCslZ-Z667Us2q5FR-p0T9oQcI6NR3Iqkv48mQlQN0KNOm5qPW_fan-sp4wzXGGecKF4eBuh7pD46Lmo3SLk4CHH3S0ZpbYz0rsGXaIfO-1i4FZmYbHcMH81fCt4LrON96ariBSpJ2ktBFzp--Ux0Y4UDw1tpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
في العاصمة بغداد...
مشاهد لاحد رجال الامن وهو ينهل بالضرب المباشر على احد المتظاهرين الذي يحمل شهادة الدكتوراه.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89644" target="_blank">📅 12:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbBRxD-3XnZiEdxOSD1Fw3pVorQaWB4gmsmTlxr9RtlC77j3Ir-sIm9sr7DRccdPwLzL_NW-0ZtNIC-QdJMwyDCFZQbx0HRKUJq8R-IIg8ZFCc5rGZAFV2AJUiwADUZuSVCuzOwyduyaQw2izyXmdqaTAfw7Pq2Cmn_bvEgvUk3ObkcM9yuxs-HH8PzBujxPP4ajLGSf_nCGkSNUL2gDXwkOhaE50eDZn-Spjs304JxWwBjtiMasDJnSDen9OB_OYKpYkKtSlzVWEPiwh043Lcz3p0sTIH98HuIPfZeO_384Dgc0NMqnDm47qAzqAJdc5dZZ_w7ShQgicRIABqP9eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مع تصاعد الدخان من المصافي النفطية في السعودية.. إرتفاع أسعار النفط العالمية حيث سعر البرميل الواحد أصبح يلامس 99 دولار.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89643" target="_blank">📅 12:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89641">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f329323008.mp4?token=PxtSPsEIqsmE1R-uYRha0habh42znGuiUWHZwsl3-hms8NKfanxXoDzqQlQ9mZ3VhWWOv3NbhB6_hitBvgGCIpqkv0dTFGYdmZg65NA8gibyk3YFrxjNzyFvst7qlM27RUTRKYOPYmTAnucFYXsdrZXvQ19PB6vSDAQCuzjLmIcPiZszN33EeOwgxPhEqSdOGCyFuGqJ2nGVDgx3VE1zc2RNpx1QK93u9-6AXLXe4rN-XW1fCevA1l4KHH-q5kxXhLAK_4zfqLQSmvCd4Zlz6xlpiiJzYQ6APw-3btJRAe8yn8xrmakQhi6WlXtsIiZAMDlbHfb6X4yDSnhzOCCshg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f329323008.mp4?token=PxtSPsEIqsmE1R-uYRha0habh42znGuiUWHZwsl3-hms8NKfanxXoDzqQlQ9mZ3VhWWOv3NbhB6_hitBvgGCIpqkv0dTFGYdmZg65NA8gibyk3YFrxjNzyFvst7qlM27RUTRKYOPYmTAnucFYXsdrZXvQ19PB6vSDAQCuzjLmIcPiZszN33EeOwgxPhEqSdOGCyFuGqJ2nGVDgx3VE1zc2RNpx1QK93u9-6AXLXe4rN-XW1fCevA1l4KHH-q5kxXhLAK_4zfqLQSmvCd4Zlz6xlpiiJzYQ6APw-3btJRAe8yn8xrmakQhi6WlXtsIiZAMDlbHfb6X4yDSnhzOCCshg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
حملة اعتقالات تطال متضاهرين من ذوي الشهادات العليا.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89641" target="_blank">📅 12:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89640">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6ykv1JodtgsAq-vDszFLgv-EHoqRFXllIAg9LNAAHtjl3O4e4u77I3-kMNLMnGvfQPEwY5PFX2edN0bxKzYpNN3-Mg6INfzkCIDm-ygs43KyjeJy0wwPtVPqhwU7N7FbVFmPr-T9w0IoX-I4glBZkTGa3K_c4L-_go55mSkzfkk1FPjzqggw5mNOBWACrFLwom3Ld_iL-cojLMkcLlvhJcYZLM2rlfQkO1rRNXK8VmeOcsgEhznfYmbf93mf6JfU01ISVRbXzhJcaxl5zoX0JyhjZ0y_GdETUS32fQqM-KTZELi4_XxkqIYp9rPKHNeI779ujDSGYqm-VZDyoyZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
اعمدة الدخان تفرض سيطرتها بسماء جيزان السعودية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/89640" target="_blank">📅 11:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89639">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d84cecfa.mp4?token=dAWMXEIjm7u6GOjlqtAbkBXqGnxsiMJQ2Bns1iCHfhzxZfJFhX988sC2111XNYHnbNd2tGIr8bAMlmsUtctPPzs3PQ0kab5OLox6CFaDVy-RzW0SCtIrshDHZQKTE1LQisOkf0MUum46HVEwF6bdgwNi_ETRdHlAtk0yY3-OhpdkDkkApex8afHWS2A7tZMaxG_ekomyTRHiN3yLOLD5IlKlrdKs7Wxf6KfbGEH6oixHvgNELPVZd62GktE8kKC3zyfi12FItmyoyfumTjIJuqZ1VjSVMsXUrfbuFxD8E1A9GrDJS4XZxpePN754MV0LDZUvTkcnTlNPDI7SKc4Ijw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d84cecfa.mp4?token=dAWMXEIjm7u6GOjlqtAbkBXqGnxsiMJQ2Bns1iCHfhzxZfJFhX988sC2111XNYHnbNd2tGIr8bAMlmsUtctPPzs3PQ0kab5OLox6CFaDVy-RzW0SCtIrshDHZQKTE1LQisOkf0MUum46HVEwF6bdgwNi_ETRdHlAtk0yY3-OhpdkDkkApex8afHWS2A7tZMaxG_ekomyTRHiN3yLOLD5IlKlrdKs7Wxf6KfbGEH6oixHvgNELPVZd62GktE8kKC3zyfi12FItmyoyfumTjIJuqZ1VjSVMsXUrfbuFxD8E1A9GrDJS4XZxpePN754MV0LDZUvTkcnTlNPDI7SKc4Ijw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
اعمدة الدخان تتوالى بالارتفاع من مصفى جيزان في السعودية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89639" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89638">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYOxQyCBgdjVT8uhY5Dmnw2aiyDAC6yJfqR4A3DCvqZ1_aCu_gWNQMrOdVRsEnv_vcvjjqZ86t7aBs1n8aXlRasUNjTNzAjrWR6BKhZ3rA8_RHwMjA8XfnmQyWJydCnA69EfVMquzHbL7ghohy1R1KjgY8rdj2xHPObgHy-nZtYvb-ijYt67MFb04yd89nvY5X7FpR_vRGIdMhi-MvA-2KtoradqHLK4ftn92LjEGShQuG_Rj3Da3HGnCP__t5aLs9ctJSLVD030PC-qY8XmjU4eoPyivOfCT8SlqJ8ZFcN8yEw7o8FZrmBWmb0H7XyZS6bcRZhNPPvwvob5i8tcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
تظهر ارتفاع مباشر لاعمدة الدخان من وسط مصفى جيزان في السعودية بعد استهدافه من قبل الجيش اليمني.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89638" target="_blank">📅 11:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89636">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية سيكون في تمام الساعة 10:40صباحاً، بعد قليل.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/89636" target="_blank">📅 11:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89635">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89635" target="_blank">📅 11:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89634">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d7819112.mp4?token=shx_YaX-MZugJzq-PqjGCWyX8ECMAw72Yqrj7jF_RoffPQPi7SCY3cJxp1BZge_A5vgOGTWoZ7hzTI04aRRAEPd_GNOT09DkYH_mXG38RNUYLWcZDYRXvC2DjQuTXjvbNPvqeWbFYyG-_rbscAi1pjqOkQoIn2Ehx8Ulb1SGF7nKNnajthYa3CadNJDo5DP8cYi51d_mGJ3A_rBhJ1p28_oaKe4pWFpzg3rnkVRoydHXyo_hH92muSjI5eIM60OVX5ernJ_PdoRHqwFwkKengq77impZihxD900vQWgA_vSEymmrpLHKmFUdvKJOJyb9cvA4IsP1aYWZy4nxv-f_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d7819112.mp4?token=shx_YaX-MZugJzq-PqjGCWyX8ECMAw72Yqrj7jF_RoffPQPi7SCY3cJxp1BZge_A5vgOGTWoZ7hzTI04aRRAEPd_GNOT09DkYH_mXG38RNUYLWcZDYRXvC2DjQuTXjvbNPvqeWbFYyG-_rbscAi1pjqOkQoIn2Ehx8Ulb1SGF7nKNnajthYa3CadNJDo5DP8cYi51d_mGJ3A_rBhJ1p28_oaKe4pWFpzg3rnkVRoydHXyo_hH92muSjI5eIM60OVX5ernJ_PdoRHqwFwkKengq77impZihxD900vQWgA_vSEymmrpLHKmFUdvKJOJyb9cvA4IsP1aYWZy4nxv-f_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
صباح اليوم من سماء جازان في السعودية تضهر سحب الدخان الكثيفة الناتجة عن احتراق مصفى جيزان بعد استهدافه من قبل الجيش اليمني.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/89634" target="_blank">📅 11:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89632">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6OqEgMY7HxlrekYt71zTQkorr2USiQl_dQnPkPGFhAK-c4dvZ351HqNy-aLtMViFdr_T2CZplWYARCLur_-Z1fNyCT78Xhm2ydDxszbrjjrOBU9qm90ovNw-U9m5RsJNRejWzcGvHfcHxDvbqMB6nQ4HIdEx49sD2Wz_U4eEK2AxB_T5IE6otpMX3O7ca4bQZa7DTU7OmhDLvpjyB60hYGTPttECHB0lRF6NK2I0O6luVwmahvaJLi8WlKTJDBAUfazwumcuam-mZYaGGT6zAsdcpbIN8hNiVSy9l3m_E1QfuiR1Vj858uvJtU7rxDd1iyo3kNnQQudkbEywLyQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NggdzwyDEiToUg0Z0PyO_jcAPNVu0zg-MzzEr8ho2o-sxA2jiiQT1VOm1VAILsj9MXY6T-I3qGzVY94td-qkL-vVHnKy4Eso1Cgm3IDGq7udgtmiMB9vTUogeK993UEIKq0oM4wXPhH1YcNP7pHGAhPUNeAzNtSG0IbOItqlhbJyR4UBCvOeI5bKDjcoYu1GHWbkntSz0Zt-_GKKeq5gcuiE_xjCx4iGExYqbMLMEJoImlNWD-aoTRa6XMvh-CLvoRSIJ2whwc9lIrfwYw5UMxoJpNODWLykLa8u6eg1HnMIFS4w-oGDgSSY5RM0co9LvRP-7Q7Py13TXKtT_8ivbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد من الأقمار الصناعية تُظهر سحبًا كثيفة من الدخان تغطي سماء جيزان جراء الحرائق الناجمة عن استهداف مصفاة أرامكو في القصف اليمني الأخير.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/89632" target="_blank">📅 10:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89631">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نايا - NAYA
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/89631" target="_blank">📅 10:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89630">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be6967c380.mp4?token=DlRh5ZWXQaoqImf-t8raAeqwZvMSY30S4QeBJ5lwzwc07yYYOvS91dqhTzEgoNjPhAiib-PbZdu0A7a4XCPwtUh6FwZ4tEY0E1_03mv2jYUYSL4CzIrxySDM4lXO5n05VLoORr_AjpDsEdzYon3LVHcu3JrDfkmRLhjOstFq9Oullni15K1yLMdBv5pbLYmL8EgJlint8Oqfp0l7Mkp9dfh8r1okxM_UndR-1V1G4na97CyiqwnJ8ihC8_HwmoK8OYl3R3wLKw8lC2KOnlRMDzQOeRDlqDfdgbuUWcv-RQCvFENC3Dra1cLra6ZRPUD3vNvLgqgfRslR-DxmX5XlQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be6967c380.mp4?token=DlRh5ZWXQaoqImf-t8raAeqwZvMSY30S4QeBJ5lwzwc07yYYOvS91dqhTzEgoNjPhAiib-PbZdu0A7a4XCPwtUh6FwZ4tEY0E1_03mv2jYUYSL4CzIrxySDM4lXO5n05VLoORr_AjpDsEdzYon3LVHcu3JrDfkmRLhjOstFq9Oullni15K1yLMdBv5pbLYmL8EgJlint8Oqfp0l7Mkp9dfh8r1okxM_UndR-1V1G4na97CyiqwnJ8ihC8_HwmoK8OYl3R3wLKw8lC2KOnlRMDzQOeRDlqDfdgbuUWcv-RQCvFENC3Dra1cLra6ZRPUD3vNvLgqgfRslR-DxmX5XlQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
صباح اليوم من سماء جازان في السعودية تضهر سحب الدخان الكثيفة الناتجة عن احتراق مصفى جيزان بعد استهدافه من قبل الجيش اليمني.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89630" target="_blank">📅 10:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89628">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c1b5f5d8.mp4?token=bNcEKCBL1wkKiqOIcbDNc1ho2NlMpho7C1h-bZrMAByOXpkZ9H6qV859cxwxlEji7n454cEgzgmxs4JDb2i90y5uadGf1tf9ozRDhhjCbn8BLXuL1RYkmq73AUnKMvMrLO6OOuMXWwLLrYVhdq0wldp042I4GUCoop8gaTeb8O-ClNgAUTRI9I5yjHYJrRrmUPDtHh68G2U8R1AGjCVnupSmyyNhLG1k2wl52MBU1jNlW9uwTzSr_tDNM7BUyw7a9nRK9VDgpElrVFkHvrcFaHVb48MuJXVL9Yup-b777Rnxlo9Xr4jF9hnGaPnAhix0EFX2PA7yOC3Ly7mos84QlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c1b5f5d8.mp4?token=bNcEKCBL1wkKiqOIcbDNc1ho2NlMpho7C1h-bZrMAByOXpkZ9H6qV859cxwxlEji7n454cEgzgmxs4JDb2i90y5uadGf1tf9ozRDhhjCbn8BLXuL1RYkmq73AUnKMvMrLO6OOuMXWwLLrYVhdq0wldp042I4GUCoop8gaTeb8O-ClNgAUTRI9I5yjHYJrRrmUPDtHh68G2U8R1AGjCVnupSmyyNhLG1k2wl52MBU1jNlW9uwTzSr_tDNM7BUyw7a9nRK9VDgpElrVFkHvrcFaHVb48MuJXVL9Yup-b777Rnxlo9Xr4jF9hnGaPnAhix0EFX2PA7yOC3Ly7mos84QlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
صباح اليوم من سماء جازان في السعودية تضهر سحب الدخان الكثيفة الناتجة عن احتراق مصفى جيزان بعد استهدافه من قبل الجيش اليمني.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89628" target="_blank">📅 10:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89627">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇾🇪
نائب رئيس الهيئة الإعلامية للجيش اليمني: البيان العسكري في الساعات القادمة، وما تأخر فيه الخير بإذن الله. https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/89627" target="_blank">📅 10:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89626">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfc95cc5d.mp4?token=BzS-8dsfvGpfTcfau2Nga_Ll-0rkrAHo1RpF-qkxKDcZZ1rqrkRhcF-Gd6DVEo7h9KFtzzT47hyM5vTuB2CymH7zySAYl0d1GWI5YU3JwXhqi4Us5bnkB3-uN1w0K_ePw0_SispaFfBUMsnjrslpxPGC61VD0ms93uIw_dXepvT9AOVVZcmeHGpjp9-5F4WPAJ0IOFWk9Q0w-33AHDb-OxTbqYn05cgMoL-ppV-lE1RhbZzm3MYO_hkxt-34T59DzfMs3yPNZFmyetde6PqboUJ51svLvEqYDQw9H5C8pHcz5f8nS5_BeBcMbZiZDYn66P3iTPs7T7k-rVR-yjPsFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfc95cc5d.mp4?token=BzS-8dsfvGpfTcfau2Nga_Ll-0rkrAHo1RpF-qkxKDcZZ1rqrkRhcF-Gd6DVEo7h9KFtzzT47hyM5vTuB2CymH7zySAYl0d1GWI5YU3JwXhqi4Us5bnkB3-uN1w0K_ePw0_SispaFfBUMsnjrslpxPGC61VD0ms93uIw_dXepvT9AOVVZcmeHGpjp9-5F4WPAJ0IOFWk9Q0w-33AHDb-OxTbqYn05cgMoL-ppV-lE1RhbZzm3MYO_hkxt-34T59DzfMs3yPNZFmyetde6PqboUJ51svLvEqYDQw9H5C8pHcz5f8nS5_BeBcMbZiZDYn66P3iTPs7T7k-rVR-yjPsFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
أعمدة الدخان تملأ سماء مدينة جيزان جنوبي السعودية عقب دك المنشأت النفطية من قبل القوات اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89626" target="_blank">📅 10:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89625">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇷🇺
🔻
الجيش البولندي :
‏أنهى سلاح الجو البولندي عمليات الرد على الضربات الروسية على أوكرانيا؛ ولم يتم رصد أي انتهاكات للمجال الجوي
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89625" target="_blank">📅 10:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89624">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية للإعلان عن عملية عسكرية واسعة في العمق السعودي، في تمام الساعة 9:30صباحا، بعد قليل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89624" target="_blank">📅 10:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89623">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
لمتابعة الاحتجاجات التي تشهدها البلاد اليوم وتطوراتها أولاً بأول يرجى
الضغط هنا
.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89623" target="_blank">📅 09:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89622">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvT0SFqhpJQ0murbcWFTMDerLhyAbfRYnVjsIQ45LuFtsnxAKM4HuydU_oiYM0m2SaCc5LrMuO5V_FdZhpRysYdjoCqQjS9lNSBxM2lL0MpMBYe5bOXKI--72c_7tb0-FsYq09AXuAyTgumAivA9SU9NN5TWIDkcwPXQiNP4BlAyh5N-F5k604m9pqCklKc-IFhFtVBf_BGlcad7g7VbSu6yTQrAUTjhm2kJjvmnGVIvsWqqOLm2sC3WOdSgoBtsiTxc0SrpTW_lzqjjj2pTi4z5oY3AcHbtVVYiWriiqCNsfcwy_nw0zP1Y0r9B3LiEDQZh_-vaBml7j6uZ86ss8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🇾🇪
🇸🇦
تصاعد أعمدة الدخان من مصفاة جيزان النفطي في السعودية نتيجة ضربة صاروخية يمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89622" target="_blank">📅 09:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89621">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN7419d_7UfPCkbyhiYwF11-sJ2IOMU57WoYQe8Nqy0dYThTuhk5a7gNMpVHGOJhSlvuwlVe-uIiVvULph3aMwjNAZi7hnIQNlvNVux5AzezmzTzEaF5Z_oXjj6wcD6Q8Zl_5nDNXGmBcxPDTqFvjVU4vydeqXXp3v6hXaUfqNuUV068oIkma7_ZtnPA193qqzHhlRrT5dW6lEU9F0VQfSB0xZoForgXtP582rLH9EMvkZ_UhPnhnHO3SpUckmq6jmol3qanLuhrJeiSdtbKZuw7MYIQBmbPWgTnpXQYTU_lIOxEsGZV3udAqWxDfPUeqQyukScez6G0Eg7_YgJ50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏الطاقة السعودية:  استهداف عدد من منشآت ومرافق قطاع الطاقة في المنطقة الجنوبية من المملكة.  ‏الاستهدافات تسببت بنشوب حرائق ما أدى لتوقف مؤقت لبعض العمليات.  ‏الجهات المختصة تواصل التعامل مع تداعيات الاستهدافات.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89621" target="_blank">📅 09:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89620">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعترف بتعرضها لضربات يمنية في أبها وخميس مشيط وجازان ونجران وتعلن عن إصابة 73 شخص كحصيلة أولية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89620" target="_blank">📅 08:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89619">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية للإعلان عن عملية عسكرية واسعة في العمق السعودي، في تمام الساعة 9:30صباحا، بعد قليل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89619" target="_blank">📅 08:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89618">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعترف بتعرضها لضربات يمنية في أبها وخميس مشيط وجازان ونجران وتعلن عن إصابة 73 شخص كحصيلة أولية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/89618" target="_blank">📅 06:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89617">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f28482b8.mp4?token=a2cbySR--53VmD7Afyl01bdR6GqibCSfZcn838qxG0RJaPiY4ju6D5UBIP2biV0ZkiQ4fSwEqfZXkIfAtoCwQjIHoOy8UBNwrzQ6qdKwfHl2VEGylw_rFx3A9ez9Fg05LA92tPbgDYYz1s7hAxZ8Jtwf7EBcRfNT6aHQ61ORp2WybR_Ib2TxZPwQOkidJGAGjdpOODz-L_Tfi_ZQBFF55OuYL5Y9t5_hu7IlCL7pgUahXrmHm9t-YfYYdBJDprKCr4NMhbkJ2fPtN-3Vu5hp5O6zZ59NAFqjeiirNsztqESrx6Dq-dAuMDu8ZCVi3-OqMZWfGi7NvbqK4ogDR4Db7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f28482b8.mp4?token=a2cbySR--53VmD7Afyl01bdR6GqibCSfZcn838qxG0RJaPiY4ju6D5UBIP2biV0ZkiQ4fSwEqfZXkIfAtoCwQjIHoOy8UBNwrzQ6qdKwfHl2VEGylw_rFx3A9ez9Fg05LA92tPbgDYYz1s7hAxZ8Jtwf7EBcRfNT6aHQ61ORp2WybR_Ib2TxZPwQOkidJGAGjdpOODz-L_Tfi_ZQBFF55OuYL5Y9t5_hu7IlCL7pgUahXrmHm9t-YfYYdBJDprKCr4NMhbkJ2fPtN-3Vu5hp5O6zZ59NAFqjeiirNsztqESrx6Dq-dAuMDu8ZCVi3-OqMZWfGi7NvbqK4ogDR4Db7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
🇮🇱
إندلاع اشتباكات بين عناصر جيش الاحتلال الصهيوني ومقاومين فلسطينيين في بلدة عقربا جنوب نابلس.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89617" target="_blank">📅 04:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89616">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
عضو المكتب السياسي لأنصار الله "حزام الأسد":
المناطق النفطية والصناعية والمنشآت الحيوية في مختلف أنحاء المملكة لم تعد آمنة، ومستقبل الاستثمار في السعودية بات على مهبّ الريح.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89616" target="_blank">📅 04:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89615">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇸🇦
إنفجار عنيف يهز خميس مشيط جنوبي السعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89615" target="_blank">📅 04:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89614">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇾🇪
🇸🇦
مصدر يمني:
الرد على عدوان وجرائم السعودية مستمر حتى اللحظة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/89614" target="_blank">📅 03:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89612">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1FgiHCHvAV2KKOf7DbRRTWusz6NgxaLs-a0gSzeYqzrDPfP27TfEMafDlFK6K2MLAbw4D4QmWP1IdAzVtIGSTvXTr8NkG6jUaPWWq8N95xdvb_qbPLwfV3sbuLG0wuZT8xkFl-B_MtkqIatu3GN2EcA7aVtc7WEQlhT06Awbmi5kKI43NLNSbi6E7CX7JlhXqrbYjh8T_Ink50MnaQN2FI-egDIu8QrN_GnvYCiDq87jYUTvXHwoyn9UdR4kXl1MQMf4FFaakLyxbyvk3uAkJZXcsYP-YaqxH0jkmb9luCV1h-m5DuL02Ql5gjY8ycCs0gh7MCwx4SlKSNnsXgq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7IM20VXgWb5e7YZ91SKDdY-iyWZwu5T1zzBwBlFuHVG8ZPm5Os9kdglKLtr0Abin0j8pgR9G-LMGMXhYK5iu21xOhc3xUc3Id-FvLec7-XGQRoKiMo0cvoP1Ui9bdCCxt3w4FqTV4mUUVrtE9OYwuClgIg-nlRh9Ifd0hRo5cdukxZta3DxvDk-Hg5odWP5JFmojkyQwafRF1QPW9ZxdO8Yixrl-kb2P3lMOaBg9Q1XtiamvT06mKgB-7CXPAkHu1dKYEtQQ4rc9YvQuBKnvMr3WPUNBzlzu9rTd7m537b4xxCB7gq5e6DzWZz1_VfuvoANQlRX2ulZWYotL6P6uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف منشأة نفطية ثانية تابعة لشركة أرامكو في مدينة أبها السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89612" target="_blank">📅 03:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89611">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي في هذه الأثناء على محافظة صعدة اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/89611" target="_blank">📅 03:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89610">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2f5bb5b3.mp4?token=q2Y17_Cehfz0NFUs9Q_lRbsKCDgAWwyPGzufn14Q2fVBpHaOCt2-8N29dRDEcE_mp4Pk7yTo2EhVnPQyqJmg2GVb5zQm6JdGgGONONn1TXTqidqreV6FZrTX1JevC2k1cs1IbHJ7bgk_HJ8M8urumiRYDKiB-YKFjhA5oERrOdPgP2YZaxEQALpS47DSueqr0bvCMpPSf275AqUX_4fDjesj8OHu_k18ms9WlHSQnaNVwTGnLG9wy1UtP4US0lH3iqmeLezJAEFalFt4-tzKxUitXvermThMHgLMk7hySabkkZBHJXDcmouTfXZXOoL3C2yQPa8zTMi4PqRjOexv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2f5bb5b3.mp4?token=q2Y17_Cehfz0NFUs9Q_lRbsKCDgAWwyPGzufn14Q2fVBpHaOCt2-8N29dRDEcE_mp4Pk7yTo2EhVnPQyqJmg2GVb5zQm6JdGgGONONn1TXTqidqreV6FZrTX1JevC2k1cs1IbHJ7bgk_HJ8M8urumiRYDKiB-YKFjhA5oERrOdPgP2YZaxEQALpS47DSueqr0bvCMpPSf275AqUX_4fDjesj8OHu_k18ms9WlHSQnaNVwTGnLG9wy1UtP4US0lH3iqmeLezJAEFalFt4-tzKxUitXvermThMHgLMk7hySabkkZBHJXDcmouTfXZXOoL3C2yQPa8zTMi4PqRjOexv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
حبا بالعررررراء
عمي احنه وطنچيه
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89610" target="_blank">📅 03:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89609" target="_blank">📅 03:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الله أكبر
🇾🇪
🇸🇦
تصاعد أعمدة الدخان من مصفاة جيزان النفطي في السعودية نتيجة ضربة صاروخية يمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89608" target="_blank">📅 03:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89606">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvSbapMUQnwmYZbigSMcQfsiHx1Q5CHUDRADoZeIYpWZwJXIciRMOu34QoO4QrYPwWLHs-KtOd11_EnnXg_WrwxDtgkoQcKb9AZBHycndr42bHiA3QMHaQauiAPn0HwnHjEKYaYdGXyL5vIUIJlukWnwPH76Jit07AzAXpmGXCcmznvThWXwbbRiE6ULYNXAfqQqu7LOr_6N2KoHXkuuZXhDPNyh7pdxyLuGTKrVrGIu341bn_OdzlimEbX3L5-F-zLxk3bjJGk5CcBJcF3h4I-PzIIMMWJhcP9ANR-b1LSgl_DziaWw-U7ZDFnUs6hCtGi_RQzj46ML3t1UVBD1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
ستنخفض أسعار النفط بشكل حاد عندما ننتصر في الحرب مع إيران ، ستصل إلى ثلاثة دولارات للجالون وكل هذا سيحدث بسرعة ، ولن تمتلك إيران أبدًا سلاحًا نوويًا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89606" target="_blank">📅 02:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89605">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/89605" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/naya_foriraq/89605" target="_blank">📅 02:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89604">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇾🇪
🇸🇦
سرب جديد من المسيرات الإنقضاضية اليمنية يستهدف مدن جنوب السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/89604" target="_blank">📅 02:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89603">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇾🇪
🇸🇦
إصابات مباشرة في قاعدة الملك خالد الجوية بخميس مشيط جنوب السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89603" target="_blank">📅 02:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89602">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇾🇪
🇸🇦
صاروخ يمني أثناء مروره بسماء المدن السعودية متوجها نحو هدفه.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89602" target="_blank">📅 02:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89601">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f26d82ac8.mp4?token=WWHg8WqraHniIiMsX33-ldG57VNItan8JvPOQ9R9bB5EJ0w1qy1qrHGnGYLBGPkGcpUUjGor_A-TJmZmxZqBuvHnALrX3aCtJ-ihUhKKvsDKmcQElg-pUKsnv3VpbLYfHrwt8bd-jjkVJMl0T7lyPOpt3SCjwINgflflFPB1lvRtigLlTAaZFe_F8fLatInKzuby5XRcl4ceBDc_AGyg1_0WIzPvPoq2bMlgveaVPBZf23dWaiOohZ1lYH8eUbyJslDTB-pxZ2vrqA7lBHwwZs_GmQ8qV4D3sB1aFq3ugU4_uJL7ce_BElQkIUJS43Mnh-d2suNCGuzST9dkx3x-DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f26d82ac8.mp4?token=WWHg8WqraHniIiMsX33-ldG57VNItan8JvPOQ9R9bB5EJ0w1qy1qrHGnGYLBGPkGcpUUjGor_A-TJmZmxZqBuvHnALrX3aCtJ-ihUhKKvsDKmcQElg-pUKsnv3VpbLYfHrwt8bd-jjkVJMl0T7lyPOpt3SCjwINgflflFPB1lvRtigLlTAaZFe_F8fLatInKzuby5XRcl4ceBDc_AGyg1_0WIzPvPoq2bMlgveaVPBZf23dWaiOohZ1lYH8eUbyJslDTB-pxZ2vrqA7lBHwwZs_GmQ8qV4D3sB1aFq3ugU4_uJL7ce_BElQkIUJS43Mnh-d2suNCGuzST9dkx3x-DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقة صاروخية جديدة تنطلق من اليمن نحو أبها ومدن سعودية أخرى.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89601" target="_blank">📅 02:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89600">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇾🇪
🇸🇦
الصواريخ والمسيرات اليمنية تطرب في أبها السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/89600" target="_blank">📅 02:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89599">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N36im1lcQP4qZxHHWQhvyM2ZXa5Z36DApYGUIaBZ4h_r86KKV-2Lz1uQJ3kuzzrmqmYbA8e8s-P7rFD0TFl4ydp_tBAanFWEizqsMlx9OtDpMEjkOFykK6Xote7jnl4RcmtBY_oYNpoO-lGSY7D6n5vRQlT48PH46p-a5hFUElu4P-1qB3gf5D83kKNGQPgfyeRv06_jY-SXaFjJGJzrLgGnlZSNiOAW6jumpwH3MuPXjup6wSEFYD3EmP2p6pr3Z760UOGPTH6g_pm-8QSSl4qgHpVPg5zunN6lNzyYYeDVW8-N8dQNTEUZjYfffPGHDnIp3MEam9c7JR5Bh3vIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرب من المسيرات الإنقضاضية اليمنية يدك السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/89599" target="_blank">📅 02:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89598">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89598" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89597">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">السعودية تفعل منظومة " لا تصور تكفى " بعد فشل منظومة الباترويت   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89597" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89596">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رشقة صاروخية نحو خميس مشيط بالسعودية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89596" target="_blank">📅 01:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89595">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/89595" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/naya_foriraq/89595" target="_blank">📅 01:37 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
