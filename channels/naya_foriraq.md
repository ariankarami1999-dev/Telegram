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
<img src="https://cdn4.telesco.pe/file/GvxqisiE4BDsb7729IOcG656uwSXrBVtWEpH3E4Li3me9dmtIzRG5LptYJqJUOCsLM83KGJboIFBR8zYb_0Ar4CcNRuQEYR255CcuMHOr3ZShrhUmwt6ReI-RlDplmPiDd04wmxKuKTTjNsqgkZvBLzigf0rgSxrkGEOjXBiL5lO5a2zfIrJajGD1CTl4UzLGDf3a1tEfZ85yNQfuvpeTZdjRhy23u4CRtetTPyawr3vpTeolnXqUW_fzXY8I2vpSw_-qqlb5C2UynuhFWU-X2NR3zL6b2vpqTWOtVpKGVLBbhklGSDaLt-F4-I38TMhhE0T_ojj64soGvRV1GA1IA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 251K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
البيت الأبيض:
الرئيس ترمب قال إن المفاوضات مع إيران تسير بشكل جيد وأوضح خطوطه الحمراء بشكل جلي.</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/naya_foriraq/76212" target="_blank">📅 17:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24bfca0631.mp4?token=OUSL_FpNaRoBkXTMZBiK_9_6RwmZys57N4e-PZWSiFlnQbewC4vsPQVcHCyjbQfe4MSYQcCcTlzFN3wDPyqiWzOfgJWlbB8pThYzZOzxMDou7o0I3ftYKPAff09kUbmWL47PdYPswuKsNvH7xyPNXu6hjgViK0Frt-egNB_v0_12AebPrSnBJcxl_f3TvqyamNHD3kT6-SsnXVtcZLT4sxBg7eSEhFSvby3wwdsvNRC2pYM5s_shz5x902Jl1ciPB9bDSX5crsFzv5TZz9-iBBF53v6av4oSr1lxF0133s4yknzF7K9zJyYXIzWLygOYq3NjzF1_T-l-cViS3Uj3X2GInrSX7CZDfoIv2tsimjEy919JqK4t9e0VDJ18NDMaJJUbsvVgLlG9ekzupVGFg-WfeNyttp4xjVGu-yj8fKLX1dt6RVe5MbnjPaBEh5DirFZdN85HftC1JRiZlfjZnOnePSz2dTR90lq-Vv2hyZC7zJMVw4RqUEHPf6xKtrvKXZICTpRD85CxYNAl065E2o7AmisKZLrlv0WGosGOSwbc6FS-DXcP76-zyiQeJ1pzfmXWyMx3yyYkPpcJa18VhwUk5QfglQWuO-xHR-DC8wO02E0AFcl6ABWR3Slu3Ec4geb9TJ30bn8k0Ka4IWtzlULS1M9J7yxaPWIUqXxNE4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24bfca0631.mp4?token=OUSL_FpNaRoBkXTMZBiK_9_6RwmZys57N4e-PZWSiFlnQbewC4vsPQVcHCyjbQfe4MSYQcCcTlzFN3wDPyqiWzOfgJWlbB8pThYzZOzxMDou7o0I3ftYKPAff09kUbmWL47PdYPswuKsNvH7xyPNXu6hjgViK0Frt-egNB_v0_12AebPrSnBJcxl_f3TvqyamNHD3kT6-SsnXVtcZLT4sxBg7eSEhFSvby3wwdsvNRC2pYM5s_shz5x902Jl1ciPB9bDSX5crsFzv5TZz9-iBBF53v6av4oSr1lxF0133s4yknzF7K9zJyYXIzWLygOYq3NjzF1_T-l-cViS3Uj3X2GInrSX7CZDfoIv2tsimjEy919JqK4t9e0VDJ18NDMaJJUbsvVgLlG9ekzupVGFg-WfeNyttp4xjVGu-yj8fKLX1dt6RVe5MbnjPaBEh5DirFZdN85HftC1JRiZlfjZnOnePSz2dTR90lq-Vv2hyZC7zJMVw4RqUEHPf6xKtrvKXZICTpRD85CxYNAl065E2o7AmisKZLrlv0WGosGOSwbc6FS-DXcP76-zyiQeJ1pzfmXWyMx3yyYkPpcJa18VhwUk5QfglQWuO-xHR-DC8wO02E0AFcl6ABWR3Slu3Ec4geb9TJ30bn8k0Ka4IWtzlULS1M9J7yxaPWIUqXxNE4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 26-05-2026 تجمعات آليات وجنود جيش العدو الإسرائيلي في ثكنة بيرانيت شمال فلسطين المحتلة بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/naya_foriraq/76211" target="_blank">📅 17:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76210">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e69coU2NHu2KH7rTDRtBA6RI_biLmXlCjJtMQefvcIc1xQm6ok4IltyX3ZzUS8fmggEeqYms-9mBs1quamIZdnMKADsGnOrCYFjhxBWz4HhWVjhr0wzjQvOToe43np8Bnf7qE4EAt02NCx_5jkUki7sal56UR14czEMKb7WssJWOqU8BK7uEUr_DnYQJ3x9bjPFflk_uam2YmsnLWv1DttOmUnT8Ubgft88hUPKpBcDx-iB8BPMYVRnvo9SwJlZ7SCiQpoNUfkkdqaNlAorUjwUj3rFLvzeHtKThAkqEmpV6Var8igIyDdt4pW6uilO4ow7ef0-fsb5WnvEnFsgb8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
اندلاع حريق وارتفاع أعمدة الدخان في القدس المحتلة.</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/naya_foriraq/76210" target="_blank">📅 17:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76209">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
🇮🇷
أفادت قناة N12 الإسرائيلية أنه من المتوقع أن تنتقل الطائرات العسكرية الأمريكية، بما في ذلك طائرات التزود بالوقود التابعة لسلاح الجو الأمريكي الموجودة في إسرائيل، إلى قواعد أوروبية في غضون 72 ساعة إذا تم توقيع اتفاق مع إيران.
‏ستعود طائرات التزود بالوقود التابعة لسلاح الجو الأمريكي إلى مطار بن غوريون إذا استؤنف القتال مع إيران.</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/naya_foriraq/76209" target="_blank">📅 16:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76208">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭐️
وسائل إعلام أوكرانية:
أرسل زيلينسكي رسالة عاجلة إلى ترامب يحذره فيها من نقص حاد في الدفاع المضاد للصواريخ في أوكرانيا.</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/naya_foriraq/76208" target="_blank">📅 16:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">التلفزيون الإيراني : القوات العسكرية الأمريكية ستنسحب من محيط إيران وتخفف الحصار البحري وفقًا لمذكرة تفاهم مسربة</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/76207" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">التلفزيون الإيراني : القوات العسكرية الأمريكية ستنسحب من محيط إيران وتخفف الحصار البحري وفقًا لمذكرة تفاهم مسربة</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/76206" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76205">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCbCshk1wcBsEIe_4I8sAD8SedTGnqaL6I1EPUv0Jd1BiWD-636x8BckrU_edEroJ3JPv5nIDTa3x-Do604-FBNhQdEkboCQIFk8gVifGbW2oL69H2yXtrNme6kpaBTQSuD6-SEL_vLepzwhYhZn10l6UluqTxFN_eusWU4FpL55PBzxL-fHv80_OlXKgghPRolR4UWGTsnAhnc4fx-BDyXTTbkQ1Isa11cSDJNYp7gVy6LxXdjBOczRoSBR_IZJ12POcJqDyxTAtV7B5JjIGT6qc_VVBkie_u4xbk_7No0SEnfxjXz9b8DCq8aN0kEmS8Bpmpb2h_xnOLJTqBZobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر
🏴‍☠️
مقتل واصابة عدد من الجنود الصهاينة في ضربة المسيرة في شوميراه.</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/76205" target="_blank">📅 15:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76204">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: إصابة بحالة حرجة جراء انفجار مُحلّقة مفخخة في شوميراه بالجليل الغربي.</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/naya_foriraq/76204" target="_blank">📅 15:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76203">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwGWB-9zSBOsIcfTSOjzY2LVNcGcNy1mZxSQYNXIwxOk5WlrGpfbAr6xqUDq88vr8TBwDssNUXVc3nytvJz_y8ztc-UfSCsDN6Zipd18H5Wn9kRfvgxl8yMTz0CGPd6qfvePDfhBthb1R4eg899qDj56q8c3oGrzSr-m_IeXthe829AHkY-BBBXpuy2Z8oq7OlK8RPRUlZ8hDOmLrdN3H6tTww313IpSNvov8_Ip97WSuE4IGxYcnTksJj-l0Ji4d7lQsn40Thi7QVdGD69UzpF3G9RhfvwHUFLi-DMn-hpL_RWCGUpOPOVhyqNdT35ApIOrndk0JosLe6JXLaC06w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزيدي يشكر مقتدى الصدر لتسليمه السلاح ويدعو باقي الفصائل لتسليم سلاحها</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/naya_foriraq/76203" target="_blank">📅 15:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76202">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
إصابة بحالة حرجة جراء انفجار مُحلّقة مفخخة في شوميراه بالجليل الغربي.</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/76202" target="_blank">📅 15:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76201">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في مستوطنة مسكاف عام على الحدود اللبنانية الجنوبية بمحلّقة
#أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/76201" target="_blank">📅 15:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76199">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSFwmWlMq63MxM17PvGROhEY5lSUSdQCrN76yVOcvaBtfXojPaWjkjoRVYSxYW250uWmWxgmc66N1ihFqTiulXrOv4ZqQbm1uAODxy0mwzJgJFILLMmWQVdGQ8ymtpzJ6d1HsWb6FOn-buEQw7NSk8qzJS8IJizA2RtwmY4-3EyKW4JAFy3uw2XqGAhRa5QjkZzcB619Om1_RyWGmGvOpu0yDYDi4MQKIUj773G91azfZGL5Kwd8tv48fftGEcBx5thlzuPPMDW2qrRwAjT6JdrPINxxorpDjIEbCHLAQul-p9rxTgs9gJ4qlFqZ-a8U5skBblsF-jR5QzKqBvEdCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7Dxn773BPC3e8bDpZJ8-TFIbVCtNnHK_gdKK4m0FQTMiiGZFzfMTqHp48hIDlCQLcVGrbD3IhtrpJVm7Vgw8qWJUij2JTO8-t6edZkrGGHV3IbZp6pnvnAccYxBVFe-PtcbBMz_FwUtpUmQP3V2X3V8I0plctS_feHCutLCYBSAC2kypfK1FDqN-BnNx3HCYHe-3ncQ-Rb_vkLux4NQiOpm0q8iH5NOdOYOXyMy-umoADfMXfClXrDPIykST2HYldZafp7EoBYmhQZTL7EmoPcramIxvUK6alCC0F1XrL5nzbPVwdM9NIJexLKSyVD5rR0KRi-_a4oBo9-nKnc2ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/naya_foriraq/76199" target="_blank">📅 15:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpE7hbGyct5NbXeNh2CH60V4YrF1Bk3LxpK8l6Da7un4zgVFIPuaht9EFS_ugLbjatdACAnOsOQL6dz03TxiKM8sdIKS7izOODX1J1oBsydjIkDl8qYSkLCIurWxKZ6L52x7QyBKfGrCqZkUjQ2ltDSj9Gb5vId2RE2cb7JJAW1bqC2QeE9IoWoX7np92590OIrNdky4I2We1pUp9Q7whpEGHlmxIXvWHC64ZAujf1WDiUT6jBXhKhIQoEEplR-XD9HxKzp-XVL793pBZ68hH9czmGbpPJLr900nWH_3LskVRuZ9mp6l1cxazhGlWemB5RUnCNFVO45n9oBbU31tWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/naya_foriraq/76198" target="_blank">📅 15:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76197">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ad79f15f1.mp4?token=ZUWX_c-bBGbAfbi-TcsEnGRL7V4caARTdIOfBU-mXQz_yFqcBWGc-t6uATcfp9LJq5moFbBNDPwM4GIb92PESSB9PXwEAO2yWErQFkKmiBwmCbGvsprCk_y67VPouCI1QDFg4ig10Y4Ne59QlenT4BD7pKxJJlQv-Ch_ZbF9dVxhPOOxNPCDJLuB4KB9M4BIcC7GlC7OzAbubRO7kO_hOVaZrUWwTafykg3e90XT1aaOr6tEk-uMqMzFzOpLYfN-FBbA5quclxegiKG-XOux6tHjth4aWVGmDpYMhI3mzuW3M15S_i08P_2emRomDmjAXZey8-J-802GF8MEWbq68g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ad79f15f1.mp4?token=ZUWX_c-bBGbAfbi-TcsEnGRL7V4caARTdIOfBU-mXQz_yFqcBWGc-t6uATcfp9LJq5moFbBNDPwM4GIb92PESSB9PXwEAO2yWErQFkKmiBwmCbGvsprCk_y67VPouCI1QDFg4ig10Y4Ne59QlenT4BD7pKxJJlQv-Ch_ZbF9dVxhPOOxNPCDJLuB4KB9M4BIcC7GlC7OzAbubRO7kO_hOVaZrUWwTafykg3e90XT1aaOr6tEk-uMqMzFzOpLYfN-FBbA5quclxegiKG-XOux6tHjth4aWVGmDpYMhI3mzuW3M15S_i08P_2emRomDmjAXZey8-J-802GF8MEWbq68g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات الجولاني تبحث مع ارهابي ظهر في عدة فيديوات يشارك في قتل واذلال العلويين سبل "تنمية مهارات الأجيال الناشئة ودعم الأنشطة الموجهة للأطفال".</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/76197" target="_blank">📅 14:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76193">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzrwiHBv3ZdUPg9D5hj-2b4cdiTiQHB8k6tCetK_7JSIgXQ-MaxBx7XABnoT7sjTn_jnpUHgh0ZODh_Z2sgUWfELQVgbgWsncA_JGU7FwrvrEdWS2bwRzS348XEoIzWXsebCTZfz9UelYakwJrZ5W2OvWtCUbBxppb1cMkaHRDyMAS9AwVOjf9GbRbFLAvBtfi96YH2xtCViJKy7m_JmYcFeug_0uWGkiJ8bRQyESHMIy-3AkI3j-o-iQlS3OrIS0-8W_KdwrjjwTsfLR_YQEjoW7wssLv3WMtv10SWngn0t7ysaICuLIyYiH9TonjdIP9zyk0jJKYYbEJOCQGi6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2jswaiIqWJSmXIwZgpbf68QJ0LgnZBjX-j6K7J_L7A31kcJSfRDjCCW7xJnrj2FYXtdodR5GiDPE9IAGdqrb8-n8DN3Hk7-i_3QOdlF-ZOKkAS-IUTp_-kyTdkbmkzuOW1ZXq5mSu0TL_QY8LWTqq0kdu0Z-JDpGZj_JO7y_zNr6Mw3FcMu_WbjQFvZleEtSxn5OZW7biGRuMhRTttzln7b48IfVP8-05wPYwHIM12afcvAFwnvCKMZSAEQJ2QwkU15qSUrycQY2FcLcjYSby0bTg2fFbeb6p5DRI_x2iERWMOPRrrPlEWYW6HqKD4ykxvZ_ASbjdwZQEdLburhlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jO6-oolcmOg_Bpl55YSBtkk1_WRAmSKv-AmRYyIoo9K9L0fy95ukjlG7i2yDObWLNZbtMq2Woy32g14dH-nVF9xZWP88OqkaV8tYi_jgAp6FrpfaOQ4HZ30jzw6aAjmiKkXX0kvDvHtCvx7TcP9Jr8zpMqp7nkv_biK0LuMZxcsxU1y9R03HY0jTzWkUDQrPUbJy8c4RE579rl3wDeGb8hqAy6UdlbOpX5CVjzDpPRfb_h8lrBW0zpIdYRq2Rkt0X2iJbGg2u6UnmvDBP3qD_JAyyWo3OMZwC1DNaObADjRIeY0K9V_bHBsFiCyTDbVW3BLUZZn6O5UxJojgG7C6Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0fe68efb0.mp4?token=gJLuaP_i2m3awUfAXCbZWeCAKyrubdqoui-rZW2wcOJANuWiNT-D6qOe75rgMqTkYHynHJWiI1BlTspzPUe4CwJHl1sF_Q8ahnqufrCOHTqkr4Wrjvu5VY-Lh9dWHsiRBba1EoiYqp-Of-EuaOVetx73i_ITuZJclqBSsmEFR2pwrX1CneRbfXa-bF482MQjpNePXfhL-GLBuWi_cltElwfwb2KAIhS3y4l7ubtyf1XD-2oWlD8Q2_abvHTHX25XMa2dcMhITe5nTWfD6CaMAe1hL6568Ff5kLbSqrBgSOwRfiWEmUBMr0zaJPP6cPc3s-U6YIdnPlOK_2LsOKX6OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0fe68efb0.mp4?token=gJLuaP_i2m3awUfAXCbZWeCAKyrubdqoui-rZW2wcOJANuWiNT-D6qOe75rgMqTkYHynHJWiI1BlTspzPUe4CwJHl1sF_Q8ahnqufrCOHTqkr4Wrjvu5VY-Lh9dWHsiRBba1EoiYqp-Of-EuaOVetx73i_ITuZJclqBSsmEFR2pwrX1CneRbfXa-bF482MQjpNePXfhL-GLBuWi_cltElwfwb2KAIhS3y4l7ubtyf1XD-2oWlD8Q2_abvHTHX25XMa2dcMhITe5nTWfD6CaMAe1hL6568Ff5kLbSqrBgSOwRfiWEmUBMr0zaJPP6cPc3s-U6YIdnPlOK_2LsOKX6OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات الجولاني تبحث مع ارهابي ظهر في عدة فيديوات يشارك في قتل واذلال العلويين سبل "تنمية مهارات الأجيال الناشئة ودعم الأنشطة الموجهة للأطفال".</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/76193" target="_blank">📅 14:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76192">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bF0clkPBaCRAcN-sNeEzE7n1K0AbaK4E4hoRJbGFh40dm5093WHjMlh4-7nWeslNpo4Y-m17o4pX3Z13OsoJD1WZ8AuqSBkADy1soTnKn34PS8zPA8BUD_Lwjtjf_Jhk2Z-iShdqMx6vSWkZMXlZsV5hBdetZh0KGeukYtoIqfwA0imoajJDuX1ltA8gv-nIh4wJurf23UxX0rEbz-n544LxvURu1E3OTn-ZYaT8qZhgUi6FSEUq7-sLiTbKTW9PV3REgAWKhBJZsXTpzgpI8fHXj2-xeMwPMnVSb1tVtHk-nd9fyjmftD10Pf1tDujMl8eX-RXL43gNLBXFstWYdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76192" target="_blank">📅 14:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76191">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea953b2d93.mp4?token=SA7VSr05JKZG1zh3w4n7UyksB8lcXyL-VniqyHv_1ELJdjfv-y2mFs250UWWU8FRKQvZjzf3uJcNSamJwkAL0w7cS9mu3hGu7em9iP0zmeWnR-6w8ESHGZe5LOQ_1U8jHLdL3VOlcy6Qd2OLNW795xly2G2eP1nizp63aRml2gBn_4R5XNrrhRCCEui3OrQJkKcEbL-nBEyW_KVNoKzoaW14C2rFhAO9Se1EHqvEufKpHM7wA9bMijfXngyobdkZ0bdPLMF4A4Qla2YGg9tTgCpZ1yWnsZmsgH8dUoeHMU4XbaXFuS7ej4YyV8XZHGwW7_E0liBXnm9IG1vGdELLgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea953b2d93.mp4?token=SA7VSr05JKZG1zh3w4n7UyksB8lcXyL-VniqyHv_1ELJdjfv-y2mFs250UWWU8FRKQvZjzf3uJcNSamJwkAL0w7cS9mu3hGu7em9iP0zmeWnR-6w8ESHGZe5LOQ_1U8jHLdL3VOlcy6Qd2OLNW795xly2G2eP1nizp63aRml2gBn_4R5XNrrhRCCEui3OrQJkKcEbL-nBEyW_KVNoKzoaW14C2rFhAO9Se1EHqvEufKpHM7wA9bMijfXngyobdkZ0bdPLMF4A4Qla2YGg9tTgCpZ1yWnsZmsgH8dUoeHMU4XbaXFuS7ej4YyV8XZHGwW7_E0liBXnm9IG1vGdELLgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجارات تهز مستوطنة شلومي شمالي الكيان بعد هجوم مسير لحزب الله</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76191" target="_blank">📅 12:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76190">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dC-l4OS90FishzoPXXCdu9HPlJ2SarBoT38xUMebS_Kk0y3StZf0370glf2nLXvJ-1-30aVjvYkqIB4p1PF_0SMb0vSR5e8Ca4XUnsR9GvPKBzl5jOnuP67mhd6s7VnvqAzmtthyWUu43bZqyBAxX3Q2OBF39XSeN1DDecjFJ66ECY4tjCSc1fxMnLHDN1aVLkp6cVViBpKvNQH9QETZOWzbadSFMJ6xmczjcadU9ySitjyy0GYWn6cXfveD65Sgys9HbSXDzha1n_n5_7yAcFGfw6J-WYy5F6u1whA6oNsU6GLoTFxSYW46yWtRKTvf2ZUgd5XxCFMfSq_4EN6dFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
حزب الله:
{فَيَكُونُ طَيْرًا بِإِذْنِ اللَّهِ} - [آل عمران - 49]</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76190" target="_blank">📅 12:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76189">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
حزب الله:
خلال تصدّيهم لتوغّل جيش الاحتلال الإسرائيلي في بلدة زوطر الشرقية، اشتبك مقاتلو المقاومة صباح الأربعاء مع قوات العدو من مسافة صفر وأجبروها على التراجع، قبل أن ينفّذ الاحتلال أحزمة نارية في المنطقة.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/76189" target="_blank">📅 12:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76188">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c126696196.mp4?token=i1j1dN7IH2oUWfFWKQuLp2aU3cwAjbM77qPYmYbx7o0UTtdvocimaum_Yc6LaSje5ynw2ExcLWUpOCreAjnnmquvPEB5rePx3rpMT6FSHUqSPeJWSLknF3ZzAJcAfHwwctADFRxMLiGptinXEOXrZzlkxhrCZ0SZ-_E9PbpqeCs_vVo0Rk5hzScdzBr3wvNLJiYmctdq4sNJ8MVeHDDgjfRU_sIAHlXCfxt_FayZBlAHHdwy4euvVM5ssj7AYS_pwvHfKsV49QfkO8v84_NgIfw18-pGeto2fnZCyJRKBsAE7hHom1V4no08Ty0qSWruV_zhcfODefQjVPncO0MNQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c126696196.mp4?token=i1j1dN7IH2oUWfFWKQuLp2aU3cwAjbM77qPYmYbx7o0UTtdvocimaum_Yc6LaSje5ynw2ExcLWUpOCreAjnnmquvPEB5rePx3rpMT6FSHUqSPeJWSLknF3ZzAJcAfHwwctADFRxMLiGptinXEOXrZzlkxhrCZ0SZ-_E9PbpqeCs_vVo0Rk5hzScdzBr3wvNLJiYmctdq4sNJ8MVeHDDgjfRU_sIAHlXCfxt_FayZBlAHHdwy4euvVM5ssj7AYS_pwvHfKsV49QfkO8v84_NgIfw18-pGeto2fnZCyJRKBsAE7hHom1V4no08Ty0qSWruV_zhcfODefQjVPncO0MNQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
‏
كوريا الجنوبية:
ترجيح بأن الهجوم على سفينة كورية بمضيق هرمز هذا الشهر كان بصاروخ إيراني، ونطالب إيران باتخاذ تدابير مسؤولة لمنع تكرار الهجوم.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76188" target="_blank">📅 11:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76187">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1g7-eWJwlyf_UMyUGhWnibuQI1L0PQ4A5D50cjylR5D41MBHYQMA_On80R-Mq-Bq0x2BaA-72mDsJLAx3mFK32GZAAxgK9C4RDcwre1BVQWwrrVfweu2u5JlH5YOuZ89zlO4E8_pUt5mM5pgkszlb2MLp3ib1auBpTUdZQ84qnoem20MX-8AdTN70O1csGe5LDoChOfOPGCOG2QgbgpmCdwGpo5Mr6MaKqqBPd_ZLYT7_49SNeH6wRCG_ob7h0XPp0kmhndyLdACT6GvlAt9y2eomJ-JlCIBVJ6sI8rVDp0wN7EcfDpIMIRR1srPBe5DGA-SLaynLnnmdK_EfMqyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد موافقة الحرس الثوري الإيراني.. ناقلة النفط المملوكة لشركة كوسكو، هوا لين وان، تعبر مضيق هرمز الآن.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76187" target="_blank">📅 10:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76186">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
نيويورك تايمز: واشنطن تعتزم نقل مواطنيها المصابين بفيروس إيبولا إلى كينيا للعلاج.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76186" target="_blank">📅 10:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76184">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTylP9ySgd0U4_eb4m0FCymN-X79eAvFOBca2qoSsvFxXiletR0G7Y5wwMjadddzFOLIbI0dyesin2vOca86V2LkuhtiWh7ur5aqoExTtoMttxi3Uk6bXkwLd8y5ylwlAdmoX50CmeD5WUkoY2CBftfEFPvNR0HBoozY0bRgPKY5s_QH_D9eOqt0mCDjTryv_CgzyyhFm67ColOCK7GqS4azH1vizcL85n90YoZ0uGUR9D602sPTIt94m12IXu9op5RbZCUVNSWqg-0aVAkNaQKJ_Om90GJ5gbCDk2BYWHc_ikXpG5vZ3TM4kRNfmruY8iwdXWCXcwXeLlA5jv-WKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8iMpUzW1Q7_4ePgnqmv4qOwia6LX3A_01_O6iXJib_W-aVkaYEMNgjRjHByf6SPgEMF_UhhB4VH2RLaqxui_QFhbSItc0xnYEbCtbkK-_fH83Z_fTgZxbWlbmkWb2qexojHqlIPMXkDYW45ZXwMaPUJKmRiAAyaf_JdVMOuAAL7wGXfWApJDz41_rb6DyhcCsAzSfO63u15Jh49svnUJFNQfB5X3_EYA0mq7DaLRyHWTu6ipnpYYpumziSWWxQ5kM2cCByzvB19cRFBVGNs8cOiciH-kQoOSxg4i4GaUsxdXK3fRDwH8C4WGvm8aD8egrAVE1nFjFaO8HyUq8rdwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">السيد مقتدى الصدر يطالب لندن بتسليم البعثيين والمندسين.. ويدعو إلى اعتذار رسمي من السفير البريطاني حسب السياقات الدبلوماسية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76184" target="_blank">📅 10:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76183">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
إن الوضع الحقيقي في لبنان معروف منذ زمن طويل، وهو يختلف تماماً عما تحاول الحكومة والجيش الإسرائيلي تصويره. فالحقيقة أن الجيش الإسرائيلي عالق: إذ توغلت قواته البرية في عمق جنوب لبنان، على بعد حوالي عشرة كيلومترات من الحدود الإسرائيلية، واكتشفت أنها معرضة هناك لخطر متزايد، وجديد نسبياً، يتمثل في الطائرات المسيرة المتفجرة التي تُشغل عبر الألياف الضوئية. كما أن هذه الطائرات تعبر الحدود تدريجياً وتطلق إنذارات في الجليل لجزء كبير من الليل والنهار، مما أدى إلى تعطيل الحياة اليومية تماماً في المجتمعات القريبة من السياج الحدودي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76183" target="_blank">📅 10:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76182">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: طائرة بدون طيار مفخخة سقطت على قواتنا في جنوب لبنان</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76182" target="_blank">📅 08:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76181">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
مابين الحرمين الشريفين.. العراقيون يؤدون صلاة عيد الأضحى المبارك بجوار أبي عبدالله الحسين وأخيه في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76181" target="_blank">📅 07:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76180">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6815935d0e.mp4?token=G5hTo82CAUNgrw9joQ1a1X2XEz_YVCxF8Mu4D43-NFPVHZ-nO2cC_-iEfpE2D_NKvmaCT6LlHzPWOGp5wmzyp2S1yLPgsLbDIBWyHr7L3Fazquumk1DoBYmONaq7up5dgtUlmH5oArPRc2DQmT3DjX6ku8TG6lpX0UlZm_YVJ-NguLF4RYL-XzTfUE7zTw4aTwXYiIpIPL-LR895KA4QrlyTvBk10YUCyQEwO0yGEvxiEhtVjjbc9AIFB9qvC6Py9Xw_AcGyKr8oMKrQhgyVV1lOaRbAtx0jAxUdmOMIzVE2YWF4iQjHrGvAndcxlENNSX57DE8qEYhEBddcN1As3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6815935d0e.mp4?token=G5hTo82CAUNgrw9joQ1a1X2XEz_YVCxF8Mu4D43-NFPVHZ-nO2cC_-iEfpE2D_NKvmaCT6LlHzPWOGp5wmzyp2S1yLPgsLbDIBWyHr7L3Fazquumk1DoBYmONaq7up5dgtUlmH5oArPRc2DQmT3DjX6ku8TG6lpX0UlZm_YVJ-NguLF4RYL-XzTfUE7zTw4aTwXYiIpIPL-LR895KA4QrlyTvBk10YUCyQEwO0yGEvxiEhtVjjbc9AIFB9qvC6Py9Xw_AcGyKr8oMKrQhgyVV1lOaRbAtx0jAxUdmOMIzVE2YWF4iQjHrGvAndcxlENNSX57DE8qEYhEBddcN1As3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارات إسرائيلية عنيفة على بلدة سحمر في البقاع الغربي شرقي لبنان.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76180" target="_blank">📅 01:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76179">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇷🇺
مبعوث روسيا لدى الأمم المتحدة، إلى دول الخليج بشأن إيران:
أنتم رهائن للسياسة الأمريكية في الشرق الأوسط. كنا نقول منذ وقت طويل إنه إذا حدث شيء من هذا القبيل، فستدخلون حتمًا في هذه الأزمة سواء أردتم ذلك أم لا.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/76179" target="_blank">📅 00:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76178">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urnnVD2l4SfffUgsuLlFxpLF36gpR6Ahj4156bnyZuUtMi7xNDk8UdFCbjnOhxbYUK5pyMTfTYindRXnZqyaZw79cd6KIWZp2Ann3i6vFOiHZtC4jTfYDOrwbVrwTa2nw5HgemJV3wR81YrGYtkubYLgpRhrB6Ru0tJ1442AK-JbovYSTeb70K0quk5xy1Ei2Zl97isau94ljqX1XrIDUbSQqjgY11BPtRruFiOKYnR3X1VRSwvLDlfcOpOT2TqV1WpHzqjjBla_nrhFwETZZD_um0k3D2YpOahSeXnfmTtf1OIneHOqG4krmBEkrRjNzQk6blmFQFHmqOjkTCZiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يبدو بسبب غلاء اسعار الاتصالات
ترامب يعلن عن الاجتماع القادم في البيت الأبيض بواسطة تغريدة</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/76178" target="_blank">📅 00:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76177">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">▫️
🇺🇸
قال سفير روسيا لدى الأمم المتحدة إن الولايات المتحدة رفضت منح تأشيرة دخول لنائب وزير الخارجية ألكسندر إليموف قبل جلسة مجلس الأمن التابع للأمم المتحدة، واصفاً ذلك بأنه انتهاك لالتزامات واشنطن بموجب ميثاق الأمم المتحدة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/76177" target="_blank">📅 00:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76176">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 26-05-2026 آلية هامر تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/76176" target="_blank">📅 00:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76175">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
26-05-2026
آلية هامر تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76175" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76174">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_j_2jc0kIE0GoJJ0Xm_e_phaJT1eUL34Gy1bt5k-BeEsJx4Y2armxjEhXbAV3bBmNm_tQolZUaR9JO9HuH6qACN4g84QNIpY2jnCjv_gTdMsR-PEWp9v6-RJG6nLONsYBnK1y8FsYqVWS9Eow667YFKv9FbwPIP_Yoo_4BVdXBKLnwaD-ZbPWt6vRJiWdc26O0nGEe_-yub12NNTVcDtAREfTMrD4OFp8jL8zdPk43ESRDeaOwWdf5gI1Plmvw-743iAbA8qLX26U2D70loz8JkRs0--i5lA6SZb3eg67MEQgBYXNbfVL_9D91_oytpf9kM2PoQcw-tOjJcocOIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إذا استسلمت إيران، واعترفت بأن بحريتها قد ذهبت وتسترحت في قاع البحر، وأن قواتها الجوية لم تعد معنا، وإذا خرج جيشها بأكمله من طهران، ملقين أسلحتهم ورافعين أيديهم عالياً، ويصرخون جميعاً "أستسلم، أستسلم" بينما يلوحون بعنف بالعلم الأبيض التمثيلي، وإذا وقع قادتها المتبقون جميعاً على "وثائق الاستسلام" الضرورية، واعترفوا بهزيمتهم أمام القوة العظيمة والمذهلة للولايات المتحدة الأمريكية، فإن صحيفة نيويورك تايمز الفاشلة، وصحيفة واشنطن بوست، وشبكة CNN الفاسدة وغير ذات أهمية الآن، وجميع أعضاء وسائل الإعلام المزيفة الأخرى، سيقومون بتغطية عناوين الأخبار بأن إيران حققت انتصاراً رائعاً وذكياً على الولايات المتحدة الأمريكية، ولم يكن الأمر قريباً حتى. لقد ضل الديمقراطيون ووسائل الإعلام طريقهم تماماً. لقد أصبحوا مجانين تماماً!!!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76174" target="_blank">📅 23:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76173">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
إنفجار خزان مواد كيميائية في واشنطن أدى إلى سقوط عدد من القتلى وإصابات بحالة حرجة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76173" target="_blank">📅 22:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76172">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135333f897.mp4?token=C-eR-YBWyCG5Ojeqc_ZGp5-flbvXXVAeGO3Y_0FwfFbBx1hMaCJDVMn5PWslzAHsO3JFtyj0Lqqx5X0MlCbJPH4-dJcl4MFlVSvo_b2nl6VfC7P3x_LzxiT-d8Ogb9oKjkCJIJTNQ6qsmq-JBrwN_2AH4ftmkkNanTHb-RyvEesy-CsM2WgCXNDvFvRpi-SBChXr0_RkVmupofFaOTUJFlDfXynzvZuGRD_K6z2ogUlfvG-2CjBqwVmS8lg97CcF0hcqoD1wwKg7m_6wvHgYpqoEKWD3nSRp1y57-twIpZ74snrUWQQ1fvef86DUQ3RQOfj0TFZ3GlJg9PXrzsUjxV6KqGM3qVQ_Ru7z9MJTLSzDkMtponnrCt9kvlX0W93lAnLleZYuyf5tIz1TeTFhm8j2ymAM-Y-qSzozAb630XD1mJB1QPJKbByAvUpT4GcFGGwW21_h0UeISSZLswbrLviz5qjCQbPfHcpYMo2uNTQZ9c5bQpaQtZkq9u9sDy2C8WKCRGoBcT5EAhAvre2TiwpsbFbRsKRG-KOt55gQbKqjO8g70IoXj-YBF7-iEx7q-5Di8IDjhn8bAkFTemRl7U1auYr6HcwvRpwDRVYQAdLy9Sjunq-maTh4DuZT2ifM-LmIKuDUcGC0Zqr27wv9Zc9N6K9ovT5NPmbGpFK_gY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135333f897.mp4?token=C-eR-YBWyCG5Ojeqc_ZGp5-flbvXXVAeGO3Y_0FwfFbBx1hMaCJDVMn5PWslzAHsO3JFtyj0Lqqx5X0MlCbJPH4-dJcl4MFlVSvo_b2nl6VfC7P3x_LzxiT-d8Ogb9oKjkCJIJTNQ6qsmq-JBrwN_2AH4ftmkkNanTHb-RyvEesy-CsM2WgCXNDvFvRpi-SBChXr0_RkVmupofFaOTUJFlDfXynzvZuGRD_K6z2ogUlfvG-2CjBqwVmS8lg97CcF0hcqoD1wwKg7m_6wvHgYpqoEKWD3nSRp1y57-twIpZ74snrUWQQ1fvef86DUQ3RQOfj0TFZ3GlJg9PXrzsUjxV6KqGM3qVQ_Ru7z9MJTLSzDkMtponnrCt9kvlX0W93lAnLleZYuyf5tIz1TeTFhm8j2ymAM-Y-qSzozAb630XD1mJB1QPJKbByAvUpT4GcFGGwW21_h0UeISSZLswbrLviz5qjCQbPfHcpYMo2uNTQZ9c5bQpaQtZkq9u9sDy2C8WKCRGoBcT5EAhAvre2TiwpsbFbRsKRG-KOt55gQbKqjO8g70IoXj-YBF7-iEx7q-5Di8IDjhn8bAkFTemRl7U1auYr6HcwvRpwDRVYQAdLy9Sjunq-maTh4DuZT2ifM-LmIKuDUcGC0Zqr27wv9Zc9N6K9ovT5NPmbGpFK_gY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد لإستهداف واسقاط مسيرة أمريكية من طراز MQ9 في سماء الخليج الفارسي ليلة البارحة بواسطة الدفاعات الجوية الإيرانية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76172" target="_blank">📅 22:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76170">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/omODEh3e74-cWwjJbtg_1ofeYYFSll__5oLHvbZ9oa2MpN2UhRRyYZMx9e3bh8OhnW6vEAq2JzI12-J1VDj6eAPrufGwubL6oKInE3E8rITSitNO-0GskHTrL5PILNX-qHjDzulKbqjXDoFH5Y7RgB_QIJ8fAk0o4h3DX5xM7kC5LMahHCtoJ9tHW-PX09_rjfVKy_TZzW7sQFbmsjflvfr8Pwtp3PCN18AhPbfmxjD8Jr-j-TYgfLJUb6LyK3BQ4HXobA7bYrnKU3t3X6KQg_7vmL9B5UQncS9AH_btKI3WDejmskHCccmqOdh8yHvCKYOedrHS8VsGNT4V9rUd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbGM3I8ZqjW4O8OGWbjX6bIk4W4frmr5EsKSZMeH8Tai9PC-HO53gxXGGr5PI7skXS2GXwjJsaAkt7PKbQKEEBr1D67cZfLCg7Lu0MGfU54ypasg4Hv4ThAKGS093BqY5Xzf0Ec_fJfZWf_l7TqEzgVBaZse7JgDgAjENI4KwUXIbjXRwIBGrLVIEWp_0cqAq6fheipE7fh2p8hAYNjHqyXkQ0qDqLLgA5jiohuUNvjxO_lJCwpLa1Hd0g1vLTCbaotxavnOU5pzuPdDlYou1X3lN93Wai8t_NSvEO-y1Bg6jiMgR0lUFCA7YoEPR0P3uORtDZG5i67jILCDXIf9Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
توثيق يظهر نظام الدفاع الجوي قصير المدى AD-08 Majid الإيراني، والذي تم عرضه خلال تدريبات ييريفان في 25 مايو في أرمينيا.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76170" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76169">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11425cc9b7.mp4?token=iXfvHGR_RoSMKzLrQjQFzSqCzGVKKUMlMb9Q1pXetXuRG0efds6PE4UqiZUALbJ3SgBRVizH7q0ohoT1tdpQJTYeGZFTV1c3BPx76HPjQEo4CMRMJGKQqITgs9gYMSEisfppPGYd9YXE9WRsIwPgCRtX4md3EpU_IEwt6pZ7XGhtKXDcrgYnV2oXyqoXcYEDmf36IRHtXSKb8OS9VWRgwQ2jIb81ex6HkCEgEomIkcTOxN4kWZKKqM9dkZggoF-otLrY9eG4tD-O-p3du-XJ0rjJQ9QUBKtkFpbGDiI3I1urHWjU9YasG3zcNj767tbkCVk0dZcSZjf2Z_Hcuxu0CoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11425cc9b7.mp4?token=iXfvHGR_RoSMKzLrQjQFzSqCzGVKKUMlMb9Q1pXetXuRG0efds6PE4UqiZUALbJ3SgBRVizH7q0ohoT1tdpQJTYeGZFTV1c3BPx76HPjQEo4CMRMJGKQqITgs9gYMSEisfppPGYd9YXE9WRsIwPgCRtX4md3EpU_IEwt6pZ7XGhtKXDcrgYnV2oXyqoXcYEDmf36IRHtXSKb8OS9VWRgwQ2jIb81ex6HkCEgEomIkcTOxN4kWZKKqM9dkZggoF-otLrY9eG4tD-O-p3du-XJ0rjJQ9QUBKtkFpbGDiI3I1urHWjU9YasG3zcNj767tbkCVk0dZcSZjf2Z_Hcuxu0CoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد لإستهداف واسقاط مسيرة أمريكية من طراز MQ9 في سماء الخليج الفارسي ليلة البارحة بواسطة الدفاعات الجوية الإيرانية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76169" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76168">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89068e1197.mp4?token=hbgliVxSmQMAz6oYrpWO_hk4Hn2qzKyXxHzaGFhFT43mfbD7XXsYys39bZUz2Y4JwPUx3N4w7cqFKpQKieyAXjM8dHlIjED59aDN-9K6T51suJX4xi0GYRSJWp0U2MzxyMtNH_v1blZfPkf4sNiHszuOclLevuja_EeE1wuJAw0HSTeSxeA-Aj6huEeL6vwzuxPcsYKDlkX-kQRQH2jzX9qt0piKkavKDIKjzqfPHYewdSgmNHA9NTplqoSD9hWhdNqVGnAebO-eZsQqvHDfmEtxjIHZRxtR41AUWTicfVOEvFbykr0uPzlC0pLuBti-50Nivax-NdeUnfacp8n3Fo4lL4QomogaGJ86iG9W7dL9pm5Kymqn0c__YzbsHMvTP3nQ-qzqR1YFfzBpKp2SAlliQnTBNuaay8ToLE0RolSIFq77aIzVsto0eGNkI8qMssRr-wT2W9aA38d4VJ0C_3-2aVhwyUMhPKGyMPIiFgbcIXwv8jVCj-r4Ab75aA3PfDHyuv8eSTcl6eNRCtuR13YWAHLR6M2_euL70Gq11K_84FryRd5ZoXTTX77dVBrhbuu7Ite--mpHNrZINxZOU8ga1ImviYkIDp0-iK9J9h3jGGridf_X5PEHzhTFHy_wT2AhXnik63KjZnJ7r3O4u3c9tMsilVDOmcYbqjdVe-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89068e1197.mp4?token=hbgliVxSmQMAz6oYrpWO_hk4Hn2qzKyXxHzaGFhFT43mfbD7XXsYys39bZUz2Y4JwPUx3N4w7cqFKpQKieyAXjM8dHlIjED59aDN-9K6T51suJX4xi0GYRSJWp0U2MzxyMtNH_v1blZfPkf4sNiHszuOclLevuja_EeE1wuJAw0HSTeSxeA-Aj6huEeL6vwzuxPcsYKDlkX-kQRQH2jzX9qt0piKkavKDIKjzqfPHYewdSgmNHA9NTplqoSD9hWhdNqVGnAebO-eZsQqvHDfmEtxjIHZRxtR41AUWTicfVOEvFbykr0uPzlC0pLuBti-50Nivax-NdeUnfacp8n3Fo4lL4QomogaGJ86iG9W7dL9pm5Kymqn0c__YzbsHMvTP3nQ-qzqR1YFfzBpKp2SAlliQnTBNuaay8ToLE0RolSIFq77aIzVsto0eGNkI8qMssRr-wT2W9aA38d4VJ0C_3-2aVhwyUMhPKGyMPIiFgbcIXwv8jVCj-r4Ab75aA3PfDHyuv8eSTcl6eNRCtuR13YWAHLR6M2_euL70Gq11K_84FryRd5ZoXTTX77dVBrhbuu7Ite--mpHNrZINxZOU8ga1ImviYkIDp0-iK9J9h3jGGridf_X5PEHzhTFHy_wT2AhXnik63KjZnJ7r3O4u3c9tMsilVDOmcYbqjdVe-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تظهر لقطات جزء من هجوم حزب الله يوم أمس في منطقة شوميراه بالجليل الغربي بواسطة محلّقات مفخخة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76168" target="_blank">📅 22:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76167">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799bcc6b46.mp4?token=llT6fmkQvuAjsB2PR6hzhjRmLRspK2Ysmw0VqXX2soZtwCEIV4pMZSzc_QtIu3pYFSgZmEftAZM4JWyQJkMuMIT_IFW4zW4aRwgiAV9g5l3RaEGjwicka_P_cNwJrS88yhiRcR67XSomFcnUxrFRLQjYDuAbuiH2UXkGG8REQ0wtMBcxRjb5DJD0lWcomfvRzoLWeJvjIKRdij9EwuqCtmTlGwyu3jzxmbINWTB31C7mBXgCjEEG0laPSSBhkkXfBgPtrQ-AtR0yzib3YUW-6BCHyZzSWv-SQ3RZR-tEiFfsfeD0THsxPGvJhnOq6QNnIWxjko6_yUS7VniwbzdRGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799bcc6b46.mp4?token=llT6fmkQvuAjsB2PR6hzhjRmLRspK2Ysmw0VqXX2soZtwCEIV4pMZSzc_QtIu3pYFSgZmEftAZM4JWyQJkMuMIT_IFW4zW4aRwgiAV9g5l3RaEGjwicka_P_cNwJrS88yhiRcR67XSomFcnUxrFRLQjYDuAbuiH2UXkGG8REQ0wtMBcxRjb5DJD0lWcomfvRzoLWeJvjIKRdij9EwuqCtmTlGwyu3jzxmbINWTB31C7mBXgCjEEG0laPSSBhkkXfBgPtrQ-AtR0yzib3YUW-6BCHyZzSWv-SQ3RZR-tEiFfsfeD0THsxPGvJhnOq6QNnIWxjko6_yUS7VniwbzdRGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان: لقد مدت إيران الإسلامية يد الأخوة إلى الدول الإسلامية، وفي الوقت نفسه لا تتردد في حماية أراضيها وسيادتها الوطنية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76167" target="_blank">📅 21:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76166">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴‍☠️
إعلام العدو يزعم: تنفيذ عملية اغتيال القائد المعين للجناح العسكري لحماس "محمد عودة" في منطقة حي الرمال بقطاع غزة بواسطة غارة من الطيران الحربي الإسرائيلي.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76166" target="_blank">📅 21:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76165">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
🏴‍☠️
دبابة ميركافا أخرى تابعة لجيش الإحتلال الإسرائيلي تم إستهدافها في بلدة زوطر الشرقية بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76165" target="_blank">📅 21:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76164">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يستهدفون دبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة رشاف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76164" target="_blank">📅 21:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76163">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce84f74f6.mp4?token=WouDaHm0h7konkt4xZhLrN6J7xgfzqpGH9OE6A5sO3dpmcJPr7F9K_UajUMSA6YMdJPMuAWLHSSHInXkMFAYYvauG60J9liizVi90DkfJ0oKDSnRvlKnE5mT9SCdKdojHq3X-LC8tIjdb3XJe4FvJ8Rv0poL2LpBeIs5l9so7lKRC5qLJMvv3afVuFJNclpisVXJ22v3RLND4f6WhjfiTsEVqyV175HBTZb9jU50CGs_W7tNfHZWJqMddE4_9ulE9NHBbhIHFCGotfM13y0piT0UKannxYufGLnElFcSzexivNIXobCGiTCMzM9UBnA_Y1T_LZ6IpvALUFwGlHvNyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce84f74f6.mp4?token=WouDaHm0h7konkt4xZhLrN6J7xgfzqpGH9OE6A5sO3dpmcJPr7F9K_UajUMSA6YMdJPMuAWLHSSHInXkMFAYYvauG60J9liizVi90DkfJ0oKDSnRvlKnE5mT9SCdKdojHq3X-LC8tIjdb3XJe4FvJ8Rv0poL2LpBeIs5l9so7lKRC5qLJMvv3afVuFJNclpisVXJ22v3RLND4f6WhjfiTsEVqyV175HBTZb9jU50CGs_W7tNfHZWJqMddE4_9ulE9NHBbhIHFCGotfM13y0piT0UKannxYufGLnElFcSzexivNIXobCGiTCMzM9UBnA_Y1T_LZ6IpvALUFwGlHvNyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو يزعم:
تنفيذ عملية اغتيال القائد المعين للجناح العسكري لحماس "محمد عودة" في منطقة حي الرمال بقطاع غزة بواسطة غارة من الطيران الحربي الإسرائيلي.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76163" target="_blank">📅 21:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76162">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اشتباكات بين البحرية الإيرانية والقوات الأميركية سقطت عدد من الشهداء وهم كلا من   پاسدار شهید عباس اسلامی  پاسدار شهید قدرت زرنگاری پاسدارشهیدعبدالرضاگلزاری پاسدار شهید حسین ستوده....</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76162" target="_blank">📅 21:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76159">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdeNdtcxf5YBv19_KY5VPjeoUtAKrlFVqoNZNj46Jew64Qyk6-GN7EqT3OKGZ14nDy6jhMIP1FaUJd8kKUj41ihTCqrurH0MzAcE8Qcu26FCm53f-OAF35w3YMk5Td8NQB8RayN1WTTI_Nx5uPl6N5ep584wppjElAlnNIRvyrOhtAhA07SHBUmr23ybjDmGEyouvOwctLXzrxWcg_VKd8TexJm5S1Of_q1TS6yBnMziCZq9YBScpA8F8H5y5GRdeKOqBWUR6gm0kGOCu4dVeCRKgOabuOj_9v173tx8cMqI_uQ2POswtjzpI4iClMOChi9WKO9LK_EEdlOvTMquKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ded70fc7.mp4?token=hgxcUJ-lD5cLGhemo1OK8CmVOlyidrHeK9XtoANBJZ3kcIUEIEmZC9SUzk3nnUrkVRtQR2i84f3rwsfrdUYqfeCbcBcxUJY8kzOZiOgY-T5elo9oZZqvdkdXvWpjcBcUwa6Dr_-f63q4ilR3gQJ0X46J0LohO3Vlb_XGAPqhlCtEZ8t2TuWdSmqNio0cSDeWHwRB2VZKvRuHRHlMWOkecLOuJX-c2u7n0P6Te0QgF0Vd6ykvHcWUMYPpaqGpK43iEm5CC_ni0JWmvtEfIdFW87FEzYX_wJoeYh6f4G9HwhOuFUjRA5TQEKJZk2aZJU4km08wbXbpx4I_O0SkP9YXZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ded70fc7.mp4?token=hgxcUJ-lD5cLGhemo1OK8CmVOlyidrHeK9XtoANBJZ3kcIUEIEmZC9SUzk3nnUrkVRtQR2i84f3rwsfrdUYqfeCbcBcxUJY8kzOZiOgY-T5elo9oZZqvdkdXvWpjcBcUwa6Dr_-f63q4ilR3gQJ0X46J0LohO3Vlb_XGAPqhlCtEZ8t2TuWdSmqNio0cSDeWHwRB2VZKvRuHRHlMWOkecLOuJX-c2u7n0P6Te0QgF0Vd6ykvHcWUMYPpaqGpK43iEm5CC_ni0JWmvtEfIdFW87FEzYX_wJoeYh6f4G9HwhOuFUjRA5TQEKJZk2aZJU4km08wbXbpx4I_O0SkP9YXZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
أنفجار عجلة بين حيفا وتل أبيب ،مقتل شخص بداخلها كحصيلة أولية ؛ وشرطة الإحتلال تعلن أن الخلفية والظروف قيد الفحص.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76159" target="_blank">📅 21:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76158">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f8e898fc0.mp4?token=mDze-yQ8v_xv8SkwoL_R4gY_uK9-AZKmJrsn1C7zThggrR4MxIrp61Zoxg7EUZCDcso61626GsVVAMaMKaY3G1A1NK1wQ17NiaS4lEY64MHBCgK8OC4ssq4jQJvkSkemwAsY1KLI1on_hSX_PkpnaZMzZYoNweEHVPDJ0Ad98rNFkfnN7M-EGnKsDml25hj6bV-t50UwCaljyMLgcGzqMKKh5nrIIonXNOqX0ejtoB-ZAfQ7Ezur3Pionb2eKvSw8rIheCvXlqrvOkcevqWhHHrn7jkv79zV4G8jKQCFpvfiBqJBFdRf8-2UbhuvvHcyF1bh9YxmwtN2zEhgnP9zXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f8e898fc0.mp4?token=mDze-yQ8v_xv8SkwoL_R4gY_uK9-AZKmJrsn1C7zThggrR4MxIrp61Zoxg7EUZCDcso61626GsVVAMaMKaY3G1A1NK1wQ17NiaS4lEY64MHBCgK8OC4ssq4jQJvkSkemwAsY1KLI1on_hSX_PkpnaZMzZYoNweEHVPDJ0Ad98rNFkfnN7M-EGnKsDml25hj6bV-t50UwCaljyMLgcGzqMKKh5nrIIonXNOqX0ejtoB-ZAfQ7Ezur3Pionb2eKvSw8rIheCvXlqrvOkcevqWhHHrn7jkv79zV4G8jKQCFpvfiBqJBFdRf8-2UbhuvvHcyF1bh9YxmwtN2zEhgnP9zXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
أنفجار عجلة بين حيفا وتل أبيب ،مقتل شخص بداخلها كحصيلة أولية ؛ وشرطة الإحتلال تعلن أن الخلفية والظروف قيد الفحص.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76158" target="_blank">📅 21:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76157">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⭐️
عقب فيضان نهر الفرات.. حكومة الجولاني تدعو لإخلاء فوري للمنازل والمحال القريبة من نهر الفرات في محافظتي دير الزور والرقة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76157" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76154">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uXOyy1vw6mYHgGByoJCNL0K49qnvFJsdSx20zBJVJwtN1mh3ofl2nNqmoby62PuTPOTSO5xT1p-FZtqsamFt8Kbm6u41tO--57bGZtOM4SuJEQbfkyMqX2GP7e36HknMtXOVjuaD1sjGdtdcKHrkgqSbZHvsjs_RItyyxSKLL12d1vvKOPbcEUYex2DhD5_eY5pxE4JGoi3Xu8CMkz0N00RDmbOAES2hPLMI2p-NrGIJQmRqWEwSKhQh5lVaiXwWBKoX_ddR2bJOu1VUhmWxJAFFL2YfQ1eNt0I3gqJQ7e1Tez-nc-QIEUUuhwJGBVboF-LAr8NVuAoGBGWFRuU9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rX26-9nuMWO_XDS1TE7nnZAGSZIr5hZDsdno8iIsYCiFZ4E0PBCP-8aLuuKnbmLYO_27Kd9WazKIc2EoC9IqHy6_XGLM7SUU4NIrqnlJ9Zbt8A0WxWax_vrfsWEeu_D8lgOd9lVtPhIkUKPexkt_CLsKuDet_KR5keJHli0NWF6p4PgkxrmNfIrNd64TS427Qi49IgZpfsJEpk4oiR8oORg6hrb_Khx_yFaV29X4DmlFmqo6lkfZjhEO9V1wfhaxsBST1Scd-kCHTjn4Ku2r3efmzTGGQzDhvGMlmGJWbd1RFX-uimWEDmdNK6kZUe0W0jpZxat9_rf2Pn82OtxqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bk2DYFKsXOgVTC0GJursHVH2y8d6OJcSJTW-rdBZQc7HrwYL2HRqGJAKRIK6QkpTXFWzI6f8pNHUfuXoMi7uRzTAalypFBTiqLexE5bO6HGCWG0rPV6fpgOy23ABVyMJUq62NSfMzjKEMxCLyeHAstP9kYfVJOFt5WavCk0DQfmpva8uKhLKfwjjSet3IIS-ECwgM8MrRMO-p-1KdtGBri9YNuwbIftME3Z2E7P4Gl0dKSkAtSzm5Ik9WeDyq3BdpPa6GEp_VpbdSrEHCQhkBkveV-gS7oYXskFvcDcdV5WtiYxxLj-zGrwyQ2Q3_aSf612c_0hB5lh-syjC4TWUqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇶
إيران والعراق لايمكن الفراق..
برای دومین روز متوالی، خدمت رسانی و ایجاد فضایی امن برای زائران ایرانی که برای شرکت در روز عرفه به گذرگاه مرزی مهران مراجعه ميكنن ، توسط فرماندهی عملیات نیروهای حشد الشعبی در استان واسط، ادامه دارد. این کار به دستور مستقیم فرمانده عملیات واسط، آقای احمد خضیر المکصوصی، انجام شده و شامل تهیه غذا، تسهیل مراحل ورود زائران و ارائه پشتیبانی لازم برای انجام زیارت میباشد.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76154" target="_blank">📅 20:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76153">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
لقد مدت إيران الإسلامية يد الأخوة إلى الدول الإسلامية، وفي الوقت نفسه لا تتردد في حماية أراضيها وسيادتها الوطنية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76153" target="_blank">📅 20:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76152">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⭐️
‏
القناة 14 العبرية:
تقديرات في إسرائيل بأن الاتفاق مع إيران سيشمل بشكل شبه مؤكد لبنان.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76152" target="_blank">📅 20:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76151">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWH-FJxI1yw8lVIYCWP4SecUXmymhDPH8ZGrgcmphZwGzWjQjaobHsT4kCOqpiS4px5R-c3qU8g-_1TEq1oKu6wdqfuIAl8RhlYD6UYmUlwONJtoGCSRkRha25C_D7LFl1g-2WUZsnbqwFpybsWZn4zL7SiW3jPJ7sx-dH5XSDs8zJKvwXg5SCBq1WF_p38W00x1uee1BhakLRfe8dSz030CJP27HcpyE0f91z87KOBaGZs1STBfbhV-1-_8WxEyIn8fPxpaosXLyEfVvA1aQEjD33G_CnY5JVYMlQjx2Ij5wqzXaf8yBBLpNF3ZUEFVx8NPIdNiV8LWHAkOqNgX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ديدار مشاور امنیت ملی عراق "قاسم الاعرجی" در مسکو با معاون دبیرکل شورای امنیت ملی ایران "علی باقری".
در این دیدار، آخرین تحولات اوضاع منطقه و راه‌های حمایت از گفت‌وگو از طریق کانال‌های دیپلماتیک برای پایان دادن به درگیری‌ها در منطقه بررسی شد، همچنین تقویت روابط تاریخی عمیق بین دو کشور و دو ملت دوست مورد بحث قرار گرفت.
آقای الاعرجی بار دیگر تأکید کرد که قانون اساسی عراق اجازه استفاده از خاک عراق به عنوان نقطه شروع برای حمله به کشورهای همسایه را نمی‌دهد و به نیاز به تشکیل شورای هماهنگی امنیتی بین همه کشورهای منطقه اشاره کرد.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76151" target="_blank">📅 20:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76150">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a65cbfac7.mp4?token=OPaepMYXAnNu2EZln5XZXIA2LEB5yh1VIAo-WyfDRXCUsAohWDiGdrpEtckJfrkBfN1-o3BEi-Fz6egsOiMDntM6PqfjfSsvXQmH-X4-TW4nDZrfRHORe2BDqmiNVSxVdZFD67gkzA-ukwGGkRqMLgpJpaAwNsVuETTnEuzUr9XLv0Az-h22poxIh9zztb4fxqyYn1NdTM-Jd03SHot_RwNnrGpHHq2bvi0HXEtjWf79pisZoq4jCAqXdBTUhD-yZaeVCoS9yT1HVDmNxZVW862KY_SvZMc9kg0YTGuud18lR14DIa9S5r6nIDE1Z_rXXAFqEB_jJB5GY6V2WHm9lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a65cbfac7.mp4?token=OPaepMYXAnNu2EZln5XZXIA2LEB5yh1VIAo-WyfDRXCUsAohWDiGdrpEtckJfrkBfN1-o3BEi-Fz6egsOiMDntM6PqfjfSsvXQmH-X4-TW4nDZrfRHORe2BDqmiNVSxVdZFD67gkzA-ukwGGkRqMLgpJpaAwNsVuETTnEuzUr9XLv0Az-h22poxIh9zztb4fxqyYn1NdTM-Jd03SHot_RwNnrGpHHq2bvi0HXEtjWf79pisZoq4jCAqXdBTUhD-yZaeVCoS9yT1HVDmNxZVW862KY_SvZMc9kg0YTGuud18lR14DIa9S5r6nIDE1Z_rXXAFqEB_jJB5GY6V2WHm9lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
نتنياهو:
قررنا تعميق العمليات العسكرية في لبنان.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76150" target="_blank">📅 20:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76149">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo2CprXpro6MT6z07mj_G7pmEYVjiS8B9_VQD2fH5P07rVZNAAa_EcZfIOUYt3vnVsw_oULLXkAhGs7Pgz59t7F3_ciIydcv87wcsTnUHVR3ce5iHokS2miPXxvi8sxsezWh82-8IDkEnEWOkURB33OB2uPZ7rZUyhWRG0JdNJrs89nsXaiSz3mYj-74tn_GTm0JY5CEYW_BcXtW-ULKhM5unpDaIKK7Glqs6ywOzJh35YHMcN-CCg4ROsYoAMzkG2jiKguZL3uey6JIJbfQbtPfQjprgDT30_eNaelCsZAnr9k7YtTnPear2YqND8pnFSlX5OfEZmWafEFN80iXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
انتهيت للتو من الفحص الطبي الدوري الذي أجري كل ستة أشهر في المركز الطبي العسكري والتر ريد.كل شيء كان على ما يرام. شكرًا للأطباء والموظفين الرائعين! عائد إلى البيت الأبيض.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76149" target="_blank">📅 20:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76146">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0b9345b0.mp4?token=d_Wld_ZaDpdWdaWgK6tE4nZePdB9w-wSUVWDpeJOP8_ikbK2-9zSwxPD_9FhA_nCrk7-vGbhwi0wNPcPKpONLhun9le0c-DMDl_k3r-sKWffDIszw25gGuhya0PlpDc4__q28uS0PFw-HsQGSmNLi56HMsbFU2a4gV6D2Rj_jW2VWKCWtfiSJUFb7aHt0k-kudJTJ-VKEkTftXiK-JUXNZUVonFnTb4h-VhexYkq22xjagzk-UGDbIgRw-brH3fy1iUb7-xhzujN2nLJNlpydG27I0dH8ErnHOX-lRY-tklVDKmKlZ6BFAir-QbpoX9z0ie1vq3nsW-ASkHQKw9HcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0b9345b0.mp4?token=d_Wld_ZaDpdWdaWgK6tE4nZePdB9w-wSUVWDpeJOP8_ikbK2-9zSwxPD_9FhA_nCrk7-vGbhwi0wNPcPKpONLhun9le0c-DMDl_k3r-sKWffDIszw25gGuhya0PlpDc4__q28uS0PFw-HsQGSmNLi56HMsbFU2a4gV6D2Rj_jW2VWKCWtfiSJUFb7aHt0k-kudJTJ-VKEkTftXiK-JUXNZUVonFnTb4h-VhexYkq22xjagzk-UGDbIgRw-brH3fy1iUb7-xhzujN2nLJNlpydG27I0dH8ErnHOX-lRY-tklVDKmKlZ6BFAir-QbpoX9z0ie1vq3nsW-ASkHQKw9HcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إشتباكات عنيفة بين مشجعي فريقي كرة القدم هبوعيل بئر السبع ومكابي تل أبيب في القدس المحتلة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76146" target="_blank">📅 20:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76145">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يستهدفون دبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة رشاف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76145" target="_blank">📅 19:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76144">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يستهدفون دبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة رشاف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76144" target="_blank">📅 19:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
نائب الرئيس الايراني:‏أُعيد فتح الإنترنت وتوفير خدمات ذكية استجابةً لمطالب الشعب، مع التوجه لإزالة العقبات أمام التنمية والريادة العلمية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76143" target="_blank">📅 18:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76142">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📰
وول ستريت جورنال: البحرية الأمريكية تستأنف توجيه السفن عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76142" target="_blank">📅 18:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76141">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6nEfyCxmpK2coDCxaj8BMmhQbCVxmpKsUXjTA6GOEeYVEq6lAy4MOR8fLgvkGYy3Y0Se941bcS_aE8FC5evM40ruoqqJA5VNzjhJWFAB0fm1s044SDgdBaQWL1uQA8p7TB_IwPtBa2iT8sOXhVSYBosvUVrtCUrYO8v_iYRprbKZGjr_FZfIyWnbL_svhVDFta1SC8RkbGUJC3nhHcelLhTI09uhZY-Ux1vMGNm_xYTxRjgZvKFLxliPnsnLLfATe_u-MVJ1J-pKUpcIjtA1YSirgReNeD3jyPZabYeIbTBd4402h07X5OMXg21WJQhT8oD9vJeqfjadnRG0lmrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
ديمتري ميدفيديف:
قال الاتحاد الأوروبي إنه سيحافظ على وجوده الدبلوماسي في كييف دون تغيير، على الرغم من تحذيرات روسيا. حسنًا، يبدو أن لديهم دبلوماسيين فائضين ويحتاجون إلى تقليص عددهم.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76141" target="_blank">📅 18:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76140">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
‏ترامب يرفع سقف استقبال اللاجئين بمقدار 10 آلاف لاجئ لاستقبال المزيد من البيض من جنوب أفريقيا.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76140" target="_blank">📅 18:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76139">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e929c95856.mp4?token=bNxOCLneAaG1MLVDriFyW_UdCQE_ULZUc8OO6op9hTeMdiWa93ea3nko0uHteeXWA1Jh3IqV8b2BqOwv1qLOVQCzfmwanmKY9-32G1DJls1isELKUhTrpMsaVQgyYojV9-oTyI6Rl8z0l48CrEl8wasXpiJsfjm2MAVelwonioEFyZGoN6ctmZRlGdEb0rqQKtoZMOx5jpQWLdsZ6bW-w1KUnUjtlgv-149UhBypCDh6D2L6cUCdktR8eifVkZ60cRE022rfy4r3nz9AfcPF54A9DVmVhaOpPNgfXL4dx0mbRSqTHHupnpxDoNZ9CZPfkZhbnkSOsDtUaN14Y2gXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e929c95856.mp4?token=bNxOCLneAaG1MLVDriFyW_UdCQE_ULZUc8OO6op9hTeMdiWa93ea3nko0uHteeXWA1Jh3IqV8b2BqOwv1qLOVQCzfmwanmKY9-32G1DJls1isELKUhTrpMsaVQgyYojV9-oTyI6Rl8z0l48CrEl8wasXpiJsfjm2MAVelwonioEFyZGoN6ctmZRlGdEb0rqQKtoZMOx5jpQWLdsZ6bW-w1KUnUjtlgv-149UhBypCDh6D2L6cUCdktR8eifVkZ60cRE022rfy4r3nz9AfcPF54A9DVmVhaOpPNgfXL4dx0mbRSqTHHupnpxDoNZ9CZPfkZhbnkSOsDtUaN14Y2gXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
الاحتلال الصهيوني يستهدف عدة منازل مدنية في محافظة النبطية جنوبي لبنان.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76139" target="_blank">📅 18:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76137">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfd9de336.mp4?token=lo9ZwmDq3-OOYqbJi0xL_RVdpzDOsmvSCNenfhtw8o3AtlWWEsM3Syzw-J9H5eW-ehJ-CJpP0N8eehM6vPehk3YDeXKaqqp10cj1YU1ebwe7GeoyRQRMjAEI7_kqxnXyEQTesb4yNEKf0Lmof8zm-ddOdLXnXOvgl41PKSL1bniEAN3dC9X2CX7eW8nMj0MU5hjB2zV7iB2KqVxqWMcKwU_cH8H8-fySWbve-okDDUXxsako6MFhW4Qquo9rhRJ0WHdkZrOnR3EXvCYHh3SqpqKiG-KczHiqVGJdxN-Vxh2xS8LuTfvyuAhgL2t_NOL-OZkBzgEmPQOABqc9FwIjag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfd9de336.mp4?token=lo9ZwmDq3-OOYqbJi0xL_RVdpzDOsmvSCNenfhtw8o3AtlWWEsM3Syzw-J9H5eW-ehJ-CJpP0N8eehM6vPehk3YDeXKaqqp10cj1YU1ebwe7GeoyRQRMjAEI7_kqxnXyEQTesb4yNEKf0Lmof8zm-ddOdLXnXOvgl41PKSL1bniEAN3dC9X2CX7eW8nMj0MU5hjB2zV7iB2KqVxqWMcKwU_cH8H8-fySWbve-okDDUXxsako6MFhW4Qquo9rhRJ0WHdkZrOnR3EXvCYHh3SqpqKiG-KczHiqVGJdxN-Vxh2xS8LuTfvyuAhgL2t_NOL-OZkBzgEmPQOABqc9FwIjag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
أ ف ب:
رئيس الوزراء الفرنسي يعتزم اللجوء إلى القضاء ضد معاملة إسرائيل "المروعة" لناشطين في أسطول غزة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76137" target="_blank">📅 18:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76136">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📰
وول ستريت جورنال:
البحرية الأمريكية تستأنف توجيه السفن عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76136" target="_blank">📅 18:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76135">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b6835677.mp4?token=j-T0muzpXE7TrgtxqrMHSMkAiBq9hYigEDrBL8RxuJ6alKKsnwAxNsZnV7vOgsMeaM8ztxlKEzl6TDZO-xY2iAdkZGVv1eB9UXy_ECzxWxp9opiraIDO-jvLQ9RKRJ92sECqv-UgssLxv8MxpK_so1f9GNRDi4KAHZVe1f91k4RT3jL45kOFH5xn8M-1NffuhBwtVXa7mvSWGzUb334EzepA9iF8LZ0UB-_UA5GSvB4v2NQAXit3-EVM0NzWS93Ks4tThpyRTOI50pWtprYTj96X9U-5-zK8q7hD18nLXF71xg1Qv5-40vMHv1jzxB78zssqTx2rmKNsDML-p9cEUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b6835677.mp4?token=j-T0muzpXE7TrgtxqrMHSMkAiBq9hYigEDrBL8RxuJ6alKKsnwAxNsZnV7vOgsMeaM8ztxlKEzl6TDZO-xY2iAdkZGVv1eB9UXy_ECzxWxp9opiraIDO-jvLQ9RKRJ92sECqv-UgssLxv8MxpK_so1f9GNRDi4KAHZVe1f91k4RT3jL45kOFH5xn8M-1NffuhBwtVXa7mvSWGzUb334EzepA9iF8LZ0UB-_UA5GSvB4v2NQAXit3-EVM0NzWS93Ks4tThpyRTOI50pWtprYTj96X9U-5-zK8q7hD18nLXF71xg1Qv5-40vMHv1jzxB78zssqTx2rmKNsDML-p9cEUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
الصحيفة الالمانية شبيغل: تخطط الولايات المتحدة لتقليص كبير للقوات العسكرية والمعدات التي تلتزم بها تجاه حلف شمال الأطلسي في أوروبا، مما يزيد الضغط على الحلفاء الأوروبيين لملء الفجوات بأنفسهم.  تشمل التخفيضات المقترحة طائرات مقاتلة، وقاذفات استراتيجية، وسفن…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76135" target="_blank">📅 17:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76134">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🌟
حزب الله ينشر:
أحرارٌ أعزّاءُ لا عبيدٌ أشقياءُ.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76134" target="_blank">📅 17:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76133">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌟
رويترز
: العقود الآجلة لخام برنت ترتفع 4 دولارات للبرميل، بعد عدة ضربات وجّهها الحرس الثوري على حاملات النفط بسبب مخالفتها قوانين مرور مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76133" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76132">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
‏ رويترز: عراقجي وقاليباف في قطر.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76132" target="_blank">📅 17:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76131">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌟
🌟
يديعوت أحرونوت:
حزب الله لديه مسيرات قادرة على الوصول حتى مسافة ٣٠ كلم.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76131" target="_blank">📅 17:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76130">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇩🇪
الصحيفة الالمانية شبيغل:
تخطط الولايات المتحدة لتقليص كبير للقوات العسكرية والمعدات التي تلتزم بها تجاه حلف شمال الأطلسي في أوروبا، مما يزيد الضغط على الحلفاء الأوروبيين لملء الفجوات بأنفسهم.
تشمل التخفيضات المقترحة طائرات مقاتلة، وقاذفات استراتيجية، وسفن حربية، وغواصات، وطائرات بدون طيار، وطائرات التزود بالوقود جواً.
لا تزال واشنطن تعتزم الحفاظ على الردع النووي في أوروبا، لكنها تريد من الأوروبيين تولي معظم مسؤوليات الدفاع التقليدية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76130" target="_blank">📅 17:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76129">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16fda706f6.mp4?token=dRBf7U8kZpnwaM-ccfmnXybvQn4PqSq7Cu16cUq5Bs0BWxR-mAsmrkW2BgtXKJY9OIICJHI96eosAGYA5MCZ_Q5Q3Jckpvg8GAaVxd0MnwYwrPfcfFbYH3Bp9K-KjtCl1pKi3_D0V4LntSqAyw1dKESIlpR9sPgjejr24ssPQrIziuXAls50HpINx61MWKCgMTGgRMMQz5QdHxSCanR2nLztNXy-7RM1J7_Dkch99N8zaE969xImLfE_UMBiNUk3dWWwrrt4GrMDY8S0ZTbgi8I0DOO88iXmEpJRabSl2u0y1DZPmNAlGC7ORlkr3CvAryOZ4dLwQjhDyycBcL6weA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16fda706f6.mp4?token=dRBf7U8kZpnwaM-ccfmnXybvQn4PqSq7Cu16cUq5Bs0BWxR-mAsmrkW2BgtXKJY9OIICJHI96eosAGYA5MCZ_Q5Q3Jckpvg8GAaVxd0MnwYwrPfcfFbYH3Bp9K-KjtCl1pKi3_D0V4LntSqAyw1dKESIlpR9sPgjejr24ssPQrIziuXAls50HpINx61MWKCgMTGgRMMQz5QdHxSCanR2nLztNXy-7RM1J7_Dkch99N8zaE969xImLfE_UMBiNUk3dWWwrrt4GrMDY8S0ZTbgi8I0DOO88iXmEpJRabSl2u0y1DZPmNAlGC7ORlkr3CvAryOZ4dLwQjhDyycBcL6weA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
الاحتلال الصهيوني يستهدف عدة منازل مدنية في محافظة النبطية جنوبي لبنان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76129" target="_blank">📅 17:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76128">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34378ee6f.mp4?token=jKi9vdSuJ_rAqupWLypbZK9EVIBrpKcX19S9qM2dFydH5g--cNBG2plQZZEARbFk0rlIgxZ_SCd2KtRj-P5SZSPxv4F8Ws9TAta4qg4kL_c3GuVkkwiy10VOeknbZ5B1G6rx2iG81q3pmrrTHsR1r7Mevzj4e7rT16v-uZHFd7yaVJ4JkpqIZvKDuYleUhqXDSqfvJH8TuFcK2PblTQBxq8eOhVAfCnDDV1l1Nb-n30wLtw9z8c0K93q-69qcsmTaBqafzxWox2LU92mUicgjLA63uFmXA-YEkJc_3s0v0y2TAGfzBL_KJy14iil73KzsxtQefaYxD_wbY3_3sntRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34378ee6f.mp4?token=jKi9vdSuJ_rAqupWLypbZK9EVIBrpKcX19S9qM2dFydH5g--cNBG2plQZZEARbFk0rlIgxZ_SCd2KtRj-P5SZSPxv4F8Ws9TAta4qg4kL_c3GuVkkwiy10VOeknbZ5B1G6rx2iG81q3pmrrTHsR1r7Mevzj4e7rT16v-uZHFd7yaVJ4JkpqIZvKDuYleUhqXDSqfvJH8TuFcK2PblTQBxq8eOhVAfCnDDV1l1Nb-n30wLtw9z8c0K93q-69qcsmTaBqafzxWox2LU92mUicgjLA63uFmXA-YEkJc_3s0v0y2TAGfzBL_KJy14iil73KzsxtQefaYxD_wbY3_3sntRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
السيناتور ديف ماكورميك:
"سيتعين علينا استخدام الجيش لفتح المضيق وطمأنة السفن التجارية. لدينا القدرة على القيام بذلك. لن يكون الأمر سهلاً، لكن هذا هو الطريق الأصعب في نهاية المطاف."
خذها ان استطعت
😎
...</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76128" target="_blank">📅 17:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76127">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZnbD9u2QK3SUomVmuBUHErgAa9a1Vk7IATREzLvhDLp8FazPbl0pvrrXC3bQOmvsL9gN0sAOjWFww0XmKUIDOmDLON2oTj7u3uNUyEgzoSrzf696crjioYxzY_ezl9cS-xa7OahNzA6xdjlzV-DevgHUkY6kjjckpMnKmgrjt7jWtjC2coVnkNNlYjfOFhSZAWOwiqu1hX0yVYKHYSU0F1zlKi3LSASQkeWI9hZyZ-TBkG3kMilouNlnd_YMbl9vrM11hxiZdNVzJmxYAIIWJtjTBjUNPzrPWP-rg7BgnurKQXcZDcdbSfuGviDJSEEbX5C4xd9YbJ8FplkHX9gQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نائب الرئيس الايراني:
‏أُعيد فتح الإنترنت وتوفير خدمات ذكية استجابةً لمطالب الشعب، مع التوجه لإزالة العقبات أمام التنمية والريادة العلمية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76127" target="_blank">📅 16:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76126">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجار يهز سواحل عمان</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76126" target="_blank">📅 15:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76125">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجار يهز سواحل عمان</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76125" target="_blank">📅 15:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76124">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d125f4a00.mp4?token=oid3yEzeCX0qSigqIJadF4kCyp9GCtjtwnUUUW6A-jbZyvJmq6fGboYfE_i4hZumAdhE4RFoPrPXyGm4yLMyMlC_HFvKWouGm8XN0T0k7fe4nuZ0rXABfV89tIzQMMooDjw1g-86bYzDccDha_zk6dG8_IDvMOjkyTPtrJvC87VfnMm8E1gWfml-tAqJXy15SlsfTaWhdcAxOrXvRaGFbsAQb3aFtypcdh8wr2LF4BY_fMMqhzviFEm9UfJiw1YBAYIHs_Vyt4syxpKKo2yeTAqkFZVIKGq9ycOF2tNxPjXbubxEn7DVRSqUkQcgXg1UVNY2Sr3PeBrMIy6nrojfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d125f4a00.mp4?token=oid3yEzeCX0qSigqIJadF4kCyp9GCtjtwnUUUW6A-jbZyvJmq6fGboYfE_i4hZumAdhE4RFoPrPXyGm4yLMyMlC_HFvKWouGm8XN0T0k7fe4nuZ0rXABfV89tIzQMMooDjw1g-86bYzDccDha_zk6dG8_IDvMOjkyTPtrJvC87VfnMm8E1gWfml-tAqJXy15SlsfTaWhdcAxOrXvRaGFbsAQb3aFtypcdh8wr2LF4BY_fMMqhzviFEm9UfJiw1YBAYIHs_Vyt4syxpKKo2yeTAqkFZVIKGq9ycOF2tNxPjXbubxEn7DVRSqUkQcgXg1UVNY2Sr3PeBrMIy6nrojfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 22-05-2026
دبابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة مركبا جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76124" target="_blank">📅 15:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76123">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxWYGYYSlBLvkDmomdS_EYCjSKapKFzMPnZCOUfT3SJIJdMciWFh7QEToXoG9ntsfS5GOW9Ad5VdF96Pg7wh7y59gxluRU4JYWwhgkjv1wTjxhrhAKUHjAYUJKIS5yxmm1s8ngZw3hBcJQ5T72_VQ6bxraFV3lSjnKeV5YPUI_I3xOzPasm9mUMvwsDbwylESurE64F9T8cj099_4EDZM7bcJROjyPczMuDlh90822K7LS790IrhJoxC0IoDI2Td-gHedZ-OQ-lh8Z2V1OBW1FnF65bUILTY0xC2akOJBX9tbQsMoTAg4VizYvv3k4jLWtlHCg4aC2ppbQXaN2cw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
الخارجية الإيرانية:
طهران سترد على الخرق الأميركي لوقف النار.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76123" target="_blank">📅 15:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76122">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇷🇺
مجلس ‏الدوما الروسي:
الهجمات على المدنيين قد تدفع موسكو لاستخدام أسلحة لا تترك أثرا لأي شخص.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76122" target="_blank">📅 14:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76121">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">#عاجـــــــــــــــل
⭐️
وفاة أول حاجة عراقية من أهالي محافظة واسط في الديار المقدسة اثناء تأدية مناسك الحج.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76121" target="_blank">📅 13:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76120">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
اندلاع أعمال شغب عنيفة داخل دار تأهيل النساء في منطقة الاعظمية وسط العاصمة بغداد وأنباء عن سقوط عدد من الإصابات</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76120" target="_blank">📅 12:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76119">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏وكالة أ ب: وساطة قطرية نجحت في تحقيق تفاهم أميركي إيراني بشأن "الأموال المجمدة"  ‏من المرجح أن تعلن الولايات المتحدة وإيران اليوم اتفاقا بشأن "الأموال المجمدة"</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/76119" target="_blank">📅 12:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76118">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: استهداف قاعدة عسكرية في الجليل الغربي بمسيرات حزب الله</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76118" target="_blank">📅 12:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76117">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏وكالة أ ب: وساطة قطرية نجحت في تحقيق تفاهم أميركي إيراني بشأن "الأموال المجمدة"
‏من المرجح أن تعلن الولايات المتحدة وإيران اليوم اتفاقا بشأن "الأموال المجمدة"</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76117" target="_blank">📅 12:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76116">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">إعلام غربي : يدرس المدعون الإسرائيليون توجيه اتهامات جنائية ضد رئيس ديوان نتنياهو، تساحي برافرمان، بتهم الاحتيال وخيانة الأمانة وعرقلة سير العدالة المرتبطة بالتسريب المزعوم لوثيقة استخباراتية سرية للغاية إلى صحيفة بيلد الألمانية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76116" target="_blank">📅 12:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76115">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌟
حزب الله: سرديّة استهداف قائد لواء المدرّعات 401 في جيش العدو الإسرائيلي العقيد مئير بيدرمان في أطراف بلدة دبل جنوبيّ لبنان بتاريخ 20-05-2026
بعد سلسلة محاولات تقدّم إلى بلدة حدّاثا ومن عدّة محاور، لم ينجح العدوّ في اختراق دفاعات المقاومة عند أطراف البلدة التي تكبّد فيها العديد من الخسائر من جنوده وآليّاته.
خلال مساء يوم 19/05/2026، هاجم العدوّ حدّاثا بشكل عنيف ومن محوري تقدّم بجمع كبير من الآليّات و34 جنديًّا (قوّة من الكتيبة الهندسيّة القتاليّة 601). دارت اشتباكات واسعة عند أطراف البلدة. وعند الفجر انكفأت القوّة المتقدّمة تاركةً خلفها جرّافتين مدمّرتين و4 دبّابات احترقت نتيجة استهدافها بالمحلّقات والقذائف المباشرة. أمّا الجنود فقد شُوهِد خروج 28 جنديًّا و6 الباقون تمّ نقلهم بواسطة آليّة نميرا بعد إصابتهم منهم قائد السرية النقيب م. ومقاتلة التوثيق العملياتي الرقيب الأول ش.، اللذين أصيبا بجروح متوسطة وخطيرة.
كان هذا التقدّم بإشراف قائد اللواء (401) مباشرةً الذي كان يتابع تقدّم القوّات وكذلك انكفاؤها من التموضع المتقدّم للواء في بلدة رشاف.
عند الساعة 05:00 فجرًا، عاد اللواء مئير بيدرمان إلى المقرّ المستحدث لعمليّات اللواء عند أطراف بلدة دبل بعد انكفاء القوّة كليًّا. هذا كلّه كان تحت عين ورصد المقاومة.
عند الساعة 07:50 صباحًا، وصلت أوّل محلّقات أبابيل الإنقضاضيّة إلى المقرّ وقامت بجولة مسح ميداني للمقرّ ودارت حوله، وعندما رصدت تموضع لضباط العدّو خلف تمويه في الطابق الأخير، وبعد فرارهم إلى الداخل لحقتهم المحلّقة التي استطاعت الدخول خلفهم إلى المقرّ وأصابتهم وأصابت غرفة العمليّات مباشرة. ونتيجة الاستهداف هذا أُصيب قائد اللواء مئير بيدرمان في رأسه وضابطان آخران.
عند الساعة 08:10، قام فريق إسعافي بإخلاء الإصابات عبر آليّة هامر إلى مهبط المروحيات. وصلت الهامر إلى المهبط عند الساعة 08:23، حيث اقلّت المروحيّة اثنين من المصابين، بينما نُقل المصاب الثالث بسيارة إسعاف.
عند الساعة 08:45، عاد الفريق إلى المقرّ عند أطراف بلدة دبل، حيث كانت تنتظره محلّقة أخرى قامت باستهداف المقرّ من جديد. وأصابت أخرى شاحنة ذخيرة، ما أدّى إلى انفجارات واندلاع حريق قرب المقرّ.
عند الساعة 09:00، وبينما كانت القوّة تستعدّ لمغادرة المبنى، استهدفت محلّقة أبابيل أخرى آليّة نميرا عند مدخل المقرّ.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76115" target="_blank">📅 12:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76114">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 20-05-2026 المقر المُستحدَث لقيادة لواء المدرّعات 401 التابع لجيش العدو الإسرائيلي في بلدة دبل جنوبيّ لبنان بسربٍ من محلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76114" target="_blank">📅 12:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76113">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1060dd6c41.mp4?token=C9obGJ-qiA6hDekG6Oz2vuAtQ4TaxUug-BeOB-lFiLSBiNy3fXQZPfnN4m-zRX4RWdHyyXYNEf3kqcFrUUFauEpNLSnSLHx9-n_kOyCFfCG7g2fAET9B-aJEess56abORzxklMAlZl04VyISLBWzRGyKNHVgAmP-u9r4s5MnOm-uq9Zjh9fbfN1A7_ARvBoNFJT05SKpOtJF_DO8jiMnMAw9eg7ueMnOeJHN_pb48-tOggY5frpKuGKNRJID93gTEOKy-4II1_KZObbe-KG8PHiWNTs0HDwyciKE_FR61zar7nyi9JtHcUpXOGl0htddYs8SW0gP7OsW8lk7MawiGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1060dd6c41.mp4?token=C9obGJ-qiA6hDekG6Oz2vuAtQ4TaxUug-BeOB-lFiLSBiNy3fXQZPfnN4m-zRX4RWdHyyXYNEf3kqcFrUUFauEpNLSnSLHx9-n_kOyCFfCG7g2fAET9B-aJEess56abORzxklMAlZl04VyISLBWzRGyKNHVgAmP-u9r4s5MnOm-uq9Zjh9fbfN1A7_ARvBoNFJT05SKpOtJF_DO8jiMnMAw9eg7ueMnOeJHN_pb48-tOggY5frpKuGKNRJID93gTEOKy-4II1_KZObbe-KG8PHiWNTs0HDwyciKE_FR61zar7nyi9JtHcUpXOGl0htddYs8SW0gP7OsW8lk7MawiGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مشهد بات مألوفاً في سوريا تحت حكم الجولاني.. حيث أصبح من هواية الأجانب الإرهابيين التجول في الأحياء المسيحية وتحديداً حي باب توما الدمشقي وترديد التكبيرات لإثارة النعرات الدينية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76113" target="_blank">📅 11:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76112">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: وجّه مجتبى خامنئي، المرشد الأعلى لإيران، رسالة تهديد إلى الولايات المتحدة : "لن تكون أمريكا آمنة في منطقتنا".</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76112" target="_blank">📅 11:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76111">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني: ما تم تداوله في الإعلام حول البنود الـ14 لمذكرة التفاهم بين إيران والولايات المتحدة لا أساس له من الصحة</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76111" target="_blank">📅 11:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76109">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">إعلام العدو : بدأت إسرائيل تعبئة احتياطية طارئة، بما في ذلك قوات المدفعية التي تم تسريحها مؤخراً من الخدمة، مع تزايد الاستعدادات لعمليات دفاعية موسعة في لبنان وسط استمرار هجمات حزب الله وانتهاكات وقف إطلاق النار</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76109" target="_blank">📅 10:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76108">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_رهبر_انقلاب_اسلامی_به_مناسبت_برگزاری_حج.pdf</div>
  <div class="tg-doc-extra">415.4 KB</div>
</div>
<a href="https://t.me/naya_foriraq/76108" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">النص الكامل لرسالة قائد الثورة الإسلامية بمناسبة موسم الحج | 5 خرداد 1405</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76108" target="_blank">📅 10:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76107">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الجيش الإسرائيلي: لم نشارك في الضربات ضد إيران إلى جانب الولايات المتحدة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/76107" target="_blank">📅 10:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76106">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭐️
هجوم بالطيران المسير الانتحاري وعدة صواريخ يستهدف مقر تابع للمعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76106" target="_blank">📅 10:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76105">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📰
‏القناة 12 الصهيونية عن مصادر:  مجتبى خامنئي لم يصادق بعد على التفاهمات المتبلورة</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76105" target="_blank">📅 10:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76104">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjIPyCroy6vmse5Ub4665N7vT8NQwAoBfQoEvfnK_BM1lmaE-qqQd9KDTzet4mbzXA7bj9gDlKTvaHg-tCfDJcoOXDQH8BPig3BHaiJO3PwfIfsYcCE8SprfICqMa2TeFo78urNVLtLMVT1px7DNG5t1ANWFdW1PyA7tjvjKuxDdctbZrPYcIrqfotXdQ62cnvWhWGPRZRa-hDsfrBWygjGz8qn4SVGNV1w9LnYdpBLMao6VTn-pQ4dlhh6gFf1uFOTCWsW5EhXbG4JwifqhLkUfrUBsA-iB2Ivbu43_XoRn3K8QCsaCwTGTLKwGFWNCIjuXyWIgzZHqtYxNDgPShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني في الشارع الرئيسي بمدينة العفولة نتيجة انفجار سيارة ووجود جريح في موقع الحادث.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76104" target="_blank">📅 09:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76103">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏴‍☠️
انفجارات داخل مستوطنة بيرنيت شمال الكيان نتيجة هجوم بمسيرات حزب الله.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/76103" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76102">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي: إيران حاولت مهاجمة القوات الأمريكية على مدى الساعات الـ٢٤ الماضية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/76102" target="_blank">📅 02:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76101">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
إيران حاولت مهاجمة القوات الأمريكية على مدى الساعات الـ٢٤ الماضية.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/76101" target="_blank">📅 02:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76100">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: ‏القوات الأمريكية تصيب أهدافاً تشمل إطلاق صواريخ و‏مواقع وسفن إيرانية تحاول زرع ألغام.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/76100" target="_blank">📅 02:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76099">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: نفذت القوات الأمريكية ضربات دفاعية في جنوب إيران يوم الاثنين.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/76099" target="_blank">📅 02:28 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
