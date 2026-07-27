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
<img src="https://cdn4.telesco.pe/file/iITVKkjmxh0o63iWYcuXBeMvk8ZAGzQ2zNMflXMe9ZHSS7HYDUdDtVXVAlEBVP_HBxjEC7zX6PXTpKM2wUR1ij4bQeeSeKY7gU0qKtRDUwvO-mF4PMOFrJ49bLHziTHoiyDFSew_NEjhgS_Tka6aDy2mPqEbupoK-vXQz5q4hukIwChF1P2d18ipvldl64EfQK6R3TaT3LUQ77TZLHwjwS0Jwp4WmsavfHru6K9Q8Gc7hClR3etT_UBS3SLgiJfIlcxr6ZokUz802qdro_6oy6e_4TyDvbN3kjLIDB3OicA42KFbEQ6CqTFRWWUbOEgL6R2bj2WWZXr0CVAvcvTvZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 18:50:44</div>
<hr>

<div class="tg-post" id="msg-85768">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dfb61ade5.mp4?token=B865K31g7fA2xsw3GuRE7Cwmg098DYP3UAwIAcEtbVUrESisDf97f-fMl54CYN1IJp__8nIeYvXTMZxYlDjgcydEc_P-TMv5b4soC87gibOj0FA1eOdcQRLTJSpqpJ9Wbv5MZHwyP7mVvVFPfW7Nm2Rth5KIn-tPVUK_L5f_Xy-2iN-Coit94ZBuRJwOeSD2_sV4AgC6Ke99Begj_r3SHRbQzdfqrbHfIoQs6l9_kja1yyFjA-MsKpwZ9l7flBu7axx8QAKy0tAsI-l-H0RfoesSR4Fmwn_kYCsl693XM9K6EC11PH8HzBTU_3-jjtjfDJxg6hlcXzKu0CJM8RSQRnxucxSsnWge-PbytetTgY3cvCNY7sVMN76UUqnFtriT2rIo8Kq50uJ8xDuonaO06qArBPyXYPiUluKGS3g88XyAf8Qqv5xv5Iu4RIcfy_1K58xXAqI0HfOUmRiRqgYd1-2RKP2gGa0s7NeuH2uVgxREz7IMfCOlHHRutC9nNe1q0Lti1Ieqfh4yVsZKilC9VIW7c44bGh-JnI7HIxJ0KxAFbTWNgwk5_HHCKl3UhMrcUTuktbCuPXvmrUe7Q5Mx4buVmINTvyn9O4VbNF8F2LQ2RzitoXtNcNpDZQ_P_lIcP1pPJRKkZspORphtKVxYNyZwhXKrk_Pr5K0G7pwPknw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dfb61ade5.mp4?token=B865K31g7fA2xsw3GuRE7Cwmg098DYP3UAwIAcEtbVUrESisDf97f-fMl54CYN1IJp__8nIeYvXTMZxYlDjgcydEc_P-TMv5b4soC87gibOj0FA1eOdcQRLTJSpqpJ9Wbv5MZHwyP7mVvVFPfW7Nm2Rth5KIn-tPVUK_L5f_Xy-2iN-Coit94ZBuRJwOeSD2_sV4AgC6Ke99Begj_r3SHRbQzdfqrbHfIoQs6l9_kja1yyFjA-MsKpwZ9l7flBu7axx8QAKy0tAsI-l-H0RfoesSR4Fmwn_kYCsl693XM9K6EC11PH8HzBTU_3-jjtjfDJxg6hlcXzKu0CJM8RSQRnxucxSsnWge-PbytetTgY3cvCNY7sVMN76UUqnFtriT2rIo8Kq50uJ8xDuonaO06qArBPyXYPiUluKGS3g88XyAf8Qqv5xv5Iu4RIcfy_1K58xXAqI0HfOUmRiRqgYd1-2RKP2gGa0s7NeuH2uVgxREz7IMfCOlHHRutC9nNe1q0Lti1Ieqfh4yVsZKilC9VIW7c44bGh-JnI7HIxJ0KxAFbTWNgwk5_HHCKl3UhMrcUTuktbCuPXvmrUe7Q5Mx4buVmINTvyn9O4VbNF8F2LQ2RzitoXtNcNpDZQ_P_lIcP1pPJRKkZspORphtKVxYNyZwhXKrk_Pr5K0G7pwPknw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
لحظة سقوط الطائرة المسيرة الامريكية في محافظة بابل العراقية.</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/naya_foriraq/85768" target="_blank">📅 18:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85767">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
‏ترامب: لن أمنحهم وقتاً طويلاً للمفاوضات؛ إذا لم تنجح المحادثات، فسوف نعود إلى عملية عسكرية قوية للغاية.</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/naya_foriraq/85767" target="_blank">📅 18:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85766">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
‏
ترامب:
لن أمنحهم وقتاً طويلاً للمفاوضات؛ إذا لم تنجح المحادثات، فسوف نعود إلى عملية عسكرية قوية للغاية.</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/naya_foriraq/85766" target="_blank">📅 18:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85763">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJrlSeI10ax10dyO53ijY4QevkySDJcF9Lf3fUpfNfiLZ9LIocMOnaeou-HiYWYJzLWw3z6_gNvg0lLsLVXoOa84pYJwITmY_atEh1P_AOQ5xy7Qjm_gEhXYAvqepqZ6kVu0tm64vP0wNwFuF9DvanIsfgRLMqg1drYq-D-9C7P5oCOl3_ekxwskMLFeR8QJacchBzmtjiNv8XdwUSrxE-amvS7UUlqhOyu3mzupwXBiNt2HQPKSo-DXJ68CU-sa4OQipXUv5-MBzy43UPxkDFJM2VMdI-78ExxFmTuoZWF_xi-3TcZrpcqoe9llB2WlSwufvxn_F3RNwZZTVLy58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0y4jAu0xUhRzQWQDv2jKihOCcHNXeFGl4UPUqpHoiC7qliicL3fXZXNkx5CG56VOXFoMI-8zMDjnpqqOZ9sWpWGzpJsYqbaQmb-ungt_fHnPGfOFwR6AD9LQakQLQxY6XI-x0dLRFrOffQo8q2_HwKk-tp5dF1LdEUKo07ZKBN2RERFTVPhAeB_L4VMzZ429Qm_7vM--Q2ycM4Q0lUmkBMArSvqfOjgHu2JWRvR9uhosN009_qb_ejNxJdv9CmrEkAWKTwk2S_L2BacBBpvWWrshQnFUX8eeHhiu_3tBv8afx38LROcBN1vX5oKtP7w0AX5NkkqyA9raMPnsV9ecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kug_BzfJ8mI1CcDVPLF0-IJX01QsjsMByVjpRI4zAw0h2xbmOpM1WqlesQOYoaEUMnMWey8jjVr4KSr5fMghaon_3SndtjH622IGnZFRtRU9qLw6OzyAQNSP1dMtbFtr_mDuF8jL0mW2yyFdoIASQ5CXgZBRCHsagnBCkLQRG37sVjk6v3vIxY6gmWOo--G0HBE-21X40N2wTwTVKIy4Jg7av5M4_9qkfIm18a3rzarlX0qiPteSqjVXC9rnA9aXsJh-ML3QOzu8ElII-duwHTsp9uW1z5wS8WVUcjYR6rSzHiCDAJvZkuyOQotJ0972PwvQVcTk4eqPmExJrKZ7Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏الاقمار الصناعية تظهر احتراقاً كثيفاً للغاز على طول خط أنابيب المكثفات/الغاز ومواقع الإنتاج في المنبع المؤدية إلى بقيق السعودية. كما نلاحظ أضراراً واضحة في خزانات الضغط في المصفاة. ‏من المرجح أن تتأثر كل من خط أنابيب الشرق والغرب وإمدادات الغاز إلى رأس تنورة بهذه الإضرابات.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/naya_foriraq/85763" target="_blank">📅 18:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85762">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
سقوط طائرة مسيرة امريكية في شمال محافظة بابل العراقية بدون اضرار.</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/naya_foriraq/85762" target="_blank">📅 18:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85761">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd27e2cef9.mp4?token=iIrW02xoyaCSh9Ob9iwpKUJTfZnTGvjT55dFnALYvBmVN88Fi0TesWLzIqEQJs8hXivXDnj79tIx_uo3g2fEv5F7IkNsuQqyyIjOTjxN0JtsT5an6ssT0YFFGCebyWEm_qzhxQbnrYiTe_7I9HG-Qd69mzxQnmDk9La9L_Bw4SnUBj6EUAlo-wGDU8Yko5I8hMvu_ZYD1JtimRAb3K4cD6xdERigf5_eRC_YSiS8wwf6LpV_Ct8HJi0d05dmUHQ6rwpu0AwfIhscDtpo570hDL5sj-PcvT3J-9wlcIGxUn5bYyhu2UJBGV_MhAA_x1pBAX0ofa83F41BwOke8uVW8rcSF5X2_GW_8vAGoaM6kk1kLoMGMmldP85psevbPQSGVYPSDttl2BmGk163-LnoIZvtz3dmI5yU3Ft0hd4ezzVx36vdLyzOceC5FhD5CqAa7hlZpjRY1ZWdaqsU9JRf-nevQQj1ftemodaSXscKx3n2jd0uAsGzSuODeZkMUlImWe_zHm4I9yOzH2eRZi91YfX0azeD_ozaWJKnoms-B70aiBT48bQV6EEYDhISePtUFK2Ucrc7IIjXFIx2l3gPcFZ2YRXFs09bJ7F9D-L4TuazVtPs3thuO4HdSEmQxW4p4yrQxJNQ9YwfqrFMgvtkFMz5QeDMtmjXbu11_5WKNjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd27e2cef9.mp4?token=iIrW02xoyaCSh9Ob9iwpKUJTfZnTGvjT55dFnALYvBmVN88Fi0TesWLzIqEQJs8hXivXDnj79tIx_uo3g2fEv5F7IkNsuQqyyIjOTjxN0JtsT5an6ssT0YFFGCebyWEm_qzhxQbnrYiTe_7I9HG-Qd69mzxQnmDk9La9L_Bw4SnUBj6EUAlo-wGDU8Yko5I8hMvu_ZYD1JtimRAb3K4cD6xdERigf5_eRC_YSiS8wwf6LpV_Ct8HJi0d05dmUHQ6rwpu0AwfIhscDtpo570hDL5sj-PcvT3J-9wlcIGxUn5bYyhu2UJBGV_MhAA_x1pBAX0ofa83F41BwOke8uVW8rcSF5X2_GW_8vAGoaM6kk1kLoMGMmldP85psevbPQSGVYPSDttl2BmGk163-LnoIZvtz3dmI5yU3Ft0hd4ezzVx36vdLyzOceC5FhD5CqAa7hlZpjRY1ZWdaqsU9JRf-nevQQj1ftemodaSXscKx3n2jd0uAsGzSuODeZkMUlImWe_zHm4I9yOzH2eRZi91YfX0azeD_ozaWJKnoms-B70aiBT48bQV6EEYDhISePtUFK2Ucrc7IIjXFIx2l3gPcFZ2YRXFs09bJ7F9D-L4TuazVtPs3thuO4HdSEmQxW4p4yrQxJNQ9YwfqrFMgvtkFMz5QeDMtmjXbu11_5WKNjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مشاهد للطائرة المسيرة الامريكية التي سقطت في منطقة المويلحه ضمن محافظة بابل العراقية.</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/naya_foriraq/85761" target="_blank">📅 18:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004bc022b2.mp4?token=OyrLV84JV2Nn9HLhiItHXowaxPva7TOrskT9wj5RJ1AKa3rTlffy2yAr6af_e-DD575j7duwqnJuCvsQh509Fp0n0IurnWBt-4UqDLxRKMtIwBd9piiF2aMZUAZyaDp8a9lbkAr-tlCrN565mWrSRwUh12BZk8Hpt6OIx9u8_gEJqnmIptCfOQdZhiTc79LqhyWu_DdwSm5xnjkyQDYGwzvBK8cut8d3KE2s44OR51i_JErFZAO8r8oHHesQlN6P_ZSFCeSnTqD0D63bqWzhhr5SC2vVPaa0qBX8vMmCjy5L-e-Dr9qfOFyLfauwDGA8lHwkUVwa3ldDknx2_L1s6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004bc022b2.mp4?token=OyrLV84JV2Nn9HLhiItHXowaxPva7TOrskT9wj5RJ1AKa3rTlffy2yAr6af_e-DD575j7duwqnJuCvsQh509Fp0n0IurnWBt-4UqDLxRKMtIwBd9piiF2aMZUAZyaDp8a9lbkAr-tlCrN565mWrSRwUh12BZk8Hpt6OIx9u8_gEJqnmIptCfOQdZhiTc79LqhyWu_DdwSm5xnjkyQDYGwzvBK8cut8d3KE2s44OR51i_JErFZAO8r8oHHesQlN6P_ZSFCeSnTqD0D63bqWzhhr5SC2vVPaa0qBX8vMmCjy5L-e-Dr9qfOFyLfauwDGA8lHwkUVwa3ldDknx2_L1s6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سقوط طائرة مسيرة امريكية في شمال محافظة بابل العراقية بدون اضرار.</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/85760" target="_blank">📅 17:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada0a48777.mp4?token=iqHRSvv9yBcdYviLVRsquzuZnPXEWB_A8gHvPFMgUlPICOEXVd0kkXRJ5WUyO6l_MKJigEyuvRaUmd8iVs1d_OCO3RI0p2TLX9DJpcIFvS-CfWI5-EnbH3oNfDE5WZpkzoYlwH4rzP7rlLbBJXiBk2dCded-yz2xmbWJZAmHLCwN0IJsmn3sw7BM09DOpMKkWrapAkHoHk4-vb-UV_kHjn0utdl5a_XoaEp_0kCjMioIKDv9haoRWU0MVHL5N6sUbIOaDSkqSRQLtKEMswYg8z1EMWxVXaBOrJ8gpI6JOaujuoFBE0u_Y0m3pOfnT3_jaU64CQDjvN_twH5Pgptc1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada0a48777.mp4?token=iqHRSvv9yBcdYviLVRsquzuZnPXEWB_A8gHvPFMgUlPICOEXVd0kkXRJ5WUyO6l_MKJigEyuvRaUmd8iVs1d_OCO3RI0p2TLX9DJpcIFvS-CfWI5-EnbH3oNfDE5WZpkzoYlwH4rzP7rlLbBJXiBk2dCded-yz2xmbWJZAmHLCwN0IJsmn3sw7BM09DOpMKkWrapAkHoHk4-vb-UV_kHjn0utdl5a_XoaEp_0kCjMioIKDv9haoRWU0MVHL5N6sUbIOaDSkqSRQLtKEMswYg8z1EMWxVXaBOrJ8gpI6JOaujuoFBE0u_Y0m3pOfnT3_jaU64CQDjvN_twH5Pgptc1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سقوط طائرة مسيرة امريكية في شمال محافظة بابل العراقية بدون اضرار.</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/naya_foriraq/85759" target="_blank">📅 17:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85758">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇶🇦
وزارة الخارجية القطرية:
ندين بشدة محاولة استهداف منشآت نفطية سعودية بطائرات مسيرة انطلقت من الأراضي العراقية.</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/naya_foriraq/85758" target="_blank">📅 17:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85757">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">على عكس اتهامات السعودية للعراق   اليمن تتبنى هجوم على بقيق والرياض</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85757" target="_blank">📅 16:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjxZjMeyBwAaIdwcZiyAenPicIFroKpGtb4s41XNGUn17QVocBzMKt4xkPra45BLR6Ly4JK8NZQLKIH0Wqn7IHux4KZqgWePFfiyNvdfSjofMQ2ike0cAQQInPq-EBNIHZP3cjaY0JJij5BhzXvVJ9boYza9tBCk5IF944lfdDh59jiGX8AkHHqRflB-yUEKvbkLLrIRDI9Atmwsqet5KqOf0U44NurPTtVxq0ByxZsaNzLrf5ZEeiJB_FrT8mroI28nL_f44XKbYqY7u1-FQMYRecTwX_iTlPmQADKcN1EDN2r5fUk0e1QydEb0NWiAjG-kYg2ndBvBMkZR07j-hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة مسيرة من طراز Mq-4c تطلق نداء 7600 (طوارئ عالمي) فوق تل ابيب بعدما كانت تعمل قرب حدود ايران</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/85756" target="_blank">📅 16:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/85755" target="_blank">📅 16:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85754" target="_blank">📅 16:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزارة الخارجية السعودية: ندين الاعتداءات بمسيرات أطلقتها المليشيات العراقية ونؤكد عزم المملكة ردع المعتدين.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85753" target="_blank">📅 16:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85752">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇾🇪
يحيى سريع: تم بحمد الله استهداف عدداً من الأهداف والنقاط الحساسة لإمدادات ونقل النفط الخام من شرق السعودية إلى ينبع بعدد من الطائرات المسيرة وذلك رداً على اختراق المسيرات التابعة للعدو السعودي للأجواء اليمنية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/85752" target="_blank">📅 16:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇾🇪
يحيى سريع:
تم بحمد الله استهداف عدداً من الأهداف والنقاط الحساسة لإمدادات ونقل النفط الخام من شرق السعودية إلى ينبع بعدد من الطائرات المسيرة وذلك رداً على اختراق المسيرات التابعة للعدو السعودي للأجواء اليمنية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/85751" target="_blank">📅 16:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">استهداف منشآت بترولية بالمنطقتين الشرقية والرياض</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85750" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SstcQYYZI9hYW3YUoShNm3gLpEnO6L9N5BaprdKJ2xjsMfTNRtWjFFCexbgQWctimQsveBWyzo0g0lY24zkTKWmijwFLvnc56CL64FaTEWvVst8Cx08wOe9nvSlyBm_joX6WuAduo1-CossZUdm21L4u1B-TpjCt776RPjHIygdtLfUbYR6LeSUnWe6VyF1WAc4k5q9wafMvGtWJC6emOy5BeAd1CJk2FRePIVDRxAELpC35l131NcTQq8mLhayR5nbqBFTYW6va2ZfLZxobcYPHIeYQZ8jmbx34J4teKIdBNNhm30kTL8e6EO4qp1f1nqYbXrY-UIHozXXW0-YKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاقمار الصناعية تظهر ان هجمات انصار الله على السعودية استهدفت في المقام الأول البنية التحتية النفطية لشركة أرامكو السعودية في جازان، حيث ضربت منشأتين: مصفاة جازان للنفط ومصنع جازان للمواد الخام.  من المرجح أن يكون لحرائق الخزانات الناتجة آثار بيئية كبيرة بسبب تلوث الهواء وانبعاث نواتج الاحتراق الخطرة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85749" target="_blank">📅 16:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85748">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FulHpqkFBvndwiEp426kxflz5T40orQHWsw_fkOkcGkXJnmzWU90y0_nEhHQ63SXcHBl9eJhfMtziQnmffm5hz33hPStv1LD44OIkPx1Vg49lgiMtmtd9iUubpzBC_77tCt-Ceg2qCShb5AAcuBR3OGYxw22vWSDgbn3vr5hq8tdyKdWytJ6tcui4WTPVmnNl5x08PR30jAiidEaFxsQb_O1rQUV6QH4qaI32mva39bZvCQ_QAS64bIZIAtX_1eiPGXofyjM6NuvzXa0F0hcnMRjqZrR2ldoGp8AEraXHno9aA5MUXeLyg8Fgy7wT-K9C4g16QGdgFwuir1ayQddZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
This could happen when you choice trump way in Hormuz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85748" target="_blank">📅 16:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزارة الخارجية السعودية:
ندين الاعتداءات بمسيرات أطلقتها المليشيات العراقية ونؤكد عزم المملكة ردع المعتدين.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/85747" target="_blank">📅 15:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYfhQbIX1rJcS1dp7lY7xGdPIhgXhqBnjBinOQDmSMujx90wLcpEFOBNiSjaUetpwix0nsN8fKs999H0AMw4OiSjQtZoI_Z-spfdDmCMstG8Cx2JaKAT1nTXmvWx7abOwP4ts45RDuovLwTSx5pZJMPzi5sxQ1_KKDiB0CMcNBBlUBi3UixdVNSfkb2z1Y9sy9WSqIbweNI3eUC7i2ZwQxpZFQLkTdAJpATIr1tUvNDR1PbhUi0rYmEjebBTVH5WjBCq4-6o7vJFMsdWuM3Ex2_FxICu_8POU0flrGerH8zTnp9lKjOHnWPOMPrHffRRaCx4C9NQVX23ZVYhOo8YIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الطلعة الجوية السابعة والعشرون للاقمار الصناعية فوق مصفاة بقيق في السعودية تظهر ان الحريق بلغ قوته 70 ميغاواط بعد الهجوم الايراني. ‏بدأت السعودية عملية حرق طارئة للغاز في مواقع إنتاج متعددة بعد تعرض مصفاة رئيسية لأضرار. وقد تم حرق أكثر من 100 ميغاواط من الغاز في مواقع متعددة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85746" target="_blank">📅 15:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f90e9vXgG8jCC6wgnC1ic8Dqq4HZdBbS5Jt3AGev-5HAIQ1NCEEJaKOYBwduzrgEgf8uZ3FUFo8g-LYsnQ5Kes9a_WsBeGdv_m1NEXg1eZ926uFST6eWsRXmj44K9dlunKs-UQymjRmvHYWoII5MQTZ6u45ljlxaqmejAeJvOGoCmPa_gyf-wgEsvcVAa4ISqsDoYaQl2HEEKFU-2KvkSPylmrQK76ZGJiLxR18kzn2ZHeDQTjJ0l3ka7Spvojncu4Gi2JftIY6butsdmhJdCE14kEYzJ38-0HILq79-wwBzfaHV4LPCaxwvL1rxm-rE4hEnjnqbKRvd1nI7vMEUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Иранский перечень целей для наказания клоуна Евросоюза
Зеленский является европейской прокси-силой, и иранский ответ может затронуть европейские энергетические ресурсы:
1. Нефтепроводы, связанные с Европой:
· Баку – Тбилиси – Джейхан
· Баку – Супса
· Саудовский трубопровод «Восток – Запад»
· Южный газовый коридор
· Транскаспийский трубопровод
· Трубопровод East Med
· Арабский газопровод
· Трубопровод Эль-Ариш – Ашкелон
2. Нефтяные и газовые месторождения, связанные с Европой:
· Месторождение Азери – Чираг – Гюнешли (ACG) в Азербайджане
· Месторождение Шах-Дениз в Азербайджане
· Месторождение Апшерон в Азербайджане
· Месторождение Левиафан в Израиле
· Месторождение Зохр в Египте
· Месторождение Кронос (блок 6) на Кипре
· Проект GGIP в Ираке
3. Заводы по производству сжиженного природного газа, связанные с Европой:
· Завод СПГ Идку (Египет)
· Завод СПГ Сегас в Дамиетте (Египет)
· Завод Ревитуса (Греция)
· Завод Александруполи (Греция)
4. Проекты зелёного водорода в Султанате Оман с европейскими инвестициями.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/85745" target="_blank">📅 15:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b07d9f8b2.mp4?token=Ha7fxjgxuw9JCTTPyVkl25v_0vBb-VdqgroCUeMdvv9JXthzVdfwNeKh0HypxpGDhTUJqCmZeBkm-hPIPXLczvipXc1dkSNSmtxlbRvtCcIb5SLzgSvOwtlKL1bZjGOqkypxjDd2WBMCOjX1dZY4wBo_tVd82Kk7OnnlkpwsFxMAx2QLVTgszX8pXDHl7pSqQM0IjkRdushrUbyr4hVv7EQOxMxL0eMDLwqf6LWxOGVJJY5Xv7dc1FDjZuOsBBp9T_lgztAl3pvC4OtWl33wUMB4T8aUDSXaEJiwNeq044zSQSmDdr9g4BqkVq_txXOFnA3mifszvvHOqXir-CoJ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b07d9f8b2.mp4?token=Ha7fxjgxuw9JCTTPyVkl25v_0vBb-VdqgroCUeMdvv9JXthzVdfwNeKh0HypxpGDhTUJqCmZeBkm-hPIPXLczvipXc1dkSNSmtxlbRvtCcIb5SLzgSvOwtlKL1bZjGOqkypxjDd2WBMCOjX1dZY4wBo_tVd82Kk7OnnlkpwsFxMAx2QLVTgszX8pXDHl7pSqQM0IjkRdushrUbyr4hVv7EQOxMxL0eMDLwqf6LWxOGVJJY5Xv7dc1FDjZuOsBBp9T_lgztAl3pvC4OtWl33wUMB4T8aUDSXaEJiwNeq044zSQSmDdr9g4BqkVq_txXOFnA3mifszvvHOqXir-CoJ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
🇮🇶
تهديدات من عصابات الجولاني تطال سواق الصهاريج العراقية</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/85744" target="_blank">📅 15:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/85743" target="_blank">📅 15:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">استهداف منشآت بترولية بالمنطقتين الشرقية والرياض</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/85742" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/85741" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85740" target="_blank">📅 15:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85738">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d1e66237.mp4?token=huOTmliZfOZs1jZaw5GOPTYVpIv9OJ3WtwgNnt34wMSVOwU_xtyIfoavZCF3izSaLt29aYd0Qe6DIr2RL4Qu58qy_hPlKqZ6ca7CMEaIvRpFzA_bK7GkhJ8yoEwJDdoO1IGt5zn8m0kpVRs7pBUu5jv_aUpnEve-I_SGqRMw8A5iVUUfXqRAMnjSOZZ_aL5Hv1xk6uGVSWEgzrIIvAF72_zJ6nvoWSWlBAL_tGpSN5x_hLNWhF4G9HgxxyiqdAxBAgHWmiM90lc8KYMf_AsOJtKnsB49toIFpXjy5Oa9hFGJnhxT2BOnhd-5nIhmBeCJg3LCD0SBuzhLRYBM-E9lyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d1e66237.mp4?token=huOTmliZfOZs1jZaw5GOPTYVpIv9OJ3WtwgNnt34wMSVOwU_xtyIfoavZCF3izSaLt29aYd0Qe6DIr2RL4Qu58qy_hPlKqZ6ca7CMEaIvRpFzA_bK7GkhJ8yoEwJDdoO1IGt5zn8m0kpVRs7pBUu5jv_aUpnEve-I_SGqRMw8A5iVUUfXqRAMnjSOZZ_aL5Hv1xk6uGVSWEgzrIIvAF72_zJ6nvoWSWlBAL_tGpSN5x_hLNWhF4G9HgxxyiqdAxBAgHWmiM90lc8KYMf_AsOJtKnsB49toIFpXjy5Oa9hFGJnhxT2BOnhd-5nIhmBeCJg3LCD0SBuzhLRYBM-E9lyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
خاص لنايا |
مشاهد من سماء مدينة جيزان السعودية حيث لا تزال سحب الدخان تغطي المدينة عقب الهجوم الذي شنه أنصار الله على منشآت ارامكو للطاقة في المدينة قبل أيام.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85738" target="_blank">📅 15:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85737">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
انخفاض صادرات النفط السعودية بنسبة تقدر بـ 50% بسبب حصار انصار الله مما أربك حوالي 3 إلى 4 ملايين برميل يوميًا حيث تأخرت الشحنات أو أعيد توجيهها أو لم تتمكن من مغادرة الميناء.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/85737" target="_blank">📅 15:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85735">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YK17_59qy1JpmKeWOrDaNi6I4wsek_ZVkfgssEsDWRsKeo00KaWy5Kj7JjojSHZLuVwZVd8TXJ3GRnvJZFr9HFr-uHa63yFNZAG6ibx-pRIJw2EF4YXuOxBd63okrtODehAXMTfeNfQNPLVg2QzKB9I1cYZQifxCHAQ15M-9ycIkTy7Zl_XgNhcHCrocQ2C4MG6BvTf0yaF_CCeSHM0H2VWhxo07z_3sWL7eH5fFpAKudHsYiNj3wC0JQFF4tj9ma7G26epPy_cQPz-REy_cCKmsSjyG5HuT06R0u6l0veOtoKch_wf8yshbTfqY2_p1gej4QftnxeMj0W9hhTTQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4Oa9i9ZyhH1jGz_EjkKGa_bWE2YNl6L8ceBOyeQiMAqLRCYvlJOCcuyT6zl5n5gVJFghrAWaKSBlAa_J_7kppD5lQHU7-obke2V7UniGuXy4XM8G41vlceeeFOw_XTeicF4b4gLuHeHqf3X5DazPpw_vs-mL6JhekU7zNsLa3sxCz_tHz9aA78vIPZT7N1XucdBRvdjRhbdi3xVTLljQZ5kYS3dBErRnnU2dvxZGY5EKhn7ot8CK6gFhy-2QN6YapLhbEZ-nHmWJ-Qz2FQVih6l1-ggAVghaHo5YNiVrQbEooQe0uicT_Z58SlIgVp0E6ZZCz5e5TLSvqaxSHZ0FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الدخان يغطي سماء مدينة جيزان السعودية منذ استهداف انصار الله لمنشأت شركة ارامكو في المدينة قبل ايام</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/85735" target="_blank">📅 15:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85734">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزير خارجية النظام الاوكراني:
إيران ونظامها متواطئ بشكل مباشر مع العدوان الروسي على أوكرانيا.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85734" target="_blank">📅 14:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85732">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1ekuTsnUNOnHJY7MUZ6kb79Geoq8LGorhzOdd5mjeJfH4WLWhJdtkizGYNEOln-nV8UD6XKB7MtqljNi1z79TMWl2QsZ_1E4XtCMp7UkAbhn3UNGbDwGrm1CY6ShSbYOsNv8tMhG2u8bPPhRmgKxBVGWAz6wQMkOqxwxo6R_WcDcv6_9fz5qzyKZ6oWS5zpskw-AOcDiOp-DtSxN3M-eNkTBdKq5ij4Hyan4WoTsicmubOZqdVeiNkcWQ71j-oMUshdiTq_AF83qha6rxndZznCpd_KVSrBXjuD7bCw52zCaU6P6HSvf3pXxDf_AYAls6cdqGZ_Bd_S2fv9McPViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E49nc1-bwPlS_MWI3UU0YylGxgUDPktLU-152ejmQHN64jY8QExqVm_TtLKzB6BLqvUVhfvqZdDdg_2zWZONUqQdvH401zQW-hg-0v04GINAqC8XA1vJjh162NVG4BNndQALGCkp0NWg0-sqIDeXGiw-4UzIE-K9leZCLRSIPh2LAAph6G307IEFkHWZpLTeqK5X_nzVK3mv_QKg8VkQeKB3KD55_aDrMCkECKbeFij-XMCQ41umXq5INprcLnFhqCExKKnDzAy6HJDFBnmW3erFD3ijcPfCq2jNlxP0RsgprnzxM5St4XW-MegWhAO8zB2fzuZPjlQwzt5cYIKbDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من الهجمات التي تعرضت لها منشأت بقيق للطاقة في السعودية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85732" target="_blank">📅 14:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85731">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مشاهد من الهجوم الجديد الذي استهدف مقرات المعارضة الايرانية الكردية في قضاء كوية ضمن محافظة اربيل</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85731" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85729">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجارات وتحذيرات متتالية في الأردن</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85729" target="_blank">📅 14:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85728">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc2zwJXIn73w7YRkSH0HB9FX9-rSS3o5aLrDgMJaVWw8CGVMXleae8JsGE_c1_a2xheRn3Np5abSnOmDHJ5oEylU1m4Jz-VFc2QQMrJk7HCHsCdHbbGahSKWx1YrrGK8RX6Yul43qwLvfZs5AD60vU5IDepU-LN-e1FifUNdfnPjFcFElr5M24hk-odUHjQj7_0qXH0dGueHmpw29qexOvJ0zJk2xUh9Cpb1eWHbg2chVoCx5yX6iWI28M2fsnVH_lJnDdKOdgSHEBAJj04PALTjimuNKu0TP2FO0JL3yfqNiMeyvAr_rsxIir1MlMzvt3SUVEYOC06n45N2Tm9Hdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر صور الأقمار الصناعية حريقًا كبيرًا لا يزال مشتعلًا في مصفاة جازان النفطية التابعة لشركة أرامكو السعودية، حيث يستمر الدخان الأسود الكثيف في التصاعد من خزان تخزين نفط كبير.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/85728" target="_blank">📅 14:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85727">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnR374wZRBRGsLhrKTQ7Gihf3N6oBC06MjB2baf4_N90Hj9oKFGB7MDt9EPbHXuuOmPVKdq6fM2luVZpMgQN3ARDu_Mjsv2Kze-abNdxMA-vUPYxgiLsGqVssBTiVqn9XKbZf-xdXOfi6wfnT90s9liqFggyOtyG7Gu4vvz0QVCBySipgP95_KIYTXgSxPwSO4_ILeBzyGshINoKeoJV6z1bzOKs_MmCWbUkfeJGO3AxFeD-PwW_2f22q4HJjQQZIcw6UogoFAtuy39R96gjHxO5XzHYzjxJxiksvyOUIERiY5J1z1-9TDb5hgZM8RRUiaJfHyFjqMz0Wt3iOD-cWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة تهز مدينة الكرك الأردنية</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85727" target="_blank">📅 14:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85726">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ff363564.mp4?token=YYvTOANeVtvsWASQjH7cSI_Rto7p21uwWBKqGjObeB3MPHK5doeJWt_tzMfYhBW9nrDItYwO09b2gZ1ImJlKf-E6buj0cYI7WJV7yQyktIBq60EJTilC_Jvu-7hfAfp-5Ht1ZncoGWQkR0BDylNTV_ZYVCLWEeyPzGorijCvW_LYPF0t982uwKZw2FJnXirq5mnFEsUUzNZS1T9sE693-e5jFlx6AU2u9eAhEbuWOMEx3a2VEvvNL0d44LRShwf95T4oJMbVgs52lMrCb5QKnhqc_uzHJ7xB_3JDb_huBbmjbVXioFTzHB7FdWiMhgXlXGI8vZEGBTzySMOxRD_ZianvVDQQHYM0UBF5y8l_ESkpTGhy3g_jbJYHWWX1hrIoZQQZi8ahfsDeNELsOKhqNermxIyih6PsC63UwtXa2PSyrto16lLQBVIPEklJ8GpXpnJ15PbcGhcibAQLjIqBLSag4tXpv4tiINoIbWRzBBIi-1BODOTF-OYniFVNpPRBPhjbf3xC2VFhhlflULvnTRFffznNBoliZcloEs_Qi2-9WZpoEu4RVBjC91SSSZT40V9rju13kbApm_pozQBSFJFrkb8hnF6BWwZddyWdqh1qpyl1JthsJ9WzNz20l2tk0dyWOOGVmLbQ0e3GDdO5hVqbTZnZ2h97-4ln0VdEFjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ff363564.mp4?token=YYvTOANeVtvsWASQjH7cSI_Rto7p21uwWBKqGjObeB3MPHK5doeJWt_tzMfYhBW9nrDItYwO09b2gZ1ImJlKf-E6buj0cYI7WJV7yQyktIBq60EJTilC_Jvu-7hfAfp-5Ht1ZncoGWQkR0BDylNTV_ZYVCLWEeyPzGorijCvW_LYPF0t982uwKZw2FJnXirq5mnFEsUUzNZS1T9sE693-e5jFlx6AU2u9eAhEbuWOMEx3a2VEvvNL0d44LRShwf95T4oJMbVgs52lMrCb5QKnhqc_uzHJ7xB_3JDb_huBbmjbVXioFTzHB7FdWiMhgXlXGI8vZEGBTzySMOxRD_ZianvVDQQHYM0UBF5y8l_ESkpTGhy3g_jbJYHWWX1hrIoZQQZi8ahfsDeNELsOKhqNermxIyih6PsC63UwtXa2PSyrto16lLQBVIPEklJ8GpXpnJ15PbcGhcibAQLjIqBLSag4tXpv4tiINoIbWRzBBIi-1BODOTF-OYniFVNpPRBPhjbf3xC2VFhhlflULvnTRFffznNBoliZcloEs_Qi2-9WZpoEu4RVBjC91SSSZT40V9rju13kbApm_pozQBSFJFrkb8hnF6BWwZddyWdqh1qpyl1JthsJ9WzNz20l2tk0dyWOOGVmLbQ0e3GDdO5hVqbTZnZ2h97-4ln0VdEFjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تُظهر صور الأقمار الصناعية حريقًا كبيرًا لا يزال مشتعلًا في مصفاة جازان النفطية التابعة لشركة أرامكو السعودية، حيث يستمر الدخان الأسود الكثيف في التصاعد من خزان تخزين نفط كبير.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85726" target="_blank">📅 14:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85725">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f63084adb.mp4?token=Lx85zNeISWxsV3pSr1RwJWp88d6--nXhVdJ9t7qiVeP3pRlTan6-g99BJPbddNtupGcia2v1Fk-SUSLXCzXdqsUCMJdF_eS7Df9fcMSSL6Rxlev8B4I1L6BsocshpgE478bZsGJbuM3OW8xsJcQK4l3IXOx-nIl2BPVeScHdLfbr4AEoX9PbmROF4iDFGu8H7kKRUVfQ0yrN0AHL7p49Fpfllji1ih0SisxvlH3B0op21PgDaojfMMmHdRPywaSeKiV_ck-BHNmJN7i1iDsP0efNIs5FyalsErCCKfRV9cfMDfLXIDhuGrwOwSzymcD6jvIKzLDwgmrU5232sMGgdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f63084adb.mp4?token=Lx85zNeISWxsV3pSr1RwJWp88d6--nXhVdJ9t7qiVeP3pRlTan6-g99BJPbddNtupGcia2v1Fk-SUSLXCzXdqsUCMJdF_eS7Df9fcMSSL6Rxlev8B4I1L6BsocshpgE478bZsGJbuM3OW8xsJcQK4l3IXOx-nIl2BPVeScHdLfbr4AEoX9PbmROF4iDFGu8H7kKRUVfQ0yrN0AHL7p49Fpfllji1ih0SisxvlH3B0op21PgDaojfMMmHdRPywaSeKiV_ck-BHNmJN7i1iDsP0efNIs5FyalsErCCKfRV9cfMDfLXIDhuGrwOwSzymcD6jvIKzLDwgmrU5232sMGgdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قضاء كوية مجددا</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/85725" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85724">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجارات عنيفة تهز مدينة الكرك الأردنية</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85724" target="_blank">📅 14:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85723">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6h4eJjiKU1ULDrf3tWv_Njl5bWFR84mynwZ4j2O2xhJZbPzBTQPLucF0uoe7wBCEUJiKSxce4ghDd0RY_cq7jrtj2qB68e2sFGGnLHcCL9PwE5uRRJ94U65WCCavkz3aMWGU3n6vuuH4ZHVG3BUHxJjDJlQhEGh0jsqtPpxswNiTTlClixbY4aEUPI7HBLsl4KUbbnuUP72djUGCx0rCkZBl3EOwAexqy4g7UgfNSU0UQtKvELdHDEidMO0yNs24cD7Wh79DGLiH6EjwxX6GImyEYMWqzhritMN6PjfWgcuiYsQAZl_0N3lAqTA4Y6Lb6slWegbqLpA0hpdI3WKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85723" target="_blank">📅 14:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85722">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85722" target="_blank">📅 14:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85721">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85721" target="_blank">📅 14:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85720">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/85720" target="_blank">📅 14:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85719">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT2CVEjSLqMDpyc_rZCrNFOJ9AE3RPz-bOtbqAblaLQXPc_ao7gCdumv9Exdn8GIyy2fiJWM260mDhBIDMPc2JuxCifBAel7k2Xz6P2XVGKFL1aGdi1FWGRrMxFfm2b1NG2CyrNFz51_SnHdNkhgEU_zg35MDHEJOmNQBU92rJPewR1h-maLFdRqc09vIJjmraihlETlry9q-muiBS09x8WXadYVqsXSt9wcCczM0GCHP4RkB5tzyMHPSEH4kWgEweLH1c2Qp7e6lPp-a3zmwJIlaLCRphOJY_f_3em1AhWgGbZrz8etMXrkPdOd-i5Igc-LDg6S3hUADeH2wHg1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرح شاه زوجة شاه ايران المخلوع تعلن حظر الحكومة المصرية إقامة أي مراسم على قبر الشاه والتي تقام سنويا في ذكرى هلاكه.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85719" target="_blank">📅 13:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85718">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇨🇴
الرئيس الكولومبي الجديد:
سألغي خطط إنشاء سفارة فلسطينية في بلادنا وسأقوم بإغلاق عدة سفارات مثل الجزائر وكوبا وجنوب افريقيا.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/85718" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85717">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea5c211d7.mp4?token=iHUg0x8-qoRTSQL5DwUNho1KO97wq1-PINHOOb-PhYT-363MVadwumsVmIoSPgHbjhu5CSzAJFVeuAXCTPVs22ZDM4KYky-Joi-p_ew397tISurDDTHBp53pdefpEh_AZzwjDbmX3asWC3tLCG77-VJ9FVFONvdbgz3tHsTxcyu_qU_QCtsmklb2Ydeie7x5pko1ARYXhytYXssvgbioqbVA5Pyq7rFebyb0NvzShfGPEoe78FVbtU4nNKWtQYA_GUVGQH-uPKGXyCOdbz7XbkakIiDH6keIblbqI-KPf8sViDatzPIfOc0dkH9m9HWdyoiJ27vJ-IR61f9PGywM8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea5c211d7.mp4?token=iHUg0x8-qoRTSQL5DwUNho1KO97wq1-PINHOOb-PhYT-363MVadwumsVmIoSPgHbjhu5CSzAJFVeuAXCTPVs22ZDM4KYky-Joi-p_ew397tISurDDTHBp53pdefpEh_AZzwjDbmX3asWC3tLCG77-VJ9FVFONvdbgz3tHsTxcyu_qU_QCtsmklb2Ydeie7x5pko1ARYXhytYXssvgbioqbVA5Pyq7rFebyb0NvzShfGPEoe78FVbtU4nNKWtQYA_GUVGQH-uPKGXyCOdbz7XbkakIiDH6keIblbqI-KPf8sViDatzPIfOc0dkH9m9HWdyoiJ27vJ-IR61f9PGywM8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قضاء كوية - محافظة اربيل بعد الهجوم المسير الايراني</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85717" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85716">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d584dd517.mp4?token=SdN_dToRTJ7D_pXMLPm2jGyL6w4kKhkbFG29-MUS7gJSzP_Lfi6i1z9KUW4IPtSoJrA0wMW1aphXg8D3ihP-sbtbTEQuYPrkoCArIqFU59JLF0xBjWqGW6NMTUeREYXkJia5J1_x1SjnMPDf1quIwAKuMGvXMT9rgRx624NS2FVhFP-Nzxf7DHiP66Tpw_GPwYqeVwJYTIdfgjwSIG1L32I8_xNaf4-fD4cea8FAsjCVcqlzQyuE_65XV15t0WmUpECxwq0jNLG-uNiQLO1GCliBO8YfaaxTVSCaeC8cBOcQB3xJpzHXijVq7Uo3EUnYS20tZ3Pe1_34Ao3H2rLscA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d584dd517.mp4?token=SdN_dToRTJ7D_pXMLPm2jGyL6w4kKhkbFG29-MUS7gJSzP_Lfi6i1z9KUW4IPtSoJrA0wMW1aphXg8D3ihP-sbtbTEQuYPrkoCArIqFU59JLF0xBjWqGW6NMTUeREYXkJia5J1_x1SjnMPDf1quIwAKuMGvXMT9rgRx624NS2FVhFP-Nzxf7DHiP66Tpw_GPwYqeVwJYTIdfgjwSIG1L32I8_xNaf4-fD4cea8FAsjCVcqlzQyuE_65XV15t0WmUpECxwq0jNLG-uNiQLO1GCliBO8YfaaxTVSCaeC8cBOcQB3xJpzHXijVq7Uo3EUnYS20tZ3Pe1_34Ao3H2rLscA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من القصف الذي استهدف مقرات المعارضة الايرانية الكردية في قصاء كوية ضمن محافظة اربيل</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/85716" target="_blank">📅 13:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85715">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d39458ad.mp4?token=mOOjwxbaITL2Kzo8ZUe9gE4ulSNhGizKnyVWuRDPeTLdqCOxtHPo8BPtSNC0Lp3nuZLbwOQXA_9hU4YTCu5nByRKBZbAsKg-2Sm-L_vmQb3-7h1UGo6Qe_U66IXkf7_IjULcsY9Xz1d8GuB8xIm6-Cd-3ZGqVrwtxuA-TgC_piW_h7u1pByYzZ0ZTOWbsNhup_Ujyz_rKTgmWbr2BltP_jwHTIuicuE7KY5kwKNaW3nRc2tRVi5W1tYeVwK3y-1SpATH0yTsWOjfqJwjDWD-H7JojjWraU-aKcqLPJyKUJixIZxduufXl8h-VeiruD1E3OeAMFSdVDUFYo6nMbNOdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d39458ad.mp4?token=mOOjwxbaITL2Kzo8ZUe9gE4ulSNhGizKnyVWuRDPeTLdqCOxtHPo8BPtSNC0Lp3nuZLbwOQXA_9hU4YTCu5nByRKBZbAsKg-2Sm-L_vmQb3-7h1UGo6Qe_U66IXkf7_IjULcsY9Xz1d8GuB8xIm6-Cd-3ZGqVrwtxuA-TgC_piW_h7u1pByYzZ0ZTOWbsNhup_Ujyz_rKTgmWbr2BltP_jwHTIuicuE7KY5kwKNaW3nRc2tRVi5W1tYeVwK3y-1SpATH0yTsWOjfqJwjDWD-H7JojjWraU-aKcqLPJyKUJixIZxduufXl8h-VeiruD1E3OeAMFSdVDUFYo6nMbNOdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قضاء كوية في محافظة اربيل يعد الهجوم الايراني على مقرات المعارضة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/85715" target="_blank">📅 13:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85714">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef8516a257.mp4?token=BqBvfLqZDs93u50zuU8adkWuxip_Xf-kddfYpC3GODhJJXu3Cs4oES2gO2LI_ggz3LOQxlibDONujqOozpgfLcTMbeBrFWKTFuUfM6hQ0HyEfOuA8fFoHsgTGUon0q6VUjOWyRJVoWmw20OHGzUNxz0w-0IzeUPSWR1CPYbnsuABXWznS3evLEDcr4nHyZDFswzFSLs0S0nb5_UNfbp2JaadZG2exnb5Dtv01E_XmVyIoWUPFTAdDtNpjIT2UZImmsmubBf9-_xIcqXST7za0uliobQ-CntJq56nSrrf8SDC2YORXITmu5XB2TN6Ne0jK00L7F3XmEh94Jq5_Kz4Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef8516a257.mp4?token=BqBvfLqZDs93u50zuU8adkWuxip_Xf-kddfYpC3GODhJJXu3Cs4oES2gO2LI_ggz3LOQxlibDONujqOozpgfLcTMbeBrFWKTFuUfM6hQ0HyEfOuA8fFoHsgTGUon0q6VUjOWyRJVoWmw20OHGzUNxz0w-0IzeUPSWR1CPYbnsuABXWznS3evLEDcr4nHyZDFswzFSLs0S0nb5_UNfbp2JaadZG2exnb5Dtv01E_XmVyIoWUPFTAdDtNpjIT2UZImmsmubBf9-_xIcqXST7za0uliobQ-CntJq56nSrrf8SDC2YORXITmu5XB2TN6Ne0jK00L7F3XmEh94Jq5_Kz4Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من قضاء كوية في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85714" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85713">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moZpA0Krrv1atV3Z_mpZK0gqeKxgOu7dXoBB0JTDnhcwR1OcPN-mBmJz4tgtnVD11ZkiXf3pCkzRTh231_rw6qe7fIdZjIOibPf823O5TzT4l61kqvUPj7_RsTr-dbzA2JJRH74WPwM2DI1gKx7EW6UgYmpJj0Ch4MRc5Qae4IzZBYIap8jJAosygYzHei6Q_MbCJzPYHcAE26Rp6yPCXiJ_RzLA4IePUDU41q2TsJOgmNzbUPbsivm-J5u03LZ3YWicCuXs4Kz1dXMkIZPVXJZxsAFcFjDoPt01IHFD9NvESE3GS4OUrwx_13WC1ZuBfGBiwLe3r4pL2tLvBvsKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85713" target="_blank">📅 13:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85712">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040b3d9ed1.mp4?token=NJHquqGqlFZ0t9XqXOUB6uKaDC1WmrFJzyS-oEW3blvTRt7J-I0FBLkpO6ChiEG1AjEgWsV5aw6066k_4Z6wEc4Q_HYKq1UxkahfXHYJ6pB_Bqd7J4wL97Liyf44KgldM254A5Kic9b30CS1TJ23zyJmYYkbOkTiIzNmjqkIVbrAYNpR2IKIpfsOzM6_NqrPkZmFz5mw9EqQZNW9vkkYz0Zrzw6ccGR6ch4hJHOvNu_V2Te5XKqbPVEzHt25_3QR5BB1zAGFbhZ0oJkJZ72MzgiO0__CmNOdg1E0ABG-sAJOaaGNX4ZGs2j677J3eoVTzZSKkgWOedz352mkHNWapQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040b3d9ed1.mp4?token=NJHquqGqlFZ0t9XqXOUB6uKaDC1WmrFJzyS-oEW3blvTRt7J-I0FBLkpO6ChiEG1AjEgWsV5aw6066k_4Z6wEc4Q_HYKq1UxkahfXHYJ6pB_Bqd7J4wL97Liyf44KgldM254A5Kic9b30CS1TJ23zyJmYYkbOkTiIzNmjqkIVbrAYNpR2IKIpfsOzM6_NqrPkZmFz5mw9EqQZNW9vkkYz0Zrzw6ccGR6ch4hJHOvNu_V2Te5XKqbPVEzHt25_3QR5BB1zAGFbhZ0oJkJZ72MzgiO0__CmNOdg1E0ABG-sAJOaaGNX4ZGs2j677J3eoVTzZSKkgWOedz352mkHNWapQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرب مسيرات يهاجم الاردن والجيش الاردني يزعم اعتراض مسيرتين</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85712" target="_blank">📅 13:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85711">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سماع دوي انفجارات في قضاء كوية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85711" target="_blank">📅 13:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85710">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/85710" target="_blank">📅 13:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85709">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85709" target="_blank">📅 13:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85708">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇶
إقليم كردستان العراق يزعم:
بعض المسيّرات التي استهدفت أربيل جاءت من الموصل.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/85708" target="_blank">📅 13:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85707">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gae1fYeyVxpXuiWhQ3mm3LfDiq3lOiGRrFmXNJ0VRL97gkWdnqkJo_8yvUEOYlpBzmMWvY8NvqAvllTjd0ib-aeiOGG-55WkS8LJ7Cgw_hqEbLsUVRnCfEgJufPMYvs20-1Z-a16wjeDb-4a8zmkQ-UIRRdBxF2uLmenI0cchO5DmSYTn6_Lr9Kaya-ycppOQtJvh7ctnNwEiNPxXebkr0ME_N1oSq845tmlFH72-hf0_E0wJjYq40zAlwfiNNk-JXNTIt115F_6NuWiPQCD4hGBxQzv_AbpgHTWocqntPpFSVrBCbLHhOxyCC0rx8P0nWlh7gwgDVwdXL8kfbmQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85707" target="_blank">📅 12:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85706">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/85706" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85705">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA_zUCKW1SbQeTNTlG8TXIY8J7Hym19d84UkyVIPU5l-zVpR2Bj8jMsmS3K8bqvVgbXtkGyE2vFUKCRsg35xly3ADs4WkwbHycc3F8ORaSp5NDHu-zeSHIrHU5W03LOy3FNj4es_dRZ6RRB6oMTy6kT3ISDoUwDPH1081Vm6op_eGzTjcRnD8K1iZs0xXY59IRBPbOg613vso2esLP-YctaVYiYLH-kkhu1LrXqkhStxaE4AqcGfdVUDXrzSXpmE-2bGSA3jN-9Bvlif172i56Ggt22n8t7hCbEsiwEkNPiX6VU8SvIkOL94ISC7oNUxVO-HX8pgixqtMHOxEpVEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البحرين تعلن اليوم عن مناورة عسكرية واسعة بمشاركة دول خليج فارس</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85705" target="_blank">📅 12:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85704">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏
🇾🇪
🇺🇸
🇾🇪
رويترز:
استمر تراجع حركة الشحن في البحر الأحمر بعد هجمات الحوثيين على منشآت النفط السعودية في البحر الأحمر. لم تعبر سوى 11 سفينة شحن مضيق باب المندب يوم الأحد .</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/85704" target="_blank">📅 12:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85703">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOfSfRt-wXTHsUaYcDX0lbQUYN_V9vAf3c-ZvIa5699rOSiLjjOk9xIl8RUMlqTZDcepgE-6kKBnXkLYB1BY15GyvmwUNe96Y-XBPf33Rf9h232KOyNoyfnaRBv_yPkeM5GE6GLfitJPctorNmZx6k2gvUsooB5jItpVvz8SZHwA-UC70P1LQxOcSpwe6BSliVU-80n1t5w4O7JkTkduikBWeCZYF3sqSNAvAproGVeqmaVBhSQwRVlfwZ4n1ka2BS_VqvImqL8ULJx3gYnp7gSFVICA7-2-859yngxZx-syPRDPixC2lj2o3fPa0UbtRv3h1E1rHQ6G-1eQzoFCMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوي صافرات الإنذار بالأردن</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85703" target="_blank">📅 12:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85702">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوي صافرات الإنذار بالأردن</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85702" target="_blank">📅 12:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85701">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpA81VqF1mRvv6IwgaHGqGONtWgfFFkFJcvgLSP-YUu9q-I6zgYMfOUyOe6qOYjocL3USI5CHimVeDRHoEZA4IeIQpqyprKi3ASTyTFNFzcnybjmnBmNWL6W-f0VTaTR57ONSEHOtIeFpODtwOcMnqkg5gg0RBFsd7FLDZ3KUWpdJx_pW8LkwjQvDlfVxneZQ1b5F_VjC6zyi8wud04UemuR09SqZ8dOcoCVhLvOWYodorEcChGa521HrwKaKl5PyHfMLJYOxhAVX4M3IgfB5xvsMomthmRv4fuu9N8XAlIQosQEcD5j77BnGXEVjiI9vb5M-YpfzrFsGpW_Vc8yVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
Bibi ass-kissers</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85701" target="_blank">📅 12:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85700">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
🇰🇼
بسبب عمليات الهروب والنقص البشري الحاصل على خلفية المواجهة مع ايران
الكويت تعلن عمليات تعبئة وفتح باب التطوع مقابل مادي داخل صفوف الجيش الكويتي .</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85700" target="_blank">📅 11:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85699">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
🇺🇸
نييورك تايمز :
‏أجبرت الحرب في إيران أسرع مستهلكي الطاقة نمواً في العالم على البحث عن موردين محليين جدد.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/85699" target="_blank">📅 11:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85698">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTbHrjKLMJ_yOASS57kvL6zQJosZyEb6y6zcSfgRH75v6bdV342dwc4_NE0oqQcKMjGFQYaOdBeGQykQG3i2xEgVsl_fxjV1q573kNyPMxfi35E61T36w48KOK1Rka0IkCQTYAM-uJZo5FZQc0qAdMVZ30iTC27MAcMFIqUuAilOlHKT0P0-3jHiEeTWj8tqd-u7Hy5QNlITws4YSX4dCMJNlis1aycUxAzQXVvPY31ARp_Sco8Agzwk2W3DNBa3DTImwz7pYOi4cVskytaHe04jl3nYYU0vWwrENsP7gM5h6SF37vVqET9a1SK6ELpJoFZLCqGsalDiC_Xn_zgFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇺🇸
القناة 13 العبرية: نتنياهو سيتوجه إلى واشنطن صباح اليوم.  وسيلتقي بترامب غداً.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85698" target="_blank">📅 11:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇱
جيش الاحتلال يدعي اعترض مسيرتين فوق الحدود مع الأردن قرب البحر الميت</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85697" target="_blank">📅 11:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
🇮🇷
هزة أرضية تضرب المناطق الواقعة على الشريط الحدودي بين شمال العراق وإيران</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85696" target="_blank">📅 11:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54f7f1637b.mp4?token=PQaV-gEcqPxAIxZcan_XQK1GQzhcRw-vWjrsiMS_9kZHYnSMuM9mwHVC9SxCB032pvtVAjIa124Yvfpjqpl2yT3CFrViU5rjfUte94_gE6GVFDdJD9TFwjT7OkCSLXJZYnoCRaAVKlDZAAgGHgTf572zv36N-IVzKu_wvetJivxB7-3juLFdgtAs9otOmYl6C1p_AafuJ7zLcVVp7IDfySB2EY_x171xIlleltVZE-NSZOv4xZBoGuSWW20j8eoX2nO3fMJHaxCLIJGT8-bSomGApbCKMn2GEamyGpqW7OeDTwRpBN3qppJRsSVrHkKM2oN3wiVuQF4D9w0ZhqPhMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54f7f1637b.mp4?token=PQaV-gEcqPxAIxZcan_XQK1GQzhcRw-vWjrsiMS_9kZHYnSMuM9mwHVC9SxCB032pvtVAjIa124Yvfpjqpl2yT3CFrViU5rjfUte94_gE6GVFDdJD9TFwjT7OkCSLXJZYnoCRaAVKlDZAAgGHgTf572zv36N-IVzKu_wvetJivxB7-3juLFdgtAs9otOmYl6C1p_AafuJ7zLcVVp7IDfySB2EY_x171xIlleltVZE-NSZOv4xZBoGuSWW20j8eoX2nO3fMJHaxCLIJGT8-bSomGApbCKMn2GEamyGpqW7OeDTwRpBN3qppJRsSVrHkKM2oN3wiVuQF4D9w0ZhqPhMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
مشاهد من المصنع الذي التهمه حريق ضخم مجهول بمدينة سديروت.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/85695" target="_blank">📅 10:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24b240f40.mp4?token=LGcVG07G7OwfpmTyzjfuOdwHesIyxONqUvPMUjhj-N8RMLhaCsRUtsyrSGInexv0k3yqAepesmHL_bfQ3eNf1pB6tCe4awNfIw5CLcD9nQCGgYh7XIbkKvPufaRzhyj6wJahnrh2RVec8NtiMduiBT6b4u63PX7YvN3NayXle2RHB4UQgkwlA5F7DhVARgPwNd6TtQhMznrmx8o43WBnjYBoa50gQMbSx_pHELSept9pKrwUPfuhENtLMCCuuhk1ZoJokxfO_PFYSF59rXleuc-pL9qgkriCpzG6CWlrovAWpbg5ZP-JhdIjdI3J7fJzniRmKfPrxlzNLXQhJIS0Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24b240f40.mp4?token=LGcVG07G7OwfpmTyzjfuOdwHesIyxONqUvPMUjhj-N8RMLhaCsRUtsyrSGInexv0k3yqAepesmHL_bfQ3eNf1pB6tCe4awNfIw5CLcD9nQCGgYh7XIbkKvPufaRzhyj6wJahnrh2RVec8NtiMduiBT6b4u63PX7YvN3NayXle2RHB4UQgkwlA5F7DhVARgPwNd6TtQhMznrmx8o43WBnjYBoa50gQMbSx_pHELSept9pKrwUPfuhENtLMCCuuhk1ZoJokxfO_PFYSF59rXleuc-pL9qgkriCpzG6CWlrovAWpbg5ZP-JhdIjdI3J7fJzniRmKfPrxlzNLXQhJIS0Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
مشاهد من المصنع الذي التهمه حريق ضخم مجهول بمدينة سديروت.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/85694" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJQzf_AUQ9tvTgH9LoVi1eulflgDEaZnWGaXsbzjTw2-YYiYxDRq6KYoBF4zxxxNkCTrXxq9OEEwT6xgNuthzIJ62KZyTkrZ9pcKon2fPPoWSyjxTrgYnZdJVP6ZWYzkk1APpBus5uL1VTMQX77vsogyvWnawfhkxp_ewHJHCM3d0CqHW5-HL19EHnaw4yl71tLe3vl0rBK7qpV67cSL5p9BRBfKNctk4sdT9KpZmaRDjFsMgkIkulD3RD-YFAMtzTKdppComYnKNbftOVF3H1crCxAT_QVnWX_sbwlctoO1uRkzpqsBEOzqsdg1chLSFtOkRpESgsyS7OD5vLPMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇷
🇺🇸
بلومبيرغ
: توقفت الهجمات الأمريكية والإيرانية لليلة ثانية على التوالي، مما خفف المخاوف من اضطرابات أوسع في الشرق الأوسط. وانخفض سعر خام برنت إلى ما دون 90 دولارًا للبرميل بعد أن أشارت إيران إلى توقفها عن الرد وإجراء محادثات مع عُمان بشأن الملاحة عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/85693" target="_blank">📅 09:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34f364bb1.mp4?token=IJO6XWVmMpKYbqHUJ9t0cWKlMB6HwjXrcZadMbBJdaET_b8-mOHEaB6OWk1h-DP45vzgPkTUxTi8-EHKh7fSLHrlINzfmd648ZJx6IGi757P7y7RSiH2MecSchziWm9fhXdl4mhiN20x8Fc6fo-sbPRoCneva9QTeavFyDR-zhr_ucv2z8K-0oYgvlhflo746yzsFS2fVI8f-oT1OFT-NBsCmZ0_RPJYFF29Kg4WDzxIR0qridpDVWKj0fWxhw3sQwrmUcT6HChws3jC9BcowcoqpwkJ1GSmn5kxQ9a45iSUZKHuZZPaOar20o9ZAx4uV8oFFtlLFXd8oqjgYzmeLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34f364bb1.mp4?token=IJO6XWVmMpKYbqHUJ9t0cWKlMB6HwjXrcZadMbBJdaET_b8-mOHEaB6OWk1h-DP45vzgPkTUxTi8-EHKh7fSLHrlINzfmd648ZJx6IGi757P7y7RSiH2MecSchziWm9fhXdl4mhiN20x8Fc6fo-sbPRoCneva9QTeavFyDR-zhr_ucv2z8K-0oYgvlhflo746yzsFS2fVI8f-oT1OFT-NBsCmZ0_RPJYFF29Kg4WDzxIR0qridpDVWKj0fWxhw3sQwrmUcT6HChws3jC9BcowcoqpwkJ1GSmn5kxQ9a45iSUZKHuZZPaOar20o9ZAx4uV8oFFtlLFXd8oqjgYzmeLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇴
🇺🇸
لقطات من الأقمار الصناعية توضح تدمير حظيرة طائرات في قاعدة الملك فيصل الجوية في الأردن في 22 يوليو، والتي تعد مستودع ذخيرة للقوات الخاصة الأمريكية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/85692" target="_blank">📅 08:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69826760c7.mp4?token=JVnuKekJTnHvb-2pZTYJBpSXyjGz8uiGR1KEf0g5vc3x4NjaLmxZQtCIGrQz8ZJBNcxXevGGHVTJA1m-ly1CRSzEPVMnm0NEeBXn8iU_R_pTqJb_q6j-iK9BQRp-bnWlwg-IFk02kn-ZsH8dQFdvt9bW0dzkPF6UB1YGbcI1JOM6cTck-7PjJpPKVSMwgAsPesAoF75QJxEKhIu3N0cGVnOuOMqsLQXkxA6mlO2hal6NFQoCNIfZUNvmh1B2NRt48ydQw2H6brdPaygmJItfnEHozN5xMAOPb-NjPJoZKT4SPvxr70du_lHU9P6UJZjlcUM-dRU3f7KU_ePLWOeRBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69826760c7.mp4?token=JVnuKekJTnHvb-2pZTYJBpSXyjGz8uiGR1KEf0g5vc3x4NjaLmxZQtCIGrQz8ZJBNcxXevGGHVTJA1m-ly1CRSzEPVMnm0NEeBXn8iU_R_pTqJb_q6j-iK9BQRp-bnWlwg-IFk02kn-ZsH8dQFdvt9bW0dzkPF6UB1YGbcI1JOM6cTck-7PjJpPKVSMwgAsPesAoF75QJxEKhIu3N0cGVnOuOMqsLQXkxA6mlO2hal6NFQoCNIfZUNvmh1B2NRt48ydQw2H6brdPaygmJItfnEHozN5xMAOPb-NjPJoZKT4SPvxr70du_lHU9P6UJZjlcUM-dRU3f7KU_ePLWOeRBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇴
🇺🇸
لقطات من الأقمار الصناعية توضح تدمير حظيرة طائرات في قاعدة الملك فيصل الجوية في الأردن في 22 يوليو، والتي تعد مستودع ذخيرة للقوات الخاصة الأمريكية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/85691" target="_blank">📅 08:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇱
🇺🇸
القناة 13 العبرية: نتنياهو سيتوجه إلى واشنطن صباح اليوم.
وسيلتقي بترامب غداً.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85690" target="_blank">📅 08:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5a2448065.mp4?token=dg0WJYoY8AAUwDcFzBzkfGCLbqEA7VTkP-FkaLCRGCszGly6JhF9u9nDkqJTfkR_Q5W_H98J7BpqsZXdP7CV_QCpNb7Ik4E3EDxJA64-zF7Kf5dirIynoDjyTFcBs5D384Mtl7QTZcoC2lPyS81ppOeVocQwWjR3bE_ab27gh6WJ26znN0RcyNiA3KNMHrqIpa_NdzbT-ZGGbIy_NVoKE5oNFBkl5C0p9rfpeqMu0EnuWcUsw8que-TGLJXaJaL4uDIfTY4ZqrnO7zwuhI_NuqU8Kz3ojpRJSZku9EHrWA0Rd_Wmfr_AKMZ1RdLjSR5kDVRwui5OInjldNA7RCE-ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5a2448065.mp4?token=dg0WJYoY8AAUwDcFzBzkfGCLbqEA7VTkP-FkaLCRGCszGly6JhF9u9nDkqJTfkR_Q5W_H98J7BpqsZXdP7CV_QCpNb7Ik4E3EDxJA64-zF7Kf5dirIynoDjyTFcBs5D384Mtl7QTZcoC2lPyS81ppOeVocQwWjR3bE_ab27gh6WJ26znN0RcyNiA3KNMHrqIpa_NdzbT-ZGGbIy_NVoKE5oNFBkl5C0p9rfpeqMu0EnuWcUsw8que-TGLJXaJaL4uDIfTY4ZqrnO7zwuhI_NuqU8Kz3ojpRJSZku9EHrWA0Rd_Wmfr_AKMZ1RdLjSR5kDVRwui5OInjldNA7RCE-ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
عملية إطلاق نار في مدينة "سياتل سنتر" بولاية واشنطن الأمريكية ؛ إصابة عدة أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/85689" target="_blank">📅 05:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭐️
المراسل:
هل أنتم قلقون بشأن احتمال قيام إيران بمهاجمة أوكرانيا؟ لقد وجهوا تهديدات بسبب ما حدث لسفينتهم. أم أن هذا ليس مصدر قلق؟
🇺🇦
زيلينسكي:
إيران هاجمتنا بالفعل من خلال تزويد روسيا بالأسلحة.
يجب أن نكون حذرين. يجب أن نفعل كل ما بوسعنا لتجنب فتح جبهة جديدة بأي شكل من الأشكال. ولكن يجب أن نكون صادقين: الإيرانيون والكوريون الشماليون هاجمونا بالفعل.
آمل ألا يزيدوا من هذه الهجمات، ولكن يجب أن نكون مستعدين لكل شيء. لا يمكننا أن نثق بهؤلاء الأشخاص لأنهم، في بداية الأمر، وبدون أي تصعيد من جانبنا، قاموا بتزويد الأسلحة.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/85688" target="_blank">📅 03:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7655e9ea63.mp4?token=vtO1WyjLnvpmtmPUqsk7DzLwAZIVgnyuHlMn1KJr6bB94GFamu5oxdUAufrTmiR02JBLcdgNWxy9JJRYlwqgpH5RR7OFL0cjAycrzQt6SLkOSi9i9VXaSjNf5hoTxZAoN5AxEFNGLA9Z2KEFAsQYNnuucvegAUrE7qd3-DnIF_2ysdBqmo41wXri7-fDty3e7P0ev1mn7q2gp8neiA8AFkUlBSkJ2zMvY3U_NjWajHIC9Xw9JReCkXQ3GKmg0UtpbegfUTvwCVyo7ePfSQSlW_MNHrSkwCgRns6VUmP6qcZRjuIvwBky26PaUipwbQOwU--nSkmHWPoJX-aAWv-0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7655e9ea63.mp4?token=vtO1WyjLnvpmtmPUqsk7DzLwAZIVgnyuHlMn1KJr6bB94GFamu5oxdUAufrTmiR02JBLcdgNWxy9JJRYlwqgpH5RR7OFL0cjAycrzQt6SLkOSi9i9VXaSjNf5hoTxZAoN5AxEFNGLA9Z2KEFAsQYNnuucvegAUrE7qd3-DnIF_2ysdBqmo41wXri7-fDty3e7P0ev1mn7q2gp8neiA8AFkUlBSkJ2zMvY3U_NjWajHIC9Xw9JReCkXQ3GKmg0UtpbegfUTvwCVyo7ePfSQSlW_MNHrSkwCgRns6VUmP6qcZRjuIvwBky26PaUipwbQOwU--nSkmHWPoJX-aAWv-0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالطيران المسير الإنتحاري يستهدف القاعدة الأمريكية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/85687" target="_blank">📅 03:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوي انفجار مجهول في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/85686" target="_blank">📅 02:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوي انفجار مجهول في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/85685" target="_blank">📅 02:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
هزة أرضية بقوة 3.2 ريختر شعر بها سكان محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/85684" target="_blank">📅 01:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
🇮🇷
مسؤول أميركي:
لدينا شكوك في أن استئناف العمليات العسكرية واسعة النطاق سيدفع إيران إلى العودة إلى طاولة المفاوضات.
استنزاف مخزون الصواريخ الاعتراضية أحد العوامل التي جعلت العودة إلى عمليات عسكرية واسعة النطاق خيارا محفوفا بالمخاطر.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/85682" target="_blank">📅 01:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85679">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ze1oJAYnbF4j1kzxxxqvSgz1Zjpn_uFXOonLpGhYVTrU-pbdNNtAWTSbEuJbTwI_GJyj_CAnKDEhg8HeUAfJ6AvzJ7V-xvzRLBvmpSMngxRYePzdv4c1iw0P-sRcscQl_m98RV4mMFN9TA0QeFTBgDSCMTDpwnvJqiVLJwA1UN5VXCcxxYBsOgHcW0Gz-laaiBrL9HoAMkUKl7rneLWWiz-mAhzZ4TucRY3lvaONPAWByPQQyb7AqDxRmSvndMc_JXmwWbD3FQyvfxhfDD2NjCQnxQDn8xiPYicyM5mvubR5Z517yvIyK49JB4q6GmP-vJjRldoiih5otuev4UF9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQDKGW0ftt7Eg_15hc7bsCDHyeE2E5Hv6kNMqAfpaaaajPjz_IOye89cRS8z5Z9dfWPqiKH1H4WRJQQ2JITgMyRkBfOGC4gVxwMslfWgDBi6SBDEzxH5nKHNKJPKyH7fhNzXesNMH4u-krTC58P_xrxQ01gxLe3XNY0VKYR8qUIbR-bkhTA1ZLrVQBwljf_VkEYNQi3l3mqE95OMQ80u0F9ooWhlVx-Z0TjTMUWqk_Ucy8sS8AaASpGEftTn5prCoDsuda3EBQbl9dPbos4lhsMU14mA5065FdqTviQxIrUN3ES9KUmV0anrnVbulBBJ5nHX8CsadHgsxGeNLrtJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWlSeGWMwtB2oSVFfDnh9pk9haFvR22e7iMZ8y23WeDaMQKIo-3zp3TG1zEdtHpcRbOi2r-YrsOM0qPM5BGkh-Lxs_gtMPO8sNov02ZjgV40LWMal7F79ywh7xXOhJdP2Jbpqt8Vb3LCLuDlIybVJu-Gmz6vqLru8ENQSsdzX4kZIrjtiVW7B-1XcOu-BrUttyVG1K9c74lCJygvBiaKTg7A8ibeTzCKmhgY0VEgVh4gvEDUqgN-VIarT1OiUEMRMkcD9rkDTzG7wHvlboY7R1GjSy7JmJ0m2aU2Z1LE15PCDKWVMKPJlUKEOs0E3kCUaddEPWrt0MzES5MkvnnppA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😆
Please set an age limit for ChatGPT. Some people couldn’t succeed in real life, so now they’re trying to succeed in Photoshop.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/naya_foriraq/85679" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85678">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">😆
Please set an age limit for ChatGPT. Some people couldn’t succeed in real life, so now they’re trying to succeed in Photoshop.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/85678" target="_blank">📅 23:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85677">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9tj3_hDFRE_AcQqqZk81JRId-pKxzZAOA9hybLE7WF-9sEGx52hHOXmagCM35sq_2Da2mFv0C5QptSAIRDnFyUy9wHBiZc0gBNjzNikl6FmdFCFMZjynsHiHrmSY9-YXBZ0qL7k7w_OOsqFyl-_k-d2N0MVg0IC06yu99f1C3flAfv84H9wULI7DVy76naF0w-IA5zfNw2T7DYlZ-f1ag_fsMq1n9weEzG0zw8XdfN0c-bFbhC6HShzcq29TiwBqRVKo3GBjYNe30JW-NxctDTv4Ebg79XIlsSqTBF_fjiVdtAlZbsaLAckrzcylPJE1u2n4Rtg4ECalgm-hzp6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: أشعلوا الرعب في قلوب الأعداء.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/85677" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85676">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqdMbGqk9v1N0BkrigeLau-emKnrLfHDBfmzsDznC2Z4NRGdq6sP6xEQn4eQtjNdJfgAQQZIBRP22MZTuvJGucqkbp0CE_2c4B_A6-jnXiPlowxWs-dUR2Jts74iGFj7iVrmOhWDX5d7jPMCfQsx1wsaLp4ZE6-6xVqsqFjHOSDeUk81r2AbsZJf-8TjX5Ox_eGnFPdFG2Z5xnt9VM_seovAgD3RxZ-NRTWEX89qtDGVsqJaUaBA5IwwIddsXNgPL6cewh7UpXDf8CHVh1S15ItnRSF2jM3GODpOl9ATSMdrnUyjgVLFpz5sf72HB3srVDh_QdSWeWGYb36YEQEHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: أشعلوا الرعب في قلوب الأعداء.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/naya_foriraq/85676" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85674">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ib8sI2h0OloAKNN5IWzyKMelr49w-v0SkKapaFJwdTU3BH07Zb3DmZu7CKyxTWuUKq85AeYfsXyFoWSRGBHVrv6DzIZr5irdshpUs7T1cjacY0255HLA5b7pGCuGsxPI-CGIPY-mMySvuUaFAw9I8ZF11OFht5b1ohUVEDr4i0Fd9QNjFuU_7p4TaYCXlJYLnWuUlUsF_kpcr2Pk-YokrKzQMxWCyBWICw9cb87SPoow3QHRuBOedBLeX0TujLtUkDfO5mUppcrlfMDTaxzL4yeYe_cNYNkQ9pOur6NmrXILBgwOwRB_Hwg_2FD-5Oj_f-D0dYFYrRresfjbCVl8UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rp0R22QwX05WXRGQ621KxFj5dIbFBmhAYJ14zwDdQEI-Qd-M5OrArwEVdrwc2S8k5PcVB-KXiXLGFgcSchvkVQESq5gN_tnCtPnXMJ4X7g5hKA1NwPsVkOw7Q009r_z_7k3XrMaDEyb5JwzO5wK9f91r0FgHzwt7CsZLSS8hXjMRh0d_rpsqHSqGWbgew9CFWGm5tA2Jgx8a-j5xewnTfVuhvWqmdT0Ka-ogD0iHAoXgRxsLGf4RZUNnyv6yzGByqlas6RLSRwgbtPt_Yw1Lpaop96eBeXQLOVfFzKyn1z9Vy4AlEr0fppqbPWQ9JVxstEdvFqfuSlDXFYwePjVx9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامب يغرّد بشأن الاستيلاء على جزيرة خرج واحتجاز سفينة نفط إيرانية.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/85674" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85673">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇱
إذاعة جيش العدو الإسرائيلي
: أطلق عناصر الجيش الإسرائيلي اليوم النار اتجاه طائرة بدون طيار تابعة لحزب الله كانت تحلّق فوق القوات. الطائرة كانت تحمل كاميرا بغرض المراقبة.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/85673" target="_blank">📅 22:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85672">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
🇺🇸
‏
الخارجية الايرانية:
تبادل الرسائل مستمر بين واشنطن وطهران.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/85672" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85671">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
🇸🇦
‏
الاعلام السعودي:
رئيس الوزراء العراقي سيزور السعودية الخميس المقبل.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/85671" target="_blank">📅 21:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85670">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇾🇪
مشاهد إسقاط وحطام طائرة "بيرقدار أكنجي" التابعة للعدو السعودي التي تم اسقاطها أثناء قيامها بأعمال عدائية في أجواء محافظة الجوف - 26 يوليو 2026م</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/naya_foriraq/85670" target="_blank">📅 21:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85665">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqfLV0bZBOoJPe6qzQ7i68qtq2Rgr1JBRDE4rwHjXHTBzy2g5CDR4NPGUkC8yTFF57s5244tSesdubQdmFWztlVT7A_n7s1Cuw-aw8Ifu_HZL2OgIvHrNpFwvmlHckU5i-m0wQA625gdu5y7ZSU3AC6AZw6XDQAkFrFCD1dK8InJTTUom-Q96sGVu-KPwroWthM3-dH_hWvrp0zFEP3pi8asrC6tW7_s0EgMgIay0gP56pjqS2UPlA5hMJ3y1gXtNn-lXwcbMwIiH2Vck7mjjvp6q2EU5FNdSsImFDfJrvsJ6uqURpqeNUVEMsx5AKdkBhbwciaqhEdBwTTlJB25Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRwdYOuv9J8d5te1k9zgKCCgVhhLJN2VtiP_3LO5Bf1heGzIOUDK2ye2O3sB1yDB77gyhO2voztynAHyayQuyGxkbgoiL8PIOD7Bgr0oefDJ8RL4aZnLBBZ7wDVvwLnlJJXXZy4dEXISs3YheBnkMZ7irs7egOrWSg2-sBWNDtxcKqv569tR-29LGwGjYSfwHUJcP23J-ZdEn8yB1dITMaKD0DjqQR0EPJWOuHhWIhlDepEyoJNI740bJMw2xWioPY_9_9727lE46HnScdDHWa7T2rRXwQixECV6t8wwTalHsgp3JTaKoqZDSaVU-Ao7esiYfWzTVC1UXV4uUrPz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojbJmImjp4m4JaAVHAiP-ywNL6_1qxxlP9GaFdqMvys2sLWXn8OBGavkBkDny2hjl6toO6b1kgj2V6ri0oMn_LT9_L_-pno9B0FugPm145AUsR2xcoGKJ7ogYcdyXiuhC6x5lwg0D9pDyl64doepyzajyPeIP4v_aF-2zwzjVWbQSmOH0ueHad-d6EnmUDjlgYcl6180QmfEqpVZS5OqX4ldKOkNVLGdo2ntpT7uBdMXeicJabwEK1jqvZ2oH3vD0-8fUzDYGJlbhU7bKVTqGtwncGaT21NnwVY9zaRzL_dLYzEUGMKvxYMBbSFdhu4BMP8KvNCEzx-cJ-GNNhYI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9xfPiBP-dF3ycEwQSa98rECNIldPcToIJxQO7-yzVoSgF1yJLcetikK1bl8ocOfv6QfSP9ChD9bngf5FGYc_PTOtvr-0d2z4aqw6cOo11QXKEjjktnJIwvXV3ecFi1MEcejWAqSwyeTLkxUg0Jeot6zWSMtuX-Advj2k3AKwy500v9G41hq5Y6Xu2wb0-ojHeunFve4QowkmlaFEqbLANTEywLpWiuc-6YbJ9W1q3OUcmg4gpUOVZCC-ugT5tlAXkckbyuMS39rfT0uiebzsdK0ulgkt4bTgQ3TgQ-hluLdGUMZ3OU-2BmvGHpn1Pv_1VsULTdwRH02hdMPcPTA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZ2aMECOTwyXvYfZGM1NnUkyAxKKoPgPJ_UY0JEosez3SrzcA815HPXE45McNAyjSU9aPdA_44_YXYrMIrXooPRjHV3Wr7E92dnnMktKy5HUdTdvo8sMENJQHlKs9SROYYZtt5GRykXkMohKALAht_LiWiC3mjgnNHZqVFvdxXYXDS_xbcVTRNy3p4jE0imssKPTqScMUaHOAz7g63NBK0Dc6GrgHivPAHL5SEGQ1j0yeiGugGS8BDERDKO0e82AOKeRNK9pnO1XtNLL-3azwroEI2J_nHcnz5n_uT4DXVbE4-QPWScqHhdGR1PU4OUnUI2TD5GS085AMrTQ8ZxsLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
صور من مشاهد إسقاط وحطام طائرة "بيرقدار أكنجي" التابعة للعدو السعودي التي تم اسقاطها أثناء قيامها بأعمال عدائية في أجواء محافظة الجوف.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/85665" target="_blank">📅 21:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85663">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
🔻
رسالة إلى القائد آية الله السيّد مجتبى الحسينيّ الخامنئي... بسم الله الرحمن الرحيم والحمد لله معزّ المؤمنين ومذلّ الظالمين، الذي جعل حياتنا جهاداً وتمهيداً، ومنايانا قتلاً في سبيله على أيدي شرار خلقه، والصلاة والسلام على رسول اللّٰه محمّد وعلى عترته الأطهار…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/85663" target="_blank">📅 20:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85662">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
🔻
رسالة إلى القائد آية الله السيّد مجتبى الحسينيّ الخامنئي
...
بسم الله الرحمن الرحيم
والحمد لله معزّ المؤمنين ومذلّ الظالمين، الذي جعل حياتنا جهاداً وتمهيداً، ومنايانا قتلاً في سبيله على أيدي شرار خلقه، والصلاة والسلام على رسول اللّٰه محمّد وعلى عترته الأطهار الميامين، وعجّل فرجهم الشريف ونحن في خير وعافية.
يقول اللّٰه تعالى: (يَا أَيُّهَا الَّذِيْنَ آمَنُوْا أَطِيْعُوا الله وَأَطِيْعُوْا الرَّسُولَ وَأُوْلِيْ الأَمْرِ مِنْكُمْ ...) النساء/ 59
أمّا بعد ...
سيّدنا يا سماحة الإمام القائد والوليّ الفقيه، آية اللّٰه السيّد مجتبى الخامنئيّ المفدَّى، السلام عليكم ورحمة اللّٰه وبركاته.
نحن أبناؤكم وإخوانكم الخامنئيُّون في حزب اللّٰه - المقاومة الإسلاميّة في لبنان، نبعث إليكم رسالتنا هذه وقلوبنا تختلج بالأمل، وتفيض بالرجاء، بأن تكونوا بأتمّ الخير والعافية، محفوظين بدرع اللّٰه الحصينة، وجُنَّته الوثيقة.
بدايةً، نهنّئكم بشهادة أبينا الوليّ الشهيد التي اختتم بها عقوداً من الجهاد والقيادة، جامعاً بين العلم والعمل، وفاتحاً أبواب العطاء فقيهاً عارفاً، وقرآنياً مفكراً، وقائداً مسدَّداً، حتى قضى شهيداً كجدّه الكرّار على أيدي «مُلجميّي» هذا الزَّمان، كما نبارك لكم شهادة وجراح وتضحياتِ إخوانكم وأخواتكم وأبنائكم وبناتكم من فدائيّي هذه الأمة في جبهة المقاومة، لا سيّما أبناء بلدكم الغالي على قلوبنا، إيران الإسلام، سائلين المولى أن يتغمّد الشهداء بالرحمة، وأن يمنَّ على الجرحى بالشفاء العاجل، وعلى عوائلهم بالصبر والسلوان.
ونحن الذين لطالما حججنا إلى مشهد المقدّسة ونهلنا من معين الإمام الرؤوف (عليه السلام) ماء الولاية الزلال، وإذ نرفع راية الحسين (عليه السلام) بيد الجهاد والتمهيد، ونقاتل أعداءنا من مسافة صفر التي تعني «لبّيك وهيهات»، فإنّنا نصافح باليد الأخرى إخواننا الأعزاء، أبناء الإمام الرضا (عليه السلام)، وخرّيجي مدرسة الإمام الخمينيّ (قدّس سرّه)، وحاملي شهادة الإمام الخامنئيّ (قدّس سرّه)، ورافعي رايتكم المباركة، من أفراد الحرس الثوريّ، والتعبئة المقدسة، وكلّ شريفٍ وأبيّ يتنسَّم طيب الولاية في إيران الإسلام، الذين نرى فيهم عشق الإمام الحسين (عليه السلام) وبذله، وبصيرة العباس وإيثاره، ويقين سلمان وولاءه.
وها أنتم اليوم، تحملون لواء الإسلام المحمّديّ الأصيل، الذي حمله الوليّ الشهيد بعد الإمام الخمينيّ العظيم، وهو اللّواء الذي رفعه الإمام الحسين (عليه السلام) ذات يوم في كربلاء، حين وقف وحيداً أمام جحافل الأعداء وصاح بهم بلسان الإباء: «والله لا أعطيكم بيدي إعطاء الذليل...».
يا قائدنا، إنّنا ومن قلب الميدان الّذي نخوض فيه معركتنا الكربلائيّة ضدّ فراعنة الأرض، نمدُّ لكم يد البيعة، بكلّ قوّة وعزم، وكلّنا يقين بأنّنا نبايع بذلك الإمام الحجّة (عجّل الله فرجه الشريف)، فأنت نائبه بالحقّ، وحجّته علينا في زمن الغيبة الكبرى.
ونعاهدكم على المضيّ قدماً في طريق ذات «الكرامة»، ممهِّدين، وصابرين، وكما كنَّا مع الوليّ الشهيد سنكون معكم، لا نخشى في اللّٰه لومة لائم، وفي أعناقنا أمانة الشهداء، والجرحى، والأسرى والمفقودين، وعوائلهم الصابرة، وفي قلوبنا نهج الخامنئيّ الشهيد الذي عنوانه الاقتدار والثقة بالله تعالى.
وتحت قيادتكم سنتقدّم بإذن اللّٰه تعالى في الميدان حاملين لراية الإسلام على هدي القرآن والعترة (عليهم السلام)، وشمسنا المهدي (عجّل الله فرجه الشريف)، وسادتنا الشهداء ممّن تقدّمنا في هذا الطريق، ولن نستوحش طريق الهدى ومعنا قوافل الشهداء والجرحى والأمّهات والآباء والزوجات وكلّ أبناء وبنات أمّة المقاومة وجبهة الجهاد، نمضي تحت قيادة أميننا العام سماحة الشيخ المجاهد نعيم قاسم (حفظه الله)، وأملنا كبير بوعد اللّٰه تعالى بوراثة الأرض، وإظهار دينه، بقيادة المنصور من آل محمّد (عليهم السلام)، وحتّى يتحقّق ذلك الوعد، لن ترى منّا سوى الطاعة وإرادة النصر وعشق الشهادة، (وَمَا النَّصْرُ إِلَّا مِنْ عِنْدِ اللهِ العَزِيْزِ الْحَكِيْمِ).
وآخر دعوانا أن الحمد لله ربّ العالمين.
أبناؤك وإخوانك في حزب الله
-المقاومة الإسلامية في لبنان-</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/85662" target="_blank">📅 20:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85661">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
‏
الاعلام الاميركي
: عُمان اقترحت إنشاء تحالف إقليمي لتقديم الخدمات بهرمز على غرار مضيق ملقا، والمقترح العُماني يتضمن آلية للدفع الطوعي مقابل الخدمات المقدمة في هرمز.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/85661" target="_blank">📅 19:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85660">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3252679764.mp4?token=kYK3dRB_gqzri9WBpEUM5nK6xfhjmqJVuJYbhAEPQubD1FHl1UvjeKszTQCBbDMubQNCMrEf0IiYYT4JOqmLxPYvmHb8IylSD5vjdj9u4ksFuyl84yLsgHUPAGNrw_J_rJ34Me_hcfwC3TvfhNkeBiIAuoMZAwD-IKU6W4ty5wGkUAUVlTECUkORd3iRBmOiQuRchqndKIXg2r9ERGkKE-8PsKXv_GB_r6C4PayzqCX0EvQxA5Vr3AVjUzoR6I-bE-VTLbrue5qU7Oindk8dhYt04ts6o2-ST-VsJQqq9qwc24EBiIFN2R2aB6qtliNeQFH2bUjDJRuM5aPKWx8WmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3252679764.mp4?token=kYK3dRB_gqzri9WBpEUM5nK6xfhjmqJVuJYbhAEPQubD1FHl1UvjeKszTQCBbDMubQNCMrEf0IiYYT4JOqmLxPYvmHb8IylSD5vjdj9u4ksFuyl84yLsgHUPAGNrw_J_rJ34Me_hcfwC3TvfhNkeBiIAuoMZAwD-IKU6W4ty5wGkUAUVlTECUkORd3iRBmOiQuRchqndKIXg2r9ERGkKE-8PsKXv_GB_r6C4PayzqCX0EvQxA5Vr3AVjUzoR6I-bE-VTLbrue5qU7Oindk8dhYt04ts6o2-ST-VsJQqq9qwc24EBiIFN2R2aB6qtliNeQFH2bUjDJRuM5aPKWx8WmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صورة نشرها مواطن هندي من مدينة جيزان السعودية تظهر تواصل تصاعد اعمدة الدخان من شركة ارامكو  شكرا لاخوننا الهنود الذين يعانون من ظلم واضطهاد النظام السعودي منذ فلم حياة الماعز</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/85660" target="_blank">📅 19:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85659">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO6r2PT4G7IeYMi0Z9_BV8RkwhFkLL71urlMS9ywIcpBqUCVYFiP8fQsBbHRh-OiU1-BN4cke3kUbu4d_42skctMcFtm8STaDNmGhbz59KUzJbBolhENcBiFOjcJdXPS9YpM_XVNd6F8mn1X4lwGvEEK9YEoSlDes4o98a-kgCjCc5SplRB_iW79xi8Y0-AN-X5l8snZTLEoepJ5eYZ3cuUXwsxA2dmTNWNVViXR59rbNlBW-COn4iskRkdHzhKaMJvgJYLRdDLv0Cm3b5auSoZGSRFGBMJGRyGFC4OYy-vv_OMsbDfk8Bc1vxTpKL9HrVguZyXA80ujSmej9o9uBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي
:
أن العمل الانتهازي الذي انطلق من أوكرانيا لن يمر دون رد.
هاجم زيلينسكي سفينة تجارية إيرانية وقتل بحارًا. هذا العمل يُعد انتهاكًا صريحًا لميثاق الأمم المتحدة، ونُفذ بتحريض من إسرائيل لجرّ أوروبا إلى حرب معها.
خلال اتصالات هاتفية مع كايا كالاس، الممثل الأعلى للاتحاد الأوروبي للشؤون الخارجية والسياسة الأمنية، وسيرغي لافروف، وزير الخارجية الروسي، أكدتُ أن عمل هذا الانتهازي المقيم في كييف لا يمكن السكوت عنه.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/85659" target="_blank">📅 19:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85658">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتن ياهو: زوجة زهران مامداني وعائلته احتفلوا بمذبحة السابع من أكتوبر.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/85658" target="_blank">📅 18:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85657">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1821e338b.mp4?token=vf-TH9XZA72ktalsBrO-E5Cx0u_OebGByqI6KbcVQj-RvwdmiRZcJwhAKUUzR-fgN6TKBDJ36XPPNmL3iFDjIRtE0Rsj1eYlDdw-_Fq53j4EjMG9dFvWENy403nrfFUnpJepIzpjml0qXrqcsUcvlUrXpOLfNXB3bFvB27GGF6Vf1_w9fvOZyTh9fVCZbNcHBsxlO30h-cNu88bTSoDctS86-RbGsFfJ1RNJd6ckL6AGADiTYi8PVJR1uxplZT24Rlzv05obP8_HrVmZ05vg0-T7TJenQAEA1LOwAUUdy57tXSmYS6RBDotCXBcDviWzo2k5YR87EL2yqo5DIjD0exyL-WqRRNQyLUwQZWG6TBX57N3Hf2c6KJgaTbo2GMB6NNnf-hJAfkhr__qLVt6aVFRidJHyOoZc7Kg81ndR-cxtm7tK-JnBfzEHhSKi3Pf8Pnfbfjy7rGCf1sw0xZ5-u2pKQz6HoB2nmVPm1iqaWxWDyzUuqWLG7IkjJkHoFlguTG9iOXKJl0ewMptPOr0hYMi2B6jnQUWLb_N1keJYm2V3y_aIAyH7wsf4hv54ZQkmSQ3_Re30YJWNpJ30fDccanGnvLgh4dqU6rv9gkv8M8l-yg4I-jTGiWGtKoTqvwbxqH8dh0MeQc6I4atIaTAfgrH_N7HZ8KTOvDfm_VUeZjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1821e338b.mp4?token=vf-TH9XZA72ktalsBrO-E5Cx0u_OebGByqI6KbcVQj-RvwdmiRZcJwhAKUUzR-fgN6TKBDJ36XPPNmL3iFDjIRtE0Rsj1eYlDdw-_Fq53j4EjMG9dFvWENy403nrfFUnpJepIzpjml0qXrqcsUcvlUrXpOLfNXB3bFvB27GGF6Vf1_w9fvOZyTh9fVCZbNcHBsxlO30h-cNu88bTSoDctS86-RbGsFfJ1RNJd6ckL6AGADiTYi8PVJR1uxplZT24Rlzv05obP8_HrVmZ05vg0-T7TJenQAEA1LOwAUUdy57tXSmYS6RBDotCXBcDviWzo2k5YR87EL2yqo5DIjD0exyL-WqRRNQyLUwQZWG6TBX57N3Hf2c6KJgaTbo2GMB6NNnf-hJAfkhr__qLVt6aVFRidJHyOoZc7Kg81ndR-cxtm7tK-JnBfzEHhSKi3Pf8Pnfbfjy7rGCf1sw0xZ5-u2pKQz6HoB2nmVPm1iqaWxWDyzUuqWLG7IkjJkHoFlguTG9iOXKJl0ewMptPOr0hYMi2B6jnQUWLb_N1keJYm2V3y_aIAyH7wsf4hv54ZQkmSQ3_Re30YJWNpJ30fDccanGnvLgh4dqU6rv9gkv8M8l-yg4I-jTGiWGtKoTqvwbxqH8dh0MeQc6I4atIaTAfgrH_N7HZ8KTOvDfm_VUeZjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: زهران مامداني يثير الكراهية. من المفترض أن يكون عمدةً لجميع سكان نيويورك - اليهود والمسلمين والمسيحيين. إنه يحاول أن يثير الفتنة بين مجموعة وأخرى. اليهود الأمريكيون في نيويورك يشعرون بالخوف.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/85657" target="_blank">📅 18:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85656">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتن ياهو: سآتي إلى نيويورك من أجل الجمعية العامة للأمم المتحدة، ولست قلقا بشأن أي شيء.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/85656" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85655">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f96e9c0943.mp4?token=b_01mDH-x0-3rC3xUif1GglYTewvTulTLe2_kgu8OgNAZ6IE534-PbCFLJIGlswEIiUMwczWOCPaklW_MuzeNhoh-rPSuFyo4Ahz01he1mup6MbJROF1GAGKZW1lJFlRufRt9_ogdzp4OmD_VUgTkhONAtgRBmSE9UA45FGcy_6oNBK9Q74FiTDDpJp1KNtI7FPj8cAgR6QE18u5cSJPTMe7HdJN1PpcxhoVnLPAPxB_RsZQs3oyYVovXqauTnInt5xDqGwM8BK1bOloJehVIN3L1kpDunF45f1kWVBPibveHMhAlGtnN5FfLe0QZBz_bYzGHtgy4u1uwwRUeGnOzI9f5jNywH_Q0W3GcBUTn8C7ebdnmS5HAei1QLnlQQ4ws_mPiDuoLxYy8rzrVwhX77XFIGtCkMQJpamb7wNC3RNhKy18qPuNPbxWIm1IWEYOAylIN4ScAw0BW2JK9tdVDY6mqHeVrbs6XGZfQ94EPhRFjVjvV-IXnJ_OGOFejel-Aa7WN9hLHEiFKHtLZyWoC-AYD2E2r7_K6F_wabKK5JDZc_pmAVDuvM3VTOyKPg9Z-dV3kxuGgPgI2BapnoVEsbOvOVivgRoh6KB-MuLe9izAXClQ53D_rV5JAdKbuN91_mgu0QMz8P3FxiRJbzQ5b4-vbSZOXH1aF3Mp6spS7Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f96e9c0943.mp4?token=b_01mDH-x0-3rC3xUif1GglYTewvTulTLe2_kgu8OgNAZ6IE534-PbCFLJIGlswEIiUMwczWOCPaklW_MuzeNhoh-rPSuFyo4Ahz01he1mup6MbJROF1GAGKZW1lJFlRufRt9_ogdzp4OmD_VUgTkhONAtgRBmSE9UA45FGcy_6oNBK9Q74FiTDDpJp1KNtI7FPj8cAgR6QE18u5cSJPTMe7HdJN1PpcxhoVnLPAPxB_RsZQs3oyYVovXqauTnInt5xDqGwM8BK1bOloJehVIN3L1kpDunF45f1kWVBPibveHMhAlGtnN5FfLe0QZBz_bYzGHtgy4u1uwwRUeGnOzI9f5jNywH_Q0W3GcBUTn8C7ebdnmS5HAei1QLnlQQ4ws_mPiDuoLxYy8rzrVwhX77XFIGtCkMQJpamb7wNC3RNhKy18qPuNPbxWIm1IWEYOAylIN4ScAw0BW2JK9tdVDY6mqHeVrbs6XGZfQ94EPhRFjVjvV-IXnJ_OGOFejel-Aa7WN9hLHEiFKHtLZyWoC-AYD2E2r7_K6F_wabKK5JDZc_pmAVDuvM3VTOyKPg9Z-dV3kxuGgPgI2BapnoVEsbOvOVivgRoh6KB-MuLe9izAXClQ53D_rV5JAdKbuN91_mgu0QMz8P3FxiRJbzQ5b4-vbSZOXH1aF3Mp6spS7Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو:
سآتي إلى نيويورك من أجل الجمعية العامة للأمم المتحدة، ولست قلقا بشأن أي شيء.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/85655" target="_blank">📅 18:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85654">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZcdpKGzfnyvUxdWH33k5vC_zEHG85zqEZrN9UdiNBblrWM9PdKmr7_nIBmLkdEgrMN2u1S7e45BYTqe4VekFwHwelBSqw59LpegwAz7R9gijGxR7Be-tOja_Re6ej75QiF62bnlj1zULsJxrlwQdzmt-QK-RSHp677MiRRNf7eKl0UxhsANATUa3G3e9jSRAy1hLBjlRz3uJeRaJqbNthb_ffX9BgaqfBbDMZQnxS8zDIk-O5pJM9WjVJFpewvih5aIF-EbfZ1_NZXUjiEKRXk1jMg-7ARxcOyovZzs-7rSEwDNGqbutDHxEUwYr4BgtpoeZ3S3VHOUZWOROzU5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇧🇭
اعلام العدو:
للمرة الأولى منذ السابع من أكتوبر.. المديس ملك البحرين يعلن أنه أجرى اتصالا هاتفيا بالرئيس الإسرائيلي.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/85654" target="_blank">📅 17:56 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
