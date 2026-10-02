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
<img src="https://cdn4.telesco.pe/file/fHLXkwzH0hD3G69sbKAdLyzoor2ZwBIQol5HGgQ-wT-mLV9CXKESdE7KvHkxqBkk9sqA-mCmVACdsQbmQoxVVKVNPdVXe_cPw86YBgMLH3y3dyljIVyEuEvCx537E_ufQAw-_iVbVJzU-XXv-HwCR6QyQp-wkhkB6qNuxCrVHSXDO0nj2Ta-TToelaszzW8P3tqj8_M3yZzz0YhZDp3IaPBYp66gdTlp3mKmJXgUNwGs_QpHav7uPp_qtvk5GQYSaB4n047ClpY62mJ6XM3S7NO3UN6Ye4_oneDnzPsqi_DzqA_cMLYMZi2FdD2JG-R3g2bVe11H9vhGUqt27RgLkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 05:52:28</div>
<hr>

<div class="tg-post" id="msg-92315">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edffd6bce5.mp4?token=eeHfQGSYf33okbZ4R-H0fRxorF-leaXdjxJnsi2XZm3rKTm38A-zDHZ2bbAggTsXdcuRB3lQ7t6RB_Te861rhQwjHJSL_XPU5ggTIgFpopLy5g0Glc-WOKUaokiNu9rver8IPj4Hmpl5hBcm0DM1h3fVlOTBebccSUFaPxyBBcnInGTmYmO01yc85qNKqTTR4a1R2MIc7LZW_IHUrMWtHdx8B-Dt5-ApaFw9KtkwN8-11eJ_hY9gUAk5UbrPppW-ke3rIWWsY_4gh8ikhTMBIErbTzk9yLD4d3R_e_nzc_qTCOEJI5JdkF6883Eubu8ADWWZfGRZvQC_pfjGxYYClw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edffd6bce5.mp4?token=eeHfQGSYf33okbZ4R-H0fRxorF-leaXdjxJnsi2XZm3rKTm38A-zDHZ2bbAggTsXdcuRB3lQ7t6RB_Te861rhQwjHJSL_XPU5ggTIgFpopLy5g0Glc-WOKUaokiNu9rver8IPj4Hmpl5hBcm0DM1h3fVlOTBebccSUFaPxyBBcnInGTmYmO01yc85qNKqTTR4a1R2MIc7LZW_IHUrMWtHdx8B-Dt5-ApaFw9KtkwN8-11eJ_hY9gUAk5UbrPppW-ke3rIWWsY_4gh8ikhTMBIErbTzk9yLD4d3R_e_nzc_qTCOEJI5JdkF6883Eubu8ADWWZfGRZvQC_pfjGxYYClw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مستمر لتحشيدات مرتزقة التحالف من قبل القوات المسلحة اليمنية في عدن</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/naya_foriraq/92315" target="_blank">📅 04:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92314">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39cddb5e2.mp4?token=sneXAORIaUffRoNzydobacw2ZFl_2x1MBJNxVcE6Ftc0w3VnzRNb8QQbfIfHTvgKs-tW_GnO_OSnpwIphBqRzsctPTXtQC-GuBB90lwBDd5GV-p6QCZrC7bnfO9t9n2eTW0zF__i9qwjiYhHFzf-J0VWaGYInYwxWX-hKIIXd9sXzeChoM84BAq9MWJEw9RdfbOAZFFVYSjexp3BHygp6tOurRUdaFhjggTb_-R-RcR0oTw9nVoGGrZaRtwo5H8ybKzlJVl4O-P7V_vhxky4uV3n0-CT0gTTa9nSxh_9tcf3nS2ih728E-dKgNRVrWhpIBELsK7Q-RMHrBKASOSKwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39cddb5e2.mp4?token=sneXAORIaUffRoNzydobacw2ZFl_2x1MBJNxVcE6Ftc0w3VnzRNb8QQbfIfHTvgKs-tW_GnO_OSnpwIphBqRzsctPTXtQC-GuBB90lwBDd5GV-p6QCZrC7bnfO9t9n2eTW0zF__i9qwjiYhHFzf-J0VWaGYInYwxWX-hKIIXd9sXzeChoM84BAq9MWJEw9RdfbOAZFFVYSjexp3BHygp6tOurRUdaFhjggTb_-R-RcR0oTw9nVoGGrZaRtwo5H8ybKzlJVl4O-P7V_vhxky4uV3n0-CT0gTTa9nSxh_9tcf3nS2ih728E-dKgNRVrWhpIBELsK7Q-RMHrBKASOSKwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اللحظات الاولى لاستهداف مرتزقة قوات التحالف في في عدن</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/naya_foriraq/92314" target="_blank">📅 04:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92313">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">إعلام أجنبي:أرسلت الولايات المتحدة مؤخراً بطاريتين إضافيتين من صواريخ "باتريوت" لحماية منشآت حيوية للنفط والغاز في كل من السعودية وقطر، وذلك في ظل احتمالية شن ضربات أمريكية جديدة ضد إيران.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/naya_foriraq/92313" target="_blank">📅 04:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92312">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f52287c44.mp4?token=LmsEvWzmmUCtCfV6ShpxHbcYYmHv1pNl45rGlIWAWwVLOj6VleNTMRl9DQw8EUQ-xYAHw0XzHlwVI8JjCqa9urgizHREphoqDMQ05kPC2VHiXVtBw6OJLQRiADyqJcVmLIj0MmhiNuMTWkQKqURDxvPt4Xk6FCXEawrnYIkMe9qHEj4gJMi4l7_6ecEaW5_QcLubJ-2AK1gofaJDR0CcFSlNlvLR_nutoFnIcbVSA7HxCm2-Dzj8jBBTAaEw5n66yAiJCF8Lx5y0CUB4aOUfzSKOIAaaU3I9olHn1gkfGTnQo_oMLaJ-24jBPbwT3M0rwHWB47XGHjj48iaqQl9EIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f52287c44.mp4?token=LmsEvWzmmUCtCfV6ShpxHbcYYmHv1pNl45rGlIWAWwVLOj6VleNTMRl9DQw8EUQ-xYAHw0XzHlwVI8JjCqa9urgizHREphoqDMQ05kPC2VHiXVtBw6OJLQRiADyqJcVmLIj0MmhiNuMTWkQKqURDxvPt4Xk6FCXEawrnYIkMe9qHEj4gJMi4l7_6ecEaW5_QcLubJ-2AK1gofaJDR0CcFSlNlvLR_nutoFnIcbVSA7HxCm2-Dzj8jBBTAaEw5n66yAiJCF8Lx5y0CUB4aOUfzSKOIAaaU3I9olHn1gkfGTnQo_oMLaJ-24jBPbwT3M0rwHWB47XGHjj48iaqQl9EIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات مستمرة داخل معسكر قوات المرتزقة السعودية في عدن</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/naya_foriraq/92312" target="_blank">📅 04:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92311">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قوات التحالف السعودية تعلن اعتراض صاروخ باليستي أطلقه انصار الله باتجاه خميس مشيط.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/naya_foriraq/92311" target="_blank">📅 03:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92310">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d8b51349.mp4?token=vwA9Ng4jEsRvK7mHhddolzy29nipe9-Tq5ANLyQ1wXzQ8NLsg2y5i8l3KSjkPB2lAd7S108S7s-JI7NBgmfeDRBfeeRPLvPEPh_Pjgea7W_iH1ewi9d2f9Wt67sPV6cUJrKDEjOHPbeK9XqVmQmw9xbu1nCqnDd76qQeyQohZhENNKm6X9wnT0c6M77nO7If9gnpuyPyOt54IcXR1kH3E-Ju49oxvyndPYvcJobMQ8Irdou-qavVmh8hdRq4l7Shi25dXXliD4W30kqUKPdcP1YuRti_WIupin0macljy62D5-PnNPB0DPYA_1ZvtzqTo-S_59UTm-Ga5nteVrnccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d8b51349.mp4?token=vwA9Ng4jEsRvK7mHhddolzy29nipe9-Tq5ANLyQ1wXzQ8NLsg2y5i8l3KSjkPB2lAd7S108S7s-JI7NBgmfeDRBfeeRPLvPEPh_Pjgea7W_iH1ewi9d2f9Wt67sPV6cUJrKDEjOHPbeK9XqVmQmw9xbu1nCqnDd76qQeyQohZhENNKm6X9wnT0c6M77nO7If9gnpuyPyOt54IcXR1kH3E-Ju49oxvyndPYvcJobMQ8Irdou-qavVmh8hdRq4l7Shi25dXXliD4W30kqUKPdcP1YuRti_WIupin0macljy62D5-PnNPB0DPYA_1ZvtzqTo-S_59UTm-Ga5nteVrnccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات مستمرة داخل معسكر قوات المرتزقة السعودية في عدن</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/naya_foriraq/92310" target="_blank">📅 03:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92309">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c47ccb5bca.mp4?token=I7KLKnfvvnQ7_lK_NNjzaP_0tZkozWHv4JzUqt1Xc-qV3Q9odH6EpQpMWlnzmdgp4MkRpQF0QsFpxVa-ByqMHShWxzv3eOgfjiANlA4mnnX7X9ccb4c9j8qDV1X9aQY0xDz5LzMNDxt82P5jeD0ql1Lay6Wa8jT6FmA7RMc7UX3Fty8cEfxxKTRVRNn7VravBETnUHIySEGwWXnRhDsg0RaXKgbTrsBrGwKVOp3ChDb2wlGpnAXhD7sz0_9JoBnQ5VinyJdYzW1VwJLwUTIzqWqVwBO-iW5AFf-wB-CnXv5H7pBOenmjDjubN9h_a3UDp5SXigVRdCU7E1oR3R7QuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c47ccb5bca.mp4?token=I7KLKnfvvnQ7_lK_NNjzaP_0tZkozWHv4JzUqt1Xc-qV3Q9odH6EpQpMWlnzmdgp4MkRpQF0QsFpxVa-ByqMHShWxzv3eOgfjiANlA4mnnX7X9ccb4c9j8qDV1X9aQY0xDz5LzMNDxt82P5jeD0ql1Lay6Wa8jT6FmA7RMc7UX3Fty8cEfxxKTRVRNn7VravBETnUHIySEGwWXnRhDsg0RaXKgbTrsBrGwKVOp3ChDb2wlGpnAXhD7sz0_9JoBnQ5VinyJdYzW1VwJLwUTIzqWqVwBO-iW5AFf-wB-CnXv5H7pBOenmjDjubN9h_a3UDp5SXigVRdCU7E1oR3R7QuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات مستمرة داخل معسكر قوات المرتزقة السعودية في عدن</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/naya_foriraq/92309" target="_blank">📅 03:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92307">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a01896a2.mp4?token=UR8SetR2cIrtWOpgqAlrAxu1iuPzZ61kz2GnEZbKCYGpWGc5xuBkYtI6-i4F_D3eM7byQahNhh5ZfEvBecdD3KvY--fohTyDmwjdwIgyQK4FZbOAk7uVb67jJIaL2x8oZdYyOMcIjMtVcDBO6zKLrefgWXrxlu8jedcFO2SYICa9m_qXJTTh53arMbduvmGMEj5Aa6LO9_Jo2yqgw-hdGm13YMCpp83nrI6lby_w--Qh2KiiCYjeDtjMxd6b_dtxcbpaYCAFfy4O9AbIGulm76rSNOr57DQ4ENZ2mUF9XPnpcClncqNJbvWnMvIPdNfi_sabxexUH8K2_FmbwqKdCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a01896a2.mp4?token=UR8SetR2cIrtWOpgqAlrAxu1iuPzZ61kz2GnEZbKCYGpWGc5xuBkYtI6-i4F_D3eM7byQahNhh5ZfEvBecdD3KvY--fohTyDmwjdwIgyQK4FZbOAk7uVb67jJIaL2x8oZdYyOMcIjMtVcDBO6zKLrefgWXrxlu8jedcFO2SYICa9m_qXJTTh53arMbduvmGMEj5Aa6LO9_Jo2yqgw-hdGm13YMCpp83nrI6lby_w--Qh2KiiCYjeDtjMxd6b_dtxcbpaYCAFfy4O9AbIGulm76rSNOr57DQ4ENZ2mUF9XPnpcClncqNJbvWnMvIPdNfi_sabxexUH8K2_FmbwqKdCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف القوات المسلحة اليمنية لمواقع مرتزقة التحالف السعودي في عدن</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/naya_foriraq/92307" target="_blank">📅 03:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92306">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇸🇦
مشاهد أخرى من الحرم المكي تُظهر إبعاد الحجاج عن شخص يُشتبه بحيازته مواد متفجرة.</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/naya_foriraq/92306" target="_blank">📅 02:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92305">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb7qt4bSlWfQe7TUmvwzTiz7T5d-H0Cb6RViuCDuUxH8a_Ga6Z1Fc6anwRChoilc_I37JbDx-kdychPqeZ70aK2_Nxz0UFftLuFEkkpdbM_8n_M7Hd5jtmQzWdsWH9B2WJ3LUHsiNHu3qEK2XiCwtxvUJGjxDJzSURZn2_TDKfmomgtQ5_vox_uAgupnQNstjT6phrGFHvd3HRlA4vqzlKJ7rtNbSL9gaLM_75078ifzIWrWwrhRLfiMWmBYEIfcCRpo17wxslSR7cIxVi9fXzq1MuxploK-mSFFAxcTOqwT3eq7nmjj_85uhLaljVtE5nY11j1RWO1-LrtVtPOjew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد الرياض،توقف حركة الرحلات الجوية في الدمام شرق السعودية</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/naya_foriraq/92305" target="_blank">📅 02:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92304">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ec9b5c12.mp4?token=fLPRVvqPw3LtmXTKOiHDefeVBF9Q4aSR-fwlE98oBOm3irz7S8ycgd2n7ZUavM-hXuOf2aggvQ9UyHiGotjtlhcckdg8pL9_t-CVvaH4LpX5AqFiEqrJHX1C7wejBmwd6aNmbNQpigMw1fxCCX2EBxcu2Xh5gCpHe3mwE4UT_lv9Kr4EyYZ6mUtU_L6sS7qe26rxDdGyMmxZ-8-FfSEH3nPurp9nfRgvFV9aCl-wvUFVl22PZIzw0pCy8CI9tQDxIadfWxZIW3QRlVlOatpRwmeOjrxLK01BzR85z479YTFzVm8aEMFycmUI3xRjiTwKcGrNT0x4Q98OtrwvLcl5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ec9b5c12.mp4?token=fLPRVvqPw3LtmXTKOiHDefeVBF9Q4aSR-fwlE98oBOm3irz7S8ycgd2n7ZUavM-hXuOf2aggvQ9UyHiGotjtlhcckdg8pL9_t-CVvaH4LpX5AqFiEqrJHX1C7wejBmwd6aNmbNQpigMw1fxCCX2EBxcu2Xh5gCpHe3mwE4UT_lv9Kr4EyYZ6mUtU_L6sS7qe26rxDdGyMmxZ-8-FfSEH3nPurp9nfRgvFV9aCl-wvUFVl22PZIzw0pCy8CI9tQDxIadfWxZIW3QRlVlOatpRwmeOjrxLK01BzR85z479YTFzVm8aEMFycmUI3xRjiTwKcGrNT0x4Q98OtrwvLcl5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن إيران:  إيران مستعدة للاستسلام. سنحقق الفوز بسهولة بالغة في الوقت الراهن</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92304" target="_blank">📅 01:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92303">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0492e588.mp4?token=YE_gy8OguvyyLcdVZDMg4SKfgLvPjOOHUIMOqxmY1NKk7DXgCsu3aeXAzv-ScpPdJKcPB8jFW1bim6zXJl_oWytkPxaU4hxoOdat7RF4me58VRf8FFCASC_y8AiH-vMI-Ng7ClFCt4T3IOaXezvVg71pvaPoK6ToEd4naaDys5HNpnxPzvH1sfYY2dZMDUtnMU8__PP1p0cxwgV3P84hZwSyQpkJ_UR0to8AQSO0_aKVc91dZET-WIQ_7xV0rePZTl2uoZJcfJvLTgkEgTCJWOEvCqwf2TQ1So_ZcA0k60H_lfPMqFzhgd6jRiHMp7Gwt8u4KTvuD0EBJ3R1SPwhVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0492e588.mp4?token=YE_gy8OguvyyLcdVZDMg4SKfgLvPjOOHUIMOqxmY1NKk7DXgCsu3aeXAzv-ScpPdJKcPB8jFW1bim6zXJl_oWytkPxaU4hxoOdat7RF4me58VRf8FFCASC_y8AiH-vMI-Ng7ClFCt4T3IOaXezvVg71pvaPoK6ToEd4naaDys5HNpnxPzvH1sfYY2dZMDUtnMU8__PP1p0cxwgV3P84hZwSyQpkJ_UR0to8AQSO0_aKVc91dZET-WIQ_7xV0rePZTl2uoZJcfJvLTgkEgTCJWOEvCqwf2TQ1So_ZcA0k60H_lfPMqFzhgd6jRiHMp7Gwt8u4KTvuD0EBJ3R1SPwhVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن إيران:
إيران مستعدة للاستسلام. سنحقق الفوز بسهولة بالغة في الوقت الراهن</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/92303" target="_blank">📅 01:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a92eaf392.mp4?token=N89h7Ekr1HGJw-bLjTB_EEirOKosn8a6PYsPAg9YaZTILl5BYDZ-63NHfgdsLO4V2GxjtpkJq3bAUmCP9uMsGW04CPFnGJ9hr4OUQlIm5X4g_oxU3JzvZHbrxKYcA3LnsZX2bmnWP14KjFn0paXLkc754X6HVatKWk7CIbpTu9DUubNrgT9m_X_hHWDCTDmBNZFJU3BYSU2jH29q7CbY3QX3ZCyWbf2JZvS_wAEVs1zIgWIv0G-IjefsKHFUnej0gPhgzhnrxbDcCzj-5PqBoyj-GYCe4lvrpb5UMObCqyI1YAB-ZikLT1hSS-jwoN8vJaacw9DYgt3ae5B-6hcHcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a92eaf392.mp4?token=N89h7Ekr1HGJw-bLjTB_EEirOKosn8a6PYsPAg9YaZTILl5BYDZ-63NHfgdsLO4V2GxjtpkJq3bAUmCP9uMsGW04CPFnGJ9hr4OUQlIm5X4g_oxU3JzvZHbrxKYcA3LnsZX2bmnWP14KjFn0paXLkc754X6HVatKWk7CIbpTu9DUubNrgT9m_X_hHWDCTDmBNZFJU3BYSU2jH29q7CbY3QX3ZCyWbf2JZvS_wAEVs1zIgWIv0G-IjefsKHFUnej0gPhgzhnrxbDcCzj-5PqBoyj-GYCe4lvrpb5UMObCqyI1YAB-ZikLT1hSS-jwoN8vJaacw9DYgt3ae5B-6hcHcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
بالفيديو المتداول من حالة الذعر التي اصابة الحجاج بعد الانباء عن امساك بشخص يحمل مواد متفجرة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92302" target="_blank">📅 00:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92301">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/92301" target="_blank">📅 00:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92300">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇪🇬
مصر تعلن دبلوماسيًا إثيوبيًا "شخصًا غير مرغوب فيه"، وتأمر بمغادرته في غضون 48 ساعة</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92300" target="_blank">📅 00:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b57ca628.mp4?token=PDHVdL8OyrWUdiL319rAE5rZi593vyVTN_qjc2e8WUcZknpUnbIvIbdjWK_uWoOWtdEyntNJZl6rB4XmyIU6051BcajfHVSvJM0jqAXb7mpm3xZxFU95ZvlKChNKGp6MSTHDhtvWAbDSFndJv3PGmdGEKDyKPcsTSmdOD8Yp5rtUPUNwd2Wh4nBRVqO8LECeqlxF9dzp0jYzda2KU4-jj30wu3m1In0bNKpM0OfZ8E204fad2xHZEu3Q4YGBwrj2ij_EyAU0ZLDV0Uk8n3rcTHZznYeFpxZOQgAWQAJjBn67NcQPb-P_jUwQuFFJXwFHVBlc7G-FeKo6flB0nVNKBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b57ca628.mp4?token=PDHVdL8OyrWUdiL319rAE5rZi593vyVTN_qjc2e8WUcZknpUnbIvIbdjWK_uWoOWtdEyntNJZl6rB4XmyIU6051BcajfHVSvJM0jqAXb7mpm3xZxFU95ZvlKChNKGp6MSTHDhtvWAbDSFndJv3PGmdGEKDyKPcsTSmdOD8Yp5rtUPUNwd2Wh4nBRVqO8LECeqlxF9dzp0jYzda2KU4-jj30wu3m1In0bNKpM0OfZ8E204fad2xHZEu3Q4YGBwrj2ij_EyAU0ZLDV0Uk8n3rcTHZznYeFpxZOQgAWQAJjBn67NcQPb-P_jUwQuFFJXwFHVBlc7G-FeKo6flB0nVNKBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
السلطات السعودية تلقي القبض على شخص  يحمل مواد متفجرة داخل الحرم المكي.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92299" target="_blank">📅 00:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92298">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0add1fe8d9.mp4?token=eyNzZRk_q92c_X5m4TDdOXECBm4RIC52eFR8JdQ-TuQ2KR85xxe6UExXkMdKM9N2U5eIutfmQfr8LBBfdY8bSKZIUrdS8MQFjhxAFpeChKr3N82VqcE1Fi8j2HsG2f6RPaB6pAEde3cK_ma-hOqPbjfL6P094OXcdY2-cU8rSgm3uAFwRrQe_fKNqmKBMCBd1i6oUQe9K5a_z2fdloTleWWn2zu5NdRKix1r8imBRniwmX52miZkgv-O9r5KT7PJ2yXYe0bq9UkcOejgA8TnAs6PFaWMVZmtEnXXtQZi8yImqwornWMhK9bbmG5H5TWqHO6_-3awl9nQDAjQ1LqDWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0add1fe8d9.mp4?token=eyNzZRk_q92c_X5m4TDdOXECBm4RIC52eFR8JdQ-TuQ2KR85xxe6UExXkMdKM9N2U5eIutfmQfr8LBBfdY8bSKZIUrdS8MQFjhxAFpeChKr3N82VqcE1Fi8j2HsG2f6RPaB6pAEde3cK_ma-hOqPbjfL6P094OXcdY2-cU8rSgm3uAFwRrQe_fKNqmKBMCBd1i6oUQe9K5a_z2fdloTleWWn2zu5NdRKix1r8imBRniwmX52miZkgv-O9r5KT7PJ2yXYe0bq9UkcOejgA8TnAs6PFaWMVZmtEnXXtQZi8yImqwornWMhK9bbmG5H5TWqHO6_-3awl9nQDAjQ1LqDWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
السعودية تسمح بدخول انتحاري داخل الحرم المكي</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92298" target="_blank">📅 00:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92297">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇸🇦
السعودية تسمح بدخول انتحاري داخل الحرم المكي</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92297" target="_blank">📅 00:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92296">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇸🇦
🇾🇪
العدوان السعودي في وسط الاحياء المدنية بالعاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92296" target="_blank">📅 00:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92295">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
‏إيران تعرض السماح لمفتشي الطاقة النووية بالدخول في حال تخفيف العقوبات.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/92295" target="_blank">📅 00:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92294">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8GSvCZ-9UzRDwM9gQH1wveXrb0X7Ly2pBwzCI3zAP9nKYpncLHLJXabfq_qQui0hRDPMCTRXNLxNHB34xso89419XtZxd0LbDkSOIw4IjvGSLqVH8aMVGMUyd_KRvgNGVXBuqlJ6mChNmTDfe15Sh12y2WbBgnM519PdvjBWXktDnE_iyfEAOt8fGAhnJWywzrmYf20h9ddIyoBcbdkC6z2FvReWgcbX_xfYEdTKDYJ2siNEUj6u1SUrILARYPXrZl71HpMt1VOnUeLd6szXVgfUjT51ZohpgULkw-NnQMdgLA-cvXCk9-l9PKAKH3hEfh_b6IZDVs_oc7yp-BNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
من العدوان السعودي الذي استهدف عاصمة اليمن صنعاء.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92294" target="_blank">📅 00:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92293">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75906a072.mp4?token=fGriO14fqztplMq7KYgSFlkkV6niC_rLLt7_efTb0G7mX7m_GwzsuvnXbPv8yYy656pMaEJUmUKQ1xtmew6cLFEv95dJVTvMouZD_9b7DEH3LaQOwyc3zDXINF6JM63AYqVn1eWoX0eYBmHTFUHvyiZ7UdEfnQsC_587PargiVcnHiGwlbnjQsAobw8wpswpHgY8mDjMhSnPjlrqPPQTj4ZJWbX2pZzMb5Q2coDvcecRrzB0U4UKHjQrMgF80K7fpEaQxSUWtHIK5x3xZ6X332BZ9JFWqSa3kd6CJEpV1-7z4pU6TYPDMoywqlcD5JZwOMd953EZmwDKOrS3IZoicQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75906a072.mp4?token=fGriO14fqztplMq7KYgSFlkkV6niC_rLLt7_efTb0G7mX7m_GwzsuvnXbPv8yYy656pMaEJUmUKQ1xtmew6cLFEv95dJVTvMouZD_9b7DEH3LaQOwyc3zDXINF6JM63AYqVn1eWoX0eYBmHTFUHvyiZ7UdEfnQsC_587PargiVcnHiGwlbnjQsAobw8wpswpHgY8mDjMhSnPjlrqPPQTj4ZJWbX2pZzMb5Q2coDvcecRrzB0U4UKHjQrMgF80K7fpEaQxSUWtHIK5x3xZ6X332BZ9JFWqSa3kd6CJEpV1-7z4pU6TYPDMoywqlcD5JZwOMd953EZmwDKOrS3IZoicQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على صنعاء الان.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92293" target="_blank">📅 23:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92292">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-7Xix1FbsM9gle3LDWIJU035xfzqHyW9_ttKU1bGwkToUhimz48Rts-ZgX7ykejCrY5zB713F0SmYRrobLI2buCvTk7ON6ZEMnbbfDAPsAZvcXd_uMa0Z-zbFK7TjKiD7KcvYQUWzHH_5ApWa47-Tg7tGeoeLYd35wF0bubkLPIElW7ssksTYgcpDUG7uW5noaIJjd765VvWI9bgBx0ul6BhZ9BYItnKpwzhHLExOJRKpTPeuMpWvNuNS8x_ylJh0HS50JEHQgupmoe5ZINmELfjZuK1feE1uczj7jKnMnBMpgHErRVq-6FsCn7uoDJZ3DR-Jgnr5QpVH178wtgCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على صنعاء الان.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92292" target="_blank">📅 23:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92291">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doyFQ17YVPcgEOVSZkeZ-F1vFpyrh_3f9Jx9Xt0kFHll-8yx8FyNKA4PSW4FhXeQ8VKcftE7gWEcQW-xd9v_q10QkrH9iewY7IWBI3Q7Z7II3QgjQ1O-Anrl5cYK9WWOYAC14O1sSbEBN6VyoLvPQ9y4f3wdaZ6qPLC-rOiXPZaw3whoQPtV1cxGg-BtXgrr7yJvx9J06RdpyqsyhpW1Untexm96WSPx0jV-f8osJ1zJ-l3kxi7zdioW3ZxBPDAlRfLFG7VQxnBV2d74SW7P7D2kOL_d7gn1pzO3qmiSy9AdurjfqoWrj1xJTqDGA6v6pyVVm3_OTjXKoBLX98qJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تعرض سفينة في مضيق هرمز لإستهداف بصاروخ من قبل بحرية الحرس الثوري واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92291" target="_blank">📅 23:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92290">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9xqHdiwQz7ArrMzOjC-22T3KarqRvbY3BdD1s5eg-kEyO9w6UWjYcNlqzyU9L23NToY1iwxCAoIAKeGIyVyPIsY2xP_Fh7YY66DJHa7Dqi76LUVK_MnetUqih8altKpkTo8A5meghMXC9yzFt5RGGTzLhBmAP7lNxHhgcMrV69qXhOYDS-N6M6pHz0Ru9My1eIpGpr7VO4lPZch2RnPwX2RPVis9h3Br-gIzqwSSebY-eeSlyPuYXXd9KXOMlOnEGfKrCzclGWPXQuX0QTHL0dX7rqepk5wQoMaAvkNSIYAWIEwu-9JwzW_YCRSvxzaXZGpQIJltvH5YCYwnLLbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
انفجارات اخرى في جازان نتيجة هجوم بصواريخ باليستية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92290" target="_blank">📅 23:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92289">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇸🇦
🇾🇪
صاروخين تستهدف جازان وخميس مشيط.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92289" target="_blank">📅 23:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92288">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUdhk7UY0zSWY2eQdUjLtcL0VAad9iU-8_PEXAhactrL2PJeCpjxonPwcPCf2DOMmW1ROtLUTnbsgArwcv7cYAURFt0zsFXAam2BMsqsMMmBvBaQOgS_CRthlvjdAElNY_izUtv1FGKE2CMyBuhOeXt1MnDreJP82QaJuc-dpNHb5qqaUmwhd1YqmIKeVSiK2WMG5wioazMWxR0ykp9chNDNeRwXHhCLTVlNPppaOIwz9TrXkeI8ohRjOd4L2rEzq6zSfv2SS9PyeKztwM7j6rCHKzyi8zaLsqhD678Cx7SODhhRJeV-dCdeffwGYOY7SEHb9XXwjU1tmrbFHUWU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بيان وزارة الخارجية الايرانية بشأن القيود المفروضة على حركة الطيران بين إيران والعراق
:
تدين وزارة خارجية الجمهورية الإسلامية الإيرانية بشدة الإجراءات والتحركات غيرء القانونية واللاإنسانية التي تقوم بها حكومة الولايات المتحدة لعرقلة التجارة والنقل الجوي الإيراني مع الدول الأخرى من خلال تطبيق عقوبات أمريكية غير قانونية خارج حدودها، وتؤكد أن هذه الإجراءات لا تتعارض فقط مع المبادئ الأساسية لميثاق الأمم المتحدة والقانون الدولي، ولا سيما مبدأ احترام السيادة الوطنية للدول، وانتهاك المعايير الأساسية لحقوق الإنسان، بل تشكل أيضاً مؤامرة خطيرة لتقويض العلاقات الودية بين الدول، وخاصة بين الدول المتجاورة.
وفي هذا الصدد، تُذكّر وزارة الخارجية بالروابط التاريخية والدينية والثقافية والشعبية العميقة التي تجمع بين إيران والعراق، وتُثمّن علاقات الأخوة وحسن الجوار بين الجمهورية الإسلامية الإيرانية وجمهورية العراق، وتعتبر القيود المفروضة على حركة الطيران المدني بين إيران والعراق منافية للمصالح والمنافع المشتركة للبلدين.
تتجاوز العلاقات الإيرانية العراقية العلاقاتث التقليدية بين البلدين الجارين، إذ تقوم على روابط شعبية عميقة ومصالح مشتركة في مختلف المجالات. وتتطلب حركة ملايين المواطنين الإيرانيين والعراقيين لأغراض اقتصادية وتجارية، وأداء فريضة الحج إلى الأماكن المقدسة، والسياحة، والتعليم، والعلاج، إدارة قضايا النقل والاتصالات بين البلدين بنهج مستقل ومسؤول واستشرافي قائم على المصالح المشتركة.
إن القيود المفروضة على حركة الطيران بين البلدين، بالإضافة إلى تسببها في مشاكل خطيرة لمئات الآلاف من المسافرين والحجاج والمرضى والطلاب والناشطين الاقتصاديين من كلا البلدين، تتعارض بشكل واضح مع طبيعة العلاقات الاستراتيجية وعلاقات حسن الجوار بين إيران والعراق.
...
🔹
تدعو الجمهورية الإسلامية الإيرانية، مع احترامها للسيادة الوطنية لجمهورية العراق، إلى اتخاذ القرارات المناسبة في مواجهة الإرهاب الاقتصادي والتحريض من جانب الولايات المتحدة، لرفع القيود وعودة رحلات الخطوط الجوية بين البلدين إلى وضعها الطبيعي بما يتماشى مع مصالح البلدين.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/92288" target="_blank">📅 23:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92287">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
تعرض سفينة في مضيق هرمز لإستهداف بصاروخ من قبل بحرية الحرس الثوري واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92287" target="_blank">📅 22:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92286">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن استهداف خميس مشيط باربع مسيرات من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92286" target="_blank">📅 22:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92285">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن استهداف خميس مشيط باربع مسيرات من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92285" target="_blank">📅 22:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92284">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
🇮🇷
‏ترامب، رداً على سؤال حول ما إذا كانت الولايات المتحدة سترد في حال ثبت تورط إيران في الهجوم على الطائرة: ‏"سيتعرضون لضربة قوية جداً، لا تقلقوا."</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92284" target="_blank">📅 22:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92282">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
‏إيران تعرض السماح لمفتشي الطاقة النووية بالدخول في حال تخفيف العقوبات.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92282" target="_blank">📅 22:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92281">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPOJqE8UTbb7lj9P2d3ohTV_BHmVzByf26dI0R46G2dlcbf9RK4gS87tKU7rdi9B5bDwoXAYsHN3OIMTF8mDoRpbdHTkrrFVz0LeM-aEhtdw5PKzPVrt7bOCgzqUWgpb-KhtgTR6VzajSZifYf3Rpa0dUnWBCL6MMtRN1GNz02UpjAu1hVQfxTSKjzeABQTJbrd8Q0lBaJAZkQ_pYkuk89qvMkNRjvw7z4rjLoTKqxrRcV1Ecckg_lM2-WZHcV4BD1I5NIRV8QqB37VSYCSIIb10eTJ8Of4aPmy3qy8qEMdwu78uUkVkozckIVeEnfWy3oR1_O261B-4tlG04zqcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تتجاوز 101 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92281" target="_blank">📅 21:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92280">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29f31a6f6.mp4?token=jYe3l8PTC7uRKzeoXna7HTHHPAYO2TF7VYuZmezIDdMu3Q4dip9l7m81UUWeyVAmJA7Th_v-Pr_jwzxtr3pn_BXjeUqCFBKMzpNiZ3u_Z738bLUuQGzEEdkKsov_tWLYy1PYuQ18lF6968LQZQx3mCq594vrhm4t7R6H9jK8pK74R6hGU3ZoDRI8o_wifSUcMJ71-Wo55t8rj8OATicX69ftgq4GrurI6bTEKx-7EjpiFCG1KWFg9CZDfGVuSGrtObmytObOERESqvF9N7cvcgJE1rL3IdETyS8qXdeNgXceBhqesfcPW5q90WaLketBIEXX1ETqsDdSV7kr6I2InW4rwt9a2ERbOIfjetIzMf0FyUCGTZbTCNukUw0GDrPRdodsKdsIpCPQzBghc-6Ks10R-WTfCTvFuQJ7nidR-rI068bbyqJQBdTzRb483pAVevThKzdgtHe6EAL7SegJyZS1FcA7bRv6nkk69eZPO-PXsJL6O8Vb_j9cUgnArWSRRQ0cWeLFlsuopIeH3vUf2rYkxsprEJBdnln1qfcsnRns0LeUVuUhrs8j1IL9llYXa-D7AT75DQV6Ut2Tv0f61Hke13GDqFPLz-bJYBOIcQHE24-8K0Dfm5gHsIzDuw7unxxrRk5IXxCY0-Tdu8Zgdmh9Tu7wrnpZQGa0bJbT_L4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29f31a6f6.mp4?token=jYe3l8PTC7uRKzeoXna7HTHHPAYO2TF7VYuZmezIDdMu3Q4dip9l7m81UUWeyVAmJA7Th_v-Pr_jwzxtr3pn_BXjeUqCFBKMzpNiZ3u_Z738bLUuQGzEEdkKsov_tWLYy1PYuQ18lF6968LQZQx3mCq594vrhm4t7R6H9jK8pK74R6hGU3ZoDRI8o_wifSUcMJ71-Wo55t8rj8OATicX69ftgq4GrurI6bTEKx-7EjpiFCG1KWFg9CZDfGVuSGrtObmytObOERESqvF9N7cvcgJE1rL3IdETyS8qXdeNgXceBhqesfcPW5q90WaLketBIEXX1ETqsDdSV7kr6I2InW4rwt9a2ERbOIfjetIzMf0FyUCGTZbTCNukUw0GDrPRdodsKdsIpCPQzBghc-6Ks10R-WTfCTvFuQJ7nidR-rI068bbyqJQBdTzRb483pAVevThKzdgtHe6EAL7SegJyZS1FcA7bRv6nkk69eZPO-PXsJL6O8Vb_j9cUgnArWSRRQ0cWeLFlsuopIeH3vUf2rYkxsprEJBdnln1qfcsnRns0LeUVuUhrs8j1IL9llYXa-D7AT75DQV6Ut2Tv0f61Hke13GDqFPLz-bJYBOIcQHE24-8K0Dfm5gHsIzDuw7unxxrRk5IXxCY0-Tdu8Zgdmh9Tu7wrnpZQGa0bJbT_L4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من ساحة التحرير وسط العاصمة العراقية بغداد، حيث تصطف النعوش الرمزية لشهداء الحشد الشعبي.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92280" target="_blank">📅 21:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92279">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇸🇦
‏
الداخلية السعودية:
قائد الطائرة ومساعده غادرا المملكة متجهين إلى أبوظبي صباح اليوم.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92279" target="_blank">📅 21:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92278">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5a-lvORcjvFOGmxRVC4ZTTaMPHWcEXi2gtDg9ANWwx8fHvAQKHXmq5qCrPA-aExMkkRKx98_GT05qpFtDV0YH5Bhm7dQKM9yHIj1MBhVYC7h4geMjslpgMjBcR0-U6HIWrbLsjvHUBGbCtdJSGUXeXQ7o74WqJOJthrmL6fFMVXlG34niQqDiRJaPwqb79fsjEaLXIyVfehN8cJK6oyHbj8ets5dxUVT_ojHLy018FXdtCekkmR8Xl2_bxZsLWAv9dq-E0mP_Yfeo_8haK-n8ettvPRcrAELN55xd4aH0bcx9qTHybQgMkEQpzTBChpZyT2JcJymFi66fxKuezgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: ذكرت، عدة مرات، أن الأمر سيستغرق 4-6 أسابيع للتخلص من التهديد النووي الإيراني، وفعلت ذلك في ليلة واحدة! بقية الوقت هو فقط للتأكد من بقائه على هذا النحو.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92278" target="_blank">📅 21:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92277">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da0c14d8e.mp4?token=l9ACZF8WZTmr5JhkTr1TZG_fQ19Omk2mB4GT-cB6S7k3dazHOftv9_Qv31tQBlGSi3YVhg3R0qIB4oDqEDWeISSveac2Hqahy48NBidqfipwJPIZuXiCZ2qDaYNei1P8_Nr65xiX9IErAQL0SgjQtvdkKzvGAN-BaBCQPtMJam2MK04PFHCkN7XqvR5rYyH1wCNYxWeIXu5LD2WbzMmGeHUVPRbQsdpk6Ifqc2g2d-atZKBuBuTU0f_ZUUGrvV0Hfc0xtNE5ViWZ2UKTrPf0o2QmQt6LqkDb4v07NLfy87iYBB2F9p5QLJIZSCFTauo9CWvyqMTT1-nDpaH1DEbQdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da0c14d8e.mp4?token=l9ACZF8WZTmr5JhkTr1TZG_fQ19Omk2mB4GT-cB6S7k3dazHOftv9_Qv31tQBlGSi3YVhg3R0qIB4oDqEDWeISSveac2Hqahy48NBidqfipwJPIZuXiCZ2qDaYNei1P8_Nr65xiX9IErAQL0SgjQtvdkKzvGAN-BaBCQPtMJam2MK04PFHCkN7XqvR5rYyH1wCNYxWeIXu5LD2WbzMmGeHUVPRbQsdpk6Ifqc2g2d-atZKBuBuTU0f_ZUUGrvV0Hfc0xtNE5ViWZ2UKTrPf0o2QmQt6LqkDb4v07NLfy87iYBB2F9p5QLJIZSCFTauo9CWvyqMTT1-nDpaH1DEbQdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات متواصلة في موقع الانفجار واللسنة اللهب ترتفع.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92277" target="_blank">📅 21:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92276">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
عمليات قنص نوعية لوحدة القناصة في جبهات جيزان تستهدف تحشيدات العدو السعودي من يمنيين وسودانيين - 01 أكتوبر 2026م.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92276" target="_blank">📅 21:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92275">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع: ‏
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 47 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية من شبكات اتصالات ومدارس وغيرها فى محافظات تعز وصعدة والجوف من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من جيزان.
‏ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1256 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92275" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92274">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فيلسوف السياسة  بمناسبة الذكرى الأربعين لاستشهاد الدكتور علي لاريجاني، لنتعرّف عليه أكثر  #نسل_الشجعان  انتاج نايا على التلغرام وفاء لخادم بنده .</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92274" target="_blank">📅 21:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92268">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rw3Ohz7uGOrqNtsYmufhYfkVwg2vOuzGyQ2hdNVjtiPqPKStfb5YTDHVsWMMQ2hd6PO5PXSPQPFJKrMkhzuIlDqdD84TQuGWFdYDNxS52oP8lXT1rqz1x8seA2hF5OdCRT7gw3JJD1p0UnOp20VrP8ZnkL63-Pbq_Ly8Zs6k3qRZKviMgwAAcSHK770DogupVZ9sgva6Sp6Gdxm716Et_Hv971lhPx4mNjap-vhyC7mqdDACGv1U9KK-4GKdnBfB2pEZuGW_gmuF69iBZrWzsLo9BKzwdh9btiYydKV-DgdYLJWR-zjYML0-9su1uBM_Hq_1cfJxZ1N65YuaFxxYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWaL5WdtrC3yxs8AOe0fcDoq_0AWAVGdANUakVxukhgxdDqoVrEtyHzYttWqwFuDe3txsSxKCMHKMu0W2zBCATwKnIBhbrjbN--m_EfjYIaQVfxJNMk9gLT7sUl4mgudZXvGwTUdlTn6oV5TgfEfh-ipPUJRQkk_sqpdryKb_3GCRhLJmjaks1cel2YwkOpL31PwriyA6O4KAq-2CLCqdpqGdByLZCINz53mXpYPSo78pMRQN-Vcrdp2GPjRVyfnZ8OuvzBvqw5g6Fc6uZr-DqizK8hQTPSRLj98XEOaei7WWdZZL1GtLWEjtqnV8H3Bf9VAFJCZJh0kDuUbMNIW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szDohnN13_1T4f9NQMKbFsbZCFwdrWAwNVo96-ySXnOwky868Wx7eI7egBN0KeudCQnkD2ExK1W4ll5DBTWbnwlx0cNYDvoFJChqY10yp005DoWYYsUo8E8r0mNMvCB-4tOYymgAQLzmBdnIP8kk8ojSD-vwPlogvVChb_h0v4qd0l9qRhKqhZLGSSxqbkS4pBSRL_1rWaSR9V9IENIbAsAoaZGPC6VOUMtFicy2acN8jjM0xhzIkQqETpbLIGsaZVEhWqrNcCKk5BhQ7rzjGZfbHDL2XRQ5UnlDu4RRWh_qEfF5Q2ke9XRevomnm6bXgvLQAgkUPZRiK_iCjy-cqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNSbYX987m8q-hBDwBKBleKT0N9IuwJpDmzy12z33qCb6azvtZ_3PRownT7w-TuYR29YdXcfJKQIp0h8-ard7nQ2jfmkVj92yP3W6Ky-QAeE5sJdRCIxtRnwn9y_T3mIAivB2LrTC0lVkSqohjAENOklQSonXlnSRzK4CPwD4MG6I9NSRBlbrwifYDg_OJm2SnSLRRPwxSrJp_Wm26ZhsfNxoKKMNit5vHVcmfnNnm2ZIV5Fg80F0YHKoiFo4V5_QVALSbndyaNeuRbR7xmcEe0uTkckgj98F0qIhOmSKDDX5g1DyZB0oC4E5dKMW_-nQz34oWc4aV3DPV-C8Mgcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gh8f8FLEta861-POStvN_IzpaHt97rlx3-VZoeDzNT-b0EVoy96COFHCmjgetSicC5TuAZVDUs87uu6B6jyZnICqL_Q82V7HxAE6zg58_ylVZ7grjhbAwvKUT4wkF_gW0Va7dnUBYRlCWWLpKhX1jDq9XHOJNbm5UYG80cC88z9GHtmy5f-uLAYoDXQoSwfiLeWqwkT0NB-gwvmlSkYynNE0MwIYTK-IO30NoqHAucSM55R8wI1Ru56LgiY-jUbw1fVflTN3neoyj5goxDDR-UCF2hDFGwOIF-ourKWWlKawlBnY-or8cWaNTK51WlXzuiQyW8IA8zsD28yLJOwKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgfAGafkiJ2jz5QM0tHX8xrPnq8OPvgMN0-RksstIZotL3LX7mqun6WVP01hee3Lew5CPb0wuRvzmbo7vV6Gcr6VckWDBBKgluuRFJ9gXcaYwr0EAqhq8zZGN3MiZV4vgIbw2PSCENHHNs5kEvpFLSEM21dsCSO9pXDtaNdJzUSHez0jVnjZ1HdpZVqacck71s_jQE-g15LgwrKp746S4tKsn6-lATkfDrIb-O844iZMoJo-I88gqN798SJhcfTMBputLgKyserSSRk5X3h-Bew2boMYIvgtTN4y31XALMOtWa8fkGrkzRvBim0IA-GHFee0debmFHzIKZjTv3Cg6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
كتائب حزب الله في العراق تطلق ثلاثة قنابل في يوم واحد.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92268" target="_blank">📅 20:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92267">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
🇮🇷
‏رداً على سؤال حول ما إذا كان للطيار أي صلة بإيران، قال ترامب: "نحن نحقق في ذلك، وحسب ما أسمع، نعم".</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92267" target="_blank">📅 20:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92266">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
ترامب حول إيران: الآن يجب عليّ اتخاذ قرار. إما أن توقع إيران على اتفاق، أو لن توجد بعد الآن.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92266" target="_blank">📅 20:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92265">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
ترمب: إيران وافقت على ألا تمتلك سلاحا نوويا.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92265" target="_blank">📅 20:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92264">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
استعراض جوي للقوة الجوية وطيران الجيش في سماء بغداد والمحافظات، غداً الجمعة، اعتباراً من الساعة العاشرة صباحاً، احتفالاً بهذه المناسبة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92264" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92263">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQgZAkhkb7feBUqY9GatgsEkJmSeY5XMpROdhU_taxQpdM34iSXBj08L5TYkP8t7pyeROv4TlK1RcKHVueU9_4ggIzkK7gfkq9DLIOFeqhRwRCd12Y5Fb_25lcoQR5hslEkxMQ1lRPe-lUzs011XOu_7OMUsmVQ4P38zaeWeyxf1xNqKxiEIc3rLvyihejx8rWZ_o-UbCOtAX-3f8onl2izY_ZjZ8WfEO43-Tl8OO-pccoeuoyrQuuiaLk_CTezqUP91ABnR-S5izoDuxPjGdxVzF_4f5p0IkhHQIHIFe4XkAvBZG0_v3hWYYDm1GOtxDpBDGzOZOuMNYH1QnPwW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعترف باستهداف مباشر للقوات المسلحة اليمنية لمحطة الطيبة الكهربائية وخروج عدة محولات فيها عن الخدمة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92263" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92262">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/278f98e7c2.mp4?token=Nwe91Ga-NEHqwh1qqFQFz8QVCDgoIKrL0DsA3SI8yjeRAB3TfVLz3vJ9f6-2FuBEINZMvEuUZItWlj6uPQAcJquJlQJrczXqc4w6bW9A8f7K_n8rLjeMNXiMpWIbV3XSHwlICQEeJkwZFfJmT3LazLAtvUTkGEy7FXd4W716RNUX-rzadf1dQ1PbB5t8Nie9jfseJByYA5O8skofgNV2_cDr769eMSXBgVXiC0fI7KXDeY3AkSJwxPlwZILL9b05l7xJTS_PWvY13TpPoq893f32epl-ys5zyRUSQMuvgnu5f1OXfmMNju0PeG0SIyGKxJhNExtUC6gZeY4laKDA-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/278f98e7c2.mp4?token=Nwe91Ga-NEHqwh1qqFQFz8QVCDgoIKrL0DsA3SI8yjeRAB3TfVLz3vJ9f6-2FuBEINZMvEuUZItWlj6uPQAcJquJlQJrczXqc4w6bW9A8f7K_n8rLjeMNXiMpWIbV3XSHwlICQEeJkwZFfJmT3LazLAtvUTkGEy7FXd4W716RNUX-rzadf1dQ1PbB5t8Nie9jfseJByYA5O8skofgNV2_cDr769eMSXBgVXiC0fI7KXDeY3AkSJwxPlwZILL9b05l7xJTS_PWvY13TpPoq893f32epl-ys5zyRUSQMuvgnu5f1OXfmMNju0PeG0SIyGKxJhNExtUC6gZeY4laKDA-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترمب
: إيران وافقت على ألا تمتلك سلاحا نوويا.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92262" target="_blank">📅 20:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92261">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a2797024.mp4?token=sl_uMkpKc_jG56WuTuGh_AxbX-1QbJWAleyzY5c1tBgBKZ3XDfwcrPXIez0R3eKQdVZhqEPyL9uewCvfwxlQSJ25RsNkHQC_JoAncVACdN5qQyVBoVGC2NtPfeVNoQ6eA693rTWEwu1czK8I8umHjThW79HUbIzOb5G9_th7owSg4todF6-GCO9d5vKYhIz9SD4zmZaUSIF7Nvu5Zj5_kHSVaKm3e5-uuUueo85pqsuEpTWdWJn2DHtyfCCGcB3KpxS_vTvj6I_pB8QKqkal49nbEOL7tM6t6F9HLsKDqtLtNewVVtFQ76wq_iN7wkkS9e0va9aKlo1Wc1H3CzNFMG2QiCPndU342rqG0BV7WFJctFTTw7c8tzzwmfhZuXR2TIVqWNGg7jsUNG-V2MgnpVrw_-W-OvLnFD6rfatpzJ5XLAbs1JnhCZ1vHUMisZvA0kuzX8UnskyrlAdeqaQR0tqtdpcaP6l2sNHFHXQ2aNezTbEjHdtmSk9YiBqv7LzRmmn6Whz1mTCc5lw2UkjpzH852_7gHVCSse3kg0NrgU3_OkieAskGDSLQSw0hf6UOiajTkz1iLODz22Gobwm3zlB8m9WTsp98jO4REwoJJ5ZbEw_-ifZZy9WCwyYEssuX5rcnjazK5jGxj5WlSQHF8YYDBSWTl_Uv4aIWtxVORfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a2797024.mp4?token=sl_uMkpKc_jG56WuTuGh_AxbX-1QbJWAleyzY5c1tBgBKZ3XDfwcrPXIez0R3eKQdVZhqEPyL9uewCvfwxlQSJ25RsNkHQC_JoAncVACdN5qQyVBoVGC2NtPfeVNoQ6eA693rTWEwu1czK8I8umHjThW79HUbIzOb5G9_th7owSg4todF6-GCO9d5vKYhIz9SD4zmZaUSIF7Nvu5Zj5_kHSVaKm3e5-uuUueo85pqsuEpTWdWJn2DHtyfCCGcB3KpxS_vTvj6I_pB8QKqkal49nbEOL7tM6t6F9HLsKDqtLtNewVVtFQ76wq_iN7wkkS9e0va9aKlo1Wc1H3CzNFMG2QiCPndU342rqG0BV7WFJctFTTw7c8tzzwmfhZuXR2TIVqWNGg7jsUNG-V2MgnpVrw_-W-OvLnFD6rfatpzJ5XLAbs1JnhCZ1vHUMisZvA0kuzX8UnskyrlAdeqaQR0tqtdpcaP6l2sNHFHXQ2aNezTbEjHdtmSk9YiBqv7LzRmmn6Whz1mTCc5lw2UkjpzH852_7gHVCSse3kg0NrgU3_OkieAskGDSLQSw0hf6UOiajTkz1iLODz22Gobwm3zlB8m9WTsp98jO4REwoJJ5ZbEw_-ifZZy9WCwyYEssuX5rcnjazK5jGxj5WlSQHF8YYDBSWTl_Uv4aIWtxVORfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
أنباء اولية عن انفجار كدس عتاد بجنوب العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92261" target="_blank">📅 20:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92260">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
أنباء اولية عن انفجار كدس عتاد بجنوب العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92260" target="_blank">📅 20:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92259">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انباء متداولة...
تم ابلاغ عدة شركات طيران عربية من ضمنها القطرية و الاردنية بعدم السماح للمسافرين الكويتيين من ركوب طياراتهم المغادرة الى العراق بدون وجود كتاب استثناء رسمي كويتي يسمح لهم بذلك.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92259" target="_blank">📅 19:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92258">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعترف باستهداف مباشر للقوات المسلحة اليمنية لمحطة الطيبة الكهربائية وخروج عدة محولات فيها عن الخدمة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92258" target="_blank">📅 19:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92257">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c3fcb712.mp4?token=TIccFBHwN_hnVwgJLVsoCr7TUDgbbXB4MEmmbzLcwCfgPP2YKXP3sRddYbWj_F70_LeM_kEGJcTm7rHzR5b8ZeK1dSJ1jl7F-jfku9Ne9l4VRIxAeDleQYqr1gXXGNffnEuUGu4PeLs30cZEV1cWZ7dSURvYd2iA_Nb0HKs1RUkaFyga3IW_SPGOJCW-UBpMlURJ8gYbyLlEcCstAS2pUsWgdJ4oohekvYXsgiwDmZLn3usOMEFr5bcupIZSC1oHRbvAUdFOKVu3psNGUjlKOHInFWGz95AMOjYtjRTQGHjBXhWL_CiR-V5GG6Zf5GrTeD4AYw50XyldAJhV0BZZajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c3fcb712.mp4?token=TIccFBHwN_hnVwgJLVsoCr7TUDgbbXB4MEmmbzLcwCfgPP2YKXP3sRddYbWj_F70_LeM_kEGJcTm7rHzR5b8ZeK1dSJ1jl7F-jfku9Ne9l4VRIxAeDleQYqr1gXXGNffnEuUGu4PeLs30cZEV1cWZ7dSURvYd2iA_Nb0HKs1RUkaFyga3IW_SPGOJCW-UBpMlURJ8gYbyLlEcCstAS2pUsWgdJ4oohekvYXsgiwDmZLn3usOMEFr5bcupIZSC1oHRbvAUdFOKVu3psNGUjlKOHInFWGz95AMOjYtjRTQGHjBXhWL_CiR-V5GG6Zf5GrTeD4AYw50XyldAJhV0BZZajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
بوتين:
إذا تعرضت روسيا، أو منطقة كالينينغراد، لهجوم مباشر، فإن مسألة استخدام جميع الأسلحة التي نمتلكها ستطرح على الفور.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92257" target="_blank">📅 19:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92256">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRRDzOUiQpKIzCnN1U0b7CXZUGDZZbHXL4jm0BfpDCu9A9gsDY2eQCJ4XHawzKKzKyZk-PR3zY6ulVPB2zaBYgkM3svk2dwpAnPwU9C6nXQKDi9C0s_66vLk9MtfqHI6mCpXmuT1hmPnQBsvjr5DBsp93zrtDMNQVusE7Y3hJh6CAkRl4RHU6hK9ka64B3fUNscIRhBiled1DcqwbflrL0fvK50SGLTgATNLa7YUz_vOJxPTQLHpD_eo_e-Qj4IgV2v1ScbQmH9W1J8d0h3xMMOEmaFjhX3pKphOqCQHcvGSVNsg9oDVWFAy9QC6gTVtacauKkOWXD2N8k4Efp6Uiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
سقـ.ـوط طفل في بئر ماء من سكنة قضاء البعاج في ناحية ربيعة بمحافظة نينوى والدفاع المدني يستتفر لانقاذه .</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92256" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92255">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASrQclgdAnqmHevC2PNRygOlaaclktaWx1lsnFqJejtxhClWVyuNVzyMns8teuKsAagnlpXM-8uckXzZ7kFsGGBksFY83fyrYFbLSyCJ0R_XwHfTGDdBXoO0NWAWvSqb0IdsM5iuUwTzynUhMblaXgPQoEPJ0wqxbchymMzVjaqU9WleQrlAu11is5VWR7B1RYRys2oSLZPphB-YEes8MBM39cKuckZDOVgzqSCXrV9gnBLQeLQCx-hnCAo4ydKdIzMr2HBrzyuLLTiPqPR6QTQ6ib0m_X0LtW9l6bkd_s6UCgmlr-4OaUwkX6Dd-gu-uvOGVMJf0eZaT9904x27LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
المقاومة الاسلامية كتائب سيد الشهداء
:
بسم الله الرحمن الرحيم
في الوقت الذي نبارك فيه لشعبنا العراقي الصابر إنهاء الوجود الأجنبي من أرض العراق، وقطعه مسافةً مهمةً على طريق استكمال سيادته الوطنية، فإننا نؤكد ما يأتي:
أولًا: نجد من الإنصاف أن نتقدم بالشكر إلى الحكومة العراقية، ممثلةً بالأخ علي الزيدي، لما أبداه من جهود حثيثة ومساعٍ جادة أسهمت في تجنيب العراق اقتتالًا شيعي ـ شيعي، والحيلولة دون انزلاق البلاد إلى فتنة داخلية.
ثانيًا: نعلن التزامنا بالاتفاق المبرم بين الاطراف المعنية، وبما جاء بخطاب القائد العام للقوات المسلحة العراقية ، ما لم يُقدِم الطرف الآخر على مخالفة التزاماته وفق البنود الموقع عليها.
ثالثًا: نتقدم بالشكر الكبير والثناء الجزيل إلى اخوتنا المقاومين في جميع الفصائل الذين جاهدوا وضحّوا، وإلى من استشهد منهم أو جُرح أو اعتُقل، في مواجهة الاحتلال الأمريكي للعراق منذ عام 2003 وحتى خروجه، مستذكرين ما قدموه وعوائلهم الكريمة من تضحيات خلال سنوات المواجهة،
رابعًا: نتوجه بالشكر والامتنان للجنة الرباعية لما بذلته من جهود مضنية لإتمام الاتفاق المبرم، موصلة الليل بالنهار لإنضاج بنوده بما يخدم المصلحة العليا للبلاد.
وفي هذه المناسبة، نؤكد أن سيادة العراق واستقلال قراره الوطني تظل غايةً أساسية، وأن المرحلة المقبلة تتطلب تغليب مصلحة العراق، والحفاظ على أمنه ووحدته، وتحصين ساحته الداخلية من كل ما من شأنه أن يعيد البلاد إلى أجواء الصراع والاقتتال الداخلي.
المقاومة الاسلامية في العراق
كتائب سيد الشهداء</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92255" target="_blank">📅 19:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92254">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇱
اعلام العبري:
أفادت تقارير بوقوع مشادة بين وزير الخارجية التركي فيدان وممثل "مجلس السلام الإسرائيلي" آيزنبرغ خلال اجتماع مغلق في نيويورك الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92254" target="_blank">📅 18:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92253">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
الحزب الديمقراطي الكوردستاني يتهم جهاز مكافحة الإرهاب بقتل مدنيين اثنين في حادثة التون كوبري وتسليم جثمانيهما إلى ذويهما على أنهما من "قتلى داعش".</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92253" target="_blank">📅 18:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92252">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
حاملة الطائرات روزفلت غادرت مع مجموعتها الضاربة قاعدة سان دييغو متجهة إلى الشرق الأوسط.
مجموعة الإنزال البحري مايكون إيلاند غادرت سان دييغو إلى الشرق الأوسط الاثنين الماضي.
أكثر من 2000 جندي من وحدة المارينز يتوجهون للشرق الأوسط على متن مجموعة الإنزال.
بحلول نهاية نوفمبر المقبل ستنتشر في محيط إيران 3 حاملات طائرات ومجموعتي إنزال.
مع حشد كل هذه القوة في الشرق الاوسط سيكون لدى القادة خيارات كثيرة للتعامل مع إيران.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92252" target="_blank">📅 18:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92251">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a54c8a6b.mp4?token=Ei7_h-6p9r4DaiQU_SWCtG9kYyz1EIvCKLTkRtTz9gz3HpjNBUkIykG2d7IgbdLMu5AKh0Lkyn-PcaEwizCe98HSuElrIti4CIb0nf43L9kz25ZpZM6HqQNJ-yxZurhWxIDrogK8kOLi-0sRqmsYssQ52WpYg930ucLCmeFGygmeR5sNw7rQqcsUxXF3MjlFheDTFTXpzlk6VPytyDALcrz4Dm-M_d1a7Ly-fZBOqt9fGwlXzcKV9t65EGyPjZaL2GeY5ia_7TnsDQFii-EBQfQbkjiDO1_Txo_j7nwj2C5qtY-isUP2JbNpYoRco4AxxlgVNH5HyNjcIJ-2zWNzwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a54c8a6b.mp4?token=Ei7_h-6p9r4DaiQU_SWCtG9kYyz1EIvCKLTkRtTz9gz3HpjNBUkIykG2d7IgbdLMu5AKh0Lkyn-PcaEwizCe98HSuElrIti4CIb0nf43L9kz25ZpZM6HqQNJ-yxZurhWxIDrogK8kOLi-0sRqmsYssQ52WpYg930ucLCmeFGygmeR5sNw7rQqcsUxXF3MjlFheDTFTXpzlk6VPytyDALcrz4Dm-M_d1a7Ly-fZBOqt9fGwlXzcKV9t65EGyPjZaL2GeY5ia_7TnsDQFii-EBQfQbkjiDO1_Txo_j7nwj2C5qtY-isUP2JbNpYoRco4AxxlgVNH5HyNjcIJ-2zWNzwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد تظهر التقدم الكبير والسيطرة على مرتفعات جبش حبشي في محافظة تعز من قبل القوات المسلحة اليمنية بعد دحر مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92251" target="_blank">📅 17:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92250">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IF6LN9IOFxYRkBsxoornmrSFkAdXVDf0PwS7tE4FUcV4KTvF68MIeYNfn2xGc1p7YeRQgWNnhOI6MDbiWvB4l1NkyTuSwmW5Wg2MYKi-XeXDvXkhnZYdvh1wvbbJSNcTcnBbmQdoOvV6tkzuVvWf6lnG3mWu0db81glxhRAId25D8p6PHZvV3mKER1UgVzy2qmFLfhw7y3hxfZonPDasN0HybXHiwwhRw3P8t75FwjN38K85mtv8AQeQElvV57vcECjUBihgQies5gYuTGMyGjJ9QE4_6zmxAeqS5GfltnXDd4RdogVTlkMcv4U3150LJQxuIZwMa_6BIISt-1ok8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بيان المقاومة الإسلامية حركة النجباء حول طرد الإحتلال الأمريكي من العراق.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92250" target="_blank">📅 17:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92249">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-s5GNpxo9ul71r2mJ2NabFaO2PQvyVrpQr8MuTw9n1uSW4JSf9IVD2KYfHNg-SG3dtC6FiOFqckqLneC0fpw2LavsZlw-dOUEDfsZnKroIDras8dmdqFRlf11_boQwCbuMD3ZjiVE0ggw01TAE9Sez7e4yycx1mcbjxbv99zA_4eX2uYRAB_Pi7GiUSy_chati5koz056nqPjkedB-xJTB4XFyymc-rlRd9muQuIIQMi0Zm7mrI5BfQqQ1_dieS4STere0ECCM1gfWs5YHezP39IHRJfpX4tGyT3VOIWYx36y-h7F-ZV6kqKGwc6QbiiAA6n96znJMZrWBuhMTh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تتجاوز 101 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92249" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92245">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcicm3Muvm3FFjskB7Sk0G9ukjBV7QG1MuSZvDT4JnIEfPjJbL9PpccazRMzCGthj71MfeVw-Dl1QdV_x1FK4tztbgicoBDtFKx8fqkh9zWY0rwk3AVssHRStOJNbn0P2dBj6rYfFlZhh0r9L4iIHH5tJA59UmmSYCgHlXKX3x-7ciHkl4WK7nliVuVtbKHktPuBKv34umBGrpuhgv_0J4KQx4xnvrhTTlDRzbeFLXNY3lW5DO_WCH9SMLPWsxqem5tY1eCYSk9SwVhDZlrNHX6TnAXmaqSLeCaTwnKs4oEVHL_2jSVB7Se7ZNFYYHWMs-MIcXoONZT2OwdY89iZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRjHTpyT6zFFVwOcZIggrxMEN3DGkY2EB4zMPYmODzUn1sfqiVY3T3t4kjivffmm1ltcA0HmnQzMj3rh3mHk-KgwBPDv-HdPJgidt2FZK2hgBQgIgxCMtB4usOrLqWMzvpr4-1sMM3jC3YseAKZV7l1k6o9eMyXU-5jRBD96aP1orlXfQE1SXLVnqvprPXFGdTJEQ-5QbCd1D3sSNFX8G_VCOUySU5xbRd5ckuN9To6uazcHvJ9FqD0a3GK7E9X7SJOexDBvbeJar5ox6rS-upN0mUeP3A5Mk7sURcZ4u1j9d7DBD6u76G2HHCELgQRnuLDnGUE1kyfhvyzCV43yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOwHQKhQv-5pgmjqrTRqIAqDerRzPFU4fiMrrO9G_mxqDyWlKJhGH1-YHRZRM_beBcnpzLeTWnlzMGLt3CJn_lCnVXLxSMYUoVzHsCgkY2C3J2UJ-lRtfL1GcU4unYF1WmKSdOfMo3zCYPkxtcQw9GwBA3orNVwQRo8LVn5R_fhR03qRkKaOBUQhKDigrKH4sUpvsi0xygPcRYYtW9s7-eMDFFea0awmKA7yFFXKh_SQO7Jbx3b3rEuNLGrRhJJJ24C8tZGjDGJtowBN8cgJH7fc3ppf0BJIhCbATNCFWce3i5s_OuYsSnEQAj2WPgMMCEw_wAw1snu6zUU6ToefXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGib-mZQcoDU7oT4bbaq2WX-Zeaf_Qxp_oH43fMtQtwAB3tz-xg1qmVGSsAAnZ1QTn7mlUjqsX3ihxXNgMqOU1ktjV9PZ1fij8lFaCuXUVrvT-spALU6kgjFlwEkML8AdgNKMuBE8wES-bvfSj1Yut81IvANsv6K0gZHlRJdf1w5bLkUo5oGOiptLzfh1SHFCBSvR2YCwb2xuNl2l0Y5PTwE8sVr1Z52Ez8kfyG-X91Pg4VLgT7hrUDOMZssm3bj8yHLAZ_CVhz6csRSoEQJ-3yzsbI0nCWV51RJzJ7cO7pIZLcuCu3QGfZcaWGupjj-VYERW55JJOvg1uC4WDN7-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇶
🇺🇸
مسيرة كبيرة لقوات الحشد الشعبي بمناسبة طرد وإخراج الإحتلال الأمريكي من العراق في العاصمة بغداد.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92245" target="_blank">📅 17:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92242">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bC1Yiw0TiCrlrEH5oby9ZTssQAAPpLfjja2NwGcMa3q0cijOYyT0b52GiO5IWo4xnG6W798e6l6COSLdSuTK3tw0S2-gnXYE6I6Wh7cjr6RKGBI-_-dV4k9UwySDZZ2CqttjQGUTPYd5NMsfOPBb1p1Hhr-PaE_mvoYZLyBUpv0hg7h9_IYGaP_1vylrel9IJ9e_Ci8C--wxe_2xzWN0GAw8LeZFBD49WBOc2lUrDXYQxR93ojA19SEESqqnvNkhBAIe09BPJqPX0HU_PJJ0NL6XsrNZHUm1-86B4QwCec8z4ZJ6LJXW_Lvm5WkeGt3dGWisZ7KH2xZ3RgFsdla3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvOVastEtPS-xfbmZIKxpxYc_FIkxzWF6_c38IrJwY6CbFeOsLm7ZIICdTWixa_U2a23Oa74UwUqFWuqoDSSKBTe4ga6njh_0npxeA_h9qywPCP7InxyEABdR-TFGrw353AFm1ForzvvrpL6CZBt3C-mIT5OQd2IF8Q-DdwA7hD2qZxbSvrkgo-Lcwqa03cI09QKqysgdlJgGhm98dm1J-2P8M5owDbx7b73NO0pbGhGgG9-tAXfRko3axZ-_sxvc0JMtOcV3o92ywgKfgRbnSFItFfNaWShgSvWWKGg5-p51_cSK7IwyGvdhQcFAArdWFnNR2I0nV-dM5Z_ynzI5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYmONqly4qeI89PBtsMqo08Qh3kAW3By6c-_5JEAMOxEDDUdFPmMzjfFVzX8NZKdyuKqLPsQ2MMw5NNLfz9TUho8ImcSefX2dYeNL5Ue7nnDHSRH_O1lwXcPJjbgaWiBZAB0nk4Huqiher4DTuAcojcMuye6DT558mR5oYeGRDr4blm_pWICpMuLbjZe1D5dsLQ4ilWMJCST-RLqU8XQsel_RZWCWmMd3hIcTQqudJOV_oSDj2HLr4SrahXQhvF2jYY7AfH2hAGh1OZTlvxxaOcIY7Mq4_iAf1eblCUEialytqI6hqbsqgMOCOkuX1ezXcWfjt9INJIChVkkWnYQ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇶
🇺🇸
إستعدادات الحشد الشعبي لبدء الإستعراض الكبير المزين بنعوش رمزية للشهداء، في العاصمة العراقية بغداد إحتفالاً بطرد القوات الأمريكية المحتلة من العراق.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92242" target="_blank">📅 17:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92241">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
وزير الأمن الداخلي الأمريكي:
ناقشنا مع بريطانيا تهديدات إيرانية محتملة لاستهداف مصالح أمريكية بالمملكة المتحدة.
كنا نعلم أن إيران والحرس الثوري قد يحاولان تنفيذ هجوم يستهدف مصالحنا ببريطانيا.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92241" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92240">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">القوات المسلحة اليمنية تشن الهجوم هو الاوسع منذ هجوم الساحل الغربي على مواقع المرتزقة في تعز وسط تقدم للانصار والسيطرة على مناطق حيوية مهمة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92240" target="_blank">📅 17:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92239">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e4750734.mp4?token=WirWCLssqomkSDl0ffWRywHiPRDJw528FbpL39ygAfuaWpV46VUAnjAGMRGHpQbRI7dIm-1temvcn7AIupWcz45FEbNQBo6CsGiNda_0afrQOD75DWVuQ0iRrvcKjsz9KOKqQNrHTw3pVi7cyrkwQ1YkG2bqiLMW5XpBdFzdwf_8wncllnhfi3sn1UIKoYqZ8-P1_J_KIwCfqTARGLVK4tTIbJ3ZF4NJNhkvP-2XgMMEJDIyzh_dRkHa1hr3bk4Ea5d-oyr7rINkuHVlO-cCOuIiw-c6tiNq8oHvPPEcCgZHhXzSfKvhbQt-teLKV1FLQjkZHIlvAVE8o6RepdknmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e4750734.mp4?token=WirWCLssqomkSDl0ffWRywHiPRDJw528FbpL39ygAfuaWpV46VUAnjAGMRGHpQbRI7dIm-1temvcn7AIupWcz45FEbNQBo6CsGiNda_0afrQOD75DWVuQ0iRrvcKjsz9KOKqQNrHTw3pVi7cyrkwQ1YkG2bqiLMW5XpBdFzdwf_8wncllnhfi3sn1UIKoYqZ8-P1_J_KIwCfqTARGLVK4tTIbJ3ZF4NJNhkvP-2XgMMEJDIyzh_dRkHa1hr3bk4Ea5d-oyr7rINkuHVlO-cCOuIiw-c6tiNq8oHvPPEcCgZHhXzSfKvhbQt-teLKV1FLQjkZHIlvAVE8o6RepdknmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇶
🇺🇸
إستعدادات الحشد الشعبي لبدء الإستعراض الكبير المزين بنعوش رمزية للشهداء، في العاصمة العراقية بغداد إحتفالاً بطرد القوات الأمريكية المحتلة من العراق.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92239" target="_blank">📅 16:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92238">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
حادث إنقلاب عجلة يستقلها ضابط برتبة عميد ركن ورئيس أركان فق21 سابقاً في الجيش العراقي وبرفقته امرأة وهم بحالة "سكر" في منطقة اليوسفية بالعاصمة العراقية بغداد.
"لا يابه دمجوا الحشد بالجيش"</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92238" target="_blank">📅 15:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92237">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇱
نتنياهو:
من الواضح أن مساعد الطيار كان انتحاريا.
قد يتكرر الحادث لأن هناك مؤشرات على أن إيران ووكلاءها يحاولون شن هجمات ضدنا في موسم الانتخابات.
هناك ثغرة بشأن فحص الطيارين ونعمل على معالجتها ونتعاون مع الإمارات لضمان عدم تكرار مثل هذا الحادث.
سنتمكن خلال أيام من تحديد ما إذا كانت لمساعد الطيار صلات بإيران.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92237" target="_blank">📅 15:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92236">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الاعلام الامريكي: ترامب يعتقد أنه من الممكن تسريع قصف إيران بعد الانتخابات</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92236" target="_blank">📅 14:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92235">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الاعلام الامريكي: ترامب يعتقد أنه من الممكن تسريع قصف إيران بعد الانتخابات</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92235" target="_blank">📅 14:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92234">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDGaVyA0rcZvs_4X4GuOGLdJL8t29cVoXg79_YsVG4zkCTBqjELdfft77MSoQ9cNg5fbo_1uWVKAAQOeCyyz4Qn3gl0bpVEeF9ZPXbTfwpIHzaTmkgjRFQ8hSlkwiPJb7A-76dWLhzzpum8BUnOiPf2S1fGqUfjUFX843IQZKwdBzzz0dKfPDBubC3L6cLuo_MgLluS1Wh9E8jIIQs9LMPLp9to_bfqy0OuRPdPmnwqIvqKaz-XMc9Vtk1SMcaumA1F3mC9kqVzWMxD9VYwI145uhofKrVG9-1Tohruq5iXTGc_rG8J0ekJ-oMK0uS2lzjCEPZMjLUFScie2P-4AnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوات الطالباني تخلي سيطرات كفري–سمود، وبرلوت، وكلار–ميدان، وإحدى السيطرات في منطقة سرتك التابعة لحدود دربنديخان لاسباب غير معروفة وانصار البرزاني يتهموها بالخيانة وتكرار سيناريو كركوك 2017</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92234" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92233">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇱
بن غفير:
سأطالب في الكابينت بتسليم الطيار المخرب، الذي أراد استهداف مئات الإسرائيليين، إلى إسرائيل، وهنا سيشعر جلده جيدا سياستي في السجون، فحياة من الجحيم تنتظره هنا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92233" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92232">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رويترز تزعم: مسؤولون من سوريا وحزب الله التقوا في تركيا الشهر الماضي في أول اجتماع بين الطرفين</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92232" target="_blank">📅 13:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92231">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رويترز تزعم: مسؤولون من سوريا وحزب الله التقوا في تركيا الشهر الماضي في أول اجتماع بين الطرفين</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/92231" target="_blank">📅 13:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92230">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
وزارة الكهرباء في اقليم كردستان العراق تعلن تقليل الكهرباء لعدة ساعات بسبب اعمال صيانة في حقل كورمور.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/92230" target="_blank">📅 12:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92229">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزارة الدفاع التركية تعلن البدء في تسليم قواعد الجيش التركي في محافظة نينوى إلى القوات المسلحة العراقية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/92229" target="_blank">📅 12:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92228">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزارة الدفاع التركية تعلن البدء في تسليم قواعد الجيش التركي في محافظة نينوى إلى القوات المسلحة العراقية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92228" target="_blank">📅 12:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92227">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5bb77711e.mp4?token=HHGROBPuaW0OnngXlBkNLEVjAsKnoXV9w9x5s_81SvixJwWeKU6ul9ZvZbWc2Tb_XtGGLhnbNBNz8qLy-hHNSAKur7sdKCH7trcpAM4SYQvWaXBmMGe0P6aKQLL4Tnsa-FXc3uqIJ5ybWHXBiQR8uj0IHKuCoMgwQji0mRqHVq0rgNd4mL_dXlj6VGgLohzpjfCQcgUXNaou3ESqXgvIaJKdUAWMCXg8PMNja3ksNAX6_hJRxFJFmkI3UvdmgnrXvQVwfrcos0AgLejNTRBUlAQobEMWkUSDpvs5XNZXknJRRN2nntt--ShqdMExf0f90QePm_0ksDgLjq7cvU4FaJci0FJYZCa0NnIzzAhrhkhdKohwF_nKYdZuAkYsdIUguY3RRYHm5-nuUd-eO0DXw4LY61juP4B-4ZoB2ULZeuFxHnPOWCxXiN3qG3weNP21Im52ZluNXd-DoiQCXpVZ-DuqNG1k4p0AnY9cYckGBa0s_JlfU-UpD5heuZB_TrVuP8a1KhrJ7Hjbzo3vu-ZtG89PG8P8Xk3lyO5dx87auS2JNkl5GKqTEv_iS041xCG2orv6w9abbFYM8VIlB30OSTlrXWJuRu8u8bp6V_rX-5lGGb4L1HXcBgELGGsepU668zvM4dlvc4K13vNsCDwuNo29yP0r0Rzkf1AcecZC5Ek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5bb77711e.mp4?token=HHGROBPuaW0OnngXlBkNLEVjAsKnoXV9w9x5s_81SvixJwWeKU6ul9ZvZbWc2Tb_XtGGLhnbNBNz8qLy-hHNSAKur7sdKCH7trcpAM4SYQvWaXBmMGe0P6aKQLL4Tnsa-FXc3uqIJ5ybWHXBiQR8uj0IHKuCoMgwQji0mRqHVq0rgNd4mL_dXlj6VGgLohzpjfCQcgUXNaou3ESqXgvIaJKdUAWMCXg8PMNja3ksNAX6_hJRxFJFmkI3UvdmgnrXvQVwfrcos0AgLejNTRBUlAQobEMWkUSDpvs5XNZXknJRRN2nntt--ShqdMExf0f90QePm_0ksDgLjq7cvU4FaJci0FJYZCa0NnIzzAhrhkhdKohwF_nKYdZuAkYsdIUguY3RRYHm5-nuUd-eO0DXw4LY61juP4B-4ZoB2ULZeuFxHnPOWCxXiN3qG3weNP21Im52ZluNXd-DoiQCXpVZ-DuqNG1k4p0AnY9cYckGBa0s_JlfU-UpD5heuZB_TrVuP8a1KhrJ7Hjbzo3vu-ZtG89PG8P8Xk3lyO5dx87auS2JNkl5GKqTEv_iS041xCG2orv6w9abbFYM8VIlB30OSTlrXWJuRu8u8bp6V_rX-5lGGb4L1HXcBgELGGsepU668zvM4dlvc4K13vNsCDwuNo29yP0r0Rzkf1AcecZC5Ek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار يهز محافظة دير الزور السورية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92227" target="_blank">📅 11:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92226">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار يهز محافظة دير الزور السورية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92226" target="_blank">📅 11:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92225">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات عنيفة تهز كييف</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92225" target="_blank">📅 11:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92224">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اشتباكات عنيفة تخوضها القوات المسلحة اليمنية مع مرتزقة السعودية على جبهة تعز</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/92224" target="_blank">📅 11:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92223">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb59079283.mp4?token=DTaYZPixmnX-GUJRVw9gWEy4FNCFVQBJbV6xhDPNzBPCMF6tc8Q8e_heoBunVXqVG7auLH8cvzxI-26qBcJoYTfSYOtfnv4eEXJtdmniMhzLYc5UUk57FE0XNWBMHJw3H5a6m8E8zyGRZX2SFOiWD7qEUc9kPltJeFZ45sHhB8BVqLw7vkx_ptaBEob12IZpAnfg9ti-WFjutOmmH9nfsbLLpD41rS9j8S97PXlefIaS2QBZAll3Zotnj-RmhxUPdpIggnzzoQ3KVzZXp35cQiwZuawxrHCoZGX2KBB-exS4BkogV-v1ZZ5pi5_S-jFYobIPm9NP31n4GaOzcUf97A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb59079283.mp4?token=DTaYZPixmnX-GUJRVw9gWEy4FNCFVQBJbV6xhDPNzBPCMF6tc8Q8e_heoBunVXqVG7auLH8cvzxI-26qBcJoYTfSYOtfnv4eEXJtdmniMhzLYc5UUk57FE0XNWBMHJw3H5a6m8E8zyGRZX2SFOiWD7qEUc9kPltJeFZ45sHhB8BVqLw7vkx_ptaBEob12IZpAnfg9ti-WFjutOmmH9nfsbLLpD41rS9j8S97PXlefIaS2QBZAll3Zotnj-RmhxUPdpIggnzzoQ3KVzZXp35cQiwZuawxrHCoZGX2KBB-exS4BkogV-v1ZZ5pi5_S-jFYobIPm9NP31n4GaOzcUf97A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات عنيفة تخوضها القوات المسلحة اليمنية مع مرتزقة السعودية على جبهة تعز</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/92223" target="_blank">📅 11:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92222">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">العلاقات العامة لحرس الثورة:
- يهنئ الحرس الثوري الإسلامي، مع إحياء ذكرى شهداء جبهة المقاومة الإسلامية في العراق ومنطقة غرب آسيا، ولا سيما القائد الشهيد الفريق قاسم سليماني والشهيد أبو مهدي المهندس، وجميع المجاهدين المؤمنين الذين نالوا شرف الشهادة خلال عقدين من المواجهة مع المعتدين الأمريكيين، الشعب العراقي الأبي، وجبهة المقاومة الإسلامية الموحدة، والمجاهدين الثوريين في العالم الإسلامي، بهذا الانتصار التاريخي.
- إن إخراج أمريكا من العراق جاء نتيجة صمود شعب هذا البلد الأبي وتمسكه باستقلاله. فقد أثبت الشعب العراقي، بصموده التاريخي، أن الإرادة الوطنية هي السلاح الأقوى في مواجهة أطماع قوى الهيمنة. وإن انتصار إرادة المقاومة العراقية الرافضة للهيمنة على الاحتلال الأمريكي، يمثل صفحة مشرقة في تاريخ نضال شعوب المنطقة من أجل الحرية.
- إن إخراج المحتلين الأمريكيين يمثل في حقيقته فرض الإرادة الراسخة للعراق البطل على النظام الأمريكي الإرهابي والمشعل للحروب، وحكام البيت الأبيض الذين يفتقرون إلى الحكمة. فأمريكا التي اعتادت التحدث بلغة القوة، اضطرت اليوم إلى الانسحاب من أرض احتلتها لمدة عقدين.
- رحلت أمريكا؛ لا بالمفاوضات ولا منّةً منها، بل بعزيمة شعب صمد، ودماء مجاهدين ضحوا بأرواحهم، وإرادة مقاومة لم تنكسر أبدا. وها هو العراق اليوم، شامخا وحرا، يقف على أنقاض احتلال دام عشرين عاما، ويشهد بزوغ فجر الاستقلال.
- لا شك أن هذا الحدث المبارك والتاريخي يمثل الخطوة الأولى في الثأر لدماء شهداء العراق، ولا سيما أبو مهدي المهندس، وبفضل الله سيكتمل الانتقام لدماء هؤلاء الأعزاء بإخراج أمريكا بالكامل من المنطقة.
- يجب على أمريكا أن تغادر المنطقة، وأن تترك إدارة الأمن لشعوبها نفسها. فقد أثبتت تجربة عقدين من الاحتلال أن الوجود الأمريكي لم يجلب الأمن فحسب، بل كان هو نفسه مصدرا لانعدام الأمن والإرهاب وعدم الاستقرار في غرب آسيا.
- بعد عشرين عاما من التدخل العسكري، أُخرجت أمريكا من العراق وسط مشاعر الكراهية والنقمة الشعبية، وقد تكبدت، بحسب اعترافها، نحو خمسة آلاف قتيل، مع الإشارة إلى أن هذا الرقم لا يمثل الإحصائية الحقيقية، وأنفقت أربعة تريليونات دولار. وهذه الأرقام تكشف حجم الهزيمة الأمريكية الثقيلة والمخزية.
- إن خروج القوات الأمريكية من العراق حدث تاريخي كبير وذو دلالات عميقة، وإنجاز عظيم لمحور المقاومة. ولا شك أن الشعب العراقي الأبي، بمواصلته هذا النهج المقدس، سينهي أيضا التدخل الأمريكي في اقتصاد بلاده ونفطها، وسيصنع مستقبلا مشرقا لنفسه من خلال الوحدة والإرادة الوطنية.
- لم تكن أمريكا يوما ولن تكون سندا يمكن الاعتماد عليه؛ فالحقائق والوقائع الميدانية تؤكد أن أمريكا راحلة، وأن الشعوب هي من يجب أن تبني بلدانها.
- ويمكن القول بحزم إن إخراج أمريكا من العراق هو باكورة إخراجها من عموم غرب آسيا وجغرافية الأمة الإسلامية.
- إن هذا الانتصار الكبير هو ثمرة الإرادة الوطنية العراقية، وجهود قوى المقاومة، والدعم الشعبي، والإجراءات الفاعلة التي اتخذتها حكومة هذا البلد.
- وفي الختام، يؤكد الحرس الثوري الإسلامي ضرورة تحلي حكومة العراق وشعبه وقوات المقاومة العراقية البطلة باليقظة والحذر إزاء المؤامرات والفتن المحتملة التي قد تخطط لها أمريكا وأعداء هذا البلد، بهدف إعادة إشاعة انعدام الأمن وعدم الاستقرار في هذه الأرض المقدسة.
ويعلن الحرس الثوري، بصفته من أبناء الشعب الإيراني، وبحزم أنه سيواصل الوقوف إلى جانب شعوب المنطقة المطالبة بالحق والرافضة للظلم، من أجل تطهير غرب آسيا من بقايا المعتدين الأمريكيين، وكذلك من النظام الصهيوني القاتل للأطفال والعنصري، ولن يتوقف حتى التحرير الكامل للقدس الشريف.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/92222" target="_blank">📅 10:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92221">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:
ستباشر الحكومة العراقية في دعم المؤسسات الأمنية بشراء منظومة الدفاع الجوي الكاملة، لتعزيز السيادة الجوية الكاملة للدولة العراقية، وتشريع قانون الحشد الشعبي وتثبيت مكانته في المنظومة الأمنية، كجزء لا يتجزأ منها تحت إمرة القائد العام للقوات المسلحة.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/92221" target="_blank">📅 09:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92220">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
القوات الأمريكية لا تزال مخولة بشن ضربات على الأراضي العراقية في حال تم اكتشاف تهديدات للموظفين الأمريكيين والمصالح الأمريكية في البلاد.
ستركز القوات الأمريكية الموجودة في الأردن على مقاتلي تنظيم داعsh، وستتدخل في حال عاود تنظيم داعsh الظهور بقوة تتجاوز قدرات العراق وسوريا، وفي حال طلبت أي من الدول المساعدة.
أما الميليشيات الموالية لإيران، فستكون مسؤولية عراقية بالكامل.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/92220" target="_blank">📅 07:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92219">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇵🇰
الحكومة الباكستانية:
قتلنا 22 إرهابيا ودمرنا كميات من الأسلحة في غارات على مواقع في أفغانستان.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/92219" target="_blank">📅 07:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92218">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇱
نتنياهو:
زودنا البريطانيين بمعلومات استخباراتية تفيد بأنه سيقع هجوم وأنه مدعوم من إيران.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/92218" target="_blank">📅 05:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92217">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3bb44f934.mp4?token=GFVGUiRvMC9qFK2i018fn1zdkNGHbthBtPx8pcxzXFOyj03uUJd47L5kWNPh7uLopxhWIxw3HNxuo8Ohjq1mJf25ZqgVBiYc9L0a7FgoHVSW5vjq-xZJD8RE2oJUCxLNGzwOeJ8_XPloCtxnWHvWo8mNEPUGOw5QcCu4tvq51UD1fPXrjedlLlNvYG7cQWjwiX8ctNlF81N7hQ3loML6g2pTr_TBwUfV2rtccIDOGnoUmBUxTSkyfdWhDM2JYmKnqp6AlqIjXjqRAYGvCOQ5ZXUcDVnpOTUcWlZfnWc7M6emVhP1mqC1hi6-g78Y3jNX0mgo36tCCKoS9b9QkkzNvjlLxCSitgjfpyk0fLvTB2AsOg2wwks3Jkt4bDj_8Gfr8Lqi9Gji38QyIyVaxG4ZhnUA2W8CBY_bWA3nDjCpqrR8t9hdjRlmmMxVVWl-o8mBiEBnujmvzxtn5rgbkwAqmg0vK6oA0ZghLrkPv3MUx1uWFUNee-qV82sZLwUjEiFHLpVxXVFKY_HJd5jqfzpL9T5JcMV4GTt0Lt3nlyPrNP3WNzHHfXoQImoheJmMVNQgyPVQgb9i69txbum_H6YOyeNcju5rJ8wdbVnRW84X3idHajp9q8Lx5gfNduOloII8xnJfUjOh_UAXf2BCtURImqXUVi1Xi_vRM7yogeOJbjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3bb44f934.mp4?token=GFVGUiRvMC9qFK2i018fn1zdkNGHbthBtPx8pcxzXFOyj03uUJd47L5kWNPh7uLopxhWIxw3HNxuo8Ohjq1mJf25ZqgVBiYc9L0a7FgoHVSW5vjq-xZJD8RE2oJUCxLNGzwOeJ8_XPloCtxnWHvWo8mNEPUGOw5QcCu4tvq51UD1fPXrjedlLlNvYG7cQWjwiX8ctNlF81N7hQ3loML6g2pTr_TBwUfV2rtccIDOGnoUmBUxTSkyfdWhDM2JYmKnqp6AlqIjXjqRAYGvCOQ5ZXUcDVnpOTUcWlZfnWc7M6emVhP1mqC1hi6-g78Y3jNX0mgo36tCCKoS9b9QkkzNvjlLxCSitgjfpyk0fLvTB2AsOg2wwks3Jkt4bDj_8Gfr8Lqi9Gji38QyIyVaxG4ZhnUA2W8CBY_bWA3nDjCpqrR8t9hdjRlmmMxVVWl-o8mBiEBnujmvzxtn5rgbkwAqmg0vK6oA0ZghLrkPv3MUx1uWFUNee-qV82sZLwUjEiFHLpVxXVFKY_HJd5jqfzpL9T5JcMV4GTt0Lt3nlyPrNP3WNzHHfXoQImoheJmMVNQgyPVQgb9i69txbum_H6YOyeNcju5rJ8wdbVnRW84X3idHajp9q8Lx5gfNduOloII8xnJfUjOh_UAXf2BCtURImqXUVi1Xi_vRM7yogeOJbjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هطول أمطار مصحوبة بعاصفة رعدية قوية بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/92217" target="_blank">📅 04:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92216">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
شرطة مقاطعة تكساس الأمريكية:
إعتقال مشتبهاً به بعد تهديد موثوق بمهاجمة مبنى الكابيتول في تكساس.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/92216" target="_blank">📅 03:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92214">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e16f07e28.mp4?token=Tz7SFZoSiwywSvpVowRfVb1SWotqKHTxJE-0d2itqd0X7o2tz7O6GRwcMqcr2OVml6VEvlcPR6U5Vp1nY5xBkSQGialPmrl9of-SybJqVdfv5fB9MqEOjSd-ADkP0tkyM-MhsIhBzDLgwNFHnFQUx6J14bvvmxNYfQxlG_q63vQh5Rzd0HhD2U26DzRQ6Hxqc0lfE3eWQyY8EOu6F3CxWbZv87-mc7xdSGmD7Gi2xpMd2ugu6SfZvTk1Ak1scV_dPBuFzjTcziVDDPXEReMQbVt_rBzvw0WO3MybGSE69L2denzSB4DZdut9eJVX6q79Qa20qruQd1r603jDuDrhTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e16f07e28.mp4?token=Tz7SFZoSiwywSvpVowRfVb1SWotqKHTxJE-0d2itqd0X7o2tz7O6GRwcMqcr2OVml6VEvlcPR6U5Vp1nY5xBkSQGialPmrl9of-SybJqVdfv5fB9MqEOjSd-ADkP0tkyM-MhsIhBzDLgwNFHnFQUx6J14bvvmxNYfQxlG_q63vQh5Rzd0HhD2U26DzRQ6Hxqc0lfE3eWQyY8EOu6F3CxWbZv87-mc7xdSGmD7Gi2xpMd2ugu6SfZvTk1Ak1scV_dPBuFzjTcziVDDPXEReMQbVt_rBzvw0WO3MybGSE69L2denzSB4DZdut9eJVX6q79Qa20qruQd1r603jDuDrhTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
محافظة البصرة في الجنوب العراقي تحتفل بخروج الاحتلال الاميركي من ارض العراق.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/92214" target="_blank">📅 01:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92213">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219db791e6.mp4?token=MT39-xIQgNtirC_2MLRakZdCVp3vPPg7K8stqNDG09YIUS3vhyL72jWCxRDXV3yyOgNBj-2N7qZpQ_iTMOAVHaGQzmpBdbJAnnl9dZJgLBAk4IBTH8fXFIMuhquUMeQIEYo8qcF1AVJnYo-DfopRHBsDT5EIIyjgdTdjSD323WYThdoJtZ3ZccUIKbcxIqyVQ5x8gUl8uKQvpQ8vy1psIt0D6xIzK9lRYVd9PnhSSL-iPRSxdkz-i05mE0SYfOj447YybcPMVjyd0GIa8ItDmYXHXgaJg5WZhhiHHCzzC9UkOKCD83b_rjOCTtcIiVNXCIJPWmKxdKsxyK3wzJQlrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219db791e6.mp4?token=MT39-xIQgNtirC_2MLRakZdCVp3vPPg7K8stqNDG09YIUS3vhyL72jWCxRDXV3yyOgNBj-2N7qZpQ_iTMOAVHaGQzmpBdbJAnnl9dZJgLBAk4IBTH8fXFIMuhquUMeQIEYo8qcF1AVJnYo-DfopRHBsDT5EIIyjgdTdjSD323WYThdoJtZ3ZccUIKbcxIqyVQ5x8gUl8uKQvpQ8vy1psIt0D6xIzK9lRYVd9PnhSSL-iPRSxdkz-i05mE0SYfOj447YybcPMVjyd0GIa8ItDmYXHXgaJg5WZhhiHHCzzC9UkOKCD83b_rjOCTtcIiVNXCIJPWmKxdKsxyK3wzJQlrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">س: تصفون الإيرانيين بأنهم مجانين. كيف يمكن إبرام صفقة مع أشخاص مجانين؟  ترامب: ربما نقوم بتدميرهم. يجب علينا اتخاذ هذا القرار. إما أن ندمرهم أو نعقد صفقة. الوقت قادم. الأمور ستنتهي قريبًا جدًا.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/92213" target="_blank">📅 00:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92212">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeeb9329cb.mp4?token=X9WLICj5FcHob1StBh4yigCpsaAloMWrVSJH6rCWoCw0C7JjaQ3drf_kBShCWsVXQQabAsEp5qQhetP-2NcCD2ECLkId8fgF12Ikgh_DIi6vZNpbF8xqiPPHkRK4qz0czytgI3_dUR1d-g1mipOgEq2o6i1JuagFUXENKvbQM-e5uc_ym01mEPO5st9KYfTSAe5CdcXg08mXXIHKEpZqw_4shhjQ4yvz88EUZP7gEIOD3tg8hpzV5bDG4-cJxFNFOeZFzh8RyUEJOwv-AWzd52moBDX5GlJcL2fE1mwA0UWntrajGJSv1YbkkoKi6VL1QHkX0D_XqpfgzKdc3Gcv5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeeb9329cb.mp4?token=X9WLICj5FcHob1StBh4yigCpsaAloMWrVSJH6rCWoCw0C7JjaQ3drf_kBShCWsVXQQabAsEp5qQhetP-2NcCD2ECLkId8fgF12Ikgh_DIi6vZNpbF8xqiPPHkRK4qz0czytgI3_dUR1d-g1mipOgEq2o6i1JuagFUXENKvbQM-e5uc_ym01mEPO5st9KYfTSAe5CdcXg08mXXIHKEpZqw_4shhjQ4yvz88EUZP7gEIOD3tg8hpzV5bDG4-cJxFNFOeZFzh8RyUEJOwv-AWzd52moBDX5GlJcL2fE1mwA0UWntrajGJSv1YbkkoKi6VL1QHkX0D_XqpfgzKdc3Gcv5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  أن نتنياهو روى قصة عن سباك إسرائيلي تولى قيادة طائرة تابعة لشركة فلاي دبي لإنقاذها من التحطم. ويضيف ترامب: "لا أعرف إن كانت القصة صحيحة، لكنها ما سمعته من بيبي".</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/92212" target="_blank">📅 00:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92211">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
ترامب
:  أن نتنياهو روى قصة عن سباك إسرائيلي تولى قيادة طائرة تابعة لشركة فلاي دبي لإنقاذها من التحطم. ويضيف ترامب: "لا أعرف إن كانت القصة صحيحة، لكنها ما سمعته من بيبي".</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/92211" target="_blank">📅 00:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92210">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47151339e0.mp4?token=ayWrnCkK97R9V_E6DeMaaaoVMFOCfyOYAkidq_Bakd5Zrqqgx79-_aRD5Ne_GL-SPIPeGjVMeG-sORxoK1JrL6NhKT_5wqENW_TyfH4vTNsiMQ52CmsBIYyevQOoHKwoGwkbMVGJuYwKu04L96fxyxeI9BUOvrqEGjCyg5liyhJJmTGCGxFxFwLfFae8MdekPSjLJlc8myySbsdyuqEMszv1mhgJpCGLPtylQQ164Fd9S1fXsn1IsqO6PVk9yyXKFAav_lU4iE0p5Jj2I1r9ikfz-Ox-mvbsSL5G_rtKtVJznQH3Y3cXprZysu3e2L8xLDUNzizHyjFNnb0wumtkzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47151339e0.mp4?token=ayWrnCkK97R9V_E6DeMaaaoVMFOCfyOYAkidq_Bakd5Zrqqgx79-_aRD5Ne_GL-SPIPeGjVMeG-sORxoK1JrL6NhKT_5wqENW_TyfH4vTNsiMQ52CmsBIYyevQOoHKwoGwkbMVGJuYwKu04L96fxyxeI9BUOvrqEGjCyg5liyhJJmTGCGxFxFwLfFae8MdekPSjLJlc8myySbsdyuqEMszv1mhgJpCGLPtylQQ164Fd9S1fXsn1IsqO6PVk9yyXKFAav_lU4iE0p5Jj2I1r9ikfz-Ox-mvbsSL5G_rtKtVJznQH3Y3cXprZysu3e2L8xLDUNzizHyjFNnb0wumtkzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
🇮🇷
ترامب حول إيران:
لقد خسرنا 18 شخصًا في مواجهة إيران. وإذا نظرتم إلى العراق، فقد خسرنا 4500 شخص.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/92210" target="_blank">📅 00:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92209">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/92209" target="_blank">📅 00:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92208">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/92208" target="_blank">📅 23:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92207">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نايا - NAYA
pinned «
ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/92207" target="_blank">📅 23:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92206">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/92206" target="_blank">📅 23:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92205">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇱
الاعلام العبري
: خطط الطيار للسيطرة على قمرة القيادة فوق الأردن وتحطيم الطائرة في الأراضي الإسرائيلية.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/92205" target="_blank">📅 23:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92204">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
وزير الحرب الأمريكي هيغسيث
يعلن عن إنشاء قيادة جديدة للحرب المستقلة.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/92204" target="_blank">📅 22:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92203">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
الاعلام الحربي لعشيرة الشغانبة يؤكد تحرير سفينة ثانية من قراصنة الصوماليين.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/92203" target="_blank">📅 22:50 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
