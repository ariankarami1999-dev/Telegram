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
<img src="https://cdn5.telesco.pe/file/P7d3I4BfVc4-z4L2DbTxHzOvCbUhT6qNkFKwqeDNubdIa5dhdKQO08tJQ1of4jDANZ1Cw69muWnxa0rLcrhaR2dHgegKlEls6qNrnl7H17nvPDtdm_AUOnIysT9Ic_EV2WFlUiFHzkmULJXfCPJ26pflSnEcBNFOKAnGsg-kY0waXla298CkIvmheai2D3M1K9qsyip7Yz5_lJfo9uM4XDrsP97xlwbZAu3H0wLjO_lSeI1dh45DmprN-nIw_wdJDbLeRS4soLzPdIiI11GxR77AbIXRPCQOJ9BdSnYao07NffWbavaYJA0uv9FWsQZ6PPSOdgtjGL8AlYHDdPekQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 462K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 14:47:03</div>
<hr>

<div class="tg-post" id="msg-103961">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQsv5_CqAPUAZ7H_n77jaw8C_R_gz-EWkNWh-JYMYoBHuCbTZ6Zy242vZHoxt34gzbWBKU7S6q9eCKYQw4wbnBCM8GruqY2l8Po-UnchLi-PWAc6gHzPggJOjuMEC4isl-GuFuzOLe0ShbfQu6kEc2G1Blg4pxT7c6rltHht_xHS8RhHSDRVUKzqvwCWHtwyHQYmsRg5DNmXkwKGLAWMEy-9UjHNGHgnWFNRyHbvl77qv1MZDnitDohtO5hZ7DwqEUqKhI8oThUlqtl-KVyryVy70U3DOzM9-vhW0dYZY1lE1ymEYmdI1lkbvqxEgT2gGYKm6Eps7Dfmer55RGAZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
👍
آغوش صمیمی کوین‌دیبروینه و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/103961" target="_blank">📅 14:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103960">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLh_uO5SKRwV5O9CP_j_vtwnfPpnpoiSgOY49leKldo21K8v0c2X88Uvhi-PEFVdlAX_4uw20lEsm7v2uneyU2eFqVxEEpcp_oDHvtCz2et3_aLB7EcuL3DIk_PwlI8hNNO8Dag0ocd34EQLPIThkTl-EAGsbuSizWoMghN8I7quNWHjamoVElEgLiEiclLTe_lxsccqdZGeGyncLWw18JJjyRa_1UJ9vTvEV-340uN1KhhI_dPsp_xkxyn0SvUCg3QchHBG6Nml3o_Q9z0GH29JfuOwJBlO7cWUyIeOJ5MbW26rlwBYyFIImwuZadySfzxLS87ZsQhCz4KXS7vgQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
افسانه، کریستیانو رونالدو، در مصاحبه‌ای با مجله ووگ درباره آینده‌اش صحبت کرد:
🔻
"کارها و فعالیت‌های زیادی در پیش دارم که به قدری زیاد هستند که نمی‌توانم فقط یک مورد را به شما بگویم. من برای همه چیز برنامه‌ریزی کرده‌ام."
🔻
"وقتی بازیکنان فوتبال از میادین خداحافظی می‌کنند، ممکن است یک خلأ بزرگ ایجاد شود، و شما باید وقت خود را با فعالیت‌های مختلف و برنامه‌ریزی‌شده پر کنید... نه فقط یک فعالیت."
🔻
"من آماده‌ام که بیشتر لذت ببرم، بیشتر سفر کنم و ورزش پدل را که خیلی دوست دارم، تماشا و بازی کنم. بنابراین، می‌خواهم به لذت بردن از دستاوردهایم ادامه دهم... و از دستاوردهایی که با هم به دست آوردیم. زیرا این ۲۵ سال، پر از فداکاری‌های روزمره بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/103960" target="_blank">📅 14:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103959">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34552c022.mp4?token=vX0N99tdY2U1eabZSfbv3ldcenrgKtINJWBwbDWtjHTjlbdlhOu0obDL-m0S2gwtq26Iav6M6sAV2_3TB7cAaDRHLgjipfN_ug_1htUJBpn0u6cn-cl8QMPYWqcY1SG_EvV6Yc4Qm1mh8KsWOVcm3Mfe_6wGBwV9e7RMrthB_qtjiSmSEtvzSyMmfsl3zD-I9YiIk4xT321yZMYDnHHhMX7FoImF4XZu3VfVC7QV5Plslf6Af8HSy_yaoQqfU01yvIGMG6BKAaC-zMlUkGBaYh2M_sZ9-pfFLIxqOqD6cP2FXAYHtHK8Hpq4qieLfyVEFbaFE1lrvwpvCe8fpyPQdQx1u-0EUwgAwR60bv8QQSmL1eyXZjCYnqJ0eapUU1vPyaP0J3YOBw5nPCPcDZx1PZRRCQ2t79cGSwokECERzP03AFbHhFrBT6u9tF9RKZuGoH9aFX65ZMKwdBKmfSVXCKT_fVZPO0cxFXXTwGTyXrV4xQiq9LnSHiNp2RxqsOaAWH-PSg45dssIWKxiNmb1Om9jgNuWI1SqjcZoW-UWHLghkQeeojjb2irA2kFHyha0MWuA58r2JLSWKf590aFXFnfF-MgoSllnXscnODZ5FBsJq4sLsfGbs1VrEKscDndND5dEESQlK37MzW2KM5Mz1GdJ9lduwhZhGixcI7vRW4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34552c022.mp4?token=vX0N99tdY2U1eabZSfbv3ldcenrgKtINJWBwbDWtjHTjlbdlhOu0obDL-m0S2gwtq26Iav6M6sAV2_3TB7cAaDRHLgjipfN_ug_1htUJBpn0u6cn-cl8QMPYWqcY1SG_EvV6Yc4Qm1mh8KsWOVcm3Mfe_6wGBwV9e7RMrthB_qtjiSmSEtvzSyMmfsl3zD-I9YiIk4xT321yZMYDnHHhMX7FoImF4XZu3VfVC7QV5Plslf6Af8HSy_yaoQqfU01yvIGMG6BKAaC-zMlUkGBaYh2M_sZ9-pfFLIxqOqD6cP2FXAYHtHK8Hpq4qieLfyVEFbaFE1lrvwpvCe8fpyPQdQx1u-0EUwgAwR60bv8QQSmL1eyXZjCYnqJ0eapUU1vPyaP0J3YOBw5nPCPcDZx1PZRRCQ2t79cGSwokECERzP03AFbHhFrBT6u9tF9RKZuGoH9aFX65ZMKwdBKmfSVXCKT_fVZPO0cxFXXTwGTyXrV4xQiq9LnSHiNp2RxqsOaAWH-PSg45dssIWKxiNmb1Om9jgNuWI1SqjcZoW-UWHLghkQeeojjb2irA2kFHyha0MWuA58r2JLSWKf590aFXFnfF-MgoSllnXscnODZ5FBsJq4sLsfGbs1VrEKscDndND5dEESQlK37MzW2KM5Mz1GdJ9lduwhZhGixcI7vRW4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
۵ گل‌بخودی عجیب تاریخ لیگ‌برتر ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/103959" target="_blank">📅 13:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103958">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d709f3b074.mp4?token=Qu4lXxMFUe4vFNXUSx5MNB-YlSMIFkWktFIFwr6B0KAvffKP20Fr5-wZQGAdsLX2q9PiaVMgVpKbvyykd4o3Rugo3WfLmZ2H88i52CEZrbwjSgbrbh2TKE2TdK4uNhzgJkbXbJOulqTbbmkCOOjzFl71x891YAITBA1HQGr43QZguj2Eu16kMHhP7Ewx-vjiOn9v8hHKE4Xe6_fniWmWMndN4WO8eK05HIQ1nBWGe75DQIO1qdApzw-l1zXQ96FhEXTetdZh4XmMZKMQUO9Tc30TS3RmNnhYcEuMlOO4iojinCzmZ0H6QMV9xxeMt6LFBMknF4INFIU6pGa3nwdNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d709f3b074.mp4?token=Qu4lXxMFUe4vFNXUSx5MNB-YlSMIFkWktFIFwr6B0KAvffKP20Fr5-wZQGAdsLX2q9PiaVMgVpKbvyykd4o3Rugo3WfLmZ2H88i52CEZrbwjSgbrbh2TKE2TdK4uNhzgJkbXbJOulqTbbmkCOOjzFl71x891YAITBA1HQGr43QZguj2Eu16kMHhP7Ewx-vjiOn9v8hHKE4Xe6_fniWmWMndN4WO8eK05HIQ1nBWGe75DQIO1qdApzw-l1zXQ96FhEXTetdZh4XmMZKMQUO9Tc30TS3RmNnhYcEuMlOO4iojinCzmZ0H6QMV9xxeMt6LFBMknF4INFIU6pGa3nwdNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
بررسی واكنش‌های جنجالی به خوش و بش بازيكنان پرسپوليس با داور بازى پرسپوليس و شمس آذر دكتر بيژن حيدرى⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/103958" target="_blank">📅 13:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103957">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAQQlfkluXsE8tl8Uqd9wE83va4Lpf-N1w12pTlTGY0R8kCzZsyyiMv04wDLF9MWZ2PFrwMw6djCFqm2lRmxXygeN3w3KX5-_VBAPtSyU-EzklAoMHcchPRUXXoo6w-HUFxdeNEXA_ki68LrFlf-lYX0tgRETHbxIt29LSyYVMgank6cPKTZDsMF_LBZ4nT44fl_g2Q9boJte_BsmLpIMDSkaM-jueOC_PlkTdzLJlSKGXPe_xwZbgoM84qE2joeq6HGG2_eaOt-QYkC9sOGwx61yE32B-B9i1VeVCIq_4h7fQaacbMtCRFb4Nq3xeq9zcbKyPF73ngKO9LyTrNLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین بازیکنان یک‌دهه اخیر لالیگا در هرفصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/103957" target="_blank">📅 12:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103956">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHm6fElWLKZSrPy4LnObSdo7J8omoco6UPUav3T3QYeL575YWEgJ7UvUD5SoD_RxVRXbeBG3F_0Kf2shZsIhUfceiftg1lnWgtL_Pl4LRErRyFtRwjIywZrky6irJpyW44o8Gf_Jfcm9fLqFlhfdV88zoDUjrMk05JfB1pj-YdAqB3jH51Kx41kYvvcjWllEgdpqSomk7jOtWigcljbzjzIt0ogHtWbOvC1uhf_MnV9QQu0CVuXYDfNrGEVLg9YTA4yE8yyKMgSxLRlvBZIa3g-Ip6-YaU7aoWreW0Mb7G75nLEIuqPLe3cc6keQ73wcv0Mt1VMhqtTt8yVf6RuACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامه فسخ دوم یاسر آسانی با استقلال رونمایی شد
نامه رسمی فسخ قرارداد یاسر آسانی با استقلال منتشر شد. بر اساس این نامه، این بازیکن پس از پایان مهلت تعیین‌شده برای پرداخت مطالباتش، قرارداد خود با باشگاه استقلال را به‌صورت یک‌طرفه و با ادعای «دلیل موجه» فسخ کرده است.
همچنین پرونده آسانی در پنل فیفا ثبت شده و شکایت او علیه استقلال در جریان است. آسانی در این پرونده مبلغ ۱.۶۵ میلیون دلار به‌عنوان مطالبات و غرامت درخواست کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/103956" target="_blank">📅 12:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103955">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇪🇸
🤯
پشماتون فر بخوره که رئال‌مادرید حدود ۲۰۰ میلیون یورو از فروش بازیکنان ذخیره خودش در فصل‌گذشته تونسته درآمد کسب کنه!!
💸
60 میلیون یورو از انتقال نیکو باز
💸
40 میلیون یورو از انتقال گارسیا به فولام
💸
20 میلیون یورو از انتقال ویکتور مونوز به لیورپول
💸
15 میلیون یورو از انتقال ماریو به میلان
💸
15 میلیون یورو از انتقال رودریگز به بورنموث
💸
12.5 میلیون یورو از انتقال خیمنز به بورنموث
💸
10 میلیون یورو برای انتقال پالاسیوس به فولام
💸
10 میلیون یورو برای انتقال اورتگا به استراسبورگ
💸
8 میلیون یورو از انتقال ویکتور به فیورنتینا
💸
4 میلیون یورو از انتقال گارسیا به بتیس
💸
3.5 میلیون یورو از انتقال مارتین به ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/103955" target="_blank">📅 12:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103954">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVibQqUuILAefmgYyN9-adXGGjMsAZTCfSdIC-bUuF6Dg8jEOe8OgoNTiTQCNswa3DNDxLxEskThXRwuRduGboQPWFQavibHPE16TLR8RhIdfYksPcLHoZC5ozBgkCOwHJgzmDWJhHwanOiARS5iHPTk81iolC1W-FhQt0ZhzNkC9yexqVgF4R1IKeFus0JCSGZBw00H9RTIFotIbaGqfzUAy-GBDu2mQYJNRRXujXL2RqzveNDVF2Ux99wMS8jMOZFoBrTcRg22bq-nCkLJrA7DolOwiFnpcHS03-bo5si9ucyKpfRV2N6MOmNRdOX4YmPYQMcFijK-7NLshT3p4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر تماشایی باشگاه استقلال برای تقابل فرداشب با نساجی مازندران در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/103954" target="_blank">📅 12:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103953">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908dffe6e9.mp4?token=XJLS1iqTHOGwQk83g9ewh75adNNHEFTk1_q7yDgFXRnsEBIuKmY2nvwr-0fYA4cL7ZWYJe0YXrHDyuOe3BfzO_8550R639LbNbDAHU5100WS0PHoVmmCqHI9EHhZBdSFLzuCKQGSWagmTEJt3KK3ne3m2PXjxWNe-IeUr6EyvKWd3Qm4v_6kdromrZq6YOsEsUw0uKaHtxiyhn3I6xPBuR3qdR-Jx0d7wSVkyJYBXXJ-6TW95F_-IyY2zvAxL_HjMLYZHcojtUSWEin7C0Rmsz0uncEus4vXIF3D-vEVw27I1ZG3qGFow4r7GGwle0ujqY6PYi_6Tw0VT1Xuk7NRDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908dffe6e9.mp4?token=XJLS1iqTHOGwQk83g9ewh75adNNHEFTk1_q7yDgFXRnsEBIuKmY2nvwr-0fYA4cL7ZWYJe0YXrHDyuOe3BfzO_8550R639LbNbDAHU5100WS0PHoVmmCqHI9EHhZBdSFLzuCKQGSWagmTEJt3KK3ne3m2PXjxWNe-IeUr6EyvKWd3Qm4v_6kdromrZq6YOsEsUw0uKaHtxiyhn3I6xPBuR3qdR-Jx0d7wSVkyJYBXXJ-6TW95F_-IyY2zvAxL_HjMLYZHcojtUSWEin7C0Rmsz0uncEus4vXIF3D-vEVw27I1ZG3qGFow4r7GGwle0ujqY6PYi_6Tw0VT1Xuk7NRDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇮🇷
سهراب بختیاری‌زاده برای اینکه ریز برا استقلالیا بماله از مصاحبه‌های فرهاد مجیدی مایه میذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/103953" target="_blank">📅 12:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103952">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9760c12668.mp4?token=s-voo9uuV60_iaOclKGICapu7GQGxEvjDYgvHuM1FcUc73aaoXFpwEBN7QhwqfCM_HRNzP2mw6StnaEPN6zyi9hV-Or_RUN2JKW3D4rT6y6HkbxZfB-CU296_uiOs1B3SnDmum3dadGOzidoHKsgBFlJQ8pLm1OkhM8h_LaJkt2J3u5Am7_sv_a4S24q7OjgvcUprHmOFxbtxz24YdCtdEFOqKbE4y51LUFFY90bQh9TU7Eix5fsjY59IF60L2rOcv23r9Pa6gJoZowYgBP-sgCwlD-tpKG8BXC0KwY4imTAcOsYTEtxkWLS0M04r9PKLgiyqYMse0QowGdpl9fHEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9760c12668.mp4?token=s-voo9uuV60_iaOclKGICapu7GQGxEvjDYgvHuM1FcUc73aaoXFpwEBN7QhwqfCM_HRNzP2mw6StnaEPN6zyi9hV-Or_RUN2JKW3D4rT6y6HkbxZfB-CU296_uiOs1B3SnDmum3dadGOzidoHKsgBFlJQ8pLm1OkhM8h_LaJkt2J3u5Am7_sv_a4S24q7OjgvcUprHmOFxbtxz24YdCtdEFOqKbE4y51LUFFY90bQh9TU7Eix5fsjY59IF60L2rOcv23r9Pa6gJoZowYgBP-sgCwlD-tpKG8BXC0KwY4imTAcOsYTEtxkWLS0M04r9PKLgiyqYMse0QowGdpl9fHEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
تاجرنیا: اینکه من نتوانستم پنجره را باز کنم ربطی به کم‌توجهی من به تیم فوتبال استقلال ندارد
انتقادات نباید طوری باشد که من از کارهای خوبم در استقلال پشیمان شوم.
وکیل به من امید داد و من هم به هواداران. حالا اینکه پنجره باز نشده مقصر من نیستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/103952" target="_blank">📅 12:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103951">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eecbdca57.mp4?token=cDU3rfnZirjSxvv7vU4oLJnrj6z1twl6DeVgmZaMjxeeeXwHpTVIKKhA3j-dykHydZ8JK2l_TJPRgb6-q1VjaNri2UYOtXIxQidDp5RFbeqk6j1i53uf6TOM1v4jU6LT9Vx5hUCHZRX2AmaqofKwIB0G5Ys7T2WWdWfJBlWXSn3YS9D5dkra_nXj12VKn8v19GLVQpd-z-wuP0tl0bk8JBMaeHXiMOQoN4lrbjW1qikdpdAUVKFtXNBYlcwH6BO6z4JTEshJf9D5dDptmFqE4Wg9vh3ED03bWfRccmU49sDetIrJ7wuw2cnu_phpwYBTwxVEK-8rirOGGdOTbrVdkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eecbdca57.mp4?token=cDU3rfnZirjSxvv7vU4oLJnrj6z1twl6DeVgmZaMjxeeeXwHpTVIKKhA3j-dykHydZ8JK2l_TJPRgb6-q1VjaNri2UYOtXIxQidDp5RFbeqk6j1i53uf6TOM1v4jU6LT9Vx5hUCHZRX2AmaqofKwIB0G5Ys7T2WWdWfJBlWXSn3YS9D5dkra_nXj12VKn8v19GLVQpd-z-wuP0tl0bk8JBMaeHXiMOQoN4lrbjW1qikdpdAUVKFtXNBYlcwH6BO6z4JTEshJf9D5dDptmFqE4Wg9vh3ED03bWfRccmU49sDetIrJ7wuw2cnu_phpwYBTwxVEK-8rirOGGdOTbrVdkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مارسکا بعد از شکست مقابل آرسنال: "من در کل همیشه نگرانم، حتی وقتی بازی‌ها رو می‌بریم؛ حالا تصور کن الان که بازی رو نبردیم چطوری‌ام."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/103951" target="_blank">📅 11:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103950">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ba20e0a3.mp4?token=BiTRHlBpWZv1X9FpZOtn_PnR9qgbvOVQgzDwmk4MKVuS0Z7Qb_eoQeTVGJj-pU6Im-_dUWQM2g2AoX7nzn0sBArsB7UO_5q7tQullLAa1FrYg7E9FJ0hOdLFrweTHUdpGKIOI039aWq2qoN2OCgnHn6sbv5jKGyTqbIV3gg6b9CuLQ_gX6q4v8z1-Dvm5no1_05RMRAutqiHCR_wyZDAJCln8kTwkyFkUTcoFbBWgA8RSBz8-EIU1Nun7buzEx-MhAG9IXH5xsjVqYP7gfRoYL40EA8h93ZU-NlgRKEraApHNbgwUp1fQmW6t7hbygJkfqBTqmYoi-PMLIIqvdbnb79iD6zT9pRo1Q_aTriUd-n5hWKIzWaYBAKVMmvBGkwjonB58jmrwvWKI4tN_uxBwaFc64Qas7_IuAFiydfnQDk76_RJJUV4DHid0OYfjb3ZeozdYtCcJ3msnxPg8yVqFCfDEoTLbHyzojOC8uc6iuOcLQRKNVj_LbuNYPk25Zer0U1lACw_T9HUWQTPAJayZSEY6L81nICm3Lj8L8yt7b4yPWNJVfU8wR-sPgxnHnEDS1p8BHnVwLo3gBTN7qfCRx_3DymiqC4gkNIF-PNOUuBLbwmXf5nDLFba0nVUmaBfQoW3ji-PqDceLIQ2VJTf4TuvtFqUn_S2m-SQsbAxVDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ba20e0a3.mp4?token=BiTRHlBpWZv1X9FpZOtn_PnR9qgbvOVQgzDwmk4MKVuS0Z7Qb_eoQeTVGJj-pU6Im-_dUWQM2g2AoX7nzn0sBArsB7UO_5q7tQullLAa1FrYg7E9FJ0hOdLFrweTHUdpGKIOI039aWq2qoN2OCgnHn6sbv5jKGyTqbIV3gg6b9CuLQ_gX6q4v8z1-Dvm5no1_05RMRAutqiHCR_wyZDAJCln8kTwkyFkUTcoFbBWgA8RSBz8-EIU1Nun7buzEx-MhAG9IXH5xsjVqYP7gfRoYL40EA8h93ZU-NlgRKEraApHNbgwUp1fQmW6t7hbygJkfqBTqmYoi-PMLIIqvdbnb79iD6zT9pRo1Q_aTriUd-n5hWKIzWaYBAKVMmvBGkwjonB58jmrwvWKI4tN_uxBwaFc64Qas7_IuAFiydfnQDk76_RJJUV4DHid0OYfjb3ZeozdYtCcJ3msnxPg8yVqFCfDEoTLbHyzojOC8uc6iuOcLQRKNVj_LbuNYPk25Zer0U1lACw_T9HUWQTPAJayZSEY6L81nICm3Lj8L8yt7b4yPWNJVfU8wR-sPgxnHnEDS1p8BHnVwLo3gBTN7qfCRx_3DymiqC4gkNIF-PNOUuBLbwmXf5nDLFba0nVUmaBfQoW3ji-PqDceLIQ2VJTf4TuvtFqUn_S2m-SQsbAxVDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خداداد عزیزی: زندگی خیلی سختی رو گذروندم. با پدرم گچکاری میرفتم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103950" target="_blank">📅 11:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103949">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9244a473.mp4?token=InVKfH_av7CQfuGa2QBnuMXQBcJMoTVFTpvMQ9PlPGRN3tWtRVriGDblIc62rtA0mtgTB04kOW3bg--5yBU7L3aVdJpDwVUeOwbuUnZlnx1R3inN7wgfKUfsQbm0ExeAxMg0e2ACgDXUAtMACvmRvlGu2ciyzil-BO240uwg_Sg_lPuPU3nNe5HLc9JfC1BM9kOYS_V9EMLr1l6oScXofSgazUCNZDtrG4db4DK-2GRE1mGpkI0Pm3T64rr-8bUEAe08szULRndhZe4ihkOxQ2CJdvxTalVkxnNRn25nEzg8OAWKlpDpfdKppLEZPqmeTDbmR6mugImMcVmW2Cw00A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9244a473.mp4?token=InVKfH_av7CQfuGa2QBnuMXQBcJMoTVFTpvMQ9PlPGRN3tWtRVriGDblIc62rtA0mtgTB04kOW3bg--5yBU7L3aVdJpDwVUeOwbuUnZlnx1R3inN7wgfKUfsQbm0ExeAxMg0e2ACgDXUAtMACvmRvlGu2ciyzil-BO240uwg_Sg_lPuPU3nNe5HLc9JfC1BM9kOYS_V9EMLr1l6oScXofSgazUCNZDtrG4db4DK-2GRE1mGpkI0Pm3T64rr-8bUEAe08szULRndhZe4ihkOxQ2CJdvxTalVkxnNRn25nEzg8OAWKlpDpfdKppLEZPqmeTDbmR6mugImMcVmW2Cw00A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✅
🇫🇷
هوادارای دیژون تو لیگ 2 فرانسه از این به بعد جای بلیت کاغذی باید شال با خودشون به ورزشگاه ببرن، تو هر شال یه تراشه الکتریکی وجود داره که حکم بلیت رو داره
تو پریمیرلیگ ایران هم تماشاگران از در و دیوار باید وارد ورزشگاه بشن تا هرکسی بتونه صندلی بهتری بشینه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/103949" target="_blank">📅 11:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103948">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c1acd77e.mp4?token=kMGHo2hFbpFE3l43efAU6plg5k2cCYp9xzjR7GWwDA-SWuMLPxRsNToegdJ91WzaWV5AxyS52F3DLMJZpAUTNKd_mWtsMUCA6ST-c0P9LJReUC5-l6CtvPwgUt-UneYaRTMIeARamy8ATiwk1-qA8x8zYZ08xiry2lHDSKErrC9ewHaugWTgLt9ugEOZfVotPZoqvO_cs0rAJbysVoOy4Y1bCwehj-ZSxF90UXn3io7s6iz3sY91sz3ltbT8quK9n41NbpG5Pa4RPoQ-cWqAiN53KyNjKbaj4ExJlRzuKZjcJlm3A0X6RYJStF-ImSYIsTbkGIEEKIQSFq4ct6CLCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c1acd77e.mp4?token=kMGHo2hFbpFE3l43efAU6plg5k2cCYp9xzjR7GWwDA-SWuMLPxRsNToegdJ91WzaWV5AxyS52F3DLMJZpAUTNKd_mWtsMUCA6ST-c0P9LJReUC5-l6CtvPwgUt-UneYaRTMIeARamy8ATiwk1-qA8x8zYZ08xiry2lHDSKErrC9ewHaugWTgLt9ugEOZfVotPZoqvO_cs0rAJbysVoOy4Y1bCwehj-ZSxF90UXn3io7s6iz3sY91sz3ltbT8quK9n41NbpG5Pa4RPoQ-cWqAiN53KyNjKbaj4ExJlRzuKZjcJlm3A0X6RYJStF-ImSYIsTbkGIEEKIQSFq4ct6CLCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تاکتیک جالب دیروز آرسنال مقابل سیتیزن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/103948" target="_blank">📅 11:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103947">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103947" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/103947" target="_blank">📅 11:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103946">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJYjiML1DAeLFbhJ7tTosCVo84DbwE5BA8Nn09MbHyQqHnYNFRA_1WSF7GEcCRSGv26LudbKKmF1-1wJnn77zZd0Ht-p_c8ATcG0_vL1A2EOg_Q6KBCHmz3Gs9ygjtGPQkMGuKw21yYyKDdqGpWfYD_gffiJN28oaTFX2PglksTB-IwxD789g_FC3p-JiGJLQQ5NhEc7wz6JbkJj7AfMUh9cVNlkys0K6IB6TW2_kb4nkjun_32_tdIYc71ezj_7WBIwnjRDNrIKg3aF24BrAx6BEnFR0-71yjnt3dexIxEJiCRrgKibMinrjpw51prLKU_vrj7iSzgpjMZuTsJwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r26
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/103946" target="_blank">📅 11:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103945">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1OsF0Kr4ODpd-NR-BMhwyqhPArqROjMrdTwFEox45I3G_UrN6KiURez-LdpRg3_H9FXpx4NIIqlbZnM6YNE1ZEAvCu4IH2mRVY8ik85_VQ36uGa6lIrwvDtM-R51YK9If9422fTFmtKU0mkxpbWordyi22vEdbqXXleqRCdvQwJMrcWX6hW7ElNqpVbwKZW5LQZONZQrMnSylKW9TMYwdHkv-PU_nqw2glP93gxFkIwYcxrZJpyp6lqiM1Y3BZYcDa5h4bkzjudws6mTERNUcpggLSlXHpxr8yFEu76bLqhAIKr7ICplFf8vmySMSo1F9uWTOd9PP6x8ul_LK4Qyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
رومانو: ویکاریو سنگربان تاتنهام به یوونتوس با قرارداد قرضی بدون بند خرید اجباری
HERE WE GO
✅
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/103945" target="_blank">📅 11:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103944">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f807afbf18.mp4?token=po6OjW6DWLple3ccMvGlty6lNk2xdX9riJhnqzwtUOB8oeXBC6sQc2I8fpmc6WeuDxucxxOrBypLXdxDzs651JU3p44xHPeVy2LoCeSXPRaoK7gkX5n8seMhayLEHQ0dC8NXPTeoMisoOGLGwuZgFY3ah7Alkt92ay3SwvZbFd-L6bb45FyCh5f-gTQUlSZ5hQt259lX5QPQ35oolNHT-LVY1c6BIDI6EKh05yL9H9obFn8fRjAKOm3qx4X6gqWt4pYZEFT5nlBEA1RCQ_eH-hddBwiLoPLb7LIRtWKPBHZg7wTGL0SOrwA-m3aUmQUrU2jaSFeiy3dKTOwYdSJC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f807afbf18.mp4?token=po6OjW6DWLple3ccMvGlty6lNk2xdX9riJhnqzwtUOB8oeXBC6sQc2I8fpmc6WeuDxucxxOrBypLXdxDzs651JU3p44xHPeVy2LoCeSXPRaoK7gkX5n8seMhayLEHQ0dC8NXPTeoMisoOGLGwuZgFY3ah7Alkt92ay3SwvZbFd-L6bb45FyCh5f-gTQUlSZ5hQt259lX5QPQ35oolNHT-LVY1c6BIDI6EKh05yL9H9obFn8fRjAKOm3qx4X6gqWt4pYZEFT5nlBEA1RCQ_eH-hddBwiLoPLb7LIRtWKPBHZg7wTGL0SOrwA-m3aUmQUrU2jaSFeiy3dKTOwYdSJC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚠️
‼️
دختره همچنان دست بردار رامین‌ رضاییان نیست: رامین‌رضاییان ازم خواست که عکسای لختی بدم بهش. دقیقا میخواست مشابه کارایی که جفری اپستین انجام می‌داد!! درخواست سکس با دوستام رو هم داشت! دعوتم کرد که باهاش برم پارتی و این چیزا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/103944" target="_blank">📅 11:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103943">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCI9shVgECh4hpPl8ntESndC79MMXoPnh5uUYOLYuaHTYi1taMNJhrNMtnmJEK0ElKROZXEw9-JWVUJ-_z6S8nLxK6gMu0CEiLQsweL4_dfj0sDLqE-t9PHu0_GvreG-FRJ_CZF4KKvzHpTIixrvpsKpriXrr5CysEsArTJjtsBu16L-XVfSMfTd0-RukjNfLyLOV-oVlyS_8Jo3UzeXGBOhXLAc_RGi4moxXligqJAkV-44l78MJ1T7LSZZVGXCaHClLx2qqRsB_HPiSxJ0rY4rtDTae1hwJeeGdu7V7wOyI9yLNcyqJ1Z6bVRUg0gQh9LOi6GtEn6aVswpzsDyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از شبکه الچرینگیتو: بارسلونا میخواد برای جذب گیوکرش از آرسنال اقدام کنه! گیوکرش گزینه جانشین فران‌تورس هست و هدف اصلی بارسلونا همچنان جذب خولیان آلوارزه
👀
❌
برخی منابع از معاوضه این بازیکن با ژول‌کونده خبر میدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/103943" target="_blank">📅 10:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103942">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2151ad88d8.mp4?token=ticsQ72IV-A4CD3fAlwRzflj0pPMzFt5b6_be7wBwB3AvX9sRRJ13SguDb5M3yl7q43w4GN2AXCdbjIFu9WO19D5k5GoAP8m-6-n27wLinQq6xj9qd8ELv5HzWA8OZAVo7XbTB0l_3zjGpBN5SvLqJuMYX1RVg6KttcZ3Ui9DM7fMkpEahtf3V8L-_h5pQggK_Do1aXKr7Rim4UX0GHjF3tf4_91GHGG-oncaefAW_CdR3fFUxEZcYly1FRY29TGn8olF8XwWG9C8bP7kuX-fw0rXt7wrMnRSr_fI5tLjkWLTwJAwsL40LUH7nh2ITW7R5Lm_sfTUleylsXmKs1bEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2151ad88d8.mp4?token=ticsQ72IV-A4CD3fAlwRzflj0pPMzFt5b6_be7wBwB3AvX9sRRJ13SguDb5M3yl7q43w4GN2AXCdbjIFu9WO19D5k5GoAP8m-6-n27wLinQq6xj9qd8ELv5HzWA8OZAVo7XbTB0l_3zjGpBN5SvLqJuMYX1RVg6KttcZ3Ui9DM7fMkpEahtf3V8L-_h5pQggK_Do1aXKr7Rim4UX0GHjF3tf4_91GHGG-oncaefAW_CdR3fFUxEZcYly1FRY29TGn8olF8XwWG9C8bP7kuX-fw0rXt7wrMnRSr_fI5tLjkWLTwJAwsL40LUH7nh2ITW7R5Lm_sfTUleylsXmKs1bEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🔥
خط‌حمله وحشی و حشری فصل‌آینده psg
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103942" target="_blank">📅 10:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103941">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPjntqq-YX0Uy-TbqPiPkPV8FTuVd7cRR_pcTCGOs7RvIrOwJweI24tZFhN3QEIzfy2a9SbV2gsL9k6OI0a8gwCBz4PmQhETsdlNszAcfElRuv6oDey6Beoj7ddC3BA6jZGFORzW4XK5U6mW3IVPW3uqZrEpLV4UDiHcs7U0q5eb-CAXkhXDVZfJj0ITQ72GcwMG6VvY43LBMaSPiq_q7arZfC1qgH2IMbb4zO0OqFEB-QNtN1DlfBDPw_vJ84ibxtbZLlWDL8JdietR-yBXMrQpkZz0cJ8EQzmmJ40NZjTVDvUUoA8O9PZF_awOLzu5DtbaIFow55g9ec1SyCSQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
🇮🇷
مهدی هاشم‌نژاد ستاره تراکتور بدلیل مصدومیت دیدار با پرسپولیس و سپاهان را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103941" target="_blank">📅 10:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103940">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdbe4bacfb.mp4?token=ImNQvLQJickUkZpdvpk1ZVyEAM8Oak7Wmo8OH_ezw5_Fy_wfNPw8r9D37K1gCM4gt-iNuheicdONmZ0OaTb_ZCaN9rJ6ah2V7StTmnCddITGBzkVA5sGS1lXZML_5PCA8CCjpl8VtZKooemgyVCgOvzyRXOfxMLorl4PUoQea9lkE6AtW79hYvB7U4ljcZOO1MzpCIB1PjJRl5aD3-XpYPXY-ODxoeEHw8hBo4lZK0DOdtA3qsJDn9kKgMThuTYuVz-yhEUJrsPN25wSNMsv1aWbHew1hGHzf47Tzq50QanQXreBx6XU3SyrU8e-oROVNMip-MXa54p7AZkhUQPWMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdbe4bacfb.mp4?token=ImNQvLQJickUkZpdvpk1ZVyEAM8Oak7Wmo8OH_ezw5_Fy_wfNPw8r9D37K1gCM4gt-iNuheicdONmZ0OaTb_ZCaN9rJ6ah2V7StTmnCddITGBzkVA5sGS1lXZML_5PCA8CCjpl8VtZKooemgyVCgOvzyRXOfxMLorl4PUoQea9lkE6AtW79hYvB7U4ljcZOO1MzpCIB1PjJRl5aD3-XpYPXY-ODxoeEHw8hBo4lZK0DOdtA3qsJDn9kKgMThuTYuVz-yhEUJrsPN25wSNMsv1aWbHew1hGHzf47Tzq50QanQXreBx6XU3SyrU8e-oROVNMip-MXa54p7AZkhUQPWMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇩🇪
گرمازدگی جمال موسیالا در بازی اخیر بایرن که با خوش‌شانسی خطر رفع شد
درحالی‌که دمای هوا آلمان حین بازی ۳۰ درجه بوده! واکنش مردم جنوب با دمای ۶۰ درجه:
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/103940" target="_blank">📅 10:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103939">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1875da2c0.mp4?token=QLXF6id72LBIFN15CmduQxhC7Xof4tw5XEisBgNFp9i28oFLWAVDbQvl-x4y14hDsOqPDeVhlH74L9iu7Sg7EnSDXPkHhb41btZ4pwei7-sJTqoK3Kc6ijMgCqH-sAsWxnpdW014zSnE6GY5TO15pdQr9hxQ0nZx4k4qoDc7JJF-N-6R_DcLHFSYFliapYh0hHdRZiojRMmLLga_1RITB5Hl7YDcS_L1xEcpxQv1lR-_lI_qEXGuKLeeSmhhSSeYCgCK_2Gt6bdezw5QALTIUJ3AWYMBymQGvtDFeYr3J5qP1YNrWMiEwPH0w5z_PuqDasUXwWVICRawZLyPBJJDhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1875da2c0.mp4?token=QLXF6id72LBIFN15CmduQxhC7Xof4tw5XEisBgNFp9i28oFLWAVDbQvl-x4y14hDsOqPDeVhlH74L9iu7Sg7EnSDXPkHhb41btZ4pwei7-sJTqoK3Kc6ijMgCqH-sAsWxnpdW014zSnE6GY5TO15pdQr9hxQ0nZx4k4qoDc7JJF-N-6R_DcLHFSYFliapYh0hHdRZiojRMmLLga_1RITB5Hl7YDcS_L1xEcpxQv1lR-_lI_qEXGuKLeeSmhhSSeYCgCK_2Gt6bdezw5QALTIUJ3AWYMBymQGvtDFeYr3J5qP1YNrWMiEwPH0w5z_PuqDasUXwWVICRawZLyPBJJDhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
آنالیز فنی بازی هفته‌اول لیگ‌برتر میان شمس‌آذر - پرسپولیس توسط محمد تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103939" target="_blank">📅 09:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103938">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0698ccdb66.mp4?token=s8Z0u6WaexaMkNceSwKshfTe9bZHkld5yxyIEFXJ-a2Q3VD6r7SrbuxzNMpJEOIKYe0Q1QK9ZfPW4zVC2KB0K6zpr5Iv0Q6yocE3-qmuyRi0SmLDtE5zQ7yHOrHAKuGdp4OpQBqsnemOOqVLK_-xhYbmgp-6MKck4Q1F1CGp4311-6oCvmL5KLr1wmyjcZgf9ld9HU4XCfQYxI1WZQyiSV8QXUHT9Tbr5IN5QdcbCBpX5SZVReKzrvnt_P-IST5MVzyE8a3okkhzp20kiPiDqiKgFoByRJbSKkDBe8K3sWDqII_S1Uf6f9TsHedGHiujNx5Gj1wTnJZlMycNrOMKSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0698ccdb66.mp4?token=s8Z0u6WaexaMkNceSwKshfTe9bZHkld5yxyIEFXJ-a2Q3VD6r7SrbuxzNMpJEOIKYe0Q1QK9ZfPW4zVC2KB0K6zpr5Iv0Q6yocE3-qmuyRi0SmLDtE5zQ7yHOrHAKuGdp4OpQBqsnemOOqVLK_-xhYbmgp-6MKck4Q1F1CGp4311-6oCvmL5KLr1wmyjcZgf9ld9HU4XCfQYxI1WZQyiSV8QXUHT9Tbr5IN5QdcbCBpX5SZVReKzrvnt_P-IST5MVzyE8a3okkhzp20kiPiDqiKgFoByRJbSKkDBe8K3sWDqII_S1Uf6f9TsHedGHiujNx5Gj1wTnJZlMycNrOMKSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
دیشب تیاگو مندز تو بازی مقابل سانتوس این شکلی نیمار رو دایورت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103938" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103937">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vyrc83iLCT-kvf8RlAXdODNZK-HThTkH8VMkP2vPD4KG5azaBkq0vDjgcE2nkuOYch1GbaQyw7LfmjFyp2NFZGAwrHQT_I0w4oz1nAPpyc3NKyyiS4BVjkCoHlPRb6WoeSJRBfC-IejfeYZRPD_WR7hhnr9mRWLXgTsBj1SYhomZNY2QBvb9VLilydWonjS2rdzxvHg-v_RAPPkjJdhHkmYEg72Yp_PjuYU8BYVOzyUtS1sT0ERzmF_CyuJSlINBXHIwH8oXtLegTT9eiWkLwZ4fKVcCuwF6Wxi6dm7WrLUBKzwKd1xpp9RD34ZpxHg9mxMx5aJW1uiExPNUx7V3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
سرمربیان بزرگی که در رده ملی فعالیت میکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103937" target="_blank">📅 09:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103936">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZRgIvVviU2AyrPp2E-O_9J7RfXJ3apjpS8MhpT4q0KBGPGrad50g8Tg1MkVAC6DJkfP8CtRGcpK4WHGyQV0wbOFaBfM5GuWSixRUo-_jJznqtJRE9DSbSSb_n4HxjXlamSSWYRAkc_XpqdjjpLBSw4xJnEnSwyjH5I96TD8MoNo90_pHW9yrNpxuWHOmUlsGDVZP2VSOKHNc3no_D_1ou_eTTYtgUC5_7b-xg2W1gODaKHO_dgFNICwJb6JVZTHNRvFXses15R027vOM0uOughmBZsuyV9VjbOTUMf7MybStayNj3UsO8bWWDBN-UT_qXEzYPECPodFMhnO3-BCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از شبکه الچرینگیتو: بارسلونا میخواد برای جذب گیوکرش از آرسنال اقدام کنه! گیوکرش گزینه جانشین فران‌تورس هست و هدف اصلی بارسلونا همچنان جذب خولیان آلوارزه
👀
❌
برخی منابع از معاوضه این بازیکن با ژول‌کونده خبر میدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/103936" target="_blank">📅 02:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103935">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccba4b58f.mp4?token=MTnClMy7t5fpJbRaNGgSLeoR5x21mafc-AaWra8NLFNb6G-RqfCZE25WV4CqLJFwzvUA2fR_vReOC-Mpe4KeNsvbQr7jGNLfFV1AKiVzP8H_cSEDiSI8YG3bKo7t_k96z_A5BRSnZzPoj01keyXnFDjAcG0auink0x_c8JrmvHbWT62GEWOB72Dv_92EAkeNTezAyeAPAy1JlrS9C3Uuc1DTB-vwFjz8oMY6e-1jxnOm-r4xjgXwBB5okyiaDswr2L6D_W444yzPaMr71farHC_nWIV_77hK9nI09nUqN4n3_r_pIKKkKhUdGUUgaSaEFnU6niYEFF4fxfTBlLq37IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccba4b58f.mp4?token=MTnClMy7t5fpJbRaNGgSLeoR5x21mafc-AaWra8NLFNb6G-RqfCZE25WV4CqLJFwzvUA2fR_vReOC-Mpe4KeNsvbQr7jGNLfFV1AKiVzP8H_cSEDiSI8YG3bKo7t_k96z_A5BRSnZzPoj01keyXnFDjAcG0auink0x_c8JrmvHbWT62GEWOB72Dv_92EAkeNTezAyeAPAy1JlrS9C3Uuc1DTB-vwFjz8oMY6e-1jxnOm-r4xjgXwBB5okyiaDswr2L6D_W444yzPaMr71farHC_nWIV_77hK9nI09nUqN4n3_r_pIKKkKhUdGUUgaSaEFnU6niYEFF4fxfTBlLq37IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
💥
ویدیو جذاب از مراسم ازدواج رونالدو و جورجینا؛ حتما ببینید از دستش ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103935" target="_blank">📅 01:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103934">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgFAO2RMmMe7O7k1TugBBTvQuCg8psVPhb8pgwNsnJovgsdgNkeQRejA1iReb7mczvsBi5-puFhn9VRKpD1p23MEcrNIPsblsNJNaGvN1QU8AWEI8vDMVXzipwjZs-37EuH8dUqJCXv9u8GfRKwQ9fLPvAidbPHJqHBmU7UQz1lziNvYNFbzIo34Mjk4zCjPopFauVjIMbEb-j6wrD3crfCSoJ9m0sf9-yUD6vHoaDiH1ncXuBbZiYJqHuxn4m42k1Eu-LMMXpVokEWeP8K8BY8yKUeYdXnOP0qVwV1Tqsqdr0uEA_hg_HVYE0QNXZbQjvODnsprIYkT94_WRVPhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
🇮🇷
باشگاه پرسپولیس: اورونوف هیچ درخواست خروجی نداده و شایعات منتشر شده در ساعات اخیر اساسا کذبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/103934" target="_blank">📅 01:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103933">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
🚨
🚨
🚨
نوید محمدزاده: قبلا هم از فلسطین حمایت کردم الان هم میکنم چون با اسرائیل حال نمیکنم. مارادونا و رونالدو اسطوره‌های زندگیمن و اوناهم طرف فلسطین بودن. من نه طرفدار حکومتم نه طرفدار شمام فقط طرفدار ایرانم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103933" target="_blank">📅 01:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7dPQ844SrvyH7onyJSFtWWF_sa6wNB9EuXTFcsSV0SZIfN-j26_BXt3eCZw5OU3mWDFMXoYANw2kPh7zmO0NQoZOTcwj9OC2WscRRfcw5yBjiHXJFP8_P8_hgi-oFJo9BGAUMOMTJvS9vrnRwvMGm24gazJYd_qqqXBFvev1kJRGdyoHaiS7m30BJW4swh-Ma7bUq12TlPDAQZsFwOKY5-K-9K6KOYdWIGO0jdJoZ6nvui_dcqMG6RHC-y0ggnUzLjftCK5ADqi5f6C6CjqtkQI1zPhp8T4VBkavj5QxNIKxhW2moS9w5G0N9og8mBv0uYAwMcvB_Y9oAbGWKZb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3d3UWPj7099CJY5XjAwEQdqXYSp6pmcmkhfqYLEAweus0ndXDo9zcCf0XKWydZkBviOUVLAFFTfHxg8yO5-9xzfJXEAUY71sSyLVNzxeAgt75MxyO5m7i0ZgFpdzbTzKxQc8i9qXZHxvOB7LzcboMtvWFojy0QS-MihhmjfxeN1Z9fEQiYMMi9kdzBAnZgk5uNtke8tIUlkSMPwCiTBUIOaiZR-UQxmsdejj4DMyk_sw0dWJ2uwVwNnFy3UU5a7cY3kSRg88VXUJWOkBD72rmVFZMmIGL1uqRJLTPIm49HiTKkJNbOlvQvG-38FtZQfZL-7paeIO3hghNOKcjj0HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاپ قهرمانی در دستان بازیکنان لانس.
❤️
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103931" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103930" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=qKqLhhPm6JHx2787XpsodsCZ9fDZwmF2nsLnO3sF8Zb3WkAMRO_mqcVjqwLkIDw18iQCZ4ZYUevOqeHu75WtfO5Qdt7cfnDtS3gBEDQd7Eh--VL_8wXxFupsqRvH7AY_oLsF_oo3zQ0ZrxPi06OXYZhoIMy_BrlSdCl5Eb9nBoSRbDR8j_Y0O-0CvEVVN73x3zBMRP53cCt3AsR5J4FODM6iuoP-O56ieTKsubcKJexsb3UXku5tPU0N-lt_C9PZxHp1WJwFWN3h-4pNfKdiq3F2_3eDcvEIYZJBnO6eNJWxURSUvTTxO-8eFnP41zf6gY80q8wRplLdYP7Np5b7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=qKqLhhPm6JHx2787XpsodsCZ9fDZwmF2nsLnO3sF8Zb3WkAMRO_mqcVjqwLkIDw18iQCZ4ZYUevOqeHu75WtfO5Qdt7cfnDtS3gBEDQd7Eh--VL_8wXxFupsqRvH7AY_oLsF_oo3zQ0ZrxPi06OXYZhoIMy_BrlSdCl5Eb9nBoSRbDR8j_Y0O-0CvEVVN73x3zBMRP53cCt3AsR5J4FODM6iuoP-O56ieTKsubcKJexsb3UXku5tPU0N-lt_C9PZxHp1WJwFWN3h-4pNfKdiq3F2_3eDcvEIYZJBnO6eNJWxURSUvTTxO-8eFnP41zf6gY80q8wRplLdYP7Np5b7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a25
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103929" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103928">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQp52RYctncY2IFw50RsIXk6d8trHcEGukn11XgQ_bDp7gqbPDfiCK7X9ptP-zdA_Pks-K4w8mQsirjpJs3t48Xj1UQ7Bz5ReYSiwxhH63FuvsxMe6xprOkA-I3yXbCWkZ_ZJ_fFkob-WBAIS1mhSz-VVOIqd8Kk8q9Am5yZ3knTVgmC_13368KPV_1QNEhko0M9fMUfX3XvoGAJBxMuhoYVxjtxvPnAllZF28gxYLCOyDvlZdFOLVH9bVhokBWpCd5-4bx3FbG8oDQF2xk83Ev-HOHDtEAJafDfdHuBH3Zx8bd1Qgye77_lb534gJKstNeSayTB47KywTRswiYgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
سوپرکاپ فوتبال فرانسه؛ ۹۰ دقیقه تلاش فوق‌العاده لانس برای قهرمانی؛ تیم وحشی انریکه مقابل حریفش آچمز شد و جام را از دست داد
⚽️
پاریس‌سن‌ژرمن 0 - 1 لانس
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103928" target="_blank">📅 00:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103927">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0ba339f4.mp4?token=iOF7xAIwMERPIvm05ebjyl1vZw2XrTXG4NSP5IxkHNwY4vmNlOhNtlkT-39IFfqSWg_wFcfPbulGaAyxti5BITHu08IszTfSVoxYdGD-rxVVhYi7pEx6CzY9wDpG2T2Gnif3zdiqXVT-D4ZVV87c45awyP56BBVGSRTty45OkPfQRA7qMwjWUuIe9uCYrRLjtzqW5DvCFUASAc2dDZ8I_y_6Y8Xtei2xuW9098BqOcavzZ8ca2YQhNkDvf3oTqXgvAa1NYiyLx3gF1lUlpLhGCZNlAhwmsDZiuMOl1r3wo9WizvwdRI5CGcgnlalPixsAaDui7TMClWezP6iykrzpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0ba339f4.mp4?token=iOF7xAIwMERPIvm05ebjyl1vZw2XrTXG4NSP5IxkHNwY4vmNlOhNtlkT-39IFfqSWg_wFcfPbulGaAyxti5BITHu08IszTfSVoxYdGD-rxVVhYi7pEx6CzY9wDpG2T2Gnif3zdiqXVT-D4ZVV87c45awyP56BBVGSRTty45OkPfQRA7qMwjWUuIe9uCYrRLjtzqW5DvCFUASAc2dDZ8I_y_6Y8Xtei2xuW9098BqOcavzZ8ca2YQhNkDvf3oTqXgvAa1NYiyLx3gF1lUlpLhGCZNlAhwmsDZiuMOl1r3wo9WizvwdRI5CGcgnlalPixsAaDui7TMClWezP6iykrzpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
خلاصه که گنده‌گوزی آخر و عاقبت نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103927" target="_blank">📅 23:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103926">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fefaf274f.mp4?token=FtS69b5wN51eME47YeAVupcgnwt5MfUemJSOdNmrzihBWbBbhB00nXPsEStgW1mEfISBKC_1pKTCc6LhfbVs9QzOt7W2zgdm_XZbkH6tz64CfkZFNH80Em9v_8FmcIz31KOEUxo2PxV7UoKN3u818M93fHeWaWhEdIFaAx2egaLSrfYE7Dmm2pO8cnUy69gQGAh-zL9PxZ-jjxVEQkEnQ9SVG3RxGa9rfnCd-S1lNT1drclKXjZjfLijlLzkqEu6FTQ7d6QQPQdEpPcaYnukNfVTGrVSScR6BVrjbJWyd62EbgXQ7-90DRo2fvPqtO5W2D6hrf_jfQ3m37hjsF9Eow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fefaf274f.mp4?token=FtS69b5wN51eME47YeAVupcgnwt5MfUemJSOdNmrzihBWbBbhB00nXPsEStgW1mEfISBKC_1pKTCc6LhfbVs9QzOt7W2zgdm_XZbkH6tz64CfkZFNH80Em9v_8FmcIz31KOEUxo2PxV7UoKN3u818M93fHeWaWhEdIFaAx2egaLSrfYE7Dmm2pO8cnUy69gQGAh-zL9PxZ-jjxVEQkEnQ9SVG3RxGa9rfnCd-S1lNT1drclKXjZjfLijlLzkqEu6FTQ7d6QQPQdEpPcaYnukNfVTGrVSScR6BVrjbJWyd62EbgXQ7-90DRo2fvPqtO5W2D6hrf_jfQ3m37hjsF9Eow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسوت اوزیل طی سه سال شفا گرفت
🔥
🤯
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103926" target="_blank">📅 23:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103925">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8863db9835.mp4?token=K0JKNPDxa67RdetKOAg5MN4dMFMsLBCl4McaIacRCSXMmfEhtwR5geZUrM2Pq-XldSdIlPoi6aeukSJYUJere2iszxwdV4jlDZkIDy4K0rXNua4cNBUjU2nkMmg1cfJbW0CV7tq2EJOivuTAVvIDr3bx287gPGW8iRqESLdBzkJZHwBCwQd1VFj2j5t_jZL9mlvjblNCm2hG1TMQdDbI2gAOPd-DkiDJQrEprexLSUEHk6FUfE74ksernFTcuKwBR76aoI4zKW508is4rVwvuRJq1Yt4BRpxtIRrUlJCECjfvQp0J-iRKu0e_wJVcHGDXmRKzaTlO0FU5xD4FkQ6SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8863db9835.mp4?token=K0JKNPDxa67RdetKOAg5MN4dMFMsLBCl4McaIacRCSXMmfEhtwR5geZUrM2Pq-XldSdIlPoi6aeukSJYUJere2iszxwdV4jlDZkIDy4K0rXNua4cNBUjU2nkMmg1cfJbW0CV7tq2EJOivuTAVvIDr3bx287gPGW8iRqESLdBzkJZHwBCwQd1VFj2j5t_jZL9mlvjblNCm2hG1TMQdDbI2gAOPd-DkiDJQrEprexLSUEHk6FUfE74ksernFTcuKwBR76aoI4zKW508is4rVwvuRJq1Yt4BRpxtIRrUlJCECjfvQp0J-iRKu0e_wJVcHGDXmRKzaTlO0FU5xD4FkQ6SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ویدیو وایرال شده از تفاوت رفتار جلالی پیش و پس از پیوستن به تیم‌فوتبال پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/103925" target="_blank">📅 22:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103924">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLsQI0-QHI61tIYrMgh-LSs8dFP6Ny6S5E3VfCM8kzxCPI_7a77HWQkglvEPflpazS8ndU-tBOr0o96BV6iCHX2-cQvqVbGNxm29K4q6w9DIWa0q8zJYCSmErDmZ_4_PJjo2zFSbAq0EsWVwa49jXtQMtOxj2b9ZLITltRQ_ClCjHZHw05oaWuSYsO48IPk5SQDy30KeiW7KzWzz9q8k7PJsEACrfAj7TE3sfe02Gu6MKiyNM8wLLdXHDlo5YVgVoKePX-PUw7eCYhgiHaZy2tF2kRBclmUuEwz_KKfED9MCkNRKFuj-WA96ZTD2r08FH3SPL2wmf_YJflOYGov4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🗞
🇪🇸
پوستر دیدنی رسانه 433 برای رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/103924" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103923">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2mi8xrXqN-rXuxDb9i9gLzLA6dG9y3iNHSIEBLoB8ydSKu3f4A53qX9KM1YavPuTtTm6Z-DQq5QwL54oph01d1v6VE-9peVSDhU7dOKfOEdE27tMpeBXVxsGXb4RUVYnOQhRz9lRilbP_JHflF7nF2yNetIa8shF2tj5zMg2n8BkXlVi93z7Mj4zuBRYsdTPxTKB-edKKMNt81nZx_U0nUGWKS9WRZtEwguw08goQM4j9Nzhr6vl0Ngcj6puW2nzbGuGP3Qc6b07zJK_6_-BBUvGEDdWVVzEgE8449rg30O_fstfmblgXfNtpidII2fqUjVcpmoD3hkL5NFLTyYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
🇪🇸
#فوووووری
از جرارد رومرو: رودری فردا دوشنبه وارد بارسلونا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/103923" target="_blank">📅 22:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103922">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzwcXPs80da-Suu6VKnp5_yktuh2profXUKKR0jlj9TFW7DL7TVaiI1g5l88xsummpT996o2lk1BbGL_8hcf2OOvMwW_ZDd1te6DI5cNDfngWutIsADn4aIRovFd3oBdv9e_G-45F2s0hlSIRrTg8_inZU0RWgTKFOAN2mUapbxHSz7x0k7Z7xCLiJlZVkv0VmCbrQVpFzM8hr-YH1PPvFYaxIS06pwbg_kvyD9z9A6WW7Oxh9HPZL0zuB10DLJrpKm-rHCTEwOcMX1hzC-hjBgEWlp7pKYN8pW2epi3LJ0Fo1wjWejHAc-o11fipgXl-85RSSMZ1DALJEEOnN5B6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2/3 DONE
✅
👀
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103922" target="_blank">📅 22:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103921">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjE26P_w6tL7__uasSkSdyoTz0EWWm4iSzSQwsj74937a5mAzNDalR2Q12SSeNEz-SGVRbE2ydzi8jVOwSee2nKDKp7OorfxrhgWU42k56nCjqKkeXZlQ8673NJ43dacy2YBV7lwYpcS9KVCWWKzSzBG4fjJGfFSl_EFielVWdtyICGpMtZsGK6BD1J_9Wh888PGEakIZLPJn5mBRiYGYRV13NMLRyrly9S1IvImYNLFP87AnGygAkWTm2_OwvBa147dIBlDFn7H7l4Fno-4oIrNbi1tqdenoDKTGQN4XLPNkyAmxwsKOVPo9eg6FsfAdHCw2MNOjLarSkEeUIBa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
مورینیو درباره بادمجون زیر چشمش: نگران نباشید از شوامنی مشت نخوردم. فقط یه شوت به صورتم خورد که اینجوری شد
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/103921" target="_blank">📅 22:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103920">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3Dni2VFg5cdyR1OB9saaDieSvAMWuEQBZjVFkXAU9yEwLPEclzWHjzNF27bUbvqJFIj3X5FO7YPOCY8BLQDK9vyTliIrapukncpdKrXVSEGnU2iDwljWm2eQEgzrJdy7du31c7WqWyFbFiMmrA0iKuVwdfIvuKUxHWkpFi5wpqBqiEIJNIuRRYBikhNLMdUAJXQ-96muzd_RPVDkOif_wRRrPdTyLg5hK73zWFuray5SRoRFOsWPywgeY71fV1cCcXRpkVui9HGIiK01C4iJmLy7Xq742BcobgZr2AhfVmQVqm6LRKcXZfQmQN92khtYRYQtXW1PxA_QBn8tVconA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از COPE:
✔️
🔴
💸
منچسترسیتی برای فروش رودری ۶۵ میلیون یورو ثابت + ۱۰ میلیون آپشن دریافت میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/103920" target="_blank">📅 22:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103919">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h15nwjPObASir1NokU4vpQdlcB3M05S-fAmALE_YqXYkDcn96DlKuJUOb3j0QC0mG9_VRSfRVEv6r9T9VibR8I2uh8rpOTQb5JWst0OJRLISxemNA1CcRMnltbZfYl02uiBW-P2zDhJgy_v1n0m4PaPxaF7WhRUv21Ml_mp37sURro0Ntrlj9KVFSDeFc7GLIsEnjpzEZ0vRqU1wZEhK2XEKXdX3b9xkH8RfQZD599AflxgndZkVZOCNMzRPjllP3rKllR_Viq3elpYzWOSKT6MJBSfmJ8BT4T28WpU0vDnINfEoxeOWqAlf-KTjinP0v1gUJyJmZoa_JMhvLGLy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
بهترین خط هافبک جهان در بارسلونا
😐
🔥
🔥
✅
🇪🇸
۶ بازیکن اسپانیایی و یک‌بازیکن هلندی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103919" target="_blank">📅 22:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103918">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg6lHtjBCFLFCMFm1wU1Rye9SMJsCUmJarNgDtZIVI-X_H68mDSStmwWRCYanOcuMsh3Dp00jkL1TsMls_KuIVmes8guVvXWqCBEZUAPPljioOvWbPnTkgwtGT85EjjpZ2xhzTiKC320C2dsav5Yl-QDFgYdZux-sKnAc130qmu3h8YziF1z4VgbujwvqZln5i3Fb2ZFoN-sELqf-ZWgYTKAuqde9NG_WlZA9_ODuZ0cT9SWgRlzH_2fNFbo5wOk09VnSv1VPPPygFIzEni96L1yJFPUYPyv2Xnqm0dm6qBTnWtpW8ClEiR5Fu9boHTDVFuSGxzVvLm1e1S-Mby4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوووووری
از رومانو: رودری ستاره سیتیزن‌ها به بارسلونا
HERE WE GO
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103918" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103917">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqjqLlrse_nJ4DiAewu7rWba2n5AZkdXUkjRgI4HD5zpwFMhKimVngc7xWyyB2GWSrPjh-7SO3HNx-q0T2kC992bpW05Z4N4oIquqrnAnq1B99cGhDDlyLY26dfi9igetWulPJYB4em5VQSFOkodWhPVIcrw6fFOGNJtF58ms4YoGCW7SGdW8hRJ9eNlQTND-lE2rIgLuxG0ps8h1yO79HrFFLOTnUg8C_n3LMQzVt6ihMOtRDo4pgMdO2TXREFQTLCQUwwsBqiN5v5_qBH3UMUetqwZzmrJeZpd3s6kdfzZWcYfpQY6DGVxHqDDsgfb84NSXIMbRql-XvqWo687xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرکاپ فرانسه؛ ترکیب پاریس مقابل لانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103917" target="_blank">📅 21:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103916">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6285ff8281.mp4?token=sYs_yx0KHbDXlIumr7Aa5JTWfZf8PCgAjfV5cBZIEISfJv9yrpfHZ5d8dJZ4zZ46TzOUaXn67bJBqTAre4kX3A8T4lIZH-YXDsGK7gtWk31wLgPFFoIVJ7vov9t2C6F7OCBJSElpiuVqS93jmAWZG7iTuFJ9y3an131M8-lIfOFi8Mv7pfrmSRAcy0BXckLXNhqz2sY-a3TMHzSsR7K0Q3FRN778uf2J2ilPh6rrvDRzvFyitrrfe9-7g7VKGrSb4IN5kfC8vHA_wFKdXdVOlpmaZDfDBzB4ImuzcGZzSuaUxBlxR_xwc7MKchxcnfD9MXTyHcaCWpLAcxcpRSyMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6285ff8281.mp4?token=sYs_yx0KHbDXlIumr7Aa5JTWfZf8PCgAjfV5cBZIEISfJv9yrpfHZ5d8dJZ4zZ46TzOUaXn67bJBqTAre4kX3A8T4lIZH-YXDsGK7gtWk31wLgPFFoIVJ7vov9t2C6F7OCBJSElpiuVqS93jmAWZG7iTuFJ9y3an131M8-lIfOFi8Mv7pfrmSRAcy0BXckLXNhqz2sY-a3TMHzSsR7K0Q3FRN778uf2J2ilPh6rrvDRzvFyitrrfe9-7g7VKGrSb4IN5kfC8vHA_wFKdXdVOlpmaZDfDBzB4ImuzcGZzSuaUxBlxR_xwc7MKchxcnfD9MXTyHcaCWpLAcxcpRSyMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
اگه موقع اجرای انواع پرس سینه، بیشتر سرشانه و پشت بازوت درگیره و سینتو حس نمیکنی و به ناتوانی نمیرسه، زاویه دستت با تنت اشتباهه.
✅
هرچقدر به 90 درجه نزدیک ترباشه ، سرشانت درگیر تره. هرچقدر به صفر درجه نزدیک تر باشه ، پشت بازوت درگیر تره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103916" target="_blank">📅 21:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103915">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT0nYnHPSt3dULYrPeDFP-PnnIWM9HhGkYPxcTlnlwUC8W6B6bGcbzzMO-NPuFoEkTK1QZFQrUmTyTBQsF27KISLQGu4LsMq2Re_rKGbO0jF30-k2zgRbhDUzEGak8FcdlRjyKR3arM-KJ-6MlzEm4PgtszNC5JZUL-FrwSuMQ5HzotgKmtSJac4IcMWPYrSNEa62ITm5rPQHRhNuB5HSumAaGGApJMTwmLXRZv-5BFLPEcdwDkuFxfQOWyO5wE_t6fjGJvm-gfc7tUR8ZaVhCb-05BKMnfAgjmhQAbGjl2cRhWfXQnVRGfcFEXKKGv0HQkNJsB1jsFSwX7OcTHffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇫🇷
اگر اتفاق خاصی رخ نده، پاریس فصل نقل و انتقالات رو با یک تراز مثبت 129 میلیون یورویی به پایان خواهد رساند.
🤯
🤯
🤯
🤯
🤯
🤯
بازیکنان جدید:
✅
فران تورس — 50 میلیون یورو
✅
ماگنِس آکلیوش — 50 میلیون یورو
✅
لوکاس دینیه — 7 میلیون یورو
بازیکنان خروجی:
❌
گونزالو راموس — 75 میلیون یورو
❌
کولو موآنی — 41 میلیون یورو
❌
کانگ لی — 40 میلیون یورو
⏳
بردلی بارکولا — بیش از 100 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103915" target="_blank">📅 21:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103914">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAYQzRHtnmU8cRW4UfKJ5X0ffpOL9n8vYXLS11fnEFpCzC0byORmBLLHHPed1ogtxL8ZIjdwITqllXXR2r1m2gKbY-fY-khPH0iNR1I6nAT4BaEw906duaPNhnfX5WP82GpLkms_yVz2eNNjCD4xIh9sbIJucDHKj4y132rwn48v8zdY3VcbZlzavte5K7ZjjBDYYt6tpqPu0GkoRzyO89iw8trAmVg2Fe-mLCwazONws1Mryt9pbktO9x-nLi70DJhD69SAigk2Zi4hZIPhik--g2xi4zPRXqVlSxAwnBpJQpg6KX3CGoOG60VG41WsAxTQtGp7O-nGQSWxo2vjCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوووووری
از فابریزیو رومانو: ژائو کانسلو به بارسلونا
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103914" target="_blank">📅 20:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103913">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f160aff0.mp4?token=AnrKUWFmgwb5sa8inafllvYSt9lDYTqR8KjVVsSEEKkttSw7Rq3tEYiHkh-HcN3AD5p5nPoITiiKTvU9nzgTFROtrc09eL3-MDv9K7Mez1EBUsGpWCgOvtn6QhgdfaS52LsAjtcMQQS6-ivKKrg0UFG87EFbJZUlpJDnnoI5Vr9gJAgMU4a7L1F5oUpg4427py607MuyTjLXVijBLkQSHlyVngDHK4GDtUH_vzvtf1x6iHc1fekglIW2Dbd-NFW0gECZSoIE4alslgkFUi-gERUMqKmhqYRaXi2ZRt_K_W44Phd_-7wNzK_mNgE6ubge8PLE_16DeZ4Wr-92pIXOig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f160aff0.mp4?token=AnrKUWFmgwb5sa8inafllvYSt9lDYTqR8KjVVsSEEKkttSw7Rq3tEYiHkh-HcN3AD5p5nPoITiiKTvU9nzgTFROtrc09eL3-MDv9K7Mez1EBUsGpWCgOvtn6QhgdfaS52LsAjtcMQQS6-ivKKrg0UFG87EFbJZUlpJDnnoI5Vr9gJAgMU4a7L1F5oUpg4427py607MuyTjLXVijBLkQSHlyVngDHK4GDtUH_vzvtf1x6iHc1fekglIW2Dbd-NFW0gECZSoIE4alslgkFUi-gERUMqKmhqYRaXi2ZRt_K_W44Phd_-7wNzK_mNgE6ubge8PLE_16DeZ4Wr-92pIXOig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🐐
دیومانده در تمرینات دیروز رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103913" target="_blank">📅 20:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103912">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPSFjZYI7NbNpWiXigfO2y-VRT6iq2Lo6lB1SBqw2IABa-nXK8kvYPj5MdpO-Wg27_-uGSy6IhcVPemErOle2yje9M7tVwy4BqH7Yw3EoPOB2KGZ14bxXG0-r1wcqqpmluJoWF06A02MreQ_E6pxthLdeSaB7MCJ6wHRzKgyVuGcsVOA2KojZBpAG-5ZX_AAWqWFZXNfg4eyDYOlFFmIQE3HA-nl5d5mTGzBVeH_YF7K-g4tzVKUGwzK4igCnJuMg2LO_AvMD7NgHKKrKpG8GODgIle0NP6ydTzQgaZCGK08exck4sEiC-EeWUQbnL4QC0z3S0IHl50C4Ic54raeKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید با نتیجه سه بر صفر مقابل شالکه به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103912" target="_blank">📅 20:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103911">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
⚽️
بارسلونا در یک بازی دوستانه، تیم بازل سوئیس را با نتیجه 5 بر 2 شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103911" target="_blank">📅 20:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103910">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA4OsB4_9a6XCnVCMtcRjcMSiDbvEMFiKG0ZqN9yVhMAn9E6q9d_plnmeVCRkl8NzmgisRgeAGR71xN2WDP-lYOUiwt353ouRHjOpy5D-SGhhoeebqeuJ_5kq9PVRzhzwTjjijZXpi6fC-8KN0CzOfUR1NS9Ei-IrSPd-hnCigb6JMirLwcqnbPEoWA_aGEWwe0XsQJg2-kzhf_0fFck6T12R9IHUuuq1zSeQJMTAPwEOlQaPA7s8ZagZhyNv88zXnhJL3Ls9l50zoa1rfUeF7JinCMAMP8fal-FmoaFT0syHSshYUYjVIMTsbdQtX0Flc6sUrkkpZoJbs045udruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
بارسلونا در یک بازی دوستانه، تیم بازل سوئیس را با نتیجه 5 بر 2 شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103910" target="_blank">📅 19:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103909">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP5lpbJ3YfJPMnc_gLTzSysJMyxiflN8CtMmRzMNDtdA9RxhIu-PuunKYHfB2jlMoRqCFjvZWBuwN1Q1UygBnQZTDMHUEi0H0ICCrOxGedsAlRS3DAdvf2tLnlVEru80tUvI-TB7T1Iw4FgjwV2IIfnZt8mhXfBRyc8Toe3GeNFpZuU9WZ34eHrkv-7eTsLUQmQeFi4NYLH6kEguntPvS10fXeGHiOTv_VhqGLwXlBF7JN1jS8rfPJqZvPfAKGt7QO_tRXnM9BRl1CHqRT0siupnp07wV5B7NEeGxkUgkn0IuyFdWC5bHbjdeB_2jO5w21xGhvPCOBnGG91y0J3csg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
تاریخچه قهرمانی‌های جام خیریه:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
21 بار — منچستر یونایتد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
18 بار — آرسنال.
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
16 بار — لیورپول.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
9 بار — اورتون.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
7 بار — منچستر سیتی.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
7 بار — تاتنهام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103909" target="_blank">📅 19:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103908">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHhAp7HQjNmMNhNcB8gF2oCt2jUk6EHwukUWj21nT65Vkr8kH458iDYr8Jv5WqcUAtpoPgPHoFohG5SDtq7APu1RdaoMZGhbd-Ce_cUpVuwKRZrWkragfOWb2o7pDOhvUiXbZ0Q3ESwKn8jRUcm1di8XFoNo5gmkq9uWW-tnTwQ2B_dBTqDRpIAyhUjNDQZGZT0BmX3QwDftmUEaPv5XKKFXkol_seJL8WnToeQ1fFrSdJoGk_A1JqJp253T0poVeuQzVI3NcPxM2Agg5Evuj6OLhFrbN0x3DFZhkCxsWh6eU2m38uRK2JEGe370EtBnku036cPwZwGZCx5Br5MPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدارهای مهم روز دوشنبه ۲۶ مرداد
💥
بیشتر از ۴۰۰ آپشن پیش بینی برای هر بازی در سایت بتگرام
✔️
شارژ حساب از طریق کارت بانکی،ووچر و ارزدیجیتال
✔️
۱۰۰٪ بونوس رایگان اولین واریز
✔️
امکان فروش شرط های خود
✔️
تسویه حساب بسیار سریع و بدون معطلی
⚡️
همین حالا ثبت‌ نام کنید و و از بونوس‌های ویژهٔ بتگرام بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103908" target="_blank">📅 19:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103907">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7EnbJqNrH-fam-uyUPEM_yU-Js5P-Z1ToKy4Nt33AcSRfe6p1JIYze-o1fBp9djtx8N65SrLuukyRDL5gR5DJOcWigRpOok6PJ6O0cH8i_VSXek-HS15XdTzdj7ZzE3Ck0wxXl2YDsKJvXEKAlRbg--j53dxOzkLRM0ObwWped59A-CQhpBL2AeEDCrPX9IkBBvDkdcES8MAXWjmi0VQwtzCxEP1zMAWyGiCzhqqFY83aCJDmjzHflsjh_NGPrP5exlhND7yKpq2Ol3ko0AUeWeXGbPH-u8yrU5dnZwUpBCyX9qIh2nbOmKBq-n7KmwbjYfe671ZDE1dEkujLO-ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#رسمیییییی
؛ کسری طاهری بازیکن نساجی با عقد قراردادی به سپاهان اصفهان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103907" target="_blank">📅 19:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103906">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElXGddR1zbUbvjtRtffUMetnINDPKToZDBY3rGWHxFY6a2OUXoFpW03nN-0AlkYgZLOqEpykxl0ai9vcLXlxKnftYHWZ8U9NtG4hscD2vxxXS63lCmUl7Wo_LAGNh551wVXFPcPi4UnurpI-4yUogieAV0IFDRQLA3AR3xOBY5l79GizDS4n1_LSSDxMTRV5yULusmxJoEy1mb24HjNQbGAFCATR2pe6KVxvHFdAqfTol2FOMgB9SJFXiI-ZcvkDYs7dM9k65HswpBXkCt6itMWXkYwV_L_NFjIyExfRLywGIBzw6-2d-MI624BTosfhQ-GwGJkNpSxrVPutfDvoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🚨
پایان‌بازی جام‌خیریه فوتبال انگلیس؛ نبرد دو غول فوتبال انگلیس قاطعانه به سود آرسنال شد؛ روزگار سیتی بعد از پپ رو به افول خواهد رفت؟
⚽️
آرسنال
😆
-
😏
منچسترسیتی
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103906" target="_blank">📅 19:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103905">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYM5EDY86py558nAM6bG05n9HATearA8RlJ411Id1TSN4JpPEBxLpx-Ufs3aRsxI8wU067aGq-7yeUm3RBypkziXL5Qf1SBhHX7jmNMK5x08DgswFZ9z4FmK0aWunws07Q6fru0obrngELLXG9p_4mLyaUwNleWoLXCkjR1K_W6otzPVFtaQs6ObBEKjYLM7Qii3AIvL04M2nQIz-i1esaNJ8EkWWOA91qpeZVSOTlqJ-TRmqkZrqtgk0SX2ABUKF0LN_C_kRhOu5y_MJ6s-f8NjWyiMKYuElxJSJ4oQOlm6r7x22-tyWe52wvjsGpu0SA9-B4oN4CZBcR9GBe6NCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🚨
پایان‌بازی جام‌خیریه فوتبال انگلیس؛ نبرد دو غول فوتبال انگلیس قاطعانه به سود آرسنال شد؛ روزگار سیتی بعد از پپ رو به افول خواهد رفت؟
⚽️
آرسنال
😆
-
😏
منچسترسیتی
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103905" target="_blank">📅 19:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103904">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlzAGaBWMH85CxIPkFgE5oCOj0_kJ_LoMvLWYHOTWXyLy8HfHB7_qk9KzlDJL3Pbzv4v-hwCjvJJw4LKR-YkvN_vL-9xhXhrPhOuAy7clqbZP2ceQPhg3WA27yf0mePZcMocImrD7Qm-Gwd3k_hj4avRlxW8FLU08Xde_QL_Y7k8QABYnMKaru9Xh5uMRVQyudjcTrq5l2IDWfLLCr-DV04xqDEZ2xcje0kNdWQP6A-VAZ9g9qdeUK9oCS0QqfTB0LtFNGeo2UFXseFMK9LcWKqxeq-OGJrIfo9ZRq1uhjYzFT752ZiATH4NMbNvUco_-C5LxHiJpj54SCRViszBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇵🇹
#فوووووری
از کریستیانو رونالدو: به احتمال بسیار زیاد پایان فصل‌جدید از فوتبال خداحافظی می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103904" target="_blank">📅 19:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103903">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/244baec6e5.mp4?token=Qbpar26QeiqpyyJWH-KCvmQqO02L7FbkK1VlthUCAbW7o-8Pj5x1pyyARUP57uVJ1sKIpfnju_68LvL8sDzSpeey_Ml5q1Z-ywK-_DcCDiK7WrywyeuYsIWcizPDA67LcW0ZDam0VZ6gqBSvQCyIhKj9GMdgWMJ0xdKdDGvUSr6edVLKcVDT37-1h1Dc22gkuqKyQh_Y7C_EXesi_vWbAJdzrTepKC5fCBURMYpUP3ZnEGoK1p04ssE5szyNcsije8jZbDRF1YFXo0lCTbOPd3qn4VTatoNUdAQCZUuOE14AUc92e16TR4gXKBzhjymVQCMPaxv9d9FRhCKlGGXQwleKlu-vCZ_YVdMsC2xhmAQ3e2FDGSXSRKHNKNnsZIl3whEVZYqPSEiUX0YMe9_h7YE4HR3EzkZYF0XefJFWHoCBbv8XwqfYpxd9PDAkr7imvIJPoDJZsgVZ5-J1pK5U_L9YnT23o7tDEqj8zk6MROTKgNG09GK8GCbUkREB8y_DQexaZn4STjHQKy_lhCoKNnVmhirpIeXJmU2FsAOtzQEytBQPMGTH9lCNzoLMMfnnnwSq2yvZieLPLr23d32oWy0TISFDIhqQH7ZWtQzKKYbS5yFGu7AWuClkLq7TyoaPXKSB6By-LJQbiSW7aJ3d5YeBccOX3Hw-VlFoI4tf4GI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/244baec6e5.mp4?token=Qbpar26QeiqpyyJWH-KCvmQqO02L7FbkK1VlthUCAbW7o-8Pj5x1pyyARUP57uVJ1sKIpfnju_68LvL8sDzSpeey_Ml5q1Z-ywK-_DcCDiK7WrywyeuYsIWcizPDA67LcW0ZDam0VZ6gqBSvQCyIhKj9GMdgWMJ0xdKdDGvUSr6edVLKcVDT37-1h1Dc22gkuqKyQh_Y7C_EXesi_vWbAJdzrTepKC5fCBURMYpUP3ZnEGoK1p04ssE5szyNcsije8jZbDRF1YFXo0lCTbOPd3qn4VTatoNUdAQCZUuOE14AUc92e16TR4gXKBzhjymVQCMPaxv9d9FRhCKlGGXQwleKlu-vCZ_YVdMsC2xhmAQ3e2FDGSXSRKHNKNnsZIl3whEVZYqPSEiUX0YMe9_h7YE4HR3EzkZYF0XefJFWHoCBbv8XwqfYpxd9PDAkr7imvIJPoDJZsgVZ5-J1pK5U_L9YnT23o7tDEqj8zk6MROTKgNG09GK8GCbUkREB8y_DQexaZn4STjHQKy_lhCoKNnVmhirpIeXJmU2FsAOtzQEytBQPMGTH9lCNzoLMMfnnnwSq2yvZieLPLr23d32oWy0TISFDIhqQH7ZWtQzKKYbS5yFGu7AWuClkLq7TyoaPXKSB6By-LJQbiSW7aJ3d5YeBccOX3Hw-VlFoI4tf4GI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
خداداد عزیزی: نمازم رو سروقت می‌خونم اما رفیق عرق خور و سگ‌مست هم دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103903" target="_blank">📅 19:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103902">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d00dcf8bc.mp4?token=CPMxbHlrUWXGadfz7N1IFNkUhrhVE135s1sK5tcoeSNeqkXX0mrKk6ZSaJYDSfxN6FBQduhW6VkV03DrHVkbeiQw23zHM5e7hZ_p5E6OLxXxJFFkB1SH-NaGcpItSrD1m8gSzy8fOcjf38c8yr-Nt8ThYpMPGdwolGfLr_qAPbaHoxlpMC0rlPlvIKn0Pq5R4jtYxwl0Nobaw1wu-PpEpOLqpO56Fse_TdufyCIeMShSgAgBVliFF_KnZ1GR0RPB5R5j3Q0FRAyqkNzh6FOeLfUSuzRmOzszqKRmDvpYhLSPUpc902uxPMYvoK1XYMUVNy2qjea8sKPaCa6m-eMXTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d00dcf8bc.mp4?token=CPMxbHlrUWXGadfz7N1IFNkUhrhVE135s1sK5tcoeSNeqkXX0mrKk6ZSaJYDSfxN6FBQduhW6VkV03DrHVkbeiQw23zHM5e7hZ_p5E6OLxXxJFFkB1SH-NaGcpItSrD1m8gSzy8fOcjf38c8yr-Nt8ThYpMPGdwolGfLr_qAPbaHoxlpMC0rlPlvIKn0Pq5R4jtYxwl0Nobaw1wu-PpEpOLqpO56Fse_TdufyCIeMShSgAgBVliFF_KnZ1GR0RPB5R5j3Q0FRAyqkNzh6FOeLfUSuzRmOzszqKRmDvpYhLSPUpc902uxPMYvoK1XYMUVNy2qjea8sKPaCa6m-eMXTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گلزنی کیلیان امباپه در بازی امروز رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103902" target="_blank">📅 18:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103901">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754c7f88a2.mp4?token=OykZYmEyAN2_1lf05NJUKD3YGqRvbPz1_Jnd7fB_nATUL456WTW_cPpD__8zDkF6FIlH0-Ke6aIxF1HC8aA9Dl4JN5I47aAWdhlLMlQDac6Ykolsedhexe98a9OzFVQ_KClyifhS-IXZgdKje8Tjx2TrPFPTEvFQnT2fQCAftJALzAUjdm2Goefum3JEr87TvWZ_AG6MhUoS52ZoHAoRSbbTwdizH46nGeUK6UJIK3khNkCJadAPfiobzzJ_WDQPtr7FDXoyCXgztOexAQG2KKXiwUDYPSlJLbYVjEYjhdvWopSCHLue6xHxuHDYso41IdWEDyayX8-_JzKTtiuz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754c7f88a2.mp4?token=OykZYmEyAN2_1lf05NJUKD3YGqRvbPz1_Jnd7fB_nATUL456WTW_cPpD__8zDkF6FIlH0-Ke6aIxF1HC8aA9Dl4JN5I47aAWdhlLMlQDac6Ykolsedhexe98a9OzFVQ_KClyifhS-IXZgdKje8Tjx2TrPFPTEvFQnT2fQCAftJALzAUjdm2Goefum3JEr87TvWZ_AG6MhUoS52ZoHAoRSbbTwdizH46nGeUK6UJIK3khNkCJadAPfiobzzJ_WDQPtr7FDXoyCXgztOexAQG2KKXiwUDYPSlJLbYVjEYjhdvWopSCHLue6xHxuHDYso41IdWEDyayX8-_JzKTtiuz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل کریم‌آدیمی در بازی امروز بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103901" target="_blank">📅 18:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103900">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گگگگگگگلللل سوم آرسناااال</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103900" target="_blank">📅 18:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103899">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56381f5fdc.mp4?token=n2DUabW_b70MJ188SJ-dnPcVR8cdS_heLcRVLxgUeCD2_yw_azh-BkXyYIIigiXbVt3Msd4wPEw4cx8nGEmfyjoqSgoyi5MZ6BLcFK9vfezizCBn11E4Vj6GAAAsVwrXz8MzzKZPxObdyY-nO-HVnCp8S7HTfFUeqd-3N5x0s5H3aZcM54BsytDso1N1iJEIzouby8Cn20IXE7yUCESog-VTA6EfMYokDqh-yM28USqLmFgct-SSVu7tzeKRClT8_Kk6RyRfsDggqS-y9w6JiiiQcijImMGe7D_ew2gEDDc-_YLLu9qoEdEd6Prj1cy9WmznSU8ZQKpNzmyzT-_MuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56381f5fdc.mp4?token=n2DUabW_b70MJ188SJ-dnPcVR8cdS_heLcRVLxgUeCD2_yw_azh-BkXyYIIigiXbVt3Msd4wPEw4cx8nGEmfyjoqSgoyi5MZ6BLcFK9vfezizCBn11E4Vj6GAAAsVwrXz8MzzKZPxObdyY-nO-HVnCp8S7HTfFUeqd-3N5x0s5H3aZcM54BsytDso1N1iJEIzouby8Cn20IXE7yUCESog-VTA6EfMYokDqh-yM28USqLmFgct-SSVu7tzeKRClT8_Kk6RyRfsDggqS-y9w6JiiiQcijImMGe7D_ew2gEDDc-_YLLu9qoEdEd6Prj1cy9WmznSU8ZQKpNzmyzT-_MuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
امیرعلی‌اکبری میگه روزم نبود بخاطر همین ناک اوت شدم. ما که نفهمیدیم روزش کی هست
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103899" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103898">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6oj6cKZ8K2RVchCMJiyn2ackZGbwA-W227vLvvXh2hZQ8Jz-wbcAse5vHHyRrL_OLXKqbdGQ3lC8PJVccaxlzThHhkPx0TAZYt9HyeUqKpDRRd0Dnf0_RXFGerf5lq2Xe4RH4xrXfMwUIPFQiBzxNoUc-5T7XyygaExK9Spvhj9j9hJ4EmfMZbYFjYGNfcWEw9DIosoKmtA4OWWwmPXCRLZ8_q9vuxw99wem8YTHdPQQz-e3BBnnEpLgffi_a3ICWE3MPBpDZ4NAfW1Z_w7r1XSENTdxpOCnWEUtiOH5IEFv14V5sU3ly8v7RrKSRZn3rBundQwjasc5NvbLi_BzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اعلام اسامی داوران هفته دوم لیگ برتر
🇮🇷
🇮🇷
استقلال - نساجی/بیژن حیدری
🇮🇷
🇮🇷
پرسپولیس - اس‌خوزستان/حسن اکرمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103898" target="_blank">📅 18:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103897">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3ab768679e.mp4?token=SphXLZhiSQvnhmHIzDhZorozf_1IOqvr3oxUxYbNkWSgKkn3udornisvCIUXaLUgzgBFNumtCXVg2Nb7rYQ3mrqLE8zKR8rqvi6po4f98y1NGebQR2G4AeaP37mkxWDgtODepXfq0YllyATNN3YakdBW25u0-1GD6C7mRxNfIzwH5nayYFitmk-I1BMylnpWSUBBjzWGSt1RQ3l7jda57KZvJnM9s8A-foRgu7lyXQ0G67v7BcVpuU9isAX9U9WI1NLrGAC2Fw-3pqO-bZOS5NXhx0aEQCn76QygsapXCh5Qp2uVNxGS-Dvd75RzRjMNBApTQYC-sBwL1kVyDnaC7S5ionPV1OFLcYn_4Af2sT2LeO7Tm40Ztt4Zf3H_yHWku8yDuK4UwP7Ewu0rPuAMpQ2SpeLYLq36QsoqHfSnk2_eUYnnD_htkfkrIqBzLQtbvOQUvGep9prwttZC4W_4-2ssJVt1qcwMX2v65XlMJC9gW-YT9dlPK2pjZwz85a-1QFNclSBTlAQbXcN2cub-5HQN5i0YRFRR4W6D-GZsrUg3BcR2lzEs7Jz1AmpOU8gz5EW9VAiYr7_vD9EttxxjB6baxn3gOxD44dwVn2v1Ue_xPd0ZpgUFmgypsxDIur16Q8dnrjLF235-MsD3ief8NCUBe74wkRiJL5gDe2s4x8k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3ab768679e.mp4?token=SphXLZhiSQvnhmHIzDhZorozf_1IOqvr3oxUxYbNkWSgKkn3udornisvCIUXaLUgzgBFNumtCXVg2Nb7rYQ3mrqLE8zKR8rqvi6po4f98y1NGebQR2G4AeaP37mkxWDgtODepXfq0YllyATNN3YakdBW25u0-1GD6C7mRxNfIzwH5nayYFitmk-I1BMylnpWSUBBjzWGSt1RQ3l7jda57KZvJnM9s8A-foRgu7lyXQ0G67v7BcVpuU9isAX9U9WI1NLrGAC2Fw-3pqO-bZOS5NXhx0aEQCn76QygsapXCh5Qp2uVNxGS-Dvd75RzRjMNBApTQYC-sBwL1kVyDnaC7S5ionPV1OFLcYn_4Af2sT2LeO7Tm40Ztt4Zf3H_yHWku8yDuK4UwP7Ewu0rPuAMpQ2SpeLYLq36QsoqHfSnk2_eUYnnD_htkfkrIqBzLQtbvOQUvGep9prwttZC4W_4-2ssJVt1qcwMX2v65XlMJC9gW-YT9dlPK2pjZwz85a-1QFNclSBTlAQbXcN2cub-5HQN5i0YRFRR4W6D-GZsrUg3BcR2lzEs7Jz1AmpOU8gz5EW9VAiYr7_vD9EttxxjB6baxn3gOxD44dwVn2v1Ue_xPd0ZpgUFmgypsxDIur16Q8dnrjLF235-MsD3ief8NCUBe74wkRiJL5gDe2s4x8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال توسط کای‌هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103897" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103896">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103896" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103895">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEkNGtnaM_SMUnLQYuAy93M0niQgphj1f2wa706yqqciusAbhBoDFU7qy1D5aWZUoF-TedQxPvPSzCzsM43QYZyessrfs_ARGOm8WuyZq71yHtc9vUV32iSmOEH1M492LWtab5CluLPp4Tci2LlT5x0jtFLg8hmR3KuH0netyAfzUDvcFPzQJ9vob7SzLnEfSzmjz25w1mDDcc6VtxduJxKD1BMUG_T_SCfjpuDHutOkNkBCLO2Y9LV2p0zM0WfavG6XfzEOQJ5ZdjNV36jiIcxZQ9TQ3D-awDJKAYOK2zpq7H_xnREuiIkKaqtHpAQUT2AIenavDoUiWMNgPeD1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g25
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103895" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103894">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلگلگگلگلگلگ دوم آرسنال هاورتززززز</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103894" target="_blank">📅 18:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103893">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0fc033ef.mp4?token=CgK-wchzeemHv1dd_U5nQT1E9rHpwFKz3StlsvV8NNbAsZNYejidu1SJNHsFEhT3IJoxlM0wa0kSB3flIKVV586VQ-6yxvzt62oo8dxEwC30PzzElCrRbm3hmEL-Jw9Jh-GjsQoXqM9Ru3luin7T8xjhfeM7UCks3KlLARPdNPWfTA7pmS2WO3rLGNIveo-jLG9YKG8TiSD79qHlyiyeOyAciKT8hA0KaRJDuyPO0_uGWWC52foGyeL2hLrSGeFleA1eNgCpUP4jMBkXqi2ohpYGqIktG0EpSem178scxf_cFzlSRR4mvrP48xkt-YdB74AhQkOhFeAJIJkeQ153Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0fc033ef.mp4?token=CgK-wchzeemHv1dd_U5nQT1E9rHpwFKz3StlsvV8NNbAsZNYejidu1SJNHsFEhT3IJoxlM0wa0kSB3flIKVV586VQ-6yxvzt62oo8dxEwC30PzzElCrRbm3hmEL-Jw9Jh-GjsQoXqM9Ru3luin7T8xjhfeM7UCks3KlLARPdNPWfTA7pmS2WO3rLGNIveo-jLG9YKG8TiSD79qHlyiyeOyAciKT8hA0KaRJDuyPO0_uGWWC52foGyeL2hLrSGeFleA1eNgCpUP4jMBkXqi2ohpYGqIktG0EpSem178scxf_cFzlSRR4mvrP48xkt-YdB74AhQkOhFeAJIJkeQ153Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
سوپرگل دیشب ژائو فلیکس برای النصر که رونالدو از روی سکو پشماش فر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103893" target="_blank">📅 18:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103892">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648b67b731.mp4?token=hfjwdVTez1M3KGhqRYi9WZq_EpYnk1o8TTXzcEEWghe6v1TKL9fhn-8Idh40NJ07an4gocEdxbzlBMMs2SxDjaMTSWk4utWP_ezTeyNtB0vthubii55rpPO1A0UsxmpAgaP6_BltpH8gnt1SwYNNgTz6LD2nLkSE4JCvGJBV7Kcfdaz_vuGxkV8igGUdkPg79-wsn4pModXF9BpZY3_qXZnePwLq2Jc6YykbgB6bfUS8l1F7iewV_sL_eDlRIdjaRbU1G-h8-WIEzZVKLQKz8GI9x2KvBBfZ_C303K2JN511CmD9-3edePVqiouC2mvmwW2A8hFeHY4UspENQWtmpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648b67b731.mp4?token=hfjwdVTez1M3KGhqRYi9WZq_EpYnk1o8TTXzcEEWghe6v1TKL9fhn-8Idh40NJ07an4gocEdxbzlBMMs2SxDjaMTSWk4utWP_ezTeyNtB0vthubii55rpPO1A0UsxmpAgaP6_BltpH8gnt1SwYNNgTz6LD2nLkSE4JCvGJBV7Kcfdaz_vuGxkV8igGUdkPg79-wsn4pModXF9BpZY3_qXZnePwLq2Jc6YykbgB6bfUS8l1F7iewV_sL_eDlRIdjaRbU1G-h8-WIEzZVKLQKz8GI9x2KvBBfZ_C303K2JN511CmD9-3edePVqiouC2mvmwW2A8hFeHY4UspENQWtmpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول آرسنال به منچستر سیتی توسط کالافیوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103892" target="_blank">📅 17:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103891">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آرسنال یکی به سیتی فرو کردددددد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103891" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103890">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103890" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103888">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcoa6bEzT5WDhopbW9TU2WxkzXLdkB2HdOgfcYdsMWVNAW8VX-6u4OZxOyCK-mnugcML7EpO57nrBEp2hYXd9TDGBNZsvxH5OKhNGTIgNFcT6RuKxs-p3DCl9GMSmHxVFqXg-mhTAQXo4_sd_0w-NYkw_QMWeB94O5XDUkbnC-HPLMNbY9J7KzuTULGc7PHvseSOJTtVumiJriFq4F_HeDynmL32Kte2OJ_-2H_3GMO06HMDuFxf1xDm4DL0tDPHcpvpPt6zsUTQ8r6HzekSxWwGCdqoqICYlP-z2Zsw6AnjufpiFnNCUrzMEROwdnQkxTiLYAodysjmEeBIBPnFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZnzkiYKhhSExkT0A5EuwOtnCRq0_nvNxsCgQ2kPiw-32e3BKrJMQV5oF6ai0URjGj8TW6sMAKrm9TtavBewOj5U5GhzrjdHPB5DqxigMFDt2dXJZtx-GnafO22yGFVO8iiRTduMIPOGbdM5wVn4fsPoO7Lxkokk8qGDU5A-TWciHqfsv56ZCQjJALDmtkSLrJ--sx_HSia7gmBgVcOalvsDDekx4hXpIDIYw4GLHirc0QmDMTgFiUiDYS5w7NnRTrz7XlIR5K7JzVeuYnzMfjxD407V0qou1RWgj_8r_ULtdaK34PueAF1ybGGCnOtXd1rlgHLBPjld7ODmmYXKMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
ترکیب رئال‌مادرید و بارسلونا در بازی‌های امروز تدارکاتی مقابل بازل و شالکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103888" target="_blank">📅 17:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103887">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2aced863.mp4?token=ZGTYw1N6l89H7zfW2RYJSxszfq2E_ZNwkE7xrl2N0Q--GX3tzFCPFqazNiJixmbuY1XiOQ4nfA_dfP1yjiLNNjmLReWcTmDKQR8SjJka26A04rqkd0rcmk1m0oibE2G1u1jtej8O1Hpe5JN55PbhgyVPJhWT9Z22G-b9KtokA6tujH1gOZ04ANOizOua2s-0zwz6CZO76x8-0S8QjtNBZ6AEL4rDunm_FeaYdC_-uXpu-cpokeMwXVNOU71PIzSmPJp9VkJ_Da7twEXsX1RnKHhrYwu9XQ3bwLYrUacZRJ5DNSTFlq1FSGcT-Y0MLlYaKkE1wVgaCl20ERd2oTsICQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2aced863.mp4?token=ZGTYw1N6l89H7zfW2RYJSxszfq2E_ZNwkE7xrl2N0Q--GX3tzFCPFqazNiJixmbuY1XiOQ4nfA_dfP1yjiLNNjmLReWcTmDKQR8SjJka26A04rqkd0rcmk1m0oibE2G1u1jtej8O1Hpe5JN55PbhgyVPJhWT9Z22G-b9KtokA6tujH1gOZ04ANOizOua2s-0zwz6CZO76x8-0S8QjtNBZ6AEL4rDunm_FeaYdC_-uXpu-cpokeMwXVNOU71PIzSmPJp9VkJ_Da7twEXsX1RnKHhrYwu9XQ3bwLYrUacZRJ5DNSTFlq1FSGcT-Y0MLlYaKkE1wVgaCl20ERd2oTsICQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
عملکرد ابوالفضل جلالی در اولین حضور فیکس در ترکیب تیم‌فوتبال پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103887" target="_blank">📅 17:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103886">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6927287d81.mp4?token=hlveF5DQHl2Ddxfm2-BNanRqqBFvkm55WTAtkjONP-c1wXha_v2sSdK1ybaud8yb0Zxd52R9uhgMfbrRPqroKAJab7tITknOGAhT_vu2T3CCeZqMjPewgSg_87BVOpsMcp2SVzF6JGDNL1PeH__VnmiWMkIDrlc9nQoQ1uNfxiX1ENrIVosoZfT3k-R0vUJLhIV_gKfjS5epS8_7TsAzChdptvQguDJgp5WHF8g97zq72jzumS35uH9eXMB99wdbN18B9gbayigCh7hp5EoQNVXDJMfMit0hdOGJU9EUTF47t1uATqh26kBBl0aYt9gTckDa1V-8avzyPeUbIzhI7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6927287d81.mp4?token=hlveF5DQHl2Ddxfm2-BNanRqqBFvkm55WTAtkjONP-c1wXha_v2sSdK1ybaud8yb0Zxd52R9uhgMfbrRPqroKAJab7tITknOGAhT_vu2T3CCeZqMjPewgSg_87BVOpsMcp2SVzF6JGDNL1PeH__VnmiWMkIDrlc9nQoQ1uNfxiX1ENrIVosoZfT3k-R0vUJLhIV_gKfjS5epS8_7TsAzChdptvQguDJgp5WHF8g97zq72jzumS35uH9eXMB99wdbN18B9gbayigCh7hp5EoQNVXDJMfMit0hdOGJU9EUTF47t1uATqh26kBBl0aYt9gTckDa1V-8avzyPeUbIzhI7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
تمسخر ۵ سانت و ۱۰ سانت امیر قلعه‌نویی در گفتگوی خداداد عزیزی و مجید واشقانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103886" target="_blank">📅 16:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103885">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5zXh8-qGWsxccOao3MZK6jeL6POYF70YibiQQGCu4fU_b0gkhfexP7GTsDnjs7nL1RLfI6-uRem6pJJc3J3M_RJwGtaYfK5Wt_TMgSRMlsjSkv1ruaJETnaT5t4pRTHKH_p0dzQ-qmyppP_Xp3mLBH9zQW9_q6ZBzreor7o0xnpj3jPkfBKg-yIPkZvRpgxwAkyLRNUs99Q-ECrMPoN-YxZEK7X3RqrRXyqFEsDpHEgLSI1sGf_YK5q1oBjlbJn2rvrklhhrLDBxR_4yJonvYGxxfcyYjEvsyRtpa5CaJVG8eWPV8NVyUT1akPDlCPhA8YjBAjXncBpf8vWS6fJSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
5 مسابقات اخیر بین سیتی و آرسنال:
آرسنال 2-2 سیتی (2024)
آرسنال 5-1 سیتی (2025)
سیتی 1-1 آرسنال (2026)
سیتی 2-0 آرسنال (2026)
آرسنال 1-2 سیتی (2026)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103885" target="_blank">📅 16:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103884">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248d4f7bea.mp4?token=QxpbyYIhHLe7iuX0_6sxXMZjAcWRWnTcbqPfvfiY6BzIW1NVn-HHTfXhVl90tAJK595FQqU6tLfAI9XZjvE4d2gwz28N9zkpTZti7kavMB631ogyaDcZRzedYbRV3M_396AfeWVstbHXivpouFnJYca8maTJnNPmyG7Qhi0KYFaXxXAT0RtHJRxPhjbr9S5xhqcJjgQAEIlZmxDhjbWdeNx_osOckQA4vfQFokbiNoQnHO17UBpK7YoZ4HpDGEO3AI8ljclijC87n6-S-tTPa49TOHMmoZs3tjLNr1lgOmiFhsDu2ZfBNPJh9N35AZrihLXVY_2jjLr7X6CZLKUq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248d4f7bea.mp4?token=QxpbyYIhHLe7iuX0_6sxXMZjAcWRWnTcbqPfvfiY6BzIW1NVn-HHTfXhVl90tAJK595FQqU6tLfAI9XZjvE4d2gwz28N9zkpTZti7kavMB631ogyaDcZRzedYbRV3M_396AfeWVstbHXivpouFnJYca8maTJnNPmyG7Qhi0KYFaXxXAT0RtHJRxPhjbr9S5xhqcJjgQAEIlZmxDhjbWdeNx_osOckQA4vfQFokbiNoQnHO17UBpK7YoZ4HpDGEO3AI8ljclijC87n6-S-tTPa49TOHMmoZs3tjLNr1lgOmiFhsDu2ZfBNPJh9N35AZrihLXVY_2jjLr7X6CZLKUq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رامین‌رضاییان خوش‌اشتها
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103884" target="_blank">📅 15:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103883">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b623d393f.mp4?token=KK_5J03YoZiD5ESlouce6hd7vH7ADwSrvzjEdh0xyF9vA1jAdGUJWExYEKTvFIeNhFvue67F88jOGlmSk2Ulh2ob0P0Ll442JFw400gXRxRx-_tCS_I8Lsu58__I_sr73B6o8HiUDOXDiFA9ZvRtD5hWVNY2yEJHUcIfiavChT0uqZcvscEuXiv6BlYdtEpkMMtJaCcKELo4qMXrTPC_KV5AtQWMD5TLsIBIH59m_3711KDZssCRUEaoHdlqLgGfmXYZg_pYv6LvIvya8AfZtTR4rBEFReIU_jwd6uMjubpGVOifCGk7sREgxbxcRyskNvaTga90tzIgjt-Jy1QS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b623d393f.mp4?token=KK_5J03YoZiD5ESlouce6hd7vH7ADwSrvzjEdh0xyF9vA1jAdGUJWExYEKTvFIeNhFvue67F88jOGlmSk2Ulh2ob0P0Ll442JFw400gXRxRx-_tCS_I8Lsu58__I_sr73B6o8HiUDOXDiFA9ZvRtD5hWVNY2yEJHUcIfiavChT0uqZcvscEuXiv6BlYdtEpkMMtJaCcKELo4qMXrTPC_KV5AtQWMD5TLsIBIH59m_3711KDZssCRUEaoHdlqLgGfmXYZg_pYv6LvIvya8AfZtTR4rBEFReIU_jwd6uMjubpGVOifCGk7sREgxbxcRyskNvaTga90tzIgjt-Jy1QS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشی داره تشویق یاد میده یا تقه‌زدنو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103883" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103881">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXwNWZBLKZvmqIfdCcT1wCqvJsYUbz3MbXa82NoNvRJ_uPxdN9PY93tEGv_gjY7JcbW4YTavPCuB1vjz5VXPLusvnHc_L302qn2w3kC-Rs2vaE-mJeFUlodgS5adM7XKgivMOZLyPaJpAZFDdR6J_wndl5kYdWoY-33TqIhTi0dHJOkuXQMxgW_f5yZJZ9g2T68zn4GmM7zT6oDpbF1ux-OI5qQ48uM00Jjs7qdJE5AgRHVsw13QEdODlq35rnmCizWpm3TBX0ZYS_C_GQMp8L3LVbsiodXsHnNPPip3DNQyYLki2fwxJZkGZYMn_BKxHJMEs_uCpxUXFEyOU81ayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q64RpEwc-qX9Tx83C_0RV7yMxzjC0fk5lXBlEodDer2A2kq7ClaZbSuIy3aqTp_59FgkBwPlnIbYrKvSyxBscg20QrfqlveF7dhfeuKssRIfZWJL49_b-QbtxyCLbDs9OI3xPnfRcYmfpzQtGJuUTdc7iE-AWMZ0EZn8AkF5IwDmHtwGxQky4JW_20-HHmcCTNLQ47LtSIrDFAFS2CqfqzV2BHUUwkl99pK5YxigT1YXc7Swc7U7LsGAFfgAta2HX_F-gqFDcUlQtu2XWb22Gtf-ety_I8U2VFcvGHbB31qZJCi2KbrPnrHw1x4rdORAz_oOpO1Efr_9c34UY-S7Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😐
🇮🇷
عباس اسماعیل‌بیگی لیدر پرسپولیس درحال یاد دادن‌تشویق وایکینگ‌ها به طرفداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103881" target="_blank">📅 15:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103880">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP311GYroWRpguZ4PY65duGFF8Fyo98ngzU7BVTwQd3LZa7la8CzOwWHBqs_bawPgBkjcnA9feOk9m-IUnymT-j0hbtupp9axIUv3qox-H0HdcQEvO5tPALRbjn50ehcwdPFkCKCGnIw0cR4s8-pJ-OuS3K5ASZUIy1fqUTn0ybN1IZRVLcD-FCQpFbRpmi4HeyoUs_iuQPNQ4CgfyHpZ1DxSLLcFi2ZNSL6r9kZ8izXtXCloE3Av9M1r6XuE_PxNrhy34D3KXNOZL3CH8p3Tpbx-Il1sE4Qr2bgR9ncM9Rtfjcw-lQ7y5wFM3Hlu0gUjewsywcQRpFAcQ-HQv4z7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فرهاد مجیدی پس از گذشت ۴ سال حضور در کشور امارات ساعاتی پیش به ایران بازگشت. مجیدی اخیرا پیشنهاد سرمربیگری تراکتور تبریز رو رد کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103880" target="_blank">📅 15:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103879">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLCwaHbFxaBrkSbJA3MEbadhyC3BnjW2g4x5EKYQTexNKqqNRL9H2iAgKwO2M6P0XKah-4yb_7vSvliFJqono8cHzYey3uf805I8CoYM5Q7dkPsM5S01smlrL7nMC6k1qLfcf9V894FqCwamiigt0kaZ9jT3Dv34gj4uerg7vSdOp3l4Zdq9yl_HtZrntMS9YTl0cJfNui1bOPDjNTkc6QJSPSlokCI-2JEJVGW2mOqwhLBQHu-LBBdxxph6e0wtmY4MrSdRvEipFCHJZm8_-urVf_KyCWbeaa6yxgYKDnRrOf1j1a_SxXvrqbFoZ_nT0kZxML7G5T4QNUBIL3SQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇪🇸
#فوووووری
از متئو مورتو: ژائو کانسلو با عقد قراردادی به بارسلونا بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103879" target="_blank">📅 15:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lu-n3GUMsf4RsZr2ptxlP4lMfvRoEbkItIUp9xRQYQq8VLw3T9C2dwVVrHdihWYaog9fNCjs2tCgbvlrUJoY7Qva2CW-DrAOSn9SqUi7NO4dG4RA6ylfQomeWk268473uKRYJx11td2aFp0soFFmE7xZ3zNiNkyk9Mz6nWwRB5m0vZ7sOLvNpuOSTws1kCYm3fCAQH8RZJ5z52Faqe2tR-iJIslen8FZPZvIbdVqx4z4a792JbSH60RieQdFXlaYihW8cMrARIVJ8si1E8oIc0GWGdGT9t-Krywoh0CxiUDF9HNUAvvW1HkVkR5QR6CvghkaeRsHmtfP0f3Fou-e7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCrt7mDL34hsBaOkCUX3_JtMsyt5KYsGu2Ac-zY1q_zectVOSyhQkRL0njDIzFUT8G940fClGihBuFUQR3ukviiIqAMewlA9kiHa87xguTEyRORKrgUlNvQQ73CJ16H1TaFn-k2BUqISbT13OH2FOL-2EYaibdOI8-ggJq2iIWnfn4NnG6jfLoSKOzZy64lgjYLmRszRfZDwZHCP5GJXs4CQJ0GiwMbPBpUapJvuAJYif1cFqspvpKC7JxUcBdRoUacD7WreQY4C4IzawMrfoaLcrT0N2weZlm8IfdI5MiYj4YsheCLbg-aGW-NmR13ntBKcl0_lDDjYzS2ovZUmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezsXJ-qBUsXr6N72jx76GpdYpfTytCbsckW1wbJL75NkvcR0VsLceSBWnIdEQcyj5qgTFB5nvawv55oLcyqNuqCHYi4mb5id8MSCIZrWakNdjnWB_cowEfN7r6LrmX2RaYTozQL3In4ILRpe_xm56UOZmNTqJTLByxJvaSE7QA2ITTnzlGPHmfPfr6aWcWQjFLsnx-k15m5EQCK_r3OYBLjVJlkUwCB40DVYAo3DSYyv4vV7ZN_QfVb5LJ9vfmOg6mP4Pp-KgV-vaNEJCPAnYpAVY0dxDA-VzEKMWAJt4m0gUYUkPKo9Pvp8KL1goPiXxgkaAo9ZHKWyzC4tfDleGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😢
⚠️
دختره ول‌کن رامین‌رضاییان نیست و یه ویدیو پر کرده حسابی ریده به سرتاپای اسطوره اخلاق و مردم‌دار نسل فوتبال فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103876" target="_blank">📅 15:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5Wf29OCPSbsoilELIl4lNKQfrFV51lijmnUywExksZmqRMopBfQLE-b9xZ5ASK42v9qrpZMQ6sYcO_pDFYgF8Mae0JsPrdL792CdOfTt_gavNNwT7iShFzxw9KgV3ZNS_a0vH-p_DQHGfiQ0Ej6W5bhJwExeGuoBiP3bdFyNj-VjINGaQ3_YRzb3JZw3L29qgqjTIvps_WBR8Ad2UqzlXN73eStBGkudwRDmVMkIZzOmhqVvC56UNRJyAe-Zx8vX0mvVktxjzHt7L21HPweJjq7JECp4yh-nouyUYwaExLQqjyIPOrko4ULYOHrhSWAm6gBYnQPUVQBp_Aq6spZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
غیررسمی؛ زایان سوزوکی دروازه‌بان 23 ساله ژاپنی به استون‌ویلا پیوست
💸
مبلغ انتقال: 30 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103875" target="_blank">📅 15:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccfdc09cad.mp4?token=TQaaYTSpmnViRA3kK4gnafaoD-PQBbPYburCsEK4bDKC0Ubre_bXnp3x5lC_3LLFOtLaPAa_GajG_h62dopsl7vWV9RbEdiOJ-30R-HO23LvCG7kZ59J0J_B03_3acvCQiEJanb3ghNRupTZQ3vVNB_1iaFFSR5Db3dC-xaMvI68SRbk0xl0mH5IYwlEIwOAyv2z2ZVAkqdMjDpnq3v91X5p-NDZ-ccEuAoqMx8xiwWlGG8gWKRgWPCMQTWFZyNTW3QfGVGdjmwaD2Po66iXWZzynAJJ0bqzUa8GjPKuVQvMuk6N6k7ahpzMIiHLb8wh96gQasmloDaTg8-rX5ciKwxp1OZovcrJPjulQKa3i2KqnUT_ZnlZJGchMjxpobRWhXl2iLaoO6DLgvw3axqdAQDvR12nnmadUlT7yDc9_L8bckuA0FOjfqtED2KLUdo441kz7qRxak43dx0lrLsGe_3qEZY1uRuIwK-5mlfGxahwlUkQ1jbeDyEUHN1dwH5Iqg4TUIGi_lSaEZyPhEicq4Iw5U7sXx9RvcNpT372C4AjwBCkpZU6aLIed2ha6tIt2gRpwjmm5O0OpIiZXPGiAfCagntYodzo1TrgS9uzXx-znNUqBxaSB6BfStRmztIZkSgdelEr0c1lZW6Xv2WmxHxLtad6nCCCWn3FMp6GozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccfdc09cad.mp4?token=TQaaYTSpmnViRA3kK4gnafaoD-PQBbPYburCsEK4bDKC0Ubre_bXnp3x5lC_3LLFOtLaPAa_GajG_h62dopsl7vWV9RbEdiOJ-30R-HO23LvCG7kZ59J0J_B03_3acvCQiEJanb3ghNRupTZQ3vVNB_1iaFFSR5Db3dC-xaMvI68SRbk0xl0mH5IYwlEIwOAyv2z2ZVAkqdMjDpnq3v91X5p-NDZ-ccEuAoqMx8xiwWlGG8gWKRgWPCMQTWFZyNTW3QfGVGdjmwaD2Po66iXWZzynAJJ0bqzUa8GjPKuVQvMuk6N6k7ahpzMIiHLb8wh96gQasmloDaTg8-rX5ciKwxp1OZovcrJPjulQKa3i2KqnUT_ZnlZJGchMjxpobRWhXl2iLaoO6DLgvw3axqdAQDvR12nnmadUlT7yDc9_L8bckuA0FOjfqtED2KLUdo441kz7qRxak43dx0lrLsGe_3qEZY1uRuIwK-5mlfGxahwlUkQ1jbeDyEUHN1dwH5Iqg4TUIGi_lSaEZyPhEicq4Iw5U7sXx9RvcNpT372C4AjwBCkpZU6aLIed2ha6tIt2gRpwjmm5O0OpIiZXPGiAfCagntYodzo1TrgS9uzXx-znNUqBxaSB6BfStRmztIZkSgdelEr0c1lZW6Xv2WmxHxLtad6nCCCWn3FMp6GozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
به‌بهانه خداحافظی چیرو ایموبیله از فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103874" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRUCH8BxpKQf9dKOkPOqXoiX1OvelsqIEn3F2nUzFVnIvHJFNxZlnYig5Bu9fLg5Ts3rl2VfYf-fta-Pza8A01LW-Vxm_DlXUrWVX9AQcnD3Lx7HUKCo73oqL7I7_Uc6YU9rz3yn9QvDLeZGJdNt3G2W3DUgMIZxTqJ2BVtwhlhanGVoG970xWw_DPAAFFkmNjuBrccG2bAJH3Hzokqz1TSQPwsb428qbZ48_Sp8U5tG-wRJFlxCB7oA-vSPzRSyFLmDUEshUNYuuqKLwi_VD7W8sBcAuTLNj_F9KYxwCLp516y88tMNhw2rpkK6r_gy4ZajFqaJpD25iPPUU_ULCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار فصل‌گذشته دیومانده و آنتونی گوردون دو ستاره جدید بارسا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103873" target="_blank">📅 14:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794f2f910.mp4?token=NH_-n-OKNTLsevhslzRdCGgt6cDnb_DstLPkPgwvxsdGVq43bLEFC0KPdc2tzYqTkUpegbMYpxqHhwUMz2ukjLWWDiCvnzKXdppnoPW_U0o6cdTHejUEu_og7gEhGNWHqbGiVBOi87odQYeDPszrhJekCLe-3Cqp2RCs7vfXrN_Xadpl5RI6Ha8QgKx7gEzFnIvBROXKmeH6-fiOFcwtPRKa64DPDOasj81WiOMgRevz4BbhqXuvEegwIdbeIfeBhb3oiPEB73tV_c89xIYrWS3LFCJXh2gHu3Sxy6Y-io1YoTiLakyz5dJC0PdnJGoH2AORDOmpki36lj2uXdw4Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794f2f910.mp4?token=NH_-n-OKNTLsevhslzRdCGgt6cDnb_DstLPkPgwvxsdGVq43bLEFC0KPdc2tzYqTkUpegbMYpxqHhwUMz2ukjLWWDiCvnzKXdppnoPW_U0o6cdTHejUEu_og7gEhGNWHqbGiVBOi87odQYeDPszrhJekCLe-3Cqp2RCs7vfXrN_Xadpl5RI6Ha8QgKx7gEzFnIvBROXKmeH6-fiOFcwtPRKa64DPDOasj81WiOMgRevz4BbhqXuvEegwIdbeIfeBhb3oiPEB73tV_c89xIYrWS3LFCJXh2gHu3Sxy6Y-io1YoTiLakyz5dJC0PdnJGoH2AORDOmpki36lj2uXdw4Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
روملو لوکاکو: تلاش میکنم یک‌ماهه ترکی یاد بگیرم، سخته اما من زود یاد میگیرم!⁣
⁣
🥶
در صورت یادگیری زبان ترکی، این هشتمین زبانی خواهد بود که لوکاکو به آن تسلط خواهد داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103872" target="_blank">📅 14:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32096c018b.mp4?token=Z9u6LZl9cnnckcjGgW87b5ECp6PvBARRsvIdg-Gut4xCGEf7Q8XW-b0UApKI6Byw_db0MukquCz-lIENVJBzjpgYV7bDDi1q06PXji7o2no7eWDv6D7haCAX-7wZLK2rUpdx_emcJhHT19hsmMaqpZ8JbZh7ivSS4_A2tG1xbYdTrmUsLxkWkx0lYPn3yxyyBfNU8XqRAJ4uS_mYbZsVeCePeYhkqhwnOatKhQ8y_EeuoKtxSj3ygJzgyznY08EXp5YkOF_6RxUi8M1yFoyxAGKJo2ivKBzEDQL3ylb0hvxcQdmdEeK49MAq3FaDQDL4L2YRl4g6P1egL8OBolejGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32096c018b.mp4?token=Z9u6LZl9cnnckcjGgW87b5ECp6PvBARRsvIdg-Gut4xCGEf7Q8XW-b0UApKI6Byw_db0MukquCz-lIENVJBzjpgYV7bDDi1q06PXji7o2no7eWDv6D7haCAX-7wZLK2rUpdx_emcJhHT19hsmMaqpZ8JbZh7ivSS4_A2tG1xbYdTrmUsLxkWkx0lYPn3yxyyBfNU8XqRAJ4uS_mYbZsVeCePeYhkqhwnOatKhQ8y_EeuoKtxSj3ygJzgyznY08EXp5YkOF_6RxUi8M1yFoyxAGKJo2ivKBzEDQL3ylb0hvxcQdmdEeK49MAq3FaDQDL4L2YRl4g6P1egL8OBolejGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نونو مندز یا کوکوریا؟ بهترین دفاع چپ فعلی دنیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103871" target="_blank">📅 13:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2353879d41.mp4?token=BhyBJZAc2VZi_9w4KsqshEEyu2xSU8kdvZI0i16DTrpVJRZea8kIJ6UWseBplxOZ4-0U7D-1o06eYdCKw-jzD_-Xg0MGWAL4XM55-0OzdAjQv3WuISw29kDBh0MN0VQh5bsqarcES0k0LRnCdf_5hR--8YT9K1gQr6hXgH5jT-8t21YkMCS1uEHPS_XbKs2ycY0czi9r0zXMI-ZPJGfn82A2zLrstmU3uj8qvuib0QazGqXVuJ4qNak_x5MgsQf6WOT8Fhqa7wJRBWIXNqx9OHPJAY507BiDPFV-soYDydQceeOzddxrQYuYa1vvXzdAOcExwm-nCt7oGKzjunwkjKo0ifffufnsUzE-s47as8YWc-H25xQqQpEQujEWD9qk3ZTbAi6PGb2a51iocr-9EeCY0-kW7eH9prBYTOfQQvk5KLqDrD-KFhS33pu9JS4Zj0sd8FiNQE0FSomLOOq_J_PyoXpyB3TEQN3Dea9xBi7AfUKD0c-1L2basR1AXbru2ZZfix1tymRGr8HF5MDbSYgcDd_JjC9jPoCkeu3Y22kVWBs2C-1Tlmo56Upi36j1pZTC6gRGBnQ1EJfe1r8MBPWn3bPOB8UHsiAywwfFscXsQeIjoC86xPLeeHxu6ai4eLqpvqF4Y9dfpwvAUewvAM86aLUAdHuv8MWEguKRDS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2353879d41.mp4?token=BhyBJZAc2VZi_9w4KsqshEEyu2xSU8kdvZI0i16DTrpVJRZea8kIJ6UWseBplxOZ4-0U7D-1o06eYdCKw-jzD_-Xg0MGWAL4XM55-0OzdAjQv3WuISw29kDBh0MN0VQh5bsqarcES0k0LRnCdf_5hR--8YT9K1gQr6hXgH5jT-8t21YkMCS1uEHPS_XbKs2ycY0czi9r0zXMI-ZPJGfn82A2zLrstmU3uj8qvuib0QazGqXVuJ4qNak_x5MgsQf6WOT8Fhqa7wJRBWIXNqx9OHPJAY507BiDPFV-soYDydQceeOzddxrQYuYa1vvXzdAOcExwm-nCt7oGKzjunwkjKo0ifffufnsUzE-s47as8YWc-H25xQqQpEQujEWD9qk3ZTbAi6PGb2a51iocr-9EeCY0-kW7eH9prBYTOfQQvk5KLqDrD-KFhS33pu9JS4Zj0sd8FiNQE0FSomLOOq_J_PyoXpyB3TEQN3Dea9xBi7AfUKD0c-1L2basR1AXbru2ZZfix1tymRGr8HF5MDbSYgcDd_JjC9jPoCkeu3Y22kVWBs2C-1Tlmo56Upi36j1pZTC6gRGBnQ1EJfe1r8MBPWn3bPOB8UHsiAywwfFscXsQeIjoC86xPLeeHxu6ai4eLqpvqF4Y9dfpwvAUewvAM86aLUAdHuv8MWEguKRDS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
ادگار داویدز: زیدان مثل یه جونور بود و با وجود اینکه ستاره بزرگی بود از زیر تمرین در نمیرفت و پا به پای همه و بلکه بیشتر از بقیه تمرین میکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103870" target="_blank">📅 13:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1863d1e5.mp4?token=sMNXB_8VgPhxlhz2tAIEYK3-V60BLGZHScnK0DqhyFEO0OCD4XLn_gnGHplw_OShhVpVmGzvfaYvSopCTRzAEGJlbkcWiucFEsedTrUdaz-T5PCrNY14t-c9xOa8sKAVjNQgNDKsLZdZSSFpZp0WRCFfLfyorswjyqe7q_hX6P0msM2IkNs9bS7yJrdQPdD74YYujo8YbpbPXVQM8CljHQOfj5IFccvyt7SYSNh2G6msLquCW7TVXsbyCliKoSkqWmjcZg8isij-AIatHagKC1Cqi2CFOe3R0_MrF5lqF2X-i1RlMjvwQ8bj1HN-uSKmNf9UosAvPRVIGusR4Qefzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1863d1e5.mp4?token=sMNXB_8VgPhxlhz2tAIEYK3-V60BLGZHScnK0DqhyFEO0OCD4XLn_gnGHplw_OShhVpVmGzvfaYvSopCTRzAEGJlbkcWiucFEsedTrUdaz-T5PCrNY14t-c9xOa8sKAVjNQgNDKsLZdZSSFpZp0WRCFfLfyorswjyqe7q_hX6P0msM2IkNs9bS7yJrdQPdD74YYujo8YbpbPXVQM8CljHQOfj5IFccvyt7SYSNh2G6msLquCW7TVXsbyCliKoSkqWmjcZg8isij-AIatHagKC1Cqi2CFOe3R0_MrF5lqF2X-i1RlMjvwQ8bj1HN-uSKmNf9UosAvPRVIGusR4Qefzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
بیست‌سال حضور احسان‌حاج‌صفی در سطح اول فوتبال ایران با پیراهن سپاهان اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103869" target="_blank">📅 13:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103867">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jR8E8rAkI2HrMtZLbaOj1MPXIB34hywWbISbqIF9lBWPCzVlM5VGgaA-wryq_5X8LsU6oX95ax3Kbn-r7jwDVD5U_3sXswxRPIE8eC0Zuaq_AyP77Y-cHP5F1nnY0UghYDBVRNkGo5aOdr2ng25Q8fiKJqtFcRdQToaB0sCcGcJcaq4oeZw9ecpSPhtiLYMbbCtfE4Bf31WMTDp98myxAFnnw3Aq5FHVqqxfmvr4WpLI9w36cHJQcYci0CbAHQH3SEx611kqTY2YGPj-I1-8m6Ev5LFCO4-Q1f-RNcI9dwp39TWJg9bknAGfi2KsCyJuc1sXai05OlxdGvD-CLo2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMlEsdhICekAwh64wK2wj2A5yg6nuAM_rsq6bhjC9y8p7w36O0eoR6oL7WfXXXKxmTBvmCVZtaFXMeGkhkXtkHjHWcY8G4NSKPhSqNK3R5zItbJHUp7gLx0w4pSJgnN6jwkR0ucqOgr0rdIwi2GDvq8dNuTn3ag-XDg_XTUIKdqBv2SjUES1RxXyG5krB8eNMdeWJ-0_EVteWM05XvTjSZSHItS40S9ldM7xgs0EIFCCVltY5o6aahw0Sx--ycLq7dlF1fozS2pfiAWIWH8lHqIsxbktOSk6O_6k9uGQxmBvyvC_CNeQMGP8VOpt02owFpdc0NQl0HW7BOIcZgnYIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
اکس رونالدو خانم ایرینا شایک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103867" target="_blank">📅 12:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103866">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMcB6sqRrkbYs6QYOoBB1O4RRh2OTCAWnGih9a5GxiS0GN8v1Sz0dydRhipJv2AE2-X3xuKtXve5LTmtMzvqIBOwBTt78uQ1ThXGVLTRA0VHDKN4akEDBKMHzRTCD9Bd6SWsRI8JFEQrCFysjV6zYwTmRHrHGxj9itBcJwPbqwPT0sxd81ySjskSpdzHyykmho2ehGb7KkXRlTN32t3HiDd6ToZDhMsYm4k5FRJ6ghvMlLq_0WzKzbKpU0gKVzkWh67SNmMYsQkr5Xjg7R25AGbIKiAQUEbz1qx8Dvs597vTqQTadXNBfW_JV416a4OrcS1t_E0QmDf0Kpn3iiiGVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از نیکو شیرا: قرارداد برنال با بارسلونا تا 2031 بزودی تمدید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103866" target="_blank">📅 12:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103865">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86eaeca4c6.mp4?token=akiLRK6PmTCXskeeRCn1vA9M3ETYPt4K0g0IKgMnd2lpBvDio8qDTwSi855v8X_EM6rKuo3hkLHmMWtaKmWR0H3j1c9ekNDEpLbfz0FOJTG5pDNkiilC1hv4ktAFj50xBG35pxTf916-67UTXj6JJj7fy9LW33rWPbKde5-YmR5PEcj7Q45kM0uwzgIU4Gh3zWP3WAkzen_bHTFhCG-NPTmpEWMW8AVJMzEZaUddVVnPOKNxF688u3R2zlqGjlZX3Xapq1nnhlDOQwiOLUqW7TRV60fw9VHPpTBRXbZEL_4B3s72-9FjoehKwYnS1alwAE-SgyhqelbjrikpzW6N8TZHm6g36NejdoCkfF5b5s0_BUrJv0XXbvxCz_FFoWbm4BCjaNV1L5gBUx9dpOvpgvX6_r3tp1YV3I0N96HWJegS7957M9oCuvee_0vw9Zf7TZM97RDoufDMWwsQmIVmn0fqIE7Pn_jhgRNcQvpP1KOozKzD9-LakSdiY541fuQFy2qgQxOqPMGSMJTG2V4noFBBTj2waGaj7q6DyrOkFIjDl-wgCdWD-mmtQLn_lHzXS99RamS-6fKRYH17T8KZsceozORw-njemJcYNa3QwsyhiefArWWl2iOlOT9teHnXtbWsift2VULWsI8ol9rfbAAAK8TSevdre1_MIRS2Dps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86eaeca4c6.mp4?token=akiLRK6PmTCXskeeRCn1vA9M3ETYPt4K0g0IKgMnd2lpBvDio8qDTwSi855v8X_EM6rKuo3hkLHmMWtaKmWR0H3j1c9ekNDEpLbfz0FOJTG5pDNkiilC1hv4ktAFj50xBG35pxTf916-67UTXj6JJj7fy9LW33rWPbKde5-YmR5PEcj7Q45kM0uwzgIU4Gh3zWP3WAkzen_bHTFhCG-NPTmpEWMW8AVJMzEZaUddVVnPOKNxF688u3R2zlqGjlZX3Xapq1nnhlDOQwiOLUqW7TRV60fw9VHPpTBRXbZEL_4B3s72-9FjoehKwYnS1alwAE-SgyhqelbjrikpzW6N8TZHm6g36NejdoCkfF5b5s0_BUrJv0XXbvxCz_FFoWbm4BCjaNV1L5gBUx9dpOvpgvX6_r3tp1YV3I0N96HWJegS7957M9oCuvee_0vw9Zf7TZM97RDoufDMWwsQmIVmn0fqIE7Pn_jhgRNcQvpP1KOozKzD9-LakSdiY541fuQFy2qgQxOqPMGSMJTG2V4noFBBTj2waGaj7q6DyrOkFIjDl-wgCdWD-mmtQLn_lHzXS99RamS-6fKRYH17T8KZsceozORw-njemJcYNa3QwsyhiefArWWl2iOlOT9teHnXtbWsift2VULWsI8ol9rfbAAAK8TSevdre1_MIRS2Dps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
صحبت های زیبای آرتتا در تحسین پپ گواردیولا پیش از بازی امروز با سیتیزن‌ها
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103865" target="_blank">📅 12:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103864">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mookz1MRHaQpXchPkvUexfP74KEqd7HRT8tRVVO0N04Klr499exjW5ASl42LKCvXQ_qu_hz00BlKmv8sN4ggXwNuz639SpuSXiep4y351c8isijvgwAnQlTgusgRA5BxRgghvTDVTpPsGuzZZMxC7XvglsyW9N1nRRkVFrivOYrOKavi8W3a13I898SaB9K9RIqOOdZGXP-u-W--8gJTFDYkHxT-aYKyuSE9nLSPgaY2xdbnQMdqK3P40QBROnF3gD9cV-iOgW6Vp3CnAFDsfrLYkV9Cvus_cTEz8271PD5PClfT2VzMto6GkRBUUKJaxsKjPilxOqrAmJ2y5V3BUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
❌
ورزشگاه نقش‌جهان اصفهان به عنوان میزبان دربی رفت لیگ‌برتر انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103864" target="_blank">📅 11:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103863">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14206cca0.mp4?token=G7tB1Xk9nZq5HHKZQjUd-3CcaZFrN01bNTpgymQ_v9vDc_i5i2OGWlFgg8UDGn5jJhtRpLrc2d6yndk0cnw853cfPpuuWCEVozOMgP0DLb5qrdb5XnRk2UjQbN-cuiuKsCFzb-hZacDPo8oZbEJTTRND9lH1Jx2VRsqz11J7QxASMzUEvT_-P7Yt4dmlMXCoMyAhKy_ineyayp0Yuh1-KSuD4OebIRIYwJhpWCfB3gCcKn3-qw_v4NjRjqB2EnZ4oMSTtX73PH6-ilJW-PtKPQl5Ic_bEyV6iP8KmokzpQHeiLKS55jpJP6rpuIWhl8n0DOiihyFwpxlEFfo4-knwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14206cca0.mp4?token=G7tB1Xk9nZq5HHKZQjUd-3CcaZFrN01bNTpgymQ_v9vDc_i5i2OGWlFgg8UDGn5jJhtRpLrc2d6yndk0cnw853cfPpuuWCEVozOMgP0DLb5qrdb5XnRk2UjQbN-cuiuKsCFzb-hZacDPo8oZbEJTTRND9lH1Jx2VRsqz11J7QxASMzUEvT_-P7Yt4dmlMXCoMyAhKy_ineyayp0Yuh1-KSuD4OebIRIYwJhpWCfB3gCcKn3-qw_v4NjRjqB2EnZ4oMSTtX73PH6-ilJW-PtKPQl5Ic_bEyV6iP8KmokzpQHeiLKS55jpJP6rpuIWhl8n0DOiihyFwpxlEFfo4-knwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظاتی با درخشش‌های یکی از بهترین لژیونر های تاریخ فوتبال ایران اشکان‌دژاگه
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103863" target="_blank">📅 11:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103862">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f9fca4e0.mp4?token=ZZyzLTHpc3d7zS88FupQfxkluQK9nBYSEWsYX6xH-VP3-NDGXVudzDywx9Hfl0b6_vUQyT6ZOTRYBQPbV43g6Lo10bp2v5FuqUsZ5Tx3pf84WDJ1wm-XFnY4vcwsDBzgYhs4bv1jQtvhlq9DtFBNsAaJkgMi1kco12Wl8a0cC5SKD8C-qXHknlTyu_8FaW2EP4gpEuvMmFk2AwysXifX8CVayATtvqe87TmIDnkVvAThRsIgb-Bv4CaBCP2_sVUnneRkBDVpodT92LqbCNZJPL6GAAek3nf-jn4IUauHZ0jz5k-aQBZHUS02upZBkMH_XqO9CdDITWdDpUrR-3_s9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f9fca4e0.mp4?token=ZZyzLTHpc3d7zS88FupQfxkluQK9nBYSEWsYX6xH-VP3-NDGXVudzDywx9Hfl0b6_vUQyT6ZOTRYBQPbV43g6Lo10bp2v5FuqUsZ5Tx3pf84WDJ1wm-XFnY4vcwsDBzgYhs4bv1jQtvhlq9DtFBNsAaJkgMi1kco12Wl8a0cC5SKD8C-qXHknlTyu_8FaW2EP4gpEuvMmFk2AwysXifX8CVayATtvqe87TmIDnkVvAThRsIgb-Bv4CaBCP2_sVUnneRkBDVpodT92LqbCNZJPL6GAAek3nf-jn4IUauHZ0jz5k-aQBZHUS02upZBkMH_XqO9CdDITWdDpUrR-3_s9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
💥
اجرای جالب و دیدنی هومن حاجی عبداللهی و آرش برهانی، با ساز و دف و تنبک و تار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103862" target="_blank">📅 11:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103861">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🇮🇷
فدراسیون فوتبال برای مشخص‌شدن پرونده فسخ قرارداد یاسر‌آسانی از فیفا استعلام گرفته و بزودی نتیجه این پرونده جنجالی مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103861" target="_blank">📅 11:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103860">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df609bdcd.mp4?token=F0qcuGX_rh7DFgYY7JufA7QCk3Za-cByUhHgN8D474lQIN4-AEAZc6Jb5GN__pCY_duQnw3ezvvlKNzaRENozFXVO6Y0c15-0y1RZn3YJx7vgtnajKZ-0L_nx0sU5Iru_ukeHW1Ity3SqjngBWGD6iHKrakqMuYZyAYbS0Dl0bf7y-rlCvE9QCF8PqolcdlAVClCXibw2kXOpuAnBYTG5B-uubw2JFOzWUgttbHplPcY5P-IH1XklFbbTAwl6oxpNv12YODNAF3833UBRFI6giMJVimp7hlpUrBgM2K18YBHrgnpqrjwbIAm46k450g8oUpy2YUcZavmeFE4c3hEzm1UgaSYroa2XoZCmH9gOpaQaPrpgW1-j_8_SKzUHYf28a875ZTEJd2ed7w6nV0c3sIhS2nQFuOp-Yh2Sz41MKc8Xc-bFgzqVcT3NN-PWIKijIs1nEcbqNucgyw-uIxBECdOIg-eLM3QjBdcDoapyaH-BXx-60TCMTzu-XjjIy4nVRYX8_TX8Pw5My7LTyl3uyXdtTCkjnkgYe2wGKc6g8KwCjHvvp3Sbg17WjgZdhRf8kyLGpb1YM7DidX2TpJneQxcvdt0UyAuX2Ffyd-2gDGoJCspHH4pcgjDR1myL1Zy0Gfz6aB3X-imKGGFmu6IuybWSLY9ngo-b89-DuUBKZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df609bdcd.mp4?token=F0qcuGX_rh7DFgYY7JufA7QCk3Za-cByUhHgN8D474lQIN4-AEAZc6Jb5GN__pCY_duQnw3ezvvlKNzaRENozFXVO6Y0c15-0y1RZn3YJx7vgtnajKZ-0L_nx0sU5Iru_ukeHW1Ity3SqjngBWGD6iHKrakqMuYZyAYbS0Dl0bf7y-rlCvE9QCF8PqolcdlAVClCXibw2kXOpuAnBYTG5B-uubw2JFOzWUgttbHplPcY5P-IH1XklFbbTAwl6oxpNv12YODNAF3833UBRFI6giMJVimp7hlpUrBgM2K18YBHrgnpqrjwbIAm46k450g8oUpy2YUcZavmeFE4c3hEzm1UgaSYroa2XoZCmH9gOpaQaPrpgW1-j_8_SKzUHYf28a875ZTEJd2ed7w6nV0c3sIhS2nQFuOp-Yh2Sz41MKc8Xc-bFgzqVcT3NN-PWIKijIs1nEcbqNucgyw-uIxBECdOIg-eLM3QjBdcDoapyaH-BXx-60TCMTzu-XjjIy4nVRYX8_TX8Pw5My7LTyl3uyXdtTCkjnkgYe2wGKc6g8KwCjHvvp3Sbg17WjgZdhRf8kyLGpb1YM7DidX2TpJneQxcvdt0UyAuX2Ffyd-2gDGoJCspHH4pcgjDR1myL1Zy0Gfz6aB3X-imKGGFmu6IuybWSLY9ngo-b89-DuUBKZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نبرد تاریخی دو اسطوره یونایتد و آرسنال در تقابل‌های مستقیم و خشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103860" target="_blank">📅 11:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103859">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRgu-u_F3W01MPTqXzwhFPvLDvxFlBGLnkRJdTiO7dN0JAAODjagNXRMLrk5ZKupZeQzsgr9wKPPOrpc0t5pHdOjYZnWYFse7lUqVVnS6PrWOFKA4c_vcyMHu2_sR_5-R2gtCabTCTD4LUrzSEL7CmqkT6B4-2MbGszh0W2f1_aYM7a1SODbGBsjWqA13h5FqoIBV54sz7tiHDP5ZYWu-Wsv24DJrYJtUK8TRH-35OjO6E5vZlgDBo32W5ELEr55SYECYbXVjDYnn0VFoOWz79CtIswdjGy9pXZUojR3sNzg1rNqBRHp8oOoGjIeynFBVMVINsb1GVtDmN6NUhcMHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
فدراسیون فوتبال برای مشخص‌شدن پرونده فسخ قرارداد یاسر‌آسانی از فیفا استعلام گرفته و بزودی نتیجه این پرونده جنجالی مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103859" target="_blank">📅 11:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103858">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103858" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103858" target="_blank">📅 11:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103857">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSBfGp9x1WJiR6D711KQW7FPMr6nizxLqwqh3OUHvVZeUVn6X1alwVXy3mvkAvFeBBMOOcwYi0HFlTJxiIDjwJHnGwljnQKuv9vpDv8WK6i7TQFWC15X1qQ0CvnUH9Rn7oFAksTdYReFIzbVkYjBQeIzY1zeU3VnREI-4GTuhp0JGYdgnUrERjSP1rxdVaT3nn0k7u0nB5Ax1mokOvM5mICYlrVoyuNIHbOGwD43MessyDb8xjCHQ6A4JZWyQBWouQVK94gdCMSNV2pYCTdOhav4dAIW_WKqVtWYGbCd0hDxES_ZSCG2KdrsZ1SKtXE_hHS4BXyRn6fNSiR6qI6cqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r25
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103857" target="_blank">📅 11:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103856">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9fcc1320.mp4?token=mfs5az_5ka1o1BHK8S2Dl-Frrs-fnAlMlg4lZAuyBZa4mR8rYKtKwc8fHoZv7iCP3a5VVClsumq-IiEx_r8WcuFPgoBfi4ibBvgG-OGWIP4mBsR-pQTndbrvjV57NaFZr2r139fVQNCfZg9u7gYQNutSzmi1ckE4eDUqTlLabHBJ_R-ahliYS7vyY-QKHukE9913YkxEVmb7RewaYqQHfDTc6nRmujwxh3vGmkcTUiRFFr5rs5MW_bFfqD953Uv_BiSKQKrK9lDyiE8qxVDjd0usMtdHWuqPJKgAwC0uEqFhjm12G7GEAm3ydg1YmFg_VgXQdsartSHYzE9Gw3_6wQ0aisYM-gjh7KL-dhrf-eMp42n_UfDXMIEKMc0wAagl4lGm0j3lGfvFn_X09mgfTkYoUb5ecLhQfCtIrGWewEX2x4dQs64N3JnACkPRvqJF1J2PLRnjs-MSUzVdD10ndQPflS-5FCjsf9jATb5jcgSRx0wRS8EuJNGMmroN8ji7DKcKzQd4viqR3aaFaJyWgKdhbwRi1tqzPOCcGESVwNSSwdAKysT4EaKtlYdITTRnaW_n9QM026ONNpjYmbmCfRCpxJC6m6OEPSwy6ZsaBzY-MfdDAs5QuSDVx8nLkwqdMBuurZktpdFufmHFSk26DT1ktf7tlC3fzyxKlacJd3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9fcc1320.mp4?token=mfs5az_5ka1o1BHK8S2Dl-Frrs-fnAlMlg4lZAuyBZa4mR8rYKtKwc8fHoZv7iCP3a5VVClsumq-IiEx_r8WcuFPgoBfi4ibBvgG-OGWIP4mBsR-pQTndbrvjV57NaFZr2r139fVQNCfZg9u7gYQNutSzmi1ckE4eDUqTlLabHBJ_R-ahliYS7vyY-QKHukE9913YkxEVmb7RewaYqQHfDTc6nRmujwxh3vGmkcTUiRFFr5rs5MW_bFfqD953Uv_BiSKQKrK9lDyiE8qxVDjd0usMtdHWuqPJKgAwC0uEqFhjm12G7GEAm3ydg1YmFg_VgXQdsartSHYzE9Gw3_6wQ0aisYM-gjh7KL-dhrf-eMp42n_UfDXMIEKMc0wAagl4lGm0j3lGfvFn_X09mgfTkYoUb5ecLhQfCtIrGWewEX2x4dQs64N3JnACkPRvqJF1J2PLRnjs-MSUzVdD10ndQPflS-5FCjsf9jATb5jcgSRx0wRS8EuJNGMmroN8ji7DKcKzQd4viqR3aaFaJyWgKdhbwRi1tqzPOCcGESVwNSSwdAKysT4EaKtlYdITTRnaW_n9QM026ONNpjYmbmCfRCpxJC6m6OEPSwy6ZsaBzY-MfdDAs5QuSDVx8nLkwqdMBuurZktpdFufmHFSk26DT1ktf7tlC3fzyxKlacJd3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
این‌هم تصویر اون خانومی که پشت تلفن موقع زنگ زدن میگه "مشترک مورد نظر در دسترس نمیباشد"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103856" target="_blank">📅 10:40 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
