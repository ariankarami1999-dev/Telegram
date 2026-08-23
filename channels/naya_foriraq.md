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
<img src="https://cdn4.telesco.pe/file/KLK_kKGHUSWG9Nr2E5GSpabJpB63pzTd2gfDu7Jj7qBcWygtzoBKLXCv41HdFuLx61OPASGzUYAZxRCNAdBi-FoNwPEhouSY8zSvBhDWj99rtB0Gnl9Z1cq-LnbSKaljdje4fpgFnY0oJXl_D7Q0KWfdcU3UZv6YG_j2YVzfBmZzUY90Y2p9k_Zzo_8NOPb5U9bB-IrIaIk90egqdKT84W87UmQMvGC-gDKdSU6lIZSTseCX3jXFHr70EFLdsDyewqaiAuQPvSg6x_RmQ_LomGLuxbetjeSItm6FKr7gR8j0sT5nY19zqqYagfNm3K7qmhpll05rjlJji7HItry_Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 21:11:53</div>
<hr>

<div class="tg-post" id="msg-88368">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
طلب من سكان المنطقة المحيطة بقطاع غزة الدخول إلى مكان محمي بسبب الاشتباه بوقوع حادث أمني.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/naya_foriraq/88368" target="_blank">📅 20:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88367">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id0Qozkqt6QraaeIzPHVFLaHkYCMH_iBHBubazVdcqR8sWb9arepNwORwIalGKCuSTo2kXcrbFwcjUZrIMmZZH2P-7Bd3uK-9EP7S3vBtDdKetqiDa3s7jGVaRca2t_GtAYVJgbJ8qkZU5Qe_jTXni8p8lUXyKGT5fyu07SFGuIj-Fb_4IKnU-jHzS95GVTBaQdE2S5ZxxuhDLCjqwAKdoHAQ_GUsXS8_Mxv4pq0QgOCJPSJpUHS9SBg_ktSLFElRQp6CuJpLdGackGWomPhdDxT93nIXYt513wNULUfRYNEj211Pjty2ezFj4bWlz1FMRPGPLBBBnqISsc6Xm8Mdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ممثل السيد مجتبى الخامنئي:
- نتوجه بالشكر والامتنان والتقدير إلى المرجعية الدينية في النجف الأشرف، ممثلة بالسيد علي السيستاني، وإلى الدولة العراقية
- نثمن دور الأجهزة الأمنية والحشد الشعبي وأصحاب المواكب وجميع المشاركين من الرجال والنساء والأطفال في مراسم التشييع
- الشعب العراقي سطر ملحمة تاريخية في التضامن الشعبي والإسلامي بحضوره الفاعل في التشييع المهيب
- نشيد بأصحاب المواكب وأبناء الحشد الشعبي وبصمتهم في إنجاح المراسم
- حب القيادة العليا في الجمهورية الإسلامية للشعب العراقي لا يخفى
- العلاقة بين الجانبين تختلف عن سائر البلدان، لما يجمعهما، جذور راسخة ومحبة مع العراق
- السيد مجتبى الخامنئي وجه شكره لكل من أسهم في إنجاح مراسم التشييع ومراسم الأربعين، التي قال إنها جسدت عمق التلاحم
- برنامج وفد السيد مجتبى الخامنئي في العراق محكوم باحترام الشعب العراقي ودولته وسيادته ومؤسساته</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/88367" target="_blank">📅 18:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88366">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
الجمهورية الاسلامية تعلن الموافقة على تكلفة المرور عبر مضيق هرمز في لجنة الأمن القومي</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/88366" target="_blank">📅 18:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88365">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇱
🇸🇾
إكسيوس:
اجتماع بين مدير الموساد الإسرائيلي ووزير الخارجية السوري.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/88365" target="_blank">📅 18:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88363">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KXvNw_sZBLR52pTVUHbyveiiP3jP5o4nhk_OldT950yul0xSdOgJVCfJPD1KiqZHQmhr4DEnu6G40CHImDXPNjUMsfU4VVDMKLITV3B-xvqzLs9cD9oKCliF93dpvnlTwrOHRsajQTMF_FgzaJuUQEKuQjkxdvOypddxlzvp4zMTbeGzsdWbLn_NeIznJqzAKz6JkbjfiUGHHDgL8ZCV7RrrW5ZzCvMShejW2copuAAsLN10aVxDD-bh9OlixRTHmOI_zRfAQt2bjrgYHpltAxFj_dGXCqjIDE6Wi44t1DFuLQolX-vxCxWJVi1YJNO0dqdAoC0V-FT6mapTfT8mig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkCdu6oP9PA1uJLnesnI9rSd2a6M224kgxMELJ8CeXAQ5ib1le7itl7zy_El6W8FeA0zRPuQmBfJq_A2rCCCS6B2CNZUJVCNO2i0IqV38b-fXrGVJvmyF1whBcBN4_cvJUkO6W6ggcEYEvBlrVrgWRRyU1X1DQoHF3vzTuMShxSCyj7aOEQ1zIf6xLisRDdrocobEyZHPL3iCY4hrEiMJncvAa76zNz2WiNBnxTYJIDTT6kedQFgDTpxw_mUKxrmB5hTYrVaTOCI-0bYOVQUVQsDxh_7QlVxtbklFhDdinM386R6p3EEHWXoCVPL38rMFuykg3rc7Emqe-dcn1s2BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
رئيس هيئة الحشد الشعبي فالح الفياض: هناك من بذل مئات المليارات من الدولارات لمسخ صورة العراقيين وتغيير هويتهم.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/88363" target="_blank">📅 18:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88362">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇶
🔻
رئيس هيئة الحشد الشعبي فالح الفياض:
هناك من بذل مئات المليارات من الدولارات لمسخ صورة العراقيين وتغيير هويتهم.</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/88362" target="_blank">📅 18:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88361">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_Ny77Lcp2e_Mhh9l8n3Y1XcS40vgvWN0N5j2p1-lLPVWZNrTAtC-7ZGKhiLUEZmpaO49pFsMYlrLwUtZS5EL4_Z3aiNuGSWmAB5mTVf_eTO-sd57ieZspHm1ht27LT5E3sJAwGVVI0W4X_ATRN9TavahdXBrRBu7vCDCFjMqQEaKFjG3P2nnreg-09iUmdctZX2kywPLNdJfQm8WSYO_ChNOlCEvOLA32TFNe67eR8RL3PKeHI5uDE5NSDdL2kp-tzcsPiWJoHH8fKy_4pvG2MFv7qyuLMGPsPRdVI0xSgLL4HrH-fOyIWOaUiPb3CWh-nKW5miOJ3WuxVrCEhFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
:
استيراد اللحوم المجمدة لتحديد أسعار اللحوم. حسناً، قد ينجح ذلك.
‏ما هي الخطة المتعلقة بالسندات وتجميد عوائد الواردات؟
‏هل توقف مشتري المنازل عن شراء المساكن؟
‏تجميد الرواتب كأجور؟
‏تؤدي السياسة الخارجية الجامدة إلى اقتصاد جامد.
‏الشيء الوحيد الذي لا يزال يتحرك؟ البوميرانغ الإيراني.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/88361" target="_blank">📅 17:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88360">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اغتيال زعيم المافيا القوقازية يانيس يوشبايف</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/88360" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88359">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حدث امني في الكيان الصهيوني</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/88359" target="_blank">📅 17:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88358">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حدث امني في الكيان الصهيوني</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/88358" target="_blank">📅 17:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88357">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇱
نتن ياهو:
هذا هو طائرة الـ F-35. هل لديكم طائرة بدون طيار في المنزل؟ يمكن أن تكون بنفس القدر من الفتك.
إذا جاءت بأعداد كبيرة، يتم تجهيزها بالأسلحة؛ إنها دقيقة للغاية، ومن الصعب اكتشافها. منذ عدة سنوات، نعمل على إيجاد حل لمشكلة الطائرات بدون طيار. نحن الأكثر تقدمًا في العالم، ولكن هذه مشكلة عالمية.
لقد رأينا ذلك في أوكرانيا، ورأينا ذلك في لبنان، ورأينا ذلك في إيران، والآن يحاولون تجديد ذلك وإدخاله إلى غزة.
تعليماتي إلى المؤسسة الأمنية وقوات الدفاع الإسرائيلية هي أن تفعلوا كل ما هو ممكن ضد هذه الأداة الفتاكة: أن تضربوها، وأن تضربوا من يشغلونها، وأن تضربوا المكان الذي يتم إطلاقها منه.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/88357" target="_blank">📅 17:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88356">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
من الحريق الذي اندلع داخل مصفى الدورة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/88356" target="_blank">📅 15:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88353">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdeeeac9dd.mp4?token=LA7IWE4OFoj2oZreK7g6EBMiOTCywmDIF2M35_cabd-m5_gwW3Ta5r5ojKRWiBWFmdqrDJCgckHO4fz48Vu38ZZW7yf_BselVs1n8cPqo-dHp5rn3V64REE2iCdKczQIzb7S1UzqpBwDfi-GPUJhTVS-hMyAG8VpGp20wqPI6bKfCMgAmh2lP8sNt8hke4s0MPNldyLXfA9doBp-Yno3EyrklwOKBLKYUCF8sD2uBIjd9R5Ik6ltEtQztm3idWJ0wSbLMMvhncSeihl-f8XiYbKd_9dUdq574Q1XmVAGvmAN9mcUgLDMxxyage-8MsqkMSbUOBZKVnWLMDhx0PA1Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdeeeac9dd.mp4?token=LA7IWE4OFoj2oZreK7g6EBMiOTCywmDIF2M35_cabd-m5_gwW3Ta5r5ojKRWiBWFmdqrDJCgckHO4fz48Vu38ZZW7yf_BselVs1n8cPqo-dHp5rn3V64REE2iCdKczQIzb7S1UzqpBwDfi-GPUJhTVS-hMyAG8VpGp20wqPI6bKfCMgAmh2lP8sNt8hke4s0MPNldyLXfA9doBp-Yno3EyrklwOKBLKYUCF8sD2uBIjd9R5Ik6ltEtQztm3idWJ0wSbLMMvhncSeihl-f8XiYbKd_9dUdq574Q1XmVAGvmAN9mcUgLDMxxyage-8MsqkMSbUOBZKVnWLMDhx0PA1Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من تصاعد اعمدة الدخان في العاصمة بغداد بعد الحريق داخل مصفى الدورة.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/88353" target="_blank">📅 15:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88352">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
مشاهد من الحريق داخل مصفى الدورة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/88352" target="_blank">📅 15:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88351">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cb36e6ce.mp4?token=pzaAHkINPQSAc6Mgiv_SDv4YHfx-Z9gJwe1KTjEmmIUKpFw55NLDULwGPl-Z6brEnt6KAFWgfgfqoYN0larQdHq6q9oG0GkV2FxNirVJhw9-JGpkO-lbvlTjBAcScLbamtUoy_ljJP67v9gDstw9pDMh4zDgM6e9bVe5bN7LS29ZEJoB_A-R2bko7D0gFZF2xN8eWkOskfYvvhtFEPOfvugJYIwWoiGdBaX4yWVaa4UaA5MxPcIvGcMUWPHfmX0D_S1oOjkbytyqtikQdzLsb4S8bGzIsLlx9ffEItk7QCq300xPFSFLAi5tyAFkVwYvwnbtKDP0Qy6Gvv6FbQ6FGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cb36e6ce.mp4?token=pzaAHkINPQSAc6Mgiv_SDv4YHfx-Z9gJwe1KTjEmmIUKpFw55NLDULwGPl-Z6brEnt6KAFWgfgfqoYN0larQdHq6q9oG0GkV2FxNirVJhw9-JGpkO-lbvlTjBAcScLbamtUoy_ljJP67v9gDstw9pDMh4zDgM6e9bVe5bN7LS29ZEJoB_A-R2bko7D0gFZF2xN8eWkOskfYvvhtFEPOfvugJYIwWoiGdBaX4yWVaa4UaA5MxPcIvGcMUWPHfmX0D_S1oOjkbytyqtikQdzLsb4S8bGzIsLlx9ffEItk7QCq300xPFSFLAi5tyAFkVwYvwnbtKDP0Qy6Gvv6FbQ6FGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من تصاعد اعمدة الدخان في بغداد وسط انباء عن اندلاع حريق داخل مصفى الدورة</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/88351" target="_blank">📅 15:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88350">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEbePPkRfnlvBESf8DQXD6DAxJvfMPwuyaqpwvuRYSzICNPMQDgn8CFTuUjcnbaquQbqolH4SzwvAUXkiKjbBnSQ4R-9Z7ibtntdZTeSo11NpXCaPRJZm7cDkz0Pb-YF5ypF87xBwK0bs4RdoPju5D5hBC48wLVGmipAYhS9EcuzWqEI2iwERr0QsgkoXNmahAi8zDoS6tlVOJdPsK1MkO6B-SNejg60w5-a4mPoopPIQGuHjINhRCfhCekz4SBoNPYXKVwfWadWL8z4NRWPPYvhq_h7hTTysiEQ-N-pnDQuQNh5pgZDdrq-O69hUd48RTQNrnTkp8BgkiW2iXtuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حريق كبير داخل في منطقة الدورة ضمن العاصمة بغداد وانباء اولية على ان الحريق داخل مصفى الدورة</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/88350" target="_blank">📅 15:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88349">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇶
وزارة التربية العراقية: هيئة الرأي تقر فرصة امتحانية استثنائية لطلبة الثالث المتوسط والسادس الإعدادي
ويؤدي المشمولون الامتحان ضمن دور خاص تعلن اللجنة الدائمة للامتحانات العامة موعده لاحقا، كما حددت الوزارة مبلغ 50 ألف دينار للطالب الراغب بالاستفادة من الفرصة، وتخصص لتغطية أجور الامتحانات ومستلزماتها.
وتكون هذه الفرصة استثنائية ونهائية، ويعد العام الدراسي 2025–2026 آخر عام لتطبيقها، فيما يرفع القرار إلى مجلس الوزراء للمصادقة عليه.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88349" target="_blank">📅 14:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88347">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGTZKheqEs52c5PCtjGH4LSPXRRxCTskhbvy5nqA15Hv8R_95mQdKHkkcQApNEkk1LxdJLrNUhYwWocXqkwlF4OvrKg6aPfDq_TkO08mJiH8QDxIBqmMSUyQM6QxySkq6OAD6c2qbVngbDidSxvt6KwpqfWygKBHXw5RRO9behsQw46-temh0n7vPv0kNAbIL0-5hRJ-nZkYcc8Zm7kzM7k0xQ19-tMY-oPMOFqzN4Jb-8FqE0ZbWJcB0XsYXWQtBvoWKNZ4eok8UwuxgFvtA7-ycilK81o9MiZQf1ehy84JvEdGsmY9YGraxbbRK28BE_RqHFQc9gG2YouR9Xj4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظ على نظافة بلدك من اتباع يزيد</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88347" target="_blank">📅 13:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88346">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
قائد فيلق القدس التابع للحرس الثوري اللواء "إسماعيل قاآني":
القضية الفلسطينية، من البحر إلى النهر، أكثر حيوية وقربًا من التحقيق من أي وقت مضى.
توسيع المستوطنات وجرائم الصهاينة هي محاولة للهروب من الأزمة والجمود العميق العسكري والأمني والسياسي والاجتماعي في الأراضي المحتلة، ولا يمكنها إخفاء الهزائم الاستراتيجية التي تكبدها منذ السابع من أكتوبر وحتى الآن.
القضية الفلسطينية هي حلم حيّ ودائم؛ حلم سيبقى قائمًا بمساعدة الله حتى يتحقق نصر الحق.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88346" target="_blank">📅 11:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88344">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUfla8ry1M0nLw_wmP_C5UugefUX7JN61LXbbx3ZX2UfOCr9Yt-I0CvEbSrLTesbXa3rMt8jLrkGoXI5O03iar1COIvyK0ZE-rxzjbrc14ZMPt3-DSFbMXBoP18OdpbrphMgSy9PYBi4m1a82vSriVUGxyy5MtfKDF6S0GPHmARElgiuCvYpYqoccE66T18s-bqNkB201SLHTQUSxdmzyjBcGjX6o37kTU7SAUgu16eZuedyRA7Ty9O3CKSfJfBAt-ZBn5NCa35Ct0BlXAT1x2a7EWiPPgbScLLFbcLzj1cUTBew_YMppUwf8jI9icVq0_-wlzdoVMJArahwO-0x-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0xaDTKxzOgWupr0mYzkPmGAVZAV4M_trw37RpuAZF8L_VwzqSiAGktRg9wO-w18lBuabSyLhj0IsLZErNnPzDv5jcRyHhdSOijVfr5Hq7wRtWk4S2CNPWSWj317V5m-lhw0D6sq1pntqjx2dCVqKeKyqplHSUm-ckye2LQMp1yHhqb0t324eryIABroiXAIcnhVJK9Gko7wh4c1sujwTGMum8HN8yXqMKWjJ1IHavnOwhWdnciybOcO2qqvgIpS-kBr66FKzK3HMIXaWl4kXSbu1n79rSfOnQgYn0_rBcdf2RfWQn7MixCOBj3BsAh_19OLqWfnngtTODfu5KHxNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
منتخبنا الوطني للسيدات يخسر ثاني مبارياتهِ الأسيوية في بطولة كرة الطائرة أمام الصين تايبيه بثلاثة أشواط دون مقابل؛
"انتم مال دولمة تخربوا بالطائرة ليش"</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88344" target="_blank">📅 11:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88343">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏
🤡
زيلينسكي: اتفقنا مع ألمانيا على توريد 600 صاروخ اعتراضي من طراز PAC-2 خلال عامي 2027 و2028</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88343" target="_blank">📅 11:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88342">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
الإعلام السعودي:
قائد الجيش الباكستاني سيحمل رسائل أميركية لإيران خلال زيارته غدا.
‏زيارة قائد جيش باكستان لإيران ستحاول كسر حالة الجمود واستئناف المفاوضات.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88342" target="_blank">📅 11:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88341">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇸🇾
🇮🇱
وزير خارجية الجولاني:
نتوقع استئناف المحادثات مع إسرائيل بشأن اتفاق أمني قريبا.
سوريا تمد يدها للدبلوماسية وتحث إسرائيل على اغتنام هذه الفرصة التاريخية.
الاتصالات مع إسرائيل انقطعت بعد هجومها على قاعدة أبو الظهور الجوية في 18 أغسطس.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88341" target="_blank">📅 11:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88340">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165cbecbdc.mp4?token=ZlCcT5N6kHEUgJtoki6WLzc4Md_8sRRIBl1wcIUqWLoe9ZhWBaHwksgSeDMhZBqYFueMGwvtTK_96jL-4EEjD6ecfbeCI0M3A3rxGKvGDWGRP-xm49x70IZYjtVHcpwvf86big0Ga54rqMyepYhxUzm81_pNhmBpbv4EdU5HuEwz-rtLyFzqFRkwC_mnZxs0RYSgUDKpDkXHluJNoB0t0rL44kDA-Y1SySofoZgIsNyjkAq6OdhXAzup_g6q4SbpcCR3INZv6mhLM-Jmq24T2XQ1vDid7pcq48DLhac4lByCNkUZqGyTUv6qISBVpARHFNA1oeJmmzSLwML5JPjY4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165cbecbdc.mp4?token=ZlCcT5N6kHEUgJtoki6WLzc4Md_8sRRIBl1wcIUqWLoe9ZhWBaHwksgSeDMhZBqYFueMGwvtTK_96jL-4EEjD6ecfbeCI0M3A3rxGKvGDWGRP-xm49x70IZYjtVHcpwvf86big0Ga54rqMyepYhxUzm81_pNhmBpbv4EdU5HuEwz-rtLyFzqFRkwC_mnZxs0RYSgUDKpDkXHluJNoB0t0rL44kDA-Y1SySofoZgIsNyjkAq6OdhXAzup_g6q4SbpcCR3INZv6mhLM-Jmq24T2XQ1vDid7pcq48DLhac4lByCNkUZqGyTUv6qISBVpARHFNA1oeJmmzSLwML5JPjY4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
🇮🇱
لحظة إنقضاض البطل الفلسطيني على المستوطن الصهيوني وتنفيذه عملية الطعن.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88340" target="_blank">📅 10:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88339">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc7fc53e44.mp4?token=DLMLewwoXmDCYKYir-3z60Dl9JZsEF3o3WA7fhO4V1htp16EP15_btvJszyzgp3hb5XzGoTSYHfazlSfmLX4k2ccU9e8NVJvTUa-ryCN6r4yfGZULKPw3Zuul2BZWVv1uz2ll0BniSVNNy-Hme7hWn4JvxnjNqiDOjm8yzg3VBDbo10u_pVUkjXguf6VoaLnxEF1MUXxMdunilSXWn8V1vo5OvwB3PuvHvONOveCW1DOwnwXL0GwVvp751RDebndYzW_1_T09lknwxyenMFoaJFUSXxwAK_HGElMtinh9o5y6BLI92UqIoi9F_nagbz0vCMY2EiPrSx_vmtmOlDDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc7fc53e44.mp4?token=DLMLewwoXmDCYKYir-3z60Dl9JZsEF3o3WA7fhO4V1htp16EP15_btvJszyzgp3hb5XzGoTSYHfazlSfmLX4k2ccU9e8NVJvTUa-ryCN6r4yfGZULKPw3Zuul2BZWVv1uz2ll0BniSVNNy-Hme7hWn4JvxnjNqiDOjm8yzg3VBDbo10u_pVUkjXguf6VoaLnxEF1MUXxMdunilSXWn8V1vo5OvwB3PuvHvONOveCW1DOwnwXL0GwVvp751RDebndYzW_1_T09lknwxyenMFoaJFUSXxwAK_HGElMtinh9o5y6BLI92UqIoi9F_nagbz0vCMY2EiPrSx_vmtmOlDDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
عملية طعن في منطقة الأغوار بفلسطين المحتلة، إصابة صهيوني كحصيلة أولية؛ المنفذ تمكن من الإنسحاب.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88339" target="_blank">📅 10:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88338">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تستهدف مواقع مرتزقة السعودية جنوبي مدينة الحديدة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88338" target="_blank">📅 10:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88337">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vObk_uFV-7XgXvNOdSRPZcC9zFAQw-lw1TJUEn9mPdV6Dg6KHHDdC7b8f3Qs9mK8lZEoc-V3KYjOH41q4f-aSW6Qgmi5dnant5_BUrcSxaplOmGb2JBmd99BP1P45DHqyxk-sK-zmIl-D9GpTebY6HiiZzSfcpa6Jbft3gNIIKsD8-VriQ-nQAv6tGffIlUPddULJWiC4UB2oxHC_JHNYgTTPvedOuI84WiAHBByNNJ4eOFce1UsJLaMb3aKFpPMUFa_KTXDRIXhjv3qeKTxjF7s8ARUyH5y1IfFnOqVAXou3Tujzhib5_w4TD59EM-V_K8-8Pw3xfrB4tkNZuLySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
عملية طعن في منطقة الأغوار بفلسطين المحتلة، إصابة صهيوني كحصيلة أولية؛ المنفذ تمكن من الإنسحاب.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88337" target="_blank">📅 10:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88336">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReIK4bNR7OAE0vRRy58JIPC7Y90OfGTwNCvMWrsO8gJ4Xk-ZGY6FlB6RZAxPmG2wS1fqJYAdoVVGoqOIan86TJiZsn9fu0ymKLFvMiVZ3SzDceFxXmlpcGV74Ot-mjpC3P7rrVwcaT2MftAsnVGKqW5cIiay4RoLDZWKSBPRBvjJo8pAcy0Ao8H9scgdSTKTa8bop6pQqgRZGVkIflFg5ixNYAeF9_En8e5oGQ6_LiMEaKclPOqHvVzaxGxFGdlkVACJT-wbgy5xDcPcrPptaJdejSTf3yRuV6soD1j3XwY6rgobQOfZ3V5Qo_bjMxtTU9t6cEVZ06aUKlwSqO1uEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يهاجم كندا مجدداً.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88336" target="_blank">📅 08:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88335">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQj_yMZ_ACR9_-cAWQXZHIXXXeowZu0usQou18p_Cz5D9mRC3KyhrlLElX1w1JX3G0SpZVwXEbpfT0KNLyR45Wc47KozqST9HijVH7rvsYoI6ZecJuNmb1GNWitfTfpMv124-X0wKHAAloFieRGTOxm1O5wN-sLiTKWnm0t7kxTu8inIBzmmly1fzni-mOVQGlY2rvEIVqOad8UknCqfNdIxwMx4EE4xobelxeq3RAO5eGhffq3JYtcQRYa5w3T8F8-Sgo5XQecd-LpC9M3jgJmq66jHkIcVpHcDg1PbyzLjCRpqpyip186txXLLNCS5VBbtqwFK3OHx8fgMK3n1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاعلام الغربي: ‏
هناك أمر غريب يحدث مع ناقلة النفط "نيو فويج". لم تتحرك بالقرب من مضيق هرمز خلال الساعتين الماضيتين. ويشير موقعها عبر نظام التعرف الآلي (AIS) إلى أنها راسية. كانت متجهة من الإمارات العربية المتحدة، والآن عادت أدراجها دون أن تتحرك.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/88335" target="_blank">📅 00:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88334">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2zXXQ8HgMCqEkUpFpozzEQliTEgvXLJHRzrbSbgPw8eLf3cM2rDgLUMqtjjJyJwnCQA0nOf21REojr889GZb9c9f-QBzhM5-7B9G0INpYsQ0_vIjvfAkgvtvRqIQTtZFbfBkV7A8Q1DaJhIDwF8M6zSgZgLGFk20uco93h7tFTMplTZkxrMVzSbQcz44o6GWYOVqzbKBgPTR7Tp38Jo9RV0lShuTpEsAcORVb7nVRvwlDYfu2U7MRoAkvEkMjRf18366JKK7yDeRlwcmBk9BAStvfNm03KGpfXKbNii9iATs8LiXZqnhlTks8OAjXcz1OWO1iLbNdnSByeTotLtgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب يعيد نشر تغريدة بخصوص مضيق هرمز اراضي امريكية
😫</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88334" target="_blank">📅 00:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88332">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07055ecbb.mp4?token=nsNy8JRLjlbUW6HcC_gU6BmhRZrS0YUOFCb8D1UGRgovP6NjBZa87uDFayM0RmowjI0AB475pYvt1drzmKeFz3r5biSkfSZYNt1IAvxVgm9dr_I2zN6JT0_b8mvW8hXAgxC4WCUXisyqZ40bVVNYbSqFEiiyeq8vUyp1jGoguhaDtW_2jEUVYr_Bo6g8Wbydkf-tmSGN6coyX50FJvrPQSD0CcS1M1kpXqh7AdqOlTqIvQDKy3mHs6O4sAqabAcdUSHdfEDFZ1SMbK9QsyTjAyulSUPvLiledDfq4Ne7ysSHknvfhUcd-VKmyUGlVTfKJ8B-ipZ8W4R8QQazFSeFTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07055ecbb.mp4?token=nsNy8JRLjlbUW6HcC_gU6BmhRZrS0YUOFCb8D1UGRgovP6NjBZa87uDFayM0RmowjI0AB475pYvt1drzmKeFz3r5biSkfSZYNt1IAvxVgm9dr_I2zN6JT0_b8mvW8hXAgxC4WCUXisyqZ40bVVNYbSqFEiiyeq8vUyp1jGoguhaDtW_2jEUVYr_Bo6g8Wbydkf-tmSGN6coyX50FJvrPQSD0CcS1M1kpXqh7AdqOlTqIvQDKy3mHs6O4sAqabAcdUSHdfEDFZ1SMbK9QsyTjAyulSUPvLiledDfq4Ne7ysSHknvfhUcd-VKmyUGlVTfKJ8B-ipZ8W4R8QQazFSeFTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الأمين العام للمجلس الأعلى للأمن القومي الإيراني "محسن رضايي":
إذا ما أراد ترامب القيام بأعمال ما، فسوف نردّ عليه بقوة وعزم.
بالتأكيد، سنقوم بإجراء تغييرات في مسألة إدارة أساليب الحرب، وستحدث تحولات في السلوك الدبلوماسي لإيران.
نقول لجميع الدول المجاورة: لا تشاركوا في الحرب الاقتصادية الأمريكة ضدنا، وإلا سنعتبركم أعداء.
نحن لا نسعى لتوسيع نطاق الحرب، ولكن إذا انضمت الدول المجاورة لإيران إلى الحرب الاقتصادية الأمريكية، فسوف نضرّ بمصالحهم.
إذا انضمت الدول المجاورة لإيران إلى الحرب الاقتصادية الأمريكية ضدنا ، فلن تخرج قطرة نفط واحدة من الخليج الفارسي ومضيق هرمز، وسنستهدف أيضًا الطرق الأخرى التي يتم من خلالها تصدير النفط من الخليج الفارسي.
مضيق هرمز مغلق ولن يفتح إلا إذا التزمت الولايات المتحدة بجميع التزاماتها.
أنصح الأمريكيين بعدم إرسال أي قوات إضافية، لأننا سنرد عليهم.
أي حركة تقوم بها الولايات المتحدة في الاتجاه الجنوبي لمضيق هرمز، ستكون هدفًا.
أي اجتماع يعقدونه مع جماعات معارضة للثورة في المنطقة، سنستهدف ذلك المكان أيضًا.
لم نقم حتى الآن بمهاجمة أي من المصالح الاقتصادية الأمريكية.
حتى الآن، استهدفنا فقط القواعد العسكرية، ولكن إذا ما تم تصعيد الحرب الاقتصادية، فنحن مستعدون لاستهداف جميع الشركات النفطية والاقتصادية الأمريكية في المنطقة.
سندافع عن إيران بكل قوة ولن نسمح بعودة الأمريكيين إلى إيران.
نبيع النفط يومياً بكميات تعادل إنتاجنا، خلف السفن البحرية الأمريكية.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88332" target="_blank">📅 22:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88331">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
رئيس المجلس الأعلى الإسلامي الشيخ همام حمودي:
لن يفلح أي رهان على حرب شيعية- شيعية بوجود المرجعية العليا والالتزام الديني ووعي أبناء شعبنا بحقيقة المؤامرة الخبيثة.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88331" target="_blank">📅 21:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88330">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d826f753.mp4?token=NkDO_biuSiNTZDo60z2rsfYvk8ZGWgTLwF-ZafaNI7Nt1L1CuEHmM6cpXeDGR0TqgYQ5JiP5fklwcbEAxrnP1qhrQZZ9tO7s-H9Mhg8Lrk_fHTLG9yRr9z-r_DJsq3r5LSwBSMRshkppj9r1ZQe5wwWSg3ZnFFsWcGiT4o3X5koF0LBNqRrGEKFCzVvKlP7utzzyVC4p8OJQfR-duDXEuUgit-u6ONh-ngE3iYoDfVKQ_xie50FXun9JnvRA1UTBEXVBcSLtnh22WZaIQlx-9QcWbd1AeCtx-RpvlxozhgQ-MtA8vtUB2vzGQm_dW-kOBff5HuHii6mzUe5r4Z4Yzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d826f753.mp4?token=NkDO_biuSiNTZDo60z2rsfYvk8ZGWgTLwF-ZafaNI7Nt1L1CuEHmM6cpXeDGR0TqgYQ5JiP5fklwcbEAxrnP1qhrQZZ9tO7s-H9Mhg8Lrk_fHTLG9yRr9z-r_DJsq3r5LSwBSMRshkppj9r1ZQe5wwWSg3ZnFFsWcGiT4o3X5koF0LBNqRrGEKFCzVvKlP7utzzyVC4p8OJQfR-duDXEuUgit-u6ONh-ngE3iYoDfVKQ_xie50FXun9JnvRA1UTBEXVBcSLtnh22WZaIQlx-9QcWbd1AeCtx-RpvlxozhgQ-MtA8vtUB2vzGQm_dW-kOBff5HuHii6mzUe5r4Z4Yzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الإمارات تكمل بناء أقفاص معدنية ضخمة حول خزانات تخزين الوقود في أبو ظبي للحماية من هجمات الطائرات الإيرانية بدون طيار، وذلك بعد نحو أربعة أشهر من العمل.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/88330" target="_blank">📅 21:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88329">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWogY4dxc_grHN9zi-98PbV2vzrA4nIyWHjLnV1VfNJgdT87-XoiaNNWP_wd8EtsWjLKSQ3H-V-Iv1S9p_iGVaS4PziEmefOj6zZJaFEua9y0i9jb6a7t4QrUiskm3vBK6_q_AZ6Ij4ap-LqjR3h0okfWr93vKPJBV9oFHBKgjih-hpX65HVdg_SN81SsJwMJm9Ky191_Rkqf7-GJ4uuGnrQB1JoGr2pwjU70vfsTKd9kTGIZYoyT3MRAge3xdIpGjsT0mAxEx9i_2EGlo1_DfFCLB-jO-0kA40Mvq2WIrhs7ARnVi67gc4omeSysJKq1KFrY8Ivw-hzU0UXamcVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
غارات اسرائيلية على الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88329" target="_blank">📅 21:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88328">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇱
‏
نتنياهو
: لن تقوم دولة فلسطينية تسيطر عليها إيران لا في غزة ولا في الضفة.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88328" target="_blank">📅 20:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88327">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0551d70e8.mp4?token=XDvAC8hiB9iDsb71XSxb3Vsksmf2YRfiyhoUexIlCJsQ136zZ2gzEZRKz2VxSxsmGO3WMEhZw4hUx-1Wozxc6KpFY1HzJwj5woda3af8lEo4onlX84GNp0SqHeB2utyW8e1MXfuhbhJWT83nurJrhxgROJruuIx19fc4FET0BKwb2nCpWZtyuIa-1WmkTWHXNeJPBGuQ2NKXdkfpSJj9OD5b7Q6ZHqDhRKTk322QHnbsRRJyOpkvKlG2O9lRjFKxM3rdcCPWl4M584ro8dtsJCAixy9d2L5yfgrLBYBlU3kzXfjbmHM3KBkby7_GNE08fI-qcu1xxa2WjV8gGFDhxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0551d70e8.mp4?token=XDvAC8hiB9iDsb71XSxb3Vsksmf2YRfiyhoUexIlCJsQ136zZ2gzEZRKz2VxSxsmGO3WMEhZw4hUx-1Wozxc6KpFY1HzJwj5woda3af8lEo4onlX84GNp0SqHeB2utyW8e1MXfuhbhJWT83nurJrhxgROJruuIx19fc4FET0BKwb2nCpWZtyuIa-1WmkTWHXNeJPBGuQ2NKXdkfpSJj9OD5b7Q6ZHqDhRKTk322QHnbsRRJyOpkvKlG2O9lRjFKxM3rdcCPWl4M584ro8dtsJCAixy9d2L5yfgrLBYBlU3kzXfjbmHM3KBkby7_GNE08fI-qcu1xxa2WjV8gGFDhxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رصد نايا
منصات مقربة من فصائل المقاومة تنشر  مقطع فديو لم يتسنى التأكد من صحته مع عبارة " ستعرفنا ستعرفنا قريبا " المقطع اظهر مسيرات من طراز حديد 110 التي تعمل بنظام المحرك النفاث .. فيما لم يعرف دقة او وقت الفديو او مدى جديته ٌ ..</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88327" target="_blank">📅 20:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88326">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrl1C-XJamRQJYcCfyf9hmbZrmaPpFM4zTPV1cSQTwfs6uteHR4SH8dBzHmlCnsx_IJjLRWiY_Br5daW9Hzjj3qwmY8qT-RFdqlBCXVIiOrSPN3GQULZZflkosXtMsYlJjbRfR_VFo7UI_D7wQ7iZoxQpzhkd1VylJMYXwqD20lrk07VLZyadQNesvEU-CQ_G4XGwsgzMcOb-7FDybUFejAWAyJcfX1jkkB-1x6tfoOUi3I6-UdkBp9WceU4iojwjRj2CxFODmoRfLiBnwwlXsqheM274QnVFvreUG94_1XG1bGW038i9zKFs_BfSryD2EuQ5TRPiMRF2SI86GKJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العبوة انفجرت بباص تابع لعصابات الجولاني على طريق معرونة – صيدنايا بريف دمشق</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88326" target="_blank">📅 19:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88325">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجار عبوة ناسفة في ريف دمشق</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88325" target="_blank">📅 19:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88324">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجار عبوة ناسفة في ريف دمشق</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88324" target="_blank">📅 19:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88323">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏
🇮🇶
وزير الاتصالات العراقي:
ملف حصر السلاح بيد الدولة يحتاج إلى واقعية ونقاش عميق ولا يمكن حسم ملف حصر السلاح بيد الدولة بمهل زمنية محددة أو تواريخ ضيقة</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88323" target="_blank">📅 19:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88322">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇨🇦
رئيس الوزراء الكندي:
لا يمكننا قبول عرض الولايات المتحدة، ولن نقبل مطالبها.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88322" target="_blank">📅 18:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88321">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc26914f9.mp4?token=sWzdoqioFpy_bEQ7TReC9WthLnwanMtUs8KhkORdV4_FUcve91k1F2l0zcL-d-9Fm9jtEfZAD4rjmdhgtDf-HLe2YdKDgpom1b4cvmX9Ifrd49QUzbrmmOxD4QTA0ZIpasArXzox30hjErBzF3dDrsNn30fECu5NIOVuSddfDKc96cL_7bXolezXC-INxv5bcG047OKzhmKF2C9hx9mqZX-c5fExonn2eaEZLUDCW1cHyUsGO9fPVBYJPFeTm2BkdBbGYXVP2zX_RBXOQ1P7b8PxsPFo_wqfbioK6C0w7WfEikx7X4DY_9FOS0vQs19ilYv_T7IaN70k2Va-O5SkjJwA0bFWe2vw_3QYpjjoRZgzSjPemXUcHtKDJUc-wvXsdJ0lxWTBQbBYGqy6p1Jgh3RoByQf8o1GeG5B8tfG480cIIRkRN3yy06M9Y9AnCWhYT6XUG4gzGrchMTA9ixoXv_ozDrxFe7mFvSYvQdUmAAaXwi1v46v5oSiEMbVkMQxhEzZrav5JkGZ7WVW9Ik7WhQVC-FbcUpOtrnUmKIxXzbKMLnqd9TCeHLQ1m4_6oMYMfbpcxKuJ6QJ8nMwKu0jjMutnecdr-GVeLuBqkv3Sj-RRYEVRTGQNonzTwTK-uZBSzOjI7pC_Pvzw6wmbCUeNQF6noS9PK4AuyutZFnydOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc26914f9.mp4?token=sWzdoqioFpy_bEQ7TReC9WthLnwanMtUs8KhkORdV4_FUcve91k1F2l0zcL-d-9Fm9jtEfZAD4rjmdhgtDf-HLe2YdKDgpom1b4cvmX9Ifrd49QUzbrmmOxD4QTA0ZIpasArXzox30hjErBzF3dDrsNn30fECu5NIOVuSddfDKc96cL_7bXolezXC-INxv5bcG047OKzhmKF2C9hx9mqZX-c5fExonn2eaEZLUDCW1cHyUsGO9fPVBYJPFeTm2BkdBbGYXVP2zX_RBXOQ1P7b8PxsPFo_wqfbioK6C0w7WfEikx7X4DY_9FOS0vQs19ilYv_T7IaN70k2Va-O5SkjJwA0bFWe2vw_3QYpjjoRZgzSjPemXUcHtKDJUc-wvXsdJ0lxWTBQbBYGqy6p1Jgh3RoByQf8o1GeG5B8tfG480cIIRkRN3yy06M9Y9AnCWhYT6XUG4gzGrchMTA9ixoXv_ozDrxFe7mFvSYvQdUmAAaXwi1v46v5oSiEMbVkMQxhEzZrav5JkGZ7WVW9Ik7WhQVC-FbcUpOtrnUmKIxXzbKMLnqd9TCeHLQ1m4_6oMYMfbpcxKuJ6QJ8nMwKu0jjMutnecdr-GVeLuBqkv3Sj-RRYEVRTGQNonzTwTK-uZBSzOjI7pC_Pvzw6wmbCUeNQF6noS9PK4AuyutZFnydOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇮🇶
مركبة تابعة لجيش الاحتلال التركي تمنع شاحنة لمواطن عراقي كردي من المرور في قضاء شيلادزي ضمن محافظة دهوك باقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88321" target="_blank">📅 17:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88320">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انباء اولية عن اختطاف أكثر من 60 مصلياً من مسجد في نيجيريا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88320" target="_blank">📅 17:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88319">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2655fd592.mp4?token=p-Ll6oLRYw0rUpCxDjUmRjG1ENM3IP3NRGQG9WmBiLTnGbiepAN0HDcVZsXsCaye3MJm55Dp1zLI-mHSk-4eLPiOe0OyXJKJyPTeOgvF5QQ8j8ne_o_iauQVdrqh7vjmVz8IgizqxbDKpDf__F9ixAQxZZ-5vcthI2nz9LOJR409xajXXk7wS5bPBm8mDw6jzfqd90dh3dveyWbyKLRhjdB7vzCx5ILysCiwKx8A2t8hcwYA8dSi-Ve7ruYG2Ptyhbl-Dcy2JGie9rSi6Qfwr71WYJAsPvdWXjlR5APLmsHNNiAC3q3Pq6Odo520UmjYCb6szwqtKKI6R9YyOmNpAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2655fd592.mp4?token=p-Ll6oLRYw0rUpCxDjUmRjG1ENM3IP3NRGQG9WmBiLTnGbiepAN0HDcVZsXsCaye3MJm55Dp1zLI-mHSk-4eLPiOe0OyXJKJyPTeOgvF5QQ8j8ne_o_iauQVdrqh7vjmVz8IgizqxbDKpDf__F9ixAQxZZ-5vcthI2nz9LOJR409xajXXk7wS5bPBm8mDw6jzfqd90dh3dveyWbyKLRhjdB7vzCx5ILysCiwKx8A2t8hcwYA8dSi-Ve7ruYG2Ptyhbl-Dcy2JGie9rSi6Qfwr71WYJAsPvdWXjlR5APLmsHNNiAC3q3Pq6Odo520UmjYCb6szwqtKKI6R9YyOmNpAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدور مذكرة إلقاء قبض بحق مواطن سوري يقيم في العراق على خلفية امتلاكه عصابة وقيامه بتهديد مواطنين عراقيين بعصابات الجولاني في حال توجههم إلى سوريا</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88319" target="_blank">📅 17:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88318">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇱
🇸🇾
‏
وزير الحرب الصهيوني:
وجهنا إنذارًا مباشرًا إلى دمشق قبل تنفيذ الغارة على "مطار أبو الظهور" وتم إبلاغ السلطات الأميركية بالمعلومات الاستخباراتية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88318" target="_blank">📅 16:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88317">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCr7hTbXTnPB4jFu3D1k_BCQktIjwVQcLRtOwU3lltq4FAsCDASNVhryhC7uXcwI08KEbplhdWCnjv7j4muywtnFANvqVfaIVUZq4uXoFsjg5Tio8yofUNp_khYGZCIczjizpAnKd-_xOdLFdLjCBrViaGdJ7bhNceUHLrsGD1QMjy84Qdab4AdULpYH-8-2KydmonnC6lMoDq2a5cqTEPn-mYmQRYPlYEW5yZT00B4nSN0WiGPMRfsMUQfBd6sdGSrGe1GDKx9nzr9CElSptsSRier33lYs4NmQNHfNEH2G8DK2P4lg1ZTZO-uwlKlNvxV6iFJIJ_JgBCz1XPvt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
بيانات التتبع:
‏
تستمر صادرات السعودية من ينبع في الانخفاض. شحنة واحدة فقط من ناقلات النفط العملاقة (VLCC) قيد التحميل. ترسو عدة ناقلات من فئة أفراماكس أو أصغر حجماً في رصيف أرامكو. من المرجح أن يكون إجمالي صادرات المنتجات المكررة والنفط الخام أقل من 4 ملايين برميل يومياً. ربما يلجأ السعوديون إلى تحويل مسار النفط للاستهلاك المحلي بعد هجمات الحوثيين المتكررة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88317" target="_blank">📅 16:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88316">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">لحظة الانفجار داخل احدى المصافي في منطقة دارمان ضمن محافظة كركوك شمالي العراق</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88316" target="_blank">📅 16:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88315">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE-D4lbnsm2ftbAC9jBzeZd9RzXGnkDbqcuJ9rD2Ts4Q9GzLMYN-Xt6uf-Zix0rd-UfezWwD1pO_8VE1fg-tuhX5_jAdXo64bAY0BAj8RStfBDRz5VouIh_-YttnEY5U0ROLCJY-JAW_Pps9E5CBbsD0CKmH5FfyG5jym_XI6TkrPijgvf7taSQpqo-Sp8BHYRyXJorucdgL-99YOlzv4lHwTGrwHQNbpjVt3qfe3J-uDaTA_cdI0wtk5tobGPsc2gV5-Pg8K8hAUcgXORH2wm96yYUxJq3cXRPN_jC_KSLWVMYQZf9BBAxIzWkEc5br8ApKDTWRQLnd5k3WBbw9rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
ارتفاع اسعار الحديد في دولة نيكاراغوا
#دنيا_وصفت_ياناس</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88315" target="_blank">📅 15:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDIpXv23Z4n0RfjUjt7exeyFbrOOEEds6or96KF49F-G3dSWLsnJLUsLAqawuoQ_6SewuKtmCyT8vk24ScTFyLb0ZmEE3E8LSKFBDuKmVFXybh078cccxjHy0WG8q4qRu9et86vDDh1_42UxaeRRf1cVXdEt81GfS4g8qvTJXOsWaPUhJjGfmYB98iMaMeXUrYtLFhy-rvwO71P_Hb9XbewQTsDmUfiXnp9Z5r9UFodwOEJI7B0nr_NTOYeaoQGSNBLZHnxRZeQ4J9BAJgoR55FpLfY-YnOFpLyYsMn7Z_l_OZ3nGDI3DyyBH8dT3PqUfWqekye-ab8fiMJlYGOrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZC37AmK13jTr5Ae0bpFDUN7kYd2cO3_q5QcOJkvSRNts7u8altyh_g6uuFzhgW8iSksUuI3tvW3trlvFDqB-iVE_8IYGblqrk9R0dobgo-zOEgrf5lv3ZDJNTyg_Z27VMnnSHOU3iKHJAMunaGP0Fd9HeHmk_vaQuh5lq-OWj36LNR56kSxFlixUqVRs1DozEOz3_OgZdCPRbLS1qbUFu4y2ER1ney_2k3QQMhQW5nkbKARnwcd58eVBNN5c9sUmqz_j5m979TV7fZwLPXe5psy_SKUPbhcxp7l_ZfaJ-6JByebTbxOJhDo4BU0HPVAT_ZVg3jL3SksqU9tMONrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IR0tniIj5JXehOh5yccSWgnAVnIe3warhe80Y3UUa7kJ3hHFB6Quni-KiiCjyMAiuMz6noXF_PcAURseBWA96sITHf47T7nERq-ljBqfmGL7nYZM_Bo2_6yfUPgTlm9G8Mk8f4MlvugyEhiG2zUXALLrYNyPAlf6uKMiqAKXcojMPjSuDbWF0oF_2ZpTuts3gk0sL7t8V1u8lynA4XVsQUXsWTI7cHkyg5xkSj0YHnU8wNe5sTIb6BNCUzA8jhK3R37Zz8RchJRja7PNHPCLoxWLfy_2lmADaVZKdcz81LHQCO6cA-H0xtz3lvFeNmC2MpalZJ2_zslafNBjxUNfTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
تمهيداً لمعركة كبيرة في حال لم يسلم لاهور نفسه.. نقل دبابات الى محيط فندق لالازار بمحافظة السليمانية مكان تواجد لاهور شيخ جنكي.  انتقال تانک به اطراف هتل لاله‌زار در السلیمانیه که "لاهور شیخ جنکی" در آن حضور دارد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88312" target="_blank">📅 15:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b84232b8c8.mp4?token=KsNqMCR5J1c1-zG3HGNbB6lEGYi2MzphlURRi0AGuhPNVzhGskQl7BdpLUJt4wwcj_wu3keuMhJS-7wR0_HffpRKgnAzNP3vhZ6Wc_5zCmlnq2FT2fBIE2b9ZCsVD3cDeeFwprvIxT8xAmuLEWsdDfcRulrnwgEpP6TCCBmqpwdxNiN68PGBL_1q1WT0OZA3Z1c2fs0wIXyw_dzirZwTE5G_hhZY8_9vuQR8rCjToAxQeghWJyh1uumyqab_OLIokOYja36jpJ_eEQueF9lZoCVxKGWflMT_04ANciR7uL7fl6A-9EztOjF393l610CYAFxhJwXrc7oVdVtW-rRiXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b84232b8c8.mp4?token=KsNqMCR5J1c1-zG3HGNbB6lEGYi2MzphlURRi0AGuhPNVzhGskQl7BdpLUJt4wwcj_wu3keuMhJS-7wR0_HffpRKgnAzNP3vhZ6Wc_5zCmlnq2FT2fBIE2b9ZCsVD3cDeeFwprvIxT8xAmuLEWsdDfcRulrnwgEpP6TCCBmqpwdxNiN68PGBL_1q1WT0OZA3Z1c2fs0wIXyw_dzirZwTE5G_hhZY8_9vuQR8rCjToAxQeghWJyh1uumyqab_OLIokOYja36jpJ_eEQueF9lZoCVxKGWflMT_04ANciR7uL7fl6A-9EztOjF393l610CYAFxhJwXrc7oVdVtW-rRiXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الإمارات تكمل بناء أقفاص معدنية ضخمة حول خزانات تخزين الوقود في أبو ظبي للحماية من هجمات الطائرات الإيرانية بدون طيار، وذلك بعد نحو أربعة أشهر من العمل.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88311" target="_blank">📅 14:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNFPegoyDaPgLY-wvNRHvgDQT4pCOOmedCkVUSp95wQax93ewwsgyWIeHlXorA9JR3Hsv95YG0ihP6TmlIQucF0IEkSXHI_U1d8iQmCznRMWKbVu4rJsCUCvv-doSmiiA68xU8MhTkzGNlDXTdixnxELh4VqAByiTOQEQPWVoI3U38dkV1__oQrDdizcLM-a2cF01zEuxJB-whNF-j6OSc6GKvjwbrT511WN7abHibaET-QWlgSLa2JjdJNQDfAlHeM5K-7SMcBqBlw25rGjIvmH19zdTREUTaLrW9SkYQGF1XxeNTyEvhxa80Csh59W-iXVO_0E_Kv_BwDIh5kN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد باقر قاليباف:
لقد تلقينا العديد من الرسائل من الدول المجاورة بشأن صياغة ترتيبات أمنية جديدة وتعاون اقتصادي في المنطقة.
‏لقد عرّضت الولايات المتحدة أمن كل حليف من حلفائها للخطر الشديد من خلال التنمر والتجاهل التام لمصالحهم من أجل إسرائيل لدرجة أنهم رأوا لفترة وجيزة وجودهم كله على المحك.
إن النظام المحلي المستقل هو ما سيحقق السلام والأمن فعلياً.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88310" target="_blank">📅 13:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88309">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaBitrCGN6u8wGTIjvXx3EUwa9FsZqYnBLbN2-rGBuzAbV5EGs9iJibBIyxPF65-aXZkJDUN1-3BPFIVI6w5kNV6oqDf789z7BG3Mk6cq7-5ECacNkw9_j1Wa2TjEaUIKvy7nsrQgo_x00qT9LbSBxn-tKkZ_qPc2-TP7yoiJQDcEEI4_BtatxvNX2i-DYxl7mQ9ySyGJhpCr9n21mqrhxanA4yeBZMGLoj-pdKlAgWfLj4KAvLYoTSgpBe-btf_T0-_qBSO6-LcX5iV2_pTvxvWfj8WpACYuKxS5jeJurGArMosqcnYcqbpkJ79cGi_4n_rQoDhe7uldp0MK1SjPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇸🇾
جيش الاحتلال الإسرائيلي يستهدف عجلة بمسيرة في ريف العاصمة السورية دمشق؛ إصابة شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88309" target="_blank">📅 12:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇾🇪
🇸🇦
مرتزقة السعودية:
الهجمات الحوثية أثرت على ميناء المخا وحركة الملاحة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88308" target="_blank">📅 12:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
قائد لجنة البحث عن المفقودين الإيرانية:
الوضع الصحي للطيارين الإيرانيين في قطر ليس جيدًا.
مكان احتجاز الطيارين الإيرانيين في البحر لا يوفر الظروف المناسبة للحفاظ على صحتهم.
يجب على الحكومة القطرية نقل الأسرى الإيرانيين إلى اليابسة وإلى مستشفى مجهز في أقرب وقت ممكن.‏
ندعو الكويت إلى إجراء اتصال أولي بين الطيارين الإيرانيين وعائلاتهم.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88307" target="_blank">📅 11:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88305">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇶
رئيس الجمهورية: هنالك تسهيل لبعض البواخر التي تحمل النفط العراقي في مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88305" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88304">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
🇮🇷
مصادر إيرانية: إيران تسمح بعبور عدد من ناقلات النفط العراقية من مضيق هرمز بناء على طلب بغداد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88304" target="_blank">📅 11:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88303">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
مراقبون يگولون تغريدة " لخ " أخرى إذا صح التعبير من ابو مجاهد العساف والجماعة حتى باميا للمواطنين بفرحة الزهره يوزعون .
النجباء مسوين شده يا ورد وزيارات وكذا على قادة الإطار التنسيقي مرتاحين لشوفة العامري حتى واحد منهم گال جنه يم هادي الكعبي مو العامري .
خبر " فصيل مسلم أشياء للقوات المسلحة العراقية و الأمريكان كانوا حاضرين للمشاهدة خبر حقيقي  " .</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/88303" target="_blank">📅 11:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88302">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
مسؤول أميركي:
لا توافق بالآراء حول حرب إيران وحل أزمتها داخل البيت الأبيض.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88302" target="_blank">📅 11:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88301">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
🇮🇷
مصادر إيرانية:
إيران تسمح بعبور عدد من ناقلات النفط العراقية من مضيق هرمز بناء على طلب بغداد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/88301" target="_blank">📅 10:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88300">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
"توم باراك" بخصوص الشرق الأوسط:
أُرسل جميع الأنبياء إلى هذه المنطقة. ليس إلى منطقة البحر الكاريبي، ولا إلى أمريكا الجنوبية، ولا إلى أمريكا الشمالية. ‏"إذا لم يستطع الله نفسه حلها، وإذا لم يستطع الأنبياء حلها، فإن فكرة قدرتنا على حلها في العام ونصف العام القادمين تبدو ضئيلة للغاية."
توم باراك صار يكفر بعد فشله بحصر السلاح في لبنان والعراق واليمن وفتح مضيق هرمز
😆</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/88300" target="_blank">📅 01:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88299">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي وإنفجارات كبيرة تهز العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/88299" target="_blank">📅 01:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88298">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz0EaWzQFUYWzeEQP2QhB2V-dJPLyvSvUi6cDgWEZOGYvG7UbxUGg4h3B21jblU_kQxFxfQrrdIy9AJos72U6YF0RmaSm8AOMWFny9mBc6OTzKYn1d-WGShrFroPm4oDDE3ekVFi3IIebI6wJuy8afRxmaMkHH-1HpH1zn308pji6mW1JI4ziE5kP1i98j47GNrUTDzUKxA5j0B7CvqnkwFAmZ5RMSHDmsVIOq7iNxqmZsQ56bWwpNihEsG3CWUVQ8oaAl8F7hC6KgrY2el9NOpEORBGUuQV0GldLyNdPOuJ2Coet_mP3CqIZxWWGOruXLoHNYMKi6Ybgnco3bSFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
طائرة مقاتلة من طراز إف-35 إيه لايتنينغ 2 تابعة لسلاح الجو الأمريكي تطلق نداء طوارئ على الرقم 7700 فوق الإمارات العربية المتحدة.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/88298" target="_blank">📅 00:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88297">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e124a7b79c.mp4?token=AEvp27JDMrMJxl1STy-946yHblskrlmnds_i7RYNV2Q-gkTxmTWsC3fWQMxDkDR020y1hv_Njt_WBHjsvP20tfMHj_urlRyN_iLdLsxmefT-wj02y23TbNyMxogiMOlNT2i7MEZnO2-_Xy8zEKctlsOSIllK5ZH9xbo_6t2wDJrlIDBeQSTjRVI-lCO1AKp_oaAqwFmQKe1LjM5-0XDTebxGJj0eZuCZ3k4iR3IbrqEPax_epWF6UDLrQuTrK_mmtrhzfhFaHYKu1tUbCwiBSQJ16M8OxmULJ2KeX0euEwFTtRBbKNk4lvVjwxjWD1q8MiYqSoPjumlWnIaKOKbOCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e124a7b79c.mp4?token=AEvp27JDMrMJxl1STy-946yHblskrlmnds_i7RYNV2Q-gkTxmTWsC3fWQMxDkDR020y1hv_Njt_WBHjsvP20tfMHj_urlRyN_iLdLsxmefT-wj02y23TbNyMxogiMOlNT2i7MEZnO2-_Xy8zEKctlsOSIllK5ZH9xbo_6t2wDJrlIDBeQSTjRVI-lCO1AKp_oaAqwFmQKe1LjM5-0XDTebxGJj0eZuCZ3k4iR3IbrqEPax_epWF6UDLrQuTrK_mmtrhzfhFaHYKu1tUbCwiBSQJ16M8OxmULJ2KeX0euEwFTtRBbKNk4lvVjwxjWD1q8MiYqSoPjumlWnIaKOKbOCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:  إيران ترغب بشدة في إبرام صفقة لكنهم ليسوا مستعدين لإبرام الصفقة المناسبة.  لدينا سيطرة كاملة على تلك المنطقة بأكملها، وبالأخص فيما يتعلق بمضيق هرمز.  وهذا يعني سيطرتنا تمتد إلى عمق المنطقة، بما في ذلك المناطق البرية.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/88297" target="_blank">📅 00:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88296">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f648adb9.mp4?token=DmvVFLxdVqvfOFfy0DhAGmbGJz4ekGxRnyHpl5PAjh7867FxHnCZ3Ph2W6mUpfODfycbWaPNcK0GzKXrjz9IwQddZwsxCjMXf63VC-k_NCG-M212j8-qKL_OuTFDQu63ZjCX6f3hvxLZtIqKgTZMKySbYwYzGJIgIsp7G29DCCEz2q0PQ6-ZCUIT8lcxrh5ckNfcGG8ZsiYIicknCSTkG9jyMfjcGMu3Q2wzWtyjTiCYZ1fb2fqv1wOfZ4XCZOmOvgFVvd-M6w4TLndCprnKUFAMGnestOI_k3YxbmKCsJX7lyTsurQpSLbclE9700tM13ZBiZcKfCxyA_8WRwpB1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f648adb9.mp4?token=DmvVFLxdVqvfOFfy0DhAGmbGJz4ekGxRnyHpl5PAjh7867FxHnCZ3Ph2W6mUpfODfycbWaPNcK0GzKXrjz9IwQddZwsxCjMXf63VC-k_NCG-M212j8-qKL_OuTFDQu63ZjCX6f3hvxLZtIqKgTZMKySbYwYzGJIgIsp7G29DCCEz2q0PQ6-ZCUIT8lcxrh5ckNfcGG8ZsiYIicknCSTkG9jyMfjcGMu3Q2wzWtyjTiCYZ1fb2fqv1wOfZ4XCZOmOvgFVvd-M6w4TLndCprnKUFAMGnestOI_k3YxbmKCsJX7lyTsurQpSLbclE9700tM13ZBiZcKfCxyA_8WRwpB1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب:
إيران ترغب بشدة في إبرام صفقة لكنهم ليسوا مستعدين لإبرام الصفقة المناسبة.
لدينا سيطرة كاملة على تلك المنطقة بأكملها، وبالأخص فيما يتعلق بمضيق هرمز.
وهذا يعني سيطرتنا تمتد إلى عمق المنطقة، بما في ذلك المناطق البرية.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88296" target="_blank">📅 00:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88295">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cED6ayK3CmDD8uJq-Bb9c94cg0q_FCM0h06RVgSe91OhcIsIazy_slkVUt6SofuJmDUiPeF2P8pRsdqepC3Y96Rjgb1ApoTe4Vx_IeeXyIuQZAn0jIp4HWT9UyziWEusPSQ6wtogTESn4QHZMXNBPFg0ndaVAENx8-vQhyRjyG2L59NkroDhQWn16cVR0YD-oInDBQ0niz6nB9uGDGMKkuebvgY5Ejxs8ml2YiX8V7gELC-f_wkX77he9KYbft6oHFznSYc_2y3CbmA9PrPrUsLcF0dGksSKvWN6u_R3jkC8HvM_tQSs2oXnfe6RMTSsa0EatYEB8__fE8rcAM3PQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
نحن ممتنون لقرار المحكمة العليا الأمريكية.
المجمع العسكري/قاعة الاحتفالات الذي يتم بناؤه على الأراضي المقدسة للبيت الأبيض، وهو أمر بالغ الأهمية للأمن القومي، سيكون الأفضل على الإطلاق!
إنه شيء طالما رغب فيه الرؤساء على مدار 150 عامًا، وهو ما سعى إليه الجيش خلال المئة عام الماضية. قريبًا سيتحقق هذا المطلب!
الأعمال الإنشائية تتم ضمن الميزانية المحددة وبوتيرة أسرع من المخطط. شكرًا لكم على اهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/88295" target="_blank">📅 23:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88294">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvHaRZBhOqsVa88P_lh8YknocC2wNm5v9-tPsFheNz2WylBAD6T5q-LnpyT10BIPrWwkIQkjJwumM2-SmlS4DCq2c9nuRbqaNJ1behX7RzU5jwumJLnGGK0DVV1WZc58nikgWprJXvEd4zdder175a9tzD8Nd1tD5LJo2CJ9qWs7PrkqT1ue8GU9SIdCWCDZkrFDE4Jpz8Z739SZZKCU7C2TGABIByc_AhzjRDSUlC6wAl9xWiM6exdwQ6DfOaaVK9DCboWaLcX242XPacrOYxjNe4tL2zF1U8awsDQuTYnTIp7Y-Qjqez5hLpPQVLNVAEKaasBjNIqQ0jg3WYq4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
الطيران الحربي الإسرائيلي يشن غارات على مرتفعات علي الطاهر في جنوب لبنان.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88294" target="_blank">📅 23:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88293">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
الجنرال وحيدي:
لن يتوقف الأعداء أبداً عن إضمار الكراهية والتآمر ضد هذه الأمة العظيمة.
سيستمر تعزيز إنتاج منتجات الصناعات الدفاعية والعسكرية، بقيادة وزارة الدفاع وجهود القوات المسلحة، بذكاء وسرعة ودهاء أكبر مما كان عليه في الماضي.
هنأ القائد العام للحرس الثوري الإسلامي وزير الدفاع بالوكالة بمناسبة يوم الصناعات الدفاعية في البلاد، مؤكداً أن الحاجة إلى الاستمرار السريع في استراتيجية زيادة القوة الدفاعية والهجومية باعتبارها الحل الذكي والفعال الوحيد لعبور المراحل التاريخية الصعبة وتحييد مخططات العدو الحالية والمستقبلية أصبحت أكثر وضوحاً من أي وقت مضى.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88293" target="_blank">📅 22:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88292">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSMEmcWFVROSqcouSKZyLGvFRbdp9d3ExOg6fUWWE2c5u7hA_FHgwBNCzFZ-Ld3opJ1kg3ITDpV3wDlxdVmEoFI80mw2eKGp_boP4jGpxVD7bUpnS-pLOVABsC-YbYDfUe_e0-IQPhOEeaqVTX_QvApVA59ng7UHeahQbasbubhROZ_2L27CFOb-q-KKGio4LgAvoxC4eaLElnG0HqlvHX8tjG4jrqDcMKrR0QTD8gmuhfYTttq3XkWBA7-5WOP3KF_8dD5NLkGwHu4gh8Txkgwa3brzfBl9mdij2reJ6Ct7QHvIrVDHqJb4lxcaL5LcZnDGZJZZbanB1Oo4BFDwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تفرض بدر نفسها مجددا في العراق كعرابة لمحور المقاومة على مستوى المنطقة
العامري يلتقي حركة حماس في بغداد تحديدا القيادي أسامة حمدان .</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88292" target="_blank">📅 22:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88291">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1nutQaYI3GatG6G1swa7PqbX46JJZoHAvcRMH9YYmZ6KNxOTIm2FqCH-uWUITRi9hVk84OB69rPSmwwLbncR6dSN1Ml3X68euVEfBVsDTHD_PTdSAg2so9pALesvKKIM8ibAfQQlCIpN3e4OTrvYz3PzmnCTD3YYr0psbdG79zy-MWdEG14dAxB1HXTu_n5dLRhXkwIyNr139JYf0M0kuC-eUVuEScHwDgSITW-yGlO1jeTvEH8SveJ_xNYsbqCpDjUgJjC-hYl9enRk8xAhZnvTgvWabc36X3EGt645jiRMsGru1Lfzua8cI1v5PXiQAMlw7NGjujtgupw_f9ksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار خام برنت ترتفع إلى 94.39 دولاراً للبرميل</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88291" target="_blank">📅 22:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88290">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXYim0fvPJxP6qZw16kYrw4CUe5miTiXZJqHqVHiaMl9svaYtALBN3cYHsNplsywYaeC2mokC0Nn1s00HSWaCcE0D3w3k7TnMe00zGLsDMb2zYJ3L1BxIZfrTVWss_yJndeneEVuEgA2w8gyVyIAcu6Eebh19OynRBKLFISfS3rfo9IwxOuaRWkkeFnSwtCfo_3-9YvMpD-ab9k7YVUsw3NO-16wpVQ1MtftWHUhQC66Jfevnlpvl0biaywsdENpFYIH3ircPXZRhjckDpcPN8hULtqKnzyx3QYKq1r5lDba9XHfwSjIicnH-giixIedc6faDz-q0abJVpXUmRTOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السلاح عزة وكرامة ..</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/88290" target="_blank">📅 21:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88289">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
يودّ فرع توزيع كهرباء شمال البصرة إعلام مواطنينا الكرام في مناطق المعامل، جنوب قضاء الزبير وغرب البصرة، أن سبب انطفاء محطة المعامل يعود إلى خروج خط 33 ك.ف عن الخدمة نتيجة عارض فني.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/88289" target="_blank">📅 21:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88288">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
طيران مسير يجوب سماء محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88288" target="_blank">📅 20:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88287">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس مجلس النواب العراقي:
رئيس الشورى الإيراني ابلغنا بأنه سيبحث استثناء العراق من مضيق هرمز مع القيادات الإيرانية.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/88287" target="_blank">📅 20:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88286">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
نفت وزارة النفط العراقية ما تردد من اخبار في وكالات الأنباء الأجنبية والمحلية ، عن تصدير شحنات نفطية عبر السكك الحديد لايران ثم لتركيا.
واكدت الوزارة ان عمليات التصدير للنفط العراقية تتم وفق السياقات التي تعتمدها الوزارة وشركة تسويق النفط "سومو" ، ومن منافذ يتم الإعلان عنها مسبقاً .</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88286" target="_blank">📅 19:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88285">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-gtgPXiKBNu1-yZfbBadLVyNC1d9uAyFgj3fUfryO2SzrsnmdsSr0YbKh2gITOrK-qxuA-IVWMd91FHY15OZd51imtUGEdPZ5YK9Rz1ebduLLN4VD1UoMrzYOeryLrae-oOyzxjEgQr0ln0xbTuldTR38lmIfXxMzc7nQaDBpBW54FrEVWPXfq1Rw3DP0L1li5VUVqInOEIW0k5eQTlwYFWWmwthhssbKlQpdS1UoQ3LiWcQQwTjuvHij02rJdKGA-yAHEpvOOYtPIQe0Ln1nlNDuOLT8or-_E2osdFgPORR1rvS_qGenNS86bCm7k0HGh6E9riLHcXgpnMc-AqtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇷
عراقجي:
قبل 14 عامًا: "أكثر العقوبات قسوة في التاريخ". فشلت.
‏قبل 8 سنوات: "أقصى ضغط". فشل.
‏قبل 5 أشهر: "استسلام غير مشروط". فشل.
‏اليوم: "أكثر عملية اقتصادية كارثية على الإطلاق". محكوم عليها بالفشل.
‏لقد شاهدنا هذا الفيلم من قبل. نفس المشكلة. لكن المتنمرين مختلفون.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88285" target="_blank">📅 18:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88284">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇶
تنويه:
تفجير مسيطر عليه في منطقة البو حداري قرب جسر الإمام علي (عليه السلام) في قضاء الكوفة في محافظة النجف الاشرف وذلك في تمام الساعة السادسة مساءً.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88284" target="_blank">📅 18:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88280">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q248TijraWH9VNwtfVjv_D18FnPRiWFy_KUFHeA3Ga1PiSnkWH9XFTLpVD8gI7KzC9qs2i10io6AsRG9TRLYTxGDTkhxAgVH1gHZ9Ln28UNBoWv-LVi-6Kh6JYz9nIyj-69bhxF3dc_26lssEKQzFiE86ez2gQ_z6_pZFcXFBPJjiG5k9WtubsEOzzeUFX5CiOEFgpQjqpM2Q1wlhHh9yavyOFqRp6og9OvbsXUm2thlgZFQoNb_wffv0Mfa37cbRmkbpZxE6kwOktL7g1sqf5STXNuIKh2ZkgeyGxtklGijbiNjwqyIujCs4xBLUXDNSx7S13R8rXeTVj4B2XJi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p72WbN0dwZLjCQQbvr53GM022VKHkNkiK0jvu7fmNw9yrXg-tOna1Db8m2AKLhXr8KHaBks9fWCY_kKNY1v2IPuIp8a5Uv9Rkg02c1IUtrbI0lBz8CiJ2N_SrZ0NaPUHNPWOhmjqwesPsXK6CK_3L5tG5efKsW9A2LtBQB69DnzIZLPzB1enayh_ay2DM0xc0dJFJg7WdR3C69gnXuaubLN_8qkKdjBvg4lcyWOAF2aERK6mbZVAC0PkjzRksPphGaEK1spYM61hA151qYh8rkvcgOfqXXa4B1Q0GoXuegynf2DAR5XKJocPpu65IgjiacIYYf0OouOCsLhQtGt7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOx_1BHnBL_IGdb7c8G6ym5qEDN2adj0AenfOAF1RSj-eJCH-qejPdd1tYjXtMF6ZxZpquSogo3eRL64Van20lCntpGxokH_7RO9Un_R9Tn0wBavgrdf32YT1y2TgBdVFvDvNaSKkl6lv7_L9NL2Saqmq6rlSMuh1wZS5ld2fiQxASZrYNiCiZaqAmOSrMsstJjPaKsfog_XQd5jRRucb7Jv-l6xejiE_iX-bK4wcuEOXqRwVbYkdSpHP1BQ78dvuhTf7oLY0D2gxbrlFGZu7XGG_5DBLLW9z4eVXf_NHhIHPVXp0JKRSA8rKoyG7ls1_3wF8TxIswHVOIQ1nd8BGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEeFNRX7p0bOSgOgQUcehkE8srtZvoTAp6MFjwmu0QFogIWTtJk8-OctGOIo2Wq3jDtHFq8uuf1eL8Wm4BEtKX28CZ6Cn9nX1wjGtvoqyN66re0DXDXcp84Qd9GAgk4sDRIXj4iwxxZHfxfFUv1PE-JNU6kMEFQyU77xiwbqFvRdiH3ofUNr7D6PsDnAkm5o2V1oq1TtIf7TyiEaSBJyEWdBZPHyXzQdWIiKzEInJVvqg3xjkyd6pObDirWpgvazT_mfbWlHoQOTrDIs6b2YZI4bAcwobgm4MGubS9oQflhPZTfvIWfirdFcxYzzEnlePDz2I0uRcCj_LkGEOZrigA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من الحريق في قسم الخدج وسط حالة من الذعر بين الكادر الطبي وأهالي الأطفال</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88280" target="_blank">📅 17:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88279">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انقطاع الكهرباء ‏عن ضاحية عبدالله السالم في الكويت بالكامل لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88279" target="_blank">📅 17:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88278">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اندلاع حريق في قسم الخدج في مستشفى النعمان ضمن العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88278" target="_blank">📅 17:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88277">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اندلاع حريق في قسم الخدج في مستشفى النعمان ضمن العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88277" target="_blank">📅 17:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88276">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku8Mhz7LEPYb_ydx-_6S0CBcqY2OJyNNkNB3oIsL-Eh1MSJjJFHT3DFpMh6HpHtkEa-8fUZ-wmckLC_gW42GQptZYbBb65hkTbQ1yW60YKfyCrB38uFQgEb2WgHVXokHKYxSdPZMv3IrptMv2hVJMwXi7sBrxAxo1Dqw5WEa-BTSvK66aX77e8QxoZgfaJNwOrFX8qI14Kq6DsQULXNI0MAWIfRyTDDOWguRPhG8AtzuMMMcmMJbc_JkWW_ohn8uk0R3LNRPv8RWG2veJBGoEaBXfCCEJ8EH_NXBWbZ8NXwjsDesHyf1_pV-3VyJ7BBMIwLk_VBcqzS9wdFUTbLu1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاقمار الصناعية:
لا تزال حوالي 3-4 طائرات تزويد بالوقود جواً تابعة لسلاح الجو الأمريكي مرئية في قاعدة العديد الجوية في قطر في صور الأقمار الصناعية التي تم التقاطها اليوم. كما عادت خمس طائرات نقل جوي من طراز C-17 غلوب ماستر تابعة للقوات الجوية الأميرية القطرية إلى القاعدة لأول مرة منذ 12 يوليو.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88276" target="_blank">📅 17:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88275">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية: مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88275" target="_blank">📅 17:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88274">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c39f9d48.mp4?token=cHlAdqG1AsFxG6xKfeX3301A-goFgqdRw-gZ_Fv4FZZQITapcyGfH-PmyDG0-RK88jUfg-e5kRiWJHwSmp-M8dr6EENXoQ5kNVwCJfaM4I3dA-H4PKrUWD5CllEvv4JBcisWQJYMng8WegFH3dq-5c6eaDF_zG3P8-Odon_cDaKJiqVyuj7oWQEe_54LteFI9UD1hXa_-g_4IOYN4n4zrTC_woMI1cChsCnPwjuZR8t7i3yRSmP8izGfDR6It1XVq5I3JCWEIJxeFY32wTIZvlrO0z3zvWu3lzFa-VAkEFs-RKtOyIyhzz-JtrTYQQFEADDWaxnksyaADL9crL8wXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c39f9d48.mp4?token=cHlAdqG1AsFxG6xKfeX3301A-goFgqdRw-gZ_Fv4FZZQITapcyGfH-PmyDG0-RK88jUfg-e5kRiWJHwSmp-M8dr6EENXoQ5kNVwCJfaM4I3dA-H4PKrUWD5CllEvv4JBcisWQJYMng8WegFH3dq-5c6eaDF_zG3P8-Odon_cDaKJiqVyuj7oWQEe_54LteFI9UD1hXa_-g_4IOYN4n4zrTC_woMI1cChsCnPwjuZR8t7i3yRSmP8izGfDR6It1XVq5I3JCWEIJxeFY32wTIZvlrO0z3zvWu3lzFa-VAkEFs-RKtOyIyhzz-JtrTYQQFEADDWaxnksyaADL9crL8wXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تزحفلي تزحفلي وفاتح ايدك</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88274" target="_blank">📅 16:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88273">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e99c8dd0e3.mp4?token=S-o4o7q-gU34M-h_pA1pdbiunoud7WEIDntusKexhowB9fQN71HCh_S_FHRF412dCp77D1doiw1mZ8XNqXHOOv9iTBKKPDJnJIY_4OJiSL_bvunLUlg9ofrTsU_NP3CzEWHp5DH6vbn0dVGeH7wMtLLBFEObx27Za4alYDzP7K6BMhwvqnAm6bYAsDZS9RT49nVOxDRlFgs-q7F2yBWHwlugmYj1NmT1YcZcgYG8UMNn1dpFj1f4VkyMKUWqhMubdaKJK1H36ucIqTFsIboClBxPbudsETencKqWpyILA-ODNq6vwDO1JX4OenSoAxjIy5sCrdCwP7mXGlEHkmC3Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e99c8dd0e3.mp4?token=S-o4o7q-gU34M-h_pA1pdbiunoud7WEIDntusKexhowB9fQN71HCh_S_FHRF412dCp77D1doiw1mZ8XNqXHOOv9iTBKKPDJnJIY_4OJiSL_bvunLUlg9ofrTsU_NP3CzEWHp5DH6vbn0dVGeH7wMtLLBFEObx27Za4alYDzP7K6BMhwvqnAm6bYAsDZS9RT49nVOxDRlFgs-q7F2yBWHwlugmYj1NmT1YcZcgYG8UMNn1dpFj1f4VkyMKUWqhMubdaKJK1H36ucIqTFsIboClBxPbudsETencKqWpyILA-ODNq6vwDO1JX4OenSoAxjIy5sCrdCwP7mXGlEHkmC3Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية: مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88273" target="_blank">📅 16:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88272">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88272" target="_blank">📅 16:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88262">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmpmMHk_8Nm9cUvrFIraUilYOh1Oq3GA_LDN9lHNA4fhl6Dm7MItgvPUDsRGeDybqIPP8wcNVOTBGsRvdt38Eqk5_W7xc8kDM9URCMERYi-jrZ7ZfGNThvLmR0U7vSwu4SBxx72pbu-13SpkMhKwYjQ1KixD41Hhe3f1o8k14X7jjpdHDiyLRl-yBVeIUfsxDtcVRBmXssq546mYsBSFguRaenPeXqroOYXKSn6Lu5A0TaVC2rh20ptQP05pf1rKDSkckR81Pt-ZurnkrnkWOq91G5yt6HF90L3Y-udSiiQN9KONJwtYUhlnQiOqbooFf13L-uJ_C69LTxVu_lO5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkrOtzVN1x6Owax_PJ56b8qTlxjoNtLgOF02wVUNfGvMVc-N5jFch-CMqA3xSrTrv2a_z6Q1vkfBfRI1_MKMDKKcz1F_W4_DPBa6eMyZ9Lvu6j4i9OwpAYvk4Tl7Y3dNhfQQ132qddd3ZPicTxo8udiFUwFaXmqTFqgpPEqOKQZs9yWn9vQeLEUlW_IwKG1PZBcUoVKx0eaRubydvrGlwJBrLZmoYYjqR7pEXD71TcYmzF3fTQWx7vfb5renhBvzC57KQQqUfGwnyoPNg3CjONBpQNFJdmLqn3YdzcKUmBoZu12NqM0XUiyH1iduQWAd9OPkLu9bU8UgJYv9kX4D7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOJnXD6YxuTemRIEpAlRZWhQ9rp3aQL-l_jV8JuVRDKtXdyzCUpk-iuLCgdtIZ846UNo4GVmsglcIK3kLM0v8OJFL8af0o3Jy9vCDGiuUM9YHtrCa_iADyxlK655wq5gAIQWkeiKyQtIdnfOCgYPphk-K-KWFmZOLknU7f2agig4PPtEwdAJXzse6UweaRMDnDRRvSs0TFyN28xf_F6P3MG2QJoitmCX5k0H4SVCDZKl7NWpZcvlUkBFrFMLGTD7rvNKEYRlQ9ZWkJlNfTPc_NB3xM3b5efi-lhW6U8_ze0F6U8ERn4i4Hsd8KDifScE0AzmBO24K7hu5U2BCNpzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Alw5CMfPjUsZ1bZZrmytU-1s_oSCYW2rkiJIE3N8x-6WfIs_FNuXPpJJEM5GjS00s_Y26UFSBZANY13O0-JhCSJDCJ4XXysvVcQNxK5v2vO4nsd_VCh_cjfxwD4FoEmN0wDb9UR_MqzHCgmqmBo416BL8_C6hHWRVMtBMm5E0XG-awFL2-rbZnqk3bDYFFS8ltcaaPLEhsRRcb5uTYMzC6l_zPanhojKQpb-NIuNU6Akl6-UluprBQ8TRYxavRUg_NglSN1629fo26uFnlD69wkfgK-jeC3FGrkoQg5OMbcuITN1E3iFN-roi1YNJT5aPRBMidHGtUeVgpDxUgUgKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7faRPcAg3zOjheyO-XyuQcYGwKluNyyKWe9dhloanZZlzfFYcGMkQ4wp_IQL7BFG29KMiEjW5UDcj9asmgjmZUJhtldBfTZQ5lXnmsNO70pRttUlzX3LljzT81BUd7tNPxn00LrjpX3XaIlNhNJhRb5LI8vHu8hq3HeINcJ8NBEeeEE_IYuiKNbh-eymFdYmqdOPmcWE5zoIil2bW43f9ID5NQOE2YrzImDdiistmpyoiSXF3dSZ6X_NAunMbI5pS_CGhTiO8-DDEbIAhnT-ycukNuuUghaC4sRvFAGRg4aKjOvlvzez_BZiEddQK--fTORRjoaTpycapDJtDafHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aaRvjdzMxl8ijXXsvgMjiAeKvadd4Tg7IdZKODb7WPVCuzKvScTVCJotTB0U6U-WdZQ8spo8tQuD4JBAjCcE6m1boMNBlsJDoS6WlD37RBy6nf4lhQGPe753ILuqa3g324tfGMDXLOd7Wqf_poew5PfDdJFQfiWC7jDCDdr_p6Yh4bugUmqbc-aWki3k9QtzRn7DN9wTWHoSd-aJR2lyXzVHCNZU1A39iF0GRVaQr9-E1cpRl7MqOVaXq9FDjdI5jmz8mZB752-zUDAM91P9YZDluyOC6D8ZfduDtWYMuvIz1ltiY0PY0l7OKVnS1IzL04zul7HC_EqHYNT-pAV8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8BlfNFdrQ2oQf0ZwfX_M2ktS5Oqu33gak7zhfoqUvKndW2rsvahZ32esMCeOnLrFdls_dGrjXMDerpjIZfvwOrDozOpVQf873JNBo9o-mRapmGbb5_SgPDdsiwe55ealSq8lUEarBhbUfsYVH7ydIfLIpOI7CA5jbGtNvkrUc2i3LIN_A6-FHp-yoG1c6Nwnc3Ezwfxerxy9Pm2d2ot35UDsZwg6VxPfRLBX76_OnvmyQNG9AT6T7bCYOftHOcX4pkk91HFfehBLgUwvevv8BpWmw-Pi_JPBQmV11jbcxQna7wTbCzArJcq2FWcx_Xn2AvZ1k8qHlMgYqE5Ee04zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibDda-nb6fRhWrLvcAM4UDq6B35lnZv9PPMtj06ecX93-_yNIher7Pl7hWGDpBYRB5TKE9_tryeOAMw-oPg0CX_CdijFLj7apMqM5kcDH2sjOrpI_XSXQjs4H7411cJwQzMkabcIlnhc7x7ak_o5EI_MemyzXT_fy3GyvjvCq2EhAEG3_xGF1Tp_AsrhXMol-fDnZ5rwenuld8uymjcsa6hYrDR8ppZ5jNsY6mCSFJIOS6gnnet0TYEN8FynK0DB0kzjEaSmpAEZniHMJsFQ-smbTevLtkI2h-QzTV4AUw0_wiVWYLikJj_MxRImZnlInLEzRa31Nd8xMRXjSzZrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNKZUJ9qhv89q2RlOynyelB9nGHOARU4qDn0JD6nQxl7XOyqYFThMIssVUO-Jbh990F2DRQseYP8i5X87aK6oS_nYvvUXB7vDfLGYMs8kLWmWoIrMc9vtUJXaLiEyV5nbi9tO8lBmsZ1JndZncdmkUysPqLJG04EUxvKpkfrqXBjSa7wHLQmCnqnVVegaSQOZReYhpj51St6oUMfZhqaNdi3ij2CulURpkku6TX7nfsIZi8cGza7h0oX0w1aUPhAqJqv4jhoWN7Ct5Rshy_9Ue8_8PBFJPnW7SYnIm7SFtNF1E-PkNSFR11tbPREQ8In1YUfZz7LQ3M7zsVOcbeVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3ANfmWxrgb6eTp-T_6dQmvF7UDEQhoEDBW4r791_KDaTlb05C4i9wcmvpvUbH9j4ATKFbkN7BE263IygZvrkGdUO5bmPH3S3Qru9UVygeZ_WfMMfiouI3KNIilEY01pm7Iz1m03xEugbXI19SjCf3SN7c8-mChfwKhN-Eg0RAR5ZaC53ZBU2CheP66bDljNNMlPRU_uuilgL0GH6pSXBkvQOMRGXMWQWYtCOUstXtKCoMaHtHEpshAj_qJaEX_BIBmeym3bz9OlQqpp-Rkmj5ibtmsNfexf_zbqMS_mbKbZEYCmHhHopn6l-RjTs1aThzhdyvCAUehKN-2k9VF8Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات المسلحة اليمنية:
صور من استهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88262" target="_blank">📅 16:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88261">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4QepPN15NByebk7DbRqejQAbtmJp40UKuik4J8nFQHgdzkt3f_p-sbAIiKshuNDQDQbhMtfYzFA24GqAvwsORWcKiOBXxbC7oqbaLjKRbnpqFKsLg-7HVS-z32Q7zEmjzteC94Xi1ygpQ1lC_pSxUp46lSnjdbFFBwydhS4UWdw1f3jmSHENW0jp9W86pURzKaNVWgMiQNZTvFqiYapbWJRtvhTLLp3wleFjdhdbDTNlXOA26URwhVrG2goVV_6XyOuDvkKSbdp0R3dL3gux38KgfggzCj0Mi13qWNJus7nqiLml9YOeFBMlBs8zwOYVBNpNgaHzxYubQDVWNkWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اندلاع حريق هائل في مستودع بالمملكة العربية السعودية قرب الرياض منذ أيام، ويبدو أنه يتسع نطاقه باستمرار، حيث تجاوزت قوته 200 ميغاواط. ويحرق الحريق بشكل رئيسي الأخشاب ومواد أخرى.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88261" target="_blank">📅 16:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88260">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98553c859a.mp4?token=imSH1TqtC5IM41fAhiIO4IHCe_CvPGpXEOJVEapLg0AEt6x8S0krOb2VDJXxPngYcj482bU5kZsrjD3kkPa4qB6ORUD0t3W1vH0qvMhIcjtFSw-HK6bjwu8EunGTmOsgrAOIxMX4J1sjLiPU4HbP33aFR3zW_tiq6vfkdX8WcL2SjlDVcWELMtZAYadGkX5CJCKo3Ib5zMANzB_BNOE_bCjdcV4NYosfpqjkJMMPOGuqKBaZUG26BkZfasgISbJRuJPNsuirAf8z4_bGjHRPG1xdcvQ2oF28Z4Sn8Rs0yakNUwf38Nr0_ZdtpFh6EWprYWl65KZUYlbWMvVebvpxvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98553c859a.mp4?token=imSH1TqtC5IM41fAhiIO4IHCe_CvPGpXEOJVEapLg0AEt6x8S0krOb2VDJXxPngYcj482bU5kZsrjD3kkPa4qB6ORUD0t3W1vH0qvMhIcjtFSw-HK6bjwu8EunGTmOsgrAOIxMX4J1sjLiPU4HbP33aFR3zW_tiq6vfkdX8WcL2SjlDVcWELMtZAYadGkX5CJCKo3Ib5zMANzB_BNOE_bCjdcV4NYosfpqjkJMMPOGuqKBaZUG26BkZfasgISbJRuJPNsuirAf8z4_bGjHRPG1xdcvQ2oF28Z4Sn8Rs0yakNUwf38Nr0_ZdtpFh6EWprYWl65KZUYlbWMvVebvpxvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر أضرار جديدة في مصفاة جازان النفطية جنوب السعودية، وذلك عقب غارة جوية شنّها انصار الله بطائرة مسيّرة في أغسطس/آب. وتؤكد صور الأقمار الصناعية الجديدة أن خزاناً نفطياً ضخماً يقع عند خط عرض قد استُهدف، ما أدى إلى اشتعال النيران فيه.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88260" target="_blank">📅 16:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88259">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا
تعرض موكب ابن السيد خضير المطروحي، قائد عملــيات نينوى في هيئة الحــشــد الشـــعبــي، إلى حـادث سير على طريق بغداد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88259" target="_blank">📅 15:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88258">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">في اول رد تركي على القصف قرب الحدود التركية.. ‏تركيا تصدر مذكرة توقيف دولية ضد نتنياهو بشأن أسطول غزة.
رد مزلزل</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88258" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88257">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
بيان صادر عن حزب الله
:
خرجت علينا الإدارة الأميركية يوم أمس، عبر وزارة الخزانة ووزارة الخارجية الأميركية، بادعاء أن حزب الله خاضع لسيطرة فيلق القدس، لتبرر من خلاله سبب إعادة إدراجه على لائحة العقوبات، في قرار ليس في حقيقته سوى حلقة ضمن سياسات الإدارات الأميركية المستمرة لاستهداف المقاومة ومجتمعها وبيئتها ومناصريها ومحاصرتهم والضغط عليهم سياسيًا وماليًا وأمنيًا، بهدف حماية أمن العدو الإسرائيلي وترسيخ احتلاله لجنوب لبنان وفتح الطريق أمامه لتنفيذ مشاريعه وأطماعه التوسعية في المنطقة.
إن هذا القرار القديم الجديد الصادر عن الخزانة الأميركية، يؤكد أن الإدارة الأميركية التي اعتادت استخدام العقوبات وسيلة لفرض سطوتها وإرادتها  على الدول والشعوب، ما زالت تتعامل مع لبنان من موقع الوصاية، وهي بدل أن تذهب إلى إلزام العدو الإسرائيلي بالانسحاب من جنوب لبنان ووقف اعتداءاته وتفجيره للمنازل وجرفه للحقول وقتل اللبنانيين، تذهب إلى حصار اللبنانيين وتعمل على تجريد لبنان من كل مرتكزات القوة، وهي بذلك تسعى إلى إحداث اضطرابات داخل لبنان وتحويل مسار المواجهة مع العدو الإسرائيلي إلى اتجاه آخر.
إن حزب الله لا ينتظر شهادةً على لبنانيته ووطنيته من أحد، فتضحيات آلاف الشهداء الذين قدموا أرواحهم من أجل لبنان وشعبه، والتاريخ الطويل من المقاومة ومواجهة الاحتلال والدفاع عن الأرض والسيادة، هي الشهادة الحقيقية على لبنانيته. وإن علاقتنا الوثيقة والأخوية بالجمهورية الإسلامية الإيرانية هي علاقة نعتز ونفتخر بها، لأنها وقفت مع لبنان ودعمته وآزرته لتحرير أرضه واستعادت سيادته وحقوقه، وبقيت إلى جانبه في كل المحطات والأزمات، وكانت من أولى الدول التي ساهمت في إعادة إعمار ما دمره العدوان الصهيوني إبان حرب تموز ٢٠٠٦.
إن الإدارة الأميركية لا تملك أي أهلية أخلاقية أو قانونية لتصنيف الآخرين ولتوزيع شهادات الوطنية عليهم، فسجلها الدموي الاجرامي من فيتنام إلى أفغانسان والعراق، ودعمها اللامتناهي للإبادة الجماعية في غزة، وتغطية جرائم العدو الإسرائيلي وما يرتكبه من قتل وتدمير في لبنان واليمن وسوريا، وعدوانها على الجمهورية الإسلامية الإيرانية، ودوسها كل القوانين والمواثيق الدولية، وضربها بعرض الحائط كل القيم الإنسانية والأخلاقية، وتحويلها العالم إلى شريعة غابة ينهش فيها القوي الضعيف، يجعلها في موقع أم الإرهاب في العالم، وينزع عنها أي حق في أن تنصب نفسها حكمًا على العالم وشعوبه.
إن كل تلك العقوبات والتصنيفات الظالمة لن تثنينا عن التمسك بخيار المقاومة وبحق لبنان واللبنانيين في الدفاع عن أرضهم وسيادتهم وثرواتهم، ولن تغيّر من حقيقة أن المقاومة كانت وما زالت وستبقى جزءًا أصيلًا من تاريخ لبنان وحاضره ومستقبله.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88257" target="_blank">📅 15:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88256">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇾🇪
🇾🇪
الإعلام الحربي اليمني:
ترقبوا الساعة الرابعة عصرا مشاهد نوعية لاستهداف القوات المسلحة تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيّرة.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88256" target="_blank">📅 14:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88255">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">استهداف منزل ضابط في وزارة الداخلية العراقية رفيع المستوى في منطقه الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88255" target="_blank">📅 14:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88253">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:  إغلاق مضيق هرمز يمثل تحدياً كبيراً.  العراق يمر بفترة عصيبة ولدينا أكثر من حل للمشكلات الاقتصادية.  جميع القوى السياسية متفقة تماما على المضي في حصر السلاح بيد الدولة وجار العمل على آليات تسليم السلاح وإنهاء هذه الحالة تماماً.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/88253" target="_blank">📅 11:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88252">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:
إغلاق مضيق هرمز يمثل تحدياً كبيراً.
العراق يمر بفترة عصيبة ولدينا أكثر من حل للمشكلات الاقتصادية.
جميع القوى السياسية متفقة تماما على المضي في حصر السلاح بيد الدولة وجار العمل على آليات تسليم السلاح وإنهاء هذه الحالة تماماً.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/88252" target="_blank">📅 11:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88251">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
مؤسسة "سي آي إس":
أن الولايات المتحدة قد استهلكت حوالي نصف مخزونها من أنظمة الدفاع الصاروخي قبل الحرب، وأنها تمتلك الآن ما يقرب من 800 نظام "باتريوت"، بينما تنتج روسيا وحدها أكثر من 100 صاروخ باليستي في الشهر.
يتزايد تساؤل الحلفاء في أوروبا وآسيا والخليج عما إذا كانت واشنطن تمتلك القدرة والإرادة السياسية للدفاع عنهم في وقت واحد، وخاصة تايوان وحلف شمال الأطلسي.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88251" target="_blank">📅 10:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88250">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
قائد هيئة الأركان العامة للقوات المسلحة الإيرانية "اللواء عبداللهي":
القوات المسلحة في الجمهورية الإسلامية الإيرانية، بفضل استعدادها الشامل والحديث في جميع المجالات البرية والبحرية والجوية والدفاع الجوي والفضاء والسيبرانية، ستواجه أي أخطاء حسابية وتهديدات تقليدية وجديدة من الأعداء بردود ثورية ومؤلمة ومدمرة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88250" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88249">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23d5a7c74.mp4?token=iorV02Yql-mQECfdVZe1fNWWpU6qubmprrwtVHOGwhJSefZhGdrRIgZDy7SZNeM-bFsioRJ9H9W7OMvy_bCHnBgMXhiJUIbzYXqJY_wr-XcDeQWENeNybes1VIqqEF3J2VwtrOydr1ZR_MXXFd0n3wRSVmLzQDS4IYr5XIr-6ISl56QUXnvYGyw-R4x3RSEg2u21xAJw_cfDEvdfBhAU72SvEN76ng1H8Wt6IhJmOK3pGJVMfmzjCjcHZ-J4_hM5KlmjJJYJqHVOI86qzjn7DB_2kkgQ-f5L0IRgTEMiYoNwceX39swZ-ESdQQ0798Hl2xDKEt0MhV_mvzriaVhOnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23d5a7c74.mp4?token=iorV02Yql-mQECfdVZe1fNWWpU6qubmprrwtVHOGwhJSefZhGdrRIgZDy7SZNeM-bFsioRJ9H9W7OMvy_bCHnBgMXhiJUIbzYXqJY_wr-XcDeQWENeNybes1VIqqEF3J2VwtrOydr1ZR_MXXFd0n3wRSVmLzQDS4IYr5XIr-6ISl56QUXnvYGyw-R4x3RSEg2u21xAJw_cfDEvdfBhAU72SvEN76ng1H8Wt6IhJmOK3pGJVMfmzjCjcHZ-J4_hM5KlmjJJYJqHVOI86qzjn7DB_2kkgQ-f5L0IRgTEMiYoNwceX39swZ-ESdQQ0798Hl2xDKEt0MhV_mvzriaVhOnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس البرلمان الإيراني خلال زيارته لمرقد الشهيد القائد أبومهدي المهندس، يكرّم عوائل الشهداء الذين ارتقوا نتيجة العدوان السعودي الأميركي الغاشم على مقرات الحشدالشعبي.  #أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88249" target="_blank">📅 10:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88248">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
🇮🇷
حضور رئيس البرلمان الإيراني محمد باقر قالیباف عند مرقد الشهيد أبو مهدي المهندس في النجف الأشرف.  #أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88248" target="_blank">📅 10:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88247">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
🇮🇷
حضور رئيس البرلمان الإيراني محمد باقر قالیباف عند مرقد الشهيد أبو مهدي المهندس في النجف الأشرف.
#أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88247" target="_blank">📅 10:07 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
