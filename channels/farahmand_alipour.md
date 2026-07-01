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
<img src="https://cdn4.telesco.pe/file/L6eANzg5E2ope30iE-H-ULCvd7G7wVWIzTloBYNqXcmq7zn-BobyVwCd0ZwAclmZtL_4gOq305cOK_MNfXllWc9Ghw-N5A-7QcSViJlWV32TqHyeaEgq8bzSO_VEmRmyYqaAbOdW_vCzZ-JcIb07rKRQLOFSjUuM5iS6zvwXmoMvJua5fn0wrpvSzoQ9IMvMi_pwZhmhqxKiIlhITFeABtp7aJT7qOuu73bYRJCtsrv958Q73_FuX_29Ohm1VrCwbsH7Y0Y0jWezT3ftlakOfIwZMVPTN-iDEDm_jFnCuG7Yl3sQV64eReV09A-6N68B1MZWsFNVBiZk5FFidrM78g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 22:25:15</div>
<hr>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pialK1hk9HI2hstF9Bak8n6E24Whj9d9TY9oqsM3ZlOChJO8T5JClSiGEx8sM0ZbkgaSwZBljwne77_rkVaL6PG5maf9dsvVkCtEQFGzZxJRNExnNymIeaWCEGUxXjWjilHElaLgnKLYUeomOau7iUIkkYQG33exnYnW1j8rs0ps684fIcLFqje48DeOMgmFnN6HJtS-wXS2EjFto_rl5NEyOypP3nuWUE7GT9p_onMyz6SklOvuaBO1zmnlFqM6GJB5147mvItjtD2nJ367wB3yXDM9JirmJ-Zxo5B_IULXWHik0eA545yCEjx9aX-O4MD9uTuJBqDbjdBNzZVm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=RUYbYCMtpUa38zQUnGs3Q7WxPe3AMuajBMmf4oWPMuWqD2TIH2jHX2oQguCExT3zcZbwLOEuJ_E_EUT3xV_dZBbhOSe9gBh7haS2C7heEJd11x3aJ3yVvxnLy64WKf-_oNgn-IoE2C3-Ka-ryvK7M_kPD5rQ2vc5AQhUoIOXFbDlhZy5CSzxXT9YHn5EKvqHdDckfmWo0FRV0PqpoBDtU70n6n03Frf7B9mZtszDiIMR8Zamsv4gT4DRrrzptfCazXiqncNjxK5PNTTn8ne3P0M-2oO9AgEvaPAJDrutbrNwbzCyG36ZDUixGu5FmidJBQxYAzxAs1KQuhI0oG1Xow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=RUYbYCMtpUa38zQUnGs3Q7WxPe3AMuajBMmf4oWPMuWqD2TIH2jHX2oQguCExT3zcZbwLOEuJ_E_EUT3xV_dZBbhOSe9gBh7haS2C7heEJd11x3aJ3yVvxnLy64WKf-_oNgn-IoE2C3-Ka-ryvK7M_kPD5rQ2vc5AQhUoIOXFbDlhZy5CSzxXT9YHn5EKvqHdDckfmWo0FRV0PqpoBDtU70n6n03Frf7B9mZtszDiIMR8Zamsv4gT4DRrrzptfCazXiqncNjxK5PNTTn8ne3P0M-2oO9AgEvaPAJDrutbrNwbzCyG36ZDUixGu5FmidJBQxYAzxAs1KQuhI0oG1Xow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=lwZdIZBcH58DkCMaATQw31Fv7hm2Y1uQBSkZNMu6b8U1l5_JTPdybrEepT8QJKal8owTD7Ka9aqqymBXxOFI1lyde07IwmtV1RhjNSCO09UyDx5prSaWM_lTL7OrBoSYvHCmTVV7jJSZysarJMkm7ZVI7-jPKRn7-kN0-lKZeszUcZF1xv2theYxUZSWyep_MFEoRE28S9At6e3iZywyMcIMlScJIOJ0BOAEPnq5y8f-EBB783puu1mjLNx50x-DwWTSKQdDLWSg7Z4JGMc3wzD0k97t7BvP0OQ4p67-dhpYv0WuUF10eGJGGrPEepoqMy9FNGry1hMaeEWZ8tU-5ERJrxOULTFtPP-_LkocEemiBdGDhwXglpGloFsyV644F_PRzIOmcDAnSdBU9FVQxHsOUvF9p51eoEPJVDGWM6ZYmLku4IgrzdpvBNRL_D9EByaTnwSROzqQTAAs7W9f-uoqxRUebrLkIkY6ZhG9NvduNExBwaorUhnCwyKCFFpCqq2N1YqQQgvyoRlShaHnvBb3XRDKW_GEHM69L-oF0OdtXAqYCcFW3vZSdVRHZP_lEOhvSYxLR1ezTBO8pbDWW3VxaotTsfCS06kmq1Tx5LbdfCWffDlmHUnBGXVeIpz1H5PGewDEQm95uCcbSKAJEK61sbmEKqLwqBlV3FonMcc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=lwZdIZBcH58DkCMaATQw31Fv7hm2Y1uQBSkZNMu6b8U1l5_JTPdybrEepT8QJKal8owTD7Ka9aqqymBXxOFI1lyde07IwmtV1RhjNSCO09UyDx5prSaWM_lTL7OrBoSYvHCmTVV7jJSZysarJMkm7ZVI7-jPKRn7-kN0-lKZeszUcZF1xv2theYxUZSWyep_MFEoRE28S9At6e3iZywyMcIMlScJIOJ0BOAEPnq5y8f-EBB783puu1mjLNx50x-DwWTSKQdDLWSg7Z4JGMc3wzD0k97t7BvP0OQ4p67-dhpYv0WuUF10eGJGGrPEepoqMy9FNGry1hMaeEWZ8tU-5ERJrxOULTFtPP-_LkocEemiBdGDhwXglpGloFsyV644F_PRzIOmcDAnSdBU9FVQxHsOUvF9p51eoEPJVDGWM6ZYmLku4IgrzdpvBNRL_D9EByaTnwSROzqQTAAs7W9f-uoqxRUebrLkIkY6ZhG9NvduNExBwaorUhnCwyKCFFpCqq2N1YqQQgvyoRlShaHnvBb3XRDKW_GEHM69L-oF0OdtXAqYCcFW3vZSdVRHZP_lEOhvSYxLR1ezTBO8pbDWW3VxaotTsfCS06kmq1Tx5LbdfCWffDlmHUnBGXVeIpz1H5PGewDEQm95uCcbSKAJEK61sbmEKqLwqBlV3FonMcc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=oE9Gz8HfKiK1GNeA4IQkn6E-S-GkCIKRQaXQSNUhy2rmw-Eec-glvVS1jAtMdwkAQ1QZG82-sjOLVZmdBCm9r7kDpTJ3plE1UfEq_SZTiEmZjJyvosEjY_xOtluTid3i6aupSLb2Oz3MunembQcOH2eMfoMev-Q1noTCXPob2oVfOFy_QoN4bD4OazGPlTmTEVTYYoYpiiema1zKd89n3OqUeTbQqBn_Ql8Bx4Ge7r5gZDZTI44D52b16Mg7wXUPaeIGNpya97hdhMKUDXHrYi6-ps3Mrd0uGaeWUBik6CcVuu5Ek1lk0X1bH-R-9xxTuoHtHBqV3i0UbrkgIQkwhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=oE9Gz8HfKiK1GNeA4IQkn6E-S-GkCIKRQaXQSNUhy2rmw-Eec-glvVS1jAtMdwkAQ1QZG82-sjOLVZmdBCm9r7kDpTJ3plE1UfEq_SZTiEmZjJyvosEjY_xOtluTid3i6aupSLb2Oz3MunembQcOH2eMfoMev-Q1noTCXPob2oVfOFy_QoN4bD4OazGPlTmTEVTYYoYpiiema1zKd89n3OqUeTbQqBn_Ql8Bx4Ge7r5gZDZTI44D52b16Mg7wXUPaeIGNpya97hdhMKUDXHrYi6-ps3Mrd0uGaeWUBik6CcVuu5Ek1lk0X1bH-R-9xxTuoHtHBqV3i0UbrkgIQkwhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePD7R4akJNHgtADoLLrEGmggcBlHSCWonPMhTvzps1rXUU5QHyOhW7AEJU-wsoCKCUkneA0rIVGxQdV09hWNvoY_TGlJ5JscAuvtZwx_FjQPBCNolGMx4uy_2miPHn3C0he8F-Gdy5AhkwXxOAByaQgsQ6GpjfFXJ4p_LDkiDMTeeIU7FewLD761zzIK_nzdyGFUILhJoniqmXXl9-JDzIa8tRb9z7d-WDIwbk4RDxJ302fMiZ5dqD3kwvZ6QpD9-bgN2Xcb8y5ApKiAcjQ1GStsDV-1ajjMCVLCx40W1Q92zkQk43Tf-lPU9Wl2idMzPSEFegspk8Z5VfDYGxnJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fahTgi4jsNM3S9IweY50s1VBGNfoHpiiZlJ1GG4UftA0KGr1gEJy8J-zr4MhwZ-xKyLYgzPjYRgkxJgtuXDJCLQYxnqjIsn6yowDqYlu7yIpsWs93Z5j-MppWVYNi8GMJOdoZUwlM-cSJHRx2JWfmljPzCP6Y7_8Mxf-yGHtVHEZWj0zfPgXUZc4Oe8QlqmovLr-ViaaCaqSe-U0ZoO4S2VTwtWyVXVxBnz3hdD7_r28_ydLtBIATwbt6qFTAlD_8jyV19w0aJzIN4o8ep0ZMIaiwXTfojX8gmDD66CPQP_35DRgUUfe0oDfTavWdnVLieTvkCe8yQYqlN3ctkyt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4fKtz9aVfS6J92jL69gAiGDLK-hG0_m_Du9Y2aq_OjI1YQUEsBqRGdm1rNOwFBZFWpQY1Qyvm18NDHceTCKgn5vRB_LWiExThmh8TkQ6f7cGwXIc-aV7YhrQUYgHJT6rRXHehEP-aosnmcK9z2Bvv71pt_Xo4wx00bpAcrgZJtPo7wcpRaT8tHOmL_hxZpB0EDZQiw6kS8u-hyX6BX-wc7CEDlEXqBbjNbOh0PP3ONGn0L_dX2hQCxkjgB4lBpL_qw7WhyPdfJ4-hxX9AGeowUnGHk2_5FwgXo1P50MSQ-8AyaqOF8R8aKCDxqcaNOzABPwBgoofO7RS3isGG6oVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4HqklxJfku_mrrXqYQ1CIzBAaSAdMXnTBy2XWgsIZ8NLZpYhdYtn_0Ffil2ADCLPv5yaEQLKbn-1vkJRDS4nQJNYSdsJlnh_ev36mChCgcKMggsMDhaNSi_KyKQA5p675Mf9Pd3eDlUTcCJJrjAuHhTqAeN2sodFUvihxE92uuUigBTsTgyrn7CVmuUPICvqDNITQBDMw6q1IbVqcI929Dg08qTsuwE_3iEWeC3HwJWisRYmWud7z_-PoUxJEERLLbI7p2ycV6DFRuL4e_u_n1Xqj6u52voOKN9gn3d6a6uSPSnCmJZRekX9_iU6-6Fx0FKaWuLy2XRmpe9_Gjn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSh8XnVVJtqMeqBeoxSdMkzBP_9sBj26r_9c7BS5O8G50pjkEuePFJQs5eo_jZGjkFvKIoU3A7UhkGeML7_jHBDPg7_jYGZ8Ufy7LCfo_XN9HuwXrMHjrtDPwGs9MXLshAfn4KYhEYO1kIxBEObAKUfhEELYFiUPtJNNpWvfY7gOV2twztQrUqAcD94kxPXcBt7xKe_WTsTodQSqcx_OCm-dqyBoLnjbODXdqhZ1NK9XYaf7iuuLbOcDMECGn7ObWNXsGTAjXWhYWia_4xk0U5IylXiR64mEu7ObKRNND4F2k1Nyn2c7_NBzdCsKHWDQdngLx7rizzeCc7pYRja47g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smUgyRuPHGfoBzNjz_qKV2ynpKmsOiKaDYcjLsTVVo8MQI0VqP0uRnyqfoDbmHADBRSVMQW4krTK4Avt-bHYhBn3rwQvEhCMMOtwm73H_EyzxX3MXo_oAPoAcWF9qC_BFuzFWVirrGe4HQo_6dMxdgLWM_a5IdPyFqbYBTYhaFko-G-mvJentcqXn3qnUR_ponLAuvlw2c95RnsorSuEJNWnNyy661Ev3OrnCSin44VR7goG6AYs5sI3PSZuTVo7Uk0Jmo0M7gcn95z0TJRJzJ-ZCqX3A68VmAQ_k1Updg-20aWhVXplP9t7TSeBQIPFMJWD_MzcE6B0-YLijBu3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QQJIZr0MEjxAsoODBxMHx604QVqgejCzXidAFUSZJV87DGrtFSobyC7ooX64Y2JMzRuzsTwbONnjy8V7N7klLSenKYIA5YdGzLEYYvgZUvBdYyyCCZQI8m_Pbw3iTJl1D7Rb4s4mMAksFaOZYeeA7D6HkgDWMEy-vY583-leNKj6SvfJzybnkKd8VpCBZCBg-YZFH7UrU4NIO2fRNqvxNSJP5C0lqk5_lN5FiB2JkatF-sBSt5IMPLHahwI6JbfArSQEzCdTlfMR4o0h-e4gMGNh5n5IoEox12K57uwQs0Cah-sV_391H_KNm_uSxr0pL9a7ee1Rnbu6mlXIEcm4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QQJIZr0MEjxAsoODBxMHx604QVqgejCzXidAFUSZJV87DGrtFSobyC7ooX64Y2JMzRuzsTwbONnjy8V7N7klLSenKYIA5YdGzLEYYvgZUvBdYyyCCZQI8m_Pbw3iTJl1D7Rb4s4mMAksFaOZYeeA7D6HkgDWMEy-vY583-leNKj6SvfJzybnkKd8VpCBZCBg-YZFH7UrU4NIO2fRNqvxNSJP5C0lqk5_lN5FiB2JkatF-sBSt5IMPLHahwI6JbfArSQEzCdTlfMR4o0h-e4gMGNh5n5IoEox12K57uwQs0Cah-sV_391H_KNm_uSxr0pL9a7ee1Rnbu6mlXIEcm4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KF4K8wfkMsoJoMBpEe96dfRQYHvj-f1e_MfVIymey6Sv7IjOP1xsDnO8xP7UcFHDyQSf3LfGRiAXclCTBnf02qozwtnzmJzGDT_5_3kQr0rL2Sh3aW5HdIeo_V7Wu64H3POhV8aFcxgb1FePMMmxhcBk-EBoRkgZr25UrR1ORdXikAJoWPmhsHf9-Qy0Llm8iS63Zcg6NKgIFhNEUfilnTXr-jFqnt91raUOvcvzi0Cavq01VAsfqbJchrMGLln7WHHn68nLj_0sz2J11KRbBcXC5NZGytp08Bjsnl1ih0edrJbFoY4B2kUSRWpmnkhWqOUH2Bkb_ANRsgz8Kqwsig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=VkHrDrjVOjysA3ZIbp77lCIKnkb6inM-JkJ9hDKoh4jW3-ne4tFt9ea-F0KMgPD_F3VGfZu0oYqL3Q0_mZuUkvuIl4Zg0P7UpJuSpvyjrIKIXBOrbjb9jKNIkwSFpyybEPpzm9akzDvB0sESTzfZpuptwWpZmNAkhR-LXPQ70zfjZ2mZhXibJ0KaVgqgqKE-4vfjdGGTguj4VkY0UUkzZXgyR8njL8960JWrljkhEHC9IiaO636K-1nEP_e1CfJ0Zw2jT3JSBSyJQ2aiGOv-Q6dxHSKD5iPuKR54OITgmkAiRx3tI7ys0_GZCpZHYP4Wt6FGiS317aqKGaDNxsERRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=VkHrDrjVOjysA3ZIbp77lCIKnkb6inM-JkJ9hDKoh4jW3-ne4tFt9ea-F0KMgPD_F3VGfZu0oYqL3Q0_mZuUkvuIl4Zg0P7UpJuSpvyjrIKIXBOrbjb9jKNIkwSFpyybEPpzm9akzDvB0sESTzfZpuptwWpZmNAkhR-LXPQ70zfjZ2mZhXibJ0KaVgqgqKE-4vfjdGGTguj4VkY0UUkzZXgyR8njL8960JWrljkhEHC9IiaO636K-1nEP_e1CfJ0Zw2jT3JSBSyJQ2aiGOv-Q6dxHSKD5iPuKR54OITgmkAiRx3tI7ys0_GZCpZHYP4Wt6FGiS317aqKGaDNxsERRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=AQveociJM9Ilmevv4kiudV68vkFz0_7JV8BoMP5S8-lO6aDKIe96IkCr7PNKAJMcfEJ-6EsyrFLXToOj_3181esT2glBQ9I7HfN_9rO14E9xfuz2D0MutXylmC29Tht8GEgCxdDqB5SGjLFlkm5-3_rr5_Qnq5082s_-6aNdb1sL4EXb-ls6oYm-i51nqiOpEgxo5G17v9RIJ9kJUEF5X8N07_QieydbE6Ld6Jsl93eUR6k6raFpeku8iIBa98kEbMHB6ZP57iAhgilWCknWLmRnTmK6_k9UMCI4Y9FyUrBm8kTscgOw1eYzhwvWXs_7VBl1ESxN6agk9HGNKjHc5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=AQveociJM9Ilmevv4kiudV68vkFz0_7JV8BoMP5S8-lO6aDKIe96IkCr7PNKAJMcfEJ-6EsyrFLXToOj_3181esT2glBQ9I7HfN_9rO14E9xfuz2D0MutXylmC29Tht8GEgCxdDqB5SGjLFlkm5-3_rr5_Qnq5082s_-6aNdb1sL4EXb-ls6oYm-i51nqiOpEgxo5G17v9RIJ9kJUEF5X8N07_QieydbE6Ld6Jsl93eUR6k6raFpeku8iIBa98kEbMHB6ZP57iAhgilWCknWLmRnTmK6_k9UMCI4Y9FyUrBm8kTscgOw1eYzhwvWXs_7VBl1ESxN6agk9HGNKjHc5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=Lcnd2DkkI6U_c0yVP1jTnC46DiTUysxgzPgOaS-wvqY2oWK-68PRLvJtqgF98og2wBl17w_lxTpD5qpL9Pf9sKZ_R391d2igGYuuB2blTj5-jKL6McVKGVeAQ2MYbhvJfVxOtm7-ulrobT6XEqK0NuRFhcWaTl6pJLEVT-PBJr_2WW8FJ2EruIxnloKtS_xW4Cp2hezWaKAyPkzmgOcBxzAyM8uhl7_oX0_xbIc0vr79u3cNbobQ2UfTGOlJG8bbcqt761IX_R7MIVfNuJIwQi8jiaZwXtiRXu_HphiXc8gLTSkzWQLTpKyUXuaixQsTuoUH7xu8oE8YYoznegd95A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=Lcnd2DkkI6U_c0yVP1jTnC46DiTUysxgzPgOaS-wvqY2oWK-68PRLvJtqgF98og2wBl17w_lxTpD5qpL9Pf9sKZ_R391d2igGYuuB2blTj5-jKL6McVKGVeAQ2MYbhvJfVxOtm7-ulrobT6XEqK0NuRFhcWaTl6pJLEVT-PBJr_2WW8FJ2EruIxnloKtS_xW4Cp2hezWaKAyPkzmgOcBxzAyM8uhl7_oX0_xbIc0vr79u3cNbobQ2UfTGOlJG8bbcqt761IX_R7MIVfNuJIwQi8jiaZwXtiRXu_HphiXc8gLTSkzWQLTpKyUXuaixQsTuoUH7xu8oE8YYoznegd95A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNsPYGZ0qvEJfuL9Z4J5N1VHys0RiZdUrqdWm8bGwSZNU03sND2ojuxXl1sHTTNoWRS6gRYB2ANuYFtB2R-dvRpUCBVr91dGBwZBfNQi-IN2lWDJ4rqXTvJugZR5WrD6g2vxT-cSUB733sBfEFwwBXBO5tDAzi8dmHa2cE244Igp-kcrbCg_X6ezBruOmcHKl1-6KoTf_vxNeMvs1sr7IilNPTp3wABVo1Yz-0kjo0nq35sU8fYP-JMdgR19hWSpQRGpH3E2GUWNm3LN94S3cHESndtySP7r3iccWFPkhRshLdwwHEU2JmsHBj8REOaYQ-m_1UJUAQ2dRnW6mvExeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=sFNuoOjguNb5eNfQmFhjPOTN9bgEDIh2PhB6BypL9lf1iffKIn_ojfDAnws-SklbAbNuXMnTD2Xz0-9ndO_AStdux1-aOTxD5QrhNR6MdP_4wfbc23ZYzsAoL0_qdkR8XPewRp-6rtZPkVZzQP3Jn76Ol-QbAgFt477qlHyzQStV8zgSsHWwrH6DLXLCBI9ZWtQEdvoVQRwDY_eTDzwqPjnR1dRXNF--6-d4jEL2K91Znsrx6nvv4D9l2yDaZVpKOwUZebs92TcOjxv3-ArHZ7maeLrVfbp9A7KhjpxE0VMJ6KTgKntIL3gfWi7kh0pejp-YRkOyygsX7L7M7GzfVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=sFNuoOjguNb5eNfQmFhjPOTN9bgEDIh2PhB6BypL9lf1iffKIn_ojfDAnws-SklbAbNuXMnTD2Xz0-9ndO_AStdux1-aOTxD5QrhNR6MdP_4wfbc23ZYzsAoL0_qdkR8XPewRp-6rtZPkVZzQP3Jn76Ol-QbAgFt477qlHyzQStV8zgSsHWwrH6DLXLCBI9ZWtQEdvoVQRwDY_eTDzwqPjnR1dRXNF--6-d4jEL2K91Znsrx6nvv4D9l2yDaZVpKOwUZebs92TcOjxv3-ArHZ7maeLrVfbp9A7KhjpxE0VMJ6KTgKntIL3gfWi7kh0pejp-YRkOyygsX7L7M7GzfVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_Rmn50EvizRPjbF1XCMsNgM2Gp9shnNQTRfMsoinxRXaYJzDZ78UVFbIHFY9uMpXYXcV-kzIY8uiAaueCQa0DHPPBfxoAm1bxVDJTOz9VSzNhNUrR3f4q_ENme5UcKsEkrMflFTmEmcaniT0czTFmxpb4h-tZtLQxyBy8TBwY9QozXPgV53pF-MV_R-_hbclC2nSpzcqg_Z-qhxxU91HkYxVl1DTN2rzUZ_8oa-1SSrzdAU_fY4AXX4eIVEL58XCwd5D-UpOCkuCd91gaAczyDbyfBQdFBRCj4BcOVvImqCDHPicvHjsi4P5t2uUegJLKLMt_989TeaMB-GoluEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFlfDranWzJvpkcLkrke5lkuxuPBpbfKo0hBRTWq7KAS8B0rvTrVAZH0dNEjTGIS_9e7IS6noEiMUMDPMWX9cldKlM0I1izvTLP-oP0LYNtwUL4U9h8oRsjcHNu_erHZWcme-ZcfrblWFUH6wrT3XI6CLtrT-OnvcIn4pTQFpH_1kr6p_-kglGzpcTJfbkRzODDoj-3cSRVTHRbMnLUWTaYIFmxL3rNQWDIwLdu1AcRqREH9mEll1vF-AhGaY-t1eyA7J-IJfavXz9yIZfpe15jeCz4Pk_4QYbBDMzD9Rxxe4C8tofAswBnDO3_orvuqEbdbIe1G29ViZcE9wX26Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=i10fjOdMpZtLxPyDWscfPWsiS08dJVHh46PTkNCIVfvcfTuYuz-y3xSogvmGiUwFvgF86Mua7nmj_nQxa3HryXaGYiO_GsgaKRybHHdQfuI9An1HTzCeUMEqgdOm7Cq-qO7sJN5kS2hUYCVh4aFklVZAEYCwhuxmJ0kJdyk7vgJZIEqx4qrGMmjHejDJ--wDUiFkknSqQp1GOalKhVYWKzHfXEtQ5VQwDL_hfoOhslCUk4u3Tazadbg8cR-SLOVmmY3AI6WgOz77rQsb90qQb3gc7eQpPguVslWlR5or4c8ItaO2XYsZWjkQljgimD1ygz3CbT1LGU_9AUEcnAvRng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=i10fjOdMpZtLxPyDWscfPWsiS08dJVHh46PTkNCIVfvcfTuYuz-y3xSogvmGiUwFvgF86Mua7nmj_nQxa3HryXaGYiO_GsgaKRybHHdQfuI9An1HTzCeUMEqgdOm7Cq-qO7sJN5kS2hUYCVh4aFklVZAEYCwhuxmJ0kJdyk7vgJZIEqx4qrGMmjHejDJ--wDUiFkknSqQp1GOalKhVYWKzHfXEtQ5VQwDL_hfoOhslCUk4u3Tazadbg8cR-SLOVmmY3AI6WgOz77rQsb90qQb3gc7eQpPguVslWlR5or4c8ItaO2XYsZWjkQljgimD1ygz3CbT1LGU_9AUEcnAvRng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0lw05bjgGeYGz2ZETLl7Rq1BQkIujdGrBTXvRWKBrNPjFt8vLwVeia-d7w9AJ7oqp1kJjCFsQwkLsPZgdoHcyeKTy2zYiB-mNdu3jX_0BovNty-sM1uSOyRpl58T8nANfS2Le0gQ2dIf-PxN-Z7G4DK16xZDl3RDOmuHJQNEmOe3VEM6lvnGwGsy15KNY5SK9AeSFeBwdw0yNNYDYrX-W4dxhjitE7apKGkGdP1rYUV7cCQukvj_KUT6Ctz1a40voPY2mxdhPcNjsiIH5ijjdJq6eRdP2VBgiaGg4BTR0dJ96pv7Mb4HHDkeH-ozSmmueR7r8thH6OxfkpL0wR_OWz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0lw05bjgGeYGz2ZETLl7Rq1BQkIujdGrBTXvRWKBrNPjFt8vLwVeia-d7w9AJ7oqp1kJjCFsQwkLsPZgdoHcyeKTy2zYiB-mNdu3jX_0BovNty-sM1uSOyRpl58T8nANfS2Le0gQ2dIf-PxN-Z7G4DK16xZDl3RDOmuHJQNEmOe3VEM6lvnGwGsy15KNY5SK9AeSFeBwdw0yNNYDYrX-W4dxhjitE7apKGkGdP1rYUV7cCQukvj_KUT6Ctz1a40voPY2mxdhPcNjsiIH5ijjdJq6eRdP2VBgiaGg4BTR0dJ96pv7Mb4HHDkeH-ozSmmueR7r8thH6OxfkpL0wR_OWz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=l_O1PWuihVg4bdf08X87doDU4cyCIB6QVuZbXW0G91OHVKlA74nK7G3LeLnNpnbWEqNzHmbAqLL2rKtDkINz53JhepwuF6GIkMnfIpEwKnIvV7MK48Yj7FOdSebZCT79z0hgiH-_ioKAeCMULe0tT7sdiv0WCOxM3C-jf6VYLeHWJ9EksIfAT-ySU-6P5QwH5UyjqYo0iFYY4msGaw0R3uq7LLEK8_M2ayxBM7cnDC3sRa88aEU0rU4NF0MXfrwzl7wVnj1_9YWbhAHBPUifN9hq0RHkvTV0UKA7H_Sgv-nHqQ_f6n3iFnL9mU-De0870p_kC7Fp95faoZ2aSDRiMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=l_O1PWuihVg4bdf08X87doDU4cyCIB6QVuZbXW0G91OHVKlA74nK7G3LeLnNpnbWEqNzHmbAqLL2rKtDkINz53JhepwuF6GIkMnfIpEwKnIvV7MK48Yj7FOdSebZCT79z0hgiH-_ioKAeCMULe0tT7sdiv0WCOxM3C-jf6VYLeHWJ9EksIfAT-ySU-6P5QwH5UyjqYo0iFYY4msGaw0R3uq7LLEK8_M2ayxBM7cnDC3sRa88aEU0rU4NF0MXfrwzl7wVnj1_9YWbhAHBPUifN9hq0RHkvTV0UKA7H_Sgv-nHqQ_f6n3iFnL9mU-De0870p_kC7Fp95faoZ2aSDRiMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5OysA8jR9_B376Fg3dnp_jiT3kNze53_WhM0NGsPcih6ruZLzayNbfp98I1uE5ZezoibG3PeIrTkNfKv7ag04zQjoceH5RraDaUCbpQojpTeFLSWTFoPGo6GUr93q5cO4cKb_og4g5aiSBTfzGogvDucn-N-0JPJY9JROaAibGPCnG3Pft0uzx1Z_rnizigVdePHqDqOKkmpZnmZ6ZmQUocPM1SM3ka7ObH8G_NIku3WRBlgOfh7r_olHjVALvMUXMVwRnXjxyqkqxO2SMjLESuWoxB0XElIcFZFGvhhXiqudtOPtjplAvP6xYtgByenoBa28qnKatMHguEeAbodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=cN5txVb-GqyEJiesxWieX-Yrwj8m0RytzTzdZxpvbNIaedJB_0pD_xvaTBYKX1YGXe2RgvNOleaB9eEx83D8xjq7KmDN6lktPWA_MLcIe7I3betLXgEnB4yzbMwysAaTzNSkuXiS-xzdcvBf4SE-liT-KSESTTzLBpmo6PlnBc0ctUvCrgjOP1oHFY9cf2shqpQ0UFTFhUMn3BqCAeFVieGgNgUnCmyO46Honbk6BkYxl_ht2MR8AboaRbObNSAbyK0aW-sSGrPJVTY2AOPKAC0w3ZC124wOrSxmXGhSbFmECn0WWnn0iCQOQhSOuBX5mgJKn-TDUPO2H2ynrnrKFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=cN5txVb-GqyEJiesxWieX-Yrwj8m0RytzTzdZxpvbNIaedJB_0pD_xvaTBYKX1YGXe2RgvNOleaB9eEx83D8xjq7KmDN6lktPWA_MLcIe7I3betLXgEnB4yzbMwysAaTzNSkuXiS-xzdcvBf4SE-liT-KSESTTzLBpmo6PlnBc0ctUvCrgjOP1oHFY9cf2shqpQ0UFTFhUMn3BqCAeFVieGgNgUnCmyO46Honbk6BkYxl_ht2MR8AboaRbObNSAbyK0aW-sSGrPJVTY2AOPKAC0w3ZC124wOrSxmXGhSbFmECn0WWnn0iCQOQhSOuBX5mgJKn-TDUPO2H2ynrnrKFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=lwa-RTWAMtOOM6m7b_4GZUzSwkFN1xh-H3ehnA5zX9c9XF45TaUcB6_S8M5ck-K461T9EtznactvS4fms9jG_RY8ilZX2SGwD37E7ntJID-ZuxM8runeeqzuFCSt18UPxaBe3wntA391laPIjA3pHRao96aVSRJGvuQZ1CGXkAG70b7UDNI-OtB_WcbYlf9URDXRcpmWBbcXXjeAfE8APFtsyl7uBcBUMw0M7vRUXLmFcWPCPSp2VOWm8UUSMsT0tRfQh2rBW1eI8UCRhCl_BIkF34qZ3LciFPMdfmpUkzGExILe6TA9OlXXZkS_i_BtL8zjBlzVK48FsyfC8mr8Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=lwa-RTWAMtOOM6m7b_4GZUzSwkFN1xh-H3ehnA5zX9c9XF45TaUcB6_S8M5ck-K461T9EtznactvS4fms9jG_RY8ilZX2SGwD37E7ntJID-ZuxM8runeeqzuFCSt18UPxaBe3wntA391laPIjA3pHRao96aVSRJGvuQZ1CGXkAG70b7UDNI-OtB_WcbYlf9URDXRcpmWBbcXXjeAfE8APFtsyl7uBcBUMw0M7vRUXLmFcWPCPSp2VOWm8UUSMsT0tRfQh2rBW1eI8UCRhCl_BIkF34qZ3LciFPMdfmpUkzGExILe6TA9OlXXZkS_i_BtL8zjBlzVK48FsyfC8mr8Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vtr17oRueptDpn1iXhBUL0v1UmxzeKwzUI_GC6H2pAphZIuDKJCtLl_eO-T8dNl4Eor6STevDZ3nptWYATWQnxFmNnQtrWFUF4cagIsKyB71qVsr_-1FOqWNiyNw8NksNpd0jXoXgJDuM_HcBDraXMGvY752JK0Elfs5XV8q9kZz6P-bdrl1CqiFYI6hSglteGuPnVEwILsCRImvtaIWy2pOmFGoRMK0ztFs0gtyT0KMuDL365CoSChbOyT4NoyLq1zJ2AbkRZZD30QlU16suMfxc5RKwxcGDapGxyOF1jQ2zeI9z_zTceb08NPpEOKKQkfaYNTtWHfYT3D9tPK_Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vtr17oRueptDpn1iXhBUL0v1UmxzeKwzUI_GC6H2pAphZIuDKJCtLl_eO-T8dNl4Eor6STevDZ3nptWYATWQnxFmNnQtrWFUF4cagIsKyB71qVsr_-1FOqWNiyNw8NksNpd0jXoXgJDuM_HcBDraXMGvY752JK0Elfs5XV8q9kZz6P-bdrl1CqiFYI6hSglteGuPnVEwILsCRImvtaIWy2pOmFGoRMK0ztFs0gtyT0KMuDL365CoSChbOyT4NoyLq1zJ2AbkRZZD30QlU16suMfxc5RKwxcGDapGxyOF1jQ2zeI9z_zTceb08NPpEOKKQkfaYNTtWHfYT3D9tPK_Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=G13n8TiKL5tryLrkLOmRdV5b8ied7D73bMA5ETOPIGnty7cS-ejhhoz0lL91ZlHgla-ht5L0T4tbF2d8ksRuFMreaEaWycO3Gd6Bcu7ztkicSVDC4Xtfx8nNqcgg_3F0ECQC7MhrsQtDpEYDcQsdkj0HJeDXsNTl2M3s3khxYAnW017hYOC6sUEu7SccNBknT_Pgr8DUnN0zGO_y7Or7vLkTjCkjtvvlUy3xKRrkvJTaZk-r860SzceFuYRC1o_kOGH6YHe8I6HuLTW-u8Sox4gPx0eTsz0Hs_QTcRDBgbPyBNF_ww5Nw0xU2bbsWjMY8jOu6cl_lBbzf3B2NBV4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=G13n8TiKL5tryLrkLOmRdV5b8ied7D73bMA5ETOPIGnty7cS-ejhhoz0lL91ZlHgla-ht5L0T4tbF2d8ksRuFMreaEaWycO3Gd6Bcu7ztkicSVDC4Xtfx8nNqcgg_3F0ECQC7MhrsQtDpEYDcQsdkj0HJeDXsNTl2M3s3khxYAnW017hYOC6sUEu7SccNBknT_Pgr8DUnN0zGO_y7Or7vLkTjCkjtvvlUy3xKRrkvJTaZk-r860SzceFuYRC1o_kOGH6YHe8I6HuLTW-u8Sox4gPx0eTsz0Hs_QTcRDBgbPyBNF_ww5Nw0xU2bbsWjMY8jOu6cl_lBbzf3B2NBV4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJZhjFGnmrqcGlHIRnKBBvi91xy0Mw6Cgh0zFgUmk_Pav9F4sp3RXo55cjEsw291KsrRTSEgwbBOSAU-Gpjg8CzofvvyxAh08Ap_wAOrPCGKX69b5Kmbj1Pi003qJP1uhvFJSx6YgFFTtXYlj7xMN8JluthQvg-TTpz-AkpskzOBeci91vjMpODVxQY7QeE92RhVaYjOdk7SRE-JK0i50mdU528Ggk-FxQrXLgiFRqS2sPcuiPX-EHcqdwGrQzJvse43cniHTnm6-d_sR7v2O7DZ86VqfMsw1asbWx-W3QMKWvCsHyN8xh__q5NI75XjvcWQ4--mZIYbLCHIMd95fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=IUXW_laYQC-qg3LcMpEx2xvvRiXDsGf3KVQaKuC1vymkIHLe8PDG5H-3c8671dLLe8BD1yBTinnIxlfFDJrtgouYvIKspEiR0oxjjXBJI4x2CVXbdoT2ukw5lnpWHWziuCnUAcTVxXAvEHdNo-H6hGfaCK1kleHlhUoC9GfR3xG28uUsNDNGjHc1K8c_jb9WAr4SDxUZCaxwRZK8NEJT_nTEhRukeSaVuJBxAtwlUwlyQ3hmC3VPULHTssOYWk4JxMq8l8KCaTEueue6kXpLeNZP6ljui9ifpuZxK4U7WSWD5vaAR5jc2PUlc1mUhB6R13RkFJChFsu-A5kMJqTniQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=IUXW_laYQC-qg3LcMpEx2xvvRiXDsGf3KVQaKuC1vymkIHLe8PDG5H-3c8671dLLe8BD1yBTinnIxlfFDJrtgouYvIKspEiR0oxjjXBJI4x2CVXbdoT2ukw5lnpWHWziuCnUAcTVxXAvEHdNo-H6hGfaCK1kleHlhUoC9GfR3xG28uUsNDNGjHc1K8c_jb9WAr4SDxUZCaxwRZK8NEJT_nTEhRukeSaVuJBxAtwlUwlyQ3hmC3VPULHTssOYWk4JxMq8l8KCaTEueue6kXpLeNZP6ljui9ifpuZxK4U7WSWD5vaAR5jc2PUlc1mUhB6R13RkFJChFsu-A5kMJqTniQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=s6wD8RHfQ4v8-obaFgPOc4gfYSGI-cmvBHlzKM9ZKCB6NYFyXyoCESYEFdatLJGmofvygbMkDLO6eAcwW2PN6L-I2p_bfomo0HkCm-1zR5srHNHiQxcHcs2OHDx64-dJM6LAmswDPCMWXH_uZ21ethiJ6JB6DwA0y1Y-xAJxC4N0USyM4VncZMG2DJgl5phb8gP7gLe9PtM_yp53x_Fgk7cS0PR0fA3KkC3bxVR95dq0RFjiwBr99jvxPrqESGZSggXDoOI3DxqHY_m2l4OWqgAwNx9bsTMZf3VDGV4wdXoKrAYjjiwqiksdqyf-k505OEDkbRBGb6Kls4eH9LRRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=s6wD8RHfQ4v8-obaFgPOc4gfYSGI-cmvBHlzKM9ZKCB6NYFyXyoCESYEFdatLJGmofvygbMkDLO6eAcwW2PN6L-I2p_bfomo0HkCm-1zR5srHNHiQxcHcs2OHDx64-dJM6LAmswDPCMWXH_uZ21ethiJ6JB6DwA0y1Y-xAJxC4N0USyM4VncZMG2DJgl5phb8gP7gLe9PtM_yp53x_Fgk7cS0PR0fA3KkC3bxVR95dq0RFjiwBr99jvxPrqESGZSggXDoOI3DxqHY_m2l4OWqgAwNx9bsTMZf3VDGV4wdXoKrAYjjiwqiksdqyf-k505OEDkbRBGb6Kls4eH9LRRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9_TLZHN1rxQsY3K6xtbSpSDHIIz5W1_KbnBvIbn0xfb8IlRXWGwIoTlOxXyewowS_QnyxGKntEqAIo6yfV0Y7IJS9iNLjSHLgIM05jYpejqqlAvWA3dY5WtXvtloL-q1DBGW8MWhtddPWUKVITG_JKYuZu07QfarniyEgdPRt8-nkfMJ5SkLf1c_Rn67mFamA-Eqxpoe6vOTqFzvHbc7Ma_SJbpumCK4N0Te4Z-SK8AJmKzovE6yXxAzNjgFtEGn57SCTnCcxWWdeW6v8D6E7BnFDl6fIunyyULfPneojrDkpvXQs1DTBJmWw-HZ9D_2SXIyBxiwcTpmexyw9SVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=a2pD0zvLSApVAOcCR9nle3So-5sNTpSgg-xRA2hNuPXrZpovuOKR2bkwLvNuwbAU0_69ZbfDRAMJGWCuowXIYk7kGPI6dM0FYYan3VEVFHeKClLT8sm8nOAjDggxxsPSGxQMXE2Oj6y2MVsjD-cm-qtYfKixXlnZPZTtf1H74yYHSMyeHc1aXT0VGuX3s5NAnGGjhiXfS4llanStuPcYLmK5HSmA0Ml2oRwSPxHirfkKmBtO7Q_ZUFBElnXvH07Az2tzfpQZGR46vcpJMQZXybaDLbvWCz8cmZvxq_rbj5YpdEa12OILCa552AaUInNkx5kjmiDrYeb0jwVM53jv2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=a2pD0zvLSApVAOcCR9nle3So-5sNTpSgg-xRA2hNuPXrZpovuOKR2bkwLvNuwbAU0_69ZbfDRAMJGWCuowXIYk7kGPI6dM0FYYan3VEVFHeKClLT8sm8nOAjDggxxsPSGxQMXE2Oj6y2MVsjD-cm-qtYfKixXlnZPZTtf1H74yYHSMyeHc1aXT0VGuX3s5NAnGGjhiXfS4llanStuPcYLmK5HSmA0Ml2oRwSPxHirfkKmBtO7Q_ZUFBElnXvH07Az2tzfpQZGR46vcpJMQZXybaDLbvWCz8cmZvxq_rbj5YpdEa12OILCa552AaUInNkx5kjmiDrYeb0jwVM53jv2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=e9ZT97y0edAUDOAzRo5MTKpiKg32D-Ytc4UgKMKOmh6EPtBm50JoMV5DW6l5y-tNdzuIRnVDc9azm-vh40amWjyNELVXZo3COh_bPTXor-9WAtEJTYGLWmcZ65Q4RAkyidvCAQU_LywBNkGYc3THgtzn7FOdjndSct0KG2r5mKH5xVDj_qv15rTnA6_7FUcXbtnPYLK3jjMCAyv0tH6LHUmiNogNLFHn4wH4ginKlKUVwxUYVImiLmkOuYwFzkuPPE3xkTjEGjGLc4OMPFGCKDCW3iZLvZ6jqj-yhzAp1MYZXWS6LEDa-6SEZb_Ye7yN3tRi1FDCn30vNK4mPY17mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=e9ZT97y0edAUDOAzRo5MTKpiKg32D-Ytc4UgKMKOmh6EPtBm50JoMV5DW6l5y-tNdzuIRnVDc9azm-vh40amWjyNELVXZo3COh_bPTXor-9WAtEJTYGLWmcZ65Q4RAkyidvCAQU_LywBNkGYc3THgtzn7FOdjndSct0KG2r5mKH5xVDj_qv15rTnA6_7FUcXbtnPYLK3jjMCAyv0tH6LHUmiNogNLFHn4wH4ginKlKUVwxUYVImiLmkOuYwFzkuPPE3xkTjEGjGLc4OMPFGCKDCW3iZLvZ6jqj-yhzAp1MYZXWS6LEDa-6SEZb_Ye7yN3tRi1FDCn30vNK4mPY17mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=KrVVB54yMdSNH1PXQxUnmu4spjO4sf6_6WPEmYKId83lI_8r8rG2Dw_w_ikLbhD_wPidEuTX1YLrIiXXvBLdbSoy158WhUmjcLePJ4K2GR5pnWSGNDhCo1Avm9hOdkGXAh1E44Ho5MO-tA7K2ZtMhuO4JKriNxd8qWPJaWWZBxw0Dry1lDlmQylBhzitu_Pyoi9tZlxYdIv3-iaDruzfpVjAa7R4JJjj2mHh64pG2rNCqcFjkApeU_mBlrtFFx-gk7mRj_vuQbrjvxSlk0ZIOxXPRG8ICNusJbjwDVK5k7VHsPxQwV6tDK7wkcQF8wCsPP_hpA-AQqntnpAeER28LDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=KrVVB54yMdSNH1PXQxUnmu4spjO4sf6_6WPEmYKId83lI_8r8rG2Dw_w_ikLbhD_wPidEuTX1YLrIiXXvBLdbSoy158WhUmjcLePJ4K2GR5pnWSGNDhCo1Avm9hOdkGXAh1E44Ho5MO-tA7K2ZtMhuO4JKriNxd8qWPJaWWZBxw0Dry1lDlmQylBhzitu_Pyoi9tZlxYdIv3-iaDruzfpVjAa7R4JJjj2mHh64pG2rNCqcFjkApeU_mBlrtFFx-gk7mRj_vuQbrjvxSlk0ZIOxXPRG8ICNusJbjwDVK5k7VHsPxQwV6tDK7wkcQF8wCsPP_hpA-AQqntnpAeER28LDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nK_QKPdjFsXFh1Vgnkd-gOs-8enEXFsfah208W1QYUA2yrXLdv92_RyGGiqS5f7xkB5tpJMNK-mbqP_qdejrBZjqDX81Qbhct1pjJkNFaDl6CzFzPDdIbuESWNS9E3LknLjvj8wyHvKHwtP1aABI4xJt_QLiPmrbTzaOlFSCIlNOBZM7VV9uLn--BaFsPSQizhQEgM2FODMo8sXqWW2Zc6EDVxuXSu4-X_wU4MMtKP1olQKDWXBtxVY8oi1j071Bu4r_tkqFUkheYx-bs5Vazhqy9ZhffSQQ_pGm9vqGCBycfQ-Gf_54Mk89Shi1ZC2Od6UG4d5OfIPPO4O5gY5L1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sr8jiq-jMl2hpkIe0vrrotDZOew7FpLr8yX699uJK_1C72w9Ut7E5IWSotcP0kF46E7zk9rw87dp0QenEvWe9aWpJTt4bUuC79x6YtP3EQtKZ-tATEMQh9_u7CqhAszJORW6N7lCGNaD3Q6F4g0M0KLxydGTDXtI4imMJ2Hd3VSxd_8mgsN2snaBLcho-yuqzMMu4-4ZCz2R5dsdlbxqgHU6UlUFjPaf0GI4BZk_pFPrkpLtxx9-NzxeRwfQuR8JAJakQGRWJaeupnaQrB6CJ6cqWFZJMUR5Bk6uZuaPwL2amYPmtwb6Gyq3GOFrqQN56TMxRk72206bwxPAueacMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDBh8eotIb-UgmXmH360iFIQuyKbXWB-jeOeuB1E9-N_ISY2R7avyeapMcBfHNjEYQa1o_2Bv-ga-Ia_-eJV34rxM0xh6OeeRI5wXUTGwV3xO7W7C8UdDuCmGNzb5qntNRoNAvo4Mn0Po40WlWLGVW0DXXzqWnd-qyyfWdm5o0J6JrnUDO8MGuILuBeLckQtP9377SVS2k9MiSwQzYoRwdyss00ubybMzTUa9EIJCf0c2il9wz9_fCSJlkB6MI5w53oclxDltwpn6ZfRl6-QmJ6yJlRY7ouLlPN0wkuf61BSO1Go3TNYSeWe4-cL_De6bCMGKt4KrBCXw5pDxQ38uQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=J1WhDv1Tcrj62tZm6VL4kbixyW48741ImYLWe_2Xc-ZnyJltke15S1pEmO_h7DtYdImZ84oVdyaMIdUUPhPgZLxXJ77-fG8wK810NTEioth_9QPlSbvwTivEnOA8gYjKHHPcTwYI31egGt5kCifIbmH2MR2VDDfe-r0REhPX1EZl8L7Yw0TqHrsMPJGj2qFx8rmE3jpEm-Dt8YGEjOpRWUw2FsC4RzERrdb1Gb5IPaj9nOexGbu64OSAOPqvvjW-TCkJEg_TmikopTbAB5Q6EoLkoph1o8nHSsqaTPuWfojH0WJ-mx4EjYr1BOm-r9xlj_nP-OIpcYy59BVXJ1slgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=J1WhDv1Tcrj62tZm6VL4kbixyW48741ImYLWe_2Xc-ZnyJltke15S1pEmO_h7DtYdImZ84oVdyaMIdUUPhPgZLxXJ77-fG8wK810NTEioth_9QPlSbvwTivEnOA8gYjKHHPcTwYI31egGt5kCifIbmH2MR2VDDfe-r0REhPX1EZl8L7Yw0TqHrsMPJGj2qFx8rmE3jpEm-Dt8YGEjOpRWUw2FsC4RzERrdb1Gb5IPaj9nOexGbu64OSAOPqvvjW-TCkJEg_TmikopTbAB5Q6EoLkoph1o8nHSsqaTPuWfojH0WJ-mx4EjYr1BOm-r9xlj_nP-OIpcYy59BVXJ1slgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaaiy1Qd0oUUDKdXIYs4PQfnxL0beWeJeWwmx-bND9FnA66c1qSJ8VvpVeFk7o5kgDF_wj_oUmQFxoVn1G6m6YsNei5kmvu_Tz7IS7daUS1WZmZ9I4qFFn5p6eQqdMUFqk1tCwuy-JdBsZf-7TLizNMszdMYvYl-uC7rWUGUPbmiKdMi_JzghYWxjQE6U80zv2_kG9pxBYrX9sSK4gA8ccLZs1_QccswulzCqAulPupcQBsxDVGExT7SX4bPWra1YUTOR2TGCJclkmqxweK-Fzbe2mg_ZBbuN_V7Qw2hjiKVy9XO-iY9GR3x1OgKqT2fUwY9aRzRdNLPQUCkDYpAqE_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaaiy1Qd0oUUDKdXIYs4PQfnxL0beWeJeWwmx-bND9FnA66c1qSJ8VvpVeFk7o5kgDF_wj_oUmQFxoVn1G6m6YsNei5kmvu_Tz7IS7daUS1WZmZ9I4qFFn5p6eQqdMUFqk1tCwuy-JdBsZf-7TLizNMszdMYvYl-uC7rWUGUPbmiKdMi_JzghYWxjQE6U80zv2_kG9pxBYrX9sSK4gA8ccLZs1_QccswulzCqAulPupcQBsxDVGExT7SX4bPWra1YUTOR2TGCJclkmqxweK-Fzbe2mg_ZBbuN_V7Qw2hjiKVy9XO-iY9GR3x1OgKqT2fUwY9aRzRdNLPQUCkDYpAqE_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=VYmOUnKtbgR8aXMpuiOQdQCLJUJvl6cpB54dHCRVRDxy4v40BEbpIdCeQJy9NUbItGth9usdeP-pqZKPy6zFEYidOv6x0-lvdhRsn8CYTzKZLzdDIPrOG_CNPJVTyjjRCa4Vky-ZFi344O9AEgiwnZy8320OeGOaOb-QUBUwK8bdbF8rScb0oboflzwi_J1OG7-jcFMs17eGTSfm_gQRJrICNV3-AOSTsJFge3bCcuKX1Yt2uHNOG73dQEmuiDeKbRnsyFCQ_z4dyPGHvuEXXoLMKbZAf9zz-YP3rcLFH0WQP3dtxKJxcx3tubjg6-YcgprKQT-NI-eeDOWTVV4OTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=VYmOUnKtbgR8aXMpuiOQdQCLJUJvl6cpB54dHCRVRDxy4v40BEbpIdCeQJy9NUbItGth9usdeP-pqZKPy6zFEYidOv6x0-lvdhRsn8CYTzKZLzdDIPrOG_CNPJVTyjjRCa4Vky-ZFi344O9AEgiwnZy8320OeGOaOb-QUBUwK8bdbF8rScb0oboflzwi_J1OG7-jcFMs17eGTSfm_gQRJrICNV3-AOSTsJFge3bCcuKX1Yt2uHNOG73dQEmuiDeKbRnsyFCQ_z4dyPGHvuEXXoLMKbZAf9zz-YP3rcLFH0WQP3dtxKJxcx3tubjg6-YcgprKQT-NI-eeDOWTVV4OTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBqRRWfVxjMMm6YaiMdD5RjTQ_2SG8o7QFld29ldzZ5J1wkiGgtmUeOj2iym1nUoVCbozKnvE1bfVY9iheiDi4Cey8jkdPLhJC8S0N50TpeCz5W8MoXOyNAe8cS2-NpF3zKDvFX6wIwyzg2DjvH6Ma1L-q9o46Gc8RLg_IyvMV6QlJm8elI3hGugukG6j6Qcu_71MuPWyKsqoRfBOeHyoZPgIsXu7SHyDdk1Sbuqdlg4ADI7VcId-DGhtQldhvPNLKN2gYD4c2Qe_liBTsFv54Lc6m5Etx3hBMZLy39GOCsS9g0ZQNaJDeOzP58-aKO6NI94uctEHBOGw_dE0kwEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTgCpcHT_fai0LTv3yTLT6i2gpGyieQBZI53a2rZPEnsUgFF_y0bh3rP2_0S6-IXi2VXK-RDwgNU3ApiZk79BNUl9ZMev2i77fT436jHiKIssQ4--1CXqKkr214IC8ZJ5vLgb_kpgzzDS-77qLzx0b8teSkZgYc8HHzv3_qEymjCrMb_A6OXhoTtcD0wkSVWpGnl88uasucY_JJldvsb8eTrD9k3f4GO6ZYA6pcbI7zBqTf4MHAci_FHZwPiUG0dkPAkhtoW2yesqt-fxUwsfrZm2Vt7ysVBAq9_eIgMD35byyarRaxsmQLhOn9mQATOVuGusxtr0cUwDaenaGqFjFMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTgCpcHT_fai0LTv3yTLT6i2gpGyieQBZI53a2rZPEnsUgFF_y0bh3rP2_0S6-IXi2VXK-RDwgNU3ApiZk79BNUl9ZMev2i77fT436jHiKIssQ4--1CXqKkr214IC8ZJ5vLgb_kpgzzDS-77qLzx0b8teSkZgYc8HHzv3_qEymjCrMb_A6OXhoTtcD0wkSVWpGnl88uasucY_JJldvsb8eTrD9k3f4GO6ZYA6pcbI7zBqTf4MHAci_FHZwPiUG0dkPAkhtoW2yesqt-fxUwsfrZm2Vt7ysVBAq9_eIgMD35byyarRaxsmQLhOn9mQATOVuGusxtr0cUwDaenaGqFjFMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw72lAUDrsaaK9XMpXU5JTYSwU4O0WUA_XIUgiaNNd6zgz7rHf2j793I9wRkSwgDExCtHZvSEfcmTBDelRfPm2ogbTAdktvGaSu53d5FVVeniAVcJ2q_6bY2R1ckd3C_gEqmhJMFknMqh6unmUOn7BmSDIEe4aiOEaRydC5wuesAqhgiQv4wJ_UJ19Izmy-jc3sEYaswTf51S7XgG9K9lT3zmLXy9fBrr1goF_I94etnQ2eK1-OO_7HO2k-6xpi_UUFTULxV6k1f4nOW9bu_SWqItXuXHmvDg9rncEx_EheHiUBEXLYMZWuZI7-mHuxylsHos24BG0zddKRO8VFR7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=fLgxrIfq4WEExQhDE7ezjYNsUHmcoB7zZPwK2_ThZtSMb-XLfK1Vet5veh6aFOqnccj0mAmuMzUP9H3jZC7NeMxQVKj1_utCXKKYgDJ0fLy1_9EwhpVawxTjkmVEEi2Mi9Ip5HmojvQtAuJh1r5zJV8qy2C9F8batkxdBCiwr5vk0DHvJKYStD8an3i-sF2AeWFqNS10N61_Pa_mPDTzA6HYso8PCzuZ_jyqxxc5kHLDKKrz5I_3SOoBNCE1cN9hDhg9FaTbIaRnfr52NN45_2tYfPtWj3FRoMYuN46ay_uATsOiNjPhPZKO7SKpZvLCs266TWfmDLkzz5drJnj6uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=fLgxrIfq4WEExQhDE7ezjYNsUHmcoB7zZPwK2_ThZtSMb-XLfK1Vet5veh6aFOqnccj0mAmuMzUP9H3jZC7NeMxQVKj1_utCXKKYgDJ0fLy1_9EwhpVawxTjkmVEEi2Mi9Ip5HmojvQtAuJh1r5zJV8qy2C9F8batkxdBCiwr5vk0DHvJKYStD8an3i-sF2AeWFqNS10N61_Pa_mPDTzA6HYso8PCzuZ_jyqxxc5kHLDKKrz5I_3SOoBNCE1cN9hDhg9FaTbIaRnfr52NN45_2tYfPtWj3FRoMYuN46ay_uATsOiNjPhPZKO7SKpZvLCs266TWfmDLkzz5drJnj6uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=mtAIkbaGz2Bjg8PYqVYSpg2Ypzk0wRhKMzJp1W7vDfr9L3hNesA4vd2B5pViWXdeE5JiVnU1N-OZCJfgx1Dw8l85D3hkzd0hkANTze-cAEgaXisbsyFUrukjpFscHuHI_Flmiwyd0ujfz0OCowXe76D6IzLzawGTekPuJoiUjoBGLB_6_c9GYjVUj3wtAYntqh3vCRR1bRxma1G7u4BtSXxy62PgdHxKJpaceYbXO8e59dwamFW21RrZ0m7SQxh_M4MHkTclRG7aQYsQMI63RdZKEsoHQeYhNhTuVZ21j9ja42SLQhiPqSd4thk3hDXuboDLastJ94U3txPk3t7_uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=mtAIkbaGz2Bjg8PYqVYSpg2Ypzk0wRhKMzJp1W7vDfr9L3hNesA4vd2B5pViWXdeE5JiVnU1N-OZCJfgx1Dw8l85D3hkzd0hkANTze-cAEgaXisbsyFUrukjpFscHuHI_Flmiwyd0ujfz0OCowXe76D6IzLzawGTekPuJoiUjoBGLB_6_c9GYjVUj3wtAYntqh3vCRR1bRxma1G7u4BtSXxy62PgdHxKJpaceYbXO8e59dwamFW21RrZ0m7SQxh_M4MHkTclRG7aQYsQMI63RdZKEsoHQeYhNhTuVZ21j9ja42SLQhiPqSd4thk3hDXuboDLastJ94U3txPk3t7_uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=jnSU7y3I2M9InACQ0qCjjHCYeFuXJKgvxa64MricnwqHCCkqqfR5UHzVjV5ccFLUdu0UGhSR2Nq9FAQ5mIbSbnk_u3XblPjKzla6_bo7JjrdVFdiYnuXoSNyqQIMJtQuBzGCFpGZARyHd3aJegGhVkANrBg02dWzVRkn0UnjeVkkkDyMl8wC3Hv8rC1R3psKTXFfI4ZbX-8YqPa7JOiT_SL1uwhO5eTih3-iXFQBcJPJINnr3t603tD9jpI_ngUmqnTx6o0Iwa6f6kIoYtFqpcu91fhC2SS7Ur2W9r2ZY_I3gwHiL_oh_GeChsJ9HCA_6fyr3smBZdk4R3qI08jSmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=jnSU7y3I2M9InACQ0qCjjHCYeFuXJKgvxa64MricnwqHCCkqqfR5UHzVjV5ccFLUdu0UGhSR2Nq9FAQ5mIbSbnk_u3XblPjKzla6_bo7JjrdVFdiYnuXoSNyqQIMJtQuBzGCFpGZARyHd3aJegGhVkANrBg02dWzVRkn0UnjeVkkkDyMl8wC3Hv8rC1R3psKTXFfI4ZbX-8YqPa7JOiT_SL1uwhO5eTih3-iXFQBcJPJINnr3t603tD9jpI_ngUmqnTx6o0Iwa6f6kIoYtFqpcu91fhC2SS7Ur2W9r2ZY_I3gwHiL_oh_GeChsJ9HCA_6fyr3smBZdk4R3qI08jSmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9mNYslk_ZKbbnbJ3d7QfdNCJjBPEzky_TIIkh1PggOPc7dtctDETIIZtZvI1JtGA-z9DR-IY3gaf_RZmoG7E6zRgIOnLslZUH4y-DU15zRvIsqO_TYg-xxT0adY_6q4F27sy-cYj9AfF-XHqVs2c3JrVZTPpQtiQW9lGIPwuVkMu3yO-pj7J0pH5exYhIZAEjdElAMKu-4tL_1GeSycM6HjpDSA6SYyB15yNv0ePp4H3kEgTmbMWLLVfQFNbXEGc3yyNs4hEFjBmXCkr3IBKTFzHvzGsZCW2mycAP5TebRT-lCZ9-MRYRmstibMYnHpwHWkoCQd9ZkhSW9YarLDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBVSlpGMrj4Sj3_AHfA8gvmCXqj9Ors__YZUl1UYoaUxCRrc5EGX16-HKUcREE7q-V0kCDL4BJzCJvXAAK9D8lOMgCJ5-Z6cEKza9AtzrmS4miuP6RGAhSqtm4tqQRWe4FxBzBI9hPOpPhMrr7LR0vOLlZnWdx6K8g1k58dok2iQP34xo-X3FzVp9wuNElgIWif092s7ycOREB5AYD_UrOhdoBHRLOVeqLUk8H8rZb6mrIN12iQSr4771NfI07hG1w1UdWyfpJXFxKoAOo0aGm19f3-lHx6dnQPiIwWCd-ZAWwAdlmrFQvZmM7kQOQhLnA2RS2DcU0gQtNL2e4bqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=I7cYfXUcSJooA_R_V5lAzta7ln3keS3o1IBp7q5I6E3oRJKGScCSLda-RdhJQw81KY7rux81kLW8hS4kgKMUZebx7-ae66epzpJjlKCcbB4RYHp_cZNfpbrsXFbER9kSkWvX0lEmOrcfG38LnKf9S_ofROxdKM6xYzAp62cuTsvyF7rPFBWvNk4oK7PaQpsv0wYkmV5hb0hoXlvBWLLK2bRjxR5m3SfZNVuEWMw51lOZst7H17ynIYzsFmTTjOWTWcc5apD2SPTrkiy5G8LZiymASch8ZC_3wwaCUbJ9rJgP6wGj-jWjzXAaNoLCr0HDoIjAPEE6EVqEejpFdeVVgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=I7cYfXUcSJooA_R_V5lAzta7ln3keS3o1IBp7q5I6E3oRJKGScCSLda-RdhJQw81KY7rux81kLW8hS4kgKMUZebx7-ae66epzpJjlKCcbB4RYHp_cZNfpbrsXFbER9kSkWvX0lEmOrcfG38LnKf9S_ofROxdKM6xYzAp62cuTsvyF7rPFBWvNk4oK7PaQpsv0wYkmV5hb0hoXlvBWLLK2bRjxR5m3SfZNVuEWMw51lOZst7H17ynIYzsFmTTjOWTWcc5apD2SPTrkiy5G8LZiymASch8ZC_3wwaCUbJ9rJgP6wGj-jWjzXAaNoLCr0HDoIjAPEE6EVqEejpFdeVVgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qi8ZpbYyZODdHn9fRqreNaDAFq_lAD3hdgdRc_k3UkkMs39Jjr5n0mtF93psR35DFljHdYtf_Z9i-3HbiNQT4XLHd2Gzr6ubp0UOaXBvSdUy9ZEEiQoPVmT4x1PCf2pe6JOz5OGpwmVYifSuvquaElAnL8c07njPPXMgDO39TBtKJelenALK2BcMl3KIHviGJ2FSMLVC3beCDNID2AWOqkgApVhJYa0iUcCPpGHtGuzpsjkL6Yf_2qgsh-nWgVQv6UuXme1HqbXb2uq_fL6TWqPFdRCZF4PmjmhE88DeXrdqkrqgv3yqITtFM4xFobZU27NU8va78m2x4josj9KJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4M59Cxx8RBGBZ506mQDlnGM5NRHebhmkxBiN1zgOuRBhFRin7B3Gx7X_CYgIDKZ6885NNHajMPp4WDPQxpfLUyH9oYMFWci6lq-s1gOdn-iaF3iGh_WaWIftN3Y1UasKD-AxLijIxGVBAChPlob34z06jIcBGXwDQkdLTSVZSniacAPpQMM7CzFZTC5Ol4AU57Vti0YfAdP00gPUpvnz2xWrIrO5UJdJggnNnU_LBfDvbQZbjEnfbu7qzTW3DCDwkq-mBY7fEUwj4YR7vFgTbvuZCiCJMLxNzDIqDUHUr3vWcC0AaVKlRxduDg5ykkJor62LcLDuQvDWm2xdNRwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=FM7Omu5MMyocVAWsjFk0BZZ5hURACtoQShiWE5O3J_lyeopHCnFY2CbnWeRs_48F5r3tLwghe30lrBsYDynrPumDJ0tSe1y9PkAX8oI1D29yt8WfvRGCWe6TI0QhyOXOXc3RwLxx1e1Yzf_B0zhakHAg54axA9yrV4IOith2Ap2zgiLF6BC2rXXlZbjy86aGQkO2NrCXsgfRvgc6cl2Oz4UAyhB-Yuvm2D1_t3uVTnZskSh7tVPhE546NF760fV-BiOVBcts2sr9V6bMuWcR_CLk52oc_maD96mrAI6LrHA8eBcEfTUdJ1946t5_zSAanDVfsNV7mpTV3mOYQQpMX30-_6Ud-Rh7qjbbfrPjh3FEXS1TvazRFFIErY_OToAq3B3DTcCsYMEO7D7NhjZUm-OME_p2lR8BFm3RctNXwPfqD_-wrF9giK-L4-OKVcuWI5WgGa0e3AQ-MbgRSCu2EJYbS4j5AF_OQTJOfBvIkJLlA2ROmZk-p0qaiV3rYuJPHYjjT-qLvCQCnVVTvvl-c0iqDRQaIfAeoPhUb5d_i7jGmu5Ip-w3s_jznXYg8eWMmWutSAuaZewm7byrHy4GlniElFMb5Cqrgd_dpNBhcvlL8agozPkiDnBi_CmLZm_Dju-ePFVmbVVfbnIvfBHaFlAOZmSidOwvyCRv85POSsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=FM7Omu5MMyocVAWsjFk0BZZ5hURACtoQShiWE5O3J_lyeopHCnFY2CbnWeRs_48F5r3tLwghe30lrBsYDynrPumDJ0tSe1y9PkAX8oI1D29yt8WfvRGCWe6TI0QhyOXOXc3RwLxx1e1Yzf_B0zhakHAg54axA9yrV4IOith2Ap2zgiLF6BC2rXXlZbjy86aGQkO2NrCXsgfRvgc6cl2Oz4UAyhB-Yuvm2D1_t3uVTnZskSh7tVPhE546NF760fV-BiOVBcts2sr9V6bMuWcR_CLk52oc_maD96mrAI6LrHA8eBcEfTUdJ1946t5_zSAanDVfsNV7mpTV3mOYQQpMX30-_6Ud-Rh7qjbbfrPjh3FEXS1TvazRFFIErY_OToAq3B3DTcCsYMEO7D7NhjZUm-OME_p2lR8BFm3RctNXwPfqD_-wrF9giK-L4-OKVcuWI5WgGa0e3AQ-MbgRSCu2EJYbS4j5AF_OQTJOfBvIkJLlA2ROmZk-p0qaiV3rYuJPHYjjT-qLvCQCnVVTvvl-c0iqDRQaIfAeoPhUb5d_i7jGmu5Ip-w3s_jznXYg8eWMmWutSAuaZewm7byrHy4GlniElFMb5Cqrgd_dpNBhcvlL8agozPkiDnBi_CmLZm_Dju-ePFVmbVVfbnIvfBHaFlAOZmSidOwvyCRv85POSsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToMRkjrNb5x_NpAS4Nb7IT-RcpATjg8wBIgIhMO6QC6Oyt-pdCRXl09nXu2ppBMWcl5wpbnWAcy8nTHqtLx_ni_6sUHVNzBbpk2-fk2_xP_g94KhQSmn6Fi3ba7dAY-syzbCYw5JvM1JHwP6uxZnGBGEGgs6-zqFGt1bB0IHAWf_GCR7mwqfen_XEMIN5-6I-lEm3a759eC2ka4JNvxVzpBaOMLo5P0Mv5RdJ_c8r-Rl4Bz5EDcO3S3jdoukhIkmnZ9O8yH96qVQc3d9mpTYkQVMAIkPLsMOG9DDOB_2ZnsZFAr8hll36oVvuFk71c27WMztbLaseqRcFqBW7YnTTGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToMRkjrNb5x_NpAS4Nb7IT-RcpATjg8wBIgIhMO6QC6Oyt-pdCRXl09nXu2ppBMWcl5wpbnWAcy8nTHqtLx_ni_6sUHVNzBbpk2-fk2_xP_g94KhQSmn6Fi3ba7dAY-syzbCYw5JvM1JHwP6uxZnGBGEGgs6-zqFGt1bB0IHAWf_GCR7mwqfen_XEMIN5-6I-lEm3a759eC2ka4JNvxVzpBaOMLo5P0Mv5RdJ_c8r-Rl4Bz5EDcO3S3jdoukhIkmnZ9O8yH96qVQc3d9mpTYkQVMAIkPLsMOG9DDOB_2ZnsZFAr8hll36oVvuFk71c27WMztbLaseqRcFqBW7YnTTGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=RLAYjO8sgtD3cP3h3b3TbG1YZGG6qKWz4Yd8paKSef-Gcq4lQUGkEnLckcIULxBvQ8nqmf7WrLTDD703JH8RY5U3_XFoNpRflVUySzfYP8ppMTNIe1QIZJgaQosT3MwWxWD_V3ujAkLyvmcT_IoCGAvMfwSLGf7DJ3HChcYA4FhylHLcI308sPpt0_k76CQpXosSyk8Qd5OgV546mwESHUnJO6zhUTVRzHYEhz4O8siGkreHSPC7dcXnguXNugiicH6rZtUW1CfLxKyXHq_ktcc7uxZURzUGTPmV_JN02ObRJ0IhMb37A0uMaUXMHKE7cgP0lTiu2WjVssqYbBM52Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=RLAYjO8sgtD3cP3h3b3TbG1YZGG6qKWz4Yd8paKSef-Gcq4lQUGkEnLckcIULxBvQ8nqmf7WrLTDD703JH8RY5U3_XFoNpRflVUySzfYP8ppMTNIe1QIZJgaQosT3MwWxWD_V3ujAkLyvmcT_IoCGAvMfwSLGf7DJ3HChcYA4FhylHLcI308sPpt0_k76CQpXosSyk8Qd5OgV546mwESHUnJO6zhUTVRzHYEhz4O8siGkreHSPC7dcXnguXNugiicH6rZtUW1CfLxKyXHq_ktcc7uxZURzUGTPmV_JN02ObRJ0IhMb37A0uMaUXMHKE7cgP0lTiu2WjVssqYbBM52Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=XbvQdXkznHK4AzpRVJOXRcBqJ_ILI-m2op35wfYBaOn_Kf34bQmGVeGKIwEfrQgqJPomNT2ZkNyP25KDJ8qdipcmnDWHd3qiVuDnb1f4ah1Wj4F4F6VlaRUSzFF-2eECikmNbRvsF7QeE8XuhYwm2gUVK4RcC2MG1m8NOluM6gFl2uOO89L73JVNquILAUaoPMRu3OpaLV8Xj0yIJ8NTpTUKdThzdMw3lTn55cHSNpDijBAKSQfbf1asFLf5KbPrI2_bcM-HANoAykGWchNEkriGp6GYCpmR8_dIY-Wf5gt1AKVGd4zR2uNSxqjaV-Zs6pdlgsZ_WLkDhTsQPhBBag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=XbvQdXkznHK4AzpRVJOXRcBqJ_ILI-m2op35wfYBaOn_Kf34bQmGVeGKIwEfrQgqJPomNT2ZkNyP25KDJ8qdipcmnDWHd3qiVuDnb1f4ah1Wj4F4F6VlaRUSzFF-2eECikmNbRvsF7QeE8XuhYwm2gUVK4RcC2MG1m8NOluM6gFl2uOO89L73JVNquILAUaoPMRu3OpaLV8Xj0yIJ8NTpTUKdThzdMw3lTn55cHSNpDijBAKSQfbf1asFLf5KbPrI2_bcM-HANoAykGWchNEkriGp6GYCpmR8_dIY-Wf5gt1AKVGd4zR2uNSxqjaV-Zs6pdlgsZ_WLkDhTsQPhBBag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/addmfPwvvaekb-U0KrBwGfEaFKFIHZR2Y5uxgAUociVwTm6Bq3YGQZXcLX3tvIczPYYpBnYKiBaD09WZAVFmaXnoORPGoaa51TZAWLbJKzvL2cBeeAD2Xjn2vBbi4mSDhxV3lHvElV6o_SlUtmtLs-P7mM7z1x-oS4UAEyaU68jnUpntmlrNFHICPki-rqGd5X0xtUydAsz3x0xkhhaQioNrfH7c9ajKw2L77uJx7tC2ZgN-EYpjioJ18Jx3IDODjP9X9H1UNMLaRxvdq1jDXBF0kFNf1NNqQfQrxC924yiGXy1DXXG0bwLS3qhxyXteRvk5_gYEDYY2aJTB2BoFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCs9SyV1klAlSXHidpulXay7cKAoTS3mygKhI9eS2EL26Wz4OSyFjMzx-HGUuTrlcWFzbb1aBzQWyPsQYY7oIUXigwFdt09omOwjQM3ZHTZpZXVAEB3psnbOCHjIruHDLIDY9VUT_-MZT8fqX3JjLmwBI6sweYonwG4WCO7oQEUYyr27FeonhKeX3tcBhs6lcUH9chYKX1PlvFJaTm9Ry6ujC3jgJvsMDhwwCbTALik7Ucuj-knuP9N-IKIjsvsnLlUZJ8ISzC8dsCvV5Mq9645lKx2t6OwYoLlyUZfZQ3wM3sAT3yFr_e-U3EIQ3IW-ch-zQG85NiGmevEPc1KdbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiZzAoUUwAXYszwW9RiWulpuQlG4xwvxszcG3s1wJ-n9cTY4G67Rrd2g5saWKoVAc7jOpO7H276HvAYmFyneTFqN-V2MgJcik4YIittNGY3X1NXA_en3kHYccnlD2h_qGs0A63D49trjnTA6FDspiuz2iMytNhI0S7m9G1h4QnuHpFUWLmSbgnU6LGKt_grb0OK_XB-dUnKZnCUcLeNTwYIvaBc1YLB1Z2idFyW-BmQvffvBffByukJNyPJqEOyjDT_4GKBcILrYyWIPLAYBqhe4Zt6XtIWNgAb9vka7pSNbjxBtBEpdct14IpdrmhR9ARy6ZGXeOgUdCrmzjYqczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHHHDRqudYKmAakCou6BgyWnJVMHcC_7lHGBXhzQq5dNC-1ZGhKOx-oHXlA1iPV687Sfn_Yievn0QaOoBMn00bTB4KLeSxd2CXK_MuI03kA_iSegA9fbBL_-G5QrOg-b0Qm9QqX-F3W4CTxS3ETWvwYEX3QnAhzX8FQ_igAWt2anSLKSi9ofNz5rBGpfwH-qeYXoGg5MRq7reYsH61nKrmPqrcWyYQLF7pujiVyvGxRnGbhY4qYKO6jLfkgB8ZB_5_wijnVGotwTKf4NUcCqmKK9D9CC_44sVUmtVZsBhLQqLWJjg3RXvGtf0iVTzv9boAjwoA7kRwukYFjTWEzf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_3mjLbICdcQmx4dTa4Xuzl-rHSfpJTQUe9jzvBQBl6iy7T1Bp4hyecD2SCivJB-0-0xnMH8D0qzgYnWMhN_skLrW4-YBtcEeQDm8dBfzCj6YrwaVHu2HgIXNyAyhwLwL4anWfq5ziGIINuyHuODQuGtzGaJXSZOcS1anPfRGwdjg8ks6MJGX4xqVjDmGqRPESYv_B0EeMJzApuhMrkI43KgfqxdD9V_0rIKESF0eddR_LgwVvJJEfD3pU4cVroeH4dc3DFLhSt51wGdG-v4tKlxTRuhvG8eC6HQD7Lv9Kae3uj5Et-slTWwUN2wWdx6cSpikcC-o7Gxqr1LlGjDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=CCvXh44z7Sb5hnmF_s20uAnopNmTZE4ep8nUbozgd5zevugsosW1kbEZ1t9LaUSsPszzVAAAJqnzpU_6ek9MIbjjLP0TEhR9QadVmTS_dplyY5BFontXGJxiY3uPa13ABgrgGGtd4aizo5jbPI-0s2yQ8lBSUR9m_546yC9FRqpxwv7ewtt0n7P9BjGE-Duht9qnqBX2ucELtc5oWW_HLu2a_Rtq0mGZh0CmPhqaf7VDBTgvNWsLU8QTMAFBzyIeZNMrPkdIN2Cmmkz_kv0TXow43bAsYHR5UgRuRcrg47oXv8_oSoXgVFcssCXYhJpkvR_jEjzGMbBeJlBfJYwY1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=CCvXh44z7Sb5hnmF_s20uAnopNmTZE4ep8nUbozgd5zevugsosW1kbEZ1t9LaUSsPszzVAAAJqnzpU_6ek9MIbjjLP0TEhR9QadVmTS_dplyY5BFontXGJxiY3uPa13ABgrgGGtd4aizo5jbPI-0s2yQ8lBSUR9m_546yC9FRqpxwv7ewtt0n7P9BjGE-Duht9qnqBX2ucELtc5oWW_HLu2a_Rtq0mGZh0CmPhqaf7VDBTgvNWsLU8QTMAFBzyIeZNMrPkdIN2Cmmkz_kv0TXow43bAsYHR5UgRuRcrg47oXv8_oSoXgVFcssCXYhJpkvR_jEjzGMbBeJlBfJYwY1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=mxLcqcg16QwtjqUYiLkeT3eE0RIly5K0I-zQwekD9xd_EUFCHmvYggwkFzME4As113ytfgjMFQfd_EZG2YEDSBCUJ0hH4_4uCickiRZS2w3_Pb2yupxUzaS1wOqPiJf0Ta6cczROtMI0DAMRtMI7o1Aerj4R4R_3Ba96hr4jysrx3GJsMzeVGMxGHK4ovr68yM6b8jV-WMcaiAv4iTHcPRb-MgIHgYQOnd9-O0gErImMOgqF5CgvYGPUCPI0MJ7_CDM8Fb5MpEkWOuJRgb7l65O_ib8wfWkZF9Gp2UxSlIlJxK2wMYJ8fg8P6CwnxqR4lyXWJ7uQtoPKnefn8WS4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=mxLcqcg16QwtjqUYiLkeT3eE0RIly5K0I-zQwekD9xd_EUFCHmvYggwkFzME4As113ytfgjMFQfd_EZG2YEDSBCUJ0hH4_4uCickiRZS2w3_Pb2yupxUzaS1wOqPiJf0Ta6cczROtMI0DAMRtMI7o1Aerj4R4R_3Ba96hr4jysrx3GJsMzeVGMxGHK4ovr68yM6b8jV-WMcaiAv4iTHcPRb-MgIHgYQOnd9-O0gErImMOgqF5CgvYGPUCPI0MJ7_CDM8Fb5MpEkWOuJRgb7l65O_ib8wfWkZF9Gp2UxSlIlJxK2wMYJ8fg8P6CwnxqR4lyXWJ7uQtoPKnefn8WS4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puWVCKaFzistYuofv327AvOflu5tv7RZ5Wti2orP9ZgsRdGMvpemmCKFTlpaZPDvCAAR4Yw3XEGsvIWIx-pzM1GCgWmQy_R3YGtcTDexZCNAbLbBzIhZGxl1XOqF1QhjEE_FcjxFNo-6Ne6FmrB8i8O-1Hkbh2jrvMXNmaCORAlaavY4Sfo9_D0hcQDE-NBH4hSHZ1uxCeqAvm1KBDARORScrw5DCQZrhlJFIzYKNK7aWND3bXH1QB9VbRI7jBNgiNR1Qp4gDgLx9M0NlgOSqW2auY8bDCp3_rZwaK4cZBXyYpGUyGHAs8ObJDnYqkxi9OXha0KbW-P82sUsEapkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEe4FUOcgw2PsXSJj08SFSs9Bk0k6u0YrlHipps4Wulesptd6HakFaCOtCmlz8xKzO-ZSNqAagorCNh0_u1Wm9MPSzmECICQMed63ibl0evOaQv3IOqzPs5wDigM_jwPQ_klc4zg7r2r3CjTNz1rmeJD_nWaYNgqRWFnLFef_5EeaYyq3rsc-eTucW-W-DdHEFojx-TQ0NXTGGUyB0u-1ITG80S7Moera5qps7WR-LmQyUm2rzsgcZ0x0IlLGZ5c3gwxzqo1nsJby4HVGGWHrIjKjzVlNkK_gVkH-uNK89pM6a7LtiWCqqZ_8dXueLfCvSLD4ZH3kqnvH5Q_4jmUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=jzek1tYpdYudQfibzRy3nhDregJyZBhUzF5dGxupAd5p7PcoebUPNCoul73BIXb7N1ZYnYK7Dz2dmgZYJS5-0wx7Qyp55Y9vDDt9ZBCJexGa1m17s5HBzbr-EL_0mdfnJMWFk0iDZ6L76dAK0rIQaC08DtQlAPOFZxI1z_TwCjt4Y4RJi3nWU6Dr_nRxRlGn1Jc0RbwNWMJ1yUYhezx1AFvR2-3RdZZS_kZErF7nns34t4cPPOv-k4Dq1LdIQeuWmJ-_8xJGVqE4pGUc2QpgiIySWuGLKtHKa6fhQrGeeA_wio5tIuMe5p1dJsnbKQSS7LPBQNmcWYMSfCwtMk8Msw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=jzek1tYpdYudQfibzRy3nhDregJyZBhUzF5dGxupAd5p7PcoebUPNCoul73BIXb7N1ZYnYK7Dz2dmgZYJS5-0wx7Qyp55Y9vDDt9ZBCJexGa1m17s5HBzbr-EL_0mdfnJMWFk0iDZ6L76dAK0rIQaC08DtQlAPOFZxI1z_TwCjt4Y4RJi3nWU6Dr_nRxRlGn1Jc0RbwNWMJ1yUYhezx1AFvR2-3RdZZS_kZErF7nns34t4cPPOv-k4Dq1LdIQeuWmJ-_8xJGVqE4pGUc2QpgiIySWuGLKtHKa6fhQrGeeA_wio5tIuMe5p1dJsnbKQSS7LPBQNmcWYMSfCwtMk8Msw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=wAoSZlPksWfQnvuCMTG6VgoV4IX-QZ33wgCg29_1M-rIJucxnGYQgq-fAG7Th48fRBXgDYbjJT1ivYmhhDov3CGfA197SUAnKRVim1uXTeGvxzt_DoWWYjA1js3p-e5RlDlvLpxP0dBaW5Dm2Vqh-EXyE_MXwOJ_SzOCPElooNmLPX0-Cfg4AMZEkdZYH6gUuOxho90x_y8rKBklXWyGQFriH9ob3yMay-qlbNe-1Ort4V5ONLmpviN7sI0gky06gLq96dc0I8WPqGAmCfZ1GO1f9TpP6D7o00NJxooGujX8xM3eMFphWpom5E49nx2K9XPhhNEtvCOXS5o7qlRl1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=wAoSZlPksWfQnvuCMTG6VgoV4IX-QZ33wgCg29_1M-rIJucxnGYQgq-fAG7Th48fRBXgDYbjJT1ivYmhhDov3CGfA197SUAnKRVim1uXTeGvxzt_DoWWYjA1js3p-e5RlDlvLpxP0dBaW5Dm2Vqh-EXyE_MXwOJ_SzOCPElooNmLPX0-Cfg4AMZEkdZYH6gUuOxho90x_y8rKBklXWyGQFriH9ob3yMay-qlbNe-1Ort4V5ONLmpviN7sI0gky06gLq96dc0I8WPqGAmCfZ1GO1f9TpP6D7o00NJxooGujX8xM3eMFphWpom5E49nx2K9XPhhNEtvCOXS5o7qlRl1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p15AF-E-W0Kj17m-Ra_KppQUUrCEetahSG5QZ_fVclVS5uTwsCMdjDjnapgmyZwy_wAlKjXl9HKuotYUbHDnFFbTdALTPRBZK-6xKPHXIxA-J8ACN0vHJgLKDDYsbv3LuLxfnxFn72gk9cuf33dpYvb2ApZ-I9w_21P0kLPgcSmf1TvaUu4WlN7CZLTpy-8frqskmuE5a6USYx0_J0Pqvt7u-djJFxIO7ZYK90CpRjGks0TbXjZdXhsekMLKLfK69Wba5wtCRdx4AamuHE_KIA7mRhNNGAf0ZDmio4MEMZwbILjhCeD2kDi2FipDHq--nlNnP1DMvDH0y6KUlm5vAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njtD1yxuf_FLlKYMHRTPiTVUQHvfTUjEkJWJA3xKrg4hT3VXGlf7k7k57kbhHgWNUWhaNjq5a72G3DyaT23l6ojAI68Ib2m3wK6x00eR0nmc8g61sOd3P_eworFB1LK9MzluxaKZWJssVBeuGACT0RSFViSfvYsy5HshNSRGXBKXV433heN4_LV8mdE05fVQA9eeXleDE_atnb_1XdUJqbX1_XsBWK1BUeylK9EzW80ApHB0DAzwyGAAWQ49zKsjZGFi2lYNeEpsBF-V_QLQvlU0v6E-HIEoYUqKn_5nWnKZoAk7-FYbRxcvi9xdZicH63dCgtfNUV37uhGCVu-ZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Udhn4849vwsA-_plmyDVgaMJKJyec8cqbbSxmXPbkCHgkcVsxK_WG4GVB-EL4018T58UrycatThtMVTH6MaC0LK2kVpuZFsJ5CYZgVRn7A53B1AYjGI79tqEvPYPk72IG9VCQDPc9jbMtz0u-9UENdL9G4VezTJ5wFy8MtkMYy8h8DFGTJVhw1StMsnKqjHPfX_Wy-Be-Ifo34K2HfBpckpYKh8A5HoGEtWlFt8rvQUZ44Eo0rPtohIBfX5lj8Fuyis09e-lM2rPfoqTJvbwhj1f8JDPR1vjruD6T_4fFWNigBQ1M_c2edGJQsG4IhTvp88vqkn4ybUDmLvwnvJLsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=rE_TPOil3Su51qQkkA05V7grcCQT4yKg2TTOOQ09MpkP-1xzAutfMiTh16PuwlGMxbzKXpgp6W_1xIAfTe9HCWLdILe4R3-4p_CMfBrlY6fJn282l8ET8eVVyF0ysNIx3Ka-kH3ppsyMR4O1uoIKdUI3fjrgUXJ3FbSPckI4Yg6JppAGXwBcyjq_qD_VNAto0tY7Im0mNPTNppiJfD5USHOga6IFWnW41NdwYurv9WAo33De5E8AZh4rn_gANLCY9y-pgLAb1SWkbMPw7GLIuXYztusllQzUlRDOVgA0OtJMvcksWZfO-6PAaR7cLKTnQWDaO8XozWUhNdHTgBoWkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=rE_TPOil3Su51qQkkA05V7grcCQT4yKg2TTOOQ09MpkP-1xzAutfMiTh16PuwlGMxbzKXpgp6W_1xIAfTe9HCWLdILe4R3-4p_CMfBrlY6fJn282l8ET8eVVyF0ysNIx3Ka-kH3ppsyMR4O1uoIKdUI3fjrgUXJ3FbSPckI4Yg6JppAGXwBcyjq_qD_VNAto0tY7Im0mNPTNppiJfD5USHOga6IFWnW41NdwYurv9WAo33De5E8AZh4rn_gANLCY9y-pgLAb1SWkbMPw7GLIuXYztusllQzUlRDOVgA0OtJMvcksWZfO-6PAaR7cLKTnQWDaO8XozWUhNdHTgBoWkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isEN6gS121MbqQ29e8eg9uZ5U67JYsO5f4L_eBEWkEaEIlulbl0o29iTS4_Ek9tYuA-G_tQsumN47Kj1YFaZYdbz5SWvBV3lI_YO76b760aUDg2h356m7nYzc-VTJcQ7P6BjmAbf_1wR44hDQx_IZ5TwkGtJZceDQOkaSIy9Qov02pmFu6eAVIe1mGgoO4eS1q-wX46jq3uVYJT0PwrI0twH2wro2Zkzx8I9RTQ88G6P6VyBl4CaCwsYvvREFFKQ0hrzgxtv85rW7F48Iflgza8uQ_ocEZXlqWcNkkgntSELDYj3fqSZAgFvQyJ1SMCW2_BEdU3T7a0k8IfY6BIwLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpDoC_6CKIe-jVzWIYjG7Csew3n-9VJn5zjbvmQ6jwSVl1MLliik3j3cfvKNbzVns8VjqmzNEvp659-EmmZnos62WgKyScsLIdBTu0X2h_x7gtQu2l5vaNppwd0lxDlbobByjKeV5vVSNTJ0AGaf-9WdCkg9OVCKmwvI9mtyHTF_qqq-33ROzanPY5jCbhrViJ5b6-_RFqndM01EaNbSM1BPZK7rq0YykBwkFs2uYCutEvBsYdbuZ1P1tybINF5l6lpoAY5l81XFqLO8_Dr4AmL3PXdhDdiK-yqWEyR_OihD7RWJdnHfb0ulUZBmI-jVp9nC4O2HDVI00OoYAg71yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmLdIzibfND6t6RUe80rZMIM75YXn1IOBbOohc8t3vlc7UyrbmomEB_Is3I32VcBtQBQC2G6wRPNR9IFe7tx5t23NdngrjCh3D5v_RwgYX786OfopJwCuziOb2Lj957NuvsEZW6yfZEjYREBT29CsHSp4MfSRI467tGDDBr__1vX5y37iCPWXf_O5bQ5vu76ZI1pfdpQlsDQ9inuUggzB1jODfsWUrfOcLVWlCk--rothFxKMGktJheqr1IEhGLa94yujYBVlZtcADnXzIDk4SmZOE7Snx9SqKJgxApja0VMaGaJ88P2AfmC8C2HoGIGnlRyvy7Okmf5Joq2H-D3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMFQ2rKcMKjXkrL6534rJeRTEFobg4Vm19q5-p83JKPG6iNPDowJ02WBmLk4umxc8alTkP-sCF3rN1zHhc-7y1LgLWwKVQucKCvh6D4tHoHYCLGbaY0y3TBk-2GBAvapRyBjNacWl_ZAglnn1KZEuYikPCUpoOJdsL4Ls0xJum7Z_0iDyU1Co9v9RBKubnbGP0Xa7RWX-RVfMsiXzzfxuzgh8AYj_5cV__Tzyi70yIdsuqZT3Uqrk5ZZBZaQEu4tYRdeR7dzwOMI4jVqBsXyy6xo7tZKw4hUCxnvD6CzFsds00dbjwbX3m6vTqxKKeUIGHcL6UWXbaHm7A7MoColEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=W3Z2XLoKyxDo-B6qgur6XSpgS6xDd_UVlMOQt2CJ144sWHK27ZSag7DmfRYo_Fbqz5rp-9eL6UtLypJaCBw-HcKN6Qk6WtaWshK8ZzhHICJEPFs8wy4fpzWwDC-5F-xbphUBL3sHkIeCnbhwSBF7MDil7PXt-U0yLxvn5dSyL3YB0ygkxUtG2WNJn9J_b5v_TTsNiYQqSzs15mIgErej2-wGTVyAIRfwE1MpWYDRxhPWFAsbCPoctlyEjDUWJiqlQrCFWYXKsxQKQl2vqS7hC1ZFdqTuv67dCkIJwaoLYYTKdI7aOKiQGqzSw01rgZAVFn0rc5RUUedMTL8-LQq2aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=W3Z2XLoKyxDo-B6qgur6XSpgS6xDd_UVlMOQt2CJ144sWHK27ZSag7DmfRYo_Fbqz5rp-9eL6UtLypJaCBw-HcKN6Qk6WtaWshK8ZzhHICJEPFs8wy4fpzWwDC-5F-xbphUBL3sHkIeCnbhwSBF7MDil7PXt-U0yLxvn5dSyL3YB0ygkxUtG2WNJn9J_b5v_TTsNiYQqSzs15mIgErej2-wGTVyAIRfwE1MpWYDRxhPWFAsbCPoctlyEjDUWJiqlQrCFWYXKsxQKQl2vqS7hC1ZFdqTuv67dCkIJwaoLYYTKdI7aOKiQGqzSw01rgZAVFn0rc5RUUedMTL8-LQq2aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSIVQKUbpnoQq38PnLq0qiULkkBWthlpnizCyt5a1j2DJ8_6dYIqXuI-Nj4rcShd1y7qNJ9DkBVf-T_oLcKSYdUJI8UAimKcFduPLtK51c9FiCEe-3chWqYbtAL67bh75qfUhXwsYDjx7wxjJ53rbP9d9FcYLyaDLRKIXovztCzVidkMLmLMNpY9JRZ7JIWFT9XXhiu6RbdvO-boC5L9vejqV8Jpm_DNZ0i_ElkcsuZJacWrXL7OzViVTBMqefaNY5V8eM_f9xMNiYv3xnMj7X2ChohNNe3suvtcxitn2ls7RHUXYMpLPUsPVm0MDGcz6yMYvEsvnqSRKLOCPQBo4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzR0NKUWqJdW5Iy5GyeDngk9o9OVIvdu600etOpb8qCHf1gABuCNVZX619SWx2ZOMaUiEnFKO8pvShu1treN4jQzdQJxKXEU_GH-dty-xZjFltRI1731pgHe3FECCw9fbhzBgJfjuhES7nBW1vutrRMbNVGeX5ySGODbT-bLyJOeBSMyQMAjNqh0gIA3HuqSZ_v-xAAlo3k185A0STjOV485mI7O3V0pPn_AKgu_lfQ8pKB3IjlRzxVpEvEu3BM3eh7Cmv9fxtzApz73uXn_T4AF-u6NqWbuyjDlsJprlnScXNSF76hBgIwNYH7kzPBzB-yAU5Flpu6yGG-gaSWiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
