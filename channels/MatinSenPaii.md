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
<img src="https://cdn1.telesco.pe/file/ThMm7mV2Z_JSD2afdUqOSZa_CY9PqEl7FAKX8LaOP1Gvyp2dXAqZsfqJIez1qUswGMC-Uefh4t22gAlZJP00fFxqvVNGeHPlj8ySTfPIEtgphsyaR6fgwf2OHAdj-WrgWLB_a8Rekiek3D77dHQoL3_rxbERTT85EViJbb1VFl0wmS0pkMwZKbjor6u2cShUE-PctwhPN1jZuraBZWY4j7j6YPZyNvX5IWmJ9bqJXUFAw2ILZUg2SzIyY6jEqoaAmJczejkUQTiQMQl95USLF-zpIOfUCBrcDjXtqkXuBI-JwwnPKM2GvR2wuqL_e_nbC7Kl3KSPr39FtbAXPanxlg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 00:41:31</div>
<hr>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k4e44i9h65hH5MLgwyTvI1JFG6RVZdjLDFD3_VZ9OPFNyy2vCV2WNf211fBJpjYAdGFqJ2Pwb056vQeVRfGDt3HC2lTG10bYdNRoTlRQOEnPfdBZB6stzG1ctH6_JbsoQC1k9d7jhrt_-c8XX4iW_35bXCLeS5B-GEplt5PL3D0eetmVNVapsjitpsp37EntQOjMepdPntgSFNskXQCIX5rOSh6Z8VLTUxiyhYEOusy7FsihvzgJRORIm7asiOG23zHnIX4S-mUszb4H27NdQ0ud9vrRf7qMMZ8rgI8rSmnLaoOWQPnsww8Ujqrhpp6P-aDe6Qa_tGyj0A3pEgigSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qjJ87iNYnObTAtAtiSpc1JN9vOIDiGKpKlLUZgdNZ8myb3z_6C3_TAA-1twaXXeuBQzQPoyILnFlp4rIdfKCSaxVMO-ysIu8X7gZxWVt51PSHEXUKr7FMha0aQZ_IA2M2BLRpgdb91i1L7mHZo3X8K10gcTEAv_Qhw99sgJ4ZhZixJzcuU7469Zhitfu0vtIrVYWqlMu--fTUxh278eCwARy7fkr-4-_Ab4AL-2c0Hx7IcAGf1JbQXM-7K4yXVNQDeSa2fO_-zPuxFupNygmiw-XeV9crFZdJ4driCvnYcugrXLUhaGuiMQY96-dgCDP-MrAdyEgIpbbwbovXrZTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g1w16IR3l7g3OS8YaytShZB14lW_urvRacbFM_Mr0Am-i-q8Q_Hj9bnMix_KcsZY8Hawdar_-_SVNOot2WzEPg5UGkJLpk8OteBS4FVUhF9RiNedXqwM1z8hp1X3XXh1XfgO0DEe00xTjPz7zIkg_rMqDj-2exeUgkYDau94bWLPmBUKLyixaRI0zfsWumSf2QSGHJJk0p67lw3QBheYiRxl-cmpnTiUK7Dex3qCrUxrH-ix7dTQ4wTxz0xiBojjsaEOFSosLpmRY8v9zKxJn0mZ6CTFm29GwnGzOIbOY7u7h9I_RsAQqoZMibo_18aSx2pwv9NnB0Y-JsoTZM2B0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rM6php1THA6DQfowHcruDr0Yza-4_w4FGUNqOzwkTL1r8YH-2EBfvDfro5lNj_yJ19_R0B_6fh9KQeqaVbrcSuvpKqKDxOnzBz2NAS0szN8-tAgNubh12gdInMAZf9YMI1aU2Rb2xhiocx9A9AKcMBO00F7xE7IXimD7KLQ0fwN4RwXcB2XhvWivdW7c9ao7nDCi4aBED8Sn93c7voE0uc4cnpf6_M6QfDo8wkgWD8ZAXMzfBNf9N1-vexCSGMcrA8--gQobnpbXt6LPf3oZW1OJTqYR5qXKJpU7dw5vQ1fJz3cqp4ppLs19g1JjIFQrEt8lZDZFLcuP9A7Bil4gHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eahwoSVvIGLdVIZZVjObdjj0mDSma_FY6CugLoC-fMYh4aVXCJKmNXAI47up-kbAutDN-wfHhRYJUq95A2hTrz7RY0YlGcskmMNr6rrUhf4UR8_n_Tr4vXtGzg5NiyV5yx5VTcQADSDGoGTiXqUyPzUEHrDOtoZ0jQ2YNFzeYTeLOqhjJoqSt7KVw4b3Ls7Tr279dxUpyg4oKnrD34C8eu_RpHeGihFMkKSbLdEYZWwH_qNvfm8PUsDeNfAEUVWAEudKwAuCzsafsL874YT6xcTvccCxpNTPUrYXtMJ2L4tQxQGR6CvipDd87wjZLuh7ehQfYz4eyllR9crz3oAHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qFrAO0QOB2yBlo21STeP2qYNilCK3v--VHEjrj-gQfnTqTPz5H20f0oPMuSuiqsoK9AdOQ-Qlle4eycaOiAZKG2_fojcvhRF2xriFlw66jHL4IWyZXZGD4RUbdOKKpSFaBzbNP--SCfKh8B4qz3Uy5n3wCb74rMh7LSm_AIOqrPXu1v5yxu_eYlCwWtdxilaG1DKGMOTp1hgobn1ePOgbwrLRYq9HvyjNhWnbQ3POkNfDCxoI7NfojqqOf7kelWmt0Cn4UURMsJ0giFonkb1qKlcNsLxrYIqHxVWOqac_txnuHVJEui20P2lJAXQdeKdCbUKKjNvoVuJsj7U11YLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mZHTWSswehntN8gW_bzvZN2gFpIe19pcqlK2hMf8pAiUAeqviL8t90NdBdTbqIovxXVKQ3DfyBZ3dn2JyiRNsrPJqV-_0rZkq3Oa5F-9GcUVjSXATGw_QlJrxcQBLTRuwTUylN3ub0nIs6u9WTAqVvA_fvGZ18Mk87Nx3czXCtBQ566is0apQ8ya1S07BnmkIb2hkB8v8JAH3KqtojbyWiAIa10eESN94MxCu-DJot1qd-WSSrMJP-_c1qtuJUCMtvc5xClorWSNU146PIj8T0IW4YTUEBPv1PcYkpwd7aiR5mhXZ01PaPjYcn3XkOiKc7fvJBEFpEnud4kdTqNbug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d5Qtbl2FdMBLT-cRtzc4fY8zzfKXWFcQPbiiw7lk8ygoyTBDtavDuf_yEsNI-gQ39d24WPOLRKAZreDIs69uBJXy83tvQJNtMQmffjuzz5Nrrfb4oll79MVLHiKLE84Z3ZyWVuzHWw8JsgCQojJNNWPfKwpwxDiiTfDMPhddQxZ6ZWmBAViGn-TDZAcL0LiSfveBn5mVmYcNnDp1DIxkcH3Wi0ib3q7HGLljf8XQtaSRGoiVWYaHL8CZ8bApfUQsjrrpFTHnWvhnRZ_ecdbNbZ0xOjPxYnb8wQpHAeDo1NdGhp9l6l2LGdaYtM4FOyI4J3RgwcPiQwfgcndJL0a9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SRVw-bDjGAx-6C8oeRYhSjByBTt51C13I6uSBTNGBjsmaAXAE26X0rAdcDcqDkrOvUWkWGMHNL707MyJQdnjb5dx5Ogj06471gWvT3F09IRv8f1r4X-A1y2VRiET7Y-FrJnXMNxwJ6UqSOH1M0yY4k7hGWlxEJrgofdZUL5v3AdqjUUVO-W5EfkTCECYcMgKnoHmG-R7ln_EqN00r_4My1b4yq-9usf9xweuUgVIXXBjbovg7Dkbf6COUT6VuT3m0yPg9-imTU1JVrDRvF0xfCcdqQi3j3919KCpvOSjj596kiZPJM0KGQWgqmsyf62-DM6lEgYl33q7zBrscvxKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xw7c1eu59Fkz9vaIMxJli8_soPmA1SNK7HhdVlgvpqaREDoyJ5_v60YW3S6ELBgY8Qq86fwBfWP-AkmzIi2JyjQ5pOASROgvKjx2pN9AeWjKhyVRpmu7B0hcql556Z-8VUrXDvUBWqHdCeZ_RsV4PldxtE_DmKR8jmZctLmrLH0kq-0HBP_fEvqUlBSIq62IRLxRCipdOE43Ml0BxbeGKEM_NvnHwGza-0edcOVdfSEyh0ZFU7Zze___I0lrEJSF91gdeR7JT2Kv-SQ-JPYRHcZMaT9pAzHo64ZCZR09aIpLotPiOCex1TMytv2JddfUbVdP7_5In1ysZZbPeWNwAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه
هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن
به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم
، سعی کردیم با
یزدان عزیز
با استدلال و تجربه‌ی خودمون به این سؤال جواب بدیم. چیزهایی که بررسی می‌کنیم:
— چرا بیشتر بحث‌های این حوزه توی شبکه‌های اجتماعی «حکم» بدون دلیله
— فرق AI با یه ابزار ساده مثل ماشین‌حساب چیه
— تفاوت نوآوری (Novelty) و خلاقیت (Creativity) و اینکه AI کدومش رو داره
— جایگزینی شغلی و تحلیل آینده
— چیزهایی که هنوز دست آدمه و AI نمی‌تونه جاش رو بگیره
— بحث کاهش نیمه‌عمر مهارت‌های تخصصی
— ۵ تا کار عملی که باعث می‌شه بازار کار هنوز بهتون نیاز داشته باشه
📹
تماشا در یوتوب:
https://youtu.be/x8V0w3I9g10</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys7fvENh-WKTbqzFOnpbln0uK6WDRBKPBL7VaPiEFOzV2D9Gp3rj8SGj1-E7jsZMGQfcdsR3qLSgpdf02uV6XMHYh_SyifyLp9y3NQrWsGRdqrKOkLVNLv6qat6gelkPWutJANG9_36WGBrovz056FDsdYfBPZ2lLWeBlk_djVPA5gCPjLjId6PaHZr4d9lVuHOdtNwBtnL6vQk2cv_KjqmtskNCi8ga978Ru-6KoeH8olvhFda0wYjymC1NSwlib-RWM9hVerRYfpAmB5B5DW4Q8o4Qs47qWmU2L54WWt1tLsuCnj5BYlZXYy6MvvzV55XtGaQ-5UkwOjU5lmMGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=Sq6lP7jkcg-BdyUXjWdbO8MEm3yBzhkek9-1--AsODWnG81eKdaDzk6HPeqtQaBKrlllkpmLHMJTi28yv8tnUrY4E_7jqTOBHdBEmeBUg9ULbYH1CDnMXkQId3HsVizdjDqgb3wEdKb6sAl5XEJbbgfOzBmMIwN7FQzg7BietRPd_d0k-Yaemy6nLmsFCP_7K6PtKgrPcPVnFgz2AjDAoTItOW6eYPLkszQ_XxMCr35P01Pdq9MIABuseF6yWqTIX2kOcZ6-7R7mGbm4zHG9oG7FjmDsTtRAkUpn9TXsh2hdbYV4A3_C8kRv9dwj3eIJRI9Xkct7DAk0mylWLSZyuIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=Sq6lP7jkcg-BdyUXjWdbO8MEm3yBzhkek9-1--AsODWnG81eKdaDzk6HPeqtQaBKrlllkpmLHMJTi28yv8tnUrY4E_7jqTOBHdBEmeBUg9ULbYH1CDnMXkQId3HsVizdjDqgb3wEdKb6sAl5XEJbbgfOzBmMIwN7FQzg7BietRPd_d0k-Yaemy6nLmsFCP_7K6PtKgrPcPVnFgz2AjDAoTItOW6eYPLkszQ_XxMCr35P01Pdq9MIABuseF6yWqTIX2kOcZ6-7R7mGbm4zHG9oG7FjmDsTtRAkUpn9TXsh2hdbYV4A3_C8kRv9dwj3eIJRI9Xkct7DAk0mylWLSZyuIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=s-bPaQaRIiBT30FUFvb58iF9cLbhn9qPulk4iGYKpcqQfyB2f8U-OpY_cZDy6IVk0manc9gt9J75yDQwIGnB33j_PtYXinY9XyeX0_1vuuKyFREqxna2_HktYFx35viUXjKdZ7r8blWhkgKl1cGG875Kef66p8ehMd0GKqMgFzOYLGOk7DYUiel7D_Cr3d27ypZ1Ru_lWkYYpCW_SWQZlC3tuIU2aNiBIp-wuyLPPa5yFv7Wek-A0g19GRj91Jgu3naxx_w5py71Wdo_n1fIR9oNFvQg1R-cd6WPyAnMDQYo6OPdM0xQVMdI5L4rrcV5-ar8USxs46Uk66EEpalnHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=s-bPaQaRIiBT30FUFvb58iF9cLbhn9qPulk4iGYKpcqQfyB2f8U-OpY_cZDy6IVk0manc9gt9J75yDQwIGnB33j_PtYXinY9XyeX0_1vuuKyFREqxna2_HktYFx35viUXjKdZ7r8blWhkgKl1cGG875Kef66p8ehMd0GKqMgFzOYLGOk7DYUiel7D_Cr3d27ypZ1Ru_lWkYYpCW_SWQZlC3tuIU2aNiBIp-wuyLPPa5yFv7Wek-A0g19GRj91Jgu3naxx_w5py71Wdo_n1fIR9oNFvQg1R-cd6WPyAnMDQYo6OPdM0xQVMdI5L4rrcV5-ar8USxs46Uk66EEpalnHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vGfnIbtIEfdHOYt5tw6Z56aHNleMWBHPiG1NYMxHQAd1GhAaTDEFCBe5MGoge3jU9PtJgXO7PThKy2_fZ254Ip-2ic0jP_HkNp6CtosgTZ7sFJWvTPTucxU0MU77p4-O51ClAL38PsFEf_HdgKu64xzgVk9CP9tQrBFERWRuo83foSeTuXY7Jvv31EtV95X5xRkJxjjWr4fftp2sbE-SwvQgbIU8_QWTBOBTS92s1PrabfV5aX8yHVGIxL776Ov-ljm7mb4MFEFzkoCcADeD5i_lTyrcmV10nvXhdR_wwHyzqpQ6RhlOi-e4-C51q72cajwwrfSJl2UuGzE2oQ-WWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hOm23LsLOqghiVjJLDJdsfhhDGhl5jmxIVfeL3gZmjYVFueIX8SCiB8sSTl8cy-003FANAX4vCZMxRCbgUnPKe9akbyUja6mzZjlo3WSVgtosjqqGPhiRsWkFA4aHT3PcBPBFKGEp2PQ469DphXry7Z14Qo-VPKNYqPDkdD18MTE6J3IT_lWYQz9nCLbYvOOqloaGSrIxgpXmqKwBe075ncJ7ECB0Q8ugz4bD6YBgT5_TQ0A-G4RRE-YDYj3uNFv_UDMglbx5jSdUbPLIW0N2zrN21i-TOmSZwpOzpa-EzUHWL440WxH_7P-9ERqSPn0GaazuA37v6WPn9KPTUjtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=ZQxMH4Znz7uzZHNJExw6l5rbHDQ9VqOeE1zCl7mwYU3-p3Z8uTGpRPE7IxFffeOpH7_awRBJ0IpPPGlT2R602jkguJU4Tn6by2lB-KKV8rJmGATLxHzw5gfGJt-bCj_2QFy7COUZyuHt5kI0gL0OE79TMFOnPe2ieNX3HKHWOZSxts2GVBQcVxre4o00WUM18bhzv-fnuUzLkWNzK_CCfEt7v0qo6PlLaNecIwoUhfX1WDvpBsjEmax81R8zYaTYz_2LmIWf6vtYR81Sy3iMzVUkJnGUYS89h9dEBgUXi-O11YT7Ci9e4SKXChdyps8Gw73zIAubhdicD2g_HS4nag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=ZQxMH4Znz7uzZHNJExw6l5rbHDQ9VqOeE1zCl7mwYU3-p3Z8uTGpRPE7IxFffeOpH7_awRBJ0IpPPGlT2R602jkguJU4Tn6by2lB-KKV8rJmGATLxHzw5gfGJt-bCj_2QFy7COUZyuHt5kI0gL0OE79TMFOnPe2ieNX3HKHWOZSxts2GVBQcVxre4o00WUM18bhzv-fnuUzLkWNzK_CCfEt7v0qo6PlLaNecIwoUhfX1WDvpBsjEmax81R8zYaTYz_2LmIWf6vtYR81Sy3iMzVUkJnGUYS89h9dEBgUXi-O11YT7Ci9e4SKXChdyps8Gw73zIAubhdicD2g_HS4nag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektABnLtMbqZJjlcjxYpH9ZyM4yIaAlGJyvQ12kVasOu5GWd704TAEVYoCL22hEJWk-9VnB4HfIr_GvHnWJVaYWFytaIC5MBKNV4kDD5FABzHfbJRKlXBxxM65q0kKUbmxOzdglypj2xaPRQx3TnXVyNVZb3SpHrue3M7rZOax3NVUj1WpWR8BOAa3Xj55J4jdjUMqQgdjHu9GUJJmYZc3oo2OaMMLxv3hTQLs1wT_ZLyJNDD_KvVSNy7GcYjz5pygwmYdJ2n32x2DvVVM8KvZo5boxYtc67Veoo8I_Fw7vAzLDOhHDyoZRw4aS1IjHEXJOVsyfE_vesyCllxttFHJ3EI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektABnLtMbqZJjlcjxYpH9ZyM4yIaAlGJyvQ12kVasOu5GWd704TAEVYoCL22hEJWk-9VnB4HfIr_GvHnWJVaYWFytaIC5MBKNV4kDD5FABzHfbJRKlXBxxM65q0kKUbmxOzdglypj2xaPRQx3TnXVyNVZb3SpHrue3M7rZOax3NVUj1WpWR8BOAa3Xj55J4jdjUMqQgdjHu9GUJJmYZc3oo2OaMMLxv3hTQLs1wT_ZLyJNDD_KvVSNy7GcYjz5pygwmYdJ2n32x2DvVVM8KvZo5boxYtc67Veoo8I_Fw7vAzLDOhHDyoZRw4aS1IjHEXJOVsyfE_vesyCllxttFHJ3EI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tsoMfXqQsQAtJt0IdyA0DeVaVr-PcYambtBy00sVleuSy_wnnOtJ0uTrRxW5H62piB-2qN7VrtzPZcimK9Mh_WOihg_TznXvOnBxdnvZ6RJz3pGxDp4P_LjSA37q5Q9X7MGQ4WRW0Q6vMiBoFV0KWHxuWbRF9p_r64UGhvDa4h-s8HPTweIKFuWaJgLjrI6slXkimkdgB7YhGVI2Jyt45MorbP5XXBZZJxeonAxqc7ypo1a3pNki5bbaP5V4b1nq5zLSY_rMcC_h8Ny-uDH4QDhidPLczeJOcHmApHsFNEqgtqwuHlaXAyFJWI9NKlEMbz_fxg8j3AME_MkTDrSv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tF0tDcIoU4anc0mzVbSecZ8eaS_hcJQMFAuMIMv8CK4pf-WiLs59zr77AYO9O4jeXy6hMlcW6lHwolvRgWUU9KzrJzSnnjq5i-PJReQ6xW-zk9SiWtGgwMa0YKzj3Qu6yokMJHgsAUER4ugopvtLJHfIbhnrj8i69Oy8RWebN9As6eKvYyj4DRQ18K98q1H6BZZwgxx1VVYCk71pGiYoEyE9reo6-qKLEZCp0Co-QDkhP4BwQfCi7YKJokUby0wBIUdIUr6hWbGk_yPj58uZYJGNy7zhnT3TubLoqqkyvR5QerNh4gyrPsuJVkCAFuFQuCPodxMKpzvPKILgCWeTKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rqXNzlHBzlcN78VvynhWtvUjwKGfJTVLA5784K-VfV0SNCyESYDXl8CfCJQT3RDdiD8VzO1tyu61ldREJqXdoNvwPDdCp35k0ttYo-73USqo_myGu0vQH-LoVV3WzTZ7Eujc-zruBQhGGRWwO_TXKOzrgCeqbODSYtKQKM6JxJ-4RRkpcq0Logxb4xTMIVg3Bop6Rnzfcps52rFxxD8BUFJG2V4CoIt15gBv6L0NW8n94paInYG4eDouRvw483ld8G3ghwvMTWkPA7Z9iQtuXost-8RpwJAyR9IfWh45bNTuQODxhZ7xL-U8P8s_j3VkpYwW7yxqw3WgSMjJwdJByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXTkrxzsz1v9_13bsXsZcMgJ3wQt_ZWFuVUXJlbCE6AqUt9EFLHLpR79HdpGaQnQHW0KYDJP13Y7UnPqaag4WPf8b_dq-9blcw5Snfqr-w1mPVxUqdhZdd0mu0GjLG89hQtApH0nUjNl-tSVZPhD68oV38MGWUCeELS1GNGQPA_hZS1Zrx7WlHddlkAjV4gIi6YPsNz6cticffw19rv4gfwnoAW1mzUw-SzAyQ89rFASY391MbpwdRmOqwMnurxY5yZExnxS30Sgmt6EafYXLC0KzBPgRWHheN0Escrr6KiKiJ425jg4jdKVhZIRI-44wBPJvrRJfVOIDK2GMEJ-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VK3TXnEdEirPRpMhdMAV_V4XhmvL2yBB_qs2uUUZ5pbxbJ1cw5nKImyaC3CnU0Azyu2nvA6By6n_1FyBPRJCFPp3wST8AG3-Wa-oaCyrDrN4PkckZhR-sUScfG-g81TAQQOu7KudzcruQlozMXmB0iCVCzZpH94jenPvzoHnI67-1iZEOU8nz1L41yp48H6IVryFjUNegrp2IKpZ_-5H4rXY6KRt3UCVnzkrJiM9b1us5JUJFJNbiJfPDOHMnwKOnX_toHfYTjfU7oJATM_HY6OWNdGzEcis-bOMQFJAthZnFTZCQiyRYxiszeH_fddOM1QAUhtaewd_1uiEhCC7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pEMFFsy-ZbQhRz6otcvwD1s7bZ-3tp-C6X2ARwOOnp6KAvFsSAX5UldCjibFX1ylYBhg6Xu4j8owYuZdEgJ7kZZAFi9OE5Ycy5vRnm0wBhYmegjlEGEooGUAqR0JM4cLSkOGXhj1VltdMXMQag7tpi0wq6CT7D59X0_lIHXObv7GfAObfhNDEGWnK2U8DdOw1uK3g-aJedeDDUK0Lu-xhVCTLfafAq650bAVOLFYO5wpItln3gZjFULqOnwTR9JfnweBDlMQUWLG0Zt1jbiBDlFpPHnyzaqpVr1hVHmYjO04EppRC0D6GXcN9plDEX8CKfVFRCnX-F1IkjMFXvOUkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RXMI6BBR9JZ4bJUoACY4pnesYhEWb9k55qVcPduGv4IHF4t8Ki57iLPld7Q7Xnn4LbZFAA2VXu5gpIA9hbGXbK_HLUo2eutIK1eKxSSvoe2Si1cAnN7KbAvDUrEBhriFmMyaSsYxaK3Kxlr6tTlTrDMl1b129Xr6ECqKlNYME2SXa0DdXjVTuP6K7K-qPZh6wuyKCZ5hSgYlZ0jUGv8FYKaRN40x4HDDRYZBasOOrH661bE4WTDxc1D_vUF2V-5kVpxHpyG0coJC759bo6_ll3RJQ_oqNHWSTRrFCdhPnbm-fnQes5Sqs2bDCFsDAQ3cKA7_rVN0HZtQhIVp083J5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lGWyeiLY_dlEATEUGeLu0n0c4DdSXX9psWxaGISTagivc1ujkpr9XOzV-S3Ks4_uPcWhdlxwtQveTRit2Nq-FAcoahVlyuy5N4frlxQEzaRickjTPHCTW8mHWD1_7k4hZTAHzu2O9LBqDh59R78nqPffmmQKH5nhxXMOGa_W7TH-lvWwasz9tZUPR4dFV_QS03LreFmWdHDSwlhmOJi6hFcsH9x_-JxbCFKJmHkD2OjG6akqXh1Wx3vcGHllXeE4fhQfiyBX0X9PHw2a0cnkMxNTrRGY_709eNoCBad18PFKIusgSxEpEF0lVCqgv53sjSwD0sJz9tydR3wxNEVxFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CgXBuiBQYIw9QKI-54MpKrk1yUee0KDZW04wMHQHtl0pF77gO2PilLbCWblFBU8nfE2fUw1ckaKOBWOD9Ro4piJie-MQ28_E9fLDfGntcPOUYgokolHxctSQzBOph015dA1BbMbA7vl1E5Xlro0oYPjhPtgapgOSwZBSiw0ywq_dIbJKxnpQmHth_HpjFu4JAoV3WfuddUiSPUGx5XRbhRTGfZbyQsHuXaEIqG0x5Y7CE9dg252R4bujcadruTIaSsy8xtdDSvG_6imNxLU3jf3J3rexRSmFA-8w89SRcpgStkq9dVzqdb6pY5hs0GwSRf0d4uMiCSGfAdg5xvgUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R21cX3QYOr0AwoXYEmmRdhkRI-k8-hEisxUFcOj9ocil-RKNqc8qlkpjNTtF9cX2BrKu-V7xBNG9-bU7YwojrR9eNEiJAJnu9zITg9bGE4JSNehrqWATpw2SQmatCzAq5pkFdaQwyWQXWQQaOW1dFzD1H0mcBnrTG0vWFW7claOSlFDi7e3iyg5S-xXDNyP9Mm-i44I1IdMWLi6tRV-sQpOVae-e3KSeonYS7OukhWf_sLsV5N6sUgT-gQsCB98cRYnvHJbzI5rv9gJHqWcdF5d50hRPR_EGHFxwxsbk4K8emDuVsQXoAf77xvSS565j1Yvr1pHV4IOAU8bQ6tviDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLddkLkedtbBR8J91ZYDW1_T5ntcamllpTnLYdd1lS3Z7-NAGXDzJa2mMp1XPvz6hGmnL_RappvV9DLa7W79DDfnxVXL32x4uTilTwTP9lqBynMvYMy1Db6oc-K2XZtcfHkrppVsQS6G8DlDM88cTKeTOFaXq9VBGgB-v2NMSacU_6pRe_-VapRsIy-jAbEzS7Ou9-cknNa5ZlVvvAhgyqDSFTQJXNsH1YFUblzyCq9Tj-MGCN9-XWL4eiwwSYVLuoKh1BDWRE2DHx7VXtuHY8LJHpqPVmHW9Xxq0fk6iRRLGzLClUENwZHyzntunLxYoSyafJhG2_pE-1VbSq2iLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HohxHc6tHUJCWJk8rleTyqognOdkI39_DpT94tP1jBKXIp8gVW_ZGN6BA7KWU9kErgjheygrG_bJUSCQS-eMHFB1OQ681XHhdOpI4HAsJMUtkhehDtVfoe8Z2GfjV3s6KIyY88EctUjr6AxaT9Ta3-aGFFsCIEGeDZZ5t05VD3PsMP7pEDLtsybCGltF4nUnySLPaOG7_Ktx1yRSo2rkBrGhtHZXH9T0Ocvf1gjMdu42D635SmlA5rrqnaG6qf0UqMsKRiYl7CLLPDr9wwBfIBuQOA0DsnfOcJFvLMKcT2_WlGm2sXzixCTjaktDcv5Jru2GLHr6woHwKrXhfQ4pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/REz2Q2438gb34JwQMdpj--dVzoJA0sYQeX50wb7o6Kw0nu0kni5Lh5zBmAaHXuDPbloc-4FD1OYTjopnKXEgNCXgl8iZbnq3JO5qNOQc2vfj_AuHfLtfqNab6JPvRd5ThWgOPe-YlrCRq8VWlVF3tJ1H7J39kc5Jj4D3Y0J8yWDO6vdWGbvU99IZGU6GfxHewDrXalYMvZ2xeppIbndqHnuW1TUrVuJs2ST2-ubot52_1_R7cyz_Qmrw8RDiKhD-ZRTdkKwtI8mkEPn7kM7uldsMTEFQFUm1JbEw-eu0k6NV_vpEvCEmeKj4SYsY8XVv1cNyKOGO0bmlP2I51RKdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KhlaEXX3A0yyhIARbIB-LDYBxsnuiE3-a_mcJ5Cu88f5WbLpGts3IBkmeIZWiRXdoq1pbEMreGgNoOcVX6rBc9-NmK_nJsN85vS0w7-rQTJu2jJYeWbkx6rK4VoLX2qRKsxAX3DUHgIBgx1t-LeOcVhXDUMNkXv9u6MFnNFYdGItzkzl-phAlB1DabbT6-rhy2XZqF44XQk2Nueq_Aw6e0YbHXI96T5YXpupp4J9LL0VkqasRXsOEqvhZ0TkYCDgo6PzpmJVUoIBzSJzBFbPVMYIzsIZtceMPyq9Yo_WX2yEE8w9E_dPWXtTMjBJ1ITN-2CDiOqH8dEWUx6J16uvaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U06FI2dExIWaEWp4lhxANcFfpiQU1ciRsbarBG4CC_vmyp39m-_3wgPWB1AxzXp31sKDkuD5iNB2dy5w-_WpT4yfQP7fWYjkLX9nt-3ynH_jbmkWHIxtT6nCMLhLC_3CjVtlkYG2tHGMyBNGV_WWWLEC6McnyRUhe79sxiGyCOvdGDrN_DqqrhTcJ5gBA5lcFeA5lBizxEXz8-X1Knupc-Z6vMcliYZqCN6BMcvMI_iztsn75XOg-IJwTBe2QptZV2buofEOzMsDMBCZOrvYrrt39iup6i7B_sX1UMO-MVvgxajrROuJTh4XJYL_8kRHkJgy6ZQTUE4QrPig_J-MvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ8QWW_JNhIKYfgpTmNN6Uy71QLz5T_5gO8_qhFh1DBKpVhhkcbY-WN4d7cL1bq1i4eg5UyrZlotnEOQj7YXmt0EJIXa1_mtGlVi8As71sDw1D4wl0gQWCS7Wz1JgNC9S3jCQoM6HfMEpR6cgGRTGDk8eBI0mrFj07d_h_qrlHXy-GN41tvtWfRhOW3lSLr-TmzGryRegj6H9Lkpx-j5jNlxOFgZK-ik-iyVmR7t_XS1oN70qrlAk6X_zfjpp0_ObBmzqIoOXnbgtLJmwFt81IoeDDMSZ8ybnd-40SR1uPyV1xyLn0MXJMBW0lS0HDus-ZHWxMnQElQ4JSmzI5sU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/um_JwYZYsyEjvkCEPKsWruOz7WyFdE2MK0vrjJtEfLn_mlRKnLVEbRzN8nlw0QV2H-vEwsv10o4ZsmLhtE_LE0P4iXn8W1WZwhCYHvR-VbbKavQwIR9xSDy6jMn7B8oj_h2B-65p3322z4oKHEqb0mSFiW66sq6peLX426ZUTBvfF8EK8Tm8Cgx7dxSHcFkDwh9sUXeS2pxM9ZnERf4-0UuCWrn7d1qWPsR3Qgjb_QtGCErz7avHvVJ32tPg9a_2AVHR8fughDBssewvofIWBOX-paL0AjT-nZtyOku6gRmfirjFUZGx6lpRpf89wtG-5oDu-ZZJeF5PB1b7PYauaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=J4HWVRn_91qTtfIelg9j6I1XDKQb80BxOvB_2G3K7ul5G-ME9q9dfFjiMD7tDW86UiO0bypt4VXi61IF5KyM7DgVtSR5maxRIOCJqBrArnb92VFNxc9L8aD3IiwNItjYGjDg4l5Zma6mFCY9HDnVVsFCM-GoLElUKN5VEhz4P9bf8nzrms7dD036L5tQ7n4KJLklrr2mjGVRvmfk0pJBvk83sMpZeXEQA7co1Rqw4pEYMBWJSN2po0-chxyLWb25nR5UcIIrB4YI7QYqh8xVmmLPkkpgv6KiDJg5m0JF8lTZEd1900_OKx_I5QTkmLP6s_iaIb88b-JK8_hBbCsMvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=J4HWVRn_91qTtfIelg9j6I1XDKQb80BxOvB_2G3K7ul5G-ME9q9dfFjiMD7tDW86UiO0bypt4VXi61IF5KyM7DgVtSR5maxRIOCJqBrArnb92VFNxc9L8aD3IiwNItjYGjDg4l5Zma6mFCY9HDnVVsFCM-GoLElUKN5VEhz4P9bf8nzrms7dD036L5tQ7n4KJLklrr2mjGVRvmfk0pJBvk83sMpZeXEQA7co1Rqw4pEYMBWJSN2po0-chxyLWb25nR5UcIIrB4YI7QYqh8xVmmLPkkpgv6KiDJg5m0JF8lTZEd1900_OKx_I5QTkmLP6s_iaIb88b-JK8_hBbCsMvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cAe6K3JhG1_7ec9Du78E_4G984P-lzHlLODNGCBW4Y5Y3zFEXJaFHYk-SDhyZ4x6soBp4yKz9BjU8slOUnNDaK-w5G7csEbSkGz80Akl4VwYzaWMsseHOFV2dw_uDUgAEj_aPFXXiOi_G_0Yl0RSYzDLgqaGIMJDBrqIQTDLCpC2vGqqafdThxCUljkBfvwtj3o7sr7wuMyn3l30X8ER7maj5RY8zr6qz95Q_gxYD3IjytamClQ9FrGS9kaTA5MqyegMlhNZdzgPkyxA6v_xurnNLTbKjz9TpgB1xPEP3g3r0AggNgWMy57Eo2u_fXMeVEslRjKRmDmN-PtqnHQUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/czBObgHR296amgSn6_X3liOqgjyNJp_r3fcWTWKItyfm7Luq_wS3lgnIPX4RNMRuJNhmK-jtTHNNvZoaOpkM-RR4nia3ieZWc059Pb6734dLIP7_Hv2nO52r7PuNKEnFuhgKYh1bq_OyCuPircpVzJtdvNzpQGqeBToY9VN4I5UnGJHozsEoFaI853pzOODe2JJIJdZN_juHisjSP-Mk0rdLDUQq_P9AmqqRKfOl8Ph0Rt0VFN-KTwCaGK7ddf4h11wgDpfcaPR6pH4kyUpH5MVqwu2eRXZwWSlh7ezvkHhZ-xCCRxhHFTEQVsGDrobG7gB-Ej2YpFOIwJv6E-fomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_bdrOAIg5ms5lxtUOLMdj3E6N0QKyTfTkkzasQnIKV7NsxNzQhdWfAHxupl4YGL2AeiIV5hS30wWJoGe-aKwwPrh_wOcc2Lor4beN5j_P17F5hn7NgP_91pm5N28G_HSjJcWgWgbTdIGvPUxr-QzMDwuddLL21CppJGZRmC6NuHjBRofWUQzINIkvyZHZVwLXDAf6R23xvYoZa7tGwweLxoutPmrHDtCm10VEG9enYvCB904y9sfSDfSQ3ZMs0I34_Wlw8yiMwCrA8lETT1qlWAvmqx23jSXOTbXgWRhDxxPHYF--yvad0llkrrqhx2UWCN8WMrUMlWND7_jrt4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=ey5XP50eRdtYsqVcB1nmJZUqjSpg67J_P6xHAPX4zsrgXmIahWy_bPaDWlYauL7XUJOAEaotwtgu7q5ocwE2zXJYkHJ3eg1E0satTmPX8Pghl52CMdxBBqHlUyuK_Ymrwx5jDEHpe4WoM12SegKpWl9YNv05fZdgI8AJQO0-J30ouIoDDFpWtuzvZmYMp502YxsppLYMnMnQCrDXwAzqwxfguAyZT1pag1TYSr4rsap-zB8l03A_MuG71FIQzFZ_tgyT2Ld9OoYSvKjvWFWKTykMTEKLW6uWRy2RgXjX_DZQb_ks60MFLdaNADcDrZyxWUp8PDgTGVD3ae6yCS11mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=ey5XP50eRdtYsqVcB1nmJZUqjSpg67J_P6xHAPX4zsrgXmIahWy_bPaDWlYauL7XUJOAEaotwtgu7q5ocwE2zXJYkHJ3eg1E0satTmPX8Pghl52CMdxBBqHlUyuK_Ymrwx5jDEHpe4WoM12SegKpWl9YNv05fZdgI8AJQO0-J30ouIoDDFpWtuzvZmYMp502YxsppLYMnMnQCrDXwAzqwxfguAyZT1pag1TYSr4rsap-zB8l03A_MuG71FIQzFZ_tgyT2Ld9OoYSvKjvWFWKTykMTEKLW6uWRy2RgXjX_DZQb_ks60MFLdaNADcDrZyxWUp8PDgTGVD3ae6yCS11mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVv2ZQFVRe55G7GJ52wibMr80PXlkItnFdV-9X8BSa1uoqxtrtreufoqBgpbl5_78vz4Iulct8dxswwrYr8mgOtAozoyc-yJl0MiDeAnxZyUxUnnKf7dt1_Wuvl6ECyCJ-jR7yiIjDaUvSLGtPQxs_8IHs3SkkY7txsg7YUJfIQ-F_wqNymlagNo6ASnY4wgE7H2ilimRXaL42qf7U6G0x19jAIj5okzdxF3gp9qyBUbFP4ku4SiLjlS6ittgVG9X1pJG2zjUd83pVAw5foU_1zIxMxmqQg81RXTE7sN6dUvPT1BIRy51nE4jAV4YCTcmodBmoHp9DOE-FLf-N_PBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EpZjb9Kw9ZrmLSmStqhil95E_rgoRLt7l2stP8UGRBB5T9XoXjxLoUTS2ad9FxIa-ojoDXuKptb_Eaa1Q0vQG7QzcXe4MFtjhZba2MGXVa6m9OaM1D7xYutHGie84C70rPGBxC5hQgemqjLmGrZLNbJbiD-W80qfNhbnQnJLZiQB9e3oPSZSMIX0hd-6mNBkImIZf8sCffQq250lEgXSnxEJBKuSmU-4sG0d26w-jU-CDfU0pifflFdNNU3lSw9JvS4h27G06opmhwjMpL9SHgSfh1xmIyIDm1Jcbv7OCbzLRHUmjQsjRk46f2CEwEcRb4KIes1hCsH2zRWC5RxSEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AWLbR4eyKD3kS1vndn5cGYp9G7yFncyVgdXKWACdvGw5gPWvuPBCt4plfGAcDHu5D3-GES2liw2yZKupY3dhHIFaWxq1xlfO5nOyQZp55YbplomLkQkf5CcdJWRf4ehATWlCbFsPLOEZKBmOEac1WHhBx9Mls5rzkvxAr1HpInt4RowuQs77c2VNvuxAmICkiMmLUO-9PkYQ7cHdhhC6JYMjL9Fk941U5r4qwOMqKdYUITeRVLduamoPO84efIAQlTn_M7U-Qy-H7HaaFhoX6dEY5kZbzoY0ejSWV0VItPxUcW4TNDpv59Qs6vMvBO0Y1isZut5tMg27vAHXMu7cvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LDxX2Gvdh1gFzMNUr1YVetTWxXDMVwhY_0ntai6VH78on92F4eUe-TOtqoablD6GaTVcgnk-pPobb5BsTuTL1_MoOO2_pqv7YsdlEeYveDG2yWOdrOdPok_VkO1Qmnl7isnkhbGvT02wpNEHINMlm6eMow9_ZNmlQow2CopOc09U4JZncNaHkplzrXoyYCk4ukLjiwJgW9xDKInGo8Q5dWbI8mKBj_-DvZw1OAgMrgbE4sX2EoABpppbQ--4lgwQmIJGeNonMuv5VrhMM7Z0PLtZnCYqUrdv21ApPZmO5aCKJCDnBRRvrp4IhF17kiw7tITfBn6wpAb2EtvQgCOB0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxfomWl1zp4KifiWHwrnYfXRBYfNdX7gEwjUO9DoRXS3cnzycXaWm9Ik3e_54WjzTud0whvymD6QhWUW7y15hcgjAnL4SLeGOGENaRQ9Xt5FIKLI6c-RAXULfqKBcIXQuUQ7qV3aX1GH4QY8gmy5DVW5UDFyUeZxOnna4nULDjLsW_xsm2MTGaT8A944MW53_6VYVR_GnwgKa3CylLx54t6tgrevhEGTvZmQyeI35E9acGj2i7d4BaiJzkuOd3g_7A8xFZbAJxRyJcbWqeZpDOtHezQ0FXDYK-spFnm_t3Xfs_dzUlI3WmzeEvIq06p1q-AbA9OZI4M6ZdVARnVWzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vpXw7ljmRMcv_iyt6You7fGj_tbtq_3dXyZvduQI1JNjwsXRc7Q0WC7vIRU-ltKhFo4oJ1XzTHJ68hfrQqOedxohEQMyx865hWJCm6JDXmS36Mj0X_DtvBXMaeKx6Y23opO5mXRW6U0qVOgZQXRk-DYMRB6gJPvofZLuk_8DykWGi5SOhQfqZTQ_XyC76gL5IupYMGqZ3iJYIkS_ARu566s_P-LyvFk7Oy_1TXMM7CC11Bep9I0IFdJnrOy-GaoN3htNORPNIf2r7TzEDSUlJDc-wyhE6d1nKxPsPZvPhs7tILLQnyby8xnSubSSkNUAKA9H9dhoIBVo5itd4ytHsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=EEfy38q1RvBKQ2_eySE1SK1A1AEmRGjQU76ZBZPADbYU0oTz8PzC8q3ljoWj2WBbdy8J7ShqHdsCJ5Hun9N-aJ7AiWxNrsGtyjwzCkOhjqnGw05ABcLpA12dG-ACTRIzTOsupmj0ty8W5BjoEQVA3VEl6PaBeF07fttbm-oQ97_6zSaios1O-8LK4tcRLp-KltXLKVsz7B66QO7BVtWcdYLXrWlCtwIuGBY8OGFwImAbhQTiLy64WjssD8S7n2cANDeyO6UIRBGNnUJ8fbyVaOrgoZCOa1Rt86hblrmpnuapUx4s_gFsOPN71VZpA6IaTXU-GPw6YXyd0GylUewieA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=EEfy38q1RvBKQ2_eySE1SK1A1AEmRGjQU76ZBZPADbYU0oTz8PzC8q3ljoWj2WBbdy8J7ShqHdsCJ5Hun9N-aJ7AiWxNrsGtyjwzCkOhjqnGw05ABcLpA12dG-ACTRIzTOsupmj0ty8W5BjoEQVA3VEl6PaBeF07fttbm-oQ97_6zSaios1O-8LK4tcRLp-KltXLKVsz7B66QO7BVtWcdYLXrWlCtwIuGBY8OGFwImAbhQTiLy64WjssD8S7n2cANDeyO6UIRBGNnUJ8fbyVaOrgoZCOa1Rt86hblrmpnuapUx4s_gFsOPN71VZpA6IaTXU-GPw6YXyd0GylUewieA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p9f8R-NMVX-T7C16y5QbekF-Fx2fKem-UdZpFLKXu-s48RwA0zuPXVEXlE-89rB1HRvz8Gzl65dPy3Ru_sxn1Yrm5tnDI1s806wCTNTk49fsJ7LeqTfFKFpsdP_Y0lfHuzq8v5_u_o9FgJBLJYr25MwyNz2eixL_bDXEZebm0dZDehkG4o6BtNwgpqsB2MoUCTLGPzMYEsLL6d0POIOCHrE7kCos3JvKN88hl2MiRGGZAp4WoB7GzTlI76bwAo-U8bcIlLmczd-P3jmH5S0BKF0dAQGWBjLCoo9BsPghT-BujL4e8bGFRctvF9mkvSVFC-Up3o1sk_w4ieJuQWbjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OyJBfCdQudy7Ym9wai0TjFcrgpgYibjiSfQB6o46dKRjM5WJQZ6Fw8A-buNuhaA4F9Jl8fLZmLZDW4Y-F6yB064m795gYx3Tb67XBFN9_o4FylMhPpT539BGgakLfAx_vruoteReNi0IDXFgh98U0OzjQfOe-FK_TmE7rlhuyy1suK5HbDG_vhq2M4B37WWGF2VmvJl8eBfKbXXBUAxP7nHlPdWQkEUhglRZBDNDqGn4k3mAtpnMpdlJ9OBryFn-0Ccp9iLWNbTSLdZzA4WuwO_BQ1qYwN27ONk3UExiymzyz_SXrVBZE8E-QNilhLIuuxD1dQCiVhPOtJAS5Y5VLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sLWUQubhHNOy4jjsi5Oc_82ak03v7XlDuYBuuawtszbHgFskvRTFM8HcJJhOsZwcKlS_dSRF88h81ak_-1ku6ce-p4WS-Ahm5nAx7sa0WBcCv8xcgTTJgI6nuqIyt8JnoNQInwwQ8g4SsnctJjcE_qo997ccmYJCpaPcCuTIkbazhlXoBSHTgsD2ZWIMQT_8XWikOArJaEaUgVvQIKXqfkn2xSOHmNHr1b5K5WRZNLmlF2AT0ed49FWSNMYTUV8FKuf3oF9vY7BkS7m4q9uWo0frO1D98mpdI4TwbHH62u2APU-VdBzlTqqPxHpleFDrrz1mDwluldjzjdDtNDXL1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G72fmC-QdbAU9D7bIxMeboxQNBdDGDjBV9q0ds3JDd8mDmeBdHs6a8yQqYJCF9nVNtOMAlVfv1d-CmDs0Z2_F6BE18VhXXdOL36XCw7JCdP_-KUpVF90yiyssulkCI2VyDQBVpfhhMy9seKNa3RNPGFZ_oxjsuKXZCxKvPANHv9sYAwsNvoZunqf3WdDF-akfS7fc0bALV3Klf3GAEQJ3vtbQzbHgbTBAMfV29qfJQQmAFs6L9CTi7SEmtGoA_AYsvZKCIUOsJiFpQCafnZpI450SC5LCQ2vcq4qNbogAOd-MTQmTWdzFhO7M1Y-7C9gKWjrRCCfPAVqerLa9xCliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4sImiJdozYB4ix5eRfmvaMDCQbbypJoXv18h2DPYVhZUQJqmiC9OZxqfgYk9fKWzdCsA7zUWjV9JudKv0KwgY1ENVSQhy95E50Gm_1LcrdA1q6KUd9uzOjm9A2IxaDN3DSjlyLK7dTXMdmuMczqoGOk0jPSCiUas_5PGhkxJE9vUkpgD-yaMjzuQKgSmug_GOMxW0r2LuK25p1HPKp3-Z8L24Y8FInejRU1obzazGjxS9g1DuLylMqt8-iHpgKfFY94KXFJ13EjOtuyzpGvbvL8Fx8AtTdLDvL3IykT-ofYKs_4tf1QmXq2798zmNL3CS_871YxC911ERA9WmGM3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/byxxunRv49WJnR2m3lmb2-QwzUNrmA9z7C9BVnMucsNSu70X-jUtsdwKq2s9oqmPt9pdkNyUiyR0yXIkYzIb0NxLayMYtCO1eOPd1U2LJFdpa-UvjCFmE1YYkPuKukWQcm3tTR81QLiuEqXz64R4pQ-UmW6B557uqPgxGU6rgXjJSidx00NxVARFbs1ABXQNGT68nntD3s-lKbwMJJJRAYsIK6rrtuqyeidqjJkueJFzv_lfixiuScP6r49RnuZMfjml4Mc0RrcSB7NLEp7u1_nn5pppR5qPxEBO2kjrAzJYJYnN-gu8R6626AdvmSXMzv8Bcg40ePASN99b6cuPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/txMgn9-TEXPKN0TPXavK_UPZoVJfEuXiEb_jKWbAj3TrAiw8UKtpwi0MnWQ8MT7lL3osnC-ILmksvpkBPXmjP4jRouzEKDcjyJc9DkuRCOhQi2cvZ9kSLKVRaOrzCqBS8TWB87ecp3LvYMRnU2S6THNaokxEdFffvP6fC7vwM6RL8dKENV6sW8o1lXlH3YiMuZh1yvY0_IQxCoacb-mMt9Hr9UQrtsBATxIzls9G6bmOKMW7NlGvC3qVePxIHC0vvv9oAzPicLzTJT8tGf4RV-Bb4irfNCslRJywAC5LtNS6IINY2bgnYvAaEOhGKZhwU3RpwkuHRRF9IWGG3TFhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QehoARqosTSollWlBJg4QjFSwrt69j2_5mpSlLo1RRb_5nVJPkhJK6DZrQPmCuEs8GN0hzwNR9eWErV0YLT5PiyoROL44fQWK7y2gY9BZzsfxEonE0x3EEsJyOQa9I9BXpifU5eoTHOMtGWYguh_fGzfVvvcaMpax1NdhUFMJ4CsddsGzCCuHcRWD9t-gZTpU_QJ8FhKidZ7hYx5R9WlLG0g9yrmgW3DZgLBu1uu2PDgrRGWjsiYhbxuTNJK77kSoPWTXX9acneqBGckMz55yI4FcwSdqcmuMS_U1WtiBa_WHiagj4njpMWCxIl-mUpGKppkiesg8QkBb9Y2Cw4rYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=bsv_9EzcAmj2dCWarYHrHhXzkQagYFGn2sVBWVPWQsx-6r3hRHnP_lC1XiN8_higmBGjDdkabdFSgBFr4OncNz4M6dZHe1a0s4UCTXAxicY48XHWGFYWgi-NtENCmTSe_-4KZyeekJ9Fz78T16QUDN7KH9i8RbG7R9lyHy7SqfThCZw2-MEpNZEvQJ15lURBQYwQrPJ1qqB9x7VQ6fhINhtnRAHknMrLmoTyI5rjjB-gjSSMYyq2dMMrfKw8qyoDfOn6TzCCeJFWvNT6pstN4hr8t_IOZg1snO2NVV48WMTqFLcjt3yLKnKfINWgYxJAKeRcbnqp2kyBGeLqOAWp4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=bsv_9EzcAmj2dCWarYHrHhXzkQagYFGn2sVBWVPWQsx-6r3hRHnP_lC1XiN8_higmBGjDdkabdFSgBFr4OncNz4M6dZHe1a0s4UCTXAxicY48XHWGFYWgi-NtENCmTSe_-4KZyeekJ9Fz78T16QUDN7KH9i8RbG7R9lyHy7SqfThCZw2-MEpNZEvQJ15lURBQYwQrPJ1qqB9x7VQ6fhINhtnRAHknMrLmoTyI5rjjB-gjSSMYyq2dMMrfKw8qyoDfOn6TzCCeJFWvNT6pstN4hr8t_IOZg1snO2NVV48WMTqFLcjt3yLKnKfINWgYxJAKeRcbnqp2kyBGeLqOAWp4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vtex8k6x0Jpp6uw6p2ntZUhu_pNo90U65-swsYMsXj1LW9X4ZmqSyBbtUkPXQcUz9sc4XsL05aMyGdencWborbHSZQJ7EGTXSfnuBdIFrPgAbiquHWPWNnaDiB79Rq-Pt3KolkzYEcLhndDacDe5XLJAR6QpvMPJlwLdn9T_aebSunCNP6SS1jsCKZ96QmhwFLdvDTen5MrJKUqSlijAJs2CVkR-MZOHXJOnwm4NvgowSyZcJSAhIBpSXZBAjEfDz79dF__a17gyPARTEIJUnh-x4o2eSrc_ZpMrb7fM54gtm8wHbGnlVBTLuA6gqnqaG7f-d0W7IVYEFzgBJm20QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EGkaIh8iP8mb8CcmcrM4a4ke_3KL1wboBAA6I2Y7mcPjsiqq4MOGxxlt9Yl3pEJtcjoxDeMA7LDpnhMuc_PDuYTMncCYfUKbghlGB_0nT9DFH0_z0yiS36cpxi1yQtgQowdMas-veovNHZBjMWTCiDpoYwToP9ogdnqtFyqpLWDi9DQBkTKE8fQLS6Izgp6KF5GXHa0kEr4pQaIP6fcOK4EWpdom2sgWysncEGlXiegBwO-4m-cu5gvr2N0JCjJb0C4jJ83KvxhEYB-MEmReyTcvTJb5iN6znjXYjB1bJGjvDvQD4dJSF0suLmCdgYRYoWMZEjj1ABg9RkXT1VEuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6WraaZDEOvGF-rVn6l5rqJG4HB8DfIJ9lqDCpP2PCJ_sQc4kRVILomGLdi-PsHbN6hCgO3S7xlu6H2onJwojfJtLgbXcUtMDZTpdhoD_VBGRc_UIKscq4xi3jQp-rcSKv1bBuQohfCV3I3yZ-IIdvMRQuoshxGsbelaP5Yavo2KleoCKRiORZSN766iETG8pHVdAccrfPWPtfmScYRpo_kXIHBucYA0EI2CIFhBJUEf_Nszb4YaUkG64f9wUlLb6DxqumNc6MkVt59vhVTS3ujO06aZOhQ-64ai8y7f6lhEIeQAnKHHVsKup1lgtjaFc41HQoMQedawdI5-npfdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmwZIh7GsPcpYCvbEvtGgds_fuN8Pud9kyaPJSG5IkWNTOOa8eOltY9SrzALoxfFGIv9yu5Thn5IU5cIh2vfg9eaRxem7wo2-4Y1AmEFm1eTwG0i4QqEcslgxqkNH8sNdjai_bonHbKFFnHcfDKNZliLmd2is6QN89mYsp5VTKoNOhWpcvTBKGF6rtAinVofN9Pn8E9htum31SFCtChuTiyPbD-bzaExQneOaH5LSG51Vb5jmhMZREdwaJGHcl-gweULOAkWJYvS5j0CR0sT_PWzmxO7AbOWawh6XsPKXdG3VXXTCbjO1r2RdliF4sSQOWyRo4Jp_DYSLEl99--UVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
