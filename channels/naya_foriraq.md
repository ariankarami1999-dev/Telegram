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
<img src="https://cdn4.telesco.pe/file/t6sHVkbFB9jMlCFu-QcbGY2jnBNDTaAAZhDzN5BG3BgE9m8ebj8c_BlLsoX6mEHkJHvEmU86Jl5LdEIYWKrj479GeAb2t0u50kojIaYW1P2DhsyWzoo_X-iotj28crtKGg2rvvP2rlfEh-wTb-jt7CaRzQPRnVm2pnEiOm0ynlSdbrAGx70hsRbVQRHAOuxMwU8JRAJ2LNyIJLIV6F2zG0TqbyGODaOqY9hS7zynaYoJNFMyb4mh4Axn0RP0PV1L5UYJclSpIjGcT7HIAhuNncya_IwsSGLStuN8v7tjEG_zGkgZxLgPrNfxKIH-FzQnbbV5LwxC4baauCRzAsm9Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 21:24:31</div>
<hr>

<div class="tg-post" id="msg-86762">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd410a271.mp4?token=VDKJF8sliMZhgorpgp3eqhNJnPkAlyjf_NL-KNOxoCyd3gK7tunl8jTaaHRGIt26Es1bzymzGF3b1cHsaqXM6TF62AJD_Rgi_siwkquN_Wdo3Htmsti2lTbFNwawCIE9qYW8tYwPW6E2yJ_jjSHlohxLIfJPyJ6rYZmgn62-27K2ioXRfiqcbOhGq7C1_nSll0RLQ750BkzDLRTP0pXXB9q_l7jvyEl_j_Xn4UnZcc4e8wVQSdI7du6nYgFkjKqwN_Ym1uptygNJTkjwMyppf9Vp0xRDqF4DC4CemHVfRIuzxmz5cQLkANh4h2_AebiZpQ61sWeJ5UkgKGUQZj_ygg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd410a271.mp4?token=VDKJF8sliMZhgorpgp3eqhNJnPkAlyjf_NL-KNOxoCyd3gK7tunl8jTaaHRGIt26Es1bzymzGF3b1cHsaqXM6TF62AJD_Rgi_siwkquN_Wdo3Htmsti2lTbFNwawCIE9qYW8tYwPW6E2yJ_jjSHlohxLIfJPyJ6rYZmgn62-27K2ioXRfiqcbOhGq7C1_nSll0RLQ750BkzDLRTP0pXXB9q_l7jvyEl_j_Xn4UnZcc4e8wVQSdI7du6nYgFkjKqwN_Ym1uptygNJTkjwMyppf9Vp0xRDqF4DC4CemHVfRIuzxmz5cQLkANh4h2_AebiZpQ61sWeJ5UkgKGUQZj_ygg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
مستوطن صهيوني:
حياة يهودية واحدة تساوي حياة 10 ملايين فلسطيني.</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/naya_foriraq/86762" target="_blank">📅 21:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eO-oMn7jVMp8sLMq09DjQXET7sbk1Wu1JoMzr_62PyVRW7l0Ma3qZgHi0wJxnj8c7tUkyIJcLfVbKURoAyVAa1dhtuqpP1Hep1Chpx4RfGabbKWzlsRd4A5wFOWI8iwhEo4u6PzItSO_lpzdsUi3LFqXh84nNSOVppc4xyDrqOZc6IG_EhiLwteQ6H4Gqrepbxjb-Mt3y8yCOJj9oxgK-NeITOaY7xhOYCbFOoHeycNC1ojdCyr-IJclFG14-i6n-RI4oUmSuj12dM10Sl39T5hnWzVEiLaWmRbgk7xVbtQFMe61ZYsOPZwvMfldOGJPAT-LJiWBRnMl9OwtytCzqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNW8T0A75D2wH5P7UPT9Ii0hQXFHez--iXa79pvjk_nifAHemtE6AR3qZN1BEg7LBnRwlnp_GxO5VVBEOg8Q--lj_KEbM99Iq2Qm996VKaTTlwnGaypa1zRqGo7DLUvKWANX6PQSHw2M7h4L79fA3hFuhOLAt8679pfCLahxDEgSydbPCPtTbj96yXZymy7knKFm-EnfMp6cAm_x1umRbXvhgDw7IUigQgcZdHQnfwpon8KR19iesZevFL5bEAV2ckJ4_j4VOX-fm7oSFdjDuJsRFUaJm7n-RAnuHWTWr7pnx-mNUw_wDpPL0c95g4Eom2k4uMrqG-UVM7qYcFcROQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca1353aa31.mp4?token=en2Gna-6q1vKFCupthlZWwJwG_WMyoXynWfZSWXp1T-6TsCvNRzjwEFl2rq9313iSqHi8UAFN0YMXPRya8NjmLJx_kEqHoi8CnguEALo3r4HMTFe61wSc3fu4nPZ4fv-RGjly5YmpFZmZjs9_X-rtkSaHuLl1xlkTIEgE_TKTAu13l6qWpZf9HrjAl7jC4loW1CupgK_9f6RVM2q3LO-89a3fDU2zXBZZ4rhEdhYSC_gEaRJDhsTkpP-b5gpbWv-iRQtx3SB60Yv0gPebWOnPzhNZaC4PLMgVp7kXrJw4IIeh94M2RxZ9dNsXUFqLwwn97NCLXQ-3-2dikFTCiWViA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca1353aa31.mp4?token=en2Gna-6q1vKFCupthlZWwJwG_WMyoXynWfZSWXp1T-6TsCvNRzjwEFl2rq9313iSqHi8UAFN0YMXPRya8NjmLJx_kEqHoi8CnguEALo3r4HMTFe61wSc3fu4nPZ4fv-RGjly5YmpFZmZjs9_X-rtkSaHuLl1xlkTIEgE_TKTAu13l6qWpZf9HrjAl7jC4loW1CupgK_9f6RVM2q3LO-89a3fDU2zXBZZ4rhEdhYSC_gEaRJDhsTkpP-b5gpbWv-iRQtx3SB60Yv0gPebWOnPzhNZaC4PLMgVp7kXrJw4IIeh94M2RxZ9dNsXUFqLwwn97NCLXQ-3-2dikFTCiWViA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
🇸🇾
حكومة الجولاني وبموافقة السفارة البحرينية في دمشق، تمنع الزائرين الشيعة من البحرين من دخول سوريا لغرض أداء الزيارات الدينية.</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/naya_foriraq/86758" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86757">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
غالبية المحادثات تدور حاليا حول مضيق هرمز ولا نعرف مصير بقية القضايا، هناك استفهام بشأن مخزون اليورانيوم بإيران وتعهدات إدارة ترمب بشأن سلوك طهران.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/naya_foriraq/86757" target="_blank">📅 21:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇱
إعلام العدو:
‏حافظ آلاف من أفراد الجيش والدفاع الإسرائيليين على حالة تأهب قصوى خلال عطلة نهاية الأسبوع، عقب تحذيرات أمريكية من ضربة أمريكية وشيكة على البنية التحتية الإيرانية، قبل أن يُلغي الرئيس ترامب العملية في اللحظة الأخيرة. وانتقد مسؤولون أمنيون إسرائيليون بشدة هذا الإلغاء المفاجئ - وهو الثاني خلال أسبوع - مؤكدين أن القرارات الأمريكية غير المتوقعة تُقوّض بشدة التخطيط العملياتي والاستعداد.</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/naya_foriraq/86756" target="_blank">📅 20:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇦
صفارات الإنذار تدوي في كييف.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/86755" target="_blank">📅 20:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
عراقجي
: المحادثات الإيرانية العمانية في طريقها إلى الانتهاء وتمر بمراحلها النهائية، وتلقينا اتصالات من بريطانيا وأوكرانيا وبلغاريا وأخبرونا أنهم لن يكونوا جزءا من الحرب علينا.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/86754" target="_blank">📅 20:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509947903f.mp4?token=nlMjB_V9wm-uYFsMmCeAP20T1tMacxFvd0w86AI1RJFEDv8W-KNHkQ8_hvnRwbmT6mBfHZ8s1FQzeNjlxoBNXorYsmLbNhD_1dtDzq3-S-FlHd73JxAt0qmdYcMmCrZT7HbpaLcuKC6Ce8ydwYfqU9vzflvCNrTZ2Gp470PDV1mbJuLqSek2u8Rpn3SsY-wK3IM57gLYI_jklArA5tNl3YK7mjUQIN_EwkAUI6_nlRIovoiP17KSoi9uhpmNS10FUneP743S3CG_FBJU5FYw4kUHOps6tF_Zfhl1zVvSE5Exh1LzY3g7emRWCZGj_nMZpny99CUZRUiCrnfpbWqaJa_VxLQHjBuCk7ohqcaz5HlUASwUdyR4lwXVBeFEIIGFejxDKJsLJWBoO1zAuC6jIIZCwxearzqafofPP7fMunbSETbcdfWXuy2rOCnSoFrqaMXRaTJU6iV677WUZRXF0_C0B1VaGf5wUqy_8ui4JyT7T5VgcK_H3rHVam-1QiViVGGwkiaYptXTC65bkhq6rwMHeFj2v_B4sG22wl-69RSpEVePmWO_uGxdhospsOTVQcORuyrVmBfM1n1o7cRzv7_VQef4n-0YEgxcGANecDT-_QOUqh1fnyRvML3jcMkh4Cc5KyYKH9ZP1tV3H-HGVj4_gInhDYpwogWyPsZeiWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509947903f.mp4?token=nlMjB_V9wm-uYFsMmCeAP20T1tMacxFvd0w86AI1RJFEDv8W-KNHkQ8_hvnRwbmT6mBfHZ8s1FQzeNjlxoBNXorYsmLbNhD_1dtDzq3-S-FlHd73JxAt0qmdYcMmCrZT7HbpaLcuKC6Ce8ydwYfqU9vzflvCNrTZ2Gp470PDV1mbJuLqSek2u8Rpn3SsY-wK3IM57gLYI_jklArA5tNl3YK7mjUQIN_EwkAUI6_nlRIovoiP17KSoi9uhpmNS10FUneP743S3CG_FBJU5FYw4kUHOps6tF_Zfhl1zVvSE5Exh1LzY3g7emRWCZGj_nMZpny99CUZRUiCrnfpbWqaJa_VxLQHjBuCk7ohqcaz5HlUASwUdyR4lwXVBeFEIIGFejxDKJsLJWBoO1zAuC6jIIZCwxearzqafofPP7fMunbSETbcdfWXuy2rOCnSoFrqaMXRaTJU6iV677WUZRXF0_C0B1VaGf5wUqy_8ui4JyT7T5VgcK_H3rHVam-1QiViVGGwkiaYptXTC65bkhq6rwMHeFj2v_B4sG22wl-69RSpEVePmWO_uGxdhospsOTVQcORuyrVmBfM1n1o7cRzv7_VQef4n-0YEgxcGANecDT-_QOUqh1fnyRvML3jcMkh4Cc5KyYKH9ZP1tV3H-HGVj4_gInhDYpwogWyPsZeiWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مباشر.. من حرم الإمام الحسين (عليه السلام) في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/86753" target="_blank">📅 19:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86752">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e92ab1e9.mp4?token=gU9T0Kt8PuoECP0SuKN04TFklU2SQhPGQP9VMVjOX49p4RoAauDTtKry2XgZKDlKgi852IaTO1nuu4YMdtcujf9q7E2X_UhCC9GwoJlShg1SmcAtOYHztGrzpmPHva7Kntx1wmPfYyiPvygX88ZW7jYMhORy_i8veofewPb8q9FZdGbBlz9xClExhslgnle14-9WeGbBFcdkDUrS98aXeRyTyVAckgzlV5RPrdDYmsEJlBp52yVazKHGBCU4k1OII6cd7niOvSJxepKu3vb2iEQXN6T0eiHwX5VmeTcNA6t-4eJ--Y5t9UMqqiNfbNaOdiLhRWiTZEjr96F2wk1YCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e92ab1e9.mp4?token=gU9T0Kt8PuoECP0SuKN04TFklU2SQhPGQP9VMVjOX49p4RoAauDTtKry2XgZKDlKgi852IaTO1nuu4YMdtcujf9q7E2X_UhCC9GwoJlShg1SmcAtOYHztGrzpmPHva7Kntx1wmPfYyiPvygX88ZW7jYMhORy_i8veofewPb8q9FZdGbBlz9xClExhslgnle14-9WeGbBFcdkDUrS98aXeRyTyVAckgzlV5RPrdDYmsEJlBp52yVazKHGBCU4k1OII6cd7niOvSJxepKu3vb2iEQXN6T0eiHwX5VmeTcNA6t-4eJ--Y5t9UMqqiNfbNaOdiLhRWiTZEjr96F2wk1YCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل اعداد كبيرة في باكستان بعد هجوم انتحاري استهدف متظاهرين</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/86752" target="_blank">📅 18:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84b98d1cf.mp4?token=t3X1PblR8lzHUAR4nQkTl9Gc168g0pNTaU-qaFNcEbKjlFprRW0n8DoaEJE34UrsN7vtWVod-aIZPnaeLw_r2_RcpAcdTHc24TyYRqa-fF-_VSU936jhXwysz0WKbcBdTSHlDZpVLxljn-bKMrz6Dsip7V-ho0tJQf2FnMhqoN5SVPa4lJaLPQtYorqgVEBNt6h_RAdvvn0YIYO8WWSF5dsX1PUAlFSmaTpE9G86WB65O5kE2xGnHtUNll90BIB8j-6-wusJhHFrjB92rQG_fZgU6ZKjlwoLqTHVPiY-7oWyX7Wp2iDhA-B-fFmL_elEfpQyG2SipxP-u2Ifx9HIQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84b98d1cf.mp4?token=t3X1PblR8lzHUAR4nQkTl9Gc168g0pNTaU-qaFNcEbKjlFprRW0n8DoaEJE34UrsN7vtWVod-aIZPnaeLw_r2_RcpAcdTHc24TyYRqa-fF-_VSU936jhXwysz0WKbcBdTSHlDZpVLxljn-bKMrz6Dsip7V-ho0tJQf2FnMhqoN5SVPa4lJaLPQtYorqgVEBNt6h_RAdvvn0YIYO8WWSF5dsX1PUAlFSmaTpE9G86WB65O5kE2xGnHtUNll90BIB8j-6-wusJhHFrjB92rQG_fZgU6ZKjlwoLqTHVPiY-7oWyX7Wp2iDhA-B-fFmL_elEfpQyG2SipxP-u2Ifx9HIQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل سبعة أشخاص في هجوم انتحاري خلال احتجاجات في شمال باكستان</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/86751" target="_blank">📅 18:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86750">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مقتل سبعة أشخاص في هجوم انتحاري خلال احتجاجات في شمال باكستان</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/86750" target="_blank">📅 18:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R53890AeXxxyx-z2WcluDL360Ir1cztlRPIFT3LWnhT7-syvLRU4CwNFPTpxweSuZUZJUTuVjWH6lRkA6intx7RH84plJ3Ofnj7v4cH59EmPdrQi4D2AHFtOYKJqWp32NAf7d9BT8kfYgsefrVwrR0I7BCL4Lhgtjiu2KL4icy9qJeaahNbqc_W_0UtDguUXonhiB1piYkRHn6kbfuRKe-9JgsKbExIgyDUtd0LOcQcYUFzhnbF_4BT3mCESCcuzGzgpIlYYA5-jD4KDIitsSGUIcOyk21yG8EK5RVHc36DXT6OzadvtP6-hfC91McPsax81aXhWK5pbERKMpg0K5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يا لثارات الحسين وأبناء الحسين
نداءٌ لا يخبو، وعهدٌ يتجدَّد مع كلّ ذكرى..
في بغداد، ارتفعت جدارية الفردوس لـتعلن أن راية الحسين (ع) باقية، وأن أبناء الحسين ماضون على درب الحق، يستلهمون من كربلاء المقدسة معاني العزة والثبات والتضحية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/86749" target="_blank">📅 18:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
🇪🇬
محكمة النقض المصرية تصادق على قرار يلزم الخطوط الجوية العراقية دفع مبلغ 787 مليون دولار أمريكي مع الفوائد.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/86748" target="_blank">📅 18:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
وزارة الخارجية الأمريكية تجدد تحذيرها لرعاياها في أنحاء الشرق الأوسط وتدعوهم إلى توخي مزيد من الحذر.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/86747" target="_blank">📅 17:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86746">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80400fcd3c.mp4?token=KWUzexYb45wlEniVW1KGvMG7FKmWoxrrPrDaIUPuUrjWK6VzZjo3KfjgnJEe49KEKWhJww-mIYGg7qXO9RFKJ3mQFd8j9GJPzPuA7hfQqAfeNQMNVXRIwKcBXhV56oyQbfb9Oc43BIfNXt_W8kE1F37InYmJGwbjhXwWOrZYWM5AX6wbKkQZRRNYF5j38IdK8aZzpX7Qe56pHypE1aosHhbqijwNn5ynmXrkVUW3epXqcwWYtNQ369RvdWANvofFW9kfYjaU9fga5N9hkge5wAQ49_raaUZ5gTPUdQXspOwNfxdFeiC8phpjzbZ9DritTOCafxwx6YIHIrlNiobRpBJ2eU7zw_KdsSdNkFf-a7oiAMfekSsX1es0zkGCFRVJgMf6qhp10b1vnmIqhRQfXB14HjpIat8_CEZb1L8pvgMxlA-eQqVyIYcAwIOXnGwMFV4ViWDl8g0jB8jMowyMbWOL1ObAXKuqrPhgw3qQ1Tj9O1s878exMovBeLJaHU-R3OQi1MA2zCPAUALqc13Lp9xwwGa9KDwo6qKj0m9SgWe26TgqGZ5jgeZ9BoqhSdnXl5RbLy8vL4hulwF4z3KMTESYXHArKnp6JXLHCJGOSfwKeQAe-dFJiwEkR05EkR0PvXirAFlg0c_hsW_veKlSr5hGSOMWeavUvJ-0SySMTRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80400fcd3c.mp4?token=KWUzexYb45wlEniVW1KGvMG7FKmWoxrrPrDaIUPuUrjWK6VzZjo3KfjgnJEe49KEKWhJww-mIYGg7qXO9RFKJ3mQFd8j9GJPzPuA7hfQqAfeNQMNVXRIwKcBXhV56oyQbfb9Oc43BIfNXt_W8kE1F37InYmJGwbjhXwWOrZYWM5AX6wbKkQZRRNYF5j38IdK8aZzpX7Qe56pHypE1aosHhbqijwNn5ynmXrkVUW3epXqcwWYtNQ369RvdWANvofFW9kfYjaU9fga5N9hkge5wAQ49_raaUZ5gTPUdQXspOwNfxdFeiC8phpjzbZ9DritTOCafxwx6YIHIrlNiobRpBJ2eU7zw_KdsSdNkFf-a7oiAMfekSsX1es0zkGCFRVJgMf6qhp10b1vnmIqhRQfXB14HjpIat8_CEZb1L8pvgMxlA-eQqVyIYcAwIOXnGwMFV4ViWDl8g0jB8jMowyMbWOL1ObAXKuqrPhgw3qQ1Tj9O1s878exMovBeLJaHU-R3OQi1MA2zCPAUALqc13Lp9xwwGa9KDwo6qKj0m9SgWe26TgqGZ5jgeZ9BoqhSdnXl5RbLy8vL4hulwF4z3KMTESYXHArKnp6JXLHCJGOSfwKeQAe-dFJiwEkR05EkR0PvXirAFlg0c_hsW_veKlSr5hGSOMWeavUvJ-0SySMTRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
فيديو صوره باكستانيين يظهر بحوزتهم جواز سفر بحريني بعد تجنيسهم من قبل عصابات ال خليفة في محاولة لتغيير ديموغرافية البلاد ذو الغالبية الشيعية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/86746" target="_blank">📅 17:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86745">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9e362b8c.mp4?token=UpiUWU7bkNxmdDyPtxWLVDJd8pj98WFI00Dbt4Ihqv-2-j8jNyvP_GrdxOd-8h0XKt3DH4MmobYjtvEtVwufa51lOaJkiS1pH6XWOB7GQxABqbLAChzpA27XT5TJilQ1TREWpuuthZq7f1MqYy-ubootnm24W_5iEvN7zTtBUOtOFu_U6Qa4kkIWfCxUU4n-VsISHa-HariWg5FllXcaX66yFhjIVbvpq1O9dl3jrwk1g8OxdoNdNVO-ghU47ghUD5bT1mGZ-vQ7_8E3p460bANEfbgcNYYWCbsgSqS5pOTEdKK6OEKg2jlzql5E20OoxZAd1aS20Gt94Zf3gRlc8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9e362b8c.mp4?token=UpiUWU7bkNxmdDyPtxWLVDJd8pj98WFI00Dbt4Ihqv-2-j8jNyvP_GrdxOd-8h0XKt3DH4MmobYjtvEtVwufa51lOaJkiS1pH6XWOB7GQxABqbLAChzpA27XT5TJilQ1TREWpuuthZq7f1MqYy-ubootnm24W_5iEvN7zTtBUOtOFu_U6Qa4kkIWfCxUU4n-VsISHa-HariWg5FllXcaX66yFhjIVbvpq1O9dl3jrwk1g8OxdoNdNVO-ghU47ghUD5bT1mGZ-vQ7_8E3p460bANEfbgcNYYWCbsgSqS5pOTEdKK6OEKg2jlzql5E20OoxZAd1aS20Gt94Zf3gRlc8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
تحطم طائرتان إطفاء أثناء مكافحة حريق غابات في اليونان.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/86745" target="_blank">📅 17:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارات متواصلة داخل معسكر التاجي</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/86744" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9cfee199.mp4?token=fibNGX3-5NCZn3575Pp1UigGf5C3nZZCVGg1rfihW7czhuOe26xUaHr1GGwBdMKmZL8L3MdS-q02o-1AlyXOmqC_byqg51llOddtedTWisIBY3KsLh04lJPx-3krVivFbXwfqoEBQt2B8NYsMUgwa9EFPC9qZtA8DMr2EkmcaAZ9ciNN0yBeHPQc2BbbY_Z_UR8CMOxMvNGWwINOUEQvFGZ9n8w4AY_nBLPSKezoXGlGF6gtQkWRXxngBSNjAzXBmbSHx0JR8KUOMxmzFoNel5gbGhj70vosRajQ1WUqFjJ61oRXkoNRd1sUu4ewDahScadLe4xecIt9j8reahvVqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9cfee199.mp4?token=fibNGX3-5NCZn3575Pp1UigGf5C3nZZCVGg1rfihW7czhuOe26xUaHr1GGwBdMKmZL8L3MdS-q02o-1AlyXOmqC_byqg51llOddtedTWisIBY3KsLh04lJPx-3krVivFbXwfqoEBQt2B8NYsMUgwa9EFPC9qZtA8DMr2EkmcaAZ9ciNN0yBeHPQc2BbbY_Z_UR8CMOxMvNGWwINOUEQvFGZ9n8w4AY_nBLPSKezoXGlGF6gtQkWRXxngBSNjAzXBmbSHx0JR8KUOMxmzFoNel5gbGhj70vosRajQ1WUqFjJ61oRXkoNRd1sUu4ewDahScadLe4xecIt9j8reahvVqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متواصلة في معسكر التاجي نتيجة حريق كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/86743" target="_blank">📅 17:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اندلاع حريق مجهول ودوي انفجارات في معسكر التاجي بالعاصمة العراقية بغداد نتيجة انفجارات كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/86742" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe13b00c74.mp4?token=qbif5NU16IwMFw3uMsgzXC9ERi17CiMO0mHZphpwVSTgbAvwL2jNhlsko_KmOIlyXATsnq-Vk5uRmktvcS_-k3pnopCHvKQZ_622W3EQUEstYStGGfB0T_TovirXDDoL0REoBT-YLRMdmXME5NuFJYCsPL6DSHPbMwyczspEkf6yfUFwCooaJRRKBho7ERGsGlwKygjgBI3yNsXR0rFzzRMcYTfnhWT1w9dh-7L4EmGjNPBlXJUxby51TsotNG5f5tgvmXQ-_PDbka3092cHxMOWECEyOZNP27vvwWzg6bJk2nqmrAzqPKMV_6N43cNO_cpwyu0feJ62b62alukuOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe13b00c74.mp4?token=qbif5NU16IwMFw3uMsgzXC9ERi17CiMO0mHZphpwVSTgbAvwL2jNhlsko_KmOIlyXATsnq-Vk5uRmktvcS_-k3pnopCHvKQZ_622W3EQUEstYStGGfB0T_TovirXDDoL0REoBT-YLRMdmXME5NuFJYCsPL6DSHPbMwyczspEkf6yfUFwCooaJRRKBho7ERGsGlwKygjgBI3yNsXR0rFzzRMcYTfnhWT1w9dh-7L4EmGjNPBlXJUxby51TsotNG5f5tgvmXQ-_PDbka3092cHxMOWECEyOZNP27vvwWzg6bJk2nqmrAzqPKMV_6N43cNO_cpwyu0feJ62b62alukuOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرق الدفاع المدني تتجه لمعسكر التاجي</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/86741" target="_blank">📅 17:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86740">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocfUumFQO52-857pGEaIb6ry_miHz1WRaZFjUimA8dAbTfsiJGw6_3UdkpxveTJVqsY1ZZsvZ16kPAbZ9WK6qz1wwWZSr8P48TrWO9_BgKBPBOZiH1i2UMvoPm7L0ZKWCagCGmYD0D8_UQMJHjPVOnfjanRmCFal8yW-Z5gHBDK7OhCrh5bCj6EW3IxCNLaYfhSxPIjohp3Rc7fFEs3KH23wsQOOH0Tiq5Ktp-FhFNzE88G7jyKn0xO7gNNwDiKlunClOjCcOkLvBZOHR_8CSoIxoBA-zX5-oCIxX16aYf9Cd2_NPGEbKw37FS91-DeFxP4Ge70xopMW289d3aI6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندلاع حريق مجهول ودوي انفجارات في معسكر التاجي بالعاصمة العراقية بغداد نتيجة انفجارات كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/86740" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8201fce1a8.mp4?token=YEWwK4Uk2VyOa9fnUDsJqvl9f9tWJcKUww6E5K5TKstBoL1uSJZo8_S9esqvMFN7zLJDbVgB5WuTaeUzhGG8Eg-Er1kYMJr5eBawQF4oSP-A4i1Pgj7ECA8xdNoEDiDnGaZtNk5iPRRnqrmt6ZD4jjwvZI9zIafhm2D0CtxO-fHIoMSvkVDnqgxXI8kZM4KtxNWJq50-3BHiFrn_O1jK8jB2SO8ctfbp8L3n_h1PKnR9oZvaCz66oXAkY5WHG66U4jafPHBG1fXz53AYP3Zcrc7Ujr9iGt7OVi_sWfrf9qPYIoqjZ_0d1gxwCx5ijEUA19_0LM7_FtA_64edzvk4jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8201fce1a8.mp4?token=YEWwK4Uk2VyOa9fnUDsJqvl9f9tWJcKUww6E5K5TKstBoL1uSJZo8_S9esqvMFN7zLJDbVgB5WuTaeUzhGG8Eg-Er1kYMJr5eBawQF4oSP-A4i1Pgj7ECA8xdNoEDiDnGaZtNk5iPRRnqrmt6ZD4jjwvZI9zIafhm2D0CtxO-fHIoMSvkVDnqgxXI8kZM4KtxNWJq50-3BHiFrn_O1jK8jB2SO8ctfbp8L3n_h1PKnR9oZvaCz66oXAkY5WHG66U4jafPHBG1fXz53AYP3Zcrc7Ujr9iGt7OVi_sWfrf9qPYIoqjZ_0d1gxwCx5ijEUA19_0LM7_FtA_64edzvk4jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق مجهول ودوي انفجارات في معسكر التاجي بالعاصمة العراقية بغداد نتيجة انفجارات كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/86739" target="_blank">📅 16:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:
- إن الانتقام لدم الشهيد، قائد الثورة، والشهيد إسماعيل هنية، أمر حتمي، وأن الرد على هذه الجرائم الكبرى سيكون قاسيًا وحاسمًا
- مؤامرة نزع سلاح حماس لن تؤدي إلى أي نتيجة، وقد باءت بالفشل منذ الآن. إننا نوعد العالم بأن عزيمة المقاومة المناهضة للصهيونية راسخة، وبفضل الله، فإن الانتصار النهائي لفلسطين على المحتلين أقرب مما يتصور الأعداء.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/86738" target="_blank">📅 16:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">علاسة 3D</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86737" target="_blank">📅 15:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مستشار الأمن القومي العراقي يقول انه تم الاتفاق على فتح مكتب لبعثة الناتو في بغداد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86736" target="_blank">📅 15:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86735">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682bf59f05.mp4?token=AeN8CP16qnW4WtmX2w-BINn-lO6LeKhivhH1qW0LS-m0GI5x2EOd4wkDNbzWXgjtXFVsMpxFCrGmpUT7wVdnhXwiRI_kc3Gs99JQ9atHI-iF54qS7kI1eUqRmvfO086qU_a1U4SIuKRs3bL7GRnc2uuN_iUbQJwxJfg2lrfqX_q9Z2nj3pCbpBpQkUUAWEG4Iex5tsgJCaAHVAL-nExRSaWO0BHt2g7J9RAeXY-NASLj9oEr-e78CWQuQ5DQQ8o1stm3clcpAClx5VuxK_XWxEoNIw3RIQYzJktgf8fx5J_eLXOS6SmMkCJsgnJYc-kgo4Es_PQ-InzANs5hUA57kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682bf59f05.mp4?token=AeN8CP16qnW4WtmX2w-BINn-lO6LeKhivhH1qW0LS-m0GI5x2EOd4wkDNbzWXgjtXFVsMpxFCrGmpUT7wVdnhXwiRI_kc3Gs99JQ9atHI-iF54qS7kI1eUqRmvfO086qU_a1U4SIuKRs3bL7GRnc2uuN_iUbQJwxJfg2lrfqX_q9Z2nj3pCbpBpQkUUAWEG4Iex5tsgJCaAHVAL-nExRSaWO0BHt2g7J9RAeXY-NASLj9oEr-e78CWQuQ5DQQ8o1stm3clcpAClx5VuxK_XWxEoNIw3RIQYzJktgf8fx5J_eLXOS6SmMkCJsgnJYc-kgo4Es_PQ-InzANs5hUA57kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السفارة الأمريكية في الكويت تتعهد بالدفاع عن الكويت سابقا والان وتنشر مقولة لجورج بوش الأب</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86735" target="_blank">📅 15:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86734">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLj7fP0L_P-iJPG2eNtDCZ9GHYHqDLCvX3z2CdPX9TsjB6CYaXE7t90JThitabFferxhIi8wqzplEPTJnnEzeISSV-K7h6HlSfBCQj2Em2WizP1YEZL_dgIKpmCm675LcGOGvYb23CHeaDQGaA0bQmDEBpoe0cxbxuBStWWRelC1QjIx7JkQXZoUBWOljMKq5m7B-aAJ4I4phYtQQduExzyjLBZ6b5wYK2sg49If6z2Rtdl3NLBPZTdhg5-P27BHOW1Feep-LELdnO8QySSKLYeT9wcZuRT7L7WfSGZodP9qof9PtYgn7wOPASABrecaq8k7AZ0mE2dliE-yaPS-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مراقبون لنايا:  بالتزامن مع التحشيدات الإيرانية قرب عبادان ؛ يناشدون العراق بفتح ممر بري للقوات الإيرانية باتجاه العبدلي ومنها إلى بقية مناطق الكويت تسهيلاً للمهمة لكن يجب الاتفاق بين الطرفين اي الجانب الإيراني على عدد من الشروط من بينها منح جزيرة بوبيان…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86734" target="_blank">📅 15:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86733">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوي صافرات الإنذار في الأردن</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86733" target="_blank">📅 15:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86732">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avb7hM-iVzBnKDbwsCZchC6iUzTnGymbdI20ISLdgllj2fp4hz3SxWLLZcen2OJCPUungDuNdZEbckoK2J-Ulb1UN6nnLaOTi1FyLvaGD8-s7hjlQkD1UErKQ4HW1AVLHmIjluH71YwL-OAJ9Ip3xGq7dGAqMFr5nUJ6VeT-ui025W35OB5E_54JUWqBv-RAhFwF9G74d_T9t2-YiIjxTr51oGofVxP2kh5UfGzF2EdiqzPPxr9Lec6wepI4QQ3_1thuik0Vh_vGS6qsC5TvBI55OHCFtEQVwYgXjBQunpWgQySbhZsh0MoAC-6papAWEUxJYkzrDS2vV48z30rzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مراقبون لنايا
:
بالتزامن مع التحشيدات الإيرانية قرب عبادان ؛ يناشدون العراق بفتح ممر بري للقوات الإيرانية باتجاه العبدلي ومنها إلى بقية مناطق الكويت تسهيلاً للمهمة لكن يجب الاتفاق بين الطرفين اي الجانب الإيراني على عدد من الشروط من بينها منح جزيرة بوبيان للعراق وعدد من الحقول النفطية الكويتية ولتأخذ ايران باقي الكويت
‏ومن باب الإنسانية أيضا يقترح ان يتضمن الاتفاق مع الجانب الإيراني على عدم المساس بآل صباح في حال لم يتمكنوا من الهروب إلى السعودية بالسرعة الكافية وتسليمهم إلى العراق وإذا تقدموا بطلب لجوء سياسي للسلطات العراقية فيجب الموافقة عليه ليعودوا إلى منازلهم في البصرة معززين مكرمين .</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86732" target="_blank">📅 15:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86731">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منظمة أوبك:
سبع دول أعضاء اتفقت على خفض إنتاجها بمقدار 188 ألف برميل يوميًا.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86731" target="_blank">📅 14:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86730">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇩
اندلاع حريق في عبّارة ركاب قبالة سواحل إندونيسيا وقد تأكدت وفاة خمسة أشخاص على الأقل بينما لا يزال 41 آخرون في عداد المفقودين.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86730" target="_blank">📅 14:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86729">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
مصدر لنايا:
وزير الخارجية الايراني عباس عراقجي يصل النجف الاشرف يوم غد للمشاركة في اداء زيارة اربعينية سيد الشهداء (ع)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86729" target="_blank">📅 14:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86728">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
نبذة عن نظام حكم عائلة البرزاني في اربيل:
- اقالة محافظة اربيل اوميد خوشناو من منصبه بسبب تعليق صور نيجيرفان بارزاني في الأماكن العامة وتعيين هيمن قادر بدلاً منه
- أوميد خوشناو قام بنشر قصائد ومدائح في حق مسرور بارزاني لكي يعيده محافظا وبالفعل تم اعادته لمنصب المحافظ
- اليوم تم اقالة اوميد خوشناو ايضا وتم تكليف زانا خالد بديلا عنه في مشهد يعكس ان الصراع لم يبقى بين السليمانية واربيل فقط بل ان الصراع السياسي اصبح بين الاطراف الحاكمة في اربيل وداخل عائلة البرزاني نفسها.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86728" target="_blank">📅 13:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86727">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=TAAAoqJU_MCKhsVZg5loh9uIjucNdahH-Ih9q6rpdNixtlhkNoPfi21iwlmTmyM47KNm9PXshYrkoilSCPL_seoCfx2eVa4KBELVnlTDUWXaNZ9If4cTrRB60nx6xil8didA_yd1KW8MJS_qKRmYj8skhfMhul6GPOBZlymBTMrXM4RWvWYIxrJeWBpseMZGu_2uYSXM6aldEC-4ycih7kOqcoOE0Oxvx6rgaOz5npQzFXbLK-MUlQLyVenDBGtT_ucJuNBnGteOyDDkpsjZdPPYEY5s4eqO1NRbpKglSqF4kYXlItv6Hnib3vOEYGDZ_xRCw07aAc6kTq0V6Y8Bng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=TAAAoqJU_MCKhsVZg5loh9uIjucNdahH-Ih9q6rpdNixtlhkNoPfi21iwlmTmyM47KNm9PXshYrkoilSCPL_seoCfx2eVa4KBELVnlTDUWXaNZ9If4cTrRB60nx6xil8didA_yd1KW8MJS_qKRmYj8skhfMhul6GPOBZlymBTMrXM4RWvWYIxrJeWBpseMZGu_2uYSXM6aldEC-4ycih7kOqcoOE0Oxvx6rgaOz5npQzFXbLK-MUlQLyVenDBGtT_ucJuNBnGteOyDDkpsjZdPPYEY5s4eqO1NRbpKglSqF4kYXlItv6Hnib3vOEYGDZ_xRCw07aAc6kTq0V6Y8Bng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
مضيق هرمز لا يزال مغلقًا.. مضيق هرمز يشهد اليوم رياحًا قوية وتقلبات بحرية، لكن إرادة المقاتلين الإيرانيين راسخة وقوية، وهي المهيمنة على هذا الممر المائي.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86727" target="_blank">📅 13:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
حريق كبير يخرج عن السيطرة في مدينة سبوكان بولاية واشنطن الأمريكية، يتسبب بإنقطاع الكهرباء وسط عمليات إخلاء واسعة تجريها فرق الدفاع المدني بالمدينة.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86726" target="_blank">📅 13:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86723">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKu4CnJXdRxfkf7t3fBn4djOUH56GDNXFecuznx_idrwrr4sD9m9h1q0kFDX-HapufhRCI3JZcPzHlG38tTs3FK1n2fj7y3V1mId0MADKWrq01NMmB163sOtRq8gRLpWkjrQInkzLeHGhwQL0TwBAazPQHAbgpnSZzbbsfJaL4fldgHFxK2tRNyLBb6lPm5Zx551yPURymgTsqO7FBgWvJQo4hWD2Fee1Z6MHRnnwAbNGrltQBkgekqyMgQeE5vwDfA9rbk6bDn-K_HznW9uv28ZKLNPJs8_LzgjwFU8QTw-CMpI-YZAOysMjhOLwKfC3922kS8Cubx8WvjSgiB5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAPqhpnPe262Z_u7KAdunOeGPab_VEW-HyMgW7Qg-vjUjGdG3wt2a1jW8QNwl31qnU-sD_Q94CqJLmActF_nKjEYPYgIX2iUg9r7HCent9dUXR7zE9Am5L1Br8hRj3IN4fZTIAUO9C_9DUixvGrvwsUK9T12ut60PMA4ROa1JOybgR2XY6ho9_QkUDkvR0Dc9Rqwkyu8G0Bk4lGGOB2xnGUalbbG_Xg1w3TrLfFVDtFHjuUDAnEElg4i_tFL-jmX0PDaQhkg53vcazsNR4nj2O8VV_5EfOoA_MGpDyxboW5UFLiaNhzS1bxilC0fholdY56mX2_DrvQ7KYzB6COifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RU7iUhQvDZMcCrnyzvvN9IoyMBl0S_OsGC_5DW3q-Lvd_r35PnJKm9XYMl_TAViggBsLsNOoz5msKsUTydQ77JuUnHfZ9hjkSFgSV2_j97acZaRPTVYCnFEgRCp841-vIK--1R2YZfNtRuCUB0alHnAApxAZ2pB3KlJe-I5gUPiXXgySZ8PffSKaflmFy689DWf9WP9geJWuvXf48U3Sskd3FdYc7YUSZqeVK77QV0FpZKZgRRCmj4CibrmcgJBRs5CFt76r5G69lfDnqMOIcM3ftihAwLuyzlN2Q-4XbNMylhbIbhujvu4NpYoJFZ5q1TIyf4I_DQr8qmrvQNcT1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هبوط اضطراري لرحلة الخطوط الجوية العراقية IA248 التي كانت متجهة من مطار كركوك الدولي إلى العاصمة التركية أنقرة لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86723" target="_blank">📅 13:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86722">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
مصدر مقرب من فريق التفاوض النووي الايراني لوكالة فارس:
لا يوجد أي اتفاق بشأن إعادة فتح مضيق هرمز، والأخبار التي تم نشرها حول هذا الموضوع كاذبة. طالما استمرت الإجراءات العدائية الأمريكية، سيظل مضيق هرمز مغلقًا، وستكون حركة السفن ممكنة فقط عبر المسار المعلن وبإذن من القوة البحرية التابعة لحرس الثورة.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86722" target="_blank">📅 12:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇱
وزير المالية الصهيوني سموتريش يتحدث عن "اسرائيل الكبرى":
‏وعدنا الله بأرض إسرائيل بكامل امتدادها المذكور في الكتاب المقدس. ‏أرجو وأدعو الله بصدق أن تتحقق تلك الرؤية يوماً ما.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86721" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86720">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌟
شركة كابيتال:
اغلقتا أكثر من 300 حساب مصرفي لمنظمة ترامب بعد مراجعة داخلية لمكافحة غسل الأموال.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86720" target="_blank">📅 12:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86716">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇱
هيئة البث الصهيونية: حماس بدأت خلال الأيام الأخيرة توزيع بنادق على عناصرها في قطاع غزة تحت غطاء أسلحة شخصية، حيث أن الحركة ترفض التخلي عن سلاحها في الوقت الذي يتمسك به "مجلس السلام" بالتزام حماس بجميع بنود الاتفاق.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86716" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86715">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cn9EXSYRu_TguiO87hM_teDex5aWHnI8Xd_Ghw_ch9L_ANSE4-jWw96LF8DegCjUTJR55dGQDctCeoOMsq7LcopUVipQ7PDXQEO49laxUiEY8ZkDoB3LSuuGTR8LxaQxkUWOj_jcqh3wusz512GpNHkc9EMSIFhpk4tAjkwn3WYaB9_S8AbEwmUbmG58JfcBgH41IR3pgMGyfNYDIAi98xqgs_38Ho1aDI5QVPxIC8TeNM9Ly6ZEtajAKTycnhB9GzdCxu9hhgGKCBafjJG8sQgCYUZx7cDCrA5hvOlKRvlgw0YPX4DOqN7beDEuZMrlonuRbhAVbrwBC9RivwVU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الإعلام الحكومي والنظام الكويتي يهاجم العراق بذكرى ما وصفه الغزو العراقي الغاشم ويطلق طابع ضد العراق ؛ علما ان ما يسمى الغزو كان على يد نظام صدام ولم يكن على يد الشعب العراقي وكان نتيجة سياسات الكويت التي دفعت صدام للهجوم على ايران ريثما انقلب بعدها صدام وطالبهم بدفع مبالغ مالية نتيجة دفاعهُ عليهم حسب تعبيره انذاك</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/86715" target="_blank">📅 11:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2FenJp7hoaVnYsfn_fMp39GWIsB97FERW2xzN84I5zqnf1GlxcC6urTLPL-0VMLNXdwZ4ZaMyq1FUaGvrlrMLp7badxp8GZlh5Ty1eRgNuY4OQWd8I7DyKjEwviimye5UZ6XE1beOhe5x5PBZolUjzHFsE9OLxlJkOigLgkF2sQM-9XPOOKIoDbJkbNQJ_00fWmTAjdakn7vQ-Mvy_DzPALvLB-a55D4AD6QcByaDsTuOXSPAMoOp6242vJJQYY3wkMIpTlkp3RzByeYasLtIJzo7O2Fh6L2QDWq907RBw-NnZy6VeOeLb6jV7sa-T6WGWG_7h63EtIBgHZ_7AVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amWrtcQnHoroWCE7mPor2pbMoiNExLoM6vWUVwNR12cjGKGxMElr5E2hItno1UdAlii_fpXOCcIBIU_JERcyg17N9LlnaB38Dd1kGrSDg_TrVJp10n9THgcO0KE8aiwnF3807vqVTT3KwPRYdcTdJT1SUwKLv9Aeh-60RFg7-iqRO21nG8EvneWWuec0eGi7EPuuiF1-jAlY_REmCsG7cn3H_i7NlogPHPqGVczqmWnXkqq6RA6rrnV_oslvmZ1Y52aWEm-t_0c2V9QbpPXKH7Qq82kKvZ7le7dQKhYYwzdOzWxpH8HiF65V1qk_ZSVhhSbWGDokzkkIrLpXxlRLKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مصدر امني لنايا   انزال أمريكي بقاعدة عين الأسد ثم انتقلت القوة باتجاه صحراء النخيب غربي العراق</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86713" target="_blank">📅 10:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇱
جيش الاحتلال: الكشف عن مخالفة أمن ميداني خطيرة بين وحدات "الجيش" الإسرائيلي التي تعمل في لبنان</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86712" target="_blank">📅 10:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
تقارير بريطانية: مجموعة واسعة من التحالفات الدولية تشهد حالة من عدم الاستقرار - في أوروبا وآسيا والشرق الأوسط وأمريكا اللاتينية - بسبب دونالد ترامب.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86711" target="_blank">📅 10:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86710">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujxG9gs53Rirvk_M7IMZawxJxx5a8hgJ44ShMav3Hk7IKsygRl1JJZocoLzoNTaiu8A4b6Y7tOpGdcuW6KjcYJcnw6OjsGxlR8n-s5E7qLAISsBfo1F_SLWVBRM9G0oIk970Vn1mIfHo6VJPCuONuqjFexNrT9wfQ41HY39pPymqHRivcVvohptwZWQ-52QMjU3OF86fnOMOa-YFVVzv6lcsuYUTYGhzNV0YWJ_Ol-Q3gCpXYMUZjuQxq9AXvyyWvxhVG2B4Oy82VzyFGeP6qaFgXr_B7ANi_X7bkgthcJRJYnHrlRWVrrNdErDdlIaOnxtYVU1JCCz2j4xWWlgD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇰🇼
طائرة نقل عسكرية أمريكية من طراز C-17 قادمة من البحر الأحمر وتتجه نحو قاعدة علي السالم الجوية في الكويت على مايبدو تحمل بديلاً عن الرادارات التي دمرتها الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/86710" target="_blank">📅 10:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86707">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p8a6J3PNTHys42rAwJyq-MTMnZNKMh7As64jwiLjI8i8J2Ro_OphQD9V4wbskiLpngBp9ta8dgPDBwqECLEaBtReISxORLg9n2mQkuPPEZ7-Qb-MjeVdmzyMPY0XMc_sfX02jw40W6TJ6FoBLJaGceY5hEkZSjiU6M38yfzJc_jz7EQ-kkqF4cIABCiMfWKraKy8KLCaMumi0hLD9n2E0GbqZst9NDcnIELuSYZTX6cwCqXD51lpVT9Mj9BdDhX32rOL-1HltAO2LDUvsghrH97IMBW9_EwVGL9-RdLzwGUzvF3sdc_WMVxw7OYArn5EzC0wwBi23NO5O1oxYLiUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBwHM-NtmihOSUv4Lp5Ze1MU_PhsMOZ18AmpyzudlRstWWKs6K-bP0nP_l4QNquMe9BMsw6v76z3t22NLGxY_utT6bMqoix0a7yjXfGCMOTrxomimRKh5phUCWx6ZHkW_L07KLa54YWJ1KrsTXUUyeZDwe3OVSVYMI4uLO_SPpaJkQjBLBQh_kAs7wDbbKYHiSom63eXuXiPIE0_cgRUT0ap7oqLp-peJjkoZDFpYBq5gVfE4O8fmHcUnjmrHgtiFnlKSu9eFGATbO2P3cNMRVBJegKpY7hL6xyVc2np6b1xI4YEVi_0Xzv1tqJLZV6-B3ag6Atn0apo6O76KwaswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcETaONRgK7GOYsBtXHn7A4_d-Fdd_3wQXu_WcAtMSmeAnhG6-NAw6EWZHSgNncmAMSmLq7lP_KMNyy7dqEhydDNYmXOOvyt9cSuVR_rJlNimhEsa5U9jorV6pNH1BGycN1ggsrcBS5TiS2rp1EK7sbGBvQ4i0kIWu8tZQV8Yd6x988nKe9gZGLOgNUuBU1hZmoDEOR1oUckkMw27ov7Rf_UgjAwpQtyJODbuHI_wx-T5L2oBxPVSxIZkIcRZ4Kb-HmpfaByN4WzJacmnlcNlBhvtcaXXDc1eQrAyMP-tXWsUap1OLN9pIGuULd-GpAdGrZDeqkfVferBcHG6sAN5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇷
حادث سير لحافلة تقل زائرين إيرانيين في محافظة واسط العراقية مما أدى إلى استشهاد عدد من الزوار الإيرانيين بالإضافة لاستشهاد عقيد ومنتسب في الجيش العراقي.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86707" target="_blank">📅 09:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86705">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aocxn9NDCHpLLE2A1-IgIhS3L2sCZH1Mz06vXHzVVPStfsvTPg2WXIPQdrg0aJrVSI2isS3PfbCiQI0_XYAPYS7fUPXBppgqoA-vwLFTZIiFxzT_vk6elSQc8mvBazktDUqROKDAtQ2gz_8EMENld9ieqFKOt5z43IW-ThBF1KKWAK9pVs3XTYBmvWaPm4-es8h2sjpMbDwonGvtoc_FV1_3ZSBPb7Ewk3rZZX9QDCHO1Uy0isLZh3o7JQrOz4o2-FhtDNOVjax5ragreL9ab-bG4ZVkRJ5tvb9oHXNhwFDPONgGYXughvlAxZqiOVX1uEkWONltkyyCfvTI7d39zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0ZMIedYzf9DqY6KWQrALlK5Fi21sO0R3-hKSilFxL1yG3_DDnmjs5vwAwqD0ZsEG_d6aervkQqw6bA6w2GffoMizZE4CBJ85wCnhuMjQIO70Pt89vsVYOKe7vaTZursqWMmXpPKw4izkh134ByZKr3IFQ84GbC-GdX7jnsx4OSBOUJNaIaRaNHNL_GNW-5PZwFqDB0IFmwzXLZjOmEQJcMfVLhz6DygZqVtyW1x9Qyl4wPY-fooJ3GH4X6RZXFjGnFxE6m7Xy_YsH_Z_iwT-D1nxuH6qamaZlmzq9XA132Q4XAJXv09vGW5ktD21JvQt-7cyASVk92XyUO29jnfwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
ناقلة الغاز الطبيعي المسال GasLog Shanghai تقوم بتغيير حالتها الملاحية إثر تعرضها لحادث استهداف بمقذوف في غرفة المحركات أدى إلى نشوب حريق وفقدان كامل للطاقة والدفع أثناء محاولتها الخروج من مضيق هرمز قبالة السواحل العمانية.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/86705" target="_blank">📅 08:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86704">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
وزارة العدل الأمريكية تفشل لالتزام بالموعد النهائي المحدد في 31 يوليو/تموز 2026، لتسليم الملفات غير المنقحة المتعلقة بمزرعة «زورو رانش» التابعة لجيفري إبستين.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86704" target="_blank">📅 08:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86703">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKKQ-qU2aMAHuZPbanAui5wFchDYHrTFq2xpHEmWnXavEYBW83rPyMG61_JkWGQqeMEH6JcUDH6-TWGGBeKojrhxn3P-D-QgLQWNDq-I9EjDD3d4ublnl2JDC94lIOZTIg2zDsMSlJZiHlpaJTETkj8gajWOy_hH4kHwTgy7AaCKywa6wvf1B7SxENrbUqZOWDeWQj8s6mLt8VkIxxfZFNgZmjyCYeGFJOPxMosDT3WKKSEpzsH-uN1tRIb7t6enYEzYm7GwZSkyPOuWSozkuxsQFLpKs4lwNIfWC2X9japUbh7q1ApDw5aEpCAT_CqZhUpFDtPY33pjDsD2o8EeVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
خوفاً من الرد الإيراني.. ترامب:
‏"الولايات المتحدة الأمريكية على أهبة الاستعداد لمواجهة الجمهورية الإسلامية الإيرانية، بمستويات من الإرهاب العسكري والقوة لم نشهدها منذ الحرب العالمية الثانية. ومع ذلك، فقد طُلب منا مؤخرًا من قبل إيران ودول أخرى في الشرق الأوسط، تأجيل أي هجوم، وذلك بعد الاتفاق على بنود اتفاق. ويشمل هذا الاتفاق الفتح الفوري والكامل لمضيق هرمز، وإنهاء التهديد النووي الإيراني. وبناءً على هذا الطلب، وافقتُ، من أجل مصلحة العالم في المستقبل، وكذلك من أجل بقاء إيران مزدهرة وناجحة، على إلغاء الهجوم، شريطة التوصل إلى اتفاق سريع. وتشاركني دولة إسرائيل في هذا الالتزام. فلنبدأ العمل جميعًا، ولننجز هذا الأمر. شكرًا لاهتمامكم بهذا الموضوع!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/naya_foriraq/86703" target="_blank">📅 05:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86702">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي "مارك روبيو":
إيران لا تزال تمتلك صواريخ ومسيرات لكنها فقدت مظلتها الدفاعية التقليدية.
لإجبار إيران على تغيير سلوكها التوسعي يجب رفع كلفة سياساتها إلى مستوى لا تستطيع تحمله.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/naya_foriraq/86702" target="_blank">📅 04:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86700">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c9209c534.mp4?token=vn-V2LxYeikOY9ox8N58iWixZTKuHNJumgVzSbHUr4ZKd52Q45DRKcrm4EM3_T3sU3BvQv842e4LwWtmIx3qSEPHoSBGzRONRbV1ryUYDoHSJBTEcIBRnhoLWUlODRa41Zp5tsVoNQEg2b0EWR7nAzGMJ169lJv2_xW9RmXNz6vsFx6cQQboRkr8GAgcIxGz_CT3hwVnNGz8RGgyNr1W-9CcJCqML_S-jNPdlWsslGuV6M4n6HaYF2iZSxclfux4zQhjc5ogKTgwJMkrVbfxQzo91GALTkZ8N0k3NHcHSxfhVN5emd-ML5LFD9-H9X_heySjHQqM5VAnx4zcea6eEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c9209c534.mp4?token=vn-V2LxYeikOY9ox8N58iWixZTKuHNJumgVzSbHUr4ZKd52Q45DRKcrm4EM3_T3sU3BvQv842e4LwWtmIx3qSEPHoSBGzRONRbV1ryUYDoHSJBTEcIBRnhoLWUlODRa41Zp5tsVoNQEg2b0EWR7nAzGMJ169lJv2_xW9RmXNz6vsFx6cQQboRkr8GAgcIxGz_CT3hwVnNGz8RGgyNr1W-9CcJCqML_S-jNPdlWsslGuV6M4n6HaYF2iZSxclfux4zQhjc5ogKTgwJMkrVbfxQzo91GALTkZ8N0k3NHcHSxfhVN5emd-ML5LFD9-H9X_heySjHQqM5VAnx4zcea6eEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
حريق كبير يخرج عن السيطرة في مدينة سبوكان بولاية واشنطن الأمريكية، يتسبب بإنقطاع الكهرباء وسط عمليات إخلاء واسعة تجريها فرق الدفاع المدني بالمدينة.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/naya_foriraq/86700" target="_blank">📅 04:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86699">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
🇸🇦
مسؤول أمريكي:
ولي العهد السعودي محمد بن سلمان تحدث مع الرئيس ترامب يوم السبت، وأعرب عن قلقه إزاء خططه لشن ضربات عسكرية جديدة واسعة النطاق ضد إيران.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/naya_foriraq/86699" target="_blank">📅 03:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86698">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مصدر امني لنايا
انزال أمريكي بقاعدة عين الأسد ثم انتقلت القوة باتجاه صحراء النخيب غربي العراق</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/naya_foriraq/86698" target="_blank">📅 03:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86697">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvGSC4w5DZxydQlypRb75MxIM-QcYRt0rysoeKWkPk4JlnDIbl3SFv0AUUTr1ZgVcMhWi_hmOONhErE0RwnV4BYYpUPSTnKahHxa6Y7AihSgpOW7wAZ1_tljJ-sqcXIF_t6xvxxBRj35HCNsnKkmXMewbg4JIXtlPoU4PzK41kqcC4vXidRMailwd34J6VngeV1YmI03_DI5wXej0qIEzzFbBzuJDOoIfB2WGuCDreHs1HGhz2PgQouvVgCsLrnOTIJB_wfkhBgQ2Jbh689QONK_gtn-pntcIZzzJrI9g-ZTnLaRxKC7XeJE4LwMNpuCQRK85P2iVE_dQ_RavQdVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب ينشر غلاف النيوزويك بما يتعلق عن فنزويلا علما انها التغريدة رقم ٢٩ خلال ٢٤ ساعة</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/naya_foriraq/86697" target="_blank">📅 02:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86696">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات جديدة في أربيل</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/naya_foriraq/86696" target="_blank">📅 02:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86695">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارات جديدة في أربيل</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/naya_foriraq/86695" target="_blank">📅 02:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86694">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">لحظه اصابت پهپاد انتحاری به مقر تروریست‌های تجزیه طلب در السلیمانیه عراق</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/naya_foriraq/86694" target="_blank">📅 02:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86693">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=TcfOpBAUhbB_9LVNZhv3qac8TjDNkgM3qn8O4lYGIIejmqTcmBUXPrr4wGpe-07rZjDrXGazNnXitUnPXyBIQl8Fv3wDFtPHlUVvSDWmSXiqHc-0p6BN6KfK_h1s-0FHOAcmirSJVm5ZZWGlRUta6jM0tPpLYARABj5Cof1cyKaOv70zDVGLp2jXg34VQn5rcmHfpjMwFpWS_fW5yF50t1by4wDi2f4AregHmZ3sM1jbQHjRX1pHZUnuMTitwFa_VRLIKgykeHqAw53ONdziEkDOaT2Vymaqz_Ku9boFvZYNyPJC5iyHKAzUY2gwu7GDJenX_AFK4GrPIfN5LEnMMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=TcfOpBAUhbB_9LVNZhv3qac8TjDNkgM3qn8O4lYGIIejmqTcmBUXPrr4wGpe-07rZjDrXGazNnXitUnPXyBIQl8Fv3wDFtPHlUVvSDWmSXiqHc-0p6BN6KfK_h1s-0FHOAcmirSJVm5ZZWGlRUta6jM0tPpLYARABj5Cof1cyKaOv70zDVGLp2jXg34VQn5rcmHfpjMwFpWS_fW5yF50t1by4wDi2f4AregHmZ3sM1jbQHjRX1pHZUnuMTitwFa_VRLIKgykeHqAw53ONdziEkDOaT2Vymaqz_Ku9boFvZYNyPJC5iyHKAzUY2gwu7GDJenX_AFK4GrPIfN5LEnMMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احتراق مقرات الإنفصاليين الأكراد في محافظة السليمانية بعد دكها بالطائرات المسيرة الإنتحارية.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/naya_foriraq/86693" target="_blank">📅 02:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86692">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4fbc9a29.mp4?token=OHC-_9Roo4YopZNLeHTlaZX31WMNn9TtdisjoQI_DB3DKyAjVhyTqi67bT2aKOVqxGJtqaZ-uxmq5BEHFEazJ7RQowt7Ca3ssWm-a86EepyCKlRtD3djQ1U_lkftY3nqIRosYu6U4rF_clsBiYOtcL6d2E5sL1foqslXkZb0GWIL4QwzaPnd3qD4R0nIt01OKnsTTpDt_H9MSCvJoJSXgXzTZT2OrwYCCpkY1Em4DVqJtntrdW-lP_oy3NL-VH1bf-74rBorYW8NDI4TM8HN6ejDEoFg2ZEIonnUPXHssViZeMVw3xQm2qOHGDQ-EssPVFTBxb6RiU5jSzlemcopwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4fbc9a29.mp4?token=OHC-_9Roo4YopZNLeHTlaZX31WMNn9TtdisjoQI_DB3DKyAjVhyTqi67bT2aKOVqxGJtqaZ-uxmq5BEHFEazJ7RQowt7Ca3ssWm-a86EepyCKlRtD3djQ1U_lkftY3nqIRosYu6U4rF_clsBiYOtcL6d2E5sL1foqslXkZb0GWIL4QwzaPnd3qD4R0nIt01OKnsTTpDt_H9MSCvJoJSXgXzTZT2OrwYCCpkY1Em4DVqJtntrdW-lP_oy3NL-VH1bf-74rBorYW8NDI4TM8HN6ejDEoFg2ZEIonnUPXHssViZeMVw3xQm2qOHGDQ-EssPVFTBxb6RiU5jSzlemcopwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي بإرتفاع منخفض يحلق في سماء مدن إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/naya_foriraq/86692" target="_blank">📅 02:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86691">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7615a3c5e.mp4?token=OQMcRPVwpx7XY2FKL6jQtQit4d96Ud9BSOfS7CFDg1x3QyXdT95bR-fmbpgNkjbgb6cvgXnhsFDCkJuYLhr-YaIIOM6ZJI5R73xK4jmU-ERyM-4ZSydI5lN8iE2Von_ZtOVQoKRVarIAAz1tOlM-ZoqC8ajuiW9rPS9GkqmZNuIxVqq0y9F35waW9UK-Volhaovpn8POp9vGpG_-3nS5tM-lWgo8pQXkWlXSI73-dF01a5-vo5_NXyn1aqXDXEw16pzrJsgZarOeNolUBwbVNoKyUQ1Lph04T0DGdPvNc3l9TKIybeOIMNkG1B3F4AwIPQcf-z8zvwoTT57GsLMARA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7615a3c5e.mp4?token=OQMcRPVwpx7XY2FKL6jQtQit4d96Ud9BSOfS7CFDg1x3QyXdT95bR-fmbpgNkjbgb6cvgXnhsFDCkJuYLhr-YaIIOM6ZJI5R73xK4jmU-ERyM-4ZSydI5lN8iE2Von_ZtOVQoKRVarIAAz1tOlM-ZoqC8ajuiW9rPS9GkqmZNuIxVqq0y9F35waW9UK-Volhaovpn8POp9vGpG_-3nS5tM-lWgo8pQXkWlXSI73-dF01a5-vo5_NXyn1aqXDXEw16pzrJsgZarOeNolUBwbVNoKyUQ1Lph04T0DGdPvNc3l9TKIybeOIMNkG1B3F4AwIPQcf-z8zvwoTT57GsLMARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد أخر للهجوم بالطيران المسير الإنتحاري على مقرات ومعاقل الانفصاليين الأكراد بمحافظة السليمانية</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/naya_foriraq/86691" target="_blank">📅 02:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86690">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
دوي انفجارات في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/86690" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86689">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50695baca0.mp4?token=LIHYhZmLTMZZh3lZlEy5yq2Eudb8-YIuKo9myTbxzJMZekG52wzLtdt9Np17Z8ALvLoaESfSN_vZ4Gb_5H1jLkuEA85vURWsRcJodXa4LrmsAOODo4Q-Jix3LFcQY_lwpVWaBJOEZJA1ZXD9BlJ7fTMFFnZFjTCNgtzV4kCDCG_jnFLbMhd9UCtttSMoUucon4F4HBS2oqFBC8m4oLuLQuphU9-UpqB7ZRDq_ke_XYP4g-p9TJt817leIn5F_FpWog2rXxOtRJ0GY5Wbwh_ImJhUedT1EJDd1jMYmu9wXLRc1V3p4F60_LcVxeT3nRM5goh0Kst8G2dg8LtN9L1P3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50695baca0.mp4?token=LIHYhZmLTMZZh3lZlEy5yq2Eudb8-YIuKo9myTbxzJMZekG52wzLtdt9Np17Z8ALvLoaESfSN_vZ4Gb_5H1jLkuEA85vURWsRcJodXa4LrmsAOODo4Q-Jix3LFcQY_lwpVWaBJOEZJA1ZXD9BlJ7fTMFFnZFjTCNgtzV4kCDCG_jnFLbMhd9UCtttSMoUucon4F4HBS2oqFBC8m4oLuLQuphU9-UpqB7ZRDq_ke_XYP4g-p9TJt817leIn5F_FpWog2rXxOtRJ0GY5Wbwh_ImJhUedT1EJDd1jMYmu9wXLRc1V3p4F60_LcVxeT3nRM5goh0Kst8G2dg8LtN9L1P3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نيران واسعة تشتعل في مقرات الإنفصاليين الأكراد بمحافظة السليمانية</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/naya_foriraq/86689" target="_blank">📅 01:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86688">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1545bf6dd.mp4?token=BDmAtAbKF4PIhCsFuoHnbtpu_Wq3dtjhflBKPUh-TG2LKOu6OWgU7DBnRuFiVSos5LwpFyM7IsROWX5Sp7RiQt-Xrm2gVwZt-VyYuvpsYL5ka0iuZWU_dS8rIIhpyKhC9sw2OJbHKsslnOzioNls7CTppQ7Gw3JvqbqBEOQFL2e_0ijIaT8zqzwdzGwAyyIqPTwbIIhhBoqzySxSk2li4Y3Pvb-qQtq0EAVE8wDrMrDLh64E7KzvGD-JFEKF72iS2coYjDkL0iHP4njHGEwNYFXuuam3aO1iuUk3sdKSaiwan806aX-aYriGuawXqAeP3MnzKDAEU2QHZXzZKM2rLqfPLa17EtkXE2xdxov8ZDadXmxFtVvJ4E9qzTSztrtOhM6mB4LRaf2s0xUU5ZTKigvKPWtYaAAosDLwhQUuljmOdnZHpCVTMi6POGvX04xydHVMHY07xfLtiG8rOtUWbQv62qrThEoeZhlBDoAb5bcKSuS1-CAFaKlYLfoYukleYJL-6ho7W2AaiRq0LgcgA3aR_dXx5OrIPMwppW-RTX62j3R9-LVdgA6fKgpQNtAJfAVhgQmlafsQG8QuFLDhdUOrA7c97idEyNZ7CtzI6N9R1xdEAK6D89WbOhLGq89Ek-fYwvlg1sKm6V28Njgy385c7Aj-Hv8H9QsIAJEgLvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1545bf6dd.mp4?token=BDmAtAbKF4PIhCsFuoHnbtpu_Wq3dtjhflBKPUh-TG2LKOu6OWgU7DBnRuFiVSos5LwpFyM7IsROWX5Sp7RiQt-Xrm2gVwZt-VyYuvpsYL5ka0iuZWU_dS8rIIhpyKhC9sw2OJbHKsslnOzioNls7CTppQ7Gw3JvqbqBEOQFL2e_0ijIaT8zqzwdzGwAyyIqPTwbIIhhBoqzySxSk2li4Y3Pvb-qQtq0EAVE8wDrMrDLh64E7KzvGD-JFEKF72iS2coYjDkL0iHP4njHGEwNYFXuuam3aO1iuUk3sdKSaiwan806aX-aYriGuawXqAeP3MnzKDAEU2QHZXzZKM2rLqfPLa17EtkXE2xdxov8ZDadXmxFtVvJ4E9qzTSztrtOhM6mB4LRaf2s0xUU5ZTKigvKPWtYaAAosDLwhQUuljmOdnZHpCVTMi6POGvX04xydHVMHY07xfLtiG8rOtUWbQv62qrThEoeZhlBDoAb5bcKSuS1-CAFaKlYLfoYukleYJL-6ho7W2AaiRq0LgcgA3aR_dXx5OrIPMwppW-RTX62j3R9-LVdgA6fKgpQNtAJfAVhgQmlafsQG8QuFLDhdUOrA7c97idEyNZ7CtzI6N9R1xdEAK6D89WbOhLGq89Ek-fYwvlg1sKm6V28Njgy385c7Aj-Hv8H9QsIAJEgLvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عنيفة وتصاعد النيران من مقرات المعارضة الكردية في منطقة طاسلوجة بمحافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/86688" target="_blank">📅 01:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86687">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0164d5015.mp4?token=RXo8G3TZW21m4EjoHnKtS7IkMR2qwI-zOTMcK8LUOnBM8_YxdS-EMX1tzPpFto2IbEyMA7rXiuk140frPCDczXGV5PJ6K8HuXLGevn1hS_dn0NFxXKUwVU_UzlKI6KPo4vjZtkBPAY-gz_fcCBoptCh8fZhQSsj2IBLCspgNAVJSYyqQbqbaHluY7Opo-OMeKFxORWDfmeY-IJSuBdIXT7sz1qqLGErcM3572Q5whNbpMIJsVciqx6CcHlW2YeAfmmsADJ3FWz5o-2kY7JL4Vhq-Q1gNQc5dTElj0boIarhH6Oshy514vO25sJfGglWgc3tiuFq6tUifOX9Ym3uVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0164d5015.mp4?token=RXo8G3TZW21m4EjoHnKtS7IkMR2qwI-zOTMcK8LUOnBM8_YxdS-EMX1tzPpFto2IbEyMA7rXiuk140frPCDczXGV5PJ6K8HuXLGevn1hS_dn0NFxXKUwVU_UzlKI6KPo4vjZtkBPAY-gz_fcCBoptCh8fZhQSsj2IBLCspgNAVJSYyqQbqbaHluY7Opo-OMeKFxORWDfmeY-IJSuBdIXT7sz1qqLGErcM3572Q5whNbpMIJsVciqx6CcHlW2YeAfmmsADJ3FWz5o-2kY7JL4Vhq-Q1gNQc5dTElj0boIarhH6Oshy514vO25sJfGglWgc3tiuFq6tUifOX9Ym3uVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالطائرات المسيرة الإنتحارية على مقرات المعارضة الكردية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86687" target="_blank">📅 01:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86686">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKq3J2jZMHYOki6RjunMJvsNLuIgMjLrhzXzIQoXzkdXStLCDqTz9tSEu7Hdzbe4uS-pshuNit5SgqXhFdIgT9McOG8T8WoLlV34lMxIRegcXrRcy1WcxNeP7ffgSKvjn4t7ZS5igUACS-qDsmIPzi1SmRGvomQfBJNfO7VlDbZWi5gPBBcwpnyDxS_4VAB-S90ZUWgAg_4tZHJDVgQBdHHfYsuvMMjKLfAHlf1Cn3SjT9Kx0J4jNEecgL4ympzgVy7x0TIdpaeNH6SPzie0HiuPeTAs5_4wGtXCaFZMXY2gFBXHvFv3Sp3TG2ev6C2oNn-_PgLk2j-3H5WKrx_CxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران حربي مكثف على الشريط الحدودي العراقي الكويتي الإيراني</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86686" target="_blank">📅 01:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86685">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هجوم بالطائرات المسيرة الإنتحارية على مقرات المعارضة الكردية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86685" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86684">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlV9dafseippQhSHJ-eyEpwJuShQfCHCyFcHzJTWhN0JlIknE9rVYZYHNGF_sxvmbQ_dExXPcv8T6SM8q5qpaUVwzQlr8vCk5-6NChC6toLcFroI8QucICy4ZdtvK5sjyqAy1-5MjuSqrkvB2Ya3A_Frm1_wxCMOZxRhkwHByBNLKwYh5hIQKyUpO1vIOxYGk1awXzMJ9mM95G1KLzyprY7vPGTu6tT_TwjXaMLvFbjaSnna7j4eOvPetjLgXvEQaIwlZOMtiboEaUqQRevYzA79rDsLJXa9H2cKvicQyFfsUfQhe0nDXBPVbbX95Cc97btmbT48KuO2TAH-sCwCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاثنين يوم الأحرار بموكب قادة النصر</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/86684" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86683">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe5171ef4.mp4?token=ir5qRhoWU7cwXH14GTEk9rl1gjr8iHL3zw8zYffi6TQabsq3YUiEeM-_BCRvUmD-T3Qim0d4MyncxEWm6Ej7S8zh6P2NsOE2i5jrp0XxdCYWREU8P6e10BdoKq1n_BKZIK4CKzEBPu2iNfa5P5IZVEmsh8pS1yz1mps630hYOu3EQc-2S03nxHY_2k4juvnaSRiURvssnsuZWESbpXlD8p1lpAjyGIQQbDaWgYfd3qxyOBE8Hh9yoyXhhluSckQYE3SN4aiTEuZdOlIOx0A297iZu1hrJWQyEXbNTl_H1QBhlKK7ptpugHXa1Q3LZjRDfkYyXblVWrwQV9kln6qYzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe5171ef4.mp4?token=ir5qRhoWU7cwXH14GTEk9rl1gjr8iHL3zw8zYffi6TQabsq3YUiEeM-_BCRvUmD-T3Qim0d4MyncxEWm6Ej7S8zh6P2NsOE2i5jrp0XxdCYWREU8P6e10BdoKq1n_BKZIK4CKzEBPu2iNfa5P5IZVEmsh8pS1yz1mps630hYOu3EQc-2S03nxHY_2k4juvnaSRiURvssnsuZWESbpXlD8p1lpAjyGIQQbDaWgYfd3qxyOBE8Hh9yoyXhhluSckQYE3SN4aiTEuZdOlIOx0A297iZu1hrJWQyEXbNTl_H1QBhlKK7ptpugHXa1Q3LZjRDfkYyXblVWrwQV9kln6qYzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إندلاع اشتباكات بين مسلحين وعناصر الأمن الأمريكي في ولاية أيداهو الأمريكية.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/86683" target="_blank">📅 01:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86682">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">طيران حربي مكثف على الشريط الحدودي العراقي الكويتي الإيراني</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/86682" target="_blank">📅 01:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86681">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8414b56.mp4?token=mC5XzySRiQl9tNyV5DVi2pLThB3zo4LSl-cNoa3x-RdX8pL4JpTGdRrwwxKcBteXuuWt6EILgeJjiCTQcWMo_uUW3QJEnZ4AhQDx7oxWDl7rlbb9SGQKQe8tO5dtwX_Io1fLiaqPMujIbuBJRSQm7nXfYbSdkMpEV-o-PUeJosqc9RYOSdcxTcvhP6R-d4EB4KbUk7Ig1ht_5WXctpadYdGjnl1Zz2K9W0fj96YWsPRcFEXop5hTgY3DrpR88VTR1ilNTI-8viVoD4K57JhW4YGZF11fJbIeypEIvtgk1N3LRVwPCyui-a965J9l4GQJwpZuQNFxIDg6Y1iq53hxHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8414b56.mp4?token=mC5XzySRiQl9tNyV5DVi2pLThB3zo4LSl-cNoa3x-RdX8pL4JpTGdRrwwxKcBteXuuWt6EILgeJjiCTQcWMo_uUW3QJEnZ4AhQDx7oxWDl7rlbb9SGQKQe8tO5dtwX_Io1fLiaqPMujIbuBJRSQm7nXfYbSdkMpEV-o-PUeJosqc9RYOSdcxTcvhP6R-d4EB4KbUk7Ig1ht_5WXctpadYdGjnl1Zz2K9W0fj96YWsPRcFEXop5hTgY3DrpR88VTR1ilNTI-8viVoD4K57JhW4YGZF11fJbIeypEIvtgk1N3LRVwPCyui-a965J9l4GQJwpZuQNFxIDg6Y1iq53hxHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إندلاع اشتباكات بين مسلحين وعناصر الأمن الأمريكي في ولاية أيداهو الأمريكية.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/86681" target="_blank">📅 01:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86680">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/462eed6d8c.mp4?token=AgKm80moLQsjZihdq2B588X2QE3hZ7r_YPqkQEOur3t9ezTvF_ejzNK9i3pMY1x2mQgm0hAbIZAKLDdDpqxKcLMXOFnA_hNJL3hMEcDC9z0wp2PHBAJoz0D7TZEe3SYUd1zWC8f67FatafonaUEfu4QUnQG7XtnPsEwFSBZvVMuMa9zUbUkpeMQPtM7u_m0UKHwekAzs8GvqJqJKpkxVWQydvOCs6ELI5JP7tLL7YV2h7T_wDvKw4pXJVYqLvphsGgoVB2F81pSAsv45qbDgbMFnm914nVAIe-FBGETyBEXNOmahcVjs_ch8JkYrS_OIBb-1qJ9cxutYy8j5r1UyOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/462eed6d8c.mp4?token=AgKm80moLQsjZihdq2B588X2QE3hZ7r_YPqkQEOur3t9ezTvF_ejzNK9i3pMY1x2mQgm0hAbIZAKLDdDpqxKcLMXOFnA_hNJL3hMEcDC9z0wp2PHBAJoz0D7TZEe3SYUd1zWC8f67FatafonaUEfu4QUnQG7XtnPsEwFSBZvVMuMa9zUbUkpeMQPtM7u_m0UKHwekAzs8GvqJqJKpkxVWQydvOCs6ELI5JP7tLL7YV2h7T_wDvKw4pXJVYqLvphsGgoVB2F81pSAsv45qbDgbMFnm914nVAIe-FBGETyBEXNOmahcVjs_ch8JkYrS_OIBb-1qJ9cxutYy8j5r1UyOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قبل قليل بدأت مساجد محافظة كركوك برفع التكبيرات بالتزامن مع استمرار الهزات الأرضية التي تشهدها المحافظة منذ يومين وحتى الآن.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/86680" target="_blank">📅 00:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86679">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9b860706.mp4?token=sHcFBb7lzpdTBNF4PhJVIs6OA_S2HEg3jJCGdvyWpboGWlNLIUfxuiXEyAVjmn_sk3Ga-ETMx-OOgMbjS8MV01xhvp-tlmx5SrFnxtiZtcZop8IJxZ00bll5D8n0s-76j-WI_w0SEZWgX3uX_hpu7auMutPYKWI0BU5m56eOMv56yMCJpKwNZYnw0cJyLvmq4ll_Ipq2qGe-hVM7rtxFc-aawerTpR1p8Ey_dTmDd9p0I6rIGeJicdRwD4LFfBtj1wMD6VqeOo_SiptZLUybO-W765OAT-LNdMDXDV2n0bv8x66Nf6aMGJVZB6iJb_F3ytiPmNamhsLNRxOiQSN1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9b860706.mp4?token=sHcFBb7lzpdTBNF4PhJVIs6OA_S2HEg3jJCGdvyWpboGWlNLIUfxuiXEyAVjmn_sk3Ga-ETMx-OOgMbjS8MV01xhvp-tlmx5SrFnxtiZtcZop8IJxZ00bll5D8n0s-76j-WI_w0SEZWgX3uX_hpu7auMutPYKWI0BU5m56eOMv56yMCJpKwNZYnw0cJyLvmq4ll_Ipq2qGe-hVM7rtxFc-aawerTpR1p8Ey_dTmDd9p0I6rIGeJicdRwD4LFfBtj1wMD6VqeOo_SiptZLUybO-W765OAT-LNdMDXDV2n0bv8x66Nf6aMGJVZB6iJb_F3ytiPmNamhsLNRxOiQSN1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من أمام مرقد الإمام أبي عبد الله الحسين (ع) وسط توافد ملايين الزائرين لإحياء أربعينية الإمام الحسين (ع).</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/naya_foriraq/86679" target="_blank">📅 00:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86678">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accb6caaa6.mp4?token=MBr7ww6cLKJcXT57JOn43dFqYnrRptMHnyQiW73fYtdSi-KZdG4oj1ULO4F_dS3ug2nlM-TAaf0Enkf_yDZXAvP3OkgTpQl0g1bLmzhJ15H1e1ARQsr9JQCefIUdksGhtxu9A4D6k5GVXHRcmTKxKnbEuqm6zB3-Dl6RXzD4OWPiYfMlo2FoeaBDLWzN7nUoQHGDH1MOryuv57hoCXrYqs8egjHMUckDkXEELWtG8XbsgOUq04mCnzW7hoHf8ldD6Wk35kY6NVVkRrOV4SdycwRnaJ84a8IgBqHpe8cZNoMOPEGtyWvr0dZeUOROxdUqDOXS0Y_XGirU7ldwZfrnWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accb6caaa6.mp4?token=MBr7ww6cLKJcXT57JOn43dFqYnrRptMHnyQiW73fYtdSi-KZdG4oj1ULO4F_dS3ug2nlM-TAaf0Enkf_yDZXAvP3OkgTpQl0g1bLmzhJ15H1e1ARQsr9JQCefIUdksGhtxu9A4D6k5GVXHRcmTKxKnbEuqm6zB3-Dl6RXzD4OWPiYfMlo2FoeaBDLWzN7nUoQHGDH1MOryuv57hoCXrYqs8egjHMUckDkXEELWtG8XbsgOUq04mCnzW7hoHf8ldD6Wk35kY6NVVkRrOV4SdycwRnaJ84a8IgBqHpe8cZNoMOPEGtyWvr0dZeUOROxdUqDOXS0Y_XGirU7ldwZfrnWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هزة ارضية تضرب محافظة كركوك واجزاء من محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/naya_foriraq/86678" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86677">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
هزة ارضية تضرب محافظة كركوك واجزاء من محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/naya_foriraq/86677" target="_blank">📅 23:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86676">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4Zm3Ae8AU2WgfrWhRRrTvG4mf5Bu6k1RJTyUcRbm7DVCmtEq4Dgq03QV9lhnCT4HBZgj6ZUv0Emi0sznGZDiQe15lmVc_VFFwSouykYkEdi8MYTQeCh3rVVLUPfNG3JOJHvQ7QAdlkAG87Cv7PAn_p-k6G9j5EufW7K_EcNoRaSflRczf0HJMbHkNQkt-nS8b17fuO9pmI4sl0ugxjQoMllOPFtg555sawIx3LckYfXG79lm1EnOkXK0NcgbJq1eCfTiBwBCqie1z3Eh-oxa2qJXq-nRhXHnngCzK0fLuMrREWSA5ch4vWkYFXRb78YLddD3gLiMij6-BpzFtG-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علاسة 3D</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/naya_foriraq/86676" target="_blank">📅 23:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86675">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇷🇺
انفجار في مقهى بالعاصمة الروسية موسكو</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/naya_foriraq/86675" target="_blank">📅 23:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86674">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sameUNt6gPopDn1GPsmAu0QVL01fNSk267UpUroVHJtHCGHt5EkOAEjBXJtoAL4R5byDyrxJ2cV5D1x8LVQAdJZHwCkJ3S4LP3G0HVQJ8JdodKRC9Kc2y4bDwMY9K8ijSfCF78XbM2VvOmxWs7q31KmwSbO0KesnDkq1F2ZE7E8xyXSW50Fb4P6X7WQo7x7eJY7EvWT4A7wQ_u43fK25o8qn1RnPSrCrWPF1fzhsft8Yr0E7PDlukRJVC-KYYfoZnjX8e8iQ8Onxe5zlS543u_DedDOonFp_SSJ2LOcnK_nig4fs1PMCxO2L9F72e93WsRazz_7Wsgh9Ggf9o4qECg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
لقد كانت الولايات المتحدة واضحة: نحن نُقرّ بسيادة المغرب على الصحراء الغربية، وندعم مقترح المغرب الجاد والموثوق والواقعي للاستقلالية الذاتية باعتباره الأساس الوحيد لحل عادل ودائم.
أي مسار آخر يطيل أمد الوضع الراهن وهو غير مقبول. هذا الحل الذي هو ضرورة ملحة لن يجلب السلام إلى المنطقة فحسب، بل أيضًا الازدهار والتكامل الأكبر لجميع أفريقيا.
يجب أن ينتهي هذا الخلاف الآن، وستواصل الولايات المتحدة المضي قدمًا في تحقيق هذا الهدف.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/naya_foriraq/86674" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86671">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p5wVxNoN7sFxZ5qmLirAJT5_2aYO1fsybIU8QG3QEg3-_nI3dx8Bn4cSz3bDt391VTptK0bOlwdtUhioivt7tj4o9vmCUwwvVX0k3XHc9rfsDg1rjBdyPDcDsvLz8Dt8xVYvOmk3Q5G0pidGYEemUlrgbnpNJzIFuVKSRInFBtpOc3z9gXfT3CwmqYeUF6Mf8GDpfwatg5rkZ7NOEqY0sUCElsFXOeJRRQN7tyLNC0c-0Sg1g6mi_x_gNeuAN8I9AXIjRueJiQbeYkj2J9nxBI4WiK_TrTFdkLObm-js2aGqfp1ZE4oYBPgJVeiOpLc9ggpcfc7rf6-NnYnouDDXpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fk9y9PfmAHSNp8MZpeF74RCJxoVpqrPS0BvU_T7uSa1i7xfgTJgHx5h5tG3y3EnvBzFUMFoB6z47jtAIfpJ3Y8jH3qq-EjAz0uRUHH3bbgsg1QccEbl-82fPzl3lTipsdj5oH0ESX0FlH4JDuYCrD2-tv8R4iY_qxsst7BtxzWClhMNoMZxz1-IxAc_7fpETYs5LuNna2cgGAkC4RO7PBgxkmIGr4L0juJ7Ehlfxoal2Re08lff3746EjhfUp04f3Fdqjubm9nXBpR9AUPYJ9lJw9V3yIK7pfuXgWw3Ye4UNAoAjMUcPIvVHW5B69pCWxgvSfhUxrl_w10wGaFUbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7xXTZz0TxeK26QcUUUJjeY34PEFD5i52v_VT34xFhKtxbamEnPSretK8sBOHeRkdi-zbFAdl0LNfFIfdT7MoP-jGRkHYOW-_LbINh7tDZbFyD4maSj7UmjRB3itTj7PLVk8a368hbTOJD8if9hEXaXUmU8_5Sve4UeKB_UF4HuphAfQDszzkxCLgitVWTcsMfiyxKVPY71AJzxZS1KtzpxSwdEeTHF--qBXkCgmF6txL5JeFAlOccWbXxCU9vr9J1Cac6JjrSET4hmkxl5pvlh5vXJ_Kq3ZKp7oN5jKKRoH7KGisOpM7zVcyBOmzQAUI3MoTasmWhV9V5ZK0FsAXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية: سنستخدم جميع الأدوات للدفاع المشروع عن حقوقنا وأمننا القومي
في بيان، أشادت وزارة الخارجية بالقوات المسلحة، وأكدت على استمرار الدفاع القوي عن كيان إيران في مواجهة التهديدات والهجمات غير القانونية من قبل الولايات المتحدة.
أعلنت وزارة الخارجية أن إيران، في مواجهة التعديات الأمريكية والإسرائيلية، ستستخدم جميع أدواتها للدفاع المشروع عن حقوقها ومصالحها وأمنها القومي.
اعتبرت الوزارة أن استمرار الحصار البحري، والتهديدات غير القانونية، والهجمات على البنية التحتية المدنية، تمثل "عملًا عدوانيًا" واضحًا وانتهاكًا لميثاق الأمم المتحدة.
أكد البيان أن صمت مجلس الأمن وجمود الأمين العام للأمم المتحدة في مواجهة هذه التعديات يتعارض مع المسؤوليات القانونية لهذه المؤسسات.
أشارت وزارة الخارجية، في إشارة إلى دور الولايات المتحدة في زعزعة استقرار مضيق هرمز وتصعيد التوترات، إلى أن الادعاءات المتعلقة بعبور السفن كانت بمثابة ستار لأعمال عسكرية وضغوط على إيران.
وأضاف البيان أن إيران، في حين تدين التعدي الأمريكي، تؤكد على الحفاظ على علاقات ودية مع جيرانها، ومواصلة الدفاع عن استقلالها وعزتها الوطنية وسيادتها.
﻿</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/naya_foriraq/86671" target="_blank">📅 22:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86669">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deb2552d63.mp4?token=KTh7aqxXpxS76Z9yaHkoPDvGRqClq5FKL_gvw9rd32F5j9hZAKHdq8E2RXh-H8uI6ziJ0qFnDnJNxFHXvUkf2RFOyPZhu110dpR6P9Y6IC_ur-hoyCYyLTV6wb9-VfcXmcJUrsmYDxlLIkCU13WxFTOK19ICMBR7WHdOyr5UEvz4zrgjK31a_VenSXDdYPmhH0qNgTkSCwcIBpkcZuoDJodNLJ81rtU1D3ukPbRKMdve7xDL-qtoCITKuYyKiQ9WDWAI6LpKqePLBpJZsnY1Wr9brZTPUtRR3KVB5k3kh9QayKc0yfyrt2oJJrsRswbsn7g3_MZkYSW-Eit7JP957Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deb2552d63.mp4?token=KTh7aqxXpxS76Z9yaHkoPDvGRqClq5FKL_gvw9rd32F5j9hZAKHdq8E2RXh-H8uI6ziJ0qFnDnJNxFHXvUkf2RFOyPZhu110dpR6P9Y6IC_ur-hoyCYyLTV6wb9-VfcXmcJUrsmYDxlLIkCU13WxFTOK19ICMBR7WHdOyr5UEvz4zrgjK31a_VenSXDdYPmhH0qNgTkSCwcIBpkcZuoDJodNLJ81rtU1D3ukPbRKMdve7xDL-qtoCITKuYyKiQ9WDWAI6LpKqePLBpJZsnY1Wr9brZTPUtRR3KVB5k3kh9QayKc0yfyrt2oJJrsRswbsn7g3_MZkYSW-Eit7JP957Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ملايين الزائرين يواصلون زحفهم نحو مرقد حبيبهم ابي عبدالله الحسين(ع).</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/naya_foriraq/86669" target="_blank">📅 22:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86668">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇨🇳
🇺🇸
روبيو
: أي صراع أميركي صيني سيكون كارثيا على العالم أجمع.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/naya_foriraq/86668" target="_blank">📅 22:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86666">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92e5e813a.mp4?token=Fu1Do9SSd5-FhAVfxoItYDZlPvekWhS-0IS4j0sBDhG40jnOB1VKcY3AAp4d--Ew_JnmzN00FICwLhgHGJhTmsS2lqcDtpnSpxZYDmbuwzK84t1enT9zU_pjg-ddPQ2EFh1RnxAsT9xX6xvP16miDfFPmFvOER76RyLyEV8z3CdcGiKrUcy0T4VgxyID6UU0KC5bkcldgSgvrfd-ll8CP9U3nmW6bgtZ33HQRdXXLdXsnKil86KUJvmMloFTi2gwuw4ghrNXX6hIjzpJUsgidIgMfKbHSJfeFkGBoMzNA4SA6fFM1Xo_i_ctxfhqxERTUYpu0KIMZCxun5sQeaaPrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92e5e813a.mp4?token=Fu1Do9SSd5-FhAVfxoItYDZlPvekWhS-0IS4j0sBDhG40jnOB1VKcY3AAp4d--Ew_JnmzN00FICwLhgHGJhTmsS2lqcDtpnSpxZYDmbuwzK84t1enT9zU_pjg-ddPQ2EFh1RnxAsT9xX6xvP16miDfFPmFvOER76RyLyEV8z3CdcGiKrUcy0T4VgxyID6UU0KC5bkcldgSgvrfd-ll8CP9U3nmW6bgtZ33HQRdXXLdXsnKil86KUJvmMloFTi2gwuw4ghrNXX6hIjzpJUsgidIgMfKbHSJfeFkGBoMzNA4SA6fFM1Xo_i_ctxfhqxERTUYpu0KIMZCxun5sQeaaPrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
نيران لا تتوقف من مقرات الاحزاب المعارضة الايرانية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/naya_foriraq/86666" target="_blank">📅 22:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86665">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fb75e16d.mp4?token=PbbZFO1T2AdoEpPmcBw805DKA2VTIcqmo5gIZ_HhXIBQ81QT6LPZJcL1esDhbEBDkycRTomfdvUbzqjNLw6mc8jHiFiev6zJ2Qft1X5HVNKcb6ERs0nAnlpOH38gw5se4W_yl5NYdbC8aH4P3RaWbl3hkl3rwgmU3Ee0nCK7H5hLsp6Vlf-8ec3hq_O1Z2xAkEwi0zFM8ZAT6DOQu5ses0IGZTpT6fjrUXljK8vnYEkoU9Axmm1dc2tu_Dh_st6WpHqUYl2aQXVPDqJ-xVmGvH0TYkZp9hdk0YgZAIuobLD1I3Hu_AnaDmZ3mFnEf6JB00OqWLBEt0Jj7VuaiAfIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fb75e16d.mp4?token=PbbZFO1T2AdoEpPmcBw805DKA2VTIcqmo5gIZ_HhXIBQ81QT6LPZJcL1esDhbEBDkycRTomfdvUbzqjNLw6mc8jHiFiev6zJ2Qft1X5HVNKcb6ERs0nAnlpOH38gw5se4W_yl5NYdbC8aH4P3RaWbl3hkl3rwgmU3Ee0nCK7H5hLsp6Vlf-8ec3hq_O1Z2xAkEwi0zFM8ZAT6DOQu5ses0IGZTpT6fjrUXljK8vnYEkoU9Axmm1dc2tu_Dh_st6WpHqUYl2aQXVPDqJ-xVmGvH0TYkZp9hdk0YgZAIuobLD1I3Hu_AnaDmZ3mFnEf6JB00OqWLBEt0Jj7VuaiAfIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
انفجار في مقهى بالعاصمة الروسية موسكو</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/naya_foriraq/86665" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86664">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c42d7c0f.mp4?token=A1THh3TA_e0cr9zI6N7zAnwoOOej6eHU19BXzFudEYy4fK1V71bu-8NBP2byflpB20UEf-dw2GBKeu4BkuAoD5Y_tCKr68psXAWcCP2S9xQcHw9pJ8WzZyXzqbSWpm5rRTN9ta8wDNQS596ctkpg8sS5Zu-snwkgf-yBhTBSyx5NHiRpdHmvjerl2Zuwo8wtLZ_bVMRBGnu1v-cjLJ6Fze2VYnKTd-xZQUEBJVPs30QOh6icx7BWwDBV6dSdl8W7QPW9wBdMR-r6xyONwhfxxY9YU47A3kPvUgoj94OrKSzRayIDIhJ1JRXi3Q9kpER_pvNvZAjshvAKO5Slj08CEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c42d7c0f.mp4?token=A1THh3TA_e0cr9zI6N7zAnwoOOej6eHU19BXzFudEYy4fK1V71bu-8NBP2byflpB20UEf-dw2GBKeu4BkuAoD5Y_tCKr68psXAWcCP2S9xQcHw9pJ8WzZyXzqbSWpm5rRTN9ta8wDNQS596ctkpg8sS5Zu-snwkgf-yBhTBSyx5NHiRpdHmvjerl2Zuwo8wtLZ_bVMRBGnu1v-cjLJ6Fze2VYnKTd-xZQUEBJVPs30QOh6icx7BWwDBV6dSdl8W7QPW9wBdMR-r6xyONwhfxxY9YU47A3kPvUgoj94OrKSzRayIDIhJ1JRXi3Q9kpER_pvNvZAjshvAKO5Slj08CEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
انفجار في مقهى بالعاصمة الروسية موسكو</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/86664" target="_blank">📅 21:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uismgN8xAvN_bAQZaUApcQvgvyViHHaFfDGbE08TH3j2s7Ex7vAtNBrg6wzzOw-RLI6MsqWZiDaQs6_k6ckV8wt-Bvpgf8QSE07mryLaGvbRfCaMnoQqrPY34MQyyNpAfMpOHH556DFo0wHUSNvNrUvTQHlaMRtdwX-UJxA6tqmeKsRjhOYtpvuPc0rot8zml9FsCP6Si3IcVlkJTAY5BgpGQS1gz8wDCOr9jDpRtMHHwQYue5Y1r2L8Q-2uChY7ATfGKsAOSmNZfcj6arUWYKjDr5AqTr4sJLp9g8cH_uwZMdAK0U6A9KBvkLfPP7Rteo9Ms85IienxVQYz26Jdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب يعيد نشر صورة قد نشرها سابقا مع الفضائيين
😫</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/86663" target="_blank">📅 21:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86662">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW6vDE4JepNJ8RlFBXpRryBTLOOEKGxqtXMeeU6UDh2n6QbFGcibY8Qq2HDJQese9zn4AAV-yjTZkmqe-EazH_wsVMmcgSX0ADAi_RFtHgK3ChVbud53RnY0XTppQ6FmMENcLP0jBZzZnVTxxAElhSCcIVSs179P20yfhBiqj7OOKgNiFOwU7Qd45fA04_lja8_NoheUneruHKsyef8eQUYwLsrM202VtOZBoxw_69q-sL6PpCRar7KkkiBLApo0LhFJeaEu8JyJhEoveq3xpJx8IbuVOTesgCK71hQJ_VXbYbIu-7ihpVZ04Zahm89fNGU66W6nrI8OEyCl9UmqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب يعيد نشر صورة قد نشرها سابقا مع الفضائيين
😫</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/86662" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86661">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
Welcome to Karbala</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/naya_foriraq/86661" target="_blank">📅 21:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86660">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الاعلام السعودي: الأردن أبلغ العراق بمعلومات عن مخططات لميليشيات لاستهداف أراضيه.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/86660" target="_blank">📅 20:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86659">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
‏الاعلام الاميركي: ترمب يدرس إصدار أمر فوري بتوجيه ضربة لـ"منشآت طاقة" في إيران.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/86659" target="_blank">📅 20:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86658">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
‏
الاعلام الاميركي:
ترمب يدرس إصدار أمر فوري بتوجيه ضربة لـ"منشآت طاقة" في إيران.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/86658" target="_blank">📅 20:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989829c477.mp4?token=cOX8jvPUUqP4TxW5PLlHevInFKZela2tFVOP__eIiSqtjMixpnKOU6Hf8mdsOrCiDUn_g7UKKN9jQP3TTCnaC5h8Vp92jkAxiksN3r5vfyEdLFiiBThoutP1DuUaqA-g7p9CbcRIk9YYRinZdFyK8IynW5smJjzdoeZyNLvWiPbTgkKaOJsgf2GUV1TRbfwdK9Jk7jWUEIV3YqcIQJeNJl_3iQCnqUeTVXfHGZqvR6Bla6omkyEmYdvMa-O_7nzignFAL4UEbgPyqe9eEN7DuZsXuGxTy9ABt2EKQJWSSTcKNdYPal2zEzV_ckyY7WL5GqvN3ZzEoeikSjSdibH1hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989829c477.mp4?token=cOX8jvPUUqP4TxW5PLlHevInFKZela2tFVOP__eIiSqtjMixpnKOU6Hf8mdsOrCiDUn_g7UKKN9jQP3TTCnaC5h8Vp92jkAxiksN3r5vfyEdLFiiBThoutP1DuUaqA-g7p9CbcRIk9YYRinZdFyK8IynW5smJjzdoeZyNLvWiPbTgkKaOJsgf2GUV1TRbfwdK9Jk7jWUEIV3YqcIQJeNJl_3iQCnqUeTVXfHGZqvR6Bla6omkyEmYdvMa-O_7nzignFAL4UEbgPyqe9eEN7DuZsXuGxTy9ABt2EKQJWSSTcKNdYPal2zEzV_ckyY7WL5GqvN3ZzEoeikSjSdibH1hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مروحي كثيف في سماء محافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/86657" target="_blank">📅 20:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الاعلام السعودي: أبلغنا العراق أننا سنضرب الميليشيات الموالية لإيران إذا هاجمت الأردن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/86656" target="_blank">📅 20:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86655">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الاعلام السعودي:
أبلغنا العراق أننا سنضرب الميليشيات الموالية لإيران إذا هاجمت الأردن.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/86655" target="_blank">📅 20:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86654">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
🇺🇸
‏أفاد مسؤولون أمريكيون لصحيفة نيويورك تايمز بأن هجمات إلكترونية إيرانية مشتبه بها استهدفت شبكات المياه في سبع ولايات على الأقل. ولا توجد أي مؤشرات حتى الآن على تعرض أي من إمدادات المياه للتغيير أو جعلها غير صالحة للشرب.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/86654" target="_blank">📅 20:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86653">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119a2ee3a7.mp4?token=ZhOa449yayFPoj32voA46HbYcu7gpzIHm524pay5ryOfFTX_1sRnDQ04-DhKk6kCESkvnYlURie5BDt418xpRUFmaE4zOeFFffAVZfm-sSRPLsZhLvB6-efnJvqBCNMw3I8mTSx0mskYtlGWmYkt1H8mRl77bO9qU5opJAf-WkhiNC1d28sZPN_f11PRDB_eujiQRHUdKDjpaEyK0hrrOT42Mi8QtQBFAyzsh_AL3eJT9fRM3Bg8Kdx6xWBBAd1SHe-qJFeifWMB2l83BBBatMsqm5qUtRAuQgE8c4FUR_CkpIeIFea6LP5R9miBA9hPGxcV3OAwmmJFFcTTCkgX-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119a2ee3a7.mp4?token=ZhOa449yayFPoj32voA46HbYcu7gpzIHm524pay5ryOfFTX_1sRnDQ04-DhKk6kCESkvnYlURie5BDt418xpRUFmaE4zOeFFffAVZfm-sSRPLsZhLvB6-efnJvqBCNMw3I8mTSx0mskYtlGWmYkt1H8mRl77bO9qU5opJAf-WkhiNC1d28sZPN_f11PRDB_eujiQRHUdKDjpaEyK0hrrOT42Mi8QtQBFAyzsh_AL3eJT9fRM3Bg8Kdx6xWBBAd1SHe-qJFeifWMB2l83BBBatMsqm5qUtRAuQgE8c4FUR_CkpIeIFea6LP5R9miBA9hPGxcV3OAwmmJFFcTTCkgX-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يزور القوات الاميركية المتمركزة في ولاية نيوجيرسي، يذكر ان هناك انطباع سائد داخل الجيش الأمريكي إذا زارهم شخصيات سياسية أو صار اهتمام بطعامهم فهذا يعني أنهم سوف يُرسلون إلى القتال
😆</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/86653" target="_blank">📅 19:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZyMieSHYa_oTjcuu1jEAngodRfBUr1TQOxOxKLBB8dMdgSPZCLc_QQRVaz-FbF3jp8JSIlCIa4B-LvBO_I-qyPXjCWbZhGJuGtQLOdqRnCIJlqF8ujyccTtumP1F-yHa0Rptls1QLL0wEcFebopQ3H04PB5HgEl-kuBBmc-7zoPtNd6A1JqZEMgncDTOOsGkdWOhEnSZdTyswq8WyuGXktw6IAadeA8rod8BUjj0mevyRXN_MVMZoCsBrEGeX5-1lr4vk8-t14yv6zS_qm49cmOeT6ePi6P_jxUuZ6EiGIJzB7WfT_oZDQEbhL25_Vie9VAXlvGwd4f5BWkiBGKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DapnD3XK9SD2R4LTYfNsTAGIZLPf9R81vYVevLZnYamQ2uq8pQDlaWVhNsEiYZ6jj4W0ETC_hsAmHoCbnGmikKaYlOSCjVYyQ2LhUMWU_3eclR9kq6OvmZ2FVV3Yz50pxy_9TOyiMMNDlKzz3sjYeHVztOY43nyWNTjP9loumB43H3Tyv6WTdIjKOGw9X2DXejZJCaq_ebsFGHX5yBhRlkfNCRxaOFuxn6-AofxcFxir4bmygma3EgtIk95MBaeItSOD9SmR2dy16jEpIXPvV9Yr1ciMJbi3VFSkGZukihBBQn3HIKLrOoNIJeUn2XlubF6mmNZhSWcc39dHNiul6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhMFg7aS1BHl8i7reFfQs6U0bqgD7KeVXuUHpenRQE7Ajkmb7osEqMDa6-oDT7cTRKam43i9KqT_rL1e2JFwNTQyxzXnNzJRCEggQQjDzK9VlKBirZTXCecZ8ywiHe9CxMQRNlU2Zhv8LBBxwHfYdSugrHIIeeL3MXl2uFnAhLcIf2REI2YsFL_Q_r-1oZccbmf1HLPz9gs-oeEjCf_4ofAgZa_ssLerwBb67n9Np6DKeB_Sag4VfT5zxNl1af03fcBeQZ5GHqSEjVssgBJVG18RW1FfvKm3bIUypfmW1-u52_Q-65OjVswZ6h3tmYjwILviKzUBUqLVHMgzU2BsBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQ0-txYXW2u89lNCREEhp0Czp_MsHsjXIN1tUvgoOMVB9IagcFBUM7Db5mJALyV06yYXgXTSjFsXheSVMNJgKxnlLMyzSIS8JjmEz6Lcwlr7MDpnKELZjZqSfCozMAG5Gdw7JPGrsfXI0rH8LBkWsyd1X3HwpFQOhUviXnAdNvV9PykpNMhiuHsJCKKNgWkIzfMMWxAOqZFVXsr7g37hSUNQtnJ_p-J0w2tEGnH3a5grC_wcTZukKaxV1ZWIRKms3Uxu-FFSbILGw7v8n_1Q2IPjJ7I3SaM763ZlQLPNcFHuf9GH-KUWPZxSE4wUTewrpm65wYA4FKwgcXQDnPbXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5sMWoTM5xuuefm66gh3cy4EJf-XZm0aXtr6104UVlVK-MEGqSWjOJ2S87bElB0cmV8evEzYMIaqBgQVBpJdTkvMCL53a34zkkRkTCuaX0EZqXnyjf4PYCarDlVXZhtVfBeVddUISWVA9GfgO2WdsRsaK3BZLqu-A2x9cSgMr8Yc9fONHTHkRY5bgZ83_SuBt2QPVvygFlH904UvBhXJHiyNbQHTDs0KPyNzMZ2UVHLot-05vrgdJc6HD0Gl-XXFBCOqg8KM7R07rUs7fp6nISDX0NeKz2o17JoqPR3huUxKWCUeAjeLOybVgYF5rX2_iVUaxY9TI1JJMAo-oGAP9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
🔻
القوة الأكثر احترافية في قوات الحشد الشعبي العراقية
نشرت مفارز لواء ٧٢ عاشوراء كلاب بوليسية على طوال طريق الزيارة الذي يمتد من العاصمة بغداد وحتى مدينة كربلاء المقدسة للبحث عن المتفجرات والممنوعات ؛ يذكر ان اللواء يعد ابرز الأولية داخل الحشد من حيث المعدات والتجربة الإعلامية العسكرية ..</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/86648" target="_blank">📅 19:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86647">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
الصحة العالمية:
تفشي إيبولا في الكونغو الديمقراطية يخرج عن السيطرة.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86647" target="_blank">📅 19:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1f0463375.mp4?token=rZIL8_ZjKyxbMX6Pty19YC6nGHFwhQa9ru5b8QukuWEABP3eFY-SpxVSDbA2awf4VutSS5691SZP4GSPtoaOSFrRmA2C6Z5Fejd3WJ0cAQ8cUKGyWN9zyHmALyw-dL2tuLhI-wUKrx2eu-YD_9a0BrRsnt9vvJuP753a3nvjBIFw8l7pIrtTVFj6ZVzis8jj2f_gJJy4OedpnIgxs3WoIYUQyaxHuCZ7wa_iWTEwe1Q9UMK-s_xjJrdpGzHc0c0FT9OF228yYhMcrm2tAZis7_2-7pZZCx8RR_wL9GYmNECAPdsiXkm4YXxkIzwN0Dh1BS3_1mjHvAiyC5XlwiONFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1f0463375.mp4?token=rZIL8_ZjKyxbMX6Pty19YC6nGHFwhQa9ru5b8QukuWEABP3eFY-SpxVSDbA2awf4VutSS5691SZP4GSPtoaOSFrRmA2C6Z5Fejd3WJ0cAQ8cUKGyWN9zyHmALyw-dL2tuLhI-wUKrx2eu-YD_9a0BrRsnt9vvJuP753a3nvjBIFw8l7pIrtTVFj6ZVzis8jj2f_gJJy4OedpnIgxs3WoIYUQyaxHuCZ7wa_iWTEwe1Q9UMK-s_xjJrdpGzHc0c0FT9OF228yYhMcrm2tAZis7_2-7pZZCx8RR_wL9GYmNECAPdsiXkm4YXxkIzwN0Dh1BS3_1mjHvAiyC5XlwiONFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
‏إخلاء القواعد الجوية الاميركية في البحرين خوفا من الهجمة الوقائية الايرانية.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/86646" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cbf8f15b8.mp4?token=jJU_I4eaEBdYwNVfmIjhzBoHoqbPIOBTvcFGS8N0YaN7R7p1nZ9k3UbQJ3cVvLIev5yD-iewjFwespkq1S4KIjZcZ9NCHyV1vmou2koI6Z3BKUSk1m2hGpkMo-oJz74f01EKcwULhAQ81mpjhYAPC1TSweTWWf_k9ngbyPu8MNotvR-KraR0mW5r83V4e7MSFIZy9Ja-mpQ90_CHWevHDcvnUZHiNDTyspsaGF-bWKVkDVPGb8dZ08B9avE9xMOEVS0-D1Gj4q5JC_PWQWV5ZxYvvFtQEFov5Z0TPAl5XS-SMBa3w1N5xJk2eHMC8ZjDKc9zTdCCdhWFqK37zA_V_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cbf8f15b8.mp4?token=jJU_I4eaEBdYwNVfmIjhzBoHoqbPIOBTvcFGS8N0YaN7R7p1nZ9k3UbQJ3cVvLIev5yD-iewjFwespkq1S4KIjZcZ9NCHyV1vmou2koI6Z3BKUSk1m2hGpkMo-oJz74f01EKcwULhAQ81mpjhYAPC1TSweTWWf_k9ngbyPu8MNotvR-KraR0mW5r83V4e7MSFIZy9Ja-mpQ90_CHWevHDcvnUZHiNDTyspsaGF-bWKVkDVPGb8dZ08B9avE9xMOEVS0-D1Gj4q5JC_PWQWV5ZxYvvFtQEFov5Z0TPAl5XS-SMBa3w1N5xJk2eHMC8ZjDKc9zTdCCdhWFqK37zA_V_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد اخرى لاحتراق مقرات المعارضة الايرانية في محافظة السليمانية شمالي العراق اثر استهدافها بطائرات مسيرة.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86645" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89cbebf655.mp4?token=kYCvnGM06reeuh1SxwqjyDKUZbWFQpVOlZm4Doh8RNeiN1qTavJ9Dyb1RSx6qETsdul_QxAhIMXhsiP5ptjBnW0JxshtUyFRS6TMROHXVFV1ZnzzR1_R7XnbteMWcf2dWtEF0pMNKWAMFOoR-Hm57xlnS6o8MHJygM3XGJtV9ZIWsHLflwQTi8qwqWQZS87xyCG7_RK3oUZxeOEB828vOTqC_Ip8f7YKdNVZWRcwg76VH4RdaBm2DAeJJ_ZjEvx0CAo9wHDls7rPnwi39OZYJprBpTUgP90fbfP3YgK0WNL38CqEvZ4f6vdHyDA7Vsj4pL4yxq8cRKfvwJmgks7pZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89cbebf655.mp4?token=kYCvnGM06reeuh1SxwqjyDKUZbWFQpVOlZm4Doh8RNeiN1qTavJ9Dyb1RSx6qETsdul_QxAhIMXhsiP5ptjBnW0JxshtUyFRS6TMROHXVFV1ZnzzR1_R7XnbteMWcf2dWtEF0pMNKWAMFOoR-Hm57xlnS6o8MHJygM3XGJtV9ZIWsHLflwQTi8qwqWQZS87xyCG7_RK3oUZxeOEB828vOTqC_Ip8f7YKdNVZWRcwg76VH4RdaBm2DAeJJ_ZjEvx0CAo9wHDls7rPnwi39OZYJprBpTUgP90fbfP3YgK0WNL38CqEvZ4f6vdHyDA7Vsj4pL4yxq8cRKfvwJmgks7pZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف مقرات المعارضة الايرانية الكردية في محافظة السليمانية</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/86644" target="_blank">📅 18:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27ee993f3.mp4?token=MV5Y23eROVVtJEx2yNHMN3gHipbp8ZMEK0dSJxYIO7_Qm1vAzimqkZA9C91KuIGxW9jRf9pIQ0cUjvNTK6IYa-puh6ghRF42iaErR-h-pwgPxxfY7wJjN_4kIH7c8Qak8wHqTEzgfQ-thggf3zpYXBMr-a_FCvALUATdeQQVx66fhG_oHI8PItSLoCkEP5F583fVEA0hz761Q97jTR1G1naRpX61IpuAzSPlYZJ8tlp6YfWI7Tv4KJE46xP8guzO_Ekh84DagfT3a9PTF4VFK0BlkcDERxL3aPiHgf3w-47O_e7ZIpymLFb2V83FtpyTaxo4M_n0Ct6b6Ed1yrR0XjFET1iH3nABMqcGCPBDKFaiAM7C-eAiMePasp6_7xRnXENTpxarBy1fCamXtoROAJuKCRYU5-5foqHrZFj1D8Ic0oMEXNcMnqbQ0n74KiOavaGDjCSZIhkCEeTVY7XZCFNxKiU0c90f1GMJd1auvj22Xk5LmINhQv6e8hkciNbmbq4nR7AZctsjohQnO5hYVXGMnsOe6B8m8zYUF_3Ais1tWcezKHfVlN9s7TF6KMUSFHjPdHStXTx-ReXGjRgDgPw0M1PiPyQlWIMKmSC9gV5UMTjgVPYzJn46tQ6fvVJ7qEmtqsB3pFC8o_Rd0luqRdliU2h6yTzIc9YNcyHFT8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27ee993f3.mp4?token=MV5Y23eROVVtJEx2yNHMN3gHipbp8ZMEK0dSJxYIO7_Qm1vAzimqkZA9C91KuIGxW9jRf9pIQ0cUjvNTK6IYa-puh6ghRF42iaErR-h-pwgPxxfY7wJjN_4kIH7c8Qak8wHqTEzgfQ-thggf3zpYXBMr-a_FCvALUATdeQQVx66fhG_oHI8PItSLoCkEP5F583fVEA0hz761Q97jTR1G1naRpX61IpuAzSPlYZJ8tlp6YfWI7Tv4KJE46xP8guzO_Ekh84DagfT3a9PTF4VFK0BlkcDERxL3aPiHgf3w-47O_e7ZIpymLFb2V83FtpyTaxo4M_n0Ct6b6Ed1yrR0XjFET1iH3nABMqcGCPBDKFaiAM7C-eAiMePasp6_7xRnXENTpxarBy1fCamXtoROAJuKCRYU5-5foqHrZFj1D8Ic0oMEXNcMnqbQ0n74KiOavaGDjCSZIhkCEeTVY7XZCFNxKiU0c90f1GMJd1auvj22Xk5LmINhQv6e8hkciNbmbq4nR7AZctsjohQnO5hYVXGMnsOe6B8m8zYUF_3Ais1tWcezKHfVlN9s7TF6KMUSFHjPdHStXTx-ReXGjRgDgPw0M1PiPyQlWIMKmSC9gV5UMTjgVPYzJn46tQ6fvVJ7qEmtqsB3pFC8o_Rd0luqRdliU2h6yTzIc9YNcyHFT8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في الموكب نفسه، تجسّد مشهدان متناقضان؛ الأول لمواطن يعبر عن ولائه برفع صورة السيد الشهيد و السيد مقتدى الصدر وسط الحشود بكل سلمية واحترام، والآخر لمندسّ استغل الصورة نفسها غطاءً ليشتم شهداء الحشد الشعبي، سعياً وراء إثارة الفتنة وشق الصف.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86643" target="_blank">📅 18:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86641">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfR-MYgziRJQSDAyvO6pTBhw8XlO6xgs8MpVjFwz0uYz5eIEAHQyepaDK2jfORt_2wBxZylaemwKUTraf0CFrO18uUqX5QtpfXJtS1U9W522frNrbnjKkEfsHN6OrCDZxQs9OPkH-tOboJ9KbAEiMTkW-h0v17aL9uNA9M2e6wm4VchalB_ir0eXLfMNvUsOKdgYSvX0I3K0kp2oZ3iOf3w2HhIgRgw3zZ5nT1xLqiRJo1pXcU2IGj0LCGzRuBPVpsMY1CFFyKsXBleev0Tbv6Tkm8FiXTJq7WTw1h_Xw3fL1RgLltF_FwW1zvflxb3JzRhYOxrCOaeujyOqZS1PnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx9a1PEEcL8cORiMn1XqtXr4xQ4GSciD3TUJk-dS7YZddczca79VuLmdoR1I2ummBTlaofPfxtTh5h0_HMMJdTFKc3rdLkEZw5gwwbsnxIf-OniEsDu0ZSNOSuKbw2X3xuKerXwniIZNtA4xWQM7oGaH352tKttebYTOrMDFpr4BgYHbMjleLsBXO1LhKN9z_vKplcBQ8SSUSYjcjXnswBSL18ayk0W9Xttq2ObZ-4d_WypYwz1I2CVnYofDM_d3FMEHAzfFiFLcG3zBW33mLoC8LmFHf8s93HIK6UZwX_2TNwchjscIhyCh-rgM_KLxq1FYK1JRjEWeoLWv553oSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد لمنطاد التجسس الامريكي</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86641" target="_blank">📅 18:34 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
