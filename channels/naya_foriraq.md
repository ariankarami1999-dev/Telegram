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
<img src="https://cdn4.telesco.pe/file/l2AdWnGecRyk1kQEXr3T-IbEAUymEXTHibljilEhrierhCAJUMahXn95ncjAu5ivxH1QkAf4L32MXy7ZwArktcX6cX5z8Ch1GkOw4JwyS10Uq9-MHUZ3dvvKKBMkgZiOGbyrqMbZeB3vK8lckQ-YOQ_kV4TRSKoRuLAjadGYS9jIG5-Hh2dEApaGrC6cQRhoxLt-mRoSGu9JnABwtEFGBWWGXcoPe1bgLEMWG88NAhV0g-p6nCMlf76ZD8i5AVMRVv-xj_5ng6eU5Z1CJbjumdwq41L0Vqx8mTuniR0ublJR_bkYJiO8_2SM-LaevhjogUgI71pUWnGd9xwrHkaLfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 253K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 17:27:22</div>
<hr>

<div class="tg-post" id="msg-75824">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
مدير مركز العمليات المعلوماتية المشتركة العراقية:
رصد أكثر من 3200 صفحة مرتبطة بـ (إسرائيل) ودول مجاورة تعمل على إثارة النعرات الطائفية، حيث وصل المركز إلى مراحل متقدمة في مواجهة هذه الحملات.</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/naya_foriraq/75824" target="_blank">📅 17:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75823">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7be1616c.mp4?token=W8i4V29-MCoRg6wpdjG0Zth4CP-Y2WjoPtoeOT0WzePGqkeLMjae8QpkD8U7wp-V_HOVW8V63JsrzJG1lqn5ic7C4TIlGVT2v6-SpFsfdaGuOkWLq7rnKhtQq9Cdc1uHW1sqA3I5Ecob3CNeL1UVGTJQkaQPVSYN-i9fVurp1gQa7vf2nUuspGIcYKlMRg50gK07n_KVSoU1f6ijvoZu1VagHUL3UMpWJwTvPt2iW5JIzcQf8QNtn5LNl6hsw5s1H9PT4EpKJ72cRSidM-vNA91uc_KELnAWTbaCiYM37XrwHYEdz1gU28Ai_t9-lvUzguP2514AhQ-Ga4Ixn-Rumg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7be1616c.mp4?token=W8i4V29-MCoRg6wpdjG0Zth4CP-Y2WjoPtoeOT0WzePGqkeLMjae8QpkD8U7wp-V_HOVW8V63JsrzJG1lqn5ic7C4TIlGVT2v6-SpFsfdaGuOkWLq7rnKhtQq9Cdc1uHW1sqA3I5Ecob3CNeL1UVGTJQkaQPVSYN-i9fVurp1gQa7vf2nUuspGIcYKlMRg50gK07n_KVSoU1f6ijvoZu1VagHUL3UMpWJwTvPt2iW5JIzcQf8QNtn5LNl6hsw5s1H9PT4EpKJ72cRSidM-vNA91uc_KELnAWTbaCiYM37XrwHYEdz1gU28Ai_t9-lvUzguP2514AhQ-Ga4Ixn-Rumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/naya_foriraq/75823" target="_blank">📅 16:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75822">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/naya_foriraq/75822" target="_blank">📅 16:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75821">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🤩
استطلاع رأي لفوكس نيوز:
ارتفاع نسبة المعارضين من الأمريكيين للعمل العسكري ضد ايران إلى 60%</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/naya_foriraq/75821" target="_blank">📅 16:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75820">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📰
‏
مسؤول أميركي لفوكس نيوز:
إيران مصممة على إبقاء اليورانيوم المخصب داخل حدودها.</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/naya_foriraq/75820" target="_blank">📅 16:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75815">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ib0jMy9t7wt6lD2k8L3fWoR5oKM4Awx9Wn_wDY719N_pZ7OeEFRAVe8tu2MLs6cHeB293SKuem5req7P_UEgE9klR_pNUZ9xbpiVFhaaLbQWflc_yVnkE1Sj8ZsHJsGulj56KfnW95qttVAvPjIWEG3bMADhhLK0W1mL_aZ3CnJ5no7G8gPGksx9KBAlcMtycqcrI2goTheXq7EWLrTXEh2MVEv_pxIA1oYTX6SmIdBLdnRBJ_hDnCxVJFqGTGrO99paYvD2npAdbtcW0Ju2v7oUXEuatNPoX-7fmRuG6Xm5CCMUxoxRUbYwmW4gV7E8Lhhpx3R_HQdz8_aStYIcBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MzyDw7VodRlBjMoOCFWhjUKnaFQ_uiy2ah5TyPb0dJVAPjRs2tWaZiZRV3u_gRVblcv90vgYEK63XWFcLOkAOk6AQYl09HkEUGQrwdq02GBg_8hERc8JjpwTfoXiWjbUIgHAFQtLORNDZSaI4nrAr33hJPagC95J-6j5I9NE6uWSMu18qZt52mHBxPGuDeJQ5WOSj_-Ydsg9ZXuCGoFLghYYVrTpya2Qe5vbAywvWYV6KSoZWijOxcH7FuxyX3l1hsi8TKPxJa6BsFngcitml9vQQk9s9dIPX6iiiP-2eQNhtx9V0YwdwtvifjBWxh4vV1apxbqNx-tbnI4pHE8ZzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gKjVYk_6GroD1JOBTDrm0wyiRymSOLX-he22OzxrQ6eEsXlq_gTO3mPe8rq31LHrYgyIibMKy6EJk66Cge9XcL33IS3RZsjZk1yYfiAcCpMx75o2EO7viqUCTvkRzZbXEqlnpaWIP05YuQg7y6x0j0uU_pM7JyW6c5SLUNYQPpVim5M5V6EvocaJgbaa3eXde3lwMo4h8T3tYOpBZ6ZHzjaW_TsW_Attqxx7OCXDNWPqNUK1iCd2PFTdnFSVZRAlN58D41geKeXtc_B_ATcy_Mv9BImNWnkCZPaTC-7eXj0CSG4v1jXeW3SStEi3GTweuWvcSGbhBN4OEpAmPkAHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1d5Rc5L7lZd6O6MxUWcBKGLJ7-QdAGH5Yu7NvxRukh2OSQ7tzyW6-6tkc8vZulqQ1On36K2iv0Ytyp2sPQzNL0w20ZyFpyYTbeX7e5BuHLJBybuG44-iAn85F9G99l0BRjHB3iFoxNiTzclxhks3RMcs0LmEwm8pbRiNeesyuH8zktDdeuotTl6wyO-Gtfvavr6T-MARFrE3eKLWW-hw4DAeZJ_pjYkbcHaOzlWDGAWbEFX1L9EiqY3Nd-oRQN8G7szeorHogMtK1GLwxQN03gj2j22oEh4YChfO-KhAfnBXMkP_dl_zOfKoMWQRdU9xZ_3idWxsPtQ80dNZrXn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcU6bQ4Ht_d_Qz2NexL0vTL_eSo-m904V4x4HqvjxUM2SwAwIsv09SUjhoRqLJ9ha-Li22tcoMUOcUg2ol0uEmf6ln65o07pGxc6wDDB89v4Ui2ARzaw4fopQMU23_K52cEMbvef_WRS0S8NUEOjucexTTMRRMX32dsMcm6PI5mp9sBSBD0Cc9xZqLdSUEMBia-7_f2wjDWlCfOfv1rM9AF2lcCtDWapANEzt4PiTV_o7MF0Dd_G_lM8aa2JZmuRsf-He1CkSkwXxd2FU374CEmBf6HCl1l6Uxtq_YIhyxrUn931AbsOeJuBnnEuH8hX1Ym4aZgjCtpFM0OjIA_1wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">يصادف 21 أيار اليوم العالمي للشاي</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/naya_foriraq/75815" target="_blank">📅 15:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75814">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اختطاف زوجة وشقيق (كاروخ سيد رزكار) زعيم الحزب الوطني الكردستاني من حي رابرين في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/naya_foriraq/75814" target="_blank">📅 15:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75813">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
🏴‍☠️
القناة 13 الإسرائيلية:
نتن ياهو يدفع باتجاه استئناف الهجمات على إيران، بينما طالب ترامب بمنح مزيد من الوقت.</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/naya_foriraq/75813" target="_blank">📅 15:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75812">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇳
‏الهند تؤجل قمة مع الاتحاد الأفريقي بسبب تفشي فيروس إيبولا</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/naya_foriraq/75812" target="_blank">📅 15:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75811">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">😞
‏الطاقة الدولية: أسواق النفط يمكن أن تصل إلى منطقة الخطر في يوليو وأغسطس، صعوبات ستواجه المزارعين لتزامن الحصاد مع ذروة طلب الوقود.</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/naya_foriraq/75811" target="_blank">📅 15:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75810">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KswtDicsSD6g1kRFMIqRaQl1bKt5lpIe4TP_zj5XKoaOVdfWj5tulUdpo3va6Yf_zwOamhHVc8lCawYk79j8kPXTVl9FWQAWwohrD6Nh4lhjG-vvnDUMNalTNI6Grbx-qJQDME-K-NMWxnW0EdAnT1yYyAwIn934QovC3u501zw9QR6PdRzxGsJgNhI9g0JAmtOdSjbLEP0GLSxUxWOwXmuIWNdXxwpD_pM6bYIEJpngpBZhE9H7_8ytj1lZtkxdWoM13fdaySSdLtrPT9mNLqsAQKeSBOKbOSP79GWSOZSX16RqyMPHVW2LRrd4adec3-Jcm_HC_UTWBpWKxO7Csg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
إيطاليا تطالب بعقوبات أوروبية على
الوزير الإسرائيلي
بن غفير بسبب المعاملة المسيئة لناشطي أسطول غزة</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/naya_foriraq/75810" target="_blank">📅 15:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75809">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">😞
‏
الطاقة الدولية:
أسواق النفط يمكن أن تصل إلى منطقة الخطر في يوليو وأغسطس، صعوبات ستواجه المزارعين لتزامن الحصاد مع ذروة طلب الوقود.</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/75809" target="_blank">📅 14:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75808">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hijuERptcGIX9kbFmuSoIiijtOLKnWruQQcyBXxmVJIGSyqRu4Mkvm41bCi0DqyLbxrOmkoKIeLEL7IDH0GnJRN9pZjcM-ZoEtVdLk-VdtNwxnTBkJ-3nFkzCAPC-oAsYY1M9YtZEy1o0w9l2p_EJwMtQrmOaQdhxkvhSXo4CkVr1lRP5NoDJK-3I7TzufGjAaqpOW4PGuEKN9ppeIo_v7c0oVuYPsjZOD-BGVjb9-BqyqYSf5VE2GEalbN5GSxQCjwHmQD0TvNMwdjH838wPlng3YXBNVOb4hrirbwbWytqpOit4RIWIB8I4xRlyC3nuLD3X-wuodQ7BFFk3uikYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الايرانية:
إن صور وزير النظام الإسرائيلي في ميناء أشدود شخصيا وهو يهين النشطاء الإنسانيين المكبلين من أسطول "المساعدة إلى غزة" (كثير منهم مواطنون أوروبيون) صادمة للغاية. إنها تستحضر أحلك أصداء التاريخ - لحظات يرى فيها نظام، محمي منذ فترة طويلة من المساءلة، نفسه استثنائيا ولا يمكن المساس به وفوق القانون.
في ثلاثينيات القرن العشرين، عزت أوروبا نفسها بالوهم بأنها يمكن أن تظل صامتة - ومحصنة - في مواجهة التدهور المنهجي للكرامة الإنسانية والقانون الدولي والمبادئ الأخلاقية الأساسية، دون أن تدفع ثمنا على الإطلاق. لقد قدم التاريخ درسا وحشيا؛ ولا يزال تطبيع الفوضى والفظائع يقتصر أبدا على هدفه الأصلي.
واليوم، يمتد الخطر الحقيقي إلى ما هو أبعد من السلوك المؤكد لمسؤول النظام الإسرائيلي. تكمن القضية الأعمق في الصمت المتواطئ، والقبول السلبي، والتقاعس المؤسسي عن العمل تجاه الاحتلال، والفصل العنصري والإبادة الجماعية التي منحت مثل هذه السياسات والسلوك مظهرا من مظاهر الحياة الطبيعية والاستمرارية والجرأة المتزايدة.
إذا استمر الغرب في توسيع الفجوة بين قيمه الأساسية المعلنة وسلوكه الفعلي، فسيتعين عليه مرة أخرى أن يتعلم درس التاريخ القاسي: الإفلات من العقاب الذي لا نهاية له لا يخفف من الفوضى - فهو يطبع الفظائع ويشجع مرتكبيها.</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/naya_foriraq/75808" target="_blank">📅 14:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75807">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f30a6f56ef.mp4?token=niKbMP_o2nC39S_L89zxptzfwRV1oTgmvuPNzAXOHyKF0Drr0o21o9YAZOaZ2ViZbLE7ndPGRuwXw1P36kfNr7GbmruC8Z8CovCO4RNk78pKa_XyRv0p-eScdbieNNbKxHuTXjMICdVcRKVNsAL0NVEM7Q6cgjQstFxzCJ5B4B5CC4NohEjTDNMUZATTGgI6yKO0BhTU1PWNdtO5aJ9OXRXljzfj83_t0N4ibMzD1uyQp0odUJu-AoGBWmdTtZThtq9wZMSokZZBoC88DY9e-KO4H-l7GJgnDIxbWP3rAJqUUMkW74Pty594NoOxNkmXvVdtX2eH-3eBRkQI8gznH6ze5XxtKmhvKRnf3bLtqb7CVLiSzLSkvXy7Ym2r3IOKA91gmrtnnbF718sgZ4aqqtwIiA5kVDUDMnv4PB0BxCRrHEIjPHhVdcbba4OWcmJF3abqMydM0OJiTkcTuxDHMsQWLAj3E9S2UOh_OkNtNYX-W_Lwag6L6SoHwqPWq_DcLIwfoYJLOaOMtL6g6y4s2R9D4cZJ9orzKIi_5NN4a8Jo72R_5BiRLefnKGiT01YlDRdSDWsKe5p5-Z2TxifqGdYjIE5fzfIOoSoc5A_1PMZb0GebPYTPS-2mYSmUw36rga1yCX-VaC6SrEHp7-ZlH2iRmeA1iZU5azUfZbi0Xqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f30a6f56ef.mp4?token=niKbMP_o2nC39S_L89zxptzfwRV1oTgmvuPNzAXOHyKF0Drr0o21o9YAZOaZ2ViZbLE7ndPGRuwXw1P36kfNr7GbmruC8Z8CovCO4RNk78pKa_XyRv0p-eScdbieNNbKxHuTXjMICdVcRKVNsAL0NVEM7Q6cgjQstFxzCJ5B4B5CC4NohEjTDNMUZATTGgI6yKO0BhTU1PWNdtO5aJ9OXRXljzfj83_t0N4ibMzD1uyQp0odUJu-AoGBWmdTtZThtq9wZMSokZZBoC88DY9e-KO4H-l7GJgnDIxbWP3rAJqUUMkW74Pty594NoOxNkmXvVdtX2eH-3eBRkQI8gznH6ze5XxtKmhvKRnf3bLtqb7CVLiSzLSkvXy7Ym2r3IOKA91gmrtnnbF718sgZ4aqqtwIiA5kVDUDMnv4PB0BxCRrHEIjPHhVdcbba4OWcmJF3abqMydM0OJiTkcTuxDHMsQWLAj3E9S2UOh_OkNtNYX-W_Lwag6L6SoHwqPWq_DcLIwfoYJLOaOMtL6g6y4s2R9D4cZJ9orzKIi_5NN4a8Jo72R_5BiRLefnKGiT01YlDRdSDWsKe5p5-Z2TxifqGdYjIE5fzfIOoSoc5A_1PMZb0GebPYTPS-2mYSmUw36rga1yCX-VaC6SrEHp7-ZlH2iRmeA1iZU5azUfZbi0Xqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام العدو:
الإمارات تشتري من إسرائيل مكبرات صوت سيتم شحنها لأبو ظبي لتستخدم في صفارات الإنذار.</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/naya_foriraq/75807" target="_blank">📅 14:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75806">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل سرب من الطائرات المسيرة</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/75806" target="_blank">📅 14:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75805">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 17-05-2026 آلية عسكرية تابعة لجيش العدو الإسرائيلي في اسكندرونة ببلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/75805" target="_blank">📅 14:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75804">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📰
وكالة ‏رويترز:
السيد مجتبى الخامنئي يرفض فكرة إخراج اليورانيوم المخصب من البلاد.</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/75804" target="_blank">📅 14:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75803">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل سرب من الطائرات المسيرة</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/75803" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75802">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الشرق الأوسط السعودية:
باتريوس كان بمهمة جمع معلومات من القادة السياسين العراقيين عن من يستهدفهم في العراق و كيف يتم تفكيك سلاح الفصائل .</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/75802" target="_blank">📅 13:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75801">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: من المتوقع اصدار تعليمات لسكك الحديد والنقل ومحطات الحافلات بالبلاد للاستعداد لحالات الطوارئ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/75801" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75800">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">إعلام إيراني: وصول قائد الجيش الباكستاني إلى طهران لتضييق الفجوات</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75800" target="_blank">📅 12:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75799">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
عمليات بغداد: تفجير مسيطر عليه من قبل الجهات الأمنية المختصة لمخلفات حربية  اليوم الخميس الموافق ٢١ ايار ٢٠٢٦ وذلك ضمن مقتربات مطار بغداد الدولي غربي العاصمة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75799" target="_blank">📅 11:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75798">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">إعلام خليجي عن ‏مصدر ديبلوماسي: طهران تدرس النص الأميركي ولم تقدّم ردّها بعد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75798" target="_blank">📅 11:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75797">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوي انفجارات في قضاء سوران بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75797" target="_blank">📅 11:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75796">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb68cec79c.mp4?token=NblFIZbhbv96HMndU3N3_soVWocsX0Inf7ZETzjGuHLuFBXNKORdx9lIlyGQBGJ_uXPHpfdhZxxJ7GV_Xxg389llPitgF8Jq_mCnQnIhgk04ZS2xSqRK4cTq5lr489-BD-vXAQsasEpW12O5ZJ5nTjGEvJq6hul0847SjCjsi42B5A2cEBnD7JeK4mL6LOPQjN0AS8YCN33TJWDgOW3Y-mbBtobiOumNMWiw5-yuVKsFZmDl_dyqi7SwDBMXcKloJ9-Jc1Rud1cs37aO4luy_IYr4QG_K7JdJQGMT_zpjGI-iKJY--ch5n8_Vay0DJhyLp436YlDGfIY5KD5_Tunrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb68cec79c.mp4?token=NblFIZbhbv96HMndU3N3_soVWocsX0Inf7ZETzjGuHLuFBXNKORdx9lIlyGQBGJ_uXPHpfdhZxxJ7GV_Xxg389llPitgF8Jq_mCnQnIhgk04ZS2xSqRK4cTq5lr489-BD-vXAQsasEpW12O5ZJ5nTjGEvJq6hul0847SjCjsi42B5A2cEBnD7JeK4mL6LOPQjN0AS8YCN33TJWDgOW3Y-mbBtobiOumNMWiw5-yuVKsFZmDl_dyqi7SwDBMXcKloJ9-Jc1Rud1cs37aO4luy_IYr4QG_K7JdJQGMT_zpjGI-iKJY--ch5n8_Vay0DJhyLp436YlDGfIY5KD5_Tunrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من لقاء وزير الخارجية الإيراني عراقجي بوزير الداخلية الباكستاني.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75796" target="_blank">📅 10:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75795">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇵🇱
🏴‍☠️
بولندا تستدعي القائم بالأعمال الإسرائيلي بشأن احتجاز نشطاء أسطول الصمود
نطالب إسرائيل بالإفراج الفوري عن مواطنينا ومعاملتهم وفقا للمعايير الدولية
ننصح مواطنينا بعدم السفر إلى إسرائيل</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75795" target="_blank">📅 10:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75794">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇪🇸
وزير الخارجية الإسباني: ترحيل 44 من نشطاء أسطول الصمود من إسرائيل إلى إسبانيا عبر تركيا مساء اليوم</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75794" target="_blank">📅 10:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75793">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن ضباط كبار:
لا جدوى من البقاء في لبنان والجيش لا يحقق إنجازات في هذه الحرب بشكلها الحالي
مهمتنا غير مفهومة ولا نعرف إن كان الجيش يريد وقفا لإطلاق النار  في لبنان
لا يوجد وقف إطلاق نار في جنوب لبنان لكن لا يمكننا تفعيل كامل قوتنا
هناك تحديات كثيرة في الجبهة اللبنانية فإما أن تسمح لنا القيادة بالعمل أو ننسحب</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75793" target="_blank">📅 09:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75792">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-vNn50y9E6xbmqU-HBFOmfTTR3VppMgINDNNLRWopFj74gbvRf6twX5oNfgQGzGpz_m6Qkgsb7j5VBGzc5SDEIuJC6wFZUNMkJG0tahvfBP15Q7JELi0ruKVle_6ybnwzTYwmxQJNfj8QbxEi6goPZ7RIIp_Unn6xHTGMYQYvvcqDNd_HhCoHGQheqAqYNnE83pDoOOQVV7KgbKiy-u5lv54kVLAbN2O6C-E3JcnuMbtfpWX6wATjlqTbYdqIn56m_V-CvGqdJqITp0BveAaG2vYE7qviJybirwkNGX5j5xpGxedfB7uhL8B0MGgrOS7tpaZ95Y3aBNpJ11egN_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو
في تلك الأيام، في مثل هذا الوقت: عشية عيد الأسابيع (شفوعوت) عام ١٩٨١، دمر سلاح الجو الإسرائيلي
المفاعل النووي العراقي
. زجّ الهجوم "إسرائيل" في جدل سياسي، إذ كانت آنذاك في خضم حملة انتخابية محمومة للكنيست العاشر. اتهمت المعارضة بيغن بالتضحية بالأمن والمصالح السياسية في سبيل الدعاية الانتخابية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75792" target="_blank">📅 08:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75791">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
مساعد قائد البحرية في الحرس الثوري الإيراني:
أيدينا على الزناد وإذا كان ترامب يظن أنه يستطيع فتح مضيق هرمز بالقوة والسفن، فعليه أن يعلم أن البحرية نفسها التي زعمتم أنها دُمرت ستُغرقكم في قاع البحر.
على أعدائنا أن يعلموا أنهم مخطئون تمامًا إن ظنوا أن هذه الأمة ستتراجع بتدمير بنيتها التحتية، فقد أثبتت هذه الأمة على مدى 47 عامًا أنها قابلة للتدمير لكنها لا تستسلم.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75791" target="_blank">📅 23:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75790">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
هجوم مسلح من قبل عناصر إرهابية يطال عجلة تابعة للقوات الأمنية في مدينة سراوان بمحافظة بلوشستان جنوب شرق إيران ؛ إستشهاد أحد أفراد الأمن الإيراني كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75790" target="_blank">📅 23:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75789">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGR58ax5-XUxnIJhQzQQkLruW_b-9FK6fuNCdrQPi4QP-Z7LU6ABdGgVeGalNfpiLP9GS-OcoV85Sd3MYTI8g8UfsWistRIV0QmaVkiyF9AdrQIT5qA7uXFH3pb_o6SUcOE4v0BJX5sN809USgKu6157-XR8_hVE5z1fOR0An2W1yme-onG5rp4mq9yL3ZwZfLNLd7NRO7kWzMZ2cERObR1e-1yIRtq05U_AoY9cakQSym6cW0p9KOWOqMl_NL0J968MsXn2H-p7CI7l-dvSrSyfGs0VcbjVUK-JELMEW8MOd1MmUBaybuMccRnSdkv0KnATeddFPpiLbuwYbJmppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هيئة إدارة مضيق الخليج الفارسي:
حددت الجمهورية الإسلامية الإيرانية حدود منطقة الإشراف على إدارة مضيق هرمز على النحو التالي: "الخط الذي يربط جبل كوه مبارك في إيران وجنوب الفجيرة في الإمارات العربية المتحدة شرق المضيق بالخط الذي يربط نهاية جزيرة قشم في إيران وأم القيوين في الإمارات العربية المتحدة غرب المضيق.
يتطلب المرور في هذه المنطقة عبر مضيق هرمز التنسيق مع إدارة الممرات المائية في الخليج الفارسي والحصول على إذن من هذه المؤسسة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75789" target="_blank">📅 23:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75788">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ddf11200.mp4?token=N3mhVe8IDJbXgn6q_FuaHu4VV4A80fQNbGBABxW9tlDvD5xVxbV8hSxI40qAp_wJ-NNDbgV9NhE4ZW725RlvibclVtYbUWfBKnPaxSmo5r1dCrYIudyzH8P0Ro_7CwgGDG2VNJETAiIHBL7D4MlQ67v5mHMeumWiDu8Fyl1AwyJqSraZL1nqloAskGFOumnyc8OlTvcAtscZguwgoHF5emPkddGt0yTVy6EpGk-hUIQTm0-FFme8VOyDi2rYVwKQe_NpjGCknznNVfxUce7ayJIrJQW6cnWIds7RX1DBsawZgWnC8DIPXPMO7lpwgaABoNjBt_VM2s9HghtgH7-DSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ddf11200.mp4?token=N3mhVe8IDJbXgn6q_FuaHu4VV4A80fQNbGBABxW9tlDvD5xVxbV8hSxI40qAp_wJ-NNDbgV9NhE4ZW725RlvibclVtYbUWfBKnPaxSmo5r1dCrYIudyzH8P0Ro_7CwgGDG2VNJETAiIHBL7D4MlQ67v5mHMeumWiDu8Fyl1AwyJqSraZL1nqloAskGFOumnyc8OlTvcAtscZguwgoHF5emPkddGt0yTVy6EpGk-hUIQTm0-FFme8VOyDi2rYVwKQe_NpjGCknznNVfxUce7ayJIrJQW6cnWIds7RX1DBsawZgWnC8DIPXPMO7lpwgaABoNjBt_VM2s9HghtgH7-DSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوالف الگهوة   من منزل العامري ، طرح مبادرة اليوم تتضمن صلح وبناء الجدار المتصدع داخل الإطار التنسيقي في العراق..</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75788" target="_blank">📅 23:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75787">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bhg7lLgh65EeQX68hls6GPuKSaII-xuZeywJEtZ9ovoXlRFSxP0WY0aUAJJT5USNqeDWltnX9COTj54B6dlpG6VqQMle6VHctp_taMbIKm0Vm2qYqGYSVTKIb0LHXzJA48jCBlxGbOXr92oMkGsbocKKpkJ8OuXrtUSvLJsgK-zKzmgdBhPJyxbq-yUs9JljOWKcqJxUbiJZ37S6pxW2ZcLAf8zVcA_AzWbQdyOY7lDc5UaUOuI07-YO-RFssRNBRw1HeJ2pTTgy3-cxtkDX0JhFXqxReJNt6pEDScJEY1-HTWdNFJf4rrKZJnFCxNYiPBDcZNW7oCd-Bnujoilgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالف الگهوة   من منزل العامري ، طرح مبادرة اليوم تتضمن صلح وبناء الجدار المتصدع داخل الإطار التنسيقي في العراق..</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75787" target="_blank">📅 23:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75786">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭐️
هجوم صاروخي جديد يدك مقرات المعارضة الكرادية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75786" target="_blank">📅 23:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75785">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⭐️
توثيق يظهر تصاعد أعمدة الدخان من مقر تابع لحزب الكوملة الكردي الإرهابي في محافظة السليمانية بعد دكه بمسيرات إنتحارية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75785" target="_blank">📅 23:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75784">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092cf934a6.mp4?token=WkflnzkcGTUSwAm3vEOlYOkXl0QH2OemOfTD8C1tGhInVkKpleHGAO31KcbzvMt3fgJwNzu_oaeOO-ce_Tjh4s5n3qX0Lo9tPSDtSIZ1yVkPGN7PWIcYDclxJ7vgb6pQ10cWjz0I3U-S2-KTQl3_xecLFqo5clFj3TrOrXHPOQuNYZFmWGhrI4lxucuPbK2Sd9-vlQRPehQqQneZfX1jvY9JwVc4qJfGoB9_oSKjZl2aNPmhTiNuJKl90IXIIXtimC50wqjtz4Udqng0lvz64QdQWW2EPVyQI1JSoBYNVrl1xQuQrD7zZ6YVE-ZTiB61_DaDtPZNJG8ibjipe56XgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092cf934a6.mp4?token=WkflnzkcGTUSwAm3vEOlYOkXl0QH2OemOfTD8C1tGhInVkKpleHGAO31KcbzvMt3fgJwNzu_oaeOO-ce_Tjh4s5n3qX0Lo9tPSDtSIZ1yVkPGN7PWIcYDclxJ7vgb6pQ10cWjz0I3U-S2-KTQl3_xecLFqo5clFj3TrOrXHPOQuNYZFmWGhrI4lxucuPbK2Sd9-vlQRPehQqQneZfX1jvY9JwVc4qJfGoB9_oSKjZl2aNPmhTiNuJKl90IXIIXtimC50wqjtz4Udqng0lvz64QdQWW2EPVyQI1JSoBYNVrl1xQuQrD7zZ6YVE-ZTiB61_DaDtPZNJG8ibjipe56XgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجار جراء هجوم بطائرة مسيرة انتحارية استهدفت مقر تابع للمعارضة الكردية (الكوملة) في محافظة السليمانية ضمن اقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75784" target="_blank">📅 23:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75783">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f0661e65.mp4?token=GzP_IfvTaeHGhPXHMIUPteBnT-3YO143jTQrpyc8l9jv1Z1y6cduoWZy10dBI0jbtvlRnndg6cyNg9S3UdEVxTOjZmuBlFyPcR158wNdsbjQTmx-4SgTwqo7O6O3leipiJAZQljFMLkQSFxdk1GiJztUJ-fYkTHxIe8s41sqaF0OgDppnuNAkFbXSarZZ5Vfqlh42lmslROZIuUNfXTc7rS_0eaVZmEOUz8gdqsKk0WjbH9T00_ObxOzEEQInAaBHBVR5NBAcMLEUiGQgwCHgPB5UxNwkTzcxokyg8kePfN0-WUzcIxXLZr6rFM2HX854SodXfnTtG5sEiaEQdR9Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f0661e65.mp4?token=GzP_IfvTaeHGhPXHMIUPteBnT-3YO143jTQrpyc8l9jv1Z1y6cduoWZy10dBI0jbtvlRnndg6cyNg9S3UdEVxTOjZmuBlFyPcR158wNdsbjQTmx-4SgTwqo7O6O3leipiJAZQljFMLkQSFxdk1GiJztUJ-fYkTHxIe8s41sqaF0OgDppnuNAkFbXSarZZ5Vfqlh42lmslROZIuUNfXTc7rS_0eaVZmEOUz8gdqsKk0WjbH9T00_ObxOzEEQInAaBHBVR5NBAcMLEUiGQgwCHgPB5UxNwkTzcxokyg8kePfN0-WUzcIxXLZr6rFM2HX854SodXfnTtG5sEiaEQdR9Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مواطنة جرينلاندية تهتف ضد مبعوث ترامب إلى جرينلاند "جيف لاندري" وتدعوه إلى ترك بلدها والعودة إلى منزله.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75783" target="_blank">📅 22:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75782">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الصهيوني:
إصابة 7 من ضباط وجنود الجيش (بعضها حرجة) نتيجة سقوط طائرة بدون طيار مفخخة في جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75782" target="_blank">📅 22:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75781">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228ceb0fe.mp4?token=EDMOcQLf9k-7QAL8i5S8M2BPOm2BwHl-BlSti1BwpftF7bw7xVZpS87jTNoF2JcsdndlBnodcobTqnVntumrcri5GC9TepS2rdH_jI8M8BfZvoSvOGak54kZE7Lm-v6M-FXkA2NGRRTTW_6qucn58Xj8yYnj9QdA8u1xoYysOhp6hT0oBBZ0LuZpQXVLvvc_2q2KIbnJNPez3am6pDRKNgRRrLLiNB7QCYkgja9TaWetoObLyeee8rhzsyH55I9QAhYKmZImmeheXByXv7gz6HQHVrGbs4YQrPoROuBruKufePNjD3atGaY28wazl79jvJXIxjD5VyTMzzXnJLfHVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228ceb0fe.mp4?token=EDMOcQLf9k-7QAL8i5S8M2BPOm2BwHl-BlSti1BwpftF7bw7xVZpS87jTNoF2JcsdndlBnodcobTqnVntumrcri5GC9TepS2rdH_jI8M8BfZvoSvOGak54kZE7Lm-v6M-FXkA2NGRRTTW_6qucn58Xj8yYnj9QdA8u1xoYysOhp6hT0oBBZ0LuZpQXVLvvc_2q2KIbnJNPez3am6pDRKNgRRrLLiNB7QCYkgja9TaWetoObLyeee8rhzsyH55I9QAhYKmZImmeheXByXv7gz6HQHVrGbs4YQrPoROuBruKufePNjD3atGaY28wazl79jvJXIxjD5VyTMzzXnJLfHVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران حربي منخفض في أجواء محافظة الموصل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75781" target="_blank">📅 22:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75780">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🌟
الله أكبر.. استهداف قوة مشاة ودبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة حداثا من قبل أبناء نصرالله.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75780" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75779">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f088d5ca1a.mp4?token=li82aT1b4S4b1Bn-MhBKI2qtxVXc05u0JsIeGFzUNuJcmw2NqF7EJTEiwdjuh1-uLYozkw1QY1Nb2brQxYSUAdFB5aPJlDaXWt7Ji4P0DuVV8-vV4AoA2JQ_xHCWre-ifRmAId1dsuRRn81vLjdY_C2-sVLuTdlm-Qh196sQSBHjuMeYHfthhuhONfFowIJvvOHhdvQ9YmqB4aHTm85YgA-eMv3prTr2g59UzBTSe8xcErbzzWzKDPXD2ze-ru-0ctuW3-uEY5dAtdi4HEK6OlLFwMtnTHB4u8J-RMOXBVTWR3a6icRG2Fvxmu3ukM0mc8ZRPYjEAcsr1L_Sn6NhG2oXsgw7HU5elYby8n4U_B13IV5FMgFIMecAJvnd6WzKNdOzpuC3JVP72Gmvcw9aa2ib_AzrBAGoKzuMSWAS-WbtPVOBg0WHBAYhlRnDp4tAGxoBdK-MZa3dFJQOZyDKH9PV4wxap7FnQdGlSV6PiGjvuzpV7Q1Hn1nwsJuZdZPcjP2qYoTByIIEkIEaJet-z_MGgJGvaFAM7HgBW4bYMR4xMc6nez4Dki6LNFNLjjO_tiPzubE53G5zvV5rRrW3dGqctFe35HRx3SUotkpy8mXC8HuqivUh_Lk0HLZAWSjgwETiQDSudCd5pukx2DGsyxjjsflwZRR7i8AMzvMftcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f088d5ca1a.mp4?token=li82aT1b4S4b1Bn-MhBKI2qtxVXc05u0JsIeGFzUNuJcmw2NqF7EJTEiwdjuh1-uLYozkw1QY1Nb2brQxYSUAdFB5aPJlDaXWt7Ji4P0DuVV8-vV4AoA2JQ_xHCWre-ifRmAId1dsuRRn81vLjdY_C2-sVLuTdlm-Qh196sQSBHjuMeYHfthhuhONfFowIJvvOHhdvQ9YmqB4aHTm85YgA-eMv3prTr2g59UzBTSe8xcErbzzWzKDPXD2ze-ru-0ctuW3-uEY5dAtdi4HEK6OlLFwMtnTHB4u8J-RMOXBVTWR3a6icRG2Fvxmu3ukM0mc8ZRPYjEAcsr1L_Sn6NhG2oXsgw7HU5elYby8n4U_B13IV5FMgFIMecAJvnd6WzKNdOzpuC3JVP72Gmvcw9aa2ib_AzrBAGoKzuMSWAS-WbtPVOBg0WHBAYhlRnDp4tAGxoBdK-MZa3dFJQOZyDKH9PV4wxap7FnQdGlSV6PiGjvuzpV7Q1Hn1nwsJuZdZPcjP2qYoTByIIEkIEaJet-z_MGgJGvaFAM7HgBW4bYMR4xMc6nez4Dki6LNFNLjjO_tiPzubE53G5zvV5rRrW3dGqctFe35HRx3SUotkpy8mXC8HuqivUh_Lk0HLZAWSjgwETiQDSudCd5pukx2DGsyxjjsflwZRR7i8AMzvMftcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: نقوم بتحرير كوبا وعلينا مساعدة الكوبيين فليس لديهم طعام ولا طاقة لكنهم شعب عظيم.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75779" target="_blank">📅 22:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75778">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامب: نقوم بتحرير كوبا وعلينا مساعدة الكوبيين فليس لديهم طعام ولا طاقة لكنهم شعب عظيم.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/75778" target="_blank">📅 22:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75777">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d5c56470.mp4?token=TbDEG2PNi8RJFZZniLgj-FvfvuXnSoMHGyyzbV-PIks6qvVsz9KmV0vbDuajYKW9bZQPqWX0Enf1Ds3VCAQC1pyeFT8fECupkqo3PN91yDjRzkycsPoOHZDwOjI9MHUNiaR3giUGzqeCJCmz27sHF-ibS9WfQtR6a4mNafw6pVpUioqNv2tVgwnP5iRY87WBzkgSsZNANb5euCAvYfxyHOK_Cb08SwC1_R-wDf5cUg5KU8oUid6yHvWiuUpFJ5W9u8w0ZI1Blqd8tCJL9GeYsLnyaQIeb-i2HzCw5U2Kseq0YLlpMDLOtjKAwX1jQ5ymqisNbpaUol6s1JS6GL9IMapTutjinAT34YsJwHLAgEOnoBLLQYKr1Ki-kwypm7A9yJIQx2cgO4P8DVGhxK4BNUWgzOuIP1KrE92QztBf4mLm87pRWqGhKgfYx9pS_nmG3qk0TuKUThm_pXH-kwY7ZpYl9kAe-LJ7UWWbw664Ek8P-skgb16LHEae77GiPbrRf4TGae9g6xG0204f_Tras4sKZnF43gcJb9dt-8uFHIwvgKt7CIhsjbJ6YsN41O97jmo2sRenr33becWidxs8MRZ4jA6BtVwp--6vbjble--HEoSWzqJVax0IQ-daZCdkW-Px9ZojsvbF8-cdnI5FNKS1U9bk161ARMDYjVtOsHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d5c56470.mp4?token=TbDEG2PNi8RJFZZniLgj-FvfvuXnSoMHGyyzbV-PIks6qvVsz9KmV0vbDuajYKW9bZQPqWX0Enf1Ds3VCAQC1pyeFT8fECupkqo3PN91yDjRzkycsPoOHZDwOjI9MHUNiaR3giUGzqeCJCmz27sHF-ibS9WfQtR6a4mNafw6pVpUioqNv2tVgwnP5iRY87WBzkgSsZNANb5euCAvYfxyHOK_Cb08SwC1_R-wDf5cUg5KU8oUid6yHvWiuUpFJ5W9u8w0ZI1Blqd8tCJL9GeYsLnyaQIeb-i2HzCw5U2Kseq0YLlpMDLOtjKAwX1jQ5ymqisNbpaUol6s1JS6GL9IMapTutjinAT34YsJwHLAgEOnoBLLQYKr1Ki-kwypm7A9yJIQx2cgO4P8DVGhxK4BNUWgzOuIP1KrE92QztBf4mLm87pRWqGhKgfYx9pS_nmG3qk0TuKUThm_pXH-kwY7ZpYl9kAe-LJ7UWWbw664Ek8P-skgb16LHEae77GiPbrRf4TGae9g6xG0204f_Tras4sKZnF43gcJb9dt-8uFHIwvgKt7CIhsjbJ6YsN41O97jmo2sRenr33becWidxs8MRZ4jA6BtVwp--6vbjble--HEoSWzqJVax0IQ-daZCdkW-Px9ZojsvbF8-cdnI5FNKS1U9bk161ARMDYjVtOsHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
16-05-2026
آلية هامر تابعة لجيش العدو الإسرائيلي في اسكندرونة ببلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75777" target="_blank">📅 22:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75776">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يعلن عن إستهداف وإسقاط مسيرة صهيونية من طراز "هرمز 450" بصاروخ أرض جو في القطاع الأوسط اللبناني.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75776" target="_blank">📅 22:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75775">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⭐️
إنفجار جراء هجوم بطائرة مسيرة انتحارية استهدفت مقر تابع للمعارضة الكردية (الكوملة) في محافظة السليمانية ضمن اقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75775" target="_blank">📅 21:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75774">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-OfHfNx8-ahEIIRjN3zkLhEBoi7MhVdwH2lXx2OcHLpxQewKLKJVPJj9ZNrC340SiBYuWWqomS8JgjEIzMhB-PfUCjyLYaUNJdMvNfF-2s5t7Z5mcrOrrhV8yf-RmhPaP0B-tCqV7EM6cXAAk3LuxQCPKf2I5DDiHqxxHKNIdvuxRd_q8162CjzeeHD9CDJ22TYy4T_AtwYrnw0_6wllgq_oxGW29ZdXKPCkLS3A0G1_jGsSVZD1qvYSItJ6Sr3ssXfk1cjNeDxRDbFlT0HBZSz2lTQrUXPDOMkM1MmAcToOQ3vXaU_GgcqHNBUfXpAbujzl6dSgLJ58uEaBkbpqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إن الأمريكيين، بعد إرسالهم رسالة إيرانية من 14 بندًا قبل ثلاثة أيام، أرسلوا رسالة أخرى إلى إيران عبر وسيط باكستاني. تدرس إيران الرسالة ولم تردّ عليها بعد. يسعى الوسيط الباكستاني في طهران إلى تقريب وجهات النظر بين الرسالتين. لم يتم التوصل…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75774" target="_blank">📅 21:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75773">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الإسرائيلية: نتنياهو يحاول إقناع ترمب بمنح الضوء الأخضر لاستئناف الحرب على إيران.  ‏نتنياهو لم يكن على توافق مع رأي ترامب بشأن التفاوض مع إيران.   ترامب يميل لدعم توجيه ضربة عسكرية لكنه لا يزال يترك نافذة ضيقة للمفاوضات مع إيران.   إسرائيل تتخذ…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/75773" target="_blank">📅 21:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75772">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
🏴‍☠️
محرقة جديدة للميركافا.. حزب الله يعلن عن إستهداف 3 دبابات ميركافا وجرافتين D9 تابعة لجيش الإحتلال الصهيوني في بلدة حداثا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75772" target="_blank">📅 21:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75771">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: استهداف دبابة ميركافا وإعطابها بواسطة صاروخ موجه في جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75771" target="_blank">📅 21:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75770">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8a416d9e.mp4?token=ieMSFbn9siTihmouoZbE0UPGqhHsUm4e5TiyokTH4TqRuKS_7AHWclro0rIak4kkKZpSCt722FJrZWgI1pX_m-Gm0DyUDkv-8paNc8So50p4x3ok9uUEb7gfEQVmXjVbWz_TIKHufxtCGmeitYee1H4HOU8j0oWmuzxW9j-dw6KQkETrR-3JiNm3MVxvk1epaUcigdTLjYZsVmpuYNx-JuY4y4lXXTg1QNdLmETKgB4E3BnBVdudmeyUuqNEnXjzaIYES-KJfkQQyneo-9MtKIgEJmBPxPowD0OYSSlzv9Gfu6yIj5JAAYHUV6BG_j0JAAqxQkFd2ypavQ0bZ8A1mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8a416d9e.mp4?token=ieMSFbn9siTihmouoZbE0UPGqhHsUm4e5TiyokTH4TqRuKS_7AHWclro0rIak4kkKZpSCt722FJrZWgI1pX_m-Gm0DyUDkv-8paNc8So50p4x3ok9uUEb7gfEQVmXjVbWz_TIKHufxtCGmeitYee1H4HOU8j0oWmuzxW9j-dw6KQkETrR-3JiNm3MVxvk1epaUcigdTLjYZsVmpuYNx-JuY4y4lXXTg1QNdLmETKgB4E3BnBVdudmeyUuqNEnXjzaIYES-KJfkQQyneo-9MtKIgEJmBPxPowD0OYSSlzv9Gfu6yIj5JAAYHUV6BG_j0JAAqxQkFd2ypavQ0bZ8A1mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
نيابة عن شرفاء العالم..
ناشطة تبصق على جندي إسرائيلي أثناء اختطاف نشطاء "أسطول الصمود" السلميين والتنكيل بهم.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75770" target="_blank">📅 21:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75769">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الإسرائيلية: نتنياهو يحاول إقناع ترمب بمنح الضوء الأخضر لاستئناف الحرب على إيران.  ‏نتنياهو لم يكن على توافق مع رأي ترامب بشأن التفاوض مع إيران.   ترامب يميل لدعم توجيه ضربة عسكرية لكنه لا يزال يترك نافذة ضيقة للمفاوضات مع إيران.   إسرائيل تتخذ…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75769" target="_blank">📅 20:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75768">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏ترامب: رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه  متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/75768" target="_blank">📅 20:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75767">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff7f595ec.mp4?token=CBLGrAYuw89kmkvQXu-daj7rRXgwVes_JHMhAnlXjEjl4oEopEVfbk0tB1d9P_WGzwSXu-V5FhWOM2_SFkSsGurhRczkMQY7lqE7hPxZTv8Tj-hE5c0fn3WfM00oat8iaSH-QJMhMyZf7F93oHOqEvrJMu1xmnLU1peOjz9289g3likzSXn5ynmUiu1o3YPKHWNIB5jcE42_De72U4-ifEj4gfxr47xf1UbCG8dSUFc4-rV55yajLICI3eg3soKNGpeu7kMFYAT3hVlbYKwVW8UkhBdoVm1p2QcpdCN317OQXuQHmAZ--3CfP-0ZFKOTyjjlHN90xhvP0vSczKP3_1jy_m0Xlwr4iqlzDRZSYoKoSew-lOacv62hyAL8IiFlOTU-NL1l9OqYsjcl-K9Wm_1k3kpWuCk4B5-oC6URhITgyFXudtsA3hD71YHnwZv_cp1XTa-3U436dknjQ2mL_ySvw6Z6XIHUqW5nPQvDp9r07wI8CyRoH5kvpTXTb6Lm_9teJtuaBnEUNxBnt6_dtHFVOGJahzTAhkNoZW5NAfRpj5qflpUvmJbWFmFBAqfBn3t0hCeVBs5JEQyBqLrBQLl97aSfvbUZyenXIEpaaN9IWd8LzFaqYbDXug2sWkHAVsUu4TRY2QEMIm1hNzSJ13RU4Q5d23uMIYLcWFsAPlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff7f595ec.mp4?token=CBLGrAYuw89kmkvQXu-daj7rRXgwVes_JHMhAnlXjEjl4oEopEVfbk0tB1d9P_WGzwSXu-V5FhWOM2_SFkSsGurhRczkMQY7lqE7hPxZTv8Tj-hE5c0fn3WfM00oat8iaSH-QJMhMyZf7F93oHOqEvrJMu1xmnLU1peOjz9289g3likzSXn5ynmUiu1o3YPKHWNIB5jcE42_De72U4-ifEj4gfxr47xf1UbCG8dSUFc4-rV55yajLICI3eg3soKNGpeu7kMFYAT3hVlbYKwVW8UkhBdoVm1p2QcpdCN317OQXuQHmAZ--3CfP-0ZFKOTyjjlHN90xhvP0vSczKP3_1jy_m0Xlwr4iqlzDRZSYoKoSew-lOacv62hyAL8IiFlOTU-NL1l9OqYsjcl-K9Wm_1k3kpWuCk4B5-oC6URhITgyFXudtsA3hD71YHnwZv_cp1XTa-3U436dknjQ2mL_ySvw6Z6XIHUqW5nPQvDp9r07wI8CyRoH5kvpTXTb6Lm_9teJtuaBnEUNxBnt6_dtHFVOGJahzTAhkNoZW5NAfRpj5qflpUvmJbWFmFBAqfBn3t0hCeVBs5JEQyBqLrBQLl97aSfvbUZyenXIEpaaN9IWd8LzFaqYbDXug2sWkHAVsUu4TRY2QEMIm1hNzSJ13RU4Q5d23uMIYLcWFsAPlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
17-05-2026
تموضع لوجستي تابع لجيش العدو الإسرائيلي في اسكندرونة ببلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75767" target="_blank">📅 20:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75766">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73f31002da.mp4?token=f9GtIQDJrrZWSuTAQz4QJqBUnqVYI2Mh45tLojbcSZEs2H6C_723QOp6_YDsr5pChjUTFvgec1RKoSTeOYb_pm4hPTNDaNEgjuE_GGEFSIluYn0qMDaMfE9zztCRIoTPTsCvgUvKAfvKKsLxZuiOsg2ioYn9SAiyJfJB61--YH1ESNhtKIfgllMYt3qzvFEmx_5Nr0GHE5FvvOjmqBY3-sh3MK58jkaes7fmjDxSFUIRGhNiIiWVbSiKD2P4Llu04olN8nv4AkQPm9bdBFGkXIDqe_Xvpm1sGVoIdV-4MERFwkEKZrtlyozkBMeIA2KEzhzmCdmU966VNA9sLatwAzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73f31002da.mp4?token=f9GtIQDJrrZWSuTAQz4QJqBUnqVYI2Mh45tLojbcSZEs2H6C_723QOp6_YDsr5pChjUTFvgec1RKoSTeOYb_pm4hPTNDaNEgjuE_GGEFSIluYn0qMDaMfE9zztCRIoTPTsCvgUvKAfvKKsLxZuiOsg2ioYn9SAiyJfJB61--YH1ESNhtKIfgllMYt3qzvFEmx_5Nr0GHE5FvvOjmqBY3-sh3MK58jkaes7fmjDxSFUIRGhNiIiWVbSiKD2P4Llu04olN8nv4AkQPm9bdBFGkXIDqe_Xvpm1sGVoIdV-4MERFwkEKZrtlyozkBMeIA2KEzhzmCdmU966VNA9sLatwAzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية تزعم:
في وقت سابق اليوم في خليج عمان، استولى مشاة البحرية الأمريكية من الوحدة البحرية الاستكشافية الـ 31 على سفينة النفط التجارية M/T Celestial Sea، التي ترفع العلم الإيراني، والتي يشتبه في أنها حاولت انتهاك الحصار الأمريكي من خلال العبور نحو ميناء إيراني.
أطلقت القوات الأمريكية سراح السفينة بعد تفتيشها وإصدار الأوامر لطاقم السفينة بتغيير مسارها.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75766" target="_blank">📅 20:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75765">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
نركز حاليا على إنهاء الحرب في جميع الجبهات لا سيما لبنان.
إذا أصر الطرف المقابل على مطالبه المفرطة فإنه يمكن القول إن الدبلوماسية لم تحقق نتائجها.
الحديث عن الإنذارات والمواعيد النهائية بشأن إيران أمرٌ سخيف.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75765" target="_blank">📅 20:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75764">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⭐️
رويترز:
بعض السفن تدفع لإيران ما يزيد عن 150 ألف دولار لضمان مرور مضيق هرمز.
‏رسوم عبور السفن لمضيق هرمز لا تفرض على كافة الدول.
‏الآلية الإيرانية الجديدة في مضيق هرمز تعطي الأفضلية للسفن المرتبطة بروسيا والصين.
‏"وثيقة الانتماء" التي تقدم للسفن مقابل عبور هرمز تؤكد عدم ارتباطها بأميركا أو تل أبيب.
‏الدول التي ترغب في عبور سفنها مضيق هرمز يجب أن تتصل بوزير الخارجية الإيراني.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75764" target="_blank">📅 20:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75763">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⭐️
إستمرار موجة الإنسحابات..
النائب "حسن قاسم الخفاجي" يعلن إنسحابه عن تحالف الإعمار والتنمية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75763" target="_blank">📅 20:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75762">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2e4689c.mp4?token=X8YDH7K9w0Jcz0C-3viUmFioKJtwNRdDTV2-2b60HrzSQ-Hbxb3QuWakbfrxCpx77b1gT66IaPCSxJPyzdy9Dtv2NvDaXV70PgSNFRaeOh53WifRKLHGzYG94IIFMTkrcTfBr_ZsnMcp3JuEJn2G8ccXMQ2UtIEKl7swN4gKh1i8W1rs2V1ExgSx01fxUVVQ8lwYXliSXwal_heTGsd0AXIM0hq1hpiOHIoA5BWdihma-TkUxeo9v32Ff1LJza7fLj2xvzXK0wtl-rU6MPRgfc58rdkbkm-F3JIid-B79C7jnIExIlzrijbpNrPh97qrfRNH3gE-EEfG7i9zbHSDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2e4689c.mp4?token=X8YDH7K9w0Jcz0C-3viUmFioKJtwNRdDTV2-2b60HrzSQ-Hbxb3QuWakbfrxCpx77b1gT66IaPCSxJPyzdy9Dtv2NvDaXV70PgSNFRaeOh53WifRKLHGzYG94IIFMTkrcTfBr_ZsnMcp3JuEJn2G8ccXMQ2UtIEKl7swN4gKh1i8W1rs2V1ExgSx01fxUVVQ8lwYXliSXwal_heTGsd0AXIM0hq1hpiOHIoA5BWdihma-TkUxeo9v32Ff1LJza7fLj2xvzXK0wtl-rU6MPRgfc58rdkbkm-F3JIid-B79C7jnIExIlzrijbpNrPh97qrfRNH3gE-EEfG7i9zbHSDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب: سنمنح ايران فرصة واحدة، أنا لست في عجلة من أمري.  إما أن نتوصل إلى اتفاق مع إيران أو سنقوم بأمور قاسية ونأمل ألا يحدث ذلك.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75762" target="_blank">📅 19:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75761">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
هجوم مسلح من قبل عناصر إرهابية يطال عجلة تابعة للقوات الأمنية في مدينة سراوان بمحافظة بلوشستان جنوب شرق إيران ؛ إستشهاد أحد أفراد الأمن الإيراني كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75761" target="_blank">📅 19:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75760">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
استهداف دبابة ميركافا وإعطابها بواسطة صاروخ موجه في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75760" target="_blank">📅 19:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75759">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93dd2e141.mp4?token=s8x8AYc_ektokuN8ahN-pPE8vyQw3lHfgIeV0iNL21GY0Wkwdl7J9WfPJeUoKTTTC12vi8hx3fR0vN07NralTFcRE985Tf7Er13hfFM688B8Yy43PK4CGGuDHqC7At-XgVXuzzDjMcU8YDGVkd4BOycstXXKAsTKTLM3xRWQ2kO64XaP0Xuzi3G6qRKkW8eDwree04tfp5Xv0UJi-5VaBZJdLtC4Ix69_HTc9d-SeGY-DF2EOUoCVuF6j_u1JhwpmAwtkypECkHZDojq2yxCua8BkypYv4BYpsQ-prXKnNdJlSAVIFl45qEpixXVfgQvIY7w6Qi9vtiLfoqdMqW7cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93dd2e141.mp4?token=s8x8AYc_ektokuN8ahN-pPE8vyQw3lHfgIeV0iNL21GY0Wkwdl7J9WfPJeUoKTTTC12vi8hx3fR0vN07NralTFcRE985Tf7Er13hfFM688B8Yy43PK4CGGuDHqC7At-XgVXuzzDjMcU8YDGVkd4BOycstXXKAsTKTLM3xRWQ2kO64XaP0Xuzi3G6qRKkW8eDwree04tfp5Xv0UJi-5VaBZJdLtC4Ix69_HTc9d-SeGY-DF2EOUoCVuF6j_u1JhwpmAwtkypECkHZDojq2yxCua8BkypYv4BYpsQ-prXKnNdJlSAVIFl45qEpixXVfgQvIY7w6Qi9vtiLfoqdMqW7cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🏴‍☠️
ضمن الإستعدادات العسكرية للعدو الصهيوأمريكي..
مشاهد تظهر العديد من طائرات التزود بالوقود الأمريكية في مطار بن غوريون الصهيوني.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75759" target="_blank">📅 18:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75758">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nA9Pe9ESzTXJL989fzb5YPX12t5np8oybqZS6VOnsKi6o9gXlb5SLpb-C2dSzYS4ScbRIdagFzHJ5qOe7Oe8EvEyRc7XAV37S7vl4nP52t6IBvlgxV_OKmwZ6I9rJWYCVK23EdHCwxxDegbL4a5021WOhNekKyW0YgttKo7b97TIDi1nfFXf_oQ7zIJEZ34sQXda0RdnyVFliBpebUVgExM8zUh_YCb2QqbFyarmlSsAodNax1Bhm_bNYR7wvqC3zS-_x59w_ByPNg9rGsGS1MzabnqzEBV2QWfXyhn-KqYIUFsMA_w15NCH-7BKOFmzPLXJCDtptX6sZ-ePJR4ubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
من المثير للصدمة أن الجمهوريين احتفظوا بالموقف المهم جدا "البرلماني" في أيدي امرأة، إليزابيث ماكدونو، التي عينها، منذ فترة طويلة، من قبل باراك حسين أوباما والمجنون الشرير المعروف باسم السيناتور هاري ريد، الذي أدار مجلس الشيوخ للدوموقراطيين ب "قبضة حديدية". على مر السنين، كانت وحشية للجمهوريين، ولكن ليس كذلك بالنسبة للدومقراطيين - فلماذا لم يتم استبدالها؟ هناك العديد من الأشخاص العادلين الذين سيكونون مؤهلين لتلك الوظيفة الحيوية.
يلعب الجمهوريون لعبة ناعمة للغاية مقارنة بالدوموقراطيين. إنه أكبر عيب في السياسة. يغش الدوموقراطيون ويكذبون ويسرقون، خاصة عندما يتعلق الأمر بالأصوات في الانتخابات، ولكنهم يلتزمون ببعضهم البعض، في حين يسمح الجمهوريون لإليزابيث ماكدونوز في العالم بالبقاء في السلطة، ووحشيتنا. نحن بحاجة إلى تمرير قانون إنقاذ أمريكا، والآن - وبالمثل، قتل المماطلة، التي من شأنها أن تعطينا كل شيء! إذا لم نمرر واحدا على الأقل من هذين الحكمين بسرعة، فلن ترى رئيسا جمهوريا آخر مرة أخرى. سينتهي الأمر بالدوموقراطيين بولايتين إضافيتين، العاصمة وبورتوريكو، وكل ما يترتب على ذلك، بما في ذلك
4 أعضاء في مجلس الشيوخ، والعديد من أعضاء الكونغرس، والعديد من الأصوات الانتخابية الإضافية، وسيحصلون أيضا على حلمهم في محكمة عليا للولايات المتحدة معبأة برقمهم المفضل - 21 قاضيا.
سيقضي الدوموقراطيون على المماطلة في اليوم الأول الذي يحصلون فيه على فرصة للقيام بذلك.
الجمهوريون لا يفعلون ذلك لأنهم يقولون إن الدوموقراطيين لن يفعلوا ذلك أبدا، لكن الجمهوريين مخطئون. كن جمهوريين أذكياء وصعبين، وإلا ستبحثون جميعا عن وظيفة في وقت أقرب بكثير مما كنتم تعتقدون أنه ممكن!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75758" target="_blank">📅 18:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75757">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d89ae9e5.mp4?token=CdwpqpDDeG6FwEEeTTZwHcPlP2LZ7kWZP53Hc38R6P5KeB-GIc9iMZRYMNH9h5h1lVqXO80OA0iv2L8ZkQPG1ar6h2w1xfnoURURraRgQPFBEC8HYd0p9OaeahYH1f8UNFWhkJzCugYkpOSnSrxw4HBznJaRdxoKKTXrXVD6uHXQ3UNpvabDjgbSdpzbe9-v9-ILywEpacXCSFDAQwVquTym_Ay-jVKr0Kew27duXfRo_STs2TB-dNiOfbJT2TeWpexvsnprmg06giJKM9ICqjidPMTaVO6mRh7LkXTNQS3u1QgS8w2jdxjpmcsIiQwr4oAnktDbx4NE_CZFKgwlU5_IQlPtBAfRSBKaMTrzMfl0gRBOQjpEeJGXlufP5zEAGisduCLxqRr_bh-iG3Jfi_h9eB_4MuWq-OcNFRe4FEKemWLw5TVuYCulBtCUKB7MB_dDDrdjRLHCs98Sl0kRkcwAmYlXrF8WMColFWGepl_hBT1IL_tbUXxlCRLWB4Aw7YYK842hts6arH2P4ZcFwDMjmbRkkBbPTvaah15J2u7TugX1eKL_ZSXNPDVFO5aLdQEjDrE6S9n6uRXmtsGPyVtwOWoCoF_kMJIPYplvwcWCXwrMEYUFZ6yPiefUGX4WTI9plk_J0FAHppCSQjTUqJwwfYAHKT3-SpAz7Df2Kow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d89ae9e5.mp4?token=CdwpqpDDeG6FwEEeTTZwHcPlP2LZ7kWZP53Hc38R6P5KeB-GIc9iMZRYMNH9h5h1lVqXO80OA0iv2L8ZkQPG1ar6h2w1xfnoURURraRgQPFBEC8HYd0p9OaeahYH1f8UNFWhkJzCugYkpOSnSrxw4HBznJaRdxoKKTXrXVD6uHXQ3UNpvabDjgbSdpzbe9-v9-ILywEpacXCSFDAQwVquTym_Ay-jVKr0Kew27duXfRo_STs2TB-dNiOfbJT2TeWpexvsnprmg06giJKM9ICqjidPMTaVO6mRh7LkXTNQS3u1QgS8w2jdxjpmcsIiQwr4oAnktDbx4NE_CZFKgwlU5_IQlPtBAfRSBKaMTrzMfl0gRBOQjpEeJGXlufP5zEAGisduCLxqRr_bh-iG3Jfi_h9eB_4MuWq-OcNFRe4FEKemWLw5TVuYCulBtCUKB7MB_dDDrdjRLHCs98Sl0kRkcwAmYlXrF8WMColFWGepl_hBT1IL_tbUXxlCRLWB4Aw7YYK842hts6arH2P4ZcFwDMjmbRkkBbPTvaah15J2u7TugX1eKL_ZSXNPDVFO5aLdQEjDrE6S9n6uRXmtsGPyVtwOWoCoF_kMJIPYplvwcWCXwrMEYUFZ6yPiefUGX4WTI9plk_J0FAHppCSQjTUqJwwfYAHKT3-SpAz7Df2Kow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اعلام العدو تحت بند سمح بالنشر: اصيب قائد اللواء 401، بجروح خطيرة إثر انفجار طائرة مسيّرة مفخخة اخترقت المنزل الذي كان متواجدًا فيه في جنوب لبنان. كما أُصيب معه أيضًا ضابط برتبة مقدم.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75757" target="_blank">📅 18:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الايرانية:
المفاوضات مستمرة عبر وسطاء باكستانيين. ما نريده في الأساس ليس مطالب، بل حقوقنا. قدمت الولايات المتحدة مطالب عديدة، لكن السؤال هو: لماذا ينبغي لإيران نقل يورانيومها المخصب إلى دولة أخرى؟ لم يكن أحد قلقًا بشأن برنامجنا النووي، والجميع يعلم أن برنامجنا النووي سلمي تمامًا.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75756" target="_blank">📅 18:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75755">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
‏
ترامب بشأن كوبا:
لن تتسامح أمريكا مع دولة مارقة تمارس عمليات عسكرية واستخباراتية وإرهابية أجنبية معادية على بعد تسعين ميلاً فقط منا.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75755" target="_blank">📅 18:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75754">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌟
نت بلوكس:
تُظهر المقاييس انقطاع خدمة الإنترنت في معظم أنحاء ‌العراق باستثناء الشمال لمدة ساعتين تقريبًا هذا الصباح. تُقدَّم هذه السياسة، المطبقة منذ سنوات، كوسيلة لوقف التسريب والغش في الامتحانات المدرسية، لكنها تؤثر بشكل غير متناسب على المستخدمين والشركات.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75754" target="_blank">📅 18:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75753">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jeh9_ABjZohB7Zh7zY01h2ySNkw7h64tQNHfNLWQ0x0yaQHaShGmDk-6IgL_BHHPEXyFRNbjkfgNi9o6ht-Vmln-A9OQSFmdY-Gwvzu5K1XGdZDHkrk3g0te14FcTev68rVn4V-jc2E8kI26LOYcDklXbPDPPiG7Tak_7L4anD29sY_6p-mPgPkR6lyqb5rGYnJZCDRSDkINngzmpAuzqUHj1MekcbN51-LoDnL7aac98Jzq1pBeiyaj7-3Um5qMp9LK1aNiQqUomPVUibGuNSA0aKGVuXMDFZDFfOmMh_sF5dXdSJB9BTAp0jcj5o_iBOYThFaa5acyKQwf7YZKaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسالة من مجاهدي المقاومة الإسلامية إلى سماحة الأمين العام لحزب الله الشيخ نعيم قاسم (حفظه الله):
بسم الله الرحمن الرحيم
سماحة الأمين العام حجة الإسلام والمسلمين المجاهد الشيخ نعيم قاسم حفظكم المولى
السلام عليكم ورحمة الله وبركاته
تلقّينا رسالتكم العزيزة وفيها أثر الوالد على أبنائه والقائد على جنوده والشيخ على مريديه.
نشكر لكم يا شيخنا الحبيب مشاعركم الصادقة ومودتكم الخالصة وعاطفتكم الصافية.
ونرد لكم التحية، بتحيّةٍ ملؤها إيمان وسنامها جهاد ومآلها نصر وشهادة.
كما نتوجّه بإجلالٍ وتعظيمٍ إلى أرواح الشهداء من إخوتنا المجاهدين وأهلنا الأوفياء، الذين أدهشوا العالم بصبرهم وثباتهم وصمودهم، وكانوا وما زالوا الحصن المنيع على الفتن والسند المتين في ذورة المحن، ظهر المقاومة في ميدان الدّفاع عن الوطن ضدّ الاحتلال الصّهيونيّ الغادر والهمجي.
أيها الأمين المفدى، إن أبناءك المجاهدين في المقاومة الإسلامية قد راهنوا على الله تعالى قبل حمل البنادق، وامتثلوا لأمره وتوكّلوا عليه ونزلوا سوح الوغى مسدّدين بالصّبر ومؤيّدين بالمدد من عنده، وهم في كل يوم يسطرون ملاحم التصدي الكربلائي ويلاحقون العدو بكافة أنواع أسلحتهم، يدمّرون دبّاباته ويحرّقون آلياته ويرعبون جنوده ويلقّنون جيشه دروساً ستُحفر في ذاكرته المصطنعة، ويبقون الوطن عصياً على القهر والإحتلال.
يا شيخنا، لقد فتحت قيادتكم الشّجاعة الطّريق أمام سلسلة من العمليات التي جعلت العدوّ منهكاً، يتهيّب الاستقرار فوق التّراب الجنوبيّ، قد أدمن النظر إلى السّماء، مترقّبا صلياتنا ومسيراتنا، واعتاد تنكيس رأسه في الأرض، مذعورًا من عبواتنا وكمائننا. عهدنا ما عهدتم إلينا به: سنبقيه على هذه الحال ولدينا مزيد؛ لن نهدأ ولن نستكين ولن تقر لنا عين حتى يرحل الاحتلال عن أرضنا مهزوماً خائباً، وبيننا وبينه أيامٌ لن يصبر على مدتها وسنصبر، لأننا أهل الأرض، وليالٍ مظلمة في عين المحتل أضأناها بذكر الله، وميدانٌ سيحصد منه أشلاء القتلى والجرحى، بعد أن زرعناه بالبارود والنار.
باسم حبات التّراب، باسم كل شهيد، وكل مجاهد في تشكيلات المقاومة المتأهبة على امتداد جبهة المواجهة، نجدد لكم الولاية والقسم والبيعة، بالاستمرار على هذا النّهج حفاظًا على العزّة والحرية والكرامة والإستقلال؛ فحياة الأوطان لا تُكتسب إلا بالتضحيات الحمراء، وشرف الجنوب يأبى أن يتحرّر إلاّ على أيدي المقاومين، ولن يخيب عليهم رهان إن شاء الله تعالى.
والسّلام عليكم ونصر الله وبركاته
أبناؤك مجاهدو المقاومة الاسلامية
الأربعاء 20-05-2026 م
03 ذو الحجّة 1447 هـ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75753" target="_blank">📅 18:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75752">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الاعلام السعودي يزعم: العمل جار بجدية على وضع اللمسات النهائية على نص اتفاق بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75752" target="_blank">📅 17:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الاعلام السعودي يزعم:
العمل جار بجدية على وضع اللمسات النهائية على نص اتفاق بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75751" target="_blank">📅 17:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75750">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏴‍☠️
اعلام العدو تحت بند
سمح بالنشر:
اصيب قائد اللواء 401، بجروح خطيرة إثر انفجار طائرة مسيّرة مفخخة اخترقت المنزل الذي كان متواجدًا فيه في جنوب لبنان. كما أُصيب معه أيضًا ضابط برتبة مقدم.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75750" target="_blank">📅 17:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75749">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🤺
🏴‍☠️
اعلام العدو:
حدث أمني في جنوب لبنان.. التفاصيل لاحقًا.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/75749" target="_blank">📅 17:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ed3da2b.mp4?token=Yjq_qN0C6fXE2W-8H9nnFk-nmEc-K-is9x2jRiL9BLqT7E4WeOAeqmCy_CfDpskMWqalGTtnlOSzgwVhrAAsLrSEvZ5H2vMjjxGWVbSxdkoGVpxx_4C-Y6KLkvJLVF81Vgvy_e6KFtahtfn1kaa70-Cd1Yp18HVPv99W1Oetgwpzxs3jcwiVjW5a0qku7CulqdFI4q1YtcLKzPubL6lDTSfyiHcSUqB3OcgiSThyFvE0I3egckMl-gdiK3uGJ2DL3rhOizg4dtLRIQDoUQqQd3-NNBDVeb7zmpucBaotyATv9OxvZ9hInKn_fAo7rkR4A1eULmZp_6gsr3aXyMcMgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ed3da2b.mp4?token=Yjq_qN0C6fXE2W-8H9nnFk-nmEc-K-is9x2jRiL9BLqT7E4WeOAeqmCy_CfDpskMWqalGTtnlOSzgwVhrAAsLrSEvZ5H2vMjjxGWVbSxdkoGVpxx_4C-Y6KLkvJLVF81Vgvy_e6KFtahtfn1kaa70-Cd1Yp18HVPv99W1Oetgwpzxs3jcwiVjW5a0qku7CulqdFI4q1YtcLKzPubL6lDTSfyiHcSUqB3OcgiSThyFvE0I3egckMl-gdiK3uGJ2DL3rhOizg4dtLRIQDoUQqQd3-NNBDVeb7zmpucBaotyATv9OxvZ9hInKn_fAo7rkR4A1eULmZp_6gsr3aXyMcMgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أوباما انسحب من أفغانستان.  علما ان بايدن من انسحب</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75748" target="_blank">📅 17:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f240d29220.mp4?token=oqHulFiR1jnDKP9xc-vrMFNyTgA9GYcPZQJMDGb_DOpg4ptCM-4ghxmwGRIQVgOz9q1LzadvZHtlY43anUBm9w--MOLBjNys6czd_A7PsnR6VeSs_zkb9O6FJKGaJcb2Ajl8DMrZ8VCawnSXn8wFc39DzjYdAQ80-tRAt7qrFEiijJH4LjpKyZcSKrQXxyOL218zmRjhvgqcyWpNj7D-B7Opiyr6lxyC-70jbedw9iuMecG2DpYU5dDWG_Pv_ye2ADm3m2yDpAm8LMMevIFvM3OKgYuvpUqxnM3yCQUynoRsvNeuEkBg4OUifNNyWYiZQo8SEzNP19iB9V9Azk0eJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f240d29220.mp4?token=oqHulFiR1jnDKP9xc-vrMFNyTgA9GYcPZQJMDGb_DOpg4ptCM-4ghxmwGRIQVgOz9q1LzadvZHtlY43anUBm9w--MOLBjNys6czd_A7PsnR6VeSs_zkb9O6FJKGaJcb2Ajl8DMrZ8VCawnSXn8wFc39DzjYdAQ80-tRAt7qrFEiijJH4LjpKyZcSKrQXxyOL218zmRjhvgqcyWpNj7D-B7Opiyr6lxyC-70jbedw9iuMecG2DpYU5dDWG_Pv_ye2ADm3m2yDpAm8LMMevIFvM3OKgYuvpUqxnM3yCQUynoRsvNeuEkBg4OUifNNyWYiZQo8SEzNP19iB9V9Azk0eJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: لو أن يسوع المسيح نزل وأحصى الأصوات، لكنت فزت في كاليفورنيا. لكنها انتخابات مزورة.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/75747" target="_blank">📅 17:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNn0bBZLKwYJzgaz82jrkzvdDPSlZtzSAjlCk6usPNWxd7iQNctbRzg8VADi5GsN9pLImgNurFrDsCK6TgJGuLA2W6MjVOxu8sbyb14t1u6f0OZD4BwZMPvprrC4vp4uNYG31oihwNkuLUj9A-nxmRj94Z1zENUQB5nkWYLrgYhHYR3P7mO2Vxv-BgJXBC33crYmx5KvNgZBvEw66aR3aPeiwc5ntDIwZ1BabS2TiLDRomi7D3mhSwTqeoFP_4CLusRTQ4Bae1EwHQJdyPameVMnsX113Q263OPcPN5S_4o-qQYKbTWKQ5PavqfALSq-40Rd9tl851qYCfxCYDeqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
وزير الخارجية السعودي:
نقدّر تجاوب ترامب بمنح المفاوضات فرصة للتوصل لاتفاق ونتطلع لأن تغتنم إيران الفرصة لتجنب التداعيات الخطيرة للتصعيد.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75746" target="_blank">📅 17:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامب: لسنا على عجلة من امرنا لفتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/75745" target="_blank">📅 17:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75744">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب: سنمنح ايران فرصة واحدة، أنا لست في عجلة من أمري.  إما أن نتوصل إلى اتفاق مع إيران أو سنقوم بأمور قاسية ونأمل ألا يحدث ذلك.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/75744" target="_blank">📅 17:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75743">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏ترامب: رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه  متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/75743" target="_blank">📅 17:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75742">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5677620f9.mp4?token=WoUKbSfmd1F77xpyq8s0K8-ZCYklQIRdj6ENynhlnxolAQx-L3bt2SYmBZdqci8ynemUSuB1ZfGgKdwzLrjre43m5dRjBAmMTRQmYnNjSWgWyNgyzPnp_eeE9te8KEMolCjH9Gvq9t7hAW6lY02uee881AYocCCIyT7o8lG-q5pWFkxknEjiTmUG2ULfUxJ2o-ZVXgSpRNqCfDfKRyLuj_gZrIDveVnd2cRKZmsoL8WxPJUP4TqAggVjAf19E5PxU2pRJeERK2JcdcQAKzkm-4zQZ6xDysI0uguKe2E0KX-feRj5qj_02ZOVObga8BQekD1Lmwvgh1KFpgAflInQZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5677620f9.mp4?token=WoUKbSfmd1F77xpyq8s0K8-ZCYklQIRdj6ENynhlnxolAQx-L3bt2SYmBZdqci8ynemUSuB1ZfGgKdwzLrjre43m5dRjBAmMTRQmYnNjSWgWyNgyzPnp_eeE9te8KEMolCjH9Gvq9t7hAW6lY02uee881AYocCCIyT7o8lG-q5pWFkxknEjiTmUG2ULfUxJ2o-ZVXgSpRNqCfDfKRyLuj_gZrIDveVnd2cRKZmsoL8WxPJUP4TqAggVjAf19E5PxU2pRJeERK2JcdcQAKzkm-4zQZ6xDysI0uguKe2E0KX-feRj5qj_02ZOVObga8BQekD1Lmwvgh1KFpgAflInQZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب:
رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه
متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75742" target="_blank">📅 17:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75741">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رئيس المعارضة في الكيان يائير لابيد: الهجوم الذي حدث اليوم قام به بن غفير لكن المسؤول عن هذا الهجوم الخطير هو رئيس الوزراء نتن ياهو الذي أدخل مجرماً مداناً إلى الحكومة، وكل من وافق على أن يكون شريكاً لشخص غير مسؤول بهذا الشكل</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/75741" target="_blank">📅 17:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75740">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">محمد باقر قاليباف: لا يزال العدو يأمل في استسلام الشعب الإيراني، ويعتقد خطأً أنه يستطيع إقناع إيران بالاستجابة بشكل إيجابي لجشع أمريكا من خلال مواصلة الحصار واستئناف الحرب. إن الضغوط الاقتصادية المتزايدة والحصار لن يجبرا إيران على الاستسلام</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75740" target="_blank">📅 17:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75739">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
‏رئيس البرلمان الإيراني محمد باقر قاليباف: التحركات الواضحة والخفية لـ"العدو" تُظهر أنهم يسعون إلى جولة جديدة من الحرب</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75739" target="_blank">📅 17:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75738">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
‏
رئيس البرلمان الإيراني محمد باقر قاليباف:
التحركات الواضحة والخفية لـ"العدو" تُظهر أنهم يسعون إلى جولة جديدة من الحرب</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/75738" target="_blank">📅 16:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75737">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPdhhv9jfyq0ngwgFa8qij3LgCOv7kOzup-mvjKWz9vDly00GOaWRPw5oRRXfG2Qf1-aR4eDFRhrU2s6jkEtczW2hPY6vhjFjIuVp5xjk28x0Gi3a16KeQb0v3VZrWohcRB_9H7omoIZPNBsEX6hQb1JsLtc6wKDzOcewX1DF2Sbw-5gk6T1Zla1WW9ctKCxgZPiakz_OJq7Rpp8XStX3Lyc4foWG3tXCkpqwJaeYEY7l0V7xB36ltFflx7AljlIhoq4fgE4LsDvI7IkQMIJVMSHq9ZJpLY4FcWgXD6ardzotT8V23DHNSwHoMo_MCz41DUXol8yROZLiqffGfPHMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن غفير يهاجم وزير الخارجية الصهيوني: هناك من في الحكومة لم يستوعبوا بعد كيفية التعامل مع مؤيدي الإرهاب. من المتوقع أن يدرك وزير الخارجية الإسرائيلي أن إسرائيل لم تعد دولةً تُعتمد عليها. أي شخص يأتي إلى أراضينا لدعم الإرهاب والتضامن مع حماس سيُختطف، ولن نتسامح…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75737" target="_blank">📅 16:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75736">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nevg-aI3EzlvZGRWDQydpClVDGcHvraw1UVV2vfvDBmtWIC0H6_wnWJVugTyjPA5o-jQQvPaNYQO2DNmdWmFD1Uz4BNxhCsLXY9Rtptsly4-NPEVXQ8j_PMGr1NsL55QGIO1rp96-HV7bRnTsFbMkzRjSFlLDX2g18dWE6jyguKRKmplZINxXCPzuqqu-1QYLC1z2gERhJgKafKHKUPGeRysshbv6T3WR91_fXNFldJUjZ6HpCPzmxQ-2DeQwPvLBDw7NY7YS-OIV3Z9_V_T9PB4vBrIc8_6nGbg5K1cEQBTRffWCfG0M3gU3ZfwToKWEzSg-KbOIN-WeQNqGNMYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الاعلان عن تشكيل تحالف سياسي في العراق تحت عنوان (تحالف البيان الوطني) يضم تحالف العقد وحركة سومريون ونواب اخرين.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/75736" target="_blank">📅 16:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75735">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixxXvKBOr8WWfp6BInyD2HYslrjmm-znDACdFEZ7mBKCyaq5xvcdkZEYiXkrgc7UaIxmrnDZVjd9_7ESJKWtXVG4-VHqUi8SDil51nknwizwT3EMUKxUaOOGQflrY4RfLZRYKmQtF4uSldS1HrcNKnM2rAnD8j4TKdDw0kHerDkCG7N5vqHDaV2mL4jUB7zGdkm6zFsUAYTsTc73PFxxT_8CCAx7B2u4StadjyLjiVQ6eIZ9H_76_pdvyZMcxqrrm-bJ_wnkm_gKoVy_-SyT1AYexVYXlllU7sKcCbwxrH3NCnEBCUZXpXJ2Oi01CYBtA9dM_KRvl21Urt06XDuScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
وزير الخارجية الصهيوني يهاجم بن غفير بعد ان كشف الوجه الحقيقي للكيان: لقد تسببتم عن علم في إلحاق الأذى بدولتنا في هذا العرض المشين - وليس للمرة الأولى. لقد أزلتم جهودا هائلة ومهنية وناجحة بذلها الكثير من الناس من جنود الجيش الإسرائيلي إلى موظفي وزارة الخارجية…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/75735" target="_blank">📅 16:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75734">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTs3oz9hcJfLDjgpSwgGmCZdaJQunFm3_5RKiDTE3Q0gQuRQAXf6Dadv0ymdkVx7vD5BkVD0_HXrPwk_73lxUt_vtG14LW8YKb8qmZnYClmuK5_VXhT5U6hpKkjp0fBQfBgeBNy0R9kKkvrlzVzU_cnkLwAKO2dclFngf7y-qe-3UHupwi8a2qaudUzGaE1bzEtSVjKMgoEsapEKUcDfWOKf2gjj3VCMW6c6sWj3s9YRfs5pNrXDq_woq3LV6Yit9tx1OoNCk6LYw205k7EnYd_zCVEMZ2QfhCvQ0qUh-7FqGyFU_T7uXyWiahGL50hmS5rX__RFs_3K8L34S4v2BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن غفير يقوم بجولة في ميناء أسدود ويشرف على اعتقال نشطاء أسطول الصمود ويقول: "أدعو نتنياهو أن يعطيني إياهم لفترة داخل السجون".</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75734" target="_blank">📅 16:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75733">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رئيسة وزراء إيطاليا ووزير خارجيتها: معاملة إسرائيل لنشطاء قافلة كسر الحصار غير مقبولة. نتوقع اعتذارا من إسرائيل بشأن معاملة نشطاء الأسطول</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75733" target="_blank">📅 15:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75732">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رئيسة وزراء إيطاليا ووزير خارجيتها: معاملة إسرائيل لنشطاء قافلة كسر الحصار غير مقبولة. نتوقع اعتذارا من إسرائيل بشأن معاملة نشطاء الأسطول</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75732" target="_blank">📅 15:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75731">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🤺
حزب الله:
شاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في موقع جل العلام على الحدود اللبنانيّة الجنوبيّة بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75731" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75730">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سوالف الگهوة
من منزل العامري ، طرح مبادرة اليوم تتضمن صلح وبناء الجدار المتصدع داخل الإطار التنسيقي في العراق..</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75730" target="_blank">📅 15:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c36a9108.mp4?token=PhfyvyCu-58SIYNe4r2-N6cDIFpVI35csDqbYN1-BcHg7_9IoWyc0aRiExaxSP8A5qQyE1uFglLckgE7_30lBv-BTqRFNDuGfsPSwI6da0OJyJcheYr0GfJPDZni67EvwgXkl6lqGHk56im4hIwJMrbw3NXdzC5-7zNKnE9iBaoqimMVhUoLg3mVAaRBn5srOCdZaQUZKsLj5lXEO0y79ydQl8osdA7Hq8hZza3HGN3Z6dMnMKmackXLsVSPw_M-1cG7h9hZsINNiZTCWLlPR1e-ddK4bOQ63eC6qGQrTfyaODF2S886F1upsz4lsQ27i5_6addJhMZizqJCK3JWVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c36a9108.mp4?token=PhfyvyCu-58SIYNe4r2-N6cDIFpVI35csDqbYN1-BcHg7_9IoWyc0aRiExaxSP8A5qQyE1uFglLckgE7_30lBv-BTqRFNDuGfsPSwI6da0OJyJcheYr0GfJPDZni67EvwgXkl6lqGHk56im4hIwJMrbw3NXdzC5-7zNKnE9iBaoqimMVhUoLg3mVAaRBn5srOCdZaQUZKsLj5lXEO0y79ydQl8osdA7Hq8hZza3HGN3Z6dMnMKmackXLsVSPw_M-1cG7h9hZsINNiZTCWLlPR1e-ddK4bOQ63eC6qGQrTfyaODF2S886F1upsz4lsQ27i5_6addJhMZizqJCK3JWVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الكيان:
رصدت قواتنا أجهزة مراقبة تابعة لحزب الله في جنوب لبنان داخل مبنى كان حزب الله يستخدمها لمراقبة قواتنا وتوجيه العمليات.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75729" target="_blank">📅 15:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75727">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزارة خارجية دويلة الامارات:
نشدد على ضرورة التزام حكومة جمهورية العراق بمنع كافة الأعمال العدائية الصادرة من أراضيها بشكل عاجل دون قيد أو شرط وضرورة التعامل مع تلك التهديدات بشكل عاجل وفوري ومسؤول بما ينسجم مع القوانين والمواثيق الدولية والإقليمية ذات الصلة. كما نؤكد على أهمية اضطلاع العراق بدوره في ترسيخ الأمن والاستقرار في المنطقة، بما يحفظ سيادته ويعزز مكانته كشريك فاعل ومسؤول في محيطة الإقليمي.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75727" target="_blank">📅 14:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75726">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6bfe77ce.mp4?token=a433k4h0Y1HN_XAjStAP6eIp0j6cejuKumUdAkgeQa1XYbWMTrBAgJ_ffCYFng1RVJ50Jse154qdMV5WtQyeF8p-BfKN3cfbItevYCY8R98VrMlYuWV60QdgMWDlhVp2DUJsl5yjvYSHjat0EqFBJuhO7z1WZQLw3Q9BM-cJuj1XxetC5bSboIwjAWfeFEj6ui74JgLWlSyxDjVEMZcCgvXAbSJ3kIly5X8yULj3UCR3FLbSamXUFJFtZYU4kDtwT5k4xNFFMgu9EomKn50oMp02xvTU_m4FdVGXFfMtrswvxknLKsYK_vI6yE5hanWXUGHPTu3rbnEHuXDqWBat2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6bfe77ce.mp4?token=a433k4h0Y1HN_XAjStAP6eIp0j6cejuKumUdAkgeQa1XYbWMTrBAgJ_ffCYFng1RVJ50Jse154qdMV5WtQyeF8p-BfKN3cfbItevYCY8R98VrMlYuWV60QdgMWDlhVp2DUJsl5yjvYSHjat0EqFBJuhO7z1WZQLw3Q9BM-cJuj1XxetC5bSboIwjAWfeFEj6ui74JgLWlSyxDjVEMZcCgvXAbSJ3kIly5X8yULj3UCR3FLbSamXUFJFtZYU4kDtwT5k4xNFFMgu9EomKn50oMp02xvTU_m4FdVGXFfMtrswvxknLKsYK_vI6yE5hanWXUGHPTu3rbnEHuXDqWBat2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بن غفير يقوم بجولة في ميناء أسدود ويشرف على اعتقال نشطاء أسطول الصمود ويقول: "أدعو نتنياهو أن يعطيني إياهم لفترة داخل السجون".</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75726" target="_blank">📅 14:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75725">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
رسالة قائد الثورة الإسلامية السيد مجتبى الخامنئي بمناسبة الذكرى الثانية لاستشهاد الشهيد رئیسي وتكريم شهداء الخدمة
بسم الله الرحمن الرحيم،
إنّ إحياء ذكرى شهداء «رحلة أيّار» (حادثة تحطّم المروحيّة) وفي مقدّمتهم رئيس الجمهورية الشهيد حجّة الإسلام والمسلمين رئيسي، يُعيد إلى الذاكرة استشهاد قوافل خدّام الشعب في جمهورية إيران الإسلامية، من مطهري وبهشتي ورجائي وباهنر، إلى رئيسي وآل هاشم وأمير عبداللهيان ولاريجاني؛ مئات الشخصيات البارزة من الذين تربّوا في مدرسة الخميني الكبير والخامنئي العزيز (أعلى الله مقامهما الشريف)،  وزيّنوا سجلّ الخدمة المخلصة والجهادية لمسؤولي الجمهورية الإسلامية بتوقيعهم المضمخ بالدماء.
ويمكن للمرء أن يعدّ  من الميزات البارزة للشهيد رئيسي: تحمّل المسؤولية، وإفساح المجال للشباب، والاهتمام بالعدالة، والدبلوماسية الفاعلة والنافعة، ولا سيما الطابع الشعبي الذي اتّسم به؛ وقد كانت هذه الخصائص تبعث الطمأنينة في نفوس أصدقاء إيران، ومنهم مجاهدو جبهة المقاومة القوية وكثير من الحريصين على النظام. وكلّ ذلك كان ممتزجًا، بالطبع، بنفحة روحانية متجذّرة في أعماق نفسه.
وأما بشأن العلاقة بين المسؤولين والشعب، فإنّ الخصائص الإيجابية المؤثّرة كانت تؤدي إلى تقدير متبادل. وهكذا جرت مراسم تشييعه إلى جوار مولاه ومخدومه الإمام أبي الحسن الرضا صلوات الله وسلامه عليه، بمشهد مهيب قلّ نظيره. وقد شكّلت الفترة غير المكتملة من رئاسته للجمهورية معيارًا لقياس حجم الجهد والحرص على الشعب والبلاد، مع الحفاظ على استقلالها.
واليوم نقف أمام الملاحم التي سطّرها الشعب الإيراني في مقاومته التاريخية الفريدة بوجه جيشين إرهابيين عالميين. وهذا الأمر يزيد من أعباء التكليف الملقى على عاتق مسؤولي الجمهورية الإسلامية - من القيادة ورؤساء السلطات إلى جميع مستويات الإدارية ـ أكثر من أيّ وقت مضى. واليوم، فإنّ شكر نعمة الانسجام بين الشعب والحكومة وسائر أجهزة الجمهورية الإسلامية، يكمن في تعزيز دوافع المسؤولين ومضاعفة خدمتهم وجهادهم، والعمل على حلّ مشكلات البلاد ، ولا سيّما في المجالين الاقتصادي والمعيشي، والحضور الميداني والمباشر، وتعريف دور جادّ للشعب الناهض بمسار تقدّم البلاد والتحرك بأمل نحو المستقبل المشرق.
رحمة الله ورضوانه على شهداء طريق الخدمة، ولتكن النصرة الإلهية ودعاء سيّدنا عجل الله تعالى فرجه الشريف سندًا لخدّام الشعب الإيراني المسلم.
السيد مجتبى الحسيني الخامنئي
20 أيار/مايو 2026</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75725" target="_blank">📅 14:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75724">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوي انفجارات في محافظة السويداء جنوب سوريا</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75724" target="_blank">📅 13:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">إعلام إيراني عن مصدر بإسلام آباد: وزير الداخلية الباكستاني توجه إلى طهران للقاء مسؤولين هناك</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75723" target="_blank">📅 12:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75722">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏الجيش الأردني يدعي إسقاط مسيرة في جرش دخلت الأجواء الأردنية</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75722" target="_blank">📅 12:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">إعلام خليجي عن ‏مصدر دبلوماسي: تضارب المواقف بين إيران وباكستان حول قنوات التفاوض ومكان المحادثات</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75721" target="_blank">📅 12:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇹
إيطاليا الدولة الـ19 التي تشغل طائرة التزود بالوقود A330.
وقعت إيطاليا صفقة بقيمة 1.4 مليار يورو مع شركة "إيرباص" لشراء ست طائرات تزود بالوقود من طراز A330 MRTT - مما يؤدي إلى إلغاء طلبية شركة "بوينج" لطائرة KC-46 Pegasus، التي اختارتها روما في الأصل في عام 2022 قبل إلغائها فجأة في عام 2024.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75720" target="_blank">📅 12:19 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
