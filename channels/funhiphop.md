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
<img src="https://cdn4.telesco.pe/file/FwMbNfb0YRK5Kkw3STtzOUI1UI0qPGYSPc0YFo35a4GV0d15W1TRHU3huPKx5RS6TOW8j79_nvfmcIOr1kOHY2FOfgZEGm3esyOn3OgH784j3D5C8g_VgtrELnOwkzQPjqIoJAEBsWFUzIlfjiJGR-zka4bYktWgq_CPDiOQG9ZBWXOhFMeWnaaq64zbvwSTjLEz965Vfh87TUjQnrDMpnGhfGp3abHnfKzQQVyU3s4GJQBZEUHrUC_cJaE1xlzF-ubH9Qgaebgo4b15clP5D06b49dEn2wujftBBhscnljvA_b1OEv4RDYM_20icnU38osiYlB1aXPAWeUXDTlsKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 02:22:26</div>
<hr>

<div class="tg-post" id="msg-81609">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مثکه به دیتاسنترا اماده باش دادن وقتی جنگ شروع شد سریع نتو ببندن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/funhiphop/81609" target="_blank">📅 01:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81608">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">راستی وارد شنبه که شدیم بازار های جهانی هم بسته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/funhiphop/81608" target="_blank">📅 01:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81607">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=kdCj19u4DD79ECu_Iemr-IUgJHvodh9vD28YmU97eFeeyFNqUIXwnxifjy4RGS11S-K8xQQVGFtRgN5mneTEF5kG9yEDks3RqlIKOaO5H-bOZ9CyMTKL0nnobZ96pTN4QW17LuEot-Vtb0KFg2UXLJDLijb14T-JVI4ZmN-v1Fc2TvMd9sn_qsj06R8rL3U_4jrTRmDRZ9X2s2doSCdQ15e7CwbHu6FZ4AoUpDAM1W2sjL6Kx-FL6W8vKDdrNOukAZGYK8bDko68AVnf5ek2d2MTf3keqAdZMgGXo7cuISQnFd3l7pyI24ZAvId27DZqmZJMcKrmLDQVqiylgb_MkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=kdCj19u4DD79ECu_Iemr-IUgJHvodh9vD28YmU97eFeeyFNqUIXwnxifjy4RGS11S-K8xQQVGFtRgN5mneTEF5kG9yEDks3RqlIKOaO5H-bOZ9CyMTKL0nnobZ96pTN4QW17LuEot-Vtb0KFg2UXLJDLijb14T-JVI4ZmN-v1Fc2TvMd9sn_qsj06R8rL3U_4jrTRmDRZ9X2s2doSCdQ15e7CwbHu6FZ4AoUpDAM1W2sjL6Kx-FL6W8vKDdrNOukAZGYK8bDko68AVnf5ek2d2MTf3keqAdZMgGXo7cuISQnFd3l7pyI24ZAvId27DZqmZJMcKrmLDQVqiylgb_MkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های اسرائیلی و امریکایی دارن کسچرخ میزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/funhiphop/81607" target="_blank">📅 01:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81606">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMHv5krfdYIpVoGFrF3bOWOMgcWLtJJl6Dqxxl9rPope6XvGVF_W2To2tpKMRhSXNE2xFKHPdkm35z6xnbOD-iwib2AH4sVSTFGTOUxHx87w5_AKasdjQP48qAjjOOZFkzgFCl5cZ9pVZdT7QOjGaeRFL9sSJG3ASS1yTukBTx3Y9-2RxBaZaq0K_-DH6aOn0VhTXCVCCi5ymckyrWU3xnovyPBGbjATtIPGDdRnlwFcmibtcW5MWgwNdnwkuqiu2ioABzq1dFRSkaW7fgRQDlvq8GhV6QERpHcS572TU1TM3oMnAh4KwLw_ehtVitEBooR28GP6ZTTAXJ8bQ6KoHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیما کاتوزیان جزو ۱۰۰ فرد تأثیرگذار دنیا در فهرست TIME100 سال ۲۰۲۶ قرار گرفت.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/81606" target="_blank">📅 00:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81605">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɪᴍᴀɴ</strong></div>
<div class="tg-text">گویا دلار تا ۲۰۰ قراره بره بالا
سال دیگه که قراره بره بالای ۲۶۰ اصلا
همین امسال فرار کنیم</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/81605" target="_blank">📅 00:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81604">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaqIf7Dyj30arAerAvyGs6m5Z_CTccr-UPYJEaRw9_GuaMi4hnnIIOjqLZtyqjdKeTtSOmFr8jrGwaIOonaIAGdpbWDWTW_qKr0pCNQ26Y8zQHv1fVNTS1IALmOgoETDb78ZCOOZm3_wqPbW_KubWw1Amng0y1n5tBnwa8TyQjIrH7oWxbgnsQCh6laY_eoIvfrSn9rg9PvznJIUZvyqityT5QaUjZ8eJTMmArLudXCcWmPV3NFYJBw3AWhag99PfxLjMZRgnMF1KcxD6yJWxym8Ao-IU50EWAiDb77y8WCsB2xYDj3GXEBNn3gvUlhINeUnJvtzZl-6m-XMyGRQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81604" target="_blank">📅 00:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81603">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c227c270.mp4?token=TlzAxa7-hRI6Q6Xfy9kgu3uwdU63BCIvovuLBp_emNBWqpJMZwt-FfYZvbgvxmgVmwJyfQ8CtMV-9EeeYXTQ1aMwuUEvWLNgUwiuLDqoCDmCmcLK5T0iC7T6bw0zFfQKUJnTHSy6dUPJjINMbuAKA2-XYnzwK_X0x8lhYB0y4vBPS9RlixQCeaV5PV_QJszy9ZTUp07SasqJyFQdXZStde6OcXx7B21UC9Gx-W9cZNtr1YCVE09D-hAaYpLe_PTEdOBuCNXggq-XfWVHeAgrzaPPle5_0NhO-i0U5RoIIS9HP7g59MKwONnadrh5y6db3EIiYbQBgdwnqWAVnaleqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c227c270.mp4?token=TlzAxa7-hRI6Q6Xfy9kgu3uwdU63BCIvovuLBp_emNBWqpJMZwt-FfYZvbgvxmgVmwJyfQ8CtMV-9EeeYXTQ1aMwuUEvWLNgUwiuLDqoCDmCmcLK5T0iC7T6bw0zFfQKUJnTHSy6dUPJjINMbuAKA2-XYnzwK_X0x8lhYB0y4vBPS9RlixQCeaV5PV_QJszy9ZTUp07SasqJyFQdXZStde6OcXx7B21UC9Gx-W9cZNtr1YCVE09D-hAaYpLe_PTEdOBuCNXggq-XfWVHeAgrzaPPle5_0NhO-i0U5RoIIS9HP7g59MKwONnadrh5y6db3EIiYbQBgdwnqWAVnaleqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترام:
من قبل از شروع جنگ ایران یه نقشه و ایده میلیون دلاری داشتم که خب ما میریم توانایی نظامی و هسته‌ای‌شون رو نابود می‌کنیم بعد سریع خارج میشیم همون‌جوری که به شما گفته بودم؛
ولی اون وسطای جنگ چیزهایی در من جرقه زد که خب عقب مونده، تو هر چی خراب کنی اونا دوباره می‌تونن بسازن که، برا همین الان دارم یه ایده میلیارد دلاری رو می‌برم جلو که بتونم کنترل و نظارت هم داشته باشم رو همه چی، خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/81603" target="_blank">📅 23:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81602">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نیویورک پست:
برد کوپر، فرمانده سنتکام طرحی رو برای یک عملیات بمباران گسترده و طولانی‌مدت (به مدت دو هفته) علیه ایران تدوین کرده که این حملات به صورت نامحدود هستن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/81602" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81598">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYDeG2BzxZhVwn1CUMv0CoxF6G8CISXngKoBSBts0u-OPpljzai0svxUMstADkzQJoa4vApcJTqINyHWAqm4kSRR7NJII7dEEP6zLJlqAdK3b3W8FZZOS5d7YprIEJqcf0dC5exOji2p8YUuv0yRAAb5xtKIAclxxUcVhBQ0Pkm4Si_A5DBQDdmnCJVK3zNKxZEM7A1D8yBgdoDgphFC01z1wSkbJA4brITbhEQ8_nfTOl9IcickVPk92YknP3so7vfTGfASjSC6iLUHygdo9w4K9BBwAMPy8A_r1IPBA_vDw0Fr-pkypZ2aiRE_fhHNcccroX5Wz4oUyA7_CgZkbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqLIBSXWqPFZfEpAMHwclqhDCU4OElymf2dKZb5fn9T1015CmqWOl5M8pnYdXvuDWHZu7jKUdoeJlGmfgqWCuSZmDzMK2km-OtfZIguQDOk_IWiM7ihpZZoe4-mh1FVl9WRJROBPEmwQUjmYtIZTo807yqADt0TU90rL47a1UyUCEveKi68FMnvRD6bedEjGnVWBv4eZiPtqT1nxEZIuoeGyWWYEWgAF2H25BQCleIW8HiYlA3jYw89xeN73srGjXrp3AgPu3_cyftkNRNB8EA7t1KpBWkFJ761a7qtJZK7DoYTYMFm1LWeSsa9vO_-oPREwvLkQPs9cLmjEzzBfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJbQHDCyBkHQA0zhWijrzP4B9eb63uns86j2QwRZP-OyqvsHejaUTuFfGIxW8WjQiJWlxoe6e0FuYb1rqLW2YDmz1OLaUXDfTbJx1pttEv1SXvPB6iEHvNPBsU0XHVTusM-TSKT01mZA1aCqb5Zky2_ws0DGn8XaVWH7OHW3EC84kCONGg8f4RMAUCxMbFkzW8xSg9pQQ7sNRAARMmwoZpPa41PMNbffUVsD59jlWIiasmfkDsCQ78bW7xOLrfTfoH0MqpHvNDf-ckVyDEX8zRvnTcI04VqJ_WxzoB9VxmFXOW8ln7DMg-E1sXZ9dM371n5N-9o_lO-NN_moubkf9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10712ee047.mp4?token=lXvRSvjJWFHGqfmW3T1oG0aiW39MBFs5UWYlWzK8pvQqr7RHCa3cjMLJbtcewiTLDkYIkESG7ancF-phPWdvrJ_J7pS5c-anqNthtt-BWiVd5X_PBsfzftMf1LXbx1M2SetEfaQ_yEV00pCkGGk50oqNqIpBvwopSj6j0KxkFRcwsTSWBd74Wsg9IK08z13wWDzNp-dTLsYmuT6bOiYjzSJ4JbehWjvwxurl0wXLwT2laR1odDZ1Qb_WBljNAaB68oOCATk2vCN3uyvMHhYmQc2KwWmHFOSHjH92FKmZmzduNUg3tR-tTTSl9WN2lH069TrnpNgv5y7nYSSkIoXL5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10712ee047.mp4?token=lXvRSvjJWFHGqfmW3T1oG0aiW39MBFs5UWYlWzK8pvQqr7RHCa3cjMLJbtcewiTLDkYIkESG7ancF-phPWdvrJ_J7pS5c-anqNthtt-BWiVd5X_PBsfzftMf1LXbx1M2SetEfaQ_yEV00pCkGGk50oqNqIpBvwopSj6j0KxkFRcwsTSWBd74Wsg9IK08z13wWDzNp-dTLsYmuT6bOiYjzSJ4JbehWjvwxurl0wXLwT2laR1odDZ1Qb_WBljNAaB68oOCATk2vCN3uyvMHhYmQc2KwWmHFOSHjH92FKmZmzduNUg3tR-tTTSl9WN2lH069TrnpNgv5y7nYSSkIoXL5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و آرتا دارن موزیک میبندن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/81598" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81597">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔞
فیلم های بیتربیتی با  زیرنویس فارسی
🇮🇷
تاحالا دیدی؟ با ربات زیر میتونی کلی فیلم آموزشی با زیرنویس فارسی دانلود کنی
💀
⚫️
@EzzyPhBot
⚫️
@EzzyPhBot
تازه میتونی از
💎
Porn هم هرچی خواستی دانلود کنی ببینی و برای دوستات بفرستی :)))</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81597" target="_blank">📅 23:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81596">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDo3UZij0scf1HImCEKsLwImV-AkiS5Ec2UWWD3EIlRPdzZM3-ncqsXRuNejtO5Q8kCDI4bLNX9pKb5XQgpKy45lB-_ni-67fVBXrgfb0xV3JDEV-jdwkp-zWQfOSlb1AL0Y6xgxyHwWFpAfSpZdL90Tx5rzhsWoBAMEpdlk9eaduRMuKL5YCaryyeN8Sg97PY-Tzt5UEmbf5_UmnUBm0Nct40hSlKnsLQTTz97M_5Xnfr3JXFiXK2ag5TlNSWUneYq2Yb87hJfTT-bd_SYaJuuVimSq5g2AmMqOKjyt-ym3DPid7JIriR_fEb2yxdii4b-uEB5KfdOHX7uwC5D--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/81596" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81595">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_tlIsRGZa8v_xcqeydZ8ThmXgPDW-t7ROB7goWNsoHBNFjbvZaUeIGBFFi_eZ8pBe5jvyCREsQgx1cfFjnp-q2prKZA9mskKyg1n65KRv_LliJxqYTw08hmgkHh1xs6m9YB3jEbOIZWWCVfjh47ifjgdi5IMC7q5Za13mSzwhYO6zpvKaKuchagrV5YFrmQDmU55FVrA5hXVR0thmj1IOx_UPK495TPsuC0jGNJ-MMvxZVR1l1ygK7j_ZgL24JkVeCujkev_IznCOdAb1EeO4cVCjr5INO9-5KFNAGoAqRATU7udF10_w00sfpmKFNCq9WCF5BqBd2hw5aOBwex9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای عمو هایی که میگفتن ما عزت و احتراممون رو با برنج و ذرت عوض نمیکنیم او عه او رو بخونید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/81595" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81594">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrJ6QlXFpbXvGHEJ4IaDOsPbsPdTytcfA81VVCqivhOekrpFeora7MXW2xbl2SCPf2SJIwQ9GBvm-CaLVREfrzwcNFq_6JgerQxB_1gZia-LhJ-jTYfpJ9IoJrkL9ji5y2OWt-dXaIwlTbTPGjzTiL6EDnSta4TnGqedgq1Vod5eUcCkGcZy8jo9_b7zcwjVQV8X2wu9VJlxUMtkLmd8T-lrHDdGLzv4QNh_Tlk1TzCNCUuuhw2pKp_j9Kv_59KWaFWBhiINnu8nMm3pX0mwU6B4ILWj1BzMJOGHW1FLp2Pb6d1ZgNwXNoWfrX0dNbUuBq6MI2LsRlVtXqQ34sjGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وول استریت جرنال:
ترامپ از دیپلماسی ناراضی است و وعده داده که ایران را با قدرت مورد حمله قرار خواهد داد.
ترامپ روز جمعه گفت که قصد دارد حملات نظامی سنگین علیه ایران را از سر بگیرد تا رژیم را مجبور به آمدن به پای میز مذاکره کند و قول داد که به این کشور «بسیار سخت» ضربه بزند و پیش‌بینی کرد که رژیم تندرو در نهایت «از صحنه خارج خواهد شد».
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81594" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81593">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">#شرمنده_بابت_پست_رپی ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81593" target="_blank">📅 21:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81592">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2I9Y9PomhAVnMgc3nI5eJnddaTU6gizVanxzBufNtNOAe6_9lDQuncloUxkI7NSOwVmTIch_y2XHlh-BzZcfOnWXY7iZ-xFgtZWyfMLPslUqRVzdL5RYq_n2Ff8OGTu9ZEEMPq2XK_Ai5sW96INa6QJwKe-u1LA9YGb1wF0ONNms4DcpCyTANVkRKW3R2BCLzYsPQqKADesIksrO2-EcW3ndY_P0adSxD2SWXYP_TBP130m1cIOFSfVfcFc-LR6sAn_QfjNZasrQ7J1CLYEN6awY1oXMffeMTnmuvkjpVYHU16fwN1kfuyKIxOlu7AZtJfJOi0zcBatv8pjWHUhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#شرمنده_بابت_پست_رپی
ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81592" target="_blank">📅 20:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81590">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGxl3y7opa5FLyxD9CY-cczLEmWN0Cv8PQW2XFIxGW-0r-0F8D3oABQWqXpvEcrLSvdsanBAxKde-7PpL0mnubmzXzS9_CgviBpcIKsLT5Rcae2oQBfUxUi91c0gmAZC3viDCYBGvqfHjb5tZZWAhKsjJvyt5MpAfpEayKbx_IRUqlXKroEy70EbRGMMBwTBUFEqDvArKTAd35J03cd5tTGuuEez6Re-e7TK0L51vP2hEpv9wqkB5_XdqR3Ph61EUDnlD9ltl0OWjakdGWwsASheVms_iPhcrlmgw5oUDJiFPS8VLHYOw7H9LHY_Nk8NvPA88J10-r_gqoGjRRaQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد
آقا تو کربلا رویت شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81590" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81589">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4m9FWZOIY1hqPXQ0wZgVUz_sJuWH2uhSRunaTjf27LskbH_eGOlAp4A3xMK1tYp1S-JwgqbZrGAPE7lbOHlzWcnBKsghlQ77thTmo5QJB6oIlyEkZfs29mT-fh1v1VS5J2M7ad1YbwY5wIXsioA43EdMki41BZKlGEb2aO0v0gbXPV78HI3_mzXpPBBnywoKihylX88fLd86Qp-JQI2G_alqQaHDVfMn_jVifeJ2Ssh3MLI9X-VgVCB4j3KeKDwjcBTyRwqB-d2vcLr3QmB7EXKjdD5XiTtnWZccN3Veq5Qd2ZFs8KXqFBKw0JHphC70pELJzMaU7DNZPopeU3PEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپهاپولوژیست هم لایک کرده بود
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81589" target="_blank">📅 18:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81588">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDr-fP0bUB9YyTohQsBsuAZizvJNzT9-UU3cd_4oTOkH-mp4a_vPIXDoLBZswaqfuDGRO_q5_S48ulbkDFb6xwEiiWHKb8Ffvf5KZmbziwxvrObrXZWamdlw-DxzZM8Vzu_lcdIHpQW-ZOhTIjosjAdFIMC5RbPvIFNPxUqXuAqk2XX8mirk6jzbDxgYpLHz3WuCHmiYdUqhxK6UmRCR_9FPcw9UCOnWu8AffzcMMdr5wk5D0Oc8i2jizgMAR6j4WP8v-D7dfGbRPIFDr12xaJ_egCgquql2c2FL6J-K4MYDhf5ftHGa3BDdiSRW5gsaG5S7ya0F1wIjn7DCGuEYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81588" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81587">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsUktVtJ7zSHIWH5uUu0TFRbzRGLTb5-lC2XVLWOiaMV920_csuyrwSLPmZQ_1T5u83t1MwKp8uz7Gm-9PkjrDJPPDlA8Sj8dc5itQG4-PUG7CezuqpxagcA_OVmPXDSAe0Ikg3pi_Dk5TpE7ofHmwOMzzPnXXNp_whJv1w0rYAftiSDDQMue5ig6VlfMsX5nuEQYL6Qxtu5Y0RIGGbMHg0BMTTW0GAoIjFqtj318iIDmoDeFoV1Zkv5qTSyY_D7fomrqHZigy6eK2DO9zs7U3T-2MxxVijDarJXGZnrQ2VNgYsJf12eM57lTMs5JJA1L3jT_Qyk97wVHxanfjgRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81587" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81586">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗥𝗮𝗽𝗶𝗪𝗮𝗿</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=RYXHQeZs2ywxE-ixSoaRTxWS8EyqRZIJ5atQ5khzPaMhjYWiW38DQo1D8mwMALz3rLXqDn6M8wK7StU1lFYYuF0mySNTIKAbCVMzX0_Yu9Q66t6xi4d_SINZZRnv3fOn8CJcMFiR8i6N2ElvSj3i1SXz6riS71pbh-A5z8XCJXfH1wQymX-Qx1LfqUQ_SRe-9jiUCKgIZ0y0IC22-GcCdv9AjssIV9Kqmm7cSsdbF-itjkJTcZt4g6Dv0M3Y7pbIjc63LYRvyVNM7udDQfRPr2GUBqICxkOhdDkBFxYDDgN4g-L4ECJYtHvrj8CMDhg2k04Vzk6HT6VzZFDyu0NdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=RYXHQeZs2ywxE-ixSoaRTxWS8EyqRZIJ5atQ5khzPaMhjYWiW38DQo1D8mwMALz3rLXqDn6M8wK7StU1lFYYuF0mySNTIKAbCVMzX0_Yu9Q66t6xi4d_SINZZRnv3fOn8CJcMFiR8i6N2ElvSj3i1SXz6riS71pbh-A5z8XCJXfH1wQymX-Qx1LfqUQ_SRe-9jiUCKgIZ0y0IC22-GcCdv9AjssIV9Kqmm7cSsdbF-itjkJTcZt4g6Dv0M3Y7pbIjc63LYRvyVNM7udDQfRPr2GUBqICxkOhdDkBFxYDDgN4g-L4ECJYtHvrj8CMDhg2k04Vzk6HT6VzZFDyu0NdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجام جلوی خود خلسه دست میزنه به اندام خصوصی جی جی
@RapiWar</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81586" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81585">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=WUrz-VsnWqPvl0hhMLAa6KrarzdjA2SdZDCvEsMa8A0lDEiuUjaFkhsHeqZE2OCxhNam3ajQpl3aYEWYNCR8VeG_ZHikYCMK-V3stcL9yLy4082_EOq_-eanDCctxrdI3YW_jvU7W2iio6k_iJXIO1wqnQG5qbETzkbj84qo7Ym2j__ZofPoOmdRwCqvqDR3MJ7mr3OXVLCH6yBmKgPiZkjnrw7haU3HoDqwOapRqWND2L_GOJgbvl7uKZ4_-3J8LsinfSEjMARDInXr7_WIs5DPoBfG8G3XicdgXeLhIqx9PXesu1JUp9Ihp3Nbh08r1fHm7Ft01kooLc9oKzpdGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=WUrz-VsnWqPvl0hhMLAa6KrarzdjA2SdZDCvEsMa8A0lDEiuUjaFkhsHeqZE2OCxhNam3ajQpl3aYEWYNCR8VeG_ZHikYCMK-V3stcL9yLy4082_EOq_-eanDCctxrdI3YW_jvU7W2iio6k_iJXIO1wqnQG5qbETzkbj84qo7Ym2j__ZofPoOmdRwCqvqDR3MJ7mr3OXVLCH6yBmKgPiZkjnrw7haU3HoDqwOapRqWND2L_GOJgbvl7uKZ4_-3J8LsinfSEjMARDInXr7_WIs5DPoBfG8G3XicdgXeLhIqx9PXesu1JUp9Ihp3Nbh08r1fHm7Ft01kooLc9oKzpdGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دسته جمعی مسلمانان به خانه های مردم در اسپانیا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81585" target="_blank">📅 16:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81584">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8_Wan5D_ReetptSN6YKibw22z0RXSnL4WnQulzksTTMd90jUzHvjvKnz9aUW32tjBfBHJEh9jLdbx6eEFttUfG_kiMM6_0YE97aB5iDLTExYPCgZgoPy_K3ZnygrFY7xycHOdTuXxwzpRWmmOB7OFecgK6Exsdcyn05YLLvGF-VuLHhcQGr2R4deGFsXw_QbR5YiaEPpX3PLYestOelfzEBtVyagOP9WdbjQUotX6Ng5KRJOkerGdATNnU9KGXJeY3KJozJvezZ7SoLA2F6LW44BajoYvi9OFvJwjv0QCErwCP5f1T2t6k0RuJxFx00CG5qBe9bBK7v5FSVafoREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت استارلینک از دیروز در کشور عراق فعال شده.
۹ میلیون برای سرعت ۱۰۰ مگابیتی و دانلود نامحدود.
۱۵ میلیون برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81584" target="_blank">📅 16:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81582">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFUWObYEUHFWvNL0BQz3IzvBAWupgaHdKBCRXZP_gqwdol61FgUJCWAEnpwNozsJ1ngzhvObCFg2dl6n_7OH_ZV_vLAXA2JjyNM57NPy_uGRIzub7juvAu99SGVw3tR9oUcATjHdAjUDB6mnZqVZvwdc6YP5H9hPEmUjHDA6olWmdzECjpyTPTcqk4KzuNuOpfe4vpZGPyVKvNS46RhM2moG1iZ1wqKfEO4nw1um1k17S3h4rkEy4jGPFvDXyPel6aCMKj2vWuUrJ8BOH9SrjkhfPmrkn3Z0IPJpvUkip2s1I5bRC7F2j3yRVz8cy5NJ1AZ8xT7FRL5QQ1VxrVnCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvsmp8kDBD0I93RurBaukJP-ujodWR3LLl4IIXZJpuffZJU3bi8qU59RUsVjB6mwhf0dHm7Za5Ai4KyZ4H0sX-WIy6S2yN3ppV2gKMVdTcaJzYFYBb0QfpymG5t0NcVX-JpnEH_sM47yu6yW5B5DS1SEekSi6IvmY618RMEqQuEbhV03DfFLbPR4RqOiP0kccxaG4Y5iysqNHmTHjg4Pytyl3etBzSzG0jmeh08urUnBeBLGTWgJ9joPYwFDJh1ymocRXq0BRi5VSzC6YU3ewJhKS4ZXWwEVqzrYe6DXT330a007Lrz7I1rDgFBVo6LlKVU7a-z3GTKpGM1SDWEVrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اصلا حواستون هست داریم چه بلایی سر اسطوره‌های ایرانمون میاریم یا نه؟؟؟
🥲
💔
#free_toomj
#تتلو
# اکسپلور
#پرامپت
پروکسی
پروکسی
پروکسی
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81582" target="_blank">📅 15:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81580">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ao4B4vB_SDqNGVshHEsqmJXdvapmKf_XPY65D1k8O_Msc1fqmPPsqNdSOuUVHtXqIY5jEH7AP24awiJJORZLj5jiHzjR7iCs3hpBhnCdojm2VI3j4redWGpzIQdMS1bsTY05uWM6e6npSeN9mYJg3NizyRo9VX0Yf_5Xgt-bsvtKiXnKSs1P7aqPhmK7DPHPuarhoNo_jIs94AJWPizDujjeWOtA9o7_1IcCHgUA4govbLjEiimpoytgYtAYN_FIzlXSBmtBrqCdAbvQm_s1g__dfEYJoDxG9oHVsvM0AwsJ2kwRV1anh2FtZeOcIKQnG7giAB1tE16oDxs7lidIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHlTF1B3fdTf9tvFINdU4armj9prefj1YF03aent8tHB_oZcV9ZeZWu-y9cRXmYhYVOPduZaIB2H0vDKq6Nna2rXlyBrOOK78PblsBP3Hee7ATGdTEifXlqn5K4L5AQtK_idR_h1HW0E59Df46bgE0wPsOIOLELSjUzS_6cmFD1dXpDfFK-_d217To-9Jgvs4aEMpE7ikIIAaF0P5FVxBeWbBCVsdgsOp9jhka1ATrgdDS6OoddXQGGBn57NnjrpTLFTVAmfIqcQa6oR5qYSuKm4vOYC68zI7dMPOLyvcFvsHoI1eP09yBsPZdRtYsrxK0qW40TRL_vc7hyOtW0f8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت استروئید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81580" target="_blank">📅 15:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81579">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMtu6cFMLGPOVOOizdvJBofZDikZUU2XViDaWbg5fOGYUtVK760BEs3m15Gf25esuVfpWOD855DL0BZ-RUxXwtO-gt-eY3RdNq1m8ZmkEB7FODGdUfqo3ndLcKb1o2YvJfPsaY76yUkOedbksVmHXn4jmC7qMfTAh2dTblrHBFHG6gBakwe2MvuomfGBSDracO8eBVPpETG2E80gg3Ig9GBhKhvEY_yTiNLE_41q2AyjtEfarNDVARf_xUaB5S5V2-1WrqNZNX5pr7rcXURFaGwqUzdXF9KoXr-DQYgtkXEbFmhu7zyBw_-aKTRoRTG1phsWc9stqPfQBk0aLcimhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81579" target="_blank">📅 14:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81578">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ امروز با کابینه امنیتی خود در مورد ایران جلسه می‌گذارد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81578" target="_blank">📅 14:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81576">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوتا کشتی تو تنگه هرمز زدیم، امشب آتیش بازی داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81576" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81575">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آقا تبریک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81575" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMJvIefQcaSLs3zV_drbpssAdjJpzXtm1fDmqtEf6kyQgmKtON6XK7MKu3h--h4nTxQ1pP1hxi4CRQ4848HFdwVmdRHY1yvCAaTq02NyLRsgPfMt-Vp7o_YL6h9g97oMhJc3enQyWgl-4V_SUpHlF2xUxeguVwS4jMbtRHrEp6fdmz7No1Nq5EMN5Vqy1zqJnhohD0-q7we1jBx_uBLDX7dlk5B7EcBbptRjAjofQh0HTEs_-I_Zfpfknnq0VBRt5-NaI4Z9IgVT0OOBXLbzoimZKujNwafSPRkuUgVHVYvmV5SXurJVO8ciQT2o2rGSKAo3IgZlY9VZ0Pf60M8eOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81573" target="_blank">📅 13:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81572">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY7FNfH6fw7y3Oem-H9V6El7FfNwMN_NoTMW6i_FDRl70WS-_KyKQqKOKIqEgdip7M9POTy41kTBUIkT1YGrMfjPbKn11gyn8KcGlGX2nuHyBKlAmxDJeQ7jjakcSXif9IKFab5OXvLnauiElBYUcowsQWGTVime6v3UdzNPR-gQe27bA4ybcz-GYzuPr7IuCEVqexiKvtbB2tvBT0vXqI5m4K07G7o6sB2cyiTxoe3v7Aq0_46CLfFUvzhnTmKotqFDguvnbzfZlxlOv7HOk4WUxcTJXYylnz7Mt3WNxcwexpXItl1ZtRw511IbbSrpx43s2yJBk_YEF_iz5MXCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر وینی چقدر شبیهشه
(پسر دوست دخترشه، پسر خودش نیست)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81572" target="_blank">📅 13:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEIy4qIUlJstEQ-m2UbW7CKohM4OSH9SJBIU4J751Rv8OClvDxX-xR4NBBLQxu3kSz2DyVQ-2g_jrGM58L88Y6GEXryM_TRB1-3QzrAhkmqF5zXT7SYyxBMzDKUmF7eMmcww7zhP2z9NVzuTnlM7fkfnhtLueuOQeh9hU-LnRbP0NNLvqldokDYUNgeqs2lbOQcT13rUnhNjxrkXqZDohFVwAjVuv-AISQR7z7pWicQ9fernMDAKb2wZqcYWtDPGnNPpHGnRrn529yi14Ar4TiofZgz1OCTANwN4D7xTLPpL_u8qUhOTv4Fx_sDA1xQOChSQzMQNajQ-sBz8knF8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81571" target="_blank">📅 13:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81570">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2lw_KpiHt7WYgNsJUYzSYi9grIAQMKHVjjDsEW4AAFeF4oJjWF3tDdtkypE9GIGxMhf7nSNnJzlaPe_4R2HstqPrizRI8NUKlDerIXr_lPqNMAnms0xa3HjZbT8AViBsioQB1UeVIvno9dN7yo5k21128bqKHboiQuWXXgF9qy7__A98VUCl2YphNaBBzjDE4-E55nu_M9pIxCzxbZZTpdgXtxkmjr26CSbdT6BBEOeHnweQ58NHDE9B6Bg0NI1193v1JmMtXeLxP4tKegvyYy9jHmBmQ4yz3ZN61v4DRl8PXbOet7HJspcQnopgTHN7675q8a2BQ3FtnwWvXhBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81570" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81569">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMRSjBm8C4O34uq8DYzBKndV3LU9Zp_zuYTCNUHj8FrtW7EAma4jB4VjFjkXlmGRFgBuHZ4vR4Qrr3PHOhdCyFKcgFKJn0H25arj2Ax3ypj3gCldw5oYi6c5AZZukQDShIkKw3M0QpGoxhNxrod3l7KJSmFPuky8lZ332UbWoE2qJIig2lh1T_gKysN18qXcvG7Y_DNK6nQFctomCAXKKVqU9AdQKa-P6_Mp0i14lfjHBtGI2DxlvDHxxhXl8WvOgp7YRz-gmGmxmn0Otrbsb_Bv8hJLM0aAT8W5FDYmrpuvgN3-G5iTY4euF4T0po3mP-HiB4igzwTTCh6WgXtbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81569" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81568">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbEGlqyCSK-eBefgqKXsXt4h4RF4jKjv52updaXCSEagSYYEmycynmSykoY4xPh6Hm9J-zKImZaC1kn8iGe4T2FaPb5QJiQ8iVpHQolINajsnUNn30QTgpjybg1nl2xkUYXPSoGBb-Nw3F1DzEtJgQklOZWWSM3eaYVG8uLAxeuGlUA7rAQiURKW6MG0myxQa1TSzKsZog_oES-zTwwUSCEn8MHkvTgMuqrvdF1B35D7pzpdScojxxx9ZGxJQWnFBQ6XujBBltiXgpzN2fMgkAwuAGWK3a0JhhaKeVfozpNJir61qY-s_ozumz_mcAUSbuNFB14uzQ6yOqYqM6qY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81568" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81567" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81566">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=guPP7APb64vuBgaf-PW-QscrTFZJ-G_88bv-Zlj9gjuQ3fT__25-0EboiNW7W32cZeKlUr-4BR9FiQGCOf3KkixzLd-AmFir_v6grf-rYUAGYHgb773-XGpWNx9KcLm7batUmv4ZmFkqZhK0-Q83NXaMKSK7JeWYkmsvt8Vn7pfl51uqh90fpukBL9ZnS2_EvSBrhIIX9xITNj2h4ctYCb_IYmDbvOI2JgiU2_orvxB5ohVJf9ISz15zzt7jih8PTy4apBf-7cz-OmQzpLBiJeG2mnA1jSwuH9F4uJnqGlIZWiwPpV6WslBiB4kot25JMIM1dfc6p4T40HJLVx8N1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=guPP7APb64vuBgaf-PW-QscrTFZJ-G_88bv-Zlj9gjuQ3fT__25-0EboiNW7W32cZeKlUr-4BR9FiQGCOf3KkixzLd-AmFir_v6grf-rYUAGYHgb773-XGpWNx9KcLm7batUmv4ZmFkqZhK0-Q83NXaMKSK7JeWYkmsvt8Vn7pfl51uqh90fpukBL9ZnS2_EvSBrhIIX9xITNj2h4ctYCb_IYmDbvOI2JgiU2_orvxB5ohVJf9ISz15zzt7jih8PTy4apBf-7cz-OmQzpLBiJeG2mnA1jSwuH9F4uJnqGlIZWiwPpV6WslBiB4kot25JMIM1dfc6p4T40HJLVx8N1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81566" target="_blank">📅 10:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81565">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvTuze2-1YFuxDrlyUWy1BpaX2MYSJeUbRWnn4ZHq_T5fDZKjdbKw-jpmSjloU0IrMKQphhQS_dKcjCBFOsZsm8al9SKHr9KFbhdjTVU0lz9of8JijB6kLV60c4Z_HmsAcQGLeT5rGaJIkalxpCdasddygFx_zTGgMvPw_-ChCeIEAhkHUo9dhQaiL8g9X8ZBiNVtOEcfVnSQvK5Xr2ADet0b4SX_7SEWAbcKSe_auOUvajKj8mQWlqm_4clGCYl7E7XN8u62vtnoswpXEJNYVWNzMQzD9RUf-qgb99gqlFN1IAEV2cd3avzCgxeMcpEG0NU1GRv7xik2bI0uRQ1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از این تحلیل کارشناسی شده‌ی رائفی‌پور، خبر اومده که عربستان داره برای حمله زمینی به یمن آماده میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81565" target="_blank">📅 09:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81564">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76336c1936.mp4?token=TQO9_xIyKKDOizh_hxBevgZvUc9Haj4SLNUfCHK2UVTz3gHI1PQ9-0tw_qBAX_WTT73l4ERgExkcsDSM55_ze714_vUjpGzo-nQAVPZQrKIKNeQMp7GjgbqX-IXjdJ1adwdRzjujPXk59R-bYbor0JF52ZSC1AMlncujuZc8QPcLEv2by569XKwErgOwBOvF1i17IyvhWjwHakA3j2eGHHHEob628JwUMXSYrnQ0cAdsFpywjMVNogwiSArJmO4HhujGEBnCyeDayuY0elhiyf94UEV3-wO0donB9Bsq9y_jDqvgkDPrRn8McXQJ-cJq65klt0Qja0EUii-OneE0Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76336c1936.mp4?token=TQO9_xIyKKDOizh_hxBevgZvUc9Haj4SLNUfCHK2UVTz3gHI1PQ9-0tw_qBAX_WTT73l4ERgExkcsDSM55_ze714_vUjpGzo-nQAVPZQrKIKNeQMp7GjgbqX-IXjdJ1adwdRzjujPXk59R-bYbor0JF52ZSC1AMlncujuZc8QPcLEv2by569XKwErgOwBOvF1i17IyvhWjwHakA3j2eGHHHEob628JwUMXSYrnQ0cAdsFpywjMVNogwiSArJmO4HhujGEBnCyeDayuY0elhiyf94UEV3-wO0donB9Bsq9y_jDqvgkDPrRn8McXQJ-cJq65klt0Qja0EUii-OneE0Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون سر شوخیو باز می‌کنن بعد تا ما چیزی می‌گیم میان می‌برنمون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81564" target="_blank">📅 06:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81563">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81563" target="_blank">📅 03:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81562">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81562" target="_blank">📅 03:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81561">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حماس خلع سلاح می شود   ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81561" target="_blank">📅 02:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81560">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حماس خلع سلاح می شود
ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81560" target="_blank">📅 01:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81559">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81559" target="_blank">📅 01:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81558">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=DtcCNOk0s1KRqb6nbYxLogU_8oywFyZILDKwA_jlaVBLUZUO1fe0DlndXmKBl1GUgwseYVcIusjZtFXNh6fqllobi6CWpOyP2b0HwhOFM33wZ9bKRiZdwb1V_sS6AkHsRbZvByVSDjykTsS80n8B4D5isOswdnpQ-LT5fm_xc9bjtZovN5K6KcZXwFrwp3NCERhor7GqDJs3W5TEMLEok6reeV9lWYKXhrXRhv57woi2xicKL3e31Gq7OrnP4wZeBUuXNccG8KP1NvgJh8-MubQSWjNS4oS3jfUmWkSwXzzRywQwmAz9WK0hshgYrwJyuZTRa-clyYcrrex3arHASoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=DtcCNOk0s1KRqb6nbYxLogU_8oywFyZILDKwA_jlaVBLUZUO1fe0DlndXmKBl1GUgwseYVcIusjZtFXNh6fqllobi6CWpOyP2b0HwhOFM33wZ9bKRiZdwb1V_sS6AkHsRbZvByVSDjykTsS80n8B4D5isOswdnpQ-LT5fm_xc9bjtZovN5K6KcZXwFrwp3NCERhor7GqDJs3W5TEMLEok6reeV9lWYKXhrXRhv57woi2xicKL3e31Gq7OrnP4wZeBUuXNccG8KP1NvgJh8-MubQSWjNS4oS3jfUmWkSwXzzRywQwmAz9WK0hshgYrwJyuZTRa-clyYcrrex3arHASoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های جالب پژمان جمشیدی درمورد شایعه‌ی جنجالی
بوسیدن دست وزیر ارشاد توسط ایشان:
آقا حالا ما نشسته بودیم یهو رندوم خیلی اتفاقی وزیر ارشاد اومد کنار ما نشست منم یکم چیز شده بودم با هم گرم گرفتیم و داشتیم می‌خندیدیم درحالی که دستم تو دست ایشون بود یه ذره خسته هم بودم یهو سرم خم شد ایشونم تیک عصبی داشتن دستشون یه ذره تکون خورد یهو دیدم رسانه‌ها دارن تیتر می‌زنن من دست این بزرگوار رو بوسیدم.
😐
این تیترای زرد و سخیف و مشمئز کننده چیه می‌زنید.
😐
چجوری می‌تونید نبینید من همیشه در کنار مردم بودم و برا همینه یک هفته‌ست باید با فیلترشکن وارد سایتم بشید دیگه مشکلتون چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/81558" target="_blank">📅 01:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81557">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این پست مربوط به رپ فارسی است  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81557" target="_blank">📅 00:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81556">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHzHu7leLPcDk3oPi2CY18tBSmDA066JjHtEJOY11w2wSNMyqDgW3QJbbdeX3HN4prv9ynwCMO4vaJifXG1UIoOIXWGaojL8qVX96nRrz57_INVrB75KWHryQis6dfG-Xcz9c8zNQZJNWQWWPGPf0ur0_akiLgXMHJPSHjM0LKxvCzRSV3B58ofXebG1XXZfaXwzNs-JzC6ipySEOXHydj5lvq_G2GGC4j_uJbWTzqWy3FKvNov2GxbcDvY-T7FatUt-_-DzrawNsmRR1UmyPL0oQwJn8kliFIj1wTlt272BVS8a7G-w86hfZ0yFqx-Ji7k-Vdr3YQ03G5hE0OwRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست مربوط به رپ فارسی است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81556" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81555">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دادستانی تهران علیه افراد حامی محکومین اعدام دی‌ ۱۴۰۴ اعلام جرم کرد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81555" target="_blank">📅 23:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81554">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INzQXPASjT8wmB6PipR01yPQ9sJ5nLfj0RW3rT2tj5Au1jD3LRyzKB5iZfO7huufriOdDrr888eMHkENPmYJckFe0ZukKHrQtMLP-HPQtjYnFHSFfOYWztiBz5dzAajwdDM3qgGU2S9vcx2PMTKseqzDyWPd2ullN1OlnE4VHAHMcPlSR7SzujKpuO9Jmfz8-vaU9S0OLufjEVJ227XWEUNjYAvVmsKE_wqgiMn9pDJAA75lanCki11d0SPYPsq1oWUTyvBclxeZxvDdQCs_IjcpHMxsmBkskEofYPMFp9Q1P0twGfBO5CKOAciy69-g-BblzW79mmTRWeQvfQ7DMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها ده سال تحمل کنید تمومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81554" target="_blank">📅 23:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81553">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37370edf56.mp4?token=qL8CgC8wk_4QxeU4it5QS4Y9xcl3xTUyBchoFiRCPdfySpDwUbUBIDPS1zfhi-8WZl4IJWeN2cfSkWDIalevGlHMBxBBmFo8dNF_ksc6tiEJu9WXQZH6kPiOuzp6M4AnKGuBAFDHkuutKGmjoUbH42Fpsf5KMmCfKqib7uLjdJfZy8X69tGakRGaIxFrluesdvhD8QPISKqr9YBD7i58yVEgMkwQkcvd-hyYsYcu_L22oFDbprii1xqJeqQDbqvMAU3YoqJaUqpKWDaMJTfJGrznW3eHu1oWFXXAKi1_WS5tE06iuwxTx-5auMdhdJLn895iLYWGEsUHGb_GyQ8iiJa6ARyJd8gqT0qEWIM-d7EFE2fp-m_NhCXTRCzmZo0jwspeLvx-1_3-WbW1KEk2iKM4n0rp5sARK80Liith7ZUVM_63vo_TCx8JQ-pHw99Ic7QXampv6_d3WZRKylzgdtST96gfGzNJMBTjV3_YeOGWC6ERP0uCydNVjHPT5KrM4eebJ0AYdyZzMWYw77s3pQtabYNicvhLbm71In1LBXGR8cuF7ild65cD_j_DOSlP-n2CYp92nWrhekCcqhkWgrb2kA4ip1zOs1rrMYlO-4SpujKhUiFxO-5LNkqRBqX--xJuXHeqxbnlR8VJZ8FchFnJj3Gg6F3NpJiamTK8m4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37370edf56.mp4?token=qL8CgC8wk_4QxeU4it5QS4Y9xcl3xTUyBchoFiRCPdfySpDwUbUBIDPS1zfhi-8WZl4IJWeN2cfSkWDIalevGlHMBxBBmFo8dNF_ksc6tiEJu9WXQZH6kPiOuzp6M4AnKGuBAFDHkuutKGmjoUbH42Fpsf5KMmCfKqib7uLjdJfZy8X69tGakRGaIxFrluesdvhD8QPISKqr9YBD7i58yVEgMkwQkcvd-hyYsYcu_L22oFDbprii1xqJeqQDbqvMAU3YoqJaUqpKWDaMJTfJGrznW3eHu1oWFXXAKi1_WS5tE06iuwxTx-5auMdhdJLn895iLYWGEsUHGb_GyQ8iiJa6ARyJd8gqT0qEWIM-d7EFE2fp-m_NhCXTRCzmZo0jwspeLvx-1_3-WbW1KEk2iKM4n0rp5sARK80Liith7ZUVM_63vo_TCx8JQ-pHw99Ic7QXampv6_d3WZRKylzgdtST96gfGzNJMBTjV3_YeOGWC6ERP0uCydNVjHPT5KrM4eebJ0AYdyZzMWYw77s3pQtabYNicvhLbm71In1LBXGR8cuF7ild65cD_j_DOSlP-n2CYp92nWrhekCcqhkWgrb2kA4ip1zOs1rrMYlO-4SpujKhUiFxO-5LNkqRBqX--xJuXHeqxbnlR8VJZ8FchFnJj3Gg6F3NpJiamTK8m4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/81553" target="_blank">📅 22:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81552">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GRKv9uRnN3q6-_HoJj7gQe5aaI8ZmoOc2-4XRSoIO_YvJVUpFjeAHDLdnd4I7oCLLMpwroraNssmkLLs8xPCbicbpFT3Eam_lDoAmd0mzggkWShppHCzeIC0kV_ejjztqbDrHT0C5zGnGXcAnHZRiKpMCsuffTZ5txhrmyGxXPceyhIFEcw-XEkufSk1r8X-0-CjOxeVqjk47vDkR-nj5UffHmmeJA2i_B_sxUGTroRhV4dbhVq3yzHVtr2KJjFZiWnbbG5cSGkBWEt726n6rGK1v7u4kJ3GCEEF34htXGQOU0Sq5IFkGGxwFRBxUtxvhSrOzV3fmAwuKzAfaiqcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
پشمامممممممممممم
نیکی نیکول دوست دختر سابق لامین یامال پورن استار بوده ، فک کنم یامال وقتی فهمیده ازش جدا شده 4 تا از فیلم هاشو پیدا کردم براتون گذاشتم ربات چه
کصی
هم میده لامصب
چه ناز و خوشگلهههه این دختر
😍
مشاهده فیلم:
https://t.me/Footballi_Dark_bot?start=get_tbcbmlqhfqdjyaew</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81552" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81551">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترک جدید مهیاد به اسم چشات میگاد ۲  ریلیز شد    SoundCloud  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81551" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81550">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0N_uaWWCMm6SSy7cdr7Pvr15SpAqYSpjLEC2xoagUOJlWOOeNbLcXKcuYJLCsVMkei__YuYMZnRtjWSm5t7V5HKvMfMqwgDAgqhCJeUiyRNyR3JwKJOhbAWqAdkDKg2UtnyrbirpRdNnvAvBWxjFeRxKrW04PQveVstdtV1NSKwTnb0erfvenjFdb9ZgBxT_R-CZgTLABtTHEBw61-cbyptJKb4wM-Iepd9vovdm-hJgoHvrn7dCHWVmvgRv0YOSFF3v5jxv6NqC-4zPz8xkmsCYHHn98u9XSyDfxZvRCYIy1-3iaV_x8cIA52zI_TOj3IE3XZ0YkLO97dwRxDQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
مهیاد
به اسم
چشات میگاد ۲
ریلیز شد
SoundCloud
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81550" target="_blank">📅 22:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81549">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-NyyQtg7NT9J4nVQC8RAZREBdVnMeKAHKl0sboFXrkjmZibrRTHhOKdlY7jPHA8sEm7cRvka98gsqnaAHyMYyI1mi4cdFbkwEja8RADgk-3rfa-272ayL71E_HtQTLw5I_c-B2bpL1FTPhQQ_2Z662JGoyVlxRs_bCgij1PYRzv0N7VuSRevGxlnOz96u4AVVF3E29cJcXAFXZCklX2nuWLk8h4aJMNq4b9BqLH18dB2IFqR3_pkepsKnUlq4qwnaatB0-UZzgngvKVHjE3hfS5gm9zaY-RAAs0fqmnLlH8kzT-LhZ2AyR-21rQn_6ArvwVTzakL4VG9V2RLotTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81549" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پیج اصلی سروش ولی زاده برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81548" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umJbrKqAmnZqKyyVBCoDjnDt0Mwma1vyL1xB1P4W5HJI5N-0hhw7novHd-IVJzD0rUaMb5uCuxg_a2j4R5C-h5B3_ZGNwG9ekIKK4up9PhgB8R-Kt_7qtIykjxx9MWw8hpksmkPCvrOT7wYyIlyqcsmf1k7EEsw2xa_lgA2niHsX8_hcA3cDOry5mDG-Mrc7H21wihBUWHNmNMVV-naIMgWLaPtkRt2fyp2IqpicVYbUYqaqcCwW6IlYsRzPLedWbBC2jEn3fsYhgYIQMlGweFtHgGrwlf1IOSPRUtI0ks2jq_59Djwi9ANkc8vKzXH0Gzk6Hil8bUhcS-5W2T_hcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81547" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ8NA9G0mkb7jKkwBu6k7Nr8JqH_ZJZy4Gab49QBJIt-cHPNYYedPsFhK-pWZXNxy4TmYuyZgJ91H0W7tXtQTgu5i2bqyg6Ai_gG7RkHTl8B6M9M1qUAXOPJXx1pnnCS8Ga9Re5LLKGle1HqlUk-CaQKBqAzngHWs7GDFvY6fmk3eEYCH5hO0_BnnMQy6yY88LGuLBDHCY4isDDBbDEZBqbWvZ6h-j75gfl6mGe7pr5UGv7XT5GajTRDhkWDg0-zfwTBMy2e4pR8ZvwBaO6GTUbGMud-8aKbHE0C99ptQeogQ1mNbSoV31Y2G11_rqMAEGWSbym5qytxTZvhFkVf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81546" target="_blank">📅 19:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqhUDQ74mXuj6frSXHdmNxTCLD8AUw98Ml_UunEHko8sFKNeOVUGpk6poaJ0mOvQbihGm5sAJkV5OjYiUeqTpCAkRJyx_RV0Elr21DhV6a6H1tvhto9KkBvzjWD3xvhh-S9_ebZArsPsAe9WTe7bxczxNT1kiIJfQLSdjUjHfDP2_6WyX6coVzGFrBxI-m5QiICnHdQYfDDEb8E04Ml-M1HFblDodgNOKcZKoF_aTprkAHKhCbAQWF9VJuSEWMkfed-rKaT0xyK6Psf1aWXXDElEc-k8gO66FrVhqBTa1LWqKl9nwetfLHDVe9l0GulNlw4cqHEXQGA3S33qzZIhgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81545" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81544">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvwlBVessC4RKq-qZZ8LwK1Iu9bfsM9iuqU9QJ8FQQj6ZbP4oBg_v9bNOBrxY_0nhaU2iuvSvIQE5YkAIDbHlUpT63cw_TK0EoHklNHYcGHKO7LEFeGh4MkGreWYOTf4EMZ1Bxy8824IWKRLdt-Gv8MS3tA0K4U4-FxBKZae_h8ajRBByWtJ9t9daVc98SEyMxd5nfvYeCIGlEmtRky7fflnxpytvYHlvUrDNzj2DsB-pc8QJQ6R7s91AZJ-6eioGU5p07L1z-hBaCa68FdVo78yBsJsCrX0Izqvripqmbuc0pPm2OAMjMgNw6zEc8h0mznzJWpBjA0e-zy-lTvA3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81544" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81543">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3mm01B_bNU8PBKEuuWmt4XxB0UHGJDJfstfdfQAw-yN2BNgNcK0jfJ31xXtWFsjpw92g44HCcRGnP3C5N9wyP8cgDCTrjGw44-k_AUslE62rllFIKuEYbq8BqsE4uBjGNXcNTrQKnsfXkjYBwBLxazz8msv42YmFCmbVL_PKAVG1AHl4ugdKnROZRSKyLVi6qp6QeP1ZLGUn-0u8T0yTSlOvKg2RsXPDQ3A0lkdJL4kGMZ7S666_wSkank17qw7aUIGQXLwfriGuvo2MtffSmToCWNXk8YVPlqwqsjFpbF9YDtMDXGRFegruM_Yp9Biwu7HsgFFpKrFPkd_htJd2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران:
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81543" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81542">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKV8C5zrGbzm91KwewZAHm7-8mNU6vAKa1E3ZJFjjraGPNW2spgYpXW3vzib0buSiDfMC07A6B-k2PXKEu8wIxS400J3y0vw_mmEKGh8n4ktChbNo2MgPUABKSQ_uAvgs-knnmBpR1uiUNr3djUBwsgHcIgCM1-dxPdmi4eSCzAn7IUmh3f5vHQgBNRGOUeSJ886k_DAx7oQHsI49g4GHCHwpH093GlzNSvRanS3ccZP5dtbSLkPyMblYgfWuXJ5VwqVNhi62f_8XpIuxCH-0RbHKj6leF7cwihVguNSb6ctkjvs-jtOFXwPh415TXTuGkKclb5pAxeZYxzKw3-HRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلشیفته چقد ترسناک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81542" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys7z77uxa7NFyTxhYQWaszvH9yS8kVKII4xrM4SS-4qEhg35659VmFLFVeRicjHHY4LpgX314h_SiEdPm47aQ1R36qQJS3rZyWNipSnDArC2_CB75reGpwHdcS1Q9-z2pbJm6lRU69tEow7bZBdmaU3sD5EMwfHD64saM27eDpBCqv7tvH2y2UZOJkEWJZbAG7hQleHwvxIpau3xW_2zgLdaUdxK1h5SsxW9FCpS_TQ6xy-ZDlClVVeKjREiuueY6upfnjF_wx1qE_G04bjwmC44DwmrNZO6jS2ksv06JhBa7k90BUZUXeWHi0jSISl5W_0kaGlw-LMmH4dwvJVgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmlGouY9Lz1W5muAtscMQASWkYMkOlYziRheY5yNAGXpXne1gctvuuNC8BJ7GK6utWUurwGlLP20GKBeN7vZYAt6gDIhchCgtmn_5jMD4-wp1cShX8sm7Hxlf2ybpRiA-SdUxRBMYLB7QTwO0G7GzrDig7S2LO8PVt5ork9y1snmd8Vi3lFNCLTJZA6bb75wguSYjRiW4P23NDLS3cU6j-hsGHjzXvcKGOs1LPfpi-GlBMlIfsdz2IyfSF31m5r44DLY5Lr3-TguUGwRwezvvu1iHeighffeSoHMkOK_hf1-5BCMlY1v3qxLQ_jMUZ_y5SW8ffXeypiZdLqHaMrWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzqqroVYXcje5RMhNl6tYgnG4NSPVheUbgJCG25eVcAxs04OSbQ_7mT5Hb1t_H-4KPujrdc1mE5-uRq3ApQe65x0gutVvWx-83hQYNlLOhismmQBiZb0nwt4JKTIORuAZxBaDJVJZjI_c2J9mlxJ3QG-3U8ZfT77NuI9anZeA_kpVXNKs3Z3yCcmrCn4svnX2weHN6zB3QIlLH49YwyoGSJxJxdbezqmGty9myWnVMsY_lBiQHYMoLYaT1W4-KGH_wlRMtfNDvswVwjgEZaKD-AhmJzLfARLeB9yD4fdnr4KhmWjG7Ppj5TkrM80tI9YYc5o17TnLqbLYQn1nfM0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOuu_baz6q-YPFl11tPspLykEZrHcTy7JT5B1LtdGdyKwwzRNFnMVcJBhHaoyyLvl6ZExpnLry8SAoJh-Kan9Fo9RLBNVcu07U2hwcJn7Pldb4WFOmiMRdwr5zP0XPH4TMy4zmuMX4zfiIzWwM9xD3SeZZkgvumY_MzwvFvR7lumyXWh6eTB0tezLpMb62e1TgGAIEbM9I6n-WXKAMTS3FQxkOGa2gU6RASbYQziS5esLgqEdf-zMGH75045Uaqmi1mtMIr746i3OB-Ikr1E4tmWhnqeQMORn6QlNXjdQ3iq10OEkhpx70prtr7Dwp0616FK-4ysomvcGYaYFDyefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhsU8_w9JG872ZHf332ncrr_059c3EyA8as6W_ZHqU1n_JoboLrgAfLQwmh0xjezix1zbfod0k1TRF4qL_vXN6c0l2Oe8SfPLGuBl2s0AzPWAlrwRFU-1xXeMC8luNgj1nsAPnCNSnefVZQpr2X5v-UulOglSx39W8Cgpkynl30RdRfQt4QU0WoZPkrCD9w9dDEmYkJBzgFMbg-Amig0L7uPNuSgwmYalAcj-DG4GpZkRiy4dEKc8CCQY0HsM3rwQG9JLBKehEQHsUqcN0QvzXU-YFNaf-rJp29sAkxlemSaxA7J12_d_AO06YwVqBs_7_gaLX2NtH4cTMxtUwXO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=OrGodhnPEh5VP6maNOPKywiUtj7u1CrQ19nmIAcrmhpAHwreKxyhQq7mPTCa-8uOyLuah2XwJprSvoQ4N8tyfO7T8Cb1tKE4SkW_5BxCwBmw_K6WUMQpY1iQFdAEJyd4Sdw504FKglssypD0pwpSNwoGuA3DK66jgRYLGxSkRmZ7hQPKNn2PbsYDzp_mmVtNnK45vQfBLIw_-lb6Mm3uWf30Paex5Bny2xAZUCF2jZ1XxmfVhwko0M4S-ihxqODAPngV8zBF8ciYPqPfQXA4PNqFQM8VjXGjj40uRBAbJy9Fqflzp07cCdIvl2NtAzqbjpHt7yGm5Am6Zu8lDaoRTTQAeByUNsMszdhp_9K5AGOiwx_IisYoWlqJfK-HgrN9S87PL3qTzoERWBmC3IrB2vCpB76oBXSDcxliqldgL8ZZUITTiF-M_nN2CrXRopLyNIK-cPm1ARUpqD1hfum1tb3dHSGj5fLLKkNCOuUgRtf4bgLOJPlUlMUaJE0RNs-D0xp5IS5AZw4UibU9EFGt39IQHdkY48BDza-9FIuJP4M1vYGIFMVsjU5O8ppnAKJ_k_dq1sfKd6eLt7Triow9NGUrZkC2-zeT2F6HP-JfFH2FU7x19if0vlcbkOpwTA5hvHuVzhy0heABokInb0-Bp6rGMCQ4JYhfp0lL7bdH0qs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=OrGodhnPEh5VP6maNOPKywiUtj7u1CrQ19nmIAcrmhpAHwreKxyhQq7mPTCa-8uOyLuah2XwJprSvoQ4N8tyfO7T8Cb1tKE4SkW_5BxCwBmw_K6WUMQpY1iQFdAEJyd4Sdw504FKglssypD0pwpSNwoGuA3DK66jgRYLGxSkRmZ7hQPKNn2PbsYDzp_mmVtNnK45vQfBLIw_-lb6Mm3uWf30Paex5Bny2xAZUCF2jZ1XxmfVhwko0M4S-ihxqODAPngV8zBF8ciYPqPfQXA4PNqFQM8VjXGjj40uRBAbJy9Fqflzp07cCdIvl2NtAzqbjpHt7yGm5Am6Zu8lDaoRTTQAeByUNsMszdhp_9K5AGOiwx_IisYoWlqJfK-HgrN9S87PL3qTzoERWBmC3IrB2vCpB76oBXSDcxliqldgL8ZZUITTiF-M_nN2CrXRopLyNIK-cPm1ARUpqD1hfum1tb3dHSGj5fLLKkNCOuUgRtf4bgLOJPlUlMUaJE0RNs-D0xp5IS5AZw4UibU9EFGt39IQHdkY48BDza-9FIuJP4M1vYGIFMVsjU5O8ppnAKJ_k_dq1sfKd6eLt7Triow9NGUrZkC2-zeT2F6HP-JfFH2FU7x19if0vlcbkOpwTA5hvHuVzhy0heABokInb0-Bp6rGMCQ4JYhfp0lL7bdH0qs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flHOkyj7Ezpe2ZrPlJIJrjsRiw4AGPSAyMpkFlnC_xLcbYY7LgwZLShUijVvQ6CF2aKo8-p4_G004zzcqVQ7GCiH57VglzEuUqp9FY2xqVveSARWTbXd5rQZILI6LfyyLgDIDHhLYgFyxSFz_CcGCis8urjjiLvNFGSyt9_xSKQvfOpFd-Vk1dvNQfEi_D-qhDlRNezwttxgzqZLIxYS9vas2DPPEDr_phKFxJxUmQDV_NDz46d6y_s6VgRRBfYzRpZ82cOiHtFAF62f764SuZtIAtGxwvex0keXXntYjbXe-jYDc3BmcHTk2Wt0RginDqE0zKYizvE-smHOMTr4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shaSba2q2Ftejm_61njPh0cDsJs1YkGIRQVYmHcOsLclV6h0s3POBEFDE0c-pbfqzFi2Tx2s1_scbwMAPWwvWoHCRoldSSI6C2Q6itTTvj_XJ3gqfBdIUUbjGDJtaOernpFdZYVcFiTEh0YTdfZf4b3uHbXff7c5NZKMV3t1QqRtDKUtsT-WXTfb0IUdzHt5QJ26ukvCWfXmUK4N18T2RzjwozR-XcOAHvOzm6jw36Pl4Gzj6uZQrFUUxJuzJ5VkKIIo7H06Q-jGDDQHVNWPWYZ-LsfZ-Nv1k6HypQ8lh4mCF6jltFYpZ4S5vvPKajyqK2Jjtre0ZusO5fliHKvdXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkXTLOedgFPrD1jYP-obbDXOxnP_SDlwayk_SdG_ZnGUPWlzSNf6ajhxTZY-4KHwHO2VkHhUxE0Q44Ur6RLYwZ3fzRreddmWd5nbh-7nKX0TB17K6B3pou0_Nfo6GR7PwXORCLQ4fjYBY4siwTuHfrUVmDL-iAZaxUn8xd9HnDc5E-GkMGF2_ecxywaitz26AOfEnePW4_hmrroh_V9T8h-1g6z-arosn8Fgwt7PfvpuCA-isBmzrOHp1hesVXaRX2vzU27KfdgSy9UEay1wzlFJUuepIhQkFNsGcmYa8Anuzjk6vgbMz_BiuxHKaK-zfBm8r5Zc5XNpLXlffkAigw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=ZIEgbcnyXqWqpi6wzu4ofr7xfUuwz8_wkogU5XplxHlAu3m5kCB465X_ZhjqVeG8LDWQ3rFPtBxyQE9TwNSkV8XwGsT1LPhGEik6-yPy4USOdLJ4Q5TJwwdBfU6j4BURwcl_KTBWSiyZJKMzEUhSv_mehSB4Q_3CZpWfIPU5oCkhQ0DMCkjaL-m2NhxbLnaEr0O0iMHZwoasWyhtdEMbv89n_G38j-q0bw2xde9PzRzzzeMN8WO7qGYKWZBzWQbt_-bwE4faxdLk9ZwujeK-bVlE8_opAIEsVG3E1BEOaDs_ocmcpG8QIPFLzZJZMm0rp_D19hPgMVldIfm_L2Lcbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=ZIEgbcnyXqWqpi6wzu4ofr7xfUuwz8_wkogU5XplxHlAu3m5kCB465X_ZhjqVeG8LDWQ3rFPtBxyQE9TwNSkV8XwGsT1LPhGEik6-yPy4USOdLJ4Q5TJwwdBfU6j4BURwcl_KTBWSiyZJKMzEUhSv_mehSB4Q_3CZpWfIPU5oCkhQ0DMCkjaL-m2NhxbLnaEr0O0iMHZwoasWyhtdEMbv89n_G38j-q0bw2xde9PzRzzzeMN8WO7qGYKWZBzWQbt_-bwE4faxdLk9ZwujeK-bVlE8_opAIEsVG3E1BEOaDs_ocmcpG8QIPFLzZJZMm0rp_D19hPgMVldIfm_L2Lcbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه شب گذشته هم:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=JyAZSMCITghmEhTYnKrdum_b-HNO4O5FwAwwgTFyIs3IVgPhU2NxOpvb1LWucd6Wp5bPhXIgKUsFfjCSPjyrtyCupbR1BkKnoNXWNOyujOAPIpK44ZVxs1mrLL3J-Z2YXkSpya-F8T6Jl45XQxsaOntRqDJSKMbH5xQftYh96Dy25tmDfaGKbdfdvQPibXF19LWVQbmVSKJz1iVUtNhVu80_v1W87gA2JkTSvyU_m_GX21yVoZSyNkMO5k6vsgHjHDB-Z01THf_say_R5MsWG-A1jiUPHl6ArFk3X9bb6iXnIX4v5Sme8PKGAImQRpgsSURUqx8AJIhRNMDEK6oxfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=JyAZSMCITghmEhTYnKrdum_b-HNO4O5FwAwwgTFyIs3IVgPhU2NxOpvb1LWucd6Wp5bPhXIgKUsFfjCSPjyrtyCupbR1BkKnoNXWNOyujOAPIpK44ZVxs1mrLL3J-Z2YXkSpya-F8T6Jl45XQxsaOntRqDJSKMbH5xQftYh96Dy25tmDfaGKbdfdvQPibXF19LWVQbmVSKJz1iVUtNhVu80_v1W87gA2JkTSvyU_m_GX21yVoZSyNkMO5k6vsgHjHDB-Z01THf_say_R5MsWG-A1jiUPHl6ArFk3X9bb6iXnIX4v5Sme8PKGAImQRpgsSURUqx8AJIhRNMDEK6oxfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQfmcPD_PiJ8z-sYPFVEBAzH2NjYTruH_qKDgtjQA8-aAMHP7hxfoNUb_6UqYMPoA4byHSViAS3ZTztRO36t0tkqs4MHJpPMB3SFJhlsI0k0WOmrN4ChdIDp7jA5KLdtZw7fpvqB7lqlIs9ipx4lqkpUBS9gmoLhvb6D4UgPc3ffd6hVbVV4bS-0LIMd4BjnNgV-f-Qxh9N6mKCwQmeGq7LZPxFExPRZgLHZDCdYWYd29zD0GNVq3dv5ihVjAGYQQ4YmeWt6ecallOi70L1LZGJOnvZLphhEXu4WKfTneF71Y7WTykoHaXAtyrZ3L0qyjFYe2kd7pvEkzqXk6ymNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8a-QbTS076K41WjQZ0e-Yg1ns7zo-1gbq8tvdjAsNtBd1SRTzKad--fSxhL1yX7noHoG3WdGKq-VbFNknKmmA57LjYjX1GBLqEN8niJiBJvm1YNzyCKQY2OfvDYPbaSJECFpN1sivwQHua4OCnfleKebYiuVVSsk1fyDaXewWnbsATaoz3MWQwLVeag6gNcpzEzpcPGQRi1MyuxaiqmXb5n5ct3Bj_t7oTR3APjXGqJcsYCzpuZ3-9IKQJJ1lPo_vejrnD6xzQW9Utx-EFUrMZzzz0StO4wa6cGzzxC1SY5ku0UhAMotGDKOtMO9Fd6WoUR1GSlXunhDr_H2yQPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS3mq04ms87qQBA1yiZsicGoFWJ9u7V3m7cMT-H0C8a3VnFqHmLJfIJiJiRipEmON1d47jkN722hSKOqwyHOKinMOx0jxLv0D0fxiZF6Wbd3qIn2zxkN93iOGjfaSfkTXTFUXmcw0gXUZiuIRGIlwEeDwJ6wWPcopQLl0dbpUYKjVYPL5myQ4VOmnIqZ3sG_lrHA6tj3JcF_UBCO6j8x9hcfcP6w2p9ov5noqUU3MoelClBIhYRCf9wYF6Xy_-h1lRv48Tv3HlRnhx7lazAlLHlqjGk_BuAvBDRytcVLTDPV4IvLchjkcxnQlTBHy06dEy6gFpBtcKun2jMksTjPdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
