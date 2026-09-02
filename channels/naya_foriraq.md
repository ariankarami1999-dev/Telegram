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
<img src="https://cdn4.telesco.pe/file/pDgYGZG-hmf7-a7_YYynH1Hm1UP4tkto-tgftya1oVN7OPKia9R70tE5aCtHC_kf3qLfy53ZhDsjVxfWfMimsEO3Y3yRDxg-zdGOKce_0LaIAE_S5buvmotGXY403fOYGiJlovNnbmasqKSfP_fEKUu-0rmDpBQJPERM-JuXiI4Sa7yPMx4IFXRdxP7AHBTCbwBZlk6rh_QHFc8u_ysPtqqPlCtqPv6_33dLCHdbrmWzjLJZr-zU-qjxKh_mFT6MFw76HHEOClAVwsN--Hg9eTQdMt90mESou_4H238WUFeqxKH7i1SvYV30UscibVs5dzd6-xFNR3v9l1uYZJla3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 15:40:45</div>
<hr>

<div class="tg-post" id="msg-89219">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
‏
وزير الخزانة الأميركي:
نجري محادثات شاملة مع كل من يدعم إيران. رسالتي إلى الجميع هي أن يبتعدوا عن إيران</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/naya_foriraq/89219" target="_blank">📅 15:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89218">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">في خبر غير مهم
▫️
‏السعودية تدين استهداف إيران لناقلتها المسماة بـ"سدر" خلال عبورها مضيق هرمز.</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/naya_foriraq/89218" target="_blank">📅 14:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89217">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">في خبر غير مهم
▫️
‏السعودية تدين استهداف إيران لناقلتها المسماة بـ"سدر" خلال عبورها مضيق هرمز.</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/naya_foriraq/89217" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89215">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏سعر الغاز الأوروبي يرتفع الى أعلى مستوياته منذ 3 أعوام بسبب تصاعد التوترات في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/89215" target="_blank">📅 13:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89214">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b99536758.mp4?token=VRMQBqnpvU26-x3_r-eZPPiyWT8-9itAR24zm0tRGenbkjkjkzhRyd2uy6egG0RY1fH7cVjnGB_lL25irFWbOAz0TswN6grDdrw7lm3u5W-ljMkvhmvB7mxxUWkRns57a-j4SysHRSpR_5fMOr81TUY3bzOdV4KFejIAsgTHbvwvpU0PDm-kIVZyxIHHIhHgPq82VtDHlpBLqfYS-JORA4cECpA8DPxUbSQr2w1PikdChlsi1huDL0kwWNqH-TsSo3x7wZnB6K3tih0PW6CObHzMaHGia45EcMYvG7l75mqPkRNcs-Ib4-J9d0y81P_rJADJ0HzSv3nTM-0Y4aRnFKOWwGLANT_mXY_MuLw8U0ZcyCEoKeXZHadgGHTb_2a3OJC_a9Z_H63XSjjMCfSy1Vx_drsyylx4jYhxVuWHxGampQbtdaWXo80ebpcvSxqslJXUQxjuLGvtDD4Z8CnyM2SZhOaVZlpjt5ejnKmKLzdpCYn-7vzxtEHVUW4a30-rolXMs-pW49fGaPc1SOag-mDqSwLmGiryzn9GYTJPg6U-3qEXz3cqpiO7zA4e3KEtpmvewugfSCgXYU4yIRipFzvNXB9VJgocPdB-zupXH1JgK0Z8LjPDfsUHlFNQXN0w-UoIEX07eXiEslTrxB47RFt1ElnjCGLEpWGlUk4VVHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b99536758.mp4?token=VRMQBqnpvU26-x3_r-eZPPiyWT8-9itAR24zm0tRGenbkjkjkzhRyd2uy6egG0RY1fH7cVjnGB_lL25irFWbOAz0TswN6grDdrw7lm3u5W-ljMkvhmvB7mxxUWkRns57a-j4SysHRSpR_5fMOr81TUY3bzOdV4KFejIAsgTHbvwvpU0PDm-kIVZyxIHHIhHgPq82VtDHlpBLqfYS-JORA4cECpA8DPxUbSQr2w1PikdChlsi1huDL0kwWNqH-TsSo3x7wZnB6K3tih0PW6CObHzMaHGia45EcMYvG7l75mqPkRNcs-Ib4-J9d0y81P_rJADJ0HzSv3nTM-0Y4aRnFKOWwGLANT_mXY_MuLw8U0ZcyCEoKeXZHadgGHTb_2a3OJC_a9Z_H63XSjjMCfSy1Vx_drsyylx4jYhxVuWHxGampQbtdaWXo80ebpcvSxqslJXUQxjuLGvtDD4Z8CnyM2SZhOaVZlpjt5ejnKmKLzdpCYn-7vzxtEHVUW4a30-rolXMs-pW49fGaPc1SOag-mDqSwLmGiryzn9GYTJPg6U-3qEXz3cqpiO7zA4e3KEtpmvewugfSCgXYU4yIRipFzvNXB9VJgocPdB-zupXH1JgK0Z8LjPDfsUHlFNQXN0w-UoIEX07eXiEslTrxB47RFt1ElnjCGLEpWGlUk4VVHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد سعيدي، أمين لجنة الأمن القومي في مجلس الشورى: يجب أن يعلم العدو أن الجمهورية الإسلامية الإيرانية سترد بقوة على أي إجراء جديد.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/89214" target="_blank">📅 13:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89213">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇹🇷
أردوغان:
يجب ألا يُفسر موقف تركيا بشأن العضوية في منظمة شنغهاي للتعاون على أنه تحول عن الغرب. هدفنا هو زيادة نفوذنا.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/89213" target="_blank">📅 13:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89212">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شبكة NBC الامريكية:
ايران تشن هجمات إلكترونية على بنية تحتية أمريكية مختلفة</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/89212" target="_blank">📅 13:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89211">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇦
انفجارات في كييف.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/89211" target="_blank">📅 13:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89210">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مضحك
🇮🇱
اعلام العبري:
توجيه تهمه لجندي في جيش العدو الاسرائيلي بالانضمام لداعش.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89210" target="_blank">📅 12:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89209">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نايا - NAYA
pinned «
🔻
It seems that the US and its allies in the region are very upset about showing the losses through photos and videos. Therefore, our channel’s name will no longer appear when searched for on Telegram.
🔻
Please share our channel link as widely as possible.…
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/89209" target="_blank">📅 12:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89208">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
It seems that the US and its allies in the region are very upset about showing the losses through photos and videos. Therefore, our channel’s name will no longer appear when searched for on Telegram.
🔻
Please share our channel link as widely as possible.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/89208" target="_blank">📅 12:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89207">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d68394667.mp4?token=ttSZOGgZx9S8hyES5avGuhtLNocA6ccqE_negXG5PzMI_qc3FBkb2dinqbCSQpvbYyGw-63kRjMeSnDko_4Poc95rsGh_Ri4zFFfWb64LaTi58F5cVjL_xUgduDmhKM0QTahxr8ATdbE51HqWVAHLg_o07ojIi5clEpgT4MjNOmd9Kb9mbBSyL0kG-M45LPLokmvfYMcWeH65WLDhfraL7XyudLWSSCQ0ax_XFBPS96taNjGOz4RD8cFDTOi7Yl5OS2PRK_MNkw2CfNKzy2X-Edmj1sjRs0yDHNOgjC48mkBksn0rRInVxxlhCUiEnYpQj0qR1xheD8z4K3_tilawA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d68394667.mp4?token=ttSZOGgZx9S8hyES5avGuhtLNocA6ccqE_negXG5PzMI_qc3FBkb2dinqbCSQpvbYyGw-63kRjMeSnDko_4Poc95rsGh_Ri4zFFfWb64LaTi58F5cVjL_xUgduDmhKM0QTahxr8ATdbE51HqWVAHLg_o07ojIi5clEpgT4MjNOmd9Kb9mbBSyL0kG-M45LPLokmvfYMcWeH65WLDhfraL7XyudLWSSCQ0ax_XFBPS96taNjGOz4RD8cFDTOi7Yl5OS2PRK_MNkw2CfNKzy2X-Edmj1sjRs0yDHNOgjC48mkBksn0rRInVxxlhCUiEnYpQj0qR1xheD8z4K3_tilawA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تم رصد حريق في مجمع عسكري أمريكي بالقرب من مطار أربيل الدولي.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/89207" target="_blank">📅 12:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89206">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOST_WVnlZnrbixFD0aQGgglbbMInIsMbhVxi83fn-5YBGL4r4M4Ep0gCtIZIhA1XuA-LL1UGAOYEKDKxcm9eMQyyR9pQgIc5xj80wvGc6ST7FwMnBi7odKbfsMz1YjRocCY8KHByXINot42Af8kpaQp2wAgYvo5cpmKp98LYVlCTXupB5XN5lmPHuaYkz14Pm1d8NKR0ZvTP1OzCGWy9bZnW4sbYsNOEDo0NWBvuBpWgs_aCEoGEQutqf9q_T2OiRTiuFKY6O5cchJ01h61A4oyPf0wC-UU6nNCSQR0Q_ZnWTMZQaU88UvRw0qeut1hm0AHCx5oYxK7SpS5HQ4ZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇪
مروحية اميركية تطلق نداء استغاثة فوق الامارات.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89206" target="_blank">📅 12:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89205">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
الحرس الثوري:
تم تفجير ناقلتين نفطيتين انتهكتا القانون وإيقافهما بعد اصطدامهما بلغم. سيتم مضاعفة العقوبات على شركات الشحن التي تنخدع بالولايات المتحدة بدلاً من اتباع الإجراءات القانونية.
العلاقات العامة للحرس الثوري الإسلامي:
بسم الله، قاسم الجبرين
وقاتلوهم حتى لا تكون فتنة و تكون الدين لله
يا شعب إيران الإسلامي الباسل الصامد، لقد ألهم صمودكم في الميدان الأمم، والعالم يشهد عملية إيقاظ الشعوب وتضييق الخناق على القوى الإجرامية المتغطرسة.
الليلة الماضية، كرر جيش أمريكا الإرهابي سيناريو الترهيب الذي نفذه مراراً وتكراراً في عدوانه على دول مختلفة، وهو مهاجمة حفل زفاف لإظهار قسوته ووحشيته وإرهاب الناس. غير مدركين أن الشعب الإيراني ليس شعبًا يخشى هذه الألاعيب، وأن هذا ليس عصر إذلال الأمم وخضوعها. لقد استيقظ العالم، وهذا القرن هو قرن إرادة الأمم في الانتصار.
بهذه المناورات الوحشية، لن يضعف تحكم قواتنا في مضيق هرمز.
أود إبلاغكم، أيها السادة، أنه قبل ساعات قليلة، انفجرت ناقلتا نفط، حرضهما الجيش الأمريكي على إنزال طاقميهما ووضعهما في أيدي عملاء أمريكيين لعبور طريق غير شرعي، وتوقفتا عند مرورهما فوق لغم بحري، وهما الآن تحترقان.
وكانت البحرية التابعة للحرس الثوري الإيراني قد حذرت سابقًا من مخاطر العبور عبر ممر ملغوم، بالإضافة إلى ذلك، تم التخطيط لعقوبات إضافية لشركات الشحن التي تقع ضحية حيلة الولايات المتحدة وتضع سفنها تحت تصرف العدو بدلًا من اتباع المسار القانوني، وسيتم تنفيذ هذه العقوبات قريبًا.
والنصر من عند الله وحده، العزيز الحكيم</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/89205" target="_blank">📅 11:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89204">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">أسعار الغاز الأوروبي تلامس 74 يورو للميغاواط/ساعة مقتربة من  ذروتها مع استمرار اغلاق الجمهورية الاسلامية لمضيق هرمز.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89204" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89203">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇱
🇺🇸
وزير الحرب الصهيوني:
مستعدون للدفاع والهجوم بتنسيق كامل مع أميركا.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89203" target="_blank">📅 11:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89201">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات جديدة تهز الكويت</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89201" target="_blank">📅 09:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏
🇷🇺
🇩🇪
تشك الشرطة الألمانية في عملية تخريب بعد حادث متعمد في محطة كهرباء فرعية في بيرغهايم أدى إلى تعطل عدة خطوط نقل وتعطيل منشآت ريفا . وأفاد السكان بسماع انفجارات ورؤية ومضات خلال الليل.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89200" target="_blank">📅 09:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89199">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏
🇷🇺
🇩🇪
تشك الشرطة الألمانية في عملية تخريب بعد حادث متعمد في محطة كهرباء فرعية في بيرغهايم أدى إلى تعطل عدة خطوط نقل وتعطيل منشآت ريفا . وأفاد السكان بسماع انفجارات ورؤية ومضات خلال الليل.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89199" target="_blank">📅 08:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇷🇺
عمدة موسكو :
تدمير 3 مسيّرات أخرى كانت متجهة نحو موسكو</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/89198" target="_blank">📅 08:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89192">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f8e598b.mp4?token=ZDzk0ROx8iM1wy4ZvWC55iK9CVccR2FaH0jl8cXcUcIM7nZWzaG9__1jw3F53O7JBzKPKPqueGzPZ8UOwCb6myNKd1q2L4vjhBirpdB1crCe7IzRBnFWnAWw8FcBFaDZXWol7H4hPBFVmEyJJegWomaYtmL73EBPOcRqOBMSXGlA0Y0TnHtUVajlUxTefEVBjSqD7wwqzOZaQywixRiLdE0edyqh2Ofv03S4qs6_JbLSpbmI72RIiDhhw4sSt0gQzbqgCZDiEUCjC03xjsmkkLninPbX_XtM4rP9Xh1RqyEYvSE4Nmo950p-GeImyjaRfHPeQ6gJiJtI_843X2eEaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f8e598b.mp4?token=ZDzk0ROx8iM1wy4ZvWC55iK9CVccR2FaH0jl8cXcUcIM7nZWzaG9__1jw3F53O7JBzKPKPqueGzPZ8UOwCb6myNKd1q2L4vjhBirpdB1crCe7IzRBnFWnAWw8FcBFaDZXWol7H4hPBFVmEyJJegWomaYtmL73EBPOcRqOBMSXGlA0Y0TnHtUVajlUxTefEVBjSqD7wwqzOZaQywixRiLdE0edyqh2Ofv03S4qs6_JbLSpbmI72RIiDhhw4sSt0gQzbqgCZDiEUCjC03xjsmkkLninPbX_XtM4rP9Xh1RqyEYvSE4Nmo950p-GeImyjaRfHPeQ6gJiJtI_843X2eEaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
Trump’s Target Bank;  For Those Asking Where U.S. Taxpayer Money Is Being Spent?!
Naya exclusively publishes video footage showing CENTCOM  target bank in the Iran “ Serik” , and how a wedding ceremony has become one of the targets of the U.S. military.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89192" target="_blank">📅 08:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89191">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
جريمة حرب أمريكية في مدينة سيريك جنوبي إيران، حيث إستهدفت حفل زفاف بقنابل شديدة الإنفجار، لتخلف 5 شهداء وعدد كبير من الإصابات حتى الأن، بينهم الكثير من الأطفال والنساء.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/89191" target="_blank">📅 08:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89190">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇱
🔻
معاريف :  أطلق حزب الله طائرة مسيرة باتجاه الشمال: تقييم الجيش الإسرائيلي - إيران وافقت على هذه الخطوة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/89190" target="_blank">📅 07:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89189">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
🇺🇸
رويترز :
الأسواق الآسيوية تتراجع بشدة مع ارتفاع أسعار النفط وعوائد السندات بسبب القتال بين الولايات المتحدة وإيران</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89189" target="_blank">📅 07:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89187">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5HySqNFdPt26Ajld_JB8x-BEdsvbfJWzqudpI3xI2kyW9ksGtruOAAondLue-mjkT3Ar-UFPVPgm4yyy_e90kaluohm2HyaS4Oc1lzagQcjr80uGtbNFy6ocHJ56nAmAfkNjFaOdhiPkzk6ASVWLAWt6TTf579r8nGTQ3Qz1C0g90OFSC3eBQYeYnSFNk38yuOVr0PnFnl7DMJkMbNvq7y44szZ-XLdTGysmkjQ1ppoecZ6rybnLUfi8y3IfEtXhR-iIPGRLFcwpU-YxRR9_RS_myF7Dc8wsb_s1CuWfMhgE09rUvkAof3FKi-hPUVI1y64HK8S-7knPbTI5VWvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
Save this song
🎧</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89187" target="_blank">📅 07:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89186">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات في البحرين</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89186" target="_blank">📅 06:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89185">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجارات في البحرين</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/89185" target="_blank">📅 06:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89184">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عدوان أمريكي على نقاط في محيط مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/89184" target="_blank">📅 06:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89183">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوي انفجار في شمال فلسطين المحتلة</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/89183" target="_blank">📅 05:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89182">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83359493e.mp4?token=McTENATpqgkzqZgXGuDTMdyMyK5AsiOiUFyAOROkS-2yqbM0IJMNY7-yZr7sGPi6EwyzHfw9wDijHHCY-C3ETSXLzEQ6BXjO2vUl4czUX2X_7ohcrW7_ILu64Zy5HjIsPQ3PJ_PX6gNflOpBjenWfetV0y0MNp1ZZf87m6Wi73kWAn57dMQ5FP-6TGhJquA_nxaCjWyWklwBfoU55JFvf8OJ5IpPB_zCh0m0RU3qOi0w8SXxmBNxareuVD2kjAQQq54n0L24zB5wR5z9uiIfiqRl3qas3J5NXbVx4gNww0yE5VMvT_yLK-awyPbUZ6iVjyza8tMIqQdQVfWrMrEpyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83359493e.mp4?token=McTENATpqgkzqZgXGuDTMdyMyK5AsiOiUFyAOROkS-2yqbM0IJMNY7-yZr7sGPi6EwyzHfw9wDijHHCY-C3ETSXLzEQ6BXjO2vUl4czUX2X_7ohcrW7_ILu64Zy5HjIsPQ3PJ_PX6gNflOpBjenWfetV0y0MNp1ZZf87m6Wi73kWAn57dMQ5FP-6TGhJquA_nxaCjWyWklwBfoU55JFvf8OJ5IpPB_zCh0m0RU3qOi0w8SXxmBNxareuVD2kjAQQq54n0L24zB5wR5z9uiIfiqRl3qas3J5NXbVx4gNww0yE5VMvT_yLK-awyPbUZ6iVjyza8tMIqQdQVfWrMrEpyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇱🇧
غارات صهيونية عنيفة على منطقة دوحة كفررمان بجنوب لبنان.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/89182" target="_blank">📅 05:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89181">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في شمال فلسطين المحتلة خشية إختراق طيران مسير قادم من لبنان.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/89181" target="_blank">📅 04:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89180">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في شمال فلسطين المحتلة خشية إختراق طيران مسير قادم من لبنان.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/89180" target="_blank">📅 04:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89179">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات جديدة تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/89179" target="_blank">📅 04:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89178">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/89178" target="_blank">📅 04:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89177">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLfXlUZbwIYrEEm2Mv8TKWJvx9eEgb3x5GCNz-0KCmwXRwZ7MPNlADkcIFUYolqW_E6zky8gDIiDjcP8yT90qFdFptK4To9Ufny_IjXJIh-bEsEziSWtYUGr2uqjxDZfBpr2WUAihw0d95O_zE6JoTdAF0iFdH8qNtdTsKPTbzJ5DYK_idAq27pmZnnmhBLjbWNxlrTLDn76JuzLGD900jhkp6I2ark0nLoWZ2PTQE1xHWopA4ihF7usI4Hs5_g53ZrkbsVtgSRReH2WeEuEebcyFXyk_oFg7tXSvWyQemYSH2XCeLWEamLoMDXMt3nbFpC2Gxaw7-3KjBxZ0kQeVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
أنا لا أحاول إجبار إيران على الجلوس إلى طاولة المفاوضات، كما ذكرت قناة ABC الإخبارية الكاذبة. لا يهمني إطلاقًا ما إذا وقعوا على اتفاقية لا قيمة لها بالنسبة لهم. أنا أفضل وضعنا الحالي بكثير، مع سيطرة شبه كاملة على مضيق هرمز، واقتصادهم ينهار تمامًا. إنهم فقط يجسدون ما لا مفر منه. متى سينتفض الشعب الإيراني ويقاتل؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/89177" target="_blank">📅 04:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89176">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgHmE2RjHEdAPz0aJRJKGj4X43m8j72MUcyRaWOZMS9CYgAJAXapQPn0Szg8sfs9yjRmv5F-oY5sYeY1htWnWf2TAKeXk5tO-l12lIsDAkX_efLqgkVme8WsNSfR8IZVdn_ogXy0tQUcuJUZssmB6wmHh-Yxi_FEKAHmbt6Jgxawg-xkAO14ViIFqFD5ZvKagb4ogX_5T5BpCn1ScxWEWIF3oRIgv0GA2skvKLxnjHeqRXKW2DwsfzquetUkbWTlacxp7gv1C3SoMJYstP-7m_SMBJ7eeKFiB-M2T-sMu-8enAKaFsDkwBqZkXQJb8Nifw9lnFewsSgOeES8cGykQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النفط يلامس 97 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89176" target="_blank">📅 04:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89175">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/89175" target="_blank">📅 04:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89174">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d9d5c89e.mp4?token=Pqh2v0IEv7EWH6to00bJvleaKTmI4sjJQa7jPT5BKUOi2Z7mooaUV-Eyr1dGKqfW1h9rx9_s4vhpri2WPe0ED2W5DYNDXu-4DvzjA34EtZkolFcOPDMd14Art2mv3A77oIov6wc9S1Bt6Eul-azUA5GpubcRpYYNfN7vdOgxyvrdwlYCq3GjBcvvwcHoWuh2FJD0EA3wj-OBd7Qrev33WQxHe7kHNYEkVQ6rmF4EYHwk_Gko5Yd2pwc_NYXtxqKONwd9-YgEFOcOLBKKHwgMSipWzukAytR_6KAWXbhwLtBReDutAC5ZqYsnxfo8FK0AU8O_L8EexNLVH4sAdAS9Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d9d5c89e.mp4?token=Pqh2v0IEv7EWH6to00bJvleaKTmI4sjJQa7jPT5BKUOi2Z7mooaUV-Eyr1dGKqfW1h9rx9_s4vhpri2WPe0ED2W5DYNDXu-4DvzjA34EtZkolFcOPDMd14Art2mv3A77oIov6wc9S1Bt6Eul-azUA5GpubcRpYYNfN7vdOgxyvrdwlYCq3GjBcvvwcHoWuh2FJD0EA3wj-OBd7Qrev33WQxHe7kHNYEkVQ6rmF4EYHwk_Gko5Yd2pwc_NYXtxqKONwd9-YgEFOcOLBKKHwgMSipWzukAytR_6KAWXbhwLtBReDutAC5ZqYsnxfo8FK0AU8O_L8EexNLVH4sAdAS9Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إنفجارات جديدة تهز أربيل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/89174" target="_blank">📅 04:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89173">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
مسؤولون أميريكيون: ‏ الجيش الأمريكي يهاجم ناقلتين تابعتين للحكومة الإيرانية.  ‏سنستهدف ناقلة نفط إيرانية مقابل كل سفينة تهاجمها إيران.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89173" target="_blank">📅 04:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89172">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">إنفجارات قوية تهز محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89172" target="_blank">📅 04:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89171">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
تحذير من المتحدث باسم مقر خاتم الأنبياء المركزي:  بسم الله الرحمن الرحيم.   الجيش الإرهابي القاتل للأطفال الأمريكي، بعد سلسلة من الإخفاقات في الحرب المفروضة على إيران الإسلامية، وهزيمته أمام شعبنا الصامد والمقاوم في وطننا العزيز، قام بشن غارات جوية وحشية…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89171" target="_blank">📅 04:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89170">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">إنفجارات جديدة تهز أربيل</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89170" target="_blank">📅 04:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89169">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
مسؤولون أميريكيون:
‏
الجيش الأمريكي يهاجم ناقلتين تابعتين للحكومة الإيرانية.
‏سنستهدف ناقلة نفط إيرانية مقابل كل سفينة تهاجمها إيران.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89169" target="_blank">📅 03:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89168">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
تحذير من المتحدث باسم مقر خاتم الأنبياء المركزي:
بسم الله الرحمن الرحيم.
الجيش الإرهابي القاتل للأطفال الأمريكي، بعد سلسلة من الإخفاقات في الحرب المفروضة على إيران الإسلامية، وهزيمته أمام شعبنا الصامد والمقاوم في وطننا العزيز، قام بشن غارات جوية وحشية وقصف على بعض المواقع العسكرية والمدنية في المناطق الجنوبية من إيران، مما أدى إلى استشهاد وإصابة عدد من المواطنين الأبرياء.
في رد فعل على هذه الجرائم والأعمال الإرهابية، قامت القوات المسلحة للجمهورية الإسلامية الإيرانية، بفضل أبناء الشعب الشجعان في الجيش الباسل والحرس الثوري الشجاع، بشن هجمات قوية ومؤثرة بالصواريخ والطائرات المسيرة على المواقع الأمريكية الإجرامية في المنطقة، مما أدى إلى تدميرها وإلحاق أضرار جسيمة بالبنية التحتية والمرافق والأسلحة والمعدات، وأدى أيضًا إلى مقتل أو إصابة عدد كبير من القادة والجنود الأمريكيين.
ستستمر هذه العملية الهجومية كدرس قاسٍ للأمريكيين حتى يندموا على جرائمهم.
نحذر من أن استمرار أفعال الأمريكيين الشريرة في المنطقة سيواجه ردود فعل أشد وأوسع وأكثر تدميراً، وأن أي دولة تتعاون مع الجيش الأمريكي المعتدي يجب أن تتحمل عواقب ذلك الخطيرة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/89168" target="_blank">📅 03:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89167">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات في الأردن</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/89167" target="_blank">📅 03:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89166">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e0d9f677.mp4?token=vR92xnsRAoy3HTDjB2GClxtVBs7vPJMYmDFYoGR2TtgDp2IAcBk0zHsvV7Wl9O_ZWdEdQzN76nm8dmYxYYn5Lk5d_LlunYs97GxdQYeq6AxERu5r0fleH0PM2ZOYrz5DMRZu4yLfxGyvOUKlvZrc1BC4Uw1MhlxFxJ7O0bs9fs3swVNF0SXFMA_m837mfSrXTC6zYWF2tI4GAWcjQ7STSJQ6AOdLLm81Ho2jk-RwjA5vSCYVTOqJwG8WIc1hUPV9t3dFGVRGZqBp6vbv5AG3xBnBKBFLTWayaj2oBsS44sJ85y2-Y6gLcwZ_96TWtq9HwOaekCUGT1nFCFkLyJPDVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e0d9f677.mp4?token=vR92xnsRAoy3HTDjB2GClxtVBs7vPJMYmDFYoGR2TtgDp2IAcBk0zHsvV7Wl9O_ZWdEdQzN76nm8dmYxYYn5Lk5d_LlunYs97GxdQYeq6AxERu5r0fleH0PM2ZOYrz5DMRZu4yLfxGyvOUKlvZrc1BC4Uw1MhlxFxJ7O0bs9fs3swVNF0SXFMA_m837mfSrXTC6zYWF2tI4GAWcjQ7STSJQ6AOdLLm81Ho2jk-RwjA5vSCYVTOqJwG8WIc1hUPV9t3dFGVRGZqBp6vbv5AG3xBnBKBFLTWayaj2oBsS44sJ85y2-Y6gLcwZ_96TWtq9HwOaekCUGT1nFCFkLyJPDVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف بالون تجسسي أمريكي في سماء أربيل بواسطة مسيرات الإنتحارية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89166" target="_blank">📅 03:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89165">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">استهداف بالون تجسسي أمريكي في سماء أربيل بواسطة مسيرات الإنتحارية</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89165" target="_blank">📅 03:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89164">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969bbbd207.mp4?token=V-cKWZM1_UPVgTe5MjTcHpwJWuMV-wFDZIAM31UfVwaendKsMhROj7liM4ZT1Dipiuol_pmuzOtY8UCYwK39gSwk1-ZPjIwk1iw-p_ErfY1w5nLiWj0cpxyVsONhr6mrB5R6idygF4I9F1u4Ym-A42TVSKwCdr8_Fl0PyT9AN1xpETtDV8vSO6O2RiGVkS9EcOyYbON8-OUWWqRlsTj_ZC2zNOKL6mmZwH9ltAxhuA45DGMkJlSA1dZsXZAJWVxA8FYCT54XPAWZTs0ANKbHsJU69BGGsAUSI3jK0JQ3eN_OcTlX7gThxrRu9tEbjaSDoKpcsuoP38xeypEzEVyrfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969bbbd207.mp4?token=V-cKWZM1_UPVgTe5MjTcHpwJWuMV-wFDZIAM31UfVwaendKsMhROj7liM4ZT1Dipiuol_pmuzOtY8UCYwK39gSwk1-ZPjIwk1iw-p_ErfY1w5nLiWj0cpxyVsONhr6mrB5R6idygF4I9F1u4Ym-A42TVSKwCdr8_Fl0PyT9AN1xpETtDV8vSO6O2RiGVkS9EcOyYbON8-OUWWqRlsTj_ZC2zNOKL6mmZwH9ltAxhuA45DGMkJlSA1dZsXZAJWVxA8FYCT54XPAWZTs0ANKbHsJU69BGGsAUSI3jK0JQ3eN_OcTlX7gThxrRu9tEbjaSDoKpcsuoP38xeypEzEVyrfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
قوات الاحتلال الامريكي تعيد رفع بالون التجسس في سماء محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89164" target="_blank">📅 03:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89163">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPTDPix-OdXL_jn20xD2bkgesn-3oUsEjkwaw_AUCGgILUMAdJkrbfDtb53CUD81WrpsObe4OQ1T1nzPtbik7QPmf2En5CXwxVUeV2xgXTPiZeck3DJlzeaw8P9Io9FlR-Yz0L2QM0l_9CTiiGl94THrBdzP8tPa46x2tg2qKl3nY3x78wCc7l0UNDUysYO4OE3krHKqPXNw_N41fFblgO0kMh4K58uH3_earGUkK-ZppiHX5cKA6TcNhEeZ7Ps0xx8ylWlACg6yXgaGHzfPbWHfOotvnCW9hSUXSPS9NBjNft-6kUFAeh1SL8qyGduVx_NwSmgqennRuHUKQtZOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تأكيدا لما اعلن عنه الحرس الثوري.. إشتعال النيران في القاعدة الأمريكية بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89163" target="_blank">📅 03:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89162">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82dcc6038.mp4?token=T2r3zbkVOibN6ve8yEGXZPGfv4du84JwxUQWQSFtDeCZN4WB60_ByyTdszrOmGlIK1TMZFAgMX9D2z2DsGezfTFGn5Z8ib7RhsPKEaNfa5GbaQICHN1caIYsZ3eAWnmVVvZhjlBbjqdF3yR4uiPtH7lx5GyAc5C8veECCRgTmnUT8EwKDA4Yo0nCCnZonwhfLu_DW94anS45uwlIZXPvUt1EWFxmED5iTQWVDaWBRyi1Vvj4O7N3h5375MgNT0FOBfhXOzKLkVpW1amv21Y37_XDJiu07AbZPWdJZfrQJC1ExDsh5ffP-rwmnnxPz9VqZyDd0V8lEXM9vtTI1prJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82dcc6038.mp4?token=T2r3zbkVOibN6ve8yEGXZPGfv4du84JwxUQWQSFtDeCZN4WB60_ByyTdszrOmGlIK1TMZFAgMX9D2z2DsGezfTFGn5Z8ib7RhsPKEaNfa5GbaQICHN1caIYsZ3eAWnmVVvZhjlBbjqdF3yR4uiPtH7lx5GyAc5C8veECCRgTmnUT8EwKDA4Yo0nCCnZonwhfLu_DW94anS45uwlIZXPvUt1EWFxmED5iTQWVDaWBRyi1Vvj4O7N3h5375MgNT0FOBfhXOzKLkVpW1amv21Y37_XDJiu07AbZPWdJZfrQJC1ExDsh5ffP-rwmnnxPz9VqZyDd0V8lEXM9vtTI1prJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أعمدة النيران والدخان تتصاعد من القاعدة الأمريكية في أربيل عقب هجوم صاروخي وبالمسيرات من قبل الحرس الثوري.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89162" target="_blank">📅 03:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89161">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f9def1c1.mp4?token=e029GzM9synD3aOz4aOKKpOv43tf4gkrcE2nKlvp4XmgQAzd7Dk-ddd213OjCYkqS91LQggmLtXM9DoeTzNZJjtpazlr19I4V7HHUK7IHp2Oe50kpoX5SflvSpAyd4ZFMJru3gf-4lhiyu8FSrNSbzZNsvcgoz84_GcWfZZ5l3hfMWBLQrLkQ0akd2s-G3VJp_mChiM-rNAtvYKqZ3F9IlvKqbN8zVJmm_xAcnsC0dZg7jzgdZS4PGhofnFPSabX9XdgVME5KDOAHj0_JJuZqefJeKmwQXDlUz-Uhz3PLKErnfHW7RW0QzEKNhIQjtFUUDoGimwPXnQwwooYNLjf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f9def1c1.mp4?token=e029GzM9synD3aOz4aOKKpOv43tf4gkrcE2nKlvp4XmgQAzd7Dk-ddd213OjCYkqS91LQggmLtXM9DoeTzNZJjtpazlr19I4V7HHUK7IHp2Oe50kpoX5SflvSpAyd4ZFMJru3gf-4lhiyu8FSrNSbzZNsvcgoz84_GcWfZZ5l3hfMWBLQrLkQ0akd2s-G3VJp_mChiM-rNAtvYKqZ3F9IlvKqbN8zVJmm_xAcnsC0dZg7jzgdZS4PGhofnFPSabX9XdgVME5KDOAHj0_JJuZqefJeKmwQXDlUz-Uhz3PLKErnfHW7RW0QzEKNhIQjtFUUDoGimwPXnQwwooYNLjf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تأكيدا لما اعلن عنه الحرس الثوري.. إشتعال النيران في القاعدة الأمريكية بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/89161" target="_blank">📅 03:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89160">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ece92424e.mp4?token=Ux2C73JStRZUXdRvyteWT7tyLlUVJFn1G03r3VBFCaQmaoCnt7axbYK51vxgHZaJztv7aqDdXAjbdd4mUIGMmvXtFJcyM3iu0Z2YPOvU0Upyge_EW9hwpIOk3CZ-4gVSAQLbz2ZI1A1sy1pOWWvexac3Sp20wn9VdKhLpoIkuHbcBJS83eajaTXcQ5nEq5gJwej4BM6jPbY0UV4oq4VZpZ59ohQ9IDZZUdn6nAuVWWtQV7t6IjD5R5rnJaH6VsWUxIdTkk9DrpsErnD5jleDnbgDMAxOiduHRIuVaQUAe-iVC2esg3DIEZHMFkNeYsS11JH88Wrboghbo2BKBEhdfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ece92424e.mp4?token=Ux2C73JStRZUXdRvyteWT7tyLlUVJFn1G03r3VBFCaQmaoCnt7axbYK51vxgHZaJztv7aqDdXAjbdd4mUIGMmvXtFJcyM3iu0Z2YPOvU0Upyge_EW9hwpIOk3CZ-4gVSAQLbz2ZI1A1sy1pOWWvexac3Sp20wn9VdKhLpoIkuHbcBJS83eajaTXcQ5nEq5gJwej4BM6jPbY0UV4oq4VZpZ59ohQ9IDZZUdn6nAuVWWtQV7t6IjD5R5rnJaH6VsWUxIdTkk9DrpsErnD5jleDnbgDMAxOiduHRIuVaQUAe-iVC2esg3DIEZHMFkNeYsS11JH88Wrboghbo2BKBEhdfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الحرس الثوري:   قام مقاتلو القوة البرية لحرس الثورة الشجعان بهجوم مدمج باستخدام الصواريخ والطائرات المسيرة على القواعد الأمريكية في أربيل، مما أدى إلى تدمير مركز إصلاح ومخازن للمعدات الفنية لجيش الإرهاب الأمريكي، وتدمير نظام توجيه منطاد التجسس الأمريكي في…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89160" target="_blank">📅 03:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89159">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔻
الحرس الثوري:
قام مقاتلو القوة البرية لحرس الثورة الشجعان بهجوم مدمج باستخدام الصواريخ والطائرات المسيرة على القواعد الأمريكية في أربيل، مما أدى إلى تدمير مركز إصلاح ومخازن للمعدات الفنية لجيش الإرهاب الأمريكي، وتدمير نظام توجيه منطاد التجسس الأمريكي في القاعدة. كما قام مقاتلو القوة البرية الشجعان بإشعال خزانات الوقود في القاعدة، وقتلوا عددًا من المعتدين.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89159" target="_blank">📅 03:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89158">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات جديدة تهز الكويت</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89158" target="_blank">📅 03:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89157">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
واشنطن بوست:
القوات الأميركية تعترض الضربات الإيرانية حتى ساعات متأخرة من الليل.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/89157" target="_blank">📅 03:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89156">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d072c568f0.mp4?token=eQDZiP3Dyey_kVHrXihhUjd-cfX9RQIjfc0XHlolkEbijj8RXomXhW8UnCHRRb0GnHGt0BzJhQauJAxtWMxNCmwcMRt6dIwv02oHV0joTYsNjjLT5zZUVRc77Pq7SvKizAMGZUQfiKo2gezWoyA6VPkVemmql6YPld_5R0w-3L-d0Q6zw2N5O6cV-AJiuQJJvTM6p-0PdnBeptz2eNtZHI1OL2-E44YzWxGDTguL-C5AxuJsflNcn_GvSfSVtgOwInNiBli8RBCYatKgcFZXyPGBM-5oJ4D2W7m3bKYydGF5iuypR-Zzi9-zODgSO_20whQg9ge0TdAsVTWmX4QSHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d072c568f0.mp4?token=eQDZiP3Dyey_kVHrXihhUjd-cfX9RQIjfc0XHlolkEbijj8RXomXhW8UnCHRRb0GnHGt0BzJhQauJAxtWMxNCmwcMRt6dIwv02oHV0joTYsNjjLT5zZUVRc77Pq7SvKizAMGZUQfiKo2gezWoyA6VPkVemmql6YPld_5R0w-3L-d0Q6zw2N5O6cV-AJiuQJJvTM6p-0PdnBeptz2eNtZHI1OL2-E44YzWxGDTguL-C5AxuJsflNcn_GvSfSVtgOwInNiBli8RBCYatKgcFZXyPGBM-5oJ4D2W7m3bKYydGF5iuypR-Zzi9-zODgSO_20whQg9ge0TdAsVTWmX4QSHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عنيف يهز أربيل</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89156" target="_blank">📅 03:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89155">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">استمرار الإنفجارات في أربيل شمالي العراق وسط هجمات واسعة بالطائرات المسيرة الإنتحارية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/89155" target="_blank">📅 03:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89154">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوي 4 انفجارات في البحرين</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89154" target="_blank">📅 03:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89153">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d20633795a.mp4?token=b74AXtnN5ZPFzYCSUozJGrZUDF5tObspbaHqy8vi5Q4KX_yMjmOQG6Iu9xRWaksIABpgTtayT30hpz6Y_rn5IX2sFH8iiWnUTHODf9nuQCyYOJ3iGA2EeGBCNaSdDcw6U7ygr1MREfJbEidoHE2F0rDInDL_5BSITC-32caeccAOVbE7LzaeqS2Ee24yByyHRE7H8-0e277bQBvgnYGDtBMf3VzdimEVxmQdS8wwwUG2Rlr0wIrjt8kuj0dJhg3UfT1X0OhkogZnJpZTkBbuxadUJbd6JgO3BZFYv2QBmBOUw2C8z_p4NM1-yoWdZMmPtbacd_1N0BDCDLzc-GBCdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d20633795a.mp4?token=b74AXtnN5ZPFzYCSUozJGrZUDF5tObspbaHqy8vi5Q4KX_yMjmOQG6Iu9xRWaksIABpgTtayT30hpz6Y_rn5IX2sFH8iiWnUTHODf9nuQCyYOJ3iGA2EeGBCNaSdDcw6U7ygr1MREfJbEidoHE2F0rDInDL_5BSITC-32caeccAOVbE7LzaeqS2Ee24yByyHRE7H8-0e277bQBvgnYGDtBMf3VzdimEVxmQdS8wwwUG2Rlr0wIrjt8kuj0dJhg3UfT1X0OhkogZnJpZTkBbuxadUJbd6JgO3BZFYv2QBmBOUw2C8z_p4NM1-yoWdZMmPtbacd_1N0BDCDLzc-GBCdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات جديد تهز قضاء سوران بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/89153" target="_blank">📅 03:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89152">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe8fe7da1.mp4?token=QmBFYMV_ROvAHx7x_PEUIMr0ZZ6pWUKVruhItgvPjQYJRnhzLkAivUT1rLndJhe6J2zOqRW3iqb-ImTdkv38lnbQpBR5GmC0znquahp3oj-WaXup-cycrhvpFeg1u6nhJ9caOcww8V7oq-mjwFwzUjtJuyrDUORBM4otd7Lm7y0C8pQm7eXp4RfDQq0tIDnap2kCEQwmuSUK5s9APm5n-bJF3bOqHshQjKZCNr6PhhsHIphZ37l0dfWWMMguS2xrFBFhw3c4nfSKjLpBsNTljmNhFXGiFlr3lK0BnAF4VsH0KpiGBTSkgjzA8YSAYzTCCUZ328RWo7di3VMOfugKxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe8fe7da1.mp4?token=QmBFYMV_ROvAHx7x_PEUIMr0ZZ6pWUKVruhItgvPjQYJRnhzLkAivUT1rLndJhe6J2zOqRW3iqb-ImTdkv38lnbQpBR5GmC0znquahp3oj-WaXup-cycrhvpFeg1u6nhJ9caOcww8V7oq-mjwFwzUjtJuyrDUORBM4otd7Lm7y0C8pQm7eXp4RfDQq0tIDnap2kCEQwmuSUK5s9APm5n-bJF3bOqHshQjKZCNr6PhhsHIphZ37l0dfWWMMguS2xrFBFhw3c4nfSKjLpBsNTljmNhFXGiFlr3lK0BnAF4VsH0KpiGBTSkgjzA8YSAYzTCCUZ328RWo7di3VMOfugKxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تشعل سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89152" target="_blank">📅 02:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89151">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوي 4 انفجارات في البحرين</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89151" target="_blank">📅 02:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89150">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عدوان أمريكي على نقاط في محيط مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/89150" target="_blank">📅 02:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89149">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c515323a.mp4?token=SWMXGLnHTpDn2Sv9sMSjY-S5_GS9AIWyK73Pf6f3fdDIdqRpT7mgFrOyuXMDH8oMEb_mvMaE10i8Wba1hDyimNKmvlXtZF4aE7dmrutxvs5jQ2_y4yHT0dstvQdrCSregAPD04jMIock4AGM9ZGj_ubODfmV7NCXLNXo3-tYgaiN2i7uQcEynWiKGq8sfsVMwrC4uW_C5UP5PUFQGc7xXXT3WoxlaNte4bljVFiR790NQRnk1d1MU8cSChdKHMQO2wadTt0bp8Z8H2dv5uAxf1kUAO8vp2-ZfFpCaf7wvpjolEWhwu0qjjLEQPqDTIS57rY1z0zxxegQ48Iqh9Dviw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c515323a.mp4?token=SWMXGLnHTpDn2Sv9sMSjY-S5_GS9AIWyK73Pf6f3fdDIdqRpT7mgFrOyuXMDH8oMEb_mvMaE10i8Wba1hDyimNKmvlXtZF4aE7dmrutxvs5jQ2_y4yHT0dstvQdrCSregAPD04jMIock4AGM9ZGj_ubODfmV7NCXLNXo3-tYgaiN2i7uQcEynWiKGq8sfsVMwrC4uW_C5UP5PUFQGc7xXXT3WoxlaNte4bljVFiR790NQRnk1d1MU8cSChdKHMQO2wadTt0bp8Z8H2dv5uAxf1kUAO8vp2-ZfFpCaf7wvpjolEWhwu0qjjLEQPqDTIS57rY1z0zxxegQ48Iqh9Dviw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات مسيرة انتحارية تحلق في سماء أربيل</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89149" target="_blank">📅 02:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89148">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f89d8f81.mp4?token=dv1rkUO7a24r8ZsdhSLP1MpM15giPJgShdi8mAqrebgM3-AyB5H6D6KgvOcODoEmkRftDaa8htf-Q9iN2e-g6BAEdHZlguWupgRcQ8K2FBtHF3bJfsciFdg5wSh5hwVQZq8qAlXC9j40-o8MDuUEMa_udbBKRUVRFcm0lo8OByQpNMEX9yCiCG6YQo3ZTRJFVtY3yhRGjLNho96NLCmm338Y91V8UFYA_vL54E_lkutkLduJdtLkaKzz4HpitH0aMj2KQOii4w15ngqoOJU5OEzM8vvb2BvN8uRd6b8tvHWxWnP6pO99pmh0TIzd0FpNjabv56ep8_CzlXt11Hu915Ubt4vess4Q0ZAhcZPSirav_JzpIB48dghiARxTe0_qNa3lzsqR9EL2ubvxct-YETDXtrXrQpZnyf8liDIu89PEOqWNDbHz1yZGQ7uJ0QiE7brbQ4ICyGkMi3lV0--8rh9IMjYOC7ldGJZoGBrC2Ad7HPDXnpKAU3y762vs9YB-_HvUROAnEmPd2-UTLG25LPsYLgKttqWsieBwhnhEB24WK9zxzVIMVe0QmPXbLpAyz3zkJ5NVVKK_XJ7SXCBhJ6MkGOYNbeOefRzsnepuLonOIfe0eyKfiaobs4y_yg_mjzsTHaWggUUKznR0DD5PtmBUW2U7HDbc32PgVQqGrbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f89d8f81.mp4?token=dv1rkUO7a24r8ZsdhSLP1MpM15giPJgShdi8mAqrebgM3-AyB5H6D6KgvOcODoEmkRftDaa8htf-Q9iN2e-g6BAEdHZlguWupgRcQ8K2FBtHF3bJfsciFdg5wSh5hwVQZq8qAlXC9j40-o8MDuUEMa_udbBKRUVRFcm0lo8OByQpNMEX9yCiCG6YQo3ZTRJFVtY3yhRGjLNho96NLCmm338Y91V8UFYA_vL54E_lkutkLduJdtLkaKzz4HpitH0aMj2KQOii4w15ngqoOJU5OEzM8vvb2BvN8uRd6b8tvHWxWnP6pO99pmh0TIzd0FpNjabv56ep8_CzlXt11Hu915Ubt4vess4Q0ZAhcZPSirav_JzpIB48dghiARxTe0_qNa3lzsqR9EL2ubvxct-YETDXtrXrQpZnyf8liDIu89PEOqWNDbHz1yZGQ7uJ0QiE7brbQ4ICyGkMi3lV0--8rh9IMjYOC7ldGJZoGBrC2Ad7HPDXnpKAU3y762vs9YB-_HvUROAnEmPd2-UTLG25LPsYLgKttqWsieBwhnhEB24WK9zxzVIMVe0QmPXbLpAyz3zkJ5NVVKK_XJ7SXCBhJ6MkGOYNbeOefRzsnepuLonOIfe0eyKfiaobs4y_yg_mjzsTHaWggUUKznR0DD5PtmBUW2U7HDbc32PgVQqGrbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الحرس الثوري:
مشاهد من الهجمات الصاروخية المكثفة التي استهدفت أهدافًا أمريكية في الأردن، في الموجة الثالثة من عملية "معاقبة المعتدين".</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89148" target="_blank">📅 02:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89147">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
الحرس الثوري:
شن مقاتلو القوة الجوية التابعة للحرس الثوري الإيراني هجومًا مكثفًا بالصواريخ الباليستية على مواقع طائرات الاستطلاع المسيّرة من طرازي RQ-4 و MQ-9 في القاعدة الجوية الأمريكية في الأردن المعروفة باسم الأمير حسن، مما أدى إلى تدمير عدد من الطائرات المسيّرة، ومقتل عدد من الطيارين والفنيين.
🔹️
بالإضافة إلى ذلك، تم إشعال النيران في العديد من البنى التحتية الفنية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89147" target="_blank">📅 02:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89146">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات في البحرين</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89146" target="_blank">📅 02:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89145">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7744c7efd3.mp4?token=Mga6tG4hMTe__UeT1orbV3J_gf-OFkXsKUP1MgzhtFfnGjYApwNiWDa9AMU7ZJL_Kmea8OK8U1K-fnB1_RB7KaXgW6sw3pODzimzP_Mx7JeHPovJKN7N6Intct1J38sL9oig8wEU1qBDa9NemhKf9YsvzWeZO2imUcF30wTDtnBPHXGRGxbZpXm--PVe5iHXiSFrF1TZS-vQiznhj9GQoaAAiVcyf_2RZ6Kbz7dz_26hD4FuFSOE1NZLPj218cKs7_SyThVgbSoC9HCoiRNpJLgjQaFWPj3qK4kPCzzfn-dBA9wrnEisj6wcEQ2H6rwWy8MNrTWPwh4resM8OE-vDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7744c7efd3.mp4?token=Mga6tG4hMTe__UeT1orbV3J_gf-OFkXsKUP1MgzhtFfnGjYApwNiWDa9AMU7ZJL_Kmea8OK8U1K-fnB1_RB7KaXgW6sw3pODzimzP_Mx7JeHPovJKN7N6Intct1J38sL9oig8wEU1qBDa9NemhKf9YsvzWeZO2imUcF30wTDtnBPHXGRGxbZpXm--PVe5iHXiSFrF1TZS-vQiznhj9GQoaAAiVcyf_2RZ6Kbz7dz_26hD4FuFSOE1NZLPj218cKs7_SyThVgbSoC9HCoiRNpJLgjQaFWPj3qK4kPCzzfn-dBA9wrnEisj6wcEQ2H6rwWy8MNrTWPwh4resM8OE-vDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات مسيرة انتحارية تحلق في سماء أربيل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/89145" target="_blank">📅 02:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89144">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
نائب القائد السياسي لحرس الثوري يوجه رسالة إلى الدول العربية:
من الأفضل لكم طرد الأمريكيين من بلدانكم واستعادة القواعد العسكرية.
وإلا، فقد أثبتت القوات المسلحة الإيرانية أنه في حال تعرض إيران لأي هجوم من أي نقطة في الكويت أو البحرين أو الأردن أو أي دولة أخرى، فإنها ستواجه ردود فعل قاطعة وحاسمة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89144" target="_blank">📅 02:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89143">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
الشركة العامة لإنتاج كهرباء المنطقة الجنوبية:
إيقاف الوحدة الثالثة مؤقتاً بسبب حريق اندلع بمحطة الناصرية البخارية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89143" target="_blank">📅 02:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89142">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
توقف العمليات الجوية في مطار البحرين الدولي.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89142" target="_blank">📅 02:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89141">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c296dec08f.mp4?token=CEkcu7nWDs30piOXYTybFTYxCmCg1-9jgIWAaw3StxDqbjy6zI0dFg3YbUPSfAUDweCMQ5QnydhUxRKopNGE7kRv7lH-_f35RA-B9N1ZE_tRiLpqhceh0uA99qKZRpI-UGJY9xFvf6gi38I-a086roakrUjAP1x5ekEUTutPRG3Bl6nQ_fUNYY2IDCQKFFCATtiGJmIyaqDuYhckqeRekfZwCco1ZYe07asPwTuv1-Tlt1hh5iqUKohWMIIxMRcTf_idtz9gYjOgzT9WWctZw7O88c-vVOCpdIuQ9iooa71_j4h7Wi7ICkPHKr_ve1fbq0nhGtkhW_cmZ2JGQkKE0hN41VKs2YPVNZfK-MWmC4u1H2jsV9Ve7YF3_H14PPKmfgnN84AvQ9iMc1vvouHZkIjZyjT6xy-fSJw-iiDD3Uu9l_2DeCoqlz7C-TrkOYu7DUTWmUW8Oi9unl3FUFeDbAwOAeSZ2I1qMbEO_NxY-sE3EtGwiczSYnuTEW1XTk19jLuJi28onOmfYnCdZpgtjZznK4glFOCTEjTcY-FpJsLtXTiGVDLHZzdziEbaMWyyGgfOm3wmQfBMaoB6hwtcZ2NjNjGAwbL_dTkwpnpqHnXKAbrI8_MGdQtu60NyaSA7xGr3PQYRPO0SXGHa78S02SoqKNB0kIze3rnGv5YqVt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c296dec08f.mp4?token=CEkcu7nWDs30piOXYTybFTYxCmCg1-9jgIWAaw3StxDqbjy6zI0dFg3YbUPSfAUDweCMQ5QnydhUxRKopNGE7kRv7lH-_f35RA-B9N1ZE_tRiLpqhceh0uA99qKZRpI-UGJY9xFvf6gi38I-a086roakrUjAP1x5ekEUTutPRG3Bl6nQ_fUNYY2IDCQKFFCATtiGJmIyaqDuYhckqeRekfZwCco1ZYe07asPwTuv1-Tlt1hh5iqUKohWMIIxMRcTf_idtz9gYjOgzT9WWctZw7O88c-vVOCpdIuQ9iooa71_j4h7Wi7ICkPHKr_ve1fbq0nhGtkhW_cmZ2JGQkKE0hN41VKs2YPVNZfK-MWmC4u1H2jsV9Ve7YF3_H14PPKmfgnN84AvQ9iMc1vvouHZkIjZyjT6xy-fSJw-iiDD3Uu9l_2DeCoqlz7C-TrkOYu7DUTWmUW8Oi9unl3FUFeDbAwOAeSZ2I1qMbEO_NxY-sE3EtGwiczSYnuTEW1XTk19jLuJi28onOmfYnCdZpgtjZznK4glFOCTEjTcY-FpJsLtXTiGVDLHZzdziEbaMWyyGgfOm3wmQfBMaoB6hwtcZ2NjNjGAwbL_dTkwpnpqHnXKAbrI8_MGdQtu60NyaSA7xGr3PQYRPO0SXGHa78S02SoqKNB0kIze3rnGv5YqVt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الأمريكي:
الولايات المتحدة الأمريكية أكملت قوات القيادة المركزية (CENTCOM) بنجاح موجة من الضربات ضد أهداف عسكرية إيرانية في 1 سبتمبر.
ضربت القوات الأمريكية أهداف الحرس الثوري الإسلامي بما في ذلك مواقع الدفاع الجوي وأنظمة الرادار والأصول والمرافق البحرية وقدرات زرع الألغام ومواقع الاتصالات.
تأتي الضربات بعد محاولات الهجمات الأخيرة التي شنها الحرس الثوري الإيراني ضد الشحن التجاري في مضيق هرمز وضد أفراد الخدمة الأمريكية.
يعمل أكثر من 50000 من أفراد الخدمة الأمريكية حاليا في جميع أنحاء الشرق الأوسط ولا يزالون يقظين ومميتين ومستعدين لمواصلة تنفيذ العمليات التي يديرها القائد العام.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/89141" target="_blank">📅 02:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89140">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991ec88d71.mp4?token=PFw94DmsYWcm7hEkwyX-3Qc9FY0h8rBJGkz6D-Zkn0tSb4hC48GUnwsCyK3be5DkeT9c1p39gr2qzmwPxrcXMhmFdS-RFCvrr-objyw9oPlWODaeIyat_wwArJPiPrI6NALzFcjuTnNTGAax1E2VrJTZwHDvta9JacSpixG-Y-EHMwO4NAl7uYx1JgVOHMf3xJVgwqlCiuy1yfgPncBwz3YQ9OzNsj7t_-1dv9jxfp1lbAnkKCW-P1fWyklW-mBuHzSCJKyNARnlKymP7lm79IAhggvZXjYlp_O7ikRHosrlOKMFqOSLzTY470ZUTmcGgLRjM-0yoiu4yKrYU4SlKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991ec88d71.mp4?token=PFw94DmsYWcm7hEkwyX-3Qc9FY0h8rBJGkz6D-Zkn0tSb4hC48GUnwsCyK3be5DkeT9c1p39gr2qzmwPxrcXMhmFdS-RFCvrr-objyw9oPlWODaeIyat_wwArJPiPrI6NALzFcjuTnNTGAax1E2VrJTZwHDvta9JacSpixG-Y-EHMwO4NAl7uYx1JgVOHMf3xJVgwqlCiuy1yfgPncBwz3YQ9OzNsj7t_-1dv9jxfp1lbAnkKCW-P1fWyklW-mBuHzSCJKyNARnlKymP7lm79IAhggvZXjYlp_O7ikRHosrlOKMFqOSLzTY470ZUTmcGgLRjM-0yoiu4yKrYU4SlKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتعال النيران في مقرات المعارضة الكردية الإرهابية في أربيل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89140" target="_blank">📅 02:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89139">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927bd8f122.mp4?token=JwJs5pSBrUIhewXo2rMVC-G8R4LI3La_rcVdm3Pr34g6JRE_4Eqy8X3ynRroTCc1FgFa2MlTOwHlmBVDBEzjLtMcIQBf8W4wUHI9dgaDYVaYiGmPCikywLqipxsl2SKR9hU0eOiiIn2j76XJyuWHp_uWdV2cAfbT3cIjpZPjlbaUf49gAg0GkBkaWoqr5gZXO_sXfALaQ4tMkX864JacHUk2u-gSzxD3ITbv8KfXYtysxEOYPDt-YHSM23OsPphTYq9ApzgrKeP4mU6bfMaS73yirkMy9easByBqtjgmWIiDHYHyAtSetOqZ_WC4_WDuinCZ7uPdZKrEE2rTmV_awA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927bd8f122.mp4?token=JwJs5pSBrUIhewXo2rMVC-G8R4LI3La_rcVdm3Pr34g6JRE_4Eqy8X3ynRroTCc1FgFa2MlTOwHlmBVDBEzjLtMcIQBf8W4wUHI9dgaDYVaYiGmPCikywLqipxsl2SKR9hU0eOiiIn2j76XJyuWHp_uWdV2cAfbT3cIjpZPjlbaUf49gAg0GkBkaWoqr5gZXO_sXfALaQ4tMkX864JacHUk2u-gSzxD3ITbv8KfXYtysxEOYPDt-YHSM23OsPphTYq9ApzgrKeP4mU6bfMaS73yirkMy9easByBqtjgmWIiDHYHyAtSetOqZ_WC4_WDuinCZ7uPdZKrEE2rTmV_awA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات واندلاع نيران في مقرات المعارضة الكردية في أربيل</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/89139" target="_blank">📅 02:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89138">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7ad2814c.mp4?token=uxXwoqBqC_c59Qbrq-Ddz_wffLZXTxjflskYfwhsJYRzsP97ebbAYzcE0L_i5I0incJxDtJR0Ms6fpLrm7y9IqPmKACgTU-BtlZ_G9IexdtyFsUw1ZrqqZqQ0P6sX9T_euy4yDcnvA2fV3xtmweXojsQWZMjKUlfo2q9UhhKPYw1EnEeqP_xE1LoDmouCm8NEA0fJzgy7qwzDyX0xhA1EkKxFClPLiuDujtf4gifbfFraoUNX-IHO3yjTTq3inbq9_81Ec5aEfa5LdUctXJI7SKVennP4O1YBuYx69UZgs4_o-4pX3Q7KiXm3zi5GRHrcfXC8-h2aci5tcwdwhIe6DE26iTCeZeKdmETj7CUJFrKfzwwPSpesqLHg2yJlDvuUPYx0h0pfwcOuFNeQb_ORKgD9rhJzB4JZlsbL78LfgLZIuM2ph0C-inipiEsUS4Ojfzt0mSVhlhZ3eKZp15o58TQNQxzJqA8XsfPDqE2Ne8divRN7lO0pttxB73b66-hnVu_rolIxAx-9iuCgRkTJJ34y3V9xRJmgVhrnLXGI2JoToDVGl5bdzI5CoA6trLIg2WD4CdGwfB4VrVELr04EzuUFuIW9lYRK44t1D6HnaTcRWMqCshDJvercQ9t1Cp8dGE666iaZesl7lbwi-EfyYmle0VcjK-aPdhVZZN7xeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7ad2814c.mp4?token=uxXwoqBqC_c59Qbrq-Ddz_wffLZXTxjflskYfwhsJYRzsP97ebbAYzcE0L_i5I0incJxDtJR0Ms6fpLrm7y9IqPmKACgTU-BtlZ_G9IexdtyFsUw1ZrqqZqQ0P6sX9T_euy4yDcnvA2fV3xtmweXojsQWZMjKUlfo2q9UhhKPYw1EnEeqP_xE1LoDmouCm8NEA0fJzgy7qwzDyX0xhA1EkKxFClPLiuDujtf4gifbfFraoUNX-IHO3yjTTq3inbq9_81Ec5aEfa5LdUctXJI7SKVennP4O1YBuYx69UZgs4_o-4pX3Q7KiXm3zi5GRHrcfXC8-h2aci5tcwdwhIe6DE26iTCeZeKdmETj7CUJFrKfzwwPSpesqLHg2yJlDvuUPYx0h0pfwcOuFNeQb_ORKgD9rhJzB4JZlsbL78LfgLZIuM2ph0C-inipiEsUS4Ojfzt0mSVhlhZ3eKZp15o58TQNQxzJqA8XsfPDqE2Ne8divRN7lO0pttxB73b66-hnVu_rolIxAx-9iuCgRkTJJ34y3V9xRJmgVhrnLXGI2JoToDVGl5bdzI5CoA6trLIg2WD4CdGwfB4VrVELr04EzuUFuIW9lYRK44t1D6HnaTcRWMqCshDJvercQ9t1Cp8dGE666iaZesl7lbwi-EfyYmle0VcjK-aPdhVZZN7xeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تتمكن من إستهداف جسم معادي في سماء جنوب البلاد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89138" target="_blank">📅 01:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89137">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">توقف مطار الكويت عن العمل</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/89137" target="_blank">📅 01:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89136">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/89136" target="_blank">📅 01:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89135">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/89135" target="_blank">📅 01:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89134">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd23a61c8.mp4?token=hkjBeFZWqKhyul-8dj34xjj6mOPFKtgpZrUkBRIhO96CxubEL25LR9-6s8-jA3gT6JN11m83XyMXIatzxlAhNuInKKtiOEuwWKDJygai9vGdJwoEmG5pXtlt6lCcoi-x7RzRj1qAPRkklX3Euyp6Ss5NcLdcQ0PeTzgXmN9XpnJ0oQmISX3-iyRnlQHRi9EhGRD6ObjooNHanVvWtF1C-sPqTy7PxslF-Ia9dH7_PvWWFTwVfcW_1mlveu-iJ53cbv-cpc4303GR_nRlvC2hpYw06xSiuIdFpoSEpHYEiIyTk4FYXZFXtnAJPFG_8NzSiqkdyXgA0aes1l1jxh1P4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd23a61c8.mp4?token=hkjBeFZWqKhyul-8dj34xjj6mOPFKtgpZrUkBRIhO96CxubEL25LR9-6s8-jA3gT6JN11m83XyMXIatzxlAhNuInKKtiOEuwWKDJygai9vGdJwoEmG5pXtlt6lCcoi-x7RzRj1qAPRkklX3Euyp6Ss5NcLdcQ0PeTzgXmN9XpnJ0oQmISX3-iyRnlQHRi9EhGRD6ObjooNHanVvWtF1C-sPqTy7PxslF-Ia9dH7_PvWWFTwVfcW_1mlveu-iJ53cbv-cpc4303GR_nRlvC2hpYw06xSiuIdFpoSEpHYEiIyTk4FYXZFXtnAJPFG_8NzSiqkdyXgA0aes1l1jxh1P4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقة جديدة تنطلق</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89134" target="_blank">📅 01:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89133">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c40f45bc4.mp4?token=s2TWmkZGnElIm0r24Auwgl__Q7sBmULiyAA_FIZ8OnP5z9MMyPvOZJCNGiY4f8fAcQFO5VR3IlGMTtmu9rnfYlFiE6lsKNvUhN64D4DgYK-LjWIo-9XYCdkTK12UVmTQWr0KzKChlNrW8Xc9Vs9u5LIluV9bd2SGynPDtlprDDtQgpc9aEqb7viquu0j4HedlaKTaZI4FssdWZEA3x3DxZz7ioagBefalQ45fG_gYHMg0dpNXKtg9egInxKEttMt4jUgkIxxHRi_meRMalf_Xo_Ue4_6XfdJIS52qdBI7Dp3uh4lBh8FBNlQiaa3jpejjuOfnH-08q77GgBYcSudHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c40f45bc4.mp4?token=s2TWmkZGnElIm0r24Auwgl__Q7sBmULiyAA_FIZ8OnP5z9MMyPvOZJCNGiY4f8fAcQFO5VR3IlGMTtmu9rnfYlFiE6lsKNvUhN64D4DgYK-LjWIo-9XYCdkTK12UVmTQWr0KzKChlNrW8Xc9Vs9u5LIluV9bd2SGynPDtlprDDtQgpc9aEqb7viquu0j4HedlaKTaZI4FssdWZEA3x3DxZz7ioagBefalQ45fG_gYHMg0dpNXKtg9egInxKEttMt4jUgkIxxHRi_meRMalf_Xo_Ue4_6XfdJIS52qdBI7Dp3uh4lBh8FBNlQiaa3jpejjuOfnH-08q77GgBYcSudHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في أربيل</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89133" target="_blank">📅 01:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89132">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجارات في أربيل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89132" target="_blank">📅 01:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89131">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4088d8cab.mp4?token=iHKL6g48mhUtGbLsz80eknIfRfGweUCc-2eQ5aRO_R0nsx4xM_fcXcg5ih4ScooMvrMr8mfyYKO9kr6USJY3jxyELU6sw5Te7cAJLMNJO2qt8EogZDyxNYH7hdCohvp-eUoN4h39PlFQVsnyHbdG6ZiuFbS9aG5IoLts-PMOWhrs97m7VySb2iNvWi0X0HjyQJbmuhERESd1lOAMncsuwp9f1Kb2FdBMWxjFCnWQkHWvmTS3hHKwOiE3d_SYYc38TopFcngU0u4atvuc6g9fhNMxUbY6whdz0EgduOe6ngrKD4VWlBEKe_vMNZvMV8Ddhx-rKGpW4d_Q8AOiuDoYMAderU01yCgffMv4wyO1hIt0XD9nY2cwhxglEN7RE20ahzUC2c0p-nm6LQCJmYXSky8CjH4gc2IJ1xPxncdLrNP8Cc-zmS9rwrFUKoorwY5wdczxxfvm-cKdJgfjVYGsGZGlKH4xaHtHim_m7JD4NIGUQmbkl1w0FMT7-881BjyrGRFL-0Lrv7FKRJGmtzcW_c8JVWPZIKE_cURso5hqcTtnvIBBE884d5DiJ58BdWqRqihQw-FvGcicaftqwuEn-LgsrBp3RJwKD_WrhmsjRgY1pxatbp05C9-9eEfnjpnn6y2T8A275rYr4I3sNTOAJSK-B07S23Oxv0TZNQ7iu3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4088d8cab.mp4?token=iHKL6g48mhUtGbLsz80eknIfRfGweUCc-2eQ5aRO_R0nsx4xM_fcXcg5ih4ScooMvrMr8mfyYKO9kr6USJY3jxyELU6sw5Te7cAJLMNJO2qt8EogZDyxNYH7hdCohvp-eUoN4h39PlFQVsnyHbdG6ZiuFbS9aG5IoLts-PMOWhrs97m7VySb2iNvWi0X0HjyQJbmuhERESd1lOAMncsuwp9f1Kb2FdBMWxjFCnWQkHWvmTS3hHKwOiE3d_SYYc38TopFcngU0u4atvuc6g9fhNMxUbY6whdz0EgduOe6ngrKD4VWlBEKe_vMNZvMV8Ddhx-rKGpW4d_Q8AOiuDoYMAderU01yCgffMv4wyO1hIt0XD9nY2cwhxglEN7RE20ahzUC2c0p-nm6LQCJmYXSky8CjH4gc2IJ1xPxncdLrNP8Cc-zmS9rwrFUKoorwY5wdczxxfvm-cKdJgfjVYGsGZGlKH4xaHtHim_m7JD4NIGUQmbkl1w0FMT7-881BjyrGRFL-0Lrv7FKRJGmtzcW_c8JVWPZIKE_cURso5hqcTtnvIBBE884d5DiJ58BdWqRqihQw-FvGcicaftqwuEn-LgsrBp3RJwKD_WrhmsjRgY1pxatbp05C9-9eEfnjpnn6y2T8A275rYr4I3sNTOAJSK-B07S23Oxv0TZNQ7iu3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في الكويت باستمرار</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89131" target="_blank">📅 01:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89130">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الكويت تحت مرمى الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/89130" target="_blank">📅 01:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89129">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الكويت تحت مرمى الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/89129" target="_blank">📅 01:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89128">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رشقة جديدة تنطلق</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89128" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89127" target="_blank">📅 01:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89126">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89126" target="_blank">📅 01:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89125">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الله أكبر  مسيرات انتحارية تصيب اهدافها بشكل مباشر في الكويت والنيران تشتعل فيها</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/89125" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89124">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تفعيل الدفاعات الجوية في سماء الكويت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89124" target="_blank">📅 01:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89123">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارات جديدة في الكويت</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89123" target="_blank">📅 01:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89122">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجارات جديدة في الكويت</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89122" target="_blank">📅 01:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89121">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">إطلاق صواريخ من إيران نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89121" target="_blank">📅 01:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89120">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">إنفجارات في الكويت</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/89120" target="_blank">📅 01:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89119">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">إنفجارات في الكويت</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89119" target="_blank">📅 01:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89118">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔻
بلومبرغ:
أصدرت حكومة الكويت مرسوماً يسمح لها بالاقتراض من صندوق ثروتها السيادية، لدعم المالية العامة للدولة، في الوقت الذي تتعامل فيه اقتصادات الخليج مع آثار الحرب الأمريكية الإيرانية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89118" target="_blank">📅 01:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89114">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6Pp0Icp610kL8n6mlsq0nqAiFBS7BwuzWiOn0xPZkUzmlkqxwZPUBTal0sYyGUlbXIFyIT5qmAzyhUz61_lDBUPvIUxqu4E1r2h2Uex7NgxEKE21W_UrR-KCxKUD1DDBNrOLAobYPoiG_VjlkHves-z-LhOwogz2nLL_MXzArH9ntOe0zgZRWhzArABzH2Gmy-0prPXW2pVrOsS5LFeZAOWtrWHOuht0AJLv8ysknKqS_JpFLdbq7cHuohr4EPmIyxP7iVRc4qGXcFYoeTpzFDQch3IZkEbP2BMHIt9nsnSKT6JSfnun0yW2GSEukNoF-otHpWNwbKGauGMH3L9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kv-hLo6NhgUExQS_kNLPomyHiyklOrISCKW-x47a3_88jSvEGLm9tCp-9uY6zGkfHlZBF8G-VYIDd8D2E4tvqzogDD483tLdTvYFEGxvhHDXGLp7lMptAgYGMKCyIgVGB5rFf1ZQXlFfJq3u5hXhgDP8RI-X-5fzwjrALvCg9DnJrvQv_1x5qUJh8F9aB4WblApLDyneh4JEWv9EjDm2JOkQE44anVSTnFo75-jEjO77Q3a5677gJU12bfjxpuzWvAChUMysj-PvFC4S1O8R5kt6P8l4ZWE6kF8TviFrIhIS9NKa0-MuMavwTUMGbkipBB4CIiGAfL_WyCXb71zmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLbw4RMd9xEsncpaBCwj3EXRu6iydoHzGTEAWJMBui447yrYCpN1gyJQxdMXNZT1ooch_2ZLUvq86-m8n9XScy0GRs6lWnFBVzTQ39EYS-pR7PfbNQlq9r7xwuY2i27vu0Vb18h2e8RWalI1UTrYDigVTakdKl8Rdu2sJQmuNo32QmePPDdrjNNXi9B8gPqVCc7Kgcf94sd4CulzlDGm5HK-U_2Bhodtg5RjV5BteL5GXpumArc-ieUp1QjSyiXghx1qZrjuPhYy0eUY8-iGSP5LMUGhevrFv4R3dBafVgy34oyQtoM3YnTTRbjoeO7oA7XL5EGPdpTQLYT2RZ7NXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EIGPgDmMfzCl4cS8uU1PsEocOtxORYHc5yyS6M7WJ27dB15ca-jw-JGqrr3bLbEmj1l6D08inuyDeqtvAJnwmpjczcxjU0UPPXBABcSHTzqwPgnFM_b9w098xClr61Ill-5OmNvlYZXae7YdKYlL0JsTyj-2ph58njWXzw6SDWiM3rLuiqQQqIAUM3SIaGO1nbXcYWJLUIkkbPKTEJrvoaUr3nk6wMLTodHjxXIlhcADejBt9jPbcwwG27Sh-MAHIhG4zP1Wvrps-5nzIQzRNdZwKj5cOcWfAdv7jchZjclwf355CwtqRJG0IYWbyrlc94CalhM-cg9tdlTBrzRXgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توثيق للحظة العدوان الأمريكي على حفل زفاف في سيريك جنوبي إيران؛ حصيلة العدوان حتى الان 5 شهداء وأكثر من 70 جريح.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/89114" target="_blank">📅 01:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89113">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080cbe3f92.mp4?token=COjiBrM0i3icB9N8XZNLjpnsdleBuQ4y8SLjf5qapPb9agxVeGfLYQh6Y1jrXPk8r6gOiLKYR2kU7uoC_0rJ_T421S71rR2xoFFFDFcUj90wf8P-P7WUVmh4VsA-YLXrBxhxgNpO9HO7RpIJ_i_3qZ7b4j--IvCAYn5Ql7SxfCB8nW8qJZ9Qg8t21rzTf-QOfEFEA2J36JcwLyBaXW8MROz5AcA3VPxiiu5w07ePuYnyDxYj_1iBl9VKJnIGkToI7MtMy1ieWnFAYFVbWvp4XQfPRugHn2BKN6OHUFMrVuoR59axeg7woKvvHYkmsCjbWBsjV_VOwDiFaLAy_DVz9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080cbe3f92.mp4?token=COjiBrM0i3icB9N8XZNLjpnsdleBuQ4y8SLjf5qapPb9agxVeGfLYQh6Y1jrXPk8r6gOiLKYR2kU7uoC_0rJ_T421S71rR2xoFFFDFcUj90wf8P-P7WUVmh4VsA-YLXrBxhxgNpO9HO7RpIJ_i_3qZ7b4j--IvCAYn5Ql7SxfCB8nW8qJZ9Qg8t21rzTf-QOfEFEA2J36JcwLyBaXW8MROz5AcA3VPxiiu5w07ePuYnyDxYj_1iBl9VKJnIGkToI7MtMy1ieWnFAYFVbWvp4XQfPRugHn2BKN6OHUFMrVuoR59axeg7woKvvHYkmsCjbWBsjV_VOwDiFaLAy_DVz9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:  في المرحلة التاسعة والعشرين من عملية "البرق"، وردًا على تجاوز العدو للمناطق الجنوبية في البلاد، استهدفت القوات المسلحة الإيرانية، قبل ساعات، منشآت الرادار ومراكز تجمع القوات الإرهابية الأمريكية في قاعدة الشيخ عيسى في البحرين بهجمات مكثفة…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/89113" target="_blank">📅 01:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89112">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
في المرحلة التاسعة والعشرين من عملية "البرق"، وردًا على تجاوز العدو للمناطق الجنوبية في البلاد، استهدفت القوات المسلحة الإيرانية، قبل ساعات، منشآت الرادار ومراكز تجمع القوات الإرهابية الأمريكية في قاعدة الشيخ عيسى في البحرين بهجمات مكثفة باستخدام طائرات مسيرة.
تعتبر قاعدة الشيخ عيسى في البحرين واحدة من أهم وأكثر القواعد الأمريكية حساسية في منطقة الخليج الفارسي، وهي مركز مهم لإصلاح وصيانة المروحيات وقطع غيار الطائرات المسيرة، وتستضيف طائرات استطلاع.
أكد قسم العلاقات العامة للجيش أن مقاتلي الجيش الإيراني قد ردوا بضراوة وبشكل واسع على أفعال العدو، وسينتقمون بشدة من المعتدين، انتقامًا يترك آثارًا عميقة.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/89112" target="_blank">📅 00:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89111">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
الحرس الثوري:
أي نقطة تُستخدم لمهاجمة إيران ستكون هدفًا.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/89111" target="_blank">📅 00:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89110">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترفيهي
🔻
الجيش الأردني:
منظومات الدفاع الجوي تعاملت مع 13 صاروخا باليستيا دخلت المجال الجوي للمملكة.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89110" target="_blank">📅 00:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89109">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=IIjlqQXI1pk0Q7fnm7tvpa6wIOOQZ-VFRyJfomAgWf5-2mFXrHs35iXKpgBgvutwTi-XxqEQLhN2qAn_x-x6M0oybL5HezvErWomfxUfEwzAWb7t3Od7YmK5ZfMz09nUCaP5VmOyEXG0FIQudKVzACnzr2iBtB3oRFLljVahnIIodhFYDYzitoyEKywihBq84tvX2neT94g9ecQc9_AAEN5YpUtPP4mQ527soICaLAFLuUb0t_QLJEt-HSoxI7asyrm5EDbag7J-pFSGwQtmeV91aT1-7EvJNwC90F0oUemuxwZz_74dmJSdIvzGlrqtmQn-1RKL3O1t0-Pj59YYFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=IIjlqQXI1pk0Q7fnm7tvpa6wIOOQZ-VFRyJfomAgWf5-2mFXrHs35iXKpgBgvutwTi-XxqEQLhN2qAn_x-x6M0oybL5HezvErWomfxUfEwzAWb7t3Od7YmK5ZfMz09nUCaP5VmOyEXG0FIQudKVzACnzr2iBtB3oRFLljVahnIIodhFYDYzitoyEKywihBq84tvX2neT94g9ecQc9_AAEN5YpUtPP4mQ527soICaLAFLuUb0t_QLJEt-HSoxI7asyrm5EDbag7J-pFSGwQtmeV91aT1-7EvJNwC90F0oUemuxwZz_74dmJSdIvzGlrqtmQn-1RKL3O1t0-Pj59YYFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إرتفاع حصيلة الشهداء إلى 5 بينهم أطفال ونساء، جراء العدوان الأمريكي على مدينة سيريك جنوبي إيران</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/89109" target="_blank">📅 00:41 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
