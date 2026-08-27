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
<img src="https://cdn4.telesco.pe/file/GeTB2c5Is2Ktf6albDP-GXldD8WbLb7pkPpkm48tpTFsZvWRYDsUOBkBoNeuTxnz9DyBJzxfSpvs0BctmDcXrx2q-wO8iCGDsxxjrTHthSwTgyIZkKmPc1fT7_PhN9kfWb-dJShCAgUVgx2AO-xEl6CYi5Sv4dOZc0eJGKzIsHntDFLb7yorEbC4UXNg5AAZt5O5wVZ2vcqrh7_f1wG85ASDe5xt6vaL2kLRIop0lgOxVGeA-YBK39sOWXZA6ZJLwMh2KuIBzUMJz3bSSj30fndVHieUGtIu_N04HqAHCC0AaWkvePpyJyt8BQ_eTYH9i7xjtN9WTw9s5hwN2Y29QQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 269K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 09:25:37</div>
<hr>

<div class="tg-post" id="msg-88607">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇷🇺
🇩🇪
دير شبيغل الألمانية
:
‏يُعتبر حزب البديل من أجل ألمانيا، بقيادة المرشح أولريش سيغموند، حزباً موالياً لروسيا بشكل خاص. وفي حال وصوله إلى منصب رئيس الوزراء، قد يتمكن بوتين من الوصول إلى معلومات حساسة للغاية عن الدولة. وهناك بالفعل مؤشرات أولية على ذلك.</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/naya_foriraq/88607" target="_blank">📅 09:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88606">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇰🇵
‏
كوريا الديمقراطية:
العداء الأميركي المستمر تجاهنا بات واضحا.
سنرد بسرعة وحسم على الأفعال العدائية.
ندين خطوة الولايات المتحدة لتزويد كوريا الجنوبية بالأسلحة.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/naya_foriraq/88606" target="_blank">📅 08:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88605">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم روسي بالطائرات المسيرة الإنقضاضية يستهدف مصانع أوكرانية في العاصمة كييف والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/naya_foriraq/88605" target="_blank">📅 08:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88604">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الله اكبر
هجوم على سفينة قبالة سواحل عمان منطقة خصب بطائرة مسيرة …</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/naya_foriraq/88604" target="_blank">📅 04:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88603">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
🌟
لقطات جديدة من حرب رمضان تُظهر لحظة الإغارة على جسر B1 في كاراج الإيرانية من قبل الطيران الصهيوأميركي.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88603" target="_blank">📅 02:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88602">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f0f8deda.mp4?token=jqnjJ2QLO7wpM2I3UDwIQYX73dhVuFTXEnFxjLHIUMRvuMQVqJualnedjjFNtgq1n23tblQ0Ib9v5HQfRbr5LbnvoqKYutIFfJmFfneSKzcdnitlwC3L439u6_xFGuXhchtpkxgECuaporvUMJYEMLKhQW3ftb-_RGF6_qQ1_ZEdjZdFa4J3n75vX51eGssJVe2dNG14oUS9q-gjNEGq4LdK0qidUTPAbotavXHMaUq8YzBhGmEAhn4QwWMJzjU7oqOKKE6imRIXrLFUCxPDRw4E2xlTWfJov_zjXM9jlqF8nfA9LJxhPuN7ulBByRhE6ZIrEnirTG9IKJDiegxD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f0f8deda.mp4?token=jqnjJ2QLO7wpM2I3UDwIQYX73dhVuFTXEnFxjLHIUMRvuMQVqJualnedjjFNtgq1n23tblQ0Ib9v5HQfRbr5LbnvoqKYutIFfJmFfneSKzcdnitlwC3L439u6_xFGuXhchtpkxgECuaporvUMJYEMLKhQW3ftb-_RGF6_qQ1_ZEdjZdFa4J3n75vX51eGssJVe2dNG14oUS9q-gjNEGq4LdK0qidUTPAbotavXHMaUq8YzBhGmEAhn4QwWMJzjU7oqOKKE6imRIXrLFUCxPDRw4E2xlTWfJov_zjXM9jlqF8nfA9LJxhPuN7ulBByRhE6ZIrEnirTG9IKJDiegxD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
توثيق أخر يظهر لحظة إسقاط الطائرة المعادية في سماء محافظة إب اليمنية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88602" target="_blank">📅 00:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e7b3f02f.mp4?token=tJAMEkqy3fOE__3Jf8y_TMFatdQWmq_SiQRJWAzYGkNmr646Yoyl0OB_noy-j7GJC-97OK2YqTTLq4gPNxj4fs11IqxYZuSltFD0Z50u2KlW2ysmp5q6vz5LwK0oZqhtaPlL6k4jJSvOBwWHPsBzr8z42DA1P6Qp5xFCy-ySIRvD8pj7TW7Wjo4mbbZCRwrqUyNEJAuGh58dH_hzIGnn-_Fm-6Ap3qOpUWm8wA0VtMMWVo4_Du6Xko6PnTTzhodSJo-l87CXfDZ3p7TVRFRsKO5f-QjvJArMRjUUpSyCvpbuTcKBmtZfux6RDCPPArrL4rbZSJuI9vPvjtRxCE04TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e7b3f02f.mp4?token=tJAMEkqy3fOE__3Jf8y_TMFatdQWmq_SiQRJWAzYGkNmr646Yoyl0OB_noy-j7GJC-97OK2YqTTLq4gPNxj4fs11IqxYZuSltFD0Z50u2KlW2ysmp5q6vz5LwK0oZqhtaPlL6k4jJSvOBwWHPsBzr8z42DA1P6Qp5xFCy-ySIRvD8pj7TW7Wjo4mbbZCRwrqUyNEJAuGh58dH_hzIGnn-_Fm-6Ap3qOpUWm8wA0VtMMWVo4_Du6Xko6PnTTzhodSJo-l87CXfDZ3p7TVRFRsKO5f-QjvJArMRjUUpSyCvpbuTcKBmtZfux6RDCPPArrL4rbZSJuI9vPvjtRxCE04TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد من إسقاط طائرة تجسسية معادية في أجواء مدينة إب اليمنية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88600" target="_blank">📅 00:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88599">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
طيران حربي كثيف يحلق فوق محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88599" target="_blank">📅 00:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88597">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6627f1fd9.mp4?token=ozTx3Ob2w0cgf3Ec_22lWp3l012cPIrWr27arNaODShlrUafLP5RH8Xx5wSisf8XZWkd15BjgL-A1ii6IllnBEcfAKVi-O9IjrpRp5MtOeCbU4jDQkvJQi6_vpshvlOuE8ZlBcSy0uf5iyAvrwDSHgCuXtHWjUNaYnLzY-0apL0UVCN1ouzPRZKAHlxsXFXk7XZXg3XhsQkiUuawPRsn9a7nKf5PM8KREbvOArRw_tYZLbSuFsHC1qvkNV4LnnHp4iSu4jq1ev0uqf48vN5QVJsGwT6_Vf5XX9NErIMSNWUQU96B0qQR6btCnm9tUSN1uCUHJZ9gidUNqpTK3ddiRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6627f1fd9.mp4?token=ozTx3Ob2w0cgf3Ec_22lWp3l012cPIrWr27arNaODShlrUafLP5RH8Xx5wSisf8XZWkd15BjgL-A1ii6IllnBEcfAKVi-O9IjrpRp5MtOeCbU4jDQkvJQi6_vpshvlOuE8ZlBcSy0uf5iyAvrwDSHgCuXtHWjUNaYnLzY-0apL0UVCN1ouzPRZKAHlxsXFXk7XZXg3XhsQkiUuawPRsn9a7nKf5PM8KREbvOArRw_tYZLbSuFsHC1qvkNV4LnnHp4iSu4jq1ev0uqf48vN5QVJsGwT6_Vf5XX9NErIMSNWUQU96B0qQR6btCnm9tUSN1uCUHJZ9gidUNqpTK3ddiRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پهپادی به مقرهای تروریست های تجزیه طلب در اربیل عراق.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88597" target="_blank">📅 00:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88596">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed70602e4e.mp4?token=TB0mzNG9Gh4qJqeN2roXCTtqshvUU8X10gY32F_MvaJr1100jNiVKV8U-xcVLIp-Nd9jpo1US890yseSU86FR_phn0N6w5xw5BeihLZUIsHm0Iw09OeTbkPamEO4qSm9XnYQTXgNWRTUf_UXJ2o_YLIB6KGtY5Gbuw06GuIVJEyq-Uulb7lV8-FKsH2cPV1uHvmamQbbJXXv9owYQrDxqY_uBejH_PtP2JFI99eOm3gomX2x18X4rr4FT4-ilzZLemueBsy2dVaomskE541wdjjq4EjHApq72bjzCCdLhUPkxpLALhttV9Jv6ezmYJmkQvbZbZJRutUTlaOqD9XWyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed70602e4e.mp4?token=TB0mzNG9Gh4qJqeN2roXCTtqshvUU8X10gY32F_MvaJr1100jNiVKV8U-xcVLIp-Nd9jpo1US890yseSU86FR_phn0N6w5xw5BeihLZUIsHm0Iw09OeTbkPamEO4qSm9XnYQTXgNWRTUf_UXJ2o_YLIB6KGtY5Gbuw06GuIVJEyq-Uulb7lV8-FKsH2cPV1uHvmamQbbJXXv9owYQrDxqY_uBejH_PtP2JFI99eOm3gomX2x18X4rr4FT4-ilzZLemueBsy2dVaomskE541wdjjq4EjHApq72bjzCCdLhUPkxpLALhttV9Jv6ezmYJmkQvbZbZJRutUTlaOqD9XWyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پهپادی به مقرهای تروریست های تجزیه طلب در اربیل عراق.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/88596" target="_blank">📅 00:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88595">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d599cf5e06.mp4?token=FPwmZ2BzZzF-GMZEFmqzyAL-RrfCHtZsc_WjXdaxF9YcdKer7BV-iJHHzeddurjXNpVTs8KKaszFqYz-tITr2viFCakkMjYKq0wU_7xWdgsbuU91zSwQ45Vt9YMU9Ttva0U14lWdEXl9Mo1HwxRzjUYsTXBtPSQ6P52SapKv9eim7wTau8ls6sLDPIPa8FS2ldDdMM04TT86S-2qAkd8ueg5Ulp0DSZLTrzCX7yxauLkZJmo9xQli6j6gy90AXdLThEVpaqBPCGDBuqAmDXyV1zoa0QKhbod13Yfe0rs80hlPKViekDjQTpyuNjBWfhOR4PbysOZE7XLDhcV74olhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d599cf5e06.mp4?token=FPwmZ2BzZzF-GMZEFmqzyAL-RrfCHtZsc_WjXdaxF9YcdKer7BV-iJHHzeddurjXNpVTs8KKaszFqYz-tITr2viFCakkMjYKq0wU_7xWdgsbuU91zSwQ45Vt9YMU9Ttva0U14lWdEXl9Mo1HwxRzjUYsTXBtPSQ6P52SapKv9eim7wTau8ls6sLDPIPa8FS2ldDdMM04TT86S-2qAkd8ueg5Ulp0DSZLTrzCX7yxauLkZJmo9xQli6j6gy90AXdLThEVpaqBPCGDBuqAmDXyV1zoa0QKhbod13Yfe0rs80hlPKViekDjQTpyuNjBWfhOR4PbysOZE7XLDhcV74olhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقرات الكوملة واليجاك في قضاء سوران بمحافظة أربيل تتعرض لهجوم بالطيران المسير الإنتحاري والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/88595" target="_blank">📅 00:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88594">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f044086b32.mp4?token=XDxxCzmWv0AOMBHOvW7RkKL5hZ2rUscTvELjVPvh3lJjQafkds3CpA9uWXaO9c5fRR1QOzgrPSCh_UyPRSwGP03CohAdQS1bnRtFIxL-p9K3E5iBtIH7wVqWD9DNZEi7y3HmtGT_HKKhJOyzmOhKH1p2xdc58PQMi0YPq78OO2Hke_vESwswUZSD9GHj47bghXOQ_9LbbhUSffyJ1qPnLk1ON5YVmGzAviGxz6NB-2IJ9u-fLCrZJcpanLN0FMlJCE9hxxsnxGXWGYpZ3zM0h1tgdCC_-V-7LKT4qUJIwFqJGsh8Vc3v_BnolPTDJUQHJ8px7JLxPEplLfLXz0Vkfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f044086b32.mp4?token=XDxxCzmWv0AOMBHOvW7RkKL5hZ2rUscTvELjVPvh3lJjQafkds3CpA9uWXaO9c5fRR1QOzgrPSCh_UyPRSwGP03CohAdQS1bnRtFIxL-p9K3E5iBtIH7wVqWD9DNZEi7y3HmtGT_HKKhJOyzmOhKH1p2xdc58PQMi0YPq78OO2Hke_vESwswUZSD9GHj47bghXOQ_9LbbhUSffyJ1qPnLk1ON5YVmGzAviGxz6NB-2IJ9u-fLCrZJcpanLN0FMlJCE9hxxsnxGXWGYpZ3zM0h1tgdCC_-V-7LKT4qUJIwFqJGsh8Vc3v_BnolPTDJUQHJ8px7JLxPEplLfLXz0Vkfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالطيران المسير الإنتحاري يطال مقرات المعارضة الكردية في أربيل</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/88594" target="_blank">📅 00:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88593">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqfIuRQ1VPtoXYXYU_Ee9gAd-TBFORQXP2XHBCBxbUqmbBSyDNIMtaUnlj6bRI804RqEFf3zj83XNcPxzKBR_E7H99PopbhGoq2BOWA-Ds7LMvL-ys9h9SIyYtup6GTKGZUt6Sw_fRLe-l9lWukdtFZ_xoQyR6lGslD1Tb6kCtIxZuwekIOxNadnTWjcwzkwuJo5WNjnk-99h4kKj_FFLkuo16lvM1Ud_jxKOen5RszYoQQxbqH89kJd0dMXnyw0Fy0D4bsEGFfsVvUXMSL1f8um17rvNPnhvGBoLG-gzggKWSUlknoMlkxGyxw6BI9mX4jpbJd3156QXRrJAawBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد النيران واعمدة الدخان من مقرات الإنفصاليين في محافظة أربيل جراء استهدافهم بالطيران المسير الإنتحاري</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/88593" target="_blank">📅 00:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88592">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eff45189c.mp4?token=GDEOgqHDvf0Kz4c-l6lrmo3w5TcHBejyjkanlUcX0TmHvyWzg1ObvNsbODL5hEF5z2g3n5_9KvNJKkvdQBxkXa4FQvfzjnqhcvAytfiW1sgR0c0e-oLZ7s7yl9wLNucVD3oZG4MIwzgsI8CZerY6DPkSsrvfGUhTrxLgjAEgVYZwGrAOUm9aFO7iYnhIIlqjsCwJmqpToBjfUgVrZdg3OTRG5eB_wvVwoO5uYHCG56jPUDk_iQhDjIPiB_umckfKWap2CZ_2CnBHEN0HgSgpKWdM3gXKhk-k-PYVc_dBwC2D0sF4CfTsDGaxWqODeBuf8D3Fb902_hLTgXZPEQTWCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eff45189c.mp4?token=GDEOgqHDvf0Kz4c-l6lrmo3w5TcHBejyjkanlUcX0TmHvyWzg1ObvNsbODL5hEF5z2g3n5_9KvNJKkvdQBxkXa4FQvfzjnqhcvAytfiW1sgR0c0e-oLZ7s7yl9wLNucVD3oZG4MIwzgsI8CZerY6DPkSsrvfGUhTrxLgjAEgVYZwGrAOUm9aFO7iYnhIIlqjsCwJmqpToBjfUgVrZdg3OTRG5eB_wvVwoO5uYHCG56jPUDk_iQhDjIPiB_umckfKWap2CZ_2CnBHEN0HgSgpKWdM3gXKhk-k-PYVc_dBwC2D0sF4CfTsDGaxWqODeBuf8D3Fb902_hLTgXZPEQTWCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
دوي إنفجار عنيف في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/88592" target="_blank">📅 00:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88591">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKNirYUrU7MqpUSAY4zZ6yNkfk7Q9TCPOadBb3sWtO_pEPepJxyv-VpZT8VIBxX1g8K33397jIfCPRDgWa5bLJOrXG58Rn4NErNO2klzLINHwfsevArxOhp4s-tJ_hThCfyUAn0IGrbCJPsgAULO3bes_iFYeKUrWykjpoSuX_BH9wM-klrQFE3Mg_03C-yh-MHTghs95LjQj9oS-8bA9QKKaURJ8-AKcfmce2qNs0xvFiV_Rgl7j0vXcyK1NPZWktyv5QHgm22s-nBuEqZmA5fQz85qBcR1I5cX_j5xLi472Msq6x2kNXIPom6qUZ7u9M_KZ4L1Dlb0faYHMeDPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
دوي إنفجار عنيف في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/88591" target="_blank">📅 00:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88590">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇾🇪
الاستهدافات طالت ميناء المخا وبعض المواقع التي تتخذها المليشيات الموالية للسعودية ملاذا لهم.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/88590" target="_blank">📅 23:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88588">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc95e1665a.mp4?token=bz3vZvjjL4luf4QsodlUt9XX-SjuJJGD_aEwcTIZJnRvjGofKje0aE7638sty2VMbT_BBrWq_Sk3_RavgVz1RtmoABvxmS_-gUufv_M6lseqyPHErOdqRt50N0PpDhSzCfaasbWyPR9XCB-t3ilqqY_b6OiWMeMHw_ALxG3gZ_wtDKKZohXFuigcbMJIE_rZuxF8iBSr9Z_OknTttXs5K5h5FwRSC0DxsZbn4ktu79G7azDjudadhMLMFKaV8HO4OW56g9O_UBZHcGxRGl6-qHYL11Ps1iM-vjbRGA5mWvE6X3Zk6kstsV4T3cWdJy2hKdVv0eDo2Y-AwwvQW8zLpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc95e1665a.mp4?token=bz3vZvjjL4luf4QsodlUt9XX-SjuJJGD_aEwcTIZJnRvjGofKje0aE7638sty2VMbT_BBrWq_Sk3_RavgVz1RtmoABvxmS_-gUufv_M6lseqyPHErOdqRt50N0PpDhSzCfaasbWyPR9XCB-t3ilqqY_b6OiWMeMHw_ALxG3gZ_wtDKKZohXFuigcbMJIE_rZuxF8iBSr9Z_OknTttXs5K5h5FwRSC0DxsZbn4ktu79G7azDjudadhMLMFKaV8HO4OW56g9O_UBZHcGxRGl6-qHYL11Ps1iM-vjbRGA5mWvE6X3Zk6kstsV4T3cWdJy2hKdVv0eDo2Y-AwwvQW8zLpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
صواريخ انصار الله تستهدف المليشيات الموالية للسعودية في المخا.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88588" target="_blank">📅 23:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88587">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇾🇪
صواريخ انصار الله تستهدف المليشيات الموالية للسعودية في المخا.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/88587" target="_blank">📅 23:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88586">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
الاستخارة تقترح بابتعاد العامري و تجلب حظوظ للفريجي العائد بقوة والمبعد قصرًا من اخوة يوسف ، اخوة يوسف يلوحون بالاستقالة بعد عودة الفريجي من سرير الموت..الأخير أسم عابر لحزبه وصاحب علاقات إقليمية ومحلية تجعل اسمه ناقوس خطر على الجميع .. من جهة اخرى أربعة وكالات استخباراتية استلموا منصبهم في فترة الشمري سيتم تغيرهم ..</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88586" target="_blank">📅 23:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88585">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7f179854.mp4?token=kaLqQnofJ-2VMJd-shTceAtOR0aNLrefHsikdFCkUhdUM2c7ThsxL4F5l576TUwgFUNJdCiGIcgKBen_L6ciZEF7r-AbYxGCh5erhod2OJvTDCupUA5FxKOR96XqJ4bT0x3o58SoIMdJuyVSq0d8VWyX9D4duNEBsUE2kpST30nOiiWjWDzLXLeStYdWlbAqXitsm-8OrKtvvR_75xMIR_DIzpGpC14-Zm7xk81nCqsk1FFoOsqUn6xEKQCsMFuDWv9tg4QhLXZxgPf6BdP8vYmy7vPWgcR5AnIJpjNAF_05etTL5-RNY5EyOa1x3Hzcsz9_u4yrIzt1tf2yyurKgkOBQJrIEkKIcI1c4bJ0C6Y-46RTSHy4i6g6tuD76HyvArdXb4Md4kkFIlleQ5u8twYM9BMYXMMuNcH6bYcV6Kh4AfW02GukCImxkTFXcMAwSdwoeeYxGp294R-0M-jq8A_NHrg-HNGnAAPeXE4XMnERPOuJCyOdNVKjhPMgFFuPz8BEtqfJ1oANNxltEkqtpCb1RyIjwUAIdeqV_cp7HHWMKqspxHca4dSukVPfXI376u5GNipz870g0Xmt0bEyeh4sKbPTEdQGk7llWS2mAkJsMmmJocZP-1lWCpgh0WpuEkH7c2tBCeGEiZexBk-l37-5KQo1Sd8JZMc3Glsl1Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7f179854.mp4?token=kaLqQnofJ-2VMJd-shTceAtOR0aNLrefHsikdFCkUhdUM2c7ThsxL4F5l576TUwgFUNJdCiGIcgKBen_L6ciZEF7r-AbYxGCh5erhod2OJvTDCupUA5FxKOR96XqJ4bT0x3o58SoIMdJuyVSq0d8VWyX9D4duNEBsUE2kpST30nOiiWjWDzLXLeStYdWlbAqXitsm-8OrKtvvR_75xMIR_DIzpGpC14-Zm7xk81nCqsk1FFoOsqUn6xEKQCsMFuDWv9tg4QhLXZxgPf6BdP8vYmy7vPWgcR5AnIJpjNAF_05etTL5-RNY5EyOa1x3Hzcsz9_u4yrIzt1tf2yyurKgkOBQJrIEkKIcI1c4bJ0C6Y-46RTSHy4i6g6tuD76HyvArdXb4Md4kkFIlleQ5u8twYM9BMYXMMuNcH6bYcV6Kh4AfW02GukCImxkTFXcMAwSdwoeeYxGp294R-0M-jq8A_NHrg-HNGnAAPeXE4XMnERPOuJCyOdNVKjhPMgFFuPz8BEtqfJ1oANNxltEkqtpCb1RyIjwUAIdeqV_cp7HHWMKqspxHca4dSukVPfXI376u5GNipz870g0Xmt0bEyeh4sKbPTEdQGk7llWS2mAkJsMmmJocZP-1lWCpgh0WpuEkH7c2tBCeGEiZexBk-l37-5KQo1Sd8JZMc3Glsl1Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
" السالفة المحد يكدرلها الكتائب تسويها"
قليلة التداول جانب من اشتباكات ابناء العراق الغيارى من مسافة صفر في احد قواطع المسوولية للدفاع عن الوطن والأرض ..</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/88585" target="_blank">📅 22:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88584">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8OjIS43HakJ1pt_XMMmJxVs2VO908zKJVparBEZpTmah4tdBRU5DCxf4np9jwXMLmWFbbBqlNxQDl2ZITt1EAdcMEeSq_DzRzD_6hvyLqtRL0nkcQm1NGH_-QNuzZ8bq1Gy8dT7Fy3UOANgq_wgTN6O5qTA-ko-KrFjJccgA-BLwTnwl5UXRLPcGCXCBcGdhfeG-UT3oeIuRswMzTz12-gh7GojfNPnc9MMbt8lqJfLqDA66g2kOsqztKqy3cFyCfOmnIy7VBpT9IPSAXBjB7WoXOmzoB8KVkZuo20EBX4qF6nAEJCO5dE2_xAaPSPpq5nRWBCRSGeX3Tj6ofyvTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الايرانية بقائي:
أرسلت أمريكا حاملة الطائرات الأمريكية "يو إس إس أبراهام لينكولن" إلى المنطقة لبسط نفوذها.
بعد شهور من الحرب - وأكثر من 200 يوم دون توقف في أي ميناء - تتجه الآن إلى تايلاند لراحة واستجمام الطاقم.
المهمة: مشروع القوة.
المهمة الحالية: مشروع العطلة.
"أنا متعب يا رئيس."</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88584" target="_blank">📅 22:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88583">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
‏
ترامب
:
اليوم، نُحيي ذكرى الأبطال الأمريكيين الثلاثة عشر الشجعان الذين قُتلوا بشكل مأساوي قبل خمس سنوات على يد إرهابيين جهاديين أشرار في كابول، أفغانستان. كانت هذه الكارثة نتيجة انسحاب جو بايدن الفاشل تمامًا من البلاد، والذي ترك جنودنا البواسل عُزّلًا، وسمح لحركة طالبان بإطلاق سراح آلاف الإرهابيين والمجرمين المتعطشين للدماء المحتجزين في سجن باغرام. كانت هذه واحدة من أبشع الفظائع في تاريخ أمتنا، ولن ننسى أبدًا أنها كانت نتيجة عدم كفاءة جو بايدن والديمقراطيين الذين كانوا في السلطة."
‏خلال حملتي الانتخابية لعام ٢٠٢٤، التقيتُ بعائلات ضحايا حادثة بوابة آبي، وهم أناس رائعون ووطنيون عظام، تجاهلهم الحزب الديمقراطي تمامًا ولم يحترمهم. وعدتهم بتحقيق العدالة عند عودتي إلى البيت الأبيض، وقد فعلنا! ألقينا القبض سريعًا على العقل المدبر الشرير المسؤول عن مقتل جنودنا، وكان ذلك من أعظم شرف لي كقائد أعلى للقوات المسلحة. بارك الله أمريكا، وبارك الله عائلات ضحايا حادثة بوابة آبي. لن ننساكم أبدًا! الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/88583" target="_blank">📅 22:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88582">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رويترز
: يبدو أن إيران وعمان تتجهان نحو ممر ملاحي مؤقت بعد ما يقرب من ستة أشهر من الحصار. وفي الوقت نفسه، تظهر واشنطن علاماتها المؤقتة على وقف التصعيد، وتعيد الموظفين الدبلوماسيين بهدوء إلى السفارات في جميع أنحاء الشرق الأوسط.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88582" target="_blank">📅 22:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88581">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COpLS9KOpq66tpxfZC6F0SX5ua6cwjTcor0CRAIILweKA8dz0LyDJmhEww6uVfgAIl1m6C2NrSfx_G_r9ixuagSsFWkIsv_OqTCE5XLblbMESB9xN1VkYiFIsbfSnv0LoYUE5yF2oYaFkNai6RkVIcjYsGuW5f44ToZUT-D0x5bcYoe7F2bXTVgg1_wER0XOErdudoTj-XSW4ICFYtXeO2xeKo_sm4KcL1q2-RDa9JuRfU3CoCf3iADsJs0FQzYI6xBa1n03ysk48-yo35mGcN6_9_NFlxb1SOqIxNOngNs5c5xmxg_KtUOkcZvpgbtQjgtrjkOhHf_RTfKG2UkVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
قاليباف
: نرحب بالبيان المبدئي للصين الذي يرفض العقوبات غير القانونية المفروضة على إيران.
تقوم الشراكة الاستراتيجية الشاملة بين إيران والصين على الاحترام المتبادل، والتعاون المثمر للطرفين، والرؤية المشتركة لعالم متعدد الأقطاب. هذه العلاقة لا تحتاج إلى موافقة أحد.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88581" target="_blank">📅 21:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88580">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
القائد العام وجه بتشكيل لجنة لتحديد شكل العلاقة مع التحالف الدولي بعد انسحابه، عملية انسحاب قوات التحالف تسير بوتيرة متسارعة وفقاً للجداول الزمنية المرسومة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88580" target="_blank">📅 21:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88579">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgDKOuRNy2WEUD6vlRYHLmr5YdX0UyQRlYGVN_4j6zu0wzPlM9HU0n3uohlxeC9arm-4R6UdRAEbgO3nT57Lk4gp21VnGoqz3RfE5QkltfPsbV88n5Iv3aNuEANxQ3u6nsoONvmHOaHEEV7N6Cnc0TycH5h6mbzZZiNa4jMFlKXoCR5CHOp4z_1FdymjGO1qb7aDFtmSmBctNCESFmZnZ7wIPyMN398ocqjq-I3FqRPpCmZhE_5Yy3DKQ0rLV81BmOR8Bqa-mp61ganXxIyJumJ_QwhxzrLNa4nUcxgaJs-c5-LrU2FgS3x5aUsvfu5aqGmc4kwmWkgeiLv4NsD7Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء يلغي الأمر الولائي الخاص بشركة كورك ويُبقي قرار هيأة الإعلام والاتصالات بإيقاف العمل مع الشركة قائماً.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88579" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88578">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
‏
وزير الطاقة الأميركي:
رغبتنا قوية في إنهاء البرنامج النووي الإيراني عبر المفاوضات.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88578" target="_blank">📅 20:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88577">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2FxRebBiXWCjWO2YL47JXCE_-UpTUguz2WEhmfRcd7_LhFf-lgb0_1o9MWJBxsU-P59E3d5rN3gGmcNNOPLKhaDQ5S4MW1ybRbYCySR6GC9K7WsUqd4T9hK8Oe4-lKzOCQZNZZaPSsFqep3U8QM2J4TMYS_R8rRCFDjeHsq8c2bHgndRp86MLwiQx4tt0QF25j4Nh_TsRmuybVzP1FW0HxlHS_IycXmPbyof4TbwZLgiG3ErJ7p_ik03PximjmbgH659r7k4UT99wuUoeSF4R8RwYBaEUwD8VCRa-fpDyofW1jV0Dz8MRDWxcR5bZeUM2mn8EYa6XpE8kC-m9LQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: اكتملت المهمة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88577" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88576">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
🏴‍☠️
إعلام أمريكي : ‏بوتين يسعى لتصعيد الحرب في أوكرانيا بعد وصول المحادثات إلى طريق مسدود .</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88576" target="_blank">📅 19:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88575">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX08zDsSNA4fxd2mi8iVu6QI495_x-OplV0vEAzf6E5sXy5BgVuJIZb_Lk2hGVl61u-IdcvXsqIR9nwdUDzwrGrf2jqWa7Qvz5BPAuq4qx2IFLNO5wPSFq1LU_TY-KdWeOjIzvk_J6dHw5PRFueOYuFJ7xIQaydM5U2TB0y0MyzI3Gf-DJ5Ldb1GBvvsDEmAhd9y2IreKkx8ivrlh4kupwFxgBoZTo6tEDAmC2hAoiFH1lpcW9-GTa4xJOzbpNUvi35XNq8hp9aOVPetoiKSes9251WzGPbDg1SdlbceMP4mPf3ySY-GNV1KBhwMvSKQAq5LuTlNSjKx_BOfgXniMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
سفينة نفطية هندية باسم "HAANA" كانت تنوي العبور عبر المسار الجنوبي لمضيق هرمز المعروف باسم "الممر العماني"، ولكنها تراجعت بعد تلقي تحذير من حرس الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88575" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88574">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
وكالة الطاقة الذرية الايرانية:
‏إيران لا تزال في حالة حرب، ولم يتم تأمين مواقعها النووية للتفتيش.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88574" target="_blank">📅 18:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88573">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVKv0JcyzKdgSS3LpS-Bjh17-e5_Vbp2wtMzjERWSIl0PUA8Igke4iTad79Y_HUaEVeC2mZAo92-fBwYstisMkuFvMAAxKQ1MmlW8TCGrWjIstBwwY9fqaRBPgPLSog58KqAFy7DEmtE6Pzn_aS48irC-XHW-5GpJGdcqCyuhk8qno4QlKXuqJJ4Zz7ALdMZUwgjmLk8q3zBQOCpomjR41qfQ1TSdXrOVHv87Djhp4rmHoGGGH-6lVXwSo0EkFvoeNdjgmzp-GM4m630StppSTZCdP7Ykhlu2Oc2m4dN0TwPYBlCFNsS5YJEyjEMQvXUKpayIHEHDdLd7e5zHAdvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای سربازِ روح‌الله، ما در (نايا) همواره از تو شنیده‌ایم ومی‌آموزیم که علی علیه السلام فرمود:
به جانت سوگند، آدمی چیزی جز گوهرِ دینش نیست؛
پس مبادا دینداری خویش را به اتکای نَسَب و تبار واگذاری.
نگر که قرآن چگونه «سلمانِ پارسی» را تا اوجِ والاآرمانی بالا کشید،
و چگونه شرک و کفر، «ابولهبِ» والاتبار را به خاکِ مذلّت فروفکند.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88573" target="_blank">📅 18:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88572">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMDi3EN4EyFVGBUZoC096szWqCAVRTywNjseeIbiT3RTTaMFAMpq6bVj6QfB5lqLDNNzR9fpQTFyNkCUfdKi2SZeWczx2ANQ2an3GCfMx_DsuEDbynWnihGPz3Lw8SXDCiQJEFplB7LscZ_Cxeg55CBbFEuKPYQIMRY7QF78JoD47E_LvXDnpoK2IexJbic_cKVGyJbfHl4D61j7l231fQXE4PU149VA8iMUDhg1Xmo8zsMoZTbjWDNvcJ0-Arx5l-nbJPjkSHCfiWfBD_ANQI2BhuQpaQJ5z2963WV9_fdS0ege3BttvzC_Kc5HpnfgxTtGf6twN368lQgOzTW2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش السلطة اللبنانية الذي ينزح مع النازحين في كل حرب يزعم: إيقاف سوري أثناء محاولته تهريب قذائف صاروخية إلى الأراضي اللبنانية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88572" target="_blank">📅 18:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88571">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e4021968.mp4?token=RvriLnJ_ZdJlAU-Mzwv51cQlSwfU7f0sp-nOTo2uiTMr4pWHxfGxBqgx7irHBwLyg-_IzRrcv8TpyGMI5dUlOF6OPeq9oc1WDzt5ir_4MY-X8O-J3w-8ifCZEuDcZejwzfWumhhJeWbKMf9jlsun3EBVx0AOJ1SlyqRqb87zKO5XnxV7Kgi30PjcmKz5g5G0_HiRduqQUx5LN6qqZpmdPP7z4pxLaL1Cc5F4ymNRt0vVXJbQHPTyZFaVHXqcM4DbLgEDvK5OW_5ALQLGNWVivRgTbIfhOMX65FAxzaVEhCb1JYzPxD-kUZCyHWYIgNDCL0NilsSSQzaENdhhUtHpVAfcrgH88c5PY5Lt4CjX8wq-CTWOej2CvZ-ZDdDj94lXamLV1uXcPuBvV6xpw_lRK36OFLjifbXIfaf6L50fADXNyqGUPfX81tkyUtMD8xK4U4nu3TwuGYxACvRZt8KPzUNKUjzTDL7mDxZIYhCjjc_gkit1LuzcVaOkS-w0EcmNdeunZfp_8-u2k5u7Te7rQvrwJQlKD5A-xGGLzks4YTLiRi5QPoel-cmAEHK7OzXQwHAkPaxacZH-URTzAh4jpN7yznTDA1rqEAT72HTQZ5nxOUHQpXISzzmNja8BmXrjWv-puD-Hyt42C8aSQDNeAdjvrbO1bPSaGzT9-c2dfjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e4021968.mp4?token=RvriLnJ_ZdJlAU-Mzwv51cQlSwfU7f0sp-nOTo2uiTMr4pWHxfGxBqgx7irHBwLyg-_IzRrcv8TpyGMI5dUlOF6OPeq9oc1WDzt5ir_4MY-X8O-J3w-8ifCZEuDcZejwzfWumhhJeWbKMf9jlsun3EBVx0AOJ1SlyqRqb87zKO5XnxV7Kgi30PjcmKz5g5G0_HiRduqQUx5LN6qqZpmdPP7z4pxLaL1Cc5F4ymNRt0vVXJbQHPTyZFaVHXqcM4DbLgEDvK5OW_5ALQLGNWVivRgTbIfhOMX65FAxzaVEhCb1JYzPxD-kUZCyHWYIgNDCL0NilsSSQzaENdhhUtHpVAfcrgH88c5PY5Lt4CjX8wq-CTWOej2CvZ-ZDdDj94lXamLV1uXcPuBvV6xpw_lRK36OFLjifbXIfaf6L50fADXNyqGUPfX81tkyUtMD8xK4U4nu3TwuGYxACvRZt8KPzUNKUjzTDL7mDxZIYhCjjc_gkit1LuzcVaOkS-w0EcmNdeunZfp_8-u2k5u7Te7rQvrwJQlKD5A-xGGLzks4YTLiRi5QPoel-cmAEHK7OzXQwHAkPaxacZH-URTzAh4jpN7yznTDA1rqEAT72HTQZ5nxOUHQpXISzzmNja8BmXrjWv-puD-Hyt42C8aSQDNeAdjvrbO1bPSaGzT9-c2dfjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عبوة ناسفة في صحراء محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88571" target="_blank">📅 18:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88570">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حدث امني في صحراء الانبار</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/88570" target="_blank">📅 18:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88569">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حدث امني في صحراء الانبار</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88569" target="_blank">📅 18:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88568">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
🇨🇳
الولايات المتحدة: عرقلنا قراصنة صينيين اخترقوا وكالة ناسا والاحتياطي الفيدرالي والمعاهد الوطنية للصحة ومجلس الشيوخ.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88568" target="_blank">📅 17:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88567">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
🇨🇳
الولايات المتحدة:
عرقلنا قراصنة صينيين اخترقوا وكالة ناسا والاحتياطي الفيدرالي والمعاهد الوطنية للصحة ومجلس الشيوخ.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88567" target="_blank">📅 17:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88566">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏امريكا تفرض عقوبات على موقع مجموعة العمل الفلسطينية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88566" target="_blank">📅 17:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88565">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامب: ليس لدى كندا أي شيء نحتاجه وحان وقت الاستغناء عنها لتعليم كندا أنكم لا تستطيعون فعل هذا بعد الآن</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88565" target="_blank">📅 17:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88564">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامب: ليس لدى كندا أي شيء نحتاجه وحان وقت الاستغناء عنها لتعليم كندا أنكم لا تستطيعون فعل هذا بعد الآن</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88564" target="_blank">📅 17:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88563">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74978db9a.mp4?token=D5AfvwZgOnUDujh49g8_0UPlB9dhi1MIg1H8ufivyFkNAZIpMmffC0Wxu2uXurmDwzr61Winh0QhEPpAy4fbmaip6L9k-ruvvDNBeAOYJR5moGeClcfYX1EPx_lCX-xutsBRNdqKPxN_jDfLZB6S4Bp2NqwNVh5EI_Wxoh4HlYknw2d42hce48NlNJz0_bp6JAIBoaRgLnbhZW6bVofbWD0K9yEqpaE82N5QLfeFOzBF9eFd0Frk2xBZECE5ineycbIksHfe2z-2wLrEvZ9Tdpk2fJb7ulxcNXeEGmsz0efshGebvr7iylBGzU8pggOxoFCTmIUhpxJ6TEHcf8Csp3_vCweZV6HkRsTAnhgNb0QiCOfgZBtuWoV4XZRHvpkS3rC1JmEBFdU--QeMaR3qwkRoFNvPgdjjTD_FadErUGCbBXI0F0cQesGDdYciZg5W5VhyQwlOwl2nLjGRQ345_Z6juWnIViG2UEBEPHFs22ZPbYyXfFS0l_wC_s9zwmq2pI0jpMuVIzVDie6IneFFJYvgUpoEtvSJSxo_BFmiW6XMM8VJfpqkw5p5s3kKXlzRCobnDk8Gu2HKSYLvkue9zOHnhpnlnjSrgbg3KAA2168zKvZFOrKuJVydEvqr0tRB5K9Fy4h_ttuAnlN_-F9-3NZFLbfAJNrO2EFDAV0zW2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74978db9a.mp4?token=D5AfvwZgOnUDujh49g8_0UPlB9dhi1MIg1H8ufivyFkNAZIpMmffC0Wxu2uXurmDwzr61Winh0QhEPpAy4fbmaip6L9k-ruvvDNBeAOYJR5moGeClcfYX1EPx_lCX-xutsBRNdqKPxN_jDfLZB6S4Bp2NqwNVh5EI_Wxoh4HlYknw2d42hce48NlNJz0_bp6JAIBoaRgLnbhZW6bVofbWD0K9yEqpaE82N5QLfeFOzBF9eFd0Frk2xBZECE5ineycbIksHfe2z-2wLrEvZ9Tdpk2fJb7ulxcNXeEGmsz0efshGebvr7iylBGzU8pggOxoFCTmIUhpxJ6TEHcf8Csp3_vCweZV6HkRsTAnhgNb0QiCOfgZBtuWoV4XZRHvpkS3rC1JmEBFdU--QeMaR3qwkRoFNvPgdjjTD_FadErUGCbBXI0F0cQesGDdYciZg5W5VhyQwlOwl2nLjGRQ345_Z6juWnIViG2UEBEPHFs22ZPbYyXfFS0l_wC_s9zwmq2pI0jpMuVIzVDie6IneFFJYvgUpoEtvSJSxo_BFmiW6XMM8VJfpqkw5p5s3kKXlzRCobnDk8Gu2HKSYLvkue9zOHnhpnlnjSrgbg3KAA2168zKvZFOrKuJVydEvqr0tRB5K9Fy4h_ttuAnlN_-F9-3NZFLbfAJNrO2EFDAV0zW2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏سأمنع منعاً باتاً تطبيق الشريعة الإسلامية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88563" target="_blank">📅 16:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88562">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd317e66d.mp4?token=OqhAW24-apmyTSKDfM_ky00fCXs6u_bJlxDPgEorRFq_EQUXKM740XZcb1rz-Fpo6wcnkovx7h77VZUbNN7jeqI7uQ58wxL5ehubFdNir_YFuyUj_NvRA6yD2eQWQ2JqTap9_uxJ50QKNBS4w5DBZblx9X3NJqayKd8ymaJ2cFEEWyfttuwQS0XsnWlXH_eaj6yri3dMOeUe3sI9hxed_yLN7YjWTy2RXJ_HxaBR9LQO-CT5E1--NngXaUmzJqUeDNN1ZSqWNmtJfajdaceAr9pAP4-tGa2H-fZngReYbX-U8iXYvOkURX5M5D8__KV2pEhnXAN-BiFvqV_9EorGqQNEHGYjTc9G6ATScHd3gNO8artOz4VptZ5v2bm6qvPnuFW8DpA4jIFepsdOJc51NR5XSKdKGwFEryWGXcqrdmMALezswBBUKPTo2ZGpVIc2EpADMBF5Z44KboyxsQVFe-bnBazvKv0OEmEBdP-1ALWi93C8uZwM0UOOgwuVvKtP2D4WLMxxcfCq-IgR2n2r8GphL0MYJSj5DQtqDNXlGcDoHRggNXxuU6XavUdry4xn3HDK7mHXs1kMopirj6JulADFZPzOZf9fwB6LZcX8Z1DcnrLJNeDNkZ_JaKhKlUXo4kVB-Df3u_oT8D7prRVTwfIgGUyC5xPmhUqtPIZrZlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd317e66d.mp4?token=OqhAW24-apmyTSKDfM_ky00fCXs6u_bJlxDPgEorRFq_EQUXKM740XZcb1rz-Fpo6wcnkovx7h77VZUbNN7jeqI7uQ58wxL5ehubFdNir_YFuyUj_NvRA6yD2eQWQ2JqTap9_uxJ50QKNBS4w5DBZblx9X3NJqayKd8ymaJ2cFEEWyfttuwQS0XsnWlXH_eaj6yri3dMOeUe3sI9hxed_yLN7YjWTy2RXJ_HxaBR9LQO-CT5E1--NngXaUmzJqUeDNN1ZSqWNmtJfajdaceAr9pAP4-tGa2H-fZngReYbX-U8iXYvOkURX5M5D8__KV2pEhnXAN-BiFvqV_9EorGqQNEHGYjTc9G6ATScHd3gNO8artOz4VptZ5v2bm6qvPnuFW8DpA4jIFepsdOJc51NR5XSKdKGwFEryWGXcqrdmMALezswBBUKPTo2ZGpVIc2EpADMBF5Z44KboyxsQVFe-bnBazvKv0OEmEBdP-1ALWi93C8uZwM0UOOgwuVvKtP2D4WLMxxcfCq-IgR2n2r8GphL0MYJSj5DQtqDNXlGcDoHRggNXxuU6XavUdry4xn3HDK7mHXs1kMopirj6JulADFZPzOZf9fwB6LZcX8Z1DcnrLJNeDNkZ_JaKhKlUXo4kVB-Df3u_oT8D7prRVTwfIgGUyC5xPmhUqtPIZrZlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الايرانيين غير محترمين</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88562" target="_blank">📅 16:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88561">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17c3fa946.mp4?token=kXqhxrEV0Wrg7ryeWYNIxBpu84yRgwdUSoT-WncOrrRjJ9atyXtSPTvlIZ28jLPRt7AmDCCBOwjRhIMdJVo8xtYHeOgX32g1rFm24F5LTTJ9Z-Fzd2FQ5PJLaF_IV7LjqF4K-OI5jyka6kgpShZC0ln_6rz8R4ZcaDxjYoTb88K5fdUuE72xCd_CktE51jKDnqcPB6Y5zKv0MAlc5BVrQNjGpN0raVdieZDy_KLAeZU1_fFVffdtOIGpb433AmcjCGt0x6OkaonbUPoyt1LRoEgUT3TEqXeoRaZGjAAPFl1nvCzfiIl_mHkoXHPsbaPpvVQKAHzsicfE0ZIT6WU2sCs-3iSmGG65o0WgZX8rHiYs8fiPxDVxTYqmMkvmkGWox1kKp6ods7CChzPBiiiHaHGo0e7md00FrrnQXYL12loW-CEEJguJIFMYnQARk6W9G9J1buPlHflOxh1INa-BH8UgloAbUg6xK58qVWvgoXqapBPxZZxH4YqlXpt67r-wq_QXZXvZDyRn28wyrYg8oImmtIPUXtJFMmpHemLL_JkInrmSWg_89guOa-Dvdc6Mrfjkj1vZKkQ9Y0SLvKR0GKDgUsMbHv3OEYKCHg2mvPXcZ7aiRqY_C73wUpi95jVOxx-ymI6k1iGJa1jtd-DHnW1R1g8KJf9i_HDv7dl70jI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17c3fa946.mp4?token=kXqhxrEV0Wrg7ryeWYNIxBpu84yRgwdUSoT-WncOrrRjJ9atyXtSPTvlIZ28jLPRt7AmDCCBOwjRhIMdJVo8xtYHeOgX32g1rFm24F5LTTJ9Z-Fzd2FQ5PJLaF_IV7LjqF4K-OI5jyka6kgpShZC0ln_6rz8R4ZcaDxjYoTb88K5fdUuE72xCd_CktE51jKDnqcPB6Y5zKv0MAlc5BVrQNjGpN0raVdieZDy_KLAeZU1_fFVffdtOIGpb433AmcjCGt0x6OkaonbUPoyt1LRoEgUT3TEqXeoRaZGjAAPFl1nvCzfiIl_mHkoXHPsbaPpvVQKAHzsicfE0ZIT6WU2sCs-3iSmGG65o0WgZX8rHiYs8fiPxDVxTYqmMkvmkGWox1kKp6ods7CChzPBiiiHaHGo0e7md00FrrnQXYL12loW-CEEJguJIFMYnQARk6W9G9J1buPlHflOxh1INa-BH8UgloAbUg6xK58qVWvgoXqapBPxZZxH4YqlXpt67r-wq_QXZXvZDyRn28wyrYg8oImmtIPUXtJFMmpHemLL_JkInrmSWg_89guOa-Dvdc6Mrfjkj1vZKkQ9Y0SLvKR0GKDgUsMbHv3OEYKCHg2mvPXcZ7aiRqY_C73wUpi95jVOxx-ymI6k1iGJa1jtd-DHnW1R1g8KJf9i_HDv7dl70jI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🌟
ترامب:  لا أعتقد أن السيد مجتبى قد مات. لقد أصيب بجروح خطيرة للغاية، في الجانب الأيسر من جسده، في الذراع، والساق، وقد أصيبت كل هذه المناطق بجروح خطيرة. ولكنني لا أعتقد أنه مات. إذا كان قد مات، فهم يقدمون عرضًا جيدًا جدًا، لأنهم يتحدثون باستمرار عن العودة…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/88561" target="_blank">📅 16:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88560">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3bd09b95.mp4?token=od7M2K4tvpR1-3UT1Qud6iWKvGpJF4qWR3P0HthIeLN31czdSCFLmDyGZUM_Kt8qJgVorXkwGYR-Zlh5I1mPZ8oUu0CTmzHLJ5JwZjtd82y54OvM_ysLmkhcECpyrk2SKpmhnJZX0-h1_WPikoqXiR0yK17jSyFLRGJhALe5P81cmaKTjecZNHc_mEzNK89_21e100VAXoCgfNex6Km1QEQb3M-AXNrtC7Z1retvfL4x9cH7teIG79AYKzqOtNDJb5zlo-UahUDGqD8_KVUJnOEO7JNp0OSyFRBmKckxyoswFSylIRDd0KsyJbgmTFYwbPgBwhv7VWgYTct76oGxyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3bd09b95.mp4?token=od7M2K4tvpR1-3UT1Qud6iWKvGpJF4qWR3P0HthIeLN31czdSCFLmDyGZUM_Kt8qJgVorXkwGYR-Zlh5I1mPZ8oUu0CTmzHLJ5JwZjtd82y54OvM_ysLmkhcECpyrk2SKpmhnJZX0-h1_WPikoqXiR0yK17jSyFLRGJhALe5P81cmaKTjecZNHc_mEzNK89_21e100VAXoCgfNex6Km1QEQb3M-AXNrtC7Z1retvfL4x9cH7teIG79AYKzqOtNDJb5zlo-UahUDGqD8_KVUJnOEO7JNp0OSyFRBmKckxyoswFSylIRDd0KsyJbgmTFYwbPgBwhv7VWgYTct76oGxyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز تعز بعد هجوم لانصار الله على مرتزقة السعودية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88560" target="_blank">📅 16:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88559">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
🌟
ترامب:
لا أعتقد أن السيد مجتبى قد مات. لقد أصيب بجروح خطيرة للغاية، في الجانب الأيسر من جسده، في الذراع، والساق، وقد أصيبت كل هذه المناطق بجروح خطيرة. ولكنني لا أعتقد أنه مات. إذا كان قد مات، فهم يقدمون عرضًا جيدًا جدًا، لأنهم يتحدثون باستمرار عن العودة للتحدث إليه للحصول على بركاته الأخيرة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88559" target="_blank">📅 16:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88558">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#تقني
🔻
القضاء الامريكي يصدر حكما يلزم شركة ميتا بوضع حدود يومية لاستخدام تطبيقاتها وحظر استخدام الإنترنت ليلاً لمستخدمي منصات التواصل الاجتماعي التابعة لها من المراهقين.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88558" target="_blank">📅 16:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88557">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
🇮🇷
مصدر إيراني رفيع المستوى:
لم يتم التوصل إلى اتفاق نهائي مع سلطنة عمان بشأن مضيق هرمز حتى الآن. لا تزال إيران وعُمان تعملان على تفاصيل اتفاقية تتعلق بمضيق هرمز.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88557" target="_blank">📅 16:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88556">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
وزارة المالية العراقية تباشر بتمويل رواتب الموظفين لشهر آب الحالي ابتداءً من اليوم.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88556" target="_blank">📅 15:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88555">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">📰
وكالة رويترز:
تحقق السلطات الأمريكية في اختراق ايراني لبيانات شركة مصنعة لتكنولوجيا مرافق المياه.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88555" target="_blank">📅 15:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88554">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbMR6-PskKvB_dch_NqBZ82Bzx5r-KDEn1VvJ7YndNCkBJkeGDQEXDvDj8l8IJ6GLUUR-yL4j_LU9Kjg5_rFIpYf_8wE_6kn0D078IjLU3WNdUof1fVyJIiy_NFFcKtMa-aDdZ6VLcuHi-GvCtUk-jvyq75bGbkaW37zQHXW0EamDusKbpDS4fjyigg8qdcGi3ODTE6PxCrez1_v7NOKpviGxyMdi3elHhrr3Nqf232ryYW1U7nrGUZB-RR9dIOpqEf2Kv7b9pJzjNVC-eODmLe3TwfxGDGdKx5NeVHLN1Oc3iESsm72gczAS4YnjGM0-XmuLCN0QmRm0nRCAKDj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
يسمح بالنشر بعد قليل ..</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88554" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88553">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
حرس الثورة:
اتفقنا مع عمان بشأن حصة كل منا من مياه مضيق هرمز وحصص عائداته.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88553" target="_blank">📅 15:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88552">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
حرس الثورة:
مضيق هرمز تحت سيطرة الحرس الثوري، ولا توجد أي سفن حربية معادية في الخليج. جميع السفن الحربية المعادية على بُعد 400 كيلومتر من مضيق هرمز، ومن الناحية العسكرية والإقليمية، لا يمكن لأي سفينة عبور هذا المضيق دون إذن إيران وإدارتها.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88552" target="_blank">📅 14:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88551">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9092897d1.mp4?token=adfvACwJuMLosKfdwuZkXOUHiBa0twj7npEMY7mtJywRPNbAhFKQjMA8sdFwOIstM2k5v5ppfrrsfJFLa9ShldnxO3bGXXiYhlO3C6e42QhmICcUDYQs_bjpRS1TFh8vwJ6D_geWHo2tnOppkaenXfTOdmGNuVZ9GwuCZLwrFFrNODLhKgekKoj-aUqrJKd5KcW13rlV5bqTobMtYno9g26wwnbSA23sH0smbL-S2McTCe_YzncJwl-wGs_2mBJgwDtC0P4euTTSJqNCRRuQ56HU84V373w2-ggSqgl1aEK-7PvJK1h2WFmnXO2jhU0dTL0i-QwHQJGrCzsGaJ2frA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9092897d1.mp4?token=adfvACwJuMLosKfdwuZkXOUHiBa0twj7npEMY7mtJywRPNbAhFKQjMA8sdFwOIstM2k5v5ppfrrsfJFLa9ShldnxO3bGXXiYhlO3C6e42QhmICcUDYQs_bjpRS1TFh8vwJ6D_geWHo2tnOppkaenXfTOdmGNuVZ9GwuCZLwrFFrNODLhKgekKoj-aUqrJKd5KcW13rlV5bqTobMtYno9g26wwnbSA23sH0smbL-S2McTCe_YzncJwl-wGs_2mBJgwDtC0P4euTTSJqNCRRuQ56HU84V373w2-ggSqgl1aEK-7PvJK1h2WFmnXO2jhU0dTL0i-QwHQJGrCzsGaJ2frA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ارتفاع كبير تشهده اسعار الوقود في محافظة اربيل شمالي العراق حيث وصل سعر لتر البانزين الى 2500 دينار.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88551" target="_blank">📅 14:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88550">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
قالیباف:
إذا لم نتمكن من تحقيق مطالبنا، فسنواجه الولايات المتحدة بسيف القوة.
يجب إيداع الأموال الإيرانية المحتجزة في حساباتنا ووضعها تحت تصرف البنك المركزي؛ فوجود خط ائتماني يعني أن بإمكان البنك المركزي فتح "اعتماد مستندي" (LC) لأي جهة يختارها وفي أي وقت يشاء.
إذا حاول العدو الغدر، فنحن رجال الميدان؛ إذ أن المسافة بين ساحة الصراع الدبلوماسي وساحة المواجهة العسكرية قصيرة بالنسبة لنا، وأصابعنا على الزناد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88550" target="_blank">📅 13:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88549">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
🇷🇺
إعلام أمريكي : ‏أفاد مسؤولون أمريكيون أن مدير وكالة الاستخبارات المركزية الأمريكية، جون راتكليف، توجه إلى موسكو، روسيا، في زيارة غير معلنة يوم الثلاثاء، وهي أول زيارة رسمية له إلى العاصمة الروسية. وقد أمضى راتكليف نحو أربع ساعات في موسكو قبل مغادرته.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88549" target="_blank">📅 13:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88548">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
🇺🇸
دوي صافرات الإنذار بالسفارة الأميركية في بغداد وسط حالة من الرعب تصيب سكان مجمع بغداد رزدنتي الملاصق لمجمع السفارة !</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88548" target="_blank">📅 12:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88547">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1481148818.mp4?token=t22N30PBKFlS5lxBhiSf23Iwj8JgZm5Hd_Ktdw9P1A4QG1zbe_MRULQL8MmHIvzhEXkRS04xICtj7qlo6xAGqzHo1okd7GX12yH3q5WS-l3kHQbohTR3QFg-81D2SSs4_Liop_khcnn5FSLJRJ9LWt5QGUXKEx9nTK5Kh4qyolldsVw-Ly6Hrm87C8SQ2Wu9V1OBVYMlWLw9w5_nxLCQlnRCS2QoBApQ22MBv6cZ41UAX3xxfqi6v3XTuCG5OxuGF8Mz5zbPWNl-ktWit0HGdvLeivl9NuUkblAE36MfAKGX-8ta4Hb2igNwIAs69qx6XFbpbmyPdMZXxIBqsurHTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1481148818.mp4?token=t22N30PBKFlS5lxBhiSf23Iwj8JgZm5Hd_Ktdw9P1A4QG1zbe_MRULQL8MmHIvzhEXkRS04xICtj7qlo6xAGqzHo1okd7GX12yH3q5WS-l3kHQbohTR3QFg-81D2SSs4_Liop_khcnn5FSLJRJ9LWt5QGUXKEx9nTK5Kh4qyolldsVw-Ly6Hrm87C8SQ2Wu9V1OBVYMlWLw9w5_nxLCQlnRCS2QoBApQ22MBv6cZ41UAX3xxfqi6v3XTuCG5OxuGF8Mz5zbPWNl-ktWit0HGdvLeivl9NuUkblAE36MfAKGX-8ta4Hb2igNwIAs69qx6XFbpbmyPdMZXxIBqsurHTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حادث سير مروع في محافظة أربيل شمالي العراق ؛ مقتل 6 وإصابة أخرين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88547" target="_blank">📅 12:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88546">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان الإيراني محمدباقر قالیباف:  دور إيران والعراق في إرساء النظام الإقليمي حاسم.  لقد أطلقت أمريكا حربًا ضد إيران بهدف الإطاحة بالنظام الإسلامي وتوسيع هيمنتها في غرب آسيا والعالم الإسلامي، ولكن بفضل دماء الشهداء وبجهود الشعب الإيراني الشجاع وجهود…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88546" target="_blank">📅 12:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88545">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان الإيراني محمدباقر
قالیباف:
دور إيران والعراق في إرساء النظام الإقليمي حاسم.
لقد أطلقت أمريكا حربًا ضد إيران بهدف الإطاحة بالنظام الإسلامي وتوسيع هيمنتها في غرب آسيا والعالم الإسلامي، ولكن بفضل دماء الشهداء وبجهود الشعب الإيراني الشجاع وجهود جبهة المقاومة، لقد منيوا بهزيمة واضحة، وأقر بذلك العالم أجمع.
إن انسحاب القوات الأمريكية المتحالفة من العراق هو مصدر فخر تاريخي للحكومة والشعب العراقي، ونأمل أن يتحقق هذا الانسحاب بشكل كامل من الأراضي والجو العراقي.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88545" target="_blank">📅 12:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88544">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇱
نتنياهو: لا يمكن التوصل إلى اتفاق دبلوماسي مع إيران.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88544" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88543">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔻
إعلام العدو:
من يتوقع أن ترفع إيران الراية البيضاء فهو مخطئ، فهذا ليس من أيديولوجيتهم، وليس في حمضهم النووي، وأعتقد أن ما يفعلونه حاليا، هو أنهم يستعدون سرا للهجوم الكبير الذي يريدون شنه ضد الولايات المتحدة وضد حلفائها في المنطقة قبيل انتخابات التجديد النصفي.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88543" target="_blank">📅 12:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88542">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇱
نتنياهو:
لا يمكن التوصل إلى اتفاق دبلوماسي مع إيران.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88542" target="_blank">📅 12:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88541">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
هزة أرضية بقوة 4 ريختر تضرب قضاء بنجوين في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88541" target="_blank">📅 11:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88540">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
مناطق شرق مضيق هرمز وشمال المحيط الهندي وبحر العرب وبحر عمان تخضع لسيطرتنا العملياتية.
السفن تخضع لمراقبتنا قبل وصولها لمضيق هرمز بمئات الكيلومترات ويمكنها العبور إذا حصلت على إذننا.
قواتنا البحرية لم تسمح لسفن العدو العسكرية بالاقتراب من سواحلنا.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88540" target="_blank">📅 10:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88539">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
رويترز:  انخفضت صادرات قطر من الغاز الطبيعي المسال بنسبة 96٪ بعد إغلاق مضيق هرمز بشكل فعال، حيث تم تصدير 18 شحنة فقط مقارنة بـ 509 شحنة في العام السابق.  فقدت قطر ما يقرب من 24 مليار دولار من عائدات الغاز، بينما تساهم زيادة صادرات الغاز الطبيعي المسال الأمريكية…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88539" target="_blank">📅 10:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88538">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
رويترز:
انخفضت صادرات قطر من الغاز الطبيعي المسال بنسبة 96٪ بعد إغلاق مضيق هرمز بشكل فعال، حيث تم تصدير 18 شحنة فقط مقارنة بـ 509 شحنة في العام السابق.
فقدت قطر ما يقرب من 24 مليار دولار من عائدات الغاز، بينما تساهم زيادة صادرات الغاز الطبيعي المسال الأمريكية في سد جزء من هذا النقص.
في الوقت نفسه، تبلغ مستويات تخزين الغاز في أوروبا أدنى مستوى لها في هذا الوقت من العام، مما يزيد من خطر ارتفاع الأسعار مع اقتراب فصل الشتاء.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88538" target="_blank">📅 10:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88537">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
في مظهر غير حضاري..
ساحات الإحتفال بالمولد النبوي الشريف بمحافظة أربيل شمالي العراق تتحول إلى مكب للنفايات!!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88537" target="_blank">📅 10:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88536">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔻
الإعلام الأمريكي:
تم إخلاء يائير نتنياهو سرًا من ميامي قبل عدة أشهر، وذلك بعد اكتشاف خلية إيرانية كانت تراقبه في اللحظات الأخيرة.
تم تهريبه بسرعة كبيرة لدرجة أن أغراضه بقيت خلفه، بعد تقديرات تشير إلى أن الخلية الإيرانية كانت بالفعل "موجودة" في منطقة ميامي.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88536" target="_blank">📅 09:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88535">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
🇮🇷
إن بي سي:
تسببت الهجمات الصاروخية والطائرات المسيرة الإيرانية في أضرار بمليارات الدولارات لمواقع الاستخبارات الأمريكية ومعدات المراقبة في جميع أنحاء الشرق الأوسط.
لقد كشفت هذه الهجمات غير المسبوقة عن نقاط ضعف في دفاعات القواعد الأمريكية وأجبرت المسؤولين على إعادة التفكير في كيفية حماية المنشآت الحساسة.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88535" target="_blank">📅 01:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88534">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
🇸🇦
مسؤول في الإدارة الأمريكية:
إدارة ترامب أحالت إلى الكونغرس اتفاقاً مع السعودية بشأن الطاقة النووية المدنية.
ترامب لا يزال يعتقد أن الاتفاق النووي مع السعودية لن يتقدم إلا إذا انضمت السعودية إلى اتفاقيات ابراهام و اعترفت بإسرائيل.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88534" target="_blank">📅 01:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88533">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2ae12376.mp4?token=ELZrHqQRc726i__ZAtF5Ee6AgVCJU-w2DKSWstsosgPNlCw3tm-DzWvP20dOaxzh3heuPgIXhto-xwSESWd6whCGOzjUMQjQ4J8VU5xcC7_aarb1Tm9PFawBrwp80NNd6s5SyEov1OyW6K4LzlalXhGLHWOIg1vXWDP6MnxjukltCChZPO32U1AnVrVBdc36L9_zUIoKVeY_nXU_0xbcbhlIeiUZYURs9CaUddZ6-YETHRYOXegfoDY1k2lPl7IAZMOzv1K06J6xLczENl8T_Y5WD6VbtHHr5z3YcypeJVpzv0lMA584OiIWU6JjQGIWBv4x6Z34A5o_Cit3n4abnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2ae12376.mp4?token=ELZrHqQRc726i__ZAtF5Ee6AgVCJU-w2DKSWstsosgPNlCw3tm-DzWvP20dOaxzh3heuPgIXhto-xwSESWd6whCGOzjUMQjQ4J8VU5xcC7_aarb1Tm9PFawBrwp80NNd6s5SyEov1OyW6K4LzlalXhGLHWOIg1vXWDP6MnxjukltCChZPO32U1AnVrVBdc36L9_zUIoKVeY_nXU_0xbcbhlIeiUZYURs9CaUddZ6-YETHRYOXegfoDY1k2lPl7IAZMOzv1K06J6xLczENl8T_Y5WD6VbtHHr5z3YcypeJVpzv0lMA584OiIWU6JjQGIWBv4x6Z34A5o_Cit3n4abnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الولايات المتحدة
: تحطمت مروحية في ولاية كنتاكي تابعة للجيش من طراز UH-60 Black Hawk، وكان على متنها أربعة أشخاص.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88533" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88532">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
صرح وزير الخارجية ماركو روبيو لعدد من نظرائه الأجانب في الأيام الأخيرة بأنه "في الوقت الراهن" لا يُتوقع أن تشنّ الولايات المتحدة ضربات جديدة ضد إيران، وأن تُركّز على الضغط الاقتصادي.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88532" target="_blank">📅 01:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88531">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ff577c2b.mp4?token=S0J5HVKvhYsoqumQvpZBDZ09nHwrI5SZIfzL_rt5DVHgGekSaoq_OwzgwuI6Y7kO705jQ8IJJojvGNs3IOAW2qwZVhET1h_Zk7fGGNnJe1BlSx9Bbl8Oh-zdTt2L3T7XAKQaFUkbOtbXHb2dUqvNxc4jxdujF3I2J7ZzUhJ6twzSVRPN4ifALa7pDWleYPI9NZh09K-Omsgeoa7yHULoafjWJ8Z-bKyi8rWm4i44P8E4pDV46BMYcTxKrYkpv2-yc-sV0fxo7Ea8YwuzzPBes9cB6PGTMHxh3LouxxKZJTFayn_sqOm6QRcfco0qJl4JtKFkkgL1iEodIsFL1SdhBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ff577c2b.mp4?token=S0J5HVKvhYsoqumQvpZBDZ09nHwrI5SZIfzL_rt5DVHgGekSaoq_OwzgwuI6Y7kO705jQ8IJJojvGNs3IOAW2qwZVhET1h_Zk7fGGNnJe1BlSx9Bbl8Oh-zdTt2L3T7XAKQaFUkbOtbXHb2dUqvNxc4jxdujF3I2J7ZzUhJ6twzSVRPN4ifALa7pDWleYPI9NZh09K-Omsgeoa7yHULoafjWJ8Z-bKyi8rWm4i44P8E4pDV46BMYcTxKrYkpv2-yc-sV0fxo7Ea8YwuzzPBes9cB6PGTMHxh3LouxxKZJTFayn_sqOm6QRcfco0qJl4JtKFkkgL1iEodIsFL1SdhBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
إعلام أمريكي : ‏أفاد مسؤولون أمريكيون أن مدير وكالة الاستخبارات المركزية الأمريكية، جون راتكليف، توجه إلى موسكو، روسيا، في زيارة غير معلنة يوم الثلاثاء، وهي أول زيارة رسمية له إلى العاصمة الروسية. وقد أمضى راتكليف نحو أربع ساعات في موسكو قبل مغادرته.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88531" target="_blank">📅 00:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88530">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd76295dc.mp4?token=SV8IIk0wYM9ubmU1LQPGPttuic40sczTk8ONTngz0CsIn6dFFkVEDGk0d8s8QOb1M4Rly-fy9v147Femp7LO7SQDH0XYhID43jtLYRwi5N_snn7oLZiqSbmxbftAjL5Oybtl1Iux-jxUbLH5AE4O_YB-SEEsVkew-cShiTV_dHM1zS3LEfvKhGu22X_I1Ff6tElcS2NLeElZQakta6r-0lbOYZROvfUUoDwOpYQAAItPIs_vpgGKGvZlCGa6yCo2UoIaozCJGjiUDgH4fmDwoqwoaEc2_akFqKjR1DemI4BVL94Sl2BQt5OFzAaCRfarso270dkRf2ixMAIU__FgjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd76295dc.mp4?token=SV8IIk0wYM9ubmU1LQPGPttuic40sczTk8ONTngz0CsIn6dFFkVEDGk0d8s8QOb1M4Rly-fy9v147Femp7LO7SQDH0XYhID43jtLYRwi5N_snn7oLZiqSbmxbftAjL5Oybtl1Iux-jxUbLH5AE4O_YB-SEEsVkew-cShiTV_dHM1zS3LEfvKhGu22X_I1Ff6tElcS2NLeElZQakta6r-0lbOYZROvfUUoDwOpYQAAItPIs_vpgGKGvZlCGa6yCo2UoIaozCJGjiUDgH4fmDwoqwoaEc2_akFqKjR1DemI4BVL94Sl2BQt5OFzAaCRfarso270dkRf2ixMAIU__FgjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
صفارات الإنذار في كييف</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88530" target="_blank">📅 00:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88529">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
حاملة الطائرات يو إس إس أبراهام لينكولن قد غادرت منطقة مسؤولية القيادة المركزية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88529" target="_blank">📅 00:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88528">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-qz5EeZuTrzkvT4-nFEduJS5HXR6dRuxyevlnoFlzsHW5NSQQ3DZ9ayr491hasZibSEdGWrGq3LQazO-frgH8vqPnSnHXyngfSVVCgMNzWkrlk0TSyGpGPdguOIXTkboANmoI5lLUbelW2S9ME74HYpCDergY3eWBOFPyH_hGeFKqSaxbxguEbVJXVkTgR7Y5YE7k6rx2XYzMRW9FXXQwV-z8i5Vg5dB1YartwDKfVDeYDybGI5-q4_RcT9ZiHmGojJMiopCkiXFMhiyd0IB4yt45eTusd5g6E2aFSKCccbTxT95BKkK_BLlZFsMbNVdFoPOZk53wZ3e4peLMqpRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
المعاون العسكري للمقاومة الاسلامية حركة النجباء الحاج عبد القادر ااكربلائي:
من مهازل الدنيا ان تقوم دولة الارهاب العالمي بازالة اسم اخر من قائمة الدول الراعية للارهاب؛ فالان اصبح الارهاب نفسه فيها دولة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88528" target="_blank">📅 00:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88527">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇦
صفارات الإنذار في كييف</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88527" target="_blank">📅 00:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88526">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGbloc_El7tYML0L1UCeK3WLjLBoBNwZDjo3pklGV3DHNts3KskJjo4KDVOn0_NdmDZXFemNNlPmeImvO1MDjyQqbCTVT9JbOC0FqF3575tGiBdeLrW7ySYi4ti8DJ5FmL6PNj_WjeTofvPOpcQreLSxfPnZZ9C7cFHs5cemGlcMprmutU5g5de5u-AoPCiz0fvC4NDkoQUM-zgRZdDjU4hIjg0L84KEDsb2azSebgWrG0xXnAnBn1JhksuGNgEpjEsPPuvE5hAKsjHdbPLe3AK10mZ2DGgpUGJv3YbSdsmStBvggHqiaCD3GCYmKrJnw65LIXz1iYKXqq6KmSt59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رويترز
: الخدمة السرية على علم بفيديو يبثه التلفزيون الحكومي الإيراني يناقش مؤامرة محتملة لاغتيال ابن ترامب
ناقش مقطع فيديو مدته ثلاث دقائق بثه التلفزيون الحكومي الإيراني مؤامرة محتملة لاغتيال بارون ترامب، البالغ من العمر 20 عاما، مدعيا أنه كان يتم مراقبته ويزعم أنه تم تقديم مكافأة قدرها 10 ملايين دولار مقابل قتله.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88526" target="_blank">📅 23:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88525">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
🇷🇺
إعلام أمريكي :
‏أفاد مسؤولون أمريكيون أن مدير وكالة الاستخبارات المركزية الأمريكية، جون راتكليف، توجه إلى موسكو، روسيا، في زيارة غير معلنة يوم الثلاثاء، وهي أول زيارة رسمية له إلى العاصمة الروسية. وقد أمضى راتكليف نحو أربع ساعات في موسكو قبل مغادرته.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88525" target="_blank">📅 23:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88524">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
المقاومة الاسلامية كتائب حزب الله:
بسم الله الرحمن الرحيم
ببالغ الاستهجان والرفض القاطع تلقينا نبأ صدور حكم جائر بحق مفتي سوريا الشيخ الدكتور أحمد بدر الدين حسون، في خطوة تمثّل استمراراً لمنهجية استهداف الشخصيات الإسلامية التي طالما دافعت عن وحدة الأمة وسماحة الدين الحنيف.
لقد كان المفتي طوال مسيرته رجل اعتدالٍ بكل ما تعنيه الكلمة؛ وقف سداً منيعاً أمام مشاريع التفرقة المذهبية والفتن الطائفية، وكرّس خطابه لإعلاء قيم التسامح والتعايش السلمي ووحدة الصف السوري والإسلامي.
إن مساعي النيل من القامات التي ناهضت التطرف والمنهج الوهابي إنما تعكس الرغبة في إسكات أي صوت يدعو إلى الاعتدال وتجاوز الأحقاد، لا سيما أن الحكم الصدر من قبل سلطة طائفية يرأسها من تلطخت يداه بالدماء، حيث لا زالت الذاكرة تحتفظ بخطاباته الطائفية واعترافاته بتنفيذ عمليات إجرامية بحق الأبرياء لا لشيء إلا أنهم يخالفونه في التوجه الديني، (وَسَيَعْلَمُ الَّذِينَ ظَلَمُوا أَيَّ مُنقَلَبٍ يَنقَلِبُونَ).
المقاومة الاسلامية
كتائب حزب الله</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88524" target="_blank">📅 23:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88523">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الاعلام الاجنبي يتداول:
أفادت مصادر عسكرية باكستانية ومصادر أمنية إيرانية أنه تم التوصل إلى اتفاق لوقف إطلاق النار بين واشنطن وطهران.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88523" target="_blank">📅 23:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88522">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDlCXgSZiP2-WC5nkZTnTHy3p3gN8E9MhCH8HFXQphUrcSTeo0MmGUbn_5pKma9AH3VteFRm2uKK0r9Hulm1U6YDHdITACD4-WtnNRycZLWvvVyWbVR5VTdUci8neHN11-NqEPFYwtF021F9qsWtKWsju983zcCpSfZLAB7hsFNZAUl3_0v1h0eyQSCaNiyU_qw4ht0m9yLPRsFvRIzlG_SHLbe1UTywP1lqOrl_BNH3Np7LP54srAKPZi3TeFL_aCEFom2-EcIuI5HFrhzgLR6tdZtBkSuPgf5q9txAvjJsHLfOOSnA19M8tqe2SRPsZ3v7BpIK3IOacIHv7u40zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي
:
إن التزام إيران بالسلام والاستقرار يقابله دبلوماسية راسخة مع جيرانها. وقد تم التأكيد خلال المحادثات مع الضيوف الباكستانيين والعمانيين على الحلول الإقليمية.
‏يُعد الإطار المقترح للممر الجديد، وإزالة الألغام المشتركة، والإدارة المستقبلية لممر هرمز مثالاً على ذلك.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88522" target="_blank">📅 22:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88521">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR5wM52jj03aUUsHVBWgyHQhVtB4ZFBUjZKiAB7Jjcjf3YbDeLUDEY7yuTUbSRRY8w6Bb3n7lmiVi9sZUsgdArN8gFa5kGVZctHlhFkfY3ngQmnlksUSAD8NbjRM1dd1MHqK45o99J6H_r-v-MGfRXYoi79FTsqyWN5JkWMRLt614Qf-164eEH_DpvbKmji_R7nnz_7TAuZPsuKZqGyh11RAGs74tcDyA4xVx61_DCZkkzQaX6Fu-mrwXizbxOLIHtQNhrxKLjNeBwaa9CBN5C-P1G_pdPo6wjJGgfiiduZgVbqzVN44tzZGzRiOC1w147TEGfaMbaI8pNe76a9lcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليبياف‏
: هو: "يوم النصر الاقتصادي".
‏ثم قال هو نفسه بعد خمس ثوانٍ: "[هههه] لماذا أرغب في تفجير النظام المالي العالمي؟"
‏سيدي، هذه ليست نورماندي، هذه ليلة ارتجال وقد نسيت نصك الخاص.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88521" target="_blank">📅 22:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88520">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇹🇷
‏وقع زلزال بقوة 4.2 درجة في أديامان جنوب تركيا.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88520" target="_blank">📅 22:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88519">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99461fe9fa.mp4?token=MwE3gENHQQ6LQX2-TbsE9Oga-2AjFjuGURNBg9kZtl_rEBO_m-JkB_j5c2z91jFDaNLK-_RN5BFBZHxrFjkM5ElvJ4va1rwqGO0FgGnOWPC3vwtCneD4IBW-PtNaKAFngq3Zb_rTKRXPLnFU4NEfdjlW5jjLgpK3B76PPrdXSCLSac1RWyzmNwq0A5L4IMTv7NFi-CY4Xwx8vQ16-9iX4LfnYznTkB8M89sn49ovfNQ6Whw5lEnm1tlp6u5f4hjURGS-GOemukDIawFOajj3nancpIh80tvm1edhNvqkCX82BkEx4O1nZXLHvA2u9DvTu_qqco91LHJuvmc3L41l3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99461fe9fa.mp4?token=MwE3gENHQQ6LQX2-TbsE9Oga-2AjFjuGURNBg9kZtl_rEBO_m-JkB_j5c2z91jFDaNLK-_RN5BFBZHxrFjkM5ElvJ4va1rwqGO0FgGnOWPC3vwtCneD4IBW-PtNaKAFngq3Zb_rTKRXPLnFU4NEfdjlW5jjLgpK3B76PPrdXSCLSac1RWyzmNwq0A5L4IMTv7NFi-CY4Xwx8vQ16-9iX4LfnYznTkB8M89sn49ovfNQ6Whw5lEnm1tlp6u5f4hjURGS-GOemukDIawFOajj3nancpIh80tvm1edhNvqkCX82BkEx4O1nZXLHvA2u9DvTu_qqco91LHJuvmc3L41l3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مظلوم عبدي يعلن حل تنظيم قوات سوريا الديمقراطية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88519" target="_blank">📅 21:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88518">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
ضبط 36 كغم من حبوب الكبتاجون وإلقاء القبض على المتاجرين بها، بعد تنفيذ كمين محكم أسفر عن الإطاحة به بالجرم المشهود.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88518" target="_blank">📅 21:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88517">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52c9cb6e3.mp4?token=WYFJbn21G5jzcCWap4uboDypNW9F9CuFrfPrgwakTWJKVebFFKK8eNLMqPlgt1asklKEy_OaqRm74IJEWJw9cl-VZI02TMKnr9AQQWFkwfUqFFgrH7gf6WRQN4o3gM0AGnBMqzE2Gch_RNhE4haAx0o0mj8sdVSZZ90TlcstdWCxe0gJOq1KxCWIRHsomihFqczn9OwhiuV4U-wxloNNCf7njOZ56O4Xzg15m4Fd2T3G7LJzXdHEkcD3XQdpna4VhKY0kRgIjp3pZO8Nj8vDrzKv5U2EMVJ9r-CdhRo9SXMdP50nWrlXjmy0QiGquMcLcAkf8tUehEQ0YiozkjH_joWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52c9cb6e3.mp4?token=WYFJbn21G5jzcCWap4uboDypNW9F9CuFrfPrgwakTWJKVebFFKK8eNLMqPlgt1asklKEy_OaqRm74IJEWJw9cl-VZI02TMKnr9AQQWFkwfUqFFgrH7gf6WRQN4o3gM0AGnBMqzE2Gch_RNhE4haAx0o0mj8sdVSZZ90TlcstdWCxe0gJOq1KxCWIRHsomihFqczn9OwhiuV4U-wxloNNCf7njOZ56O4Xzg15m4Fd2T3G7LJzXdHEkcD3XQdpna4VhKY0kRgIjp3pZO8Nj8vDrzKv5U2EMVJ9r-CdhRo9SXMdP50nWrlXjmy0QiGquMcLcAkf8tUehEQ0YiozkjH_joWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇮🇱
رئيس تركيا أردوغان حول إسرائيل وسوريا: نحن لن نتوقف عن دعم جيراننا لمساعدتهم على النهوض، لمجرد أن الشبكات الإجرامية التي لديها دماء الأبرياء على أيديها مستاءة من ذلك.  السياسة الخارجية لهذا البلد يتم تحديدها حصريًا وبشكل كامل من قبل الشعب التركي.  لا يمكن…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88517" target="_blank">📅 20:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88516">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c8b533d3.mp4?token=fQsgGp9yd8nNkyEwpFILO778kxUxjO6HAJ9hhoUNHEy3c_VaFe_SJWJbGrwGZ-xEImXt5BmyZQ3H-cw7BulPnzGniRVrTXRx_K5vQ4dAeTJPnIzLQ915cwVbe5DIJDaoQ2yD0qkasEVjH2LPXalIepmYILX4urDc_wiRzUO125OgWIeOr53JV334qrGYQ6Lenqtr0_rMHjlebPrtKzL9lW2Do5gWplqmHgOtvPqlrm3xAJvl0JOMyPiOQSoE360xk0UT9s8k5RIwm52xNcKsGz2_-vi4GwK2Psjzr-fy1lmepF53HqcyXGRQYyN_SsF8YHfDfjHSnv9hqUNyhWUwCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c8b533d3.mp4?token=fQsgGp9yd8nNkyEwpFILO778kxUxjO6HAJ9hhoUNHEy3c_VaFe_SJWJbGrwGZ-xEImXt5BmyZQ3H-cw7BulPnzGniRVrTXRx_K5vQ4dAeTJPnIzLQ915cwVbe5DIJDaoQ2yD0qkasEVjH2LPXalIepmYILX4urDc_wiRzUO125OgWIeOr53JV334qrGYQ6Lenqtr0_rMHjlebPrtKzL9lW2Do5gWplqmHgOtvPqlrm3xAJvl0JOMyPiOQSoE360xk0UT9s8k5RIwm52xNcKsGz2_-vi4GwK2Psjzr-fy1lmepF53HqcyXGRQYyN_SsF8YHfDfjHSnv9hqUNyhWUwCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
وزير الحرب الصهيوني في سوريا:  لن نتحرك من جبل الشيخ ومن المنطقة الأمنية ما دامت هناك تهديدات جهادية على إسرائيل. الرسالة إلى الرئيس السوري واضحة - عندما تستيقظ صباحا في القصر بدمشق، وتنظر إلى الأعلى نحو جبل الشيخ وترى الجيش الإسرائيلي - فأنت تعرف أننا…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88516" target="_blank">📅 20:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88515">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rh2HPRHew9mfH1OVVJA0FvbHO6i33By-mfCEZ88LxgxwX7eKrqKP9KQJk-RR6mwB6T2P7k65n0BdepkG5ytUkNBnUCprQBcmqFswFNAy1ZPtu1kriUCs9foY9T6izmjFCI48tjpN8QPMtKyonfp6oP-HXF58liveh5Ani6Qq5TxoOPskNlErHxLqY5p2J8MI_SaTrADx4GvdS7NAtLJCOV2nP9bdNnNPvD1gJPmnLY6L6LNqLEBEdNOAsALMD4cLAPt_ymOApOiFtEM-fvKcOOjOmvzxd711wUqJdlnBH6DfrHTTVakdEeR1ZvbQGeL70FN4RwvpQVWlBn86xgCfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يعيد نشر تقرير
: أمريكا على وشك تحقيق ثروة طائلة في منطقة الشرق الأوسط والخليج.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88515" target="_blank">📅 19:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88514">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇱
وزير خارجية الكيان:
سنطرد ممثلي هولندا من مركز الدعم الدولي لغزة بسبب تحركات حكومتهم المعادية
لإسرائيل
.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88514" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88513">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFoKDIZq9E9tYx4Yz2iGpGxbTJucUUkCJAycw9E18i4grHC5IHG_Z-lpnqCCn32d3jJg7gRbByCmCU2eV_JXySNWNS7ct5cnxyymm9BW2CnfmTqJeNmBsmfTKqV_9z7NqeBnp4bjBraee9-c0VZ_QGq3GLbrbEmLznFSwFfvBs0z7SfbVMxuNBOnzT-NXHxDXoJPggGa3EZpP7pwe6Rk73jQnvR8m3hFHEiCPMpypnkKQHYjOPCvlzK7TSAoDLYW5FeSjekpw6S0v7VXIGeILO2BncwKAR4oXLDB0wDGI-FZPNYeuhQZmSZBZwzg8HrQfnYxS6l-Ug0jqxuA7RejKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇮🇷
بيان ايراني عماني مشترك
:
أجرى معالي السيد بدر بن حمد بن حمود البوسعيدي وزير خارجية سلطنة عمان مشاورات بناءة مع نظيره الإيراني الدكتور السيد عباس عراقجي خلال زيارة العمل التي يقوم بها إلى الجمهورية الإسلامية الإيرانية.
ركزت المشاورات على الأهمية التي يوليها البلدان لاستئناف الملاحة الآمنة عبر مضيق هرمز مع الحفاظ على سيادتهما وحقوقهما السيادية. وناقش الوزيران إطاراً مرحلياً من شأنه أن يوفر أساساً عملياً وقابلاً للتطبيق للمضي قدماً، في ضوء الوضع الراهن في المضيق، الناجم عن الحرب الأخيرة وتداعياتها الكارثية.
يتضمن الإطار المقترح إنشاء ممر ملاحي مشترك مؤقت عبر مضيق هرمز، واتفاقية لتنفيذ مشروع مشترك لتطهير المضيق من الألغام. وستستمر المفاوضات الفنية بين الجانبين بهدف الاتفاق على ممر ملاحي دائم، وإدارة المضيق مستقبلاً، بالإضافة إلى آلية لتبادل معلومات إدارة حركة الملاحة، وتوفير الخدمات البحرية والأمنية اللازمة.
وفي هذا الصدد، أكد الجانبان على أهمية إجراء محادثات مشتركة مع دول المنطقة المطلة على مياه خليج فارس. كما أكدا على ضرورة الالتزام بالقانون الدولي المعمول به واحترام الحقوق السيادية للدول الساحلية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88513" target="_blank">📅 19:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88512">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYbXUr1O-RD6h3DQo5nR0e3GP-a6_5fBfq7nghfiRkDe0b0wJPZdVAi1pgvqWyAFuNA0iMyXC8zbM6dTJ0nCo5G-cd0m1tSFyhVLm-4PCA2Prdrm_HdYHm2da0APHtWga6no21J4Cw1ukKmdjLHTyaXTclR89mO6-VLBTH7gplriiigjVOPdNkaExx4ha1qMecO4qQP2wUuDXQLLBWa9EPWe-uU8WC4vvcuczZ4RaEwJlyqikJDh49E0s7ysKVcBX4afg1XxEnalRSlT-cuLKSahRPFmgdhBzfN4Ogr_VYtFpFOwSzODFNGbH2f1YEWciURIg6216loAXfWYIaPPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
المتحدث باسم الخارجية الايرانية
:
‏
الولايات المتحدة: "يوم النصر الاقتصادي".
‏أولئك الذين يفضلون الظهور بمظهر "الخاضعين كالظلال" يقولون: "هذا جيد".
‏لكن انتظر on. هذا ليس جيداً على الإطلاق.
‏عندما يعلن أحد المتنمرين أن على كل بنك وشركة وميناء وحكومة أن تختار بين إطاعة أهواء واشنطن أو مواجهة الانتقام الأمريكي، فإن الأمر لم يعد يتعلق بإيران فقط.
‏يتعلق الأمر بتدمير أهم القواعد الأساسية للقانون الدولي وميثاق الأمم المتحدة - أي احترام المساواة السيادية وحق تقرير المصير لجميع الدول.
‏لن تقبل أي دولة محترمة تقدر سيادتها ومصالحها الوطنية بتطبيع مثل هذا الفوضى العارمة والتنمر الممنهج.
‏تُعد كندا من بين الدول التي بدأت بالفعل في استيعاب هذا الدرس...</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88512" target="_blank">📅 19:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88511">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f3771f51e.mp4?token=EBUjr6oN3uLXkQeWgNY4tc0X1H9N02rNsKG76Qcps3hNrAxwkcye3f_m7Zm9NDSR2nczwLi0lACm1f8nbNPZIzZpJkQe6opnAenworbOtCVEzeXfRJWSeN9rpdgWtGGWYZ_bamh1Fx8NeVImLL5Gthb4m4v2yARBgUrDy7YdPd9p3DrTuy6g_oib8FrtgLRqOY2T9YCvnZOTTFJsDacUfAIQBGvp95tYeW1mH6gkdfobL1xMh5GYknag2aEVLZf5tcFE_wZiIW5Fw78U9ei3biGFViqIyVtVfcQJ0X2m5d-1pIxHvo2xD51-0DrhRiX3ER5V2cT0eGH9jKrHmE5eDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f3771f51e.mp4?token=EBUjr6oN3uLXkQeWgNY4tc0X1H9N02rNsKG76Qcps3hNrAxwkcye3f_m7Zm9NDSR2nczwLi0lACm1f8nbNPZIzZpJkQe6opnAenworbOtCVEzeXfRJWSeN9rpdgWtGGWYZ_bamh1Fx8NeVImLL5Gthb4m4v2yARBgUrDy7YdPd9p3DrTuy6g_oib8FrtgLRqOY2T9YCvnZOTTFJsDacUfAIQBGvp95tYeW1mH6gkdfobL1xMh5GYknag2aEVLZf5tcFE_wZiIW5Fw78U9ei3biGFViqIyVtVfcQJ0X2m5d-1pIxHvo2xD51-0DrhRiX3ER5V2cT0eGH9jKrHmE5eDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعداد كبيرة من ميليشيات البرزاني تدخل قضاء خبات ضمن محافظة اربيل لاقتحام منازل الهركية</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88511" target="_blank">📅 18:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88510">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">زلزال بقوة 4.9 ريختر يضرب افغانستان</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88510" target="_blank">📅 18:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88509">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇱
🇸🇾
وزير الحرب الصهيوني في سوريا:  لن نتحرك من جبل الشيخ ومن المنطقة الأمنية ما دامت هناك تهديدات جهادية على إسرائيل. الرسالة إلى الرئيس السوري واضحة - عندما تستيقظ صباحا في القصر بدمشق، وتنظر إلى الأعلى نحو جبل الشيخ وترى الجيش الإسرائيلي - فأنت تعرف أننا…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88509" target="_blank">📅 18:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88508">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇨🇦
🇺🇸
‏
كندا تصعد الحرب التجارية مع امريكا
- كندا تفرض رسوماً جمركية تتراوح بين
15% و50%
على منتجات أميركية بقيمة تقارب
20 مليار دولار
.
- كندا تضاعف الرسوم على
منتجات الصلب الأميركية
من
25% إلى 50%
- الحكومة الكندية تعلن عن حزمة دعم بقيمة
7.5 مليار دولار كندي
لمساعدة الشركات والعمال المتضررين من الرسوم الأميركية الجديدة</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88508" target="_blank">📅 18:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88507">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c487d787a0.mp4?token=GjRekhwx3-dsikvc3rapLyKNL3ITYq2tUBK9weEUPadrT1oBMzAxbuPw7mjaWjiuasexaV-UI0MsFPyvlb0oieEX4MFPQpgrtQijQ3I1mt1_PRfDqwnL4eRvVIq2TX2OAA5WNwAzkNIH8gpwuc7EGhtwoYwmh9my-6DavbtZ1IW8GyfkZbv4BNKsUex02hSQKxYZd2j_TfRi5tNjuLW_hF6pL-KNdoC8kmJK_0nVQpUc8gpQExxbLhXZHKF7XPRDLzRxJYMNnUQ9BnqwpAQOh14CDJFYRNA19D2G_XHTjY85xVhFKM4dpupH0mZAcJ8ThC22QaaWAwwJ6hNtCzGhm4PxyKqbaDeYKNW1gUod2TyacHVj6Xwj-sKayPJEjGwAdZaL3OAI_8H87qW7bwfJzR6gFbC5i_-MUCQxLVnomLr20e0MKFL0WlW6Q5htv3chZcrz8htNx1KUC9Rt27EHzeVOl4DuGoWgvwxHcp6lkqSzkIFbDqnI2Qf8XWkFf8MnHtUFpAt4S2-goYXzjudEbDqeiHHP3Yhn96mJS_C6rWeB1gWJS0f1TVBRUlApToO6LZ_MaDamwSShVz9RZsjZF_rxZjYjhub44NH00uFUwKyb54MN86JeydHZJyYteiTwHYbEyvkoUKD5UQyGM8NoEsy830gBUeAJr6Ti6k4r3jE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c487d787a0.mp4?token=GjRekhwx3-dsikvc3rapLyKNL3ITYq2tUBK9weEUPadrT1oBMzAxbuPw7mjaWjiuasexaV-UI0MsFPyvlb0oieEX4MFPQpgrtQijQ3I1mt1_PRfDqwnL4eRvVIq2TX2OAA5WNwAzkNIH8gpwuc7EGhtwoYwmh9my-6DavbtZ1IW8GyfkZbv4BNKsUex02hSQKxYZd2j_TfRi5tNjuLW_hF6pL-KNdoC8kmJK_0nVQpUc8gpQExxbLhXZHKF7XPRDLzRxJYMNnUQ9BnqwpAQOh14CDJFYRNA19D2G_XHTjY85xVhFKM4dpupH0mZAcJ8ThC22QaaWAwwJ6hNtCzGhm4PxyKqbaDeYKNW1gUod2TyacHVj6Xwj-sKayPJEjGwAdZaL3OAI_8H87qW7bwfJzR6gFbC5i_-MUCQxLVnomLr20e0MKFL0WlW6Q5htv3chZcrz8htNx1KUC9Rt27EHzeVOl4DuGoWgvwxHcp6lkqSzkIFbDqnI2Qf8XWkFf8MnHtUFpAt4S2-goYXzjudEbDqeiHHP3Yhn96mJS_C6rWeB1gWJS0f1TVBRUlApToO6LZ_MaDamwSShVz9RZsjZF_rxZjYjhub44NH00uFUwKyb54MN86JeydHZJyYteiTwHYbEyvkoUKD5UQyGM8NoEsy830gBUeAJr6Ti6k4r3jE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ميليشيات البرزاني تواصل اقتحام منازل الهركية في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88507" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88506">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رئيس الوزراء العراقي يوجه باعتماد البطاقة الوطنية الموحدة في الانتخابات المقبلة</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88506" target="_blank">📅 18:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88505">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Miso-kUg5ooDHV8ydWmd8n2bULKiBSUB3wcOmpS6p4a_p6Fyl-J6ozjG5mEZkLKS0_sdVR-6OiXeLk9eFTiV32-rDh6H9rs8IV74l9b0RFPo9gk30WvtGDK81eSc1CdbMaFYcSrNK4mag43ZF76lr5HwEcE0CIw1AJoFSMlTdLHgM-59DLiT_SY5BEcLcjAkVXpNjSOfQnrpV7jR12laB5fkryKF-8UaEyxOKQb_qpyVUO44vswaMi8caf9Zd64blagGsDnr68tO9_-nnRqECRzeKIaNTncmg61MD9o3flIHE2ikqHeNbRKT8hMDJtoS2awoDKes92Vdqx-eUYCn_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
ترامب يزعم:
لقد أُبلغتُ للتو من قِبل البحرية الأمريكية بإزالة جميع الألغام و/أو تفجيرها في المياه الدولية لمضيق هرمز. وقد تم إخطار إيران بأن أي سفينة أو قارب يزرع ألغامًا جديدة سيتم تدميره فورًا وبشكل منهجي. ومن خلال قوة الفضاء، نراقب كل شبر من المضيق، كما نفعل أيضًا مع موقع بيك آكس ماونتن والمواقع النووية الثلاثة الأخرى التي تم تدميرها بالفعل. هناك سياسة عدم تسامح مطلق مع زرع الألغام سارية المفعول بالكامل.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88505" target="_blank">📅 18:03 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
