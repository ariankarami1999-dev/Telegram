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
<img src="https://cdn4.telesco.pe/file/u01jPFQoPPrH-UfRVIBgRWYvkPXCyXdYL6JuxReZ6TmkukqxSXS33oqpLLlYl9tzK8gZJE9gK-kMuyOml2Y1MuwUG-wvZwfW_T80Gkf0DOGy4j0ZVIQtgQAvcKvHumsN0WpgoZi2Fv8wA4SIh3FPvdxtmBfohtGF75Ab6sUTPv5-2VAqc1p0w14vX0t8AapNt9y2Cl3g8xfVpm5k332VjSzajyRmjrhAowWHRnMW7dMNI5oroCG7-5fjdQ1E2Y_37a2KA3Rol0FD2cakXlCQSdiR0JNVPpjbV9bkgtufUgxM_TnRQJ2bEkXf9cNtT7-nhToqpZaDi-nq_nTzX9y1IQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 00:58:40</div>
<hr>

<div class="tg-post" id="msg-89954">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">جيش الإحتلال الإسرائيلي: تم تفعيل أنظمة الإنذار بشأن اختراق طائرات معادية في عدة مناطق في شمال البلاد.</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/89954" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89953">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">طيران مسير يخترق شمال فلسطين المحتلة</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/naya_foriraq/89953" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89952">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">طيران مسير يخترق شمال فلسطين المحتلة</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/naya_foriraq/89952" target="_blank">📅 00:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سماع دوي انفجارات في سيريك والمناطق الساحلية من مدينة ميناب جنوبي إيران.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/naya_foriraq/89951" target="_blank">📅 00:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عدوان سعودي على محافظة الجوف اليمنية.</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/naya_foriraq/89950" target="_blank">📅 00:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89949">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">التلفزيون الإيراني: دوي انفجارات في جزيرة قشم جنوبي إيران.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/naya_foriraq/89949" target="_blank">📅 00:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89948">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">التلفزيون الإيراني: دوي انفجارات في جزيرة قشم جنوبي إيران.</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/naya_foriraq/89948" target="_blank">📅 00:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89947">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇾🇪
الرئيس اليمني مهدي المشاط يصدر عفوا رئاسيا عن كل المخدوعين بجبهات الساحل الغربي لمن ألقى سلاحه وعاد إلى رشده.</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/naya_foriraq/89947" target="_blank">📅 00:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89946">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
انفجارات تسمع في سيريك</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/89946" target="_blank">📅 23:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89945">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A80UpMDNw4wD61sM1Dw9MTc_GiWVD-Ai1a_dXApV4N5F5fIN9me0XaNZwQf42itlNbUEZRPC-s4V9S1ZpLnLjPq1hO9_u2dVnVFymaJ3gUXoFgvRlVXZ9p_3gDDjB3Zgt8XtIHC62ifEM473u8R5pQD3sL74_pCLEF9kl9kWrFXLEn4V9TZeKuvgO1IaydRtwXnmqf8ojGkTB9-mn2FCoImwXt1yvGRJPQkcGN0YHjbDpy68B52vZ7qqo1pU0lWYjbn5CGXkGkqNa82I627CDMY67x8Wg_Pn8o0cVo705UCDMF4XfJ83J2-TXL7PWQv2Ks4jgYT96CbYb5vIWrmRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية: الادعاءات الواردة في بيان جامعة الدول العربية تتعارض مع الواقع
وزارة الخارجية بجمهورية إيران الإسلامية، أصدرت بيانًا أدانت فيه بشدة ورفضت جميع الاتهامات والادعاءات الباطلة الواردة في البيان الختامي لاجتماع وزراء الخارجية في "جامعة الدول العربية" ضد البلاد.
أكدت جمهورية إيران الإسلامية، مع التأكيد على سيادتها المطلقة على الجزر الثلاث: أبو موسى، وتنب الكبير، وتنب الصغير، أن أي ادعاءات إقليمية في هذا الشأن لا تتمتع بأي شرعية قانونية أو تاريخية.
جاء في البيان أن أوجه عدم الاستقرار في المنطقة هي نتيجة للعدوان العسكري المباشر من قبل الولايات المتحدة وإسرائيل، وليس بسبب وجود إيران؛ وإيران دائمًا ما تؤكد على الأمن في الخليج العربي بالتعاون مع الدول الساحلية.
رفضت وزارة الخارجية الادعاءات بالتدخل في شؤون اليمن، وأكدت على ضرورة الحفاظ على وحدة وسلامة أراضي هذا البلد ودعم الحوارات اليمنية-اليمنية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89945" target="_blank">📅 23:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89944">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
🇮🇶
مصدر امني لنايا...
قوة أمنية كبيرة تنتشر داخل مدينة الصدر بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/89944" target="_blank">📅 23:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89943">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab93955bb.mp4?token=dzXZ2WeoVI_d-VlM-LDbs6ltqyBmZLkxr2b-lkR2S6fvWPbtkou1E0NdpMUXN8yNTfwBS8u3GFTrC8aH-ttBnuSStaWxx80AN-yAPONbgSy6j3SSyuuv3326nhK-OZo-2fkfPhfbqwdqNTsydT_kLa5kG_9tq2uBPmfhwJdCPOVHwAhU5AkSUnxfX6s3RZ2MaM5U3v6CojMXA39t2aZrqzrmTaovlvBoiloOyoZ0QvkFFtIZYgmN4YGs_eErkwA2NwY85ndR_Z1uD7_dQcc_4cUXytNpsXgJJKLZBSAOiy4ZxLo21lHksce7hHwah6WJuZxKX7LxRG8km8XOjMdPPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab93955bb.mp4?token=dzXZ2WeoVI_d-VlM-LDbs6ltqyBmZLkxr2b-lkR2S6fvWPbtkou1E0NdpMUXN8yNTfwBS8u3GFTrC8aH-ttBnuSStaWxx80AN-yAPONbgSy6j3SSyuuv3326nhK-OZo-2fkfPhfbqwdqNTsydT_kLa5kG_9tq2uBPmfhwJdCPOVHwAhU5AkSUnxfX6s3RZ2MaM5U3v6CojMXA39t2aZrqzrmTaovlvBoiloOyoZ0QvkFFtIZYgmN4YGs_eErkwA2NwY85ndR_Z1uD7_dQcc_4cUXytNpsXgJJKLZBSAOiy4ZxLo21lHksce7hHwah6WJuZxKX7LxRG8km8XOjMdPPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: "أعتقد أن الحرب ستنتهي فورًا بعد الانتخابات. لأنهم لم يعودوا قادرين على الاستمرار. إنهم يائسون ويحاولون التأثير على الانتخابات."</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89943" target="_blank">📅 22:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89942">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c763a585fa.mp4?token=ox8UGbNaWBNSliFFG1rPwscv4YahdqM4ijrqh0lXwSI9qM_NzlChO_I0iJJV5R0kYCwmnoUGI3_SijAcDR_yiymH8AjKNNmRKk9bFhARXl3QxbOUAEmhLJiKfyHnhQzdPL0VeyzG2vn9FFPoveMFPuxmn-biiz2xgNCv8JLmAk_pStdpGGuALsqTUZ1yQZOl0H5uH_k1KfmFSxgjge7IMRfr1piS92e3_J2j7zt0qU0__D5IxPqW76ilmGv0qY4zYcbkcYA2MlSqVKWfZCb2-ZNoW-X9OeHcSwKa3Q59-iPfcWfbAdFTKwOzXYqAAS0Dc-frGGk03NGowUJqSnoN7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c763a585fa.mp4?token=ox8UGbNaWBNSliFFG1rPwscv4YahdqM4ijrqh0lXwSI9qM_NzlChO_I0iJJV5R0kYCwmnoUGI3_SijAcDR_yiymH8AjKNNmRKk9bFhARXl3QxbOUAEmhLJiKfyHnhQzdPL0VeyzG2vn9FFPoveMFPuxmn-biiz2xgNCv8JLmAk_pStdpGGuALsqTUZ1yQZOl0H5uH_k1KfmFSxgjge7IMRfr1piS92e3_J2j7zt0qU0__D5IxPqW76ilmGv0qY4zYcbkcYA2MlSqVKWfZCb2-ZNoW-X9OeHcSwKa3Q59-iPfcWfbAdFTKwOzXYqAAS0Dc-frGGk03NGowUJqSnoN7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول أسعار الوقود: لا يمكن أن نسمح لإيران بامتلاك أسلحة نووية، عد الانتخابات، ستنخفض أسعار النفط بشكل كبير.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89942" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89941">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b379fbf2a.mp4?token=vpJrHJWVTYhW0AWDWxNt-jWN4foVlvPzkTEEhuDdHRdCS0um6HVxBgdr5-ElwfzhZ285Egwcw3cBFayyXparGqvmvgozZ7EOYQm090MUjc4foAgvCoLvz3OEGheban4NBg0byaQpzs0eSSmMsssNr1tNxYbujiYXLFWhCqlEG9RT3KKTjf2lGgt8dvKnhioawgt4psADQazhmKD34I4x-8AoaM8pnBF0q_MVkydeZJMS8K-kdbDwJlo8P7YSd-Tk-TQM6KLd7B52J0oR_9nYz46DTD497bHqHd9SPoI-HEyAT6DDXwPg9gFHgpnlbEM7XrMr4z75d9MPXpKQAJy4yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b379fbf2a.mp4?token=vpJrHJWVTYhW0AWDWxNt-jWN4foVlvPzkTEEhuDdHRdCS0um6HVxBgdr5-ElwfzhZ285Egwcw3cBFayyXparGqvmvgozZ7EOYQm090MUjc4foAgvCoLvz3OEGheban4NBg0byaQpzs0eSSmMsssNr1tNxYbujiYXLFWhCqlEG9RT3KKTjf2lGgt8dvKnhioawgt4psADQazhmKD34I4x-8AoaM8pnBF0q_MVkydeZJMS8K-kdbDwJlo8P7YSd-Tk-TQM6KLd7B52J0oR_9nYz46DTD497bHqHd9SPoI-HEyAT6DDXwPg9gFHgpnlbEM7XrMr4z75d9MPXpKQAJy4yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول أسعار الوقود:
لا يمكن أن نسمح لإيران بامتلاك أسلحة نووية، عد الانتخابات، ستنخفض أسعار النفط بشكل كبير.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/89941" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89940">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
🇮🇶
ماذا حدث في سمنان بايران   تتلخص الحادثة في شجار نشب بالقرب من سكن «نيكان» في شارع كارگر، بعد أن كان أحد الأشخاص الإيرانين في حالة سُكر مع بنت إيرانية سكرانة ايضا ، حيث دخل في خلاف مع عدد من الطلاب العراقيين من دون أي استفزاز أو خطأ من جانبهم ، ثم تطور…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/89940" target="_blank">📅 21:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89939">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇾🇪
🇸🇦
السعودية تعترف:
انصار الله هاجموا الأربعاء مدن "خميس مشيط" و"أبها" و"جازان" السعودية بصواريخ باليستية وطائرات مسيّرة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89939" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89938">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03c8641d.mp4?token=ss_euObBAbWzOeTjU2AdNuZLSNJWefEOfNKdcdQ__cUSpn8ZnB7ev6EdNSAYh71MH5kyU-SOEEYNVN-LzTUhIVvQoF4cEGuF3xtVZRKIaj_kIU8O78cBjxV4ghz6v5H9xUiuTd3ORoGveIQq2tUo-UDAGRCeHZqrlTvROs08RJjSISSCSZZdUk8CYNg5kJdwm-ljbY4e5WN-JbsmfuRXt1EcSAR9NVBN8lKEqW8TpOQ2iDfegsrU54aCVPzZ2PWRX1AObXNwBggR_rqgqwe6ioWamIiVUSqD__jEPy6A9XQsue660YS8YxnoPAODoSdot4M56ruYjYKv0DusUqb9Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03c8641d.mp4?token=ss_euObBAbWzOeTjU2AdNuZLSNJWefEOfNKdcdQ__cUSpn8ZnB7ev6EdNSAYh71MH5kyU-SOEEYNVN-LzTUhIVvQoF4cEGuF3xtVZRKIaj_kIU8O78cBjxV4ghz6v5H9xUiuTd3ORoGveIQq2tUo-UDAGRCeHZqrlTvROs08RJjSISSCSZZdUk8CYNg5kJdwm-ljbY4e5WN-JbsmfuRXt1EcSAR9NVBN8lKEqW8TpOQ2iDfegsrU54aCVPzZ2PWRX1AObXNwBggR_rqgqwe6ioWamIiVUSqD__jEPy6A9XQsue660YS8YxnoPAODoSdot4M56ruYjYKv0DusUqb9Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر امني...
أصوات الانفجارات التي تُسمع في محافظة أربيل شمالي العراق تعود إلى إطلاق ألعاب نارية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89938" target="_blank">📅 21:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89937">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇷🇺
🇺🇦
رئيس وزراء النرويج:
طائرة زيلينسكي كادت تتعرض لضربة بطائرة مسيّرة أثناء توجهها إلى أوسلو.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/89937" target="_blank">📅 21:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89936">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T40RcRI2wKB92B6ulKEbFk0Eve98jEFxqMwqHZe8F9Kg4a81WnQP-sHpkLTjJ7m96JhcRwygXM1tx0X-cBjK9q4k92u-9H75N80jK_LoqiA9fhk19G-NvSLV9etI3qOR5_GPPwUOyBJ709TY0Ku4DxdSU3QmTSsLF4W9nJyRtlem2jjO2NZYFFxgAuhxlRZUWkJL71Ga2FCg2iD26parUziZk6KIGT7poWWRhavnsg04PEksLm69to9Hb6ScN0Zy6SQJ1f5h7xvpWnkbfxIBFPveoCbs0jhIIVjfeqx-qwZfqouS7ZgqLi_dAWjkxbSjejhundbecTynXTIDEVfdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
شركة «أبل» تطلق هاتفها الجديد iPhone 18 Pro Max.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/89936" target="_blank">📅 20:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89935">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
سمع صوت انفجار من البحر في جنوب مدينة جاسك</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/89935" target="_blank">📅 19:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89934">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇷🇺
🇨🇳
🇮🇷
صوتت الصين وروسيا ضد الجهود المبذولة لممارسة الضغط على إيران في وكالة الطاقة الذرية الدولية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/89934" target="_blank">📅 19:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89933">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29b3df097.mp4?token=txpahwEkP76MVWSuny6C3QOGPpFWyFEPZIdWAXXAcavHqOpeQ5VnBWbwhvdtRvx4Z6SFrnQeezL6kEa9mTNhYvIUDEFB0l_C69zqKX9ps1monn5sTHQejcM3IFojTZlqg-YHN9ZdF5EPvKHB0e6lrQwL9ErwD_rQ8sYsuULX8aystk0Ja3juH68K-SpLJEjSj93O3Sq5tQx5Dte9fyzB1Leo_WPEgcJM_p37PBVs8Ht2bb8umIpgX0VsFU-j8OpHqh8gEnnHtJlmoGziIbaFmLUlKWTVkTSEfMzmYdUgqqLVuAgPlbBSCsOeQnPLpxJN86qrNSwAgfK5xORbX1GvpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29b3df097.mp4?token=txpahwEkP76MVWSuny6C3QOGPpFWyFEPZIdWAXXAcavHqOpeQ5VnBWbwhvdtRvx4Z6SFrnQeezL6kEa9mTNhYvIUDEFB0l_C69zqKX9ps1monn5sTHQejcM3IFojTZlqg-YHN9ZdF5EPvKHB0e6lrQwL9ErwD_rQ8sYsuULX8aystk0Ja3juH68K-SpLJEjSj93O3Sq5tQx5Dte9fyzB1Leo_WPEgcJM_p37PBVs8Ht2bb8umIpgX0VsFU-j8OpHqh8gEnnHtJlmoGziIbaFmLUlKWTVkTSEfMzmYdUgqqLVuAgPlbBSCsOeQnPLpxJN86qrNSwAgfK5xORbX1GvpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راح اكبر مشچبي
🚀
#قريبا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89933" target="_blank">📅 19:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89932">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
وكالة معلومات الطاقة الأمريكية:
انخفضت صادرات النفط من ينبع في السعودية بنحو 50٪ في شهر أغسطس مقارنة بشهر يوليو، وذلك بسبب الاضطرابات التي شهدتها مضيق باب المندب.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89932" target="_blank">📅 19:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89931">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">القوات المسلحة اليمنية ‏تستهدف منطقة حيس بالصواريخ الباليستية والطائرات المسيرة</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/89931" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89930">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
🇺🇸
دوي صافرات الإنذار داخل مجمع السفارة الأميركية بالعاصمة بغداد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/89930" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89929">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">#وثائقي
«الثأر العراقي»
«ملحمة العراقيين في حرب رمضان: ما بين المعلن والخفي» تفاصيل تحت بند سمح الان بالنشر ..
🔻
إنتاج: مکتب الاعلام والعلاقات لحركة النجباء فی الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89929" target="_blank">📅 19:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇵🇰
وزير الدفاع الباكستاني يعرب للجمهورية الاسلامية الايرانية عن أمله في التوصل إلى حل دائم للقضايا بين السعودية واليمن.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89928" target="_blank">📅 19:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇾🇪
🇾🇪
على خلفية تواصل الضربات اليمنية على ارامكو..
بلومبرغ: شركة داو الأمريكية تدرس الانسحاب من شراكتها في مشروع أرامكو السعودية البالغة قيمته 20 مليار دولار.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/89927" target="_blank">📅 18:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdafc6b1b9.mp4?token=Zmuos9VYy3bDAYH5hQVmbfLTrpZq05dHrqvDQ3030m1UK04WgoacsNP4810NlXAt8aDYcUPhiavC55BtIzmznZ0HzcwUIYTJ2qLM_QG5BGQjXhBEk95a0ic8MrJ5_-i8tu6F6INYi6EituSTk8Em8meYiFq2hd8A-7Z8jIXuVGnjgxtRImBmf-MfyJVDufnbxhBEiFbg8WHpmhz3Yf_aolLePf9S6aMeBPhpbjfa9TaKmYwrFm-2-R-H7B5K3DM_NQoyLrv9Pgb4bHxrlGs-v9ONri-_k4UIvbKk3NNoBuYMHcRVoKVuSUVejGV0GW1UHy-riIuykaArWReLYue1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdafc6b1b9.mp4?token=Zmuos9VYy3bDAYH5hQVmbfLTrpZq05dHrqvDQ3030m1UK04WgoacsNP4810NlXAt8aDYcUPhiavC55BtIzmznZ0HzcwUIYTJ2qLM_QG5BGQjXhBEk95a0ic8MrJ5_-i8tu6F6INYi6EituSTk8Em8meYiFq2hd8A-7Z8jIXuVGnjgxtRImBmf-MfyJVDufnbxhBEiFbg8WHpmhz3Yf_aolLePf9S6aMeBPhpbjfa9TaKmYwrFm-2-R-H7B5K3DM_NQoyLrv9Pgb4bHxrlGs-v9ONri-_k4UIvbKk3NNoBuYMHcRVoKVuSUVejGV0GW1UHy-riIuykaArWReLYue1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر لنايا:
رتل كبير للاحتلال الامريكي شوهد في قضاء الشرقاط ضمن محافظة صلاح الدين شمالي العراق ويتجه لجهة غير معروفة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/89926" target="_blank">📅 18:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89925">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIbFAY3RSYdp4u_GkkPNWOz5Bs81gEmwQpF8twMMp77Oiei1ehBEaxQYZeyKps4jjryou9JyucpiJgtvGlfBq_MHvGy-QtoSaQFTM7qPfNpINujJIOdasZ3hZSax0H5suDey2DtOcpME_aYj9q5L3EmMzmiTagiJuc81vs-9L9VQqFstmJTJdeeQJ19itRtFBfB1cmqKoZtIUzIa7ay6jPwg9dO6sKdmjPgGvGtkJCcsFw1_wdnJvmoOIj6emQA7ziQTNdCFjl0XRZK_8aS-D4zLJnrSBsp8b4bj-0oehymC17p8N7qqMiXxR85l0W3IsJuAbvKak4AXvofY2co9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تتجاوز الـ101 دولار للبرميل</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89925" target="_blank">📅 18:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89924">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات تهز ابها</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89924" target="_blank">📅 18:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89923">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇸🇦
🇵🇰
صحيفة تركية:
السعودية تطلب من باكستان التدخل والمشاركة في ضرب انصار الله.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89923" target="_blank">📅 18:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89922">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
وكالة الانباء الفرنسية:
تسارع في البناء بموقع إيراني محصّن على عمق كبير داخل جبل كولانغ قرب نطنز، استخبارات غربية تشتبه في بناء طهران منشأة غير معلنة لتخصيب اليورانيوم قرب نطنز.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89922" target="_blank">📅 18:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89921">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انصار الله يدكون نظام ال سعود</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89921" target="_blank">📅 17:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89920">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجارات تهز خميس مشيط</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/89920" target="_blank">📅 17:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89919">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/89919" target="_blank">📅 17:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89918">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89918" target="_blank">📅 17:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89917">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تسيطر على معسكر خالد وتتجه صوب مدينة المخا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/89917" target="_blank">📅 17:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89916">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">السعودية تعلن تأسيس
"صندوقًا لتأمين أخطار الحرب للبضائع والسفن" بالتزامن مع عدم قدرتها على رفع رأسها في مضيق هرمز وباب المندب.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89916" target="_blank">📅 17:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89915">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf-GR2ch3WWEgtDZnUP31ENodD5cJ_y7gGrSN_Mcy4HH7ge9rGaLB8TK7cGx9PorafRdkDFL20BZwcIlnFQfp88jntswqtj1yRXcH1vGeTt2Of_q9Q7619RIk9R1FxHp1G1qUG1acyqXmuq1D1e6J9VEFgBqbGRYU3Zky75wxm_Cj40ym5M1obImmM9iNqpANjIN_FbE368lc3vb15i0p6IS21hP63SobG7REhxRYpO8zAuvBSMZGEJ0z750Kon2SnVW-mhQg7FRHQJBLZcHjrelJqT7w_GB0ws25TYtQ9gnLIQpLvSibfkW-bpG_OWZO82IQI7KNg4dAzeknLQ2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وصول نتن ياهو الى قمة جبل الشيخ السوري وسط صمت عصابات الجولاني</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/89915" target="_blank">📅 16:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89914">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد أولية لضرب تحشيدات العدو السعودي شرقي الجوف وقتل وأسر عدد منهم وإحراق آلياتهم</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89914" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89913">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇸🇾
مجلس محافظي الوكالة الدولية للطاقة الذرية يغلق ملف عدم وفاء سوريا بالتزاماتها بعد موافقة سوريا الجولاني على النزع الكامل وبدون اي شروط او مفاوضات.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89913" target="_blank">📅 16:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89912">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مشاهد من الاشتباكات بين مرتزقة الامارات ومرافقي وزير دفاع مرتزقة السعودية في الضالع</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/89912" target="_blank">📅 16:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89911">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مشاهد قريبة من موقع الانفجار المجهول الذي طال مستودع ذخيرة في محافظة ادلب</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89911" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89910">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
الاعلام الامني العراقي:
بسم الله الرحمن الرحيم
﴿قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ﴾
صدق الله العلي العظيم
​استمراراً للنهج التعقيبي والضغط المباشر على ما تبقى من فلول الإرهاب، وتأكيداً للجاهزية العالية لقواتنا المسلحة البطلة في ملاحقة العصابات الإرهابية ودحرها ودك أوكارها أينما وجدت، وبناءً على معلومات دقيقة وردت من أبطال جهاز مكافحة الإرهاب، وبالتنسيق مع خلية الاستهداف التابعة لمكتب القائد العام للقوات المسلحة، وبعد عمليات رصد ومتابعة لحركة عناصر من عصابات داعش الإرهابية، نفذ صقور الجو بواسطة طائرات F-16 أربع ضربات جوية دقيقة استهدفت مضافات وأوكار الإرهابيين في وادي الشاي ضمن قاطع قيادة عمليات صلاح الدين، وأسفرت الضربات عن تدمير الأهداف المحددة بالكامل .
وسنوافيكم التفاصيل لاحقًا.
​إن قواتنا الأمنية بمختلف صنوفها وتشكيلاتها تؤكد لجميع أبناء شعبنا الأبي أنها ستظل العين الساهرة واليد الضاربة ضد كل من تسوّل له نفسه المساس بأمن الوطن واستقراره، ولن يكون للإرهابيين أي ملاذ آمن على أرض العراق.
​حمى الله العراق وشعبه العظيم.
​=====
مكتب القائد العام للقوات المسلحة
الإعلام الأمني
9 أيلول 2026</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89910" target="_blank">📅 16:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89909">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ناقلة نفط تعرضت الى ضربة ايرانية في الخليج الفارسي قرب سواحل دبي</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89909" target="_blank">📅 16:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89908">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇾🇪
🇾🇪
انباء اولية عن سيطرة القوات المسلحة اليمنية على معسكر قناو شرقي الجوف وتطهيرها من مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89908" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89907">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">▫️
هيئة التجارة البريطانية: بلاغًا عن حادث وقع على بعد 28 ميلًا بحريًا جنوب شرق الفاو في العراق. أفاد ربان ناقلة نفط بتعرضها لإصابة من مقذوف مجهول والطاقم بخير، ولم يتم الإبلاغ عن أي تأثير بيئي في هذا الوقت.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/89907" target="_blank">📅 15:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89906">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65365c285b.mp4?token=FqN6aUCUCYuY1QaBFIBu3QbxApARkyA3JkZxkY7vq4_l2pztHP2vpJrM22Dqf5gZpSJpLyezDhFr0Lk6sZdj7FCjPTXM_zpvvQHVnJr8mzBOruwuNQYuxExFW1-PxWNAkk4yooEH5BnesiW58j-xCyUnBrxb2XCLxxAF8Vp5RfYYZbb4JpQBcfezIt7PzVyGCajXblmaHnRd3-QCMtd_JLelAmZJz5PsbePnLs0P-NF9F-IFRE42_YRBUH0doWpdoYn-iicTmVUIMQGWQ5VGYh64AtZau1HNm5sWxKbHPOcqc7fM8A8euFX8fTMJHD1WB_tMLN9JjZJoGfDm2LQkGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65365c285b.mp4?token=FqN6aUCUCYuY1QaBFIBu3QbxApARkyA3JkZxkY7vq4_l2pztHP2vpJrM22Dqf5gZpSJpLyezDhFr0Lk6sZdj7FCjPTXM_zpvvQHVnJr8mzBOruwuNQYuxExFW1-PxWNAkk4yooEH5BnesiW58j-xCyUnBrxb2XCLxxAF8Vp5RfYYZbb4JpQBcfezIt7PzVyGCajXblmaHnRd3-QCMtd_JLelAmZJz5PsbePnLs0P-NF9F-IFRE42_YRBUH0doWpdoYn-iicTmVUIMQGWQ5VGYh64AtZau1HNm5sWxKbHPOcqc7fM8A8euFX8fTMJHD1WB_tMLN9JjZJoGfDm2LQkGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرتزقة الامارات يضرمون النيران بعجلات وزير دفاع مرتزقة السعودية ومرافقيه في الضالع</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89906" target="_blank">📅 15:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89905">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78da6df60.mp4?token=nCV18gWLM7z6V-x3uWVTiEbHgetMQ_e2XXVjSzGiVzWTZ_24lJXEudsTlGUFN5zB6j73_1GDi6gDv_jxV5Ofbvca0vW7TclVuqaT-lAf8qSYwl-V9AHZPwEaZPPv8zAfYEcLILnKbhkZSgFBVeIu8CfjpDumwAAWnikiCKRnruZ09__kgdzRGP22kUb5wqsWyX5q4u-yiU7aCFYxBf8D42g3i238O_6LLQNY6Vdppnv3r3ZdSPTJkA459Oe_J1Rk9qA8dJrJlkvFk2iLDBrm4nEsUM8YDkb2pSYyNXxVXuUSE4izdMPGxpROWAHLrqvSORES0NltGI64YzEIMUzwfpEjjugXteTgXgruAUpi_M_UP9Zi1VHt36_O43e7SpGC9SUnt0NtCQSME137I_omqp-DBfuSs4E73KIN3iUqAh1IOcKDEpS9dypEImR769fHuhJJbRjNROr1Ike80EZDOK711CBhsMPntOVwZQVIdZnPfnrCGWQM-giiy0VjaAx1L2H50StSuXSL3vkRJXEJyrlwtBnWDJad3Sg2I49TrdITzI2ENWvwF1MS2GzjNAQb6wCYCmH3eLX4h6vTBzrHFnoKLXTJ2atcF-9S1cfDtcxkhXDsM_lR74TgF1SiUdapqmBGWISBiNp2pWbGzCsfo5ZFu-ofKxz9BSHJhB4xmD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78da6df60.mp4?token=nCV18gWLM7z6V-x3uWVTiEbHgetMQ_e2XXVjSzGiVzWTZ_24lJXEudsTlGUFN5zB6j73_1GDi6gDv_jxV5Ofbvca0vW7TclVuqaT-lAf8qSYwl-V9AHZPwEaZPPv8zAfYEcLILnKbhkZSgFBVeIu8CfjpDumwAAWnikiCKRnruZ09__kgdzRGP22kUb5wqsWyX5q4u-yiU7aCFYxBf8D42g3i238O_6LLQNY6Vdppnv3r3ZdSPTJkA459Oe_J1Rk9qA8dJrJlkvFk2iLDBrm4nEsUM8YDkb2pSYyNXxVXuUSE4izdMPGxpROWAHLrqvSORES0NltGI64YzEIMUzwfpEjjugXteTgXgruAUpi_M_UP9Zi1VHt36_O43e7SpGC9SUnt0NtCQSME137I_omqp-DBfuSs4E73KIN3iUqAh1IOcKDEpS9dypEImR769fHuhJJbRjNROr1Ike80EZDOK711CBhsMPntOVwZQVIdZnPfnrCGWQM-giiy0VjaAx1L2H50StSuXSL3vkRJXEJyrlwtBnWDJad3Sg2I49TrdITzI2ENWvwF1MS2GzjNAQb6wCYCmH3eLX4h6vTBzrHFnoKLXTJ2atcF-9S1cfDtcxkhXDsM_lR74TgF1SiUdapqmBGWISBiNp2pWbGzCsfo5ZFu-ofKxz9BSHJhB4xmD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرتزقة الامارات يلقون القبض على مرافقي وزير دفاع مرتزقة السعودية في الضالع</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89905" target="_blank">📅 15:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89904">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b191540306.mp4?token=LAgwF8DTbke6OZ6NJ51q3h4CsG-flpmNL2suIWK76ZWz3Rr7FT5Q3xsml8GMDcsy-GUj0WATEy0A912dKtp054aBdPOJ8tUGGAgpzzS2GlKiBTE0ZBBA1-Y23SNdgvFpwX4lDn04CkVtLBs2o52lhCgLa4kn0pCYkHpgGKx-y2e-8V2f1SvILLp-WXkamn6_3vOQKQMT1VvJcP8pVDNPc2NTHCJqVuTYfNbLPFGK4rMF219ZonWMpSl-VS_aMHAPGOix5lxqmZB59el_OVR8wl1EXbunEPc6_zRsb5xhYcj87oGPJJZBXqsl7kP5fcpbASAA00gD46et02gPBtDsjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b191540306.mp4?token=LAgwF8DTbke6OZ6NJ51q3h4CsG-flpmNL2suIWK76ZWz3Rr7FT5Q3xsml8GMDcsy-GUj0WATEy0A912dKtp054aBdPOJ8tUGGAgpzzS2GlKiBTE0ZBBA1-Y23SNdgvFpwX4lDn04CkVtLBs2o52lhCgLa4kn0pCYkHpgGKx-y2e-8V2f1SvILLp-WXkamn6_3vOQKQMT1VvJcP8pVDNPc2NTHCJqVuTYfNbLPFGK4rMF219ZonWMpSl-VS_aMHAPGOix5lxqmZB59el_OVR8wl1EXbunEPc6_zRsb5xhYcj87oGPJJZBXqsl7kP5fcpbASAA00gD46et02gPBtDsjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطع جميع طرق الضالع من قبل مرتزقة الامارات لمحاصرة وزير دفاع مرتزقة السعودية طاهر العقيلي</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89904" target="_blank">📅 15:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89903">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة الرابعة عصرا مشاهد أولية لكسر زحوفات التحشيدات التابعة للعدو السعودي شرقي الجوف وقتل وأسر عدد منهم وإحراق آلياتهم.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89903" target="_blank">📅 15:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89902">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX8MpeAfiopALClKu-dK_mHyECVMsOe8GH4WWaK1OCBN9r316nWNbGQ-2bDayM1Wu1B4D5HHkHgmzJMiIFZYWrcPYrJbFd3ASl5lnHmegOQBP-Rx_jGYFAfwoMUa6wcxMTFkMfknaxdr7JfYJcU1eNVwfFWI-3BzYgrE2rKpjoBay9yc8erJX5uA4juHQa3E2xA3Gyu4YagTlGz3dSgkquPtBhLe-pTElBDRUmbOXAuPCXwN7yRg3MTKo5WBY0Y8k6QZuEQoW_bCFApaKaimnDfXJ1126p-e14nLzEfdxhxThAM5P7-HU4KwkPyANV24DfbwkayOI96BDFWY_w_JDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
هيئة التجارة البريطانية: بلاغًا عن حادث وقع على بعد 28 ميلًا بحريًا جنوب شرق الفاو في العراق. أفاد ربان ناقلة نفط بتعرضها لإصابة من مقذوف مجهول والطاقم بخير، ولم يتم الإبلاغ عن أي تأثير بيئي في هذا الوقت.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/89902" target="_blank">📅 14:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89901">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/120f95a63b.mp4?token=arzEo_V9UvJQK-r2csCyvnNHOX0F8T0XG8iBS_ALxxG77J38wcYSUAB7wjonMuKVzJKbk9flvKcE8oDUgmw27dnPgT6ENR3oJgzRWh74N5V1e6rn_42CZHGK7FiZqZDmdUi4W7fIN_ySazz6thjNfcOAbgEQgF56ksuYRxFObWMnNVJ8aIpkvUHLcolZ61J6kavFJOfTtC_cMibJe9SxZsJDWDWGmNZxhT9mQilPWpUuk3Qw_RljKkh3xYfF0ejd-P_IdXMVHIzF02P0ysrP-Lb53Tzt1g6A0A_9lv-0vfm0Z9Cc02s4d27DgaMFfJ5eSWpGhIcvLLoJbZdl86VzRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/120f95a63b.mp4?token=arzEo_V9UvJQK-r2csCyvnNHOX0F8T0XG8iBS_ALxxG77J38wcYSUAB7wjonMuKVzJKbk9flvKcE8oDUgmw27dnPgT6ENR3oJgzRWh74N5V1e6rn_42CZHGK7FiZqZDmdUi4W7fIN_ySazz6thjNfcOAbgEQgF56ksuYRxFObWMnNVJ8aIpkvUHLcolZ61J6kavFJOfTtC_cMibJe9SxZsJDWDWGmNZxhT9mQilPWpUuk3Qw_RljKkh3xYfF0ejd-P_IdXMVHIzF02P0ysrP-Lb53Tzt1g6A0A_9lv-0vfm0Z9Cc02s4d27DgaMFfJ5eSWpGhIcvLLoJbZdl86VzRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
هيئة التجارة البريطانية: بلاغًا عن حادث وقع على بعد 28 ميلًا بحريًا جنوب شرق الفاو في العراق. أفاد ربان ناقلة نفط بتعرضها لإصابة من مقذوف مجهول والطاقم بخير، ولم يتم الإبلاغ عن أي تأثير بيئي في هذا الوقت.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89901" target="_blank">📅 14:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89900">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بلومبيرغ : العراق يطالب بزيادة حصته من الإنتاج في منظمة أوبك
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/89900" target="_blank">📅 14:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89899">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">▫️
هيئة التجارة البريطانية: بلاغًا عن حادث وقع على بعد 28 ميلًا بحريًا جنوب شرق الفاو في العراق. أفاد ربان ناقلة نفط بتعرضها لإصابة من مقذوف مجهول والطاقم بخير، ولم يتم الإبلاغ عن أي تأثير بيئي في هذا الوقت.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89899" target="_blank">📅 14:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89898">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">▫️
هيئة التجارة البريطانية: بلاغًا عن حادث وقع على بعد 28 ميلًا بحريًا جنوب شرق الفاو في العراق. أفاد ربان ناقلة نفط بتعرضها لإصابة من مقذوف مجهول والطاقم بخير، ولم يتم الإبلاغ عن أي تأثير بيئي في هذا الوقت.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89898" target="_blank">📅 14:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89897">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات في مضيق هرمز</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89897" target="_blank">📅 14:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89896">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-yxN1vgQJ0JmhvrC6ub5frqFBOAxAnbe9j5ch3-QseqvkXrd7NYL7otSR1DEvS8nkBRfnS_xPDKe_Kmkvl_tKKPC8YnN8GhnFUF3sKRIoBn3k2sGTGX78sDq2z7sXWFjcqp4CQGYVooFQITbyOiZF1ZnvU2Y002E1QcV2K6rqAIV4NLW4pSYXSde7fbVqipE7m3vyHCGLAOGFqzNNfoTsPHDDWPNjzToYIaQp1nAR9pyG0WhlbDE5JiMbKDZr_SAUhJgJGznPA14yRYCpVpEtfiXn5EPb1iF7TgoLCJddCQUe5RGRMZgIuZtGbJd8Be6GeKLIV4Vx2PhKxzwss45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
هيئة التجارة البريطانية:
بلاغًا عن حادث وقع على بعد 28 ميلًا بحريًا جنوب شرق الفاو في العراق. أفاد ربان ناقلة نفط بتعرضها لإصابة من مقذوف مجهول والطاقم بخير، ولم يتم الإبلاغ عن أي تأثير بيئي في هذا الوقت.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89896" target="_blank">📅 14:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89895">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇾🇪
🇾🇪
المتحدث باسم القوات المسلحة اليمنية العميد يحيى سريع:
إن الجريمة التي ارتكبها العدو السعودي المجرم يوم الإثنين الماضي 7/9/2026 باستهداف السجن المركزي في مدينة الحزم بمحافظة الجوف والتى راح ضحيتها عدد كبير من نزلاء السجن مع عدد من الزوار بينهم أطفال ونساء فقد أقلعت عند الساعة 16:30 طائرة حربية نوع  F15-SA من قاعدة الملك خالد الجوية بخميس مشيط واستهدفت السجن بغارتين جويتين وعادت إلى نفس القاعدة فى خميس مشيط عند الساعة 16:45.
إن محاولات تنصل العدو السعودي عن جرائمه وعدوانه على بلدنا لن يعفيه من عواقب وتبعات هذا العدوان والإجرام مهما حاول التغطية على ذلك.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89895" target="_blank">📅 14:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89894">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04cb36b45c.mp4?token=jOTYgUsFUthzSTf1w-3P3jT2Fq5qNs_0mSW7CxavMmfWuTEL9WWhDDsLgpUPskmLT3iHBk2Xk3xVKpG1bbVR0Nhe6ofmc2uoXpyMYl0n47FUSTFwW_QdTCZw6SiCoQqtJ2wkkbsrrubvNx7OuFPB7DueIHS4R83qGtveC8RYERIdH6twu8Jn-H4bNgfErIW3d_A6kLY1EUbO8_I_NsxSZCp_rNuoGRZ-eWQ9eNf8x7-I9A7AN28S26S3H-D1qPc_eT-LxTJtCKRNo91s5Gcu9qIibZRnzeV1tjNuLpGJI0jC1dKB614Oh1hokWfCXpz1Iswwz_3R0UUn-g8H_-dK_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04cb36b45c.mp4?token=jOTYgUsFUthzSTf1w-3P3jT2Fq5qNs_0mSW7CxavMmfWuTEL9WWhDDsLgpUPskmLT3iHBk2Xk3xVKpG1bbVR0Nhe6ofmc2uoXpyMYl0n47FUSTFwW_QdTCZw6SiCoQqtJ2wkkbsrrubvNx7OuFPB7DueIHS4R83qGtveC8RYERIdH6twu8Jn-H4bNgfErIW3d_A6kLY1EUbO8_I_NsxSZCp_rNuoGRZ-eWQ9eNf8x7-I9A7AN28S26S3H-D1qPc_eT-LxTJtCKRNo91s5Gcu9qIibZRnzeV1tjNuLpGJI0jC1dKB614Oh1hokWfCXpz1Iswwz_3R0UUn-g8H_-dK_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرتزقة الامارات يقصفون معسكر عبود بقذائف الهاون وانباء عن هروب وزير دفاع مرتزقة السعودية طاهر العقيلي من المعسكر</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/89894" target="_blank">📅 14:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89893">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏مرتزقة الامارات يفرضون حصار على معسكر عبود في مدينة الضالع لتواجد وزير دفاع مرتزقة السعودية طاهر العقيلي داخله</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/89893" target="_blank">📅 13:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89892">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇵🇰
وزير الدفاع الباكستاني:
هجمات الحوثيين على السعودية قد تؤدي إلى تفعيل اتفاقية الدفاع المشترك.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89892" target="_blank">📅 13:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89891">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bb27f2bce.mp4?token=iqhgHeWWrmTxgXSi-e5M-_UlCQ2wZUt-wIPYgjesjbq9Ce-xixjNoz7ErbK96UqLKMebJ5zG65fRZMtwx7mxxD3uCz9VIGwNaQBjHQJlR5y3nQ4LqUjoDrHzhpcjiYZWzEbGWnnvzwSJ6X9oIpjrCs6apGmN2WghXeQB-zk8GUypQlDeJarH-QZTgAxTQE6bwZvufd1LjigCF0iHnpcngbCx5yh7jp4xyu-nwMRuJuBR9syTKigpPKRUrq1KhSxYC_x-0AmSh3yIC7Llo6noGT7wSbnQiuNRvnxlrcUIIdwfjYV5VXTUPc4VR0mUWw1mqLrkqWZjWXP8SFCBmkVAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bb27f2bce.mp4?token=iqhgHeWWrmTxgXSi-e5M-_UlCQ2wZUt-wIPYgjesjbq9Ce-xixjNoz7ErbK96UqLKMebJ5zG65fRZMtwx7mxxD3uCz9VIGwNaQBjHQJlR5y3nQ4LqUjoDrHzhpcjiYZWzEbGWnnvzwSJ6X9oIpjrCs6apGmN2WghXeQB-zk8GUypQlDeJarH-QZTgAxTQE6bwZvufd1LjigCF0iHnpcngbCx5yh7jp4xyu-nwMRuJuBR9syTKigpPKRUrq1KhSxYC_x-0AmSh3yIC7Llo6noGT7wSbnQiuNRvnxlrcUIIdwfjYV5VXTUPc4VR0mUWw1mqLrkqWZjWXP8SFCBmkVAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرتزقة الامارات يستعدون لاعتقال وزير دفاع مرتزقة السعودية طاهر العقيلي خلال زيارته للضالع</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89891" target="_blank">📅 13:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89890">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">توتر امني بين مرتزقة السعودية ومرتزقة الامارات في مدينة الضالع خلال زيارة وزير دفاع مرتزقة السعودية الى المدينة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/89890" target="_blank">📅 13:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89889">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e4a4414b.mp4?token=jC7d4ODcuamcEpqbBqI_gOibmhj6tOPFcsSJ2GF1rUKuVQs50Ad0xgESF4FzZIqscYJERTC3OKvd4OJ3tGNISY2XySe6ZrDJ9ksyxM7P8PKDE5nuQGz62j9UR8aKO-MXgLXmmof5w5ts9fFPfl6i14MG5Yg3FhbP5vP6LPp9v9X5eNqLxxKUl6FCy1crDKcvEbxdH91n23D4MKhWcwhyIN_U91amOQj-6G5LhVpHwP2Porspn51TxPTcz6xFIseAMZP71aAxm1TwAFVJeJIvjy2pHVJApzgX8kxHWckJsO3hsR1AhrAxQ9U1pjH0ylt3Fcev3x_Uy5tZIpN7KGFDiDHoY4Yi0OJ4EX5_IrBimwm07NSILVLITteUTe3WFISKLjLh6fznB5vjLKaQxX3RDizEhAisGBMlvog19NdIy8Jz0pQtMO05B5FwjfLju1GDnqw6-iLCLgNbWGa8ET13t6RPomAGN28ik-Wc8bILksrZ45V3SmolcVMHQ_CPqo-2TDq5oflISg6ix5Utudqa0jLuuFc-i2yQisGFHAv6V-zUBL3gr1t-skz0xWG848p1Egcnx5UWfc5_BQA9Tsu1IM3aj6TDSeEQOCBoIU3mcP9g7cedGqJlzf8_MJQXHIBEgVoOPQF1iWfKc7IwZD2BbJWrZoHQ42Zc1I-J8XkVvyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e4a4414b.mp4?token=jC7d4ODcuamcEpqbBqI_gOibmhj6tOPFcsSJ2GF1rUKuVQs50Ad0xgESF4FzZIqscYJERTC3OKvd4OJ3tGNISY2XySe6ZrDJ9ksyxM7P8PKDE5nuQGz62j9UR8aKO-MXgLXmmof5w5ts9fFPfl6i14MG5Yg3FhbP5vP6LPp9v9X5eNqLxxKUl6FCy1crDKcvEbxdH91n23D4MKhWcwhyIN_U91amOQj-6G5LhVpHwP2Porspn51TxPTcz6xFIseAMZP71aAxm1TwAFVJeJIvjy2pHVJApzgX8kxHWckJsO3hsR1AhrAxQ9U1pjH0ylt3Fcev3x_Uy5tZIpN7KGFDiDHoY4Yi0OJ4EX5_IrBimwm07NSILVLITteUTe3WFISKLjLh6fznB5vjLKaQxX3RDizEhAisGBMlvog19NdIy8Jz0pQtMO05B5FwjfLju1GDnqw6-iLCLgNbWGa8ET13t6RPomAGN28ik-Wc8bILksrZ45V3SmolcVMHQ_CPqo-2TDq5oflISg6ix5Utudqa0jLuuFc-i2yQisGFHAv6V-zUBL3gr1t-skz0xWG848p1Egcnx5UWfc5_BQA9Tsu1IM3aj6TDSeEQOCBoIU3mcP9g7cedGqJlzf8_MJQXHIBEgVoOPQF1iWfKc7IwZD2BbJWrZoHQ42Zc1I-J8XkVvyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توتر امني بين مرتزقة السعودية ومرتزقة الامارات في مدينة الضالع خلال زيارة وزير دفاع مرتزقة السعودية الى المدينة</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89889" target="_blank">📅 13:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89888">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a21fe1cac.mp4?token=ADXwLKPPjNIe9a22W3DRpx2o9pJZrBG-8w3R1QVpXnyW9o_xBNsHmIPB_CqpFsivGTPB7sPy_FlGeLwk4Gr3c7VaPynp89UxtsLkJKduf6SBzz5zTdQdAkChuPdL4H7cPwTbFI2s6nLOWGK-zkDyT3RcV7z2eQ7WoqOc2fThP8ZgyqHW1JEFUDp4gERFvysG61S2aBlkzyrUz7ptly_AuwwcU2_T5Bl5fn8tXjTz4-aymuNATDMdJv00sa_6GIec4vNOuRq2EYbLQ5Ki8TNSeZfVSF4LvWjzVc76itJTQ_hVM9U0TVQ4z5Kli1_tAL2mIeIwEF9qHKDNHHnEJeKVpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a21fe1cac.mp4?token=ADXwLKPPjNIe9a22W3DRpx2o9pJZrBG-8w3R1QVpXnyW9o_xBNsHmIPB_CqpFsivGTPB7sPy_FlGeLwk4Gr3c7VaPynp89UxtsLkJKduf6SBzz5zTdQdAkChuPdL4H7cPwTbFI2s6nLOWGK-zkDyT3RcV7z2eQ7WoqOc2fThP8ZgyqHW1JEFUDp4gERFvysG61S2aBlkzyrUz7ptly_AuwwcU2_T5Bl5fn8tXjTz4-aymuNATDMdJv00sa_6GIec4vNOuRq2EYbLQ5Ki8TNSeZfVSF4LvWjzVc76itJTQ_hVM9U0TVQ4z5Kli1_tAL2mIeIwEF9qHKDNHHnEJeKVpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدو السعودي يشن غارات على جنوب مأرب</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89888" target="_blank">📅 13:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89887">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
🇾🇪
اصوات انفجارات تسمع في العاصمة اليمنية صنعاء ناجمة عن اطلاقات صاروخية باتجاه المرتزقة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89887" target="_blank">📅 13:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89886">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ناقلة نفط تعرضت الى ضربة ايرانية في الخليج الفارسي قرب سواحل دبي</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89886" target="_blank">📅 12:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89885">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A05v35b3WegwCF0ctjiFSpKbwpCUZqD6lmZX0zdhNFocXWLciJ53T5u-0jZZcgv_mwquDQlq-rMxc0J_69L2EGysXmu7SNW_r_IvnSQVnE2f4ENa8OI4goSuO5qJA_RpJzS0eyjWqSsuGQRzqnsaUf8mcm9W5Y3NkziCcg5ov8n8708oX5ZSwajz3lT2BfyqJ0dmRopCMt0va4uKhEjQr6zCUJeie6JwDlZCaU0qiqu0J-N5xui2bQNihe_bG98uxcubLZ3ExAhZXWkSh5xDk65po48ylGJPi2XY8JF1h_u32jVfr2VIJ_HdZSBBlet6qSBCu7XL0A7z8XSWNXE9mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناقلة نفط ثالثة استهدفت قرب سواحل الامارات</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/89885" target="_blank">📅 12:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89884">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d80f3ae3.mp4?token=Ay_EilGz3h9xULQlm99-LSwn6DpAOZMFShGuvpiM5u8E6KbWEHqVGZHbYRS4NavG6wE1Awnd18l67aWE8GgHHmbLZ2SvJgTZlpBx1lhYawc7oewboyKNSCIJqT9Dv2mUOTTaqBFyTC3tQ-_8uoy4lqB3n7TlcoGqAuRzGSmJOfyBPuT0KVa2g0NY4A6qCEiStRE0e4sUGGHzp-xVUkTO6Db0UlKtm_TvuMu9a8aXw9Ql-u2w6SkHpK9HmSSXg_y2DKZdSw9Uioy9OaKpzbd61wRI4yg4Fu82Og4ozyDSqburzrh4GxnWXGGCl-6rnPnRdG1WyeFAu4uoni7JTHtTNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d80f3ae3.mp4?token=Ay_EilGz3h9xULQlm99-LSwn6DpAOZMFShGuvpiM5u8E6KbWEHqVGZHbYRS4NavG6wE1Awnd18l67aWE8GgHHmbLZ2SvJgTZlpBx1lhYawc7oewboyKNSCIJqT9Dv2mUOTTaqBFyTC3tQ-_8uoy4lqB3n7TlcoGqAuRzGSmJOfyBPuT0KVa2g0NY4A6qCEiStRE0e4sUGGHzp-xVUkTO6Db0UlKtm_TvuMu9a8aXw9Ql-u2w6SkHpK9HmSSXg_y2DKZdSw9Uioy9OaKpzbd61wRI4yg4Fu82Og4ozyDSqburzrh4GxnWXGGCl-6rnPnRdG1WyeFAu4uoni7JTHtTNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد قريبة من موقع الانفجار المجهول الذي طال مستودع ذخيرة في محافظة ادلب</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/89884" target="_blank">📅 12:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89882">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0efb6b14.mp4?token=maGM3TsKnkE47StidHQEol44NpVASA4mNsp52dtguxwLiYqXm0iL7-39UqyOwfnNd119lMbvTZDwuY74lex8H2tPZVnGdhM4e2qDIqfbrvC2XQI14WwTNecuq-hQwg_Zt7UW8aLKfygBLd9aty6RuMcuSYmDQEQZQXicLrGk6uyymHfCI4jIObB9zdZ4mmYwuY6qDlnexg_-p_XDlL4I1kiNPqTTc1nq-_xln8I-X7196vq_TWpLgQFo75n_MUzw8j-wdiHz7ciazFtc2a9ik6c58LRKNT2naUCvXua0dQ5xbQk0eSy1QVUSW_xaU-dL7_zAM-OjH5D05u2CgErxLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0efb6b14.mp4?token=maGM3TsKnkE47StidHQEol44NpVASA4mNsp52dtguxwLiYqXm0iL7-39UqyOwfnNd119lMbvTZDwuY74lex8H2tPZVnGdhM4e2qDIqfbrvC2XQI14WwTNecuq-hQwg_Zt7UW8aLKfygBLd9aty6RuMcuSYmDQEQZQXicLrGk6uyymHfCI4jIObB9zdZ4mmYwuY6qDlnexg_-p_XDlL4I1kiNPqTTc1nq-_xln8I-X7196vq_TWpLgQFo75n_MUzw8j-wdiHz7ciazFtc2a9ik6c58LRKNT2naUCvXua0dQ5xbQk0eSy1QVUSW_xaU-dL7_zAM-OjH5D05u2CgErxLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات قوية تسمع في محافظة ادلب السورية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89882" target="_blank">📅 12:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89881">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24720b384.mp4?token=LG5tvI368QK6DtZYnyVUf6C19JgUd76V706y-K5ro2ckzlwp5Y9zGOvWpxtVsC3qpnnfDj2-HvTsOQ57QhNiLJB3xeCQg694lUwemN5P6oNSVY-HFaVilva319DGcFnT-R33QPyCeQYXtqivXekxILIGv27xuslrgByxhRj_tctPhCSslWOzWjpayteOP5JMRp_E_cxLpi45CBVOU60cEGOWq-rg70AJHmGaJdGHi_3LXMe_J_e26x0CWt0o059XSXjRkG46r3DkdjqFzgO_-Qh06YbqBMg0m961CMiz6GRjw352V73JzX4fzWxCuxpeehddD0LHlXb1vE6nFv1GMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24720b384.mp4?token=LG5tvI368QK6DtZYnyVUf6C19JgUd76V706y-K5ro2ckzlwp5Y9zGOvWpxtVsC3qpnnfDj2-HvTsOQ57QhNiLJB3xeCQg694lUwemN5P6oNSVY-HFaVilva319DGcFnT-R33QPyCeQYXtqivXekxILIGv27xuslrgByxhRj_tctPhCSslWOzWjpayteOP5JMRp_E_cxLpi45CBVOU60cEGOWq-rg70AJHmGaJdGHi_3LXMe_J_e26x0CWt0o059XSXjRkG46r3DkdjqFzgO_-Qh06YbqBMg0m961CMiz6GRjw352V73JzX4fzWxCuxpeehddD0LHlXb1vE6nFv1GMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات قوية تسمع في محافظة ادلب السورية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89881" target="_blank">📅 12:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89880">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbce3efd84.mp4?token=SMISGfwxDnxOK_VFEw_50ISlFUVz117tAfzN9tneybxDV6YbxIEaR4BZBX6tvQl_zCjva6zk4q2dBvLctzO_xb-2xDMIn9wm4JKJUwwxQFZttzGl8BUsIjGW7s_3xOxq38ADBWge52_CJWNID9W6G26JH6Om5v15rO2hGKy1ueiCUPB89MsRCmHeLbjgvHAozFamLKIxzO9ar6Nl6VwgrxunzvpIJhoJSrt_IX2eR6yop7Oi4St_GiW3yKIT-pSsLbJR0SCXNW8eDnOKtFv6nKVshAnEBbRyrl0RDovyZRAzbSKcUp1hRZtqT3MCphMTBDzmKatFrXc0ehPA-7Mb5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbce3efd84.mp4?token=SMISGfwxDnxOK_VFEw_50ISlFUVz117tAfzN9tneybxDV6YbxIEaR4BZBX6tvQl_zCjva6zk4q2dBvLctzO_xb-2xDMIn9wm4JKJUwwxQFZttzGl8BUsIjGW7s_3xOxq38ADBWge52_CJWNID9W6G26JH6Om5v15rO2hGKy1ueiCUPB89MsRCmHeLbjgvHAozFamLKIxzO9ar6Nl6VwgrxunzvpIJhoJSrt_IX2eR6yop7Oi4St_GiW3yKIT-pSsLbJR0SCXNW8eDnOKtFv6nKVshAnEBbRyrl0RDovyZRAzbSKcUp1hRZtqT3MCphMTBDzmKatFrXc0ehPA-7Mb5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز مدينة إدلب السورية معقل الجماعات التكفيرية الارهابية في العالم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89880" target="_blank">📅 12:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89879">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aixi0oGjFghowgDyAHqaTtqfrhcIP4TPzISiDtyA2-Hmu0rplOJLJRIxNMfa2i5fvR_73NVTIlLBSHkYoTHnQFDQXaPr71LGRBo6mLrG9vsb6bGUinVk2RCN3Qc2r3hNakJ0a7sKXuw8DzJojpNQDm0xt465W-oYpLH0Yh1s_dh8zs_LI7EvSRGtWA0puaUPtyssv9AF-cSc9h-fuia4xZ150SLZINL8dqTs-xkgfpkTdR_ibE9R2vgtGnJhaBCX1l89KNHGeYk2YpKAr0J7Yn0yDN5McvLPa3xYHZbe7eDCqwFP6sUNsXPfLErt55xI0L16jI_qTZl5p3dTy3c2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر... عدة سفن تُستهدف في مضيق هرمز قرب خليج عمان.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89879" target="_blank">📅 12:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89878">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇸🇦
انفجارات قوية في خميش مشيط بالسعودية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/89878" target="_blank">📅 11:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89877">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
تحذير من محمد باقر قالیباف إلى "هيجست": الهدف التالي هو أصول الطاقة الخاصة بكم في المنطقة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/89877" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89876">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCAEhGAa5sr8tGs57RqQT_ati2_G-FWGbINGewe8pP9Q5_BUNaCJldkNJPw0ZW9HYH34mHpOeXj-NLQuEmNRA_Nq39aXxDpz95eiVbp0KueS1W2PqbqeSOZ41IH1FtFMPx-ghIoTDL1UZ1B6Rmp-fOkJ_ulB5EwvQ4Ym4PYUIyR3obO8bLKhOBf3i_iNMDuh834GpyZ9E6B_OrSY9Caw6E5p8Hd4BBCPkSc_f_9veo7TnVZA_Boku4SV-aR7yjPXryTkP-xaauT1_v73XGksoeTeLf8t3QKw2IuX0ce6OMemiaSVbkSed5tZjZmmdSHbR4DoSguWvoelHytImKXaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد ضرب مراكز الطاقة في السعودية وصولة الجمهورية الاسلامية ليلة البارحة واخيرا سعر خام البرنت يصل 100 دولار.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/89876" target="_blank">📅 10:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89875">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ناقلة نفط تعرضت الى ضربة ايرانية في الخليج الفارسي قرب سواحل دبي</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89875" target="_blank">📅 10:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89874">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/89874" target="_blank">📅 10:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89873">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇸🇦
انفجارات قوية في خميش مشيط بالسعودية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/89873" target="_blank">📅 09:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89872">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f90a670c.mp4?token=Pxj4ZsIHcH37Jedu0PSz2SNbDLKPufbBA_b7HjFo4HN2erHJE8M0XakkHMLcn2vOSWKlyqe5i2E6DOMPLw-s2nNPXPH2NCLZE4eGdtRsLWFwp4RZVDPMOZtEHh4h7a9_MC4VQHne6tWNXIgAZDAW9qIaettkTNNmXvdJxstl96IBLHCil8eOkkEFABH4aOnnvnIA_ABOlmowFXz706JA7cc9QfxPb_9O3itrguLfP4XMR1aKOW6zH4175DnLXr-5FjnRDYBrRU8tlShguEWXJeMU8W9j_dFNxPKRua0S1tSds29S1lKn20hg11rDo0FyLKI50XYuIG19w9XL3VrayQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f90a670c.mp4?token=Pxj4ZsIHcH37Jedu0PSz2SNbDLKPufbBA_b7HjFo4HN2erHJE8M0XakkHMLcn2vOSWKlyqe5i2E6DOMPLw-s2nNPXPH2NCLZE4eGdtRsLWFwp4RZVDPMOZtEHh4h7a9_MC4VQHne6tWNXIgAZDAW9qIaettkTNNmXvdJxstl96IBLHCil8eOkkEFABH4aOnnvnIA_ABOlmowFXz706JA7cc9QfxPb_9O3itrguLfP4XMR1aKOW6zH4175DnLXr-5FjnRDYBrRU8tlShguEWXJeMU8W9j_dFNxPKRua0S1tSds29S1lKn20hg11rDo0FyLKI50XYuIG19w9XL3VrayQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قراءة سريعة   بسبب كمية التوثيقات الواردة من الأردن مر هذا الفديو لكن للأسف لم يتم تحليله بشكل جيد   -نحن نتحدث على ان كل إطلاقة في الفديو الظاهر هو من منظومة PAC 3 التي تقدر بسعر ثلاثة ونصف مليون دولار للصاروخ الواحد.  -الفديو اظهر ان راس الصاروخ الإيراني…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/89872" target="_blank">📅 09:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89871">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/853992de9f.mp4?token=BXskjOOfFzmZI6VRPO6Prk_7JOzKCniF8joTtqU3pvD9r67xkYNxvyzmFV4NIT9XUH2OUcVJBTSzG4pGxORiGzocE8X7QjKUMiNcKkTK_4r9TCULnpJfHnReq3BoivyD2Woiabj46SYV4X6fcS4yNp0T5kyo2dAYxABBzW1r4HkLxWM75mMjsUrLJaXBpdmJHxgL_PqcpKfuEohBPzKXB27rjFVj2918voIm0zIrIeP1ioDdLvEOY_3S4ZorqrFG3I279wIybXyNT6kEVfQOVxWeaSd6fSwMjoDiI-TqhkUfIDsksZ7ElND4fA2udaWUdYo5g2Us6TNrdLfO2ZJf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/853992de9f.mp4?token=BXskjOOfFzmZI6VRPO6Prk_7JOzKCniF8joTtqU3pvD9r67xkYNxvyzmFV4NIT9XUH2OUcVJBTSzG4pGxORiGzocE8X7QjKUMiNcKkTK_4r9TCULnpJfHnReq3BoivyD2Woiabj46SYV4X6fcS4yNp0T5kyo2dAYxABBzW1r4HkLxWM75mMjsUrLJaXBpdmJHxgL_PqcpKfuEohBPzKXB27rjFVj2918voIm0zIrIeP1ioDdLvEOY_3S4ZorqrFG3I279wIybXyNT6kEVfQOVxWeaSd6fSwMjoDiI-TqhkUfIDsksZ7ElND4fA2udaWUdYo5g2Us6TNrdLfO2ZJf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
صور الأقمار الصناعية تظهر اصابات لبيت طائرات ال F15 الأمريكية في قاعدة الملك خالد نتيجة هجمات أنصار الله في اليمن ..
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/89871" target="_blank">📅 09:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89870">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇶🇦
إندلاع حريق في ميناء الوكرة القطري.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/89870" target="_blank">📅 08:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89869">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي بعدد من الغارات على محافظات مأرب والجوف وتعز والحديدة اليمنية.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/89869" target="_blank">📅 07:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89868">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
الحرس الثوري:
تم استهداف سفينتين أمريكيتين، و8 ناقلات نفط، و10 سفن مخالفة، كانت تهدف إلى العبور عبر المنطقة المحظورة وغير الآمنة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/89868" target="_blank">📅 05:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89867">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6a70ad2a.mp4?token=d8BcJpmUdMWMK-TKgxlIncUWXSeeuhE02Z5vzsus14LPwlqeddcWR_dnqnUvYVa5_o-9uYLNDz87zzLk4Xsk23n7-8YxHTqLIiRkgGBYyqiwb_EunVb2IhgHCdSJCeKK5ANcN-sgLibdznrAyEbH3_wEa1_EGtaeOSodVbjoepGGcNXI0PCZIydfCf1U_dkGynnCwJ8NgPiQwtosgo-4sK727masFK6gU1Uh6GFEZtztMSUWxWj99RDhd6VdLgkMt45QbbRag4XNLvvEN_sP8e_BvpFOdOZXfGpm6aFkO2zQzU8aHcjfgkDLY4880XimsyFTRrcu2OTs6FnuEwkisA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6a70ad2a.mp4?token=d8BcJpmUdMWMK-TKgxlIncUWXSeeuhE02Z5vzsus14LPwlqeddcWR_dnqnUvYVa5_o-9uYLNDz87zzLk4Xsk23n7-8YxHTqLIiRkgGBYyqiwb_EunVb2IhgHCdSJCeKK5ANcN-sgLibdznrAyEbH3_wEa1_EGtaeOSodVbjoepGGcNXI0PCZIydfCf1U_dkGynnCwJ8NgPiQwtosgo-4sK727masFK6gU1Uh6GFEZtztMSUWxWj99RDhd6VdLgkMt45QbbRag4XNLvvEN_sP8e_BvpFOdOZXfGpm6aFkO2zQzU8aHcjfgkDLY4880XimsyFTRrcu2OTs6FnuEwkisA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد متداولة لإنفجار في مياه الخليج الفارسي يعود لإستهداف سفن أمريكية من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/89867" target="_blank">📅 05:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89866">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ec42e3c6.mp4?token=fk-UxZroALKGV2s4Kvt4cGbqDBgyu8M-6BIY7SoJKX6hUiJSPI-knIImmfJROVrgBtNfHzHrM7CZuwYwti8xHx1tLtm8hNW6O7QyIQCe_G44PCK7afJ6PiBARX76IzUpxhEBCZqqVVzeyv27vI2zP83J0F9md9cHpwwdvKGVBdLQ1fMe7Mw2KGN0Uv4cpIrOowGmZxB0P_zpn174HvqLIuz2y74WtzYPbHExvLrtTm2Yuan8aTC95eYtPWebn4cBE86bBJsGAbDGFH-gkUUG7zgEWGXUIYABMQtswLrfTAIi_T8uMKx9eIjFfTwYp9P1QSYMkXpDJq0zNMxjS_9uwlgCG6Iq1-TkL6lz0Kbmn_etZsNADULovY8N246BZPk9q6EB-QnF8_-K1g1l0Znnp2K_sJvAkB-LBXuoFZfeLNbGfnp_gVyi5xt7IIJOOQImPjuxIZdXBX5I_Rg88BZmUNdO3JeBBSQR7UPADnm-jZsEqdVgJm8uVsHgi_1rMrcl2VXV34vgeCWThHLjYDs8Cm2OjMZKv24grKtN7h1OnRYhTbcPCy79oTte8lYFtfjBt3nkqQ5xDjdqd60jYdrPQkcDB6Du-EdPfQHbojpYl6GTJpX4HaAwroSbmFzQ_8AMYxigYs_EmIyI_Xh_XErZSJTNYaJmq7nk8pyLnHacTG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ec42e3c6.mp4?token=fk-UxZroALKGV2s4Kvt4cGbqDBgyu8M-6BIY7SoJKX6hUiJSPI-knIImmfJROVrgBtNfHzHrM7CZuwYwti8xHx1tLtm8hNW6O7QyIQCe_G44PCK7afJ6PiBARX76IzUpxhEBCZqqVVzeyv27vI2zP83J0F9md9cHpwwdvKGVBdLQ1fMe7Mw2KGN0Uv4cpIrOowGmZxB0P_zpn174HvqLIuz2y74WtzYPbHExvLrtTm2Yuan8aTC95eYtPWebn4cBE86bBJsGAbDGFH-gkUUG7zgEWGXUIYABMQtswLrfTAIi_T8uMKx9eIjFfTwYp9P1QSYMkXpDJq0zNMxjS_9uwlgCG6Iq1-TkL6lz0Kbmn_etZsNADULovY8N246BZPk9q6EB-QnF8_-K1g1l0Znnp2K_sJvAkB-LBXuoFZfeLNbGfnp_gVyi5xt7IIJOOQImPjuxIZdXBX5I_Rg88BZmUNdO3JeBBSQR7UPADnm-jZsEqdVgJm8uVsHgi_1rMrcl2VXV34vgeCWThHLjYDs8Cm2OjMZKv24grKtN7h1OnRYhTbcPCy79oTte8lYFtfjBt3nkqQ5xDjdqd60jYdrPQkcDB6Du-EdPfQHbojpYl6GTJpX4HaAwroSbmFzQ_8AMYxigYs_EmIyI_Xh_XErZSJTNYaJmq7nk8pyLnHacTG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي ينشر مشاهد يزعم أنها لإستهداف ناقلة نفط إيرانية في خليج عُمان.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/89866" target="_blank">📅 05:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89865">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89865" target="_blank">📅 04:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89864">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/89864" target="_blank">📅 04:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89863">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مصدر اردني لنايا   تم نقل عدد كبير من الجنود الأمريكان الجرحى وهناك اصابات ميئوس منها باتجاه قاعدة درمشتاين في المانيا نتيجة اصابة قاعدة الأزرق والمفرق بالصواريخ الإيرانية ..</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/89863" target="_blank">📅 04:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89862">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
سماع دوي إنفجار في مدينة كنغان جنوبي إيران.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89862" target="_blank">📅 04:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89861">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا.. لحظة انقضاض صاروخ إيراني وتحقيق إصابة دقيقة ومباشرة داخل القاعدة الأمريكية في الأردن.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/89861" target="_blank">📅 04:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89860">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ff3d240b.mp4?token=R6TNzcYhW3sLW_6pAfmmZ6OuaYUI1GXTuMKlJrDONGvG34r1dBGnzvTJvymCod8KnWHNgeFY81-My9LSFmqJsjy0aZmv6T5V8wbP0h9rlcPegzCFWnIin6ugYKT41fWzfhMHRH-d0uSJs96y8l8Mc6hKjSldYYfaOFG62yAF1P2HjcQZfjWUbxz-5Ij7YE88fPr_DDoYSET9JbDqpCuojz1DFFKSNevZw6U-3oCdDJxdWfDG-7RYXaRubcNx5AKZdtQW45dKUKVllesmXxHTLlJl7LHc0b09LhG-JgbMBuS3dGpndjxCsdJJOUs4byBSmTtQb3TGwotAya69pfnV6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ff3d240b.mp4?token=R6TNzcYhW3sLW_6pAfmmZ6OuaYUI1GXTuMKlJrDONGvG34r1dBGnzvTJvymCod8KnWHNgeFY81-My9LSFmqJsjy0aZmv6T5V8wbP0h9rlcPegzCFWnIin6ugYKT41fWzfhMHRH-d0uSJs96y8l8Mc6hKjSldYYfaOFG62yAF1P2HjcQZfjWUbxz-5Ij7YE88fPr_DDoYSET9JbDqpCuojz1DFFKSNevZw6U-3oCdDJxdWfDG-7RYXaRubcNx5AKZdtQW45dKUKVllesmXxHTLlJl7LHc0b09LhG-JgbMBuS3dGpndjxCsdJJOUs4byBSmTtQb3TGwotAya69pfnV6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا.. لحظة انقضاض صاروخ إيراني وتحقيق إصابة دقيقة ومباشرة داخل القاعدة الأمريكية في الأردن.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89860" target="_blank">📅 04:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89859">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b93bdcba2e.mp4?token=NQGFowjfpD2wdaQIoLG24oVx4BO2QbGFoGp0yjvSHTWiIhhgC1hePclw5gWGRo5CHRwR3GVMbK9afp0ccPqQbldGMOPuqeQY0tHLhz1xnKFts4G069YPh8uZod5C1iqGgaBmAa-WmKTz0-aJThUdEB9AkXorVNbF8nIUp5Zetz53R5441eqgolqexOV5Tjjv9xFkoYYBJtq0HS0Bz3P-u5-BOqQSCfpkboItBqmaQdeeFEsFhgeKnLLZ14IYBsq9I-Gm8CPqMK3jrhLocp9y6Kywov0Bav3P3l_xy0AuxaR9KMYfYqvl_HYbZeun7LLPoL4_tvjQgYBGuHzcrZm1OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b93bdcba2e.mp4?token=NQGFowjfpD2wdaQIoLG24oVx4BO2QbGFoGp0yjvSHTWiIhhgC1hePclw5gWGRo5CHRwR3GVMbK9afp0ccPqQbldGMOPuqeQY0tHLhz1xnKFts4G069YPh8uZod5C1iqGgaBmAa-WmKTz0-aJThUdEB9AkXorVNbF8nIUp5Zetz53R5441eqgolqexOV5Tjjv9xFkoYYBJtq0HS0Bz3P-u5-BOqQSCfpkboItBqmaQdeeFEsFhgeKnLLZ14IYBsq9I-Gm8CPqMK3jrhLocp9y6Kywov0Bav3P3l_xy0AuxaR9KMYfYqvl_HYbZeun7LLPoL4_tvjQgYBGuHzcrZm1OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد أخرى من الهجوم الصاروخي الإيراني الواسع على القواعد الأمريكية في الأردن.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89859" target="_blank">📅 04:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89858">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/771e5444d9.mp4?token=VKlIUMq-qUehjaGV_0tOPe7OHv3rFshpmxFfuiYxgEucOeHN8gA-Z6g8Ubm7VhqMToFZIcNYortjeCS40QxPh8vQ9m0W3ekCRXOretGEoKeYz-q9lICxKaT7Nh6ltBZgm2ne389zDNwZsm-QDsEctX7kXjx83pEm9SJICrB4yZNi4YxvnXJmuCLukvo7gpUUzjH-R_ET5iMfqZBa-rQ6KmuRIjNhzr4zDY7PfdWhWpDGQytU3cBCfZXn9vyjjHk-cqijgZYhs9seW8PwnAF_2MapmxkoIyJMmPmclrIYYKoN5q2y264yS4ULSybfOi8YTJg6l-gu-WaY-3HxzpT7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/771e5444d9.mp4?token=VKlIUMq-qUehjaGV_0tOPe7OHv3rFshpmxFfuiYxgEucOeHN8gA-Z6g8Ubm7VhqMToFZIcNYortjeCS40QxPh8vQ9m0W3ekCRXOretGEoKeYz-q9lICxKaT7Nh6ltBZgm2ne389zDNwZsm-QDsEctX7kXjx83pEm9SJICrB4yZNi4YxvnXJmuCLukvo7gpUUzjH-R_ET5iMfqZBa-rQ6KmuRIjNhzr4zDY7PfdWhWpDGQytU3cBCfZXn9vyjjHk-cqijgZYhs9seW8PwnAF_2MapmxkoIyJMmPmclrIYYKoN5q2y264yS4ULSybfOi8YTJg6l-gu-WaY-3HxzpT7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
خلافاً لمزاعم الجيش الأردني.. مشاهد تؤكد مرور الصواريخ الإيرانية بسلام ونجاح نحو أهدافها داخل القواعد الأمريكية في الأردن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89858" target="_blank">📅 04:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89857">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b5afb2b2f.mp4?token=ptV1_TmQedtCh3lWsug2sUGdwKJFhWUOlt8_nRmBoAGVQgQhhnEI_-9D_zKeswc58HNeQLWOZP3-C49FIkLnnTwPs6pHCvpq7fLLc5IJcGVlSzu-x7Pbrs9f97EwbLaEWuucY3zxzxHbLhI4ymJA8BQZ-XsIPeneFl5PVSVB_tGDJwx4XTg0eT5Cm0eQ5jVdB-iIrf5z7LZAQascsYeQb0sk98gjoV09GqGQzV3r5vM0XMRNO6vNEiy8JZW3ZaeVezunyantTYaNkBe5kpGs3Axx6c7GWxsmxN6HtaZKQE7As3EybxgqieKHG-A6Tp9i_wqi1RFKEsYhsue6KrDtvhNoQ0-u1i-8wvWcsvM6j3hjUc8d01UAVACHG5HgdLPL2j56jrmJudOB_-hGbNXHmd6H1ESE8SxxsjuR_3Y-HMw9_JiXGO2Rv6vmG3Aag7-9uFBtKWkYOKRA8DOB2bw4JjdZ-ezRF9kkN0cMwaZ85h2r-NNwec3DWRq1MNnIOxqDPz5EvEQ9CWv46lQ5o-YxLQPHqac2U6T4nZfDcc9RDkKFFNP0Ni7mQDto84R3tIs5k9YI8AJxm3QFuVvOcv33smgmnrlOXONSv4VSsLMcjkLWVZOBRAi_oq-IgPwMOidWOvRXAtRnQXqvZtZbDheYK5aZ0lX9PWhwPV8l-lJx-Lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b5afb2b2f.mp4?token=ptV1_TmQedtCh3lWsug2sUGdwKJFhWUOlt8_nRmBoAGVQgQhhnEI_-9D_zKeswc58HNeQLWOZP3-C49FIkLnnTwPs6pHCvpq7fLLc5IJcGVlSzu-x7Pbrs9f97EwbLaEWuucY3zxzxHbLhI4ymJA8BQZ-XsIPeneFl5PVSVB_tGDJwx4XTg0eT5Cm0eQ5jVdB-iIrf5z7LZAQascsYeQb0sk98gjoV09GqGQzV3r5vM0XMRNO6vNEiy8JZW3ZaeVezunyantTYaNkBe5kpGs3Axx6c7GWxsmxN6HtaZKQE7As3EybxgqieKHG-A6Tp9i_wqi1RFKEsYhsue6KrDtvhNoQ0-u1i-8wvWcsvM6j3hjUc8d01UAVACHG5HgdLPL2j56jrmJudOB_-hGbNXHmd6H1ESE8SxxsjuR_3Y-HMw9_JiXGO2Rv6vmG3Aag7-9uFBtKWkYOKRA8DOB2bw4JjdZ-ezRF9kkN0cMwaZ85h2r-NNwec3DWRq1MNnIOxqDPz5EvEQ9CWv46lQ5o-YxLQPHqac2U6T4nZfDcc9RDkKFFNP0Ni7mQDto84R3tIs5k9YI8AJxm3QFuVvOcv33smgmnrlOXONSv4VSsLMcjkLWVZOBRAi_oq-IgPwMOidWOvRXAtRnQXqvZtZbDheYK5aZ0lX9PWhwPV8l-lJx-Lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حيل ترفيهي  الجيش الأردني: أن منظومات الدفاع الجوي الأردنية تعاملت مع 20 صاروخا باليستيا أطلقت تجاه الأراضي الأردنية، وقد تم اعتراض وتدمير 18 صاروخًا منها بنجاح، فيما سقط صاروخان في مناطق خالية من التجمعات السكانية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89857" target="_blank">📅 03:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89856">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b559bb43b8.mp4?token=sr07fGWqqX6alVFxyurEoSrByyr4a30ZbvbbqCGW2rJY-SdA1s4_7uRF32xEA8Ep5XeczLrcmCcjVF_vlEUNGhLrb4K9EvPta2n_5BZwuQKEjFJ2uogB6jKh7MAYBpYpw4abkK6YQtBzPxHWnirdCRstzXXHzg1miUmxf83F6s89UX8X9HiKj63H2jNMdtezamMzpwoaHOQ7-8rJ1xWYHauy45UDIskaXfRuifF8zijp6aXyVTFJfm0YI_ngZjMbTtD1jF7H6xE3YyWJxBGlJyJ9jkNSxSASxd7WZqDPlBVp3SYBbo0RofBdxVriZWwm6T-iWWYG7zBdP2dpahXAYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b559bb43b8.mp4?token=sr07fGWqqX6alVFxyurEoSrByyr4a30ZbvbbqCGW2rJY-SdA1s4_7uRF32xEA8Ep5XeczLrcmCcjVF_vlEUNGhLrb4K9EvPta2n_5BZwuQKEjFJ2uogB6jKh7MAYBpYpw4abkK6YQtBzPxHWnirdCRstzXXHzg1miUmxf83F6s89UX8X9HiKj63H2jNMdtezamMzpwoaHOQ7-8rJ1xWYHauy45UDIskaXfRuifF8zijp6aXyVTFJfm0YI_ngZjMbTtD1jF7H6xE3YyWJxBGlJyJ9jkNSxSASxd7WZqDPlBVp3SYBbo0RofBdxVriZWwm6T-iWWYG7zBdP2dpahXAYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شكرا للشعب الأردني المسلم المجاهد   على دعم الهجوم الإيراني من خلال التصوير وتحديد مواقع المجرمين في الأردن</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89856" target="_blank">📅 03:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89855">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامب يعلن الحرب على كندا
اتخذ ترامب يوم الثلاثاء خطوة لتصعيد الحرب التجارية مع كندا بشكل حاد، ساعياً إلى منع استيراد بعض السيارات ومنتجات الألبان والكحول.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89855" target="_blank">📅 03:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89854">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzxtTHJPmAB9WHSU8Q35Ygr4OTMrbSrXM_L74WPpCV4aHg0o-W8Lc14KOUAqC2jd-ZiwGfzxwv6XqrLl80m8VimK0TjdZfNlP2zy0AVidczPVqMHHJG70Nij7sBh-68-gD0zeJ8hum3c8XnEBRPyjMeWSeJ5YK36LSt6Fc3Z1WCnjhmhixmi76q5K9R-Dq6XUwgsmD94XvLO7z0aEUQNQiQssrOhSTdVdwgwfMTSOM8ayotmXXopP8Zrq6pXLDsXg3ZRi7wxlBIe_8e3gbvPVE2niQCYti2RwEnoxRKLyDQ3rn6fNVnhYgGdBIYUo1K1TXJqIOpRY7VySTKlY0sI1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يهرب عن التعليق من الضربة الإيرانية ؛ واو! الحزب الشعبوي في ألمانيا حظي بليلة كبيرة جدًا. لقد سئموا أخيرًا من قوانين وأنظمة الهجرة الفظيعة للغاية، والتي ألحقت أضرارًا بألمانيا بشكل كبير. إنهم في تصاعد، ولن يقبلوا بهذا الأمر بعد الآن!
اجعلوا ألمانيا عظيمة مجددًا!!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89854" target="_blank">📅 03:23 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
