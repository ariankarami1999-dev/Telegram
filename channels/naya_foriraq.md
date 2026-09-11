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
<img src="https://cdn4.telesco.pe/file/L1wWB6kRB8LxsPNPvgswWKQVNorwrj6LNIs_dDMiGIG2dnmUSNHFj2gu2A-wMCgzY8M7A1Cs1uyQSFfiML8scUlTCakhdAjgW5d8qf0sVFrzElwYW5FaTeouzW1kzOW3x-G_rFqghye8J-iZIQ0CFK4xQN5GQ85RZ2Hi2UF53IiqlqsfhxZ37npqAtZgC06A9fwAlisq8UJ1rU5HuXytzdUFaeLcjKBnPJP3aBahXtKbcUTJ9_mkTgocH7QEe0T3Dds168KLIG5evINjPj0I7pVPtNYaCW3o3QcHufZ4WMGU4jGc_x3lr3yPWaET5JaHzi2-lLFLpKEY8Zc8sMD8mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 09:45:45</div>
<hr>

<div class="tg-post" id="msg-90152">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
🇸🇦
سي ان ان: الولايات المتحدة توسع أنشطتها الاستخباراتية، مستهدفة دعم الحملة السعودية، ارسلنا أكثر من 100 مستشار عسكري أمريكي في السعودية.</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/naya_foriraq/90152" target="_blank">📅 09:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90151">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇾🇪
مصدر يمني:
تم أسر 2000 جندي من مرتزقة السعودية، مع عتادهم العسكري في جزيرة زقر وحنيش وميون على يد القوات اليمنية البطلة.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/90151" target="_blank">📅 05:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90150">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e117b174.mp4?token=wASShXabUKNsejrzRQeN-bLDvRCTScgQOelKmpUrP_HqsNvETfMQgxBbz5-FIBrDMyhyJU0Lq-5_yaSGS-J8sDTD5_YHv89EyYA2Ac3VHt-T9JIEbWS-HDO_YknGpN5nd28-qYyaLAbgCLkoPyi016CglxiKNHTpQsWN67G6hK8hWMb8BfEIxa1-DnGYZTGjmiVRQxdIirzfH1NNRfKpddo2kX8u8-s5beD3DWHtkXdzoETshliudeNvZJEjO7yTc5dEUQbe5VlPfTzYHqchakxK83UM-BRamGFkB5pLML29JcwoPe3CVWnP98paEBc81l7ExP3fEXyipWw-aLcuzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e117b174.mp4?token=wASShXabUKNsejrzRQeN-bLDvRCTScgQOelKmpUrP_HqsNvETfMQgxBbz5-FIBrDMyhyJU0Lq-5_yaSGS-J8sDTD5_YHv89EyYA2Ac3VHt-T9JIEbWS-HDO_YknGpN5nd28-qYyaLAbgCLkoPyi016CglxiKNHTpQsWN67G6hK8hWMb8BfEIxa1-DnGYZTGjmiVRQxdIirzfH1NNRfKpddo2kX8u8-s5beD3DWHtkXdzoETshliudeNvZJEjO7yTc5dEUQbe5VlPfTzYHqchakxK83UM-BRamGFkB5pLML29JcwoPe3CVWnP98paEBc81l7ExP3fEXyipWw-aLcuzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
عقب تحريرها من مرتزقة السعودية..
القوات اليمنية تقوم بتأمين الأحياء والمحلات التجارية في مدينة المخا.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/90150" target="_blank">📅 05:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90149">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/510c41afc7.mp4?token=kcR7TW4s2F0u6nwfoFJd-7UzwaGdrYduP5jwIJkH7QOyYArVcXPEk4wIBi5QnXeSuBHGqKk8LNBismqQKHdiE_bTqV7xgF0waMQmwJkMnIY6qsXJ9qgEYi1wnlmkYE-O52mVsU6DKZ0A96IL1wHAQQEYlND-0ClmC86DR8cUHrRX791F9E4pjAvknNRJkUjIe5O2OItoBCqRWVlhQlwVPtP6XM6F5IRA1ej4m1M7-CxAet12nB_wggC8MBbAIShi88JJq9DRegMQk6E3ZnqZE42BICKFuFEEeXStvdwbH1R5YPst-Go1aELjqmMBbGo0SS_58kTUL6DkVd2ovOVcl2NrVSjFisNCoDLzpD5PzHSdI17XmS4i3IaafANlo8tzFSunBHj-G8-TZKdJ7kEnvJuqjhWzSZze-K0PCTiYSViOsLtt7EN3aiwDLWr5AxSAQtFPf2a7JvnqyOMG9bqi-AG_Nu0BcHjQYSM5Iknqho8rhxjKRG2um6nk5EsRLoHn95F6jcEpw0kQILrBk4aWCNvYi-9KGtdAFDWv3KWj3Nth_LnJwvEGxEgx4P73-1yahFPZMGizgi46s0Gw7JaZYzdNFlz5HUX-vA5812FBWRDps3gjAXf2-RGyJ8sTfgiMDfTyYfIWbRyeAvKUo4DKa4CU7lWuvcdOkPa3jtqZqes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/510c41afc7.mp4?token=kcR7TW4s2F0u6nwfoFJd-7UzwaGdrYduP5jwIJkH7QOyYArVcXPEk4wIBi5QnXeSuBHGqKk8LNBismqQKHdiE_bTqV7xgF0waMQmwJkMnIY6qsXJ9qgEYi1wnlmkYE-O52mVsU6DKZ0A96IL1wHAQQEYlND-0ClmC86DR8cUHrRX791F9E4pjAvknNRJkUjIe5O2OItoBCqRWVlhQlwVPtP6XM6F5IRA1ej4m1M7-CxAet12nB_wggC8MBbAIShi88JJq9DRegMQk6E3ZnqZE42BICKFuFEEeXStvdwbH1R5YPst-Go1aELjqmMBbGo0SS_58kTUL6DkVd2ovOVcl2NrVSjFisNCoDLzpD5PzHSdI17XmS4i3IaafANlo8tzFSunBHj-G8-TZKdJ7kEnvJuqjhWzSZze-K0PCTiYSViOsLtt7EN3aiwDLWr5AxSAQtFPf2a7JvnqyOMG9bqi-AG_Nu0BcHjQYSM5Iknqho8rhxjKRG2um6nk5EsRLoHn95F6jcEpw0kQILrBk4aWCNvYi-9KGtdAFDWv3KWj3Nth_LnJwvEGxEgx4P73-1yahFPZMGizgi46s0Gw7JaZYzdNFlz5HUX-vA5812FBWRDps3gjAXf2-RGyJ8sTfgiMDfTyYfIWbRyeAvKUo4DKa4CU7lWuvcdOkPa3jtqZqes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إنهيار مبنى قيد الإنشاء قرب جسر الصرافية بالعاصمة بغداد، وأنباء عن مصرع 8 عمال كحصيلة اولية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90149" target="_blank">📅 04:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇾🇪
غنائم من مرتزقة السعودية في أيدي أبطال القوات اليمنية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90148" target="_blank">📅 03:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3fbe7e70.mp4?token=c-OM1JV1kjzEOkYArrHzg_OWp-51p7-DB2j8_uszR4UgK9j_7gEcnyq8tWlJc9QWyXDokuoBgShaBcRcXrLmgPFvpZxIpC2aBrLR74piTKZAmW61411UvpHvOxktdH95RInu7uiSO3czWjVGIso22Eqf1qCoqM9pHdlfniIPbujeMNsutqNZ85vNqDNNuk057yrxWOMQJ-3SA34jbMtH3Po6G28X-cJ_Ti-ZZ4v1sQ6q93dos_QTvrywywpBQfq93_J0mZAI15enmFJlgAzFwbnC0dgQPjLhhJ-UqJfmdtxtT3OSQheY6tAVpk8QJY_opNfbd7d-YFGbhqu82G5CCi_a4Md3vqFO6RujVQVsPrY0quo5f_EcUz5ncZU4fBRRkeQU3SRCvo3YRzpCxt7VQ9NAIfg59j_ODPJDAUpxlw93ukcS_1_fjzRafAx54n6bqbUSiy9ZUT-v_q1T-TcCVb6-rn2mK4YHpFgVNRXRgrWdlEmilu9RoWXKJzUMTe1IclNfW9lghom7xBnb9iavUT6IR4N0X2NOrwlLET4E6ZnS5A0gQ1I8Q8unADliajyCOuxuGBe5o_VQV40xnoeaO-1dIqxmsEaNtAWYop6dthSBKFpYCwFXFaHwcYwH3KYiCtwvtCh_SzNZ0pJJM9sVpZDA5jIyPYf7CXHp0DeUmoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3fbe7e70.mp4?token=c-OM1JV1kjzEOkYArrHzg_OWp-51p7-DB2j8_uszR4UgK9j_7gEcnyq8tWlJc9QWyXDokuoBgShaBcRcXrLmgPFvpZxIpC2aBrLR74piTKZAmW61411UvpHvOxktdH95RInu7uiSO3czWjVGIso22Eqf1qCoqM9pHdlfniIPbujeMNsutqNZ85vNqDNNuk057yrxWOMQJ-3SA34jbMtH3Po6G28X-cJ_Ti-ZZ4v1sQ6q93dos_QTvrywywpBQfq93_J0mZAI15enmFJlgAzFwbnC0dgQPjLhhJ-UqJfmdtxtT3OSQheY6tAVpk8QJY_opNfbd7d-YFGbhqu82G5CCi_a4Md3vqFO6RujVQVsPrY0quo5f_EcUz5ncZU4fBRRkeQU3SRCvo3YRzpCxt7VQ9NAIfg59j_ODPJDAUpxlw93ukcS_1_fjzRafAx54n6bqbUSiy9ZUT-v_q1T-TcCVb6-rn2mK4YHpFgVNRXRgrWdlEmilu9RoWXKJzUMTe1IclNfW9lghom7xBnb9iavUT6IR4N0X2NOrwlLET4E6ZnS5A0gQ1I8Q8unADliajyCOuxuGBe5o_VQV40xnoeaO-1dIqxmsEaNtAWYop6dthSBKFpYCwFXFaHwcYwH3KYiCtwvtCh_SzNZ0pJJM9sVpZDA5jIyPYf7CXHp0DeUmoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد مذلة لمرتزقة السعودية حيث مرتزقة الإمارات تمنعهم من دخول عدن عقب هروبهم من المناطق التي سيطرت عليها القوات اليمنية البطلة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90147" target="_blank">📅 03:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90146">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇾🇪
🇸🇦
‏الأرتال العسكرية المتبقية من مرتزقة السعودية تهرب من راس العارة بعد دكهم برشقات صاروخية من قبل القوات اليمنية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90146" target="_blank">📅 03:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e27a0041.mp4?token=s39tC5zgq_766LoAvEthMVmGTVaXr1U3thcK9ILvyIzYYAMlQFI4uZibqul5416E7kYNd50S2hRnxweeksWLi7UtMLXi2NVJCjfEJQCkg4IdSG8lpDW33Ad_dyUrJ7a_hb4IBXOUFmu6WjhPt9ZDuf5koiAfn4gqqYqEeU__0Rmjuq4snGrSVI7MZAThmT_qCEt7bLXOHbjGJq7WZsOi5mEylMCD8w1gAoYFxaByboPMN2txoHHQHIKal74HMWYTWb3mjtxsMJdLJs_v9J6vxClaUbwxwJiRdQjf9RoHlG5nRyCgsBGXF8pQbPONAo0xysNNOS7ul-WD5nuVEkXsGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e27a0041.mp4?token=s39tC5zgq_766LoAvEthMVmGTVaXr1U3thcK9ILvyIzYYAMlQFI4uZibqul5416E7kYNd50S2hRnxweeksWLi7UtMLXi2NVJCjfEJQCkg4IdSG8lpDW33Ad_dyUrJ7a_hb4IBXOUFmu6WjhPt9ZDuf5koiAfn4gqqYqEeU__0Rmjuq4snGrSVI7MZAThmT_qCEt7bLXOHbjGJq7WZsOi5mEylMCD8w1gAoYFxaByboPMN2txoHHQHIKal74HMWYTWb3mjtxsMJdLJs_v9J6vxClaUbwxwJiRdQjf9RoHlG5nRyCgsBGXF8pQbPONAo0xysNNOS7ul-WD5nuVEkXsGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  ستنتهي حرب إيران مباشرة بعد الانتخابات النصفية الأمريكية.  الإيرانيون يواصلون القتال بصعوبة وهم في مأزق عميق.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90145" target="_blank">📅 03:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90144">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be127dc55.mp4?token=VZHG_SbZ6jpz4zqIX-SdGh_rvCTsx6JtVi7rqu2ZBPXUXTG4re678LQlypQlYyB_vs1pJvpubz6wpFHgtY1Po_Z7T5W7S-60UkSPLOyh0ky62x4SQTuycPUWRShvq3vYak0MPMf2Cpo4QBgvSTOARgOGqi2-5IjlRuium2ojePZe4Seo41zkZxMXGVoUtwgrQrCVLgJmjCfZh1-3aKCmMsX1BbhBdKtQl5VEtCyatnYWGhUN1xfsAL7Uc79b8HArbB8fu7gS_PwkvUeIrR1PLih2zEjt2cmXeE5h6jAyZnmrXz8FUJl5_w-JnIQKM-D-o9Wgz3NOikzXm7mldVTeI2OTTe6E9yuVgFFlMDU-9XKOEBVNWCdW7Wcw20VhTUsgPLjYzJ631je8os9l5H5euB8f-FIDMUib8pBFCRAuy_sGETDwW2n1tRncGQTZF0nfdTdVgRj1I-20auu9zlik-GakuuChP3vNK6ueXa_hhmzbvrIqhXqMrRNYhAGmA9HBzJTY4g1F9PCfZ7dPnFYERvQlP6zAfcvATMWNMmCLsSHmWTlbUM5tol8e95Vb6YbP0T1pGyrsp5jhbW9aYPVjAflZNX2yvIZWWWXSf6-xIJjjOQzc-Ehx9VznNRWMzahOW97erZyQkV_O1tusy0QGnaEisSWyQIIij1kma2yhTRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be127dc55.mp4?token=VZHG_SbZ6jpz4zqIX-SdGh_rvCTsx6JtVi7rqu2ZBPXUXTG4re678LQlypQlYyB_vs1pJvpubz6wpFHgtY1Po_Z7T5W7S-60UkSPLOyh0ky62x4SQTuycPUWRShvq3vYak0MPMf2Cpo4QBgvSTOARgOGqi2-5IjlRuium2ojePZe4Seo41zkZxMXGVoUtwgrQrCVLgJmjCfZh1-3aKCmMsX1BbhBdKtQl5VEtCyatnYWGhUN1xfsAL7Uc79b8HArbB8fu7gS_PwkvUeIrR1PLih2zEjt2cmXeE5h6jAyZnmrXz8FUJl5_w-JnIQKM-D-o9Wgz3NOikzXm7mldVTeI2OTTe6E9yuVgFFlMDU-9XKOEBVNWCdW7Wcw20VhTUsgPLjYzJ631je8os9l5H5euB8f-FIDMUib8pBFCRAuy_sGETDwW2n1tRncGQTZF0nfdTdVgRj1I-20auu9zlik-GakuuChP3vNK6ueXa_hhmzbvrIqhXqMrRNYhAGmA9HBzJTY4g1F9PCfZ7dPnFYERvQlP6zAfcvATMWNMmCLsSHmWTlbUM5tol8e95Vb6YbP0T1pGyrsp5jhbW9aYPVjAflZNX2yvIZWWWXSf6-xIJjjOQzc-Ehx9VznNRWMzahOW97erZyQkV_O1tusy0QGnaEisSWyQIIij1kma2yhTRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف صاروخي للقوات اليمنية على تحشدات مرتزقة السعودية في منطقة رأس العارة غربي محافظة لحج، يجبرهم على الهروب والإنسحاب.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90144" target="_blank">📅 03:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90143">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44ae578a02.mp4?token=CQajoxSpNd0FkWLvwdtWIyJF_7ehwGT68z39I2m8-O17wKDewO6iz7AfiMl6i8-JQPumsy--eG6CMKO8jmwf8GQ8J_maoN2mQ5qygGeLq4bgR0AGRbPvNLb2xOo8eTSsPOlKKCyK01X4PQmTDURCrhEbYoAqG7VrW5OTMBYquFYc53QagGNtIYGV6A1qvSyaM58qUizJHZYDzc-0V1QFpw1u7yW4ZF4rOzr97fRyu7CyxdNyYwbToIUBOn6v04_sewQImfOItmRXjDIlIkejhMvDuqxeqMFoIu9HD8CPREi_mwK1aOKuu0iOYvqehXYrcjaqmCHnYreTddWF6cwOSZf7jZK10PHNbxselXhDwqvaARMb1wRDm_M93VgNW50oDJ48lsOcvrjOVpSX3ltmxikRSUMa0INkD7hSr-B4o9gI10Cw5wzGO-6fB-kDpFVPqzXdXuJ-ATNIKf_jbhrt_vt9ERXEV7SSFBLjxkHOGyTVdWgbiRiyNBJKHD1Haev3gmeSHGDprzo5CVKwnl8v5zyzAT779bOA3hGHs6qoc5ZxfnQAjRLa2BLwOmqTp2AjgTefRlaM4hWDFIatb_1XE8gcP2JR7oh0FUgAL_Ol8zVVaFqYI7_a29HmrgCbqP4XyAVd5baFihdth7ZCJDxW51t24Dq74fCbdVIm7_p0QtU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44ae578a02.mp4?token=CQajoxSpNd0FkWLvwdtWIyJF_7ehwGT68z39I2m8-O17wKDewO6iz7AfiMl6i8-JQPumsy--eG6CMKO8jmwf8GQ8J_maoN2mQ5qygGeLq4bgR0AGRbPvNLb2xOo8eTSsPOlKKCyK01X4PQmTDURCrhEbYoAqG7VrW5OTMBYquFYc53QagGNtIYGV6A1qvSyaM58qUizJHZYDzc-0V1QFpw1u7yW4ZF4rOzr97fRyu7CyxdNyYwbToIUBOn6v04_sewQImfOItmRXjDIlIkejhMvDuqxeqMFoIu9HD8CPREi_mwK1aOKuu0iOYvqehXYrcjaqmCHnYreTddWF6cwOSZf7jZK10PHNbxselXhDwqvaARMb1wRDm_M93VgNW50oDJ48lsOcvrjOVpSX3ltmxikRSUMa0INkD7hSr-B4o9gI10Cw5wzGO-6fB-kDpFVPqzXdXuJ-ATNIKf_jbhrt_vt9ERXEV7SSFBLjxkHOGyTVdWgbiRiyNBJKHD1Haev3gmeSHGDprzo5CVKwnl8v5zyzAT779bOA3hGHs6qoc5ZxfnQAjRLa2BLwOmqTp2AjgTefRlaM4hWDFIatb_1XE8gcP2JR7oh0FUgAL_Ol8zVVaFqYI7_a29HmrgCbqP4XyAVd5baFihdth7ZCJDxW51t24Dq74fCbdVIm7_p0QtU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‏المراسلة: لو لم نتناول ملف إيران، لكنتم ستفوزون بسهولة في انتخابات التجديد النصفي. هل لديكم أي ندم؟
🇺🇸
‏ترامب: لا، أنا لا أؤمن بكلمة "الندم". يمكنك دائماً أن تشكك في نفسك قليلاً.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90143" target="_blank">📅 02:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702b942a90.mp4?token=cV0nHTCuqX2QchmJp90Z-DW_DAlxmCLAuZSedXp_XHEIr6CkXfOf12A5qytrN-u_yvOaeDODniTqQSMj0AiXp9wbAqWCEBibCtOf9AnkTTvuC-pg6RVE2wW4lcmxnF2Hxm7h0215IzFH0K5eB61l0lD-w0XxK6t-xDpjZK4BKhlAe8ksld1uDyALMjriu5CBrfuekX0OXs3hP2ILBQUN3inBafiG_QSkULUWXU5jKJGMxs8sOYHtbpky0aTQNVp5nvhVog3v73jycddncOk_hTl8qCKxcmPGWozdBSgVEUvT04o8XKwsO8cE0VnVPcPgjSGAwVeCsAkIe4C3ybriDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702b942a90.mp4?token=cV0nHTCuqX2QchmJp90Z-DW_DAlxmCLAuZSedXp_XHEIr6CkXfOf12A5qytrN-u_yvOaeDODniTqQSMj0AiXp9wbAqWCEBibCtOf9AnkTTvuC-pg6RVE2wW4lcmxnF2Hxm7h0215IzFH0K5eB61l0lD-w0XxK6t-xDpjZK4BKhlAe8ksld1uDyALMjriu5CBrfuekX0OXs3hP2ILBQUN3inBafiG_QSkULUWXU5jKJGMxs8sOYHtbpky0aTQNVp5nvhVog3v73jycddncOk_hTl8qCKxcmPGWozdBSgVEUvT04o8XKwsO8cE0VnVPcPgjSGAwVeCsAkIe4C3ybriDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‏المراسلة: كيف ستتمكن إيران من إطلاق الصواريخ إذا قمنا بتدميرها؟
🇺🇸
‏ترامب: بإمكانهم دائماً إطلاق الصواريخ. كان لديهم الكثير منها.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90142" target="_blank">📅 02:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc0c2b690f.mp4?token=iF5WR5worrGl4aSMjeCsdVK9mNh2Kn4rf61PxQ9f929jJ3xhxmRFuVaPpfiFXwJOzVNRNId-0xzHn88EfAm2CZia0JjV5AX3MHx8r37ZQewBQvKi8dtTQdG5Bep10SHhw3ATY2mdAMVkWcSm1HMIJVzwpWpUPIiRknFd1PYSaDi4nC5mJsCoVCxdSamuLpkIQ3MlhOwQFIqlqixnMsth7UdNd30BAGGrJnwT-BKtE0NQDihRY8BV2HWwgUrSVkGjGR-jEwrvwvTHZzpd_406JM3dWvai3Ni1YK_59kCWn9XZWUAlhkGr5-sQ1s7ddNJlwK0zDRhLhCTVx803Wv3C5mkUrRR9NcziCrZw6ztG82y_wqHRNlLXKzlojXMIuNw_JqxVvkhl90Y6jOhWoFhluHg-OTJ6-Uaj_VQ2ShHVoUy9rjImQdqGmFHL8KdiLIxjzZ1CxNp6NUj0oD-eByppeih9MIYmzkY6Bx8aS8pqfp11dwLE5X9NKXjqUppe_HZjJLKJvgpHgxJl3zvGGITce5vQDLTHK73mIx6sJ2b6BHyrj9BUFW9JK459SkYisEPej_v8QPeeaTN3wObH3BVxay6jqxUTTRi79Xhra4mpRqMVlLD4-zYMe6A2LIeLvbl2hLDNBs3pwaaMYo-bbRtUcUj9X_p3-47wJyeT9pdqrVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc0c2b690f.mp4?token=iF5WR5worrGl4aSMjeCsdVK9mNh2Kn4rf61PxQ9f929jJ3xhxmRFuVaPpfiFXwJOzVNRNId-0xzHn88EfAm2CZia0JjV5AX3MHx8r37ZQewBQvKi8dtTQdG5Bep10SHhw3ATY2mdAMVkWcSm1HMIJVzwpWpUPIiRknFd1PYSaDi4nC5mJsCoVCxdSamuLpkIQ3MlhOwQFIqlqixnMsth7UdNd30BAGGrJnwT-BKtE0NQDihRY8BV2HWwgUrSVkGjGR-jEwrvwvTHZzpd_406JM3dWvai3Ni1YK_59kCWn9XZWUAlhkGr5-sQ1s7ddNJlwK0zDRhLhCTVx803Wv3C5mkUrRR9NcziCrZw6ztG82y_wqHRNlLXKzlojXMIuNw_JqxVvkhl90Y6jOhWoFhluHg-OTJ6-Uaj_VQ2ShHVoUy9rjImQdqGmFHL8KdiLIxjzZ1CxNp6NUj0oD-eByppeih9MIYmzkY6Bx8aS8pqfp11dwLE5X9NKXjqUppe_HZjJLKJvgpHgxJl3zvGGITce5vQDLTHK73mIx6sJ2b6BHyrj9BUFW9JK459SkYisEPej_v8QPeeaTN3wObH3BVxay6jqxUTTRi79Xhra4mpRqMVlLD4-zYMe6A2LIeLvbl2hLDNBs3pwaaMYo-bbRtUcUj9X_p3-47wJyeT9pdqrVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: سنقوم بمعالجة الدين البالغ 40 تريليون دولار من خلال النمو الاقتصادي. نحن نحقق نموًا بوتيرة أسرع من أي وقت مضى.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90141" target="_blank">📅 02:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90140">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6fa3f0e.mp4?token=jFGBVTin1Q094EzoMtoJFfBzOkioKvaTz0dqFNk975rJcACsZGQcEPoIhadqk3WEyukDSAuVRuXw5k7rklN7ZmVF9Bs9puFsDVUEO1A5ly5mk9XU5DEvCXFt-B2BlyRYU3B6CRLijGa6pw-NnlowZMoFmTKw6k2x3RhrzeNPypZnfNIVUUtw3OOhWyIlX0c7zlGsXb767HKHRC9VjT-DGoSLm39yWwwCgjzQ9eRg8Im3rffqhc6zoD0vg-Zhhmed68LKGSB11Jnzn_TVyD_j9J8sxJZFLZJjix39uhdFGU68SBApNOc58TgI9wsVUVrBGlsmCWbdU6Gc9Al29gOiRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6fa3f0e.mp4?token=jFGBVTin1Q094EzoMtoJFfBzOkioKvaTz0dqFNk975rJcACsZGQcEPoIhadqk3WEyukDSAuVRuXw5k7rklN7ZmVF9Bs9puFsDVUEO1A5ly5mk9XU5DEvCXFt-B2BlyRYU3B6CRLijGa6pw-NnlowZMoFmTKw6k2x3RhrzeNPypZnfNIVUUtw3OOhWyIlX0c7zlGsXb767HKHRC9VjT-DGoSLm39yWwwCgjzQ9eRg8Im3rffqhc6zoD0vg-Zhhmed68LKGSB11Jnzn_TVyD_j9J8sxJZFLZJjix39uhdFGU68SBApNOc58TgI9wsVUVrBGlsmCWbdU6Gc9Al29gOiRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب:
سنقوم بمعالجة الدين البالغ 40 تريليون دولار من خلال النمو الاقتصادي. نحن نحقق نموًا بوتيرة أسرع من أي وقت مضى.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90140" target="_blank">📅 02:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7S9JXCLEVLGMdPvV9bZ7I2eX2U0m5s4czgr0Wt2yIOTm51ga-bkbvQ_iP_xzsDB97BJgUatcpX0sAd3s4-8Um0LxsJrX_tay95XwHCpgoC3MbFHq30IYJ8YSI9z-XiAbGqfVgY93MqgocvwSlyui_bNlPDTCKolm15eKc9yOBeM_KIwzFYQNYPjCjqbVo18vdum5f_giSW5RcC3nZcz15et81RAXGPCNaZvw-uLGwaV-3u0lSFb1kVvugbe4hR3m3cwoBwrMwSBezS3B4lNlZSetTfiuFhVofqBPazqqsmv7KfiG-E__0Ujc2bqjDTTrjUwFjMFPyqjxZyiVigUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
تؤكد الجمهورية الإسلامية الإيرانية موقفها المبدئي والثابت بشأن ضرورة احترام استقلال اليمن وسيادته الوطنية ووحدة أراضيه، وإنهاء الحصار غير الشرعي واللاإنساني المفروض على هذا البلد. ولا شك أن الأمن والاستقرار في غرب آسيا ومنطقة البحر الأحمر لن يتحققا دون احترام حقوق وكرامة الشعب اليمني العظيم.
لا يمكن فصل ما يحدث حالياً في اليمن عن تطورات عقدٍ مضى. فالشعب اليمني العظيم والنبيل، بوصفه ورثة حضارةٍ عريقةٍ ومشرقةٍ لطالما لعبت دوراً حاسماً ومشرّفاً في تاريخ المنطقة والعالم، له الحق في أن يعيش حياةً كريمةً، متحرراً من الضغوط والترهيب والحصار الوحشي، وأن تُحترم سيادته الوطنية وسلامة أراضيه احتراماً كاملاً.
تؤكد الجمهورية الإسلامية الإيرانية، مع تأكيدها على ضرورة الاهتمام بمصالح الأمة الإسلامية - خاصة في ظل الوضع الذي تواجه فيه منطقة غرب آسيا الشر والقمع والتوسع غير المسبوق للكيان الصهيوني بالتواطؤ مع الولايات المتحدة - على أن حل القضايا المتعلقة باليمن غير ممكن من خلال الحصار المستمر والعدوان العسكري.
تؤكد الجمهورية الإسلامية الإيرانية على ضرورة استئناف الحوار فوراً استناداً إلى خارطة الطريق المتفق عليها وتنفيذ بنودها، وهي مستعدة لأي نوع من الجهود في هذا الاتجاه.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90139" target="_blank">📅 02:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72affd6b7d.mp4?token=mobpZhlOd7dhoKBnLeSERwyY7UiSk8GKo_sLqMSY0HlSX3t1fL9gbXdwl3zrcw6Z-DCCe5gd8Bp7ld0Ms4O7uyii1leBgxAxVYYda61AsVPlmUS0Y1RyGanBTfQ3KgysgL1bXbtqwBK3BtJS9P2JdUN_ulc3QWbZF4a4RpzkRGVRbP0ikloFLiw-eOUmq4uOTIoVqLbWjA5pwqkSvIEf4tGZTPy-sJXZlO5nHH6d_nTBYUHs7p27LT-MWCq5a6s_pr8PiazoGZ0NNjcYGv4d8LMbVqRqrap89YCCWDeSMD9VdLksSLAgzGsAl1s1rAi_GTdm83f05GBZKiHKs5dYxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72affd6b7d.mp4?token=mobpZhlOd7dhoKBnLeSERwyY7UiSk8GKo_sLqMSY0HlSX3t1fL9gbXdwl3zrcw6Z-DCCe5gd8Bp7ld0Ms4O7uyii1leBgxAxVYYda61AsVPlmUS0Y1RyGanBTfQ3KgysgL1bXbtqwBK3BtJS9P2JdUN_ulc3QWbZF4a4RpzkRGVRbP0ikloFLiw-eOUmq4uOTIoVqLbWjA5pwqkSvIEf4tGZTPy-sJXZlO5nHH6d_nTBYUHs7p27LT-MWCq5a6s_pr8PiazoGZ0NNjcYGv4d8LMbVqRqrap89YCCWDeSMD9VdLksSLAgzGsAl1s1rAi_GTdm83f05GBZKiHKs5dYxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
محاولات هروب مستمرة لمرتزقة السعودية وسط منعهم من دخول محافظتي عدن ولحج من قبل مرتزقة الإمارات.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90138" target="_blank">📅 02:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90135">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa53b820d.mp4?token=aAERqeVMTawcXRdb5lscC9hcJLCApx63aAfhURelHYNj5IrIqjP99jKMSYL7ohcn_vuaG0DHjIw49pkuVs9cD3_1IFs9iMtkHn0q3AaNCUx3Rc26bEUi4KChBxewq1Mqp-jgf5KSudyopHyYtcSx8Utqsl50smGPfM2gfPPIUBuBWXADPJZZTtL02gwkN8LZzcDrCfLyktx5EFfazcQatd01EX7UQf7aQ2UvzwsQWV4znnLB5UDmz0DnGv-YJaq2W_I5X1YTZtpBpPCKckQOVHFiieY2GM5kdBhDO1bsq68EjCENNZRS6HlDeoUtugQOURUKRFstnS-pCiUg1dzOtkUUKMsBD3iQ-pV2LaMdSRAPSWrn9DAnMtqHyshgTzMf4Va7x-FNx_mLSmEdf6edOhM1cvC_hGrd4muPFofLz29sjy52NDYWErDTlgnJp4DcF3Iv6AfCpDUXWDaOsw7sOoQmPYJpf7GwCL1JFNzAhL5YphKfxQspsulBA7gzJ8lIt2tNUDzY4EYJyyBdaJt5jyhn-9fATt1Z_E-Ur4sjX77TAdSnSF6aQQtGTFrZNzW3uM95X4PbzfC32IPsdcvGu9WX6pXOx6nPUtjzu7mAPdw3yW0fR9UxoQRsO1wVyRXI3lC7fbUvA7LnZSUARDLAV40WulynInJmYL96tpzsEPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa53b820d.mp4?token=aAERqeVMTawcXRdb5lscC9hcJLCApx63aAfhURelHYNj5IrIqjP99jKMSYL7ohcn_vuaG0DHjIw49pkuVs9cD3_1IFs9iMtkHn0q3AaNCUx3Rc26bEUi4KChBxewq1Mqp-jgf5KSudyopHyYtcSx8Utqsl50smGPfM2gfPPIUBuBWXADPJZZTtL02gwkN8LZzcDrCfLyktx5EFfazcQatd01EX7UQf7aQ2UvzwsQWV4znnLB5UDmz0DnGv-YJaq2W_I5X1YTZtpBpPCKckQOVHFiieY2GM5kdBhDO1bsq68EjCENNZRS6HlDeoUtugQOURUKRFstnS-pCiUg1dzOtkUUKMsBD3iQ-pV2LaMdSRAPSWrn9DAnMtqHyshgTzMf4Va7x-FNx_mLSmEdf6edOhM1cvC_hGrd4muPFofLz29sjy52NDYWErDTlgnJp4DcF3Iv6AfCpDUXWDaOsw7sOoQmPYJpf7GwCL1JFNzAhL5YphKfxQspsulBA7gzJ8lIt2tNUDzY4EYJyyBdaJt5jyhn-9fATt1Z_E-Ur4sjX77TAdSnSF6aQQtGTFrZNzW3uM95X4PbzfC32IPsdcvGu9WX6pXOx6nPUtjzu7mAPdw3yW0fR9UxoQRsO1wVyRXI3lC7fbUvA7LnZSUARDLAV40WulynInJmYL96tpzsEPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مظلوم عبدي يعلن حل تنظيم قوات سوريا الديمقراطية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90135" target="_blank">📅 02:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90134">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9198c05ccf.mp4?token=uC1s1iQuynqmhw4fY0UUkIBBxqv9kLvw9i0W2cXG56UWJHpRjiwBatwKpZS156Um4vw59HJSN_LwwQ0AsFX3x6oqLWiOYvDnVRtmVmDeIDfdMdydMX8gO5tL-Wyeyb64AEz4PgpkW-NECYR5bhYIzCyK5pxnruAK1gWuB9Uek0iXEELq_gWdAxM-1WPKzuKlaASF8E--B-naAFBBATOaLjFnwbBPjDPZFGTy724pkxk7PKPL49pj5lU1GFC7nodAWrBs4YwXWuoSeklsu6A-zMymFTKVUQJHf0R7YFNi66yt6MIz2LJPxTjm6T--uC4_SDGHBmJhUVFhZ5MiwXvm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9198c05ccf.mp4?token=uC1s1iQuynqmhw4fY0UUkIBBxqv9kLvw9i0W2cXG56UWJHpRjiwBatwKpZS156Um4vw59HJSN_LwwQ0AsFX3x6oqLWiOYvDnVRtmVmDeIDfdMdydMX8gO5tL-Wyeyb64AEz4PgpkW-NECYR5bhYIzCyK5pxnruAK1gWuB9Uek0iXEELq_gWdAxM-1WPKzuKlaASF8E--B-naAFBBATOaLjFnwbBPjDPZFGTy724pkxk7PKPL49pj5lU1GFC7nodAWrBs4YwXWuoSeklsu6A-zMymFTKVUQJHf0R7YFNi66yt6MIz2LJPxTjm6T--uC4_SDGHBmJhUVFhZ5MiwXvm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
محاولات هروب مستمرة لمرتزقة السعودية وسط منعهم من دخول محافظتي عدن ولحج من قبل مرتزقة الإمارات.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90134" target="_blank">📅 01:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90133">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gteO9ZACQU0XSoMAUTGdcryoz8UW_T3LGBPisVFIUr5j6ViB15VaQg9s48OFtu6aKRWxQx_w_wgvFuUPJruQ0h61eGD481Hc0vmcDwLlogha6LKQzsoRhVF6JA2s_F0aFa8RCbQ_Cnd2Jg4i7O1T8Ehb2NxUX-tuRecsE3y8ObSiLklHN6y5kvDDOWRpWI0HzsfNFRO8x5bvhX0juzhiS4MhsmmqKUA8_VFz7F8dlBtxplVLMeMcRpIcLKXSgzjlCulsiegigc7WOFUcYMK0bKQgotfpXJmfLRdR2ah2bliWwrkzOTpxL6-2XBVE2SKz3qPQ0r_cjaTfmBt5bSp1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
النفط يلامس 110 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90133" target="_blank">📅 01:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90132">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇾🇪
الجيش اليمني يطلق عدة صواريخ نحو مواقع مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90132" target="_blank">📅 01:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90131">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇱
اختفاء جندي من جيش الاحتلال الإسرائيلي على أحد شواطئ مدينة حيفا.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90131" target="_blank">📅 01:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90130">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇾🇪
🇸🇦
عدة غارات ينفذها طيران العدو سعودي في المخا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90130" target="_blank">📅 00:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5DlEEKpaGm11Xv7vjWS1AyOBPRJ5z9r8qA3SEadh5AxrJJ-3IqnTRlVRIKA7RkrrShvNW4-5D6jkDC_Kg_7YULwT-ivlIZZk4mFQkxvdWOr8HTwVlceHEy89TKGcZHrnn4QT-LLVD8Nu0tHnTSGb5f7OfYEbt7KAkaXSl54PI3YlpHFMWQGAkqt6q_Jtqht-2yQp4AY4rUZnY1UiZBjMSFVj_XJgPscWZHef1SISrn6i84HQE2BK68gZiDpt2zeGC79yY_KNwzVcR6oHJxCTMA5ey7cbB8BYrqelcg90XrFuf-sUBHMTm4E-KYOnEjaZDwvi0YOAC1GS1PIcuZIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف السفينة الثانية في مضيق هرمز واندلاع حرائق واسعة فيها.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90129" target="_blank">📅 00:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90128">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnkdgQtqLqOlpt0MSoViwgJNVMSo15iuvf1VwhjRTdEOwoqNVJ8f29mEDimI30UqhOFcwrPzicIwYc7dD270ZE9PU0GohBpTLGmR8SRUY79qagDZS8ZVXh3U3Y0eteINxxTIP2pKhZPd6BH-Wo-pGhkD3RipppT5CEAXyWXLH51EvKRl0bSo1WjgR1UgjioffRuqxCaGz2n8Zuww8-aSIS84MzYlu9t0SNP3ygSICCkRF1yFCVjA2uUqLOsKiS73YIBvIlfX3dK-kN-ix_WtUCa-pgHLD2Iqvvyt84BJl6EsjPeoX11jlMhDtRWYzRkj9c0bDeNCJ6p6Q-C_HpVU-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تجاوز متوسط ​​سعر الديزل الوطني في الولايات المتحدة 6 دولارات للجالون لأول مرة</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90128" target="_blank">📅 23:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90127">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله اكبر استهداف سفينة قرب بحر عمان</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90127" target="_blank">📅 23:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90126">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الله اكبر
استهداف سفينة قرب بحر عمان</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90126" target="_blank">📅 23:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90125">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTVgqHptcjorYUkko3YGiN1x5pp18ZfGDFvjX2cGSN_cPHMyUmOGfbR74CWZ32ELJuxHx12ybIHRvoj4vcVNipgzKVaovW8iT37e-DxHAzs-lggaDd0ATgth7zxILwaNkrrAHnNMZkQ0lUgYuUFwmMgQdc4StCL_sjvl2W37dYu7J9GB17PzqS8i_XZSk8ZZbHuSXYPSo_4WMuohqSHZ29MmknZ2agAJbj2ta3DHTqIvETGM37uBLjGz4PuUpXrjZGBJCW8s3kzrRE5ZfVDvVe7yQGMruMbbyFRus1LPn9o10HGrcr4dOTOPnQjVlLgm6teVCMSETZdgRgLQTCaKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
قليلة التداول و تنشر لاول مرة " الشهيد الحي ابو الاء الولائي " زعيم كتائب سيد الشهداء العراقية من سجون الطاغية والاحتلال ؛ بتاريخ مشرف مقاوم مملوءة بالآباء الكريم والعزة النبيلة بوجه الظلم والذل</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/90125" target="_blank">📅 23:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90124">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
🇸🇦
إعلام أمريكي: امريكا ترسل ١٠٠ مستشار عسكري للسعودية على الفور</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/90124" target="_blank">📅 23:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90123">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89269525c5.mp4?token=FgHuXfRQshsjtcxMm9o0T7E71O0-j0pkKzKYpn-VM493QeR93M4AZ_EGc-IhqYXHkhOHETio_G_5Y3t0OonWaqvttXijio-19BDbXfbWtTJI4Uqh_BnJag3ReQf7V8L2wVpQsMXyopolSR0EdHUsPlGykULT3K4lo1eB87gw0O3JYEmz_eHAOhWBL4tr5n8v4Kj6KSb1IcxAKb644RExdn6ZB-RDMrbuyCxfYEdQYgeCqKxkuIhBsJe6B7rlVbrv6rqyDUFEd2X05x0m3Dx7zxdpVHikM-Cbvqaq0L8PwVAqjNqHaD1UHXq9nNIcpiU-op-RjXtS0UzMUOdAbXb9sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89269525c5.mp4?token=FgHuXfRQshsjtcxMm9o0T7E71O0-j0pkKzKYpn-VM493QeR93M4AZ_EGc-IhqYXHkhOHETio_G_5Y3t0OonWaqvttXijio-19BDbXfbWtTJI4Uqh_BnJag3ReQf7V8L2wVpQsMXyopolSR0EdHUsPlGykULT3K4lo1eB87gw0O3JYEmz_eHAOhWBL4tr5n8v4Kj6KSb1IcxAKb644RExdn6ZB-RDMrbuyCxfYEdQYgeCqKxkuIhBsJe6B7rlVbrv6rqyDUFEd2X05x0m3Dx7zxdpVHikM-Cbvqaq0L8PwVAqjNqHaD1UHXq9nNIcpiU-op-RjXtS0UzMUOdAbXb9sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تفعيل الدفاعات الجوية في ارومية بمحافظة اذربيجان الغربية بالجمهورية الاسلامية.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/90123" target="_blank">📅 23:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90122">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
🇺🇸
وزارة الخزانة الأمريكية تعلن عن عقوبات جديدة ضد مسؤولون تنفيذيون في شركات عراقية.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/90122" target="_blank">📅 22:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90121">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf39a528ac.mp4?token=dIkT5DWGrCV-3256H_StXvLdXyECTLpa6EXqRR_DdrQtV9wSrFbevYOMn5sIsqLqyMc_faUkK3kLij3FCQWF_2exd0ebrEqkRXEmBB58dLYOUJ1D9oIpNi0uO9w3Da3oyZ69JvYzZs40UFuHzkLHt70uga7wC4cgsu1ZbqlZxXWQ6KWtm9hXuo_th61Xo0LFTW97eJYqfvdqa3yl6zlQRFnSlGO_Wk7oE1cysfj0brav5-VMyfERsc3yKJk8qjCnrqXLMut2EOW2hk1vCzKRjzEY-4PN34VN8oHF81vPnw3lAKS_-NB5ja0KCmqOwUXmW0mYv1rSKtl4E5EkAurfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf39a528ac.mp4?token=dIkT5DWGrCV-3256H_StXvLdXyECTLpa6EXqRR_DdrQtV9wSrFbevYOMn5sIsqLqyMc_faUkK3kLij3FCQWF_2exd0ebrEqkRXEmBB58dLYOUJ1D9oIpNi0uO9w3Da3oyZ69JvYzZs40UFuHzkLHt70uga7wC4cgsu1ZbqlZxXWQ6KWtm9hXuo_th61Xo0LFTW97eJYqfvdqa3yl6zlQRFnSlGO_Wk7oE1cysfj0brav5-VMyfERsc3yKJk8qjCnrqXLMut2EOW2hk1vCzKRjzEY-4PN34VN8oHF81vPnw3lAKS_-NB5ja0KCmqOwUXmW0mYv1rSKtl4E5EkAurfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اكثر من ثلاث انفجارات تطال ابها في السعودية</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/90121" target="_blank">📅 22:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90120">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2YR4MCPNRl-yFRM3C780brJr_bR1WBXoreJ7w8p9P0c-JRP6hN4ymFqJ5G3qJRE7Ha2snqPNVdGuUc3SrtbHZoY78C82s5OCHO0yjxxdwuuLKy3QV52PLWqT-5Q1eq_snKpCMcpfxuxicoN1QoUFpC9v2rvawqCuldSP6TNr4dzXSCB89UwDfcr1L4BQv1qstNTSaiQMIQj3MDErTZ0QSwIH_c20GQpYbaW5CiiANxak3g4GMNlVXLTRabbA5FcvidvePprtsErc1q252Taz6GwhQn20o7QBEi9ysY6eTQsJzM77sFrfS7K4jFKx_HrCaHRSgxk2_EgS7hkHK5yaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران اسعاف فوري سعودي ينطلق من الرياض باتجاه أبها لنقل جرحى مرتزقة العدوان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90120" target="_blank">📅 22:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90119">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رشقة اخرى نحو أبها</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90119" target="_blank">📅 22:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90118">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رشقة اخرى نحو أبها</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90118" target="_blank">📅 22:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90117">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/90117" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90117" target="_blank">📅 22:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90116">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رشقة اخرى نحو أبها</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90116" target="_blank">📅 22:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90115">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90115" target="_blank">📅 22:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90114">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رشقة من أنصار الله نحو خميس مشيط</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90114" target="_blank">📅 22:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90113">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90113" target="_blank">📅 22:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90111">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انتحار جندي إسرائيلي</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90111" target="_blank">📅 22:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90110">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
🇸🇦
سي ان ان: الولايات المتحدة توسع أنشطتها الاستخباراتية، مستهدفة دعم الحملة السعودية، ارسلنا أكثر من 100 مستشار عسكري أمريكي في السعودية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90110" target="_blank">📅 22:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90109">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
🇸🇦
سي ان ان:
الولايات المتحدة توسع أنشطتها الاستخباراتية، مستهدفة دعم الحملة السعودية، ارسلنا أكثر من 100 مستشار عسكري أمريكي في السعودية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90109" target="_blank">📅 22:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90108">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccmkeKVIyVVSTx_gCsMek_ONXuyShjXFIHVvNIlbZWTvCRZaZZSQoV6IX8elLG5YrtSjAgeWVSOIDmBmkoohmn9dEgl2Nf8shsFp3UaMqnH0OIcqXZg5WQPplSJLtfAqcZP_EWvctrFdEUEfE5EXgG5u6vi2shn77ZGcjrV8hVsyIiSoezt9MqaPxmjAYtBRTGAa8U20kVPXKnyhNYgaOJ-fuUI1R4yznhi06POXcA85UUZXoY5XY1CeKkIOi-ppNo9xHItrk_meIAybkSmj_1VoKDLZHi-ABr07a17ZLJ4BIZ0ffw4b1KEFLMLt6P2sXKPnwa0iAIZmSi9jXz3i1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط تصل الى 107$ للبرميل الواحد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90108" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90107">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇱
اعلام العدو يزعم ان صوت الانفجارات المسموعة ناتجة عن تفجيرات ضخمة لانفاق وذخائر.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90107" target="_blank">📅 22:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90106">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">القوات المسلحة اليمنية في ميناء المخا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90106" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90105">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
🇺🇸
وزارة الخزانة الأمريكية
تعلن عن عقوبات جديدة ضد مسؤولون تنفيذيون في شركات عراقية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90105" target="_blank">📅 22:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90104">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
‏
مسؤول أمريكي:
بلغ متوسط ​​كمية النفط الإيراني أو المشتبه بانتمائه لإيران في المياه 110 ملايين برميل خلال الأسبوع الماضي، مقابل 180 مليون برميل قبل الحرب.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90104" target="_blank">📅 22:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90103">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c2af1239.mp4?token=On6djgpl9UTKHTrV8fh-9Fh-Gr6nghISTr__rY8HtJvtcf8ogprdHxbnOyaCdfyqM9k7wJETsh0UJjwhO0HVJy1nwmrgZtkGL34_E8E3eyrttNqU13tXsEeX3LE3-sYBpsoLglV6ESQ0xaWHcc8z-FcwPyARPdwXGpENpsF7B7b1URWHm1dz7txwagMNECxqfLyHrsNjAlI9z2Xigzb2Rq_lgt7Ov76NShRjzg2xuvs1HEoh6IXX8MyemvMtWsPJe1hofZnM-dlhTsai9Tf8k1rqD6Blv9i2L57x4ACOuYhT3TGtmW1V5WFgf04HT-S11gRlsnLk8agArNPETOUQkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c2af1239.mp4?token=On6djgpl9UTKHTrV8fh-9Fh-Gr6nghISTr__rY8HtJvtcf8ogprdHxbnOyaCdfyqM9k7wJETsh0UJjwhO0HVJy1nwmrgZtkGL34_E8E3eyrttNqU13tXsEeX3LE3-sYBpsoLglV6ESQ0xaWHcc8z-FcwPyARPdwXGpENpsF7B7b1URWHm1dz7txwagMNECxqfLyHrsNjAlI9z2Xigzb2Rq_lgt7Ov76NShRjzg2xuvs1HEoh6IXX8MyemvMtWsPJe1hofZnM-dlhTsai9Tf8k1rqD6Blv9i2L57x4ACOuYhT3TGtmW1V5WFgf04HT-S11gRlsnLk8agArNPETOUQkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
انفجارات قوية في جنوب لبنان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90103" target="_blank">📅 21:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90102">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e0c86462.mp4?token=pAGzv5OecZJ86lW-8sSqVwuT8C-Fhic4_xGIs9pDQBog8cgFQwF8U8HHZPVKa_UcgqpFSiEy_s3dJwOPqJ6Rb-CG8xlqXGafL4XYTLq9wJWImCbAIchOzDqZW3VoJgTlNwylukMHonQIOhGmxiNUOpwxjRhVjEHSzpruqiAh-7UrjRyiXyXasNJLf3ufKagOdAbaAL5fEOXVHt4tGV5LQ7IxpXCx9V0UosZBg8-8_bEWtZQnhcn-Qe-4ACO053hkMblreaiWbcJrd1hHsChKMtkD-ROx-yJWvQhyK1StBk-GTtnfk0Y3STdB2gUL3Qzv8-7SCKQE6SwkzZnM3mWY2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e0c86462.mp4?token=pAGzv5OecZJ86lW-8sSqVwuT8C-Fhic4_xGIs9pDQBog8cgFQwF8U8HHZPVKa_UcgqpFSiEy_s3dJwOPqJ6Rb-CG8xlqXGafL4XYTLq9wJWImCbAIchOzDqZW3VoJgTlNwylukMHonQIOhGmxiNUOpwxjRhVjEHSzpruqiAh-7UrjRyiXyXasNJLf3ufKagOdAbaAL5fEOXVHt4tGV5LQ7IxpXCx9V0UosZBg8-8_bEWtZQnhcn-Qe-4ACO053hkMblreaiWbcJrd1hHsChKMtkD-ROx-yJWvQhyK1StBk-GTtnfk0Y3STdB2gUL3Qzv8-7SCKQE6SwkzZnM3mWY2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
انفجارات قوية في جنوب لبنان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90102" target="_blank">📅 21:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90101">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏
🇺🇸
رصد نايا   غادرت اليوم عدة طائرات تابعة لقيادة العمليات الخاصة الأمريكية قاعدة ميلدنهال الجوية الملكية البريطانية، متجهةً على الأرجح نحو القيادة المركزية الأمريكية، مع العلم أنه لم يتم التأكد بعد من كونها وجهتها النهائية. وتشير بعض خطط الرحلات إلى توقفات…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90101" target="_blank">📅 21:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90100">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">▫️
‏قررت الجزائر إغلاق مجالها الجوي أمام جميع طائرات الإمارات طائرة مدنية وعسكرية مسجلة اعتبارًا من 11 سبتمبر.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90100" target="_blank">📅 21:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90099">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922f30bb9b.mp4?token=cABpnLSFVmSLeQZmwKT447vNvXQzGUyhAJ79B1_cDAfUfxyN-Z8te3b_kgsEcAJIpMbpeO_pZrVy5rdo0UKwd2dOoeNr4fBw73zs28-E8Cc4rIeeMURoDoDdltA0A6CTGYBHgVqS3GrjNNQfmAOFdWAp5Z3r8aHyPEhG1vaqrwYX-zHQy0X-MfA_XE1o-Vubfy7iCoiA9FZHALr6GLh3YwraX9duHhNqxyNC_zp4ogY_KU7vY3MI0YHtDWtGmOoCZmTKKeNtCgv4ykBOk4Ii4zKYLhs-BXx50BRh941zwMJh5iSls0Q1ksqGrDZekRPRBxDyYQ2bRKAsI-AXq1hQOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922f30bb9b.mp4?token=cABpnLSFVmSLeQZmwKT447vNvXQzGUyhAJ79B1_cDAfUfxyN-Z8te3b_kgsEcAJIpMbpeO_pZrVy5rdo0UKwd2dOoeNr4fBw73zs28-E8Cc4rIeeMURoDoDdltA0A6CTGYBHgVqS3GrjNNQfmAOFdWAp5Z3r8aHyPEhG1vaqrwYX-zHQy0X-MfA_XE1o-Vubfy7iCoiA9FZHALr6GLh3YwraX9duHhNqxyNC_zp4ogY_KU7vY3MI0YHtDWtGmOoCZmTKKeNtCgv4ykBOk4Ii4zKYLhs-BXx50BRh941zwMJh5iSls0Q1ksqGrDZekRPRBxDyYQ2bRKAsI-AXq1hQOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏
نتنياهو
: دمّرنا قدرة إيران الفورية على إنتاج قنابل نووية مرتين وهي تحاول مرة أخرى</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90099" target="_blank">📅 21:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90098">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇾🇪
مشاهد حطام طائرة الاستطلاع المسلح "كاريال" التابعة للعدو السعودي والتي استقطتها الدفاعات الجوية لحظة قيامها بأعمال عدائية في أجواء محافظة حجة - 10 سبتمبر 2026م</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90098" target="_blank">📅 21:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90089">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8PcnSeumYGdV8PyvjGFy9HjREMMaMg9p0wpo0I9-FxC8jK1mfhr8phsUlLDoOyoytzh0Gc596OI7iOs6FAhVgscnkz6gev1BFuVeLSJM1FMDmLk7rIrB54hnLbCnzgMG-x5YU_1vnkS2U-2VkkVe0rWpMYoL0p5NlaeXOCbmmWOVPWy1bJ8dT6A96ta8NRsiux2Kg4dRnevRfuBAixHdhFiwCZvkII9pX6h96UAE7ZSmd56kGrz6G3T-DLFbFd6L49XkekeAo-XCPcchE4u5UmSmtogkrxML-AaPqm8eqPZORJRCX2BA0R8UF9pDAED6vodeLOK3i8k2z_mzbjI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6Rb_NUFNYuRvUDrMkA0IMF7wThMS3Cb7uH1OBvIVot9xiNkBCCtOsbFxXZBOJb8m-ukn5ViTl3qdALQXKAkA8nT6fGB14CR98XmARRy88C01X0McduoXQznZzT3CCo4jBNRlfxr-ganIv5MNqNsu1a4thEqPOSarvxVYKC-1PO3RG15LmzRvR7CDi3bIiiWFef1aPuFIGqFrnbBhf4lAiz6t-Xp8nnhlDB2cEiFT4Ru1_3othb1bozeir03KfVZ7ydQ9C6nKykXzfclrUbDIBjCbASxu_61aE8YzrRtmnKDo9vinWTuhmoOxlyMi28W5yEQ2JnrHcCQXkNnx8pkTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5oELaXHL5uHPfeTpYpjf_yXtwQnI0lbvvJN5kuJmgzIBraFlT1H9j2TCmiZ36grXDDMGqVKfVBUBw0wOgsyL1lTNtArbdEO57x1CNX4kW5_g6evTSv-2FCo3SfUtO6-Ip37J-xt9Wj5GcopXpJteIrpVAt86gKZqUgBsM7MloFxNScTGdiF0aVqlvaTZb3tXSyZgtlhZJrBGc8X6NU4DHiaPGGjRQYHH-vViOeMdo9ScRmzWA3LN8vfDhds4tX-SLArbBcCc4hOm09EyZ3Wqc6G9KDR0tDNG6I8tTVhk_cUV-rDhQkUBPkZA-CEHRUlr6aX5sZsJ43lUZklThFCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHLCOYShDi93ClSs4gEZO0vLbIgVy2r1GNmafRRGl3KFn9iRXNYdigLVFqZ3DUC_xPj5e7cMv0BBjLMg7b8R3urDuuAprkC_kMsxpnhuWgLmNGu_KC3P3T8Lx0P6E9PbjM2I7z3NL4kJ3YMjPHtFX8BueDQTjOI4fXdVus8Rcf1y3figbSTEzjJpnfwYoiVyW4hctGFWIPh3KA-9KXmJf0FSS_VdSBf4l8K_sfz48jWE7ME5h5-fZvJZIwvuT-ofbiVL6QHxB7ECh_L4iEKYJ3A0QS5STZdFDbJcD1doXNM4Fp3_9CGaR_5ZSUa8MPm-E1N3Qyp408GVlaT3ARPqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNjeA1S9sP9MunGAB1XHCjsYmkOhFWI_u82f4mG-8NRFt8yOGELkhQL10MGK9peGI5DRCFGjXgN_HxlMuWTFnjw7CZg-6rAH5zLIw3SLLxDLTqUWslxPDseGYy99RHUcaScPwfrrvaDFUXuSSBI8jUL4yf_7k7Qkhasn6lYsyItlvy0Gtm2y_eySHa8vJPm0wWp0nypamcR7kqagkT9EsdVAXGd_st0P4FdwnrPWtrjd3IssiKX1lD2D44KRhdakOsrIIHVLZH5WRFgueOu2vYhB2PqvL36w8kJDw4KgPY0Na0Vq-TcdV7t-aeCUGHwknRMvIxcknRYeIhVben6Q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcTw_3makJaMK5S1oMa7YJNB1P9N1EVOatu4HoKavkUp6aSPayjfLVS4-z0PIDBA3zraX9ww9t-xVstxZZqMD_ne_L_y0GUoNBVoy_YkS9XnQbieuzOKXrgsLerC_82NtYjHykkhPCBjoJy5z5xg4EtOBeCqSjuxlIYUB_UOyT6ED5w8SXuO1Wc5Z14gw-FetpHO2IgRztLD6ZeK0FJqA43UUabewsxlhJAJ83iqK0bysvNEfP4fj7--6UDGeUeV8tYe5JxzUS7PVaINU44PKZl3yMHObWlAYmgAClMyxs7sYfvxxJMAmgB6qqAKYxsspB4nwuMamXzz8c8NAQkPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAYbZbF3SkCW5daVWt9OtE9zcwKo4vURofUlI9RllPhYFoXBzFhoZKvkPXN5HaAC0R3yv2H4nSGOxj2ofMb8TV9xeKbfw7oiMuNagv515sBoxzAzDEG6ZLKS_64iWvB2IJsXkqIqeILY1L1176tpIkSEgHRSAuQv6UfYnJvpqlvcbTtQuZdpe-7Pjv-LoemsPOxSt3bJ5iLXcx_u1eUovdfnheLF0o7qJEZf_ZqRbqfwS-yRrRk-S2ohYWGGMUVxZXw8gBQzWSTcKo8pso3gmGBATeFx_7FWbpKgdhCF8FAJddyKP95nS1SUZIIqKpfWkOvNufQoDI5ZnSvB33hkkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IkiZ-NLzTw0uhkI5vY-kBF3OsK_kQHHMH4WmFOJqOrO023ZNRoXs62wfDZtkgnqM1EIZkq0-A4wYYP_o5M8yM8FahmxTuqPhV_j5MhFlKT-i6S1ZjvgVlP_C1Fm_IfI4cM0lAxWMq5f7oGR3efaJq8xYW79W72rxN8d-XLFNuC-v7Q2M7bUPOvHcAdtib6hJJyCPNAyhIyn-rTGbH8N8PchLlRpGssnypnigXJw_s_KQps8jw9-Y29EHw0im2Yeydrp73C1jdPL40EnQJhrnmbjO_ATazMzCQuktahP7x_HE2QZzkjCV-8dzqivaq6Y5wZGM_3hNIo0xxwHIkxIZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDyWrNcbqajR8DOdU9npD4SE0iqWwsb7o-FwnduF-EOf021aUqtXW9Nj_aGjmRbPg84FrSHrozwfZkR6PDN4XYXdHjz9pHyVIx1CTf1mJDrqOItBeD4MyQar2n6-50mzySc9wp7nh9kitJGJ9mGOnBlp5FKOV4qL2JBkVWGURWbcOxZFU9UY_aPf82zknU4gathCyTW69IbP1RLxqhFM3KN0r89TcQ1CpU5AD-q7eojfVB74a9KVeEO2c6ZtUh5RxUbJiW64M-ED_TMEDVvDszUaJYc3OEYpHosbBgyyEk8EmIGo7FTNJgEZdsrugfSBp4hlkEtM3-YzEHepH8gBuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
صور من مشاهد حطام طائرة الاستطلاع المسلح "كاريال" التابعة للعدو السعودي والتي استقطتها الدفاعات الجوية لحظة قيامها بأعمال عدائية في أجواء محافظة حجة</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90089" target="_blank">📅 20:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90088">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
‏
ترمب
:  لم تتضرر أي طائرة عسكرية أميركية في الضربة الإيرانية على القاعدة الجوية في الأردن.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90088" target="_blank">📅 20:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90087">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5aee63c24.mp4?token=vBXMmJf-4PM3_khYzn7QX5YvrEox3Ff1AZjrpQu0DYCI98dtmmH7hzIbArkCG_nTt5z5CZQleRUodvBsq83mzlFlCclOJe9YTvdaCWqymFT1BCoKgrThF4CBZI8796d3QoDLCECdUTBIW9_3YxYBYkn1klWnZ3v0NhMoclJp3w_nwomNdrhq3JNaePSJ4B3VnnWmLrl_95ji34RRYCqVAfsZHENcjrS0Uha1ygYFWRERAY06XvOAz6eQf9JasUk456Fos8XfEUuEQVO6gKb7YIfVoN5XYCPsdMxvIXe8xDPuFr3DaUJECHVDAnRe7m-20k9ok08c-umhPPyq09gW5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5aee63c24.mp4?token=vBXMmJf-4PM3_khYzn7QX5YvrEox3Ff1AZjrpQu0DYCI98dtmmH7hzIbArkCG_nTt5z5CZQleRUodvBsq83mzlFlCclOJe9YTvdaCWqymFT1BCoKgrThF4CBZI8796d3QoDLCECdUTBIW9_3YxYBYkn1klWnZ3v0NhMoclJp3w_nwomNdrhq3JNaePSJ4B3VnnWmLrl_95ji34RRYCqVAfsZHENcjrS0Uha1ygYFWRERAY06XvOAz6eQf9JasUk456Fos8XfEUuEQVO6gKb7YIfVoN5XYCPsdMxvIXe8xDPuFr3DaUJECHVDAnRe7m-20k9ok08c-umhPPyq09gW5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔻
بيان من القوات البحرية التابعة لحرس الثورة الإسلامية بشأن تدمير زورق مسير تابعة للجيش الإرهابي الأمريكي في مضيق هرمز
أيها الشعب الإيراني العظيم والمستنير؛ لقد أرسل الجيش الإرهابي والمتحرش الأمريكي، خلال الأيام الماضية، زورق مسير غير مأهول إلى مضيق هرمز، خوفًا من الاقتراب والمواجهة مع مقاتلي الإسلام الشجعان.
بمساعدة الله تعالى، تمكنت القوات البحرية التابعة لحرس الثورة الإسلامية من إصابة زورق مسير (غير مأهول) تابع للعدو، يحمل الرقم 5838، من طراز "سيل درون"، في مدخل المضيق الاستراتيجي هرمز، وأفشلت بذلك مهمته العدوانية.
تعلن القوات البحرية التابعة لحرس الثورة الإسلامية بكل حزم: أن مضيق هرمز مغلق وخاضع لسيطرتنا الذكية ومراقبتنا الاستخبارية، وأن أي وجود معادي في هذا المضيق الاستراتيجي سيتم استهدافه.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90087" target="_blank">📅 20:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90086">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
المقاومة الاسلامية كتائب حزب الله:
بسم الله الرحمن الرحيم
​"وَمَا النَّصْرُ إِلاَّ مِنْ عِندِ اللّهِ الْعَزِيزِ الْحَكِيمِ"
نتوجه بأسمى آيات التهاني والتبريكات إلى الشعب اليمني الشقيق، وأبطاله في القوات المسلحة، ورجال أَنصار الله، بمناسبة الانتصار العظيم في طريق استعادة السيادة الوطنية لليمن الأبي، وتطهير أرضه من مرتزقة الكيان السعودي.
إن هذا الإنجاز الميداني في سوح المواجهة يمثل صفعة لمشاريع العدو الصهيوأمريكي وأذنابهم في المنطقة، وخسارة أخرى للنظام السعودي الإجرامي بقيادة محمد بن سلمان التي أنفق عشرات المليارات من الدولارات لإخضاع أهل اليمن الأعزة.
ولم يكن لهذا النصر أن يتحقق لولا الإيمان الراسخ، والتوكل المطلق على الله، والتمسك  بنهج العترة الطاهرة، إلى جانب الصمود الأسطوري والتضحيات الجسام التي قدمها أبناء اليمن الأحرار.
كتائب حزب الله</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90086" target="_blank">📅 20:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90085">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
‏
وول ستريت جورنال:
إيران تعاود إنتاج الصواريخ الباليستية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90085" target="_blank">📅 20:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90084">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8sU2qar6oQSH3mAB7X59jGl20bkLdGcYKWUiOR2C3HmhQAI7Ko6Lp4CYHWixGv6UwJAYaxCN8M4-z63AAQb4UwcV6UOb-CKGx257gvLQGRc8c1lIKTq5vceWcck4FIeQUzRt3eK5cN5WaH9h1aNUOxB5AAkcPzL_IplR_-I1-urMMmo4eryLaJqy3CupSd5iXYcuAH7jU6x5LZ-9nZthBp8Gpgf3A98LmKnFWPXmx490bw9Mk-u7hRdw6hDpSpYt2K6rqOddZ6iLOyoMTRXp8a_nEfBP9Ro9gbAY4WguzflfaLy-hm-XvxSD695b8UAVwYiuqzlLAJ7t_jXsj-NQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
: إليك جرعتك اليومية من "التوجيهات الاستباقية"، تحسّباً ألا تصلك أخبار من سلطات نظامك: إليك الترسانة التي سيستنزفونها والترتيب الدقيق لاستخدامها. تظاهرْ بأنك لا تدري ما سيحدث تالياً
😉
.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90084" target="_blank">📅 20:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90083">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQAgmH6UYsjlzkmZkpWdZl9l3u3Nvq3IPzJ8kyMTpRg7quhLFCQOYaIuh1ohM883ndmhS5aZn50cf4-i62WdDP6gn28ULmWOeiwqzR0ZLNkCNNRBiumNsYyzMGqdCDI60_csG8MrpOVEBGzgse6rS-ezWrddB4l3CrOEKMK8gnuNldn3H4robczPwYxkEtTibggnBXyr6BqQQifM9vAXbTjytNSdKxS83GveEzhb0pd3ieOq5APrcFPJsb55LbtSjOtnrTuPN1Z6HwEEvqUHRDkY53r3qo5Xnv0zY7Ut22ltfcQuXK7hM_UbwfiFmBTWkznyl5KHVYIWfdqLXeT5ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
بعد ان ذاقو الويلات:
أميركا تضع مكافأة مالية لمن يُبلّغ عن بيع الجمهورية الإسلامية للطائرات المسيّرة.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90083" target="_blank">📅 20:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90082">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
🇺🇸
رصد نايا
غادرت اليوم عدة طائرات تابعة لقيادة العمليات الخاصة الأمريكية قاعدة ميلدنهال الجوية الملكية البريطانية، متجهةً على الأرجح نحو القيادة المركزية الأمريكية، مع العلم أنه لم يتم التأكد بعد من كونها وجهتها النهائية. وتشير بعض خطط الرحلات إلى توقفات في مرسيليا بفرنسا وبافوس باليونان.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90082" target="_blank">📅 19:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90081">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
🇸🇦
الجيش اليمني:
شن طيران العدو السعودي خلال الـ24 ساعة الماضية 64 غارة جوية توزعت على محافظات تعز والحديدة ومأرب والجوف، من خلال طائرات نوع F15 وتايفون أقلعت من قاعدتي الملك فهد بالطائف والملك خالد بخميس مشيط، فيما تمكنت قواتنا المسلحة بفضل الله من التصدي لتشكيل قتالي قبل قليل في محافظة تعز وإجباره على المغادرة، وذلك باستهدافه بعدد من صواريخ أرض جو محلية الصنع.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90081" target="_blank">📅 19:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90080">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e493e9d419.mp4?token=dMRQBepyMdreLpm5Y1ik1ZdeJAAm4XBBH-We3yZXMRpH1LJTffbQe6UQ-Jx7Ve1CKVFrkYFoyjNFsNpHJMLU3dCqNaUK3Nn3OLk1a8JhcO6bhmpWWddMwvvLiwVS3d10LJqHYnrz7uHne8p6XZ9K-vfCit6EegUhoY6L9RqrJVURUX9oBqzBW5KU08_5oRPqgOKmDh_WXP_ZXLQbHXbuWMn_veEHBxuNbFigfLZb9SQLR94rFnoqpSt5VqD4dY2AlFqUJYgGCd7L0mtvaD8RHqnNNoliPyar-wEyVVQXMUltF6aUxtJgXgo_GaRZv9q8rXwLsi-PYfk_flIFjB-1dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e493e9d419.mp4?token=dMRQBepyMdreLpm5Y1ik1ZdeJAAm4XBBH-We3yZXMRpH1LJTffbQe6UQ-Jx7Ve1CKVFrkYFoyjNFsNpHJMLU3dCqNaUK3Nn3OLk1a8JhcO6bhmpWWddMwvvLiwVS3d10LJqHYnrz7uHne8p6XZ9K-vfCit6EegUhoY6L9RqrJVURUX9oBqzBW5KU08_5oRPqgOKmDh_WXP_ZXLQbHXbuWMn_veEHBxuNbFigfLZb9SQLR94rFnoqpSt5VqD4dY2AlFqUJYgGCd7L0mtvaD8RHqnNNoliPyar-wEyVVQXMUltF6aUxtJgXgo_GaRZv9q8rXwLsi-PYfk_flIFjB-1dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر اضرار كبيرة في خزانات التخزين في مصفاة جازان السعودية بعد الهجوم الصاروخي الذي شنه انصار الله</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90080" target="_blank">📅 19:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90079">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr5vFnmQ9ZBK9wyGNdjcd6e2HRM0KqlUxyLS1Levgzp339CFXa9Bnekr0AYFfBQSkY95B7d6Mk99ae21hvyUp3lGUs1UlzSHwTTr6J6yA6yaRYmrat-OuSr7__YL-i0iYJNi997YThQiGyOXgjAQl94UOE8pi4TDTvGuyc-74IE2_J6VYiwGuV-hd3-I5hrW7MgyRbHxLrePqfjSzSsHoz6yQepIuYkjTN11DBUbmj1SGwkYe16jZMQsgXIayy3CdbXcolm8Ru9IdOI7Iw6aydmqxkUW-YjBr1TKEz-xLXGBS3HbCslDj6mGoa2Wcm4aYjaGm5rh91NELB8m2blsOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط تصل الى 107$ للبرميل الواحد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90079" target="_blank">📅 19:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90078">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fffef3ae.mp4?token=nuwjE9cfSKftkKp8nJiM_FFWFIZmzjW584O-bySLrvKsLOJ15r0j0eUDuMXiM4ggbqJEwtDmDkEr33BjZOOKM-mOULYVZTXRJN3KIPiB4NmufLyN54uYtc1SVjKsrJvgeko275JE8rv5t09dQ5055VqtwIx-lXkInsPwZvCTTX-EeVSdwaA7Ap-dnB4kMaJqI5bKoEO-l98rOOV67X_MyrHCHQI8kfEKURHxBooL78LvK_C7SXRG534A12a-cUh7RrNGr9rLARRFTCgYPXsCV7_e5PWEfuq1xJJadjkbpLic0-UpQvmJ6mWUESWhUVkkANgY9nxW80eXZjk2y1918Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fffef3ae.mp4?token=nuwjE9cfSKftkKp8nJiM_FFWFIZmzjW584O-bySLrvKsLOJ15r0j0eUDuMXiM4ggbqJEwtDmDkEr33BjZOOKM-mOULYVZTXRJN3KIPiB4NmufLyN54uYtc1SVjKsrJvgeko275JE8rv5t09dQ5055VqtwIx-lXkInsPwZvCTTX-EeVSdwaA7Ap-dnB4kMaJqI5bKoEO-l98rOOV67X_MyrHCHQI8kfEKURHxBooL78LvK_C7SXRG534A12a-cUh7RrNGr9rLARRFTCgYPXsCV7_e5PWEfuq1xJJadjkbpLic0-UpQvmJ6mWUESWhUVkkANgY9nxW80eXZjk2y1918Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
مرتزقة السعودية يقومون ببيع اسلحتهم في عدن بعد فرارهم من جبهات الساحل الغربي.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90078" target="_blank">📅 19:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90077">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">القوات المسلحة اليمنية في ميناء المخا</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90077" target="_blank">📅 19:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90074">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlY2IrBshNmMuTWSQSoq1J0irVYNTPGzs_JbnvpXa02reph0ntF_40BOIv2q-ZJa5cPspw5Tnl1L4mdtFYQDV-82m4zgjthCzc4jCJ3J2_74bQA_1jqHttCgiWZnUH3RA595CNPpWIfgG5GbfmEE-jBreDCw89Oybn4PrYtdnhAdkBF1J3dm6XrZ-ewZrny5dDd2OU9eSZ2Thg4m6BXqJT2IrMZ_WPWQDNnrE1xN1vzAynwCCQ6SfXv1KyG9rxZhEYPWfvmOu3yR6BPMdQCTMriaJJa1Y7ahNRljGfjL_e3PSLvhpTno4ReVGwjpyVBSQMmCTz42HATAmVsx1y2B6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFqw2ENQlAN2GtONjTxlAREPCwZlFvqh8eXPUYrvR4b0GkqCxpk7gy1Ef7Tc5Q6a1JIDsEgChySWZ8da47IG-RE0dgIX0SGsBHJADS75NNAfcf4As6gQym_La-_5gEi09fwtccAz-fj5zDfbDsIdc17FstEfvQhiqiUXbkjZ-5mbJNiGa1Gtu9V4SeCuoHlMtQBvklIWACN2zQUm7Qn3VtpgaIYG8hl7A_0gNxVTx1MJGNr1Zc1mgO378NlO0D0swtnxJRQhS8mzKaUw1XROYAhzLJgJHgac85W-TggIEKwJ3R8y57d3b0axdbhOIQ2ucPqVzJfsdW5W0wLv21U8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcFzYZm8NLOSQV4lzzpKaah0Jrdus5YeqUMdWTrnyT86K5w07OXucByZSYPxlKVaNyGicJqCYIrHGvizkhdjNcO3zn6Cv7NfHN2YvWw57OcEyE90iBK7FrHHc6XJbkhVdqochC8doeGBtIu5jw3mbqIotqo06SD4cMfI1_fMEh_Hy0qimMGIy23zMYkPFn-YDaKjzPzN7gV9FM6L1sEJmgmghX2a8xet-YAB5eiLuDIByhxJILOPkz9gWNipD1bAwBkdzT_Q8dYQSI3zGwPvw9nwI_E_nXrqIXb3nn6Py7ElO0ByNvGixSAoxuQ5jfwzHC07sFNscjDQxMhPj9plFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇾🇪
‏محافظ الحديدة يتفقد الأوضاع في حيس والخوخة بعد السيطرة عليها من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90074" target="_blank">📅 19:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90073">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ميليشيا البيشمركة تعلن توحيد قواتها في محاولة لعدم خسارة الدعم الامريكي.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90073" target="_blank">📅 19:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90072">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9003eba0.mp4?token=e4R-XlfTx7wzCAe840gaC63AEedoUTlbQ99okv5wKTKof0BN-L6644-culcdj1FfsMFbPHQtK93W_SJorh74o79IhvAMM9CNgdl794Lm5Mk9xwPuZjcLGbFQygcurTauIGGKZm2pVg_oLJZVHx22P9qALnNIyZ9_Bp2qMkD1WTqSH2DDf7Ex-EMBrINzyiHvCEJo__rqzM7ARK9zezskSm-OktLv4GRjG1bAF11slbLfGrLTvVOIVEpdnbspNX-VMk96U1N_ZMFvP9hY0IeyT9LEkF3biIVqxnp-xdW-Cu8KJVFsaNqCIlAF7LdScKaU23YwUdDVLEVB5akXpc2FmS3Typ6K6yrEHy_98q2SIpCQYH1oPvW02PbWylXBkfpsd2tvCF21Zj7pArAh954Zc2I6KdPpfKHaKKNrlTuETWQXhjZbgBOcleJSQxSiBHWy5QB5F_gxIZoTm7iOA_mygSI1tlo-xvV0luf1kostIWVXAcvBAYpgXbvEQ4_lX1tO-jRQOFT6bE8Mog3ITmfN0OOfOqOJsXlCVJJp-iAOx9C1hOzz6Z12iHhSEp9FYNLiR8WThDNkNaZne-c29hWPrWARlHmhB8QGynYZNw_mcP5p8porJ84dUJhcf4szukyCGbUo2jAwJVWeuXlY-CNV8g7yPpM288IGSgP1cQEqnfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9003eba0.mp4?token=e4R-XlfTx7wzCAe840gaC63AEedoUTlbQ99okv5wKTKof0BN-L6644-culcdj1FfsMFbPHQtK93W_SJorh74o79IhvAMM9CNgdl794Lm5Mk9xwPuZjcLGbFQygcurTauIGGKZm2pVg_oLJZVHx22P9qALnNIyZ9_Bp2qMkD1WTqSH2DDf7Ex-EMBrINzyiHvCEJo__rqzM7ARK9zezskSm-OktLv4GRjG1bAF11slbLfGrLTvVOIVEpdnbspNX-VMk96U1N_ZMFvP9hY0IeyT9LEkF3biIVqxnp-xdW-Cu8KJVFsaNqCIlAF7LdScKaU23YwUdDVLEVB5akXpc2FmS3Typ6K6yrEHy_98q2SIpCQYH1oPvW02PbWylXBkfpsd2tvCF21Zj7pArAh954Zc2I6KdPpfKHaKKNrlTuETWQXhjZbgBOcleJSQxSiBHWy5QB5F_gxIZoTm7iOA_mygSI1tlo-xvV0luf1kostIWVXAcvBAYpgXbvEQ4_lX1tO-jRQOFT6bE8Mog3ITmfN0OOfOqOJsXlCVJJp-iAOx9C1hOzz6Z12iHhSEp9FYNLiR8WThDNkNaZne-c29hWPrWARlHmhB8QGynYZNw_mcP5p8porJ84dUJhcf4szukyCGbUo2jAwJVWeuXlY-CNV8g7yPpM288IGSgP1cQEqnfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية من داخل مدرج مطار المخا الدولي.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90072" target="_blank">📅 18:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90071">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">العدو السعودي يشن نحو 10 غارات على مديرية ذو باب.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90071" target="_blank">📅 18:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90070">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">العدو السعودي يشن نحو 10 غارات على مديرية ذو باب.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90070" target="_blank">📅 18:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90069">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90069" target="_blank">📅 18:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90068">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇾🇪
🇾🇪
‏مركز تنسيق العمليات الإنسانية في اليمن يُبلغ جميع شركات الشحن العالمية بأن الملاحة في البحر الأحمر آمنة لجميع الشركات، باستثناء الحظر السابق على السفن السعودية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90068" target="_blank">📅 18:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90067">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇾🇪
🇾🇪
‏
الاستاذ محمد عبدالسلام - الناطق الرسمي لانصار الله:
‏إن ما قامت به القوات المسلحة اليمنية في بعض المناطق الساحلية عملية وطنية في إطار فرض السيادة اليمنية، والتعامل مع التحديات والأطماع التي تهدد السلم الأهلي.
‏إن السلام الحقيقي والعادل والمشرف كان وسيبقى خيارنا الاستراتيجي، وأن على الجميع أن يدرك بأن خيار السلام مع اليمن هو الأقل كلفة والأقصر طريقا نحو إعادة تنظيم العلاقات وفق مبادئ حسن الجوار والاحترام المتبادل والمصالح المشتركة.
‏إننا نؤكد أن الجمهورية اليمنية ليست لديها أي مطامع في أي دولة من دول الجوار أو الدول العربية والإسلامية وغيرها من دول العالم، ولم تعتدي على أي دولة بل هي من تم الاعتداء عليها بما يتنافى مع الأخوة الإسلامية والعربية.
‏أما بشأن حرية الملاحة وحركة التجارة الدولية في البحر الأحمر وباب المندب فهي آمنة ومنتظمة، ولا داعي لأي قلق دولي حيالها، فليس عليها أي خطر من جهة اليمن، والعمليات الجارية حالياً هي محددة الأهداف وفق ما تم الإعلان عنه سابقا وتأتي في الإطار الدفاعي، ومتى ما توقف العدوان على اليمن وتم رفع الحصار عنه، فسوف تتوقف العمليات الحالية .</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90067" target="_blank">📅 17:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90066">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39dbddee2.mp4?token=KfgwbqNIyZnOWqujcSmPzFdt05YnFB6Zii1JFRW3TnDlVnjx1LgDZ1jYvmejLYM3ENQ3cAxgAW1M5bJDYtc8EATE348DdJZx8jV-p7bgxl1wRi-q8boswAdLHOTWGw1whEM_FWRDhm9bq6_hXyK38kvp_Mq8-Rz7M8UytBhoXYVp_Cg5TyAX6TsLEwRSwJJHd6IR2b1xfcX18tSKAJ1cB2-xdolImf3bOxkuMLawPrduWjSMwWkCv05WjgrU-QY9zP6IhW2l1qJPNajVitRyFdQC7RjyNvjMdvdcMQqh-EP0oN-JGehWqWYZG_Jx9UhvB6cB_OoYoeIPFaboeFVlzBmT7XEJi5V04rbtSp7izbAwhkfGfN7zCoJ4ojvaE8xHwAZ3WYHlKSW6AoRNKMdpp7mV6JvKdoPf7eZ1pCKjb72hUIXM4p6Dmh-PDSLRA1bYS_34pEEqkN53ehJ5ZxihGhJ3FFzVkBejt9cXYtvtjJKmHoCITqyowCa0WQJG_D7uJ-cErI5bOqOP0Tlyt4sfZaDhQXIj664VKsryuct4rOCRgCJusj8JxpyAW08v8pXS7agMXP7jfT5TvMSd-gBxs0JtC34Slf3cI4xUUlONnsp_nZvnX6OKFvizlWXWAOU1trHZB4VeuRMXzoYXVzb-a1V43x56BZ30nb3wBsCdF1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39dbddee2.mp4?token=KfgwbqNIyZnOWqujcSmPzFdt05YnFB6Zii1JFRW3TnDlVnjx1LgDZ1jYvmejLYM3ENQ3cAxgAW1M5bJDYtc8EATE348DdJZx8jV-p7bgxl1wRi-q8boswAdLHOTWGw1whEM_FWRDhm9bq6_hXyK38kvp_Mq8-Rz7M8UytBhoXYVp_Cg5TyAX6TsLEwRSwJJHd6IR2b1xfcX18tSKAJ1cB2-xdolImf3bOxkuMLawPrduWjSMwWkCv05WjgrU-QY9zP6IhW2l1qJPNajVitRyFdQC7RjyNvjMdvdcMQqh-EP0oN-JGehWqWYZG_Jx9UhvB6cB_OoYoeIPFaboeFVlzBmT7XEJi5V04rbtSp7izbAwhkfGfN7zCoJ4ojvaE8xHwAZ3WYHlKSW6AoRNKMdpp7mV6JvKdoPf7eZ1pCKjb72hUIXM4p6Dmh-PDSLRA1bYS_34pEEqkN53ehJ5ZxihGhJ3FFzVkBejt9cXYtvtjJKmHoCITqyowCa0WQJG_D7uJ-cErI5bOqOP0Tlyt4sfZaDhQXIj664VKsryuct4rOCRgCJusj8JxpyAW08v8pXS7agMXP7jfT5TvMSd-gBxs0JtC34Slf3cI4xUUlONnsp_nZvnX6OKFvizlWXWAOU1trHZB4VeuRMXzoYXVzb-a1V43x56BZ30nb3wBsCdF1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتال مرتزقة السعودية الهاربين تتكدس امام عدن وسط رفض مرتزقة الامارات من ادخالهم</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90066" target="_blank">📅 17:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90065">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a357cb919.mp4?token=XMIiXwhG3AFQwAMyB76kR-RxCGkfWMnWr6wHlyhftviFdPrdgBhziQ_NF63BiPVt_P4uJ--ipaX89OsyDXMCmNGWwie2L39eTJIF-X-6qEdTvOGxxP5VcGpAhVgWjB5B2HlceE7Y6s-IwTDsxceH34NF1cMtwiWimS2jSpBJPJqBLff1SFCd9IuGpQGpXa5kbvRej5PM1WJtHwMRIX8bFdAmdBzE61S4aaPwQ_DjG5ZprtuMTfnv_UaHg0hFebjyG9xNTuqnlyGfwbyVGiUyRnWQZuseyyH9aI3xya97muBVLuDkR7hi6WhglTboLlRQKLerNeB4FS16rgQ0b8aJiKVWHPUbU6tafdYOz91Bf3PLwBBcVBL2ulT2tOVwji2axuJCHrQnRKotliw4MvnZWnqSPWHNtR4pj87blIBNTTxsKi3fPmTgTLojHOWaWOX0JxDq8KnFqznhJw-n-M3_38Krz3rXriThkfbHnC125Kao-3yJUKgiL0hFxTzFcQJbDddQdD7SWYYoAFazxkJTXCpjpEnUydB7_VepL6M6pAUJpQua2nP9yfX7ArTrSAIAiObjrirTblDNtrRszz2zXL2C2Ex-KVusJ1_dNJmqHtYO4CrcZN3i2EGcUL2_wn8Z97Jwcl8Z4IgXoJkzEKBlYqnLx_3fb7vrpyCu_qFxxdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a357cb919.mp4?token=XMIiXwhG3AFQwAMyB76kR-RxCGkfWMnWr6wHlyhftviFdPrdgBhziQ_NF63BiPVt_P4uJ--ipaX89OsyDXMCmNGWwie2L39eTJIF-X-6qEdTvOGxxP5VcGpAhVgWjB5B2HlceE7Y6s-IwTDsxceH34NF1cMtwiWimS2jSpBJPJqBLff1SFCd9IuGpQGpXa5kbvRej5PM1WJtHwMRIX8bFdAmdBzE61S4aaPwQ_DjG5ZprtuMTfnv_UaHg0hFebjyG9xNTuqnlyGfwbyVGiUyRnWQZuseyyH9aI3xya97muBVLuDkR7hi6WhglTboLlRQKLerNeB4FS16rgQ0b8aJiKVWHPUbU6tafdYOz91Bf3PLwBBcVBL2ulT2tOVwji2axuJCHrQnRKotliw4MvnZWnqSPWHNtR4pj87blIBNTTxsKi3fPmTgTLojHOWaWOX0JxDq8KnFqznhJw-n-M3_38Krz3rXriThkfbHnC125Kao-3yJUKgiL0hFxTzFcQJbDddQdD7SWYYoAFazxkJTXCpjpEnUydB7_VepL6M6pAUJpQua2nP9yfX7ArTrSAIAiObjrirTblDNtrRszz2zXL2C2Ex-KVusJ1_dNJmqHtYO4CrcZN3i2EGcUL2_wn8Z97Jwcl8Z4IgXoJkzEKBlYqnLx_3fb7vrpyCu_qFxxdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم كميات كبيرة من الاسلحة كانت بحوزة مرتزقة السعودية في حيس</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90065" target="_blank">📅 17:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90064">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم كميات كبيرة من الاسلحة كانت بحوزة مرتزقة السعودية في حيس</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90064" target="_blank">📅 17:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90063">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czmZUlAQX9KvR0ILwlXqiet-VcuvNN6f-xGNep_TrJ2fhhS0cUj3Gre0Jdb4vgaLUoh7Q9mZyF2nlfidWLLJH2nOvM108upYxZBeT5xaJYMeVJS3Yh1K9M1kAJ1oCWvunzA22yGSt1b2OuX_Bb9ElTiuspeh3-qJsOO3FiZcIcmAwyQAkpc2HP0vlSE2zUkWDRLz5AKRI6_p1q_jePvVlj3KKcRLpriDDnkXvZkt5n9QKI1x5ooaU2Ob4a4vfBAt4cdLj-mwpXeWv5CbQxkRjI7-xCrj0WbqRsDRFtaut1_wLiGvERxfY6slaLEks_0dlGcbxSxQnrnVKL17HbnS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية من داخل مطار المخا الدولي.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90063" target="_blank">📅 17:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90062">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c28fafdac.mp4?token=Z-j9GnQAKyqeqs9medsYzb-KvHxMiYH8rA2yIq0nELnsRKw_Q0QcLosBd1y5Vr46QnBpKRUfRSttAJuv_Kwko9Aacto1L46sSm6dWxLTYMqonPk2WHtkUVC2vcsvFvdXROWnzaU-HHWwEdkqemLR2ir9XkbteV-sHlFsgWgOCmQJauuFQG3bk6DyjxtBFNPqhhCv2270WR9lLR8kNwgp0KPsXwHzOrzJFarBb73BefBFzL51KAtvG3O3GwpLrDw6SdaEz0WkSgE-swWU9rivTfbSXa0rMUhgngJsAyThILASQt6Vi5u6FztmHxVU1kGBbfQZ45dDGlymta-1ScVdYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c28fafdac.mp4?token=Z-j9GnQAKyqeqs9medsYzb-KvHxMiYH8rA2yIq0nELnsRKw_Q0QcLosBd1y5Vr46QnBpKRUfRSttAJuv_Kwko9Aacto1L46sSm6dWxLTYMqonPk2WHtkUVC2vcsvFvdXROWnzaU-HHWwEdkqemLR2ir9XkbteV-sHlFsgWgOCmQJauuFQG3bk6DyjxtBFNPqhhCv2270WR9lLR8kNwgp0KPsXwHzOrzJFarBb73BefBFzL51KAtvG3O3GwpLrDw6SdaEz0WkSgE-swWU9rivTfbSXa0rMUhgngJsAyThILASQt6Vi5u6FztmHxVU1kGBbfQZ45dDGlymta-1ScVdYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تستعرض داخل مدينة المخا بعد طرد مرتزقة السعودية منها</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90062" target="_blank">📅 17:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90061">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f352cc8f3.mp4?token=BOZQnn8nEGm6vXlNYB5mMgcz1fh1P1qtVkbw7c-_WsprGCtRFvL_pKnvO4qP74TyByT-B2zWfQEzgwV1d-_Q5QL6V1TQR060Iy_eF4es39_3IEoBwbDHLt6f9lY4yuZPoxFntI31zfT6qj-XD7_1zvw_K6PQVai2BKhVKxED6LkAKLPYcW8f0hPK1LV4SJnBKkEa4TCEEn2AMIXRvw9lZmXrJGfNs7YWb0mOEOJTP6LcuFU9Ga1g0o5adyY3kQ9cd7NwADyFK_09DcmGufHiJI2dxoKTQ1DRq0IZ6YZlq26Q5wM-qhxHmqbYFsTHZM_6yPwxamN-wENgGInmFX5JC6tJgG7y_XEcCaca5q662uVkzYkyZVYZPlusfUm6c3x8am0WwRo1dHU7aV8C4m_RKTq-Vrh7Y8cUkm6hi-ttpcmJ4rnt95BHL7-D41tX6IXK_43-QgKbI_eunfrQ1F4-uXzaXvVHRf3aySnV0wLhP075ScAPHVVUQRnNN6yZ3D99042cHFcgk-pSaiaZxRNIRdTlEzUZ1B9jDayKer2V82zJKU3aRsX50t019UFHr_dFnfi2LlGNktD-cmiQzTTsnp8I_ho0G2LdHSKdL8Ye8lAypz3faGXHBrvHK41mK3ccMR66RQm-sCfbWMxh_VYZgvzoXDbJQ0okK9pmU0uY1Bk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f352cc8f3.mp4?token=BOZQnn8nEGm6vXlNYB5mMgcz1fh1P1qtVkbw7c-_WsprGCtRFvL_pKnvO4qP74TyByT-B2zWfQEzgwV1d-_Q5QL6V1TQR060Iy_eF4es39_3IEoBwbDHLt6f9lY4yuZPoxFntI31zfT6qj-XD7_1zvw_K6PQVai2BKhVKxED6LkAKLPYcW8f0hPK1LV4SJnBKkEa4TCEEn2AMIXRvw9lZmXrJGfNs7YWb0mOEOJTP6LcuFU9Ga1g0o5adyY3kQ9cd7NwADyFK_09DcmGufHiJI2dxoKTQ1DRq0IZ6YZlq26Q5wM-qhxHmqbYFsTHZM_6yPwxamN-wENgGInmFX5JC6tJgG7y_XEcCaca5q662uVkzYkyZVYZPlusfUm6c3x8am0WwRo1dHU7aV8C4m_RKTq-Vrh7Y8cUkm6hi-ttpcmJ4rnt95BHL7-D41tX6IXK_43-QgKbI_eunfrQ1F4-uXzaXvVHRf3aySnV0wLhP075ScAPHVVUQRnNN6yZ3D99042cHFcgk-pSaiaZxRNIRdTlEzUZ1B9jDayKer2V82zJKU3aRsX50t019UFHr_dFnfi2LlGNktD-cmiQzTTsnp8I_ho0G2LdHSKdL8Ye8lAypz3faGXHBrvHK41mK3ccMR66RQm-sCfbWMxh_VYZgvzoXDbJQ0okK9pmU0uY1Bk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرتزقة الامارات تتأهب للنزول لشوارع عدن وطرد مرتزقة السعودية الفارين من المعارك منها</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90061" target="_blank">📅 17:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90060">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مرتزقة الامارات تتأهب للنزول لشوارع عدن وطرد مرتزقة السعودية الفارين من المعارك منها</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90060" target="_blank">📅 17:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90059">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏رئيس المرتزقة المقيم في الرياض يدعو لتدخل العرب والعالم لحماية الساحل الغربي</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90059" target="_blank">📅 17:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90058">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏رئيس المرتزقة المقيم في الرياض يدعو لتدخل العرب والعالم لحماية الساحل الغربي</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90058" target="_blank">📅 17:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90057">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اعلام مرتزقة السعودية: ‏الحوثيون يسيطرون على جزر زقر وحنيش الكبرى والصغرى الاستراتيجية قبالة الخوخة في البحر الأحمر.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90057" target="_blank">📅 17:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90056">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcrfPwbymIPf7J8XXJKyi_RVXmPvwXXGKC5ivfrTvCZe8qNUibedMqzhf5TW22NF_xh3gem3C6XWHrVPUxXzjLx50NLqyUQSOyO3yGHy4CQ_tNMzkwkXGUidgF3wewxB0uwKHSCww3WUh6PIVs4OzkwuciqHAAh7xryvOrtGyytjTKguSB5PZfx9PAavR9jAVGk1PAR9SvIXiJ9yTff3RObh4T9enbCGkFYgP5fDo2_SEQl2BWimKN0vUawoj9z3v2To9Exdf2UDJOgMNEfjpWMp7K_dQxQJk4s41lTSCEHjXyj3axeuJRqmsiPbu5AFdh9aze4R-OB6r3QSzVnSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90056" target="_blank">📅 16:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90055">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90055" target="_blank">📅 16:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90054">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مرتزقة الامارات يمنعون مرتزقة السعودية من دخول عدن بعد فرارهم من المخا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90054" target="_blank">📅 16:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90053">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060ab4db91.mp4?token=ORQPqWth0HKGC1U_VjW5Li0Fq1CnIHOXLVFSE6IrERSRKcUDyeipWQyDiStrNeG4zTf4jLRjqRfS7lKV4i2WzZWlnIXbkY9k0KjQ6nR4tQVPiht5w5xESzwPuDIj-ZL2_lD99w1bk1eHl2gTM-i8l-HdPDngPdJO3ICNOqLcKJx5H849OG6rig_a0RirTssOOiASpNNal9DVjws9GqtP9jqr-lIPme2TKklOtgX2wZbpYN0dzerFFsBxohniKksAvje5MHtBsuWNhE9aFo-AIIl2l8ma9HuDluGPHbsRxipdii6OVjeTVQNrFql1GoRrnHT2XMBC-wszHuBdxQXnQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060ab4db91.mp4?token=ORQPqWth0HKGC1U_VjW5Li0Fq1CnIHOXLVFSE6IrERSRKcUDyeipWQyDiStrNeG4zTf4jLRjqRfS7lKV4i2WzZWlnIXbkY9k0KjQ6nR4tQVPiht5w5xESzwPuDIj-ZL2_lD99w1bk1eHl2gTM-i8l-HdPDngPdJO3ICNOqLcKJx5H849OG6rig_a0RirTssOOiASpNNal9DVjws9GqtP9jqr-lIPme2TKklOtgX2wZbpYN0dzerFFsBxohniKksAvje5MHtBsuWNhE9aFo-AIIl2l8ma9HuDluGPHbsRxipdii6OVjeTVQNrFql1GoRrnHT2XMBC-wszHuBdxQXnQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرتزقة الامارات يمنعون مرتزقة السعودية من دخول عدن بعد فرارهم من المخا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90053" target="_blank">📅 16:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90052">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔻
مصدر يمني لنايا:
الجبهات الاخرى التي فتحها مرتزقة السعودية لايقاف تقدم القوات المسلحة على الساحل الغربي تشهد اليوم توقف شبه كامل بسبب انهيار معنوياتهم وتواصل تقدم قواتنا المسلحة وسيطرتها على مواقع استراتيجية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90052" target="_blank">📅 16:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90051">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ باقتحام منطقة ذو باب المطلة على مضيق باب المندب</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90051" target="_blank">📅 16:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90050">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93171897c.mp4?token=Be4fNk4gTs9C1tGvoBPGSc6bpi1yo0iiYqA8KQ4cQuWooL3ZdXNQAF8Zoi_FA9hoR4FDnohR4Q3TlqjZ4Ss88J65Ibid_ck-Gy1Cl1KT-W39-fGqxuhLT3KjgFLQEYOprWStJi-czZVGy3EWoC74t7sr09knbyXxPNSBIQ-JhJWPEdpPsGIeWi87tUnUV3xLURbYibAr9guv_frNmznUcNdXogTEnIlBQeu2vFDEVJB6CePyB28D9-f_ocnau0nJR1hdSAYyBxWcCKi_JtnTKL4WyBGZpkTCXLNSE7OWds_EHstJTCXcbU969gKzNzBllsY2NHRXkqiB24f6v0MZUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93171897c.mp4?token=Be4fNk4gTs9C1tGvoBPGSc6bpi1yo0iiYqA8KQ4cQuWooL3ZdXNQAF8Zoi_FA9hoR4FDnohR4Q3TlqjZ4Ss88J65Ibid_ck-Gy1Cl1KT-W39-fGqxuhLT3KjgFLQEYOprWStJi-czZVGy3EWoC74t7sr09knbyXxPNSBIQ-JhJWPEdpPsGIeWi87tUnUV3xLURbYibAr9guv_frNmznUcNdXogTEnIlBQeu2vFDEVJB6CePyB28D9-f_ocnau0nJR1hdSAYyBxWcCKi_JtnTKL4WyBGZpkTCXLNSE7OWds_EHstJTCXcbU969gKzNzBllsY2NHRXkqiB24f6v0MZUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية في ميناء المخا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90050" target="_blank">📅 16:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90049">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4Ek10Xm3JqWVGRWBo09lwjAwtvEHMqfnXwIqdBfrQ1UAl0fulkqmstqtk6Vf2_czM9CyDbg0-_lJZz5w1ve21AQSpfv2epw9JG9aKrJerXnDk5X8nmjIJ6nqva0cj-YQY-NpYWUTP3aB15EVCPsCLsDb23CxHC8Dow_utluInx6q2E9FM-icWz1aIgiJ8iPzvD5K6gGaRZSZ23H9EDuE7lm1qUmHCkvmhKXnvJb5u_Jctliqb3KfDL2mpNZwN2YxlHEflqvxi9L_zfo3JZ7PoF5ocGOlXnbsNI4WD0ziVlV9mQobbKfg9A1fI6q_BQf7ScxV4XoK2eAFK0-d_cZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية في ميناء المخا</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90049" target="_blank">📅 16:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90048">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902b8b8c56.mp4?token=N0b4mUJjkNn9z7NFwDWG1gpXeqAQk47ER3Ng9tPj9w18y74TU_69msr5Yuc3FikCZxCeQt-LPOi-STcTOG8svkxlP0OQaYW8Ti2fjmLZ6t9bAXpNWXuzl8Vs2nQMi9u7khKV4_Cyzr67jqR-M5onlluRMw9muWu1meZqajIVM4v4uuGWElQuduM0kyXQcqDAw-sKUiCksqwvhQuizAdhN41VenEAwf5pny-j6XKdq8I5YBn8yvz8dlCszaCj8XKgE5xD69j5t_05UtIHxGHUF4TsnAqSqj-ysAqF1zkGVGzuLyrF7dc0-z25GfewJcV51ipJGQdBJDnvEFksefd5OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902b8b8c56.mp4?token=N0b4mUJjkNn9z7NFwDWG1gpXeqAQk47ER3Ng9tPj9w18y74TU_69msr5Yuc3FikCZxCeQt-LPOi-STcTOG8svkxlP0OQaYW8Ti2fjmLZ6t9bAXpNWXuzl8Vs2nQMi9u7khKV4_Cyzr67jqR-M5onlluRMw9muWu1meZqajIVM4v4uuGWElQuduM0kyXQcqDAw-sKUiCksqwvhQuizAdhN41VenEAwf5pny-j6XKdq8I5YBn8yvz8dlCszaCj8XKgE5xD69j5t_05UtIHxGHUF4TsnAqSqj-ysAqF1zkGVGzuLyrF7dc0-z25GfewJcV51ipJGQdBJDnvEFksefd5OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية في ميناء المخا</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90048" target="_blank">📅 16:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90047">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90047" target="_blank">📅 16:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90046">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90046" target="_blank">📅 16:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90045">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDMaQuS_r3F1khY7hVbqh9Wpq-Nh9Rtp59ZsoPIGR_B-QbYPHFcWMBfbSMt-XV5GuIuPhCg1NgoB2hx6W7eKrWhvmz2CyH4jizBQv_IAw2dXfTK_PphgLHa9OIIwFyU82dfPuWvBpDCKM_4bHuKwv3Ap_UhpLmjUJIORBXuVIjwJhInQev2Ggqifrv_0v15KUrMOipKsxxwmyaQ4Nc8SfYprzhrBlcCcLJQGdEuyyhQRswpaxRDOlor3X3H3ISPCeTlVQZkhlOAycTsvkr3A5rm9tehV7tDga4n3IXB8BExWzTYh5YtQmlPbGy3i0obQWHTkePFAOz-Xm0rtLD_PCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
بعد سيطرتها الكاملة:
القوات المسلحة اليمنية تعيد فتح الطرقات الرئيسية خط البرح ـ مفرق الحناية ـ العوشقة ـ الوازعية البرح ـ خط الحديدة ـ مفرق المخا ـ مدينة المخا " أمام المواطنين والمسافرين والطرقات الرابطة بين مديريات حيس والخوخة مع باقي مديريات محافظة الحديدة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90045" target="_blank">📅 16:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90044">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSTVIFhasYA3vy6O0rl_cq-Vw3dHQ6UMtJTP8nsm-kL9uNIhdka4sh7gTvxcY9SrPTnEKul_KvE2CIb9OgLwn5CzSLxRb4WExGYCJQs_iGnRawswvQficIqlO9eTgPcF8Z2dhxKnO7OyMjE2XZchmWXrJzoaKg3j5DOU91DNRJJ-J_Om1v_ipV4-_L7UCuDUDzzPRltuhaqzFopYkzIRIZeH66xmBH5blhguUV2NzmTN1-htPV3Cj62lH4oLPjX4CyYzJj2Q9IK-FbAUsrFt04bql5Kot1b42Cr2d6K6ktWVwbrq0uR08dUMysy0LZz80j0oElyCpHpBzjPvId_Dkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذهب إلى فرعون إِنَّهُ طَغَى
المسيرة القرانية تنتصر على محور بعل و ابستن</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90044" target="_blank">📅 16:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90043">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hESl2_d8MiAL88ClK5j38y21y7mBJ01mXoSFNCFagvn0cYPxbTwlwPyjWrlsIYwAP1ZA-6tPONO9vCuptZFP-VgTUtexC4xFY4DiXnnjLuMIIzCTC-yRzrgMflyJBsi3FN0lRvGTCjs6od67M2B1WcGSdpt8CBnUmy-pJSAOd8LhQkdiqrR_HjpUgz3DP1woSNr0J_gl1wQgQrs6uyJxJyc5J9XBiYiVV71CJNVtlCEkeH6NO23xolmXEm96EM2wcD1-nBikQo5LLnNucdWSHgLzTqjMECgaAPKYrhktrZbPvKuwu-PunlgsCLUfrd1yvgVN-Lp8AU6pfm0eBlWfBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ارتفاع اسعار النفط الى 105$ للبرميل
.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90043" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90042">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇾🇪
مصدر من الحكومة اليمنية لنايا
لا نفكر بالوقت الحالي للزحف نحو مكة المكرمة .</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90042" target="_blank">📅 16:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90041">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igeL7Oes7Pgs48pqKBD0MLtlZhVTirfN0c19s67nGRU-PP1wsC-WxpoEHuTTuM_gMZW83gdLAf1zLp8D5JjUeGo5STZoA-0noXsdmDCFEijWie0dmWoETaLV0Cb7nFm9_Zcj5SHE_Oxc1M_fO4URTQ7MCU572HXA5Di4EwbVFS25510TS7Pe7mPk7jPyBSkazGpOExK1rDjCynl37a1WzpYduC2aqCdmy9c0nYAxMrpVB2uZZEjEJ89VkU9ikWNWvBgGUAW-kmHJR7omDehhEGQ_xgVBPVKCa6G2Nafi-0WgjyOnU2IlBQkSNHi0L2bhg2T6z5aZnJ6eI0_YOyYvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسؤولي انصار الله يبدأون بالاستماع إلى احتياجات المواطنين في الخوخة وقضاء حوائجهم بعد هروب مرتزقة السعودية من المدينة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90041" target="_blank">📅 16:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90040">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzMtimX8Dc3ep2e5eoOLDkBkHUcGbnB5gk3FUKsWd7jXwk40Br-zzwv1uZ7H2gsbRKJsDparOsOmenkdiVTABm-YD8w5MZBUyFzoFhbyMf3RFcKnk3yJ4iyvVGBZiJ012TldWY36TwtQPq1Jm5Gnfb9KQ2xY_Wo4no-Xu8R4ZPbmsQd4jiHYX7VPDHJvBrJJuL3clJlRDi5PGBPumlAI6N67iAO6sf8tm4tLa9xYFRynb5bbNeRH9yWNswDJDnHZg3WXWh2s7JpgMaDByrIj4XkRDgIRqNTBLtn68_dbyFrKQKy47SW--GdR_0LkW933yaZG5LMCIcSMg0vCjsuNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار النفط تصل إلى 104 دولارات للبرميل بعد تقارير سعودية عن انخفاض في الإنتاج</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90040" target="_blank">📅 15:59 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
