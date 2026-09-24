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
<img src="https://cdn4.telesco.pe/file/Ajk7E5GyFxtzkZOO5l6amf1eOUKgWOf6uXKxusWlQMDZnJV5EmYZGxNu6RFXzWd6WVWXve4MJqpHWyV9puX-cg0g7uD87-LMO-JWm56RINiH19j8w1Y-llDdtlP45GSS_7edcreF-gvHDVO6WTixuP9x286U0X4AEtoYEmdEIbuCQnVn8PwGSb6Cbj0EFpwvr_5W4uOfF_auegDvV1FZpizrsm7TP7-Y6NyOpfWfZLNPpUw0Xblpzh9vh9EVciAgoYlL8GDwFvU3gN3ZUMOnDgtzgk-fqo9yqG0WlhmaAsfE3_cffIW4Zfz408yLmcpOLMERuYJnUiZs4BD6Zyuhxw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-91485">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
كتائب حزب الله تصف الشركات المساهمة في إحكام الحصار على إيران بلا كرامة وتدعو إلى كسره عبر  دعم المنتجات الإيرانية وتشجيع تبادلها.</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/naya_foriraq/91485" target="_blank">📅 19:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91484">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
كتائب حزب الله تصف الشركات المساهمة في إحكام الحصار على إيران بلا كرامة وتدعو إلى كسره عبر  دعم المنتجات الإيرانية وتشجيع تبادلها.</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/naya_foriraq/91484" target="_blank">📅 19:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3038b2edc.mp4?token=rxYclis4RbWm31IvC_xjQR6NoaDGW_-Iz4h6qRgQItaUV9AXD4qs7vNEK6tLD5NAsBdTl6nu9wI_uHcH24pFhkVdma79HPOzWo5OoBSF_V_9r-aF9gkTdaYN3xZKUueZX7XVCakxeAn6VA1bXNdVbB9LIAbax-LW2aeKu_3CznGKTreyqQnzSur35KrPZXoVVSwc7yGUMis1ScJXk3bzpgnOcEtwAOFSHSIxSbiEFwYgMqrBzSh3SFkEp_67ida-pr1nGQcbbpivva3EwWEh4Bv1E13PjatW67i049-HrbX2PFahIYWSAMW31vdGZF0u9Fj5_HIO_fp9ySu-MvsKAXT6W9YVvtGotYzg4wJpoLi4L8nwQ-WgktxYjm9rQV92-wCZ8PuSzcaxBv9qxra_HgJZr4Hk9cr5K5PV9eGacGvqkPxbJZu9pEHbvIuMO1Kqdxn1n7dRoHzsAsITQCSRJGM5BfOFglmfW5gseSQEE100cJVlP5RSKbbc_a44XihN6Bpg4T5vLULnqS_Qn4o0SaUj9V20JMn7KA2-4p1lkpi8pkbLfMKId2p_EjAPQJkjcJQ8dFAJdt_BSSUxLZz0sWfkWEn2w9UKSBYehUkpv6cmiQ0n_SsyUbjb6LSWwxxf0v7acPpcZ-N4pq9xMLEMkMw8ZKIjwjTm7lPwMPxtib4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3038b2edc.mp4?token=rxYclis4RbWm31IvC_xjQR6NoaDGW_-Iz4h6qRgQItaUV9AXD4qs7vNEK6tLD5NAsBdTl6nu9wI_uHcH24pFhkVdma79HPOzWo5OoBSF_V_9r-aF9gkTdaYN3xZKUueZX7XVCakxeAn6VA1bXNdVbB9LIAbax-LW2aeKu_3CznGKTreyqQnzSur35KrPZXoVVSwc7yGUMis1ScJXk3bzpgnOcEtwAOFSHSIxSbiEFwYgMqrBzSh3SFkEp_67ida-pr1nGQcbbpivva3EwWEh4Bv1E13PjatW67i049-HrbX2PFahIYWSAMW31vdGZF0u9Fj5_HIO_fp9ySu-MvsKAXT6W9YVvtGotYzg4wJpoLi4L8nwQ-WgktxYjm9rQV92-wCZ8PuSzcaxBv9qxra_HgJZr4Hk9cr5K5PV9eGacGvqkPxbJZu9pEHbvIuMO1Kqdxn1n7dRoHzsAsITQCSRJGM5BfOFglmfW5gseSQEE100cJVlP5RSKbbc_a44XihN6Bpg4T5vLULnqS_Qn4o0SaUj9V20JMn7KA2-4p1lkpi8pkbLfMKId2p_EjAPQJkjcJQ8dFAJdt_BSSUxLZz0sWfkWEn2w9UKSBYehUkpv6cmiQ0n_SsyUbjb6LSWwxxf0v7acPpcZ-N4pq9xMLEMkMw8ZKIjwjTm7lPwMPxtib4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇺🇸
استعراض اميركي خلال حضور الرئيس الصيني في الولايات المتحدة.</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/naya_foriraq/91483" target="_blank">📅 19:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91482">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz-NPL_PkrVGHFI14SpZ6IFs_fJt6uQMOeasAeVgsNe_KetRDfWGhpJ-M6tM4Byo0pJywLGEdvG2M0_OruGbw8uQ3yCsBzcQ2XBdjOzo1JLDflK5X3Mikh1TzasQGBE8VcZNS5STdhs3SjBLOchQA9T5OQ-P5foPrtRZpq8gEHrny_BcwsmRTQwKwIWMaZqjkdS59hQKUa2ilAgHNiXEtJ8y69mz5dwVXjcF7TAwiMGge9HBUArjqO5AMp98Dz_RRBn5sedO4237os94ZWIW-9A1KwFHViAKatr22or3JdYBI8KjKEaWxhptch_NXilWXsepUr-LPaPhl3hCGi6Dhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
انفجار جسم مجهول اخر في سماء العراق.</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/naya_foriraq/91482" target="_blank">📅 18:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91481">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
🔻
تعليق رحلات شركات الطيران الإيرانية من وإلى الإمارات بدءا من اليوم وحتى إشعار آخر.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/naya_foriraq/91481" target="_blank">📅 18:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91480">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAETkI0-uItNjAkXCl7w_4SKp4JmjVbAiqKnn8ei1lCuvF9y2oOtrLA-g-PTmIMmd9RERgSkIorVPRulqX9U7fOmBsoAgtWWIwgEW0JVySnyURu-gNIzyOAnh4-V67uP8-j7zuWOFBun01RgVFu8gOC1tIDzgCbpS_0ursf_0X49Wf9mqzw1SDeU7RRAjdJmPMeRghKp4DBI5eK6uGqD9ngHjhp-fYeIXVSBct-_rKG6u35UIv18xFyj48v-wMiba5wnx_KmgCFjkkk9sT0AOMwSs0XHVME7WzCE7srkt_SQiE3qmCH3hD6zLUIKCo3-B1w_9_O6a1LJg9bcTN9LjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إستمرار إرتفاع أسعار النفط حيث تجاوز سعر البرميل 106 دولار.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/naya_foriraq/91480" target="_blank">📅 18:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91479">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بيان مهم للقوات المسلحة اليمنية في تمام الساعة 5:50مساءً، بعد قليل.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/naya_foriraq/91479" target="_blank">📅 18:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91478">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بيان مهم للقوات المسلحة اليمنية في تمام الساعة 5:50مساءً، بعد قليل.</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/naya_foriraq/91478" target="_blank">📅 17:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91477">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏رئيس السلطة الفلسطينية محمود عباس يبدأ كلمته في الامم المتحدة عبر الفيديو بعد عدم منحه تأشيرة للمشاركة في اجتماعات نيويورك</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/91477" target="_blank">📅 17:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91476">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
تبادل وزراء الخارجية الإيراني والأوكراني وجهات النظر حول كيفية حل مسألة الهجوم الأوكراني في يوليو على سفينة إيرانية في بحر قزوين.</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/91476" target="_blank">📅 17:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91475">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇱
مسؤول صهيوني:
إسرائيل تتابع الأنشطة الإيرانية في منشأة تحت الأرض بالقرب من نطنز وتقدر أن جولة جديدة من القتال قد تحدث مع الولايات المتحدة او بدونها.</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/91475" target="_blank">📅 17:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91474">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qfpc_3CpYugO6r4rjSvGQXmX4kcZ3DB-4iQbaXbkkoMYDj4CGYxArvG5wH-17gi-hy-Qlf6WnP1yLhmsO3B8VPe2IdkjN3TofUoeU-qtDZAZzC9uvTQUMqkYNJDWBwN4ec8dWNp2Wsl6yfEJ5fpxn9nqJkT8-CbND7KVPTkm4AYyC00ZrcZSU6o6aqQTAwvwQgMoOzhwOuDo4m06yooHQH2HYjHwvktD4YXwtX2yQbJBRMBJoqv5IR9BeFgiNAjCVVdbhyv-Fghnadw3iXVzXlwDz2TV2NbBiiHxsPcOXy__6Sxle83urZPcn-P6tggCm9JHNtGKzKuRKpn2nha2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحشد الشعبي يحبط مخططا ارهابيا لاستهداف مواقع عسكرية في محافظة الأنبار غربي العراق</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/91474" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91473">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سماع دوي انفجارين في مضيق هرمز</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/91473" target="_blank">📅 16:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91472">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">يمنيين يقومون باسقاط طائرة مسيرة سعودية بواسطة الحجارة في مديرية مران غرب محافظة صعدة.</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/naya_foriraq/91472" target="_blank">📅 16:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91471">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a96ab0f7.mp4?token=W2VO56IEL8j8bxmMN--lsTmfqoivCWfoSURQKchAHjMkexwpCUgjoGD-t8wdOKLu-HnjC9bKEZEjzrm_BjlHATioaK22Hfl3GAYM99KsYOF63XX1GqwUqEMIYDPV-Ev4QGXJNGb_26C54Sh17RAvfuTlhpQCobXMczhwik0K41aTGV2nyJMahmLjVf0fVCAOpPohqpasxq6-SunnnGczvGoJYiRYJ7Zx0YFdZqFnNQx0_mSM20I1JAEkNUBhptJrXxfhH8AZhhd9IsNDTW8P0iJ1iAoidpfAsIOPFgerVUAFtHgjOrPGqMHmbSEdGkXodR0gk6ICppqk68RHke-zGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a96ab0f7.mp4?token=W2VO56IEL8j8bxmMN--lsTmfqoivCWfoSURQKchAHjMkexwpCUgjoGD-t8wdOKLu-HnjC9bKEZEjzrm_BjlHATioaK22Hfl3GAYM99KsYOF63XX1GqwUqEMIYDPV-Ev4QGXJNGb_26C54Sh17RAvfuTlhpQCobXMczhwik0K41aTGV2nyJMahmLjVf0fVCAOpPohqpasxq6-SunnnGczvGoJYiRYJ7Zx0YFdZqFnNQx0_mSM20I1JAEkNUBhptJrXxfhH8AZhhd9IsNDTW8P0iJ1iAoidpfAsIOPFgerVUAFtHgjOrPGqMHmbSEdGkXodR0gk6ICppqk68RHke-zGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يمنيين يقومون باسقاط طائرة مسيرة سعودية بواسطة الحجارة في مديرية مران غرب محافظة صعدة.</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/naya_foriraq/91471" target="_blank">📅 16:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91470">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg9kdbtQAf25FOriYr_p7Hgi15HeyyfCvXpURZr61_8Y3fGsUD14nPpUdJcQMLQgB9bXAIytG02MmzNVvthAFcUV22PmcKTIeYrtqTke8lZ9mChCKKROv3IkYfIHEDQP3YTd60rb7BXysY3qqdthnVDyZ9aaR38vAPD2hRbTfcu0V1P6Y-oZ4R7dWzZlht3_4zblQSn4iKTPMdCmwjUAFEK_Asm0efRHglxpp8MIMLeA_PzhvFRG-UpxClQbAz4fagM3h9czYVjKotQWcVfvUPIH-ChURwEDqGaC24_5IRK-CjhuDAK9lxhZZayHa9hfe4r4kUQ8h5SBgXpbcPX2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
صواريخ يمنية تتجه لدك القواعد العسكرية والاصول الاقتصادية لنظام ال سعود.</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/naya_foriraq/91470" target="_blank">📅 16:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91469">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇾🇪
🇾🇪
صواريخ يمنية تتجه لدك القواعد العسكرية والاصول الاقتصادية لنظام ال سعود.</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/naya_foriraq/91469" target="_blank">📅 16:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91468">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLuC2-xWME4JSpGYv5IQhXTK7us2TmwrRBgK4t63E9buK6Xy6jKyUGZR5rj21i-cv6CQDIIpbIJamOsUaxoX92J1-RX1197LfD9wa1CfWUcRAb3OEQUReVcm-QdOxrAGsn5jlPVUvbegR8Npj01bLx7u_Z7kG20hnqa9dgExTmkZLP081JmUnBCTMLToYIc120I9r6PlnAEjyXwMvtPPiMeH4L4lQEmuc9GDGLAAlkVEiZEeutv7HbaDluYmHL9hoRYRv3-gQPdz56zmyXkFZAu3ZKkd4hioFKx5Mzk-hb5PBUKzplm8O-D_JBd0bOcMGaksOW6-7A_s6CXGef5eGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتل رئيس المجلس الانتقالي الجنوبي (جميل أحمد الأغبري) الموالي للامارات في مركز هجرة بمنطقة الأغبرة بمديرية المضاربة محافظة لحج خلال مواجهات مع القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/91468" target="_blank">📅 15:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91467">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
وزارة البيئة العراقية تعلن حالة الطوارئ البيئية في العراق بسبب تلوث الانهار.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/91467" target="_blank">📅 15:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91466">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgMt49OP_Q7BBCKlcxKQPJpHggSLOhpeehRGiuWWVNGkUI2uBfwlwvyIglLTzvch1tiTgFCG8yU78S75Mf4HUeRFAQ5BUvkD7QW5NXenICp9QC-fXGvqxXEb0bQ5Ud3i7h19_wK3otVhI0cqKY_winD3NyOKhW5LLUhgB9yskLwHr4wgPLALcL-eBwdPt5GmGApr7m_3aK51fOWExhO4XzGG7pfR-5yehVZ5-6kZYxqHRi54RI4coOU6YP-JNkhH2BZsGVNGJModQKYfbSSAkqVeHJmgZLCwFLTAUmMnFdHAk4oCUI1Sr_7xieEwffiXGcTMON48CIOoy525ItU0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
عصابات الجولاني تكلف الارهابي محمد صبحي بمنصب مدير قسم الإعلام الرقمي في الرقة.
يظهر محمد صبحي وخلفه عدد من الرؤوس المقطوعة رافعا سبابة ما يسمى بالتوحيد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/91466" target="_blank">📅 15:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91465">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الانفجارات سمعت بوضوح قرب سيطرة دار الضيافة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91465" target="_blank">📅 14:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91464">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سماع دوي انفجارات بالقرب من السفارة البريطانية في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91464" target="_blank">📅 14:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91463">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سماع دوي انفجارات بالقرب من السفارة البريطانية في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91463" target="_blank">📅 14:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91462">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d249860dd.mp4?token=Oaj2C3eJMIzveZQALQofjRZ9jX2Wv7zZV0KXNqlAeOFRLamuq-UnBsO2hXT3o5dYj5Xb2A7J5bLO4cf4pOqhw42Q7gU0fXeKKw7DIUbuCnope5FmBn8dOb8acQDYiggmggQxeqdiSI_SbA4FgZB-RW8hntQ8-JOqLcuGbxCh5i35QbYOqSWDfVzYJQzThq3pqxdMHE2UtYGruGvDBNvJ7mBA5BWJQz-NtBuN6Jn7OhZQupSy8BYOqU4Tm2Yuxqft_PhJI_9DXmE7nccd6xCn62bzJRekPCN1WhqjPxH1uafafSWnEi9byFxDrk-LtfBd3zhfgSVXq1I99PHOFoRSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d249860dd.mp4?token=Oaj2C3eJMIzveZQALQofjRZ9jX2Wv7zZV0KXNqlAeOFRLamuq-UnBsO2hXT3o5dYj5Xb2A7J5bLO4cf4pOqhw42Q7gU0fXeKKw7DIUbuCnope5FmBn8dOb8acQDYiggmggQxeqdiSI_SbA4FgZB-RW8hntQ8-JOqLcuGbxCh5i35QbYOqSWDfVzYJQzThq3pqxdMHE2UtYGruGvDBNvJ7mBA5BWJQz-NtBuN6Jn7OhZQupSy8BYOqU4Tm2Yuxqft_PhJI_9DXmE7nccd6xCn62bzJRekPCN1WhqjPxH1uafafSWnEi9byFxDrk-LtfBd3zhfgSVXq1I99PHOFoRSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في محافظة درعا السورية وانباء عن عدة قتلى وجرحى</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91462" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91461">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بلومبرغ:
وافق ترامب والرئيس الصيني على تمديد فترة الهدنة التجارية حتى 10 يناير 2027، وتجنب التصعيد على الرغم من الخلافات حول المعادن النادرة، والقيود التكنولوجية، وقضية تايوان.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/91461" target="_blank">📅 14:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91458">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇸🇾
انفجارات تهز محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/91458" target="_blank">📅 14:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91457">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al0aNCdgkt8L7HkkEee-QvjKebX2A_OYNRNgptAJutxXqUaGyU-FbSWPEt7MkCxnhQ3MYXeyoTOkjjhU9eLb4aoXZocfXpXDVWMjjpESU7ASQF-pP_Tt6vDbVWjBDapmqxc4yUYmGMqjT2eBev1aZVA0p1P5p8fm3ANXL9tsZ-XAPW4vnrQ8uge1gneu7126517J7OCORbnjWaM_TDgT2w4GRAiLO9PSNpNP_SRMLsFruZAWo_RvMo8jppWstuyDWs6tWWqV7Cw15R8lYPKXLZcNslYN0NVV0Rapn-RYpKDfneEdhKqg_QvtylC6bKiMEhGuyLdfw16eN_kQL0tgKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
عضو انصار الله حزام الاسد:
‏ماذا يحدث الآن داخل القواعد العسكرية السعودية ومنشآت أرامكو؟</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/91457" target="_blank">📅 14:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91456">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجارات في جدة</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/91456" target="_blank">📅 14:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91454">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFsZC76967CKoreOAK3tX17qNvifYACmWbr-walkDmp-Exuq-Yh_HDTpWcqyfEY6USwZhb3ePvaJEbI7jsJ05a6l09TSIA2QHY_KD_ZCyxSnSWgC9ulSqVJbit_2jwEmzdY4qUevRDuBsB28WCHaCsRCGUh_gbOYwoBkvvuB0fW1WHkkX2HnNPOOIxfZktT58JYcqLWQxY1p1xipU-RCoyN-TTcb0iNbE_cIvGC6eZnFiLUWJ4iliKRRVPFzf8rjJt5ymeP0WrLo-ivtO9UWxuUplmXfsLc61vtfNajJ14dkHD-GzFnGB8aykfzBPmm6QvMMSUlm3TSlUv6Qnn-XfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yw-FVn3gty48Pc5RkGwClHGd1ibmdUS2PNlVVSAg6dLYV8JWmNRc3QuA9KJM7g3tPKYCp0q6fy9f1KUYyl-JedDYKHHOj4VsyJcv6h769zkN9BsI_ACOS4795W6bCqbPvLvyaWwxvt4IlIjPEtIGCuaB9iDJBFtAyOgoMxxGRSfNR2PZ-i-0uwg_t0j-Liin_C08hps3HSyNao-xiW_ZrG6iaKNZ96ira5kPjuUGbA9DtN9ys1WmgeRG8VZhCfMvPmDz5NQTBFRznc_rHia41vRmP3bdDGiWwq438Z3xTsDKKWR_iiqG_R7JVQ7f5R10OrGPjYUow1jaQyMqn-7oEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لحظة انطلاق صواريخ انصار الله لدك العدو السعودي وقواعده العسكرية</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/91454" target="_blank">📅 14:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91453">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Br4v9XmBGOq4VJokpG1Vdi1SboNN7p5pPvOVUNRXGtViLTafebUI2Q0YCD-HKxsfwtdK2DuOiP-4Mu7eibot0eAk59y6Fzn7c_8Frn_ju6ZgmaWTAjF7gE6BmzbH1RrPuVbQI-5qaSFSbdw8HNzuBtqAQZ4Th7ueT8ioy7qs6UVrxXLvnORkbLR7wI59VJc7trVVdqG8qmqXLq2FNVx1BWxYR0zB7PAnESuwBj-F3KWff5vakDp3rR4i-PHMcVJTY659X9Na8LvD9l3hMV1hkpPpgfXX2AUi7HKt9v3ltvGeXk1MAZ6qm-jrcSyxwTaVc5-bTI-nAP1YkkR903xe0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف ميناء ينبع</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/91453" target="_blank">📅 14:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91452">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ينبع تحت القصف</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91452" target="_blank">📅 14:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91451">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">القوات المسلحة اليمنية تدك القواعد العسكرية والمصالح الاقتصادية لنظام ال سعود في مختلف المناطق السعودية</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/91451" target="_blank">📅 13:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91450">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تبوك تحت القصف</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/91450" target="_blank">📅 13:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نظام ال سعود يكرر الكذبة مجددا: تفعيل الانذار المبكر في مكة المكرمة</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/91449" target="_blank">📅 13:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجارات تهز الطائف</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/91448" target="_blank">📅 13:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجارات في جدة</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/91447" target="_blank">📅 13:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91446" target="_blank">📅 13:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91445" target="_blank">📅 13:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91444">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
أمين مجلس الأمن القومي الإيراني محسن رضائي:
تصعيد أمريكي جديد قد يفتح جبهة ثانية في باب المندب إلى جانب هرمز.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91444" target="_blank">📅 13:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91443">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔻
رئيس المخابرات الدنماركية:
لا يمكن استبعاد غزو روسيا لدول حلف الناتو .
من المتوقع أن تزيد روسيا من تصعيد حربها الهجينة ضد الناتو والغرب في الأشهر المقبلة.
روسيا قد تستهدف دول اوربية بمسيرات مزيفة و باعلام أوكرانية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91443" target="_blank">📅 13:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91442">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7554bb0c65.mp4?token=qe2l2cKsRgMACyIj5Ui2X6ENTgdsgOSh5M_JmS52UO2U3BdIkyB-MerTnS6vWwvjl6F92sDIQsKJPpIuZB5iJ5rHOr8ikIRIFfxv1oOZDrJqK9-Qkq3vbERygaxmI3R4hfYMGK-zfmnEsXQApqYXfR4hZILAXZCuDRWGX2ERvL3O8R1noLVxDvl1vy0TIo3GiHKbLgUIt6urwA-_wepqnC5rxhDyyPcNRP2mkEwbBsYfciR76Lm6yh4dYVP8PDlg4xdwEM6SYwIdDuZwo7zk-a-m24T7_jW2iyToeC_zMnrhTOhKng90_JiRGbewTPF0wkJCNEqoDyB1jDvAvoP_fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7554bb0c65.mp4?token=qe2l2cKsRgMACyIj5Ui2X6ENTgdsgOSh5M_JmS52UO2U3BdIkyB-MerTnS6vWwvjl6F92sDIQsKJPpIuZB5iJ5rHOr8ikIRIFfxv1oOZDrJqK9-Qkq3vbERygaxmI3R4hfYMGK-zfmnEsXQApqYXfR4hZILAXZCuDRWGX2ERvL3O8R1noLVxDvl1vy0TIo3GiHKbLgUIt6urwA-_wepqnC5rxhDyyPcNRP2mkEwbBsYfciR76Lm6yh4dYVP8PDlg4xdwEM6SYwIdDuZwo7zk-a-m24T7_jW2iyToeC_zMnrhTOhKng90_JiRGbewTPF0wkJCNEqoDyB1jDvAvoP_fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تتمكن من دحر مرتزقة السعودية وتفرض سيطرتها الكاملة على خط تعز عدن.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91442" target="_blank">📅 13:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91441">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇸🇦
عقب الضربات اليمانية..
‏
رئيس أرامكو السعودية:
وضع الطاقة في العالم سيزداد سوءا لأن الانقطاع كبير وليس محدودا.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91441" target="_blank">📅 13:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91440">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
منظمة الطيران المدني الإيراني: بسبب عدم إصدار تركمانستان تصريحًا للطائرات الإيرانية للمرور عبر أجوائها، لم تتمكن رحلة الطيران من طهران إلى دوشنبة من الوصول إلى وجهتها، واضطرت إلى العودة إلى مطار الإمام الخميني في طهران.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91440" target="_blank">📅 13:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91439">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
تماشياً مع القرارات الأمريكية الظالمة.. تم إلغاء رحلة شركة "وارش" الجوية من طهران إلى "دوشنبه" عاصمة طاجيكستان، وعودتها إلى مطار الإمام الخميني، بعد أن مُنعت من إستخدام المجال الجوي لدولة أذربيجان.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/91439" target="_blank">📅 13:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91438">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
المساعد والمستشار الأعلى لقائد الثورة الإسلامية "اللواء صفوي":  نحن مستعدون لمرحلة جديدة من الحرب المحتملة مع الولايات المتحدة.  قواتنا المسلحة تقوم بصياغة سيناريوهات بذكاء، وقد أعدت خططًا للأسوأ من السيناريوهات، بحيث إذا هاجم الأمريكيون والصهاينة مرة أخرى…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91438" target="_blank">📅 12:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91437">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399dabb06c.mp4?token=KRQB4RXc8lmG7ma2-hGS5sKrOv4dZ7ijUX_5yCSdTB-lK5dye7EFhSrwtnZvi5MZoNWegJ57sg5g2Ggzpex-57m5zvohfZDJExGhmjgrcf6yLr725xhtXMBqbEPZQGhSUWRZVkTg2hgSlst9FaoyVoSiqMStCM0jMZNsSWllviCxT0FK5jhQdMskC7clgTLMTwHwT_mNQFrChqd5Fpwe0skeTSVp8pKfIaO7ZRzI5Rdd3iNnV0GIVh2JOvncLYHjreKWf2dyVH8CYOhbmGK0UUM9eEFQTn8L8967-TMNU1PfnOefZISyCxzbhTY60-RByLH2u14tG0M2r8_R45Wx1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399dabb06c.mp4?token=KRQB4RXc8lmG7ma2-hGS5sKrOv4dZ7ijUX_5yCSdTB-lK5dye7EFhSrwtnZvi5MZoNWegJ57sg5g2Ggzpex-57m5zvohfZDJExGhmjgrcf6yLr725xhtXMBqbEPZQGhSUWRZVkTg2hgSlst9FaoyVoSiqMStCM0jMZNsSWllviCxT0FK5jhQdMskC7clgTLMTwHwT_mNQFrChqd5Fpwe0skeTSVp8pKfIaO7ZRzI5Rdd3iNnV0GIVh2JOvncLYHjreKWf2dyVH8CYOhbmGK0UUM9eEFQTn8L8967-TMNU1PfnOefZISyCxzbhTY60-RByLH2u14tG0M2r8_R45Wx1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدث امني خطير في محافظة الانبار</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91437" target="_blank">📅 12:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91436">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حدث امني خطير في محافظة الانبار</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/91436" target="_blank">📅 12:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91435">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685d72f92.mp4?token=YM5diDg7jPYamIVM0ih3F0g0YPZf6KMNUudzfeRuCkShEI0Y6JUOws_BRZBkQqYiSv9GG00yhvH9w-MMhl2vg0-GGjHriaAgompV7ngIygrcrgoohQu16S6MTappxHsj72RO2_S-rLMHjvB0fxUPyhNMjAiBNpUvYiNYCyzgrtmiDjI2JCXfpiGCjjXcuD95mijGOU4JF1ZPORlE6ew2bAOLT3vxjnX5aGFsocT3zEFLDnfZD-6E5IofZn4gDqzAY-QVUPWHdnpybbHmVO3l1DRAhNMCOnCvO1lIP31Tr-0SeLKUe6w3LKxt0RXLLRf2ZskyhuOPx6SwnLbbrDzsA0qaMg9xzedko_v2fF0IwT9Yec5V1w1eway2MeKGdeBlhntJY7aOXHaIsmwm3nYGCimp3ltQbpjKMTWUjNMbui5N02fc0MVr-8_cRrwfXRB2sc59n56bXyDQ1AZBGjg74sXFcgkPIw_v7b5QCeL9qVqeizk0REFNnCye99Mqq7J-d_jM-JCEjKC9zc7iFABgAYLSdiBXZj049wmwUMH2t16i0im5rZcsKhK9I1yF2yd5GlTf6slDR5iCfrVRgRp5m29IUhOonO28Iw8-tRaRy0ySkuEZRwqInJ1oEzDTIGcc6NNCUbWnco4tC5rwN2rYieFkE6Qfok6onwRr0rmBifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685d72f92.mp4?token=YM5diDg7jPYamIVM0ih3F0g0YPZf6KMNUudzfeRuCkShEI0Y6JUOws_BRZBkQqYiSv9GG00yhvH9w-MMhl2vg0-GGjHriaAgompV7ngIygrcrgoohQu16S6MTappxHsj72RO2_S-rLMHjvB0fxUPyhNMjAiBNpUvYiNYCyzgrtmiDjI2JCXfpiGCjjXcuD95mijGOU4JF1ZPORlE6ew2bAOLT3vxjnX5aGFsocT3zEFLDnfZD-6E5IofZn4gDqzAY-QVUPWHdnpybbHmVO3l1DRAhNMCOnCvO1lIP31Tr-0SeLKUe6w3LKxt0RXLLRf2ZskyhuOPx6SwnLbbrDzsA0qaMg9xzedko_v2fF0IwT9Yec5V1w1eway2MeKGdeBlhntJY7aOXHaIsmwm3nYGCimp3ltQbpjKMTWUjNMbui5N02fc0MVr-8_cRrwfXRB2sc59n56bXyDQ1AZBGjg74sXFcgkPIw_v7b5QCeL9qVqeizk0REFNnCye99Mqq7J-d_jM-JCEjKC9zc7iFABgAYLSdiBXZj049wmwUMH2t16i0im5rZcsKhK9I1yF2yd5GlTf6slDR5iCfrVRgRp5m29IUhOonO28Iw8-tRaRy0ySkuEZRwqInJ1oEzDTIGcc6NNCUbWnco4tC5rwN2rYieFkE6Qfok6onwRr0rmBifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تماشياً مع القرارات الأمريكية الظالمة..
تم إلغاء رحلة شركة "وارش" الجوية من طهران إلى "دوشنبه" عاصمة طاجيكستان، وعودتها إلى مطار الإمام الخميني، بعد أن مُنعت من إستخدام المجال الجوي لدولة أذربيجان.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91435" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91434">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔻
إل موندو:
الاستخبارات الأمريكية حذرت عدة حكومات أوروبية من أن روسيا قد تكون بصدد التخطيط لعملية باستخدام الطائرات بدون طيار ضد إسبانيا أو فرنسا أو إيطاليا.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/91434" target="_blank">📅 11:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91433">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvedUod5-0qpjMsUieRvUoU3BoIGvNjmGDE66VNDbzqgXyF2sfkVXvnIj-1iel6yQjoq1_0EfNRoLwcxKbF2WALu9jny1ZvpSbUqQC-ta6MO3-hfPkM7WCxJxhy4yJqTtOmTAN3LeI9OERagnQ-M9DjbdRfWttfSS3qAlPPk6ZpZEusRgTGLPWIG5zXbGucdphgQg2dNE-g-l4Ks_EuTOoKxENgQol4SHsNrC2Z9qR5Z54kDs6pYX-w35j8pMZRYx-X9bRLR8St4xXl3iMpDVTyOXRAkCkjYR-sFvkcHhuk1V3ep6TuAZkaZKofyO92jmKzj9vYBXKF7TAgTfuPepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية ترتفع إلى 105 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91433" target="_blank">📅 11:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91432">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رويترز:
اندلع حريق في محطة أرضية لشبكة "ستارلينك" للأقمار الصناعية في منطقة ماسوفيا ببولندا، مساء الأربعاء.
وكانت هذه المحطة توفر خدمات الاتصال لبولندا وأوكرانيا، بما في ذلك المستخدمين العسكريين الأوكرانيين.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91432" target="_blank">📅 11:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91431">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkztPNBLvccWUj0cEV5p5MkE9vWL0uoqx5wVl_DBzw6Ryt4OPKTSLJ_dmLril11vJenmd4-yz18M5Qj34TngQY5wdCnjCUkjw8KM1lSCA2NrPeqdrP-5wDMsyf1toBhGaG6kOpdV_JeX0JYDKiOQpd7M4yqpAKxh-f8maGWRzoT-nb8qFfLGlqv-030xtizRGQr-XR5uFuPpanz0h_PkfHRDOcYCE8DsxFkuV-r-sXA85RvTlWhUrSQzcdEmeu3V28d9T_LH8CkU_ed7RMufTWi_tCYw32CFYcLIvmo8yP6iwC9Szy5tarMrtAQEtKTrCjNeGyrFynbR6gkdNuF2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية ترتفع إلى 105 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/91431" target="_blank">📅 11:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91430">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇹🇷
هزة ارضية بقوة 5.6 ريختر في تركيا، شعر بها سكان الشمال والشرق السوري وبيروت ومحافظة دهوك العراقية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91430" target="_blank">📅 11:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91429">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1bde9216d.mp4?token=CsOVirZsM765bUT7K2tpDmEChqBvPZDP6m2C0JKFDd-t81a3haAIRYFy7lbt2yDueRQoWGIWAmLiqLG4XHIAVoh_zcYKblp5ZKdxxXUpqKmBPSX8CaM6tnEvHxgWAss__1RCPmtV2PQHUp2hFwqQSRRlV98wjb9shHa1HahDfBIoI10Hj3-sbm8MPLuhrOSFszRnkAjjjPlTPIZMEdZjGag9M9u3NrSfOwKpi4NDIHucgjMunFUT_3ggaDX4PJD1e3Y24YKMfW1Rz_0qBaglhiv6eASA7BJedOXn27zeV7z8KnX6uQqW_fsdnfRyrTZN0tJNuxfsoZ_y8io0f4K45ocUGePHQTUre1WXgyEXmsh_7wHTYgUYF1O-f72FSKtyKebYJezZRv6uJ40PXNMdjYewODyP6GjHPXh222QIOYqPJ81WPIFzSt9hPGSGKRy6-OcuHaOLZADqlgGpVi-qQLfQ1SZTNi0nGiWKPRp73h_GkpBN6lzDPSCwkuVoKPX_bhrln4kK9eHBGK4-BDVxnI8hHfhKP-IWJYrreFuW8szqwBrA-l1kBh1g5lXMZPPOXo24iJDybPRaMJxe4b3hN6Rg761ZbU69thM9CQ0JvjQQ4fjsc3_I-DAutTv-HwQkLUg9KIldnJJ_0-TtlCrYR11XzbnhiaxNQQQOYvX2opA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1bde9216d.mp4?token=CsOVirZsM765bUT7K2tpDmEChqBvPZDP6m2C0JKFDd-t81a3haAIRYFy7lbt2yDueRQoWGIWAmLiqLG4XHIAVoh_zcYKblp5ZKdxxXUpqKmBPSX8CaM6tnEvHxgWAss__1RCPmtV2PQHUp2hFwqQSRRlV98wjb9shHa1HahDfBIoI10Hj3-sbm8MPLuhrOSFszRnkAjjjPlTPIZMEdZjGag9M9u3NrSfOwKpi4NDIHucgjMunFUT_3ggaDX4PJD1e3Y24YKMfW1Rz_0qBaglhiv6eASA7BJedOXn27zeV7z8KnX6uQqW_fsdnfRyrTZN0tJNuxfsoZ_y8io0f4K45ocUGePHQTUre1WXgyEXmsh_7wHTYgUYF1O-f72FSKtyKebYJezZRv6uJ40PXNMdjYewODyP6GjHPXh222QIOYqPJ81WPIFzSt9hPGSGKRy6-OcuHaOLZADqlgGpVi-qQLfQ1SZTNi0nGiWKPRp73h_GkpBN6lzDPSCwkuVoKPX_bhrln4kK9eHBGK4-BDVxnI8hHfhKP-IWJYrreFuW8szqwBrA-l1kBh1g5lXMZPPOXo24iJDybPRaMJxe4b3hN6Rg761ZbU69thM9CQ0JvjQQ4fjsc3_I-DAutTv-HwQkLUg9KIldnJJ_0-TtlCrYR11XzbnhiaxNQQQOYvX2opA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
المساعد والمستشار الأعلى لقائد الثورة الإسلامية "اللواء صفوي":
نحن مستعدون لمرحلة جديدة من الحرب المحتملة مع الولايات المتحدة.
قواتنا المسلحة تقوم بصياغة سيناريوهات بذكاء، وقد أعدت خططًا للأسوأ من السيناريوهات، بحيث إذا هاجم الأمريكيون والصهاينة مرة أخرى مراكزنا ومصالحنا الوطنية، فستكون جبهة الحرب أوسع هذه المرة.
الآن، بعد أن امتدت الحرب من الخليج الفارسي ومضيق هرمز إلى البحر الأحمر، قد تتسع هذه الجبهة في المرحلة التالية من الحرب المحتملة (مع الولايات المتحدة الأمريكية)، وقد تمتد إلى المحيط الهندي أو أماكن أخرى.
حركة أنصار الله لديها أهداف واستراتيجيات خاصة بها، وقد حققت تقدمًا كبيرًا في مجال إنتاج الأسلحة. أعتقد أن الربط بين الخليج الفارسي والبحر الأحمر، ومضيق هرمز ومضيق باب المندب سيغير مسرح الحرب.
أود أن أعلن هنا أنه إذا بدأت الولايات المتحدة حربًا جديدة، فقد يظهر أمام أعينهم مسرح (جبهة) جديد يتمحور حول البحر الأحمر ومضيق باب المندب. هل هم مستعدون لخوض معركة في هذا الجبهة؟ هذا سؤال يجب أن يولوه اهتمامًا أكبر.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91429" target="_blank">📅 11:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91428">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eb871e3a.mp4?token=K3LTCfJi9pmW5N_FkXivBmz0UgS4JneBaJwSW1WS7C9kt2jKtgxq09wE6MnzwCsFtZdpiUdBxCM64Sp0JLUESGCMogAHsrh9qkiaVvLGG-eJs5VkKy-e_C9cJnjsMwk_XTGk1xBzIWwDQD9wTJMZqoWOay6DBe0MzHzXjMNa6ZmsPwKnajDW0VjViwCeX2aUyUpcp6q_3SjZAM7UjjlIAPRNgrPGAhdjnaNyGLqH41P6cX0R4R_tPCk6x7yiNcw7FlckPOf-GNGG9dKBE_7-oRHrYfVJDHBlX4l5jooL7sNdxb0R59wYJZD4Y8qaLyK4ExsgFBTOm4xEBwPR3e60Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eb871e3a.mp4?token=K3LTCfJi9pmW5N_FkXivBmz0UgS4JneBaJwSW1WS7C9kt2jKtgxq09wE6MnzwCsFtZdpiUdBxCM64Sp0JLUESGCMogAHsrh9qkiaVvLGG-eJs5VkKy-e_C9cJnjsMwk_XTGk1xBzIWwDQD9wTJMZqoWOay6DBe0MzHzXjMNa6ZmsPwKnajDW0VjViwCeX2aUyUpcp6q_3SjZAM7UjjlIAPRNgrPGAhdjnaNyGLqH41P6cX0R4R_tPCk6x7yiNcw7FlckPOf-GNGG9dKBE_7-oRHrYfVJDHBlX4l5jooL7sNdxb0R59wYJZD4Y8qaLyK4ExsgFBTOm4xEBwPR3e60Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
إيران والعراق لايمكن الفراق..
العلم العراقي يرفرف في مناورات "فدائيين إيران" بمحافظة خوزستان الإيرانية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91428" target="_blank">📅 10:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91427">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
إنفجار داخل مقر لإرهابيي المعارضة الكردية يشعل سماء قضاء سوران في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91427" target="_blank">📅 10:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91426">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇱
🇹🇷
وزير الحرب الإسرائيلي مهاجماً أردوغان:
"أردوغان هو سلطان على الورق، قوي في خطابات التحريض المناهضة للسامية، ولكنه ضعيف في الأفعال. أقترح عليه أن يتوقف عن التدخل في شؤون إسرائيل. دولة إسرائيل قوية وتعرف كيف تحمي نفسها - نحن لسنا الأكراد الذين يتعامل معهم بقسوة في تركيا، حتى في هذه الأيام".</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91426" target="_blank">📅 09:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91425">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔻
‏
وول ستريت جورنال:
1300 شحنة بمكونات صينية مزدوجة الاستخدام وصلت لوزارة الدفاع الإيرانية.
‏شركات صينية زودت إيران بمواد تستخدم في إنتاج الصواريخ الباليستية والمسيرات.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91425" target="_blank">📅 09:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91424">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇹🇷
🇮🇶
رويترز:
تركيا توافق على تسليم معسكر لها للقوات المسلحة العراقية في شمالي العراق.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91424" target="_blank">📅 04:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91423">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f26b235d.mp4?token=HCu0Ha4UtKSAWlNrDqQaZK9NWEgEnWQhRkWchBdBtqYjiTs4tycDgvVhFGh7mElgjI_5bnwB1b9vgty-V7IpYy1ssyHNUuYzqL0Gg5VqaheUXcVSy9dkvygZzO0jfAAVYx68HuQ15wv09g3Nh9VXvVaNJ2dvkvHc7ZoSo9A_kjBTcKRy7iIMaxSyuIiyx2u5nfhGFPWseUVBRh8Y_m2Evy5UbuILSw-3c3l6_IK54_4HXdmrCwsnVN10FidGnDJf0ZPsv4JTANH63brrcLaGHZzScVbxBl-Ju7337LHdrbMsL3MJ00wBDOjuGmRgRBtWubJEqUP9Jv009wJtQLQs3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f26b235d.mp4?token=HCu0Ha4UtKSAWlNrDqQaZK9NWEgEnWQhRkWchBdBtqYjiTs4tycDgvVhFGh7mElgjI_5bnwB1b9vgty-V7IpYy1ssyHNUuYzqL0Gg5VqaheUXcVSy9dkvygZzO0jfAAVYx68HuQ15wv09g3Nh9VXvVaNJ2dvkvHc7ZoSo9A_kjBTcKRy7iIMaxSyuIiyx2u5nfhGFPWseUVBRh8Y_m2Evy5UbuILSw-3c3l6_IK54_4HXdmrCwsnVN10FidGnDJf0ZPsv4JTANH63brrcLaGHZzScVbxBl-Ju7337LHdrbMsL3MJ00wBDOjuGmRgRBtWubJEqUP9Jv009wJtQLQs3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مقرات المعارضة الكردية الإرهابية في أربيل شمالي العراق تحترق بعد دكها بالطائرات المسيرة الإنقضاضية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91423" target="_blank">📅 03:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91422">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔻
دوي انفجار عنيف في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91422" target="_blank">📅 03:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91421">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7970135621.mp4?token=Lg2S2mzji8SgwVR3DSVKAXwGoIfPjm529zilxbM1gk78ZLDXZOngmQMKI3DPtDkRN6x6P126tASC2IZqzbRsqV7mDsoVSRjDep8ZVSBrOSvpcYR3LBjE1YCKU6264R0c4j-fyy8FKpSLT6EtKGEI2eEA4TQ2grVt2YhntXO7pYHDwpRhyE3IJUVD3oAmXkIiSd5BGvjDFbM8Dznf3Y3Uh4rWe5Aaub1Juu3FEcDKF9af8Cf9_A3gAq0JGg_15cQJDT1jCK3757_dhpQ5ajMmPmzgUVLE3sM-5FCU6s67R301TWdA1eSC_5EcAHWWrVfWZSWS-sGPVhrDp4E3UvY2Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7970135621.mp4?token=Lg2S2mzji8SgwVR3DSVKAXwGoIfPjm529zilxbM1gk78ZLDXZOngmQMKI3DPtDkRN6x6P126tASC2IZqzbRsqV7mDsoVSRjDep8ZVSBrOSvpcYR3LBjE1YCKU6264R0c4j-fyy8FKpSLT6EtKGEI2eEA4TQ2grVt2YhntXO7pYHDwpRhyE3IJUVD3oAmXkIiSd5BGvjDFbM8Dznf3Y3Uh4rWe5Aaub1Juu3FEcDKF9af8Cf9_A3gAq0JGg_15cQJDT1jCK3757_dhpQ5ajMmPmzgUVLE3sM-5FCU6s67R301TWdA1eSC_5EcAHWWrVfWZSWS-sGPVhrDp4E3UvY2Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
لحظة إنقضاض الطائرة المسيرة الانتحارية على مقرات الانفصاليين في أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91421" target="_blank">📅 03:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91420">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3995a51c1.mp4?token=aCA0SULdoZGR99c4zdqcAw50YNclCufA6ZF6FX2uZLMaS2APZ6LM52VQHm-L_qHft233oUbjJkPfiXFBn7j3VAEs5h0j8IOShC_OAoEcCA1GkuHDci3ODNlz6I1bbg6hm048ABKBDbbAQ-qA-lJklYqXl_MnA5-_tnVufALK9ioCG8iQY4yh5BJOpqIDGACuHfxbOf5aCyqV8z3SFxt9aopdCv4Hf9QVDR9BQs1vocr4EksQ24R71OGKhxvNW-r14xJoGWtZpmVVlHrYqluwna2UBNftDoAiImv_MMGatOGLjqb3f3NOvgLIs9W3HJwRugypvUVKLToCtLb0kM-aDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3995a51c1.mp4?token=aCA0SULdoZGR99c4zdqcAw50YNclCufA6ZF6FX2uZLMaS2APZ6LM52VQHm-L_qHft233oUbjJkPfiXFBn7j3VAEs5h0j8IOShC_OAoEcCA1GkuHDci3ODNlz6I1bbg6hm048ABKBDbbAQ-qA-lJklYqXl_MnA5-_tnVufALK9ioCG8iQY4yh5BJOpqIDGACuHfxbOf5aCyqV8z3SFxt9aopdCv4Hf9QVDR9BQs1vocr4EksQ24R71OGKhxvNW-r14xJoGWtZpmVVlHrYqluwna2UBNftDoAiImv_MMGatOGLjqb3f3NOvgLIs9W3HJwRugypvUVKLToCtLb0kM-aDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
لحظة إنقضاض الطائرة المسيرة الانتحارية على مقرات الانفصاليين في أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91420" target="_blank">📅 03:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91419">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تتمكن من دحر مرتزقة السعودية وتفرض سيطرتها الكاملة على خط تعز عدن.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91419" target="_blank">📅 02:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91417">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eac70bf40.mp4?token=RM1d7cVAKu3Ev02F2W_oebF4Ig6Y0SVOhG-pqEd9T4OO-yppz8DqLLJ6zhwLdXQyyeQ_JYNvxCHwFWAlU_RvmbSIroItfp2eeTndurMwRDpYrfmZGiqnx0b7NNgf00UhkIUvgA6oI1xzC8jETJHAZbYeg_r17212X53090vhEZJciFx8MMg2dCZeNaJ5ywCcRr2Jp-Hu8ke_IqTjcLIYPYg48xorn6Cyz73DCgXxUI2-oUIrFfk7j0bes633ajWOaS0kDyQXYxIbJb9_HyG1Acs3sL5sO8AHUns6mMKTw-Y5rhCb6Lo7x9lrEpi_YBLve6Zp0jM_EExFVtSmS5hVtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eac70bf40.mp4?token=RM1d7cVAKu3Ev02F2W_oebF4Ig6Y0SVOhG-pqEd9T4OO-yppz8DqLLJ6zhwLdXQyyeQ_JYNvxCHwFWAlU_RvmbSIroItfp2eeTndurMwRDpYrfmZGiqnx0b7NNgf00UhkIUvgA6oI1xzC8jETJHAZbYeg_r17212X53090vhEZJciFx8MMg2dCZeNaJ5ywCcRr2Jp-Hu8ke_IqTjcLIYPYg48xorn6Cyz73DCgXxUI2-oUIrFfk7j0bes633ajWOaS0kDyQXYxIbJb9_HyG1Acs3sL5sO8AHUns6mMKTw-Y5rhCb6Lo7x9lrEpi_YBLve6Zp0jM_EExFVtSmS5hVtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سقوط قتلى وجرحى في صفوف الانفصاليين جراء هجمات بالطائرات الإنتحارية طالت مقراتهم في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91417" target="_blank">📅 02:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91416">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
إنفجارات تهز محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91416" target="_blank">📅 02:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91415">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2868023a93.mp4?token=JCCaT8TyPEeAWsA0xgrrGk8hvl9rGy5tGbTp4lQhz3IXhOcjsJaIIhwWMMKg5gc203E3w4aVvRJZuklxoFnGxAtgSuYPze8OoW6ykrXKnh-1fErhoSZKFIlVMKGhizCKd7eKPQstdYZhgUVmt1_QJ3Lu2e74dfmkdPrScFcKbVl_RE4s-N2G5cXW2mZPKrHH1WdpetsNHLY9Ft0FmMdsXr0Yw7io7dICWYIjE68O2-SAxs9JMLGZcaWY3on8P0CBMdjb2eTpQsrkcGF3bWP6jXGWyh8LNCzNDyoUglJorPWZBVM_xKjgzv2wsGBfaHeKl6oKQLPq7QtwPDo9UAKCVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2868023a93.mp4?token=JCCaT8TyPEeAWsA0xgrrGk8hvl9rGy5tGbTp4lQhz3IXhOcjsJaIIhwWMMKg5gc203E3w4aVvRJZuklxoFnGxAtgSuYPze8OoW6ykrXKnh-1fErhoSZKFIlVMKGhizCKd7eKPQstdYZhgUVmt1_QJ3Lu2e74dfmkdPrScFcKbVl_RE4s-N2G5cXW2mZPKrHH1WdpetsNHLY9Ft0FmMdsXr0Yw7io7dICWYIjE68O2-SAxs9JMLGZcaWY3on8P0CBMdjb2eTpQsrkcGF3bWP6jXGWyh8LNCzNDyoUglJorPWZBVM_xKjgzv2wsGBfaHeKl6oKQLPq7QtwPDo9UAKCVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فريق الصحفيين المتواجدين في البيت الأبيض يمتنعون عن تغطية كلمة ترامب، والبدائل الأخرى تواجه صعوبات في البث.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91415" target="_blank">📅 02:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91414">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5f475039.mp4?token=JHGRyp-bzdj44z9AlzHexidOZv_snWpNHyoUzGuMjMNXjES1d8mwh8FR3pRtGVsrUxt-0PfUZ8lKJ5_StqwJsTZjXnq6PYeFWD7Wktwapo0UdF082a5L4mGMclLfMrrSov-XzF-1PtLzaM8BAAfRPGdho8NYr8k2IEoGj72wwNkCN4DM3G1jj6ScSxJtkaulV_YxST2nB_aa801_PZDB98rggn8h-00YSUDyMkWjoja89i3nsRYc-xGXXFrEpsb8pQQQu_rMfQRz8dYRs_6sw_PGj883hYdRDI_IfFhru5KLmBcotIpEUKvxlLFN8jin1Ue_blEdyzt_Qh7ZNwzCag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5f475039.mp4?token=JHGRyp-bzdj44z9AlzHexidOZv_snWpNHyoUzGuMjMNXjES1d8mwh8FR3pRtGVsrUxt-0PfUZ8lKJ5_StqwJsTZjXnq6PYeFWD7Wktwapo0UdF082a5L4mGMclLfMrrSov-XzF-1PtLzaM8BAAfRPGdho8NYr8k2IEoGj72wwNkCN4DM3G1jj6ScSxJtkaulV_YxST2nB_aa801_PZDB98rggn8h-00YSUDyMkWjoja89i3nsRYc-xGXXFrEpsb8pQQQu_rMfQRz8dYRs_6sw_PGj883hYdRDI_IfFhru5KLmBcotIpEUKvxlLFN8jin1Ue_blEdyzt_Qh7ZNwzCag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهدة لطائرات مسيرة في سماء محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91414" target="_blank">📅 02:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91413">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe0d2abf0.mp4?token=t70pEqiNyA9Q0TIDhpeWXoThi-LSXVA2sTkLKuMgiArYhuSifeWs1UbGjp0vPeYsusZQtQgqQ8bs6NCp2YMSGDtlcP8p3v-PHd_NPhKdfJpHNLNGtTR7irIX-CWGUVpMB6F_AtL4qsA8FdpbeoqLmYbJj_25m8xcqBMC04i_YjmsSWxwiNuqVtnjIIpIN7UhBy4__z4-j5AKxYZVhzavufsTXATe1T1Ac8E7GYtNgZy_k1p0rOCB0gltJs2wCJdncR-HKI8lRsB2br_sPP22Xi7mIc4sY3wytU9fw91N4R9qwaCb2ORKAL8hQCpXQrVA5aZmhalIsO2raZ2LeVcd_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe0d2abf0.mp4?token=t70pEqiNyA9Q0TIDhpeWXoThi-LSXVA2sTkLKuMgiArYhuSifeWs1UbGjp0vPeYsusZQtQgqQ8bs6NCp2YMSGDtlcP8p3v-PHd_NPhKdfJpHNLNGtTR7irIX-CWGUVpMB6F_AtL4qsA8FdpbeoqLmYbJj_25m8xcqBMC04i_YjmsSWxwiNuqVtnjIIpIN7UhBy4__z4-j5AKxYZVhzavufsTXATe1T1Ac8E7GYtNgZy_k1p0rOCB0gltJs2wCJdncR-HKI8lRsB2br_sPP22Xi7mIc4sY3wytU9fw91N4R9qwaCb2ORKAL8hQCpXQrVA5aZmhalIsO2raZ2LeVcd_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء عن صوت انفجار في اربيل شمال العراق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91413" target="_blank">📅 02:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91412">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انباء عن صوت انفجار في اربيل شمال العراق</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91412" target="_blank">📅 02:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91411">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae51612e7d.mp4?token=oCMwxRyA32Jskb0HSMrZ5XU6HJBNy80zIwT7QyDmmdTtxi-XLVd1yE8WCA2q5NnAGsev8-_ZdiqKpRjiZKTGuDAUu6NIIReMGeuizdhHmi17zzmLBEAEchKJ64YjEc3HtwnWKiWU13tTG7Z2uGJ_WWYlh71PgYdNm4V6BB0js8rWzVQQInYzD-h56o-BYelIz-OmblUQe9Mk8odUpBUW_9on9zWsA7p-qPXxafP1r3HwGPg7TmyXnmYmDU56B5OTTiWAGkIZSd8LdhnhRahcmAqfqnec4QC_mqiwasP0BIYYTZbHRQ2rUFzP5G2aN4H0DC54EKyYWkZe6QIx4a-xhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae51612e7d.mp4?token=oCMwxRyA32Jskb0HSMrZ5XU6HJBNy80zIwT7QyDmmdTtxi-XLVd1yE8WCA2q5NnAGsev8-_ZdiqKpRjiZKTGuDAUu6NIIReMGeuizdhHmi17zzmLBEAEchKJ64YjEc3HtwnWKiWU13tTG7Z2uGJ_WWYlh71PgYdNm4V6BB0js8rWzVQQInYzD-h56o-BYelIz-OmblUQe9Mk8odUpBUW_9on9zWsA7p-qPXxafP1r3HwGPg7TmyXnmYmDU56B5OTTiWAGkIZSd8LdhnhRahcmAqfqnec4QC_mqiwasP0BIYYTZbHRQ2rUFzP5G2aN4H0DC54EKyYWkZe6QIx4a-xhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇨🇳
‏ترامب يستقبل الرئيس الصيني بمراسم رسمية في قاعدة أندروز الجوية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91411" target="_blank">📅 02:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91410">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
وزير الخزانة الامريكية ‏بيسنت يعلق على الازمة الاقتصادية التي اشعلتها الولايات المتحدة قائلاً: "قد تتعرض ناقلات النفط للهجوم.لكن الكثير منها يواصل.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91410" target="_blank">📅 01:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91409">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/503e190498.mp4?token=BzQZbHBLN4qjIfhT42tp6YdtqVGBtlgvF2d5BOoy4fYSXEqWGc2mFqSk4J6ohI2GW-Yi_ePfNbIa9nRhZDMYKkdG549MIv3es3hULXa2cqGv8WPU8BDvzlG5YIHlLImKitZOQ5y_gOu_d8eUtmB0fU7M0BNMFxUOdMMRii5v2QiA8S7fCC3fjrGs6xsphEkj30tw8hwHoh9w7LV1RC4TLHC_MG3Uc32r63KwDe6wq9a_MCDzPNFD-Jdp4vkOnNN0faVUA7vE9xntAic-nSALj3umPfvY0LK7odc4_fmVgehNdb9NdJ9DAl6S8bY9-QRog6cY7XIocU-6RMdvTrnHc4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/503e190498.mp4?token=BzQZbHBLN4qjIfhT42tp6YdtqVGBtlgvF2d5BOoy4fYSXEqWGc2mFqSk4J6ohI2GW-Yi_ePfNbIa9nRhZDMYKkdG549MIv3es3hULXa2cqGv8WPU8BDvzlG5YIHlLImKitZOQ5y_gOu_d8eUtmB0fU7M0BNMFxUOdMMRii5v2QiA8S7fCC3fjrGs6xsphEkj30tw8hwHoh9w7LV1RC4TLHC_MG3Uc32r63KwDe6wq9a_MCDzPNFD-Jdp4vkOnNN0faVUA7vE9xntAic-nSALj3umPfvY0LK7odc4_fmVgehNdb9NdJ9DAl6S8bY9-QRog6cY7XIocU-6RMdvTrnHc4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
السفينة التي تم استهدافها صباح اليوم من قبل الحرس الثوري بسبب مخالفتها قوانين العبور في المضيق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91409" target="_blank">📅 01:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91408">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
🇨🇳
‏
ترامب يستقبل الرئيس الصيني بمراسم رسمية في قاعدة أندروز الجوية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91408" target="_blank">📅 01:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91407">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a40a23d1.mp4?token=jP3feDfByDf1GlwkeO7Yu_jalL7xAJP-FRqjEwX7_6s0jsaUKpbZ7slWkLj8DodGCWXUgYF2oCwfo5COELxd1lav46Zc_LhubVefBtILT-ktOnJXE9KdRRSSG8EuAGsQUjnPqXlLLI0DAe8fuLmqCLq1CLJ3D2qaCBaFr6oOHr_OyjEEWUWoTxNaRYm17c658L5kaoTY7l28CMgpZrXYtYGBW2MAfCVNW5mMb_gcNCz4gwNXWu83-DMX_UKKulqWA2iL3CQ76OU8megNSexSNCEf3V4H4reSCurO1eX4-XCbh60RBfQ7g5pcBTcGzRr2I6WqFVhjT7PKi7b_nR8X4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a40a23d1.mp4?token=jP3feDfByDf1GlwkeO7Yu_jalL7xAJP-FRqjEwX7_6s0jsaUKpbZ7slWkLj8DodGCWXUgYF2oCwfo5COELxd1lav46Zc_LhubVefBtILT-ktOnJXE9KdRRSSG8EuAGsQUjnPqXlLLI0DAe8fuLmqCLq1CLJ3D2qaCBaFr6oOHr_OyjEEWUWoTxNaRYm17c658L5kaoTY7l28CMgpZrXYtYGBW2MAfCVNW5mMb_gcNCz4gwNXWu83-DMX_UKKulqWA2iL3CQ76OU8megNSexSNCEf3V4H4reSCurO1eX4-XCbh60RBfQ7g5pcBTcGzRr2I6WqFVhjT7PKi7b_nR8X4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ظهور جسم مجهول انفجر قبل لحظات فوق سماء وسط وجنوب العراق.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91407" target="_blank">📅 01:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91406">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الصين تحتجز قطعًا حساسة من طائرات الـ F-35 تم تحويلها إلى هونغ كونغ.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/91406" target="_blank">📅 23:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91405">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
انفجارات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/91405" target="_blank">📅 23:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91404">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxv9EDY7vwNbgm8ZU7TideMBNsma-_xn1IxOu1QjEoZYzHsBqIVhlUaoBM7VdSrQdGKgTg7xXjKoRLa835oMm3tbcGeT6eOzLeomOrZTwkiAxkslzJNn4EsUJfLdM69_msu606ZMzkEg07-sZByDHpq1mL4OnemLzAVjh4k0rq4R4eUqQOisBaja8uXsS3FYj7yOw5e8pdleZuwlvU0dv1rciiuTM7s7TDxffPnmPxvLk1anGTsdCdxrzmO-dbEeIJcuWwnYDtHwDW_N0yYqyGx5PMGP2Qvpbuz6n5NK_HH0XJt0AnP3vQjDEDb2qQvRgDHE9kv9GpBCAQ5VoWIKVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇰
🇮🇷
اطلاق صاروخي من باكستان شوهدت من ايران وباكستان وانباء تتحدث عن نجاح عملية الاطلاق.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91404" target="_blank">📅 23:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91403">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
انسحاب النائب العراقي ياسر وتوت من تحالف الاعمار والتنمية وانضمامه لكتلة ثابتون.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91403" target="_blank">📅 23:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91402">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDWSn0gRAcjJaw1QYP3sWXu2FYFkXr_fIk-j7nb8ltxv4ZReSElWsr_25RBdSvvR7qhLj88_mpzf0-eMOrm8hJIqgq-yomHO4MhGmXtwnWco3tugc9AYj0B7comQZi0MZF4_VS2AgTP2mgK2bbuk6Iwyhz9gUFnqmAt5qJ3QraRKNu0C-BIHrbZjga3ZQhnLXDe0zdDZwxgIFXDqJXxeQuEU4u9r_8w6L818ZttJu2N61z8uI86BmaBfb9Zy2Yl-zN5Okz9jL5Za9u1Z5scIXzn4UiaFzPF4z-goHlXgLPuipxs5MAfwnJ5PZLA1P--I3kWG0kRSYbnEGEdP8ul9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
الحرس الثوري الإسلامي
اليوم، في قلب النظام المتعجرف، أعاد رئيسنا إنتاج رسالة القوة والفخر والكرامة والأمل لأمة صورت على مدى سبعة أشهر جبلاً من السلطة في ذروة القمع أمام أعين شعوب العالم.
بالاعتماد على هذه الوحدة، بدءًا من أعلى سلطة تنفيذية في البلاد وصولًا إلى المحاربين الشجعان في الميدان والناس في الشوارع، سنحبط العدو ونجعل مستقبلنا أفضل من الماضي.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/91402" target="_blank">📅 23:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91401">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
عكس خطاب ترامب في الأمم المتحدة الموقف السياسي غير المستقر الذي هو عليه.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91401" target="_blank">📅 22:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91400">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
🇹🇷
‏
بيان عراقي تركي:
تركيا ستسلم "تدريجياً " للحكومة العراقية معسكر بعشيقة - زليكان، و الاتفاق على إنهاء وجود العناصر الأجنبية المسلحة المحظورة في سنجار.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/91400" target="_blank">📅 22:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91399">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdBOkgg8MFrN7uz28a2kCfzmpsJJFfyZCoJshQoUJgH_kSAduszj19573VKY9PEPsn2FhzyRvptTyP-eSrqJE6HEcNvAfgKyTPzOsbp0hE2Myi00AgkXXxUmHJWRryrjWLqHtz8XvLMFKFv7v3Tezs0sPE0JqO5gkrBJCxU18NWbOFxdhgbyVgV0tJRWCK5RsW4Dbba2t2binlCZl1rHUBZT5LuGAiD3i8Lh9EH-Nz2RmQ7iEXLC_1Tnnru5A4BICA82Ef0Xye0yxcUcwT5dd4RNDQyLUV2YkmaKieb9LXbxTpFnlTl_JQOYz7r2dc432H360B1nJEW35JwkIHaeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط ترتفع لتصل الى 103 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91399" target="_blank">📅 22:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91398">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87ad81d2a.mp4?token=EOF62F-JfrSbqRey5Qi-fuNyau-1b4BfQs86ePDE2QXlNWRig-_uzWpheMhJv1gwc_-Tke635Lm5O3PnAlSfYXWq37Tp2B0u2HkehAjZbZlPYC2Tm18I1I2OBQlpdIUVa4swHM3CzGbi5kK0d1jAXWyksWNEsNhWdhmFWF5Cyus08mSMxgVS309a7fEL9TUX29FIGNSarMjMlbGjrfC7GZeiNPw6YLHko5vuma-D1LESePzbes5nMrUouL5jzZTgmMsek1KZBJnRf2TrshtjGB_AgklAbdH83IEFZol8MUp93htmqZw31OcD8TyWH_C9iPuEiROejDQpiC_oWAd7Lb42851tScYbU1A1S_vL-n3l9XTJt6qSut_DzWqvs-RH6hE-uFY-n4Ey_hFD6uBo_M6UhzjflscwLd3q07w-H4U7YME07zUlvFTqHeRivfIk_nb3ZwfhPBZR9Iml7Rm1u4a3RMfLDnFgrYT07_VG07VFAY1XjaAStlou2xXs6zhQ5TZbLBgFN-W4L7cHyJ70kDKTFY0kYYTGDNlyBFXvYDgFG-azh4ZLji9ckf_-vHMmpgM719Kn_vGBEEeHsrXpoXi_t77NUXC62v2Vsd9P8Xr7jvY6BXh2YZFTnIKVKiDAdaFnAEVITmB10fEiulDpZpDvJRwfPc7zQ3fCgFLYsg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87ad81d2a.mp4?token=EOF62F-JfrSbqRey5Qi-fuNyau-1b4BfQs86ePDE2QXlNWRig-_uzWpheMhJv1gwc_-Tke635Lm5O3PnAlSfYXWq37Tp2B0u2HkehAjZbZlPYC2Tm18I1I2OBQlpdIUVa4swHM3CzGbi5kK0d1jAXWyksWNEsNhWdhmFWF5Cyus08mSMxgVS309a7fEL9TUX29FIGNSarMjMlbGjrfC7GZeiNPw6YLHko5vuma-D1LESePzbes5nMrUouL5jzZTgmMsek1KZBJnRf2TrshtjGB_AgklAbdH83IEFZol8MUp93htmqZw31OcD8TyWH_C9iPuEiROejDQpiC_oWAd7Lb42851tScYbU1A1S_vL-n3l9XTJt6qSut_DzWqvs-RH6hE-uFY-n4Ey_hFD6uBo_M6UhzjflscwLd3q07w-H4U7YME07zUlvFTqHeRivfIk_nb3ZwfhPBZR9Iml7Rm1u4a3RMfLDnFgrYT07_VG07VFAY1XjaAStlou2xXs6zhQ5TZbLBgFN-W4L7cHyJ70kDKTFY0kYYTGDNlyBFXvYDgFG-azh4ZLji9ckf_-vHMmpgM719Kn_vGBEEeHsrXpoXi_t77NUXC62v2Vsd9P8Xr7jvY6BXh2YZFTnIKVKiDAdaFnAEVITmB10fEiulDpZpDvJRwfPc7zQ3fCgFLYsg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي
: بعملية نوعية كبرى، إلقاء القبض على تاجر دولي بارز للمخدرات على الحدود العراقية السورية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91398" target="_blank">📅 21:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91397">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
البيت الأبيض يضع خطة لحظر تصدير الديزل لمدة 90 يومًا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91397" target="_blank">📅 20:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91396">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10fa15f285.mp4?token=KXS-scJfUKHfBOIjrtEUoTqO-wMSgUUv0g4sgAg3vVyoYKgIm2jp6gOObsM9qcjbVjz-ViyNKYLZ4MZXqdLg4IVgPkEQ5YbFlB3jmcCw75tS5VdCY8U1VKRakZc5x7YhwmdHYyMmjISR5lvALOXAf3f0aIjThWewiyzsz5cDKsZMiJes4fhvo9UaIew8fbh1BmsTalhQgL15X5pWcPzHGgjCVcz3SX021dB8do4FEQRajkBAkZLI2_E5X857o4UUYWK6ii2oPVGv0dV_cLUOfymPut_qgNdyjoRfX6zmzxCoSI4ul5ZtxefYHnJTT_lnqc5bx8sLd_mxrsnN_lO7mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10fa15f285.mp4?token=KXS-scJfUKHfBOIjrtEUoTqO-wMSgUUv0g4sgAg3vVyoYKgIm2jp6gOObsM9qcjbVjz-ViyNKYLZ4MZXqdLg4IVgPkEQ5YbFlB3jmcCw75tS5VdCY8U1VKRakZc5x7YhwmdHYyMmjISR5lvALOXAf3f0aIjThWewiyzsz5cDKsZMiJes4fhvo9UaIew8fbh1BmsTalhQgL15X5pWcPzHGgjCVcz3SX021dB8do4FEQRajkBAkZLI2_E5X857o4UUYWK6ii2oPVGv0dV_cLUOfymPut_qgNdyjoRfX6zmzxCoSI4ul5ZtxefYHnJTT_lnqc5bx8sLd_mxrsnN_lO7mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
في وقت يعاني فيه العراق من أزمة تصحّر وتُقام عشرات حملات التشجير
... شاحنات تركية تدخل إلى عمق الأراضي العراقية في محافظة دهوك، وتقوم بقطع الأشجار وتحميلها حطبًا ثم تعود أدراجها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91396" target="_blank">📅 20:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91395">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 52 غارةً جويةً وصاروخاً من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي انطلق من جيزان، استهدفت محافظات الحديدة وتعز والبيضاء ومأرب وصعدة وخلفت شهداء وجرحى بينهم نساء وأطفال ودماراً في المنشآت المدنية من شبكات اتصالات ومدارس وجسور وطرقات وغيرها.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا العزيز 988 غارةً وصاروخاً.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91395" target="_blank">📅 19:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91394">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇱
🇸🇾
الجولاني يكشر انيابه: الجولان هي أراضٍ سورية تقع تحت اعتراف الأمم المتحدة. لا يوجد أي نقاش حول هذه الأراضي ومن هي الجهة التي تملكها.  والقنيطرة ودرعا وريف دمشق والسويداء؟؟؟ https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91394" target="_blank">📅 19:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91393">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
السفينة التي تم استهدافها صباح اليوم من قبل الحرس الثوري بسبب مخالفتها قوانين العبور في المضيق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91393" target="_blank">📅 19:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
القوات الامنية العراقية تبطل مفعول عبوة ناسفة في ناحية الرشاد بمحافظة كركوك شمالي العراق.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91392" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91390">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f03f1569.mp4?token=lEGb3DounlHv4GRes57dvdj1it6gf3OgyCF6Yd-8LoreK-9N3CFMEdUuRqnrx7OzePh0vJ1oAM99yg4MKSkxchnuM1A57c2J7NwkmOSPzz3fVaDFpbWmkQEHsywLhkYcnifikjNQvwHsQZgdzd9h5fwFbJtXAwIvOUKRji2k11apXK3Jdx-t1Gw5o0rOm0IsRxERLJATTE-Fem-K3zyqYD0twB14ImT-VSYT1jQuc-uLrATox8HOuw1GxkYOxfEDyXjaHhUOGk_YBQ9Xqn96HL-wU0VVioF1OLDYOBtCgumBc4n_uZwGGlnVUxyyh5QolHegWTUHPK7F1xhsv7YKVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f03f1569.mp4?token=lEGb3DounlHv4GRes57dvdj1it6gf3OgyCF6Yd-8LoreK-9N3CFMEdUuRqnrx7OzePh0vJ1oAM99yg4MKSkxchnuM1A57c2J7NwkmOSPzz3fVaDFpbWmkQEHsywLhkYcnifikjNQvwHsQZgdzd9h5fwFbJtXAwIvOUKRji2k11apXK3Jdx-t1Gw5o0rOm0IsRxERLJATTE-Fem-K3zyqYD0twB14ImT-VSYT1jQuc-uLrATox8HOuw1GxkYOxfEDyXjaHhUOGk_YBQ9Xqn96HL-wU0VVioF1OLDYOBtCgumBc4n_uZwGGlnVUxyyh5QolHegWTUHPK7F1xhsv7YKVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
المتحدث باسم الوكالة الذرية في ايران يرد على ترامب:
الوكالة لديها إمكانية الوصول إلى جميع منشآتنا
"إسلامي"، رئيس منظمة الطاقة الذرية:
على الرغم من عمليات التفتيش المتعددة التي أجرتها الوكالة، لم يتم تسجيل أي تقرير عدم امتثال. الوكالة لديها إمكانية الوصول إلى جميع المنشآت. إنهم لا يصدقون هذه الحقيقة لأن هدفهم هو إيقاف تقدمنا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91390" target="_blank">📅 19:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91386">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmg1b9i43IpohUxLTfkkFeYnpb-zck7ab8u_mUfxECYoRLYY_LHRy2_IQT6jNPhnwou_JTne8dI661SP-wdwBP9kv6PrBySuq4lVqMXQsDThDI-s59HMfrXjsDbrJtsiuHrAFBwHLd4w4DAoDB45cGkvjRu7hVSYwuYh8WHQHwxxNrY2vgocYJhOcyymGzngKvvRZCjjTRaKScAdFGnscQ2OH4IivWKAGoCfFccBZU8otFPFGlhd_M0bL1GExmDFUD5NuzmivWZQ9JTf9V36Bwp1olA9dxaeOU9iw2_CZ-F9plrti8AU-r6CmwX_X8-_C4LMG3Uuffl_495tcKfmJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bj_YXJ88_2zoAdkgRg7uY-_XvFVxmZ2VdrKq03VPqpN3Us4yn6IyN9wNJDT4J0v-8r-AbzwcdCTDrQQwv7JBZDie6UxF7zM-H0czTHByu5krAp_DBW74Q-raX0-XoiU4pjynsZ0K7KS7CeWhArDDHhKtA6e5Xgx5jECfSfdA64s_93ehtJyPpCkgqscZpCfQxKrgpuL-QPdk6qna6IEVvQYdLhQ9CUfc3Z0bF0QYldtkU9ysacenz2f5BMlXYrmaqC60py2VHVJo1Js9RRewfLD7Klb_xngOsO9a87-B4_lvmPTszBehfuihXxWfwk5BXDXrA-tl5Q_ZvnvXOejOmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9ndxLlN7DbXKTRrCYlrmVVgmFpkdPIiQuVLN_f2aU_8nGi6O8JyPC2lOrWoigz39e7scOJE7t7ByVWNEWa-w15yVMhxS8zTTHtyITKjITCEQOFZTT_fGcmBINJyjZTH2OfevA-DtVlDGOp10Tu69y-Kgtnqy8FcTJcSNjCN-LP9zFvl6hf8feVgfZp_dQZ6CQawUSYOwF5rxuKnwoRBsPcmSVjRwloiONxjEzLdBhaEQAL-vXxvRtnU5ml1qF033UPnEI_gB5teyrN7UNbEEIkW5JyByqkmQYObu_Q_rXJWWd8aIUZfpP_FhY6JtA-3n__sYcPmHn7egaJ6uMN6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbzCHbiT4UfdGyGEQpUEZ1O1B9yZ4mPNkx5C09IWcwsgs-B9ZEwjI73X4CbbNUZh2f39_kIjDsIhsrHFr-AWsQxRG6fvRkrrX4QUNFFabrLS6PBsUoqQzdOhx8D7mTlVyA0_t9PedRyR5kuccWDlbGbchILW8V6AFVnv7mhyLbivgM2tYq9s7iJJs_lwGUmRXCS4a0i5RoTv1TYEIGPCplPYX1mFxFhbnoTG9rmjJlI64MetktvXXS-_e6hWs_7ENxXhHZfJgA0fFCcIfPXMgS6iD7i2MPcvJDviJdrQIu8p0dkTaDHC5Ol8Kse6--ZSNQD9ypdiugm69guqEz2Ziw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇱
🇸🇾
جيش العدو الاسرائيلي
يعثر على اسلحة في عمق الاراضي السورية.
قلت له اعطي نيوجيرسي
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91386" target="_blank">📅 19:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91385">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/636d677358.mp4?token=PMg5mQplXdAjOFpYyspxkEC5OvY7Dmgs1GUNCCKSUVcNvrdsg5leqhC1lG9n-VchG9FD1RC-T3qUxGb4F_1LfzkKRT-ptVMJ4P-sCYBIzNwKs7OsPz7uiwoSQTS9G0BQ38bbpzJ9t1ZQ46ooBytXH3HsVzmsnV2UiIPwTmC-xFKwZl6lF4bdUJh3-tkwJTzqu4FlLMFNk4h5tFPu8RTpe-c18-fW3r9qWRfeBXp_1Fmlp4HMvLSc4dzM-SOwvPSbdHT9mQfwmWr4tWadaOlpbO6YtE45H0yVt4wsh2ay1OTU3QBfjRQ4TqdPLyZYqmCSPFVmPU2Q1c08prPkrViq2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/636d677358.mp4?token=PMg5mQplXdAjOFpYyspxkEC5OvY7Dmgs1GUNCCKSUVcNvrdsg5leqhC1lG9n-VchG9FD1RC-T3qUxGb4F_1LfzkKRT-ptVMJ4P-sCYBIzNwKs7OsPz7uiwoSQTS9G0BQ38bbpzJ9t1ZQ46ooBytXH3HsVzmsnV2UiIPwTmC-xFKwZl6lF4bdUJh3-tkwJTzqu4FlLMFNk4h5tFPu8RTpe-c18-fW3r9qWRfeBXp_1Fmlp4HMvLSc4dzM-SOwvPSbdHT9mQfwmWr4tWadaOlpbO6YtE45H0yVt4wsh2ay1OTU3QBfjRQ4TqdPLyZYqmCSPFVmPU2Q1c08prPkrViq2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هيئة عمليات التجارة البريطانية: مسؤول أمن إحدى الشركات التابعة لسفينة شحن افاد بتعرضها لإطلاق قذيفة مجهولة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91385" target="_blank">📅 18:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91384">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزير الخارجية الامريكي روبيو:
اجتماعنا مع الايرانيين كان إيجابيًا، ولكنه لم يحقق اختراقًا.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91384" target="_blank">📅 18:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91383">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
مسؤول إيراني رفيع المستوى: طهران تدرس رد الولايات المتحدة على اقتراحها لإنهاء العداء.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91383" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91382">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي ‏روبيو:
يجب نزع سلاح الميليشيات العراقية لتفادي "بلقنة" العراق.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91382" target="_blank">📅 18:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91381">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏روبيو: الحوثيون هاجموا مقرات دبلوماسية.. إنهم قوة شريرة بالمنطقة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91381" target="_blank">📅 18:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91380">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
مسؤول إيراني رفيع المستوى:
طهران تدرس رد الولايات المتحدة على اقتراحها لإنهاء العداء.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91380" target="_blank">📅 18:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91379">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي: سنفي بالتزاماتنا الواردة في اتفاقية الدفاع مع السعودية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91379" target="_blank">📅 18:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91378">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي:
سنفي بالتزاماتنا الواردة في اتفاقية الدفاع مع السعودية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91378" target="_blank">📅 18:20 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
