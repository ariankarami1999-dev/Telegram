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
<img src="https://cdn4.telesco.pe/file/e4vPygAOdTjKYyftUK_K6uPF2CmpkFR5G4vmhXONTy_d72ed_o4CG21Y4O1tTb3maaQbZUvXkALLM330NgGJ03ErIVQ1XnxQKXaP5-QV_sgBmGFhG1lnFIqRaomVtrwR3I03-YYhxmvdhbXYxkokwtLjwZ1JDVEnWdD-gVmFpu5jgo4mQxLqGVFYCN3vDzSK__sg-KeWx5F5FCwsVKkW-E-EKLPiC464jEAh_61uIrOp6Rhj0sgzegaClo9D9RJQl5bFmpNIj_AmM82M6tunRHrnrRQzrlR_LN7538GVbSCJm6z3_PyaiCrrILOT6ALLIHl5qEnTFRHE0G-axQxy_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 18:56:49</div>
<hr>

<div class="tg-post" id="msg-82307">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
‏ترامب:  «طلبت منا الجمهورية الإسلامية الإيرانية مواصلة "المحادثات". وقد وافقنا على ذلك، لكن الولايات المتحدة أوضحت لهم، بعبارات لا لبس فيها، أن وقف إطلاق النار قد انتهى! شكرًا لاهتمامكم بهذا الأمر. الرئيس دونالد جيه. ترامب».</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/naya_foriraq/82307" target="_blank">📅 18:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82306">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHP6ZgPDz00u2nNfh-_KGXUnmSqAd5T0gb2YxjNd_GDlb_oAhmByTZS0Hfo9jGqvNOD2ofZ-GKZAFTfyTg3kWmIprt9xYyANJEGV6bOfPonGtkpFMhOV2ptfJBJ5eJCCAPuswYfKpfxcLKndqZMj3p5SLBvOSAOaquxBdfccHhoCXoAxC6r219S8dwURnxyb-GosXFop4DvRdb4I9sYggLNfjfYrLexYz2tv7_ggVldlPs8_qD9bXSndDjnPcuDxzQUUdbVxaPp3XpBwukNYmM6Yzim4Di8OiSpN_DFWQuuI0sDDH8F_233FifI8XD1Jr7-zV2lgoUB5SxIYpg9drQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب
:
«طلبت منا الجمهورية الإسلامية الإيرانية مواصلة "المحادثات". وقد وافقنا على ذلك، لكن الولايات المتحدة أوضحت لهم، بعبارات لا لبس فيها، أن وقف إطلاق النار قد انتهى! شكرًا لاهتمامكم بهذا الأمر. الرئيس دونالد جيه. ترامب».</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/82306" target="_blank">📅 18:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82305">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
‏جلسة لمجلس الأمن بشأن النووي الإيراني</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/82305" target="_blank">📅 17:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82304">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
‏جلسة لمجلس الأمن بشأن النووي الإيراني</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/82304" target="_blank">📅 17:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82303">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b551c66b.mp4?token=XLoIW2QT7Q4Z-0JbH1FOmBzm3-YH8SuuUEXVkaXuckIfCS0M-5zQu_YKw48haClmPsaMVbOjuK9zOte5V9mnFgliywJeTKTQXhVokHXg_NiMLK2Jyt3if1ou6y3tSZI1SIRzbNOUpqtdyO2TRWxh26tP2eoxXOipwXoY89ePF9F-SMrLdGToDThyWJppKeHCsHxWW58qKNPgkyb4VKrIs1prvOpTAoqYD8Z4zwuE_JEgOHAeRc_N9tpVBIPBAcpdWCoCaQSVisNG3osw_IodCU1lIXG_MEQsl2hqdmxZhJjE6d_hqUL185-sB9RA6rSPDjuMsUcErgQIq5v5uaJgBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b551c66b.mp4?token=XLoIW2QT7Q4Z-0JbH1FOmBzm3-YH8SuuUEXVkaXuckIfCS0M-5zQu_YKw48haClmPsaMVbOjuK9zOte5V9mnFgliywJeTKTQXhVokHXg_NiMLK2Jyt3if1ou6y3tSZI1SIRzbNOUpqtdyO2TRWxh26tP2eoxXOipwXoY89ePF9F-SMrLdGToDThyWJppKeHCsHxWW58qKNPgkyb4VKrIs1prvOpTAoqYD8Z4zwuE_JEgOHAeRc_N9tpVBIPBAcpdWCoCaQSVisNG3osw_IodCU1lIXG_MEQsl2hqdmxZhJjE6d_hqUL185-sB9RA6rSPDjuMsUcErgQIq5v5uaJgBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
IRGC now</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/82303" target="_blank">📅 17:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82301">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aEYnmS6bbewY-dFzcnhUFXejMX4S4RO4SQ6HtEuWUfnNtoW9cIq4ZQjaPWrAPNspDMbuLSEQK7TEUrWCe4Mm8a1_2PGSjycqHYCmNUAOtwF6ih291LNYzBl5nsnBFSoAQkluwPEPxIWaFRqwnyrf1JyDuAnaUvGlAUyhkdaXEq9IxQqkXn97xj_b_mjmGhAUnk9LQmW4hW0yjK0yVmrYgGm0Tfylhe7k_Tyf46CX2cO4y438NEUcXOOzRRyFXpMF16Qc76fNz359Ppo8y_0Pi9JOpt3FiRGC7bwuCa8nbpJan0QbTWdgYZuVYF2IEMMLjq2gt3N-DTjDqSBjLKg__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tz9rqSitTc_UCa-M7s6g8-jJAMdwG_20IIy-GS5VJER7-C9Y2WAL-Kn_54cMoKPI1XRFmV7DpiCa5-6VqPvCuhZltzMIhIUWjXY_ABfB-tnqaV9l8LStmuwuzHspgXVUFDf3hD9FZikJaD0QwgAirCSs-GKSeS5toW-HzKcYNm7PFsM0KZnG62y-rrU1rbmmKCQOM4WrwCBP8SceyDdarRDs6kuTZDM0-aqgH27V0zQqY7OkjUdimir0FVmi8-sp6Yf6M_cqNzVOvUVOC776OmIcK9t201YQrpWNJv48F3FvaAeb08toHEs-atxpUQxOH5glquVRO4ihS5GjvCPQOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇺🇸
مواقع التتبع: رصدت حاملة الطائرات الأمريكية "يو إس إس أبراهام لينكولن" في صور الأقمار الصناعية "سنتينل-2" بتاريخ 10/07/2026 تبحر الحاملة حاليًا شمالًا في خليج عُمان، وتقترب بشكل خطير من نطاق صواريخ إيران، دون وجود أي مرافقة مرئية.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/82301" target="_blank">📅 17:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82300">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴‍☠️
زيلينسكي : لم تعد مصفى في روسيا اسلحتنا لا تستطيع الوصول إليها ؛ استهدفنا مصافي روسية على عمق ٢٥٠٠ كم في سيبيريا</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/naya_foriraq/82300" target="_blank">📅 17:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82299">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
🔵
🇮🇶
بسبب عدم فعالية منظومة الباتريوت
وزارة الدفاع الألمانية : تقرر تقليص عدد قواتها من ٥٠٠ إلى ٣٠ عسكري في محافظة اربيل شمالي العراق وابلغت حكومة الإقليم بهذا القرار بعد ان كان مقرر بقائهم حتى منتصف عام ٢٠٢٧.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/82299" target="_blank">📅 16:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82298">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية:
مروحية من طراز CH-53 سوبر ستاليون تابعة لسلاح مشاة البحرية الأمريكية تقوم بتوصيل الإمدادات إلى سفينة تابعة للبحرية الأمريكية في بحر العرب.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/82298" target="_blank">📅 16:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82296">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOx_WpLfDpnFt09XVCPY4u5NphYRI2kzV_nLHKrtFnSFfWwKM5SO_8So7W089AXcZI_6IhDeCpOoP7RWd4t0W3oPxLB1Mp33lcDFJ_G5AsqfseLR0OA2GTzdUX8ZKImyMEdDC9HxLaFs4OGUNgdBcxAivQg6TOXfLv78UtjuOYPqQEY7BLCsITPEoooei6ff2OHJ3esE04OFfEAmbUkVugzUG_Lcg2YgZ6uJLi2_VKYv7eoVBtm2tuax8sHoT0kErqFrEmHD5Rc47_nNOSJy0jAHY0BIEriSW_-dYMniavgkNjPTBzNPSnqEfjvHa8vE2UCh3cz_P8Mz0_W8YgK-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNcFaWWHCQgjNBfuf_Rr-wRr91lHQ1e8vNLmFbhNGSSjlwOXylvH16GDY6OcuGiG2oA2WukSt0TYW90hgEtB7aSrWjE31GT4jlb6QlX0zgAbVtPCrBWpx9OmUFfAF800u-81KRFhMy3OMy8sYLKLVJ2wRqHp1OmNK_ILmGkF8Dy4tOrrK-DEztyPzfcc-dkJlBCBJwQ3mTthhPWw2TdBEhODArUZyepT2hXR1eEW3Gz9TE9593WTDSSC2Wb5oybqJzYuVaJsA1_EmkBZ3QxgWeT1sirOTlWANiuHGMpJ-bLFvU6GptgG8H6OMBRxofNVmS3fAGnRBI7rMQyTDolvqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇺🇸
مواقع التتبع:
رصدت حاملة الطائرات الأمريكية "يو إس إس أبراهام لينكولن" في صور الأقمار الصناعية "سنتينل-2" بتاريخ 10/07/2026 تبحر الحاملة حاليًا شمالًا في خليج عُمان، وتقترب بشكل خطير من نطاق صواريخ إيران، دون وجود أي مرافقة مرئية.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/82296" target="_blank">📅 16:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82295">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbPP7Y8iz-9IRlQlqXHxgF98ht96Ady25rJ8Y8RGCZcS6Y3EFjScLwOTdxeB6atBB_UzcwASk7WJQErPSjkJaYGQEeeL09kRK6aExh-exNVyfj3gTRbSRmFQIo5D6yr2CiVSm4ea32YRt8hrYFsEj_AY1SjvsP3c2smTPnaKEJY57KhSnO_zmUWSUo7Z3piWI3jz4C1uHYGueZp99G-SHND8DHkAJX-uUXHeMniDUJ_1cHxkwQScqYzOKSi0-Vm9Y8LFpTFdWeUYNMWQi6xsNhO-8cGrIRcF4z98ZK1KjZKeG7bINWgdxYCQ7Dge3IvxY6Lq6wmPJPmWnbKKs2SyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
لن أوقع على مشروع قانون الإسكان الذي وافق عليه الكونغرس بالكامل وأُرسل إلى البيت الأبيض احتجاجًا على حقيقة أن مجلس الشيوخ الأمريكي غير قادر على تمرير قانون إنقاذ أمريكا، الذي يحظى بتأييد 97% من الحزب الجمهوري، ونسبة عالية جدًا من الديمقراطيين غير السياسيين.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/82295" target="_blank">📅 16:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82294">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
غضب شعبي واسع في محافظة البصرة وعموم العراق وإضراب شامل يدخل حيز التنفيذ في مراسي بيع الأسماك مع تظاهرات مرتقبة للصيادين عصر اليوم احتجاجًا على قيام خفر السواحل الكويتي بقتل صياد عراقي ودعوات للحكومة العراقية لاتخاذ موقف حازم إزاء الجريمة الكويتية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/82294" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82293">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
نائب الرئيس الايراني:
العراق كان لسنوات تحت الاحتلال والنفوذ الأمريكي. الحضور الواسع للشعب في النجف وكربلاء أغضب ترامب، وأظهر أن النفوذ الروحي للقائد الشهيد يتجاوز حدود إيران.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/82293" target="_blank">📅 16:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82292">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📰
مصادر لـCNN:
ادارة ترامب لا تريد مشاركة اسرائيل في الهجمات على ايران.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/82292" target="_blank">📅 16:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82291">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
🔹
غروسي مدير الوكالة الدولية للطاقة الذرية:
نحن نراقب الوضع في محطة بوشهر للطاقة النووية في إيران ونحث جميع الأطراف على ضبط النفس.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/82291" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82290">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
فيلق بدر يرصد هتافات الملايين.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/82290" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82289">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇷🇺
🇮🇷
وصول اول 6 موظفين من شركة روس آتوم الروسية الى محطة بوشهر النووية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/82289" target="_blank">📅 15:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82288">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
بيان لرئيس هيئة الحشد الشعبي
:
بعد اختتام مراسم تشييع المرجع المعظم الشهيد السيد علي الخامنئي (رضوان الله تعالى عليه)، التي شهدت حضوراً جماهيرياً تاريخياً جسّد عمق الوفاء الذي يكنّه الشعب العراقي لرموزه وقادته، نتوجه بخالص الشكر والتقدير إلى جميع الجهات التي أسهمت في إنجاح هذه المناسبة الوطنية والإنسانية الخالدة.
ونتقدم أولاً بجزيل الشكر إلى الحكومة العراقية والعتبات المقدسة لما وفرته من دعم ورعاية وتنسيق عالٍ أسهم في نجاح المراسم، كما نعرب عن بالغ تقديرنا إلى قواتنا الأمنية التي أدت واجبها بكفاءة ومسؤولية عالية، وأسهمت في حفظ الأمن وتأمين انسيابية مراسم التشييع.
ونخص بالشكر أبناءنا في هيئة الحشد الشعبي، وفي مقدمتهم الأخ رئيس أركان الهيئة، وجميع القادة والمجاهدين والمنتسبين، الذين بذلوا جهوداً استثنائية في التنظيم والخدمة والتأمين، مؤكدين روح الانضباط والإخلاص في أداء الواجب.
كما نتقدم بخالص الامتنان إلى المواكب والهيئات الحسينية، والمتطوعين والخدّام، وإلى الأسرة الإعلامية والثقافية، والنخب الفكرية، ومنظمات المجتمع المدني، وكل من أسهم في خدمة المشيعين ونقل صورة هذا الحدث التاريخي إلى العالم.
ونعبر عن عميق تقديرنا لعائلة المرجع الشهيد، على ثقتها بالشعب العراقي، كما نقف بإجلال أمام أبناء شعبنا العزيز الذين صنعوا بحضورهم ووفائهم ملحمةً ستبقى خالدة في ذاكرة العراق.
نسأل الله تعالى أن يتغمد الشهيد الجليل بواسع رحمته، وأن يجزي جميع من أسهم في إنجاح هذه المناسبة خير الجزاء، وأن يحفظ العراق وشعبه، ويديم عليه نعمة الأمن والوحدة والعزة.
رئيس هيئة الحشد الشعبي
فالح الفياض</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/82288" target="_blank">📅 15:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82287">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔻
رئيس أركان الحشد الشعبي عبد العزيز المحمداوي:
بسم الله الرحمن الرحيم
لقد أقدم أبناءُ العراق الأوفياءُ والغيارى، مرةً أخرى، على تعريف العالم بمواقف الكبرياء، وفاضت فيهم مكارمُ الرجولة والشهامة والبطولة وكرم الضيافة والمواساة وأداء واجب العزاء.
فكانوا جديرين باستقبال وتشييع وتوديع السيد الزائر لجدّه أمير المؤمنين (عليه السلام)، والشهيد الوافد على جدّه سيد الشهداء (عليه السلام).
وكأنّه أراد أن يقول: (أوفيتَ يا ابنَ رسولِ الله).
عظّم الله أجوركم،
وأحسن الله لكم العزاء،
وشكر الله سعيكم.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/82287" target="_blank">📅 15:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82286">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
🇮🇷
مشاهد تنشر لأول مرة
جانب من مجلس العزاء النسائي في النجف الاشرف لتوديع جثامين العائلة المباركة للامام الشهيد
#قوموا_لله
🏴</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/82286" target="_blank">📅 15:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82285">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c1048520.mp4?token=s1enFUE5_oRi7CH18VIJPgMuMC3JuOAW1nxqE5vif9m0JVQuc0IUfZAJoiOagXW5Vyj6fdVxZ6APFcgz-F7Kx74ws9YU81GrccJvCzAsQ_fEpYYRMTAnZUJxItWChMMRC4O4qSbLJ6YYP7eP6q3vW8xRu7sCjWDvINTLY5I0_gyqvOecqj24cSCpLZQoS0UsJ0nXKgKzpwVyCtB8mWGoWE_tk2bwVb6qf-d6O4fFeI3glLe3JToReXIaLq-R0ySBnAvq-GuyGYwaiUUtfAXYiIXfqnZd52zP-ULn5Fd5ilrWfQwyDItTtuCYzS1F2hERhTHwLsWyg9kyo_gYu6TzZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c1048520.mp4?token=s1enFUE5_oRi7CH18VIJPgMuMC3JuOAW1nxqE5vif9m0JVQuc0IUfZAJoiOagXW5Vyj6fdVxZ6APFcgz-F7Kx74ws9YU81GrccJvCzAsQ_fEpYYRMTAnZUJxItWChMMRC4O4qSbLJ6YYP7eP6q3vW8xRu7sCjWDvINTLY5I0_gyqvOecqj24cSCpLZQoS0UsJ0nXKgKzpwVyCtB8mWGoWE_tk2bwVb6qf-d6O4fFeI3glLe3JToReXIaLq-R0ySBnAvq-GuyGYwaiUUtfAXYiIXfqnZd52zP-ULn5Fd5ilrWfQwyDItTtuCYzS1F2hERhTHwLsWyg9kyo_gYu6TzZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اندلاع حريق كبير وغامض بالقرب من مطار اربيل الدولي شمالي العراق
🚨
🔥
، قرب المطار توجد قاعدة للجيش الأمريكي!
🇺🇸
✈️</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/82285" target="_blank">📅 14:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82284">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
اندلاع حريق كبير وغامض بالقرب من مطار اربيل الدولي شمالي العراق
🚨
🔥
، قرب المطار توجد قاعدة للجيش الأمريكي!
🇺🇸
✈️</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/82284" target="_blank">📅 14:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82283">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
مجلس القضاء الاعلى في العراق يصدر بيان بخصوص "سرقة القرن":  موجز هذه الجريمة يتلخص بان الشركات الأجنبية العاملة في العراق تودع لدى الهيئة العامة للضرا ئب امانات  بقيمة 5% من قيمة المشروع لضمان انجازه وبعد انتهاء عمل الشركة من حقها تسحب هذا المبلغ خلال خمسة…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82283" target="_blank">📅 14:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82282">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇶
مجلس القضاء الاعلى في العراق يصدر بيان بخصوص "سرقة القرن":
موجز هذه الجريمة يتلخص بان الشركات الأجنبية العاملة في العراق تودع لدى الهيئة العامة للضرا ئب امانات  بقيمة 5% من قيمة المشروع لضمان انجازه وبعد انتهاء عمل الشركة من حقها تسحب هذا المبلغ خلال خمسة سنوات ولكن شركات التعقيب ومنها شركتي المحكوم نور زهير القانت والمبدعون اتبعت اجراءات غير اصًولية في عملية سحب هذه الامانات  لهذا تم اتخاذ الاجراءات القانونية بحق جميع المتورطين بهذه الجريمة من اصحاب تلك الشركات والموظفين اللذين ساعدوهم في عملية السحب الغير أصولية.
ثانيا
تم الاتفاق بين رئيس مجلس القضاء ورئيس مجلس الوزراء السابق  وبعد الحصول على موافقة القاضي المختص بالتحقيق في تلك القضية على اطلاق سراح المتهم الأساسي فيها المدعو نور زهير بكفالة ضامنة لاعادة تلك الاموال المسحوبة وعلى شكل دفعات مقابل تخفيف العقوبة عنه في حينه وفعلا تم اعادة مبلغ قدره ٣٦٥ مليار دينار من اصل مجموع المبلغ المترتب بذمة الشركتين  التابعة له القانت والمبدعون وقدره (١,٦١٨,٣٧٠,٨٨٢,٠٠٠) ترليون دينار وهذا المبلغ هو جزء من مجموع المبلغ الكلي المسحوب من مصرف الرافدين من قبل جميع شركات السحب والبالغ قدره ( ٣،٨٣١،٣٧٠،٨٨٢،٠٠٠) ثلاثة ترليون وثمنمائة وواحد وثلاثين مليار وثلثمائة وسبعين مليون وثمنمائة واثنين وثمانون الف دينار عراقي
ثم سافر المتهم المذكور خارج العراق  وتوقفت عملية التسديد لهذا تم احالته على محكمة جنايات  مكافحة الفساد المركزية وصدر حكم غيابي بحقه بالسجن لمدة عشر سنوات مع تنظيم ملف استرداد ومخاطبة مديرية الشرطة العربية والدولية لاعادته إلى العراق
بعد صدور قانون تعديل قانون العفو قدم محامي المحكوم المذكور طلب بشمول موكله بالقانون مقابل اكمال  عملية تسديد بقية المبلغ المترتب بذمته  وفعلا تم مخاطبة وزارة المالية لبيان الرأي بخصوص هذا الطلب باعتبارها الجهة المتضررة ويجب استحصال موافقة الوزير على الية تسديد المبالغ المترتبة بذمة المحكوم بحسب قانون تعديل قانون العفو ولم ترد إلى المحكمة اي اجابة بخصوص ذلك لذا بقي موضوع شمول المحكوم المذكور بقانون العفو معلق لحين الاتفاق مع وزارة المالية على الية تسديد المبالغ مع المحكوم او وكيله المحامي
وفي نفس الوقت صدرت احكام حضورية بالسجن بحق  ١٢ موظف بعناوين مختلفة في الهيئة العامة للضرائب ممن ساعد المحكوم في عملية سحب المبالغ  بمعاملات خلاف السياقات المتبعة وحاليا هم في السجن يقضون مدة محكوميتهم مع ملاحظة  إمكانية  شمولهم بقانون تعديل قانون العفو النافذ لكن بعد تسديد قيمة التعويض الذي تحدده وزارة المالية ويدفع من قبلهم
كذلك صدرت احكام غيابية بالسجن  بحق مدير مكتب رئيس الوزراء في حينه وعدد من المستشارين مع تنظيم ملفات استردادهم من الدول التي يقيمون فيها كذلك مذكرات قبض بحق اخرين  مع ملاحظة ايضا ان جميع هولاء ممكن شمولهم بقانون تعديل قانون العفو في حال تسديد ما ترتب بذمتهم من مبالغ
وصدرت احكام حضورية بالسجن بحق اشخاص من غير الموظفين استغلو علاقاتهم مع وزير المالية في حينه وساهمو في تسهيل سحب اموال هذه الشركات .وتمت مصادرة اموالهم المنقولة وغير المنقولة
وتم اجراء التحقيق مع رئيس الوزراء الذي حصلت خلال فترة حكومته هذه الجريمة وتم غلق التحقيق بحقه لعدم كفاية الادلة
كذلك تم مصادرة عقارات واموال منقوله في العراق ودولة الكويت عائدة لقسم من المحكومين الموجودين حاليا في السجن
ثالثا
اما بخصوص قضية شركة مصافي الشمال والمتهم الموقوف عدنان الجميلي وعدد من اعضاء مجلس النواب سوف يتم اتباع نفس الاجراءات المشار اليها فيما تقدم في حال كون جريمة اي منهم مرتكبة قبل تاريخ نفاذ قانون تعديل قانون العفو و يسدد ما بذمته من أموال إلى الوزارة المتضررة
اما إذا كانت الجريمة مرتكبة بعد نفاذ  قانون العفو سوف يتم التعامل مع المتهمين بسياقات واجراءات مختلفة كون جريمتهم غير مشمولة بقانون العفو .لدا يجري البحث حاليا و بالاتفاق   مع السيد رئيس الوزراء  لوضع خارطة طريق تتفق مع الآليات الدستورية و القانونية لتحقيق الهدفين المنوه عنهما في اعادة اموال الدولة مقابل تخفيف الاجراءات القانونية بحق من يعيد تلك الاموال طوعا.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/82282" target="_blank">📅 13:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82281">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇬🇧
‏ هيئة بحرية بريطانية: التهديد الأمني في مضيق هرمز لا يزال مرتفع</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82281" target="_blank">📅 13:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82280">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
رئيس جمعية الصيادين العراقيين بدران التميمي يروي تفاصيل استشهاد الصياد برصاص خفر السواحل الكويتي</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82280" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82279">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇷🇺
الكرملين:
سنوسع المنطقة الأمنية داخل أوكرانيا.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82279" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82278">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
غضب شعبي واسع في محافظة البصرة وعموم العراق وإضراب شامل يدخل حيز التنفيذ في مراسي بيع الأسماك مع تظاهرات مرتقبة للصيادين عصر اليوم احتجاجًا على قيام خفر السواحل الكويتي بقتل صياد عراقي ودعوات للحكومة العراقية لاتخاذ موقف حازم إزاء الجريمة الكويتية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/82278" target="_blank">📅 13:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82277">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
غضب شعبي واسع في محافظة البصرة وعموم العراق وإضراب شامل يدخل حيز التنفيذ في مراسي بيع الأسماك مع تظاهرات مرتقبة للصيادين عصر اليوم احتجاجًا على قيام خفر السواحل الكويتي بقتل صياد عراقي ودعوات للحكومة العراقية لاتخاذ موقف حازم إزاء الجريمة الكويتية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82277" target="_blank">📅 13:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82276">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تبعات حرب إيران
🇮🇷
⚔️
‏
الطاقة الدولية:
نتوقع عجزا في المعروض العالمي للنفط بـ 860 ألف برميل يوميا في 2026
🛢️
📉
.
إمدادات النفط العالمية ستنخفض بمقدار 3.7 مليون برميل يوميا في عام 2026
🛢️
📉
.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/82276" target="_blank">📅 11:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82275">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
🇮🇷
مسؤول أمريكي حول إيران:
الوضع متغير وقد تستأنف الضربات إذا لزم الأمر.
قائد حاملة الطائرات لينكن ببحر العرب أبلغ أفراد طاقمها بالحفاظ على جاهزيتهم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/82275" target="_blank">📅 10:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82274">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRwbZw5t-bydh0ZJHCkzWlS4RCCdT8KAf8zMhN-xhXggskF5XKwHdXdWxknI6exMftsYk0wtKcJeUQRyXlqxP00kfmJt8ipU17eLkFb-WZ43liaYUVzBy6jAsg-6FR7zHSkeQN_DICe38fwuTl0Gu2E94c_znalA81qQpyKqtVFNUkpraJctjhV-bc3kCyAlFkdyxB_UpZVjxVd2RpTiiFqtlScRNcLUd0481i61Lsg7mCaXz-WtDTYrx9v2PRlrSEe2zkNRDBBWkDbVe8SENYAL99H0tAMxsm3oUHbRH00KLzhN7eXxLdGz-6yX3hU8Rj_3C_-NT_mZKQjY3uinlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
الرئيس الإيراني مسعود بزشكيان يوجه رسالة شكر إلى العراق وشعبه والمراجع العظام على مراسيم التشييع المهيبة التي جرت في العراق.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/naya_foriraq/82274" target="_blank">📅 06:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82273">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
مسؤولين أمريكيين:
التقرير الإسرائيلي عن مخطط إيراني لاغتيال ترمب قد يكون محاولة لدفعه نحو التصعيد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/naya_foriraq/82273" target="_blank">📅 04:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82272">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مسؤول أمريكي:
عدم شن الجيش الأمريكي ضربات جديدة على إيران الخميس جاء نتيجة جهود إقليمية لخفض التصعيد</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/naya_foriraq/82272" target="_blank">📅 02:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82271">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtBahM6bN4tXrb3W9InQ5MvESEwaom0wLK1N1BfoZ1KgJOyygsfO3uxvFOJV6PPNhED_Wt7rwLnKXXv2wNsLULOnQpX4QN-fJJrdPeIeyqmwJo9wWzI7rW1IdTYcdgwhma5_TULCF5h28OpvdmFf9HFFg4RAwhTH7KhkB_9sDtIqUWVWMU-aaFqV-2jHuSOgPv4ro9G787tqoPtReDPVfYV_Yq_JljhsM5hmHdgJTAAfW5YD_SBNERz9DZ5Buw9pHRv7Urz3xe6lSO8KWsH3-edkUoiGjRGb1XeoocOFAC0JQ5YBcXvSnLqWrfiQoOIF2-RkwtzMYE26EG_beaM-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الآن تم دفن أمامنا القائد
💔
الصلاة الصلاة يرحمكم الله
#قوموا_لله
🏴</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/naya_foriraq/82271" target="_blank">📅 01:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82270">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
مصدر إيراني: لم يحدث أي حادث أمني قرب مرقد الإمام الرضا (ع) أو على طول مسار تشييع جثمان الشهداء.  "بلوار سرافرازان" في غرب مشهد، ويبعد أكثر من 15 كيلومترًا عن مرقد الإمام الرضا (ع).</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/naya_foriraq/82270" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇰🇵
كوريا الديمقراطية الشعبية العظمى : بيونغ يانغ قررت تعزيز قواتها النووية نوعيا وكميا</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/naya_foriraq/82269" target="_blank">📅 01:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
مساعد الأمن لمحافظة خراسان الرضوية الإيرانية: إطلاق نار في منطقة "بلوار سرافرازان" في مدينة مشهد المقدسة، أسفر عن مقتل شخصين؛ هوية القتلى لم يتم تحديدها بعد.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/naya_foriraq/82268" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">كما اكدنا لكم ان العدوان انطلق من الكويت وتحت غطاء معلوماتي من قاعدة الظهران الأمريكية في السعودية</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/naya_foriraq/82267" target="_blank">📅 00:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
مساعد الأمن لمحافظة خراسان الرضوية الإيرانية:
إطلاق نار في منطقة "بلوار سرافرازان" في مدينة مشهد المقدسة، أسفر عن مقتل شخصين؛ هوية القتلى لم يتم تحديدها بعد.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/naya_foriraq/82266" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbrm0_7l5QQQsbT1hPNj_SqEwPo0pi0ReqJitDzn3e74L01LBblNJ9-v7QrimbJufcQDbAZWFFFUxLhgf1KXoenh2yZQiLcoOqFXNkj0km-W7ykqg9VY_s95uabki256m5eOkJkRBqsG_azpcCniIgw1IE5Nyc3t6TjhvToWpoy0Ngq7qWp758r1q5VtW7ks1WWvDnzjX04s5A9EIuGtk4DHwuNTeZtFfOykHzQMfb8Qp44TUxOwy54inmbUOspGaUw6x88LeYci_ro3Z66JHDZzn8BgYa0h5-3zBbrCZJEr80sOnaodNJT2-NkqK0dQ9UaFx7ZSAQb6jZ82crwjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكويت تقتل العراق</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/naya_foriraq/82265" target="_blank">📅 00:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82264">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBT1sqKYlrcJ7G6TlhJHhT02NROP-5EU-t9iLEgsMshrM-njv75XzjtTeIHJ4eA6pfZWYsPHNOKcdyFWOEL_sX-EmqMalDPOI-xbMp060Ae630KW-UFtEt3TfYQ01WN1Ylvx98Sx6JCuuXToUrLm1huQCELjk387tggzfAfne_r122Z28VJpv1ayZrUpM9YAqNXdAkGWTA08o86zCtjFYemdsbWKwnf9-mdsGbAsQLCIrL8_TISS99qawcVn-hcw_vURGocJC1ncsQF-uOHJHqzOB8soNz37tyYAnB_8YXnF22-WqUPj4fuAHON8nBz0u1VLgOZla5Wepb2agaJ4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رسالة من رجال ساحة المعركة إلى المشيعين:
الحمد لله أنكم ملأتم الفراغ الذي تركناه في تشييع الإمام الشهيد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/naya_foriraq/82264" target="_blank">📅 00:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82263">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO3wSPRCkAGgI6O93N4FEPPlcSw-Gepgzgvknk98fZUJww9rsyEmFih_jmt8XDGtPrTSB3UGGcXBt92IAYZPFJTHCgOqhjARbThmErw3ZiJO0fJpuzWzHrfAB8uUH4q_AeRHzoN1-4OkCx01DpcTdAOx1hsNYALUPW7uG7-z4qIY8dJj5EdoP1co8TcBGxP73CdOtbEwM43X_hx_y1_UB7L2xi1r9BX5S5IcQZRn6HU9UU9P1crft5NLd7qQCHgGcAWnqB1_4axkB3pj9sxeHeRjADoiWcPLbZ4JrgiZaYGKWohCTaPMRxjYRfJCdic7TDD-eRxEAR_E0Cu6D3ZSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شُكْرٌ بِحَجْمِ الْجُمُوعِ الْمِلْيُونِيَّةِ لِنَجْلِ الْمَرْجَعِ الْأَعْلَى، سَمَاحَةِ السَّيِّدِ مُحَمَّد رِضَا السِّيسْتَانِيِّ؛ عَلَى انْتِقَائِهِ الْمُفْرَدَاتِ الْبَلِيغَةَ الَّتِي تَحَدَّثَ بِهَا خِلَالَ مَرَاسِمِ تَشْيِيعِ السَّيِّدِ الْوَلِيِّ الْمُسْتَطَابِ، مُعْتَمَدِ الْمَرْجِعِيَّةِ الرَّشِيدَةِ فِي الْعَتَبَةِ الْحُسَيْنِيَّةِ الْمُقَدَّسَةِ، سَمَاحَةِ الشَّيْخِ الْمُجَاهِدِ عَبْدِ الْمَهْدِي الْكَرْبَلَائِيِّ.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/naya_foriraq/82263" target="_blank">📅 00:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82262">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac4250178.mp4?token=NEx4O-u6WugpTEahOfHgxkApazBW62HA2k5d8ZmrLgMPNfJSQwdXLSPAkXhfL-HkrKB976gj34uTXRLnQk3oaLR79a-LHyx8Aq-0tYr4IQtJrphMAvvY83J38NoEsgVtU8ROhkmnIqXgpZJyGGW2Dz_o59mIY5oMukyzXV7lPW4tefTGq7iTf0vZ1iGKud4uI2Jrij0WjF5Mt67z99aDLiIgP6Em7QnJkrtVnNOOwFApvIkEkqqiTgIL77PQh4--EgfF8FrNagTSfaxYJ7mKv0Ku9vbhZ1V4YWv0wbR5XzuGPDMMdU9qPuNin1FwAjD4iITLZMV0vCPsmbrm6ibxsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac4250178.mp4?token=NEx4O-u6WugpTEahOfHgxkApazBW62HA2k5d8ZmrLgMPNfJSQwdXLSPAkXhfL-HkrKB976gj34uTXRLnQk3oaLR79a-LHyx8Aq-0tYr4IQtJrphMAvvY83J38NoEsgVtU8ROhkmnIqXgpZJyGGW2Dz_o59mIY5oMukyzXV7lPW4tefTGq7iTf0vZ1iGKud4uI2Jrij0WjF5Mt67z99aDLiIgP6Em7QnJkrtVnNOOwFApvIkEkqqiTgIL77PQh4--EgfF8FrNagTSfaxYJ7mKv0Ku9vbhZ1V4YWv0wbR5XzuGPDMMdU9qPuNin1FwAjD4iITLZMV0vCPsmbrm6ibxsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بعد 24 ساعة من لقاء الجولاني وترامب وتلقي تعليمات لمهاجمة حزب الله.. عصابات الجولاني تشن حملة أمنية على حي عش الورور العلوي وتعتقل عدد كبير من الشبان العلوية حيث لفقت التهمة مسبقاً "خلية مسؤولة عن تفجيرات دمشق مرتبطة بحزب الله" وذلك لذريعة الدخول في حرب لبنان</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/naya_foriraq/82262" target="_blank">📅 00:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82261">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391970061f.mp4?token=uizkovjxXvnzVe6KyWF-vTxxBMAq8Y-p1Le3PSnYITAZfzeIYyIxfykGJVTTJOtU_Zc3Cve6d3MS0jYfFHhHwNUFp_0g2NmcFDST_aG_le_Y8BQm0R1EltXynl4xahHDt5PwOZfzLcEbYi5Fnz6PVdFqjBpfM1G7j6IgHyd4UNnGYwXN7rNkwqH5rontzFa8NmeyZLFh9OLlqLKAodc_m2yRyHfsKUJKg7ayRkqsK1z0YwoXZE8ynG2cDm0HjVPSaYfS8meW5ivI_hxoOP0IFyfZvtxWAyCxmuXEiFl2IZx_lpi8neELRs3lRAapSdGMsswgWpDZVdtkmSe5p7PcB7ZBxVZ_kq7E6ma67CAjOQzj8SVl97vzIdOjI-VIA6J3uRBP3T0eSktmokcSbP005cVgtAc6DCaPtr84Rrw3u7Y9BWBBAChwSPGdy7GVp3twKp0PK6qgmqSKol6x7fraQZUZLfXJzo-na9qKiX-gCVaCEP8XEaDJ0I2F61iqfVCoIASzU1d7BQ-fWaY_IIUQRtHMYJ83bpU7BGyM_Vsub7U9xBVcbXb18o_BV9Z7b1cZbHIzZbVPIX3HUNi_GbPRoUNbRt_HXt-JYcTI7l7K-GeQS29iJlfP9t4QiB1Yld-0ZeVFh65nFModHaRIU8UkbDV5TKa6P5JqqM-1euQr85I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391970061f.mp4?token=uizkovjxXvnzVe6KyWF-vTxxBMAq8Y-p1Le3PSnYITAZfzeIYyIxfykGJVTTJOtU_Zc3Cve6d3MS0jYfFHhHwNUFp_0g2NmcFDST_aG_le_Y8BQm0R1EltXynl4xahHDt5PwOZfzLcEbYi5Fnz6PVdFqjBpfM1G7j6IgHyd4UNnGYwXN7rNkwqH5rontzFa8NmeyZLFh9OLlqLKAodc_m2yRyHfsKUJKg7ayRkqsK1z0YwoXZE8ynG2cDm0HjVPSaYfS8meW5ivI_hxoOP0IFyfZvtxWAyCxmuXEiFl2IZx_lpi8neELRs3lRAapSdGMsswgWpDZVdtkmSe5p7PcB7ZBxVZ_kq7E6ma67CAjOQzj8SVl97vzIdOjI-VIA6J3uRBP3T0eSktmokcSbP005cVgtAc6DCaPtr84Rrw3u7Y9BWBBAChwSPGdy7GVp3twKp0PK6qgmqSKol6x7fraQZUZLfXJzo-na9qKiX-gCVaCEP8XEaDJ0I2F61iqfVCoIASzU1d7BQ-fWaY_IIUQRtHMYJ83bpU7BGyM_Vsub7U9xBVcbXb18o_BV9Z7b1cZbHIzZbVPIX3HUNi_GbPRoUNbRt_HXt-JYcTI7l7K-GeQS29iJlfP9t4QiB1Yld-0ZeVFh65nFModHaRIU8UkbDV5TKa6P5JqqM-1euQr85I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارة الخارجية العراقية: وفاة أحد الصيادين العراقيين الذين تم اعتقالهم من قبل خفر السواحل الكويتي.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/naya_foriraq/82261" target="_blank">📅 23:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82260">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حاكم مدينة كنارك الإيرانية: الأجهزة المعنية هرعت على الفور إلى موقع الهجوم والتحقيق جار في أبعاده وتفاصيله</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/naya_foriraq/82260" target="_blank">📅 23:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82259">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مكتب نتنياهو: أطلع ترامب نتنياهو على التحركات الأمريكية ضد إيران.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/naya_foriraq/82259" target="_blank">📅 23:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82257">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
الإطار التنسيقي في العراق : نتقدم بخالص الشكر والتقدير إلى جميع المشاركين وإلى كل من أسهم في تنظيم وإقامة مراسم تشييع نعش السيد علي الخامنئي في النجف الأشرف وكربلاء المقدسة</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/naya_foriraq/82257" target="_blank">📅 23:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82256">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔻
مصادر لنايا: الصواريخ الأخيرة التي استهدفت إيران انطلقت من الكويت</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/naya_foriraq/82256" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82255">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مصدر إيراني ينفي وقوع انفجارات في بندر عباس وقشم وسيريك وجاسك.</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/naya_foriraq/82255" target="_blank">📅 23:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82254">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">محافظ بوشهر الإيرانية: نحقق في أسباب الانفجارات في بوشهر وجغادك إن كانت ناجمة عن دفاعات جوية أو مقذوفات معادية</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/naya_foriraq/82254" target="_blank">📅 22:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82253">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇦
🇷🇺
الجيش الأوكراني يعلن مقتل أربعة من أفراد طاقم طائرة هليكوبتر من طراز Mi-8 بعد تحطم الطائرة أثناء اعتراض طائرات بدون طيار روسية في منطقة بولتافا في 30 يونيو.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/naya_foriraq/82253" target="_blank">📅 22:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82252">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مصدر إيراني ينفي وقوع انفجارات في بندر عباس وقشم وسيريك وجاسك.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/naya_foriraq/82252" target="_blank">📅 22:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82251">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd6632e1f9.mp4?token=nTjP0TOa527tv_uzZY5iAsB2CjeyzxPP8Y8UKgQze9EUKaXk36EV_SKX3IL5hsxq-R-00PEASS347PzkCFwYeBd4DC8BYOEFEeToYgt_NTtZJZ3RekHCNCCluv5_o2Sj08wyMPFZa3_D71ZUrLXJqN-9yV0DLAW4Bz9ZAUf7Tw7tuMw2rrsYWjv2sYwpd8b2LxEP_PtQqLgJlB4Nwdh_yKzrnErkaZ9zb2ipLwLmZIWPO7bJxJ-60YbOYxh60H5R6ip--dc7ucZv6qhbGg6mRukDpwut6YKGivVFTajhYJypVi7O6k_a1GGhEdS2-a_pSFe3F33rqitKYBoH74Z71w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd6632e1f9.mp4?token=nTjP0TOa527tv_uzZY5iAsB2CjeyzxPP8Y8UKgQze9EUKaXk36EV_SKX3IL5hsxq-R-00PEASS347PzkCFwYeBd4DC8BYOEFEeToYgt_NTtZJZ3RekHCNCCluv5_o2Sj08wyMPFZa3_D71ZUrLXJqN-9yV0DLAW4Bz9ZAUf7Tw7tuMw2rrsYWjv2sYwpd8b2LxEP_PtQqLgJlB4Nwdh_yKzrnErkaZ9zb2ipLwLmZIWPO7bJxJ-60YbOYxh60H5R6ip--dc7ucZv6qhbGg6mRukDpwut6YKGivVFTajhYJypVi7O6k_a1GGhEdS2-a_pSFe3F33rqitKYBoH74Z71w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنشر لأول مرة
رئيس أركان الحشد الشعبي الحاج ابو فدك المحمداوي يقوم بمسح مقتنيات المشيعيين طلبوا النذر والذكرى من الضريح الشريف.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/naya_foriraq/82251" target="_blank">📅 22:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82250">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية في شابهار وسيستان وبلوشستان إيران</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/naya_foriraq/82250" target="_blank">📅 22:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82249">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اكسيوس نقلا عن مصدر أمريكي : ليس لنا أي علاقة باي ضربة ع إيران حاليا</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/naya_foriraq/82249" target="_blank">📅 22:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82248">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اكسيوس نقلا عن مصدر أمريكي : ليس لنا أي علاقة باي ضربة ع إيران حاليا</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/naya_foriraq/82248" target="_blank">📅 22:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82247">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اكسيوس نقلا عن مصدر أمريكي : ليس لنا أي علاقة باي ضربة ع إيران حاليا</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/naya_foriraq/82247" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82246">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
مصادر لنايا: الصواريخ الأخيرة التي استهدفت إيران انطلقت من الكويت</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/naya_foriraq/82246" target="_blank">📅 22:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82245">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مصدر إيراني ينفي وجود انفجارات في جزيرة خرج</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/naya_foriraq/82245" target="_blank">📅 21:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82244">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=md4BjzMZr9oZGlTlcxd4XbosuSYXTuF3_RB9_hxdj5X3BE7C-625DoFD8P6JUZjYcdhSX1V7rXd3FPluWBb-O3Qwxcks04IGLZC03MzmEJs0734RIDWz737Ww-TD5u099vWTwPdDgHhEi1o63wRrKOvz31vX04nKgMF443Ut7b6vCkcFw319eNqUxcS-n0LBFu9uBiLqBYERGODJLftjKKRiyLIGMBrJRdFFVDU_NZrmqWrVv6tQw__vnd_LrUxKrP9f9SS1QMSynmYnEO0U2qQ2pPifcBb_DP-7by9M3SqSN9bq8d47mz_STQRlTiHIwzRrgPssQHluEosuB4CAvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=md4BjzMZr9oZGlTlcxd4XbosuSYXTuF3_RB9_hxdj5X3BE7C-625DoFD8P6JUZjYcdhSX1V7rXd3FPluWBb-O3Qwxcks04IGLZC03MzmEJs0734RIDWz737Ww-TD5u099vWTwPdDgHhEi1o63wRrKOvz31vX04nKgMF443Ut7b6vCkcFw319eNqUxcS-n0LBFu9uBiLqBYERGODJLftjKKRiyLIGMBrJRdFFVDU_NZrmqWrVv6tQw__vnd_LrUxKrP9f9SS1QMSynmYnEO0U2qQ2pPifcBb_DP-7by9M3SqSN9bq8d47mz_STQRlTiHIwzRrgPssQHluEosuB4CAvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظات من الصلاة على جثمان "شهيد إيران" والمرجع الأعلى للشيعة في العالم، سماحة آية الله العظمى السيد علي الحسيني الخامنئي، من قبل آية الله الحاج السيد مصطفى الحسيني الخامنئي.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/naya_foriraq/82244" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82243">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سماع انفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/naya_foriraq/82243" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82242">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عدوان على الأهواز</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/naya_foriraq/82242" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82241">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799e0dcd32.mp4?token=vaU8dSVyTZLES9_Xsmy1mk_qt0vJ2hy7lhC6C4k9Z0g4vczJ92bie05LqszsnmGFE98qOYUpUJi_1pkpIEThWEjJFY_I_xP5tiVcEf34dqV0PI-Edm4kTguw5wvpV5tG1CecDqgi4FQ3kR-e88cslEKmg4hbWPoKnd3vFDYTxhAVXtjR9QL9jfl6T1hzG6WsZThd2xlM4tby7L0yj2u-cakFncN1OMlbOuZDOYWxyMfZZQI3TMQ2MrzQOtEQK6zZ6MXYuGiX1cS2Exks158TPoz7A9ff3tGMBOjec8pmjVXTpf-kl5qNUxrE7jqOkdIUjMR6KXpd-p4AVXlWEhi7gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799e0dcd32.mp4?token=vaU8dSVyTZLES9_Xsmy1mk_qt0vJ2hy7lhC6C4k9Z0g4vczJ92bie05LqszsnmGFE98qOYUpUJi_1pkpIEThWEjJFY_I_xP5tiVcEf34dqV0PI-Edm4kTguw5wvpV5tG1CecDqgi4FQ3kR-e88cslEKmg4hbWPoKnd3vFDYTxhAVXtjR9QL9jfl6T1hzG6WsZThd2xlM4tby7L0yj2u-cakFncN1OMlbOuZDOYWxyMfZZQI3TMQ2MrzQOtEQK6zZ6MXYuGiX1cS2Exks158TPoz7A9ff3tGMBOjec8pmjVXTpf-kl5qNUxrE7jqOkdIUjMR6KXpd-p4AVXlWEhi7gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران في مدينة كنارك الإيرانية</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/naya_foriraq/82241" target="_blank">📅 21:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82239">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تفعيل الدفاعات الجوية في بوشهر الآن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/82239" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82238">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية في شابهار وسيستان وبلوشستان إيران</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/82238" target="_blank">📅 21:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82237">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية في شابهار وسيستان وبلوشستان إيران</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/82237" target="_blank">📅 21:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82236">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية في شابهار وسيستان وبلوشستان إيران</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/82236" target="_blank">📅 21:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb7818d5a.mp4?token=Gh4loOcnpxZZGDJ3qM0vZ3vYlx0iQewK8t9bRnturJrqFT0dHQFZ8jds7Vng_Lk-jv_75O7zI_ylLX5aQ1H08Gf7JHK1345G44uBNYIjILV5598Z2UqZMbFf-WDebCzJHNg6B2VQpVtK215hhhYHelxa7oR8vpNlbs06aP28wasNvdvNX8jgM7mPqzpr2t6Q1U3xZhpJgCBf1ee8nWSxQBABpUexAJ3a1zprsVIXbJMI_vnHmkFXbJHkI8_hV_rpyD6rWRvihD6Sr-m3n6teAGY8VrPxyMFklWhSqDmnEsjqLBRFn4IYPSgSh6VqSxFl6bLZBKciuYxppGk-9dURwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb7818d5a.mp4?token=Gh4loOcnpxZZGDJ3qM0vZ3vYlx0iQewK8t9bRnturJrqFT0dHQFZ8jds7Vng_Lk-jv_75O7zI_ylLX5aQ1H08Gf7JHK1345G44uBNYIjILV5598Z2UqZMbFf-WDebCzJHNg6B2VQpVtK215hhhYHelxa7oR8vpNlbs06aP28wasNvdvNX8jgM7mPqzpr2t6Q1U3xZhpJgCBf1ee8nWSxQBABpUexAJ3a1zprsVIXbJMI_vnHmkFXbJHkI8_hV_rpyD6rWRvihD6Sr-m3n6teAGY8VrPxyMFklWhSqDmnEsjqLBRFn4IYPSgSh6VqSxFl6bLZBKciuYxppGk-9dURwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مديرية الإعلام في الحشد الشعبي:
ويأتي الشكر، من حيث ينبغي أن يبدأ، إلى القائد المشرف ميدانياً على الجزء الأكبر من هذا الحدث، رئيس أركان هيئة الحشد الشعبي أبو فدك، الذي كان حاضراً في الميدان طوال ساعات العمل، يتابع التفاصيل لحظةً بلحظة، ويقود الجهد التنظيمي والأمني كما تُقاد المهام الكبرى، حتى اكتملت هذه المراسم بالصورة التي تليق بعظمة المناسبة.
كما نتقدم بعظيم الامتنان إلى رئيس هيئة الحشد الشعبي الأستاذ فالح الفياض، وإلى جميع قادة العمليات ومديري المديريات ومنتسبي هيئة الحشد الشعبي، الذين واصلوا الليل بالنهار لأيام طويلة، وسخروا جميع الإمكانات الأمنية واللوجستية والخدمية، وفاءً لواجبهم الوطني والأخلاقي، وإيماناً منهم بأن خدمة هذا الحدث مسؤولية تاريخية قبل أن تكون مهمة وظيفية.
وأخيراً، فإنني أعتذر لكل الشخصيات والمؤسسات والمديريات والكوادر التي لم تُذكر أسماؤها في هذا البيان، ليس انتقاصاً من دورها أو غفلةً عن فضلها، وإنما خشية الإطالة، أو بسبب الإرهاق الذي رافق أيام العمل المتواصل. فلكل من أسهم، صغيراً كان أم كبيراً، بصمة ستبقى محفورة في ذاكرة هذا اليوم التاريخي، وسيظل العراق يعتز بما قدّمه أبناؤه من صورة مشرّفة في الوفاء والتنظيم والانتماء.
﻿</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/82235" target="_blank">📅 21:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
مديرية الإعلام في الحشد الشعبي:
نخص بالشكر المدونين والمؤثرين في شبكات التواصل الاجتماعي، الذين كان لهم دور بارز في إيصال رسالة هذا الحدث التاريخي إلى العالم، إذ حققت المواد الإعلامية الخاصة بالمراسم عبر مختلف المنصات مئات الملايين من المشاهدات والتفاعلات، لتؤكد الحضور الاستثنائي لهذا الحدث في الفضاء الرقمي، وتعكس صورة مشرقة عن وفاء العراقيين وعظمة هذه المناسبة.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82234" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82233">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c8950292.mp4?token=WVsyYIy5bm5-dMIl9RFCSmh9q2CxI4jvrNeLnwW5u32eEch1k3Zfy-t37gljzi_jMnmaV_kugiCQehNO-Dw9wnSvVaOWoRSwdMMzlp9RwTiHtkOnSS8a_gx3IzUCT_g6oHF1YuHhk3VN0RN2E12E68Wt0fPB4vuclE3UtozZpXfLEzGqTZspqds8BNrvHp4O4NCywQKX8oKTxXiVE2wvKK1XSjllh8kJ8ruQxB8ouNzGZxUE46P5JNMF9y8KkHPK64Atyz3SXkvA8DOq-Ulaln-HaU5bxbcskBGBUVvMpUFX7IFkEmnbdV2-7lmOW98sAHA8UyM6LDH95fZVCgW-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c8950292.mp4?token=WVsyYIy5bm5-dMIl9RFCSmh9q2CxI4jvrNeLnwW5u32eEch1k3Zfy-t37gljzi_jMnmaV_kugiCQehNO-Dw9wnSvVaOWoRSwdMMzlp9RwTiHtkOnSS8a_gx3IzUCT_g6oHF1YuHhk3VN0RN2E12E68Wt0fPB4vuclE3UtozZpXfLEzGqTZspqds8BNrvHp4O4NCywQKX8oKTxXiVE2wvKK1XSjllh8kJ8ruQxB8ouNzGZxUE46P5JNMF9y8KkHPK64Atyz3SXkvA8DOq-Ulaln-HaU5bxbcskBGBUVvMpUFX7IFkEmnbdV2-7lmOW98sAHA8UyM6LDH95fZVCgW-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحضير مكان دفن جثمان الشهيد السيد علي الخامنئي في حرم الإمام الرضا (عليه السلام).</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/82233" target="_blank">📅 21:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82232">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">على الرغم من رفض نتنياهو للانسحاب
‏مسؤول أميركي: سيتم تحديد أول منطقة تجريبية تنسحب منها إسرائيل من لبنان خلال أيام</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/82232" target="_blank">📅 21:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82231">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">كان العبرية: في إسرائيل، يُعتقد أن الاشتباكات بين إيران والولايات المتحدة ستستمر في الأيام القادمة في الوقت الحالي، يتعلق الأمر بصراع بين الولايات المتحدة وإيران، دون تدخل إسرائيلي ومع ذلك، على الرغم من ذلك، فإن كبار المسؤولين في إسرائيل كانوا يرغبون في الحصول على موافقة من ترامب لشن هجمات إسرائيلية بمفرده</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/82231" target="_blank">📅 20:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82230">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">لقطات متنوعة عراقية حشداوية
من تشيع السيد القائد الخامنئي بين كربلاء المقدسة والنجف الأشرف</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/82230" target="_blank">📅 20:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82229">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔻
نائب العمليات في منظمة الإطفاء في زنجان الإيرانية: نفي وقوع انفجار في زنجان ومصدر الدخان ناتج عن حريق في ورشة إعادة تدوير.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/82229" target="_blank">📅 20:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82228">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مسؤول أميركي: الصواريخ والمسيّرات الإيرانية لم تسبب أضرارا جسيمة
أمريكا تتملص من الرد بحجة الأضرار غير جسيمة</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/82228" target="_blank">📅 19:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82227">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">"سي ان ان" عن مصادر: قطر وباكستان تعملان على إعادة أميركا وإيران إلى طاولة المفاوضات</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/82227" target="_blank">📅 19:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82226">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اسماعيل بقائي: ‏
سافر الرسول من بلاد فارس إلى خراسان عن طريق السفينة.
‏إذا فاضت عيناي بالدموع خلفها،
‏صرخةٌ ينبغي أن أكتبها على شكل وداعك
‏فليخرج صراخ من قلب كل من يقرأه.
‏سعدي
‏اليوم، تُودّع إيران شهيدها إلى مثواه الأخير، وتُسلمه إلى علي بن موسى الرضا (عليه السلام). إن جسد رجل عظيم يقع على أكتاف شعبٍ دافع عن هذه الأرض لسنواتٍ طويلة في وجه تقلبات الأحداث، وحافظ على وحدتها وقوتها في وجه كل أنواع الاضطرابات، ثم سعى إلى الشهادة في سبيل الله، ونال هذه الرحيلة المجيدة.
‏طويل القامة، كشجرة السرو الإيرانية، يستمتع دائماً بشمس المقاومة والمثابرة، وقامته، كظل ثابت، امتدت فوق هذه الأرض؛ أصبح "السيد الوطني" في النهاية "نار إيران".
‏في ثقافتنا الإسلامية، لا تُعدّ الشهادة نهايةً للحياة، بل بدايةً لحياةٍ أخرى؛ إنها تحررٌ من ضيق الدنيا وانضمامٌ إلى رحابة القرب الإلهي. فمن منظور هذا المذهب، لا يغيب الشهيد عن الدنيا، بل هو حيٌّ بفضل وعد الله، ويرزقه ربه. لذا، فالشهادة ليست نهاية المجاهد، بل هي ذروة مسيرته ولحظة لقائه بالحبيب الأبدي.
‏إن قافلة الشهداء، من كربلاء إلى يومنا هذا، هي خيط لا ينقطع في تاريخ الإيمان والسعي وراء الشرف؛ خيط كل حلقة فيه هي استمرار لنفس الطريق الأحمر ونفس العهد الأبدي مع الحقيقة، "الذي لا يبايعه أحد مثله".
‏في عيون العثّات العمياء، يمكن إلقاء رجال الله في التراب، ولكن في عيون رجال الله، جسدهم وروحهم كالبخور الذي تفوح منه رائحة شهية من لهيب الاستشهاد:
‏قال المفرقع سراً للدخان
‏قلبي لا ينبض وأنا سعيد بالعودة.
‏أتمنى أن يدرك قيمتي وأن يكون ممتناً لي.
‏رأى كاندير في هلاكه عودة للربح.
‏كان العود مربوطاً بعقد من رأسه إلى أخمص قدميه.
‏تم فتح باب الغياب لتلك العقود.
‏أهلاً وسهلاً بك يا صديقي آكل اللهب.
‏يا أيها الفاني، يا شهيدي، يا الشاهد الفخور!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/82226" target="_blank">📅 19:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82225">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">#ترفيهي
‏بيان لدول مجلس التعاون الخليجي: ‏أي اعتداء على أي دولة في المجلس هو اعتداء مباشر على كافة دول الخليج</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/82225" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82224">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بدأ نقل جثمان قائد الثورة الشهيد إلى حرم الإمام الرضا (ع) لإقامة صلاة الجنازة والدفن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/82224" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82222">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHXHSbAjBlIHVatLNQmOispV_hTvCi-v1fuBF9-31FWpw7NVy9RPwAs51eW3i_4I8Ju0c-s2yB7ynjr90cOhDGVddgWKhRNCo-qAwv41G3qps3FYqjiwTRS_9c70kguNW3Mr_vvnymcDrElOQmtK39FpjedusbHhheDXUxnIMJXXddhXbUkVMAbPxOJfoTo0aapo_62j8ZezHyoQhZRqPkMGnmmFFXicTDPrtYv9mFa0_PathX-ImjpnJnrHU_nd7yOSQyDv74xodnN1g5x8IET8oRhCpRakMIthsd7rr1Ss34RC2AQGboMyw6ZW_NBdDiSHO4pb9bd_p8JHoXYWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZIdfN-hh2z335QNV99NP0qOvHaVs4g2Nz4Yjymv7sZIVKGsNMYXGx7fhl9IuFP33o_jhJnh4i6LkEQtyK0eXZvCljecfGf2dBwVeRchWxnbsu6r4Xv-zMcEa65KYQoH00BwIHs2YKUFd8Fw_BFmhtolm2jDU7yuNvun23F-77efhXJd6-CSI6sHVUrkhom7b12krpcP5wZP0bHKWLkdeBHmWty9TrugZ3pDOy4K-trNqn4KZCPX9J1F39gM7pqCfgJqg-VJ_GamspxUezei9eWFVbNQUqQUySzBhQwdW0EeugTxU48M6diqaM6r6e5I59jiiJfdiIQSF1IuE7b4dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طيران التزويد بالوقود الأمريكي ينشط في سماء الأردن هذه اللحظات</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/82222" target="_blank">📅 18:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82221">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
نتنياهو: لو لم نتحرك لكانت إيران قد امتلكت أسلحة نووية والحرب لم تنته بعد وتحديات جديدة تبرز أمامنا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82221" target="_blank">📅 18:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82220">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE3eq926KbN_c86gWUoBUKwIcLVhk5BJWG4nceNUVjeYH_FmcujSCQLDcycWQw2bFUH8t9rT9ySF7uSodSQ2z3QlsyawnSyLT5H655dSQ9oQn6Dcu1RRqhOMfm07GTxoxtvlm_E-9F_9NU_35rdEEkcM1qnvD7feZY3vd_HibF7BtigMowJasqpZfOZYG_G3RxqV19qJZkHIoilhAz4AIdsV2EGumBkq9c_uGIsfche4wdC3xHGeH5WSBFRLnTrQ0AHRIDkAvIXGR3lIYfpxUaMGkkEaGjJzckUotusvuyvwo20359ZdQS3sq6yDXOIJaK5JoPsldaU2N_X2d9lZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران التزويد بالوقود الأمريكي ينشط في سماء الأردن هذه اللحظات</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/82220" target="_blank">📅 18:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82219">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-vV9s6MObyJlbX4gM8J80plxWqaA0nrSZxFa0BIWdGOihFNKBY0reLl7dyK2IOvG4L9qZKzRnb5Zuo1b-Tt0BMXdO85nbriXXxbwvZlTpabZvHxYnAzT5PH9nlSkVFZ9hqO4rTKea7Jf85iZDuJgwN6ZL_z5jUM4y_yPu4qPY6BNWhpd96atvsr4Iy_HShrrT_FaDIVx2v3vVzFm9PUI7E_hd-92tV8fmFUckkOao6l7nb34XUdNY7zCIVhdkdpC9szobizPf4rDz2DcYEyfmBLagJOUGUpyZoY7yotC1qidjJL50AQ6MY9EEb_3XeJBj9rUTava7nAN3ZPSCW2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحاج ابو فدك المحمداوي في الصف الأول يتصدر جموع المشيعين في مشهد المقدسة</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82219" target="_blank">📅 18:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82218">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏وزير دفاع الاحتلال برسالة لـ إيران: جيشنا في حالة تأهب واستعداد لاستئناف المعركة</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/82218" target="_blank">📅 18:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82217">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بدأ نقل جثمان قائد الثورة الشهيد إلى حرم الإمام الرضا (ع) لإقامة صلاة الجنازة والدفن</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82217" target="_blank">📅 18:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82216">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزارة الخارجية العراقية: وفاة أحد الصيادين العراقيين الذين تم اعتقالهم من قبل خفر السواحل الكويتي.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82216" target="_blank">📅 18:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82215">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزير الخارجية الايراني لقائد الجيش الباكستاني: من حق إيران الدفاع عن نفسها ضد أي مغامرات أخرى من جانب الجيش الأمريكي</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82215" target="_blank">📅 18:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82214">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية: العراق سيأخذ من شركة ستارلينك 9% من واردات الشركة 8% مباشر و1% للخدمة الشاملة الى جانب 15% الضريبة المفروضة على شركات الاتصالات</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/82214" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82213">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية: العراق سيأخذ من شركة ستارلينك 9% من واردات الشركة 8% مباشر و1% للخدمة الشاملة الى جانب 15% الضريبة المفروضة على شركات الاتصالات</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82213" target="_blank">📅 18:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82212">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية:
العراق سيأخذ من شركة ستارلينك 9% من واردات الشركة 8% مباشر و1% للخدمة الشاملة الى جانب 15% الضريبة المفروضة على شركات الاتصالات</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/82212" target="_blank">📅 18:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82211">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
القائم بالاعمال الامريكي في بغداد:
نتشاور مع الحكومة العراقية لدعم خيارات العراق لبناء المرونة فيما يتعلق بإنتاج الكهرباء على المدى القصير.
لعد جنرال الكتريك شجانت تسوي من 2003 ولليوم ، يومية موقعين عقد وياها وضخ فلوس ونفس الطاس ونفس الحمام
😄</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/82211" target="_blank">📅 17:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82210">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb52071cdf.mp4?token=Tp9PmfBEAyD7gce5cUKbukjj21nFXDp1P4OW7agDFs06b0sQszuqgTUj2kdAwSb8aJi-wMe6BVRHhUnllBEskY400V-DW3f1x_bji0xczT9oc1LjCMZ2Aq6qPsFIKTiHsOYQHtV6f6xaPtLy0NjByW68uRGWlbjFcCqf4qpkmxMbisXf85A6u-b5hgxOvd4u2DT6-15-rn2Xk-JdHfxheUIkMr2p5XImhfrs4yulai-NXcj333Ms2kR8aay0oemPLuGsDingNA303ncD0NdIf0Fx239vekINNVBGD-lLgU6lZI4caoxvggBtA8LOvXcueM329MQFxqTxkh745qtAnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb52071cdf.mp4?token=Tp9PmfBEAyD7gce5cUKbukjj21nFXDp1P4OW7agDFs06b0sQszuqgTUj2kdAwSb8aJi-wMe6BVRHhUnllBEskY400V-DW3f1x_bji0xczT9oc1LjCMZ2Aq6qPsFIKTiHsOYQHtV6f6xaPtLy0NjByW68uRGWlbjFcCqf4qpkmxMbisXf85A6u-b5hgxOvd4u2DT6-15-rn2Xk-JdHfxheUIkMr2p5XImhfrs4yulai-NXcj333Ms2kR8aay0oemPLuGsDingNA303ncD0NdIf0Fx239vekINNVBGD-lLgU6lZI4caoxvggBtA8LOvXcueM329MQFxqTxkh745qtAnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔰
كما قال الشيخ أكرم الكعبي: سلاحنا وديعةُ الإمام الحجة (عج) وقد تجلت آثار هذه الوديعة في مشهد الوفاء المليوني الذي شهدته النجف في وداع الإمام الخامنئي (رض)
#قوموا_لله
#كونوا_احرارا
ً</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/82210" target="_blank">📅 17:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82209">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏وزير الطاقة التركي: نخطط لتوقيع اتفاقية مع العراق بشأن خط أنابيب لاستمرار تصدير النفط لـ12 شهر اخرى.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/82209" target="_blank">📅 17:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82208">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مطار النجف الاشرف الدولي يعود للعمل امام الرحلات التجارية بعد الإغلاق المؤقت</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82208" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82207">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
بيان لحرس الثورة الاسلامية:
بسم
الله
قاصم
الجبارين
«
فَمَنِ
اعْتَدَىٰ
عَلَيْكُمْ
فَاعْتَدُوا
عَلَيْهِ
بِمِثْلِ
مَا
اعْتَدَىٰ
عَلَيْكُمْ
»
لقد ذكرنا في البيان السابق أن تكرار العدوان سيوسع نطاق ردنا ليشمل قواعد العدو الأخرى في المنطقة، وفي المرحلة الثانية من الرد على اعتداءات الجيش الأمريكي القاتل للأطفال، قمنا بتحويل هذا التهديد إلى فعل
دكّ مقاتلو القوة الجوفضائية التابعة للحرس الثوري في تمام الساعة 14:20 من بعد ظهر اليوم مركز قيادة وسيطرة العدو في غرب آسيا وقاعدة العدو الجوية في الأزرق بالأردن بـ 10 صواريخ باليستية
في حال تكرار عدوان الجيش الأمريكي الإرهابي، لن تكون بقية القواعد الأمريكية في المنطقة في مأمن من نيراننا الكثيفة
وما
النصر
إلا
من
عند
الله
العزيز
الحكيم</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/82207" target="_blank">📅 16:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643cebc914.mp4?token=PoiANIvnCJDdPUqzZemBy4ByHugCSKSBoXPXu_Aufc0oB499Yut855Z7ssj8-G-KuXSIUwIvudTZd68LPsi0ms9Gt3gX37MDiTl_Q8hZRuHwa0kB52UFB0qfX8LLdoMRF6I6rcf783sWhGemKrCfJKFNrYIQn899CuzLNMXid2VvYSTC2lE6Q9hwXO4iFdQb2uf1AdFiHTHz4GbrxPUtPVcAiXLqYIazQK0UICNeEPrEMdWsEHdCEYgSTF0xTzAoWhjY3NfimozuCBs8q5NixY5AqfjnYRHuL7sMk_6Z-FDNJBaJJUnmlMKHBV3Bir3K_FFtDOETnWyGjQ6xsmFTwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643cebc914.mp4?token=PoiANIvnCJDdPUqzZemBy4ByHugCSKSBoXPXu_Aufc0oB499Yut855Z7ssj8-G-KuXSIUwIvudTZd68LPsi0ms9Gt3gX37MDiTl_Q8hZRuHwa0kB52UFB0qfX8LLdoMRF6I6rcf783sWhGemKrCfJKFNrYIQn899CuzLNMXid2VvYSTC2lE6Q9hwXO4iFdQb2uf1AdFiHTHz4GbrxPUtPVcAiXLqYIazQK0UICNeEPrEMdWsEHdCEYgSTF0xTzAoWhjY3NfimozuCBs8q5NixY5AqfjnYRHuL7sMk_6Z-FDNJBaJJUnmlMKHBV3Bir3K_FFtDOETnWyGjQ6xsmFTwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
لحظة تدمير طائرة MQ9 الامريكية بواسطة الدفاع الجوي الايراني.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/82206" target="_blank">📅 16:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇩🇿
شركة سوناطراك الجزائرية: حادث في مصفاة أرزيو.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/82205" target="_blank">📅 16:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">قطر توقف زيادة إنتاج الغاز الطبيعي المسال بعد الهجوم على ناقلة النفط في مضيق هرمز</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/82204" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82203">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
قائد مقر خاتم الانبياء المركزي:
هذا الحزن والغضب سيستمران في طريق الثأر لقتلة القائد الشهيد، القوات المسلحة ستعمل، بدعم الله والشعوب المسلمة، على محاسبة منفذي ما وصفها بالجرائم الإرهابية</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/82203" target="_blank">📅 16:12 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
