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
<img src="https://cdn4.telesco.pe/file/PADA92dWzcoVkG2MMFL-kV6JCddL1Xa518iWoi1j6RWPNZE2nxq_1glLQdbswKQpVVr1zsxMhGh3FM5yeLd4wyn5rgSdeUJzeBOwYM-bt2AcCjpasmG9wKWIUUNN_JqD_volbI1ie6tqdafsE8tbndpDo_FGuEZFJey9BWOg74-_HP-prIWT-aBfl3mwbb7HVpZ1HWc61TeX8Fk2_1BZe7omBTtLp0dnLRHUQJLCIz_QDfFMCbOsF5_pd5vDU4ar4XDw3NTpAzIjFfBB1QaIXQgI256CWnIv-Jv_Kw6fmXI70J8viLFOMJnx1RgzH4pgFD5L0N_Z3aCpJgZbnNQjaQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 04:50:25</div>
<hr>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qia-P_vF1XX_UfyE5sf1mODjf0HuKmM_aLxspRgx-ZtoJAHhZX26lcNYHdK33b1dglUCTjD-hVFxG6vX22Ix9P1fDCiM7v3UVZ44tNIDGjF3Zl53zVMHAo_Cdff3zJUwCf9dlosAhjwicAJX_RtdrkarJsnNNNziYW86XJPmeVNOvUH2oMMIHR9r-67PiAYWEnN-cRfRWQwlbSoEuP5oWGVWnWWPUnsgsbg_pAF3KE7GSDFo12fkzXZBJ0LSKojYvUdi9sQaaZPnDQn2RSsrBukAAwZEfO0l0cZDTKuhP-S_caxClY3bBd1Acpk2bN3qXIjb6Gi86hOrW8DOaiqgww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=MMj3dUKaTOLzQxCNSksQBTAHxGykFoF8bi_rVBYkBBvLHASudwk1WCtrOWpaWYkLjduY3j-a9qdc5pqXRajERKbZzcyYomnK1TKxsM-nnNMIA_uYbqLQ2BJH4ki9LkRFtIKaeLEtodNWnXQ8nchoEsA1IF7jodkq167grpNjtU0IQmgJJjZ-bwiSlfxWnq8ucXgHwCEJT_aew6to3-KJb5SYSDUPQ1QCP24g1k1UhYa9WTtoiesT-8RlriiB10uGMDplzTtO-qD2-IvkbYrKbDLdsbDLyxbo2KKTghkfOGdheVM5VBv_3gi1wCOTK8PcPSYLQiZTMIhLYyH-7z-Lua_9sr8SwwB6Dm3mZZqN1Mz21CaQH0Op6_N7uHjYtYylLeoS7lCxa52CRrvfEvu59rn8QCCbBDPxnGnSQXtWoKE5Pvx6tqw1xQznNrOqX-wIa2L6wDnIu8SU5LG_yJ6dvl0bxTcXO3sBjqF_uU920n5yCCuzPpnT29YFFQWw6ZOq5zuAgNoYIZ7EbAjtCl7HJ4jHNofg981RasGzDxrYgmozS2CLTJUvmATZor6EDbTGNWMPG3EvNYBSrIhQRWKhQ90MW_MOC2KvZeJw5r8Ggv249etjpU5XQegeBxOzTEScrecxAUBDoIoAWDtMXhHf5wrPhv_M0AHVv9KbqQnRb38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=MMj3dUKaTOLzQxCNSksQBTAHxGykFoF8bi_rVBYkBBvLHASudwk1WCtrOWpaWYkLjduY3j-a9qdc5pqXRajERKbZzcyYomnK1TKxsM-nnNMIA_uYbqLQ2BJH4ki9LkRFtIKaeLEtodNWnXQ8nchoEsA1IF7jodkq167grpNjtU0IQmgJJjZ-bwiSlfxWnq8ucXgHwCEJT_aew6to3-KJb5SYSDUPQ1QCP24g1k1UhYa9WTtoiesT-8RlriiB10uGMDplzTtO-qD2-IvkbYrKbDLdsbDLyxbo2KKTghkfOGdheVM5VBv_3gi1wCOTK8PcPSYLQiZTMIhLYyH-7z-Lua_9sr8SwwB6Dm3mZZqN1Mz21CaQH0Op6_N7uHjYtYylLeoS7lCxa52CRrvfEvu59rn8QCCbBDPxnGnSQXtWoKE5Pvx6tqw1xQznNrOqX-wIa2L6wDnIu8SU5LG_yJ6dvl0bxTcXO3sBjqF_uU920n5yCCuzPpnT29YFFQWw6ZOq5zuAgNoYIZ7EbAjtCl7HJ4jHNofg981RasGzDxrYgmozS2CLTJUvmATZor6EDbTGNWMPG3EvNYBSrIhQRWKhQ90MW_MOC2KvZeJw5r8Ggv249etjpU5XQegeBxOzTEScrecxAUBDoIoAWDtMXhHf5wrPhv_M0AHVv9KbqQnRb38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=rtIy4Eyimgli-AUpel4-NAZ5Xl9RgLzDofoeFfO4yv_aYxKSVaRjvMV9TYY4-C5WYE4uejPsGW4fuDb5XI3_kQRHU3wgJf1qhn4Kr6l-R_rYmqtqXsvB2GnGAOwiF44EvjtzpWN5wW1lrrUUTfQhALkQG4K8tZUPepcKEiQmk1j6vj6Engz7jR7_7s4izNaSYu4_PPzek7tbsifP4GB6fEc8VS4NExUk-MHluoM4U3kv43-3H7QyJHrjy7HDdUDZDwlRBhWULEebTbTlWY4uRwywqjaU4nnbRwHqV7x5UOpfqH3CVFwO2waQ1W1ur8EmEI5uFyCRSLhgJz72Prm24a2j-rkL26EmjqSLViw_MMKY6v5ydC8OJk8EdrkPw_qhBkYe1DRgK1XPgcWksl8yJ3NMunfEdT3TAEXq6Th2ZMWzMMLzZ325VgW5d3pP6faa5AGKI-FzZL_c84PsONbk2TsIERM-DEd3XeX3MtWXTG05pK0Z8zERqcYV2CgrBwGzQJdM4aKWGwSGwdhhKrzIz536UWXCy1qJhNwcZnu_cjtbsENtBNZ55BlEZ1GnmhAvHwVt7Mae2wlH0fwRqv-1iZ674jpwUlXGPaqX9rL7geVOugeb88o--_I78CcrxEoNG7gg_Tzcj8rS0Q8coy-5o9c21s9bypXZ66EYOgcoLeo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=rtIy4Eyimgli-AUpel4-NAZ5Xl9RgLzDofoeFfO4yv_aYxKSVaRjvMV9TYY4-C5WYE4uejPsGW4fuDb5XI3_kQRHU3wgJf1qhn4Kr6l-R_rYmqtqXsvB2GnGAOwiF44EvjtzpWN5wW1lrrUUTfQhALkQG4K8tZUPepcKEiQmk1j6vj6Engz7jR7_7s4izNaSYu4_PPzek7tbsifP4GB6fEc8VS4NExUk-MHluoM4U3kv43-3H7QyJHrjy7HDdUDZDwlRBhWULEebTbTlWY4uRwywqjaU4nnbRwHqV7x5UOpfqH3CVFwO2waQ1W1ur8EmEI5uFyCRSLhgJz72Prm24a2j-rkL26EmjqSLViw_MMKY6v5ydC8OJk8EdrkPw_qhBkYe1DRgK1XPgcWksl8yJ3NMunfEdT3TAEXq6Th2ZMWzMMLzZ325VgW5d3pP6faa5AGKI-FzZL_c84PsONbk2TsIERM-DEd3XeX3MtWXTG05pK0Z8zERqcYV2CgrBwGzQJdM4aKWGwSGwdhhKrzIz536UWXCy1qJhNwcZnu_cjtbsENtBNZ55BlEZ1GnmhAvHwVt7Mae2wlH0fwRqv-1iZ674jpwUlXGPaqX9rL7geVOugeb88o--_I78CcrxEoNG7gg_Tzcj8rS0Q8coy-5o9c21s9bypXZ66EYOgcoLeo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=KIbnb80nsbs7h1CSs22c02oIGCYoGY8mHb0hiGmPi9TPdu3-WcPT353-r5LmBdG8i6AkSmgXKmtIM9_6R5pcIg3FL4O1UxRYvd8jgepMqHUDACqHPQcde5xtFXPjmtvqTS527Et2yQN4SOdX_W51K2vrmHkROGujcZ8_YXK1aOGQ32pjafVhI8GFkKLsQHP-Q3z-oyUqmEcGz8XaSSBl-3Kk_r_RIW1y-ylBG_3k2Vigxx-etq-DMpTjHLShkWXvAOkqD2V0_rniO1r7XSe0FJQe_d4ZY-Vm2JdXjfAFszN7a0F10U-ufpbf1p9id_qJYvS1GRh2UzbjEIxTrVRFyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=KIbnb80nsbs7h1CSs22c02oIGCYoGY8mHb0hiGmPi9TPdu3-WcPT353-r5LmBdG8i6AkSmgXKmtIM9_6R5pcIg3FL4O1UxRYvd8jgepMqHUDACqHPQcde5xtFXPjmtvqTS527Et2yQN4SOdX_W51K2vrmHkROGujcZ8_YXK1aOGQ32pjafVhI8GFkKLsQHP-Q3z-oyUqmEcGz8XaSSBl-3Kk_r_RIW1y-ylBG_3k2Vigxx-etq-DMpTjHLShkWXvAOkqD2V0_rniO1r7XSe0FJQe_d4ZY-Vm2JdXjfAFszN7a0F10U-ufpbf1p9id_qJYvS1GRh2UzbjEIxTrVRFyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=pEfshKPhUeOYiXOAoShl4NqZ-y81MO_Y7oUz0tkTOsUHPAoZ7e8bJiwiMnfBtHdgyKjjtMTmKvK5smoh8dQXAGwTnR_vfh8Od_uf4vv567qByA29yYujhMVaB-twQCBcyzmBYnhpNjiqFTIYTFkE3vna1svylgCQqUIWc_D4xxyKVq-PUtYkl3Ds4lTyKgndm4o85c_1TjaTfEBR_3IrLzVetbMdUyvsXRN8B-tN1HmNFCl-BClMGMo2PMJE5u_9jRpxeu8uxyQMZh1IxvSAA1cG-AgNAdCwaQ_SDADBFIHBos0Ejg_SBv7f0klamHqQIwk7iJUI42NMQTkWq7Nh8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=pEfshKPhUeOYiXOAoShl4NqZ-y81MO_Y7oUz0tkTOsUHPAoZ7e8bJiwiMnfBtHdgyKjjtMTmKvK5smoh8dQXAGwTnR_vfh8Od_uf4vv567qByA29yYujhMVaB-twQCBcyzmBYnhpNjiqFTIYTFkE3vna1svylgCQqUIWc_D4xxyKVq-PUtYkl3Ds4lTyKgndm4o85c_1TjaTfEBR_3IrLzVetbMdUyvsXRN8B-tN1HmNFCl-BClMGMo2PMJE5u_9jRpxeu8uxyQMZh1IxvSAA1cG-AgNAdCwaQ_SDADBFIHBos0Ejg_SBv7f0klamHqQIwk7iJUI42NMQTkWq7Nh8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ZbeoRQ1rpl74-annyCplLOeMaaQm9FbkOfph933nQ05me9RghIF3WzF-CN-CUrKvrADxZ1eB9cO1BHGVnZwD1bked90K1M-cNh8Seh8WEFnUSWmFfNJoQtIkhF0n18WMRrUPZRsx1fzOs6D9ln6hwI4oRee8X6iBI_H6GbB3BMhE9VkzTg_D4Yt5JxLFq1h9wPjfEgtoWK5JKrMNun6xrCB80i4zHUHXFbV-qRzydL-mIhxL5aCkMJhYQscqIsqEizfqJg8OGvU3nQ0w8iXLgVrEaQAa-gZ_ekBl1Y2Vc2TOA-XD8PV-bXCAb3uBiRXyqG2A-bwblbZLJ-SXJ5v-Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ZbeoRQ1rpl74-annyCplLOeMaaQm9FbkOfph933nQ05me9RghIF3WzF-CN-CUrKvrADxZ1eB9cO1BHGVnZwD1bked90K1M-cNh8Seh8WEFnUSWmFfNJoQtIkhF0n18WMRrUPZRsx1fzOs6D9ln6hwI4oRee8X6iBI_H6GbB3BMhE9VkzTg_D4Yt5JxLFq1h9wPjfEgtoWK5JKrMNun6xrCB80i4zHUHXFbV-qRzydL-mIhxL5aCkMJhYQscqIsqEizfqJg8OGvU3nQ0w8iXLgVrEaQAa-gZ_ekBl1Y2Vc2TOA-XD8PV-bXCAb3uBiRXyqG2A-bwblbZLJ-SXJ5v-Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=S7_4XnPGV7hckGwFtwZIf3CoW7vEtfNYH056Gu4x4KcUmbZdSX2W9zi5k-sRbUh8P1U9DsGx70h1PeTfTfCAcZImyO4gsL-LYWr7povNjo3sN3HEkJePLQkx7W6jmuw1XFCzZKJ9-Q3MZvyh4K2o38rFHDZ5SFy-RZ8G_Z8kIGKvjIggN1t_SfVAg8zm2ERUBhBL6HOpXgKk4qzxOLD9dvxx6WN_tVSKWgAItx6197yjjH4bRG0VuBJQCa8lQ59n_QuMqs-2EeL2pSeKleBIQCQ-ajR0xQ7AyP8pmIBZKy0K96VFKRos8TCcEc93wMUMQeeoxaBHvOlxCiaW8J2wLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=S7_4XnPGV7hckGwFtwZIf3CoW7vEtfNYH056Gu4x4KcUmbZdSX2W9zi5k-sRbUh8P1U9DsGx70h1PeTfTfCAcZImyO4gsL-LYWr7povNjo3sN3HEkJePLQkx7W6jmuw1XFCzZKJ9-Q3MZvyh4K2o38rFHDZ5SFy-RZ8G_Z8kIGKvjIggN1t_SfVAg8zm2ERUBhBL6HOpXgKk4qzxOLD9dvxx6WN_tVSKWgAItx6197yjjH4bRG0VuBJQCa8lQ59n_QuMqs-2EeL2pSeKleBIQCQ-ajR0xQ7AyP8pmIBZKy0K96VFKRos8TCcEc93wMUMQeeoxaBHvOlxCiaW8J2wLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Ec2Uz5HtP61JMu5Ud-_Kqwa6paD84jmozTUhmBQI7yPFscRF7W7DqsNb-9qqTNe7yH3kSyj5R0YAuE1oO7-3f6hmd-5HdFuVAKbspYe8kNSkCf7C0NE-TzAfU6zIQuf5YlLbZCX5bY_W72p63sP3I0cqQdwpEr8cbpPHPEpwGV3Rm3jnIMiIZydMDU8XJ9q66rngF012Px8mbTCuWDHtjzWXa8u29my-eTkthuIWrwjsufZRAwDFiPzx8pxjyv-z9tU7nkSy-BWQI63BabWMOKVWBUAe3Mv-znCo4gGGIgscSuwA5HSkIt16Pv9fh8CNZswMCXILf6041C-lSRXlHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Ec2Uz5HtP61JMu5Ud-_Kqwa6paD84jmozTUhmBQI7yPFscRF7W7DqsNb-9qqTNe7yH3kSyj5R0YAuE1oO7-3f6hmd-5HdFuVAKbspYe8kNSkCf7C0NE-TzAfU6zIQuf5YlLbZCX5bY_W72p63sP3I0cqQdwpEr8cbpPHPEpwGV3Rm3jnIMiIZydMDU8XJ9q66rngF012Px8mbTCuWDHtjzWXa8u29my-eTkthuIWrwjsufZRAwDFiPzx8pxjyv-z9tU7nkSy-BWQI63BabWMOKVWBUAe3Mv-znCo4gGGIgscSuwA5HSkIt16Pv9fh8CNZswMCXILf6041C-lSRXlHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jG7_krJUwxhmHLfRqeYzVhQI5saXpHa2qNRkaosR1uZq0XuPJu9EJeYymsOJK1Zh3jZUNu56vhI4d4g-NbIH4dXosXtGW9pgPSHN2Giiwdsb24xqEnoJ6tLEZwUSwOPXueGSdUjFNPmvrMwFWXNhPochcaSOIu4VX2W0nUbSIUkngcPl12f9vfi2cj2naUiN0TmpmltzRqL4patywI4v190JiqFbEi9-Ef8nVfy4oFnE5h-DPHsA97z3skLLNHsEZxxrzRxTdpReiFrL4um2ItXVsC1j5NaZa91BlTbUIttAMcRpcE_Rr5bvyuRWqvmtMQ878Enk5KSyPB3iACv2uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jG7_krJUwxhmHLfRqeYzVhQI5saXpHa2qNRkaosR1uZq0XuPJu9EJeYymsOJK1Zh3jZUNu56vhI4d4g-NbIH4dXosXtGW9pgPSHN2Giiwdsb24xqEnoJ6tLEZwUSwOPXueGSdUjFNPmvrMwFWXNhPochcaSOIu4VX2W0nUbSIUkngcPl12f9vfi2cj2naUiN0TmpmltzRqL4patywI4v190JiqFbEi9-Ef8nVfy4oFnE5h-DPHsA97z3skLLNHsEZxxrzRxTdpReiFrL4um2ItXVsC1j5NaZa91BlTbUIttAMcRpcE_Rr5bvyuRWqvmtMQ878Enk5KSyPB3iACv2uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Rls82BPG2iPz1dCwmIRyiYua_ylDu3qVL6sJne-13zR0wlu_ET4caH7dDr6rHjkPlz7TtIT7smpvDqVERr_TdVKdZ8LfY5aacndrc0cDaOaES2ieLmhCJPZMYpJNd_n4uaNEAMoN0GPzprr0Z6E01pb3DykWFPKoD-kz5hjTbPbRWDtFucOYSXYjFMCMsfEnCxktXz04Lha8n_Ua71qbAhbQ5lVb00u0L_q46WYsoXLwPoFU6YhIArbL-QqGiOZ-wWVEmGnoEb1K7ZrB8hngKF15GrIvA96ImKue8XPW58mo05uw3kdXVwgAal_apwI8POh4CWK1WXzpCvO-HQLNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Rls82BPG2iPz1dCwmIRyiYua_ylDu3qVL6sJne-13zR0wlu_ET4caH7dDr6rHjkPlz7TtIT7smpvDqVERr_TdVKdZ8LfY5aacndrc0cDaOaES2ieLmhCJPZMYpJNd_n4uaNEAMoN0GPzprr0Z6E01pb3DykWFPKoD-kz5hjTbPbRWDtFucOYSXYjFMCMsfEnCxktXz04Lha8n_Ua71qbAhbQ5lVb00u0L_q46WYsoXLwPoFU6YhIArbL-QqGiOZ-wWVEmGnoEb1K7ZrB8hngKF15GrIvA96ImKue8XPW58mo05uw3kdXVwgAal_apwI8POh4CWK1WXzpCvO-HQLNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaYauJPGdhTKToXoQWKinEyVQ8tLEd90vSeI6HFyNcScWGzyCd427O2JTJZXwWZTW0ysgyOcVqPUKzCzRlMqN2Oyhmsxc0Y_cXX2R9M-M9GszqIiX65wPa2IXQoyV2FutvwYSvjfGXkKR2eyd0SuLclGXBVAvjIvfrduzVEL_Y7NMgqaNFnGWTMsTgTZrgk0_yXeb-jVEjKxwKfQqJ03GZMIMyipjRwbtN8DVvoBoHx4yO0F7beO6Z1GCgeJis4UiMOdhftX1S7NLlErKuSqgoKdOrZLv1e7zFM8q2TOFTUfHdBkMo1UqT4XFQD0wIhYMRNCfPscIW9Sgettdninyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=OCNw1fCrlj6F1QS3i26ETevxZdGhuFMSMVVw6AXrIj7PxU4yKm-cl5p2Ltv1uziKz7Iz8Mnkr7kCucxOkkBodfLX7l3ZHxetX9FF7gwGJvoMTCtJQw2zj0trCIFPSTXfXdaMQZT6fB04_RGAsBONpLlrqMEz1kpNgGylx53pOlhPPSc6iPI--lQ9_FTdNFsBsvfLcOoTmoZQwN8LEktRVRsRZc4pih4MBLtiwyC7Hgx6d-N1rVRJULTfj9QYJGAzweRXG3m1cX78rb3l8mSI3L7pta-GNwjHuPStj4F9qjzeijWxZh-tRnpEJIq-KfmtrpkIbvN2UMS6BX1nalIgJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=OCNw1fCrlj6F1QS3i26ETevxZdGhuFMSMVVw6AXrIj7PxU4yKm-cl5p2Ltv1uziKz7Iz8Mnkr7kCucxOkkBodfLX7l3ZHxetX9FF7gwGJvoMTCtJQw2zj0trCIFPSTXfXdaMQZT6fB04_RGAsBONpLlrqMEz1kpNgGylx53pOlhPPSc6iPI--lQ9_FTdNFsBsvfLcOoTmoZQwN8LEktRVRsRZc4pih4MBLtiwyC7Hgx6d-N1rVRJULTfj9QYJGAzweRXG3m1cX78rb3l8mSI3L7pta-GNwjHuPStj4F9qjzeijWxZh-tRnpEJIq-KfmtrpkIbvN2UMS6BX1nalIgJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=ZcaGB4J2P5qvjp_zi-Xryf5fQa5Ch3ML5Q5_27ZLoy0EniKIFBGLrzFu0ErZgAMzkHT5jmKLr3idvwIiei4iT6dbk523z8pqaNXbfIzqNbvu94PO3VhEOOaUC3J2pIf-9VP758gjwf7nOnhKVH2i7aNzGdAvIiQ9OO0sQA-nN3sDJsoQ9T1YQFyohUWMm4GXBvQj6hou2tI5x64rsByRxRKBS-KuzSJSY6Xyw2G00L8mX-x6uy2bz2ZW7lQWIVhJXXB9LpAkaEGAqGsBaSNc0SWvX1VGMTA9X5cVFZmZLOnGlnIuwbdHAJgm2653oxYLmUVju4zZuENaDTwFQfHa2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=ZcaGB4J2P5qvjp_zi-Xryf5fQa5Ch3ML5Q5_27ZLoy0EniKIFBGLrzFu0ErZgAMzkHT5jmKLr3idvwIiei4iT6dbk523z8pqaNXbfIzqNbvu94PO3VhEOOaUC3J2pIf-9VP758gjwf7nOnhKVH2i7aNzGdAvIiQ9OO0sQA-nN3sDJsoQ9T1YQFyohUWMm4GXBvQj6hou2tI5x64rsByRxRKBS-KuzSJSY6Xyw2G00L8mX-x6uy2bz2ZW7lQWIVhJXXB9LpAkaEGAqGsBaSNc0SWvX1VGMTA9X5cVFZmZLOnGlnIuwbdHAJgm2653oxYLmUVju4zZuENaDTwFQfHa2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=PaKKaIuwfPala-MvmkqTK1rkpTamYZB8oHAPmyfklxM-258wx3WzXqMsCnPYuHtv_oqpNIMwrR_DOLOVtpqxuuqmAObig1xQTx2s0IbLByhm3nFSogDcblcpKXWlgwn6qfwpmQjSFWXehw_3jrHMn1Arl0X25YNBBPOmw0mAfYoXjMPBK7NSQDqtiuKc1OMKMIQG0kGC-I3z1l2QfFcsS7dsAlbE9amdDuiwuQEDTbSaEnqS3tl-f2L9cyEFMMlpsYO-fb8gnlrKd15gXA0NLgbhFhDM_Db4zNvZonaeXKck-lYqvFH-a5ioHPlbuM2kza1objI1A9QsBnn7Zl4Wkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=PaKKaIuwfPala-MvmkqTK1rkpTamYZB8oHAPmyfklxM-258wx3WzXqMsCnPYuHtv_oqpNIMwrR_DOLOVtpqxuuqmAObig1xQTx2s0IbLByhm3nFSogDcblcpKXWlgwn6qfwpmQjSFWXehw_3jrHMn1Arl0X25YNBBPOmw0mAfYoXjMPBK7NSQDqtiuKc1OMKMIQG0kGC-I3z1l2QfFcsS7dsAlbE9amdDuiwuQEDTbSaEnqS3tl-f2L9cyEFMMlpsYO-fb8gnlrKd15gXA0NLgbhFhDM_Db4zNvZonaeXKck-lYqvFH-a5ioHPlbuM2kza1objI1A9QsBnn7Zl4Wkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Rx4MLvkFBEcRTneBo1b_-NcEM57KPsn2rbLnkfPupZGNXbIWBdSiIf4LsQIl52dttwz18YUjhD5pXFp0PBO81kGKiSaSKM0cwH40_swzqX_m26z8lUEugqcfTHf-cbvTjGfZm-sx32rOQ4yLMuFdNx1pFuykXPiwOlFnYoBokx1Ut9JejX70TtRT3-txK6nXoeqjH4QufdE4yHMV5XS-c_SrQwMj82lPL6HwXV-7ERqNVPQf0pbd1Babt_tNpPpErK_aA2TozzsHO88COkIeEjy-X6i_9kBNogLpPUFCguQRU-M4MAxPtCG-zazunGUcBUsKtInEYEyn0oyNyVAsHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Rx4MLvkFBEcRTneBo1b_-NcEM57KPsn2rbLnkfPupZGNXbIWBdSiIf4LsQIl52dttwz18YUjhD5pXFp0PBO81kGKiSaSKM0cwH40_swzqX_m26z8lUEugqcfTHf-cbvTjGfZm-sx32rOQ4yLMuFdNx1pFuykXPiwOlFnYoBokx1Ut9JejX70TtRT3-txK6nXoeqjH4QufdE4yHMV5XS-c_SrQwMj82lPL6HwXV-7ERqNVPQf0pbd1Babt_tNpPpErK_aA2TozzsHO88COkIeEjy-X6i_9kBNogLpPUFCguQRU-M4MAxPtCG-zazunGUcBUsKtInEYEyn0oyNyVAsHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhLRdJt_SoNEWmdZR0EBKtJXWYO8h_61bL5Ds9OuAb-h4WeqLs2p6uHCyLsS972Ai2tDCxsODqteRW-v2TDbeQst-oBRSFjzrFourMMXx79Kd_0iJuYPJUqpSJ77BR_stWsJK-678g8UnXHHVru8HOagv1ucl4Ic1mJ_JNzvZ4-3CLLU2BnyeohTWENEcHXXL-LpWuT4LwJcDedP_B9Njn0yG5qtJRQ8BVVYOuXJrcP57ZLd5acdO-RDm45SKEq1N1AUWRIDnmRcRVFl074RKrxBiH7aps0BGqqzohw39Bt8OsG8Yu2cMpR7ToTBfHD8tnEFIfRFToq49rr3U-AXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qJDW3ijL-EADTKjVkptjbrxjvuYAM6NrijyH81V-LEiY1ZeIEZxfZDNnkwkHeysDTv-5Ap1KoWS3l9-WVvXkA4usETYByqGxwj2i04CtpIDxoOKvNu8nh4ST39685Te5ZiIllsHeubXn2jX93Yz7u36pbzo1txDtVZGzFF5RrGs8-4Xq7G0ikZjfuW9mqpD343LJiTslubiseJhjZVOCrINLllQ3A5-r0e6szlhw5piOVhNV-Y3RnygW61S6uYergyeOIbL7iX6xKlY0SeLKfaUubgBPBKtaCiy0uIy1-8o0zSvB88YGnPEo4_oZA8Tp6HUyeJB6qp862ZpMwox1izzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qJDW3ijL-EADTKjVkptjbrxjvuYAM6NrijyH81V-LEiY1ZeIEZxfZDNnkwkHeysDTv-5Ap1KoWS3l9-WVvXkA4usETYByqGxwj2i04CtpIDxoOKvNu8nh4ST39685Te5ZiIllsHeubXn2jX93Yz7u36pbzo1txDtVZGzFF5RrGs8-4Xq7G0ikZjfuW9mqpD343LJiTslubiseJhjZVOCrINLllQ3A5-r0e6szlhw5piOVhNV-Y3RnygW61S6uYergyeOIbL7iX6xKlY0SeLKfaUubgBPBKtaCiy0uIy1-8o0zSvB88YGnPEo4_oZA8Tp6HUyeJB6qp862ZpMwox1izzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Krr1suwTeJxBXWgalVX5Fozbjw-857CZcXIJmjgOKWNocsPyMsE7VYzdmgnXBEyDS3IHJEoL56dnLzcmLTLbkZn5yy2ZLTG_Hnqbp8VlcURLCPuPlFIDf-fQGfADbFocQf8XCU9mBOwQH_4PZgUoeozYHjyVg9hH4m1N_9Q6OpxHRLRw_uDJZD8binXMu_mTZ6BpouTFmWj922sjvGujrJSLwl6_Alp959KZVqpQwixnkoUCwdfWACceIL5puNL8gJ7quztYsLFwihLqBd_N2WEcdzgWXolUAAkdwI929Rb1Ktpk1yV3tcEhn1YTwynfXf_00q-NEzJvUFwnvU2mAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Krr1suwTeJxBXWgalVX5Fozbjw-857CZcXIJmjgOKWNocsPyMsE7VYzdmgnXBEyDS3IHJEoL56dnLzcmLTLbkZn5yy2ZLTG_Hnqbp8VlcURLCPuPlFIDf-fQGfADbFocQf8XCU9mBOwQH_4PZgUoeozYHjyVg9hH4m1N_9Q6OpxHRLRw_uDJZD8binXMu_mTZ6BpouTFmWj922sjvGujrJSLwl6_Alp959KZVqpQwixnkoUCwdfWACceIL5puNL8gJ7quztYsLFwihLqBd_N2WEcdzgWXolUAAkdwI929Rb1Ktpk1yV3tcEhn1YTwynfXf_00q-NEzJvUFwnvU2mAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCvur7gqGhDbgM3TKCyPWZba0KXa_zIoFkWBUXRCFnVizoKbpkKwKWkjm8AwjBAwZmu9wuIXz-_AYPzSgfwpIaLKT4y_XZxjytvYqxxSkK8gkMyuW25mY-hFUAOdCkt1fMuqKH4UMKKxPqufJbbW8W7RcIuEuPbdRVJ4SIIdBwV1hxcGRPKM2e0ufh6MIrOzbisn4bjqQB94dXHC9oXCbWOBQyIaQFJdvi4LOzWBBBXOROsR-srezpnAyet6rvtdUGMSN1-cN_xrsC---dio6HdhEEc09LILPJTwaWsUXJzCmcYILKN12QpTljKLwJBR8p2kErmATQBVP1A42UPCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdSaHxqw8Ul-c9BnUyYEWZhc3vZdH-bUIgAS5EO3YIz5_eIIJ27XCLRDALnG-3G7ZjZrcBb0kRM3UII4WeE1B6XIXMA6dGHZEGQKzGgAnOX_KS2h9c1Y98bHvBnJflrn8tUQWNA8wnw_fqDRQd3N5LABkZXc5N7MvMUJZblXIC3Bfes5NBh1f06xAAzIg2Nt15RHskYrkq5SF9_6i8OER8QUjfoivMFF3J-cvZEEtAcmSKKBW8wqX-_xxag1ZtHRsYjyIWafCzmXnCiN8BkWCQg_4DW5HURd0JqmRteN2KvHS4_uS920ethFP9i92AIBsGmECOoxsmBvDcV-82KJIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=GbCDERHb15DNyYnMsDLsLn4yEEIbihiwh3Qn7weK4Z2H_3WIzBH6oBFyu5dRuCbuIwlREg5obyL3_r4c3ALGz4P08KuGaeSNfVw7pXsVfvxWWihHwpwZCLWoh-46cbNnNdmR9ft_UCPTTrV_TRuPzLzbUcbAOLxeH9vfkAEI4InngG2zTckX5urWtEpBtZ7omvSmmjhm9dD6rSD9w4h_0IkZ-YliKCZ18wvJ_uhTFmhrbidY4cUkI6_M6zNe7Y7GaolikdrGxtBcWQlJt9JCU7u0z64O34jwBWEVF1xv-Zh3UTfqK0D8_ksVn-_TPLA4ZL_fB40mBZ5gyaPQj2xAkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=GbCDERHb15DNyYnMsDLsLn4yEEIbihiwh3Qn7weK4Z2H_3WIzBH6oBFyu5dRuCbuIwlREg5obyL3_r4c3ALGz4P08KuGaeSNfVw7pXsVfvxWWihHwpwZCLWoh-46cbNnNdmR9ft_UCPTTrV_TRuPzLzbUcbAOLxeH9vfkAEI4InngG2zTckX5urWtEpBtZ7omvSmmjhm9dD6rSD9w4h_0IkZ-YliKCZ18wvJ_uhTFmhrbidY4cUkI6_M6zNe7Y7GaolikdrGxtBcWQlJt9JCU7u0z64O34jwBWEVF1xv-Zh3UTfqK0D8_ksVn-_TPLA4ZL_fB40mBZ5gyaPQj2xAkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trftaCC_yl_doOsWQwS5SZTgyr-pQ1zQmC80mxMR3y-KwpHIJLRth5_BnNYIalM0sp2zCCBes5Wsv9aIeT7HNNsFispe-7HmAlEvsARiUfJolHQdU8Y-JSz9_4toBL-TuGGpwx-O1fAX77p0rj12PI4VrTyz11SSH1lAB8fzc3NseAE8OfbJ8g-aMsGYJUbffPhnT9pl4JLBtE23M06XouUgIryNqEHW5rfIEsMhMD_lsRMmqNnOEuTYwtD-gaoFCftjZIdJoVfEZCRyVD_OUJC59qj4CBm_kaWv9ybp9q1ZrFxZ2XAB_VKcYCE5gLhg6hUuT1VmAPhw3JonJOmyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NioGghf-LfdSLavDODfeWFCkQOJcxD-j1z5HDLv8t2kOqtcPs1SZ2fhYBfNhwhB6oWn0vP8J_Zcciee6bBwJ-UR9Aejgvp0KA061-XAVepM0wWCJKr2DKxVWKdmWe0ko_QsV8bXIVN8u0ruTHNWGqrXNlLxNuzgKPSfCYwaB8MYNb8FiKz8ZNTlRqe8c31wdNzFo4acfhVtSHIBDDGKuUEdz2_tTGydu6lv-ZW5110hwgARCB8SmiK8DFetl-kkjd5E_VbO8Fhw8IoO9BRTh-XBG4cLg_hqTiUlY283KChuXIT7RrceOQF3wL9oIhdzmo6Ehy9PTk-Gxi4jSjNpjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8DBsHXCvmD0CwcgAVDhjFOCaDA-B8Zmqz0g-RIIAb9CcR_CpSCz3YYZv7cPDKDWqtMxwaawQP9uocoBMa8Nqnap9Yebh7EiKBHY64aBzJBf4JjPl7xxZAgQmA4RgkU7RntsuBkW4VgSS1T_iV4CZ6MCVkqjmAO-WcHpArTBO3ZfQEhgXKR22E8vA-Zat13G94Cp7g61HkKbo4VYXzWqpI3ZyxSVI59P4aJIfHzKJTSi220-Gi0QNROp-OhTArSreD7isAkdclKZI-m4KOuRzzu4TcP_96u9q0ACfKqzAVspHZ8Sx-G76W-Pb_TFeUJyG2IhbHokUNbPlIQ7Mh-xAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=H2dW5Q1ReBijt_PzQfLH54FORgjM2BGh90eSLayvqFBLlux_XSkGHa75sLwN3WsraGxNwcfe7gfm7kg8hmrIFqSdgSw4xCIRCEBmBDYi4EQ_e78oub7IYSCBlcEGCfWFlv4C33a7mMVclUviZxrmpvYzC1GHFaPxLsDCaoK7oPJb6u3GpMD_eHlDaKewWeczplj7xvfvXjGdj1eE6uzGimpOAsm3UTa8sbx01gjl2WICWOuDaPJFxrw5mw2Blg5njpBAmVlHyh0-EFmXwF4KqFHRaFeQ35yrrkJnrg_YZUQEwpWrrpWyhVOzYiFUzbWpLCwFxkXbsLmJG3VXVoFrFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=H2dW5Q1ReBijt_PzQfLH54FORgjM2BGh90eSLayvqFBLlux_XSkGHa75sLwN3WsraGxNwcfe7gfm7kg8hmrIFqSdgSw4xCIRCEBmBDYi4EQ_e78oub7IYSCBlcEGCfWFlv4C33a7mMVclUviZxrmpvYzC1GHFaPxLsDCaoK7oPJb6u3GpMD_eHlDaKewWeczplj7xvfvXjGdj1eE6uzGimpOAsm3UTa8sbx01gjl2WICWOuDaPJFxrw5mw2Blg5njpBAmVlHyh0-EFmXwF4KqFHRaFeQ35yrrkJnrg_YZUQEwpWrrpWyhVOzYiFUzbWpLCwFxkXbsLmJG3VXVoFrFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=sy6RRaI2mgMZBs4UJTUvWYky4ZtNfHUZ1CL6S4dbJ1ssPwb2eiyqoPW2rxSPOq4SBoX0wkBClLXuZq8PO07Q_h1-wcZ4FNNfJUmMNvOKp4FwBbGPs1OY0R4aOn1IED7b22vDoYiiYi07tdvVY6NZmdazyyMGXSZ2nIUS13AvBGQgsdkExOPpi_iJ2MWlXJrq4MGBa3JUVer7GSKPw7xC7i_J1RXtu6Uwgt7JvwOI7N6bxAxDR30MQzfNv6b0ir4PlXEUtjoHv8wFOQqSbAKXLTVQzYJ3FnDBuM_sEMbdmfO6tMEIPvelntsMoQxmbHyIbwSOPHt75dnebRyNJY5J9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=sy6RRaI2mgMZBs4UJTUvWYky4ZtNfHUZ1CL6S4dbJ1ssPwb2eiyqoPW2rxSPOq4SBoX0wkBClLXuZq8PO07Q_h1-wcZ4FNNfJUmMNvOKp4FwBbGPs1OY0R4aOn1IED7b22vDoYiiYi07tdvVY6NZmdazyyMGXSZ2nIUS13AvBGQgsdkExOPpi_iJ2MWlXJrq4MGBa3JUVer7GSKPw7xC7i_J1RXtu6Uwgt7JvwOI7N6bxAxDR30MQzfNv6b0ir4PlXEUtjoHv8wFOQqSbAKXLTVQzYJ3FnDBuM_sEMbdmfO6tMEIPvelntsMoQxmbHyIbwSOPHt75dnebRyNJY5J9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=jHXaBekiKsheVWKH0XZ5gmnoS9aFer9LNjeAOnnS-0AhokXEHR2q5E7Ct33sWO2NGdaqJmnXayT2-MqBWin18Ict6a-GlJjrI7vjXEFQYROgUrk9YjN41EImNaxDoEe1zVtRCj53PlFveVq1z7NF20QR-4ri1sj3dt0FH0pflkMxoouIsHDh4CmYg-KxUbIGwTCw1bWMFOUPpyoVZ1oAr5o9AATG9zeHIO28CyEqivEBCyR3x0Ie_daZNZE2NyNtnDgvG35ZDbhYk3Qo8Ctr5va0xQnkayZdwHx2zLeLV7RX-i_lA191Av3nNlrJSZRUTg867NPqvQyolusTkDhEWFYpG4mu_GgdsR-c6kI3bfuofMCaHPc988UYB_eTv4xkJAdSQ77FOzvG9Z2vNHRNKnVuIe2qTnLdp2ijQ_ArhcS5-_gmQUR7rlzhcKNAAQU8yizZATms3KS8REC8TOzdN6Pu-4YOfReUCts7XTiZoOY9FLFQluqO3-co-FQvaxJa84eUK4mCy_BaNg9zHWJm4gUTaeG4xDdDkTi5uTzINdJ1iFO0hQ6BGn7ZokiyulbM54Zztv2yDPE52vezlChJyNUrXZLyu8s3SuDO8gJ23e39OcRPvKp_Px0B8Xt-92O_CbRMzRv-OVLNJzCeTnA3k2SulITXyUp_wlyAIGcKR0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=jHXaBekiKsheVWKH0XZ5gmnoS9aFer9LNjeAOnnS-0AhokXEHR2q5E7Ct33sWO2NGdaqJmnXayT2-MqBWin18Ict6a-GlJjrI7vjXEFQYROgUrk9YjN41EImNaxDoEe1zVtRCj53PlFveVq1z7NF20QR-4ri1sj3dt0FH0pflkMxoouIsHDh4CmYg-KxUbIGwTCw1bWMFOUPpyoVZ1oAr5o9AATG9zeHIO28CyEqivEBCyR3x0Ie_daZNZE2NyNtnDgvG35ZDbhYk3Qo8Ctr5va0xQnkayZdwHx2zLeLV7RX-i_lA191Av3nNlrJSZRUTg867NPqvQyolusTkDhEWFYpG4mu_GgdsR-c6kI3bfuofMCaHPc988UYB_eTv4xkJAdSQ77FOzvG9Z2vNHRNKnVuIe2qTnLdp2ijQ_ArhcS5-_gmQUR7rlzhcKNAAQU8yizZATms3KS8REC8TOzdN6Pu-4YOfReUCts7XTiZoOY9FLFQluqO3-co-FQvaxJa84eUK4mCy_BaNg9zHWJm4gUTaeG4xDdDkTi5uTzINdJ1iFO0hQ6BGn7ZokiyulbM54Zztv2yDPE52vezlChJyNUrXZLyu8s3SuDO8gJ23e39OcRPvKp_Px0B8Xt-92O_CbRMzRv-OVLNJzCeTnA3k2SulITXyUp_wlyAIGcKR0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=sZpPN2KYhF82YAip79mRqgF9ACM8LVxWapj3aAr6KKvrhHHroGZ0C6ndpH_eJfdXQ4s4p4LQhni5jiYfRgQOFrhGW9fYZC1wU8K-6EqnnyIpdXI4w7sriwuxnDhMnKaGLTLs7TuyWVLTSJwuFY2yr3QO1nu-i-mIK7WrtRLj00Xck3O24MV7Hbc-XGYogk7q3GIC-J4z3QdjWtTZNmj7hNMCBmSxssXeF6b_3bSr_eVAgLXDMR_Q5zorR8jqmhs_2cYklM-BfFMhyZTln7RK5DsvNbyggTAq9uFbwYGFV7ud-I3c4oQjM7BWn8nSc0dyoEJg_s6-lHwHu1Pcio_TR0zfLuhtGyHB6faEqso1jkcl9O84udsUqBVgAWGuHnOsWn0fXdJ5-WWh820QYNvOdUe8_-CxrCOxhJNBNhtKoEURBjKXIdmxlW0N62645P_o5An1mvwUSizZSOAy3l0OaHPOvkuW-YdSTPZaHhrEID3aDa-ULJ0AuLSvPxmG0xyjjJ6IsueUwi-OtYKmZUb_QoCwUVftYhEWg5eObFkQJy2pgHXT9GTpw94Dy2ETVQrJWYBb3tAit3VZEJV9UdIeIB0OvrQlwLdF12ms9SIz8lQXPA_ExFBChf68csxVFUeP42i1zvgDttNQaQdxh7xtDzY2HnWWKFBjWsubQRmhfdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=sZpPN2KYhF82YAip79mRqgF9ACM8LVxWapj3aAr6KKvrhHHroGZ0C6ndpH_eJfdXQ4s4p4LQhni5jiYfRgQOFrhGW9fYZC1wU8K-6EqnnyIpdXI4w7sriwuxnDhMnKaGLTLs7TuyWVLTSJwuFY2yr3QO1nu-i-mIK7WrtRLj00Xck3O24MV7Hbc-XGYogk7q3GIC-J4z3QdjWtTZNmj7hNMCBmSxssXeF6b_3bSr_eVAgLXDMR_Q5zorR8jqmhs_2cYklM-BfFMhyZTln7RK5DsvNbyggTAq9uFbwYGFV7ud-I3c4oQjM7BWn8nSc0dyoEJg_s6-lHwHu1Pcio_TR0zfLuhtGyHB6faEqso1jkcl9O84udsUqBVgAWGuHnOsWn0fXdJ5-WWh820QYNvOdUe8_-CxrCOxhJNBNhtKoEURBjKXIdmxlW0N62645P_o5An1mvwUSizZSOAy3l0OaHPOvkuW-YdSTPZaHhrEID3aDa-ULJ0AuLSvPxmG0xyjjJ6IsueUwi-OtYKmZUb_QoCwUVftYhEWg5eObFkQJy2pgHXT9GTpw94Dy2ETVQrJWYBb3tAit3VZEJV9UdIeIB0OvrQlwLdF12ms9SIz8lQXPA_ExFBChf68csxVFUeP42i1zvgDttNQaQdxh7xtDzY2HnWWKFBjWsubQRmhfdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=DJ2zKTLpmy1khQ7H9xp0Ly_tu7d0aXyj5sBBsyfGW45U83hzAZblz4uFZIA4vHki6iukJXmArSbkWy3FDFj9Cm_p4tC1ehjtMcD8BXHwTfbLKxgMyqdymT8xM2l41DOwPYT_lu5XZCpL5by57degzbPa6nEeCxnIDQp32v7nsR1KrGsmjU8PMQ_kCMEJFUlkwCaObyrNcOK89MRIk721xFKWOIvcuf_sAf8HnEal7fHZWQXU_VlkCNIeAWYI4WOZHiCIQzABYaLTnxH6--Q88JPMPLo7CfYihtiJU0BBjLY-y_5YHLYhSIr-gipJhbH3-914Lc0HkvAQJ2CvhDv6yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=DJ2zKTLpmy1khQ7H9xp0Ly_tu7d0aXyj5sBBsyfGW45U83hzAZblz4uFZIA4vHki6iukJXmArSbkWy3FDFj9Cm_p4tC1ehjtMcD8BXHwTfbLKxgMyqdymT8xM2l41DOwPYT_lu5XZCpL5by57degzbPa6nEeCxnIDQp32v7nsR1KrGsmjU8PMQ_kCMEJFUlkwCaObyrNcOK89MRIk721xFKWOIvcuf_sAf8HnEal7fHZWQXU_VlkCNIeAWYI4WOZHiCIQzABYaLTnxH6--Q88JPMPLo7CfYihtiJU0BBjLY-y_5YHLYhSIr-gipJhbH3-914Lc0HkvAQJ2CvhDv6yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m02navOY-SIi6CA7Lpt5rImJu-cbXaQTxsvv0Xrhf3M1UHa_0Uis2NScCBm2C6rRmLPb7Dm7pnb_jDzQjCKpKpOkBwM1kbo0mwiWOUNtlgydGU6O9Fm1rL5bkj8ZnaTZ0FnECBEj-jZ7_0vMtSQSJo5UoY1kUA2YbcbHAq0QXkXw0FcFtZDZDPTsJikLnGC5MeVhc5HNDFq0Z3JlmsnyJHnNvMJLm9QZck8V1WTO_ek5dm_pzy89okHqUcXlMgrrxebOrfjhY_UbyrqL5C2eWaxECuFhFMto7gMP1UiQWaQGbxIxfc0FHms2R7v3htQSCzAAyu0FquUBLncmga-0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=lWP4aXBBLicWk-1wa1W18xDk50sDnB2BkgRnRXo4FhUGcAS26_Q9kUlKP5LabUtCPmxv_giEvJm03fX8aKlmxL9p0XUdTpIwgVdqF1ANbQ6WlMJgqjmw-1LEIeQHgJgF1PRE-8TiEZ4smUyX-1kzAI4xqq19j5k7xTg9BdxAH3DzZ5cP7Pdh3wgU9iZcTLYNNTvKmyYJRy5R8U_8ud37lkWQlqgoPNiuN8_c19qwcmKaKE35CTFpyrQmhukVYThUll0GokdGc0hX8Z7Jsz6BKVMLhpO8ZG8GoOx1gRYxD6i80ZoUSEy_2k2HecZGz2co8kJkgejymRL0yu51lQFqMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=lWP4aXBBLicWk-1wa1W18xDk50sDnB2BkgRnRXo4FhUGcAS26_Q9kUlKP5LabUtCPmxv_giEvJm03fX8aKlmxL9p0XUdTpIwgVdqF1ANbQ6WlMJgqjmw-1LEIeQHgJgF1PRE-8TiEZ4smUyX-1kzAI4xqq19j5k7xTg9BdxAH3DzZ5cP7Pdh3wgU9iZcTLYNNTvKmyYJRy5R8U_8ud37lkWQlqgoPNiuN8_c19qwcmKaKE35CTFpyrQmhukVYThUll0GokdGc0hX8Z7Jsz6BKVMLhpO8ZG8GoOx1gRYxD6i80ZoUSEy_2k2HecZGz2co8kJkgejymRL0yu51lQFqMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=TyyIPSSzkp5igeMMzMpFeorPC_ZQ9ydRCp2a8WXFzVbGInSYSQQ_VsG9qoV8A6hvwQha2T98kl6GtCQD0Db3bAMiOLiF8Z6CU3RYr7G6_TzYUx5TgIg8a5LOdLvydLLAt3PnrFfxajzdge5wHrhr1yegEomD6XSSBT_q83fD-PoWUS3hGJ_BNfb8OK1PqI6doKI2JwqhhpQOo_tyw543zDBUA26jyo4P7jmiHKu5G1dmyl9BABBSbJazWqz2O_aiK7FgCnhBEmPMCOdl9RuoL772S3Qvx8EelCyriUIR9Pi40dzsxgTs8GuApFfqDjqyc1FLiHGO00KUjiiECpYDEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=TyyIPSSzkp5igeMMzMpFeorPC_ZQ9ydRCp2a8WXFzVbGInSYSQQ_VsG9qoV8A6hvwQha2T98kl6GtCQD0Db3bAMiOLiF8Z6CU3RYr7G6_TzYUx5TgIg8a5LOdLvydLLAt3PnrFfxajzdge5wHrhr1yegEomD6XSSBT_q83fD-PoWUS3hGJ_BNfb8OK1PqI6doKI2JwqhhpQOo_tyw543zDBUA26jyo4P7jmiHKu5G1dmyl9BABBSbJazWqz2O_aiK7FgCnhBEmPMCOdl9RuoL772S3Qvx8EelCyriUIR9Pi40dzsxgTs8GuApFfqDjqyc1FLiHGO00KUjiiECpYDEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQsmFL-JvytYmjhGtcpAPuhQcFAnMLbRqEE5Qh4UhyHY2udYw0aQztkuzVW8T5BuII2AZqkibvH8zr7KzHB6hwQb3AJB3twhCjpa_AWQ-KYLyurP65QAObj0F8OOr8_m7u3arFfYKzY8qTTLGxpZJhTYt8ZOb0JWOBudJqAyAqITLlaOI_w79Qy-eFAivtpHuyl32tKmot8ziMOU0sxeYj3S5XUIbd8wODdu0d920Dd22E08IuajnNWrLYdJ1SuCEqtaUC4pbpxuU7rUlwb-ggdqKrXDIhZzRJ1h3aBeKIB-9SseV1Q-wbJnAxboRD-PLDs8u4eJ_GA6NZXKAh0jZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BODdyPr9xgDsvlWXInoMp3pDJTod9YuDp8t5uh6V_gVrs-_t_Audwrq_pawFchXWjFuiRpCi_gP8xpQZQqbNz_vGcqH3m8P_U2xA0oxa9HCb7-Bkis6TGXrMnPlEwowa115ItIFniC-9ArAwj2_1wR3pAXot2OzRrkp-OqPbFWhtKPonDqeiQBoe6Di9MQvlLo-OldbYOrtbSsVLMTMU_z2Qsxk_Xr9sWXBOp7j_BdpmXB6n1Kr50i-xkc3aHhJ0Z2K_b3TD20ZGU04UMXaO6g4424jWFiSzpC8rYdoBH3L2xRzpl9psWrLYje_dUPAQlSdKrZPTqhtdTgalhyNdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYbE5R40I-bFKVMAB8hQf8hCYrgm9y7slJxGBstXaRnK4cCQzEsrTKKdm9rtYbzOnErxy1Tgnm0v_SDoKV-tilHWVEP3FZOxqEl9DjjxA81xqOhArIlsyQyAPYRapp-AXLTlt82cn8mje6orTo5x3mEukOZ0WlFhjOEWvdQdySlym3768Rp7Y4RkIMl_UxIAvp2MlhRXZj-zlwa6O5YMFwbza-h1BypYhQcba0IlvRx6K0rQB3vZcQdCw1VSPcV8Cfbx75KyJqUPdGaKUEFCJdyskTWG2Y75woEY-lnRE0awolMe3-Ow6jS2nzxNu00CTXFNR4p0SsoVqj9ABO8-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6wmfz_4Hm1WVuArDsY-zo-fbxp_WGn9LbJ6iZ9F1eZbE6xD0CcH7vOkuHWRkdBJBThImyJAEpLx8mZQk1rTPaytp2QraZ_YW9rXPCr8TCTlw0wYkLQwwIcr0Dut61KVybsmZWCJFX5LRwJ8s46_MuorBgzkz2mPXV6234eZyPqqz_JEGtH_Camwgiw_41zw7QB9QPYXBwdarZvNZ10YRB0a-zj3NsOECZgMxYGA9L9AeqGlCXOT_H6n_r1TOb8WbRrOor8pOED8jRpxCXJQbCKeSGhJYvqurBTtx4rI4lZMzyynMLzJyq-YuLUbv5gzwDHHnU4930if2ewSxbXCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFfwBe5vPSITIiw2FYSWFEr5DDgNz5Rj_xJDbQgkxr6bq98Tptb9ZzJo7xKdTPp_vElu4mvaJIX5Gu9P5UwfNIANhfx_4-FTWx4elok_PzoDn00ybYjIkfo6UbrbvxAw2erbZr0zla2Gtpp6Jdquw0uSH9G6HuiJHwN2aa9sHqu9DLttsmT_2ThsaRBFnM5ND3OEA5bFuMBBsTKakzTWEFNyVf3wQGVbBrAMd50rxpkjtA_45yGBU96Y3x7ckzKKoAr8DDdzw8akoUbM0rlB0Vi5qGmkRfwSGHY72zWeuy78apmUaAW4R0OMiH3GwP9u-UuS0rbUOfDALtXbrtsoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eS73ZhQPOtegA3YEGvKzHSaI0lbyCzfqqAUredfVtaH6Op3wt6e1C8minJkos0ECEJicqV79INsuCX1n-U0-gQ9fqF0K58TApC0RTbAmhL-yqIjfWsaFJ47v-Fz3JV2c8DNEJI0aqihbZO3sK2h5cAUoXsK01ij_z52C9GgF7Mr4VZjej2b-X8GcnHdniyXpcMiFMGuQwMkn6BbTZ479PirM5i6B9HRsID6CUdwtyVdAaJvGFsTZRmAhCjsNjpPHs-KFwYBvFGgRGzu5EEKbJk1T960kapniU3H4Jxse9bkg0740IMi9VJZXrdMyvh1VDRbTBT3WGQh7P38vbUE_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXTYCZ9B6Rpty8lvdkXp7s6ITxKspDmI1dSSj0kA-OIcnivtN9sDmjxtj5A6wg7A1Oqb9h85HhYpnR9_wsNPIf-w_TMQSDNk98NsloOJU9tJimqTuS15oVNWemxl8j8m9f4rRmdM4nvCqKCGym8ckUqyJ0hZ_Ly1QPGl5rCG6jJRb28SZ_p3Zs0LG4tG8P-IqPJCix1t_aiCbu4f8oZz6kexJ9dO3m1_kCA03vIGf8CraQ-deenZL5aav8PLYtmc1Nzga10wkPp34zt631Vbr7R0txKZXXLaDicagfWIdNb2ETQV_pBCo9dA8A7dmfHrEWxDcoL0tAi0zpPt7O7V3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlKe-dVV3VmquMXdlz8BRK0-ySGLGj1Q9x76A-osiULPVp16EP_jYedWZTnLFPeZWjFN-ZQ_oxkBUkapt3FxAqyihQ2G4drOA9vo4kQ-3EAmCosdQbjT1K_7Krc4Aru4-Z86G5ORVtF8oLWbFX5CiNueNR0Mw-3ENZQVL388W1KVk56BOFh80FXC3jG-kCtVb9PIGHUQ4W6-DyId6RW_HxX6SfXBNaody2-tI5Xg0a_MuGh0crxVTkNAasg_QZZxoFxoedOTjZpBTl1pvhVuiJwzAyPb_yYRSKeplhTz5msqjtRuSOvPlc0GuW3L9lkXqiKVDFcmgMSexw215l99gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQoyl0qACZb5lXfLwM_4wzZ0-7tOEpD9T_zOFkCrzGQLVQ-XNEo0TQNISOOpbRbedsLK-EgpwLuA4mQ1KrRDUY54ckQDtolWzGBHvrAEPzD3AiG5_2SvWxGJ2PKnII4Yn7DkkktLmEW1R_hMwufTghHQJL6gN_MGNEIs9M6b_kXht1uh1iWRwiqUVT31wwHUvz1u1OuBVNQjChxQpfFUwz5RVINDf6VVFCnvLZhqeiN_chHlhX4DIyshbmsG9hTGh40OfIqaIIe7XgnJg32Y-ROuXcDI_7BWj67ybVbJxoHpiyIt23Pmp7Caw21s8mqxJK7uvwLZQMb8Fx0lwcdNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bm5CpDIVaK9sFAQxjDvPF0aOje-uxbG5w5hHRcZTCLc1HYjGMbwEk3NLkEUUxmA_8wm31qKrzKa6VuoLUwkzRCEWi0M0Ua5XuHL0y6hg7Nuo1zyY7X3px9FpXZ1f3IbXxfoUsujIlyRybSNKV1vauVb-ks48x9mfGwbFn2Cmd1KXhl9OyCERwTeGkaxTFhVd0_xyozbUrtcb6nzo1n83i7tw6qOxWRlDUz8RjkyUchtS7QiQTiHPzmOBepUEuaPM1VrTgOGZtFW8oMhYBjvHHj7PXOZLPZCQi0VQwO6F_YWnJwdhTxas89xOlKjMIaR3My30nOPswnBGN8sa3ejP-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=GSBO3fJ8p_CQjMAg6uH1F_JMJAWO07eQhQobaUZ_x2iYpuOuTb_IaTLrxe1QNs1RHZfRxWtkK4CbC48VH1gJrPGFyI0g6_3v4Le2B1LB_IenKsyKkB9wTwBZE2oT4DiPDQFkboE0iFk5mgvJ5TBQXGWervhVWvn6w0KfVFlmh1MFssd4Y_RFDxRArs7qeLTIR6-taflJf5V1oufgbPmemXjJFSAYVvXl9Ey0o_J1fNJF3IgKektyxZHaLPI6vo319fZSUknh9KUIFVXELAtG5p8cgRWGYWB95QPx304vwBQSNodor9h1QQqGxUajEMin6p6-PdQZ5-inLTrOvwCh6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=GSBO3fJ8p_CQjMAg6uH1F_JMJAWO07eQhQobaUZ_x2iYpuOuTb_IaTLrxe1QNs1RHZfRxWtkK4CbC48VH1gJrPGFyI0g6_3v4Le2B1LB_IenKsyKkB9wTwBZE2oT4DiPDQFkboE0iFk5mgvJ5TBQXGWervhVWvn6w0KfVFlmh1MFssd4Y_RFDxRArs7qeLTIR6-taflJf5V1oufgbPmemXjJFSAYVvXl9Ey0o_J1fNJF3IgKektyxZHaLPI6vo319fZSUknh9KUIFVXELAtG5p8cgRWGYWB95QPx304vwBQSNodor9h1QQqGxUajEMin6p6-PdQZ5-inLTrOvwCh6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcVg7JRpx1z_Qplc7ZvBS61REbijlnnr5MfshvQ4Pf4e_GLwDg7pli5FSY3fu4M9Gz_JAzQ9ScEV__ON4ENdI62dfh58LuAO6_uPXxEE2VMt0lSBFvcjvQS57OO1ukimX4VIgcupxFPHFsDgc9RuSUSFio_U0L6VoKxvXXl6xEvavUxY1BjzoLcqHupH-esRlF_RvvHduBlqsKy21-B_EJnVCzIJEbJMgb0kQO9KREvK88WLefursD4V0LkdN_Q0TBggkSC9bK764sI-_drXbdOUnRZ0mWNqQtNa8-v-P-R0_hL04CelpFYDat-xsXwArNcgSzoL7PmjsCgYGweiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIjUZW155IhBBZL7f3a2Y9MpYUbTZi05jq9Ubh6bYK1AIAIA6EVU8Rj3CSbPRZHWvOacdHO55Q2KWxiptSnPUdFNrX4g12FgYTi-2FbU73rRQEZKDLpM9bXTAQOBI9Wpgxvycnksz7xmgVuL4ESPg_lzbS69Dirl1XKq6cZkNpAFoPsW_izYPSZD0re7sOy9oyqABLAvzNqZx_elWlurowDqX2y-ES5WUwhE_KbXwwPjED2dP7ifCFp_xaXjggvW6-U67bQl0bCh3NdIdWxuJJ1c5cgqX3bujWe1bLYcaZ_cYo39Fj79PJryEZNRc0zZ0VEJTpHz35si4x5oKNliVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=JVrUyQdRggzzA14CTKVWb_w9lNDwgVwPTLjsRqBKyku6hOhwptYlJC6xhzfZt1uLoTexq1RrLWylZ4-iM0Qnci5lkTiNo4ogfF5wEZBaYwBOgrV1tmJWAKi7PLqIxvnw23eVqabqsdNptWnXJVnviskEE3qGLNkQ4uY-KiMC7js8RxiMI9ZdmQd3jFoRY_qUTYjI5fOvrcZM_bE6RBcrLmwgY4eWP-FDKpyiNyPlS1qJB34lnMHyp3lkvTzv9CDMVsZpPYr6U1d18pgXwY-tu-R8DJs5Ah5FY0s2G-N1eyp6mtRubskCvmbs9JSAZxTC3jwH72zr4PzP6_H8NY_adA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=JVrUyQdRggzzA14CTKVWb_w9lNDwgVwPTLjsRqBKyku6hOhwptYlJC6xhzfZt1uLoTexq1RrLWylZ4-iM0Qnci5lkTiNo4ogfF5wEZBaYwBOgrV1tmJWAKi7PLqIxvnw23eVqabqsdNptWnXJVnviskEE3qGLNkQ4uY-KiMC7js8RxiMI9ZdmQd3jFoRY_qUTYjI5fOvrcZM_bE6RBcrLmwgY4eWP-FDKpyiNyPlS1qJB34lnMHyp3lkvTzv9CDMVsZpPYr6U1d18pgXwY-tu-R8DJs5Ah5FY0s2G-N1eyp6mtRubskCvmbs9JSAZxTC3jwH72zr4PzP6_H8NY_adA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=d-QIZOWe4OVM0qhNTTYY72n535yAY0fsz8P61VWT1ummU4xE5zonRQVC4HwJRuZPKzqm8mjO6aMlwQPV7TeVpwNEsDAwV27MWcTpMTX6d519GiHq9RVFMj2MRRqKom5dPNONbQim40SIKB7anasSdPjqY0nuP2JHKaSaOBswrczrGaQWyj4Yy5CjQcgU1F_1GGeAqCPjfcs1qWZ8pOFVGnm4L6gTnO530vZIebuucB12DFXLB4wOPBEMZ5AXOZ2z_U5-hFA4S6jY4VTWIpCx06REIoiAt5ulcWBgbsoGsec2-MA6Qh5lDmGXiYxlgoLS6kjCfoGncTXcnxTlhp7OrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=d-QIZOWe4OVM0qhNTTYY72n535yAY0fsz8P61VWT1ummU4xE5zonRQVC4HwJRuZPKzqm8mjO6aMlwQPV7TeVpwNEsDAwV27MWcTpMTX6d519GiHq9RVFMj2MRRqKom5dPNONbQim40SIKB7anasSdPjqY0nuP2JHKaSaOBswrczrGaQWyj4Yy5CjQcgU1F_1GGeAqCPjfcs1qWZ8pOFVGnm4L6gTnO530vZIebuucB12DFXLB4wOPBEMZ5AXOZ2z_U5-hFA4S6jY4VTWIpCx06REIoiAt5ulcWBgbsoGsec2-MA6Qh5lDmGXiYxlgoLS6kjCfoGncTXcnxTlhp7OrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGkZgDXSYTUeMqPBscuMv_xm0P5y2z5vf37Zt6EU3HA2vUZSDcbpvuBXKthbidRqV9iFszMi0m8mqk9QZ4iU0n_IiPdKZr7ueqOyDMFpu9R0qBCpX8Hgf46PaIhf_kMVyeoPehyh8sZNnENj6t0xI--aD7AaR_KXf7igqTueHfnT8FwY-4nE_VTLk0VmxK61UNg7lxrQQfEYu241YvoU9SuvRd-B6M6Y7IyeUOwzZeFYzGKvw_TpNO5j_NG35NZhNYfDZjfAg3g5oWlktaTgp_i1ufV599a2uWI-7ZEkcXcMOV41bjVqO8KCU3hnF0QC0tttIRXszkWRwmsUr4_YPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhiIawTGR6rAOLU8HloMoq4isbFwFGjQU-UOPMLWtbTCyPZlmneepPR4hoNnKSz_tysNvq4q_Q4EeMCTNxkAH3zMazcXPxPjExYojR7YPhFpdAjD9J5guRtUtJuc3Ini6dRdYlq3mzCPQiZNvt0avQRhFmcKsGikkYOemAZU1op8XZXfGz75Jzj_K4PIdSB_1X9GWutZGt2PhbEtE3fNnDtgXRQ-dlYfuAAKzWZTkMI6eBGodaTLjDNb_eCtjhoo-wBr4tBQIq7XWaPB4Z4Cc0KcMrTEVeWaRCzxB1NCYCxtqJSFmrkahJQbFc8My1Ak0ZSxqPkEeUfyMvVpWZCOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4GUasO_fhEGrdiu07mX4pG_oe_ip9tTyx1VFtZ8QKqsTdmCSlbshQvPs7d5c-HkSLiJ5JE4LCCZjJk8MqCqMzAFLk4UjZY9LjgfTEjvuRsNHvzucEfqBZ8NBTpviHSjjoOKSY-QSCg0pQNJjia9pATjFQuVAaUqC1OixxCrVWsw68eQ70bGVQoA1oSDfQBEzrAB7JCwSntw30nLGZZ2EV22CuW5EZTmJJjxFTwGxiufxkSpLcPmr379rJKsMgkERRFhryvLIqorXjT7xqq-l0SUm3hsrmG1O-uB2ybBp_i064hxQNfesFf0nUqJyMgNzW8khiscNNksts9m1K7mgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgBw3aUSspwEsHuj4OnmI-gyA3_it3gLCiQVBvS8RsLcsEdLe8D4cLhy_KQf0j5DU6hoEXEsGpYkNTI4L7kbrxtgHDIpM_lxlQfMdsZXpvHzG6c0--TbFt3EpTEHKeHuoUz6ynPpNw2_RnJiHj8641Z5OdTRoXrHL0RNt1-Fgc07o4TrTuk4MnYsOOixDG-yhh5_kec4RFIww8d6qM64rH47AQT4OBBmryAAveHp3EoIWy1Q8IMSDhm_ooIoAzgez-_aRs8HRw_FJWPpbObOwmgYa02OJ1O06E3bFTUmjt54CBjOdViaVHipdjBtCKi4z8UntSKgoLR8VD9z782BmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa_Ds-zwgRFtH-BIvWdsvDBKbvoHuOpRC-m0Em1NO798LqtTMGNEPSmQKajdQGpQTXwieK9iLmvSLi3rkvdSpiTdWX2osQOUQqaDSzS4eTzXSqgXosuTw1FNzXCCiQy--nj8azXAwaDTSBTwIYo6g9N2RgiEXIy59UZF-sJcJJs8z_PIVHKrWj42z1_2XQB2TC6CEDjsZwUbt-azthfq7vv3P-jN1bUwfYq723XvWtkuCJLZZKY0eK_Di8QtBpLQ2ggkSV8jmdZ0KaDj5j_5lOut0XEwBWZKCj8JTE-Jl9T8KAhTkGFJwiBIPM_8a824fPHG3PF2EEwcfS8EDFoeQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHy3EARokWEnmRSSTT1LYp0Lpn4zv5K8jO7G3tc5o6etCSTW4dX9MEChS9Lfq3lmVerQ2KOCbQpbcfFN_A543R45pRu08llqeDXQNG-S1whRvFRZ1GnWY1nQaCaoHZp8UFcQ9pEPN2_IZFhy3b9FOwxbWNRd_ZqCe4lZTrrpXbE1BEMU52kQCmMPOKS5tUtyooYf6jP1Zrfbw7nWLKXL6Z7dVgzXWUW8HhU7_VORmqqU1gVVCY5f2xahpG-ECAD7HmjfMbJbXRsuuIRTrkWxOGwKLw-8xwilrr_ce1aFO7CasZNloFsZB0MBpVKySPNayhqKDbW6GjJyIOK9DHvIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aczzEIMkTe5-x4B03EMTJkTDMzJY4vP9enFR0lylog1m5HzoozHCMb8wNY5TnpZTKxzttc8kxecrXelusWRuTEEE3r4rHToBJssWZG338DRPtz6cRhubwV905vwT__9Tw-ZQSbMrZD6bHJd-2niRPGAPsAh_JrK3E_-m5oU4PZYsDRl_x5Cw5e9de-7Ug2lvdEO98vJND5VbYBqIu7YOcf69NZpRu2XrkVXkO8fdfOvi2RPAcbWbhem2fkTYU9cFkd--T6FeY_hCPlCt9cQBBzo-zzo8BVDAudLEJgXLdqn-Z7V84u4gC7WMUfH9DzZVENKz4i3N6kI1fajEMJaR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMJjohU0pso--xN9kUwJ738jDMvAUkxiIy3C9Xlp4qlh8_0vHDHun4vT4W4QbjbYiOW1Te3Mh7PgZ1InnYoaebx48LzUoiyy8k2O6W0RVLfytFiIfaxuseR_pbM3gCBRxdy1ZcQ1pDWf83-S_ms3O_Ac6mdOHZyTJ5EyLyFfuQf3nVwWJ3lIUjqQM_4mSq1NyjmyTCiaYobuOl0VE70314YLKIw57eT4KB2Aoxt02kiLIjVZxJlx_akUJOV3wY3V2PIQbtsNaiikZkd_FGxqp6rGToof18SRu2Or0DdXpp-kQGsn8OMWWjO0KvYfFUfVetj_r5MS2lwQAVL5QrMazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=mf_A0b3x-4x12mg4_87VYAMCtkzhV-juCHDRDFDXI_rVwKOFgOeaGuYkg6UKMznMCiq9WngipkCOPB1__2HZytlV58hu9lMgfhTQ5uUw29aqJrVR7urxywRoHx6gQA0kz1s4Ufn4uB2KYA_-iJY4PkhD2qvWK5LWc57xQQp1q1xzkJJIKQw-I9Hyfwcr9OQnhNcbgeOvnJpXx9USqiSannk17KcdCz7j6YnoO99FQo7t0WIpzFWGxRX1fZ7raZJSsa_l1_iQeYk6GERf92GHj6jlqZ2mcO_fx2PtEpiF7hg5SEJCCNz0JODX8gcsrugtI0cuUm4k6bW7Y_jhtzjyNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=mf_A0b3x-4x12mg4_87VYAMCtkzhV-juCHDRDFDXI_rVwKOFgOeaGuYkg6UKMznMCiq9WngipkCOPB1__2HZytlV58hu9lMgfhTQ5uUw29aqJrVR7urxywRoHx6gQA0kz1s4Ufn4uB2KYA_-iJY4PkhD2qvWK5LWc57xQQp1q1xzkJJIKQw-I9Hyfwcr9OQnhNcbgeOvnJpXx9USqiSannk17KcdCz7j6YnoO99FQo7t0WIpzFWGxRX1fZ7raZJSsa_l1_iQeYk6GERf92GHj6jlqZ2mcO_fx2PtEpiF7hg5SEJCCNz0JODX8gcsrugtI0cuUm4k6bW7Y_jhtzjyNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHPKdV5Y1BroEeuDvLpXC0ryluGf3l8Tz5RbAlV57uyvXSod5OMfUtgF0Vzw4Rz3-ZjunJR5AcaahBPkxOAreiy1UIVqJdhkA5KsqLDwVmPXv8yjF6nIH8G6rsXYCKMq20lMhIb1xRhcVY2YnxHp6XsvzMS3cGgpJ8zcjcGzlZTTO1rYnOWkWpHVX37ZQFriYU1IFeXlUcVx6eA7RG5Kb2iKDqQNP49LhDZq1uFERTkZE58zj7eDnTpepaU69N_N3zlFJebMs9z4kYkihikm8C9ybFDRH9VJyMzhyHX5JVEyF-dffCVBy_amSy-0i5m6a0uMZrK1AMxUkUvaAfTYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=LWqhgo9pMOKlk4f6Q2zDI9xWD8H7LVzEhn6oS-cOENfifMEk5tW5ft8nKNpR1vI0mSl7Is7VFlQUnayr7pbcu9wJ5MhQbW_vyxr0qeD20WR4-mK36ZbO0rfu0w5GFbec-dhej0sLiloU3yjEJLE_Xeg-SkxUDK9GvfvZKWulx-kHrUr-vRxABNGAvsw1lhAPBx_7x74P1zlTZHaKzR1OZStvyZIySckHPsRbkJNG_yBWe6L9vonVFBMFnUE2CE3-7MvBRGO-wor-Nmqvpt8x5sWzBiLHGrP1d2_o9hzml82QgWkjleemUpPV_oYeDt3AcKKVeGTXlEuHVpnoyZ7jGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=LWqhgo9pMOKlk4f6Q2zDI9xWD8H7LVzEhn6oS-cOENfifMEk5tW5ft8nKNpR1vI0mSl7Is7VFlQUnayr7pbcu9wJ5MhQbW_vyxr0qeD20WR4-mK36ZbO0rfu0w5GFbec-dhej0sLiloU3yjEJLE_Xeg-SkxUDK9GvfvZKWulx-kHrUr-vRxABNGAvsw1lhAPBx_7x74P1zlTZHaKzR1OZStvyZIySckHPsRbkJNG_yBWe6L9vonVFBMFnUE2CE3-7MvBRGO-wor-Nmqvpt8x5sWzBiLHGrP1d2_o9hzml82QgWkjleemUpPV_oYeDt3AcKKVeGTXlEuHVpnoyZ7jGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=DyD9VC0V4YzJ-VrDXM-EycREIJ5W4LKphKXptVHAjgEox3d8UdzGf13Tpct8ChPxSkO_HkBv_18Hv_oPXj8B_2kVUpPDLbeQ6CwzJYxz8ayAP2DPShx_Z0ztm6f8dABRlHee43gAlMpVBUwsSYi20AdP4w-_Lp6k3xWdAzt518rs6swOohr3n_GDKqe7PAqvLyDQ6t10TORLssiCciGq0xpDveT52W7GWdJX4J1UITPKZsA2S-OOtUvnwwnNYGVPHiO7HARPljlFmvEVNv4HAzzu-bDVGCWGXxwCd0v_EJHhRjhlMNnovzPDrOgeRVKjL4FMqVICoM4KXLavvkK9mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=DyD9VC0V4YzJ-VrDXM-EycREIJ5W4LKphKXptVHAjgEox3d8UdzGf13Tpct8ChPxSkO_HkBv_18Hv_oPXj8B_2kVUpPDLbeQ6CwzJYxz8ayAP2DPShx_Z0ztm6f8dABRlHee43gAlMpVBUwsSYi20AdP4w-_Lp6k3xWdAzt518rs6swOohr3n_GDKqe7PAqvLyDQ6t10TORLssiCciGq0xpDveT52W7GWdJX4J1UITPKZsA2S-OOtUvnwwnNYGVPHiO7HARPljlFmvEVNv4HAzzu-bDVGCWGXxwCd0v_EJHhRjhlMNnovzPDrOgeRVKjL4FMqVICoM4KXLavvkK9mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0UEnqhB18cVP_bxSdhY5TUeKr4UgvegSOUON9SiAiK3zMJXGHxKkmyYEPoIbW0ZQKur0D1bpz7QoIkiEd9ycxaVs-GHLTbSop9KIhg40aPidEEFdDp9lgLWqltxVHloFqgQ_HMVvCSnc7ojIk7gH8JrOaIwrBtnW6OruZlbkiHipRxDXje90USP953_H4yM-4Io61MhWF6Uw2ydP6iDNB-GzlATcmAV7rqzB_nZ1jtjAmNmBjp-3b_fiw9G4T6XPLayIJ3iA2ElCxvCXpkQomPeTfMD8CfToyLCOfiCFyO_BKXJ5Nq-RK_3o_qSQG0FpamUKvIFgES1eT9xBnqkqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_eP8y5rsd6nC9Hts5GU1gHejjiQAAzpeFsYCojshSJWx5yuL7M4AWfW-G8Vp8yM-_vjR2D1oyQjoXzwj6Rd7Ncd3FZQKQheVTf_363Jf707_4OxygaGnc0zZ0smApOubJPSMufFh2gPCwyvRk8qLykJ9B6BPmWAWTffj7BmON4-K_Kmfwkpz9a9Bu2qHP_Rv2qm9xj_H9Muc7Imd71NQWMuQFKyiM9MTtMlaUQKO1gJLf6yNL7Bz6SiUARbDIEHmE2babhyqJSlboqAIyYgaeA6vmFbvBi9xlUI5zP1v5peWcS7jF54xwoHvlb0-jqKn28hCbvByX092HKUaDtoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=VRPsWu2rLgtjJEXgBdzOa39P70geTnR9vvDGGVlYfFdEjHvgCDGU8OUnEYcfLrDhaOURdfrITs-DTkiQmY87V-bJsxPXlhMRQp3SXbobVGgjtK4zRFEnMRHXh2a5ZXpRLEMRQg_wpJKHDY0ync0fyGdBJnok18nu5Scf6-KgLV2r3ItsIFiDef6bqWaxmfjHMvfMeve_R9mKLeLQfEXnfj4lWXFwL3XN_d0YOsDAjaNH2V30IUDv0dDf8FzMu9OmGUOKQZR3OfATLy4gE40LpUmkGvFh4ZCHCTMaAzBh52SMdDxuCTdFwt8O_2I3appCkVzCFgwaZ90Er1-g6M7xemdsMCpCXC_STrT8y945Ki6IZj2rD5R73mnJpSiUfYOIlEBjgUnydv9f1DriqFIlBWJk9kKqOF39KJ3I4FXZVCValP7KIzoqZ-L4U6718zcWGmohU-yrOj6uv5CDg5V-ztbauHX2MArKXhbnl0FdAhkyXrbpQ3N3dJxbM_jLerQlr0IvuiuieovgtcxxARucRmOMV6O6PDllmMViNrV-L8BgthEZABEFp98zJlSslX2ilwPSc9a_xn0VQ7O0VHR7eRNq1gV3r0fYygwV3DIuL1j1K5W-LKvxPtYfsKe_u9mMSf2sn3unzYCHufpi3JQJPqMB4HcTrKPwdXwoqbGOANQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=VRPsWu2rLgtjJEXgBdzOa39P70geTnR9vvDGGVlYfFdEjHvgCDGU8OUnEYcfLrDhaOURdfrITs-DTkiQmY87V-bJsxPXlhMRQp3SXbobVGgjtK4zRFEnMRHXh2a5ZXpRLEMRQg_wpJKHDY0ync0fyGdBJnok18nu5Scf6-KgLV2r3ItsIFiDef6bqWaxmfjHMvfMeve_R9mKLeLQfEXnfj4lWXFwL3XN_d0YOsDAjaNH2V30IUDv0dDf8FzMu9OmGUOKQZR3OfATLy4gE40LpUmkGvFh4ZCHCTMaAzBh52SMdDxuCTdFwt8O_2I3appCkVzCFgwaZ90Er1-g6M7xemdsMCpCXC_STrT8y945Ki6IZj2rD5R73mnJpSiUfYOIlEBjgUnydv9f1DriqFIlBWJk9kKqOF39KJ3I4FXZVCValP7KIzoqZ-L4U6718zcWGmohU-yrOj6uv5CDg5V-ztbauHX2MArKXhbnl0FdAhkyXrbpQ3N3dJxbM_jLerQlr0IvuiuieovgtcxxARucRmOMV6O6PDllmMViNrV-L8BgthEZABEFp98zJlSslX2ilwPSc9a_xn0VQ7O0VHR7eRNq1gV3r0fYygwV3DIuL1j1K5W-LKvxPtYfsKe_u9mMSf2sn3unzYCHufpi3JQJPqMB4HcTrKPwdXwoqbGOANQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQqQJ8UIgWZltu-COajevcKlhEFW4kGcizEBcvIKI712UBsXiXKZIHuYDy6Qm7G3D7_m6KGS10IQ-wxVylg7kUMVS8yBnyUZKmdRNoov9ghzvLUaek8TJtF2OmL5hoPHEzwtt-1b9844i5p-c3L1OVC2qn9-xDRIHX8tCswY8xsrsnU8qIc2-Z71579La6u1H6atkNsnKLxlJjuIuEMKhmDE8wqQYnAIb7p_6UoRnZ57O9rJkiIzvs44O0V_C54CB3YOvmzZ_zFDc_AOwshXx-_Zbqd8fWYLYsLBp_HD7QbZmh4ShipSVBdvAzDjmSxHBz3wI-K-Q4aV2n91HQp3lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=vwy8qepEdkkNtFRDtWpnf1S0kZrmKJWTtqm0N2br7bNsIpb2npI_pbWvI5gxY1ox5C320XqzLTmKKtyPpv_ToDNdndIb3WaXbf-XqYtQ31pSo5ow-iXMFCU-UCkNw-sHdARRf6wPNEZNFBflqGUpwCdlI5UO3P60fMAV4aP7rYJjDIAhh_AzI4b5Cf3azHLqj18MvpzbxVZpYzjYWV3Epbbdxw9GYrlsoUZHWOth1f22r3a9yxQAGk4CR9NmV4YuM08n4TX7acY766NRgB_eUB6KVPbnedNETKMBuxiPydRD_yTJ6X9B4AmxRubUxGduIDFYfR2trPYSiSaCyqei6oLt8anXvEROyPQflZPGx1T-QfWu0Ki-ntXOEWwEkNtt-EHLvfMxuzECcwX7uRinVD-LneT8t46L0dIJ_D2GRWKDdl2gCdaWzlKm0RXZUFrn01tI-xcgRhSXN4qYSa7rUq2gcUCJpC0J-ldoMn0nUllKr2Q4WPA-GJ-lvREO3J4DCcPNbwy6FGsGvmGw-Ox0mkpBt5eZhOQOkswLZZxKtUn-GMpQm7SdWNoXVK5ICHBDVDFjaGMlSKh-CTA2UGcLzzxoZ4XHC349qH5EM_grbo1Xm1I7QaTkOVyXplAcoKZNQTyDX3iDdKKtxDROMw3jnXKCNrKZkRGdg04yYk0L9hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=vwy8qepEdkkNtFRDtWpnf1S0kZrmKJWTtqm0N2br7bNsIpb2npI_pbWvI5gxY1ox5C320XqzLTmKKtyPpv_ToDNdndIb3WaXbf-XqYtQ31pSo5ow-iXMFCU-UCkNw-sHdARRf6wPNEZNFBflqGUpwCdlI5UO3P60fMAV4aP7rYJjDIAhh_AzI4b5Cf3azHLqj18MvpzbxVZpYzjYWV3Epbbdxw9GYrlsoUZHWOth1f22r3a9yxQAGk4CR9NmV4YuM08n4TX7acY766NRgB_eUB6KVPbnedNETKMBuxiPydRD_yTJ6X9B4AmxRubUxGduIDFYfR2trPYSiSaCyqei6oLt8anXvEROyPQflZPGx1T-QfWu0Ki-ntXOEWwEkNtt-EHLvfMxuzECcwX7uRinVD-LneT8t46L0dIJ_D2GRWKDdl2gCdaWzlKm0RXZUFrn01tI-xcgRhSXN4qYSa7rUq2gcUCJpC0J-ldoMn0nUllKr2Q4WPA-GJ-lvREO3J4DCcPNbwy6FGsGvmGw-Ox0mkpBt5eZhOQOkswLZZxKtUn-GMpQm7SdWNoXVK5ICHBDVDFjaGMlSKh-CTA2UGcLzzxoZ4XHC349qH5EM_grbo1Xm1I7QaTkOVyXplAcoKZNQTyDX3iDdKKtxDROMw3jnXKCNrKZkRGdg04yYk0L9hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8OB0dlYdXFkICfHYrQqLP9UXyZoIpY-iK7e--y99CDr5bQc9UinY3WcN0bmAlCFBGGgNNoc-vPRGoinlUf2qKtoT6eMxd3BoLCYQjfGUjlG_B6UDJMFLAR4GL4IilBTnUOoLTUX8rtk30w8mLsE1_dvViMMcAuCrW05C9UpeZShOXU3sfm9qdHg9K1FZAXnY8jyPioapBAuZak0rks_J2lHOe8Flh1JxFPHDmayEoAOm7UVs0GlmFlaOsxuviS4DnSWlnUTs4CqDM4O6y8ICn88xg5JRVviTomYMaBj5XRFF-d8y6bweyvPDveRxplj1aQ2KIlCmLDTL4hob5m-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP7tVq1C8Wc75R_PJEFONgG-L6n4dgTgUQR0gzgpGwFna_Ks1ytf1AKmSkZVuVItr4jNT8vIrLT8ZCB29w4bBu6hoBuF6tV_xKZLbc0YIqXD5xjPDUP3IOFy7IUp0fjAv2AnLNdeOg9gEB8iNvSjAbwkq2_LYvJ3sNxCKRBxgQkkDrncgTf_5b71kGkNHbds9AHLc9pvBMtTBI6zeCcqchNlEATiSSkYNsxO7yq9gCWGcBCT1J0CBaiwXL06I3k3iemeEmv4Qzpgg9LtDDCT7-I25qO4ZDJ_EoIkh5uH-z9_MhW4rqdN7Zlt2h0H7-4IDQ90XjymnDd_gnJJqQYLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjJPHpO0pLic1eIaMbTtqzVwpxOu0yESdZ9SclbXWnt2JwGHc7EKjxaULFC8iG5mu6MOvzAOds0S-MyMxS92qj-wtIMBewfTKow8vc4e3oBGd-IZGphNZxdkyL8rRaU3cJrF0bvXL0MrU7pOccn8Hp0jiDfyScpQOF1aI7Q0jjJWPc4yS42J_BtE9JWWzaXcqdEHcseNvkJiRsw6xJcdZj9iMyoriWovJA6p2r_mBPg9NUFXVcnL2LlxT6R-FKgPAh2CGJcu_V1_JKjCdX426bwM3Heo1esGq-zdFfVOvlH2sjYKOGepZLxASyBTW-L2T16n8r8pLmBgADPs4op53A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtceI4LbMcWZb0znMwAMSMbBVa0IC8FgO2e4EFGzYdENvXcphJWCNYRLaobGmmWbH_X8lIO9RQdzqzwtsfRnWuwS2iboQNIISX5Wwg1SPPRBpqKbw3XlSGqJ-vOH1AVob_jKzwOI6tKVOElBP8gcwd6b7mHFWjEJw4edNlGzHZ9g31Uswlao0RfqE54Jlo2cJc8e0CVQXbgouaPCkxnIJ30otz2YsaJZ3R2jnaJ3Ruy6qHpro1uKiJFhw70gNvCGF7bQlDXTOo2m0EcWJtfAfBSHLjGJtZ-CZBw8ola_mXYtcfqbGy1se3Gm6vOj8s0TW8O3geTfJGipeiaI2YSkSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnU8DwdQDepShXfTBuQBIB0rBaIKBtqjCB8yIX7Hj3aWy7DZ8uvX7CZAqvcPIGG0G5za3itfCIRh0S4gS1UUTPe26sF2wmFiTBDTotYkaeuPsmYtmlRZ3GtPikrW7NL2Pq1XnNYrM2hpBNtYs9RA6uxJGkSJ1HwhC3urlqfzgeOcWPvuBL2DYld44ExaAE46DYgrB7ztAT9yg7Xu3J-RdlnP2yawPXRRRMMmf27PCrxgulgPORDfP8xU0mydkpGBP_52pX7PSho395hPRZa1PE1OSp-6SIKE9r8EiuPnBiAlmzEH8ISjDu8Y89vylTHJ4w-GsZAoddUaJEFTXlGkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
