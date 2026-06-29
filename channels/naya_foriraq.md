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
<img src="https://cdn4.telesco.pe/file/LUASdlT7F9V-VpKjga_7eOaoUVoFFFaaLe2DvMB0M16pNZPreWf575JDsKXpWN4qF_T8pCpPLzP0U6oAVaJMd7SX2kqxZjMwGraFm9rcBhqXyGCT_UxDbB_LU8Bud9wX-VBlUGwAAfCq2RdXrqvQySRJSODfMD8PIGFG1eSftmXbV2nClofwJRtYi7_s6Q4POhHoZYC7uDs9I-b7CqUYT2Bbu3FEi0pquMu8eHplRiEp_iGumVUTOufzMBH0gIK7kDQrNunfI1zqgwiKSCMQVJztsa6FMa2Zs9nV8iuvC2ki7rgJmGnvWNZYpQnJPvI07x8OUV0kPqaS3byK2XKoWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 22:51:11</div>
<hr>

<div class="tg-post" id="msg-80345">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔻
المحكمة الجنائية الدولية تفتح تحقيقًا مع مسؤولين كبار من الإمارات العربية المتحدة ودول مجاورة، بتهمة المساعدة والتحريض على ارتكاب جرائم وحشية في إقليم دارفور السوداني.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/naya_foriraq/80345" target="_blank">📅 22:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80343">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔻
الإطار التنسيقي يدعو جماهيره إلى المشاركة الواسعة في تشييع الشهيد علي الخامنئي في الأراضي العراقية</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/naya_foriraq/80343" target="_blank">📅 22:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
مسؤول أمريكي:
دورنا يشمل استخدام قوات أمريكية على الأرض في لبنان وإسرائيل
عون وينك السيادة عم تبكي
😫</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/naya_foriraq/80342" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80338">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtcvaVL9DDn4HjaQRSnAmEMdZrRR7ULGGGjQa-7EJEbzvwyf_O7DSFoU4vlcM-C4OcACvkIMPW_wg68v1KebE1TIAcpL5FGrdcO3XT3gPO2nXznZgnfYAhIlhMeMQDbS0V4ZURnY2ajSRXzN9nO0kSNrBscBbH73gJtNplVlD6IBKiuhgSJMRYIW6VmP8in4iy3TkGA_s0DlS4zqBkWhy7VQpIVgUVhKIsLs7ujAL8FJCKBAMP3IcCpomHdy627mg5x6sjwa4-QXom9BVM2k_Zh247H4esb_I819pvC6aumO1Gcohn5NABgoLiBtlsMGUq-atVx62gLVmTHYnUgpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-oVArYeBarLigi1_AqN0si3Z_Ebmyiodn7qpXdJbiu2rgZ5Rel_oYIpeTuUP18zHSRQpQt6B2Y0ELBF3YkNicj17_lQfNcM5-sOT-y48IZeIUNpowmDmef7-2y8tZsScPbcgIqgSsq_hFdBAk1PIQxFrngrtCT30OauZ_dhofxf-MF4oKTkBcj-Is1CqbfBh9B1SE5HDPPUAjz0x6yVBX3V6iT_Pq2cRovwnZ0v-BgHafb-He5ge0gbuJhaXSF7DBYQ4PtH0SBpwHyPp2ASYNAHfZvzy2Wa-ET7lQfpvLCB32G7bt6Fqfh3D_9591OY3oDB2qd3ydJ7YcL6TYE0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUG_Av_A_fOu0NUOHJZA8clSDXWw0y2kknf169krx84zuW8dUbjID32P7JM7z2WTQE5-NpAJBH_fAgunG8yi5jXGhFAyjeEIp9KTYlW6KL6ern7kMPgH5qU4gHjVvuVeSy9cidvsT56OjI6SEf52Ep8QnzbqBXSxfGd_ZWF725-y37qHEZuftMc7cCI_MI8AFbQviGTBVtDuxxmSbLwd1IaaSohlCjdz_8n9SBXhYvWMyQeU9TBJ6ig2WtVZfv36bez0cORIGIAaGNkI_IxD7Wfby3-9RUiXX-jcXWg-6EpphuSmqRSB0UWXKMruCnCRaeU0lWAvnd06eC27DiG3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5768GxrEkr-z-k_UDuZ5OuXQmztnYUh9Dni4LivSESdfCzoACfHmdR31D60WEmKxsxZPjH9Z8aB9MNBPAZyTiLcuVaw6UOweHwKsQIZIChU0oFrvc7e86okE330CxkLU-417KjdROQVdIZmN2q6uyqRx6-U5YjNwaEHofAndQHH-jPvTCVsceHIxevPG16JaGgyS8Ihvp9lfb0doNjW--oyqqv5iAfADGtphddFblStekhc2E4cbjRs2LVbBcXATHo_nPHubHnUXrkYeyXUuajjF01HIeSRUkKePEWOH1SyEgDmWlGfgX7bo5v3j_Jz24z_3Ru0HhoO1Or6z4Qu1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
مجلس القضاء الأعلى: التحقيقات مع وكيل وزير النفط لشؤون التوزيع تسفر عن ضبط 11 مليون دولار و4 مليارات دينار</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/naya_foriraq/80338" target="_blank">📅 22:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
🔻
مجلس القضاء الأعلى:
التحقيقات مع وكيل وزير النفط لشؤون التوزيع تسفر عن ضبط 11 مليون دولار و4 مليارات دينار</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/naya_foriraq/80337" target="_blank">📅 22:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80336">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية إسماعيل بقائي:  وفد خبراء إيراني يتوجه إلى الدوحة لمتابعة تنفيذ التفاهمات.  زيارة الممثلين الأمريكيين إلى قطر لا علاقة لها بزيارة الوفد الإيراني.  لن نعقد أي اجتماعات تفاوضية على أي مستوى مع الجانب الأمريكي في الأيام المقبلة.…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/naya_foriraq/80336" target="_blank">📅 22:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80335">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a3817a74.mp4?token=SUsb6bbUOApoacbTImXxIJLI8EwmEi_kvw_wF6KQore3GVln6hp3PS9N4qzPnhUgQIvTZP959jx59htbyXWKLwc_xXLlyyzX_fg2Z6pj9dWKslm2VoibRMZlPq6719yigaWlUENe5RvMBbAuVrlCdyP_sO8OEVy7L_JIOT2g7qJcTY7d3caw-eMLJGVEuUE1xBpqhVtmtoYR9xqulRpjkXjRoSIV4sxdtdMn17VuxCE3e0XHhzgP-R8jnVZRo_KVQ7zym2EdOaviowANBrkNIhylLWnhOmSgP8-CNpjOVlEQsPhvGonHL52tV-z2HFg6xQOZK97BflNTQLU6Nfv_Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a3817a74.mp4?token=SUsb6bbUOApoacbTImXxIJLI8EwmEi_kvw_wF6KQore3GVln6hp3PS9N4qzPnhUgQIvTZP959jx59htbyXWKLwc_xXLlyyzX_fg2Z6pj9dWKslm2VoibRMZlPq6719yigaWlUENe5RvMBbAuVrlCdyP_sO8OEVy7L_JIOT2g7qJcTY7d3caw-eMLJGVEuUE1xBpqhVtmtoYR9xqulRpjkXjRoSIV4sxdtdMn17VuxCE3e0XHhzgP-R8jnVZRo_KVQ7zym2EdOaviowANBrkNIhylLWnhOmSgP8-CNpjOVlEQsPhvGonHL52tV-z2HFg6xQOZK97BflNTQLU6Nfv_Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مروحي يجوب سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/naya_foriraq/80335" target="_blank">📅 21:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80334">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭐️
هجوم إرهابي يستهدف عجلة في مدينة سراوان بمحافظة بلوشستان الإيرانية ؛ إستشهاد شخص وإصابة أخر كحصيلة أولية.</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/80334" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80333">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">البيت الأبيض: ويتكوف وكوشنر سيحضران في اجتماع الدوحة.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/80333" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80332">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnl733bVDhXZFdH43FFPq9p_kCI2SP2QYiHjj_nc39SzbOuzOMwjpjDhVrnwI0YfgZk7fQesB-nPbreN5gkMs5yCpiqhgIoToQOaOuO0BxoEPhINU9kygM_anlZfBcSJZ02zdJt8Ng3VW8UNo2xXb9LPv7PFdLcVRYt5aDi8aN5HL4DSF2vzMcpkWgAPW7WCc6pI48wKs_a83ztgDyb7RbKCeimsHeB2AFvmXjRaM1-DzvLQib5-1gkrAPat4cjUakMdJmmyG3PQUHwPCwtIUMy8_McwPaIO9Rm35eVZLmkDroxfvyeFGHH4Nxk46BUn09Rn7c6MJe0oQgixLR6VGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
قيادة الحشد تبحث الاستعدادات للأربعينية ومراسم تشييع السيد الشهيد الخامنئي.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80332" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80331">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تحليق طيران مروحي إسرائيلي بأجواء عدة مناطق في حوض اليرموك.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80331" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اعلام العدو: تم تفجير عبوة ناسفة استهدفت مقر القيادة الميداني لنائب قائد لواء الكوماندوز في جنوب لبنان. هناك مصابان من جنود الاحتياط في الوحدة. أحدهما في حالة خطيرة، والآخر في حالة متوسطة، وقد جرى إجلاؤهما بواسطة مروحية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80330" target="_blank">📅 20:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية تحذر فرانسا:
إيران وحدها ستتولى عملية إزالة الألغام من مضيق هرمز بحسب مذكرة التفاهم.
لن تشاركنا أي دولة في نزع ألغام مضيق هرمز ولن نسمح بذلك من حيث المبدأ.
الوضع في مضيق هرمز حساس ومعقد وننصح فرنسا بشدة بعدم تعقيده باستفزازاتها.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80329" target="_blank">📅 20:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80328">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزير الخارجية العراقي فؤاد حسين يلتقي الارهابي ابو محمد الجولاني</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/80328" target="_blank">📅 20:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
🇮🇷
مسؤول أمريكي:
أوضحنا لإيران أننا لن نفرج عن أموالها المجمدة إلا إذا تحقق تقدم في الملف النووي.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/80327" target="_blank">📅 19:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndWeowgaHO_7XA2b5ho0GpOflW-lQAb5B16_xSCefdchjoYARF2Voo4QRo9On2T4pbuyND6n0ICvJ9zxeeR0i2ycvxhJAGCABWs5-oMM_rsf0MNq5CY1ZFHwH9SdCP9Z3PwVUsZSPMlQSf3A9BnQqHxL0Smt0xYdhnIjyDdvF1s7EqVsiM-sHzV9RD3Uk7r2LBx760Yt8xSC1HyOa-errel48fvuC0Br32a1hl0FAHvHZsbzQBhzD8EfwiZ7Wwhfq4bOlBzmMF7oS6dimkoeKzC8WeLLQoB_e6nLceTCUzgoeO1ihkmX8ufY7-IW8_ZqZ_ozxn4Tla0joId5xLyeFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب:  «انتصارٌ كبيرٌ قبل لحظاتٍ في المحكمة العليا، في قضية سلوتر، حيث تمّ تأكيد سلطة الرئيس في بلادنا لعزل مسؤولي السلطة التنفيذية والمعينين في الوكالات، أو الممثلين، بموجب المادة الثانية. لقد سعى رؤساء الولايات المتحدة إلى هذا القرار منذ زمنٍ طويل، ويعود…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/80326" target="_blank">📅 18:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الاسرائيلي:
نتجهز لمعركة جديدة مع إيران في اي لحظة يمكن ان تحدث ولن ننسحب من لبنان.
اندلاع الحرب مجددا مع إيران قد يحصل إذا قرر ترمب أن المفاوضات استنفدت أو أن تهاجم إيران إسرائيل.
معادلة هجوم حزب الله على مستوطنات الشمال تساوي الهجوم في الضاحية لا تزال قائمة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80325" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXvhifz-DJIwMPg5hjPSzHMppWeD623HDJWQjvEIXiIeSqPUtlx8qkxN2iMpQNH0RG7G52EA08HUzVegIocdSi9I0tpDaOwCaZQkWthkYaHOjRdxatHAzleJMvbxUbFuANPSA2AkKNjxzpNVPOeWhaQp8-PjyFdjOx3xhs1rHMYo90a7WhTK87yf0EJn0euCHpqDyhTckxLeF1-jYV7yuUfTGtzjaZWVFnfNgIzaWLhuouwlxTnhPCfstIi2Pms8btsS6rVPpc3PiT9CervrwgQDzB6l40rQTuh_wN3qrZpCVI115o3RF19Aqm-mMiJG9DHVBhQKxjpJrhrwHis3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
«انتصارٌ كبيرٌ قبل لحظاتٍ في المحكمة العليا، في قضية سلوتر، حيث تمّ تأكيد سلطة الرئيس في بلادنا لعزل مسؤولي السلطة التنفيذية والمعينين في الوكالات، أو الممثلين، بموجب المادة الثانية. لقد سعى رؤساء الولايات المتحدة إلى هذا القرار منذ زمنٍ طويل، ويعود تاريخه إلى ثلاثينيات القرن الماضي. إنه لشرفٌ عظيمٌ لي أن أكون الرئيس الحالي الذي حقق هذا الحكم التاريخي وغير المسبوق، وهو أحد أهم الأحكام التي صدرت على الإطلاق فيما يتعلق بصلاحيات الرئيس. شكرًا لكم على اهتمامكم بهذا الأمر!»</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80324" target="_blank">📅 18:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قد يغرد …</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80323" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
وزارة المواصلات القطرية:
حرصا على السلامة العامة، تهيب وزارة المواصلات بجميع ملاك ومستخدمي الوسائط البحرية، بما في ذلك قوارب النزهة، وقوارب الصيد، والدراجات المائية، وسائر الوسائط البحرية المماثلة، التوقف مؤقتا عن الإبحار وممارسة الأنشطة البحرية، اعتبارا من تاريخ صدور هذا التعميم وحتى إشعار آخر.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/80322" target="_blank">📅 17:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
العثور على جندي بالجيش الإسرائيلي مقتولاً في وسط البلاد.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/80321" target="_blank">📅 17:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزارة التربية العراقية تعلن استرداد أكثر من 73 مليون دينار لخزينة الدولة في صلاح الدين بعد متابعة دقيقة لملفات التقاطع الوظيفي</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80320" target="_blank">📅 17:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رئيس الوزراء العراقي:
يوم 30 أيلول المقبل سيشهد خروج قوات التحالف بشكل كلي.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80319" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌟
احسان العوادي رئيس اللجنة العليا لتنسيق مراسم تشييع قائد الثورة الإسلامية الشهيد في العراق:  لسماحة آية الله العظمى الإمام الخامنئي (قدس الله نفسه الزكية) مكانة رفيعة ومتميزة وقدم هذا القائد العظيم خدمات خالدة لأمن العراق وعزّته وللعالم الإسلامي، أنّ إقامة…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80318" target="_blank">📅 17:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌟
احسان العوادي
رئيس اللجنة العليا لتنسيق مراسم تشييع قائد الثورة الإسلامية الشهيد في العراق:
لسماحة آية الله العظمى الإمام الخامنئي (قدس الله نفسه الزكية) مكانة رفيعة ومتميزة وقدم هذا القائد العظيم خدمات خالدة لأمن العراق وعزّته وللعالم الإسلامي، أنّ إقامة مراسم تشييع سماحته في العراق والعتبات المقدسة تمثّل شرفًا تاريخيًا للشعب العراقي، أنّ الحكومة والشعب العراقيين لن يدّخرا أي جهد لإقامة مراسم تليق بهذه المناسبة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80317" target="_blank">📅 17:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80316">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏وزير الحرب الصهيوني: الجيش اللبناني لن يتحول فجأة إلى أسود تهاجم حزب الله.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80316" target="_blank">📅 17:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80315">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0C-w0qQnSL2-29exCdmz7pqqMq1AzsaUnrBuej9vJHoSoUCwql2rkP_EXnTRE7yDoJOc3Sb3DCIls8HAuDwVph6dlvFakkaHF3lKqVgiMQ1-l6u9yjUWwzWJkB0yBB1PeM8Zn7eROLucJT3FvU5Vff683MNRZjxqG1KSPOXJjV6Af6_R8UfiduWvPi0j5bRXDB6KjsMoyFKzUvqupcbGnbkEAKbM3zipXGLI_OL0bZJI8n1vQG_uS8MLDbxKgUAv8YSkT6JvAC-YNPRQe1B8N_s8aPapqR-ByyKBGGg8Hrm-Az4SFfMm-quuaZ0tWcQAfGI0CZHCgeChme68-kT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزير الخارجية العراقي فؤاد حسين يلتقي الارهابي ابو محمد الجولاني</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80315" target="_blank">📅 16:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80314">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏وزير الحرب الصهيوني: حزب الله عزز وجوده في الجنوب بسبب ضغط ترمب على نتنياهو</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80314" target="_blank">📅 16:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80313">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏
وزير الحرب الصهيوني:
حزب الله عزز وجوده في الجنوب بسبب ضغط ترمب على نتنياهو</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80313" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80312">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/760337d8fc.mp4?token=gSt8guwwBpUERGboDqZ72n-IOhFttOl4JaMpvtq60xmWqP2hB4DnKgKu46iSR6LrYwcyfL5bkEqLqYfYVt1fNrMErUWj2JbhWT1bpc3Xl4-lDBQ6fad8-A4PsJw8yJhlVhQNhLBwNwDOFoRIkkSUdjbRbb13Q93N5FoREaQEK1sQLvPY-OI8syvqouwKcX7R6Y0rm_13K1uKjXHzargr6yWU-AzjN6DXAey1H1s6lu8VaviQWkNd7lKrFGEI-56kFD5Ap5h2uccoGe7_PM6lyklogB14Zy6JLK0Fj0z0nKK2vtulOZDwmp1CICHJbb-3wDzaHB9phimSi8FEqlnD1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/760337d8fc.mp4?token=gSt8guwwBpUERGboDqZ72n-IOhFttOl4JaMpvtq60xmWqP2hB4DnKgKu46iSR6LrYwcyfL5bkEqLqYfYVt1fNrMErUWj2JbhWT1bpc3Xl4-lDBQ6fad8-A4PsJw8yJhlVhQNhLBwNwDOFoRIkkSUdjbRbb13Q93N5FoREaQEK1sQLvPY-OI8syvqouwKcX7R6Y0rm_13K1uKjXHzargr6yWU-AzjN6DXAey1H1s6lu8VaviQWkNd7lKrFGEI-56kFD5Ap5h2uccoGe7_PM6lyklogB14Zy6JLK0Fj0z0nKK2vtulOZDwmp1CICHJbb-3wDzaHB9phimSi8FEqlnD1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تقوم بهدم جميع منازل قرية المزرعة الشيعية بريف حمص بالدبابات والجرافات وتوجه سكان القرية بالذهاب إلى إيران أو الضاحية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80312" target="_blank">📅 16:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80311">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
🇮🇷
وزارة الخارجية العمانية:
عقدت اللجنة المشتركة العمانية الإيرانية اجتماعها الأول في مسقط بشأن مضيق هرمز لتبادل وجهات النظر حول إدارة المضيق مستقبلاً والمسائل ذات الصلة.
ناقش الجانبان سبل تعزيز التنسيق بشأن القضايا المتعلقة بمضيق هرمز بما يتوافق مع المصالح المشتركة للبلدين وسيادتهما، مؤكدين التزامهما بالقانون الدولي، واستكشاف أطر التعاون في مجالات الملاحة والخدمات البحرية، انطلاقاً من كونهما دولتين تتشاركان المضيق، وفي ضوء التفاهمات الثنائية والدولية القائمة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80311" target="_blank">📅 16:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80310">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
زعيم المعارضة الصهيونية لابيد:
لن يشكل نتن ياهو حكومات في إسرائيل بعد الآن.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80310" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80309">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34c356325e.mp4?token=DBzOwLpK3DLLp07bBvpsVI3dsZXpJjcF6Zt_WHrow3oHh48GjXmRS9OmlnYmI_rdSF0PLXv7H0W8Zauh7qV9H_eRfr3_gOZyxOFraXJlmVqhQZbC-qzFxWWoOvHTIPo4XbuJgJf76pLCW175SqMJ-eJ2HGJrp2XHqDmVETzIQNKHVG9tJtlIDJJiKwH5y7XuWCL5nqY6kHNkWOOOBi5Nwmi-G23I4U1f8a_Lj-zpj9as9Cr5Set16rggPUrmGbqKvEYYBCS8xgrU9RzU5FvLj-1BRUJlbuDfEKl6Mh0Rbbsc-UUnX8LGqBMI_IuFsDs7K44StyW0rYlFNNVZ7JJvfo7s3y08k9VWKId6ZcyXKMZIZhM_X3hR7gIzOnd97NI6Hee7z-xR5R2iwhDaoU6LMD_VESLPYXKKN-IqqLt7mvgWqP08Ix0xHYu-oLBO2SW3yWGkMm8H9pCy490i-frdU1nuOFewruJy76tqa0IQcPMJHak9dd9u5nriXRN2hazvNbUwxNqS8OOmRDxXE-PsPfIk7xnEENgp5VqjR_6vuuaUQt-uY_4X9hiESAYeRoKSHjfPYOmJzqyo7UCb7SQCIsxKIw0yb692q4I1EzdZFArIJYxM9NqyE968SU_aIXEkt5n7LerGWrOV0DypDlM3X_bJsV4S_tp_LZS_L3EAI6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34c356325e.mp4?token=DBzOwLpK3DLLp07bBvpsVI3dsZXpJjcF6Zt_WHrow3oHh48GjXmRS9OmlnYmI_rdSF0PLXv7H0W8Zauh7qV9H_eRfr3_gOZyxOFraXJlmVqhQZbC-qzFxWWoOvHTIPo4XbuJgJf76pLCW175SqMJ-eJ2HGJrp2XHqDmVETzIQNKHVG9tJtlIDJJiKwH5y7XuWCL5nqY6kHNkWOOOBi5Nwmi-G23I4U1f8a_Lj-zpj9as9Cr5Set16rggPUrmGbqKvEYYBCS8xgrU9RzU5FvLj-1BRUJlbuDfEKl6Mh0Rbbsc-UUnX8LGqBMI_IuFsDs7K44StyW0rYlFNNVZ7JJvfo7s3y08k9VWKId6ZcyXKMZIZhM_X3hR7gIzOnd97NI6Hee7z-xR5R2iwhDaoU6LMD_VESLPYXKKN-IqqLt7mvgWqP08Ix0xHYu-oLBO2SW3yWGkMm8H9pCy490i-frdU1nuOFewruJy76tqa0IQcPMJHak9dd9u5nriXRN2hazvNbUwxNqS8OOmRDxXE-PsPfIk7xnEENgp5VqjR_6vuuaUQt-uY_4X9hiESAYeRoKSHjfPYOmJzqyo7UCb7SQCIsxKIw0yb692q4I1EzdZFArIJYxM9NqyE968SU_aIXEkt5n7LerGWrOV0DypDlM3X_bJsV4S_tp_LZS_L3EAI6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المحلل البحريني جعفر سلمان المقرب من العائلة الحاكمة الذي كان وقد وصف العراق بـ"جمهورية موز" يقول في لقاء انه لولا الامريكان لكان الخليج لقمة سائغة امام الجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80309" target="_blank">📅 16:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هيئة النزاهة العراقية: السجن لمدير عام الهيئة العامة للضرائب الأسبق وزوجته عن جريمة غسل الأموال. الحكم تضمن تغريمهما أكثر من (32) مليار دينار ومصادرة عقارات وأموال داخل العراق وخارجها ومصادرة (22) عقاراً في بغداد وتركيا باسم المدانة وبدلات إيجارها ومخشلات ذهبية عائدة لها ومصادرة الأموال المودعة في البنوك التركية والكويتية العائدة للمدانة</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80308" target="_blank">📅 16:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHLNLpIk9SpYLrOdQqHkGKM72GdOiQoCqCo9wzfT6AunRQuN3ogRSy97DUrY7mo6oMgJyCRu4Z86xQOxQZzywKPF-rKURC6a2uZaUadD69juett0CVt03uYTYm7P1HzsvE2fnrdI3L6DLfuUnodlw9wgabko3-6ZiVV_pLLR_XPbON7st3HdDutI3imhZ9B40ypalsrKxwGImFgpFLqmdztbUuCUatJn9FzbC8CssVBJp0ctOOBxIOxVBwj0KJaxWKwXHgH8AKIfHpvhDTMbrIa8l6FFHRcK_bXIAWBlwU5GndjOKLLIpoxV0TqhuYu7ZOiMkMbl-CdK0GmlGQBzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-TLfnrQLDB4G8sulIFmd1cTtcwCzELdcABAihwXPK_raVbhuPAZhM1MB7LJfqmFb4aJjwij-1Y2Gdw0UHt0yUdmQsEUo02LTyxlZJVNp0yFbJyjuSksegynzoCOyAypN7mKgwlfch-hls9CNwOHDliLYHvGBiekL2uHSl5XFllyZ17tGQSsVE5nQZ_slllAz15eYGJsIXU2gD1caC1JBZm1O0kKw_5sPllcBr4MGM0-gPx7ONiY6ss14Pr_P1mItefHKFetTHVQbe6JIe_g23HbdkdHvzbh55Osd430uk6I7OwXcQid46Pj4DahGQm6wKmZqyqPELk9JQOZda42_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندلاع حريق داخل جامعة الانبار غربي العراق وفرق الدفاع المدني تستنفر</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80306" target="_blank">📅 16:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قوة امنية من بغداد تصل محافظة ذي قار للبحث عن رئيس لجنة توزيع الأراضي في المحافظة بعد ان وزع 1500 قطعة ارض مقابل اموال ثم ولاذ بالفرار</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80305" target="_blank">📅 15:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رئيس الوزراء العراقي: نسعى إلى آلية تقسيم مُنصفة ولا تجحف حق العراق والعراقيين في منظمة أوبك</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80304" target="_blank">📅 15:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">البيت الأبيض:
ويتكوف وكوشنر سيحضران في اجتماع الدوحة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80303" target="_blank">📅 15:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اعلام العدو: حزب الله استهدف مقر بداخله كبار ضباط الجيش الإسرائيلي في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80302" target="_blank">📅 15:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: حدث امني في جنوب لبنان</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80301" target="_blank">📅 15:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رئيس الوزراء العراقي: زياراتنا المقبلة ستكون إلى تركيا وإيران والسعودية بعد واشنطن</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80300" target="_blank">📅 15:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇩🇪
الشرطة الألمانية:
مقتل خمسة أشخاص في إطلاق نار في ستاد، شمال ألمانيا.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80299" target="_blank">📅 15:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حدث امني في جنوب لبنان</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80298" target="_blank">📅 15:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
إطلاق رواتب مجاهدي هيئة الحشد الشعبي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80297" target="_blank">📅 15:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqBl71aoRGD8rJ9wqsWyFZ-dRWvUCM1z7XGbZUe1JkBRhhhYn5EpaibcRVVV2HkfJ1BF81cu21hsC8snhsDnuH1G_BjeMFL_VYmPrMH6Zen4i17uXgPkIsx9Ip8wSseFemeuErwUi0yWvAfclUXd9F9W_aNxRY4EcmewRKwKf4VXoi_1zmJBtCYYpsgp6zXefRvk-1XAACrm1ONdEK71f2lIq-1wBCwluzmhaoDOKp4UzT2a6rfLBmvPwHnmbLeYqz6z7kzfwrRKtEgpHr-4smxvE9NqsK9nZAJjZH7ikobPSTB3-QuBA4gz7ftzQYJBV8LPKoyp3qtN2Q_XXAZEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Upk5xSj0QBxh5GwErf_qA4XEYhVGtOqPNk2mAb7Ef5HWF4G8vnc7uFqKvhCyr86deNeND7dauEN-TMG76uhZ_9WCmwEHD8sP5yconCeW7txNCwmS8IHkuCyoCNsn9840ywnXzOT_a_DCF9CZu68kGmutmPcw8GtJ77XK6upgGnKd4gtH3m9oE7nJV6MN_G4MqlyPEbz2MdM0JXIpUi3F40avfwSO1ORxIPacVBzvxbm-RLfQhPav9fVMSMsr0OUtjG5_KaNmrn3_bqJEngMINIE6coja1oYnDC28UKE-2gMYUKtdko6iPVP_vl5ZpRa-Prx-8KKAygcizzSPM2SRkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇸🇾
عصابات الجولاني تضرم النار في مقام الشيخ ناصر الحكيم التابع للطائفة العلوية في قرية العريضة بريف حمص الغربي.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80295" target="_blank">📅 15:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مصدر في هيئة النزاهة العراقية: النواب الثلاثة المعتقلين في أربيل ضُبطت بحوزتهم أثناء عملية الاعتقال مبالغ مالية تُقدر بـ10 ملايين دينار، إضافة إلى 15 قطعة سلاح متنوعة من بينها مسدسات وبنادق من نوع M4.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80294" target="_blank">📅 15:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80293">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مصدر في هيئة النزاهة العراقية: النواب الثلاثة المعتقلين في أربيل ضُبطت بحوزتهم أثناء عملية الاعتقال مبالغ مالية تُقدر بـ10 ملايين دينار، إضافة إلى 15 قطعة سلاح متنوعة من بينها مسدسات وبنادق من نوع M4.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80293" target="_blank">📅 15:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80292">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏴‍☠️
‏
إيدو نوردن، رئيس ديوان نتن ياهو:
‏ينبغي أن تكون هناك دولة واحدة بين نهر الأردن والبحر الأبيض المتوسط.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80292" target="_blank">📅 15:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80291">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnfLVRxv21D3mH2CX_4HzDIWZqiJ6Um2GHojORqCJ0W4bidVNMEEzlINeUpqjDFO-gM9yq8_dEPfEFT9soD9WRPbApMC_pphL4njaC4OTpXQgnnQzr9Ah3FkPwf_x1zacLU9gd_djZYe8kMYvUUQT2mQC7EfhTrn93hJ7y9Zo2aUJDFmAevBr6MV_lpHVv_Y41xnErhIn624TU5M2i4-Golk6tWm3MR_Iz43zPukfPoi5mQTm4F9XVQI00tPRzrstAHXJhUZ4LnP3FeH4EX9-wjmgeNJPnWHvzE7jhhIh6PC_WaLgUhUqX_qwW_eOUMYL0gpvZR59S7A4vvUBn7HTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
إيران طلبت عقد اجتماع. سيعقد غداً في الدوحة!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80291" target="_blank">📅 15:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80290">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
اطلق حزب الله صاروخ أرض-جو باتجاه طائرة مقاتلة تابعة لسلاح الجو</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/80290" target="_blank">📅 14:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">المجلس الوزاري للاقتصاد في العراق يقرر تشكيل لجنة مشتركة برئاسة هيئة المنافذ الحدودية الاتحادية وممثلين عن الجهات المختصة في الحكومة الاتحادية والإقليم لغرض إجراء مسح كامل للشريط الحدودي وزيارة المعابر والمنافذ غير الرسمية في الإقليم</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80289" target="_blank">📅 14:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80288">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d54f652a6.mp4?token=G342QdVstxXsNeDwDcp4dREnUIqHRESlhPbrWDBBDZvBUdUUZMkperxN2RfOJUPfrzF5ds08rApUuYnhP3CADoHr3F8osXGx8S5XnEYwB1456_S_XFak3YNDqC9KJNDHnWVcWQCNOBDwTfrMgmRjI3wuwnoo8Ip9WCgnx5c8BQkObLAd804b_LNnShHoCrvCmyfS_ykywV7h9rNNZ05m796hShz-95bA6_ZkJOrUBl5poWbTtLcs8_0PznBJ0D35sxgQxw07AhMNX6oGCoTvP0r3UlvJ-nmYfZa94CU89sNl6W5JgZjS-ThvreaXZrpFqnKrIWTNkTIqfjcOCNggQzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d54f652a6.mp4?token=G342QdVstxXsNeDwDcp4dREnUIqHRESlhPbrWDBBDZvBUdUUZMkperxN2RfOJUPfrzF5ds08rApUuYnhP3CADoHr3F8osXGx8S5XnEYwB1456_S_XFak3YNDqC9KJNDHnWVcWQCNOBDwTfrMgmRjI3wuwnoo8Ip9WCgnx5c8BQkObLAd804b_LNnShHoCrvCmyfS_ykywV7h9rNNZ05m796hShz-95bA6_ZkJOrUBl5poWbTtLcs8_0PznBJ0D35sxgQxw07AhMNX6oGCoTvP0r3UlvJ-nmYfZa94CU89sNl6W5JgZjS-ThvreaXZrpFqnKrIWTNkTIqfjcOCNggQzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من عزاء بني اسد والقبائل العراقية في كربلاء المقدسة في ذكرى دفن الاجساد الطاهرة بعد ثلاث ايام من واقعة الطف الاليمة</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80288" target="_blank">📅 14:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80287">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
‏
ترامب:
أعلى نسب تأييد في استطلاعات الرأي على الإطلاق. حتى أعلى من يوم الانتخابات، 5 نوفمبر. هذا على الرغم من حقيقة أن إيران لن تمتلك سلاحاً نووياً!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80287" target="_blank">📅 14:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080fa0dd58.mp4?token=uB9R__JTx6TRPz5fGKuTcTpmVu9GrwDNulWNKeCyUBFWQzwasz4dts6LzZqLuFzGc6wD6mptu1WokGQ4TeSHCCdtcgUbyUmJlvb_eSAwr25Ms0dd67oIgoWR3YWrcO25ipENy6eCmiLzsySL4T340GaNmMaC1LEMuwpGnLQUYm3EWhPselRaqSsY19x6IhU7G-sqcXVeJeqflP4I6jIlQ-bYVt-XXFFbd2UxZKVg2-HYu3FU5NLKW9rnsFHvraurhmj_-EyBqAQ4XnKwQiHZ99Ni2ruY7k89tZiYoBk4PjPa2lqj__rKrn6sLH4m30oZitqRzWYSDkoW5LgUta72Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080fa0dd58.mp4?token=uB9R__JTx6TRPz5fGKuTcTpmVu9GrwDNulWNKeCyUBFWQzwasz4dts6LzZqLuFzGc6wD6mptu1WokGQ4TeSHCCdtcgUbyUmJlvb_eSAwr25Ms0dd67oIgoWR3YWrcO25ipENy6eCmiLzsySL4T340GaNmMaC1LEMuwpGnLQUYm3EWhPselRaqSsY19x6IhU7G-sqcXVeJeqflP4I6jIlQ-bYVt-XXFFbd2UxZKVg2-HYu3FU5NLKW9rnsFHvraurhmj_-EyBqAQ4XnKwQiHZ99Ni2ruY7k89tZiYoBk4PjPa2lqj__rKrn6sLH4m30oZitqRzWYSDkoW5LgUta72Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مطار كركوك الدولي شمالي العراق وانباء عن حريق كبير في محيطه</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80286" target="_blank">📅 14:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80285">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: الاعترافات التي التي أدلى بها المتهمون تقود لشبكات أخرى على مستوى الأسماء والأموال، سردية مكافحة الفساد لا تشبه سابقاتها وحماية المال العام مسؤولية لا تتأثر بالأشخاص أو الظروف</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80285" target="_blank">📅 13:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80284">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: سيتم التعامل وفق القانون مع من يتخلف عن تسليم سلاحه قبل نهاية سبتمبر</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80284" target="_blank">📅 13:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80283">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: رئيس الوزراء وجه وزارة المالية بإنشاء حساب لإيداع الأموال المستردة من المتورطين بالكسب غير المشروع</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80283" target="_blank">📅 13:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80282">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: إلقاء القبض على 21 متهما متورطا في ملفات الفساد في عملية صولة الفجر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/80282" target="_blank">📅 13:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80281">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: إلقاء القبض على 21 متهما متورطا في ملفات الفساد في عملية صولة الفجر</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80281" target="_blank">📅 13:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80280">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
هيئة النزاهة العراقية: تمكنا من حجز كميات كبيرة من الأموال في الخارج</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/80280" target="_blank">📅 12:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80279">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a162cc92.mp4?token=gskBTflLiVCp3Gr0HInOUiwrMP_gJpKFxfpBLRDAAz4gNhR5xXYWyYssDlQm_1PgmyUnqDFEURo_ZPBc3LhC1DL9eBCbSTXyfC6PZ5VcOGwspvTnjprg7XY3YLQp6lVSWgDKWt1d_gIPwfL1CEhD3V-2YIlqgRh-omMvq-BAc1lpAK42z6ARzYBQ4p-Nh59QkYgVRly50xdzyonViEua-wBWwutWdig7ugnvY8JkXq9d2YUGvA_tyAZE07Dm4k4eWym7VenO5oiTSBPlc8i3DBr-RuPx4Ec5_O9-9S2QnINt1WbJVU8IWEkbKJKOOwcED9MxehoSJblqfmbHk_L-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a162cc92.mp4?token=gskBTflLiVCp3Gr0HInOUiwrMP_gJpKFxfpBLRDAAz4gNhR5xXYWyYssDlQm_1PgmyUnqDFEURo_ZPBc3LhC1DL9eBCbSTXyfC6PZ5VcOGwspvTnjprg7XY3YLQp6lVSWgDKWt1d_gIPwfL1CEhD3V-2YIlqgRh-omMvq-BAc1lpAK42z6ARzYBQ4p-Nh59QkYgVRly50xdzyonViEua-wBWwutWdig7ugnvY8JkXq9d2YUGvA_tyAZE07Dm4k4eWym7VenO5oiTSBPlc8i3DBr-RuPx4Ec5_O9-9S2QnINt1WbJVU8IWEkbKJKOOwcED9MxehoSJblqfmbHk_L-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قوة أمنية من بغداد تقتحم بلدية بعقوبة بمحافظة ديالى وأنباء عن اعتقال موظفين ومهندسين من داخل البلدية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/80279" target="_blank">📅 12:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7f80ffc4.mp4?token=rBajnszdn71Fmii36xkv6f9b-b3wZoAyLMzAO9sJi2LcfdOrdqG-ICipLeoNRKHTa3ZFAoP6gdOjZDdI7-nBqWwvR9iX7_IDsg6UxKlvwEivOlapqiTu0P1A7vcvUjktCrkQPmR3DzfPq9jRaW_ReSQKvy5STVb4NikQ7tKml2C6Q5AC6OWJ1Igt1__m7pSesHj4LWevLiwNZAdesMDwhmsXZXYE_EMePjopue9b8eCiC62jacsCGj0eHYwpqW06wC0pls6TBPdQGepIJR2LF_CCdnj71aRQEcNnZChdIfNzjpghEnGPtCbPaiGGg58jpze9rIyvszxD-K4LteV8BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7f80ffc4.mp4?token=rBajnszdn71Fmii36xkv6f9b-b3wZoAyLMzAO9sJi2LcfdOrdqG-ICipLeoNRKHTa3ZFAoP6gdOjZDdI7-nBqWwvR9iX7_IDsg6UxKlvwEivOlapqiTu0P1A7vcvUjktCrkQPmR3DzfPq9jRaW_ReSQKvy5STVb4NikQ7tKml2C6Q5AC6OWJ1Igt1__m7pSesHj4LWevLiwNZAdesMDwhmsXZXYE_EMePjopue9b8eCiC62jacsCGj0eHYwpqW06wC0pls6TBPdQGepIJR2LF_CCdnj71aRQEcNnZChdIfNzjpghEnGPtCbPaiGGg58jpze9rIyvszxD-K4LteV8BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حريق ضخم جداً يلتهم معارض النهضة وسط العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80277" target="_blank">📅 11:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nywpc9D2H0kbM70TZe0MQ0IX9OBuct9BH0ZipTD48NfIUSBgW3OmbpnbssFEdnHHk9WiNP4hC8oARY_SlBGBrL0x6ybAdu8UMlmEtpGo-htIZgJSn5SOz8ePAQzL5zXyW8DjfXURbxd9EjWhf7fugnDQlXBtQu4r8NpOf9Z6HgtNLxLif29fCqgFuG_rJb2nC-gIF14xgMFs-mCVgq76UwnYfIMhihPDtZWTLQbY_j8V132-24WOicX1z33QLNkDLthsZ2yLti0J1M1zSdDkITI1ZMolS044KjNLBFTGYiCjBnghQRrof0pb-mHNnHUKpAIOcLFRBPOOncuVCIUNFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يوجه آئمة صلاة الجمعة لوقفة سليمة يوم الجمعة ترفع فيها رايات الإمام الحسين وأعلام العراق دعماً لحملة الاعتقالات ضد الفاسدين في العراق.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/80276" target="_blank">📅 11:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjL77aapBxFLlG0HjsH8gAt9nXemvHMVCTCZBcbJ0ykpztUJf351tuhzMDy0_vOYLq3l0B25BUCfXZR4gMwhqhMWeQeXAo8oDtUg-wbmN35m8T-MGjeQ-hxE5_BLwgPCgUCOWYiOBRhG-63eH2jFMp1N-RNuY14Yfcdg9rinuSY6LGzNFfp7YUZ8q4F45eY_iaWBlPs4Dm2qXtIbZgI5vhC0nMUpOmM7X0yM6gs9Xz88374qmr2yUIGIZy5q0M4iWRRVbMOHiLOVZHslKQwAqBNbuNQFlqXMS-D9jue3wLnhGeWw5nk7Nh8ql5Uw0IzYY0EJ2b6boRFYAzSkFDMqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الجيش اللبناني يغلق طريق النبطية الفوقا ويمنع دخول الأهالي إليها بعد تكرار الاعتداءات الإسرائيلية حيث تعد هذه الخطوة أول خطة استراتيجية تم تطبيقها من قبل الحكومة اللبنانية لتحرير الجنوب.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/80275" target="_blank">📅 10:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c76cd22f.mp4?token=eE_tOEYsbri1QKb7RNFPKXk21TKiAgJ667IUIAfUbF4iB-soH9Eyag12VjnVVEwp-r43kcTA8gpxL2OAbKRBN4KUTHKuH8HbfmgYMTFpDZzGV8dFrQs1pX1Jy4eGu03zE-a6Lm7MLs-64v3opTMqVPzZViQDHafVXy1FKSiFhVkPq3cu34jXuLaCFLIcX0e4eJ-kt8XpT8S4_E69qrgTkaiYSCW5nZiGWSMD4UOjiQmyhzYzf7CMxFqG0_KGkdnb8wC77tpqoPjmOt7dF0fI4X4XBiRJAWctMGRsR1msvF2hVJn6EKWEQktVj86krlCmt0pdZJrd2KYrg20BTa0r4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c76cd22f.mp4?token=eE_tOEYsbri1QKb7RNFPKXk21TKiAgJ667IUIAfUbF4iB-soH9Eyag12VjnVVEwp-r43kcTA8gpxL2OAbKRBN4KUTHKuH8HbfmgYMTFpDZzGV8dFrQs1pX1Jy4eGu03zE-a6Lm7MLs-64v3opTMqVPzZViQDHafVXy1FKSiFhVkPq3cu34jXuLaCFLIcX0e4eJ-kt8XpT8S4_E69qrgTkaiYSCW5nZiGWSMD4UOjiQmyhzYzf7CMxFqG0_KGkdnb8wC77tpqoPjmOt7dF0fI4X4XBiRJAWctMGRsR1msvF2hVJn6EKWEQktVj86krlCmt0pdZJrd2KYrg20BTa0r4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قوات أمنية تصل إلى محافظة كركوك شمال العراق لليوم الثاني على التوالي لتنفيذ عمليات الاعتقال بحق مسؤولين متهمين بقضايا الفساد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/80274" target="_blank">📅 10:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7iWNtpJ-sY0l2-cNZOJUJHhrTVweJoF2OxLrKFStyg1Hsg8xkHlw8fQ-VV6Goks0d1TBm5LebX368nBjWjp5SK8oJaRk9Z8yGJQnpmVa8z-OwDSQUu9Bb7dRHZDJFbAsO-YNC7nZXlN2zhBUAJqy_vBT5lfAlNgd90023FyOrMsq8ZaQ814FrTJvUtnaVulL-bmEThbCvSTzQyhKLNKQ6_gpU0e-HSczs2HJfhY-IJBXO8D8aargiEtKcLmQ61_Yn4SsfYb0eHsu6jDCX_30ZsGlEFMDC2842u14-dF8d6OSs4WzlLXsGPevGYPeYySR-QoUOQ7zUew1MyYSKoqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
القوات الامنية تضبط شخص بحوزته مليارين في سيطرة قضاء قلعة صالح بمحافظة ميسان جنوبي العراق.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/80273" target="_blank">📅 01:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80271">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
مجلس الوزراء يقر مبادرة المليون قطعة أرض سكنية كمشروع وطني لتوزيع الأراضي المخدومة على المستحقين في جميع المحافظات، باستثناء إقليم كردستان.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/80271" target="_blank">📅 01:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80270">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
رئاسة الوزراء العراقية: ما جرى من صولةٍ ضد الفساد هي مرحلة أولى، والوضع بات من غير الممكن السكوت عنه.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/80270" target="_blank">📅 01:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80269">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f416360a.mp4?token=CmGFx74u3_JDcGK7txYoUZu9FjxGYgedqNQ5O7lqU7F8O_EpuOj2Tv8XALVZgAn4I7K7VkfeuLpOwrDB9iaeNZh7yTMKKqmOf79kStpaB72CnQ3Xk4o14t_Jc8APfP1-CuKN7_KrhAe12ZdG4UpIvnZeoE4-JYg1mZXT8HEVYeKm0FMJAlG2BmOwboGNcx-42BiOdAb1H0XWpRnDMzhI7lFFCSsyyWDVz1GO2OuSQ_Pnszx1wRuY7Z2ufU9Hwzz_xCMtrC1iLMdiOneAN_0iXR4UMvMlbZDQK4lqoqXlZ58mSlfvLIhaa2-G4LGKPrZ_YiLwlp3qMtWmdK1zdg6znA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f416360a.mp4?token=CmGFx74u3_JDcGK7txYoUZu9FjxGYgedqNQ5O7lqU7F8O_EpuOj2Tv8XALVZgAn4I7K7VkfeuLpOwrDB9iaeNZh7yTMKKqmOf79kStpaB72CnQ3Xk4o14t_Jc8APfP1-CuKN7_KrhAe12ZdG4UpIvnZeoE4-JYg1mZXT8HEVYeKm0FMJAlG2BmOwboGNcx-42BiOdAb1H0XWpRnDMzhI7lFFCSsyyWDVz1GO2OuSQ_Pnszx1wRuY7Z2ufU9Hwzz_xCMtrC1iLMdiOneAN_0iXR4UMvMlbZDQK4lqoqXlZ58mSlfvLIhaa2-G4LGKPrZ_YiLwlp3qMtWmdK1zdg6znA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انتشار واسع للقوات الامنية في محافظة واسط العراقية.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/80269" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80268">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
رئاسة الوزراء العراقية:
ما جرى من صولةٍ ضد الفساد هي مرحلة أولى، والوضع بات من غير الممكن السكوت عنه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/80268" target="_blank">📅 01:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80267">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
استمرار القصف العشوائي الصهيوني على قرية عابدين بمحافظة درعا السورية وسط نزوح معظم أهالي القرية.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/80267" target="_blank">📅 01:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80266">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
انباء متداولة عن انعقاد مؤتمر لهيئة النزاهة الاتحادية بعد قليل.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/80266" target="_blank">📅 00:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80265">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLLyc5ZHzPpokiCRXjiUwFim_xcoFQhkHPd89FCBgZ1yODY67FRChGRynYJAErHoasxZPJB0TRNo7anufAe0x8pnWwDlm3HfyT7THMmedf0Q4LLOzqn2-pu25O-2RwZfYHLZ3ko3uAGkvKCFY0bjw9G3yqke4_s66GZDLupAZmt9mDJjgYfbAFoeFgb6J4v0dnTD3X4R2S2B-vPNt-uw_rvcgzs8404fHJA-1PNm9_uf4vwZ6YdB17m6PAMLqoOFD5_rTz_hHIUYRbSZy_I9g-QJRkzkb-RAas0M7Pq1YRnAMqX6RMSNt3XKAMjvjdVWyZawoITRrFql3UYJsesRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
انباء متداولة عن انعقاد مؤتمر لهيئة النزاهة الاتحادية بعد قليل.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/80265" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80264">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d422bceb1.mp4?token=osSnRDdlsslm85jHkfqvk7-u-3tFo4BNv2pHRh87RoG8TxoRGRUtBnh3iTrcommtEevUt1GIApILk_OAkya7YwTdjuJB2dZZIwPivg9MOEag_EAiL1aG50nShNvcZVRsOpcNE2ddcDsQnRVEzy_hiCz3v4igZ8s_cK8siQeljJQfVcFDvKxp8IldERzxJ-lnP0Ho0DdRrGADWfP5RgwkeInw6qtcYnvuYRMQnFs-ISwWF4YuMHEWk9uorWBqOJuKgtXK0M--OoqbW-jRiOJkfkIicbA79eITdF1v5Gk18wyN9x6f3-TY_klBEVw5O3Xumz4zCGtKeFbWVQSktjQnog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d422bceb1.mp4?token=osSnRDdlsslm85jHkfqvk7-u-3tFo4BNv2pHRh87RoG8TxoRGRUtBnh3iTrcommtEevUt1GIApILk_OAkya7YwTdjuJB2dZZIwPivg9MOEag_EAiL1aG50nShNvcZVRsOpcNE2ddcDsQnRVEzy_hiCz3v4igZ8s_cK8siQeljJQfVcFDvKxp8IldERzxJ-lnP0Ho0DdRrGADWfP5RgwkeInw6qtcYnvuYRMQnFs-ISwWF4YuMHEWk9uorWBqOJuKgtXK0M--OoqbW-jRiOJkfkIicbA79eITdF1v5Gk18wyN9x6f3-TY_klBEVw5O3Xumz4zCGtKeFbWVQSktjQnog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أربيل تسلّم 8 معتقلين إلى هيئة النزاهة العراقية في سيطرة آلتون كوبري بينهم أعضاء مجلس النواب محمد المياحي، وأشواق الجبوري، وزياد الجنابي، إضافة إلى 5 موظفين كبار في الحكومة</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/80264" target="_blank">📅 00:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80263">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔻
الاعلام الاميركي:
اتفقت الولايات المتحدة وإيران على وقف الهجمات المتبادلة في مضيق هرمز وعقد اجتماع يوم الثلاثاء في الدوحة.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/80263" target="_blank">📅 23:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80262">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdb22e6ee.mp4?token=fUc85LjnGvkwxb6U0ZrWgIQEQ2ZeF4soOrwwCGXLFu56LbBte8sbEXg9tKcJmMsTYm3PIbaCE8pu01MPQ8Ly3Iq8WADqYGtHLjDtDsALgrBF6vcykYvwSqRbzMquqJ0bCb4fZvARg1QDQuU6vroq8gf8xtxRnZPEwCzMaIU13aQ_M6CAS6S7JbIM5WffHROxpqEUTXVwUWJIlBC5DUIdS9iy2UZdsc_RD3qd6exaf6nIvoXJ0Iq2dKhmb-83WO0IPQeb-zb9yhp9M1W2SG5dzkS1Mh1IEIaa7WuUkzbFhsWLGD0cTjQXgXDiIKc6GNr83JVAVrp7OS48XT7JQnSTzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdb22e6ee.mp4?token=fUc85LjnGvkwxb6U0ZrWgIQEQ2ZeF4soOrwwCGXLFu56LbBte8sbEXg9tKcJmMsTYm3PIbaCE8pu01MPQ8Ly3Iq8WADqYGtHLjDtDsALgrBF6vcykYvwSqRbzMquqJ0bCb4fZvARg1QDQuU6vroq8gf8xtxRnZPEwCzMaIU13aQ_M6CAS6S7JbIM5WffHROxpqEUTXVwUWJIlBC5DUIdS9iy2UZdsc_RD3qd6exaf6nIvoXJ0Iq2dKhmb-83WO0IPQeb-zb9yhp9M1W2SG5dzkS1Mh1IEIaa7WuUkzbFhsWLGD0cTjQXgXDiIKc6GNr83JVAVrp7OS48XT7JQnSTzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار القصف العشوائي الصهيوني على قرية عابدين بمحافظة درعا السورية وسط نزوح معظم أهالي القرية.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/80262" target="_blank">📅 23:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80261">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc497ecbb1.mp4?token=VfOHbS-uKqWK5BrUPHWAc57FihKAhbdSup2wm0ZSNS0y5SOGkkwG9ZpIrDuAo_xX-S1BEF1glN4RkVVUT7yhKCGeex6jBjgEQtOhR5BYS02fmkbM_3F97SNY7PptkX1ZDaYuXzPPANZOHQg5DJx-W2tfJB6dcXqb8hb1JEJBIkmSLt0mIYIBEHrQQszaf-lISgGLIzXN3keKxKH0P5-w3hdqDlcxvyTnMQD8N4x-249KQc1sBulAeOj5B1n-NMeiQvz8U5rN76wBHHEjYbKyXu5KJvgCho-Cbf3PjYfOIXvdvM4qnKDyBK0bhGduP3Hog9Z77zhPGXw1itgRhEJ58A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc497ecbb1.mp4?token=VfOHbS-uKqWK5BrUPHWAc57FihKAhbdSup2wm0ZSNS0y5SOGkkwG9ZpIrDuAo_xX-S1BEF1glN4RkVVUT7yhKCGeex6jBjgEQtOhR5BYS02fmkbM_3F97SNY7PptkX1ZDaYuXzPPANZOHQg5DJx-W2tfJB6dcXqb8hb1JEJBIkmSLt0mIYIBEHrQQszaf-lISgGLIzXN3keKxKH0P5-w3hdqDlcxvyTnMQD8N4x-249KQc1sBulAeOj5B1n-NMeiQvz8U5rN76wBHHEjYbKyXu5KJvgCho-Cbf3PjYfOIXvdvM4qnKDyBK0bhGduP3Hog9Z77zhPGXw1itgRhEJ58A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار القصف العشوائي الصهيوني على قرية عابدين بمحافظة درعا السورية وسط نزوح معظم أهالي القرية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/80261" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80260">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febc059431.mp4?token=WT_Bnwcmyw840ik8j_HNBjDncBvQwGR0hqBE2YNgYwzaIz114Rb7_VUlyY4pmPg5wFjpx9q5TOzNjw5QBQsxYh-p6Pj4MsNXLsQ1EgPljQJWU_h_4uYybO1GhdhzOC-OuzX8L7KxF30lp_dSoepyfVVQ_3E9Lsts8UkzB_sHiuMvY6LwUcQa4pN5Tzadi3-p3-WkFtDyNT-eYebqqcdKrAX5bIfoc1c-S0RFqD9N_LCQdOxKYdxaH8T0l0zM6Vts1cEUBaI7RQ6B9Uh74Toqb4oRusnl2soSePAAUmkLxL2iNKzcUqGSDXBBQgHuI9omVqKFgvYLxRccoj2Pw40pWDgMZeB5GwPP1HIFodBy9wQ-KxurQUg5sAqDZGH-XQBgMJnOsYBU2BEuxY5xmp1sQ9Sufq82byX3tA-mLbL20yJkWqHzD_qogOCudIkVQMfSmvdW_9aBuPpZUT9hvxS6EPaCAyyMWQQRXv3T-JRMOHNwF-kg9CBJmyrbuaDl8PYvUxSCZla1WGZC8QwPzcMzP51FbAzOOEaDMOihYi6eDvskO95UTCJvodx-GTUtf0X3WFKRcCuuLFX1P8SOVpiEMuw9_dDgafewhxHtEC94Qr3YsELM2YZ4XERGXQOzhl20pTCQQ9vIFYvp_1K0TTu7XSuBjTVneCnc90KHkkTY47g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febc059431.mp4?token=WT_Bnwcmyw840ik8j_HNBjDncBvQwGR0hqBE2YNgYwzaIz114Rb7_VUlyY4pmPg5wFjpx9q5TOzNjw5QBQsxYh-p6Pj4MsNXLsQ1EgPljQJWU_h_4uYybO1GhdhzOC-OuzX8L7KxF30lp_dSoepyfVVQ_3E9Lsts8UkzB_sHiuMvY6LwUcQa4pN5Tzadi3-p3-WkFtDyNT-eYebqqcdKrAX5bIfoc1c-S0RFqD9N_LCQdOxKYdxaH8T0l0zM6Vts1cEUBaI7RQ6B9Uh74Toqb4oRusnl2soSePAAUmkLxL2iNKzcUqGSDXBBQgHuI9omVqKFgvYLxRccoj2Pw40pWDgMZeB5GwPP1HIFodBy9wQ-KxurQUg5sAqDZGH-XQBgMJnOsYBU2BEuxY5xmp1sQ9Sufq82byX3tA-mLbL20yJkWqHzD_qogOCudIkVQMfSmvdW_9aBuPpZUT9hvxS6EPaCAyyMWQQRXv3T-JRMOHNwF-kg9CBJmyrbuaDl8PYvUxSCZla1WGZC8QwPzcMzP51FbAzOOEaDMOihYi6eDvskO95UTCJvodx-GTUtf0X3WFKRcCuuLFX1P8SOVpiEMuw9_dDgafewhxHtEC94Qr3YsELM2YZ4XERGXQOzhl20pTCQQ9vIFYvp_1K0TTu7XSuBjTVneCnc90KHkkTY47g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع اشتباكات بين مقاومين سوريين وقوات جيش الاحتلال الإسرائيلي في محيط بلدة عابدين بريف درعا الغربي.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/80260" target="_blank">📅 23:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80259">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWPSXwP55VbUXuFK0o6lCxmijhF4e83jKxTq-i15Y_OXTjlVE3x1yLu8mPhUR13aunIPugLb-bkIMzi6cDUFM_kuN8KAZiJE1kI6cYoQJEb39RUPCsIyEJhuWXYzAsc_ZyhLZkwtnUwmM1SomRDa8TQgaZ-VFZKQNb39z-R8_HjrLXf3uGXhZfV7fY85kHcUpDgfdMV8uDGPSsfHwui3l-hWZ3IVpeveuKisrIVcg6euKqMO1b2aVe-KDETU6cxVMoQmN5Wggr5aKFd0sVMmg9QMo9CmEka12H2gd52SX0n7xgKOFlc8srHYJq9frtprFceGoxb5PPRHryJgACGb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اندلاع اشتباكات بين مقاومين سوريين وقوات جيش الاحتلال الإسرائيلي في محيط بلدة عابدين بريف درعا الغربي.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/80259" target="_blank">📅 23:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80258">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMEKqzL96BisA_sUQwUZ0j_cnZKXTWKZWvojPVqoJf0mMcO_WZ7bE9K4ceTugKrjytUaa3Dk-F2_A2LGuJZjbO6WeoE-xsWGworCQx-ubh9ZkwAm4OGd9DwhP09xDsMxpBo1WsVlcj_WJIWR0BmF8r1opNM8uccTpIrYRAPSTQ3BQT75fTWPSB_DWav4pSmhlS1JrANxzUvc0rVnMIgu0Z9pzb6uc8Y6zAXxhtEz_iV-uPr7lDgiyIAVAoAToZKqEaczoDXTPLk_zM9TqBf0zp9B-i9-GgcIHct139PE6RqShfCh61v_cGnpFzMLWDs5grkj8Dwu06q_QmeI_KBdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الاعلام السعودي:
اعتراض صواريخ فوق شمال الأردن.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/80258" target="_blank">📅 23:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80257">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee392353a.mp4?token=PQhdMMzY_PDRn_jqi0buO0JZGe5dAnKfOwa3E_DZGOvlxEXRJJrpwK-4xDdz9RBmUf2DR0hGFRZIw_jk2mK0pS-csiaSOVIDbYBU4aYJV9ujHfS0RzgwYCM4fidI-hL3VGFNTF1LKg4N6yqOm7mDLTuWRipi5cWDukTHpMCKOpLqjSFrQfe79aFVsx_yfd42wxW5hl4wjfImlGgMmJbBWN4I66jpbboYm-9oH94GFOLr48XtOwkNiZoTXeHerkFtH8NT-quaJRcFlTefFxrjP2rxfvCcHyuqlyznzR_8aKF8qoS41lAWggwGVWOw_YoICZe-APuPD3pC_tOFH650yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee392353a.mp4?token=PQhdMMzY_PDRn_jqi0buO0JZGe5dAnKfOwa3E_DZGOvlxEXRJJrpwK-4xDdz9RBmUf2DR0hGFRZIw_jk2mK0pS-csiaSOVIDbYBU4aYJV9ujHfS0RzgwYCM4fidI-hL3VGFNTF1LKg4N6yqOm7mDLTuWRipi5cWDukTHpMCKOpLqjSFrQfe79aFVsx_yfd42wxW5hl4wjfImlGgMmJbBWN4I66jpbboYm-9oH94GFOLr48XtOwkNiZoTXeHerkFtH8NT-quaJRcFlTefFxrjP2rxfvCcHyuqlyznzR_8aKF8qoS41lAWggwGVWOw_YoICZe-APuPD3pC_tOFH650yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع اشتباكات بين مقاومين سوريين وقوات جيش الاحتلال الإسرائيلي في محيط بلدة عابدين بريف درعا الغربي.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/80257" target="_blank">📅 23:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80256">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKG9ltctIDExYI-2_UwH28tlFVtOH9o2KOcAVKPA63GRRXl9cu1a0d-tC04r4mLd3c9CdjZTZooozydyThd-EXTYPxlAyGS_l4hwtwYckhDG1EIUjUbqf1Gany__togQlM0h6Fc632sA5XYsi4koblH79sHj4BFiByf-xScAj5pQzurjFkXfjBeNV1olukouEhPfZtdbc5hku96KV1MlulaBDYSvVbvawkNzoIInT9FZUHrL3NitoYt-nX_3JSM7j6xr-v0-FaGvt2_qEcRSE8yqYLNdryZ2toDzsVOvL9BGZ7931a9vU6cDUZxGt6gEbneb-AqAfidN_AEXoI5-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
استيفاء مبلغ (2500) دينار من جميع الداخلين إلى العراق عبر منفذ حاج عمران في محافظة اربيل تحت مسمى "دخولية العراق" ما أثار تساؤلات بشأن السند القانوني لهذا الرسم والى خزينة اي برزاني تذهب هذه المبالغ
الله يديم الرخص
بالفين ونص دخولية بلاد الحضارات
😄</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/80256" target="_blank">📅 23:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80255">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e2ec824e.mp4?token=jqvJAN-2aKCx2h-f3-VDhfXdMnFwfDcqJ-F1qesUJ8fOTAMvOpwDoIoG3kmjwjnZeWDCQZnmSodNkut-dLUtzksWDz1u_GryMaY71MR1Rx2-pIvfC-N31Q7m1a4NCl1MwG-8VO8d0XOZSjQUivafD6Xgp76BtFBvBZrl5r4qwlEy8x_Am39wQ4wnzJHp-F5rB0iFeqKFCnYmQD-lUmauxDn6K9M-MZIJNwpl84IGm-n8wpG7ZcSm9HtcpZvr2YnpuVlwwpwpsb9LmkO6WdbTn8KHTaBpn_CwulZIMbMDRMVUYxYJZ_3mw81Gi4Lj48Nlt5xmcvjJ-vSqM57rkM6h6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e2ec824e.mp4?token=jqvJAN-2aKCx2h-f3-VDhfXdMnFwfDcqJ-F1qesUJ8fOTAMvOpwDoIoG3kmjwjnZeWDCQZnmSodNkut-dLUtzksWDz1u_GryMaY71MR1Rx2-pIvfC-N31Q7m1a4NCl1MwG-8VO8d0XOZSjQUivafD6Xgp76BtFBvBZrl5r4qwlEy8x_Am39wQ4wnzJHp-F5rB0iFeqKFCnYmQD-lUmauxDn6K9M-MZIJNwpl84IGm-n8wpG7ZcSm9HtcpZvr2YnpuVlwwpwpsb9LmkO6WdbTn8KHTaBpn_CwulZIMbMDRMVUYxYJZ_3mw81Gi4Lj48Nlt5xmcvjJ-vSqM57rkM6h6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أربيل تسلّم 8 معتقلين إلى هيئة النزاهة العراقية في سيطرة آلتون كوبري بينهم أعضاء مجلس النواب محمد المياحي، وأشواق الجبوري، وزياد الجنابي، إضافة إلى 5 موظفين كبار في الحكومة</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/80255" target="_blank">📅 22:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80254">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رئيس تحالف عزم مثنى السامرائي</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/80254" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80253">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⭐️
إعلام العدو يزعم: إطلاق صواريخ من إيران نحو الأردن.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/80253" target="_blank">📅 21:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80252">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭐️
إعلام العدو يزعم:
إطلاق صواريخ من إيران نحو الأردن.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/80252" target="_blank">📅 21:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80251">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
قاضي تحقيق محكمة جنايات مكافحة الفساد المركزية:
أن التحقيقات في قضية المتهم (عدنان الجميلي/ وكيل وزارة النفط لشؤون التصفية) قد بدأت في الشهر العاشر من عام 2025، إثر تلقي المحكمة مجموعة من الإخبارات التي تتضمن قيام عدد من المرشحين بصرف مبالغ مالية طائلة لدعم دعايتهم الانتخابية مستغلين موارد الدولة، وبدعم من شخصيات نافذة في الحكومة السابقة. ولأهمية ودقة هذه الجريمة، استمرت جهود جمع الأدلة والمعلومات عدة أشهر، وعقب إلقاء القبض على المتهم المذكور، كشفت مجريات التحقيق عن تورط مجموعة من أعضاء مجلس النواب في استغلال موارد الدولة للدعاية الانتخابية، والانتفاع من العقود الحكومية بصورة مباشرة أو بالواسطة للحصول على عمولات ومنافع شخصية لأنفسهم ولغيرهم، الأمر الذي اقتضى إجراء التحقيق معهم واتخاذ الإجراءات القانونية بحقهم. وبناءً على طلب المحكمة ومفاتحة مجلس النواب، رُفعت الحصانة عن النواب المتهمين من قِبل رئيس مجلس النواب العراقي الحالي، استناداً إلى الصلاحيات الممنوحة له بموجب أحكام المادتين (63/ثانياً/ج) و(7/رابعاً) من قانون مجلس النواب العراقي رقم 13 لسنة 2018، والمادة (11/ثانياً/3) من قانون العقوبات العراقي رقم 111 لسنة 1969 المعدل، والمادة (20/ثالثاً) من النظام الداخلي لمجلس النواب العراقي. وفور ورود كتب رفع الحصانة، وبالتعاون مع هيئة النزاهة الاتحادية وجهات إنفاذ القانون، وبإشراف مباشر من رئيسي مجلس القضاء الأعلى ومجلس الوزراء، جرى الشروع بتنفيذ أوامر القبض الصادرة بحقهم وتوقيفهم، حيث تم ضبط أموال ومبرزات جرمية تثبت ارتكابهم ما يخالف القانون، في حين لا يزال قسم منهم هارباً، علماً أن التحقيقات في هذه القضية مستمرة على ضوء الأدلة، وسوف تتخذ الإجراءات القانونية بحق شخصيات سياسية وأشخاص آخرين خلال الفترة القادمة تزامناً مع تطور مجريات التحقيق.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/80251" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80250">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d2b6622c.mp4?token=O1tMywEJ8ug5muhjvCwvHfJozZzhPmJgJfRVhqr-zMhZlK9-LiVsqTsIcrUFOgnGraOs1Hf6LvPHjMImGIOvgUMuHCBzbZ6ExKrim4t6OGJ-X0K5h_0XuwQmV8o6NOsXYLTIOcGCnRYckChtwXzsJPEe6PTatq5_IXu7nyRj_LXPbYS9iWL15EkvI8N7a23EiKSZeeLOf-W-J3qhXPu7YWtxoOvSbH0sYMF1Jq8Eaa8Nz2ZemzcA1rFHvIlYnfc14bxv5u7nfHAvnWOt-NVL6wUg1wOoZm_1LxpaqBNfwl369EJZFxmVzrOhO04A1b90RfJAMDCp6ji9MNFSUTA_zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d2b6622c.mp4?token=O1tMywEJ8ug5muhjvCwvHfJozZzhPmJgJfRVhqr-zMhZlK9-LiVsqTsIcrUFOgnGraOs1Hf6LvPHjMImGIOvgUMuHCBzbZ6ExKrim4t6OGJ-X0K5h_0XuwQmV8o6NOsXYLTIOcGCnRYckChtwXzsJPEe6PTatq5_IXu7nyRj_LXPbYS9iWL15EkvI8N7a23EiKSZeeLOf-W-J3qhXPu7YWtxoOvSbH0sYMF1Jq8Eaa8Nz2ZemzcA1rFHvIlYnfc14bxv5u7nfHAvnWOt-NVL6wUg1wOoZm_1LxpaqBNfwl369EJZFxmVzrOhO04A1b90RfJAMDCp6ji9MNFSUTA_zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
اندلاع اشتباكات بين جيش الإحتلال الإسرائيلي وأهالي منطقة حوض اليرموك بمحافظة درعا السورية،ماأجبر جيش الإحتلال الصهيوني على الإنسحاب من المنطقة.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/80250" target="_blank">📅 21:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80249">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
التحذير الذي نقله كبار المسؤولين في شعبة الاستخبارات والقيادة الجنوبية إلى رئيس الأركان زمير الأسبوع الماضي:
الجناح العسكري لحركة حماس يعيد تنظيم صفوفه استعدادًا للحرب من جديد. وتقوم حماس بإنتاج مئات العبوات الناسفة والصواريخ المضادة للدروع شهريًا، كما تجند مقاتلين تتراوح أعمارهم بين 18 و22 عامًا، وبدأت مؤخرًا بإجراء تدريبات لعناصر وحدة "النخبة"، وتحاول تهريب طائرات مسيّرة ووسائل اتصال من سيناء، وتعيد تأهيل البنية التحتية تحت الأرض في أنحاء قطاع غزة.
الموقف الذي نقله الجيش الإسرائيلي إلى الأمريكيين هو ضرورة العودة إلى القتال، إلا أن الأمريكيين يعارضون ذلك، ويرغبون في الإبقاء على الوضع القائم وفق الاتفاقات، مع السعي إلى مواصلة تنفيذ رؤية الرئيس ترامب ومجلس السلام.
وقال الضباط لرئيس الأركان: "حماس قوية على الأرض، ولا أحد يشكل تهديدًا لها، والمنظمة ليست مستعدة للتخلي عن السيطرة على غزة."</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/80249" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80248">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
هيأة الإعلام والإتصالات العراقية:
الامتناع عن تداول أسماء أو معلومات غير مؤكدة أو غير صادرة عن جهات رسمية.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/80248" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80247">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/526853f2ac.mp4?token=Ks5imsUfurAOPi1qfmDzQfLeJlm3PNgTHXYPCaic9VDvnpcUj6M9qWXj_0JxIIdk__fL1PDPucqeCBFnFpBYV-_pOI1UB58_zAOBgRQp8MLZJYtBBvchFH5C3MSta79IMMNKR8YdGhRZOJXOYwvs5AU8Uy_l_gqJxWcJLbCAQlCFGObg8wWwDCmWngFVeN-d7sDsGpv9hb9E7cFBEPHhdAfbv2-aN_dWTTgEAJ_9ndPpOjsBeDyL87hnmL4oxivDT5TUEtQKf3k4cH2xwJV0XRN1e2s_T1n4MSmvngizrCc6cdJxM7eAjUBpaHFwSfh1l4ueFV_m2fs-9wVH9xtYK02j5GKpqKMzWiVPMMy2qg3jwWEDMNMPB6EgJcWF6OfjTTnARxsEEsZs83jW22Prz6JhqA-1KjOkct3udG5rt3FHaS1gM7TTBXl0xaCxoPNkSbsjehcR-ORcQN5I2NPoMWmOEwQuPd15Q83GdxC6JaSDuYgYooyH4ASRAh_B_XaUHjiyMJwrNrUd4yt6rtb6ISLq_E1-VFo8s5MNKesHGhI2kDjyYjzuI7y8ghZI-ITW3ou8Ej3x-LfqhZmP7UFYXXDGsgvlfee3agD8FUFCzlHh5bFMzGLT4i3c3LLisCtCKYEB0SSAxRV7GpPDe91z3zjnLskjAOFi7wW26XlbfVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/526853f2ac.mp4?token=Ks5imsUfurAOPi1qfmDzQfLeJlm3PNgTHXYPCaic9VDvnpcUj6M9qWXj_0JxIIdk__fL1PDPucqeCBFnFpBYV-_pOI1UB58_zAOBgRQp8MLZJYtBBvchFH5C3MSta79IMMNKR8YdGhRZOJXOYwvs5AU8Uy_l_gqJxWcJLbCAQlCFGObg8wWwDCmWngFVeN-d7sDsGpv9hb9E7cFBEPHhdAfbv2-aN_dWTTgEAJ_9ndPpOjsBeDyL87hnmL4oxivDT5TUEtQKf3k4cH2xwJV0XRN1e2s_T1n4MSmvngizrCc6cdJxM7eAjUBpaHFwSfh1l4ueFV_m2fs-9wVH9xtYK02j5GKpqKMzWiVPMMy2qg3jwWEDMNMPB6EgJcWF6OfjTTnARxsEEsZs83jW22Prz6JhqA-1KjOkct3udG5rt3FHaS1gM7TTBXl0xaCxoPNkSbsjehcR-ORcQN5I2NPoMWmOEwQuPd15Q83GdxC6JaSDuYgYooyH4ASRAh_B_XaUHjiyMJwrNrUd4yt6rtb6ISLq_E1-VFo8s5MNKesHGhI2kDjyYjzuI7y8ghZI-ITW3ou8Ej3x-LfqhZmP7UFYXXDGsgvlfee3agD8FUFCzlHh5bFMzGLT4i3c3LLisCtCKYEB0SSAxRV7GpPDe91z3zjnLskjAOFi7wW26XlbfVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
اندلاع اشتباكات بين جيش الإحتلال الإسرائيلي وأهالي منطقة حوض اليرموك بمحافظة درعا السورية،ماأجبر جيش الإحتلال الصهيوني على الإنسحاب من المنطقة.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/80247" target="_blank">📅 20:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80246">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
‏قطر تعلن عن مقتل شخص إثر إصابته بشظايا ناجمة عن العمليات العسكرية بالمنطقة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/80246" target="_blank">📅 20:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80245">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7354f35590.mp4?token=ihkXycTGKku0Zrk2BRzDHcrW0Y1ixgRjvKQ0KBWC9AVieQRQv-queIuJKZiauO0kfQ8lPl8ZRqPa_IpU7jllvQEYGxUA02v_NkyYcsc-7drANyjTPtQcVEZ0crTTLv5pXyBfuuP0jLwiA87QRANYC2hxlglHKyzTzL-J0yZzlp2r9dF8N7kuXGq7FpuICexHGw5AiGUQbgUCewuidT3ioln79LWFsE1qoShQZqItJi0HrGfba2e9mpAMr6tKk7U21GaHMWktifok9WwZIoII0RuddDcu4CKdkueGOdNJvGQytjillDrZxyB6OK33YR5qFjc5yGhK1PNk5g0-18oOVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7354f35590.mp4?token=ihkXycTGKku0Zrk2BRzDHcrW0Y1ixgRjvKQ0KBWC9AVieQRQv-queIuJKZiauO0kfQ8lPl8ZRqPa_IpU7jllvQEYGxUA02v_NkyYcsc-7drANyjTPtQcVEZ0crTTLv5pXyBfuuP0jLwiA87QRANYC2hxlglHKyzTzL-J0yZzlp2r9dF8N7kuXGq7FpuICexHGw5AiGUQbgUCewuidT3ioln79LWFsE1qoShQZqItJi0HrGfba2e9mpAMr6tKk7U21GaHMWktifok9WwZIoII0RuddDcu4CKdkueGOdNJvGQytjillDrZxyB6OK33YR5qFjc5yGhK1PNk5g0-18oOVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
قوات أمنية إضافية تصل إلى محافظة كركوك لتنفيذ عملية الإعتقال بحق مسؤولين متهمين بقضايا فساد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/80245" target="_blank">📅 20:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80244">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce546b894b.mp4?token=MPOvG6IIpVP0ezyXqplbssQ-C_FSu89SOa2_kpnVL7FP9giqv0w7_mvxmce5R8_2j8l0aysJ7hQR_IXCJXZ_zaFZed0XftaOlT2GZBINW15Go4b1GppcjfQ6f7uAg3dqW8D39eweiF7KUpHdXHlT-TvFLhOj3bnxe9OmtWvPhf3LQAWJULL8aBraJAIFbN-pNUtqseAX8gb4LdBZwhiul4jNnBKDp63LHfAbzDkrSZaNcNoqZe037WiYrWbfTAj_PpfS9PMYSxdJSeLStvJ4rpRaOm2MbMGEFmhy3PnFKYaXkrMIrMdp7CVNQyCps7u8sQKqEyN2muOsNnzov2ByZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce546b894b.mp4?token=MPOvG6IIpVP0ezyXqplbssQ-C_FSu89SOa2_kpnVL7FP9giqv0w7_mvxmce5R8_2j8l0aysJ7hQR_IXCJXZ_zaFZed0XftaOlT2GZBINW15Go4b1GppcjfQ6f7uAg3dqW8D39eweiF7KUpHdXHlT-TvFLhOj3bnxe9OmtWvPhf3LQAWJULL8aBraJAIFbN-pNUtqseAX8gb4LdBZwhiul4jNnBKDp63LHfAbzDkrSZaNcNoqZe037WiYrWbfTAj_PpfS9PMYSxdJSeLStvJ4rpRaOm2MbMGEFmhy3PnFKYaXkrMIrMdp7CVNQyCps7u8sQKqEyN2muOsNnzov2ByZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
سوريا الجولاني..
سائحة أجنبية تتعرض للهجوم والتحرش في إحدى ساحات محافظة حلب السورية.
اوه ماي كاد
😆</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/80244" target="_blank">📅 19:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80243">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
زلزال بقوة 5.3 ريختر يضرب الصين.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/80243" target="_blank">📅 19:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80242">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
🌟
وول ستريت جورنال:
توقف محادثات كانت مقررة هذا الأسبوع بين واشنطن وطهران في سويسرا بسبب تجدد القتال.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/80242" target="_blank">📅 19:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80241">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔻
مصادر:
وصول قائمه بأسماء مطلوبين من محافظة الموصل بتهم فساد من الهيئات التحقيقه في بغداد الى رئاسة محكمة استئناف نينوى لتنفيذ اوامر القاء القبض بحقهم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/80241" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80239">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16897205e.mp4?token=N61BjKfqo6ryIBsnYtN32xM68r-flAr0zkEZuocdQwBF4eZyqWVc-J4Po59CvsASyNX6VHplYeYaGrfHXD4lk2umW7y2b8IojZmWFLpyfzFbu4KwQGB-KQ7pBSmClxWN4z9OIMFRi1ZLXb15jQvmT6aWl8T__8S96pvUsXp_zGh66qGjiWYMLMrk3wWs2GnH2wdiOsDMHXktCF8n7NzJX5FOZeNAmDm-IfztFotcRuV57ZiTihDaQr5p3818Dih2dg01U0HPgvmAk_QHJDZfP4CXLjgFU5RTHYbuCotiDfn3h3ori3Pv3OOHCUcNZeOlZltZQVdH5Qf-QMlmlk3M6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16897205e.mp4?token=N61BjKfqo6ryIBsnYtN32xM68r-flAr0zkEZuocdQwBF4eZyqWVc-J4Po59CvsASyNX6VHplYeYaGrfHXD4lk2umW7y2b8IojZmWFLpyfzFbu4KwQGB-KQ7pBSmClxWN4z9OIMFRi1ZLXb15jQvmT6aWl8T__8S96pvUsXp_zGh66qGjiWYMLMrk3wWs2GnH2wdiOsDMHXktCF8n7NzJX5FOZeNAmDm-IfztFotcRuV57ZiTihDaQr5p3818Dih2dg01U0HPgvmAk_QHJDZfP4CXLjgFU5RTHYbuCotiDfn3h3ori3Pv3OOHCUcNZeOlZltZQVdH5Qf-QMlmlk3M6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
قوات أمنية إضافية تصل إلى محافظة كركوك لتنفيذ عملية الإعتقال بحق مسؤولين متهمين بقضايا فساد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/80239" target="_blank">📅 19:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80238">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6992ed5645.mp4?token=Xl8Oce2gjptnFm5tfC8CBW7UZthe9AqMt_A7uk8WapYeGzxdpYZMFPizc6ECDfzZpHSyn9WaPAA9dJBEl0CWEx3KQGqV_6gQWtJpALkHK7T5XqgBktwaOSJJ82-fI3wiS8EEFV4HTaD-287cN4RiF50e4b312F1fpht9OqqZL08P2MQcbYBZ9xU0inJp3cI0c7ITg7jxuUo4rznB3a5Mya1eyazvxK-i16gfiSXQuZG9_naJsgjefh0e44MrWjT0XLjUc_UH8_6BlQZI-jnXAW2iSq4gcFJSGyYnwRfgPuLiUU5EsDAMlp8uUqU5scFFAtCJU3ZrQREJeoEJ8xjBsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6992ed5645.mp4?token=Xl8Oce2gjptnFm5tfC8CBW7UZthe9AqMt_A7uk8WapYeGzxdpYZMFPizc6ECDfzZpHSyn9WaPAA9dJBEl0CWEx3KQGqV_6gQWtJpALkHK7T5XqgBktwaOSJJ82-fI3wiS8EEFV4HTaD-287cN4RiF50e4b312F1fpht9OqqZL08P2MQcbYBZ9xU0inJp3cI0c7ITg7jxuUo4rznB3a5Mya1eyazvxK-i16gfiSXQuZG9_naJsgjefh0e44MrWjT0XLjUc_UH8_6BlQZI-jnXAW2iSq4gcFJSGyYnwRfgPuLiUU5EsDAMlp8uUqU5scFFAtCJU3ZrQREJeoEJ8xjBsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
آليات تابعة للقوات الأمنية تدخل إلى محافظة كركوك شمالي العراق، خلال عملية مداهمة وإعتقال عدد من المتهمين بقصايا فساد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/80238" target="_blank">📅 19:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80237">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
‏
السفير الأميركي بالأمم المتحدة:
صبر ترامب على إيران بدأ ينفد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/80237" target="_blank">📅 19:05 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
