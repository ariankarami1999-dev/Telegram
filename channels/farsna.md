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
<img src="https://cdn4.telesco.pe/file/OqEMc-0B_TqTU76iXe6lEFkpb9JMDhqk83F8EKJJ7lxvqFIAdr9Cq5NvMniWFNkpUlKgig61HnISHNpZpcArr9S62-FMGQGR3Z7o1hIc9twzrDgMU0Z6Xe3rCQCbcLyySCQU1Z5v3LDswpeSEG_Id46UkT0n8fVusbkHeGjExLcIc3XJfdHCkgyJaWRU2BwYPVKuqFyHrPNbiLhi5GM-cFUnvVuC7UztBBJjL7AjaC2yA9dNmHZuZqIP4kyyNYE1Z3Te66pM5GlzRWDC8TH5wlFgcFWvqqj4NXNSIpQpsPovNgNChDwN4OxHAXEMFMxmnKrGPBtMZUHwdo2fy5uIpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 20:18:30</div>
<hr>

<div class="tg-post" id="msg-435979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3438c891.mp4?token=CurMLxbvD3GEQOMAgp2wYb7jQ5iN7eePDZes2qnjVkvwMmbNhf2J8YAX7p3GkZ8biNtInbX1syVrd2MKiepdWzYkpa3cBAfqqhrr2Z5YNoKgbQKKKl4cVhtLJIeAGBtE6tPhcPbbHWAeggsljFQqtehQx9-nJvuCf_zQSVcSq0SUYsOdbGv4Rv9aDkJnfTHwqSQjOA8J-2BkvfPLGS474Uc0LKZ7jR9s-Tav_8quh7zhaZoyo-_NLNaYB_dIfVhx-AUQVGkBr6DJ5hZZUZIdRRJkiYKt4kcUBuWl0V3yk6tfFlaGoUC7c43_0n73GtmEyDWJZzR-LoPQQZ80IAprL1_vaFwVBPxSqZfoK2vkYcWcjBfOWv49nIE6Pbo3tf7r4db893LGOcnyOCq7BqeqR8AVNtokfk8Llm5pShk1lXZyc1Kq0PBVZ8Rn1TnHWArDth6J7Sk2iV0U1zO5Eh6EW3p0W0HSNLo25sNg5x9NMxd8TCM0yERcTV6xviGJdNfu27BRggl6ZgZK-uwocl5EjT1s5LXm3rlK4m0UOaCOUqGlVRRw2KWVhqWZ07KU-ZzmCnG7XxHelhN5RrqwXW1lHfLUFHKiRmXqMN5OxNEanncPtOkiSotX2F-Evf7XnnqDBFn6iD-G-YMWvBVVXwJA-fbAxYuzcAfpTmQKd5cPuaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3438c891.mp4?token=CurMLxbvD3GEQOMAgp2wYb7jQ5iN7eePDZes2qnjVkvwMmbNhf2J8YAX7p3GkZ8biNtInbX1syVrd2MKiepdWzYkpa3cBAfqqhrr2Z5YNoKgbQKKKl4cVhtLJIeAGBtE6tPhcPbbHWAeggsljFQqtehQx9-nJvuCf_zQSVcSq0SUYsOdbGv4Rv9aDkJnfTHwqSQjOA8J-2BkvfPLGS474Uc0LKZ7jR9s-Tav_8quh7zhaZoyo-_NLNaYB_dIfVhx-AUQVGkBr6DJ5hZZUZIdRRJkiYKt4kcUBuWl0V3yk6tfFlaGoUC7c43_0n73GtmEyDWJZzR-LoPQQZ80IAprL1_vaFwVBPxSqZfoK2vkYcWcjBfOWv49nIE6Pbo3tf7r4db893LGOcnyOCq7BqeqR8AVNtokfk8Llm5pShk1lXZyc1Kq0PBVZ8Rn1TnHWArDth6J7Sk2iV0U1zO5Eh6EW3p0W0HSNLo25sNg5x9NMxd8TCM0yERcTV6xviGJdNfu27BRggl6ZgZK-uwocl5EjT1s5LXm3rlK4m0UOaCOUqGlVRRw2KWVhqWZ07KU-ZzmCnG7XxHelhN5RrqwXW1lHfLUFHKiRmXqMN5OxNEanncPtOkiSotX2F-Evf7XnnqDBFn6iD-G-YMWvBVVXwJA-fbAxYuzcAfpTmQKd5cPuaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهلوانی ستارگان کشتی در میان مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 94 · <a href="https://t.me/farsna/435979" target="_blank">📅 20:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGJyRGFgEkM6BYw3Tt4w_8_TEJvgTqonxU-MnXZRunwH6_cbSXLwaTx_NKXDFn72QUfKnKrJzZ_Nd-OFwrX62SIaB60_2t1wAIWVifsPLjyp4ya-jjbcdrRtOOCWJSBgNhPkC8erKdaDlgLLvU_NHrHg9sCTkQ7TAamoMdFSswpsrK6je5voAkvt6oG39N1hGts-8RwI4EM4UB5e5VG7RG_j-ol90dxydQOeT-dKwNGe6hJIATv-OiRMUQUClH4cfsIXu3PqASpRIVV9EIgzHjsww9U0Tybof5V7W757l8sH9HR0wq4ZqZwyxuKpr2B50w99f4-SqqBFNXDJVZPxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌اتم: ساخت‌وساز‌ها در نیروگاه اتمی بوشهر از سر گرفته شده است
🔹
رئیس روس اتم: «عملیات بتن‌ریزی و آرماتوربندی ساختمان‌های واحد دوم نیروگاه اتمی بوشهر از سر گرفته شده است. متخصصان ما که در محل باقی مانده‌اند، همکاری فعالانه با پیمانکاران را در چارچوب تعهدات قراردادی خود آغاز کرده‌اند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farsna/435978" target="_blank">📅 20:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435972">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_MkoY1Ran_XQOFcT42LlckLd85yYBzLxjCfbJIexakQqScjgflpdia_CUtqjJRCstSSgktpWPgJYzVctL8oWrNek6W09piG6FMOvpWWuV3LBaiodNcQCOkUWA_whuYvXFiDXHPTLa5Hpb5skD_L-5UGqIQEqu_7XUhNEsM-7FnKmAjSb1bd2JuISFVEyRXy-VHml5ZLQi4iyg-2D8AbwqvkOS21zcvAWHEAspOFbujw9JPkGBedql0zyCEXPbu--J-eiBwzFS67SptuJwKbNIih4mnmNq5oUqkk_m9_EzkvP66V3fulz2nfL-un44vKnaf3N2D8V3BcZlNezeDt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AHrUJ-q9lnjsXVEoh5lC--hIperwCNk4-gfcqqjFIjKz-psh_oJZbBG-lkbLCw0MDtKY8aKAbmjyskKIEbnTgvz2bjUtypT-aoReJT7ETKv1Ng4IzQmweqI2RhUlnUWkv6C7iwIWtkNFne8CBs4QNwHKV0jdtNSuG9H5KY847jJ4_O1AoJHzArs7cFiEkpysCyCbb3EyoJY31R_HOXGbC3D3VwIADGtkyZokWcX0EpFPZawaQUd3cv2YO-D7dzKzicTAK1MmGd82kAT_NfnCTmcJMCPXq50Z3pgElfMrZRaZH2QWAoWjp3EQEflXphNxarFCIG--dCIu4LE6ughJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sATRFv2-CDdhUamYmjckxkwZz7aQVZhP6Zc5LtTCH9SGfIJ3ZwZFhHlxwGmH-3EoB0HrJvPu67VUg9l2XHUclF4NZKPIcotq-4Q2d7iNohQC6SsnrCFSPHRCHSSLyzeb127C5moyKIvhe2896KqvBxaxOcMI6cpOfd35LNsTGuQpy5GXDwXmn8resJehAxQ1tI43c20NFwOQl1LullRUi0uJXidFmed2BCXCbobiRHl_CWao8Ch81GzBlsLelevw3fwdVYsSQPjxOZb22cg6kTXBj883N-C_tVzOqNEVrwzg-x4vKvs5M1aMnQkfslJgPfMsN2fV3mHUvHvBRP53JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rKH6YRu_g0Hp_s_NxCvEH_wY9pnrbSTizMC_ozk5aK8N_tNaSO1Xm8scpi0IpWee31U3dczd7Kcs2zwFWw_LGBeR-qQMdKTiLdpU8JN0D7gKHvR5Q0voNlKMc5rvX8eZN6lrAuVgBHj1axx8GIaswFHwjUp2sENwoBMo0Ob4j0dO53TKUPYzHtRPDzaoSyxy_Nncbua791qsW8ZV6Fz0bdn2ZZ41XLSfStXdzE86qRPveqvYyz3SSMkZ6vr4if7LP1X9zTNJclw9sNxcl53zOlWef6FUcjFBZGmKe6Kl-E9Oy52nQnYlt2Q-s0OJlYLFKlWrZVorSIitu9G7I0rEog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzGXX0qWnDOXsQ_aur9DC59bvY55pNVUfuT81AbBlAZLSisi5My43l95q_9ODfvI5gyxOa4SuliKLKrjN0zUed50MaugefXi7pToN1cbu8WfcqCeeWAu03haBLbj8TBHspGl64PVkl4vFcoWtggKWPK6QTfcE99JPOaG2g1J98Lj-n5r4oj7bbnVy3nhYRSrf3poWAg_RKPb3f0tWDSws7gYIje9HDGj8hkEcJZ_5-Il6EBOy2DKXM2Pg7p-e84Kea2Ntccjf-FoG72R1s543aO2I6qJEoJrmfRAeutIOe2A18ZpkzWONE7G4FY96q_7sNHfz8mxm32tCxAFiXyIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzDtauggh3zeKR3HC7AtuUieC4cH5ixUWfzm434vN8tmdml8FPnYiH9aiu82vLkh0-JF8SEF5LRYxgx8o69khmoHdZwZ5MTcDDmMe7Q_i0v-HubLkrEtTDvMDkDsy16p1JVNTVekqYpOwyIcOMXf1kyNO8yK17AJHoq4vs-Fb0VT5eg0bYX699SaQbHnMSMIbTInQvIy8ucQMDotlAirobtKimJ2N-wSC4uVVgOAdz2SyXjzOQJ33WSKUgKj8iBiPni0hN42-ytLDU2pQiSJ27wpoVDTdaF-gJiLTO1i09yJYfxtNbskC37p0_sQaU_2dayHzvO1qWhXrAW9krKkIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طعنۀ تصویری هنرمندان جهان به سفر ترامپ به چین
🔹
سفر ترامپ به چین واکنش اهالی هنر را نیز به همراه داشت که البته همراه با طعنه و تحقیر بود؛ برای مثال، کمال شرف، کاریکاتوریست یمنی در سه تصویر ترامپ را تحقیر کرد: اژدهایی که نماد چین است با یک فوت، ترامپ را به باد می‌دهد.
🔹
اکونومیست نیز تصویری منتشر کرد که در آن ترامپ به شکل فردی بدبو (که اطرافش را حشرات موذی گرفته است) در حال گفت‌وگو با رهبر چین است؛ علی نجدی، تصویرگر جوان عرب نیز با تصویری با زمینه پرچم چین، ترامپ را پشت سر رهبر چین نشان داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/farsna/435972" target="_blank">📅 19:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435971">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec94244e4.mp4?token=iG2pafpCiBncPw-iRAeXXkAel8hYPECoKnNX4ixbs2FiGOVWffgRYe69WHqLkE980fZ3tZIoXbYlH030Ni6ja2NG-XE3HsyW2jWYI7Fs2uU14DtJj-sQuKVXp_ymndoeibHK_mp-tQFKFlJkCTR5-TWNjwcFD23hxA2AFTfOGcRHXCeLxKFaKorONWEA3p28DJFhf5uuLSf8a7ZcJhMhGzmw42A0UOEZ_1vevPRSpA8OEtQCbSRtbjNl2U89O4-KS9kRYZk6VxbLiZfjgKA-Aw1u26Z9YpnQeBsKED-Xo-firkdDoNxQ0ZibRo4sB-ffou3mFQeYctk5QSNXA9b1srvJEISydtlIkkv9rdFY-lS2wvopEN_qoRfBi-pSSAYDJ0IPupnh-QjjE_eLfzypAMuIdntyxLPpMEaVfWk7U692OIm8wz00EmY7Is51U6XmVMMZYqSTgNicC-AKZqueTOL933Im_XXD8EXQjjKRjKZ75BRnJDU_7ZLyEK9sb8KFuXwXA6Z3Ws5EEpagu_CrAwvUC_ZxZq2G_kgmuHkce_h3OUQMRWD3G7Q8ak_khsqNziP2w5lbFIusunIE1V117ifHPu7KeLWKk-ACqHj4VBMfHUlON6P_Iaje2t4xBKYGiITVvLQf4tXRsRlila46J0GoNVC1h_S7B-JK8qIInMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec94244e4.mp4?token=iG2pafpCiBncPw-iRAeXXkAel8hYPECoKnNX4ixbs2FiGOVWffgRYe69WHqLkE980fZ3tZIoXbYlH030Ni6ja2NG-XE3HsyW2jWYI7Fs2uU14DtJj-sQuKVXp_ymndoeibHK_mp-tQFKFlJkCTR5-TWNjwcFD23hxA2AFTfOGcRHXCeLxKFaKorONWEA3p28DJFhf5uuLSf8a7ZcJhMhGzmw42A0UOEZ_1vevPRSpA8OEtQCbSRtbjNl2U89O4-KS9kRYZk6VxbLiZfjgKA-Aw1u26Z9YpnQeBsKED-Xo-firkdDoNxQ0ZibRo4sB-ffou3mFQeYctk5QSNXA9b1srvJEISydtlIkkv9rdFY-lS2wvopEN_qoRfBi-pSSAYDJ0IPupnh-QjjE_eLfzypAMuIdntyxLPpMEaVfWk7U692OIm8wz00EmY7Is51U6XmVMMZYqSTgNicC-AKZqueTOL933Im_XXD8EXQjjKRjKZ75BRnJDU_7ZLyEK9sb8KFuXwXA6Z3Ws5EEpagu_CrAwvUC_ZxZq2G_kgmuHkce_h3OUQMRWD3G7Q8ak_khsqNziP2w5lbFIusunIE1V117ifHPu7KeLWKk-ACqHj4VBMfHUlON6P_Iaje2t4xBKYGiITVvLQf4tXRsRlila46J0GoNVC1h_S7B-JK8qIInMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این روزها مردم دنیا ۲ صحنه از ایران می‌بینند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/farsna/435971" target="_blank">📅 19:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435970">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hk3wpqTw8uZdOtveQxOuo-3mEVp-BJTlPMViIJb9-ijLYGG14vBLeACWcSu2QsiPe1KgnDOlFSB10BBKbDGwW8qaG47bbOWFSdBwOJfnVdxOHBpEg7OejQ9rE8bLdsCIX7pPwQNc-UxM3kBI7Qx6Nz8LxCAIkMkggPu6iCg_4CFsyBj7-_KP5HF0GJ2o3cIVLfE67zaIk28wTmkAog-3yk5DN5btGS8q00bHVCRQeCVGVEYNXIV8R-ItCktlexhlWXNwjbWwwiGOFqyiUz0tA1d_QHVP8WubEom7viqlifKc2lVvaCZVW2UPfcLSoMlMqH9RVSPRe5n3dPIIcPobaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: سرو ۴۵۰۰ سالهٔ ابرکوه ریشه در ایرانِ کهن دارد
🔹
کهن‌ترین موجود زندهٔ آسیا، سرو باستانی ابرکوه، با قدمتی دست‌کم ۴۵۰۰ ساله، در سرزمینی ریشه دارد که در همان زمان نیز با نام ایران شناخته می‌شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/farsna/435970" target="_blank">📅 19:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435969">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5297611bf.mp4?token=A3wzdBne908GD5a5TJF1f059htIJDqvdaUiin8Fn3ij9LGevYeI713Z7MoZhaU_a0A3Amje6YbdvVJnAI5xuD-dT3q8yFctbix2eF2mnL9kC-RJTyUMsjavpxF7sJmb7BF6G5x-JgmxxrL_UyjiV2XLcwTEsVGxvg0c-WeAycVUs7pJ9EUjAvYag2dBxO9tVVMW171ZC7h7eQr71NBz4HkG-jCdIerwhJC-pr69rgZrwdpqdipz6EzQpd0ZZcL6KRq-1s5Uh3TMVkfTSAZ8VlSYfEj1jHoHss1wasudYoCKyiQ7Pbq8E0BFk7FVToJMJcHRUyRWFFmvdQQLT0b584A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5297611bf.mp4?token=A3wzdBne908GD5a5TJF1f059htIJDqvdaUiin8Fn3ij9LGevYeI713Z7MoZhaU_a0A3Amje6YbdvVJnAI5xuD-dT3q8yFctbix2eF2mnL9kC-RJTyUMsjavpxF7sJmb7BF6G5x-JgmxxrL_UyjiV2XLcwTEsVGxvg0c-WeAycVUs7pJ9EUjAvYag2dBxO9tVVMW171ZC7h7eQr71NBz4HkG-jCdIerwhJC-pr69rgZrwdpqdipz6EzQpd0ZZcL6KRq-1s5Uh3TMVkfTSAZ8VlSYfEj1jHoHss1wasudYoCKyiQ7Pbq8E0BFk7FVToJMJcHRUyRWFFmvdQQLT0b584A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزش باد شدید باعث گردباد در اردبیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/farsna/435969" target="_blank">📅 19:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435967">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شبکهٔ ۱۴ اسرائیل از شنیده‌شدن ۲ انفجار در الجلیل غربی خبر داد
@Farsna</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/farsna/435967" target="_blank">📅 19:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435966">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌ ‌حزب‌الله: تجمعی از سربازان ارتش دشمن اسرائیلی در شهر الناقوره با ۲ پهپاد انتحاری هدف قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/farsna/435966" target="_blank">📅 19:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435965">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dce83785a.mp4?token=AkYYZq-XUl5psoC5mC-J07ypsyJO0teNgIicyuTVBMBOc-UIri9Hql-JgbxWqqXPhpR5ste_7b2uQLPzserVjuMIw6oCMM6qRaWRmqHSMaP_JsXyucnQCgxjZVCgd8Iho0zPUxDyBd9Xaq9inUPq2wrC4ACScCDR_1rC3QjZSXfGgwQvSkSEudk9SRlwVvUR3B_S2jYIotFdbN4nh_Y-WwnK5HdcuJmVsXVPewmGCIfrqgsJucQcnWYFB_Cq-OYlOBuCQR61V1AyId2-uMVFvOTZa3alJjiJ2-bMOJZeORO_PsKxWrI01lo_lwXpxZljogdnZLeGpWYqpXZCT9Mrwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dce83785a.mp4?token=AkYYZq-XUl5psoC5mC-J07ypsyJO0teNgIicyuTVBMBOc-UIri9Hql-JgbxWqqXPhpR5ste_7b2uQLPzserVjuMIw6oCMM6qRaWRmqHSMaP_JsXyucnQCgxjZVCgd8Iho0zPUxDyBd9Xaq9inUPq2wrC4ACScCDR_1rC3QjZSXfGgwQvSkSEudk9SRlwVvUR3B_S2jYIotFdbN4nh_Y-WwnK5HdcuJmVsXVPewmGCIfrqgsJucQcnWYFB_Cq-OYlOBuCQR61V1AyId2-uMVFvOTZa3alJjiJ2-bMOJZeORO_PsKxWrI01lo_lwXpxZljogdnZLeGpWYqpXZCT9Mrwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم‌هایت را ببند برایت یک داستان تعریف کنم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/435965" target="_blank">📅 19:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435964">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61032176c.mp4?token=vyxLS5fL7gvg3ez5iw5VXNzDQx5ouM3yE_YjmeP4vh1BZWOt5hTnVBFtC9kc9FLjeMVTQTE1_z5Lmoy4v16EfOIDg3EPid4FQceAPMYcro0do6b_RSvuLEBUSpA0749abQ2FqIThsmXiQUCQKY4TdiU4XcrwdA0qU3KBjHaGFYL_XypBbGFvQ3qYP7epbO5swhcbM_cHXgJbbGFRAKfBLibM8KIyfj9uguPkxBRbVZnTj8_DHCfMCuMO3fEbt5TLzWReH7wc3Th2Z7YCoYpAhMGONokJ-NNqsANX7AfAQ_sxXtsc3I3dA4He45uZGdiXLOUvRAyt4MrgSoB9sbfMqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61032176c.mp4?token=vyxLS5fL7gvg3ez5iw5VXNzDQx5ouM3yE_YjmeP4vh1BZWOt5hTnVBFtC9kc9FLjeMVTQTE1_z5Lmoy4v16EfOIDg3EPid4FQceAPMYcro0do6b_RSvuLEBUSpA0749abQ2FqIThsmXiQUCQKY4TdiU4XcrwdA0qU3KBjHaGFYL_XypBbGFvQ3qYP7epbO5swhcbM_cHXgJbbGFRAKfBLibM8KIyfj9uguPkxBRbVZnTj8_DHCfMCuMO3fEbt5TLzWReH7wc3Th2Z7YCoYpAhMGONokJ-NNqsANX7AfAQ_sxXtsc3I3dA4He45uZGdiXLOUvRAyt4MrgSoB9sbfMqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رخت عزای حضرت جوادالائمه(ع) بر تن صحن و سرای حرم رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/farsna/435964" target="_blank">📅 19:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435962">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfDzm1HmzvVMoJm2t1aDE58zDIc3g-oVy3iM2ut4QZsZjOzvhafKgzbrMTsaSt_irpabC9u-Vgf2b5XbXff6fbtT0o7PWI6Zs2EjFZiHQoZKSBwDj9rDjjfYli5h-bK1-jCcPyz2hrSvFeH8_HAYSgchbzEiKt9Cklgej8veRFIJ2-RtMTP_mNTY--_1_9hl1iGWkI8oWvH6_BeFfquGRpTwki5311UK0jqOg5fIRdMOYqGB14PcaFZXnq7K-4FF1apDg2LD12Rhk2LafcTqpBvgKHiVIJ03_5RBD8HO2VmnNrocAdSxwxqWfeAnKAnOFVBnseZ0kJQnm2AVzsiiFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8148f902c4.mp4?token=iHbbU1sokrpGzTIUJbZWlpkAB7CWlHY1ZjU7kj4s3drUW26RBPUm6ut8-XngSTHv3EIoWpcSeoOf_Q1ZmRkRP6qsWXzVNYMEJ09Qzuxg0YIiM4WC3T3ZRUcgGtz8lLV1fP6mbzLPLiyJ_eYr8eIAa4O2kiHYYnM7ZppmBkOq8nPzG8A_wi6e5cbMEogLdbx-y9FqKq031HPepvl0P5Z4NEM3wgwd7WUt-BJAmdxLG79oN2FX3uFMpEv42z7ZbefoDjuaRBJ-aas0KQHUtlggTWKGoZSmFncCMXb2GstljVAk5Ncfo9V3PejY5oJOoCkMSiDbteUSOBHftPg3Jtm77jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8148f902c4.mp4?token=iHbbU1sokrpGzTIUJbZWlpkAB7CWlHY1ZjU7kj4s3drUW26RBPUm6ut8-XngSTHv3EIoWpcSeoOf_Q1ZmRkRP6qsWXzVNYMEJ09Qzuxg0YIiM4WC3T3ZRUcgGtz8lLV1fP6mbzLPLiyJ_eYr8eIAa4O2kiHYYnM7ZppmBkOq8nPzG8A_wi6e5cbMEogLdbx-y9FqKq031HPepvl0P5Z4NEM3wgwd7WUt-BJAmdxLG79oN2FX3uFMpEv42z7ZbefoDjuaRBJ-aas0KQHUtlggTWKGoZSmFncCMXb2GstljVAk5Ncfo9V3PejY5oJOoCkMSiDbteUSOBHftPg3Jtm77jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله راهکار صهیونیست‌ها در برابر «FPV» را به سخره گرفت
🔹
حزب‌الله با انتشار تصاویری، اقدام ارتش اسرائیل در نصب تورهای فلزی برای محافظت از حملات کوادکوپترهای مقاومت را به سخره گرفت.
🔹
حزب‌الله در این ویدیو بخشی از سخنرانی معروف شهید سیدحسن نصرالله را آورده که او با اشاره به آیه قرآن، گفته بود اسرائیل «سست‌تر از خانه عنکبوت است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/farsna/435962" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435955">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqG68xyDFNSzpXW9v8khJwGKWiotzhHXsZXj1RQHyyvxm9xUH0A8gZiGjcB3K5ELiHZeR2hL_6WQSDORk0tCGGwdw_zKMOIRUppw2SdJeKXpx1gfjD2J3rg8wwu7PNKiFGTV8L6RUMbVgeI2sDh3vdNwit00BgyMyvC5CbRPC9cbjaGuqIS8_kOH0PozCWYOOlkyLKyj5rP2owb_VQKNYW4Xpw6koJmlh5I56mRJEyOSrjC3ILITXOAgFTmMOwO-_TspNsCbB8bIaBTqUWgwkZAToIwdNBT8DRwjhZ4P7eUtPLd04ztYsWsQRoxchF8pLQAjhyCd7fUWXZiXLNFZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8YX96WknMUmpHSMOgOmSj0bGMuuebRrmfYGj1J0MTsmssKLoZ-qWO_F63D9mzSDt6UkUxJKasTcmLVjBtIuJ54dplLL2yTtVbMbITnos0aRWVzVZiCxKZ66wOTUW_Oq_Gx5ap3N4by8c8Sdoz7fhDUhKWM63ZIQuwSpVpywNre-7KSlAA9vl49amMQO6ZVg-K1cErBHCpfMDXYj-W4U83kfoABPr1GzqnsEXAqoEk9xC6_Ce3D4VHlqiYQ7q_8dIczkAr_O9fJPe4MQ1-okjOX0B27lLkbpGD1ttbUOzOXHTqWqsLl9g-G2kz-Qxenl1CaVRC2MqXFiV_pBo1ZJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wz08Am-AJDXsetI6pkH8wNt_XbIfv8IJGoydAjwZ6rSm45P5xOvUKo7VWvgwK1JbCzEWvqXqhGEHPBQjr_zo8IRiif1YKbpwUihJX53hVWyYf6OVLkGA6f7ZIrsSI4ynzHJBcH_fGo6Nd9OW_HZNP00uzYjTj3pk8w1f1ND37icjqSOqWzFGG_tisWkRVhSJnfaQKWuIrMpGCFajxpDVQFQo0Y5phXa3MCgtTyBhS87m_TCA8D8rI7hzymGTyqheStsEXxzLXg1HomR-SMH_khDQsa9goruIvgFit5eC2p8MWfQRG0VNnCOiTECof2ntCcSyXp40eD3-gMO2jvSN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRe1-WFR_Xa86tthnlN2wSBSfug-nllNfT3PYMSt33f25EUYdkQdirhljpmw27MgQOmjDzJim-DyCTj9nMc0HJ-U4XtdkzE4KwkgYG5scNA15EKFaKiOSi059lwvFPB4AGp2q2B2zBx-bSMv-LIEj_D_rqCMrO1vG2RkyG8L7SM_LDmcU_Fi14CtDnhGthFuju7Mcr1IYBMWgoY1tIYDnv7wLV3HXWoNsHxxnu18cv84k71qLcPfmcrS4gyRai9N8mo8MF6jF6yWUHLRkfBjhfkVVhO-9WJz31uuN9ACqi6IqGaETatEEbbT7nTsK97BHI6mPAXWXGUeBYTNcefDyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/to-aldTPZcWbZlkO4NvKh4cexqPsIcrvftrUsIvqtX_KwPF4qFM7QNDm0h9-mq64b5wWzTQC3qU9FO37gIs-zTYspx-ZCjuWnkiI_LdRmrG3pvbyVd7o0Ze3OFqffvGPQF9nirZVtBHm-6KEPVsaYeYabZeYu8c3YlEZkT0NrJbu739T7vmdFEZrMUvSUjSu5vvyYG4uFm451PzxARKSLaQqbnY1KGeZtmhQOjuY04mIfMlJ9U-eODJ5fhlgt05Y90JjySE5Dneje4Wi-Oh5A7fl1kT0g2fRdq9OSjhwhRkTFnIqBM0tHKrwnq21ZidgGpQ3g18BOv59kRj-jhss0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yt0zuaPb2TcQnpYbXyAoYv55uu6Z6UJkHJcMKKG5EZiW8IPm4CyAMllQzMn4LniS5LHTKZ5jc-lGCRJ54GypvP48HJTF5fFPujrTYil69SgZGaoIGFmVkulfDWEfigxkHwN-3EDYoEYc2Ayr_uEoZ7I0CkIYtwRXF6Lsu1_8ZuK8MzoPWTAFuwLveJOow_fiwuC2EVBygCZfuosyQF0GN3svbhqYvHtM30vYcQ4VYKtVlKUwqv32j8QX3XisJSvXQjBLQz6vdWYQGY7Kb_iLpJZDxGZFHITJprV2m5UiTo63VoS4rt2tQV2Ymgyu4g7OZH8uSaojczxW3LG4QIJ4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrFYkYTZ5aGh-j4eDTHlup2ExiLm9zhoNwYi5Z3GENhEzm6jxmk7V3GyjtW3u0KTcvRw8lGjgYo1e0SUq9B6WTR7Jm2j6sskHk4f3EmWQymC2VD_CXM0bv1w3ohITRXtNdZDqhMiEIGtXT8ahAf3v8umi6PXomYVY-YDcq6qcA59KyUDcSKOWw78nadL2bN6LtrCdYWRc4Bq0oVXpIfNwJWm0QgANxNXOHiuo_fhfkQeqhBXaKzlY7WB9zcvI7KVr1H_lPGdi-LczTnvXxAKiBTT8oIDGZkMRGSm90GmuDpHSeTHkKsqg1oXSCV7YDlSPtsmjgMlGWUXhD7ZifgH4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جریان زندگی در ساحل خلیج فارس
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/farsna/435955" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435954">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsW9-4-b6p9dPMZ4yQMdJDIfJ4lEDG-G0xDkyf5Ql2mV_GiJEPRy1T6JC3QIUgcBVhQmAZC_SsZLq0M-Q6kA3xPVL3mX24nCJHK1PXxtsSMJHsHTLQrUpdCbcRempiP0Gc2g90lnw6tO6muKG_0485_S9nu4dtYL1NIJWYWnj971_xfs9fqMGUlUSGJDU6hdMuKHu-1lcZGLBJodCLSsOvD00o-nk2HeHor_RxWgPgUdn-j34fsgDT4vSrNHDJgKGYtCad4VhgYlVpVPYxMfjhf_xJPzsam5AvFHT9Y2X15tvek92M7d8M85vchcvfSA34M27u8JAnAK6-wMZePOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین از قطعنامۀ پیشنهادی آمریکا و بحرین درباره تنگۀ هرمز انتقاد کرد  سفیر چین در سازمان ملل از پیش‌نویس قطعنامۀ پیشنهادی آمریکا و بحرین دربارۀ تنگۀ هرمز انتقاد و تاکید کرد که محتوا و زمان آن مناسب نیست و تصویب آن کمک‌کننده نخواهد بود.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/farsna/435954" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435953">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@Farsna.pdf</div>
  <div class="tg-doc-extra">1.7 MB</div>
</div>
<a href="https://t.me/farsna/435953" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">موافقان و مخالفان حمل و نقل رایگان در شورای شهر چه کسانی هستند؟
🔹
همزمان با نزدیک شدن به پایان اجرای طرح موقتی رایگان شدن حمل‌ونقل عمومی در تهران، برخی از اعضای شورای شهر از بررسی طرحی خبر داده‌اند که هدف آن رایگان شدن دائمی مترو و اتوبوس در پایتخت است. قرار است فردا این طرح در شورای شهر تهران به رأی گذاشته شود.
🔹
براساس اظهارات مطرح‌شده در شورا، ۱۰ نفر از اعضای شورای شهر تهران از این طرح حمایت کرده‌اند و معتقدند رایگان شدن حمل‌ونقل عمومی می‌تواند به کاهش ترافیک، کاهش آلودگی هوا و افزایش استفاده شهروندان از حمل‌ونقل عمومی کمک کند. به گفته موافقان، این سیاست در برخی شهرهای جهان نیز تجربه شده و نتایج مثبتی داشته است.
🖼
اما چه کسانی در شورای شهر با این طرح موافق هستند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/farsna/435953" target="_blank">📅 18:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435952">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کپیتال اکونومیست: درگیری طولانی با ایران، قیمت نفت را به ۱۵۰ دلار خواهد رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/435952" target="_blank">📅 18:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435951">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صدور دستور توقیف اموال ۱۲۹ عامل دشمن در آذربایجان‌غربی
🔹
رئیس دادگستری آذربایجان‌غربی: دستور توقیف اموال ۱۲۹ نفر از عوامل دشمن به‌دلیل اقدامات ضدامنیتی و همکاری با کشورهای متخاصم صادر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/435951" target="_blank">📅 18:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372813d6e1.mp4?token=FIsvv-vPMwC-4xhRBdd2W0ZYzLXJAKeGkjWTX_z5Yym62GPXcE0XbNcSwuyDlIS6mwjZALsDyCqVIYWEUJRbwFKvh-1f0koCchFsiR2nuOPAv-L-ReP8z4W9AUFkiFQHdO7Ki3Q0Ml0mjPKMK3rkrcsv8Cig_lXDDhcbD0Xbdd5nuek2fskZTziTXBXxC5yT9MlcbBhbpHjqDeMEo-LmBtFD6LavOg9sBH_FEjKfdLQpuu-jbMigPSjUwnEV85ZAgx7zc-61k6Q7FLuHe8Pv7GoWUwn1qHZw0WZtJjL1NNJ5H7KPOSD_lkadA5_ra06KumlZPBIuYi-ZPEEJ59SAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372813d6e1.mp4?token=FIsvv-vPMwC-4xhRBdd2W0ZYzLXJAKeGkjWTX_z5Yym62GPXcE0XbNcSwuyDlIS6mwjZALsDyCqVIYWEUJRbwFKvh-1f0koCchFsiR2nuOPAv-L-ReP8z4W9AUFkiFQHdO7Ki3Q0Ml0mjPKMK3rkrcsv8Cig_lXDDhcbD0Xbdd5nuek2fskZTziTXBXxC5yT9MlcbBhbpHjqDeMEo-LmBtFD6LavOg9sBH_FEjKfdLQpuu-jbMigPSjUwnEV85ZAgx7zc-61k6Q7FLuHe8Pv7GoWUwn1qHZw0WZtJjL1NNJ5H7KPOSD_lkadA5_ra06KumlZPBIuYi-ZPEEJ59SAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط یک شهر پاکستانی به دست جدایی‌طلبان
🔹
منابع محلی روز شنبه از تسلط جدایی‌طلبان بلوچ بر شهر راهبردی دالبندین در پاکستان خبر می‌دهند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/435949" target="_blank">📅 18:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133f7d7bda.mp4?token=vvH5lwL99-19l1Kq47ivM1f2Pg6FCsIjHDMFhSJrIyA3R2bR2ViR3hZ11RfbxxgcwFGFxSl9FILGwM6DQJp0Qik0msbahdAis5dznO79VzGiFnbe2Rmdequ7pYK_scZ2tPoNLbdIroPR5JvDcturtoWe7UYlPPXTvXyGlYAXcIAyUnV_m7DJ49PQkBRmMAyw5nmvZgRwwZ1oBFgDtRRRb3-xEMw0KBJTQgcDTzEmBiOY-EjlVjEaXuweWPgNIOjso6OKK00XoacXVX7U5ac9jKut1SFt2ufzSgHXYVvzxGJGNcHGCnei_5FFjViKZbVwQprOjWd_05YhWt1kF4I_1XEJMUn1mJuFL_BLgo1jnkfgH0YVeBsLm_7ltDdPDJmJESeSVSupamUcZynfm9Gb749C_O1oQ4DkNa8c8v--Ukt11o72HtB0Z98Vsb-b-j6IPndmgKHonRp76IqGBmrCpcd5oF-wFcyFZo-Gl52N6TTqRZJBEorVvwB2Ygzk--lXhUbmQREgsFLcrT9l8xsSpO0ph56U399KfGa_9hEOGwHINBWemFLsx3t_bV0iBx1eELWkq4LJ8B2K_h-U4nsnk0OoW9irEBJ-T23Zxiuf4uWhlR9fWs3WaoIDa40qtkyP9RiRE_yrVb3dFeCqGFpdEVBzuoIG21Rd6yJRAc_Q-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133f7d7bda.mp4?token=vvH5lwL99-19l1Kq47ivM1f2Pg6FCsIjHDMFhSJrIyA3R2bR2ViR3hZ11RfbxxgcwFGFxSl9FILGwM6DQJp0Qik0msbahdAis5dznO79VzGiFnbe2Rmdequ7pYK_scZ2tPoNLbdIroPR5JvDcturtoWe7UYlPPXTvXyGlYAXcIAyUnV_m7DJ49PQkBRmMAyw5nmvZgRwwZ1oBFgDtRRRb3-xEMw0KBJTQgcDTzEmBiOY-EjlVjEaXuweWPgNIOjso6OKK00XoacXVX7U5ac9jKut1SFt2ufzSgHXYVvzxGJGNcHGCnei_5FFjViKZbVwQprOjWd_05YhWt1kF4I_1XEJMUn1mJuFL_BLgo1jnkfgH0YVeBsLm_7ltDdPDJmJESeSVSupamUcZynfm9Gb749C_O1oQ4DkNa8c8v--Ukt11o72HtB0Z98Vsb-b-j6IPndmgKHonRp76IqGBmrCpcd5oF-wFcyFZo-Gl52N6TTqRZJBEorVvwB2Ygzk--lXhUbmQREgsFLcrT9l8xsSpO0ph56U399KfGa_9hEOGwHINBWemFLsx3t_bV0iBx1eELWkq4LJ8B2K_h-U4nsnk0OoW9irEBJ-T23Zxiuf4uWhlR9fWs3WaoIDa40qtkyP9RiRE_yrVb3dFeCqGFpdEVBzuoIG21Rd6yJRAc_Q-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای سربه‌زیر شدن ترامپ در چین  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/farsna/435948" target="_blank">📅 18:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435941">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnJh71IbW4LjEIsrKwOrsDWGqBUAsUs896ASWJjITS-cfNpqM0cgr5d-7X5B4GMS_UZHVJpzORwinWZn-3x9d-hiUP3CTOYS8MBsG7Y-5ZvN7I3cf1pQ4D7yLKA7mBA4GAsnpCkfKja8nGftdKGLHyjakInTQm22U5mkc2nQN-YFB5BVY6-ORwxEtCI7qsJHsvjkPPF5w11mkIg5tqca7T_jJcpFYuaXKq48GxP_sUzL3osnYJjlX3-vaae97U_qddJRfnh06hMWXUkwk0Wb_c7prMO5Dj36JYKFWj__QgIicxed3LlAi0Hl6KKogzpdJJtn39hK0m8N6HRZ-OuG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLlJBpOqHSLMLSmFceiIpzKgk8mpCQzsi3CdEGZuYikpFp5lhEF_ZQ2b1vyY9lcpZzUAzE68Xm1n50mKooK-loTHRm9nMLcHPgTO4SjCvb32IO5JSPTK8JcJWE2u1wAeLomiWwXkR5rr54tdbAuA7oeKfbuoCvjZjQ4rtlCM7883eRqHp8iO1QuNEmhAjmht4SxQwCxqA9vRx-rLYwfWqsiDCL9WAwRpSohTGn0a293PtXwOkfMNZU8NnDJaQAoD8hC1zc0SfLI4s8DrKIYxeS7dD9ZyeXTqOYoAMxxzrva8vy9tsmAhr20VxfNX4O7CmWh0qkjdqDPw8H_NDcNHsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJYydWuwxNlv7fsNDs_HUUpow-D1lVcw7cO-Gip9a9JEkhs2pUuQwNLgIHSkE2RYIChGBaJE7hqDW1GuDBESBZdJYPYtiEOu_vnhL8HK87gfbYEeY5soa8mxRJQPNgRECJsnlAfca4_I6xJsMCGCaeUfHwCNQM94h9p4pV4JKWfkBqj5Vw7Ny7KT2ceU2bAtNiRA7wh5xBkFbGThtRMGCu78x3iD7211_RI2wSFZBhYAfVtuMDkLdFE_Mm1giAm57cRXAqTeD7ZPpPInDeLzw3BrVepYQA3uhKCh1FHLbWnEN6-zdipSNjpen49LQ33rEYk35HecvcI19PMg48IEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qrd7XNNB9bftbpHJ8ZUYDtuDTMAK3-iLKBk3veFptJfbEbLlQVLUmB7paTUigYzcRy3kwXquAer-lCbQ7c5G3YygeSBUuggzMSPh58BVy-NkQNOlbNy9P7jlcNezkKfg-f4V3wwe3I8zMiLk8P4gPtstBxTGhJx7EHTNVN9ciMginJ0EMmxNssFxYM2kOiipmQUHQAlquMKFVwZ6YoOStVOUvgtCupTTZA99jIciIh4yzPV77czBuf7CLUK7UCcTo6KAZ6SJ-v5qW6CyrT2EVnC8WKq1RC1OD_pnPsTaqnjoQ7c3-kzQTWyGO14rHXCFsFpLRIXvMMrvlfruEcEFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGsoiLw5IlWg25iUZyTMHz8jjpTQBOoe8XqQtHvFyXKnukVULQsNxLXU-ABGSyoeQ2Iw7D17PgXxFYbzTkUJNp5lXiEmyBHdM7GrqIKAGx7SZZU5q0kXsAdKVKZH21zXGlxmapUdBcxQreBkEFi53bF2SOb41FZyV_8mnr6DDgJ1r92PcXlOQXOPNBLcE9lR2Yk42yXg3v-9N6JaDttUwf9pCspK5MuMcQ9O_Owvly2M2RdoiPoVswkVq6_i2xNE1MZjBS4SRy8bSgQScFyWsbOvnolZCuB6Qm7fu39WuhG7_WL3DTY0Xu2yk4LKUA4ux0QC07KSbqnvixz3dCwbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRACJDK27nND3NM_XmofSEhGiTuU7Gt6q15ccwq22482TwcH5J1JaEs1mYU918YMiErb09OnRvWS34mEZ0dH8RV-CUmBLsghWdluQzrFEB2BsuhxdpvYWkO-QNfHXcc3bi447UtvfsTcLsmvKcIbZpZS96nzY2uSYbb9zNsfFqOCQgtSVHbisDr6BjkaBA6a9yRZ3VAe_-e6eunMCZe_YqnIyBUE9GMw_11FQ-yFkqou1-H4cK_D0r4GmKd6DQVERdHqg7apAafLcdNlA0WnC81Lu1e86IW6_TuJJOvhuk99Ixo84_knNJfImBFWwyzUjAQKojIeIlGx-FHELNL8Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkdR2WYttbH_dib2MlzG87nsaX4jypLOC6ZD4KMZ2tO2IiK4hTXDHndhcd9DEVRDX-VgaHliL8OLurZrPIKXFvvv3H3PD0I2NLTAQ0Zh_FSIBWix8soW5-LCMzKzEhVa-xFuneVxnjf6bvYW7V-_jxiYde4GDNHOXm6tr8ml0VRLQccaQH1m3AMoRBOTG2X-DPlknUOJhaOnaUoELGM933IKgNz44DoEppVPefIRdwjHMzQ2MW3Cg1qheqyVhWpDHZhD8mi0QNcOG65CZZsPK-hJTDcUKq32rLsOplhO3eGlN8S3hd1DIhIm4o9HHEt6nVfsCRE0FxYdBw626TXKSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
فلامینگوهای مهاجر میهمان بهاری بوجاق گیلان
عکس:
یعقوب رخش بهار
@Farsna</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/435941" target="_blank">📅 18:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435940">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794694d83.mp4?token=MR554P3jTh2DtYCgpnnuMFOg_uTN7KzMgL1tSwXITmn6JibOYcAutclT6p1EZXHUFsfKGgWFJUdUT-Rv5cYvKEKxZoSjbiT176fGSr4-IsoYnRRhbVSiUHm_Kiycewl7a3O2j_n5msISlMS_2nh7JcNE6E2LTobemd8EHmZYYmFyRSUisEkoLpB9YXz-jxwgS9Z_y7J2bQ9Egqx_nbu_KwHBKpNB1cxtE9AHezb0GF4UD2iUUs9lh_2NxY_TO9eO1OuhHODcgQmZTTcdLyj4w2Pdhw8c80AEgzO0dTKIyfzNH5v5D2U6JRLy5gJg4KS08KLSYz3IsWUh6Iw1EruFow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794694d83.mp4?token=MR554P3jTh2DtYCgpnnuMFOg_uTN7KzMgL1tSwXITmn6JibOYcAutclT6p1EZXHUFsfKGgWFJUdUT-Rv5cYvKEKxZoSjbiT176fGSr4-IsoYnRRhbVSiUHm_Kiycewl7a3O2j_n5msISlMS_2nh7JcNE6E2LTobemd8EHmZYYmFyRSUisEkoLpB9YXz-jxwgS9Z_y7J2bQ9Egqx_nbu_KwHBKpNB1cxtE9AHezb0GF4UD2iUUs9lh_2NxY_TO9eO1OuhHODcgQmZTTcdLyj4w2Pdhw8c80AEgzO0dTKIyfzNH5v5D2U6JRLy5gJg4KS08KLSYz3IsWUh6Iw1EruFow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی حزب‌الله به یک بولدوزر رژیم صهیونیستی
@Farsna</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farsna/435940" target="_blank">📅 18:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435939">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-37.pdf</div>
  <div class="tg-doc-extra">4.8 MB</div>
</div>
<a href="https://t.me/farsna/435939" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-36.pdf</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/435939" target="_blank">📅 17:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435938">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va2922388hGoouYqbApRzFEbsy4ZySDk1YQE6pspASHnUboUZqdXf6VdzXYR5Kd0zEmqR5MDXAlBlmj8hONqkCA98RMU7Zts6M4k6ZuCQQ3HkazVYVGXNXHwmB_wdOoWZ7mDwHMjFSd41You7JzrLEPSwuDgl1f41ya5IcgHZQzOqQPpi2Mwx4MtIpAKXNe82kv-alrIYMI_c0cQnFU8QHWDJT8b2u2Juyf50PCrrG6hoeEvp1tczzKxuxMwoqDVCEPP_fpWfHf-WTjL6SAyg9Ggju6_gGkrX2K1Gm-Gbm7MKbTpxktK_RNN2dz6Avyc1S44EU0WoZ29_3wDEQuSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرگردانی ۲۰ هزار ملوان در تنگهٔ هرمز
🔹
حدود ۲۰۰۰ کشتی با ۲۰ هزار ملوان همچنان در تنگهٔ هرمز سرگردان هستند. از زمان شروع جنگ رمضان، ایران کنترل کامل این آبراه استراتژیک را در دست گرفته و قوانین جدیدی برای تردد کشتی‌ها وضع کرده است.
🔹
برخی از این ملوانان حتی وضعیت قانونی خود را از دست داده‌اند. شرکت‌های کشتیرانی پوشش بیمهٔ آنها را لغو کرده‌اند و حالا دیگر نمی‌توانند وارد هیچ بندری در جهان شوند.
🔹
جکلین اسمیت، هماهنگ‌کنندهٔ دریایی اتحادیهٔ بین‌المللی حمل‌ونقل، وضعیت ملوانان را با دوران کرونا مقایسه می‌کند. او می‌گوید: «در کرونا ملوانان ماه‌ها در کشتی‌ها گیر کرده بودند چون اجازهٔ پیاده‌شدن نداشتند. حالا دوباره همان وضعیت تکرار شده است.»
🔹
این درحالی‌ست که سازمان بنادر و دریانوردی ایران اخیرا با صدور پیامی علام کرده تمامی کشتی‌های درحال تردد در آب‌های منطقه، به‌ویژه شناورهای مستقر در آب‌های سرزمینی و لنگرگاه‌های ایران، می‌توانند در صورت نیاز از خدماتی نظیر تأمین آذوقه، سوخت، خدمات بهداشتی و پزشکی و همچنین اقلام مجاز مورد نیاز تعمیراتی بهره‌مند شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/435938" target="_blank">📅 17:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435937">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌ هدف‌قراردادن یک خودروی دیگر اسرائیل توسط حزب‌الله
🔹
حزب‌الله: یک خودروی نمیرای وابسته به ارتش دشمن اسرائیلی را در میدان شهر الطیبه هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/435937" target="_blank">📅 17:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435936">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حزب‌الله: یک خودروی نظامی ارتش صهیونی را در میدان شهر الطیبه هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farsna/435936" target="_blank">📅 17:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435929">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahp8cv6NXJo916Ywu7yVobAfzzDQbqa0RUzfECPP4TbfkX8VSz40CldadQdOcv9wOiWA2fZ0wogRoex1iZiPA6Gp5X37zrHrNC_txFjx6FO2IriySsJjFzopxN62SRJWFGkdyBpPfeC2QmjxPvVRyciO3hgAZsHqs3U0By9LOiDtDKoT-X_AO5e2y34c-5Oc1-OBTzWXxhlwABgK2Nwr6topA2PXAkUJyjB6w8sEMslpD3H95hzQcdF_-8OOVIIXm_E9bYclCl9NsEtzqrT05N2foZqSL4-ZAdY4-JmPidwtB9kOy0d8gn4Hpa_8LQ0z073IMb-eJjkmPeJtV5TKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYibfWk_xIdW5uwkcdWRq4NSpvGzQ6nIjOqMbkgm5ohbLE0pfCCtzuF86sabJ6zq20nZdq5BUHjrDME1Hquk6CNBCgghM4NDtYqPxUAvC8-TNjNxwnBchblcahB4kzEiIntSp4MtPH4KaQNTNChiHygl2MLKH9hwpDVrXig_NxOcNs0PUuTVamtbjor_f_r-MRqNKNldUmLxa0iPmZctYlyj-Jjwon8peTZJ01Q5s4-dwcSjt-z0YuViNLdG-fRL6cowB90z2q0mjIiN0w-mCNLETOyAtoDvYP6npuVg3kZyIL2S_knRcXNrF6N7EIcecv7rfY3DtAbnxF7faMRa0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gh8YNmetgxsH2d5VRy2UTQWhdNnAUivqIiBipNGNl8LPxE-2GjterFxa4cEWseuKgNNzQpE3XEfgpWlWvl0ROy7FPklAcsOShKwQm6ErTIaro5uo-Uld_9CoPWCrDIz_uqti9OLEd9AY58OC4h5eB1r70LhA-euW9nc7sosu5X8a5xEqQhsInLUFEDdjWurCNAb-LzgahJbwu0lfHoeaTxjYO3xVqII-oHPnP8w9iTeyb2CRQSH5df-SpDeinWLzJL5SV6KY4QqDv01xS9q0qnvBmzeKBNx0084vudeFSRXXi7XZZQlcygHoUiduUSAC79D5ffj5oBD1AE1DJN6mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SC4XexA960kwiNh5QeaeGtiOjoWE_5Q3uXbCP5s1bfs0RJEqgL3Mo8uZG5lLiLvPzVpvQotA6pQabk_sBWC4b4zjX8cp12cJDjR5wzedmP9003K6HPLDXpGW03lsgDG3SihUzdMyWqtw0YW4_zVj9Xw8vH8n2ZfGVNqvUsh7p0T0tFdgHG_CFwJV61-qHt5KT1Gbd2ZLlC3_N-m6STm-xEw52E0f3b8oEwVTcgDbNoPMgyHU2iW-7kNqsGUw1VF7gez9sbXo9z1eVdqtBENAPsZlXRle_xbPjYHcwyiPM6zcJ4u3Dpc3dmCvjw08HYHKEfcCxraO9C_9IKvwiLlQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmC07ykMHqXlEkrQyyGMgL77wdkA1CVbraWfDSz2r5WZlHxVSb2XcGAR_sfb4XLii6ehfCrhOeHm1SDd5LeD8B_bsLaDJ0NNevYGCPMQPoHkj-aKdLoeL_0uxulbTLp1RdavPh0Ko8lbLDt4gIbQHPt21nFnNdEQQK6LBYm3aTNseeKvQ-TrDiu2dDK06Tuv-62mhTt0-ULFyH1nSo5OoufV6E03sgcb7d766P-Qpwa5Kv4CfBnTK1Css8TV4FpJRwZooQUsB1UKvvHL21OcoGznQsCz50o4rltk_7twi4-X9AL5aaqjb_G1NwmqHW2f5ouHH7TycSFkr53d9ai_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxze38A2L8dc7Ojj4EVFolKR9eDa9Mc9YafPEO-OP5BWSaUZa7tQ1oii_BgZWUev0GYnw6e4WXMZ9oiObuQuIeBO-ar6eQTR-Oc4umqhhtbyq02OGSqrBbodj-uyz0shTWNeN-ATt_GK1d1s14b7_oxVb7NIB_qbycIwSO5Ra0Vu8rlEuW-_kBbph95HsgRp9aumyxoHpylHIrjq_nuDJ-qWm5OuoUScaVpnMNleICV8LhTTQBd8tfFehQ9FXaaWek9C_lO9-j75K_kWDvtqflJmWVmQxMIC0XHAIclgXc1VpcXbUbmQ0ENhsDUpel6ew2jWJ5gOBnBI2nVWv8GL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fh74LciT7Pxf6nqKlfHau0DrUOzwXEl0lXzuYjifeJZr4HnHodpa8aMNblaNZ0qOPZr6UC5mvZkud293HY8bRYkeYJfcj82l4pokGiCMcDeY1KLBYRM_BkKEF9jzexWt1mF4mtF4af8tIP3U_bFTkLxldHtZ-KMPJDAy_jvs8-tz_BZvoLy3dRCbnQesnrLbxvtYeuDxAUX-cj9SMvO7_LFqsDM__ceCpHniOYG15TSpMiYXNAaInDiKG9Tpt9gN9_XflMj0d-346j8ROkur_wiQMCinaGFtZVFWN48hwQEMA-n7rJYUb0floF2F90wVo9C74nNyH5jq4aAfV1GdZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اکران فیلم «نیم‌شب» روی پل طبیعت
عکس:
محمد وحدتی
@Farsna</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/farsna/435929" target="_blank">📅 17:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435928">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حزب‌الله: یک خودروی نظامی ارتش صهیونی را در میدان شهر الطیبه هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/farsna/435928" target="_blank">📅 17:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435927">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b562d32cb.mp4?token=q0CSNV8kHxcj7dXNrSOMm7N6WLFnVR6HIA86yNL8sXREK_9yvypFoHBEjhyeenRilb-HLgKAE_L2RkUkajayVvVIKmjuWm_qHH-AAI-LmcDXQIZTwTEZcI4KvQuzagglcKvzgBhsFMXNujHFvJYBQljhdWNmbkevvEtZYkqD4EmxmAqwPMS-6JUzzczfCdqYbaZDDsHSPmkVJb-mufduxzuZFy5x-ahuvlh_DA0cgC9-E_51W8ldgr_AtEqH5wckb4KxG45coN9s57JW2CcOTN3jeuKPzqgnjlBslVqE6GVh-6sErz2KTd-Dkucp_CPSbnlUtIdV7mHiBuj0TLwFc68OMGdjJz1YWv6lM_6GDxZG-uI-K17_c9_mtYTQ4QH1kfJ63EULoGnYWGZywyK9i9bjBwDe-8N2VJTf4FGSUZNkG8Qs74yvNQnE40sxFrAvIeOQE-3CHRVtDWnpmREVMF0icRlPrHLVP-4HWcF55SVkOz3viNAi8D3B9aCdt5IAjocNi-IP8p18VKWXfPm2lqwnXKzm5SANrkihjWEB1SH7CaEkWH9hUTKN3fZiz9s7fdnoxl8-JdmQkQk4LSUyjrTWRsL7bHsDjrrN3fvDi-YDT9SkiRKPxdczEFxcpNZLA4sl_qhJhj-mgRiJADIiCAYDhnAc-J2o2rFSZpRwBgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b562d32cb.mp4?token=q0CSNV8kHxcj7dXNrSOMm7N6WLFnVR6HIA86yNL8sXREK_9yvypFoHBEjhyeenRilb-HLgKAE_L2RkUkajayVvVIKmjuWm_qHH-AAI-LmcDXQIZTwTEZcI4KvQuzagglcKvzgBhsFMXNujHFvJYBQljhdWNmbkevvEtZYkqD4EmxmAqwPMS-6JUzzczfCdqYbaZDDsHSPmkVJb-mufduxzuZFy5x-ahuvlh_DA0cgC9-E_51W8ldgr_AtEqH5wckb4KxG45coN9s57JW2CcOTN3jeuKPzqgnjlBslVqE6GVh-6sErz2KTd-Dkucp_CPSbnlUtIdV7mHiBuj0TLwFc68OMGdjJz1YWv6lM_6GDxZG-uI-K17_c9_mtYTQ4QH1kfJ63EULoGnYWGZywyK9i9bjBwDe-8N2VJTf4FGSUZNkG8Qs74yvNQnE40sxFrAvIeOQE-3CHRVtDWnpmREVMF0icRlPrHLVP-4HWcF55SVkOz3viNAi8D3B9aCdt5IAjocNi-IP8p18VKWXfPm2lqwnXKzm5SANrkihjWEB1SH7CaEkWH9hUTKN3fZiz9s7fdnoxl8-JdmQkQk4LSUyjrTWRsL7bHsDjrrN3fvDi-YDT9SkiRKPxdczEFxcpNZLA4sl_qhJhj-mgRiJADIiCAYDhnAc-J2o2rFSZpRwBgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاد دانشگاه آمریکایی: دولت ترامپ، کوچک‌‎ترین درکی از تحولات جهان ندارد
🔹
کاتسیافیکاس: باز کردن تنگه هرمز برای آمریکا غیرممکن است؛ درخواست آمریکا از چین برای اعمال فشار بر ایران نشانه‌ای از درماندگی و ناآگاهی از تحولات جهان و فقدان هرگونه راهبرد مشخص در دولت ترامپ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/435927" target="_blank">📅 17:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435920">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1MLmsfUJielzYvJ3gRZk4iqBMyW_1BQxf2LUAOXoJfbJbJKO42SwrOtMm2R-4sx59WJh0Bs1I1e96aaDEEd9zK9iqW1Wc7lO8jRfkpgDeh2xCen-t4fJMfy9defHBhhBgPT6jg-P7aRrBNMkKU0bCGCgJwqzXs3pMHUiT_c-h9EbbMy2nZpGcBWEbcVu2fZO31QjF5GOcaIThMMNBmUosPAyWnKLFljy9wX26YCm87t2kI55-5fRWISzMKWsMAgCbIh0qJvZ2077KzDMAKac29UTgO6bM25JP6SfrTegZiTtM3vJGoU_RO5XAslIPT55Kh8Xma-RQrMYNBPP_qjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IGeaQFdHBtouF6yElUEhEGxU0FV5p6t57wHhdaFhW_5FJek9uB96xl-SGTct7sV2xqPoaZSt9OiUkqq6pEb6SVtc7w5kr6eV1IzfXJu5sS1DYAktslXlv5LkTIGaKkJS9xOI3kTZcPFWtN_RefTH6YMQdXLcDvE3qoFxquraEQjqheEUvg2lzcw4_zUIzuxQ1_RBLJgb0w76gThmwmPcAOFrtjScxoKgaz7Zq7CwrdS_BxyB_vqRzTqcGS1uQDl9cRtSSUXNHn3Abu1EHpVjxGXPcNx9sAxy2BRWkKoKGZDNZJ9Wh40nXFBboFhtkqvCZl5eBLSfsAA9qW2IZXWYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4PW2ZXlOGmscMbXuKC0TEtdEq-fCM5H378K48AZfSHs-O7YA_vS7vSHOIY28xEo-_-DQOIlUo7E1h1pP4aCYLoIVV3AibnKhxY7zR1CZvuPkc5q1WjKylNzAQ2qo3D_xL0U4F1bRyJxhibA9fXFfhLKAb2WKmG4wpddZI4MZlUjOzZQ-29voO-IJtdTCELtKPSKcAN4j7Lp8OQRFxJFazrs4i7zuFZv4Q4qSiPoyWaOgQPz70OEC1eMjvyC66pfSGWNRsTxspZerYKEZKNF-ymSMbOGeNPr22Anrst2lTTfhQ8abgE3alAE85YuViejx0sVhXIsQxhMx8DhKEEhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSoDtG8MULu-wKCeoTuKnAlPU8sBR3Ria5gAiuwlmJaWGd6O5fMj5o8w_nRYqjQWwvpUZdCNv-m80G257AKIhfvQRlIBS4n2hLZNAAg1gFySIs7gJFJnT-Lf0BxHvRcTwe4aNSNbQ8xCz_6St3_L6htg1xqO0_tGrbU0wLn6P0XMpPj6FIswHeBkDtnrNpOTPkXi1QUiJo2H33b0FnGXaahy7gnvnVm0FZfv8y0tJJ2-fT_6N_HypS6ivONzhKQ1m4W83BmR_mhveUvu_dyayXz9xXIwSH_smDSIW1cEnG8nXCbnO0E1SA56ml1yxvsg17cDbWO9XnUImYkArs8iHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e83XnV0Uwd9kyS7cTyhSdcwqdbJoIRRNWC95wbAqSTfoewpgJsyKmjNNvX-nChZvxXvANcx1OPym23YH20_UO38esaOTI-kqQWIs4SeGRUxuleot1p7HhGBqJgogm4Uf8c5G8-V8cmwyn4PJMN-30dnCVdY0woHj-OICrKQT73dT0iMuUfTPiuwCoGdpS8fHxrSSMpmQwUCbrj-Dap_-KgS8j1PLwfzzwS4x71v2tarYTvyfjB93X_iYlp6ChW0Qc9W67z78kbgC7TejYvw3h4-thebl8D2X1sJorDdsGYs3MPtt2Y54D3rf2GjiZq6E62Uyx1raxKN3Sdx4DVK05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JaIY-2m6Q0brlfNRYJx9YUXK396Hawk1IQYnwjX4odv11Oak_AT-hnE4JpPGyMlXxLdevGyBe4iuvrRqcp4TQVOEZXznWNrkkfusoi9VmFeO9HS2qSzp9_v3PK1ItzMp6L25jngKzQ6SH6dyi1I56YFVeLVz64euV-VaaGhtPswCjdY3Nqkdpl6dNshBtIzbBi0ZjRfRN_Qrnf7PkfrVega7WlCXAQB9apy99OEn97lCoohfGzBW0rVk3n5BxJQ3Y7Pj_oKyD1OUCKbyf48j7LrsJJedskFhIy7LPdMRCIrXZpop20I1OC3CqbyPyAc1CF9UMSRYEFBEDwnZsFis_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuLMNE-wTKexAwpQ_dgGPod4WqjrI3xMSB8kLy735skYp0_kA7TPUQlSJVunkssQvF22EfW82uOsUiP7pASxdVfNFrwiLaOUh3TRe9pvcnQ7Ug3mORXyzdJ5b41-99sFXnP-x3RLpXMg3bSgfNyvovrs4oVIwaOaxss3HAZ6j3OfxaCSDKYo9wf6X8_LU0fJarQ_FkB10JZNkoSsJe5dEVztr76-97ghuSkMXi25s4c8CKNZCDnvJdaZxfB6fU3JTBbffSVXDekEKTSPfOabCap3qZUTpDqNtoVcbOXnPS4A73zOt8FMQJd8TeqMFSz79hRm1J301qpEybP2pkTnjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست گرامیداشت دومین سالگرد شهادت آیت‌الله رئیسی
🔹
نشست گرامیداشت دومین سالگرد شهادت آیت‌الله سید‌ابراهیم رئیسی و همراهانشان با حضور وزرای دولت سیزدهم امروز در خبرگزاری فارس برگزار شد.
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/435920" target="_blank">📅 17:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435919">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwNbqLOXOPX16QkO2eRgrA-KBxKyNChCRx1uELhNlH-FhO-lBDNgC3uriK-fqytr21IsF18tz3gKbo-6i9W_nzox7_cYhQWxk_Q2Pi7imsEgVm2qsUP47rryDxcNIunGjfnDbrgo75GxFAYJX8_IF1NOgxIteVoh9DWK1-sKaWuVq_NFvxlqJvL_UOzt74onU0ajA2QutmQOQQ-Cg4KuWVTiqX8sTjk4Z7BQ-U7imRqitUpL8_QfCtTbR5-dDlKDkmm_hd8nF3TKSDUZ6DjIz0Cq5bCzypJMvpqLmu8CyFLhohcQW5E6bZPwemPMVP_PVNuMCqpz4lbNg16LG28xqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار لوازم خانگی در شوک گرانی‌های پی‌درپی
🔹
بازار لوازم خانگی در ماه‌های اخیر با موج تازه‌ای از افزایش قیمت‌ها مواجه شده است؛ به‌طوری‌که قیمت برخی کالاها در فاصله چند ماه تا ۲ برابر افزایش یافته و فعالان بازار از بلاتکلیفی قیمت‌ها و سردرگمی خریداران خبر می‌دهند.
🔹
بر اساس مشاهدات میدانی خبرنگار فارس، قیمت جاروبرقی که زمستان سال گذشته بین ۱۲ تا ۲۰ میلیون تومان بود، اکنون به حدود ۳۵ تا ۴۰ میلیون تومان رسیده است.
🔹
قیمت ماشین لباسشویی در بازار حدود ۸۰ تا ۹۰ میلیون تومان اعلام می‌شود؛ در حالی که همین کالا در اسفند ماه سال گذشته بین ۳۰ تا ۴۰ میلیون تومان قیمت داشت.
🔹
فروشندگان بازار لوازم خانگی از شرایط فعلی بازار به شدت گلایه دارند و می‌گویند نه خریداران و نه فروشندگان چشم‌انداز روشنی از قیمت‌ها ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/435919" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435918">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جادهٔ چالوس مسدود شد
🔹
پلیس‌راه البرز: جادهٔ چالوس حدفاصل کرج - شهرستانک و محدوده خوزنکلا و پلیس‌راه کرج، از کیلومتر ۱۸ تا ۳۰ به‌دلیل اجرای عملیات تور سنگ مسدود خواهد شد.
🔹
این محدودیت ترافیکی در روزهای یکشنبه، دوشنبه، سه‌شنبه و چهارشنبه از ساعت ۰۹:۰۰ تا ۱۴:۰۰ اعمال می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/435918" target="_blank">📅 17:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435917">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b03e5807c.mp4?token=Y1mDtjVK3WW_j-tLyGTyi-0zGiPofeumil0UBx5nf4am8IK08s4OzgUsgj_MLyQoWMxXgjoRRXd7eeldqsyisqfoc4pdmfqufU-P0X230QBNA7D3xduz3YLvX8Z_7ZmexMdf7zYjOwKbmPbpLVUyk4TL0tsM2ex5d_Tg3-YtHVJkiqIDTGI4pSANIKXLYgoLlbQHUMcmsL9AaW-mrmRldrL6ZOMIn3c7_TOQmCjjvXc0N5mmhhw9SohG5AHmibau92ba_0tUTHOkN2x0lqtPfClpg6rz2i6X3iD8gO-yvpxqlCdXQzGqkmf67l-vsN_JJew4ueofvO4gZ4NE54LUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b03e5807c.mp4?token=Y1mDtjVK3WW_j-tLyGTyi-0zGiPofeumil0UBx5nf4am8IK08s4OzgUsgj_MLyQoWMxXgjoRRXd7eeldqsyisqfoc4pdmfqufU-P0X230QBNA7D3xduz3YLvX8Z_7ZmexMdf7zYjOwKbmPbpLVUyk4TL0tsM2ex5d_Tg3-YtHVJkiqIDTGI4pSANIKXLYgoLlbQHUMcmsL9AaW-mrmRldrL6ZOMIn3c7_TOQmCjjvXc0N5mmhhw9SohG5AHmibau92ba_0tUTHOkN2x0lqtPfClpg6rz2i6X3iD8gO-yvpxqlCdXQzGqkmf67l-vsN_JJew4ueofvO4gZ4NE54LUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشور پاکستان با استقبال همتای ایرانی وارد تهران شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/farsna/435917" target="_blank">📅 16:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435916">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4224963680.mp4?token=TOHo-VnhMyvluR6DNAK3e5sDBzKdEJwo-y87ybS1bgssLA7TB6h1b97zLwkwvrDCSyzK_0SqbBk3hChmlj1iBg_hBr09Lv3kBpxFwxp2GCGJRiiGyy_pu5pzs1NiQdGinOtY6EmeEb-pHEKJkeQ-zRXzEXYHTOR3KYKRGqvQ3KsZJPGwRVBfKlD8Mk72y1BJ5yvNGGJeHDqHeusPfNcU-THtlEO2n1m-YWeEhgdeiYXW7pV63kqIWYwC2AfNYO_xzUnurUXdZxpR7emb1LzlIKAJRl_kbilCG7B79lMElDlyFKBIyqWsqNJNrj5zfoW59PzBNMhlMxXbiNvsgy2QVEpzvwmn-xicS1_4uGmCLRfAgcSBtRP67mO3xQ2NWwEioxdsI2hpV5FWYIg3SE7ZMb-G8osiLOVLkBcgRxAXBgweniRExjdX2vFouZKmlVDLuqNRRK_WjIIzuPxSk2svoF3Lac55as_kjlT3wGBHD1ftF7aew1BGp9TyfmXkVut2cCHqa5ZLCNg6KOa-MR_Y_gFyohqIgeTZPGMYC9dSS8dDJvaN6kr5Hxaqz-tlMLwj3iZwUmV20FgHza-_IwG44PFRp51V2-2BzjlDhXN6y1yEPSx6xRnWlH2835CUhKQ2UynMIu6tgTyr82SkAr268rIcRZv36xGOzI4yc6SbLQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4224963680.mp4?token=TOHo-VnhMyvluR6DNAK3e5sDBzKdEJwo-y87ybS1bgssLA7TB6h1b97zLwkwvrDCSyzK_0SqbBk3hChmlj1iBg_hBr09Lv3kBpxFwxp2GCGJRiiGyy_pu5pzs1NiQdGinOtY6EmeEb-pHEKJkeQ-zRXzEXYHTOR3KYKRGqvQ3KsZJPGwRVBfKlD8Mk72y1BJ5yvNGGJeHDqHeusPfNcU-THtlEO2n1m-YWeEhgdeiYXW7pV63kqIWYwC2AfNYO_xzUnurUXdZxpR7emb1LzlIKAJRl_kbilCG7B79lMElDlyFKBIyqWsqNJNrj5zfoW59PzBNMhlMxXbiNvsgy2QVEpzvwmn-xicS1_4uGmCLRfAgcSBtRP67mO3xQ2NWwEioxdsI2hpV5FWYIg3SE7ZMb-G8osiLOVLkBcgRxAXBgweniRExjdX2vFouZKmlVDLuqNRRK_WjIIzuPxSk2svoF3Lac55as_kjlT3wGBHD1ftF7aew1BGp9TyfmXkVut2cCHqa5ZLCNg6KOa-MR_Y_gFyohqIgeTZPGMYC9dSS8dDJvaN6kr5Hxaqz-tlMLwj3iZwUmV20FgHza-_IwG44PFRp51V2-2BzjlDhXN6y1yEPSx6xRnWlH2835CUhKQ2UynMIu6tgTyr82SkAr268rIcRZv36xGOzI4yc6SbLQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه‌پرداز مطرح آمریکایی: واشنگتن در ایران کیش و مات شده
🔹
«شکستِ» راهبردهای آمریکا در جنگ، حتی تحلیلگر برجسته آمریکایی رابرت کِیگن را هم به اعتراف واداشته است. او که از جمله حامیان سرسخت سلطه آمریکا بر جهان بوده، اکنون معتقد است که ایالات متحده در ایران…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/435916" target="_blank">📅 16:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435915">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd7fb76eb.mp4?token=pTbyHcGPD_u_bKv-Oga0athb41h5nGAwHzhnlekYgGdZxb-6__cEvesmX1HHppZrc8IpESE0gspG2hW9GVktAqUeQD_hro1PcFDVhhyQW5ZNLVQAAqR5hn02MYwpf7U3SK6gBN79TYZd2qcnOtm20LCut7gxvvAKm6EIdJR9ftZ-YS_GmznR_PDEI1JmaVYNrc_VViW-qigjWvlk8zgDF44DuFoT8USDUdSiJ6Y1_9WWT8f0v16b29XCss79VT0duOq-5SAEukKpwfL3hJ2nsV0BKXuCkJGzKlA-JVU6wkdxux7xx0iKRjL5G4Ss70squREHzfBhADfc4ohqwpPIe2qbgp_iy7jXJQQeJB25tAWCpS8ZlMiR2fF9d9dgpSiHrzOYBhKA4cFnp0i7YupWJ_9xUA11DmSU3BFIOOCYyKRxJLr8-NAB-vMoUHa_BYkDdArcfUsDH_94hdjvFCOcmeHsIsZdlFcU6N66RORCySCYHaLVeGqKTE65czm9C0OtXBujGJKkZP1MtWvD-1-MLCLUG44okLUW4kQMx5EHTvKX2YTNCfTic_RF5WrCqbjffHWJrnKVuoOaCwvzKxOeG0MGPYlVZ2ropYXK8PZYgAPAqxp1GmsMQL58ddo8cmEo10psZsAz9O2hBXb2hTul_-qui5mA7yTeEGgW4bDnH8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd7fb76eb.mp4?token=pTbyHcGPD_u_bKv-Oga0athb41h5nGAwHzhnlekYgGdZxb-6__cEvesmX1HHppZrc8IpESE0gspG2hW9GVktAqUeQD_hro1PcFDVhhyQW5ZNLVQAAqR5hn02MYwpf7U3SK6gBN79TYZd2qcnOtm20LCut7gxvvAKm6EIdJR9ftZ-YS_GmznR_PDEI1JmaVYNrc_VViW-qigjWvlk8zgDF44DuFoT8USDUdSiJ6Y1_9WWT8f0v16b29XCss79VT0duOq-5SAEukKpwfL3hJ2nsV0BKXuCkJGzKlA-JVU6wkdxux7xx0iKRjL5G4Ss70squREHzfBhADfc4ohqwpPIe2qbgp_iy7jXJQQeJB25tAWCpS8ZlMiR2fF9d9dgpSiHrzOYBhKA4cFnp0i7YupWJ_9xUA11DmSU3BFIOOCYyKRxJLr8-NAB-vMoUHa_BYkDdArcfUsDH_94hdjvFCOcmeHsIsZdlFcU6N66RORCySCYHaLVeGqKTE65czm9C0OtXBujGJKkZP1MtWvD-1-MLCLUG44okLUW4kQMx5EHTvKX2YTNCfTic_RF5WrCqbjffHWJrnKVuoOaCwvzKxOeG0MGPYlVZ2ropYXK8PZYgAPAqxp1GmsMQL58ddo8cmEo10psZsAz9O2hBXb2hTul_-qui5mA7yTeEGgW4bDnH8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکاری یک اسرائیلی با ایران، بدون دستمزد و به‌دلیل نفرت از اسرائیل
🔹
پروندۀ یک فرد ساکن فلسطین اشغالی که بدون دریافت دستمزد و بر اساس نفرت از اسرائیل با مأموران ایرانی همکاری کرده مورد توجه رسانه‌ها قرار گرفته است.
🔹
«احمد دعاس»، رانندۀ کامیون ۲۷ ساله  متهم…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/435915" target="_blank">📅 16:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435914">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انسداد مسیر جنوب به شمال کندوان
🔹
پلیس‌راه مازندران: از ساعت ۱۶ امروز مسیر جنوب به شمال کندوان مسدود شده است؛ حدود ساعت ۱۸ از پل‌زنگوله تردد به سمت شمال نیز ممنوع خواهد شد.
🔹
همچنین از ساعت ۱۹ مسیر شمال به جنوب مرزن‌آباد به سمت البرز و تهران یک‌طرفه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farsna/435914" target="_blank">📅 16:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435912">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jScuAbZ7mAUDRUNtAl-ZdUt7-2_QaccBkYnCNO5vkNehbGyzISaH2uUcyJaQ_VStyWzF4QGj5dfEZrdmMFaoqy5LJVQdjO8563Abf3Yfq_LvVh-Q_eJceWd5UEeH6aK67nAVsla_-j47jGagj7sHifJY8Fhlc7LSt5XHokjl6LQ_bMWd_8UdSNjNCK8RI4GXPEwawB6j69UeHU1qfcq_EGrQGJJ7dB9u8RaM2Df79Is3HUAAkU0dgz2ygBVNUHjVpC4naD3qnmpDmeuTRL5ccGt-o0xXuPHBt8hXVt_JypjyVWK1CeX1lKJ3CKzVxqDzuHJD29rYTFQ2BGFPYyNvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زوج‌های جوان در سال جدید نیز از بانک‌ها روی خوش ندیدند
🔹
از صف وام ازدواج سال گذشته حدود ۵۴۰ هزار نفر وام خود را نگرفته و به امسال منتقل شده‌اند.
🔹
با این حال پیگیری‌ها نشان می‌دهد بانک‌ها تاکنون به‌صورت جدی پرداخت وام ازدواج را شروع نکرده‌اند.
🔹
پیگیری خبرنگار فارس از چندین بانک نشان می‌دهد که اغلب بانک‌ها با وجود گذشت ۲ ماه از سال یا پرداخت وام ازدواج را شروع نکرده‌اند، یا اگر شروع کرده‌اند بسیار کند این وام را پرداخت می‌کنند.
🔹
یکی از بانک‌ها در پاسخ خبرنگار فارس در مورد تعداد افراد در صف می‌گوید: «سیستم ما آمار در صف را نشان نمی‌دهد فقط بانک مرکزی می‌تواند آمار را ببیند.»
🔹
در صورتی که پرداخت وام ازدواج به همین روال پیش برود نه تنها افراد در صف موفق به دریافت وام نمی‌شوند، بلکه تعداد بیشتری به سال بعد منتقل خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/435912" target="_blank">📅 16:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435911">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84537cc3f5.mp4?token=p9-LJj1kTojVvBeCrXKsUL84F2s1fTuGVdhcfMDmYcs_piSn3TQEELJnBRWFEatLrNJe4rSLck5KBWr8yyWwZh2HrRA_2KzNs44q3E4MwpL52hB_RsZH3UxSVYsipI0XDjz5RLovo-OKhNYA8iN3E6CH_Px3j81RKueY1cFaCHzmXE6grk7Nyd_BYsu4tVoDD9SAwUnICdPUeqaNBnSQYvIzvCS1hgy-hxHAUxoXAtERFaPubXlG2DxhRVjtD9_7xQw9ETWfhkSFT0yLbHkRmWpoXUmdorZ7XoSBMm_v-jqXsqErIlMeRV9PtOxLrJqO1eOeBAG8rIyQ_W6M9c8QOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84537cc3f5.mp4?token=p9-LJj1kTojVvBeCrXKsUL84F2s1fTuGVdhcfMDmYcs_piSn3TQEELJnBRWFEatLrNJe4rSLck5KBWr8yyWwZh2HrRA_2KzNs44q3E4MwpL52hB_RsZH3UxSVYsipI0XDjz5RLovo-OKhNYA8iN3E6CH_Px3j81RKueY1cFaCHzmXE6grk7Nyd_BYsu4tVoDD9SAwUnICdPUeqaNBnSQYvIzvCS1hgy-hxHAUxoXAtERFaPubXlG2DxhRVjtD9_7xQw9ETWfhkSFT0yLbHkRmWpoXUmdorZ7XoSBMm_v-jqXsqErIlMeRV9PtOxLrJqO1eOeBAG8rIyQ_W6M9c8QOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز نمایشگاه مجازی کتاب از ساعت ۱۰ صبح
🔹
نمایشگاه مجازی کتاب تهران امروز از ساعت ۱۰ صبح در سامانهٔ book.icfi.ir آغازبه‌کار می‌کند.
🔹
نمایشگاه به مدت یک هفته برقرار است و کتاب‌ها در این دوره با ۲۵٪ تخفیف و ارسال رایگان فروخته خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/435911" target="_blank">📅 16:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435910">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دلیل امارات برای خروج از اوپک
🔹
وزیر انرژی امارات، در شبکهٔ ایکس نوشت که خروج از اوپک یک انتخاب حاکمیتی و راهبردی بر اساس چشم‌انداز اقتصادی بلندمدت و تعهد به امنیت انرژی جهانی است. این تصمیم تحت تأثیر ملاحظات سیاسی نیست و هیچ اختلافی با شرکا را منعکس نمی‌کند.
🔹
امارات قصد دارد تولید نفت خود را به ۵ میلیون بشکه در روز برساند. خط لوله‌ای که میادین نفتی ابوظبی را به بندر فجیره در دریای عمان متصل می‌کند.
🔹
حتی با خط لوله جدید در ۲۰۲۷، بخش زیادی از نفت امارات ناگزیر از تنگهٔ هرمز تحت کنترل ایران عبور می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/435910" target="_blank">📅 16:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435909">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6643075c39.mp4?token=tmQQSTpOn1OjQHh4vYHQailIgTrMgfx-hvyiZnI-ZKw0DY9593CSo4J4enZeHkpvh5CKHc_6L55gSBITXbhMgwY-Y6wyt6sorWnzTMR_rVGUvqIbCvhB_Mcutz54OxAhKa32fMMbbPmyfHY5YgEMAjwYtFIAp_tM6te0-1KW3wisslDMGgttFZIQSfEaljqyWfvpbYDYyYXZ2ro4ERDcP3BhkIh2JgvCPyOkbdlp6gxT9Ox2cSWW6aRb9xZZ2dwA6hWeQXtK4Gw_KVQvb-MVJm9s4zg1q2Nw0XbYyVXY_Y44C0vS1L8Miumu-DlWNEFoi40wsMdCZPrlfqc9_ltIdIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6643075c39.mp4?token=tmQQSTpOn1OjQHh4vYHQailIgTrMgfx-hvyiZnI-ZKw0DY9593CSo4J4enZeHkpvh5CKHc_6L55gSBITXbhMgwY-Y6wyt6sorWnzTMR_rVGUvqIbCvhB_Mcutz54OxAhKa32fMMbbPmyfHY5YgEMAjwYtFIAp_tM6te0-1KW3wisslDMGgttFZIQSfEaljqyWfvpbYDYyYXZ2ro4ERDcP3BhkIh2JgvCPyOkbdlp6gxT9Ox2cSWW6aRb9xZZ2dwA6hWeQXtK4Gw_KVQvb-MVJm9s4zg1q2Nw0XbYyVXY_Y44C0vS1L8Miumu-DlWNEFoi40wsMdCZPrlfqc9_ltIdIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پانتا، رئیس اسبق سیا: انسداد تنگهٔ هرمز اهرم فشار فوق‌العادهٔ ایران علیه آمریکا است
🔹
شگفت‌زده شدم که ترامپ از انسداد تنگهٔ هرمز توسط ایران غافلگیر شده؛ در زمان تصدی وزارت دفاع، از وقوع قطعی این اتفاق آگاه بودیم.
🔹
به‌دلیل انسداد تنگهٔ هرمز، ایالات متحده درحال تحمل پیامدهایی سنگین است و اقتصاد ما آسیب جدی دیده است.
🔹
باید اذعان کرد که ایران با انسداد تنگهٔ هرمز، اهرم فشار فوق‌العاده‌ای در اختیار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/435909" target="_blank">📅 15:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435902">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GClt5GQlCl33_JngVQkWE4uOPuNLCvVSYzvDEXzNYIVMZ-Tn_k6XEs68CN0-KuXl8xgFhH95i1zLHexcR8G6mKjjrZoulrEnbnPamBsDl_zHiXQkpKjGyfpr78CXIgITo1YvxG9kgSaBOEoOL6NpNN_LEKfxTGFrAuxKZFdnF_0U8MPIeJIARU-7d26cemRRREn-d5goRQqt-baxGkP32Eyo173oMUg_aMDre3PEupTO1bZoRbHAB2snOfA9Ly3wFqbKDt1Iv16REihRp-IUvZK6Cn7h8x8rj_8iwZ3iXNRNSPuBcqGJvBqeNBxmkFGKU0VGCtc-oQZm2zPykjUkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTY3LeGjKZPdeo53iigiO4h-od-MpZA3FILUyBWFD0UitavLfvIQW7hXqEVPiNQIxh-xiS3U7DFF4azQFaEybuGSAEgHE7MizBGsPoM_lKDOkvkaKUyP1rHsgIFnsgD_6yNzPAJMcFViU8Wss0HSHuTtf14vM6hdp4h8zk4uRoWBORNAPeF6ShOg5e5EkvQpYJoKgxCZxHccRqn2woKwbtVpX77fPPcYGvZca2u_5Xp5be1Xw1SYgjoEMfmaYbyEUhLEvtNR-k7GrGfEiqdd_ApIBsPqSuOS-G_HtzF80Fx75h-QsxzOEVUVxJemxHBIH4IOjEa23aEkODT8P29-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYbj9bLSbB_dv3C8WM0E5Hh5cUY8mdDlNe1paSMtmtqTerZzEKekfTjYjwkLJJzYMggKnokdSFY49zJGDD5MxMYhaPR3z8Xhom-NmLPRabst4mc2oWoq1dciejTvGDzHMsW7jJLHAruEKxh6WuEKG2w6M-XLqWziQkyvbzLVwuXDIaDUszl06UdOW5b-iUL3SI2uYK4iA1BqrC7NQ7FMAVAO52e8G3yeq3TolYQFq_PfNIy5-0EDoaL9LnzYBfoXLbwwJfIs6doGHQntkSHoT4cCprcz63viWPvEaH57Pbi3YmiTwcY9_Ic6c7oY6F6ooji7q-G1ZL6kCWWJRTVaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-QO0HP_vA6aDulpTUm6FWtO4R4mFoWIbBTeoWOoFy8ilTVLiJZ_MuZDFW1O7n1LSQWEnIMxsdgkBQoOPJeLiHiXtN1wsdqQ-o64JVnNCkXDlmD2M01vnYkdJh2rfbw0sU1IrhKCghncKeQMwdGLsI70hlzgpo9NNIJqDSiWlca28jimI1gqWrjZ56xQLnzFeI27BJNWpKvlXOZ7BwVB1aL6d8J94aAOTO9QCNNs5nJEAmWWyZ5_D0u46nIzhNU2Pjrc7CeuXEiEKCwI3_z_jdSIM3OpGSk7aCZC5JFzyQ3EClPH7r7uvRdj14D2-x3oSkRuGPDPsQcS_583OtMsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuZZsWh1kUZjQKf-NLiC2Z8qEV6-XVWo1dt4lpgcLL-pxMArlEOkvSx53vVJIrjTeK_8NtkiRYpFCpburKorPqdLS_vNTTG0yDK8367EGuUQZJjE8eyKoaDNXALGUI_KekgoNjYrd7986gIjZG-MbvQKt4qdqVqwNjT9VBONMREaAC1XMcqN26JMvSkfJrVpDcP5DtGEUk_plPCdv_Q6gGJWAEMFg5OgXllDhCT3OdmgCWTO6eBQnUq8dwKnb3UpolBt9Mcdh9Vnp6IgYWSwEKBu8dXDcF-CK9Q5mNVYkdvCOWw7MuRmBzEh5JZG8YCknzMNJnIbH0qAGc2NXIfmcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdXCFrLVhmCdQoayspH_6BrWvdlaWBCT7rHhcPewmS-wVmNaI5k_lov62QZ9sKWrEh2ACzNFlKVnTAEbDK-0bIBs-JCk11gF4eWJM5Q59Em6OFnrggU1jnIvmEXs-Z5B7sjorzeJZ0ZQg5JPu-suU9_FQnqlFoW4dL0oBnm1woCNKkS6ScWMsVPM-2VZHi8iV8IaNPlnydy_t2mWHLPTRmLoOyDKMFR71pLINy7Rleo73D08x18IX8_ncMxZSBa9WmvcNq6vRUPLlSA7eAT1-aTZKiHj07wpCRLGPZ0J-o7tU6K6re8gkP8y-PzbA90C_a-CDmvISDdZXO3mvLCMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNbYKHx6OlSit-GDpAXCTcKUJU9lrRunjjKfCsi4xlpiocSlziTgdTpfA8p02geYfazZJUBxdYOioyUTGZ-QHinjCrSDiRyJRuAv8eZOv6GqB1paRIi3tESF7ODrYfE6C7oAD82NjiMJkM-_pyLqrhEMme17jqtF3Ys-LHeJSNxEHAqrySX8ULeVCnpTiil_zdHOg75H_sQaov8S1ETjyWMDO2dU_aLOXiGieuD8Qqg4TeLj8A7QdDODsVHDkcdR6zJiZrrykFuh-u0clC0Fbfq2BPxoGAKUzaAZi8C6y-fXZDeGHhv4f3FNlMawhOeNSN_P7gDS5xqKhQESBIZ0pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
صید ماهی صُبور در سد سلولی صنگور خوزستان
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/435902" target="_blank">📅 15:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435899">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796c415e0e.mp4?token=uuYvtUmkR1VtUuXBKut_IRKryta1GpovezMS-ZAb_Ao-2rI2-FbRl2vH5y6U3_5YG3rWmoHm2zT6hCEFflupGoDcaUjVj1RM4VzcO6GUWHjdNphACzhUnxxPHg6KnMjou3Gw98jXhTUDGe3LgkhBukmlKzFwMkkn_ky8Os2vDVvxW7kf1rbu0aCGvpLV89OT9gHEp6RdEbU5HM8NDBHsB40U1uzwr44Kz9kVxASjCEHRqbj4Ol_UP6RxB35ZjxNkkfzsbQcyW85QYJYXzhFDThwnr4itXs4kRX-keNaHVdhcN5PptD96MwYr9hU1KRK2iMZNWC9JhIfb2mXJ56smRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796c415e0e.mp4?token=uuYvtUmkR1VtUuXBKut_IRKryta1GpovezMS-ZAb_Ao-2rI2-FbRl2vH5y6U3_5YG3rWmoHm2zT6hCEFflupGoDcaUjVj1RM4VzcO6GUWHjdNphACzhUnxxPHg6KnMjou3Gw98jXhTUDGe3LgkhBukmlKzFwMkkn_ky8Os2vDVvxW7kf1rbu0aCGvpLV89OT9gHEp6RdEbU5HM8NDBHsB40U1uzwr44Kz9kVxASjCEHRqbj4Ol_UP6RxB35ZjxNkkfzsbQcyW85QYJYXzhFDThwnr4itXs4kRX-keNaHVdhcN5PptD96MwYr9hU1KRK2iMZNWC9JhIfb2mXJ56smRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: فرمانده عزالدین قسام را ترور کردیم
🔹
نتانیاهو و کاتس، وزیر جنگ رژیم صهیونیستی مدعی ترور «عزالدین حداد» فرمانده گردان‌‌های عزالدین قسام (شاخه نظامی حماس) در غزه شدند.
🔹
رسانه‌های اسرائیلی مدعی شده‌اند که عزالدین حداد در بمباران آپارتمانی در محله الرمال…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/435899" target="_blank">📅 15:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435891">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17c3c0505.mp4?token=Wk_K3c9ruJz1tY6I7wV5euVcgpUvO2a95UlRMAXh8iieh08QMRK4XERRGkz9t-xYdi0dzOOwIFwTOcOBqafMF5GFcIfw8YjtOg8AJ8ah2Fw3WTddl6gNitek2ohLDCQQd0EDGqYxkAnVCfItbxLsNeszB62zP92aYMeyaYdBNgbOlKBnxFHupmED1ZUmFC1Devlbo-1lSbNTZ6_r0HtlrY2d0QteQsL5cTPBo0AnD6kzE9FugTtJpPbZRhpL8OQx5IcVOcn441unRRBEwvBDDcAMervdjtEh97C8pIniY34D9bDGjt85FyRQzcNTDEIeqEyssfeDOKV4FCVd8KVAcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17c3c0505.mp4?token=Wk_K3c9ruJz1tY6I7wV5euVcgpUvO2a95UlRMAXh8iieh08QMRK4XERRGkz9t-xYdi0dzOOwIFwTOcOBqafMF5GFcIfw8YjtOg8AJ8ah2Fw3WTddl6gNitek2ohLDCQQd0EDGqYxkAnVCfItbxLsNeszB62zP92aYMeyaYdBNgbOlKBnxFHupmED1ZUmFC1Devlbo-1lSbNTZ6_r0HtlrY2d0QteQsL5cTPBo0AnD6kzE9FugTtJpPbZRhpL8OQx5IcVOcn441unRRBEwvBDDcAMervdjtEh97C8pIniY34D9bDGjt85FyRQzcNTDEIeqEyssfeDOKV4FCVd8KVAcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور در دورهٔ اصلاحات: مدال افتخار موشکی‌شدن ایران را باید به سینهٔ رهبر شهید زد  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/435891" target="_blank">📅 15:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435890">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIyymL9L8dfx4PdBZgArmR-AzwRqxBZoObn5CLsgXpAzfE5JKjbCQu7ziA6lqZUZavglIGSxutXwYad-2o2LY7ScGuxx9EZDeVz1DQJkbd49r1WueeOmNCcwi61iU2UdhrnHO6z3RbVvCkM-O0EJJP6OuBrqXY9Yz3xJniUBNTA7cHkURxtjbWxc09OkEGpI9lGgMQ2qVVVH584Suf2fPJ4Au-hPSp5gLKxIHSs15w-Vtw3VrEDXYmsGubIY5-MIJeLfqp3oOkHRnJ25ce0wj0mbsA6zKxgLyDMtoP9e5dRQiFQ-Z5AhF_nhEQnpjlOn1wPhoDiTjWLq2XyOmwAIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
جزئیات تسهیلات ویژه بانک صادرات ایران به کسب‌وکارهای آسیب‌دیده در جنگ رمضان
🔹
بانک صادرات ایران با هدف حمایت از تولید ملی و اشتغال کارگران، فرآیند پرداخت تسهیلات ویژه به کسب‌وکارها و بنگاه‌های اقتصادی آسیب‌دیده در جنگ رمضان را سرعت بخشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/435890" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435889">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S66AEe88z8M89aai-FZE-FzhIFp95i52TXVXIp4YQqq_5s5ZSYwY5g1_zR4PfDqJ6CrIYcMQS1rWsidMg5zY4GnjDi3cwJt0KC-KII6LDozQ0b3VF6Ufw8QKO4GWsUop3iznnhd5F2RkeZybW55bqkPdalRqxvlRXbYKCAwoXYrjoNxjgTMsAUJV2UrrBdnP756b7qp-s57x7Pq07A5drOuxttxD6cEBizLwTPyhkQ9UZXpQbkfvjySJt3b68D_YAzLLy_d6oMjuIRX2ApLyNXnGSLsxoQC2m-Tn9BEBYaFlK5kHWhzFgVblhuLRtqwclxTyJ-DIe3vcf1pPV98zCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مس دوباره از ۱۴هزار دلار گذشت؛
🔰
بازار جهانی در تنگنای عرضه
🔻
قیمت جهانی مس در معاملات اخیر بیش از ۲درصد افزایش یافت و برای دومین‌بار در سال جاری از مرز ۱۴هزار دلار در هر تن عبور کرد؛ رخدادی که از نگاه تحلیلگران، نشانه‌ای روشن از فشرده‌تر شدن توازن بازار جهانی این فلز راهبردی است.
🔸
مس که اوایل سال جاری رکورد تاریخی ۱۴هزار و ۵۰۰ دلار در هر تن را ثبت کرده بود، اکنون از ابتدای سال حدود ۹.۳ درصد بازدهی داشته و بار دیگر به بالاترین سطح پایانی تاریخ نزدیک شده است.
🔸
تحلیلگران، جهش اخیر قیمت را حاصل هم‌زمانی ریسک‌های فزاینده در سمت عرضه و تقویت چشم‌انداز تقاضای بلندمدت می‌دانند.
ادامه خبر در مس‌پرس
👇
https://mespress.ir/x6QK
@mespress_ir</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/435889" target="_blank">📅 15:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435888">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/435888" target="_blank">📅 15:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435887">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c0659d89.mp4?token=pwiaWSzC88m3dxIsA8wDseujbwyJjWAWEtU1XFIyCkyR6BJBSN1rKWcz4KXAgLYB2UsFJLInAiVqGwvFsQQdURAFC6BoFUv5Vo6Ll-KZvkjLc5UVa-J0cLXBCuAhUL7RPl3hP0fJNnqnSKEQj0ijx97dny4E31j9QDCiAjsVF202o__TPxRfTsfA96VISyHJJgAWhocwr5lInVVtVtsMnc2Gt2hAJBsC2UMTrFwxofzZ9v12EHkNtRbNqXOdLo9QiJGBeVD3FrOyW-HmQAxt-Wo9BuX7wCichStDKyR5griAU2j4VVoDrElQvcurDaprB-8V_p4G5pE2BeBhgPZRFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c0659d89.mp4?token=pwiaWSzC88m3dxIsA8wDseujbwyJjWAWEtU1XFIyCkyR6BJBSN1rKWcz4KXAgLYB2UsFJLInAiVqGwvFsQQdURAFC6BoFUv5Vo6Ll-KZvkjLc5UVa-J0cLXBCuAhUL7RPl3hP0fJNnqnSKEQj0ijx97dny4E31j9QDCiAjsVF202o__TPxRfTsfA96VISyHJJgAWhocwr5lInVVtVtsMnc2Gt2hAJBsC2UMTrFwxofzZ9v12EHkNtRbNqXOdLo9QiJGBeVD3FrOyW-HmQAxt-Wo9BuX7wCichStDKyR5griAU2j4VVoDrElQvcurDaprB-8V_p4G5pE2BeBhgPZRFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف نفتکش متخلف در تنگه هرمز
🔹
محمولۀ ۴۵۰ هزار بشکه‌ای نفتکش متخلف به مخازن ساحلی استان هرمزگان بازگردانده شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/435887" target="_blank">📅 15:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435886">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b828f779.mp4?token=rg-LuKHADfElrppUtSCc_TOxPRTbrG4qAqydZrHjN-VjQlLZUGlFdMjaN2rd7RrdQH7Q8dKThX3kqfGmjNB3YElY9COQr1YhZJWhhgG4cTdisomqwR2XZqP7008nbhjFS45HDn2o5cavw4q4eIvRg-YZGflneLlu_JZWRb6u4ceT8rRh-A-XsnjYuHuq8FrKMaP0XNw3lt13xw0W9SNB_oYHOnDpZKudr_j4eQt7DT_a6G3HuI76qM-UvbAc-ZqRiJ5HBfJZzB629CzwgVRI54KbCyn5Q-UZDioSCQb9GU17IwOqCCksl_xf3aYSrG91otpnK2leJbsV_5lauW0Hbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b828f779.mp4?token=rg-LuKHADfElrppUtSCc_TOxPRTbrG4qAqydZrHjN-VjQlLZUGlFdMjaN2rd7RrdQH7Q8dKThX3kqfGmjNB3YElY9COQr1YhZJWhhgG4cTdisomqwR2XZqP7008nbhjFS45HDn2o5cavw4q4eIvRg-YZGflneLlu_JZWRb6u4ceT8rRh-A-XsnjYuHuq8FrKMaP0XNw3lt13xw0W9SNB_oYHOnDpZKudr_j4eQt7DT_a6G3HuI76qM-UvbAc-ZqRiJ5HBfJZzB629CzwgVRI54KbCyn5Q-UZDioSCQb9GU17IwOqCCksl_xf3aYSrG91otpnK2leJbsV_5lauW0Hbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین خبرها از تنگه هرمز
🔹
پس از گذشت کشتی‌هایی از کشورهای شرق آسیا و به‌ویژه چین، ژاپن و پاکستان امروز خبر آمد که اروپایی‌ها هم وارد مذاکره با نیروی دریایی سپاه شده‌اند.
🔹
نظم ایرانی در تنگه هرمز هم در مبادی ورودی از جنوب جزیره هرمز تا مبدا خروجی در جنوب جزیره لارک همچنان پابرجاست.
@Farsna</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/435886" target="_blank">📅 14:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABb9s_vTfuHu6R1yt2oY0H4iFAOeUimzjerK0JLQKr0Yxqnkq4wPeNVwA0sFkJOp7Jp4kc3cxaVxVhX7zNuBBCcyF9wznczkJXZu84ZLRtcs67iTuL9yviIlVN3BdilHssNrtENVBaj9HSsgr_0wP4BK1HBpjVuJxO33PT6TdkQC2npxcy_4TQgD3cnsGWqR_sVvY8kVdoeL1hKAqaE2o5Cv_M6d8hAG8ujWNpsOcHS8wtPgFDU4sHtUdHFG1_nYgsOUXjiv0GCxTmHTwhmMk3NMQ_lC4dPR_v98JVEgSq2EOhxxZJC04DgsRFxdCXYgF1TKxuRC47HqJJ-jt-LTQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مشاور رهبر انقلاب: این خویشتنداری همیشگی نیست
🔹
ایران سال‌ها به چشم دوست و برادر به آنها نگاه کرد ولی آنها با پیش فروش استقلال خود، حتی خاک و خانه‌هایشان را در اختیار دشمنان فلسطین و ایران قرار دادند.
🔹
پاسخ جمهوری اسلامی به سنگرهای استیجاری سنتکام در جنگ اخیر تمام عیار نبود؛ اما قطعا این خویشتنداری همیشگی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/435885" target="_blank">📅 14:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQrUSVddRLvMzpm0h6WbeRR1xm5WqIGX4FzNrIGT2q4oTij7voAJh8PA1G25lweykGc9AVNVNGTeW51IRi45pyv5n7w3acpgcsw6T-hkqyM_-SY2699yJFWPq2M2BVaJcmWk4jJZ45CGfOucbHU0ldAnVu2ZoTg3NRuwatn1Y378PPO8-cQgH9yAoJbdQrhYq1dCiv8uoOtEJayDQHD8wVM0fppEWuB5okR2jMfEBKw6hKEtGfe_cm079M7wAK1V_ufWdQiMvOHVXTRYYLeeNhEU05U_lsmLGB7D3XaiIfrT61P4LTxqlbPrGfH9SDCuqu3VMskjQZMrIEkjIyi1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت‌ملی مجلس: فقط کشتی‌های طرف همکاری با ایران حق عبور از تنگهٔ هرمز دارند
🔹
ایران در چارچوب حق حاکمیت ملی و تضمین امنیت تجارت بین‌الملل، سازوکاری حرفه‌ای برای مدیریت ترافیک تنگهٔ هرمز در مسیر تعیین‌شده تهیه کرده که به‌زودی رونمایی می‌شود.
🔹
در این فرآیند، فقط کشتی‌های تجاری و طرف‌های همکاری با ایران از آن بهره‌مند خواهند شد. حقوق لازم در ازایِ خدمات تخصصی ارائه شده، با این سازوکار برای ایران اخذ می‌شود.
🔹
این مسیر کماکان برای عاملین پروژهٔ به اصطلاح آزادی بسته خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/435884" target="_blank">📅 14:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435877">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYVHWixb6PK2D5tj9GpGE6gLVVemjTfFl7CQKHCLL5FUcA35pU-GwmaQs6bY797Fc2VhYrWMPFiQi6aRqvB2K7eGwluNzACWpNFpaKTN2WXGYQ-w5x-zknZtxdHSjzno_pzJKNV2f1YP5Z6cFSi_5t5mEgTPeJRY3FnrEOtGAVSzmYECnLFBbpctL9Yd3XzTAvZg0W_8o6XmWT0VqXeAvQqmTAdrq5HCVZyrJWEDw25r5BJD2bds3Sb0YnYy6f0MYFzO1kJbVowDX60rmacZO233xsPQ-EWJ1Ea1nwtcerPwcyaaH-ja7QCHuYT01OMoR5TvocmiUlviJMOrluSGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVJSl79NZJS1Rl4GuQ5wzR6PJo_3bS5oZZbJZ2B02Rx7cM6NlND-7Nfn3RTSeTydWvJXP01-wwY-_oinZbVoGZsthhpcCcLUMcLG6Nnn2BnynZ7jB5Mar2hrZZKqk0ZacX4yJ_5377xUhI02UCaN-P8rEkepktg4V0FyxGeeAppjRNIz-1fviOj_B6lmbG0jvtlkf1g0w-fxy1PfyjJsaQkfdeiMoGmZfDt2bnu9aL9uE5xTxSlqX7o40-j1DP_qa5PsDXk6NK9HxzR8_LAShZzJOqre5PauqKz0Zc_hOeeF04Cly8IKBuIi97Whox8V3gm3zD3m5XBgZZoaAtQdFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLgjFIvO_wNvpB83bHJPC7TmzuvJBEhB7jkHK7kb3NMQo-bSDKovL_onj8BBIywZenkq6pZ-IFnlo0EXM9uSMRRSjUCRu6oqbBdXGLBgZjggEjDVTwlacBR7pcfrklztoXqlllQ5F5vQD4xAq1P2Sw3ZQp1y8I2UTX0-XAZNmHcERRyplnDfEVzHPslHBBStHXegVKZ2pUambJEpWi4Sq_p8NpMriS6eEOjIeMmTpIdshx9IF_bXqZwMvJgSsjsFACNLqqksdZpUMxPuDOEeL7ZI1A53x6Uhigqd52dLudPpDEGhz1PxiVQkmJEuz1FUIN8kfAWMDEHE8D-3elNRrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0JHpTciA4j2qVaKrENReT6g0EyR_TL8NQY_bTi1brIKwaTOgrQSxHq6Nz8TN1cg7tHsJjUfRMtW_yzEty6mMOf2A42a23v8RY7U7m5ZtNezaslUDX9S4bF1G4MmUzJs6Vd_O0QfGvBo9oaCzoqZrD7ls6aW1_livDgKVTmmSs7hFyA46Qwju-LLFbLvIYSzxraK9Sh8rjLwkkdHu47DoS2VFk7cpfRW83l4tabZ1Ht6JY100bWVg4c7ThrXSlf0t9wXqegbL0RecvuW3athMdcdv41U4mOqJN2N8aoP59I2XI_2GmumAeWj5M1aHC2cBDoo80qf4LlqKHycm6fGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNaCJjCYyl7_XaNZ7PCyGXx5Z-Noxtj5ZyrjDpFwb9QZJ18z7_rhcHFSCLRIohva-m8cNxUzCjjnuYwZmaLkQK1TwK0rn2NA69f6_LxypHUiY4XDSGqIpsfg9AaUG1rH7agl5e9mQmxpUDBCXzleI5CcKTfuA2zWIhAg_XU_GPXP6_8OnhDRdGEnHaiGSQ_Q0hXA9VanHrMVV5Qr4fpUh17aIwVVpjyZKbuj97M7R7fm_qxBH9eWHpec_2Q4ImQ3BybKY6BbjCcawSwcXbew38AMzOu9aUx-yqSl5nRPThwqpE6booH8pusQPoaoSflUwzeMqEz0qd-igarn02z4KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfQGAQJ1V4wz1WEcCi7JKyErbKDC3oznXk5m5SC0LrfVY1w-XRnMFTFfaf7g7Hx5ZmQBOjm1MNaqtNp4YqXCWu17A4zKJAZ-56dPaCndMhRffkatkgFZ7TOoxPlbahJBK3oM-jxqS2jqPTW1A0yi2HLMueckcPcPYGW7B3TsrSxEt41ySqN-plLfGSwZ-G2SD3HP8DMG5kBrYSwdGrdu3J21nSlAGc63AoPAYSItI_X9PRI1bLm7XzpHGSMGg7YzS8qbNbDKmkP7OO4fiS1qTWX7b7-RqiUuuCwlCJKo2NX4710ICMw-5PGvHg3JyfW8-pAWlsnkOuFQOPaPJ-h2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RYkYr-NWO8Tf-rZWMupC67YypKPkIMIb6Zy74IitfFMVoaMc__-1MBjWBaQ3whqU0s6qSXmph5doyu39qhoRHfS7wSS5mi1hHP4G-6pVhVxEP_5KIsWfzYefuueKex7Sjxzr4nvR0WckJQXorrURtuaiSzeWO3cgbHo5xtBWNULF1HbjCabxbH9vbX6lz3OoT-V7J3n89oW0t_N14Cb-wLkquECM2R9n-kxgRw84q2stMdmpl4SXjY-IHYnDSy41LM4eys9GnIm8bY2zEZuExddKcVT5A_X_ilU3MolzyD414GZPbB7mfr1c-WAUgVwAidb0_ekhaTC-Ti9UprkdnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سیاه‌پوشی حرم امیرالمومنین(ع) در آستانهٔ شهادت حضرت جوادالائمه(ع)
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/435877" target="_blank">📅 14:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435876">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات در شیراز
به‌مدت ۳ روز
🔹
روابط‌عمومی ارتش فارس: عملیات خنثی‌سازی ‌بمب‌های عمل‌نکرده از حملات اخیر در شهر شیراز از امروز تا ساعت ۱۴ به‌مدت ۳ روز انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/435876" target="_blank">📅 13:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdRcLurr78cVtVPZVj_l_dsHpIsy4W2LWzJxZkfJ_yHHc9f_Qj2gxOz7AcsGlmBld6ZYwA4tfQO7XCakWraSDbKJ1cgu1I6iRV0puFocv4Mm4E5Q7RTjDiCTfox_vtBBLB9MrnlaTiJFVR82UXSRVFPjwpzo8upIAFyaRXqWp0cRBDQMEBqzfwx5znT8Jp6v098giqj2B54TQpDTSZY2acLnig8A774iLEhpJmfAnGBslRxKnABlN_8yj8ryexZMczc444LeGTugtlhFONxR75lZ7TAekk9W1MV89jVZ1qMa0jmhZN6Ls57D39biEHmunrnOKh5BCWDYdPmRs5qWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌های بزرگ روسیه وارد همکاری مالی با ایران شدند
🔹
پیمان‌پاک، رئیس اسبق سازمان توسعهٔ تجارت ایران: برخی از بانک‌های بزرگ روسیه از جمله اسبربانک و وی‌تی‌بی‌بانک که هر یک دارای دارایی‌هایی در حدود ۴۰۰ تا ۵۰۰ میلیارد دلار هستند، با بانک مرکزی ایران و بانک‌های عامل کشور حساب‌های کارگزاری فعال ایجاد کرده‌اند.
🔹
این بانک‌ها از نظر حجم دارایی تقریباً ۲ برابر مجموع دارایی بانک‌های ایران منابع مالی در اختیار دارند و همین موضوع ظرفیت قابل‌توجهی برای توسعهٔ مبادلات مالی فراهم کرده است.
🔹
اتصال سامانهٔ مالی ایران «سپام» به شبکهٔ روسی SPFS باعث شده انتقال ارز تجار از چند ماه به حدود ۴۸ ساعت کاهش یابد و حجم مبادلات ارزی رشد شدیدی پیدا کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/435875" target="_blank">📅 13:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m72PdbE82vtuDTDAxaZgz2ifDzqqgnmL8cnCGAW-2JYa4w1uZDV_7cU-HG7azhuFSQinuzyGubTQ6CrhXRKQVlkTBY3h5Ew6zzauyZC3pqDufu3juZgOcLjndo9EwyOOw5CtFKeZeTxvGTbb_F9RzhtoSRpjCJMuRJF1hVt_qy1LOVrBlQxp_2drkB9yqB0TC_KG4eYiYBhzqBMHgGO1-D5fgzcLf9sgQjncH49J0ST4RPTUDjMOxNbgR0dk3g-zFBVaNBgjBPy84DKAcTQQ2pDqpNMT_NIcaWdTAu_3237E1uiaN-SDifck8ADkPFNE7qUNSt9lHcNPjU5Z5_tkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاتک ایران به محاصرهٔ آمریکا با مهرهٔ چینی
🔹
یک نفتکش غول‌پیکر چینی که از تنگهٔ هرمز عبور کرده بود، خارج از خط محاصرهٔ آمریکا رویت شد.
🔹
این نفتکش پیش از آغاز مذاکرات رئیس‌جمهور چین و ترامپ درحال عبور از مسیر تعیین‌شدهٔ ایران در تنگهٔ هرمز در کنار جزیرهٔ لارک دیده شده بود.
🔹
حالا پایش داده‌های ماهواره‌ای نشان می‌دهد که نفتکش «یوان هوا هو» از خط محاصرهٔ آمریکا رد شده و آخرین سیگنالی که ارسال کرده است به روز پنج‌شنبه بازمی‌گردد؛ یعنی زمانی‌که ترامپ در پکن حضور داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/435874" target="_blank">📅 13:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU7GznrVP4Ac3WkBY8cD5PbDAkpIPlHpusB1cYD5v2G041Cp7x45HEIaCujdbOmHLBTJwGd-Pil_6jIFSDzuu2bhzVMuSTSdY525iRnUCI1Zm1GC63_V6tOOX2G9gM2W7ggG1R9AgV6V_WQMUqVgtX8AKXq5GBhWxRRYTKWyh7lT-YVF-09JkK8hR4zEp0q9ii1A5PoFTRYkLRVd65BfLWyQ7McIWCbolYij7vHajgWmA5MVnoNMkhzizLUzB0rYqm-JJLySbe1kOmJFF2T1qOnjiJu7iQ0jvCGOG0G8SboHz4SkgDeGdmc-gHYopJmKEItmogDIyc_kYGrcXGybTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ، تجارت ایران و عمان را ۲.۵ برابر کرد
🔹
باجلان، فعال اقتصادی ایرانی ساکن عمان: حجم مبادلات تجاری ایران بعد از جنگ رشد بسیار زیادی پیدا کرد؛ به‌طوری که در این مدت از ۲ میلیارد دلار به ۵ میلیارد دلار رسیده است.
🔹
بعد از جنگ با حرکت خوبی که در بحث مدیریت تنگهٔ هرمز اتفاق افتاد، حجم بسیار سنگینی از کالاها از سراسر جهان وارد اسکلهٔ سلطان قابوس، بندر سویق و بندر صحار شد.
🔹
عمانی‌ها نسبت به ایرانی‌ها احترام بسیار زیادی قائل هستند و مفتیان عمان در زمان جنگ به‌نفع ایران اعلام جبهه کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/435873" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P583t9P1AHP4fkOeyfudQV8DnenTu_mSiQvyTaQ_XcQq_gDOxjmkxftOdOsYFVgYmd8809IsO86qsT-qGEoRk596qievSZA68Loji-CKhW1ruMy-QGQ1Fa3igqP-M81V8Bx4YFZkhGO4YTHtdTPHtivzb-ILMxHdQsao9P1Q56woyI4ym_FKD82nh3qgE0t3NlJ1tpLWRPvYR51X9zGwV9l88ZypSadpOLLWYBrMv8jK1CsgnkuZRAU-EexZZJpcmc1ZwW5ALKdA3WSQnILr962aId9l1XZVJqbXxNAQJDv5_aJq6PctHEkpWPFXFJJxajErCL3jIQ9zEs0hsnkR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ ماموریت ویژۀ رئیس‌جمهور به معاون اول در سِمت جدید
🔹
پزشکیان نظر به ضرورت فوری استقرار حکمرانی یکپارچه، منسجم و کارآمد در فضای مجازی عارف را با حفظ سمت به‌عنوان رئیس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب کرد.
🔹
رئیس‌جمهور همچنین «تدوین و اجرای…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/435872" target="_blank">📅 13:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2006914dc.mp4?token=tfBhvczb42ksOa-1het9-29dBraURBvKWWMIffDLqb8o0xo3nHONuTZiBpPGyTM30A6vukEVFh0NfRN2NtHKj4PzBpXQ_2x3Y7zX4GH9acYanUGXpGHt3_32LDuBfQTyDtU3k_20RZqGpnHeMuo4jZyqhBYUJ2eLncJKvOtqYnbn51SyKhPqujUTB4vdBs3QY1MgYGFlogLBjKFXmP9lEVfQpC-EHSgasTK64erGVF-xGUFtcSXJlwijiQn8hXTyiBFhLBGCHHDmzbMdJiIWt-E5aWvYuuizN4u4H10Oon9ccZbIdWQXijfW_J8LPiXgjl4w5dNau7s5XL8sieOavA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2006914dc.mp4?token=tfBhvczb42ksOa-1het9-29dBraURBvKWWMIffDLqb8o0xo3nHONuTZiBpPGyTM30A6vukEVFh0NfRN2NtHKj4PzBpXQ_2x3Y7zX4GH9acYanUGXpGHt3_32LDuBfQTyDtU3k_20RZqGpnHeMuo4jZyqhBYUJ2eLncJKvOtqYnbn51SyKhPqujUTB4vdBs3QY1MgYGFlogLBjKFXmP9lEVfQpC-EHSgasTK64erGVF-xGUFtcSXJlwijiQn8hXTyiBFhLBGCHHDmzbMdJiIWt-E5aWvYuuizN4u4H10Oon9ccZbIdWQXijfW_J8LPiXgjl4w5dNau7s5XL8sieOavA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجاهد: شهید حاجی‌زاده، دورۀ مدیریت شهید رئیسی را نقطه عطف پیشرفت‌های فضایی کشور می‌دانست
🔹
معاون پیگیری‌های ویژۀ دفتر دولت شهید رئیسی ادامه داد: گمان من این بود که اگر دولت شهید رئیسی ادامه پیدا می‌کرد، بسیاری از مشکلات کشور و مسائل ما حل می‌شد.  @Farsna…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/435871" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b62ce881c.mp4?token=uymyT4vkuPb8tbWkrT9JbsCG11qqWfxIUEo-8xjlJKI3dy3VM__MqJA7VgBDyTsRFiL6jnSMtLGqvm2KcR-u6g_mwmnmQkmcAcychvX3y6b26pYzhvcqUMsgbQ_UUMHYDSdqegaSvoO86wR4Ee97fY-7fj_McpKTCTFMfR7ku-4uZp8He_jWuv-5lnICu_LEqRoBuz_l7665X1kMtOOBJkHsleIHZ-vmf4Xm__3DcWQ_ZBpzlADPe4wULPV3ilV0tUr7n-Z4c1b8A2HLGTitMKG4oaQIQBdsCSoKUAKlVg0F9HFBJCVlOfY52joDK3d-xzqT8wcFGoX4FUcxndqGaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b62ce881c.mp4?token=uymyT4vkuPb8tbWkrT9JbsCG11qqWfxIUEo-8xjlJKI3dy3VM__MqJA7VgBDyTsRFiL6jnSMtLGqvm2KcR-u6g_mwmnmQkmcAcychvX3y6b26pYzhvcqUMsgbQ_UUMHYDSdqegaSvoO86wR4Ee97fY-7fj_McpKTCTFMfR7ku-4uZp8He_jWuv-5lnICu_LEqRoBuz_l7665X1kMtOOBJkHsleIHZ-vmf4Xm__3DcWQ_ZBpzlADPe4wULPV3ilV0tUr7n-Z4c1b8A2HLGTitMKG4oaQIQBdsCSoKUAKlVg0F9HFBJCVlOfY52joDK3d-xzqT8wcFGoX4FUcxndqGaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خلجی: شهید رئیسی پنجشنبه و جمعه‌ها را نیز به روزهای پرخبر تبدیل کرد
🔹
رئیس شورای اطلاع‌رسانی دولت سیزدهم: رهبر شهید انقلاب دولت و شخصیت شهید رئیسی را با دوران پرافتخار امیرکبیر مقایسه کردند؛ این اتفاق بسیار مهمی است.   @Farsna - Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/435870" target="_blank">📅 12:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6f5b69a3.mp4?token=SQfwuv7lt46CFpnL2Yjt3mP6VPxtFq56xVO3N2-L9yqITT3CyPspuEHU_M4m5NbJJ-ka-KCXaZPbOTGRbEct3u6IQwglKaqgLVtT5pXT1WpnWDsxKWHjGXaS0Y0cF1y6qVN7zoMUhpKAcBVO0qoA9N1uLFrCYjLf9ExhGaShFaAT2v2yx45Haek-HFxe2Cb8qfFYFfzC7ry2uX9STZ-gRDh_cvHalzoij8nhcFYBBD3r1G11Ach_E2rlLKvJVpyC6PAxrnwXFs_KdWRPVku31-QolG_1yznN0K_NMf_5ag8DUhZfw3GWx9RKxTNBmhjrAb-zUwQzajnxrlJLvfJLmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6f5b69a3.mp4?token=SQfwuv7lt46CFpnL2Yjt3mP6VPxtFq56xVO3N2-L9yqITT3CyPspuEHU_M4m5NbJJ-ka-KCXaZPbOTGRbEct3u6IQwglKaqgLVtT5pXT1WpnWDsxKWHjGXaS0Y0cF1y6qVN7zoMUhpKAcBVO0qoA9N1uLFrCYjLf9ExhGaShFaAT2v2yx45Haek-HFxe2Cb8qfFYFfzC7ry2uX9STZ-gRDh_cvHalzoij8nhcFYBBD3r1G11Ach_E2rlLKvJVpyC6PAxrnwXFs_KdWRPVku31-QolG_1yznN0K_NMf_5ag8DUhZfw3GWx9RKxTNBmhjrAb-zUwQzajnxrlJLvfJLmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضوی: شهید رئیسی ایران قوی را در سایۀ اجرای عدالت اجتماعی تعریف کرده بودند
🔹
وزیر رفاه دولت سیزدهم: اولین دستوری که آیت‌الله رئیسی به من دادند موضوع کالابرگ بود. به من گفتتند به هر شکل ممکن باید این کار عملیاتی و اجرایی شود.   @Farsna</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/435869" target="_blank">📅 12:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ujns3dyK8VA-tob27L5J79v9Fj-gU0gCxOHkIATWYY8WSI9DtYKloNUUTuOBII8i_Tm3Fcy4SR20bFjprejtN0Z4_OferxILVk4Wsg9snfqHs1m1n6Oz25_bbR8appY0fAV5ETW-z7hG7Rh79oZlWT5qzFj_gL7kd3Bk0pjbPE8bLWg6EFcN2PaZB96DelHvKSXVssi27onGQvExjeKA1XZhhRzFiJ1RAIu_g3X7OBhpt4G2a4aIYKVys3IxL05nHYIy8N31jXz049kziZEV1AYeqnmUY49zsxlO1YyT3CKjMMwGDYJ-BhlhZedc0wopvm4smnV44NhMxNxJEr8Fug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز نمایشگاه مجازی کتاب از ساعت ۱۰ صبح
🔹
نمایشگاه مجازی کتاب تهران امروز از ساعت ۱۰ صبح در سامانهٔ book.icfi.ir آغازبه‌کار می‌کند.
🔹
نمایشگاه به مدت یک هفته برقرار است و کتاب‌ها در این دوره با ۲۵٪ تخفیف و ارسال رایگان فروخته خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/435868" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ad4ac91d.mp4?token=rxuPMX-qIHaPX4KyqHMqLPe-aFBfjbaOnCEfRXliM_ch9XiMJfhI7pE6TxYPKSLwAw6dwa_eE1qRAWDY_1EQxkScPlSqsTatV_uexVQ-ZBhRalHISLaIZ0mNg8QxAVCdpRIiPN7IHJmoTv3y7dk-N_Bi4YZGyC0nce2UvH8WWEopR8hmwEGeiY9yuskjMYtcINNvxkHnmB9Ezj8JHgQlWGcWh26IHNqgUHMU6mAZv_M11oY8fEUhhsE04Sbqh04LnXgbtL0eFjAHGVKeD6bVst2yIMp7Un1wEb8UDDc15rlxccATrwYTiUXbbkDMsundP1UJiLZnzM1T-lpdTeiC2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ad4ac91d.mp4?token=rxuPMX-qIHaPX4KyqHMqLPe-aFBfjbaOnCEfRXliM_ch9XiMJfhI7pE6TxYPKSLwAw6dwa_eE1qRAWDY_1EQxkScPlSqsTatV_uexVQ-ZBhRalHISLaIZ0mNg8QxAVCdpRIiPN7IHJmoTv3y7dk-N_Bi4YZGyC0nce2UvH8WWEopR8hmwEGeiY9yuskjMYtcINNvxkHnmB9Ezj8JHgQlWGcWh26IHNqgUHMU6mAZv_M11oY8fEUhhsE04Sbqh04LnXgbtL0eFjAHGVKeD6bVst2yIMp7Un1wEb8UDDc15rlxccATrwYTiUXbbkDMsundP1UJiLZnzM1T-lpdTeiC2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقاپور، مرد سال فوتسال آسیا: این دشمن در حد مردم ایران نیست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/435867" target="_blank">📅 12:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ9PxW_kk8aomk0urUIBscIBUezVbvOTo4rHwf7CN50E3ML8XNwAjhBJRVXFV_x2YvZnc5Hn5VZSgPad9gsJ-GyrO3qUdxqCs-XAZKJi-9wUlRo-xXjyecNJW_oMoZI0kbQUIxOLgxiNqxQsgZEtA-nWHEZRqvcn0tgAYbhRIMaG7fvu5Iy2IVG3rlBTyieplIOOiCpaISbI0UlNPdQ8qqc2OR5Um5CsiJMOpx95bknV-Ta8ZD0BYBajaKg4MuSUT_toeJPCVAK-kDi7YpXotssI3TnuMcgSAHVWsZuYznI6M4MfGP1n-skJic1EPaoBP3MUaTbjwSFZMTXBTNKE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گندم به بازار سیاه رفت
!
🔹
رئیس بنیاد ملی گندم‌کاران: در حالی که وضعیت تولید گندم امسال بهتر از پارسال ارزیابی شده تا امروز یک میلیون و ۴۰۰ هزار تن از کشاورزان خریداری شده که نسبت به پارسال ۲۸۰ هزار تن کمتر خریداری شده.
🔹
کارشناس کشاورزی ابراهیم مرادزاده علاقه نداشتن کشاورزان برای فروش گندم به دولت را هشداری برای مصرف گندم در خوراک دام می‌داند.
🔹
اکنون قیمت هر کیلو ذرت دامی در بازار آزاد اگر پیدا شود ۶۰ هزار و قیمت گندم ۴۹ هزار است و مرغدار گندم ارزان را جایگزین ذرت گران به‌عنوان خوراک مرغ می‌کند.
🔹
رئیس بنیاد ملی گندم‌کاران می‌گوید دولت پس از ۴۵ روز هنوز ریالی به کشاروزی نداده و انگیزۀ آنها را برای فروش به دلال بیشتر و احتمال ورود گندم به چرخۀ خوراک دام و تهدید خودکفایی را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/435866" target="_blank">📅 12:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">توقیف اموال ۵۱ نفر از خائنین به کشور در یزد
🔹
اموال ۵۱ نفر از خائنین به وطن و افراد تاثیرگذار در شبکهٔ همکاران دشمن در راستای اجرای قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونسیتی علیه امنیت و منافع ملی در یزد توقیف شد.
🔹
این اموال شامل وجوه نقد بانکی، اموال منقول و غیرمنقول، سهام شرکت‌ها و حتی اموال وکالتی می‌شود که با دستور قضایی توقیف شده است و بررسی دقیق‌تر در مورد پرونده این افراد ادامه دارد.
🔹
از این تعداد، ۲۰ نفر در داخل کشور حضور دارند و ۳۱ نفر دیگر درحال‌حاضر در خارج از کشور به‌سر می‌برند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/435865" target="_blank">📅 12:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435863">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4385b6bb5c.mp4?token=Qqm0giCMeWv22_Ta54RsLokOY9x1k_HHlbA2qUIpXDLwUIAcWWT6JLlAcVmcj4zpFbwWqjCA9xnH4cYHWxzkdy3qsRuIS1eR1o7yqDKJm2-qGaCpuTE5SwNUDEggC0C-U8ea4L-yY-n7XpJ5MfGy2nIKdz9llgwsPbllJTJ3sD7ZNGjU1uaTEXaqlYMBbynno6DMJyZKR-dpteCMApqKx_9b9XRYeRdVYwc2cBxtDy4106agbK_N_P--5LCOs463rXNVkKx3WeebArHx1eLYVcku6fEXwF_zKNpZm6m3Lt9tWPehI2IZ2xeAAbOCpFziyOpUJ4zPCCFDkWwh2Evw7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4385b6bb5c.mp4?token=Qqm0giCMeWv22_Ta54RsLokOY9x1k_HHlbA2qUIpXDLwUIAcWWT6JLlAcVmcj4zpFbwWqjCA9xnH4cYHWxzkdy3qsRuIS1eR1o7yqDKJm2-qGaCpuTE5SwNUDEggC0C-U8ea4L-yY-n7XpJ5MfGy2nIKdz9llgwsPbllJTJ3sD7ZNGjU1uaTEXaqlYMBbynno6DMJyZKR-dpteCMApqKx_9b9XRYeRdVYwc2cBxtDy4106agbK_N_P--5LCOs463rXNVkKx3WeebArHx1eLYVcku6fEXwF_zKNpZm6m3Lt9tWPehI2IZ2xeAAbOCpFziyOpUJ4zPCCFDkWwh2Evw7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضوی: شهید رئیسی بر این باور بود که ایران باید قوی باشد
🔹
وزیر کار دولت سیزدهم: ایشان بر این باور بود آن ایران قویست که می‌تواند در بزنگاه‌ها نجات‌بخش محور مقاومت و ایران اسلامی باشد. @Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/435863" target="_blank">📅 11:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435862">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055e57e9b1.mp4?token=bm4WdK3cSqm5aOljX526D6Dr-NuE9oXhS3ymVilmed2DLLkz4FstygiwsfCqZHdKRAOF5tajY6y6ai5MKV1T7tpvzRpWp3USc6tfHUo9IT7AqM-4RjcC6rRONZnk2Bs0HvXNvRVcWxgshk5Ce0Bl8di_0pbQEh4MauoVTu7epPdmk2cQJXEhgz1FiR659J_065LfWKg8ei-ZxXMHneUSbx5iBJP2DyljZL01rPHU-ztuNlorfRrbmsYFPHyYe4KDdUhrHZHFmoKh6XjMsahlKusBeEdNePpkEm4U_GLt7nXnTBQB5j87cpJDQElE5lplC8AurClOridsnZFFzhi47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055e57e9b1.mp4?token=bm4WdK3cSqm5aOljX526D6Dr-NuE9oXhS3ymVilmed2DLLkz4FstygiwsfCqZHdKRAOF5tajY6y6ai5MKV1T7tpvzRpWp3USc6tfHUo9IT7AqM-4RjcC6rRONZnk2Bs0HvXNvRVcWxgshk5Ce0Bl8di_0pbQEh4MauoVTu7epPdmk2cQJXEhgz1FiR659J_065LfWKg8ei-ZxXMHneUSbx5iBJP2DyljZL01rPHU-ztuNlorfRrbmsYFPHyYe4KDdUhrHZHFmoKh6XjMsahlKusBeEdNePpkEm4U_GLt7nXnTBQB5j87cpJDQElE5lplC8AurClOridsnZFFzhi47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک با اسلحه در برنامۀ زندۀ تلویزیون!
@Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/435862" target="_blank">📅 11:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d5637a2e6.mp4?token=gIoQIFIy58PZgR61rK7-_o_WS70jFNut72x0j9yYWK8ZXHaPSteWLfKLbwisgund3eiMnEtThzMxv2UkYn1kqZ8nu2IRBCa2valCjLWJHxDaKVcnbxsMUrboX8cq97nHJGHGEv2sIjDlHIRCEy4PvZ-_AC8z_g3wZT197xUKZS20keCw7He2RpcBNXURGI233LejAlPCMzffo8c0Vxs4-SFulHJIQdbJy3hm9bS4DsJXG5Xyx7tei3h2ahSzBq4stxeK3v7KTNIVjiEy7ATrd9bT5OQpirYcF7hAz7zBRsuw0xk9TDFbBsNmzGg26_6SK6CyrM8a_Q4d-JTG955GWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d5637a2e6.mp4?token=gIoQIFIy58PZgR61rK7-_o_WS70jFNut72x0j9yYWK8ZXHaPSteWLfKLbwisgund3eiMnEtThzMxv2UkYn1kqZ8nu2IRBCa2valCjLWJHxDaKVcnbxsMUrboX8cq97nHJGHGEv2sIjDlHIRCEy4PvZ-_AC8z_g3wZT197xUKZS20keCw7He2RpcBNXURGI233LejAlPCMzffo8c0Vxs4-SFulHJIQdbJy3hm9bS4DsJXG5Xyx7tei3h2ahSzBq4stxeK3v7KTNIVjiEy7ATrd9bT5OQpirYcF7hAz7zBRsuw0xk9TDFbBsNmzGg26_6SK6CyrM8a_Q4d-JTG955GWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشریح برنامه‌های دومین سالگرد شهادت آیت‌الله رئیسی  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/435861" target="_blank">📅 11:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99a5e9d49a.mp4?token=eQkpYABj_63d2VsCK3UhtwbPybDYDuRLW7dVyADh16rCg5w-nPNXxqy2MDtxaeLcYAT4K6E4GyeyLUiVV82HLk4AU88-ijmlcCIMaglg_4VClPBNwyiks9JpgKXT9AH3ZMwKVmVVzPI5lzFAD6eH4LHujjOXfod7V9sOS97jafTrgEj_5AzqHwmuCcfm9LM1v48IAntXNvUtmXx9OGZdvVBGiCg3KaUys9pHVlB2wQGJhlVx-QJjGytEZhruqqzsEV9KS9Af49Bz-TM3pu6IqogaPFE6jyOc9AfopQ0vnEosuN6Iljjp3WIOih-ayJz0K1dPVhS6T1XXAy5x_Z81GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99a5e9d49a.mp4?token=eQkpYABj_63d2VsCK3UhtwbPybDYDuRLW7dVyADh16rCg5w-nPNXxqy2MDtxaeLcYAT4K6E4GyeyLUiVV82HLk4AU88-ijmlcCIMaglg_4VClPBNwyiks9JpgKXT9AH3ZMwKVmVVzPI5lzFAD6eH4LHujjOXfod7V9sOS97jafTrgEj_5AzqHwmuCcfm9LM1v48IAntXNvUtmXx9OGZdvVBGiCg3KaUys9pHVlB2wQGJhlVx-QJjGytEZhruqqzsEV9KS9Af49Bz-TM3pu6IqogaPFE6jyOc9AfopQ0vnEosuN6Iljjp3WIOih-ayJz0K1dPVhS6T1XXAy5x_Z81GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
نشست خبری دومین سالگرد شهادت آیت‌الله رئیسی را در پخش زندهٔ فارس و آپارات ببینید  @Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/435860" target="_blank">📅 11:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435859">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaEncd2rswxlEF5GeBly6-uEC7_wKKe9mcUClH1wukM1bIqcSf8CJgJFd_HZTYTlUZhc43dzUMAZJYioC4nuEDahmIa1Cz8BOLHgrAE9Uo2bHDII8xYvNpk5k7lm9hQ6Kbi4YT-ElsEI8ZqSzWME23CvWoKdXg-marM4KOvWIFZbRciiV0GwI8LVdKayLbIjOl0Df82D7M-_411y2TQGf0kq43V6bA7vDqdXjTgokiAMnzJyx_y4bK5RaK9joKqitlxkhSqTdESbw01DnsoJVJqo_z2SHsH3TJi4WsUE8RA5uxlLzNWrwYm6pcmY1vTPFYHQeOm9hl22fW39MdzhnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
نشست خبری دومین سالگرد شهادت آیت‌الله رئیسی را در پخش زندهٔ
فارس
و
آپارات
ببینید
@Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/435859" target="_blank">📅 11:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435857">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آخرین وضعیت نحوۀ برگزاری امتحانات دورۀ متوسطۀ شهر تهران
🔹
آموزش‌وپرورش تهران از پیش‌بینی دو سناریو برای نحوۀ برگزاری امتحانات پایه‌های هفتم تا دهم خبر داد.
🔸
سناریوی نخست: در صورت تداوم شرایط فعلی، احتمالا امتحانات داخلی دانش‌آموزان پایه‌های هفتم، هشتم، نهم…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/435857" target="_blank">📅 11:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435856">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTIBhIdnt5sJsvMV-6VrH81eBTYagu5aUb6mXeMKVEhtqp0-PTF874W24hsQ2Qd5rAftklIBY7rPmApIJZPcIKVy6m8IUvHu7SEYGUw9Nu9bn9HXPdIukz7mpPeeuoYgI25dCYDQyY5BhJl_XXK_fBd13ym8mj0f9U00pu7lCnPBHZjBnvrNNjLLQnAEIiyXXPFdrrLNm9hHY3OJxtG7d9Kfx7Ke9_XEDFFsHhRDc4MiQW6obsKvF1I9CGW8K7JQP791XFtgx7vsaEUHMmFHpxR81Rf6W-CBI2M5vZATrU4gK4Tt0bvx2xvwriM6lXhyTHzR4h-BxYqcVRaUpqnXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود بیش از ۱۷ هزار زائر ایرانی به سرزمین وحی
🔹
رئیس سازمان حج و زیارت: تا پایان روز پنجشنبه ۱۷ اردیبهشت‌ماه، بیش از ۱۷ هزار و ۵۰۰ زائر ایرانی وارد عربستان سعودی شده‌اند و روند انتقال زائران از مدینه منوره به مکه مکرمه نیز به‌صورت منظم با قطار سریع‌السیر ادامه…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/435856" target="_blank">📅 10:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435855">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ca9b32ea.mp4?token=dG3dF5OyYUwQeNKBeBE2BsMi9OVNIscDwwzZl0Vif4es3sg1dUxHqqIWHcCKv2owlhqLv9KEpK6RRzVtawX5KdOOxL_mTRkj_lGjlVwUQRIzy-scv6uEIxnvQ9XgNjcRIAetykRG0PYVYuZpyMYj7mtPWItd1slJp1JrRpNti-E0xReGjdCKf9wJN7_L37prONHEVfXhOYbxtEdvw6F9QQ6-EJvOJiiwhJrW60_9a39NSt9YrzAANd9A6r0IgakFC5ExZALXdxRA1wz6hqBhJs3dKfy0tvOk5mnnapKTYUhLRHu0k-EBkyulyS2sXwW-AZj24B_GlDpATnyktptOE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ca9b32ea.mp4?token=dG3dF5OyYUwQeNKBeBE2BsMi9OVNIscDwwzZl0Vif4es3sg1dUxHqqIWHcCKv2owlhqLv9KEpK6RRzVtawX5KdOOxL_mTRkj_lGjlVwUQRIzy-scv6uEIxnvQ9XgNjcRIAetykRG0PYVYuZpyMYj7mtPWItd1slJp1JrRpNti-E0xReGjdCKf9wJN7_L37prONHEVfXhOYbxtEdvw6F9QQ6-EJvOJiiwhJrW60_9a39NSt9YrzAANd9A6r0IgakFC5ExZALXdxRA1wz6hqBhJs3dKfy0tvOk5mnnapKTYUhLRHu0k-EBkyulyS2sXwW-AZj24B_GlDpATnyktptOE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازخوانی سالگرد سفر اردیبهشتی رهبر شهید به مریوان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/435855" target="_blank">📅 10:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435854">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-EyqRNLJ6bD4EfB9t_uXUW3U8Aqjr4o9D6X2Gb_4rKcdi3e3xcv5VxCCo2ImuHFWXQDijaJwfloOhH3rluihLLFR4tMUT-dlYr5jqWjs0zr6B2-trfUi3nSQ4o6amNVI9fiIpj6HZkJUIart6NdKt4to2kx5dg8RQrGyfKU4AcZxV7u6F3MYHyLLVqn1sv0C4W1jPW7nU_QESHrvs1ABl5mFnX9oVrJhdyW5GZo7sL7cGy6e22V0QptcyS9V9k_TliZv_XN7LlzTXggEduxN7P5HEeIubp1S8jvhPA_sJZEV2zALf9C-7PwbwxUkSdxlEhIOGIt7RE42hwSolfISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌ رایگان‌بودن مترو و اتوبوس تا ۲۷ اردیبهشت تمدید شد
🔹
شهردار تهران: خدمات رایگان مترو و اتوبوس تا ۲۷ اردیبهشت تمدید شد و تصمیم‌گیری نهایی به‌زودی در شورای شهر انجام می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/435854" target="_blank">📅 10:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdee230e76.mp4?token=giD0BI7l8t0X27kdb12RUTAZW5jGcjz7IpUwNPadbCYGyD1PW0Vj_Y0r2LmxXfXk1iMS0O9DpFgueEzNNO82Fl_qXWg61Mf-Zv0Q_9_dwVWW1o4V3byv8BxjlUciX9c9vBLjPmQvCU83g2gdkRoHDNS-x0nfJlhtAkCzdy_L1xEbz6R7UGp7J9Sd7Ho8T-pNdloGq3T_UNxjYXesypAn5Ki1Fo1B1XcAuAvh0LFNUk0CsIBgMX5ASuveUG4TyZUCaxrGmWxB151ljSMuyPjtgXAfnKQooAMmDys5ld3HkvNJ5PgenxJ5fvZhtUTMxG6crtNw2l-div462ljk12ukzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdee230e76.mp4?token=giD0BI7l8t0X27kdb12RUTAZW5jGcjz7IpUwNPadbCYGyD1PW0Vj_Y0r2LmxXfXk1iMS0O9DpFgueEzNNO82Fl_qXWg61Mf-Zv0Q_9_dwVWW1o4V3byv8BxjlUciX9c9vBLjPmQvCU83g2gdkRoHDNS-x0nfJlhtAkCzdy_L1xEbz6R7UGp7J9Sd7Ho8T-pNdloGq3T_UNxjYXesypAn5Ki1Fo1B1XcAuAvh0LFNUk0CsIBgMX5ASuveUG4TyZUCaxrGmWxB151ljSMuyPjtgXAfnKQooAMmDys5ld3HkvNJ5PgenxJ5fvZhtUTMxG6crtNw2l-div462ljk12ukzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهلوی‌چی‌ها به خودی می‌زنند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/435852" target="_blank">📅 09:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فراخوان مشمولان متولد ۱۳۵۵ تا ۱۳۸۷ برای تعیین‌تکلیف سربازی
🔹
سازمان وظیفهٔ عمومی فراجا اعلام کرد: همهٔ مشمولان غایب و غیرغایب متولد سال‌های ۱۳۵۵تا ۱۳۸۷ باید خدمت وضعیت خدمتی خود را تعیین‌تکلیف کنند و مشمولانی که در مهلت تعیین‌شده وضعیت خود را مشخص نکنند، وارد غیبت می‌شوند و با محرومیت‌های اجتماعی مواجه خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/435851" target="_blank">📅 09:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435850">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgyuB9av5mC0hPX9bZJOst-GRl0NOCaa7UPabTjlI6RLQ0iBAPkxuEAurLlx2fE3BAVQ3wV5VWbKFdCvpL1sKQu8BgBqFnA1Zw6fzjxTUUBGjTmhq5lSQQu4SNdsYmrcFDfKgbcB8pj5qNAOh9oFljGkG6K_FHyZTD8UsgYDQ8cSd1rHT3ZyTFHlPJkhVKm-mMcdA7EnubvR0ARbgoptVnm7Bz28QO_opcPKxIWUJj0Aer0U-c-XnGclMHLDu_J7lIj7NjBk5wVNx-zxKcKtI6mhAP7eiDl4G7fxr-6l3kE6QSH3_4QgsQSvxJVc_GS6pU7jI_h00EybCdglG2hV3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رهبر کاتولیک‌های جهان: تهدیدها علیه ایران به‌هیچ‌وجه پذیرفتنی نیست
🔹
پاپ لئو: حمله به زیرساخت‌های غیرنظامی برخلاف قوانین بین‌المللی است. تهدیدها علیه ایران به‌هیچ‌وجه پذیرفتنی نیست.
🔹
مردم همواره به دنبال صلح باشند و نه خشونت؛ و جنگ را طرد کنند؛ به‌ویژه…</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/435850" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc2eb23cc.mp4?token=MF6sHy1LRolEjKnw955xvNFNs1NtGv_6PPceln7i1TU-zLeaacDxTSBgsWncgfQKkx6HGh5ijBOxIeiAhXiDXgKpxuLawtEdRudCAAwil8TffGaWE7bzcVgIiCkTDF3AHnq3MFBOGv29x5wtkQDS_UxZGp7lWv-z_gGasvdSSR7G5vil2M16EbONOFxU4psqXeMrLqzttvveggceeJkGgr41UJ04aF35anAzea5zW9Zm8z4vbNz9HVzrb4C9i1dDIhsF7RKoN28wF4zQF3chnaiYIGhsQ7nRgyEN9tFZOc7WryUZkRQ8jxz6vTQTNsYC7PAUw53ZICZycGCPvx_zFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc2eb23cc.mp4?token=MF6sHy1LRolEjKnw955xvNFNs1NtGv_6PPceln7i1TU-zLeaacDxTSBgsWncgfQKkx6HGh5ijBOxIeiAhXiDXgKpxuLawtEdRudCAAwil8TffGaWE7bzcVgIiCkTDF3AHnq3MFBOGv29x5wtkQDS_UxZGp7lWv-z_gGasvdSSR7G5vil2M16EbONOFxU4psqXeMrLqzttvveggceeJkGgr41UJ04aF35anAzea5zW9Zm8z4vbNz9HVzrb4C9i1dDIhsF7RKoN28wF4zQF3chnaiYIGhsQ7nRgyEN9tFZOc7WryUZkRQ8jxz6vTQTNsYC7PAUw53ZICZycGCPvx_zFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ خواننده سیاسیِ منفور به محسن چاووشیِ وطن‌پرست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/435849" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUV8bvEtH654Ig0YVzeQhMUzwNZyZfcICwCCBYGIFyaXZdntiI4BN4FEJvhdstqLNvCaDJt5vZjV8GeILgNBOSjOu2QwmynLKpJgtxa8ORH0o-jRHE240NA1dZxM5h0L_nNWXRRgz9uv0z6E1IjwRxTrBtwcJz2tco29g7KHtRwWlp5Qc15ZYgMGJoTfbr__Sit7SsVmLnxKwxTLIcoBiwpHgfdl471emenUJyXoEab9fcinlv6a0j66LHGqpcr4lmEKceo-vtWV95Tar-iPnWLomZCbmW_GMZCLNabJxOtdureY22CfqJYgV_yxWvIBxpzzFOsSFGBfupFqs5JeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مدعی کشتن مرد شماره ۲ داعش شد
🔹
رئیس‌جمهور آمریکا، بامداد امروز از کشته شدن فعال‌ترین تروریست جهان به نام «ابوبلال المینوکی»، نفر دوم داعش در سطح بین‌المللی، خبر داد.
🔹
ترامپ در پیام خود مدعی شد که این عملیات به فرمان مستقیم او و با مشارکت «نیروهای دلاور آمریکایی و نیروهای مسلح نیجریه» انجام شده است.
🔹
رئیس‌جمهور آمریکا در ادامه بار دیگر با تلاش برای پررنگ کردن نقش آمریکا در این عملیات نوشت که که المینوکی گمان می‌کرده می‌تواند در آفریقا پنهان شود، اما از وجود منابع اطلاعاتی آمریکا که تمام تحرکات او را زیر نظر داشتند، بی‌خبر بوده است. ترامپ در این باره نوشت: «نمی‌دانست که ما منابعی داریم که ما را در جریان کارهایش نگه می‌داشتند.»
🔹
ترامپ در پایان پیام خود از همکاری دولت نیجریه در این عملیات قدردانی کرد و نوشت: «از دولت نیجریه برای همکاری شما در این عملیات سپاسگزارم. خداوند آمریکا را حفظ کند!»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/435848" target="_blank">📅 09:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emRk2FVFekZ4mIG-Q9AFvi8gqbjlE23W5SQIePkYz-41lFfYc20f3d9DxfwdNhUCfPbqem4fV3htIH6wl-cJmtGH3N4nZmr5m67Sp9RMx-TE7EPgjN99QBPX-T4TZ2YPIOq3tzkB1xT2dCXOQFeb7B6JVgW1rofU6KqP3kb7AstLggMK1HeBaFT7s2EmoZq2ASlgBJbFc19WN6bH3qdOVL4ZasyV-Rgx_zQNSPln4y7YCNi6IN8nZ4zB5xXYM196c7v4D8kPOXFIvziAeGDRyaxM5827-yVsxOgb9oFYoyqT0zR0m6CLxdZsGc6Qo0Iw_G4-vFTtSjr83aI9iUq9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز نمایشگاه مجازی کتاب از ساعت ۱۰ صبح
🔹
نمایشگاه مجازی کتاب تهران امروز از ساعت ۱۰ صبح در سامانهٔ
book.icfi.ir
آغازبه‌کار می‌کند.
🔹
نمایشگاه به مدت یک هفته برقرار است و کتاب‌ها در این دوره با ۲۵٪ تخفیف و ارسال رایگان فروخته خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/435847" target="_blank">📅 08:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGUDoTZGzRhdvhe0YICb6AYsd91C4f7e6FKEhDNMdQL_3YH9ndxvd7hSSmpdsAV4oeIjvrTgyIHIWghigqk9ywGZQSItAHT9m15n2mO-1ZJVKOCDXeyJmS6EO5nDuyeU7AubzHZmmwamN3EibIs8iJiMWPk4jtwRV-GG5No_Cm5XCQ5UoCBFa7ybhX0ilR8iYxasO_S6g0FNXFECNPABJGVcumAKunuKFdV9MRY_zycXcaL438FAm9ZGT0cJb2ZLCgq4mR4V-eJbRcLt0QEtKoWD90zTAsAyTY7lUyysJdgNq_dJ8fz8DQqDBNFsyku78mrDvx31H07J6uzIGvVMwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی، هدیۀ چینی‌ها را دور ریخت
🔹
خبرنگار نیویورک‌تایمز گزارش داد کلیۀ اعضای هیئت آمریکایی پیش از سوارشدن به هواپیما برای ترک چین، تک‌تک اقلامی را که چینی‌ها در اختیارشان گذاشته بودند، دور انداختند.
🔹
هدیه‌ها، نشان‌ها، سنجاق‌ها و اشیای یادبود همگی در همان محل درون یک سطل زباله ریخته شدند.
🔹
به‌گفتهٔ این خبرنگار، هیچ اقلامی با منشأ چینی اجازه ورود به هواپیما را نداشت.
🔹
این احتیاط‌ها تنها به زمان خروج محدود نمی‌شد؛ پیش از این نیز اعضای هیئت آمریکایی تمام وسایل الکترونیکی شخصی خود را پیش از سفر به چین در خانه گذاشته بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/435846" target="_blank">📅 08:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
تعطیلی ادارات و بانک‌های ایلام به‌دلیل گردوغبار
🔹
کارگروه اضطرار آلودگی هوای استان ایلام با توجه به تداوم گردوغبار و افزایش شاخص آلودگی، از تعطیلی تمامی دستگاه‌های اجرایی، ادارات و بانک‌های استان در روز شنبه ۲۶ اردیبهشت‌ماه خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/435845" target="_blank">📅 07:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435844">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بارش باران و رعدوبرق در ۱۴ استان
🔹
سازمان هواشناسی امروز شنبه برای تهران و ۱۳ استان واقع در نوار شمالی کشور بارش باران و رعدوبرق پیش‌بینی کرد.
🔹
در استان‌های آذربایجان شرقی، آذربایجان غربی، اردبیل، کردستان، کرمانشاه، لرستان، زنجان، قزوین، البرز، تهران، همدان، مرکزی، مازندران و گیلان در برخی ساعات بارندگی، رعدوبرق و در نقاط مستعد تگرگ پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/435844" target="_blank">📅 07:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435843">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNRTYGvz_IUnbkABTR1CqNWW_M3VstZbuwYYgvSA8-Qm7yxVpbP_1rx4iFc22NjOVI6oe75KdDJUQGTWtjmBsSNPL7DSPKm6dBsWsDkGgkkJMgJOAt7wRHlIazpPtJ7yqDQhELXnIM6MZobSgtx5yCrSdhmUwB236tiv3JchLQotMWJ4o6vF-a-puBbgyreTBqAe795i2e4JTqmcGf5voqW1x1FgFGr9tj9OKID2AxIz-ebSgHWXK8T8NJVQJYuEnKP5eSztgtPjlVmCgr-dc5t3l4MEE0m2ZKOJzmcR3erwcm2eYWNMQzqG3dnVOYoQlg6fTsABUcISjuBj_H6dsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام گمرک‌های عراق به‌روی ایران باز شد
🔹
بیش از یک ماه از محاصرۀ دریایی آمریکا می‌گذرد، تجارت ریلی ایران و چین سه برابر شده، پاکستان یک مسیر ترانزیتی جدید با ایران راه‌اندازی کرده و مجوز عبور کالاهای کشورهای ثالث از طریق خاک این کشور به مقصد ایران را می‌دهد.
🔹
حالا نخست‌وزیر عراق هم ادارۀ گمرک‌های مناطق شمالی، مرکزی، غربی، جنوبی، ادارۀ گمرک بار هوایی و گمرک فرودگاه بین‌المللی بغداد را موظف کرده تا حمل‌ونقل ترانزیت و بارگیری مجدد کالا‌ها با ایران را فعال کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/435843" target="_blank">📅 07:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435841">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMv2Aif85NoD_MOjxJgC461VVQAULvydVbG1gZWueLYs3rP0bywVK9Hslg0mSJyPAizPBstp8kk7HvW0dq1ijk2uxrveM95OCKmtl0d3K0EjTMNtA1n92eBWKFNaI27D16d1aCeoFuGZ_BycuFqTSzm_9bBoTKbbjqTbXi1qqNHYuQob-q2AKIHxvHKM9GoUX_Zv96szGrFwwHu65DirmX-NFlNopC6LcEl2Ud7tWQubbd_UhCipa_KvK7XQtRHQK4MR7BOabPxHkJqjFJjVK_hRw_EckIj_zrQ9tBfxmvLFmivWk4fx63exc9U9Y_DGozZ3diiRAc6Z4NE4q2U2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احضار غول‌های فناوری به سنا
🔹
مدیران عامل شرکت‌های بزرگ فناوری آمریکا از جمله متا، آلفابت، تیک‌تاک و اسنپ بار دیگر برای حضور در جلسه استماع سنای آمریکا درباره امنیت کودکان در فضای آنلاین احضار شدند.
🔹
این جلسه در شرایطی برگزار می‌شود که فشارها بر شرکت‌های فناوری در آمریکا به‌دلیل اتهام طراحی پلتفرم‌های اعتیادآور و آسیب‌زا برای نوجوانان افزایش یافته است. قانون‌گذاران آمریکایی طی ماه‌های اخیر بارها خواستار تصویب قوانین سخت‌گیرانه‌تر علیه شبکه‌های اجتماعی شده‌اند.
🔹
جلسه جدید سنا ادامه روندی است که از سال ۲۰۲۴ آغاز شد؛ زمانی که مدیران شبکه‌های اجتماعی برای پاسخ‌گویی درباره سوءاستفاده از کودکان و محتوای خطرناک به کنگره احضار شده بودند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/435841" target="_blank">📅 05:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435840">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🎥
روایت سخنگوی دولت سیزدهم از عصبانیت شهید رئیسی برای عدم پاسخگویی به یک دانشجو
@Farsna
-
link</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/435840" target="_blank">📅 05:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435839">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e91091688.mp4?token=fYCBPzatdaPl5O2M3iSvIdCz9Xtp30hAHm1Ep5gDU_iDs3FXo5OASViweC_ZOEvnnutUn7Zo6jgHEB7n71WyCitUTSMegv3sV6nV2UfttWZBVXxGTz8b1dz_lDRsUlqnez2fdQjs1SS5H5I637nR9wmoxxzZbasufOpXxyAXLnolHGc3RqrwivRJRJrUfng52MU9Abd1cm8uj6nxv4Fyin_iIIb7rBMKIS08stwFk3FgeBBxL7kEb--1x8RwtZxDqbIDKa1pCdeplkcF-bgLVFfpY5AQlVQlj8PhgEjOS0uBKVl3yOatuxDCKNC0ysTeZi5GSnfkWUVBmTyWiGK02w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e91091688.mp4?token=fYCBPzatdaPl5O2M3iSvIdCz9Xtp30hAHm1Ep5gDU_iDs3FXo5OASViweC_ZOEvnnutUn7Zo6jgHEB7n71WyCitUTSMegv3sV6nV2UfttWZBVXxGTz8b1dz_lDRsUlqnez2fdQjs1SS5H5I637nR9wmoxxzZbasufOpXxyAXLnolHGc3RqrwivRJRJrUfng52MU9Abd1cm8uj6nxv4Fyin_iIIb7rBMKIS08stwFk3FgeBBxL7kEb--1x8RwtZxDqbIDKa1pCdeplkcF-bgLVFfpY5AQlVQlj8PhgEjOS0uBKVl3yOatuxDCKNC0ysTeZi5GSnfkWUVBmTyWiGK02w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنگ‌تمام اردبیلی‌ها در شب هفتادوششم
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/435839" target="_blank">📅 04:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435838">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62cdb5a18d.mp4?token=FpL0lHtec5GdNvFf4XfDrNlBCEM3ypfrDozwOs22GWy60gmsksavVgn8aqpvAWYNCCrIe52jWV0lVFD0s1arptTcUX6SLkT2bMD-_Sr_2bpbg2a2fS7xzM7YD9uAK6jCyx9d3IOneBZ-zCIUmcjTN_vm2IPJovM3cym_uX-H--wa99o_QSTdDb9jTIxrC6R7NmmloCkcy4cpAi5R2lLJkEw9tiuvCx_ilaFuy_PTpov4LWWggnDhD4Q7C7WhD94j_98jnhibo7GgZzmt3tqFfbihidGjPirD_hYuOQi57bimdcDhvB1E5iCfdHtg5WLtf3nLvzMHIlYiN_XaemgEuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62cdb5a18d.mp4?token=FpL0lHtec5GdNvFf4XfDrNlBCEM3ypfrDozwOs22GWy60gmsksavVgn8aqpvAWYNCCrIe52jWV0lVFD0s1arptTcUX6SLkT2bMD-_Sr_2bpbg2a2fS7xzM7YD9uAK6jCyx9d3IOneBZ-zCIUmcjTN_vm2IPJovM3cym_uX-H--wa99o_QSTdDb9jTIxrC6R7NmmloCkcy4cpAi5R2lLJkEw9tiuvCx_ilaFuy_PTpov4LWWggnDhD4Q7C7WhD94j_98jnhibo7GgZzmt3tqFfbihidGjPirD_hYuOQi57bimdcDhvB1E5iCfdHtg5WLtf3nLvzMHIlYiN_XaemgEuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نسل زِدی‌های جهادی!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/435838" target="_blank">📅 04:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435837">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyAGcxUpPR8IPLb1_y707YpdNmd0GGlgMyQIbBZ4TahTsdQkKNqGzpDnBqrW9wjx4jaevi6P8PtBV0XB8uUZvjyUFmmRq4W1cSnXZG9kioB8W9avoW4ZNHCdyt6f8q1OOwjW3-4S4DlGjHmfArUgBzrYDWcEiJnll9sLtPjk4LqoKjQCIAVEIs8v5UjXgA25VG9KU3Va1Ki8m9pGmHBkTbdD-1nc2O-Qj4BfVb9lbbNmYKX_KVUSdc1ACRczZI8Ce-KKUaWIW6QxD_UCxN8fh1L3Hjfin1gruzOHrQQS_NigdKIfcSEMG0JHdnLd1gopjMif89Q840qZgxbhDNrtSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز بنزین هند را گران کرد
🔹
در پی جهش قیمت جهانی نفت و تشدید بحران انرژی ناشی از ناامنی در تنگۀ هرمز، هند برای نخستین‌بار طی چهار سال اخیر قیمت بنزین و گازوئیل را افزایش داد؛ اقدامی که از تشدید فشار اقتصادی بر سومین واردکنندۀ بزرگ نفت جهان حکایت دارد.
🔹
در همین حال، نخست‌وزیر هند طی روزهای اخیر به‌صورت بی‌سابقه از مردم خواسته مصرف سوخت را کاهش دهند، سفرهای غیرضروری را محدود کنند و استفاده از حمل‌ونقل عمومی را افزایش دهند.
🔹
رسانه‌های هندی این اقدامات را بخشی از برنامۀ اضطراری دولت برای مقابله با تبعات بحران انرژی توصیف کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/435837" target="_blank">📅 03:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435827">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTJ4F72Y2xYZuB2GrsbSOPGKXfCQD4TagWw3Ty5nFn1j68QB1q6ybL9qQi0vnfroXLNolb_m8Coe_2XRvx6X8ZTE_fSWnEQappmtjDEmPvRqE-Wt1zCUTnYjWA74A5e-xnG6o3zuVeMF72hnLc1l6Y6tikm3pGUpOq2GQ-Udf9nMKQTKDRUR0jdVeaKTiwOiH5ljoAfSL4KTa0DgcFQKrVqThrZwFccyEzLN3b9SJrdaB0yas1C1axe0nwcaVK-mPXI9T3dPnJhwR9yEuHEf4_NWeyq9ilQBxYQLOK7cRM33i7etVikzKJWR6UsvlFtpMz891vgR5e2ZGZ4L1NmqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vos-dMWxwm7Z4uIorNYfHaJPw3ZEHpKQiDpW6Ybwu1IuSt-EI8uP734-qeXQzQ9iynZUvoMbCNS9oYmGKueIWz3Gy1EGg91o-5g4xMuAgBWlNg7HoJ_ahG7KZo47eK_8uuBGOMet4lG8QXv-Rl8NJ9hNNtjlNT0q-AAMXQC7-TRhtTGiUsD4yIiqIVc8C7zs69qsWPSdSUjI8ZSqYEztdS2VZAGrkKUwU8WFDTlJua2wQyLQqRqTioyVJLffRM2oqBJKub2VIc7cs8MLW0msFB5NWbUknkPKBtUWUNkaaUh53hfdbPzROMhI_QefKNfj2awb1FlDQo8gYIxI_wxDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLor9dgaohtFnU1uddmlYdKAJx9OdQJbRqgxwkKshGjy5-bT3uDj9Di6C3WeaziIGm7OsOKMT94a8hIML2ac89vHEoZG9OevmhqaFA7Ln7FXv8BaDE-STjwd1DockyBciuUa8bBzlapEtA_kFMkzGeoGCVXF9TmN_Effs2JFyUNnV2wZr3dlGdENtQmzXwtWS_ZWDePfCJ4Quyvnq_ERF2PPlid3lyBARllXURdaJKGjN1aZNDkS1UGRs3ScZuB5kKgb7nzGkjGoKR3HgM2UiugbqGhC5FGsecB0jidTlABciDtBs_97U-AejyT1hk5JblxtyPhsHK5pzkEEgK-Q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hiYDUNifR4xPsvSobXkWLd67uJcrMBS91nbL4VtdFotHEcDwBTYl0hmoS_SKCXTV0ViNCmOiQDzVLj9VMONjdL0BaRehFVtTOBRWGFp3pRbSmJwEhu1DjLXlB-l5CQZw21jUedeDI79xX2qr2StqZmXTX-Ltvehw5prPpoDZIg69hf3Nty6gMNohLQNoG3IpK2bhgLz4C6SsGb1fBtkhwNfQoufSEALLKTzQYfGfZpjEX6PaIJfbw53cNaeRkiYjj1Wn7ZZ7QFkkeZ0ZP_39lgYE_jGEmmbXI-QzaDlPOYmkFeyB6iPedYO7-VzTJ00bzikLwp4Qy6tSXpHogEhOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avefFjs__jFGfZDXUSYm7UDKsbdqDa_zr00-4Z_56wk46WkommUdoDyZCtW-eMcHFzXD9zNbMt8l3e7UQl_b8J3BBMvB7Ce3tgWSQrmNqtP3Y1fK5r46fuh4qUw_uVGspE3i-NS9pByDVV_X6g_BDMMnnQoHF_g6MdqXx2GyUy59X8VMkW_I-72Ybs8SQQGHmdZbTFNux7JA65lWAJjOT5zJQk2EeEraPJnQjdH0qsP36jlY_FYQKZQ5mQ6g6dZRLP_ZPGufsOsEIJG-MhoKwt5IhcJIYw5oDzS6065hAoI5cSGLceZzzVSvFmVM67EhohyBizRmKfU-ptDDcVo41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cECzrXsBHWPvLTCXiJYZyA1ha_QY57S7POLC8cLm_LY2o7OIKfzUajv4gT4l3rgO1-x7RCFrIY7u3hOEPSMBNFcJX_4XSNmvT4OMBznhR414ZcySXku13UaYKUOC3QJ5AkTOCXo_AFGFFdP3Vn-5qiQKnyLT2XJmBKtevgrasIvcWsVYDoKrTlDes6rUpVm6OA-L1OptTpOw250Ayl8w-YZmfkYZgMOUupeuN9TWkDrT0fvmAoHi_FUYfBHy9Cuj6pTaW2Y5KODgAhMpQ9xzc3QkfYVsx8H-ianmTWq6zNQGrs1lTY3fI7fD3qEMyO1CVBzEPZXtOup4st-msOw7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQhz555ID3L6rJINHcdMQ6Tc3SJtwVMSzojAkCLypK3GBkZ0siiGh-3D-cqHt8nBfYiJQp-N7pfZnSvUFltc5S6WNR458Eguv_yRmGpcBt4VoCARfMhkikow4RiS0hdrio1GJQ7OUAvLqcdRmrm6dfgsI5LuVUe2v_EMk3tzmKoZvsAHuK93q_g80TCSXusCW7JkKXKgMus_k4bwWHozVraoyd8_3sC7Lkn_8gczqf0ifKcVJyw4OuQJV2vVT5YtwKYc20wcUR_6J-xnC4NRhXCyV0M5ayINvO7KlMO69jRdqP62jDkxILcacoJdyFdMk_jBUpdvv9U5YJ6Tlw0iNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AySCZLkDZll8ZOG48FB7kx175VeRwWH7GylWi1_o9D96f9XC_yB7wlu2Avb3MwJ0eRlXIG4srHl5YWMVF5fyFIG9Dzw_F9RCFE_waZsQZeeOjcd0mY5jqi37-ukcTWZa3gaBA86AWiubypi-BBdMereuNF10_nRr8r7bKnbuVZCTNGpqcdOqsntVj-tvY1iokEk48uUyJ4ahFMlB-8iDAXYOe_heSS5nhUgyDyWAFRd7oQmHYOAVEhir70anA8tATu7E2rxrsjh5tu_20dYYpkFxiUzjK8btD-24GZ5DvQp0W9j25jBO97dRr3HweE9FqC4yQU2EBY-7WcL6OpEGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pk-eR_1P8DF_RqlubdkZmO_bg_669Ez1JKZbPhz0aE2wQGXstc-7VYc0huzs5MhqtCkWgznAL39RlxBQsQPN-pHkSeP-Yqa1BDDWRjvHCR_Ti-Prq-7PbxwSvLQILd4h5wyyrqFYic9U-DSm-EaGhdsjRH9K_1lzLtiYgDE_Wz7_BXciDwxg1uIdhNlV_0j3-_oM34mdLkjIN6GtTfM73Of1hUZXPfeZXoKwVZF0Z2NDSFy6Ola-yob4MFHrsjjf2X8p1VSeQ_wcgyyCsnNG4ECNAcdV5F1QgITPkrR1_8C_xUCODhs6S7-kUkaOmEHGRMF0mDfRJT8c2E_N4d2E9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQ0ozhdzT20tilVDLaUg0suZ4Dd7I7vvEwwLk3nGvTqh-N4TEzDeWoCJTSIIBESF6dNtBgKGIWos_2EyEwsxDnWWfZ1eseMMl-cV69ELdnc7DShZ4TQefpHxBnCvihN1esVS1SHHq5ZrnDAKWhzn5OOWy2ywH03x_Ai6PbBoFukxWKKz1m-5IAUZ6ptpnsKsOBHlGiH1n2ntwb8e3NIL9UWdBMKFnSOJcXgumSzTzb7DsKYMboTXDJKVfr_twPcLipwFMq8BvqmGJzN2ypkJ9ZnwiqIOm8alh2CBEpdVOhcgfa-YWJeDKFy5t4YgGbX8jNWxIMnLJqi9rSvQzQHU0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن تکلیف دختران تهرانی در میدانِ دفاع ملی
🔹
جشن تشرف (تکلیف) دختران تهرانی در هفتادوششمین شب حماسه‌آفرینی در میدان جهاد برگزار شد.
عکاس:
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/435827" target="_blank">📅 03:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435826">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baab29a915.mp4?token=CMzv4r41SyGU6HQcuLiIwOX39R_0dg2665an2QcVPpLubxY07QCo4R17jkeScdW4uGzSx1O-0KDRg6oxYfHhi8oitG0rhEEQGDH8VCwRKaA0fhIhAC2zjlZgUjaunfUnnxk-Skq3BLNaVyKhNN-2jOm3q3GXHQzkVmUzKi1zsq7cra87BWVlEZ-CPMVFxu_oMXW0liQNLCAG56rUdGzPY8TkeHdtxCXZ8s-L2qKo61Rx6ec_MynbfSY7wdmCvSh_T57Wc3fAufL9j6y70-rb5WUh5nO1yOHxzVSu6GZaSHMDHztd3D1qNqzYFulMV4NECmTXqfnROizc_phkIH3Bbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baab29a915.mp4?token=CMzv4r41SyGU6HQcuLiIwOX39R_0dg2665an2QcVPpLubxY07QCo4R17jkeScdW4uGzSx1O-0KDRg6oxYfHhi8oitG0rhEEQGDH8VCwRKaA0fhIhAC2zjlZgUjaunfUnnxk-Skq3BLNaVyKhNN-2jOm3q3GXHQzkVmUzKi1zsq7cra87BWVlEZ-CPMVFxu_oMXW0liQNLCAG56rUdGzPY8TkeHdtxCXZ8s-L2qKo61Rx6ec_MynbfSY7wdmCvSh_T57Wc3fAufL9j6y70-rb5WUh5nO1yOHxzVSu6GZaSHMDHztd3D1qNqzYFulMV4NECmTXqfnROizc_phkIH3Bbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هفتادوششمین شب حماسه‌آفرینی قمی‌ها در میدان خیابان
@Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/435826" target="_blank">📅 02:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435825">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6Fu5Q5NJ0eY4ffM5ZL8QMh2Iwe7qM4FxhFcocYA--hPtqsy4wtzn9KeHDltNzhBLgc6CqhY7AmepT4BJMcQhUHy8XeX_TsmYuNALGbW9qKqbOyAj8yAjKt0-hieYwuLxvVv9AgMNGJnpjh_MtIQ8slfUNkngf5a8CIF7GVtiXCtjICVtsuLlJ9lwj9nsehB31ZjOv9rnXa5WjKbmSAZNnFYmMF0eHCK-XQJlLxhD4ihZMTKPZtaiq_VAael3FEi3ruJ0nGZ4ZQQ6SmYRGwMSujHXRNgTCu_sGJ3HT2yLhitXxDoMrREEuZhm8T__a1zZgf6ALaije2uU4Z7rj7qYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب‌نشینی ایلان ماسک مقابل انگلیس
🔹
شبکۀ اجتماعی ایکس متعلق به ایلان ماسک، با انگلیس به توافق رسیده تا نظارت بر محتوای نفرت‌پراکن و مرتبط با گروه‌های افراطی را افزایش دهد.
🔹
ایکس متعهد شده گزارش‌های مربوط به محتوای نفرت‌پراکن یا تروریستی را به‌طور میانگین ظرف ۲۴ ساعت بررسی کند و حداقل ۸۵ درصد محتوای گزارش‌شده را طی ۴۸ ساعت ارزیابی کند.
🔹
این اقدام در حالی انجام می‌شود که دولت انگلیس طی سال‌های اخیر قوانین سخت‌گیرانه‌تری برای کنترل محتوای آنلاین تصویب کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/435825" target="_blank">📅 02:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435824">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc9a447c75.mp4?token=EH-51Cg-VWABvf_EC3wWhhSa7hfOVoujDMkaNTOs3fF9yAI2OjO-PVGMbxN6wDJ90mdZZKxWEghVUV2M3eoYDLpDUGVLfy_E7XkW3Bq6L7NvWejYX90iywgwTXBHTXovQCEptS9Q-_7Vu1cViPObOLcQLigSMtGZm7XLWciJfUh3jZ9FmBIbS3d8NDnJBc6VRJGOjBnzQtVX2nKkKagBOOsnkn-CPt6Rj6dq5PpPBtiRTDEDSypKDtj-o8cibeMfgcfoa8jq35Iv9OYV5hqH5wR7SQzVKD7a_n79zYFgwPjum_B3Ftr1ysqgne9kOr1Wdt6syfaiAj_8LZhdQTKjbjL1sh6Xbtkxxcd4_PeGmGp3uAJUUvCao7xw_OS1y0kZRvwAYOf9Rw0TWlK5EVZQmXwGaaxwpzZjzR5TwYWltlcOtjCK9sbVU7fJNQtrCtXHxg8Ula_K-QbVBhXR2T3N3bjmQVCJvPyg_5HLLLxDSJ2Ecu5V0p1z3I5Z7h_C537twLmLNs-xaagS9YwepC4M6Elh5AZ_5xQ26htJy6WpKYdhcxRxeXE1rAg4WEGox_uZpuB0q8FE5sbZKDbvnWQkWn-H1liqhbhjGGHsCfp7Gn3XNZXre08hPr2jnapfwF1198gtINvq9vT2wnmTrKD1B3zAiiKLTFujtZy-CBF60qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc9a447c75.mp4?token=EH-51Cg-VWABvf_EC3wWhhSa7hfOVoujDMkaNTOs3fF9yAI2OjO-PVGMbxN6wDJ90mdZZKxWEghVUV2M3eoYDLpDUGVLfy_E7XkW3Bq6L7NvWejYX90iywgwTXBHTXovQCEptS9Q-_7Vu1cViPObOLcQLigSMtGZm7XLWciJfUh3jZ9FmBIbS3d8NDnJBc6VRJGOjBnzQtVX2nKkKagBOOsnkn-CPt6Rj6dq5PpPBtiRTDEDSypKDtj-o8cibeMfgcfoa8jq35Iv9OYV5hqH5wR7SQzVKD7a_n79zYFgwPjum_B3Ftr1ysqgne9kOr1Wdt6syfaiAj_8LZhdQTKjbjL1sh6Xbtkxxcd4_PeGmGp3uAJUUvCao7xw_OS1y0kZRvwAYOf9Rw0TWlK5EVZQmXwGaaxwpzZjzR5TwYWltlcOtjCK9sbVU7fJNQtrCtXHxg8Ula_K-QbVBhXR2T3N3bjmQVCJvPyg_5HLLLxDSJ2Ecu5V0p1z3I5Z7h_C537twLmLNs-xaagS9YwepC4M6Elh5AZ_5xQ26htJy6WpKYdhcxRxeXE1rAg4WEGox_uZpuB0q8FE5sbZKDbvnWQkWn-H1liqhbhjGGHsCfp7Gn3XNZXre08hPr2jnapfwF1198gtINvq9vT2wnmTrKD1B3zAiiKLTFujtZy-CBF60qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج هفتادوششم دفاع ملی در رفسنجان
@Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/435824" target="_blank">📅 02:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435823">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تداوم بازداشت ۴۱ عالم شیعی در زندان‌های بحرین
🔹
جمعیت وفاق ملی اسلامی بحرین: از زمان قطع ارتباط با ۴۱ عالم شیعی بازداشت‌شده بیش از ۷۲ ساعت می‌گذرد؛ امری که نشانگر ادامه جنگ سیستماتیک علیه شیعیان در بحرین است.
🔹
رژیم بحرین همچنین ۱۰ شهروند را در پرونده‌های…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/435823" target="_blank">📅 02:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435822">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPElXj-inazforfQcM0uyY67zYGSCJapYunhQqyl8R-JJfm9VPIZmmlJ8lJMDlNjIRqg3tkkjLH-O8pz5QUEhChtaaXP8uphmAU3oE5ry9whS-ga_8iDuHZGAHjZbO0kuqGVY3KEIUSAALcavtr6CVrcI16NkAU88JW235pSo216y7nAMEQX04x9FlwybrfTbEDxl6EkkqphjSPPPkeaiL1xYtqxWbSLrfmoV1tp6UqUB8Ivb5BIvytzaRrHJELYGHE85dCoikt7RhRU5KN7tSFmCfedO6x_3gtrPIeKs6N1TqAM-CYjuPTEStSHW4ZgTnrGGmHom-X28cubGb2Kxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین از قطعنامۀ پیشنهادی آمریکا و بحرین درباره تنگۀ هرمز انتقاد کرد
سفیر چین در سازمان ملل از پیش‌نویس قطعنامۀ پیشنهادی آمریکا و بحرین دربارۀ تنگۀ هرمز انتقاد و تاکید کرد که محتوا و زمان آن مناسب نیست و تصویب آن کمک‌کننده نخواهد بود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/435822" target="_blank">📅 01:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435821">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8920b53738.mp4?token=A9BojfFmUsLgn0LyxmbgVG35FzO_fnM65EzbVVbRH-4DMl4XWk-Gv2xVGC0MUaCQX8wXPrYL-IePDODx76pwJj_z5VCsTmjXcVEE3r1HsOGk85BksP62EZ8jOFEUrTADAz3UnVFJtEvkuYa_c_LQwVWQjzkH3FYiw08z6WNcNdScls0r5J2OzR5XqLzjJFS3VKg2ORDElMAICEz_9h0gFnWe_saAQmNeqfb3crnXohPoU1xXywWZQJjjuH8Y8sJAcb8FNVjl_sIHy0D3CuDHhpcQ1xHTp0lrewHIW250DMn94nOMaKwWoVi5YsIbjRjrgoj1qWuiZYQJpWTZ7pKKhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8920b53738.mp4?token=A9BojfFmUsLgn0LyxmbgVG35FzO_fnM65EzbVVbRH-4DMl4XWk-Gv2xVGC0MUaCQX8wXPrYL-IePDODx76pwJj_z5VCsTmjXcVEE3r1HsOGk85BksP62EZ8jOFEUrTADAz3UnVFJtEvkuYa_c_LQwVWQjzkH3FYiw08z6WNcNdScls0r5J2OzR5XqLzjJFS3VKg2ORDElMAICEz_9h0gFnWe_saAQmNeqfb3crnXohPoU1xXywWZQJjjuH8Y8sJAcb8FNVjl_sIHy0D3CuDHhpcQ1xHTp0lrewHIW250DMn94nOMaKwWoVi5YsIbjRjrgoj1qWuiZYQJpWTZ7pKKhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایلام خیابان را به میدان اقتدار تبدیل کردند
@Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/435821" target="_blank">📅 01:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435820">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fin4UTIaEU-hanZG6pvix8IJhoPby7d4-f2Mogp4YzH6Nkzq396z3w_rMic8eDFSOn_ioExrWBobOdAqUGavGoOXE7KWfbZGKurvFSyljz1zDjCJyp3pGIVFt8H1GHWq7MfPZc7V_hecdq_vtP9mM_8tosIsjuhYw-UY-BCEUnIK2KZ9uNXbwXPsaGiA-3ZN0xcUZ_kJ9JbQ9uZqLjSJp41D7hv2xp1qQkNsi8fbdamEYzgiCITSswyGlG7hbuT2l0nAmsRibp04c4SWMxDS5MWNHOtZ4NOxIIXUnG1Pge2xsqjr2qiGeAKaSthAizSso5qSaY6mtHn2tvRWx1vH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسته بودن تنگۀ هرمز برق کوبا را قطع کرد
🔹
صدها نفر از مردم کوبا با حضور در خیابان‌ها و روشن کردن آتش نسبت به قطعی گسترده و سراسری برق تجمع اعتراضی برپا کردند.
🔹
کمبود سوخت عامل اصلی قطعی برق در کوباست که به خاطر جنگ آمریکا و اسرائیل علیه ایران تشدید شده است.
🔹
وزیر انرژی کوبا می‌گوید، ذخایر سوختی که روسیه به این کشور اهدا کرده بود تمام شده است. وی آمریکا را به خاطر بسته ماندن تنگۀ هرمز سرزنش و تاکید کرد که قطع جریان نفت ضررهای زیادی به کوبا وارد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/435820" target="_blank">📅 01:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435819">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rktGFbw1C6weWAq3kvvV1Vbq0UwHPFMBoGwQf8f5wHvwd2_lHDTWxzAqiW9YbCFwAT8DYatzmX2tLz7c1H3hpzHM7rr2AYFHB2gBzYXTAxacpKqQtGlefOHPURGAWrobRivPvfiz-s8zyJk_mjzBvvCgNDQTLe_rqihrBHJo0jPWA4yvglBMgk91pxVFJdprXR_hyZhQwBvl86ZsjvAL9XHSfMXTHpUTuSyrrL9KdbRpB57P2RNaGJ3KcYsci75PYej7ec4dvtAzH3XuMB2wI7uRXQmARBeAsnQvYkG9dNSA2iLVR4_RY77peWtNbYOm4O8YVMWjrOElo7CBRxpzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز یک قرار تازه برای تعیین تکلیف امتحانات نهایی!
🔹
سخنگوی آموزش‌وپرورش روز گذشته اعلام کرد که «تا پایان تیرماه صبر می‌کنیم و اگر امکان برگزاری آزمون نهایی فراهم شود، انجام می‌دهیم». تاریخی که تاکنون چندین بار تغییر کرده است.
🔹
اولین‌بار سخنگوی آموزش‌وپرورش دو هفتۀ پیش در حاشیۀ نشست خبری‌اش زمان تعیین تکلیف امتحانات نهایی را نیمۀ مرداد ذکر کرد، اما سه روز پیش وزیر آموزش‌وپرورش، این تاریخ را نیمۀ تیرماه عنوان کرد و حالا سخنگو، پانزده روز به آن اضافه کرده است.
🔸
دانش‌آموزان می‌گویند که در این شرایط بلاتکلیف هستند اما مسئولان آموزش‌وپرورش به جای توضیح دربارۀ تغییر تاریخ‌ها، می‌گویند که دانش‌آموزان به جای نگرانی، درس‌هایشان را مطالعه کنند تا زمان امتحانات اطلاع‌رسانی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/435819" target="_blank">📅 01:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435818">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ff319359.mp4?token=XO1OducE_bBz9gme5wOqObEXiYnzaRGSXrtkE8hGteO_FGRcg5jNmrEwYja5MZ-2uT4ZpPPS4-72rgrLUkzTONnUT6IhiRcb9-YNJbOX_BXiT1lZccQLiEO0LThTfBgYnBs607PFKrkNUPn6JXwtd1I4opy7XwuMSjE-ZP81U_9nyW9CaoI9LIxJ55uGMM2AWO19jsHDMRdLyz_1V7XytHUjXZcX2bWlpa8RcBW0bGgJd26heozZ1LEzxE0_eCqYVCNAdN8DnTi0a4HQcKalpsC5DYQzf40c08cHxv6KADShZUPtiaWgryMA-a6sJeyqum9bwi52R2IQeQUV67UZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ff319359.mp4?token=XO1OducE_bBz9gme5wOqObEXiYnzaRGSXrtkE8hGteO_FGRcg5jNmrEwYja5MZ-2uT4ZpPPS4-72rgrLUkzTONnUT6IhiRcb9-YNJbOX_BXiT1lZccQLiEO0LThTfBgYnBs607PFKrkNUPn6JXwtd1I4opy7XwuMSjE-ZP81U_9nyW9CaoI9LIxJ55uGMM2AWO19jsHDMRdLyz_1V7XytHUjXZcX2bWlpa8RcBW0bGgJd26heozZ1LEzxE0_eCqYVCNAdN8DnTi0a4HQcKalpsC5DYQzf40c08cHxv6KADShZUPtiaWgryMA-a6sJeyqum9bwi52R2IQeQUV67UZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور خانم مجری شبکه سه با اسلحه روی آنتن زنده تلویزیون
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/435818" target="_blank">📅 00:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435816">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎥
پاکدشتی‌ها: حتی در سخت‌ترین شرایط به آمریکا اعتماد نمی‌کنیم
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/435816" target="_blank">📅 00:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435815">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhfe7XIzst-eMOjIxY0hz31czPyp3waMMazChk6Bomlr8ug5J0ELQEa1FBgTmRkO2Wylb8FhglMuXZ7B-atD55i0kJypl-u1XZYuGMx9RcKK-LabiVsjPh3j5Drj9DKJfXHAMQELaJxW45IGq0ubRQWnwtTZ8hnKsMwikbRECzYknyMl0L_XjGebHdO3DEd7TXtOQSxtT5vvskkCYN5SylruFN_Y1OGnQs-tnvmJa7nlJFukL89PuGRoXxKnXYosVveu47E8B-ScLUVaMMLDP0KAWiocsEbp4cd-rx9k3QJkh3SGRr7_XlNOJ0kNwJSKUGzR_AKaDXFJu5JTL1XUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش عراقچی به تبعات جنگ ایران بر اقتصاد امریکا
🔹
به آمریکایی‌ها گفته می‌شود که باید هزینه‌های سرسام‌آور جنگِ انتخابی علیه ایران را بپردازند.
🔹
فعلاً افزایش قیمت بنزین و حباب بازار سهام را کنار بگذارید.
🔹
درد واقعی زمانی آغاز می‌شود که بدهی آمریکا و نرخ وام‌های مسکن شروع به جهش کنند.
🔹
همین حالا هم میزان ناتوانی در بازپرداخت وام خودرو به بالاترین سطح خود در بیش از ۳۰ سال گذشته رسیده است.
🔸
تمام این‌ها قابل اجتناب بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/435815" target="_blank">📅 00:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435814">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔹
حزب‌الله: با یک اسکادران پهپاد تهاجمی، تجمع خودروها و سربازان ارتش رژیم صهیونیستی را در نزدیکی شهر ناقوره هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/435814" target="_blank">📅 00:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435809">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pP4c-xSBttTIVk7AAVdmZYB2LQADwaSI2SxMK1XUyJXA68Jk6z0nTJi6HR7J50fhtpOez-jE4-d7bdasOTHV2MS673Rlnfx42dj_IVFbAlT2pa-iuUQ5k9e1STMuaN2taDuvgLzfA6JCg6tfSBQjjbmI5m3oBP5yrcf8AOnMDcRxCExNbPLVsDGNihAlgElWl2DOe_L8t317xNNmQ1w2CZxOcrH2pHC3q_8BKBFioF4WGuG_4lGWM7B3Xnd6gjHT4qkrytzyrCxsy9XDstdydaxCIjr-uI0E-QsQJjVRof4pSxNM_MBCEJfSTeiP-DLJcvecSq9F7ZfOONg1JgDMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiCRHke-4FVeZRsOdhaHVeIAeMhe4Ry63hYPITnhrqL9qYuF4yPvEV0vlM7LG_2ipJdY4PzhkQtvmIabtKs4wCYRP4T8tpRV5MvR7pmfeNg1EAdfIE7Xgr8_-Yy10ULaIoqnCCgA2jpKJSK2Dal02hQ1Yh3HcKwzEyjhQJRP-GEdl0iLIP7cRsnNKUl2aReMw_LMfuwS-rghvAcV70PKA3TmuUQDDl0_Lw5HN0ytKzXrN4d6bckW-kZArSL3N0dr9_ozYA--6rvKsdWvAeKlXPj0dBwJdrQV1PPizzVfOrF4La_br2iu700_D_kTvtsDtw2zIxmVmFAxT3Z_HSfJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8IO1_BXExp4FVK7_a62PiSGvNZt48UmyBwW7-UDpy4W74oB9XFc8CAb7V-csjE1RL-w0L_tw1b1PDtss7dHhOBdngKelAFP3M4KdIXeEqlbCTrcfqbtni7VWgv5u_P9VVmvO-0n0TYpK0419LQazZ8mrC6efkKrjy9VQ34R68gSWbHcjXw15xEwzH-A99OR4ZBhlxnz_DXnxxlEUN75bd9fJ_W1fwn6UwpXvQaqoFrXzJIPT7gqeqaf6e4AubhTbLucJtPooM1gkqsFhRIBWk2_BadSzYtarVwBTDZznFFOpJ0H0Iba04JSa1PYgglTQwiDZrNdSrR59UB1ARZNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXte61syjCbwHBjGRGIs1K95dMXBTA57xhLoIoTPLT5d-bzwTDOG-dGiLCB7_lNob6Q6VUsMoAdFvUpM4BvK-oAHh7rupbPTDv3MN39xQPqJgkTUEbbC2TOuGpPRAdEhS8wSh_PdwJzvKOdV-9jsQxjU4cPuv7imYabPNvhPVPz7_VxI48P_D8Nvy0BixxhgC_9FQLYBxXQFdgKUNS3H2DDxYCG2E_npnfiYgdUcdJ_lUVBC4A74vI6tMboZk8HYolDoP0HIm1TiG3QN9r8OZ7WlstKV2jc64pIe3H4LpiFZQIdJds3uAp_FUXDDlkG_f4DdxNG9-rohbs0A3AbNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yp3Tge9Nbcdim6H7PiKzyUeUBuEm2tk2qbS8dcLxkI2hvX3E4xpU3pVA4OSEGlpZLg_ct5TA4Ihy3CNg50yZLBPqdZu4CWTvnjYzPQCXZ5M7kx4T_M_XXSzPbnn6YM4f46xi9gNW9rhGtwbNZOB3qZuWhRUKRf8o-8fG6Mfz0y-k4E1nWRkvOWLPZxSlyqXpXj9kwqegpj4OoZNqgiz4jJ_xv82GJ7PNMYR65ppIsIlahBy53bfG7_zuGbSgt1jd7a0USgmmSa0WH5sr2FbejSs-L9rZ3133i2hPyahGqmmpp1wlSRR6ElfHI-27_qTqz-lgRn5VO1E9qNzXsShF9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۶ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/435809" target="_blank">📅 00:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435799">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rm-8dzJnDu66yHEhyGUMmCmEp-2sqQHDFukHg-YneodEtm3qXnmUlBNO5yBaRrRMnTuOZHtVHfUfyF6GDzKvfaL_i8xKk2qc2-ATQETR3OvnX1E4bM9pPOobMNGosd3KyP4Qkdo9qXeyU794s13lRosTJLlaDXrKSa8HTz3_1mW_NEBlFY_vPgVNVagxX7vBG6TLfwFY9CKd0IS7CES_-Aor-RIhWhsCSY70DU_pLnJVzpTkW8ayXtSkhyohOt1vstyy-Z4jKhcs3gI-5O1lgdqMUXA8lIAXmuqi5yrYah1HsqDLbdTukaEKH75wO2Z1MpidvS2uJ3AzIInWTKXIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOJiim5OfguloUJYzsAq9Mxtgsj10SqqgR6sVMIqpoqsJTpmIB5Ip17h_KQMlUeiE-G8aqPVV8Q6pxiMKE6TkauQUE12NhUxf96as28AUGc1PoEdA3HYGEMicrH0wh5BL_QH7OiyzHrEBn4LnrLR_jRSQcW5Q3xMpL5o4zyulSPAJSXx5MbidHKpEM99PMaJ7_1LoKk7EzSrWZq9oj2eTLg25XKVKDnhmwJcW_kaGWoMnx1xlVCAV7XQRLMMfiXu7iwlDVRVzbvFjPg8w1ZBYqK0j-cGh_xKLI8ZXdpA3v-V3tft_4GvZ8Ngk6jZiAusOJxG4NjSxCkjrVWHomY9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGli6Alkh69xnXZuPlSspmo9eh2cDiNwQYsNnoOiL-Z1d_hGTfWXZIQNimZemmEA6WgXu9r8HHDNVnEalDqX68t_gYz2a-Okxik5h4nQJoGHG_eawdmVqp5hAegm-mZBCm-78d8o7rdJYCv_EMuw93XWYEqMA6i0P_KDbKwPie5blIHnEOm1HZ1fPvplXHUDugnyHLsiBctNiwGwrwO3Zt77ZJ0Eivfk6IrxRB5HJ8_fxq50elyCrv9ypL6cKknadJ0V-yEmwsZ3kj97909Ypd7MO8LVsnZh5YloPAdvpm_kWVcgROCSV17_dpxxe863QO1u1AOP7MVT6xlH4Wk6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzdABEUr1LeRRY0q5rZ_97_oMclNApqtAvRyUVN_34RkpJaQQFgzn-iL7IQcu0nGyx21SyVAWHEU_79ti2Kid7GhY26ToxmN895N7liRnqNgjXYw5Mm1tRRctyf9YbLOiyxfh3w9u9Qj9jkwNVnHx4m_M4KIVs7_XDTdsPeJ8vSoVSB4kpIot2jVerJjPJhGeh6IIK4cVCX0_iwxNqhqvfhahDF2DFkbeNgWuepjZUZ7Op4YVixVU6o7zCXL_SdMaPHLW2HOfETy9k8J9IfKPUWEpaMomcJBRYLn6CmkfLu0jVj9zt2ukwjiJycUkH034y4UMpk2Vo0qT-7fyGcI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmTuFS1W_fUQjxf4OLrPgjV90Qd7WTi2_8u1h0u4-PqKX4iEWZPd52PQDxhk-CkJSrYM-G_BVpnaNRuBOM1aRaj_MnjrI2E99K3l5vHvuB8H_tT0OGRhImeVW0bIy3SDSHuN8VcNy2FMQf-tTumVsI1z5IxS7ihrLC1UIWPPBVynlYvR7nxTAR2Y7pl_S7ptkk4qCTC0PKfwChAKlP-SCPijuLfc8tgYXQhk-XyH488KDILFu-b_aGseOXuJPOQcM1J-xUVYCOErKshWDHffM19_6leNLB6hMhRN4wuHROO1KkofGrLBqCMEsF4tEpFbplygGu5T0qq8Zq8juAv0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAfH5zHJEC0nz_2Gb_KptU1ru14GVxsIG4s5LHeiCMuCEK_NWcshSHX9UhEGLOI5AoF2So29ssSMvTSKBPSFKDBMri1x8VFAhCHh9glsnoti6FqbWIN6ZM3eu8NwbeZcbTFaTcon53qdSWcOOwvblWJCXdk_RDpkzrjBdKrmWTwUF0GVZhmRVnoWZr4SS2N4pCHCSIw6sTYntjlrmUfcnZ3idJ4KjoMUcNXmyF3Z5-uZn5PU_3bhtgYT_yd_b-yxgBQ21IpGEf_9fw6fK-4de9VqUYbFvcZ3F-ZWIaT7oIz2j8BRfNnMxGO9F8odSareUZfMFYBOYUKNaaAkumjG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_Jg6ZjYk2Tw437sLXGfD3DXw5Q5hREm9OiEKE6xqyBoLihAQEm8Nf6qy5tSkReh3BbVRjPoaG4M0-aQRCn-iYdH2oWjrjCKr5yL4RvNQuif5THAzIfnUJBugUPDrFHHeE7JRE1bZiFo0_2e_xc-ndmNNGgaQ_37_h-s3Y-mot3Q8gDk3dqvsXCc7rt7rk8LPp6CGRQr8S4fNSZOAkZChFcJlwCxYCKvSDp_914S2M2AWRGeOPMzeCLaJXWrTGh46GoAA_FlAYoUoWoOpVoLMJsj2vaBOICNpikto8iYqrNs9LtIL8rPoz7AqWWHv8yBe3QKI-L2wB-b2aROp0gr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTD6_u5wnIN1E0stb0i0n6uzWt8xlm1YaazgDECLyhSq5zwl-Nvhjw6fsjvB6jOaYsmXImBbY-FpmSBpJQccvMIDB8jg3RgoeJCAWw5CQCiSxw3l9dHVlPhhLitRVvZtX698FeZcyHXwXN9zHlSzMHK3KQZPUAqDPP7QE5YYDG_-ibm6p5ksQnybkCYKx640VAbwQoKwefXvqRR661nrWC6Mu1kVsHQEjEfh396LhAJcJsQqHk7qBfMcH2ec2f2ZPoUWaiJXNQpfSHzS3R8V-xsIkjmvTXD8Ak_woufJVMrESxF9U57QcEILUBSSe3BUUqpzPt10bLjaTQ3s7wGXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBymO1F5USnVqEi8Sh-BQWpl0a5El4j56yokvSUrIbB6J6j48UiWa2ESRiMJaik0fa87-y41D46j4WrMv2MKBzvTBSoRlcQuZvlm3vX4v3-SXhK2e6JFEntH-Nk3ml3D-arP7aS8Kv-MvN_64GYpeg9CEjSSiqbC4RBOj-auHySYhFnGvExs6trsidED8OFqBvPzkFw-As3uWCMWfU1lQaDRM7t7mZ1rdnouN7r-T_jGhDXHoSOcSbAO69TvzzzLUrfAD3nbjqkSEHpWsnoepF07w4qZaQZlW95oFCP3GKXtEXl3BMFNT0syCOx2cEHSiGfTQ8Xd-HzMsGTNBCELOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mknBmLoZqaC675gUP1_Rw7uRFZpDBZvtIa3iM4oYv4nOjQKAHFF8CpMUN0CPokH9F1OwIy5Zjg0PoiYYQ-AzPhm-mGVw1wU-uocV3AmA4dG92leMuadvZN55jwnol7WJvl2vYIfFr6_zBV8wGGAk5m8kam4dUiahrlUrc0rPB13zs6idGKz4BN8RhzsBcyAeB5jifP3T8l_B3wIL5arUfvDwWddI7jQc-jStEGievtiS4jcUrYSFjhmLzPRLYPiUZBsGOECNI7_IxnpzVlvFNR9d2ZIbFvbuq4BZHRPUzr7_fG6wyXnyPhPAsW1fQeeds6oLM6AN8qPcrCfpVLObIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/435799" target="_blank">📅 00:34 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
