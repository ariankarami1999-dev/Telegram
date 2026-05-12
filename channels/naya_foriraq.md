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
<img src="https://cdn4.telesco.pe/file/pMPxmvEYW3MA10h5wfjcznt9GhhcXmnfsQdF5zF6uzIH_7A8-FuwKMAgHMdGimui_4uItFLvZROoritSs_YTKm8XYKFCzamWZF9L9v_6JK6xiYBJ6ETsDzkowSIXW8p59MlF-TSOIKa3CmcNBN80eh7Bj1EMJXXpTlpOD3_H7UOykJjiFGPHWhtANTvEi-1e67PgZn1RYZEdFSV55iOVyIO7H_G3oNiDzf5J8F-qEWR9bNW4PLVbSGRSCKJT2Br6SO9iary3Mi12h8gl5qbPJzUB4XR9eeAaui4hZyqgcRfxA1uDMSo1NcPcL39NrcGRymjEY8QCeU3oxelmysmQxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 03:22:36</div>
<hr>

<div class="tg-post" id="msg-75278">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e582f4652d.mp4?token=IQ3Vn3xDKWZMpGV-tCJYCD_eW9M6ZZ9K14cO9JXRj7jB5v-woxMN3TT_HDV8bL1sGpnGbnOFQzhjO1wO9shLrQFkbt1S0jIzp5XU9mQJXuwYSt460KAdIT1fM-2r052yjdE0cSmUYXsHaTuJ0wXFma5lKXLdcJ6qwc-ex_yXVPBhlsjeTvurCoOmUvmMojLhHdZCcfES8sBKoT5ajHgABacGzLr5so3e-uMi-x2j2aBlyX6HC-2vpZLnSzIKCTWbAiFBhr8cA-2DRibcZNnFzn2ZSzxD653nXUC1FVdqxWD4CECgHLRr4DbgVQ3VF37YG7MpEjRxoGrPsKQiHnUI-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e582f4652d.mp4?token=IQ3Vn3xDKWZMpGV-tCJYCD_eW9M6ZZ9K14cO9JXRj7jB5v-woxMN3TT_HDV8bL1sGpnGbnOFQzhjO1wO9shLrQFkbt1S0jIzp5XU9mQJXuwYSt460KAdIT1fM-2r052yjdE0cSmUYXsHaTuJ0wXFma5lKXLdcJ6qwc-ex_yXVPBhlsjeTvurCoOmUvmMojLhHdZCcfES8sBKoT5ajHgABacGzLr5so3e-uMi-x2j2aBlyX6HC-2vpZLnSzIKCTWbAiFBhr8cA-2DRibcZNnFzn2ZSzxD653nXUC1FVdqxWD4CECgHLRr4DbgVQ3VF37YG7MpEjRxoGrPsKQiHnUI-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مظاهرة إحتجاجية ضد نظام آل خليفة ،رفضاً لإسقاط الجناسي عن العلماء والمواطنين في البحرين.</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/naya_foriraq/75278" target="_blank">📅 01:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75277">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKIFRYj0xa0T3quG0eS8KuuN4sw80G_39Dl_5reO_9ZUxYyR8SumAtQwGaSlx6zjI-w-K0y3YHETSekZNciHftv4Wkuz_MEhNKgtaLugbcu7L5ryRQ3qW9N5pg-7XD1xHAZqNlaihWKWFmkFvPtMRihNnXH3ACKYSgv3Ru1cuUUrzcP1hXXjiJ3d7XL3nomo916c-qpz_1dz8kO-HZc2NErtzxR1k51yfRk-lKXmXVp3qyNMoKSARKL0mHWIVwZ0PxfGG_E1k6K4IZu2unzWsFD9LV7pNYlacxyqXRVS5zBJvrDw262vHkhMjk7hs61LZwpI2ZbD5bpgQNDYAfjJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
عندما تقول الأخبار المزيفة أن العدو الإيراني يبلي بلاءً حسناً، عسكرياً، ضدنا، فإن هذا خيانة فعلية لأنه بيان كاذب، بل سخيف. إنهم يساعدون العدو ويحرضونه! كل ما يفعلونه هو إعطاء إيران أملاً كاذباً عندما لا يجب أن يوجد أي أمل. هؤلاء جبناء أمريكيون يخونون بلدنا. كان لدى إيران 159 سفينة في بحريتها - كل سفينة واحدة تستقر الآن في قاع البحر. ليس لديهم بحرية، وقد ذهبت قواتهم الجوية، وذهبت كل التكنولوجيا، ولم يعد "قادتهم" معنا، والبلد كارثة اقتصادية. فقط الخاسرون والجاحدون والحمقى قادرون على توجيه انتقادات ضد أمريكا!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75277" target="_blank">📅 23:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75276">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭐️
هزة أرضية بقوة 3.4 ريختر تضرب العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/75276" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75275">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cdd385b3.mp4?token=VQ9TxjV-H6K_EQrlLUxie4FyMgwADH6KYHVEGpebKlfwgS5rKNtgLeky7Q8vuO6sfxzMGxsi_NyguVlqL9icdWi0fIp0hOLriLfpdUVBnYHztCympN23uIc90XVc7vBcCKfnZesEusoNtwhuMa1Fthd4tLUInD7EDbIF4BiXBXwrPJKzzJ6lGkcpYMXuzZ0XabaWCMO3_Y75DVeNE42n0GxS2Cz2QfX70mFKzGnlbBeZV8MJBT6BnH0WGhiZuppRc-9bGwkhajlqmzlwE7D2OlfWYoDasoxW3P39OkQLuzWJuMuI4vtet7WVQ7Tyd03Vbx4kNnNv_kL4z4yz6DVWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cdd385b3.mp4?token=VQ9TxjV-H6K_EQrlLUxie4FyMgwADH6KYHVEGpebKlfwgS5rKNtgLeky7Q8vuO6sfxzMGxsi_NyguVlqL9icdWi0fIp0hOLriLfpdUVBnYHztCympN23uIc90XVc7vBcCKfnZesEusoNtwhuMa1Fthd4tLUInD7EDbIF4BiXBXwrPJKzzJ6lGkcpYMXuzZ0XabaWCMO3_Y75DVeNE42n0GxS2Cz2QfX70mFKzGnlbBeZV8MJBT6BnH0WGhiZuppRc-9bGwkhajlqmzlwE7D2OlfWYoDasoxW3P39OkQLuzWJuMuI4vtet7WVQ7Tyd03Vbx4kNnNv_kL4z4yz6DVWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
دبابتي ميركافا تابعة للجيش الصهيوني (8 دبابات خلال اليوم) تم إعطابها من قبل الأبطال في حزب الله بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75275" target="_blank">📅 23:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75274">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee72acfb5.mp4?token=OxMAl9QRmLtjYmlOeSGnHJ-Sf3P22jmKK9pJZCppbR8gwVN8tgy5zNmnyN1JCSTeNSs1RO10Q1GLOk0xaXxuwgshVub9lWWv_ofgJwM_sqGUtBK-x66kYWMoY2Xa5rEGNn0560ujHMbl1rBW4jACeyPtH_K7i6KZ5GDgG_mj_eL7pUdmCqckVWgVBcpIYfsPdLFApHXt97PLvc_BOXlNGg_WyKZYsqSaPLOJQCofdj2irsFDUEFsWnp1Y-pDm_t4HG0cFYD9D69QYhm2W5CPYpenH1evMDpDtLndVZdBACyz83b2BuuYD_f8R-pmqByKatsknBlcxuRQCQIwoGQcHaAJiBOcaCOXHX1mDTS0c2CLhZ-2WFfnQSKz7lVDf8oldt4QxQjR694qcjDquIGUEBaHPdwWj7_ERwe_C0aPUBS7hnG21fohYqchQ3MpCaUrJfEKNxaHtUwZDN6IwmEW7S-L6jcpt9nBg3XFugsXM-zSamt2vFA1tjRCZyGYeF0DF7PBoWuIs3UPJNFDWtlUtAsuSr23KVrCc4EJLMgSR08ikovCqctQaGwL5-6pj6Pe01P2WkDWiSDCg9zEswjRevvOTxTjEREmogwu5rKd5A4f0L838c_PtblNbw_WPmTj_QkZg1xAIICCFKmJAfL2n7mayVtYZUGuPxyRNcxrvUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee72acfb5.mp4?token=OxMAl9QRmLtjYmlOeSGnHJ-Sf3P22jmKK9pJZCppbR8gwVN8tgy5zNmnyN1JCSTeNSs1RO10Q1GLOk0xaXxuwgshVub9lWWv_ofgJwM_sqGUtBK-x66kYWMoY2Xa5rEGNn0560ujHMbl1rBW4jACeyPtH_K7i6KZ5GDgG_mj_eL7pUdmCqckVWgVBcpIYfsPdLFApHXt97PLvc_BOXlNGg_WyKZYsqSaPLOJQCofdj2irsFDUEFsWnp1Y-pDm_t4HG0cFYD9D69QYhm2W5CPYpenH1evMDpDtLndVZdBACyz83b2BuuYD_f8R-pmqByKatsknBlcxuRQCQIwoGQcHaAJiBOcaCOXHX1mDTS0c2CLhZ-2WFfnQSKz7lVDf8oldt4QxQjR694qcjDquIGUEBaHPdwWj7_ERwe_C0aPUBS7hnG21fohYqchQ3MpCaUrJfEKNxaHtUwZDN6IwmEW7S-L6jcpt9nBg3XFugsXM-zSamt2vFA1tjRCZyGYeF0DF7PBoWuIs3UPJNFDWtlUtAsuSr23KVrCc4EJLMgSR08ikovCqctQaGwL5-6pj6Pe01P2WkDWiSDCg9zEswjRevvOTxTjEREmogwu5rKd5A4f0L838c_PtblNbw_WPmTj_QkZg1xAIICCFKmJAfL2n7mayVtYZUGuPxyRNcxrvUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
09-05-2026
آلية "هامفي" اتصالات تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75274" target="_blank">📅 23:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75273">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌟
🏴‍☠️
دبابة ميركافا صهيونية تحترق بعد استهدافها في موقع العبّاد بواسطة محلقة انقضاضية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/75273" target="_blank">📅 22:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75272">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6LSRaKo8u1Li1YH8RT33Kte4bnVSf-4monLtrMogk4htDib76sLJIQbNa0kKXYTD3t4JtRSZBPzqp6kncwSstNIWXx49aVTrIPzVG9XJOPIzptXAP9aqU_JNfmJLJPcnQKngE2yuaB2aTukAn9Z-y_HJsPJmQcdWRuRy3jnqxh7RsuWBqtMDOsIxNIO6lUawHPjvNc26ZTgEES4v_yblhaBsP5geqgydaCiPk3B_T-4a3KaLAx2VHalmqrSvHPk7v6hRC4QX-02j52GYR5pAse9bBAsDjYXqik_QkDKCSdg_qc0XspKMlc59fHZcQGxIBBm84z9XJwzCJDn2pJ6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في خبر غير مهم  وزارة خارجية دويلة الكويت تستدعي السفير الايراني وتسلمه مذكرة احتجاج</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75272" target="_blank">📅 22:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75271">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
🏴‍☠️
استهداف دبابتي ميركافا للجيش الصهيوني في بلدة الطيبة بجنوب لبنان من قبل أبطال حزب الله.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/75271" target="_blank">📅 22:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75270">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭐️
رويترز:
العراق وباكستان أبرما اتفاقيات مع إيران للسماح بشحن النفط والغاز المسال من الخليج الفارسي.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75270" target="_blank">📅 22:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75269">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792b04ea24.mp4?token=sN35FGdEW0AuDLGTxd3Ybn7TAMLoqWdMzW4MgvzcoFGaqyEz3bMVqrymv0O76mxzUCfKiUMMJQgx8GtRUspVJ_bJsIXuCXwbAGzHyzi8GwhdCwtb4zOKqNjzqGXwqD2jt7JsfgVm_Ivh4f2e0L86-cnGcWrLRNFqoh-D2InL_hiqGSVWMpMVHPkgoIShvKZy4-HT2Afb1obxp1Yvy7jTssgI7YidV2OQfxuKpI5mJFgxUDxsMSJNzacK625c_mi2K4db26do6mp2xMuwURckjuwsTIuN-74Xz-on5Ug5cFePFIJTtFl_XWS_W_FFL4ch5c6J1OIslw9caZbPSeWCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792b04ea24.mp4?token=sN35FGdEW0AuDLGTxd3Ybn7TAMLoqWdMzW4MgvzcoFGaqyEz3bMVqrymv0O76mxzUCfKiUMMJQgx8GtRUspVJ_bJsIXuCXwbAGzHyzi8GwhdCwtb4zOKqNjzqGXwqD2jt7JsfgVm_Ivh4f2e0L86-cnGcWrLRNFqoh-D2InL_hiqGSVWMpMVHPkgoIShvKZy4-HT2Afb1obxp1Yvy7jTssgI7YidV2OQfxuKpI5mJFgxUDxsMSJNzacK625c_mi2K4db26do6mp2xMuwURckjuwsTIuN-74Xz-on5Ug5cFePFIJTtFl_XWS_W_FFL4ch5c6J1OIslw9caZbPSeWCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يغادر واشنطن متوجهًا إلى بكين في الصين.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/75269" target="_blank">📅 22:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75268">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a470cd8205.mp4?token=ZFqGmhhBpl9u-bMG9Qqz1esUgJo6e-K6dmklUjjNPHHUbjjBmXp0jaFjDYTmib3jTtT4cIIR0TqpszWgtHwNLiqEd3K10XpcuQilsNz3vcqakJVD4reU-TY9QN_JDYz-An5wxrLcCIvzWtKeZqwBene2gd7DpoM7XXR05Xw9oTC4jbekxg2y-UiJV6TkBpxOYTcUCFLfQ4tzaMbXV6wa2yD0SxRKz-f-4vD7JpeAYShdiQmFVxeW0GqOQby05LHYT1cFzCycQ709Tnx5qkB6p7Rfhkt1Y0obFKGYc0P8iSh9U5ADL56aWGg66Oh4ZsM7uaM-Sc0AbaT2in7OCNICfIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a470cd8205.mp4?token=ZFqGmhhBpl9u-bMG9Qqz1esUgJo6e-K6dmklUjjNPHHUbjjBmXp0jaFjDYTmib3jTtT4cIIR0TqpszWgtHwNLiqEd3K10XpcuQilsNz3vcqakJVD4reU-TY9QN_JDYz-An5wxrLcCIvzWtKeZqwBene2gd7DpoM7XXR05Xw9oTC4jbekxg2y-UiJV6TkBpxOYTcUCFLfQ4tzaMbXV6wa2yD0SxRKz-f-4vD7JpeAYShdiQmFVxeW0GqOQby05LHYT1cFzCycQ709Tnx5qkB6p7Rfhkt1Y0obFKGYc0P8iSh9U5ADL56aWGg66Oh4ZsM7uaM-Sc0AbaT2in7OCNICfIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: أنا من سيعلن عن نهاية الحرب مع إيران.  يمكنني أن أنسحب الآن لكنني لا أريد ذلك بل أريد إكمال الأمر تماما.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75268" target="_blank">📅 22:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75267">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⭐️
رويترز:
شنت المملكة العربية السعودية سراً ضربات جوية انتقامية على إيران في أواخر مارس بعد هجمات متكررة بالصواريخ والطائرات بدون طيار من قبل إيران على المملكة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/75267" target="_blank">📅 21:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75266">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭐️
هزة أرضية بقوة 3.4 ريختر تضرب العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/75266" target="_blank">📅 21:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75265">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الصهيوني:
إصابة 190 ضابطا وجنديا في معارك جنوب لبنان خلال الأسبوعين الماضيين.
مقتل 18 ضابطا وجنديا وإصابة 910 منذ تجدد القتال في جنوب لبنان مطلع مارس الماضي.
إصابة 114 ضابطا وجنديا بجروح متوسطة و52 حالتهم خطيرة.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75265" target="_blank">📅 21:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75264">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية: صحراء النجف الأشرف تخضع لسيطرة كاملة من قبل القوات الأمنية العراقية.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75264" target="_blank">📅 21:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75263">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
ترامب: قضينا على الجيش الإيراني.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/75263" target="_blank">📅 21:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75262">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
ترامب: قضينا على الجيش الإيراني.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/75262" target="_blank">📅 21:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75261">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">أنباء عن إنفجار في مدينة صنعاء اليمنية.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/75261" target="_blank">📅 21:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75260">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp9ubC3dnspd18nZaJGbot1MN_yXw11fX4aqLJHIOnZ2WwPYtocnL7LMpfqPqsNTlLkxXIjG9RHAGV-q6AmKdrrsHzBAmwLdrzRXXYpSmq_rvfcoqNGL57eQI6OdmKk9ZsJh-X7iu0fQZGLseOxce4tfFJX6gd7xtqF_MUHDS1sFNZH-Db90lzhA_k8umUBIV9bT_FK6uis44peEOjt3yQHawfCWkw0q3gBGtwLP1QRDYXpQxLH3X75Srqe9T5ARK5E2b0lGFns8WjsmmbgBySGQrL8Xsts8rbbOGAU11c-bMXeTM4OrWR4mBEG-nayU6eGwPf1u2uSYzJ6qug9K_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: لن نبرم مع إيران إلا اتفاقا جيدا.  ‏ لا أعتقد أننا سنحتاج مساعدة رئيس الصين بشأن إيران.  حلف النيتو خيب آمالي ولا نحتاج إلى مساعدة منه.  لا أعتقد أننا بحاجة إلى أي مساعدة بشأن إيران وسننتصر بطريقة أو أخرى سواء بشكل سلمي أو بغير ذلك.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/75260" target="_blank">📅 21:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75259">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khjqhpd00Li0J860CS5JXlh6kWf02UQ29URcl4OYzSgtbSuhT0ZnSjahbJKFiQh6KCsL49BczU_0DTkUbvAdBxlN1Fp7CQRDtj7pJS17jaXk3r6KpludJjIiwz7YJZ0k0DzDAElWaCQ60MS-SiwiqxCtXSxTNup0o_pDia7pmWtZYPv2zC6m0d4EHHqWXGhsvzoidS95dFtFFkMVkRu0oCo_WjhV7WZftP_0fA0Q3Xd25qT59WRv8qH25iDJpjoJQo6sz1kGdss-TdDpz_Y7HgW8NVtaEF-NIGECyJzE2us7_9JLfOYwvSprwWYSu9cqSQtUgjMpOjElm14pKsDwCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇱🇧
الدم بالدم
عن مسيرات حزب الله التي تتبختر بالجليل</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/75259" target="_blank">📅 21:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75258">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23265c0b8f.mp4?token=HzqdmypTmwkzRe8slFzdJIWENqwVNa61xKaU0KmO-AYLkI8ZrUn16loCexu1beihtEwMrEm71NjiA8msqTD4-5hTNmXyhJFfIKHesk0DADrHAvlE2tMmkJuWM7pQpSPuf0pe87Rcd9QpKSTZFHVjoZLZbuKyQ3cGJO7yJYu1jXBPCwTxK4OPauhVaH_hq9TmwLZKkVnTSkGnwLngSMwLefSs9GyLXLjJDL-tub4anThUlqwA32hUof_yLZzLVwL7ZqlkIh9B1a0Mketvnl3_ZOanN9G1WMu_1nHmSYpgAKe80oUagUDS-QoVc1Vgi0kws0Ofp-L4aGTi3ub-imZOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23265c0b8f.mp4?token=HzqdmypTmwkzRe8slFzdJIWENqwVNa61xKaU0KmO-AYLkI8ZrUn16loCexu1beihtEwMrEm71NjiA8msqTD4-5hTNmXyhJFfIKHesk0DADrHAvlE2tMmkJuWM7pQpSPuf0pe87Rcd9QpKSTZFHVjoZLZbuKyQ3cGJO7yJYu1jXBPCwTxK4OPauhVaH_hq9TmwLZKkVnTSkGnwLngSMwLefSs9GyLXLjJDL-tub4anThUlqwA32hUof_yLZzLVwL7ZqlkIh9B1a0Mketvnl3_ZOanN9G1WMu_1nHmSYpgAKe80oUagUDS-QoVc1Vgi0kws0Ofp-L4aGTi3ub-imZOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
لن نبرم مع إيران إلا اتفاقا جيدا.
‏ لا أعتقد أننا سنحتاج مساعدة رئيس الصين بشأن إيران.
حلف النيتو خيب آمالي ولا نحتاج إلى مساعدة منه.
لا أعتقد أننا بحاجة إلى أي مساعدة بشأن إيران وسننتصر بطريقة أو أخرى سواء بشكل سلمي أو بغير ذلك.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/75258" target="_blank">📅 21:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75257">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-05-2026
قوّة لجنود جيش العدو الإسرائيلي بعد رصدها في منزل في بلدة الطيبة جنوبي لبنان بصاروخ موجّه.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/75257" target="_blank">📅 21:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75256">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
🏴‍☠️
استهداف دبابتي ميركافا للجيش الصهيوني في بلدة الطيبة بجنوب لبنان من قبل أبطال حزب الله.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/75256" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75255">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴‍☠️
🇮🇶
جانب من انتشار جحافل قوات الحشد الشعبي في صحراء النخيب غربي العراق للبحث عن اي تواجد او نشاط مريب ..</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75255" target="_blank">📅 20:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75254">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭐️
الحكومة البريطانية:
سنساهم بمسيرات ومقاتلات وسفينة حربية في مهمة متعددة الجنسيات لتأمين مضيق هرمز.
‏مهمة مضيق هرمز ستكون متعددة الجنسيات ودفاعية ومستقلة.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75254" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75253">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
صحراء النجف الأشرف تخضع لسيطرة كاملة من قبل القوات الأمنية العراقية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75253" target="_blank">📅 20:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75252">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-05-2026
جندي من جيش العدو الإسرائيلي في بلدة الطيبة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75252" target="_blank">📅 19:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75251">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
‏
الطاقة الأميركية:
أسعار النفط ستكون أعلى بـ 20 دولارا حال إغلاق هرمز حتى نهاية يونيو.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75251" target="_blank">📅 19:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75250">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16dad3ff36.mp4?token=DiEx5FKiDnGnQHTXsSgO0bJorARITNJU9Fd6-9lOg1AO3gUcre7KwhrEY-lG5lDv2P-NxV9ufXlri8HLSZa-EpoHMrBtxqEwPsq0eNc-TRdC1jUx6zijdOjxjyoQS6ozpLCkUJ3C4R0KjI8SHcbkyKobzmONJMYQSZeeiI6ubNwF8AEEN9it6WP4brLRYMS5U5hX34UxHuSHacRLyviOilfYezqnBhyyZUuFlSPjDD65cEVEDX0EBY172yTq7T43Z9X8OcrWBS-pN8zzndXTEDSSAV6icqyplZ0LsG8DIoN0m5tQ4hqcAgtttUvJFUmkvvc0Rpnlj7CzNGMSRubKFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16dad3ff36.mp4?token=DiEx5FKiDnGnQHTXsSgO0bJorARITNJU9Fd6-9lOg1AO3gUcre7KwhrEY-lG5lDv2P-NxV9ufXlri8HLSZa-EpoHMrBtxqEwPsq0eNc-TRdC1jUx6zijdOjxjyoQS6ozpLCkUJ3C4R0KjI8SHcbkyKobzmONJMYQSZeeiI6ubNwF8AEEN9it6WP4brLRYMS5U5hX34UxHuSHacRLyviOilfYezqnBhyyZUuFlSPjDD65cEVEDX0EBY172yTq7T43Z9X8OcrWBS-pN8zzndXTEDSSAV6icqyplZ0LsG8DIoN0m5tQ4hqcAgtttUvJFUmkvvc0Rpnlj7CzNGMSRubKFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يحرق مواقع وآليات العدو.. سرب من المسيرات ينطلق من لبنان مرة اخرى ويستهدف أماكن تموضع الجيش الصهيوني في الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/75250" target="_blank">📅 19:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75249">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دبابة ميركافا صهيونية تشتعل بعد دكها من قبل أبناء نصرالله</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75249" target="_blank">📅 19:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75248">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8gb2MRHvRQfcHwNqy-VjE0am46jYuwdBOqW68xwRcouGBojo37rvKizp24cZjLoqEom9aiq3NRCG_JZ-qRByMuNkql3U7mE6iN1zQQSWU_t1J8rp5O166DvqTGjH5Y2MMpgVYgYzR5wLttS5FXL65CKxo72al7L65KoEuZV7ljiJzJsenVwXNvdFc4uLbsLCx3VXdL08TTv47KFF6WinvcbNoZSXhN2HEoQ6R0OV5sZpZlfvZyHDf3GE9tUnVc1vNTgM4fEBJVFRZbdSxqvqOAQvqcOvqdFfTZ0ap5PPn6X3g5ks5luuwpsZS_rO0Ozi8VsLrpIAUzIBdu4KaVQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني خطير ومعقد على الحدود الشمالية، مع وقوع عدد من الإصابات، فيما لا يزال الحدث مستمرًا والطيران يعمل على نقل المصابين.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75248" target="_blank">📅 19:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75247">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
🏴‍☠️
مجدداً من لبنان.. الطائرات المسيرة تهاجم مستوطنات الشمال الفلسطيني المحتل وتصيب موقع عسكري صهيوني واعمدة الدخان ترتفع منه.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75247" target="_blank">📅 19:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75246">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw2EUW556K7egetDc20k50i4PjkvFXh3HBrhXmHbz91gPhNdkkZlXg76wBPEoJnVuRPStxhhM_6EHz_mRWy6W3z8hDc7Hwj4kYgVg2K3AjnVA06907Q1lyXVruXgv54vCq26IWsGA7xm3rYWHkk1dBiE0uqDNweISrni7h1kg92ZGUsBNk1ltHdK_Jj87H2JxeAEbRIvrEsq5ItBTx3X_I9p8sRjUQ02BaJrEyiWYhWpDGHdjF8AWACbt-WpTOyNEDWlM1bkZpZQr7vPosGIGx_-1LLUiph5RXhC1wuCzJtnkFr7AaYnxlAxoSEawUA5ZMraxlG5R0GbS2FO_rZDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مسير من لبنان يهاجم مستوطنات الشمال الفلسطيني المحتل</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75246" target="_blank">📅 19:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75245">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
09-05-2026
خيمة مُستَحدَثة لجيش العدو الإسرائيلي عند خلّة الراج في بلدة دير سريان جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/75245" target="_blank">📅 19:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75244">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بعد منع ناقلة تحمل نفط عراقي من المرور.. المتحدث باسم القيادة المركزية الامريكية: قواتنا منعت ناقلة النفط آجيوس فانوريوس من عبور هرمز لانتهاكها الحصار. ناقلة النفط كانت ترفع علم مالطا ولم تكن محملة بنفط إيراني</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75244" target="_blank">📅 18:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75243">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">طيران مسير من لبنان يهاجم مستوطنات الشمال الفلسطيني المحتل</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/75243" target="_blank">📅 18:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75242">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91423ce81.mp4?token=jgix5QbUFBpwTksZrREezVPtmOauNOmVVhUyDvffEAem466FKsikQzT7iUA-GbCDoG2KJKFbklQpiHiD4OTZHJh7EnFQjM7oBIl2auS7igxC555IvOs0Vj1W_Ph1POaAftpkXQp9fyJm_olxlIyYwK1pMoAG-DBmodEtPTiVFREinX1ySDN3PpA4Rc9hv-7qp_37HOh7Jke_zb5jKc3dXssgkTCM_C3Jl5ypxcObydqek9jZR4S_YdDrLDvp72Ar9TG8IrIVBBK3pph9awfHamIXLtd1RKEVG3g4K5V0Jargx6CCbAAEU-xJBcZ4uj-grpaMBx7p0uVAPQFcZ1wtRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91423ce81.mp4?token=jgix5QbUFBpwTksZrREezVPtmOauNOmVVhUyDvffEAem466FKsikQzT7iUA-GbCDoG2KJKFbklQpiHiD4OTZHJh7EnFQjM7oBIl2auS7igxC555IvOs0Vj1W_Ph1POaAftpkXQp9fyJm_olxlIyYwK1pMoAG-DBmodEtPTiVFREinX1ySDN3PpA4Rc9hv-7qp_37HOh7Jke_zb5jKc3dXssgkTCM_C3Jl5ypxcObydqek9jZR4S_YdDrLDvp72Ar9TG8IrIVBBK3pph9awfHamIXLtd1RKEVG3g4K5V0Jargx6CCbAAEU-xJBcZ4uj-grpaMBx7p0uVAPQFcZ1wtRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
استهداف موقع للجيش الإسرائيلي قرب مستوطنة مرجليوت واشتعال النيران داخله.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/75242" target="_blank">📅 18:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75241">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بعد منع ناقلة تحمل نفط عراقي من المرور..
المتحدث باسم القيادة المركزية الامريكية: قواتنا منعت ناقلة النفط آجيوس فانوريوس من عبور هرمز لانتهاكها الحصار. ناقلة النفط كانت ترفع علم مالطا ولم تكن محملة بنفط إيراني</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75241" target="_blank">📅 18:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75240">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">في خبر غير مهم
وزارة خارجية دويلة الكويت تستدعي السفير الايراني وتسلمه مذكرة احتجاج</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75240" target="_blank">📅 18:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75239">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75239" target="_blank">📅 18:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75238">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
تهديد المحلقات يتوسع باستمرار ويوقع خسائر كبيرة في صفوف القوات على الأرض.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75238" target="_blank">📅 17:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75236">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlyAkEQhsn_UnDBu5LBGOxvVh6gODBK_PpJfJtOFLmvz-d1gls2Y_CG6B8lbPhbZbFMLJay33SSc-YAcOsCh6OsdVgER-BViTk48ftMPJddfXEHlYDKzvmZmWDZP4La7xyI1sG_bvzFJayZF2iDSKBR9vlAPrW_KBsWOLyxDh5OkjHs2fGnZgOyoVlL709x_EUzsDps7Mv0M5hfmb-lpCPOW0omwQB1xSPfDTboJoSh2WuVlwZBl_Q82_rqCbRV0k2BaXgf4DpJ8T6CxWHLQaUmmRvYcs8wcOqsHQ0hE81LtDVN13OL77oNoiOzBZz9IeyfB75vUMxuhmrydqlcwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTVQIEGr4VCQqg4w5nFqZNs7HfR1OvJvBSd2F6w8bk5q6WfdaGbNQlHftxcb33RP3BJaxYefrONGiQH6V0um_3fHRut-1enGB21O1zCkJpVMiWkiakk3-e7yHdNx3DiZUZAxjPXWPFC7AxV6FUv5pzYXg75qOkLoXcV4Lgrbrg_wcgs_KK4AOR6fTZrPr5yOE5H67PA4FrnUx6GGBcCB518xPFFBUvzZStzFyt65oh8Dl6c7D1Esp_NwFoFjSXzQX0kU4uqC1WSWchp1T81u8ap10NjfA6CZCoW3ccTelWQCvNHEQr5S6dXEv2tGWgaEyoQZ6643_mKK41-9sCD16A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇻🇦
🇮🇷
بابا الفاتيكان "ليون الرابع عشر" يمنح أعلى وسام دبلوماسي فخري في الفاتيكان لسفير إيران لدى الكرسي الرسولي محمد حسين مختاري
ترامب يعاين الاضرار
😄</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75236" target="_blank">📅 17:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75234">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: تفعيل الدفاعات الجوية في الجليل الأعلى بعد هجوم لحزب الله.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75234" target="_blank">📅 17:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75233">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
تفعيل الدفاعات الجوية في الجليل الأعلى بعد هجوم لحزب الله.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/75233" target="_blank">📅 17:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75232">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇷🇺
‏روسيا تعلن إجراء اختبار ناجح لصاروخ "سارمات" النووي وتؤكد دخوله للخدمة نهاية العام.. بوتين: مدى صاروخ "سارمات" النووي قد يتجاوز 35 ألف كيلومتر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75232" target="_blank">📅 17:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75231">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامب: نجري اتصالات مباشرة مع مسؤولين إيرانيين ولسنا في عجلة من أمرنا للتوصل إلى اتفاق</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75231" target="_blank">📅 16:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75225">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hu-tMG5qIHE6l0E4C1FQzBeS7GK08sgc980k_3j9eFTIhZNDypEhT2dXgLqW7gXgnnS4XauF4RuZ7yuXav47vicuBTVYdL6MVYH3lcV0pJ6-pXNKzPCyF9lDDWQthw4-pl9Wqt7Zz9h7LEkYQFBoqFzAD4-Epkufg90ZENosd-WAFQTUzQi_08CjyJQODNhtcMbFipdnZZ277dr-gZrD2QPTmi6rudvMhBLGSjdOtLG-rE8KU5A7OC-p2lPPrzHsmpqh-M4z43bGvvBXpBycDe5oYUzKgLrHoB9HY-P3_cOthe7atbontZaMDZGTE3NgKXi8RQEiWZsse004pa_aTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SXAIrQZj1L6rofic-m099OZwY8zqH0Bf383lkjHs3nWg4gPmuHXWJGUHj6hnaW1JsSyFKimJukXzAc6UNzE8CNpmbI-u_KhDlz64b8L9N73lMYd2bFyx1D61c50_L-l-aFHirfRZqIgOZJkCFNdu1V2_NmluZn60D5Dmj6PQPZ0mObBMTjGjXudiT-Gu2KpzjGBaGdQ9Xrr2XfU8w6XEwMAzoa9Lv9R5ZePKklPoW7tI3fhWOug0AF7FL-W7Ru2ns0FNy-dA8r0xQDOdLVB2GcnvxIewZ05cRZo-52EdEOOHjcNmpTzwYliNriRIjvNjLh2hQHGffITWVL95qzKZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcXjXd7CmLXEq-IwgW6cCYIQcHz5gmH9PPGOAoq08hFZYQyrNR2JiGv1QUhxRZqr81SlceB_Mld60-s93mAQqVhUd4eOj1XG7lsacbb0DrRH1NhT81zoUkKui7YUjGfi3-EkdE6GmOzhRPJdrW86JMJOoGJlv8YddRKhQepF_JJEswUUluWTycIkNT-efr2sG91oY34jCdWtjeZPPFtzllCpVjuHvARxWrR9SZ4IXWcMq0ndVAMdtTWRvZZDQaW4twgOXw-r0PNxNc937p94Eec5ZmEzqbZxfBBXCgYGjT1JZNYvBb8TG-oa6zDakX-MfAPU91w52zpEBjT-GeWbeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arR3xdZsYAFzGU1CUqOryRfl37VjQbkIKkhwg-bwcG4YCjZ0ndoXYMVcT8cUB_RLDOTPhM94EVA7RZMB2bEgs6ndLaR1DzwQak_QnmttD4EJBzAeu-ZeHri1tizR3Zt0Iw_yhk36YcB2Ni34iEFLOSdjEy7tyizUZAJtVuTY19ZtBUAVLN392WQmF2xWTrMkXSOHR46G94UiYmSgFPh-kK1TOS1J_qznQeDLl6ge-MmSiWnHM6kfRJhi4ZAnkAh9OldkJgYRLgc5FPA6-_LZh0Cy-VvWG10TQrNeAktktp4TcuzaABRN_ki59_wOVcNHKFvwE3I34P0Pv1cDQ-Twdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvJMcJw_jKfKWFCk-1QT-7xeuOJTxj0nCq06PBqhtR373BhJU1DN2NXPDvvT1HbjKikEPM5A3987hv0UoiLPVxwo3ML2r82iHm0s63RvkI2KKQEhSH3dUW4a8yq-SFvbI8a6yjQkegS8MJR2A1pwLb25f0tYxG_jKhJWEtbOkQAMr0pj6gR2cG0gB3UWelVkXVCo5ecJE3FPYSvkwoW2wvotwoMX0YDfArm8JgR-ODxpoVAFqanF4m7_sgHPRKT8Y9a3cZ_9EVopWpvyqowjl-MulqC9VnHIHlaq1ivJtR_5He75qeo7ONFsuaB2Vtgihc3O3dr6YmimrRxIlzpJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgtD131l3WzhOAh4EISckThFzCHMnlBzBT3oQ-cWMeWC5I8CeY44UQb_yPg2WJh8jrZ2JC4Qk-QV6K3c6-ATzSORyiUYv7mCfHGZYqWJfXNMUb3tysQ9IlUvLicScTaeiEv3yK7K_PwN5ZRM2PTDn7aa_ZQPnIvZdq9EU0Y1M6AfYfgMU5tp4D6Xdkw7GlqQsGABXP0cmjwHdAKFh_ee1zlowbciVNxz2D5YqNyzhGhWVobvOyFza_pf9-dkorh6X4QwlgAilFXJO6_dhh3bFZlKy2udMmuhBidvR80iyXk4q8k1OGvbYFVAGC3zDuoWtKsSmjYQImGttDje7ReqKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماذا حدث في منطقة شنان قرب الاديان لمن هي الـ عجلات العسكرية المدرعة ماذا يفعل الأمريكان بالأحداثية  ‏37R  KV 750018  3478349 ما قصة هبوط هليكوبتر عدد ٦ ونصب خيم أمريكية في صحراء الانبار جنوب ناحية النخيب منطقة شنانه الاحداثيات ‏38R  KV  69654  98230  لماذا…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75225" target="_blank">📅 16:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75218">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uR5NXyxHeDTi1CeVdO1iHHEShTfhlwM7u3uMkU20yhoGafJdjlJP9M2kf9zlKr9jqGyH1Faugor1phLHUq3R-9E6vYMGN8iezgA-aWqD57XLXIENc6jK3nhRUajU1mbGEgCRmuX6yo4J3bH-uzjfXXj0QX0ZIYWnIm9TD_WtG1XIjlAQKWo7jd8OYnpFdge8lproZOiniel0uYdgFtMAP_JRtAZaGJJNlTLGZwc7ZdV8YiikqcjyUuWe5Z-hAoj4Y_gdNpYuBHzQeWOFm0M04QCVVgqBddh2pOY2UHlMAnUHDEG08ZQrf0d-UOOJEHz7dQ5ZoXtAuhNXehOy1d76Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي الايرانية:
قد يكون أحد خيارات إيران في حال وقوع هجوم آخر هو تخصيب اليورانيوم بنسبة 90%. سنناقش هذا الأمر في البرلمان.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75218" target="_blank">📅 16:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75217">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزير الحرب الأمريكي: لن نكشف عن الخطوة التالية ضد إيران لضمان عدم حصولها على قنبلة نووية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75217" target="_blank">📅 16:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75216">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الرئيس التنفيذي لشركة أدنوك: هناك نقص في مليار برميل على مستوى العالم بسبب إغلاق مضيق هرمز.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75216" target="_blank">📅 15:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75215">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 10-05-2026 منزل يتموضع فيه جنود جيش العدو الإسرائيلي في بلدة طير حرفا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75215" target="_blank">📅 15:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75214">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: الجيش الإسرائيلي لا يزال يحقق من أين بالضبط أُطلق الطائرة المسيّرة. "من الشرق" - قد تكون اليمن، إيران، أو العراق.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75214" target="_blank">📅 14:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75213">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/75213" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75213" target="_blank">📅 14:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75212">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هجوم من الشرق يتعرض له الكيان</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75212" target="_blank">📅 14:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75211">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">المتحدث باسم جيش العدو: اعترضنا طائرة بدون طيار أُطلقت من جهة الشرق.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75211" target="_blank">📅 14:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75210">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519ac44ef2.mp4?token=DyNv4rLYZj25BBc7EQo-hjYikrCWN7BZG8jk08dIyw24PLo3PAa17bzlHKSERW4WNHHykz0nXWXdPap3kIlGBW5zNiq_H1Pl2JNuFZhP40xzjBxKYONQIB7WmTWJYnVpkuMV9NOYP9TrcV4GPab7GktrzhuUT1DW2oi3zfSwrltxz08_4GJoI-soBv9DboShRF6q8dWzJGjApVL_a4U2v9KKTnwpZNSVOZGXbUtnajOk50AYa2U6Nebd9taQ3cLnuNXEfpa9E75_vO7HBbZodF4xj1_QbHmhbGRz-wZ131z3XksOOWDaLEFh2djtB5piNNXQWc10hb0LDIqmlNieVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519ac44ef2.mp4?token=DyNv4rLYZj25BBc7EQo-hjYikrCWN7BZG8jk08dIyw24PLo3PAa17bzlHKSERW4WNHHykz0nXWXdPap3kIlGBW5zNiq_H1Pl2JNuFZhP40xzjBxKYONQIB7WmTWJYnVpkuMV9NOYP9TrcV4GPab7GktrzhuUT1DW2oi3zfSwrltxz08_4GJoI-soBv9DboShRF6q8dWzJGjApVL_a4U2v9KKTnwpZNSVOZGXbUtnajOk50AYa2U6Nebd9taQ3cLnuNXEfpa9E75_vO7HBbZodF4xj1_QbHmhbGRz-wZ131z3XksOOWDaLEFh2djtB5piNNXQWc10hb0LDIqmlNieVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المتحدث باسم جيش العدو: اعترضنا طائرة بدون طيار أُطلقت من جهة الشرق.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75210" target="_blank">📅 14:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75209">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رغم التأكيد في بيان سابق
الاعلام الامني العراقي: لم يحدث إنزال جوي ولا صحة لوجود قاعدة في صحراء النخيب</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75209" target="_blank">📅 14:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75208">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بلومبرج: ‏تطلب قطر من السفن في منشأتها الرئيسية لتصدير الغاز الطبيعي المسال إيقاف تشغيل أجهزة الإرسال والاستقبال الخاصة بها.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75208" target="_blank">📅 12:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75207">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌟
الأمين العام لحزب الله: لا علاقة لأحد خارج لبنان بالسلاح والمقاومة وتنظيم شؤون الدولة اللبنانية الداخلية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75207" target="_blank">📅 12:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75205">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بي بي سي: تجري الولايات المتحدة مفاوضات منتظمة وسرية مع الدنمارك لفتح ثلاث قواعد عسكرية جديدة في جنوب جرينلاند.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75205" target="_blank">📅 11:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75204">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0eLTgI1UE2nuCiSPzPZ9MM9Z1QB9Od5E0rumDrWC-pvFWbVgdgNMUmOlfoF_YFsLOWVKtHHSRFhrN5smvFN5T4NZRqK9xvDLm1PTfPPWhDcHqZ9gYPSGGlS0V_-2ogh8nj5J6K0iLiHcghJ1IbFXTWul1EHEB72qbizfX6tPIYcj3mINsn7n_XBc51qdz_603jFE-01lmaBK-JkhMb9QfFFotiN19MTF6lPIt5DxAuT2JV41Ogn_Rk14v39vqMgcnwUBZ6JrPey4mxb4iJ5kn-MZyowACibKf-gbusaiS5yDIfoBMyymgwqdE5WxwK1YLx6i_oLhD5SiIsMaT2wNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
النفط يلامس 106 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75204" target="_blank">📅 10:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75203">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
وزارة التربية العراقية:
دعم الطلبة بإضافة خمس درجات لتلاميذ الصف الخامس الابتدائي وطلبة المراحل المتوسطة والإعدادية للصفوف غير المنتهية، بما فيها الإعداديات المهنية بفروعها كافة
إتاحة فرصة أداء امتحانات الدور الثاني لتلاميذ الصفوف الأربعة الأولى من المرحلة الابتدائية المنتظمين بالدوام (حصراً) والذين رسبوا في امتحانات الدور الأول، بغض النظر عن عدد المواد الدراسية التي لم يحققوا فيها النجاح.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75203" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75202">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي في البرلمان: أحد خيارات إيران إذا وقع عدوان تخصيب اليورانيوم بنسبة 90%</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75202" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75201">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: إصابة 8 مقاتلين من لواء غولاني في 3 اشتباكات قرب النهر على أطراف زوطر الشرقية جنوب لبنان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75201" target="_blank">📅 10:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75200">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇵🇰
الشرطة الباكستانية: مقتل 7 أشخاص بانفجار في سوق شمال غربي البلاد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75200" target="_blank">📅 09:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75199">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇱🇧
🇮🇶
لبنان يعفي العراقيين من التبعات المالية والقانونية المترتبة بذمتهم عن تجاوز فترات إقامتهم داخل لبنان خلال السنوات السابقة ولغاية 31/12/2026 وإلغاء إشارات المنع من دخول لبنان على كافة العراقيين المغادرين إلى العراق ليتمكنوا من زيارة لبنان مستقبلاً دون مشاكل.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75199" target="_blank">📅 08:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75198">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeD23vszxHkPJf8oxD3mzjPjcQkT3lUTSA3CcWOOM9sXqCgqMMZ9JXqauD7NsBdoKrUng1loloMIaIplCBw5C1KkVTnt2WAUPSg__Hklz-3XNQpLkaVGgBB8TOaiV_LfUBizYMFWyGpm31Q6_GYrRKsmX7gW4_GIOWzNACywdwmVy0eTWYXyrJXhKgobwLd4z1sjs0-iYUdZ-b-0aoOCXRSLjbSfhJlchLnDdrBjBqDch4IhDzJZYETiHFnNQEJugThMnlSXFxmcvMGtEC51h0cTcvCeqeO2akr1NBSFz91js4MbP4Gp3B5Zti9vuacabNy5MbADM574gfJRF9uJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد تباطؤ الاتفاق الإيراني الأميركي، أسعار النفط تقفز إلى 105 دولارات للبرميل.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/75198" target="_blank">📅 01:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75197">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8ben2j97ADj_Q_x0hbZf4UkvWYVRH1cc3uJ93gXY3RNx4A8iZHIMzJLsQbQqsBc5dsz21kYWJOB6pZrGnpiAN3sfT7T5--biclHNS7I5epY11OPL_CMgDWV6VY47GG-CetFDbv3MSg-NSlQhavQc7HgHnP99ncow9HXukyRYnNQL7-cf2atp0NBvlGdLEwSy7_M01-9qZax6L3Clfub0LZ_f_qwgoUQeKtJ3DEri47znYyZyZf_pZ6gMdJCBXd_ZhAqZOuQeL-Sm0UI67GMnSU0MHGi1Cmd3j2SubSv0tMBJgXyt44SvOs0ZfjPBhRRD-V2YblRL8JzWstZwxasMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب : اني حيل فرحان بزيارتي للصين ، الصين بلد يشك شك وبي خوش قائد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/75197" target="_blank">📅 01:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75196">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c76991be.mp4?token=JSKe8V_rXJsRCfSTNy0H-5ZJiGMtDFzMdv-d1gV954RB1SwfaAYJcBXD1jDDX-u4GBQvs2mQPHB5qIl4ozTxIHSDq6fw4etuS27ESBACCBTZnzVfbsJlSPQIep_fnWzmXEfoKJgJS4HpedpOMrzfKK13eSVY2dUhc7C6oKJTIyghbrwQepnMjulFdXJ-FIOKYY70bWeccV2TnFZgWUqxvkDR9FApRdxF0WbhGI8x_o3l9OrYN0zb_G2Rwj00033H__mASdQgIAu1jsrlmx6wm7RZY5pb_Y6TSA_NTYMxFaTuoVFNstGN9dEuN0EcpmwHeFGAnRqArOKt09hmU9mwgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c76991be.mp4?token=JSKe8V_rXJsRCfSTNy0H-5ZJiGMtDFzMdv-d1gV954RB1SwfaAYJcBXD1jDDX-u4GBQvs2mQPHB5qIl4ozTxIHSDq6fw4etuS27ESBACCBTZnzVfbsJlSPQIep_fnWzmXEfoKJgJS4HpedpOMrzfKK13eSVY2dUhc7C6oKJTIyghbrwQepnMjulFdXJ-FIOKYY70bWeccV2TnFZgWUqxvkDR9FApRdxF0WbhGI8x_o3l9OrYN0zb_G2Rwj00033H__mASdQgIAu1jsrlmx6wm7RZY5pb_Y6TSA_NTYMxFaTuoVFNstGN9dEuN0EcpmwHeFGAnRqArOKt09hmU9mwgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇮🇶
من تل ابيب الى الانبار   تمارس القيادة المركزية الوسطى الامريكية التي يعد جيش الكيان جزء منها ؛ عمليات استطلاع مركزة على مدى ٢٤ ساعة و على مناطق الأمن القومي الصهيوني خط امتداد ، النخيب ، الرزازة ، الخالدية ، الكيلو ١٠٦ ، خط ال H 3 ،  ومناطق الطاش ،…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/75196" target="_blank">📅 01:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75195">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وزارة الخارجية الإماراتية: دويلة الإمارات تؤكد أن حادث اختطاف ناقلة النفط قبالة السواحل اليمنية يمثل تهديدا مباشرا لأمن الملاحة البحرية</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75195" target="_blank">📅 01:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75194">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYTP61B2zTOUcCuAyCwusbcPQBhHkPBX3tNzykHb6er4hNcN1VUC3mqjP-soZUt_7tDwmBlF2x0WREtOqlXmIz4MgqqkFin9A1ADDASxfsR6BwAytZLedowjN-pSeJqgUekcjCvVEwkc2Pure3LSU9Puy4RwF-CqgEY5cd5cqb60nY4TaZzWdgquY8VkIxwC2wwbQKcDCetprG_UxgSlI2Y8LGa4ea2hAGsJ2d6XZ01wYFq6spmDGLdKOnUsFMo0odp6weCScRVWvyTfX_800wYwJ1xBsuy3m-bHxv36Y-PpddOA4Kydxk2ameTgOMWKCWgG4_VVkbOZqVxbnSRXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇮🇶
من تل ابيب الى الانبار
تمارس القيادة المركزية الوسطى الامريكية التي يعد جيش الكيان جزء منها ؛ عمليات استطلاع مركزة على مدى ٢٤ ساعة و على مناطق الأمن القومي الصهيوني خط امتداد ، النخيب ، الرزازة ، الخالدية ، الكيلو ١٠٦ ، خط ال H 3 ،  ومناطق الطاش ، عين تمر ، وادي شنان .. الكيان يعتبر هذه المناطق مصادر خطر ستراتيجية كونها مناطق منصات إطلاق صدام السابقة نحو النقب ، مناطق ذات طابع ديني كونها جغرافية نهر الفرات " من النيل إلى الفرات ممر داوود " ، مناطق بعيدة ومفتوحة عن السكان ما يؤمن أمان نسبي امني لقاعدة إدارة عمليات متقدمة .</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75194" target="_blank">📅 01:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75193">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM0PSkgyacm6xnHLCUf61ZVGIYO2WzDoluMckoPci8ZE7sRz88DN5CDlNsTn18_yaoQHHYe7S8H75jG3DLG84nsyKNYhCpMbNd66w0mnX_TBvDMJ8AnSNNZ8XgnFHDuOlhH58YWm0YG5o2f2pxMzvLEg2rOY0nNAPfrWgc9J62eyq698hdC4mITMok3LkOOBR-5C3xxEyR_azvCtwUDyxT0-Y1rhTeKPGIQAx8kc7DvKnNCdIZcZ3yD3rxsvl3R8jAwQ5NyKIo7Gemy8ZbPqPH4kHMUMqLLBK1-ZLwNKpmy_XCpGsSIL-LutYvYxXHfbKbeEGZDON7S_0v_zKW4Y0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
لا بديل عن قبول حقوق الشعب الإيراني كما وردت في المقترح ذي النقاط الأربع عشرة. وأي نهج آخر سيكون بلا جدوى، ولن يُسفر إلا عن سلسلة من الإخفاقات. كلما طال أمد مماطلتهم، زادت الأعباء المالية على دافعي الضرائب الأمريكيين.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75193" target="_blank">📅 00:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75191">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnwLboArLRBxDfYKYSS4uEjrsBdl6p_fNy94eML3jBmynXG6RPqwf5fGMD-FjLZlvmlWJuVa91QDVD20zMYqnSZL0tQ4pgVLNdxozMbrrTUDgTAlRPNe-eboQDIgm1zXIXwzj-l3uPUEmObnaranCUoIKCk8FJ9DsLHPJFuqtDuXl7gH7EQi1MBRS-WKyDtUnlC66t9YopRAgUp_3M5R2Y4u8GAGJgaqlzdFz_vUramDX3mtHiq2XBvUrCX7VMFHVaHGVSK2t1YsPSzCh8PLM9zEENFwSe3XaRLgmCfophdbwRUjTT5pEdV39YUtbtBBfBaLZznbHM3XPFQ0mJqCqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبنا العراقي العظيم
هل لديك معلومات عن الأشخاص الظاهرين في الصورة عناوينهم اسمائهم … مكافأة مادية في حالة معرفتك اي شخص ظاهر بالصورة راسلنا عبر البوت …</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75191" target="_blank">📅 00:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75190">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
قامت دولة الإمارات العربية المتحدة بشن ضربات عسكرية غير معلنة على إيران، بما في ذلك ضرب مصفاة نفطية في جزيرة لافان في أوائل أبريل - تقريبًا في الوقت الذي أعلن فيه ترامب وقف إطلاق النار.
أدى الهجوم إلى اندلاع حريق كبير وأدى إلى إيقاف تشغيل المصفاة لعدة أشهر. ردت إيران بضربات صاروخية وبدون طيار ضد الإمارات العربية المتحدة والكويت.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75190" target="_blank">📅 23:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75189">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">طيران مسير من لبنان يخترق مستوطنة مجدل شمس في الجولان الشمالي المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75189" target="_blank">📅 23:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75188">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0682c7b887.mp4?token=hasT0jlMowI5ILU6kq2YmfTA5Rs-816wjNfwd85hwKeLjvVvDlDwCjwAoXnT7duE9rkOWvlq7e3U59Nvgy1WcY9yyuNvzIPYloSXfBnivNmRYSLFYwDc3aD_DIE6H7C06dFFgh2yo9D6m249Rj7IH5GSptJ_vU6OlUifiJ1fuO69Rtsm9_hWuYe7m767L6zKlgg7YxeJpr6JWdZYyahZsYQaB6MRqf4pQKJkI355eucROq2o4dbCYCWOLAvO58wEgN4WY4k8qJy1gxlJ-Ch-qu87VRz8YPh0_nO2IW0gA_Nrv7Nyq_mYl91VxC10AcJrfN6FNj_APpkmBSgEOScWTAjbHJhWoE5EQfl6pfuRksKEo8-_dTI5Zzh9-jz7mViIYeJSH1R5LXG5GwlpMQYCn8zo9_oPWuHquktjr3SMtz-rMk9iNqvk0O-QHFVM87D8k0Cea3Sc-cwD0uegVJXspysPUExcBV29q4_wO3bV2XPmLGubIakbSD5EZa_pZsv_Ez7g8v0goQUPYhshY30yvqm9ZXy-9vfNDmSPRdzGjFQQUdQqCylyB2SF7lOQWz-JOF2eJZ6jijuSWx9wLhz58O6micr0fKiR7GW-6jCQs9jRhERdH-_tDLQXBOqiBaAa6VdhlKO3X805EP9R5e5U8trZ5eu-tIY9kAu1xd3wIek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0682c7b887.mp4?token=hasT0jlMowI5ILU6kq2YmfTA5Rs-816wjNfwd85hwKeLjvVvDlDwCjwAoXnT7duE9rkOWvlq7e3U59Nvgy1WcY9yyuNvzIPYloSXfBnivNmRYSLFYwDc3aD_DIE6H7C06dFFgh2yo9D6m249Rj7IH5GSptJ_vU6OlUifiJ1fuO69Rtsm9_hWuYe7m767L6zKlgg7YxeJpr6JWdZYyahZsYQaB6MRqf4pQKJkI355eucROq2o4dbCYCWOLAvO58wEgN4WY4k8qJy1gxlJ-Ch-qu87VRz8YPh0_nO2IW0gA_Nrv7Nyq_mYl91VxC10AcJrfN6FNj_APpkmBSgEOScWTAjbHJhWoE5EQfl6pfuRksKEo8-_dTI5Zzh9-jz7mViIYeJSH1R5LXG5GwlpMQYCn8zo9_oPWuHquktjr3SMtz-rMk9iNqvk0O-QHFVM87D8k0Cea3Sc-cwD0uegVJXspysPUExcBV29q4_wO3bV2XPmLGubIakbSD5EZa_pZsv_Ez7g8v0goQUPYhshY30yvqm9ZXy-9vfNDmSPRdzGjFQQUdQqCylyB2SF7lOQWz-JOF2eJZ6jijuSWx9wLhz58O6micr0fKiR7GW-6jCQs9jRhERdH-_tDLQXBOqiBaAa6VdhlKO3X805EP9R5e5U8trZ5eu-tIY9kAu1xd3wIek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
03-05-2026
تجمّعًا لآليات وجنود جيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75188" target="_blank">📅 23:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75187">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇶
قيادة العمليات المشتركة:
لا وجود لأي قواعد أو قوات غير مصرح بها على الأراضي العراقية وتحديداً في صحراء كربلاء شرق النخيب والنجف.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75187" target="_blank">📅 23:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75186">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271439eb30.mp4?token=VbsJk8s1C86KcCesuUSsoD2JBJ_5_bHsKRUIcnammCx1LCdAyjKyJr_AnF7wVqRRhbZvPjGfBFjaneNKoY8tjSmu96iLkdsVfKFzRL8ORtCEJ9Zx7NPln-5nhwjbm9Va4iszUTjOHkH5LTwj2jBbMbNPjoLkvidYhLP_t79Cd9rkbfPNPW1xev-PHlEJn_2MGztrwTDtXSdVK0CRNFHJebDqtANZFzOZ4t8x6B9qGIiqnHQfwRRbi8Ev3Sn9Do12Y-B8RhoNa86k3h26OdCOZ2z29abyU51zyWtKLNGnOuwjOjplUY_quJnKUI1MkJgJVX0MG3FrRaGF-M7bJQ7_3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271439eb30.mp4?token=VbsJk8s1C86KcCesuUSsoD2JBJ_5_bHsKRUIcnammCx1LCdAyjKyJr_AnF7wVqRRhbZvPjGfBFjaneNKoY8tjSmu96iLkdsVfKFzRL8ORtCEJ9Zx7NPln-5nhwjbm9Va4iszUTjOHkH5LTwj2jBbMbNPjoLkvidYhLP_t79Cd9rkbfPNPW1xev-PHlEJn_2MGztrwTDtXSdVK0CRNFHJebDqtANZFzOZ4t8x6B9qGIiqnHQfwRRbi8Ev3Sn9Do12Y-B8RhoNa86k3h26OdCOZ2z29abyU51zyWtKLNGnOuwjOjplUY_quJnKUI1MkJgJVX0MG3FrRaGF-M7bJQ7_3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
"لامين يامال" يرفع علم فلسطين خلال احتفالات نادي برشلونة بالدوري الإسباني.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75186" target="_blank">📅 22:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75185">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98b0e607ed.mp4?token=KgaB4M4uUDnX0LsfYvRs2J_TfFox8d6y7kBJ0JCy1QPIa0t7navab3rfrdOBHuNT1MFPMliexjEMceNw-zzNYXZPr6qquQ4AgDRYUyfa-hG3HsHsYfHVyhLFWvV4UhkGqiilk3kEMAp21HvO6fV6u25IBtERDLUawSq12xRvju15b4iOukEsCNEwjGXgT5WqOfaNlS6ArcJGmh-D0cBeBCJCzf9V2sW1xI_DtX18qnhwAkHkOD3j53v-5LCRpMKUExya1rQUxXhpv6C_D4mKCB4Kzgg9lrIRYf4n7VKImryTIPycYUAmB47j7nY5dhpddsskYdto1D91JTdyCtm1iZUeBOgP2jdLBA4fGkfbXrHFpKrEzQIBb5wwQXhsX7_I_aOvvAlwX9jy0o6gdnFcrVh9lb746Y_aouxPbG6ri3-r8dp-3AoIp32qCipTlEzd6kRQgOyxdwN0upT40-463xvDTIp5WHBT74VkHqdK9pOzK7a03nzM9rWxX9CromDtR5a_XxJA8rDthelVEa_-uIrMjhnPbW2Cr529sAvBMUd9AY3TfMukZGoYnnrJ2FQkK0_OLBWMnu_fUz8p1V7yP0jVbuTZ_S86x-AFSuW3Rd6RMuZ5t5borJCF6tqVYpKJlVMTICmdkM7PthlanF0xbjHpNvmzi8uZluP-enP_U54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98b0e607ed.mp4?token=KgaB4M4uUDnX0LsfYvRs2J_TfFox8d6y7kBJ0JCy1QPIa0t7navab3rfrdOBHuNT1MFPMliexjEMceNw-zzNYXZPr6qquQ4AgDRYUyfa-hG3HsHsYfHVyhLFWvV4UhkGqiilk3kEMAp21HvO6fV6u25IBtERDLUawSq12xRvju15b4iOukEsCNEwjGXgT5WqOfaNlS6ArcJGmh-D0cBeBCJCzf9V2sW1xI_DtX18qnhwAkHkOD3j53v-5LCRpMKUExya1rQUxXhpv6C_D4mKCB4Kzgg9lrIRYf4n7VKImryTIPycYUAmB47j7nY5dhpddsskYdto1D91JTdyCtm1iZUeBOgP2jdLBA4fGkfbXrHFpKrEzQIBb5wwQXhsX7_I_aOvvAlwX9jy0o6gdnFcrVh9lb746Y_aouxPbG6ri3-r8dp-3AoIp32qCipTlEzd6kRQgOyxdwN0upT40-463xvDTIp5WHBT74VkHqdK9pOzK7a03nzM9rWxX9CromDtR5a_XxJA8rDthelVEa_-uIrMjhnPbW2Cr529sAvBMUd9AY3TfMukZGoYnnrJ2FQkK0_OLBWMnu_fUz8p1V7yP0jVbuTZ_S86x-AFSuW3Rd6RMuZ5t5borJCF6tqVYpKJlVMTICmdkM7PthlanF0xbjHpNvmzi8uZluP-enP_U54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 08-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75185" target="_blank">📅 22:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75182">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669465c27.mp4?token=ooyZtnG353B7Og1DJ1GFiCdfJ3vnxM8PWSpENYe5ATEno9h6ihB-X42NyoCW9xF2gfvm0B4dmAkKD9ilbURSJuA4orQT5egZJoQiCPSSZMJJ1OtQi7iIRMeRpAsGfDCBGnrHVICQCVnAFL8IuJZ1qQS7kt1I3CydgHOhuo_KFW2Vdaw94VZ9slnuglwt9842KPeamHvcWqaKw46VrBz0Pe6M0JIiWzBVFbfZJ2xqcyFMErNrK5uWzai5R9h3Xf8SHYVaUk2P4kq6DtbTBuVK9wlXuuLhqlU9oU2HQvmY0BXeMmiSKmBvl4Cb55z1z8YzpLZuGZrIApK8PnDXe1IyzmI-0OlUi4kIQbYDPlvhdgCg61lnec30JhC10P7zFvcpzitaI4CoPc0uSrzgjj5iBEuDW0r8f-tOn8ZOxYjdNEcIx9UGmccQCSkuOI7LNb7i8EYNOKYMWupd7WSG5YpxB-BVHqUybn4wolKmhrSTHPIB0Fwe8tTE0SRhZfKsGo1L2QCMHqcOOsdO8eHP66GO1D1HIJ1618k-Kdok3MPC-v174shZyylMWUt6aGCaCP0vm1jHdExWEtPY9Q93EGoYlcWSo5F5icoVeNuBGW6h_jdF_wvXC_dki6U4opFrEsQRZqBl4mRSVMX166560IoXLyek6i_QQ8saB9nj6xfyzQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669465c27.mp4?token=ooyZtnG353B7Og1DJ1GFiCdfJ3vnxM8PWSpENYe5ATEno9h6ihB-X42NyoCW9xF2gfvm0B4dmAkKD9ilbURSJuA4orQT5egZJoQiCPSSZMJJ1OtQi7iIRMeRpAsGfDCBGnrHVICQCVnAFL8IuJZ1qQS7kt1I3CydgHOhuo_KFW2Vdaw94VZ9slnuglwt9842KPeamHvcWqaKw46VrBz0Pe6M0JIiWzBVFbfZJ2xqcyFMErNrK5uWzai5R9h3Xf8SHYVaUk2P4kq6DtbTBuVK9wlXuuLhqlU9oU2HQvmY0BXeMmiSKmBvl4Cb55z1z8YzpLZuGZrIApK8PnDXe1IyzmI-0OlUi4kIQbYDPlvhdgCg61lnec30JhC10P7zFvcpzitaI4CoPc0uSrzgjj5iBEuDW0r8f-tOn8ZOxYjdNEcIx9UGmccQCSkuOI7LNb7i8EYNOKYMWupd7WSG5YpxB-BVHqUybn4wolKmhrSTHPIB0Fwe8tTE0SRhZfKsGo1L2QCMHqcOOsdO8eHP66GO1D1HIJ1618k-Kdok3MPC-v174shZyylMWUt6aGCaCP0vm1jHdExWEtPY9Q93EGoYlcWSo5F5icoVeNuBGW6h_jdF_wvXC_dki6U4opFrEsQRZqBl4mRSVMX166560IoXLyek6i_QQ8saB9nj6xfyzQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إنفجار كبير في مصفاة إتش إف سنكلير بولاية أوكلاهوما الأمريكية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75182" target="_blank">📅 22:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75181">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
البيت الأبيض عن إيران:
ترامب يضع كل الخيارات على الطاولة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75181" target="_blank">📅 21:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75180">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMgp-V9eMnyzKFYJKhZotM2PpLihaz_xIsRzVxFeLXUAIIhya_nOKtO7xtyXS80k012qVHwm0zcWJI2_jJ5vYQjVE_DLcrMcZwVcb_5lUA93QWvyA0OmMGzlPeU_UBKMkSsNeQhalvVKoSCHE7GDcmLg38o_DftdcqoAwrVYaTnAul-_FBWyjRuLVumYVocv_XLFZrGwlzPAjmY-yZ2GGOCwfREsfqkg8wvkEi1YB28xeZMY1nNLg1qvUVaadRXbC_hpyRI41UCGZzybx42w9e5kBjbVFK_xakN3ygo7ZtlD0EbZxOYtpnef6i9Lrx2zzI4VlkGr79Qv8TsxuBe3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني:
‏قواتنا المسلحة على أهبة الاستعداد للرد على أي عدوان بأسلوبٍ يُعلّم الدرس؛ فالاستراتيجية الخاطئة والقرارات الخاطئة ستؤدي حتماً إلى نتائج خاطئة. وقد أدرك العالم أجمع هذا الأمر. نحن مستعدون لجميع الخيارات. سيتفاجأون.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75180" target="_blank">📅 21:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75179">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭐️
أكسيوس عن مسؤوليين: ترامب يدرس العمل العسكري ضد إيران في ظلّ "وقف إطلاق النار على حافة الانهيار".  ‏يجتمع ترامب مع فريق الأمن القومي المعني بإيران يوم الاثنين ؛‏سيناقش ترامب مع الفريق سبل المضي قدماً في الحرب مع إيران.  ترمب يرغب في اتفاق لإنهاء الحرب لكن…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75179" target="_blank">📅 21:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75178">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-05-2026
المقر المُستَحدَث لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75178" target="_blank">📅 21:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75177">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c252d1fee.mp4?token=r8KZ_NdvofK31tbarCa0AuZyp1PuDgxk0GUdqLlG7TJHZJUJyHAvSFtKvK0-Gh8gyK1EEzpsJ-np4IpCC3cHf_1xQLFea1Rp_ZAysHEg-igCXoHnSzJi2HzvP3PcrAOdf-AKD2EhNy6dXiZO96EyZ4CC942S2wrx9qH_wHZtP5xfTJetIn4e5Tjckgy58jAihGBDaG35GgqoC8K79C11-R2mqPpjlNTLjpjVeOL9c6SlI2QfQCFZqgsvNnnKnGdRHdRoqxXKW9Yo3H5lyXv_JuDoGigEvGyeRrNTePEdz82NZ0yaUq49gfgQXapX9F5hB3ttQYH1H_U1wlMSrBuyyDkaE8DrRTSDglqVVEnMTpnhcdtGENxU0GiCqWsCyza0QU4UnatIpEgpbFuRjKotPf0IM4Ipxp9Yy-IYyQjuU5TWsOr173-Pp11jK4fbNV27T3fPSdaQEdjQwWyKxVD9VdG2W_44043KOgGx_Jl79r5SteTwT8aAmGaKRNJaAxWFfe9XP7JwOnMuEk6mHyb9L8HuHsvBvdCypjOrLcs0Zk0DbAUO4PxDIzXCYyc1NypeZ0HXXoQIgAwJ5m2tcNC4pRjJ-uIMuTMfgaehvSc-m18Uqh_q47Bzo0O06um_jSqb07guJBXfoyIPlxW4XQZ9hAR2sYqNqSoiKbXSbXPQVBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c252d1fee.mp4?token=r8KZ_NdvofK31tbarCa0AuZyp1PuDgxk0GUdqLlG7TJHZJUJyHAvSFtKvK0-Gh8gyK1EEzpsJ-np4IpCC3cHf_1xQLFea1Rp_ZAysHEg-igCXoHnSzJi2HzvP3PcrAOdf-AKD2EhNy6dXiZO96EyZ4CC942S2wrx9qH_wHZtP5xfTJetIn4e5Tjckgy58jAihGBDaG35GgqoC8K79C11-R2mqPpjlNTLjpjVeOL9c6SlI2QfQCFZqgsvNnnKnGdRHdRoqxXKW9Yo3H5lyXv_JuDoGigEvGyeRrNTePEdz82NZ0yaUq49gfgQXapX9F5hB3ttQYH1H_U1wlMSrBuyyDkaE8DrRTSDglqVVEnMTpnhcdtGENxU0GiCqWsCyza0QU4UnatIpEgpbFuRjKotPf0IM4Ipxp9Yy-IYyQjuU5TWsOr173-Pp11jK4fbNV27T3fPSdaQEdjQwWyKxVD9VdG2W_44043KOgGx_Jl79r5SteTwT8aAmGaKRNJaAxWFfe9XP7JwOnMuEk6mHyb9L8HuHsvBvdCypjOrLcs0Zk0DbAUO4PxDIzXCYyc1NypeZ0HXXoQIgAwJ5m2tcNC4pRjJ-uIMuTMfgaehvSc-m18Uqh_q47Bzo0O06um_jSqb07guJBXfoyIPlxW4XQZ9hAR2sYqNqSoiKbXSbXPQVBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
الغيارى من أبناء الشعب البحريني يشتبكون مع عصابات آل خليفة رفضاً لقرارات إسقاط الجناسي وإعتقال رجال الدين الشيعة بتهمة دعم الجمهورية الإسلامية في حربها ضد العدو الصهيوأمريكي.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75177" target="_blank">📅 20:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75176">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80335b35d0.mp4?token=WX1liKHbK7K7x2O1RGocSE65Y_XNo5kKg0kuHZzNBzyQbLP2n5axvF5_nfcDYyi0e2WOmH8uVbTTB7jXmYMggV7MSK9JymFXENMX6Xs6Jd5mGueDp09iNmodYWSajt2scp7tGDx2u3HnJTp_QWhh-7lVeyh3rQTC_wtdJAHhUxkUlFrjXs8kVKehbwuaEeHvjZCYP2rIw2-FU4DCS0mNzKxX5HyERSzVihwgJR4tDEiIEH671ThQvfR60qJ0wXdyH_wW5XCNKU049Aeob5s3hLlBqeEhitxmABgfRo5Romxxz3HMLdn8YJNMK0Ib8H4teePyftT3Ndq4IJwKDzkY9KKNwxH_LR5DwfdrJXPXutbcC_I8DpJEh2fWkHXS1RcccCGqLqHERkOAfcAcXYUnbtfdSRXyxx5Rz4SXgfrFVE3WO3txlPkChSzDb-zH1Pnar0PSzcWWggtOz7GXJCVi2osZyYQeZlnUPQxjBjhfFz820eurN7EV_SSe9lt0defoO61eVAfsCra_nGQBeff35mWqAT4luRB25Ahb1VxKbMPlzzwJ4Zy5CQCSSJAlkz3mgt8V2BiYdv-O-1hDbSXo4oXhZiRs9BUU8fZK2oi3PS_KsVCQuuyUfLjzzP0Cd4Slr8Jdx3yrYmwIuA61L5yzBEE8YOtOA9OeHXxFLnBl4cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80335b35d0.mp4?token=WX1liKHbK7K7x2O1RGocSE65Y_XNo5kKg0kuHZzNBzyQbLP2n5axvF5_nfcDYyi0e2WOmH8uVbTTB7jXmYMggV7MSK9JymFXENMX6Xs6Jd5mGueDp09iNmodYWSajt2scp7tGDx2u3HnJTp_QWhh-7lVeyh3rQTC_wtdJAHhUxkUlFrjXs8kVKehbwuaEeHvjZCYP2rIw2-FU4DCS0mNzKxX5HyERSzVihwgJR4tDEiIEH671ThQvfR60qJ0wXdyH_wW5XCNKU049Aeob5s3hLlBqeEhitxmABgfRo5Romxxz3HMLdn8YJNMK0Ib8H4teePyftT3Ndq4IJwKDzkY9KKNwxH_LR5DwfdrJXPXutbcC_I8DpJEh2fWkHXS1RcccCGqLqHERkOAfcAcXYUnbtfdSRXyxx5Rz4SXgfrFVE3WO3txlPkChSzDb-zH1Pnar0PSzcWWggtOz7GXJCVi2osZyYQeZlnUPQxjBjhfFz820eurN7EV_SSe9lt0defoO61eVAfsCra_nGQBeff35mWqAT4luRB25Ahb1VxKbMPlzzwJ4Zy5CQCSSJAlkz3mgt8V2BiYdv-O-1hDbSXo4oXhZiRs9BUU8fZK2oi3PS_KsVCQuuyUfLjzzP0Cd4Slr8Jdx3yrYmwIuA61L5yzBEE8YOtOA9OeHXxFLnBl4cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-05-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75176" target="_blank">📅 20:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75175">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
🇮🇷
اللجنة الأمنية العليا العراقية – الإيرانية تعقد اجتماعاً في العاصمة بغداد وتؤكد أهمية تعزيز التنسيق الأمني المشترك، وتشديد إجراءات ضبط الحدود ومنع أي عمليات تسلل أو تحركات للجماعات الإرهابية أو المسلحة التي من شأنها تهديد الأمن والاستقرار في البلدين والمنطقة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75175" target="_blank">📅 20:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75174">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
‏ترامب: الإيرانيون حاولوا إعادة بناء قدراتهم في الأسابيع الماضية.  ‏وقف إطلاق النار في إيران على أجهزة الإنعاش.  انتظرنا عدة أيام للحصول على الرد الإيراني وكان يمكن أن يكون جاهزا خلال 10 دقائق.  مقترح إيران قطعة من القمامة ولم أكمل قراءته. الحل الدبلوماسي…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75174" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75173">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇦
زيلينسكي:
نحن نستعد لهجمات جديدة، روسيا لا تنوي إنهاء الحرب.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75173" target="_blank">📅 20:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75172">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
مصدر مُقرّب من فريق التفاوض الإيراني:
خلافاً لما تدّعيه بعض وسائل الإعلام الغربية، لا يوجد في نص إيران ما يسمح لها بقبول سحب المواد النووية المخصبة.
حدّدت إيران إطارًا زمنيًا مُحدّدًا في خطتها المُقترحة لاستلام أموالها المُجمّدة. أن الولايات المتحدة نصّت في خطتها على الإفراج عن الأموال الإيرانية المُجمّدة، لكن إيران أصرّت على ضرورة الإفراج عنها خلال فترة زمنية مُحدّدة.
إن ادعاء بعض وسائل الإعلام الغربية التي تنشر أخبارًا كاذبة بأن إيران اقترحت تجميد تخصيب اليورانيوم لمدة 15 عامًا ضمن خطتها محض افتراء، وهو مجرد تضليل نفسي.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75172" target="_blank">📅 19:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75171">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21e6e3a31.mp4?token=A0f2fhQiUx53MrqTSWPERckICMND5mGvlQ1IdTxHxz8hUXmtPQftFQwu3U-l-v7M8MtonEI2xpxweKFBjMgewiNiChpxG1nR7-52epB3ZfJByTbTrrkdeXYbUT4x8ReGHUnlaMWsoAt8AW1cNtmiaRPJpQ-OCRxd4fT0NxIfsYT8CmiFEjdzfq8_inwVNF6PaV5dYUr-TqwRlafpJU8PS61aWNGIUDBRdzJBApDcklOIIceezjT9zMGKAzj-pq7T840jHaPOAsBeHrpWnI4JucXzk-nNEWFLnXaF9jOYi1AadkcssnSrUCExrHTkpMBFha2G0IUmevKQZ1TQWdHO87eexLI6Tb9dRe778h_zWuGN_HWOIlV8uY1D1VAvs_oSRlCmFWNEcrg15e4SvJBoFEQ5Q4UYUmpajr8sGImFMVVyfMKOal5I9DotKzHaN_i6Gt9lb_0ocL7u9uv7UkKPdmIXkHsHTuX2D-0Ao7a0qBkPhUckn5j9kdElfSc2Z_YzNrHm5RNnXjaJHmpqmR4kMad_NIfaFYE6z0sflFhXHf8hxdgPORMVQnv88bdNaHoAdcAXNU13CXCb4sc8rWH9Bh6XmEoAFaPLmqMLbT3ziy6MyhCS5lybK3N7rmslxfhJKAoZ9uDk3tWPnpmuoziRdRGhupzmq_pFKdWzXIlywfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21e6e3a31.mp4?token=A0f2fhQiUx53MrqTSWPERckICMND5mGvlQ1IdTxHxz8hUXmtPQftFQwu3U-l-v7M8MtonEI2xpxweKFBjMgewiNiChpxG1nR7-52epB3ZfJByTbTrrkdeXYbUT4x8ReGHUnlaMWsoAt8AW1cNtmiaRPJpQ-OCRxd4fT0NxIfsYT8CmiFEjdzfq8_inwVNF6PaV5dYUr-TqwRlafpJU8PS61aWNGIUDBRdzJBApDcklOIIceezjT9zMGKAzj-pq7T840jHaPOAsBeHrpWnI4JucXzk-nNEWFLnXaF9jOYi1AadkcssnSrUCExrHTkpMBFha2G0IUmevKQZ1TQWdHO87eexLI6Tb9dRe778h_zWuGN_HWOIlV8uY1D1VAvs_oSRlCmFWNEcrg15e4SvJBoFEQ5Q4UYUmpajr8sGImFMVVyfMKOal5I9DotKzHaN_i6Gt9lb_0ocL7u9uv7UkKPdmIXkHsHTuX2D-0Ao7a0qBkPhUckn5j9kdElfSc2Z_YzNrHm5RNnXjaJHmpqmR4kMad_NIfaFYE6z0sflFhXHf8hxdgPORMVQnv88bdNaHoAdcAXNU13CXCb4sc8rWH9Bh6XmEoAFaPLmqMLbT3ziy6MyhCS5lybK3N7rmslxfhJKAoZ9uDk3tWPnpmuoziRdRGhupzmq_pFKdWzXIlywfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إعلام العدو:
توثيق يظهر وجود عدد كبير من طائرات التزويد بالوقود الأمريكية في مطار بن غوريون.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75171" target="_blank">📅 19:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75170">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
ترامب: لدي خيبة أمل كبيرة تجاه الأكراد الذين منحناهم سلاحا ليسلموه داخل إيران لكنهم احتفظوا به.  ‏يقول الكونغرس إن الأكراد "يقاتلون بشدة". كلا، إنهم يقاتلون بشدة عندما يتقاضون رواتبهم.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75170" target="_blank">📅 19:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75169">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksHaaeafhw4I9DgeiCEjtaJ5cLoFjbafWD5ko1uM0DkrbHXxixnmgECOo-32GtIpUYOB4EYiom_Vh3wqsCbM5BaT1d9g6KihltmwJd23q5y-WoC8C4IPDT54nCX3aM51puCYn-0lQ97gVhD7cvNfJVN0CfQgmf7_KN3yKcD6VRy6yR8gN1d_cHJnqdfTs9_EJwBjZO5jo97WDc0IFzthU7XXmVHuyl7MhKw5LBjZLczb8uge5ENpW6oZrqIr-7-r0Fvv_tOmiqF17h8jo-k6-9zlGfjpP3mPNu5dkFpOqQJhZNKaS6zb2fHp5JrP2__P5sxXJwp9nSQb_t1nkt_UZm_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksHaaeafhw4I9DgeiCEjtaJ5cLoFjbafWD5ko1uM0DkrbHXxixnmgECOo-32GtIpUYOB4EYiom_Vh3wqsCbM5BaT1d9g6KihltmwJd23q5y-WoC8C4IPDT54nCX3aM51puCYn-0lQ97gVhD7cvNfJVN0CfQgmf7_KN3yKcD6VRy6yR8gN1d_cHJnqdfTs9_EJwBjZO5jo97WDc0IFzthU7XXmVHuyl7MhKw5LBjZLczb8uge5ENpW6oZrqIr-7-r0Fvv_tOmiqF17h8jo-k6-9zlGfjpP3mPNu5dkFpOqQJhZNKaS6zb2fHp5JrP2__P5sxXJwp9nSQb_t1nkt_UZm_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: الإيرانيون حاولوا إعادة بناء قدراتهم في الأسابيع الماضية.  ‏وقف إطلاق النار في إيران على أجهزة الإنعاش.  انتظرنا عدة أيام للحصول على الرد الإيراني وكان يمكن أن يكون جاهزا خلال 10 دقائق.  مقترح إيران قطعة من القمامة ولم أكمل قراءته. الحل الدبلوماسي…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75169" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75168">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emgmmWHqKmOGZOiAmIaAEJ6krpEJaWY9QTC1XQLMtt3_zGlFQ6lePkM8aOK1suVDkZYenwNUc2ViSgZ22GWGQ7Mj5JyRYO9EfacweBgltyBTRYNlyyUkPyKoAOMHwy7UJjtZIZ32T1preVXuyHaPB5dR6J1RyoYy64nAn_1TUbn06k_X3rslx8G852kvZAPzwaVzisaJEDEVcHSEv4tuO4Gni4S8gfwtaiMvkdg1NW5-QR3qbWOBNlkyoKUlOKTxtGaOA2IxwJvI1HlJ-r4ppl0r7KkrT2oEWgDQa1sQKv41Hsbmcnpn3SC7SX9Wgw8wdDMUNNao1jOyWSrGHMRCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
الرئيس الإيراني مسعود بزشكيان يقدم شكره للمرجع الاعلى سماحة السيد علي السيستاني والشعب العراقي.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75168" target="_blank">📅 19:14 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75167">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8d45e7ce.mp4?token=VoQk9EWgbOpTyjQt4wnyd2kJSaHtn1CUfizPxqJe-OLRBVN2Q73pYn4Obqavh41cSA38rijzppIKnkysbzd666L61Il8l7lGh_PVm8qKj94ZwEYMVa5-hBI4DZkSIKbsqOPbJL4m-cRhyCumMPfJUPGGpTnMxuKJhvCBJVdyM1MlXIPJ3pJ5Cr_rL2cBouhBqGykUw4ZxqAbGqK7q_BgIozXtIiIJEA5OqailFspIh-HUjDkGCyGU6M7Au928fWyPXVzcSNRTsERKcIj4pbT1EtUcqEqrAu9t83ldU2dd22xpQOG3IndiF2J97HguuXxR5u63eBUbaKVI8yXApOX4JsLe27UrZbt5iDhdNj6cjKbONnaZ0G4uHXKxDU4qIynKrpwyThxUl0uZkNsDrhKDCcCAf2tky-smVgSbKS5Q9zSfo_QqkynVFRTP8cdeoV2goCgaRfzYS9VPbfSPsROPPXkulgtQ7IafY28yrcghpXzMYzP-BdRNhm284brk1LhLsVTO_95u8wuFkeUhGkYq44cuwnHbeHcn4D6rzjy1NpRxwP5mWO61xrr99xPEaOVP9A2IVdpSeEwaCLxBSK4Yw7JnHvWEav_iT2Jp7-r4JgY_ZDRMXv1uljVia7ddu8dM1fMDeEzQPQWrUazwRCn-MlOhNgfEtBP-8PrKEPCeDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8d45e7ce.mp4?token=VoQk9EWgbOpTyjQt4wnyd2kJSaHtn1CUfizPxqJe-OLRBVN2Q73pYn4Obqavh41cSA38rijzppIKnkysbzd666L61Il8l7lGh_PVm8qKj94ZwEYMVa5-hBI4DZkSIKbsqOPbJL4m-cRhyCumMPfJUPGGpTnMxuKJhvCBJVdyM1MlXIPJ3pJ5Cr_rL2cBouhBqGykUw4ZxqAbGqK7q_BgIozXtIiIJEA5OqailFspIh-HUjDkGCyGU6M7Au928fWyPXVzcSNRTsERKcIj4pbT1EtUcqEqrAu9t83ldU2dd22xpQOG3IndiF2J97HguuXxR5u63eBUbaKVI8yXApOX4JsLe27UrZbt5iDhdNj6cjKbONnaZ0G4uHXKxDU4qIynKrpwyThxUl0uZkNsDrhKDCcCAf2tky-smVgSbKS5Q9zSfo_QqkynVFRTP8cdeoV2goCgaRfzYS9VPbfSPsROPPXkulgtQ7IafY28yrcghpXzMYzP-BdRNhm284brk1LhLsVTO_95u8wuFkeUhGkYq44cuwnHbeHcn4D6rzjy1NpRxwP5mWO61xrr99xPEaOVP9A2IVdpSeEwaCLxBSK4Yw7JnHvWEav_iT2Jp7-r4JgY_ZDRMXv1uljVia7ddu8dM1fMDeEzQPQWrUazwRCn-MlOhNgfEtBP-8PrKEPCeDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: عدد السفن العسكرية الإيرانية الآن صفر.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75167" target="_blank">📅 19:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75166">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8swIklc_KlV2X0E4rJ88acY4w_yCk1dqzlfhkCxWRdwDUn2H2fP_-pTu-sjlq72I8iPF2hmTqt0aSVkMbzC9V8EQ1CBje3JrMxcNzATgOW-JnsEmdKgTy8FIKrl0LTCRPNJlkoZRK4kqmKl16Vzf212A5xwHdQLa1A_bn0nIJ5hxE5-V8hgUzKzyCTEdlbFWDHhRgclgIWqXRuiPCgC_c85tyRlXNxFrV80OuUDqJ8Z_wSs3xr1vgM03-c2wJaGG8O81mo23aj5AQAt5KU1hoEdmq5Wv_WsB6Q45doxfWsISsIsI2dxSl-aA49nQghepQumVudIJCfn9ZnHHAzeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏ترامب: سألتقي بمجموعة كبيرة من الجنرالات بشأن إيران.  اقتراح إيران غير مقبول ‏ولدي خطة بشأنها.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75166" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75165">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
رئيس منظمة الطاقة الذرية الإيرانية:
موضوع التكنولوجيا النووية ليس على جدول أعمال المفاوضات.
التخصيب غير قابل للتفاوض.
أنشطة صناعة الطاقة النووية في إيران سلمية وستظل سلمية.
تم اتخاذ التدابير اللازمة لحماية المراكز والأصول النووية وتطبيقها.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75165" target="_blank">📅 18:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75164">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe6bf720a.mp4?token=nN-X_JtOsns9T63uaYedGvhdjwO2eZAqAsRJOAFEypcJ-qEOLx-0mCn5Hy-nJvjvcTEijGnJ06Bv1Kbf0WwGjiZUuoLhTVQ6S77QGCnqU9YGL0fl-j-HKZTA6WQat0Eg2oKtngkDvex48wMbqxlkVkelO2RssyZd5fg1Ao-kszA7n2Jq2nsi3WoXxUeiBoWIYoASdl7h_jr1ERZyMLxgZDK6ubBoEcQNPu4LieB5p4dWOe21oNmLH-Rv91auAgZk0jVbR39S-uxBNIqyO5uS9o7LK7eXIBO9KDwqcggKRGJBpsL5uTXjqpc-QoceOpwCSPmA4p7nOFX93PGPCjxHxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe6bf720a.mp4?token=nN-X_JtOsns9T63uaYedGvhdjwO2eZAqAsRJOAFEypcJ-qEOLx-0mCn5Hy-nJvjvcTEijGnJ06Bv1Kbf0WwGjiZUuoLhTVQ6S77QGCnqU9YGL0fl-j-HKZTA6WQat0Eg2oKtngkDvex48wMbqxlkVkelO2RssyZd5fg1Ao-kszA7n2Jq2nsi3WoXxUeiBoWIYoASdl7h_jr1ERZyMLxgZDK6ubBoEcQNPu4LieB5p4dWOe21oNmLH-Rv91auAgZk0jVbR39S-uxBNIqyO5uS9o7LK7eXIBO9KDwqcggKRGJBpsL5uTXjqpc-QoceOpwCSPmA4p7nOFX93PGPCjxHxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: سنتعامل مع إيران حتى يتم التوصل إلى اتفاق.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75164" target="_blank">📅 18:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75163">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏴‍☠️
صحيفة "معاريف" العبرية:
حاول حزب الله إسقاط طائرة مقاتلة تابعة لسلاح الجو الإسرائيلي في لبنان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75163" target="_blank">📅 18:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75162">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
أ.ب عن مصدر دبلوماسي:
إسلام آباد تحاول ترتيب مذكرة تفاهم لإنهاء الحرب وفتح طريق حوار أوسع بين واشنطن وطهران.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75162" target="_blank">📅 18:28 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
