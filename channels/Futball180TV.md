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
<img src="https://cdn5.telesco.pe/file/ltCLOSapohYYquOOO_HoIOPwWLYhGDPIJkU9KVOJ_nUgbkvypsXTMXAVTcDBm_4eIBoPQ9xvEHtuXAeAfqDsy2399ELCkVOD1KfKa1ZnpV0BEj_DlMugJ-MNHKfiVFK6OqtFb5ppDge7h0QM3KT6s7HjopPZe_-AVHszvD5sOfqwxU7VglJmnoYZOwxmyvrH_uKW5n5K-YyJVpHuQUyUlzea-x-vdh9MA9LJCzAyzDqDJvzFm319tp6qSN5CiOtDffwlwm0356ILyjmvzNGvCBKBaWSQvvaQZ0NsXVOQwUkEv24_OVmsV3Saa6NY9GssSZyNzvQAP1ajPrBKq7ac5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 404K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 04:16:56</div>
<hr>

<div class="tg-post" id="msg-107095">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/Futball180TV/107095" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107094">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/107094" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107093">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfrFY9Hk4MCifHyW2Bpa2woSRg4NsAejrl_kSizv8Wcz3pUnP0Ht9Px_uwZ8vE8S5nGZh1zRoXY0wNxAiLffaZ4p5eM5af28XJ_fChsDedOiX--_SoDvvRdY5qNFFcjcBo13tsTisFvmKST2JM7Hz_EepwV2U8whGGsT-tHwe63z3SedhAt6J9ymArbl6XHWSlXgksxTtgzOonKMaaQo1CDQiBBNdbB9F2NpnzxAimQKYuJhb9njoPw8pd0nqd9-e_3Ph8jbO3ia2HzIiR_jBvzGA8FhqHxHm3vBINKoozG0CCipmsKktrTtHczg9LA9-1sLUtWU3uG7yg3mC_I_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو اعلام کرد: قرارداد آرتتا با آرسنال به مدت ۴ فصل تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/107093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Siukmh3VqTiRt5AShb8VfjrYz6HWahS1bqso6DEyolfhNnNBJn5nrGL5NT1nC260AZ3skuOOVsF2MFU3V2l223pz_EqNS22wzNOAv4viaz5eVyZbo4ybC7UaGj0xJfABuJ-g5HeGv6OcVOSFA-qQByJgdixOOUlTTtprHAJZGShmDN-dKcIKgAASIdfmLSlq5tFuDKaYCCe-l9CxTBkDQdaKheqG30h8ohaTMC-onlEJnuzwwPjHtMXKcIdYgTaRpQk5vqJ_tWS6qEUfRrS0pvGB34z4gwejp5asWMqlWN-V1M1irNIggilQ4uifglAbWq1hNKnHoCg0p_S2Ak8CIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔥
بعد فیفا دی عجب روزایی داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/Futball180TV/107092" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rujAL8pUzTaMuNt73fA6KNH-1s8iEiEuyjbCZEB8QwQi6sZa2dHfocCRozuC4uy3BZ_l2kxSweznU8Gc7EBcHqAESATz4Q16KmU0CKSDFfSywVcx3GJtNnUG14q20gvznASWQkPFFrOKEsRkzAk1tKDEy_q5U8schaK32kbQ6vq6mr-INkMXUCFCnCPu81WX4O4BbHGB0d02qHikh4UKGtWOr6Blgaq9HpeKoCdYO0iAzvfCSRij890xLFQQSHz8PcNVUb6qYRDhwk51IPN2AT3vb2tbUK99t88UEiqc9Ia_j6nF1Eei7KazQT4xaO6WftZQd38QIe4CBqKPaRdniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیفو سکسی عربستانی‌ها برای بازی فرداشب با کویت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/107091" target="_blank">📅 00:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107090">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhVI5qpphDMjBHsxQZOoqoncY1ApjLCkfqBMPWCGaEZnX6meX0Jb3W68V1tkC2YpN8b_4fBmyNf4Ej-FHrQscyR_lnoA_6FERbjp1pR4thUCiMS0I6Noyu6Pp9pTqmsfF13jo0P5x1fqRRgwGTPAVTRBOLzPG1zGRSTYYUoYVwgq_oQ4oA54G-HF9ZX_PeYz4uI_rPsV3v0llMDJF3nQUu67KSJO8hggYNzuVMFCaahKkUiDbcqvAtThc2nM7f0cqFPmQo8YsO_2pJbCjXuZgrdsdy1TskC4B3mZ8D8Wq2pKTkmFKmkFK2SNU48NKzoTZVTJIRGBVie9RHaW_30qpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
عراقچی و ویتکاف در حاشیه نشست امروز سازمان‌ملل با هم دیدار کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107090" target="_blank">📅 23:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107089">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec872952d.mp4?token=bL-W7lkCpgHUOvYzfADqM3TR5JimlhwC-zH7m5XuovqSfGI5JBtNtc8rT8kJ24RmrAt4y3BLchRTbj40ja9ydqgzk5mFNe5pEQwQocEgpZ_ts2KzsSXlZyEr8x-4fz65KwP7CVUmYhazYQ_00rVBOJnVZEL3bavuPfPc3XuaIBEJUckX_FgBcw2m9JpVjQJYppq5D8trDzs7fsg0h1u0h5t4QA5hkvBGqFURBp7mScwGWYkAElVEHihAMe291J4wogomtIxA73ldPO8PRna9Ia1HjY27607aLFomJXBJU0Hy-Lj7fLtXS5PLLhfpgL414Bhv7aArsCt1AgaRqLdhP29YibrqYGmJev5WK4g_IkVvlLoMHjF2IJNQd79gIQBl7M5JY11cWFij_b4Tkm6prThyploWd2rOj5sT4AdzSXwKwZcNckaJtt019wWEh-_dxgMD_NzENJWcxTotk8OD1r86V1VRbXVM30YXt0IZZJqS9Cdn2uBJ814XIGvT5srrSsTzfwnpqF_Obr4FF5gWsgzjpJMeav9Z89q13OLFsbwxmMOT6A5XhZa_cyXRm2OQxADtA14aeAsZ3RnfWbI7pxGjARZ6G2mai2jsC2GsgVrInhxXHipHKJvbg24oG2mbOwVt9ttjw8XEdBxQS5f1ZtVhlCT2no2T3cCdeYfgCnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec872952d.mp4?token=bL-W7lkCpgHUOvYzfADqM3TR5JimlhwC-zH7m5XuovqSfGI5JBtNtc8rT8kJ24RmrAt4y3BLchRTbj40ja9ydqgzk5mFNe5pEQwQocEgpZ_ts2KzsSXlZyEr8x-4fz65KwP7CVUmYhazYQ_00rVBOJnVZEL3bavuPfPc3XuaIBEJUckX_FgBcw2m9JpVjQJYppq5D8trDzs7fsg0h1u0h5t4QA5hkvBGqFURBp7mScwGWYkAElVEHihAMe291J4wogomtIxA73ldPO8PRna9Ia1HjY27607aLFomJXBJU0Hy-Lj7fLtXS5PLLhfpgL414Bhv7aArsCt1AgaRqLdhP29YibrqYGmJev5WK4g_IkVvlLoMHjF2IJNQd79gIQBl7M5JY11cWFij_b4Tkm6prThyploWd2rOj5sT4AdzSXwKwZcNckaJtt019wWEh-_dxgMD_NzENJWcxTotk8OD1r86V1VRbXVM30YXt0IZZJqS9Cdn2uBJ814XIGvT5srrSsTzfwnpqF_Obr4FF5gWsgzjpJMeav9Z89q13OLFsbwxmMOT6A5XhZa_cyXRm2OQxADtA14aeAsZ3RnfWbI7pxGjARZ6G2mai2jsC2GsgVrInhxXHipHKJvbg24oG2mbOwVt9ttjw8XEdBxQS5f1ZtVhlCT2no2T3cCdeYfgCnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇫🇷
اولین تمرین خروس‌ها زیر نظر زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107089" target="_blank">📅 22:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107088">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=F8FmfRg7U6E20BO-MYrupZwOVD8QN4LFWy43FXWUB60oB-1V1R2QNsoc3VKdYt4TEU-TvopO-eJv5UWu1-aDyP7uUYsMngDx1v_fxm74gLZIbucx8Fp7gE1QVv8X2lClGi508ev0WJemfFzU-UZ2IAMLx27A8e2EMETelY3yJzAOYhc2b7ubanpk4lSHYJYWNAEACyrN7GpbagH8fYmoVUAAvDzpLB_SJxVLDmNmv85ucZNjE9zekDWe7keXVvIkVkdQcUT856cMKZrjRPoZFwAJPCCbgxYP6nwo4KowYZ9MYCu-r6Ym3zVJniRnCcHkOqaCINCP_J99QTr6gdB59TuDJKnQ_DhFHVvohmIgOcbXKLb3NTCxjR0VD7ZlaB2TP7l5yxb9fxox6FiZB1DM-kMCf2npf4pmAZuABSGcov2KNuad1iGaiUaNRdu28-s6Z1rCqS8mm7nbpmG4ERfmII7Y-dhOOJlXO4PGmVgn5lNg28Jd3pW7A1jW7vxJUTtkYh-SEUPuTfWKqEuZGRYtJvREHL97Hi9hswLh9tO5BaGa7Ad3WGGh2nnDf-L-y-5jx_xzVx1OGinjTDtWLEhSAubzaknmndJ0o49_lHfE2_dNb-GP8cn2giUZh-HAdI9sexzmrGUSIdS_tzkBOq-t56Ja_yxert2jUkjfKG8QSa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=F8FmfRg7U6E20BO-MYrupZwOVD8QN4LFWy43FXWUB60oB-1V1R2QNsoc3VKdYt4TEU-TvopO-eJv5UWu1-aDyP7uUYsMngDx1v_fxm74gLZIbucx8Fp7gE1QVv8X2lClGi508ev0WJemfFzU-UZ2IAMLx27A8e2EMETelY3yJzAOYhc2b7ubanpk4lSHYJYWNAEACyrN7GpbagH8fYmoVUAAvDzpLB_SJxVLDmNmv85ucZNjE9zekDWe7keXVvIkVkdQcUT856cMKZrjRPoZFwAJPCCbgxYP6nwo4KowYZ9MYCu-r6Ym3zVJniRnCcHkOqaCINCP_J99QTr6gdB59TuDJKnQ_DhFHVvohmIgOcbXKLb3NTCxjR0VD7ZlaB2TP7l5yxb9fxox6FiZB1DM-kMCf2npf4pmAZuABSGcov2KNuad1iGaiUaNRdu28-s6Z1rCqS8mm7nbpmG4ERfmII7Y-dhOOJlXO4PGmVgn5lNg28Jd3pW7A1jW7vxJUTtkYh-SEUPuTfWKqEuZGRYtJvREHL97Hi9hswLh9tO5BaGa7Ad3WGGh2nnDf-L-y-5jx_xzVx1OGinjTDtWLEhSAubzaknmndJ0o49_lHfE2_dNb-GP8cn2giUZh-HAdI9sexzmrGUSIdS_tzkBOq-t56Ja_yxert2jUkjfKG8QSa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
توضیحات بازگشا سخنگوی پرسپولیس درباره شکایت از آسانی به کمیته استیناف
🔻
فردا به آقای تاج و فدراسیون فوتبال نامه می‌زنیم و سه درخواست داریم. حضور وکلای پرسپولیس، ضبط جلسه و پخش آنلاین جلسه رسیدگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107088" target="_blank">📅 22:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107087">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvrJb56T6Q2UV67fYclxjWB1qHfL_jZ9A6MP5pglerxx7wjvvlIfsJoGVB6eZjtF15h5owESIFaHGjLWcAYSyNj4xX79qRWq7JTmUQQNsHZnC8974dJYm2BGqSmb9PboeOljix5QeqEq0SdLpnnxAgekY6LPidYWnKN7uJ5T9CqHDkUH8ib2DdnqYJ-nWd_utSoi1zOZxVak4H87cVef-Zzt_nix6QPrf6k9JaFPXp8JMfKeKRNF2WFAbaX66DCn4UhLmXriDkb2poyJRNsV690U6e3NB2V_Ezz0joKyrc0_vwTsYb4e92ducN9CIXZo1TyoQYxWmcHMwrhd2ZoBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
جمهوری آذربایجان رسماً پروازها به ایران را تا اطلاع ثانوی متوقف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107087" target="_blank">📅 21:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107086">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91400e175a.mp4?token=GPgHgjjEi_3QrZWZdF96eKuBDL2bdqY2dWJmLK0IKbyj88qRWSrKoEnzcLknDfggnj2PYnrMVew6Czh6XDKUCDWwIcnegh8jQpTqyH0XghxsVGEuJArz1aj3SE91nrz6vs3AcvqqpMEqrlIzWjJCQ5RmU8-ZQ2OYdtzRW0xrRut-sLKdPQlDZmgZU-tET84MD7glIlBr9AZFxpEUinFM-DH5jNKVoRRRwVyqZGAcqjlTFyoVBEfwyV5Ho4HpM0zbunpUaqNQ6jY5BLIjEWihcTKKjwOmQIR272nON6wY1YvBKogTC_ghHS2HrZh5mmvGhXnoVZIiVbyyp09De9uwVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91400e175a.mp4?token=GPgHgjjEi_3QrZWZdF96eKuBDL2bdqY2dWJmLK0IKbyj88qRWSrKoEnzcLknDfggnj2PYnrMVew6Czh6XDKUCDWwIcnegh8jQpTqyH0XghxsVGEuJArz1aj3SE91nrz6vs3AcvqqpMEqrlIzWjJCQ5RmU8-ZQ2OYdtzRW0xrRut-sLKdPQlDZmgZU-tET84MD7glIlBr9AZFxpEUinFM-DH5jNKVoRRRwVyqZGAcqjlTFyoVBEfwyV5Ho4HpM0zbunpUaqNQ6jY5BLIjEWihcTKKjwOmQIR272nON6wY1YvBKogTC_ghHS2HrZh5mmvGhXnoVZIiVbyyp09De9uwVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد چلغوز گودرزی رو داشته باشید که دوباره تصمیم گرفته بره مقبره کوروش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107086" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107085">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
تمرین تیم‌ملی فرانسه
✔️
کلاس آموزشی تیپ زدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107085" target="_blank">📅 21:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107084">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🙂
💥
مسکات حلال‌خور اتلتیکو مینیرو برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107084" target="_blank">📅 20:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107083">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=CCnwhkUubhuErj1LyQqqfSZfNzghWDsYj4_aUv4QzwqNYdg6UCYqH7pUR5UZKnZzfRkhyunXOuaz3khAgf68VM2bHLi4HMbE-tTreALdARNKURLONFMqR6QmRCUUebxwySIApPrvIABEwzuHp_pW_bpytSUec420NqF18YtXI89mrNsVz6rT0ZKn97T3OR2SRxo8qmI1DfvkbdOshE_qH6VD3HogVo9j3ugvVzxs7I66ygumCd8hMYYwSMCt1ygXeK77Wd6e08e5jmpPLqzI3IfZ8K1JZRC8g2teqCJZ5YCHKnewcso5SptxqrtUT7N1jNHu8_2ZWRSbNmmyzkhbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=CCnwhkUubhuErj1LyQqqfSZfNzghWDsYj4_aUv4QzwqNYdg6UCYqH7pUR5UZKnZzfRkhyunXOuaz3khAgf68VM2bHLi4HMbE-tTreALdARNKURLONFMqR6QmRCUUebxwySIApPrvIABEwzuHp_pW_bpytSUec420NqF18YtXI89mrNsVz6rT0ZKn97T3OR2SRxo8qmI1DfvkbdOshE_qH6VD3HogVo9j3ugvVzxs7I66ygumCd8hMYYwSMCt1ygXeK77Wd6e08e5jmpPLqzI3IfZ8K1JZRC8g2teqCJZ5YCHKnewcso5SptxqrtUT7N1jNHu8_2ZWRSbNmmyzkhbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
🇮🇷
پیش بینی چند هوش مصنوعی مختلف از قهرمان فصل گذشته لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107083" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107082">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=fDbswZjmKyf0a6c4ngKyYoQFm-38xtRH_8fMAyElQxdKk3isO_BJkcsYSibQhIo5rXM1M4QqNgjf-fd3j2wT6u3h9eS8RpZ4Po_J2PQZfFnq7zQ0Bk2GivnO2-8ENvX-avW25oWdrJW6yME9Abhzx17X4ctbp4IiVhGg37FvrEOXGBhjSkkDqLoZBOTys4sibPpho3K94ngeRDAWL06vfOA7fAGo0E4zN3W-b6u5K500jCnm9dfDQ8YjcHIWlnrKZakVIIBrPIpDUviAs1Bjr8b6gB4iRemt4tfqpwXoVkt7gi0xuTUfYZbCHB4ruhz3uGWzKZisFGFfki7GxycT5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=fDbswZjmKyf0a6c4ngKyYoQFm-38xtRH_8fMAyElQxdKk3isO_BJkcsYSibQhIo5rXM1M4QqNgjf-fd3j2wT6u3h9eS8RpZ4Po_J2PQZfFnq7zQ0Bk2GivnO2-8ENvX-avW25oWdrJW6yME9Abhzx17X4ctbp4IiVhGg37FvrEOXGBhjSkkDqLoZBOTys4sibPpho3K94ngeRDAWL06vfOA7fAGo0E4zN3W-b6u5K500jCnm9dfDQ8YjcHIWlnrKZakVIIBrPIpDUviAs1Bjr8b6gB4iRemt4tfqpwXoVkt7gi0xuTUfYZbCHB4ruhz3uGWzKZisFGFfki7GxycT5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107082" target="_blank">📅 18:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=INNuUvfiafSKiWbIw0vngbqI_K5XbQDC-Sq6PuWbKODhUipACbdkXor0K-EBsmOpXYZDlRozfUQzp9mt6GDtDX9weMegBwK205SGEHIJSOEulATvPqQWuP-Kb20rDMVjZqtFoveq550WHc9kUE0GFUp_ET86Ngzhyj7l14z5gp86fYyEh1RCbQcOjFWxDHdlFkHdmVmEJ7P4gpmeCvyGgOTu11fXMferCasJUVnKfWQc_ff1yQi68zpdrlIazlPnWtv0UNOuj5R7fcJnyS98I1jmj8HCJI1UDvgCdEX9AL6546g_nAcbIHidVJ1VKW-Mm255q7TNx3SZrOt6hEkf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=INNuUvfiafSKiWbIw0vngbqI_K5XbQDC-Sq6PuWbKODhUipACbdkXor0K-EBsmOpXYZDlRozfUQzp9mt6GDtDX9weMegBwK205SGEHIJSOEulATvPqQWuP-Kb20rDMVjZqtFoveq550WHc9kUE0GFUp_ET86Ngzhyj7l14z5gp86fYyEh1RCbQcOjFWxDHdlFkHdmVmEJ7P4gpmeCvyGgOTu11fXMferCasJUVnKfWQc_ff1yQi68zpdrlIazlPnWtv0UNOuj5R7fcJnyS98I1jmj8HCJI1UDvgCdEX9AL6546g_nAcbIHidVJ1VKW-Mm255q7TNx3SZrOt6hEkf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ: انتخابات هیچ تأثیری بر تصمیم من درباره ایران ندارد و تنها تمرکز من بر عدم دستیابی این کشور به سلاح هسته‌ای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107081" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107080">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
⭕️
⭕️
ترامپ: باید تصمیم بزرگی بگیرم درباره اینکه آیا می‌خواهم ایران را نابود کنم یا اجازه دهم به حیات و شکوفایی خود ادامه دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107080" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107079">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=DmCkZtTyAdTRuQT--ms66eXgWooxIRg4MivA4olEXN_MFywlrofUbFkgxolW8LXdn2TG5tJquLslCR3e7SXzkeFfFQoq2eARJ-or61bL5RNVmNJQ-HYg7_mOBWLQbBaS2JtTPsV5VdTJb5wnYpbNKXTMtl15itjjLyU5EpOwybFkBb8DDc1woLPKYbtgvtL_tidlkhTC9CgsfuxpPnxjYliaNEyxmzFgjCdlUzWVTXvOrOfZPRuB68EWuAEeAWUQJmIdL640a1x7F6lP3ZXtkfQUSVk6O3BneAEEFdBZfJcRUS5qPh9NrIo6fjCfijIhmoK6KQK14SGWypsVpZlrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=DmCkZtTyAdTRuQT--ms66eXgWooxIRg4MivA4olEXN_MFywlrofUbFkgxolW8LXdn2TG5tJquLslCR3e7SXzkeFfFQoq2eARJ-or61bL5RNVmNJQ-HYg7_mOBWLQbBaS2JtTPsV5VdTJb5wnYpbNKXTMtl15itjjLyU5EpOwybFkBb8DDc1woLPKYbtgvtL_tidlkhTC9CgsfuxpPnxjYliaNEyxmzFgjCdlUzWVTXvOrOfZPRuB68EWuAEeAWUQJmIdL640a1x7F6lP3ZXtkfQUSVk6O3BneAEEFdBZfJcRUS5qPh9NrIo6fjCfijIhmoK6KQK14SGWypsVpZlrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: ایران موشکی با قابلیت هدف قرار دادن اروپا ساخته بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107079" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107078">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=SCXsAgoaDI2e3qdcUkT4zANZxMPlkwCFtzS_QLqnAeqmLyZpX38e8SQVMYAsoch6fsQwZk5AIF3roUvl5nEEw2Osn9kLMqq48B42F9THLjGeHqKvuEM5HsFZNmBC62WFsZCYrgULyvFgpK-I98YNxiH6sGN43RlmdWMuy9UVK0FsMA8Hu-Cd9rxZvWq04lKSORp4ZowSD3LJpCgDTdhm4-E4bXNAYDMKcgM9ZctBxo0uu3tH1QzKbE_PXM4sFKDRZU_QdgwhC6rbHCDQ2_Y7KTwxz_FKH7vr9XgLHjb1pE4ny3-Y8rzFKKsVKf3nlASyFDkO-p6fqchVBJndpOiwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=SCXsAgoaDI2e3qdcUkT4zANZxMPlkwCFtzS_QLqnAeqmLyZpX38e8SQVMYAsoch6fsQwZk5AIF3roUvl5nEEw2Osn9kLMqq48B42F9THLjGeHqKvuEM5HsFZNmBC62WFsZCYrgULyvFgpK-I98YNxiH6sGN43RlmdWMuy9UVK0FsMA8Hu-Cd9rxZvWq04lKSORp4ZowSD3LJpCgDTdhm4-E4bXNAYDMKcgM9ZctBxo0uu3tH1QzKbE_PXM4sFKDRZU_QdgwhC6rbHCDQ2_Y7KTwxz_FKH7vr9XgLHjb1pE4ny3-Y8rzFKKsVKf3nlASyFDkO-p6fqchVBJndpOiwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ در سازمان ملل: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107078" target="_blank">📅 18:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107077">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=BK0fSH-g1Jt-Pw40hy3XKsYiguYgTzbdPBdL_jyn3SN_tHUentSTkju_lsJdpf26bITqzY3E5UMyrvjDU-AWrUuRjZzObJxjEMQIqeU3hJadwTxikFY4oIiF9l0XP64c34mI8Ih6JMI0SXZlrJdKj5WES7n6VXrE_QFlD7UoyJfaXL1BAsDPLxil8QFqkeRIdv1aPGDCXFC2m1VKBJOngrE1KiWaHnygU6IJLqNACKWtdxl8nJOMEKWIBKuBKLw7KkAVOmOaa6ZqHbBwB-hdA71YWXcPacx1f_g3fqr3iv4VGd719eWM1EbhpWd0zyHPcfgYiq9zKQFDJ8aguh_vqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=BK0fSH-g1Jt-Pw40hy3XKsYiguYgTzbdPBdL_jyn3SN_tHUentSTkju_lsJdpf26bITqzY3E5UMyrvjDU-AWrUuRjZzObJxjEMQIqeU3hJadwTxikFY4oIiF9l0XP64c34mI8Ih6JMI0SXZlrJdKj5WES7n6VXrE_QFlD7UoyJfaXL1BAsDPLxil8QFqkeRIdv1aPGDCXFC2m1VKBJOngrE1KiWaHnygU6IJLqNACKWtdxl8nJOMEKWIBKuBKLw7KkAVOmOaa6ZqHbBwB-hdA71YWXcPacx1f_g3fqr3iv4VGd719eWM1EbhpWd0zyHPcfgYiq9zKQFDJ8aguh_vqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
تعریف عجیب علیرضا علیزاده از نوید عاشوری که موجب پاره شدن دوباره عادل شد: گفتم ازدواج نکرده بودی، با هم زندگی می‌کردیم!
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107077" target="_blank">📅 18:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107076">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=FsPVF0DODLQhfUuUk3SWSyLyYnips3_X-Hr1QKk3vD3XmOe9K8BBHp2YPG9XpVheGRODUquH3mGjabYHfzL-zl_9ZsbMxbyMkXLOmtNCfZNV6kSrvhdfzs7dQv_c4P1JNE30coHLzJ6khhlQJlH7PWFOYDGqhMt9_wxuNmdDw1Ccetc4nCxM76jq_Ejtz-gxDbtjHLyHBW0SzG24mKpr96V3G4WbV-nO1XCCT0iDYHaahKbxx5JJ4uShS72q79gDpLJBOlIlIBQyFLNKIS--oUVXnSji6RwY0b7dF9O_uZqTNGTsrfy2Z3PQTiHaioRIO41Oq-htuVpPXSoNsagT-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=FsPVF0DODLQhfUuUk3SWSyLyYnips3_X-Hr1QKk3vD3XmOe9K8BBHp2YPG9XpVheGRODUquH3mGjabYHfzL-zl_9ZsbMxbyMkXLOmtNCfZNV6kSrvhdfzs7dQv_c4P1JNE30coHLzJ6khhlQJlH7PWFOYDGqhMt9_wxuNmdDw1Ccetc4nCxM76jq_Ejtz-gxDbtjHLyHBW0SzG24mKpr96V3G4WbV-nO1XCCT0iDYHaahKbxx5JJ4uShS72q79gDpLJBOlIlIBQyFLNKIS--oUVXnSji6RwY0b7dF9O_uZqTNGTsrfy2Z3PQTiHaioRIO41Oq-htuVpPXSoNsagT-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعضی‌وقتا آدم فکر میکنه لیونل‌مسی تو زمین فوتبال بیشتر از دوتا چشم داره
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107076" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107075">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107075" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107075" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107074">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbXdsNWAYzs41p9iduL7ZmBlkLm4UGFx2s8VK0AYO0gqNJ-n67jfEXn34NeU6aumiqwRBb5D_-TOtBQcQ2MzixV7D0lfGZOkHxQiOff1mOkadmFGl_mgn_2k5k2m82eL834Fs6ZmMUbriqbNhItSG3ymxWswey-XPRszcaSHzD9qygsjSBgMNnHYUA-ngajxm9aJ8bdrJMR8FYiKS9s1eBICCH904FX9Vo3lo1iatqD54iavgKUFtucTgNYsGMnnwFhhDC30SvOW2fd-OBVTTJsfQAh8AWB9rp9vHHrEMpBueeBr4eQNnbZPnDz9xo8vZeeAj3PFES5hdz0vbl2Uqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107074" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107073">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvQTvCy-UGXTdYtVYWQCeh6EnyZOr7KUtYTZ2ntth0nSXh9Ktwi5ajMMiqMndLAS_bqzgt7wR4X_eDcS6uBUk8s_uAgnqzZcjGJhB4P1yDPtpiUzStMJEEqbCfpt6Y2cjdD0vKW-1A0GyyeRjfPk1QXfdcknf8AlKTGrQM2K2tNZdmZoW-rRIJcBJOwk3FL3qsTyuyfNP6ujV5KbGd3wr4KeHYW_i4veVbJOVromlBD-TdOKViGFms5lUPDGYAZal8IgXfaZU_KWpGnxypaon7T1viVa8tE3OaboDQZGVN7-Sei9PLTx-pM1k92aHNRtkUXTl9B7pnAFfRPhHUPCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
لامین یامال :
🔻
به نظرم همون‌طور که می‌گن، توپ طلا جایزه بهترین بازیکن ساله؛ برای بازیکنی که متفاوته، از تماشای بازی کردنش لذت می‌بری و حتی فقط برای دیدن اون بازیکن حاضر می‌شی بری استادیوم. فکر می‌کنم توپ طلا برای همون بازیکن متفاوته؛ ربطی به تعداد گل‌هایی که می‌زنه یا چیزای دیگه نداره.
🔻
وقتی به توپ طلا فکر می‌کنم، یاد مسی، رونالدینیو و بازیکنایی از این دست می‌افتم. اونا متفاوتن و وقتی بازیشون رو می‌بینی، باعث می‌شن لبخند بزنی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107073" target="_blank">📅 17:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107072">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjjS0dshSJIOo3ewQoIK3lTSm0k9dvoKWFPbuIkj5m5HOjqywqTlOu0ZxnaxlFz6nS2g9TICRJmVucgJ6Fh6WDClm5Rx49HPD_T-IDH_fnaIbWvB4dG0_e4u84Mn4o9TAh514NwONk30N_Mo3cuypOJYEAePeIemkO_iTT6hiBJhMCBlcpUJnOQPEDpoXD__sUZ4Gt9laZ4oETcaS8WI6gKrFUJ4zh0_TmpOkRRFlNNnSXPmWgJ3wQvIWcD8bxhTyH3eUb1phV_igbD0VsY4B08gvXl0THt8nvCsG1N2CZRXbk9ln2y1a5KgCG_gJunqOohAyScIBYWJDFETMSsPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد جدید آرسنال با آرتتا بزودی امضا میشه و این سرمربی به مدت طولانی قراردادش رو تمدید میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107072" target="_blank">📅 17:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107071">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=GZ58PbUlv6UOPBqhEPuUd9msx_MLIdG7vRnD057r_1Tr0gdsfwsd0v02bmJ-Ou-Bf1xdgXR9Do88LW6OahqU05d9Q83PnlOpd1yuy64u3WQc9L5IiifVTmGXDFlWbsIkuoTKz_YU8RODoICGrv_luYRUcCpFIWRv6WI24F0oJ--RHnBZzixIlS2mHsK7HP0bIs7YWb79LbtRu_PJmd7_bdAbXIILklsRtwKcS8spr93Zbg-d41kKVpE3xKjF992Dg9tO0VYsZ5O9HyP6-K4oVzIugwDptYoTrLGqSgVIhsmDyBgX6XBIaDlwDlQSoZTt77HlVFSlX7zIPlOMQyFPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=GZ58PbUlv6UOPBqhEPuUd9msx_MLIdG7vRnD057r_1Tr0gdsfwsd0v02bmJ-Ou-Bf1xdgXR9Do88LW6OahqU05d9Q83PnlOpd1yuy64u3WQc9L5IiifVTmGXDFlWbsIkuoTKz_YU8RODoICGrv_luYRUcCpFIWRv6WI24F0oJ--RHnBZzixIlS2mHsK7HP0bIs7YWb79LbtRu_PJmd7_bdAbXIILklsRtwKcS8spr93Zbg-d41kKVpE3xKjF992Dg9tO0VYsZ5O9HyP6-K4oVzIugwDptYoTrLGqSgVIhsmDyBgX6XBIaDlwDlQSoZTt77HlVFSlX7zIPlOMQyFPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارلتو، نشون بده یه مادریدیستای واقعی هستی.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107071" target="_blank">📅 16:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107070">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9DIUVW5ZAcJe4nctCdvkT2ikBH20rz0WkkTbmi37YDi_ESPpl5kbAP1DuHsJlDYm6Jy7bsI2h5hJazrjdx01SO0xMhdAmGq6YzPNDz7XRFng-WY0UBXPQpkhmoSI571vIhCJ4IUTtcCh5SBGfXEwYdEdaoBt3Vu_wjMeqfhO2wU2bPqqstcOmzYY4t7cyWfMmd5Z397-YNZKeWKAUQ7a8ZejiObUCAUm1gNYiLkO6yrcLTK8W3CH5nQ8SwnjnNyM76-io90k-W1g-YSXQw_wdqSgt6WTHzTiP_lCjHob--qjnd4eAH2H3UK40l-cl0KSbW3VT6dFPWo9lCmKIfI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
سهراب بختیاری‌زاده برای نیم‌فصل خواهان جذب یک‌مهاجم خارجی، یک وینگر چپ خارجی و تلاش برای جذب محمد جواد حسین‌نژاد شده است. از سویی بازگشت خلیفه و گودرزی نیز جزو برنامه‌های بختیاری‌زاده در اعلام به تاجرنیا بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107070" target="_blank">📅 16:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107068">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsRslc9RyYkUCsyVjAGgRXDeTIYNqIcrEUA_O4s_geJLX2DFga3oucjt70xJgDbbkqNukWzr7xW42eZVXj_TW0F8AjD3QJQI81-IQ8yfSVFVSnvvpFuS-HiRbFh9L0tZO1eUNXlTcQGLr7gkNk-d9kHMGLbaNtzO8ZfihDZHA4H1trFFsHn_6rdGq79inC5rYKOouxvF6tEFH14dWHV2S9skiNOBm2LcV9tSSMjXyzh1x9TIJGBCU8VwGQX1hjZCrz5pTrhEcyUwEH1_pl_Cf0vVbv1rk2m75RWvj5RT6v9KGCTIB3Y72XOoO33JeAwxwmQFdABJrc-DOvMSa3J4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
اوج تلاش خداداد عزیزی برای درخواست بخشش از مردم بابت وویس زشتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107068" target="_blank">📅 16:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107067">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGA50mKYhyLCrUrmveJO80v0JF94NS4pN8R5gzCDlIQe2FT5lPlwDr3HgVMcSrGQE46jIySSR02N2wfatXo9ae8WfaO1h1Ex2D7jrBNTm-mRz5dzaiO5iRO-CVjV6AkTEl6V-CVEhYlRb7xX1w_-7W62nIVtLofhSmPautmZZaw-ytYjT2rOxtyXT7rreqj1jivKL1zBKm0cQ0ewo1WAL0uPJjavgCUQayoEFM1Aqisq9HV9BLnCqViuHN4JPyPxMYG2rgBLePHqwvNGFde0reifu8oXgOTre_motEy2P3oNXpQkVdzKO7oI352007lNR6qDGzEr6Oq52QUiJ_z4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عملکرد فوق‌العاده موناکو زیر دست فلیپه‌لوئیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107067" target="_blank">📅 16:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107066">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejWLkTb-fSAaBlH-QCuB9CVrIdKlJSZSlYLl7xF7qAiz51YfXL4iCnyDSThT4VWz0ujofc0hRbPo-Pj3ATJsXC4lFa1sPAsyl_QL0mpf3JPaWVm3yxREH33bryE5O6i6uelWGPyxhFw-YGfUePFsnU9-fLHN-4-Rx8_Ue1SyqoBsoMGCi9bxSWh6dwrJXkWd-Bq8_pVlFgKpnfA6IadVrGs7rhYv067vCgKERzHyKgjiZg1H_17Ng_2sPkbXMG8w3-ZgKprfbpG3WhIINZZRhXW72QnH_c8K_bo_JbCuorv_G1DoVCNf4emuuufF21sMXPwMaO1PKeYwjQ6Qkk5zKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار
تیم با ۱۰۰ درصد برد اروپا تا پیش‌از فیفادی جاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107066" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107065">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_xtuGzSphCfLRbP4QuyWRhjObdm43cMVPcG7zk2pDbARgDySrf-I7m6D1vGHkKTw7KkrHgshCbB04pzPkFfMPD9m5_J-3BuWMELNsDLZj_QAyHOxNSqfmPfUr_ew_9vwqgKOGUEjabIMekRfoMZihnXsKbzOX9PmSaoKt5S5rQO9hz9ylzseYvk74n0-6PLv62RSIB7kAMGFh79cYTZ17gYhL6KsgjqWdLD8AC0otyLxHZwR9UNazMH49q5r9APl2_89rDwjx-N2ny335HO9zJEiz3PTd0m_SZkl13SBuhZX_GgZJGsQeOHKhb9DABDgKYQI_2BmZ8w6PizuWNWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
عربستان و چند کشور خاورمیانه در آستانه جام ملتهای آسیا با فشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107065" target="_blank">📅 15:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107064">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=itsRfMWXP9X8O8HnDzXobvtWUdlKSTgS6LErx1XigfU0TBH6-uyo_90kTnSJDw8GPfJL_nB3p4yUJqkILgUBUwd4Ge_iZqs8CAFtK0BPVkEx4c09F9qO9CiptgIaavNDMZHBTXbDPydsWGwZHRD5ZGrKQPraBuX44BEu5k2Nl4a-1Rk3oEQ9FxkxHhqbOIzviwbxxFXWEMnMXz7M84NGdBxacrDlUZRqxFZgEXxMSY9RDTs-6sL1D9_l6xs9FNSDwKnCFHM_-thk5Akr4VmU2h-7XElaFarFzcHmiNX3Kn3yjVP0P1SqRpeb8KpG8hjY15AsJw4MZfPbJiky0343Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=itsRfMWXP9X8O8HnDzXobvtWUdlKSTgS6LErx1XigfU0TBH6-uyo_90kTnSJDw8GPfJL_nB3p4yUJqkILgUBUwd4Ge_iZqs8CAFtK0BPVkEx4c09F9qO9CiptgIaavNDMZHBTXbDPydsWGwZHRD5ZGrKQPraBuX44BEu5k2Nl4a-1Rk3oEQ9FxkxHhqbOIzviwbxxFXWEMnMXz7M84NGdBxacrDlUZRqxFZgEXxMSY9RDTs-6sL1D9_l6xs9FNSDwKnCFHM_-thk5Akr4VmU2h-7XElaFarFzcHmiNX3Kn3yjVP0P1SqRpeb8KpG8hjY15AsJw4MZfPbJiky0343Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
مرور هفته‌عجیب فوتبال در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107064" target="_blank">📅 14:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107063">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=TTph6eWjpYjAT43dPx04vTfHA0hIYEi4w0eUU3qKsRjxdiDGyBFI6djDYUUleEFtsozt3cXdZChhS1YgGZqoxNpoeiuD-bUoC2_ud1oOIjeAi9VKGfYIQ1dZe9qzD124X40mybIl0wT1_PaaxKRLwyleQ0WcXNma9_4UjOtstYHAbXRicPWTfIR5RNn4FJ-82-pV1cabX2hNJTEhGbFP4oRBGl2KcNcFKrIW-oeTsTwaT-gTMux-pCfpCZPaAN_XNq9nDUWZiVkJ-VyJT55WGtLFNi37nTrZ2pVgsT41nYla3dbYYPHbAQD-T3FpsFdJFSt9_8BSDzGXRY7ELVVbTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=TTph6eWjpYjAT43dPx04vTfHA0hIYEi4w0eUU3qKsRjxdiDGyBFI6djDYUUleEFtsozt3cXdZChhS1YgGZqoxNpoeiuD-bUoC2_ud1oOIjeAi9VKGfYIQ1dZe9qzD124X40mybIl0wT1_PaaxKRLwyleQ0WcXNma9_4UjOtstYHAbXRicPWTfIR5RNn4FJ-82-pV1cabX2hNJTEhGbFP4oRBGl2KcNcFKrIW-oeTsTwaT-gTMux-pCfpCZPaAN_XNq9nDUWZiVkJ-VyJT55WGtLFNi37nTrZ2pVgsT41nYla3dbYYPHbAQD-T3FpsFdJFSt9_8BSDzGXRY7ELVVbTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
🇪🇸
پست‌سمی تیم رئال‌بتیس از جدول لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107063" target="_blank">📅 14:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107062">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068efa824d.mp4?token=GwPuKiL2pwf0EcasZo-5GxNGfJTLwZv-ehXnCrx28czI8AFpq4och-NXbMcTRQ2KW0fc3BM7Lp37h4u5P7rc6CKT9J7jhvsbXbx8lwtqlbVvwXXuEFlZ4LLGRAfR4SRxjjVPa2K_MHhs9cQy81nHE3xxbgJqG_7CfYOEu4sPekD-N7F9wpDqFYwfTPluvHL5CbW-5JxJEblYHwKWca0fB_D4C1NDWurXX1YqrDM6AeWovHklcZV1icPh5KPKMRd0QekSzw9a3jJAVXP5RAZW1LbQ1VWbnL7kwrAxIY-eZf72hnr82nh7GGXW3mgw1kHk88Bggwb-gfn5qwVGF-Yn1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068efa824d.mp4?token=GwPuKiL2pwf0EcasZo-5GxNGfJTLwZv-ehXnCrx28czI8AFpq4och-NXbMcTRQ2KW0fc3BM7Lp37h4u5P7rc6CKT9J7jhvsbXbx8lwtqlbVvwXXuEFlZ4LLGRAfR4SRxjjVPa2K_MHhs9cQy81nHE3xxbgJqG_7CfYOEu4sPekD-N7F9wpDqFYwfTPluvHL5CbW-5JxJEblYHwKWca0fB_D4C1NDWurXX1YqrDM6AeWovHklcZV1icPh5KPKMRd0QekSzw9a3jJAVXP5RAZW1LbQ1VWbnL7kwrAxIY-eZf72hnr82nh7GGXW3mgw1kHk88Bggwb-gfn5qwVGF-Yn1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇮🇷
🇮🇷
شوخی ابوطالب‌حسینی با عدم قهرمانی پرسپولیس در آسیا و ناکامی‌های استقلال در دربی به سبک هوادار مشهور منچستریونایتد
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107062" target="_blank">📅 14:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107061">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=pQUJGSWD5tAVWNqLeE7GVWQFNlHMUyXuZBT635_gs7OR16EVhi-AmdTzYkweVGY3s23Gr6Ld3hHjPw215BuJW9Vh2eZ9Czfkdsixi-FW_eyP0CII6iP3FkxCJNaDcxm6eokWsbg_mmzGttLvna-jwdoUdB44j3OZzb7JiL5gfCSUEUwPVAbTeE_ws3CF3yBzq79cXPeJQj0E0TUmIANZcBEbj6l12O3n2NNpL72KGxIec7sl7MgKPCqonF4owbBrp6AhTJOyozXEFGjPo9vpU4QupQIZLFi6nVJQOCWzWmh3OrHeFwYgDQGDbMy_lGZo8UEr4tasbWouDSP1PE778w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=pQUJGSWD5tAVWNqLeE7GVWQFNlHMUyXuZBT635_gs7OR16EVhi-AmdTzYkweVGY3s23Gr6Ld3hHjPw215BuJW9Vh2eZ9Czfkdsixi-FW_eyP0CII6iP3FkxCJNaDcxm6eokWsbg_mmzGttLvna-jwdoUdB44j3OZzb7JiL5gfCSUEUwPVAbTeE_ws3CF3yBzq79cXPeJQj0E0TUmIANZcBEbj6l12O3n2NNpL72KGxIec7sl7MgKPCqonF4owbBrp6AhTJOyozXEFGjPo9vpU4QupQIZLFi6nVJQOCWzWmh3OrHeFwYgDQGDbMy_lGZo8UEr4tasbWouDSP1PE778w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
🇸🇳
سادیو مانه با حضور در زادگاهش در کشور سنگال، مبلغ ۲۰ میلیون دلار را برای احداث یک پروژه با اشتغال‌زایی بیش از هزار نفر، سرمایه‌گذاری خواهد کرد. مانه اعلام کرده که بیشتر دستمزدش در دوران فوتبال را صرف رشد منطقه محروم خودش در سنگال خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107061" target="_blank">📅 13:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107060">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=UX2KmSlTDMZkL-UzPNawb4GZIFORUvwOXnqDpcAGPGFipurYHUnC_53jaUtaburPkg9vjBC-4Seo1ah0fK_gD4kLhDN1zFHh2RQQHeuMWofNSXyj02VAKiV3saP5LcHqFjl0wpxud5txNaUQhZLxUBTp0-4cDirycAPVMJZXtL3qcW_goMip4R1YKhmj59mq6Dp-1oeJn2kSUloEs71gW5EJMZsrXb93JFFJix7RyGa9OQhYwk65m211sKE48tw8u8Cv-f9cwOFtTTw02TmgZjxvHLzfWjk07v99wInENmpwUOrpK33Ikhhy084gOSHr95nwjEzCbfe6eu2hKVEN2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=UX2KmSlTDMZkL-UzPNawb4GZIFORUvwOXnqDpcAGPGFipurYHUnC_53jaUtaburPkg9vjBC-4Seo1ah0fK_gD4kLhDN1zFHh2RQQHeuMWofNSXyj02VAKiV3saP5LcHqFjl0wpxud5txNaUQhZLxUBTp0-4cDirycAPVMJZXtL3qcW_goMip4R1YKhmj59mq6Dp-1oeJn2kSUloEs71gW5EJMZsrXb93JFFJix7RyGa9OQhYwk65m211sKE48tw8u8Cv-f9cwOFtTTw02TmgZjxvHLzfWjk07v99wInENmpwUOrpK33Ikhhy084gOSHr95nwjEzCbfe6eu2hKVEN2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
علت جدایی ابوطالب از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107060" target="_blank">📅 13:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107059">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=s0QGHYJcWSWaRk4KJg8BQ8DjdjFA-RLGvaHAzGpj8LCdVRpO_ZZs6c8O9ClK7E27KV0opBv6fTys1cvWl9YEd_z0GiWxu_4ZVn5yNibebqdDuJxvLB-MgsrVBF5LVj2QNnMU0TawSZAK64SeIjCixqHDE_0zd1axiSvS9hTId_q55uZ0BaRDJ6vPpsNOadW4n0pyTgaotHWZgWCgq5XJE5goxjZha4XKGS4jn7004tCTIwA7CgXYJFhOigHZKvknybERaDhwsBfCjNtPXBW4FM2aHF8WCcFM7wIAkJX4d7jm03nda2V4ssRDzsrcaENkjrJZaBZtLl-SAQTyxzs_6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=s0QGHYJcWSWaRk4KJg8BQ8DjdjFA-RLGvaHAzGpj8LCdVRpO_ZZs6c8O9ClK7E27KV0opBv6fTys1cvWl9YEd_z0GiWxu_4ZVn5yNibebqdDuJxvLB-MgsrVBF5LVj2QNnMU0TawSZAK64SeIjCixqHDE_0zd1axiSvS9hTId_q55uZ0BaRDJ6vPpsNOadW4n0pyTgaotHWZgWCgq5XJE5goxjZha4XKGS4jn7004tCTIwA7CgXYJFhOigHZKvknybERaDhwsBfCjNtPXBW4FM2aHF8WCcFM7wIAkJX4d7jm03nda2V4ssRDzsrcaENkjrJZaBZtLl-SAQTyxzs_6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
‼️
دیس سنگین ابوطالب به خداداد عزیزی: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107059" target="_blank">📅 13:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107058">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=T4pWRefd2-auLeYzncGuQuGkTJoBLXoE5QdQv2KAhw_Nob8_wGKvMqn1SfETLMRTjcnUMrmJQgak5w0NVLl--0pFhQWfHqO-52ZAS7Hntb0LPipNjk0g5_PU7qqFb70jMqPblK1BDOADjL3VlgLLc0kWu1iwj652L1MBRVHUqjG1yr66x_1RnaZnQeBPvyXZ8NDWy5wd-wr20vsVyJGhrz2l9baK4X6OMYyWQw2YL0X6IQLwIov6U77HUIXAIJZZPSPoyY9bdClK_alFZKFYcck78BoUx8-o15CVHu0cjQzA_v1473kRmolXvzyzg-2YQV6ZHD7AUKey5dvqvPmgHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=T4pWRefd2-auLeYzncGuQuGkTJoBLXoE5QdQv2KAhw_Nob8_wGKvMqn1SfETLMRTjcnUMrmJQgak5w0NVLl--0pFhQWfHqO-52ZAS7Hntb0LPipNjk0g5_PU7qqFb70jMqPblK1BDOADjL3VlgLLc0kWu1iwj652L1MBRVHUqjG1yr66x_1RnaZnQeBPvyXZ8NDWy5wd-wr20vsVyJGhrz2l9baK4X6OMYyWQw2YL0X6IQLwIov6U77HUIXAIJZZPSPoyY9bdClK_alFZKFYcck78BoUx8-o15CVHu0cjQzA_v1473kRmolXvzyzg-2YQV6ZHD7AUKey5dvqvPmgHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
‼️
ابوطالب حسینی ویس لو رفته خداداد عزیزی رو مودبانه ترجمه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107058" target="_blank">📅 12:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107057">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nxu1REMRxhqvMrVb4RafdpYlqSIjNtBkfU2o4cTAZALYlmZSnCuoG_dT6Mu7Eeo2jmWbF1JpZQgE0yCy-I5ebfYPA_3ty2myRc3fci4xkURdgdozyshiDMM7ROh5G82_MmuIzCMslfXfWP2G_y-gM6hoJEzozFgkmXk6mupXtrGF-RJyJ49EEH7MUT6YDkwN6htQVV2bMt0_L3gNpqAVy29jQjzR4ssduo4joPKEaRO6pKMzbKE52T3xSwqGQt64FBtw23Ije4bMDz5Y1so5zxMNMJ_2IGkoP5nRSM6-Lb69EW8Gvdk3JLoxQva-DXPKllx-5ECub_saIV9bOJ4Jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107057" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107056">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Se-SuPYTTCVElS_1Re-ngyhptFqgaMkqUtBbkkjO28pxnA7TMXtjFyMvuxZfAczfMd5TrEs_i3KgL-Fft5lnir1Pil6YllufS5ziTAkQswyoyaf0zpepVQ1HxMxoBiCbADQnI_lPJ-b_6wZlxGt_AjVT-6gUpXJE6PmxyvGeXvSMi4GJGoQtgjJhQyflXCWaiUG9CF2VhtpJu6NxVtPNgb0dXmw93_FLKWmHTRQYKftuPgklDhWtTZzfDo-LPSK7dchW7dzcPdlju8VPeIeTOLx0vS0IIdjyXA1jmAF4Dw_wE5xlhrxv3I-0dfV2TJBMUZRrcUB-SXDqHk21yudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمع سن سه نفر جلو: 110 سال
احتمال فیکس شدن هر سه بازیکن تو جام ملتهای آسیا هم زیاده. جوان‌گرایی بی‌نظیر امیر قلعه نویی بعد از سال چهارم مربیگریش در تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107056" target="_blank">📅 12:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107055">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=h5QHsx2ApRpJMVR4BV5dM39c4Oju8AolqNLq7zqOPkBESCDWCheJ2BzVT_PKxR91H9qHy1033IZ7tEs7-n59j1OcL11RThkhHSJUBuldJ6er-6bkQd9ANDAfzL3dT0cs8Qwwxb5y1iX14XMuNQWn7MJxRwFM0u1EXU4H74h28bb_YhC5Amw1SgsVPOJTB7Dz4jZSTsLjj4qrn8XfwC8wNN9tu00KlaaWNg2NW_7GtANCjp7IoKAcMdEjIb7BcjIx_S8OQRvQCcAq4Yz55hvckxuVM8OpJTAkicjegCeSbXmNxLDcvlJNBwFvrthSg6FjSS_-qoCo17xkUKse_4DPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=h5QHsx2ApRpJMVR4BV5dM39c4Oju8AolqNLq7zqOPkBESCDWCheJ2BzVT_PKxR91H9qHy1033IZ7tEs7-n59j1OcL11RThkhHSJUBuldJ6er-6bkQd9ANDAfzL3dT0cs8Qwwxb5y1iX14XMuNQWn7MJxRwFM0u1EXU4H74h28bb_YhC5Amw1SgsVPOJTB7Dz4jZSTsLjj4qrn8XfwC8wNN9tu00KlaaWNg2NW_7GtANCjp7IoKAcMdEjIb7BcjIx_S8OQRvQCcAq4Yz55hvckxuVM8OpJTAkicjegCeSbXmNxLDcvlJNBwFvrthSg6FjSS_-qoCo17xkUKse_4DPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما هم از فیفادی بدتون میاد
🙄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107055" target="_blank">📅 11:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107054">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=SIXfExxcTp2Hs4NaJw8RHAY8suqzhj89IMgxlqkuovHmBQfr1mcDC1TOVVDBLjQpvTuVFJsN5TUDDUnNmOIhlIhEje0WbKEH_EP1PzbMRxzx_PhRJ2s2UmB1tzQb6Co-JJycIWIb30D4SYYpr3bnMXO0ls_WjfB52QAH-07XhES2HRusYywgeluKsbqBDDlo-_XW1QbG1141-Se5RwIB94hOak9ug9TNjTU23xCYnDkperogIuTePZ5iZde5XYx9rHh2-XUOCnxmc8f-jcUtH7eiLstgIodvwN39INBAHtK6WpJKoOK6JMQTxCdDPOIV6-lYYnhcK3kYl1QWuQdVxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=SIXfExxcTp2Hs4NaJw8RHAY8suqzhj89IMgxlqkuovHmBQfr1mcDC1TOVVDBLjQpvTuVFJsN5TUDDUnNmOIhlIhEje0WbKEH_EP1PzbMRxzx_PhRJ2s2UmB1tzQb6Co-JJycIWIb30D4SYYpr3bnMXO0ls_WjfB52QAH-07XhES2HRusYywgeluKsbqBDDlo-_XW1QbG1141-Se5RwIB94hOak9ug9TNjTU23xCYnDkperogIuTePZ5iZde5XYx9rHh2-XUOCnxmc8f-jcUtH7eiLstgIodvwN39INBAHtK6WpJKoOK6JMQTxCdDPOIV6-lYYnhcK3kYl1QWuQdVxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇱
اولین تمرین لاله‌های نارنجی زیر نظر ژاوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107054" target="_blank">📅 11:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107053">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107053" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107053" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107052">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvs4FKoB-KAIoZCyB70qNE1-x6W1ImzMd05VYSNAKh5CCkqrdJ-AW_QkbtnLWerWZI0aWbPX25sr4QM31bkmPYN9vxdoufoLCSlX15W4frcT0pqZssXfkZ3npelpBgP8XbUI9Ayg18h3Pd2I7YhKBCSJhPgkVdAw10C0IdGecCG1mBGDw4UhNeP5G72m85I3A5j9Yxp1aCglZxB7ICj531BozJWoe075E3PVEvCZNcpKhihAnWTY6fjBevXgx54xiLVvopGpcwnJoIJR6_hHPktpNtDDgI7whZFKmOcK_ysWgFXJUfdqpCLKgiMNjXE5xbMMV_ejrlZrhI0xrMg80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107052" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107051">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5JSOOLoajzxOpFU5rKmpViaKxE5gTd6UlD9HbdlUiBNsuYWajI9ihENo3f9sDQUmMHbS-MXRlUF_89gVjYxRpcfIZi1nYxc1jpWDsd8FuBnVndsRB-arpqtw6sWqZ1cx7WDMJc-PlQBZnp7xknQUhg5JbGHbrSzcO6FMM4mlbGfPr2jOnrZRcBDUuc-VCyvljfuZQrTtpMPWtbaKnr3Wi45beelz2K3fIHGl387x7Ug-XLiTHu3DOs-ikw1caM6APtFrzdSqbssXMgZ3U9tX7OGsp1wH63VZLPP52JaE-J5LILRQ-z18X4kwKCdCx1GfVa0HDcoRn4nX0J7av9yXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل مسی ۲.۶ میلیون یورو برای کمک به ساخت مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
✅
این مرکز تخصصی سرطان کودکان در بیمارستان سنت خوآن دِ دئو بارسلونا قرار دارد و ظرفیت رسیدگی به حدود ۴۰۰ بیمار در سال را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107051" target="_blank">📅 11:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107050">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=qRHopVpmjKRcGewJxQsDN-xPkczp8FmLeD0vgpaKM0wvMNF9Mu2mMgO3lh8qrVa3ETyjp82MJ90jksdwuchGyBdmcRpfWEY9iPHSqPh8sj54M5-3Emj1B9Rw6h_3783aeb3_S2evcblGY-fn5i0xQD97JvkH_cHq2vIPcFRpGle2MGkg3TEWiFGurMkycxc-1NYVtEnQsfmaDPKNqtwPEwhyeEU7Hmb-SvlV7tNMHg1maJq15sTh5s_N16ozbj3xgaWh8YgGfBVWcohpChS5UBt-TL6yY3IrEiwnQ2Xy193Usp7i117zTaI9iI6-yme-KNC7IEDi8uxkXo8SLztACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=qRHopVpmjKRcGewJxQsDN-xPkczp8FmLeD0vgpaKM0wvMNF9Mu2mMgO3lh8qrVa3ETyjp82MJ90jksdwuchGyBdmcRpfWEY9iPHSqPh8sj54M5-3Emj1B9Rw6h_3783aeb3_S2evcblGY-fn5i0xQD97JvkH_cHq2vIPcFRpGle2MGkg3TEWiFGurMkycxc-1NYVtEnQsfmaDPKNqtwPEwhyeEU7Hmb-SvlV7tNMHg1maJq15sTh5s_N16ozbj3xgaWh8YgGfBVWcohpChS5UBt-TL6yY3IrEiwnQ2Xy193Usp7i117zTaI9iI6-yme-KNC7IEDi8uxkXo8SLztACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
در این ویدیو پیرترین موجود زنده دنیا را مشاهده ‌می‌کنید، کوسه گرینلند که بیش از 390 ساله که در اعماق اقیانوس زندگی میکنه؛ این کوسه زمانی متولد شد که آیزاک نیوتون، موتسارت و چارلز داروین هنوز متولد نشده بودن؛ البته که گالیله 70 ساله و شکسپیر چندین سال قبل از دنیا رفته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107050" target="_blank">📅 11:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107049">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=oUrd6QYLwX7TcdF3IXOlbsvY-HNGVLNK7XSvrmn1GaHQCMGH9LX83EBmVvDhnXhMmVAAQoU_dfcRiWn8WcHTg5b9NOzHNRBHLvXKBFv8tNvUXomP00EAy9tZrEXdU9XyMbemuSzqCjGq4J02-upS2x8NZACsgQCjTH8VJJw0vboIkmWvjtUBTM3JpOu9t_nKKbi81jgqikkcD45F40lIYEyFkjTmXIDIknGzuoyEzc-qLpvdgFy7g8vhg91VeQLwtA8QdvHQLS4ExW6B7dTCdb70LeSfwl5oMZPhXuAmclNSZGabM2qklCtdYNLe-B0LmnOfG4KVZQtuMlx1eX_kCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=oUrd6QYLwX7TcdF3IXOlbsvY-HNGVLNK7XSvrmn1GaHQCMGH9LX83EBmVvDhnXhMmVAAQoU_dfcRiWn8WcHTg5b9NOzHNRBHLvXKBFv8tNvUXomP00EAy9tZrEXdU9XyMbemuSzqCjGq4J02-upS2x8NZACsgQCjTH8VJJw0vboIkmWvjtUBTM3JpOu9t_nKKbi81jgqikkcD45F40lIYEyFkjTmXIDIknGzuoyEzc-qLpvdgFy7g8vhg91VeQLwtA8QdvHQLS4ExW6B7dTCdb70LeSfwl5oMZPhXuAmclNSZGabM2qklCtdYNLe-B0LmnOfG4KVZQtuMlx1eX_kCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاییز با بوی نو کتاب فارسی شروع می‌شه
🍁
✏️
حتی زمان ما، شروع مدرسه ها صفای دیگه ای داشت ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107049" target="_blank">📅 10:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107048">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=gTAcPOsRnvuvX5d1ByEPo2UjkrDyyaLO4iYKdVjuv_nckHLUAKoXoEZVqwf7T7n-SN0MXqo3ySucQvz38N9gvmHyokEY-HuhNCh6iRvrqEvzCHc7924386dgFDLPwOL2RpQlHKeK9L_65xph4_PQcNM2FHctIAMz2JXyjr_OdS9gAh_z9rrgUmgOnx1brOlIGUxVh2obIAJEbb5IC8X2f1T-yHssYqYPri5f59RPNAHDmkLMTShfBEl-nvffLs7mFap3IsTAJYhC7Q4A1B12j2ZsbghLQ7neP4JYGmT0ZoGeWMc7P1FgYtcx9ULDP4gTBGEnabbh6g8P8KkeUbIEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=gTAcPOsRnvuvX5d1ByEPo2UjkrDyyaLO4iYKdVjuv_nckHLUAKoXoEZVqwf7T7n-SN0MXqo3ySucQvz38N9gvmHyokEY-HuhNCh6iRvrqEvzCHc7924386dgFDLPwOL2RpQlHKeK9L_65xph4_PQcNM2FHctIAMz2JXyjr_OdS9gAh_z9rrgUmgOnx1brOlIGUxVh2obIAJEbb5IC8X2f1T-yHssYqYPri5f59RPNAHDmkLMTShfBEl-nvffLs7mFap3IsTAJYhC7Q4A1B12j2ZsbghLQ7neP4JYGmT0ZoGeWMc7P1FgYtcx9ULDP4gTBGEnabbh6g8P8KkeUbIEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107048" target="_blank">📅 10:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107047">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090ef42156.mp4?token=mAydgFE1JTizWLCkyLKxzhF8IYegg7hkUZqXh7QVraci0TtA2G9Z56IerZiq_mMPeG6LKqLAld3sZFthcCw-4WPvLhZkyWnkJ3SzoJGr-YoL1fruGuQ09D_EPM05lUJH_z-QsmWGymNEYiiiFaXWZR6gsSFLBGGVCKSpO_68VEnqhVXiSuvOp5BwSmddmUgu3gtDGSE3g1jdOkMhleR864EhbcI0XZyL2a0YsjahYCe8Y_ei3uV4UT_7vJ__YHmqq40ZPBPSmA91OoZSeCjKZIioSu3Wt1zrdOMANXM9BShO6ED_3rWMYs1xHRKwQMc5Y5GdZILc0IEhe5KyFKbb5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090ef42156.mp4?token=mAydgFE1JTizWLCkyLKxzhF8IYegg7hkUZqXh7QVraci0TtA2G9Z56IerZiq_mMPeG6LKqLAld3sZFthcCw-4WPvLhZkyWnkJ3SzoJGr-YoL1fruGuQ09D_EPM05lUJH_z-QsmWGymNEYiiiFaXWZR6gsSFLBGGVCKSpO_68VEnqhVXiSuvOp5BwSmddmUgu3gtDGSE3g1jdOkMhleR864EhbcI0XZyL2a0YsjahYCe8Y_ei3uV4UT_7vJ__YHmqq40ZPBPSmA91OoZSeCjKZIioSu3Wt1zrdOMANXM9BShO6ED_3rWMYs1xHRKwQMc5Y5GdZILc0IEhe5KyFKbb5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی: مربی داشتیم (کمک فرهاد مجیدی) که آدم بسیار فاسدی بود. همه فوتبالی‌ها میدونن فاسده اما هنوز داره مربیگری می‌کنه
+احتمالا این شخص فراز کمالوند هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107047" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107046">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=vkM6Nln1XY7vVln5UJ5RKRsJyj80QT99RXia-Lz8UmAjQWJR2n63R2IEDcNqaOwBqBZJ-RfkBJAi2eC4Ij0YwxkQY3IIeQhaLovV4uP_LB467jLX03IGT__l-2MZ_NiH0_obxtEaAR6o4f63mkPJbBFZmntufbNICn0Ss1zBZim974FMj50RWyXfm9lbvhB2DlV3CVyIZu-vPJ8TqH2_g_tdLIi0ZWY5ZYuhNXFmoqvIe89OSlnExjIfJEssTPV52WOK9QWsJp6SwC-A5qy_4CbZsubGN45LOAcG1wTGG1yWkFoOHR-Xcyd9fpFILnJOM7mJMv14bBclxLa7kmx5Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=vkM6Nln1XY7vVln5UJ5RKRsJyj80QT99RXia-Lz8UmAjQWJR2n63R2IEDcNqaOwBqBZJ-RfkBJAi2eC4Ij0YwxkQY3IIeQhaLovV4uP_LB467jLX03IGT__l-2MZ_NiH0_obxtEaAR6o4f63mkPJbBFZmntufbNICn0Ss1zBZim974FMj50RWyXfm9lbvhB2DlV3CVyIZu-vPJ8TqH2_g_tdLIi0ZWY5ZYuhNXFmoqvIe89OSlnExjIfJEssTPV52WOK9QWsJp6SwC-A5qy_4CbZsubGN45LOAcG1wTGG1yWkFoOHR-Xcyd9fpFILnJOM7mJMv14bBclxLa7kmx5Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
تعریف و تمجید حمید مطهری سرمربی فولاد خوزستان از سهراب بختیاری زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107046" target="_blank">📅 09:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107045">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=Gtt0OgS-T74ZRdRU_LL7Qtngqo-RMGdR1MVPDC3BfGbR5qm172xHEMlbjVSe8Udq5G4gUI9qvhjXLbG6MmIScb_8rGaVQ5KIWdSYUOeivGjQAY-52usNnZxvXgQT54JZpinpPrm-n5RrYKYhXj-1xgW2CvzHQVREFCvha-yxsU0qYZ7P8X_liDyNFX-DIv0cCdDxPHCeOASmmbogzDgrEeAjCffRTHlhKfWGKPfKTlCfyUsjtP3ErxaxENyti3Vsr86m2zeE9Dun0xtN9suKHdDZwVIlY8nUC6MajS30uCszx_LIB6C76RTtHIgD10i8H68oaSjeelt_K-QVDJ8mTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=Gtt0OgS-T74ZRdRU_LL7Qtngqo-RMGdR1MVPDC3BfGbR5qm172xHEMlbjVSe8Udq5G4gUI9qvhjXLbG6MmIScb_8rGaVQ5KIWdSYUOeivGjQAY-52usNnZxvXgQT54JZpinpPrm-n5RrYKYhXj-1xgW2CvzHQVREFCvha-yxsU0qYZ7P8X_liDyNFX-DIv0cCdDxPHCeOASmmbogzDgrEeAjCffRTHlhKfWGKPfKTlCfyUsjtP3ErxaxENyti3Vsr86m2zeE9Dun0xtN9suKHdDZwVIlY8nUC6MajS30uCszx_LIB6C76RTtHIgD10i8H68oaSjeelt_K-QVDJ8mTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
فوش ناموسی بلینگهام به مادر داور بازی با اتلتیکو که شکار رسانه‌ها شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107045" target="_blank">📅 09:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107044">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=XTHqNasWvDIM1zj77aEFWefpMeTyHyBNQXjCpRNG1bdGtwhglvw6xMRVSwD_UtwZILrHNvBh-Dc4SkXQGA1E_X7vIfQSuSaj7znEw4cib7ClrWVfM4TfD7wWYhHYMfD_97_wQBiSVHjCn6qE_hoUoshyXEyAroFq4b3RyRlWnFxmbh2QpSb-sxuVbJIjP3fmXxKHFIJWB7uaA8pTxO9vopAQJlIh4DylJ7eLVp3CFjlF8LdG43lilF52I_Gtybs7aCsU6zS5Iw14Ig4CPuoAoa9HDWZgWfX0IS0Sl28Ntg4XcL0mxEUstiJZnnwPj18xC4AT7gJ-qPN0xouwyZG1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=XTHqNasWvDIM1zj77aEFWefpMeTyHyBNQXjCpRNG1bdGtwhglvw6xMRVSwD_UtwZILrHNvBh-Dc4SkXQGA1E_X7vIfQSuSaj7znEw4cib7ClrWVfM4TfD7wWYhHYMfD_97_wQBiSVHjCn6qE_hoUoshyXEyAroFq4b3RyRlWnFxmbh2QpSb-sxuVbJIjP3fmXxKHFIJWB7uaA8pTxO9vopAQJlIh4DylJ7eLVp3CFjlF8LdG43lilF52I_Gtybs7aCsU6zS5Iw14Ig4CPuoAoa9HDWZgWfX0IS0Sl28Ntg4XcL0mxEUstiJZnnwPj18xC4AT7gJ-qPN0xouwyZG1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
شعر خوانی جالب قیاسی:
«مثل رابطه سهراب بختیاری‌زاده و صالح حردانی
مثل حال دروازه‌بان بعد از تک به تک شدن با یاسر آسانی
یا مثل حال اتوبوس تیم ملی بعد از جریان کنعانی»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107044" target="_blank">📅 08:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107043">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107043" target="_blank">📅 01:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107042">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfEQ6seswBEhfoCFT6BhaqC-1v4E4KLj0OUcYwutxzG_Abam08a4qcRWGxXdwUKKxfy9mSGRIpWC5fJ68c78rz8OXBVxGhSrVDEJ05GciFQJSyETDfnNGuinnLnvD6EzgqtPODOyWz8hAHTEyj4-m0cDRiirg5uPEtuOkCdrGRCCUvDikD0euW4s0m-nEPQKGeejB0n0yFE-lVfBCFMzdI1d57m1Cpx2dzwisFTVcSeKBd_IRTSMBQ2ZAgLXjZ32tDZFha3PQB1O8YaK-VxXeZ8bxtztQbw3Q_vvPsIW7hWmRh-Sk_vj2xILLRU8vhOLpGSeRNRSIBZDWaSE3iRp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107042" target="_blank">📅 01:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107041">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=kCUnfgRqWFpZQOpQXSK-rNyMdA1lWDPJelWv_FGSZTsUfzNvFb81O3Gqr0GPus6c6p1sYfTSygF4tgU9M6ijPE7Z0BTsaoxMgd1on5DBBcTAE0MByRVJcu5iZzmJAErQ042mL_t3M4NWxMEcvZ0Ked7oK4EfYg1UkplrDt8hCWvyMWZn-TLPJb1-3RvNDHtqElvwdfjQUg4Ufveg8XMtLg5rEPwZvMLkwyot30gkSnIe-s3uNImLyRtJVZiF5LWRT3dsZik5SjFnpXAoQa0_k8uDARhNwOdA3-DCwZSUrAG4p2IErvE1gdRDKZuEM06tEkZXVNMGfwsq5T94eYVdWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=kCUnfgRqWFpZQOpQXSK-rNyMdA1lWDPJelWv_FGSZTsUfzNvFb81O3Gqr0GPus6c6p1sYfTSygF4tgU9M6ijPE7Z0BTsaoxMgd1on5DBBcTAE0MByRVJcu5iZzmJAErQ042mL_t3M4NWxMEcvZ0Ked7oK4EfYg1UkplrDt8hCWvyMWZn-TLPJb1-3RvNDHtqElvwdfjQUg4Ufveg8XMtLg5rEPwZvMLkwyot30gkSnIe-s3uNImLyRtJVZiF5LWRT3dsZik5SjFnpXAoQa0_k8uDARhNwOdA3-DCwZSUrAG4p2IErvE1gdRDKZuEM06tEkZXVNMGfwsq5T94eYVdWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🐐
🇦🇷
رونمایی‌رسمی لیونل‌مسی از پیراهن ویژه خودش در آخرین بازی ملی با آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107041" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107040">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b37185041.mp4?token=ZR6T5feNYyvKysqDa4XkVfKd1Z-UsX4HIbx927fKut_5UVuFDXFt8VXJ5kEZDuMSygZ42i03_8_CZjb9WOBvs2PmGecF4lkUWYSRL2PGNZYQWUnQ-i-eRCZhpacF-E4qD6Ff2fkM-KF7LUDzT2AOwYmfMLWFsTydOV8gjr5ZGcsFFEYi9wRUESc8sarDe2YksXH33O4oIZhUpf7HEQvO1WEO9V_Wo9SaD8eGwBPAEeYX_k0Nvt3l8dZnvct0dVO4lhmMgQHTJHZb_HRC9npixME4tDLZj_ta2XOvGDTt5ymKfKRxpTJBf8BT16ffIWCa7jvdGz9PARCl0F7GdyC-ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b37185041.mp4?token=ZR6T5feNYyvKysqDa4XkVfKd1Z-UsX4HIbx927fKut_5UVuFDXFt8VXJ5kEZDuMSygZ42i03_8_CZjb9WOBvs2PmGecF4lkUWYSRL2PGNZYQWUnQ-i-eRCZhpacF-E4qD6Ff2fkM-KF7LUDzT2AOwYmfMLWFsTydOV8gjr5ZGcsFFEYi9wRUESc8sarDe2YksXH33O4oIZhUpf7HEQvO1WEO9V_Wo9SaD8eGwBPAEeYX_k0Nvt3l8dZnvct0dVO4lhmMgQHTJHZb_HRC9npixME4tDLZj_ta2XOvGDTt5ymKfKRxpTJBf8BT16ffIWCa7jvdGz9PARCl0F7GdyC-ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام علیرضا بیرانوند به میثاقی روی آنتن زنده: اگر نظام وظیفه اعلام کند من چه زمانی باید به سربازی بروم به جان 2 تا بچه ام فردا می روم سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107040" target="_blank">📅 00:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107038">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXWENM7ZhtgeuMXpyV0qF5xaJU8hRPZ6aonO4nxtd-dtlzMS9rAwtW-GxRyv13kaRfOuglTvtVs7-7wcWMdLNDUPN0XCY6-_VlqVPi4x5fsp5UXOg1J-N3AANlkHWEQwKKoUSW9o3HZYA8S4m_3J3L4wXpngQyIoFxNQespvJxMBxj8QlWmBMrXVCRP-EXU1hoaWDi4KT6QwnCFP-E_NxMQVKeg8RFFz0RYCLo3YQXO7i-1KEZNtM4Ab-9XyQrDV7jnF6AN6I4FgTdBv70yifOYUzn4HH0Quiw9nqkh9ZKbC6YCkao9jFMSh2NwAIfXlIv-wH9uPEXIciSeyNS9GCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHIyPghGc1MY58fPnMLe4nrbFChvb1clDVVop3M-lo5Zm_lJ94_TVpv7G49RWFMPelkj8lg9JinPT6naNJDiM8TX3spi7bzre7MgYVTllybttqCSQmtxJ9pTN73lfWZERytAYZUAju4HSTHFV6d3TgQOxDv0LGqWV00A--ZoDokS2NEhXFyYBcxoNz5B7Vb3ycLABGIr8e7yq0q6_Nmk8VCcmAK39KPBkXqqLWiAoMQGFs0UOVNaDFatHZNnMnuPrx1XDdX1Cj_Rqpf-9J6il3NrtCVzY_z7-R1tBBPdt96zQa6XF9Uv4yPmQtycJ5a6DvSwS9zhb4uu_aBbqSICwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
دلیل عدم دعوت اللهیار صیادمنش انتشار این استوری در ایام اعتراضات سراسری دی‌ماه ۱۴۰۴ است که باعث شده حداقل تا چند سال قید حضور در تیم‌ملی را بزند مگر اینکه به مانند سردار آزمون دست به پاچه‌خواری بزند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107038" target="_blank">📅 00:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107037">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
⭕️
‼️
اللهیار صیادمنش: در اردوها به بازیکن احترام نمی‌گذاشتند. حرف‌هایی که جوان‌ها نمی‌توانند بزنند را می‌گویم. در این چهار سال ۱۰ بازی دوستانه روی نیمکت بودم، ۲۰ دقیقه هم بازی نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107037" target="_blank">📅 00:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107036">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
⭕️
🎙
اللهیار صیادمنش: تا این افراد در تیم‌ملی باشند حتی اگر بخواهند هم دیگر برایشان بازی نمی‌کنم. در اردوهایی که زیر دست این آقا(قلعه‌نویی) دعوت شدم هم چیزی به من اضافه نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107036" target="_blank">📅 00:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107035">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
⭕️
‼️
🎙
گلایه تند اللهیار صیادمنش بابت ربط‌دادن عدم دعوت به تیم ملی، به مسائل اخلاقی: می‌دانستم قلعه‌نویی هیچ اعتقادی به من ندارد چون اصلا هیچ مسابقه‌ای را از لژیونرها نمی‌بیند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107035" target="_blank">📅 00:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107034">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0e4K3bMh1oFEUNBCYM7VtZ0FQTa1wk-1_GWopUXmCcFkwnk-iJsdTwN_dY3EhkdofVpPB3Ap00MZiFmYiiHhZJ0MUR5vRu-xMjR9YdXIYkDD36g5sQP9lrD0YLXYToUWalbg5ionwZt01DgdaSM2orqssH8uCdD46y5fSOGmrdxcsV7IXtfduXEsOHu_JJds3Bcz1tYxWUjHAHx5vHIfAxejyNneJKrZOtUnPcosGDDcqNKCTyZ8iVYMUJ2EVdrt9_hQzMB6sYIxquzWBmCf8op8GJD8qj5A4E2yeI8GQNkn2v3QiHYlEfRVHphc-hdDc5aAHtl3NZsCfDD_pi9Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
خاویر‌تباس رئیس لالیگا:
🔹
باخت دیروز رئال مقابل اتلتیکو صرفا جنبه فنی داشت. درست است که اخراج یک بازیکن حریف نادیده گرفته شد اما اینها بهانه خوبی برای باختن نیست. امیدواریم رئال‌مادرید واقعیت تیمش را ببیند و دست از جنجال بردارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107034" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107033">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=RzK18LMTl66mDTpuiIv88tPVSwz_BAy78CCGjM5kQm1_dtpbeXXOzb3I8wGlZMNihHNsTRzIjOr-uvHcxTwxT0LAr1cRDhElcbzoy0qPBrWXJBxAl_bDKGuN5HSHH7RAFpWPv2vi9EZW5HSnczFu3yklzqYaBHfrWR4MIzycN8C8-Nm6VE1DGPiFgItBail8KT-TayivVXIE-HxmXzDr0iEclpyvkPt9hUVbKUyIK_h060qYPuZCl54I9aEpNdFPeTR837cLTFjuzJNlNnNBhmKhIqREpcYBSYDC2ryfg0Kw7HaCGtwHLirfpPR2fH2G_t7NgIab2j7tDb8EjTem4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=RzK18LMTl66mDTpuiIv88tPVSwz_BAy78CCGjM5kQm1_dtpbeXXOzb3I8wGlZMNihHNsTRzIjOr-uvHcxTwxT0LAr1cRDhElcbzoy0qPBrWXJBxAl_bDKGuN5HSHH7RAFpWPv2vi9EZW5HSnczFu3yklzqYaBHfrWR4MIzycN8C8-Nm6VE1DGPiFgItBail8KT-TayivVXIE-HxmXzDr0iEclpyvkPt9hUVbKUyIK_h060qYPuZCl54I9aEpNdFPeTR837cLTFjuzJNlNnNBhmKhIqREpcYBSYDC2ryfg0Kw7HaCGtwHLirfpPR2fH2G_t7NgIab2j7tDb8EjTem4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
میثاقی: اردوی تیم ملی تمام شود سربازی علیرضا بیرانوند تعین تکلیف می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107033" target="_blank">📅 23:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107032">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=WLzDifixhaU59MWeca6OIr1wSfC_Bd6SjRu2YdCHkbk0pF8hqiUs4jSWU4BxwjtRX88uwD_F--HNmHnVkN_ZWm7wCnw5ZCiRIDB_wTeQjGasvTt9tr3HrmFkUMlLl5qtSyNUH4EXprYUAYCJxP5RCl2wAWGRnPw9NXtMq-XO3SKTlwSkuToq_5mnLbqa3yjByj8LPURXS71K31ZHJpElXh9BSK3DisRoiSKEtDV9EFkBGG1UudURBLUurUkKxKJ25vcqmQk4An6BUSkUhJg72uJiv6kfFqajSdnZaExLG6D-YSiFN2psQhSP6ddS8Rq2xXzg7ngIsz4rgYz4U_8vWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=WLzDifixhaU59MWeca6OIr1wSfC_Bd6SjRu2YdCHkbk0pF8hqiUs4jSWU4BxwjtRX88uwD_F--HNmHnVkN_ZWm7wCnw5ZCiRIDB_wTeQjGasvTt9tr3HrmFkUMlLl5qtSyNUH4EXprYUAYCJxP5RCl2wAWGRnPw9NXtMq-XO3SKTlwSkuToq_5mnLbqa3yjByj8LPURXS71K31ZHJpElXh9BSK3DisRoiSKEtDV9EFkBGG1UudURBLUurUkKxKJ25vcqmQk4An6BUSkUhJg72uJiv6kfFqajSdnZaExLG6D-YSiFN2psQhSP6ddS8Rq2xXzg7ngIsz4rgYz4U_8vWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ابوالفضل جلالی بازیکن پرسپولیس: برای هواداران استقلال احترام قائل هستم. آنها زمانی که در تیمشان بودم به من انرژی دادند. در استقلال بهترین عملکرد را داشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107032" target="_blank">📅 23:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107031">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=Q-SPIF2bv63dgGVlOzH9KZFhubSRcBfHG0ouDIPaiRshXxcELkAF5pHRqjFgtXHEmGn9eJWClotx_CqpYJsQXrukOOM1Kfiq78TGsdB6Ej5DCLVriUFoOFtjbbr0gvzhBzGgAEL84AYtjEWd1e35FFWQtIqmHThIVkmjWDqhjF1ntTVDirL7UzWqA4AFeKV29C_fN8L2-51_MCqBSOUaFf-3ljnMHsEwwfWyYIv3dguavTHsuF06xNRRdhUXJdjvWnO0EohvGLUclYEaIcoZbrCejcMLPKryRq6bDr-SIsC6xjEdEw3un0h0IWxmYqVjbajWuo1KYyr8qrUKx0cXDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=Q-SPIF2bv63dgGVlOzH9KZFhubSRcBfHG0ouDIPaiRshXxcELkAF5pHRqjFgtXHEmGn9eJWClotx_CqpYJsQXrukOOM1Kfiq78TGsdB6Ej5DCLVriUFoOFtjbbr0gvzhBzGgAEL84AYtjEWd1e35FFWQtIqmHThIVkmjWDqhjF1ntTVDirL7UzWqA4AFeKV29C_fN8L2-51_MCqBSOUaFf-3ljnMHsEwwfWyYIv3dguavTHsuF06xNRRdhUXJdjvWnO0EohvGLUclYEaIcoZbrCejcMLPKryRq6bDr-SIsC6xjEdEw3un0h0IWxmYqVjbajWuo1KYyr8qrUKx0cXDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
ابوالفضل جلالی مدافع پرسپولیس: الان طرفدار پرسپولیس هستم، عاشق پرسپولیس هستم و سرباز این تیم هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107031" target="_blank">📅 23:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107030">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=Sz67kh2JrQ4RTO3_5CIHbfQ151hrMmCeX6NrgWuX1I-Aq9yoEb2QAR9w_F5R8SaQBTtUD1GEwt4ktDpwGKM0nKx_4RWEbmCRLLvFDXO3f-EoPccPInrQunaG6XtVQh5ARDYLtNYO2umpPHWAoLNXdtQzCnvl-CM2PfTZwp6K7gyVc0SDePtmUWdVRKenD94LoC5WmzpYcmheoTAePHe17I5Vh3tJkwOhpGUvQ4DHG63Z148oldDWaFG8KpgGlLFdMnphmpgvPz2bgpGTiu_592gKDKLLqWwrl2Xt4ID6bfDufkjwFdmj5s8ENXfNMyFuHf1ZujDXNj5ehQkQGHqDQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=Sz67kh2JrQ4RTO3_5CIHbfQ151hrMmCeX6NrgWuX1I-Aq9yoEb2QAR9w_F5R8SaQBTtUD1GEwt4ktDpwGKM0nKx_4RWEbmCRLLvFDXO3f-EoPccPInrQunaG6XtVQh5ARDYLtNYO2umpPHWAoLNXdtQzCnvl-CM2PfTZwp6K7gyVc0SDePtmUWdVRKenD94LoC5WmzpYcmheoTAePHe17I5Vh3tJkwOhpGUvQ4DHG63Z148oldDWaFG8KpgGlLFdMnphmpgvPz2bgpGTiu_592gKDKLLqWwrl2Xt4ID6bfDufkjwFdmj5s8ENXfNMyFuHf1ZujDXNj5ehQkQGHqDQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
ابوالفضل جلالی: ساپینتو شاید از قیافه من خوشش نمی آمد که به من بازی نمی داد چون از نظر فنی مورد تایید او بودم/ جالب است رامین رضاییان هم همین مشکل را با ساپینتو داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107030" target="_blank">📅 23:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107029">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=CnNzd-j28UTk9pKLQKiDcG-lVenaM3HMIATLsRzbvspdcAbA12gA0qh3qaWfrWbJDby8Blcyk1hP4LAYnDKrXkcBb67E9T0oqn6NRFLJJZ0HivwYh5Lz5Tqg4q1hvQhjkgh5LfeK4PsTHYgYX1o3O6Y1k18WjGswyZuUf573sIDYRkSWE5WgGydUjQEsNyEEGzyCwfExkGpc-mcdF_vbae7sUW32LsuwE733QPo-n_f_619fLfldWpkMOJ_Bt47nI4IAWnslXGD7ZjiXuhmBm_gG9aTItslNt_tXMJs2Jy5x70qy0mOa8vteUMR4bGzXjpc0CHMmVGu59Q5CT8L3aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=CnNzd-j28UTk9pKLQKiDcG-lVenaM3HMIATLsRzbvspdcAbA12gA0qh3qaWfrWbJDby8Blcyk1hP4LAYnDKrXkcBb67E9T0oqn6NRFLJJZ0HivwYh5Lz5Tqg4q1hvQhjkgh5LfeK4PsTHYgYX1o3O6Y1k18WjGswyZuUf573sIDYRkSWE5WgGydUjQEsNyEEGzyCwfExkGpc-mcdF_vbae7sUW32LsuwE733QPo-n_f_619fLfldWpkMOJ_Bt47nI4IAWnslXGD7ZjiXuhmBm_gG9aTItslNt_tXMJs2Jy5x70qy0mOa8vteUMR4bGzXjpc0CHMmVGu59Q5CT8L3aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید الهویی مربی تیم ملی: درخواست کرده ایم که از اول دی ماه اردوی آماده سازی تیم ملی جهت حضور در جام ملتهای آسیا را برگزار کنیم
🔴
میثاقی: با این وضعیت بعید می دانم تیم های لیگ برتری بازیکن به تیم ملی بدهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107029" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107028">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12081ba765.mp4?token=gJ1CLmDS0CR1gc_RZMaBczW_ZYEROfI3_ThI1-Y_2tlbBGubolRmROLOifxguvc_WcWrL4jmfWiEJ1Dy3lS2hSIj-gR4Q6Gjp7F0gN48NhkEpKSBn5WMT7M_RDNyOysNmS-PxP_H3xGLdVbcfpQ83nCisjqrWQO89TAyVSIHIeFAVYBB1YM6QWcnOt44fYrZmjPRNeY_FtgfR0Xmg1aANUL9U9MNzJZA53bYHeyuZ3lyIiHVfzNQUDdGoYmgOGqtpj1xTP9DVsS2Gb647T8wP4ra1EzNqVkWuqQViLFhq8u2WgGLSjKY0glUe09FdUaXAbw2x9X8K3OxkQypmK_IUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12081ba765.mp4?token=gJ1CLmDS0CR1gc_RZMaBczW_ZYEROfI3_ThI1-Y_2tlbBGubolRmROLOifxguvc_WcWrL4jmfWiEJ1Dy3lS2hSIj-gR4Q6Gjp7F0gN48NhkEpKSBn5WMT7M_RDNyOysNmS-PxP_H3xGLdVbcfpQ83nCisjqrWQO89TAyVSIHIeFAVYBB1YM6QWcnOt44fYrZmjPRNeY_FtgfR0Xmg1aANUL9U9MNzJZA53bYHeyuZ3lyIiHVfzNQUDdGoYmgOGqtpj1xTP9DVsS2Gb647T8wP4ra1EzNqVkWuqQViLFhq8u2WgGLSjKY0glUe09FdUaXAbw2x9X8K3OxkQypmK_IUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
سعید الهویی: پرونده حضور احمد نوراللهی در تیم ملی کلا بسته شده است و این بازیکن خواب و خیال تیم‌ملی با حضور قلعه‌نویی را از سر خود بیرون کند
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107028" target="_blank">📅 23:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107027">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMiNEQsIovM0mXtSfMG0WFBDUe8pDqeut59dHvyzxQ_N4FoxYFvJBc9ooCsluJVPV1G-mTVcGJBymcVvBQHVmqhBrKPe9cPc3BtgfRMU4-pFTrFZtkUAzwXGcZO7bEiijmLCtRgCOzbbu3SxG1n9ejFNWIEimjdvOKT_X6iM93kAYvqTpBnTJ9uCctdSLiNwmyCZgWdf5wMLk0worMBbnZqRCARDGGPQUWevMpGDOY_VyLYthl0tb43iaAy70Zf1yRFV6N4BygaU9LXIuhfMBq8AOHE0wyumv-ue2aSb-Hmca-84o2oRGUk_dbpK5__vIQ2QlpgHN0Tz_CroYvr-dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/107027" target="_blank">📅 23:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107026">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45095faec.mp4?token=jB_x9hVPOgIPNf6aNzEYl43YnnISG-ikNiKV3Yb_Yh1st0smfBJVDZxLeU8rzrOMkZw18kwFSeiVV1UdgeZsSZe-its4XpAG-RyZJxkYr7H75gOiVBsigGIJR_7Wqxz41Gxhx0CwYKjPAwNSXOxYKF_JDpnQoC0idz7G8FIemHknz0VbwtTAUWck-9r3DyYrjWsyp7EbC4O-eec0K8WZ4ZBcVYv7CBwDw1hP1Yw_KQKLew_n4M-GTM0lE-FDh3AQWlF-qGikLvLn6r5q1kdeabtxBUE0r42T_SaV2b2vk6s6lC4m-MEgSTR6NZsGDLlVTkZ47pE5dkqQatZjWAwpew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45095faec.mp4?token=jB_x9hVPOgIPNf6aNzEYl43YnnISG-ikNiKV3Yb_Yh1st0smfBJVDZxLeU8rzrOMkZw18kwFSeiVV1UdgeZsSZe-its4XpAG-RyZJxkYr7H75gOiVBsigGIJR_7Wqxz41Gxhx0CwYKjPAwNSXOxYKF_JDpnQoC0idz7G8FIemHknz0VbwtTAUWck-9r3DyYrjWsyp7EbC4O-eec0K8WZ4ZBcVYv7CBwDw1hP1Yw_KQKLew_n4M-GTM0lE-FDh3AQWlF-qGikLvLn6r5q1kdeabtxBUE0r42T_SaV2b2vk6s6lC4m-MEgSTR6NZsGDLlVTkZ47pE5dkqQatZjWAwpew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107026" target="_blank">📅 22:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107025">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
🙂
🎙
به مالکوم گفتم Bro, Easy Football!
کلماتی که از درگیری شدید علیرضا علیزاده با بازیکن سابق بارسا جلوگیری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107025" target="_blank">📅 22:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107024">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
‼️
انتقاد تند عادل فردوسی‌پور: پدرمون در اومد این‌قدر با ازبکستان بازی کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/107024" target="_blank">📅 22:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107023">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=obIwdVSFOmD9SOMXz6Usoq3h35lB9bawOcl0IK1U5pzaf1hmm9_r145MNYkxPSpJPVbAOypzu0dJO0cnVzur54UrGUxIKmFIgJKA-fCJzlOAr7QGaLdHLXlCEUCp-NIqk-tbGgGKwxX5S-fxYsTwV49HTBEEvnZ36_FdEh_SK3fd1Q9bGkD5H-cHKFDSVKcGcBKBPQDUzvu3lHFa05XxLnmPYeEOmUhXFrf7wrZtAhkMMj60F6Z-jPFwQqzV3ArKgj1vc1ANk6t5C_zpFeHTLfeAb3MXXbxS3t9vp3IKRG7T-cyirtZa2O4uwVm2vRasudVU4vmAf_Css2xvByWJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=obIwdVSFOmD9SOMXz6Usoq3h35lB9bawOcl0IK1U5pzaf1hmm9_r145MNYkxPSpJPVbAOypzu0dJO0cnVzur54UrGUxIKmFIgJKA-fCJzlOAr7QGaLdHLXlCEUCp-NIqk-tbGgGKwxX5S-fxYsTwV49HTBEEvnZ36_FdEh_SK3fd1Q9bGkD5H-cHKFDSVKcGcBKBPQDUzvu3lHFa05XxLnmPYeEOmUhXFrf7wrZtAhkMMj60F6Z-jPFwQqzV3ArKgj1vc1ANk6t5C_zpFeHTLfeAb3MXXbxS3t9vp3IKRG7T-cyirtZa2O4uwVm2vRasudVU4vmAf_Css2xvByWJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ادامه شاهکارهای داورای لالیگا این صحنه رو هم دیروز داور بازی دپورتیوو و بتیس کارت قرمز تشخیص نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/107023" target="_blank">📅 21:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107022">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107022" target="_blank">📅 20:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107021">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abz0BF1cBAV_RPBPFRFbhlNtWBDduZS9ALjPYvF6c8Ui-u1_san61z6HGHmVcUtqN4d612PbYGDB7EtihMvB56zlfWoEukIxGZ68wjU1kce8ZPnA1DlxnQh4Rc5jZ424_ANOaJdULghCpcdnh9-ORHzwEpaobWUB9VCgNGD4E9-1xXYPxEIm_8_0-TxOmxogBk1bSU3Uvf1smVl7bqrTiER4co5gP1Xjn9JO2rLurjTcE2WApZPnCuje_GwwrHSOeI2r907KUwKyjopkT9EdNHi6wiokZiaWmEB1i5QNZoAMYwIn00xGzzcGN4qnSl3i__zxM5AGLSl23_soMXG48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
مقایسه آمار نیمار و رافینیا در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/107021" target="_blank">📅 20:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107020">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=UtkXF4Y1RbUGJHJRvtGio2Ln0mLOE-BS-6xi_YPuMJ6mZPVQqi4absllW7YzTfls0P75quARYquEGAQYh0EwRjoql0sKQqdyqsT6dRTfTCKyZjKRMxF5N6pfy25Ji9E1SuB7O7imSAd-9aHMTHtol4SePSc4kZenybkKhrFYCNsftAcUcGSWNf4tmXXw8daFSOVmGughMO5fNoVB-pCBZnKf9s24CaXChoUSyKwyKxhQNOcTUnt3q2rLt01uQNeUyTGKUIMr0fIpG8RwRyJpelULmsO-qEnK0QVNJhuu4B2bYnd_HXxrdaXuaVFwiie44-mhBx966s8WQyOsJthWpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=UtkXF4Y1RbUGJHJRvtGio2Ln0mLOE-BS-6xi_YPuMJ6mZPVQqi4absllW7YzTfls0P75quARYquEGAQYh0EwRjoql0sKQqdyqsT6dRTfTCKyZjKRMxF5N6pfy25Ji9E1SuB7O7imSAd-9aHMTHtol4SePSc4kZenybkKhrFYCNsftAcUcGSWNf4tmXXw8daFSOVmGughMO5fNoVB-pCBZnKf9s24CaXChoUSyKwyKxhQNOcTUnt3q2rLt01uQNeUyTGKUIMr0fIpG8RwRyJpelULmsO-qEnK0QVNJhuu4B2bYnd_HXxrdaXuaVFwiie44-mhBx966s8WQyOsJthWpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
واکنش اتلتیکو مادرید به عکس‌های پرینت شده مورینیو در کنفرانس خبری
: «همین حالا به آزار و اذیت داوران پایان دهید!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/107020" target="_blank">📅 20:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107019">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=qSUQ4TWLfwDR4WnQhaq9Sq9-invDvLpLhpE95J7QTsdyq5FIMFrmv-RE2F8NhdM43dM4htKRjolbFDXS6Q4lolF35LgDd0lSATA8EdGzIihVPbSWu6q5fnzRVMvCbsvID7-Fo2oYS56KKXT2ziyK1NS2GtXLM_vom2bqFZr-_zUq1RSPZON5mXdQ1N5X0YwPdpvG_dYyU8ZbzXYJmz2e7vhg9ome_FLFJPQKVnQAG-qyvJ35FyDoFMnCH38i2sVh5DbfzCGh8tHlqLXaCdNMYZKNV97Tc-_hzlJMW51on_RIV92Te85nH2G9S4ptExj4lUj-VkhLyxaJia_bendAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=qSUQ4TWLfwDR4WnQhaq9Sq9-invDvLpLhpE95J7QTsdyq5FIMFrmv-RE2F8NhdM43dM4htKRjolbFDXS6Q4lolF35LgDd0lSATA8EdGzIihVPbSWu6q5fnzRVMvCbsvID7-Fo2oYS56KKXT2ziyK1NS2GtXLM_vom2bqFZr-_zUq1RSPZON5mXdQ1N5X0YwPdpvG_dYyU8ZbzXYJmz2e7vhg9ome_FLFJPQKVnQAG-qyvJ35FyDoFMnCH38i2sVh5DbfzCGh8tHlqLXaCdNMYZKNV97Tc-_hzlJMW51on_RIV92Te85nH2G9S4ptExj4lUj-VkhLyxaJia_bendAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رختکن تیم‌فوتبال رئال‌مادرید بعد از شکست دیشب جلو اتلتیکو!
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107019" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107018">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=RHKTaE1KUlgVtVKhUfx4wkC2Nxh8ae2cnfF56s3gUlFCvHlJjN07I8h7KBHfuK768XjWj-TxmnYjZBYZw3usCbebA9S-E6S4fYmjQKAcarK_v0ZlFFbm5Jpvmrq-3aIn8KV0e1YumyNOd_Un3TaT9o8qgZ6Z9LNaGE2WxAzilZOsOxauh8Eje8fpDweH0O_MHkKOoU1CW2JM7aySJoz8K6jM_rMmGlg7ao36dYnPbTMVmFo7t_PYvvLkNVaOFZuSea3tpsHcthIzwGzQErS5MJhgcJzyaRZ7KrKVde04Ka978_JhNAaipLEpCGoydHYzWcZ4R6ZVKkRDmKvZemj4GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=RHKTaE1KUlgVtVKhUfx4wkC2Nxh8ae2cnfF56s3gUlFCvHlJjN07I8h7KBHfuK768XjWj-TxmnYjZBYZw3usCbebA9S-E6S4fYmjQKAcarK_v0ZlFFbm5Jpvmrq-3aIn8KV0e1YumyNOd_Un3TaT9o8qgZ6Z9LNaGE2WxAzilZOsOxauh8Eje8fpDweH0O_MHkKOoU1CW2JM7aySJoz8K6jM_rMmGlg7ao36dYnPbTMVmFo7t_PYvvLkNVaOFZuSea3tpsHcthIzwGzQErS5MJhgcJzyaRZ7KrKVde04Ka978_JhNAaipLEpCGoydHYzWcZ4R6ZVKkRDmKvZemj4GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «ک…، خفه‌شو» دهنشو بست و این شاهکار رو خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107018" target="_blank">📅 19:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107017">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=QnHM4mRrSOkQJigEmqktBSUXevIdl2HqUN1k8zWdWeLmrV_UyOmiNdo1LM2aQ8Joyd9LZya_u3Z3E96LkGsI2lh6uUkdGeAgEN_jKH9Ci5l3FLwkZ89cYaTGt6Gehaoa0AqxVy-sdW5DYzTN3LRVhuflt3IYe-3hWTKCUXnzBV5LXpQEvigbb8ahUUF5Bh5OencWIHy89S9NuItIc9WahK2RudtEoLQDIMuw_MJc4J3r0_fpbkCOa_PC37d_Fwcln0Wl8ZpPVoSr-ay0BN8dkT5vEp5AMAnQcbZNcaBu5LLvdbVnEmju8QMsz-J6AJsWQBy9Y6Fw63mG9ojj3X3o6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=QnHM4mRrSOkQJigEmqktBSUXevIdl2HqUN1k8zWdWeLmrV_UyOmiNdo1LM2aQ8Joyd9LZya_u3Z3E96LkGsI2lh6uUkdGeAgEN_jKH9Ci5l3FLwkZ89cYaTGt6Gehaoa0AqxVy-sdW5DYzTN3LRVhuflt3IYe-3hWTKCUXnzBV5LXpQEvigbb8ahUUF5Bh5OencWIHy89S9NuItIc9WahK2RudtEoLQDIMuw_MJc4J3r0_fpbkCOa_PC37d_Fwcln0Wl8ZpPVoSr-ay0BN8dkT5vEp5AMAnQcbZNcaBu5LLvdbVnEmju8QMsz-J6AJsWQBy9Y6Fw63mG9ojj3X3o6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت هاشم‌بیک‌زاده از استخدام مربی خصوصی رونالدو برای رساندن مدافع تیم‌ملی به جام‌جهانی ۲۰۱۴ برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107017" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107016">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=ke0Ll0FHubeqZIAQ7NKpG_R_UgS81ZlVM4UCcUd7_JRzJF-LG92FYGT0i_LnElM8WsOEK0mg_PbUAVyjLWWVfegqQNptiobiIBxiZCuy559AepJdWgcS5Y0oBOfqWv-vxdDuwaKvzT5wKmKsKemCVQiCHFqPGKPLDajLmRnS2WbSp8IfInY-juJgljTyD9FA1pqYoLqmdYTiIYfPGVDz4fr5Xg2PnNnhka63mbkjuE-8UJwTaqVlNAWhBA8jflADWupj9G4tQz9teaXqQepldJc4mLWx5Uv7TGiynMT73mMB8JXBCVwu_m_L8egNTYMhq9vq8PyZd_1KLDAcdPNcgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=ke0Ll0FHubeqZIAQ7NKpG_R_UgS81ZlVM4UCcUd7_JRzJF-LG92FYGT0i_LnElM8WsOEK0mg_PbUAVyjLWWVfegqQNptiobiIBxiZCuy559AepJdWgcS5Y0oBOfqWv-vxdDuwaKvzT5wKmKsKemCVQiCHFqPGKPLDajLmRnS2WbSp8IfInY-juJgljTyD9FA1pqYoLqmdYTiIYfPGVDz4fr5Xg2PnNnhka63mbkjuE-8UJwTaqVlNAWhBA8jflADWupj9G4tQz9teaXqQepldJc4mLWx5Uv7TGiynMT73mMB8JXBCVwu_m_L8egNTYMhq9vq8PyZd_1KLDAcdPNcgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین قیاسی: مهران مدیری برای حضور در برنامه من اصلا هیچ پول نگرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107016" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107015">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107015" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107015" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107014">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1LreGp64ka0yTSXnH-rAUtlQuKmRGzkykps62PLkngmRvN5zjNc7tiQ_SZeQTh516xzhM0Hj0vfHDq-JKNxkMC0cz95TQWHrXQ-2JnwxVgpeYhGbF7gfR7O4vRDSzeRuDbt793LiqDQ_P83cSw4CT2xwkK61UWvxyes4xNQZ3P2oChSN8gU7h-4b67d_1z2-t3mHQeD-_ETIr5MkmkhCgQtXxtOBmgx3hsUeBU1mWMvAiD9bfT0JCKUMI8mRdxBqkkWj9tFTZVL_e5nJA6jNa_nYBRKLb_E4H6Pf0U2VK45z4boytJD4FUmizIkNV4UwE_3V8J_49tcl3SfpxuXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107014" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107013">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=Lvt06zPIDVI8OGRQjwaw36KB38JczLScjB3LDAETUqWa9DVRuLKcQyfSpLP9Pvpe2wNFh_qlZ_yh2al__Dvsult0yQKVzWL-OkWB_sr7Ksu6tjb3pbyyXUnBLOvP6A1y6UUSVLt5k6rqLTp-spguWUHm7vktAnBI4MrX0frDySq2rO4r4-IkqYB5H1JclKNWFUP72PTfjgOUOvzrKiucLCBEJ8IBpsQLW2Mz_4OcrLytyPVD4cM6FpdaMOsVTTvI4ydWPYmuMQu3EieMNuU6HXbtKRvjVvFDXQNCiS89L0d4TP1RSuOpdTDADgNZUDIi7tHQJHVEHV4-7SU4T-DV1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=Lvt06zPIDVI8OGRQjwaw36KB38JczLScjB3LDAETUqWa9DVRuLKcQyfSpLP9Pvpe2wNFh_qlZ_yh2al__Dvsult0yQKVzWL-OkWB_sr7Ksu6tjb3pbyyXUnBLOvP6A1y6UUSVLt5k6rqLTp-spguWUHm7vktAnBI4MrX0frDySq2rO4r4-IkqYB5H1JclKNWFUP72PTfjgOUOvzrKiucLCBEJ8IBpsQLW2Mz_4OcrLytyPVD4cM6FpdaMOsVTTvI4ydWPYmuMQu3EieMNuU6HXbtKRvjVvFDXQNCiS89L0d4TP1RSuOpdTDADgNZUDIi7tHQJHVEHV4-7SU4T-DV1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
بهترین گل‌ دوران فرشید اسماعیلی کدام است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107013" target="_blank">📅 17:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107012">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpmBvqvFyfogkcGqC424DQ8CTBdf3gcTzwbSQi6X4LweUD_bILaMiPID-ANFmvTCS2aghhyr7mH8dbnDXooGATeU0boWWhaHkJ2a2ybLmHAepVS6Ixr3Xg9eUnNT-nRF3F6i_L379MIxpiIgAXLaaE0gQxJbKtmokC1iXRh7GYJ1cuczxHESBENcpYVOZySazRLJCBmq6iGS8Y_tRAljd3MPFQ5AKS8JoDFjQzsLmL4TOMzsseRauHjoCLsuNfQrWpeQopFEVFdRzPMfiYFTqHQPkP-2YV1XH8DdlJaD8LZmApNfEHVdf8ewLp9-n5a1-gUFfbE9wZWe13CqW4zMbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سه سرمربی آخر منچسترسیتی همشون پنج بازی اولشون تو PL رو بردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107012" target="_blank">📅 17:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107011">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=Tu-Q53BhGhPe7MBGfCBiyvKiaVdGXkWsJEZb9HJwPrZqKjNt7ApI6S1eKv2oNPUeH2XNvb6SGXwMiaU4U2xiO8AXJpaYDcVwvUJFVHGMw9q-mJZVkZf2glNwFk7266WLYVFUSlMmBz0X8O363iZ0klPd4fG4hRqHgwVPR7f33M-8_KOZOU-NwUnp7flsHQcgIfqAvwqsnLQPlsG9B1bEVC6X-X0MU1jhNUwh31W7ArbCgxT4m-ew8Jw_TOULAnPU-Y0nm3LkUvB6FRwZ3Q1Uh5QBod5wsdpRlTtOnAQLYeFM9OhfwwYJRcYgaI5-3n5aA8SP0DjspXKPZ1YCTtwWdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=Tu-Q53BhGhPe7MBGfCBiyvKiaVdGXkWsJEZb9HJwPrZqKjNt7ApI6S1eKv2oNPUeH2XNvb6SGXwMiaU4U2xiO8AXJpaYDcVwvUJFVHGMw9q-mJZVkZf2glNwFk7266WLYVFUSlMmBz0X8O363iZ0klPd4fG4hRqHgwVPR7f33M-8_KOZOU-NwUnp7flsHQcgIfqAvwqsnLQPlsG9B1bEVC6X-X0MU1jhNUwh31W7ArbCgxT4m-ew8Jw_TOULAnPU-Y0nm3LkUvB6FRwZ3Q1Uh5QBod5wsdpRlTtOnAQLYeFM9OhfwwYJRcYgaI5-3n5aA8SP0DjspXKPZ1YCTtwWdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند شروع جذاب و یک خداحافظی تلخ. این فیفا دی رو از دست ندین.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107011" target="_blank">📅 16:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107010">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
⭕️
⭕️
⭕️
🇺🇸
وزیر خزانه‌داری آمریکا: تمام شرکت‌های هواپیمایی ایرانی از ۲۳ سپتامبر فعالیت خود را در سراسر جهان متوقف خواهند کرد و از پرواز به تمامی مقاصد بین‌المللی منع خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107010" target="_blank">📅 16:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107009">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMHZ-4-okEK5CgAbka6JDl7CLJqIBzu70GjLOliSj0H2iLG9EfbKyjsd_oPjbDrs84dmA5cdr9c8vGbhBQ3cBA83UIdUpZntWSWLqjnMEWIt-aJPgPPqaibVCpUTUHYLD6R6HBpsdocbY8atR_mqYGajm0pC3eYC2rtfkYOizgCplJmMxFP0FlC38e-sNXe9zi2_SG-9HRpJbmNB5v157YF1H6GkahEV8LPg5CTGNhKTjdQcA3FckWT6N2ZvUt7wI773cnKakSIDPWd30mzx0gTmPj3YkY6lbUdcU12zLnDnUwEyl412XKD22YFpyGukx5p1zCiXOQtX9L2XvsKGEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
آمار درخشان اللهیار صیادمنش در لخ‌پوزنان لهستان که نتیجه آن عدم دعوت به تیم‌ملی بود:
🔴
۱۵ بازی؛ ۷ گل؛ ۲ پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107009" target="_blank">📅 16:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107008">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d7084572.mp4?token=YBDHMKZgLSNWHAydnTRPN7B74mJXOGWmuMPgxqnLGdopP_f2ckItU0yrFS1EzSX7C9zN3_q4Z0Ev3K81oCCJEDY6t3xeOliJJfpOOtMYD-AGRZ7JZUpNWz3UZ3VwoPxqHQbjE1Cs4PLHaM3lwBMF-4aLBEONz9UvBAnsQYbTVY90ixx53bTLmf4KJtTbQpHS0DgaDDjfH9ZmLLHw5M4nHFHGXQ6ZFKOg5-yH39oVKIUfVN7uaQ4JhNh1e2PfmBSDC-mPxy7oMHJ_HoEaue7FOkgXFxwp4Y95gfKQzkh4fXILqtVvNevDIIkO0Ht7Y8R2Iv7c5_e-_UwNX-iEGZVjIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d7084572.mp4?token=YBDHMKZgLSNWHAydnTRPN7B74mJXOGWmuMPgxqnLGdopP_f2ckItU0yrFS1EzSX7C9zN3_q4Z0Ev3K81oCCJEDY6t3xeOliJJfpOOtMYD-AGRZ7JZUpNWz3UZ3VwoPxqHQbjE1Cs4PLHaM3lwBMF-4aLBEONz9UvBAnsQYbTVY90ixx53bTLmf4KJtTbQpHS0DgaDDjfH9ZmLLHw5M4nHFHGXQ6ZFKOg5-yH39oVKIUfVN7uaQ4JhNh1e2PfmBSDC-mPxy7oMHJ_HoEaue7FOkgXFxwp4Y95gfKQzkh4fXILqtVvNevDIIkO0Ht7Y8R2Iv7c5_e-_UwNX-iEGZVjIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
افشاگری یاشار سلطانی خبرنگار: روح‌الله رضوی کشمیری، مجری جنجالی شبکه خبر ۱۷ میلیارد نفت از ایران فروخته!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107008" target="_blank">📅 16:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107007">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQYzZwk2jlMFbbK3z0BTD4EEW-VzOlJ9CBNoJxc2Zsl5zJqgeT6jKH0VBDTMfP-btwWNuE5HLp2iyHM1AQAPSkc45xIqlTK3-ZQB6TxNsS7A0c8Rf_x-qG-lggYX1AgtvsNi2dXHDRBoGfZ8Ls_qTOfMI1ZhURn-wt0sgtc6awITvuIuKt39k6eEOvplSgKtVEsWo02txn1-cmaA7mDolPy44FXDcX5fqRl81rnbmnzlcHW4a5KL2e2DgZiIjr0ApS0SCWutPOKK9Zm8d72TjXoftXZAsH1mVlH6IxMyMC5I6wlIj2vWVTfm-5Ox0elfEjirVmlsyLKmop5X0sPnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
دیدار دو اسطوره محبوب و مردمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107007" target="_blank">📅 16:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107006">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=cUlCRXgA0pDxIhWZOfAldZ2a7BLBBm1RJzbw99XnmEEu0eyVhEdcg09E2f49mk-KbeWFqJPZCTXdT2e9I3WRo9LmnthUOBNz5G-G7J-DOi34vvN4OJrVWEpMwCSj_zz-ZT-_JbhB0hOLNFguyY2aOGLjzkpneISKsVq3QXKheF5Ws260f0CvAR9dng9bDue7hyRIx-KKrDUFn6wKtvw84JGrge-BhORNLWNR_oqb7n1rXF0hjUer0q39qeUK0Hc7N9VdI6b-8L148W0hTwVDdbSnrz4BnztezkCmIsrZebfEDolk-sstp2jUE4S7y2uK7hhCPgeo0bawK6oldXsAGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=cUlCRXgA0pDxIhWZOfAldZ2a7BLBBm1RJzbw99XnmEEu0eyVhEdcg09E2f49mk-KbeWFqJPZCTXdT2e9I3WRo9LmnthUOBNz5G-G7J-DOi34vvN4OJrVWEpMwCSj_zz-ZT-_JbhB0hOLNFguyY2aOGLjzkpneISKsVq3QXKheF5Ws260f0CvAR9dng9bDue7hyRIx-KKrDUFn6wKtvw84JGrge-BhORNLWNR_oqb7n1rXF0hjUer0q39qeUK0Hc7N9VdI6b-8L148W0hTwVDdbSnrz4BnztezkCmIsrZebfEDolk-sstp2jUE4S7y2uK7hhCPgeo0bawK6oldXsAGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مانوئل نویر در بازی بایرن جلو یونیون که انگار خودش رو دروازه‌بان نمیدونه
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107006" target="_blank">📅 15:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107005">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4379faf506.mp4?token=UcKDOU7bEJHRe5FZrzHv-6iOy5ffL8yon6js0aQITBidF-dR-pOvdpd0eca_anVbiU34tERiFb3dIcX5l6qE0dV7wR8lYlMAztXZYCn4bw992KTBXMOg-wGsr_yq6oLrfRBbYnvjgMlBFSEafiliPbY2FFV5LROtuArX0Hx6-RYfRZyhrDZI25guJE9Ab-J1JubH76say1gwL7HEBCOgMRxLLvg1n32IPAQrbqQsbsrUGk-6CtBEgOCjk7Wn0el8c6ImLMLhuV316i1jX_cNCn70bsnHBFkFHb4PYPxz0dx2FMiGEUEbeaoYE5BodxAeWDpI3oBGInpxDlKG2j5a9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4379faf506.mp4?token=UcKDOU7bEJHRe5FZrzHv-6iOy5ffL8yon6js0aQITBidF-dR-pOvdpd0eca_anVbiU34tERiFb3dIcX5l6qE0dV7wR8lYlMAztXZYCn4bw992KTBXMOg-wGsr_yq6oLrfRBbYnvjgMlBFSEafiliPbY2FFV5LROtuArX0Hx6-RYfRZyhrDZI25guJE9Ab-J1JubH76say1gwL7HEBCOgMRxLLvg1n32IPAQrbqQsbsrUGk-6CtBEgOCjk7Wn0el8c6ImLMLhuV316i1jX_cNCn70bsnHBFkFHb4PYPxz0dx2FMiGEUEbeaoYE5BodxAeWDpI3oBGInpxDlKG2j5a9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تمسخر امید عالیشاه توسط مجری صداوسیما پس از فحاشی زشت خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107005" target="_blank">📅 15:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107004">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB1DQamPjO3M-gSoQPN8tTl-5ZMUW6-YzKbqxTWAjLyZF4ExBIdeZUxHn8LhJlD7HPTtH2eUjeCMHnapwlIsj9nRTVTwHthuvujm67UK5ND1-zIEJu8uPSNTZT-tfFll3FLnA_moGqV3treOS7TrHMyCAjTGXMLbREw5nVLygpSUDRFtv01IYiIM4cuiMj0ZYqyUnvFMuPvWAQGDNbfLJfT1kk1mTiWZ0yKZbjuYBVWZwdSrBhzmSGIrJKevXid9BR5GwDZgJLCE2CGhzuriUzLXhabgvYqueUaAz2GbG9qkHTqF0dg1t9N0FJdb5LTXBI2q4sKhE1HjnUXO-G5QbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107004" target="_blank">📅 14:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107003">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2bYl0sFVBIK1bTyuN13lxWVxNo3uzSluEfjYCh5Ha27E3FQW2_ZMEJxxcXmkWjMTbflEZBiMy5j67tTC_zjPVPaZcdR6fQZP42kquuX-PHF8Un1I3ytyGBGeHTyleqwG6RdGAAh2NNGUe10EM5DNCqvcua89vScF32cy8f9ZTWMf4nDHMeiazF__0NHQavNn8AgvARuaQ887OdPmvyN5ws1dKfii6AOe-1wrIk9Z3by2McOJsX7HmsTk330UkZuoRNg4hwa136-6X73rUa6qKzOL2S1ZCmVup1r95rzI3u4dC1EXAU4ITrZ88LPumt83r502d-FHx09cSUcTSo4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد تیم‌ملی اسپانیا با دلافوئنته تا سال ۲۰۳۲ میلادی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107003" target="_blank">📅 14:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107002">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=MQse0kNtRUHxIrxWvJAuZaMPyiYaUJV1JUAOd07EgDVuywbGzK3uMrN3rKSsZDVPLDh0XT6CEyZ-om0jldTpj3qf3waqk90oa7iINtakTAJJ5gCEQEjUbqOsbL-TqrfPMyP_9YC3Encj02OdStp-BiHAOeljHHaJimHMG9DXGmynxCz77sNMIG-7kWI-QvgFRrye-i8RcrDQ2ATNqbG5gAe2X7T9D9jr3kJPwLjX3sVEaIlyw7xLCJYloNS8Vnqos_r2zrJNnrnP56KPeC3KJcGi16B7fIz9-FLQHqtfX6hTwFRW7NNRgnVgmiw89BuRmG1qowWsA4bXHAQmpNu1OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=MQse0kNtRUHxIrxWvJAuZaMPyiYaUJV1JUAOd07EgDVuywbGzK3uMrN3rKSsZDVPLDh0XT6CEyZ-om0jldTpj3qf3waqk90oa7iINtakTAJJ5gCEQEjUbqOsbL-TqrfPMyP_9YC3Encj02OdStp-BiHAOeljHHaJimHMG9DXGmynxCz77sNMIG-7kWI-QvgFRrye-i8RcrDQ2ATNqbG5gAe2X7T9D9jr3kJPwLjX3sVEaIlyw7xLCJYloNS8Vnqos_r2zrJNnrnP56KPeC3KJcGi16B7fIz9-FLQHqtfX6hTwFRW7NNRgnVgmiw89BuRmG1qowWsA4bXHAQmpNu1OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
🇪🇸
بازیکنان رئال‌مادرید و زیدی‌هاشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107002" target="_blank">📅 14:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107001">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrIJyR3t6jIB3G-aLpsAGNawxlfKZjk-sogUZO7mYO6N6FXw-3J_g3rjyIxhrXfLknJtrS5wyj_2nniFMHNpu9EmcJffysg_7nAjxTrjmlR0NowdgS1gN7JllcUK6ks85zZ-D8ashQrb2EeQecieJAQZQ_o51wwUkXW0e5vNTWGLqbtwuxFqxt7DqT7us2IR5mZ53mh3A46GovELedV1iEdY8nJa_-b8fuXLG3U8K0B7uXcz5Da0xPgxyRfcc8EEYdIlOfW2upqqhFUuf4_e5ccdty7q5e5vn2-jn_-4ByDOf5jdTPlkP4p3fC3i4RXY35Qo42mlK0ueo19NA8BFsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین تعداد گل رافینیا، مسی و کریستیانو پس از گذشت ۷ هفته نخست لیگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107001" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107000">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihl82QtPnZl2uDJdKCaNOdL9VW41C0mgn79gAXaG-RYF5GVseWN062YIjc8pSicnRsZ5_RzKCOQ_aH5iFpqGqp156BCbvWj5NHK2_VjbshynvhANOOuCnUPaHs5q3pYJ7w0pBjPEbXkpqQem4wSk9kbkjroEE4TpkqpuidOTV3k5tWf4W_DqzENcm5PMXbqgvsLMgBrhtSdPE3DmpGmE4NRCDgFQPKJ8xSKnV9hvs1d4deewR8hdsaT9qiGqKzdwiZnZZS5lc0BNUfs_ZJ8huxWZSvnnFJZTmiLsi9PIJqTuTGOuMplCpLr8aa6SJmyAnzRFhH9Q3jWWK80jKO96Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107000" target="_blank">📅 13:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106999">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=CInr-UsGOO-v4zCk9kspIOjDcv5zP-yk8jAWTSAvIbdswLN8ht8uW5YWIjS-wAkMX3zJuuZt7AeFLfmgGpcqVIZ8qet0XPT1B86ASmflVGg4PWRSuMDinx6ZYu8ut-utBtguJHyk1XM_SQENR8QoUwbh_V2lqhE4KPMwyD8KpC1qt-fgzf4wmOVovIWdCztHYEFnXMC14AsimDJinzGpd9Pi8_Ne8P29Q2GvGU6VvG2eOLXP-gHuErgXJ9tw5QiI9Gl5YBKfGot3n1fP-ljh6heJLefzfLGq_LokOKlN2xlQpwtFJ-w-puHaZoW_qnAzl-UMra0AHS5Fjz2b6wmzszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=CInr-UsGOO-v4zCk9kspIOjDcv5zP-yk8jAWTSAvIbdswLN8ht8uW5YWIjS-wAkMX3zJuuZt7AeFLfmgGpcqVIZ8qet0XPT1B86ASmflVGg4PWRSuMDinx6ZYu8ut-utBtguJHyk1XM_SQENR8QoUwbh_V2lqhE4KPMwyD8KpC1qt-fgzf4wmOVovIWdCztHYEFnXMC14AsimDJinzGpd9Pi8_Ne8P29Q2GvGU6VvG2eOLXP-gHuErgXJ9tw5QiI9Gl5YBKfGot3n1fP-ljh6heJLefzfLGq_LokOKlN2xlQpwtFJ-w-puHaZoW_qnAzl-UMra0AHS5Fjz2b6wmzszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
اولین گزارش سعید زلفی در پلتفرم اینترنتی پس از جدایی از صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106999" target="_blank">📅 13:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106998">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbiUPUsBlFpz78Zu6FTUaHqs_oi6d1JmzApioVDknbRVRF1M2YRwsYFA982FBsykVYjtdqKZoR7c1lCf2Ym5plYbq_nhB1Jh1lZYILhberlpoWdgj5p0WV42wlauYo_TPugctFtsYCZ6RyZB3R00hDQeBM0RFJUdznij95MIp1XB1zCtqaOsel350780wPJp2-WY87uEnaLvLBjWmu6KKW3y4h8HrOzJBCmbkBaZ6nWiimjlriXveR8AqKojQxPq6o1IrM7qxw89wlWJXFNfnhk2EPsiyK1Rrn8jqIDxRkQFudSdwTYEbXbBJiektdSn9xByTweKu-kPy1jcHOuutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔴
اینو حتماً تو اینستاگرامتون فعال کنید!
برید:
Settings → Data usage and media quality → Data Saver
با فعال کردنش، اینستاگرام مصرف اینترنت کمتری برای لود عکس و ویدیو داره یه تنظیم کوچیکه، ولی اگه زیاد اینستا می‌رید، تو مصرف حجمتون حسابی اثر می‌ذاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106998" target="_blank">📅 13:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106997">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApoP_m3LQ0gAIDJcdju3j8inYXvGcF3jPvArNxluV95lUxXGZ0GA-BcjX0H88L56rQGCFRHdniaGgNPGpIqEz8vukWITSziVWKWmXjhqIqYwqPn8tNuQ_Jf5J4zCzDGk10hUYQKRTatwuGmawzbF3MpQhUaQnOHgCIZ4F8YskwR3c6F6cwdupNPB883APeYzBcpZ2Tgj3v6jKNO8t4z1s9jHdPTfCD_m434ZbeKSfJi5GHTDHnOUNVP5FVN0yr9EPZvjl8kAGHfk729UkBje0o7mTOMPqdG5FJZeLwV_LLr1LO-QzuYjyfzA7yVEHrdqThDiRMawC3_wVNQkyAYGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🙂
استاد گودرزی
: متاسفانه پارسال نزاشتن پیاده تا آرامگاه کوروش بزرگ برم؛ اما امسال دیگه میرم
هموطن راه در جهان یکیست و آن راه راستیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106997" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106996">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=UVwRXNmFgOvXRA1xp2EaGcXjWMlFor8N17GA1ph3AyfbHsdHWAmm4dX4slo7f2A-g_kdqoLQRWm178WzPDOlsh4CH0uahI3Cf8nT4NHJRZtAw9oN57kGBgvCO381lkfub4hoi-XHNL5a95KPEsz4bz2-QutEvtDtD91qtlwOCs69slAVs_LOXRWquCZsmJzGBI4EfWJl6z8hkziKZuR2nx0oFlc0dLz2zyLt9xOn4lHT0JLeWbJBAnQSXR_soois9gF41FP4ow_AZ5VRHvHks--2eq7OMGXs8SRbJUZ8XoHxD-8BafDR-bp-75aIchfP2ZYotQYK7fZ0cFzUevapVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=UVwRXNmFgOvXRA1xp2EaGcXjWMlFor8N17GA1ph3AyfbHsdHWAmm4dX4slo7f2A-g_kdqoLQRWm178WzPDOlsh4CH0uahI3Cf8nT4NHJRZtAw9oN57kGBgvCO381lkfub4hoi-XHNL5a95KPEsz4bz2-QutEvtDtD91qtlwOCs69slAVs_LOXRWquCZsmJzGBI4EfWJl6z8hkziKZuR2nx0oFlc0dLz2zyLt9xOn4lHT0JLeWbJBAnQSXR_soois9gF41FP4ow_AZ5VRHvHks--2eq7OMGXs8SRbJUZ8XoHxD-8BafDR-bp-75aIchfP2ZYotQYK7fZ0cFzUevapVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
لامین‌یامال از مدعیان اصلی توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106996" target="_blank">📅 12:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106995">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwO24HoCa7O27jeOjj2U3qWL_XTcdbDzWNVkED4a7zaAHjHim6bY_Ir_hPc3LayLq9KlXQFcrAw_Nlr4NP6cfdXZ8napUlpRSKcXe9Q2Cmq6DjXlA1Ke1xPeMU8PuLE2yg4NXnpnGm3hcW_Nu2auTiA3q0l_tNZPmRgMrZdHtroqg_8RD4sUChrUZrVe02oUMPxq4KvdH-UKsH_Hs7Hbp1UQX5_ivgDaeD20NJbOZbU7_2tayT968mNWnSGCpzPiFaYNaB7DTeXYQse22gl8sazMkG2a_MJhPpR-QPGR2sLj88rONLr--RgIVSUg3lRULMya338_KhC7sbLjuH6oiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106995" target="_blank">📅 12:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106994">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp5-1z0oXn-q1H2AB6h-w6XvJbwe3V09kHJCllkX0W-sh1Rf8SxABUCT61xFUBO9jsBMJ3ZGm_O9X7M-SI8HkJnFmWY-bKW1c2VXcEATXrE8unS4UbdbeUKYKQx39YDdCs-3SdlZqsVT-iXcDRwhv_lhpA2GiP965NLnTW5U1Hsz28LiRNd8s0y--vH8hGKoKaPycSDfiqqnWW9Bt8bNsVIIGcgONoX2X5NckhQAgKTX1jkOwKYSiwQ9SB03pbihJ7vTYWAtx5Wcro_8WWvD4Uc6-45TBoZ_ihoyQk8lXxL93r9gyLJCmpj1Z7mO7wJte798w4lpC4Pdl74sZEoK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫡
🔥
بهترین بازیکن فعلی فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106994" target="_blank">📅 12:20 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
